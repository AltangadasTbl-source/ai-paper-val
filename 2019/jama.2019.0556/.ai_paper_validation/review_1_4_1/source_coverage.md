# Source and Reused-Evidence Coverage

## Page-level coverage map

| Document | Direct-source scope | Reusable document/page maps | Reusable native page text | Reusable OCR text and rendered pages | Explicit reusable-evidence gaps | Coverage direction for downstream stages |
|---|---|---|---|---|---|---|
| DOC-001 | `jama_bot_2019_oi_190007.pdf`, pp. 1-11 | Page manifest records pp. 1-11 | pp. 1-11 | pp. 3, 5-8 | No page-level text gap. No rendered/OCR asset for pp. 1-2, 4, 9-11; no separate layout or structured-table extraction. | Map all pp. 1-11 from native page text; use OCR/rendered pages for visual displays; confirm candidate evidence in the direct PDF. |
| DOC-002 | `joi190007supp1_prod.pdf`, pp. 1-60 | Document identity/page count only | None | None | pp. 1-60 lack reusable page-level evidence assets. | Old protocol exclusion is void. Inspect direct PDF wherever complete mapping or a cross-source definition/comparison requires it. |
| DOC-003 | `joi190007supp2_prod.pdf`, pp. 1-5 | Document identity/page count only | None | None | pp. 1-5 lack reusable page-level evidence assets. | Old SAP exclusion is void. Inspect direct PDF for statistical definitions and result-linked comparisons as required. |
| DOC-004 | `joi190007supp3_prod.pdf`, pp. 1-25 | Page records for pp. 1-2, 16-23; excluded-page list names pp. 3-15, 24-25 without evidence records | pp. 1-2, 16-23 | pp. 16-23 | pp. 3-15 and 24-25 lack reusable page-level evidence assets; pp. 1-2 lack OCR/rendering; no separate layout or structured-table extraction. | Reuse mapped pages completely, and inspect direct PDF for the 15 unmapped pages when result relevance or definitions cannot be excluded from source evidence. |
| DOC-005 | `joi190007supp4_prod.pdf`, p. 1 | Document identity/page count only | None | None | p. 1 lacks reusable page-level evidence assets. | Use direct PDF if package-wide mapping identifies a quantitative, definition, or cross-source relevance; do not rely on the old administrative exclusion as a scientific boundary. |

## Aggregate coverage

| Evidence level | Covered source pages | Coverage |
|---|---:|---:|
| Direct PDF availability | 102 of 102 | 100% |
| Reusable page-level native text | 21 of 102 | 20.6% |
| Reusable OCR text | 13 of 102 | 12.7% |
| Reusable rendered page image | 13 of 102 | 12.7% |
| Reusable structured table/workbook/CSV extraction | 0 | None present |
| Separately identified reusable layout text | 0 | None present |

There are 81 source pages without reusable page-level text: DOC-002 pp. 1-60, DOC-003 pp. 1-5, DOC-004 pp. 3-15 and 24-25, and DOC-005 p. 1. This is a preprocessing/reuse gap, not permission to sample or omit result-relevant source content.

## Fitness and integrity conclusions

- Current source hashes match the identities recorded in the reusable preprocessing manifest, so reusable assets are source-matched at document level.
- All 21 native page-text files, 13 OCR text files, and 13 PNG files are present and nonempty/readable.
- OCR metadata reports completed Tesseract CPU processing but supplies no mean confidence, exact command, or Tesseract version. OCR is therefore a locator/transcription aid, not final authority.
- Native extraction and rendering commands/tool versions are not recorded. Page manifests provide stable source-page mappings, but no distinct layout-text or structured-table output exists.
- The old package manifest and document-status records contain stale audit boundaries and dispositions. Only identity/page metadata is reusable; those fields cannot restrict Workflow 1.4.1 discovery.
- Aggregate `normalized_text.txt` files duplicate the more precise page-level text sets and should not replace page-specific citations.

## Required gap handling

Downstream mappers should begin with all reusable evidence represented by DOC-001 pp. 1-11 and DOC-004 pp. 1-2, 16-23. They must then use direct-source inspection for result-relevant content or necessary definitions in the 81-page derivative gap. Any targeted extraction created later belongs under `review_1_4_1/preprocessing/`; it is new evidence, not part of this before-hash reuse set.
