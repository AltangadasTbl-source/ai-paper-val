# Reusable Evidence-Asset Inventory

This inventory excludes legacy candidate ledgers, checker outputs, verifier/critic/quality outputs, endetail content, and final reports from discovery scope. All listed files are preserved unchanged. Fitness is for source location, mapping, or transcription assistance; the direct source remains authoritative.

## Asset classes and counts

| Fitness | Asset count |
|---|---:|
| USABLE | 56 |
| PARTIAL | 5 |
| STALE | 2 |
| DUPLICATE | 11 |
| UNREADABLE | 0 |
| **Total inventoried reusable assets** | **74** |

## Document records, manifests, and source maps

| Asset path | Exact source coverage | Method | Fitness | Gap or limitation |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/package_manifest.md | DOC-001 pp. 1-10; DOC-002 pp. 1-7; DOC-003 pp. 1-29 | Prior package inventory | PARTIAL | Page identities/counts are usable; prior study-linkage and audit-scope conclusions are not reused. |
| .ai_paper_validation/document_outputs/DOC-001/document_record.md | DOC-001 pp. 1-10 | Document record | STALE | Its preprocessing update conflicts with present OCR files for pp. 7-9. |
| .ai_paper_validation/document_outputs/DOC-002/document_record.md | DOC-002 pp. 1-7 | Document record | PARTIAL | Identity and heading map usable; prior scope decision is not reused. |
| .ai_paper_validation/document_outputs/DOC-003/document_record.md | DOC-003 pp. 1-29 | Document record | PARTIAL | Identity and contents map usable; prior scope decision is not reused. |
| .ai_paper_validation/preprocessing/DOC-001/page_manifest.json | DOC-001 pp. 1-10 | Page-level extraction manifest | STALE | OCR absence/incompletion claims for pp. 7-9 conflict with retained OCR text and metadata. |
| .ai_paper_validation/preprocessing/ocr_backend.json | DOC-001 pp. 3, 5-9 | OCR provenance metadata | USABLE | Provenance only; no source transcription. |
| .ai_paper_validation/review_1_3_1/extraction/main_quantitative_evidence.md | DOC-001 pp. 1-10 | Source-linked reusable quantitative evidence map | USABLE | Reusable map only; direct PDF remains final authority. |
| .ai_paper_validation/review_1_3_1/extraction/support_quantitative_evidence.md | DOC-002 pp. 1-7; DOC-003 pp. 1-29 | Source-linked reusable quantitative evidence map | USABLE | Reusable map only; direct PDF remains final authority. |

## DOC-001 native and normalized text

| Assets | Exact source pages | Method | Fitness | Gap or limitation |
|---|---|---|---|---|
| .ai_paper_validation/preprocessing/DOC-001/native_text/page-01.txt through page-07.txt; page-09.txt; page-10.txt | DOC-001 PDF pp. 1-7, 9-10 | Per-page native layout text | USABLE | Table/figure geometry on pp. 3 and 5-9 still requires source-page visual confirmation. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page-08.txt | DOC-001 PDF p. 8 | Per-page native layout text | PARTIAL | Over-expanded table reading order; use retained render/OCR and source page. |
| .ai_paper_validation/preprocessing/DOC-001/normalized_text/page-01.txt through page-10.txt | DOC-001 PDF pp. 1-10 | Terminal-form-feed-normalized copies of native text | DUPLICATE | Adds no source content; p. 8 retains the native-text defect. |

## DOC-001 renders, OCR text, and OCR metadata

| Assets | Exact source pages | Method | Fitness | Gap or limitation |
|---|---|---|---|---|
| .ai_paper_validation/preprocessing/DOC-001/page_images/page-03.png, page-05.png, page-06.png, page-07.png, page-08.png, page-09.png | DOC-001 PDF pp. 3, 5-9 | Rendered source pages | USABLE | p. 8 is lower resolution; inspect direct PDF for final confirmation. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_text/page-03.txt, page-05.txt, page-06.txt, page-07.txt, page-08.txt, page-09.txt | DOC-001 PDF pp. 3, 5-9 | RapidOCR CPU transcription | USABLE | Transcription aid only; direct PDF controls. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page-03.json, page-05.json, page-06.json, page-07.json, page-08.json, page-09.json | DOC-001 PDF pp. 3, 5-9 | Per-page OCR provenance/confidence record | USABLE | Metadata only. |

## Full-document layout text

| Asset path | Exact source coverage | Method | Fitness | Gap or limitation |
|---|---|---|---|---|
| .ai_paper_validation/rights_screen/jama_flint_2019_oi_190079.txt | DOC-001 pp. 1-10 | Full-document native layout text with form-feed page boundaries | DUPLICATE | Concatenates the per-page native text. |
| .ai_paper_validation/rights_screen/joi180151supp1_prod.txt | DOC-002 pp. 1-7 | Full-document native layout text with form-feed page boundaries | USABLE | No page-image derivative; direct PDF supplies visual check. |
| .ai_paper_validation/rights_screen/joi180151supp2_prod.txt | DOC-003 pp. 1-29 | Full-document native layout text with form-feed page boundaries | PARTIAL | Table/figure geometry is incomplete on visual material; retained renders supplement pp. 7-26. |

## DOC-003 rendered pages and OCR text

| Assets | Exact source pages | Method | Fitness | Gap or limitation |
|---|---|---|---|---|
| .ai_paper_validation/review_1_3_1/preprocessing/support_pages/doc003-07.png through doc003-21.png | DOC-003 PDF pp. 7-21 | Rendered source pages | USABLE | Visual locator only; direct PDF controls. |
| .ai_paper_validation/review_1_3_1/preprocessing/support_pages/doc003-22.png through doc003-26.png | DOC-003 PDF pp. 22-26 | Rendered source pages | USABLE | Visual locator only; direct PDF controls. |
| .ai_paper_validation/review_1_3_1/preprocessing/support_pages/doc003-22-ocr.txt through doc003-26-ocr.txt | DOC-003 PDF pp. 22-26 | Targeted Tesseract OCR of embedded forest-plot text | USABLE | Transcription aid only; direct PDF controls. |

## Coverage fitness and explicit gap disposition

The asset set contains no Office/table/workbook extraction because no Office or workbook direct source exists. The two reusable quantitative evidence maps cover all direct-source pages, so their source-location maps provide complete reusable coverage. The remaining derivative limitations are: DOC-001 p. 8 native-text reading order, DOC-003 table/figure layout in full-document text, and stale DOC-001 manifest/record OCR statements. Each limitation has a usable accompanying source-linked map or rendered/OCR support and therefore leaves no fresh-required source unit. Downstream mappers must treat the direct PDF page as authority and directly confirm any value used in a candidate.
