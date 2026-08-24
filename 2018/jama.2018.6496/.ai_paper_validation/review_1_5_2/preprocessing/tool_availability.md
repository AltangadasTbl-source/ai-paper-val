# Fresh preprocessing tool availability

Checked on 2026-08-23. No software was installed, no web content was accessed, and no GPU was probed or used.

| Tool or route | Runtime result | Use in this run |
|---|---|---|
| `sha256sum`, `file` | Available | Hashing and initial type inspection. Chrome superseded DOC001’s incomplete `file` page count. |
| `pdfinfo`, `pdftotext`, `pdftoppm`, `pdftocairo`, Linux `tesseract` | Not found on `PATH` | Native/layout extraction and Linux rendering/OCR unavailable. |
| `libreoffice` / `soffice` | Not found | No Office sources supplied. |
| `pandoc` | Available, rejects PDF input | Not used for extraction. |
| Windows Chrome | `C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe` | Used offline in headless mode with GPU disabled and CDP on localhost. |
| Windows Tesseract | `C:\\msys64\\ucrt64\\bin\\tesseract.exe` | Used directly in CPU mode with English language data. |

## Successful local source-only fallback

Chrome used a temporary profile and flags `--headless=new --remote-debugging-port=9226 --remote-allow-origins=* --window-size=1600,2200 --disable-gpu --no-first-run`. Each local PDF was opened in Chrome. In the CDP webview target, `Runtime.evaluate` hid `#sidenav` and `#toolbar`, called `viewer.viewport_.fitToPage()`, `viewer.viewport_.goToPage(zero_based_page_index)`, and `viewer.viewport_.getPageScreenRect(index)`; `Page.captureScreenshot` captured that page rectangle to `preprocessing/rendered_pages/`.

Each PNG was OCRed with the equivalent direct CPU command:

```text
C:\msys64\ucrt64\bin\tesseract.exe <rendered-page.png> <ocr-output-base> -l eng
```

This produced 49 PNGs and 49 paired OCR text files. Chrome viewer page counts were DOC001=11, DOC002=25, DOC003=13.

