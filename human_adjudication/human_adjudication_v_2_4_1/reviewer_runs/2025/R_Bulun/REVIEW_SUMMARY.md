# v.2.4.1 independent primary review, 2025: reviewer R_Bulun

Reviewer R_Bulun. All 109 candidates in the 2025 workbook (13 papers) were judged from the original PDFs before the corresponding final-report card was read. jama.2025.11178 and jama.2025.15185 were reviewed on 2026-10-14, after their reports were completed, and are reported in the addendum at the end. I did not open or list the other reviewer's folder or any other year or role folder under `reviewer_runs/`, anything under `human_adjudication_v_2_3_1/` or `human_adjudication/previous/`, `meta_report/`, the repository paper packages or any `.ai_paper_validation/` folder, or the excluded jama.2024.2302 document, and I did not use git history. Sources were limited to the read-only mirror of PDFs, final reports and `QUALITY_CONTROL_SCOPE.md` files.

## Files

- `judgments.json`: one record per candidate (D, E, H-L, column R note, evidence, rationale with recomputations).
- `human_adjudication_v_2_4_1_2025_R_Bulun_completed.xlsx`: built from the R_B blank with `fill_review.py`; `recalc_check.py` reports 109/109 rows PRIMARY READY and Workflow status PRIMARY READY (133/133 after the 2026-10-14 rebuild; see the addendum).
- `REVIEW_SUMMARY.md`: this file.
- Working material (text extractions, OCR output, renders, R and Python scripts) is in my private working folder, not in the output folder.

## Counts

Dispositions: retain 100, exclude 9, discuss 0.

| E (final) | retain | exclude | discuss | total |
|---|---:|---:|---:|---:|
| statistical_results | 30 | 3 | 0 | 33 |
| report_internal_inconsistency | 3 | 0 | 0 | 3 |
| plan_material | 7 | 5 | 0 | 12 |
| protocol_report | 60 | 1 | 0 | 61 |
| total | 100 | 9 | 0 | 109 |

E changed from the AI suggestion (1):

- 2025::jama.2025.20765::C011 (protocol_report to plan_material): the report's 20% attrition matches the protocol's own sample-size calculation; the conflict is between that calculation and a 10% statement elsewhere in the same protocol, so the report only corroborates one side of a plan-internal inconsistency.

Exclusions (9):

- 2025::jama.2024.27643::C012: the eTable 3B CI-versus-P disagreements are explained by display rounding (main text gives the plasma upper limit as -0.4%; CI-implied P computed .041).
- 2025::jama.2024.27643::C014: wording slip ("estimated DRR decrease") in simulation commentary of a master SAP version that by its own governance clause does not apply to this regimen; the next sentence states the intended meaning.
- 2025::jama.2024.27643::C015: stray dash before ".3675" in an illustrative example in the same non-operative master SAP; the figure prints 0.3675.
- 2025::jama.2025.16450::C004: count/percentage slip (31/294 printed as 20%; 60/294 = 20.4% reconciles the row) in historical background data that do not inform this trial's design or analysis.
- 2025::jama.2025.19563::C003: the HbA1c-branch restriction was introduced by a dated protocol amendment (v1.4), and the report follows the amended protocol.
- 2025::jama.2025.19563::C008: inconsistent recruitment-pool portal counts and percentages in a feasibility paragraph; not a design element.
- 2025::jama.2025.19563::C010: summing valid wear periods over all available periods is exactly what zero assignment implies; the descriptions are compatible.
- 2025::jama.2025.9110::C002: HR 0.93 (0.88-1.00) with P=.04 is compatible once half-unit rounding is allowed (CI-implied P spans .009-.057).
- 2025::jama.2025.9663::C005: inverted wording of the adherence numerator in internal-pilot progression criteria; the adherence definition two pages later is clear and the pilot criteria do not enter the reported analysis.

## Outcome codes (retained rows)

statistical_results (30 retained):

- H: confirmed_issue 27, probable_issue 3 (2025::jama.2025.19563::C009, C012, C013), not_issue 0, indeterminate 0.
- I: minor_presentation 23, substantive 6, indeterminate 1 (2025::jama.2025.19563::C009).
- J: unlikely 21, possible 5, direct 3, unknown 1.

Confirmed or probable and substantive (6, all confirmed):

