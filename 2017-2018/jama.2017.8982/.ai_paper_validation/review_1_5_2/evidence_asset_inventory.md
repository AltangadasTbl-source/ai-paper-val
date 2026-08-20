# Fresh Evidence Asset Inventory

## Scope and integrity boundary

This inventory was prepared afresh from the three direct PDF scientific sources only. No prior audit extraction, OCR, candidate record, or report was consulted. The source PDFs were read only. All newly created derivatives are under `preprocessing/`. Every shorter derivative path in the inventory tables below (for example, `metadata/...`, `native_text/...`, `layout_text/...`, `page_text/...`, or `rendered_pages/...`) is explicitly relative to that directory; its review-root-relative path is `preprocessing/` plus the displayed path.

## Toolchain and exact commands

- `pdfinfo version 26.01.0`
- `pdftotext version 26.01.0`
- `pdftoppm version 26.01.0`
- `tesseract 5.5.0` (available but not invoked)

For each source, the following direct commands were run with the literal source filename:

```text
pdfinfo "SOURCE.pdf" > preprocessing/metadata/DOC-ID_pdfinfo.txt
pdftotext "SOURCE.pdf" preprocessing/native_text/DOC-ID.txt
pdftotext -layout "SOURCE.pdf" preprocessing/layout_text/DOC-ID.txt
pdftotext -f PAGE -l PAGE "SOURCE.pdf" preprocessing/page_text/native/DOC-ID-pPAGE.txt
pdftotext -layout -f PAGE -l PAGE "SOURCE.pdf" preprocessing/page_text/layout/DOC-ID-pPAGE.txt
pdftoppm -f PAGE -l PAGE -singlefile -r 200 -png "SOURCE.pdf" preprocessing/rendered_pages/DOC-ID-pPAGE
```

The last three commands were run separately for every page in its recorded page range. Rendering all pages is a conservative result-relevant-page procedure; it preserves every table, figure, caption, and narrative page for subsequent mapping. `tesseract` was not run: native and layout text were usable for every page containing scientific or result-relevant material. DOC-002 p. 21 is a visually confirmed, otherwise blank printed page containing only page number 894, so it contains no result-relevant material and does not warrant OCR.

## Source-level assets

| Source ID | Direct source and role | PDF units | Fresh outputs | Native / layout total bytes | Limitation |
|---|---|---:|---|---:|---|
| DOC-001 | `jama_moon_2017_oi_170077.pdf` — main randomized clinical trial article | 9 pages | `metadata/DOC-001_pdfinfo.txt`; `native_text/DOC-001.txt`; `layout_text/DOC-001.txt`; 9 native-page files; 9 layout-page files; 9 PNG renders | 53,139 / 144,453 | Text extraction is usable; visual renders retained for dense tables/figures and page-layout confirmation. |
| DOC-002 | `joi170077supp1_prod.pdf` — trial protocol / supporting research strategy | 21 pages | `metadata/DOC-002_pdfinfo.txt`; `native_text/DOC-002.txt`; `layout_text/DOC-002.txt`; 21 native-page files; 21 layout-page files; 21 PNG renders | 79,698 / 84,954 | p. 21 is only printed page number 894; no scientific content. All other page text is usable. |
| DOC-003 | `joi170077supp2_prod.pdf` — supplementary tables, figure, and references | 12 pages | `metadata/DOC-003_pdfinfo.txt`; `native_text/DOC-003.txt`; `layout_text/DOC-003.txt`; 12 native-page files; 12 layout-page files; 12 PNG renders | 11,823 / 18,300 | Some table pages have low native-text byte counts because of sparse tabular layout; layout text plus a 200-dpi render is usable for the displayed evidence. |

## Complete page-level extraction and OCR decision inventory

`Native bytes` is the byte count of the freshly direct-extracted page text file. `Rendered` identifies the fresh 200-dpi PNG. “Yes” in the result-relevant column means the page was conservatively retained for scientific/result mapping; it does not itself assert that every line is an outcome result.

