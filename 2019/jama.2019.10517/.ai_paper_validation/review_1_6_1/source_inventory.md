# Direct Source Inventory

All supplied PDF, DOC, DOCX, XLS, XLSX, and CSV sources in the current package were inventoried. Exactly four direct sources are present, all PDFs; no Office or CSV sources are present. Workflow controls, audit derivatives, and the download-note text are not direct scientific sources. Identity and page counts were established with direct `sha256sum` and `pdfinfo`. Roles follow supplied content, not supplement numbering. Every PDF page remains in scope for mapping, including administrative and reference pages.

| Source ID | Source path | Format | Stable unit type | Total units | Document role | Content and role basis | Mixed-role bundle |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_flint_2019_oi_190079.pdf | PDF | PDF_PAGE | 10 | REPORT | Main randomized-trial article, Research / Original Investigation; title and quantitative results on PDF p.1 | No |
| DOC-002 | joi190079supp1_prod.pdf | PDF | PDF_PAGE | 42 | PLAN | PDF p.1 states PROTOCOL & DATA ANALYTIC PLAN and lists research methods, data analysis, safety monitoring and pharmacotherapy protocol | No; protocol, analytic plan and operational appendix are all PLAN |
| DOC-003 | joi190079supp2_prod.pdf | PDF | PDF_PAGE | 10 | REPORT | PDF p.1 identifies supplementary content and nine estimated least-square mean result figures on PDF pp.2-10 | No |
| DOC-004 | joi190079supp3_prod.pdf | PDF | PDF_PAGE | 1 | PLAN | PDF p.1 specifies prospective data-access approval, specified-purpose analysis and signed access-agreement conditions; operational data-sharing document without trial results | No; role assigned to operational access content, not to its publication as a supplement |

## Integrity and inventory method

Commands: `rg --files --hidden` with workflow, configuration and git controls excluded, extension filtering for every direct format; `pdfinfo` for each PDF; `sha256sum --` for each direct source. PDF content was inspected using supplied reusable source-linked records and direct `pdftotext` on content-identifying pages. The full protocol layout derivative was compared byte-for-byte against direct `pdftotext -layout joi190079supp1_prod.pdf -` and matched. Source-record hashes for all four PDFs match current direct-source hashes. Legacy records' older scope restrictions were ignored; they do not restrict this review.

Complete source identity is recorded in `source_hashes_before.sha256`. No source was modified. No sibling package, external literature, or web resource was inspected. Existing scientific checker, candidate, screening, classification and final-report contents were not read.
