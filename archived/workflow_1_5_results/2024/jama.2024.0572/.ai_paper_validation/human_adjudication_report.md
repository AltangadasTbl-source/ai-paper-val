# Human Adjudication Report — JAMA 2024.0572

**Package status:** 7 supplied PDFs preserved unchanged; 2 documents scientifically audited (main article and results supplement); 5 documents **Not Audited by Design**. Eight accepted issues are submitted for **Human Adjudication** (3 Major; 5 Minor). This report contains only accepted, document-grounded findings; it is not a legal opinion.

## Source-package processing status

| Document ID | Filename | Classification | Scientific-audit scope / processing status |
|---|---|---|---|
| DOC-001-MAIN | `jama_sarraj_2024_oi_240006_1708623114.96234.pdf` | Main article | PDF pp. 1-14; preprocessing and scientific audit complete. |
| DOC-002-ADMIN-COLLAB | `joi240006supp1_prod_1708623114.97236.pdf` | Administrative material | **Not Audited by Design**; inventory and rights screen complete. |
| DOC-003-PROTOCOL | `joi240006supp2_prod_1708623114.99233.pdf` | Protocol | **Not Audited by Design**; inventory and rights screen complete. |
| DOC-004-SAP-TRIAL | `joi240006supp3_prod_1708623114.99733.pdf` | Statistical analysis plan | **Not Audited by Design**; inventory and rights screen complete. |
| DOC-005-SAP-ANALYSIS | `joi240006supp4_prod_1708623115.00733.pdf` | Statistical analysis plan | **Not Audited by Design**; inventory and rights screen complete. |
| DOC-006-RESULTS-SUPP | `joi240006supp5_prod_1708623115.01733.pdf` | Results supplement | PDF pp. 1-53; preprocessing and scientific audit complete. OCR-required pages were rendered for visual review; no OCR output was available. |
| DOC-007-ADMIN-DATA | `joi240006supp6_prod_1708623115.02733.pdf` | Administrative material | **Not Audited by Design**; inventory and rights screen complete. |

## Scientific evidence cards

### 1. Main Table 1 general-anesthesia percentage does not reproduce from the displayed EVT total

**Category / severity:** Arithmetic inconsistency / Minor  
**Issue statement:** Main Table 1 reports 100 EVT patients as 59.9%, although the displayed EVT total of 168 yields 59.5% to one decimal.

**Evidence — reported item:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 5, Table 1, column `Endovascular thrombectomy (n = 168)`, row `General anesthesia used`: **`100 (59.9)`**.

**Comparison:** Reported percentage: 59.9%. Comparator: `100/168 × 100 = 59.5238%`, rounded to one decimal = **59.5%**. Discrepancy: reported value is **0.4 percentage points higher**. No row-specific denominator is displayed; 59.9% corresponds to an unstated denominator of 167 (`100/167 × 100 = 59.8802%`).

**Reproducible calculation:** Inputs: count 100; displayed column total 168. Formula: `(100 ÷ 168) × 100`. Result: 59.5238%; rounding tolerance: nearest 0.1 percentage point; expected displayed value 59.5%.

**Bounded impact:** One baseline percentage is not reproducible from the displayed denominator. The evidence does not determine whether the percentage is wrong or a nonmissing denominator was omitted; it does not challenge the count or any outcome.

**Verification instruction:**

1. Confirm the Table 1 EVT header, row count, and percentage on PDF p. 5.
2. Recalculate `100/168 × 100` to one decimal.
3. Confirm the finding if no row denominator of 167 is documented; that denominator would resolve the arithmetic issue but confirm a denominator-presentation omission.

### 2. Supplement eTable 1 general-anesthesia percentage does not reproduce from the displayed as-treated EVT total

**Category / severity:** Arithmetic inconsistency / Minor  
**Issue statement:** Supplement eTable 1 reports 100 as-treated EVT patients as 59.5%, although the displayed EVT total of 170 yields 58.8% to one decimal.

**Evidence — reported item:** DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF pp. 35-36, eTable 1, column `Endovascular thrombectomy N=170`, row `General Anesthesia Used`: **`100 (59.5%)`**.

**Comparison:** Reported percentage: 59.5%. Comparator: `100/170 × 100 = 58.8235%`, rounded to one decimal = **58.8%**. Discrepancy: reported value is **0.7 percentage points higher**. No row-specific denominator is reported in the table or footnotes; 59.5% corresponds to unstated denominator 168 (`100/168 × 100 = 59.5238%`).

**Reproducible calculation:** Inputs: count 100; displayed column total 170. Formula: `(100 ÷ 170) × 100`. Result: 58.8235%; rounding tolerance: nearest 0.1 percentage point; expected displayed value 58.8%.

