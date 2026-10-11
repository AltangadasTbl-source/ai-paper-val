# Reusable evidence asset inventory

Every eligible extraction, rendered page, source-identity record and page map found below the prior audit area is listed separately below. The inventory excludes all legacy scientific conclusions, candidate/checker/screening/recheck/critic/quality/report artifacts. No table/workbook extraction or Office evidence asset was found. Eligible assets are selected as read-only transcription, visual or identity aids; identical copies are explicitly marked DUPLICATE and do not increase page coverage. All listed assets are hashed for preservation and are available to downstream agents. No scripts are executed from the legacy audit area.

Fitness is functional: USABLE means a current-source-matched extraction or complete image/map for its specified units; PARTIAL means sparse chart text or a legacy scope-limited identity record, which requires the other named evidence to complete reuse; DUPLICATE means byte-identical to an earlier listed asset. No stale or unreadable asset was found. Main/protocol/data-statement native text is nonempty; plot native text is sparse and PARTIAL, with USABLE full-page images for each affected page.

Engine provenance: legacy document_outputs and matching preprocessing native text used PyMuPDF (`fitz`, sort=True); 300-dpi rendered pages used PyMuPDF. Their OCR used rapidocr_onnxruntime with rapidocr-cuda, onnxruntime 1.28.0; that is retained historical provenance, not a GPU operation in this CPU run. Normalized text combines native and targeted OCR according to the page manifests. review_1_5_1 native/layout text used direct Poppler pdftotext; the full 42-page protocol layout, pp. 22-42 layout, and data-statement native text are byte-identical to current direct pdftotext 26.01.0 output. Other legacy review images have unspecified original rendering engine, are usable as page locators, and never override the direct source.

Commands in this curation: `rg --files --hidden .`, `pdfinfo`, `pdftotext -f 1 -l 2 <source> -`, `pdftotext -layout <source> - | cmp - <asset>`, `pdftotext -layout -f 22 -l 42 <source> - | cmp - <asset>`, `pdftotext <data-statement> - | cmp - <asset>`, `file <image>`, and `sha256sum`. Direct pdfinfo/pdftotext version 26.01.0; sha256sum uutils coreutils 0.10.0. Outputs are source_inventory.md, source_coverage.md, this inventory and the before-hash manifests. No new extraction, rendering or OCR derivative was produced by the curator.

