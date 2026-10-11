# Direct Source Inventory

Inventory scope is this paper package only. Four supplied PDFs and no supplied DOC, DOCX, XLS, XLSX, or CSV sources were found outside the audit area. Direct sources are unchanged. Roles follow document content. Stable unit type is PDF_PAGE; all physical pages, including covers, administrative material, references, and nearly empty pages, are counted.

| Source ID | Source path | Format | Document role | Content and exact scope | Total units | Native characters | Layout characters |
|---|---|---|---|---|---:|---:|---:|
| DOC-001 | jama_azoulay_2018_oi_180109.pdf | PDF | REPORT | Main article; PDF pp.1-9 | 9 | 54893 | 93716 |
| DOC-002 | joi180109supp1_prod.pdf | PDF | PLAN | Protocol and SAP bundle; PDF pp.1-129. Contents identify initial protocol pp.2-69, final protocol pp.70-81, original SAP pp.82-83, and final SAP material from p.84; all remaining physical pages through 129 included. No mixed REPORT/PLAN bundle. | 129 | 191334 | 239045 |
| DOC-003 | joi180109supp2_prod.pdf | PDF | REPORT | Results supplement: cover p.1, oxygenation/ventilation eTable p.2, cumulative ventilation eFigure p.3, respiratory rate/oxygenation eFigure p.4, comfort/dyspnea eFigure p.5 | 5 | 2893 | 5799 |
| DOC-004 | joi180109supp3_prod.pdf | PDF | REPORT | Retrospective data-sharing availability statement, PDF p.1; no quantitative result display or prospective analysis plan | 1 | 519 | 526 |

Total: 144 physical PDF pages. Character volumes are exact `wc -m` counts of the existing full-document derivatives, including whitespace and form feeds; normalized-text volumes are smaller. Counts bound context allocation rather than scientific relevance. The French-language sections of the supplied plan remain supplied evidence; generated records are English.

Direct commands: `pdfinfo "source.pdf"` for each source; `pdftotext -f 1 -l 1 "source.pdf" -` for role identification; `sha256sum -- "source.pdf"` for each source. Engines: Poppler pdfinfo/pdftotext 25.03.0; GNU coreutils sha256sum 9.7. Hashes are in source_hashes_before.sha256 with package-relative paths. File format/header checks use file 5.46. No Office extraction, OCR, conversion, or fallback environment was required.

Recommended mapping scopes: main mapper DOC-001 pp.1-9; support shards DOC-002 pp.1-32, pp.33-64, pp.65-94, pp.95-129; the last support shard also includes DOC-003 pp.1-5 and DOC-004 p.1. Each shard stays below 200000 normalized text characters and 32 unique existing rendered source pages when visual material is selected by exact page. Every page receives fresh scientific mapping even when its derivative is reusable. No previously assigned relevance label is a coverage boundary.
