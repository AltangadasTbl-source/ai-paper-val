# Fresh evidence-asset inventory

All assets were initiated fresh from the three direct sources; no old audit derivative was used. Linux native/layout tools were unavailable, so local Chrome PDF-viewer rendering followed by direct local CPU Tesseract OCR created the evidence assets.

| Document ID | Source units | Native text asset | Layout text asset | Rendered-page asset | OCR text asset | Table/sheet asset | Method and result |
|---|---:|---|---|---|---|---|---|
| DOC001 | 11 PDF pages | Not produced | Not produced | 11 PNG files in `preprocessing/rendered_pages/` | 11 text files in `preprocessing/ocr_text/` | No worksheet; table enumeration deferred to page/OCR review | Chrome CDP rendered every viewer page; Windows Tesseract with `-l eng` ran directly on every PNG. |
| DOC002 | 25 PDF pages | Not produced | Not produced | 25 PNG files in `preprocessing/rendered_pages/` | 25 text files in `preprocessing/ocr_text/` | No worksheet; table enumeration deferred to page/OCR review | Chrome CDP rendered every viewer page; Windows Tesseract with `-l eng` ran directly on every PNG. |
| DOC003 | 13 PDF pages | Not produced | Not produced | 13 PNG files in `preprocessing/rendered_pages/` | 13 text files in `preprocessing/ocr_text/` | No worksheet; table enumeration deferred to page/OCR review | Chrome CDP rendered every viewer page; Windows Tesseract with `-l eng` ran directly on every PNG. |

Totals: 49 rendered PNGs and 49 direct CPU-OCR text files. `preprocessing/page_inventory.md` provides the page-to-asset mapping.

