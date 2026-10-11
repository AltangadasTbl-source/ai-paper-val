# 2018 R_B independent primary review (v.2.3.1): summary

Reviewer ID: `AI-sim-ClaudeOpus5.5-2018-R_B` (an AI-simulated reviewer, not a human adjudicator).
Scope: 10 papers and 119 candidates from `2018/release/human_adjudication_v_2_3_1_2018_R_B.xlsx`.

## Outputs

- `judgments.json`: one row per candidate, with D, E, H–L, the workbook note (R), the evidence pages inspected, and the rationale with the recomputation.
- `human_adjudication_v_2_3_1_2018_R_B_completed.xlsx`: built with `fill_review.py` from the release template, which was not modified.

## How sources were read

The Read tool could not render PDF pages in this environment because `pdftoppm` is not installed. I used PyMuPDF (`fitz`, in the user site-packages of the system `python3`) for two things:

- to extract per-page text for searching;
- to render cited pages to PNG, which I then viewed with Read.

Every table and figure cited in a judgment was viewed as a rendered page image or checked against the extracted page text. All recomputations were done in Python (scipy from the 2019 venv) and are recorded in the rationales. **All 37 source PDFs were readable; no source was unreadable.**

## Counts

| Field | Counts |
|---|---|
| D | retain 118, exclude 1, discuss 0 |
| E | statistical_results 76, report_internal_inconsistency 21, protocol_report 11, plan_material 11 |
| H (retained statistical_results, n=75) | confirmed_issue 74, probable_issue 1 |
| I | minor_presentation 52, substantive 23 |
| J (optional) | unlikely 44, direct 24, possible 7 |
| K (retained report_internal/plan_material, n=32) | minor_presentation 30, substantive_inconsistency 2 |
| L (retained protocol_report, n=11) | substantive_difference 6, minor_presentation 4, indeterminate 1 |

### Changes to the AI domain (E): 8

Each of these moved from report_internal_inconsistency to statistical_results. Following the Codebook, statistical_results applies when the judgment concerns a numerical estimate, interval or count/percentage display.

- 2017.21906 C002 (discharge β-blocker RD/OR differ, Table 2 vs text)
- 17075 C002 (abstract RD sign)
- 17075 C005 and C006 (eTable 10 count/percentage reversed)
- 18020 C002 (INQoL values impossible on the stated 0–100 scale)
- 14282 C017 (respiratory-rate CI endpoint)
- 14282 C023 and C024 (forest-plot HRs inverted relative to Table 2)

### Disposition differences from the AI suggestion: 2

- **0156 C008: retained, not discuss.** The protocol's composite "technique failure" (28-day death, regurgitation or procedural failure) is not reported. The article reports procedural failure only, under "rate of BMV or ETI failure." That plan-report difference is established from the documents. The AI's 27 > 21 bound is invalid because 54/1022 are ETI *survivors* (Table 2), not deaths.
- **6496 C002: excluded.** The ETT+stylet denominators are 366 for the composite and 364 for hypoxemia. A first-attempt failure is a composite failure even without oximetry, and protocol p.21 excludes missing data only from "the relevant outcome." The 2-patient difference therefore has a satisfactory explanation.

## Discuss list

None. Every candidate could be resolved from the supplied documents. Where an aspect stayed uncertain, I used an indeterminate code inside a retained row instead of deferring:

- 0948 C001: whether the ≥60 vs >60 mL/kg rule mattered (L = indeterminate).
- 18020 C004: the placebo AE denominator is not printed (H = probable_issue).

## Where I disagreed with or went beyond the AI rationale

- **2017.21906 C005:** anticoagulant vs heparin in an eTable 6 footnote. Judged minor, not substantive. The wording matches the SAP and looks like a carried-over plan footnote.
- **0948 C001:** L = indeterminate rather than an implied substantive difference. The report materials disagree with each other (article ≥60, Supplement 3 >60), and the rule actually applied is unknown.
- **9128 C011:** "BMI percentile" appears only in the original protocol text. The original SAP (April 2012), the revised protocol and the final SAP all specify raw BMI, so this is a minor label issue, not a change of outcome scale.
- **14282 C018:** the AI called this "communication-only." As printed, 153 vs 31 patients per arm of 388 (P ≈ 7e-25) contradicts "no statistical difference." The sentence is internally contradictory, so it is a confirmed, substantive issue.
- **14280 C012–C021 (Table 2 RRs):** this goes beyond the AI's per-row point-estimate framing.
  - The printed P values reproduce exactly from uncorrected χ² tests on the printed counts.
  - The printed CIs are about half the width any valid estimator allows on those counts.
  - So the whole RR column, estimates and CIs, is unreliable. Every row was rated substantive.
