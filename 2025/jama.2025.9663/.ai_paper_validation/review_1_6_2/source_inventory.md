# Direct Source Inventory

Scope: every direct PDF, DOC, DOCX, XLS, XLSX and CSV in the current paper package, excluding workflow controls and derivative tooling. Exactly three direct sources are present; all are PDFs. No source was modified. Source SHA-256 values match the legacy package_manifest.yaml; historical audit exclusions do not constrain this run.

| Source ID | Source path | Format | Document role | Total stable units | Source identity and content basis | SHA-256 |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_martin_2025_oi_250042_1753377747.91025.pdf | PDF | REPORT | 11 | UK-ROX randomized trial main article: title, structured abstract, methods, results, tables, figures and end matter. | 2081dc4315dd23f92712a5fd95cc03c5d3e9b7ee4fc8e24a27d8bf24d68c3266 |
| DOC-002 | joi250042supp1_prod_1753377747.92525.pdf | PDF | PLAN | 136 | Bound original/final protocol, changes, original/final statistical analysis plan and changes; prospective content throughout. No REPORT bundle component identified. Visually inspected protocol page29 and SAP page100 confirm content roles. | 6fd5db6abde804baaa62264ddd158e664307941e4162fe1f2e80b4eb80662504 |
| DOC-003 | joi250042supp2_prod_1753377747.93025.pdf | PDF | REPORT | 29 | Contents, eMethods, eFigures/eTables with reported trial results, and references. Definitions in a results supplement do not make it a prospective plan. | bcd3bce5a729190ce6917128dc271f60ad99acb2f48395d86d69f88653e2469c |

Unit type is PDF_PAGE, meaning the one-based physical supplied PDF page rather than printed footer numbering. All 176 pages are included in mapping, including contents and references. Native text in PLAN material is glyph-mapped and unusable; reusable raster assets cover 32 of its 136 pages. A legacy source record that says plan material was excluded is identity metadata only.

Page counts and encryption status were freshly confirmed using the supplied fallback helper with temporary PyMuPDF 1.26.4: 11,136,29 pages, all unencrypted. Commands: .ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py info followed by each exact Source path above. Direct-source hashes are recorded in source_hashes_before.sha256. Direct PDF tools were absent in tooling_record.md.

Existing document records and page manifests supply source/page links. Legacy raw native/layout/OCR/raster derivatives are retained as evidence aids; scientific findings and final classifications are reconstructed by later agents.