- 2025::jama.2024.24764::C001 (abstract/body "no difference in quality of life" versus day-7 EQ-5D index P=.02)
- 2025::jama.2024.27643::C007 (model mortality rates 0.007/0.006 in the article vs 0.010/0.009 in eTable 2)
- 2025::jama.2024.27643::C013 (eTable 3B serum NfL rows on the log x100 scale but labeled % change; -26.4% vs -23.2%)
- 2025::jama.2025.20765::C006 (headline "crude" RR 3.0 vs crude ratio 2.73 and supplementary unadjusted RR 2.89; RR derivation from a logistic model not described)
- 2025::jama.2025.24175::C009 (MALS "number needed to harm" 8.8 where serious adverse events were less frequent on treatment)
- 2025::jama.2025.24175::C010 (finite NNH intervals for nonsignificant differences)

K (retained report_internal_inconsistency and plan_material, 10): report_internal_inconsistency substantive_inconsistency 3 (2025::jama.2024.27643::C008, 2025::jama.2025.20765::C012, 2025::jama.2025.24175::C013); plan_material minor_presentation 6, substantive_inconsistency 1 (2025::jama.2024.27643::C011).

L (retained protocol_report, 60): substantive_difference 52, version_timing 4 (2025::jama.2024.27643::C004, 2025::jama.2025.19563::C002, 2025::jama.2025.4390::C003, C004), minor_presentation 2 (2025::jama.2025.20765::C008, 2025::jama.2025.7583::C002), indeterminate 1 (2025::jama.2025.20765::C004), left blank 1 (2025::jama.2025.7583::C001: the planned between-group comparison of embolization-procedure complications is degenerate because the control arm cannot have them). Rows where the report itself discloses the change were retained with "Disclosed" in column R (for example 2025::jama.2025.19563::C001, C004-C007; 2025::jama.2025.7583::C003; 2025::jama.2025.9110::C001; 2025::jama.2025.4390::C006).

## Discuss list

