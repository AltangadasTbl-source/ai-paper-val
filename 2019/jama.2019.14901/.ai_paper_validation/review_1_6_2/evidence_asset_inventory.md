# Workflow 1.6.2 Evidence Asset Inventory

All reusable asset locations below the existing audit area were inventoried without reading old candidate, checker, screening, verifier, critic, endetail, or final-report conclusions. Every reused asset has a package-relative SHA-256 record in reused_artifact_hashes_before.sha256. Source-linked native/layout text, OCR, images and provenance metadata are reusable; legacy scientific selection and scope exclusions are not adopted. No reusable artifact is modified.

Fitness: USABLE means usable for the exact stated location; PARTIAL means incomplete content or metadata; DUPLICATE means an additional overlapping derivative without unique page coverage. There are no STALE or UNREADABLE primary reuse assets. Overlapping derivatives never increase unique unit counts. Source hashes match the prior package manifest for all four documents. Per-page direct pdftotext -layout output matches every main, protocol and results native-text asset after whitespace normalization. DOC-004 text was checked against its single direct source page. PDF pp. 42 protocol and 9 results include images for which native text alone is incomplete; the existing rendered images cover their full source pages.

Engines and commands: pdfinfo source.pdf for source metadata; sha256sum -- source.pdf for identity; pdftotext -layout -f N -l N source.pdf - for source/text matching. Native assets named native_text are actually layout-preserving Poppler extraction, confirmed against direct output. Legacy document_outputs OCR uses rapidocr_onnxruntime CPU with onnxruntime 1.28.0, documented in ocr_backend.json; review_1_6_1 protocol p.42 OCR is Tesseract-style CPU text, with legacy engine version unrecorded. Rendered images are legacy source-page rasters; exact render engine/version is unrecorded. This provenance limitation does not limit mapping because sources remain available for exact confirmation. No rendering, OCR, extraction file, or Office conversion was newly produced by the curator.

The complete per-file table below records exact pages/ranges. Metadata scopes refer to the linked page set, not to inherited scientific audit boundaries. DUPLICATE rows are retained and hashed as optional corroborating locators. OCR remains a transcription aid; source pages govern every eventual evidence recheck.

