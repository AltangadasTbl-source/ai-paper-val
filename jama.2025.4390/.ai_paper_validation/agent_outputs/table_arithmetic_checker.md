# Table Arithmetic Checker Response

- **Agent:** table_arithmetic_checker
- **Scope:** Result-relevant tables only: main article Tables 1-2 (PDF pp. 5-6, 8) and results-supplement eTables 1-9 (PDF pp. 27-49). Protocol and SAP were not audited.
- **Method:** Checked visible numerators, denominators, percentages, categorical row totals, repeated values, displayed differences, and stated cross-document table anchors. Source PDFs were not modified.

## Retained candidate (1)

| ID | Allowed category | Exact location | Source values | Calculation / logical basis | Verification instruction |
|---|---|---|---|---|---|
| TAC-01 | Presentation inconsistency | `joi250019supp3_prod_1749674951.30054.pdf`, PDF p. 37, eTable 5, **Ethnicity - no. (%)**, `Other` row | Morning allocation (n=44): White/Caucasian **40 (90.9)** and Other **40 (90.9)**. Bedtime allocation (n=57): White/Caucasian **53 (93.0)** and Other **53 (93.0)**. | The `Other` cells exactly duplicate the White/Caucasian cells. Including the eight displayed ethnicity rows gives Morning **85/44 = 193.2%** and Bedtime **111/57 = 194.7%**. This is incompatible with the table's baseline ethnicity breakdown; the analogous eTable 3 breakdown (PDF pp. 29-32) partitions to its stated allocation totals. | Visually inspect PDF p. 37 and compare the `Other` row with `White/Caucasian`; check the source table/export for the intended `Other` values or row placement. |

## No candidate retained after checks

- Main article Table 1: visible categorical counts and percentages reconcile to allocation denominators where categories are exhaustive.
- Main article Table 2: displayed count/percentage rows, rate differences, and direct eTable 9 ABPM anchors were internally compatible; small rate-difference apparent gaps were consistent with rounding of displayed rates.
- Results supplement eTables 1-4 and 6-9: visible component counts, percentages, and stated totals reconciled within rounding or were explicitly non-additive by table footnote. eTable 8 reason rows were not summed because the footnote permits multiple reasons per participant.

