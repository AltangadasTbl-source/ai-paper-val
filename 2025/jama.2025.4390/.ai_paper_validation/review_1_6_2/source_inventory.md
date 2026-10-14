# Workflow 1.6.2 Direct-Source Inventory

Scope: this package only. Recursive extension inventory found exactly four supplied PDF sources and no DOC, DOCX, XLS, XLSX, or CSV sources. Workflow controls and audit derivatives are not supplied scientific sources. Stable source units are physical PDF pages, including cover, references, administrative content, and signatures; no source page is excluded from mapping.

| Source ID | Source path | Document role | Content basis | Unit type | Total units | Source identity |
|---|---|---|---|---|---:|---|
| DOC-001 | jama_garrison_2025_oi_250019_1749674951.29054.pdf | REPORT | Main BedMed randomized clinical trial article; results, tables, figures, and interpretation. | PDF_PAGE | 12 | Current SHA-256 in source_hashes_before.sha256; historical initial-record hash differs. |
| DOC-002 | joi250019supp1_prod_1749674951.29554.pdf | PLAN | Contents identifies BedMed protocol version May 2, 2016 and protocol amendment log. This physical bundle contains plan versions/amendments only. | PDF_PAGE | 18 | Current SHA-256 agrees with historical initial document record. |
| DOC-003 | joi250019supp2_prod_1749674951.30054.pdf | PLAN | Contents and rendered/OCR heading identify statistical analysis plan, attestation, and signatures. No results-report component. | PDF_PAGE | 7 | Current SHA-256 agrees with historical initial document record. |
| DOC-004 | joi250019supp3_prod_1749674951.30054.pdf | REPORT | Supplemental administrative information and methods followed by eFigures and eTables reporting trial data; this is a non-plan results supplement. | PDF_PAGE | 49 | Current SHA-256 in source_hashes_before.sha256; historical initial-record hash differs. |

Total: 86 physical PDF pages. No mixed REPORT/PLAN bundle was identified. Document roles are based on content, not supplement number. Plan citations to material outside this package do not create additional supplied sources.

Page totals were freshly confirmed with `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py info SOURCE`, engine PyMuPDF (pinned package-local fallback), because tooling_record.md records direct pdfinfo absent. Hash engine: direct sha256sum. Source files remain unchanged.

Historical extraction metadata is used only for source identity, extraction quality, and location coverage. Its prior audit exclusions are not carried forward. No old candidate, screening, classification, checker, verifier, critic, or report content was used.

The main and results sources have different current hashes from the historical initial document records. The later review_1_5_1 derivatives have no retained matching source-hash proof. They are conservatively classified STALE for current-source scientific authority; all 61 main/results pages require fresh direct-source mapping. They remain available as locators, with current-source evidence taking precedence. The 25 protocol/SAP pages have reusable source-matched evidence, including rendered SAP pages where encoded native text is unreadable.
