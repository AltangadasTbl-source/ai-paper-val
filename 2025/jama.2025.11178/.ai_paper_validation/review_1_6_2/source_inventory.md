# Direct Source Inventory

Six supplied direct sources were inventoried throughout this package, excluding audit derivatives and workflow support files. No supplied DOC, DOCX, XLS or CSV source exists. Five PDF page counts were confirmed from the exact source with the recorded PyMuPDF1.26.4 fallback info helper. Workbook structure was inspected directly with unzip: one worksheet, eTable 3, A1:J115; 1140 stored/styled cell elements, of which 525 contain values. Original workbook extraction retains exactly the 525 populated cell addresses and cached values.

| Source ID | Source path | Unit type | Total units | Document role | Role by content |
|---|---|---|---:|---|---|
| DOC-001 | jama_debar_2025_oi_250046_1755300121.13587.pdf | PDF_PAGE | 14 | REPORT | Main article reports randomized trial results, with abstract, methods, tables, figures and discussion. |
| DOC-002 | joi250046supp1_prod_1755300121.14087.pdf | PDF_PAGE | 77 | PLAN | UH3 study protocol, Version 5.0, November 10, 2022; prospective trial design and amendment history. |
| DOC-003 | joi250046supp2_prod_1755300121.15087.pdf | PDF_PAGE | 29 | PLAN | Statistical analysis plan specifying analyses before the reported results. |
| DOC-004 | joi250046supp3_prod_1755300121.15087.pdf | PDF_PAGE | 7 | REPORT | Published TIDieR description of study interventions; retrospective supplement describing the performed trial interventions, not a prospective operational manual. |
| DOC-005 | joi250046supp4_prod_1755300121.15587.pdf | PDF_PAGE | 19 | REPORT | Published results and analysis-method supplement with eTables and eFigures. |
| DOC-006 | joi250046supp5_prod_1755300121.16087.xlsx | WORKSHEET | 1 | REPORT | eTable 3 baseline characteristics by outcome-completion group and related reported statistics. |

No direct source bundle was identified as containing both PLAN and REPORT documents. The protocol and SAP remain PLAN despite their physical supplement packaging. The intervention description and results-method appendices are REPORT by their published explanatory content. PDF covers, references, amendment histories, sparse pages and all workbook cells remain in scope. Stable source units are 146 PDF pages and 1 worksheet, total 147. Exact source hashes are recorded in source_hashes_before.sha256. No source or original reused artifact was modified.

New downstream assignments: DOC-001 pp.1–14 to main_quantitative_mapper; DOC-002 pp.1–77, DOC-003 pp.1–29, DOC-004 pp.1–7, DOC-005 pp.1–19 and DOC-006 eTable 3 A1:J115 to support_quantitative_mapper. Fresh-required subsets are DOC-002 pp.21–77, DOC-003 pp.1–29 and DOC-005 p.12. Reusable image-only protocol pages still require fresh scientific reading.
