# Reused Evidence-Asset Inventory

This inventory covers every existing OCR/native text, source-location map, page manifest, document record, rendered page, and available table-style evidence ledger below the pre-existing audit area. It excludes old candidate, queue, verifier, critic, endetail, quality, and final-report content as discovery scope. No direct Office, workbook, CSV, layout-text, workbook-extraction, or standalone table-extraction asset exists.

Fitness is assessed only for reuse as a locator/transcription/mapping aid; direct source remains authoritative. `USABLE` means page/source linkage and legibility are adequate; `PARTIAL` means it cannot replace fresh full-unit direct mapping; `DUPLICATE` means an equivalent canonical map is already present. No inventoried eligible asset was unreadable or demonstrably stale.

| Asset path | Asset type and method | Exact mapped source location | Fitness | Coverage and gap note |
|---|---|---|---|---|
| .ai_paper_validation/package_manifest.md | Package document map | DOC-001 pp. 1-11; DOC-002 pp. 1-46; DOC-003 pp. 1-9; DOC-004 pp. 1-48 | USABLE | Source identity, page counts, and supplied-scope locator; not a numeric extraction. |
| .ai_paper_validation/preprocessing/preprocessing_summary.md | Preprocessing coverage map | DOC-001 pp. 1-11; DOC-003 pp. 1-9; records DOC-002 pp. 1-46 and DOC-004 pp. 1-48 as unextracted | USABLE | Confirms native/OCR coverage and the 94-page extraction gap. |
| .ai_paper_validation/preprocessing/page_level_manifest.csv | Page-to-source manifest | DOC-001 pp. 1-11; DOC-003 pp. 1-9; DOC-002 pp. 1-46 and DOC-004 pp. 1-48 as no extraction | USABLE | Canonical structured page-location map. |
| .ai_paper_validation/preprocessing/page_level_manifest.json | Page-to-source manifest | Same locations as the CSV manifest | DUPLICATE | JSON duplicate of the canonical CSV page map. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/document_record.md | Document record | DOC-001 pp. 1-11 | USABLE | Locates native text and six visual/OCR companions. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/preprocessing_record.md | Preprocessing record | DOC-001 pp. 1-11; rendered/OCR pp. 3, 5-9 | USABLE | Confirms complete native coverage and selected visual coverage. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/normalized_text/native_text.txt | Native PDF text, page-delimited | DOC-001 pp. 1-11 | USABLE | Complete reusable native text; page headers provide exact PDF-page mapping. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/main_text_extractor_evidence.md | Source-location/evidence map | DOC-001 pp. 1-11, with table/figure references | USABLE | Result-location aid only; direct PDF and native text remain authority. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/ocr_text/page-03.txt | OCR companion | DOC-001 p. 3 | USABLE | Figure 1 visual-text corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/ocr_text/page-05.txt | OCR companion | DOC-001 p. 5 | USABLE | Table 1 visual-text corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/ocr_text/page-06.txt | OCR companion | DOC-001 p. 6 | USABLE | Table 1 continuation/results-text corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/ocr_text/page-07.txt | OCR companion | DOC-001 p. 7 | USABLE | Table 2 corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/ocr_text/page-08.txt | OCR companion | DOC-001 p. 8 | USABLE | Table 3 corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/ocr_text/page-09.txt | OCR companion | DOC-001 p. 9 | USABLE | Figure 2 corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/page_images/page-03.png | Rendered full page | DOC-001 p. 3 | USABLE | Figure 1 visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/page_images/page-05.png | Rendered full page | DOC-001 p. 5 | USABLE | Table 1 visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/page_images/page-06.png | Rendered full page | DOC-001 p. 6 | USABLE | Table 1/results visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/page_images/page-07.png | Rendered full page | DOC-001 p. 7 | USABLE | Table 2 visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/page_images/page-08.png | Rendered full page | DOC-001 p. 8 | USABLE | Table 3 visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/page_images/page-09.png | Rendered full page | DOC-001 p. 9 | USABLE | Figure 2 visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP1/document_record.md | Document record | DOC-002 pp. 1-46 | USABLE | Confirms the document identity and absent full extraction. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP1/preprocessing_record.md | Preprocessing record | DOC-002 pp. 1-46 | USABLE | Explicitly records no scientific-content extraction, rendering, or OCR. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP1/rights_screen_render/page-1.png | Rendered page | DOC-002 p. 1 | PARTIAL | Rights-screen render is not quantitative-ready text; direct mapping remains required. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP1/rights_screen_render/page-2.png | Rendered page | DOC-002 p. 2 | PARTIAL | Rights-screen render is not quantitative-ready text; direct mapping remains required. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/document_record.md | Document record | DOC-003 pp. 1-9 | USABLE | Locates complete native text and seven visual/OCR companions. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/preprocessing_record.md | Preprocessing record | DOC-003 pp. 1-9; rendered/OCR pp. 3-9 | USABLE | Confirms full native and selected visual coverage. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/normalized_text/native_text.txt | Native PDF text, page-delimited | DOC-003 pp. 1-9 | USABLE | Complete reusable native text; page headers provide exact PDF-page mapping. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/results_supplement_extractor_response.md | Source-location/evidence map | DOC-003 pp. 1-9, including eTables/eFigures | USABLE | Result-location aid only; direct PDF and native text remain authority. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/ocr_text/page-3.txt | OCR companion | DOC-003 p. 3 | USABLE | eTables 1-2 corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/ocr_text/page-4.txt | OCR companion | DOC-003 p. 4 | USABLE | eTables 3-4 corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/ocr_text/page-5.txt | OCR companion | DOC-003 p. 5 | USABLE | eTables 5a-5b corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/ocr_text/page-6.txt | OCR companion | DOC-003 p. 6 | USABLE | eTable 6 corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/ocr_text/page-7.txt | OCR companion | DOC-003 p. 7 | USABLE | eFigures 1-2 corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/ocr_text/page-8.txt | OCR companion | DOC-003 p. 8 | USABLE | eFigure 3 corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/ocr_text/page-9.txt | OCR companion | DOC-003 p. 9 | USABLE | eFigure 4 corroboration. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/page_images/page-3.png | Rendered full page | DOC-003 p. 3 | USABLE | eTables 1-2 visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/page_images/page-4.png | Rendered full page | DOC-003 p. 4 | USABLE | eTables 3-4 visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/page_images/page-5.png | Rendered full page | DOC-003 p. 5 | USABLE | eTables 5a-5b visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/page_images/page-6.png | Rendered full page | DOC-003 p. 6 | USABLE | eTable 6 visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/page_images/page-7.png | Rendered full page | DOC-003 p. 7 | USABLE | eFigures 1-2 visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/page_images/page-8.png | Rendered full page | DOC-003 p. 8 | USABLE | eFigure 3 visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP3/page_images/page-9.png | Rendered full page | DOC-003 p. 9 | USABLE | eFigure 4 visual confirmation. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP4/document_record.md | Document record | DOC-004 pp. 1-48 | USABLE | Confirms the document identity and absent full extraction. |
| .ai_paper_validation/document_outputs/JAMA2024-24764-SUPP4/preprocessing_record.md | Preprocessing record | DOC-004 pp. 1-48 | USABLE | Explicitly records no scientific-content extraction, rendering, or OCR. |
| .ai_paper_validation/tmp/pdfs/JAMA2024-24764-SUPP4/cover-1.png | Rendered page | DOC-004 p. 1 | PARTIAL | Selected image only; full direct mapping remains required. |
| .ai_paper_validation/tmp/pdfs/JAMA2024-24764-SUPP4/cover-2.png | Rendered page | DOC-004 p. 2 | PARTIAL | Selected image only; full direct mapping remains required. |
| .ai_paper_validation/tmp/pdfs/JAMA2024-24764-SUPP4/publication-43.png | Rendered page | DOC-004 p. 43 | PARTIAL | Selected image only; full direct mapping remains required. |
| .ai_paper_validation/tmp/pdfs/JAMA2024-24764-SUPP4/end-48.png | Rendered page | DOC-004 p. 48 | PARTIAL | Selected image only; full direct mapping remains required. |
| .ai_paper_validation/tmp/pdfs/evidence_verifier/main-p4-04.png | Legacy verifier rendered crop | DOC-001 p. 4 | PARTIAL | Cropped legacy visual; native text already covers p. 4 and this is not a full page map. |
| .ai_paper_validation/tmp/pdfs/evidence_verifier/supp1-p28-28.png | Legacy verifier rendered crop | DOC-002 p. 28 | PARTIAL | Cropped legacy visual; it cannot substitute for fresh full-page direct mapping. |
| .ai_paper_validation/tmp/pdfs/figure_flow_checker/main-p9-top-left.png | Legacy checker rendered crop | DOC-001 p. 9, top-left region | PARTIAL | Crop is a visual locator only; full page image and native text cover p. 9. |

## Coverage conclusion and gaps

Reusable quantitative-ready native text covers DOC-001 pp. 1-11 and DOC-003 pp. 1-9, for 20 reusable source units. The extracted page manifests and records corroborate this mapping. All DOC-002 pp. 1-46 and DOC-004 pp. 1-48 are fresh-required because no complete native/layout/OCR/table extraction covers those pages; selected image/crop artifacts are partial and do not reduce the fresh-required count. Fresh direct-source assignments are DOC-002 pp. 1-46 and DOC-004 pp. 1-48 to the support quantitative mapper. The main quantitative mapper is assigned the reusable-backed DOC-001 pp. 1-11; the support quantitative mapper is assigned the reusable-backed DOC-003 pp. 1-9 as well as both fresh scopes.
