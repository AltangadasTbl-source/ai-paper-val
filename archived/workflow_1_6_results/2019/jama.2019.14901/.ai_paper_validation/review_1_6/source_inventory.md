# Direct-source inventory

Inventory uses package-local paths only. Four direct PDFs were found; no DOC, DOCX, XLS, XLSX, or CSV source exists. Stable units are physical PDF pages, including covers, references, appendices, and administrative pages. Direct `pdfinfo` (Poppler 26.01.0) establishes counts; `sha256sum` establishes identity in `source_hashes_before.sha256`. Supplied sources remain unchanged.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis and bundle assessment |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_thille_2019_oi_190108.pdf | PDF | PDF_PAGE | 11 | REPORT | Direct p1 identifies JAMA Original Investigation and randomized clinical trial results; full article and reference/context pages. No PLAN content bundle. |
| DOC-002 | joi190108supp1_prod.pdf | PDF | PDF_PAGE | 48 | PLAN | Direct p1 identifies HIGH-WEAN protocol version 4 dated 17 October 2017; p2 is Clinical Trial Protocol; contents and later pages contain prospective procedures, statistics, background and references. Historical/background quantitative material remains PLAN. No separate REPORT result bundle. |
| DOC-003 | joi190108supp2_prod.pdf | PDF | PDF_PAGE | 9 | REPORT | Direct p1 indexes eTables 1-5 and survival eFigure; non-plan results supplement. No PLAN bundle. |
| DOC-004 | joi190108supp3_prod.pdf | PDF | PDF_PAGE | 1 | REPORT | Direct p1 is a published-article Data Sharing Statement stating Data available: No. Administrative report-associated declaration, not prospective protocol/SAP material. No PLAN bundle; quantitative applicability must be recorded by mapper. |

All four source hashes agree with source identities recorded in the reusable package manifest. Legacy exclusions and scientific-audit recommendations are not scope constraints. Current mapping scope contains all 69 pages.
