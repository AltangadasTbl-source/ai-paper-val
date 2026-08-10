# Critic Review of Verified Findings

## Scope

This critique reviewed only the eight findings classified as `Verified` in
`.ai_paper_validation/evidence_verifier.md`: TA-001, TA-002, statistical candidates
1/2/3, and FF-01/02/03. No new issue search or external-information review was
performed.

For this review, `Major` denotes an inconsistency that can materially reverse or
misstate the reported interpretation or analysis population. `Minor` denotes a
localized numeric, abbreviation, or covariate-label inconsistency whose impact is
bounded and does not establish that the underlying effect estimate is wrong.

## Decisions

| Verifier card | Parent candidate | Decision | Final severity | Concise rationale |
|---|---|---|---|---|
| V-01 | TA-001 | Accepted | Minor | The displayed count, column total, and percentage are directly documented and fail to reproduce at the table's precision. The unavailable row-specific denominator limits the conclusion to a displayed arithmetic/denominator-reporting inconsistency, which the card states. |
| V-02 | TA-002 | Accepted | Minor | The as-treated column identifies `N=170`, but `100/170` rounds to 58.8%, not the displayed 59.5%; no different denominator is reported. The card does not speculate about which element is wrong. |
| V-03 | Statistical candidate 1 | Accepted | Major | The sentence labelled follow-up imaging exactly reproduces the randomization-modality counts (328 CT and 8 MR DWI), while the package separately reports 204 patients with MR-DWI follow-up. This is document-grounded and materially misstates the apparent follow-up population. |
| V-04 | Statistical candidate 2 | Accepted | Minor | The main text and explicitly cited eTable 11 report different upper quartiles (125 vs 135 mL) for the same group and measure; the 10-mL difference is direct and localized. |
| V-05 | Statistical candidate 3 | Accepted | Minor | The expansion `absolute risk reduction` conflicts internally with the modified-Poisson method, ratio-scale null of 1 stated in the table footnote, and the separately defined `aRD`. The exact intended ratio expansion need not be inferred to establish the label inconsistency. |
| V-06 | FF-01 | Accepted | Major | The main text says both favorable-outcome probabilities increase with mismatch volume under EVT, whereas both cited EVT curves decline as mismatch volume increases. The contradiction reverses the reported direction of the modeled association. |
| V-07 | FF-02 | Accepted | Major | For the adverse mRS 5-6 outcome, eFigure 13 labels RR values below 1 as favoring medical management even though the displayed risks and same-outcome eFigure 9 show that side favors thrombectomy. The annotations invert the figure's interpretation. |
| V-08 | FF-03 | Accepted | Minor | eFigure 18, eFigure 19, and the main text inconsistently identify the fixed covariate as CTP/MRI core or composite core, variables the supplement defines differently. The inconsistency is certain, although the correct model input is not available. |

**Accepted:** 8. **Rejected:** 0. **Uncertain:** 0.

No accepted cards are duplicative: V-01 and V-02 concern different analysis
populations and different nonreproducing percentages; the remaining cards concern
distinct statements, values, figures, or model labels.

## Final accepted evidence cards

### C-01 — Main Table 1 general-anesthesia percentage does not reproduce from the displayed EVT total

- **Category / severity:** Arithmetic inconsistency / Minor
- **Issue statement:** Main Table 1 reports 100 EVT patients as 59.9%, although the displayed EVT total of 168 yields 59.5% to one decimal.
- **Reported item:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 5, Table 1, column `Endovascular thrombectomy (n = 168)`, row `General anesthesia used`: **`100 (59.9)`**.
- **Comparator and calculation:** The column header gives **`n = 168`** and no row-specific denominator. `100/168 × 100 = 59.5238%`, which rounds to **59.5%**, 0.4 percentage points below the displayed 59.9%. The displayed percentage would correspond to the unstated denominator 167 (`100/167 × 100 = 59.8802%`).
- **Bounded impact:** One baseline percentage is not reproducible from the displayed denominator. The evidence does not determine whether the percentage is wrong or a nonmissing denominator was omitted; it does not challenge the count or any outcome.
- **Human verification:**
  1. Confirm the Table 1 EVT header, row count, and percentage on PDF p. 5.
  2. Recalculate `100/168 × 100` to one decimal.
  3. Confirm the finding if no row denominator of 167 is documented; such a denominator would resolve the arithmetic issue but confirm a denominator-presentation omission.

