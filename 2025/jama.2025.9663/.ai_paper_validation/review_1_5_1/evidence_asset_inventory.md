# Reused Evidence-Asset Inventory

This inventory covers 115 existing eligible derivative/document-map assets below `.ai_paper_validation/`, excluding the new `review_1_5_1` directory. It does not treat legacy candidate, checker, verifier, critic, endetail, or final-report content as scientific input. All paths below are package-relative. Hashes for every listed asset are in `reused_artifact_hashes_before.sha256`.

## Asset classification key

- **USABLE:** source-matched and suitable as a locator/transcription aid for the specified units.
- **PARTIAL:** useful metadata or a partial source map, but it cannot close every stated unit or contains legacy-scope limitations.
- **STALE:** a valid retained artifact whose former scope/coverage statement conflicts with Workflow 1.5.1 complete coverage.
- **DUPLICATE:** retained document record with no independent page-level evidence beyond another listed asset.
- **UNREADABLE:** not usable for direct-source mapping.

## Page-level extraction and render assets

| Asset path or exact path set | Type / method | Direct-source locations covered | Fitness | Classification | Curation use |
|---|---|---|---|---|---|
| `.ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/page-001.txt` through `page-011.txt` | Native normalized text | DOC-001 PDF pp. 1-11, one file per matching page | Page manifest reports usable/acceptable native text on every page. | USABLE | Primary reusable locator/transcription aid for DOC-001 pp. 1-11. |
| `.ai_paper_validation/document_outputs/DOC-001-main-article/ocr_text/page-001.txt`, `page-003.txt` through `page-010.txt`, and `page-001-abstract-crop.txt` | Tesseract OCR | DOC-001 PDF pp. 1, 3-10; abstract crop is a subregion of p. 1 | Selective visual support for layout-dependent pages; crop duplicates only a portion of p. 1. | USABLE | Cross-check/locator only; no extra unit credit beyond native coverage. |
| `.ai_paper_validation/document_outputs/DOC-001-main-article/page_images/page-001.png`, `page-003.png` through `page-010.png`, and `page-001-abstract-crop.png` | Rendered PNG | DOC-001 PDF pp. 1, 3-10; crop is a p. 1 subregion | 200-dpi visual source representation retained for figures/tables/flow. | USABLE | Visual confirmation aid only; no extra unit credit. |
| `.ai_paper_validation/document_outputs/DOC-003-supplement-2-results/normalized_text/page-002.txt` through `page-027.txt` | Native normalized text | DOC-003 PDF pp. 2-27, one file per matching page | Page manifest reports acceptable native text on pp. 2-7 and retained native text plus visual/OCR support on pp. 8-27. | USABLE | Primary reusable locator/transcription aid for DOC-003 pp. 2-27. |
| `.ai_paper_validation/document_outputs/DOC-003-supplement-2-results/ocr_text/page-008.txt` through `page-027.txt` | Tesseract OCR | DOC-003 PDF pp. 8-27 | Selective visual support for layout-dependent eFigures/eTables. | USABLE | Cross-check/locator only; no extra unit credit beyond native coverage. |
| `.ai_paper_validation/document_outputs/DOC-003-supplement-2-results/page_images/page-008.png` through `page-027.png` | Rendered PNG | DOC-003 PDF pp. 8-27 | 200-dpi visual source representation retained for eFigures/eTables. | USABLE | Visual confirmation aid only; no extra unit credit. |

No native/layout text, OCR, rendered page, table extraction, workbook extraction, or page image is retained for any DOC-002 page, or for DOC-003 pp. 1, 28-29. These are explicit fresh-source gaps.

## Page manifests, document records, and source-location maps

