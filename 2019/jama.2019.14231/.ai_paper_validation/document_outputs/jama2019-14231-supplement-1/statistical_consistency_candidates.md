# Statistical Consistency Audit — Candidate Evidence Cards

## Scope and evidence used

- **Main article:** `jama2019-14231-main-article` / `jama_aminian_2019_oi_190103.pdf`, PDF pp. 1-12.
- **Results supplement:** `jama2019-14231-supplement-1` / `joi190103supp1_prod.pdf`, PDF pp. 6-20 only.
- **Evidence maps used:** `main_text_extraction.json` and `results_evidence_map.md`; page-linked native text was consulted to verify the exact wording and values. Source PDFs were not modified.
- **Outcome of routine checks:** No discrepancy was found in repeated Table 2/eTable 6 HRs, CIs, or P values; the main-article outcome figures reproduce the same HR/CIs/P values. All eTable 6 Cox-model CIs exclude 1 and its listed model P value is below .05. The cerebrovascular absolute-risk-difference CI including 0 is not a candidate because it is a separately estimated bootstrap risk-difference estimand, whereas P=.02 is for the adjusted Cox HR. The 98.8% Bonferroni CIs in eTable 8 are likewise not paired with an unadjusted .05 decision threshold.

---

## Candidate 1 — Primary-outcome E-values do not reproduce from the reported HR and CI

- **Category / severity:** Statistical reporting inconsistency / Moderate.
- **Issue statement:** eTable 12 reports primary-composite E-values of 2.15 and 1.92, but those values are incompatible with the displayed primary HR 0.61 and its upper 95% CI limit 0.69 under the same risk-ratio-scale E-value calculation that reproduces the other seven eTable 12 rows.
- **Reported item:** `jama2019-14231-supplement-1`, PDF p. 20, eTable 12, row **Primary composite**: “E-value for HR estimate” **2.15** and “E-value for upper limit of 95% CI” **1.92**. The same row’s surgery HR is supplied by `jama2019-14231-supplement-1`, PDF p. 9, eTable 6: **0.61 (95% CI, 0.55-0.69)**; it is repeated in the supplement PDF p. 19, sensitivity analysis C: **HR 0.61 [95% CI 0.55 to 0.69]**.
- **Comparator / direct calculation:** PDF p. 19 says the E-value is “expressed on the risk ratio scale,” and eTable 12 labels the two columns as E-values for the HR estimate and its upper CI limit. For a protective ratio `r < 1`, use `E = 1/r + sqrt((1/r) × (1/r − 1))`.
  - For `r = 0.61`: `1/0.61 + sqrt((1/0.61) × (1/0.61 − 1)) = 2.663`, reporting to two decimals as **2.66**, not **2.15**.
  - For the upper limit `r = 0.69`: the same calculation is `2.256`, reporting as **2.26**, not **1.92**.
  - Rounding cannot account for the gap: inputs that round to 0.61 (0.605-0.615) yield approximately 2.63-2.70, and inputs that round to 0.69 (0.685-0.695) yield approximately 2.23-2.28.
  - Internal replication check: applying the calculation to the remaining eTable 12 HRs/upper limits gives values consistent with the table after rounding (secondary 2.61/2.12 vs 2.62/2.11; mortality 2.78/2.12 vs 2.81/2.13; heart failure 4.70/3.50 vs 4.69/3.52; coronary disease 2.26/1.56 vs 2.27/1.55; cerebrovascular disease 2.35/1.32 vs 2.35/1.31; nephropathy 4.44/3.26 vs 4.46/3.29; atrial fibrillation 1.88/1.21 vs 1.90/1.21).
- **Logical impact:** The printed primary E-values make the primary association appear less robust to unmeasured confounding than the values implied by its reported HR/CI; the event HR, CI, and its direction are unaffected.
- **Human verification:**
  1. In supplement p. 9, confirm the primary HR/CI is 0.61 (0.55-0.69); in p. 20, confirm 2.15/1.92 are printed in the primary-composite E-value columns.
  2. Recalculate using the equation above (or inspect the analysis output for any HR-to-risk-ratio transformation). Values near 2.66 and 2.26 confirm the inconsistency; a documented, primary-specific transformation that yields 2.15/1.92 would resolve it.