### C-02 — Supplement eTable 1 general-anesthesia percentage does not reproduce from the displayed as-treated EVT total

- **Category / severity:** Arithmetic inconsistency / Minor
- **Issue statement:** Supplement eTable 1 reports 100 as-treated EVT patients as 59.5%, although the displayed EVT total of 170 yields 58.8% to one decimal.
- **Reported item:** DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF pp. 35-36, eTable 1, column `Endovascular thrombectomy N=170`, row `General Anesthesia Used`: **`100 (59.5%)`**.
- **Comparator and calculation:** No row-specific denominator is reported in the table or its footnotes. `100/170 × 100 = 58.8235%`, which rounds to **58.8%**, 0.7 percentage points below 59.5%. The displayed percentage corresponds to the unstated denominator 168 (`100/168 × 100 = 59.5238%`).
- **Bounded impact:** The discrepancy is limited to one baseline percentage and does not establish whether the count, percentage, or omitted denominator requires correction.
- **Human verification:**
  1. Confirm `N=170` on PDF p. 35 and `100 (59.5%)` on PDF p. 36.
  2. Recalculate `100/170 × 100` to one decimal.
  3. Confirm the finding if no row denominator of 168 is documented; such documentation would resolve the arithmetic issue but confirm a denominator-presentation omission.

### C-03 — A sentence labelled follow-up imaging reproduces randomization-imaging counts

- **Category / severity:** Presentation inconsistency / Major
- **Issue statement:** The Results section labels 8 MRI and 328 CT examinations as follow-up imaging, but those exact counts are the modalities used to determine core at randomization and the package reports a separate 204-patient MR-DWI follow-up cohort.
- **Reported item:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 4, Results, second paragraph: **“Follow-up imaging modality was MRI in 8 of 336 patients (2%) and CT in 328 of 336 patients (98%).”**
- **Comparators:** DOC-001-MAIN PDF p. 5, Table 1, `Imaging modality used to determine ischemic core volume at randomization`: CT perfusion **165 EVT + 163 medical care** and MR DWI **3 EVT + 5 medical care**. DOC-001-MAIN PDF p. 9 reports **“MR diffusion follow-up (n = 204 [61%])”**. DOC-006-RESULTS-SUPP PDF p. 51, eTable 11, `patients with MR DWI follow-up`, gives **MM N=101**, **mTICI 0-2a N=24**, and **mTICI 2b-3 N=79**.
- **Logical chain:** `165+163=328` CT and `3+5=8` MR DWI at randomization; `101+24+79=204` MR-DWI follow-up. The p. 4 values reproduce the randomization modality counts and conflict with the documented follow-up cohort.
- **Bounded impact:** The time-point label can make the MRI follow-up population appear to contain 8 rather than 204 patients. It does not alter the displayed infarct-growth estimates.
- **Human verification:**
  1. Confirm the p. 4 sentence.
  2. Sum the randomization-modality cells in Table 1 on p. 5.
  3. Confirm `n=204` on main PDF p. 9 and `101+24+79=204` in supplement eTable 11 on p. 51.
  4. The finding is confirmed if the p. 4 sentence remains labelled follow-up imaging.

### C-04 — Medical-management infarct-growth upper quartile is 125 mL in the main article and 135 mL in eTable 11

