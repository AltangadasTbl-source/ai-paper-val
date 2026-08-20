#!/usr/bin/env python3
"""Validate legacy recovery coverage, queue cap, report cards, links, and source integrity."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


CANDIDATE_HEADING = re.compile(r"^##\s+((?:C\d{2,}|R\d{3,}))\b", re.MULTILINE)
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
REQUIRED_PATCH_FILES = (
    "legacy_inventory.json",
    "legacy_inventory.md",
    "run_state.json",
    "source_hashes_before.json",
    "legacy_source_coverage.md",
    "lineage_map.md",
    "recovered_candidate_ledger.md",
    "evidence_recheck.md",
    "statistical_reconciliation.md",
    "review_queue.md",
    "quality_audit.md",
    "recovery_log.md",
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


def validate_pdf_link(base: Path, href: str) -> str | None:
    split = urlsplit(href)
    if split.scheme or split.netloc or ".pdf" not in split.path.casefold():
        return None
    if not re.fullmatch(r"page=[1-9]\d*", split.fragment):
        return f"PDF evidence link lacks a valid #page=N fragment: {href}"
    target = (base / unquote(split.path)).resolve()
    if not target.is_file():
        return f"PDF evidence link does not resolve: {href} -> {target}"
    return None


def validate_workbook_link(base: Path, href: str) -> str | None:
    split = urlsplit(href)
    if split.scheme or split.netloc or not split.path.casefold().endswith(WORKBOOK_SUFFIXES):
        return None
    target = (base / unquote(split.path)).resolve()
    if not target.is_file():
        return f"Workbook evidence link does not resolve: {href} -> {target}"
    return None


def validate_plain_source_link(base: Path, href: str) -> str | None:
    split = urlsplit(href)
    if split.scheme or split.netloc:
        return f"Source evidence link is external: {href}"
    target = (base / unquote(split.path)).resolve()
    if not target.is_file():
        return f"Source evidence link does not resolve: {href} -> {target}"
    return None


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, choices=("1.2.1", "1.2.2"))
    parser.add_argument("--package", type=Path, default=Path("."))
    args = parser.parse_args()

    package = args.package.expanduser().resolve()
    legacy = package / ".ai_paper_validation"
    version_token = args.profile.replace(".", "_")
    patch_dir = legacy / f"patch_{version_token}"
    report_path = legacy / f"final_report_{version_token}.md"
    html_path = legacy / f"final_report_{version_token}.html"
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_PATCH_FILES:
        path = patch_dir / relative
        if not path.is_file():
            errors.append(f"Missing required patch artifact: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"Required patch artifact is empty: {relative}")
    if args.profile == "1.2.2":
        endetail_harvest = patch_dir / "endetail_harvest.md"
        if not endetail_harvest.is_file() or endetail_harvest.stat().st_size == 0:
            errors.append("Patch 1.2.2 requires a nonempty endetail_harvest.md artifact.")
    for path in (report_path, html_path):
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Missing or empty versioned report: {path.name}")

    inventory_path = patch_dir / "legacy_inventory.json"
    try:
        inventory = json.loads(read(inventory_path))
    except json.JSONDecodeError:
        inventory = {}
        errors.append("legacy_inventory.json is invalid JSON.")
    if inventory.get("profile") != args.profile:
        errors.append("Inventory profile does not match requested validator profile.")
    expected_endetail = "ENDDETAIL_DETECTED" if args.profile == "1.2.2" else "NOT_DETAILED"
    if inventory.get("endetail_detection", {}).get("status") != expected_endetail:
        errors.append(f"Profile requires endetail status {expected_endetail}.")

    coverage = read(patch_dir / "legacy_source_coverage.md")
    for candidate_source in inventory.get("candidate_sources", []):
        if str(candidate_source) not in coverage:
            errors.append(f"Candidate-bearing legacy artifact lacks source coverage: {candidate_source}")

    ledger_text = read(patch_dir / "recovered_candidate_ledger.md")
    recheck_text = read(patch_dir / "evidence_recheck.md")
    queue_text = read(patch_dir / "review_queue.md")
    quality_text = read(patch_dir / "quality_audit.md")
    report_text = read(report_path)
    ledger_ids = CANDIDATE_HEADING.findall(ledger_text)
    recheck_ids = CANDIDATE_HEADING.findall(recheck_text)
    queue_ids = CANDIDATE_HEADING.findall(queue_text)
    quality_ids = CANDIDATE_HEADING.findall(quality_text)
    report_sections = sections(report_text)
    report_ids = list(report_sections)

    for label, values in (
        ("ledger", ledger_ids),
        ("recheck", recheck_ids),
        ("queue", queue_ids),
        ("quality", quality_ids),
        ("report", report_ids),
    ):
        if len(values) != len(set(values)):
            errors.append(f"Duplicate candidate ID in {label}: {values}")
    if set(ledger_ids) != set(recheck_ids):
        errors.append("Recovered ledger and evidence recheck IDs differ.")
    if not set(queue_ids).issubset(set(ledger_ids)):
        errors.append("Review queue contains an ID absent from the recovered ledger.")
    if len(queue_ids) > 10:
        errors.append(f"Review queue exceeds the cap of 10: {len(queue_ids)}")
    if set(queue_ids) != set(report_ids):
        errors.append(f"Queue/report IDs differ: queue={queue_ids}, report={report_ids}")
    if set(ledger_ids) != set(quality_ids):
        errors.append("Quality audit must cover every recovered ledger ID.")

    if "Pending Human Adjudication" not in report_text:
        errors.append("Markdown report lacks Pending Human Adjudication notice.")
    if FORBIDDEN_FIELD.search(report_text):
        errors.append("Report contains a filled AI adjudication field.")
    for candidate_id, section in report_sections.items():
        for field in CARD_FIELDS:
            if field not in section:
                errors.append(f"{candidate_id} lacks required field {field}")
        links = [match.group(1) for match in MARKDOWN_LINK.finditer(section)]
        pdf_links = [link for link in links if ".pdf" in urlsplit(link).path.casefold()]
        workbook_links = [
            link for link in links if urlsplit(link).path.casefold().endswith(WORKBOOK_SUFFIXES)
        ]
        doc_links = [link for link in links if urlsplit(link).path.casefold().endswith(DOC_SUFFIXES)]
        csv_links = [link for link in links if urlsplit(link).path.casefold().endswith(".csv")]
        if not pdf_links and not workbook_links and not doc_links and not csv_links:
            errors.append(f"{candidate_id} has no PDF, Office, or CSV evidence link.")
        if workbook_links and not (
            re.search(r"\bworksheet\b", section, re.IGNORECASE)
            and re.search(r"\bcells?\b", section, re.IGNORECASE)
        ):
            errors.append(f"{candidate_id} workbook evidence lacks worksheet and cell details.")
        for link in pdf_links:
            error = validate_pdf_link(report_path.parent, link)
            if error:
                errors.append(f"{candidate_id}: {error}")
        for link in workbook_links:
            error = validate_workbook_link(report_path.parent, link)
            if error:
                errors.append(f"{candidate_id}: {error}")
        if doc_links and not re.search(
            r"\b(?:P\d{4}|T\d{3}\s+R\d{3}\s+C\d{3}|paragraph|table)\b",
            section,
            re.IGNORECASE,
        ):
            errors.append(f"{candidate_id} DOC/DOCX evidence lacks paragraph/table details.")
        if csv_links and not (
            re.search(r"\brow\b", section, re.IGNORECASE)
            and re.search(r"\bcolumn\b|\bC\d+\b", section, re.IGNORECASE)
        ):
            errors.append(f"{candidate_id} CSV evidence lacks row and column details.")
        for link in [*doc_links, *csv_links]:
            error = validate_plain_source_link(report_path.parent, link)
            if error:
                errors.append(f"{candidate_id}: {error}")

    hashes_path = patch_dir / "source_hashes_before.json"
    try:
        before = json.loads(read(hashes_path)).get("sources", [])
    except json.JSONDecodeError:
        before = []
        errors.append("source_hashes_before.json is invalid JSON.")
    for entry in before:
        source = package / str(entry.get("path", ""))
        if not source.is_file():
            errors.append(f"Source disappeared after preflight: {entry.get('path')}")
        elif source.stat().st_size != entry.get("bytes") or sha256(source) != entry.get("sha256"):
            errors.append(f"Source integrity failure: {entry.get('path')}")

    for entry in inventory.get("legacy_files", []):
        artifact = legacy / str(entry.get("path", ""))
        if not artifact.is_file():
            errors.append(f"Legacy artifact disappeared after preflight: {entry.get('path')}")
        elif artifact.stat().st_size != entry.get("bytes") or sha256(artifact) != entry.get("sha256"):
            errors.append(f"Legacy artifact integrity failure: {entry.get('path')}")

    if html_path.is_file():
        html = read(html_path)
        parser_html = ReportHTMLParser()
        parser_html.feed(html)
        if "<html" not in html.casefold():
            errors.append("HTML report is not standalone HTML.")
        if not parser_html.has_toc:
            errors.append("HTML report lacks a table of contents.")
        if "Pending Human Adjudication" not in html:
            errors.append("HTML report lacks Pending Human Adjudication notice.")
        for href in parser_html.hrefs:
            if ".pdf" in href.casefold() and "#page=" in href.casefold():
                error = validate_pdf_link(html_path.parent, href)
                if error:
                    errors.append(f"HTML: {error}")
            elif urlsplit(href).path.casefold().endswith(WORKBOOK_SUFFIXES):
                error = validate_workbook_link(html_path.parent, href)
                if error:
                    errors.append(f"HTML: {error}")
            elif urlsplit(href).path.casefold().endswith((*DOC_SUFFIXES, ".csv")):
                error = validate_plain_source_link(html_path.parent, href)
                if error:
                    errors.append(f"HTML: {error}")

    result = {
        "schema_version": 1,
        "profile": args.profile,
        "status": "PASS" if not errors else "FAIL",
        "ledger_candidate_count": len(ledger_ids),
        "review_queue_count": len(queue_ids),
        "queue_candidate_ids": queue_ids,
        "report_candidate_ids": report_ids,
        "source_integrity": "PASS" if not any("integrity" in item.casefold() for item in errors) else "FAIL",
        "cpu_only": True,
        "errors": errors,
        "warnings": warnings,
    }
    patch_dir.mkdir(parents=True, exist_ok=True)
    (patch_dir / "patch_validation.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
