# Statistical Consistency Check - JAMA 2025.9110

## Scope and evidence

- **Checker:** `statistical_consistency_checker`
- **Documents used:** `JAMA2025_9110_D01_MAIN` (`jama_summers_2025_oi_250040_1753124024.36498.pdf`) and `JAMA2025_9110_D04_RESULTS_SUPP` (`joi250040supp3_prod_1753124024.38098.pdf`).
- **Evidence used:** the D01 main-text evidence map, the D04 result-relevant supplementary evidence map, source-linked normalized text, and rendered source pages for the cited tables/figures.
- **Excluded by design:** D02 protocol, D03 SAP, references on D04 pp. 33-34, external sources, and unstated assumptions.
- **Checks:** point estimate within interval; interval/null/P-value coherence; effect direction; repeated estimates, intervals, and P values; analysis and summary-statistic labels; subgroup labels and denominators; sensitivity-analysis reporting; narrative/table/figure agreement.
- **Model-dependent checks:** CI symmetry was not used. Exact agreement of model-based estimates with crude calculations was not required. The primary and subgroup CIs use block bootstrap, the ventilation effect uses a tobit mixed model, and other estimates are adjusted/mixed-model quantities.

## Local candidates

Five candidates are retained, within the package limit.

### SC-01 - Protocol-deviation participant percentage uses the event count rather than the participant count

- **Category:** Arithmetic inconsistency
- **Confidence:** High
- **Exact location:** `joi250040supp3_prod_1753124024.38098.pdf`, source PDF p. 16, eTable 8, “Total protocol deviations,” augmented-protein column.
- **Source values:** Column denominator `n = 1681`; “Number of participants with at least one event” `151 (9.4)`; “Number of events” `158`.
- **Calculation/logical basis:** `151 / 1681 × 100 = 8.98%`, which rounds to `9.0%`, not `9.4%`. Conversely, `158 / 1681 × 100 = 9.40%`, showing that the displayed `9.4%` matches the event count immediately below rather than the participant count. The usual-protein entry is coherent: `95 / 1716 = 5.54%`, displayed as `5.6%`.
- **Verification instruction:** Recalculate the percentage from the participant numerator `151` and denominator `1681`; confirm whether the intended entry is `151 (9.0%)`, while retaining `158` as the separate number of events.

### SC-02 - Bayesian primary-outcome row is labeled mean (SD) although it reports medians and an IQR

- **Category:** Statistical reporting inconsistency
- **Confidence:** High
- **Exact locations:** `jama_summers_2025_oi_250040_1753124024.36498.pdf`, source PDF p. 7, Table 2, Bayesian quantile mixed-model row; `joi250040supp3_prod_1753124024.38098.pdf`, source PDF p. 27, eFigure 6.
- **Source values/statements:** Table 2 labels the outcome “(bayesian quantile mixed model), mean (SD)” but gives augmented `62.0 (0 to 77)` and usual `64.0 (0 to 77)`, followed by “Median difference, −1.50 (−3.86 to 0.90).” eFigure 6 likewise reports “Median Difference: −1.50 (95% CrI: −3.86, 0.90).” The same group summaries are explicitly labeled median (IQR) in the primary quantile-model row and in the Results.
- **Logical basis:** A `mean (SD)` summary contains one parenthetical SD, not the displayed lower and upper quartiles. The analysis is a Bayesian **quantile** model and both the effect label and companion figure identify a median difference. Thus the row’s descriptive-statistic label conflicts with its values and method.
- **Verification instruction:** Inspect Table 2’s Bayesian row against the primary row and eFigure 6; determine whether “mean (SD)” should read “median (IQR).”

### SC-03 - Ventilation group summaries are labeled mean (SD), but the displayed triplets are medians (IQR)

- **Category:** Cross-document inconsistency
- **Confidence:** High
- **Exact locations:** `jama_summers_2025_oi_250040_1753124024.36498.pdf`, source PDF p. 7, Table 2, “Duration of invasive ventilation”; `joi250040supp3_prod_1753124024.38098.pdf`, source PDF p. 18, eTable 10; eMethods, source PDF p. 4.
- **Source values/statements:** Main Table 2 labels the group summaries “mean (SD), h” but displays augmented `84.0 (35.0 to 178.9)` and usual `78.0 (33.2 to 161.0)`. D04 eTable 10 reports period-specific ventilation values in the same three-number form and states, “Data presented as median (IQR) or n (%).” D04 eMethods separately states that the tobit-model treatment effect is a **difference in means**; Main Table 2 reports that model effect as `6.8 h (95% CI, −3.0 to 16.5)`.
- **Logical basis:** The effect estimate can validly be a model-based mean difference while the observed group distributions are summarized by medians and IQRs. The main-table label conflates those two quantities: each group cell contains a median plus two quartile bounds, not a mean plus one SD.
- **Verification instruction:** Compare the Table 2 group cells with eTable 10’s summary-statistic footnote and the tobit-model eMethods; relabel the descriptive group summaries as median (IQR) while retaining the effect estimate as a mean difference if intended.

### SC-04 - Discussion calls the day-10 urea summaries means, whereas all reported numeric summaries are medians (IQR)

