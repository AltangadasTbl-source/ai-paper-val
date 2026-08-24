# Fresh Preprocessing Execution Log

Working directory: package root. All source arguments were direct, quoted package-root filenames.

## Metadata

```text
pdfinfo "jama_de_boer_2019_oi_190122.pdf" > ".ai_paper_validation/review_1_5_2/preprocessing/metadata/jama_de_boer_2019_oi_190122.pdfinfo.txt"
pdfinfo "joi190122supp1_prod.pdf" > ".ai_paper_validation/review_1_5_2/preprocessing/metadata/joi190122supp1_prod.pdfinfo.txt"
pdfinfo "joi190122supp2_prod.pdf" > ".ai_paper_validation/review_1_5_2/preprocessing/metadata/joi190122supp2_prod.pdfinfo.txt"
pdfinfo "joi190122supp3_prod.pdf" > ".ai_paper_validation/review_1_5_2/preprocessing/metadata/joi190122supp3_prod.pdfinfo.txt"
```

Outputs: DOC-001 11 pages; DOC-002 33 pages; DOC-003 19 pages; DOC-004 1 page.

## Fresh text extraction

For each of the four filenames above, these two direct commands completed successfully, producing the paired assets named in `evidence_asset_inventory.md`:

```text
pdftotext "SOURCE.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/native_text/SOURCE.txt"
pdftotext -layout "SOURCE.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/layout_text/SOURCE.txt"
```

## Targeted render commands

```text
pdftoppm -f N -l N -singlefile -png -r 180 "jama_de_boer_2019_oi_190122.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-pN"
  N = 1,2,3,4,5,6,7,8,9,10,11
pdftoppm -f N -l N -singlefile -png -r 180 "joi190122supp1_prod.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-pN"
  N = 11,12,13,14,15,16,17,18,19,20,31,32,33
pdftoppm -f N -l N -singlefile -png -r 180 "joi190122supp2_prod.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-pN"
  N = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
pdftoppm -f 1 -l 1 -singlefile -png -r 180 "joi190122supp3_prod.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp3_prod-p1"
```

Output: 44 PNG images, all successfully written.

## OCR decision

`tesseract` 5.5.0 was available but was not invoked. Native and layout text were readable for every result-relevant page, so there were zero pages satisfying the targeted OCR criterion. No GPU was probed or used.
