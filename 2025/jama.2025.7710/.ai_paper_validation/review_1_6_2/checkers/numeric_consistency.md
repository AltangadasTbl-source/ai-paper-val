# Numeric consistency review

## Scope and method

Mandatory main numeric checker stage. Reviewed every assigned canonical relationship N001–N100 in DOC-001 REPORT, all physical PDF pages 1–11 mapped by the main mapper. All 100 relationship records are complete in [numeric relationship inventory](../relationships/numeric_relationship_inventory.md). Support numeric N201–N241 belongs to the disjoint support numeric checker and is not duplicated here. Read QUALITY_CONTROL_SCOPE.md, the complete 1.6.2 review contract, and the numeric role contract before checking. Used only supplied sources and current source-linked maps/text, without old candidate/report conclusions or web evidence.

Applied participant flow, randomized/received/available-outcome/followed-up counts, numerator/denominator/percentage identity, mutually exclusive row and subgroup partitions, matched primary counts, outcome-specific maternal/infant units, and RR versus other measure identity. Applied the half-unit input interval rule before the relative discrepancy threshold 0.05. All 155 explicit percentage pairs in the assigned numeric rows reconcile under that rule; complete interval calculations appear in the inventory. Continuous descriptive summaries were checked for scale, mean/median identity, interval ordering and repeated-copy identity where available, without assuming raw observations.

Main source-native and layout derivatives are current-run PyMuPDF 1.26.4 CPU extractions. The [direct Figure 1 source](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4) was additionally rendered with package-local pdf_tools.py, PyMuPDF 1.26.4, 200 dpi, CPU to preprocessing/numeric_main/page-4.png and inspected visually. No new OCR was required.

## Reconciled high-level checks

