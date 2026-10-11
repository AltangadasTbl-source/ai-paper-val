# Workflow 1.6 Mechanical Evidence Recheck

Pending Human Adjudication. Complete assigned scope: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018. This artifact records mechanical source facts and classification confirmation, without dispositions or adjudications. Runtime agent: 01a1288e-8403-7051-b0a2-9dde819d0e0a.

## Source authority and method

Read QUALITY_CONTROL_SCOPE.md, PERFORMANCE_PROFILE.md, workflow_1_6/review_contract.md, workflow_1_6/report_spec.md, workflow_1_6/settings.toml, current tooling_record.md, source_inventory.md, and the complete current candidate_ledger.md. Current native/layout assets were locators. Final printed-value confirmation used visually inspected fresh renders made directly from the supplied PDFs with CPU-only Poppler 26.01.0. No OCR, GPU, Python extraction, source modification, reused-artifact modification, or external source was used.

The fresh derivatives are below review_1_6/preprocessing/recheck/. Engine for every PNG: direct pdftoppm (Poppler 26.01.0), 130 dpi. Engine for every TXT: direct pdftotext -layout (Poppler 26.01.0). Exact executed command templates (N substituted by the enumerated page numbers below):

```bash
pdftoppm -f N -l N -singlefile -r 130 -png jama_aminian_2019_oi_190103.pdf .ai_paper_validation/review_1_6/preprocessing/recheck/main-pN
pdftotext -layout -f N -l N jama_aminian_2019_oi_190103.pdf .ai_paper_validation/review_1_6/preprocessing/recheck/main-pN-layout.txt
pdftoppm -f N -l N -singlefile -r 130 -png joi190103supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/recheck/supp1-pN
pdftotext -layout -f N -l N joi190103supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/recheck/supp1-pN-layout.txt
pdftoppm -f N -l N -singlefile -r 130 -png joi190103supp2_prod.pdf .ai_paper_validation/review_1_6/preprocessing/recheck/plan-pN
pdftotext -layout -f N -l N joi190103supp2_prod.pdf .ai_paper_validation/review_1_6/preprocessing/recheck/plan-pN-layout.txt
```

| Source | Exact pages | Derivatives and visual confirmation |
|---|---|---|
| jama_aminian_2019_oi_190103.pdf | 2, 3, 4, 5, 6, 7, 9 | Each main-pN.png and main-pN-layout.txt; every PNG visually inspected |
| joi190103supp1_prod.pdf | 1, 5, 6, 10, 14, 17, 18, 19 | Each supp1-pN.png and supp1-pN-layout.txt; every PNG visually inspected |
| joi190103supp2_prod.pdf | 2, 3, 4, 6 | Each plan-pN.png and plan-pN-layout.txt; every PNG visually inspected |

Additional direct native-layout locators were produced with `pdftotext -layout SOURCE OUTPUT` for each entire supplied PDF, outputs main-all-layout.txt, supp1-all-layout.txt, and plan-all-layout.txt in that same directory. These were searched for medication-sample definitions, matching-ratio order, rounding/precision definitions, and point-estimation wording; they were not substituted for page visual confirmation. Local JavaScript arithmetic independently reproduced the recorded numerical comparisons.

Content-role confirmation: the main article is an Original Investigation reporting methods/results (REPORT); supplement 1 reports eTables/eFigures and sensitivity results (REPORT); supplement 2 contains a dated prospective study protocol and amendment (PLAN). Roles are assigned from this content. Primary relationship precedence is P_R > P_P > S_C > S_W. No case needs a newly added P_P relationship.

## Recheck state and classification register

| ID | Evidence state | Primary relationship | All relationships | Category confirmed | Review domain |
|---|---|---|---|---|---|
| C001 | recorded_candidate | S_W | S_W | Numeric or arithmetic inconsistency | statistical_results |
| C002 | recorded_candidate | S_W | S_W | Numeric or arithmetic inconsistency | statistical_results |
| C003 | recorded_candidate | S_W | S_W | Numeric or arithmetic inconsistency | statistical_results |
| C004 | recorded_candidate | S_W | S_W | Numeric or arithmetic inconsistency | statistical_results |
| C005 | recorded_candidate | S_W | S_W | Numeric or arithmetic inconsistency | statistical_results |
| C006 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C007 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C008 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C009 | recorded_candidate | S_W | S_W | Measure, label, or scale inconsistency | report_internal_inconsistency |
| C010 | recorded_candidate | S_W | S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C011 | record_input_error | S_C | S_C, S_W | Denominator, proportion, or total inconsistency | statistical_results |
| C012 | recorded_candidate | S_W | S_W | Rate-versus-count inconsistency | statistical_results |
| C013 | recorded_candidate | S_C | S_C | Measure, label, or scale inconsistency | report_internal_inconsistency |
| C014 | recorded_candidate | S_W | S_W | Measure, label, or scale inconsistency | report_internal_inconsistency |
| C015 | recorded_candidate | P_R | P_R | Measure, label, or scale inconsistency | protocol_report |
| C016 | recorded_candidate | S_W | S_W | Measure, label, or scale inconsistency | report_internal_inconsistency |
| C017 | record_input_error | S_W | S_W | Measure, label, or scale inconsistency | report_internal_inconsistency |
| C018 | recorded_candidate | P_R | P_R | Numeric or arithmetic inconsistency | protocol_report |

Sixteen recorded_candidate states and two record_input_error states; no transcription requiring repaired_residual and no direct disproof requiring not_reproduced. Every ID remains present. The two changed provisional states concern unsupported comparator alignment, not source transcription.

## C001 — Heart-failure absolute risk difference

