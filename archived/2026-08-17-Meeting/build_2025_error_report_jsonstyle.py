#!/home/juliz/venvs/stt/bin/python
"""Build a compact JSON-style catalog of all 2025 paper errors."""

from __future__ import annotations

import collections
import datetime as dt
import re
import subprocess
from pathlib import Path

from build_2025_error_report import (
    Finding,
    markdown_table,
    package_sort_key,
    parse_finding_section,
    parse_summary,
    visible_html_text,
)
from build_2025_error_report_concise import core_statement


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "2025_paper_error_report.md"


# Curated only after reading the detailed Verified sections in all 14 original
# HTML reports. Keys use the parser's package-local canonical candidate IDs.
REPRESENTATIVE_SELECTIONS: dict[str, list[tuple[str, str, str, str, str]]] = {
    "Presentation inconsistency": [
        ("jama.2025.4390", "C1", "Unit/scale label failure", "Tier A — strong final result", "The main subgroup figure labels an exposure-like quantity as an event rate, materially changing interpretation."),
        ("jama.2025.7710", "C1", "Primary analysis-unit ambiguity", "Tier A — strong final result", "Women, infants, and patients are used for the same primary records; the scientific analysis unit becomes unclear."),
        ("jama.2025.250116", "C4", "Duplicated outcome panel", "Tier A — strong final result after deduplication", "An entire interaction panel is copied to a different outcome. Use this as the canonical ImmunoSep duplication record and deduplicate the overlapping 24175 finding."),
        ("jama.2025.15185", "C8", "Effect-measure mislabeling", "Tier A — strong final result", "Calling an odds ratio an FMA mean difference changes the statistical meaning of the displayed effect."),
        ("jama.2025.16450", "C4", "Measure-definition error", "Tier B — valid final reporting result", "RR is expanded as risk difference although the article uses RR for relative risk and RD for risk difference; the error is clear but localized."),
        ("jama.2025.20765", "C6", "Missing denominator/missingness definition", "Tier B — valid interpretability result", "The omission prevents readers from identifying the adverse-event analysis population, although it does not by itself prove a numerical value wrong."),
        ("jama.2025.24175", "5", "Direction/sign presentation error", "Tier A — strong final result", "The mortality difference sign is the reverse of the displayed arm ordering and is directly recoverable from the printed risks."),
        ("jama.2025.24175", "6", "Event count versus patient incidence", "Tier A — strong final result", "The abstract attaches a patient percentage to an event count, conflating two different safety quantities."),
        ("jama.2025.9110", "C3", "Randomization-unit misstatement", "Tier A — strong final result", "Patient-level randomization wording conflicts with the stated ICU/cluster randomization and can mislead interpretation of the design."),
        ("jama.2025.11178", "C9", "Adjusted/unadjusted label conflict", "Tier A — strong final result", "The table title says adjusted while the surrounding description and footnote explicitly say unadjusted."),
    ],
    "Statistical reporting inconsistency": [
        ("jama.2025.11178", "C4", "Structurally invalid effect/CI displays", "Tier A — strong final result", "Multiple SMD cells fail point-estimate containment, endpoint ordering, or sign preservation under the table's own definition."),
        ("jama.2025.250116", "C5", "Interaction-effect misinterpretation", "Tier A — strong final result", "Within-stratum treatment effects are labeled and interpreted as interaction tests, altering the scientific claim."),
        ("jama.2025.250116", "C3", "Point estimate outside its CI", "Tier A — strong final result", "The OR cannot lie below its own lower confidence limit; this later HTML record verifies an item that was uncertain in package 24175."),
        ("jama.2025.15185", "C5", "Estimand population mismatch", "Tier A — strong final result", "The Full analysis set label conflicts with its death-exclusion definition and the displayed N."),
        ("jama.2025.15185", "C6", "Logical rule cannot produce reported N", "Tier A — strong final result", "The written conjunction and the reported analysis population are mathematically incompatible."),
        ("jama.2025.20765", "C8", "Incorrect ITT designation", "Tier A — strong final result", "A death-excluded post hoc population is labeled intention-to-treat, changing the meaning of the analysis set."),
        ("jama.2025.19563", "C4", "Conflicting inferential footnotes", "Tier B — valid final reporting result", "Age receives two unexplained P values and the all-other statement conflicts with the reported sex significance."),
        ("jama.2025.20765", "C4", "Narrative/table percentage mismatch", "Tier B — valid final numerical-reporting result", "Two adverse-event percentages cannot be reproduced from the displayed table counts, but the absolute differences are small."),
        ("jama.2025.9110", "C4", "Summary-statistic/model mismatch", "Tier A — strong final result", "A median/IQR Bayesian outcome is labeled mean (SD), misdescribing both the summaries and the model-based estimand."),
        ("jama.2025.11178", "C5", "Repeated effect estimate mismatch", "Tier B — valid final reporting result", "The text and table publish different SMDs for the same outcome, time point, and comparison; authoritative output is needed to choose the correction."),
    ],
    "Arithmetic inconsistency": [
        ("jama.2025.4390", "C5", "Category-total reconstruction failure", "Tier B — valid but low-impact final result", "The city counts sum to 44 rather than the province total of 43; this is clear but localized."),
        ("jama.2025.4390", "C7", "Percentage reconstruction failure", "Tier A — strong final result", "The printed percentage is nonreproducible and is propagated into two tables."),
        ("jama.2025.9110", "C1", "Subcategory counts below denominator", "Tier B — valid final result", "The sex counts leave two records unexplained and also fail the aggregate cross-check."),
        ("jama.2025.9110", "C2", "Wrong numerator used for percentage", "Tier A — strong final result", "The percentage beside participant count 151 numerically matches 158 events, indicating a quantity-level mix-up."),
        ("jama.2025.11178", "C3", "Gross count/percentage incompatibility", "Tier A — strong final result", "The supported count gives 45.4%, not 73.2%; the corrected display is directly recoverable."),
        ("jama.2025.15185", "C1", "Overall total one below every reconstruction", "Tier A — strong final result", "Arm totals and every classification block independently give 146 rather than the printed 145."),
        ("jama.2025.19563", "C1", "Simple denominator-rule failure", "Tier A — strong final result", "The displayed 10/59 is approximately 17%, not 19%, under the table's stated rule."),
        ("jama.2025.20765", "C2", "Cluster percentage denominator failure", "Tier A — strong final result", "The printed 5/40 percentage should be 12.5%, not 7.5%."),
        ("jama.2025.20765", "C3", "Repeated cause-percentage error", "Tier A — strong final result", "Two 1/27 cells are reported as 7.4% although each should be 3.7%."),
        ("jama.2025.250116", "C2", "Odds-ratio transcription/reconstruction failure", "Tier A — strong final result after deduplication", "The counts support an OR near 1.94 rather than 1.194. Deduplicate against the overlapping 24175 item 2."),
    ],
    "Cross-document inconsistency": [
        ("jama.2025.9110", "C5", "Summary-statistic definition changes across documents", "Tier A — strong final result", "The main article says mean (SD) while the supplement identifies median (IQR) for the same ventilation summaries."),
        ("jama.2025.9663", "C1", "Wrong supplementary-figure destination", "Tier C — supporting/editorial example", "The error is unambiguous but only redirects readers from eFigure 4 to eFigure 5; scientific impact is limited."),
        ("jama.2025.15185", "C2", "Arm counts conflict across documents", "Tier A — strong final result", "Only the main-article arm counts reproduce the supplement's overall totals, making the supplement internally and externally inconsistent."),
        ("jama.2025.15185", "C3", "Large timing discrepancy across documents", "Tier A — strong final result", "The same onset-to-randomization variable is reported as 3 days in the article and 7/8 days in the supplement."),
        ("jama.2025.15185", "C4", "One-participant numerator mismatch", "Tier B — valid but low-impact final result", "The same placebo response is 52/270 in the article and 51/270 in the supplement."),
        ("jama.2025.19563", "C6", "Unreconciled analysis-set sizes", "Tier A — strong final result", "The figure and co-cited table use different HbA1c analysis populations without explaining the inclusion rule."),
        ("jama.2025.19563", "C7", "Percent versus percentage-point definition", "Tier A — strong final result", "The supplement changes an absolute percentage-point threshold into percent notation, altering the clinical scale."),
        ("jama.2025.19843", "V2", "Composite definition/count impossibility", "Tier A — highest-priority mentor result", "MACE is reported smaller than dialysis even though dialysis is defined as a MACE component; the article and figure also disagree on the definition."),
        ("jama.2025.20765", "C1", "Omitted cluster changes analysis totals", "Tier A — strong final result", "One mHealth cluster and 40 participants disappear from one table relative to two corroborating displays."),
        ("jama.2025.20765", "C5", "Reversed adverse-event direction statement", "Tier A — strong final result", "The narrative direction for irritability and anxiety is opposite the tabled occurrence and therefore reverses the substantive safety statement."),
    ],
    "Participant-flow inconsistency": [
        ("jama.2025.11178", "C1", "Mutually exclusive flow categories do not partition N", "Tier A — highest-priority mentor result", "The follow-up-pattern categories overcount the analysis population by three and are localized to two treatment arms."),
    ],
}