**Bounded impact:** The discrepancy is limited to one baseline percentage and does not establish whether the count, percentage, or omitted denominator requires correction.

**Verification instruction:**

1. Confirm `N=170` on PDF p. 35 and `100 (59.5%)` on PDF p. 36.
2. Recalculate `100/170 × 100` to one decimal.
3. Confirm the finding if no row denominator of 168 is documented; such documentation would resolve the arithmetic issue but confirm a denominator-presentation omission.

### 3. A sentence labelled follow-up imaging reproduces randomization-imaging counts

**Category / severity:** Presentation inconsistency / Major  
**Issue statement:** The Results section labels 8 MRI and 328 CT examinations as follow-up imaging, but those exact counts are the modalities used to determine core at randomization and the package reports a separate 204-patient MR-DWI follow-up cohort.

**Evidence — reported item:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 4, Results, second paragraph: **“Follow-up imaging modality was MRI in 8 of 336 patients (2%) and CT in 328 of 336 patients (98%).”**

**Evidence — comparators:** DOC-001-MAIN, PDF p. 5, Table 1, `Imaging modality used to determine ischemic core volume at randomization`: CT perfusion **165 EVT + 163 medical care**; MR DWI **3 EVT + 5 medical care**. DOC-001-MAIN, PDF p. 9: **“MR diffusion follow-up (n = 204 [61%])”**. DOC-006-RESULTS-SUPP, PDF p. 51, eTable 11, `patients with MR DWI follow-up`: **MM N=101; mTICI 0-2a N=24; mTICI 2b-3 N=79**.

**Comparison and logical chain:** Reported follow-up counts: CT 328 and MRI 8. Randomization-modality comparator: `165+163=328` CT and `3+5=8` MR DWI. Separate follow-up comparator: `101+24+79=204` MR-DWI follow-up. The reported p. 4 values reproduce the randomization modality counts, while the documented follow-up cohort is 204.

**Bounded impact:** The time-point label can make the MRI follow-up population appear to contain 8 rather than 204 patients. It does not alter the displayed infarct-growth estimates.

**Verification instruction:**

1. Confirm the quoted p. 4 sentence.
2. Sum the randomization-modality cells in Table 1 on p. 5.
3. Confirm `n=204` on main PDF p. 9 and `101+24+79=204` in supplement eTable 11 on p. 51.
4. Confirm the issue if the p. 4 sentence remains labelled follow-up imaging.

### 4. Medical-management infarct-growth upper quartile is 125 mL in the main article and 135 mL in eTable 11

**Category / severity:** Cross-document inconsistency / Minor  
**Issue statement:** For the same medical-management MR-DWI follow-up group and infarct-growth measure, the main article reports an upper quartile of 125 mL while the cited supplement reports 135 mL.

**Evidence — reported item:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 9, section `Association of Follow-Up Infarct Volume and Infarct Growth With EVT Outcomes`: medical management **`median, 95 [IQR, 56-125] mL`**, with citation to eTable 11.

**Evidence — comparator:** DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 51, eTable 11, MM `N=101`, row `Infarct growth from CTP/MRI core (ml), median (IQR)`: **`95 (56, 135)` mL**.

**Comparison and calculation:** The group, measure, median (95 mL), and lower quartile (56 mL) match. Upper quartile: main article 125 mL; supplement 135 mL. Formula: `135 − 125`; discrepancy: **10 mL higher in the supplement**. No rounding tolerance is applicable because the values are reported as whole mL.

**Bounded impact:** Only the upper quartile of this descriptive distribution is inconsistent; the median, lower quartile, and adjacent reperfusion-group values agree.

**Verification instruction:**

1. Confirm `95 [IQR, 56-125] mL` on main PDF p. 9.
2. Confirm `95 (56, 135)` in the MM column of supplement eTable 11 on PDF p. 51.
3. Confirm both identify infarct growth from baseline CTP/MRI core in the MR-DWI follow-up group.

### 5. `aRR` is expanded as “absolute risk reduction” for a ratio measure

**Category / severity:** Presentation inconsistency / Minor  
**Issue statement:** The article expands `aRR` as “absolute risk reduction,” although its method, values, footnotes, and separately reported `aRD` identify it as a multiplicative ratio measure.

**Evidence — reported items:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 6: **“Functional independence (absolute risk reduction [aRR], 0.89 [95% CI, 0.84-0.95] per 10-mL increase)”**; PDF p. 7, Table 2 abbreviations, and PDF p. 9, Table 3 abbreviations: **`aRR, absolute risk reduction`**.

