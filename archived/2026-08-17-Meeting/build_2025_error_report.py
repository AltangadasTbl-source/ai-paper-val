#!/home/juliz/venvs/stt/bin/python
"""Build an exhaustive, categorized Markdown report from 2025 validation reports."""

from __future__ import annotations

import collections
import datetime as dt
import html
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "2025_paper_error_report.md"


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


@dataclass
class SummaryRow:
    candidate: str
    key: str
    disposition: str
    category_raw: str
    severity_raw: str


@dataclass
class Finding:
    package: str
    candidate: str
    key: str
    title: str
    status: str
    category: str
    category_raw: str
    severity: str
    severity_raw: str
    body: str
    md_path: Path
    html_path: Path
    html_confirmed: bool


def plain(text: str) -> str:
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    return html.unescape(text).strip()


def candidate_key(text: str) -> str | None:
    cleaned = plain(text)
    match = re.match(r"\s*((?:C|V)\s*-?\s*\d+|\d+)\b", cleaned, re.I)
    if not match:
        return None
    token = re.sub(r"\s+", "", match.group(1)).upper()
    letter = token[0] if token[0].isalpha() else ""
    digits = re.sub(r"\D", "", token)
    return f"{letter}{int(digits)}"


def heading(line: str) -> tuple[int, str] | None:
    match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
    if not match:
        return None
    return len(match.group(1)), plain(match.group(2))


def section_bounds(lines: list[str], phrase: str) -> tuple[int, int, int] | None:
    for index, line in enumerate(lines):
        parsed = heading(line)
        if not parsed:
            continue
        level, title = parsed
        if phrase.lower() not in title.lower():
            continue
        end = len(lines)
        for next_index in range(index + 1, len(lines)):
            next_heading = heading(lines[next_index])
            if next_heading and next_heading[0] <= level:
                end = next_index
                break
        return index + 1, end, level
    return None


def parse_summary(lines: list[str]) -> dict[str, SummaryRow]:
    bounds = section_bounds(lines, "Candidate Disposition Summary")
    if not bounds:
        return {}
    start, end, _ = bounds
    rows: dict[str, SummaryRow] = {}
    for line in lines[start:end]:
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0].lower() == "candidate":
            continue
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells[:4]):
            continue
        key = candidate_key(cells[0])
        if not key:
            continue
        rows[key] = SummaryRow(
            candidate=plain(cells[0]),
            key=key,
            disposition=plain(cells[1]),
            category_raw=plain(cells[2]),
            severity_raw=plain(cells[3]),
        )
    return rows


def normalize_category(raw: str) -> str:
    value = raw.lower()
    if "participant flow" in value:
        return "Participant-flow inconsistency"
    if "arithmetic" in value:
        return "Arithmetic inconsistency"
    if "cross-document" in value:
        return "Cross-document inconsistency"
    if "statistical" in value:
        return "Statistical reporting inconsistency"
    if "presentation" in value:
        return "Presentation inconsistency"
    return "Other or unclassified inconsistency"


def normalize_severity(raw: str) -> str:
    value = raw.lower()
    if "major" in value:
        return "Major"
    if "moderate" in value:
        return "Moderate"
    if "minor" in value:
        return "Minor"
    if "uncertain" in value or "potential" in value:
        return "Uncertain"
    return "Not assigned"


def visible_html_text(path: Path) -> str:
    parser = VisibleTextParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return re.sub(r"\s+", " ", " ".join(parser.parts)).casefold()


