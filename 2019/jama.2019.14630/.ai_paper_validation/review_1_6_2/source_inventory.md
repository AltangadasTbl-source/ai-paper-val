# Direct-source inventory

All supplied sources in the current package were inventoried. The five package-root PDFs are direct evidence. The one PDF below the prior audit area is a rendered/extracted derivative, not an additional supplied source. No direct DOC, DOCX, XLS, XLSX, or CSV file is present. Stable units are PDF pages, including covers, reference and affiliation pages, and blank separators. Direct tools: pdfinfo and pdftotext, Poppler 26.01.0; SHA-256 engine: sha256sum. Document roles follow content rather than filenames.

| Source ID | Source path | Format | Document role | Total units | Content and role basis | Reusable coverage |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_saynorea_2019_oi_190106_1635377898.43062.pdf | PDF | REPORT | 14 | Main JAMA original investigation reporting the interim PREDIMED-Plus randomized trial; no bound PLAN component. | Source-complete native layout, PDF pp. 1-14 |
| DOC-002 | joi190106supp1_prod_1635377898.47058.pdf | PDF | PLAN | 75 | Cover identifies Trial protocol; prospective trial procedures and design; no results REPORT component. | Source-complete native layout, PDF pp. 1-75 |
| DOC-003 | joi190106supp2_prod_1635377898.49605.pdf | PDF | PLAN | 30 | Cover identifies Statistical analysis plan; prospective analysis specification; no results REPORT component. | Source-complete native layout, PDF pp. 1-30 |
| DOC-004 | joi190106supp3_prod_1635377898.49725.pdf | PDF | REPORT | 29 | Contents enumerate eTables 1-9 and eFigures 1-3 reporting trial results; no bound PLAN component. | Source-complete native layout and reusable sparse-page/figure renders, PDF pp. 1-29 |
| DOC-005 | joi190106supp4_prod_1635377898.50723.pdf | PDF | REPORT | 1 | Data-sharing statement supplied with the reported study; ancillary REPORT material, without prospective statistical plan content. | Source-complete native layout, PDF p. 1 |

## Identity and exact-source matching

The five canonical whole-source layout files were each compared byte-for-byte with the output of `pdftotext -layout SOURCE - | cmp -s - ASSET`. All five returned status 0. Form-feed record counts are respectively 14, 75, 30, 29, and 1 and agree with pdfinfo. Source hashes are recorded in source_hashes_before.sha256 with package-relative paths. Native source-complete coverage supersedes the incomplete ranges in earlier page manifests; those old range choices are not reused as review boundaries.

## Downstream assignments

Main mapper: DOC-001 PDF pp. 1-14. Support mapper union: DOC-002 PDF pp. 1-75; DOC-003 PDF pp. 1-30; DOC-004 PDF pp. 1-29; DOC-005 PDF p. 1. The coordinator must shard the support union because its combined normalized text exceeds the configured context bound. Every page remains assigned, including pages without statistical content. No source unit requires fresh extraction; visual confirmation can use retained source-linked images or targeted direct-source rendering.
