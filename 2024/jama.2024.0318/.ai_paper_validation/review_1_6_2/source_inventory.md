# Workflow 1.6.2 Direct-Source Inventory

Inventory scope is the current paper package only. Recursive local discovery found four direct PDFs and no DOC, DOCX, XLS, XLSX, or CSV sources. Existing audit derivatives are evidence assets, not additional direct sources. Stable units are physical PDF pages, including covers, references, and administrative pages. Direct `pdfinfo` (Poppler 26.01.0) supplied counts; direct `pdftotext` first-page inspection supplied content-based roles. All supplied sources are unchanged.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content and role basis |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_courcoulas_2024_oi_240004_1721756962.76052.pdf | PDF | PDF_PAGE | 11 | REPORT | Page 1: JAMA Original Investigation, Long-Term Outcomes of Medical Management vs Bariatric Surgery in Type 2 Diabetes; main results article. |
| DOC-002 | joi240004supp1_prod_1721756962.80052.pdf | PDF | PDF_PAGE | 65 | PLAN | Page 1: ARMMS-T2D Clinical Protocol; prospective protocol bundle includes statistical-plan content. All bundled plan versions remain PLAN. |
| DOC-003 | joi240004supp2_prod_1721756962.82552.pdf | PDF | PDF_PAGE | 22 | REPORT | Page 1: Supplemental Online Content; eMethods, Statistical Supplementary Appendix, eReferences, eFigures and eTables accompanying reported results. Methods explaining the reported analysis remain REPORT. |
| DOC-004 | joi240004supp3_prod_1721756962.84052.pdf | PDF | PDF_PAGE | 1 | REPORT | Page 1: Data Sharing Statement issued with the report; administrative report adjunct, with no prospective statistical design. Complete page still requires mapping of applicable scope. |

No mixed REPORT/PLAN bundle was identified. No standalone SAP or structured dataset was supplied. Historical document-record scope exclusions are metadata only and do not govern this review. All 99 pages enter mandatory mapping.

## Direct integrity

`source_hashes_before.sha256` records all four package-relative direct paths. Their current SHA-256 values equal the identities in historical document records, establishing source continuity for derivative reuse. No sibling packages or external sources were inspected.

## Mapper assignments and canonical locators

- Main mapper: DOC-001 PDF pages 1-11; canonical full layout `.ai_paper_validation/review_1_5_3/preprocessing/main/DOC-001_pp1-11_direct_layout.txt`; per-page layout files in `.ai_paper_validation/document_outputs/DOC-001/preprocessing/normalized_text/`; visual pages 3-8 in the matching `page_images/` directory.
- Support primary shard: DOC-002 PDF pages 1-40; canonical per-page `.ai_paper_validation/review_1_5_3/preprocessing/support/DOC-002/page-NNN-layout.txt`.
- Support secondary shard: DOC-002 PDF pages 41-65; DOC-003 PDF pages 1-22; DOC-004 PDF page 1. DOC-003 pages 1-7 use `.ai_paper_validation/review_1_5_3/preprocessing/support/DOC-003/page-NNN-layout.txt`; pages 8-22 use `.ai_paper_validation/document_outputs/DOC-003/preprocessing/normalized_text/page-NNN.txt` with matching images. DOC-003 pages 8-13 additionally have OCR in `.ai_paper_validation/review_1_5_3/preprocessing/support/DOC-003/visual_confirmation/page-NNN-ocr.txt`. DOC-004 page 1 uses `.ai_paper_validation/review_1_5_3/preprocessing/support/DOC-004/page-001-layout.txt`.

These assignments partition all source units; every mapper must inspect each assigned unit and explicitly map any page with no relevant relationship. Entire DOC-002 layout text totals 218,152 bytes, exceeding the 200,000-character context bound; the two support shards avoid loading the whole protocol together. Reusable sparse figure text and OCR are locators; retained images supply visual content, and exact direct sources remain final authority.
