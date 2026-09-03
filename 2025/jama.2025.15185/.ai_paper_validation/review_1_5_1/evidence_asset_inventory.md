# Reused Evidence-Asset Inventory

Scope: every existing eligible text, normalized text, rendered page, page manifest, document status map, and evidence map below `.ai_paper_validation/document_outputs/`. All 88 files were SHA-256 hashed before reuse; exact individual hashes and paths are in `reused_artifact_hashes_before.sha256`. No reusable asset was modified. Historical checker, candidate, queue, verifier, critic, endetail, quality, and final-report records were not read.

Fitness terms: `USABLE` means source-linked and sufficient as a mapper locator/transcription aid; `PARTIAL` means it supports only the stated content and requires the paired visual asset or direct source for missing graphical content; `DUPLICATE` means a page-preserving alternate derivative that adds no unique coverage; `STALE` means a historical scope/status record that does not cover workflow-1.5.1 extraction; `UNREADABLE` was not observed.

| Asset group and exact package-relative paths | Count | Exact source-unit mapping | Method / content role | Fitness | Coverage disposition |
|---|---:|---|---|---|---|
| `document_outputs/main_article/preprocessing/native_text/page-001.txt` through `page-010.txt` | 10 | DOC-001 PDF pp. 1-10, one file per identically numbered page | Native `pdftotext` page extraction | USABLE | Reusable coverage for DOC-001 pp. 1-10. |
| `document_outputs/main_article/preprocessing/normalized_text/page-001.txt` through `page-010.txt` | 10 | DOC-001 PDF pp. 1-10, one file per identically numbered page | Page-preserving whitespace/form-feed normalization of corresponding native text | DUPLICATE | Locator alternate only; does not increase the 10 unique covered pages. |
| `document_outputs/main_article/preprocessing/page_images/page-004.png`, `page-005.png`, `page-006.png` | 3 | DOC-001 PDF pp. 4, 5, 6 | 200-dpi rendered visual evidence for Table 1, Figure 1, Table 2/Figure 2 | USABLE | Complements native text on the three visual pages; no additional units. |
| `document_outputs/main_article/preprocessing/page_manifest.md` | 1 | DOC-001 PDF pp. 1-10 | Page-to-derivative map and extraction-quality record | USABLE | Confirms exact source mapping for the 10 reusable pages. |
| `document_outputs/main_article/preprocessing_status.md` | 1 | DOC-001 PDF pp. 1-10 | Historical preprocessing status | USABLE | Confirms direct-source identity and completed page coverage; not scientific evidence by itself. |
| `document_outputs/main_article/main_article_results_extraction.md` | 1 | DOC-001 PDF pp. 1, 3-8 (with cited source pages); no coverage claim for unlisted p. 2, p. 9, p. 10 | Existing result-evidence map | PARTIAL | Useful locator only; native text/page manifest provides complete pp. 1-10 coverage. |
| `document_outputs/supplement_3_results/preprocessing/native_text/page-010.txt` through `page-027.txt` | 18 | DOC-004 PDF pp. 10-27, one file per identically numbered page | Native page extraction | USABLE on pp. 10-17, 19, 20, 24; PARTIAL on pp. 18, 21-23, 25-27 | Together with matched PNG renders, covers DOC-004 pp. 10-27. Sparse/graphic text is not treated as sufficient alone. |
| `document_outputs/supplement_3_results/preprocessing/normalized_text/page-010.txt` through `page-027.txt` | 18 | DOC-004 PDF pp. 10-27, one file per identically numbered page | Page-preserving whitespace/form-feed normalization of corresponding native text | DUPLICATE | Locator alternate only; does not increase the 18 unique covered pages. |
| `document_outputs/supplement_3_results/preprocessing/page_images/page-010.png` through `page-027.png` | 18 | DOC-004 PDF pp. 10-27, one image per identically numbered page | 200-dpi rendered source-linked visual evidence | USABLE | Provides visual coverage for every page and is necessary to support the partial native-text pages 18, 21-23, and 25-27. |
| `document_outputs/supplement_3_results/preprocessing/page_manifest.md` | 1 | DOC-004 PDF pp. 10-27 | Page-to-native-text/render map and quality record | USABLE | Confirms coverage and the required visual handling for sparse/graphic pages. |
| `document_outputs/supplement_3_results/preprocessing_status.md` | 1 | DOC-004 PDF pp. 10-27 | Historical preprocessing status | USABLE | Confirms selected pages and source-linked output; not scientific evidence by itself. |
| `document_outputs/supplement_3_results/results_evidence_map_pages_10_27.md` | 1 | DOC-004 PDF pp. 10-27 | Existing table/figure evidence map with page locations | USABLE | Locator for all 18 reusable pages; source PDF remains final authority. |
| `document_outputs/supplement_1_protocol/preprocessing_status.md` | 1 | DOC-002, no page extraction | Historical status says earlier scope excluded the protocol | STALE | No reusable units; fresh direct mapping required for pp. 1-94. |
| `document_outputs/supplement_2_sap/preprocessing_status.md` | 1 | DOC-003, no page extraction | Historical status says earlier scope excluded the SAP | STALE | No reusable units; fresh direct mapping required for pp. 1-18. |
| `document_outputs/supplement_4_administrative/preprocessing_status.md` | 1 | DOC-005, no page extraction | Historical status says earlier scope excluded the administrative supplement | STALE | No reusable units; fresh direct mapping required for pp. 1-8. |
| `document_outputs/supplement_5_analysis_code/preprocessing_status.md` | 1 | DOC-006, no page extraction | Historical status says earlier scope excluded the analysis-code supplement | STALE | No reusable units; fresh direct mapping required for p. 1. |
| `document_outputs/supplement_6_data_sharing/preprocessing_status.md` | 1 | DOC-007, no page extraction | Historical status says earlier scope excluded the data-sharing supplement | STALE | No reusable units; fresh direct mapping required for p. 1. |

## Coverage and gap reconciliation

- Usable source-linked coverage: DOC-001 pp. 1-10 (10 pages) and DOC-004 pp. 10-27 (18 pages), totaling 28 unique PDF pages.
- Explicit derivative limitations: DOC-004 native text is sparse or partial for pp. 18, 21-23, and 25-27. Corresponding source-linked PNG renders are present and usable for visual mapping; final evidence confirmation must remain against the source PDF page.
- Fresh-required direct-source gaps: DOC-002 pp. 1-94; DOC-003 pp. 1-18; DOC-004 pp. 1-9; DOC-005 pp. 1-8; DOC-006 p. 1; DOC-007 p. 1 (131 pages total).
- No OCR text, workbook extraction, Office extraction, CSV extraction, document-record file, or separate source-location map other than the listed page/evidence maps exists below the audit output area.

## Tool and integrity note

Inventory used `find`, `sha256sum`, and existing page/status manifests. `pdfinfo` confirmed the direct PDF page counts. No direct source, derivative, OCR, conversion, rendering, or scientific candidate analysis was created in this inventory stage.
