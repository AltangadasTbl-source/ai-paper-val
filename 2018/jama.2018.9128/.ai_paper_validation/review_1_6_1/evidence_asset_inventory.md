# Reusable Evidence Asset Inventory

The only legacy audit area is `review_1_5_2/preprocessing`. Every file below it is inventoried and hashed in `reused_artifact_hashes_before.sha256`. No old candidate, checker, verifier, critic, screening, classification, or report material was read. Existing artifacts remain unchanged.

Fitness meanings: USABLE provides readable source-linked content; PARTIAL provides only a subset or a locator requiring another asset; STALE would disagree with current source identity/content; DUPLICATE would add no distinct representation; UNREADABLE would supply no recoverable content. No STALE, DUPLICATE, or UNREADABLE files were found. Native text byte-matches current direct extraction for all three PDFs. Native and layout representations are complementary, not duplicate file instances. Whole-document layout is byte-identical for DOC-002. DOC-001 and DOC-003 layout differences against current Poppler are whitespace and placement of rotated axis labels; text values and page partition remain usable.

The legacy generation engine/version was not retained in metadata. Native/layout content identifies Poppler-compatible extraction, PNG files are full 1530 × 1980 CPU PDF page renderings, and OCR is prior OCR with engine unrecorded. Current comparison uses direct `pdftotext`; PNG integrity uses `file`; hashes use direct `sha256sum`. This distinction avoids claiming an unrecorded legacy engine. Prior PDF metadata reports are useful identity locators but are partial scientific evidence. OCR is partial and may mistranscribe mathematical glyphs; reusable images and exact supplied sources govern interpretation.