| Asset path | Source ID | Exact source units | Kind / engine | Fitness | Reuse action |
|---|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001-main-article/document_record.json | DOC-001 | PDF pp. 1-11 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-001.txt | DOC-001 | PDF p. 1 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-002.txt | DOC-001 | PDF p. 2 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-003.txt | DOC-001 | PDF p. 3 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-004.txt | DOC-001 | PDF p. 4 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-005.txt | DOC-001 | PDF p. 5 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-006.txt | DOC-001 | PDF p. 6 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-007.txt | DOC-001 | PDF p. 7 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-008.txt | DOC-001 | PDF p. 8 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-009.txt | DOC-001 | PDF p. 9 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/ocr_text/page-003.txt | DOC-001 | PDF p. 3 | OCR text; legacy CPU | PARTIAL | Reuse locator; image/source governs transcription |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/page_manifest.json | DOC-001 | PDF pp. 1-9 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/page_ocr_metadata/page-003.json | DOC-001 | PDF p. 3 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-003-03.png | DOC-001 | PDF p. 3 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-005-05.png | DOC-001 | PDF p. 5 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-006-06.png | DOC-001 | PDF p. 6 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-007-07.png | DOC-001 | PDF p. 7 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-008-08.png | DOC-001 | PDF p. 8 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-002-protocol/document_record.json | DOC-002 | PDF pp. 1-48 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/document_record.json | DOC-003 | PDF pp. 1-9 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-001.txt | DOC-003 | PDF p. 1 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-002.txt | DOC-003 | PDF p. 2 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-003.txt | DOC-003 | PDF p. 3 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-004.txt | DOC-003 | PDF p. 4 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-005.txt | DOC-003 | PDF p. 5 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-006.txt | DOC-003 | PDF p. 6 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-007.txt | DOC-003 | PDF p. 7 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-008.txt | DOC-003 | PDF p. 8 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-009.txt | DOC-003 | PDF p. 9 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-002.txt | DOC-003 | PDF p. 2 | OCR text; legacy CPU | PARTIAL | Reuse locator; image/source governs transcription |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-003.txt | DOC-003 | PDF p. 3 | OCR text; legacy CPU | PARTIAL | Reuse locator; image/source governs transcription |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-004.txt | DOC-003 | PDF p. 4 | OCR text; legacy CPU | PARTIAL | Reuse locator; image/source governs transcription |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-005.txt | DOC-003 | PDF p. 5 | OCR text; legacy CPU | PARTIAL | Reuse locator; image/source governs transcription |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-006.txt | DOC-003 | PDF p. 6 | OCR text; legacy CPU | PARTIAL | Reuse locator; image/source governs transcription |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-007.txt | DOC-003 | PDF p. 7 | OCR text; legacy CPU | PARTIAL | Reuse locator; image/source governs transcription |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-008.txt | DOC-003 | PDF p. 8 | OCR text; legacy CPU | PARTIAL | Reuse locator; image/source governs transcription |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-009.txt | DOC-003 | PDF p. 9 | OCR text; legacy CPU | PARTIAL | Reuse locator; image/source governs transcription |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_manifest.json | DOC-003 | PDF pp. 1-9 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-002.json | DOC-003 | PDF p. 2 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-003.json | DOC-003 | PDF p. 3 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-004.json | DOC-003 | PDF p. 4 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-005.json | DOC-003 | PDF p. 5 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-006.json | DOC-003 | PDF p. 6 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-007.json | DOC-003 | PDF p. 7 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-008.json | DOC-003 | PDF p. 8 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-009.json | DOC-003 | PDF p. 9 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-002-2.png | DOC-003 | PDF p. 2 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-003-3.png | DOC-003 | PDF p. 3 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-004-4.png | DOC-003 | PDF p. 4 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-005-5.png | DOC-003 | PDF p. 5 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-006-6.png | DOC-003 | PDF p. 6 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-007-7.png | DOC-003 | PDF p. 7 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-008-8.png | DOC-003 | PDF p. 8 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-009-9.png | DOC-003 | PDF p. 9 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/results_evidence_map.json | DOC-003 | PDF pp. 1-9 | Source-location/table map | PARTIAL | Reuse reported-data locations only; reconstruct all relationships anew |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/results_evidence_map.md | DOC-003 | PDF pp. 1-9 | Source-location/table map | PARTIAL | Reuse reported-data locations only; reconstruct all relationships anew |
| .ai_paper_validation/document_outputs/DOC-004-data-sharing-statement/document_record.json | DOC-004 | PDF p. 1 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/document_outputs/package_manifest.json | DOC-001, DOC-002, DOC-003, DOC-004 | Identity: 11, 48, 9, 1 PDF pages | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/preprocessing/ocr_backend.json | DOC-001, DOC-003 | DOC-001 pp. 3, 5-8; DOC-003 pp. 2-9 | Identity/coverage/engine metadata | PARTIAL | Reuse identity/provenance only; ignore legacy scope exclusions |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/main_p1-8_layout.txt | DOC-001 | PDF pp. 1-8 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/main_p1.png | DOC-001 | PDF pp. 1 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/main_p4.png | DOC-001 | PDF pp. 4 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/main_p6.png | DOC-001 | PDF pp. 6 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/main_p7.png | DOC-001 | PDF pp. 7 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/main_p8.png | DOC-001 | PDF pp. 8 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/protocol_p11.png | DOC-002 | PDF pp. 11 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/protocol_p11_layout.txt | DOC-002 | PDF pp. 11 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/protocol_p30-31_layout.txt | DOC-002 | PDF pp. 30-31 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/protocol_p30.png | DOC-002 | PDF pp. 30 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/protocol_p31.png | DOC-002 | PDF pp. 31 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/protocol_p31_layout.txt | DOC-002 | PDF pp. 31 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/protocol_p32.png | DOC-002 | PDF pp. 32 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/protocol_p32_layout.txt | DOC-002 | PDF pp. 32 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/results_p4-7_layout.txt | DOC-003 | PDF pp. 4-7 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/results_p4.png | DOC-003 | PDF pp. 4 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck/results_p7.png | DOC-003 | PDF pp. 7 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-001-main-article_page-010.txt | DOC-001 | PDF p. 10 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-001-main-article_page-011.txt | DOC-001 | PDF p. 11 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-001.txt | DOC-002 | PDF p. 1 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-002.txt | DOC-002 | PDF p. 2 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-003.txt | DOC-002 | PDF p. 3 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-004.txt | DOC-002 | PDF p. 4 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-005.txt | DOC-002 | PDF p. 5 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-006.txt | DOC-002 | PDF p. 6 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-007.txt | DOC-002 | PDF p. 7 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-008.txt | DOC-002 | PDF p. 8 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-009.txt | DOC-002 | PDF p. 9 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-010.txt | DOC-002 | PDF p. 10 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-011.txt | DOC-002 | PDF p. 11 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-012.txt | DOC-002 | PDF p. 12 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-013.txt | DOC-002 | PDF p. 13 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-014.txt | DOC-002 | PDF p. 14 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-015.txt | DOC-002 | PDF p. 15 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-016.txt | DOC-002 | PDF p. 16 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-017.txt | DOC-002 | PDF p. 17 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-018.txt | DOC-002 | PDF p. 18 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-019.txt | DOC-002 | PDF p. 19 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-020.txt | DOC-002 | PDF p. 20 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-021.txt | DOC-002 | PDF p. 21 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-022.txt | DOC-002 | PDF p. 22 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-023.txt | DOC-002 | PDF p. 23 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-024.txt | DOC-002 | PDF p. 24 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-025.txt | DOC-002 | PDF p. 25 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-026.txt | DOC-002 | PDF p. 26 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-027.txt | DOC-002 | PDF p. 27 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-028.txt | DOC-002 | PDF p. 28 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-029.txt | DOC-002 | PDF p. 29 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-030.txt | DOC-002 | PDF p. 30 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-031.txt | DOC-002 | PDF p. 31 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-032.txt | DOC-002 | PDF p. 32 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-033.txt | DOC-002 | PDF p. 33 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-034.txt | DOC-002 | PDF p. 34 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-035.txt | DOC-002 | PDF p. 35 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-036.txt | DOC-002 | PDF p. 36 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-037.txt | DOC-002 | PDF p. 37 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-038.txt | DOC-002 | PDF p. 38 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-039.txt | DOC-002 | PDF p. 39 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-040.txt | DOC-002 | PDF p. 40 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-041.txt | DOC-002 | PDF p. 41 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-042.txt | DOC-002 | PDF p. 42 | Native/layout text; Poppler verified | PARTIAL | Header/footer only; pair with p.42 image/OCR |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-043.txt | DOC-002 | PDF p. 43 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-044.txt | DOC-002 | PDF p. 44 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-045.txt | DOC-002 | PDF p. 45 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-046.txt | DOC-002 | PDF p. 46 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-047.txt | DOC-002 | PDF p. 47 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-048.txt | DOC-002 | PDF p. 48 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-004-data-sharing-statement_page-001.txt | DOC-004 | PDF p. 1 | Native/layout text; Poppler verified | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_source/main-p1.png | DOC-001 | PDF pp. 1 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_source/main-p4.png | DOC-001 | PDF pp. 4 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_source/main-p6.png | DOC-001 | PDF pp. 6 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_source/main-p8.png | DOC-001 | PDF pp. 8 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_source/protocol-p31.png | DOC-002 | PDF pp. 31 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_source/protocol-p33.png | DOC-002 | PDF pp. 33 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_source/protocol-p34.png | DOC-002 | PDF pp. 34 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/cross_source/results-p2.png | DOC-003 | PDF pp. 2 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck/data-sharing-p1-layout.txt | DOC-004 | PDF pp. 1 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck/main-all-layout.txt | DOC-001 | PDF pp. 1-11 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck/main-p7.png | DOC-001 | PDF pp. 7 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck/protocol-p30-p34-layout.txt | DOC-002 | PDF pp. 30-34 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck/protocol-p30.png | DOC-002 | PDF pp. 30 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck/results-all-layout.txt | DOC-003 | PDF pp. 1-9 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck/results-p6.png | DOC-003 | PDF pp. 6 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck/results-p9.png | DOC-003 | PDF pp. 9 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/statistics_pass1/main-p01.txt | DOC-001 | PDF pp. 1 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_6_1/preprocessing/statistics_pass1/main-p04.txt | DOC-001 | PDF pp. 4 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_6_1/preprocessing/statistics_pass1/plan-p33-p34.txt | DOC-002 | PDF pp. 33-34 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_6_1/preprocessing/statistics_pass1/results-p02.txt | DOC-003 | PDF pp. 2 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_6_1/preprocessing/statistics_pass1/results-p06-p07.txt | DOC-003 | PDF pp. 6-7 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_6_1/preprocessing/statistics_pass1/results-p07.png | DOC-003 | PDF pp. 7 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |
| .ai_paper_validation/review_1_6_1/preprocessing/support/protocol-p42-layout.txt | DOC-002 | PDF pp. 42 | Native/layout text; legacy direct extraction | DUPLICATE | Optional overlapping page locator |
| .ai_paper_validation/review_1_6_1/preprocessing/support/protocol-p42-ocr.txt | DOC-002 | PDF pp. 42 | OCR text; legacy CPU | PARTIAL | Reuse locator; image/source governs transcription |
| .ai_paper_validation/review_1_6_1/preprocessing/support/protocol-p42.png | DOC-002 | PDF pp. 42 | Rendered source page; legacy raster | USABLE | Reuse source-linked locator |

