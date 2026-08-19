#!/usr/bin/env python3
"""Validate exact runtime token usage and summarize token-only cost by agent and model."""

from __future__ import annotations

import argparse
import csv
import json
import re
import tomllib
from collections import defaultdict
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any


FIELDS = (
    "record_id",
    "agent_id",
    "role",
    "model",
    "service_tier",
    "context_class",
    "price_multiplier",
    "input_tokens",
    "cached_input_tokens",
    "cache_write_tokens",
    "output_tokens",
    "reasoning_tokens",
    "total_tokens",
    "usage_source",
    "status",
)
TOKEN_FIELDS = (
    "input_tokens",
    "cached_input_tokens",
    "cache_write_tokens",
    "output_tokens",
    "reasoning_tokens",
    "total_tokens",
)
ALLOWED_STATUS = {"EXACT", "TOTALS_ONLY", "UNAVAILABLE"}
ALLOWED_CONTEXT = {"SHORT", "LONG"}
TIER_ALIASES = {"PRIORITY": "FAST"}
PLACEHOLDER = re.compile(r"^(?:__|unknown|todo|tbd|n/a|none)?$", re.IGNORECASE)
USD_QUANTUM = Decimal("0.000001")


@dataclass(frozen=True)
class Rate:
    input: Decimal
    cached: Decimal
    cache_write: Decimal
    output: Decimal


def money(value: Decimal) -> str:
    return str(value.quantize(USD_QUANTUM, rounding=ROUND_HALF_UP))


def parse_nonnegative_int(value: str, label: str, errors: list[str]) -> int:
    try:
        parsed = int(value)
    except ValueError:
        errors.append(f"{label} must be a nonnegative integer, got {value!r}.")
        return 0
    if parsed < 0:
        errors.append(f"{label} must be nonnegative, got {parsed}.")
        return 0
    return parsed


def parse_multiplier(value: str, label: str, errors: list[str]) -> Decimal:
    try:
        parsed = Decimal(value)
    except InvalidOperation:
        errors.append(f"{label} must be a positive decimal, got {value!r}.")
        return Decimal(1)
    if not parsed.is_finite() or parsed <= 0:
        errors.append(f"{label} must be a positive finite decimal, got {value!r}.")
        return Decimal(1)
    return parsed


def read_pricing(path: Path) -> tuple[dict[str, Any], dict[tuple[str, str, str], Rate]]:
    with path.open("rb") as handle:
        raw = tomllib.load(handle)
    required = {
        "schema_version",
        "as_of_utc",
        "currency",
        "unit_tokens",
        "source_url",
        "estimate_label",
        "long_context_threshold_input_tokens",
        "rates",
    }
    missing = sorted(required - set(raw))
    if missing:
        raise ValueError(f"Pricing snapshot lacks fields: {', '.join(missing)}")
    if raw["currency"] != "USD" or raw["unit_tokens"] != 1_000_000:
        raise ValueError("Pricing snapshot must use USD per 1,000,000 tokens.")
    rates: dict[tuple[str, str, str], Rate] = {}
    for index, item in enumerate(raw["rates"], start=1):
        key = (
            str(item["model"]),
            str(item["service_tier"]).upper(),
            str(item["context_class"]).upper(),
        )
        if key in rates:
            raise ValueError(f"Duplicate pricing rate at item {index}: {key}")
        try:
            rates[key] = Rate(
                input=Decimal(str(item["input_per_million"])),
                cached=Decimal(str(item["cached_input_per_million"])),
                cache_write=Decimal(str(item["cache_write_per_million"])),
                output=Decimal(str(item["output_per_million"])),
            )
        except (KeyError, InvalidOperation) as error:
            raise ValueError(f"Malformed pricing rate at item {index}: {error}") from error
    return raw, rates


def empty_totals() -> dict[str, Any]:
    return {
        "exact_records": 0,
        "totals_only_records": 0,
        "unavailable_records": 0,
        "unpriced_records": 0,
        **{field: 0 for field in TOKEN_FIELDS},
        "known_token_cost_usd": Decimal(0),
    }


