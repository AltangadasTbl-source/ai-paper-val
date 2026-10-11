# Direct source inventory

Inventory scope is the current package only. Five direct PDFs were found; no DOC, DOCX, XLS, XLSX, or CSV source exists. Audit derivatives are not direct sources. Stable source units are one physical PDF page, including covers, references, and administrative pages. Counts and identity were obtained with direct Poppler pdfinfo 25.03.0 and sha256sum; PDF encryption is absent. SHA-256 values are recorded in source_hashes_before.sha256 using package-relative paths.

| Source ID | Source path | Document role | Content basis | Stable unit type | Total units | Exact unit scope | Bundle composition |
|---|---|---|---|---|---:|---|---|
| DOC-001 | jama_simonis_2018_oi_180108.pdf | REPORT | Main JAMA randomized trial article: low versus intermediate tidal volume and ventilator-free days | PDF_PAGE | 9 | Physical PDF pages 1–9 | Report only |
| DOC-002 | joi180108supp1_prod.pdf | PLAN | Cover identifies Trial protocol; study protocol, prospective procedures, analysis sections, references, and appendices | PDF_PAGE | 49 | Physical PDF pages 1–49 | Plan only; no results-report bundle |
| DOC-003 | joi180108supp2_prod.pdf | PLAN | Study update and detailed statistical analysis plan, version 1.0 dated November 24, 2017 | PDF_PAGE | 22 | Physical PDF pages 1–22 | Plan only |
| DOC-004 | joi180108supp3_prod.pdf | REPORT | Non-plan supplementary methods, references, result eTables, and eFigures | PDF_PAGE | 13 | Physical PDF pages 1–13 | Report only |
| DOC-005 | joi180108supp4_prod.pdf | REPORT | Data sharing statement accompanying the published report; retrospective data-availability statement, no prospective analysis plan | PDF_PAGE | 1 | Physical PDF page 1 | Report only; no result-bearing numerical content |

Content roles were established from supplied PDF cover/content text, not supplement numbering. No source bundles both REPORT and PLAN content. The data-sharing statement remains in coverage despite having no quantitative relationships.

Canonical mapper assignments: main_quantitative_mapper owns DOC-001 pages 1–9; support_quantitative_mapper owns DOC-002 pages 1–49, DOC-003 pages 1–22, DOC-004 pages 1–13, and DOC-005 page 1. Every page requires fresh scientific mapping even where its extraction is reusable. There are no uncovered extraction units requiring new preprocessing.