---

## Candidate 2 — Time-varying-HR narrative cites the wrong supplementary table

- **Category / severity:** Presentation inconsistency / Minor.
- **Issue statement:** The time-varying-HR narrative says eTable 4 contains adjusted HRs at 2, 5, and 8 years, whereas eTable 4 contains event rates and the described HR table is eTable 7.
- **Reported item:** `jama2019-14231-supplement-1`, PDF p. 19, sensitivity analysis B, verbatim: “**eTable 4 displays adjusted hazard ratios and 95% confidence intervals at 2, 5, and 8 years after the index date.**”
- **Comparator:** In the same PDF p. 19 immediately after this sentence, and identically on PDF p. 10, **eTable 7** is titled “Time-Varying Hazard Ratios and 95% CIs at 2, 5, and 8 Years After the Index Date” and supplies those values (e.g., primary: 0.57 [0.49, 0.65], 0.78 [0.66, 0.93], 0.79 [0.64, 0.97]). PDF p. 6 **eTable 4** is instead titled “Cause-Specific Event Rates (%) per 100 Patient-Years of Follow-up at 8 Years” and reports primary rates 4.51 versus 7.45 and a difference 2.94 (95% CI, 2.42-3.48).
- **Logical impact:** The time-varying values themselves are displayed consistently in eTable 7 on pp. 10 and 19, but the erroneous reference prevents a reader from locating the claimed HR evidence by the cited table number.
- **Human verification:**
  1. Compare the cited sentence on supplement p. 19 with table titles and columns on pp. 6, 10, and 19.
  2. Confirmation is the p. 6 eTable 4 rate table and p. 10/p. 19 eTable 7 time-varying-HR table; correcting “eTable 4” to “eTable 7” resolves the issue.

---

## Candidate 3 — E-value interpretation labels the primary outcome as 5-component MACE, contrary to the reported 6-component primary outcome

- **Category / severity:** Presentation inconsistency / Moderate.
- **Issue statement:** The E-value interpretation describes the primary outcome as “5-component MACE,” while the article defines and repeatedly labels the primary outcome as a composite of six outcomes.
- **Reported item:** `jama2019-14231-supplement-1`, PDF p. 19, sensitivity analysis C, verbatim: “the calculated E-value of 2.15 would mean that residual confounding could explain the observed association if there exists an unmeasured covariate having a relative risk association at least as large as 2.15 with both **5-component MACE** and with metabolic surgery.”
- **Comparator:** `jama2019-14231-main-article`, PDF p. 1, Main Outcomes and Measures, defines the primary outcome as extended MACE, “**composite of 6 outcomes**,” and names all-cause mortality, coronary artery events, cerebrovascular events, heart failure, nephropathy, and atrial fibrillation. The same 6-component definition is repeated in main-article PDF p. 2, Primary and Secondary End Points, and PDF p. 7, Figure 2 caption. Supplement PDF p. 20 labels the corresponding E-value row “Primary composite,” while supplement p. 19 itself pairs its interpretation with primary HR 0.61 (95% CI, 0.55-0.69), the HR reported for that 6-component primary outcome in eTable 6 (p. 9).
- **Logical impact:** The label creates ambiguity about the endpoint to which the primary E-value interpretation applies. It does not alter the HR/CI printed for the article’s defined primary composite, but it could imply a different, unreported five-component outcome.
- **Human verification:**
  1. Confirm all six components in the primary-outcome definition on main-article pp. 1/2/7.
  2. Confirm “5-component MACE” in supplement p. 19 and that no five-component outcome is named as the p. 19 E-value input. Replacing it with the defined six-component primary composite resolves the issue; otherwise the authors should identify the five-component endpoint and its associated HR/CI.

## Candidate count

**3 local candidates.** No protocol or SAP pages were used.
