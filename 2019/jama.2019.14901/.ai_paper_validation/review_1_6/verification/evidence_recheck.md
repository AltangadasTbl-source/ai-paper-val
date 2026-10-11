# Workflow 1.6 Mechanical Evidence Recheck

Scope: every assigned stable ID C001–C032, separately rechecked against supplied PDF pages. Runtime task: `/root/evidence_recheck`; stage preset `qc16_evidence_rechecker`; model `gpt-6.1-sol`; reasoning effort `high`. All IDs remain Pending Human Adjudication. Evidence states describe the evidence record only.

## Direct-source procedure and derivatives

Fresh direct Poppler 26.01.0 `pdftotext -layout` reads were made from all three supplied PDFs, preserving page breaks. Derivatives are `preprocessing/evidence_recheck/main-layout.txt`, `preprocessing/evidence_recheck/results-layout.txt`, and `preprocessing/evidence_recheck/plan-layout.txt`. Exact-source pages were rendered with direct Poppler 26.01.0 `pdftoppm -singlefile -scale-to 2000 -png`: main p8, results pp4/8/9, and plan pp7/42. Their six PNGs are in `preprocessing/evidence_recheck/`. These fresh renders were visually inspected for table column assignment, four cough/secretion cells, all center denominators, the survival title/axis/P value, plan abbreviation spelling, and the readiness worksheet. Direct native/layout extraction supplied the remaining readable printed text. Existing derivatives were used only to locate pages; neither they nor prior scientific conclusions supplied final authority. No OCR, GPU, installation, or source/reused-artifact modification occurred.

Direct R 4.5.2 arithmetic checked the authored calculations; output is `preprocessing/evidence_recheck/calculations.txt`. Commands used `chisq.test(..., correct=FALSE/TRUE)`, `fisher.test`, `quantile`, and direct divisions/variance arithmetic. R was auxiliary calculation, not candidate discovery or classification. All links below refer to PDF physical pages, not printed journal page numbers.

## C001 — Main difficult-weaning percentage

