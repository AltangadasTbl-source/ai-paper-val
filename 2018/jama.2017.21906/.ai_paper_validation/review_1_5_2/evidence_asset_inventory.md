# Fresh Evidence-Asset Inventory

## Tools and execution record

All commands operated on the four direct package PDFs only. Tool versions were: `pdfinfo 26.01.0`, `pdftotext 26.01.0`, `pdftoppm 26.01.0`, and `tesseract 5.5.0`. Tesseract was inspected for availability but not invoked. No GPU was probed or used; no software was installed; no network access or Office conversion was needed.

Commands executed, with each source explicitly named:

```text
sha256sum -- <each direct PDF>
pdfinfo <each direct PDF> > preprocessing/pdfinfo/<source>.pdfinfo.txt
pdftotext <each direct PDF> preprocessing/native_text/<source>.txt
pdftotext -layout <each direct PDF> preprocessing/layout_text/<source>.txt
pdftoppm -f 1 -l 1 -singlefile -png -r 180 jama_huffman_2018_oi_170166.pdf preprocessing/rendered_pages/DOC-001-page-001
pdftoppm -f 4 -l 10 -png -r 180 jama_huffman_2018_oi_170166.pdf preprocessing/rendered_pages/DOC-001
pdftoppm -f 4 -l 4 -singlefile -png -r 180 joi170166supp2_prod.pdf preprocessing/rendered_pages/DOC-003-page-004
pdftoppm -f 17 -l 27 -png -r 180 joi170166supp3_prod.pdf preprocessing/rendered_pages/DOC-004
```

## Assets by source

| Source ID | Fresh metadata asset | Fresh native-text asset | Fresh layout-text asset | Result-relevant rendered pages | Text adequacy and limitation |
|---|---|---|---|---|---|
| DOC-001 | `preprocessing/pdfinfo/jama_huffman_2018_oi_170166.pdfinfo.txt` | `preprocessing/native_text/jama_huffman_2018_oi_170166.txt` (68831 bytes) | `preprocessing/layout_text/jama_huffman_2018_oi_170166.txt` (132071 bytes) | pp. 1, 4-10: `preprocessing/rendered_pages/DOC-001-page-001.png`, `DOC-001-04.png` through `DOC-001-10.png` | Usable native/layout text for all 12 pages. Renders cover abstract, flow diagram, Tables 1-3, Figures 2-3, and adjacent results narrative. |
| DOC-002 | `preprocessing/pdfinfo/joi170166supp1_prod.pdfinfo.txt` | `preprocessing/native_text/joi170166supp1_prod.txt` (60342 bytes) | `preprocessing/layout_text/joi170166supp1_prod.txt` (76543 bytes) | None required | Usable native/layout text for all 32 pages, including protocol outcomes, intervention, monitoring, and data-capture sections. No result table/figure had unusable text requiring a render. |
| DOC-003 | `preprocessing/pdfinfo/joi170166supp2_prod.pdfinfo.txt` | `preprocessing/native_text/joi170166supp2_prod.txt` (20618 bytes) | `preprocessing/layout_text/joi170166supp2_prod.txt` (24223 bytes) | p. 4: `preprocessing/rendered_pages/DOC-003-page-004.png` | Usable native/layout text for all 9 pages. The sample-size display was additionally rendered for visual confirmation. |
| DOC-004 | `preprocessing/pdfinfo/joi170166supp3_prod.pdfinfo.txt` | `preprocessing/native_text/joi170166supp3_prod.txt` (19903 bytes) | `preprocessing/layout_text/joi170166supp3_prod.txt` (25936 bytes) | pp. 17-27: `preprocessing/rendered_pages/DOC-004-17.png` through `DOC-004-27.png` | Fresh native/layout text is usable for pp. 1-2 and 17-27. On pp. 3-16 it is only a repeated copyright line and does not expose visible toolkit content. |

## Supplied OCR fallback: DOC-004 pp. 3-16

The user specifically directed reuse of the existing OCR to avoid another OCR pass. For each of these 14 pages, the supplied OCR manifest identifies `joi170166supp3_prod.pdf`, the current SHA-256 `511f4a907e4c48d920f1c6b89d444fe76c7c91e11bbae84cdee834fa0393f3ec`, and the same PDF page. Therefore it may be consulted only as source-matched page-level text fallback after the fresh direct extraction failed. The fallback files are:

```text
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_003.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_004.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_005.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_006.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_007.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_008.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_009.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_010.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_011.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_012.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_013.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_014.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_015.txt
.ai_paper_validation/preprocessing/joi170166supp3_prod/ocr_pages/page_016.txt
```

No new OCR was run. The supplied fallback is not an audit finding, candidate set, extraction decision, or discovery boundary. Its historical metadata reports a non-CPU backend, but that backend was not invoked in this run. If a later reviewer needs a visual confirmation for any fallback item, the direct PDF page remains the evidence location and the source-matched supplied image may be inspected; no rerun is required by this preparation stage.

## Limitations

- PDF `file` output labels DOC-001 as a 10-page document even though direct `pdfinfo` reports 12 pages; this inventory uses `pdfinfo` and the 12 form-feed-separated text units, which agree.
- DOC-004 pp. 3-16 have no usable fresh text layer. The matched supplied OCR provides text fallback, but OCR should be checked against the direct PDF image before relying on exact typography or a close numeric distinction.
- All 80 direct-source pages have fresh native and layout extraction assets. No source was modified.
