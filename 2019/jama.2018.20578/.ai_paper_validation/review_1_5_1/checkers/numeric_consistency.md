# Numeric Consistency Check

## Scope, method, and count

This checker reviewed all 68 canonical numeric/reporting relationships in `relationships/numeric_relationship_inventory.md`, including relevant numeric components of the mapped `MS001`-`MS013` and `SS001`-`SS008` inferential relationships. Direct source PDFs were used for every proposal. Arithmetic used the printed inputs; a percentage printed to one decimal has a display tolerance of plus or minus 0.05 percentage point, and a value printed to two decimals has a display tolerance of plus or minus 0.005 unless a source footnote gives an exact value.

Completed nonfinding coverage includes: DOC-001 Figure 1 branch and phase totals; Table 1 category and percentage checks other than Proposal G; Tables 2-3 denominator, range, and nonexclusive-event checks; Table 4 missing-data/paired-change caveat; Table 5 triglyceride and glucose differences; DOC-003 study-flow and risk-bias totals; ARD/NNT/NNH rounding; rate-versus-risk labels; eTable 4 endpoint precision; and eTable 6's exact 0.9989 upper endpoint. No proposal is based only on a finite-precision display-zero P value.

Seven distinct candidate proposals are below. They are proposals only, all **Pending Human Adjudication**. No stable candidate ID, severity, validity, or disposition is assigned here.

