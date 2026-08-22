# Reusable Evidence-Asset Inventory

All paths are package-relative. “Coverage” names exact source PDF pages. Fitness refers to suitability as a source-linked locator/transcription aid; direct PDFs remain the final authority. This inventory excludes legacy candidate, verifier, critic, adjudication, and final-report artifacts from reuse.

| Asset group and paths | Asset type | Source mapping | Coverage and fitness | Reuse decision |
|---|---|---|---|---|
| `.ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-001.txt` through `page-012.txt` | Native PDF text | DOC-001 PDF pp. 1-12, one file per identically numbered page | USABLE. All 12 pages are page-addressable and manifest quality is satisfactory. | Designate as primary reusable text for DOC-001. |
| `.ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-001.txt` through `page-012.txt` | Normalized native text | DOC-001 PDF pp. 1-12, one file per identically numbered page | DUPLICATE. Page-linked normalized rendition of the usable native text; no independent evidence coverage. | Retain as optional locator only; do not count additional coverage. |
| `.ai_paper_validation/preprocessing/jama2019-14231-main-article/images/page-003.png`, `page-005.png` through `page-010.png` | Rendered pages | DOC-001 PDF pp. 3, 5, 6, 7, 8, 9, 10 | USABLE. Visual confirmation for result-relevant figures/tables/flow diagram on exactly the named pages. | Reuse for visual confirmation only; native text remains primary. |
| `.ai_paper_validation/preprocessing/jama2019-14231-main-article/ocr_text/page-003.txt` and `ocr_metadata/page-003.json` | OCR text and OCR metadata | DOC-001 PDF p. 3 | USABLE. CPU RapidOCR cross-check for participant-flow diagram; metadata reports mean confidence 0.9104. | Reuse as a page-3 visual-text locator; confirm direct PDF if cited. |
| `.ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-006.txt` through `page-020.txt` | Native PDF text | DOC-002 PDF pp. 6-20, one file per identically numbered page | USABLE. All 15 selected pages are page-addressable and manifest quality is satisfactory. | Designate as primary reusable text for DOC-002 pp. 6-20. |
| `.ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-006.txt` through `page-020.txt` | Normalized native text | DOC-002 PDF pp. 6-20, one file per identically numbered page | DUPLICATE. Page-linked normalized rendition of the usable native text; no independent evidence coverage. | Retain as optional locator only; do not count additional coverage. |
| `.ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-006.png` through `page-016.png`, and `page-018.png` through `page-020.png` | Rendered pages | DOC-002 PDF pp. 6-16 and 18-20 | USABLE. Visual references exist for 14 exact pages. The lack of a render for p. 17 is not a coverage gap because usable native text exists for p. 17. | Reuse for visual confirmation on named pages only. |
| `.ai_paper_validation/preprocessing/page_manifest.json` | Page manifest/source-location map | DOC-001 PDF pp. 1-12; DOC-002 PDF pp. 6-20; no DOC-003 page record | PARTIAL. It precisely maps existing page-level derivatives, but records an older bounded scope and has no page records for DOC-002 pp. 1-5 or DOC-003 pp. 1-7. | Reuse for derivative provenance and exact page mapping; do not use it to limit coverage. |
| `.ai_paper_validation/preprocessing/ocr_backend.json` | OCR backend record | DOC-001 PDF p. 3 only, via page manifest | USABLE. CPU-only backend provenance for the existing OCR asset; it does not independently transcribe a source page. | Reuse as OCR provenance only. |
| `.ai_paper_validation/document_outputs/package_manifest.json` | Package document map | DOC-001 PDF pp. 1-12; DOC-002 PDF pp. 1-20; DOC-003 PDF pp. 1-7 | PARTIAL. Correctly identifies three documents and page totals, but applies an older scientific scope. | Reuse for document identity/page counts only. |
| `.ai_paper_validation/document_outputs/jama2019-14231-main-article/document_record.json` | Document record | DOC-001 PDF pp. 1-12 | PARTIAL. Source hash and page count match the current direct PDF; record describes full native-text coverage but is not a complete page transcript. | Reuse for identity/provenance only. |
| `.ai_paper_validation/document_outputs/jama2019-14231-supplement-1/document_record.json` | Document record | DOC-002 PDF pp. 1-20; derivative coverage only pp. 6-20 | PARTIAL. Source hash and page count match; prior page selection is incomplete for the current review. | Reuse for identity/provenance only. |
| `.ai_paper_validation/document_outputs/jama2019-14231-supplement-2/document_record.json` | Document record | DOC-003 PDF pp. 1-7 | PARTIAL. Source hash and page count match but no page extraction was retained. | Reuse for identity/provenance only; assign all pages fresh. |
| `.ai_paper_validation/document_outputs/jama2019-14231-main-article/main_text_extraction.json` and `main_text_extraction.md` | Native/table-oriented source-location extraction | DOC-001 PDF pp. 1-12 | USABLE. Paired source-linked map names page/table/figure locations across all main-article pages; source hash matches. | Reuse as a location map, not as an old finding set. |
| `.ai_paper_validation/document_outputs/jama2019-14231-supplement-1/results_evidence_map.md` | Results source-location/table extraction | DOC-002 PDF pp. 6-20 | USABLE. Page-linked map covers each page 6-20, including eTables/eFigures and comparators; source hash matches through the associated record. | Reuse as a location map, not as an old finding set. |

## Asset count and gap assessment

- Eligible reusable artifacts inventoried: 86 files: 27 native-text files, 27 normalized-text files, 21 rendered pages, 1 OCR-text file, 1 OCR metadata file, 1 OCR backend record, 1 page manifest, 4 document/package records, and 3 source-location extraction/map files. The 59 assets designated for active reuse are hashed; the 27 normalized files are classified as duplicate optional locators and are not designated for use.
- USABLE artifact groups provide direct reusable page coverage for DOC-001 pp. 1-12 and DOC-002 pp. 6-20: 27 unique source pages.
- DUPLICATE normalized-text files add no source-page coverage beyond native text.
- PARTIAL provenance/map assets identify the historical bounded scope but do not close current-review coverage gaps.
- STALE assets: none identified; document-record source hashes match the direct-source digests. UNREADABLE assets: none identified. No workbook, CSV, or Office/table-extraction asset exists in this package.
- Fresh direct-source extraction and mapping assignments: DOC-002 PDF pp. 1-5; DOC-003 PDF pp. 1-7. These 12 units must not be omitted because an older record labeled them outside its prior audit scope.

## Curation commands and versions

- `find .ai_paper_validation -type f` to enumerate audit-area files without scanning sibling packages.
- `sha256sum -- <designated reusable artifact>`: SHA-256 digests for all 59 actively reused assets are recorded in `reused_artifact_hashes_before.sha256`.
- `pdfinfo` / `pdftotext`: Poppler `26.01.0` as recorded in `source_inventory.md`.
- No conversion, OCR, rendering, Office extraction, or source/derivative modification was performed in this stage.
