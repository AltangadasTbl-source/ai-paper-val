# Reused Evidence-Asset Inventory

This inventory includes every existing OCR-text, native/layout-text, table/workbook extraction, rendered-page, page-manifest, document-record, and source-location-map artifact below the pre-existing audit area. It does not use legacy candidate, queue, verifier, critic, endetail, checker, or final-report content as discovery scope. Hashes for all 137 listed artifacts are recorded in `reused_artifact_hashes_before.sha256`.

## Coverage and fitness key

- **USABLE:** Source-linked, readable evidence adequate as a locator or transcription aid for the stated units.
- **PARTIAL:** Readable but incomplete for the stated units; the stated gaps require a complementary reusable asset or direct source.
- **STALE:** Retained historical mapping or record that does not provide current complete reusable coverage.
- **DUPLICATE:** Repeats another artifact's content without adding source-unit coverage.
- **UNREADABLE:** Cannot be used. No artifact in the supplied reusable set is unreadable.

## Asset inventory

| Asset class | Exact artifact path or file set | Source and exact covered location | Method | Fitness | Coverage and gap assignment |
|---|---|---|---|---|---|
| Document manifest | .ai_paper_validation/package_manifest.md | DOC-001 through DOC-007; package-level source identity, not page evidence. | Historical package source map. | PARTIAL | Identifies all seven sources but supplies no page-level extraction; all source pages remain governed by `source_coverage.md`. |
| Document record | .ai_paper_validation/document_outputs/DOC-001-MAIN/document_record.md | DOC-001, PDF pp. 1-14. | Historical direct-source record. | USABLE | Complete document identity and preprocessing map; complements native text for all 14 pages. |
| Document record | .ai_paper_validation/document_outputs/DOC-002-ADMIN-COLLAB/document_record.md | DOC-002, PDF pp. 1-30. | Historical direct-source record. | STALE | Retains page count and identity only; no page extraction. Fresh mapping is DOC-002 pp. 1-30. |
| Document record | .ai_paper_validation/document_outputs/DOC-003-PROTOCOL/document_record.md | DOC-003, PDF pp. 1-82. | Historical direct-source record. | STALE | Retains page count and identity only; no page extraction. Fresh mapping is DOC-003 pp. 1-82. |
| Document record | .ai_paper_validation/document_outputs/DOC-004-SAP-TRIAL/document_record.md | DOC-004, PDF pp. 1-40. | Historical direct-source record. | STALE | Identifies image-first source only; no reusable render or OCR. Fresh mapping is DOC-004 pp. 1-40. |
| Document record | .ai_paper_validation/document_outputs/DOC-005-SAP-ANALYSIS/document_record.md | DOC-005, PDF pp. 1-7. | Historical direct-source record. | STALE | Retains page count and identity only; no page extraction. Fresh mapping is DOC-005 pp. 1-7. |
| Document record | .ai_paper_validation/document_outputs/DOC-006-RESULTS-SUPP/document_record.md | DOC-006, PDF pp. 1-53. | Historical direct-source record. | USABLE | Complete document identity and page-level preprocessing provenance; complements native text and renders for all 53 pages. |
| Document record | .ai_paper_validation/document_outputs/DOC-007-ADMIN-DATA/document_record.md | DOC-007, PDF p. 1. | Historical direct-source record. | STALE | Retains page count and identity only; no page extraction. Fresh mapping is DOC-007 p. 1. |
| Page manifest | .ai_paper_validation/preprocessing/DOC-001-MAIN/page_manifest.csv | DOC-001, PDF pp. 1-14; each row names source PDF page and native text, and pp. 5-9 render paths. | Page-level extraction manifest. | USABLE | Full page map; no DOC-001 reusable-coverage gap. |
| Native text | .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-001.txt through page-014.txt (14 files) | DOC-001, respectively PDF pp. 1-14. | Native PDF text extraction. | USABLE | All 14 pages assessed Good; no DOC-001 text gap. |
| Normalized text | .ai_paper_validation/preprocessing/DOC-001-MAIN/normalized_text.txt | DOC-001, PDF pp. 1-14 with page markers. | Normalized native-text concatenation. | DUPLICATE | Repeats the full per-page native extraction as a convenient locator; no additional unit coverage. |
| Rendered pages | .ai_paper_validation/preprocessing/DOC-001-MAIN/page_images/page-005.png through page-009.png (5 files) | DOC-001, respectively PDF pp. 5-9. | 200-dpi rendered visual evidence. | USABLE | Supports visual tables and figures on pp. 5-9. Pages 1-4 and 10-14 require no render because the native text is usable. |
| Extraction summary | .ai_paper_validation/preprocessing/DOC-001-MAIN/extraction_summary.md | DOC-001, PDF pp. 1-14. | Historical preprocessing provenance. | USABLE | Documents all 14 native-text pages and visual-render scope; no independent text content. |
| Source-location map | .ai_paper_validation/document_outputs/DOC-001-MAIN/main_text_extraction.md | DOC-001, source references throughout PDF pp. 1-14. | Structured source-linked result map derived from native text and renders. | USABLE | Full-document locator and table/figure map. It remains a locator; downstream claims require direct-source confirmation. |
| Page manifest | .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_manifest.csv | DOC-006, PDF pp. 1-53; each row names source PDF page, native text, quality, and where applicable rendered page. | Page-level extraction manifest. | USABLE | Full page map. It identifies sparse or partial native text on pp. 5-8, 13-25, 37, 48, and 50. |
| Native text | .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-001.txt through page-004.txt, page-009.txt through page-012.txt, page-026.txt through page-036.txt, page-038.txt through page-047.txt, page-049.txt, and page-051.txt through page-053.txt (33 files) | DOC-006, respectively PDF pp. 1-4, 9-12, 26-36, 38-47, 49, and 51-53. | Native PDF text extraction. | USABLE | Good native text on all listed pages. |
| Native text | .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-005.txt through page-008.txt, page-013.txt through page-025.txt, page-037.txt, page-048.txt, and page-050.txt (20 files) | DOC-006, respectively PDF pp. 5-8, 13-25, 37, 48, and 50. | Native PDF text extraction. | PARTIAL | Sparse, partial visual-text, or partial-continuation text. Complementary rendered pages are present for every listed page; downstream mapping must use direct PDF confirmation for values. |
| Normalized text | .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/normalized_text.txt | DOC-006, PDF pp. 1-53 with page markers. | Normalized native-text concatenation. | PARTIAL | Repeats page text and inherits the 20-page sparse/partial native-text gap; use rendered evidence for those pages. |
| Rendered pages | .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-005.png through page-053.png (49 files) | DOC-006, respectively PDF pp. 5-53. | 200-dpi rendered visual evidence. | USABLE | Covers every visual or sparse/partial native-text page, including pp. 5-8, 13-25, 37, 48, and 50. Pages 1-4 are covered by usable native text. |
| Extraction summary | .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/extraction_summary.md | DOC-006, PDF pp. 1-53. | Historical preprocessing provenance. | USABLE | Documents full native-text scope, 49 rendered pages, and unavailable historical OCR; no independent text content. |
| Source-location map | .ai_paper_validation/document_outputs/DOC-006-RESULTS-SUPP/results_supplement_evidence_map.md | DOC-006, source-linked result evidence across PDF pp. 4-53. | Structured source-linked supplement map using native text and renders. | PARTIAL | Valuable locator for eMethods, eFigures, and eTables; pp. 1-3 remain covered by native text and all mapped values require direct-source confirmation. |

## Asset-type absence and limitations

No reusable OCR text, layout-text extraction, table extraction, workbook extraction, Office conversion, DOC/DOCX, XLS/XLSX, or CSV evidence asset exists below the prior audit area. The historic OCR attempt for DOC-006 produced no OCR output; its affected native-text pages are instead covered by reusable renders. No reusable page-level asset exists for DOC-002, DOC-003, DOC-004, DOC-005, or DOC-007, so every page of those sources is fresh-required. No asset is classified UNREADABLE.

## Reusable-coverage partition

The complete usable reusable set covers DOC-001 pp. 1-14 and DOC-006 pp. 1-53: 67 unique source units. All other direct-source units, 160 pages, are fresh-required. Overlapping normalized text, page manifests, summaries, document records, and source maps are metadata or duplicate locators and were not double-counted.
