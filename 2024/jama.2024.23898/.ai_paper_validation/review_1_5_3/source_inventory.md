# Direct Source Inventory

This inventory includes every direct PDF, DOC, DOCX, XLS, XLSX, and CSV source at the package root. No direct DOC, DOCX, XLS, XLSX, or CSV source was present. Direct sources were inspected locally with `file` and `pdfinfo`; the PDF page count from `pdfinfo` is the stable unit count. SHA-256 baselines are recorded in `source_hashes_before.sha256` with package-relative paths.

| Source ID | Package-relative source path | Type | Stable unit type and count | Direct-source condition | Reusable coverage | Fresh mapping assignment |
|---|---|---|---|---|---|---|
| DOC-001 | jama_paterson_2024_oi_240139_1741633738.12862.pdf | PDF main article | PDF_PAGE, 10 | PDF 1.4; not encrypted; native text layer reported by the supplied page map | Native and normalized text for pp. 1-10; selected rendered pages 3, 4, 6, 7, and 8 | Main quantitative mapper: reuse-backed mapping of pp. 1-10, with direct PDF confirmation for any later candidate |
| DOC-002 | joi240139supp1_prod_1741633738.16362.pdf | PDF protocol | PDF_PAGE, 66 | PDF 1.7; encrypted with copy permitted; `pdfinfo` reports 66 pages | No reusable page extraction, render, table extraction, or source-location map | Support quantitative mapper: fresh direct-source extraction and mapping of pp. 1-66 |
| DOC-003 | joi240139supp2_prod_1741633738.17362.pdf | PDF statistical analysis plan | PDF_PAGE, 40 | PDF 1.7; encrypted with copy permitted; `pdfinfo` reports 40 pages | No reusable page extraction, render, table extraction, or source-location map | Support quantitative mapper: fresh direct-source extraction and mapping of pp. 1-40 |
| DOC-004 | joi240139supp3_prod_1741633738.18862.pdf | PDF results supplement | PDF_PAGE, 2 | PDF 1.6; not encrypted; native text layer reported by the supplied page map | Native and normalized text for pp. 1-2; rendered visual complement for p. 2 | Main quantitative mapper: reuse-backed mapping of pp. 1-2, including the p. 2 render for graphical labels, with direct PDF confirmation for any later candidate |
| DOC-005 | joi240139supp4_prod_1741633738.20861.pdf | PDF data-sharing statement | PDF_PAGE, 1 | PDF 1.4; not encrypted; `pdfinfo` reports 1 page | No reusable page extraction, render, table extraction, or source-location map | Support quantitative mapper: fresh direct-source extraction and mapping of p. 1 |

## Complete direct-source gap assignment

- DOC-001: no scientific-coverage gap; all pp. 1-10 have reuse-backed text coverage. Visual complements are available for pp. 3, 4, 6, 7, and 8.
- DOC-002: fresh-required pp. 1-66.
- DOC-003: fresh-required pp. 1-40.
- DOC-004: no scientific-coverage gap; p. 1 has reuse-backed text coverage and p. 2 has reuse-backed text plus a rendered visual complement.
- DOC-005: fresh-required p. 1.

The 12 reusable units and 107 fresh-required units are disjoint and partition all 119 unique direct-source units. “Mapped” in the coverage ledger means assigned to a reuse-backed or fresh direct-source mapper scope; it does not treat an old candidate, verifier, critic, endetail, or report artifact as evidence.
