# Fresh Evidence-Asset Inventory

## Toolchain and method

All work used direct CPU-local tools on the supplied PDFs. No network access, package-source modification, GPU probe/use, OCR of already usable text, Office conversion, or legacy-audit evidence input occurred.

| Tool | Version observed | Use |
|---|---|---|
| pdfinfo | Poppler 26.01.0 | Page-count and PDF metadata extraction |
| pdftotext | 26.01.0 | Native and layout-preserving fresh text extraction |
| pdftoppm | 26.01.0 | Targeted 180-dpi PNG renderings for visual table/figure checking |
| tesseract | 5.5.0 (available, CPU mode) | Not invoked; no relevant page had unusable native/layout text |

The commands were executed from the package root with quoted source paths. Per source, the direct pattern was:

```text
pdfinfo "SOURCE.pdf" > preprocessing/metadata/SOURCE.pdfinfo.txt
pdftotext "SOURCE.pdf" "preprocessing/native_text/SOURCE.txt"
pdftotext -layout "SOURCE.pdf" "preprocessing/layout_text/SOURCE.txt"
pdftoppm -f N -l N -singlefile -png -r 180 "SOURCE.pdf" "preprocessing/rendered_pages/SOURCE-pN"
```

## Per-source assets and OCR decisions

| Source ID | Metadata asset | Native text asset | Layout text asset | Text output bytes (native/layout) | Rendered result-relevant pages | Render output pattern | OCR decision and exact basis |
|---|---|---|---|---:|---|---|---|
| DOC-001 | `preprocessing/metadata/jama_de_boer_2019_oi_190122.pdfinfo.txt` | `preprocessing/native_text/jama_de_boer_2019_oi_190122.txt` | `preprocessing/layout_text/jama_de_boer_2019_oi_190122.txt` | 58253 / 103426 | 1-11 (11 pages) | `preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-pN.png` | NOT_RUN. Native and layout text are usable for all result-relevant narrative, Table 1, Table 2, Figures 1-4, captions, and footnotes. |
| DOC-002 | `preprocessing/metadata/joi190122supp1_prod.pdfinfo.txt` | `preprocessing/native_text/joi190122supp1_prod.txt` | `preprocessing/layout_text/joi190122supp1_prod.txt` | 114248 / 122030 | 11-20, 31-33 (13 pages) | `preprocessing/rendered_pages/joi190122supp1_prod-pN.png` | NOT_RUN. All 33 pages have usable native/layout text. Rendered pages contain specific aims, study population/enrollment, procedures, analysis/power quantities, and analytic-plan addendum; unrendered pages contain background, risk/benefit/monitoring, roster, or references. |
| DOC-003 | `preprocessing/metadata/joi190122supp2_prod.pdfinfo.txt` | `preprocessing/native_text/joi190122supp2_prod.txt` | `preprocessing/layout_text/joi190122supp2_prod.txt` | 25575 / 37670 | 1-19 (19 pages) | `preprocessing/rendered_pages/joi190122supp2_prod-pN.png` | NOT_RUN. Native/layout text are usable for supplementary methods, all eTables, and all eFigures. |
| DOC-004 | `preprocessing/metadata/joi190122supp3_prod.pdfinfo.txt` | `preprocessing/native_text/joi190122supp3_prod.txt` | `preprocessing/layout_text/joi190122supp3_prod.txt` | 756 / 763 | 1 (1 page) | `preprocessing/rendered_pages/joi190122supp3_prod-p1.png` | NOT_RUN. The one-page data-sharing statement has usable native/layout text; it contains no outcome display requiring OCR. |

## Exact page-level visual-render scope

| Source ID | Rendered pages | Visual evidence purpose |
|---|---|---|
| DOC-001 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | Article abstract/method definitions, results displays, tables, figures, captions, and discussion/references containing result comparisons. |
| DOC-002 | 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 31, 32, 33 | Protocol aims/population/procedures and planned analysis/power; later analytic-plan addendum. |
| DOC-003 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 | Supplement cover/methods, eTables 1-11, and eFigures 1-3. |
| DOC-004 | 1 | Data-sharing statement. |

## Completeness and limitations

- Fresh metadata, native text, and layout text exist for every one of the 64 direct PDF pages.
- 44 result-relevant pages were rendered as fresh PNGs. The remaining 20 protocol pages have complete usable native/layout text and do not contain a result display requiring visual table/figure confirmation.
- OCR count: 0 pages. No page met the workflow criterion of unusable relevant native/layout text.
- No source type was unavailable and no extraction tool required by this package was missing.
