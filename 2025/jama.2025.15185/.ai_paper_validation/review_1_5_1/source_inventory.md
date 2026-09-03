# Direct Source Inventory

Inventory performed from the supplied package root on 2026-09-03. Direct sources were identified by extension and inspected with `pdfinfo`; no source was modified. There are no supplied DOC, DOCX, XLS, XLSX, or CSV files. Stable review unit: `PDF_PAGE`.

| Source ID | Package-relative source path | Type | Total stable units | Direct-tool identity check | Reusable-page coverage | Fresh direct-source assignment |
|---|---|---|---:|---|---|---|
| DOC-001 | jama_engelter_2025_oi_250066_1761597796.45511.pdf | PDF | 10 | `pdfinfo`: 10 pages | pp. 1-10 | None; later main mapper uses reusable source-linked text/rendered evidence for pp. 1-10. |
| DOC-002 | joi250066supp1_prod_1761597796.4601.pdf | PDF | 94 | `pdfinfo`: 94 pages | None | Later support mapper: direct extraction and mapping of pp. 1-94. |
| DOC-003 | joi250066supp2_prod_1761597796.4701.pdf | PDF | 18 | `pdfinfo`: 18 pages | None | Later support mapper: direct extraction and mapping of pp. 1-18. |
| DOC-004 | joi250066supp3_prod_1761597796.4701.pdf | PDF | 27 | `pdfinfo`: 27 pages | pp. 10-27 | Later support mapper: fresh direct extraction and mapping of pp. 1-9; reusable source-linked assets support pp. 10-27. |
| DOC-005 | joi250066supp4_prod_1761597796.4751.pdf | PDF | 8 | `pdfinfo`: 8 pages | None | Later support mapper: direct extraction and mapping of pp. 1-8. |
| DOC-006 | joi250066supp5_prod_1761597796.4751.pdf | PDF | 1 | `pdfinfo`: 1 page | None | Later support mapper: direct extraction and mapping of p. 1. |
| DOC-007 | joi250066supp6_prod_1761597796.4801.pdf | PDF | 1 | `pdfinfo`: 1 page | None | Later support mapper: direct extraction and mapping of p. 1. |

## Counts and partition

- Direct sources: 7 PDFs; 0 DOC/DOCX/XLS/XLSX/CSV sources.
- Unique direct units: 159 PDF pages.
- Reusable-covered units: 28 (DOC-001 pp. 1-10; DOC-004 pp. 10-27).
- Fresh-required units: 131 (DOC-002 pp. 1-94; DOC-003 pp. 1-18; DOC-004 pp. 1-9; DOC-005 pp. 1-8; DOC-006 p. 1; DOC-007 p. 1).
- Partition check: 28 + 131 = 159.

## Source-integrity baseline

The seven direct-source SHA-256 values are recorded in `source_hashes_before.sha256`. That baseline is coordinator-owned and was present before this inventory; this curator did not alter it.

## Limitations

Earlier document-output status records labelled several sources “Not Audited by Design.” That historical scope is not a scientific coverage boundary in workflow 1.5.1; all such pages are explicitly fresh-required above.
