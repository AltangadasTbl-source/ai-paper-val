# Direct Source Inventory

Scope: the current package only. Recursive extension inventory found five supplied PDFs and no supplied DOC, DOCX, XLS, XLSX, or CSV files. Existing audit derivatives are inventoried separately and never treated as direct sources. PDF page counts use direct Poppler pdfinfo 25.03.0. Direct SHA-256 values and exact package-relative paths are recorded in source_hashes_before.sha256 using sha256sum.

| Source ID | Source path | Format | Document role by content | Complete units | Exact unit scope | Role basis and bundle assessment | Downstream mapper artifact |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_simonis_2018_oi_180108.pdf | PDF | REPORT | 9 | PDF pages 1-9 | Main randomized-trial article reporting methods, results, tables, figures, and references; no bound prospective plan | extraction/main_quantitative_evidence.md |
| DOC-002 | joi180108supp1_prod.pdf | PDF | PLAN | 49 | PDF pages 1-49 | Trial protocol version 3.2, prospective procedures, statistical sections, and appendices; no bound results report | extraction/support_quantitative_evidence.md |
| DOC-003 | joi180108supp2_prod.pdf | PDF | PLAN | 22 | PDF pages 1-22 | Study update and detailed statistical analysis plan version 1.0, dated November 24, 2017, with plan modifications and table shells; operational updates do not make it a results report | extraction/support_quantitative_evidence.md |
| DOC-004 | joi180108supp3_prod.pdf | PDF | REPORT | 13 | PDF pages 1-13 | Non-plan results supplement containing eMethods, eReferences, eTables 1-5, and eFigures 1-4; eMethods describe reported study procedures | extraction/support_quantitative_evidence.md |
| DOC-005 | joi180108supp4_prod.pdf | PDF | REPORT | 1 | PDF page 1 | Retrospective data-sharing statement accompanying the published report; no prospective analysis plan | extraction/support_quantitative_evidence.md |

No supplied bundle contains both REPORT and PLAN sections requiring split document-role assignment. Covers and references retain the enclosing content role. These assignments concern document content, not supplement numbering or filenames.

The complete stable unit count is 94 PDF pages. DOC-001 belongs to the main mapper; DOC-002 through DOC-005 belong to the support mapper. DOC-002 pages 12, 13, 14, 36, 39, 40, 41, 42 require fresh visual extraction; all other pages have reusable text or rendered-page support. Every page still requires a new scientific evidence map.

## Text size and context planning

Character counts below measure each source-matched native text with wc -m under the current UTF-8 locale. The normalized count removes whitespace with POSIX tr and counts remaining characters; it is a planning proxy, not an extraction transformation. Original derivatives remain unchanged.

| Source ID | Native characters | Normalized non-whitespace characters | Native text artifact |
|---|---:|---:|---|
| DOC-001 | 49907 | 41996 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/jama_simonis_2018_oi_180108.txt |
| DOC-002 | 81350 | 69346 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180108supp1_prod.txt |
| DOC-003 | 28212 | 23982 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180108supp2_prod.txt |
| DOC-004 | 22088 | 17233 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180108supp3_prod.txt |
| DOC-005 | 505 | 431 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180108supp4_prod.txt |

Native extraction was compared byte-for-byte against pdftotext SOURCE.pdf - using cmp; all five native files match current source extraction. Page-boundary inventory uses awk with the form-feed record separator; each count equals pdfinfo. Raster gaps use direct pdfimages -list and exact rendered-page filename inventory. No Python or fallback extraction was used by the curator.

## Direct-source SHA-256

| Source path | SHA-256 |
|---|---|
| jama_simonis_2018_oi_180108.pdf | aa0fdc5835724bd9c4fdcecf14eb7cef28a955428db34ad5cba8f644076148d9 |
| joi180108supp1_prod.pdf | a9dc5bb5421c410977a7317fa74d137b700f116d6f8a495e2a98e0c22fff949f |
| joi180108supp2_prod.pdf | 9aa3d6bf69706a5e25e5727cb0cfec6a32bda8299fa8bb3fde14e4755e782ec2 |
| joi180108supp3_prod.pdf | 31eaf84d5b839a38ccc04f4d577fe15d5521ce470f128c8c70ddb1825834d83b |
| joi180108supp4_prod.pdf | d158abc51ba2a5bf4499bfcec8201ce35e60752c1aa464befcadd3c6045e74be |
