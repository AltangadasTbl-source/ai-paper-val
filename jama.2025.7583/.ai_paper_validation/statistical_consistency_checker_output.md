# Statistical consistency checker output

- **Article package:** `jama.2025.7583`
- **Audited documents:** DOC-001-MAIN and DOC-004-RESULTS-SUPP
- **Evidence used:** source-mapped main-text evidence map; source-mapped results-supplement evidence map; native/normalized page text; rendered source pages for DOC-001-MAIN PDF pp. 5-6 and DOC-004-RESULTS-SUPP PDF pp. 9 and 14-15.
- **Excluded by design:** DOC-002-PROTOCOL, DOC-003-ADMIN, and DOC-005-SAP.
- **External sources:** none.

## Retained local candidates

**None.** No document-grounded statistical reporting inconsistency was verified.

## Rejected checks

### R1 - Primary result is consistent across repeated locations

- **Status:** Rejected.
- **Locations and values:**
  - DOC-001-MAIN PDF p. 1, Abstract, Results: 24/162 (14.8%) vs 33/157 (21.0%); after imputation OR 0.64 (95% CI, 0.36-1.14); adjusted absolute difference -6% (95% CI, -14% to 2%); P=.13.
  - DOC-001-MAIN PDF p. 2, Key Points: adjusted OR 0.64 (95% CI, 0.36-1.14).
  - DOC-001-MAIN PDF p. 5, Results, Primary End Point: the same counts, OR, CI, adjusted absolute difference, CI, and P value.
  - DOC-001-MAIN PDF p. 6, Table 2 and Figure 2: 24/162 vs 33/157; adjusted absolute difference -0.06 (95% CI, -0.14 to 0.02); P=.13; all-patient OR 0.64 (95% CI, 0.36-1.14).
  - DOC-004-RESULTS-SUPP PDF p. 9, eFigure 2, primary row: 24/162 vs 33/157; OR 0.64 (95% CI, 0.36-1.14); P=.13.
  - DOC-004-RESULTS-SUPP PDF p. 15, eTable 4, EMPROTECT row: 24/162 (14.8%) vs 33/157 (21.0%); ITT with imputation OR 0.64 (95% CI, 0.36-1.14); P=.13.
- **Reasoning:** Every repeated OR and CI agrees. The OR CI contains 1 and the adjusted absolute-difference CI contains 0, consistent with P=.13 and the article's "not statistically significant" wording. The lower observed recurrence proportion in the embolization arm is directionally consistent with OR <1 and a negative risk difference.
- **Verification instruction:** Compare the cited rows side by side and confirm the identical values and null-value relationships.

### R2 - On-site sensitivity analysis is consistent between main text and supplement

- **Status:** Rejected.
- **Locations and values:**
  - DOC-001-MAIN PDF p. 5, Results, Primary End Point: OR 0.61 (95% CI, 0.35-1.06); P=.08.
  - DOC-004-RESULTS-SUPP PDF p. 9, eFigure 2, "On site assessment": 27/162 vs 38/156; OR 0.61 (95% CI, 0.35-1.06); P=.08.
- **Reasoning:** The estimate, CI, and P value repeat exactly. The CI contains 1 and P>.05; the lower event proportion in the embolization arm agrees with OR <1.
- **Verification instruction:** Read the p. 5 sentence and the p. 9 "On site assessment" row.

### R3 - eFigure 2 sensitivity-analysis CIs and P values are null-consistent

- **Status:** Rejected.
- **Location:** DOC-004-RESULTS-SUPP PDF p. 9, eFigure 2.
- **Values:**
  - Primary, multiple imputation: OR 0.64 (0.36-1.14), P=.13.
  - Complete cases: OR 0.64 (0.35-1.14), P=.13.
  - On-site assessment, multiple imputation: OR 0.61 (0.35-1.06), P=.08.
  - Adjudicated cases, no multiple imputation: OR 0.66 (0.37-1.19), P=.17.
  - Excluding non-embolized MMA patients, multiple imputation: OR 0.71 (0.39-1.30), P=.27.
