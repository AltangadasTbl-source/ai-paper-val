# Complete Source Coverage Ledger

Counts are unique PDF pages. `Reusable units + fresh-required units = total units` for every direct source. All direct-source pages have been mapped through the disjoint evidence-mapping artifacts recorded in `coverage_manifest.md`.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_martin_2025_oi_250042_1753377747.91025.pdf | PDF_PAGE | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | joi250042supp1_prod_1753377747.92525.pdf | PDF_PAGE | 136 | 0 | 136 | 136 | COMPLETE |
| DOC-003 | joi250042supp2_prod_1753377747.93025.pdf | PDF_PAGE | 29 | 26 | 3 | 29 | COMPLETE |

## Exact partition and required downstream assignments

| Source ID | Reusable direct-source units | Fresh-required direct-source units | Reason for fresh requirement |
|---|---|---|---|
| DOC-001 | PDF pages 1-11 | None | Usable page-matched normalized native text covers every page; pages 1 and 3-10 also have reusable render/OCR support. |
| DOC-002 | None | PDF pages 1-136 | The only document records/page manifest explicitly state no scientific extraction, render, or OCR. The 136-page source must be freshly extracted and mapped from the direct PDF. |
| DOC-003 | PDF pages 2-27 | PDF pages 1, 28-29 | Usable page-matched normalized native text exists for pages 2-27, with render/OCR support for pages 8-27. No retained page-level evidence exists for pages 1, 28, or 29. |

## Curation limitations

- Reused OCR and rendered pages are transcription/location aids; direct PDF remains authoritative for all later candidate confirmation.
- DOC-002's prior “Not Audited by Design” designation is a derivative-coverage gap, not a Workflow 1.5.1 scope exclusion. All 136 pages are assigned fresh-required.
- DOC-003 pages 1 and 28-29 are fresh-required even though older preprocessing called them out of scope.
