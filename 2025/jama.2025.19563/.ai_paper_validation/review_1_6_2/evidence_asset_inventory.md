# Reusable evidence-asset inventory

Every retained raw native/layout/OCR text, rendered page, document record, package source-location manifest, and PDF page manifest was inventoried. Prior scientific extraction narratives were excluded to avoid inherited interpretations. No old candidate, checker, screening, classification, verifier, critic, quality, or report content was read. All inventoried evidence assets are preserved and hashed in reused_artifact_hashes_before.sha256. Hashing does not establish historical source identity independently; source filename/page count and legible headings establish the locator identity, and exact source confirmation remains mandatory at recheck.

## Coverage and fitness by group

| Asset group | Exact source locations | Fitness | Engine | Coverage consequence |
|---|---|---|---|---|
| DOC-001 document_outputs normalized native | DOC-001 pp. 1-11 | USABLE | pypdf historical extraction; version not recorded | Eleven text-backed units; 58,292 unique-page Unicode characters |
| DOC-001 document_outputs PNG and OCR | DOC-001 pp. 5-9 | USABLE images; OCR individually assessed below | PyMuPDF render at 200 dpi; tesseract when available, historical versions not recorded | Visual aids for flow/table/figures |
| DOC-002 review_1_5_1 full page PNGs | DOC-002 pp. 1-90 | PARTIAL | Historical rendering engine not recorded; samples 1700x2200, 2550x3300, 2125x2750 | Eighty-six usable image-backed units and four direct-source replacement pages; 3 mapping shards of 30 pages |
| DOC-002 review_1_5_1 aggregate native/layout | DOC-002 pp. 1-30, 31-60, 61-90 | UNREADABLE | Historical native/layout extractor not recorded | Glyph-encoded; not content evidence. 595,338 bytes including both representations |
| DOC-002 review_1_5_1 sparse OCR | DOC-002 p. 1; empty files pp. 2-3, 31-39, 61-62 | PARTIAL | Historical OCR engine not recorded | P. 1 title locator readable; remaining OCR empty. Fresh OCR/transcription required for efficient full mapping |
| DOC-003 review_1_5_1 native/layout | DOC-003 pp. 1-33, 36-37, 67-69 | USABLE | Historical native/layout extractor not recorded | Completes the early and terminal pages omitted by prior document_outputs scope |
| DOC-003 document_outputs native/OCR/PNG | DOC-003 pp. 34-35, 38-66 | USABLE native/PNG; OCR individually assessed below | pypdf text; PyMuPDF 200 dpi render; historical OCR engine/version not fully recorded | Thirty-one results display pages |
| DOC-003 review_1_5_1 terminal PNG | DOC-003 pp. 67-68 | USABLE | Historical renderer not recorded | Reference-page visual companion; p. 69 native text usable |
| Package/document/page manifests | DOC-001 pp. 1-11; DOC-002 source identity; DOC-003 pp. 34-35, 38-66 | PARTIAL | Historical manifest generation | Exact locator metadata retained; previous restricted scientific scope is not inherited |

After decoder checks, 166 source pages have usable reusable text or a full-page image; four DOC-002 pages require fresh direct-source renders. No STALE asset was established; missing historical source hashes are a provenance limitation, not affirmative evidence of staleness. Low-resolution/alternate renders and aggregate copies are DUPLICATE locator aids. Empty OCR and unavailable-engine placeholders are UNREADABLE and never treated as coverage. Table/workbook/cell extraction and Office/CSV source-location maps were not present. Old scientific extraction narrative files are deliberately excluded from reuse.

## Recommended canonical paths

- Main: `.ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-NNN.txt` for PDF pp. 1-11, with `.ai_paper_validation/document_outputs/DOC-001-main-article/page_images/page-NNN.png` for pp. 5-9.
- Plan: `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-NN.png` (01-30); `p031-p060/page-NN.png` (31-60); `p061-p090/page-NN.png` (61-90). Every page exists and has nonzero PNG content.
- Results: `.ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/pNN.txt` for pp. 1-30; `p031-p060/page-NN-native.txt` for pp. 31-33, 36-37; `.ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-NNN.txt` for pp. 34-35, 38-66; `review_1_5_1/preprocessing/DOC-003/p061-p069/page-NNN-native.txt` for pp. 67-69.

## Individual asset registry

