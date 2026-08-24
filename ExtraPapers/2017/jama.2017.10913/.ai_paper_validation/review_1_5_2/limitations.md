# Fresh-Processing Limitations

- The package contains three direct PDFs and no direct DOC, DOCX, XLS, XLSX, or CSV source. Office conversion and Office structure extraction were therefore not applicable.
- All 47 PDF pages supplied usable native and layout text. No page met the criterion for targeted OCR; CPU Tesseract was available but not invoked.
- `pdftotext` can flatten visual table geometry and does not provide the numerical trace of plotted curves. The fresh 150-dpi rendered PNGs are retained for verification of table columns, figure labels, captions, flow diagrams, and chart displays.
- DOC-002 pp. 26-29 contain reference-list continuation. They were freshly extracted and included in complete source coverage but were not rendered because no result-relevant table, figure, or quantitative display appears on those pages.
- Protocol values in DOC-002 include background, preliminary, planning, and prespecified material. Any later cross-document comparison must match population, analysis status, time point, and contrast rather than assume it is a trial-result duplicate.
