# Workflow 1.6.2 Reusable Evidence Asset Inventory

171 individual extraction/metadata/image assets were inventoried and SHA-256 hashed before scientific mapping in reused_artifact_hashes_before.sha256. Search covered the entire existing audit area, excluding current-run outputs. No standalone OCR, table/workbook extraction, or separate source-location map exists beyond the native/layout text, two page manifests, and three document records catalogued here. Rights records, the package manifest, and legacy scientific conclusions are preserved and are not extraction inputs.

## Fitness method and engines

All 80 primary page texts were compared with exact direct-source page extraction after removing whitespace: DOC-001 and DOC-003 match Poppler pdftotext -layout; DOC-002 matches pdftotext default. All 46 DOC-002 layout texts, full main layout, and five targeted raw layout extracts also match source extraction. Every retained PNG has a readable PNG signature and image dimensions confirmed with file. Source SHA-256 matches each legacy document record. Legacy image render engine was Poppler pdftoppm/pdftocairo; exact prior version was not recorded. Current direct confirmation engines are Poppler pdftotext/pdfinfo 26.01.0 and sha256sum uutils 0.10.0. No new render/OCR/converted derivative was produced. Compute device: CPU.

USABLE indicates a coherent source-matched extraction or source-linked retained image/map. DUPLICATE indicates redundant coverage of a primary per-page extraction or image. PARTIAL indicates metadata usable for identity/provenance but containing obsolete processing-scope statements, or source-matched caption/footer text that does not capture its page screenshot content and therefore requires fresh visual mapping. The normalized document texts are redundant page aggregates. All individual assets, including redundant and partial ones, are hashed to preserve integrity.

