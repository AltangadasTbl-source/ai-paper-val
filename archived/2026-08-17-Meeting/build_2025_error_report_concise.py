#!/home/juliz/venvs/stt/bin/python
"""Build the concise, conclusion-only edition of the 2025 error report."""

from __future__ import annotations

import collections
import datetime as dt
import re
from pathlib import Path

from build_2025_error_report import (
    ROOT,
    Finding,
    finding_sort_key,
    markdown_table,
    package_sort_key,
    parse_finding_section,
    parse_summary,
    visible_html_text,
)


OUTPUT = ROOT / "2025_paper_error_report.md"


def extract_labeled_paragraph(body: str, labels: list[str]) -> str | None:
    """Return text on/after a bold Markdown label, up to the next paragraph."""
    lines = body.splitlines()
    for label in labels:
        pattern = re.compile(
            rf"^\s*(?:-\s*)?\*\*{re.escape(label)}(?:\s+under\s+review)?[.:]?\*\*\s*(.*)$",
            re.I,
        )
        for index, line in enumerate(lines):
            match = pattern.match(line)
            if not match:
                continue
            parts: list[str] = []
            remainder = match.group(1).strip()
            if remainder:
                parts.append(remainder)
                cursor = index + 1
            else:
                cursor = index + 1
                while cursor < len(lines) and not lines[cursor].strip():
                    cursor += 1
            while cursor < len(lines):
                current = lines[cursor].strip()
                if not current or current.startswith("#"):
                    break
                if re.match(r"^(?:-\s*)?\*\*[^*]+[.:]?\*\*", current):
                    break
                parts.append(current)
                cursor += 1
            result = " ".join(parts).strip()
            result = re.sub(r"\s+", " ", result)
            return result or None
    return None


def core_statement(finding: Finding) -> str:
    issue = extract_labeled_paragraph(
        finding.body,
        ["Issue statement", "Issue statement under review"],
    )
    if issue:
        return clean_core(issue)
    conclusion = extract_labeled_paragraph(
        finding.body,
        [
            "Existing supported conclusion",
            "Supported conclusion",
            "Existing conclusion",
            "Conclusion",
        ],
    )
    if conclusion:
        return clean_core(conclusion)
    # Every source heading itself states the core mismatch. This fallback is
    # deliberately explicit rather than reconstructing new scientific claims.
    return finding.title.rstrip(".") + "."


def clean_core(text: str) -> str:
    """Remove adjudication boilerplate while preserving the error claim."""
    text = re.sub(
        r"^The critic retained an? (?:Major|Minor) [^.!?]*? because\s+",
        "",
        text,
        flags=re.I,
    )
    text = re.sub(r"^The locked finding is\s+", "", text, flags=re.I)
    if text and not re.match(r"^e(?:Table|Figure)\b", text):
        text = text[0].upper() + text[1:]
    return text


def load_findings() -> tuple[list[Finding], list[Path]]:
    md_paths = sorted(
        ROOT.glob("jama.2025.*/.ai_paper_validation/final_report.md"),
        key=lambda path: package_sort_key(path.parts[-3]),
    )
    findings: list[Finding] = []
    for md_path in md_paths:
        package = md_path.parts[-3]
        html_path = md_path.with_suffix(".html")
        lines = md_path.read_text(encoding="utf-8").splitlines()
        summary = parse_summary(lines)
        html_text = visible_html_text(html_path)
        findings.extend(
            parse_finding_section(
                lines,
                "Verified Scientific Findings",
                "Verified",
                package,
                summary,
                md_path,
                html_path,
                html_text,
            )
        )
        findings.extend(
            parse_finding_section(
                lines,
                "Uncertain Candidate",
                "Uncertain",
                package,
                summary,
                md_path,
                html_path,
                html_text,
            )
        )
    return findings, md_paths