- **Category:** Statistical reporting inconsistency
- **Confidence:** High
- **Exact locations:** `jama_summers_2025_oi_250040_1753124024.36498.pdf`, source PDF p. 8, Discussion; source PDF p. 5, “Biochemical Outcomes”; `joi250040supp3_prod_1753124024.38098.pdf`, source PDF p. 19, eTable 11.
- **Source values/statements:** Discussion: “mean urea concentrations at day 10 were higher in the augmented protein group.” Results: “median (IQR)” day-10 urea `13.0 (8.2-18.8)` vs `10.6 (7.1-15.4)` mmol/L. eTable 11 repeats those values with available denominators `n=439` vs `n=417` and states, “Data are Median (IQR).”
- **Logical basis:** No day-10 mean is reported in the article package. The Discussion assigns a different central-tendency statistic to the same day-10 comparison than the Results and eTable 11.
- **Verification instruction:** Check the analysis output or intended wording; if the cited values are the displayed medians, change “mean urea concentrations” to “median urea concentrations.”

### SC-05 - Table 2 sends the Bayesian figure to Supplement 1, but the cited figure is in Supplement 3

- **Category:** Presentation inconsistency
- **Confidence:** High
- **Exact locations:** `jama_summers_2025_oi_250040_1753124024.36498.pdf`, source PDF p. 7, Table 2 footnote f; source PDF p. 4, Primary Outcome; `joi250040supp3_prod_1753124024.38098.pdf`, source PDF p. 27, eFigure 6.
- **Source values/statements:** Table 2 footnote f: “Bayesian model diagram is shown in eFigure 6 in Supplement 1.” Main Results p. 4 locates eFigures 5 and 6 in `Supplement 3`. D04 is headed `SUPPLEMENT 3` and contains `eFigure 6: Bayesian model analysis` on p. 27 with the repeated estimate `−1.50 (95% CrI, −3.86 to 0.90)`.
- **Logical basis:** The cross-reference in the table footnote conflicts with both the main Results cross-reference and the supplied figure’s document location.
- **Verification instruction:** Open the Table 2 footnote link and the supplied supplements; change “Supplement 1” to “Supplement 3” if eFigure 6 on D04 p. 27 is the intended target.

## Passed statistical checks

- **Primary analysis:** `−1.97` lies within `−7.24 to 3.30`; the interval includes the null `0` and `P=.46` is nonsignificant. These values repeat exactly in the abstract (p. 1), Results (p. 5), and Table 2 (p. 7). The negative direction agrees with augmented `62` vs usual `64` days and the stated convention that fewer days is worse.
- **Primary secondary/sensitivity analyses:** linear-model `−1.26 (−3.59 to 1.06), P=.29`; nontrial-formula exclusion `−0.97 (−6.04 to 4.10), P=.71`; palliative/organ-donation exclusion `−1.12 (−7.17 to 4.93), P=.72`; and survivor-only `0.01 (−1.94 to 1.96), P=.995` all have point estimates inside their CIs and null/P-value relationships in the expected direction.
- **Bayesian analysis:** `−1.50` lies within the `95%` credible interval `−3.86 to 0.90`; the interval crosses `0`, the posterior median is negative, and the reported posterior probability of any benefit (`effect >0`) is `0.109`. Table 2 and D04 eFigure 6 repeat the estimate and interval exactly.
- **Binary and time-to-event secondary outcomes:** survival RR `0.99 (0.95-1.03), P=.47`; ventilation mean difference `6.8 (−3.0 to 16.5), P=.17`; hospital-discharge HR `0.96 (0.90-1.02), P=.15`; tracheostomy RR `1.15 (0.66-2.01), P=.57`; and new-KRT RR `0.97 (0.81-1.16), P=.69` are directionally coherent and pair null-containing intervals with nonsignificant P values.
- **Rounded boundary check:** ICU-discharge HR `0.93 (0.88-1.00), P=.04` was not treated as inconsistent. The two-decimal CI endpoint may round to `1.00` from a value below `1`; no unrounded endpoint is provided.
- **Subgroup effects and labels:** Every point estimate in Main Figure 3 and D04 eFigure 7 lies within its CI, and signs agree with the displayed treatment-versus-control medians. Interaction P values repeat consistently after rounding: mechanical ventilation `.02` vs `.023`; KRT `<.001` in both; age `.11` vs `.106`; BMI `.47` vs `.468`. Subgroup counts reconcile to full treatment denominators for ventilation, KRT, and age. BMI totals are lower (`1288` vs `1280`), but both figures repeat the same subgroup counts and do not claim complete BMI availability.
- **Period and treatment denominators:** D04 eTable 4 period counts sum to augmented `1681` and usual `1716`. D04 eTable 10 period-specific day-90 survivors sum to `1221` and `1269`, matching Main Table 2; period-specific new-KRT outcomes sum to `122` and `127`, also matching Main Table 2.
- **Readmissions:** Main Table 2’s at-least-one hospital-readmission values `161 (9.6%)` and `172 (10.0%)` reconcile to D04 eTable 14’s post-index hospital-readmission rows (`1681−1520=161`; `1716−1544=172`).
- **No CI-symmetry finding:** Bootstrap, mixed-model, tobit, Bayesian, and subgroup intervals were not screened for symmetry around the point estimate.

## Observations not promoted

- The narrative statements that discharge destinations were “similar” and that there were “no differences” in readmission events are accompanied only by descriptive summaries; Main Table 2 footnote k explicitly says no statistical comparison was performed. The wording can be read descriptively, so no inconsistency candidate was retained.
- D04 eTable 5 calls `696.0 (408.0, 950.8)` vs `676.2 (405.0, 956.7)` the “Mean volume” of formula delivery while its footnote and Main Results describe the displayed cross-patient summaries as median (IQR). “Mean” may denote a participant-level daily-average variable subsequently summarized by a median; without a clearer method statement, this was not promoted.

## Disposition

Five document-verifiable local candidates are returned. Candidate SC-01 may overlap the table-arithmetic stream and should be deduplicated by the coordinator. The remaining estimate/CI/P-value, direction, repeated-value, subgroup, denominator, and sensitivity checks passed as described above.
