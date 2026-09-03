# Reused Evidence-Asset Inventory

Inventory method: recursive file inventory below the existing audit area, SHA-256 hashing, filename-to-source mapping, and direct inspection of the permitted preprocessing record, document records, and source-linked evidence maps. Old candidate, checker, queue, verifier, critic, endetail, and final-report material was excluded from discovery scope.

Fitness terms: **USABLE** = source-matched and sufficient as a locator/transcription aid for its stated units; **PARTIAL** = source-matched but incomplete for the stated units; **DUPLICATE** = an overlapping derivative retained only as optional visual provenance; **UNREADABLE** and **STALE** were not observed.

| Asset group and package-relative paths | Method / exact source coverage | Fitness | Coverage use |
|---|---|---|---|
| `.ai_paper_validation/preprocessing/DOC-001/native_pages/page-001.txt` through `page-010.txt` (10 files) | Page-level native `pdftotext` extraction; DOC-001 PDF pp. 1-10, one file per same-numbered page. | USABLE | Reusable for all 10 DOC-001 page units. |
| `.ai_paper_validation/preprocessing/DOC-001/page_images/page-004.png` through `page-007.png` (4 files) | Rendered inspection pages; DOC-001 PDF pp. 4-7. | DUPLICATE | Optional visual confirmation only; native text already covers the same page units. |
| `.ai_paper_validation/preprocessing/DOC-004/native_pages/page-001.txt` through `page-009.txt` (9 files) | Page-level native extraction; DOC-004 PDF pp. 1-9. | USABLE | Reusable locator/transcription aid for pages 1-9. |
| `.ai_paper_validation/preprocessing/DOC-004/native_pages/page-010.txt` through `page-018.txt` (9 files) | Page-level native extraction; DOC-004 PDF pp. 10-18. The text layer is largely figure titles/labels rather than full plotted content. | PARTIAL | Use only with rendered page images; it does not independently cover visual figure values. |
| `.ai_paper_validation/preprocessing/DOC-004/page_images/page-003.png` through `page-018.png` (16 files) | Rendered inspection pages; DOC-004 PDF pp. 3-18. | USABLE | Visual reusable evidence for tables/figures on pp. 3-18; together with native text, supports all DOC-004 pages. |
| `.ai_paper_validation/preprocessing/processing_record.md` | Preprocessing provenance and page-to-artifact map for DOC-001 pp. 1-10 and DOC-004 pp. 1-18. | USABLE | Source-location map; not an independent numeric transcription. |
| `.ai_paper_validation/document_outputs/DOC-001/document_record.md` through `DOC-006/document_record.md` (6 files) | Stable document identity records; each maps one exact direct PDF to DOC-001 through DOC-006 and records page count/classification. | USABLE | Identity and scope locator for all 194 page units; not an independent extraction. |
| `.ai_paper_validation/document_outputs/package_manifest.md` | Package-level document map; DOC-001 through DOC-006, with exact filenames and page counts. | USABLE | Identity/page-count locator for all 194 page units; not an independent extraction. |
| `.ai_paper_validation/document_outputs/DOC-001/main_article_result_evidence.md` | Source-linked evidence map for DOC-001 PDF pp. 1, 3, 4, 6, 7, and 8; it declares main-article result scope. | PARTIAL | Reusable result locator for listed pages only; native page text remains the complete DOC-001 reusable page coverage. |
| `.ai_paper_validation/document_outputs/DOC-004/results_evidence_map.md` | Source-linked evidence map for DOC-004 PDF pp. 2-18; it identifies eTables/eFigures and their source pages. | PARTIAL | Reusable result locator for pp. 2-18; native text plus rendered pages provide full DOC-004 coverage. |

There are 58 eligible pre-existing reused assets: 28 native-text files, 20 rendered-page files, 7 document records, 2 result-evidence maps, and 1 preprocessing record. No existing OCR output, layout-text extraction, tabular extraction, workbook extraction, standalone page manifest, or Office/CSV source artifact was found. All 58 are listed and hashed individually in `reused_artifact_hashes_before.sha256`.

## Unit coverage decision

Reusable page coverage is DOC-001 pp. 1-10 (10 units) and DOC-004 pp. 1-18 (18 units), totaling 28 unique units. The remaining 166 unique page units have no usable page-level reusable extraction and are fresh-required: DOC-002 pp. 1-153, DOC-003 pp. 1-9, DOC-005 pp. 1-3, and DOC-006 p. 1. Document maps do not convert uncovered pages into reusable page extraction.
