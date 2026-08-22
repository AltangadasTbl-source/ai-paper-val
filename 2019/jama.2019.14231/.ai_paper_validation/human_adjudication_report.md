# Human Adjudication Report

**Package:** `jama.2019.14231`  
**Disposition:** 3 retained issues (all Minor); 1 candidate rejected as insufficiently document-grounded. This report is limited to the supplied PDFs and page-linked derived artifacts; no external information was used. It is not a legal opinion.

## Scope and preprocessing provenance

- **Scientific scope:** `jama2019-14231-main-article` (12/12 PDF pages); `jama2019-14231-supplement-1` (results pages 6-20; page 1 inventory only); `jama2019-14231-supplement-2` (protocol; **Not Audited by Design** for scientific checks).
- **Text/OCR:** native PDF text was used for scoped pages. OCR backend selection is recorded in `.ai_paper_validation/preprocessing/ocr_backend.json`: RapidOCR CPU (`CPUExecutionProvider`; CUDA unavailable). One OCR cross-check was performed on main-article PDF p. 3 participant-flow diagram; all other scoped pages had satisfactory native text. Page-level provenance is in `.ai_paper_validation/preprocessing/page_manifest.json`.
- **Source preservation:** source PDFs were not modified. Per-document inventory, rights, scope, processing, and agent records remain under `.ai_paper_validation/document_outputs/`.

## Scientific issues for human adjudication

### 1. Table 2 absolute risk differences do not reproduce from displayed incidences

**Issue statement:** Five Table 2 absolute 8-year risk-difference point estimates conflict with the displayed nonsurgical-control minus metabolic-surgery incidences required by the table footnote, so the printed point estimates cannot be reproduced from the reported inputs.

**Category / severity:** Arithmetic inconsistency / Minor.

**Evidence:**

- **Reported incidence inputs and differences** — `jama2019-14231-main-article`, `jama_aminian_2019_oi_190103.pdf`, PDF p. 7 (printed p. 1277), Table 2, rows Heart failure, Coronary artery disease, Cerebrovascular disease, Nephropathy, and Atrial fibrillation; columns “Cumulative Incidence at 8 y” and “Absolute 8-Year Risk Difference.”
- **Rule** — same table, footnote a: “difference in 8-year absolute risk (nonsurgical control group − metabolic surgery).”
- **Repeated inputs** — `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF p. 7, eTable 5, Year 8 Surgical Group and Nonsurgical Group columns, same five rows.

| Row | Reported surgical / nonsurgical | Reported risk difference | Comparator calculation | Discrepancy |
|---|---:|---:|---:|---:|
| Heart failure | 6.8% / 18.9% | 12.9% (95% CI, 10.4-15.1) | 18.9 − 6.8 = 12.1 percentage points | reported +0.8 pp |
| Coronary artery disease | 7.9% / 11.6% | 4.2% (95% CI, 1.9-6.8) | 11.6 − 7.9 = 3.7 pp | reported +0.5 pp |
| Cerebrovascular disease | 4.1% / 5.6% | 1.8% (95% CI, −0.03 to 3.4) | 5.6 − 4.1 = 1.5 pp | reported +0.3 pp |
| Nephropathy | 6.1% / 16.3% | 11.1% (95% CI, 8.8-13.6) | 16.3 − 6.1 = 10.2 pp | reported +0.9 pp |
| Atrial fibrillation | 7.9% / 13.6% | 6.5% (95% CI, 4.4-8.7) | 13.6 − 7.9 = 5.7 pp | reported +0.8 pp |

**Reproducible calculation:** the two incidences and the reported difference are each displayed to 0.1 pp. Allowing ordinary independent rounding of all three displayed values gives a conservative tolerance of **less than 0.2 pp** for the difference between the printed subtraction and the printed risk-difference estimate. Observed gaps are 0.8, 0.5, 0.3, 0.9, and 0.8 pp; none is reconciled by that tolerance.

**Bounded impact:** These five Table 2 point estimates need confirmation or correction. The evidence does not establish which underlying estimate is correct or that incidences, CIs, HRs, or association direction are wrong.

**Verification instruction:**

1. Transcribe the five incidence pairs, adjacent differences, and footnote a from main-article PDF p. 7; subtract surgical from nonsurgical, allowing <0.2 pp rounding tolerance across the three displayed values.
2. Confirm the same pairs in Supplement 1 PDF p. 7 eTable 5.
3. Confirm the issue if the five gaps remain and no documented additional estimand explains them; author calculation output identifying such an estimand would resolve it.

### 2. Time-varying-HR narrative cross-references the wrong eTable

**Issue statement:** The supplement directs readers to eTable 4 for time-varying adjusted HRs and CIs at 2, 5, and 8 years, but those results are in eTable 7, obstructing verification of the stated results.

**Category / severity:** Presentation inconsistency / Minor.

**Evidence:**

- **Narrative** — `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF p. 19, section B, Time-varying hazard ratios: “eTable 4 displays adjusted hazard ratios and 95% confidence intervals at 2, 5, and 8 years after the index date.”
- **Cited table** — same document, PDF p. 6, eTable 4 title: “Cause-Specific Event Rates (%) per 100 Patient-Years of Follow-up at 8 Years”; columns provide surgical/nonsurgical rates and event-rate differences.
- **Matching table** — same document, PDF pp. 10 and 19, eTable 7 title: “Time-Varying Hazard Ratios and 95% CIs at 2, 5, and 8 Years After the Index Date.” Its Primary row reports 0.57 (0.49, 0.65), 0.78 (0.66, 0.93), and 0.79 (0.64, 0.97).

