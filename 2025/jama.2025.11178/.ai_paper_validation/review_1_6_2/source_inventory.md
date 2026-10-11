# Direct-source inventory

All supplied direct PDF/DOC/DOCX/XLS/XLSX/CSV files were inventoried within this package. Audit-area PDFs and CSVs are derivatives, not additional direct sources. No direct DOC, DOCX, XLS, or CSV is supplied. Source hashes are in source_hashes_before.sha256. PDF counts use pdfinfo; workbook count and location use unzip of xl/workbook.xml and xl/worksheets/sheet1.xml. Document roles are determined by content.

| Source ID | Source path | Document role | Unit type | Total units | Content and exact locations |
|---|---|---|---|---:|---|
| DOC-001 | jama_debar_2025_oi_250046_1755300121.13587.pdf | REPORT | PDF_PAGE | 14 | Main randomized trial article, including tables and figures. |
| DOC-002 | joi250046supp1_prod_1755300121.14087.pdf | PLAN | PDF_PAGE | 77 | UH3 study protocol version 5.0 and amendment/version material; no results-report bundle. |
| DOC-003 | joi250046supp2_prod_1755300121.15087.pdf | PLAN | PDF_PAGE | 29 | RESOLVE statistical analysis plan version 6.0 dated 18 July 2024, with plan change summaries (direct source title confirmed by fresh SAP mapper). |
| DOC-004 | joi250046supp3_prod_1755300121.15087.pdf | REPORT | PDF_PAGE | 7 | Published retrospective TIDieR intervention-description supplement, including delivery and modifications; not a prospective operational manual. |
| DOC-005 | joi250046supp4_prod_1755300121.15587.pdf | REPORT | PDF_PAGE | 19 | Results/methods supplement, outcome measures, adherence, missing data and sensitivity analyses. |
| DOC-006 | joi250046supp5_prod_1755300121.16087.xlsx | REPORT | WORKSHEET | 1 | Results workbook; worksheet eTable 3, declared range A1:J115, 525 nonempty cells. |

No source contains a mixed REPORT/PLAN bundle. PDF page references always use physical PDF pages. Native text for DOC-002 and DOC-003 is corrupted throughout; source images remain legible. Legacy selection flags and scope exclusions were not adopted.
