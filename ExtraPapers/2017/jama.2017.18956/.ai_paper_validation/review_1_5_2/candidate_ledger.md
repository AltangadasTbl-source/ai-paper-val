# Stable Candidate Ledger

All entries are quality-control candidates and remain **Pending Human Adjudication**. Stable IDs were assigned after merging only proposals involving the same printed values, comparator, and consistency rule. No candidate is based on a display-zero P value.

## C001 — Spontaneous-delivery hazard ratio conflicts across narrative and Figure 2B

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Primary Outcome narrative; DOC-001 `jama_saccone_2017_oi_170144.pdf#page=6`, Figure 2 panel B.
- **Source evidence:** The narrative prints HR `0.36` with 95% CI `0.54-0.87`; Figure 2B, labelled spontaneous delivery only, prints HR `0.68` with the identical 95% CI `0.54-0.87`.
- **Comparator and rule:** Matched occurrences of the same spontaneous-delivery Cox result should reproduce the same point estimate, and an HR must lie within its own ordered CI.
- **Calculation:** `0.36 != 0.68`, and `0.36 < 0.54`; `0.68` lies within `[0.54, 0.87]`.
- **Direct observation versus inference:** The values and labels are direct observations. A transcription error or unexpectedly different model is an unconfirmed explanation.
- **Provenance:** Numeric proposal P-N05; statistical pass-1 P01; cross-source Proposal 1.
- **Exact human question:** What HR and 95% CI were produced for the spontaneous-delivery Cox analysis through 34 weeks, and which printed occurrence is intended?

## C002 — SPTB under 32 weeks difference does not round from printed counts

- **Category:** Numeric or arithmetic inconsistency
- **Exact source location:** DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, spontaneous preterm birth `<32 wk`.
- **Source evidence:** Pessary `10/150 (6.7%)`; control `14/150 (9.3%)`; printed difference `-2.6%`.
- **Comparator and rule:** The exact printed counts and denominators imply the percentage-point difference; a one-decimal result is checked with a 0.05-point rounding tolerance.
- **Calculation:** `100*(10/150 - 14/150) = -2.666...`, conventionally `-2.7%`; `-2.6%` corresponds to subtracting the already rounded displayed percentages.
- **Direct observation versus inference:** Counts, denominators, percentages, and difference are direct. Which production convention governs the difference is unresolved.
- **Provenance:** Numeric proposal P-N01.
- **Exact human question:** Should the difference be `-2.7%`, or was it intentionally calculated from rounded displayed percentages or another denominator?

## C003 — Operative-vaginal-delivery difference does not round from printed counts

- **Category:** Numeric or arithmetic inconsistency
- **Exact source location:** DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, operative vaginal delivery.
- **Source evidence:** Pessary `5/150 (3.3%)`; control `10/150 (6.7%)`; printed difference `-3.4%`.
- **Comparator and rule:** The exact printed counts and denominators imply the percentage-point difference under standard one-decimal rounding.
- **Calculation:** `100*(5/150 - 10/150) = -3.333...`, conventionally `-3.3%`; `-3.4%` equals the difference between the displayed rounded percentages.
- **Direct observation versus inference:** Printed values are direct; the table-production convention is not stated.
- **Provenance:** Numeric proposal P-N02. The separate CI-containment rule for this row is C010 and is not merged.
- **Exact human question:** Is `-3.4%` intended, and what denominator or rounding convention generated it?

## C004 — Chorioamnionitis difference does not round from printed counts

- **Category:** Numeric or arithmetic inconsistency
- **Exact source location:** DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, chorioamnionitis.
- **Source evidence:** Pessary `5/150 (3.3%)`; control `7/150 (4.7%)`; printed difference `-1.4%`.
- **Comparator and rule:** The exact printed counts and denominators imply the percentage-point difference under standard one-decimal rounding.
- **Calculation:** `100*(5/150 - 7/150) = -1.333...`, conventionally `-1.3%`; `-1.4%` equals subtraction of the rounded displayed percentages.
- **Direct observation versus inference:** Printed values are direct; the production convention or any alternate denominator is not supplied.
- **Provenance:** Numeric proposal P-N03.
- **Exact human question:** Should the difference be `-1.3%`, or is the printed `-1.4%` based on an intended alternative convention?

## C005 — Perinatal-death difference does not round from printed counts

- **Category:** Numeric or arithmetic inconsistency
- **Exact source location:** DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, perinatal death.
- **Source evidence:** Pessary `2/150 (1.3%)`; control `4/150 (2.7%)`; printed difference `-1.4%`.
- **Comparator and rule:** The exact printed counts and denominators imply the percentage-point difference under standard one-decimal rounding.
- **Calculation:** `100*(2/150 - 4/150) = -1.333...`, conventionally `-1.3%`; `-1.4%` equals subtraction of the rounded displayed percentages.
- **Direct observation versus inference:** Printed values are direct; an alternate calculation is not stated.
- **Provenance:** Numeric proposal P-N04.
- **Exact human question:** Should the difference be `-1.3%`, or is another stated or intended calculation responsible for `-1.4%`?

## C006 — Birth weight under 2500 g difference lies outside its printed CI