def add_totals(
    target: dict[str, Any],
    tokens: dict[str, int],
    cost: Decimal,
    record_kind: str,
    *,
    unpriced: bool = False,
) -> None:
    target[record_kind] += 1
    if unpriced:
        target["unpriced_records"] += 1
    for field in TOKEN_FIELDS:
        target[field] += tokens[field]
    target["known_token_cost_usd"] += cost


def serial_totals(value: dict[str, Any]) -> dict[str, Any]:
    count_complete = value["unavailable_records"] == 0
    price_complete = (
        count_complete
        and value["totals_only_records"] == 0
        and value["unpriced_records"] == 0
    )
    result = {
        key: item
        for key, item in value.items()
        if key != "known_token_cost_usd"
    }
    result["known_token_cost_usd"] = money(value["known_token_cost_usd"])
    result["estimated_total_token_cost_usd"] = (
        money(value["known_token_cost_usd"]) if price_complete else None
    )
    result["total_token_count_status"] = "COMPLETE" if count_complete else "INCOMPLETE"
    if value["unavailable_records"]:
        result["status"] = "INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE"
    elif value["totals_only_records"]:
        result["status"] = "INCOMPLETE_BILLING_BREAKDOWN"
    elif value["unpriced_records"]:
        result["status"] = "INCOMPLETE_PRICE_UNAVAILABLE"
    else:
        result["status"] = "COMPLETE"
    return result