**Location found:** Yes. [Main PDF p. 7, Table 2 heart failure row and footnote a](../../../jama_aminian_2019_oi_190103.pdf#page=7); [main PDF p. 4, Statistical Analysis](../../../jama_aminian_2019_oi_190103.pdf#page=4). Both pages visually inspected directly.

**Source value/text matched:** Yes. The heart failure absolute 8-year risk difference is 12.9% (95% CI 10.4–15.1).

**Comparator matched:** Yes. The same row reports surgical cumulative incidence 6.8% and nonsurgical cumulative incidence 18.9%. Footnote a names the difference as nonsurgical control group minus metabolic surgery. Page 4 describes Kaplan–Meier cumulative incidence and absolute risk differences; bootstrap percentile calculation is specified for the CIs.

**Consistency rule applicable:** Yes for the displayed same-outcome, same-time risk subtraction. It does not equate this risk-difference CI with the adjusted Cox HR CI or P value.

**Calculation or logical comparison reproduced:** 18.9−6.8=12.1 percentage points, compared with 12.9; difference 0.8 percentage points. With three quantities individually rounded to a tenth, combined nearest-tenth uncertainty is at most 0.15 percentage points, below 0.8. This is a displayed point-estimate comparison, not a reconstruction of the fitted model or bootstrap distribution.

**Necessary inputs available:** The two displayed risks, displayed difference, time, outcome, group order, and stated difference rule are available.

**Exact missing inputs or definitions:** Unrounded cumulative incidence values and the precise point-estimation implementation for the ARD, including whether a separately derived point estimate or risk set was used. Bootstrap CIs alone do not define an alternative ARD point estimate.

**Source-grounded alternative interpretation:** The source supplies bootstrap uncertainty estimation and outcome-specific risk sets; a separately generated ARD point estimate could conceivably explain the display, but the source does not state that its point estimate differs from subtraction of the same-row risks. This remains an alternative requiring a definition, not an inferred production process.

**Direct observation versus inferred explanation:** The row values and footnote are direct source observations. Subtraction and the rounding bound are reproduced diagnostics. No numerical replacement, production error mechanism, or effect on conclusions is established.

**Compared document roles:** REPORT main p. 7 Table 2 ARD; REPORT same-page two cumulative incidences and footnote a; REPORT main p. 4 Statistical Analysis. These are reporting content inside one article.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Registered category Numeric or arithmetic inconsistency and domain statistical_results confirmed. All substantive comparators are in one REPORT; no role/type correction or competing precedence relationship.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct source confirms all registered values and the same-row subtraction remains different beyond displayed rounding.

**Exact remaining human question:** Was the heart failure ARD point estimate calculated from the same 8-year Kaplan–Meier risks printed in Table 2, or from a separately defined estimand, risk set, or point-estimation rule; where is that rule documented?

## C002 — Coronary-artery-disease absolute risk difference

**Location found:** Yes. [Main PDF p. 7, Table 2 coronary artery disease row and footnote a](../../../jama_aminian_2019_oi_190103.pdf#page=7); [main PDF p. 4, Statistical Analysis](../../../jama_aminian_2019_oi_190103.pdf#page=4). Both pages visually inspected directly.

**Source value/text matched:** Yes. The coronary artery disease absolute 8-year risk difference is 4.2% (95% CI 1.9–6.8).

**Comparator matched:** Yes. The same row reports surgical cumulative incidence 7.9% and nonsurgical cumulative incidence 11.6%. Footnote a names the difference as nonsurgical control group minus metabolic surgery. Page 4 describes Kaplan–Meier cumulative incidence and absolute risk differences; bootstrap percentile calculation is specified for the CIs.

**Consistency rule applicable:** Yes for the displayed same-outcome, same-time risk subtraction. It does not equate this risk-difference CI with the adjusted Cox HR CI or P value.

**Calculation or logical comparison reproduced:** 11.6−7.9=3.7 percentage points, compared with 4.2; difference 0.5 percentage points. With three quantities individually rounded to a tenth, combined nearest-tenth uncertainty is at most 0.15 percentage points, below 0.5. This is a displayed point-estimate comparison, not a reconstruction of the fitted model or bootstrap distribution.

**Necessary inputs available:** The two displayed risks, displayed difference, time, outcome, group order, and stated difference rule are available.

**Exact missing inputs or definitions:** Unrounded cumulative incidence values and the precise point-estimation implementation for the ARD, including whether a separately derived point estimate or risk set was used. Bootstrap CIs alone do not define an alternative ARD point estimate.

**Source-grounded alternative interpretation:** The source supplies bootstrap uncertainty estimation and outcome-specific risk sets; a separately generated ARD point estimate could conceivably explain the display, but the source does not state that its point estimate differs from subtraction of the same-row risks. This remains an alternative requiring a definition, not an inferred production process.

**Direct observation versus inferred explanation:** The row values and footnote are direct source observations. Subtraction and the rounding bound are reproduced diagnostics. No numerical replacement, production error mechanism, or effect on conclusions is established.

**Compared document roles:** REPORT main p. 7 Table 2 ARD; REPORT same-page two cumulative incidences and footnote a; REPORT main p. 4 Statistical Analysis. These are reporting content inside one article.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Registered category Numeric or arithmetic inconsistency and domain statistical_results confirmed. All substantive comparators are in one REPORT; no role/type correction or competing precedence relationship.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct source confirms all registered values and the same-row subtraction remains different beyond displayed rounding.

**Exact remaining human question:** Was the coronary artery disease ARD point estimate calculated from the same 8-year Kaplan–Meier risks printed in Table 2, or from a separately defined estimand, risk set, or point-estimation rule; where is that rule documented?

## C003 — Cerebrovascular-disease absolute risk difference

**Location found:** Yes. [Main PDF p. 7, Table 2 cerebrovascular disease row and footnote a](../../../jama_aminian_2019_oi_190103.pdf#page=7); [main PDF p. 4, Statistical Analysis](../../../jama_aminian_2019_oi_190103.pdf#page=4). Both pages visually inspected directly.

**Source value/text matched:** Yes. The cerebrovascular disease absolute 8-year risk difference is 1.8% (95% CI −0.03 to 3.4).

**Comparator matched:** Yes. The same row reports surgical cumulative incidence 4.1% and nonsurgical cumulative incidence 5.6%. Footnote a names the difference as nonsurgical control group minus metabolic surgery. Page 4 describes Kaplan–Meier cumulative incidence and absolute risk differences; bootstrap percentile calculation is specified for the CIs.

**Consistency rule applicable:** Yes for the displayed same-outcome, same-time risk subtraction. It does not equate this risk-difference CI with the adjusted Cox HR CI or P value.

**Calculation or logical comparison reproduced:** 5.6−4.1=1.5 percentage points, compared with 1.8; difference 0.3 percentage points. With three quantities individually rounded to a tenth, combined nearest-tenth uncertainty is at most 0.15 percentage points, below 0.3. This is a displayed point-estimate comparison, not a reconstruction of the fitted model or bootstrap distribution.

**Necessary inputs available:** The two displayed risks, displayed difference, time, outcome, group order, and stated difference rule are available.

**Exact missing inputs or definitions:** Unrounded cumulative incidence values and the precise point-estimation implementation for the ARD, including whether a separately derived point estimate or risk set was used. Bootstrap CIs alone do not define an alternative ARD point estimate.

**Source-grounded alternative interpretation:** The source supplies bootstrap uncertainty estimation and outcome-specific risk sets; a separately generated ARD point estimate could conceivably explain the display, but the source does not state that its point estimate differs from subtraction of the same-row risks. This remains an alternative requiring a definition, not an inferred production process.

**Direct observation versus inferred explanation:** The row values and footnote are direct source observations. Subtraction and the rounding bound are reproduced diagnostics. No numerical replacement, production error mechanism, or effect on conclusions is established.

**Compared document roles:** REPORT main p. 7 Table 2 ARD; REPORT same-page two cumulative incidences and footnote a; REPORT main p. 4 Statistical Analysis. These are reporting content inside one article.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Registered category Numeric or arithmetic inconsistency and domain statistical_results confirmed. All substantive comparators are in one REPORT; no role/type correction or competing precedence relationship.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct source confirms all registered values and the same-row subtraction remains different beyond displayed rounding.

**Exact remaining human question:** Was the cerebrovascular disease ARD point estimate calculated from the same 8-year Kaplan–Meier risks printed in Table 2, or from a separately defined estimand, risk set, or point-estimation rule; where is that rule documented?

## C004 — Nephropathy absolute risk difference

**Location found:** Yes. [Main PDF p. 7, Table 2 nephropathy row and footnote a](../../../jama_aminian_2019_oi_190103.pdf#page=7); [main PDF p. 4, Statistical Analysis](../../../jama_aminian_2019_oi_190103.pdf#page=4). Both pages visually inspected directly.

**Source value/text matched:** Yes. The nephropathy absolute 8-year risk difference is 11.1% (95% CI 8.8–13.6).

**Comparator matched:** Yes. The same row reports surgical cumulative incidence 6.1% and nonsurgical cumulative incidence 16.3%. Footnote a names the difference as nonsurgical control group minus metabolic surgery. Page 4 describes Kaplan–Meier cumulative incidence and absolute risk differences; bootstrap percentile calculation is specified for the CIs.

**Consistency rule applicable:** Yes for the displayed same-outcome, same-time risk subtraction. It does not equate this risk-difference CI with the adjusted Cox HR CI or P value.

**Calculation or logical comparison reproduced:** 16.3−6.1=10.2 percentage points, compared with 11.1; difference 0.9 percentage points. With three quantities individually rounded to a tenth, combined nearest-tenth uncertainty is at most 0.15 percentage points, below 0.9. This is a displayed point-estimate comparison, not a reconstruction of the fitted model or bootstrap distribution.

**Necessary inputs available:** The two displayed risks, displayed difference, time, outcome, group order, and stated difference rule are available.

**Exact missing inputs or definitions:** Unrounded cumulative incidence values and the precise point-estimation implementation for the ARD, including whether a separately derived point estimate or risk set was used. Bootstrap CIs alone do not define an alternative ARD point estimate.

**Source-grounded alternative interpretation:** The source supplies bootstrap uncertainty estimation and outcome-specific risk sets; a separately generated ARD point estimate could conceivably explain the display, but the source does not state that its point estimate differs from subtraction of the same-row risks. This remains an alternative requiring a definition, not an inferred production process.

**Direct observation versus inferred explanation:** The row values and footnote are direct source observations. Subtraction and the rounding bound are reproduced diagnostics. No numerical replacement, production error mechanism, or effect on conclusions is established.

**Compared document roles:** REPORT main p. 7 Table 2 ARD; REPORT same-page two cumulative incidences and footnote a; REPORT main p. 4 Statistical Analysis. These are reporting content inside one article.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Registered category Numeric or arithmetic inconsistency and domain statistical_results confirmed. All substantive comparators are in one REPORT; no role/type correction or competing precedence relationship.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct source confirms all registered values and the same-row subtraction remains different beyond displayed rounding.

**Exact remaining human question:** Was the nephropathy ARD point estimate calculated from the same 8-year Kaplan–Meier risks printed in Table 2, or from a separately defined estimand, risk set, or point-estimation rule; where is that rule documented?

## C005 — Atrial-fibrillation absolute risk difference

**Location found:** Yes. [Main PDF p. 7, Table 2 atrial fibrillation row and footnote a](../../../jama_aminian_2019_oi_190103.pdf#page=7); [main PDF p. 4, Statistical Analysis](../../../jama_aminian_2019_oi_190103.pdf#page=4). Both pages visually inspected directly.

**Source value/text matched:** Yes. The atrial fibrillation absolute 8-year risk difference is 6.5% (95% CI 4.4–8.7).

**Comparator matched:** Yes. The same row reports surgical cumulative incidence 7.9% and nonsurgical cumulative incidence 13.6%. Footnote a names the difference as nonsurgical control group minus metabolic surgery. Page 4 describes Kaplan–Meier cumulative incidence and absolute risk differences; bootstrap percentile calculation is specified for the CIs.

**Consistency rule applicable:** Yes for the displayed same-outcome, same-time risk subtraction. It does not equate this risk-difference CI with the adjusted Cox HR CI or P value.

**Calculation or logical comparison reproduced:** 13.6−7.9=5.7 percentage points, compared with 6.5; difference 0.8 percentage points. With three quantities individually rounded to a tenth, combined nearest-tenth uncertainty is at most 0.15 percentage points, below 0.8. This is a displayed point-estimate comparison, not a reconstruction of the fitted model or bootstrap distribution.

**Necessary inputs available:** The two displayed risks, displayed difference, time, outcome, group order, and stated difference rule are available.

**Exact missing inputs or definitions:** Unrounded cumulative incidence values and the precise point-estimation implementation for the ARD, including whether a separately derived point estimate or risk set was used. Bootstrap CIs alone do not define an alternative ARD point estimate.

**Source-grounded alternative interpretation:** The source supplies bootstrap uncertainty estimation and outcome-specific risk sets; a separately generated ARD point estimate could conceivably explain the display, but the source does not state that its point estimate differs from subtraction of the same-row risks. This remains an alternative requiring a definition, not an inferred production process.

**Direct observation versus inferred explanation:** The row values and footnote are direct source observations. Subtraction and the rounding bound are reproduced diagnostics. No numerical replacement, production error mechanism, or effect on conclusions is established.

**Compared document roles:** REPORT main p. 7 Table 2 ARD; REPORT same-page two cumulative incidences and footnote a; REPORT main p. 4 Statistical Analysis. These are reporting content inside one article.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Registered category Numeric or arithmetic inconsistency and domain statistical_results confirmed. All substantive comparators are in one REPORT; no role/type correction or competing precedence relationship.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct source confirms all registered values and the same-row subtraction remains different beyond displayed rounding.

**Exact remaining human question:** Was the atrial fibrillation ARD point estimate calculated from the same 8-year Kaplan–Meier risks printed in Table 2, or from a separately defined estimand, risk set, or point-estimation rule; where is that rule documented?

## C006 — Unmatched male percentage

**Location found:** Yes. [Main Table 1, PDF p. 5, men row and column header](../../../jama_aminian_2019_oi_190103.pdf#page=5), directly rendered and visually inspected.

**Source value/text matched:** Yes. The count/percentage cell is 18895 (48.2%).

**Comparator matched:** Yes. Its cohort column header gives N=39267.

**Consistency rule applicable:** Yes, conditionally on ordinary unweighted count/cohort-denominator percentages and direct nearest-tenth rounding. Those are the displayed number/percentage/header relationship; the source does not prescribe a rounding sequence.

**Calculation or logical comparison reproduced:** 100×18895/39267=48.119285914%. This lies outside [48.15,48.25)%, the direct nearest-tenth interval for 48.2%; direct rounding yields 48.1%. The arithmetic is independently reproduced.

**Necessary inputs available:** Printed count, percentage, and common cohort header denominator are available.

**Exact missing inputs or definitions:** Exact percentage denominator, any weighting or analytic restriction, and rounding sequence/tie-breaking convention. No underlying participant data or production code is supplied.

**Source-grounded alternative interpretation:** No specified alternative denominator or weighting is printed for this cell. A separate denominator or weighting could explain the percentage only if documented; the displayed sex counts sum to the full unmatched cohort.

**Direct observation versus inferred explanation:** Cell and header are source observations; the division and rounding comparison are diagnostics. A transcription mechanism, alternate denominator, or two-stage process is not established.

**Compared document roles:** REPORT main Table 1 men count/percentage; REPORT same-table cohort header. Both are results reporting in a single document.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Denominator, proportion, or total inconsistency; statistical_results. Roles and relationship confirmed without correction; no conflicting PLAN comparator.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct source confirms the registered cell and denominator, and the direct count-to-percentage rule gives the reproduced mismatch.

**Exact remaining human question:** What numerator, denominator, or weighting rule produced 48.2% for 18895 men in the stated unmatched cohort of 39267?

## C007 — Matched other-race percentage

**Location found:** Yes. [Main Table 1, PDF p. 5, other race row and column header](../../../jama_aminian_2019_oi_190103.pdf#page=5), directly rendered and visually inspected.

**Source value/text matched:** Yes. The count/percentage cell is 234 (2.1%).

**Comparator matched:** Yes. Its cohort column header gives N=11435.

**Consistency rule applicable:** Yes, conditionally on ordinary unweighted count/cohort-denominator percentages and direct nearest-tenth rounding. Those are the displayed number/percentage/header relationship; the source does not prescribe a rounding sequence.

**Calculation or logical comparison reproduced:** 100×234/11435=2.046348929%. This lies outside [2.05,2.15)%, the direct nearest-tenth interval for 2.1%; direct rounding yields 2.0%. The arithmetic is independently reproduced. A documented two-stage rounding rule would reconcile this specific display.

**Necessary inputs available:** Printed count, percentage, and common cohort header denominator are available.

**Exact missing inputs or definitions:** Exact percentage denominator, any weighting or analytic restriction, and rounding sequence/tie-breaking convention. No underlying participant data or production code is supplied.

**Source-grounded alternative interpretation:** Two-stage rounding is a concrete numerical alternative: 2.046348929% → 2.05% → 2.1%. Neither a two-stage sequence nor its tie-breaking convention is stated. It can reconcile the display under that convention and must not be asserted as the authors’ production process.

**Direct observation versus inferred explanation:** Cell and header are source observations; the division and rounding comparison are diagnostics. A transcription mechanism, alternate denominator, or two-stage process is not established.

**Compared document roles:** REPORT main Table 1 other race count/percentage; REPORT same-table cohort header. Both are results reporting in a single document.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Denominator, proportion, or total inconsistency; statistical_results. Roles and relationship confirmed without correction; no conflicting PLAN comparator.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct source confirms the registered cell and denominator, and the direct count-to-percentage rule gives the reproduced mismatch, with a named two-stage rounding alternative remaining unresolved.

**Exact remaining human question:** Was 2.1% calculated directly from 234/11435 or produced by two-stage rounding (2.046348929% → 2.05% → 2.1%), and what rounding convention was used?

## C008 — Unmatched UACR missingness percentage

**Location found:** Yes. [Main Table 1, PDF p. 6, UACR missingness row and column header](../../../jama_aminian_2019_oi_190103.pdf#page=6), directly rendered and visually inspected.

**Source value/text matched:** Yes. The count/percentage cell is 14665 (37.4%).

**Comparator matched:** Yes. Its cohort column header gives N=39267.

**Consistency rule applicable:** Yes, conditionally on ordinary unweighted count/cohort-denominator percentages and direct nearest-tenth rounding. Those are the displayed number/percentage/header relationship; the source does not prescribe a rounding sequence.

**Calculation or logical comparison reproduced:** 100×14665/39267=37.346881605%. This lies outside [37.35,37.45)%, the direct nearest-tenth interval for 37.4%; direct rounding yields 37.3%. The arithmetic is independently reproduced. A documented two-stage rounding rule would reconcile this specific display.

**Necessary inputs available:** Printed count, percentage, and common cohort header denominator are available.

**Exact missing inputs or definitions:** Exact percentage denominator, any weighting or analytic restriction, and rounding sequence/tie-breaking convention. No underlying participant data or production code is supplied.

**Source-grounded alternative interpretation:** Two-stage rounding is a concrete numerical alternative: 37.346881605% → 37.35% → 37.4%. Neither a two-stage sequence nor its tie-breaking convention is stated. It can reconcile the display under that convention and is not an observed production process.

**Direct observation versus inferred explanation:** Cell and header are source observations; the division and rounding comparison are diagnostics. A transcription mechanism, alternate denominator, or two-stage process is not established.

**Compared document roles:** REPORT main Table 1 UACR missingness count/percentage; REPORT same-table cohort header. Both are results reporting in a single document.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Denominator, proportion, or total inconsistency; statistical_results. Roles and relationship confirmed without correction; no conflicting PLAN comparator.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct source confirms the registered cell and denominator, and the direct count-to-percentage rule gives the reproduced mismatch, with a named two-stage rounding alternative remaining unresolved.

**Exact remaining human question:** Was 37.4% calculated directly from 14665/39267 or produced by two-stage rounding (37.346881605% → 37.35% → 37.4%), and what rounding convention was used?

## C009 — Absolute standardized-difference definition versus signed entries

**Location found:** Yes. [Main PDF p. 5, standardized-difference columns](../../../jama_aminian_2019_oi_190103.pdf#page=5) and [p. 6, Table 1 footnote b and continued columns](../../../jama_aminian_2019_oi_190103.pdf#page=6), both directly rendered and inspected.

**Source value/text matched:** Yes. Footnote b defines standardized differences as the absolute value of the difference in means or proportions between groups (metabolic surgery − nonsurgical control group) divided by pooled standard deviation.

**Comparator matched:** Yes. Before/after matching entries include men −28.0/−2.9 and age −75.3/−19.9. Other negative entries are also visible.

**Consistency rule applicable:** Yes. An absolute numerator divided by a positive standard deviation cannot be negative. Reconstructing the precise SD formula is unnecessary to the sign comparison.

**Calculation or logical comparison reproduced:** Each named negative cell is below zero, whereas the stated absolute-value definition yields a nonnegative standardized difference whenever defined.

**Necessary inputs available:** Absolute-value wording, positive-SD mathematical sign rule, and negative cell signs. The signs are source-confirmed; cell magnitudes were not recomputed.

**Exact missing inputs or definitions:** Whether the columns intentionally show signed differences and whether the footnote is intended to define absolute differences; underlying means/variances and exact pooled-SD formula are absent for magnitude reconstruction.

**Source-grounded alternative interpretation:** The negative signs follow the named surgery-minus-control direction, consistent with a signed definition; the word absolute may instead describe a different intended presentation. Either interpretation requires human confirmation of the intended label.

**Direct observation versus inferred explanation:** Footnote and signs are directly observed. The nonnegativity comparison is deductive. A software or copyediting mechanism is not established.

**Compared document roles:** REPORT main p. 6 footnote b; REPORT main pp. 5–6 standardized-difference columns, all reporting content in one article.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Measure, label, or scale inconsistency; report_internal_inconsistency. Registered roles/type unchanged.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Printed absolute-value definition and source-confirmed negative entries conflict in sign.

**Exact remaining human question:** Are the columns intended to show signed or absolute standardized differences, and which definition should govern extraction of the printed values?

## C010 — Surgical biguanide percentage

**Location found:** Yes. [Results supplement eTable 3, PDF p. 5, biguanides row and column header](../../../joi190103supp1_prod.pdf#page=5), directly rendered and visually inspected.

**Source value/text matched:** Yes. The count/percentage cell is 1530 (67.9%).

**Comparator matched:** Yes. Its cohort column header gives N=2287.

**Consistency rule applicable:** Yes, conditionally on ordinary unweighted count/cohort-denominator percentages and direct nearest-tenth rounding. Those are the displayed number/percentage/header relationship; the source does not prescribe a rounding sequence.

**Calculation or logical comparison reproduced:** 100×1530/2287=66.899868824%. This lies outside [67.85,67.95)%, the direct nearest-tenth interval for 67.9%; direct rounding yields 66.9%. The arithmetic is independently reproduced.

**Necessary inputs available:** Printed count, percentage, and common cohort header denominator are available.

**Exact missing inputs or definitions:** Exact percentage denominator, any weighting or analytic restriction, and rounding sequence/tie-breaking convention. No underlying participant data or production code is supplied.

**Source-grounded alternative interpretation:** The eTable supplies a common surgery denominator and no special biguanide denominator or weighting. A different medication-specific analytic set could explain the display only if independently defined; no such definition is printed in this table.

**Direct observation versus inferred explanation:** Cell and header are source observations; the division and rounding comparison are diagnostics. A transcription mechanism, alternate denominator, or two-stage process is not established.

**Compared document roles:** REPORT results supplement eTable 3 biguanides count/percentage; REPORT same-table cohort header. Both are results reporting in a single document.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Denominator, proportion, or total inconsistency; statistical_results. Roles and relationship confirmed without correction; no conflicting PLAN comparator.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct source confirms the registered cell and denominator, and the direct count-to-percentage rule gives the reproduced mismatch.

**Exact remaining human question:** Is biguanide use based on the printed 1530 count and 2287 denominator, or on a separately defined analytic denominator or weighting rule?

## C011 — Baseline medication analytic sample versus cohort size

**Location found:** Yes. [Results supplement p. 14, eTable 10 year-0 nonsurgical sample](../../../joi190103supp1_prod.pdf#page=14); [supplement p. 5, eTable 3 header](../../../joi190103supp1_prod.pdf#page=5); [main p. 6, Table 1 matched nonsurgical header](../../../jama_aminian_2019_oi_190103.pdf#page=6); [main p. 3, Other Outcomes and Statistical Analysis](../../../jama_aminian_2019_oi_190103.pdf#page=3); [main p. 4, Statistical Analysis and Results](../../../jama_aminian_2019_oi_190103.pdf#page=4). All directly rendered and visually inspected.

**Source value/text matched:** Yes. eTable 10 year 0 reports surgery 2287 and nonsurgical 11433; its title explicitly identifies sample sizes for computing medication proportions.

**Comparator matched:** Yes. eTable 3 and main Table 1 report the matched nonsurgical cohort as 11435. Main p. 4 Results also identifies 11435 enrolled matched controls, and pp. 3–4 discuss medication measurements/proportion tests without requiring complete analytic availability at year 0.

**Consistency rule applicable:** No unconditional equality rule is established. The comparison would require the enrolled matched cohort and year-0 medication-proportion analytic sample to be identical; the titles describe distinct quantities.

**Calculation or logical comparison reproduced:** 11435−11433=2 reproduces the count difference. It does not reproduce an established denominator inconsistency because population identity is an unsupported input alignment.

**Necessary inputs available:** Both counts, group, index-date time point, and sample titles.

**Exact missing inputs or definitions:** Medication analytic inclusion/availability rule at year 0; identities/reasons for any omitted participants; an explicit statement requiring the analytic and enrolled populations to coincide.

**Source-grounded alternative interpretation:** eTable 10 is explicitly an analytic sample table and may legitimately restrict participants available for medication-proportion computation. Two unavailable observations would explain the difference, but this number-specific cause is not stated and is not inferred as fact.

**Direct observation versus inferred explanation:** Both Ns and the two-person difference are observations/derived arithmetic. The equality of populations and any exclusion mechanism are unestablished assumptions.

**Compared document roles:** REPORT supplement p. 14 eTable 10 analytic N; REPORT supplement p. 5 eTable 3 enrolled header; REPORT main p. 6 Table 1 enrolled header and main pp. 3–4 methods/results. All are reporting content, not plans.

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Classification confirmation:** Denominator, proportion, or total inconsistency; statistical_results. Comparator structure retains S_C for main-versus-supplement and S_W for the within-supplement comparison; S_C takes precedence. No role/type correction. This describes the registered comparison, not proof of a substantive discrepancy. Classification ambiguity is the unestablished population identity.

**Evidence state:** record_input_error

**Determining recheck fact:** The comparison equates an enrolled cohort header with an explicitly medication-specific analytic sample without a source statement establishing their identity. The residual denominator question cannot be settled from the package.

**Exact remaining human question:** What is the year-0 medication analytic eligibility/availability rule, why does its nonsurgical N equal 11433, and does any supplied definition require this N to equal the 11435 enrolled controls?

## C012 — Percentage suffix on person-time rates

**Location found:** Yes. [Results supplement p. 6, eTable 4 title, headers, footnotes, and primary row](../../../joi190103supp1_prod.pdf#page=6); [p. 1, contents entry](../../../joi190103supp1_prod.pdf#page=1), both directly rendered and inspected.

**Source value/text matched:** Yes. The title/contents say Cause-Specific Event Rates (%) per 100 Patient-Years of Follow-up at 8 Years.

**Comparator matched:** Yes. Headers specify rate per 100 patient-years and difference in event rate per 100 patient-years. Primary rates are 4.51 surgery and 7.45 nonsurgery, difference 2.94. Footnote b repeats the event-rate difference per 100 patient-years.

**Consistency rule applicable:** Yes for the dimensional label. Events divided by patient-time are a rate; a percentage of patients is dimensionless. Scaling the rate by 100 retains time in the denominator.

**Calculation or logical comparison reproduced:** 7.45−4.51=2.94 per 100 patient-years, so the example rate difference reconciles. The (%) title suffix introduces an additional dimensionless-risk reading not supplied by the table’s person-time units.

**Necessary inputs available:** Explicit rate units, title suffix, source values, and difference rule. The person-time denominator itself is unnecessary to this label comparison.

**Exact missing inputs or definitions:** Whether (%) intentionally denotes informal per-100 scaling rather than patient risk; any explicit interpretation of that suffix. Raw person-time totals would be needed to recompute rates, which this candidate does not attempt.

**Source-grounded alternative interpretation:** The title may use (%) informally for a rate scaled per 100 patient-years. That reading reconciles intent but still requires the extractor to retain person-time units rather than treat the numbers as risk percentages.

**Direct observation versus inferred explanation:** Title, header, footnotes, and example values are directly observed. Unit comparison is deductive; no wrong event counts or clinical conclusion is inferred.

**Compared document roles:** REPORT supplement p. 1 contents and p. 6 eTable 4 title versus REPORT same-page rate headers/footnotes. One results supplement.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Rate-versus-count inconsistency; statistical_results. Content roles and internal relationship unchanged.

**Evidence state:** recorded_candidate

**Determining recheck fact:** The percentage suffix and explicit person-time-rate labels coexist in the source; the unit ambiguity remains as registered.

**Exact remaining human question:** Is (%) intended solely as informal per-100 rate notation, and should the table be extracted exclusively as events per 100 patient-years?

## C013 — Five-component label attached to six-component primary result

**Location found:** Yes. [Results supplement p. 19, E-value primary-outcome interpretation](../../../joi190103supp1_prod.pdf#page=19); [main p. 2, Primary and Secondary End Points](../../../jama_aminian_2019_oi_190103.pdf#page=2); [main p. 7, Figure 2 caption and Table 2 primary result](../../../jama_aminian_2019_oi_190103.pdf#page=7). [PLAN p. 4, six listed outcomes and primary definition](../../../joi190103supp2_prod.pdf#page=4) is corroboration only. All cited pages directly rendered and inspected.

**Source value/text matched:** Yes. Supplement interpretation names 5-component MACE. Its immediately preceding primary-outcome discussion specifies HR 0.61 (95% CI 0.55–0.69) and E-value 2.15.

**Comparator matched:** Yes. Main defines the primary composite as six outcomes, listing all-cause mortality, coronary artery events, cerebrovascular events, heart failure, nephropathy, and atrial fibrillation; Figure 2 caption repeats six and the primary HR/CI match the supplement.

**Consistency rule applicable:** Yes. Matching endpoint name/context and identical HR/CI identify the reported primary result; the component-count labels differ.

**Calculation or logical comparison reproduced:** Six enumerated components versus five in the interpretation differ by one. No five-component primary analysis is defined in these locations.

**Necessary inputs available:** Printed primary-result HR/CI, primary-outcome context, component definitions, and count labels.

**Exact missing inputs or definitions:** Whether a distinct five-component analysis was intended by the E-value interpretation and, if so, its component list and identity.

**Source-grounded alternative interpretation:** The phrase could refer to a separate five-component analysis, but the surrounding source explicitly ties it to the primary HR and E-value; a separate analysis would need definition rather than assumption.

**Direct observation versus inferred explanation:** The labels, list, and identical HR/CI are directly observed. Result-identity reasoning is grounded in these matches; an omitted-word or editing mechanism is not established.

**Compared document roles:** REPORT supplement p. 19 interpretation; REPORT main p. 2 definition and p. 7 caption/result. PLAN supplement 2 p. 4 is a dated prospective primary-endpoint definition supporting the main six-component side, not conflicting with it.

**Relationship type:** S_C

**All relationships:** S_C

**Classification confirmation:** Measure, label, or scale inconsistency; report_internal_inconsistency. S_C confirmed. Do not add P_R: the PLAN only corroborates one side of the two-REPORT mismatch. Do not add S_W solely for supplement HR context: it does not independently state a conflicting component count.

**Evidence state:** recorded_candidate

**Determining recheck fact:** The source interpretation explicitly says five while the matched primary endpoint definition says six.

**Exact remaining human question:** Does the E-value 2.15 interpretation concern the six-component primary outcome associated with HR 0.61, or a separately defined five-component outcome, and where is that definition?

## C014 — Time-varying HR text points to rate table

**Location found:** Yes. [Results supplement p. 19, Time-varying hazard ratios paragraph and repeated eTable 7](../../../joi190103supp1_prod.pdf#page=19); [p. 6, eTable 4](../../../joi190103supp1_prod.pdf#page=6); [p. 10, eTable 7](../../../joi190103supp1_prod.pdf#page=10), all directly rendered and inspected.

**Source value/text matched:** Yes. Page 19 says eTable 4 displays adjusted hazard ratios and 95% confidence intervals at 2, 5, and 8 years.

**Comparator matched:** Yes. eTable 4 is a cause-specific event-rate table per 100 patient-years at 8 years; primary rates 4.51/7.45 and difference 2.94. eTable 7, on pp. 10 and 19, supplies time-varying HRs at 2/5/8 years; primary HRs 0.57 (0.49,0.65), 0.78 (0.66,0.93), 0.79 (0.64,0.97).

**Consistency rule applicable:** Yes. A specific numbered table reference must identify a table containing the named measure and time points.

**Calculation or logical comparison reproduced:** Number 4 leads to per-time rates at 8 years; number 7 leads to the named HR/CI structure at three years. This is a table-identity/measure comparison, not a demand that rate numbers equal HRs.

**Necessary inputs available:** Reference wording, actual table numbers/titles, measures, time points, and example values.

**Exact missing inputs or definitions:** Intended numbered reference. No model inputs are needed to confirm the reference mismatch.

**Source-grounded alternative interpretation:** A draft numbering scheme could have used number 4, but the supplied document physically labels the matching table eTable 7; historical production numbering is not documented.

**Direct observation versus inferred explanation:** Reference text and both table structures are directly observed. Intended number and production cause are unknown.

**Compared document roles:** REPORT supplement p. 19 reference; REPORT supplement p. 6 eTable 4; REPORT supplement pp. 10/19 eTable 7. All belong to one results report.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Measure, label, or scale inconsistency; report_internal_inconsistency. Roles/type unchanged; no cross-document relationship.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Printed eTable 4 reference demonstrably identifies different content from its stated HR/CI description, which matches eTable 7.

**Exact remaining human question:** Which supplied table is intended by the page-19 statement that eTable 4 displays adjusted HRs and CIs at 2, 5, and 8 years?

## C015 — Named matching direction in protocol versus report

**Location found:** Yes. [PLAN PDF p. 3, Matching Process](../../../joi190103supp2_prod.pdf#page=3); [main p. 3, Figure 1 caption and final cohort boxes](../../../jama_aminian_2019_oi_190103.pdf#page=3); [main p. 4, Statistical Analysis continuation and Results](../../../jama_aminian_2019_oi_190103.pdf#page=4); [PLAN p. 6, Sensitivity analyses context](../../../joi190103supp2_prod.pdf#page=6), all directly rendered and inspected.

**Source value/text matched:** Yes. The prospective protocol says each non-surgical patient will be matched by propensity score to five surgical patients.

**Comparator matched:** Yes. Main Figure 1 caption says each surgical patient was matched to five nonsurgical patients; p. 4 repeats that named direction. Final Ns are 2287 surgery and 11435 nonsurgery.

**Consistency rule applicable:** Yes. The two explicit named-group statements reverse the matching direction. This rule compares report wording with plan wording; it does not reconstruct actual matching implementation.

**Calculation or logical comparison reproduced:** REPORT surgery:nonsurgery = 2287:11435 = 1:5. Literal PLAN named direction implies surgery:nonsurgery = 5:1 for that matching statement.

**Necessary inputs available:** Both explicit named-group directions, report achieved Ns, and matching context.

**Exact missing inputs or definitions:** Intended original protocol group order, actual implementation code, and whether a disclosed amendment intentionally changed the named direction. No claim of a proven implementation or compliance difference follows.

**Source-grounded alternative interpretation:** The PLAN sentence may reverse group names while referring to the same intended matching. PLAN p. 6 describes ratios 1:1, 1:5, 1:10 without naming numerator/denominator order; this corroborative context cannot independently prove a plan-internal discrepancy.

**Direct observation versus inferred explanation:** The two sentences and achieved cohort Ns are source observations. Literal ratio comparison is a diagnostic. A wording mistake, implementation difference, or protocol departure is not established.

**Compared document roles:** PLAN supplement 2 p. 3 is inside the prospective January 6, 2019 study protocol; REPORT main pp. 3–4 describe achieved matching/results. PLAN p. 6 unnamed ratio context is a plan locator/corroboration, not an additional discrepant comparator.

**Relationship type:** P_R

**All relationships:** P_R

**Classification confirmation:** Measure, label, or scale inconsistency; protocol_report. P_R confirmed because explicit PLAN and REPORT directions differ. No P_P is added for unnamed-ratio plan context.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Source pages contain oppositely named matching statements, and the achieved ratio agrees with the REPORT direction.

**Exact remaining human question:** Which group order was intended by the prospective matching statement, and does the reversal reflect wording or a documented change in the matching plan?

## C016 — Lower zero tick on descending weight-change axis

**Location found:** Yes. [Main PDF p. 9, Figure 4A vertical axis and panel annotation](../../../jama_aminian_2019_oi_190103.pdf#page=9), directly rendered with Poppler and visually inspected.

**Source value/text matched:** Yes. The vertical percent-change axis shows 0, −5, −10, −15, −20, −25, then 0 at its lowest displayed level. The lower glyph is physically printed to the left of the vertical axis at the bottom horizontal-axis intersection; the x-axis time-zero glyph is separately printed below the intersection.

**Comparator matched:** Yes. The upper 0 and intervening negative ticks form evenly spaced descending steps; panel labels Percent Change, % (95% CI) and Total weight loss, %. Annotation reports Δ=14.7% (95% CI, 14.5–14.9), P<.001.

**Consistency rule applicable:** Yes. An unbroken linear numeric axis cannot repeat 0 below −25 after successive −5 steps. No axis break or scale reset is shown.

**Calculation or logical comparison reproduced:** Differences between displayed adjacent ticks through −25 are −5. A next equally spaced step would continue the negative sequence; the printed lower 0 instead changes by +25. This diagnosis does not prescribe a corrected label.

**Necessary inputs available:** Visual glyph position, full tick sequence, spacing, axis label, and absence of a displayed scale break.

**Exact missing inputs or definitions:** Intended bottom tick/axis extent and whether the lower glyph was intended as an independent annotation. No extraction ambiguity remains about the glyph itself.

**Source-grounded alternative interpretation:** It could have been intended as an annotation rather than a tick, but its alignment with the vertical-axis labels and the distinct x-axis zero make that interpretation require explicit figure-design confirmation.

**Direct observation versus inferred explanation:** Both zeros and their positions are directly visible in a fresh render from the supplied PDF. Linear-sequence inconsistency is deductive. OCR artifacts are disproven; the production cause and intended replacement are not established.

**Compared document roles:** REPORT main p. 9 Figure 4A upper/lower ticks, negative sequence, and percent-change axis labels. All are one report figure.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Measure, label, or scale inconsistency; report_internal_inconsistency. Registered roles/type confirmed. Classification ambiguity is limited to intended annotation versus intended tick; the printed lower 0 is confirmed.

**Evidence state:** recorded_candidate

**Determining recheck fact:** The supplied-source render visibly contains a lower vertical-axis 0 distinct from x-axis time zero, confirming the registered visual mismatch.

**Exact remaining human question:** Is the lower vertical-axis 0 intended as a tick or independent annotation, and what bottom scale value/extent was intended for Figure 4A?

## C017 — Reciprocal matching-ratio notation in sensitivity figure

**Location found:** Yes. [Results supplement p. 17, Matching and index date sampling prose](../../../joi190103supp1_prod.pdf#page=17); [p. 18, eFigure 4 legend/title](../../../joi190103supp1_prod.pdf#page=18), both directly rendered and inspected.

**Source value/text matched:** Yes. Prose gives matching ratios 1:1, 1:5, and 1:10.

**Comparator matched:** Yes. The figure legend headed Matching ratio gives 1:1, 5:1, and 10:1. The legend and caption do not name numerator/denominator group order. The figure title concerns HRs for metabolic surgery versus no surgery, which defines the HR comparison, not necessarily the matching-ratio convention.

**Consistency rule applicable:** Conditional only. Ratios conflict if both locations use the same named-group order. Neither of the compared ratio lists specifies that order, so this alignment is not established.

**Calculation or logical comparison reproduced:** 1:5 and 5:1, and 1:10 and 10:1, are reciprocal ordered ratios. Reversing numerator/denominator group convention makes them equivalent descriptions of the same group-size allocation. No HR mismatch is inferred from the legend notation.

**Necessary inputs available:** Printed ratio lists, figure legend context, prose matching context, and five sampled index-date iterations.

**Exact missing inputs or definitions:** Explicit surgery:nonsurgery or nonsurgery:surgery group order for each ratio list and the allocation associated with each figure color.

**Source-grounded alternative interpretation:** Prose may use surgery:nonsurgery and the legend nonsurgery:surgery. That gives coherent reciprocal notation without different analyses. The underlying reference HRs and named surgery-versus-control treatment contrast do not determine ratio numerator order.

**Direct observation versus inferred explanation:** Reciprocal strings are directly observed. Same-order alignment is an unsupported input assumption; a plotting-label mistake is not established.

**Compared document roles:** REPORT results supplement p. 17 sensitivity prose; REPORT same supplement p. 18 figure legend. Neither is PLAN content.

**Relationship type:** S_W

**All relationships:** S_W

**Classification confirmation:** Measure, label, or scale inconsistency; report_internal_inconsistency. Registered internal-report comparator structure is retained, with explicit classification ambiguity over ratio order. No cross-document discrepancy is introduced by corroborating main sensitivity prose.

**Evidence state:** record_input_error

**Determining recheck fact:** Treating the reciprocal strings as conflicting allocations requires unsupported same-order alignment. The package does not define both lists’ orders, and the alternative reverse-order convention can reconcile them; residual discrepancy cannot be settled.

**Exact remaining human question:** What named-group order is used by each matching-ratio list, and which surgery/control allocation does each eFigure 4 legend color represent?

## C018 — Precision-conditional HbA1c eligibility boundary

**Location found:** Yes. [PLAN PDF p. 2, surgical inclusion criterion b](../../../joi190103supp2_prod.pdf#page=2); [main PDF p. 2, Surgical Patients criterion 3](../../../jama_aminian_2019_oi_190103.pdf#page=2); [main p. 3, Figure 1 eligibility footnote b](../../../jama_aminian_2019_oi_190103.pdf#page=3), all directly rendered and inspected.

**Source value/text matched:** Yes. PLAN surgical inclusion says HbA1c >6.4% or on diabetes medication.

**Comparator matched:** Yes. REPORT surgical inclusion says HbA1c 6.5% or greater or taking at least one diabetes medication. Figure 1 footnote b describes exclusion below 6.5% without diabetes medication.

**Consistency rule applicable:** Yes as a conditional comparison of explicitly printed numerical predicates for the same surgical eligibility context. For medication users the medication alternative may make both true. For unmedicated persons the two HbA1c predicates are equivalent on a 0.1% grid but not universally equivalent for finer-precision values. The rule does not presume actual measurement precision or changed enrolled populations.

**Calculation or logical comparison reproduced:** An unmedicated value 6.45% satisfies >6.4% and fails ≥6.5%. On one-decimal values, the smallest value above 6.4 is 6.5, so the rules agree. The possible distinguishing interval is (6.4,6.5)%; neither endpoint itself creates a difference.

**Necessary inputs available:** Both thresholds, strict/inclusive boundary words, common surgical inclusion context, and medication alternative. These suffice to reproduce the conditional numerical comparison.

**Exact missing inputs or definitions:** HbA1c storage precision, the precision and rounding used by eligibility selection, whether selection acted on rounded/displayed or full-precision values, and whether any unmedicated records were in the distinguishing interval.

**Source-grounded alternative interpretation:** The criteria may be intended as equivalent shorthand for one-decimal laboratory results. No supplied precision definition proves or disproves that reading. The source does not establish any affected participant count.

**Direct observation versus inferred explanation:** The two printed rules are directly observed. The 6.45 example and one-decimal equivalence are logical diagnostics. Actual screening differences, population changes, and protocol compliance are not inferred.

**Compared document roles:** PLAN supplement 2 p. 2 is prospective surgical eligibility wording; REPORT main p. 2 surgical inclusion and p. 3 eligibility footnote describe report cohort construction. Both REPORT locations use the same 6.5 boundary and do not create an S_W discrepancy.

**Relationship type:** P_R

**All relationships:** P_R

**Classification confirmation:** Numeric or arithmetic inconsistency; protocol_report. P_R remains applicable to the explicitly matched printed thresholds; this is a precision-conditional rule comparison. Unlike C011/C017, no identity of differently described populations or unspecified group order is required to expose the conditional predicate difference. Missing selection precision limits application to actual screening, not reproduction of the printed-rule comparison.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct source confirms >6.4 versus ≥6.5 for the same surgical criterion, reproducing the registered conditional comparison while preserving one-decimal equivalence and missing actual selection precision.

**Exact remaining human question:** Did eligibility selection use a one-decimal HbA1c grid or finer/full-precision values, and were >6.4% and ≥6.5% intended to implement the identical boundary for unmedicated patients?

## Completeness and unresolved definitions

All 18 assigned stable IDs have separate source, comparator, calculation/rule, input, alternative, classification, and evidence-state records. There are no missing source pages, unreadable locations, transcription repairs, or source-role changes in this assigned scope.

Remaining human definitions are bounded: ARD point estimation/unrounded risks (C001–C005); count-percentage denominators/rounding (C006–C008, C010); signed versus absolute standardized-difference convention (C009); medication analytic eligibility (C011); percent suffix meaning for rates (C012); component count/result identity (C013); intended numbered table reference (C014); intended matching group direction (C015); Figure 4A intended lower scale/annotation (C016); figure/prose ratio order (C017); HbA1c selection precision (C018). No mechanism or paper-level conclusion change is assigned.

