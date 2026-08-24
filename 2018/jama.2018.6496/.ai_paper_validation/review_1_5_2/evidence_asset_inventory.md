# Fresh Evidence-Asset Inventory

## Tools and commands

| Tool | Version observed | Use |
|---|---|---|
| `pdfinfo` | 26.01.0 | Fresh PDF metadata and page-count confirmation |
| `pdftotext` | 26.01.0 | Native and `-layout` text extraction |
| `pdftoppm` | 26.01.0 | 200-dpi PNG rendering of selected result-relevant pages |
| `tesseract` | 5.5.0 | Available CPU OCR backend; not invoked |

Commands run, with literal source paths and outputs:

```text
pdfinfo -- jama_driver_2018_oi_180054.pdf
pdfinfo -- joi180054supp1_prod.pdf
pdfinfo -- joi180054supp2_prod.pdf
pdftotext -- jama_driver_2018_oi_180054.pdf .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-001.txt
pdftotext -layout -- jama_driver_2018_oi_180054.pdf .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-001.txt
pdftotext -- joi180054supp1_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-002.txt
pdftotext -layout -- joi180054supp1_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-002.txt
pdftotext -- joi180054supp2_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-003.txt
pdftotext -layout -- joi180054supp2_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-003.txt
pdftoppm -png -r 200 -f 1 -l 10 -- jama_driver_2018_oi_180054.pdf .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001
pdftoppm -png -r 200 -f 5 -l 22 -- joi180054supp1_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002
pdftoppm -png -r 200 -f 1 -l 13 -- joi180054supp2_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003
```

No Office source was supplied, so no Office conversion or structure extraction was applicable. No GPU was probed or used. No Tesseract command was run: the relevant native and layout text was readable and sufficient for source mapping.

## Per-source asset records

| Source ID | Native-text asset | Layout-text asset | Native / layout size | Rendered pages | OCR asset / decision | Limitation |
|---|---|---|---:|---|---|---|
| DOC-001 | `preprocessing/native_text/DOC-001.txt` | `preprocessing/layout_text/DOC-001.txt` | 61166 / 107683 bytes | 1-10 | None; native and layout text usable on every page, including Tables 1-5 and Figure 1 | Page 11 contains references rather than results; it remains text-mapped. Visual table alignment is preserved in layout text and PNGs. |
| DOC-002 | `preprocessing/native_text/DOC-002.txt` | `preprocessing/layout_text/DOC-002.txt` | 53164 / 59842 bytes | 5-22 | None; native and layout text usable on every page | It is a protocol, not a results report. Text includes PDF line-number artefacts; these do not obscure definitions, counts, or statistical-method statements. |
| DOC-003 | `preprocessing/native_text/DOC-003.txt` | `preprocessing/layout_text/DOC-003.txt` | 12444 / 14892 bytes | 1-13 | None; native and layout text usable on every page, including eTable 1 | The graph image itself is not digitized as numeric coordinates; its printed caption/description and reported hazard ratio are present in text and the page PNG. |

## Page-level fresh mapping and OCR decisions

Each listed page was checked against its fresh native/layout asset. `Usable` means that the page's relevant printed text, labels, and any displayed values were readable in at least one fresh text asset. `Rendered` identifies a new PNG asset; an em dash means rendering was not needed because the page was non-result reference/context material. Every row has OCR decision `NO_OCR_USABLE_TEXT`.

