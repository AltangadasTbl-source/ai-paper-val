# Numeric Consistency Review

## Scope, authority, and method

This checker reviewed all 62 stable numeric/reporting relationships, `N001` through `N062`, from `relationships/numeric_relationship_inventory.md`. It used the completed main and support quantitative evidence maps as locators only. The direct supplied PDFs were the authority: `jama_brenner_2019_oi_190039.pdf` (DOC-001), `joi190039supp1_prod.pdf` (DOC-002), `joi190039supp2_prod.pdf` (DOC-003), `joi190039supp3_prod.pdf` (DOC-004), and `joi190039supp4_prod.pdf` (DOC-005).

Applied checks, where the relationship supplied the necessary inputs, were arithmetic, arm and subgroup sums, row/column and confusion-matrix totals, numerator/denominator percentages, percentage-point differences, missingness identities, population and time-point matching, units/labels/scales, reference-group direction, count-versus-rate/proportion distinctions, and repeated-value matching. A displayed percentage was treated as reconciling when the exact count-derived percentage rounds to the printed one decimal place (tolerance: 0.05 percentage point for an individual percentage). A displayed difference was treated as reconciling when it is compatible with subtraction of the unrounded underlying proportions and one-decimal display (tolerance: 0.1 percentage point, allowing independent rounding of the two printed component percentages). Planning quantities, protocols, administrative values, and explicit no-result records were checked for a concrete numeric contradiction only; a difference between planned and observed quantities was not treated as a contradiction.

## Coverage register and no-candidate outcomes

