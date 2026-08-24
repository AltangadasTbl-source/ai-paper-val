# Fresh Direct-Source Inventory

Prepared as a source-first inventory for Workflow 1.5.2. Only the three direct PDFs in the package were classified. No legacy audit derivative, legacy OCR, extracted text, candidate record, or previous final report was inspected or used.

| Source ID | Package-relative path | Type | Size (bytes) | SHA-256 | Total units | Likely role | Available content / limitations |
|---|---|---|---:|---|---:|---|---|
| DOC-001 | jama_jabre_2018_oi_180004.pdf | PDF 1.4 | 382467 | 114e922542bbb1f8369ca9b5c19be65d93856e16cf4ff295c483439e4e208839 | 9 PDF pages | Main randomized clinical-trial article | Title/abstract, methods, flow chart, Tables 1-2, results, discussion, and references. Native text is present on all 9 pages. |
| DOC-002 | joi180004supp1_prod.pdf | PDF 1.7 | 3482589 | 70106d31b08e3a9d7eaac8a0e035bbf8d92a43b51f2483b634d7349b0c5f6913 | 134 PDF pages | Supplement: original/final protocols, amendments, and statistical analysis plan | Native text is present on pages 1-107 and 110-125. Pages 108-109 and 126-134 are blank in the direct PDF text stream and are result-irrelevant. Two result-relevant image/table pages (PDF pp. 52 and 103) required targeted OCR. |
| DOC-003 | joi180004supp2_prod.pdf | PDF 1.5 | 87908 | 937e18794fc87074907b1e9ab792f9a35d2f2d895d586dd27e7cbf44d5ed8d46 | 3 PDF pages | Supplementary result tables | Cover/description plus eTable 1 (centre contributions) and eTable 2 (post-hoc analyses). Native text is present on all 3 pages. |

## Classification and scope

- Direct-source inventory count: 3 files, all PDFs; no DOC, DOCX, XLS, XLSX, or CSV direct sources are present.
- Stable IDs are assigned in package filename order supplied to this review: DOC-001 through DOC-003.
- PDF page counts were established directly with `pdfinfo`; PDFs are unencrypted. File type was independently confirmed with `file`.
- The SHA-256 values above are also the values supplied to the coordinator for the required `source_hashes_before.sha256` artifact.
