# Direct Source Inventory

Inventory scope: the current paper package recursively, including hidden paths. Audit derivatives, workflow controls, and generated reports are not direct supplied sources. Four direct PDF sources were found; no direct DOC, DOCX, XLS, XLSX, or CSV source exists. All sources remain unchanged. Stable units are physical PDF pages, including cover pages and end matter.

| Source ID | Source path | Document role | Content and role basis | Unit type | Total units | Exact scope | Inspection engine |
|---|---|---|---|---|---:|---|---|
| DOC-001 | jama_blakely_2024_oi_240020_1710443209.74411.pdf | REPORT | Page 1 identifies a JAMA Original Investigation reporting the HIP randomized trial; the body contains methods, results, Tables 1–3 and Figures 1–3. | PDF_PAGE | 10 | PDF pp. 1–10 | Direct pdfinfo and pdftotext 26.01.0 |
| DOC-002 | joi240020supp1_prod_1710443209.74911.pdf | PLAN | Page 1 identifies the HIP Trial Protocol; prospective hypotheses, study design, planned analyses, SAE definitions and protocol changes follow. | PDF_PAGE | 25 | PDF pp. 1–25 | Direct pdfinfo and pdftotext 26.01.0 |
| DOC-003 | joi240020supp2_prod_1710443209.75411.pdf | PLAN | Page 1 identifies Statistical Analysis Plan, version 1, dated October 31, 2022; subsequent pages specify hypotheses, sample size and analyses. | PDF_PAGE | 10 | PDF pp. 1–10 | Direct pdfinfo and pdftotext 26.01.0 |
| DOC-004 | joi240020supp3_prod_1710443209.75411.pdf | REPORT | Page 1 lists additional enrollment information, frequentist primary and major secondary outcome analyses, participating centers and acknowledgments. This is a non-plan results supplement. | PDF_PAGE | 8 | PDF pp. 1–8 | Direct pdfinfo and pdftotext 26.01.0; reusable rendered-page visual inspection |

Total: 4 sources and 53 unique physical pages. No source bundles both REPORT and PLAN material. Role assignments are content-based. Hashes are recorded using package-relative source paths in source_hashes_before.sha256. All PDFs are readable, unencrypted and have native text layers. Supplement 3 has corrupted native glyphs; readable reusable images cover pp. 2–5. Pages 1 and 6–8 require fresh direct inspection. No legacy scientific exclusion or old scope instruction constrains this review.
