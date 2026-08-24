# Fresh Evidence-Asset Inventory

All assets below were newly generated for this run from the three direct PDFs. `pdfinfo`, `pdftotext`, `pdftoppm`, and `tesseract` were available from Poppler 26.01.0 and Tesseract 5.5.0. CPU-only policy was observed; Tesseract was not run because the relevant native and layout text was usable.

| Source ID | Direct-source check and exact method | Fresh asset path | Units covered | Result-relevant visual/OCR decision | Limitations |
|---|---|---|---|---|---|
| DOC-001 | `pdfinfo`; `pdftotext`; `pdftotext -layout` | preprocessing/native_text/DOC-001_jama_andrews_2017_oi_170091.txt | PDF pp. 1-8 | Rendered with `pdftoppm -f 1 -l 8 -png -r 150`; 8 PNGs at `preprocessing/rendered_pages/DOC-001_p-1.png` through `DOC-001_p-8.png`. OCR not needed. | Text extraction flattens some table geometry; use matching rendered page to verify row/column alignment. |
| DOC-001 | `pdftotext -layout` | preprocessing/layout_text/DOC-001_jama_andrews_2017_oi_170091_layout.txt | PDF pp. 1-8 | Layout text is usable for Tables 1-2 and figure captions; rendered pages retain visual evidence. | Figure plotted values may require visual interpretation rather than text extraction. |
| DOC-002 | `pdfinfo`; `pdftotext`; `pdftotext -layout` | preprocessing/native_text/DOC-002_joi170091supp1_prod.txt | PDF pp. 1-29 | Rendered substantive protocol pp. 1-25 with `pdftoppm -f 1 -l 25 -png -r 150`; 25 PNGs at `preprocessing/rendered_pages/DOC-002_p-01.png` through `DOC-002_p-25.png`. OCR not needed. | Pages 26-29 are reference-list continuation, freshly extracted/classified but not visually rendered because they contain no result-relevant display. |
| DOC-002 | `pdftotext -layout` | preprocessing/layout_text/DOC-002_joi170091supp1_prod_layout.txt | PDF pp. 1-29 | Layout text is usable for protocol Tables 1-5 and Figures 1-2; rendered protocol pages preserve table and flow-diagram geometry. | Protocol numbers are planning/preliminary material and must be matched by population/time/role before comparison to trial results. |
| DOC-003 | `pdfinfo`; `pdftotext`; `pdftotext -layout` | preprocessing/native_text/DOC-003_joi170091supp2_prod.txt | PDF pp. 1-10 | Rendered with `pdftoppm -f 1 -l 10 -png -r 150`; 10 PNGs at `preprocessing/rendered_pages/DOC-003_p-01.png` through `DOC-003_p-10.png`. OCR not needed. | Native text is usable; visual pages remain the confirmation source for eTable column alignment. |
| DOC-003 | `pdftotext -layout` | preprocessing/layout_text/DOC-003_joi170091supp2_prod_layout.txt | PDF pp. 1-10 | Layout text is usable for eTables 1-5 (pp. 6-10); visual pages preserve cells, headings, and footnotes. | None affecting extraction; reported model definitions still need source-grounded review. |

Native-text byte counts: DOC-001 45,119; DOC-002 72,743; DOC-003 20,433. Layout-text byte counts: DOC-001 83,884; DOC-002 79,459; DOC-003 25,927. The 43 rendered PNGs are fresh derivatives; no Office conversion or structure extraction was applicable because all direct sources are PDFs.

## Reproducible Direct Commands

The following commands were run from the package root with the exact direct filenames listed in `source_inventory.md`:

```text
sha256sum -- jama_andrews_2017_oi_170091.pdf joi170091supp1_prod.pdf joi170091supp2_prod.pdf
pdfinfo jama_andrews_2017_oi_170091.pdf
pdfinfo joi170091supp1_prod.pdf
pdfinfo joi170091supp2_prod.pdf
pdftotext jama_andrews_2017_oi_170091.pdf .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-001_jama_andrews_2017_oi_170091.txt
pdftotext -layout jama_andrews_2017_oi_170091.pdf .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-001_jama_andrews_2017_oi_170091_layout.txt
pdftotext joi170091supp1_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-002_joi170091supp1_prod.txt
pdftotext -layout joi170091supp1_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-002_joi170091supp1_prod_layout.txt
pdftotext joi170091supp2_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-003_joi170091supp2_prod.txt
pdftotext -layout joi170091supp2_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-003_joi170091supp2_prod_layout.txt
pdftoppm -f 1 -l 8 -png -r 150 jama_andrews_2017_oi_170091.pdf preprocessing/rendered_pages/DOC-001_p
pdftoppm -f 1 -l 25 -png -r 150 joi170091supp1_prod.pdf preprocessing/rendered_pages/DOC-002_p
pdftoppm -f 1 -l 10 -png -r 150 joi170091supp2_prod.pdf preprocessing/rendered_pages/DOC-003_p
```

Tool versions: Poppler `pdfinfo`, `pdftotext`, and `pdftoppm` 26.01.0; Tesseract 5.5.0 (available but unused).
