# Complete Direct-Source Coverage

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_aminian_2019_oi_190103.pdf | PDF_PAGE | 12 | 12 | 0 | 12 | COMPLETE |
| DOC-002 | joi190103supp1_prod.pdf | PDF_PAGE | 20 | 20 | 0 | 20 | COMPLETE |
| DOC-003 | joi190103supp2_prod.pdf | PDF_PAGE | 7 | 7 | 0 | 7 | COMPLETE |

Totals: 39 unique source units, 39 reusable-backed, 0 fresh-required. Mapped counts now equal every source total after both complete mapper artifacts closed all 39 pages.

Exact reusable partition and assignment:

- DOC-001 PDF pages 1–12: page-level native text, confirmed against direct-source layout text for every page; main mapper owns all 12 pages.
- DOC-002 PDF pages 1–5: later combined native/layout files under review_1_5_1/preprocessing, verified against every selected direct-source page; PDF pages 6–20: page-level native text, confirmed against direct-source layout text for every page; support mapper owns all 20 pages.
- DOC-003 PDF pages 1–7: later combined native/layout files under review_1_5_1/preprocessing, verified against all direct-source pages; support mapper owns all 7 pages.

There are no uncovered text units. The older page manifest contains no text extraction for DOC-002 pp1–5 or DOC-003 pp1–7, but the later source-matched assets close those derivative gaps. Legacy extraction-map scope is partial and never limits mapping. Existing page images cover DOC-001 pp3,5,6,7,8,9,10 and DOC-002 pp6,7,8,9,10,11,12,13,14,15,16,18,19,20. Other pages lack reusable images; their native/layout text is usable. Mappers can render exact pages on CPU if direct visual inspection requires it, without counting overlapping derivatives as new source units. Every candidate requires exact direct-source confirmation regardless of reusable coverage.
