# Fresh Evidence-Asset Inventory

## Methods and tools

All processing was local and source-first. `pdfinfo` 26.01.0 established PDF metadata and page counts. `pdftotext` 26.01.0 produced native text, then `pdftotext -layout` 26.01.0 produced layout-preserving text for every page. `pdftoppm` 26.01.0 rendered selected result-relevant display pages at 200 dpi PNG. Tesseract 5.5.0 was available but was not run: the native and layout text supplied usable, selectable result-relevant text on every relevant page. No GPU, web access, Office conversion, or legacy audit asset was used.

| Source ID | Fresh metadata asset | Fresh native-text asset | Fresh layout-text asset | Result-relevant rendered pages | OCR asset / decision | Limitation |
|---|---|---|---|---|---|---|
| DOC-001 | preprocessing/jama_saccone_2017_oi_170144.pdfinfo.txt | preprocessing/native_text/jama_saccone_2017_oi_170144.txt | preprocessing/layout_text/jama_saccone_2017_oi_170144.txt | preprocessing/rendered_pages/DOC-001-p1.png; DOC-001-p3.png; DOC-001-p4.png; DOC-001-p5.png; DOC-001-p6.png; DOC-001-p7.png | Not required; native/layout text usable on pages 1-8 | PDF text is multi-column and some figure/table geometry requires the rendered PNG alongside layout text. |
| DOC-002 | preprocessing/joi170144supp1_prod.pdfinfo.txt | preprocessing/native_text/joi170144supp1_prod.txt | preprocessing/layout_text/joi170144supp1_prod.txt | preprocessing/rendered_pages/DOC-002-p3.png; DOC-002-p4.png; DOC-002-p12.png; DOC-002-p13.png; DOC-002-p14.png | Not required; native/layout text usable on pages 1-16 | Protocol pages contain planned rather than observed results; their role is definition, outcome, sample-size, and analysis-plan comparison. |
| DOC-003 | preprocessing/joi170144supp2_prod.pdfinfo.txt | preprocessing/native_text/joi170144supp2_prod.txt | preprocessing/layout_text/joi170144supp2_prod.txt | preprocessing/rendered_pages/DOC-003-p2.png; DOC-003-p3.png; DOC-003-p4.png | Not required; native/layout text usable on pages 1-4 | Dense eTable columns can require visual confirmation against page PNGs. |

## Page-level fresh-extraction record

| Source ID | Page(s) | Fresh extraction method | Result-relevant display / visual asset | OCR decision | Exact limitation or note |
|---|---|---|---|---|---|
| DOC-001 | 1 | Native and layout text | Rendered: DOC-001-p1.png | Not required | Abstract columns are selectable; rendered page preserves summary display. |
| DOC-001 | 2 | Native and layout text | None | Not required | Narrative/key-points page; usable native/layout text. |
| DOC-001 | 3 | Native and layout text | Rendered: DOC-001-p3.png (Figure 1) | Not required | Participant-flow geometry is visual; counts are available in text. |
| DOC-001 | 4 | Native and layout text | Rendered: DOC-001-p4.png (Table 1) | Not required | Multi-column Table 1 requires layout text and visual page for alignment. |
| DOC-001 | 5 | Native and layout text | Rendered: DOC-001-p5.png (Table 2) | Not required | Multi-column outcome table requires layout text and visual page for alignment. |
| DOC-001 | 6 | Native and layout text | Rendered: DOC-001-p6.png (Figure 2) | Not required | Kaplan-Meier plot is visual; caption and text are selectable. |
| DOC-001 | 7 | Native and layout text | Rendered: DOC-001-p7.png | Not required | Narrative discussion contains result interpretation; usable text. |
| DOC-001 | 8 | Native and layout text | None | Not required | Reference page; no result display. |
| DOC-002 | 1 | Native and layout text | None | Not required | Protocol title page; usable text. |
| DOC-002 | 2 | Native and layout text | None | Not required | Abbreviation page; usable text. |
| DOC-002 | 3 | Native and layout text | Rendered: DOC-002-p3.png | Not required | Protocol summary; visual rendering retained for structured summary fields. |
| DOC-002 | 4 | Native and layout text | Rendered: DOC-002-p4.png | Not required | Planned sample size and primary outcome; visual rendering retained. |
| DOC-002 | 5 | Native and layout text | None | Not required | Introduction; usable text. |
| DOC-002 | 6 | Native and layout text | None | Not required | Objective; usable text. |
| DOC-002 | 7 | Native and layout text | None | Not required | Study design and inclusion criteria; usable text. |
| DOC-002 | 8 | Native and layout text | None | Not required | Exclusion criteria; usable text. |
| DOC-002 | 9 | Native and layout text | None | Not required | Outcome definitions/follow-up; usable text. |
| DOC-002 | 10 | Native and layout text | None | Not required | Management definitions; usable text. |
| DOC-002 | 11 | Native and layout text | None | Not required | Intervention/randomization/masking; usable text. |
| DOC-002 | 12 | Native and layout text | Rendered: DOC-002-p12.png | Not required | Secondary-outcome list; visual rendering retained. |
| DOC-002 | 13 | Native and layout text | Rendered: DOC-002-p13.png | Not required | Sample-size assumptions; visual rendering retained. |
| DOC-002 | 14 | Native and layout text | Rendered: DOC-002-p14.png | Not required | Statistical-analysis plan; visual rendering retained. |
| DOC-002 | 15 | Native and layout text | None | Not required | Reference page; no result display. |
| DOC-002 | 16 | Native and layout text | None | Not required | Reference page; no result display. |
| DOC-003 | 1 | Native and layout text | None | Not required | Supplement index; usable text. |
| DOC-003 | 2 | Native and layout text | Rendered: DOC-003-p2.png (eTable 1) | Not required | Dense table columns require layout text and visual page for alignment. |
| DOC-003 | 3 | Native and layout text | Rendered: DOC-003-p3.png (eTable 2) | Not required | Dense outcomes table requires layout text and visual page for alignment. |
| DOC-003 | 4 | Native and layout text | Rendered: DOC-003-p4.png (eTable 3) | Not required | Dense subgroup table requires layout text and visual page for alignment. |

All page units had usable native and layout text. OCR units: 0. There are no sheets, Office tables, or CSV rows because no such direct source exists.