- **Location found / source matched:** REPORT [main p5, Table 1 HF column](../../../jama_thille_2019_oi_190108.pdf#page=5): header n=302, difficult weaning 92 (31); neighboring categories 203 (67), 7 (2).
- **Comparator matched / rule applicable / calculation reproduced:** The same-column header is the denominator; 100×92/302=30.463576%, ordinarily rounding to 30%, not 31%. Counts sum 302; displayed percentages sum 100; independently rounded percentages sum 99. The independent-rounding diagnostic is applicable only if that convention is intended.
- **Necessary inputs / exact missing definitions / alternative:** Count and header are available; percentage-allocation convention is absent. Sum-preserving categorical allocation reproduces 67/31/2 and is a source-grounded alternative, not a demonstrated production rule.
- **Observation versus inference:** The tuple is directly printed; division is arithmetic; intentional balancing is inferred.
- **Classification:** Denominator, proportion, or total inconsistency; both locations REPORT; primary S_W; all S_W; domain statistical_results. Confirmed, no correction.
- **Evidence state / determining fact:** `recorded_candidate`: the registered conditional independent-rounding difference is reproduced; categorical allocation remains a named unresolved definition.
- **Exact human question:** Were category percentages independently rounded or adjusted to total 100%, and what convention explains 92/302 as 31%?

## C002 — Main day90 mortality percentage

- **Location found / source matched:** REPORT [main p8, Table 2 mortality at day90](../../../jama_thille_2019_oi_190108.pdf#page=8): HF n=302, 65 (21).
- **Comparator matched / rule applicable / calculation reproduced:** 100×65/302=21.523179%, ordinarily rounding to 22%. The same page's patients meeting reintubation criteria row prints 65 (22) under the identical header, confirming a different displayed percentage for the same ratio.
- **Necessary inputs / exact missing definitions / alternative:** Both tuples and header are available; row-specific percentage estimator/rounding convention is absent. Truncation gives 21; a survival summary would require a different declared definition from the No. (%) row.
- **Observation versus inference:** Different percentages for identical count/header are direct; identifying which production convention generated 21 is inference.
- **Classification:** Denominator, proportion, or total inconsistency; both REPORT within Table 2; primary/all S_W; domain statistical_results. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: both the arithmetic diagnostic and directly differing 65/302 displays reproduce.
- **Exact human question:** Why is 65/302 shown as 21% here and 22% elsewhere on the same table, and which mortality percentage definition was intended?

## C003 — Nonhypercapnic difficult-weaning percentage

- **Location found / source matched:** REPORT [results p3, eTable 2 nonhypercapnic HF column](../../../joi190108supp2_prod.pdf#page=3): n=254; difficult 70 (27); simple 177 (70), prolonged 7 (3).
- **Comparator matched / rule applicable / calculation reproduced:** 100×70/254=27.559055%, ordinarily 28%. Categories sum 254; displayed percentages 70+27+3=100; ordinary independent rounding gives 101.
- **Necessary inputs / exact missing definitions / alternative:** All counts/header are available; category-balancing convention is absent. Reducing an independently rounded category by one percentage point reconciles the displayed total.
- **Observation versus inference:** Printed ratio/percentage direct; independent rounding diagnostic derived; intentional balancing unconfirmed.
- **Classification:** Denominator, proportion, or total inconsistency; both REPORT; primary/all S_W; domain statistical_results. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: registered conditional rounding difference reproduces, with a concrete sum-preserving alternative.
- **Exact human question:** Is 27% the deliberate balancing allocation for this category, or which denominator/rounding rule should accompany 70 patients?

## C004 — Nonhypercapnic prolonged-weaning percentage

- **Location found / source matched:** REPORT [results p3, eTable 2 nonhypercapnic NIV column](../../../joi190108supp2_prod.pdf#page=3): n=276; prolonged 12 (5); simple 194 (70), difficult 70 (25).
- **Comparator matched / rule applicable / calculation reproduced:** 100×12/276=4.347826%, ordinarily 4%. Categories sum 276; displayed percentages 70+25+5=100, independently rounded values sum 99. Standard largest-remainder allocation would favor the difficult category, so balancing is possible but its rule is not established.
- **Necessary inputs / exact missing definitions / alternative:** Counts/header available; actual allocation rule absent. A manually balanced distribution can produce the printed whole percentages.
- **Observation versus inference:** Printed tuple direct; division derived; balancing mechanism inferred.
- **Classification:** Denominator, proportion, or total inconsistency; both REPORT; primary/all S_W; domain statistical_results. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: ordinary-rounding discrepancy remains conditional on an unnamed percentage-allocation convention.
- **Exact human question:** Which percentage-allocation rule gives prolonged weaning 5% from 12/276?

## C005 — Hypercapnic HF ineffective-cough percentage

- **Location found / source matched:** REPORT [results p4, eTable 2 hypercapnic HF ineffective cough](../../../joi190108supp2_prod.pdf#page=4), visually confirmed: 14/45 (69), row No./total No. (%).
- **Comparator matched / rule applicable / calculation reproduced:** 100×14/45=31.111111%, ordinarily 31%. The complement 31/45=68.888889%, ordinarily 69%. Nonhypercapnic same-row 51/239 (21) follows numerator/denominator convention.
- **Necessary inputs / exact missing definitions / alternative:** Explicit numerator/denominator and label available; no alternative percentage convention declared. Complementary cough category could explain the number while changing what the printed percentage describes.
- **Observation versus inference:** Cell/label are direct; complement arithmetic is reproduced; reversed coding or transcription mechanism is inference.
- **Classification:** Denominator, proportion, or total inconsistency; both REPORT within eTable 2; primary/all S_W; domain statistical_results. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: 69% does not describe the displayed 14/45 numerator and exactly follows the complementary ratio.
- **Exact human question:** Does 69% describe effective cough, or which component of the ineffective-cough cell is intended?

## C006 — Hypercapnic NIV ineffective-cough percentage

- **Location found / source matched:** REPORT [results p4, eTable 2 hypercapnic NIV ineffective cough](../../../joi190108supp2_prod.pdf#page=4), visually confirmed: 16/59 (73).
- **Comparator matched / rule applicable / calculation reproduced:** 100×16/59=27.118644%, ordinarily 27%; complement 43/59=72.881356%, ordinarily 73%. Nonhypercapnic NIV 70/263 (27) follows numerator convention; pooled REPORT main p6 86/322 (27) corroborates 16+70 and 59+263, adding no discrepancy relationship.
- **Necessary inputs / exact missing definitions / alternative:** Explicit fraction and label available; complementary cough classification may explain 73, but no complementary-percent label is supplied.
- **Observation versus inference:** Printed inputs direct; divisions reproduced; production mechanism inferred.
- **Classification:** Denominator, proportion, or total inconsistency; both discrepancy locations REPORT results; primary/all S_W; domain statistical_results. Confirmed; main corroboration does not add S_C.
- **Evidence state / determining fact:** `recorded_candidate`: percentage follows complement rather than explicit numerator.
- **Exact human question:** Is the intended ineffective-cough percentage 16/59 or its complement, and what should the cell label describe?

## C007 — Hypercapnic HF abundant-secretion percentage

- **Location found / source matched:** REPORT [results p4, eTable 2 hypercapnic HF abundant secretions](../../../joi190108supp2_prod.pdf#page=4), visually confirmed: 20/46 (57).
- **Comparator matched / rule applicable / calculation reproduced:** 100×20/46=43.478261%, ordinarily 43%; complement 26/46=56.521739%, ordinarily 57%. Same-row nonhypercapnic 101/242 (42) follows numerator convention; pooled main 121/288 (42) corroborates the counts.
- **Necessary inputs / exact missing definitions / alternative:** Explicit fraction/label available; percentage might intentionally describe absence of abundant secretions, but that label is not printed.
- **Observation versus inference:** Direct cell and label; derived complement identity; possible coding reversal inferred.
- **Classification:** Denominator, proportion, or total inconsistency; discrepancy within REPORT results; primary/all S_W; domain statistical_results. Confirmed, corroborative main does not add a relationship.
- **Evidence state / determining fact:** `recorded_candidate`: printed 57% matches the complement, not 20/46.
- **Exact human question:** Does 57% describe patients without abundant secretions, or which cell component is intended for the labeled outcome?

## C008 — Hypercapnic NIV abundant-secretion percentage

- **Location found / source matched:** REPORT [results p4, eTable 2 hypercapnic NIV abundant secretions](../../../joi190108supp2_prod.pdf#page=4), visually confirmed: 23/61 (62).
- **Comparator matched / rule applicable / calculation reproduced:** 100×23/61=37.704918%, ordinarily 38%; complement 38/61=62.295082%, ordinarily 62%. Same-row nonhypercapnic NIV 91/265 (34) and pooled main 114/326 (35) use numerator convention.
- **Necessary inputs / exact missing definitions / alternative:** Explicit fraction and outcome label available; complementary classification can explain 62 but is not the stated label.
- **Observation versus inference:** Direct cell; reproduced arithmetic; production/coding explanation inferred.
- **Classification:** Denominator, proportion, or total inconsistency; REPORT results locations; primary/all S_W; domain statistical_results. Confirmed; corroboration creates no S_C.
- **Evidence state / determining fact:** `recorded_candidate`: the printed percentage matches the complementary proportion.
- **Exact human question:** Which of the numerator, percentage, or outcome label is intended to describe abundant secretions for these 61 patients?

## C009 — Hypercapnic NIV ICU-reintubation percentage

- **Location found / source matched:** REPORT [results p6, eTable 3 reintubation up until ICU discharge](../../../joi190108supp2_prod.pdf#page=6): NIV n=63, 6 (9); HF 10/48 (21); difference −11.3.
- **Comparator matched / rule applicable / calculation reproduced:** 100×6/63=9.523810%, ordinarily 10%; count-based difference 9.523810−20.833333=−11.309524, rounding to −11.3, supports count/header alignment.
- **Necessary inputs / exact missing definitions / alternative:** Inputs available; percentage rounding convention absent. Plain truncation yields 9 directly, whereas ordinary rounding yields 10.
- **Observation versus inference:** Cell/header direct; arithmetic diagnostic reproduced; intent to truncate inferred.
- **Classification:** Denominator, proportion, or total inconsistency; REPORT; primary/all S_W; domain statistical_results. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: ordinary-rounding difference reproduced; truncation remains a named alternative.
- **Exact human question:** Was 9% intentionally truncated or based on another denominator, and which convention describes 6/63 ICU reintubations?

## C010 — Hypercapnic NIV ICU composite percentage

- **Location found / source matched:** REPORT [results p6, eTable 3 mortality or reintubation in ICU](../../../joi190108supp2_prod.pdf#page=6): NIV n=63, 6 (9); HF 11/48 (23); difference −13.4.
- **Comparator matched / rule applicable / calculation reproduced:** 100×6/63=9.523810%, ordinarily 10%; difference 100×(6/63−11/48)=−13.392857, rounds −13.4.
- **Necessary inputs / exact missing definitions / alternative:** Count/header available; percentage convention absent. Truncation yields 9 and could reconcile display; this is a separate composite outcome, not a duplicate of C009.
- **Observation versus inference:** Cell direct; division reproduced; intentional truncation inferred.
- **Classification:** Denominator, proportion, or total inconsistency; REPORT; primary/all S_W; domain statistical_results. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: conditional rounding discrepancy reproduces for this separate row.
- **Exact human question:** Which rounding or denominator rule produced the composite-event 9% from 6/63?

## C011 — Nonhypercapnic day90 mortality difference

- **Location found / source matched:** REPORT [results p7, eTable 4 mortality at day90](../../../joi190108supp2_prod.pdf#page=7): HF 54 (21), n=254; NIV 50 (18), n=276; difference −3.8 (−9.9 to 3.6).
- **Comparator matched / rule applicable / calculation reproduced:** Unadjusted count difference 100×(50/276−54/254)=−3.143900, ordinarily −3.1. CI midpoint −3.15 supports this diagnostic but is not proof of the interval construction. One-decimal component rounding yields 18.1−21.3=−3.2, also not −3.8.
- **Necessary inputs / exact missing definitions / alternative:** Counts/headers/difference available; exact difference estimator absent. An adjusted or separately defined estimate could differ, but none is labeled for this row.
- **Observation versus inference:** Direct printed effect and inputs; count arithmetic reproduced; transcription mechanism inferred.
- **Classification:** Numeric or arithmetic inconsistency; REPORT; primary/all S_W; domain statistical_results. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: displayed −3.8 does not reconcile with the displayed count contrast under the ordinary absolute-difference interpretation.
- **Exact human question:** Which estimator or population produces −3.8, or which printed contrast was intended for the 54/254 versus 50/276 mortality result?

## C012 — Conditional mortality among reintubated difference

- **Location found / source matched:** REPORT [results p7, eTable 4 mortality in ICU of reintubated patients](../../../joi190108supp2_prod.pdf#page=7): HF 17/49 (35), NIV 9/35 (26); difference −8.9 (−27.1 to 11.2).
- **Comparator matched / rule applicable / calculation reproduced:** 100×(9/35−17/49)=−8.979592, ordinarily −9.0. One-decimal component rounding 25.7−34.7 also gives −9.0. Truncation toward zero gives −8.9.
- **Necessary inputs / exact missing definitions / alternative:** Explicit conditional denominators and contrast available; estimator/truncation convention absent. A separately estimated effect or truncation could explain the displayed value.
- **Observation versus inference:** Printed inputs direct; ordinary/truncated diagnostics reproduced; explanation unconfirmed.
- **Classification:** Numeric or arithmetic inconsistency; REPORT; primary/all S_W; domain statistical_results. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: registered conditional precision discrepancy reproduces pending exact convention.
- **Exact human question:** Is −8.9 intentionally truncated or separately estimated, and what calculation rule should link it to 17/49 and 9/35?

## C013 — Composite difference and two-stage rounding

- **Location found / source matched:** REPORT [main p8, Table 2 mortality or reintubation in ICU](../../../jama_thille_2019_oi_190108.pdf#page=8), visually confirmed: HF64/302 (21), NIV51/339 (15), difference −6.2 (−12.2 to −0.2).
- **Comparator matched / rule applicable / calculation reproduced:** Exact difference is −6.147805, ordinary one-step −6.1. However, component risks rounded to one decimal are 21.2 and 15.0, whose difference is exactly −6.2. Thus printed count ratios and displayed contrast admit an explicit coherent rounding path.
- **Necessary inputs / exact missing definitions / alternative:** All numeric inputs available; rounding-stage convention absent. Two-stage rounding reconciles the registered numeric display without another population or model.
- **Observation versus inference:** Values and coherent arithmetic directly reproducible; whether production actually used two stages is inference.
- **Classification:** Numeric or arithmetic inconsistency; REPORT; primary/all S_W; domain statistical_results. Registration classification preserved; no newly established discrepancy relationship.
- **Evidence state / determining fact:** `not_reproduced`: the implied unavoidable arithmetic mismatch is disproven by exact reproduction of −6.2 using rounded component percentages. The one-step diagnostic remains true but is not the only coherent computation.
- **Exact human question:** Was two-stage component rounding intended, and should the reporting convention specify one or two rounding stages?

## C014 — Respiratory-failure effect across main locations

- **Location found / source matched:** REPORT [main p1 abstract](../../../jama_thille_2019_oi_190108.pdf#page=1) and [p6 Secondary Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=6): −8.7%, CI −15.2 to −1.8, P=.01. REPORT [p8 Table 2](../../../jama_thille_2019_oi_190108.pdf#page=8): −8.5, same CI/P; HF88/302, NIV70/339.
- **Comparator matched / rule applicable / calculation reproduced:** Same day7 respiratory-failure endpoint, arms, population, and inferential tuple. Count contrast is −8.490105296pp, rounding −8.5. Printed effects differ 0.2pp beyond combined 0.1pp one-decimal rounding allowance. Coordinator registration arithmetic repair from the cross-source checker is independently confirmed.
- **Necessary inputs / exact missing definitions / alternative:** Counts and matched results available; no alternative model/population identifies −8.7. An undisclosed estimand could explain it only with an additional definition.
- **Observation versus inference:** Different printed effects direct; count calculation reproduced; production explanation inferred.
- **Classification:** Numeric or arithmetic inconsistency; all REPORT within main; primary/all S_W; domain statistical_results. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: matched report effects visibly differ and count contrast reproduces −8.5.
- **Exact human question:** Which effect estimate or distinct estimand is intended at the three main locations?

## C015 — ICU stay contrast unit

- **Location found / source matched:** REPORT [main p8, Table 2 ICU stay row and shared difference heading](../../../jama_thille_2019_oi_190108.pdf#page=8), visually confirmed: length of stay median (IQR), days; HF11 (7 to19), NIV12 (7 to19); contrast0.5 (−1.6 to2.6), heading Absolute Difference, % (95% CI).
- **Comparator matched / rule applicable / logical comparison reproduced:** Day-scale row and percent-unit contrast heading coexist. An absolute untransformed difference in duration has units days; percent requires a stated normalization. No arithmetic equality with rounded medians is assumed.
- **Necessary inputs / exact missing definitions / alternative:** Row/header available; contrast estimator, scale, and any percent normalization absent. Heading may apply only to binary rows while this contrast is days.
- **Observation versus inference:** Printed unit conflict direct; intended unit inferred.
- **Classification:** Measure, label, or scale inconsistency; REPORT; primary/all S_W; domain report_internal_inconsistency. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: printed heading does not distinguish the continuous day-scale contrast.
- **Exact human question:** What unit and estimator apply to 0.5, and how should the shared percent heading identify this row?

## C016 — Hospital stay contrast unit

- **Location found / source matched:** REPORT [main p8, Table 2 hospital stay row/shared heading](../../../jama_thille_2019_oi_190108.pdf#page=8), visually confirmed: median (IQR), days; HF23 (15 to39), NIV25 (15 to42); contrast2.3 (−1.4 to6.1) under Absolute Difference, % (95% CI).
- **Comparator matched / rule applicable / logical comparison reproduced:** Absolute day-scale contrast and percent heading are dimensionally distinct unless normalization is defined. The value 2.3 is not required to equal the difference between rounded medians.
- **Necessary inputs / exact missing definitions / alternative:** All labels/cells available; estimator and intended contrast unit absent. A generic binary-outcome heading may have been carried onto a duration estimate in days; a percent contrast would need a defined scale.
- **Observation versus inference:** Header/row direct; intended scale inferred.
- **Classification:** Measure, label, or scale inconsistency; REPORT; primary/all S_W; domain report_internal_inconsistency. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: the hospital row shares a percentage-unit contrast heading without a separate definition.
- **Exact human question:** Is 2.3 a day-scale or normalized percent effect, and what estimator/unit should identify it?

## C017 — HF center IQR

- **Location found / source matched:** REPORT [main p6, Table 1 participating centers](../../../jama_thille_2019_oi_190108.pdf#page=6): 30 centers; HF patients per center median(IQR)10 (9–25). REPORT [results p8, eTable 5 HF denominators](../../../joi190108supp2_prod.pdf#page=8), all 30 visually read: 19,16,7,15,6,13,10,5,17,10,11,1,12,11,12,10,12,2,5,25,8,2,19,14,3,10,4,14,2,7.
- **Comparator matched / rule applicable / calculation reproduced:** Denominators sum302. Median10; linear Q1/Q3=5.25/13.75; median-of-halves5/14; maximum25. Ordinary sample quartiles cannot yield9/25 from the full supplied vector.
- **Necessary inputs / exact missing definitions / alternative:** Complete matching vector available; exact quartile convention/alternative population absent. Another population/statistic could differ but is not labeled.
- **Observation versus inference:** Center fractions/main summary direct; quantiles derived; different-set explanation inferred.
- **Classification:** Cross-document numeric inconsistency; both REPORT in separate documents; primary/all S_C; domain report_internal_inconsistency. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: complete302-patient center vector fails to reproduce printed IQR under ordinary quantiles.
- **Exact human question:** Which center population and dispersion definition generate9–25?

## C018 — NIV center IQR

- **Location found / source matched:** REPORT [main p6 Table 1](../../../jama_thille_2019_oi_190108.pdf#page=6): 30 centers; NIV13 (9–23). REPORT [results p8 eTable 5 NIV denominators](../../../joi190108supp2_prod.pdf#page=8), all visually read: 19,16,7,17,7,14,13,7,17,12,13,2,13,13,12,13,13,5,6,23,9,4,21,17,3,11,5,16,2,9.
- **Comparator matched / rule applicable / calculation reproduced:** Sum339; median12.5 coherently rounds13; linear Q1/Q3=7/15.5; median-of-halves7/16; maximum23. Neither ordinary quantile choice nor rounding produces9/23.
- **Necessary inputs / exact missing definitions / alternative:** Complete matching vector available; alternative population/statistic/quantile definition absent. Full range would be2–23, not9–23.
- **Observation versus inference:** Printed vector/summary direct; summary arithmetic derived; alternative study subset unconfirmed.
- **Classification:** Cross-document numeric inconsistency; REPORT versus separate REPORT; primary/all S_C; domain report_internal_inconsistency. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: complete339-patient vector does not reproduce the printed IQR.
- **Exact human question:** Which population or dispersion statistic underlies9–23?

## C019 — Conditional pooled pre-SBT PaCO2 SD

- **Location found / source matched:** REPORT [main p5, Table 1 pre-SBT NIV PaCO2](../../../jama_thille_2019_oi_190108.pdf#page=5):40 (8), header339. REPORT [results p4 eTable 2](../../../joi190108supp2_prod.pdf#page=4): corresponding NIV strata37 (8), header276, and51 (8), header63. End-SBT REPORT [main p6](../../../jama_thille_2019_oi_190108.pdf#page=6) explicitly gives measured n241 for a different time point.
- **Comparator matched / rule applicable / calculation reproduced:** Labels/time match; actual measured-n partition does not. Substituting headers gives pooled mean39.601770, SD9.672330, lower SD bound9.040442 with rounding allowances, exceeding8.5. Formula requires actual measured n and same observations, which are not supplied for pre-SBT cells.
- **Necessary inputs / exact missing definitions / alternative:** Means/SDs/header totals available; row-specific measured n and observation-set identity absent. Variable-specific missingness can change weights; end-SBT n241 cannot be imported.
- **Observation versus inference:** Moments direct; incompatible pooled SD is conditional on unsupported measurement-n assignment.
- **Classification:** Cross-document numeric inconsistency; REPORT versus REPORT; primary/all S_C; domain report_internal_inconsistency. Confirmed for registered comparison.
- **Evidence state / determining fact:** `record_input_error`: header n was substituted for unreported measured n, so the required partition alignment is unestablished and residual variance question cannot be settled.
- **Exact human question:** What measured n and exact subsets generated each pre-SBT cell, and do they partition the main measured observations?

## C020 — PLAN duration decomposition

- **Location found / source matched:** PLAN [protocol p32 section5.6](../../../joi190108supp1_prod.pdf#page=32): total51months with36months for study and12analysis; participation3months, recruitment36months. PLAN [p11 synopsis](../../../joi190108supp1_prod.pdf#page=11): total51,39study,12analysis; inclusion36, participation3.
- **Comparator matched / rule applicable / calculation reproduced:** p32 expressed two-part decomposition36+12=48, not51; p11 decomposition39+12=51. Shared total matches; stated study component differs3months.
- **Necessary inputs / exact missing definitions / alternative:** Components available; whether p32study means recruitment only is undefined. Inclusion36+follow-up3+analysis12=51 is coherent but p32 describes its36as study component while synopsis uses39.
- **Observation versus inference:** Different component descriptions and sum direct; omitted follow-up accounting inferred.
- **Classification:** Numeric or arithmetic inconsistency; both prospective PLAN content in one protocol bundle; primary/all P_P; domain plan_material. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: the printed decomposition and study-duration components differ; a coherent follow-up explanation does not remove those printed differences.
- **Exact human question:** Is p32study36 intended to mean recruitment only, and how should the51month decomposition include follow-up?

## C021 — Reintubation acidosis threshold

- **Location found / source matched:** REPORT [main p4 Outcomes severe respiratory failure](../../../jama_thille_2019_oi_190108.pdf#page=4): pH<7.25 with PaCO2>45. PLAN [protocol pp30–31 section5.4](../../../joi190108supp1_prod.pdf#page=31): severe reintubation criterion pH<7.35 with PaCO2>45; antecedent severe-failure framing is onp30. Ordinary nonsevere respiratory-failure threshold7.35 is separately defined.
- **Comparator matched / rule applicable / logical comparison reproduced:** Both refer to severe respiratory failure leading to reintubation with at least two criteria. Threshold difference0.10; illustrative pH7.30/PaCO2>45 meets PLAN acidosis criterion but not REPORT criterion, with no patient event imputed.
- **Necessary inputs / exact missing definitions / alternative:** Criteria available; implementation history/amendment and actual criterion-count generation absent. An amended stricter threshold may explain difference.
- **Observation versus inference:** Different cutoffs direct; impact on actual patients/counts cannot be inferred.
- **Classification:** Measure, label, or scale inconsistency; REPORT versus prospective PLAN; primary/all P_R; domain protocol_report. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: matched cutoff definitions directly differ.
- **Exact human question:** Which threshold generated reported criteria counts, and was the7.25definition documented as a change?

## C022 — PLAN historical Su sample size

- **Location found / source matched:** PLAN [protocol p15 historical trial paragraph](../../../joi190108supp1_prod.pdf#page=15): largest multicenter trial included400patients; reference[21]. PLAN [p17 Table1 Su2012 row](../../../joi190108supp1_prod.pdf#page=17): same reference; NIVn202, O2n204.
- **Comparator matched / rule applicable / calculation reproduced:**202+204=406,6more than400. Both identify the same historical trial. Exact counts disagree; rounding406 to two significant figures gives400 and can explain the narrative if intended as approximate.
- **Necessary inputs / exact missing definitions / alternative:** Both printed counts available; narrative precision/population distinction absent. Broad background approximation is plausible; no separate included/randomized population is given.
- **Observation versus inference:** Values direct; sum reproduced; intentional approximation inferred.
- **Classification:** Numeric or arithmetic inconsistency; both PLAN historical/background content, despite reporting a prior study; primary/all P_P; domain plan_material. Confirmed by content.
- **Evidence state / determining fact:** `recorded_candidate`: conditional exact-count difference reproduces; intended background rounding remains a named definition.
- **Exact human question:** Is400a deliberately rounded description of406or a different trial population?

## C023 — PLAN readiness oxygenation boundaries

- **Location found / source matched:** PLAN [protocol p27 weaning procedure](../../../joi190108supp1_prod.pdf#page=27): SpO2>90% on FiO2≤40% or PaO2/FiO2≥150, PEEPup to8. PLAN [p42 Appendix2 readiness worksheet](../../../joi190108supp1_prod.pdf#page=42), visually confirmed: SpO2≥92%, FiO2≤40%, PEEP≤8.
- **Comparator matched / rule applicable / logical comparison reproduced:** Both concern readiness for a spontaneous breathing/weaning test; example SpO2=91%with other conditions held equal passes text saturation threshold but fails worksheet threshold. p27 explicitly allows usual center procedures and proposes this local worksheet where no protocol exists.
- **Necessary inputs / exact missing definitions / alternative:** Thresholds and implementation framing available; whether worksheet intentionally tightens general criterion is undefined. A stricter local implementation is coherent and permitted by differing center practices; comparison concerns printed numeric boundaries, not assumed eligibility counts.
- **Observation versus inference:** Differing boundaries direct; unintended inconsistency or actual recruitment effect inferred and unestablished.
- **Classification:** Measure, label, or scale inconsistency; both prospective PLAN; primary/all P_P; domain plan_material. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: registered threshold difference remains observable; intended relation between general and local criterion is unresolved.
- **Exact human question:** Is≥92%a deliberate local implementation of>90%, and which criterion should readers associate with the study?

## C024 — Survival time-axis origin

- **Location found / source matched:** REPORT [results p9 eFigure](../../../joi190108supp2_prod.pdf#page=9), visually confirmed: title survival From Extubation to Day90; x-axis Days Since Intubation; ticks0–90, initial risk302/339. REPORT p1contents repeats extubation title as corroboration.
- **Comparator matched / rule applicable / logical comparison reproduced:** One plotted x-axis has two differently named origins without an origin transformation. Different words are direct; no event-time reconstruction is possible.
- **Necessary inputs / exact missing definitions / alternative:** Labels available; actual time variable, origin translation, and event-time data absent. Axis may be stale, or title may describe an intended endpoint different from plotted origin.
- **Observation versus inference:** Labels direct; which is erroneous inferred. No exact effect is read from curve pixels.
- **Classification:** Measure, label, or scale inconsistency; both REPORT in the same results document; primary/all S_W; domain report_internal_inconsistency. Confirmed; main methods merely corroborate extubation framing.
- **Evidence state / determining fact:** `recorded_candidate`: title and x-axis directly name different time origins.
- **Exact human question:** Does the plotted curve use intubation or extubation as time zero, and which label should identify that variable?

## C025 — Respiratory-failure P across REPORT documents

- **Location found / source matched:** REPORT [main p8 Table2](../../../jama_thille_2019_oi_190108.pdf#page=8):88/302 versus70/339, day7 respiratory failure, P=.01. REPORT [results p2 eTable1](../../../joi190108supp2_prod.pdf#page=2): identical outcome/counts/headers, P=.02. Mainpp1/6 repeat .01; REPORT [main p4 methods](../../../jama_thille_2019_oi_190108.pdf#page=4) says chi-square for this outcome.
- **Comparator matched / rule applicable / calculation reproduced:** Printed P differs at identical two-decimal precision. Standard uncorrected Pearson P=.0127859 rounds.01; continuity-corrected chi-square P=.0164904 rounds.02. Thus coherent distinct chi-square conventions can reproduce both numbers; no common convention is established.
- **Necessary inputs / exact missing definitions / alternative:** Counts and method family available; supplement exact test/correction rule absent. Different chi-square variants are a concrete source-compatible explanation.
- **Observation versus inference:** Distinct printed P direct; same-test conflict is conditional, not established inferential arithmetic error.
- **Classification:** Statistical reporting inconsistency; REPORT versus distinct REPORT; primary/all S_C; domain statistical_results. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: matched displayed P differs, pending named test convention; supported different-test alternative must remain on the card.
- **Exact human question:** Were the two rows intended to use the same chi-square convention, or should their tests/corrections be distinguished?

## C026 — Nonhypercapnic day7 P precision

- **Location found / source matched:** REPORT [main p7 subgroup paragraph](../../../jama_thille_2019_oi_190108.pdf#page=7):530patients,13%versus18%, difference−5.0, CI−11.2to1.1, P=.10. REPORT [results p7 eTable4](../../../joi190108supp2_prod.pdf#page=7):HF45/254, NIV35/276; same effect/CI, P=.1057.
- **Comparator matched / rule applicable / calculation reproduced:** Same day7 endpoint and subgroup. Four-decimal bin[.10565,.10575) rounds.11to two decimals; .10bin[.095,.105) does not overlap. Truncation to two decimals gives.10; unknown alternative test could also differ. Main Figure3B log-rank.11is explicitly a different time-to-event output, not substituted comparator.
- **Necessary inputs / exact missing definitions / alternative:** Matched tuples available; prose rounding/truncation and exact P-producing test absent.
- **Observation versus inference:** Printed precision difference direct; ordinary nearest-rounding mismatch reproduced; intent to truncate inferred.
- **Classification:** Statistical reporting inconsistency; REPORT versus REPORT; primary/all S_C; domain statistical_results. Confirmed.
- **Evidence state / determining fact:** `recorded_candidate`: ordinary nearest rounding cannot reconcile the matched printed P values, pending exact convention.
- **Exact human question:** Was prose.10truncated from.1057or calculated using a different test?

## C027 — Prespecified secondary-outcome count

- **Location found / source matched:** REPORT [main p1 abstract](../../../jama_thille_2019_oi_190108.pdf#page=1):11prespecified secondary outcomes. REPORT [p4 Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=4) expands3reintubation times, respiratory failure, treatment continuation,2stays,4mortality times. PLAN [protocol p25 section3.5](../../../joi190108supp1_prod.pdf#page=25) additionally includes ventilatory-support-free days during14days, counting intubation/NIV/HFNC.
- **Comparator matched / rule applicable / calculation reproduced:** REPORT expansion3+1+1+2+4=11; same PLAN expansion adds1=12. This is the concrete prespecified-count framing, not a claim about motives or raw outcomes.
- **Necessary inputs / exact missing definitions / alternative:** Lists/count available; amendment history and whether abstract means only reported planned outcomes absent. A reported subset or approved removal could explain11.
- **Observation versus inference:** Lists/count direct; omission from printed REPORT list demonstrated; intentional selective reporting cannot be inferred.
- **Classification:** Denominator, proportion, or total inconsistency; REPORT versus prospective PLAN; primary/all P_R; domain protocol_report. Confirmed; synopsis only corroborates PLAN.
- **Evidence state / determining fact:** `recorded_candidate`: supplied lists expand to11versus12under the same counting rule.
- **Exact human question:** What counting basis or documented amendment explains11prespecified outcomes and the14day support-free endpoint?

## C028 — Day90 mortality P and survival log-rank P

- **Location found / source matched:** REPORT [main p8 Table2](../../../jama_thille_2019_oi_190108.pdf#page=8):65/302versus62/339, day90 mortality, P=.30. REPORT [main p4 methods](../../../jama_thille_2019_oi_190108.pdf#page=4) specifically assigns log-rank to Kaplan–Meier extubation-to-death curves; REPORT [results p9 eFigure](../../../joi190108supp2_prod.pdf#page=9), visually confirmed, explicitly labels log-rank P=.37and title day90 survival, with the origin-label conflict separately retained as C024.
- **Comparator matched / rule applicable / calculation reproduced:** Same nominal horizon/population, but table fixed-time count contrast and curve time-to-event test are different statistical objects. Equality requires a common test/event-time/censoring definition not supplied for Table2. Raw count Pearson P=.305165, Yates.354363, Fisher.321906cannot reconstruct log-rank; no event-time data are supplied.
- **Necessary inputs / exact missing definitions / alternative:** Counts/labels available; table exact test, actual curve origin, event times/censoring unavailable. Distinct fixed-time and log-rank analyses need not agree.
- **Observation versus inference:** Different P direct; treating them as one result/test is unsupported alignment.
- **Classification:** Statistical reporting inconsistency; registered locations REPORT versus REPORT; primary/all S_C; domain statistical_results. Confirmed for the registered comparison.
- **Evidence state / determining fact:** `record_input_error`: registered equality depends on an unestablished common-test/time-origin alignment; supplied log-rank attribution describes curves, not an explicit Table 2 test.
- **Exact human question:** Which test generated Table 2 day90 P, and was it meant to match the survival curve with which origin and censoring definition?

## C029 — PLAN PaO2 expansion

- **Location found / source matched:** PLAN [protocol p7 abbreviations](../../../joi190108supp1_prod.pdf#page=7), visually confirmed: PaO2 Partial Pressure of Dioxide; adjacent PaCO2 Partial Pressure of Carbon Dioxide. REPORT [main p6 Table1 abbreviations](../../../jama_thille_2019_oi_190108.pdf#page=6): PaO2 partial pressure of arterial oxygen.
- **Comparator matched / rule applicable / logical comparison reproduced:** Same measurement symbol labels physiological quantitative cells and oxygenation ratios; supplied full expansions differ. Dioxide is incomplete as a gas identification relative to explicit arterial oxygen; no gas-value error follows from wording alone.
- **Necessary inputs / exact missing definitions / alternative:** Exact expansions available; intended English wording absent. Translation or omission may explain PLAN text.
- **Observation versus inference:** Printed wording difference direct; error mechanism and any effect on measured values inferred and unestablished.
- **Classification:** Measure, label, or scale inconsistency; prospective PLAN versus REPORT; primary/all P_R; domain protocol_report. Confirmed; PLAN quantitative usage corroborates meaning without another P_Pdiscrepancy.
- **Evidence state / determining fact:** `recorded_candidate`: exact-source expansion differs from explicitly named report oxygen measure.
- **Exact human question:** What full gas definition was intended for PLAN PaO2, and is the discrepancy confined to abbreviation wording?

## C030 — PLAN FiO2 expansion

- **Location found / source matched:** PLAN [protocol p7 abbreviations](../../../joi190108supp1_prod.pdf#page=7), visually confirmed exact spelling: FiO2 Dioxyde Fraction. The next line says SpO2 Dioxygene saturation. REPORT [main p4 Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=4) defines fraction of inspired oxygen in PaO2:FIO2; REPORT [p6 abbreviations](../../../jama_thille_2019_oi_190108.pdf#page=6) repeats inspired-oxygen fraction.
- **Comparator matched / rule applicable / logical comparison reproduced:** Same quantitative denominator symbol, but PLAN wording names dioxyde and omits inspired qualification, while REPORT explicitly names oxygen. Nearby dioxygene wording supplies a plausible transcription/translation explanation; it does not establish another substantive discrepancy relationship.
- **Necessary inputs / exact missing definitions / alternative:** Exact printed spellings available; intended translation and actual data-field wording absent. A typo for an oxygen fraction is plausible; actual numeric values are not challenged.
- **Observation versus inference:** Printed expansion direct; intended oxygen meaning/cause inferred.
- **Classification:** Measure, label, or scale inconsistency; PLAN versus REPORT; primary/all P_R; domain protocol_report. Confirmed; no role correction.
- **Evidence state / determining fact:** `recorded_candidate`: supplied labels differ for the same quantitative fraction symbol.
- **Exact human question:** Was Dioxyde intended as an oxygen-fraction label, and is only abbreviation wording affected?

## C031 — ICU-mortality P diagnostic

- **Location found / source matched:** REPORT [main p8 Table2 ICU mortality](../../../jama_thille_2019_oi_190108.pdf#page=8), visually confirmed:HF26/302,NIV21/339,P=.25; REPORT [p1 abstract](../../../jama_thille_2019_oi_190108.pdf#page=1) repeats.25. REPORT [p4 methods](../../../jama_thille_2019_oi_190108.pdf#page=4) specifies chi-square for ICU mortality and two-tailed inference.
- **Comparator matched / rule applicable / calculation reproduced:** Standard uncorrected Pearson χ²=1.370452597, P=.241734136 rounds .24; likelihood-ratio P=.242123765 also rounds .24; continuity-corrected P=.308257873 rounds .31; Fisher .288309354 rounds .29 is another diagnostic, not the specified chi-square. Registered standard-test diagnostic reproduces; .25bin[.245,.255) excludes these values. Exact adjusted/stratified chi-square cannot be reconstructed without its inputs.
- **Necessary inputs / exact missing definitions / alternative:** Printed counts/family available; exact test statistic, chi-square convention, any row-specific nonmissing denominator or adjustment absent. An explicitly defined alternative chi-square could differ; absence alone does not prove incorrect inference.
- **Observation versus inference:** Printed tuple direct; standard-test difference conditional diagnostic; production mechanism unestablished.
- **Classification:** Statistical reporting inconsistency; REPORT within main; primary/all S_W; domain statistical_results. Confirmed; PLAN corroboration adds no relationship.
- **Evidence state / determining fact:** `recorded_candidate`: specified test-family/count diagnostic remains as registered pending the named exact test/denominator definition, without declaring a proven numerical contradiction.
- **Exact human question:** Which chi-square statistic, denominators, and adjustment generated.25for26/302versus21/339?

## C032 — Nonhypercapnic ICU-mortality P diagnostic

- **Location found / source matched:** REPORT [results p7 eTable4 ICU mortality](../../../joi190108supp2_prod.pdf#page=7):HF21/254,NIV19/276,P=.5548,difference−1.4,CI−6.1to3.2. REPORT [main p4 methods](../../../jama_thille_2019_oi_190108.pdf#page=4) supplies general ICU mortality chi-square family and subgroup analysis; it is corroborative rather than a discrepant result.
- **Comparator matched / rule applicable / calculation reproduced:** Uncorrected Pearson χ²=.362927994, P=.546884582; likelihood-ratio P=.547092106; Yates .661493369; Fisher .622413761. None is in.5548four-decimal bin[.55475,.55485). These are diagnostics under explicit unadjusted header-denominator assumptions; compatible exact subgroup test variant is not identified. CI is ordered/contains estimate/crosses0and is not independently challenged.
- **Necessary inputs / exact missing definitions / alternative:** Counts/header/family available; exact subgroup test statistic/correction/adjustment and nonmissing denominators absent. A separately specified subgroup/stratified calculation could differ, but its inputs are unavailable.
- **Observation versus inference:** Printed tuple direct; standard-test mismatch reproduced conditionally; same precise inferential convention cannot be inferred from general methods.
- **Classification:** Statistical reporting inconsistency; discrepancy REPORT within results; primary/all S_W; domain statistical_results. Confirmed; main corroboration does not add S_C.
- **Evidence state / determining fact:** `recorded_candidate`: registered conditional standard-family diagnostic reproduces pending exact subgroup test/denominator definition; incomplete specifications are not treated as a proven numeric contradiction.
- **Exact human question:** Which exact test and denominators generated.5548for21/254versus19/276?

## Completion and classification confirmation

All 32 assigned IDs were individually checked. Location found, source value/text, comparator, rule applicability, calculation/logical comparison, available inputs, missing definitions, alternative interpretation, direct-versus-inferred distinction, classification, evidence state, determining fact, and remaining human question appear in each card. All registered roles, primary relationship types, all relationships, primary categories, and mechanically derived domains are confirmed. No PLAN corroboration was elevated to a discrepancy relationship. Evidence-state changes concern C013/C019/C028 as specified below; all other registered conditional or direct observations remain recorded_candidate. No assigned ID was removed or renumbered. No severity or human adjudication was assigned.

| ID | Evidence state | Primary relationship | All relationships | Confirmed primary category | Domain |
|---|---|---|---|---|---|
| C001 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C002 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C003 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C004 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C005 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C006 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C007 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C008 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C009 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C010 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C011 | recorded_candidate | S_W | S_W | Numeric or arithmetic inconsistency | statistical_results |
| C012 | recorded_candidate | S_W | S_W | Numeric or arithmetic inconsistency | statistical_results |
| C013 | not_reproduced | S_W | S_W | Numeric or arithmetic inconsistency | statistical_results |
| C014 | recorded_candidate | S_W | S_W | Numeric or arithmetic inconsistency | statistical_results |
| C015 | recorded_candidate | S_W | S_W | Measure, label, or scale inconsistency | report_internal_inconsistency |
| C016 | recorded_candidate | S_W | S_W | Measure, label, or scale inconsistency | report_internal_inconsistency |
| C017 | recorded_candidate | S_C | S_C | Cross-document numeric inconsistency | report_internal_inconsistency |
| C018 | recorded_candidate | S_C | S_C | Cross-document numeric inconsistency | report_internal_inconsistency |
| C019 | record_input_error | S_C | S_C | Cross-document numeric inconsistency | report_internal_inconsistency |
| C020 | recorded_candidate | P_P | P_P | Numeric or arithmetic inconsistency | plan_material |
| C021 | recorded_candidate | P_R | P_R | Measure, label, or scale inconsistency | protocol_report |
| C022 | recorded_candidate | P_P | P_P | Numeric or arithmetic inconsistency | plan_material |
| C023 | recorded_candidate | P_P | P_P | Measure, label, or scale inconsistency | plan_material |
| C024 | recorded_candidate | S_W | S_W | Measure, label, or scale inconsistency | report_internal_inconsistency |
| C025 | recorded_candidate | S_C | S_C | Statistical reporting inconsistency | statistical_results |
| C026 | recorded_candidate | S_C | S_C | Statistical reporting inconsistency | statistical_results |
| C027 | recorded_candidate | P_R | P_R | Denominator, proportion, or total inconsistency | protocol_report |
| C028 | record_input_error | S_C | S_C | Statistical reporting inconsistency | statistical_results |
| C029 | recorded_candidate | P_R | P_R | Measure, label, or scale inconsistency | protocol_report |
| C030 | recorded_candidate | P_R | P_R | Measure, label, or scale inconsistency | protocol_report |
| C031 | recorded_candidate | S_W | S_W | Statistical reporting inconsistency | statistical_results |
| C032 | recorded_candidate | S_W | S_W | Statistical reporting inconsistency | statistical_results |

Evidence-state totals: recorded_candidate 29; not_reproduced 1; record_input_error 2; repaired_residual 0. No source-access or extraction limitation prevents checking an assigned printed location. Remaining limitations are definition/input limitations named individually, especially actual measured-n partition for C019, table-versus-curve inferential alignment for C028, exact mortality test conventions for C031/C032, and rounding/allocation conventions for the small precision records. Source spelling is preserved in quotations; surrounding analysis is English.