Additional location-map asset inventoried, not reused: .ai_paper_validation/document_outputs/DOC-001-main-article/main_article_results_evidence.md — DOC-001 PDF pp. 1-9, PARTIAL legacy selected-results map. Primary page text and rasters supply the full scope; the selected map is not a discovery boundary or scientific comparator. Restriction records are administrative records rather than extraction assets and are not reused. No table/workbook extraction, CSV record extraction, or Office paragraph/cell map exists beyond the listed reported-result maps.

Exact mandatory downstream assignments: main mapper DOC-001 PDF pp. 1-11; support mapper DOC-002 pp. 1-48, DOC-003 pp. 1-9, DOC-004 p. 1. No uncovered unit remains in the reusable coverage partition. Protocol p.42 OCR should be read beside its full raster; no OCR-only interpretation is required. The coverage ledger remains PENDING_MAPPING until scientific page mapping is complete.

Curation completion: 153 eligible evidence assets inventoried, 152 included in the reusable hash set and one legacy selected-results map inventoried without reuse. All four source hashes and all 152 reusable asset hashes verify against their before files. The protocol p.42 raster was visually inspected and is legible across the complete source page; its OCR includes symbol/character transcription limitations and must be paired with the raster. Fresh-required unit count: 0. Every unit remains assigned to downstream scientific mapping.

