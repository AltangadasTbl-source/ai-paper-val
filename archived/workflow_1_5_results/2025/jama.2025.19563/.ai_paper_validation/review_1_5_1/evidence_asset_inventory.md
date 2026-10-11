# Reused Evidence-Asset Inventory — Workflow 1.5.1

## Method and integrity

The existing audit area was inventoried by path and file type without reading old candidate, verifier, critic, endetail, quality, or final-report outputs. Every eligible existing OCR/native text, rendered page, page manifest, document record, and source-location/evidence map is hashed in `reused_artifact_hashes_before.sha256` (127 files). The direct source is authoritative; all assets below are locators or transcription/visual aids.

`USABLE` means source-linked and usable for its stated units. `PARTIAL` means usable only for the named units and creates explicit fresh work elsewhere. `DUPLICATE` means an aggregate repeats individual hashed assets and supplies no independent coverage. No eligible asset was unreadable; no source-identity mismatch was observed, so no eligible asset was classified `STALE`.

## Page manifests and document maps

| Asset path(s) | Asset class | Exact source locations | Fitness | Coverage and use limitation |
|---|---|---|---|---|
| `.ai_paper_validation/pdf_preprocessing_manifest.json` | Page-level source-location map | DOC-001 pp. 1-11; DOC-003 pp. 34-35, 38-66 | PARTIAL | Maps 42 individual page extractions and 36 visual companions. It explicitly has no DOC-002 page records and no DOC-003 records outside the named pages. |
| `.ai_paper_validation/pdf_preprocessing_manifest.md` | Human-readable page manifest | DOC-001 pp. 1-11; DOC-003 pp. 34-35, 38-66 | PARTIAL | Narrative companion of the JSON page manifest; incomplete for current 170-page scope. |
| `.ai_paper_validation/package_manifest.json` | Source/document map | DOC-001 pp. 1-11; DOC-002 pp. 1-90 identity only; DOC-003 pp. 1-69 identity with old selected subset | PARTIAL | Identifies all three PDFs and page counts, but its old audit scope is not a current coverage boundary. |
| `.ai_paper_validation/package_manifest.md` | Source/document map | DOC-001 pp. 1-11; DOC-002 pp. 1-90 identity only; DOC-003 pp. 1-69 identity with old selected subset | PARTIAL | Human-readable companion; use only for provenance/locator information. |
| `.ai_paper_validation/document_outputs/DOC-001-main-article/document_record.md` | Document record | DOC-001 pp. 1-11 | PARTIAL | Identifies the source and points to the page manifest; it does not replace individual page assets. |
| `.ai_paper_validation/document_outputs/DOC-002-protocol/document_record.md` | Document record | DOC-002 pp. 1-90 identity; no individual page mapping | PARTIAL | Establishes 90 pages and warns that sampled native extraction is glyph-encoded. It leaves all pp. 1-90 fresh-required. |
| `.ai_paper_validation/document_outputs/DOC-003-results-supplement/document_record.md` | Document record | DOC-003 pp. 34-35, 38-66 | PARTIAL | Identifies the 31 page-level assets only; pp. 1-33, 36-37, and 67-69 remain fresh-required. |

## Native text assets

| Asset path(s) | Asset class | Exact source locations | Fitness | Coverage and use limitation |
|---|---|---|---|---|
| `.ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native/page-001.txt` through `page-011.txt` | Per-page native text (11 files) | DOC-001 PDF pp. 1-11, one same-numbered file per page | USABLE | The manifest records readable native extraction with no replacement characters. Use as a locator/transcription aid; visually confirm table/figure layout where needed. |
| `.ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/native_all_selected_pages.txt` | Aggregate native text | DOC-001 PDF pp. 1-11 | DUPLICATE | Concatenates the 11 individual native-text files; it does not add coverage. |
| `.ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native/page-034.txt`, `page-035.txt`, and `page-038.txt` through `page-066.txt` | Per-page native text (31 files) | DOC-003 PDF pp. 34-35 and 38-66, one same-numbered file per page | USABLE | The page manifest records usable native extraction. It covers only 31/69 pages and table layout can be flattened. |
| `.ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/native_all_selected_pages.txt` | Aggregate native text | DOC-003 PDF pp. 34-35 and 38-66 | DUPLICATE | Concatenates the 31 individual native-text files; it does not add coverage. |