Paths are package-relative. Byte lengths give reproducible asset burden; page maps are exact. Aggregate files contain duplicate page text and do not increase unique coverage. Engine details above apply to each group; unknown historical engine/version is explicitly retained as a limitation.

| Artifact | Source ID | Exact units | Fitness | Bytes |
|---|---|---|---|---:|
| .ai_paper_validation/document_outputs/DOC-001-main-article/document_record.md | DOC-001 | Document identity; prior selective page scope | PARTIAL | 1097 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-001.txt | DOC-001 | PDF p. 1 | USABLE | 3616 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-002.txt | DOC-001 | PDF p. 2 | USABLE | 5852 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-003.txt | DOC-001 | PDF p. 3 | USABLE | 6115 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-004.txt | DOC-001 | PDF p. 4 | USABLE | 6076 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-005.txt | DOC-001 | PDF p. 5 | USABLE | 3935 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-006.txt | DOC-001 | PDF p. 6 | USABLE | 5280 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-007.txt | DOC-001 | PDF p. 7 | USABLE | 5862 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-008.txt | DOC-001 | PDF p. 8 | USABLE | 1881 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-009.txt | DOC-001 | PDF p. 9 | USABLE | 5855 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-010.txt | DOC-001 | PDF p. 10 | USABLE | 8584 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-011.txt | DOC-001 | PDF p. 11 | USABLE | 5420 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native_all_selected_pages.txt | DOC-001 | PDF pp. 1-11 | DUPLICATE | 59413 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/ocr/page-005.txt | DOC-001 | PDF p. 5 | USABLE | 4005 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/ocr/page-006.txt | DOC-001 | PDF p. 6 | USABLE | 5492 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/ocr/page-007.txt | DOC-001 | PDF p. 7 | USABLE | 6342 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/ocr/page-008.txt | DOC-001 | PDF p. 8 | USABLE | 1944 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/ocr/page-009.txt | DOC-001 | PDF p. 9 | USABLE | 6332 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/ocr_all_selected_visual_pages.txt | DOC-001 | PDF pp. 5-9 | DUPLICATE | 24540 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/page_images/page-005.png | DOC-001 | PDF p. 5 | USABLE | 447660 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/page_images/page-006.png | DOC-001 | PDF p. 6 | USABLE | 622015 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/page_images/page-007.png | DOC-001 | PDF p. 7 | USABLE | 604028 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/page_images/page-008.png | DOC-001 | PDF p. 8 | USABLE | 248470 |
| .ai_paper_validation/document_outputs/DOC-001-main-article/page_images/page-009.png | DOC-001 | PDF p. 9 | USABLE | 607969 |
| .ai_paper_validation/document_outputs/DOC-002-protocol/document_record.md | DOC-002 | Document identity; prior selective page scope | PARTIAL | 1318 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/document_record.md | DOC-003 | Document identity; prior selective page scope | PARTIAL | 1486 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-034.txt | DOC-003 | PDF p. 34 | USABLE | 1110 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-035.txt | DOC-003 | PDF p. 35 | USABLE | 1031 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-038.txt | DOC-003 | PDF p. 38 | USABLE | 905 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-039.txt | DOC-003 | PDF p. 39 | USABLE | 1708 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-040.txt | DOC-003 | PDF p. 40 | USABLE | 1738 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-041.txt | DOC-003 | PDF p. 41 | USABLE | 1462 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-042.txt | DOC-003 | PDF p. 42 | USABLE | 1983 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-043.txt | DOC-003 | PDF p. 43 | USABLE | 1995 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-044.txt | DOC-003 | PDF p. 44 | USABLE | 1986 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-045.txt | DOC-003 | PDF p. 45 | USABLE | 2044 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-046.txt | DOC-003 | PDF p. 46 | USABLE | 2028 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-047.txt | DOC-003 | PDF p. 47 | USABLE | 1990 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-048.txt | DOC-003 | PDF p. 48 | USABLE | 621 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-049.txt | DOC-003 | PDF p. 49 | USABLE | 1596 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-050.txt | DOC-003 | PDF p. 50 | USABLE | 927 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-051.txt | DOC-003 | PDF p. 51 | USABLE | 1174 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-052.txt | DOC-003 | PDF p. 52 | USABLE | 1087 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-053.txt | DOC-003 | PDF p. 53 | USABLE | 1965 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-054.txt | DOC-003 | PDF p. 54 | USABLE | 2169 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-055.txt | DOC-003 | PDF p. 55 | USABLE | 853 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-056.txt | DOC-003 | PDF p. 56 | USABLE | 894 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-057.txt | DOC-003 | PDF p. 57 | USABLE | 967 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-058.txt | DOC-003 | PDF p. 58 | USABLE | 1302 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-059.txt | DOC-003 | PDF p. 59 | USABLE | 568 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-060.txt | DOC-003 | PDF p. 60 | USABLE | 628 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-061.txt | DOC-003 | PDF p. 61 | USABLE | 1169 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-062.txt | DOC-003 | PDF p. 62 | USABLE | 1126 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-063.txt | DOC-003 | PDF p. 63 | USABLE | 1278 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-064.txt | DOC-003 | PDF p. 64 | USABLE | 406 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-065.txt | DOC-003 | PDF p. 65 | USABLE | 402 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-066.txt | DOC-003 | PDF p. 66 | USABLE | 1070 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native_all_selected_pages.txt | DOC-003 | PDF pp. 34-35, 38-66 | DUPLICATE | 42445 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-034.txt | DOC-003 | PDF p. 34 | USABLE | 1651 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-035.txt | DOC-003 | PDF p. 35 | USABLE | 2016 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-038.txt | DOC-003 | PDF p. 38 | USABLE | 904 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-039.txt | DOC-003 | PDF p. 39 | USABLE | 397 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-040.txt | DOC-003 | PDF p. 40 | USABLE | 1731 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-041.txt | DOC-003 | PDF p. 41 | USABLE | 666 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-042.txt | DOC-003 | PDF p. 42 | USABLE | 424 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-043.txt | DOC-003 | PDF p. 43 | USABLE | 2001 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-044.txt | DOC-003 | PDF p. 44 | USABLE | 359 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-045.txt | DOC-003 | PDF p. 45 | USABLE | 1917 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-046.txt | DOC-003 | PDF p. 46 | USABLE | 460 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-047.txt | DOC-003 | PDF p. 47 | USABLE | 1981 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-048.txt | DOC-003 | PDF p. 48 | USABLE | 604 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-049.txt | DOC-003 | PDF p. 49 | USABLE | 1153 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-050.txt | DOC-003 | PDF p. 50 | USABLE | 893 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-051.txt | DOC-003 | PDF p. 51 | USABLE | 974 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-052.txt | DOC-003 | PDF p. 52 | USABLE | 332 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-053.txt | DOC-003 | PDF p. 53 | USABLE | 577 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-054.txt | DOC-003 | PDF p. 54 | USABLE | 2166 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-055.txt | DOC-003 | PDF p. 55 | USABLE | 666 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-056.txt | DOC-003 | PDF p. 56 | USABLE | 709 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-057.txt | DOC-003 | PDF p. 57 | USABLE | 434 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-058.txt | DOC-003 | PDF p. 58 | USABLE | 1303 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-059.txt | DOC-003 | PDF p. 59 | USABLE | 569 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-060.txt | DOC-003 | PDF p. 60 | USABLE | 617 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-061.txt | DOC-003 | PDF p. 61 | USABLE | 1158 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-062.txt | DOC-003 | PDF p. 62 | USABLE | 1119 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-063.txt | DOC-003 | PDF p. 63 | USABLE | 490 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-064.txt | DOC-003 | PDF p. 64 | USABLE | 207 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-065.txt | DOC-003 | PDF p. 65 | USABLE | 354 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-066.txt | DOC-003 | PDF p. 66 | USABLE | 941 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr_all_selected_visual_pages.txt | DOC-003 | PDF pp. 34-35, 38-66 | DUPLICATE | 32036 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-034.png | DOC-003 | PDF p. 34 | USABLE | 274866 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-035.png | DOC-003 | PDF p. 35 | USABLE | 402198 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-038.png | DOC-003 | PDF p. 38 | USABLE | 193056 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-039.png | DOC-003 | PDF p. 39 | USABLE | 374444 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-040.png | DOC-003 | PDF p. 40 | USABLE | 265995 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-041.png | DOC-003 | PDF p. 41 | USABLE | 256084 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-042.png | DOC-003 | PDF p. 42 | USABLE | 414382 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-043.png | DOC-003 | PDF p. 43 | USABLE | 294549 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-044.png | DOC-003 | PDF p. 44 | USABLE | 396851 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-045.png | DOC-003 | PDF p. 45 | USABLE | 307563 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-046.png | DOC-003 | PDF p. 46 | USABLE | 414078 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-047.png | DOC-003 | PDF p. 47 | USABLE | 299604 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-048.png | DOC-003 | PDF p. 48 | USABLE | 116446 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-049.png | DOC-003 | PDF p. 49 | USABLE | 274440 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-050.png | DOC-003 | PDF p. 50 | USABLE | 178708 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-051.png | DOC-003 | PDF p. 51 | USABLE | 204582 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-052.png | DOC-003 | PDF p. 52 | USABLE | 225884 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-053.png | DOC-003 | PDF p. 53 | USABLE | 387204 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-054.png | DOC-003 | PDF p. 54 | USABLE | 325446 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-055.png | DOC-003 | PDF p. 55 | USABLE | 162464 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-056.png | DOC-003 | PDF p. 56 | USABLE | 192230 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-057.png | DOC-003 | PDF p. 57 | USABLE | 152072 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-058.png | DOC-003 | PDF p. 58 | USABLE | 212389 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-059.png | DOC-003 | PDF p. 59 | USABLE | 122214 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-060.png | DOC-003 | PDF p. 60 | USABLE | 124074 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-061.png | DOC-003 | PDF p. 61 | USABLE | 212985 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-062.png | DOC-003 | PDF p. 62 | USABLE | 210205 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-063.png | DOC-003 | PDF p. 63 | USABLE | 269207 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-064.png | DOC-003 | PDF p. 64 | USABLE | 90733 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-065.png | DOC-003 | PDF p. 65 | USABLE | 85119 |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-066.png | DOC-003 | PDF p. 66 | USABLE | 222019 |
| .ai_paper_validation/package_manifest.json | MULTIPLE | Source identity/page locator metadata | PARTIAL | 1053 |
| .ai_paper_validation/package_manifest.md | MULTIPLE | Source identity/page locator metadata | PARTIAL | 2369 |
| .ai_paper_validation/pdf_preprocessing_manifest.json | MULTIPLE | Source identity/page locator metadata | PARTIAL | 42378 |
| .ai_paper_validation/pdf_preprocessing_manifest.md | MULTIPLE | Source identity/page locator metadata | PARTIAL | 1219 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/layout.txt | DOC-002 | PDF pp. 1-30 | UNREADABLE | 130314 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/low-01.png | DOC-002 | PDF p. 1 | DUPLICATE | 49030 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/lowocr-01.txt | DOC-002 | PDF p. 1 | USABLE | 366 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/lowocr-a.txt | DOC-002 | PDF p. 1 (empty trial OCR) | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/lowpage-12.png | DOC-002 | PDF p. 12 | DUPLICATE | 172796 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/lowpage-13.png | DOC-002 | PDF p. 13 | DUPLICATE | 127906 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/lowpage-14.png | DOC-002 | PDF p. 14 | DUPLICATE | 145017 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/lowpage-15.png | DOC-002 | PDF p. 15 | DUPLICATE | 128565 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/native.txt | DOC-002 | PDF pp. 1-30 | UNREADABLE | 111011 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/ocr-01.txt | DOC-002 | PDF p. 1 | USABLE | 367 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-01.png | DOC-002 | PDF p. 1 | USABLE | 91780 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-01.txt | DOC-002 | PDF p. 1 | USABLE | 367 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-02.png | DOC-002 | PDF p. 2 | USABLE | 288124 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-02.txt | DOC-002 | PDF p. 2 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-03.png | DOC-002 | PDF p. 3 | USABLE | 338746 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-03.txt | DOC-002 | PDF p. 3 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-04.png | DOC-002 | PDF p. 4 | USABLE | 192657 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-05.png | DOC-002 | PDF p. 5 | USABLE | 207022 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-06.png | DOC-002 | PDF p. 6 | USABLE | 274190 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-07.png | DOC-002 | PDF p. 7 | USABLE | 214991 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-08.png | DOC-002 | PDF p. 8 | USABLE | 179900 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-09.png | DOC-002 | PDF p. 9 | USABLE | 221038 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-10.png | DOC-002 | PDF p. 10 | USABLE | 253964 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-11.png | DOC-002 | PDF p. 11 | USABLE | 482585 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-12.png | DOC-002 | PDF p. 12 | USABLE | 569408 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-13.png | DOC-002 | PDF p. 13 | USABLE | 408056 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-14.png | DOC-002 | PDF p. 14 | USABLE | 477619 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-15.png | DOC-002 | PDF p. 15 | USABLE | 406136 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-16.png | DOC-002 | PDF p. 16 | USABLE | 426601 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-17.png | DOC-002 | PDF p. 17 | USABLE | 365859 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-18.png | DOC-002 | PDF p. 18 | USABLE | 340385 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-19.png | DOC-002 | PDF p. 19 | USABLE | 470624 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-20.png | DOC-002 | PDF p. 20 | USABLE | 450230 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-21.png | DOC-002 | PDF p. 21 | USABLE | 455736 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-22.png | DOC-002 | PDF p. 22 | USABLE | 353849 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-23.png | DOC-002 | PDF p. 23 | USABLE | 317800 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-24.png | DOC-002 | PDF p. 24 | USABLE | 328573 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-25.png | DOC-002 | PDF p. 25 | USABLE | 788465 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-26.png | DOC-002 | PDF p. 26 | USABLE | 485947 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-27.png | DOC-002 | PDF p. 27 | USABLE | 359024 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-28.png | DOC-002 | PDF p. 28 | USABLE | 450328 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-29.png | DOC-002 | PDF p. 29 | USABLE | 319044 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p001-p030/page-30.png | DOC-002 | PDF p. 30 | USABLE | 68652 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/cairo-39.png | DOC-002 | PDF p. 39 | DUPLICATE | 504816 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/layout.txt | DOC-002 | PDF pp. 31-60 | UNREADABLE | 111266 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-39.png | DOC-002 | PDF p. 39 | DUPLICATE | 144195 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-40.png | DOC-002 | PDF p. 40 | DUPLICATE | 123288 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-41.png | DOC-002 | PDF p. 41 | DUPLICATE | 117914 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-42.png | DOC-002 | PDF p. 42 | DUPLICATE | 167610 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-43.png | DOC-002 | PDF p. 43 | DUPLICATE | 148833 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-44.png | DOC-002 | PDF p. 44 | DUPLICATE | 108574 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-45.png | DOC-002 | PDF p. 45 | DUPLICATE | 80188 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-46.png | DOC-002 | PDF p. 46 | DUPLICATE | 13603 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-47.png | DOC-002 | PDF p. 47 | DUPLICATE | 61617 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-48.png | DOC-002 | PDF p. 48 | DUPLICATE | 72353 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-49.png | DOC-002 | PDF p. 49 | DUPLICATE | 51959 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-50.png | DOC-002 | PDF p. 50 | DUPLICATE | 14925 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-51.png | DOC-002 | PDF p. 51 | DUPLICATE | 45915 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/low-52.png | DOC-002 | PDF p. 52 | DUPLICATE | 54294 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/native.txt | DOC-002 | PDF pp. 31-60 | UNREADABLE | 89933 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-31.png | DOC-002 | PDF p. 31 | USABLE | 581990 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-31.txt | DOC-002 | PDF p. 31 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-32.png | DOC-002 | PDF p. 32 | USABLE | 767774 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-32.txt | DOC-002 | PDF p. 32 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-33.png | DOC-002 | PDF p. 33 | USABLE | 778150 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-33.txt | DOC-002 | PDF p. 33 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-34.png | DOC-002 | PDF p. 34 | USABLE | 649717 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-34.txt | DOC-002 | PDF p. 34 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-35.png | DOC-002 | PDF p. 35 | USABLE | 797520 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-35.txt | DOC-002 | PDF p. 35 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-36.png | DOC-002 | PDF p. 36 | USABLE | 438245 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-36.txt | DOC-002 | PDF p. 36 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-37.png | DOC-002 | PDF p. 37 | USABLE | 505342 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-37.txt | DOC-002 | PDF p. 37 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-38.png | DOC-002 | PDF p. 38 | USABLE | 464415 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-38.txt | DOC-002 | PDF p. 38 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-39.png | DOC-002 | PDF p. 39 | USABLE | 514814 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-39.txt | DOC-002 | PDF p. 39 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-40.png | DOC-002 | PDF p. 40 | USABLE | 433293 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-41.png | DOC-002 | PDF p. 41 | USABLE | 412488 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-42.png | DOC-002 | PDF p. 42 | USABLE | 565012 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-43.png | DOC-002 | PDF p. 43 | USABLE | 837434 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-44.png | DOC-002 | PDF p. 44 | USABLE | 590338 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-45.png | DOC-002 | PDF p. 45 | UNREADABLE | 414462 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-46.png | DOC-002 | PDF p. 46 | USABLE | 75007 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-47.png | DOC-002 | PDF p. 47 | USABLE | 303433 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-48.png | DOC-002 | PDF p. 48 | USABLE | 403692 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-49.png | DOC-002 | PDF p. 49 | USABLE | 234208 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-50.png | DOC-002 | PDF p. 50 | USABLE | 80196 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-51.png | DOC-002 | PDF p. 51 | USABLE | 208151 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-52.png | DOC-002 | PDF p. 52 | USABLE | 264587 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-53.png | DOC-002 | PDF p. 53 | USABLE | 133817 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-54.png | DOC-002 | PDF p. 54 | UNREADABLE | 330186 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-55.png | DOC-002 | PDF p. 55 | USABLE | 199784 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-56.png | DOC-002 | PDF p. 56 | USABLE | 375872 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-57.png | DOC-002 | PDF p. 57 | USABLE | 286780 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-58.png | DOC-002 | PDF p. 58 | USABLE | 334413 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-59.png | DOC-002 | PDF p. 59 | USABLE | 39698 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-60.png | DOC-002 | PDF p. 60 | USABLE | 424857 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/layout.txt | DOC-002 | PDF pp. 61-90 | UNREADABLE | 86684 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/native.txt | DOC-002 | PDF pp. 61-90 | UNREADABLE | 66130 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/p72.png | DOC-002 | PDF p. 72 | USABLE | 63154 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-61.png | DOC-002 | PDF p. 61 | USABLE | 304884 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-61.txt | DOC-002 | PDF p. 61 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-62.png | DOC-002 | PDF p. 62 | USABLE | 528400 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-62.txt | DOC-002 | PDF p. 62 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-63.png | DOC-002 | PDF p. 63 | USABLE | 319804 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-64.png | DOC-002 | PDF p. 64 | USABLE | 135068 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-65.png | DOC-002 | PDF p. 65 | USABLE | 266695 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-66.png | DOC-002 | PDF p. 66 | USABLE | 251082 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-67.png | DOC-002 | PDF p. 67 | USABLE | 114404 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-68.png | DOC-002 | PDF p. 68 | USABLE | 519170 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-69.png | DOC-002 | PDF p. 69 | USABLE | 34780 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-70.png | DOC-002 | PDF p. 70 | USABLE | 235436 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-71.png | DOC-002 | PDF p. 71 | USABLE | 414019 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-72.png | DOC-002 | PDF p. 72 | UNREADABLE | 87111 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-73.png | DOC-002 | PDF p. 73 | UNREADABLE | 595078 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-74.png | DOC-002 | PDF p. 74 | USABLE | 302072 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-75.png | DOC-002 | PDF p. 75 | USABLE | 281715 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-76.png | DOC-002 | PDF p. 76 | USABLE | 150001 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-77.png | DOC-002 | PDF p. 77 | USABLE | 168474 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-78.png | DOC-002 | PDF p. 78 | USABLE | 141427 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-79.png | DOC-002 | PDF p. 79 | USABLE | 152156 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-80.png | DOC-002 | PDF p. 80 | USABLE | 168805 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-81.png | DOC-002 | PDF p. 81 | USABLE | 153494 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-82.png | DOC-002 | PDF p. 82 | USABLE | 143485 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-83.png | DOC-002 | PDF p. 83 | USABLE | 105296 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-84.png | DOC-002 | PDF p. 84 | USABLE | 109860 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-85.png | DOC-002 | PDF p. 85 | USABLE | 98315 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-86.png | DOC-002 | PDF p. 86 | USABLE | 467185 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-87.png | DOC-002 | PDF p. 87 | USABLE | 144163 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-88.png | DOC-002 | PDF p. 88 | USABLE | 421990 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-89.png | DOC-002 | PDF p. 89 | USABLE | 406891 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p061-p090/page-90.png | DOC-002 | PDF p. 90 | USABLE | 118087 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p01.txt | DOC-003 | PDF p. 1 | USABLE | 620 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p02.txt | DOC-003 | PDF p. 2 | USABLE | 3276 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p03.txt | DOC-003 | PDF p. 3 | USABLE | 3748 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p04.txt | DOC-003 | PDF p. 4 | USABLE | 1114 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p05.txt | DOC-003 | PDF p. 5 | USABLE | 3441 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p06.txt | DOC-003 | PDF p. 6 | USABLE | 308 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p07.txt | DOC-003 | PDF p. 7 | USABLE | 1861 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p08.txt | DOC-003 | PDF p. 8 | USABLE | 3002 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p09.txt | DOC-003 | PDF p. 9 | USABLE | 791 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p10.txt | DOC-003 | PDF p. 10 | USABLE | 604 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p11.txt | DOC-003 | PDF p. 11 | USABLE | 2493 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p12.txt | DOC-003 | PDF p. 12 | USABLE | 141 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p13.txt | DOC-003 | PDF p. 13 | USABLE | 3298 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p14.txt | DOC-003 | PDF p. 14 | USABLE | 1479 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p15.txt | DOC-003 | PDF p. 15 | USABLE | 1840 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p16.txt | DOC-003 | PDF p. 16 | USABLE | 1857 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p17.txt | DOC-003 | PDF p. 17 | USABLE | 689 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p18.txt | DOC-003 | PDF p. 18 | USABLE | 2945 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p19.txt | DOC-003 | PDF p. 19 | USABLE | 1361 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p20.txt | DOC-003 | PDF p. 20 | USABLE | 1351 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p21.txt | DOC-003 | PDF p. 21 | USABLE | 2864 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p22.txt | DOC-003 | PDF p. 22 | USABLE | 1252 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p23.txt | DOC-003 | PDF p. 23 | USABLE | 1590 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p24.txt | DOC-003 | PDF p. 24 | USABLE | 3320 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p25.txt | DOC-003 | PDF p. 25 | USABLE | 2391 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p26.txt | DOC-003 | PDF p. 26 | USABLE | 1129 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p27.txt | DOC-003 | PDF p. 27 | USABLE | 586 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p28.txt | DOC-003 | PDF p. 28 | USABLE | 4732 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p29.txt | DOC-003 | PDF p. 29 | USABLE | 4852 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/layout/p30.txt | DOC-003 | PDF p. 30 | USABLE | 4908 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p01.txt | DOC-003 | PDF p. 1 | USABLE | 581 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p02.txt | DOC-003 | PDF p. 2 | USABLE | 3154 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p03.txt | DOC-003 | PDF p. 3 | USABLE | 3664 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p04.txt | DOC-003 | PDF p. 4 | USABLE | 1088 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p05.txt | DOC-003 | PDF p. 5 | USABLE | 3143 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p06.txt | DOC-003 | PDF p. 6 | USABLE | 293 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p07.txt | DOC-003 | PDF p. 7 | USABLE | 1854 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p08.txt | DOC-003 | PDF p. 8 | USABLE | 2737 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p09.txt | DOC-003 | PDF p. 9 | USABLE | 438 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p10.txt | DOC-003 | PDF p. 10 | USABLE | 598 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p11.txt | DOC-003 | PDF p. 11 | USABLE | 2485 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p12.txt | DOC-003 | PDF p. 12 | USABLE | 142 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p13.txt | DOC-003 | PDF p. 13 | USABLE | 3283 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p14.txt | DOC-003 | PDF p. 14 | USABLE | 1441 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p15.txt | DOC-003 | PDF p. 15 | USABLE | 1712 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p16.txt | DOC-003 | PDF p. 16 | USABLE | 1731 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p17.txt | DOC-003 | PDF p. 17 | USABLE | 672 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p18.txt | DOC-003 | PDF p. 18 | USABLE | 2939 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p19.txt | DOC-003 | PDF p. 19 | USABLE | 1356 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p20.txt | DOC-003 | PDF p. 20 | USABLE | 1346 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p21.txt | DOC-003 | PDF p. 21 | USABLE | 2720 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p22.txt | DOC-003 | PDF p. 22 | USABLE | 1171 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p23.txt | DOC-003 | PDF p. 23 | USABLE | 1450 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p24.txt | DOC-003 | PDF p. 24 | USABLE | 3271 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p25.txt | DOC-003 | PDF p. 25 | USABLE | 2275 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p26.txt | DOC-003 | PDF p. 26 | USABLE | 1012 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p27.txt | DOC-003 | PDF p. 27 | USABLE | 411 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p28.txt | DOC-003 | PDF p. 28 | USABLE | 2915 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p29.txt | DOC-003 | PDF p. 29 | USABLE | 2959 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p001-p030/native/p30.txt | DOC-003 | PDF p. 30 | USABLE | 2896 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/figure-34.png | DOC-003 | PDF p. 34 | DUPLICATE | 317876 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/figure-35.png | DOC-003 | PDF p. 35 | DUPLICATE | 443583 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/page-31-layout.txt | DOC-003 | PDF p. 31 | USABLE | 3877 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/page-31-native.txt | DOC-003 | PDF p. 31 | USABLE | 2382 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/page-32-layout.txt | DOC-003 | PDF p. 32 | USABLE | 377 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/page-32-native.txt | DOC-003 | PDF p. 32 | USABLE | 368 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/page-33-layout.txt | DOC-003 | PDF p. 33 | USABLE | 323 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/page-33-native.txt | DOC-003 | PDF p. 33 | USABLE | 309 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/page-36-layout.txt | DOC-003 | PDF p. 36 | USABLE | 2667 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/page-36-native.txt | DOC-003 | PDF p. 36 | USABLE | 1258 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/page-37-layout.txt | DOC-003 | PDF p. 37 | USABLE | 826 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p031-p060/page-37-native.txt | DOC-003 | PDF p. 37 | USABLE | 600 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p061-p069/page-067-layout.txt | DOC-003 | PDF p. 67 | USABLE | 3110 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p061-p069/page-067-native.txt | DOC-003 | PDF p. 67 | USABLE | 941 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p061-p069/page-067-ocr.txt | DOC-003 | PDF p. 67 | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p061-p069/page-067.png | DOC-003 | PDF p. 67 | USABLE | 194819 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p061-p069/page-068-layout.txt | DOC-003 | PDF p. 68 | USABLE | 600 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p061-p069/page-068-native.txt | DOC-003 | PDF p. 68 | USABLE | 264 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p061-p069/page-068.png | DOC-003 | PDF p. 68 | USABLE | 63121 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p061-p069/page-069-layout.txt | DOC-003 | PDF p. 69 | USABLE | 2058 |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003/p061-p069/page-069-native.txt | DOC-003 | PDF p. 69 | USABLE | 1915 |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-002-page-015.png | DOC-002 | Source identity/page locator metadata | DUPLICATE | 493026 |