**Direct comparison / logical chain:** required features are adjusted HRs + 95% CIs + 2/5/8-year time points. eTable 4 has event rates at 8 years only; eTable 7 contains all required features. Therefore, the narrative reference should be eTable 7.

**Bounded impact:** The cross-reference needs correction; the time-varying HR values remain available in eTable 7 and are not shown to be numerically wrong.

**Verification instruction:**

1. Compare the p. 19 reference sentence with eTable 4 (p. 6) and eTable 7 (pp. 10, 19).
2. Confirm the issue if only eTable 7 has the stated HR/CI/time-point structure; changing “eTable 4” to “eTable 7” resolves it.

### 3. E-value interpretation labels the six-component primary endpoint “5-component MACE”

**Issue statement:** The supplement calls the E-value’s primary endpoint “5-component MACE,” while the main article defines the corresponding primary composite as six outcomes, creating endpoint-label ambiguity.

**Category / severity:** Presentation inconsistency / Minor.

**Evidence:**

- **E-value wording** — `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF p. 19, section C, E-Value: “the calculated E-value of 2.15 would mean that residual confounding could explain the observed association if there exists an unmeasured covariate having a relative risk association at least as large as 2.15 with both 5-component MACE and with metabolic surgery.” The preceding paragraph identifies the “primary outcome,” HR 0.61 (95% CI 0.55-0.69), and primary-endpoint E-value 2.15.
- **Table label** — same document, PDF p. 20, eTable 12, “Primary composite” row: E-values 2.15 and 1.92.
- **Primary-endpoint definition** — `jama2019-14231-main-article`, `jama_aminian_2019_oi_190103.pdf`, PDF p. 3 (printed p. 1273), “Primary and Secondary End Points”: “The primary end point was the incidence of extended major adverse cardiovascular events (MACE, composite of 6 outcomes),” followed by all-cause mortality, coronary artery events, cerebrovascular events, heart failure, nephropathy, and atrial fibrillation.

**Direct comparison / logical chain:** the specified primary composite has six named components; the E-value text connects 2.15 to the primary HR/endpoint but calls it five-component MACE. The supplied results material identifies no separate five-component endpoint for this E-value.

**Bounded impact:** The endpoint label needs confirmation or clarification. This evidence does not alter the reported primary HR, CI, event counts, or defined six-component composite.

**Verification instruction:**

1. Confirm “composite of 6 outcomes” and count the listed components on main-article PDF p. 3.
2. Confirm “5-component MACE,” its link to HR 0.61/E-value 2.15 (Supplement 1 p. 19), and the “Primary composite” row (p. 20).
3. Confirm the issue unless the authors identify a distinct five-component endpoint and calculation; otherwise, replacing the phrase with the defined six-component primary composite resolves it.

## Rejected candidate (not a scientific issue)

**Primary-composite E-values — Rejected / insufficiently document-grounded.** The package reports HR 0.61 (95% CI, 0.55-0.69) and E-values 2.15/1.92 (`jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF pp. 9, 19-20; eTable 6, section C, eTable 12). A candidate calculation derived 2.66/2.26 using a transformation inferred from other rows, but the supplied material does not state that formula, require a common HR-to-risk-ratio treatment for every endpoint, or provide primary-row calculation output. **Missing evidence:** a supplied formula/analysis specification requiring that transformation, or author calculation output with exact inputs and transformation. Accordingly, the package does not establish an inconsistency; this does not affirm that the reported E-values are correct.

## AI Training Restriction Summary

This separate screen records supplied-material evidence only and is not legal advice or a scientific issue list.

| Document ID / filename | Status | Exact evidence location and quoted language | Human Compliance Review |
|---|---|---|---|
| `jama2019-14231-main-article` / `jama_aminian_2019_oi_190103.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1 and 12; recurring footer pp. 1-12: “© 2019 American Medical Association. All rights reserved.” Embedded XMP metadata screened; no AI-training, fine-tuning, model-improvement, rights, permissions, or TDM statement located. | No |
| `jama2019-14231-supplement-1` / `joi190103supp1_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1 and 20; recurring footer pp. 1-20: “© 2019 American Medical Association. All rights reserved.” Embedded XMP metadata screened; no AI-training, fine-tuning, model-improvement, rights, permissions, or TDM statement located. | No |
| `jama2019-14231-supplement-2` / `joi190103supp2_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1 and 7 and embedded XMP (document-information and `pdfx:Company` fields): no copyright, license, rights-and-permissions, terms, TDM, AI-use, AI-training, fine-tuning, or model-improvement statement located. | No |

The general copyright footers do not expressly address AI training and are not treated here as an AI-training restriction, permission, or condition. Silence is not treated as permission. The supplied workflow assumption that AI-training permissions have been given is operational only and does not change these source-language records.
