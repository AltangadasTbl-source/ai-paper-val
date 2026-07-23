# Table arithmetic checker record: DOC-001-MAIN

- **Source reviewed:** `jama_shotar_2025_oi_250033_1750956987.75881.pdf`, PDF pp. 1-9.
- **Result-relevant tables reviewed:** Table 1 (PDF p. 5), Table 2 (PDF p. 6), and Table 3 (PDF p. 7). Values were checked against the source-mapped rendered pages and native text.
- **Excluded by scope:** protocol, SAP, and administrative PDFs; no external material used.

## Retained candidate (1)

### TBL-001 - Standard-care treatment-type rows exceed their shared denominator

- **Category:** Arithmetic inconsistency
- **Exact location:** DOC-001-MAIN, PDF p. 5, Table 1, `Treatment` section, standard-care column.
- **Source values:** `Trepanation burr hole craniostomy`: 146/163 (89.6%); `Trephine craniostomy`: 18/163 (11.0%). Table footnote e describes the procedures as performed "either" with a cranial drill (burr-hole craniostomy) "or" a skull trephine cylindrical saw (trephine craniostomy).
- **Calculation:** 146 + 18 = **164**, while both rows use a denominator of **163**. The displayed percentages also sum to 89.6% + 11.0% = **100.6%**. Individually, 146/163 = 89.57% and 18/163 = 11.04%, so the issue is the adjacent-row total, not percentage rounding.
- **Reasoning:** The table's own either/or procedural description makes these treatment-type rows mutually exclusive as presented; their reported counts cannot exceed the shared 163 patients.
- **Verification instruction:** Compare the standard-care surgery-type counts with the source case coding. Correct one numerator or the denominator; if a patient could legitimately be counted in both rows, revise the table/footnote to make nonexclusive classification explicit.

## Rejected checks

- **Table 1 - sex and CSDH laterality totals:** no issue. Embolization: female + male = 32 + 139 = 171 and unilateral + bilateral CSDH = 127 + 44 = 171. Standard care: 36 + 135 = 171 and 130 + 41 = 171. Corresponding displayed percentages are consistent with their denominators after one-decimal rounding.
- **Table 1 - embolization treatment-type rows:** no issue. 150/167 + 17/167 = 167/167 (89.8% + 10.2% = 100.0%).
- **Table 2 - visible numerator, denominator, percentage, and outcome-component checks:** no issue. Primary outcome: 24/162 = 14.8% and 33/157 = 21.0%; component counts are 22 + 2 = 24 and 32 + 1 = 33. Repeat surgery: 7/162 = 4.3% and 13/157 = 8.3%. Mortality: 3/165 = 1.8%, 9/165 = 5.5%, and 13/165 = 7.9%. Procedure-complication values are also consistent with N = 171 (1/171 = 0.6%; 3/171 = 1.8%; 2/171 = 1.2%).
- **Table 3 - visible percentages:** no issue. 36/171 = 21.1%, 32/171 = 18.7%, 91/171 = 53.2%, and 89/171 = 52.0%, to one decimal place. Subrows were not summed because the source does not state that adverse-event categories are mutually exclusive.

## Scope and disposition

One document-verifiable local candidate is retained. No other main-article table candidate met the evidence threshold.
