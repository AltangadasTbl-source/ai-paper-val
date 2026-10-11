# Evidence-Asset Inventory and Mapper Handoff

Inventory covers every existing extraction, OCR, rendered page, page metadata, page manifest, document record, and source-location map under the pre-existing audit area. No old candidate, verifier, critic, endetail, classification, or final-report content was read as a scientific input. Mixed scientific maps were identified only from their headings and are excluded from reuse; new relationships must be rebuilt from the supplied sources and raw derivatives.

Engine record: the five full layouts are exact current-source matches to Poppler pdftotext 26.01.0 `-layout` output. Normalized per-page text retains page-number source mapping and is auxiliary to the complete layout. Existing OCR is rapidocr-cpu according to page metadata/manifests, and may contain imperfect character transcription. Existing PNGs are full-page Poppler-style renders used as visual locators; final quantitative authority is the exact current supplied PDF page. All reused eligible files are hashed in reused_artifact_hashes_before.sha256, using package-relative paths. No reused file was modified. Duplicate and excluded mixed documents are inventoried but are not hashed as reused evidence.

`USABLE` means readable and useful for its stated unit and method, not authority for a candidate determination. `PARTIAL` means limited transcription, sparse text, or metadata with incomplete scientific-unit coverage. Partial artifacts do not leave an uncovered unit where the current-source-matched complete layout and a complementary image supply the same source page. `DUPLICATE` means an alternative raw derivative overlapping selected evidence. No artifact was judged STALE or UNREADABLE after source matching of the complete layouts and file-format inspection of retained images.

