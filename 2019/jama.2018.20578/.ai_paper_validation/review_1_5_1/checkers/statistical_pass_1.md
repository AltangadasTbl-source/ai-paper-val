# Statistical Consistency Review — Pass 1

## Scope

Independent pass 1 over all 21 stable inferential relationships in `statistics/relationship_inventory.md`: S001-S021. Direct-source evidence is the three supplied PDFs; 1.5.1 mapper files were used only to locate and organize source material. This pass does not assign candidate IDs, severity, validity, acceptance, correction, or any disposition. All proposals are Pending Human Adjudication.

## Per-relationship completion records

| S ID | Pass-1 checks completed | Result | Status |
|---|---|---|---|
| S001 | Model, effect-measure, population, adjustment, sidedness labels | Defined models and labels are internally differentiated; no printed mismatch | PASS_1_COMPLETE |
| S002 | HR containment/order, direction, repeated location, diagnostic P compatibility | Compatible at printed precision | PASS_1_COMPLETE |
| S003 | HR containment/order, reference direction, diagnostic P compatibility | Compatible at printed precision | PASS_1_COMPLETE |
| S004 | Direction, figure/test label, repeated-result identity | Distinct log-rank test; no numeric-band coordinates | PASS_1_COMPLETE |
| S005 | HR containment/order, direction, P compatibility, population distinction | Compatible at printed precision | PASS_1_COMPLETE |
| S006 | Eight estimate/CI containment/order, direction/narrative, P/CI definition | SP1-01 proposed; adjusted-P/CI equality not assumed | PASS_1_COMPLETE |
| S007 | Estimate/CI containment/order, scale direction, adjusted-P definition | Compatible; endpoint/P calculation diagnostic only | PASS_1_COMPLETE |
| S008 | Sixteen estimate/CI containment/order, estimand/label distinction | Compatible; no paired inputs/test definitions | PASS_1_COMPLETE |
| S009 | Four difference/CI containment/order, sign and proportion direction | Compatible; two exact-CI labels retained | PASS_1_COMPLETE |
| S010 | Missing-data model and pattern-mixture wording | No numerical vector to reconcile | PASS_1_COMPLETE |
| S011 | Sensitivity population/qualitative conclusion labels | No numerical estimates supplied | PASS_1_COMPLETE |
| S012 | Power inputs and revision statement | Missing alpha/control risk/calculation prevents reconstruction | PASS_1_COMPLETE |
| S013 | Multiplicity, sidedness, exploratory interpretation labels | Compatible; CI adjustment definition absent | PASS_1_COMPLETE |
| S014 | Bayesian/frequentist effect, scale, risk/rate, ARD direction labels | Compatible; no unprinted ARD formula or variance inferred | PASS_1_COMPLETE |
| S015 | 44 DIC/I2/model selections against printed rule | SP1-02 proposed; remaining 43 selections reproduce | PASS_1_COMPLETE |
| S016 | ARD interval order/sign, NNT/NNH display rule, rate/risk labels | Compatible; reciprocal checks diagnostic only | PASS_1_COMPLETE |
| S017 | Estimate/SE/t/P diagnostic compatibility | Rounded ratio compatible; df/sidedness absent | PASS_1_COMPLETE |
| S018 | HR/CrI containment/order/direction; finite-precision endpoint | Compatible; 1.004 footnote resolves `1.00` | PASS_1_COMPLETE |
| S019 | RR/CI containment/order, measure/direction, fixed/random and heterogeneity labels | SP1-03 proposed; no Q/df for exact heterogeneity P checks | PASS_1_COMPLETE |
| S020 | HR/CrI containment/order, sensitivity definitions, endpoint precision | Compatible; 0.9989 footnote resolves `1.00` | PASS_1_COMPLETE |
| S021 | Population, count, endpoint, duplicate/cross-location reconciliation | SP1-03 proposed; intended forest endpoint convention absent | PASS_1_COMPLETE |

## Candidate proposals for coordinator registration

### SP1-01 — HbA1c daily-rate unit label conflicts with the measure’s table scale