| Asset path | Source ID | Exact source units | Asset kind / engine | Fitness | Coverage note |
|---|---|---|---|---|---|
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/document_record.yaml | DOC-001 | PDF pp. 1-10 | source identity record | PARTIAL | Identity/hash reusable; legacy audit restrictions have no effect |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/native_extraction_quality.json | DOC-001 | PDF pp. 1-10 | metadata | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-001.txt | DOC-001 | PDF p. 1 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-002.txt | DOC-001 | PDF p. 2 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-003.txt | DOC-001 | PDF p. 3 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-004.txt | DOC-001 | PDF p. 4 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-005.txt | DOC-001 | PDF p. 5 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-006.txt | DOC-001 | PDF p. 6 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-007.txt | DOC-001 | PDF p. 7 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-008.txt | DOC-001 | PDF p. 8 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-009.txt | DOC-001 | PDF p. 9 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-010.txt | DOC-001 | PDF p. 10 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-001.txt | DOC-001 | PDF p. 1 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-002.txt | DOC-001 | PDF p. 2 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-003.txt | DOC-001 | PDF p. 3 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-004.txt | DOC-001 | PDF p. 4 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-005.txt | DOC-001 | PDF p. 5 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-006.txt | DOC-001 | PDF p. 6 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-007.txt | DOC-001 | PDF p. 7 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-008.txt | DOC-001 | PDF p. 8 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-009.txt | DOC-001 | PDF p. 9 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-010.txt | DOC-001 | PDF p. 10 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-003.json | DOC-001 | PDF p. 3 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-005.json | DOC-001 | PDF p. 5 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-006.json | DOC-001 | PDF p. 6 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-007.json | DOC-001 | PDF p. 7 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-008.json | DOC-001 | PDF p. 8 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-009.json | DOC-001 | PDF p. 9 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-003.txt | DOC-001 | PDF p. 3 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-005.txt | DOC-001 | PDF p. 5 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-006.txt | DOC-001 | PDF p. 6 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-007.txt | DOC-001 | PDF p. 7 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-008.txt | DOC-001 | PDF p. 8 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-009.txt | DOC-001 | PDF p. 9 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/page_level_manifest.json | DOC-001 | PDF pp. 1-10 | page/source-location manifest | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-003.png | DOC-001 | PDF p. 3 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-005.png | DOC-001 | PDF p. 5 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-006.png | DOC-001 | PDF p. 6 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-007.png | DOC-001 | PDF p. 7 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-008.png | DOC-001 | PDF p. 8 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-009.png | DOC-001 | PDF p. 9 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D02/document_record.yaml | DOC-002 | PDF pp. 1-42 | source identity record | PARTIAL | Identity/hash reusable; legacy audit restrictions have no effect |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/document_record.yaml | DOC-003 | PDF pp. 1-10 | source identity record | PARTIAL | Identity/hash reusable; legacy audit restrictions have no effect |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/native_extraction_quality.json | DOC-003 | PDF pp. 1-10 | metadata | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-001.txt | DOC-003 | PDF p. 1 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-002.txt | DOC-003 | PDF p. 2 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-003.txt | DOC-003 | PDF p. 3 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-004.txt | DOC-003 | PDF p. 4 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-005.txt | DOC-003 | PDF p. 5 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-006.txt | DOC-003 | PDF p. 6 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-007.txt | DOC-003 | PDF p. 7 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-008.txt | DOC-003 | PDF p. 8 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-009.txt | DOC-003 | PDF p. 9 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-010.txt | DOC-003 | PDF p. 10 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-001.txt | DOC-003 | PDF p. 1 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-002.txt | DOC-003 | PDF p. 2 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-003.txt | DOC-003 | PDF p. 3 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-004.txt | DOC-003 | PDF p. 4 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-005.txt | DOC-003 | PDF p. 5 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-006.txt | DOC-003 | PDF p. 6 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-007.txt | DOC-003 | PDF p. 7 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-008.txt | DOC-003 | PDF p. 8 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-009.txt | DOC-003 | PDF p. 9 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-010.txt | DOC-003 | PDF p. 10 | native plus targeted OCR / manifest-defined | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-002.json | DOC-003 | PDF p. 2 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-003.json | DOC-003 | PDF p. 3 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-004.json | DOC-003 | PDF p. 4 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-005.json | DOC-003 | PDF p. 5 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-006.json | DOC-003 | PDF p. 6 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-007.json | DOC-003 | PDF p. 7 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-008.json | DOC-003 | PDF p. 8 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-009.json | DOC-003 | PDF p. 9 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-010.json | DOC-003 | PDF p. 10 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-002.txt | DOC-003 | PDF p. 2 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-003.txt | DOC-003 | PDF p. 3 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-004.txt | DOC-003 | PDF p. 4 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-005.txt | DOC-003 | PDF p. 5 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-006.txt | DOC-003 | PDF p. 6 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-007.txt | DOC-003 | PDF p. 7 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-008.txt | DOC-003 | PDF p. 8 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-009.txt | DOC-003 | PDF p. 9 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-010.txt | DOC-003 | PDF p. 10 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/page_level_manifest.json | DOC-003 | PDF pp. 1-10 | page/source-location manifest | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-002.png | DOC-003 | PDF p. 2 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-003.png | DOC-003 | PDF p. 3 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-004.png | DOC-003 | PDF p. 4 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-005.png | DOC-003 | PDF p. 5 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-006.png | DOC-003 | PDF p. 6 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-007.png | DOC-003 | PDF p. 7 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-008.png | DOC-003 | PDF p. 8 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-009.png | DOC-003 | PDF p. 9 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-010.png | DOC-003 | PDF p. 10 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/document_outputs/JAMA2019-10517-D04/document_record.yaml | DOC-004 | PDF p. 1 | source identity record | PARTIAL | Identity/hash reusable; legacy audit restrictions have no effect |
| .ai_paper_validation/document_outputs/package_manifest.yaml | DOC-001, DOC-002, DOC-003, DOC-004 | PDF pp. 1-10; pp. 1-42; pp. 1-10; p. 1 | metadata | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-001.txt | DOC-001 | PDF p. 1 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-002.txt | DOC-001 | PDF p. 2 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-003.txt | DOC-001 | PDF p. 3 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-004.txt | DOC-001 | PDF p. 4 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-005.txt | DOC-001 | PDF p. 5 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-006.txt | DOC-001 | PDF p. 6 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-007.txt | DOC-001 | PDF p. 7 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-008.txt | DOC-001 | PDF p. 8 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-009.txt | DOC-001 | PDF p. 9 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-010.txt | DOC-001 | PDF p. 10 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/ocr_text/page-003.txt | DOC-001 | PDF p. 3 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/ocr_text/page-005.txt | DOC-001 | PDF p. 5 | OCR text / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/page_ocr_metadata/page-003.json | DOC-001 | PDF p. 3 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/page_ocr_metadata/page-005.json | DOC-001 | PDF p. 5 | OCR metadata / rapidocr-cuda | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-003.png | DOC-001 | PDF p. 3 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-005.png | DOC-001 | PDF p. 5 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-006.png | DOC-001 | PDF p. 6 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-007.png | DOC-001 | PDF p. 7 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-008.png | DOC-001 | PDF p. 8 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-009.png | DOC-001 | PDF p. 9 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-001.txt | DOC-003 | PDF p. 1 | native text / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-002.txt | DOC-003 | PDF p. 2 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-003.txt | DOC-003 | PDF p. 3 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-004.txt | DOC-003 | PDF p. 4 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-005.txt | DOC-003 | PDF p. 5 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-006.txt | DOC-003 | PDF p. 6 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-007.txt | DOC-003 | PDF p. 7 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-008.txt | DOC-003 | PDF p. 8 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-009.txt | DOC-003 | PDF p. 9 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-010.txt | DOC-003 | PDF p. 10 | native text / PyMuPDF | PARTIAL | Sparse plotted-content text; full page image supplies complete visual coverage |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-002.png | DOC-003 | PDF p. 2 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-003.png | DOC-003 | PDF p. 3 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-004.png | DOC-003 | PDF p. 4 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-005.png | DOC-003 | PDF p. 5 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-006.png | DOC-003 | PDF p. 6 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-007.png | DOC-003 | PDF p. 7 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-008.png | DOC-003 | PDF p. 8 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-009.png | DOC-003 | PDF p. 9 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-010.png | DOC-003 | PDF p. 10 | 300-dpi rendered page / PyMuPDF | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/ocr_backend.json | DOC-001 and DOC-003 | document-level identity/processing metadata | metadata | USABLE | Locator only; source is authority |
| .ai_paper_validation/preprocessing/ocr_backend_gpu_diagnostic.json | DOC-001 and DOC-003 | document-level identity/processing metadata | metadata | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_all_pages.txt | DOC-002 | PDF pp. 1-42 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p01.txt | DOC-002 | PDF p. 1 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p02.txt | DOC-002 | PDF p. 2 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p03.txt | DOC-002 | PDF p. 3 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p04.txt | DOC-002 | PDF p. 4 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p05.txt | DOC-002 | PDF p. 5 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p06.txt | DOC-002 | PDF p. 6 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p07.txt | DOC-002 | PDF p. 7 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p08.txt | DOC-002 | PDF p. 8 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p09.txt | DOC-002 | PDF p. 9 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p10.txt | DOC-002 | PDF p. 10 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p11.txt | DOC-002 | PDF p. 11 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p12.txt | DOC-002 | PDF p. 12 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p13.txt | DOC-002 | PDF p. 13 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p14.txt | DOC-002 | PDF p. 14 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p15.txt | DOC-002 | PDF p. 15 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p16.txt | DOC-002 | PDF p. 16 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p17.txt | DOC-002 | PDF p. 17 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p18.txt | DOC-002 | PDF p. 18 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p19.txt | DOC-002 | PDF p. 19 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p20.txt | DOC-002 | PDF p. 20 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p21.txt | DOC-002 | PDF p. 21 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_pp01_21.txt | DOC-002 | PDF pp. 1-21 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_all_pages.txt | DOC-002 | PDF pp. 1-42 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p01.txt | DOC-002 | PDF p. 1 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p02.txt | DOC-002 | PDF p. 2 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p03.txt | DOC-002 | PDF p. 3 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p04.txt | DOC-002 | PDF p. 4 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p05.txt | DOC-002 | PDF p. 5 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p06.txt | DOC-002 | PDF p. 6 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p07.txt | DOC-002 | PDF p. 7 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p08.txt | DOC-002 | PDF p. 8 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p09.txt | DOC-002 | PDF p. 9 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p10.txt | DOC-002 | PDF p. 10 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p11.txt | DOC-002 | PDF p. 11 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p12.txt | DOC-002 | PDF p. 12 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p13.txt | DOC-002 | PDF p. 13 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p14.txt | DOC-002 | PDF p. 14 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p15.txt | DOC-002 | PDF p. 15 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p16.txt | DOC-002 | PDF p. 16 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p17.txt | DOC-002 | PDF p. 17 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p18.txt | DOC-002 | PDF p. 18 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p19.txt | DOC-002 | PDF p. 19 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p20.txt | DOC-002 | PDF p. 20 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p21.txt | DOC-002 | PDF p. 21 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_pp01_21.txt | DOC-002 | PDF pp. 1-21 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/visual_p17.png | DOC-002 | PDF p. 17 | rendered page / engine unrecorded | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_001/visual_p21.png | DOC-002 | PDF p. 21 | rendered page / engine unrecorded | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | DOC-002 | PDF pp. 22-42 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_native.txt | DOC-002 | PDF pp. 22-42 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-004_p1_layout.txt | DOC-004 | PDF p. 1 | layout text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-004_p1_native.txt | DOC-004 | PDF p. 1 | native text / pdftotext | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_6_1/preprocessing/cross-main-p04.png | DOC-001 | PDF p. 4 | rendered page / engine unrecorded | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_6_1/preprocessing/cross-main-p05.png | DOC-001 | PDF p. 5 | rendered page / engine unrecorded | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_6_1/preprocessing/cross-plan-p12.png | DOC-002 | PDF p. 12 | rendered page / engine unrecorded | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_6_1/preprocessing/cross-plan-p14.png | DOC-002 | PDF p. 14 | rendered page / engine unrecorded | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_6_1/preprocessing/inclusion_screen/protocol-p10.png | DOC-002 | PDF p. 10 | rendered page / engine unrecorded | USABLE | Locator only; source is authority |
| .ai_paper_validation/review_1_6_1/preprocessing/statistics_pass_1/protocol-p14.png | DOC-002 | PDF p. 14 | rendered page / engine unrecorded | DUPLICATE | Byte-identical to .ai_paper_validation/review_1_6_1/preprocessing/cross-plan-p14.png |
| .ai_paper_validation/review_1_6_1/preprocessing/statistics_pass_1/protocol-p16.png | DOC-002 | PDF p. 16 | rendered page / engine unrecorded | USABLE | Locator only; source is authority |

