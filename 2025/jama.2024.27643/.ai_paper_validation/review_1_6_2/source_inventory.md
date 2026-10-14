# Direct source inventory

Runtime agent: /root/curator. Complete package-only enumeration found six direct PDFs and no DOC, DOCX, XLS, XLSX, or CSV source. All 404 PDF pages enter mapping, including administrative and rights pages. Roles are assigned from document content. Protocol and SAP bundles contain several prospective plan versions, not REPORT components. Source hashes match the supplied identities recorded in the legacy package manifest; old scientific scope/dispositions are not adopted.

| Source ID | Source path | Format | Stable unit type | Total units | Document role | Content evidence |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_berry_2025_oi_240158_1742927563.7361.pdf | PDF | PDF_PAGE | 12 | REPORT | p.1 JAMA Original Investigation, CNM-Au8 in Amyotrophic Lateral Sclerosis; abstract, results, tables, figures and discussion. |
| DOC-002 | joi240158supp1_prod_1742927563.7611.pdf | PDF | PDF_PAGE | 229 | PLAN | p.1 HEALEY ALS Platform Trial Protocol Version 5.0; master protocol and CNM-Au8 regimen-specific appendix versions. |
| DOC-003 | joi240158supp2_prod_1742927563.7711.pdf | PDF | PDF_PAGE | 130 | PLAN | p.1 Master Statistical Analysis Plan Version 3.0; regimen C statistical analysis plan versions and prospective statistical specifications. |
| DOC-004 | joi240158supp3_prod_1742927563.7911.pdf | PDF | PDF_PAGE | 26 | REPORT | p.1 contents lists eMethods, efficacy eTables 1–4, adverse-event eTable 5, serum neurofilament eFigure; results supplement. |
| DOC-005 | joi240158supp4_prod_1742927563.8061.pdf | PDF | PDF_PAGE | 6 | REPORT | p.1 Supplemental Online Content: Nonauthor Collaborators; roster of personnel, institutions and roles, non-plan administrative report material. |
| DOC-006 | joi240158supp5_prod_1742927563.8111.pdf | PDF | PDF_PAGE | 1 | REPORT | p.1 Data Sharing Statement; retrospective report/data availability material, no prospective statistical plan. |

Stable page counts were directly confirmed by six `python3 workflow_1_6_2/scripts/pdf_tools.py info` calls using the available system PyMuPDF fallback while installation proceeded. This generated no derivative. Exact hashes are in source_hashes_before.sha256. The PDF metadata is unencrypted for every source.

## Disjoint canonical mapping inputs

All paths below are package-relative. Each native shard uses form-feed boundaries: segment1 is its first listed PDF page. Individual page text/image paths use the PDF page in their filename. A mapper must include complementary images/OCR named in evidence_asset_inventory.md where the native text does not transcribe image content.

| Scope | Canonical legacy path | Text characters | Fresh-required units in scope |
|---|---|---:|---|
| DOC-001 pp.1–12 | .ai_paper_validation/document_outputs/DOC-001/preprocessing/normalized_text.txt | 125685 | None |
| DOC-002 pp.1–76 | .ai_paper_validation/review_1_5_3/preprocessing/support-001/doc002_p001_p076_native.txt | 158125 | None |
| DOC-002 pp.77–152 | .ai_paper_validation/review_1_5_3/preprocessing/support-002/doc002_p077_p152_native.txt | 130719 | pp.108,121,137,138 |
| DOC-002 pp.153–229 | .ai_paper_validation/review_1_5_3/preprocessing/support-003/doc002_p153_p229_native.txt | 121377 | p.187 |
| DOC-003 pp.1–65 | .ai_paper_validation/review_1_5_3/preprocessing/support-004/doc003_p001_p065_native.txt | 167357 | pp.54,55,58,59,60 |
| DOC-003 pp.66–130 | .ai_paper_validation/review_1_5_3/preprocessing/support-005/doc003_p066_p130_native.txt | 185339 | None |
| DOC-004 pp.1–25 | .ai_paper_validation/document_outputs/DOC-004/preprocessing/normalized_text.txt | 63178 | None |
| DOC-004 p.26 | .ai_paper_validation/document_outputs/DOC-004/preprocessing/native_pages/page-26.txt | 433 | None |
| DOC-005 pp.1–6 | .ai_paper_validation/review_1_5_3/preprocessing/support-006/doc005_native_p001_p006.txt | 16713 | None |
| DOC-006 p.1 | .ai_paper_validation/review_1_5_3/preprocessing/support-006/doc006_native_p001.txt | 1029 | None |

Character counts use `wc -m` before normalization and are conservative shard-planning counts. Native-only shards all fit the 200000-character bound. DOC-003 pp.66–130 layout is 206056 characters and must not be consumed whole alongside the native source in one bounded shard. The corpus requires seven disjoint mapping scopes: main, three protocol, two SAP, and one results/administrative supplement scope. The ten fresh-assigned pages received direct visual confirmation and rendering, with no new OCR needed. Page137 retained its conservative fresh assignment after native coverage was confirmed; no double count is introduced. No source page is omitted because it is historical, background, administrative, sparse, or rights content.
