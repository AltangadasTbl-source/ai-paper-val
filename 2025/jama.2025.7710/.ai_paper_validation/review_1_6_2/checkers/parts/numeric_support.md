# Numeric consistency checker: support shard

## Assigned scope and evidence

Scope: all 41 stable numeric families N201–N241 in DOC-004, the six-page REPORT supplement. Page 1 is the cover/table index; N201–N206 are page 2 sensitivity families; N207–N227 retain both site strata across pages 3–5; N228–N241 retain both Yes and No for both arms on page 6. Main N001–N100 are assigned to a separate numeric checker. This shard does not assign candidate IDs or adjudication fields.

Read completely: the numeric role contract, QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md and the run tooling record. Review inputs were the new support evidence map, normalized source native text A027, and reusable source-page images A031/A033/A035/A037/A039, all read afresh. No old candidate/checker/report conclusions or external sources were used. Every numeric row was checked against the page images and matched source-native layout.

The complete inventory is [numeric_support_inventory.md](../../relationships/parts/numeric_support_inventory.md). It retains every printed component, numerator, denominator, percentage, model label, estimate, interval and P value, with explicit count/percentage and population checks. Legacy derivative-engine provenance is unknown. No new extraction, rendering or OCR was needed.

## Rules and results

The review checked numerator/denominator percentages, missing-count additions to randomized infant headers, Yes/No totals against treated maternal headers, both site strata, subgroup totals, the two operative-birth decompositions, primary-composite site totals against the non-imputed sensitivity counts, and treatment-received denominators against untreated exclusions and the main-map flow context. All equalities and all 131 printed percentages reconcile under the specified half-unit rule.

For a count n and denominator d, the recomputed interval was [100 max(0,n−0.5)/(d+0.5),100(n+0.5)/(d−0.5)]. The interval of a one-decimal printed percentage p was [p−0.05,p+0.05]. Every such comparison had overlapping intervals, gap 0 and relative discrepancy 0. Reconciled checks are inventory records, not excluded observations.

eTable 2 estimates carry a relative-risk label and a log-binomial footnote. All finite displayed risk ratios are compatible with the ratio of the two printed risks; no row evidently substitutes an odds ratio or another measure. eTable 1 identifies GEE or indicator-adjusted GLM models, so those estimates are not asserted to be literal crude count ratios. eTable 3 prints no effect measure.

## Findings

No qualifying numeric finding was identified within the assigned shard. No F-NUM-101 or subsequent identifier is assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 eTable 1 page 2, N201–N203 ([source](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=2)) | The printed GEE relative risks 1.01, 1.62 and 0.96 differ from the literal crude ratios 85/87 = 0.97701, (14/1629)/(8/1637) = 1.75859 and 75/80 = 0.93750. The same table expressly identifies GEE log-binomial estimation with twin-clustering adjustment and identifies imputation for the first two rows. No statement identifies these estimates as crude. Aggregate count ratios therefore do not supply a reproduction rule for those fitted estimates. | MODEL_VERSUS_CRUDE |

## Completion and limitations

Completed: 41/41 assigned families; all six source pages accounted for; 158 count-denominator category pairs checked, including 131 printed percentages; both site rows for 21 site families; Yes and No in both arms for all 14 side-effect families. Findings: 0. Excluded observations: 1 consolidated modeled-versus-crude pattern. Scientific-coverage gaps: 0 within the assigned shard.

Limits: legacy extraction/rendering engine provenance is unknown; fitted GEE and imputed estimates cannot be regenerated from aggregate counts alone. Statistical estimate/interval/P-value compatibility, Fisher test reproduction and plan/report comparisons belong to the separately assigned specialists. The main flow and main-table relationship checks remain with the main numeric checker.

