# Fresh Evidence-Asset Inventory

## Tools and direct commands

- `pdfinfo version 26.01.0`; invoked once per direct PDF for metadata and page count.
- `pdftotext version 26.01.0`; invoked once per PDF for native text and once with `-layout` for layout-preserving text.
- `pdftoppm version 26.01.0`; invoked at 180 dpi with `-f N -l N -singlefile -png` for the listed result-relevant pages.
- `tesseract 5.5.0`; not invoked. No relevant page had unusable native and layout text after direct extraction and selected-page rendering.
- PDF extraction emitted non-fatal `Syntax Warning: Invalid Font Weight` messages for the main article; output files were nevertheless produced and readable.

Command form used (with each exact source and output path substituted):

```text
pdfinfo -- "SOURCE.pdf"
pdftotext -- "SOURCE.pdf" "preprocessing/native_text/SOURCE.txt"
pdftotext -layout -- "SOURCE.pdf" "preprocessing/layout_text/SOURCE.txt"
pdftoppm -f N -l N -singlefile -png -r 180 -- "SOURCE.pdf" "preprocessing/rendered_pages/DOC-NNN-pN"
```

## Per-source fresh derivatives and decisions

| Source ID | Metadata/native/layout assets | Native/layout outcome and limitations | Rendered result-relevant pages | OCR decision |
|---|---|---|---|---|
| DOC-001 | `preprocessing/native_text/jama_parshuram_2018_oi_180015.txt` (64626 bytes); `preprocessing/layout_text/jama_parshuram_2018_oi_180015.txt` (119769 bytes) | Readable native and layout text for all 11 pages. Multi-column order and Figure/Table spatial alignment are imperfect on pp. 3 and 7-8; rendered images provide visual corroboration. | pp. 1-9: `preprocessing/rendered_pages/DOC-001-p1.png` through `DOC-001-p9.png` | Not required: the relevant printed text is usable in native/layout extraction; images address layout rather than OCR recovery. |
| DOC-002 | `preprocessing/native_text/joi180015supp1_prod.txt` (134797 bytes); `preprocessing/layout_text/joi180015supp1_prod.txt` (146148 bytes) | Readable native and layout text for all 37 pages. Long protocol tables may wrap rows in text extraction; rendered table and power/analysis pages support visual reading. | pp. 7-17 and 19-30: `preprocessing/rendered_pages/DOC-002-p7.png`, `DOC-002-p8.png`, `DOC-002-p9.png`, `DOC-002-p10.png`, `DOC-002-p11.png`, `DOC-002-p12.png`, `DOC-002-p13.png`, `DOC-002-p14.png`, `DOC-002-p15.png`, `DOC-002-p16.png`, `DOC-002-p17.png`, `DOC-002-p19.png`, `DOC-002-p20.png`, `DOC-002-p21.png`, `DOC-002-p22.png`, `DOC-002-p23.png`, `DOC-002-p24.png`, `DOC-002-p25.png`, `DOC-002-p26.png`, `DOC-002-p27.png`, `DOC-002-p28.png`, `DOC-002-p29.png`, `DOC-002-p30.png` | Not required: all result-relevant protocol, analysis, and tabular text is readable; rendering was used for visual table structure. |
| DOC-003 | `preprocessing/native_text/joi180015supp2_prod.txt` (10571 bytes); `preprocessing/layout_text/joi180015supp2_prod.txt` (12994 bytes) | Readable native and layout text for all 7 pages. Source contains line-numbered analysis-plan prose and code-like expressions; line wrapping is preserved imperfectly but is readable. | pp. 1-7: `preprocessing/rendered_pages/DOC-003-p1.png` through `DOC-003-p7.png` | Not required: relevant analysis-plan text is usable. |
| DOC-004 | `preprocessing/native_text/joi180015supp3_prod.txt` (25830 bytes); `preprocessing/layout_text/joi180015supp3_prod.txt` (41820 bytes) | Readable native and layout text for all 14 pages. eFigure label placement and wide eTable columns are not fully linearized; rendering supports exact visual table/figure interpretation. | pp. 1-14: `preprocessing/rendered_pages/DOC-004-p1.png` through `DOC-004-p14.png` | Not required: extracted result text is usable and selected images preserve complex layout. |

## Table and figure location inventory

| Source ID | Direct-source locations prepared for later mapping |
|---|---|
| DOC-001 | Figure 1 (p. 3); Tables 1-3 (pp. 5-7); Figure 2 (p. 8); result narrative and definitions (pp. 1-9). |
| DOC-002 | Trial and analysis text (pp. 7-17); Tables 1-7 (pp. 19-28, with Table 4 continuing p. 23 and Table 6 continuing pp. 26-27); power/sample-size appendix (pp. 29-30). |
| DOC-003 | Primary/secondary analysis plan and code/expression display (pp. 1-5); subgroup plan (p. 6); ICU analysis plan (p. 7). |
| DOC-004 | eFigure S1 (pp. 1-3); eFigure S2 (pp. 4-5); eTable 1 (pp. 6-8); eTable 2 (pp. 9-10); eTable 3 (p. 11); eTable 4 (pp. 12-13); eTable 5 (p. 14). |

## Completeness and limitations

Fresh native and layout text was generated for all 69 direct PDF pages. Fifty-three result-relevant pages were additionally rendered as PNG: 9 in DOC-001, 23 in DOC-002, 7 in DOC-003, and 14 in DOC-004. The remaining 16 pages are title/background, references, or non-result narrative pages; their readable native/layout text remains available for full-source mapping. No OCR unit was necessary. No Office conversion was applicable because no Office source was supplied.

