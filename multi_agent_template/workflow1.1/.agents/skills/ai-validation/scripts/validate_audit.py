#!/usr/bin/env python3
"""Validate required audit artifacts, candidate preservation, and PDF page links."""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


REQUIRED = (
    "package_manifest.md",
    "package_manifest.json",
    "run_metadata.json",
    "context_coverage.md",
    "preprocessing/page_manifest.json",
    "extraction/main_evidence.md",
    "extraction/supplement_evidence.md",
    "checkers/table_arithmetic.md",
    "checkers/figure_flow.md",
    "checkers/statistical_consistency.md",
    "candidate_registry.md",
    "statistics/coverage_matrix.md",
    "verification/evidence_recheck.md",
    "quality/evidence_quality_audit.md",
    "final_report.md",
    "final_report.html",
)
CANDIDATE_HEADING = re.compile(r"^##\s+(C\d{3,})\b", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\((?:<)?([^)>]+)(?:>)?\)")
FORBIDDEN_FIELD = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\*\*)?(severity|disposition|evidence status)(?:\*\*)?\s*:",
    re.IGNORECASE | re.MULTILINE,
)
REQUIRED_COVERAGE_STAGES = {
    "main_extraction",
    "supplement_extraction",
    "table_arithmetic",
    "figure_flow",
    "statistics_pass_1",
    "evidence_verification",
    "statistics_pass_2",
    "evidence_quality",
    "report_generation",
}


class AuditHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.ids: set[str] = set()
        self.has_toc = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(str(values["id"]))
        if tag == "nav" and values.get("id") == "TOC":
            self.has_toc = True
        if tag == "a" and values.get("href"):
            self.hrefs.append(str(values["href"]))


def candidate_sections(markdown: str) -> dict[str, str]:
    matches = list(CANDIDATE_HEADING.finditer(markdown))
    return {
        match.group(1): markdown[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(markdown)]
        for index, match in enumerate(matches)
    }


def validate_pdf_link(audit_dir: Path, href: str) -> str | None:
    split = urlsplit(href)
    if split.scheme or split.netloc or ".pdf" not in split.path.lower():
        return None
    if not re.fullmatch(r"page=[1-9]\d*", split.fragment):
        return f"PDF evidence link lacks a valid #page=N fragment: {href}"
    target = (audit_dir / unquote(split.path)).resolve()
    if not target.is_file():
        return f"PDF evidence link does not resolve: {href} -> {target}"
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit_dir", nargs="?", type=Path, default=Path("audit"))
    args = parser.parse_args()
    audit_dir = args.audit_dir.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED:
        artifact = audit_dir / relative
        if not artifact.is_file():
            errors.append(f"Missing required artifact: {relative}")
        elif artifact.stat().st_size == 0:
            errors.append(f"Required artifact is empty: {relative}")

    coverage_path = audit_dir / "context_coverage.md"
    coverage = coverage_path.read_text(encoding="utf-8") if coverage_path.is_file() else ""
    coverage_rows: list[list[str]] = []
    for line in coverage.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) == 5 and cells[0] in REQUIRED_COVERAGE_STAGES:
            coverage_rows.append(cells)
    covered_stages = {row[0] for row in coverage_rows}
    missing_stages = sorted(REQUIRED_COVERAGE_STAGES - covered_stages)
    if missing_stages:
        errors.append(f"Context coverage lacks required stages: {missing_stages}")
    seen_shards: set[tuple[str, str]] = set()
    for stage, shard_id, scope, artifact_text, status in coverage_rows:
        shard_key = (stage, shard_id)
        if not shard_id or shard_key in seen_shards:
            errors.append(f"Context coverage has a missing or duplicate shard ID: {shard_key}")
        seen_shards.add(shard_key)
        if not scope:
            errors.append(f"Context coverage has an empty scope: {shard_key}")
        allowed_status = status == "COMPLETE" or (
            stage == "supplement_extraction" and status == "NOT_APPLICABLE"
        )
        if not allowed_status:
            errors.append(f"Context coverage is incomplete: {shard_key} status={status!r}")
        if status == "COMPLETE":
            artifact = (audit_dir / artifact_text).resolve()
            try:
                artifact.relative_to(audit_dir)
            except ValueError:
                errors.append(f"Context coverage artifact escapes audit/: {artifact_text}")
            else:
                if not artifact.is_file() or artifact.stat().st_size == 0:
                    errors.append(
                        f"Context coverage artifact is missing or empty: {shard_key} -> {artifact_text}"
                    )

    registry_path = audit_dir / "candidate_registry.md"
    report_path = audit_dir / "final_report.md"
    html_path = audit_dir / "final_report.html"
    registry = registry_path.read_text(encoding="utf-8") if registry_path.is_file() else ""
    report = report_path.read_text(encoding="utf-8") if report_path.is_file() else ""
    registry_ids = CANDIDATE_HEADING.findall(registry)
    report_sections = candidate_sections(report)
    report_ids = list(report_sections)
    if len(registry_ids) != len(set(registry_ids)):
        errors.append("Candidate registry contains duplicate candidate IDs.")
    if set(registry_ids) != set(report_ids):
        errors.append(
            "Candidate preservation failure: registry/report IDs differ: "
            f"registry={registry_ids}, report={report_ids}"
        )
    if FORBIDDEN_FIELD.search(report):
        errors.append("Final report contains an AI adjudication field such as severity or disposition.")
    if "Pending Human Adjudication" not in report:
        errors.append("Final report lacks the Pending Human Adjudication notice.")

    for candidate_id, section in report_sections.items():
        links = [match.group(1) for match in MARKDOWN_LINK.finditer(section) if ".pdf" in match.group(1).lower()]
        if not links:
            errors.append(f"{candidate_id} has no PDF evidence link.")
        for link in links:
            error = validate_pdf_link(audit_dir, link)
            if error:
                errors.append(f"{candidate_id}: {error}")

    if html_path.is_file():
        rendered = html_path.read_text(encoding="utf-8")
        html_parser = AuditHTMLParser()
        html_parser.feed(rendered)
        if not html_parser.has_toc:
            errors.append("HTML report lacks a table of contents.")
        if "Pending Human Adjudication" not in rendered:
            errors.append("HTML report lacks the human-adjudication notice.")
        for href in html_parser.hrefs:
            if ".pdf" in href.lower() and "#page=" in href.lower():
                error = validate_pdf_link(audit_dir, href)
                if error:
                    errors.append(f"HTML: {error}")

    result = {
        "schema_version": 1,
        "status": "PASS" if not errors else "FAIL",
        "candidate_count": len(registry_ids),
        "registry_candidate_ids": registry_ids,
        "report_candidate_ids": report_ids,
        "errors": errors,
        "warnings": warnings,
    }
    output = audit_dir / "audit_validation.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
