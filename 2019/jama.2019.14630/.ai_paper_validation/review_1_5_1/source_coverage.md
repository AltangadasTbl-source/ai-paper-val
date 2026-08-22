# Complete source coverage

The stable unit is one PDF page. Reusable units are backed by an eligible, source-matched pre-existing layout/native extraction; a page covered only by a document record is not reusable. Every fresh-required unit has a downstream direct-source mapper assignment in `coverage_manifest.md`.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_saynorea_2019_oi_190106_1635377898.43062.pdf | PDF_PAGE | 14 | 14 | 0 | 14 | COMPLETE |
| DOC-002 | joi190106supp1_prod_1635377898.47058.pdf | PDF_PAGE | 75 | 0 | 75 | 75 | COMPLETE |
| DOC-003 | joi190106supp2_prod_1635377898.49605.pdf | PDF_PAGE | 30 | 0 | 30 | 30 | COMPLETE |
| DOC-004 | joi190106supp3_prod_1635377898.49725.pdf | PDF_PAGE | 29 | 29 | 0 | 29 | COMPLETE |
| DOC-005 | joi190106supp4_prod_1635377898.50723.pdf | PDF_PAGE | 1 | 0 | 1 | 1 | COMPLETE |

**Totals:** 149 unique units; 43 reusable units; 106 fresh-required units; 149 mapped units.

## Exact coverage and gaps

- **DOC-001:** `document_outputs/DOC-001/main_layout.txt` has 14 form-feed-delimited pages and maps to PDF pp. 1-14. Page-native files provide higher-fidelity per-page coverage for pp. 1-11. The retained OCR and source-location metadata for p. 3 are auxiliary. There is no scientific-coverage gap.
- **DOC-002:** only document-identity/preprocessing records exist; no eligible native/layout/OCR/table/page extraction maps any PDF page. PDF pp. 1-75 require fresh direct-source mapping.
- **DOC-003:** only document-identity/preprocessing records exist; no eligible native/layout/OCR/table/page extraction maps any PDF page. PDF pp. 1-30 require fresh direct-source mapping.
- **DOC-004:** `document_outputs/DOC-004/supp3_layout.txt` has 29 form-feed-delimited pages and maps to PDF pp. 1-29. Page-native files cover pp. 1-27; selected OCR/rendered assets are auxiliary, including sparse p. 8. There is no scientific-coverage gap.
- **DOC-005:** only document-identity/preprocessing records exist; no eligible native/layout/OCR/table/page extraction maps its page. PDF p. 1 requires fresh direct-source mapping.

Legacy record statements that a source was “not audited by design” are stale for workflow 1.5.1 and did not reduce fresh-required coverage.

