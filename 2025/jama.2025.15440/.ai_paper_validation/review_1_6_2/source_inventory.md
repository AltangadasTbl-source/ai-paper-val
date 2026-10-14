# Direct-source inventory

Inventory scope is the current paper package, including all direct PDF, DOC, DOCX, XLS, XLSX and CSV files. Exactly four direct PDFs were located; no supplied Office or CSV sources were located. Stable units are physical PDF pages, including covers, contents, methods and references. Counts were confirmed directly with the recorded fallback helper, PyMuPDF 1.26.4. SHA-256 values match the retained document-identity records; legacy processing boundaries do not restrict this run.

| Source ID | Source path | Document role | Content basis | Unit type | Total units | SHA-256 |
|---|---|---|---|---|---:|---|
| DOC-001 | jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf | REPORT | Main AMALFI randomized clinical trial article: structured abstract, Methods, Results, tables, figures and references; fresh page 1 native locator confirms identity. | PDF_PAGE | 9 | 4bb1cfc9284d00a83984f493da34bab05357d4cca69abf0c06a281a5597fd927 |
| DOC-002 | joi250068supp1_prod_1760999665.28862.pdf | PLAN | AMALFI trial protocol version 2.0, 2021-06-08; fresh page 1 render visually confirms prospective protocol identity. | PDF_PAGE | 26 | 3f599193f39b562d392dc919161fd3afa8c728d8652738f9c971ca327c01047a |
| DOC-003 | joi250068supp2_prod_1760999665.29862.pdf | PLAN | Statistical Analysis Plan version 1.2, 26 June 2025, aligned with protocol version 2.0; fresh page 1 native locator confirms identity. | PDF_PAGE | 24 | f8b6cb7ad9f52502035f24b476c23d76c09d3459375b8f34f234a4f060c1d892 |
| DOC-004 | joi250068supp3_prod_1760999665.30362.pdf | REPORT | Supplemental Online Content with eMethods, eTables 1–3 and eFigures 1–4; fresh page 1 contents identify reported analyses and results. | PDF_PAGE | 11 | b23b7b0f4699d6a025bf18e7f95e6098372a122b8bdb0f7580ac82c29638d01a |

No mixed REPORT/PLAN bundle was identified. Document roles are assigned by content rather than supplement numbering. Total direct-source scope: 70 PDF pages.

Commands used: recursive package-local file inventory by extension; `sha256sum -- SOURCE`; `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py info SOURCE` for each PDF. Fresh identity locators: `preprocessing/curator-DOC-001-p1.txt`, `preprocessing/curator-DOC-002-p1.txt`, `preprocessing/curator-DOC-003-p1.txt`, `preprocessing/curator-DOC-004-p1.txt`; engine PyMuPDF 1.26.4, native text, CPU. Protocol visual identity: `preprocessing/curator-DOC-002-p1.png`; engine PyMuPDF 1.26.4, 200 dpi render, CPU. No fresh OCR was performed by the curator.
