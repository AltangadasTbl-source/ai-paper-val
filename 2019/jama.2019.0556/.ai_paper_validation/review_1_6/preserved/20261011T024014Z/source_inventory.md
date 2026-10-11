# Workflow 1.6 Source Inventory

Inventory is complete for the current package only. Recursive package file inventory found five direct PDFs and no DOC, DOCX, XLS, XLSX, or CSV sources. Unit counts were independently obtained with direct Poppler pdfinfo 26.01.0; identity hashes were obtained with direct sha256sum. PDF physical page numbers are the stable units, regardless of printed pagination. All sources are unencrypted and have native text. Content-role inspection used direct pdftotext 26.01.0 on title/contents pages; it did not use legacy scientific decisions.

| Source ID | Source path | Unit type | Total units | Document role | Content basis and bundle notes |
|---|---|---|---:|---|---|
| DOC-001 | jama_bot_2019_oi_190007.pdf | PDF_PAGE | 11 | REPORT | Published MooDFOOD randomized clinical trial main article, with observed outcomes and results tables; no bound plan bundle. |
| DOC-002 | joi190007supp1_prod.pdf | PDF_PAGE | 60 | PLAN | Trial protocol, version 7 dated July 11, 2017 with final amendments; protocol material and its background remain PLAN. |
| DOC-003 | joi190007supp2_prod.pdf | PDF_PAGE | 5 | PLAN | MooDFOOD Analysis Plan Prevention Trial Data, prospective research questions, outcomes, covariates and planned analyses. |
| DOC-004 | joi190007supp3_prod.pdf | PDF_PAGE | 25 | REPORT | Non-plan supplementary online content: recruitment, interventions, analytical explanations and observed results appendices; no bound protocol/SAP document. Contextual descriptions within this results supplement retain REPORT role. |
| DOC-005 | joi190007supp4_prod.pdf | PDF_PAGE | 1 | REPORT | Publication-linked data-sharing statement describing available study data and access; non-plan administrative report. No reported quantitative results expected, but its complete page is assigned for mapping. |

Total: five sources, 102 PDF_PAGE units; three REPORT documents (37 pages), two PLAN documents (65 pages). Mixed REPORT/PLAN bound bundles: none identified by content.

Source integrity baseline: source_hashes_before.sha256, containing package-relative paths. All five direct hashes match the existing extraction identity manifest. Derivatives are aids; exact supplied source pages remain final authority.

Commands: `pdfinfo "SOURCE.pdf"`; `pdftotext -f 1 -l 2 "SOURCE.pdf" -`; `sha256sum -- "SOURCE.pdf"`. Direct native character counts for shard planning (not new derivatives): protocol 98,846, SAP 12,925, results supplement 40,366, data-sharing statement 1,121; entire support union 153,258 characters, below the 200,000-character shard bound. Rendered pages should be requested in bounded batches of at most 32.
