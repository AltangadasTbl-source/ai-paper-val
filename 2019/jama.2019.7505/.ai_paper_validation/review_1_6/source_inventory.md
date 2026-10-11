# Workflow 1.6 Direct Source Inventory

The package contains six direct PDF sources and no DOC, DOCX, XLS, XLSX, or CSV sources. Recursive package-only extension inventory excluded workflow code and audit derivatives from direct-source status. Stable units are physical, one-based PDF pages (`PDF_PAGE`), including title, contributor, reference, and administrative pages. No page is omitted because it lacks quantitative results.

| Source ID | Source path | Document role | Role basis from content | Unit type | Total units | Exact stable scope | Layout characters |
|---|---|---|---|---|---:|---|---:|
| DOC-001 | jama_bluth_2019_oi_190055_16092.pdf | REPORT | Main randomized-trial article, abstract, results, tables, figures, discussion, contributors and references | PDF_PAGE | 14 | PDF pp. 1-14; printed article pp. 2292-2305 | 131510 |
| DOC-002 | joi190055supp1_prod_16092.pdf | PLAN | Research protocol version 2.6, October 2016, with prospective procedures, statistical planning, appendices and background evidence | PDF_PAGE | 36 | PDF pp. 1-36; cover and protocol printed pp. 1-35 | 79641 |
| DOC-003 | joi190055supp2_prod_16092.pdf | PLAN | Overview of protocol-version amendments and approved operational changes | PDF_PAGE | 3 | PDF pp. 1-3 | 6887 |
| DOC-004 | joi190055supp3_prod_16092.pdf | PLAN | Updated statistical analysis plan finalized January 20, 2018, before final inclusion and database lock | PDF_PAGE | 3 | PDF pp. 1-3 | 9516 |
| DOC-005 | joi190055supp4_prod_16092.pdf | REPORT | Non-plan supplementary results, eMethods, eTables 1-9, eFigures 1-12, contributor list and references | PDF_PAGE | 43 | PDF pp. 1-43 | 94059 |
| DOC-006 | joi190055supp5_prod_16092.pdf | PLAN | Prospective operational data-sharing and access conditions; no numerical trial results | PDF_PAGE | 1 | PDF p. 1 | 1126 |

No physical bundle combines REPORT and PLAN content. Historical/background numbers inside the protocol retain PLAN role. Methods that explain completed analyses inside the results supplement retain REPORT role. The data-sharing statement's prospective access rules support its PLAN assignment; it is ancillary and supplies no quantitative relationship.

## Source identity and inspection

Current direct `pdfinfo` confirms page counts 14, 36, 3, 3, 43, 1; total 100. All sources are unencrypted readable PDFs. The main source is 480254 bytes; supplement sizes are 403679, 309438, 118873, 1032894, and 21678 bytes respectively. Direct hashes are recorded in `source_hashes_before.sha256` with package-relative filenames. The source files and prior audit assets were not modified.

Tool engines: direct Poppler 26.01.0 (`pdfinfo`, `pdftotext`, `pdftoppm`); direct uutils `sha256sum` 0.10.0. Tooling record declares all direct capabilities available and fallback environment NOT_NEEDED. No OCR, Office conversion, Python extraction, web access, sibling inspection, or GPU operation was needed for inventory.

Commands: `pdfinfo "source.pdf"`; `pdftotext -f N -l N "source.pdf" -`; `pdftotext -layout -f N -l N "source.pdf" -`; `sha256sum -- "source.pdf"`. Every page was matched to the reusable extraction at the same physical page index. Equality checks discarded whitespace only; numeric strings, punctuation, and other content were preserved. Form-feed segmentation yielded exactly the direct page counts in both text formats. Direct commands streamed validation output without creating derivatives.

## Downstream mapping assignments

DOC-001 pp. 1-14 go to the main quantitative mapper. DOC-002 pp. 1-36, DOC-003 pp. 1-3, DOC-004 pp. 1-3, DOC-005 pp. 1-43 and DOC-006 p. 1 go to the support mapper, split if visual or relationship context bounds require. All 100 units must be mapped afresh for quantitative discovery, even though their preprocessing evidence is reusable. Fresh-required direct-source units due to unusable or absent evidence: zero.

Support layout text totals 191229 characters, below the 200000 normalized-text bound even before normalization. Support has 55 reusable rendered pages, above the 32-page visual-context bound if all are loaded in one shard. Plan and results scopes offer a natural disjoint split: PLAN sources total 43 units with 30 renders; REPORT supplement total 43 units with 25 renders. Main has 14 units and 12 renders. These are context bounds, never coverage or finding limits.