## Exact unique text burdens

Preferred native text has 58,292 Unicode characters for DOC-001 and 103,297 for DOC-003. Within DOC-003: pp. 1-30 have 55,489; pp. 34-35 and 38-66 have 39,807; pp. 31-33, 36-37, 67-69 have 8,001. All 69 pages fit a single text context below 200,000 characters; rendered results display work covers 31 pages (34-35, 38-66) and therefore stays within the 32-page bound. The terminal reference images need not be loaded together with all result displays. DOC-002 has only 367 characters of canonical readable title OCR on p. 1; full mapping must use its images or fresh OCR.

Registry count: 341 assets, comprising 337 page/text/document-record files and four source/page manifests. The two retained scientific extractor narrative files were inventoried by filename only and not read or reused. No new extraction, rendering, or OCR derivative was produced by curation. `file` confirmed sampled PNG encoding/dimensions; the protocol p. 90 and p. 76 images were visually inspected for legibility, identity, and bound plan-bundle context. Historical image and native/OCR engines remain as recorded above; the current independent PDF information engine is PyMuPDF 1.28.0 through the bundled helper.

## Current decoder checks and fresh replacements

Mapping revealed that reusable DOC-002 images for PDF pp. 45, 72, and 73 were not usable by the image decoder. File presence/nonzero size during inventory did not establish decoder fitness. Their native/layout text is also unreadable, so these three units are reclassified fresh-required and covered with CPU PyMuPDF 1.28.0 source renders through the bundled helper. Reused files remain unchanged and in the integrity hash set. Mapping artifacts record the replacement paths and exact source-page inspection. Additional fresh renders of already reusable units serve visual confirmation and do not increase fresh-required counts.

DOC-002 p. 54 also failed the reused-image decoder and was covered by direct CPU PyMuPDF source render preprocessing/plan002-page054.png and explicit visual inspection. The final affected fresh-required set is pp. 45, 54, 72, 73 (four units); all other reusable assets remain locator aids.
