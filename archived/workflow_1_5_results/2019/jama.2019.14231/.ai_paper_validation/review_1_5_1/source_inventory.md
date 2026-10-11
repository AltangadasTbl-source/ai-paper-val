# Direct Source Inventory

Inventory time (UTC): 2026-08-18. This inventory was limited to direct package sources and eligible pre-existing extraction assets. Legacy candidate, verifier, critic, adjudication, and final-report content was excluded from discovery scope.

| Source ID | Package-relative path | Format | Stable unit type | Units | SHA-256 | Direct inspection | Fitness | Notes |
|---|---|---|---|---:|---|---|---|---|
| DOC-001 | jama_aminian_2019_oi_190103.pdf | PDF | PDF_PAGE | 12 | fcf715eadcef54b5c78a557ae684311a96c22c502f4297293156d6cf7f94e4b9 | `pdfinfo` reports 12 pages; native text layer present. | USABLE | Main article; reusable native text covers PDF pp. 1-12. |
| DOC-002 | joi190103supp1_prod.pdf | PDF | PDF_PAGE | 20 | ec4e0375222279bcc2137db1be3649d22fd86997f308c1c8f0cba85cfba4c322 | `pdfinfo` reports 20 pages; native text layer present. | PARTIAL | Results supplement; reusable native text covers PDF pp. 6-20 only. PDF pp. 1-5 require fresh direct-source mapping. |
| DOC-003 | joi190103supp2_prod.pdf | PDF | PDF_PAGE | 7 | 254d15bd2cc32b6c0c21d399caa17ac84fd6b1136e320cd046e0cfefc3ed713f | `pdfinfo` reports 7 pages; native text layer present. | PARTIAL | Protocol; no reusable page extraction exists. PDF pp. 1-7 require fresh direct-source mapping. |

## Direct-source totals

- Unique direct sources: 3.
- Unique stable source units: 39 PDF pages.
- Reusable-backed units: 27 PDF pages.
- Fresh-required units: 12 PDF pages.
- No direct PDF, DOC, DOCX, XLS, XLSX, or CSV source other than the three PDFs was present at package root.

## Commands and local tool versions

- `pdfinfo <source.pdf>`: Poppler `26.01.0`.
- `pdftotext -v`: Poppler `26.01.0` (not run to create or alter an artifact in this curation stage).
- `file <source.pdf>`: identified all three direct sources as PDF documents.
- `sha256sum -- <source.pdf>`: generated the direct-source digests recorded above; the coordinator-owned `source_hashes_before.sha256` remains authoritative for this run.

No direct source was modified.
