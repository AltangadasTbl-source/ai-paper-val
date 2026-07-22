# PDF Preprocessing Record - DOC-003

- **Source file:** `soi250075supp2_prod_1767031598.05318.pdf`
- **Inventory classification:** Results supplement.
- **Compliance status:** No AI Training Restriction Located in Provided Materials; no Human Compliance Review flag.
- **Selected scientific-audit range:** PDF pages 1-3 (all pages).
- **Scientific-processing status:** **Preprocessed and ready for results-supplement extraction.**
- **Extraction status:** Native text extracted page-by-page and normalized. Page 3 was additionally rendered and OCRed because it contains eTable 2, a results table required by later checks.
- **Source preservation:** Source PDF was not modified.

## Artifact index

| Artifact | Purpose |
|---|---|
| `preprocessing/page_manifest.md` | Page-level extraction method, quality assessment, and source-page provenance |
| `preprocessing/page-001-native.txt` through `page-003-native.txt` | Page-specific native PDF text |
| `preprocessing/page-001-normalized.txt` through `page-003-normalized.txt` | Source-page-tagged normalized native text |
| `preprocessing/DOC-003-normalized-native-text.txt` | Combined normalized native text, source-page ordered |
| `preprocessing/images/page-003-results-table-180dpi.png` | Rendered eTable 2 page for column-sensitive verification |
| `preprocessing/page-003-ocr.txt` | Noncanonical OCR search aid for the rendered eTable 2 page |

## Downstream-use note

Use pages 1-2 for eligibility context and page 3 for eTable 2 checks. For page 3, retain the native text for searchability but confirm table cells, inequalities, and column assignment against the linked image/source PDF.
