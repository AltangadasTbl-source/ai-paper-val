# Workflow 1.6.2 Source Inventory

The package contains five direct PDF sources and no direct DOC, DOCX, XLS, XLSX, or CSV sources. Software fixtures inside the temporary tooling environment are excluded. Unit counts were obtained with the recorded fallback command `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py info SOURCE`; engine: PyMuPDF 1.26.4. SHA-256 was obtained with direct `sha256sum`. Sources and existing artifacts remain unchanged.

| Source ID | Source path | Format | Units | Document role | Content basis and bundle status |
|---|---|---|---:|---|---|
| DOC-001 | jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf | PDF | 11 | REPORT | Published main article reporting the Budesonide in Babies randomized clinical trial; pages 1–11. No PLAN bundle. |
| DOC-002 | joi250072supp1_prod_1761000786.68881.pdf | PDF | 35 | PLAN | Study protocol: title and contents, protocol version 3.0, prospective study procedures and analysis. Pages 1–35. No REPORT bundle. |
| DOC-003 | joi250072supp2_prod_1761000786.6938.pdf | PDF | 162 | PLAN | Manual of Procedures with prospective operational forms, treatment, screening, follow-up and data procedures; pages 1–162. No REPORT bundle. |
| DOC-004 | joi250072supp3_prod_1761000786.6988.pdf | PDF | 48 | PLAN | One full statistical analysis plan v1.3 dated 10 September 2024, with revision history for v1.0–1.2; pages 1–48. Prospective analysis specifications remain PLAN. No REPORT bundle. |
| DOC-005 | joi250072supp4_prod_1761000786.6988.pdf | PDF | 16 | REPORT | Non-plan results supplement, eTables 1–8; pages 1–16. No PLAN bundle. |

Total unique source units: 272 PDF_PAGE units. Content roles are assigned from document content, not supplement numbering. Prior document-record scope exclusions are historical metadata and do not apply to this review. Every direct-source page is assigned downstream.

Source integrity baseline: source_hashes_before.sha256, using package-relative source paths. Existing manifests identify source filenames and page counts; no historical source-hash baseline was located. Reusable asset identity is based on source identifiers, exact page locators and matching content; it does not imply a cryptographic historical source match.
