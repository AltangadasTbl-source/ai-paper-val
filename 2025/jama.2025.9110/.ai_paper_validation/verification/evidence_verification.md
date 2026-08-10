# Evidence Verification

Package: `jama.2025.9110`

Scope: Seven coordinator-supplied candidates only. Evidence was checked against the original D01 and D04 PDFs and their page-linked extractions/renders. D02 and D03 were not opened. No external sources were used. Each candidate used two verification rounds at most: (1) page-linked text extraction and (2) visual inspection of the cited PDF page.

## Summary

| Candidate | Classification | Category |
|---|---|---|
| C01 | Verified | Arithmetic inconsistency |
| C02 | Verified | Arithmetic inconsistency |
| C03 | Verified | Presentation inconsistency |
| C04 | Verified | Statistical reporting inconsistency |
| C05 | Verified | Cross-document inconsistency |
| C06 | Verified | Statistical reporting inconsistency |
| C07 | Verified | Presentation inconsistency |

## C01 - Period 3 augmented-protein sex counts do not reconcile to the group denominator

**Classification: Verified**

- **Location:** `joi250040supp3_prod_1753124024.38098.pdf` (D04), PDF p. 10, eTable 4, Period 3 - Augmented Protein, Sex rows. Comparison: `jama_summers_2025_oi_250040_1753124024.36498.pdf` (D01), PDF p. 5, Table 1, Sex rows.
- **Source values:** D04 gives the Period 3 augmented-protein denominator as `n = 551`, with Male `359 (65.2)` and Female `190 (34.5)`. D01 Table 1 gives augmented-protein totals of Male `1070 (63.7)` and Female `611 (36.3)` among `n = 1681`.
- **Calculation/logical basis:** `359 + 190 = 549`, which is 2 fewer than 551; `65.2% + 34.5% = 99.7%`. Across all four augmented-protein periods in D04, the male counts total `303 + 187 + 359 + 220 = 1069` and the female counts total `177 + 111 + 190 + 132 = 610`, whereas D01 Table 1 reports 1070 male and 611 female. Thus, the displayed period-level sex counts omit two participants relative to both the Period 3 denominator and the complete aggregate sex totals, with no missing/other sex row or footnote.
- **Human verification instruction:** On D04 p. 10, add the two Period 3 sex counts and compare them with `n = 551`; then total the four augmented-period male and female rows and compare them with D01 Table 1 on p. 5.

## C02 - Protocol-deviation participant percentage appears calculated from the event count

**Classification: Verified**

- **Location:** `joi250040supp3_prod_1753124024.38098.pdf` (D04), PDF p. 16, eTable 8, Total protocol deviations, Augmented Protein column.
- **Source values:** Column denominator `n = 1681`; Number of participants with at least one event `151 (9.4)`; Number of events `158`.
- **Calculation/logical basis:** `151 / 1681 x 100 = 8.9827%`, which rounds to `9.0%` at one decimal. `158 / 1681 x 100 = 9.3992%`, which rounds to the displayed `9.4%`. The percentage beside the participant count therefore matches the event count rather than the participant count.
- **Human verification instruction:** Recalculate both `151/1681` and `158/1681` to one decimal and compare each result with the displayed `9.4%`.

## C03 - Patient boxes use patient-level randomization wording in a cluster-randomized trial

**Classification: Verified**

- **Location:** `jama_summers_2025_oi_250040_1753124024.36498.pdf` (D01), PDF p. 3, Figure 1. Comparison statements: D01 p. 2, Design/Trial Procedures; D01 p. 8, Limitations.
- **Source statements:** Figure 1 contains patient-count boxes reading `1043 Randomized to augmented protein group`, `1015 Randomized to usual protein group`, `650 Randomized to augmented protein group and included in primary outcome analysis`, and `703 Randomized to usual protein group and included in the primary outcome analysis`. D01 p. 2 describes a `cluster randomized` trial, says `ICUs were randomly assigned`, and states that participants commenced the formula `to which the ICU was randomized`. D01 p. 8 states, `randomization occurred at the cluster level rather than the patient level`.
- **Logical basis:** The figure's downstream patient-count boxes use direct patient-level "Randomized to" wording even though the article explicitly identifies the ICU/cluster, not the patient, as the unit randomized. The finding is limited to terminology/presentation; it does not assert that the participant counts or actual allocation were wrong.
- **Human verification instruction:** Compare the four Figure 1 patient boxes on p. 3 with the unit-of-randomization statements on pp. 2 and 8; assess replacing patient-level `Randomized to` with `Assigned/allocated to`.

## C04 - Bayesian primary-outcome row labels median/IQR values as mean (SD)

**Classification: Verified**

