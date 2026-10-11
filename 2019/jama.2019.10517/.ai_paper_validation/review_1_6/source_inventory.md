# Workflow 1.6 Direct Source Inventory

Inventory completed within the current package only. `find` searched every package file for PDF, DOC, DOCX, XLS, XLSX, and CSV extensions; four direct PDFs and no Office or CSV sources were found. Existing evidence derivatives are not additional direct sources. SHA-256 was recorded before source-content inspection in `source_hashes_before.sha256`. Stable units are physical PDF pages, including covers, references, and administrative pages.

| Source ID | Source path | Unit type | Total units | Document role | Content basis and bundle note |
|---|---|---|---:|---|---|
| DOC-001 | jama_flint_2019_oi_190079.pdf | PDF_PAGE | 10 | REPORT | Page 1 is an Original Investigation reporting the STOP-PD II randomized clinical trial; pages 1-10 comprise article results, methods, tables, figures, and end matter. No separate plan bundle. |
| DOC-002 | joi190079supp1_prod.pdf | PDF_PAGE | 42 | PLAN | Page 1 states PROTOCOL & DATA ANALYTIC PLAN. Contents include prospective research design, data analysis, human-subject protections, and pharmacotherapy protocol. Historical/background results remain PLAN content. No REPORT bundle identified. |
| DOC-003 | joi190079supp2_prod.pdf | PDF_PAGE | 10 | REPORT | Page 1 lists eFigures 1-9 of mixed-model estimated least-square means in randomized groups; pages 2-10 contain those results plots. No plan bundle. |
| DOC-004 | joi190079supp3_prod.pdf | PDF_PAGE | 1 | PLAN | Page 1 is a Data Sharing Statement defining prospective access, approval, and agreement conditions; this is operational material with no reported results. Classified PLAN by content under the prospective operational-document rule. Role ambiguity: administrative data-sharing statements are not specifically named in the normative examples; recheck any compared location if it enters a candidate. |

Total: 4 sources, 63 PDF_PAGE units, 20 REPORT pages and 43 PLAN pages. Source counts were established with direct `pdfinfo` (Poppler 26.01.0); source roles were established from first-page `pdftotext` output and contents rather than file numbering. Current hashes agree with the legacy package identity records. Legacy exclusions and old role wording are not adopted as current coverage boundaries.

## Complete mapper assignments

- Main mapper: DOC-001 pages 1-10, using source-linked native text, selected rendered pages, and locator-only extraction map.
- Support mapper part 1: DOC-002 pages 1-21, DOC-003 pages 1-10, and DOC-004 page 1. Use per-page native/layout protocol text, native text plus rendered results figures on pages 2-10, and the operational page's native/layout derivatives. Read graphical values as approximate unless exact printed values exist. Artifact: extraction/parts/support_first_and_results.md.
- Support mapper part 2: DOC-002 pages 22-42, using source-matched 21-page native/layout concatenations. Artifact: extraction/parts/support_plan_second.md.

There are no uncovered units. All assignments require fresh scientific mapping; reusable extraction does not constitute mapping completion. Mapped counts were initialized to zero; coordinator now confirms all 63 current mapping units complete in source_coverage.md.

Current role confirmation: the fresh high-effort evidence rechecker read DOC-004 directly and recommends PLAN for its prospective data-access/approval/agreement conditions. The first mapper's REPORT disclosure interpretation was preserved as a bounded ambiguity and corrected in the current support map. No candidate compares a DOC-004 numeric result; source role totals remain20REPORT pages and43PLAN pages.
