#!/usr/bin/env python3
"""Validate workflow 1.2.0 source integrity, exact coverage, candidate flow, and reports."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


REQUIRED_FILES = (
    "source_inventory.json",
    "source_inventory.md",
    "source_hashes_before.json",
    "run_state.json",
    "package_manifest.json",
    "package_manifest.md",
    "source_coverage.md",
    "coverage_manifest.json",
    "rights/content_use_restriction_summary.md",
    "preprocessing/unit_manifest.json",
    "extraction/main_evidence.md",
    "extraction/support_evidence.md",
    "checkers/table_arithmetic.md",
    "checkers/figure_flow.md",
    "checkers/statistical_pass_1.md",
    "checkers/statistical_pass_2.md",
    "statistics/coverage_matrix.md",
    "statistics/coverage_matrix.json",
    "candidate_ledger.md",
    "verification/evidence_recheck.md",
    "quality/evidence_quality_audit.md",
    "review_queue.md",
    "final_report_1_2_0.md",
    "final_report_1_2_0.html",
)
REQUIRED_STAGES = {
    "source_inventory",
    "rights_screen",
    "preprocessing",
    "main_extraction",
    "support_extraction",
    "table_arithmetic",
    "figure_flow",
    "statistics_pass_1",
    "evidence_recheck",
    "statistics_pass_2",
    "evidence_quality",
    "queue_selection",
    "report_generation",
}
CANDIDATE_HEADING = re.compile(r"^##\s+(C\d{3,})\b", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\((?:<)?([^)>]+)(?:>)?\)")
FORBIDDEN_FIELD = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:severity|disposition|evidence status|validity)"
    r"(?:\*\*)?\s*:\s*\S+",
    re.IGNORECASE | re.MULTILINE,
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
    "**Bounded impact:**",
    "**Human verification steps:**",
    "**Human adjudication fields:**",
)
WORKBOOK_SUFFIXES = (".xls", ".xlsx")
DOC_SUFFIXES = (".doc", ".docx")


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


def load_json(path: Path, errors: list[str]) -> dict[str, object]:
    try:
        value = json.loads(read(path))
    except json.JSONDecodeError:
        errors.append(f"Invalid JSON: {path.name}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"JSON root is not an object: {path.name}")
        return {}
    return value


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sections(markdown: str) -> dict[str, str]:
    matches = list(CANDIDATE_HEADING.finditer(markdown))
    return {
        match.group(1): markdown[
            match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        ]
        for index, match in enumerate(matches)
    }


def local_target(base: Path, href: str) -> Path | None:
    split = urlsplit(href)
    if split.scheme or split.netloc or not split.path:
        return None
    return (base / unquote(split.path)).resolve()


def evidence_link_error(base: Path, href: str, section: str) -> str | None:
    split = urlsplit(href)
    path_lower = split.path.casefold()
    target = local_target(base, href)
    if target is None:
        return f"Evidence link is external or empty: {href}"
    if not target.is_file():
        return f"Evidence link does not resolve: {href} -> {target}"
    if path_lower.endswith(".pdf"):
        if not re.fullmatch(r"page=[1-9]\d*", split.fragment):
            return f"PDF evidence link lacks #page=N: {href}"
    elif path_lower.endswith(WORKBOOK_SUFFIXES):
        if not re.search(r"\bworksheet\b", section, flags=re.IGNORECASE) or not re.search(
            r"\bcells?\b", section, flags=re.IGNORECASE
        ):
            return f"Workbook evidence lacks worksheet and cell/range details: {href}"
    elif path_lower.endswith(DOC_SUFFIXES):
        if not re.search(
            r"\b(?:P\d{4}|T\d{3}\s+R\d{3}\s+C\d{3}|paragraph|table)\b",
            section,
            flags=re.IGNORECASE,
        ):
            return f"DOC/DOCX evidence lacks paragraph/table identifier: {href}"
    elif path_lower.endswith(".csv"):
        if not re.search(r"\brow\b", section, flags=re.IGNORECASE) or not re.search(
            r"\bcolumn\b|\bC\d+\b", section, flags=re.IGNORECASE
        ):
            return f"CSV evidence lacks row and column details: {href}"
    else:
        return f"Unsupported evidence-link format: {href}"
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, default=Path("."))
    args = parser.parse_args()
    package = args.package.expanduser().resolve()
    audit = package / ".ai_paper_validation"
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_FILES:
        path = audit / relative
        if not path.is_file():
            errors.append(f"Missing required artifact: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"Required artifact is empty: {relative}")

    inventory = load_json(audit / "source_inventory.json", errors)
    manifest = load_json(audit / "package_manifest.json", errors)
    coverage = load_json(audit / "coverage_manifest.json", errors)
    statistics = load_json(audit / "statistics/coverage_matrix.json", errors)
    hashes = load_json(audit / "source_hashes_before.json", errors)

    if inventory.get("profile") != "1.2.0" or inventory.get("preflight_status") != "FRESH_PACKAGE":
        errors.append("Source inventory is not a successful workflow-1.2.0 fresh preflight.")
    inventory_sources = inventory.get("sources", [])
    if not isinstance(inventory_sources, list):
        inventory_sources = []
        errors.append("source_inventory.json sources is not an array.")
    source_ids = [str(item.get("document_id")) for item in inventory_sources if isinstance(item, dict)]
    source_paths = [str(item.get("path")) for item in inventory_sources if isinstance(item, dict)]
    if len(source_ids) != len(set(source_ids)) or len(source_paths) != len(set(source_paths)):
        errors.append("Source inventory has duplicate document IDs or paths.")

    manifest_documents = manifest.get("documents", [])
    if not isinstance(manifest_documents, list):
        manifest_documents = []
    manifest_ids = [str(item.get("document_id")) for item in manifest_documents if isinstance(item, dict)]
    if set(manifest_ids) != set(source_ids):
        errors.append(f"Manifest/inventory document IDs differ: inventory={source_ids}, manifest={manifest_ids}")
    source_coverage = read(audit / "source_coverage.md")
    rights_summary = read(audit / "rights/content_use_restriction_summary.md")
    for document_id, path_text in zip(source_ids, source_paths):
        if path_text not in source_coverage:
            errors.append(f"Direct source absent from source_coverage.md: {path_text}")
        if document_id not in rights_summary:
            errors.append(f"Direct source lacks rights-summary entry: {document_id}")
        for record in (
            audit / "documents" / document_id / "record.md",
            audit / "rights" / "documents" / f"{document_id}.md",
        ):
            if not record.is_file() or record.stat().st_size == 0:
                errors.append(f"Missing document-level record: {record.relative_to(audit)}")

    stages = coverage.get("stages", {})
    if not isinstance(stages, dict):
        stages = {}
        errors.append("coverage_manifest.json stages is not an object.")
    missing_stages = sorted(REQUIRED_STAGES - set(stages))
    if missing_stages:
        errors.append(f"Coverage manifest lacks required stages: {missing_stages}")
    for stage_name, stage in stages.items():
        if not isinstance(stage, dict):
            errors.append(f"Coverage stage is not an object: {stage_name}")
            continue
        expected = stage.get("expected_units", [])
        completed = stage.get("completed_units", [])
        artifacts = stage.get("artifacts", [])
        if not isinstance(expected, list) or not isinstance(completed, list):
            errors.append(f"Coverage stage units are not arrays: {stage_name}")
            continue
        if len(expected) != len(set(map(str, expected))) or len(completed) != len(set(map(str, completed))):
            errors.append(f"Coverage stage has duplicate units: {stage_name}")
        if set(map(str, expected)) != set(map(str, completed)):
            errors.append(f"Coverage stage is incomplete: {stage_name}")
        if not isinstance(artifacts, list) or not artifacts:
            errors.append(f"Coverage stage has no artifact list: {stage_name}")
        else:
            for artifact_text in artifacts:
                artifact = (audit / str(artifact_text)).resolve()
                try:
                    artifact.relative_to(audit)
                except ValueError:
                    errors.append(f"Coverage artifact escapes audit root: {artifact_text}")
                else:
                    if not artifact.is_file() or artifact.stat().st_size == 0:
                        errors.append(f"Coverage artifact missing or empty: {stage_name} -> {artifact_text}")
    for stage_name in ("source_inventory", "rights_screen", "preprocessing"):
        stage = stages.get(stage_name, {}) if isinstance(stages, dict) else {}
        if set(map(str, stage.get("expected_units", []))) != set(source_ids):
            errors.append(f"{stage_name} expected units do not equal all direct document IDs.")

    relationships = statistics.get("relationships", [])
    if not isinstance(relationships, list):
        relationships = []
        errors.append("Statistics relationships is not an array.")
    relationship_ids: list[str] = []
    for relationship in relationships:
        if not isinstance(relationship, dict):
            errors.append("Statistics relationship is not an object.")
            continue
        relationship_id = str(relationship.get("id", ""))
        relationship_ids.append(relationship_id)
        if not re.fullmatch(r"S\d{3,}", relationship_id):
            errors.append(f"Invalid statistical relationship ID: {relationship_id}")
        if relationship.get("pass_1") != "COMPLETE" or relationship.get("pass_2") != "COMPLETE":
            errors.append(f"Statistical relationship lacks both completed passes: {relationship_id}")
    if len(relationship_ids) != len(set(relationship_ids)):
        errors.append("Statistical coverage matrix has duplicate relationship IDs.")
    for stage_name in ("statistics_pass_1", "statistics_pass_2"):
        stage = stages.get(stage_name, {}) if isinstance(stages, dict) else {}
        if set(map(str, stage.get("expected_units", []))) != set(relationship_ids):
            errors.append(f"{stage_name} coverage units differ from the statistical relationship set.")

    ledger_text = read(audit / "candidate_ledger.md")
    recheck_text = read(audit / "verification/evidence_recheck.md")
    quality_text = read(audit / "quality/evidence_quality_audit.md")
    queue_text = read(audit / "review_queue.md")
    report_path = audit / "final_report_1_2_0.md"
    report_text = read(report_path)
    html_path = audit / "final_report_1_2_0.html"
    candidate_sets = {
        "ledger": CANDIDATE_HEADING.findall(ledger_text),
        "recheck": CANDIDATE_HEADING.findall(recheck_text),
        "quality": CANDIDATE_HEADING.findall(quality_text),
        "queue": CANDIDATE_HEADING.findall(queue_text),
    }
    report_sections = sections(report_text)
    candidate_sets["report"] = list(report_sections)
    for label, values in candidate_sets.items():
        if len(values) != len(set(values)):
            errors.append(f"Duplicate candidate ID in {label}: {values}")
    ledger_ids = candidate_sets["ledger"]
    if set(candidate_sets["recheck"]) != set(ledger_ids):
        errors.append("Ledger/recheck candidate IDs differ.")
    if set(candidate_sets["quality"]) != set(ledger_ids):
        errors.append("Ledger/quality candidate IDs differ.")
    if not set(candidate_sets["queue"]).issubset(set(ledger_ids)):
        errors.append("Review queue contains an ID absent from the ledger.")
    if len(candidate_sets["queue"]) > 10:
        errors.append(f"Review queue exceeds 10: {len(candidate_sets['queue'])}")
    if set(candidate_sets["queue"]) != set(candidate_sets["report"]):
        errors.append("Review queue and final report candidate IDs differ.")
    for candidate_id, section in sections(ledger_text).items():
        if "**Queue routing status:**" not in section:
            errors.append(f"Ledger candidate lacks queue routing status: {candidate_id}")

    stage_expectations = {
        "evidence_recheck": ledger_ids,
        "evidence_quality": ledger_ids,
        "queue_selection": ledger_ids,
        "report_generation": candidate_sets["queue"],
    }
    for stage_name, expected_ids in stage_expectations.items():
        stage = stages.get(stage_name, {}) if isinstance(stages, dict) else {}
        if set(map(str, stage.get("expected_units", []))) != set(expected_ids):
            errors.append(f"{stage_name} expected units differ from required candidate IDs.")

    if "Pending Human Adjudication" not in report_text:
        errors.append("Markdown report lacks Pending Human Adjudication notice.")
    if FORBIDDEN_FIELD.search(report_text):
        errors.append("Report contains a filled AI adjudication field.")
    source_suffixes = (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".csv")
    for candidate_id, section in report_sections.items():
        for field in CARD_FIELDS:
            if field not in section:
                errors.append(f"{candidate_id} lacks required field {field}")
        evidence_links = [
            match.group(1)
            for match in MARKDOWN_LINK.finditer(section)
            if urlsplit(match.group(1)).path.casefold().endswith(source_suffixes)
        ]
        if not evidence_links:
            errors.append(f"{candidate_id} has no source evidence link.")
        for href in evidence_links:
            error = evidence_link_error(report_path.parent, href, section)
            if error:
                errors.append(f"{candidate_id}: {error}")

    source_integrity_failed = False
    hash_sources = hashes.get("sources", [])
    if not isinstance(hash_sources, list):
        hash_sources = []
    if {str(item.get("path")) for item in hash_sources if isinstance(item, dict)} != set(source_paths):
        errors.append("Source hash record does not cover exactly the direct source set.")
    for entry in hash_sources:
        if not isinstance(entry, dict):
            continue
        source = package / str(entry.get("path", ""))
        if not source.is_file():
            errors.append(f"Source disappeared: {entry.get('path')}")
            source_integrity_failed = True
        elif source.stat().st_size != entry.get("bytes") or sha256(source) != entry.get("sha256"):
            errors.append(f"Source integrity failure: {entry.get('path')}")
            source_integrity_failed = True

    if html_path.is_file():
        html_text = read(html_path)
        html_parser = ReportHTMLParser()
        html_parser.feed(html_text)
        if "<html" not in html_text.casefold():
            errors.append("HTML report is not standalone HTML.")
        if not html_parser.has_toc:
            errors.append("HTML report lacks a table of contents.")
        if "Pending Human Adjudication" not in html_text:
            errors.append("HTML report lacks Pending Human Adjudication notice.")
        for href in html_parser.hrefs:
            if urlsplit(href).path.casefold().endswith(source_suffixes):
                error = evidence_link_error(html_path.parent, href, html_text)
                if error:
                    errors.append(f"HTML: {error}")

    result = {
        "schema_version": 1,
        "profile": "1.2.0",
        "status": "PASS" if not errors else "FAIL",
        "source_count": len(source_ids),
        "statistical_relationship_count": len(relationship_ids),
        "ledger_candidate_count": len(ledger_ids),
        "review_queue_count": len(candidate_sets["queue"]),
        "queue_candidate_ids": candidate_sets["queue"],
        "source_integrity": "FAIL" if source_integrity_failed else "PASS",
        "cpu_only": True,
        "errors": errors,
        "warnings": warnings,
    }
    audit.mkdir(parents=True, exist_ok=True)
    (audit / "audit_validation_1_2_0.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
