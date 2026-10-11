# Direct-source inventory

All direct PDF, DOC, DOCX, XLS, XLSX and CSV files in this package were inventoried using `rg --files --hidden` and extension inspection. There are five direct PDFs; no direct Office or CSV sources. Existing derived files and workflow controls are not direct sources. Stable units are complete physical PDF pages, including covers, references and signing trails.

| Source ID | Source path | Document role | Content-based identity | Unit type | Total units | Reusable units | Fresh-required units | Exact downstream assignment |
|---|---|---|---|---|---:|---:|---:|---|
| DOC-001 | jama_paterson_2024_oi_240139_1741633738.12862.pdf | REPORT | Main randomized trial article, Intravenous Lidocaine for Gut Function Recovery in Colonic Surgery | PDF_PAGE | 10 | 10 | 0 | Main mapper: PDF pp. 1-10 |
| DOC-002 | joi240139supp1_prod_1741633738.16362.pdf | PLAN | ALLEGRO Study Protocol version 8, 21 December 2022; includes appended operational scales and signing trail; no report-result bundle | PDF_PAGE | 66 | 66 | 0 | Support mapper: PDF pp. 1-66 |
| DOC-003 | joi240139supp2_prod_1741633738.17362.pdf | PLAN | ALLEGRO Statistical Analysis Plan, minimally invasive RCT, version 2, 9 September 2024; dummy displays and signing trail; no report-result bundle | PDF_PAGE | 40 | 40 | 0 | Support mapper: PDF pp. 1-40 |
| DOC-004 | joi240139supp3_prod_1741633738.18862.pdf | REPORT | Supplemental online content containing prespecified subgroup analysis of primary outcome | PDF_PAGE | 2 | 2 | 0 | Support mapper: PDF pp. 1-2 |
| DOC-005 | joi240139supp4_prod_1741633738.20861.pdf | REPORT | Retrospective publication data-sharing statement; administrative report content, no prospective statistical plan | PDF_PAGE | 1 | 1 | 0 | Support mapper: PDF p. 1 |

The source roles above were checked against direct-source first-page content using `pdftotext -f 1 -l 1 SOURCE -`; they are independent of the earlier review scope. No supplied bundle mixes REPORT and PLAN content. DOC-002 and DOC-003 are encrypted with extraction permitted; `pdfinfo` and `pdftotext` succeed. Document page counts are `pdfinfo` 26.01.0 counts. Hash engine: direct `sha256sum`; source_hashes_before.sha256 uses package-relative paths.

Native/layout page text for every source was reproduced byte-exact using current Poppler 26.01.0 in memory and compared with its existing derivative; no derivative was changed. Visual inspection is still mandatory for all figures and spatial tables. In particular, DOC-002 pp. 51, 52, 62 and DOC-004 p. 2 have sparse text and must use their existing images. Source-linked legacy metadata records contain mixed metadata and audit summaries: only identity/extraction portions are reused; exposed earlier audit summaries and all historical scientific decisions are excluded from this review.
