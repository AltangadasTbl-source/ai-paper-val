# Complete Direct-Source Coverage

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_sun_2024_oi_240088_1746815064.14747.pdf | PDF_PAGE | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | joi240088supp1_prod_1746815064.21247.pdf | PDF_PAGE | 25 | 18 | 7 | 25 | COMPLETE |
| DOC-003 | joi240088supp2_prod_1746815064.36071.pdf | PDF_PAGE | 167 | 0 | 167 | 167 | COMPLETE |

**Partition check:** 203 total units = 29 reusable units + 174 fresh-required units; mapped units = 203.

## Exact coverage and downstream assignments

**DOC-001.** Reuse-backed units are PDF pages 1-11, via native page text; pages 5-9 also have retained rendered pages. No unit is fresh-required. `qc15_main_quantitative_mapper` is assigned the reuse-backed mapping of PDF pages 1-11. The normalized aggregate is a duplicate locator, not an additional unit source.

**DOC-002.** Reuse-backed units are PDF pages 1-2 and 10-25, via native text; pages 10-25 also have retained renders. Fresh-required units are PDF pages 3-9. `qc15_support_quantitative_mapper` is assigned both fresh direct-source extraction and mapping for pages 3-9 and reuse-backed mapping for pages 1-2 and 10-25. The prior extraction omitted pages 3-9, which must be mapped even if later found non-result-relevant. Sparse native text on pages 10-13 is paired with usable renders.

**DOC-003.** No unit is reuse-backed. Fresh-required units are PDF pages 1-167. `qc15_support_quantitative_mapper` is assigned fresh direct-source extraction and mapping for PDF pages 1-167. No native, layout, OCR, table, or rendered derivative exists; the legacy document record and manifest are inventory-only and do not cover scientific mapping.

Every non-usable or uncovered unit is included in the fresh-required count and has a mapper assignment. `Mapped units` records assigned complete coverage, not a claim that a legacy derivative itself was sufficient.
