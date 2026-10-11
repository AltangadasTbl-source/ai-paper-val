# Reusable Evidence Asset Inventory

Inventory scope: every existing extraction, OCR text/metadata, rendered page, page manifest, document record, and location map below the audit area. Earlier candidate, checker, screening, verifier, critic, endetail, classification and final-report records are excluded. Historical preprocessing scripts are inventoried as tooling only and are neither run nor reused as scientific evidence. No workbook, CSV, Office extraction, or separate structured table extraction exists.

The five complete layout text files in `review_1_6_1/preprocessing/recheck/` are preferred. For each one, `pdftotext -layout SOURCE - | cmp -s - ASSET` returned equality. Its form-feed-separated page count matches `pdfinfo SOURCE`. These direct commands used Poppler 26.01.0; existing extraction engines were native PDF extraction/Poppler where recorded, rendering engines are existing PDF page rendering (historical version not recorded), and OCR engine is Tesseract CPU, documented by OCR metadata. No derivative was newly written by this curator. Existing engine version omissions do not undermine verified source/page coverage.

Fitness: USABLE covers its stated source unit; PARTIAL has selected-unit or metadata-only coverage; STALE includes unavailable target paths; DUPLICATE is redundant with the preferred derivative; UNREADABLE would lack usable content. Partial records never define the current scientific scope. All selected reusable artifacts are included in the before-hash file; unselected duplicate and administrative records are preserved and inventoried.