## Proposal A — HbA1c daily-rate unit differs from the main table's stated scale

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-001 p. 1](../../../jama_flint_2019_oi_190079.pdf#page=1), abstract Results; [DOC-001 p. 7](../../../jama_flint_2019_oi_190079.pdf#page=7), secondary-outcomes text; [DOC-001 p. 8](../../../jama_flint_2019_oi_190079.pdf#page=8), Table 4 header.
- **Printed inputs:** The abstract and Results text both print "HbA1c levels (-0.0002 mg/dL; 95% CI, -0.0021 to 0.0016)" (with brackets and adjusted P in Results). Table 4 labels the measure "HbA1c, %."
- **Rule and reproducible check:** A repeated estimate for the same analyte should retain its measure scale. HbA1c is explicitly displayed in the article's Table 4 on a percentage scale, whereas the abstract appends `mg/dL`, the unit used for the adjacent lipid/glucose measures.
- **Calculation and tolerance:** This is a direct unit comparison, not a conversion. No rounding tolerance changes `%` into `mg/dL`.
- **Direct observation versus inference:** Direct observation is the two printed unit labels and the same -0.0002 interval. The inference is that the abstract's `mg/dL` label may be a carryover label rather than the intended unit.
- **Alternative source-grounded interpretations:** The repeated `mg/dL` labels may be carryover from adjacent analytes, while the intended modeled scale may be percentage points per day; the supplied pages state no transform supporting mg/dL for HbA1c.
- **Quality-control relevance:** A unit copied as `mg/dL` rather than percentage can corrupt outcome-scale extraction and any comparison of metabolic trajectory effects.
- **Exact human question:** Was the abstract's `mg/dL` unit intentionally assigned to the HbA1c daily-rate estimate, or should the estimate be labeled on the percentage scale used in Table 4?

## Proposal B — Total-cholesterol incident-value difference does not reconcile with its printed counts and percentages

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [DOC-001 p. 9](../../../jama_flint_2019_oi_190079.pdf#page=9), Table 5, Total cholesterol row.
- **Printed inputs:** Olanzapine: `9 (14.1)` of `n = 64`; placebo: `6 (9.7)` of `n = 62`; printed absolute unadjusted difference: `4.3 (-8 to 17.2)` percent.
- **Rule and reproducible calculation:** For the printed arm counts and header denominators, the absolute percentage-point difference is `(9 / 64 - 6 / 62) x 100 = 4.385...` percentage points. The separately printed percentages give `14.1 - 9.7 = 4.4` percentage points.
- **Tolerance:** With integer counts and the stated arm denominators, the exact raw difference rounds to `4.4` at one decimal. The printed `4.3` differs by about 0.085 percentage point, exceeding the plus or minus 0.05 percentage-point one-decimal rounding tolerance.
- **Direct observation versus inference:** The counts, denominators, percentages, and `4.3` are direct observations. The inference is that either the displayed difference, an undisclosed analysis denominator, or an unprinted calculation convention differs from the stated raw inputs.
- **Alternative source-grounded interpretations:** The table may have used a measure-specific evaluable denominator or a statistical calculation with unprinted handling of missing data, even though the row percentages agree with the header denominators. The printed table does not state such an alternative denominator or adjustment.
- **Quality-control relevance:** The difference is the table's explicit between-group effect summary; a discordant point value can be copied into evidence extraction or meta-analytic data abstraction.
- **Exact human question:** What denominator and calculation produced the printed `4.3` percentage-point total-cholesterol difference, given the displayed `9/64` and `6/62` counts?

## Proposal C — LDL incident-value difference repeats the same nonreconciling point estimate

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [DOC-001 p. 9](../../../jama_flint_2019_oi_190079.pdf#page=9), Table 5, LDL row.
- **Printed inputs:** Olanzapine: `9 (14.1)` of `n = 64`; placebo: `6 (9.7)` of `n = 62`; printed absolute unadjusted difference: `4.3 (-8 to 17.2)` percent.
- **Rule and reproducible calculation:** `(9 / 64 - 6 / 62) x 100 = 4.385...` percentage points, which rounds to `4.4`; likewise, `14.1 - 9.7 = 4.4` percentage points.
- **Tolerance:** The printed `4.3` is about 0.085 percentage point from the raw-count difference, outside one-decimal rounding tolerance of plus or minus 0.05 percentage point.
- **Direct observation versus inference:** Direct observation is the repeated count/denominator/percentage vector and its row-specific printed difference. The inference is that this row may share a production or calculation issue with Proposal B, but it remains a distinct outcome relationship and is not merged with it.
- **Alternative source-grounded interpretations:** As for Proposal B, an undisclosed evaluable denominator or analysis convention could exist; no such denominator is printed in this row.
- **Quality-control relevance:** LDL is a separate outcome and its individual effect summary may be abstracted independently.
- **Exact human question:** What denominator and calculation produced the printed `4.3` percentage-point LDL difference, given the displayed `9/64` and `6/62` counts?

## Proposal D — Printed DIC selection rule does not yield the displayed all-patient incident-cancer model at I2 = 25%

- **Category:** Numeric or arithmetic inconsistency.
- **Exact source locations:** [DOC-003 p. 4](../../../joi180151supp2_prod.pdf#page=4), eMethods model-selection rule; [DOC-003 p. 5](../../../joi180151supp2_prod.pdf#page=5), eMethods 3, all-patients Incident Cancer row.
- **Printed inputs:** The rule states that the lowest DIC model is selected; if the DIC difference is `≤3`, the random-effects model is selected when fixed-effect `I2 >25%`. The Incident Cancer row prints fixed DIC `27.06`, random DIC `27.93`, `I2 25`, and model `random`.
- **Rule and reproducible calculation:** `27.93 - 27.06 = 0.87`, so the difference is within 3. The printed `25` is not greater than the printed threshold `25`; applying the stated tie rule therefore selects fixed, which also has the lower DIC.
- **Tolerance:** The comparison uses an explicit strict inequality. No numerical rounding tolerance can make the printed integer 25 satisfy `>25`; however, an unprinted unrounded I2 between 25.0 and 25.5 could display as 25 and exceed 25.
- **Direct observation versus inference:** Direct observation is the rule, DICs, I2, and `random` label. The inference is a rule/output inconsistency based on the printed rounded I2.
- **Alternative source-grounded interpretations:** Model selection may have used an unrounded I2 greater than 25% or an internal convention of `≥25%`, neither of which is printed. The model could also have been selected by an additional unreported criterion.
- **Quality-control relevance:** The selected model determines the presentation and interpretation of this outcome's meta-analytic result.
- **Exact human question:** Was the underlying fixed-effect I2 greater than 25% before display rounding, or was a `≥25%`/other model-selection convention used for all-patient incident cancer?

## Proposal E — Egger test estimate and standard error do not reproduce the printed t statistic at displayed precision

- **Category:** Numeric or arithmetic inconsistency.
- **Exact source location:** [DOC-003 p. 21](../../../joi180151supp2_prod.pdf#page=21), eFigure 3.
- **Printed inputs:** `Egger Test: -0.47 (standard error: 0.77); t = -0.59, P = 0.57.`
- **Rule and reproducible calculation:** For a coefficient test with the displayed coefficient and standard error, `t = estimate / SE = -0.47 / 0.77 = -0.6104`, which rounds to `-0.61`, not `-0.59`.
- **Tolerance:** Treating both inputs as nearest-hundredth values gives coefficient magnitude 0.465 to less than 0.475 and SE 0.765 to less than 0.775. The attainable magnitude interval is approximately 0.600 to 0.621, which cannot round to 0.59 (0.585 to less than 0.595).
- **Direct observation versus inference:** The four printed values are direct observations. The inference is the usual coefficient/SE t-statistic identity; eFigure 3 does not print a different test formula.
- **Alternative source-grounded interpretations:** The t statistic may be from a distinct parameter, variance estimate, or software-output field not explained on the figure. Ordinary nearest-hundredth rounding and ordinary two-decimal truncation do not bridge the displayed ratio. Degrees of freedom and sidedness are not printed, so P-value compatibility is not separately asserted.
- **Quality-control relevance:** Estimate, SE, and test statistic are routinely extracted as a consistency set for small-study-bias assessments.
- **Exact human question:** Which unrounded coefficient and standard error, or which distinct calculation, generated the displayed `t = -0.59`?

## Proposal F — Total-stroke forest plot includes ASCEND data labeled as unavailable for all stroke and duplicates its ischaemic-stroke row

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-002 p. 7](../../../joi180151supp1_prod.pdf#page=7), protocol change; [DOC-003 p. 9](../../../joi180151supp2_prod.pdf#page=9), eTable 1 ASCEND definition; [DOC-003 p. 16](../../../joi180151supp2_prod.pdf#page=16), eTable 4 total stroke; [DOC-003 p. 24](../../../joi180151supp2_prod.pdf#page=24), eFigure 4 Total stroke and Ischemic stroke panels.
- **Printed inputs:** The protocol says ASCEND is excluded from the primary cardiovascular outcome because it defines stroke exclusively as ischaemic. eTable 1 says ASCEND `All strokes` is `Not included in analysis – only reports ischemic stroke`. eTable 4 total stroke has `12` studies and totals `1,116/73,883` versus `1,136/72,317`. The Total stroke forest plot has `13` rows and totals `81,623/80,057`, including ASCEND `240/7,740` versus `263/7,740`, RR `0.91 (0.77; 1.08)`. The Ischemic stroke panel prints the same ASCEND `240/7,740` versus `263/7,740`, RR `0.91 (0.77; 1.08)`.
- **Rule and reproducible calculation:** `81,623 - 73,883 = 7,740` and `80,057 - 72,317 = 7,740`, exactly the ASCEND per-arm total in the Total stroke forest. A source-defined all-stroke analysis that excludes ASCEND should not add ASCEND's ischaemic-only row to its all-stroke total without stating a distinct endpoint convention. The identical ASCEND row in both panels confirms that the forest's Total stroke panel uses the ischaemic-only ASCEND data.
- **Tolerance:** Counts are integers and the per-arm differences equal the displayed ASCEND denominators exactly; no rounding tolerance applies.
- **Direct observation versus inference:** Direct observations are the protocol/table exclusion wording, count totals, forest rows, and identical ASCEND event/total/RR row. The inference is that the Total stroke forest plot has included an outcome that the supplied source labels as unavailable for all stroke, or it uses an unstated endpoint convention.
- **Alternative source-grounded interpretations:** The authors may have intentionally treated ASCEND's ischaemic stroke as a usable total-stroke proxy for the frequentist forest analysis while excluding it from the Bayesian table, or `total stroke` may have a panel-specific operational definition. Neither interpretation is stated in the cited supplied source units.
- **Quality-control relevance:** The number of studies, denominators, pooled RR, and endpoint definition are core data elements likely to be copied into systematic reviews or meta-analyses.
- **Exact human question:** Was ASCEND intentionally included as an ischaemic-only proxy in the frequentist Total stroke forest plot, and if so, why does the supplied eTable/protocol define its all-stroke outcome as not included?

## Proposal G — Hyperlipidemia percentages reproduce only with the opposite arm denominators

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [DOC-001 p. 5](../../../jama_flint_2019_oi_190079.pdf#page=5), Table 1, Hyperlipidemia row and arm headers.
- **Printed inputs:** Olanzapine header `n = 64`, value `18 (29.0)`; placebo header `n = 62`, value `19 (29.7)`.
- **Rule and reproducible calculation:** Each within-arm percentage should use its own arm denominator. `18/64 x 100 = 28.125%`, which rounds to `28.1%`, not `29.0%`; `19/62 x 100 = 30.645...%`, which rounds to `30.6%`, not `29.7%`. Conversely, `18/62 x 100 = 29.032...%` rounds to `29.0%`, and `19/64 x 100 = 29.6875%` rounds to `29.7%`.
- **Tolerance:** Both own-arm discrepancies are far outside ±0.05 percentage point, while both printed percentages exactly reproduce at one decimal with the opposite arm denominators.
- **Direct observation versus inference:** The headers, counts, and percentages are direct observations. Use of opposite-arm denominators or a production transposition is inferred from the exact reproduced values.
- **Alternative source-grounded interpretations:** A row-specific denominator reversal may have occurred only in percentage calculation, or the printed counts/percentages may have been transposed independently; no alternative denominators are stated.
- **Quality-control relevance:** Baseline comorbidity percentages are routinely extracted and may be copied independently of the counts.
- **Exact human question:** Which arm denominators were intended for the two hyperlipidemia percentages, and should the printed percentages be recomputed from 18/64 and 19/62?

## Limitations

The source does not provide individual participant data, unrounded I2 values, the unrounded Egger coefficient/SE, measure-specific Table 5 analysis denominators beyond the printed headers, or a stated forest-plot exception for ASCEND. These omissions do not erase the printed comparisons; they define the human-adjudication questions above.
