# Human Adjudication Report

## Package and processing scope

| Document ID | Filename | Classification and scientific scope |
|---|---|---|
| DOC-001 | `jama_butler_2020_oi_200054.pdf` | Main article; audited, PDF pp. 1–10. |
| DOC-002 | `joi200054supp1_prod.pdf` | Protocol; **Not Audited by Design** for scientific checks. |
| DOC-003 | `joi200054supp2_prod.pdf` | Results supplement; audited, PDF pp. 1–13. |
| DOC-004 | `joi200054supp3_prod.pdf` | Data Sharing Statement; **Not Audited by Design** for scientific checks. |

Native text was available for all supplied PDFs. Selective OCR used the CPU manifest: `rapidocr-cpu` (`CPUExecutionProvider`; CUDA unavailable). This report contains five accepted Minor findings and one separate Uncertain item; it makes no finding about unreported data or estimands.

## Scientific evidence cards

### 1. Placebo eTable 4 distribution has an incompatible percentage and total — Accepted

- **Category / severity:** Arithmetic inconsistency / Minor.
- **Issue statement:** In the placebo 3-month oral-candidiasis distribution, one displayed percentage does not match its fraction and the four category counts exceed their common denominator, so the distribution cannot be correct as printed.
- **Evidence:** **DOC-003, `joi200054supp2_prod.pdf`, PDF p. 7, eTable 4, 3-month section, Placebo column:** `(-/+) 20/119 (16.8)`, `(+) 20/119 (16.0)`, `(++) 38/119 (31.9)`, `(+++) 42/119 (35.3)`. The footnote says the levels are `(-/+)`, `(+)`, `(++)`, and `(+++)`.
- **Direct comparison:** Reported `(+)` value: `20/119 (16.0%)`; fraction-implied value: `16.8%`, a reported value **0.8 percentage points lower**. Reported category-count total: `120`; stated denominator: `119`, an excess of **1**.
- **Calculation / rule:** `20 ÷ 119 × 100 = 16.8067%`, which rounds to `16.8%` at one decimal (rounding interval `16.75%–16.85%`), not `16.0%` (interval `15.95%–16.05%`). `20 + 20 + 38 + 42 = 120`; mutually exclusive categories should total `119` if the common denominator applies.
- **Bounded impact:** Correction or confirmation is needed for this placebo-arm 3-month distribution. The displayed adjusted odds ratio `0.7 (0.20 to 2.17), P=.49` is not recalculated or deemed incorrect by this card.
- **Verification instruction:** 1. Inspect the four placebo 3-month eTable 4 cells and their source data/export. 2. Recalculate `20/119` and sum the four counts. 3. A corrected percentage of `16.8%` and category total of `119`, or a documented different numerator/denominator/category definition, resolves the issue.

### 2. The repeated `19/27` percentage is misrounded — Accepted

- **Category / severity:** Arithmetic inconsistency / Minor.
- **Issue statement:** The placebo second-follow-up fraction `19/27` is displayed as `70.0%` in both the supplement and main article, although it rounds to `70.4%`, creating a repeated localized display inconsistency.
- **Evidence A:** **DOC-003, `joi200054supp2_prod.pdf`, PDF p. 8, eTable 5, “Enterobacterales in stool resistant to at least one of the tested antibiotics,” second follow-up, Placebo column:** `19/27 (70.0)`; adjacent probiotic value `23/33 (69.7)` and absolute difference `-0.01 (-0.24 to 0.23)`.
- **Evidence B:** **DOC-001, `jama_butler_2020_oi_200054.pdf`, PDF p. 7, Results microbiology paragraph:** `19/27 [70.0%]`.
- **Direct comparison:** Reported percentage: `70.0%`; fraction-implied percentage: `70.4%`; discrepancy: **−0.4 percentage points** in both locations.
- **Calculation / rule:** `19 ÷ 27 × 100 = 70.3704%`, which rounds to `70.4%` at one decimal (interval `70.35%–70.45%`), not `70.0%` (interval `69.95%–70.05%`). From the displayed fractions, `23/33 − 19/27 = -0.00673`, which rounds to the table’s `-0.01`; this supports the fractions rather than the displayed `70.0%`.
- **Bounded impact:** The reported placebo percentage in the table and duplicated narrative needs correction or confirmation. This card does not assess the reported adjusted odds ratio, CI, or P value.
- **Verification instruction:** 1. Confirm the `19/27` source cell in eTable 5 and the duplicated main-text sentence. 2. Recalculate to one decimal. 3. Replacing `70.0%` with `70.4%`, or documenting a nonstandard percentage denominator, resolves the issue.

### 3. CACE coefficient, confidence interval, and P value are incompatible at stated precision — Accepted

