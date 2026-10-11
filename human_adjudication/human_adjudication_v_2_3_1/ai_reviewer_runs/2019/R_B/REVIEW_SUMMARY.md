# v.2.3.1 primary review, 2019, role R_B: AI-simulated reviewer summary

Reviewer ID: `AI-sim-ClaudeOpus5.5-2019-R_B` (AI-simulated reviewer, Claude Opus 5.5 agent; not a human adjudicator).
Scope: 9 papers, 62 candidates. Independent of R_A; no R_A output, pipeline internals, earlier adjudication versions or `records/` were read.

## Outputs

- `judgments.json`: 62 rows with D, E, H-L, the workbook note (R), the pages inspected and the full rationale.
- `human_adjudication_v_2_3_1_2019_R_B_completed.xlsx`: built by `fill_review.py` from the unmodified release template. The template SHA-256 still matches `release/output_hashes.json`.

## Counts

| Disposition (D) | n |
|---|---|
| retain | 59 |
| exclude | 3 |
| discuss | 0 |

| Domain (E) | all | retained |
|---|---|---|
| report_internal_inconsistency | 26 | 26 |
| statistical_results | 22 | 21 |
| plan_material | 7 | 7 |
| protocol_report | 7 | 5 |

**E changed from the AI suggestion: 2**

- `2019::jama.2019.2210::C002`: statistical_results -> report_internal_inconsistency. The candidate is a caption-versus-display conflict, not a numerical result.
- `2019::jama.2019.7505::C001`: report_internal_inconsistency -> statistical_results. Recomputation shows the abstract CI endpoint is the numerical error.

**Outcome codes (retained rows only)**

- H (21 statistical_results): confirmed_issue 20, probable_issue 1
- I: substantive 10, minor_presentation 11
- J (optional): direct 7, possible 8, unlikely 6
- K (33 report_internal/plan_material): minor_presentation 32, substantive_inconsistency 1, non_inconsistency 0, indeterminate 0
- L (5 protocol_report, optional): substantive_difference 3, minor_presentation 1, blank 1 (`17380::C007`; see below)

Retained statistical issues graded confirmed and substantive (10):

- 14231 C002-C006 (Table 2 ARDs vs incidences)
- 12618 C005 (missed-dose SD/P)
- 14901 C003, C004 (complement percentages)
- 7505 C001 (abstract CI sign)
- 7505 C002 (DIC RR/CI)

Substantive report-internal inconsistency (1): 2210 C009, where the Table 2 HR-direction footnote is reversed.

## Discuss list

None. Every candidate could be settled from the supplied documents after recomputation. The closest judgment calls are below. In each, the facts are clear and only the classification is debatable.

- `17380::C007` (10 vs 20 imputations): retained as a descriptive protocol-report difference with L left blank. None of the L codes fits a real difference that is immaterial and not a wording issue. Exclusion would also be defensible.
- `14630::C006/C007` (Table 1 vs eTable 9 baseline weight/BMI): eTable 9 is labelled MI, and whether baseline risk factors were imputed is unstated. Retained as minor because the cause cannot be determined and the magnitude is immaterial either way.

## Where I disagreed with or went beyond the AI rationale

- **Excluded, AI said retain (3):**
  - `12618::C003`: the article's block sizes 4/6 match both SAP versions (Jan 2013 and Mar 2017). Only the 2012 MOP draft says 4/6/8, and the final protocol is silent.
  - `14231::C007`: eTable 10 is explicitly an analysis-specific denominator table. A 2-patient difference changes no printed percentage.
  - `2210::C008`: the article explicitly equates randomization and the start of supplementation (same visit).
- `12618::C005`: the AI framed P = .87 as wrong. Recomputation suggests the reverse.
  - Ten of 194 patients missed at least 20% of doses (sensitivity n = 184), which forces SD >= 3.5. The printed "SDs" of 1.0 and 0.5 are therefore impossible.
  - Treated as SEs, they give P of about .86-.87.
  - The likely error is the SD label, not the P value. Confirmed either way.
- `12618::C002`: graded probable, not confirmed. The stated eligibility rule gives 74 - 5 = 69, not 68, but one further unstated exclusion could explain 68.
- `14231::C002-C006`: the five component-outcome ARDs all exceed the incidence difference by 0.3-0.9 pp and sit near the bootstrap-CI midpoints, while the composite and mortality rows reproduce exactly. This points to a population or estimator mismatch, not five typos.
- `2210::C002`: the misplaced caption sentence belongs to Figure 2C (the competing-risk panel, which has no at-risk table).
- `4755::C001-C003`: I could not confirm the "detached fragment" text objects the AI evidence mentions. PyMuPDF finds no hidden 18.2/25.7/21.6 on the page. The values are absent, apparently clipped. They are derivable from the arm PPVs, so graded minor.
- `7505::C002`: the printed RR 2.00 equals p_high / mean(p_high, p_low). See the broader concern below.
- `14901::C003/C004`: graded substantive although these are baseline descriptors, because the printed percentages invert majority and minority (31% shown as 69%).

