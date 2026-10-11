# Direct Source Inventory

The complete current package was searched recursively for PDF, DOC, DOCX, XLS, XLSX, and CSV sources, excluding generated audit/workflow/control areas. Three direct PDFs are present; no direct Office or CSV source is present. Generated audit images and text are evidence assets, not direct sources. Source roles below were assigned from the current direct cover/contents pages extracted with pdftotext, independently of historical roles.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content and stable units |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_graham_2024_oi_240078_1739900423.19074.pdf | PDF | PDF_PAGE | 9 | REPORT | JAMA Original Investigation: A Vaping Cessation Text Message Program for Adolescent E-Cigarette Users; complete PDF pp. 1-9, including abstract, methods, Tables 1-3, flow figure, discussion and references. |
| DOC-002 | joi240078supp1_prod_1739900423.22574.pdf | PDF | PDF_PAGE | 15 | PLAN | Cover identifies Supplement 1: Study Protocol; original protocol, methods, safety monitoring and summary of changes; complete PDF pp. 1-15. It is a bound plan bundle and contains no results-report document. |
| DOC-003 | joi240078supp2_prod_1739900423.24574.pdf | PDF | PDF_PAGE | 16 | REPORT | Supplementary Online Content: eAppendices A-D, methods details, eTables 1-6 and references; complete PDF pp. 1-16. Methods retrospectively describe the reported study rather than constituting a prospective plan; no plan-report mixed bundle. |

Total direct sources: 3. Total stable source units: 40 PDF pages. Unit identity is physical PDF page, independently of printed pagination. Source SHA-256 values are recorded using package-relative paths in source_hashes_before.sha256.

## Inventory tools and identity checks

Direct pdfinfo (Poppler 26.01.0) established 9, 15 and 16 pages and readable, unencrypted PDF identities. Direct pdftotext (Poppler 26.01.0) extracted current cover/contents pages to standard output for role assignment. Direct sha256sum (uutils coreutils 0.10.0) established immutable-source baselines. No source or legacy asset was modified. All native/page/full-document asset comparisons were exact matches; no new OCR or conversion is required.

## Scope restoration

Historical document/page records excluded the protocol and supplementary pp. 2-3 and 16 from earlier review. Those historical decisions have no effect on this workflow. Later reusable source-matched layout assets cover these units, and the downstream support mapper must map them along with every other source page.

