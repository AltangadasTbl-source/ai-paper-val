# Fresh Evidence-Asset Inventory

## Tools and run boundary

- Fresh direct-source preparation used Poppler 24.02.0 from `/tmp/qc15-poppler/usr/bin` with `LD_LIBRARY_PATH=/tmp/qc15-poppler/usr/lib/x86_64-linux-gnu`.
- Fresh commands: `pdfinfo`, `pdftotext`, `pdftotext -layout`, and targeted `pdftoppm -png -r 150`. No network, installation, Office conversion, Python helper, GPU probe, GPU invocation, or new OCR was performed.
- `pdfinfo`, `pdftotext`, and `pdftoppm` each reported version 24.02.0. `file` confirmed every fresh rendered derivative is a PNG image.
- Native and layout text are fresh evidence derivatives for every direct PDF page. They are not reusable source units; direct-source reusable-unit count remains zero.

## PDF metadata and text derivatives

| Source ID | Fresh metadata asset | Native-text asset | Layout-text asset | Exact command pattern | Text usability and limitations |
|---|---|---|---|---|---|
| DOC-001 | `preprocessing/pdfinfo/jama_huffman_2018_oi_170166.txt` | `preprocessing/native_text/jama_huffman_2018_oi_170166.txt` (68,831 bytes) | `preprocessing/layout_text/jama_huffman_2018_oi_170166.txt` (132,249 bytes) | `pdfinfo "jama_huffman_2018_oi_170166.pdf"`; `pdftotext SOURCE OUTPUT`; `pdftotext -layout SOURCE OUTPUT` | Native/layout text is usable on pp. 1-12. Layout text preserves the principal table alignment better than native text; visual flow and figure elements require rendered-page confirmation. |
| DOC-002 | `preprocessing/pdfinfo/joi170166supp1_prod.txt` | `preprocessing/native_text/joi170166supp1_prod.txt` (60,342 bytes) | `preprocessing/layout_text/joi170166supp1_prod.txt` (76,543 bytes) | `pdfinfo "joi170166supp1_prod.pdf"`; `pdftotext SOURCE OUTPUT`; `pdftotext -layout SOURCE OUTPUT` | Native/layout text is usable on pp. 1-32. Some front-matter, form, and table-like spacing is nonsemantic; no result-relevant page had unusable text requiring rendering or OCR. |
| DOC-003 | `preprocessing/pdfinfo/joi170166supp2_prod.txt` | `preprocessing/native_text/joi170166supp2_prod.txt` (20,618 bytes) | `preprocessing/layout_text/joi170166supp2_prod.txt` (24,223 bytes) | `pdfinfo "joi170166supp2_prod.pdf"`; `pdftotext SOURCE OUTPUT`; `pdftotext -layout SOURCE OUTPUT` | Native/layout text is usable on pp. 1-9. Page 1 is a title/approval page; the remaining SAP pages are textually extractable. |
| DOC-004 | `preprocessing/pdfinfo/joi170166supp3_prod.txt` | `preprocessing/native_text/joi170166supp3_prod.txt` (19,903 bytes) | `preprocessing/layout_text/joi170166supp3_prod.txt` (25,936 bytes) | `pdfinfo "joi170166supp3_prod.pdf"`; `pdftotext SOURCE OUTPUT`; `pdftotext -layout SOURCE OUTPUT` | Native/layout text is usable on pp. 1-2 and 17-27. Pages 3-16 each yield only the copyright line in native/layout extraction and are image-only toolkit pages. Supplied hash-matched OCR is used for those exact pages; no new OCR was run. |

All command patterns above were executed with `LD_LIBRARY_PATH=/tmp/qc15-poppler/usr/lib/x86_64-linux-gnu` and exact quoted source/output paths under the package root.

## Fresh visual derivatives

| Source ID | Rendered pages | Fresh assets | Exact rendering command pattern | Purpose and limitation |
|---|---|---|---|---|
| DOC-001 | 1, 4-10 | `preprocessing/rendered_pages/jama_huffman_2018_oi_170166-page-001.png`; `...-page-004.png` through `...-page-010.png` | `pdftoppm -f N -l N -singlefile -png -r 150 "jama_huffman_2018_oi_170166.pdf" "preprocessing/rendered_pages/jama_huffman_2018_oi_170166-page-NNN"` | Visual confirmation of the abstract, participant-flow diagram, Tables 1-3, and Figures 2-3. Pages 2-3 and 11-12 had usable layout text and no result-table/figure need for rendering. |
| DOC-002 | None | None | Not applicable | All result-relevant protocol content is textually usable; no visual result table or figure required a fresh render. |
| DOC-003 | None | None | Not applicable | The complete SAP is textually usable; no visual result table or figure required a fresh render. |
| DOC-004 | 17-27 | `preprocessing/rendered_pages/joi170166supp3_prod-page-017.png` through `...-page-027.png` | `pdftoppm -f N -l N -singlefile -png -r 150 "joi170166supp3_prod.pdf" "preprocessing/rendered_pages/joi170166supp3_prod-page-NNN"` | Visual confirmation of eTables 1-7 and eFigures 1A-2B. Pages 1-2 have usable text but no reported-result display; pages 3-16 are toolkit images and are covered by the supplied OCR reuse record below. |

## Permitted supplied OCR reuse: DOC-004 pp. 3-16

The user expressly authorized reuse of the existing OCR derivatives at `.ai_paper_validation/preprocessing/joi170166supp3_prod/`. This is the sole old derivative inspected in this run, solely to verify source matching and coverage for DOC-004 image-only pages 3-16; it is not a reusable direct-source unit and did not substitute for fresh PDF native/layout extraction.

| Verification item | Result |
|---|---|
| OCR manifest | `.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_manifest.json` |
| Manifest source filename and SHA-256 | `joi170166supp3_prod.pdf`; `511f4a907e4c48d920f1c6b89d444fe76c7c91e11bbae84cdee834fa0393f3ec`, exactly matching DOC-004 and `source_hashes_before.sha256` |
| Manifest page scope | 14 completed pages: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 |
| Existing text files verified present | 14 files at `.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_003.txt` through `page_016.txt` |
| Current-run OCR action | None. No tesseract, other OCR engine, CPU OCR, GPU probe, or GPU invocation was run. |
| Reuse limitation | The supplied OCR manifest reports an external GPU-based OCR backend. That provenance is preserved as supplied; it was not invoked or repeated in this CPU-only workflow run. OCR text is only an aid for image-only toolkit-page reading and requires visual source confirmation if used in a later quantitative claim. |

## Complete preparation classification

All 80 direct PDF pages now have fresh PDF metadata plus fresh native and layout extraction. Result-relevant visual displays have targeted fresh renders where necessary. DOC-004 pp. 3-16 have native/layout unusability explicitly classified and a verified, user-authorized existing OCR aid. The exact page-level method, result relevance, and limitation record is `preprocessing/source_page_classification.md`. No preparation gaps block source mapping.
