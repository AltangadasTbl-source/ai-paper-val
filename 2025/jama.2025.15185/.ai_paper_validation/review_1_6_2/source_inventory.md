# Direct Source Inventory

Fresh curation excludes every pre-existing workflow 1.6.2 artifact, as requested by the user. Only supplied PDFs and older document_outputs/review_1_5_1 factual extraction assets are used. Direct package inventory finds seven PDFs and no DOC, DOCX, XLS, XLSX, or CSV sources. Each PDF page is one stable unit. Total: 159 units.

| Source ID | Source path | Document role | Content and role basis | Unit type | Total units | Identity/tool |
|---|---|---|---|---|---:|---|
| DOC-001 | jama_engelter_2025_oi_250066_1761597796.45511.pdf | REPORT | Main trial article with reported results | PDF_PAGE | 10 | Pinned PyMuPDF 1.26.4 info; SHA-256 in source_hashes_before.sha256 |
| DOC-002 | joi250066supp1_prod_1761597796.4601.pdf | PLAN | Trial protocol bundle; prospective objectives, interventions, analysis rules and multiple protocol versions | PDF_PAGE | 94 | Pinned PyMuPDF 1.26.4 info; SHA-256 in source_hashes_before.sha256 |
| DOC-003 | joi250066supp2_prod_1761597796.4701.pdf | PLAN | Statistical analysis plan: objectives and prospective analysis procedures. First page bears Final Report wording, but page 10 explicitly specifies analyses that will be performed; role follows content. Mapper must distinguish any embedded reporting material by location. | PDF_PAGE | 18 | Pinned PyMuPDF 1.26.4 info; SHA-256 in source_hashes_before.sha256 |
| DOC-004 | joi250066supp3_prod_1761597796.4701.pdf | REPORT | Non-plan results supplement: eTables, estimands, outcomes, safety and figures | PDF_PAGE | 27 | Pinned PyMuPDF 1.26.4 info; SHA-256 in source_hashes_before.sha256 |
| DOC-005 | joi250066supp4_prod_1761597796.4751.pdf | REPORT | Published nonauthor collaborator list; administrative results-package material rather than prospective plan | PDF_PAGE | 8 | Pinned PyMuPDF 1.26.4 info; SHA-256 in source_hashes_before.sha256 |
| DOC-006 | joi250066supp5_prod_1761597796.4751.pdf | REPORT | ESTREL Main Analysis Code; implementation supplied with report, including imputation pooling and primary model | PDF_PAGE | 1 | Pinned PyMuPDF 1.26.4 info; SHA-256 in source_hashes_before.sha256 |
| DOC-007 | joi250066supp6_prod_1761597796.4801.pdf | REPORT | Published data sharing statement | PDF_PAGE | 1 | Pinned PyMuPDF 1.26.4 info; SHA-256 in source_hashes_before.sha256 |

Direct-source count command: package-local find for PDF/DOC/DOCX/XLS/XLSX/CSV, excluding temporary tooling dependencies. Information command for each exact filename: `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py info SOURCE`. Engine: pymupdf. Hash engine: direct sha256sum. Source hash paths are package-relative. No sibling packages or web sources were accessed.