# Compact numeric evidence for every representative record from the statistical
# category onward. These strings are transcribed or directly reconstructed from
# the detailed evidence in the original HTML reports; they are not inferred from
# the short mentor notes above.
REPRESENTATIVE_NUMBERS: dict[tuple[str, str], str] = {
    # Statistical reporting inconsistency
    ("jama.2025.11178", "C4"): "Table 3 examples: −0.25 (95% CI, −0.24 to 0.01), −0.36 (−0.35 to −0.12), and −0.27 (−0.26 to −0.12). Across the table: 8 point-estimate/CI containment failures, 18 reversed-endpoint cells, and 4 sign conflicts.",
    ("jama.2025.250116", "C5"): "Printed high-stratum ORs reconstruct as APACHE II ≥25: (12×32)/(26×8)=1.846≈1.85; CCI ≥5: (20×69)/(34×7)=5.798≈5.79; SOFA ≥10: (25×57)/(42×11)=3.084≈3.08. SOFA <10 gives OR≈2.019; the high/low ratio is ≈1.53, not 3.08.",
    ("jama.2025.250116", "C3"): "eFigure 9B prints OR 0.11 (95% CI, 0.36–3.42), P=.86, with deaths 32/40 (placebo) and 31/38 (precision immunotherapy). The cells give OR≈1.107 and diagnostic 95% CI≈0.358–3.421.",
    ("jama.2025.15185", "C5"): "Full analysis set: Estimand 1 N=582; Estimands 3–4 N=610; deaths=28 (17 placebo, 11 levodopa); 610−28=582. Printed effects: −0.98 (95% CI, −3.77 to 1.81) and win ratio 1.06 (0.86 to 1.26).",
    ("jama.2025.15185", "C6"): "Base N=582; Estimand 6 N=496 (86 medication failures); Estimand 7 N=450 (132 rehabilitation failures); Estimand 11 N=395 (187 excluded). Under the printed AND rule, at most 86 can be excluded, so retained N must be ≥496, not 395.",
    ("jama.2025.20765", "C8"): "Primary ITT denominators: 720 and 360; deaths: 25 and 27. eTable 9 uses 695 and 333, exactly 720−25 and 360−27; primary counts are 300/695=43.2% and 55/333=16.5%.",
    ("jama.2025.19563", "C4"): "eTable 11 groups: N=151 vs N=149. Age is assigned P=.010 in footnote 1 and P=.014 in footnote 2; sex has P=.041, contradicting footnote 2's statement that all other P values exceed .05.",
    ("jama.2025.20765", "C4"): "Main text: nausea 23.0% vs 22.3%; diarrhea 7.5% vs 7.5%. eTable 10: nausea 161/699=23.0% vs 71/334=21.3%; diarrhea 51/699=7.3% vs 25/334=7.5%.",
    ("jama.2025.9110", "C4"): "Bayesian row: 62.0 (0–77) vs 64.0 (0–77), median difference −1.50 (95% CrI, −3.86 to 0.90), but the row label says mean (SD). The adjacent row and eFigure 6 identify median (IQR)/median difference.",
    ("jama.2025.11178", "C5"): "Results text gives 3-month pain-severity SMDs −0.26 and −0.36; Table 3 gives −0.25 and −0.34 for the same comparisons.",
    # Arithmetic inconsistency
    ("jama.2025.4390", "C5"): "British Columbia header=43; 14 city counts are 12, 1, 1, 1, 1, 1, 1, 1, 4, 12, 1, 3, 3, 2, summing to 44. Province headers 43+326+22+29+16=436, matching eTable 1's 436 providers.",
    ("jama.2025.4390", "C7"): "Bedtime calcium-channel blocker: 479/1677=28.5629%→28.6%, but 28.2% is printed in main Table 1 and supplement eTable 3. Controls: 489/1680=29.1%; 968/3357=28.8%.",
    ("jama.2025.9110", "C1"): "Period 3 augmented protein: n=551; male 359 (65.2%) + female 190 (34.5%)=549, leaving 2. Across periods: male 1069 vs Table 1's 1070; female 610 vs 611; combined 1679 vs 1681.",
    ("jama.2025.9110", "C2"): "Augmented-protein denominator=1681; participants with ≥1 deviation=151 (printed 9.4%), events=158. 151/1681=8.9827%→9.0%; 158/1681=9.3992%→9.4%.",
    ("jama.2025.11178", "C3"): "Workbook eTable 3: All Observed N=1568; current depression 711 (73.2%); missing=2. With missing excluded, 711/(1568−2)=45.402%→45.4%; 162+243+711=1116, matching the overall count.",
    ("jama.2025.15185", "C1"): "Supplement overall=145, but arm totals 67+79=146; intensity 58+86+2=146; outcome 1+29+116=146; drug relation 2+66+23+2+39+14=146. Main article also reports 146.",
    ("jama.2025.19563", "C1"): "Human-led DPP N=59; cell 10 (19%). Direct calculation: 10/59=16.949%→17%; the adjacent row already prints 10 (17%), and all seven column counts sum to 59.",
    ("jama.2025.20765", "C2"): "Control site 2008: 5 deaths among 40 participants, printed as 5 (7.5%). 5/40=12.5%; 7.5% of 40 corresponds to 3 deaths. A neighboring 5-death site is printed as 12.5%.",
    ("jama.2025.20765", "C3"): "Usual-care total=27 deaths; Drug user=1 (7.4%) and Severe pneumonia=1 (7.4%). Each is 1/27=3.7037%→3.7%; 7.4% corresponds to 2/27. Printed usual-care percentages sum to 107.3%.",
    ("jama.2025.250116", "C2"): "Responders: 40/106 (37.7%) vs 29/122 (23.8%); printed unadjusted OR 1.194 (95% CI, 1.09–3.45), P=.030. From nonresponders 66 and 93: OR=(40×93)/(66×29)=1.9436; diagnostic CI≈1.10–3.45.",
    # Cross-document inconsistency
    ("jama.2025.9110", "C5"): "Main Table 2 labels mean (SD) but prints 84.0 (35.0–178.9) vs 78.0 (33.2–161.0); model effect is mean difference 6.8 (95% CI, −3.0 to 16.5). Supplement eTable 10 defines the group summaries as median (IQR).",
    ("jama.2025.9663", "C1"): "Main text: time-to-death HR 1.01 (95% CI, 0.96–1.05), cited as eFigure 4. eFigure 4 is oxygenation (N=2489); eFigure 5 is mortality and prints HR 1.01 (0.96–1.05), P=.82.",
    ("jama.2025.15185", "C2"): "Supplement Overall/placebo/levodopa: ischemic 519/259/263 and hemorrhagic 91/44/44. Main levodopa values are 260 and 47. Only 259+260=519 and 44+47=91; the supplement arm values miss each overall by 3.",
    ("jama.2025.15185", "C3"): "Main article: levodopa 3.0 days (IQR 2.0–5.0), placebo 3.0 (2.0–5.0). Supplement: levodopa 7 (5–11), placebo 8 (5–10): median differences of 4 and 5 days.",
    ("jama.2025.15185", "C4"): "Placebo response: main article 52/270=19.259%→19%; supplement 51/270=18.889%→18.89%. Difference: 1 participant, or 0.370 percentage points. Levodopa agrees at 51/276.",
    ("jama.2025.19563", "C6"): "Figure 3B axes extend to Human 149 and AI 151; visible nonzero bars are at least 117 and 121. eTable 14 HbA1c-change N=103 and N=106, respectively: at least 14 and 15 fewer; its other outcomes use N=149 and N=151.",
    ("jama.2025.19563", "C7"): "Same component counts in both displays: AI 35/130 and Human 35/130. Main article threshold: absolute HbA1c decrease ≥0.2 percentage points; supplement says 0.2%. Example: 0.2% relative to 6.0% is 0.012 percentage points, not 0.2.",
    ("jama.2025.19843", "V2"): "Placebo N=104; day-30 MACE 36 (34.6%) and dialysis 38 (36.5%). MACE is 2 participants and 1.9 percentage points below a stated component. eFigure 4 repeats 36 but omits dialysis from its MACE definition.",
    ("jama.2025.20765", "C1"): "Main Table 1: 18 mHealth clusters×40=720 participants, prior quit attempts 178 (24.7%). eTable 2: 17 clusters, 680 participants, Yes=168 and No=512. Shortfalls: 1 cluster, 40 participants, 10 Yes, 30 No.",
    ("jama.2025.20765", "C5"): "Any-grade occurrence: dry mouth 438/699=62.7% vs 186/334=55.7%; irritability 283/699=40.5% vs 145/334=43.4%; anxiety 233/699=33.3% vs 123/334=36.8%. Text says all three are more common in mHealth, but the latter two are lower.",
    # Participant-flow inconsistency
    ("jama.2025.11178", "C1"): "Overall N=2331; pattern rows 295+188+283+1568=2334 (+3); nonzero rows 188+283+1568=2039 vs 2036 (+3). painTRAINER: 777 vs N=776 (+1); Health Coach: 780 vs N=778 (+2); usual care: 777=777.",
}


