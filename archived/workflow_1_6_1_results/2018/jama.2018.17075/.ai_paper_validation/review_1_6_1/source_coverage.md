# Complete source-coverage ledger

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_cooper_2018_oi_180132.pdf | PDF_PAGE | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | joi180132supp1_prod.pdf | PDF_PAGE | 194 | 194 | 0 | 194 | COMPLETE |
| DOC-003 | joi180132supp2_prod.pdf | PDF_PAGE | 24 | 24 | 0 | 24 | COMPLETE |
| DOC-004 | joi180132supp3_prod.pdf | PDF_PAGE | 1 | 1 | 0 | 1 | COMPLETE |

Unique-unit totals: 229 total, 229 reusable-backed, 0 fresh-required, and 229 mapped after complete specialist handoffs. Mapping completed for every page; reusable coverage describes preprocessing coverage only. The coordinator finalized mapped counts against all four durable mapper artifacts.

No uncovered source unit remains without an eligible derivative. Native and layout extraction is PARTIAL for DOC-002 because PDF pages 140–162, 183–185, and 187 (27 pages) have no usable native text. Existing readable rendered PNGs cover all those exact pages; the support mapper must inspect all 27 visually. No OCR asset exists. Absence of OCR is a derivative limitation, not permission to omit those pages.

Disjoint mandatory mapping assignments:

| Assignment | Exact source units | Basis | Fresh-required units |
|---|---|---|---:|
| Main mapper | DOC-001 PDF pages 1–10 | Source-matched native/layout text and corresponding rendered pages | 0 |
| Support shard 1 | DOC-002 PDF pages 1–69 | Native/layout text and corresponding rendered pages; 161,128 normalized character-count bound | 0 |
| Support shard 2 | DOC-002 PDF pages 70–138 | Native/layout text and corresponding rendered pages; 187,760 normalized character-count bound | 0 |
| Support shard 3 | DOC-002 PDF pages 139–194; DOC-003 PDF pages 1–24; DOC-004 PDF page 1 | Text plus mandatory visual mapping of all 27 native-blank plan pages; approximately 82,329 native characters combined | 0 |

These assignments partition 229 unique PDF pages without overlap. Character bounds were measured per form-feed-delimited page with awk over reusable native text. Page images are listed individually in evidence_asset_inventory.md and hash-protected; source pages remain final authority.

Mapping completion evidence: main_quantitative_evidence.md covers 10/10 main pages; plan_001.md covers 69/69 plan pages; plan_002.md covers 69/69 plan pages; support_003.md covers 56/56 remaining plan pages, 24/24 results-supplement pages, and 1/1 data-sharing page. Canonical support map merges all 219 support pages without loss. Sparse-text raster instruments and flowcharts outside the 27 native-blank pages were also inspected visually, including DOC-002 p.39 and pp.103-107. All page-level applicability decisions remain in the maps.
