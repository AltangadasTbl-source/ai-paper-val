# Direct source inventory

All supplied PDF, DOC, DOCX, XLS, XLSX, and CSV files in the current package were inventoried; four PDFs and no Office/workbook/CSV sources were found. Unit type is PDF_PAGE. Counts were independently confirmed using the bundled pdf_tools.py info command and PyMuPDF 1.26.4 in the temporary package-local environment. All PDFs are unencrypted. sha256sum produced package-relative integrity records; all four current hashes match existing document identity metadata.

| Source ID | Source path | Format | Total units | Document role | Content basis and complete scope |
|---|---|---|---:|---|---|
| DOC-001 | jama_summers_2025_oi_250040_1753124024.36498.pdf | PDF | 10 | REPORT | Original Investigation, Augmented Enteral Protein During Critical Illness: The TARGET Protein Randomized Clinical Trial; PDF pp. 1-10. |
| DOC-002 | joi250040supp1_prod_1753124024.37199.pdf | PDF | 40 | PLAN | TARGET Protein trial protocol, including prospective substudy material; title and contents identify Research Plan, Data Management, and Analysis and Reporting of Results; PDF pp. 1-40. |
| DOC-003 | joi250040supp2_prod_1753124024.37799.pdf | PDF | 31 | PLAN | TARGET Protein statistical analysis plan for a cluster randomized cross-sectional double cross-over trial; PDF pp. 1-31. |
| DOC-004 | joi250040supp3_prod_1753124024.38098.pdf | PDF | 34 | REPORT | Non-plan results supplement with eMethods, eTables 1-14, eFigures 1-7, ICEMAN material and references; PDF pp. 1-34. |

No mixed REPORT/PLAN bound bundle was identified. Existing metadata's former scientific scope exclusions are not adopted: every page, including plan bodies, appendix material and reference pages, is assigned to current mapping. The two PLAN sources have unusable encoded native text, but readable reusable OCR and rendered pages support complete mapping. Current scientific discovery does not use old selection, classification, screening or disposition artifacts.

Direct info command pattern: `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py info "SOURCE.pdf"` (engine PyMuPDF 1.26.4; CPU metadata parsing). A preliminary confirmation also used the user-authorized ~/venvs/stt/bin/python, PyMuPDF 1.28.0; the package-local pinned confirmation supersedes it. No derivative was created by these info commands.
