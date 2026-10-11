# Direct source inventory

Inventory scope: this paper package only. The three supplied sources are PDFs. No direct DOC, DOCX, XLS, XLSX, or CSV is present. Stable units are physical PDF pages, including cover, references, forms, scanned material, and otherwise blank pages. Counts use direct Poppler pdfinfo 25.03.0. SHA-256 uses direct sha256sum; package-relative hashes are recorded in source_hashes_before.sha256. No source or legacy artifact was modified.

| Source ID | Source path | Format | Document role | Unit type | Total units | Content basis |
|---|---|---|---|---|---:|---|
| DOC-001 | jama_jabre_2018_oi_180004.pdf | PDF | REPORT | PDF_PAGE | 9 | Original Investigation reporting the randomized CAAM clinical trial, results, tables, figures, and references. |
| DOC-002 | joi180004supp1_prod.pdf | PDF | PLAN | PDF_PAGE | 134 | Cover lists original protocol, final protocol, amendments, summary of changes, and original statistical analysis plan. The bound bundle remains PLAN throughout; it contains multiple protocol versions and prospective analysis material, not a mixed REPORT/PLAN bundle. |
| DOC-003 | joi180004supp2_prod.pdf | PDF | REPORT | PDF_PAGE | 3 | Supplementary Online Content with investigator-centre contributions and post-hoc analyses, a non-plan results supplement. |

Direct commands: pdfinfo "jama_jabre_2018_oi_180004.pdf"; pdfinfo "joi180004supp1_prod.pdf"; pdfinfo "joi180004supp2_prod.pdf"; sha256sum -- each exact source path. Roles were assigned from direct pdftotext inspection of each cover/opening page, not supplement numbering.

All 146 physical page units require fresh scientific mapping, even when backed by reusable extraction. Reusable coverage is not scientific mapping completion. No old candidate, checker, screening, verification, critic, quality, classification, or final-report conclusion was used for inventory or scope.
