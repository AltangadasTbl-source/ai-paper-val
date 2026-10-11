# Direct-source inventory

Inventory is confined to this paper package. Three supplied direct sources are present, all PDFs; no supplied DOC, DOCX, XLS, XLSX, or CSV source is present. Stable units are physical PDF pages, including contents, references, code tables, protocol text, and amendments. PDF metadata and page counts were read with Poppler pdfinfo 26.01.0. Every source has a usable native text layer. SHA-256 hashes match legacy document identity records and are recorded separately.

| Source ID | Source path | Format | Total units | Document role | Content basis and complete mapping scope |
|---|---|---|---:|---|---|
| DOC-001 | jama_aminian_2019_oi_190103.pdf | PDF | 12 | REPORT | Main article, Association of Metabolic Surgery With Major Adverse Cardiovascular Outcomes in Patients With Type 2 Diabetes and Obesity. Physical PDF pp. 1-12 correspond to printed JAMA pp. 1271-1282. Retrospective matched-cohort report; full mapping assigned to main mapper. |
| DOC-002 | joi190103supp1_prod.pdf | PDF | 20 | REPORT | Results supplement. Physical PDF p. 1 contents; pp. 2-5 diagnosis/procedure and medication definitions; pp. 6-20 event rates, cumulative incidence, Cox-model results, longitudinal summaries, observation counts, and sensitivity analyses. Full mapping assigned to support mapper. |
| DOC-003 | joi190103supp2_prod.pdf | PDF | 7 | PLAN | Physical PDF p. 1 contents, pp. 2-6 original study protocol dated January 6, 2019, and p. 7 protocol amendment dated August 2, 2019. The amendment states that additions address journal peer-review comments; both documents are plan specifications in one bound plan bundle. Full mapping assigned to support mapper. |

The supplement roles follow their content. No source mixes REPORT and PLAN material. The supplied study is observational; the workflow applies the supplied quantitative scope without converting it to a randomized-trial design.

## Inventory tools and integrity

Commands: `pdfinfo SOURCE.pdf`; `sha256sum -- SOURCE.pdf`; `pdftotext -f 1 -l 2 SOURCE.pdf -`. All use direct local tools. Every PDF page has a source-matched reusable text artifact. Existing records that previously excluded definitions or protocol pages do not restrict this review. Direct sources and existing audit artifacts remain unchanged.

Support mapping confirms the amendment's printed date as August 2, 2019 on DOC-003 p. 7; the inventory date was updated to match that transcription. Roles and unit counts are unchanged.
