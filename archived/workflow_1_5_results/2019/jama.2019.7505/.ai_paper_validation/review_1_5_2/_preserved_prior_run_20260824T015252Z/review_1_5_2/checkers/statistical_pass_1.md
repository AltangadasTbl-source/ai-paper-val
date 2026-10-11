# Statistical consistency review — pass 1

## Scope and method

Independent fresh-source pass over all 31 canonical inferential-statistical relationships, `S001` through `S031`, using only the current-run relationship inventories, extraction maps, and fresh native/layout text. Direct sources are DOC-001 (main article), DOC-002 (protocol), DOC-003 (protocol change history), DOC-004 (SAP), and DOC-005 (online supplement). No old audit output, web material, or external statistical convention was used as evidence.

For each relationship, I checked available point estimates against interval ordering/containment, sign and direction, effect-measure/scale/reference/population/time/contrast labels, repetitions, and inferential compatibility only where the supplied source defined a compatible model and rule. Calculations called **diagnostic approximations** below do not substitute for the reported analysis. In particular, no sidedness, degrees of freedom, covariance, variance estimator, multiplicity adjustment, denominator, model, or estimand mapping was inferred where not supplied.

Fresh native/layout extraction is partly column-scrambled for DOC-001 Table 2 on PDF p. 7 and Table 3 on PDF p. 9. Checks requiring a precise row-to-inferential-column association at those locations are therefore definition/evidence limited; no association was fabricated. No `P = 0`, `p = 0.000`, or equivalent display-zero result was found in this scope, so no `DISPLAY_ZERO_NOT_CANDIDATE` record was needed.

## Pre-ledger candidate observations

These are distinct candidate observations for coordinator registration. They have no stable `C` IDs and remain **Pending Human Adjudication**. They do not assign validity, severity, or a correction.

### P1-STAT-001 — Table 2 monitoring percentages do not reconcile with the printed count denominators

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [DOC-001, Table 2, PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8).
- **Printed evidence:** “Monitoring of neuromuscular function, No./total No. (%)” is `632/982 (64.9)` in the high-PEEP group and `651/984 (67.7)` in the low-PEEP group; the displayed absolute difference is `-1.8% (-6.0 to 2.4)`, `P=.40`.
- **Consistency rule:** A displayed percentage in a `No./total No. (%)` cell should equal the displayed numerator divided by the displayed denominator, subject to ordinary one-decimal rounding.
- **Calculation:** `632 / 982 × 100 = 64.358%` (64.4% to one decimal), not 64.9%; `651 / 984 × 100 = 66.159%` (66.2%), not 67.7%. The count-derived percentage difference is about `-1.80` percentage points, whereas the two printed parenthetical percentages differ by `-2.8` percentage points.
- **Direct observation versus inference:** The count, denominator, percentage, difference, interval, and P value are printed in one row. The calculation only tests the printed count/denominator-to-percentage identity; it does not infer the method used for the interval or P value.
- **Alternative source-grounded interpretation:** One or more printed count, denominator, or percentage values may be a transcription/display error; the source does not identify which field, if any, governs the calculation.
- **Human question:** Which source-table values were used for this row’s analysis and should the printed counts, denominators, percentages, and displayed difference be reconciled?

