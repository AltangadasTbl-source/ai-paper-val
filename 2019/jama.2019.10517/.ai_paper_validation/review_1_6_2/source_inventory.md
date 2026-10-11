# Direct source inventory

Complete recursive package inventory found four direct sources, all PDFs; no DOC, DOCX, XLS, XLSX or CSV source is supplied. Workflow control files and audit derivatives are not direct scientific sources. Unit counts use PDF_PAGE and were independently confirmed with direct Poppler pdfinfo 26.01.0. Source SHA-256 values match the supplied document identity records. Source roles below were assigned from direct first-page content, not legacy scope restrictions.

| Source ID | Source path | Document role | Unit type | Total units | Content and role basis |
|---|---|---|---|---:|---|
| DOC-001 | jama_flint_2019_oi_190079.pdf | REPORT | PDF_PAGE | 10 | Original Investigation: STOP-PD II randomized clinical trial; abstract, methods, results, tables, figures and end matter. |
| DOC-002 | joi190079supp1_prod.pdf | PLAN | PDF_PAGE | 42 | Sustaining Remission of Psychotic Depression: Protocol & Data Analytic Plan; research design, analysis, participant protection, and pharmacotherapy appendix. Entire bundle is prospective plan material; no REPORT/PLAN mixed bundle identified. |
| DOC-003 | joi190079supp2_prod.pdf | REPORT | PDF_PAGE | 10 | Supplementary Online Content listing and displaying eFigures 1-9: mixed-model estimated least-square means. |
| DOC-004 | joi190079supp3_prod.pdf | REPORT | PDF_PAGE | 1 | Non-plan data sharing statement accompanying the report; administrative content, no quantitative trial results. REPORT is the applicable non-plan role; its sole page must still be mapped for applicability. |

The complete direct-source union is DOC-001 pp. 1-10, DOC-002 pp. 1-42, DOC-003 pp. 1-10, and DOC-004 p. 1 (63 unique units). No supplied unit is excluded because a legacy document record restricted audit scope. Direct commands: `pdfinfo "<source>"`, `pdftotext -f 1 -l 2 "<source>" -`, and `sha256sum -- "<source>"`. All tools run locally; no source was modified.