| Asset path | Kind / engine | Exact source units | Fitness | Reused | Assessment |
|---|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001/ai_training_restriction_record.json | Administrative document record | DOC-001 PDF pp. 1–11 | PARTIAL | No | No quantitative extraction coverage. |
| .ai_paper_validation/document_outputs/DOC-001/document_status.json | Source/location metadata | DOC-001 PDF pp. 1–11 | PARTIAL | Yes | Historical locators only; prior scope exclusions not inherited. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text.txt | Aggregate normalized/native text | DOC-001 PDF pp. 1–11 | PARTIAL | Yes | Only listed units covered; complete layout provides remaining pages. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_001.txt | Native page text / historical extractor | DOC-001 PDF p. 1 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_002.txt | Native page text / historical extractor | DOC-001 PDF p. 2 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_003.txt | Native page text / historical extractor | DOC-001 PDF p. 3 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_004.txt | Native page text / historical extractor | DOC-001 PDF p. 4 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_005.txt | Native page text / historical extractor | DOC-001 PDF p. 5 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_006.txt | Native page text / historical extractor | DOC-001 PDF p. 6 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_007.txt | Native page text / historical extractor | DOC-001 PDF p. 7 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_008.txt | Native page text / historical extractor | DOC-001 PDF p. 8 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_009.txt | Native page text / historical extractor | DOC-001 PDF p. 9 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_010.txt | Native page text / historical extractor | DOC-001 PDF p. 10 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_011.txt | Native page text / historical extractor | DOC-001 PDF p. 11 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_text/page_003.txt | OCR text / Tesseract CPU | DOC-001 PDF p. 3 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_text/page_005.txt | OCR text / Tesseract CPU | DOC-001 PDF p. 5 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_text/page_006.txt | OCR text / Tesseract CPU | DOC-001 PDF p. 6 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_text/page_007.txt | OCR text / Tesseract CPU | DOC-001 PDF p. 7 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_text/page_008.txt | OCR text / Tesseract CPU | DOC-001 PDF p. 8 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-001/page_manifest.json | Source/location metadata | DOC-001 PDF pp. 1–11 | PARTIAL | Yes | Historical locators only; prior scope exclusions not inherited. |
| .ai_paper_validation/document_outputs/DOC-001/rendered_pages/page_003.png | Rendered page / historical PDF renderer | DOC-001 PDF p. 3 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-001/rendered_pages/page_005.png | Rendered page / historical PDF renderer | DOC-001 PDF p. 5 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-001/rendered_pages/page_006.png | Rendered page / historical PDF renderer | DOC-001 PDF p. 6 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-001/rendered_pages/page_007.png | Rendered page / historical PDF renderer | DOC-001 PDF p. 7 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-001/rendered_pages/page_008.png | Rendered page / historical PDF renderer | DOC-001 PDF p. 8 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-002/ai_training_restriction_record.json | Administrative document record | DOC-002 PDF pp. 1–60 | PARTIAL | No | No quantitative extraction coverage. |
| .ai_paper_validation/document_outputs/DOC-002/document_status.json | Source/location metadata | DOC-002 PDF pp. 1–60 | PARTIAL | Yes | Historical locators only; prior scope exclusions not inherited. |
| .ai_paper_validation/document_outputs/DOC-003/ai_training_restriction_record.json | Administrative document record | DOC-003 PDF pp. 1–5 | PARTIAL | No | No quantitative extraction coverage. |
| .ai_paper_validation/document_outputs/DOC-003/document_status.json | Source/location metadata | DOC-003 PDF pp. 1–5 | PARTIAL | Yes | Historical locators only; prior scope exclusions not inherited. |
| .ai_paper_validation/document_outputs/DOC-004/ai_training_restriction_record.json | Administrative document record | DOC-004 PDF pp. 1, 2, 16–23 | PARTIAL | No | No quantitative extraction coverage. |
| .ai_paper_validation/document_outputs/DOC-004/document_status.json | Source/location metadata | DOC-004 PDF pp. 1, 2, 16–23 | PARTIAL | Yes | Historical locators only; prior scope exclusions not inherited. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text.txt | Aggregate normalized/native text | DOC-004 PDF pp. 1, 2, 16–23 | PARTIAL | Yes | Only listed units covered; complete layout provides remaining pages. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_001.txt | Native page text / historical extractor | DOC-004 PDF p. 1 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_002.txt | Native page text / historical extractor | DOC-004 PDF p. 2 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_016.txt | Native page text / historical extractor | DOC-004 PDF p. 16 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_017.txt | Native page text / historical extractor | DOC-004 PDF p. 17 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_018.txt | Native page text / historical extractor | DOC-004 PDF p. 18 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_019.txt | Native page text / historical extractor | DOC-004 PDF p. 19 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_020.txt | Native page text / historical extractor | DOC-004 PDF p. 20 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_021.txt | Native page text / historical extractor | DOC-004 PDF p. 21 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_022.txt | Native page text / historical extractor | DOC-004 PDF p. 22 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_023.txt | Native page text / historical extractor | DOC-004 PDF p. 23 | USABLE | Yes | Exact-page locator/transcription aid. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_016.txt | OCR text / Tesseract CPU | DOC-004 PDF p. 16 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_017.txt | OCR text / Tesseract CPU | DOC-004 PDF p. 17 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_018.txt | OCR text / Tesseract CPU | DOC-004 PDF p. 18 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_019.txt | OCR text / Tesseract CPU | DOC-004 PDF p. 19 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_020.txt | OCR text / Tesseract CPU | DOC-004 PDF p. 20 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_021.txt | OCR text / Tesseract CPU | DOC-004 PDF p. 21 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_022.txt | OCR text / Tesseract CPU | DOC-004 PDF p. 22 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_023.txt | OCR text / Tesseract CPU | DOC-004 PDF p. 23 | USABLE | Yes | Exact-page transcription aid; source remains authority. |
| .ai_paper_validation/document_outputs/DOC-004/page_manifest.json | Source/location metadata | DOC-004 PDF pp. 1, 2, 16–23 | PARTIAL | Yes | Historical locators only; prior scope exclusions not inherited. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_016.png | Rendered page / historical PDF renderer | DOC-004 PDF p. 16 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_017.png | Rendered page / historical PDF renderer | DOC-004 PDF p. 17 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_018.png | Rendered page / historical PDF renderer | DOC-004 PDF p. 18 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_019.png | Rendered page / historical PDF renderer | DOC-004 PDF p. 19 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_020.png | Rendered page / historical PDF renderer | DOC-004 PDF p. 20 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_021.png | Rendered page / historical PDF renderer | DOC-004 PDF p. 21 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_022.png | Rendered page / historical PDF renderer | DOC-004 PDF p. 22 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_023.png | Rendered page / historical PDF renderer | DOC-004 PDF p. 23 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/document_outputs/DOC-005/ai_training_restriction_record.json | Administrative document record | DOC-005 PDF p. 1 | PARTIAL | No | No quantitative extraction coverage. |
| .ai_paper_validation/document_outputs/DOC-005/document_status.json | Source/location metadata | DOC-005 PDF p. 1 | PARTIAL | Yes | Historical locators only; prior scope exclusions not inherited. |
| .ai_paper_validation/package_manifest.md | Source/location metadata | Source identity metadata | PARTIAL | Yes | Historical locators only; prior scope exclusions not inherited. |
| .ai_paper_validation/preprocessing/README.md | Source/location metadata | Source identity metadata | PARTIAL | No | Historical preprocessing documentation; no unique source coverage. |
| .ai_paper_validation/preprocessing/complete_current_run.py | Historical tooling | No source units | DUPLICATE | No | Preserved; not executed. |
| .ai_paper_validation/preprocessing/current_run_manifest.json | Source/location metadata | Source identity metadata | PARTIAL | Yes | Historical locators only; prior scope exclusions not inherited. |
| .ai_paper_validation/preprocessing/extract_native_text.py | Historical tooling | No source units | DUPLICATE | No | Preserved; not executed. |
| .ai_paper_validation/preprocessing/finalize_manifests.py | Historical tooling | No source units | DUPLICATE | No | Preserved; not executed. |
| .ai_paper_validation/preprocessing/ocr_backend.json | Source/location metadata | Source identity metadata | PARTIAL | Yes | Historical locators only; prior scope exclusions not inherited. |
| .ai_paper_validation/preprocessing/render_required_visuals.py | Historical tooling | No source units | DUPLICATE | No | Preserved; not executed. |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_confirmation/main-layout.txt | Layout text / Poppler | DOC-001 PDF pp. 1–11 | DUPLICATE | No | Identical to selected recheck layout; no additional unique coverage. |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_confirmation/protocol-layout.txt | Layout text / Poppler | DOC-002 PDF pp. 1–60 | DUPLICATE | No | Identical to selected recheck layout; no additional unique coverage. |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_confirmation/protocol-p16.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 16 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_confirmation/protocol-p18.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 18 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_confirmation/protocol-p23.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 23 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_confirmation/protocol-p28.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 28 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_confirmation/protocol-p43.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 43 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_confirmation/results-layout.txt | Layout text / Poppler | DOC-004 PDF pp. 1–25 | DUPLICATE | No | Identical to selected recheck layout; no additional unique coverage. |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_confirmation/sap-p4.png | Rendered page / historical PDF renderer | DOC-003 PDF p. 4 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/curator/asset_paths.txt | Source/location metadata | Legacy asset path map | STALE | No | Several listed preserved paths are absent; current inventory used. |
| .ai_paper_validation/review_1_6_1/preprocessing/numeric_visual/main-p4.png | Rendered page / historical PDF renderer | DOC-001 PDF p. 4 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/data-sharing-layout.txt | Layout text / Poppler | DOC-005 PDF p. 1 | USABLE | Yes | Complete page boundaries and exact byte match to direct current source extraction. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Layout text / Poppler | DOC-001 PDF pp. 1–11 | USABLE | Yes | Complete page boundaries and exact byte match to direct current source extraction. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-p8.png | Rendered page / historical PDF renderer | DOC-001 PDF p. 8 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Layout text / Poppler | DOC-002 PDF pp. 1–60 | USABLE | Yes | Complete page boundaries and exact byte match to direct current source extraction. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-p16.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 16 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-p23.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 23 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-p28.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 28 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-p43.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 43 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Layout text / Poppler | DOC-004 PDF pp. 1–25 | USABLE | Yes | Complete page boundaries and exact byte match to direct current source extraction. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-p17.png | Rendered page / historical PDF renderer | DOC-004 PDF p. 17 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/sap-layout.txt | Layout text / Poppler | DOC-003 PDF pp. 1–5 | USABLE | Yes | Complete page boundaries and exact byte match to direct current source extraction. |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/sap-p4.png | Rendered page / historical PDF renderer | DOC-003 PDF p. 4 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/support_visual/protocol-p12.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 12 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/support_visual/protocol-p31.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 31 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/support_visual/protocol-p32.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 32 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |
| .ai_paper_validation/review_1_6_1/preprocessing/support_visual/protocol-p38.png | Rendered page / historical PDF renderer | DOC-002 PDF p. 38 | USABLE | Yes | Exact-page visual aid; historical engine version unrecorded. |

