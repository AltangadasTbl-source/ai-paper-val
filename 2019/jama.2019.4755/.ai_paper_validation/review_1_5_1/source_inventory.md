# Direct Source Inventory

## Scope and method

This inventory covers every direct PDF, DOC, DOCX, XLS, XLSX, and CSV source in this paper package. No DOC, DOCX, XLS, XLSX, or CSV direct source was present. Existing candidate, checker, verifier, critic, endetail, queue, and final-report content was excluded from discovery scope.

Commands used were `rg --files -g '*.{pdf,PDF,doc,DOC,docx,DOCX,xls,XLS,xlsx,XLSX,csv,CSV}' -g '!workflow_1_5_1/**' -g '!**/.git/**'`, `sha256sum -- <each exact PDF path>`, and `pdfinfo -- <each exact PDF path>`. Tool versions recorded during this inventory were Poppler `pdfinfo version 26.01.0`, Poppler `pdftotext version 26.01.0`, and `tesseract 5.5.0`.

| Source ID | Package-relative path | Type | Stable units | SHA-256 | PDF identity | Existing document record |
|---|---|---|---:|---|---|---|
| DOC-001 | jama_brenner_2019_oi_190039.pdf | PDF | 7 PDF pages | 799606a7244357dc9942c50cf7782001d00bfbd6fcdc821ccad1aeca67fae328 | PDF 1.4; letter; creator XPP; producer iTextSharp.LGPLv2.Core 3.7.4.0 | `.ai_paper_validation/document_outputs/doc-799606a72443/document_record.json` |
| DOC-002 | joi190039supp1_prod.pdf | PDF | 62 PDF pages | 5143f7e4da1ae6c98ec6233a3dee86053082e1fb85e4b5a6b70d2f4e74f4a14b | PDF 1.5; letter; creator PDF24 Creator; producer Acrobat Distiller 10.1.16 | `.ai_paper_validation/document_outputs/doc-5143f7e4da1a/document_record.json` |
| DOC-003 | joi190039supp2_prod.pdf | PDF | 10 PDF pages | 5704a644014e515ba117d6f77ba50b0f0fe6d9633442bf5c967d77192029ce81 | PDF 1.3; letter; creator Microsoft Word 2013; producer Acrobat Distiller 10.1.9 | `.ai_paper_validation/document_outputs/doc-5704a644014e/document_record.json` |
| DOC-004 | joi190039supp3_prod.pdf | PDF | 8 PDF pages | b45e07a04d8267f58d72e1809f785a46f932101412f35ef3448689e2638c0e0d | PDF 1.7; A4; creator and producer Microsoft Word 2016 | `.ai_paper_validation/document_outputs/doc-b45e07a04d82/document_record.json` |
| DOC-005 | joi190039supp4_prod.pdf | PDF | 1 PDF page | ded78f53da7bbb5e05d0afb3070dbccaac6c35cd7a0087309dd23442bfb17f5a | PDF 1.7; letter; creator and producer Microsoft Word 2016 | `.ai_paper_validation/document_outputs/doc-ded78f53da7b/document_record.json` |

**Direct-source totals:** 5 sources; 88 unique PDF-page units; 0 Office or CSV units.

## Source-location and extraction gaps

- DOC-001 has current usable native/layout text and page-location support for PDF pages 1-7.
- DOC-004 has current usable native/layout text and page-location support only for PDF pages 4-8. PDF pages 1-3 require fresh direct-source mapping.
- DOC-002, DOC-003, and DOC-005 have identity-level document records only; all their PDF pages require fresh direct-source extraction and mapping.
- There are no existing table/workbook extraction assets and no direct Office/workbook/CSV source to inventory.
