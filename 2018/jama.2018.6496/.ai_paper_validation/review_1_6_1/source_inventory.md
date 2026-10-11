# Direct-source inventory

Inventory is limited to the current package. All supplied PDF, DOC, DOCX, XLS, XLSX, and CSV files were enumerated, excluding workflow controls and audit derivatives. Three direct PDFs are present; no direct Office or CSV sources are present. Stable units are physical PDF pages, counted by `pdfinfo` (Poppler 25.03.0). Source hashes are recorded with package-relative paths in `source_hashes_before.sha256`.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_driver_2018_oi_180054.pdf | PDF | PDF_PAGE | 11 | REPORT | Published randomized-trial article, titled Effect of Use of a Bougie vs Endotracheal Tube and Stylet on First-Attempt Intubation Success Among Patients With Difficult Airways Undergoing Emergency Intubation. |
| DOC-002 | joi180054supp1_prod.pdf | PDF | PDF_PAGE | 25 | PLAN | Clinical Trial Protocol for Bougie use in Emergency Airway Management (BEAM); pp. 19-21 contain planned statistical methods, populations and interim analysis. |
| DOC-003 | joi180054supp2_prod.pdf | PDF | PDF_PAGE | 13 | REPORT | Non-plan Supplementary Online Content: eTable 1 pp. 2-3; eFigure 1 p. 4; procedural eFigure 2 p. 5; interim analysis results p. 6; postintubation data form pp. 7-13. |

DOC-003 is primarily a results supplement. Its pp. 7-13 reproduce an operational data-collection instrument, which is prospective operational content and should be treated as PLAN if a checker compares a specification from the instrument itself. Page 6 quotes a protocol rule and reports its application: distinguish the quoted PLAN specification from the REPORT interim results. The bundle is not a separate SAP or protocol version. Roles of exact compared locations must be confirmed from content at recheck.

Every PDF is unencrypted and has a native text layer. Existing text assets cover all physical pages. No extraction asset or source was modified. Old candidate, checker, screening, verifier, critic, endetail, classification or final-report content was not read.
