# Workflow 1.6.2 Direct-Source Inventory

Inventory scope: current paper package only. Recursive case-insensitive discovery of supplied PDF, DOC, DOCX, XLS, XLSX, and CSV files found exactly four PDF sources and no Office or CSV sources. All stable units are physical PDF pages; trailing form-feed empty segments are not pages. Source hashes use direct `sha256sum` with package-relative paths.

| Source ID | Source path | Format | Document role | Stable unit definition | Total units | Content basis and bundle boundaries |
|---|---|---|---|---|---:|---|
| DOC-001 | jama_de_boer_2019_oi_190122.pdf | PDF | REPORT | Physical PDF page | 11 | Main randomized-trial article, including abstract, methods, results, tables, figures, discussion and references. |
| DOC-002 | joi190122supp1_prod.pdf | PDF | PLAN | Physical PDF page | 33 | Protocol dated June 28, 2010, pp. 1-30; protocol addendum/changes to analytic plan, pp. 31-33. All components are prospective plan content; this bundle contains no REPORT component. Analysis plan pp. 17-20 and amended analysis pp. 32-33 are distinct supplied locations. |
| DOC-003 | joi190122supp2_prod.pdf | PDF | REPORT | Physical PDF page | 19 | Supplementary online content, supplementary methods, eTables and eFigures reporting this trial. Methods in a results supplement are REPORT content rather than a prospective PLAN. |
| DOC-004 | joi190122supp3_prod.pdf | PDF | REPORT | Physical PDF page | 1 | Data-sharing statement associated with the published report; operational sharing information, no prospective statistical-analysis plan. |

Total: 4 sources, 64 PDF_PAGE units. Direct `pdfinfo` confirmed counts 11, 33, 19 and 1. Every cached pdfinfo record exactly matches current `pdfinfo` output. All PDFs are unencrypted. DOC-002 has usable native/layout text on all 33 pages and is not a scanned-only protocol. No conversion or OCR is required for inventory. Direct sources and every legacy artifact remain unchanged.

Complete downstream scopes: main mapper DOC-001 pp. 1-11; support mapper DOC-002 pp. 1-33, DOC-003 pp. 1-19 and DOC-004 p. 1. No source unit may be omitted because it contains only title, references, sharing information or background; its mapping may explicitly state no trial-result relationship. Source order above governs stable source IDs.
