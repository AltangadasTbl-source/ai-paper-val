#!/usr/bin/env python3
"""Validate workflow 1.6.2 coverage, agent provenance, screening, classification, reports, timing, and integrity."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


REQUIRED_COMMON = (
    "routing_preflight.md",
    "tooling_record.md",
    "run_state.md",
    "source_inventory.md",
    "source_hashes_before.sha256",
    "evidence_asset_inventory.md",
    "source_coverage.md",
    "coverage_manifest.md",
    "agent_execution_manifest.md",
    "extraction/main_quantitative_evidence.md",
    "extraction/support_quantitative_evidence.md",
    "relationships/numeric_relationship_inventory.md",
    "statistics/relationship_inventory.md",
    "checkers/numeric_consistency.md",
    "checkers/statistical_pass_1.md",
    "checkers/cross_source_consistency.md",
    "checkers/statistical_pass_2.md",
    "screening/inclusion_screen.md",
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
    "inclusion_screening",
    "candidate_registration",
    "evidence_recheck",
    "statistics_pass_2",
    "evidence_quality",
    "report_generation",
)
CARD_FIELDS = (
    "**Candidate statement:**",
    "**Review domain:**",
    "**Relationship type:**",
    "**All relationships:**",
    "**Compared document roles:**",
    "**Evidence state:**",
    "**Inclusion audit:**",
    "**Finding IDs:**",
    "**Qualifying route:**",
    "**Classification rationale:**",
    "**Classification ambiguity:**",
    "**Exact source locations:**",
    "**Source evidence:**",
    "**Reported-versus-comparator:**",
    "**Reasoning procedure:**",
    "**Calculation:**",
    "**Affected result or extracted value:**",
    "**Why context does not resolve it:**",
    "**Alternative source-grounded interpretations:**",
    "**Mechanical evidence recheck:**",
    "**Potential downstream evidence impact:**",
)
RELATIONSHIP_TYPES = ("P_R", "P_P", "S_C", "S_W")  # also the precedence order
REVIEW_DOMAINS_BY_RELATIONSHIP = {
    "P_R": ("protocol_report",),
    "P_P": ("plan_material",),
    "S_C": ("statistical_results", "report_internal_inconsistency"),
    "S_W": ("statistical_results", "report_internal_inconsistency"),
}
REVIEW_DOMAINS = (
    "statistical_results",
    "report_internal_inconsistency",
    "protocol_report",
    "plan_material",
)
EVIDENCE_STATES = (
    "reproduced",
    "reproduced_after_transcription_correction",
    "not_reproduced",
)
INCLUSION_AUDIT_VALUES = ("CONFIRMED", "QUESTIONED")
CLASSIFICATION_HEADER = (
    "ID",
    "Review domain",
    "Relationship type",
    "All relationships",
    "Compared document roles",
    "Evidence state",
    "Inclusion audit",
    "Finding IDs",
)
SCREENING_HEADER = (
    "Finding ID",
    "Source checker",
    "Screening stage",
    "Decision",
    "Reason code",
    "Candidate ID",
)
SCREENED_OUT_CODES = (
    "NOT_REPRODUCED",
    "ROUNDING_OR_DISPLAY_PRECISION",
    "NOTATION_OR_TYPOGRAPHY",
    "TERMINOLOGY_OR_WORDING",
    "MODEL_VERSUS_CRUDE",
    "CONTEXT_RESOLVES",
    "CONDITIONAL_OR_UNREPORTED",
    "PERIPHERAL_COMPARISON",
    "OUT_OF_FOCUS",
    "DUPLICATE_OF_INCLUDED",
)
FINDING_SOURCES = {
    "NUM": ("numeric_consistency_reviewer", "checkers/numeric_consistency.md"),
    "XS": ("cross_source_consistency_reviewer", "checkers/cross_source_consistency.md"),
    "ST1": ("statistics_pass_1", "checkers/statistical_pass_1.md"),
    "ST2": ("statistics_pass_2", "checkers/statistical_pass_2.md"),
    "QA": ("quality_control_auditor", "quality/evidence_quality_audit.md"),
}
FINDING_ID = re.compile(r"^F-(NUM|XS|ST1|ST2|QA)-\d{3,}$")
FINDING_HEADING = re.compile(r"^#{2,4}\s+(F-(?:NUM|XS|ST1|ST2|QA)-\d{3,})\b", re.MULTILINE)
EMPTY_CELL = {"—", "-", "–", "None", "none", "N/A"}
FORBIDDEN_ISSUE_WORDS = re.compile(
    r"\b(errors?|erroneous(?:ly)?|mistakes?|mistaken(?:ly)?|defects?|wrong(?:ly)?|"
    r"incorrect(?:ly|ness)?)\b",
    re.IGNORECASE,
)
ALLOWED_ERROR_BEFORE = re.compile(
    r"(?:standard|type\s+(?:i|ii|1|2)|measurement|sampling|random|systematic|residual|"
    r"mean\s+squared?|root\s+mean\s+squared?|family[- ]?wise|experiment[- ]?wise|alpha|beta|"
    r"absolute|relative|prediction|refractive|medication|prescribing|dosing|diagnostic|"
    r"medical|surgical|septal|tube|birth|cognitive|visual[- ]field|perfusion|filling)[\s-]+$",
    re.IGNORECASE,
)
ALLOWED_ERROR_AFTER = re.compile(r"^[\s-]+(?:bars?|spending|rates?|terms?|variance|sums?\s+of\s+squares)\b", re.IGNORECASE)
QUOTED_SPAN = re.compile(r"`[^`\n]*`|\u201c[^\u201d\n]*\u201d|\"[^\"\n]*\"")
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
# The model element is the default run model; validation compares every row with the run model
# recorded in routing_preflight.md.
REQUIRED_AGENT_STAGES = {
    "coordinator": ("gpt-6.1-sol", "high", "CURRENT_SESSION", "run_state.md"),
    "reuse_asset_curator": ("gpt-6.1-sol", "medium", "FRESH_SPAWN", "source_inventory.md"),
    "main_quantitative_mapper": (
        "gpt-6.1-sol",
        "medium",
        "FRESH_SPAWN",
        "extraction/main_quantitative_evidence.md",
    ),
    "support_quantitative_mapper": (
        "gpt-6.1-sol",
        "medium",
        "FRESH_SPAWN",
        "extraction/support_quantitative_evidence.md",
    ),
    "numeric_consistency_reviewer": (
        "gpt-6.1-sol",
        "medium",
        "FRESH_SPAWN",
        "checkers/numeric_consistency.md",
    ),
    "cross_source_consistency_reviewer": (
        "gpt-6.1-sol",
        "medium",
        "FRESH_SPAWN",
        "checkers/cross_source_consistency.md",
    ),
    "statistics_pass_1": ("gpt-6.1-sol", "high", "FRESH_SPAWN", "checkers/statistical_pass_1.md"),
    "inclusion_screener": ("gpt-6.1-sol", "high", "FRESH_SPAWN", "screening/inclusion_screen.md"),
    "evidence_rechecker": ("gpt-6.1-sol", "high", "FRESH_SPAWN", "verification/evidence_recheck.md"),
    "statistics_pass_2": ("gpt-6.1-sol", "high", "FRESH_SPAWN", "checkers/statistical_pass_2.md"),
    "quality_control_auditor": (
        "gpt-6.1-sol",
        "high",
        "FRESH_SPAWN",
        "quality/evidence_quality_audit.md",
    ),
    "report_generator": ("gpt-6.1-sol", "medium", "FRESH_SPAWN", "limitations.md"),
}
DEFAULT_RUN_MODEL = "gpt-6.1-sol"
ALLOWED_EFFORTS = {"high", "medium"}
RUN_MODEL_SOURCES = {"DEFAULT", "USER_SELECTED"}
EXPLICIT_MODEL_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:/-]*")
MOVING_MODEL_ALIAS = re.compile(r"(?:^~|latest|\bauto\b|\bdefault\b)", re.IGNORECASE)
QUALIFYING_ROUTE = re.compile(r"^\*\*Qualifying route:\*\*\s*(Route A, category [1-5]|Route B)\b", re.MULTILINE)


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
        if reused + fresh != total:
            errors.append(
                f"Reuse plus fresh-required units must equal total units for {source_path}."
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


def validate_routing_preflight(text: str, errors: list[str]) -> str:
    run_match = re.search(r"^- Run model:\s*(\S+)\s*$", text, re.MULTILINE)
    source_match = re.search(r"^- Run model source:\s*(\S+)\s*$", text, re.MULTILINE)
    run_model = run_match.group(1) if run_match else ""
    source = source_match.group(1) if source_match else ""
    if source not in RUN_MODEL_SOURCES:
        errors.append("Routing preflight must record Run model source: DEFAULT or USER_SELECTED.")
    if not run_model or not EXPLICIT_MODEL_ID.fullmatch(run_model) or MOVING_MODEL_ALIAS.search(run_model):
        errors.append(f"Routing preflight must record an exact, non-alias Run model: {run_model or 'missing'}.")
    elif source == "DEFAULT" and run_model != DEFAULT_RUN_MODEL:
        errors.append(f"Run model source DEFAULT requires Run model: {DEFAULT_RUN_MODEL}.")
    expected = {
        "Status": "PASS",
        "Provider": "CURRENT_SESSION",
        "Coordinator model": run_model,
        "Coordinator reasoning effort": "high",
        "Ordinary specialist model": run_model,
        "Ordinary specialist reasoning effort": "medium",
        "Statistical specialist model": run_model,
        "Statistical specialist reasoning effort": "high",
        "Screening, recheck, and audit specialist model": run_model,
        "Screening, recheck, and audit specialist reasoning effort": "high",
        "Fixed model matrix": "PASS",
        "Named agent presets": "PASS",
        "Named agent preset count": "10",
        "Mandatory specialist stages": "11",
        "Mandatory agent start contract": "FRESH_DISTINCT",
        "Coordinator inference": "PASS",
        "Execution mode": "INTERACTIVE_CLI",
        "Launch command": "codex --approve-for-me",
    }
    for label, value in expected.items():
        match = re.search(rf"^- {re.escape(label)}:\s*(.+?)\s*$", text, re.MULTILINE)
        if not match or match.group(1) != value:
            errors.append(f"Routing preflight must record {label}: {value}.")
    checked = re.search(r"^- Checked UTC:\s*(\S+)\s*$", text, re.MULTILINE)
    if not checked or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", checked.group(1)):
        errors.append("Routing preflight must record a UTC timestamp in YYYY-MM-DDTHH:MM:SSZ form.")
    return run_model


def validate_agent_execution_manifest(
    text: str, run_dir: Path, errors: list[str], run_model: str
) -> dict[str, tuple[str, str, str, str, str]]:
    agents: dict[str, tuple[str, str, str, str, str]] = {}
    stage_agents: dict[str, tuple[str, str, str, str, str]] = {}
    for number, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 6 or cells[0] in {"Stage", "---"}:
            continue
        stage, agent_id, model, effort, start_mode, artifact = cells
        if any(not value for value in (stage, model, effort, start_mode, artifact)):
            errors.append(f"Agent execution line {number} has an empty required field.")
        if model != run_model or effort not in ALLOWED_EFFORTS:
            errors.append(
                f"Agent execution line {number} has a forbidden model/effort pair: "
                f"{model}/{effort}."
            )
        if stage != "coordinator" and start_mode != "FRESH_SPAWN":
            errors.append(f"Agent execution stage {stage} must use FRESH_SPAWN.")
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/-]{2,}", agent_id) or re.search(
            r"(?:runtime-id|agent-id|placeholder|unknown|todo|n/a)", agent_id, re.IGNORECASE
        ):
            errors.append(f"Agent execution line {number} has a missing or placeholder runtime ID.")
        if agent_id in agents:
            errors.append(f"Duplicate agent execution row for runtime ID: {agent_id}")
            continue
        agents[agent_id] = (stage, model, effort, start_mode, artifact)
        if stage in stage_agents:
            errors.append(f"Duplicate agent execution stage: {stage}")
        else:
            stage_agents[stage] = (agent_id, model, effort, start_mode, artifact)
        if not PLAIN_ARTIFACT_PATH.fullmatch(artifact):
            errors.append(f"Agent execution has invalid artifact path on line {number}.")
        else:
            target = (run_dir / artifact).resolve()
            if not inside(run_dir, target):
                errors.append(f"Agent execution artifact escapes the review directory: {artifact}")
            elif not target.is_file() or target.stat().st_size == 0:
                errors.append(f"Agent execution artifact is missing or empty: {artifact}")
    if not agents:
        errors.append("agent_execution_manifest.md has no agent rows.")
    for stage, (_, expected_effort, expected_start, expected_artifact) in REQUIRED_AGENT_STAGES.items():
        expected_model = run_model
        if stage not in stage_agents:
            errors.append(f"Missing mandatory fresh agent execution row: {stage}")
            continue
        _, model, effort, start_mode, artifact = stage_agents[stage]
        if (
            model != expected_model
            or effort != expected_effort
            or start_mode != expected_start
        ):
            errors.append(
                f"{stage} must record {expected_model}/{expected_effort}/{expected_start}, got "
                f"{model}/{effort}/{start_mode}."
            )
        if artifact != expected_artifact:
            errors.append(f"{stage} artifact must be exactly {expected_artifact}.")
    return agents


def validate_control_files_english(package: Path, profile: str, errors: list[str]) -> None:
    token = profile.replace(".", "_")
    required_paths = [
        package / "AGENTS.md",
        package / "PERFORMANCE_PROFILE.md",
        package / "QUALITY_CONTROL_SCOPE.md",
        package / "README.md",
        package / "START_PROMPT.md",
        package / "USAGE.md",
        package / "CODEX_SETUP.md",
        package / f"workflow_{token}/review_contract.md",
        package / f"workflow_{token}/report_spec.md",
        package / f"workflow_{token}/settings.toml",
        package / f"workflow_{token}/scripts/render_report.py",
        package / f"workflow_{token}/scripts/validate_review.py",
    ]
    workflow_files = sorted(
        path
        for path in (package / f"workflow_{token}").rglob("*")
        if path.is_file() and path.suffix.casefold() in {".md", ".toml", ".py"}
    )
    paths = list(dict.fromkeys([*required_paths, *workflow_files]))
    for path in paths:
        if not path.is_file():
            errors.append(f"Missing workflow-1.6.2 control file: {path.relative_to(package)}")
        elif CJK_TEXT.search(read(path)):
            errors.append(
                f"Workflow control file contains forbidden CJK text: {path.relative_to(package)}"
            )


def card_value(section: str, label: str) -> str:
    match = re.search(rf"^\*\*{re.escape(label)}:\*\*[ \t]*(.*?)[ \t]*$", section, re.MULTILINE)
    return match.group(1).strip() if match else ""


def parse_classification_table(ledger_text: str, errors: list[str]) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    tables = 0
    in_table = False
    for line in ledger_text.splitlines():
        if not line.startswith("|"):
            in_table = False
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if tuple(cells) == CLASSIFICATION_HEADER:
            tables += 1
            in_table = True
            continue
        if not in_table or set("".join(cells)) <= set("-: "):
            continue
        if len(cells) != len(CLASSIFICATION_HEADER):
            errors.append(f"Classification table row has {len(cells)} cells: {line.strip()}")
            continue
        row = dict(zip(CLASSIFICATION_HEADER, cells))
        if row["ID"] in rows:
            errors.append(f"Duplicate classification table row: {row['ID']}")
        rows[row["ID"]] = row
    if tables > 1:
        errors.append("candidate_ledger.md must contain exactly one classification table.")
    return rows


def split_ids(cell: str) -> list[str]:
    return [item.strip() for item in cell.split(",") if item.strip()]


def validate_classification(
    ledger_text: str,
    ledger_ids: list[str],
    report_sections: dict[str, str],
    included_findings: dict[str, set[str]],
    errors: list[str],
) -> dict[str, object]:
    table = parse_classification_table(ledger_text, errors)
    if ledger_ids and not table:
        errors.append("candidate_ledger.md lacks the required classification table.")
    if list(table) != ledger_ids:
        errors.append(
            "Classification table must list every and only ledger C ID in stable-ID order: "
            f"table={list(table)} ledger={ledger_ids}"
        )
    counts: dict[str, dict[str, int]] = {
        "review_domain": {},
        "relationship_type": {},
        "evidence_state": {},
        "inclusion_audit": {},
    }
    for candidate_id, row in table.items():
        relationship = row["Relationship type"]
        relations = split_ids(row["All relationships"])
        domain = row["Review domain"]
        state = row["Evidence state"]
        audit = row["Inclusion audit"]
        roles = row["Compared document roles"]
        findings = split_ids(row["Finding IDs"])
        if relationship not in RELATIONSHIP_TYPES:
            errors.append(
                f"{candidate_id} relationship type must be one of {RELATIONSHIP_TYPES}: {relationship}"
            )
        if not relations or any(item not in RELATIONSHIP_TYPES for item in relations):
            errors.append(
                f"{candidate_id} all relationships contain an unknown code: {row['All relationships']}"
            )
        elif len(relations) != len(set(relations)):
            errors.append(f"{candidate_id} all relationships repeat a code.")
        elif relationship not in relations:
            errors.append(f"{candidate_id} all relationships must include the relationship type.")
        elif relationship != min(relations, key=RELATIONSHIP_TYPES.index):
            errors.append(
                f"{candidate_id} relationship type violates precedence P_R > P_P > S_C > S_W: "
                f"{relationship} with {relations}"
            )
        if domain not in REVIEW_DOMAINS:
            errors.append(f"{candidate_id} review domain must be one of {REVIEW_DOMAINS}: {domain}")
        elif relationship in REVIEW_DOMAINS_BY_RELATIONSHIP and domain not in REVIEW_DOMAINS_BY_RELATIONSHIP[relationship]:
            errors.append(
                f"{candidate_id} review domain {domain} is inconsistent with relationship type "
                f"{relationship}; allowed: {REVIEW_DOMAINS_BY_RELATIONSHIP[relationship]}"
            )
        if state not in EVIDENCE_STATES:
            errors.append(f"{candidate_id} evidence state is invalid: {state}")
        if audit not in INCLUSION_AUDIT_VALUES:
            errors.append(f"{candidate_id} inclusion audit must be CONFIRMED or QUESTIONED: {audit}")
        if relationship in {"P_R", "P_P"} and not re.search(r"\bPLAN\b", roles):
            errors.append(f"{candidate_id} is {relationship} but no PLAN location is recorded.")
        if relationship in {"P_R", "S_C", "S_W"} and not re.search(r"\bREPORT\b", roles):
            errors.append(f"{candidate_id} is {relationship} but no REPORT location is recorded.")
        if set(findings) != included_findings.get(candidate_id, set()):
            errors.append(
                f"{candidate_id} Finding IDs must equal its INCLUDE rows in the screening log: "
                f"ledger={sorted(findings)} screening={sorted(included_findings.get(candidate_id, set()))}"
            )
        section = report_sections.get(candidate_id)
        if section is not None:
            for label, expected in (
                ("Review domain", domain),
                ("Relationship type", relationship),
                ("All relationships", ", ".join(relations)),
                ("Compared document roles", roles),
                ("Evidence state", state),
                ("Inclusion audit", audit),
                ("Finding IDs", ", ".join(findings)),
            ):
                if card_value(section, label) != expected:
                    errors.append(
                        f"{candidate_id} report field {label} differs from the ledger classification table."
                    )
            for label in (
                "Classification rationale",
                "Classification ambiguity",
                "Affected result or extracted value",
                "Why context does not resolve it",
            ):
                if not card_value(section, label):
                    errors.append(f"{candidate_id} report field {label} is empty.")
        for key, value in (
            ("review_domain", domain),
            ("relationship_type", relationship),
            ("evidence_state", state),
            ("inclusion_audit", audit),
        ):
            counts[key][value] = counts[key].get(value, 0) + 1
    return {"rows": len(table), **counts}


def validate_screening(
    run_dir: Path,
    ledger_ids: list[str],
    manifest_agents: dict[str, tuple[str, str, str, str, str]],
    errors: list[str],
) -> tuple[dict[str, set[str]], dict[str, object]]:
    text = read(run_dir / "screening/inclusion_screen.md")
    rows: list[dict[str, str]] = []
    tables = 0
    in_table = False
    for line in text.splitlines():
        if not line.startswith("|"):
            in_table = False
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if tuple(cells) == SCREENING_HEADER:
            tables += 1
            in_table = True
            continue
        if not in_table or set("".join(cells)) <= set("-: "):
            continue
        if len(cells) != len(SCREENING_HEADER):
            errors.append(f"Screening table row has {len(cells)} cells: {line.strip()}")
            continue
        rows.append(dict(zip(SCREENING_HEADER, cells)))
    if tables != 1:
        errors.append("screening/inclusion_screen.md must contain exactly one screening table.")

    ledger_set = set(ledger_ids)
    included: dict[str, set[str]] = {}
    primary: dict[str, dict[str, str]] = {}
    audit: dict[str, dict[str, str]] = {}
    for row in rows:
        finding = row["Finding ID"]
        match = FINDING_ID.fullmatch(finding)
        if not match:
            errors.append(f"Screening row has an invalid finding ID: {finding}")
            continue
        prefix = match.group(1)
        checker, _ = FINDING_SOURCES[prefix]
        stage = row["Screening stage"]
        decision = row["Decision"]
        reason = row["Reason code"]
        candidate = row["Candidate ID"]
        if row["Source checker"] != checker:
            errors.append(f"{finding} source checker must be {checker}: {row['Source checker']}")
        expected_stages = {"NUM": {"initial", "audit"}, "XS": {"initial", "audit"},
                           "ST1": {"initial", "audit"}, "ST2": {"pass_2", "audit"}, "QA": {"audit"}}[prefix]
        if stage not in expected_stages:
            errors.append(f"{finding} screening stage must be one of {sorted(expected_stages)}: {stage}")
        target = audit if stage == "audit" else primary
        if finding in target:
            errors.append(f"{finding} has more than one {'audit' if stage == 'audit' else 'screening'} row.")
        target[finding] = row
        if decision == "INCLUDE":
            if reason != "MEETS_THRESHOLD":
                errors.append(f"{finding} INCLUDE must use reason code MEETS_THRESHOLD: {reason}")
            if candidate not in ledger_set:
                errors.append(f"{finding} INCLUDE must name a ledger candidate ID: {candidate}")
        elif decision == "SCREENED_OUT":
            if reason not in SCREENED_OUT_CODES:
                errors.append(f"{finding} screened-out reason code is invalid: {reason}")
            elif reason == "DUPLICATE_OF_INCLUDED":
                if candidate not in ledger_set:
                    errors.append(f"{finding} DUPLICATE_OF_INCLUDED must name a ledger candidate ID: {candidate}")
            elif candidate not in EMPTY_CELL:
                errors.append(f"{finding} screened-out row must use an empty candidate cell: {candidate}")
        else:
            errors.append(f"{finding} decision must be INCLUDE or SCREENED_OUT: {decision}")
    for finding, row in audit.items():
        if finding.startswith("F-QA-"):
            continue
        if finding not in primary:
            errors.append(f"{finding} has an audit row without an initial or pass-2 screening row.")
        elif primary[finding]["Decision"] == "INCLUDE" and row["Decision"] == "SCREENED_OUT":
            errors.append(
                f"{finding} was registered as a candidate; the auditor may record QUESTIONED but may "
                "not screen it out."
            )
    final = {**primary, **audit}
    for finding, row in final.items():
        if row["Decision"] == "INCLUDE" and row["Candidate ID"] in ledger_set:
            included.setdefault(row["Candidate ID"], set()).add(finding)
    for row in primary.values():
        if row["Decision"] == "INCLUDE" and row["Candidate ID"] in ledger_set:
            included.setdefault(row["Candidate ID"], set()).add(row["Finding ID"])
    if set(included) != ledger_set:
        errors.append(
            "Every ledger candidate must have at least one INCLUDE row and every INCLUDE row must name "
            f"a ledger candidate: screening={sorted(included)} ledger={sorted(ledger_set)}"
        )

    for prefix, (_, artifact) in FINDING_SOURCES.items():
        defined = {
            item for item in FINDING_HEADING.findall(read(run_dir / artifact))
            if item.startswith(f"F-{prefix}-")
        }
        screened = {finding for finding in final if finding.startswith(f"F-{prefix}-")}
        if defined - screened:
            errors.append(f"Findings in {artifact} lack a screening decision: {sorted(defined - screened)}")
        if screened - defined:
            errors.append(f"Screened findings are not defined as headings in {artifact}: {sorted(screened - defined)}")
    if any(row["Screening stage"] == "pass_2" for row in primary.values()):
        stages = {
            stage: (model, effort, start)
            for stage, model, effort, start, _ in manifest_agents.values()
        }
        if stages.get("inclusion_screener_pass_2", ("", "", ""))[1:] != ("high", "FRESH_SPAWN"):
            errors.append(
                "Pass-2 findings require a fresh run-model/high inclusion_screener_pass_2 agent row."
            )
        screen_ids = {
            agent_id for agent_id, values in manifest_agents.items()
            if values[0] in {"inclusion_screener", "inclusion_screener_pass_2"}
        }
        if len(screen_ids) < 2:
            errors.append("The pass-2 inclusion screen must use a different runtime agent from the initial screen.")

    reasons: dict[str, int] = {}
    decisions = {"INCLUDE": 0, "SCREENED_OUT": 0}
    for row in final.values():
        if row["Decision"] in decisions:
            decisions[row["Decision"]] += 1
        if row["Decision"] == "SCREENED_OUT":
            reasons[row["Reason code"]] = reasons.get(row["Reason code"], 0) + 1
    summary = {
        "findings": len(final),
        "included_findings": decisions["INCLUDE"],
        "screened_out_findings": decisions["SCREENED_OUT"],
        "screened_out_by_reason": dict(sorted(reasons.items())),
    }
    return included, summary


def validate_vocabulary(texts: dict[str, str], errors: list[str]) -> None:
    for label, text in texts.items():
        hits: list[str] = []
        for line in text.splitlines():
            if line.lstrip().startswith(">"):
                continue
            stripped = QUOTED_SPAN.sub(" ", line)
            for match in FORBIDDEN_ISSUE_WORDS.finditer(stripped):
                word = match.group(1).casefold()
                if word.startswith(("error", "defect")):
                    before = stripped[max(0, match.start() - 40) : match.start()]
                    after = stripped[match.end() : match.end() + 30]
                    if ALLOWED_ERROR_BEFORE.search(before) or ALLOWED_ERROR_AFTER.match(after):
                        continue
                hits.append(stripped[max(0, match.start() - 30) : match.end() + 30].strip())
        if hits:
            errors.append(
                f"{label} describes an issue with a forbidden word (use inconsistency, discrepancy, "
                f"or does not reconcile): {hits[:3]}"
            )


TOOLING_FIELDS = {
    "Probe UTC": None,
    "Platform": None,
    "Direct tools available": None,
    "Fallback environment": {"NOT_NEEDED", "CREATED", "INSTALL_FAILED"},
    "Fallback packages": None,
    "Fallback capabilities used": None,
    "Fallback environment removed": {"YES", "NOT_CREATED"},
    "Compute device": {"CPU", "GPU_USER_REQUESTED"},
    "Tooling limitations": None,
}


def validate_tooling(run_dir: Path, errors: list[str]) -> dict[str, str]:
    text = read(run_dir / "tooling_record.md")
    values: dict[str, str] = {}
    for label, allowed in TOOLING_FIELDS.items():
        match = re.search(rf"^-\s+\*\*{re.escape(label)}:\*\*[ \t]*(\S.*?)[ \t]*$", text, re.MULTILINE)
        if not match:
            errors.append(f"tooling_record.md lacks field: {label}")
            continue
        values[label] = match.group(1)
        if allowed and values[label] not in allowed:
            errors.append(f"tooling_record.md {label} must be one of {sorted(allowed)}: {values[label]}")
    if values.get("Probe UTC") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", values["Probe UTC"]):
        errors.append("tooling_record.md Probe UTC must be YYYY-MM-DDTHH:MM:SSZ.")
    environment = values.get("Fallback environment")
    removed = values.get("Fallback environment removed")
    venv_dir = run_dir / "tooling" / "venv"
    if venv_dir.exists():
        errors.append("The temporary fallback environment still exists; run bootstrap_tooling.py remove.")
    if environment in {"CREATED", "INSTALL_FAILED"} and not (run_dir / "tooling" / "bootstrap_log.json").is_file():
        errors.append("A fallback environment was attempted but tooling/bootstrap_log.json is missing.")
    if environment == "CREATED" and removed != "YES":
        errors.append("A created fallback environment must be recorded as removed: YES.")
    if environment == "NOT_NEEDED" and removed != "NOT_CREATED":
        errors.append("Fallback environment removed must be NOT_CREATED when no environment was needed.")
    if environment == "INSTALL_FAILED" and values.get("Tooling limitations", "").casefold() in {"", "none"}:
        errors.append("INSTALL_FAILED requires the affected units in Tooling limitations.")
    return values


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
    parser.add_argument("--profile", required=True, choices=("1.6.2",))
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
        errors.append("Workflow 1.6.2 must not create a count-limited review_queue.md.")

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
    run_model = validate_routing_preflight(read(run_dir / "routing_preflight.md"), errors)
    tooling = validate_tooling(run_dir, errors)
    agent_errors_before = len(errors)
    manifest_agents = validate_agent_execution_manifest(
        read(run_dir / "agent_execution_manifest.md"), run_dir, errors, run_model
    )
    mandatory_agent_routing_ok = len(errors) == agent_errors_before

    if args.profile == "1.6.2":
        reused_path = run_dir / "reused_artifact_hashes_before.sha256"
        if not reused_path.is_file() or reused_path.stat().st_size == 0:
            errors.append("Workflow 1.6.2 requires reused_artifact_hashes_before.sha256.")
            reused_hashes: dict[str, str] = {}
        else:
            reused_hashes = parse_hash_file(reused_path, package, errors)
            if not reused_hashes and re.search(
                r"^#\s*NO_REUSABLE_ASSETS\b", read(reused_path), re.MULTILINE
            ):
                # The package has no reusable extraction assets: every unit must be mapped fresh.
                if source_units != fresh_units:
                    errors.append(
                        "NO_REUSABLE_ASSETS requires every source unit to be fresh-required "
                        f"(total={source_units}, fresh={fresh_units})."
                    )
            else:
                verify_hashes("Reused artifact", reused_hashes, package, errors)
        new_prefix = f".ai_paper_validation/review_{token}/"
        if any(relative.startswith(new_prefix) for relative in reused_hashes):
            errors.append("The reused-artifact inventory contains new workflow-1.6.2 outputs.")

    ledger_text = read(run_dir / "candidate_ledger.md")
    recheck_text = read(run_dir / "verification/evidence_recheck.md")
    quality_text = read(run_dir / "quality/evidence_quality_audit.md")
    report_text = read(report_path)
    run_state_text = read(run_dir / "run_state.md")
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

    # Every generated text artifact must be English; source-derived text under preprocessing/ and
    # the temporary tooling directory are excluded because they reproduce supplied sources.
    generated_texts = {
        path.relative_to(run_dir).as_posix(): read(path)
        for path in sorted(run_dir.rglob("*"))
        if path.is_file()
        and path.suffix.casefold() in {".md", ".sha256", ".csv", ".json", ".txt"}
        and path.relative_to(run_dir).parts[0] not in {"preprocessing", "tooling"}
        and path.name != "review_validation.json"
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
        if re.search(r"\*\*Human (?:adjudication fields|verification steps):\*\*", section):
            errors.append(
                f"{candidate_id} must not contain human adjudication fields or human verification steps; "
                "human adjudication is recorded in the review workbook."
            )
        if not QUALIFYING_ROUTE.search(section):
            errors.append(f"{candidate_id} Qualifying route must be 'Route A, category N' (N = 1-5) or 'Route B'.")
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

    included_findings, screening = validate_screening(run_dir, ledger_ids, manifest_agents, errors)
    classification = validate_classification(
        ledger_text, ledger_ids, report_sections, included_findings, errors
    )
    for heading in ("Inclusion Screening Summary", "Review-Domain Summary"):
        if not re.search(rf"^#{{1,4}}\s+(?:\d+\.?\s+)?{re.escape(heading)}\b", report_text, re.MULTILINE):
            errors.append(f"Markdown report lacks the {heading} section.")
    validate_vocabulary(
        {
            report_path.name: report_text,
            "candidate_ledger.md": ledger_text,
            "verification/evidence_recheck.md": recheck_text,
            "quality/evidence_quality_audit.md": quality_text,
            "screening/inclusion_screen.md": read(run_dir / "screening/inclusion_screen.md"),
        },
        errors,
    )

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
        "schema_version": 4,
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
        "run_model": run_model,
        "statistical_agents": f"fresh-distinct-{run_model}-high",
        "mandatory_agent_routing": f"fresh-distinct-fixed-{run_model}-configured"
        if mandatory_agent_routing_ok
        else "FAIL",
        "agent_count": len(manifest_agents),
        "screening": screening,
        "classification": classification,
        "fallback_environment": tooling.get("Fallback environment"),
        "compute_device": tooling.get("Compute device"),
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
