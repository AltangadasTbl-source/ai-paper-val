# Workflow 1.6.2 Source Inventory

Inventory scope is the current paper package only. All direct PDF, DOC, DOCX, XLS, XLSX, and CSV sources were searched recursively, excluding generated audit derivatives and repository controls. There are three direct PDFs and no supplied Office, workbook, or CSV sources. Stable units are physical PDF pages, including covers, contents, and references.

| Source ID | Source path | Document role | Content identity and role basis | Unit type | Total units | SHA-256 |
|---|---|---|---|---|---:|---|
| DOC-001 | jama_cinciripini_2024_oi_240036_1716416465.98349.pdf | REPORT | Main JAMA Original Investigation, Smoking Cessation After Initial Treatment Failure With Varenicline or Nicotine Replacement: A Randomized Clinical Trial; direct PDF p. 1 | PDF_PAGE | 10 | f51fd5b8f20a10df81121eb8aa19f1c4defb98d04ad476ce1e60dd95c68a18d1 |
| DOC-002 | joi240036supp1_prod_1716416466.00349.pdf | PLAN | Protocol 2014-0213, August 23, 2023; prospective objectives, study design, and data analysis; direct PDF pp. 1-2 | PDF_PAGE | 45 | eb73035cb7b875a25b3c955e6f730eb7f6ef88b711b3d18f0296ee3a857ed004 |
| DOC-003 | joi240036supp2_prod_1716416466.01349.pdf | REPORT | Supplemental Online Content with eAppendices, reported secondary analyses, eFigures, and eTables; direct PDF pp. 1-3 | PDF_PAGE | 36 | 51a06c53356580e94c262ebe16a3efc634ef1130da3ad33c478f97e0eae6f566 |

No supplied bundle combines PLAN and REPORT content. DOC-003 contains sample-size and model descriptions supporting reported results; these do not establish a separate prospective plan bundle.

Direct identity engines: sha256sum; pdfinfo (Poppler); pdftotext 26.01.0 for direct pp. 1-2 identity checks. Commands used: sha256sum -- SOURCE; pdfinfo SOURCE; pdftotext -f 1 -l 2 SOURCE -. CPU; no fallback helper or Office extractor was needed.

The earlier DOC-001 and DOC-003 document-record hashes differ from the current direct hashes. Their old absolute paths also refer to a former package location. These metadata fields are stale and are not source identity authority. Every one of the 241 reusable text files was compared with fresh direct pdftotext extraction at its exact source page/range; all matched after whitespace removal, with all non-whitespace characters and order retained. Source text fitness is therefore established independently of the stale hash fields. This does not assert equality of every PDF graphic or annotation.

Legacy scope decisions and scientific conclusions were not adopted. Every source page is assigned to new mapping: DOC-001 pp. 1-10 to the main mapper; DOC-002 pp. 1-45 and DOC-003 pp. 1-36 to the support mapper. Mapping is not yet complete.

Coordinator coverage update: all 91 physical pages are now mapped. The inventory-time mapping-pending note above records the handoff state; current completed counts and statuses are in source_coverage.md and coverage_manifest.md.
