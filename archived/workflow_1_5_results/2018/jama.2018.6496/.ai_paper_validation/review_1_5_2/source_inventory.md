# Fresh Direct-Source Inventory

Prepared from the three direct PDF sources only. No previous audit derivative or final report was consulted.

| Source ID | Package-relative source path | Type | Size (bytes) | SHA-256 | Likely role | Stable units | Fresh preparation method | Result-relevant scope |
|---|---|---|---:|---|---|---|---|---|
| DOC-001 | jama_driver_2018_oi_180054.pdf | PDF | 421488 | 684db2edf58f16d1d24e8ddb6a463429b027450314c923e06700acdd0167e7d2 | Main randomized clinical-trial article | 11 PDF pages | `pdfinfo`; `pdftotext`; `pdftotext -layout`; targeted PNG rendering | Article pages 1-10: abstract, methods, participant flow, tables, results, figures/captions, and discussion quantitative statements. Page 11 is references and was freshly text-mapped for completeness. |
| DOC-002 | joi180054supp1_prod.pdf | PDF | 690636 | 38c1822278c238d2e9f217cd626c307b9d7ad8152f93f3281a03f58990e6108c | Supporting clinical-trial protocol | 25 PDF pages | `pdfinfo`; `pdftotext`; `pdftotext -layout`; targeted PNG rendering | Protocol pages 5-22: outcome definitions, design, population, procedures, planned statistical methods, interim analysis, and monitoring. Pages 1-4 and 23-25 were freshly text-mapped as title/contents/definitions/references context. |
| DOC-003 | joi180054supp2_prod.pdf | PDF | 741158 | b8b7e9731b69407ff10ffc262eb42477965333e3697461e848d8fe50e13b4b31 | Supporting results, interim analysis, figures, and data form | 13 PDF pages | `pdfinfo`; `pdftotext`; `pdftotext -layout`; targeted PNG rendering | Pages 1-6: clustered analysis table, figure descriptions, and interim analysis. Pages 7-13: postintubation data-form labels and outcome/complication fields. |

## Inventory boundaries

- Direct-source count: 3 PDFs; no DOC, DOCX, XLS, XLSX, or CSV source is present in this package.
- Total stable source units: 49 PDF pages (11 + 25 + 13).
- Every unit was newly prepared; reusable units are zero.
- The PDF metadata reports no encryption for all three documents. DOC-001 is untagged; DOC-002 and DOC-003 are tagged. These metadata facts did not prevent usable native/layout text extraction.
