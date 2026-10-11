# Workflow 1.6.2 Direct Source Inventory

Scope: the current paper package only. A recursive extension inventory found five direct PDFs and no DOC, DOCX, XLS, XLSX, or CSV sources. Workflow-control files and audit derivatives are not direct sources. Source counts, byte sizes, and SHA-256 values were checked against the current files with direct `pdfinfo` and `sha256sum`; every hash agrees with the existing package manifest. Document roles below are assigned from source content. Old scientific routing statements in document records are ignored.

| Source ID | Source path | Document role | Content and exact scope | Unit type | Total units | Bytes | Downstream mapper |
|---|---|---|---|---|---:|---:|---|
| DOC-001 | jama_arleth_2024_oi_240147_1738701765.27201.pdf | REPORT | Main TRAUMOX2 article; source PDF pp. 1-11 | PDF_PAGE | 11 | 569159 | main_quantitative_mapper |
| DOC-002 | joi240147supp1_prod_1738701765.28701.pdf | PLAN | Bound protocol/SAP bundle: cover p. 1; original protocol v1.4 pp. 2-35; final protocol v1.8 pp. 36-77 including prospective DMSC charter pp. 68-73; change summary pp. 78-79; SAP v1.0 and its supporting plan material pp. 80-103 | PDF_PAGE | 103 | 980743 | support_quantitative_mapper |
| DOC-003 | joi240147supp2_prod_1738701765.29201.pdf | REPORT | Results supplement: contents p. 1; eMethods pp. 2-12; eFigure p. 13; eTables 1-11 pp. 14-25; references p. 26 | PDF_PAGE | 26 | 564891 | support_quantitative_mapper |
| DOC-004 | joi240147supp3_prod_1738701765.30201.pdf | REPORT | Accompanying collaborator list, pp. 1-3; descriptive administrative report material | PDF_PAGE | 3 | 125002 | support_quantitative_mapper |
| DOC-005 | joi240147supp4_prod_1738701765.30701.pdf | REPORT | Accompanying data-sharing statement, p. 1; descriptive administrative report material | PDF_PAGE | 1 | 15824 | support_quantitative_mapper |

DOC-002 contains several PLAN versions and prospective operational documents, with no REPORT results section. No supplied bundle combines REPORT and PLAN content. DOC-004 and DOC-005 are report-associated administrative materials rather than prospective trial-analysis plans; all four pages still require mapping and an explicit applicability record.

Unique total source units: 144. Unique reusable-backed units: 141. Fresh-required units: 3. Mapped units at this inventory handoff: 0. Every unit is assigned to a mapper; no page is excluded by an earlier audit's scope.

Fresh-required assignments: support_quantitative_mapper must inspect DOC-002 source pp. 33 and 75 (embedded participant and study-progress timelines) and p. 103 (embedded CONSORT flow diagram). Existing native text and the overlapping pp. 62-91 layout text do not represent those figures. Direct CPU rendering with recorded `pdftoppm` or `pdftocairo` must supply the visual evidence, with targeted `tesseract` only if needed. No Office conversion or fallback helper is required.

All source hashes are in `source_hashes_before.sha256`, with package-relative paths. This inventory does not diagnose reporting issues.
