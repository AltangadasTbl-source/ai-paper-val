# Workflow 1.6.1 Direct Source Inventory

Status: COMPLETE. Specialist inference: PASS. The current package alone was inventoried using direct local tools. Five supplied PDF sources and no supplied DOC, DOCX, XLS, XLSX, or CSV sources were found. Derived legacy PDFs are evidence assets, not direct sources. No source or pre-existing artifact was modified.

| Source ID | Source path | Format | Stable unit type | Total units | Document role | Content basis | Downstream mapping assignment |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_saynorea_2019_oi_190106_1635377898.43062.pdf | PDF | PDF_PAGE | 14 | REPORT | Main randomized-trial article; title and reported results on p. 1; tables/figures through p. 11 and contributor, disclosure, and reference context through p. 14. | main_quantitative_mapper; all pages 1-14, including context-only pages |
| DOC-002 | joi190106supp1_prod_1635377898.47058.pdf | PDF | PDF_PAGE | 75 | PLAN | Trial protocol, identified by source cover and protocol title; prospective trial design and operational material. | support_quantitative_mapper protocol shard; all pages 1-75, including context-only pages |
| DOC-003 | joi190106supp2_prod_1635377898.49605.pdf | PDF | PDF_PAGE | 30 | PLAN | Statistical analysis plan, identified by source cover and Section 1 trial-analysis-plan title. | support_quantitative_mapper SAP shard; all pages 1-30, including context-only pages |
| DOC-004 | joi190106supp3_prod_1635377898.49725.pdf | PDF | PDF_PAGE | 29 | REPORT | Non-plan results supplement; cover enumerates eTables 1-9 and eFigures 1-3. Author affiliations on pp. 28-29 remain in mapping scope. | support_quantitative_mapper results shard; all pages 1-29, including context-only pages |
| DOC-005 | joi190106supp4_prod_1635377898.50723.pdf | PDF | PDF_PAGE | 1 | REPORT | Retrospective data-sharing statement accompanying the published trial; no prospective analysis or operational plan; administrative report content. | support_quantitative_mapper results shard; all pages 1-1, including context-only pages |

Every source is a single-role document by supplied content. No supplied bundle combines REPORT and PLAN content. DOC-005 is administrative REPORT content and may have no applicable quantitative relationships; its single page must still be mapped. Source identification uses the actual cover/content, not the supplement number alone.

Direct-source stable unit total: 149 unique PDF pages. Page counts were obtained with pdfinfo; source content identity was checked with direct pdftotext. SHA-256 was obtained with sha256sum using package-relative paths and is recorded in source_hashes_before.sha256. The legacy .ai_paper_validation/document_outputs/DOC-004/supp3-p7.pdf is a one-page derivative of DOC-004 p. 7 and is excluded from the direct-source count.