def load_findings_from_html() -> tuple[list[Finding], list[Path]]:
    """Parse the original HTML reports directly; Markdown reports are not inputs."""
    html_paths = sorted(
        ROOT.glob("jama.2025.*/.ai_paper_validation/final_report.html"),
        key=lambda path: package_sort_key(path.parts[-3]),
    )
    findings: list[Finding] = []
    for html_path in html_paths:
        package = html_path.parts[-3]
        converted = subprocess.run(
            ["pandoc", str(html_path), "-f", "html", "-t", "gfm", "--wrap=none"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        lines = converted.splitlines()
        summary = parse_summary(lines)
        html_text = visible_html_text(html_path)
        findings.extend(
            parse_finding_section(
                lines,
                "Verified Scientific Findings",
                "Verified",
                package,
                summary,
                html_path,
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
                html_path,
                html_path,
                html_text,
            )
        )
    return findings, html_paths


def plain_link(match: re.Match[str]) -> str:
    label, target = match.group(1), match.group(2)
    basename = Path(target.split("#", 1)[0]).name
    if basename.lower().endswith(".xlsx"):
        source_name = "results workbook"
    elif basename.startswith("jama_"):
        source_name = "main article PDF"
    elif supplement := re.search(r"supp(\d+)", basename, re.I):
        source_name = f"supplement {supplement.group(1)} PDF"
    else:
        source_name = basename
    clean_label = re.sub(r"[*`]", "", label).strip()
    if clean_label.lower().startswith(("pdf p", "the same", "same file", "the linked")):
        return f"{source_name}, {clean_label}"
    if re.search(r"\.(?:pdf|xlsx)\b", clean_label, re.I):
        clean_label = re.sub(r"^.*?\.(?:pdf|xlsx)\b", source_name, clean_label, count=1, flags=re.I)
        return clean_label
    if clean_label.lower().endswith((".pdf", ".xlsx")):
        return source_name
    return clean_label


def clean_location_line(line: str, max_chars: int = 220) -> str:
    line = re.sub(r"\[([^]]+)\]\(([^)]+)\)", plain_link, line)
    line = re.sub(r"^\s*(?:[-*]|\d+[.)])\s*", "", line)
    line = re.sub(
        r"^\*\*(?:Exact source locations?|Source locations?|Location|Direct source evidence)[:.]?\*\*\s*",
        "",
        line,
        flags=re.I,
    )
    line = re.sub(r"[*`]", "", line)
    line = re.sub(r"\s+", " ", line).strip(" ;")
    if len(line) > max_chars:
        cut = max(
            line.rfind(";", 0, max_chars),
            line.rfind(".", 0, max_chars),
            line.rfind(",", 0, max_chars),
        )
        line = line[: cut if cut > max_chars // 2 else max_chars - 3].rstrip(" ,;") + "…"
    return line


def extract_locations(
    finding: Finding,
    max_items: int = 2,
    max_chars: int = 220,
) -> list[str]:
    body = finding.body
    boundary = re.search(r"(?im)^#{0,6}\s*(?:\*\*)?(?:Reasoning procedure|Direct comparison|Reported-versus)", body)
    evidence_head = body[: boundary.start()] if boundary else body
    locations: list[str] = []
    for line in evidence_head.splitlines():
        if line.lstrip().startswith("|"):
            continue
        if not re.search(r"\]\([^)]*\.(?:pdf|xlsx)(?:#page=\d+)?\)", line, re.I):
            continue
        cleaned = clean_location_line(line, max_chars=max_chars)
        if cleaned and cleaned not in locations:
            locations.append(cleaned)
        if len(locations) == max_items:
            break
    if not locations:
        locations.append(
            f"{finding.package}/.ai_paper_validation/final_report.html — {finding.candidate}, {finding.title}"
        )
    return locations


def shorten_problem(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+This is a directly reproducible [^.]+\.?$", "", text, flags=re.I)
    return text


def expected_statement(finding: Finding, problem: str) -> str:
    title = finding.title.lower()
    category = finding.category.lower()

    recoverable = re.search(r"directly recoverable display is\s+(`[^`]+`|[-+]?\d+(?:\.\d+)?%?)", problem, re.I)
    if not recoverable:
        recoverable = re.search(
            r"should (?:arithmetically )?(?:round to|be)\s+(`[^`]+`|[-+]?\d+(?:\.\d+)?%?)",
            problem,
            re.I,
        )
    if recoverable:
        return f"Use the recoverable value stated in the finding: {recoverable.group(1).strip()}."

    if "support 52/131" in problem:
        return "The narrative should report 52/131 (39.7%) so its numerator agrees with the table, subgroup totals, and percentage."
    if "positive 6.1%" in problem and "−6.1" in problem:
        return "Under the displayed precision-immunotherapy-minus-placebo ordering, the difference should be −6.1 percentage points."
    if "attaches 88.8% to 1069" in problem:
        return "State that 1069 events occurred in 245 of 276 patients (88.8%); attach 88.8% to patients, not to the event count."
    if "mislabels the displayed baseline bmi values as weight" in problem.lower():
        return "Label the values as BMI (kg/m²), not weight."
    if "incorrectly expands `rr` as “risk difference”" in problem.lower():
        return "Expand RR as relative risk; reserve RD for risk difference."
    if "fractional-scale fio2 values as percentages" in problem.lower():
        return "Either label the displayed values as fractions or multiply them by 100 before labeling them as percentages."
    if "absolute percentage points" in problem.lower() and "percent notation" in problem.lower():
        return "Use the main article's absolute percentage-point definition in the supplement; do not express it as a relative percent change."
    if "mean (sd)" in problem.lower() and "median" in problem.lower():
        return "Use median (IQR) for the three-number summaries and median-based analysis; do not label them mean (SD)."
    if "full analysis set" in problem.lower() and "excluding deaths" in problem.lower():
        return "Use a population label consistent with whether deaths are included; do not call an N that includes deaths the defined Full analysis set."
    if "intention to treat" in problem.lower() and "deaths" in problem.lower():
        return "Label the result as the post hoc death-excluded analysis, not intention-to-treat."
    if "10 of 59 as 19%" in problem.lower():
        return "Report 10/59 as 16.9% (approximately 17.0%), not 19%."
    if "overall `n=145` is one event below" in problem.lower():
        return "The overall adverse-event total should be 146 if it is intended to equal the displayed arm and classification totals."
    if "151 participants" in problem.lower() and "158" in problem and "1681" in problem:
        return "Report 151/1681 as 9.0%; 9.4% corresponds to 158/1681 events, not 151 participants."
    if "diagnostic percentage is 12.5%" in problem.lower():
        return "Report 5/40 as 12.5%, not 7.5%."
    if "conventional one-decimal calculation gives 3.7%" in problem.lower():
        return "Report each 1/27 cell as 3.7%, not 7.4%."
    if "diagnostic crude or of approximately 1.94" in problem.lower():
        return "The displayed counts support a crude OR near 1.94; verify the source model and replace the printed 1.194 if it is a transcription error."

    if any(word in title for word in ["duplicat", "repeats"]):
        return "Remove the duplicate, or replace it with the intended row/panel from the authoritative source output."
    if any(word in title for word in ["cross-reference", "citation", "points efigure"]):
        return "The citation should point to the supplement table or figure that actually contains the described result."
    if any(word in title for word in ["omits", "omitted", "absent", "missing", "undefined", "blank"]):
        return "Add the missing value, definition, or note; otherwise revise the title/marker so it does not promise information that is absent."
    if any(word in title for word in ["mislabel", "labels", "calls", "wording", "term", "mean versus median"]):
        return "Use the label, unit, summary statistic, or analysis description that matches the quantity actually displayed."
    if "confidence interval" in title or "outside its" in title or "smd" in title:
        return "Regenerate a matched point estimate and confidence interval; the point estimate must lie within its own interval and the endpoints must be ordered correctly."
    if "p value" in title or "p-value" in title:
        return "The estimate, confidence interval, and P value should come from the same stated test/model; confirm them against the original analysis output."
    if "arith" in category or any(word in title for word in ["percentage", "percentages", "total", "counts do not"]):
        return "Recalculate from the stated numerator and denominator, then replace the nonreproducible value while preserving the verified count/total."
    if "participant-flow" in category:
        return "Mutually exclusive flow categories must sum to the stated analysis total; correct the affected category cells."
    if "cross-document" in category:
        return "Use one authoritative value or definition consistently in the main article, supplement, table, figure, and narrative."
    if "statistical" in category:
        return "The reported value and label should match the stated estimand, analysis population, effect measure, and model output."
    if any(word in title for word in ["differ", "conflict", "inconsistent", "do not reconcile", "reversed"]):
        return "The conflicting locations should report the same value, direction, definition, or denominator; use authoritative source output when the correct version is not recoverable."
    return "Correct the affected display so its value and description agree with the authoritative analysis output."


def quote_value(text: str) -> str:
    return text.replace('"', "“").replace("\n", " ")


def emit_record(
    out: list[str],
    record_id: str,
    finding: Finding,
    status: str,
) -> None:
    locations = extract_locations(finding)
    problem = shorten_problem(core_statement(finding))
    expected = (
        expected_statement(finding, problem)
        if status == "verified"
        else "Do not amend the publication yet; first obtain the missing definition, unrounded result, or model/source output identified by the validation report."
    )
    out.extend(
        [
            f"### {record_id} — {finding.package} / {finding.candidate}",
            "",
            "> {  ",
            f'> **"severity"**: "{quote_value(finding.severity_raw)}",  ',
        ]
    )
    if status != "verified":
        out.append(f'> **"status"**: "{status}",  ')
    for index, location in enumerate(locations, 1):
        out.append(f'> **"location_{index}"**: "{quote_value(location)}",  ')
    out.extend(
        [
            f'> **"problem"**: "{quote_value(problem)}",  ',
            f'> **"expected"**: "{quote_value(expected)}"  ',
            "> }",
            "",
        ]
    )


def emit_representative_review(out: list[str], verified: list[Finding]) -> int:
    lookup = {(finding.package, finding.key): finding for finding in verified}
    selected_count = 0
    tier_counts = collections.Counter(
        tier.split(" —", 1)[0]
        for selections in REPRESENTATIVE_SELECTIONS.values()
        for _, _, _, tier, _ in selections
    )
    out.extend(
        [
            "# Representative issues for mentor review",
            "",
            "This section was selected after reading the detailed Verified sections in all 14 original `final_report.html` files. It prioritizes direct reproducibility, interpretive consequence, clear source location, and independence from duplicate package records. Each original error category contributes up to 10 representative issues; categories with fewer than 10 verified records contribute all available records.",
            "",
            markdown_table(
                ["Assessment", "Meaning for final output"],
                [
                    ["Tier A", "Strong final result: directly reproducible and scientifically or interpretively meaningful."],
                    ["Tier B", "Valid final result: useful, but mainly a localized reporting or editorial problem."],
                    ["Tier C", "Supporting example: clear but low-impact, or best retained only after deduplication/context review."],
                ],
            ),
            "",
            markdown_table(
                ["Selected assessment", "Count"],
                [[tier, tier_counts[tier]] for tier in ["Tier A", "Tier B", "Tier C"]],
            ),
            "",
            "The `mentor_note` field explains why the item is—or is not—worth emphasizing in the final communication. Overlapping ImmunoSep findings are explicitly marked for deduplication.",
            "",
        ]
    )
    for category, selections in REPRESENTATIVE_SELECTIONS.items():
        out.extend([f"## {category}: representative set ({len(selections)})", ""])
        for rank, (package, key, pattern, tier, mentor_note) in enumerate(selections, 1):
            finding = lookup.get((package, key))
            if finding is None:
                raise RuntimeError(f"HTML-based representative selection not found: {package} {key}")
            if finding.category != category:
                raise RuntimeError(
                    f"Representative selection category mismatch: {package} {key}: "
                    f"{finding.category!r} != {category!r}"
                )
            selected_count += 1
            out.extend(
                [
                    f"### typical_{selected_count:03d} — {package} / {finding.candidate}",
                    "",
                    "> {  ",
                    f'> **"rank_in_category"**: "{rank}",  ',
                    f'> **"source_title"**: "{quote_value(finding.title)}",  ',
                    f'> **"representative_pattern"**: "{quote_value(pattern)}",  ',
                ]
            )
            if category != "Presentation inconsistency":
                numbers = REPRESENTATIVE_NUMBERS.get((package, key))
                if numbers is None:
                    raise RuntimeError(
                        f"Missing representative numeric evidence: {package} {key}"
                    )
                for index, location in enumerate(
                    extract_locations(finding, max_items=4, max_chars=520), 1
                ):
                    out.append(f'> **"location_{index}"**: "{quote_value(location)}",  ')
                out.append(f'> **"reported_numbers"**: "{quote_value(numbers)}",  ')
            out.extend(
                [
                    f'> **"problem"**: "{quote_value(shorten_problem(core_statement(finding)))}",  ',
                    f'> **"final_output_value"**: "{quote_value(tier)}",  ',
                    f'> **"mentor_note"**: "{quote_value(mentor_note)}"  ',
                    "> }",
                    "",
                ]
            )
    return selected_count


def main() -> None:
    findings, html_paths = load_findings_from_html()
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
    vc = collections.Counter(finding.category for finding in verified)
    uc = collections.Counter(finding.category for finding in uncertain)

    out: list[str] = [
        "---",
        'title: "2025 Paper Errors — JSON-Style Concise Catalog"',
        'subtitle: "Location, problem, and expected state for every classified finding"',
        'author: "Generated from the local AI paper-validation archive"',
        f'date: "{dt.date(2026, 8, 14).isoformat()}"',
        "lang: en-US",
        "toc: true",
        "toc-depth: 1",
        "numbersections: true",
        "---",
        "",
        "# Summary",
        "",
        f"This catalog is generated directly from all **{len(html_paths)} original `final_report.html` files**. It converts all **{len(verified)} verified error records** into a fixed JSON-style structure: actual location(s), the observed problem, and the expected corrected state. The **{len(uncertain)} uncertain candidates** are listed separately and are not treated as established errors.",
        "",
        markdown_table(
            ["Error type", "Verified", "Uncertain"],
            [[category, vc.get(category, 0), uc.get(category, 0)] for category in categories if vc.get(category, 0) or uc.get(category, 0)],
        ),
        "",
        "When the reports do not identify which conflicting number is authoritative, the `expected` field says that the locations must be reconciled against source output instead of inventing a replacement value. Counts remain report-level instances because the two ImmunoSep packages contain overlapping findings.",
        "",
    ]

    representative_count = emit_representative_review(out, verified)
    out.extend(["# Verified error records", ""])

    counter = 0
    for category in categories:
        items = sorted(
            [finding for finding in verified if finding.category == category],
            key=lambda finding: (finding.package, finding.key),
        )
        if not items:
            continue
        out.extend([f"## {category} ({len(items)})", ""])
        for finding in items:
            counter += 1
            emit_record(out, f"error_{counter:03d}", finding, "verified")

    out.extend(
        [
            "# Uncertain records",
            "",
            "These records identify a plausible problem, but the supplied package does not establish which element is wrong or what corrected value should replace it.",
            "",
        ]
    )
    for index, finding in enumerate(sorted(uncertain, key=lambda item: (item.category, item.package, item.key)), 1):
        emit_record(out, f"concern_{index:03d}", finding, "uncertain")

    out.extend(["# Source report index", ""])
    for html_path in html_paths:
        package = html_path.parts[-3]
        out.append(
            f"- **{package}:** [final_report.html]({package}/.ai_paper_validation/final_report.html)"
        )

    OUTPUT.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    print(f"Verified JSON-style records: {counter}")
    print(f"Uncertain JSON-style records: {len(uncertain)}")
    print(f"Representative mentor-review records: {representative_count}")


if __name__ == "__main__":
    main()
