# Table arithmetic/internal-consistency check — DOC-001 and DOC-003

## Scope and disposition

Checked only result-relevant tables identified in the evidence maps: DOC-001 Table 1 (PDF p. 5), Table 2 (p. 6), and Table 3 (p. 7); and DOC-003 eTables 1–6 (PDF pp. 4–11). Protocol and administrative documents were not inspected. Two document-verifiable local candidates are proposed below. The remaining visible numerator/denominator percentages, subgroup Ns, and displayed row relationships reconciled to their reported precision or were not arithmetically derivable from the reported values.

## Candidate TA-01 — eTable 4 reports an incompatible placebo percentage and category total

- **Category / severity:** Arithmetic inconsistency; moderate (localized result-table presentation).
- **Exact location:** DOC-003, `joi200054supp2_prod.pdf`, PDF p. 7, eTable 4, *Between-Arm Differences for Amount of Oral Candidiasis Outcome Measures*, 3-month section, Placebo column, `(-/+)` and `(+)` rows; table footnote defining the four semi-quantitative levels.
- **Verbatim source values:** `(-/+) 20/119 (16.8) 80`; `(+) 20/119 (16.0) 80`; `(++) 38/119 (31.9) 80`; `(+++) 42/119 (35.3) 80`. The footnote defines the displayed levels as `(-/+)`, `(+)`, `(++)`, and `(+++)`.
- **Calculation and tolerance:** `20 / 119 × 100 = 16.8067%`, which rounds to **16.8%** to one decimal (rounding interval 16.75%–16.85%). It cannot round to the reported **16.0%** (interval 15.95%–16.05%). Also, the four displayed category numerators total `20 + 20 + 38 + 42 = 120`, whereas their shared displayed denominator is `119`; for mutually exclusive semi-quantitative levels, the category total should equal the denominator.
- **Reasoning:** One visible numerator/denominator percentage is incompatible with its own displayed percentage, and the same four-level distribution contains one more category count than its stated denominator. Both discrepancies are local to the same placebo, 3-month distribution and require no unreported data.
- **Bounded impact:** The error affects the presentation of one placebo-arm 3-month oral-candidiasis distribution; it does not by itself establish that the adjusted OR `0.7 (0.20 to 2.17)` or its P value is incorrect.
- **Human verification:** (1) Check the source table cell and the four category labels. (2) Recalculate `20/119` and sum the four category counts. (3) Confirm whether one count, denominator, or percentage was transcribed incorrectly; correction to `16.8%` and a total of 119 would resolve the visible arithmetic conflict.

## Candidate TA-02 — eTable 5 displays 19/27 as 70.0%, rather than the one-decimal percentage implied by the fraction

- **Category / severity:** Arithmetic inconsistency; low (localized repeated percentage presentation).
- **Exact location:** DOC-003, `joi200054supp2_prod.pdf`, PDF p. 8, eTable 5, *Between-Arm Differences for Microbiology Outcome Measures*, *Enterobacterales in stool resistant to at least one of the tested antibiotics*, `Second follow-up, n/N (%)`, Placebo column. The same fraction/percentage is repeated in DOC-001, `jama_butler_2020_oi_200054.pdf`, PDF p. 7, Results microbiology paragraph.
- **Verbatim source values:** DOC-003: placebo `19/27 (70.0)`; probiotic `23/33 (69.7)`; displayed absolute difference `-0.01 (-0.24 to 0.23)`. DOC-001 repeats `19/27 [70.0%]`.
- **Calculation and tolerance:** `19 / 27 × 100 = 70.3704%`, which rounds to **70.4%** at one decimal (rounding interval 70.35%–70.45%). It cannot round to the displayed **70.0%** (interval 69.95%–70.05%). Using the fractions, `23/33 − 19/27 = -0.00673`, which rounds to the table's `-0.01`; this independently supports the fraction rather than the displayed 70.0%.
- **Reasoning:** The numerator and denominator, the one-decimal percentage, and the adjacent absolute-difference column cannot all be true at the shown precision. The inconsistency is duplicated from the supplement table into the main-article narrative.
- **Bounded impact:** This is a 0.4-percentage-point display error in the placebo second-follow-up percentage. The reported adjusted OR, CI, and P value cannot be recomputed from the displayed data and are not alleged to be wrong.
- **Human verification:** (1) Verify the `19/27` cell in eTable 5 and its duplicate in the main text. (2) Calculate the percent to one decimal and the unrounded risk difference. (3) Replacing `70.0%` with `70.4%` would reconcile the displayed components.