| Relationship ID | Direct-source scope checked | Applied result | Outcome |
|---|---|---|---|
| N001 | DOC-001 PDF p. 1, Abstract | 1208 + 1214 = 2422; dose, two-day timing, centre components, and stated population labels were mutually compatible. | No candidate. |
| N002 | DOC-001 PDF p. 2 | Advanced-neoplasm definition and 14 practices + 4 hospitals = 18 centres reconcile. | No candidate. |
| N003 | DOC-001 PDF p. 2 | Four kits for each of two FITs and baseline plus three post-dose samples are consistently labelled. | No candidate. |
| N004 | DOC-001 PDF p. 3 | Block allocation 10 + 10 = 20; analytical range, time, and temperature use compatible units. | No candidate. |
| N005 | DOC-001 PDF p. 3 | Primary cutoffs, day-2 scheduled-sample timing, outcome, and analysis-set labels are mutually compatible. | No candidate. |
| N006 | DOC-001 PDF pp. 1, 3-4, Figure | 1208 = 1131 + 77; 1214 = 1153 + 61; 1131 = 1075 + 56; 1153 = 1059 + 94; arm exclusions 56 + 94 = 150; 77 + 61 + 150 = 288; 2422 - 288 = 2134. Figure exclusion subrows also sum to their arm totals. | No candidate. |
| N007 | DOC-001 PDF pp. 1, 3 | 8 + 216 = 224; 224/2134 = 10.50%, 8/2134 = 0.375%, and 216/2134 = 10.12%, compatible with 10.5%, 0.4%, and 10.1%. | No candidate. |
| N008 | DOC-001 PDF p. 4, Table 1 | Sex and all age-band counts sum separately to 1075 and 1059; displayed percentages reconcile within rounding tolerance. | No candidate. |
| N009 | DOC-001 PDF p. 4, Table 1 footnote | 805 + 228 = 1033 = 1075 - 42; 794 + 221 = 1015 = 1059 - 44. Indication percentages use the nonmissing denominators and reconcile. | No candidate. |
| N010 | DOC-001 PDF p. 4, Table 1 | Each arm’s colonoscopy categories sum to its analysis total; 3 + 5 CRC and 112 + 104 advanced adenoma give 224 advanced neoplasms. | No candidate. |
| N011 | DOC-001 PDF p. 3 | Day-2 valid-result counts are compatible with the corresponding Table 2 confusion-matrix totals. | No candidate. |
| N012 | DOC-001 PDF p. 4 | Event and participant counts, serious-event subset, group assignment, and recovery statement have no concrete numerical conflict. | No candidate. |
| N013 | DOC-001 PDF p. 5, Table 2, all participants | TP + FN and TN + FP give stated test denominators; 45/112 = 40.2%, 755/918 = 82.2%, 31/102 = 30.4%, and 807/910 = 88.7%. Differences reconcile under rounding. | No candidate. |
| N014 | DOC-001 PDF p. 5, Table 2, all participants | Counts yield 28.6%, 91.7%, 22.5%, and 94.8%; the displayed +6.0 and -3.1 percentage-point differences reconcile under rounding. | No candidate. |
| N015 | DOC-001 PDF p. 5, Table 2, all participants | Counts yield 34.7%, 83.8%, 22.0%, and 91.8%; displayed differences reconcile. | No candidate. |
| N016 | DOC-001 PDF p. 5, Table 2, men | Counts yield 42.9%, 80.0%, 27.8%, and 85.1%; displayed differences reconcile. | No candidate. |
| N017 | DOC-001 PDF p. 5, Table 2, men | Counts yield 32.5%, 90.7%, 24.1%, and 93.2%; displayed differences reconcile. | No candidate. |
| N018 | DOC-001 PDF p. 5, Table 2, men | Counts yield 39.4%, 82.7%, 21.8%, and 89.3%; displayed differences reconcile. | No candidate. |
| N019 | DOC-001 PDF p. 5, Table 2, women | Counts yield 34.3%, 84.4%, 33.3%, and 92.3%; displayed differences reconcile. | No candidate. |
| N020 | DOC-001 PDF p. 5, Table 2, women | Counts yield 20.0%, 92.7%, 20.8%, and 96.5%; displayed differences reconcile. | No candidate. |
| N021 | DOC-001 PDF p. 5, Table 2, women | Counts yield 23.3%, 84.9%, 22.2%, and 94.5%; displayed differences reconcile. | No candidate. |
| N022 | DOC-001 PDF p. 5, Table 3, all participants | PPV and NPV recomputed from N013 counts reconcile, including independently rounded percentage-point differences. | No candidate. |
| N023 | DOC-001 PDF p. 5, Table 3, all participants | PPV and NPV recomputed from N014 counts reconcile, including independently rounded percentage-point differences. | No candidate. |
| N024 | DOC-001 PDF p. 5, Table 3, all participants | PPV and NPV recomputed from N015 counts reconcile, including independently rounded percentage-point differences. | No candidate. |
| N025 | DOC-001 PDF p. 5, Table 3, men | PPV and NPV recomputed from N016 counts reconcile. | No candidate. |
| N026 | DOC-001 PDF p. 5, Table 3, men | PPV and NPV recomputed from N017 counts reconcile. | No candidate. |
| N027 | DOC-001 PDF p. 5, Table 3, men | PPV and NPV recomputed from N018 counts reconcile. | No candidate. |
| N028 | DOC-001 PDF p. 5, Table 3, women | PPV and NPV recomputed from N019 counts reconcile. | No candidate. |
| N029 | DOC-001 PDF p. 5, Table 3, women | PPV and NPV recomputed from N020 counts reconcile. | No candidate. |
| N030 | DOC-001 PDF p. 5, Table 3, women | PPV and NPV recomputed from N021 counts reconcile. | No candidate. |
| N031 | DOC-001 PDF p. 4; DOC-004 PDF pp. 5-6 | Narrative pointers correctly identify multi-sample and exact-day per-protocol analyses; quoted male differences match eTables 3 and 4. | No candidate. |
| N032 | DOC-001 PDF p. 5 | Discussion’s 24-percentage-point planned difference matches the stated 60% versus 36% power context. | No candidate. |
| N033 | DOC-001 PDF p. 5 | Dose and day-2 labels match the design and results context. | No candidate. |
| N034 | DOC-001 PDF p. 6 | Approximately 4% primary-analysis exclusions, 22% diagnostic indication, and one-time-screening limitation are correctly distinguished and have no conflicting denominator. | No candidate. |
| N035 | DOC-002 PDF p. 10 | Preliminary observational values are labelled as preliminary observational evidence, not the randomized result; no concrete within-source arithmetic or label conflict. | No candidate. |
| N036 | DOC-002 PDF pp. 10-11 | Planned 300-mg randomized design, timing, target N, and reference standard are internally compatible. | No candidate. |
| N037 | DOC-002 PDF pp. 13-14 | Planned randomized N=2400 and primary analysis N=2000 are planning quantities; protocol timing is reconciled by the SAP relabelling. | No candidate. |
| N038 | DOC-002 PDF pp. 18-21 | Four kits for each of two tests equals eight kits; baseline and subsequent collection schedule is internally compatible. | No candidate. |
| N039 | DOC-002 PDF pp. 19, 27 | Three-month limit and delay/drop-out rules use compatible time and population definitions. | No candidate. |
| N040 | DOC-002 PDF p. 24 | Random-number range 1-4000 is an allocation identifier range, not a reported participant count; no count conflict. | No candidate. |
| N041 | DOC-002 PDF pp. 26-27 | Recruitment target, duration, payment, and 25% stopping rule are planning/administrative quantities with no internal contradiction. | No candidate. |
| N042 | DOC-002 PDF pp. 30-33 | Dose ranges and safety-observation times are consistently labelled. | No candidate. |
| N043 | DOC-002 PDF pp. 35-44, 50-62 | Administrative/appendix material contains no mapped observed-result relationship requiring arithmetic reconciliation. | No candidate. |
| N044 | DOC-003 PDF pp. 2-3 | SAP trial-design, planned N, test, and reference-standard quantities are internally compatible. | No candidate. |
| N045 | DOC-003 PDF p. 4 | FAS, per-protocol, and ITS population definitions are distinct; footnote explicitly reconciles protocol day labels with SAP day labels. | No candidate. |
| N046 | DOC-003 PDF p. 6 | Raw ng Hb/mL buffer measurement and categorical µg Hb/g feces cutoffs are explicitly different scales, not conflicting quantities. | No candidate. |
| N047 | DOC-003 PDF p. 6 | Secondary measure labels distinguish sensitivity, AUC, PPV, NPV, likelihood ratios, and utilization measures. | No candidate. |
| N048 | DOC-003 PDF p. 7 | Missing, invalid, and multiple-sample selection rules state compatible day and inclusion definitions. | No candidate. |
| N049 | DOC-003 PDF p. 10 | Reference page contains no observed result requiring a numeric check. | No candidate. |
| N050 | DOC-004 PDF p. 4, eTable 2 | Quantitative intervention returned/valid totals equal sums of scheduled rows; every actual-day row sums to its valid-result count, including any-day total. | No candidate. |
| N051 | DOC-004 PDF p. 4, eTable 2 | Qualitative intervention returned/valid totals and actual-day distributions reconcile. | No candidate. |
| N052 | DOC-004 PDF p. 4, eTable 2 | Quantitative control returned/valid totals and actual-day distributions reconcile. | No candidate. |
| N053 | DOC-004 PDF p. 4, eTable 2 | Qualitative control returned/valid totals and actual-day distributions reconcile. | No candidate. |
| N054 | DOC-004 PDF p. 5, eTable 3, all | Confusion-matrix totals, sensitivity/specificity percentages, intervention-minus-control differences, and sex subgroup sums reconcile. | No candidate. |
| N055 | DOC-004 PDF p. 5, eTable 3, men | Counts, proportions, and displayed differences reconcile. | No candidate. |
| N056 | DOC-004 PDF p. 5, eTable 3, women | Counts, proportions, and displayed differences reconcile. | No candidate. |
| N057 | DOC-004 PDF p. 6, eTable 4, all | Per-protocol counts, proportions, differences, and sex subgroup sums reconcile. | No candidate. |
| N058 | DOC-004 PDF p. 6, eTable 4, men | Per-protocol counts, proportions, and displayed differences reconcile. | No candidate. |
| N059 | DOC-004 PDF p. 6, eTable 4, women | Per-protocol counts, proportions, and displayed differences reconcile. | No candidate. |
| N060 | DOC-004 PDF p. 7, eTable 5, all | PPV/NPV values and reported differences reconcile with eTable 4 count-derived ratios, allowing independent rounding. | No candidate. |
| N061 | DOC-004 PDF p. 7, eTable 5, men | PPV/NPV values and reported differences reconcile with eTable 4 count-derived ratios, allowing independent rounding. | No candidate. |
| N062 | DOC-004 PDF p. 7, eTable 5, women; DOC-004 PDF p. 6, eTable 4, women | NPV values/differences reconcile. Three PPV-difference cells contain only a minus sign despite printed arm PPVs and confidence intervals; separate proposals NC001-NC003 record the distinct rows. | Three proposals. |