| Asset path | Kind | Source ID | Exact source units | Fitness | Engine / fitness basis |
|---|---|---|---|---|---|
| .ai_paper_validation/review_1_5_2/preprocessing/jama_barkin_2018_oi_180075.pdfinfo.txt | PDF_METADATA | DOC-001 | PDF pages 1–11 | PARTIAL | Prior pdfinfo metadata; current direct pdfinfo verifies page count |
| .ai_paper_validation/review_1_5_2/preprocessing/joi180075supp1_prod.pdfinfo.txt | PDF_METADATA | DOC-002 | PDF pages 1–113 | PARTIAL | Prior pdfinfo metadata; current direct pdfinfo verifies page count |
| .ai_paper_validation/review_1_5_2/preprocessing/joi180075supp2_prod.pdfinfo.txt | PDF_METADATA | DOC-003 | PDF pages 1–8 | PARTIAL | Prior pdfinfo metadata; current direct pdfinfo verifies page count |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/jama_barkin_2018_oi_180075.txt | LAYOUT_TEXT | DOC-001 | PDF pages 1–11 | USABLE | Legacy Poppler-compatible; current direct pdftotext layout content match |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi180075supp1_prod.txt | LAYOUT_TEXT | DOC-002 | PDF pages 1–113 | USABLE | Legacy Poppler-compatible; current direct pdftotext layout content match |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi180075supp2_prod.txt | LAYOUT_TEXT | DOC-003 | PDF pages 1–8 | USABLE | Legacy Poppler-compatible; current direct pdftotext layout content match |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/jama_barkin_2018_oi_180075.txt | NATIVE_TEXT | DOC-001 | PDF pages 1–11 | USABLE | Legacy Poppler-compatible; current direct pdftotext byte-match |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180075supp1_prod.txt | NATIVE_TEXT | DOC-002 | PDF pages 1–113 | USABLE | Legacy Poppler-compatible; current direct pdftotext byte-match |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180075supp2_prod.txt | NATIVE_TEXT | DOC-003 | PDF pages 1–8 | USABLE | Legacy Poppler-compatible; current direct pdftotext byte-match |
| .ai_paper_validation/review_1_5_2/preprocessing/ocr_text/DOC-002-p039.txt | OCR_TEXT | DOC-002 | PDF page 39 | PARTIAL | Prior OCR, engine unrecorded; readable locator with glyph limitations, image available |
| .ai_paper_validation/review_1_5_2/preprocessing/ocr_text/DOC-002-p108.txt | OCR_TEXT | DOC-002 | PDF page 108 | PARTIAL | Prior OCR, engine unrecorded; readable locator with glyph limitations, image available |
| .ai_paper_validation/review_1_5_2/preprocessing/ocr_text/DOC-002-p109.txt | OCR_TEXT | DOC-002 | PDF page 109 | PARTIAL | Prior OCR, engine unrecorded; readable locator with glyph limitations, image available |
| .ai_paper_validation/review_1_5_2/preprocessing/ocr_text/DOC-002-p111.txt | OCR_TEXT | DOC-002 | PDF page 111 | PARTIAL | Prior OCR, engine unrecorded; readable locator with glyph limitations, image available |
| .ai_paper_validation/review_1_5_2/preprocessing/ocr_text/DOC-003-p005.txt | OCR_TEXT | DOC-003 | PDF page 5 | PARTIAL | Prior OCR, engine unrecorded; readable locator with glyph limitations, image available |
| .ai_paper_validation/review_1_5_2/preprocessing/ocr_text/DOC-003-p006.txt | OCR_TEXT | DOC-003 | PDF page 6 | PARTIAL | Prior OCR, engine unrecorded; readable locator with glyph limitations, image available |
| .ai_paper_validation/review_1_5_2/preprocessing/ocr_text/DOC-003-p007.txt | OCR_TEXT | DOC-003 | PDF page 7 | PARTIAL | Prior OCR, engine unrecorded; readable locator with glyph limitations, image available |
| .ai_paper_validation/review_1_5_2/preprocessing/ocr_text/DOC-003-p008.txt | OCR_TEXT | DOC-003 | PDF page 8 | PARTIAL | Prior OCR, engine unrecorded; readable locator with glyph limitations, image available |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p001.png | RENDERED_PAGE | DOC-001 | PDF page 1 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p002.png | RENDERED_PAGE | DOC-001 | PDF page 2 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p003.png | RENDERED_PAGE | DOC-001 | PDF page 3 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p004.png | RENDERED_PAGE | DOC-001 | PDF page 4 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p005.png | RENDERED_PAGE | DOC-001 | PDF page 5 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p006.png | RENDERED_PAGE | DOC-001 | PDF page 6 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p007.png | RENDERED_PAGE | DOC-001 | PDF page 7 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p008.png | RENDERED_PAGE | DOC-001 | PDF page 8 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p009.png | RENDERED_PAGE | DOC-001 | PDF page 9 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p010.png | RENDERED_PAGE | DOC-001 | PDF page 10 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p011.png | RENDERED_PAGE | DOC-001 | PDF page 11 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p014.png | RENDERED_PAGE | DOC-002 | PDF page 14 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p018.png | RENDERED_PAGE | DOC-002 | PDF page 18 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p019.png | RENDERED_PAGE | DOC-002 | PDF page 19 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p020.png | RENDERED_PAGE | DOC-002 | PDF page 20 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p021.png | RENDERED_PAGE | DOC-002 | PDF page 21 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p037.png | RENDERED_PAGE | DOC-002 | PDF page 37 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p038.png | RENDERED_PAGE | DOC-002 | PDF page 38 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p039.png | RENDERED_PAGE | DOC-002 | PDF page 39 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p040.png | RENDERED_PAGE | DOC-002 | PDF page 40 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p041.png | RENDERED_PAGE | DOC-002 | PDF page 41 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p042.png | RENDERED_PAGE | DOC-002 | PDF page 42 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p043.png | RENDERED_PAGE | DOC-002 | PDF page 43 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p044.png | RENDERED_PAGE | DOC-002 | PDF page 44 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p045.png | RENDERED_PAGE | DOC-002 | PDF page 45 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p046.png | RENDERED_PAGE | DOC-002 | PDF page 46 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p047.png | RENDERED_PAGE | DOC-002 | PDF page 47 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p069.png | RENDERED_PAGE | DOC-002 | PDF page 69 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p070.png | RENDERED_PAGE | DOC-002 | PDF page 70 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p071.png | RENDERED_PAGE | DOC-002 | PDF page 71 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p092.png | RENDERED_PAGE | DOC-002 | PDF page 92 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p093.png | RENDERED_PAGE | DOC-002 | PDF page 93 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p094.png | RENDERED_PAGE | DOC-002 | PDF page 94 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p095.png | RENDERED_PAGE | DOC-002 | PDF page 95 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p096.png | RENDERED_PAGE | DOC-002 | PDF page 96 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p097.png | RENDERED_PAGE | DOC-002 | PDF page 97 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p098.png | RENDERED_PAGE | DOC-002 | PDF page 98 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p099.png | RENDERED_PAGE | DOC-002 | PDF page 99 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p100.png | RENDERED_PAGE | DOC-002 | PDF page 100 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p101.png | RENDERED_PAGE | DOC-002 | PDF page 101 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p102.png | RENDERED_PAGE | DOC-002 | PDF page 102 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p108.png | RENDERED_PAGE | DOC-002 | PDF page 108 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p109.png | RENDERED_PAGE | DOC-002 | PDF page 109 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p110.png | RENDERED_PAGE | DOC-002 | PDF page 110 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p111.png | RENDERED_PAGE | DOC-002 | PDF page 111 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p112.png | RENDERED_PAGE | DOC-002 | PDF page 112 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p113.png | RENDERED_PAGE | DOC-002 | PDF page 113 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p002.png | RENDERED_PAGE | DOC-003 | PDF page 2 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p003.png | RENDERED_PAGE | DOC-003 | PDF page 3 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p004.png | RENDERED_PAGE | DOC-003 | PDF page 4 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p005.png | RENDERED_PAGE | DOC-003 | PDF page 5 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p006.png | RENDERED_PAGE | DOC-003 | PDF page 6 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p007.png | RENDERED_PAGE | DOC-003 | PDF page 7 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p008.png | RENDERED_PAGE | DOC-003 | PDF page 8 | USABLE | Prior CPU PDF renderer, engine unrecorded; valid full-page PNG |

