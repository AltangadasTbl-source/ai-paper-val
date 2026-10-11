# Complete Source Coverage Ledger

`Mapped units` records an explicit curation-stage assignment for every unique direct-source page: either a usable reusable page asset or a fresh direct-source mapper assignment. It does not assert that later scientific relationship mapping has already occurred.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_zahid_2025_oi_250093_1768590553.08463.pdf | PDF_PAGE | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 | joi250093supp1_prod_1768590553.08963.pdf | PDF_PAGE | 109 | 0 | 109 | 109 | COMPLETE |
| DOC-003 | joi250093supp2_prod_1768590553.09463.pdf | PDF_PAGE | 16 | 14 | 2 | 16 | COMPLETE |

## Exact unit assignments

| Source ID | Reusable-backed pages | Fresh-required pages | Downstream mapper assignment |
|---|---|---|---|
| DOC-001 | 1-9 | None | Main mapper: reusable normalized text on pages 1-9; confirm direct PDF as required. |
| DOC-002 | None | 1-109 | Support mapper: current-run fresh layout extraction and 180-dpi rendered/OCR derivatives under `review_1_5_1/preprocessing/DOC-002`, pages 1-109; direct PDF remains authority. |
| DOC-003 | 3-16 | 1-2 | Support mapper: fresh direct PDF native/layout extraction for pages 1-2; reusable normalized text and rendered pages for pages 3-16; confirm direct PDF as required. |

The counts partition each source exactly: reusable plus fresh-required equals total (9 = 9 + 0; 109 = 0 + 109; 16 = 14 + 2). The total fresh-required burden is 111 pages and the total mapped curation scope is 134 pages.

Current-run fresh assets for DOC-002 and DOC-003 pp. 1-2 are downstream work products, not pre-existing reused artifacts; they are intentionally excluded from `reused_artifact_hashes_before.sha256`.
