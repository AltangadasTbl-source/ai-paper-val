# Source Coverage

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_jabre_2018_oi_180004.pdf | PDF_PAGE | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 | joi180004supp1_prod.pdf | PDF_PAGE | 134 | 133 | 1 | 134 | COMPLETE |
| DOC-003 | joi180004supp2_prod.pdf | PDF_PAGE | 3 | 3 | 0 | 3 | COMPLETE |

Unique-unit totals at inventory handoff: total 146; reusable 145; fresh-required 1; mapped 0. Reusable and fresh-required partition each source. Mapped counts remain zero until fresh mapper artifacts document complete inspection, including reuse-backed pages.

DOC-001 pages 1-9 and DOC-003 pages 1-3 have source-matched native/layout text. DOC-002 pages 1-107 and 110-125 have source-matched native/layout text (123 pages); pages 108-109 and 126-133 have source-hash-matched OCR and rendered images (10 further pages). Page 52 has supplementary OCR/images, and page 103 has OCR/images; both are already counted within native-backed units and create no additional unit.

Fresh-required assignment: support quantitative mapper must render and inspect DOC-002 page 134 directly with pdftoppm or pdftocairo, identify its actual content or blankness, and map its result-relevant status. No reusable text or image covers this page. Native text emptiness does not establish visual blankness. Fresh derivative must remain below review_1_6_1 and record its direct rendering engine.

Downstream main quantitative mapping assignment: all DOC-001 pages 1-9. Downstream support quantitative mapping assignment: all DOC-002 pages 1-134 and DOC-003 pages 1-3, split into disjoint context-bounded shards as needed. Existing OCR is a locator and transcription aid; direct PDF pages remain authoritative. An asset without complete coverage does not authorize omission of its uncovered units.

Current mapping closure: all 146 unique units are mapped. Main artifact confirms DOC-001 pages 1-9 (9); support-original part confirms DOC-002 pages 1-56 (56); support-final part confirms DOC-002 pages 57-134 (78) and DOC-003 pages 1-3 (3). The canonical support artifact is a lossless concatenation of both parts with source-link prefixes adjusted for its directory. DOC-002 page 134 was directly rendered with Poppler pdftoppm 25.03.0 and visually inspected; its content is mapped in the final-plan/results part. Earlier inventory counts describe the inventory handoff only; the completed table records current coverage.
