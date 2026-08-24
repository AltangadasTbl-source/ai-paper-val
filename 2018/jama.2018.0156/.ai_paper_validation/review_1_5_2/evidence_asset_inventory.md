# Evidence Asset Inventory

This inventory records only artifacts prepared or explicitly authorized for this fresh Workflow 1.5.2 preprocessing stage. It does not adopt prior audit conclusions.

| Asset group | Source and exact units | Method | Fresh artifact or permitted reference | Result and limitation |
|---|---|---|---|---|
| Source identity metadata | DOC-001 pp. 1-9; DOC-002 pp. 1-134; DOC-003 pp. 1-3 | Local `sha256sum`, `stat`, and `file` | `source_inventory.md`; `source_hashes_before.sha256` | Complete source identity, type, size, and stable page-unit inventory. |
| Simple PDF text | All 146 PDF pages | Coordinator-authorized `/home/juliz/venvs/stt/bin/pymupdf gettext -mode simple` fallback | `preprocessing/pymupdf_simple_text/DOC-001_jama_jabre_2018_oi_180004.txt`; `preprocessing/pymupdf_simple_text/DOC-002_joi180004supp1_prod.txt`; `preprocessing/pymupdf_simple_text/DOC-003_joi180004supp2_prod.txt` | Complete page-delimiter coverage: 9 + 134 + 3 form feeds. DOC-002 pp. 108-109 and 126-134 have no extractable text. |
| Layout-preserving PDF text | All 146 PDF pages | Coordinator-authorized `/home/juliz/venvs/stt/bin/pymupdf gettext -mode layout` fallback | `preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt`; `preprocessing/pymupdf_layout_text/DOC-002_joi180004supp1_prod.txt`; `preprocessing/pymupdf_layout_text/DOC-003_joi180004supp2_prod.txt` | Complete page-delimiter coverage: 9 + 134 + 3 form feeds. DOC-002 pp. 108-109 and 126-134 have no extractable text. |
| PDF metadata | DOC-001 pp. 1-9; DOC-002 pp. 1-134; DOC-003 pp. 1-3 | Required direct `pdfinfo` | None | Blocked: `pdfinfo` not installed or available in `PATH`. Page counts used here are 9 and 3 as supplied for this run and 134 from the hash-matched OCR manifest for DOC-002. |
| Fresh result-page rendering | All 146 PDF pages | Required direct `pdftoppm` or `pdftocairo` | None | Blocked: both renderers are absent from `PATH`. The successful text-extraction fallback does not provide visual table/figure rendering. |
| Authorized supplied OCR text and images | DOC-002 pp. 52, 108, 109, 126, 127, 128, 129, 130, 131, 132, 133 | Reuse only under explicit user override; no engine invoked in this run | `preprocessing/reused_ocr/DOC-002_authorized_ocr_provenance.md` | Complete source-hash-matched reference inventory for 11 pages. Text and page-image paths resolve to the supplied artifacts outside this fresh directory. |
| New OCR | All PDF pages | CPU Tesseract would normally apply only after unusable native/layout text | None | Explicitly prohibited by user override. No CPU or GPU OCR was probed or run. |

## Tool record

- Commands successfully used: `sha256sum`, `stat`, `file`, and coordinator-authorized `/home/juliz/venvs/stt/bin/pymupdf gettext` (PyMuPDF 1.28.0).
- Tools unavailable: `pdfinfo`, `pdftotext`, `pdftoppm`, `pdftocairo`.
- OCR handling: no OCR command was run. The supplied DOC-002 OCR manifest reports `rapidocr-cuda`, but that is historical provenance only; it was not invoked, validated as an engine choice, or generalized to any other page.
- Office conversion and the optional Office structure extractor were not applicable: there are no direct Office sources.

## Coverage implication

All 146 page units now have fresh simple and layout extraction delimiters. DOC-002 has 11 empty direct-text page segments: pp. 108-109 and 126-134. The explicitly authorized source-hash-matched OCR supplies text-plus-image evidence for ten of those pages (pp. 108-109 and 126-133); p. 134 remains empty in both fresh text outputs and has no user-authorized OCR. This is recorded as a source-page limitation, not a scientific conclusion.
