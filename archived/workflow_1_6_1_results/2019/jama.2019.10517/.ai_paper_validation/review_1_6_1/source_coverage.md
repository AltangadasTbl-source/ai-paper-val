# Complete Source-Coverage Ledger

Counts use unique PDF pages; overlapping derivatives do not increase reusable counts. Every unit has usable source-linked reusable text or rendering. All assigned mapper artifacts are complete: main pages 1–10; support shard 1 protocol pages 1–21, all result pages and data-sharing page; support shard 2 protocol pages 22–42. Mapped counts reflect fresh scientific reasoning documented in those artifacts.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_flint_2019_oi_190079.pdf | PDF_PAGE | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | joi190079supp1_prod.pdf | PDF_PAGE | 42 | 42 | 0 | 42 | COMPLETE |
| DOC-003 | joi190079supp2_prod.pdf | PDF_PAGE | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-004 | joi190079supp3_prod.pdf | PDF_PAGE | 1 | 1 | 0 | 1 | COMPLETE |

Total source units: 63. Reusable units: 63. Fresh-required units: 0. There is no reusable-derivative coverage gap. All 63 pages have received new mapper reasoning; reusable counts measure availability of extraction aids only.

## Exact downstream mapping assignments

- Main mapper: DOC-001 PDF pp.1-10, using per-page native/normalized text and images for pp.3,5-9.
- Support shard 1: DOC-002 PDF pp.1-21, using exact per-page native/layout files and pp.1-21 aggregate derivatives; reusable images additionally cover pp.17,21.
- Support shard 2: DOC-002 PDF pp.22-42, using exact 21-page native/layout aggregate derivatives.
- Support result/operational scope: DOC-003 PDF pp.1-10, with per-page renderings for every eFigure on pp.2-10; DOC-004 PDF p.1, with native/layout text. This scope may share one support shard within the 200000-character context bound.

Protocol layout_all_pages contains 219075 characters and native_all_pages contains 201060 characters; neither should be loaded in its entirety into one support shard. The disjoint pp.1-21 and pp.22-42 derivatives satisfy the bound. Sparse eFigure native text is PARTIAL as a graphic transcription, while complete reusable rendered pages close that derivative gap. No plotted value should be treated as an exact numerical point label unless the supplied figure prints it.
