# Fresh Evidence-Asset Inventory

All assets below were freshly generated from direct package sources. No previous audit derivative was used as an input.

## Tools and versions

| Tool | Version | Use |
|---|---|---|
| pdfinfo | 26.01.0 | PDF page count, metadata, encryption, and dimensions |
| pdftotext | 26.01.0 | Native text and `-layout` table-preserving text |
| pdftoppm | 26.01.0 | CPU PDF-to-PNG rendering at 150 dpi |
| tesseract | 5.5.0 | Available CPU OCR backend; not invoked because no result-relevant page had unusable native/layout text |

## Per-source assets and extraction decisions

| Source ID | Fresh assets | Exact command pattern used | Page scope | Result-relevant visual scope | OCR decision and limitation |
|---|---|---|---|---|---|
| DOC-001 | `preprocessing/metadata/DOC-001_pdfinfo.txt`; `preprocessing/native_text/DOC-001.txt`; `preprocessing/layout_text/DOC-001.txt`; `preprocessing/rendered_pages/DOC-001-01.png` through `DOC-001-10.png`; page probes `preprocessing/metadata/DOC-001-p1.txt`, `p4.txt`, `p7.txt`, `p8.txt` | `pdfinfo`; `pdftotext`; `pdftotext -layout`; `pdftoppm -r 150 -f 1 -l 10 -png` | Native/layout text and rendering: PDF pages 1-10 | Rendered all pages 1-10; primary tables/figures visually checked on pages 4-7 | **No OCR.** Native and layout text were usable for all result-relevant content; page renders preserve table/figure placement for exact visual checking. |
| DOC-002 | `preprocessing/metadata/DOC-002_pdfinfo.txt`; `preprocessing/native_text/DOC-002.txt`; `preprocessing/layout_text/DOC-002.txt`; `preprocessing/rendered_pages/DOC-002-001.png` through `DOC-002-194.png`; page probes `preprocessing/metadata/DOC-002-p19.txt`, `p28.txt`, `p71.txt`, `p73.txt`, `p82.txt`, `p83.txt`, `p139.txt`, `p179.txt`, `p189.txt`, `p190.txt`, `p191.txt`, `p192.txt`, `p193.txt`, `p194.txt` | `pdfinfo`; `pdftotext`; `pdftotext -layout`; `pdftoppm -r 150 -f 1 -l 194 -png` | Native/layout text and rendering: PDF pages 1-194 | Rendered every page 1-194, including protocol/SAP-definition pages and DSMC result pages 188-194; page 189 render visually checked and has readable table and charts | **No OCR.** Result-relevant protocol, SAP, DSMC table, and figure pages have usable native/layout text plus readable renders. Pages 140-162 are embedded blank/non-substantive pages, not an OCR gap. |
| DOC-003 | `preprocessing/metadata/DOC-003_pdfinfo.txt`; `preprocessing/native_text/DOC-003.txt`; `preprocessing/layout_text/DOC-003.txt`; `preprocessing/rendered_pages/DOC-003-01.png` through `DOC-003-24.png`; page probes `preprocessing/metadata/DOC-003-p1.txt` through `DOC-003-p24.txt` | `pdfinfo`; `pdftotext`; `pdftotext -layout`; `pdftoppm -r 150 -f 1 -l 24 -png` | Native/layout text and rendering: PDF pages 1-24 | Rendered all pages 1-24 (all are supplementary quantitative results, tables, figures, or analytic definitions) | **No OCR.** Native/layout extraction is usable; renders supply table/figure visual evidence where reading order is not sufficient. |
| DOC-004 | `preprocessing/metadata/DOC-004_pdfinfo.txt`; `preprocessing/native_text/DOC-004.txt`; `preprocessing/layout_text/DOC-004.txt`; `preprocessing/rendered_pages/DOC-004-1.png`; page probe `preprocessing/metadata/DOC-004-p1.txt` | `pdfinfo`; `pdftotext`; `pdftotext -layout`; `pdftoppm -r 150 -f 1 -l 1 -png` | Native/layout text and rendering: PDF page 1 | Rendered page 1 | **No OCR.** The data-sharing statement's native and layout text are readable and it contains no result display. |

## Completeness and naming note

`pdftoppm` pads each output sequence to the width needed for that sequence: DOC-001 and DOC-003 use two-digit suffixes, DOC-002 uses three-digit suffixes (for example, `DOC-002-001.png` and `DOC-002-194.png`), and the one-page DOC-004 render is `DOC-004-1.png`. Together the source has exactly 194 DOC-002 PNG assets and 229 rendered PDF-page assets.

## OCR decision record

The CPU-only OCR policy was assessed after native and layout extraction and visual rendering. No OCR unit was created: **0 pages** required OCR. This is a decision, not a missing-tool condition. No GPU was probed or invoked.
