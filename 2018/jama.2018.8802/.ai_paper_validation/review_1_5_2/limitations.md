# Fresh-Preprocessing Limitations

1. The package contains three direct PDF research sources (44 PDF pages) and no direct Office, workbook, or CSV source.
2. The usual Linux `pdfinfo`, `pdftotext`, `pdftoppm`, `pdftocairo`, `tesseract`, `libreoffice`, and `soffice` commands are unavailable. Fresh local Acrobat COM extraction nevertheless supplied complete native text and coordinate-layout TSVs for all 44 pages.
3. Fresh direct full-page visual-confirmation rasters exist for 13 selected pages: DOC-001 pp. 3, 4, 6, 7, 8; DOC-002 pp. 13, 14, 15, 18, 19; and DOC-003 pp. 2, 3, 8. The native text and coordinate layout are readable on every result-relevant page, so OCR was not required. DOC-002 p. 5 is a planned flow diagram whose only text is caption/page furniture; it contains no reported result display requiring image review.
4. Acrobat native extraction contains some duplicated adjacent token runs in support text/tables. The coordinate-layout TSVs preserve word positions and should be used to reconstruct columns and distinguish extraction artifacts from printed evidence.
5. `capture_window.ps1`, all `*test.png` files, and the failed blank/cropped trials `DOC-003-page-008.png` and `DOC-003-page-008b.png` are excluded from evidence. No legacy derivative, external source, web content, package installation, GPU use, or source modification was used.
