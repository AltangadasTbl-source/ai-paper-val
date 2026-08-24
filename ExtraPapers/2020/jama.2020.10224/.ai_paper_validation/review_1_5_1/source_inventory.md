# Direct Source Inventory

This inventory was prepared from package-root file enumeration and direct `file` and `pdfinfo` inspection. Direct-source discovery was limited to supplied PDF, DOC, DOCX, XLS, XLSX, and CSV files. No legacy candidate, verifier, critic, endetail, review-queue, or final-report content was read or used as a discovery boundary.

## Direct sources

| Source ID | Package-relative path | Type | Stable unit type | Total units | Direct inspection | SHA-256 | Notes |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_okereke_2020_oi_200066.pdf | PDF | PDF_PAGE | 10 | PDF 1.4; letter pages; 10 pages | 5d7ca4528c3c0d6c32e105598d4d862726b54a72ef8b76dfd3200de12b05b50e | Main article. Stable units are PDF pages 1 through 10. |
| DOC-002 | joi200066supp1_prod.pdf | PDF | PDF_PAGE | 31 | PDF 1.5; letter pages; 31 pages | 0a3b7b0905eaa8152dbf9b3b675992fc80ec8a35b258ca236a428bce81ffbe07 | Protocol summary. Stable units are PDF pages 1 through 31. |
| DOC-003 | joi200066supp2_prod.pdf | PDF | PDF_PAGE | 48 | PDF 1.6; letter pages; 48 pages | efba5b6eeb6411c34ce02f9fb123ab90161c2b63c7e685298690959601a7be81 | Supplementary methods, results, tables, and figures. Stable units are PDF pages 1 through 48. |
| DOC-004 | joi200066supp3_prod.pdf | PDF | PDF_PAGE | 2 | PDF 1.4; A4 pages; 2 pages | 4f48f06519cc7ddcfd8d914c9aa52381b1557c3f95efdcf9aa5000757644924e | Data-sharing statement. Stable units are PDF pages 1 through 2. |

The direct-source total is 91 unique PDF-page units. No package-root DOC, DOCX, XLS, XLSX, or CSV direct source was present.

## Assessed non-source package graphic

`joi200066_featured.png` is a 1600 by 840 RGB PNG package graphic. It is not one of the requested direct-source file types and does not supply an independent direct scientific record. It is therefore classified as a non-source package graphic, not a direct scientific source and not a source-coverage row. Its derived OCR is retained in the evidence-asset inventory only as graphic provenance; it does not create a direct-source unit or fresh-mapping obligation.

## Inventory method and boundary

Direct tools used were `file` 5.46, `pdfinfo` 26.01.0, and `sha256sum` 0.8.0. `pdfinfo` page totals establish the stable page-unit counts. The direct-source hashes are recorded separately in `source_hashes_before.sha256` by the coordinator. No source file was modified.