- **Reasoning:** Each CI contains the OR null value 1 and each P value exceeds .05. The primary and complete-case lower CI limits (0.36 vs 0.35) are not an erroneous repeated CI because the rows identify different analysis populations/missing-data approaches.
- **Verification instruction:** Inspect all five eFigure 2 rows and their population labels.

### R4 - Secondary-outcome CI/null and P-value relationships are consistent

- **Status:** Rejected.
- **Location:** DOC-001-MAIN PDF p. 6, Table 2; repeated counts/P values also appear in the Secondary End Points text on p. 6 and, for repeat surgery, the Abstract on p. 1.
- **Values and basis:**
  - Repeat surgery: 7/162 (4.3%) vs 13/157 (8.3%); difference -4.0% (95% CI, -9.4% to 1.4%); P=.14. The CI contains 0 and P>.05. Recalculation of the stated Pearson chi-square test from the displayed 2x2 counts gives P=0.1447, which rounds to .14.
  - Disability/dependency at 1 month: difference 3.8% (95% CI, -2.3% to 9.9%); P=.22. The CI contains 0 and P>.05.
  - Disability/dependency at 6 months: difference 0.8% (95% CI, -5.2% to 6.8%); P=.79. The CI contains 0 and P>.05.
  - Mortality at 1 month: 3/165 vs 3/165; difference 0% (95% CI, -3.0% to 3.0%); P=1.00. The displayed equal counts and CI containing 0 agree; recalculation of the stated two-sided Fisher exact test gives P=1.00.
  - Mortality at 6 months: 9/165 vs 13/165; difference -2.4% (95% CI, -7.9% to 2.9%); P=.38. The CI contains 0 and P>.05; recalculation of the stated Pearson chi-square test gives P=0.3774, which rounds to .38.
  - Hospital stay: median difference 1 day (95% CI, -1 to 5); P=.12. The CI contains 0 and P>.05.
- **Reasoning:** No CI-versus-null/P-value conflict or direction reversal is present.
- **Verification instruction:** Recheck Table 2 values and footnotes d-i; for the count outcomes, reconstruct the displayed 2x2 tables.

### R5 - Subgroup labels, denominators, directions, and interaction claims are consistent

- **Status:** Rejected.
- **Location:** DOC-001-MAIN PDF p. 6, Figure 2; prespecified subgroup definitions are on DOC-001-MAIN PDF p. 3, Statistical Analysis.
- **Values:**
  - Unilateral CSDH: 12/118 vs 22/117; OR 0.51 (95% CI, 0.25-1.07).
  - Bilateral CSDH: 12/44 vs 11/40; OR 1.03 (95% CI, 0.39-2.67); interaction P=.32 for localization.
  - No anticoagulant/antiplatelet medication: 5/51 vs 13/50; OR 0.34 (95% CI, 0.11-1.03).
  - Medication use: 19/111 vs 20/107; OR 0.83 (95% CI, 0.43-1.59); interaction P=.18 for medication use.
  - The subgroup denominators sum to the all-patient observed denominators in each arm: 118+44=162, 117+40=157, 51+111=162, and 50+107=157.
- **Reasoning:** Each label agrees with the prespecified factor and the displayed event proportions agree with the OR direction. Every subgroup CI contains 1, and both interaction P values exceed .05, consistent with the text stating that interaction tests were not statistically significant.
- **Verification instruction:** Verify labels and denominator sums directly in Figure 2 and compare with the two subgroup factors named on p. 3.

### R6 - Main-versus-supplement event denominators and components align

- **Status:** Rejected.
- **Locations and values:**
  - DOC-001-MAIN PDF p. 5 and p. 6, Table 2: 24 recurrence events in the embolization arm (22 adjudicated recurrences plus 2 neurological/undetermined deaths) and 33 in standard care (32 plus 1).
  - DOC-004-RESULTS-SUPP PDF p. 11, eTable 2: recurrence-event column denominators N=24, N=33, and overall N=57; neurological/undetermined deaths are 2/24, 1/33, and 3/57.
  - Repeat surgery is 7 in the embolization arm and 13 in standard care in both DOC-001-MAIN Table 2 (p. 6) and DOC-004-RESULTS-SUPP eTable 2 (p. 11).
