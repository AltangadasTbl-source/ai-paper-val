# Direct-Source Inventory

Inventory performed for Workflow 1.5.1 before scientific mapping. The package contains three direct sources and no DOC, DOCX, XLS, XLSX, or CSV direct sources. Each PDF was checked with `pdfinfo`; source hashes are recorded separately in `source_hashes_before.sha256` by the coordinator.

| Source ID | Package-relative source path | Format | Stable unit type | Total units | `pdfinfo` pages | Native-text indication | Direct-source status |
|---|---|---|---|---:|---:|---|---|
| DOC-001 | jama_martin_2025_oi_250042_1753377747.91025.pdf | PDF | PDF_PAGE | 11 | 11 | Available | Complete direct-source inventory; all pages require result-relevant mapping. |
| DOC-002 | joi250042supp1_prod_1753377747.92525.pdf | PDF | PDF_PAGE | 136 | 136 | Existing record reports unavailable/unusable; no page-level reuse extraction exists. | Complete direct-source inventory; all pages require fresh direct-source mapping. |
| DOC-003 | joi250042supp2_prod_1753377747.93025.pdf | PDF | PDF_PAGE | 29 | 29 | Available | Complete direct-source inventory; page-level reuse exists only for pages 2-27. |

## Inventory method and boundary

- Direct-source extensions searched: PDF, DOC, DOCX, XLS, XLSX, and CSV, case-insensitively, at the package root and below it while excluding the new review directory from derivative discovery.
- `pdfinfo` verified 11, 136, and 29 pages for DOC-001, DOC-002, and DOC-003 respectively; total direct-source units are 176 PDF pages.
- No Office workbook, delimited data, DOC, or DOCX direct source was present, so no Office structure extraction was required.
- Existing audit derivatives were inventoried as reusable evidence assets only. Legacy candidate/checker/reviewer/critic/endetail/final-report records were not used to define scientific scope or candidate discovery.