## Temporary numeric-consistency proposals

### NC001 — Missing women’s quantitative 10.2 µg Hb/g PPV difference point estimate

- **Relationship:** N062.
- **Category:** Denominator, proportion, or total inconsistency; Numeric or arithmetic inconsistency.
- **Exact source locations:** DOC-004, `joi190039supp3_prod.pdf`, PDF p. 7, eTable 5, Women, Quantitative, cutoff 10.2 µg Hb/g, Difference in PPV column; supporting count inputs in PDF p. 6, eTable 4, Women, Quantitative, cutoff 10.2 µg Hb/g.
- **Printed inputs:** eTable 5 prints aspirin PPV 15.9%, placebo PPV 34.1%, a standalone `-` in the Difference in PPV point-estimate cell, and 95% CI `[ -34.7, -1.3 ]`. eTable 4 prints aspirin TP=11 and FP=58 and placebo TP=14 and FP=27.
- **Rule and reproducible calculation:** The eTable 5 column is headed “Difference in PPV [95% CI]”; for the displayed aspirin-versus-placebo ordering, difference = aspirin PPV − placebo PPV. From printed PPVs, 15.9 − 34.1 = -18.2 percentage points. Independently from the linked counts, `(11/(11+58) - 14/(14+27)) × 100 = -18.204...` percentage points, which rounds to -18.2.
- **Tolerance:** 0.1 percentage point for a difference produced from independently one-decimal-rounded percentages; the direct count calculation rounds unambiguously to -18.2. The printed point-estimate cell is not a numeric value, so rounding tolerance cannot convert its lone minus sign into a displayed estimate.
- **Direct observation versus inference:** Direct observation: the source prints the two PPVs, a confidence interval, and only `-` in the point-estimate cell. Inference: -18.2 is the reproducible arithmetic value that the omitted point-estimate cell would contain if the table follows its stated difference column.
- **Alternative source-grounded interpretations:** The standalone minus sign may be a production/formatting loss of the numeric characters rather than an intended statement that no difference was estimated. The confidence interval itself remains compatible with a negative difference. The supplied PDF does not state why the number is absent.
- **Quality-control relevance:** A reader extracting the women’s quantitative 10.2 PPV comparison lacks the printed point estimate despite having both component proportions and an interval, creating an avoidable ambiguity in a tabulated comparative result.
- **Exact human question:** Should the Difference in PPV cell for women at quantitative 10.2 µg Hb/g display `-18.2` percentage points (95% CI -34.7 to -1.3), and if not, what point estimate was intended?

