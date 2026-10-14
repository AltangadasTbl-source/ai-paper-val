# Direct-source inventory

Inventory covers this package only. A recursive extension inventory found five direct PDFs and no direct DOC, DOCX, XLS, XLSX, or CSV sources. Audit derivatives are not direct sources. Stable units are physical PDF pages, including cover, reference, administrative, and blank pages. Sources are unchanged and their hashes match the existing preprocessing identity record.

| Source ID | Source path | Format | Total units | Document role | Content and role basis |
|---|---|---|---:|---|---|
| DOC-001 | jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf | PDF | 12 | REPORT | Main JAMA trial article: Precision Immunotherapy to Improve Sepsis Outcomes. |
| DOC-002 | joi250116supp1_prod_1771885794.26255.pdf | PDF | 72 | PLAN | Bound prospective trial protocol and statistical analysis plan; no REPORT component. |
| DOC-003 | joi250116supp2_prod_1771885794.27755.pdf | PDF | 54 | REPORT | Online supporting methods, eTables, eFigures, and results, including references; supporting methods describe reporting context rather than a separate prospective plan. |
| DOC-004 | joi250116supp3_prod_1771885794.28255.pdf | PDF | 28 | REPORT | Nonauthor collaborator appendix associated with the reported study; administrative material still requires full unit mapping. |
| DOC-005 | joi250116supp4_prod_1771885794.28755.pdf | PDF | 1 | REPORT | Published study data-sharing statement; no prospective statistical design content. |

Total: 5 direct sources, 167 PDF_PAGE units. All are unencrypted. Page counts were confirmed from each direct PDF with the supplied `workflow_1_6_2/scripts/pdf_tools.py info` helper, using the temporary pinned environment: PyMuPDF 1.26.4 and pypdf 5.9.0. Direct `pdfinfo` was unavailable. An earlier identity check used the user-requested interpreter with PyMuPDF 1.28.0; the pinned helper repeated and confirmed every count before handoff. Hash engine: direct `sha256sum`; exact hashes are in `source_hashes_before.sha256`.

Legacy document records contain mixed administrative metadata and prior review summaries. Only source identity and extraction-location fields inform this inventory; scientific summaries, dispositions, and counts do not define review scope. Source content determines the roles above.