| Asset path | Type | Direct-source locations covered | Fitness | Classification | Curation use |
|---|---|---|---|---|---|
| `.ai_paper_validation/document_outputs/DOC-001-main-article/page_manifest.json` | Page manifest | DOC-001 PDF pp. 1-11 | Enumerates native path for every page and visual/OCR paths for pp. 1, 3-10. | USABLE | Exact page-to-derivative map. |
| `.ai_paper_validation/document_outputs/DOC-003-supplement-2-results/page_manifest.json` | Page manifest | DOC-003 PDF pp. 1-29 | Accurately identifies retained native pp. 2-27 and visual/OCR pp. 8-27; marks pp. 1, 28-29 as former no-derivative pages. | PARTIAL | Exact gap locator; cannot close pp. 1, 28-29. |
| `.ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol-sap/page_manifest.json` | Page manifest | DOC-002 PDF pp. 1-136 (no usable page entries) | Retained old empty/former-exclusion record; no per-page mapping or extraction. | STALE | Establishes no reusable page coverage only. |
| `.ai_paper_validation/document_outputs/DOC-001-main-article/inventory.md` | Document inventory | DOC-001 PDF pp. 1-11 | Correct source identity/page count and former processing scope. | USABLE | Document identity locator. |
| `.ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol-sap/inventory.md` | Document inventory | DOC-002 PDF pp. 1-136 | Correct source identity/page count but old “not audited” scope is superseded for coverage. | PARTIAL | Identity/page-count locator; not a scope boundary. |
| `.ai_paper_validation/document_outputs/DOC-003-supplement-2-results/inventory.md` | Document inventory | DOC-003 PDF pp. 1-29 | Correct source identity/page count; former result-only scope is incomplete for current coverage. | PARTIAL | Identity/page-count locator; not a scope boundary. |
| `.ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing_status.md` | Processing record | DOC-001 PDF pp. 1-11 | Matches retained derivatives and all-page native coverage. | USABLE | Coverage-method provenance. |
| `.ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol-sap/preprocessing_status.md` | Processing record | DOC-002 PDF pp. 1-136 | Records no retained extraction/render/OCR under old scope. | STALE | Derivative-gap provenance only. |
| `.ai_paper_validation/document_outputs/DOC-003-supplement-2-results/preprocessing_status.md` | Processing record | DOC-003 PDF pp. 1-29 | Correctly records retained pages but old non-audited pp. 1, 28-29 statement is incomplete for current coverage. | PARTIAL | Gap/method provenance; directs fresh mapping for pp. 1, 28-29. |
| `.ai_paper_validation/document_outputs/DOC-001-main-article/main_text_extractor.md` | Existing evidence map | DOC-001 PDF pp. 1, 4, 6-10 and linked derivative locations | Useful page-specific result locator, not a complete page map. | PARTIAL | Locator only; mapper must cover all 11 source pages. |
| `.ai_paper_validation/document_outputs/DOC-003-supplement-2-results/results_supplement_extractor.md` | Existing evidence map | DOC-003 PDF pp. 2, 6-27 and linked derivative locations | Useful page-specific locator. A legacy candidate paragraph is excluded from discovery use. | PARTIAL | Locator only; reuse evidence mapping but independently reconstruct relationships. |
| `.ai_paper_validation/document_outputs/DOC-001-main-article/results_supplement_extractor.md` | Non-applicable document record | None | States that another extractor owns this source; contains no independent evidence. | DUPLICATE | No coverage credit. |
| `.ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol-sap/main_text_extractor.md` | Non-applicable document record | None | States former non-audit; contains no source extraction. | STALE | No coverage credit. |
| `.ai_paper_validation/document_outputs/DOC-002-supplement-1-protocol-sap/results_supplement_extractor.md` | Non-applicable document record | None | States former non-audit; contains no source extraction. | STALE | No coverage credit. |
| `.ai_paper_validation/document_outputs/DOC-003-supplement-2-results/main_text_extractor.md` | Non-applicable document record | None | States another extractor owns this source; contains no independent evidence. | DUPLICATE | No coverage credit. |
| `.ai_paper_validation/package_manifest.yaml` | Package source map | DOC-001 pp. 1-11; DOC-002 pp. 1-136; DOC-003 pp. 1-29 | Correct identities/page counts but retains old scope exclusions. | PARTIAL | Identity and derivative-provenance locator only. |
| `.ai_paper_validation/preprocessing_summary.md` | Package processing summary | DOC-001 pp. 1-11; DOC-002 pp. 1-136; DOC-003 pp. 1-29 | Compact accurate derivative description, but its old “none/not audited” entries do not satisfy current coverage. | PARTIAL | Derivative-gap locator only. |
| `.ai_paper_validation/native_extraction_metrics.json` | Page/source-location map | DOC-001 pp. 1-11; DOC-003 nominally pp. 1-27 | Useful quality metrics for retained pages, but it nominally lists DOC-003 p. 1 although no matching normalized file exists. | STALE | Do not grant p. 1 reusable credit; use only to cross-check retained page quality. |

## Coverage result

Unique unit credit is granted only once per direct page: DOC-001 pp. 1-11 (11 pages) and DOC-003 pp. 2-27 (26 pages), for 37 reusable units. The remaining 139 of 176 direct-source pages are fresh-required: DOC-002 pp. 1-136 and DOC-003 pp. 1, 28-29. No `UNREADABLE` eligible binary/text asset was found; the DOC-002 empty page-manifest entry is classified STALE rather than unreadable because it remains parseable provenance of absent extraction.
