# Complete Source Coverage

`Mapped units` records complete unit-to-downstream-mapper assignment at this curation stage, not completion of scientific relationship reconstruction. Every uncovered or non-usable reusable unit is in the fresh-required partition and has a direct-source assignment below.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_cinciripini_2024_oi_240036_1716416465.98349.pdf | PDF_PAGE | 10 | 0 | 10 | 10 | COMPLETE |
| DOC-002 | joi240036supp1_prod_1716416466.00349.pdf | PDF_PAGE | 45 | 0 | 45 | 45 | COMPLETE |
| DOC-003 | joi240036supp2_prod_1716416466.01349.pdf | PDF_PAGE | 36 | 0 | 36 | 36 | COMPLETE |

| Metric | Count |
|---|---:|
| Unique total source units | 91 |
| Reusable units | 0 |
| Fresh-required units | 91 |
| Mapped units | 91 |

## Exact fresh direct-source mapper assignments

| Source ID | Exact unit scope | Reason fresh mapping is required | Downstream mapper assignment |
|---|---|---|---|
| DOC-001 | PDF pp. 1-10 | All prior text, rendered-page, and map assets are stale because the recorded source SHA-256 does not match the current direct source. | main_quantitative_mapper: direct PDF extraction and source-page mapping. |
| DOC-002 | PDF pp. 1-45 | No existing native/layout text, OCR, table extraction, workbook extraction, or rendered-page asset exists. | support_quantitative_mapper: direct PDF extraction and source-page mapping. |
| DOC-003 | PDF pp. 1-36 | Existing page-level derivatives for pp. 4-35 are stale because the recorded source SHA-256 does not match the current direct source; pp. 1-3 and 36 have no derivative. | support_quantitative_mapper: direct PDF extraction and source-page mapping. |

Scientific coverage has no unassigned gap. Fresh extraction/mapping must be completed from the current direct source before any reusable derivative is used as a locator.
