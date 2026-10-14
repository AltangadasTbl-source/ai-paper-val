# v.2.4.1 independent primary review, 2025 cohort: reviewer R_A

Reviewer R_A reviewed all 109 candidates in the 13 papers with workflow 1.6.2 output (jama.2025.11178 and jama.2025.15185 are empty placeholder sheets). Each candidate was judged from the original PDFs at the cited locations before the candidate's card in `final_report_1_6_2.md` was read. I did not open the R_Bulun folder or any other reviewer folder under `reviewer_runs/`, any other working folder, anything under `human_adjudication_v_2_3_1/` or `human_adjudication/previous/`, `meta_report/`, the paper packages under the repository's `2025/` folder, any `.ai_paper_validation/` folder, or git history. All source material came from the read-only mirror of the PDFs, cards and `QUALITY_CONTROL_SCOPE.md`.

## Files

- `human_adjudication_v_2_4_1_2025_R_A_completed.xlsx`: completed workbook built with `fill_review.py`. `recalc_check.py` reports 109/109 rows `PRIMARY READY` and Checks workflow status `PRIMARY READY`.
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