| Artifact path | Source and exact units | Method / engine | Fitness | Reuse treatment |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001-main-article/completion_record.md | DOC-001 Source-level administrative metadata | Legacy processing metadata; content not read | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/initial_document_record.md | DOC-001 PDF pp. 1-14; old extraction scope 1-11 | Document identity/location record | PARTIAL | REUSED identity only |
| .ai_paper_validation/document_outputs/DOC-001-main-article/main_text_extraction.md | DOC-001 Old selected-page map, scientific content excluded | Mixed scientific extraction/map; headings inventoried only | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-001.txt | DOC-001 PDF p. 1 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-002.txt | DOC-001 PDF p. 2 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-003.txt | DOC-001 PDF p. 3 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-004.txt | DOC-001 PDF p. 4 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-005.txt | DOC-001 PDF p. 5 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-006.txt | DOC-001 PDF p. 6 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-007.txt | DOC-001 PDF p. 7 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-008.txt | DOC-001 PDF p. 8 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-009.txt | DOC-001 PDF p. 9 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-010.txt | DOC-001 PDF p. 10 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-011.txt | DOC-001 PDF p. 11 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/ocr/page-003.txt | DOC-001 PDF p. 3 | rapidocr-cpu OCR | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/page_images/table_check-07.png | DOC-001 PDF p. 7 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/page_manifest.md | DOC-001 PDF pp. 1-11 | Page-location manifest | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/page_metadata/page-003.ocr.json | DOC-001 PDF p. 3 | OCR engine metadata | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing_record.md | DOC-001 Source-level administrative metadata | Legacy processing metadata; content not read | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-001/main_layout.txt | DOC-001 PDF pp. 1-14 | pdftotext -layout exact current-source match | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol/completion_record.md | DOC-002 Source-level administrative metadata | Legacy processing metadata; content not read | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol/initial_document_record.md | DOC-002 PDF pp. 1-75 | Document identity/location record | PARTIAL | REUSED identity only |
| .ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol/preprocessing_record.md | DOC-002 Source-level administrative metadata | Legacy processing metadata; content not read | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-003-supplement-2-sap/completion_record.md | DOC-003 Source-level administrative metadata | Legacy processing metadata; content not read | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-003-supplement-2-sap/initial_document_record.md | DOC-003 PDF pp. 1-30 | Document identity/location record | PARTIAL | REUSED identity only |
| .ai_paper_validation/document_outputs/DOC-003-supplement-2-sap/preprocessing_record.md | DOC-003 Source-level administrative metadata | Legacy processing metadata; content not read | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/completion_record.md | DOC-004 Source-level administrative metadata | Legacy processing metadata; content not read | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/initial_document_record.md | DOC-004 PDF pp. 1-29; old extraction scope 1-27 | Document identity/location record | PARTIAL | REUSED identity only |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-001.txt | DOC-004 PDF p. 1 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-002.txt | DOC-004 PDF p. 2 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-003.txt | DOC-004 PDF p. 3 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-004.txt | DOC-004 PDF p. 4 | Native/layout page text | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-005.txt | DOC-004 PDF p. 5 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-006.txt | DOC-004 PDF p. 6 | Native/layout page text | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-007.txt | DOC-004 PDF p. 7 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-008.txt | DOC-004 PDF p. 8 | Native/layout page text | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-009.txt | DOC-004 PDF p. 9 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-010.txt | DOC-004 PDF p. 10 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-011.txt | DOC-004 PDF p. 11 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-012.txt | DOC-004 PDF p. 12 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-013.txt | DOC-004 PDF p. 13 | Native/layout page text | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-014.txt | DOC-004 PDF p. 14 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-015.txt | DOC-004 PDF p. 15 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-016.txt | DOC-004 PDF p. 16 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-017.txt | DOC-004 PDF p. 17 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-018.txt | DOC-004 PDF p. 18 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-019.txt | DOC-004 PDF p. 19 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-020.txt | DOC-004 PDF p. 20 | Native/layout page text | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-021.txt | DOC-004 PDF p. 21 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-022.txt | DOC-004 PDF p. 22 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-023.txt | DOC-004 PDF p. 23 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-024.txt | DOC-004 PDF p. 24 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-025.txt | DOC-004 PDF p. 25 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-026.txt | DOC-004 PDF p. 26 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/normalized_text/page-027.txt | DOC-004 PDF p. 27 | Native/layout page text | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/ocr/page-004.txt | DOC-004 PDF p. 4 | rapidocr-cpu OCR | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/ocr/page-006.txt | DOC-004 PDF p. 6 | rapidocr-cpu OCR | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/ocr/page-008.txt | DOC-004 PDF p. 8 | rapidocr-cpu OCR | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/ocr/page-013.txt | DOC-004 PDF p. 13 | rapidocr-cpu OCR | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/ocr/page-020.txt | DOC-004 PDF p. 20 | rapidocr-cpu OCR | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/figure_render-25.png | DOC-004 PDF p. 25 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/figure_render-26.png | DOC-004 PDF p. 26 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/figure_render-27.png | DOC-004 PDF p. 27 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/page-004.png | DOC-004 PDF p. 4 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/page-006.png | DOC-004 PDF p. 6 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/page-008.png | DOC-004 PDF p. 8 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/page-013.png | DOC-004 PDF p. 13 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/page-020.png | DOC-004 PDF p. 20 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/table_check-07.png | DOC-004 PDF p. 7 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/table_check-10.png | DOC-004 PDF p. 10 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_images/table_check-21.png | DOC-004 PDF p. 21 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_manifest.md | DOC-004 PDF pp. 1-27 | Page-location manifest | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_metadata/page-004.ocr.json | DOC-004 PDF p. 4 | OCR engine metadata | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_metadata/page-006.ocr.json | DOC-004 PDF p. 6 | OCR engine metadata | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_metadata/page-008.ocr.json | DOC-004 PDF p. 8 | OCR engine metadata | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_metadata/page-013.ocr.json | DOC-004 PDF p. 13 | OCR engine metadata | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/page_metadata/page-020.ocr.json | DOC-004 PDF p. 20 | OCR engine metadata | PARTIAL | REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/preprocessing_record.md | DOC-004 Source-level administrative metadata | Legacy processing metadata; content not read | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-004-supplement-3-results/results_supplement_evidence_map.md | DOC-004 Old selected-page map, scientific content excluded | Mixed scientific extraction/map; headings inventoried only | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-004/supp3-p7.pdf | DOC-004 PDF p. 7 | Single-page PDF derivative | DUPLICATE | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-004/supp3_layout.txt | DOC-004 PDF pp. 1-29 | pdftotext -layout exact current-source match | USABLE | REUSED |
| .ai_paper_validation/document_outputs/DOC-005-supplement-4-data-sharing/completion_record.md | DOC-005 Source-level administrative metadata | Legacy processing metadata; content not read | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/DOC-005-supplement-4-data-sharing/initial_document_record.md | DOC-005 PDF p. 1 | Document identity/location record | PARTIAL | REUSED identity only |
| .ai_paper_validation/document_outputs/DOC-005-supplement-4-data-sharing/preprocessing_record.md | DOC-005 Source-level administrative metadata | Legacy processing metadata; content not read | PARTIAL | NOT_REUSED |
| .ai_paper_validation/document_outputs/package_manifest.md | DOC-001/DOC-002/DOC-003/DOC-004/DOC-005 Source-level identity | Package document-location record; not read | PARTIAL | NOT_REUSED |
| .ai_paper_validation/preprocessing/ocr_backend.json | DOC-001/DOC-004 Source-level OCR engine | OCR engine metadata | PARTIAL | REUSED |
| .ai_paper_validation/preprocessing/rendered/supp3-03.png | DOC-004 PDF p. 3 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/preprocessing/rendered/supp3-07.png | DOC-004 PDF p. 7 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/preprocessing/rendered/supp3-09.png | DOC-004 PDF p. 9 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/preprocessing/rendered/supp3-10.png | DOC-004 PDF p. 10 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-002_supp1_layout_fresh.txt | DOC-002 PDF pp. 1-75 | pdftotext -layout exact current-source match | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-003_supp2_layout_fresh.txt | DOC-003 PDF pp. 1-30 | pdftotext -layout exact current-source match | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-004_visual-25.png | DOC-004 PDF p. 25 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-004_visual-26.png | DOC-004 PDF p. 26 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-004_visual-27.png | DOC-004 PDF p. 27 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-005_supp4_layout_fresh.txt | DOC-005 PDF p. 1 | pdftotext -layout exact current-source match | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/DOC-005_visual.png | DOC-005 PDF p. 1 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc001-p004.png | DOC-001 PDF p. 4 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc001-p005.png | DOC-001 PDF p. 5 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc001-p007.png | DOC-001 PDF p. 7 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc001-p010.png | DOC-001 PDF p. 10 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc004-p003.png | DOC-004 PDF p. 3 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc004-p005.png | DOC-004 PDF p. 5 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc004-p007.png | DOC-004 PDF p. 7 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc004-p010.png | DOC-004 PDF p. 10 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc004-p011.png | DOC-004 PDF p. 11 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc004-p016.png | DOC-004 PDF p. 16 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc004-p017.png | DOC-004 PDF p. 17 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc004-p019.png | DOC-004 PDF p. 19 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc004-p021.png | DOC-004 PDF p. 21 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/doc004-p023.png | DOC-004 PDF p. 23 | Retained full-page PNG render | USABLE | REUSED |
| .ai_paper_validation/tmp_rights/supp3.txt | DOC-004 PDF pp. 1-29 | Layout text duplicate of selected full supplement layout | DUPLICATE | NOT_REUSED |
| .ai_paper_validation/tmp_rights/supp3_metadata.txt | DOC-004 PDF metadata | XMP metadata | PARTIAL | NOT_REUSED |