None. Candidates I considered for discuss: 2025::jama.2025.19563::C009 (whether the printed R code's summary functions re-impute internally depends on package defaults I could not check; retained as probable_issue with indeterminate substantiveness because the code as printed does not pass the interpolated series and three bout calls are identical); 2025::jama.2025.4390::C003 and C004 (the final published protocol cited by the report is not supplied; coded version_timing); 2025::jama.2025.20765::C014 (log-asymmetric RR intervals are expected under an unstated OR-to-RR conversion, so only the demonstrable typographic upper limit "42" was treated as the issue).

## Where I disagreed with or went beyond the AI card

- 2025::jama.2024.27643::C012: card retained a CI/P significance conflict; I excluded it as rounding. I added that the 60-mg serum interval is asymmetric about its estimate on the log scale (recorded under C013).
- 2025::jama.2024.27643::C013: card listed the log/original-scale explanation only as an alternative; my computation shows the serum rows reproduce exactly on the log x100 scale (P=.030 recomputed).
- 2025::jama.2024.27643::C014, C015 and 2025::jama.2025.9663::C005, 2025::jama.2025.16450::C004, 2025::jama.2025.19563::C008: excluded as content that does not bear on the reported design or analysis.
- 2025::jama.2025.19563::C003: excluded because the report follows a formally amended protocol.
- 2025::jama.2025.24175::C013: beyond the card, the panel B "interaction" rows in eFigures 7-9 reproduce exactly the within-subgroup treatment ORs (e.g., SOFA>=10: 3.08, 1.37-6.96) rather than interaction terms, so the article's interaction claims rest on mislabeled output; 2025::jama.2025.24175::C014's "0.11" is a typo for 1.11.
- 2025::jama.2025.20765::C006: added the cross-table disagreement between Table 2 crude RR 3.0 and eTable 8 unadjusted RR 2.890.
- 2025::jama.2025.20765::C019: added the same sign reversal for the death row of main Table 2.
- 2025::jama.2025.16450::C005: a second factor-table cell (0.125 LPM, 4 kg) is also off by one; neither can change BPD classification.
- 2025::jama.2025.16450::C001: added that the report's severe-hyperglycemia definition also differs from the SAP.
- 2025::jama.2024.24764::C003: added that Table 1 lists ASA class V participants although the discussion says patients unlikely to survive were not included.
- 2025::jama.2024.27643::C007: added the ALSFRS-R slope credible-interval discrepancies between article and eTable 2.
- 2025::jama.2024.27643::C010: added the El Escorial subgroup partition difference.
- 2025::jama.2025.19563::C009: added that the three threshold-specific BoutsOfPA calls are identical.
- 2025::jama.2025.4390::C006 and others: noted partial disclosure in eAppendix Section 5.

## Possible errors outside the candidate set (observed, not adjudicated)

- jama.2024.24764: pooled LOS ratio of geometric means 0.96 (0.88-1.06) with P=.21 (abstract, p.6, Table 3); the CI implies P of about .39 (.33-.45 allowing for rounding).
- jama.2024.27643: plasma NfL CI printed three ways (text -17.8 to -0.4%; Figure 3 -17.8 to -0.5%; eTable 3B -18.0 to 0).
- jama.2025.16450: Table 2 footnote says all populations analyzed by randomized group, but eTable 1 labels the per-protocol set "as treated"; Figure 1 footnote says 5 untreated, the text says 6.
- jama.2025.19563: Figure 3A footnote labels BMI values as weight; the supplement's methods index lists eTables 18 and 19 twice with different content.
- jama.2025.19843: eTable 3 kidney replacement therapy "duration" 30 (0-30) days and "free days" 0 (0-2) appear swapped (dialysis occurred in about a third of patients); mechanical-ventilation rows look similarly suspect. Table 2 says P values are not reported for secondary outcomes, but the abstract gives them.
- jama.2025.20765: Table 2 adjusted self-report RR printed "2.8 (1.9 to 42)"; the protocol computes "704 x 1.50 ~ 1080" (704 x 1.5 = 1056); Supplement 1 pages labeled as the v4.0 protocol carry v6.0 headers.
- jama.2025.24175: day-15 responders "51 of 131" in the text vs 52/131 in Table 2; 28-day and 90-day mortality differences use opposite sign conventions; the abstract's "1069 serious TEAEs (88.8%)" applies a patient percentage to an event count; eFigure 7 panel A plots the SOFA<10 marker at about 1.0 although the counts give OR 2.02; SAP v2.0 is dated 18 May 2024, after the last follow-up.
- jama.2025.4390: the article says both that the trial "ran to completion" and that it "stopped early solely due to funding constraints".
- jama.2025.7710: the protocol and SAP describe Benjamini-Hochberg as controlling the family-wise error rate (it controls the false discovery rate).
- jama.2025.9110: Table 2 labels the ventilation row "mean (SD)" but prints median (IQR)-type values; the SAP says secondary outcomes would be reported without P values, yet Table 2 gives them.

## Template or source issues

- Text layers are unusable (font-encoding garbage) for large parts of several supplements: jama.2025.15440 Supplement 1, jama.2025.16450 Supplements 1-3, jama.2025.19563 Supplement 1 (entire), jama.2025.20765 Supplement 1, jama.2025.24175 Supplement 1, jama.2025.9110 Supplement 2, jama.2025.9663 Supplement 1; jama.2025.19843 Supplement 2 (SAP) has no text layer. All were read by OCR, with renders where OCR dropped light-gray lines.
- jama.2025.20765 Supplement 1: pages 6-39, listed in its table of contents as the earlier v4.0 protocol, carry "V6.0 07.03.25" running headers although their content is v4.0.
- jama.2025.4390: only the May 2016 protocol and an amendment log are supplied; the final protocol (published 2022) that the article and SAP cite is not, which limits several protocol_report judgments.
- jama.2025.20765 Supplement 1 image files (png/jpg) are small logo images and were not needed.
- No mismatch was found between workbook titles/locations and the cards; cited pages existed at the stated physical PDF page numbers.

## OCR and rendering use

- OCR (RapidOCR, 300 dpi): jama.2025.15440 Supp1 pp.20-22; jama.2025.16450 Supp1 pp.12, 21, 25, Supp2 pp.39, 59, 152, 154, Supp3 pp.11, 22, 29, 32-39; jama.2025.19563 Supp1 all 90 pages; jama.2025.19843 Supp2 all 9 pages; jama.2025.20765 Supp1 all 109 pages; jama.2025.24175 Supp1 all 72 pages; jama.2025.4390 Supp2 all 7 pages; jama.2025.9110 Supp2 all 31 pages; jama.2025.9663 Supp1 pp.29-31, 68-71, 94-95, 98, 103-104, 117-118, 127-128, 131-132. Reason in every case: garbled or missing text layer.
- Renders checked visually: jama.2024.27643 Supp2 p.59 (dash before .3675); jama.2025.15440 Supp1 p.22 (rotated power table); jama.2025.16450 Supp1 p.12 (Grade 3 cell); jama.2025.19563 Supp2 p.44; jama.2025.20765 Supp1 pp.49, 53 (lines missed by OCR); jama.2025.24175 Supp2 pp.51-53 (eFigures 7-9 are images); jama.2025.4390 Supp2 p.6 (SAP subgroup and sensitivity text missed by OCR) and Supp3 p.46 (column alignment); jama.2025.9663 Supp1 pp.30, 70, 71.

## Limitations

- Annotated source pages. After the coordinator's notice, all renders used `annots=False`. Before the notice, renders used the default setting, but none of the pages I rendered is on the coordinator's list of annotated pages (jama.2025.4390 main pp.6, 8, 9 and Supp3 pp.22, 29, 32, 37, 39; jama.2025.7710 main pp.1, 4, 5 and Supp1 p.1; jama.2024.27643 Supp1 pp.162, 172, 181, 183, 197). I read jama.2025.4390 main pp.6, 8, 9 and Supp3 pp.37, 39 and jama.2025.7710 main pp.1, 4, 5 only through the PDF text layer, which does not carry annotation content, and I did not see any annotation. The calls that use those pages (2025::jama.2025.4390::C001, C002, C005-C009, C011, C012 and 2025::jama.2025.7710::C001-C003) rest on my own reading of the printed text and my own recomputations (for example R tests for eTable 5 and the person-time check for Figure 3). I did not open jama.2024.27643 Supp1 pp.162-197.
- Some judgments depend on documents not supplied (later protocol versions, separate PD/analysis plans, published protocols). I coded version_timing or noted the limitation where this mattered.
- OCR occasionally drops light-gray lines; where wording was decisive I rendered the page, but minor OCR omissions elsewhere cannot be excluded.
- The arctools R package was not available locally, so for 2025::jama.2025.19563::C009 I could not check whether its summary function re-imputes internally.
- Recomputations use Wald or exact formulas from printed counts; where a report used model-based or bootstrap estimates, such checks indicate consistency rather than reproduce the authors' analysis.
- L is optional and reflects my description of each difference only; it does not judge whether a change was justified.

## Addendum (2026-10-14): jama.2025.11178 and jama.2025.15185

### Independence statement

Reviewer R_Bulun judged the 24 new candidates (jama.2025.11178 C001-C018; jama.2025.15185 C001-C006) from the original PDFs and the 11178 xlsx supplement before reading each final-report card. I did not open or list the other reviewer's folder, any other year or role folder under `reviewer_runs/`, `reviewer_runs/README.md`, any `compare_<year>.txt`, any other folder under the scratchpad `work/` directory, anything under `human_adjudication_v_2_3_1/` (other than running its Python interpreter for the check) or `human_adjudication/previous/`, `meta_report/`, the repository paper packages or any `.ai_paper_validation/` folder, and I did not use git. Sources were the read-only mirror of the two papers (PDFs, xlsx, `final_report_1_6_2.md` and `QUALITY_CONTROL_SCOPE.md`). For consistency I re-read this summary and my earlier `judgments.json` and applied the same rules: disclosed plan-report changes retained with "disclosed" noted; count/percentage slips with correct counts coded minor_presentation; the domain chosen by the materials actually compared.

### Files

- `judgments_11178_15185.json`: 24 records (D, E, H-L, column R note, evidence, rationale with recomputations), in key order. `fill_review.py --check` reports no ERROR lines (the 109 earlier keys are listed as MISSING because they are in `judgments.json`).
- I did not modify `judgments.json` or the completed workbook. On 2026-10-14 the coordinator merged the 24 rows unchanged into `judgments.json` (now 133 rows) and rebuilt `human_adjudication_v_2_4_1_2025_R_Bulun_completed.xlsx` from the rebuilt R_B blank workbook; `recalc_check.py` reports 133/133 rows and Checks `PRIMARY READY`.

### Counts

New candidates (24): retain 23, exclude 1, discuss 0.

| E (final) | retain | exclude | discuss | total |
|---|---:|---:|---:|---:|
| statistical_results | 15 | 1 | 0 | 16 |
| report_internal_inconsistency | 0 | 0 | 0 | 0 |
| plan_material | 0 | 0 | 0 | 0 |
| protocol_report | 8 | 0 | 0 | 8 |
| total | 23 | 1 | 0 | 24 |

All 133 candidates of 2025 (earlier 109 plus these 24): retain 123, exclude 10, discuss 0.

| E (final) | retain | exclude | discuss | total |
|---|---:|---:|---:|---:|
| statistical_results | 45 | 4 | 0 | 49 |
| report_internal_inconsistency | 3 | 0 | 0 | 3 |
| plan_material | 7 | 5 | 0 | 12 |
| protocol_report | 68 | 1 | 0 | 69 |
| total | 123 | 10 | 0 | 133 |

E changed from the suggested domain: none among the 24 (one change in the year overall, 2025::jama.2025.20765::C011, reported above).

Exclusions (1):

- 2025::jama.2025.11178::C004: the three "non-reproducing" NNT points follow the standard round-up convention. Ceiling of 100/(difference in printed adjusted percentages) reproduces all 57 positive NNT points in Table 2 and eTables 7-8 within display rounding, whereas round-to-nearest fails 22 of them.

### Outcome codes (retained rows)

statistical_results (15 retained):

- H: confirmed_issue 13, probable_issue 1 (2025::jama.2025.11178::C018), indeterminate 1 (2025::jama.2025.15185::C006), not_issue 0.
- I: substantive 4, minor_presentation 11, indeterminate 0.
- J: direct 3, possible 3, unlikely 9, unknown 0.

Confirmed or probable and substantive (4, all confirmed):

- 2025::jama.2025.11178::C003 (Table 3 SMDs incompatible with the stated common usual-care SD in 19-20 of 21 rows, including sign reversals; the Results text quotes the 6-month SMDs as 3-month values)
- 2025::jama.2025.11178::C010 (14 SMD points outside their printed CIs, 18 intervals with descending limits, 20 SMD intervals disagreeing with the MD intervals on null coverage)
- 2025::jama.2025.11178::C016 (eTable 11 labeled median/IQR but showing mean-type values with CI-like bounds, and the group columns in the order usual care, painTRAINER, health coach rather than as labeled)
- 2025::jama.2025.15185::C001 (single PROMIS-29 score and effect reported without aggregation rule or favorable direction)

K: no retained report_internal_inconsistency or plan_material rows among the 24.

L (8 retained protocol_report rows): substantive_difference 7, indeterminate 1 (2025::jama.2025.11178::C001, session durations), left blank 0. Rows where the report discloses the change: 2025::jama.2025.11178::C007 (IPW added by the 17 July 2024 SAP amendment, disclosed in Supplement 4); 2025::jama.2025.15185::C004 (deviations listed in Supplement 3); 2025::jama.2025.15185::C002 and C003 are only partly disclosed (main p.5 describes the protocol-SAP differences as terminology).

### Discuss list

None. Candidates considered for discuss: 2025::jama.2025.15185::C006 (whether Table 2 SAE categories may overlap is not stated; retained with H indeterminate because the record is worth keeping and the documents cannot settle it); 2025::jama.2025.11178::C018 (the eTable 11 omnibus test is undefined; retained as probable_issue); 2025::jama.2025.11178::C007 (the SAP's conditional missing-data clause partly supports the reported hierarchy; retained as a difference because the SAP never designates the pattern-mixture/IPW analysis as primary or the complete-case analysis as sensitivity).

### Where I disagreed with or went beyond the AI card

- 2025::jama.2025.11178::C004: the card registers three NNT points and lists rounding up only as an alternative; my full-table check shows round-up is the operative convention, so I excluded the candidate.
- 2025::jama.2025.11178::C008 and C009: the card attributes the finite NNT intervals to possibly different RR/RD interval constructions. The six affected cells are the only ones printed with an en dash, eTables 7-8 print the same construction with a negative NNH limit (eg "31 (13, -60)"), and RR-based approximations give NNH limits close to the printed second numbers (152, 70, 59, 39, 68, 84 vs 186, 76, 57, 38, 67, 79). The minus sign was lost, and the "point outside interval" in C009 (63 (18-38)) is the same display defect.
- 2025::jama.2025.11178::C014: the printed P values in eTable 3 reproduce almost exactly when each "95% CI" is read as estimate ± 1 SE (correlation 0.999), so the intervals are mislabeled. The three ratio rows the card adds from eTables 4-5 are compatible with display rounding.
- 2025::jama.2025.11178::C012: the workbook's selection P values resolve the direction (employment, not education, met the weight-model rule), so eTable 2's list is the error.
- 2025::jama.2025.11178::C015: subtraction from eTable 1 gives the implied 3-month counts for the first subset (109, 94, 108; total 311).
- 2025::jama.2025.11178::C016: added the column misassignment (mean absolute error 0.03 under usual care/painTRAINER/health coach vs 1.02 as labeled).
- 2025::jama.2025.11178::C003: added the Results-text SMDs (-0.26, -0.36 called 3-month values; Table 3 prints them at 6 months).
- 2025::jama.2025.11178::C001: noted that the coach session duration also differs (60 vs 45-60 minutes).
- 2025::jama.2025.15185::C005: added two planned analyses reported as post hoc, the protocol per-protocol analysis (estimand 11) and the center-stratified display (eFigure 5).
- 2025::jama.2025.15185::C006: my render shows that only the stroke subtypes are indented, and the trauma/fall/fracture rows suggest overlapping classification; I therefore coded H indeterminate rather than an established count error.
- 2025::jama.2025.15185::C001 and C004: added the main-text vs eTable 4 copy discrepancies (PROMIS-29 levodopa 66 vs 64.74; PRAI placebo 52/270 vs 51/270).

### Possible errors outside the candidate set (observed, not adjudicated)

- jama.2025.11178: SAP §14 says the painTRAINER enhancement started after about 140 enrollees, whereas Supplement 4 p.13 and eTable 8 give 454. The xlsx gives 1713 women, whereas Table 1 and the abstract give 1712. eTable 5 notes that site information "has been excluded" but prints three unlabeled site rows. eTable 4 lists the 3-month HC vs PT contrast twice. Table 3 labels PGIC values "mean change from baseline", although PGIC has no baseline measurement.
- jama.2025.15185: main p.6 PROMIS-10 is 28 (6) in both groups vs eTable 4 29.87/30.04, and the 5-week placebo SD is 26 vs 25.20. The win-ratio estimate is called an odds ratio with upper limit 1.25 in the eTable 2 text vs 1.26 in the eTable 2 table. eTable 6 gives an overall n of 145 vs 146. The deviation section says "two deviations" but lists three. The color legend of eFigure 7 ("moderate-severe" / "very severe impairment") does not match its text legend (≤35 severe vs >35 mild to moderate).

### Template or source issues

- Text layers unusable (font-encoding garbage): jama.2025.11178 Supplement 1 (protocol) and Supplement 2 (SAP); jama.2025.15185 Supplement 1 (protocol; most analysis pages) and Supplement 5 (analysis code). jama.2025.15185 Supplement 2 (SAP) has no text layer.
- jama.2025.15185 Supplement 1 contains more than one protocol version (eg synopses at pp.10 and 56, §11.4.2 at pp.39 and 86); the candidate locations use the later version, which I confirmed.
- The workbook titles and locations matched the cards; cited pages existed at the stated physical PDF page numbers. No reader highlights were present on 11178 Supplement 4 p.7.

### OCR and rendering use

- OCR (RapidOCR, 300 dpi): jama.2025.11178 Supplement 1 all 77 pages and Supplement 2 all 29 pages; jama.2025.15185 Supplement 2 all 18 pages, Supplement 1 pp.10, 39, 56, 70, 86, 87, and Supplement 5 p.1. Reason in every case: garbled or missing text layer.
- Renders viewed (annots=False): jama.2025.11178 main pp.9-11 (rotated Tables 2-3, 200 dpi), Supplement 1 pp.42-44 and 56-57, Supplement 2 pp.19-21 (OCR dropped lines); jama.2025.15185 main p.6 (Table 2 indentation, 170 dpi), Supplement 1 pp.86-87 (OCR dropped lines), Supplement 2 p.11, Supplement 3 pp.25, 27 (eFigures 5 and 7 are images).

### Limitations

- Several 11178 judgments rest on reconstructions from rounded displays: the NNH approximation from RR limits ignores the covariance between the painTRAINER percentage and the RR; the omnibus reconstruction assumes all three contrasts come from one fit; and the ±1 SE reading of eTable 3 is inferred from the P values rather than stated. I graded certainty accordingly (C018 probable).
- jama.2025.15185 Supplement 3 eTables 7-8 (image-only, p.18) were identified from the index but not inspected; they concern post hoc baseline-FMA models and did not bear on a candidate decision.
- OCR drops light-gray lines; where wording was decisive I read the rendered page, but minor omissions elsewhere in the protocol and SAP OCR cannot be excluded.
- L remains optional and descriptive; it does not judge whether a change was justified.
