# v.2.4.1 independent primary review, 2025 cohort: reviewer R_A

Reviewer R_A reviewed all 109 candidates in the 13 papers with workflow 1.6.2 output. The remaining two papers, jama.2025.11178 and jama.2025.15185, were reviewed on 2026-10-14 after their reports were completed, and are reported in the addendum at the end. Each candidate was judged from the original PDFs at the cited locations before the candidate's card in `final_report_1_6_2.md` was read. I did not open the R_Bulun folder or any other reviewer folder under `reviewer_runs/`, any other working folder, anything under `human_adjudication_v_2_3_1/` or `human_adjudication/previous/`, `meta_report/`, the paper packages under the repository's `2025/` folder, any `.ai_paper_validation/` folder, or git history. All source material came from the read-only mirror of the PDFs, cards and `QUALITY_CONTROL_SCOPE.md`.

## Files

- `human_adjudication_v_2_4_1_2025_R_A_completed.xlsx`: completed workbook built with `fill_review.py`. `recalc_check.py` reports 109/109 rows `PRIMARY READY` and Checks workflow status `PRIMARY READY` (133/133 after the 2026-10-14 rebuild; see the addendum).
- `judgments.json`: one row per candidate with D, E, H to L, the column R note, the evidence inspected and the full rationale with recalculations.
- `REVIEW_SUMMARY.md`: this file.
- Recalculation scripts (R, Python), OCR output and page renders are in the private working folder `scratchpad/work/2025/R_A/` (`r/`, `scripts/`, `ocr/`, `img/`).

## Counts

Dispositions: 101 retain, 8 exclude, 0 discuss.

| Review domain (final E) | Retain | Exclude | Discuss | Total |
|---|---:|---:|---:|---:|
| statistical_results | 35 | 1 | 0 | 36 |
| report_internal_inconsistency | 0 | 0 | 0 | 0 |
| plan_material | 8 | 3 | 0 | 11 |
| protocol_report | 58 | 4 | 0 | 62 |
| Total | 101 | 8 | 0 | 109 |

E changed from the AI suggestion (3; all report_internal_inconsistency to statistical_results). Each one is a numerical value attributed to the wrong quantity or outcome, and the Codebook says to use statistical_results when judging a numerical reporting error:

- `2025::jama.2024.27643::C008`: 24-week SVC change estimates (−9.32 vs −8.53) are labelled as monthly rates in the article.
- `2025::jama.2025.20765::C012`: all-cause mortality (52/1080 = 4.8%) is presented as TB-specific mortality (32/1080 = 3.0%).
- `2025::jama.2025.24175::C013`: identical interaction-model output is printed for two different outcomes (primary response and 28-day mortality).

Exclusions (8):

- `2025::jama.2024.27643::C015`: line-end dash before ".3675" in an illustrative example trial in the master SAP; not a design element of this trial.
- `2025::jama.2025.16450::C004`: count/percentage slip (31/294 printed 20%; numerator should be 60) in historical-cohort background data, not a design element.
- `2025::jama.2025.19563::C003`: HbA1c-branch restriction comes from a dated protocol amendment (v1.4, March 2022, during enrollment); the report follows the amended plan.
- `2025::jama.2025.19563::C008`: wrong portal-access percentages in the recruitment-pool paragraph of the protocol; not a statistical design element.
- `2025::jama.2025.20765::C011`: the 10% attrition figure belongs to the overall multi-phase summary; the Phase 3 calculation in the same protocol, the SAP and the report all use 20%.
- `2025::jama.2025.4390::C006` and `C007`: outcome-hierarchy and vision-outcome wording changed between the 2016 protocol and the SAP, which was written before the interim analysis while investigators were blinded. The report matches the SAP.
- `2025::jama.2025.9110::C002`: ICU HR 0.93 (0.88-1.00) with P = .04 is compatible once display rounding is taken into account (CI-implied P range 0.009-0.057).