| Asset path | Exact source coverage | Asset kind / engine | Fitness | Coverage or fitness note |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001/document_record.md | DOC-001 all source pages | Document identity / native-processing metadata | USABLE | Use identity, hash, and engine only; prior audit boundaries are not discovery input. |
| .ai_paper_validation/document_outputs/DOC-001/images/page-005.png | DOC-001 PDF p. 5 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-001/images/page-006.png | DOC-001 PDF p. 6 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-001/images/page-007.png | DOC-001 PDF p. 7 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-001/images/page-008.png | DOC-001 PDF p. 8 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-001/images/page-009.png | DOC-001 PDF p. 9 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-001/native_text/page-001.txt | DOC-001 PDF p. 1 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/native_text/page-002.txt | DOC-001 PDF p. 2 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/native_text/page-003.txt | DOC-001 PDF p. 3 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/native_text/page-004.txt | DOC-001 PDF p. 4 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/native_text/page-005.txt | DOC-001 PDF p. 5 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/native_text/page-006.txt | DOC-001 PDF p. 6 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/native_text/page-007.txt | DOC-001 PDF p. 7 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/native_text/page-008.txt | DOC-001 PDF p. 8 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/native_text/page-009.txt | DOC-001 PDF p. 9 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/native_text/page-010.txt | DOC-001 PDF p. 10 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/native_text/page-011.txt | DOC-001 PDF p. 11 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text.txt | DOC-001 all source pages | Normalized document text / Poppler layout | DUPLICATE | Redundant full-document text; per-page source-matched files are primary. |
| .ai_paper_validation/document_outputs/DOC-001/page_manifest.csv | DOC-001 all source pages | Page/source-location map / native metadata | USABLE | Use exact page paths, native quality, and image location only; no prior scientific decisions. |
| .ai_paper_validation/document_outputs/DOC-002/document_record.md | DOC-002 all source pages | Document identity / native-processing metadata | PARTIAL | Identity and hash usable; prior no-extraction scope statement superseded by 92 source-matched page files. |
| .ai_paper_validation/document_outputs/DOC-003/document_record.md | DOC-003 all source pages | Document identity / native-processing metadata | USABLE | Use identity, hash, and engine only; prior audit boundaries are not discovery input. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-002.png | DOC-003 PDF p. 2 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-003.png | DOC-003 PDF p. 3 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-004.png | DOC-003 PDF p. 4 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-005.png | DOC-003 PDF p. 5 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-006.png | DOC-003 PDF p. 6 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-007.png | DOC-003 PDF p. 7 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-008.png | DOC-003 PDF p. 8 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-009.png | DOC-003 PDF p. 9 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-010.png | DOC-003 PDF p. 10 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-011.png | DOC-003 PDF p. 11 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-012.png | DOC-003 PDF p. 12 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-013.png | DOC-003 PDF p. 13 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-014.png | DOC-003 PDF p. 14 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-015.png | DOC-003 PDF p. 15 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-016.png | DOC-003 PDF p. 16 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-017.png | DOC-003 PDF p. 17 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-018.png | DOC-003 PDF p. 18 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-019.png | DOC-003 PDF p. 19 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-020.png | DOC-003 PDF p. 20 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/images/page-021.png | DOC-003 PDF p. 21 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-001.txt | DOC-003 PDF p. 1 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-002.txt | DOC-003 PDF p. 2 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-003.txt | DOC-003 PDF p. 3 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-004.txt | DOC-003 PDF p. 4 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-005.txt | DOC-003 PDF p. 5 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-006.txt | DOC-003 PDF p. 6 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-007.txt | DOC-003 PDF p. 7 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-008.txt | DOC-003 PDF p. 8 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-009.txt | DOC-003 PDF p. 9 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-010.txt | DOC-003 PDF p. 10 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-011.txt | DOC-003 PDF p. 11 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-012.txt | DOC-003 PDF p. 12 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-013.txt | DOC-003 PDF p. 13 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-014.txt | DOC-003 PDF p. 14 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-015.txt | DOC-003 PDF p. 15 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-016.txt | DOC-003 PDF p. 16 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-017.txt | DOC-003 PDF p. 17 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-018.txt | DOC-003 PDF p. 18 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-019.txt | DOC-003 PDF p. 19 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-020.txt | DOC-003 PDF p. 20 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-021.txt | DOC-003 PDF p. 21 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-022.txt | DOC-003 PDF p. 22 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/native_text/page-023.txt | DOC-003 PDF p. 23 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/document_outputs/DOC-003/normalized_text.txt | DOC-003 all source pages | Normalized document text / Poppler layout | DUPLICATE | Redundant full-document text; per-page source-matched files are primary. |
| .ai_paper_validation/document_outputs/DOC-003/page_manifest.csv | DOC-003 all source pages | Page/source-location map / native metadata | USABLE | Use exact page paths, native quality, and image location only; no prior scientific decisions. |
| .ai_paper_validation/review_1_5_3/preprocessing/main_quantitative_mapper/DOC-001-layout.txt | DOC-001 PDF pp. 1–11 | Full native layout / Poppler pdftotext | DUPLICATE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/doc001-page-2-layout.txt | DOC-001 PDF p. 2 | Raw targeted layout / Poppler pdftotext | DUPLICATE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/doc001-page-5-layout.txt | DOC-001 PDF p. 5 | Raw targeted layout / Poppler pdftotext | DUPLICATE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/doc001-page-5.png | DOC-001 PDF p. 5 | Rendered source page / Poppler CPU | DUPLICATE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/doc003-page-13.png | DOC-003 PDF p. 13 | Rendered source page / Poppler CPU | DUPLICATE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/doc003-page-14.png | DOC-003 PDF p. 14 | Rendered source page / Poppler CPU | DUPLICATE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/doc003-page-22-layout.txt | DOC-003 PDF p. 22 | Raw targeted layout / Poppler pdftotext | DUPLICATE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/doc003-page-22.png | DOC-003 PDF p. 22 | Rendered source page / Poppler CPU | USABLE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/doc003-page-6-layout.txt | DOC-003 PDF p. 6 | Raw targeted layout / Poppler pdftotext | DUPLICATE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/doc003-page-6.png | DOC-003 PDF p. 6 | Rendered source page / Poppler CPU | DUPLICATE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/doc003-pages-13-15-layout.txt | DOC-003 PDF pp. 13–15 | Raw targeted layout / Poppler pdftotext | DUPLICATE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-001.txt | DOC-002 PDF p. 1 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-002.txt | DOC-002 PDF p. 2 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-003.txt | DOC-002 PDF p. 3 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-004.txt | DOC-002 PDF p. 4 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-005.txt | DOC-002 PDF p. 5 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-006.txt | DOC-002 PDF p. 6 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-007.txt | DOC-002 PDF p. 7 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-008.txt | DOC-002 PDF p. 8 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-009.txt | DOC-002 PDF p. 9 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-010.txt | DOC-002 PDF p. 10 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-011.txt | DOC-002 PDF p. 11 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-012.txt | DOC-002 PDF p. 12 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-013.txt | DOC-002 PDF p. 13 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-014.txt | DOC-002 PDF p. 14 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-015.txt | DOC-002 PDF p. 15 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-016.txt | DOC-002 PDF p. 16 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-017.txt | DOC-002 PDF p. 17 | Native layout / Poppler pdftotext | PARTIAL | Source-matched caption/footer only; image content freshly rendered and visually mapped in this run. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-018.txt | DOC-002 PDF p. 18 | Native layout / Poppler pdftotext | PARTIAL | Source-matched caption/footer only; image content freshly rendered and visually mapped in this run. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-019.txt | DOC-002 PDF p. 19 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-020.txt | DOC-002 PDF p. 20 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-021.txt | DOC-002 PDF p. 21 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-022.txt | DOC-002 PDF p. 22 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-023.txt | DOC-002 PDF p. 23 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-024.txt | DOC-002 PDF p. 24 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-025.txt | DOC-002 PDF p. 25 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-026.txt | DOC-002 PDF p. 26 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-027.txt | DOC-002 PDF p. 27 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-028.txt | DOC-002 PDF p. 28 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-029.txt | DOC-002 PDF p. 29 | Native layout / Poppler pdftotext | PARTIAL | Source-matched caption/footer only; image content freshly rendered and visually mapped in this run. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-030.txt | DOC-002 PDF p. 30 | Native layout / Poppler pdftotext | PARTIAL | Source-matched caption/footer only; image content freshly rendered and visually mapped in this run. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-031.txt | DOC-002 PDF p. 31 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-032.txt | DOC-002 PDF p. 32 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-033.txt | DOC-002 PDF p. 33 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-034.txt | DOC-002 PDF p. 34 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-035.txt | DOC-002 PDF p. 35 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-036.txt | DOC-002 PDF p. 36 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-037.txt | DOC-002 PDF p. 37 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-038.txt | DOC-002 PDF p. 38 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-039.txt | DOC-002 PDF p. 39 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-040.txt | DOC-002 PDF p. 40 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-041.txt | DOC-002 PDF p. 41 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-042.txt | DOC-002 PDF p. 42 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-043.txt | DOC-002 PDF p. 43 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-044.txt | DOC-002 PDF p. 44 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-045.txt | DOC-002 PDF p. 45 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_layout/page-046.txt | DOC-002 PDF p. 46 | Native layout / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-001.txt | DOC-002 PDF p. 1 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-002.txt | DOC-002 PDF p. 2 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-003.txt | DOC-002 PDF p. 3 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-004.txt | DOC-002 PDF p. 4 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-005.txt | DOC-002 PDF p. 5 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-006.txt | DOC-002 PDF p. 6 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-007.txt | DOC-002 PDF p. 7 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-008.txt | DOC-002 PDF p. 8 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-009.txt | DOC-002 PDF p. 9 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-010.txt | DOC-002 PDF p. 10 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-011.txt | DOC-002 PDF p. 11 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-012.txt | DOC-002 PDF p. 12 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-013.txt | DOC-002 PDF p. 13 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-014.txt | DOC-002 PDF p. 14 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-015.txt | DOC-002 PDF p. 15 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-016.txt | DOC-002 PDF p. 16 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-017.txt | DOC-002 PDF p. 17 | Native text / Poppler pdftotext | PARTIAL | Source-matched caption/footer only; image content freshly rendered and visually mapped in this run. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-018.txt | DOC-002 PDF p. 18 | Native text / Poppler pdftotext | PARTIAL | Source-matched caption/footer only; image content freshly rendered and visually mapped in this run. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-019.txt | DOC-002 PDF p. 19 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-020.txt | DOC-002 PDF p. 20 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-021.txt | DOC-002 PDF p. 21 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-022.txt | DOC-002 PDF p. 22 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-023.txt | DOC-002 PDF p. 23 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-024.txt | DOC-002 PDF p. 24 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-025.txt | DOC-002 PDF p. 25 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-026.txt | DOC-002 PDF p. 26 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-027.txt | DOC-002 PDF p. 27 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-028.txt | DOC-002 PDF p. 28 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-029.txt | DOC-002 PDF p. 29 | Native text / Poppler pdftotext | PARTIAL | Source-matched caption/footer only; image content freshly rendered and visually mapped in this run. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-030.txt | DOC-002 PDF p. 30 | Native text / Poppler pdftotext | PARTIAL | Source-matched caption/footer only; image content freshly rendered and visually mapped in this run. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-031.txt | DOC-002 PDF p. 31 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-032.txt | DOC-002 PDF p. 32 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-033.txt | DOC-002 PDF p. 33 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-034.txt | DOC-002 PDF p. 34 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-035.txt | DOC-002 PDF p. 35 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-036.txt | DOC-002 PDF p. 36 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-037.txt | DOC-002 PDF p. 37 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-038.txt | DOC-002 PDF p. 38 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-039.txt | DOC-002 PDF p. 39 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-040.txt | DOC-002 PDF p. 40 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-041.txt | DOC-002 PDF p. 41 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-042.txt | DOC-002 PDF p. 42 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-043.txt | DOC-002 PDF p. 43 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-044.txt | DOC-002 PDF p. 44 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-045.txt | DOC-002 PDF p. 45 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-046.txt | DOC-002 PDF p. 46 | Native text / Poppler pdftotext | USABLE | Source-matched; locator and transcription aid. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc003_render_check/page-20.png | DOC-003 PDF p. 20 | Rendered source page / Poppler CPU | DUPLICATE | Readable PNG; source/page identity retained; inspect visually when figures require it. |
| .ai_paper_validation/review_1_5_3/preprocessing/support/doc003_render_check/page-21.png | DOC-003 PDF p. 21 | Rendered source page / Poppler CPU | DUPLICATE | Readable PNG; source/page identity retained; inspect visually when figures require it. |

