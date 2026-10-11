# Complete Source-Coverage Ledger

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_brenner_2019_oi_190039.pdf | PDF_PAGE | 7 | 7 | 0 | 7 | COMPLETE |
| DOC-002 | joi190039supp1_prod.pdf | PDF_PAGE | 62 | 27 | 35 | 62 | COMPLETE |
| DOC-003 | joi190039supp2_prod.pdf | PDF_PAGE | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-004 | joi190039supp3_prod.pdf | PDF_PAGE | 8 | 8 | 0 | 8 | COMPLETE |
| DOC-005 | joi190039supp4_prod.pdf | PDF_PAGE | 1 | 1 | 0 | 1 | COMPLETE |

Total unique source units: 88; reusable: 53; fresh-required: 35; mapped: 88. All five rows partition their source exactly. COMPLETE status follows the main mapper's seven individual page rows, support shard A's 42 individual page rows, and support shard B's 39 individual page rows. Every fresh-required protocol page was directly rendered and visually inspected; protocol p.49 is a scanned signed approval page rather than blank. No scientific source-coverage gap remains.

DOC-001: normalized/native/bounding-box text covers pp. 1-7, rendered pages supplement table and flow inspection. DOC-003: complete pp. 1-10 layout text. DOC-004: pp. 1-3 complete layout text plus normalized/native/bounding-box text for pp. 4-8. DOC-005: complete p. 1 layout text.

DOC-002 reusable pages: 2, 3, 4, 5, 9, 10, 11, 14, 15, 17, 25, 27, 28, 29, 33, 36, 39, 42, 43, 45, 46, 47, 48, 50, 55, 59, 60.

DOC-002 fresh-required pages: 1, 6, 7, 8, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 26, 30, 31, 32, 34, 35, 37, 38, 40, 41, 44, 49, 51, 52, 53, 54, 56, 57, 58, 61, 62. The reusable full layout file is source-matched but PARTIAL: these 34 pages contain non-whitespace control characters from embedded font encoding, and p. 49 has no extracted text. Conservatively assign all 35 pages to direct visual inspection, with targeted Tesseract CPU OCR where meaningful source content remains unreadable. An empty text page must be visually confirmed as blank or mapped from its image. The old layout remains a locator on fresh-required pages but does not confer reusable unit credit.

Downstream assignments: fresh main mapper owns DOC-001 pp. 1-7; fresh support mapper owns DOC-002 pp. 1-62, DOC-003 pp. 1-10, DOC-004 pp. 1-8, DOC-005 p. 1, covering both reusable and fresh-required units. Explicit extraction sharding may be assigned by the coordinator while preserving these source scopes.
