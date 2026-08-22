# Reused Evidence-Asset Inventory

Inventory timestamp: 2026-08-18T23:20:42Z. This inventory is limited to source-linked reusable OCR/native/normalized text, page images, OCR metadata, document records, manifests, and extraction maps below the existing audit area. Fitness is for discovery and mapping only; the supplied direct source remains authoritative for final confirmation. `DUPLICATE` means the asset adds no source-unit coverage beyond a stronger or byte-identical mapped asset. No reusable layout-text, workbook, spreadsheet, CSV, or Office-extraction asset is present.

Fresh-run native/layout files subsequently created below `.ai_paper_validation/review_1_5_1/preprocessing/` are intentionally not listed or hashed here: they are new direct-source work, not reusable pre-existing artifacts. Their creation alone does not change this pre-mapping ledger.

| Asset path | Asset type and method | Exact source location(s) | Coverage and fitness | Classification | Gap or mapper use |
|---|---|---|---|---|---|
| .ai_paper_validation/document_outputs/package_manifest.json | Document map | DOC-001 pp. 1-9; DOC-002 pp. 1-60; DOC-003 pp. 1-11; DOC-004 pp. 1-3; DOC-005 p. 1 | Complete document identity/page-count map; not page text. | USABLE | Identifies all five direct sources; does not close any page-extraction gap. |
| .ai_paper_validation/preprocessing/page_manifest.json | Page manifest and source-location map | DOC-001 pp. 1-9; DOC-004 pp. 1-3 | Complete for its two listed documents and reports native extraction quality; absent for DOC-002, DOC-003, and DOC-005. | PARTIAL | Reuse for 12 mapped pages; fresh mapping required for DOC-002 pp. 1-60, DOC-003 pp. 1-11, DOC-005 p. 1. |
| .ai_paper_validation/preprocessing/ocr_backend.json | OCR method record | DOC-001 pp. 4-7; DOC-004 pp. 2-3 | CPU-only backend provenance; no source text itself. | USABLE | Supports OCR provenance only. |
| .ai_paper_validation/preprocessing/README.md | Preprocessing scope record | DOC-001 pp. 1-9; DOC-004 pp. 1-3 | Source-linked preprocessing summary consistent with the page manifest; no page text itself. | DUPLICATE | Use only as provenance. |
| .ai_paper_validation/document_outputs/DOC-001/initial_document_record.md | Document record | DOC-001 pp. 1-9 | Complete identity/classification record. | USABLE | Document map only; native page assets provide page evidence. |
| .ai_paper_validation/document_outputs/DOC-001/preprocessing_record.md | Preprocessing record | DOC-001 pp. 1-9 | Complete method/location pointer for native page extraction. | USABLE | Use as provenance pointer. |
| .ai_paper_validation/document_outputs/DOC-001/main_text_extraction.md | Main-article extraction map | DOC-001 pp. 1-9; explicit table locations p. 5 and p. 7 | Summary extraction is source-linked but not a page-complete substitute. | PARTIAL | Native page assets map all pages; use this only as a locator. |
| .ai_paper_validation/document_outputs/DOC-002/initial_document_record.md | Document record | DOC-002 pp. 1-60 | Complete identity/page-count record, without reusable page extraction. | USABLE | Fresh direct-source mapping: pp. 1-60. |
| .ai_paper_validation/document_outputs/DOC-002/preprocessing_record.md | Preprocessing record | DOC-002 pp. 1-60 | Explicitly records no scientific extraction/OCR. | PARTIAL | Fresh direct-source mapping: pp. 1-60. |
| .ai_paper_validation/document_outputs/DOC-003/initial_document_record.md | Document record | DOC-003 pp. 1-11 | Complete identity/page-count record, without reusable page extraction. | USABLE | Fresh direct-source mapping: pp. 1-11. |
| .ai_paper_validation/document_outputs/DOC-003/preprocessing_record.md | Preprocessing record | DOC-003 pp. 1-11 | Explicitly records no scientific extraction/OCR. | PARTIAL | Fresh direct-source mapping: pp. 1-11. |
| .ai_paper_validation/document_outputs/DOC-004/initial_document_record.md | Document record | DOC-004 pp. 1-3 | Complete identity/classification record. | USABLE | Document map only; native page assets provide page evidence. |
| .ai_paper_validation/document_outputs/DOC-004/preprocessing_record.md | Preprocessing record | DOC-004 pp. 1-3 | Complete method/location pointer for native page extraction. | USABLE | Use as provenance pointer. |
| .ai_paper_validation/document_outputs/DOC-004/results_supplement_extraction.md | Results-supplement extraction map | DOC-004 pp. 1-3; eTable p. 2; eFigure p. 3 | Source-linked summary extraction, including visual-check pointer, but not a replacement for the page assets. | PARTIAL | Native text plus page image maps all three pages; use as locator. |
| .ai_paper_validation/document_outputs/DOC-005/initial_document_record.md | Document record | DOC-005 p. 1 | Complete identity/page-count record, without reusable page extraction. | USABLE | Fresh direct-source mapping: p. 1. |
| .ai_paper_validation/document_outputs/DOC-005/preprocessing_record.md | Preprocessing record | DOC-005 p. 1 | Explicitly records no scientific extraction/OCR. | PARTIAL | Fresh direct-source mapping: p. 1. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page-001.txt | Native PDF text | DOC-001 p. 1 | Complete page text; page manifest quality adequate. | USABLE | Reusable page mapping. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page-002.txt | Native PDF text | DOC-001 p. 2 | Complete page text; page manifest quality adequate. | USABLE | Reusable page mapping. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page-003.txt | Native PDF text | DOC-001 p. 3 | Complete page text; page manifest quality adequate. | USABLE | Reusable page mapping. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page-004.txt | Native PDF text | DOC-001 p. 4 | Complete page text; page manifest quality adequate. | USABLE | Reusable page mapping. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page-005.txt | Native PDF text | DOC-001 p. 5 | Complete page text; page manifest quality adequate. | USABLE | Reusable page mapping. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page-006.txt | Native PDF text | DOC-001 p. 6 | Complete page text; page manifest quality adequate. | USABLE | Reusable page mapping. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page-007.txt | Native PDF text | DOC-001 p. 7 | Complete page text; page manifest quality adequate. | USABLE | Reusable page mapping. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page-008.txt | Native PDF text | DOC-001 p. 8 | Complete page text; page manifest quality adequate. | USABLE | Reusable page mapping. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page-009.txt | Native PDF text | DOC-001 p. 9 | Complete page text; page manifest quality adequate. | USABLE | Reusable page mapping. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text/page-001.txt | Normalized page text | DOC-001 p. 1 | Byte-identical to native page text. | DUPLICATE | Native text is the preferred reusable asset. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text/page-002.txt | Normalized page text | DOC-001 p. 2 | Byte-identical to native page text. | DUPLICATE | Native text is the preferred reusable asset. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text/page-003.txt | Normalized page text | DOC-001 p. 3 | Byte-identical to native page text. | DUPLICATE | Native text is the preferred reusable asset. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text/page-004.txt | Normalized page text | DOC-001 p. 4 | Byte-identical to native page text. | DUPLICATE | Native text is the preferred reusable asset. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text/page-005.txt | Normalized page text | DOC-001 p. 5 | Byte-identical to native page text. | DUPLICATE | Native text is the preferred reusable asset. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text/page-006.txt | Normalized page text | DOC-001 p. 6 | Byte-identical to native page text. | DUPLICATE | Native text is the preferred reusable asset. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text/page-007.txt | Normalized page text | DOC-001 p. 7 | Byte-identical to native page text. | DUPLICATE | Native text is the preferred reusable asset. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text/page-008.txt | Normalized page text | DOC-001 p. 8 | Byte-identical to native page text. | DUPLICATE | Native text is the preferred reusable asset. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text/page-009.txt | Normalized page text | DOC-001 p. 9 | Byte-identical to native page text. | DUPLICATE | Native text is the preferred reusable asset. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text.txt | Concatenated normalized text | DOC-001 pp. 1-9 | Page-complete content but page boundaries are less direct than the per-page files. | DUPLICATE | Use per-page native files for exact locations. |
| .ai_paper_validation/preprocessing/DOC-001/page_images/page-004.png | Rendered page image | DOC-001 p. 4 | Direct visual adjunct for native text. | USABLE | Reuse for visual confirmation only. |
| .ai_paper_validation/preprocessing/DOC-001/page_images/page-005.png | Rendered page image | DOC-001 p. 5 | Direct visual adjunct for native text. | USABLE | Reuse for visual confirmation only. |
| .ai_paper_validation/preprocessing/DOC-001/page_images/page-006.png | Rendered page image | DOC-001 p. 6 | Direct visual adjunct for native text. | USABLE | Reuse for visual confirmation only. |
| .ai_paper_validation/preprocessing/DOC-001/page_images/page-007.png | Rendered page image | DOC-001 p. 7 | Direct visual adjunct for native text. | USABLE | Reuse for visual confirmation only. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page-004.json | OCR metadata | DOC-001 p. 4 | Links image and OCR output; mean confidence 0.911. | USABLE | OCR provenance only; native text is preferred. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page-005.json | OCR metadata | DOC-001 p. 5 | Links image and OCR output; mean confidence 0.873. | USABLE | OCR provenance only; native text is preferred. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page-006.json | OCR metadata | DOC-001 p. 6 | Links image and OCR output; mean confidence 0.841. | USABLE | OCR provenance only; native text is preferred. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page-007.json | OCR metadata | DOC-001 p. 7 | Links image and OCR output; mean confidence 0.809. | USABLE | OCR provenance only; native text is preferred. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_text/page-004.txt | OCR text | DOC-001 p. 4 | Secondary transcription where native page text is adequate. | DUPLICATE | Use only for visual-text comparison. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_text/page-005.txt | OCR text | DOC-001 p. 5 | Secondary transcription where native page text is adequate. | DUPLICATE | Use only for visual-text comparison. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_text/page-006.txt | OCR text | DOC-001 p. 6 | Secondary transcription where native page text is adequate. | DUPLICATE | Use only for visual-text comparison. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_text/page-007.txt | OCR text | DOC-001 p. 7 | Secondary transcription where native page text is adequate. | DUPLICATE | Use only for visual-text comparison. |
| .ai_paper_validation/preprocessing/DOC-004/native_text/page-001.txt | Native PDF text | DOC-004 p. 1 | Sparse cover/index text is expected and documented. | USABLE | Reusable page mapping. |
| .ai_paper_validation/preprocessing/DOC-004/native_text/page-002.txt | Native PDF text | DOC-004 p. 2 | eTable text; page manifest quality adequate. | USABLE | Reusable page mapping. |
| .ai_paper_validation/preprocessing/DOC-004/native_text/page-003.txt | Native PDF text | DOC-004 p. 3 | Sparse eFigure title/caption text; source image supplies visual adjunct. | USABLE | Reusable page mapping plus visual confirmation. |
| .ai_paper_validation/preprocessing/DOC-004/normalized_text/page-001.txt | Normalized page text | DOC-004 p. 1 | Byte-identical to native page text. | DUPLICATE | Native text is preferred. |
| .ai_paper_validation/preprocessing/DOC-004/normalized_text/page-002.txt | Normalized page text | DOC-004 p. 2 | Byte-identical to native page text. | DUPLICATE | Native text is preferred. |
| .ai_paper_validation/preprocessing/DOC-004/normalized_text/page-003.txt | Normalized page text | DOC-004 p. 3 | Byte-identical to native page text. | DUPLICATE | Native text is preferred. |
| .ai_paper_validation/preprocessing/DOC-004/normalized_text.txt | Concatenated normalized text | DOC-004 pp. 1-3 | Page-complete content but page boundaries are less direct than per-page files. | DUPLICATE | Use per-page native files for exact locations. |
| .ai_paper_validation/preprocessing/DOC-004/page_images/page-002.png | Rendered page image | DOC-004 p. 2 | Direct visual adjunct for eTable. | USABLE | Reuse for visual confirmation. |
| .ai_paper_validation/preprocessing/DOC-004/page_images/page-003.png | Rendered page image | DOC-004 p. 3 | Direct visual adjunct for eFigure. | USABLE | Reuse for visual confirmation. |
| .ai_paper_validation/preprocessing/DOC-004/page_images/rendered_page-003.png | Rendered page image | DOC-004 p. 3 | Explicitly source-mapped by the results-supplement extraction map. | DUPLICATE | Use either p. 3 image for visual confirmation. |
| .ai_paper_validation/preprocessing/DOC-004/page_images/rendered_page.png | Rendered page image | No exact source page recorded | Filename and surrounding records do not establish a truthful page identity. | UNREADABLE | Do not use; it adds no coverage. |
| .ai_paper_validation/preprocessing/DOC-004/ocr_metadata/page-002.json | OCR metadata | DOC-004 p. 2 | Links image and OCR output; mean confidence 0.812. | USABLE | OCR provenance only; native text is preferred. |
| .ai_paper_validation/preprocessing/DOC-004/ocr_metadata/page-003.json | OCR metadata | DOC-004 p. 3 | Links image and OCR output; mean confidence 0.745. | USABLE | OCR provenance only; use page image for visual confirmation. |
| .ai_paper_validation/preprocessing/DOC-004/ocr_text/page-002.txt | OCR text | DOC-004 p. 2 | Secondary transcription where native table text is adequate. | DUPLICATE | Use only for visual-text comparison. |
| .ai_paper_validation/preprocessing/DOC-004/ocr_text/page-003.txt | OCR text | DOC-004 p. 3 | Secondary caption/graphic transcription; lower-confidence OCR. | PARTIAL | Page image/direct PDF required for any figure-value transcription. |

## Excluded legacy content

The following pre-existing files were neither read nor used as scientific discovery scope and were not treated as reusable evidence assets: `ai_training_restriction_record.md`, `figure_flow_checker.md`, `table_arithmetic_checker.md`, `statistical_consistency_candidates.md`, `evidence_verification.md`, `critic_review.md`, and any final or human-adjudication report. Their names indicate legacy restrictions, candidate/checker, verification, critic, or final-report content.

## Coverage outcome

Usable reusable source-unit coverage is DOC-001 pages 1-9 and DOC-004 pages 1-3, for 12 unique pages. The complete fresh direct-source gap is DOC-002 pages 1-60, DOC-003 pages 1-11, and DOC-005 page 1, for 72 unique pages. The unidentified `rendered_page.png` is an asset-level limitation only; it does not create a source-unit gap because DOC-004 page 3 has other mapped native and rendered assets.
