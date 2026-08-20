# Numeric Consistency Check

## Coverage and rules

All `N001-N072` in `relationships/numeric_relationship_inventory.md` were checked against the fresh source assets and the exact supplied PDFs. No prior audit output or external material was used. This lane checked arithmetic, arm totals, counts/denominators/percentages, category complements, repeated values, outcome/population matching, labels/scales/units, interval order/containment when directly checkable, and count-versus-rate/proportion distinctions.

For a count `x` with stated arm denominator `n`, percentage checks used `100x/n`; the usual one-decimal display tolerance is half a displayed unit (0.05 percentage points). For a displayed between-arm percentage-point difference, the rule used the exact printed-count risks `100(x_P/n_P-x_C/n_C)` when the table itself supplies both counts and denominators. This is a diagnostic arithmetic rule, not a reconstruction of an unreported model. Nested CL categories and eTable-1 microbiology rows were not summed without a source statement of exclusivity. Bootstrap CI methods were not reverse-engineered.

## Explicit no-candidate / limited outcomes

| N IDs checked | Checks completed | Result |
|---|---|---|
| N001-N007, N010-N013, N017-N018, N021-N024 | repeated eligibility/timing/intervention units, rounded abstract means, design and outcome labels | No concrete mismatch; cross-location precision/population matches. |
| N008, N023 | flow identity: 90+84+15+10+3+1=203; 503-203=300; 150+150=300; primary analyses 150+150 | Reconciles. |
| N009, N019-N020, N059-N061, N070-N072 | all 150-based baseline, swab, treatment and subgroup denominators; complements 133+17=150, 125+25=150, 56+94=150, 42+108=150 | Reconciles. eTable-1 organism rows are potentially overlapping and therefore not totalled. |
| N014-N015, N032 (mode totals only) | race totals 133+10+7=150 and 135+10+5=150; parity totals 104+46=150 and 105+45=150; delivery modes 45+5+100=150 and 57+10+83=150 | Reconciles. |
| N025-N026, N028-N031, N034, N036, N038-N040, N062-N064, N066, N068-N069 | outcome counts, percentages, exact difference arithmetic, repeated narrative values, outcome definitions and units | No qualifying mismatch. Post-hoc overall PTB was kept distinct from spontaneous PTB. |
| N041, N043-N045, N050-N058 | at-risk sequences (not event totals), zero-event safety statement, interaction labels, protocol-to-report matching including explicitly disclosed OR-to-RR analysis change | No concrete numeric/label contradiction. |
| N046-N048 | external contextual values and correction notice | Limited: no supplied direct source comparator/reproduced correction wording; no candidate inferred. |

## Candidate proposals for human adjudication

### P-N01 — SPTB <32 weeks displayed difference does not round from printed counts

- **Primary category:** Numeric or arithmetic inconsistency.
- **Exact location:** `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Spontaneous preterm birth <32 wk.”
- **Printed inputs:** pessary `10 (6.7%)` of `150`; control `14 (9.3%)` of `150`; between-group difference `-2.6%`.
- **Direct observation:** all counts, denominators, and the displayed difference appear in the same Table 2 row.
- **Reproducible calculation:** `100*(10/150 - 14/150) = -2.666...` percentage points, which rounds to `-2.7%` to one decimal. A displayed `-2.6%` has rounding interval `[-2.65, -2.55]`; the count-derived value is outside it by about `0.0167` percentage points.
- **Tolerance:** ±0.05 percentage points for a one-decimal display.
- **Inference / alternatives:** This is arithmetic diagnostic reasoning from the table’s own counts. A non-150 analysis denominator, a nonstandard difference calculation, or a different unprinted population could explain the display, but each conflicts with the table headers/count presentation and requires confirmation.
- **Quality-control relevance:** a percentage-point estimate can be reused in evidence extraction independently of its RR.
- **Human question:** Should the Table 2 difference be `-2.7%`, or is another denominator/calculation intended for this row?

### P-N02 — Operative-vaginal-delivery displayed difference does not round from printed counts

- **Primary category:** Numeric or arithmetic inconsistency.
- **Exact location:** `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Operative vaginal delivery.”
- **Printed inputs:** pessary `5 (3.3%)` of `150`; control `10 (6.7%)` of `150`; difference `-3.4%`.
- **Direct observation:** all values are printed in the one row; the three delivery modes total 150 in each arm.
- **Reproducible calculation:** `100*(5/150 - 10/150) = -3.333...` percentage points, which rounds to `-3.3%`; `-3.4%` has interval `[-3.45,-3.35]`, which excludes the count-derived value.
- **Tolerance:** ±0.05 percentage points.
- **Inference / alternatives:** A different underlying denominator or nonstandard calculation could account for the result, but neither is stated and Table 2 labels both arms `n=150`.
- **Quality-control relevance:** the row’s numeric effect display is not reproducible from its printed event data.
- **Human question:** Is `-3.4%` the intended operative-vaginal difference, and if so what denominator/calculation should readers use?

