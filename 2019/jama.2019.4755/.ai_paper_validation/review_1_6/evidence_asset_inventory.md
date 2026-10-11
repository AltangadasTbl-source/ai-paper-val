# Reusable Evidence-Asset Inventory

Curation COMPLETE. Every existing extraction, rendered page, OCR metadata, page manifest, document record, and source-location map was discovered by filename before content inspection. Every eligible path is listed separately below and hashed in reused_artifact_hashes_before.sha256. Scripts and AI-training restriction records are not evidence assets and were not used. No old candidate, checker, review queue, critic, classification, or final-report content was read. Source-linked evidence maps are transcription/locator aids only; older exclusions in their metadata are ignored.

Source hashes match the existing package manifest. The four complete prior support layout files were compared byte-for-byte with direct pdftotext -layout output for their exact page scopes and match. Protocol text has embedded-font corruption and one empty page; its fresh-required list is in source_coverage.md. All remaining required units have native/layout text, confirmed against source page count, native/bbox metadata, and direct title inspection. Images are valid PNGs according to file; images and OCR are locators/transcription aids rather than final authority.

Preferred mapper paths:

- Main DOC-001 pp. 1-7: .ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-N.txt, .ai_paper_validation/preprocessing/native_bbox_main_N.html; source-linked renders under .ai_paper_validation/document_outputs/D01/ocr_pages/ for pp. 1-5 and 7.
- Support A DOC-002 pp. 1-32: .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-002_pp1-62_layout.txt; page boundaries are form feeds. Fresh-required pp. 1, 6, 7, 8, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 26, 30, 31, 32.
- Support A DOC-003 pp. 1-10: .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-003_pp1-10_layout.txt; optional exact p6/p8 layout and PNGs under .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/.
- Support B DOC-002 pp. 33-62: same protocol layout; fresh-required pp. 34, 35, 37, 38, 40, 41, 44, 49, 51, 52, 53, 54, 56, 57, 58, 61, 62.
- Support B DOC-004 pp. 1-3: .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-004_pp1-3_layout.txt; pp. 4-8: .ai_paper_validation/document_outputs/doc-b45e07a04d82/normalized_pages/page-N.txt and .ai_paper_validation/preprocessing/native_bbox_supp_N.html; corresponding PNGs under .ai_paper_validation/document_outputs/D04/ocr_pages/ or the hash-ID directory.
- Support B DOC-005 p1: .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-005_p1_layout.txt.

Historical engines: native/layout/bbox = Poppler pdftotext (historical exact version unrecorded); rendered PNG = Poppler pdftoppm/pdftocairo (historical exact version unrecorded); OCR = rapidocr_onnxruntime CPU as documented in .ocr.json and ocr_backend.json; source maps/manifests = prior local evidence mapping/inventory. Current identity/fitness checks: sha256sum, pdfinfo, pdftotext 26.01.0, file, awk, cmp. No new derivatives were produced by curation. Historical backend metadata was read; no GPU probe or invocation occurred.

USABLE means a source-linked derivative is readable and appropriate for its exact listed scope. PARTIAL means incomplete source coverage, encoding corruption, or identity-only metadata with obsolete scope controls. DUPLICATE means its bytes match an earlier inventoried eligible path, with no additional source-unit credit. STALE and UNREADABLE were not needed for any asset. Full coverage counts are unique page units, never derivative-file counts.

