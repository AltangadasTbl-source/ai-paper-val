# Stable Candidate Ledger

All candidates below are **Pending Human Adjudication**. Exact duplicates across numeric, statistical-pass-1, and cross-source lanes were merged before stable IDs; candidates concerning different printed rows or values were retained separately. No count target, severity, or AI adjudication was applied.

## C001 — Reversed endpoint in the eTable 2 PEEP interquartile range

- **Category:** Numeric or arithmetic inconsistency
- **Source location:** DOC-004, `joi180108supp3_prod.pdf`, PDF p. 6, eTable 2, Other Mode of Ventilation, after titration on randomization day, intermediate arm, PEEP.
- **Printed evidence and rule:** `8 (5-1)` cm H2O in a table defined as median (IQR). The required ordering is lower quartile <= median <= upper quartile; `5 <= 8` but `8 <= 1` is false.
- **Alternative and human question:** A typesetting error is possible, but no replacement endpoint is supplied. What are the intended quartiles?
- **Lane provenance:** NF001; SF013; XF002.

## C002 — At-risk-for-ARDS percentages use undisclosed denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, Patients at risk for ARDS, arm headers n=477 and n=484.
- **Printed evidence and rule:** `292 (61.6)` and `290 (60.3)`; 292/477=61.2% and 290/484=59.9%, while denominators 474 and 481 reproduce the printed percentages.
- **Alternative and human question:** Available-case denominators may have been used but are not printed. What exact denominators and missing counts apply?
- **Lane provenance:** NF002; contextual overlap with XF003, retained separately because it concerns distinct printed values.

## C003 — Septic-shock percentages use undisclosed denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, Septic shock, arm headers n=477 and n=484.
- **Printed evidence and rule:** `82 (17.6)` and `74 (15.5)`; 82/477=17.2% and 74/484=15.3%, not the displayed percentages.
- **Alternative and human question:** Available-case reporting may explain the values, but no row denominators are supplied. What exact denominators were used?
- **Lane provenance:** NF003; contextual overlap with XF003, retained separately because it concerns distinct printed values.

## C004 — Tobacco-use categories use undisclosed denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, Tobacco use, arm headers n=477 and n=484.
- **Printed evidence and rule:** Category counts total 475 in the low arm and 482 in the intermediate arm, below the headers; displayed percentages use smaller variable-specific denominators rather than the arm totals.
- **Alternative and human question:** Missing baseline values may explain the smaller totals despite an Unknown category. What denominators and missingness rule were intended?
- **Lane provenance:** NF004; XF003.

## C005 — Alcohol-use categories use undisclosed denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, Alcohol use, arm headers n=477 and n=484.
- **Printed evidence and rule:** Category counts total 475 and 482; percentages such as 121/475=25.5% and 92/482=19.1% use these smaller totals, which are not identified.
- **Alternative and human question:** Variable-specific available-case denominators may apply. Should 475/482 and the missing counts be disclosed?
- **Lane provenance:** NF005; XF003.

## C006 — ICU-admission categories use undisclosed denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, Reason for ICU admission, arm headers n=477 and n=484.
- **Printed evidence and rule:** Surgical plus medical counts equal 475 and 482; percentages reproduce those totals (for example 82/475=17.3% and 79/482=16.4%), not the arm headers.
- **Alternative and human question:** Two patients per arm may be omitted for a source-grounded reason that is not printed. What denominators and missing categories apply?
- **Lane provenance:** NF010; XF003.

## C007 — Sedative-infusion percentages omit effective denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Source location:** DOC-004, `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Sedative infusion, arm headers n=477 and n=484.
- **Printed evidence and rule:** `320 (70.6)` and `333 (72.1)`; arm-header calculations give 67.1% and 68.8%, while approximately 453/462 reproduce the displayed percentages.
- **Alternative and human question:** A complete-case subset may apply. What exact row totals were used, and should they be printed?
- **Lane provenance:** NF006; SF014; XF005.

