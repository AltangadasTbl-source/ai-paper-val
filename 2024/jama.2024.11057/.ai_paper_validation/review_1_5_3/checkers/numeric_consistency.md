# Numeric Consistency Review

## Scope, source authority, and method

This review covers the stable numeric/reporting inventory `N001`-`N056`, representing every mapped direct-source unit in D001 (9 pages), D002 (15 pages), and D003 (16 pages). Canonical mapped evidence and source-coverage records were reviewed; the sole candidate was additionally confirmed against the supplied D003 PDF via direct layout extraction. No web material, older candidate/report/checker content, or scientific disposition was used.

Arithmetic was reproduced from printed counts and denominators. For a percentage printed to one decimal place, the tolerance was half of the final displayed unit, plus ordinary rounding: 0.05 percentage points. For a percentage printed to two decimals, tolerance was 0.005 points. Integer totals required exact equality unless the source explicitly said categories were not mutually exclusive. Differences between rounded displayed percentages were accepted when the unrounded count-derived value reconciled. Summary measures, confidence intervals, model-derived estimates, and weighted estimates were not treated as simple count arithmetic unless a source-supplied formula made that check applicable.

## Complete check record

| Inventory relationships | Checks applied | Outcome and reproducible observation |
|---|---|---|
| N001, N005, N021-N022, N030-N031, N039 | Population, arm total, participant flow, missingness and repeated-value checks. | No candidate. 759 + 744 = 1503; 759 + 744 + 178 = 1681; 521 + 543 = 1064 and 1064/1503 = 70.79%, displayed 70.8%. Figure arithmetic reconciles: 19,495 - 13,778 = 5,717; 5,717 - 3,273 = 2,444; 2,444 - 763 = 1,681. Figure first exclusion reasons are expressly not mutually exclusive and were not summed. |
| N002-N003, N006-N010, N040-N045, N055-N056 | Time, outcome, analysis-population, planned-versus-actual, scale/unit and no-applicable-unit checks. | No candidate. The sources distinguish the 1503 main-arm ITT set, the 1681 three-arm randomized set, the 1064 seven-month main-arm responders, and the 1016 CTP complete-data set. Protocol quantities are planned/contextual rather than final-RCT denominators. |
| N011-N020 | Table 1 category totals, available-denominator/missingness, percent, pooled-summary, scale and label checks. | No candidate. Mutually exclusive categories sum to their stated available N (for example, intervention grade 11+28+120+263+301+15+19 = 757 and control 7+29+129+253+277+20+28 = 743). Category percentages are compatible with their available Ns under stated tolerance. Nonexclusive substance-use rows were not summed. |
| N023 | SMD label/reference check. | No candidate. The statement describes SMD thresholds and does not relabel an SMD as a risk, percentage, or rate. |
| N024-N029, N046-N047, N051, N053 | Numerator/denominator, percentage, RD, risk/proportion, RR/OR label, missingness population, formula and rounding checks. | No candidate. Main ITT calculations reconcile: 287/759 = 37.813% -> 37.8%; 208/744 = 27.957% -> 28.0%; difference = 9.856 points -> 9.9. Repeated: 131/759 = 17.260% -> 17.3%; 61/744 = 8.199% -> 8.2%; difference = 9.061 -> 9.1. eTable 5 separately reconciles CCA 287/521 = 55.09% -> 55.1% and 208/543 = 38.31% -> 38.3%, and correctly labels CCA, IPRW, and missing=vaping analyses as distinct populations/estimands. eTable 3 formula rows reconcile within printed precision, e.g. at OR.miss=1: 52.26 - 40.48 = 11.78 -> 11.79; 52.26/40.48 = 1.291 -> 1.29; odds ratio = 1.606 -> 1.61. No printed percentage is a person-time rate. |
| N032-N037 | Complete-data CTP analysis totals, subgroup sums, percentages and percentage-point calculations. | No candidate. 445+326+30+215 = 1016; 598+418 = 1016; 501+515 = 1016; 300+298 = 598; 201+217 = 418. Treatment row category counts each equal their row N. 24.1% equals (30+215)/1016 = 24.114%; 41.1 - 24.1 = 17.0 points after printed rounding. 52.9 - 35.0 = 17.9 points. The 3.4%/n=10 statement has an implied denominator about 294, compatible with the stated subgroup context and ordinary rounding; it does not claim the full 598 as its denominator. |
| N038-N039, N048-N050, N054 | Repeated-value, comparator, item denominator, eTable category total, reference group, scale and duplicated-value checks. | No candidate. eTable 1's daily-use categories sum exactly to available Ns 733 and 727; repeated items occur under named distinct instruments and are not duplicates representing different results. eTable 2 waitlist categories reconcile to their disclosed available Ns; its waitlist gender denominator is not printed, but displayed counts sum to 178 and no conflicting denominator is asserted. eTable 6 distinguishes interaction betas, reference groups, and nominal from Holm-adjusted P values. |
| N052 | eTable 4 denominator, category-sum, missingness, summary-statistic label and scale checks. | One candidate-generating observation, detailed below. All other eTable 4 categorical rows reconcile to their bracketed available Ns and 439 + 1,064 = 1,503. |

