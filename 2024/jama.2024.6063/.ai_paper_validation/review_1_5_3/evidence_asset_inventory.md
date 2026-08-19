# Reusable Evidence-Asset Inventory

This is an inventory of the eligible reusable evidence assets below the existing audit area. It was compiled from file paths, page manifests, document records, preprocessing records, and source-location metadata; old candidate, verifier, critic, checker, endetail, and final-report content was not used to set discovery scope. All listed files are hashed individually in `reused_artifact_hashes_before.sha256`.

## Asset classes and coverage

| Asset group and exact member paths | Asset type and method | Exact source locations | Coverage classification | Fitness classification | Gaps and downstream assignment |
|---|---|---|---|---|---|
| `.ai_paper_validation/preprocessing/DOC-JAMA2024-6063-MAIN-2f574565/normalized_text/page-001.txt` through `page-009.txt` | Native/layout text; page-level `pdftotext -layout` output normalized only for page delimiters. | `jama_laslett_2024_oi_240048_1727199125.7595.pdf` pp. 1-9, one text asset per same-numbered PDF page. | USABLE | USABLE | p. 10 is absent; main mapper must freshly extract and map p. 10. |
| `.ai_paper_validation/preprocessing/DOC-JAMA2024-6063-MAIN-2f574565/page_images/page-003.png`, `page-005.png`, `page-006.png`, `page-007.png`, and `page-008.png` | Rendered 200-dpi PNG pages. | Main PDF pp. 3 and 5-8. | DUPLICATE | USABLE | These visual assets add visual confirmation but no additional uniquely covered unit beyond usable native text. No rendering exists for pp. 1, 2, 4, 9, or 10; text covers pp. 1, 2, 4, and 9, while p. 10 remains fresh-required. |
| `.ai_paper_validation/preprocessing/DOC-JAMA2024-6063-MAIN-2f574565/page_manifest.md` | Page manifest. | Main PDF pp. 1-10; it maps native text for pp. 1-9 and rendered pages for pp. 3 and 5-8. | PARTIAL | USABLE | The manifest explicitly records p. 10 as not extracted under a prior scope; main mapper owns fresh p. 10 mapping. |
| `.ai_paper_validation/document_outputs/DOC-JAMA2024-6063-MAIN-2f574565/document_record.md` | Document record. | Main PDF pp. 1-10, with legacy scientific coverage only pp. 1-9. | STALE | PARTIAL | The direct-source identity is usable, but its legacy exclusion of p. 10 cannot govern this run. Main mapper owns p. 10. |
| `.ai_paper_validation/document_outputs/DOC-JAMA2024-6063-MAIN-2f574565/pdf_preprocessing_record.md` | Preprocessing/source-location record. | Main PDF pp. 1-9 for existing text; records p. 10 only as formerly excluded. | PARTIAL | USABLE | Does not provide p. 10 extraction; main mapper owns p. 10. |
| `.ai_paper_validation/document_outputs/DOC-JAMA2024-6063-MAIN-2f574565/main_text_extractor_response.md` | Source-location map from prior main-text extraction. | Main PDF pp. 1, 3, 5-9, with table/figure locations stated in the record. | PARTIAL | PARTIAL | It is a result summary rather than page-complete native text and omits pp. 2, 4, and 10 as a location map. Native text supplies pp. 2 and 4; main mapper owns p. 10. |
| `.ai_paper_validation/document_outputs/DOC-JAMA2024-6063-SUPP1-317ff46a/document_record.md` | Document record. | Protocol PDF pp. 1-15, identified but marked not audited in the prior workflow. | STALE | PARTIAL | No reusable scientific extraction; support mapper owns fresh pp. 1-15. |
| `.ai_paper_validation/document_outputs/DOC-JAMA2024-6063-SUPP1-317ff46a/pdf_preprocessing_record.md` | Preprocessing/source-location record. | Protocol PDF pp. 1-15, with no prior extraction. | STALE | PARTIAL | No reusable page coverage; support mapper owns fresh pp. 1-15. |
| `.ai_paper_validation/document_outputs/DOC-JAMA2024-6063-SUPP2-57681138/document_record.md` | Document record. | Statistical analysis plan PDF p. 1, identified but marked not audited in the prior workflow. | STALE | PARTIAL | No reusable scientific extraction; support mapper owns fresh p. 1. |
| `.ai_paper_validation/document_outputs/DOC-JAMA2024-6063-SUPP2-57681138/pdf_preprocessing_record.md` | Preprocessing/source-location record. | Statistical analysis plan PDF p. 1, with no prior extraction. | STALE | PARTIAL | No reusable page coverage; support mapper owns fresh p. 1. |
| `.ai_paper_validation/preprocessing/DOC-JAMA2024-6063-SUPP3-67e172cd/normalized_text/page-001.txt` through `page-015.txt` | Native/layout text; page-level `pdftotext -layout` output normalized only for page delimiters. | `joi240048supp3_prod_1727199125.83025.pdf` pp. 1-15, one text asset per same-numbered PDF page. | USABLE | USABLE | No coverage gap. Support mapper owns reusable-backed mapping of pp. 1-15. |
| `.ai_paper_validation/preprocessing/DOC-JAMA2024-6063-SUPP3-67e172cd/page_images/page-002.png` through `page-015.png` | Rendered 200-dpi PNG pages. | Results-supplement PDF pp. 2-15. | DUPLICATE | USABLE | The images provide visual table/figure confirmation but do not add uniquely covered units beyond usable native text. p. 1 has usable native text and no rendering is required by the asset plan. |
| `.ai_paper_validation/preprocessing/DOC-JAMA2024-6063-SUPP3-67e172cd/page_manifest.md` | Page manifest. | Results-supplement PDF pp. 1-15; native text on every page and rendered evidence on pp. 2-15. | USABLE | USABLE | No gap. |
| `.ai_paper_validation/document_outputs/DOC-JAMA2024-6063-SUPP3-67e172cd/document_record.md` | Document record. | Results-supplement PDF pp. 1-15. | USABLE | USABLE | No gap; it is a document-level provenance map, not a replacement for page text. |
| `.ai_paper_validation/document_outputs/DOC-JAMA2024-6063-SUPP3-67e172cd/pdf_preprocessing_record.md` | Preprocessing/source-location record. | Results-supplement PDF pp. 1-15, with page-text coverage pp. 1-15 and render coverage pp. 2-15. | USABLE | USABLE | No gap. |
| `.ai_paper_validation/document_outputs/DOC-JAMA2024-6063-SUPP3-67e172cd/results_supplement_extractor_response.md` | Source-location map from prior results-supplement extraction. | Results-supplement PDF pp. 2-15, including eTables 1-8 and eFigure. | PARTIAL | PARTIAL | p. 1 is not represented by this summary map, although p. 1 has usable native text. The map is a locator only; support mapper owns full reusable-backed pp. 1-15 mapping. |

## Counts and absent classes

- Eligible reusable artifacts inventoried and hashed: 55.
  - Native/layout text: 24 files (main pp. 1-9; results supplement pp. 1-15).
  - Rendered pages: 19 PNG files (main pp. 3 and 5-8; results supplement pp. 2-15).
  - Page manifests: 2 files.
  - Document records: 4 files.
  - Preprocessing/source-location records: 4 files.
  - Extractor source-location maps: 2 files.
- Existing OCR text: none.
- Existing table extraction: none.
- Existing workbook extraction: none.
- Existing Office, workbook, and CSV direct sources: none.
- UNREADABLE eligible assets: none observed from file inventory and manifest metadata.

## Reuse decision

Usable reusable page text covers 24 unique source units: main PDF pp. 1-9 and results supplement pp. 1-15. Rendered pages are retained as visual companions, not counted again as unique reusable units. The 17 remaining direct PDF pages are fresh-required and assigned in `source_coverage.md`: main p. 10 to the main mapper; protocol pp. 1-15 and statistical-analysis-plan p. 1 to the support mapper. Every planned mapper must use the direct source as authority for any candidate-level conclusion.
