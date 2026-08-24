# Fresh Evidence-Asset Inventory

## Tooling and method record

All processing was new under `.ai_paper_validation/review_1_5_2/preprocessing/`. No legacy output was read, copied, or reused. The package contains only PDFs, so no Office conversion or Office structure extraction was applicable.

| Tool | Version observed | Use |
|---|---|---|
| `pdfinfo` | 26.01.0 | Direct PDF metadata and page-count determination. |
| `pdftotext` | 26.01.0 | Fresh native and layout-preserving extraction for every PDF. |
| `pdftoppm` | 26.01.0 | 200-dpi PNG rendering of selected result-relevant pages. |
| `tesseract` | 5.5.0 | Direct CPU-only English OCR (`--psm 6`) of the two pages with unusable relevant native/layout text. |
| `file` | system utility | Direct PDF type confirmation. |
| `sha256sum` | system utility | Direct-source integrity hashing. |

Commands were applied with explicit direct-source filenames:

```text
pdfinfo "jama_jabre_2018_oi_180004.pdf"
pdfinfo "joi180004supp1_prod.pdf"
pdfinfo "joi180004supp2_prod.pdf"
pdftotext "SOURCE.pdf" ".../preprocessing/native_text/SOURCE.txt"
pdftotext -layout "SOURCE.pdf" ".../preprocessing/layout_text/SOURCE.txt"
pdftoppm -r 200 -f N -l N -singlefile -png "SOURCE.pdf" ".../preprocessing/rendered_pages/DOC-NNN-pNNN"
tesseract ".../rendered_pages/DOC-002-p052.png" ".../ocr_text/DOC-002-p052" -l eng --psm 6
tesseract ".../rendered_pages/DOC-002-p103.png" ".../ocr_text/DOC-002-p103" -l eng --psm 6
```

`SOURCE.pdf` and `N` in the command record denote only the explicitly enumerated source/page scopes below; no unresolved source glob was used. OCR ran on the CPU through direct Tesseract invocation; no GPU was probed or invoked.

## Fresh native and layout text

| Source ID | Direct-source scope | Asset | Bytes | Method and assessment |
|---|---|---|---:|---|
| DOC-001 | PDF pp. 1-9 | `preprocessing/native_text/jama_jabre_2018_oi_180004.txt` | 53231 | Fresh `pdftotext`; usable narrative, flow, table, and result text on all pages. |
| DOC-001 | PDF pp. 1-9 | `preprocessing/layout_text/jama_jabre_2018_oi_180004.txt` | 86882 | Fresh `pdftotext -layout`; retained aligned table displays for visual comparison. |
| DOC-002 | PDF pp. 1-134 | `preprocessing/native_text/joi180004supp1_prod.txt` | 278554 | Fresh `pdftotext`; usable text on pp. 1-107 and 110-125. Direct PDF pp. 108-109 and 126-134 are blank/result-irrelevant. |
| DOC-002 | PDF pp. 1-134 | `preprocessing/layout_text/joi180004supp1_prod.txt` | 337197 | Fresh `pdftotext -layout`; retained protocol/SAP tables and aligned displays. Relevant content on pp. 52 and 103 was not sufficiently captured and is supplemented with fresh OCR below. |
| DOC-003 | PDF pp. 1-3 | `preprocessing/native_text/joi180004supp2_prod.txt` | 2412 | Fresh `pdftotext`; usable eTable text on pp. 2-3. |
| DOC-003 | PDF pp. 1-3 | `preprocessing/layout_text/joi180004supp2_prod.txt` | 4400 | Fresh `pdftotext -layout`; retained aligned eTable displays. |

## Rendered result-relevant pages

All following PNG assets are fresh 200-dpi direct renderings in `preprocessing/rendered_pages/`.

| Source ID | Rendered PDF pages | Evidence purpose |
|---|---|---|
| DOC-001 | 1, 4, 5, 6, 8 | Abstract/results; participant-flow figure; Tables 1-2; primary-result narrative. Assets: `DOC-001-p001.png`, `DOC-001-p004.png`, `DOC-001-p005.png`, `DOC-001-p006.png`, `DOC-001-p008.png`. |
| DOC-002 | 9-11, 15-17, 21-22, 24, 36-37, 50-54, 64-66, 70-72, 76-77, 79, 91-92, 101-105, 110-112, 114-117, 119-124 | Original/final protocol endpoints, population/target counts, statistical rules, scales, amendments, and SAP. Every rendered page has one asset named `DOC-002-pNNN.png`. |
| DOC-003 | 2-3 | eTable 1 centre contributions and eTable 2 post-hoc analyses. Assets: `DOC-003-p002.png`, `DOC-003-p003.png`. |

Rendered-page count: 52 (DOC-001: 5; DOC-002: 45; DOC-003: 2). Result-relevant pages not separately rendered remain freshly mapped through the complete native and layout extraction above; rendered pages were selected for tables, figures, endpoint/statistical definitions, amendments, and visual validation.

## Targeted fresh OCR decisions

| Source ID | PDF page | Native/layout decision | Fresh assets | OCR assessment |
|---|---:|---|---|---|
| DOC-002 | 52 | Relevant Intubation Difficulty Scale table had only a short heading in native/layout text (81 non-whitespace native characters); table content was unusable. | `preprocessing/rendered_pages/DOC-002-p052.png`; `preprocessing/ocr_text/DOC-002-p052.txt` | Fresh CPU Tesseract recovered the IDS parameter, score, and difficulty bands. Retain the rendered page as the visual authority because OCR has ordinary symbol/typographic imperfections. |
| DOC-002 | 103 | Relevant final-protocol Intubation Difficulty Scale table had only a short heading in native/layout text (101 non-whitespace native characters); table content was unusable. | `preprocessing/rendered_pages/DOC-002-p103.png`; `preprocessing/ocr_text/DOC-002-p103.txt` | Fresh CPU Tesseract recovered the IDS table and score bands. Retain the rendered page as the visual authority because OCR has ordinary symbol/typographic imperfections. |

No other result-relevant page required OCR: the fresh native plus layout text was usable. Blank DOC-002 pp. 108-109 and 126-134 were not OCR targets because they contain no result-relevant evidence.

## Limitations

- PDFs only: no conversion or Office-structure assets exist, by design.
- OCR is a convenience transcription for two visual scale tables, not a replacement for the cited source PDF or rendered PNG. Mathematical symbols/subscripts and a few typographic characters can be imperfectly recognized.
- DOC-002 includes blank pages (108-109 and 126-134) that remain in the 134-page direct-source coverage count; they have no extractable or result-relevant content.
