# Direct Source Inventory — Workflow 1.6.2

Every direct PDF, DOC, DOCX, XLS, XLSX, and CSV file was sought within the current paper package, excluding generated audit derivatives and workflow controls. Four supplied PDFs were found; no supplied Office/workbook/CSV source was found. Direct pdfinfo confirms physical-page counts and no encryption. One unit is one one-based physical PDF page, including reference, cover, and administrative pages. Full SHA-256 values are in source_hashes_before.sha256.

| Source ID | Package-relative source path | Legacy document ID | Format | Stable unit type | Total units | Document role | Content basis |
|---|---|---|---|---|---:|---|---|
| DOC-001 | jama_laslett_2024_oi_240048_1727199125.7595.pdf | DOC-JAMA2024-6063-MAIN-2f574565 | PDF | PDF_PAGE | 10 | REPORT | Page 1 identifies JAMA Original Investigation and reports the randomized trial; pp. 1–10 form the main report. |
| DOC-002 | joi240048supp1_prod_1727199125.7845.pdf | DOC-JAMA2024-6063-SUPP1-317ff46a | PDF | PDF_PAGE | 15 | PLAN | Page 1 identifies the trial protocol, version 02, February 2016; protocol content spans pp. 1–15. |
| DOC-003 | joi240048supp2_prod_1727199125.8245.pdf | DOC-JAMA2024-6063-SUPP2-57681138 | PDF | PDF_PAGE | 1 | PLAN | Page 1 identifies the Statistical analysis plan and prospective analysis statements, excerpted from the February 2016 protocol. |
| DOC-004 | joi240048supp3_prod_1727199125.83025.pdf | DOC-JAMA2024-6063-SUPP3-67e172cd | PDF | PDF_PAGE | 15 | REPORT | Page 1 indexes non-plan eTables 1–8 and an eFigure; pp. 2–15 contain results and illustration. |

Role assignments are based on current supplied source content inspected with direct pdftotext -f 1 -l 1 SOURCE -; no mixed REPORT/PLAN bundle was identified. Source identities were verified with sha256sum -- SOURCE and counts with pdfinfo SOURCE.

Mapping assignments: main mapper owns DOC-001 pp. 1–10; support mapper owns DOC-002 pp. 1–15, DOC-003 p. 1, and DOC-004 pp. 1–15. There are no uncovered text units; the complete disjoint union of 39 reusable-backed pages and two fresh-required protocol pages requires new mapping. Protocol pp. 4–5 have historical numeric figures absent from reusable text; new CPU renders and the support map close both units. Results-supplement table map: p2 eTable1; p3 eTable2; p4 eTable3; pp5–7 eTable4; p8 eTable5; p9 eTable6; pp10–13 eTable7; p14 eTable8; p15 eFigure. No legacy scope exclusion is adopted.

