# Statistical Consistency Checker Response

## Scope and evidence used

- DOC-001: `jamasurgery_dat_2025_oi_250075_1767031598.03318.pdf`, PDF pages 1-9 only. Page 10 was not audited by design.
- DOC-003: `soi250075supp2_prod_1767031598.05318.pdf`, PDF pages 1-3.
- Evidence maps used: DOC-001 `agent_responses/main_text_extractor.md` and DOC-003 `agent_responses/results_supplement_extractor.md`.
- Source verification used normalized native text and the retained renders for DOC-001 Tables 2-4 and DOC-003 eTable 2. DOC-002 protocol was not opened or used.
- External sources were not used. CI symmetry was not used as an error criterion.

## Candidate issues

### Candidate 1 - Corrupted pN N3 row in the postoperative-morbidity regression table

- **Category:** Statistical reporting inconsistency
- **Severity:** Moderate
- **Exact location:** DOC-003, `soi250075supp2_prod_1767031598.05318.pdf`, PDF p. 3, eTable 2, pN block, N3 row. Cross-check: DOC-001, `jamasurgery_dat_2025_oi_250075_1767031598.03318.pdf`, PDF p. 7 (journal p. 15), Table 4, Overall morbidity.
- **Reported values:** N0, 10/51 (19.6%), reference; N1-2, 16/83 (19.3%), OR 0.98 (95% CI, 0.41-2.36), P = .963; N3, **29/74 (25.7%), OR 0.431 (95% CI, 0.60-3.37), P = .431**. DOC-001 Table 4 reports 23 LDG plus 22 ODG patients with overall morbidity, total 45.
- **Logical/calculation basis:**
  - 29/74 = 39.2%, not 25.7%.
  - The pN morbidity numerators sum to 10 + 16 + 29 = 55, whereas the table's other complete variable partitions and DOC-001 Table 4 establish 45 morbidity events.
  - The displayed point estimate 0.431 lies outside its reported 95% CI of 0.60-3.37.
  - The direction is inconsistent: the displayed N3 morbidity rate exceeds the N0 rate, but OR 0.431 indicates lower odds.
  - With the displayed counts, the univariate N3-vs-N0 odds ratio is (29/45)/(10/41) = 2.64, not 0.431.
  - A possible typographic reconciliation, to be verified rather than assumed, is 19/74 = 25.7% and OR approximately 1.42; 10 + 16 + 19 = 45, and 1.42 lies within 0.60-3.37. The exact repetition of .431 as both the displayed OR and P value further supports a cell-placement/transcription check.
- **Verification instruction:** Inspect the source eTable 2 production data or author-verified analysis output for the N3 morbidity numerator, univariate OR, CI, and P value. Confirm which cells should read 19 rather than 29 and approximately 1.42 rather than 0.431; do not correct solely from inference.

### Candidate 2 - Surgical-approach estimate is called an independent/multivariable result in the article but is displayed only as univariate in eTable 2

- **Category:** Cross-document inconsistency
- **Severity:** Moderate
- **Exact locations:**
  - DOC-001, PDF p. 6 (journal p. 14), `Risk Factors Related to Postoperative Morbidity`: "In the multivariate analyses..." and "the surgical approach (LDG vs ODG) was not an independent predictor... (OR, 0.85; 95% CI, 0.44-1.63; P = .62) (eTable 2 in Supplement 2)."
  - DOC-003, PDF p. 3, eTable 2, Approach block: LDG 23/104 (22.1%), reference; ODG 22/104 (21.2%), OR 0.85 (95% CI, 0.44-1.63), P = .619 under **Univariate**; the multivariate OR and P-value cells are blank.
- **Logical basis:** The exact estimate, CI, and P value cited in the article as evidence that approach was not an "independent predictor" appear in the supplement's univariate columns, not its multivariate columns. The supplied package therefore does not document the claimed adjusted/independent estimate. The prose also labels the contrast "LDG vs ODG," while eTable 2 places the estimate on the ODG row with LDG as reference; the intended contrast direction should be confirmed.
- **Verification instruction:** Compare the fitted multivariable model output with the final eTable 2 column assignments. Determine whether approach was entered in the multivariable model and either populate/label the multivariable result or revise the main-text claim to univariate/nonindependent evidence with an explicit reference group.

### Candidate 3 - Age >=60 morbidity percentage and univariate OR do not agree with the displayed counts

- **Category:** Statistical reporting inconsistency
- **Severity:** Low to moderate
- **Exact location:** DOC-003, PDF p. 3, eTable 2, Age block.
- **Reported values:** Age <60: 13/88 (14.8%), reference. Age >=60: 32/120 (27.7%), univariate OR 2.28 (95% CI, 1.12-4.64), P = .040; multivariate OR 1.70 (95% CI, 0.79-3.65), P = .173.
- **Calculation/logical basis:** 32/120 = 26.7%, not 27.7%. Under the stated binary logistic-regression method, the unadjusted OR from the displayed dichotomous counts is (32/88)/(13/75) = 2.10, not 2.28. These differences exceed rounding and mean that the counts, percentage, and univariate OR cannot all describe the same 208 observations. The CI/null/P relationship itself is directionally consistent: 1 is outside 1.12-4.64 and P = .040 is below .05; no CI-symmetry inference was used.
- **Verification instruction:** Recompute the age-stratified 2-by-2 table and univariate logistic model from the analysis data, then verify both denominators, both event counts, the percentage, and the univariate estimate before deciding which printed value is wrong.

