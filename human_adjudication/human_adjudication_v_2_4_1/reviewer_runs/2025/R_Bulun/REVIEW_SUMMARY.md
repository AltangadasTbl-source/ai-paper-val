# v.2.4.1 independent primary review, 2025: reviewer R_Bulun

Reviewer R_Bulun. All 109 candidates in the 2025 workbook (13 papers; jama.2025.11178 and jama.2025.15185 are empty placeholders) were judged from the original PDFs before the corresponding final-report card was read. I did not open or list the other reviewer's folder or any other year or role folder under `reviewer_runs/`, anything under `human_adjudication_v_2_3_1/` or `human_adjudication/previous/`, `meta_report/`, the repository paper packages or any `.ai_paper_validation/` folder, or the excluded jama.2024.2302 document, and I did not use git history. Sources were limited to the read-only mirror of PDFs, final reports and `QUALITY_CONTROL_SCOPE.md` files.

## Files

- `judgments.json`: one record per candidate (D, E, H-L, column R note, evidence, rationale with recomputations).
- `human_adjudication_v_2_4_1_2025_R_Bulun_completed.xlsx`: built from the R_B blank with `fill_review.py`; `recalc_check.py` reports 109/109 rows PRIMARY READY and Workflow status PRIMARY READY.
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
