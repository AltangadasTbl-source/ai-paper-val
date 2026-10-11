# Direct Source Inventory

Prepared fresh for Workflow 1.5.2. Direct sources were identified only from the package root. No prior audit extraction, candidate, or review decision was used as evidence.

| Source ID | Package-relative source path | Type | Size (bytes) | SHA-256 | Stable units | Likely role | Direct-source availability and extraction status |
|---|---|---|---:|---|---|---|---|
| DOC-001 | jama_jabre_2018_oi_180004.pdf | PDF 1.4 | 382467 | 114e922542bbb1f8369ca9b5c19be65d93856e16cf4ff295c483439e4e208839 | 9 PDF pages | Main article (identified from the `jama_` article filename) | `file` confirmed PDF 1.4 and 9 pages. A coordinator-authorized PyMuPDF fallback produced simple and layout text with 9 form-feed-delimited, nonempty page segments in each output. No OCR was run. |
| DOC-002 | joi180004supp1_prod.pdf | PDF 1.7 | 3482589 | 70106d31b08e3a9d7eaac8a0e035bbf8d92a43b51f2483b634d7349b0c5f6913 | 134 PDF pages | Supplement 1 / supporting results material (identified from filename) | A coordinator-authorized PyMuPDF fallback produced simple and layout text with 134 form-feed-delimited page segments. Both have no extractable text on pp. 108-109 and 126-134. Existing source-hash-matched OCR supplements pp. 108-109 and 126-133; page 134 remains an empty direct-text segment. No OCR was run. |
| DOC-003 | joi180004supp2_prod.pdf | PDF 1.5 | 87908 | 937e18794fc87074907b1e9ab792f9a35d2f2d895d586dd27e7cbf44d5ed8d46 | 3 PDF pages | Supplement 2 / supporting material (identified from filename) | Page count supplied for this run is 3. A coordinator-authorized PyMuPDF fallback produced simple and layout text with 3 form-feed-delimited, nonempty page segments in each output. No OCR was run. |

## Inventory method and boundaries

- Direct source discovery: package-root PDF enumeration; no DOC, DOCX, XLS, XLSX, or CSV direct source was present.
- Identity and type: `sha256sum`, `stat`, and `file` run locally on the three direct PDFs.
- Tool availability checked locally: `pdfinfo`, `pdftotext`, `pdftoppm`, and `pdftocairo` were not found in `PATH`; their prescribed direct extraction/rendering commands could not be executed.
- Coordinator-authorized deviation: local `/home/juliz/venvs/stt/bin/pymupdf gettext` (PyMuPDF 1.28.0) was used in `simple` and `layout` modes as a bounded extraction fallback. This is text extraction, not OCR. Exact commands, checksums, page delimiters, and the one empty un-OCRed page are recorded in `preprocessing/pymupdf_extraction_log.md`.
- The supplied OCR assets for DOC-002 are an explicit user-authorized exception to the no-legacy-derivative evidence boundary. Their source SHA-256 matches DOC-002 exactly. They are referenced, rather than treated as a general reusable extraction or a prior audit conclusion.
- Direct source unit total: 146 PDF pages (9 + 134 + 3). No sheet, workbook, CSV row, Office paragraph, or Office table unit exists in this package.
