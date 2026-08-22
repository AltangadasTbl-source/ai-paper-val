# Direct Source Inventory — Workflow 1.5.1

Inventory completed from the package root using `file` and `pdfinfo`. The five direct sources are PDF files; no DOC, DOCX, XLS, XLSX, or CSV direct source was present. Direct-source SHA-256 values are recorded separately in `source_hashes_before.sha256`.

| Source ID | Package-relative source path | Format | Stable unit type | Total units | Text layer / direct-tool observation | Existing reusable coverage | Fresh direct-source mapping requirement |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_rathinam_2019_oi_190092.pdf | PDF 1.4 | PDF_PAGE | 10 | `pdfinfo` reports 10 letter-size pages; page-1 text layer is available. | Native layout-preserving text exists for pages 1–10. | None; all pages have usable reusable native text and remain subject to direct-source confirmation during recheck. |
| DOC-002 | joi190092supp1_prod.pdf | PDF 1.7 | PDF_PAGE | 16 | `pdfinfo` reports 16 letter-size pages; page-1 text layer is available. | Native layout-preserving text exists for pages 1–16. | None; all pages have usable reusable native text and remain subject to direct-source confirmation during recheck. |
| DOC-003 | joi190092supp2_prod.pdf | PDF 1.7 | PDF_PAGE | 153 | `pdfinfo` reports 153 letter-size pages; page-1 text layer is available. | No page-level OCR, native/layout text, table extraction, rendered-page set, or source-location map covers the 153 units. | All pages 1–153 require fresh direct-source extraction and mapping by the support evidence mapper. |
| DOC-004 | joi190092supp3_prod.pdf | PDF 1.3 | PDF_PAGE | 83 | `pdfinfo` reports 83 letter-size pages; page-1 text layer is available. | No page-level OCR, native/layout text, table extraction, rendered-page set, or source-location map covers the 83 units. | All pages 1–83 require fresh direct-source extraction and mapping by the support evidence mapper. |
| DOC-005 | joi190092supp4_prod.pdf | PDF 1.7 | PDF_PAGE | 1 | `pdfinfo` reports one letter-size page; page-1 text layer is available. | A document record identifies the source but no reusable page extraction exists. | Page 1 requires fresh direct-source extraction and mapping by the support evidence mapper. |

## Counts and gap partition

- Direct sources: 5.
- Unique direct-source units: 263 PDF pages.
- Units with usable reusable page extraction: 26.
- Fresh-required units: 237.
- Unit-location assignments made in `source_coverage.md`: 263.

## Inventory limitations

No Office or structured-data direct source was supplied. The existing audit area contains no OCR text, rendered page image, table/workbook extraction, or Office extraction eligible for reuse. Legacy candidate, checker, verifier, critic, endetail, and final-report files were intentionally not used as a discovery scope or scientific input.
