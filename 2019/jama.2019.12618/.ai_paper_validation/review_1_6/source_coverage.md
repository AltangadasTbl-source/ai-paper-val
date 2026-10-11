# Workflow 1.6 Source Coverage

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_rathinam_2019_oi_190092.pdf | PDF_PAGE | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | joi190092supp1_prod.pdf | PDF_PAGE | 16 | 16 | 0 | 16 | COMPLETE |
| DOC-003 | joi190092supp2_prod.pdf | PDF_PAGE | 153 | 134 | 19 | 153 | COMPLETE |
| DOC-004 | joi190092supp3_prod.pdf | PDF_PAGE | 83 | 83 | 0 | 83 | COMPLETE |
| DOC-005 | joi190092supp4_prod.pdf | PDF_PAGE | 1 | 1 | 0 | 1 | COMPLETE |

Final coverage: total 263 = reusable 244 + fresh-required 19 = mapped 263. Every source row is COMPLETE after the six disjoint fresh-agent mapping assignments.

DOC-003 fresh-required pages, exactly: 15, 19, 74, 81, 84, 89, 90, 91, 94, 96, 105, 107, 109, 116, 118, 120, 133, 134, 136. Current Poppler and reusable layout both yield empty page records for these pages. They require direct-source rendering and visual mapping, with targeted CPU OCR when useful. DOC-003 p80 also has an empty text record, but an existing readable rendered page supplies reusable coverage and was visually inspected by the curator. Count p80 once among reusable units. Empty text does not prove a blank source page.

Disjoint downstream scopes: DOC-001 pp1-10 main; DOC-002 pp1-16 and DOC-005 p1 support; DOC-003 pp1-64 (fresh15,19); DOC-003 pp65-128 (fresh74,81,84,89,90,91,94,96,105,107,109,116,118,120); DOC-004 pp1-64; DOC-003 pp129-153 (fresh133,134,136) plus DOC-004 pp65-83. Each source page, including administrative/reference/cover pages, must receive an explicit mapped record. Produce separate durable parts if rendered-page or 120-relationship context bounds are reached.

Coordinator closure: all six fresh mapping agents completed disjoint scopes on 2026-10-11. All 263 pages have complete per-page registers; every one of the 19 fresh-required pages was directly rendered and visually inspected, with CPU OCR where useful. Mapped 263 = total 263.