Rule applied to plan versions: where the report follows a later plan version fixed before follow-up was complete, I treated the earlier version as superseded and excluded the candidate. Where the later plan was finalized after follow-up ended (24175, 20765, 7583, 7710), or where concurrent plan documents conflict (27643 C001, 16450 C001, 7583 C002, 9663 C001-C002), I retained the difference.

## Outcome codes (retained rows)

statistical_results (35 retained):

- H: confirmed_issue 27; probable_issue 5; indeterminate 3; not_issue 0.
- I: substantive 10; minor_presentation 22; indeterminate 3.
- J (all assessed): direct 5; possible 16; unlikely 14.

Confirmed or probable and substantive (10): `jama.2024.24764::C001`, `jama.2024.27643::C007`, `jama.2024.27643::C008`, `jama.2024.27643::C013`, `jama.2025.19563::C013`, `jama.2025.20765::C006`, `jama.2025.20765::C012`, `jama.2025.24175::C009`, `jama.2025.24175::C010`, `jama.2025.24175::C013` (all prefixed `2025::`).

K (plan_material, 8 retained): substantive_inconsistency 2 (`jama.2024.27643::C011`, `jama.2025.20765::C015`); minor_presentation 6. No report_internal_inconsistency rows remain.

L (protocol_report, 58 retained): substantive_difference 51; minor_presentation 3; indeterminate 3; version_timing 1; none left blank. The minor_presentation rows are `jama.2025.20765::C008`, `jama.2025.7583::C001` and `jama.2025.7583::C002`. The indeterminate rows are `jama.2024.27643::C010`, `jama.2025.24175::C002` and `jama.2025.9663::C001`. The version_timing row is `jama.2025.4390::C003`. Disclosed changes (for example the 19563 SAP-change table, 7583 SAP v2, 9110 tobit model, 20765 post hoc covariates) were retained and marked "disclosed" in column R. L is a description of the difference only, not a judgment that the change was improper.

## Discuss list

None. Candidates I considered for discuss and why I did not use it:

- `jama.2025.19563::C009` (the printed R code computes an interpolated activity vector but passes the raw vector to the summary functions). The effect depends on whether the arctools functions impute internally, which I could not verify. I retained it with H and I indeterminate rather than deferring.
- `jama.2025.24175::C002` (LOCF triggered by ICU discharge while the stated rule is home discharge). Retained with L indeterminate.
- `jama.2025.9663::C001` (stratification-only analysis in the current protocol but not in the SAP). Retained with L indeterminate.
- `jama.2025.4390::C003` (the diuretic adaptive-decision timing may come from the published 2022 protocol, which is not supplied). Retained with L version_timing.

The published final protocols for 4390 (BMJ Open 2022) and the governing master SAP v2.0 for 27643 would resolve the version questions above.

## Where I disagreed with or went beyond the AI card

- Domain changes for 27643 C008, 20765 C012 and 24175 C013 (see Counts).
- `jama.2024.27643::C013`: the card raised a possible log/original-scale explanation without establishing it. My check confirmed it: the eTable 3B serum rows equal 100 × log-scale values (exp(0.268) − 1 = 30.7%; exp(−0.264) − 1 = −23.2%), which reproduce the article exactly.
- `jama.2024.27643::C012`: I judged the plasma rows to be rounding (CI-implied P 0.039/0.040). The serum 60-mg row has its estimate 4.5 units from the CI midpoint (−27.4 vs −22.9), which the card did not single out.
- `jama.2025.16450::C005`: the card flagged only the 2.5-kg cell. My check of all 144 factor cells found a second non-reproducing cell (0.125 LPM, 4 kg: printed 4, computed 3.1). Neither cell affects BPD classification thresholds.
- `jama.2025.16450::C006`: the card does not name the method. I recomputed all eight sparse rows: every printed interval is log-Wald, and exact (Fisher) intervals are much wider (e.g., 0.012-76.5 vs printed 0.06-15.66).
- `jama.2025.20765::C006`: I added that the "crude" RRs cannot be crude risk ratios (TB success 1.2 vs 1.04 from the counts; 1.1 vs 1.00 when excluding deaths). The card asserted no crude-ratio discrepancy.
- `jama.2025.20765::C014`: the card treats 14 rows as non-reproducing under a log-symmetric rule. Because the interval method is not stated, I recorded this as indeterminate.
- `jama.2025.24175::C013`: I added that the panel A subgroup ORs for 28-day mortality point in the opposite direction from those for the response outcome. The duplicated interaction tables therefore cannot both be correct, and the article's interaction claims rest on them.
- I excluded the five plan-material or version items listed under Counts, which the card had retained as findings.

