# Fresh Preprocessing Execution Status

Installed local Acrobat COM completed fresh direct extraction from every supplied PDF. `acrobat_extract.vbs` writes UTF-8 page-delimited native text from Acrobat page-word APIs; `acrobat_layout.vbs` writes coordinate-layout TSVs using the same page-word universe and word quadrilaterals.

| Source ID | Source | Pages | Native text | Coordinate layout | Result-relevant usability | Rendering/OCR decision |
|---|---|---:|---|---|---|---|
| DOC-001 | jama_wang_2018_oi_180070.pdf | 10 | COMPLETE: 9526 words, pp. 1-10 | COMPLETE: 9526 token rows, pp. 1-10 | Text-readable throughout; fresh full-page visual confirmation for pp. 3, 4, 6, 7, 8. | OCR NOT REQUIRED |
| DOC-002 | joi180070supp1_prod.pdf | 25 | COMPLETE: 7283 words, pp. 1-25 | COMPLETE: 7283 token rows, pp. 1-25 | Text-readable for result material; fresh full-page visual confirmation for pp. 13, 14, 15, 18, 19. P. 5 is a planned flow diagram without reported results. | OCR NOT REQUIRED |
| DOC-003 | joi180070supp2_prod.pdf | 9 | COMPLETE: 3879 words, pp. 1-9 | COMPLETE: 3879 token rows, pp. 1-9 | Text-readable on every eAppendix/eTable page; fresh full-page visual confirmation for pp. 2, 3, 8. | OCR NOT REQUIRED |

The complete fresh source universe is 44 pages and 20,688 extracted words/tokens. No native/layout/image/OCR derivative from an earlier audit was reused.

Thirteen `rendered_pages/*-full.png` assets are fresh direct full-page visual-confirmation evidence. `capture_window.ps1`, `rendered_pages/*test.png`, and failed blank/cropped trials `DOC-003-page-008.png` and `DOC-003-page-008b.png` are non-evidence. No OCR text was needed because every result-relevant page has usable fresh native and coordinate-layout text. The normal Linux PDF/OCR executables were unavailable; Acrobat COM was the installed local direct alternative. No web, GPU, or source modification was used.
