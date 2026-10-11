# Direct-Source Inventory — Workflow 1.5.1

Inventory date: 2026-09-02. Scope is the current package root only. Direct sources were identified by file extension (`.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.csv`) and inspected with `pdfinfo` where applicable. No Office or CSV direct source is present. No direct source was modified.

| Source ID | Package-relative source path | Format | Stable unit type | Total units | Identity/tool evidence | Reuse decision |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_garrison_2025_oi_250019_1749674951.29054.pdf | PDF | PDF_PAGE | 12 | `pdfinfo`: 12 pages; current SHA-256 differs from the legacy document record's source hash | All 12 pages require fresh direct-source extraction because legacy derivatives are stale. |
| DOC-002 | joi250019supp1_prod_1749674951.29554.pdf | PDF | PDF_PAGE | 18 | `pdfinfo`: 18 pages; current SHA-256 matches the legacy document record | All 18 pages require fresh direct-source extraction because no page-level reusable text/table extraction exists. |
| DOC-003 | joi250019supp2_prod_1749674951.30054.pdf | PDF | PDF_PAGE | 7 | `pdfinfo`: 7 pages; current SHA-256 matches the legacy document record | All 7 pages require fresh direct-source extraction because only metadata and two rights-review renders exist. |
| DOC-004 | joi250019supp3_prod_1749674951.30054.pdf | PDF | PDF_PAGE | 49 | `pdfinfo`: 49 pages; current SHA-256 differs from the legacy document record's source hash | All 49 pages require fresh direct-source extraction because legacy derivatives are stale. |

## Inventory totals

- Direct sources: 4 PDFs; 0 DOC/DOCX; 0 XLS/XLSX; 0 CSV.
- Stable source units: 86 PDF pages.
- Current source SHA-256 values are recorded separately in `source_hashes_before.sha256` by the coordinator.

## Source-integrity consequence

The current hashes for DOC-001 and DOC-004 do not match the hashes embedded in their legacy initial-document records. Their normalized text, rendered pages, OCR, manifests, and source-location maps are therefore `STALE` and cannot provide reusable coverage. DOC-002 and DOC-003 legacy metadata is source-matched but lacks sufficient page-level extraction for scientific mapping; metadata can be used only as a locator. The fresh-required partition is consequently 86 of 86 units.