- **Category / severity:** Statistical reporting inconsistency / Minor.
- **Issue statement:** The reported CACE coefficient `0.01`, its wide 95% CI, and `P=.52` are not mutually compatible under the stated two-stage least-squares coefficient presentation, so at least one reported component needs confirmation.
- **Evidence A:** **DOC-003, `joi200054supp2_prod.pdf`, PDF p. 3, eAppendix 4, adherence/CACE paragraph:** randomization was used as the instrument; the coefficient is an adjusted mean difference per percentage-point product use, and “for presentation purposes” the coefficient and 95% CI were multiplied by 100.
- **Evidence B:** **DOC-003, `joi200054supp2_prod.pdf`, PDF p. 5, eTable 2, “Analysis of Primary Outcome Measure Accounting for Study Product Adherence,” CACE row:** `N 305`; `Adjusted coefficient, 95% CI: 0.01 (-0.20 to 0.41)`; `p-value .52`.
- **Direct comparison:** The reported CI has midpoint `(−0.20 + 0.41)/2 = 0.105` and half-width `(0.41 − (−0.20))/2 = 0.305`, whereas the reported estimate is `0.01`; the approximate two-sided Wald P value implied by the rounded CI is `~.95`, not `.52` (**about .43 higher**).
- **Calculation / rule:** Using the ordinary symmetric 95% Wald-CI rule, `SE ≈ 0.305/1.96 = 0.1556`; `z ≈ 0.01/0.1556 = 0.064`; two-sided `P ≈ 0.95`. Rounding tolerance considered: estimate `0.005–0.015`; CI endpoints `−0.205 to −0.195` and `0.405 to 0.415`. Even at the estimate’s maximum rounding value, a P value of `.52` (two-sided `|z| ≈ 0.64`) would require `SE ≈ 0.023`, whose approximate 95% CI is `0.015 ± 1.96×0.023` (about `−0.03 to 0.06`), not the printed interval. This check is conditional on the ordinary coefficient/CI/P convention indicated by the eAppendix; the article does not provide an alternative test definition in these locations.
- **Bounded impact:** Confirm which of the CACE estimate, CI, or P value should be corrected. This card does not alter the primary-outcome result or infer a treatment effect.
- **Verification instruction:** 1. Inspect the CACE model output and its test statistic. 2. Confirm the scale after the stated multiplication by 100 and whether the CI and P derive from the same model/test. 3. Matching estimate, CI, and P on the same scale resolves the issue.

### 4. Adherence median conflicts with its IQR and differs across documents — Accepted

- **Category / severity:** Cross-document inconsistency / Minor.
- **Issue statement:** The main article reports an adherence median below the lower quartile, while the results supplement gives a different median with the same IQR and description, so the adherence summary requires confirmation.
- **Evidence A:** **DOC-001, `jama_butler_2020_oi_200054.pdf`, PDF p. 4, Results, “Intervention Fidelity” paragraph:** “For the 302 care home residents who initiated at least 1 study product dose, a median of `93.3%` (interquartile range [IQR], `93.56% to 99.45%`) full or partial doses were taken.”
- **Evidence B:** **DOC-003, `joi200054supp2_prod.pdf`, PDF p. 5, text immediately above eTable 2:** “median percentage of taken study product either in full dose or partial dose was `97.8% (IQR 93.56 to 99.45)`.”
- **Direct comparison:** DOC-001 median `93.3%` is **0.26 percentage points below** its reported first quartile `93.56%`; DOC-003 reports median `97.8%`, **4.5 percentage points higher** than DOC-001, with the same IQR `93.56% to 99.45%`.
- **Calculation / rule:** By the reported IQR convention, `Q1 ≤ median ≤ Q3`. DOC-001 gives `93.56 ≤ 93.3`, which is false by `93.56 − 93.3 = 0.26` percentage points. No rounding tolerance can reverse this ordering at the displayed precision: even `93.3` rounded to one decimal is below the lower bound `93.56` rounded to two decimals.
- **Bounded impact:** The product-adherence descriptive statement(s), including the text introducing eTable 2, need correction or confirmation. This card does not establish whether the CACE analysis itself used an incorrect adherence value.
- **Verification instruction:** 1. Recreate the adherence summary for the stated 302 initiators. 2. Confirm whether both locations use the same population and dose definition. 3. A median within `93.56%–99.45%` and matching values across locations, or documented differing populations/definitions, resolves the issue.

### 5. Oral-candidiasis absolute risk difference cannot be reconciled from supplied evidence — Uncertain