## Exact Page-to-Asset Coverage Map

Each row maps one unique source unit to its primary usable existing asset. Whole-document layout uses stable one-based form-feed page positions, not physical lines. Additional exact-page OCR/images above supplement these locators. Protocol p. 31 uses the existing rendered image because layout retains only its caption. Protocol pp. 32 and 38 were visually inspected in their existing images: p. 32's body is the assessment box retained by native text; p. 38's body is blank. Main and supplement rendered-page and OCR assets provide table/figure coverage without changing unique page counts.

| Source ID | Exact unit | Primary reusable asset | Locator / fitness |
|---|---|---|---|
| DOC-001 | PDF p. 1 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Form-feed page 1 / USABLE |
| DOC-001 | PDF p. 2 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Form-feed page 2 / USABLE |
| DOC-001 | PDF p. 3 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Form-feed page 3 / USABLE |
| DOC-001 | PDF p. 4 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Form-feed page 4 / USABLE |
| DOC-001 | PDF p. 5 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Form-feed page 5 / USABLE |
| DOC-001 | PDF p. 6 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Form-feed page 6 / USABLE |
| DOC-001 | PDF p. 7 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Form-feed page 7 / USABLE |
| DOC-001 | PDF p. 8 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Form-feed page 8 / USABLE |
| DOC-001 | PDF p. 9 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Form-feed page 9 / USABLE |
| DOC-001 | PDF p. 10 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Form-feed page 10 / USABLE |
| DOC-001 | PDF p. 11 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt | Form-feed page 11 / USABLE |
| DOC-002 | PDF p. 1 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 1 / USABLE |
| DOC-002 | PDF p. 2 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 2 / USABLE |
| DOC-002 | PDF p. 3 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 3 / USABLE |
| DOC-002 | PDF p. 4 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 4 / USABLE |
| DOC-002 | PDF p. 5 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 5 / USABLE |
| DOC-002 | PDF p. 6 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 6 / USABLE |
| DOC-002 | PDF p. 7 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 7 / USABLE |
| DOC-002 | PDF p. 8 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 8 / USABLE |
| DOC-002 | PDF p. 9 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 9 / USABLE |
| DOC-002 | PDF p. 10 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 10 / USABLE |
| DOC-002 | PDF p. 11 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 11 / USABLE |
| DOC-002 | PDF p. 12 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 12 / USABLE |
| DOC-002 | PDF p. 13 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 13 / USABLE |
| DOC-002 | PDF p. 14 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 14 / USABLE |
| DOC-002 | PDF p. 15 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 15 / USABLE |
| DOC-002 | PDF p. 16 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 16 / USABLE |
| DOC-002 | PDF p. 17 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 17 / USABLE |
| DOC-002 | PDF p. 18 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 18 / USABLE |
| DOC-002 | PDF p. 19 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 19 / USABLE |
| DOC-002 | PDF p. 20 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 20 / USABLE |
| DOC-002 | PDF p. 21 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 21 / USABLE |
| DOC-002 | PDF p. 22 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 22 / USABLE |
| DOC-002 | PDF p. 23 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 23 / USABLE |
| DOC-002 | PDF p. 24 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 24 / USABLE |
| DOC-002 | PDF p. 25 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 25 / USABLE |
| DOC-002 | PDF p. 26 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 26 / USABLE |
| DOC-002 | PDF p. 27 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 27 / USABLE |
| DOC-002 | PDF p. 28 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 28 / USABLE |
| DOC-002 | PDF p. 29 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 29 / USABLE |
| DOC-002 | PDF p. 30 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 30 / USABLE |
| DOC-002 | PDF p. 31 | .ai_paper_validation/review_1_6_1/preprocessing/support_visual/protocol-p31.png | Full rendered PDF p. 31 / USABLE |
| DOC-002 | PDF p. 32 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 32 / USABLE |
| DOC-002 | PDF p. 33 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 33 / USABLE |
| DOC-002 | PDF p. 34 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 34 / USABLE |
| DOC-002 | PDF p. 35 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 35 / USABLE |
| DOC-002 | PDF p. 36 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 36 / USABLE |
| DOC-002 | PDF p. 37 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 37 / USABLE |
| DOC-002 | PDF p. 38 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 38 / USABLE |
| DOC-002 | PDF p. 39 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 39 / USABLE |
| DOC-002 | PDF p. 40 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 40 / USABLE |
| DOC-002 | PDF p. 41 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 41 / USABLE |
| DOC-002 | PDF p. 42 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 42 / USABLE |
| DOC-002 | PDF p. 43 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 43 / USABLE |
| DOC-002 | PDF p. 44 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 44 / USABLE |
| DOC-002 | PDF p. 45 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 45 / USABLE |
| DOC-002 | PDF p. 46 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 46 / USABLE |
| DOC-002 | PDF p. 47 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 47 / USABLE |
| DOC-002 | PDF p. 48 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 48 / USABLE |
| DOC-002 | PDF p. 49 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 49 / USABLE |
| DOC-002 | PDF p. 50 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 50 / USABLE |
| DOC-002 | PDF p. 51 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 51 / USABLE |
| DOC-002 | PDF p. 52 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 52 / USABLE |
| DOC-002 | PDF p. 53 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 53 / USABLE |
| DOC-002 | PDF p. 54 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 54 / USABLE |
| DOC-002 | PDF p. 55 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 55 / USABLE |
| DOC-002 | PDF p. 56 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 56 / USABLE |
| DOC-002 | PDF p. 57 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 57 / USABLE |
| DOC-002 | PDF p. 58 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 58 / USABLE |
| DOC-002 | PDF p. 59 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 59 / USABLE |
| DOC-002 | PDF p. 60 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/protocol-layout.txt | Form-feed page 60 / USABLE |
| DOC-003 | PDF p. 1 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/sap-layout.txt | Form-feed page 1 / USABLE |
| DOC-003 | PDF p. 2 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/sap-layout.txt | Form-feed page 2 / USABLE |
| DOC-003 | PDF p. 3 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/sap-layout.txt | Form-feed page 3 / USABLE |
| DOC-003 | PDF p. 4 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/sap-layout.txt | Form-feed page 4 / USABLE |
| DOC-003 | PDF p. 5 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/sap-layout.txt | Form-feed page 5 / USABLE |
| DOC-004 | PDF p. 1 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 1 / USABLE |
| DOC-004 | PDF p. 2 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 2 / USABLE |
| DOC-004 | PDF p. 3 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 3 / USABLE |
| DOC-004 | PDF p. 4 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 4 / USABLE |
| DOC-004 | PDF p. 5 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 5 / USABLE |
| DOC-004 | PDF p. 6 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 6 / USABLE |
| DOC-004 | PDF p. 7 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 7 / USABLE |
| DOC-004 | PDF p. 8 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 8 / USABLE |
| DOC-004 | PDF p. 9 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 9 / USABLE |
| DOC-004 | PDF p. 10 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 10 / USABLE |
| DOC-004 | PDF p. 11 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 11 / USABLE |
| DOC-004 | PDF p. 12 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 12 / USABLE |
| DOC-004 | PDF p. 13 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 13 / USABLE |
| DOC-004 | PDF p. 14 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 14 / USABLE |
| DOC-004 | PDF p. 15 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 15 / USABLE |
| DOC-004 | PDF p. 16 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 16 / USABLE |
| DOC-004 | PDF p. 17 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 17 / USABLE |
| DOC-004 | PDF p. 18 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 18 / USABLE |
| DOC-004 | PDF p. 19 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 19 / USABLE |
| DOC-004 | PDF p. 20 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 20 / USABLE |
| DOC-004 | PDF p. 21 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 21 / USABLE |
| DOC-004 | PDF p. 22 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 22 / USABLE |
| DOC-004 | PDF p. 23 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 23 / USABLE |
| DOC-004 | PDF p. 24 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 24 / USABLE |
| DOC-004 | PDF p. 25 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-layout.txt | Form-feed page 25 / USABLE |
| DOC-005 | PDF p. 1 | .ai_paper_validation/review_1_6_1/preprocessing/recheck/data-sharing-layout.txt | Form-feed page 1 / USABLE |

