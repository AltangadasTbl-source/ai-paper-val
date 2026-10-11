# Evidence Asset Inventory

Scope: every pre-existing reusable OCR text, native/layout text, rendered page, page manifest, OCR metadata record, document record, and source-location map below `.ai_paper_validation/`. Old candidate, checker, verifier, critic, endetail, quality, and final-report content was not read or used as discovery scope. No pre-existing table/workbook extraction, Office workbook, or CSV extraction exists. `USABLE` assets provide the stated mapping; `PARTIAL` assets are auxiliary or do not independently cover a page; `DUPLICATE` is retained as alternate provenance only. No identified asset is `STALE` or `UNREADABLE`: direct-source hashes match the document maps.

| Asset path | Asset class and method | Exact direct-source location(s) | Coverage and fitness |
|---|---|---|---|
| .ai_paper_validation/document_outputs/package_manifest.json | Document manifest | DOC-001 PDF pp. 1-11; DOC-002 pp. 1-48; DOC-003 pp. 1-9; DOC-004 p. 1 | USABLE; document identity, hashes, and complete page-count map only. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/document_record.json | Document record | DOC-001 PDF pp. 1-11 | USABLE; identity and legacy page-scope metadata only. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/page_manifest.json | Page manifest | DOC-001 PDF pp. 1-9 | PARTIAL; exact native/OCR/page links for pp. 1-9; pp. 10-11 require fresh mapping. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-001.txt | Native PDF text | DOC-001 PDF p. 1 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-002.txt | Native PDF text | DOC-001 PDF p. 2 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-003.txt | Native PDF text | DOC-001 PDF p. 3 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-004.txt | Native PDF text | DOC-001 PDF p. 4 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-005.txt | Native PDF text | DOC-001 PDF p. 5 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-006.txt | Native PDF text | DOC-001 PDF p. 6 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-007.txt | Native PDF text | DOC-001 PDF p. 7 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-008.txt | Native PDF text | DOC-001 PDF p. 8 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-009.txt | Native PDF text | DOC-001 PDF p. 9 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/ocr_text/page-003.txt | CPU OCR text | DOC-001 PDF p. 3 | PARTIAL; additive flow-diagram transcription, matched to a usable native-text page. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/page_ocr_metadata/page-003.json | OCR metadata record | DOC-001 PDF p. 3 | USABLE; OCR method/provenance map only. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-003-03.png | Rendered page | DOC-001 PDF p. 3 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-005-05.png | Rendered page | DOC-001 PDF p. 5 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-006-06.png | Rendered page | DOC-001 PDF p. 6 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-007-07.png | Rendered page | DOC-001 PDF p. 7 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-008-08.png | Rendered page | DOC-001 PDF p. 8 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-002-protocol/document_record.json | Document record | DOC-002 PDF pp. 1-48 | USABLE; identity and page-count map only; no reusable page extraction. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/document_record.json | Document record | DOC-003 PDF pp. 1-9 | USABLE; identity and page-scope metadata only. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_manifest.json | Page manifest | DOC-003 PDF pp. 1-9 | USABLE; exact native/OCR/rendered-page links for every page. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-001.txt | Native PDF text | DOC-003 PDF p. 1 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-002.txt | Native PDF text | DOC-003 PDF p. 2 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-003.txt | Native PDF text | DOC-003 PDF p. 3 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-004.txt | Native PDF text | DOC-003 PDF p. 4 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-005.txt | Native PDF text | DOC-003 PDF p. 5 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-006.txt | Native PDF text | DOC-003 PDF p. 6 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-007.txt | Native PDF text | DOC-003 PDF p. 7 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-008.txt | Native PDF text | DOC-003 PDF p. 8 | USABLE; high-quality page text. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-009.txt | Native PDF text | DOC-003 PDF p. 9 | USABLE; high-quality page text; OCR remains auxiliary for eFigure. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-002.txt | CPU OCR text | DOC-003 PDF p. 2 | PARTIAL; additive eTable visual transcription. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-003.txt | CPU OCR text | DOC-003 PDF p. 3 | PARTIAL; additive eTable visual transcription. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-004.txt | CPU OCR text | DOC-003 PDF p. 4 | PARTIAL; additive eTable visual transcription. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-005.txt | CPU OCR text | DOC-003 PDF p. 5 | PARTIAL; additive eTable visual transcription. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-006.txt | CPU OCR text | DOC-003 PDF p. 6 | PARTIAL; additive eTable visual transcription. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-007.txt | CPU OCR text | DOC-003 PDF p. 7 | PARTIAL; additive eTable visual transcription. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-008.txt | CPU OCR text | DOC-003 PDF p. 8 | PARTIAL; additive eTable visual transcription. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/ocr_text/page-009.txt | CPU OCR text | DOC-003 PDF p. 9 | PARTIAL; additive eFigure transcription; reported mean confidence 0.732. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-002.json | OCR metadata record | DOC-003 PDF p. 2 | USABLE; OCR method/provenance map only. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-003.json | OCR metadata record | DOC-003 PDF p. 3 | USABLE; OCR method/provenance map only. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-004.json | OCR metadata record | DOC-003 PDF p. 4 | USABLE; OCR method/provenance map only. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-005.json | OCR metadata record | DOC-003 PDF p. 5 | USABLE; OCR method/provenance map only. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-006.json | OCR metadata record | DOC-003 PDF p. 6 | USABLE; OCR method/provenance map only. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-007.json | OCR metadata record | DOC-003 PDF p. 7 | USABLE; OCR method/provenance map only. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-008.json | OCR metadata record | DOC-003 PDF p. 8 | USABLE; OCR method/provenance map only. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/page_ocr_metadata/page-009.json | OCR metadata record | DOC-003 PDF p. 9 | USABLE; OCR method/provenance map only. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-002-2.png | Rendered page | DOC-003 PDF p. 2 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-003-3.png | Rendered page | DOC-003 PDF p. 3 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-004-4.png | Rendered page | DOC-003 PDF p. 4 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-005-5.png | Rendered page | DOC-003 PDF p. 5 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-006-6.png | Rendered page | DOC-003 PDF p. 6 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-007-7.png | Rendered page | DOC-003 PDF p. 7 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-008-8.png | Rendered page | DOC-003 PDF p. 8 | USABLE; visual-confirmation asset. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/rendered_pages/page-009-9.png | Rendered page | DOC-003 PDF p. 9 | USABLE; visual-confirmation asset for the eFigure. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/results_evidence_map.json | Source-location map | DOC-003 PDF pp. 1-9; p. 1 index, p. 2 eTable 1, pp. 3-5 eTable 2, p. 6 eTable 3, p. 7 eTable 4, p. 8 eTable 5, p. 9 eFigure | USABLE; page/table locator map, not a candidate source. |
| .ai_paper_validation/document_outputs/DOC-003-results-supplement/results_evidence_map.md | Source-location map | DOC-003 PDF pp. 1-9; same table/page locations as the JSON map | DUPLICATE; human-readable alternate of the JSON location map. |
| .ai_paper_validation/document_outputs/DOC-004-data-sharing-statement/document_record.json | Document record | DOC-004 PDF p. 1 | USABLE; document identity only; no reusable page extraction. |
| .ai_paper_validation/preprocessing/ocr_backend.json | OCR backend record | DOC-001 PDF p. 3 and DOC-003 PDF pp. 2-9 | USABLE; CPU OCR method provenance only. |

## Fresh direct-source native-text mappings created in this run

`pdftotext -layout` was run page-by-page directly against the supplied PDFs. These new artifacts are not reused-artifact inputs and are intentionally absent from `reused_artifact_hashes_before.sha256`.

| Asset path pattern | Exact direct-source location(s) | Fitness |
|---|---|---|
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-001-main-article_page-010.txt; .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-001-main-article_page-011.txt | DOC-001 PDF pp. 10-11 | USABLE; fresh layout-preserving native text. |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-001.txt through DOC-002-protocol_page-048.txt | DOC-002 PDF pp. 1-48, one matching file per page | USABLE; fresh layout-preserving native text. |
| .ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-004-data-sharing-statement_page-001.txt | DOC-004 PDF p. 1 | USABLE; fresh layout-preserving native text. |

Coverage gap disposition: no scientific-coverage gaps remain. Legacy reusable-derivative gaps are DOC-001 pp. 10-11, all DOC-002 pages, and DOC-004 p. 1; each was directly mapped through the fresh files above. A protocol appendix page (DOC-002 PDF p. 42) contains only a page heading in its text layer, but the direct page extraction is truthful and its direct-source page mapping is complete; any later content-specific visual confirmation should use the supplied PDF page.
