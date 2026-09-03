# Reused Evidence-Asset Inventory

Inventory scope is `.ai_paper_validation/document_outputs/` only. Sixty pre-existing files were found and snapshotted in `reused_artifact_hashes_before.sha256`. This inventory does not use any legacy candidate, checker, verifier, critic, queue, endetail, or final-report content as scientific input.

Fitness terminology: `USABLE` means source-linked and page-addressable for current mapping; `PARTIAL` means usable only for the named pages; `STALE` means preserved provenance that is not reused for 1.5.1 scientific mapping; `DUPLICATE` means redundant to page-level assets; `UNREADABLE` means not fit for reliable reuse.

## DOC-001 — jama_zahid_2025_oi_250093_1768590553.08463.pdf

| Asset class and exact relative paths | Source location(s) | Method / fitness | Disposition |
|---|---|---|---|
| `document_outputs/DOC-001/preprocessing_page_manifest.json`; `document_outputs/DOC-001/preprocessing_record.md` | PDF pp. 1-9 | Page manifest and preprocessing record identify native-first extraction, page paths, quality, and image/OCR supplements. `USABLE`. | Reuse as source-location map for pp. 1-9. |
| `document_outputs/DOC-001/normalized_text/page-001.txt` through `page-009.txt` | PDF pp. 1-9 respectively | Native normalized text; p. 4 is native-plus-OCR with a locally joined-word limitation; remaining pages are recorded high quality. `USABLE` at page level. | Reuse for all 9 pages, with direct-source confirmation; p. 4 also has visual/OCR support. |
| `document_outputs/DOC-001/normalized_text/document-normalized.txt` | PDF pp. 1-9 | Concatenated duplicate of the page-level normalized-text coverage. `DUPLICATE`. | Do not use as the primary locator. |
| `document_outputs/DOC-001/page_images/page-004.png` through `page-007.png` | PDF pp. 4-7 respectively | 2550x3300 rendered PNGs for flow/table/figure visual confirmation. `PARTIAL` because only pp. 4-7 are rendered. | Reuse for visual confirmation on the four named pages. |
| `document_outputs/DOC-001/ocr_text/page-004.txt` | PDF p. 4 | OCR supplement for the locally joined native run. `PARTIAL`. | Reuse only as an aid alongside p. 4 image and direct PDF. |
| `document_outputs/DOC-001/inventory.md`; `document_outputs/DOC-001/processing_status.md` | Document-level | Legacy document records. `STALE` for current scope because they include old workflow status. | Preserve; use neither for discovery nor coverage decisions. |
| `document_outputs/DOC-001/main_text_extractor_response.md` | Document-level, no complete current page map established | Legacy extractor response. `STALE`. | Preserve; contents not used. |

## DOC-002 — joi250093supp1_prod_1768590553.08963.pdf

| Asset class and exact relative paths | Source location(s) | Method / fitness | Disposition |
|---|---|---|---|
| `document_outputs/DOC-002/inventory.md`; `document_outputs/DOC-002/processing_status.md` | Document-level only | Legacy inventory/status records state no page-level preprocessing. They contain no reusable native, layout, OCR, rendered-page, table, or page-map asset. `STALE`. | Preserve only; all PDF pp. 1-109 require fresh direct-source mapping. |

## DOC-003 — joi250093supp2_prod_1768590553.09463.pdf

| Asset class and exact relative paths | Source location(s) | Method / fitness | Disposition |
|---|---|---|---|
| `document_outputs/DOC-003/preprocessing_page_manifest.json`; `document_outputs/DOC-003/preprocessing_record.md` | PDF pp. 3-16 | Page manifest and preprocessing record identify native-first source linkage and every page asset. They explicitly omit pp. 1-2. `PARTIAL`. | Reuse as source-location map for pp. 3-16; assign pp. 1-2 fresh. |
| `document_outputs/DOC-003/normalized_text/page-003.txt` through `page-016.txt` | PDF pp. 3-16 respectively | Native normalized text. Pages 7, 14, and 16 are sparse/moderate and have OCR/image support; other named pages are high quality. `USABLE` at page level. | Reuse for pp. 3-16 with direct-source confirmation. |
| `document_outputs/DOC-003/normalized_text/document-normalized.txt` | PDF pp. 3-16 | Concatenated duplicate of the page-level normalized-text coverage. `DUPLICATE`. | Do not use as the primary locator. |
| `document_outputs/DOC-003/page_images/page-003.png` through `page-016.png` | PDF pp. 3-16 respectively | 2550x3300 rendered PNG pages for tables and eFigure. `USABLE` at page level. | Reuse for visual confirmation on pp. 3-16. |
| `document_outputs/DOC-003/ocr_text/page-007.txt`; `document_outputs/DOC-003/ocr_text/page-014.txt`; `document_outputs/DOC-003/ocr_text/page-016.txt` | PDF pp. 7, 14, 16 | OCR supplements for sparse native extraction. `PARTIAL`. | Reuse only on the named pages alongside image/direct PDF. |
| `document_outputs/DOC-003/rights_footer_page1.png` | PDF p. 1 footer only | Cropped footer image; it does not cover p. 1 content. `PARTIAL`. | Not sufficient for p. 1; direct-source fresh extraction remains assigned. |
| `document_outputs/DOC-003/inventory.md`; `document_outputs/DOC-003/processing_status.md` | Document-level | Legacy document records; prior scope omitted pp. 1-2. `STALE`. | Preserve; current coverage is determined from direct source and page manifest, not legacy scope. |
| `document_outputs/DOC-003/results_supplement_extractor_response.md` | Document-level, no complete current page map established | Legacy extractor response. `STALE`. | Preserve; contents not used. |

## Coverage and limitations

There are no reusable table-extraction, workbook-extraction, layout-text, CSV, DOC, or DOCX assets in this directory. The usable reusable evidence is page-addressable native normalized text for DOC-001 pp. 1-9 and DOC-003 pp. 3-16, with rendered-page support for DOC-001 pp. 4-7 and DOC-003 pp. 3-16. Fresh direct-source extraction is required for every DOC-002 page and DOC-003 pp. 1-2. The garbled native first-page probe of DOC-002 confirms that fresh mapping should use page-selected direct extraction and targeted visual/OCR support as necessary; it does not reduce its 109-page requirement.

The coordinator's current-run DOC-002 layout and rendered/OCR outputs under `review_1_5_1/preprocessing/DOC-002`, and the current-run DOC-003 pp. 1-2 layout text, are fresh derivatives rather than existing reusable assets. They are outside this before-reuse hash snapshot and remain assigned to downstream fresh-source mapping.
