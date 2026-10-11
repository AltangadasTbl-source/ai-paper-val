# 2024 R_A primary review (v.2.3.1): AI-simulated reviewer summary

Reviewer ID: `AI-sim-ClaudeOpus5.5-2024-R_A`. This is an AI-simulated reviewer (Claude Opus 5.5 agent), not a human adjudicator.
Scope: 10 papers, 91 candidates. Template: `2024/release/human_adjudication_v_2_3_1_2024_R_A.xlsx` (read only, not modified).

Outputs (this folder):
- `judgments.json`: all 91 judgments, each with a workbook note (R), the evidence inspected, and a rationale.
- `human_adjudication_v_2_3_1_2024_R_A_completed.xlsx`: built with `fill_review.py`.
- `REVIEW_SUMMARY.md`: this file.

## How sources were read

The Read tool could not render PDF pages because `pdftoppm` is not installed. I used the system Python's PyMuPDF (`fitz`) in two ways:
- I extracted page-tagged text for searching and quoting.
- I rendered individual pages to PNG, which I then viewed with the Read tool.

Every table, figure and flow diagram that a judgment depends on was viewed as a rendered image. Where text extraction was enough (narrative sentences and protocol wording), the `evidence` field says "(text)".

For jama.2024.0572 Figure 2, I extracted the bar-segment rectangles and the legend swatch colors from the PDF vector drawing. I used them to reconstruct the mRS counts by arm and stratum.

All arithmetic was done in Python (scipy for P values, Wald intervals and Beta quantiles). Each computation is described in the relevant rationale.

No source was unreadable. Some protocol formula pages in jama.2024.4183 (protocol p.29) extract as garbled math glyphs, but the tables that candidates C010–C012 depend on (protocol p.32–34) were rendered and read without difficulty.

## Counts

| Field | Counts |
|---|---|
| D (disposition) | retain 84, exclude 7, discuss 0 |
| E (domain) | statistical_results 59, report_internal_inconsistency 19, protocol_report 7, plan_material 6 |
| H (retained statistical_results, n=56) | confirmed_issue 52, probable_issue 4 |
| I | minor_presentation 47, substantive 9 |
| J (optional) | unlikely 35, possible 14, direct 7 |
| K (retained RII/plan_material, n=24) | minor_presentation 21, substantive_inconsistency 3 |
| L (retained protocol_report, n=4) | minor_presentation 2, substantive_difference 2 |

Across all domains, 14 retained candidates are rated substantive (9 under I, 3 under K, 2 under L):

- **I = substantive (9):**
  - 0318 C001: Figure 1 arm branches sum to 315, not 305.
  - 0572 C001: Figure 2 mRS distribution conflicts with eTable 2.
  - 19585 C002: the main text gives 6.4% of statements rejected; eTable 3 gives 10.5%.
  - 4183 C005 and C006: the abstract's primary risk-difference CrI is printed as 6%–11%; the correct interval is 2%–11% (2%–10% in the eTable).
  - 4183 C007: the direction of the varenicline switch-vs-continuation result is reversed in the narrative, and the sign is reversed in the eTable.
  - 6063 C009, C010 and C011: rows in eTable 4 were copied from other rows, so the true results are unrecoverable.
- **K = substantive_inconsistency (3):**
  - 11057 C001: pre-quit messaging is 6 weeks in the main text and 1 week in the results supplement and protocol.
  - 12829 C010: protocol V2.0 gives an eligibility window of 14–90 days in one place and 21–90 days in another.
  - 23898 C003: readmission window is 30 days in Methods and 90 days in Table 3.
- **L = substantive_difference (2):**
  - 2302 C003: the reported Bayesian prior is narrower than the one in the SAP.
  - 23898 C002: opioid-use window is 24 hours in the report and 72 hours in the protocol and SAP.

## E changed from the AI suggestion: 20 of 91

**Seventeen changes followed one consistent rule.** If my judgment rests on a numerical recomputation, a P-value/CI check, or the definition of a reported statistic (effect measure, summary statistic, sign), I used statistical_results. The Codebook says to use statistical_results "when specifically judging a statistical or numerical reporting issue". These were:

- 0318 C003
- 0572 C001 and C002
- 11057 C002
- 12829 C016
- 19585 C002 and C003
- 25786 C003, C004, C005 and C006
- 4183 C007
- 6063 C012, C013 and C016

Conversely, 4183 C004 (a missing "not" in a narrative sentence) went from statistical_results to report_internal_inconsistency.

**Four protocol_report suggestions changed to report_internal_inconsistency.** In each case the decisive conflict lies within the report materials (main article versus results supplement, or within the main article), and the report either agrees with the plan or the plan comparison cannot explain the conflict:

- 11057 C001
- 12829 C009
- 23898 C003
- 23898 C007

## Disposition differs from the AI suggestion: 6

The AI suggested retain for 90 candidates and exclude for 1 (19585 C001, which I also excluded). I excluded these 6 additional candidates:

- **12829 C003:** the Table S4 denominator of 241 is explicitly footnoted, and every row reproduces with it.
- **12829 C008:** the out-of-range stenosis categories in Table 1 match, one to one, the post-randomization adjudication exclusions in Figure 1. This is a correct ITT baseline table.
- **12829 C013:** the repeated visit numbers come from a punctuation slip in a protocol sentence; the sentence agrees with the schedule.
- **2302 C005:** every document uses "enrollment" and "randomization" interchangeably as time zero, and randomization occurred at consent.
- **23898 C001:** the protocol and SAP themselves use "after surgery" as shorthand for "after start of operation".
- **23898 C004:** the protocol's ERAS bands are explicitly "e.g.", the SAP set no cut points, and the report discloses that its cut points were defined post hoc.

