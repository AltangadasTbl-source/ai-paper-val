# Reused Evidence-Asset Inventory

All 232 source-linked reusable artifacts listed in `reused_artifact_hashes_before.sha256` were hashed before mapping. Old candidate, checker, verifier, critic, endetail, and final-report outputs were excluded from this inventory and were not used as scientific-discovery inputs.

| Asset group / path pattern | Files | Exact source-location coverage | Method / content | Fitness | Mapping consequence |
|---|---:|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001/document_record.md through DOC-005/document_record.md | 5 | DOC-001 pp. 1-12; DOC-002 pp. 1-72; DOC-003 pp. 1-54; DOC-004 pp. 1-28; DOC-005 p. 1 | Document identity and prior processing-location record | PARTIAL | Usable as provenance/map only; does not substitute for direct page mapping. |
| .ai_paper_validation/document_outputs/DOC-001/preprocessing_record.json through DOC-005/preprocessing_record.json | 5 | Same respective complete source ranges | Preprocessing scope metadata | PARTIAL | Confirms absent derivatives for DOC-002, DOC-004, and DOC-005; prior scope descriptions do not restrict this run. |
| .ai_paper_validation/preprocessing/page_level_manifest.tsv | 1 | DOC-001 pp. 1-12; DOC-003 pp. 1, 6-53 | Page-to-native/render/OCR location map | PARTIAL | USABLE locator for listed pages; DOC-003 pp. 2-5 and 54 have no row and require fresh mapping. |
| .ai_paper_validation/preprocessing/source_pdf_sha256.txt | 1 | DOC-001 through DOC-005 complete files | Earlier direct-source identity hashes | USABLE | Provenance cross-check only; current hash record is authoritative for this run. |
| .ai_paper_validation/preprocessing/DOC-001/native_pages/page_*.txt | 12 | DOC-001 pp. 1-12 | Native per-page text | USABLE | Reusable coverage for all DOC-001 pages. |
| .ai_paper_validation/preprocessing/DOC-003/native_pages/page_*.txt | 49 | DOC-003 p. 1 and pp. 6-53 | Native per-page text | USABLE | Reusable coverage for these 49 DOC-003 pages. Sparse text on selected table/figure pages remains paired with rendered/OCR assets. |
| .ai_paper_validation/preprocessing/DOC-001/images/page_*.png | 6 | DOC-001 pp. 3-8 | Rendered pages for figure/table visual confirmation | USABLE | Supplemental visual locator for listed pages; native text covers the remaining DOC-001 pages. |
| .ai_paper_validation/preprocessing/DOC-003/images/page_*.png | 48 | DOC-003 pp. 6-53 | Rendered pages for eTables/eFigures | USABLE | Supplemental visual locator for listed pages; native/OCR text is available for page-level mapping. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_pages/page_*.txt | 6 | DOC-001 pp. 3-8 | OCR text derived from corresponding renders | USABLE | Transcription aid only; direct PDF remains confirmation authority. |
| .ai_paper_validation/preprocessing/DOC-003/ocr_pages/page_*.txt | 48 | DOC-003 pp. 6-53 | OCR text derived from corresponding renders | USABLE | Transcription aid only; direct PDF remains confirmation authority. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page_*.json | 6 | DOC-001 pp. 3-8 | OCR provenance and confidence metadata | USABLE | Supports OCR fitness assessment only. |
| .ai_paper_validation/preprocessing/DOC-003/ocr_metadata/page_*.json | 41 | DOC-003 p. 6 and pp. 14-53 | OCR provenance and confidence metadata | PARTIAL | No metadata exists for OCR text on DOC-003 pp. 7-13; those pages remain covered by native text and render/OCR artifacts. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text.txt | 1 | DOC-001 pp. 1-12, without stable page boundaries | Concatenated normalized native text | PARTIAL | Locator only; per-page native assets supply stable coverage. |
| .ai_paper_validation/preprocessing/DOC-003/normalized_text.txt | 1 | DOC-003 p. 1 and pp. 6-53, without stable page boundaries | Concatenated normalized native text | PARTIAL | Locator only; per-page native assets supply stable coverage. |
| .ai_paper_validation/preprocessing/ocr_backend_report.json | 1 | OCR environment provenance, no single source unit | CPU-backend report | STALE | Not used for transcription because per-page metadata records a conflicting earlier GPU selection. |
| .ai_paper_validation/preprocessing/gpu_ocr_backend_report.json | 1 | OCR environment provenance, no single source unit | GPU-backend report | STALE | Not used for transcription; retained only as inconsistent historical provenance. |

No reusable native/layout text, OCR, rendering, table/workbook extraction, or page map was found for DOC-002, DOC-004, or DOC-005. No standalone table extraction, Office workbook extraction, DOC/DOCX map, XLS/XLSX map, or CSV extraction exists in the package. No asset was classified DUPLICATE or UNREADABLE. The conflicting historical backend reports do not invalidate the source-linked OCR text as a locator, but they preclude treating backend metadata as current-run processing provenance.

Reusable source-unit coverage is therefore DOC-001 pp. 1-12 and DOC-003 p. 1 plus pp. 6-53 (61 unique PDF pages). Fresh direct-source mapping is required for DOC-002 pp. 1-72, DOC-003 pp. 2-5 and 54, DOC-004 pp. 1-28, and DOC-005 p. 1 (106 unique PDF pages).