### Candidate 4 - Several additional eTable 2 univariate ORs do not reproduce from their displayed morbidity cells

- **Category:** Statistical reporting inconsistency
- **Severity:** Moderate
- **Exact location:** DOC-003, PDF p. 3, eTable 2, Sex, Approach, BMI, Comorbidity, and ASA blocks.
- **Reported versus count-derived ORs:**

| Contrast (nonreference vs reference) | Displayed morbidity cells | Reported univariate OR | OR from displayed cells |
|---|---:|---:|---:|
| Female vs male | 11/54 vs 34/154 | 0.97 | (11/43)/(34/120) = 0.90 |
| ODG vs LDG | 22/104 vs 23/104 | 0.85 | (22/82)/(23/81) = 0.94 |
| BMI >=25 vs <25 | 10/63 vs 35/145 | 0.64 | (10/53)/(35/110) = 0.59 |
| Comorbidity yes vs no | 33/113 vs 12/95 | 3.10 | (33/80)/(12/83) = 2.85 |
| ASA 3 vs ASA 1 | 27/113 vs 1/9 | 2.76 | (27/86)/(1/8) = 2.51 |

- **Logical basis:** For an unadjusted binary logistic regression with a categorical predictor, the point estimate for each displayed two-level contrast is fixed by the corresponding 2-by-2 counts. The discrepancies are about 7%-10%, exceed rounding, and are selective: other rows reproduce closely (eg, tumor size >=5 cm vs <5 cm, 1.747 vs reported 1.75; anemia yes vs no, 1.803 vs reported 1.80; GOO yes vs no, 0.646 vs reported 0.65). This pattern suggests that some morbidity cells and univariate model estimates may come from different data versions or that table values were transcribed inconsistently. No claim is made about raw-data validity.
- **Verification instruction:** Re-run each univariate categorical model from the locked analysis dataset and compare it with the exact eTable morbidity counts. Confirm whether the displayed counts or ORs need correction and whether any analysis-set/filter difference was intended and should be stated.

## No-issue checks

- **Comorbidity repeated multivariable result:** DOC-003 eTable 2 reports OR 2.42 (95% CI, 1.11-5.30), P = .026. DOC-001 Abstract p. 1 and Results p. 6 repeat OR 2.42 (95% CI, 1.11-5.30), P = .03. The P value is consistent rounding, the estimate lies within its CI, the CI excludes 1, P < .05, and the positive direction agrees with 33/113 (29.2%) vs 12/95 (12.6%).
- **Approach repeated numerical result:** Apart from the model-label/reference-direction issue in Candidate 2 and the count-derived OR issue in Candidate 4, the values repeat consistently: DOC-003 has 0.85 (0.44-1.63), P = .619; DOC-001 p. 6 has 0.85 (0.44-1.63), P = .62. The CI includes 1 and P > .05.
- **Main morbidity results:** DOC-001 Abstract p. 1, narrative p. 5, and Table 4 p. 7 consistently report overall morbidity 23/104 (22.1%) vs 22/104 (21.2%), P = .87, and major/severe complications 3/104 (2.9%) vs 4/104 (3.8%), P > .99. Outcome naming is reconciled by the explicit Clavien-Dindo grade >=IIIa definition.
- **Operative results:** DOC-001 Abstract p. 1, narrative p. 5, and Table 2 p. 5 consistently repeat operating time 220.0 (42.4) vs 153.7 (36.7), P < .001, and blood loss 80 (50-145) vs 50 (30-100), P = .003. Effect directions are stable across locations.
- **Recovery results:** DOC-001 narrative p. 6 and Table 4 p. 7 repeat the same values and P values for flatus, oral diet tolerance, hospital stay, and time to adjuvant chemotherapy. Because the method permits either a t test or Mann-Whitney U test as applicable, summary-statistic reconstruction was not used to challenge these P values.
- **Subgroup/category denominators:** DOC-003 pT denominators 64 + 144 = 208 agree with DOC-001 Table 3 totals for pT1-pT3 and pT4a. DOC-003 pN denominators 51 + 83 + 74 = 208 agree with DOC-001 Table 3 totals for N0, N1-2, and N3a/N3b. DOC-003 anastomosis denominators 163 + 45 = 208 agree with DOC-001 Table 2 totals for Billroth II and Roux-en-Y. The pN morbidity cells, not the subgroup labels or denominators, are the problem in Candidate 1.
- **Participant denominators:** DOC-001 Abstract, Figure, Results, Tables 1-4, and DOC-003 eTable 2 consistently use 208 analyzed participants, 104 LDG and 104 ODG. No analyzed-population denominator conflict was located.
- **Confidence-interval checks:** No issue was raised from CI symmetry or reconstructed standard errors. All ordinary reported ORs fall within their CIs except the pN N3 row in Candidate 1. CI/null/P direction agrees elsewhere: CIs excluding 1 have P < .05 and CIs including 1 have P > .05.

## Disposition

Four local candidates are submitted for evidence verification. No protocol/SAP evidence, external knowledge, methodological critique, misconduct inference, or clinical-appropriateness judgment was used.
