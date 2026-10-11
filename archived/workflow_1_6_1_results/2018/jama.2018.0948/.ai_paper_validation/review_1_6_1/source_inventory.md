# Direct Source Inventory

Inventory scope: every direct PDF, DOC, DOCX, XLS, XLSX and CSV in this paper package, recursively excluding audit derivatives, workflow controls and hidden tool configuration. Four direct PDFs are present; no Office or CSV source is supplied. Stable units are physical PDF pages, including cover, reference and administrative pages. Source hashes were initialized by the coordinator and confirmed with `sha256sum -c`; all four match.

| Source ID | Source path | Format | Document role | Role basis by content | Unit type | Total units | Reusable units | Fresh-required units |
|---|---|---|---|---|---|---:|---:|---:|
| DOC-001 | jama_parshuram_2018_oi_180015.pdf | PDF | REPORT | Published EPOCH randomized clinical trial article with abstract, methods, outcome tables, figures, discussion and references; physical pp. 1-11 correspond to journal pp. 1002-1012. | PDF_PAGE | 11 | 11 | 0 |
| DOC-002 | joi180015supp1_prod.pdf | PDF | PLAN | Research protocol 005, version dated 23 February 2011, with prospective design, outcomes, sample-size and analysis specifications, supporting operational materials and appendices; no results-report bundle. | PDF_PAGE | 37 | 37 | 0 |
| DOC-003 | joi180015supp2_prod.pdf | PDF | PLAN | EPOCH statistical analysis plan, primary/secondary analysis definitions, model descriptions and R code; classified as analysis-plan material by content, including retrospective grammatical phrasing. | PDF_PAGE | 7 | 7 | 0 |
| DOC-004 | joi180015supp3_prod.pdf | PDF | REPORT | Supplementary results: eFigures 1-2, eTables 1-5, outcome definitions, hospital-level results, ICU resource utilization and sample assumptions/post-trial calculations. | PDF_PAGE | 14 | 14 | 0 |

No physically bound source combines REPORT and PLAN roles. Outcome definitions and pre-trial assumptions contextualizing the results supplement remain REPORT content; source roles may be checked at an exact cited location during classification confirmation.

Structural source inspection engine: direct `pdfinfo` 25.03.0. Content/role inspection engine: direct `pdftotext` 25.03.0, first two physical pages plus source-matched full native/layout page structure. All PDFs are unencrypted, US letter, with stable physical page counts 11, 37, 7 and 14. Direct tools were used; no Python extraction, OCR, Office conversion, web or sibling-package inspection occurred.
