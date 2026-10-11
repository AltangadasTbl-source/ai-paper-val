# Workflow 1.6 Source Inventory

The inventory is restricted to the current paper package. Three direct PDFs and no direct DOC, DOCX, XLS, XLSX, or CSV sources were found. Workflow controls and generated audit files are not supplied scientific sources. Current `pdfinfo` (Poppler 25.03.0) establishes complete physical page counts; all PDFs are readable, unencrypted, letter size, and page rotation 0. Source hashes are maintained by the coordinator in `source_hashes_before.sha256`.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_driver_2018_oi_180054.pdf | PDF | PDF_PAGE | 11 | REPORT | Main randomized clinical trial article; abstract, methods, results, five tables, two figures, discussion, and references. All physical pp.1-11 are REPORT. |
| DOC-002 | joi180054supp1_prod.pdf | PDF | PDF_PAGE | 25 | PLAN | Clinical Trial Protocol with prospective operations and statistical-analysis sections, background evidence, sample-size planning, and references. All physical pp.1-25 are PLAN. |
| DOC-003 | joi180054supp2_prod.pdf | PDF | PDF_PAGE | 13 | REPORT; mixed REPORT/PLAN bundle | Results supplement: pp.1-6 are REPORT (cover, eTable 1 and notes pp.2-3, eFigures pp.4-5, interim analysis reporting p.6); pp.7-13 are PLAN operational material (eAppendix 2 Postintubation Data Form). Comparisons must use the role of the cited content rather than the file name. |

The DOC-003 p.6 quotation of a protocol stopping rule is presented within an interim-analysis result appendix. Classify the compared statement by content if a future comparison specifically concerns that prospective rule; do not automatically classify the entire result appendix as PLAN. The blank data collection form on pp.7-13 is a prospective operational instrument, and therefore PLAN under the supplied scope definition. This mixed bundle does not change unique page counts.

Stable source locations use physical PDF page numbers, including cover pages. Direct locations are `jama_driver_2018_oi_180054.pdf#page=N`, `joi180054supp1_prod.pdf#page=N`, and `joi180054supp2_prod.pdf#page=N`; report-relative links must adjust directory prefixes truthfully.

