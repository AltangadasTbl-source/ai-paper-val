# Human Adjudication Report

Scope: six critic-retained evidence cards. Card 6 is **Uncertain** and is retained only to obtain the missing denominators/footnotes. This report is not a legal opinion.

## Scientific issues

### 1. Paone No-PAP baseline FEV1 has a median outside its reported IQR

- **Category / severity:** Presentation inconsistency / Minor
- **Issue statement:** In eTable 6, the Paone No PAP group's reported FEV1 median (30.0% predicted) is greater than the reported IQR upper bound (24.5% predicted), so this baseline summary cannot describe a conventional median-and-IQR distribution as printed and needs confirmation.
- **Evidence:**
  - **Reported value —** `JAMA2019_22343_SUPP2_RESULTS`, *joi190154supp2_prod.pdf*, PDF p. 30, eTable 6, Paone 2014 row, **No PAP** patient-characteristics column: “-FEV1 % predicted 30.0 (23.5-24.5)”.
- **Direct comparison:** reported median = **30.0% predicted**; reported IQR = **23.5–24.5% predicted**; comparator rule = median must lie within the reported IQR. The median is **5.5 percentage points above** the stated upper quartile.
- **Calculation / tolerance:** inputs: median 30.0, IQR upper bound 24.5 (% predicted). Rule: `median ≤ IQR upper bound`. `30.0 − 24.5 = +5.5 percentage points`; the inequality fails. No rounding tolerance can reconcile a 5.5-point difference at the displayed one-decimal precision.
- **Bounded impact:** The Paone No-PAP baseline FEV1 summary in eTable 6 requires correction or confirmation; no effect estimate is assessed here.
- **Verification:**
  1. Check the source extraction sheet or Paone study table for the No-PAP FEV1 quartiles and median.
  2. Confirm the issue if the source values retain median 30.0 with Q3 24.5; resolve it if the table contains a transcription, column-placement, or numeric error that restores `Q1 ≤ median ≤ Q3`.

### 2. CAT weighted mean-difference confidence interval differs between the main text and eTable 10

- **Category / severity:** Cross-document inconsistency / Minor
- **Issue statement:** The same 14-patient CAT comparison is reported with different 95% confidence-interval limits in the main text and eTable 10, which prevents a single unambiguous value from being cited.
- **Evidence:**
  - **Main-text value —** `JAMA2019_22343_MAIN`, *jama_wilson_2020_oi_190154.pdf*, PDF p. 7 (printed p. 461), results paragraph immediately above “No statistically significant differences in outcomes…”: “quality of life [COPD assessment test]: weighted mean difference [WMD], 2.30 [95% CI, −2.23 to 6.83]; P = .32”.
  - **Supplement value —** `JAMA2019_22343_SUPP2_RESULTS`, *joi190154supp2_prod.pdf*, PDF p. 43, eTable 10, “HMV/BPAP mix (pressure controlled ventilation) (high intensity) vs. HMV/BPAP mix (pressure support ventilation)” row, Quality of life/COPD assessment test: “1 RCT25; 14 patients” and “WMD: 2.30, 95% CI: -2.35 to 6.95, I2=N/A”.
- **Direct comparison:** reported WMD is the same (**2.30**), but main text CI = **−2.23 to 6.83** and eTable 10 CI = **−2.35 to 6.95**. The supplement lower limit is **0.12 lower** and upper limit **0.12 higher**.
- **Calculation / tolerance:** `−2.35 − (−2.23) = −0.12`; `6.95 − 6.83 = +0.12`. Both CIs are displayed to two decimal places; the 0.12 differences exceed a ±0.01 last-digit rounding tolerance.
- **Bounded impact:** The reported CAT WMD point estimate is unchanged, but the accompanying 95% CI needs a single confirmed version.
- **Verification:**
  1. Check the meta-analysis output or calculation sheet for study 25 (14 patients) and its CAT scale direction.
  2. Confirm the issue if the source output supports only one of the two interval pairs; resolve it by correcting the nonmatching main-text or eTable 10 interval.

### 3. Treatment-duration ordering is reversed between the main-text narrative and eTable 10

- **Category / severity:** Cross-document inconsistency / Major
- **Issue statement:** The 26-patient Funk 6-minute-walk comparison assigns the 43% increase and 11% decrease to opposite duration-order descriptions in the main text and eTable 10, which could reverse the reported duration-associated direction of change.
- **Evidence:**
  - **Main-text value —** `JAMA2019_22343_MAIN`, *jama_wilson_2020_oi_190154.pdf*, PDF p. 6 (printed p. 460), results paragraph beginning “One RCT of 49 patients…”: “One RCT that included 26 patients found that patients who received BPAP for more than 6 months had a 43% increase in their 6-minute walk distance test, while the group who received treatment for less than 6 months had an 11% reduction (P = .04).”
  - **Supplement header —** `JAMA2019_22343_SUPP2_RESULTS`, *joi190154supp2_prod.pdf*, PDF p. 43, eTable 10, row header: “BPAP for 6 months vs. BPAP for more than 6 months”.
  - **Supplement result —** same document/location, 6-minute walk distance test (meters) row: “1 RCT28; 26 patients” and “43% increase vs. 11% decrease, p=0.04”.
