# Source and Reused-Evidence Coverage

This map records the complete source-location coverage available before scientific extraction. A
reused text or image is a locator/transcription aid only; direct sources remain final authority.

## DOC-001 — `jama_flint_2019_oi_190079.pdf`

| Exact PDF scope | Reused coverage | Fitness | Downstream requirement |
|---|---|---|---|
| p. 1 | Native layout text; duplicate normalized text; duplicate full-document rights text | `USABLE` | Confirm any candidate against direct PDF p. 1 |
| p. 2 | Native layout text; duplicate normalized text; duplicate full-document rights text | `USABLE` | Confirm any candidate against direct PDF p. 2 |
| p. 3 | Native/normalized text; 300-dpi PNG; OCR text and metadata (mean confidence 0.8923); duplicate full text | `USABLE` | Use image/OCR for Figure 1 location, then confirm against direct PDF p. 3 |
| p. 4 | Native layout text; duplicate normalized text; duplicate full-document rights text | `USABLE` | Confirm any candidate against direct PDF p. 4 |
| p. 5 | Native/normalized text; 300-dpi PNG; OCR text and metadata (mean confidence 0.8646); duplicate full text | `USABLE` | Table layout requires image/direct-PDF corroboration on p. 5 |
| p. 6 | Native/normalized text; 200-dpi PNG; OCR text and metadata (mean confidence 0.8904); duplicate full text | `USABLE` | Ignore stale manifest confidence; use page metadata and direct PDF p. 6 |
| p. 7 | Native/normalized text; 200-dpi PNG; OCR text and metadata (mean confidence 0.8404); duplicate full text | `USABLE` | Manifest incorrectly says OCR was not run; confirm against direct PDF p. 7 |
| p. 8 | Over-expanded native/normalized text; 150-dpi PNG; OCR text and metadata (mean confidence 0.8795); duplicate full text | `PARTIAL` | Native reading order is unusable; use OCR/image only as aids and confirm every value against direct PDF p. 8 |
| p. 9 | Native/normalized text; 200-dpi PNG; OCR text and metadata (mean confidence 0.9003); duplicate full text | `USABLE` | Manifest incorrectly says OCR was not run; confirm against direct PDF p. 9 |
| p. 10 | Native layout text; duplicate normalized text; duplicate full-document rights text | `USABLE` | Confirm any candidate against direct PDF p. 10 |

DOC-001 source coverage is 10/10 pages. The page-manifest metadata is stale for OCR availability on
pages 7-9, but the page-level files close the evidence-asset location gap.

## DOC-002 — `joi180151supp1_prod.pdf`

| Exact PDF scope | Reused coverage | Fitness | Downstream requirement |
|---|---|---|---|
| p. 1 | Full-document layout text with page delimiter; document map | `USABLE` | Confirm source identity/title against direct PDF p. 1 |
| pp. 2-7 | Full-document layout text with exact page delimiters; document map identifies protocol sections through p. 7 | `USABLE` | Map all result-relevant protocol definitions from the full text; confirm any candidate against the exact direct PDF page |

DOC-002 source coverage is 7/7 pages. There are no reusable page images, OCR files, or page-level text
files; the current full-layout text nevertheless reproduces the entire source text layer exactly.

## DOC-003 — `joi180151supp2_prod.pdf`

| Exact PDF scope | Reused coverage | Fitness | Downstream requirement |
|---|---|---|---|
| p. 1 | Full-document layout text with page delimiter; document map/table of contents | `USABLE` | Confirm headings against direct PDF p. 1 |
| pp. 2-6 | Full-document layout text; document map identifies eMethods and model-selection locations | `USABLE` | Map quantitative/statistical definitions and confirm exact locations in direct PDF |
| pp. 7-9 | Full-document layout text; document map identifies eTable 1 | `PARTIAL` | Table structure may not be fully preserved; inspect direct PDF pages 7-9 |
| pp. 10-14 | Full-document layout text; document map identifies eTable 2 | `PARTIAL` | Table structure may not be fully preserved; inspect direct PDF pages 10-14 |
| p. 15 | Full-document layout text; document map identifies eTable 3 | `PARTIAL` | Inspect direct PDF p. 15 for exact cells/labels |
| p. 16 | Full-document layout text; document map identifies eTable 4 | `PARTIAL` | Inspect direct PDF p. 16 for exact cells/labels |
| p. 17 | Full-document layout text; document map identifies eTable 5 | `PARTIAL` | Inspect direct PDF p. 17 for exact cells/labels |
| p. 18 | Full-document layout text; document map identifies eTable 6 | `PARTIAL` | Inspect direct PDF p. 18 for exact cells/labels |
| pp. 19-26 | Full-document layout text; document map identifies eFigures 1-4 | `PARTIAL` | Figure geometry/graphics are not represented by text alone; inspect direct PDF pages 19-26 and render targeted pages if necessary |
| pp. 27-29 | Full-document layout text; document map identifies references | `USABLE` | Direct PDF remains authority if any location is used |

DOC-003 source coverage is 29/29 pages at the text-layer level. Reused evidence is partial for visual
table/figure structure on pages 7-26 because no rendered pages or OCR exist for this document.

## Complete coverage and gaps summary

- Every direct source file and all 46 PDF pages are registered.
- Reused text reaches all 46 pages: DOC-001 has page-level layout text; DOC-002 and DOC-003 have exact
  current full-document layout text with one form-feed delimiter per source page.
- Reused rendered pages exist only for DOC-001 pp. 3 and 5-9.
- Reused OCR exists only for DOC-001 pp. 3 and 5-9.
- No reusable table extraction, workbook extraction, Office structure, CSV map, or locally converted
  Office PDF exists, and no Office/CSV direct source is present.
- The missing visual derivatives do not exclude any page. They require direct-PDF review and, only if
  exact confirmation cannot otherwise be made, targeted new rendering/OCR under the contract.

