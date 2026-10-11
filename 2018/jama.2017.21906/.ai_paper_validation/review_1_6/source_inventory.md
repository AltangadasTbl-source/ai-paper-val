# Direct Source Inventory

Four direct PDFs are present in this paper package. There are no direct DOC, DOCX, XLS, XLSX, or CSV sources. Audit derivatives are not direct sources. The stable unit is one physical PDF page, including covers, references, and administrative pages; total scope is 80 unique units.

| Source ID | Source path | Format | Stable units | Document role | Content and source binding |
|---|---|---|---:|---|---|
| DOC-001 | jama_huffman_2018_oi_170166.pdf | PDF | 12 | REPORT | ACS QUIK trial main article, physical PDF pp. 1-12 (printed pp. 567-578). Current native extraction exactly matches reusable native text. Current PDF metadata matches reusable pdfinfo, including the August 2026 modification date. |
| DOC-002 | joi170166supp1_prod.pdf | PDF | 32 | PLAN | ACS QUIK protocol version 22 September 2014, pp. 1-32, including historical background, consent forms, and operational appendices. Protocol p. 14 contains Time and Events material inadequately represented by text and requires fresh visual mapping. |
| DOC-003 | joi170166supp2_prod.pdf | PDF | 9 | PLAN | Statistical Analysis Plan revised 17 June 2015, physical PDF pp. 1-9. Cover and prospective analysis details establish PLAN role. |
| DOC-004 | joi170166supp3_prod.pdf | PDF | 27 | REPORT; PLAN | Mixed bundle. Index p. 1 and results eTables/eFigures pp. 17-27 are REPORT. Toolkit eAppendix pp. 2-16 contains prospective operational materials, historical/sample audit-and-feedback data, admission/discharge checklists; these locations are PLAN. Role must be assigned by compared content rather than supplement filename. |

Hashes are in source_hashes_before.sha256, with package-relative source paths. PDF page counts and identity were obtained directly using pdfinfo 25.03.0; hashing uses direct sha256sum. Fresh native/layout comparison used direct pdftotext 25.03.0 to stdout and cmp. None of these commands modifies supplied sources or legacy derivatives.

All four existing native-text files match direct current extraction byte for byte. Three support layout-text files also match byte for byte. The main layout derivative differs in whitespace and vertical placement/order of labels on rotated graphics under the current Poppler version; source/native text identity remains exact. Treat layout as a locator, with images/direct pages for figure positions.

No older candidate, verifier, critic, endetail, classification, or report content was read for this inventory.
