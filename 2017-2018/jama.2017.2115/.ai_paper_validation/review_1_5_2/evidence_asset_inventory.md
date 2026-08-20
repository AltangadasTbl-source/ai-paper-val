# Fresh Evidence-Asset Inventory

## Scope and integrity

This inventory covers only the three direct supplied PDFs. Existing audit derivatives were not inspected or used as evidence. The direct-source hashes were recorded before preprocessing in `source_hashes_before.sha256`; no source was modified. All 28 PDF pages were freshly inspected through the newly created native and layout text assets and classified below.

## Tools and commands

| Tool | Version observed | Use |
|---|---|---|
| `pdfinfo` | 26.01.0 | PDF metadata and page-count confirmation |
| `pdftotext` | 26.01.0 | Native and `-layout` text extraction |
| `pdftoppm` | 26.01.0 | 200-dpi PNG rendering of result-relevant pages |
| `tesseract` | 5.5.0 | Direct CPU OCR only for unusable relevant native/layout text |

Commands executed, with paths relative to the package root:

```text
pdfinfo jama_lappe_2017_oi_170019.pdf
pdfinfo joi170019supp1_prod.pdf
pdfinfo joi170019supp2_prod.pdf
pdftotext jama_lappe_2017_oi_170019.pdf .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-001.txt
pdftotext -layout jama_lappe_2017_oi_170019.pdf .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-001.txt
pdftotext joi170019supp1_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-002.txt
pdftotext -layout joi170019supp1_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-002.txt
pdftotext joi170019supp2_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-003.txt
pdftotext -layout joi170019supp2_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-003.txt
pdftoppm -r 200 -f 1 -l 9 -png jama_lappe_2017_oi_170019.pdf .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001
pdftoppm -r 200 -f 1 -l 12 -png joi170019supp1_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002
pdftoppm -r 200 -f 1 -l 6 -png joi170019supp2_prod.pdf .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003
tesseract .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-6.png .ai_paper_validation/review_1_5_2/preprocessing/ocr_text/DOC-003-6 -l eng --psm 6
```

## Assets by direct source

### DOC-001 — `jama_lappe_2017_oi_170019.pdf`

- Role/type/metadata: main randomized clinical-trial article; PDF 1.4; 445614 bytes; 10 letter pages; not encrypted; producer `iTextSharp.LGPLv2.Core 3.7.4.0`.
- SHA-256: `af73f4f45ba4d330b06c21d0ac4a54c9069641578aa7a5f8063f4160af49c34d`.
- Fresh text assets: `preprocessing/native_text/DOC-001.txt` (53824 bytes) and `preprocessing/layout_text/DOC-001.txt` (86066 bytes). Native and layout extraction were usable for every page, including tables and figures; no OCR was required.
- Fresh renderings: `preprocessing/rendered_pages/DOC-001-01.png` through `preprocessing/rendered_pages/DOC-001-09.png` at 200 dpi. Page 10 is a reference-only page; it was text-inspected and classified but not result-relevant for rendering.

| PDF page | Fresh classification and method | Limitation |
|---:|---|---|
| 1 | Abstract and primary quantitative/statistical results; native and layout text usable; rendered. | None material. |
| 2 | Background, methods, eligibility, intervention, and analytic definitions that contextualize reported results; native and layout text usable; rendered. | None material. |
| 3 | Methods, adherence, outcome ascertainment, and statistical-analysis definitions; native and layout text usable; rendered. | None material. |
| 4 | Participant-flow figure and results narrative; native and layout text usable; rendered for visual flow verification. | None material. |
| 5 | Tables 1 and 2 baseline/follow-up quantitative displays; layout text usable; rendered for table alignment. | Visual table confirmation required during mapping. |
| 6 | Figure 2 and cancer-incidence results narrative/table continuation; native and layout text usable; rendered. | Visual figure-axis confirmation required during mapping. |
| 7 | Table 3 cancer-site counts and results narrative; layout text usable; rendered for table alignment. | Visual table confirmation required during mapping. |
| 8 | Discussion with reported post hoc results and effect estimates; native and layout text usable; rendered. | None material. |
| 9 | Limitations/conclusion and quantitative contextual statements; native and layout text usable; rendered. | None material. |
| 10 | References only; native and layout text usable; classified as non-result-relevant. | Not rendered because it contains no reported result display. |

### DOC-002 — `joi170019supp1_prod.pdf`