def calculate(
    ledger_path: Path, pricing_path: Path
) -> tuple[dict[str, Any], list[str]]:
    pricing, rates = read_pricing(pricing_path)
    errors: list[str] = []
    agent_totals: dict[str, dict[str, Any]] = defaultdict(empty_totals)
    model_totals: dict[str, dict[str, Any]] = defaultdict(empty_totals)
    package_totals = empty_totals()
    agent_meta: dict[str, dict[str, str]] = {}
    seen_records: set[str] = set()
    seen_sources: set[str] = set()

    with ledger_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError(
                "Token ledger header must exactly equal: " + ",".join(FIELDS)
            )
        rows = list(reader)
    if not rows:
        raise ValueError("Token usage ledger has no data rows.")

    threshold = int(pricing["long_context_threshold_input_tokens"])
    for line, row in enumerate(rows, start=2):
        prefix = f"token ledger line {line}"
        record_id = row["record_id"].strip()
        agent_id = row["agent_id"].strip()
        role = row["role"].strip()
        model = row["model"].strip()
        status = row["status"].strip().upper()
        usage_source = row["usage_source"].strip()
        if PLACEHOLDER.fullmatch(record_id):
            errors.append(f"{prefix} has a missing or placeholder record_id.")
        elif record_id in seen_records:
            errors.append(f"{prefix} duplicates record_id {record_id!r}.")
        seen_records.add(record_id)
        for name, value in (("agent_id", agent_id), ("role", role), ("model", model)):
            if PLACEHOLDER.fullmatch(value):
                errors.append(f"{prefix} has a missing or placeholder {name}.")
        if status not in ALLOWED_STATUS:
            errors.append(f"{prefix} status must be EXACT, TOTALS_ONLY, or UNAVAILABLE.")
            status = "UNAVAILABLE"

        prior = agent_meta.setdefault(agent_id, {"role": role, "model": model})
        if prior != {"role": role, "model": model}:
            errors.append(f"{prefix} changes role or model for agent {agent_id!r}.")

        if status == "UNAVAILABLE":
            if any(row[field].strip() != "__" for field in TOKEN_FIELDS):
                errors.append(f"{prefix} UNAVAILABLE rows require __ in every token field.")
            if usage_source in {"", "__"}:
                errors.append(f"{prefix} must name why authoritative usage is unavailable.")
            agent_totals[agent_id]["unavailable_records"] += 1
            model_totals[model]["unavailable_records"] += 1
            package_totals["unavailable_records"] += 1
            continue

        if status == "TOTALS_ONLY":
            for field in (
                "service_tier",
                "context_class",
                "price_multiplier",
                "cached_input_tokens",
                "cache_write_tokens",
                "reasoning_tokens",
            ):
                if row[field].strip() != "__":
                    errors.append(f"{prefix} TOTALS_ONLY requires __ in {field}.")
            if usage_source in {"", "__"}:
                errors.append(f"{prefix} TOTALS_ONLY row lacks an authoritative usage_source.")
            elif usage_source in seen_sources:
                errors.append(f"{prefix} duplicates usage_source {usage_source!r}; possible double count.")
            seen_sources.add(usage_source)
            tokens = {
                "input_tokens": parse_nonnegative_int(
                    row["input_tokens"].strip(), f"{prefix} input_tokens", errors
                ),
                "cached_input_tokens": 0,
                "cache_write_tokens": 0,
                "output_tokens": parse_nonnegative_int(
                    row["output_tokens"].strip(), f"{prefix} output_tokens", errors
                ),
                "reasoning_tokens": 0,
                "total_tokens": parse_nonnegative_int(
                    row["total_tokens"].strip(), f"{prefix} total_tokens", errors
                ),
            }
            if tokens["total_tokens"] != tokens["input_tokens"] + tokens["output_tokens"]:
                errors.append(f"{prefix} total_tokens must equal input_tokens plus output_tokens.")
            for target in (agent_totals[agent_id], model_totals[model], package_totals):
                add_totals(target, tokens, Decimal(0), "totals_only_records")
            continue

        tier = TIER_ALIASES.get(row["service_tier"].strip().upper(), row["service_tier"].strip().upper())
        context = row["context_class"].strip().upper()
        multiplier = parse_multiplier(row["price_multiplier"].strip(), f"{prefix} price_multiplier", errors)
        if context not in ALLOWED_CONTEXT:
            errors.append(f"{prefix} context_class must be SHORT or LONG.")
        if usage_source in {"", "__"}:
            errors.append(f"{prefix} EXACT row lacks an authoritative usage_source.")
        elif usage_source in seen_sources:
            errors.append(f"{prefix} duplicates usage_source {usage_source!r}; possible double count.")
        seen_sources.add(usage_source)
        tokens = {
            field: parse_nonnegative_int(row[field].strip(), f"{prefix} {field}", errors)
            for field in TOKEN_FIELDS
        }
        if tokens["cached_input_tokens"] + tokens["cache_write_tokens"] > tokens["input_tokens"]:
            errors.append(f"{prefix} cached plus cache-write tokens exceed input_tokens.")
        if tokens["reasoning_tokens"] > tokens["output_tokens"]:
            errors.append(f"{prefix} reasoning_tokens exceed output_tokens.")
        if tokens["total_tokens"] != tokens["input_tokens"] + tokens["output_tokens"]:
            errors.append(f"{prefix} total_tokens must equal input_tokens plus output_tokens.")
        expected_context = "LONG" if tokens["input_tokens"] > threshold else "SHORT"
        if context in ALLOWED_CONTEXT and context != expected_context:
            errors.append(
                f"{prefix} context_class must be {expected_context} for request input_tokens "
                f"{tokens['input_tokens']}."
            )
        rate = rates.get((model, tier, context))
        unpriced = rate is None
        if rate is None:
            if not bool(pricing.get("allow_missing_rates", False)):
                errors.append(f"{prefix} has no price rate for {model}/{tier}/{context}.")
            cost = Decimal(0)
        else:
            uncached = (
                tokens["input_tokens"]
                - tokens["cached_input_tokens"]
                - tokens["cache_write_tokens"]
            )
            numerator = (
                Decimal(uncached) * rate.input
                + Decimal(tokens["cached_input_tokens"]) * rate.cached
                + Decimal(tokens["cache_write_tokens"]) * rate.cache_write
                + Decimal(tokens["output_tokens"]) * rate.output
            )
            cost = numerator * multiplier / Decimal(pricing["unit_tokens"])
        add_totals(agent_totals[agent_id], tokens, cost, "exact_records", unpriced=unpriced)
        add_totals(model_totals[model], tokens, cost, "exact_records", unpriced=unpriced)
        add_totals(package_totals, tokens, cost, "exact_records", unpriced=unpriced)

    agents = []
    for agent_id in sorted(agent_totals):
        agents.append({"agent_id": agent_id, **agent_meta[agent_id], **serial_totals(agent_totals[agent_id])})
    models = []
    for model in sorted(model_totals):
        agent_count = sum(1 for meta in agent_meta.values() if meta["model"] == model)
        models.append({"model": model, "agent_count": agent_count, **serial_totals(model_totals[model])})
    package = serial_totals(package_totals)
    result = {
        "schema_version": 1,
        "status": "FAIL" if errors else package["status"],
        "accounting_basis": pricing["estimate_label"],
        "pricing_as_of_utc": pricing["as_of_utc"],
        "pricing_source": pricing["source_url"],
        "currency": pricing["currency"],
        "agent_count": len(agents),
        "model_count": len(models),
        "agents": agents,
        "models": models,
        "package": package,
        "errors": errors,
    }
    return result, errors