**Evidence — comparators:** DOC-001-MAIN, PDF p. 4: **“modified Poisson regression models with robust standard errors.”** Table footnotes on PDF pp. 7 and 9: **“aRR greater than 1 indicates higher rate ratio.”** PDF p. 9, Table 3 separately defines **`aRD, absolute risk difference`** and reports additive estimates such as **`−0.001`**.

**Comparison and logical chain:** Reported label: “absolute risk reduction.” Comparator: the footnote places aRR on a multiplicative ratio scale with null 1; an absolute reduction/difference is additive with null 0; separately reported aRD identifies the additive measure. These definitions are not interchangeable. No numerical recomputation or rounding tolerance applies.

**Bounded impact:** The numeric estimates need not be wrong, but the expansion can cause a ratio such as 0.89 to be read as an absolute risk reduction. The package does not establish the exact wording intended for the ratio abbreviation.

**Verification instruction:**

1. Confirm the modified-Poisson method on p. 4 and the `absolute risk reduction` expansion on pp. 6, 7, and 9.
2. Confirm the table footnotes call the measure a `rate ratio` and Table 3 separately reports `aRD`.
3. Confirm the presentation issue if the incompatible definitions coexist.

### 6. Main text and eFigure 17 report opposite EVT directions for mismatch volume

**Category / severity:** Statistical reporting inconsistency / Major  
**Issue statement:** The main article says functional-independence and independent-ambulation probabilities increase with mismatch volume in EVT recipients, but both EVT curves in the explicitly cited eFigure 17 decline as mismatch volume increases.

**Evidence — reported item:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 8, section `Association of Mismatch With EVT Treatment Effect and Functional Outcomes`: **“as mismatch volume increased, the marginal probability of functional independence and independent ambulation increased for patients receiving EVT but decreased in patients receiving medical management only (eFigure 17 in Supplement 5).”**

**Evidence — comparator:** DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 23, eFigure 17: panel A is probability of mRS 0-2; panel B is probability of mRS 0-3; legend identifies teal as EVT. In both panels the EVT curve declines from left to right as mismatch volume increases; neither arm’s favorable-outcome curve rises.

**Comparison and logical chain:** Reported direction for EVT: increasing. Comparator direction in both plotted EVT curves: declining over the increasing x-axis. Rule: an increasing modeled probability requires an upward slope as x increases. The narrative direction and plotted directions are opposite. No numeric rounding applies.

**Bounded impact:** The within-EVT direction of this modeled association is reported inconsistently. This finding does not invalidate the separate categorical mismatch treatment-effect estimates.

**Verification instruction:**

1. Read the quoted sentence on main PDF p. 8.
2. Follow the EVT curves in supplement eFigure 17 panels A and B on PDF p. 23 from low to high mismatch volume.
3. Confirm the issue if both curves decline while the text states they increase.

### 7. eFigure 13 reverses favor-direction labels for the adverse mRS 5-6 outcome

**Category / severity:** Presentation inconsistency / Major  
**Issue statement:** eFigure 13 labels relative risks below 1 as favoring medical management for complete dependence or death, although the displayed risks and same-outcome eFigure 9 show that this side favors thrombectomy.

**Evidence — reported item:** DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 19, eFigure 13, outcome `complete dependence or death (mRS 5-6)`: below-1 side labelled **`Favours Medical Management`**; above-1 side labelled **`Favours Thrombectomy`**.

**Evidence — source values and comparator:** DOC-006-RESULTS-SUPP, PDF p. 19, eFigure 13, NCCT core `<70mL (n=132)`: thrombectomy **`27 (39.71%)`**; medical management **`39 (60.94%)`**; RR **`0.68 (0.49-0.95)`**, plotted below 1. DOC-006-RESULTS-SUPP, PDF p. 15, eFigure 9, same mRS 5-6 outcome: below-1 side labelled **`Favours Thrombectomy`**.

**Comparison and logical chain:** eFigure 13 defines RR as thrombectomy relative to medical management. Inputs: 39.71% thrombectomy and 60.94% medical management. Rule: for an adverse outcome, fewer events favor the treatment with the lower risk. `39.71% < 60.94%` and RR `0.68 < 1`; thus below 1 represents fewer adverse outcomes under thrombectomy. eFigure 13's labels are opposite to this and to eFigure 9. No rounding tolerance affects the direction.

**Bounded impact:** Point estimates and CIs remain visible, but the annotations invert the intended visual interpretation of all rows.

**Verification instruction:**

1. Confirm the outcome, favor labels, example percentages, and RR on supplement PDF p. 19.
2. Compare the same-outcome labels in eFigure 9 on PDF p. 15.
3. Confirm the issue if the opposite labels remain for the same adverse outcome.