| Source ID | PDF page | Result-relevant retained | Native bytes | Native/layout assessment | Rendered asset | OCR decision and reason |
|---|---:|---|---:|---|---|---|
| DOC-001 | 1 | Yes | 4,502 | Usable narrative and abstract text; layout usable. | `rendered_pages/DOC-001-p1.png` | Not run — usable native/layout text. |
| DOC-001 | 2 | Yes | 6,255 | Usable narrative text; layout usable. | `rendered_pages/DOC-001-p2.png` | Not run — usable native/layout text. |
| DOC-001 | 3 | Yes | 6,489 | Usable narrative and methods text; layout usable. | `rendered_pages/DOC-001-p3.png` | Not run — usable native/layout text. |
| DOC-001 | 4 | Yes | 4,948 | Usable narrative and methods text; layout usable. | `rendered_pages/DOC-001-p4.png` | Not run — usable native/layout text. |
| DOC-001 | 5 | Yes | 3,751 | Usable narrative/results text; layout usable. | `rendered_pages/DOC-001-p5.png` | Not run — usable native/layout text. |
| DOC-001 | 6 | Yes | 5,998 | Usable results/table text; layout usable. | `rendered_pages/DOC-001-p6.png` | Not run — usable native/layout text. |
| DOC-001 | 7 | Yes | 5,563 | Usable results/table text; layout usable. | `rendered_pages/DOC-001-p7.png` | Not run — usable native/layout text. |
| DOC-001 | 8 | Yes | 6,947 | Usable results/table text; layout usable. | `rendered_pages/DOC-001-p8.png` | Not run — usable native/layout text. |
| DOC-001 | 9 | Yes | 8,686 | Usable final table/reference text; layout usable. | `rendered_pages/DOC-001-p9.png` | Not run — usable native/layout text. |
| DOC-002 | 1 | Yes | 4,380 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p1.png` | Not run — usable native/layout text. |
| DOC-002 | 2 | Yes | 4,159 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p2.png` | Not run — usable native/layout text. |
| DOC-002 | 3 | Yes | 4,707 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p3.png` | Not run — usable native/layout text. |
| DOC-002 | 4 | Yes | 4,209 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p4.png` | Not run — usable native/layout text. |
| DOC-002 | 5 | Yes | 3,679 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p5.png` | Not run — usable native/layout text. |
| DOC-002 | 6 | Yes | 4,273 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p6.png` | Not run — usable native/layout text. |
| DOC-002 | 7 | Yes | 4,578 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p7.png` | Not run — usable native/layout text. |
| DOC-002 | 8 | Yes | 4,132 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p8.png` | Not run — usable native/layout text. |
| DOC-002 | 9 | Yes | 4,550 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p9.png` | Not run — usable native/layout text. |
| DOC-002 | 10 | Yes | 4,682 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p10.png` | Not run — usable native/layout text. |
| DOC-002 | 11 | Yes | 3,716 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p11.png` | Not run — usable native/layout text. |
| DOC-002 | 12 | Yes | 4,449 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p12.png` | Not run — usable native/layout text. |
| DOC-002 | 13 | Yes | 4,658 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p13.png` | Not run — usable native/layout text. |
| DOC-002 | 14 | Yes | 4,202 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p14.png` | Not run — usable native/layout text. |
| DOC-002 | 15 | Yes | 3,724 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p15.png` | Not run — usable native/layout text. |
| DOC-002 | 16 | Yes | 3,695 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p16.png` | Not run — usable native/layout text. |
| DOC-002 | 17 | Yes | 3,904 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p17.png` | Not run — usable native/layout text. |
| DOC-002 | 18 | Yes | 3,448 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p18.png` | Not run — usable native/layout text. |
| DOC-002 | 19 | Yes | 3,751 | Usable protocol narrative text; layout usable. | `rendered_pages/DOC-002-p19.png` | Not run — usable native/layout text. |
| DOC-002 | 20 | Yes | 796 | Usable reference/closing text; layout usable. | `rendered_pages/DOC-002-p20.png` | Not run — usable native/layout text. |
| DOC-002 | 21 | No | 6 | Visually confirmed page number only (894); no scientific evidence. | `rendered_pages/DOC-002-p21.png` | Not run — no result-relevant material to OCR. |
| DOC-003 | 1 | Yes | 1,414 | Usable supplement contents text; layout usable. | `rendered_pages/DOC-003-p1.png` | Not run — usable native/layout text. |
| DOC-003 | 2 | Yes | 679 | Usable video-topic table text; layout usable. | `rendered_pages/DOC-003-p2.png` | Not run — usable native/layout text. |
| DOC-003 | 3 | Yes | 1,600 | Usable demographic-table text; layout usable. | `rendered_pages/DOC-003-p3.png` | Not run — usable native/layout text. |
| DOC-003 | 4 | Yes | 281 | Usable continuation-table text with layout/render support. | `rendered_pages/DOC-003-p4.png` | Not run — layout and render usable. |
| DOC-003 | 5 | Yes | 1,923 | Usable baseline-characteristics table text; layout usable. | `rendered_pages/DOC-003-p5.png` | Not run — usable native/layout text. |
| DOC-003 | 6 | Yes | 474 | Usable continuation-table text with layout/render support. | `rendered_pages/DOC-003-p6.png` | Not run — layout and render usable. |
| DOC-003 | 7 | Yes | 1,612 | Usable imputation-analysis table text; layout usable. | `rendered_pages/DOC-003-p7.png` | Not run — usable native/layout text. |
| DOC-003 | 8 | Yes | 1,326 | Usable race/ethnicity outcome table text; layout usable. | `rendered_pages/DOC-003-p8.png` | Not run — usable native/layout text. |
| DOC-003 | 9 | Yes | 1,046 | Usable continuation-table text; layout usable. | `rendered_pages/DOC-003-p9.png` | Not run — usable native/layout text. |
| DOC-003 | 10 | Yes | 493 | Usable continuation-table text with layout/render support. | `rendered_pages/DOC-003-p10.png` | Not run — layout and render usable. |
| DOC-003 | 11 | Yes | 577 | Usable figure/caption text with render support. | `rendered_pages/DOC-003-p11.png` | Not run — layout and render usable. |
| DOC-003 | 12 | Yes | 398 | Usable reference text; layout usable. | `rendered_pages/DOC-003-p12.png` | Not run — usable native/layout text. |