## Exact coverage and gaps

- DOC-001 native/layout: pages 1–11. Rendered pages: 1–11. No OCR needed for text. Reusable union: 11 unique pages; fresh-required: none.
- DOC-002 native/layout: pages 1–113. Rendered pages: 14, 18, 19, 20, 21, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 69, 70, 71, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 108, 109, 110, 111, 112, 113. OCR: pages 39, 108, 109, 111. Native-readable pages without an existing PNG: 1–13, 15–17, 22–36, 48–68, 72–91, 103–107. Reusable union: 113 unique pages; fresh-required: none. Figure/equation graphics require rendered inspection during mapping even when surrounding native text is readable.
- DOC-003 native/layout: pages 1–8. Rendered pages: 2–8. OCR: 5–8. Native page 6 has only copyright text; its rendered page confirms no omitted graphic or table. Existing PNG absent on page 1, a fully native-readable cover/list. Reusable union: 8 unique pages; fresh-required: none.

Asset totals: 71 files = 3 native text + 3 layout text + 8 OCR text + 54 rendered pages + 3 PDF metadata. No table/workbook extraction, page manifest, document record, source-location map, or Office derivative exists elsewhere under the audit area. This inventory supplies the fresh explicit source-location map. Page separation is ASCII form feed, with 11/113/8 records respectively. Each page has native text; sparse pages were checked against reusable renders. Text/assets are locators and transcription aids, and every final candidate still requires exact-source confirmation.

Current commands: `pdfinfo SOURCE.pdf`; `pdftotext SOURCE.pdf -` compared bytewise with legacy native text; `pdftotext -layout SOURCE.pdf -` compared with legacy layout; `file` for every rendered PNG; `sha256sum` for each source and reusable file. These current comparisons produced no retained derivatives and did not modify sources or reusable assets. CPU only; no fallback helper used. Missing tesseract and Office conversion are irrelevant to initial reuse coverage; direct rendering permits later visual confirmation.

## Mapping-stage coverage correction and new derivatives

Full mapping found PARTIAL native/layout coverage on DOC-002 pages13,54,63,67 despite readable surrounding text. No prior render covered these pages. Their embedded diagram/aim/endpoint content required fresh direct rendering; source_coverage.md now assigns109 reusable and4 fresh-required PLAN pages, all113 mapped. These four direct-source gaps are closed. The initial inventory's fresh0 assessment is superseded by this detailed content inspection.