## OCR and rendered-page assets

| Asset path(s) | Asset class | Exact source locations | Fitness | Coverage and use limitation |
|---|---|---|---|---|
| `.ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/ocr/page-005.txt` through `page-009.txt` | Per-page OCR text (5 files) | DOC-001 PDF pp. 5-9 | USABLE | Companion OCR for visual flow/table/figure pages; native text remains primary where readable. |
| `.ai_paper_validation/document_outputs/DOC-001-main-article/normalized_text/ocr_all_selected_visual_pages.txt` | Aggregate OCR text | DOC-001 PDF pp. 5-9 | DUPLICATE | Concatenates individual OCR companions. |
| `.ai_paper_validation/document_outputs/DOC-001-main-article/page_images/page-005.png` through `page-009.png` | Rendered page images (5 files) | DOC-001 PDF pp. 5-9 | USABLE | Visual confirmation aid for labels, table alignment, figure values, and flow arrows. |
| `.ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr/page-034.txt`, `page-035.txt`, and `page-038.txt` through `page-066.txt` | Per-page OCR text (31 files) | DOC-003 PDF pp. 34-35 and 38-66 | USABLE | Companion OCR for each reused supplement page; compare with the paired rendered image when layout is material. |
| `.ai_paper_validation/document_outputs/DOC-003-results-supplement/normalized_text/ocr_all_selected_visual_pages.txt` | Aggregate OCR text | DOC-003 PDF pp. 34-35 and 38-66 | DUPLICATE | Concatenates the individual OCR companions. |
| `.ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-034.png`, `page-035.png`, and `page-038.png` through `page-066.png` | Rendered page images (31 files) | DOC-003 PDF pp. 34-35 and 38-66 | USABLE | Visual confirmation aid for eFigures/eTables on the named pages only. |

## Existing table/evidence maps

| Asset path | Asset class | Exact source locations | Fitness | Coverage and use limitation |
|---|---|---|---|---|
| `.ai_paper_validation/document_outputs/DOC-001-main-article/main_text_extractor_evidence.md` | Source-location/evidence map | DOC-001 PDF pp. 1-11; table/figure references chiefly pp. 5-9 | PARTIAL | Structured locator for results-oriented content on an otherwise fully page-reused document. It is not an independent table extraction and must not replace direct-source confirmation. |
| `.ai_paper_validation/document_outputs/DOC-003-results-supplement/results_supplement_extractor_response.md` | Source-location/evidence map | DOC-003 PDF pp. 34-35 and 38-66 | PARTIAL | Structured locator for the same 31 reused pages. It has no mapping for DOC-003 pp. 1-33, 36-37, or 67-69. |

## Asset counts and coverage conclusion

| Asset family | Files hashed | Unit coverage contributed |
|---|---:|---|
| Page/document/source maps and document records | 7 | Provenance for all sources; page-level mapping only for 42 pages |
| Per-page native text | 42 | DOC-001 pp. 1-11; DOC-003 pp. 34-35, 38-66 |
| Aggregate native text | 2 | Duplicate only |
| Per-page OCR text | 36 | DOC-001 pp. 5-9; DOC-003 pp. 34-35, 38-66 |
| Aggregate OCR text | 2 | Duplicate only |
| Rendered page images | 36 | DOC-001 pp. 5-9; DOC-003 pp. 34-35, 38-66 |
| Existing evidence/source-location maps | 2 | Locator-only support for their named reused scopes |
| **Total eligible reused files** | **127** | **42 unique source pages reusable; 128 unique pages fresh-required** |

There are no existing layout-text assets, standalone table/workbook extractions, Office structure extracts, or CSV extracts in the audit area. `.ai_paper_validation/run_pdf_preprocessor.py` is a preprocessing utility rather than a reusable evidence asset and was not hashed as evidence.