- Role/type/metadata: supporting protocol/research-design document; PDF 1.5; 418595 bytes; 12 letter pages; not encrypted; tagged PDF; producer `Microsoft Word 2010`.
- SHA-256: `a2782a096e4690f29d9fefa4522d19745b42dc047da7ae00c142f6bad6736d69`.
- Fresh text assets: `preprocessing/native_text/DOC-002.txt` (51889 bytes) and `preprocessing/layout_text/DOC-002.txt` (54564 bytes). Native and layout extraction were usable for all pages. No OCR was required.
- Fresh renderings: `preprocessing/rendered_pages/DOC-002-01.png` through `preprocessing/rendered_pages/DOC-002-12.png` at 200 dpi. Every page was treated as potentially result-relevant because it supplies quantitative design, projected retention/power, outcome, or analysis definitions that can be matched to article results.

| PDF page | Fresh classification and method | Limitation |
|---:|---|---|
| 1 | Trial design, planned allocation, intervention, follow-up, and nested case-control definition; text usable; rendered. | None material. |
| 2 | Table 4 projected recruitment/retention timeline and visit totals; layout text usable; rendered for table alignment. | Wide table requires visual confirmation during mapping. |
| 3 | Sample-size/power assumptions; Tables 5 and 6 quantitative displays; layout text usable; rendered. | Table 6 continues on p. 4. |
| 4 | Table 6 continuation, power narrative, and recruitment counts; text usable; rendered. | Table continuation must be read with p. 3. |
| 5 | Cancer ascertainment and validation-count definitions; text usable; rendered. | None material. |
| 6 | Assessment and longitudinal measurement definitions; text usable; rendered. | None material. |
| 7 | Planned intervention, dosage, and adherence definitions; text usable; rendered. | None material. |
| 8 | Planned time-to-event endpoint and analysis methods; text usable; rendered. | None material. |
| 9 | Interim-analysis and type-I-error/power statements; text usable; rendered. | None material. |
| 10 | Secondary outcomes and data-management quantitative definitions; text usable; rendered. | None material. |
| 11 | Screening/stratification and analytic covariate details; text usable; rendered. | None material. |
| 12 | Rationale and base-rate/dose statements; text usable; rendered. | None material. |

### DOC-003 — `joi170019supp2_prod.pdf`

- Role/type/metadata: supplementary online figures and post hoc statistical-analysis material; PDF 1.6; 249374 bytes; 6 letter pages; not encrypted; optimized; producer `Microsoft Word 2010`.
- SHA-256: `4c6200e596fdd764522785ef39e620cc6fb0ea725877a9339edbc829bf32fab2`.
- Fresh text assets: `preprocessing/native_text/DOC-003.txt` (4890 bytes) and `preprocessing/layout_text/DOC-003.txt` (5047 bytes). Pages 1-5 had usable native/layout text. Page 6 had usable body text but corrupted glyph encodings in headings; its 200-dpi rendering was directly OCRed on CPU as a targeted corroborating asset.
- Fresh renderings: `preprocessing/rendered_pages/DOC-003-1.png` through `preprocessing/rendered_pages/DOC-003-6.png` at 200 dpi. Fresh OCR asset: `preprocessing/ocr_text/DOC-003-6.txt` (2357 bytes), generated with English language data and PSM 6.

| PDF page | Fresh classification and method | Limitation |
|---:|---|---|
| 1 | Supplement contents/figure index; text usable; rendered. | No numeric result display beyond scope index. |
| 2 | eFigure 1 post hoc Kaplan-Meier description, exclusions, follow-up, and number-at-risk figure; text usable; rendered. | Plot/numbers-at-risk require visual confirmation during mapping. |
| 3 | eFigure 2A residual plot and serum-level range; text usable; rendered. | Figure coordinates require visual confirmation during mapping. |
| 4 | eFigure 2B coefficient, P value, hazard ratio, and interval; text usable; rendered. | Figure presentation requires visual confirmation during mapping. |
| 5 | eFigure 2C rescaled hazard-ratio plot; text usable; rendered. | Figure coordinates require visual confirmation during mapping. |
| 6 | Post hoc statistical-analysis narrative and references; native/layout body text usable, but heading glyph encoding was corrupted; rendered and CPU OCRed. | OCR repeats some decorative heading glyph errors; use the rendered page plus usable body text for exact reading. |

## Preprocessing limitation summary

No tools were missing, no Office source was supplied, no Office conversion was applicable, and no GPU was probed or used. The only extraction limitation is DOC-003 p. 6 heading-glyph corruption in native/layout text; the underlying body text remains usable and a targeted CPU OCR asset and page rendering are available. Table/figure geometry is preserved by the listed PNG renderings for the mapper to verify rather than inferred from linear text order.
