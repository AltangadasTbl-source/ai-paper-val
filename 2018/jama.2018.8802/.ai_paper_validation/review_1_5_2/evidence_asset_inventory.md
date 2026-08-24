# Fresh Evidence-Asset Inventory

## Tools and methods

- `pdfinfo version 26.01.0`: direct metadata/page-count extraction for each PDF. Outputs: `preprocessing/metadata/DOC-001_pdfinfo.txt`, `preprocessing/metadata/DOC-002_pdfinfo.txt`, and `preprocessing/metadata/DOC-003_pdfinfo.txt`.
- `pdftotext version 26.01.0`: direct native-text extraction. Outputs: `preprocessing/native_text/DOC-001.txt`, `preprocessing/native_text/DOC-002.txt`, and `preprocessing/native_text/DOC-003.txt`.
- `pdftotext -layout version 26.01.0`: direct layout-preserving extraction for aligned tables and displays. Outputs: `preprocessing/layout_text/DOC-001.txt`, `preprocessing/layout_text/DOC-002.txt`, and `preprocessing/layout_text/DOC-003.txt`.
- `pdftoppm version 26.01.0`: 200-dpi PNG renderings of every page classified as result-relevant below (39 fresh canonical renders). Outputs are enumerated below under `preprocessing/rendered_pages/`.
- `tesseract 5.5.0`: available but not run. Every result-relevant page had usable native and layout text; no OCR unit met the threshold for CPU OCR.
- No Office source was present; no conversion or Office structure extraction was applicable. No GPU was probed or used.

The exact direct commands used were `pdfinfo "SOURCE.pdf"`, `pdftotext "SOURCE.pdf" "OUTPUT.txt"`, `pdftotext -layout "SOURCE.pdf" "OUTPUT.txt"`, and `pdftoppm -f N -l N -singlefile -r 200 -png "SOURCE.pdf" "OUTPUT-PNN"`.

## DOC-001 — main article

Native text (64,361 bytes) and layout text (105,053 bytes) were usable on all 10 pages. Pages 1-9 contain result-relevant abstract, methods/results context, Figure 1, or Tables 1-3 and were visually rendered. Page 10 is author/reference material and was not rendered; its native/layout text remains available for complete source coverage. Rendered assets: `DOC-001-p01.png`, `DOC-001-p02.png`, `DOC-001-p03.png`, `DOC-001-p04.png`, `DOC-001-p05.png`, `DOC-001-p06.png`, `DOC-001-p07.png`, `DOC-001-p08.png`, `DOC-001-p09.png`.

| Page(s) | Fresh methods/assets | Result-relevant status | OCR | Limitation |
|---|---|---|---|---|
| 1 | native + layout + render | Abstract and article opening; quantitative summary | Not needed | Multi-column reading order is best checked in layout/rendering. |
| 2-4 | native + layout + render | Study methods, enrollment/outcome definitions, and result context | Not needed | Native text can interleave columns. |
| 5 | native + layout + render | Figure/narrative performance-measure results | Not needed | Visual figure alignment requires rendered page. |
| 6 | native + layout + render | Table 1 baseline characteristics | Not needed | Table cells may require visual confirmation. |
| 7 | native + layout + render | Table 2 adherence results | Not needed | Table cells/footnotes may require visual confirmation. |
| 8 | native + layout + render | Table 3 outcome results | Not needed | Table cells/footnotes may require visual confirmation. |
| 9 | native + layout + render | Discussion/limitations and quantitative interpretation | Not needed | Multi-column reading order is best checked in layout/rendering. |
| 10 | native + layout | Author/reference material; no result display identified | Not needed | Not rendered because no result-relevant visual display was identified. |

## DOC-002 — supporting protocol/statistical-analysis-plan document

Native text (33,098 bytes) and layout text (39,028 bytes) were usable on all 25 pages. Pages 1-21 contain protocol, definitions, figures, outcomes, population, and analysis information, and every one was visually rendered. Pages 22-25 are references and were retained in native/layout text only. Rendered assets: `DOC-002-p01.png` through `DOC-002-p21.png` (one canonical `pNN` file per page).

| Page(s) | Fresh methods/assets | Result-relevant status | OCR | Limitation |
|---|---|---|---|---|
| 1-4 | native + layout + render | Protocol title, aim, scope, and background | Not needed | Line-numbered protocol text; rendering retains direct page appearance. |
| 5 | native + layout + render | Flow diagram | Not needed | Diagram placement is visual; inspect rendering for exact labels. |
| 6-8 | native + layout + render | Participants, eligibility, and randomization | Not needed | Rendering retains direct page appearance. |
| 9 | native + layout + render | Intervention figure | Not needed | Diagram placement is visual. |
| 10-11 | native + layout + render | Intervention procedures | Not needed | Rendering retains direct page appearance. |
| 12 | native + layout + render | Continuous-quality-improvement figure | Not needed | Diagram placement is visual. |
| 13 | native + layout + render | Monitoring-cycle figure and primary-outcome introduction | Not needed | Diagram and outcome text share the page. |
| 14-16 | native + layout + render | Performance-measure definitions/eligibility and denominators | Not needed | Dense definition display requires layout/render confirmation. |
| 17 | native + layout + render | Follow-up outcome definitions | Not needed | Rendering retains direct page appearance. |
| 18-19 | native + layout + render | Statistical analysis plan and composite-measure example | Not needed | Equations/line-numbered paragraphs may need layout confirmation. |
| 20-21 | native + layout + render | Consent, data capture, and quality-control procedures | Not needed | Rendered because population/data definitions can affect numeric interpretation. |
| 22-25 | native + layout | References only; no protocol result display identified | Not needed | Not rendered because no result-relevant visual display was identified. |

## DOC-003 — supplementary online results/tables

Native text (11,700 bytes) and layout text (14,018 bytes) were usable on all 9 pages. All pages are result-relevant or define quantitative result measures and were rendered. Rendered assets: `DOC-003-p01.png` through `DOC-003-p09.png`.

| Page(s) | Fresh methods/assets | Result-relevant status | OCR | Limitation |
|---|---|---|---|---|
| 1-2 | native + layout + render | Supplement heading/eAppendix baseline-survey details | Not needed | Page 2 includes narrative definitions that should be checked against rendering if line wraps matter. |
| 3-4 | native + layout + render | eTable 1 performance-measure specifications and exclusions | Not needed | Dense multi-row table continues across pages; visual row alignment may require rendering. |
| 5 | native + layout + render | eTable 2 baseline characteristics | Not needed | Table cells/footnotes may require visual confirmation. |
| 6-7 | native + layout + render | eTable 3 secondary outcomes and notes | Not needed | Table spans pages and contains adjusted-effect footnotes. |
| 8-9 | native + layout + render | eTable 4 sensitivity-analysis adherence results and definitions | Not needed | Table continues across pages; visual row alignment may require rendering. |

## Limitations and OCR decision

Text extraction is fresh and direct, but PDF native text may not preserve multi-column or table-cell reading order. Layout text and fresh canonical page renderings were therefore retained for all 39 result-relevant pages: DOC-001 pp. 1-9 (9), DOC-002 pp. 1-21 (21), and DOC-003 pp. 1-9 (9). No source page had unusable relevant native/layout text, so zero OCR files were created. Page coverage is complete for all 44 direct PDF pages even where rendering was not necessary. Legacy or noncanonical derivative filenames were not counted.