## Exact Mapper Assignments

Main mapper: DOC-001 pp. 1-14 from complete main_layout.txt. The old per-page collection covers only pp. 1-11; pp. 12-14 are mandatory scope from the complete layout. Retained main p. 3 OCR supplies flow-diagram transcription; table and previous source-page renders provide p. 4, 5, 7, and 10 visual context.

Protocol support shard: DOC-002 pp. 1-75 from DOC-002_supp1_layout_fresh.txt, 184474 bytes. This full-source text independently fits the 200000-character bound.

Other support shard: DOC-003 pp. 1-30, DOC-004 pp. 1-29, and DOC-005 p. 1, using their three complete layouts (157454 bytes combined). Sparse DOC-004 pp. 4, 6, 13, and 20 pair native/layout text with retained OCR and matching page images. DOC-004 p. 8 has only copyright text in current native extraction (61 bytes including form feed), an equally sparse retained OCR, and a page image; inspect the exact supplied page before stating its missing-content limitation. DOC-004 pp. 25-27 use retained figure renders. DOC-004 pp. 28-29 are mandatory fresh scientific mapping from existing complete layout despite the old page-manifest exclusions.

All complete-layout assets are USABLE. No page requires fresh extraction solely because no derivative exists. Every one of the 149 physical pages still requires new mapping and quantitative relationship discovery. Existing derivative absence for a subset of per-page text/images is an optimization limitation only, since complete source-matched layout and direct PDF are available.

## Curation Totals and Remaining Confirmation

113 eligible assets inventoried: 72 USABLE, 39 PARTIAL, 2 DUPLICATE; 97 selected reusable artifacts hashed. Every source has a byte-identical full-layout asset, so unique reusable coverage is 149 pages and fresh-required extraction is zero. The retained DOC-004 p. 8 image was visually inspected during curation and contains only the copyright footer; the downstream mapper must confirm the exact current source page before final limitation wording. The old main page manifest references a p. 3 PNG that is absent from the existing audit area; retained main p. 3 text and OCR and the complete main layout remain available, and a direct current PDF render can be produced if quantitative visual confirmation requires it. This missing optional image does not remove a page from mapping scope.

## New derivatives and reconstructed maps

New scientific maps and checker outputs are held only under review_1_6 and are not reused legacy evidence. Source-linked rendering/extraction commands and engines are recorded in each responsible map/checker. Direct CPU Poppler26.01.0 supplied targeted main p3/p6/p9, protocol p18/p24/p45/p54 and reviewer p22/p23/p27/p28/p38/p44/p49/p53, SAP p7/p15, current blank results p8 and table-heading/red-wine p1/p7 confirmation. None required OCR or a fallback environment. Existing source-matched figure and table images were read unchanged. Any quoted legacy OCR glyph was compared with source-native/current rendered glyph before numerical use; source values remain authority.