## Possible errors outside the candidate set (observed, not adjudicated)

- jama.2024.24764: the pooled LOS ratio of geometric means 0.96 (0.88-1.06) is printed with P = .21 in the abstract, text and Table 3, but the CI implies P ≈ 0.39. The readmission RD 0.010 (−0.014 to 0.034) does not fit 11/399 vs 11/398. The discussion cites ASA 5 patients as excluded while Table 1 lists 7 ASA V patients.
- jama.2024.27643: the article reports the outlier-sensitivity NfL difference as −9.7% (−18.5% to 0.1%), P = .05; the eFigure gives +9.7% (−0.1% to +18.5%), P = .051. ALSFRS-R slope credible intervals in the article differ from eTable 2. M-SAP v3.0 (p8) states that regimen C is governed by M-SAP v2.0, which is not supplied.
- jama.2025.16450: eTable 4 abbreviations define "RR = risk difference". The article says 6 untreated infants were excluded, while Figure 1 footnote j says 5. eTable 1 labels the PP population "as treated", while Table 2 says all populations are by randomized assignment.
- jama.2025.19563: Figure 3 footnote labels baseline BMI as "baseline median weight". eTables 18a and 18b report identical results for two different physical-activity assumptions.
- jama.2025.19843: eTable 3 appears to swap duration and free-day labels for mechanical ventilation and kidney replacement therapy (median KRT duration 30 days). The abstract gives P values for secondary outcomes although Table 2 says they are not reported. The limitations section misstates the sample-size assumption (50% weaning failure vs 50% successful weaning).
- jama.2025.20765: Table 2 prints the death absolute difference as "4 (1.0 to 7.1)" (should be negative) and a CI "1.9 to 42". The protocol computes 704 × 1.5 as about 1080 (actually 1056). eTable 4 overall column 3/52 is printed as 5.7% and 8/52 as 15.2%.
- jama.2025.24175: the text gives 51 of 131 for day-15 SOFA responders, while Table 2 gives 52/131. Table 2 prints the mortality differences with the opposite sign convention to the primary row. SAP v2.0 is dated 18 May 2024, after last follow-up on 29 April 2024.
- jama.2025.4390: Table 1 calcium channel blocker 479/1677 is printed as 28.2% (computed 28.6%).
- jama.2025.7710: the primary GEE RR is 1.02 although crude risks are 5.1% vs 5.2% (crude RR 0.99). The article dates the analysis 24 October 2024; SAP v1.2 was finalized 25 October 2024.
- jama.2025.9110: the SAP states that secondary outcomes would be reported with effect sizes and CIs only, but Table 2 gives P values.

## Template or source issues