Eligible inventory and preserved reuse hash count: 194 assets. Reusable unit union: all 63 PDF pages; fresh-required unit union: none. Every unit enters the fresh relationship mapping stage regardless of reuse.

Excluded legacy response wrappers are inventoried by path only: `.ai_paper_validation/document_outputs/JAMA2019-10517-D01/main_text_extractor_response.yaml` and `.ai_paper_validation/document_outputs/JAMA2019-10517-D03/results_supplement_extractor_response.md`. Their complete source-linked raw native, OCR, rendered-page and page-manifest inputs are inventoried above, so these potentially mixed scientific response artifacts are unnecessary and were not read or reused. Legacy not_audited_by_design and rights-screening records are not evidence extraction assets and impose no scientific scope boundary. Legacy preprocessing Python scripts were inspected only to identify existing engine provenance, never executed or used for scientific discovery. Existing backend JSON is historical engine metadata; it does not authorize GPU processing in this run.

## New source-confirmation derivatives and merge provenance

New workflow derivatives are distinct from read-only reused assets and are not included in the reused-asset before hashes. Main mapping produced direct Poppler layout text and CPU rendered pages 3-9 under preprocessing/main_mapping/. Support core produced direct protocol pp.1-21 layout and schedule images under preprocessing/support_mapping/; support appendix produced source-matched pp.22-42 layout and p41.png under preprocessing/support_appendix_mapping/. Cross-source review produced CPU plan12.png and plan21.png under preprocessing/cross_source/. Exact commands and source units are recorded in the respective mapping/checker artifacts. No new OCR was necessary. Canonical support and numeric artifacts merge every disjoint part; only relative source-link depth is adjusted for the canonical directory. The eligibility glyph correction is explicitly annotated in the new map without altering any extracted or reused text.

Mechanical recheck visually inspected all affected supplied pages, reusing current exact-source images and adding 14 CPU Poppler renders (main pp.1,2,10; result supplement pp.1-10; data-sharing p.1) under preprocessing/evidence_recheck/. Commands and every page location are recorded in verification/evidence_recheck.md. No OCR was needed. All five stable comparisons were reproduced without registration transcription or classification changes.

The final inclusion/classification audit produced four direct Poppler CPU layout locator texts under preprocessing/quality_inclusion_audit/: main.txt (DOC-001), plan.txt (DOC-002), supp2.txt (DOC-003), and supp3.txt (DOC-004). Each is individually listed in the coverage manifest. Candidate confirmation remains grounded in supplied pages and the source-derived visual recheck; locator text does not supersede source glyphs. No new OCR or fallback environment was used.
