# Direct-source inventory

All supplied source formats were searched inside this paper package, including hidden paths; supplied direct evidence comprises seven PDFs. There are no direct DOC, DOCX, XLS, XLSX, or CSV sources. Legacy page-manifest CSVs are derivatives. No source or legacy artifact was modified. Unit counts come from direct `pdfinfo` (Poppler 26.01.0); hashes use direct `sha256sum` with package-relative paths.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content-based identity and exact inventory location |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_sarraj_2024_oi_240006_1708623114.96234.pdf | PDF | PDF_PAGE | 14 | REPORT | Main original investigation; p. 1 title/abstract identifies ischemic injury and penumbra SELECT2 analysis. Complete scope pp. 1-14. |
| DOC-002 | joi240006supp1_prod_1708623114.97236.pdf | PDF | PDF_PAGE | 30 | REPORT | Nonauthor collaborator list, p. 1 heading. Administrative non-plan supplement; pp. 1-30 mapped for result relevance. |
| DOC-003 | joi240006supp2_prod_1708623114.99233.pdf | PDF | PDF_PAGE | 82 | PLAN | SELECT2 protocol, p. 1 protocol title/date, p. 2 agreement; entire protocol bundle pp. 1-82. |
| DOC-004 | joi240006supp3_prod_1708623114.99733.pdf | PDF | PDF_PAGE | 40 | PLAN | Scanned trial Statistical Analysis Protocol; reusable p. 2 image shows SELECT2 Statistical Analysis Plan V1.0.0, Nov. 20, 2022. Complete pp. 1-40. |
| DOC-005 | joi240006supp4_prod_1708623115.00733.pdf | PDF | PDF_PAGE | 7 | PLAN | Analysis-specific Statistical Analysis Protocol; p. 2 identifies a prespecified secondary analysis, version 1.0.0 dated July 7, 2023. Complete pp. 1-7. |
| DOC-006 | joi240006supp5_prod_1708623115.01733.pdf | PDF | PDF_PAGE | 53 | REPORT | Results supplement; p. 1 identifies eMethods, eFigures 1-20, eTables 1-13. Complete pp. 1-53. |
| DOC-007 | joi240006supp6_prod_1708623115.02733.pdf | PDF | PDF_PAGE | 1 | REPORT | Data-sharing statement p. 1; administrative non-plan material. |

Total: 227 PDF pages. No content-based mixed REPORT/PLAN bundle was identified at inventory; mappers must retain any prospective versus reported content distinctions in exact-location records. Administrative material remains included, despite legacy restricted audit scopes. Old scope statements in document records are metadata only and do not constrain this run.

## Source identity and reusable fitness checks

Commands: `pdfinfo "source.pdf"`; `pdftotext -f 1 -l 2 "source.pdf" -`; `cmp -s <(pdftotext -layout "source.pdf" -) "legacy-layout.txt"`; `sha256sum -- "source.pdf"`.

Direct whole-source layout extraction exactly matches reusable layout for DOC-001, DOC-002, DOC-003, DOC-005, and DOC-007. All 40 scanned DOC-004 pages have corresponding reusable images and OCR; inventory visually inspected p. 2 to establish plan content. DOC-006 has 53 page-specific native files and rendered pp. 5-53; complete native text plus images cover all unique pages. Sparse/partial native pages are explicitly identified in the asset inventory and require visual source interpretation during mapping, without requiring repeated rendering or OCR.

## Downstream assignments and context bounds

Main mapping: DOC-001 pp. 1-14. Support union: DOC-002 pp. 1-30; DOC-003 pp. 1-82; DOC-004 pp. 1-40; DOC-005 pp. 1-7; DOC-006 pp. 1-53; DOC-007 p. 1. Every unit is reusable-backed; no extraction gap exists, and every unit still requires fresh scientific mapping.

Bounded recommended support scopes: protocol DOC-003 pp. 1-82 (180,289 characters); analysis plan plus results DOC-005 pp. 1-7 and DOC-006 pp. 1-53 (120,340 native/OCR characters); administrative material plus trial SAP DOC-002 pp. 1-30, DOC-004 pp. 1-40, DOC-007 p. 1 (157,052 characters). Visual review must remain within 32 viewed images per shard: split DOC-004 pp. 1-20 / pp. 21-40 when all images are needed; split DOC-006 pp. 1-32 / pp. 33-53 when all 49 rendered pages are needed. These recommendations constrain context only, never scientific coverage.

## Completed mapping update

Every direct-source unit is mapped. Protocol pages 13, 18, 21, 71, 78, 80 and 81 contained graphics/formulas not fully exposed by reusable text and were directly rendered and read by the protocol mapper. The final partition is 220 reusable-backed plus seven fresh-required pages, with 227 mapped pages. Initial inventory zero-fresh estimates above are superseded by this source-linked gap closure and source_coverage.md. All direct-source document roles remain as inventoried.
