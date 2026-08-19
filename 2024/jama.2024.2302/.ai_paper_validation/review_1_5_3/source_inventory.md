# Direct Source Inventory

This inventory contains every direct PDF and DOCX file in the current paper package. No XLS, XLSX, CSV, or DOC direct source is present. Source hashes are recorded in `source_hashes_before.sha256` with package-relative paths.

| Source ID | Package-relative path | File type | Stable unit definition and count | Direct inspection method | SHA-256 | Reusable coverage | Fresh-direct assignment |
|---|---|---|---|---|---|---|---|
| PDF-001 | jama_blakely_2024_oi_240020_1710443209.74411.pdf | PDF | PDF pages 1-10; 10 units | `pdfinfo` confirmed 10 pages. | `5398950bc5dc8eec3f9a9ddc35396780331ae5f94fa041f314b766900c73370a` | Native text and selected renders cover all 10 pages. | None; the main mapper must use the reusable assets with direct PDF confirmation for source evidence. |
| PDF-002 | joi240020supp1_prod_1710443209.74911.pdf | PDF | PDF pages 1-25; 25 units | `pdfinfo` confirmed 25 pages. | `1681c20dcb22840868bf25a80229d5d7b6960d127495313ad6c3b97ba6adf7da` | No reusable text, render, table, or page-level source map covers scientific content. | Support mapper: fresh direct-source extraction and mapping of pages 1-25. |
| PDF-003 | joi240020supp2_prod_1710443209.75411.pdf | PDF | PDF pages 1-10; 10 units | `pdfinfo` confirmed 10 pages. | `7732e7049179a37d93e4c7fc4f135b0e23240967b0b755a521553e58e5810b65` | No reusable text, render, table, or page-level source map covers scientific content. | Support mapper: fresh direct-source extraction and mapping of pages 1-10. |
| PDF-004 | joi240020supp3_prod_1710443209.75411.pdf | PDF | PDF pages 1-8; 8 units | `pdfinfo` confirmed 8 pages. | `2d9370fa728934f2efdae13c563d9fba39149a7a0f5a58781d4628aa8115b650` | Rendered pages cover pages 2-5; their paired native text is corrupted or sparse and is locator-only. | Support mapper: fresh direct-source extraction and mapping of pages 1 and 6-8; pages 2-5 require visual direct-PDF confirmation while reusing rendered pages. |
| DOCX-001 | Detailed_Errors_On_C1_C3_C5.docx | DOCX | `w:p` paragraph elements 1-237; 237 units. Five `w:tbl` elements are contained within these paragraph units and are recorded as structural locations, not additive units. | `file` confirmed a Word 2007+ document; package XML structure was counted without reading legacy candidate content. | `2d2d65eb1e208e400e7a60df176fc572a97354d4685eb53eebdeaafe8bd8665e` | No reusable Office extraction or paragraph/table map exists. This is a legacy-named auxiliary document and is not a candidate-discovery input. | Support mapper: fresh structural source-location mapping for paragraphs 1-237 and tables 1-5, while excluding its legacy candidate assertions from scientific discovery. |

## Stable-unit totals

- Unique direct sources: 5.
- Unique source units: 290.
- Reusable-backed units: 14.
- Fresh-required units: 276.
- Inventory-mapped and assigned units: 290.

`Mapped` in the coverage ledger means that every stable source unit has an exact reusable or fresh-direct assignment. It does not claim that scientific quantitative relationships have been mapped; that work belongs to the downstream mappers.

## Gaps and required handling

- PDF-002 and PDF-003 have document records only; these records identify the source but do not supply usable scientific extraction. All 35 PDF pages require fresh direct extraction.
- PDF-004 pages 1 and 6-8 have no reusable page derivative. Pages 2-5 have renders for visual confirmation, but their native text has documented corrupted glyphs or sparse extraction; derived text must not be treated as final source wording.
- DOCX-001 has no existing extraction. The legacy-oriented filename and content boundary require structural inventory only until a downstream mapper records exclusion from scientific candidate discovery.
- No OCR text, layout-text extraction, table extraction, workbook extraction, or source-linked CSV extraction exists below the prior audit area.