## New direct-source derivatives produced during checking

These derivatives are new run artifacts, not reused assets; their source hashes are in source_hashes_before.sha256. Engine: direct Poppler pdftoppm 26.01.0, CPU, single-page PNG scaled to 1800 pixels. Exact commands are recorded in checkers/numeric_consistency.md.

| Asset path | Source ID | Exact source units | Kind / engine | Fitness | Reuse action |
|---|---|---|---|---|---|
| .ai_paper_validation/review_1_6_2/preprocessing/numeric-results-p4.png | DOC-003 | PDF p. 4 | New render; Poppler 26.01.0 CPU | USABLE | Direct visual confirmation of eTable 2 cells |
| .ai_paper_validation/review_1_6_2/preprocessing/numeric-results-p7.png | DOC-003 | PDF p. 7 | New render; Poppler 26.01.0 CPU | USABLE | Direct visual confirmation of eTable 4 values |

## New direct-source evidence-recheck derivatives

The mechanical rechecker created 13 additional run-local derivatives with direct Poppler 26.01.0 CPU tooling. All exact source units, paths, commands, DPI and layout parameters are listed in verification/evidence_recheck.md, Derivative provenance and limitations. That complete provenance table is incorporated as the derivative registry; every source location remains linked to the supplied PDF. These files are new run artifacts and are excluded from the reused-artifact hash inventory. No OCR or conversion was performed.
