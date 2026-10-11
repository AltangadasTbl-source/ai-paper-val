# Direct-source inventory

Inventory scope: the current package only; all PDF, DOC, DOCX, XLS, XLSX, and CSV files were enumerated. Four PDFs and no Office or CSV sources are supplied. Every PDF is unencrypted and locally readable. Unit counts are current direct `pdfinfo` counts; identity hashes are in source_hashes_before.sha256.

| Source ID | Source path | Format | Document role | Total units | Content basis and bundle note |
|---|---|---|---|---:|---|
| DOC-001 | jama_cooper_2018_oi_180132.pdf | PDF | REPORT | 10 | Main published POLAR randomized clinical trial article; title, abstract, methods, results, tables, figures and references. |
| DOC-002 | joi180132supp1_prod.pdf | PDF | PLAN | 194 | Bound trial protocols and amendments, SAP versions and updates, DSMC stopping rules and DSMC reports. The bundle contains prospective plan material plus interim operational reporting; its protocol/SAP/DSMC governance content establishes PLAN. Comparisons within the bound plan bundle remain plan-internal. Embedded DSMC result displays are identified by content during mapping. |
| DOC-003 | joi180132supp2_prod.pdf | PDF | REPORT | 24 | Non-plan supplementary results: eTables 1–13, eFigures 1–7, per-protocol, as-treated and post hoc analyses, and references. |
| DOC-004 | joi180132supp3_prod.pdf | PDF | REPORT | 1 | Published data-sharing statement; no prospective statistical analysis specification. |

Direct-tool engines: pdfinfo and pdftotext Poppler 25.03.0; sha256sum. Four supplied source hashes were recorded by the coordinator before inventory and remain untouched. Native-text identity was checked by byte comparison with current direct-source pdftotext output for every document, without creating persistent duplicate derivatives.
