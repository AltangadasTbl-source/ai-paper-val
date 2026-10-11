# Coordinator-Authorized PyMuPDF Extraction Fallback

## Deviation and boundary

The workflow-preferred Poppler commands were unavailable (`pdfinfo`, `pdftotext`, `pdftoppm`, and `pdftocairo` were not found in `PATH`). The coordinator therefore authorized a bounded local fallback solely for direct PDF text extraction. This fallback is a workflow deviation: PyMuPDF CLI `gettext` was used in place of `pdftotext` and `pdftotext -layout`.

It is not OCR. No OCR command, GPU command, network request, external data source, installation, or handwritten Python was invoked. Existing DOC-002 OCR assets were not replaced.

## Tool provenance

- Executable: `/home/juliz/venvs/stt/bin/pymupdf`
- Package: `pymupdf` version `1.28.0`
- Package location: `/home/juliz/venvs/stt/lib/python3.12/site-packages`
- CLI capability inspected: `pymupdf gettext --help`; available modes include `simple` and `layout`.

## Exact commands

```text
/home/juliz/venvs/stt/bin/pymupdf gettext -mode simple -output .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_simple_text/DOC-001_jama_jabre_2018_oi_180004.txt jama_jabre_2018_oi_180004.pdf
/home/juliz/venvs/stt/bin/pymupdf gettext -mode layout -output .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt jama_jabre_2018_oi_180004.pdf
/home/juliz/venvs/stt/bin/pymupdf gettext -mode simple -output .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_simple_text/DOC-002_joi180004supp1_prod.txt joi180004supp1_prod.pdf
/home/juliz/venvs/stt/bin/pymupdf gettext -mode layout -output .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_layout_text/DOC-002_joi180004supp1_prod.txt joi180004supp1_prod.pdf
/home/juliz/venvs/stt/bin/pymupdf gettext -mode simple -output .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_simple_text/DOC-003_joi180004supp2_prod.txt joi180004supp2_prod.pdf
/home/juliz/venvs/stt/bin/pymupdf gettext -mode layout -output .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_layout_text/DOC-003_joi180004supp2_prod.txt joi180004supp2_prod.pdf
```

## Output integrity and page coverage

Each `gettext` output uses a form-feed page delimiter. The form-feed counts match the complete stable PDF page-unit counts.

| Source | Mode | Output path | Bytes | SHA-256 | Form feeds / expected pages | Nonempty page segments | Empty page segments |
|---|---|---|---:|---|---|---:|---|
| DOC-001 | simple | `preprocessing/pymupdf_simple_text/DOC-001_jama_jabre_2018_oi_180004.txt` | 52806 | `0aebb98460e1745f77f80fd9a46d285bdb8e7346d1b081b4dbc1b715db2be45d` | 9 / 9 | 9 | None |
| DOC-001 | layout | `preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt` | 127202 | `bdb30e03c2c30d367c97cf2ebf029f5d182584555b56cfd5c56a439d4fb92f52` | 9 / 9 | 9 | None |
| DOC-002 | simple | `preprocessing/pymupdf_simple_text/DOC-002_joi180004supp1_prod.txt` | 289079 | `c5c558d1faf2a20ee0e80baf46f825157b4a3421cce10998b429175da5f1503a` | 134 / 134 | 123 | 108, 109, 126-134 |
| DOC-002 | layout | `preprocessing/pymupdf_layout_text/DOC-002_joi180004supp1_prod.txt` | 422328 | `f248fff0ee3c85d24567f85cd47dde301aff80e12dfa5c1510ea89557e0df247` | 134 / 134 | 123 | 108, 109, 126-134 |
| DOC-003 | simple | `preprocessing/pymupdf_simple_text/DOC-003_joi180004supp2_prod.txt` | 2827 | `26c981db1b8a973dbc7684433a64671febc67662b4c3964fdb0551963112c74c` | 3 / 3 | 3 | None |
| DOC-003 | layout | `preprocessing/pymupdf_layout_text/DOC-003_joi180004supp2_prod.txt` | 6865 | `8beb8f04d8b948c4911dfd946b0288c33ed15f789855b8ebc2695b4ae2c90bc0` | 3 / 3 | 3 | None |

For DOC-002, the source-hash-matched supplied OCR references remain supplementary evidence for pp. 52, 108, 109, and 126-133. Of the 11 empty text segments, ten have such existing OCR coverage (108-109 and 126-133); p. 134 has neither extractable text nor user-authorized OCR and must be treated as an explicitly empty/unavailable evidence unit.