The 100 individual records include reconciled checks; they are not excluded observations. Important count bridges are:
- Registered3748−excluded491=randomized3257=1626+1631 women.
- Infant randomized totals1634=1626+8 and1641=1631+10; total3275.
- As-randomized receipt1552+74=1626 and1555+76=1631. Nonreceipt reason sums equal74 and76.
- Complete/future consent withdrawal4+2+1+2=9; available women3257−9=3248 and infants3275−9=3266. Lost-follow-up4+10=14;3266−14=3252 followed infants. Two placebo infants have incomplete primary data;3252−2=3250 primary infants.
- SC followed1634−4−4−1=1625; placebo followed1641−2−10−2=1627, then placebo primary1627−2=1625.
- Assignment-dose totals902+558+94=1554 and914+549+92=1555. The former includes two SC-assigned participants receiving placebo; actual treatment counts1552 SC and1557 placebo total3109. Untreated3257−3109=148. This matches the actual-treatment safety definition and the REPORT supplement [eTable 3](../../../joi250034supp3_prod_1750956984.12018.pdf#page=6).
- Ethnicity, parity, previous birth method, conception, recruitment site, infant sex, birth mode, labor onset and analgesia partitions each sum to their own printed denominator.
- Primary site events16+67=83 and24+60=84; site denominators883+742=1625 and887+738=1625. All six Figure 2 subgroup partitions also reproduce83/1625 and84/1625.
- Main RR labels are supported by log-binomial GEE/GLM descriptions and subgroup or maternal risk-ratio computations. Mean differences in hours are distinct from the Table 2 medians in hours. No evidenced different effect-measure identity emerged.

## Findings

No qualifying finding was emitted from the assigned main numeric scope. This reflects full 100-relationship coverage, not a finding-count target. No candidate IDs or adjudication labels are assigned here.

## Excluded observations

Only apparent issues decided against emission are listed. Reconciled counts and ordinary differences between distinct outcomes are retained solely in the inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT [abstract p.1](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=1), [demographics p.4](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4), [Table 1 p.5](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=5); N004/N023/N028/N032 | Placebo Australia/New Zealand53.6% in abstract/narrative versus53.7% in Table 1, and Pacific Islander3.2% in narrative versus3.3% in Table 1. Half-unit percentage intervals touch at53.65 and3.25 respectively; gap0, relative discrepancy0. The narrative randomized denominator1631 and table known-ethnicity denominator1629 also reconcile their corresponding percentages. One consolidated display-precision pattern. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [abstract p.1](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=1), [p.4](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4), [p.6](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=6), [site narrative p.7](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=7) compared with Figure 1/Table 3/Figure 2 infant counts; N019/N021/N093/N094 and S001/S021 | The narrative sometimes calls the1625/1629/1637 and883/887/742/738 neonatal outcome contributors women. The displayed randomized women/infants and twin counts, infant composite definition, infant follow-up boxes, and infant headers identify the numerical unit immediately. Every event and contributor value is retained. This is a single women/infants wording pattern, without a changed printed number or ambiguous extraction population. | TERMINOLOGY_OR_WORDING |
| REPORT [Table 3 p.7](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=7), [Figure 2/Table 4 p.8](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=8), methods [p.3](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=3); S021/S024–S032/S035/S048–S055 | Main GEE risk ratios need not equal crude count ratios: for example primary1.02 versus83/84=0.9881, encephalopathy0.94 versus1.00, seizures1.87 versus2.00, pH2.28 versus(12/1629)/(5/1637)=2.4118. The report explicitly labels its multifetal-clustering model. Those comparisons do not demonstrate a substituted odds ratio or a contradictory crude/unadjusted label. One modeled-versus-crude pattern. | MODEL_VERSUS_CRUDE |

## Limitations and handoff

Scope 100/100 main N relationships; 155 explicit count-percentage pairs checked; 0 findings; 3 excluded-observation patterns. Raw observations and model fit objects are not supplied; this prevents independent reconstruction of descriptive means/medians/dispersion and every GEE coefficient from aggregates. These absent inputs are not themselves findings. No source-coverage limitation remains in this assigned numeric scope. Statistical interval/test consistency and planned-versus-reported design are covered by their mandatory independent lanes; the inventory cross-references the mapped S relationships without repeating those reviews.

Artifacts: relationships/numeric_relationship_inventory.md; checkers/numeric_consistency.md. Unique fresh derivative: preprocessing/numeric_main/page-4.png (PyMuPDF 1.26.4, CPU, 200 dpi).

# Numeric consistency checker: support shard

## Assigned scope and evidence

Scope: all 41 stable numeric families N201–N241 in DOC-004, the six-page REPORT supplement. Page 1 is the cover/table index; N201–N206 are page 2 sensitivity families; N207–N227 retain both site strata across pages 3–5; N228–N241 retain both Yes and No for both arms on page 6. Main N001–N100 are assigned to a separate numeric checker. This shard does not assign candidate IDs or adjudication fields.

Read completely: the numeric role contract, QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md and the run tooling record. Review inputs were the new support evidence map, normalized source native text A027, and reusable source-page images A031/A033/A035/A037/A039, all read afresh. No old candidate/checker/report conclusions or external sources were used. Every numeric row was checked against the page images and matched source-native layout.

The complete inventory is [numeric_support_inventory.md](../relationships/parts/numeric_support_inventory.md). It retains every printed component, numerator, denominator, percentage, model label, estimate, interval and P value, with explicit count/percentage and population checks. Legacy derivative-engine provenance is unknown. No new extraction, rendering or OCR was needed.

## Rules and results

The review checked numerator/denominator percentages, missing-count additions to randomized infant headers, Yes/No totals against treated maternal headers, both site strata, subgroup totals, the two operative-birth decompositions, primary-composite site totals against the non-imputed sensitivity counts, and treatment-received denominators against untreated exclusions and the main-map flow context. All equalities and all 131 printed percentages reconcile under the specified half-unit rule.

For a count n and denominator d, the recomputed interval was [100 max(0,n−0.5)/(d+0.5),100(n+0.5)/(d−0.5)]. The interval of a one-decimal printed percentage p was [p−0.05,p+0.05]. Every such comparison had overlapping intervals, gap 0 and relative discrepancy 0. Reconciled checks are inventory records, not excluded observations.

eTable 2 estimates carry a relative-risk label and a log-binomial footnote. All finite displayed risk ratios are compatible with the ratio of the two printed risks; no row evidently substitutes an odds ratio or another measure. eTable 1 identifies GEE or indicator-adjusted GLM models, so those estimates are not asserted to be literal crude count ratios. eTable 3 prints no effect measure.

## Findings

No qualifying numeric finding was identified within the assigned shard. No F-NUM-101 or subsequent identifier is assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 eTable 1 page 2, N201–N203 ([source](../../../joi250034supp3_prod_1750956984.12018.pdf#page=2)) | The printed GEE relative risks 1.01, 1.62 and 0.96 differ from the literal crude ratios 85/87 = 0.97701, (14/1629)/(8/1637) = 1.75859 and 75/80 = 0.93750. The same table expressly identifies GEE log-binomial estimation with twin-clustering adjustment and identifies imputation for the first two rows. No statement identifies these estimates as crude. Aggregate count ratios therefore do not supply a reproduction rule for those fitted estimates. | MODEL_VERSUS_CRUDE |

## Completion and limitations

Completed: 41/41 assigned families; all six source pages accounted for; 158 count-denominator category pairs checked, including 131 printed percentages; both site rows for 21 site families; Yes and No in both arms for all 14 side-effect families. Findings: 0. Excluded observations: 1 consolidated modeled-versus-crude pattern. Scientific-coverage gaps: 0 within the assigned shard.

Limits: legacy extraction/rendering engine provenance is unknown; fitted GEE and imputed estimates cannot be regenerated from aggregate counts alone. Statistical estimate/interval/P-value compatibility, Fisher test reproduction and plan/report comparisons belong to the separately assigned specialists. The main flow and main-table relationship checks remain with the main numeric checker.