## Discuss list

None. After checking, every candidate could be settled from the documents.

The closest call is jama.2024.6063 C001: the placebo arm shows 21 discontinuations in Figure 1 but 23 withdrawals or losses in the Results. "Completed treatment" and "completed trial" could differ, so I recorded it as retain with H=probable_issue rather than discuss.

## Other places I disagreed with the AI rationale

- **0318 C003:** the AI treated this as a pure cross-document P-value mismatch. Recomputing from the CI shows that P=.002 is the inconsistent value: the largest P compatible with the rounded CI is about 0.0009.
- **0572 C001:** the AI's reconstruction was conditional on rounding. The vector-geometry reconstruction gives near-integer counts (within 0.03), so the conflict is confirmed. The as-treated Table 2 agrees with eTable 2, which makes Figure 2 the outlier.
- **2302 C005:** the AI says the main article uses "randomization". It also says "10 months after enrollment" (p.4).
- **12829 C010:** the AI cited p.7 for the 21–90 synopsis; I found it on PDF p.9. A body exclusion criterion ("within 21 days") and the protocol change log also bear on this.
- **6063 C003–C008:** the AI treated these as six independent percentage errors. They share one cause: both arms print the pooled percentage column (4, 26, 155, 25 and 6 of 216).
- **4183 C010:** both phase-1 response Beta distributions are inconsistent with their labels, not only the varenicline one.
- **Substantiveness:** I rated most rounding, label and cross-reference findings minor_presentation. I reserved substantive for errors that change a reported estimate, interval or direction, or that make the correct value unrecoverable.

## Incidental observations (not candidates; not scored)

- **12829:** Results text gives 343 (69.1%) male, but 343/501 = 68.5%.
- **25786 eTable 2:** the restrictive-arm firearm row uses 724 as its denominator; all other rows use 742.
- **4183:**
  - Protocol Table 3 Aim 1 prints 0.240, but 0.749 − 0.504 = 0.245.
  - The main text compares EOT+30 varenicline continuation as "0%; n = 42", while eFigure 2 uses 0/77.
  - Nonattenders were imputed into the continuation arms (40/90 CNRT and 35/77 varenicline), so the continuation comparators are partly nonrandomized. This is a design-interpretation concern rather than a reporting error.
- **6063 C012:** the raw difference of the arm changes is +0.3, while the adjusted estimate is −0.27. The orientation of the contrast is not documented.

## Independence and confinement

- I did not open `2024/jama.2024.2302/Detailed_Errors_On_C1_C3_C5.docx`, any `.ai_paper_validation/`, `workflow_*`, `meta_report/` or `archived/` folder, `human_adjudication/previous/`, git history, or anything under `ai_reviewer_runs/2024/R_B/` or other year/role folders. The `evidencePaths` links in the Links sheet point into `.ai_paper_validation/`; I did not follow them.
- **Shared scratchpad incident.** Before I knew the session scratchpad was shared, I wrote these files at the scratchpad top level:
  - Sheet dumps: `Papers.txt`, `Candidates.txt`, `Evidence.txt`, `Links.txt`, `Relations.txt`, `Manifest.txt`, `Protocol_plan_table.txt` and `C_jama.2024.0318.txt`.
  - `extract.py`.

  Consequences:
  - Another agent overwrote my top-level `extract.py`. When I re-ran it, Python executed that other agent's version, which failed at its first line (`import pymupdf, glob, os, sys`). I saw only that traceback line and did not read the file further.
  - I may have overwritten top-level files of the same names written by another agent; I cannot tell.
  - I listed `*.txt` at the scratchpad top level once (`wc -c`). The listing showed only the eight dump files named above.
  - I did not read any other scratchpad file or folder that I did not create.

  All my later work is in the private folder `scratchpad/2024_R_A_private/` (first created as `R_A_private_work/`, then renamed). This folder holds the text extracts, renders, per-paper row files and helper scripts.

## Workbook and script observations

- **Evidence sheet quality varies.**
  - jama.2024.25786: each EV0–EV3 field repeats the whole concatenated evidence text, and the text contains leftover "Human adjudication fields: Validity __ Importance __ Action __ Initials __" template strings.
  - jama.2024.4183: EV1–EV3 are generic placeholders ("Printed evidence versus the matched source occurrence or stated consistency rule").
- **19585 C001:** the AI's own baseline disposition is exclude ("NOT REPRODUCED"), yet the candidate remains in the review set. This is harmless, but reviewers should notice it.
- **`fill_review.py`:**
  - It sets F=primary_done for every row.
  - It does not check that R stays within any length limit. I kept every R at 400 characters or fewer.
  - No bugs found.
- **`recalc_check.py`:** it ran cleanly. Checks reports "Unfinished" as `0.0` (float) rather than `0`, which is cosmetic.

## recalc_check output

```
G: {'PRIMARY READY': 91}
Checks 1 Check -> Result
Checks 2 Candidates -> 91
Checks 3 Primary ready -> 91
Checks 4 Unfinished -> 0.0
Checks 5 Discuss / unresolved -> 0
Checks 6 Workflow status -> PRIMARY READY
Checks 7 Ready with discuss -> 0
Checks 8 Meaning -> PRIMARY READY means independent data entry is complete; discuss remains unresolved and prevents that paper's outcome counts.
Checks 9 Next action -> Inspect G on C_ sheets or filter Decisions readiness. Save the completed file and deliver it; preserve normal Excel backups.
```
