# Limitations and Missing Definitions

## Fresh preprocessing limitations

At preprocessing, the local PATH contained `file` and `sha256sum` but not `pdfinfo`, `pdftotext`, `pdftoppm`, `pdftocairo`, `tesseract`, `libreoffice`, or `soffice`. Consequently, no fresh native text, layout text, rendered PDF page, OCR text, or Office-conversion derivative could be produced. The affected scope is all 69 PDF pages: DOC-001 pp. 1-11, DOC-002 pp. 1-37, DOC-003 pp. 1-7, and DOC-004 pp. 1-14.

Exact page counts were recovered from PDF page trees with a read-only local structural fallback where necessary. This supports complete source-unit coverage but does not expose result text, visual tables, figures, captions, or page-level quantitative relationships. No GPU was probed or used, no software was installed, no web resource was accessed, and no existing audit derivative was used as evidence.
