# Direct-source inventory

Inventory covers every supplied PDF, DOC, DOCX, XLS, XLSX and CSV in this package. Four direct PDFs were found; no supplied Office or CSV source exists. Workflow files and audit derivatives are not direct sources. Source identity and page counts were obtained with direct pdfinfo 26.01.0; content roles were checked with direct pdftotext first-page inspection. SHA-256 uses sha256sum.

| Source ID | Source path | Format | Document role | Unit type | Total units | Content and stable units |
|---|---|---|---|---|---:|---|
| DOC-001 | jama_urashima_2019_oi_190023.pdf | PDF | REPORT | PDF_PAGE | 9 | Main article; all nine pages, including article information and references on page 9. |
| DOC-002 | joi190023supp1_prod.pdf | PDF | PLAN | PDF_PAGE | 45 | Protocol/SAP bundle: initial version pp. 2–16, final version pp. 17–33, references pp. 34–35, appendices pp. 36–44 and amendment summary p. 45; p. 1 is contents. No REPORT section identified. |
| DOC-003 | joi190023supp2_prod.pdf | PDF | REPORT | PDF_PAGE | 41 | Results supplement: contents, eFigures and eTables, pp. 1–41. |
| DOC-004 | joi190023supp3_prod.pdf | PDF | REPORT | PDF_PAGE | 1 | Published data-sharing statement; supporting report administration, not prospective statistical design. |

All page numbers are physical PDF page numbers, indexed from 1. None of the supplied PDFs is encrypted. Bound-plan version comparisons remain PLAN versus PLAN. Legacy by-design exclusions are not carried into this workflow; every direct-source page enters mapper scope.