- Prior annotations in source PDFs. The supplied PDFs for jama.2025.4390 (article pp6, 8, 9; supplement 3 pp22, 29, 32, 37, 39) and jama.2025.7710 (article pp1, 4, 5) contain highlight and comment annotations, with author field "AltanGadasTbl", that mark suspected errors. Examples are "duplications, check the number on page 29" and "Duplicated numbers, different p values", which correspond to 4390 C011 and C012. I saw the highlights when rendering pages for 4390 C001, C011 and C012, and read the comment text afterwards through an annotation listing. My judgments rest on my own recalculations, but these files are not clean for independent review and should be replaced with unannotated originals. The 27643 protocol annotations (authors "karenho", "Michael hotchkin") appear to be original document artifacts.
- Text layers: the plan documents for 15440, 16450, 19563, 20765, 24175, 4390 (SAP), 9110 (SAP) and 9663 use encoded fonts with unusable text, and the 19843 SAP is scanned. Locations had to be read by OCR.
- jama.2025.20765 Supplement 1: the pages of the earlier protocol (v4.0) carry a running header "V6.0 07.03.25", which makes the version hard to identify (relevant to C015).
- Column C locations for 27643 begin with a generic phrase ("Physical PDF pages; PLAN/REPORT roles are stated above...") instead of a role per page, and several 20765 and 24175 locations run to several hundred characters. All cited pages were found.
- jama.2025.11178 and jama.2025.15185 have no candidates, as documented.

## OCR and rendering use

- OCR (RapidOCR, 300 dpi) for pages with encoded or missing text layers: 15440 protocol pp20-22 (Table 4 is printed rotated; I rotated the render and read it visually); 16450 protocol pp12, 21, 25, Manual pp39, 59, 152-154, SAP pp11, 22, 29, 32-39 and the entire results supplement (16 pages); 19563 protocol pp6, 15, 16, 18, 37-39, 80-81, 86-88; 19843 SAP pp1-9 (scanned); 20765 Supplement 1 (27 pages across protocol v4.0/v6.0, change log, SAP and SMS log); 24175 protocol/SAP pp7, 24-27, 57, 63-72; 4390 SAP pp1-7; 9110 protocol pp20-21 and SAP pp13, 14, 18, 28; 9663 protocol/SAP pp30, 69-71, 95-98, 104, 118-119, 126-132, 136.
- Rendered pages read visually where table layout mattered: 16450 Manual Table 1 (to confirm the 0.125-LPM row); 20765 results supplement pp3-15; 24175 supplement pp27, 29, 44, 51-53 (forest-plot panels); 4390 SAP p6 and supplement pp33-48; 27643 M-SAP p59 (the line-end dash); 20765 Supplement 1 overview pages (to locate document boundaries). OCR digits used in conclusions were checked against the rendered image.

## Limitations

- Plan documents that are cited but not supplied (the governing master SAP v2.0 for 27643, the 2022 published protocol for 4390, the external PD SAP for 27643) limit several protocol_report judgments. These are flagged in column R.
- I could not verify the arctools R package API (19563 C009). The interval method for 20765 is unstated, so C014 stays indeterminate.
- OCR of tables may misalign cells. I re-read every value used in a conclusion against a page render, but OCR omitted a few lines in prose passages; where this happened I relied on the surrounding text and on corroborating plan documents.
- The prior annotations in the 4390 and 7710 PDFs (see Template or source issues) were visible during part of the review, which compromises full independence for 4390 C001, C011 and C012. All three were also identifiable from the candidate titles and were confirmed by recalculation.
- Classifying L and I involves judgment. I applied a consistent rule to plan versions (see Counts) and to point-value typos with recoverable correct values (minor_presentation), but another reviewer could reasonably draw these lines differently.

## Addendum (2026-10-14): jama.2025.11178 and jama.2025.15185

### Independence statement