## Candidate consistency issue: eTable 4 summary-statistic labels for motivation and confidence

**Primary category:** Measure, label, or scale inconsistency.

**Exact source location:** D003, `joi240078supp2_prod_1739900423.24574.pdf`, [PDF p. 12](<../../../joi240078supp2_prod_1739900423.24574.pdf#page=12>), eTable 4, rows “Motivation to quit vaping, median (IQR)” and “Confidence to quit vaping, median (IQR)”; comparator rows in the same table are “Days per month vaping, median (IQR)” and “Concern about health consequences of vaping, median (IQR).” The matching main-table definitions are D001 [PDF p. 4](<../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4>), Table 1, where motivation and confidence are displayed as median (IQR) with interval-form IQRs.

**Printed inputs:** eTable 4 calls motivation “median (IQR)” and prints nonresponder/responder values `4.1 (0.8)` and `4.1 (0.8)`. It calls confidence “median (IQR)” and prints `3.2 (1.1)` and `3.5 (1.1)`. The same source defines both response scales as 1-5. In that table, actual median-IQR displays use lower-to-upper interval form: days/month `30.0 (27.0-30.0)` versus `29.0 (26.0-30.0)` and health-consequence concern `4.0 (3.0-5.0)` versus `3.0 (3.0-4.0)`. D001 Table 1 likewise prints motivation `4.0 (4.0-5.0)` and confidence `3.0 (3.0-4.0)` under “median (IQR).”

**Direct observation:** The PDF prints the labels “median (IQR)” for the motivation and confidence rows but prints parenthetical values `0.8` and `1.1`, unlike the interval-form IQR presentation used for the other median-IQR rows in the same table and in the matched main Table 1.

**Reproducible rule and calculation:** Under the source’s own display convention, a reported IQR is shown as a two-bound interval `Q1-Q3`, not a single dispersion number. The printed values at issue have one number inside parentheses. Therefore the label-to-display test fails: `summary label = median (IQR)` expects `median (Q1-Q3)`; observed displays are `4.1 (0.8)`, `3.2 (1.1)`, and `3.5 (1.1)`. This is a direct formatting/label comparison, not an attempt to calculate a median from unavailable individual data.

**Tolerance:** None for the label/format comparison. Numerical rounding cannot turn a single parenthetical dispersion value into a two-bound IQR under the table’s stated convention.

**Inference and alternatives:** The most parsimonious inference is that these parenthetical values may be SDs and the rows may instead be means (SD), or that an unprinted alternative IQR convention was used for only these rows. That is an inference, not a source-proven correction. The sources do not provide participant-level data or a note defining a single-number IQR convention, so the exact intended summary cannot be resolved locally.

**Quality-control relevance:** A data extractor could record the values as medians with IQRs because of the printed labels, while the one-number parenthetical values visually resemble SDs. The issue is limited to reporting clarity for baseline responder/nonresponder comparisons and does not establish an error in the trial’s outcome estimates.

**Exact human question:** Were the eTable 4 motivation-to-quit and confidence-to-quit values intended to be means (SDs), or is there a source-defined reason that their IQRs are printed as single values while all other median-IQR rows use lower-to-upper interval notation?

## Limitations

The supplied PDFs do not provide participant-level data, unrounded table values, person-time denominators, or all model inputs; checks requiring these were limited to printed arithmetic, explicit source formulas, and labels. Inferential compatibility is separately assigned to the statistical reviewers. The protocol describes planned analyses and contextual prior studies; those were checked only for concrete population, unit, and planned-versus-observed reporting consistency.

## Counts

- Relationships checked: 56 numeric/reporting relationships.
- Candidate-generating observations: 1 distinct document-grounded candidate consistency issue.
- Candidate IDs, severity, validity, disposition, and correction: not assigned.
