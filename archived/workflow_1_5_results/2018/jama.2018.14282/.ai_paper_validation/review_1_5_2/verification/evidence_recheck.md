# Mechanical Evidence Recheck

This artifact mechanically rechecks the complete stable candidate set, C001 through C028, against the supplied direct-source PDFs. Fresh native/layout text and rendered pages were used only to locate evidence; the direct PDFs were the final authority. Every candidate remains **Pending Human Adjudication**. No candidate ID is deleted, merged, renumbered, or given an AI disposition.

## C001 — Standard-arm men percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Sex, Men](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — the Standard Oxygen Therapy column is headed `n = 388` and prints `247 (63.6)` for men.
- **Comparator printed value/text matched:** Yes — the displayed arm denominator is 388; the paired women row prints `141 (36.4)` and the two sex counts sum to 388.
- **Consistency rule applicable:** A count expressed as a one-decimal percentage of the displayed arm denominator should equal the count divided by 388, rounded to one decimal under the ordinary nearest rule.
- **Calculation or logical comparison reproduced:** `247/388 × 100 = 63.659794%`, which rounds to `63.7%`, not the printed `63.6%` (difference from the unrounded value, −0.0598 percentage points).
- **Necessary inputs available / exact missing inputs or definitions:** Count, printed percentage, and displayed denominator are available. The exact production denominator and rounding convention are not stated beyond the column heading.
- **Source-grounded alternative interpretation:** The paired sex counts exhaust the displayed arm and their printed percentages total 100.0%; this could reflect a convention chosen to force a displayed total, but no such convention is documented.
- **Direct observation versus inferred explanation:** Direct observation is `247 (63.6)` under `n = 388`. The arithmetic discrepancy is derived; any denominator substitution or adjusted rounding is an inferred explanation.
- **Exact remaining human question:** What denominator and rounding rule generated 63.6% for 247 standard-arm patients?

## C002 — Standard-arm women percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Sex, Women](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — the Standard Oxygen Therapy column is headed `n = 388` and prints `141 (36.4)` for women.
- **Comparator printed value/text matched:** Yes — the displayed denominator is 388; the paired men row prints `247 (63.6)` and the counts sum to 388.
- **Consistency rule applicable:** Apply count/denominator conversion and nearest one-decimal rounding.
- **Calculation or logical comparison reproduced:** `141/388 × 100 = 36.340206%`, which rounds to `36.3%`, not `36.4%` (difference +0.0598 points).
- **Necessary inputs available / exact missing inputs or definitions:** Count, percentage, and denominator are available. The production rounding convention is not supplied.
- **Source-grounded alternative interpretation:** The two printed sex percentages total 100.0%, so an undocumented paired rounding adjustment is possible; the page does not state one.
- **Direct observation versus inferred explanation:** The printed pair and denominator are direct. The rounding comparison is derived; a forced-total policy is inferred.
- **Exact remaining human question:** What denominator and rounding rule generated 36.4% for 141 standard-arm patients?

## C003 — Standard-arm heart-failure percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Heart failure](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — Standard Oxygen Therapy (`n = 388`) prints `27 (6.9)`.
- **Comparator printed value/text matched:** Yes — the applicable displayed arm denominator is 388.
- **Consistency rule applicable:** Apply count/denominator conversion and nearest one-decimal rounding.
- **Calculation or logical comparison reproduced:** `27/388 × 100 = 6.958763%`, which rounds to `7.0%`, not `6.9%` (difference −0.0588 points).
- **Necessary inputs available / exact missing inputs or definitions:** Count, percentage, and arm denominator are available. No row-specific denominator, missingness count, or alternative rounding rule is printed.
- **Source-grounded alternative interpretation:** A row-specific nonmissing denominator could alter the percentage, but Table 1 supplies no such denominator or missingness note for heart failure.
- **Direct observation versus inferred explanation:** `27 (6.9)` and `n = 388` are direct observations. A hidden denominator or rounding convention is inferred.
- **Exact remaining human question:** What denominator and rounding rule generated 6.9% for 27 standard-arm patients?

