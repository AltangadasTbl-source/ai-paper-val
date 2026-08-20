# Statistical Consistency Review — Pass 1

## Scope and method

Fresh statistical pass 1 independently reviewed all 29 canonical inferential relationships: S001--S017 (DOC-001) and S1001--S1012 (DOC-002--DOC-003). Evidence was confined to the supplied PDFs and their current fresh native/layout/render assets. The detailed, per-relationship `PASS_1_COMPLETE` record is in `statistics/relationship_inventory.md`.

Checks applied where source definitions supported them: point-estimate containment, endpoint ordering, risk-difference sign/direction, effect-measure/scale labels, count/denominator arithmetic, exact matched repetitions, and model/multiplicity labels. P/CI/test/statistic/SE reconstruction was deliberately not performed where the package did not define compatible inferential rules. In particular, the reported aRD CIs are transformed from logistic OR/CIs while reported P values are Hochberg-adjusted logistic-regression values; no common inversion rule, covariance, sidedness, degrees of freedom, variance estimator, or final decision rule was supplied.

## Complete relationship status

| S ID | Pass-1 status | Summary of direct result |
|---|---|---|
| S001 | PASS_1_COMPLETE | Sample-size arithmetic coherent; simulation inputs insufficient for power reconstruction. |
| S002 | PASS_1_COMPLETE | GEE/logistic, cluster, and covariate labels compatible; detailed estimating-equation definitions missing. |
| S003 | PASS_1_COMPLETE | OR-to-aRD conversion and scale labels agree across methods/Table 3. |
| S004 | PASS_1_COMPLETE | Final Hochberg versus planned Bonferroni not treated as same-rule contradiction. |
| S005 | PASS_1_COMPLETE | Main `<.001` summary compatible with eTable 2 `<.0001` values. |
| S006 | PASS_1_COMPLETE | aRD/CI containment, 89.1−80.2=8.9, direction and repetitions coherent. |
| S007 | PASS_1_COMPLETE | aRD/CI containment, −1.7 direction and adjusted-risk subtraction coherent. |
| S008 | PASS_1_COMPLETE | Corrected map label: 2.6-point estimate is NQI-only; interaction test separate. |
| S009 | PASS_1_COMPLETE | Combined contrast containment, sign, and 89.6−80.2=9.4 coherent. |
| S010 | PASS_1_COMPLETE | Containment, sign, and 74.1−70.4=3.7 coherent. |
| S011 | PASS_1_COMPLETE | Containment, sign, 12.4-point difference and repetitions coherent. |
| S012 | PASS_1_COMPLETE | Containment, sign, and 70.9−67.6=3.3 coherent. |
| S013 | PASS_1_COMPLETE | Containment, sign, 11.8-point difference and repetitions coherent. |
| S014 | PASS_1_COMPLETE | aRD/CI coherent; CI/P apparent tension not tested across transformed CI/Hochberg P. |
| S015 | PASS_1_COMPLETE | Containment, sign, 8.7-point difference and repetitions coherent. |
| S016 | PASS_1_COMPLETE | `not significant` versus printed p=.05 not mechanically contradictory without final threshold/unrounded P. |
| S017 | PASS_1_COMPLETE | No supplied race-stratified tests/estimates; qualitative inference not reconstructable. |
| S1001 | PASS_1_COMPLETE | Protocol/final GEE logistic model descriptions compatible at supplied detail. |
| S1002 | PASS_1_COMPLETE | Supine interaction presentation follows stated interaction-model branching at supplied detail. |
| S1003 | PASS_1_COMPLETE | Planned Bonferroni and final Hochberg are distinct rules; no same-rule comparison available. |
| S1004 | PASS_1_COMPLETE | No matched final secondary-model result supplied. |
| S1005 | PASS_1_COMPLETE | Planning totals coherent; 96% and 80% protocol values concern stated different contrasts. |
| S1006 | PASS_1_COMPLETE | Chi-square labels/cross-location bounds coherent; exact test implementation absent. |
| S1007 | PASS_1_COMPLETE | Imputation aR/aRD/P/interaction labels and covariate exception coherent. |
| S1008 | PASS_1_COMPLETE | Supine imputation estimates/ordered CIs/aR subtractions coherent. |
| S1009 | PASS_1_COMPLETE | Room-sharing imputation estimates/ordered CIs/aR subtractions coherent. |
| S1010 | PASS_1_COMPLETE | Soft-bedding imputation estimates/ordered CIs/aR subtractions coherent. |
| S1011 | PASS_1_COMPLETE | Pacifier imputation estimates/ordered CIs/aR subtractions coherent. |
| S1012 | PASS_1_COMPLETE | Frequency display rechecked; two independent table/figure issues emitted below. |

