# Fresh Evidence-Asset Inventory

All paths below are relative to `.ai_paper_validation/review_1_5_2/`. Each evidence derivative was freshly generated from its exact direct source with installed local Acrobat COM; no prior audit derivative was reused.

| Asset ID | Source ID | Scope | Method | Output path | Completeness and usability |
|---|---|---|---|---|---|
| A-001 | DOC-001 | pp. 1-10 | Acrobat COM `getPageNumWords`/`getPageNthWord`, UTF-8 page-delimited native text | preprocessing/native_text/DOC-001.txt | COMPLETE: 10 pages, 9526 words; every page has 661-1473 words and is readable for result mapping. |
| A-002 | DOC-001 | pp. 1-10 | Acrobat COM `getPageNthWordQuads`, token plus coordinates per TSV row | preprocessing/layout_text/DOC-001.tsv | COMPLETE: 9526 token rows plus header; page, word index, X/Y, and token support column reconstruction. |
| A-003 | DOC-002 | pp. 1-25 | Acrobat COM `getPageNumWords`/`getPageNthWord`, UTF-8 page-delimited native text | preprocessing/native_text/DOC-002.txt | COMPLETE: 25 pages, 7283 words. All pages contain text; pp. 1 and 5 have 93 and 23 words. P. 5 is a planned-trial flow diagram, not a reported result display. |
| A-004 | DOC-002 | pp. 1-25 | Acrobat COM `getPageNthWordQuads`, token plus coordinates per TSV row | preprocessing/layout_text/DOC-002.tsv | COMPLETE: 7283 token rows plus header. Some duplicated adjacent native token runs are an extraction artifact; resolve with coordinate layout and exact source location, not as a second printed result. |
| A-005 | DOC-003 | pp. 1-9 | Acrobat COM `getPageNumWords`/`getPageNthWord`, UTF-8 page-delimited native text | preprocessing/native_text/DOC-003.txt | COMPLETE: 9 pages, 3879 words. All pages are text-readable; low-text pp. 4 and 7 continue an eTable/footnotes and have coordinate layout. |
| A-006 | DOC-003 | pp. 1-9 | Acrobat COM `getPageNthWordQuads`, token plus coordinates per TSV row | preprocessing/layout_text/DOC-003.tsv | COMPLETE: 3879 token rows plus header; page, word index, X/Y, and token support table reconstruction. |
| A-007 | DOC-001 | pp. 3, 4, 6, 7, 8 | Fresh direct full-page PDF rasters for exact-source visual confirmation | preprocessing/rendered_pages/DOC-001-page-003-full.png; preprocessing/rendered_pages/DOC-001-page-004-full.png; preprocessing/rendered_pages/DOC-001-page-006-full.png; preprocessing/rendered_pages/DOC-001-page-007-full.png; preprocessing/rendered_pages/DOC-001-page-008-full.png | COMPLETE: five 612×792 full-page raster assets used to visually confirm selected main-article evidence. |
| A-008 | DOC-002 | pp. 13, 14, 15, 18, 19 | Fresh direct full-page PDF rasters for exact-source visual confirmation | preprocessing/rendered_pages/DOC-002-page-013-full.png; preprocessing/rendered_pages/DOC-002-page-014-full.png; preprocessing/rendered_pages/DOC-002-page-015-full.png; preprocessing/rendered_pages/DOC-002-page-018-full.png; preprocessing/rendered_pages/DOC-002-page-019-full.png | COMPLETE: five 595×842 full-page raster assets used to visually confirm selected support-document evidence. |
| A-009 | DOC-003 | pp. 2, 3, 8 | Fresh direct full-page PDF rasters for exact-source visual confirmation | preprocessing/rendered_pages/DOC-003-page-002-full.png; preprocessing/rendered_pages/DOC-003-page-003-full.png; preprocessing/rendered_pages/DOC-003-page-008-full.png | COMPLETE: two 595×842 portrait and one 842×595 landscape full-page raster assets used to visually confirm selected eAppendix/eTable evidence. |

## Extraction controls and page accounting

`preprocessing/acrobat_extract.vbs` opens each exact PDF in local Acrobat COM, obtains page count, and enumerates every page word. `preprocessing/acrobat_layout.vbs` enumerates the same page-word universe and writes word quadrilateral coordinates. Native files use `=== PDF PAGE N | NATIVE WORDS W ===`; each layout TSV has the matching token universe.

| Source ID | Page coverage | Native words | Layout tokens | Result-relevant visual decision |
|---|---|---:|---:|---|
| DOC-001 | pp. 1-10 | 9526 | 9526 | Native/layout text is usable throughout. Full-page visual confirmation also exists for pp. 3, 4, 6, 7, 8; no OCR required. |
| DOC-002 | pp. 1-25 | 7283 | 7283 | Native/layout text is usable throughout. Full-page visual confirmation exists for pp. 13, 14, 15, 18, 19; no OCR required. P. 5 is a planned flow diagram with no reported result content. |
| DOC-003 | pp. 1-9 | 3879 | 3879 | Native/layout text is usable throughout. Full-page visual confirmation exists for pp. 2, 3, 8; no OCR required. |

## Non-evidence and unavailable tools

- The 13 files named `*-full.png` are fresh exact-source visual-confirmation evidence. `capture_window.ps1`, `rendered_pages/*test.png`, and the failed `DOC-003-page-008.png`/`DOC-003-page-008b.png` trials are non-evidence and were not inspected for scientific mapping.
- Linux `pdfinfo`, `pdftotext`, `pdftoppm`, `pdftocairo`, and `tesseract` remain unavailable. Acrobat COM supplied complete direct text/layout extraction; no replacement installation, web access, legacy output, or GPU was used.
- No OCR was performed because no result-relevant page remained text-unusable after this fresh extraction.