## C004 — High-flow liver-disease percentage conflicts with displayed count

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Liver](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — High-Flow Oxygen Therapy (`n = 388`) prints `45 (13.3)`.
- **Comparator printed value/text matched:** Yes — the displayed denominator is 388; the adjacent Standard Oxygen Therapy value is separately printed as `56 (14.4)`.
- **Consistency rule applicable:** The printed percentage should reconcile to the printed count over the displayed arm denominator, allowing ordinary one-decimal rounding.
- **Calculation or logical comparison reproduced:** `45/388 × 100 = 11.597938%`, or `11.6%` to one decimal, not `13.3%`; the gap is 1.7021 points. A percentage of 13.3% with count 45 mathematically implies a denominator near 338, which is not printed for this row.
- **Necessary inputs available / exact missing inputs or definitions:** The count, percentage, and column denominator are available. Missing are any row-specific denominator, missingness definition, or source note explaining a population near 338.
- **Source-grounded alternative interpretation:** An unprinted row-specific analysis population could reconcile the pair; Table 1 instead labels the column `n = 388` and gives no liver-row exception.
- **Direct observation versus inferred explanation:** The row values and arm denominator are direct. A transcription, column-placement issue, or hidden denominator is inferred.
- **Exact remaining human question:** Which count, percentage, or population denominator was intended for high-flow liver disease?

## C005 — Standard-arm kidney-disease percentage conflicts with displayed count

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Kidney disease](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — Standard Oxygen Therapy (`n = 388`) prints `69 (20.4)`.
- **Comparator printed value/text matched:** Yes — the displayed denominator is 388; the adjacent high-flow value is separately printed as `73 (18.8)`.
- **Consistency rule applicable:** The count/percentage pair should reconcile to the displayed arm denominator under one-decimal rounding.
- **Calculation or logical comparison reproduced:** `69/388 × 100 = 17.783505%`, or `17.8%`, not `20.4%`; the gap is 2.6165 points. A percentage of 20.4% with count 69 implies a denominator near 338, not printed for this row.
- **Necessary inputs available / exact missing inputs or definitions:** Count, percentage, and arm denominator are present. No row-specific denominator or missingness definition is supplied.
- **Source-grounded alternative interpretation:** A row-specific denominator near 338 could reconcile the pair, but the source does not print such a denominator or a kidney-row exception.
- **Direct observation versus inferred explanation:** `69 (20.4)` under `n = 388` is direct. A hidden denominator, transcription, or placement mechanism is inferred.
- **Exact remaining human question:** Which count, percentage, or population denominator was intended for standard-arm kidney disease?

## C006 — Standard-arm nontransplant immunosuppression percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Non-transplant-related reasons](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — Standard Oxygen Therapy (`n = 388`) prints `98 (25.2)`.
- **Comparator printed value/text matched:** Yes — the parent `Immunosuppressive drugs` row prints `135 (34.8)` and the companion `After solid organ transplantation` row prints `37 (9.5)`; their counts sum to 135, while the displayed arm denominator remains 388.
- **Consistency rule applicable:** The row's percentage should equal 98/388 to the shown precision; the child counts should also remain coherent with the parent count.
- **Calculation or logical comparison reproduced:** `98/388 × 100 = 25.257732%`, which rounds to `25.3%`, not `25.2%`; `98 + 37 = 135`, so the count subtotal itself reproduces.
- **Necessary inputs available / exact missing inputs or definitions:** Parent and child counts, percentages, and arm denominator are available. The percentage-production rule is missing.
- **Source-grounded alternative interpretation:** The source may have applied an undocumented rounding adjustment across the two child percentages, but it does not describe one.
- **Direct observation versus inferred explanation:** The printed parent/child records are direct; the rounding discrepancy is derived and the adjustment mechanism is inferred.
- **Exact remaining human question:** What denominator and rounding rule generated 25.2% for 98 standard-arm patients?

## C007 — High-flow ≥3-days-after-ICU-admission percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Randomization, ≥3 days after](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — High-Flow Oxygen Therapy (`n = 388`) prints `20 (5.1)`.
- **Comparator printed value/text matched:** Yes — the four high-flow timing counts are 244, 77, 47, and 20 and sum to 388.
- **Consistency rule applicable:** The count should convert to a percentage of the exhaustive arm total under nearest one-decimal rounding.
- **Calculation or logical comparison reproduced:** `20/388 × 100 = 5.154639%`, which rounds to `5.2%`, not `5.1%`; `244 + 77 + 47 + 20 = 388`.
- **Necessary inputs available / exact missing inputs or definitions:** Count, exhaustive timing total, and displayed denominator are available. The rounding rule is not defined.
- **Source-grounded alternative interpretation:** An undocumented category-level rounding adjustment is possible, although the source presents the four timing rows as an exhaustive arm distribution.
- **Direct observation versus inferred explanation:** Values and exhaustive subtotal are direct; adjusted rounding is inferred.
- **Exact remaining human question:** What rounding rule generated 5.1% for 20 of 388 high-flow patients?

## C008 — Standard-arm ≥3-days-after-ICU-admission percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Randomization, ≥3 days after](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — Standard Oxygen Therapy (`n = 388`) prints `20 (5.1)`.
- **Comparator printed value/text matched:** Yes — the four standard-arm timing counts are 251, 79, 38, and 20 and sum to 388.
- **Consistency rule applicable:** Apply the displayed exhaustive arm denominator and nearest one-decimal rounding.
- **Calculation or logical comparison reproduced:** `20/388 × 100 = 5.154639%`, which rounds to `5.2%`, not `5.1%`; `251 + 79 + 38 + 20 = 388`.
- **Necessary inputs available / exact missing inputs or definitions:** All count and denominator inputs are present; the source-specific rounding convention is absent.
- **Source-grounded alternative interpretation:** A category-level adjustment could preserve a desired displayed total, but no adjustment rule is printed.
- **Direct observation versus inferred explanation:** The table values are direct; any adjusted rounding mechanism is inferred.
- **Exact remaining human question:** What rounding rule generated 5.1% for 20 of 388 standard-arm patients?

## C009 — Standard-arm vasopressor percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Vasopressors at randomization](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — Standard Oxygen Therapy (`n = 388`) prints `39 (10.0)`.
- **Comparator printed value/text matched:** Yes — the displayed denominator is 388; the high-flow comparator is separately printed as `33 (8.5)`.
- **Consistency rule applicable:** Apply count/denominator conversion and nearest one-decimal rounding.
- **Calculation or logical comparison reproduced:** `39/388 × 100 = 10.051546%`, which rounds to `10.1%`, not `10.0%` (difference −0.0515 points).
- **Necessary inputs available / exact missing inputs or definitions:** Count, percentage, and arm denominator are available. No alternative denominator or rounding rule is supplied.
- **Source-grounded alternative interpretation:** A nonstandard truncation or hidden eligible denominator could yield 10.0%, but neither is documented on the page.
- **Direct observation versus inferred explanation:** The printed pair is direct; truncation or a hidden denominator is inferred.
- **Exact remaining human question:** What denominator and rounding rule generated 10.0% for 39 standard-arm patients?

## C010 — High-flow do-not-intubate percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Goals of care, Do not intubate](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — High-Flow Oxygen Therapy (`n = 388`) prints `13 (3.3)`.
- **Comparator printed value/text matched:** Yes — the displayed arm denominator is 388 and the other goals-of-care counts are printed in the same arm.
- **Consistency rule applicable:** Apply count/denominator conversion and nearest one-decimal rounding.
- **Calculation or logical comparison reproduced:** `13/388 × 100 = 3.350515%`, which rounds to `3.4%`, not `3.3%` (difference −0.0505 points).
- **Necessary inputs available / exact missing inputs or definitions:** Count, percentage, and denominator are present. The exact rounding convention is missing.
- **Source-grounded alternative interpretation:** Truncation would display 3.3%, but the source does not state truncation and other table percentages are not uniformly truncated.
- **Direct observation versus inferred explanation:** The table pair is direct; a truncation policy is inferred.
- **Exact remaining human question:** What denominator and rounding convention generated 3.3% for 13 high-flow patients?

## C011 — High-flow do-not-resuscitate percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Goals of care, Do not resuscitate](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — High-Flow Oxygen Therapy (`n = 388`) prints `3 (0.7)`.
- **Comparator printed value/text matched:** Yes — the displayed arm denominator is 388.
- **Consistency rule applicable:** Apply count/denominator conversion and nearest one-decimal rounding.
- **Calculation or logical comparison reproduced:** `3/388 × 100 = 0.773196%`, which rounds to `0.8%`, not `0.7%` (difference −0.0732 points).
- **Necessary inputs available / exact missing inputs or definitions:** The needed count, percentage, and denominator are present. No alternate denominator or rounding convention is printed.
- **Source-grounded alternative interpretation:** Decimal truncation would produce 0.7%, but the table does not declare a truncation policy.
- **Direct observation versus inferred explanation:** The printed values are direct; truncation is an inferred mechanism.
- **Exact remaining human question:** What denominator and rounding convention generated 0.7% for 3 high-flow patients?

## C012 — Standard-arm do-not-resuscitate percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Goals of care, Do not resuscitate](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — Standard Oxygen Therapy (`n = 388`) prints `1 (0.2)`.
- **Comparator printed value/text matched:** Yes — the displayed arm denominator is 388.
- **Consistency rule applicable:** Apply count/denominator conversion and nearest one-decimal rounding.
- **Calculation or logical comparison reproduced:** `1/388 × 100 = 0.257732%`, which rounds to `0.3%`, not `0.2%` (difference −0.0577 points).
- **Necessary inputs available / exact missing inputs or definitions:** Count, percentage, and denominator are available. The rounding convention is not specified.
- **Source-grounded alternative interpretation:** Decimal truncation would give 0.2%, but the page does not define truncation.
- **Direct observation versus inferred explanation:** The printed pair is direct; a truncation policy is inferred.
- **Exact remaining human question:** What denominator and rounding convention generated 0.2% for 1 standard-arm patient?

## C013 — Standard-arm unknown-goals percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Goals of care, Unknown](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — Standard Oxygen Therapy (`n = 388`) prints `27 (6.9)`.
- **Comparator printed value/text matched:** Yes — the five standard-arm goals-of-care counts 309, 15, 1, 36, and 27 sum to 388.
- **Consistency rule applicable:** Apply the exhaustive arm denominator and nearest one-decimal rounding.
- **Calculation or logical comparison reproduced:** `27/388 × 100 = 6.958763%`, which rounds to `7.0%`, not `6.9%`; `309 + 15 + 1 + 36 + 27 = 388`.
- **Necessary inputs available / exact missing inputs or definitions:** The count and denominator identity are complete. The source-specific percentage-rounding rule is absent.
- **Source-grounded alternative interpretation:** An adjusted rounding scheme across exhaustive categories could be intended, but no such scheme is stated.
- **Direct observation versus inferred explanation:** Printed values and subtotal are direct; adjusted rounding is inferred.
- **Exact remaining human question:** What rounding rule generated 6.9% for 27 of 388 standard-arm patients?

## C014 — High-flow pre-randomization standard-oxygen percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, Table 1, Received standard oxygen therapy before randomization](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- **Source printed value/text matched:** Yes — High-Flow Oxygen Therapy (`n = 388`) prints `311 (80.1)`.
- **Comparator printed value/text matched:** Yes — the displayed arm denominator is 388; the standard-arm comparator is separately printed as `334 (86.1)`.
- **Consistency rule applicable:** Apply count/denominator conversion and nearest one-decimal rounding.
- **Calculation or logical comparison reproduced:** `311/388 × 100 = 80.154639%`, which rounds to `80.2%`, not `80.1%` (difference −0.0546 points).
- **Necessary inputs available / exact missing inputs or definitions:** Count, percentage, and denominator are available. No alternative denominator or rounding rule is printed.
- **Source-grounded alternative interpretation:** A pre-randomization data-availability denominator could differ from 388, but the source provides no missingness count or alternate denominator for this row.
- **Direct observation versus inferred explanation:** The printed pair is direct; a restricted data-availability denominator is inferred.
- **Exact remaining human question:** What denominator and rounding rule generated 80.1% for 311 high-flow patients?

## C015 — High-flow ICU-acquired-infection percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.5, Table 2, ICU-acquired infection](../../../jama_azoulay_2018_oi_180109.pdf#page=5).
- **Source printed value/text matched:** Yes — High-Flow Oxygen Therapy (`n = 388`) prints `39 (10.0)`.
- **Comparator printed value/text matched:** Yes — the arm denominator is 388; Standard Oxygen Therapy prints `41 (10.6)`.
- **Consistency rule applicable:** The displayed percentage should reconcile to the event count over the displayed analysis denominator, unless an explicit at-risk denominator is supplied.
- **Calculation or logical comparison reproduced:** `39/388 × 100 = 10.051546%`, which rounds to `10.1%`, not `10.0%`; `41/388 × 100 = 10.567010%`, which does round to the printed 10.6% comparator.
- **Necessary inputs available / exact missing inputs or definitions:** Counts and arm denominators are available. The table does not supply a separate infection-at-risk denominator or a rounding rule.
- **Source-grounded alternative interpretation:** ICU-acquired infection could use an at-risk subset defined by ICU exposure, but Table 2 presents `n = 388` and no alternate denominator.
- **Direct observation versus inferred explanation:** Printed event pairs and headings are direct; an at-risk denominator is inferred.
- **Exact remaining human question:** Which denominator and rounding rule generated 10.0% for 39 high-flow infections?

## C016 — Standard-arm hospital-mortality percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.5, Table 2, Hospital mortality](../../../jama_azoulay_2018_oi_180109.pdf#page=5).
- **Source printed value/text matched:** Yes — Standard Oxygen Therapy (`n = 388`) prints `162 (41.7)`.
- **Comparator printed value/text matched:** Yes — the arm denominator is 388; High-Flow Oxygen Therapy prints `160 (41.2)`.
- **Consistency rule applicable:** Mortality count divided by the displayed arm denominator should reproduce the one-decimal percentage.
- **Calculation or logical comparison reproduced:** `162/388 × 100 = 41.752577%`, which rounds to `41.8%`, not `41.7%`; `160/388 × 100 = 41.237113%`, which rounds to the printed 41.2% comparator.
- **Necessary inputs available / exact missing inputs or definitions:** Counts, percentages, and arm denominator are available. No hospital-follow-up denominator or rounding exception is stated.
- **Source-grounded alternative interpretation:** A denominator excluding patients without hospital disposition could differ, but the table says no patients were lost to follow-up and supplies no alternative hospital denominator.
- **Direct observation versus inferred explanation:** The values and no-loss footnote are direct; an alternate disposition denominator is inferred.
- **Exact remaining human question:** What denominator and rounding rule generated 41.7% for 162 standard-arm hospital deaths?

## C017 — Respiratory-rate confidence-interval endpoint differs between matched occurrences

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.1, abstract](../../../jama_azoulay_2018_oi_180109.pdf#page=1) and [DOC-001 PDF p.6, Secondary Outcomes](../../../jama_azoulay_2018_oi_180109.pdf#page=6).
- **Source printed value/text matched:** Yes — the abstract prints 25/min versus 26/min, difference `−1.8/min`, 95% CI `−3.2 to −0.2` after 6 hours.
- **Comparator printed value/text matched:** Yes — the results narrative prints the same 25/min versus 26/min, mean difference `−1.8`, and lower endpoint `−3.2`, but upper endpoint `−0.3`.
- **Consistency rule applicable:** Matched occurrences with the same population, arms, six-hour time point, estimate, unit, confidence level, and displayed precision should have matching interval endpoints unless distinct analyses or rounding are identified.
- **Calculation or logical comparison reproduced:** Exact comparison reproduces a 0.1/min upper-endpoint difference: `−0.2 − (−0.3) = 0.1`; all other printed matching elements agree.
- **Necessary inputs available / exact missing inputs or definitions:** Both displayed intervals and matching dimensions are available. Missing are unrounded endpoints, model/analysis-set identity for each occurrence, and the rounding rule.
- **Source-grounded alternative interpretation:** Separate hidden-precision calculations or display rounding could produce different endpoints, but neither occurrence identifies a distinct analysis or precision basis.
- **Direct observation versus inferred explanation:** The endpoint mismatch is directly printed. Rounding, transcription, or separate calculations are inferred explanations.
- **Exact remaining human question:** Which 95% CI, underlying analysis, and rounding rule is authoritative for the six-hour respiratory-rate difference?

## C018 — Arm-attributed support-needs percentages use the overall-trial denominator

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.6, Post Hoc Outcomes](../../../jama_azoulay_2018_oi_180109.pdf#page=6).
- **Source printed value/text matched:** Yes — the paragraph states that vasopressors and renal replacement therapy were needed in `153 patients (19.7%) randomized to high-flow oxygen therapy` and `31 patients (4%) randomized to standard oxygen therapy`.
- **Comparator printed value/text matched:** Yes — the article consistently states 388 analyzed patients per arm and 776 overall, including [DOC-001 PDF p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1).
- **Consistency rule applicable:** A percentage grammatically attached to an arm count ordinarily uses that arm's denominator unless the overall denominator is expressly assigned.
- **Calculation or logical comparison reproduced:** `153/776 × 100 = 19.7165%` and `31/776 × 100 = 3.9948%`, reproducing 19.7% and 4.0%. Within-arm calculations are `153/388 = 39.4330%` and `31/388 = 7.9897%`, or 39.4% and 8.0%.
- **Necessary inputs available / exact missing inputs or definitions:** Both arm and overall denominators are available. Missing is an explicit statement of which denominator the sentence intends for the percentages and whether the two treatments are a combined outcome or separate needs.
- **Source-grounded alternative interpretation:** The paragraph begins `In the overall population`, supporting an interpretation that each percentage is intentionally a share of all 776 participants even though each count is then attributed to an arm.
- **Direct observation versus inferred explanation:** The printed counts, percentages, and trial denominators are direct. Whether the grammar communicates an overall or within-arm rate is interpretive.
- **Exact remaining human question:** Were 19.7% and 4.0% intended as shares of the overall trial population, and if so should that denominator be made explicit rather than read as within-arm risks?

## C019 — eTable high-flow invasive-MV percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-003 PDF p.2, eTable](../../../joi180109supp2_prod.pdf#page=2).
- **Source printed value/text matched:** Yes — High-flow oxygen therapy (`N=388`) prints invasive mechanical ventilation `39 (10.0)`.
- **Comparator printed value/text matched:** Yes — the displayed denominator is 388; the same column prints 349 non-intubated patients receiving high-flow (`349 (100)`), and `39 + 349 = 388`.
- **Consistency rule applicable:** The invasive-MV count should reconcile to the displayed randomized-group denominator under one-decimal rounding.
- **Calculation or logical comparison reproduced:** `39/388 × 100 = 10.051546%`, which rounds to `10.1%`, not `10.0%`; the complementary count identity reproduces 388.
- **Necessary inputs available / exact missing inputs or definitions:** Count and group denominator are available. The exact denominator used for 10.0% and rounding convention are absent.
- **Source-grounded alternative interpretation:** A six-hour evaluable denominator or truncation might explain 10.0%, but the eTable labels the column `N=388` and provides no alternate denominator.
- **Direct observation versus inferred explanation:** The eTable values are direct; an evaluable subset or truncation is inferred.
- **Exact remaining human question:** What denominator and rounding rule generated 10.0% for 39 high-flow invasive-MV events at six hours?

## C020 — eTable standard-arm invasive-MV percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-003 PDF p.2, eTable](../../../joi180109supp2_prod.pdf#page=2).
- **Source printed value/text matched:** Yes — Standard Oxygen (`N=388`) prints invasive mechanical ventilation `46 (11.8)`.
- **Comparator printed value/text matched:** Yes — the same column prints standard oxygen only `342 (88.2)`, and the counts sum to 388.
- **Consistency rule applicable:** Each count/percentage pair should reconcile to the displayed group denominator at one decimal.
- **Calculation or logical comparison reproduced:** `46/388 × 100 = 11.855670%`, which rounds to `11.9%`, not `11.8%`; `46 + 342 = 388`.
- **Necessary inputs available / exact missing inputs or definitions:** Counts and denominator are available. The rounding or complementary-category adjustment rule is not stated.
- **Source-grounded alternative interpretation:** The paired percentages 11.8% and 88.2% total 100.0%, suggesting a possible undocumented complementary adjustment rather than independent nearest rounding.
- **Direct observation versus inferred explanation:** The displayed pairs and exhaustive counts are direct; a forced-complement convention is inferred.
- **Exact remaining human question:** What percentage-production rule generated 11.8% for 46 standard-arm invasive-MV events?

## C021 — eTable standard-oxygen-only percentage does not reconcile

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-003 PDF p.2, eTable](../../../joi180109supp2_prod.pdf#page=2).
- **Source printed value/text matched:** Yes — Standard Oxygen (`N=388`) prints standard oxygen only `342 (88.2)`.
- **Comparator printed value/text matched:** Yes — the same column prints invasive mechanical ventilation `46 (11.8)`; the counts sum to 388 and percentages sum to 100.0%.
- **Consistency rule applicable:** Apply count/denominator conversion and nearest one-decimal rounding to the exhaustive category.
- **Calculation or logical comparison reproduced:** `342/388 × 100 = 88.144330%`, which rounds to `88.1%`, not `88.2%`; `342 + 46 = 388`.
- **Necessary inputs available / exact missing inputs or definitions:** Counts and denominator are complete. The table does not define an adjusted complementary rounding rule.
- **Source-grounded alternative interpretation:** The printed 88.2% is exactly the complement of the printed 11.8%, consistent with forcing the two displayed percentages to 100.0%; that convention is not stated.
- **Direct observation versus inferred explanation:** Counts and displayed percentages are direct; forced complementary rounding is inferred.
- **Exact remaining human question:** Was 88.2% calculated independently from 342/388 or set as the complement of 11.8%, and what rounding rule was intended?

## C022 — IMV cumulative-incidence comparison has incompatible printed test labels

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.4, methods continuation](../../../jama_azoulay_2018_oi_180109.pdf#page=4), [DOC-001 PDF p.6, Secondary Outcomes](../../../jama_azoulay_2018_oi_180109.pdf#page=6), and [DOC-003 PDF p.3, eFigure 1](../../../joi180109supp2_prod.pdf#page=3).
- **Source printed value/text matched:** Yes — the article methods specify cumulative incidence of IMV with death without IMV as a competing risk, comparison by the Gray test, and a cause-specific Cox model; the results print `P = .17` for the matched IMV outcome.
- **Comparator printed value/text matched:** Yes — eFigure 1 is titled `Cumulative Incidence of Mechanical Ventilation` and prints `P (log Rank test) = 0.17` for the same treatment groups and time-since-randomization display.
- **Consistency rule applicable:** Gray and log-rank are distinct named test procedures; a matched cumulative-incidence display should use the source-defined test label or state that a separate estimand/censoring procedure was used.
- **Calculation or logical comparison reproduced:** The numerical P labels match at 0.17, while the named procedures do not: `Gray test ≠ log Rank test`. No equivalence is inferred from equal rounded P values.
- **Necessary inputs available / exact missing inputs or definitions:** Endpoint, competing-risk definition, planned test name, figure test label, and rounded P value are available. Missing are the actual test statistic, variance, event/censoring data, software output, and confirmation of which procedure generated each P value.
- **Source-grounded alternative interpretation:** The eFigure could depict a separate time-to-IMV analysis using log-rank, but its cumulative-incidence title and matched treatment outcome do not state a different estimand or censoring rule.
- **Direct observation versus inferred explanation:** The conflicting printed test names are direct. A mislabeled figure or separate analysis is inferred.
- **Exact remaining human question:** Was the eFigure P=.17 produced by Gray's test, a log-rank test, or a distinct time-to-IMV analysis, and what competing-risk/censoring rule applied?

## C023 — Figure 3A mortality HR is reciprocal to the matched table/narrative orientation

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.5, Table 2 and Primary Outcome](../../../jama_azoulay_2018_oi_180109.pdf#page=5) and [DOC-001 PDF p.7, Figure 3A](../../../jama_azoulay_2018_oi_180109.pdf#page=7).
- **Source printed value/text matched:** Yes — Table 2/narrative print 138/388 high-flow versus 140/388 standard, HR `0.98 (0.77 to 1.24)`.
- **Comparator printed value/text matched:** Yes — Figure 3A's all-patient row prints the same event totals but HR `1.02 (0.81-1.29)` and places `Favors High-Flow Nasal Oxygen Therapy` left of 1 and `Favors Standard Oxygen Therapy` right of 1.
- **Consistency rule applicable:** Reciprocal effect-ratio orientations require an explicit numerator/reference definition and favor-axis labels consistent with that orientation.
- **Calculation or logical comparison reproduced:** The point estimate and lower endpoint reproduce directly: `1/0.98 = 1.020408 → 1.02` and `1/1.24 = 0.806452 → 0.81`. The displayed upper endpoint does not reproduce by directly reciprocating the displayed rounded input: `1/0.77 = 1.298701 → 1.30`, whereas Figure 3A prints 1.29. The overall values remain compatible with a reciprocal orientation if the undisplayed Table 2 endpoint before rounding was slightly greater than 0.77, but that hidden precision is not supplied. Thus the orientation comparison reproduces; the ledger's stronger claim that all displayed reciprocal endpoints match after direct rounding does not.
- **Necessary inputs available / exact missing inputs or definitions:** Matched events, table HR/CI, figure HR/CI, and favor labels are available. The figure's hazard-ratio numerator/reference group and both analyses' unrounded estimates/endpoints are not printed.
- **Source-grounded alternative interpretation:** Figure 3A may intentionally use standard-versus-high-flow while Table 2 uses high-flow-versus-standard; the near-reciprocal pattern supports this when hidden precision is allowed, but the figure does not define the reversal and its favor labels still require alignment to it.
- **Direct observation versus inferred explanation:** Event totals, HRs, intervals, and labels are direct; an intentional reciprocal contrast is inferred.
- **Exact remaining human question:** What numerator/reference group defines Figure 3A HRs, and are its left/right favor labels aligned with that definition?

## C024 — Figure 3B IMV HR is reciprocal to the matched table/narrative orientation

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.5, Table 2](../../../jama_azoulay_2018_oi_180109.pdf#page=5), [DOC-001 PDF p.6, Secondary Outcomes](../../../jama_azoulay_2018_oi_180109.pdf#page=6), and [DOC-001 PDF p.7, Figure 3B](../../../jama_azoulay_2018_oi_180109.pdf#page=7).
- **Source printed value/text matched:** Yes — Table 2/narrative print 150/388 high-flow versus 170/388 standard and cause-specific HR `0.85 (0.68 to 1.06)`.
- **Comparator printed value/text matched:** Yes — Figure 3B's all-patient row uses the same event totals but prints HR `1.17 (0.94-1.46)` under the same left-high-flow/right-standard favor labels.
- **Consistency rule applicable:** A reciprocal cause-specific HR orientation must be explicitly defined and its favor-axis direction must correspond to the ratio.
- **Calculation or logical comparison reproduced:** The lower endpoint reproduces directly: `1/1.06 = 0.943396 → 0.94`. Direct reciprocals of the other displayed rounded inputs are `1/0.85 = 1.176471 → 1.18` and `1/0.68 = 1.470588 → 1.47`, whereas Figure 3B prints 1.17 and 1.46. Those values can still be compatible with a reciprocal orientation when undisplayed pre-rounding values are allowed, but the needed hidden precision is absent. Thus the near-reciprocal orientation comparison reproduces; the ledger's stronger claim of exact after-rounding agreement from all displayed inputs does not.
- **Necessary inputs available / exact missing inputs or definitions:** Event counts, table/narrative HR, figure HR, intervals, and labels are available. Missing are the figure's reference-group definition, both analyses' unrounded estimates/endpoints, and confirmation that its HR remains the same cause-specific estimand.
- **Source-grounded alternative interpretation:** Figure 3B may intentionally report standard-versus-high-flow ratios, as supported by the reciprocals; however, no figure-specific contrast definition explains the reversal or connects it to the favor labels.
- **Direct observation versus inferred explanation:** Printed values and labels are direct; intentional reciprocal orientation is inferred.
- **Exact remaining human question:** What numerator/reference group and hazard estimand define Figure 3B, and are the favor labels consistent with them?

## C025 — Revised-superiority sample-size total conflicts with equal arm counts

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-001 PDF p.3, Statistical Analysis](../../../jama_azoulay_2018_oi_180109.pdf#page=3), [DOC-002 PDF p.90, published-protocol abstract; sentence continues on p.91](../../../joi180109supp1_prod.pdf#page=90), [DOC-002 PDF p.91, continuation](../../../joi180109supp1_prod.pdf#page=91), and [DOC-002 PDF p.103, sample-size calculation](../../../joi180109supp1_prod.pdf#page=103).
- **Source printed value/text matched:** Yes — the main article prints `779 patients (389 in each group)` for 90% power under the 30% versus 20% superiority assumptions.
- **Comparator printed value/text matched:** Yes — the published-protocol abstract states 389 in each treatment group and 778 overall across pp.90-91; p.103 explicitly prints `778 patients (389 in each group)` under the same 30%, 20%, 5%, and 90% assumptions.
- **Consistency rule applicable:** For two equal arms of 389, the total is their arithmetic sum; matched design assumptions and allocation should not produce two totals without an explanation.
- **Calculation or logical comparison reproduced:** `389 + 389 = 778`, not 779. The support comparator's total reproduces exactly.
- **Necessary inputs available / exact missing inputs or definitions:** Both arm sizes, both totals, design direction, assumed rates, alpha, and power are supplied. Missing are version history or an allocation rule that could make 779 compatible with two groups of 389.
- **Source-grounded alternative interpretation:** The main article may preserve an earlier rounded total while retaining equal-arm counts from the published protocol, but no supplied version states a 390/389 allocation or another derivation of 779.
- **Direct observation versus inferred explanation:** The totals and arm sizes are directly printed. A carried-forward or rounded target is inferred.
- **Exact remaining human question:** Was the revised target 778 total with 389 per group, or 779 total with a different arm allocation, and which source wording is intended?

## C026 — Noninferiority bound/sign wording conflicts with its explanatory axis

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-002 PDF p.40, Figure 4](../../../joi180109supp1_prod.pdf#page=40) and [DOC-002 PDF p.42, lines 603-604](../../../joi180109supp1_prod.pdf#page=42).
- **Source printed value/text matched:** Yes — Figure 4 labels its axis `Difference in Efficacy (New Treatment Minus Active Control)`, places zero at the center and the noninferiority margin on the negative side, and shows noninferiority when the lower CI bound lies to the right of that margin.
- **Comparator printed value/text matched:** Yes — p.42 states that a 9% margin is clinically relevant and that noninferiority is demonstrated if the lower 95% CI boundary is `less than 9%`.
- **Consistency rule applicable:** A lower-bound noninferiority rule must use a signed margin and inequality consistent with the printed effect orientation and axis.
- **Calculation or logical comparison reproduced:** On the printed new-minus-control efficacy scale, the margin is negative and noninferiority requires the lower bound to exceed that negative margin. The text instead gives a positive 9% value with `less than`; the sign/inequality cannot be mapped to the figure without an unprinted scale transformation.
- **Necessary inputs available / exact missing inputs or definitions:** Axis orientation, margin side, and prose inequality are available. Missing are the exact mathematical effect definition, whether efficacy or mortality risk is used, the signed margin, and the prespecified inequality.
- **Source-grounded alternative interpretation:** The text could refer to a differently oriented mortality-risk difference for which +9% has another meaning, or it may omit a minus sign/change the inequality; the page does not state either mapping.
- **Direct observation versus inferred explanation:** The axis and sentence are direct observations. Translation, omitted sign, opposite scale, or inequality error are inferred explanations.
- **Exact remaining human question:** What exact signed effect measure and inequality defined the 9% margin, and how should the p.42 sentence map to Figure 4's new-minus-control axis?

## C027 — Primary-hypothesis intervention is labelled NIV while plans identify HFNO

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-002 PDF p.52, Type of comparisons](../../../joi180109supp1_prod.pdf#page=52) and [DOC-002 PDF p.104, Methodology of the statistical analysis](../../../joi180109supp1_prod.pdf#page=104).
- **Source printed value/text matched:** Yes — p.52 states `The primary hypothesis is non inferiority of the NIV in terms of 28-day mortality` and immediately says `HFNO is superior over standard oxygen or NIV` for secondary outcomes.
- **Comparator printed value/text matched:** Yes — p.104 states `The primary hypothesis is superiority of the NIV in terms of 28-day mortality` and immediately says `HFNO is superior over standard oxygen`; the supplied plans elsewhere define HFNO as the experimental intervention.
- **Consistency rule applicable:** The named experimental intervention in the primary hypothesis should match the intervention defined for the trial, unless the text explicitly equates NIV with HFNO or defines a separate comparison.
- **Calculation or logical comparison reproduced:** Exact label comparison gives `NIV` in both primary-hypothesis sentences versus `HFNO` in their adjacent intervention statements; no numerical calculation is required.
- **Necessary inputs available / exact missing inputs or definitions:** Both primary-hypothesis sentences and adjacent HFNO comparator statements are available. Missing is any definition equating NIV and HFNO in these passages or identifying NIV as the primary experimental arm.
- **Source-grounded alternative interpretation:** `NIV` could be a carried-forward generic or template label, while the repeated adjacent HFNO language identifies the intended intervention; the documents do not explicitly make that equivalence.
- **Direct observation versus inferred explanation:** The intervention-label difference is direct. Template carryover or synonymy is inferred.
- **Exact remaining human question:** Does `NIV` intentionally denote HFNO in either primary-hypothesis sentence, and if not, which intervention label was intended?

## C028 — Planned primary outcome alternates between day-28 vital status and hospital death

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes — [DOC-002 PDF p.54, Primary outcome](../../../joi180109supp1_prod.pdf#page=54), [DOC-002 PDF p.82, Original statistical plan](../../../joi180109supp1_prod.pdf#page=82), and [DOC-002 PDF p.104, Analysis of the primary outcome](../../../joi180109supp1_prod.pdf#page=104).
- **Source printed value/text matched:** Yes — each passage says all patients will be followed until day 28 and classified alive or dead.
- **Comparator printed value/text matched:** Yes — each passage then states that the relative risk of `hospital death` in the experimental versus control arm will be estimated.
- **Consistency rule applicable:** A fixed day-28 all-cause vital-status endpoint and hospital death are distinct endpoint/time labels unless the protocol explicitly defines them as equivalent.
- **Calculation or logical comparison reproduced:** Exact within-passage comparison reproduces the same label switch on all three pages: `alive or dead at day 28` followed by `hospital death`. No event-level calculation is possible from the supplied plans.
- **Necessary inputs available / exact missing inputs or definitions:** Repeated endpoint sentences, the day-28 horizon, and the relative-risk wording are available. Missing are the definition of hospital death, handling of discharge before day 28, deaths after discharge but before day 28, and any equivalence rule.
- **Source-grounded alternative interpretation:** `Hospital death` may be shorthand for day-28 death during the index admission, especially if all relevant deaths occurred before discharge, but the plans do not state that restriction or supply patient-level timing.
- **Direct observation versus inferred explanation:** The repeated endpoint-label switch is direct. Shorthand or empirical equivalence is inferred.
- **Exact remaining human question:** Is the planned estimand day-28 all-cause mortality, hospital mortality without a fixed horizon, or hospital death limited/censored at day 28, and how are post-discharge deaths handled?

## Completion accounting

- **Stable ID set rechecked:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020, C021, C022, C023, C024, C025, C026, C027, C028.
- **ID-set result:** 28/28 stable IDs have separate records; no extra or missing ID.
- **Direct-source location sets found:** 28/28.
- **Source printed evidence matched to the ledger:** 28/28.
- **Comparator evidence matched:** 28/28.
- **Arithmetic or logical comparison performed:** 28/28. Nineteen count/percentage calculations and seven other comparisons reproduce as stated in the ledger. The two reciprocal-ratio orientation comparisons (C023-C024) reproduce directionally and are compatible with hidden precision, but direct reciprocation of all displayed rounded values does not reproduce every displayed figure value; those exact limitations are recorded in the candidate sections.
- **Ledger-to-source transcription mismatches found during recheck:** None.
- **Ledger calculation overstatements found during recheck:** Two — C023 and C024 overstate exact reciprocal agreement after rounding the already-rounded displayed values. This is a mechanical recheck fact and does not alter either stable ID.
- **Remaining limitations:** Exact production denominators/rounding policies are absent for the 19 count/percentage candidates; unrounded interval/model details are absent for C017; intended denominator semantics are absent for C018; actual test output is absent for C022; figure reference-group definitions are absent for C023-C024; authoritative sample-target/version history is absent for C025; formal signed estimand definitions are absent for C026; and intervention/outcome definitions remain absent for C027-C028. These missing definitions leave the stated human questions open and do not alter any stable ID.