- **Location:** `jama_summers_2025_oi_250040_1753124024.36498.pdf` (D01), PDF p. 7, Table 2, Primary outcome (secondary analyses), Bayesian quantile mixed-model row. Comparison: D01 p. 7 primary-outcome row and `joi250040supp3_prod_1753124024.38098.pdf` (D04), PDF p. 27, eFigure 6.
- **Source values/statements:** The Bayesian quantile mixed-model outcome label ends with `mean (SD)`, but the treatment cells are `62.0 (0 to 77)` and `64.0 (0 to 77)` and the effect is `Median difference, -1.50 (-3.86 to 0.90)`. The primary row immediately above labels the identical treatment summaries as `median (IQR)`. D04 eFigure 6 labels the Bayesian result `Median Difference: -1.50 (95% CrI: -3.86, 0.90)`.
- **Logical basis:** A three-number center/lower-quartile/upper-quartile display identical to the primary median (IQR) summaries, paired with a Bayesian quantile model and a median-difference effect, cannot be a mean with one SD. The `mean (SD)` row label is inconsistent with the values and analysis.
- **Human verification instruction:** Read the complete Bayesian row on D01 p. 7, compare its group cells with the primary row above, and confirm the effect label in D04 eFigure 6 on p. 27.

## C05 - Ventilation group summaries are labeled mean (SD) in the main table but median (IQR) in the supplement

**Classification: Verified**

- **Location:** D01 `jama_summers_2025_oi_250040_1753124024.36498.pdf`, PDF p. 7, Table 2, Duration of invasive ventilation row. Comparisons: D04 `joi250040supp3_prod_1753124024.38098.pdf`, PDF p. 18, eTable 10 and footer; D04 p. 4, eMethods, Duration of invasive ventilation.
- **Source values/statements:** D01 labels the outcome `Duration of invasive ventilation, mean (SD), h` but displays `84.0 (35.0 to 178.9)` and `78.0 (33.2 to 161.0)`. D04 eTable 10 presents the corresponding period-level ventilation summaries as three-number values and states `Data presented as median (IQR) or n (%)`. D04 eMethods says the tobit model compares mean duration and that the **treatment effect estimate** is a difference in means.
- **Logical basis:** The D01 treatment-group cells contain a center plus lower and upper endpoints, not a mean plus one SD, and the supplement identifies the analogous descriptive summaries as median (IQR). The model-based difference in means describes the treatment effect and does not convert the treatment-group descriptive summaries into means (SDs).
- **Human verification instruction:** Compare the D01 p. 7 ventilation row label and three-number cells with the D04 p. 18 footer, then confirm on D04 p. 4 that `difference in means` refers to the model effect estimate.

## C06 - Discussion calls day-10 urea summaries means although reported values are medians (IQR)

**Classification: Verified**

- **Location:** D01 `jama_summers_2025_oi_250040_1753124024.36498.pdf`, PDF p. 8, Discussion. Comparisons: D01 p. 5, Biochemical Outcomes; D04 `joi250040supp3_prod_1753124024.38098.pdf`, PDF p. 19, eTable 11.
- **Source statements/values:** D01 Discussion says, `In this trial, mean urea concentrations at day 10 were higher in the augmented protein group`. D01 Results says, `By day 10, median (IQR) blood urea concentration was 13.0 (8.2-18.8) mmol/L` in the augmented group and `10.6 (7.1-15.4) mmol/L` in the usual group. D04 eTable 11 repeats those values and states `Data are Median (IQR)`.
- **Logical basis:** The Discussion uses `mean` for the same day-10, between-group urea comparison that the Results and supplement report as medians (IQR). This verifies a central-tendency terminology inconsistency; it does not claim that the direction of an unreported mean comparison is false.
- **Human verification instruction:** Compare the exact day-10 sentence on D01 p. 8 with the labeled day-10 summaries on D01 p. 5 and the median (IQR) footer on D04 p. 19.

## C07 - Table 2 cross-reference points eFigure 6 to Supplement 1 instead of Supplement 3

**Classification: Verified**

- **Location:** D01 `jama_summers_2025_oi_250040_1753124024.36498.pdf`, PDF p. 7, Table 2 footnote f. Comparisons: D01 p. 4, Primary Outcome; D04 `joi250040supp3_prod_1753124024.38098.pdf`, PDF p. 27, eFigure 6.
- **Source statements:** Table 2 footnote f says, `Bayesian model diagram is shown in eFigure 6 in Supplement 1.` D01 p. 4 places `eFigure 5 and eFigure 6` in `Supplement 3`. D04 p. 27 visibly contains `eFigure 6: Bayesian model analysis`; D04 is the supplied file `joi250040supp3_prod_1753124024.38098.pdf`.
- **Logical basis:** The Table 2 footnote identifies Supplement 1, while the Results text and the actual supplied Supplement 3 file locate eFigure 6 in Supplement 3.
- **Human verification instruction:** Read footnote f on D01 p. 7, compare the Results cross-reference on D01 p. 4, and confirm the eFigure 6 heading on D04 p. 27.

## Verification disposition

All seven supplied candidates meet the project evidence standard at verification. No additional issues were searched for or added.
