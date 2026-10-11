# Direct Source Inventory

Inventory scope: every direct PDF, DOC, DOCX, XLS, XLSX, and CSV file at the package root. No DOC, DOCX, XLS, XLSX, or CSV direct source was present. The three PDFs below are the complete direct-source set. Page counts were obtained with `pdfinfo` on 2026-09-02; the source SHA-256 snapshot is maintained in `source_hashes_before.sha256` by the coordinator.

| Source ID | Package-relative path | Format | Stable unit type | Total units | Direct identity and extraction observation |
|---|---|---|---|---:|---|
| DOC-001 | jama_zahid_2025_oi_250093_1768590553.08463.pdf | PDF 1.4 | PDF_PAGE | 9 | Main article; native text layer is present. PDF producer: iTextSharp.LGPLv2.Core 3.7.4.0. |
| DOC-002 | joi250093supp1_prod_1768590553.08963.pdf | PDF 1.6 | PDF_PAGE | 109 | Supplement 1; native text layer exists but direct first-page extraction is garbled, so page identity and content require fresh direct-source extraction/mapping. PDF producer: Acrobat Distiller 25.0. |
| DOC-003 | joi250093supp2_prod_1768590553.09463.pdf | PDF 1.6 | PDF_PAGE | 16 | Supplement 2; native text layer is present. PDF producer: Adobe PDF Library 25.1.108. |

## Unit identity

PDF page number is the stable unit for all three sources. The complete package total is 134 PDF pages (9 + 109 + 16). Reusable coverage is assessed separately in `source_coverage.md`; all pages remain in the 1.5.1 review scope regardless of a prior record's narrower audit selection.

## Curation boundaries

Existing candidate, checker, verifier, critic, endetail, queue, and final-report records were not read or used to determine source scope. The legacy extractor-response files are listed only as stale provenance assets because they do not provide a complete current page-level map; their contents were not used for scientific discovery.
