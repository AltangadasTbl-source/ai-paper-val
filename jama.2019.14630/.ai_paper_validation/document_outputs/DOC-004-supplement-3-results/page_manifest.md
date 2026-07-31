# Page-level extraction manifest — DOC-004-supplement-3-results

- Source PDF: `joi190106supp3_prod_1635377898.49725.pdf` (unchanged).
- Selected audit range: PDF pp. 1–27. PDF pp. 28–29 are excluded (additional-author affiliations).
- OCR selector: [`../../preprocessing/ocr_backend.json`](../../preprocessing/ocr_backend.json); selected backend `rapidocr-cpu`, not CUDA. Completed page metadata records actual CPU execution and confidence.
- Text path pattern: `normalized_text/page-PPP.txt`; images, where retained, are `page_images/page-PPP.png` at 200 dpi.

| Source PDF p. | Native characters | Extraction quality | Method / retained artifact |
|---:|---:|---|---|
| 1 | 2,410 | Adequate contents/index text | Native PDF text; `normalized_text/page-001.txt` |
| 2 | 5,967 | High eTable text | Native PDF text; `normalized_text/page-002.txt` |
| 3 | 4,124 | High eTable text | Native PDF text; `normalized_text/page-003.txt` |
| 4 | 826 | Sparse continuation | Native + completed CPU OCR: `ocr/page-004.txt`, `page_metadata/page-004.ocr.json`, `page_images/page-004.png` |
| 5 | 3,066 | Adequate eTable text | Native PDF text; `normalized_text/page-005.txt` |
| 6 | 624 | Sparse continuation | Native + completed CPU OCR: `ocr/page-006.txt`, `page_metadata/page-006.ocr.json`, `page_images/page-006.png` |
| 7 | 2,044 | Adequate eTable text | Native PDF text; `normalized_text/page-007.txt`; retained table image `page_images/table_check-07.png` |
| 8 | 60 | Missing result text (copyright-only layer) | Native + completed CPU OCR: `ocr/page-008.txt`, `page_metadata/page-008.ocr.json`, `page_images/page-008.png`; OCR also contains only 58 characters |
| 9 | 4,571 | High eTable text | Native PDF text; `normalized_text/page-009.txt` |
| 10 | 3,638 | Adequate eTable text | Native PDF text; `normalized_text/page-010.txt` |
| 11 | 3,225 | Adequate eTable text | Native PDF text; `normalized_text/page-011.txt` |
| 12 | 3,343 | Adequate eTable text | Native PDF text; `normalized_text/page-012.txt` |
| 13 | 857 | Sparse continuation | Native + completed CPU OCR: `ocr/page-013.txt`, `page_metadata/page-013.ocr.json`, `page_images/page-013.png` |
| 14 | 2,796 | Adequate eTable text | Native PDF text; `normalized_text/page-014.txt` |
| 15 | 3,761 | Adequate eTable text | Native PDF text; `normalized_text/page-015.txt` |
| 16 | 2,230 | Adequate eTable text | Native PDF text; `normalized_text/page-016.txt` |
| 17 | 3,207 | Adequate eTable text | Native PDF text; `normalized_text/page-017.txt` |
| 18 | 3,224 | Adequate eTable text | Native PDF text; `normalized_text/page-018.txt` |
| 19 | 3,221 | Adequate eTable text | Native PDF text; `normalized_text/page-019.txt` |
| 20 | 314 | Sparse continuation | Native + completed CPU OCR: `ocr/page-020.txt`, `page_metadata/page-020.ocr.json`, `page_images/page-020.png` |
| 21 | 3,092 | Adequate eTable text | Native PDF text; `normalized_text/page-021.txt` |
| 22 | 3,717 | Adequate eTable text | Native PDF text; `normalized_text/page-022.txt` |
| 23 | 2,915 | Adequate eTable text | Native PDF text; `normalized_text/page-023.txt` |
| 24 | 3,679 | Adequate eTable text | Native PDF text; `normalized_text/page-024.txt` |
| 25 | 791 | Limited, expected figure caption/labels | Native PDF text; `normalized_text/page-025.txt`; retained figure image `page_images/figure_render-25.png` |
| 26 | 515 | Limited, expected figure caption/labels | Native PDF text; `normalized_text/page-026.txt`; retained figure image `page_images/figure_render-26.png` |
| 27 | 427 | Limited, expected figure caption/labels | Native PDF text; `normalized_text/page-027.txt`; retained figure image `page_images/figure_render-27.png` |

Completed CPU OCR is explicitly CPU: page 4 mean confidence 0.8624; page 6 0.8804; page 8 0.8957; page 13 0.8601; and page 20 0.9143. Actual provider information and full backend reports are retained in each page metadata JSON. The detector and recognizer provider fields are empty in the selected backend report; CUDA was neither available nor claimed.