### NC002 — Missing women’s quantitative 17.0 µg Hb/g PPV difference point estimate

- **Relationship:** N062.
- **Category:** Denominator, proportion, or total inconsistency; Numeric or arithmetic inconsistency.
- **Exact source locations:** DOC-004, `joi190039supp3_prod.pdf`, PDF p. 7, eTable 5, Women, Quantitative, cutoff 17.0 µg Hb/g, Difference in PPV column; supporting count inputs in PDF p. 6, eTable 4, Women, Quantitative, cutoff 17.0 µg Hb/g.
- **Printed inputs:** eTable 5 prints aspirin PPV 17.1%, placebo PPV 42.9%, a standalone `-` in the Difference in PPV point-estimate cell, and 95% CI `[ -48.4, -0.7 ]`. eTable 4 prints aspirin TP=6 and FP=29 and placebo TP=9 and FP=12.
- **Rule and reproducible calculation:** Difference = aspirin PPV − placebo PPV. From the printed PPVs, 17.1 − 42.9 = -25.8 percentage points when subtracting displayed rounded values. From the linked printed counts, `(6/(6+29) - 9/(9+12)) × 100 = -25.714...` percentage points, which rounds to -25.7; this is the appropriate count-derived one-decimal comparison.
- **Tolerance:** 0.1 percentage point for independently rounded percentages. The 0.1 difference between subtraction of displayed components (-25.8) and count-derived rounding (-25.7) is within that tolerance. A standalone minus sign is not a displayed numeric point estimate.
- **Direct observation versus inference:** Direct observation: the source prints both PPVs and a negative confidence interval but only `-` in the point-estimate cell. Inference: the count-derived point estimate is -25.7 percentage points; its consistency with the interval does not restore the omitted printed value.
- **Alternative source-grounded interpretations:** The minus sign may represent a truncated negative number in the PDF table layout. The interval could have been deliberately reported without a point estimate, but that would depart from the eTable’s named difference column and the other rows; no explanation is supplied.
- **Quality-control relevance:** The women’s higher-cutoff comparative PPV result cannot be extracted as a complete effect estimate from the published table without recalculation from another table.
- **Exact human question:** Should the Difference in PPV cell for women at quantitative 17.0 µg Hb/g display `-25.7` percentage points (95% CI -48.4 to -0.7), and if not, what point estimate was intended?