## Display-zero exclusion

**DISPLAY_ZERO_NOT_CANDIDATE count: 0.** No assigned source printed `P = 0`, `p = 0.000`, or an equivalent finite-precision display zero. Printed inequalities (`P < .001`, `<.0001`) are not display zeros and were reviewed as ordinary bounded P values. No tail probability was derived.

## Provisional candidates for coordinator registration

### STAT1-CAND-001 — eTable 5 room-sharing percentage does not reproduce its printed count and denominator

- **Potential primary category:** Numeric or arithmetic inconsistency.
- **Exact supplied-source locations:** DOC-003 (`joi170077supp2_prod.pdf`) PDF p. 9, eTable 5, “Sleep Location,” Breastfeeding/Breastfeeding control group, All stratum; matched repetition in DOC-001 (`jama_moon_2017_oi_170077.pdf`) PDF p. 7, Table 3, Room Sharing Without Bed Sharing, BF NQI/BF mHealth control arm.
- **Printed evidence:** DOC-003 p. 9 prints All-stratum room sharing as `N=291`, `205 (70.5%)`. DOC-001 p. 7 prints the matched control-arm result as `205/291 (70.4)`.
- **Rule:** A one-decimal percentage printed next to a count and denominator should reproduce the count divided by denominator to the displayed precision; the same matched result should agree across the two supplied displays after precision matching.
- **Calculation (diagnostic arithmetic):** `205 / 291 × 100 = 70.446735%`; conventional one-decimal rounding gives `70.4%`, agreeing with DOC-001 p. 7 and not DOC-003 p. 9’s `70.5%`.
- **Direct observation versus inference:** Directly observed are the two printed percentages and shared `205/291` count/denominator. The rounding conclusion is diagnostic arithmetic from those printed values; it does not infer a model or a P value.
- **Alternative supplied-source-grounded interpretation:** The DOC-003 table may have used an unreported percentage computation/rounding workflow or contain a table-production transcription discrepancy. No source supplies an alternative denominator for this All stratum.
- **Exact human question:** Does eTable 5’s `70.5%` represent an unreported denominator/underlying value, or should this matched `205/291` percentage be `70.4%` to one decimal?

### STAT1-CAND-002 — eTable 5 and eFigure give nonidentical age-threshold labels for the same race-stratified frequency display

- **Potential primary category:** Measure, label, or scale inconsistency.
- **Exact supplied-source locations:** DOC-003 (`joi170077supp2_prod.pdf`) PDF pp. 9--10, eTable 5 title; DOC-003 PDF p. 11, eFigure title and footnote directing readers to eTable 5 for sample sizes.
- **Printed evidence:** eTable 5 title says the displayed outcomes are “when infant was `≥60 days` of age.” The eFigure title says the graph is “when infant was `>60 days` of age”; its footnote directs readers to eTable 5 for data/sample sizes. Both display the control versus combined-intervention race/ethnicity frequencies.
- **Rule:** `≥60 days` includes an infant exactly 60 days old; `>60 days` excludes that boundary. When a table and its referenced graphical frequency display purport to describe the same result population, the inclusion boundary should be stated consistently or differentiated.
- **Calculation:** No numerical calculation applies; this is a direct population-boundary/label comparison.
- **Direct observation versus inference:** The nonidentical labels and the figure-to-table data reference are direct observations. Whether any 60-day-old infant was included, and whether data differ, is not supplied and is not inferred.
- **Alternative supplied-source-grounded interpretation:** The two labels may be a wording/rounding convention for one analysis population, or one source may describe a genuinely different inclusion boundary. The package does not give boundary counts or a figure-specific denominator.
- **Exact human question:** Which age-inclusion rule generated eFigure data, and should the eFigure and eTable 5 labels be harmonized or explicitly distinguished?

## Limitations and missing definitions

- No raw logistic-regression ORs, SEs, test statistics, covariance, degrees of freedom, working correlation, variance estimator, sidedness details beyond stated two-sided planning, or final interaction decision rule are supplied.
- The package specifies Hochberg-adjusted logistic P values and aRD CIs transformed from logistic OR/CIs, so equality between 95% CI null inclusion and adjusted P threshold was not presumed.
- Protocol Bonferroni statements were not assumed to define final Hochberg results. Planned versus final method wording was retained as context only.
- No candidate is based on finite-precision P-value display zero; none occurred in this scope.

## Counts

- **Relationships independently completed:** 29.
- **Provisional candidates:** 2.
- **DISPLAY_ZERO_NOT_CANDIDATE records:** 0.
- **Stable C IDs assigned:** 0 (coordinator-only registration step pending).
