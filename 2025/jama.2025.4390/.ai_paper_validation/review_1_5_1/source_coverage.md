# Complete Source Coverage Ledger — Workflow 1.5.1

`Mapped units` means each unit has been placed in either the reusable or fresh-direct mapping partition. Fresh-direct mapping is mandatory for every fresh-required unit and must be completed by downstream mapper assignments. Counts are unique PDF pages.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_garrison_2025_oi_250019_1749674951.29054.pdf | PDF_PAGE | 12 | 0 | 12 | 12 | COMPLETE |
| DOC-002 | joi250019supp1_prod_1749674951.29554.pdf | PDF_PAGE | 18 | 0 | 18 | 18 | COMPLETE |
| DOC-003 | joi250019supp2_prod_1749674951.30054.pdf | PDF_PAGE | 7 | 0 | 7 | 7 | COMPLETE |
| DOC-004 | joi250019supp3_prod_1749674951.30054.pdf | PDF_PAGE | 49 | 0 | 49 | 49 | COMPLETE |

## Partition and assignment basis

| Source ID | Reusable page set | Fresh-required page set | Reason |
|---|---|---|---|
| DOC-001 | None | pp. 1-12 | All legacy page derivatives and maps are stale: legacy record SHA-256 `72ebde634187c4f60d10bad66cf649cb8d1df7e032a172ce4fb73abc1fa7f4fb` differs from current source SHA-256 `4e5c3847e835d3ba2694c543b4474df8230f84141d03fefc6f70748d6c4cc61b`. |
| DOC-002 | None | pp. 1-18 | Legacy page manifest is source-matched metadata only; it names no retained normalized page text, OCR, table extraction, or rendered evidence page. |
| DOC-003 | None | pp. 1-7 | Legacy manifest is source-matched metadata only; rights-review renders cover only pp. 1 and 7 and are not a documented scientific extraction. |
| DOC-004 | None | pp. 1-49 | All legacy page derivatives and maps are stale: legacy record SHA-256 `26d0e8b356d8cf498f93542029b96c3652dcbe96eb8a283e48393de163f92c39` differs from current source SHA-256 `d02bb335cb37cc4ad5907b864414c557c6822c19d7d297467391bade3ef5be82`. |

Totals: 86 total units = 0 reusable units + 86 fresh-required units; 86 mapped units. There is no scientific-coverage gap: every page is in the fresh-direct mapping partition.
