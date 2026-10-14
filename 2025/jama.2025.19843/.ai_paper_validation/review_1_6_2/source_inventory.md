# Workflow 1.6.2 direct-source inventory

Inventory scope: current package only. Six supplied PDFs; no supplied DOC, DOCX, XLS, XLSX, or CSV files. Source identity and page counts were freshly checked using the recorded missing-tool fallback: `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py info "source.pdf"` (PyMuPDF 1.26.4). All PDFs are unencrypted. Direct `sha256sum` produced package-relative identities in source_hashes_before.sha256. Content headings from direct first-page native extraction and reusable page images establish roles; legacy review conclusions and legacy restrictions on scientific scope are not inputs.

| Source ID | Source path | Unit type | Total units | Document role | Content basis | Mapping scope |
|---|---|---|---:|---|---|---|
| DOC-001 | jama_combes_2025_oi_250087_1766516490.94011.pdf | PDF_PAGE | 10 | REPORT | Original investigation, Methods and Results | PDF pp. 1-10 |
| DOC-002 | joi250087supp1_prod_1766516490.96011.pdf | PDF_PAGE | 153 | PLAN | Protocol bundle with original, second, final versions and change summary | PDF pp. 1-153 |
| DOC-003 | joi250087supp2_prod_1766516490.96511.pdf | PDF_PAGE | 9 | PLAN | Statistical analysis plan, final version 11/04/2025; scanned pages | PDF pp. 1-9 |
| DOC-004 | joi250087supp3_prod_1766516490.97011.pdf | PDF_PAGE | 18 | REPORT | Supporting methods, eTables 1-6 and eFigures 1-9 | PDF pp. 1-18 |
| DOC-005 | joi250087supp4_prod_1766516490.97511.pdf | PDF_PAGE | 3 | REPORT | Retrospective nonauthor collaborator roster; no prospective analysis specification | PDF pp. 1-3 |
| DOC-006 | joi250087supp5_prod_1766516490.97511.pdf | PDF_PAGE | 1 | REPORT | Data-sharing statement linked to published report | PDF p. 1 |

No bundle contains both REPORT and PLAN content. Administrative REPORT sources remain mandatory mapping units; their numeric/result relevance is determined by the fresh mapper rather than omission at inventory.

Protocol layout text contains 153 form-feed-delimited page records: 150 substantive usable text pages, empty records at PDF pp.4 and49, and a footer-only record at p.95 whose signed-page image was identified and freshly mapped by the coverage audit. All three pages require fresh direct rendering and inspection; that inspection is complete. Three disjoint protocol mapping scopes have normalized character counts below the 200000-character context bound: pp. 1-51 = 177937; pp. 52-102 = 192438; pp. 103-153 = 179184. Counts include the supplied text body and omit separating form-feed characters. Split scopes are context bounds, not scientific sampling.
