# Direct Source Inventory

Inventory method: recursive package-root filename inventory restricted to direct `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, and `.csv` files outside the audit area; direct PDF identity and page count verified with `pdfinfo`; SHA-256 recorded in `source_hashes_before.sha256`. No Office or CSV direct sources were present. No direct source was modified.

| Source ID | Package-relative path | Type | Stable units and exact locations | SHA-256 | Reuse result | Fresh mapping assignment |
|---|---|---|---|---|---|---|
| DOC-001 | jama_dupuis_2024_oi_240111_1733431204.38761.pdf | PDF | 11 PDF pages, pp. 1-11 | 3bad9f52dda0bc9785f3bce603964d856547d282a82291e8041038269876d524 | USABLE native text maps pp. 1-11; rendered pages map pp. 5-9 | None; main mapper uses reusable-backed pages 1-11 and direct PDF for final authority |
| DOC-002 | joi240111supp1_prod_1733431204.57929.pdf | PDF | 46 PDF pages, pp. 1-46 | 05270ecd389a8ba0aea6f462e0e3785077892769305daae517da05b09cfdd99d | No eligible extraction; document record only | Support mapper: fresh direct PDF mapping pp. 1-46 |
| DOC-003 | joi240111supp2_prod_1733431204.76024.pdf | PDF | 23 PDF pages, pp. 1-23 | f7a9d88b6c6ffb018ce740a7abef376ebfabb0e0d6761366dc18ebbbe13c6d0b | USABLE native text maps pp. 1-23; rendered pages map pp. 2-21 | None; support mapper uses reusable-backed pages 1-23 and direct PDF for final authority |

Direct-source total: 3 files, 80 unique PDF-page units. Reusable coverage: 34 units. Fresh-required coverage: 46 units.

## Direct-tool record

- `pdfinfo` established page counts: DOC-001 11, DOC-002 46, DOC-003 23; all are unencrypted PDFs.
- `sha256sum` established the three source hashes above.
- No direct DOC/DOCX/XLS/XLSX/CSV was found, so no Office extractor was needed.