### 8. Prediction figures and main text inconsistently identify the fixed core-volume covariate

**Category / severity:** Cross-document inconsistency / Minor  
**Issue statement:** The prediction-figure text alternately identifies the fixed covariate as CTP/MRI core and composite core, while the main article describes the figure relationship using CTP/MRI core, so the reported model input is not consistently identified.

**Evidence — reported items and comparators:**

- DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 24, eFigure 18 title: **“with CTP/MRI core volume set at a) 70ml, b) 100ml and c) 150ml”**; explanatory text: **“composite core volume estimates.”**
- DOC-006-RESULTS-SUPP, PDF p. 25, eFigure 19 title and body: **“composite core volume”** at 70, 100, and 150 mL.
- DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 10, after citing eFigures 18 and 19: **“The relationship was consistent across estimated CT perfusion/MRI core volumes set at 70 mL, 100 mL, and 150 mL.”**
- DOC-006-RESULTS-SUPP, PDF pp. 24-25, panel strips: **`Core Volume 70`**, **`Core Volume 100`**, **`Core Volume 150`**.
- DOC-006-RESULTS-SUPP, PDF p. 37, eTable 1 footnote: composite core is **“the larger of CTP/MRI core volume and CT hypodensity volume estimates.”**

**Comparison and logical chain:** The figure/main-text labels assign CTP/MRI core and composite core to the prediction figures. The footnote defines composite core as a distinct larger-of-two estimate. Therefore the reported labels do not consistently identify the fixed model input. No calculation or rounding tolerance applies.

**Bounded impact:** Readers cannot determine from the reported labels which core estimate was held fixed, especially for eFigure 19. The evidence does not establish that the plotted probabilities are numerically wrong or which label is correct.

**Verification instruction:**

1. Compare the eFigure 18 title and explanatory text on supplement PDF p. 24.
2. Compare eFigure 19 on supplement PDF p. 25 with the main-text statement on main PDF p. 10.
3. Confirm on supplement PDF p. 37 that composite core is defined as a distinct larger-of-two estimate.
4. Confirm the reporting issue if the conflicting labels remain; model output is needed only to identify the correct label.

## AI Training Restriction Summary

This separate document-rights screen is not a scientific issue list and is not legal advice. It records only the supplied PDFs and embedded metadata. “No AI Training Restriction Located” does not imply permission.

| Document ID | Filename | Status | Exact evidence location and quotation/value | Human Compliance Review |
|---|---|---|---|---|
| DOC-001-MAIN | `jama_sarraj_2024_oi_240006_1708623114.96234.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1, bottom copyright line (repeated including p. 14): **“© 2024 American Medical Association. All rights reserved.”** XMP keywords/creator checked; no rights, license, permission, terms, TDM, or AI-use field. | No |
| DOC-002-ADMIN-COLLAB | `joi240006supp1_prod_1708623114.97236.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1-2 and 29-30; XMP metadata: no copyright, license, rights-and-permissions, terms, TDM, or AI-use language located; no applicable quotation. | No |
| DOC-003-PROTOCOL | `joi240006supp2_prod_1708623114.99233.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1-2 and 81-82; XMP metadata: no copyright, license, rights-and-permissions, terms, TDM, or AI-use language located; no applicable quotation. | No |
| DOC-004-SAP-TRIAL | `joi240006supp3_prod_1708623114.99733.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 2 diagonal watermark (also pp. 39-40): **“CONFIDENTIAL”**. It does not state an AI-training restriction or permission condition; document-info metadata has no such field. | Completed — confidentiality marking was recorded; user confirmed all permissions for this AI investigation on 2026-07-29. It is not classified as an AI-training restriction. |
| DOC-005-SAP-ANALYSIS | `joi240006supp4_prod_1708623115.00733.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1-2 and 6-7; XMP metadata: no copyright, license, rights-and-permissions, terms, TDM, or AI-use language located; no applicable quotation. | No |
| DOC-006-RESULTS-SUPP | `joi240006supp5_prod_1708623115.01733.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1-2 and 52-53; XMP metadata: no copyright, license, rights-and-permissions, terms, TDM, or AI-use language located; no applicable quotation. | No |
| DOC-007-ADMIN-DATA | `joi240006supp6_prod_1708623115.02733.pdf` | No AI Training Restriction Located in Provided Materials | Complete PDF p. 1 and document-info metadata: no copyright, license, rights-and-permissions, terms, TDM, or AI-use language located; no applicable quotation. | No |

**Submission status:** Submitted for Human Adjudication. Review the eight numbered scientific evidence cards and the separate rights-screen record for DOC-004-SAP-TRIAL.
