# Fresh-preprocessing limitations

1. Linux `pdfinfo`, `pdftotext`, `pdftoppm`, `pdftocairo`, `tesseract`, `libreoffice`, and `soffice` are unavailable on `PATH`; safe discovery also found no qpdf, mutool, Ghostscript, pdfimages, or exiftool substitute. Pandoc rejects PDF input.
2. A source-only local fallback provided page images and OCR but not native/layout text: Windows Chrome PDF viewer was controlled through CDP on localhost with GPU disabled, and direct Windows `tesseract.exe -l eng` created all 49 OCR files. No network URL, external source, GPU, Python, or legacy audit derivative was used.
3. OCR can contain recognition, reading-order, symbol, table-alignment, and footnote-association errors. Reviewers must compare material OCR observations against the corresponding fresh PNG and supplied PDF page.
4. Native/layout text search, exact text-coordinate recovery, and direct table reconstruction remain unavailable. Table count is not asserted during preprocessing.
5. No direct Office, workbook, or CSV source was supplied.
6. DOC001’s actual viewer count is 11 pages, superseding the Linux `file` report of 10; DOC002 and DOC003 have 25 and 13 pages.

See `preprocessing/tool_availability.md` and `preprocessing/page_inventory.md`.

