# Workflow 1.6 Direct Source Inventory

The package was inventoried recursively for PDF, DOC, DOCX, XLS, XLSX, and CSV direct sources, excluding the audit derivative area. Exactly four direct PDFs are supplied; no Office or CSV source is present. All 96 physical PDF pages are in scope, including reference, cover, and administrative pages. Stable units are physical PDF pages, numbered from 1. Sources are unmodified.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis | Assigned mapper |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_urashima_2019_oi_190023.pdf | PDF | PDF_PAGE | 9 | REPORT | Published AMATERASU trial article; p. 1 abstract, body results and discussion, p. 9 article information and references. | main_quantitative_mapper |
| DOC-002 | joi190023supp1_prod.pdf | PDF | PDF_PAGE | 45 | PLAN | p. 1 identifies initial protocol/SAP pp. 2-16, final protocol/SAP pp. 17-33, references pp. 34-35, operational appendices pp. 36-44, and approved changes p. 45. Historical plan versions and background data remain PLAN. | support_quantitative_mapper |
| DOC-003 | joi190023supp2_prod.pdf | PDF | PDF_PAGE | 41 | REPORT | Non-plan results supplement containing eTables, eFigures, and subgroup results. | support_quantitative_mapper |
| DOC-004 | joi190023supp3_prod.pdf | PDF | PDF_PAGE | 1 | REPORT | Published retrospective data-sharing statement associated with the article; contains availability/access terms, not prospective trial conduct or an analysis plan. No reported scientific numerical relationship is assumed absent before mapping. | support_quantitative_mapper |

No physically mixed REPORT/PLAN bundle was identified. DOC-002 contains several PLAN components and versions, rather than a results-report component. Role assignments are by content, and must be confirmed for every compared candidate location.

## Identity and tooling

Direct source identities and current page counts were confirmed by `pdfinfo` (Poppler 26.01.0). Source hashes were obtained using direct `sha256sum` and are recorded with package-relative paths in `source_hashes_before.sha256`. Direct `pdftotext` was used on source cover/administrative pages for inventory and role identification, writing no derivative. All tools use the recorded direct-tool path; no fallback environment, Office conversion, new OCR, network source, or GPU operation was needed.

Prior document metadata was inspected solely for source identity and extraction-location mapping. Its scope exclusions and conclusion fields were not adopted. In particular, the old main-document record described p. 9 as rights-only, whereas the current direct PDF p. 9 contains article information and references. The current inventory includes it. Historical absolute paths in manifests refer to a prior local root; exact package-relative paths resolve here. No old candidate, checker, verifier, critic, classification, endetail, or final-report file was opened as a discovery input.