- **Reasoning:** The component counts reproduce the main event totals and repeated surgery counts without a cross-document denominator conflict.
- **Verification instruction:** Compare the main Table 2 primary-event component rows with eTable 2's headers and death/repeat-surgery rows.

### R7 - Contextual eTable 4 CI/P-value relationships are internally coherent

- **Status:** Rejected.
- **Location:** DOC-004-RESULTS-SUPP PDF pp. 14-15, eTable 4.
- **Values and reasoning:**
  - EMBOLISE: RR 0.36 (95% CI, 0.11-0.80), P=.008; CI excludes 1 and P<.05.
  - STEM: OR 0.36 (95% CI, 0.20-0.66), P=.001; CI excludes 1 and P<.05.
  - MAGIC-MT: difference -3.3 percentage points (95% CI, -7.4 to 0.8), P=.10; CI contains 0 and P>.05.
  - EMPROTECT: OR 0.64 (95% CI, 0.36-1.14), P=.13; CI contains 1 and P>.05.
- **Reasoning:** No CI-versus-null/P-value conflict is visible within the supplied summary. EMPROTECT repeats the main-article values exactly. The other trials were checked only for internal relationships within supplied DOC-004, not against external articles.
- **Verification instruction:** Read the "Primary outcome" cells of eTable 4; do not externally retrieve the summarized trials.

## Uncertain checks

### U1 - Exact adjusted/MI regression calculations

- **Status:** Uncertain; not a candidate.
- **Locations:** DOC-001-MAIN PDF pp. 3, 5-6; DOC-004-RESULTS-SUPP PDF pp. 6 and 9.
- **Reasoning:** The package reports logistic regression adjusted for medication use and CSDH localization, multiple imputation with 10 datasets, and Rubin pooling. Aggregate displayed counts are insufficient to reproduce exact adjusted OR CIs or P values. Only the model-independent null-value and direction checks above are valid.
- **Verification instruction:** Reproduce only from the patient-level analytic data and imputation/model specification, if made available; do not infer an error from aggregate counts.

### U2 - Confidence-interval symmetry

- **Status:** Uncertain; not a candidate.
- **Locations:** DOC-001-MAIN PDF p. 3, Statistical Analysis; p. 6, Table 2 footnotes b and g.
- **Reasoning:** The primary adjusted risk-difference CI was obtained by bootstrap, and disability/dependency CIs were obtained using generalized estimating equations. Symmetry around the displayed point estimate is therefore not assumed and was not used as an error screen.
- **Verification instruction:** Check against the original bootstrap/GEE output only.

### U3 - Interaction, GEE, and Wilcoxon P values

- **Status:** Uncertain; not a candidate.
- **Locations:** DOC-001-MAIN PDF p. 6, Figure 2 interaction P values .32 and .18; Table 2 disability P values .22 and .79; hospital-stay P=.12.
- **Reasoning:** Interaction-model, GEE, and rank-sum statistics cannot be reconstructed from the displayed subgroup event counts, percentages, medians, and IQRs alone. Their reported CI/null relationships and qualitative claims are coherent, but exact recalculation is not document-grounded.
- **Verification instruction:** Compare with the underlying fitted-model and rank-sum output if available.

### U4 - Observed fractions beside multiply imputed analyses

- **Status:** Rejected as an inconsistency; retained here as a presentation audit note.
- **Locations:** DOC-004-RESULTS-SUPP PDF p. 9, eFigure 2; DOC-001-MAIN PDF p. 6, Table 2 footnote a.
- **Reasoning:** eFigure 2 places observed fractions (eg, 24/162 and 33/157) beside rows labeled "full analysis set, multiple imputation." This could appear ambiguous in isolation, but main Table 2 footnote a explicitly states that case numbers and percentages are observed values before imputation, while the inferential estimate is after imputation. The supplied documents therefore resolve the apparent conflict.
- **Verification instruction:** Read eFigure 2 together with main Table 2 footnotes a-c.
