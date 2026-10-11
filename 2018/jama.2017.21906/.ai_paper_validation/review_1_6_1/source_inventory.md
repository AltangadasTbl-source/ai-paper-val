# Direct Source Inventory

Inventory scope is the current package only. All direct PDF, DOC, DOCX, XLS, XLSX, and CSV files were enumerated, excluding generated audit derivatives. Four PDF sources were found; no direct Office, workbook, or CSV sources exist. PDF page numbers below are physical source pages, including covers, references, administrative material, and blank forms. Roles are assigned by content, not filenames.

| Source ID | Source path | Format | Unit type | Total units | Document role by content | Content and role locations | SHA-256 |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_huffman_2018_oi_170166.pdf | PDF | PDF_PAGE | 12 | REPORT | Main ACS QUIK randomized clinical trial article, physical pp. 1–12. | 11311a6bb5c7a4be734ed60776b308f525ad101671ccc8d34bab18735aaca5f5 |
| DOC-002 | joi170166supp1_prod.pdf | PDF | PDF_PAGE | 32 | PLAN | ACS QUIK Protocol Version 22 September 2014, physical pp. 1–32, including prospective procedures and consent appendices. | 0e13bdfc6e5e3c8b86e187f54f0a3d7d0217fc0614be9fbdbbb7839dbab9004a |
| DOC-003 | joi170166supp2_prod.pdf | PDF | PDF_PAGE | 9 | PLAN | ACS QUIK Statistical Analysis Plan 17 June 2015, physical pp. 1–9. | d49019c3cf6ee0766fb319f254f27f87751a73bfec66c34d38bae16a956bb1c6 |
| DOC-004 | joi170166supp3_prod.pdf | PDF | PDF_PAGE | 27 | REPORT and PLAN mixed bundle | REPORT p. 1 contents/provenance and pp. 17–27 trial eTables/eFigures; PLAN pp. 2–16 toolkit cover, sample audit/feedback templates and prospective admission/discharge checklists. | 511f4a907e4c48d920f1c6b89d444fe76c7c91e11bbae84cdee834fa0393f3ec |

DOC-004 toolkit pages are operational intervention material. The appendix heading identifies a sample audit and feedback report; p. 6 expressly labels a Sample Hospital and historical demonstration period; pp. 15–16 are blank admission/discharge forms. Sample template values are not trial outcome observations. Each downstream comparison must retain the role of its exact page.

Direct page counts were confirmed with pdfinfo (Poppler 25.03.0). Hashes were calculated with sha256sum and recorded using package-relative paths. Every native extraction matches the present source byte-for-byte when reproduced with pdftotext. No supplied source or legacy artifact was changed.
