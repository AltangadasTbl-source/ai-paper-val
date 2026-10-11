# Direct Source Inventory

Inventory scope: this paper package only; case-insensitive PDF, DOC, DOCX, XLS, XLSX, and CSV enumeration. Four direct PDFs were found. No Office, workbook, or CSV sources were supplied. Stable unit: PDF_PAGE, including covers, roster pages, references, and nonnumeric pages. Page counts were obtained directly with Poppler pdfinfo, corroborated by complete form-feed-delimited native and layout text.

| Source ID | Source path | Format | Total units | Document role | Content basis and stable locations |
|---|---|---|---:|---|---|
| DOC-001 | jama_de_boer_2019_oi_190122.pdf | PDF | 11 | REPORT | Main randomized-trial article, abstract p. 1; methods pp. 2-4; trial results, tables, and figures pp. 4-9; discussion and references pp. 9-11. |
| DOC-002 | joi190122supp1_prod.pdf | PDF | 33 | PLAN | Trial protocol dated June 28, 2010, pp. 1-30; protocol addendum changing the analytic plan, pp. 31-33, described on p. 31 as submitted in the NIH grant renewal application on March 2, 2015 and implemented upon funding on February 24, 2016. Background and historical numerical figures pp. 5-9 remain PLAN content. The bound bundle contains multiple plan components and no REPORT component. |
| DOC-003 | joi190122supp2_prod.pdf | PDF | 19 | REPORT | Non-plan results supplement: contents p. 1; supplementary laboratory methods and references pp. 2-5; eTables 1-11 pp. 6-16; eFigures 1-3 pp. 17-19. |
| DOC-004 | joi190122supp3_prod.pdf | PDF | 1 | REPORT | Published-article data-sharing statement, p. 1. This is a report-associated disclosure, not a prospective protocol, SAP, or operational analysis plan. No trial numerical outcome table is present, but the page remains in complete coverage. |

Total source units: 64. Source identity hashes: source_hashes_before.sha256, with package-relative paths. Sources are unchanged. Content-based roles were assigned from current direct-source extraction and source-matched reusable texts, without reading prior candidate or classification records.

Commands: rg --files --hidden . with PDF/DOC/DOCX/XLS/XLSX/CSV case variants; pdfinfo "SOURCE.pdf"; pdftotext "SOURCE.pdf" -; pdftotext -layout "SOURCE.pdf" -; sha256sum -- "SOURCE.pdf". Engine: Poppler 26.01.0 for PDF text and image tools; direct sha256sum for integrity. No fallback or Python extraction was needed.
