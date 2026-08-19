# Complete Source Coverage

Unit counts use one PDF page as one unique source unit. `Mapped units` means each unit has an assigned direct or reusable-backed mapping lane; it is not a claim that later scientific relationship mapping is complete.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_dupuis_2024_oi_240111_1733431204.38761.pdf | PDF_PAGE | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | joi240111supp1_prod_1733431204.57929.pdf | PDF_PAGE | 46 | 0 | 46 | 46 | COMPLETE |
| DOC-003 | joi240111supp2_prod_1733431204.76024.pdf | PDF_PAGE | 23 | 23 | 0 | 23 | COMPLETE |

Totals: 80 unique units; 34 reusable units; 46 fresh-required units; 80 mapped units. The reusable-plus-fresh partition and mapped-total equality hold for every source row.

## Downstream assignments and gaps

- DOC-001 PDF pp. 1-11: reusable-backed mapping assigned to `main_evidence_mapping`; exact native-page locations and required rendered-page confirmation are in `evidence_asset_inventory.md`.
- DOC-002 PDF pp. 1-46: no native/layout/OCR/table/rendered reusable evidence exists. All 46 pages are fresh-required and assigned to `support_evidence_mapping` using the supplied PDF directly. The legacy document record's earlier "Not Audited by Design" scope is stale for Workflow 1.5.3 and is not a coverage boundary.
- DOC-003 PDF pp. 1-23: reusable-backed mapping assigned to `support_evidence_mapping`; exact native-page locations and required rendered-page confirmation are in `evidence_asset_inventory.md`.
