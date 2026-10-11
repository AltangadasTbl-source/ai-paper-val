# Fresh direct-source coverage

This source-first preprocessing run found six direct PDF sources and no direct Office or structured-data source. Fresh native and layout text were made with the direct installed Windows `pdftotext.exe` v4.00 executable using Windows UNC paths. Form-feed boundaries confirm every unit below. `pdfinfo` remains unavailable. DOC-001's fresh extractor count is 14 pages, which conflicts with the earlier `file` page-count string of 10; the direct extraction boundary count governs the mapped-unit record pending `pdfinfo` confirmation.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_bluth_2019_oi_190055_16092.pdf | PDF_PAGE | 14 | 0 | 14 | 14 | COMPLETE |
| DOC-002 | joi190055supp1_prod_16092.pdf | PDF_PAGE | 36 | 0 | 36 | 36 | COMPLETE |
| DOC-003 | joi190055supp2_prod_16092.pdf | PDF_PAGE | 3 | 0 | 3 | 3 | COMPLETE |
| DOC-004 | joi190055supp3_prod_16092.pdf | PDF_PAGE | 3 | 0 | 3 | 3 | COMPLETE |
| DOC-005 | joi190055supp4_prod_16092.pdf | PDF_PAGE | 43 | 0 | 43 | 43 | COMPLETE |
| DOC-006 | joi190055supp5_prod_16092.pdf | PDF_PAGE | 1 | 0 | 1 | 1 | COMPLETE |

Totals: 100 unique source units; 0 reusable units; 100 fresh-required units; 100 freshly mapped units.

Each complete row has a fresh, non-empty native and layout-text page boundary for every listed unit. The exact extractor command/version, page-boundary verification, and remaining rendering limitation are in `preprocessing/metadata/tool_availability.md` and `evidence_asset_inventory.md`.