def markdown(result: dict[str, Any]) -> str:
    package = result["package"]
    lines = [
        "# Token Usage and Token-Only Cost Summary",
        "",
        f"- **Accounting status:** {result['status']}",
        f"- **Total-token count status:** {package['total_token_count_status']}",
        f"- **Accounting basis:** {result['accounting_basis']}",
        f"- **Pricing as of UTC:** {result['pricing_as_of_utc']}",
        f"- **Pricing source:** {result['pricing_source']}",
        f"- **Known token cost (USD):** {package['known_token_cost_usd']}",
        "- **Estimated complete token cost (USD):** "
        + (package["estimated_total_token_cost_usd"] or "__"),
        "",
        "Cached-input and cache-write tokens are subsets of input tokens. Reasoning tokens are a subset "
        "of output tokens. They are shown for auditability and are not added again to total tokens. "
        "Totals-only rows retain authoritative input/output/total counts when billing breakdowns are "
        "missing. Unpriced rows retain exact token details when a dynamic route has no configured "
        "resolved-model rate. Amounts exclude non-token charges and are not an invoice.",
        "",
        "## By agent",
        "",
        "| Agent ID | Role | Model | Exact records | Unpriced records | Totals-only records | Unavailable records | Input | Known cached input | Known cache writes | Output | Known reasoning | Total | Known cost USD | Complete estimated cost USD | Status |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in result["agents"]:
        lines.append(
            "| {agent_id} | {role} | {model} | {exact_records} | {unpriced_records} | {totals_only_records} | {unavailable_records} | "
            "{input_tokens} | {cached_input_tokens} | {cache_write_tokens} | {output_tokens} | "
            "{reasoning_tokens} | {total_tokens} | {known_token_cost_usd} | {estimated} | {status} |".format(
                **row, estimated=row["estimated_total_token_cost_usd"] or "__"
            )
        )
    lines.extend(
        [
            "",
            "## By model",
            "",
            "| Model | Agents | Exact records | Unpriced records | Totals-only records | Unavailable records | Input | Known cached input | Known cache writes | Output | Known reasoning | Total | Known cost USD | Complete estimated cost USD | Status |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in result["models"]:
        lines.append(
            "| {model} | {agent_count} | {exact_records} | {unpriced_records} | {totals_only_records} | {unavailable_records} | {input_tokens} | "
            "{cached_input_tokens} | {cache_write_tokens} | {output_tokens} | {reasoning_tokens} | "
            "{total_tokens} | {known_token_cost_usd} | {estimated} | {status} |".format(
                **row, estimated=row["estimated_total_token_cost_usd"] or "__"
            )
        )
    lines.extend(
        [
            "",
            "## Package total",
            "",
            f"- **Total-token count status:** {package['total_token_count_status']}",
            f"- **Input tokens:** {package['input_tokens']}",
            f"- **Cached input tokens (subset):** {package['cached_input_tokens']}",
            f"- **Cache-write tokens (subset):** {package['cache_write_tokens']}",
            f"- **Output tokens:** {package['output_tokens']}",
            f"- **Reasoning tokens (subset):** {package['reasoning_tokens']}",
            f"- **Total tokens:** {package['total_tokens']}",
            f"- **Known token cost (USD):** {package['known_token_cost_usd']}",
            "- **Estimated complete token cost (USD):** "
            + (package["estimated_total_token_cost_usd"] or "__"),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--pricing", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    try:
        result, errors = calculate(args.ledger, args.pricing)
    except (OSError, ValueError, tomllib.TOMLDecodeError) as error:
        raise SystemExit(f"Token accounting failed: {error}") from error
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text(markdown(result), encoding="utf-8")
    args.json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