### P-N03 — Chorioamnionitis displayed difference does not round from printed counts

- **Primary category:** Numeric or arithmetic inconsistency.
- **Exact location:** `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Chorioamnionitis.”
- **Printed inputs:** pessary `5 (3.3%)` of `150`; control `7 (4.7%)` of `150`; difference `-1.4%`.
- **Direct observation:** values co-occur in one Table 2 row.
- **Reproducible calculation:** `100*(5/150 - 7/150) = -1.333...` percentage points, which rounds to `-1.3%`; `-1.4%` has interval `[-1.45,-1.35]` and excludes the count-derived value.
- **Tolerance:** ±0.05 percentage points.
- **Inference / alternatives:** An unstated analysis denominator or calculation could explain it; none is supplied in the row or table footnotes.
- **Quality-control relevance:** a copied absolute difference would not reproduce the displayed count data.
- **Human question:** Should the reported difference be `-1.3%`, or is an alternative denominator/calculation intended?

### P-N04 — Perinatal-death displayed difference does not round from printed counts

- **Primary category:** Numeric or arithmetic inconsistency.
- **Exact location:** `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Perinatal death.”
- **Printed inputs:** pessary `2 (1.3%)` of `150`; control `4 (2.7%)` of `150`; difference `-1.4%`.
- **Direct observation:** values co-occur in one Table 2 row.
- **Reproducible calculation:** `100*(2/150 - 4/150) = -1.333...` percentage points, which rounds to `-1.3%`; `-1.4%` has interval `[-1.45,-1.35]` and excludes the count-derived value.
- **Tolerance:** ±0.05 percentage points.
- **Inference / alternatives:** An unstated denominator/calculation could explain the row; the stated arm sizes and counts otherwise give the calculation above.
- **Quality-control relevance:** printed count and effect representations are not mechanically reproducible together.
- **Human question:** Is `-1.4%` correct for this row, and if so what calculation generated it?

### P-N05 — Narrative spontaneous-delivery HR conflicts with its CI and Figure 2

- **Primary category:** Cross-document numeric inconsistency.
- **Exact locations:** `jama_saccone_2017_oi_170144.pdf#page=5`, Primary Outcome narrative: “hazard ratio, `0.36`; 95% CI, `0.54-0.87`”; and `jama_saccone_2017_oi_170144.pdf#page=6`, Figure 2 panel B: spontaneous-delivery-only HR `0.68 (95% CI 0.54-0.87)`.
- **Printed inputs:** same stated CI `0.54-0.87`, but point estimates `0.36` (narrative) and `0.68` (panel B).
- **Direct observation:** both direct-source locations use the spontaneous-delivery survival-analysis context; the narrative estimate `0.36` is also below its own printed lower CI bound `0.54`.
- **Reproducible rule/calculation:** a reported two-sided 95% CI must have lower endpoint <= its point estimate <= upper endpoint. `0.54 <= 0.36` is false; panel B supplies `0.68`, which is within `0.54-0.87`.
- **Tolerance:** none for ordering/containment; no rounding tolerance can bridge `0.18`.
- **Inference / alternatives:** The direct contradiction could be a narrative typographic error, a mislabeled analysis, or a figure/narrative matching issue. The identical CI and spontaneous-delivery description make a distinct analysis less apparent, but supplied material does not identify the intended correction.
- **Quality-control relevance:** a hazard ratio is a directly extractable quantitative effect; the two values cannot both describe the same displayed result.
- **Human question:** Which HR is intended for the spontaneous-delivery survival analysis—`0.36` or `0.68`—and should the narrative/figure labels be amended?

