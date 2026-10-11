# Direct-source inventory

Inventory covers the current package only. Direct tools: `pdfinfo` (26.01.0), `pdftotext` (26.01.0), `sha256sum`; compute device CPU. Routing and tooling preflight are PASS; the fresh curator model responded successfully under the required gpt-6.1-sol/medium named role. All supplied sources remain unchanged. No Office or CSV sources are present. Stable unit type is PDF_PAGE and pages are physical PDF pages.

| Source ID | Source path | Document role | Units | Content basis and bundle note |
|---|---|---|---:|---|
| DOC-001 | jama_engelter_2025_oi_250066_1761597796.45511.pdf | REPORT | 10 | Main ESTREL randomized clinical trial article, including abstract, results, tables, figures, and references. |
| DOC-002 | joi250066supp1_prod_1761597796.4601.pdf | PLAN | 94 | Clinical study protocol and plan bundle; cover identifies protocol version 1.1, 30 November 2018. Inspect every bundled page/version during mapping. No results-report bundle established at inventory. |
| DOC-003 | joi250066supp2_prod_1761597796.4701.pdf | PLAN | 18 | Prospective objectives, analysis populations, estimand strategies, and predefined analyses. Cover and watermark say Final Report, but inspected content specifies analyses to be performed, so role is PLAN by content. Mapper must flag any REPORT-containing sections if encountered. |
| DOC-004 | joi250066supp3_prod_1761597796.4701.pdf | REPORT | 27 | Non-plan supplemental content: methods/context followed by eTables and eFigures with trial results. |
| DOC-005 | joi250066supp4_prod_1761597796.4751.pdf | REPORT | 8 | Nonauthor collaborator roster supplied with the reported trial; administrative REPORT material, without a prospective statistical plan. |
| DOC-006 | joi250066supp5_prod_1761597796.4751.pdf | REPORT | 1 | ESTREL Main Analysis Code; implemented analysis code, not a prospective protocol. |
| DOC-007 | joi250066supp6_prod_1761597796.4801.pdf | REPORT | 1 | Published data-sharing statement; administrative REPORT material, without a prospective statistical plan. |

Total: 7 PDFs, 159 unique PDF pages. Commands: `pdfinfo "SOURCE.pdf"`; `pdftotext -f 1 -l 1 "SOURCE.pdf" -`; `pdftotext -layout "SOURCE.pdf" -`. Direct extraction was read as inventory evidence and not stored as a new derivative. PDF page-count completeness was checked for every source. Direct-source SHA-256 values are recorded separately in source_hashes_before.sha256 with package-relative paths.
