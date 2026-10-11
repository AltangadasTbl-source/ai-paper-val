# Direct Source Inventory

Inventory is restricted to this paper package. All supplied PDF, DOC, DOCX, XLS, XLSX and CSV paths were searched, including hidden paths; workflow tooling and derivative audit records were excluded from direct-source classification. Four PDF sources are supplied; no Office or CSV direct sources are supplied. Stable units are physical PDF pages, counted by direct Poppler `pdfinfo` 26.01.0. Source SHA-256 values are recorded in `source_hashes_before.sha256` using package-relative paths.

| Source ID | Source path | Format | Document role | Total units | Exact units | Content and role basis |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_de_boer_2019_oi_190122.pdf | PDF | REPORT | 11 | PDF pp. 1-11 | Main randomized clinical trial article, including abstract, methods, results, tables, figures and references. |
| DOC-002 | joi190122supp1_prod.pdf | PDF | PLAN | 33 | PDF pp. 1-33 | Protocol dated June 28, 2010 (pp. 1-30) and protocol addendum changing the analytic plan (pp. 31-33), submitted March 2, 2015 and implemented upon funding February 24, 2016. All content is plan material; this is a bound plan-version bundle, not a results supplement. |
| DOC-003 | joi190122supp2_prod.pdf | PDF | REPORT | 19 | PDF pp. 1-19 | Supplementary online results and methods: eAppendix, eTables 1-11, eFigures 1-3. No prospective plan document is bound into this source. |
| DOC-004 | joi190122supp3_prod.pdf | PDF | REPORT | 1 | PDF p. 1 | Non-plan data-sharing statement accompanying the reported trial. Contains no independent quantitative outcome display. |

Roles were determined from the source-linked title, contents and sections, not supplement numbering. No source contains both REPORT and PLAN content. The protocol/addendum bundle remains PLAN throughout.

Total: 4 sources, 64 PDF_PAGE units. Main mapping assignment: DOC-001 pp. 1-11. Support mapping assignment: DOC-002 pp. 1-33, DOC-003 pp. 1-19, DOC-004 p. 1. Every page is assigned, including administrative, bibliography and statement pages; pages with no result-relevant numeric content must receive an explicit mapping record.
