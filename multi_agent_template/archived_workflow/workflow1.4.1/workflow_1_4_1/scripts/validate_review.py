#!/usr/bin/env python3
"""Validate workflow 1.4 coverage, uncapped candidate conservation, links, tone, and integrity."""

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
    "run_state.md",
    "source_inventory.md",
    "source_hashes_before.sha256",
    "evidence_asset_inventory.md",
    "source_coverage.md",
    "coverage_manifest.md",
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
EMPTY_CANDIDATE_NOTICE = "No stable candidates were identified"
CJK_TEXT = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
PERFORMANCE_LABELS = (
    "Target elapsed minutes",
    "Started UTC",
    "Finished UTC",
    "Observed elapsed minutes",
    "Target status",
    "Exceedance causes",
)
COMMON_AGENT_PROFILE = {
    "qc14-cross-source-consistency-reviewer.toml": ("gpt-5.6-terra", "medium"),
    "qc14-evidence-rechecker.toml": ("gpt-5.6-sol", "high"),
    "qc14-main-quantitative-mapper.toml": ("gpt-5.6-terra", "medium"),
    "qc14-numeric-consistency-reviewer.toml": ("gpt-5.6-terra", "medium"),
    "qc14-quality-control-auditor.toml": ("gpt-5.6-sol", "high"),
    "qc14-report-generator.toml": ("gpt-5.6-terra", "medium"),
    "qc14-statistical-consistency-reviewer.toml": ("gpt-5.6-terra", "high"),
    "qc14-support-quantitative-mapper.toml": ("gpt-5.6-terra", "medium"),
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
    for label in ("validity", "importance", "action", "initials", "notes"):
        pattern = re.compile(
            rf"(?:\*\*)?{label}(?:\*\*)?\s*:\s*(?:_{{2,}}|—|-|\[\s*\])\s*$",
            re.IGNORECASE | re.MULTILINE,
        )
        if not pattern.search(tail):
            return False
    return True


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
    run_state: str, report: str, errors: list[str]
) -> tuple[float | None, str | None]:
    state = performance_fields(run_state, "run_state.md", errors)
    report_values = performance_fields(report, "Markdown report", errors)
    if state and report_values and state != report_values:
        errors.append("Performance metadata differs between run_state.md and the Markdown report.")
    if state.get("Target elapsed minutes") != "20-25":
        errors.append("Performance target must be exactly 20-25 minutes.")

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

    expected_status = None if observed is None else (
        "MET_TARGET" if observed <= 25 else "EXCEEDED_TARGET"
    )
    status = state.get("Target status")
    if expected_status and status != expected_status:
        errors.append(f"Target status must be {expected_status} for observed time {observed}.")
    causes = state.get("Exceedance causes", "")
    if status == "EXCEEDED_TARGET" and causes.casefold() in {"", "none", "n/a", "not applicable"}:
        errors.append("An exceeded target requires bounded exceedance causes.")
    return observed, status


def validate_reasoning_profile(package: Path, profile: str, errors: list[str]) -> None:
    expected = dict(COMMON_AGENT_PROFILE)
    asset_role = (
        "qc14-reuse-asset-curator.toml"
        if profile == "1.4.1"
        else "qc14-fresh-source-preprocessor.toml"
    )
    expected[asset_role] = ("gpt-5.6-terra", "medium")
    agent_dir = package / ".codex/agents"
    for filename, (model, effort) in expected.items():
        path = agent_dir / filename
        value = read(path)
        if not value:
            errors.append(f"Missing workflow-1.4 agent configuration: {filename}")
            continue
        model_match = re.search(r'^model\s*=\s*"([^"]+)"\s*$', value, re.MULTILINE)
        effort_match = re.search(
            r'^model_reasoning_effort\s*=\s*"([^"]+)"\s*$', value, re.MULTILINE
        )
        actual_model = model_match.group(1) if model_match else None
        actual_effort = effort_match.group(1) if effort_match else None
        if (actual_model, actual_effort) != (model, effort):
            errors.append(
                f"Reasoning profile mismatch for {filename}: "
                f"expected={model}/{effort} actual={actual_model}/{actual_effort}"
            )

    root_config = read(package / ".codex/config.toml")
    if not re.search(r'^model\s*=\s*"gpt-5\.6-sol"\s*$', root_config, re.MULTILINE):
        errors.append("Workflow-1.4 coordinator model must be gpt-5.6-sol.")
    if not re.search(
        r'^model_reasoning_effort\s*=\s*"high"\s*$', root_config, re.MULTILINE
    ):
        errors.append("Workflow-1.4 coordinator reasoning effort must be high.")


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
        package / f".codex/rules/workflow-{profile.replace('.', '-')}.rules",
        package / ".codex/config.toml",
    ]
    workflow_files = sorted(
        path for path in (package / f"workflow_{token}").rglob("*") if path.is_file()
    )
    agent_files = sorted((package / ".codex/agents").glob("qc14-*.toml"))
    paths = list(dict.fromkeys([*required_paths, *workflow_files, *agent_files]))
    for path in paths:
        if not path.is_file():
            errors.append(f"Missing workflow-1.4 control file: {path.relative_to(package)}")
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
    parser.add_argument("--profile", required=True, choices=("1.4.1", "1.4.2"))
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

    validate_reasoning_profile(package, args.profile, errors)
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
        errors.append("Workflow 1.4 must not create a count-limited review_queue.md.")

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

    if args.profile == "1.4.1":
        reused_path = run_dir / "reused_artifact_hashes_before.sha256"
        if not reused_path.is_file() or reused_path.stat().st_size == 0:
            errors.append("Workflow 1.4.1 requires reused_artifact_hashes_before.sha256.")
            reused_hashes: dict[str, str] = {}
        else:
            reused_hashes = parse_hash_file(reused_path, package, errors)
            verify_hashes("Reused artifact", reused_hashes, package, errors)
        new_prefix = f".ai_paper_validation/review_{token}/"
        if any(relative.startswith(new_prefix) for relative in reused_hashes):
            errors.append("The reused-artifact inventory contains new workflow-1.4.1 outputs.")

    ledger_text = read(run_dir / "candidate_ledger.md")
    recheck_text = read(run_dir / "verification/evidence_recheck.md")
    quality_text = read(run_dir / "quality/evidence_quality_audit.md")
    report_text = read(report_path)
    run_state_text = read(run_dir / "run_state.md")
    observed_minutes, target_status = validate_performance(run_state_text, report_text, errors)
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
        if (run_dir / relative).suffix.casefold() in {".md", ".sha256"}
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
            errors.append(f"{candidate_id} does not use one exact workflow-1.4 category.")
        if not human_fields_are_blank(section):
            errors.append(f"{candidate_id} human adjudication fields are absent or filled.")

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
        "schema_version": 1,
        "profile": args.profile,
        "status": "PASS" if not errors else "FAIL",
        "candidate_count": len(ledger_ids),
        "candidate_ids": ledger_ids,
        "candidate_limit": None,
        "report_all_candidates": True,
        "statistical_relationship_count": len(relationship_ids),
        "source_integrity": "PASS"
        if not any("integrity failure" in item.casefold() or "hash inventory" in item.casefold() for item in errors)
        else "FAIL",
        "agent_first": True,
        "python_role": "auxiliary-only",
        "target_minutes": "20-25",
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