The 24 candidates of the two papers (11178 C001-C018; 15185 C001-C006) were judged in the same way as the other 109: from the original PDFs and the 11178 xlsx supplement at the cited locations first, and from the candidate's card in `final_report_1_6_2.md` afterwards. I did not open the R_Bulun folder, any other year or role folder under `reviewer_runs/`, `reviewer_runs/README.md`, any `compare_<year>.txt`, any other folder under `scratchpad/work/`, anything under `human_adjudication_v_2_3_1/` (other than running its Python interpreter for the validator) or `human_adjudication/previous/`, `meta_report/`, the paper packages under the repository's `2025/` folder, any `.ai_paper_validation/` folder, or git history. I re-read this summary and my earlier `judgments.json` to apply the same coding rules, in particular the plan-version rule (a plan finalized after follow-up ended does not supersede the earlier plan, so the difference is retained) and the rule that numerical reporting errors belong to statistical_results. The highlight annotations formerly on 11178 supplement 4 p. 7 had been removed from the copy I used; I saw no annotations in either paper's files.

### Files

- `judgments_11178_15185.json`: one row per candidate (24 rows) with D, E, H to L, the column R note, the evidence inspected and the full rationale with recalculations. `fill_review.py --check` reports no errors (the 109 earlier keys are listed as missing from this file, as expected).
- I did not modify `judgments.json` or the completed workbook. On 2026-10-14 the coordinator merged the 24 rows unchanged into `judgments.json` (now 133 rows) and rebuilt `human_adjudication_v_2_4_1_2025_R_A_completed.xlsx` from the rebuilt blank workbook; `recalc_check.py` reports 133/133 rows and Checks `PRIMARY READY`.
- Recalculation scripts (R and Python), OCR output and renders for these papers are in the private working folder `scratchpad/work/2025/R_A/` (`r/`, `scripts/`, `ocr/`, `img/`, `txt/`).

### Counts

Dispositions for the 24 candidates: 23 retain, 1 exclude, 0 discuss.

| Review domain (final E) | Retain | Exclude | Discuss | Total |
|---|---:|---:|---:|---:|
| statistical_results | 15 | 1 | 0 | 16 |
| report_internal_inconsistency | 0 | 0 | 0 | 0 |
| plan_material | 0 | 0 | 0 | 0 |
| protocol_report | 8 | 0 | 0 | 8 |
| Total | 23 | 1 | 0 | 24 |

All 133 candidates of the 2025 cohort (earlier 109 plus these 24): 124 retain, 9 exclude, 0 discuss.

| Review domain (final E) | Retain | Exclude | Discuss | Total |
|---|---:|---:|---:|---:|
| statistical_results | 50 | 2 | 0 | 52 |
| report_internal_inconsistency | 0 | 0 | 0 | 0 |
| plan_material | 8 | 3 | 0 | 11 |
| protocol_report | 66 | 4 | 0 | 70 |
| Total | 124 | 9 | 0 | 133 |

E changed from the AI suggestion: none of the 24. Each suggested domain matched the materials compared and the nature of the problem.

Exclusion (1):

- `2025::jama.2025.11178::C004`: the three NNT points that do not reproduce under conventional rounding (8, 7 and 8) are the round-up (ceiling) values of 1/RD. Across all 81 NNT points in Table 2 and eTables 7-8, every printed value equals the ceiling of 1/RD within display precision, and 24 are compatible only with rounding up. The tables apply the standard round-up convention consistently.

### Outcome codes (retained rows)

statistical_results (15 retained):

- H: confirmed_issue 12; probable_issue 3 (11178 C011, C018; 15185 C006); indeterminate 0; not_issue 0.
- I: substantive 6; minor_presentation 9; indeterminate 0.
- J (all assessed): direct 3; possible 5; unlikely 7.

Confirmed or probable and substantive (6): `2025::jama.2025.11178::C003`, `C008`, `C009`, `C010`, `C016`, and `2025::jama.2025.15185::C001`.

K: no plan_material or report_internal_inconsistency rows among the 24.

