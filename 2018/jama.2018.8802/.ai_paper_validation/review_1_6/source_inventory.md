# Direct-source inventory

Scope: every direct PDF, DOC, DOCX, XLS, XLSX, and CSV in this paper package. Case-insensitive extension inventory found three PDFs and no Office/workbook/CSV sources. No sibling package, external source, or old candidate/report content was inspected.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis | Bundle roles |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_wang_2018_oi_180070.pdf | PDF | PDF_PAGE | 10 | REPORT | Main published randomized trial article; abstract, methods, results, tables, figures, references | REPORT only |
| DOC-002 | joi180070supp1_prod.pdf | PDF | PDF_PAGE | 25 | PLAN | Dated 2014/4/17 prospective GOLDEN BRIDGE-AIS trial protocol; eligibility, intervention, outcome definitions, sample-size planning, and Statistical analysis plan on PDF pp. 18–20 | PLAN only, including historical/background figures and references |
| DOC-003 | joi180070supp2_prod.pdf | PDF | PDF_PAGE | 9 | REPORT | Supplementary Online Content; baseline-survey eAppendix, performance-measure specifications and eTables 2–4 containing reported trial results | REPORT only |

Source counts were obtained with direct pdfinfo 25.03.0. All PDFs are unencrypted. PDF page counts are physical source page counts, including covers and references; source IDs match the existing page/text namespace. Direct hashes are recorded using sha256sum with package-relative paths in source_hashes_before.sha256.

Commands: pdfinfo "jama_wang_2018_oi_180070.pdf"; pdfinfo "joi180070supp1_prod.pdf"; pdfinfo "joi180070supp2_prod.pdf". Identity and role were checked against direct pdftotext output as well as source-linked reusable extraction. No supplied bundle mixes REPORT and PLAN content.