| Source ID | Page | Fresh text usability and mapped content | Rendered | OCR decision / limitation |
|---|---:|---|---|---|
| DOC-001 | 1 | Usable; title, abstract, population totals, primary/secondary outcome summaries | Yes | NO_OCR_USABLE_TEXT |
| DOC-001 | 2 | Usable; introduction, eligibility and difficult-airway definitions | Yes | NO_OCR_USABLE_TEXT |
| DOC-001 | 3 | Usable; randomization, outcome definitions, statistical analysis | Yes | NO_OCR_USABLE_TEXT |
| DOC-001 | 4 | Usable; Figure 1 participant flow and exclusion counts | Yes | NO_OCR_USABLE_TEXT |
| DOC-001 | 5 | Usable; baseline narrative and Table 1 | Yes | NO_OCR_USABLE_TEXT |
| DOC-001 | 6 | Usable; Table 2 and results narrative | Yes | NO_OCR_USABLE_TEXT |
| DOC-001 | 7 | Usable; Table 3 trial outcomes | Yes | NO_OCR_USABLE_TEXT |
| DOC-001 | 8 | Usable; Table 4 successful technique after failed first attempt | Yes | NO_OCR_USABLE_TEXT |
| DOC-001 | 9 | Usable; Table 5 complications and subgroup/figure text | Yes | NO_OCR_USABLE_TEXT |
| DOC-001 | 10 | Usable; subgroup results, discussion and quantitative interpretation | Yes | NO_OCR_USABLE_TEXT |
| DOC-001 | 11 | Usable; references | — | NO_OCR_USABLE_TEXT; no result display |
| DOC-002 | 1 | Usable; protocol title and investigator/source identity | — | NO_OCR_USABLE_TEXT; title context |
| DOC-002 | 2 | Usable; contents and section locations | — | NO_OCR_USABLE_TEXT; contents context |
| DOC-002 | 3 | Usable; contents and planned analysis/interim section locations | — | NO_OCR_USABLE_TEXT; contents context |
| DOC-002 | 4 | Usable; abbreviation and term definitions | — | NO_OCR_USABLE_TEXT; definitions context |
| DOC-002 | 5 | Usable; background and study objective | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 6 | Usable; prior quantitative background and risk context | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 7 | Usable; background, rationale, and endpoint context | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 8 | Usable; risks and study-objective statements | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 9 | Usable; primary and secondary endpoint definitions | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 10 | Usable; outcome measurement definitions | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 11 | Usable; study design, randomization, and procedures | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 12 | Usable; procedures and treatment-switch conditions | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 13 | Usable; eligibility/population criteria | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 14 | Usable; consent and population context | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 15 | Usable; consent conditions and risk statements | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 16 | Usable; patient-objection procedure | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 17 | Usable; study procedures and data collection | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 18 | Usable; adverse-event monitoring and observations | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 19 | Usable; planned statistical methods and summary conventions | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 20 | Usable; analysis populations and primary-outcome analysis | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 21 | Usable; secondary analyses, interim/futility criteria | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 22 | Usable; monitoring/administrative quantitative context | Yes | NO_OCR_USABLE_TEXT |
| DOC-002 | 23 | Usable; references | — | NO_OCR_USABLE_TEXT; reference context |
| DOC-002 | 24 | Usable; references | — | NO_OCR_USABLE_TEXT; reference context |
| DOC-002 | 25 | Usable; references | — | NO_OCR_USABLE_TEXT; reference context |
| DOC-003 | 1 | Usable; supplement contents and evidence-unit index | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 2 | Usable; eTable 1 clustered outcome analysis values, CIs, and P values | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 3 | Usable; eTable 1 footnotes, clustering method, outcome definitions | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 4 | Usable; eFigure 1 description and hazard ratio/CI | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 5 | Usable; eFigure 2 procedure labels and measured distances/angles | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 6 | Usable; interim-analysis plan and observed enrollment/success counts | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 7 | Usable; data-form variable labels and indication categories | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 8 | Usable; data-form preoxygenation categories | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 9 | Usable; data-form medication and procedural variable labels | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 10 | Usable; first-attempt start/end and device fields | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 11 | Usable; intubating-condition and second-attempt fields | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 12 | Usable; success/switch outcome fields | Yes | NO_OCR_USABLE_TEXT |
| DOC-003 | 13 | Usable; complication fields | Yes | NO_OCR_USABLE_TEXT |

## Result-display/table and figure availability

| Source ID | Freshly available structured display or figure evidence |
|---|---|
| DOC-001 | Figure 1 (page 4); Table 1 (page 5); Table 2 (page 6); Table 3 (page 7); Table 4 (page 8); Table 5 (page 9); related results/subgroup narrative (pages 5-10). |
| DOC-002 | No trial-result table. Fresh protocol text supplies outcome definitions (pages 9-10), procedures/population definitions (pages 11-18), and planned statistical/interim-analysis methods (pages 19-21). |
| DOC-003 | eTable 1 and footnotes (pages 2-3); eFigure 1 (page 4); eFigure 2 (page 5); interim analysis (page 6); postintubation data-form sections (pages 7-13). |
