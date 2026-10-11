# Workflow 1.6.2 Source Inventory

The direct-source inventory searched the current package recursively for PDF, DOC, DOCX, XLS, XLSX, and CSV files, including hidden audit locations. Three supplied PDFs were found. No supplied Office documents or CSV files are present. Workflow code, configurations, and audit derivatives are not supplied scientific sources.

| Source ID | Source path | Format | Unit type | Total units | Document role | Identity and role basis |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_wang_2018_oi_180070.pdf | PDF | PDF_PAGE | 10 | REPORT | Wang et al., JAMA 2018;320(3):245–254, doi:10.1001/jama.2018.8802; original trial report. PDF pp. 1–10 correspond to printed pp. 245–254. |
| DOC-002 | joi180070supp1_prod.pdf | PDF | PDF_PAGE | 25 | PLAN | GOLDEN BRIDGE–Acute Ischemic Stroke protocol dated 2014/4/17; prospective trial specification with statistical analysis plan on PDF pp. 18–19, intervention and outcome definitions, and references. Entire bundle is PLAN; no REPORT portion. |
| DOC-003 | joi180070supp2_prod.pdf | PDF | PDF_PAGE | 9 | REPORT | Supplementary Online Content for the same article: eAppendix baseline survey and eTables 1–4. Results and measurement definitions accompany the trial report; no prospective plan bundle. |

Total unique source units: 44 PDF pages. Identity checked using direct pdfinfo (Poppler 25.03.0); current metadata, file sizes, and page counts agree with the reusable metadata for all three sources. The main PDF is 505453 bytes, plan PDF 735518 bytes, and report supplement PDF 334922 bytes. All are unencrypted. Direct sha256sum hashes are recorded using package-relative paths in source_hashes_before.sha256.

Source-page content anchors were checked with direct pdftotext (Poppler 25.03.0), independently on every page, against the page-delimited reusable native and layout text. This was an asset fitness/identity check, not scientific candidate discovery. Plan p. 5 contains an image-only flow diagram in addition to its native caption; its reusable full-page image was inspected visually. No source was modified.

The assigned mapping partition is main mapper: DOC-001 PDF pp. 1–10; support mapper: DOC-002 PDF pp. 1–25 and DOC-003 PDF pp. 1–9. All units require new scientific mapping; none requires fresh extraction as a prerequisite.
