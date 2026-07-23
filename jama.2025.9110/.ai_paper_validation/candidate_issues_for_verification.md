# Coordinator Candidate Set for Evidence Verification

Package: `jama.2025.9110`

Scope: deduplicated findings from the table-arithmetic, figure/flow, and statistical-consistency checks. Seven candidates retained, within the package maximum of 10. D02 protocol and D03 SAP were not used. No external sources or unstated external knowledge were used.

## C01 — Period 3 augmented-protein sex counts do not reconcile to the group denominator

- Proposed category: Arithmetic inconsistency
- Source: `joi250040supp3_prod_1753124024.38098.pdf` (D04), p. 10, eTable 4, Sex rows, Period 3 augmented-protein column.
- Values: group `n=551`; male `359 (65.2%)`; female `190 (34.5%)`.
- Basis: `359 + 190 = 549`, two fewer than 551; percentages total 99.7%. Aggregating period sex counts also yields 1069 male and 610 female, while D01 Table 1 reports 1070 and 611 among 1681 augmented participants.
- Verification: inspect the original rendered table and source-linked text; determine whether counts are incorrect or an undisclosed missing/other category explains the difference.

## C02 — Protocol-deviation participant percentage appears calculated from the event count

- Proposed category: Arithmetic inconsistency
- Source: D04 p. 16, eTable 8, augmented-protein total protocol deviations.
- Values: denominator `1681`; participants with at least one event `151 (9.4%)`; number of events `158`.
- Basis: `151/1681 = 8.98%`, rounding to 9.0%; `158/1681 = 9.40%`, matching the displayed percentage.
- Verification: inspect the source table and recalculate the participant percentage.

## C03 — Patient boxes use patient-level randomization wording in a cluster-randomized trial

- Proposed category: Presentation inconsistency
- Source: `jama_summers_2025_oi_250040_1753124024.36498.pdf` (D01), p. 3, Figure 1; comparison statements on D01 pp. 2 and 8.
- Values/statements: four patient-count boxes say “Randomized to…”; Methods say ICUs were randomly assigned and participants received the formula to which the ICU was randomized; Limitations states randomization occurred at cluster, not patient, level.
- Basis: the figure terminology visually attributes randomization to patients, inconsistent with the stated unit of randomization.
- Verification: compare the visible figure labels with the Methods and Limitations wording.

## C04 — Bayesian primary-outcome row labels median/IQR values as mean (SD)

- Proposed category: Statistical reporting inconsistency
- Source: D01 p. 7, Table 2, Bayesian quantile mixed-model row; D04 p. 27, eFigure 6.
- Values/statements: group cells `62.0 (0 to 77)` and `64.0 (0 to 77)` are labeled “mean (SD),” while the effect is a median difference `−1.50 (−3.86 to 0.90)` and eFigure 6 identifies the same median-difference analysis.
- Basis: each group cell gives a center with lower and upper quartiles, not a mean with one SD; the quantile-model analysis and effect label identify medians.
- Verification: inspect the original Table 2 row and eFigure 6; compare with the primary row’s median (IQR) label.

## C05 — Ventilation group summaries are labeled mean (SD) in the main table but median (IQR) in the supplement

- Proposed category: Cross-document inconsistency
- Source: D01 p. 7, Table 2, duration of invasive ventilation; D04 p. 18, eTable 10; D04 p. 4, eMethods.
- Values/statements: D01 displays `84.0 (35.0 to 178.9)` vs `78.0 (33.2 to 161.0)` under “mean (SD)”; D04 eTable 10 says data are median (IQR). The tobit-model effect is separately a difference in means.
- Basis: the main-table descriptive label conflicts with the supplement’s description of the same three-number group summaries; the model-based mean difference does not change the group summary statistic.
- Verification: inspect both source tables and the eMethods statement.

## C06 — Discussion calls day-10 urea summaries means although reported values are medians (IQR)

- Proposed category: Statistical reporting inconsistency
- Source: D01 p. 8, Discussion; D01 p. 5, Biochemical Outcomes; D04 p. 19, eTable 11.
- Values/statements: Discussion says “mean urea concentrations”; Results and eTable 11 report median (IQR) `13.0 (8.2-18.8)` vs `10.6 (7.1-15.4)` mmol/L.
- Basis: the narrative uses a different central-tendency statistic from every reported numeric summary for that comparison.
- Verification: compare the exact Discussion sentence with Results and eTable 11.

## C07 — Table 2 cross-reference points eFigure 6 to Supplement 1 instead of Supplement 3

- Proposed category: Presentation inconsistency
- Source: D01 p. 7, Table 2 footnote f; D01 p. 4, Primary Outcome; D04 p. 27, eFigure 6.
- Values/statements: footnote f says eFigure 6 is in Supplement 1; Results locates eFigures 5 and 6 in Supplement 3; the supplied D04 is Supplement 3 and contains eFigure 6 on p. 27.
- Basis: the table footnote conflicts with both the Results text and the supplied figure’s document location.
- Verification: inspect the footnote, the Results cross-reference, and D04 heading/page 27.

## Priority order

1. C01 and C02 — exact arithmetic errors.
2. C05 and C07 — cross-document/table-reference contradictions.
3. C04 and C06 — statistic-label inconsistencies.
4. C03 — figure terminology inconsistent with the declared randomization unit.

