# PDF Preprocessing Record - DOC-001

- **Source file:** `jamasurgery_dat_2025_oi_250075_1767031598.03318.pdf`
- **Inventory classification:** Main article.
- **Compliance status:** Explicit AI Training Restriction; the Human Compliance Review authorization recorded on 2026-07-21 permits this workflow to continue. The authorization does not change the rights-screen classification.
- **Selected scientific-audit range:** PDF pages 1-9 only.
- **Excluded scientific range:** PDF page 10, which begins an Invited Commentary, is **Not Audited by Design** for main-study evidence.
- **Scientific-processing status:** **Preprocessed and released for main-text extraction and scientific checks on PDF pages 1-9.**
- **Extraction status:** Native text extracted page-by-page and normalized for pages 1-9. Pages 3-7 were additionally rendered and OCRed because they contain the CONSORT flow diagram (p. 3) or numbered result tables (Tables 1-4, pp. 4-7) required by later checks.
- **Source preservation:** Source PDF was not modified.

## Artifact index

| Artifact | Purpose |
|---|---|
| `preprocessing/page_manifest.md` | Page-level extraction method, quality assessment, selected scope, and source-page provenance |
| `preprocessing/page-001-native.txt` through `page-009-native.txt` | Page-specific native PDF text for the authorized scientific range |
| `preprocessing/page-001-normalized.txt` through `page-009-normalized.txt` | Source-page-tagged normalized native text |
| `preprocessing/DOC-001-normalized-native-text.txt` | Combined normalized native text for pages 1-9, in source-page order |
| `preprocessing/images/page-003-consort-flow-180dpi.png` | Rendered CONSORT flow diagram page for participant-flow verification |
| `preprocessing/images/page-004-table-1-180dpi.png` through `page-007-table-4-180dpi.png` | Rendered result-table pages for column-sensitive table/statistical verification |
| `preprocessing/page-003-ocr.txt` through `page-007-ocr.txt` | Noncanonical OCR search aids derived only from the selected rendered pages |

## Downstream-use note

Use the normalized native text for prose search and page-level sourcing. For the CONSORT diagram (p. 3) and Tables 1-4 (pp. 4-7), use the retained image/source PDF to confirm each branch, cell, column, comparison symbol, and footnote before recording evidence. Do not use page 10 as main-study evidence.