## Observations outside the candidate set (not judged; flag for the coordinator)

- **jama.2019.7505 Table 3 RR column.** Most printed risk ratios do not equal the crude ratio of the displayed risks. Examples:
  - Primary PPC: crude 0.904 (Wald 0.77-1.07) vs printed 0.93 (0.83-1.04)
  - Hypoxemia: 0.365 vs 0.51
  - Hypotension: 1.84 vs 1.43

  For sparse rows the printed RR equals p_high / mean(p_high, p_low): aspiration 1.33, ARDS 1.50, pneumothorax 0.50, in-hospital mortality 1.41, DIC 2.00. This may be a nonstandard parameterization affecting the primary estimate, and it merits a dedicated candidate.
- **jama.2019.10517 Table 5.** The cholesterol-row CI (-8 to 17.2) is not reproduced by Wald (-6.9 to 15.6) or Newcombe (-7.4 to 16.1), and only the other rows are footnoted as exact CIs.
- **jama.2019.12618 eTable 8.** Headers N = 62/56 differ from the main text's 60/54 patients continuing to 12 months.
- **jama.2019.2210 Table 1.** ApaI placebo GT 61/150 = 40.7% is printed 40.

## Sources and tooling

- **PDF rendering.** The Read tool could not render PDF pages (no pdftoppm), and no PDF library is installed in `2019/.venv`.
  - All PDFs were read with PyMuPDF (user site-packages, system `python3`): text extraction plus page rendering to PNG for tables and figures.
  - All computation used `2019/.venv/bin/python`.
- **Image-only pages** were rendered and read visually:
  - `joi190092supp2_prod.pdf` p.80 (FAST MOP v4.5 §2.5.1)
  - eFigures in `joi190122supp2_prod.pdf` p.18-19
  - eTable 5 in `joi190039supp3_prod.pdf` p.7
  - Main-paper Tables/Figures for 10517 (p.8), 17380 (p.7-8), 2210 (p.5-7)
- **Unreadable sources:** none. Pages not needed for any candidate were not examined.
- **`2019/sources/`** holds only v2.1.5.3 adjudication materials. It was not used.
- **Shared scratchpad: independence disclosure.** Before I knew the scratchpad root was shared, my first sheet dump wrote to the root (`scratchpad/`) instead of a private folder. All later work is in my own subfolder `scratchpad/y2019_RB/` (with `img/` inside it). Exposure to other agents' files at the root was as follows.
  - **Possibly overwritten.** I wrote 2019 template dumps to these root files, which may already have existed as another agent's files: `Papers.txt`, `Candidates.txt`, `Evidence.txt`, `Links.txt`, `Relations.txt`, `Protocol_plan_table.txt`. I have not touched them since.
  - **Read.** Immediately after writing, I printed `Papers.txt` in full and about the first 6,000 characters of `Candidates.txt`. Both contained another agent's **2024** material:
    - the jama.2024.* paper list
    - the first 2024 candidates of `jama.2024.0318`, with their AI rationales
    - byte counts of the root `*.txt` files
  - **Listed by name only (contents not opened):** `C_jama.2024.0318.txt`, `Manifest.txt`, `cands.txt`, `dossier/`, `dossier_jama.2024.*.txt`, `dump.py`, `papers/`, `rb/`, `rt.xlsx`, `t.json`, `t.xlsx`. A filesystem search for PDF tools also printed the path `scratchpad/pdfenv/bin/pypdfium2`. I did not use that environment.
  - **2019 independence.** No 2019 R_A material was read: I did not open or list `y2019_RA_work/`, nor the top-level `tools/`, `txt/` or `img/` folders. The 2024 content I saw concerns different papers and played no part in any 2019 judgment.
- **Scripts.** No problems found in `fill_review.py` or `recalc_check.py`. A minor note: `fill_review.py` accepts and applies an optional field only when non-null, so an intentionally blank optional L keeps the template formula. This is the intended behavior.

## recalc_check output

```
G: {'PRIMARY READY': 62}
Checks 1 Check -> Result
Checks 2 Reviewer role -> R_B
Checks 3 Total candidates -> 62
Checks 4 Primary ready -> 62
Checks 5 Unfinished -> 0.0
Checks 6 Discuss / unresolved -> 0
Checks 7 Workflow status -> PRIMARY READY
Checks 8 Ready discuss rows -> 0
Checks 9 Papers with counts -> 9
Checks 10 Next action -> Save and deliver this independent review with its built-in results.
Checks 11 Scope -> Entry checks and independent completion only. Discuss is not a confirmed absence of error. Review the evidence; preserve ordinary Excel backups.
```