- **Category / severity:** Cross-document inconsistency / Minor
- **Issue statement:** For the same medical-management MR-DWI follow-up group and infarct-growth measure, the main article reports an upper quartile of 125 mL while the cited supplement reports 135 mL.
- **Reported item:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 9, `Association of Follow-Up Infarct Volume and Infarct Growth With EVT Outcomes`: medical management **`median, 95 [IQR, 56-125] mL`**, with citation to eTable 11.
- **Comparator:** DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 51, eTable 11, MM `N=101`, row `Infarct growth from CTP/MRI core (ml), median (IQR)`: **`95 (56, 135)`** mL.
- **Calculation:** The group, measure, median, and lower quartile match. The upper quartiles differ by `135−125 = 10 mL`.
- **Bounded impact:** Only the upper quartile of this descriptive distribution is inconsistent; the median, lower quartile, and adjacent reperfusion-group values agree.
- **Human verification:**
  1. Confirm `95 [IQR, 56-125] mL` on main PDF p. 9.
  2. Confirm `95 (56, 135)` in the MM column of supplement eTable 11 on PDF p. 51.
  3. Confirm both identify infarct growth from baseline CTP/MRI core in the MR-DWI follow-up group.

### C-05 — `aRR` is expanded as “absolute risk reduction” for a ratio measure

- **Category / severity:** Presentation inconsistency / Minor
- **Issue statement:** The article expands `aRR` as “absolute risk reduction,” although its method, values, footnotes, and separately reported `aRD` identify it as a multiplicative ratio measure.
- **Reported items:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 6: **“Functional independence (absolute risk reduction [aRR], 0.89 [95% CI, 0.84-0.95] per 10-mL increase)”**; PDF p. 7, Table 2 abbreviations, and p. 9, Table 3 abbreviations: **`aRR, absolute risk reduction`**.
- **Comparators:** DOC-001-MAIN PDF p. 4 says secondary outcomes used **“modified Poisson regression models with robust standard errors.”** Table footnotes on pp. 7 and 9 state **“aRR greater than 1 indicates higher rate ratio.”** Table 3 separately defines **`aRD, absolute risk difference`** and reports additive estimates such as `−0.001`.
- **Logical chain:** The footnote explicitly places `aRR` on a multiplicative ratio scale with null 1, while an absolute reduction/difference is additive with null 0; the separately reported `aRD` confirms that the two labels are not interchangeable.
- **Bounded impact:** The numeric estimates need not be wrong, but the expansion can cause a ratio such as 0.89 to be read as an absolute risk reduction. The package does not establish the exact wording intended for the ratio abbreviation.
- **Human verification:**
  1. Confirm the modified-Poisson method on p. 4 and the `absolute risk reduction` expansion on pp. 6, 7, and 9.
  2. Confirm the table footnotes call the measure a `rate ratio` and Table 3 separately reports `aRD`.
  3. The incompatible coexisting definitions confirm the presentation inconsistency.

### C-06 — Main text and eFigure 17 report opposite EVT directions for mismatch volume

- **Category / severity:** Statistical reporting inconsistency / Major
- **Issue statement:** The main article says functional-independence and independent-ambulation probabilities increase with mismatch volume in EVT recipients, but both EVT curves in the explicitly cited eFigure 17 decline as mismatch volume increases.
- **Reported item:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 8, `Association of Mismatch With EVT Treatment Effect and Functional Outcomes`: **“as mismatch volume increased, the marginal probability of functional independence and independent ambulation increased for patients receiving EVT but decreased in patients receiving medical management only (eFigure 17 in Supplement 5).”**
- **Comparator:** DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 23, eFigure 17. Panel A is probability of mRS 0-2, panel B probability of mRS 0-3, and the legend identifies teal as EVT. In both panels the EVT curve declines from left to right as mismatch volume increases; neither arm's favorable-outcome curve rises.
- **Logical chain:** An increasing modeled probability requires an upward slope over an increasing x-axis. Both plotted EVT slopes are negative, directly opposing the narrative direction.
- **Bounded impact:** The within-EVT direction of this modeled association is reported inconsistently. This finding does not invalidate the separate categorical mismatch treatment-effect estimates.
- **Human verification:**
  1. Read the quoted sentence on main PDF p. 8.
  2. Follow the EVT curves in supplement eFigure 17 panels A and B on PDF p. 23 from low to high mismatch volume.
  3. Confirm both curves decline; opposite text and plot directions confirm the issue.

