# Direct Source Inventory

Inventory includes every direct PDF, DOC, DOCX, XLS, XLSX, and CSV file in the current package. Five direct PDFs exist; no direct Office or CSV files and no derived PDFs exist. All units are stable one-based PDF pages. Sources were counted with direct `pdfinfo` (Poppler 26.01.0) and hashed with `sha256sum`. Roles below are assigned from current source title/content, not from legacy classifications or scope decisions.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis and bundle notes |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_bot_2019_oi_190007.pdf | PDF | PDF_PAGE | 11 | REPORT | Main JAMA original investigation reporting the MooDFOOD randomized clinical trial; article, references, and investigator material included. |
| DOC-002 | joi190007supp1_prod.pdf | PDF | PDF_PAGE | 60 | PLAN | Protocol, version 7 with final amendments, title and contents identified on PDF pp. 1–4; prospective design, intervention, assessments and statistical specifications. All 60 pages included. |
| DOC-003 | joi190007supp2_prod.pdf | PDF | PDF_PAGE | 5 | PLAN | MooDFOOD Analysis Plan Prevention Trial Data; prospective research proposal and statistical analysis specifications. |
| DOC-004 | joi190007supp3_prod.pdf | PDF | PDF_PAGE | 25 | REPORT | Supplementary Online Content with explanatory appendices and reported adherence, adverse events, symptom, moderation, sensitivity and CACE results. Descriptions of interventions and methods contextualize the results; this is a results supplement, not a bound protocol/SAP bundle. |
| DOC-005 | joi190007supp4_prod.pdf | PDF | PDF_PAGE | 1 | REPORT | Publication-associated data sharing statement, reporting availability of data and documents; no prospective trial design specification. Administrative scope still mapped. |

Total: 5 direct sources, 102 PDF pages. No mixed REPORT/PLAN bundle was identified. Every source is assigned to downstream full-source mapping, including pages described as outside earlier review scopes. No earlier candidate, checker, verifier, critic, screening, endetail, classification, or final report content was used.
