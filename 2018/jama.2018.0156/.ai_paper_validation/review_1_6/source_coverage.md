# Workflow 1.6 Complete Source Coverage

Complete scientific mapping now covers every source unit. Reusable units are unique PDF pages covered by current-source-matched native/layout text or source-hash-matched OCR and images; overlapping derivatives count once. The original reusable/fresh-required partition is retained, and the table records final mapped counts.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_jabre_2018_oi_180004.pdf | PDF_PAGE | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 | joi180004supp1_prod.pdf | PDF_PAGE | 134 | 133 | 1 | 134 | COMPLETE |
| DOC-003 | joi180004supp2_prod.pdf | PDF_PAGE | 3 | 3 | 0 | 3 | COMPLETE |

Total: 146 source units, 145 reusable units, 1 fresh-required unit. Every page enters scientific mapping, regardless of derivative fitness or quantitative density.

## Exact reusable and fresh-required partition

DOC-001: reusable pp. 1-9. DOC-003: reusable pp. 1-3.

DOC-002: native/layout-backed pp. 1-51, 53-107, 110-125 (122 pages); OCR-plus-image-backed p. 52, pp. 108-109, 126-133 (11 pages). Fresh-required: p. 134 (one page), with neither usable native/layout content nor OCR/rendered derivative. Direct source rendering and visual mapping are mandatory. Other native/layout-empty pages have usable existing OCR and images and therefore remain reusable-backed; their scientific review includes direct-source confirmation when a candidate depends on them.

## Proposed bounded mapping shards

| Shard | Source scope | Page count | Normalized reusable layout characters | Fresh-required scope |
|---|---|---:|---:|---|
| main-001 | DOC-001 pp. 1-9 | 9 | Below 200000 | None |
| support-001 | DOC-002 pp. 1-32 | 32 | 68615 | None |
| support-002 | DOC-002 pp. 33-64 | 32 | 76587 | None |
| support-003 | DOC-002 pp. 65-96 | 32 | 75054 | None |
| support-004 | DOC-002 pp. 97-125 | 29 | 56812 plus existing OCR for pp. 108-109 | None |
| support-005 | DOC-002 pp. 126-134 | 9 | 0 layout characters; existing OCR for pp. 126-133 | p. 134 |
| support-006 | DOC-003 pp. 1-3 | 3 | Below 200000 | None |

Each proposed shard satisfies the 200000 normalized-character and 32 rendered-page bounds. Exact final assignments belong in the coordinator's coverage_manifest.md. No scientific-coverage limitation is accepted: p. 134 must be freshly inspected before completion.

## Coordinator completion

All mapping artifacts are durable and complete. DOC-001 maps 9/9 pages; DOC-002 maps 134/134 across five disjoint support shards; DOC-003 maps 3/3 pages. DOC-002 p134 was freshly rendered with direct Poppler 25.03.0 and visually confirmed as header/footer-only with an empty body. Initial mapped=0 refers to inventory time; the authoritative table above now records completed counts. No scientific source-unit gap remains. New derivative engines/commands are recorded in each corresponding extraction artifact.
