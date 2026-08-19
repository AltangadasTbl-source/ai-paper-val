# Source Coverage Ledger

Stable units are unique PDF pages. “Reusable units” means a usable existing native-text derivative maps to that exact page. “Fresh-required units” means no usable existing derivative covered that page at inventory; each has a newly created direct native and layout extraction in this run. The evidence mappers completed every assigned page.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_wilson_2020_oi_190154.pdf | PDF_PAGE | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | joi190154supp1_prod.pdf | PDF_PAGE | 15 | 0 | 15 | 15 | COMPLETE |
| DOC-003 | joi190154supp2_prod.pdf | PDF_PAGE | 49 | 29 | 20 | 49 | COMPLETE |

## Exact coverage and fresh-source assignments

- DOC-001: reusable native text maps one-to-one to PDF pages 1-11. Main evidence mapping is assigned to `extraction/main_quantitative_evidence.md`.
- DOC-002: no reusable page extraction exists. Fresh native and layout text map one-to-one to PDF pages 1-15 under `preprocessing/native_text/DOC-002_PROTOCOL/` and `preprocessing/layout_text/DOC-002_PROTOCOL/`. Support evidence mapping is assigned to `extraction/support_quantitative_evidence.md`.
- DOC-003: reusable native text maps one-to-one to PDF pages 17-45. Fresh native and layout text map one-to-one to PDF pages 1-16 and 46-49 under `preprocessing/native_text/DOC-003_RESULTS/` and `preprocessing/layout_text/DOC-003_RESULTS/`. The sparse direct text on page 8 is paired with a fresh rendered visual page. Support evidence mapping is assigned to `extraction/support_quantitative_evidence.md`.

The partitions reconcile: 11 + 15 + 49 = 75 total units; 40 reusable units + 35 fresh-required units = 75 total units. The completed mapper assignments cover the disjoint union of all 75 units.
