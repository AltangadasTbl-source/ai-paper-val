# Fresh Evidence-Asset Inventory — Workflow 1.5.2

This inventory was prepared directly from the three package PDFs.  No legacy audit extraction, OCR, candidate set, or report was read or reused.  All paths below are package-relative.

## Direct-source accounting

| Source ID | Direct source | Type | Bytes | SHA-256 | Likely role | Stable units | Fresh-preparation status |
|---|---|---|---:|---|---|---:|---|
| DOC-001 | `jama_barkin_2018_oi_180075.pdf` | PDF | 572,243 | `231de40e6ac86c81413c11d958fc410e49450ece9b6ddb0c22e2042d2c162e36` | Main randomized clinical-trial article; abstract, narrative, CONSORT figure, and results tables | 11 PDF pages | 11/11 complete |
| DOC-002 | `joi180075supp1_prod.pdf` | PDF | 1,614,109 | `b67c573979a4264284b87711cc2dd9ff7a74c2d709e1b045993f54624a4c6196` | Clinical-trial protocol packet: original/revised protocol, original/final statistical analysis plans, and amendments | 113 PDF pages | 113/113 complete |
| DOC-003 | `joi180075supp2_prod.pdf` | PDF | 261,375 | `5417d3ddc9769fa45832d8495fb337bcbeb2396276f08c79c81efa7626556a9a` | Supplementary online content: eTables 1-2 and eFigures 1-3 | 8 PDF pages | 8/8 complete |

**Total direct-source units:** 132 PDF pages.  There are no direct DOC, DOCX, XLS, XLSX, or CSV sources in this package; no Office conversion or Office-structure extraction was applicable.

## Tools and exact extraction commands

- `pdfinfo version 26.01.0` (Poppler); `pdftotext version 26.01.0` (Poppler); `pdftoppm` from the same Poppler installation; `tesseract 5.5.0` with `leptonica-1.86.0`, language `eng`, CPU invocation only.
- Metadata was saved with `pdfinfo -- "SOURCE.pdf" > ".ai_paper_validation/review_1_5_2/preprocessing/SOURCE.pdfinfo.txt"`.
- Native text was created with `pdftotext -- "SOURCE.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/native_text/SOURCE.txt"`.
- Layout text was created with `pdftotext -layout -- "SOURCE.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/layout_text/SOURCE.txt"`.
- Selected visual evidence was rendered at 180 dpi with `pdftoppm -f N -l N -singlefile -png -r 180 -- "SOURCE.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-XXX-pNNN"`.
- Targeted image text was created only for listed pages with `tesseract ".../DOC-XXX-pNNN.png" ".../DOC-XXX-pNNN" -l eng --psm 6`.

## Fresh derivatives

| Source ID | Metadata | Native text | Layout text |
|---|---|---|---|
| DOC-001 | `preprocessing/jama_barkin_2018_oi_180075.pdfinfo.txt` | `preprocessing/native_text/jama_barkin_2018_oi_180075.txt` (60,899 bytes) | `preprocessing/layout_text/jama_barkin_2018_oi_180075.txt` (108,600 bytes) |
| DOC-002 | `preprocessing/joi180075supp1_prod.pdfinfo.txt` | `preprocessing/native_text/joi180075supp1_prod.txt` (349,101 bytes) | `preprocessing/layout_text/joi180075supp1_prod.txt` (393,761 bytes) |
| DOC-003 | `preprocessing/joi180075supp2_prod.pdfinfo.txt` | `preprocessing/native_text/joi180075supp2_prod.txt` (8,947 bytes) | `preprocessing/layout_text/joi180075supp2_prod.txt` (13,787 bytes) |

## Page-level extraction and usability record

| Source ID | Exact PDF-page scope | Native/layout method and usability | Render decision and derivative scope | OCR decision and limitations |
|---|---|---|---|---|
| DOC-001 | pp. 1-11 (all 11 units) | Native and layout text are usable on every page for narrative, tables, CONSORT labels/counts, estimates, intervals, and P values. Layout text is the preferred derivative for Tables 1-2 and aligned displays. | Rendered all result-relevant main-article pages: `preprocessing/rendered_pages/DOC-001-p001.png` through `DOC-001-p011.png`. | No OCR: relevant native/layout text was usable throughout. Visual rendering preserves table/figure placement for mapping. |
| DOC-002 | pp. 1-113 (all 113 units) | Native and layout text are usable for prose and printed numeric/statistical content on pp. 1-107 and 110-113, including contents, protocol, revised protocol, power/sample-size displays, original SAP, final SAP, and amendments. On p. 108 and p. 111, prose is usable but native/layout extraction corrupts some displayed mathematical glyphs; use the rendered image plus targeted OCR for the equation identity. Page 109 is a short continuation page (179 extracted characters), but its printed continuation sentence and page label are usable in context. | Rendered visually structured/statistical pages: p. 014; pp. 018-021; pp. 037-047; pp. 069-071; pp. 092-102; and pp. 108-113 (36 pages), as `preprocessing/rendered_pages/DOC-002-pNNN.png`. These include schedules/tables, projected-trajectory figure, power/sample-size tables, analysis-plan text, and equations. Other protocol pages remain available in complete native/layout derivatives and did not require rendering for visual numeric recovery. | OCR was required only where relevant graphic/equation text was not usable natively: p. 039 (`ocr_text/DOC-002-p039.txt`), p. 108 (`...p108.txt`), p. 109 (`...p109.txt`), and p. 111 (`...p111.txt`). OCR supports visual comparison but imperfectly renders Greek/subscript notation; the rendered PNG remains authoritative for exact equation glyphs. |
| DOC-003 | pp. 1-4 | Native and layout text are usable for the supplementary-content index (p. 1) and eTable 1/eTable 2 values, labels, footnotes, estimates, CIs, and P values (pp. 2-4). | Rendered pp. 2-4 as `preprocessing/rendered_pages/DOC-003-p002.png` through `DOC-003-p004.png` to preserve table alignment and continuation. | No OCR: relevant tabular native/layout text was usable. |
| DOC-003 | pp. 5-8 | Native/layout text preserves captions but is incomplete for plotted curve/axis/legend content on the eFigure pages; p. 6 has only a copyright line in native extraction. | Rendered all figure pages: `preprocessing/rendered_pages/DOC-003-p005.png` through `DOC-003-p008.png`. | Targeted OCR: `ocr_text/DOC-003-p005.txt`, `...p006.txt`, `...p007.txt`, and `...p008.txt`. OCR captures captions and portions of labels/axes; p. 006 yields only copyright because its embedded visual has no reliably recognized text. Use the PNG, not OCR, for visual curve/legend inspection. |

## Render/OCR counts and source limitations

- Rendered evidence assets: 54 PNG pages (DOC-001: 11; DOC-002: 36; DOC-003: 7).
- OCR evidence assets: 8 text files (DOC-002: 4; DOC-003: 4).  No GPU was probed or used.
- No extraction tool was missing. PDF metadata reports 11, 113, and 8 pages respectively, matching the 132-unit accounting above.
- OCR is a navigation/comparison aid only. It is not a replacement for source PDFs or the rendered PNGs, especially for DOC-002 equation notation and DOC-003 plots.
- DOC-002 is a protocol/SAP packet rather than a results dataset. It supplies planned-model, population, time-point, and analysis-definition evidence; it does not itself provide a complete observed-results table.
