# Page-level extraction manifest — DOC-001-main-article

- Source PDF: `jama_saynorea_2019_oi_190106_1635377898.43062.pdf` (unchanged).
- Selected audit range: PDF pp. 1–11.
- OCR selector: [`../../preprocessing/ocr_backend.json`](../../preprocessing/ocr_backend.json); selected backend `rapidocr-cpu`, with no NVIDIA GPU available. Native text is adequate for every selected page; page 3 additionally has retained CPU OCR for the flow diagram.
- Text path pattern: `normalized_text/page-PPP.txt`, where `PPP` is the three-digit source PDF page number. Each file is a direct page-level native-text extraction and retains the source-PDF/page mapping below.

| Source PDF p. | Native characters | Extraction quality | Method / retained artifact |
|---:|---:|---|---|
| 1 | 7,494 | High | Native PDF text; `normalized_text/page-001.txt` |
| 2 | 9,780 | High | Native PDF text; `normalized_text/page-002.txt` |
| 3 | 8,358 | High; flow-diagram text present | Native + completed CPU OCR: `ocr/page-003.txt`, `page_metadata/page-003.ocr.json`, `page_images/page-003.png` |
| 4 | 9,843 | High; Table 1 text present | Native PDF text; `normalized_text/page-004.txt` |
| 5 | 9,214 | High; Table 2 text present | Native PDF text; `normalized_text/page-005.txt` |
| 6 | 9,368 | High; Figure 2 text present | Native PDF text; `normalized_text/page-006.txt` |
| 7 | 5,872 | Adequate; Table 3 text present | Native PDF text; `normalized_text/page-007.txt` |
| 8 | 10,149 | High; Table 3 continuation text present | Native PDF text; `normalized_text/page-008.txt` |
| 9 | 9,509 | High; Figure 3 text present | Native PDF text; `normalized_text/page-009.txt` |
| 10 | 9,873 | High; Figure 4 text present | Native PDF text; `normalized_text/page-010.txt` |
| 11 | 10,357 | High | Native PDF text; `normalized_text/page-011.txt` |

Status: completed native extraction. The retained flow-diagram OCR on p. 3 is explicitly CPU (mean confidence 0.9094); all other pages require no OCR supplementation.