### P1-STAT-002 — Table 2 reversal percentages do not reconcile with the printed count denominators

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [DOC-001, Table 2, PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8).
- **Printed evidence:** “Reversal, No./total No. (%)” is `724/982 (74.3)` in the high-PEEP group and `723/984 (75.2)` in the low-PEEP group; the displayed absolute difference is `0.2% (-3.6 to 4.1)`, `P=.90`.
- **Consistency rule:** A displayed percentage in a `No./total No. (%)` cell should equal the displayed numerator divided by the displayed denominator, subject to ordinary one-decimal rounding.
- **Calculation:** `724 / 982 × 100 = 73.727%` (73.7% to one decimal), not 74.3%; `723 / 984 × 100 = 73.476%` (73.5%), not 75.2%. The count-derived percentage difference is about `0.25` percentage points, broadly matching the displayed `0.2%`; the two displayed parenthetical percentages instead differ by `-0.9` percentage points.
- **Direct observation versus inference:** The calculation assesses only the printed count/denominator-to-percentage identity and does not infer an interval or P-value model.
- **Alternative source-grounded interpretation:** One or more printed count, denominator, or percentage values may be a transcription/display error; no source definition identifies the intended calculation inputs.
- **Human question:** Which source-table values were used for this row’s analysis and should the printed counts, denominators, percentages, and displayed difference be reconciled?

### P1-STAT-003 — Repeated synthetic-colloid-use P values differ across the main table and eTable 3