## Table and figure evidence locations

The exact table/figure evidence method for every listed display is fresh `pdftotext -layout` plus the named fresh PNG render. Text-only conversion does not preserve every visual cell boundary; the render is the retained evidence for visual alignment, spanning cells, footnotes, and plotted points. No Office sheets or structured-table sources are present.

| Source ID | Display / source page location | Exact fresh evidence assets | Limitation |
|---|---|---|---|
| DOC-001 | Tables 1–3, PDF pp. 3–6 (displayed tables and their narrative references) | `layout_text/DOC-001.txt`; `page_text/layout/DOC-001-p3.txt` through `DOC-001-p6.txt`; `rendered_pages/DOC-001-p3.png` through `DOC-001-p6.png` | Use rendered page for visual column alignment. |
| DOC-001 | Tables 3–5, PDF pp. 6–8 (including continuations/references) | `layout_text/DOC-001.txt`; `page_text/layout/DOC-001-p6.txt` through `DOC-001-p8.txt`; `rendered_pages/DOC-001-p6.png` through `DOC-001-p8.png` | Use rendered page for visual column alignment and footnotes. |
| DOC-002 | Protocol Figure 1, PDF p. 5 | `page_text/layout/DOC-002-p5.txt`; `rendered_pages/DOC-002-p5.png` | Diagram geometry is available only in the render. |
| DOC-002 | Protocol Tables 1–2, PDF pp. 8–9 | `page_text/layout/DOC-002-p8.txt`; `page_text/layout/DOC-002-p9.txt`; `rendered_pages/DOC-002-p8.png`; `rendered_pages/DOC-002-p9.png` | Use rendered page for visual column alignment. |
| DOC-002 | Protocol Figure 2, PDF p. 11 | `page_text/layout/DOC-002-p11.txt`; `rendered_pages/DOC-002-p11.png` | Diagram geometry is available only in the render. |
| DOC-003 | eTable 1, PDF p. 2 | `page_text/layout/DOC-003-p2.txt`; `rendered_pages/DOC-003-p2.png` | Use rendered page for original list/table layout. |
| DOC-003 | eTable 2, PDF pp. 3–4 | `page_text/layout/DOC-003-p3.txt`; `page_text/layout/DOC-003-p4.txt`; `rendered_pages/DOC-003-p3.png`; `rendered_pages/DOC-003-p4.png` | Continuation and column alignment require the renders. |
| DOC-003 | eTable 3, PDF pp. 5–6 | `page_text/layout/DOC-003-p5.txt`; `page_text/layout/DOC-003-p6.txt`; `rendered_pages/DOC-003-p5.png`; `rendered_pages/DOC-003-p6.png` | Continuation and column alignment require the renders. |
| DOC-003 | eTable 4, PDF p. 7 | `page_text/layout/DOC-003-p7.txt`; `rendered_pages/DOC-003-p7.png` | Use rendered page for visual column alignment. |
| DOC-003 | eTable 5, PDF pp. 8–10 | `page_text/layout/DOC-003-p8.txt` through `DOC-003-p10.txt`; `rendered_pages/DOC-003-p8.png` through `DOC-003-p10.png` | Continuation and footnote alignment require the renders. |
| DOC-003 | eFigure, PDF p. 11 | `page_text/layout/DOC-003-p11.txt`; `rendered_pages/DOC-003-p11.png` | Plot geometry and visual data labels require the render. |

## Completeness summary

- Direct sources processed: 3 PDF documents.
- Source units processed: 42 of 42 PDF pages.
- Fresh native-page text assets: 42; fresh layout-page text assets: 42; whole-document native and layout assets: 6.
- Fresh rendered-page assets: 42 at 200 dpi.
- OCR units: 0. There were no result-relevant pages with unusable native/layout text.
- Office/CSV assets: 0; no direct Office or CSV source was in the assigned direct-source set.
