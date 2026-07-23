# PDF preprocessing response — DOC-003

- Scientific-audit coverage: source PDF pages 4–35 (32 pages). Pages 1–3 (cover/contents) and 36 (references) are **Not Audited by Design** for the default scientific audit.
- Native text: extracted for every selected page, with one normalized file per page and a combined selected-range file in `preprocessing/native_text/`.
- Selective visual renders: pages 14–16 (E-Figures 1–3) and 17–35 (E-Tables 1–12), at 200 dpi in `preprocessing/page_images/`.
- OCR: not used. Native text was usable on all selected pages, including compact tables; renders preserve table and figure layout for visual checking.
- Page-level evidence map and extraction-quality assessment: `preprocessing/page_extraction_manifest.md`.
- Limitation: native PDF text retains multi-column/table spacing and page continuations; use the rendered page alongside the page-level text when verifying a specific cell, row, or plotted/flow label.

Source PDF was not modified.