- **Category:** Statistical reporting inconsistency
- **Exact source location:** DOC-003 `joi170144supp2_prod.pdf#page=3`, eTable 2, birth weight `<2500 grams`.
- **Source evidence:** Pessary `28/150 (18.7%)`; control `45/150 (30.0%)`; difference `-11.3%` with 95% CI `-1.1 to +21.2`; RR `0.62 (0.41-0.94)`; `P=.03`.
- **Comparator and rule:** A point estimate must lie within its own ordered CI; event risks and RR establish the negative effect direction.
- **Calculation:** `100*(28/150 - 45/150) = -11.333...`, consistent with `-11.3%`, but `-11.3 < -1.1`, so the estimate is outside `[-1.1, 21.2]`.
- **Direct observation versus inference:** The non-containment is direct. A sign or endpoint transcription issue is plausible but unconfirmed; no replacement CI is inferred.
- **Provenance:** Numeric proposal P-N06; statistical pass-1 P04.
- **Exact human question:** What verified 95% CI belongs to the `-11.3%` difference, and are the printed endpoint signs correct?

## C007 — Respiratory-distress-syndrome difference does not round from printed counts

- **Category:** Numeric or arithmetic inconsistency
- **Exact source location:** DOC-003 `joi170144supp2_prod.pdf#page=3`, eTable 2, respiratory distress syndrome.
- **Source evidence:** Pessary `14/150 (9.3%)`; control `31/150 (20.7%)`; printed difference `-11.4%`.
- **Comparator and rule:** The exact printed counts and denominators imply the percentage-point difference under standard one-decimal rounding.
- **Calculation:** `100*(14/150 - 31/150) = -11.333...`, conventionally `-11.3%`; `-11.4%` equals subtraction of the rounded displayed percentages.
- **Direct observation versus inference:** Printed values are direct; the table-production convention is not stated.
- **Provenance:** Numeric proposal P-N07.
- **Exact human question:** Should the difference be `-11.3%`, or is `-11.4%` based on an intended rounded-percentage convention or different denominator?

## C008 — Cervical-length subgroup difference is on the opposite side of the rounding boundary

- **Category:** Numeric or arithmetic inconsistency
- **Exact source location:** DOC-003 `joi170144supp2_prod.pdf#page=4`, eTable 3, TVU cervical length `<=10 mm` subgroup.
- **Source evidence:** Pessary `3/56 (5.4%)`; control `10/42 (23.8%)`; printed difference `-18.4%`.
- **Comparator and rule:** Exact fractions imply the percentage-point difference under standard one-decimal rounding.
- **Calculation:** `100*(3/56 - 10/42) = -18.45238...`, conventionally `-18.5%`; subtraction of the displayed rounded percentages gives `-18.4%`.
- **Direct observation versus inference:** This is extremely close to the one-decimal rounding boundary. The direct fractions and display are supplied; the production convention is not.
- **Provenance:** Numeric proposal P-N08.
- **Exact human question:** Was `-18.4%` intentionally calculated from displayed rounded percentages, or should the fraction-derived value round to `-18.5%`?

## C009 — Cesarean-delivery difference lies outside its printed CI

- **Category:** Statistical reporting inconsistency
- **Exact source location:** DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, cesarean delivery.
- **Source evidence:** Pessary `45/150 (30.0%)`; control `57/150 (38.0%)`; difference `-8.0%` with 95% CI `-3.2 to 19.0`; RR `0.79 (0.57-1.09)`; `P=.18`.
- **Comparator and rule:** A point estimate must lie within its own ordered CI.
- **Calculation:** `30.0 - 38.0 = -8.0`, but `-8.0 < -3.2`, so the point estimate is outside `[-3.2, 19.0]`.
- **Direct observation versus inference:** Non-containment is direct; a sign or endpoint production error is possible but no corrected CI is supplied.
- **Provenance:** Statistical pass-1 P02.
- **Exact human question:** What signed 95% CI belongs to the printed `-8.0%` cesarean-delivery difference?

## C010 — Operative-vaginal-delivery difference lies outside its printed CI

- **Category:** Statistical reporting inconsistency
- **Exact source location:** DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, operative vaginal delivery.
- **Source evidence:** Pessary `5/150 (3.3%)`; control `10/150 (6.7%)`; difference `-3.4%` with 95% CI `-2.1 to 9.1`; RR `0.50 (0.18-1.43)`; `P=.29`.
- **Comparator and rule:** A point estimate must lie within its own ordered CI.
- **Calculation:** `-3.4 < -2.1`, so `-3.4%` is outside `[-2.1, 9.1]`.
- **Direct observation versus inference:** Non-containment is direct; an endpoint/sign transcription issue is a possible but unsupported explanation.
- **Provenance:** Statistical pass-1 P03. C003 uses a different comparator and arithmetic rule and remains distinct.
- **Exact human question:** What signed 95% CI belongs to the operative-vaginal-delivery difference, and is the printed point estimate paired with the intended interval?

## Registration Summary

- **Stable candidate count:** 10
- **Stable ID set:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010
- **Status of every candidate:** Pending Human Adjudication
- **Display-zero-only candidates:** 0