def main() -> None:
    findings, md_paths = load_findings()
    verified = [finding for finding in findings if finding.status == "Verified"]
    uncertain = [finding for finding in findings if finding.status == "Uncertain"]
    categories = [
        "Presentation inconsistency",
        "Statistical reporting inconsistency",
        "Arithmetic inconsistency",
        "Cross-document inconsistency",
        "Participant-flow inconsistency",
        "Other or unclassified inconsistency",
    ]
    verified_counts = collections.Counter(finding.category for finding in verified)
    uncertain_counts = collections.Counter(finding.category for finding in uncertain)
    severity_counts = collections.Counter(finding.severity for finding in verified)

    out: list[str] = [
        "---",
        'title: "Concise Error Report for Audited 2025 Papers"',
        'subtitle: "All classified findings reduced to their core error statements"',
        'author: "Generated from the local AI paper-validation archive"',
        f'date: "{dt.date(2026, 8, 14).isoformat()}"',
        "lang: en-US",
        "toc: true",
        "toc-depth: 2",
        "numbersections: true",
        "---",
        "",
        "# Summary",
        "",
        f"This concise report covers **{len(md_paths)} paired validation reports**, retaining **all {len(verified)} verified report-level findings** while reducing each entry to its core conclusion: what is wrong and why the displayed information is inconsistent. Detailed calculations, step-by-step verification procedures, alternative explanations, and repeated metadata have been removed.",
        "",
        f"The report also lists **{len(uncertain)} uncertain candidates** separately. They are not counted as established errors. Counts are report-level instances rather than unique-paper error rates because `jama.2025.24175` and `jama.2025.250116` overlap on the ImmunoSep materials.",
        "",
        markdown_table(
            ["Error type", "Verified", "Uncertain"],
            [
                [category, verified_counts.get(category, 0), uncertain_counts.get(category, 0)]
                for category in categories
                if verified_counts.get(category, 0) or uncertain_counts.get(category, 0)
            ],
        ),
        "",
        markdown_table(
            ["Verified severity", "Count"],
            [[level, severity_counts[level]] for level in ["Major", "Minor"] if severity_counts[level]],
        ),
        "",
        "## Reading rule",
        "",
        "Each item below contains only the source report's conclusion-level statement (or its issue statement when no separately labeled conclusion exists). Source locations and full derivations remain available through the package report links in the source index.",
        "",
        "# Verified errors by type",
        "",
    ]

    for category in categories:
        items = sorted([finding for finding in verified if finding.category == category], key=finding_sort_key)
        if not items:
            continue
        out.extend([f"## {category} ({len(items)})", ""])
        for finding in items:
            out.extend(
                [
                    f"### {finding.package} · {finding.candidate} — {finding.title}",
                    "",
                    f"**Severity:** {finding.severity_raw}  ",
                    f"**Core error:** {core_statement(finding)}",
                    "",
                ]
            )

    out.extend(
        [
            "# Uncertain candidates",
            "",
            "These items remain unresolved because the reports lack the model output, definition, unrounded result, or other evidence needed to identify which printed element is wrong.",
            "",
        ]
    )
    for category in categories:
        items = sorted([finding for finding in uncertain if finding.category == category], key=finding_sort_key)
        if not items:
            continue
        out.extend([f"## Potential {category.lower()} ({len(items)})", ""])
        for finding in items:
            out.extend(
                [
                    f"### {finding.package} · {finding.candidate} — {finding.title}",
                    "",
                    f"**Core concern:** {core_statement(finding)}",
                    "",
                ]
            )

    out.extend(
        [
            "# Overall interpretation",
            "",
            "The most common errors are presentation failures: incorrect labels, duplicated content, incomplete table cells, mismatched units, and faulty cross-references. These errors often leave the underlying analysis unchanged but can cause readers to misidentify the population, quantity, unit, effect measure, or direction being reported.",
            "",
            "The statistical-reporting errors are less frequent but potentially more consequential. Recurring patterns include point estimates outside their own confidence intervals, inconsistent P values, reversed effect directions, incorrect analysis-set or estimand labels, and results described differently across text, tables, and figures.",
            "",
            "Arithmetic errors are usually directly recoverable from displayed numerators and denominators. Cross-document errors mainly reflect failures to propagate one authoritative result consistently through the main article and supplement. The participant-flow finding shows that mutually exclusive follow-up categories can fail to reconcile even when headline totals appear plausible.",
            "",
            "A compact publication-quality control process should therefore verify five things: numerator/denominator arithmetic, point-estimate/CI containment, consistent repeated values, correct labels and units, and valid figure/table cross-references.",
            "",
            "# Source index",
            "",
        ]
    )
    for md_path in md_paths:
        package = md_path.parts[-3]
        out.append(
            f"- **{package}:** [final_report.md]({package}/.ai_paper_validation/final_report.md); "
            f"[final_report.html]({package}/.ai_paper_validation/final_report.html)"
        )

    OUTPUT.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    missing_core = [finding for finding in findings if core_statement(finding) == finding.title.rstrip(".") + "."]
    print(f"Wrote {OUTPUT}")
    print(f"Verified findings: {len(verified)}")
    print(f"Uncertain candidates: {len(uncertain)}")
    print(f"Title-only fallbacks: {len(missing_core)}")
    for finding in missing_core:
        print(f"  {finding.package} {finding.candidate}: {finding.title}")


if __name__ == "__main__":
    main()
