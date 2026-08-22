# Direct Source Inventory

Inventory timestamp: 2026-08-18T23:20:42Z. This inventory covers every root-level direct source with a supported source extension. No DOC, DOCX, XLS, XLSX, or CSV direct source was present. Stable unit counts use PDF pages from `pdfinfo`.

| Source ID | Package-relative source path | Format | Stable unit type | Total units | Text layer | Document classification | Reusable-asset coverage | Fresh direct-source assignment |
|---|---|---|---|---:|---|---|---|---|
| DOC-001 | jama_parsons_2020_oi_190140.pdf | PDF | PDF_PAGE | 9 | Available | Main article | Native and normalized page text maps every page 1-9; targeted page images/OCR also exist for pages 4-7. | No page is initially fresh-required; mapper must use the source PDF for final evidence confirmation. |
| DOC-002 | joi190140supp1_prod.pdf | PDF | PDF_PAGE | 60 | Available | Protocol | No page-level reusable text, layout text, OCR, table extraction, or rendered-page asset exists. | Fresh direct-source native/layout extraction and mapping: PDF pages 1-60. |
| DOC-003 | joi190140supp2_prod.pdf | PDF | PDF_PAGE | 11 | Available | Statistical analysis plan | No page-level reusable text, layout text, OCR, table extraction, or rendered-page asset exists. | Fresh direct-source native/layout extraction and mapping: PDF pages 1-11. |
| DOC-004 | joi190140supp3_prod.pdf | PDF | PDF_PAGE | 3 | Available | Results supplement | Native and normalized page text maps pages 1-3; page images/OCR cover pages 2-3 and a rendered page is mapped to page 3. | No page is initially fresh-required; mapper must use the source PDF for final evidence confirmation. |
| DOC-005 | joi190140supp4_prod.pdf | PDF | PDF_PAGE | 1 | Available | Administrative data-sharing statement | No page-level reusable text, layout text, OCR, table extraction, or rendered-page asset exists. | Fresh direct-source native/layout extraction and mapping: PDF page 1. |

## Counts and gap assignment

- Direct sources: 5 PDFs; 0 DOC/DOCX/XLS/XLSX/CSV files.
- Unique source units: 84 PDF pages.
- Reusable-backed units: 12 pages (DOC-001 pages 1-9; DOC-004 pages 1-3).
- Fresh-required units: 72 pages (DOC-002 pages 1-60; DOC-003 pages 1-11; DOC-005 page 1).
- The legacy document classifications are retained only as document-map metadata. They do not remove any direct source or page from Workflow 1.5.1 source coverage.