### P-N06 — Birth-weight <2500 g difference CI excludes its displayed difference and has direction conflict

- **Primary category:** Numeric or arithmetic inconsistency.
- **Exact location:** `joi170144supp2_prod.pdf#page=3`, eTable 2, “Birth weight <2,500 grams.”
- **Printed inputs:** pessary `28 (18.7%)` of `150`; control `45 (30.0%)` of `150`; difference `-11.3% (95% CI, -1.1 to +21.2)`; RR `0.62 (0.41 to 0.94)`; `P=0.03`.
- **Direct observation:** the printed negative difference lies outside its printed interval because `-11.3 < -1.1`; both event risks and RR indicate fewer events in the pessary group.
- **Reproducible rule/calculation:** interval containment requires `lower <= estimate <= upper`; `-1.1 <= -11.3` is false. The count-derived difference is `100*(28/150-45/150)=-11.333...%`, agreeing with the printed negative point estimate, not with an interval entirely from `-1.1` to `+21.2`.
- **Tolerance:** none for containment. This is not an attempt to reconstruct the CI method.
- **Inference / alternatives:** The endpoints may have a sign/order transcription problem (for example, a visually similar intended negative endpoint), but the supplied source does not establish a replacement.
- **Quality-control relevance:** the table’s absolute effect and interval cannot be interpreted together and may be extracted separately.
- **Human question:** What are the intended 95% CI endpoints for the `-11.3%` birth-weight <2500 g difference?

### P-N07 — RDS displayed difference does not round from its printed counts

- **Primary category:** Numeric or arithmetic inconsistency.
- **Exact location:** `joi170144supp2_prod.pdf#page=3`, eTable 2, “Respiratory distress syndrome.”
- **Printed inputs:** pessary `14 (9.3%)` of `150`; control `31 (20.7%)` of `150`; difference `-11.4%`.
- **Direct observation:** the row provides both counts, arm denominators, and difference.
- **Reproducible calculation:** `100*(14/150-31/150)=-11.333...` percentage points, which rounds to `-11.3%`; `-11.4%` has interval `[-11.45,-11.35]`, excluding the count-derived value.
- **Tolerance:** ±0.05 percentage points.
- **Inference / alternatives:** an unstated denominator or nonstandard calculation could explain the display; the table presents all outcomes as counts/proportions with `N=150` per arm.
- **Quality-control relevance:** the displayed absolute difference is not reproducible from the accompanying data.
- **Human question:** Should the RDS difference be `-11.3%`, or was another denominator/calculation used?

### P-N08 — CL <=10 mm subgroup difference does not round from printed fractions

- **Primary category:** Numeric or arithmetic inconsistency.
- **Exact location:** `joi170144supp2_prod.pdf#page=4`, eTable 3, `TVU CL <=10 mm` subgroup.
- **Printed inputs:** pessary `3/56 (5.4%)`; control `10/42 (23.8%)`; difference `-18.4%`.
- **Direct observation:** exact numerators and denominators are printed, and denominators complement the corresponding >10-mm rows to 150 per arm.
- **Reproducible calculation:** `100*(3/56-10/42)=-18.452...` percentage points, which rounds to `-18.5%`; `-18.4%` has interval `[-18.45,-18.35]` and excludes the fraction-derived value by about `0.0024` percentage points.
- **Tolerance:** ±0.05 percentage points.
- **Inference / alternatives:** This is very near the rounding boundary. A calculation based on a more precise unprinted quantity is not applicable to the printed integer fractions, but a table-production convention could explain the last digit; human confirmation is appropriate.
- **Quality-control relevance:** the subgroup absolute difference may be copied independently from its numerator/denominator display.
- **Human question:** Is `-18.4%` the intended rounded difference for the printed `3/56` and `10/42` subgroup data?

## Result

Eight distinct document-grounded proposals were emitted. They are all **Pending Human Adjudication**; this checker assigns no stable candidate IDs, severity, validity, correction, or disposition. No proposal is based on a `P=0`/`p=0.000` display.
