# Stable Candidate Ledger

All seven distinct quality-control candidates are **Pending Human Adjudication**. Stable IDs were assigned only after merging genuine duplicates across the numeric, statistical-pass-1, cross-source, and evidence-quality lanes. No candidate was deleted, ranked, assigned severity, or adjudicated. Similar production mechanisms did not cause distinct outcome rows to be merged.

## C001 — HbA1c daily-rate unit conflicts with the table scale

- **Category:** Measure, label, or scale inconsistency
- **Relationship provenance:** N008, N051, S006; numeric Proposal A; statistical-pass-1 SP1-01; cross-source Proposal 1.
- **Exact source locations:** [DOC-001 abstract, PDF p. 1](../../jama_flint_2019_oi_190079.pdf#page=1); [DOC-001 Results, PDF p. 7](../../jama_flint_2019_oi_190079.pdf#page=7); [DOC-001 Table 4, PDF p. 8](../../jama_flint_2019_oi_190079.pdf#page=8).
- **Direct observation:** The abstract and Results give the HbA1c daily-rate estimate as `-0.0002 mg/dL` with 95% CI `-0.0021 to 0.0016`; Table 4 labels HbA1c as `%`.
- **Consistency rule:** A named measure should retain a coherent unit/scale across matched occurrences; `%` and `mg/dL` are different units.
- **Calculation:** Direct label comparison; no rounding or numeric conversion reconciles the two units.
- **Alternative source-grounded interpretation:** The text unit may be a repeated carryover label from adjacent metabolic analytes; the package supplies no transformation supporting mg/dL for HbA1c.
- **Remaining human question:** What unit and any transform were used for the HbA1c treatment-by-time coefficient?
- **Status:** Pending Human Adjudication

## C002 — Total-cholesterol percentage-point difference does not reconcile with printed counts

- **Category:** Denominator, proportion, or total inconsistency
- **Relationship provenance:** N055; numeric Proposal B.
- **Exact source location:** [DOC-001 Table 5, PDF p. 9](../../jama_flint_2019_oi_190079.pdf#page=9), Total cholesterol row.
- **Direct observation:** Olanzapine is `9/64 (14.1%)`, placebo is `6/62 (9.7%)`, and the printed absolute unadjusted difference is `4.3` percentage points.
- **Consistency rule:** The displayed unadjusted between-arm percentage-point difference should reconcile with the printed arm counts/denominators or percentages.
- **Calculation:** `(9/64 - 6/62) x 100 = 4.385...`, which rounds to `4.4`; the printed percentages also give `14.1 - 9.7 = 4.4`, outside the ±0.05 one-decimal rounding band for `4.3`.
- **Alternative source-grounded interpretation:** A measure-specific evaluable denominator or unprinted calculation convention may have been used, although the printed row does not state one.
- **Remaining human question:** Which denominator and calculation produced `4.3` for this row?
- **Status:** Pending Human Adjudication

## C003 — LDL percentage-point difference does not reconcile with printed counts

- **Category:** Denominator, proportion, or total inconsistency
- **Relationship provenance:** N056; numeric Proposal C.
- **Exact source location:** [DOC-001 Table 5, PDF p. 9](../../jama_flint_2019_oi_190079.pdf#page=9), LDL row.
- **Direct observation:** Olanzapine is `9/64 (14.1%)`, placebo is `6/62 (9.7%)`, and the printed absolute unadjusted difference is `4.3` percentage points.
- **Consistency rule:** The displayed unadjusted between-arm percentage-point difference should reconcile with the printed arm counts/denominators or percentages.
- **Calculation:** `(9/64 - 6/62) x 100 = 4.385...`, which rounds to `4.4`; `14.1 - 9.7 = 4.4`, outside the ±0.05 one-decimal rounding band for `4.3`.
- **Alternative source-grounded interpretation:** A measure-specific evaluable denominator or unprinted calculation convention may have been used, although the printed row does not state one.
- **Remaining human question:** Which denominator and calculation produced `4.3` for the distinct LDL outcome row?
- **Status:** Pending Human Adjudication

## C004 — Incident-cancer model label does not follow the printed DIC/I2 rule

- **Category:** Statistical reporting inconsistency
- **Relationship provenance:** N062, S015; numeric Proposal D; statistical-pass-1 SP1-02.
- **Exact source locations:** [DOC-003 model-selection rule, PDF p. 4](../../joi180151supp2_prod.pdf#page=4); [DOC-003 all-patients incident-cancer row, PDF p. 5](../../joi180151supp2_prod.pdf#page=5).
- **Direct observation:** The rule selects random effects for DIC differences within 3 when fixed-effect `I2 >25%`. The row prints fixed DIC `27.06`, random DIC `27.93`, `I2=25%`, and model `random`.
- **Consistency rule:** Applying the printed strict threshold and displayed inputs should reproduce the displayed model selection.
- **Calculation:** DIC difference is `27.93 - 27.06 = 0.87`; displayed `25` is equal to, not greater than, 25, and the fixed model also has the lower displayed DIC.
- **Alternative source-grounded interpretation:** The unrounded I2 may exceed 25%, or an unprinted `>=25%` or other selection rule may have been applied.
- **Remaining human question:** What unrounded I2 and exact threshold/rounding convention governed this row?
- **Status:** Pending Human Adjudication

## C005 — Egger estimate and standard error do not reproduce the printed t statistic at displayed precision

- **Category:** Statistical reporting inconsistency
- **Relationship provenance:** S017; numeric Proposal E; statistical pass 1 recorded a conflicting diagnostic nonfinding; statistical pass 2 used the mechanical recheck interval, resolved that diagnostic disagreement, and retained the conditional mismatch.
- **Exact source location:** [DOC-003 eFigure 3, PDF p. 21](../../joi180151supp2_prod.pdf#page=21).
- **Direct observation:** The figure prints Egger estimate `-0.47`, standard error `0.77`, `t=-0.59`, and `P=.57`.
- **Consistency rule:** For the displayed coefficient test, the ordinary identity is `t = estimate / SE` unless a distinct statistic is defined.
- **Calculation:** `-0.47/0.77 = -0.6104`, rounding to `-0.61`. Nearest-hundredth rounding intervals give an attainable magnitude of about `0.600` to `0.621`, which cannot round to `0.59`.
- **Alternative source-grounded interpretation:** The t statistic may correspond to a distinct unreported parameter, variance estimate, or software-output field; ordinary rounding and ordinary two-decimal truncation do not bridge the displayed ratio.
- **Remaining human question:** Which unrounded coefficient/SE or distinct calculation generated `t=-0.59`?
- **Status:** Pending Human Adjudication

## C006 — ASCEND is excluded for all stroke but included in the total-stroke forest plot

- **Category:** Cross-document numeric inconsistency
- **Relationship provenance:** N068, S019, S021; numeric Proposal F; statistical-pass-1 SP1-03; cross-source Proposal 2.
- **Exact source locations:** [DOC-002 protocol change, PDF p. 7](../../joi180151supp1_prod.pdf#page=7); [DOC-003 eTable 1, PDF p. 9](../../joi180151supp2_prod.pdf#page=9); [DOC-003 eTable 4, PDF p. 16](../../joi180151supp2_prod.pdf#page=16); [DOC-003 eFigure 4, PDF p. 24](../../joi180151supp2_prod.pdf#page=24).
- **Direct observation:** eTable 1 says ASCEND is not included for all stroke because it reports only ischaemic stroke. eTable 4 reports 12 studies and totals `73,883/72,317`. The total-stroke forest plot reports 13 rows and `81,623/80,057`, including ASCEND `240/7,740` versus `263/7,740`; the same ASCEND row is also in the ischaemic-stroke panel.
- **Consistency rule:** A source-defined all-stroke analysis excluding ASCEND should not add its ischaemic-only row under a total-stroke label without stating a distinct endpoint convention.
- **Calculation:** `81,623 - 73,883 = 7,740` and `80,057 - 72,317 = 7,740`, exactly the displayed ASCEND denominators in each arm.
- **Alternative source-grounded interpretation:** The frequentist analysis may intentionally use ASCEND ischaemic stroke as a total-stroke proxy under an unstated endpoint convention distinct from the Bayesian table.
- **Remaining human question:** Was ASCEND intentionally included in the frequentist total-stroke panel, and what endpoint rule supports that inclusion?
- **Status:** Pending Human Adjudication

## C007 — Hyperlipidemia percentages reproduce only with the opposite arm denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Relationship provenance:** N029; numeric Proposal G; evidence-quality coverage repair.
- **Exact source location:** [DOC-001 Table 1, PDF p. 5](../../jama_flint_2019_oi_190079.pdf#page=5), Hyperlipidemia row and arm headers.
- **Direct observation:** The olanzapine column has header `n=64` and `18 (29.0)`; the placebo column has header `n=62` and `19 (29.7)`.
- **Consistency rule:** A within-arm percentage should reconcile with its own printed numerator and arm denominator.
- **Calculation:** `18/64 x 100 = 28.125%` (`28.1%`) and `19/62 x 100 = 30.645...%` (`30.6%`). The printed values instead exactly match the opposite denominators: `18/62 = 29.032...%` (`29.0%`) and `19/64 = 29.6875%` (`29.7%`).
- **Alternative source-grounded interpretation:** The row may contain a denominator reversal, or counts/percentages may have been transposed by a different production mechanism; the table states no row-specific denominators.
- **Remaining human question:** Which denominators were intended, and should the two percentages be recomputed from their own arm counts?
- **Status:** Pending Human Adjudication

## Merge record

- C001 merges the same unit conflict independently reported by all three lanes.
- C004 merges the numeric and statistical-pass-1 reports of the same DIC/model row and rule.
- C006 merges the numeric, statistical-pass-1, and cross-source reports of the same endpoint-membership/count identity.
- C002 and C003 remain separate because they are independently extractable outcome rows even though their printed vectors are identical.
- C005 remains registered because the displayed-precision interval calculation is reproducible; pass 2 resolved the pass-1 diagnostic disagreement using the mechanical recheck while leaving the candidate Pending Human Adjudication.
- C007 was appended without renumbering after the final evidence-quality audit found an N029 omission; it requires exact-source mechanical recheck before quality closure.