- **Category / severity:** Cross-document inconsistency / Uncertain (not a confirmed final issue).
- **Issue statement:** The main article’s 3-month oral-candidiasis ARD is `−0.2%`, whereas the displayed raw counts imply `+1.7` percentage points probiotic minus placebo and eTable 5 displays `0.02`; the necessary adjusted-estimand definition or calculation is not supplied.
- **Evidence A:** **DOC-001, `jama_butler_2020_oi_200054.pdf`, PDF p. 7, Results microbiology paragraph:** “presence of oral candida at 3 months (`88/113 [77.9%]` in the probiotic group vs `80/105 [76.2%]` in the placebo group; ARD, `−0.2% [95% CI, −11.3% to 10.9%]`; AOR, `1.23 [0.54 to 2.83]`; `P=.62`).”
- **Evidence B:** **DOC-003, `joi200054supp2_prod.pdf`, PDF p. 8, eTable 5, “Presence of oral Candidiasis,” 3 months:** probiotic `88/113 (77.9)`; placebo `80/105 (76.2)`; absolute difference `0.02 (-0.10 to 0.13)`; adjusted odds ratio `1.2 (0.54 to 2.83)`; `P=.62`.
- **Direct comparison:** Raw probiotic-minus-placebo difference: `77.876% − 76.190% = +1.685` percentage points (about `+1.7%`), consistent with the eTable’s decimal `+0.02`; main-text ARD is `−0.2%`, **1.885 percentage points lower and opposite in sign** than the raw difference.
- **Calculation / rule:** Inputs: `88/113` and `80/105`. Formula: `(88 ÷ 113 − 80 ÷ 105) × 100 = +1.685` percentage points; rounding to one decimal is `+1.7%`, and as a proportion to two decimals is `+0.02`. No definitive comparison is possible because the supplied pages do not define the ARD estimand/calculation or show whether `−0.2%` is an adjusted marginal estimate on another scale. Rounding tolerance therefore cannot resolve the sign difference without that missing evidence.
- **Bounded impact:** Confirm the main-text ARD and its relation to the eTable absolute difference before treating either as erroneous. No confirmed correction is proposed.
- **Verification instruction:** 1. Locate the analysis output or methods definition for the oral-candidiasis ARD. 2. Confirm its direction, denominator/population, and whether it is adjusted or marginal. 3. Evidence that `−0.2%` is a separately defined adjusted estimate resolves the discrepancy; otherwise a corrected main-text/table value should be identified.

### 6. eFigure 2’s stated N does not match the Table 2 infection-duration population — Accepted

- **Category / severity:** Participant flow inconsistency / Minor.
- **Issue statement:** eFigure 2 labels the infection-duration display `N=305`, while the corresponding Table 2 outcome is explicitly for participants with at least one infection and reports 111 plus 102 participants, so the figure denominator/label requires confirmation.
- **Evidence A:** **DOC-003, `joi200054supp2_prod.pdf`, PDF p. 13, eFigure 2 title and footnote:** “Mean Duration of All-Cause Infections (Days) by Group (`N=305`)”; “Mean duration of infection was calculated by dividing the number of infection days by the total number of infections.” The figure’s y-axis is “Number of care home residents.”
- **Evidence B:** **DOC-001, `jama_butler_2020_oi_200054.pdf`, PDF p. 6, Table 2, “Between-Group Differences for Infection-Related Outcome Measures,” row “≥1 infection, No. (%)”:** probiotic `111 (73.0)` and placebo `102 (66.7)`. **Same table, row “Infection duration, for ≥1 infection, mean (SD), days”:** probiotic `6.8 (4.7)` and placebo `6.0 (4.9)`.
- **Direct comparison:** Figure label: `N=305`; Table 2 participants with ≥1 infection: `111 + 102 = 213`; discrepancy: **92 participants** (`305 − 213`).
- **Calculation / rule:** The Table 2 duration row is expressly limited to “for ≥1 infection”; its corresponding counts total `213`. If eFigure 2 depicts that duration outcome’s resident distribution, its displayed `N` should identify the applicable population or explain inclusion of the remaining `92` participants. No rounding applies to these integer counts.
- **Bounded impact:** Confirm the analytic population and label for eFigure 2; this card does not establish that the plotted infection days, means, or medians are incorrect.
- **Verification instruction:** 1. Check the eFigure 2 dataset and caption against the Table 2 duration analysis set. 2. Determine whether the figure includes all 305 analysis participants, only the 213 with ≥1 infection, or another unit such as infections. 3. An explicit matching denominator/unit or a corrected figure label resolves the issue.

## AI Training Restriction Summary

This supplied-materials screen is separate from the scientific issues and is not a legal opinion. Per package instruction, AI-training permissions are currently assumed given.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| DOC-001 | No AI Training Restriction Located in Provided Materials | `jama_butler_2020_oi_200054.pdf`, PDF pp. 1–10, footer: “© 2020 American Medical Association. All rights reserved.” Embedded XMP metadata: no copyright, rights, licence, permissions, terms, text-and-data-mining, or AI-use field. | No |
| DOC-002 | No AI Training Restriction Located in Provided Materials | `joi200054supp1_prod.pdf`, PDF p. 2, “General Information”: “The protocol should not be used as a guide, or as an aide-memoire for the treatment/care of other patients/participants.” PDF pp. 1–76 and embedded metadata: no AI-use/training or rights-and-permissions language located. | No |
| DOC-003 | No AI Training Restriction Located in Provided Materials | `joi200054supp2_prod.pdf`, PDF p. 1 (repeated pp. 2–13): “© 2020 American Medical Association. All rights reserved.” Embedded XMP metadata: no rights, licence, permissions, terms, text-and-data-mining, AI-use, training, fine-tuning, or model-improvement language located. | No |
| DOC-004 | No AI Training Restriction Located in Provided Materials | `joi200054supp3_prod.pdf`, PDF p. 1, “Additional Information”: “Who can access the data: Researchers whose proposed use of the data has been approved” and “Mechanisms of data availability: After approval of a proposal and with a signed data access agreement.” Embedded metadata: no rights, licence, permissions, terms, or AI-use field. | No |

