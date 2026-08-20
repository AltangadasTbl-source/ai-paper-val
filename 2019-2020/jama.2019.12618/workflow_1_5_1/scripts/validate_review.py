#!/usr/bin/env python3
"""Validate workflow 1.5 coverage, agent provenance, reports, timing, and integrity."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from calculate_token_cost import calculate as calculate_token_cost
from calculate_token_cost import markdown as token_cost_markdown


REQUIRED_COMMON = (
    "run_state.md",
    "source_inventory.md",
    "source_hashes_before.sha256",
    "evidence_asset_inventory.md",
    "source_coverage.md",
    "coverage_manifest.md",
    "agent_execution_manifest.md",
    "token_usage_ledger.csv",
    "token_usage_summary.md",
    "token_usage_summary.json",
    "extraction/main_quantitative_evidence.md",
    "extraction/support_quantitative_evidence.md",
    "relationships/numeric_relationship_inventory.md",
    "statistics/relationship_inventory.md",
    "checkers/numeric_consistency.md",
    "checkers/statistical_pass_1.md",
    "checkers/cross_source_consistency.md",
    "checkers/statistical_pass_2.md",
    "candidate_ledger.md",
    "verification/evidence_recheck.md",
    "quality/evidence_quality_audit.md",
    "limitations.md",
)
REQUIRED_STAGES = (
    "source_inventory",
    "evidence_assets",
    "main_evidence_mapping",
    "support_evidence_mapping",
    "numeric_checks",
    "statistics_pass_1",
    "cross_source_checks",
    "candidate_registration",
    "evidence_recheck",
    "statistics_pass_2",
    "evidence_quality",
    "report_generation",
)
CARD_FIELDS = (
    "**Candidate statement:**",
    "**Category:**",
    "**Exact source locations:**",
    "**Source evidence:**",
    "**Reported-versus-comparator:**",
    "**Reasoning procedure:**",
    "**Calculation:**",
    "**Alternative source-grounded interpretations:**",
    "**Mechanical evidence recheck:**",
    "**Quality-control relevance:**",
    "**Potential downstream evidence impact:**",
    "**Human verification steps:**",
    "**Human adjudication fields:**",
)
ALLOWED_CATEGORIES = (
    "Numeric or arithmetic inconsistency",
    "Denominator, proportion, or total inconsistency",
    "Statistical reporting inconsistency",
    "Cross-document numeric inconsistency",
    "Measure, label, or scale inconsistency",
    "Rate-versus-count inconsistency",
    "Analysis-unit or population inconsistency",
)
SOURCE_SUFFIXES = (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".csv")
WORKBOOK_SUFFIXES = (".xls", ".xlsx")
DOC_SUFFIXES = (".doc", ".docx")
CANDIDATE_HEADING = re.compile(r"^##\s+(C\d{3,})\s+[—-]", re.MULTILINE)
STAT_RELATIONSHIP = re.compile(r"\bS\d{3,}\b")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\((?:<)?([^)>]+)(?:>)?\)")
HASH_LINE = re.compile(r"^([0-9a-fA-F]{64})\s+[*]?(.+?)\s*$")
FORBIDDEN_ADJUDICATION = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:severity|disposition|evidence status)"
    r"(?:\*\*)?\s*:\s*\S+",
    re.IGNORECASE | re.MULTILINE,
)
COUNT_CAP_LANGUAGE = re.compile(
    r"\b(?:top[- ]?10|at most 10|maximum of 10|deferred_by_review_cap)\b", re.IGNORECASE
)
P_ZERO_REFERENCE = re.compile(
    r"(?:\bP(?:\s*[- ]?value)?\s*=\s*0(?:\.0+)?(?![\d.])"
    r"|\bP(?:\s*[- ]?value)?\s+(?:of|is)\s+(?:literal\s+)?zero\b)",
    re.IGNORECASE,
)
P_ZERO_INDEPENDENT_LABEL = "**Independent contradiction beyond P=0 display:**"
EMPTY_CANDIDATE_NOTICE = "No stable candidates were identified"
CJK_TEXT = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
PERFORMANCE_LABELS = (
    "Target basis",
    "Total source units",
    "Fresh-source units",
    "Target elapsed minutes",
    "Started UTC",
    "Finished UTC",
    "Observed elapsed minutes",
    "Target status",
    "Exceedance causes",
)
TARGET_RANGE = re.compile(r"^([1-9]\d*)-([1-9]\d*)$")
PLAIN_ARTIFACT_PATH = re.compile(
    r"^(?:\.\./)?[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*$"
)
STAT_AGENT_ARTIFACTS = {
    "statistics_pass_1": "checkers/statistical_pass_1.md",
    "statistics_pass_2": "checkers/statistical_pass_2.md",
}


class ReportHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.has_toc = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "nav" and values.get("id") == "TOC":
            self.has_toc = True
        if tag == "a" and values.get("href"):
            self.hrefs.append(str(values["href"]))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inside(root: Path, path: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def candidate_sections(markdown: str) -> tuple[list[str], dict[str, str]]:
    matches = list(CANDIDATE_HEADING.finditer(markdown))
    ids = [match.group(1) for match in matches]
    sections = {
        match.group(1): markdown[
            match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        ]
        for index, match in enumerate(matches)
    }
    return ids, sections


def parse_hash_file(path: Path, package: Path, errors: list[str]) -> dict[str, str]:
    entries: dict[str, str] = {}
    for number, raw in enumerate(read(path).splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = HASH_LINE.fullmatch(line)
        if not match:
            errors.append(f"Malformed SHA-256 line in {path.name}:{number}")
            continue
        relative = match.group(2)
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts:
            errors.append(f"Hash path must be package-relative without '..': {relative}")
            continue
        resolved = (package / candidate).resolve()
        if not inside(package, resolved):
            errors.append(f"Hash path escapes package: {relative}")
            continue
        normalized = candidate.as_posix()
        if normalized in entries:
            errors.append(f"Duplicate hash path in {path.name}: {relative}")
            continue
        entries[normalized] = match.group(1).casefold()
    return entries


def verify_hashes(
    label: str, entries: dict[str, str], package: Path, errors: list[str]
) -> None:
    if not entries:
        errors.append(f"{label} hash inventory is empty.")
        return
    for relative, expected in entries.items():
        target = (package / relative).resolve()
        if not target.is_file():
            errors.append(f"{label} file is missing: {relative}")
        elif sha256(target) != expected:
            errors.append(f"{label} integrity failure: {relative}")


def validate_local_link(report_dir: Path, package: Path, href: str) -> str | None:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        return f"external or absolute link is forbidden: {href}"
    if not parsed.path:
        return None
    decoded = unquote(parsed.path)
    target = (report_dir / decoded).resolve()
    if not inside(package, target):
        return f"link escapes the paper package: {href}"
    if not target.is_file():
        return f"local evidence target does not exist: {href}"
    suffix = target.suffix.casefold()
    if suffix == ".pdf" and not re.fullmatch(r"page=[1-9]\d*", parsed.fragment, re.IGNORECASE):
        return f"PDF evidence link must end in #page=N: {href}"
    return None


def has_truthful_structural_location(section: str, suffixes: set[str]) -> bool:
    if suffixes & set(WORKBOOK_SUFFIXES):
        if not (
            re.search(r"\bworksheet\b", section, re.IGNORECASE)
            and re.search(r"\bcells?\b", section, re.IGNORECASE)
        ):
            return False
    if suffixes & set(DOC_SUFFIXES):
        if not re.search(
            r"\b(?:P\d{4}|T\d{3}\s+R\d{3}\s+C\d{3}|paragraph|table)\b",
            section,
            re.IGNORECASE,
        ):
            return False
    if ".csv" in suffixes:
        if not (
            re.search(r"\brow\b", section, re.IGNORECASE)
            and re.search(r"\b(?:column|C\d+)\b", section, re.IGNORECASE)
        ):
            return False
    return True


def human_fields_are_blank(section: str) -> bool:
    marker = "**Human adjudication fields:**"
    tail = section.split(marker, 1)[1] if marker in section else ""
    tail = re.split(r"^##\s+", tail, maxsplit=1, flags=re.MULTILINE)[0]
    pattern = re.compile(
        r"^-\s+\*\*(Validity|Importance|Action|Initials|Notes):\*\*\s+(\S.*)$",
        re.MULTILINE,
    )
    values = pattern.findall(tail)
    expected = {"Validity", "Importance", "Action", "Initials", "Notes"}
    return len(values) == 5 and {label for label, _ in values} == expected and all(
        value.strip() == "__" for _, value in values
    )


def p_zero_has_independent_contradiction(section: str) -> bool:
    if not P_ZERO_REFERENCE.search(section):
        return True
    match = re.search(
        rf"^{re.escape(P_ZERO_INDEPENDENT_LABEL)}\s*(\S.*)$",
        section,
        re.MULTILINE,
    )
    if not match:
        return False
    value = match.group(1).strip()
    if len(value) < 25:
        return False
    return not re.match(
        r"(?:none|n/a|not applicable|finite precision|rounding|underflow|display(?: only)?|"
        r"very small|exact p cannot|positive tail)",
        value,
        re.IGNORECASE,
    )


def performance_fields(text: str, label: str, errors: list[str]) -> dict[str, str]:
    values: dict[str, str] = {}
    for field in PERFORMANCE_LABELS:
        match = re.search(
            rf"^-\s+\*\*{re.escape(field)}:\*\*\s*(\S.*)$",
            text,
            re.MULTILINE,
        )
        if not match:
            errors.append(f"{label} lacks performance field: {field}")
        else:
            values[field] = match.group(1).strip()
    return values


def validate_performance(
    run_state: str,
    report: str,
    source_units: int,
    fresh_units: int,
    errors: list[str],
) -> tuple[float | None, str | None, str | None]:
    state = performance_fields(run_state, "run_state.md", errors)
    report_values = performance_fields(report, "Markdown report", errors)
    if state and report_values and state != report_values:
        errors.append("Performance metadata differs between run_state.md and the Markdown report.")

    for field, expected in (
        ("Total source units", source_units),
        ("Fresh-source units", fresh_units),
    ):
        try:
            actual = int(state.get(field, ""))
        except ValueError:
            errors.append(f"{field} must be an integer.")
        else:
            if actual != expected:
                errors.append(f"{field} must equal source_coverage.md: {expected}.")

    basis = state.get("Target basis", "").strip()
    if len(basis) < 20 or re.search(
        r"(?:placeholder|unknown|todo|tbd|n/a|not applicable)", basis, re.IGNORECASE
    ):
        errors.append("Target basis must be a bounded package-specific explanation.")

    target_minutes = state.get("Target elapsed minutes", "")
    target_match = TARGET_RANGE.fullmatch(target_minutes)
    upper_bound = 0
    if not target_match:
        errors.append("Target elapsed minutes must be a positive whole-minute MIN-MAX range.")
    else:
        lower_bound, upper_bound = map(int, target_match.groups())
        if lower_bound >= upper_bound:
            errors.append("Target elapsed minutes must have a lower bound below its upper bound.")

    observed: float | None = None
    try:
        observed = float(state.get("Observed elapsed minutes", ""))
        if observed < 0:
            raise ValueError
    except ValueError:
        errors.append("Observed elapsed minutes must be a nonnegative number.")

    started = finished = None
    for key in ("Started UTC", "Finished UTC"):
        raw = state.get(key, "")
        try:
            parsed = dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
            if parsed.tzinfo is None or parsed.utcoffset() != dt.timedelta(0):
                raise ValueError
        except ValueError:
            errors.append(f"{key} must be an ISO-8601 UTC timestamp ending in Z.")
            continue
        if not raw.endswith("Z"):
            errors.append(f"{key} must end in Z.")
        if key == "Started UTC":
            started = parsed
        else:
            finished = parsed
    if started and finished:
        elapsed = (finished - started).total_seconds() / 60
        if elapsed < 0:
            errors.append("Finished UTC precedes Started UTC.")
        elif observed is not None and abs(elapsed - observed) > 1.0:
            errors.append(
                "Observed elapsed minutes differs from the UTC timestamps by more than one minute."
            )

    expected_status = None if observed is None or upper_bound <= 0 else (
        "MET_TARGET" if observed <= upper_bound else "EXCEEDED_TARGET"
    )
    status = state.get("Target status")
    if expected_status and status != expected_status:
        errors.append(f"Target status must be {expected_status} for observed time {observed}.")
    causes = state.get("Exceedance causes", "")
    if status == "EXCEEDED_TARGET" and causes.casefold() in {"", "none", "n/a", "not applicable"}:
        errors.append("An exceeded target requires bounded exceedance causes.")
    return observed, status, target_minutes if target_match else None


def validate_source_coverage(
    text: str,
    profile: str,
    direct_sources: set[str],
    errors: list[str],
) -> tuple[int, int]:
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    total_sum = 0
    fresh_sum = 0
    data_rows = 0
    for number, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 8 or cells[0] in {"Source ID", "---"}:
            continue
        source_id, source_path, unit_type, total_raw, reused_raw, fresh_raw, mapped_raw, status = cells
        data_rows += 1
        if not source_id or source_id in seen_ids:
            errors.append(f"Duplicate or empty source-coverage ID on line {number}: {source_id}")
        seen_ids.add(source_id)
        if not unit_type:
            errors.append(f"Source coverage lacks a unit type on line {number}.")
        if source_path in seen_paths:
            errors.append(f"Source coverage has duplicate source path: {source_path}")
        seen_paths.add(source_path)
        try:
            total, reused, fresh, mapped = map(
                int, (total_raw, reused_raw, fresh_raw, mapped_raw)
            )
        except ValueError:
            errors.append(f"Source-coverage counts must be integers on line {number}.")
            continue
        if total < 1 or min(reused, fresh, mapped) < 0:
            errors.append(f"Source-coverage counts are out of range on line {number}.")
        if profile == "1.5.1" and reused + fresh != total:
            errors.append(
                f"Reuse plus fresh-required units must equal total units for {source_path}."
            )
        if profile == "1.5.2" and (reused != 0 or fresh != total):
            errors.append(
                f"Workflow 1.5.2 requires zero reuse and full fresh coverage for {source_path}."
            )
        if mapped != total:
            errors.append(f"Mapped units must equal total units for {source_path}.")
        if status != "COMPLETE":
            errors.append(f"Source-coverage row is not COMPLETE: {source_path}={status}")
        total_sum += total
        fresh_sum += fresh
    if not data_rows:
        errors.append("source_coverage.md has no valid source rows.")
    if seen_paths != direct_sources:
        errors.append(
            "Source coverage must contain exactly one row per direct source: "
            f"expected={sorted(direct_sources)} recorded={sorted(seen_paths)}"
        )
    return total_sum, fresh_sum


def validate_agent_execution_manifest(
    text: str, run_dir: Path, errors: list[str]
) -> dict[str, tuple[str, str, str, str, str]]:
    agents: dict[str, tuple[str, str, str, str, str]] = {}
    statistics: dict[str, tuple[str, str, str, str, str]] = {}
    coordinator_ids: list[str] = []
    for number, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 6 or cells[0] in {"Stage", "---"}:
            continue
        stage, agent_id, model, effort, start_mode, artifact = cells
        if any(not value for value in (stage, model, effort, start_mode, artifact)):
            errors.append(f"Agent execution line {number} has an empty required field.")
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/-]{2,}", agent_id) or re.search(
            r"(?:runtime-id|agent-id|placeholder|unknown|todo|n/a)", agent_id, re.IGNORECASE
        ):
            errors.append(f"Agent execution line {number} has a missing or placeholder runtime ID.")
        if agent_id in agents:
            errors.append(f"Duplicate agent execution row for runtime ID: {agent_id}")
            continue
        agents[agent_id] = (stage, model, effort, start_mode, artifact)
        if not PLAIN_ARTIFACT_PATH.fullmatch(artifact):
            errors.append(f"Agent execution has invalid artifact path on line {number}.")
        else:
            target = (run_dir / artifact).resolve()
            if not inside(run_dir, target):
                errors.append(f"Agent execution artifact escapes the review directory: {artifact}")
            elif not target.is_file() or target.stat().st_size == 0:
                errors.append(f"Agent execution artifact is missing or empty: {artifact}")
        if stage == "coordinator":
            coordinator_ids.append(agent_id)
            if model != "gpt-5.6-sol" or effort != "high" or start_mode != "CURRENT_SESSION":
                errors.append(
                    "The coordinator execution must record "
                    "gpt-5.6-sol/high/CURRENT_SESSION."
                )
            if artifact != "run_state.md":
                errors.append("The coordinator execution artifact must be exactly run_state.md.")
        if stage in STAT_AGENT_ARTIFACTS:
            if stage in statistics:
                errors.append(f"Duplicate statistical execution row: {stage}")
            statistics[stage] = (agent_id, model, effort, start_mode, artifact)
    if not agents:
        errors.append("agent_execution_manifest.md has no agent rows.")
    if len(coordinator_ids) != 1:
        errors.append("Agent execution manifest must contain exactly one coordinator row.")
    for stage, expected_artifact in STAT_AGENT_ARTIFACTS.items():
        if stage not in statistics:
            errors.append(f"Missing fresh statistical execution row: {stage}")
            continue
        agent_id, model, effort, start_mode, artifact = statistics[stage]
        if model != "gpt-5.6-terra" or effort != "high" or start_mode != "FRESH_SPAWN":
            errors.append(
                f"{stage} must record gpt-5.6-terra/high/FRESH_SPAWN, got "
                f"{model}/{effort}/{start_mode}."
            )
        if artifact != expected_artifact:
            errors.append(f"{stage} artifact must be exactly {expected_artifact}.")
    ids = [record[0] for record in statistics.values() if record[0]]
    if len(ids) == 2 and len(set(ids)) != 2:
        errors.append("Statistical passes 1 and 2 must use distinct fresh runtime agent IDs.")
    return agents


def validate_token_accounting(
    package: Path,
    run_dir: Path,
    profile: str,
    manifest_agents: dict[str, tuple[str, str, str, str, str]],
    report_text: str,
    errors: list[str],
    warnings: list[str],
) -> dict[str, object]:
    token = profile.replace(".", "_")
    ledger = run_dir / "token_usage_ledger.csv"
    pricing = package / f"workflow_{token}/token_pricing.toml"
    summary_md = run_dir / "token_usage_summary.md"
    summary_json = run_dir / "token_usage_summary.json"
    try:
        expected, accounting_errors = calculate_token_cost(ledger, pricing)
    except (OSError, ValueError) as error:
        errors.append(f"Token accounting could not be calculated: {error}")
        return {}
    errors.extend(f"Token accounting: {item}" for item in accounting_errors)
    expected_markdown = token_cost_markdown(expected)
    if read(summary_md) != expected_markdown:
        errors.append("token_usage_summary.md is stale or differs from the deterministic calculation.")
    try:
        actual = json.loads(read(summary_json))
    except json.JSONDecodeError as error:
        errors.append(f"token_usage_summary.json is malformed: {error}")
    else:
        if actual != expected:
            errors.append("token_usage_summary.json is stale or differs from the deterministic calculation.")

    summary_agents = {str(item["agent_id"]): item for item in expected.get("agents", [])}
    if set(summary_agents) != set(manifest_agents):
        errors.append(
            "Token ledger must cover every and only agent execution ID, including the coordinator: "
            f"ledger={sorted(summary_agents)} manifest={sorted(manifest_agents)}"
        )
    for agent_id, (stage, model, _, _, _) in manifest_agents.items():
        if agent_id in summary_agents and summary_agents[agent_id].get("model") != model:
            errors.append(f"Token ledger model differs from the manifest for agent {agent_id}.")
        if agent_id in summary_agents and summary_agents[agent_id].get("role") != stage:
            errors.append(f"Token ledger role differs from the manifest for agent {agent_id}.")

    status = str(expected.get("status", ""))
    if status == "INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE":
        warnings.append(
            "Authoritative per-response usage was unavailable for at least one agent; known tokens "
            "are reported, but complete package token count and price remain blank."
        )
    elif status == "INCOMPLETE_BILLING_BREAKDOWN":
        warnings.append(
            "Authoritative input/output/total usage is complete, but at least one response lacks "
            "cached/cache-write billing detail; token totals are complete and price is incomplete."
        )
    package_totals = expected.get("package", {})
    report_values = {
        "Token accounting status": str(expected.get("status", "")),
        "Total-token count status": str(package_totals.get("total_token_count_status", "")),
        "Total tokens": str(package_totals.get("total_tokens", "")),
        "Known token cost (USD)": str(package_totals.get("known_token_cost_usd", "")),
        "Estimated complete token cost (USD)": str(
            package_totals.get("estimated_total_token_cost_usd") or "__"
        ),
    }
    for label, expected_value in report_values.items():
        match = re.search(
            rf"^-\s+\*\*{re.escape(label)}:\*\*\s*(\S.*)$",
            report_text,
            re.MULTILINE,
        )
        if not match:
            errors.append(f"Markdown report lacks token-accounting field: **{label}:**")
        elif match.group(1).strip() != expected_value:
            errors.append(
                f"Markdown report token field {label} differs from token_usage_summary.json."
            )
    for item in expected.get("models", []):
        if str(item.get("model", "")) not in report_text:
            errors.append(
                f"Markdown report token-accounting section lacks model {item.get('model')}."
            )
    return expected


def validate_control_files_english(package: Path, profile: str, errors: list[str]) -> None:
    token = profile.replace(".", "_")
    required_paths = [
        package / "AGENTS.md",
        package / "PERFORMANCE_PROFILE.md",
        package / "QUALITY_CONTROL_SCOPE.md",
        package / "README.md",
        package / "START_PROMPT.md",
        package / "USAGE.md",
        package / f"workflow_{token}/review_contract.md",
        package / f"workflow_{token}/report_spec.md",
        package / f"workflow_{token}/settings.toml",
        package / f"workflow_{token}/token_pricing.toml",
        package / f"workflow_{token}/scripts/calculate_token_cost.py",
    ]
    workflow_files = sorted(
        path
        for path in (package / f"workflow_{token}").rglob("*")
        if path.is_file() and path.suffix.casefold() in {".md", ".toml", ".py"}
    )
    paths = list(dict.fromkeys([*required_paths, *workflow_files]))
    for path in paths:
        if not path.is_file():
            errors.append(f"Missing workflow-1.5 control file: {path.relative_to(package)}")
        elif CJK_TEXT.search(read(path)):
            errors.append(
                f"Workflow control file contains forbidden CJK text: {path.relative_to(package)}"
            )


def coverage_ids(coverage: str, stage: str, prefix: str) -> set[str]:
    ids: set[str] = set()
    pattern = re.compile(rf"\b{re.escape(prefix)}\d{{3,}}\b")
    for line in coverage.splitlines():
        if re.match(rf"^\|\s*{re.escape(stage)}\s*\|", line):
            ids.update(pattern.findall(line))
    return ids


def validate_coverage_artifacts(
    coverage: str, run_dir: Path, package: Path, errors: list[str]
) -> None:
    seen_shards: set[tuple[str, str]] = set()
    for number, line in enumerate(coverage.splitlines(), start=1):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 5 or cells[0] in {"Stage", "---"}:
            continue
        stage, shard, scope, artifact, status = cells
        if stage not in REQUIRED_STAGES:
            errors.append(f"Unknown coverage stage on line {number}: {stage}")
        if not shard or not scope or not artifact:
            errors.append(f"Coverage row has an empty required cell on line {number}.")
        key = (stage, shard)
        if key in seen_shards:
            errors.append(f"Duplicate coverage shard: {stage}/{shard}")
        seen_shards.add(key)
        if status != "COMPLETE":
            errors.append(f"Coverage row is not COMPLETE: {stage}/{shard}={status}")
        if not PLAIN_ARTIFACT_PATH.fullmatch(artifact):
            errors.append(
                f"Coverage Artifact cell must contain exactly one plain relative path "
                f"on line {number}: {artifact}"
            )
            continue
        relative = Path(artifact)
        if relative.is_absolute():
            errors.append(f"Coverage artifact path must be relative: {artifact}")
            continue
        target = (run_dir / relative).resolve()
        if not inside(package, target):
            errors.append(f"Coverage artifact path escapes the package: {artifact}")
        elif not target.is_file() or target.stat().st_size == 0:
            errors.append(f"Coverage artifact is missing or empty: {artifact}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, choices=("1.5.1", "1.5.2"))
    parser.add_argument("--package", type=Path, default=Path("."))
    args = parser.parse_args()

    package = args.package.expanduser().resolve()
    token = args.profile.replace(".", "_")
    audit_root = package / ".ai_paper_validation"
    run_dir = audit_root / f"review_{token}"
    report_path = audit_root / f"final_report_{token}.md"
    html_path = audit_root / f"final_report_{token}.html"
    errors: list[str] = []
    warnings: list[str] = []

    validate_control_files_english(package, args.profile, errors)

    for relative in REQUIRED_COMMON:
        path = run_dir / relative
        if not path.is_file():
            errors.append(f"Missing required review artifact: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"Required review artifact is empty: {relative}")
    for path in (report_path, html_path):
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Missing or empty versioned report: {path.name}")

    if (run_dir / "review_queue.md").exists():
        errors.append("Workflow 1.5 must not create a count-limited review_queue.md.")

    coverage = read(run_dir / "coverage_manifest.md")
    for stage in REQUIRED_STAGES:
        pattern = re.compile(
            rf"^\|\s*{re.escape(stage)}\s*\|.*\|\s*COMPLETE\s*\|\s*$",
            re.MULTILINE,
        )
        if not pattern.search(coverage):
            errors.append(f"Coverage stage is absent or incomplete: {stage}")
    validate_coverage_artifacts(coverage, run_dir, package, errors)

    source_hash_path = run_dir / "source_hashes_before.sha256"
    source_hashes = parse_hash_file(source_hash_path, package, errors)
    verify_hashes("Source", source_hashes, package, errors)
    direct_sources = {
        path.relative_to(package).as_posix()
        for path in package.iterdir()
        if path.is_file() and path.suffix.casefold() in SOURCE_SUFFIXES
    }
    if set(source_hashes) != direct_sources:
        errors.append(
            "Source hash inventory must exactly match direct package sources: "
            f"expected={sorted(direct_sources)} recorded={sorted(source_hashes)}"
        )
    source_units, fresh_units = validate_source_coverage(
        read(run_dir / "source_coverage.md"), args.profile, direct_sources, errors
    )
    manifest_agents = validate_agent_execution_manifest(
        read(run_dir / "agent_execution_manifest.md"), run_dir, errors
    )

    if args.profile == "1.5.1":
        reused_path = run_dir / "reused_artifact_hashes_before.sha256"
        if not reused_path.is_file() or reused_path.stat().st_size == 0:
            errors.append("Workflow 1.5.1 requires reused_artifact_hashes_before.sha256.")
            reused_hashes: dict[str, str] = {}
        else:
            reused_hashes = parse_hash_file(reused_path, package, errors)
            verify_hashes("Reused artifact", reused_hashes, package, errors)
        new_prefix = f".ai_paper_validation/review_{token}/"
        if any(relative.startswith(new_prefix) for relative in reused_hashes):
            errors.append("The reused-artifact inventory contains new workflow-1.5.1 outputs.")

    ledger_text = read(run_dir / "candidate_ledger.md")
    recheck_text = read(run_dir / "verification/evidence_recheck.md")
    quality_text = read(run_dir / "quality/evidence_quality_audit.md")
    report_text = read(report_path)
    run_state_text = read(run_dir / "run_state.md")
    token_accounting = validate_token_accounting(
        package,
        run_dir,
        args.profile,
        manifest_agents,
        report_text,
        errors,
        warnings,
    )
    observed_minutes, target_status, target_minutes = validate_performance(
        run_state_text, report_text, source_units, fresh_units, errors
    )
    ledger_ids, _ = candidate_sections(ledger_text)
    recheck_ids, _ = candidate_sections(recheck_text)
    quality_ids, _ = candidate_sections(quality_text)
    report_ids, report_sections = candidate_sections(report_text)

    for label, values in (
        ("ledger", ledger_ids),
        ("recheck", recheck_ids),
        ("quality", quality_ids),
        ("report", report_ids),
    ):
        if len(values) != len(set(values)):
            errors.append(f"Duplicate candidate ID in {label}: {values}")
    if set(ledger_ids) != set(recheck_ids):
        errors.append("Candidate ledger and evidence recheck ID sets differ.")
    if set(ledger_ids) != set(quality_ids):
        errors.append("Candidate ledger and quality audit ID sets differ.")
    if ledger_ids != report_ids:
        errors.append(f"Candidate ledger/report IDs or order differ: {ledger_ids} vs {report_ids}")
    for stage in (
        "candidate_registration",
        "evidence_recheck",
        "evidence_quality",
        "report_generation",
    ):
        scoped = coverage_ids(coverage, stage, "C")
        if scoped != set(ledger_ids):
            errors.append(
                f"Coverage scope for {stage} must enumerate every and only ledger C ID: "
                f"scope={sorted(scoped)} ledger={ledger_ids}"
            )

    if not ledger_ids:
        for label, text in (
            ("ledger", ledger_text),
            ("recheck", recheck_text),
            ("quality", quality_text),
            ("report", report_text),
        ):
            if EMPTY_CANDIDATE_NOTICE.casefold() not in text.casefold():
                errors.append(f"Zero-candidate {label} lacks the required explicit notice.")

    combined_candidate_flow = "\n".join((ledger_text, recheck_text, quality_text, report_text))
    if COUNT_CAP_LANGUAGE.search(combined_candidate_flow):
        errors.append("Review artifacts contain a forbidden 10-candidate cap or cap-deferral route.")
    if "Pending Human Adjudication" not in report_text:
        errors.append("Markdown report lacks the Pending Human Adjudication notice.")
    if not re.search(r"quality[- ]control", report_text, re.IGNORECASE):
        errors.append("Markdown report is not framed as a quality-control review.")
    if FORBIDDEN_ADJUDICATION.search(report_text):
        errors.append("Markdown report contains an AI adjudication or severity field.")

    generated_texts = {
        relative: read(run_dir / relative)
        for relative in REQUIRED_COMMON
        if (run_dir / relative).suffix.casefold() in {".md", ".sha256", ".csv", ".json"}
    }
    generated_texts[report_path.name] = report_text
    generated_texts[html_path.name] = read(html_path)
    for relative, value in generated_texts.items():
        if CJK_TEXT.search(value):
            errors.append(f"Generated artifact contains forbidden CJK text: {relative}")

    for candidate_id, section in report_sections.items():
        for field in CARD_FIELDS:
            if field not in section:
                errors.append(f"{candidate_id} lacks required field {field}")
        category_line = next(
            (line for line in section.splitlines() if line.startswith("**Category:**")), ""
        )
        if not any(category_line.strip() == f"**Category:** {value}" for value in ALLOWED_CATEGORIES):
            errors.append(f"{candidate_id} does not use one exact workflow-1.5 category.")
        if not human_fields_are_blank(section):
            errors.append(
                f"{candidate_id} human adjudication fields must appear once each with exact __ values."
            )
        if not p_zero_has_independent_contradiction(section):
            errors.append(
                f"{candidate_id} mentions a display-zero P value without an independent "
                "source-grounded contradiction; P=0 display alone is not a candidate."
            )

        links = [match.group(1) for match in MARKDOWN_LINK.finditer(section)]
        evidence_links = []
        evidence_suffixes: set[str] = set()
        for href in links:
            suffix = Path(unquote(urlsplit(href).path)).suffix.casefold()
            if suffix in SOURCE_SUFFIXES:
                evidence_links.append(href)
                evidence_suffixes.add(suffix)
        if not evidence_links:
            errors.append(f"{candidate_id} has no PDF, Office, or CSV evidence link.")
        if not has_truthful_structural_location(section, evidence_suffixes):
            errors.append(f"{candidate_id} lacks truthful Office/CSV structural locations.")
        for href in evidence_links:
            error = validate_local_link(report_path.parent, package, href)
            if error:
                errors.append(f"{candidate_id}: {error}")

    statistics_inventory = read(run_dir / "statistics/relationship_inventory.md")
    pass_1 = read(run_dir / "checkers/statistical_pass_1.md")
    pass_2 = read(run_dir / "checkers/statistical_pass_2.md")
    relationship_ids = sorted(set(STAT_RELATIONSHIP.findall(statistics_inventory)))
    for relationship_id in relationship_ids:
        if relationship_id not in pass_1 or relationship_id not in pass_2:
            errors.append(f"Statistical relationship lacks both pass records: {relationship_id}")
    if relationship_ids:
        if "PASS_1_COMPLETE" not in statistics_inventory:
            errors.append("Statistical inventory lacks PASS_1_COMPLETE status.")
        if "PASS_2_COMPLETE" not in statistics_inventory:
            errors.append("Statistical inventory lacks PASS_2_COMPLETE status.")
    for stage in ("statistics_pass_1", "statistics_pass_2"):
        scoped = coverage_ids(coverage, stage, "S")
        if scoped != set(relationship_ids):
            errors.append(
                f"Coverage scope for {stage} must enumerate every and only statistical S ID: "
                f"scope={sorted(scoped)} inventory={relationship_ids}"
            )

    if html_path.is_file():
        html = read(html_path)
        html_parser = ReportHTMLParser()
        html_parser.feed(html)
        if "<html" not in html.casefold():
            errors.append("HTML report is not standalone HTML.")
        if not html_parser.has_toc:
            errors.append("HTML report lacks a table of contents.")
        if "Pending Human Adjudication" not in html:
            errors.append("HTML report lacks Pending Human Adjudication notice.")
        for href in html_parser.hrefs:
            suffix = Path(unquote(urlsplit(href).path)).suffix.casefold()
            if suffix in SOURCE_SUFFIXES:
                error = validate_local_link(html_path.parent, package, href)
                if error:
                    errors.append(f"HTML: {error}")

    result = {
        "schema_version": 2,
        "profile": args.profile,
        "status": "PASS" if not errors else "FAIL",
        "candidate_count": len(ledger_ids),
        "candidate_ids": ledger_ids,
        "candidate_limit": None,
        "report_all_candidates": True,
        "statistical_relationship_count": len(relationship_ids),
        "total_source_units": source_units,
        "fresh_source_units": fresh_units,
        "source_coverage": "PASS"
        if not any("source coverage" in item.casefold() or "source-coverage" in item.casefold() or "mapped units" in item.casefold() for item in errors)
        else "FAIL",
        "source_integrity": "PASS"
        if not any("integrity failure" in item.casefold() or "hash inventory" in item.casefold() for item in errors)
        else "FAIL",
        "agent_first": True,
        "statistical_agents": "fresh-distinct-terra-high",
        "agent_count": len(manifest_agents),
        "token_accounting_status": token_accounting.get("status"),
        "total_tokens": token_accounting.get("package", {}).get("total_tokens")
        if isinstance(token_accounting.get("package"), dict)
        else None,
        "known_token_cost_usd": token_accounting.get("package", {}).get(
            "known_token_cost_usd"
        )
        if isinstance(token_accounting.get("package"), dict)
        else None,
        "estimated_complete_token_cost_usd": token_accounting.get("package", {}).get(
            "estimated_total_token_cost_usd"
        )
        if isinstance(token_accounting.get("package"), dict)
        else None,
        "root_codex_required": False,
        "python_role": "auxiliary-only",
        "target_minutes": target_minutes,
        "observed_elapsed_minutes": observed_minutes,
        "target_status": target_status,
        "errors": errors,
        "warnings": warnings,
    }
    run_dir.mkdir(parents=True, exist_ok=True)
    output = run_dir / "review_validation.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