- **Direct comparison:** main text explicitly maps **>6 months → 43% increase** and **<6 months → 11% reduction**. eTable 10 places the result under the ordered comparison **“BPAP for 6 months vs. BPAP for more than 6 months”**, whose first-versus-second ordering is the reverse of the narrative’s >6-month-versus-<6-month ordering. The numerical contrast is 43% vs −11%, a **54-percentage-point** separation, but the duration-to-result mapping is not consistently displayed.
- **Calculation / tolerance:** inputs: +43% and −11%. `43 − (−11) = 54 percentage points`. The issue is an ordering/mapping conflict, not a rounding difference; rounding tolerance is not applicable.
- **Bounded impact:** The duration-associated 6-minute-walk statement and the eTable 10 comparison header require confirmation or harmonization; this card does not assess causality or the underlying trial.
- **Verification:**
  1. Check Funk study 28’s group labels and the original 6-minute-walk values, including which duration group is first in the comparison.
  2. Confirm the issue if eTable 10’s ordered header assigns the first value to 6 months while the main text assigns 43% to >6 months; resolve it by correcting the header or narrative mapping and retaining the verified group order.

### 4. Figure 1 pooled mortality CI differs from the narrative CI

- **Category / severity:** Presentation inconsistency / Minor
- **Issue statement:** Figure 1 and the accompanying main-text results paragraph report the same BPAP-versus-no-device pooled mortality odds ratio but different lower 95% CI limits, leaving the displayed confidence interval internally inconsistent.
- **Evidence:**
  - **Figure value —** `JAMA2019_22343_MAIN`, *jama_wilson_2020_oi_190154.pdf*, PDF p. 4 (printed p. 458), Figure 1A, “BPAP vs no device” subtotal: “0.66 (0.50-0.87)”.
  - **Narrative value —** same document, PDF p. 5 (printed p. 459), “BPAP Compared With No Device” paragraph: “OR, 0.66 [95% CI, 0.51-0.87]; P = .003; 13 studies; 1423 patients; SOE, moderate”.
- **Direct comparison:** Figure 1A = **OR 0.66 (95% CI 0.50–0.87)**; narrative = **OR 0.66 (95% CI 0.51–0.87)**, 13 studies/1423 patients. The lower limit in the narrative is **0.01 higher**; point estimate and upper limit match.
- **Calculation / tolerance:** `0.51 − 0.50 = +0.01`. Both limits are displayed to two decimals. A ±0.01 last-digit rounding tolerance could account for this difference, but the two printed values remain nonidentical.
- **Bounded impact:** The BPAP mortality pooled effect’s lower CI limit needs confirmation; the card does not alter the stated point estimate, study count, or patient count.
- **Verification:**
  1. Check the forest-plot export and underlying pooled-analysis output for the BPAP mortality subtotal.
  2. Resolve the issue if a single rounded CI is selected and used in both Figure 1A and the narrative; confirm it as a presentation discrepancy if both current printed values are retained without an explained rounding convention.

### 5. Figure 4 pooled quality-of-life CI differs from the narrative CI

- **Category / severity:** Presentation inconsistency / Minor
- **Issue statement:** Figure 4 and the main-text BPAP results paragraph give the same pooled quality-of-life SMD but different upper 95% CI limits, so the printed summary is not internally uniform.
- **Evidence:**
  - **Figure value —** `JAMA2019_22343_MAIN`, *jama_wilson_2020_oi_190154.pdf*, PDF p. 5 (printed p. 459), Figure 4, “Overall” row: “0.16 (–0.06 to 0.38)”.
  - **Narrative value —** same document, PDF p. 5 (printed p. 459), “BPAP Compared With No Device” paragraph: “SMD, 0.16 [95% CI, −0.06 to 0.39]; 9 studies; 833 patients; SOE, insufficient”.
