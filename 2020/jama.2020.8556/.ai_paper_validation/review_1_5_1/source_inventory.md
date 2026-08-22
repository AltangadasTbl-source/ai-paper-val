# Direct Source Inventory

Inventory method: package-root filename scan for PDF, DOC, DOCX, XLS, XLSX, and CSV; direct `pdfinfo` inspection for every PDF. No Office, workbook, or CSV direct source was present. The four source PDFs are immutable supplied inputs and are separately recorded in `source_hashes_before.sha256` by the coordinator.

| Source ID | Package-relative path | Format | Stable unit type | Units | Direct inspection | Content role | Reusable extraction coverage | Fresh mapping assignment |
|---|---|---|---|---:|---|---|---|---|
| DOC-001 | jama_butler_2020_oi_200054.pdf | PDF | PDF_PAGE | 10 | PDF 1.4; letter; text layer available | Main article | Native text covers PDF pp. 1-10; page renders cover pp. 4-7 | None; all pages are reusable-backed for the main mapper. |
| DOC-002 | joi200054supp1_prod.pdf | PDF | PDF_PAGE | 76 | PDF 1.6; A4; text layer available | Protocol/support source | No reusable page extraction, render, OCR, table, or location-map extraction is usable for the current full-coverage contract | Support mapper: fresh direct native/layout extraction and source mapping for PDF pp. 1-76, including blank-page confirmation where applicable. |
| DOC-003 | joi200054supp2_prod.pdf | PDF | PDF_PAGE | 13 | PDF 1.7; A4; text layer available | Results supplement | Native text covers PDF pp. 1-13; page renders cover pp. 4-13 | None; all pages are reusable-backed for the support mapper. |
| DOC-004 | joi200054supp3_prod.pdf | PDF | PDF_PAGE | 1 | PDF 1.4; A4; text layer available | Data-sharing/support source | No reusable page extraction, render, OCR, table, or location-map extraction is usable for the current full-coverage contract | Support mapper: fresh direct native/layout extraction and source mapping for PDF p. 1. |

## Stable-unit and gap accounting

- Unique direct sources: 4.
- Unique direct source units: 100 PDF pages.
- Reusable-backed units: 23 PDF pages (DOC-001 pp. 1-10; DOC-003 pp. 1-13).
- Fresh-required units: 77 PDF pages (DOC-002 pp. 1-76; DOC-004 p. 1).
- No direct DOC, DOCX, XLS, XLSX, or CSV source exists in this package.
- No reusable table/workbook extraction exists. The reusable main and supplement evidence maps are partial locator aids, not a replacement for the complete per-page native-text coverage.

## Exact downstream mapping scopes

- Main quantitative mapper: DOC-001 PDF pp. 1-10, using the page-matched native text and direct PDF confirmation; visually confirm tables/figure on pp. 4-7 with the existing renders.
- Support quantitative mapper, reusable-backed shard: DOC-003 PDF pp. 1-13, using page-matched native text and direct PDF confirmation; visually confirm eTables/eFigures on pp. 4-13 with the existing renders.
- Support quantitative mapper, fresh-direct shard: DOC-002 PDF pp. 1-76 and DOC-004 PDF p. 1. Extract native/layout text directly from the supplied PDFs and map every page, including blank or administrative pages, before scientific relationship screening.

## Asset limitations that do not leave a source-coverage gap

- DOC-001 OCR and its metadata exist on pp. 4-7, but they duplicate the stronger native text and are not used to increase reusable-unit counts.
- DOC-003 has no OCR; page renders supply visual confirmation for pp. 4-13 and native text supplies reusable coverage for every page.
- Older document manifests that call DOC-002 or DOC-004 not audited are stale relative to this workflow's all-direct-source coverage requirement; their pages are explicitly fresh-required above.
