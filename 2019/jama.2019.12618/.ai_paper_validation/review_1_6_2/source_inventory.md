# Workflow 1.6.2 Direct Source Inventory

Five direct sources are supplied, all PDFs. No direct DOC, DOCX, XLS, XLSX, or CSV sources exist. Stable units are physical PDF pages, independently counted with direct Poppler pdfinfo 26.01.0. Each source is included in full. Source paths and integrity hashes are package-relative in source_hashes_before.sha256. Source roles follow document content, rather than supplement number.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content and role basis | Complete scope |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_rathinam_2019_oi_190092.pdf | PDF | PDF_PAGE | 10 | REPORT | Main randomized-trial article; p. 1 identifies JAMA Original Investigation and reported trial results. | PDF pp. 1-10 |
| DOC-002 | joi190092supp1_prod.pdf | PDF | PDF_PAGE | 16 | REPORT | Non-plan supplementary results, eligibility context, adverse-event definitions and guidance, eTables 1-9; title and contents at pp. 1-2. | PDF pp. 1-16 |
| DOC-003 | joi190092supp2_prod.pdf | PDF | PDF_PAGE | 153 | PLAN | Original protocol, final protocol, summary of changes, and prospective Manual of Operations and Procedures, identified on p. 1. Versions remain PLAN throughout the bound document. | PDF pp. 1-153 |
| DOC-004 | joi190092supp3_prod.pdf | PDF | PDF_PAGE | 83 | PLAN | Original statistical analysis plan, final statistical analysis plan and summary of changes, identified on p. 1. Versions remain PLAN throughout the bound document. | PDF pp. 1-83 |
| DOC-005 | joi190092supp4_prod.pdf | PDF | PDF_PAGE | 1 | REPORT | Non-plan administrative reporting supplement, headed Data Sharing Statement. No prospective statistical plan; classified REPORT for the required binary role scheme. Mapping must document its limited quantitative relevance. | PDF p. 1 |

Total: 263 physical PDF pages. No physical source combines REPORT and PLAN roles; the protocol and SAP each combine plan versions. Legacy inventory statements that excluded entire plans or administrative content from earlier scientific work are provenance only and do not restrict this run.

## Complete reusable and fresh partition

- DOC-001: reusable pp. 1-10; fresh-required none.
- DOC-002: reusable pp. 1-16; fresh-required none.
- DOC-003: reusable pp. 1-153. Legacy native/layout text covers pp. 1-14, 16-18, 20-73, 75-79, 82-83, 85-88, 92-93, 95, 97-104, 106, 108, 110-115, 117, 119, 121-132, 135, 137-153; OCR paired with existing rendered pages covers pp. 15, 19, 74, 80, 81, 84, 89, 90, 91, 94, 96, 105, 107, 109, 116, 118, 120, 133, 134, 136. Fresh-required none; every OCR page still requires mapper inspection.
- DOC-004: reusable pp. 1-74 and 76-83; fresh-required p.75. Initial curation counted all pages reusable, but mapper inspection located the alpha-spending formula on physical p.75 rather than the existing discussion-page image p.74; incomplete native formula symbols required fresh exact-page rendering. CPU Poppler image preprocessing/sap_003/page-075.png and extraction/parts/sap_065_083.md close that gap. Existing supplementary visual assets cover formula-rich pp. 22-24, 26, 34, 63-67, 74 and selected additional pages.
- DOC-005: reusable p. 1; fresh-required none.

Direct source is final authority. Reusable assets are transcription aids and do not mean any page has already been scientifically mapped in this run.