## Unique coverage and gaps

DOC-001: native/layout PDF pp. 1–11; figures/tables images pp. 5–9. DOC-002: native and layout pp. 1–46. DOC-003: native/layout pp. 1–23; figure/table images pp. 2–21 and eMethods image p. 22. Overlapping files never increase reusable units. 76 pages have complete reusable-backed coverage; DOC-002 screenshot pp. 17, 18, 29 and 30 have partial caption-only text and required fresh CPU visual mapping, now complete. Missing images on purely textual pages are not coverage gaps. No source unit is STALE or UNREADABLE; DOC-002's partial legacy document record does not affect its complete later page extraction.

All source-linked reusable units must undergo new quantitative mapping. Fresh-required count: 0. Reuse does not imply scientific checks have already been performed in this run.

## Current-run visual derivatives

These four derivatives freshly cover screenshot content absent from reusable caption-only text; they are not reused artifacts. Direct engine: Poppler pdftoppm 26.01.0, Compute device: CPU. Command and visual inspection are recorded in extraction/support_quantitative_evidence.md. No OCR was used.

| New derivative path | Direct source location | Engine | Use |
|---|---|---|---|
| preprocessing/support_map/doc002-p17.png | DOC-002 physical PDF p. 17 | pdftoppm 26.01.0 CPU | Instrument screenshot mapped visually |
| preprocessing/support_map/doc002-p18.png | DOC-002 physical PDF p. 18 | pdftoppm 26.01.0 CPU | Participant landing page mapped visually |
| preprocessing/support_map/doc002-p29.png | DOC-002 physical PDF p. 29 | pdftoppm 26.01.0 CPU | Original instrument screenshot mapped visually |
| preprocessing/support_map/doc002-p30.png | DOC-002 physical PDF p. 30 | pdftoppm 26.01.0 CPU | Original landing page mapped visually |

## Coordinator coverage-fitness refinement

DOC-002 reusable native/layout pp. 17, 18, 29 and 30 contain appendix captions and footers only, rather than the instrument/landing-page screenshot content. Eight text assets were therefore refined from USABLE to PARTIAL, changing final asset fitness counts to 148 USABLE, 14 DUPLICATE and 9 PARTIAL. The unique source-unit partition is 76 reusable and four fresh-required pages. The support mapper's four CPU renders and direct visual mapping already close these units; no scientific content or candidate changed and no further extraction is required. Initial exact source/text matching remains true but was insufficient to establish complete screenshot coverage. Original reused assets and their hashes were preserved.
