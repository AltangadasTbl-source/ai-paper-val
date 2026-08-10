# PDF Preprocessing Manifest

Native PDF text was extracted before any rendering/OCR. OCR and PNG rendering were retained only for scoped pages with a required table, figure, or flow diagram. Source PDFs were read only.

| Document | Selected source pages | Native text quality | Rendered/OCR pages | Status |
|---|---|---|---|---|
| DOC-001-main-article | 1-11 | usable: 11 | 5-9 | Complete |
| DOC-003-results-supplement | 34-35, 38-66 | usable: 31 | 34-35, 38-66 | Complete |
| DOC-002-protocol | None | Not assessed by design | None | Not Audited by Design |

## Page-level records

The JSON companion contains the source PDF, source page, text-quality metrics, method, and every retained artifact path for each processed page.

## Quality limitations

- Native text is readable on all selected pages, but multicolumn journal text and tables can have non-linear reading order or collapsed word spacing.
- OCR text is an image-derived companion for visual checking; it is not a substitute for checking the retained page image when verifying table alignment, figure labels, or flow arrows.
- Excluded supplement pages, including pp. 36-37, and the entire protocol were not processed for scientific content by design.
