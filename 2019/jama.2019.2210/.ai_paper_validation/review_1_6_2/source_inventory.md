# Workflow 1.6.2 Direct Source Inventory

Inventory covers this package only. Direct `pdfinfo` established complete stable page counts; `pdftotext` first-page content established document roles. No Office or CSV source is supplied. Every PDF page enters the current review, including administrative and reference pages. Legacy scope exclusions do not restrict coverage.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content and exact scope |
|---|---|---|---|---:|---|---|
| DOC001 | jama_urashima_2019_oi_190023.pdf | PDF | PDF_PAGE | 9 | REPORT | Main AMATERASU article, PDF pp. 1-9; p. 9 is article information and references. |
| DOC002 | joi190023supp1_prod.pdf | PDF | PDF_PAGE | 45 | PLAN | Protocol with embedded SAP: contents p. 1, initial version pp. 2-16, final version pp. 17-33, references pp. 34-35, appendices pp. 36-44, amendment summary p. 45. Contains multiple plan versions, no REPORT bundle component. |
| DOC003 | joi190023supp2_prod.pdf | PDF | PDF_PAGE | 41 | REPORT | Results supplement: contents p. 1 and eTables/eFigures pp. 2-41. |
| DOC004 | joi190023supp3_prod.pdf | PDF | PDF_PAGE | 1 | REPORT | Published data-sharing statement p. 1, administrative companion to the results report; no prospective statistical plan content. |

Total: 4 direct sources, 96 PDF_PAGE units. SHA-256 values are in `source_hashes_before.sha256`, with package-relative paths. The supplied sources have remained unchanged. Role assignments derive from supplied content, not supplement numbering.

Canonical legacy location aliases: DOC001 = DOC-JAMA-2019-2210-MAIN = JAMA2019-2210-DOC-01; DOC002 = DOC-JAMA-2019-2210-SUPP-PROTOCOL-SAP = JAMA2019-2210-DOC-02; DOC003 = DOC-JAMA-2019-2210-SUPP-RESULTS = JAMA2019-2210-DOC-03; DOC004 = DOC-JAMA-2019-2210-SUPP-DATA-SHARING = JAMA2019-2210-DOC-04. Absolute paths in legacy metadata are historical; current package-relative filenames are authoritative.