- **18020 C010 and C011:** the CI midpoints show likely endpoint sign errors (upper −0.51 and lower +1.96). With those corrections the intervals become consistent with the printed estimates and P values.
- **0156 C004:** the PP survival CI (−10 to 9.7) is wrong, but the same Wald method reproduces every ITT CI in Table 2 exactly.
- **2017.21906 C001 and C002, 0156 C003 and C005:** the erroneous occurrence was identified by CI symmetry or by recomputing from counts.

## Incidental observations (not candidates; not adjudicated)

- **0156:** PP survival-to-admission CI. The counts give a Wald CI of −8.16 to 0.08; the paper prints −7.6 to 0.6.
- **8802:** in-hospital death HR 0.96 (0.90–1.02) is implausibly narrow for 34 events.
- **18020:** Table 2 note d says all significant findings favored mexiletine. The SCN4A fifth transient-paresis result (P = .02) favors placebo.
- **18020:** eTable 4 mexiletine "Any 27" equals the sum of the reaction counts even though 2 patients had more than 1 reaction.
- **14282:** the plans specify a relative risk for the primary outcome; the article reports a Cox HR.
- **6496:** the clustered P (.95) is much larger than the unclustered P (.24) despite ICC < 0.001.

## Workbook and script notes

- `fill_review.py --check` passed with 0 errors and 0 missing. The build succeeded, and the script sets F = primary_done for every judged row.
- The H column header in the template and Codebook is misspelled "Statistcal_or_numerical issue."
- Codebook section numbering skips from 4 to 6.
- Checks row 6 shows "Unfinished rows -> 0.0" (a float) under the `formulas` recalculation.
- No script bugs found.

## recalc_check output

```
G: {'PRIMARY READY': 119}
Checks 1 Check -> Result
Checks 2 Reviewer role -> R_B
Checks 3 Candidates -> 119
Checks 4 Primary ready rows -> 119
Checks 5 Discuss / unresolved rows -> 0
Checks 6 Unfinished rows -> 0.0
Checks 7 Workflow status -> PRIMARY READY
Checks 8 Meaning -> PRIMARY READY means independent entry is complete. Discuss remains unresolved and is not counted as absence of error.
Checks 9 Next action -> Inspect G on paper sheets and readiness in Decisions. Save and deliver this file after review.
```

## Independence and scratchpad disclosure

I did not read anything under `ai_reviewer_runs/2018/R_A/` or any other output folder. I did not open `.ai_paper_validation/`, `workflow_*`, `meta_report/`, `archived/` or `human_adjudication/previous/`, and I did not use git history. The only AI material used was what the workbook embeds.

**Before I knew the session scratchpad was shared**, I wrote these files at its top level:

- `render.py`, `extract.py`, `dump.py`
- `papers/` (10 candidate dumps from my R_B template)
- `txt/` (37 PDF text extracts)
- `img/` (3 page PNGs)

The first write of `render.py` may have overwritten a file of the same name if one already existed. I cannot tell whether one did.

**I saw one line of another agent's script.** When I next ran the top-level `render.py`, another agent's script had replaced it. Running it failed, and the traceback displayed one line of that script: `pid, pref, pages = sys.argv[1], sys.argv[2], sys.argv[3]`.

- I did not otherwise open, list or read any scratchpad file I had not created.
- I never listed the scratchpad top level.
- I did not access `y2018_RA_agent`.
- I did run one `diff` of top-level `papers/jama.2017.21906.txt` (created by me) against my private copy; the two were identical.

I then moved all my work into a private folder, renamed on the coordinator's instruction to `scratchpad/y2018_RB_agent/`. I left the top-level files in place because other agents may since have overwritten them, and deleting them could destroy their work. No other agent's content informed any judgment.