L (protocol_report, 8 retained): substantive_difference 7; indeterminate 1 (`2025::jama.2025.11178::C007`); none left blank. Disclosed changes were retained and marked in column R (11178 C007, IPW added to the SAP after follow-up ended; 15185 C004, deviations listed in supplement 3 p. 7; 15185 C002, partly disclosed as differences in "statistical terminology"). Under the plan-version rule, the 15185 SAP (signed 27 September 2024, one month after the last participant's last visit) does not supersede protocol v1.4 (28 February 2023), so the population and model changes in 15185 C002 and C003 are retained.

### Discuss list

None. Candidates I considered for discuss and why I did not use it:

- `jama.2025.11178::C007`: the SAP states that primary analyses use participants with follow-up data under MAR, then makes a pattern-mixture plus weighting approach conditional on more than 15% missingness, without saying whether that approach becomes primary. Retained with L indeterminate.
- `jama.2025.11178::C018`: the printed omnibus P values for physical function at 6 and 12 months cannot be reached from the contrast intervals within display rounding, but this assumes that the omnibus test used the same covariance as the contrasts. Retained as probable_issue.
- `jama.2025.15185::C006`: the serious adverse event categories could reconcile if one event can carry several categories, which the table does not state. Retained as probable_issue.
- `jama.2025.11178::C001`: a non-overlapping description of session length could be a revised estimate of completion time rather than a change in delivery. Retained as substantive_difference with that caveat in column R.

### Where I disagreed with or went beyond the AI card

- `jama.2025.11178::C004`: the card kept upward rounding as an unresolved alternative. Checking all 81 NNT points shows the convention is applied throughout, so I excluded the candidate.
- `jama.2025.11178::C008` and `C009`: the card could not identify a mechanism. In the text layer, exactly the six HC-vs-painTRAINER NNT intervals whose RR interval includes 1 use an en dash; all 21 others use a hyphen. Reading the en dash as a lost minus sign (for example 24 (12 to -186)) gives RD lower limits of -0.54 to -2.63 percentage points, matching those implied by the RR intervals and the table's own footnote e. The printed intervals therefore misstate null coverage, and C009 (63 outside 18-38) is one instance of the same error.
- `jama.2025.11178::C014`: the card treated ten rows as a null-significance pattern. For eTable 3, the z implied by each CI is about 1.94 times the z implied by its P value across all 20 rows with exact P values, and treating each interval as estimate plus or minus 1 SE reproduces the printed P values. The three rows the card took from eTables 4 and 5 (age, the second education row and PEG) reproduce once the limit printed as 1 or 1.00 is allowed its rounding range.
- `jama.2025.11178::C016`: beyond the summary-statistic label conflict, the three raw-score columns of eTable 11 reproduce all printed mean differences in 21 of 21 rows only when ordered usual care, painTRAINER, health coach. The printed column labels are permuted. The card explicitly did not infer this.
- `jama.2025.11178::C012`: the xlsx selection P values resolve the conflict: employment meets the stated selection rule for the weight model and education does not, so eTable 5 is consistent with the rule and eTable 2 names the wrong variable.
- `jama.2025.11178::C003`: the Results text quotes 3-month SMDs of -0.26 and -0.36, which are the 6-month values in Table 3 (3-month values -0.25 and -0.34).
- `jama.2025.11178::C018`: the covariance of the two contrasts with usual care is identified from the three contrast intervals, so the omnibus reconstruction does not need an independence assumption. My values (P = .025 and .010; minimum over the rounding box about .009 and .003) agree with the card's bounds.
- `jama.2025.15185::C006`: the card counted only two failing sums because it allowed plus or minus 0.5 per integer count. Without that allowance all four comparisons fail (levodopa 143 vs 126 and placebo 139 vs 129 at the top level; infection subtypes 59 vs 55 and 52 vs 44).
- `jama.2025.15185::C001`: the card set aside the text-table difference as within tolerance. The text's levodopa PROMIS-29 mean of 66 does not round from eTable 4's 64.74.
- `jama.2025.15185::C005`: the article labels the center plot and the FMA 35-point subgroup as post hoc, although the protocol and SAP prespecified a center display and a median split of baseline FMA (median 34).

### Possible errors outside the candidate set (observed, not adjudicated)

- jama.2025.11178: health coach adverse events 16/778 are printed as 2.0% (2.06%). The xlsx counts 1713 women; Table 1 sums to 1712. Table 2 column headers give n = 643, 690 and 703 (participants with any follow-up), while the analysis is described as covering all randomized participants with weighting. The SAP (p. 21) says the painTRAINER enhancement began after about 140 enrollments; supplement 4 (p. 13) and eTable 8 give 454. eTable 4 prints the "Health Coach vs painTRAINER 3M" row twice. The eTable 8 footnotes call the RR column note "c", which is the omnibus P note.
- jama.2025.15185: the text and eTable 4 disagree on PROMIS-10 means (28 (6) in both groups vs 29.87 and 30.04), the placebo FMA SD at 5 weeks (26 vs 25.20) and the placebo PRAI numerator (52 vs 51 of 270). In eTable 1, the row labelled median NIHSS shows mean (SD)-type values (8.2 (3.9)), and the row labelled time from onset shows values matching the NIHSS medians in main Table 1 (7 [5-11], 8 [5-10]); the main table gives time from onset as 3.0 (2.0-5.0). eTable 6 gives n = 145 prespecified AEs overall vs 67 + 79 = 146. eFigure 7's color legend ("moderate - severe" vs "very severe impairment") does not match the subgroup definition in its own legend and in the text (35 or less severe; more than 35 mild to moderate). eFigure 5 is titled FMA at 3 months but its axis shows change from visit 1 to visit 3. Table 1 labels the age row "Median age 80 y or older".

### Template or source issues

- The protocol and SAP of jama.2025.11178 and the SAP, much of the protocol and the analysis code of jama.2025.15185 have encoded or missing text layers; all cited locations had to be read by OCR or from renders.
- Supplement 1 of jama.2025.15185 contains two protocol versions (v1.1, 30 November 2018, pp. 1-46; v1.4, 28 February 2023, pp. 47-94) without a separating label; the candidate locations cite both.
- 11178 Table 2 is printed rotated, so its column alignment had to be checked on a render.
- No annotations were visible in the copies supplied for these two papers.

### OCR and rendering use

- OCR (RapidOCR, 300 dpi unless stated): 11178 protocol pp. 1, 43-44, 55-57 and SAP pp. 1-5, 19-21; 15185 SAP pp. 1-18, protocol pp. 1-2, 10, 39, 55-56, 70, 85-88, and protocol pp. 46-52 at 200 dpi to locate the v1.4 cover page.
- OCR dropped lines on several pages, so I read the rendered pages for every value or sentence used in a conclusion: 11178 protocol pp. 43-44, 56-57 and SAP pp. 19-21 (110 dpi); 11178 main p. 9 (Table 2, 170 dpi); 15185 protocol pp. 86-87, SAP pp. 4 and 11 (top), main p. 6 (Table 2 at 200 dpi, for indentation), the analysis code (150 dpi) and supplement 3 pp. 18, 25 and 27 (eTables 7-8, eFigures 5 and 7).
- The 11178 xlsx was read directly with openpyxl; character codes of the Table 2 interval separators were read from the PDF text layer.

### Limitations

- Several 11178 judgments rest on reconstructions: NNT rounding (C004), the lost-minus interpretation (C008, C009), the 1.96-factor pattern in eTable 3 (C014), the omnibus Wald reconstruction (C018) and the eTable 11 column order (C016). Each reproduces across many rows, but none can be confirmed without the authors' output.
- The SMD columns of 11178 Table 3 are wrong in several distinct ways, and no single column shift reproduces them, so the intended values cannot be recovered.
- For 15185 C006, multiple coding of a single event would explain part of the excess; the event-level coding is not supplied.
- OCR of the encoded plan documents omitted some lines; I relied on the rendered pages for those passages. As before, classifying I and L involves judgment, particularly for 11178 C001 (session length) and C007 (missing-data hierarchy).