def repair_links(text: str, package: str) -> str:
    def replace(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        if target.startswith("../"):
            target = f"{package}/{target[3:]}"
        return f"[{label}]({target})"

    text = re.sub(r"\[([^]]+)\]\(([^)]+)\)", replace, text)
    # GFM does not recognize the source reports' LaTeX \[...\] form.
    # Normalize delimiter-only lines so Pandoc typesets, rather than prints,
    # the six display equations in jama.2025.19843.
    text = re.sub(r"(?m)^(\s*)\\\[\s*$", r"\1$$", text)
    text = re.sub(r"(?m)^(\s*)\\\]\s*$", r"\1$$", text)
    return text


def demote_body_headings(body_lines: list[str], original_candidate_level: int) -> str:
    output: list[str] = []
    for line in body_lines:
        parsed = heading(line)
        if parsed and parsed[0] > original_candidate_level:
            new_level = min(6, 3 + parsed[0] - original_candidate_level)
            output.append(f"{'#' * new_level} {line.split(maxsplit=1)[1]}")
        else:
            output.append(line)
    return "\n".join(output).strip()


def parse_finding_section(
    lines: list[str],
    phrase: str,
    status: str,
    package: str,
    summary: dict[str, SummaryRow],
    md_path: Path,
    html_path: Path,
    html_text: str,
) -> list[Finding]:
    bounds = section_bounds(lines, phrase)
    if not bounds:
        return []
    start, end, section_level = bounds
    candidates: list[tuple[int, int, str, str, int]] = []
    for index in range(start, end):
        parsed = heading(lines[index])
        if not parsed:
            continue
        level, title = parsed
        if level != section_level + 1:
            continue
        key = candidate_key(title)
        if not key:
            continue
        match = re.match(r"\s*((?:C|V)\s*-?\s*\d+|\d+)\s*(?:[.—–-]+)?\s*(.*)", title, re.I)
        if not match:
            continue
        candidate = re.sub(r"\s+", "", match.group(1)).upper()
        issue_title = match.group(2).strip() or title
        candidates.append((index, level, candidate, issue_title, key))

    findings: list[Finding] = []
    for position, (index, level, candidate, title, key) in enumerate(candidates):
        block_end = candidates[position + 1][0] if position + 1 < len(candidates) else end
        body = demote_body_headings(lines[index + 1 : block_end], level)
        row = summary.get(key)
        category_raw = row.category_raw if row else "Not assigned"
        severity_raw = row.severity_raw if row else "Not assigned"
        title_in_html = re.sub(r"\s+", " ", title).casefold() in html_text
        findings.append(
            Finding(
                package=package,
                candidate=candidate,
                key=key,
                title=title,
                status=status,
                category=normalize_category(category_raw),
                category_raw=category_raw,
                severity=normalize_severity(severity_raw),
                severity_raw=severity_raw,
                body=repair_links(body, package),
                md_path=md_path,
                html_path=html_path,
                html_confirmed=title_in_html,
            )
        )
    return findings


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    rendered = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows:
        rendered.append("| " + " | ".join(str(cell).replace("|", "\\|") for cell in row) + " |")
    return "\n".join(rendered)


def package_sort_key(name: str) -> tuple[int, str]:
    match = re.search(r"(\d+)$", name)
    return (int(match.group(1)) if match else 0, name)


def finding_sort_key(finding: Finding) -> tuple[tuple[int, str], str]:
    return package_sort_key(finding.package), finding.key


def main() -> None:
    md_paths = sorted(ROOT.glob("jama.2025.*/.ai_paper_validation/final_report.md"), key=lambda p: package_sort_key(p.parts[-3]))
    if not md_paths:
        raise SystemExit("No jama.2025.* final_report.md sources found")

    findings: list[Finding] = []
    source_checks: list[list[object]] = []
    summary_sizes: dict[str, int] = {}
    for md_path in md_paths:
        package = md_path.parts[-3]
        html_path = md_path.with_suffix(".html")
        if not html_path.exists():
            raise SystemExit(f"Missing paired HTML report: {html_path}")
        lines = md_path.read_text(encoding="utf-8").splitlines()
        summary = parse_summary(lines)
        summary_sizes[package] = len(summary)
        html_text = visible_html_text(html_path)
        current = []
        current.extend(parse_finding_section(lines, "Verified Scientific Findings", "Verified", package, summary, md_path, html_path, html_text))
        current.extend(parse_finding_section(lines, "Uncertain Candidate", "Uncertain", package, summary, md_path, html_path, html_text))
        findings.extend(current)
        confirmed = sum(item.html_confirmed for item in current)
        source_checks.append([package, len(summary), sum(item.status == "Verified" for item in current), sum(item.status == "Uncertain" for item in current), f"{confirmed}/{len(current)}"])

    verified = [item for item in findings if item.status == "Verified"]
    uncertain = [item for item in findings if item.status == "Uncertain"]
    verified_category = collections.Counter(item.category for item in verified)
    uncertain_category = collections.Counter(item.category for item in uncertain)
    verified_severity = collections.Counter(item.severity for item in verified)
    per_package: list[list[object]] = []
    for package in sorted({item.package for item in findings}, key=package_sort_key):
        package_findings = [item for item in findings if item.package == package]
        per_package.append(
            [
                package,
                sum(item.status == "Verified" for item in package_findings),
                sum(item.status == "Uncertain" for item in package_findings),
                sum(item.status == "Verified" and item.severity == "Major" for item in package_findings),
            ]
        )

    category_order = [
        "Presentation inconsistency",
        "Statistical reporting inconsistency",
        "Arithmetic inconsistency",
        "Cross-document inconsistency",
        "Participant-flow inconsistency",
        "Other or unclassified inconsistency",
    ]

    out: list[str] = []
    out.extend(
        [
            "---",
            'title: "Detailed Error Report for Audited 2025 Papers"',
            'subtitle: "Exhaustive synthesis of paired final_report.md and final_report.html artifacts"',
            'author: "Generated from the local AI paper-validation archive"',
            f'date: "{dt.date(2026, 8, 14).isoformat()}"',
            "lang: en-US",
            "toc: true",
            "toc-depth: 3",
            "numbersections: true",
            "---",
            "",
            "# Executive summary",
            "",
            f"This report synthesizes **{len(md_paths)} paired Markdown/HTML validation reports** for local packages whose identifiers begin with `jama.2025.`. It retains **all {len(verified)} verified report-level findings** and **all {len(uncertain)} uncertain candidate records** that have dedicated detailed write-ups. The counts are *report-level finding instances*, not an estimate of unique underlying errors or an error rate among all published 2025 papers.",
            "",
            "Every detailed title extracted from Markdown was checked against the paired HTML rendering. The catalog preserves the source reports' own classifications, severity labels, locations, numerical checks, interpretive limits, and verification or correction instructions. Rejected or explicitly excluded interpretations are not counted as errors because the source reports did not establish them as findings.",
            "",
            "The dominant pattern is editorial and presentation control rather than a single computational failure mode. Presentation problems include ambiguous or incorrect labels, duplicated rows or figures, wrong units, incomplete headers, and broken cross-references. Statistical-reporting problems include confidence intervals that do not contain their point estimates, discordant inferential values, mislabeled estimands, and effect directions or analysis labels inconsistent with definitions. Arithmetic findings are usually locally recoverable from displayed counts and denominators. Cross-document findings arise when the main article, supplement, figure, table, or narrative repeats the same quantity inconsistently.",
            "",
            "## Headline counts",
            "",
            markdown_table(
                ["Status", "Report-level instances"],
                [["Verified findings", len(verified)], ["Uncertain candidates", len(uncertain)], ["Total detailed records", len(findings)]],
            ),
            "",
            markdown_table(
                ["Verified severity", "Count"],
                [[severity, verified_severity.get(severity, 0)] for severity in ["Major", "Moderate", "Minor", "Uncertain", "Not assigned"] if verified_severity.get(severity, 0)],
            ),
            "",
            "## Verified findings by error type",
            "",
            markdown_table(
                ["Error type", "Verified", "Uncertain"],
                [[category, verified_category.get(category, 0), uncertain_category.get(category, 0)] for category in category_order if verified_category.get(category, 0) or uncertain_category.get(category, 0)],
            ),
            "",
            "## Package-level distribution",
            "",
            markdown_table(["Package", "Verified", "Uncertain", "Verified major"], per_package),
            "",
            "# Scope, evidence, and counting rules",
            "",
            "The user-specified path `./paper/.ai-validation/` was not present. A workspace-wide search located the 14 report pairs listed below under `jama.2025.*/.ai_paper_validation/`; these are the complete matching `final_report.md` and `final_report.html` artifacts used here.",
            "",
            "For each package, the Markdown report supplied the structured text and the HTML report served as a rendering cross-check. Candidate category and severity were taken from the package's Candidate Disposition Summary. Final inclusion followed the detailed **Verified Scientific Findings** and **Uncertain Candidates** sections, which is important where a verifier-stage disposition was later narrowed by a critic-stage decision. No web source or evidence outside the local report pairs was used.",
            "",
            "A verified finding is counted once each time it appears as a detailed verified finding in a package report. An uncertain candidate is tabulated separately and is not promoted to an error. Categories with qualified wording such as “potential statistical reporting inconsistency” are normalized to the corresponding base category for aggregation; the original wording remains in each record. Major-if-confirmed wording is retained as Major in the uncertain record's metadata, but not counted among verified major findings.",
            "",
            "## Markdown–HTML reconciliation",
            "",
            markdown_table(["Package", "Summary-table rows", "Detailed verified", "Detailed uncertain", "Titles found in HTML"], source_checks),
            "",
            "# Cross-package overlap and adjudication differences",
            "",
            "The packages `jama.2025.24175` and `jama.2025.250116` concern the same ImmunoSep materials. Their records must not be treated as statistically independent observations. This report keeps both because the request is exhaustive and because their adjudications differ:",
            "",
            "- The day-15 SOFA numerator conflict appears as 24175 item 1 and 250116 C01; both are verified.",
            "- The eTable 10/SII odds-ratio discrepancy appears as 24175 item 2 and 250116 C02; both are verified.",
            "- The eFigure 8B/eFigure 7B duplication appears as 24175 item 4 and 250116 C04; both are verified.",
            "- The eFigure 9 APACHE odds-ratio/CI issue is uncertain in 24175 item 3 but verified in 250116 C03.",
            "- Two malformed eTable 14 cells are described as rejected/recoverable in 24175 appendix B, but are verified separately as 250116 C06 and C07.",
            "",
            "Accordingly, headline numbers are explicitly labeled report-level instances. For decision-making on ImmunoSep, the later or otherwise authoritative package should be selected by a human reviewer; this synthesis does not silently override either final report.",
            "",
            "# Detailed verified findings, grouped by error type",
            "",
        ]
    )

    for category in category_order:
        items = sorted([item for item in verified if item.category == category], key=finding_sort_key)
        if not items:
            continue
        out.extend([f"## {category}", "", f"**{len(items)} verified report-level finding{'s' if len(items) != 1 else ''}.**", ""])
        for item in items:
            out.extend(
                [
                    f"### {item.package} · {item.candidate} — {item.title}",
                    "",
                    f"**Status:** Verified  ",
                    f"**Category:** {item.category_raw}  ",
                    f"**Severity:** {item.severity_raw}  ",
                    f"**Source reports:** [Markdown]({item.package}/.ai_paper_validation/final_report.md); [HTML]({item.package}/.ai_paper_validation/final_report.html)  ",
                    f"**HTML title cross-check:** {'Confirmed' if item.html_confirmed else 'Not matched automatically; inspect manually'}",
                    "",
                    item.body,
                    "",
                ]
            )

    out.extend(["# Detailed uncertain candidates, grouped by potential error type", "", "These records are included for completeness but are not counted as established errors. Each requires the additional evidence or model-output confirmation stated in its source write-up.", ""])
    for category in category_order:
        items = sorted([item for item in uncertain if item.category == category], key=finding_sort_key)
        if not items:
            continue
        out.extend([f"## {category}", ""])
        for item in items:
            out.extend(
                [
                    f"### {item.package} · {item.candidate} — {item.title}",
                    "",
                    f"**Status:** Uncertain; not an established error  ",
                    f"**Potential category:** {item.category_raw}  ",
                    f"**Potential severity:** {item.severity_raw}  ",
                    f"**Source reports:** [Markdown]({item.package}/.ai_paper_validation/final_report.md); [HTML]({item.package}/.ai_paper_validation/final_report.html)  ",
                    f"**HTML title cross-check:** {'Confirmed' if item.html_confirmed else 'Not matched automatically; inspect manually'}",
                    "",
                    item.body,
                    "",
                ]
            )

    top_category, top_count = verified_category.most_common(1)[0]
    major_packages = sorted({item.package for item in verified if item.severity == "Major"}, key=package_sort_key)
    out.extend(
        [
            "# Related summary and implications",
            "",
            f"Across the {len(verified)} verified report-level findings, **{top_category.lower()}** is the largest normalized class ({top_count} instances). This class is broad: it includes errors in headings, labels, denominator descriptions, units, duplicated content, and cross-references. Its frequency indicates that final production and consistency review is at least as important as recomputation of numerical results.",
            "",
            f"The verified Major findings occur in {len(major_packages)} package(s): {', '.join(f'`{name}`' for name in major_packages)}. These deserve priority because their source reports identify risks such as unreconciled analysis populations, invalid or duplicated inferential displays, reversed treatment-effect statements, incompatible analysis-unit labels, or substantial cross-document conflicts. Minor does not mean ignorable: many Minor findings are easy to correct and can still mislead readers, prevent reproduction, or undermine confidence in a table.",
            "",
            "The findings suggest five recurring quality-control checks:",
            "",
            "1. Recompute every percentage from its displayed numerator and explicit denominator, including missing-data exclusions.",
            "2. Require every point estimate to lie within its printed confidence interval and verify that interval endpoints are ordered lower-to-upper.",
            "3. Reconcile repeated results across abstract, narrative, tables, figures, and supplements from one authoritative output table.",
            "4. Validate every label against the estimand, analysis unit, unit of measure, summary statistic, and adjusted/unadjusted status actually used.",
            "5. Run duplication and cross-reference checks on rows, panels, captions, supplementary figure numbers, and table citations before publication.",
            "",
            "The eight uncertain records should be resolved with the exact additional evidence named in their descriptions—for example, model-output definitions, source datasets, unrounded estimates, or authoritative production exports. They should not be corrected by inference from rounded displays alone.",
            "",
            "# Source index",
            "",
        ]
    )
    for md_path in md_paths:
        package = md_path.parts[-3]
        out.append(f"- **{package}:** [final_report.md]({package}/.ai_paper_validation/final_report.md); [final_report.html]({package}/.ai_paper_validation/final_report.html)")

    output_text = "\n".join(out).rstrip() + "\n"
    OUTPUT.write_text(output_text, encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    print(f"Packages: {len(md_paths)}")
    print(f"Verified findings: {len(verified)}")
    print(f"Uncertain candidates: {len(uncertain)}")
    print("Verified by category:")
    for category in category_order:
        if verified_category.get(category):
            print(f"  {category}: {verified_category[category]}")
    print("Verified by severity:")
    for severity, count in verified_severity.items():
        print(f"  {severity}: {count}")
    failed_html = [f"{item.package} {item.candidate}" for item in findings if not item.html_confirmed]
    print(f"HTML title cross-check failures: {len(failed_html)}")
    if failed_html:
        print("  " + ", ".join(failed_html))


if __name__ == "__main__":
    main()
