# Direct Source Inventory

Direct-source identification was limited to supplied local PDF, DOC, DOCX, XLS, XLSX, and CSV files outside the audit area. No DOC, DOCX, XLS, XLSX, or CSV source was present. Hashes are recorded separately in `source_hashes_before.sha256`.

| Source ID | Package-relative source path | Format | Stable unit type | Units | Direct inspection status | Reusable coverage | Fresh-required scope | Downstream mapper assignment |
|---|---|---|---|---:|---|---|---|---|
| DOC-001 | jama_atherton_2025_oi_240145_1741627844.85412.pdf | PDF | PDF_PAGE | 11 | `pdfinfo` confirmed 11 pages; unencrypted | Native page-delimited text covers pp. 1-11; rendered/OCR companions cover pp. 3, 5-9 | None | main quantitative mapper: reusable-backed pp. 1-11 |
| DOC-002 | joi240145supp1_prod_1741627844.87412.pdf | PDF | PDF_PAGE | 46 | `pdfinfo` confirmed 46 pages; unencrypted | No complete quantitative-ready reusable extraction; two rights-screen images and one legacy crop are partial only | pp. 1-46 | support quantitative mapper: fresh direct-source extraction and mapping, pp. 1-46 |
| DOC-003 | joi240145supp3_prod_1741627844.89412.pdf | PDF | PDF_PAGE | 9 | `pdfinfo` confirmed 9 pages; unencrypted | Native page-delimited text covers pp. 1-9; rendered/OCR companions cover pp. 3-9 | None | support quantitative mapper: reusable-backed pp. 1-9 |
| DOC-004 | joi240145supp4_prod_1741627844.90412.pdf | PDF | PDF_PAGE | 48 | `pdfinfo` confirmed 48 pages; unencrypted | No complete quantitative-ready reusable extraction; four selected rendered pages are partial only | pp. 1-48 | support quantitative mapper: fresh direct-source extraction and mapping, pp. 1-48 |

Totals: 4 direct sources, 114 unique source units, 20 reusable units, 94 fresh-required units, and 0 scientifically mapped units at this stage. The reusable and fresh-required counts partition every direct source. The missing Supplements 2 and 5 mentioned in legacy records are not supplied direct sources and are not counted.
