# Source inventory

Inventory is limited to this package. Six supplied PDFs were found; no supplied DOC, DOCX, XLS, XLSX, or CSV source exists. Unit counts were obtained directly using Poppler pdfinfo 26.01.0. Document roles were assigned from source-page content using direct pdftotext, not supplement numbering. All source paths are package-relative; SHA-256 identities are recorded in source_hashes_before.sha256.

| Source ID | Source path | Document role | Content and role basis | Unit type | Total units |
|---|---|---|---|---|---:|
| DOC-001 | jama_bluth_2019_oi_190055_16092.pdf | REPORT | Main published PROBESE randomized clinical trial, with methods, results, tables, figures, investigator list and references | PDF_PAGE | 14 |
| DOC-002 | joi190055supp1_prod_16092.pdf | PLAN | Research protocol version 2.6, October 2016, with prospective design and appendices | PDF_PAGE | 36 |
| DOC-003 | joi190055supp2_prod_16092.pdf | PLAN | Approved protocol-change overview | PDF_PAGE | 3 |
| DOC-004 | joi190055supp3_prod_16092.pdf | PLAN | Updated statistical analysis plan, finalized January 20, 2018 before database locking and analysis | PDF_PAGE | 3 |
| DOC-005 | joi190055supp4_prod_16092.pdf | REPORT | Results supplement with committees, investigators, sites, eMethods, eTables, eFigures and references; eMethods explain reported analysis and are not a prospective protocol/SAP bundle | PDF_PAGE | 43 |
| DOC-006 | joi190055supp5_prod_16092.pdf | REPORT | Publication data-sharing statement, a non-plan publication support document | PDF_PAGE | 1 |

No supplied source bundles both REPORT and PLAN material. Prospective protocol and SAP are supplied separately from the results supplement. All 100 pages require scientific mapping, including ancillary pages whose relevance must be explicitly recorded.

## Mapper assignments and context bounds

Main mapper: DOC-001 pp. 1-14. Canonical layout asset .ai_paper_validation/review_1_5_2/preprocessing/layout_text/jama_bluth_2019_oi_190055_16092.txt (131,090 Unicode characters including form-feed separators; below 200,000-character bound). Existing rendered pages cover pp. 1-12; pp. 13-14 have native/layout text and contain investigator/reference material.

Support mapper: DOC-002 pp. 1-36; DOC-003 pp. 1-3; DOC-004 pp. 1-3; DOC-005 pp. 1-43; DOC-006 p. 1. Canonical layout paths are .ai_paper_validation/review_1_5_2/preprocessing/layout_text/<source-basename>.txt. Combined support layout length is 190,063 Unicode characters, below 200,000. Recommended durable support parts: plan-material (DOC-002, DOC-003, DOC-004; 95,505 characters); results-supplement (DOC-005; 93,432 characters); data-sharing (DOC-006; 1,126 characters). These scopes are disjoint and complete. The 32-rendered-page context bound applies to each visual handoff: do not bundle all support images into one visual handoff. Results figures pp. 31-42 are rendered and require visual mapping; other support rendered pages can be inspected in separate source-bounded batches. No missing derivative requires fresh extraction, but direct-source inspection remains necessary wherever a mapper finds transcription or visibility limits.
