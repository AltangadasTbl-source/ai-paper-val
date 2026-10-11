# Direct Source Inventory

Inventory completed by fresh asset-curator agent /root/curator. Package-relative paths are used throughout. Direct source discovery inspected the current package recursively for PDF, DOC, DOCX, XLS, XLSX, and CSV files; no sibling packages were inspected. Exactly four direct PDFs were found. No Office, workbook, or CSV source exists. Unit counts were confirmed by direct Poppler pdfinfo 25.03.0. Sources are unencrypted. Before hashes are in source_hashes_before.sha256.

| Source ID | Source path | Format | Unit type | Total units | Document role | Role assignment by content | Mixed bundle |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_parshuram_2018_oi_180015.pdf | PDF | PDF_PAGE | 11 | REPORT | JAMA Original Investigation, Effect of a Pediatric Early Warning System on All-Cause Mortality in Hospitalized Pediatric Patients; EPOCH Randomized Clinical Trial. Includes reported findings, tables, flow figure, discussion, references, and subsequent article-related pages; every physical page remains in scope. | No REPORT/PLAN mixture identified |
| DOC-002 | joi180015supp1_prod.pdf | PDF | PDF_PAGE | 37 | PLAN | Research Protocol 005, version dated 23 February 2011, protocol summary, prospective methods, operational appendices, background study results and references. Historical results inside this protocol retain PLAN role. | No REPORT/PLAN mixture identified |
| DOC-003 | joi180015supp2_prod.pdf | PDF | PDF_PAGE | 7 | PLAN | EPOCH SAP, Primary / Secondary Analysis, hospital-level and individual-level models, code, adjustments, and analysis definitions. Past-tense language does not convert this supplied statistical analysis plan to a results report. | No REPORT/PLAN mixture identified |
| DOC-004 | joi180015supp3_prod.pdf | PDF | PDF_PAGE | 14 | REPORT | Supplementary Online Content containing eFigures 1-2, outcome definitions, eTables 2-4 observed hospital/patient outcomes and eTable 5 sample assumptions/post-trial calculations. Planning assumptions reproduced within this results supplement do not establish a separate protocol/SAP document. | No separate PLAN document bound into this supplement |

Total direct units: 69 PDF pages. Document roles: two REPORT files (25 pages), two PLAN files (44 pages).

Commands: pdfinfo "SOURCE.pdf"; sha256sum -- "SOURCE.pdf". Exact source hashes are stored separately, never inferred from earlier audit records. Native-text identity and page boundaries were checked against direct extraction as documented in evidence_asset_inventory.md. Document roles are inventory classifications; later exact-location rechecks confirm candidate-specific classifications.

Provider provenance: the user's current-provider instruction overrides the package's historical openrouter setting. No provider controls or credentials were changed. A coordinator-reported narrowly adapted local validator may be required for that literal provider metadata check; all scientific validation must remain unchanged.