## Completeness and Limitations

96 pre-existing files are inventoried: 70 USABLE, 18 PARTIAL, 7 DUPLICATE and 1 STALE. This includes 4 preserved historical scripts as non-reused tooling entries. 82 selected extraction/image/metadata records are hashed for integrity. All 102 source pages have reusable coverage; fresh-required units are zero. Historical selected-page manifests and document records are partial metadata, never scientific coverage boundaries. The stale asset-path map contains unavailable target paths, but current complete layouts and actual images close every source-unit gap. No new OCR, rendering or Office conversion occurred. Candidate discovery remains wholly downstream.

Before-integrity commands: `sha256sum -- SOURCE`; `sha256sum -- SELECTED_ASSET`. All hash lines use package-relative paths. Every exact source page remains the authoritative evidence for later candidate rechecks.

## New checker derivatives

These are current-run derivatives, separate from the unchanged reused-artifact hash set. Every item uses direct Poppler 26.01.0 on CPU. Numeric command details are in relationships/numeric_relationship_inventory.md, New derivative command register. Cross-source text uses pdftotext -layout on the complete named source; no OCR or conversion is used.

| Current-run derivative | Engine | Exact source scope |
|---|---|---|
| preprocessing/numeric_review/main-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-001 pp. 1-11 |
| preprocessing/numeric_review/protocol-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-002 pp. 1-60 |
| preprocessing/numeric_review/sap-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-003 pp. 1-5 |
| preprocessing/numeric_review/report-support-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-004 pp. 1-25 |
| preprocessing/numeric_review/main-p4.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-001 p. 4 |
| preprocessing/numeric_review/protocol-p23.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 23 |
| preprocessing/numeric_review/support-p4.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 4 |
| preprocessing/cross_source_review/main-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-001 pp. 1-11 |
| preprocessing/cross_source_review/protocol-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-002 pp. 1-60 |
| preprocessing/cross_source_review/sap-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-003 pp. 1-5 |
| preprocessing/cross_source_review/support-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-004 pp. 1-25 |