- **Direct comparison:** Figure 4 = **SMD 0.16 (95% CI −0.06 to 0.38)**; narrative = **SMD 0.16 (95% CI −0.06 to 0.39)**, 9 studies/833 patients. The narrative upper limit is **0.01 higher**; point estimate and lower limit match.
- **Calculation / tolerance:** `0.39 − 0.38 = +0.01`. Both values are displayed to two decimals. A ±0.01 last-digit rounding tolerance could account for the difference, but the report should present one confirmed rounded CI.
- **Bounded impact:** The pooled BPAP quality-of-life upper CI limit requires confirmation; this card does not alter the SMD, number of studies, or participant count.
- **Verification:**
  1. Check the Figure 4 export and underlying pooled SMD output for the nine-study, 833-patient analysis.
  2. Resolve the issue if the confirmed rounded upper limit is made identical in the figure and narrative; confirm it as a presentation discrepancy if the two values are both intended without a stated rounding rule.

### 6. **Uncertain** — Cheung CPAP/BPAP denominators may not align across eTables 6 and 10

- **Category / severity / status:** Participant flow inconsistency / Uncertain / **Uncertain**
- **Issue statement:** eTable 6 lists 24 CPAP and 23 BPAP patients for Cheung, whereas eTable 10 reports 49 participants with percentages that imply 23 and 26 denominators; without outcome-population footnotes or flow data, it cannot be determined whether this is an inconsistency or different analysis populations.
- **Evidence:**
  - **Baseline/group counts —** `JAMA2019_22343_SUPP2_RESULTS`, *joi190154supp2_prod.pdf*, PDF p. 19, eTable 6, Cheung 2010 row, intervention/groups and patient-characteristics columns: “CPAP” with “-24 Patients”; “BPAP ST” with “-23 Patients”.
  - **Outcome summary —** same document, PDF p. 43, eTable 10, “BPAP vs. CPAP” / “Number of patients with exacerbations” row: “1 RCT17; 49 patients” and “30.43% vs. 53.85%; RD: -0.23, 95% CI: -0.50 to 0.03; OR: 0.38, 95% CI: 0.12 to 1.22; I2= N/A”.
  - **Missing evidence:** eTable 10 does not state its two outcome denominators or event counts, and the supplied evidence does not provide a participant-flow/analysis-population footnote linking eTable 6 counts to the exacerbation outcome.
- **Direct comparison:** eTable 6 total = **24 CPAP + 23 BPAP = 47**. eTable 10 total = **49 participants**. The printed percentages can be represented by **7/23 = 30.43%** and **14/26 = 53.85%**, which sum to **49**, but the eTable 10 group order and denominators are not explicitly supplied.
- **Calculation / tolerance:** `24 + 23 = 47`; `7 ÷ 23 × 100 = 30.43%`; `14 ÷ 26 × 100 = 53.85%`; `23 + 26 = 49`. The total difference is `49 − 47 = +2 participants`. Percentages are rounded to two decimals; ±0.005 percentage point rounding tolerance was considered. This arithmetic identifies a possible denominator mismatch only; it does not establish that the tables should use the same analysis population.
- **Bounded impact:** Confirmation is needed for the Cheung exacerbation analysis denominators and its “49 patients” total before treating the counts as inconsistent; no correction is asserted.
- **Verification:**
  1. Check Cheung study 17’s CONSORT/participant-flow information, outcome-specific analysis table, and any eTable 6/eTable 10 footnotes for randomized, treated, and analyzed denominators.
  2. Resolve this card if documented outcome denominators of 23 and 26 (or another explained 49-participant analysis set) are shown; confirm a participant-flow inconsistency only if the same intended analysis population is documented as 24 CPAP and 23 BPAP without an explanation for the 49-participant outcome total.

## AI Training Restriction Summary

Separate compliance screen only; not a legal opinion and not a scientific issue list.

| Document ID | File | Status | Exact evidence location and excerpt | Human Compliance Review |
|---|---|---|---|---|
| `JAMA2019_22343_MAIN` | *jama_wilson_2020_oi_190154.pdf* | No AI Training Restriction Located in Provided Materials | PDF p. 1 (printed p. 455), footer, repeated through PDF p. 11: “© 2020 American Medical Association. All rights reserved.” Embedded PDF-information/XMP metadata was also screened; no AI-training, fine-tuning, or model-improvement term was located. | No |
| `JAMA2019_22343_SUPP1_PROTOCOL` | *joi190154supp1_prod.pdf* | No AI Training Restriction Located in Provided Materials | PDF p. 1, title/provenance page: “This supplementary material has been provided by the authors to give readers additional information about their work.” Embedded metadata and PDF pp. 1 and 15 were screened; no AI-training, fine-tuning, or model-improvement term was located. **Scientific audit: Not Audited by Design (protocol).** | No |
| `JAMA2019_22343_SUPP2_RESULTS` | *joi190154supp2_prod.pdf* | No AI Training Restriction Located in Provided Materials | PDF p. 1, Supplementary Online Content title page, repeated on PDF pp. 2–15: “© 2020 American Medical Association. All rights reserved.” Embedded PDF-information/XMP metadata was also screened; no AI-training, fine-tuning, or model-improvement term was located. | No |