## C008 — Analgesic-infusion percentages omit effective denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Source location:** DOC-004, `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Analgesic infusion, arm headers n=477 and n=484.
- **Printed evidence and rule:** `277 (61.1)` and `273 (59.1)`; arm-header calculations give 58.1% and 56.4%, while 453/462 reproduce the displayed percentages.
- **Alternative and human question:** A complete-case subset may apply. What exact row totals were used, and should they be printed?
- **Lane provenance:** NF007; SF015; XF005.

## C009 — Neuromuscular-blockade percentages omit effective denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Source location:** DOC-004, `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Neuromuscular blockade, arm headers n=477 and n=484.
- **Printed evidence and rule:** `53 (11.7)` and `60 (13.0)`; arm-header calculations give 11.1% and 12.4%, while 53/453=11.7% and 60/462=13.0%.
- **Alternative and human question:** A complete-case subset may apply. What exact row totals were used, and should they be printed?
- **Lane provenance:** NF008; SF016; XF005.

## C010 — Vasopressor-use percentages omit effective denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Source location:** DOC-004, `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Use of vasopressors, arm headers n=477 and n=484.
- **Printed evidence and rule:** `363 (80.0)` and `353 (76.4)`; arm-header calculations give 76.1% and 72.9%, while 454/462 reproduce the displayed percentages.
- **Alternative and human question:** A complete-case subset may apply. What exact row totals were used, and should they be printed?
- **Lane provenance:** NF009; SF017; XF005.

## C011 — Mortality effect-measure wording conflicts with Table 2 and the SAP

- **Category:** Measure, label, or scale inconsistency
- **Source locations:** DOC-001 PDF p. 4 Statistical Analysis and p. 6 Table 2/footnotes; DOC-003 `joi180108supp2_prod.pdf`, PDF p. 13.
- **Printed evidence and rule:** Main Methods says ICU/hospital length of stay and mortality rates were compared using Kaplan-Meier/Cox and reported as HRs; Table 2 labels ICU and hospital mortality as RR, and the SAP specifically assigns RR to ICU/hospital mortality and Cox HR to 28/90-day mortality.
- **Alternative and human question:** The main Methods sentence may be overbroad. Which model/effect measure was used for ICU and hospital mortality, and which label should be clarified?
- **Lane provenance:** SF001; S008/S009 cross-source review context.

## C012 — ICU-mortality RR does not reproduce from printed risks

- **Category:** Statistical reporting inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, ICU mortality and footnote c.
- **Printed evidence and rule:** Low 132/450 and intermediate 115/458 with printed RR 1.11; (132/450)/(115/458)=1.167, which rounds to 1.17.
- **Alternative and human question:** An unreported model or population may underlie 1.11. What estimator and denominator population generated it?
- **Lane provenance:** SF002.

## C013 — Hospital-mortality RR does not reproduce from printed risks

- **Category:** Statistical reporting inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, hospital mortality and footnote c.
- **Printed evidence and rule:** Low 151/477 and intermediate 140/484 with printed RR 1.06; the displayed-risk ratio is 1.094, which rounds to 1.09.
- **Alternative and human question:** An unreported estimator may underlie 1.06. What model or population generated it?
- **Lane provenance:** SF003.

## C014 — ARDS RR does not reproduce from printed risks

- **Category:** Statistical reporting inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, ARDS and footnote c.
- **Printed evidence and rule:** Low 17/448 and intermediate 23/462 with printed RR 0.86; the displayed-risk ratio is 0.762, which rounds to 0.76.
- **Alternative and human question:** An unreported estimator/population may apply. What produced RR 0.86?
- **Lane provenance:** SF004.

## C015 — Pneumonia RR does not reproduce from printed risks

- **Category:** Statistical reporting inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, pneumonia and footnote c.
- **Printed evidence and rule:** Low 19/450 and intermediate 17/462 with printed RR 1.07; the displayed-risk ratio is 1.147, which rounds to 1.15.
- **Alternative and human question:** An unreported estimator/population may apply. What produced RR 1.07?
- **Lane provenance:** SF005.

## C016 — Pneumothorax RR does not reproduce from printed risks