Statistical pass 1 current-source confirmations use the following derivatives. Source scopes are recorded in statistics/relationship_inventory.md; layout commands use pdftotext -layout -f FIRST -l LAST, native commands omit -layout, and the p.19 image uses pdftoppm at 110 dpi. All run directly on CPU with Poppler 26.01.0.

| Current-run derivative | Engine | Exact source scope |
|---|---|---|
| preprocessing/statistics_pass_1/main-methods-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-001 p. 4 |
| preprocessing/statistics_pass_1/main-results-native.txt | pdftotext native, Poppler 26.01.0, CPU | DOC-001 pp. 5-6 |
| preprocessing/statistics_pass_1/main-secondary-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-001 p. 8 |
| preprocessing/statistics_pass_1/sap-methods-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-003 pp. 2-5 |
| preprocessing/statistics_pass_1/protocol-summary-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-002 pp. 8-9 |
| preprocessing/statistics_pass_1/protocol-power-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-002 pp. 16-17 |
| preprocessing/statistics_pass_1/protocol-outcomes-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-002 p. 28 |
| preprocessing/statistics_pass_1/protocol-diagnostic-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-002 pp. 33-34 |
| preprocessing/statistics_pass_1/protocol-analysis-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-002 pp. 43-44 |
| preprocessing/statistics_pass_1/cace-method-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-004 pp. 14-15 |
| preprocessing/statistics_pass_1/inference-tables-layout.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-004 pp. 18-22 |
| preprocessing/statistics_pass_1/supp3-page19.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 19 |