| Asset ID | Existing package-relative path | Source units | Type and engine | Fitness | Use and limitation |
|---|---|---|---|---|---|
| A001 | .ai_paper_validation/document_outputs/D01/native_pages/page-1.txt | DOC-001 p. 1 | Native text / Poppler | USABLE | Source-linked main-report derivative |
| A002 | .ai_paper_validation/document_outputs/D01/native_pages/page-2.txt | DOC-001 p. 2 | Native text / Poppler | USABLE | Source-linked main-report derivative |
| A003 | .ai_paper_validation/document_outputs/D01/native_pages/page-3.txt | DOC-001 p. 3 | Native text / Poppler | USABLE | Source-linked main-report derivative |
| A004 | .ai_paper_validation/document_outputs/D01/native_pages/page-4.txt | DOC-001 p. 4 | Native text / Poppler | USABLE | Source-linked main-report derivative |
| A005 | .ai_paper_validation/document_outputs/D01/native_pages/page-5.txt | DOC-001 p. 5 | Native text / Poppler | USABLE | Source-linked main-report derivative |
| A006 | .ai_paper_validation/document_outputs/D01/native_pages/page-6.txt | DOC-001 p. 6 | Native text / Poppler | USABLE | Source-linked main-report derivative |
| A007 | .ai_paper_validation/document_outputs/D01/native_pages/page-7.txt | DOC-001 p. 7 | Native text / Poppler | USABLE | Source-linked main-report derivative |
| A008 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-1.ocr.json | DOC-001 p. 1 | OCR metadata / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A009 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-1.png | DOC-001 p. 1 | Rendered PNG / Poppler | USABLE | Source-linked main-report derivative |
| A010 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-1.txt | DOC-001 p. 1 | OCR text / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A011 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-2.ocr.json | DOC-001 p. 2 | OCR metadata / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A012 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-2.png | DOC-001 p. 2 | Rendered PNG / Poppler | USABLE | Source-linked main-report derivative |
| A013 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-2.txt | DOC-001 p. 2 | OCR text / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A014 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-3.ocr.json | DOC-001 p. 3 | OCR metadata / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A015 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-3.png | DOC-001 p. 3 | Rendered PNG / Poppler | USABLE | Source-linked main-report derivative |
| A016 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-3.txt | DOC-001 p. 3 | OCR text / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A017 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-4.ocr.json | DOC-001 p. 4 | OCR metadata / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A018 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-4.png | DOC-001 p. 4 | Rendered PNG / Poppler | USABLE | Source-linked main-report derivative |
| A019 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-4.txt | DOC-001 p. 4 | OCR text / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A020 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-5.ocr.json | DOC-001 p. 5 | OCR metadata / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A021 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-5.png | DOC-001 p. 5 | Rendered PNG / Poppler | USABLE | Source-linked main-report derivative |
| A022 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-5.txt | DOC-001 p. 5 | OCR text / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A023 | .ai_paper_validation/document_outputs/D01/ocr_pages/page-7.png | DOC-001 p. 7 | Rendered PNG / Poppler | USABLE | Source-linked main-report derivative |
| A024 | .ai_paper_validation/document_outputs/D04/native_pages/page-4.txt | DOC-004 p. 4 | Native text / Poppler | USABLE | Source-linked results-supplement derivative |
| A025 | .ai_paper_validation/document_outputs/D04/native_pages/page-5.txt | DOC-004 p. 5 | Native text / Poppler | USABLE | Source-linked results-supplement derivative |
| A026 | .ai_paper_validation/document_outputs/D04/native_pages/page-6.txt | DOC-004 p. 6 | Native text / Poppler | USABLE | Source-linked results-supplement derivative |
| A027 | .ai_paper_validation/document_outputs/D04/native_pages/page-7.txt | DOC-004 p. 7 | Native text / Poppler | USABLE | Source-linked results-supplement derivative |
| A028 | .ai_paper_validation/document_outputs/D04/native_pages/page-8.txt | DOC-004 p. 8 | Native text / Poppler | USABLE | Source-linked results-supplement derivative |
| A029 | .ai_paper_validation/document_outputs/D04/ocr_pages/page-4.ocr.json | DOC-004 p. 4 | OCR metadata / RapidOCR CPU | USABLE | Source-linked results-supplement derivative |
| A030 | .ai_paper_validation/document_outputs/D04/ocr_pages/page-4.png | DOC-004 p. 4 | Rendered PNG / Poppler | USABLE | Source-linked results-supplement derivative |
| A031 | .ai_paper_validation/document_outputs/D04/ocr_pages/page-4.txt | DOC-004 p. 4 | OCR text / RapidOCR CPU | USABLE | Source-linked results-supplement derivative |
| A032 | .ai_paper_validation/document_outputs/D04/ocr_pages/page-5.png | DOC-004 p. 5 | Rendered PNG / Poppler | USABLE | Source-linked results-supplement derivative |
| A033 | .ai_paper_validation/document_outputs/D04/ocr_pages/page-6.png | DOC-004 p. 6 | Rendered PNG / Poppler | USABLE | Source-linked results-supplement derivative |
| A034 | .ai_paper_validation/document_outputs/D04/ocr_pages/page-7.png | DOC-004 p. 7 | Rendered PNG / Poppler | USABLE | Source-linked results-supplement derivative |
| A035 | .ai_paper_validation/document_outputs/D04/ocr_pages/page-8.png | DOC-004 p. 8 | Rendered PNG / Poppler | USABLE | Source-linked results-supplement derivative |
| A036 | .ai_paper_validation/document_outputs/doc-5143f7e4da1a/document_record.json | DOC-002 pp. 1-62 | Source-linked metadata | PARTIAL | Source-linked identity/transcription map; old exclusions ignored; no scientific dispositions reused |
| A037 | .ai_paper_validation/document_outputs/doc-5704a644014e/document_record.json | DOC-003 pp. 1-10 | Source-linked metadata | PARTIAL | Source-linked identity/transcription map; old exclusions ignored; no scientific dispositions reused |
| A038 | .ai_paper_validation/document_outputs/doc-799606a72443/document_record.json | DOC-001 pp. 1-7 | Source-linked metadata | PARTIAL | Source-linked identity/transcription map; old exclusions ignored; no scientific dispositions reused |
| A039 | .ai_paper_validation/document_outputs/doc-799606a72443/main_article_evidence_inventory.json | DOC-001 pp. 1-7 | Source-linked metadata | PARTIAL | Source-linked identity/transcription map; old exclusions ignored; no scientific dispositions reused |
| A040 | .ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-1.txt | DOC-001 p. 1 | Layout text / Poppler | USABLE | Source-linked main-report derivative |
| A041 | .ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-2.txt | DOC-001 p. 2 | Layout text / Poppler | USABLE | Source-linked main-report derivative |
| A042 | .ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-3.txt | DOC-001 p. 3 | Layout text / Poppler | USABLE | Source-linked main-report derivative |
| A043 | .ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-4.txt | DOC-001 p. 4 | Layout text / Poppler | USABLE | Source-linked main-report derivative |
| A044 | .ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-5.txt | DOC-001 p. 5 | Layout text / Poppler | USABLE | Source-linked main-report derivative |
| A045 | .ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-6.txt | DOC-001 p. 6 | Layout text / Poppler | USABLE | Source-linked main-report derivative |
| A046 | .ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-7.txt | DOC-001 p. 7 | Layout text / Poppler | USABLE | Source-linked main-report derivative |
| A047 | .ai_paper_validation/document_outputs/doc-799606a72443/ocr_pages/page-4.png | DOC-001 p. 4 | Rendered PNG / Poppler | USABLE | Source-linked main-report derivative |
| A048 | .ai_paper_validation/document_outputs/doc-799606a72443/ocr_pages/page-5.ocr.json | DOC-001 p. 5 | OCR metadata / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A049 | .ai_paper_validation/document_outputs/doc-799606a72443/ocr_pages/page-5.png | DOC-001 p. 5 | Rendered PNG / Poppler | USABLE | Source-linked main-report derivative |
| A050 | .ai_paper_validation/document_outputs/doc-799606a72443/ocr_pages/page-5.txt | DOC-001 p. 5 | OCR text / RapidOCR CPU | USABLE | Source-linked main-report derivative |
| A051 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/document_record.json | DOC-004 pp. 1-8 | Source-linked metadata | PARTIAL | Source-linked identity/transcription map; old exclusions ignored; no scientific dispositions reused |
| A052 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/normalized_pages/page-4.txt | DOC-004 p. 4 | Layout text / Poppler | USABLE | Source-linked results-supplement derivative |
| A053 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/normalized_pages/page-5.txt | DOC-004 p. 5 | Layout text / Poppler | USABLE | Source-linked results-supplement derivative |
| A054 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/normalized_pages/page-6.txt | DOC-004 p. 6 | Layout text / Poppler | USABLE | Source-linked results-supplement derivative |
| A055 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/normalized_pages/page-7.txt | DOC-004 p. 7 | Layout text / Poppler | USABLE | Source-linked results-supplement derivative |
| A056 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/normalized_pages/page-8.txt | DOC-004 p. 8 | Layout text / Poppler | USABLE | Source-linked results-supplement derivative |
| A057 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-4.ocr.json | DOC-004 p. 4 | OCR metadata / RapidOCR CPU | USABLE | Source-linked results-supplement derivative |
| A058 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-4.png | DOC-004 p. 4 | Rendered PNG / Poppler | USABLE | Source-linked results-supplement derivative |
| A059 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-4.txt | DOC-004 p. 4 | OCR text / RapidOCR CPU | USABLE | Source-linked results-supplement derivative |
| A060 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-5.ocr.json | DOC-004 p. 5 | OCR metadata / RapidOCR CPU | USABLE | Source-linked results-supplement derivative |
| A061 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-5.png | DOC-004 p. 5 | Rendered PNG / Poppler | USABLE | Source-linked results-supplement derivative |
| A062 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-5.txt | DOC-004 p. 5 | OCR text / RapidOCR CPU | USABLE | Source-linked results-supplement derivative |
| A063 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-6.ocr.json | DOC-004 p. 6 | OCR metadata / RapidOCR CPU | USABLE | Source-linked results-supplement derivative |
| A064 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-6.png | DOC-004 p. 6 | Rendered PNG / Poppler | USABLE | Source-linked results-supplement derivative |
| A065 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-6.txt | DOC-004 p. 6 | OCR text / RapidOCR CPU | USABLE | Source-linked results-supplement derivative |
| A066 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-7.ocr.json | DOC-004 p. 7 | OCR metadata / RapidOCR CPU | USABLE | Source-linked results-supplement derivative |
| A067 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-7.png | DOC-004 p. 7 | Rendered PNG / Poppler | USABLE | Source-linked results-supplement derivative |
| A068 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-7.txt | DOC-004 p. 7 | OCR text / RapidOCR CPU | USABLE | Source-linked results-supplement derivative |
| A069 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-8.png | DOC-004 p. 8 | Rendered PNG / Poppler | USABLE | Source-linked results-supplement derivative |
| A070 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/ocr_pages/page-8.txt | DOC-004 p. 8 | OCR text / RapidOCR CPU | USABLE | Source-linked results-supplement derivative |
| A071 | .ai_paper_validation/document_outputs/doc-b45e07a04d82/results_supplement_evidence_map.json | DOC-004 pp. 4-8 | Source-linked metadata | PARTIAL | Source-linked identity/transcription map; old exclusions ignored; no scientific dispositions reused |
| A072 | .ai_paper_validation/document_outputs/doc-ded78f53da7b/document_record.json | DOC-005 p. 1 | Source-linked metadata | PARTIAL | Source-linked identity/transcription map; old exclusions ignored; no scientific dispositions reused |
| A073 | .ai_paper_validation/document_outputs/package_manifest.json | DOC-001 pp. 1-7; DOC-002 pp. 1-62; DOC-003 pp. 1-10; DOC-004 pp. 1-8; DOC-005 p. 1 | Source-linked metadata | PARTIAL | Identity/location metadata; historical scope exclusions ignored |
| A074 | .ai_paper_validation/preprocessing/native_bbox_main_1.html | DOC-001 p. 1 | Bounding-box text / Poppler | USABLE | Source-linked main-report derivative |
| A075 | .ai_paper_validation/preprocessing/native_bbox_main_2.html | DOC-001 p. 2 | Bounding-box text / Poppler | USABLE | Source-linked main-report derivative |
| A076 | .ai_paper_validation/preprocessing/native_bbox_main_3.html | DOC-001 p. 3 | Bounding-box text / Poppler | USABLE | Source-linked main-report derivative |
| A077 | .ai_paper_validation/preprocessing/native_bbox_main_4.html | DOC-001 p. 4 | Bounding-box text / Poppler | USABLE | Source-linked main-report derivative |
| A078 | .ai_paper_validation/preprocessing/native_bbox_main_5.html | DOC-001 p. 5 | Bounding-box text / Poppler | USABLE | Source-linked main-report derivative |
| A079 | .ai_paper_validation/preprocessing/native_bbox_main_6.html | DOC-001 p. 6 | Bounding-box text / Poppler | USABLE | Source-linked main-report derivative |
| A080 | .ai_paper_validation/preprocessing/native_bbox_main_7.html | DOC-001 p. 7 | Bounding-box text / Poppler | USABLE | Source-linked main-report derivative |
| A081 | .ai_paper_validation/preprocessing/native_bbox_supp_4.html | DOC-004 p. 4 | Bounding-box text / Poppler | USABLE | Source-linked results-supplement derivative |
| A082 | .ai_paper_validation/preprocessing/native_bbox_supp_5.html | DOC-004 p. 5 | Bounding-box text / Poppler | USABLE | Source-linked results-supplement derivative |
| A083 | .ai_paper_validation/preprocessing/native_bbox_supp_6.html | DOC-004 p. 6 | Bounding-box text / Poppler | USABLE | Source-linked results-supplement derivative |
| A084 | .ai_paper_validation/preprocessing/native_bbox_supp_7.html | DOC-004 p. 7 | Bounding-box text / Poppler | USABLE | Source-linked results-supplement derivative |
| A085 | .ai_paper_validation/preprocessing/native_bbox_supp_8.html | DOC-004 p. 8 | Bounding-box text / Poppler | USABLE | Source-linked results-supplement derivative |
| A086 | .ai_paper_validation/preprocessing/native_extraction_quality.json | DOC-001 pp. 1-7 and DOC-004 pp. 4-8 | Source-linked metadata | PARTIAL | Identity/location metadata; historical scope exclusions ignored |
| A087 | .ai_paper_validation/preprocessing/native_layout_quality_report.json | DOC-001 pp. 1-7 and DOC-004 pp. 4-8 | Source-linked metadata | PARTIAL | Identity/location metadata; historical scope exclusions ignored |
| A088 | .ai_paper_validation/preprocessing/ocr_backend.json | DOC-001 pp. 1-7 and DOC-004 pp. 4-8 | Source-linked metadata | PARTIAL | Identity/location metadata; historical scope exclusions ignored |
| A089 | .ai_paper_validation/preprocessing/page_manifest.json | DOC-001 pp. 1-7 and DOC-004 pp. 4-8 | Source-linked metadata | PARTIAL | Identity/location metadata; historical scope exclusions ignored |
| A090 | .ai_paper_validation/preprocessing/preprocessing_summary.json | DOC-001 pp. 1-7 and DOC-004 pp. 4-8 | Source-linked metadata | PARTIAL | Identity/location metadata; historical scope exclusions ignored |
| A091 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-001-p1-layout.txt | DOC-001 p. 1 | Layout text / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A092 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-001-p1.png | DOC-001 p. 1 | Rendered PNG / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A093 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-001-p5-layout.txt | DOC-001 p. 5 | Layout text / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A094 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-001-p5.png | DOC-001 p. 5 | Rendered PNG / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A095 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-003-p6-layout.txt | DOC-003 p. 6 | Layout text / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A096 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-003-p6.png | DOC-003 p. 6 | Rendered PNG / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A097 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-003-p8-layout.txt | DOC-003 p. 8 | Layout text / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A098 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-003-p8.png | DOC-003 p. 8 | Rendered PNG / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A099 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-004-p6.png | DOC-004 p. 6 | Rendered PNG / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A100 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-004-p7-bbox.html | DOC-004 p. 7 | Bounding-box text / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A101 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-004-p7-header-crop.png | DOC-004 p. 7 | Rendered PNG / Poppler | PARTIAL | Header crop only; full page image also available |
| A102 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-004-p7.png | DOC-004 p. 7 | Rendered PNG / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A103 | .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/DOC-004-pp6-7-layout.txt | DOC-004 pp. 6-7 | Layout text / Poppler | USABLE | Exact source-page derivative; visual confirmation aid |
| A104 | .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-002_pp1-62_layout.txt | DOC-002 pp. 1-62 | Poppler layout text | PARTIAL | 27 reusable pages; 35 fresh-required pages listed in source_coverage.md |
| A105 | .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-003_pp1-10_layout.txt | DOC-003 pp. 1-10 | Poppler layout text | USABLE | Complete ten-page source-matched layout |
| A106 | .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-004_pp1-3_layout.txt | DOC-004 pp. 1-3 | Poppler layout text | USABLE | Complete exact three-page source-matched layout |
| A107 | .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-005_p1_layout.txt | DOC-005 p. 1 | Poppler layout text | USABLE | Complete exact one-page source-matched layout |

Inventoried and integrity-hashed existing evidence assets: 107.

Fitness totals: USABLE 92; PARTIAL 15; STALE 0; DUPLICATE 0; UNREADABLE 0. No two inventoried assets had identical SHA-256 bytes; overlapping versions still cover the same unique source pages and never inflate reusable counts. Rendered pages and crop files are supplemental visual aids. No standalone workbook/table-extraction files exist; structured main/report table transcriptions occur in the two source-location maps listed above. Five ai_training_restriction_record.json files and five historical preprocessing Python scripts were discovered but excluded from scientific reuse and not hashed as evidence. There were no additional eligible OCR, extraction, page manifest, document-record, or source-location-map files in the existing audit area.

The native/layout excerpts and structured maps show sensitivity, specificity, predictive-value and corresponding diagnostic-count tables; this content supports the bounded diagnostic-performance complexity stated in the planning target. Curation does not evaluate any result or diagnose candidates.
