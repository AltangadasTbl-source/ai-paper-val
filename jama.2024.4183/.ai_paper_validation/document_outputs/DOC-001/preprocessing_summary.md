# PDF preprocessing response — DOC-001

- Scientific-audit coverage: source PDF pages 1–10 (10/10 pages).
- Native text: extracted for every selected page, with one normalized file per page and a combined selected-range file in `preprocessing/native_text/`.
- Selective visual renders: pages 3 (Figure 1), 5 (Table), 6 (Figure 2 participant flow), and 7 (Figure 3), at 200 dpi in `preprocessing/page_images/`.
- OCR: not used. Native text was usable on all pages, including the visual pages; renders preserve layout for visual checking.
- Page-level evidence map and extraction-quality assessment: `preprocessing/page_extraction_manifest.md`.
- Limitation: native PDF text retains the publisher's multi-column order and table spacing; use the rendered page alongside the page-level text when adjudicating a row/column or figure-flow relationship.

Source PDF was not modified.