- **Proposed category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-001 p. 1, Abstract; p. 7, Secondary Outcomes; p. 8, Table 4 (`jama_flint_2019_oi_190079.pdf#page=1`, `#page=7`, `#page=8`).
- **Direct observation:** The abstract and result text print the HbA1c daily-rate estimate as `-0.0002 mg/dL` (95% CI, `-0.0021 to 0.0016`). Table 4 labels the same measured analyte `HbA1c, %`; p. 4 calls it hemoglobin A1c and the p. 8 table does not list it among the mg/dL analytes.
- **Consistency rule:** A repeated effect estimate should retain the scale/unit of its named measure. Percent HbA1c and mg/dL are different units.
- **Diagnostic reasoning:** Estimate/CI containment and the non-significant direction are otherwise compatible; this proposal concerns the unit label only.
- **Alternative source-grounded interpretation:** The daily-rate text may be a repeated unit-label typographical error rather than a numerical or model-result error.
- **Missing definition / human question:** Confirm the intended reporting unit for the HbA1c treatment-by-time coefficient and whether any transform was used before modeling.
- **Status:** Pending Human Adjudication.

### SP1-02 — Printed incident-cancer model label does not reproduce under the printed DIC/I2 rule

- **Proposed category:** Statistical reporting inconsistency.
- **Exact source locations:** DOC-003 p. 4, eMethods 2 model-selection rule; p. 5, eMethods 3 all-patients incident-cancer row (`joi180151supp2_prod.pdf#page=4`, `#page=5`).
- **Direct observation:** The rule says DIC differences within 3 are selected using fixed-effect I2, with random effects favored if `I2 >25%`. The all-patient incident-cancer row prints fixed DIC `27.06`, random DIC `27.93`, `I2=25%`, and selected model `random`.
- **Consistency rule:** With displayed DIC difference 0.87 (within 3) and displayed I2 equal to, not greater than, 25%, the printed `random` selection does not follow the printed strict `>25%` criterion. Fixed also has the lower displayed DIC.
- **Diagnostic reasoning:** The comparison uses only the stated decision rule and displayed table values; no external model convention is inferred.
- **Alternative source-grounded interpretation:** The displayed whole-percent I2 may be a rounded presentation of an unprinted value above 25%, or an unprinted selection rule may have been used.
- **Missing definition / human question:** Provide the unrounded incident-cancer fixed-effect I2 and the exact tie/rounding rule used for this row.
- **Status:** Pending Human Adjudication.

### SP1-03 — Total-stroke frequentist forest plot includes ASCEND despite supplied all-stroke exclusion label

- **Proposed category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-002 p. 7; DOC-003 p. 9 eTable 1, p. 16 eTable 4, and p. 24 eFigure 4 (`joi180151supp1_prod.pdf#page=7`, `joi180151supp2_prod.pdf#page=9`, `#page=16`, `#page=24`).
- **Direct observation:** eTable 1 says ASCEND is `Not included in analysis – only reports ischemic stroke` for all strokes. eTable 4 total stroke reports 12 studies and 73,883 aspirin/72,317 no-aspirin participants. The p. 24 frequentist total-stroke forest plot displays 13 rows, including `ASCEND 240/7740` versus `263/7740`, with totals 81,623/80,057. The difference from eTable 4 totals is 7,740 participants in each arm, exactly ASCEND’s displayed forest-plot total. DOC-002 explains ASCEND’s ischaemic-only primary-outcome definition as a reason to exclude it from a *primary cardiovascular outcome* sensitivity analysis.
- **Consistency rule:** The supplied all-stroke endpoint definition/exclusion label and the eTable 4 12-study population cannot be reconciled with the p. 24 total-stroke forest plot’s ASCEND inclusion without a separately stated endpoint convention.
- **Diagnostic reasoning:** This is a direct matched-source count/endpoint comparison, not a reconstruction of the forest model. The 7,740-per-arm difference is exact source arithmetic.
- **Alternative source-grounded interpretation:** The frequentist forest plot may intentionally analyze an ASCEND stroke endpoint under an unstated convention distinct from eTable 1/eTable 4; the cited source units do not state that convention.
- **Missing definition / human question:** Identify the endpoint definition and inclusion rule used for ASCEND in the frequentist total-stroke forest plot, and confirm whether the p. 24 row belongs under the `Total stroke` label.
- **Status:** Pending Human Adjudication.

## Display-zero record

- **DISPLAY_ZERO_NOT_CANDIDATE count:** 0. No relationship in S001-S021 presents `P = 0`, `p = 0.000`, or an equivalent display zero. Values such as P<.001 are not display zeros and were not converted to reconstructed tail probabilities.

## Limitations

- Exact P-value, test-statistic, SE, and interval reconciliation was restricted to relationships with supplied compatible definitions. No degrees of freedom, covariance, variance estimator, multiplicity sequence, denominator, model, sidedness, or estimand mapping was inferred from convention.
- All approximate calculations above are explicitly diagnostic and rely on rounded printed values; they are not replacement analyses.
- DOC-003 does not supply the unrounded I2 for SP1-02 or a stated frequentist total-stroke ASCEND endpoint convention for SP1-03.
