# Table arithmetic and internal-consistency check

**Scope:** DOC-003 result-relevant eTables 1-10 (PDF pp. 15-27). DOC-002 was not audited by design.

## Candidates for verification

| Candidate ID | Taxonomy | Exact location | Source values and calculation | Concise basis / verification instruction |
|---|---|---|---|---|
| DOC003-C1 | Presentation inconsistency | `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 26, eTable 9, **Any serious adverse event** row | The row has blank cells under both **Events, No.** columns, but reports 58 (0.7%) and 29 (0.4%) under **Patients, No. (%)**. Enumerated event counts below it sum to 64 conservative events (2 + 12 + 16 + 19 + 7 + 1 + 1 + 1 + 1 + 1 + 1 + 0 + 1 + 1) and 37 usual events (1 + 8 + 15 + 11 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 2 + 0 + 0). | The table visibly labels event-total columns but leaves the overall-row cells blank despite reporting row-level event counts. Verify whether omission was intentional; do not infer that 64 and 37 must be printed without author/source confirmation. |
| DOC003-C2 | Presentation inconsistency | `joi250042supp2_prod_1753377747.93025.pdf`, PDF p. 27, eTable 10, **Year published** row, HOT-ICU column | The displayed value is **202**. The six adjacent values are four-digit years: 2025, 2024, 2023, 2022, 2021, and 2020. Digit-count comparison: 3 versus 4. | A visibly incomplete year value is locally inconsistent in format. Verify the intended four-digit year from the source production record; this check does not infer the missing digit. |

## Checks without a candidate

- eTable 1 site counts sum to the stated total: 16,500.
- eTables 2-4: displayed mutually exclusive category counts reconcile to their displayed denominators where a complete category set is shown.
- eTables 5-6: displayed mean differences agree with the group values to their shown rounding precision; small tenth-unit differences are compatible with calculation before rounding.
- eTable 7 percentages reconcile to their stated analysis denominators, including 1661 / 13,052 = 12.7% (one-year mortality missingness).
- eTable 8: ICU-stay counts reconcile as 5211 + 2122 = 7333 and 5290 + 2158 = 7448; acute-hospital-stay counts reconcile as 4791 + 2532 = 7323 and 4906 + 2528 = 7434.
- eTable 10 displayed achieved-oxygenation high-minus-low values reconcile to shown precision; no arithmetic candidate other than DOC003-C2.