### NC003 — Missing women’s qualitative 10.2 µg Hb/g PPV difference point estimate

- **Relationship:** N062.
- **Category:** Denominator, proportion, or total inconsistency; Numeric or arithmetic inconsistency.
- **Exact source locations:** DOC-004, `joi190039supp3_prod.pdf`, PDF p. 7, eTable 5, Women, Qualitative, cutoff 10.2 µg Hb/g, Difference in PPV column; supporting count inputs in PDF p. 6, eTable 4, Women, Qualitative, cutoff 10.2 µg Hb/g.
- **Printed inputs:** eTable 5 prints aspirin PPV 9.7%, placebo PPV 31.2%, a standalone `-` in the Difference in PPV point-estimate cell, and 95% CI `[ -38.9, -3.9 ]`. eTable 4 prints aspirin TP=6 and FP=56 and placebo TP=10 and FP=22.
- **Rule and reproducible calculation:** Difference = aspirin PPV − placebo PPV. From printed PPVs, 9.7 − 31.2 = -21.5 percentage points. From linked printed counts, `(6/(6+56) - 10/(10+22)) × 100 = -21.572...` percentage points, which rounds to -21.6.
- **Tolerance:** 0.1 percentage point for independently rounded percentages. The 0.1 difference between subtraction of displayed components (-21.5) and count-derived rounding (-21.6) is within tolerance. The printed standalone minus sign does not meet the table’s numeric point-estimate format.
- **Direct observation versus inference:** Direct observation: both arm PPVs and a confidence interval are printed, but the difference point-estimate cell has only `-`. Inference: -21.6 percentage points is the count-derived value that is compatible with the displayed components and interval.
- **Alternative source-grounded interpretations:** The omission may be a repeated table-production truncation specific to negative women’s PPV differences. The supplied materials do not establish whether the authors intentionally omitted these estimates or whether an original typeset value was lost.
- **Quality-control relevance:** The table gives an incomplete comparative PPV result for the women’s qualitative test, which can lead to inconsistent manual extraction or unnecessary reconstruction from confusion-matrix counts.
- **Exact human question:** Should the Difference in PPV cell for women at qualitative 10.2 µg Hb/g display `-21.6` percentage points (95% CI -38.9 to -3.9), and if not, what point estimate was intended?

## Counts and limitations

- **Relationships checked:** 62 of 62 (`N001`-`N062`).
- **No-candidate relationship outcomes:** 61 relationships (N001-N061).
- **Relationships with one or more temporary proposals:** 1 relationship (N062).
- **Distinct temporary proposals:** 3 (`NC001`-`NC003`).
- **Limitations:** This numeric checker did not assign stable `C` IDs, severity, validity, disposition, or a correction. It did not use legacy candidate/checker/report conclusions, external literature, or the web. Confidence-interval generation and inferential-test compatibility beyond directly supplied definitions belong to the statistical review scope.
