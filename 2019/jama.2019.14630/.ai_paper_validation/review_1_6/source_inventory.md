# Direct-Source Inventory

Scope is the current paper package only. A recursive inventory excluding audit derivatives and workflow controls found five direct PDFs and no DOC, DOCX, XLS, XLSX, or CSV sources. Stable units are all physical PDF pages, including covers, references, affiliations, and supplied administrative material. Counts use direct Poppler pdfinfo 26.01.0; hashes use sha256sum. Document roles are assigned from current source content, not supplement numbering.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis and full mapping assignment |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_saynorea_2019_oi_190106_1635377898.43062.pdf | PDF | PDF_PAGE | 14 | REPORT | Original Investigation reporting the interim randomized-trial results; main mapper covers PDF pp. 1-14, including article back matter. |
| DOC-002 | joi190106supp1_prod_1635377898.47058.pdf | PDF | PDF_PAGE | 75 | PLAN | Trial protocol/research plan, with prospective trial operations and historical/background material; support mapper covers PDF pp. 1-75. |
| DOC-003 | joi190106supp2_prod_1635377898.49605.pdf | PDF | PDF_PAGE | 30 | PLAN | Statistical analysis plan with versions and prospective analysis rules; support mapper covers PDF pp. 1-30. |
| DOC-004 | joi190106supp3_prod_1635377898.49725.pdf | PDF | PDF_PAGE | 29 | REPORT | Results supplement with eTables 1-9 and eFigures 1-3; support mapper covers PDF pp. 1-29, including affiliations pp. 28-29. |
| DOC-005 | joi190106supp4_prod_1635377898.50723.pdf | PDF | PDF_PAGE | 1 | REPORT | Retrospective publication data-sharing statement for the reported study; describes availability and access rather than a prospective protocol or SAP; support mapper covers PDF p. 1. |

No supplied source is a mixed REPORT/PLAN bundle. DOC-005 is administrative report content; numerical scientific relationships may be absent, but its physical page remains mandatory mapping scope.

## Source-Matched Reusable Text

Each following existing text artifact was compared byte-for-byte with the stream from direct `pdftotext -layout SOURCE -`. Every comparison returned MATCH. Form-feed counts equal all physical source pages. No extraction file was rewritten, and no new preprocessing derivative was needed for curation.

| Source | Full-layout asset | Page count | Bytes | Fitness |
|---|---|---:|---:|---|
| DOC-001 | .ai_paper_validation/document_outputs/DOC-001/main_layout.txt | 14 | 140131 | USABLE |
| DOC-002 | .ai_paper_validation/review_1_5_1/preprocessing/DOC-002_supp1_layout_fresh.txt | 75 | 184474 | USABLE |
| DOC-003 | .ai_paper_validation/review_1_5_1/preprocessing/DOC-003_supp2_layout_fresh.txt | 30 | 83286 | USABLE |
| DOC-004 | .ai_paper_validation/document_outputs/DOC-004/supp3_layout.txt | 29 | 73167 | USABLE with existing sparse-page OCR and figure/page renders |
| DOC-005 | .ai_paper_validation/review_1_5_1/preprocessing/DOC-005_supp4_layout_fresh.txt | 1 | 1001 | USABLE |

All source-level text sizes are below the 200000-character mapping bound; byte counts are conservative bounds on character counts. Support scope should retain disjoint source sections to avoid exceeding the bound for their concatenated union. The protocol size reflects supplied text complexity, not a universal time-target rule.

Legacy page manifests cover main pp. 1-11 and results-supplement pp. 1-27 only. Their old selected ranges and exclusion statements are not scientific scope for this run. Full-layout assets close the prior derivative gaps for main pp. 12-14 and results-supplement pp. 28-29.

Exact UTF-8 character counts measured with `wc -m`: DOC-001 139148; DOC-002 183878; DOC-003 83068; DOC-004 73014; DOC-005 1001. The other-support shard contains 157083 characters. Source-size bounds and full page counts are independent checks; no page is sampled.