### C-07 — eFigure 13 reverses favor-direction labels for the adverse mRS 5-6 outcome

- **Category / severity:** Presentation inconsistency / Major
- **Issue statement:** eFigure 13 labels relative risks below 1 as favoring medical management for complete dependence or death, although the displayed risks and same-outcome eFigure 9 show that this side favors thrombectomy.
- **Reported item:** DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 19, eFigure 13, `complete dependence or death (mRS 5-6)`: the below-1 side is labelled **`Favours Medical Management`** and the above-1 side **`Favours Thrombectomy`**.
- **Source values and comparator:** In eFigure 13, NCCT core `<70mL (n=132)` gives thrombectomy **`27 (39.71%)`**, medical management **`39 (60.94%)`**, and RR **`0.68 (0.49-0.95)`**, plotted below 1. DOC-006-RESULTS-SUPP PDF p. 15, eFigure 9, labels the below-1 side **`Favours Thrombectomy`** for the same mRS 5-6 outcome.
- **Logical chain:** The figure defines the RR as thrombectomy relative to medical management. For the adverse mRS 5-6 outcome, `39.71% < 60.94%` and RR `0.68 < 1`, so the below-1 side represents fewer adverse outcomes under thrombectomy. eFigure 13's favor labels are therefore reversed.
- **Bounded impact:** Point estimates and CIs remain visible, but the annotations invert the intended visual interpretation of all rows.
- **Human verification:**
  1. Confirm the outcome, favor labels, example percentages, and RR on supplement PDF p. 19.
  2. Compare the same-outcome labels in eFigure 9 on PDF p. 15.
  3. The opposite labels for the same adverse outcome confirm the issue.

### C-08 — Prediction figures and main text inconsistently identify the fixed core-volume covariate

- **Category / severity:** Cross-document inconsistency / Minor
- **Issue statement:** The prediction-figure text alternately identifies the fixed covariate as CTP/MRI core and composite core, while the main article describes the figure relationship using CTP/MRI core, so the reported model input is not consistently identified.
- **Reported items and comparators:**
  - DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 24, eFigure 18 title: **“with CTP/MRI core volume set at a) 70ml, b) 100ml and c) 150ml”**; its explanatory text instead says **“composite core volume estimates.”**
  - DOC-006-RESULTS-SUPP PDF p. 25, eFigure 19 title and body specify **“composite core volume”** at 70, 100, and 150 mL.
  - DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 10, after citing eFigures 18 and 19: **“The relationship was consistent across estimated CT perfusion/MRI core volumes set at 70 mL, 100 mL, and 150 mL.”**
  - The panel strips on supplement pp. 24-25 say only **`Core Volume 70`**, **`Core Volume 100`**, and **`Core Volume 150`**.
- **Logical chain:** DOC-006-RESULTS-SUPP PDF p. 37, eTable 1 footnote, defines composite core as **“the larger of CTP/MRI core volume and CT hypodensity volume estimates.”** Composite and CTP/MRI core are therefore distinct variables, but the cited labels assign both to the prediction figures.
- **Bounded impact:** Readers cannot determine from the reported labels which core estimate was held fixed, especially for eFigure 19. The evidence does not establish that the plotted probabilities are numerically wrong or which label is correct.
- **Human verification:**
  1. Compare the eFigure 18 title and explanatory text on supplement PDF p. 24.
  2. Compare eFigure 19 on supplement PDF p. 25 with the main-text statement on main PDF p. 10.
  3. Confirm on supplement PDF p. 37 that composite core is defined as a distinct larger-of-two estimate.
  4. The conflicting labels confirm the reporting issue; model output is needed only to identify the correct label.