## Independent screening derivatives

All items below were produced and visually read by the initial screener, using direct Poppler 26.01.0 on CPU. Layout text uses pdftotext -layout on every source page; images use pdftoppm -f N -l N -r 100 -singlefile -png. These current-source images can be reused by later stages without new rendering.

| Current-run derivative | Engine | Exact source scope |
|---|---|---|
| preprocessing/initial_screen/main-p1.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-001 p. 1 |
| preprocessing/initial_screen/main-p2.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-001 p. 2 |
| preprocessing/initial_screen/main-p3.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-001 p. 3 |
| preprocessing/initial_screen/main-p4.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-001 p. 4 |
| preprocessing/initial_screen/main-p6.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-001 p. 6 |
| preprocessing/initial_screen/main-p7.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-001 p. 7 |
| preprocessing/initial_screen/main-p8.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-001 p. 8 |
| preprocessing/initial_screen/protocol-p8.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 8 |
| preprocessing/initial_screen/protocol-p9.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 9 |
| preprocessing/initial_screen/protocol-p16.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 16 |
| preprocessing/initial_screen/protocol-p17.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 17 |
| preprocessing/initial_screen/protocol-p18.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 18 |
| preprocessing/initial_screen/protocol-p20.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 20 |
| preprocessing/initial_screen/protocol-p23.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 23 |
| preprocessing/initial_screen/protocol-p28.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 28 |
| preprocessing/initial_screen/protocol-p33.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 33 |
| preprocessing/initial_screen/protocol-p34.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 34 |
| preprocessing/initial_screen/protocol-p43.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 43 |
| preprocessing/initial_screen/protocol-p44.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-002 p. 44 |
| preprocessing/initial_screen/sap-p2.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-003 p. 2 |
| preprocessing/initial_screen/sap-p3.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-003 p. 3 |
| preprocessing/initial_screen/sap-p4.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-003 p. 4 |
| preprocessing/initial_screen/sap-p5.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-003 p. 5 |
| preprocessing/initial_screen/support-p3.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 3 |
| preprocessing/initial_screen/support-p4.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 4 |
| preprocessing/initial_screen/support-p15.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 15 |
| preprocessing/initial_screen/support-p16.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 16 |
| preprocessing/initial_screen/support-p18.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 18 |
| preprocessing/initial_screen/support-p19.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 19 |
| preprocessing/initial_screen/support-p20.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 20 |
| preprocessing/initial_screen/support-p21.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 21 |
| preprocessing/initial_screen/support-p22.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 22 |
| preprocessing/initial_screen/main.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-001 pp. 1-11 |
| preprocessing/initial_screen/protocol.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-002 pp. 1-60 |
| preprocessing/initial_screen/sap.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-003 pp. 1-5 |
| preprocessing/initial_screen/support.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-004 pp. 1-25 |
| preprocessing/initial_screen/sharing.txt | pdftotext -layout, Poppler 26.01.0, CPU | DOC-005 pp. 1 |

## Additional evidence-recheck derivatives

Direct source confirmations use pdftoppm -f N -l N -r 100 -singlefile -png, Poppler 26.01.0 on CPU. Source hashes were checked before visually reading these pages. Full scope is recorded in verification/evidence_recheck.md.

| Current-run derivative | Engine | Exact source scope |
|---|---|---|
| preprocessing/evidence_recheck/support-p14.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 14 |
| preprocessing/evidence_recheck/support-p17.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 17 |
| preprocessing/evidence_recheck/main-p9.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-001 p. 9 |
| preprocessing/evidence_recheck/sharing-p1.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-005 p. 1 |

## Additional quality-audit derivatives

Direct source confirmations use pdftoppm, Poppler 26.01.0, CPU, 100 dpi. No OCR was required.

| Current-run derivative | Engine | Exact source scope |
|---|---|---|
| preprocessing/quality_audit/support-p12.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 12 |
| preprocessing/quality_audit/support-p23.png | pdftoppm PNG, Poppler 26.01.0, CPU | DOC-004 p. 23 |