- **Primary category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001, Table 2, PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); [DOC-005, eTable 3, PDF p. 24](../../../joi190055supp4_prod_16092.pdf#page=24).
- **Printed evidence:** DOC-001 reports synthetic-colloid use as `74 (7.5%)` versus `56 (5.7%)`, with `P=.09`. DOC-005 eTable 3 repeats `74 (7.5)` versus `56 (5.7)` for “Synthetic colloids, No. (%)” with `P value 0.10`; both tables name high PEEP `n=989` and low PEEP `n=987`.
- **Consistency rule:** Matched reproductions of the same population, contrast, binary result, and precision format should not give different printed P values unless the sources identify different tests or analysis definitions.
- **Calculation:** Direct comparison of the printed fields: `.09 ≠ .10`. No tail probability was reconstructed.
- **Direct observation versus inference:** The repeated counts, group sizes, and differing P displays are direct observations. The supplied tables do not state a table-specific testing rule that explains whether different tests were deliberately used.
- **Alternative source-grounded interpretation:** The two tables may use distinct, undocumented tests or one P display may be a transcription/rounding discrepancy.
- **Human question:** Were different tests intentionally used for this matched synthetic-colloid-use comparison, and if not, which printed P value corresponds to the intended analysis?

### P1-STAT-004 — eFigure 11 body text labels the displayed mortality result as extra-pulmonary complications

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-005, eFigure 11, PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41); [DOC-001, Table 3, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- **Printed evidence:** eFigure 11 is titled “Probability of death in the first 5 postoperative days” and gives `0.5%` versus `0.3%` and “hazard ratio for 5-day mortality, `1.67` (95% CI `0.40 to 6.97`; `P=0.484`)”; its body sentence calls those rates “postoperative extra-pulmonary complications.” DOC-001 Table 3 reports mortality at 5 days as `5 (0.5)` versus `3 (0.3)`, `HR 1.67 (0.40 to 6.97)`, `P=.48`.
- **Consistency rule:** An outcome label in a figure body must agree with the figure title and the matched outcome/statistics at the same time window.
- **Calculation:** Logical identity comparison, not an inferential reconstruction: the eFigure title, hazard-ratio label, event rates, and matched main-table result identify 5-day mortality; the body sentence instead names postoperative extra-pulmonary complications.
- **Direct observation versus inference:** The conflicting labels and matched numerical mortality result are printed. The conclusion is limited to the label mismatch, not an assertion about which analytic data were used.
- **Alternative source-grounded interpretation:** The body phrase may be a carryover label from eFigure 10; the supplied sources do not state the intended final wording.
- **Human question:** Should the eFigure 11 body outcome label be reconciled with its death title and its mortality HR/result?

## Relationship-level pass-1 records

| ID | PASS_1_COMPLETE record | Candidate key(s) | Definitions/limitations retained |
|---|---|---|---|
| S001 | Sample-size chronology, power, target RR, dropout, and re-estimation were compared across main article, protocol, and change history. Original 748 and revised 1912 plus 5%=2013 are coherently distinguished as planning stages; final alpha .044 agrees with interim plan. No candidate. | None | No recalculation of trial power or spending function: full design inputs and implementation are not supplied. |
| S002 | Primary PPC RR `.93` (`.83–1.04`), difference `-2.3%` (`-5.9 to 1.4`), and `P=.23` have ordered intervals containing their null values and direction agrees with high-versus-low counts/narrative. A log-scale diagnostic approximation from the RR CI gives a two-sided P near `.21`, broadly near `.23`. No candidate. | None | The source does not give a complete estimator/variance/estimand mapping for converting displayed event counts to the reported RR; raw-ratio comparisons are diagnostic only. |
| S003 | Secondary RR/t-test/HR and exploratory-alpha definitions were read against the SAP. No incompatible observed value is assigned in this relationship. No candidate. | None | Continuous Table 2 testing rule and individual result-to-model mapping are not fully supplied. |
| S004 | Tidal-volume and PEEP differences have ordered endpoints containing each displayed estimate; signs agree with the arm means and all PEEP differences/directions. No candidate. | None | DOC-001 p. 7 column order is scrambled in fresh extraction; continuous-outcome test/variance rule is not stated, so P/CI checks are limited to direct display compatibility. |
| S005 | Recoverable peak/driving pressure, respiratory-rate, FIO2, SpO2, CO2, heart-rate, and MAP differences have ordered intervals containing their displayed estimates and signs agree with group values. No candidate. | None | Same DOC-001 p. 7 column-scrambling and absent compatible continuous-outcome inference rule. |
| S006 | Procedure comparisons were checked for containment/order/direction. The epidural and other recoverable values are directionally coherent. Two count/denominator-to-percentage inconsistencies in monitoring and reversal meet the candidate threshold. | P1-STAT-001; P1-STAT-002 | No model was inferred for the Table 2 intervals/P values. |
| S007 | Primary PPC repetitions across abstract, Key Points, narrative, Table 3, and Figure 2 match `211/989` vs `233/987`, difference `-2.3%`, RR `.93` (`.83–1.04`), and `P=.23`; interval/null and direction checks are coherent. No candidate. | None | The supplied RR method does not state enough estimator detail to equate the reported RR mechanically to the crude count ratio; that comparison remains diagnostic only. |
| S008 | Mild respiratory-failure estimate `-1.9%` (`-5.1 to 1.2`), RR `.92` (`.80–1.05`), and `P=.22` are repeated coherently between narrative/table evidence; intervals contain null and direction agrees. No candidate. | None | Same unspecified RR estimand/variance mapping; Table 3 serialized-column limitation applies to non-narrative fields. |
| S009 | Pleural-effusion estimate `2.2%` (`.7–3.8`), RR `1.35` (`1.14–1.62`), and `P=.005` match narrative/table evidence; intervals exclude the respective nulls and direction agrees. No candidate. | None | Same unspecified RR estimator/variance mapping. |
| S010 | Remaining primary-component fields were checked only where row identity survived extraction. Displayed intervals are ordered and contain their linked estimates when recoverable. No candidate. | None | DOC-001 p. 9 column serialization prevents reliable row-level RR/CI/P association for all components; no association was invented. |
| S011 | Recoverable secondary/postoperative/adverse-event fields show no direct cross-location contradiction. No candidate. | None | DOC-001 p. 9 column serialization prevents complete row-level interval/P/statistic association; test rules are not supplied for every row. |
| S012 | Desaturation rescue, vasoactive-use, and 5-day-mortality effects have ordered intervals containing their estimates; RR/HR directions agree with displayed contrasts. Mortality HR `1.67` (`.40–6.97`) and P `.48` are compatible by diagnostic log-scale approximation. No candidate. | None | The report does not provide a complete binary-RR estimator mapping; the Cox model is named only for mortality. |
| S013 | All subgroup RRs have ordered intervals containing their estimates and direction agrees with the listed subgroup risks; interaction P values are directly displayed. No candidate. | None | Interaction-model coefficients, covariance, and sidedness are not supplied; no mechanical interaction-P reconstruction was attempted. |
| S014 | Narrative statements on ITT/per-protocol and adjustment/sensitivity analyses agree in direction with eTables 8–9 (no claimed statistically significant primary benefit). No candidate. | None | Narrative provides no numerical effect for some claims; “similar” is not a mechanically defined statistic. |
| S015 | Protocol/change-history and main-article sample-size/alpha/RR/power records were reconciled as planned versions, not concurrent observed analyses. No candidate. | None | Interim implementation outputs and complete power-calculation inputs are absent. |
| S016 | Protocol gamma-spending schedule, look sizes, and stated efficacy/futility P boundaries were read as planned monitoring definitions; final `.044` matches the main/SAP primary alpha. No candidate. | None | No observed interim test statistics, spending software output, or final analysis mapping is supplied. |
| S017 | SAP primary RR/CI/chi-square and alpha `.044` match the main article’s stated primary analysis. No candidate. | None | The phrase “Wald likelihood-ratio approximation” does not supply all estimator/variance details needed for a mechanical count-to-RR reconciliation. |
| S018 | SAP secondary/subgroup/sensitivity methods, including the stated 99.58% Bonferroni CI, were checked. `1 - .05/12 = .99583`, consistent with 99.58% display. No candidate. | None | No component-specific adjusted CI results are mapped in a form permitting a full method-to-result check. |
| S019 | ARISCAT ORs have ordered CIs containing estimates; coefficients exponentiate to displayed ORs within printed precision (diagnostic checks). No candidate. | None | Coefficient rounding and the original model covariance are not supplied; calculations are diagnostic. |
| S020 | eTable 3 P values were checked as displayed. The synthetic-colloid-use repetition conflicts with DOC-001 Table 2 and meets the candidate threshold. No other exact matched inference contradiction was found. | P1-STAT-003 | eTable 3 does not state its row-specific test; no P calculation was reconstructed. |
| S021 | eTable 4 vasoactive-use P `.02` matches the main-table vasoactive-use P `.02`; other drug/dose P values have no supplied compatible test rule for reconstruction. No candidate. | None | Table-specific test type, distributional rule, and denominator/model details are not supplied. |
| S022 | eTable 5 P values were reviewed for matching labels/population; no same-result conflicting repetition or internally supplied compatible test rule was found. No candidate. | None | Test types and multiplicity handling are unstated. |
| S023 | eTable 6 categorical and pressure P values were reviewed for label, scale, population, and repeated-value conflicts. No candidate. | None | Test types and any multilevel-category test definitions are unstated. |
| S024 | eTable 7 daily VAS values/P values were reviewed against the main narrative’s “comparable” direction. No direct contradiction; no candidate. | None | Repeated-measures method, missing-data handling for daily observed N, covariance, and row-specific test definition are unstated. |
| S025 | Per-protocol effect estimates/CIs/P values are ordered and contain their estimates; PPC P `.17` is directionally coherent with the main narrative. No candidate. | None | eTable 8 uses generic “Effect Estimate”; the source does not identify it as RR or OR for each row, so crude ratio or P/CI reconstruction was not used as a contradiction. |
| S026 | Sensitivity-model labels and point/interval ordering were checked. Random-effect, proportional-odds, and common-GEE estimates have ordered CIs containing their estimates; diagnostic P approximations are broadly compatible. Average-relative-effect `.99` (`.94–1.05`), `P=.98` is retained as a definition-limited diagnostic discrepancy, not a candidate. | None | Although the GEE footnote names a model, it does not define the CI-to-P test linkage, variance/covariance, transformation, or averaged estimand needed to call the diagnostic approximation a contradiction. |
| S027 | eFigures 1–7 labels define mean/95% CI displays and time-by-group mixed-model P values; no exact plotted values/P values are extractable for testing. No candidate. | None | Fresh text has no readable plotted coordinates/P values on DOC-005 pp. 31–37. |
| S028 | Time-to-PPC HR `.88` (`.73–1.06`), `P=.190`, has an ordered interval containing 1 and a point below 1; diagnostic log-scale P is near `.18`, compatible with displayed precision. No candidate. | None | Schoenfeld-residual P `.05` tests a different proportional-hazards assumption; no cross-test equivalence was inferred. |
| S029 | Time-to-severe-PPC HR `.85` (`.66–1.09`), `P=.197`, has an ordered interval containing 1; diagnostic log-scale P is near `.20`, compatible with display. No candidate. | None | Schoenfeld-residual P `.28` is a distinct assumption test; full Cox variance details are absent. |
| S030 | Time-to-PEPC HR `1.12` (`.89–1.39`), `P=.314`, has ordered endpoints containing 1; diagnostic log-scale P is near `.32`, compatible with display. No candidate. | None | Schoenfeld-residual P `.67` is a distinct assumption test; full Cox variance details are absent. |
| S031 | Mortality HR `1.67` (`.40–6.97`), `P=.484`, is internally compatible by diagnostic log-scale approximation and matches DOC-001 mortality values. The eFigure body outcome label conflicts with its title/statistic/main-table match and meets the candidate threshold. | P1-STAT-004 | Schoenfeld-residual P `.14` is a distinct test; no equivalence with the mortality-effect P was inferred. |

## Explicit completion markers

- S001 — `PASS_1_COMPLETE`
- S002 — `PASS_1_COMPLETE`
- S003 — `PASS_1_COMPLETE`
- S004 — `PASS_1_COMPLETE`
- S005 — `PASS_1_COMPLETE`
- S006 — `PASS_1_COMPLETE`
- S007 — `PASS_1_COMPLETE`
- S008 — `PASS_1_COMPLETE`
- S009 — `PASS_1_COMPLETE`
- S010 — `PASS_1_COMPLETE`
- S011 — `PASS_1_COMPLETE`
- S012 — `PASS_1_COMPLETE`
- S013 — `PASS_1_COMPLETE`
- S014 — `PASS_1_COMPLETE`
- S015 — `PASS_1_COMPLETE`
- S016 — `PASS_1_COMPLETE`
- S017 — `PASS_1_COMPLETE`
- S018 — `PASS_1_COMPLETE`
- S019 — `PASS_1_COMPLETE`
- S020 — `PASS_1_COMPLETE`
- S021 — `PASS_1_COMPLETE`
- S022 — `PASS_1_COMPLETE`
- S023 — `PASS_1_COMPLETE`
- S024 — `PASS_1_COMPLETE`
- S025 — `PASS_1_COMPLETE`
- S026 — `PASS_1_COMPLETE`
- S027 — `PASS_1_COMPLETE`
- S028 — `PASS_1_COMPLETE`
- S029 — `PASS_1_COMPLETE`
- S030 — `PASS_1_COMPLETE`
- S031 — `PASS_1_COMPLETE`

## Pass-1 totals and handoff

- **Canonical relationships completed:** 31/31 (`S001`–`S031`), each with an explicit `PASS_1_COMPLETE` record above.
- **Distinct pre-ledger candidate observations:** 4 (`P1-STAT-001` through `P1-STAT-004`).
- **Display-zero findings:** 0; no candidate was created from P-value formatting.
- **Key limitations:** partially scrambled fresh native/layout table columns on DOC-001 pp. 7 and 9; unavailable plotted numerical values for DOC-005 pp. 31–37; missing row-specific estimator, test, variance/covariance, and estimand definitions where explicitly noted.
- **Required pass-2 scope:** revisit all 31 S IDs; use the complete cross-lane candidate ledger and mechanical recheck facts, and re-evaluate the four provisional observations after stable candidate registration.