- **Category:** Statistical reporting inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, pneumothorax and footnote c.
- **Printed evidence and rule:** Low 8/448 and intermediate 6/462 with printed RR 1.16; the displayed-risk ratio is 1.375, which rounds to 1.38.
- **Alternative and human question:** An unreported estimator/population may apply. What produced RR 1.16?
- **Lane provenance:** SF006.

## C017 — Atelectasis RR does not reproduce from printed risks

- **Category:** Statistical reporting inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, atelectasis and footnote c.
- **Printed evidence and rule:** Low 51/449 and intermediate 52/464 with printed RR 1.00; the displayed-risk ratio is 1.014, which rounds to 1.01.
- **Alternative and human question:** Model derivation or greater unprinted precision could explain the small difference. What produced the printed RR 1.00?
- **Lane provenance:** SF007.

## C018 — Extrapulmonary-infection RR does not reproduce from printed risks

- **Category:** Statistical reporting inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, extrapulmonary infection and footnote c.
- **Printed evidence and rule:** Low 20/448 and intermediate 28/463 with printed RR 0.84; the displayed-risk ratio is 0.738, which rounds to 0.74.
- **Alternative and human question:** An unreported estimator/population may apply. What produced RR 0.84?
- **Lane provenance:** SF008.

## C019 — Extrapulmonary-sepsis RR does not reproduce from printed risks

- **Category:** Statistical reporting inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, extrapulmonary sepsis and footnote c.
- **Printed evidence and rule:** Low 12/448 and intermediate 16/463 with printed RR 0.87; the displayed-risk ratio is 0.775, which rounds to 0.78.
- **Alternative and human question:** An unreported estimator/population may apply. What produced RR 0.87?
- **Lane provenance:** SF009.

## C020 — Delirium RR does not reproduce from printed risks

- **Category:** Statistical reporting inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, delirium and footnote c.
- **Printed evidence and rule:** Low 149/343 and intermediate 132/361 with printed RR 1.15; the displayed-risk ratio is 1.188, which rounds to 1.19.
- **Alternative and human question:** An unreported estimator/population may apply. What produced RR 1.15?
- **Lane provenance:** SF010.

## C021 — Tracheostomy RR does not reproduce from printed risks

- **Category:** Statistical reporting inconsistency
- **Source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 6, Table 2, need for tracheostomy and footnote c.
- **Printed evidence and rule:** Low 54/477 and intermediate 52/484 with printed RR 1.03; the displayed-risk ratio is 1.054, which rounds to 1.05.
- **Alternative and human question:** An unreported estimator/population may apply. What produced RR 1.03?
- **Lane provenance:** SF011.

## C022 — The same subgroup intervals are labelled IQR and 95% CI

- **Category:** Measure, label, or scale inconsistency
- **Source locations:** DOC-001 PDF p. 6, Subgroups and Exploratory Analyses; DOC-004 `joi180108supp3_prod.pdf`, PDF p. 9, eTable 5.
- **Printed evidence and rule:** Main text calls the inside-ICU -2.50 (-4.63 to -0.36) and outside-ICU 1.45 (-0.52 to 3.43) intervals IQRs; eTable 5 prints the identical values under Mean Difference (95% CI).
- **Alternative and human question:** The narrative may contain a label transcription error. Are these 95% CIs, and which source label should be corrected?
- **Lane provenance:** SF012; XF001.

## C023 — Enrollment completion dates differ by two days

- **Category:** Cross-document numeric inconsistency
- **Source locations:** DOC-001 `jama_simonis_2018_oi_180108.pdf`, PDF pp. 1 and 5; DOC-003 `joi180108supp2_prod.pdf`, PDF pp. 3 and 5.
- **Printed evidence and rule:** The main article reports enrollment through August 20, 2017; the SAP says enrollment was complete on August 22, 2017, for the same trial.
- **Alternative and human question:** The dates may refer to last randomization versus administrative completion, but the supplied sources do not define that distinction. What operational event does each date represent?
- **Lane provenance:** XF004.

**Stable candidate count:** 23. Every item remains **Pending Human Adjudication**.