| New derivative path | Source unit | Engine | Purpose | Coverage |
|---|---|---|---|---|
| preprocessing/support001-p013.png | DOC-002 PDF p13 | direct CPU Poppler pdftoppm25.03.0 | Embedded design diagram omitted by native/layout | Fresh-required unit mapped |
| preprocessing/support2-p054.png | DOC-002 PDF p54 | direct CPU Poppler pdftoppm25.03.0 | Ancillary aim labels with font encoding gaps | Fresh-required unit mapped |
| preprocessing/support2-p063.png | DOC-002 PDF p63 | direct CPU Poppler pdftoppm25.03.0 | Embedded revised design diagram omitted by text | Fresh-required unit mapped |
| preprocessing/support003-p067.png | DOC-002 PDF p67 | direct CPU Poppler pdftoppm25.03.0 | Amended secondary endpoint text with substituted glyphs | Fresh-required unit mapped |
| preprocessing/support003-p092.png | DOC-002 PDF p92 | direct CPU Poppler pdftoppm25.03.0 | Confirm model equation glyphs | Reusable-backed unit confirmed |
| preprocessing/main-direct-p006.png | DOC-001 PDF p6 | direct CPU Poppler pdftoppm25.03.0 | Confirm table continuation and narrative | Reusable-backed unit confirmed |

Commands were targeted `pdftoppm -f N -l N -singlefile -png SOURCE OUTPUT_PREFIX`, with scale options recorded in mapper artifacts. No new OCR or fallback environment used. Each derivative has a unique output path; source/reused files remain unchanged.

Cross-source checker fresh confirmation derivatives (existing reusable units remain reusable): preprocessing/xs-main-p002.png (DOC-001p2), preprocessing/xs-main-p003.png (DOC-001p3), preprocessing/xs-plan-p064.png (DOC-002p64). Engine direct CPU Poppler pdftoppm25.03.0. Targeted one-page render commands and direct values recorded in checkers/cross_source_consistency.md. These corroborate transcription; no new source-coverage gap.

## Statistical pass 1 direct confirmation derivatives

All are direct CPU Poppler25.03.0 source confirmations on reusable-backed units; commands are recorded in checkers/statistical_pass_1.md. They do not change source partition counts.

| Derivative path | Exact source scope | Engine |
|---|---|---|
| preprocessing/st1-supp2-p002-004.txt | DOC-003 PDF pp2-4 | pdftotext -layout |
| preprocessing/st1-plan-p110-113.txt | DOC-002 PDF pp110-113 | pdftotext -layout |
| preprocessing/st1-main-p002-003.txt | DOC-001 PDF pp2-3 | pdftotext -layout |
| preprocessing/st1-plan-p064-065.txt | DOC-002 PDF pp64-65 | pdftotext -layout |
| preprocessing/st1-plan-p106-109.txt | DOC-002 PDF pp106-109 | pdftotext -layout |
| preprocessing/st1-plan-p064.png | DOC-002 PDF p64 | pdftoppm direct one-page render |
| preprocessing/st1-main-p002.png | DOC-001 PDF p2 | pdftoppm direct one-page render |
| preprocessing/st1-main-p003.png | DOC-001 PDF p3 | pdftoppm direct one-page render |

Inclusion screen direct CPU Poppler25.03.0 layout confirmation derivatives: preprocessing/screen-main-p002-003.txt (DOC-001pp2-3); preprocessing/screen-plan-p063-065.txt (DOC-002pp63-65); preprocessing/screen-plan-p106-107.txt (DOC-002pp106-107); preprocessing/screen-plan-p113.txt (DOC-002p113); preprocessing/screen-plan-p013-015.txt (DOC-002pp13-15). Commands and image inspection provenance recorded in screening/inclusion_screen.md. These source confirmations do not change final source partition or reused hashes.

## Exact-source mechanical recheck derivatives

Six direct CPU Poppler25.03.0 renders support context confirmation: preprocessing/recheck-plan-p014.png (DOC-002p14), recheck-plan-p015.png (p15), recheck-plan-p065.png (p65), recheck-plan-p106.png (p106), recheck-plan-p107.png (p107), recheck-plan-p113.png (p113). All lie under preprocessing/; exact commands and existing source render inspections are recorded in verification/evidence_recheck.md. Sixteen assigned candidate locations spanning11unique PDF pages were found and read. No coverage gap remains; new renders confirm already reusable-backed units.

Statistical pass2 direct CPU Poppler25.03.0 `pdftotext -layout` derivatives: preprocessing/st2-main.txt (DOC-001pp1-11), preprocessing/st2-plan.txt (DOC-002pp1-113), preprocessing/st2-report-supp.txt (DOC-003pp1-8). Exact commands and source-integrity checks recorded in checkers/statistical_pass_2.md. These are current-source confirmations, not reused artifacts or fresh-coverage gaps. All116Srelationships independently complete in both passes.
