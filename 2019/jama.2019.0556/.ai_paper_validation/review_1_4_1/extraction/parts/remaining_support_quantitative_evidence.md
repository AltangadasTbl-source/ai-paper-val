# Support-003 quantitative evidence map

**Mapper:** `qc14_support_quantitative_mapper` repair shard `support-003`  
**Scope completed:** DOC-003 `joi190007supp2_prod.pdf` PDF pp. 1-5; DOC-004 `joi190007supp3_prod.pdf` PDF pp. 3-15 and 24-25; DOC-005 `joi190007supp4_prod.pdf` PDF p. 1.  
**Method:** Direct PDF text extraction was read for every assigned page. This is an evidence and relationship map, not a candidate assessment. `R-N` and `R-S` IDs are mapper-local only.

## DOC-003 — analysis-plan form

Source: [joi190007supp2_prod.pdf — PDF pp. 1-5](../../../../joi190007supp2_prod.pdf#page=1).

### Population, interventions, outcomes, and denominator rules

| Local ID | Evidence and relationship map | Exact location |
|---|---|---|
| R-N-001 | Planned data waves are T0, T3, T6, T9, and T12. The stated study question compares two nutritional strategies—multi-nutrient supplementation (A) and food-related behavioral change therapy (B)—for preventing depression in high-risk overweight people with subsyndromal depressive symptoms. | [DOC-003 p. 1](../../../../joi190007supp2_prod.pdf#page=1), [p. 2](../../../../joi190007supp2_prod.pdf#page=2) |
| R-N-002 | Primary outcome is cumulative onset of MDD since T0, binary and measured with the MINI 5.0 plus MDD section: `yes=1` if an MDD episode occurs between T0-T12 (positive at T3, T6, or T12); `no=0` only if negative at T3, T6, and T12. This defines the numerator/event identity and the follow-up denominator condition. | [DOC-003 p. 2](../../../../joi190007supp2_prod.pdf#page=2) |
| R-N-003 | Secondary continuous depressive-symptom outcomes: PHQ-9 and IDS30-SR at T3, T6, and T12. Other listed outcomes are GAD-7 anxiety symptoms and HRQoL measured with EQ-5D-5L. | [DOC-003 p. 2](../../../../joi190007supp2_prod.pdf#page=2) |
| R-N-004 | Stratification covariates for all analyses are baseline MINI history of MDD (yes/no) and center (AMS, LEI, EXE, MAL). Other covariates are not default primary-analysis adjustments but may be used secondarily. | [DOC-003 p. 2](../../../../joi190007supp2_prod.pdf#page=2), [p. 3](../../../../joi190007supp2_prod.pdf#page=3) |
| R-N-005 | Planned flow display: counts screened, randomized, allocated to each intervention, followed up, and analyzed. Planned baseline table has four columns, one for each intervention combination, and includes listed demographic, clinical, behavioral, dietary, medication/supplement, and center variables. No numerical result is displayed in this plan. | [DOC-003 p. 3](../../../../joi190007supp2_prod.pdf#page=3) |
| R-N-006 | Planned adherence/descriptive quantities include Morisky self-report compliance, percentage of multi-nutrient pills taken, reasons for noncompliance, sessions attended, food-related-behavior change, and use of other therapies. Supplement biomarker comparison: vitamin D, selenium, folic acid, n-3 PUFA (EPA/DHA) at T6/T12, adjusted for corresponding T0 concentration. FBC compliance comparisons: food-related behavior at T3/T6/T12 and FFQ dietary intake at T6/T12, adjusted for matching T0 data. | [DOC-003 p. 3](../../../../joi190007supp2_prod.pdf#page=3) |
| R-N-007 | Primary-analysis population is intention-to-treat. Secondary CACE contrasts persons allocated to intervention who complied with persons in control who would have complied if offered treatment. Compliance definitions: supplements at least 70% taken over 12 months, using weighed jars or, if unavailable, self-report averaged over T3/T6/T9/T12; F-BA at least 8 of 21 sessions over 12 months. | [DOC-003 p. 4](../../../../joi190007supp2_prod.pdf#page=4) |
| R-N-008 | Planned adverse events/side effects are to be described by group; planned blinding report asks which supplement intervention participants thought they received. No event counts, denominators, or blinding results appear on assigned pages. | [DOC-003 p. 3](../../../../joi190007supp2_prod.pdf#page=3) |

### Prespecified statistical relationships

| Local ID | Evidence and relationship map | Exact location |
|---|---|---|
| R-S-001 | For binary cumulative MDD onset, logistic regression estimates each intervention effect; reported outputs are odds ratios, 95% CIs, and P values. A and B are effect-coded and both main effects and their interaction are planned. | [DOC-003 p. 3](../../../../joi190007supp2_prod.pdf#page=3) |
| R-S-002 | Secondary outcomes are planned for mixed models or generalized estimating equations, reporting regression coefficients, 95% CIs, and P values. In addition to stratification covariates, baseline depression score is adjusted for; T12 continuous outcomes are to display between-group standardized mean differences with 95% CIs and P values. | [DOC-003 p. 3](../../../../joi190007supp2_prod.pdf#page=3) |
| R-S-003 | All statistical tests are planned two-sided with significance threshold `P 0.05` (printed without an inequality sign). | [DOC-003 p. 3](../../../../joi190007supp2_prod.pdf#page=3) |
| R-S-004 | Multiplicative interaction for primary outcome is the A*B term in logistic regression, with independent variables and covariates. A sensitivity analysis defines biological interaction as departure from additivity of relative risks, using RERI from a linear odds-ratio model; RERI >0 indicates departure, likelihood-based 95% CIs are planned, and preventive conditions are recoded so the assumed-lowest-risk joint stratum is reference. | [DOC-003 p. 4](../../../../joi190007supp2_prod.pdf#page=4) |
| R-S-005 | Secondary time-to-MDD-onset analysis uses Cox regression and reports hazard ratios, 95% CIs, and P values. | [DOC-003 p. 4](../../../../joi190007supp2_prod.pdf#page=4) |
| R-S-006 | Prespecified effect-modification tests concern history of depression and center. Logistic models include A, B, MDD history, center, and appropriate interaction terms (examples A*MDD history and B*MDD history); one interaction P<0.05 defines statistically significant effect modification, to be shown stratified or in text. | [DOC-003 p. 4](../../../../joi190007supp2_prod.pdf#page=4), [p. 5](../../../../joi190007supp2_prod.pdf#page=5) |
| R-S-007 | Missingness is to be inspected by frequency and nature; FIML or MI used as appropriate. If MI is used, 100 datasets impute missing primary outcome under MAR and estimates are combined with Rubin's rules; sensitivity analyses are planned because missing-data assumptions are unverifiable. Outlier sensitivity analyses and log transformations are planned if needed for model assumptions/non-normal data. | [DOC-003 p. 5](../../../../joi190007supp2_prod.pdf#page=5) |

## DOC-004 — online supplement appendices and references

Source: [joi190007supp3_prod.pdf — assigned PDF pp. 3-15](../../../../joi190007supp3_prod.pdf#page=3); [assigned PDF pp. 24-25](../../../../joi190007supp3_prod.pdf#page=24).

### Eligibility, exposure, intervention dose, and outcome-scale definitions

| Local ID | Evidence and relationship map | Exact location |
|---|---|---|
| R-N-009 | Eligibility: online inclusion age 18-75 years, BMI 25-40 kg/m2, and PHQ-9 >=5. Telephone exclusions include current MDD within past 6 months under DSM-IV, antidepressant drugs or psychological intervention in past 6 months, and specified clinical/feasibility exclusions. This defines enrolled-population boundaries; no enrolled count is reported. | [DOC-004 p. 3](../../../../joi190007supp3_prod.pdf#page=3) |
| R-N-010 | Supplements/placebos: two pills/day for one year. Active supplement 1 contains 1412 mg EPA+DHA at 3:1; active supplement 2 contains selenium 30 micrograms, folic acid 400 micrograms, vitamin D3 20 micrograms, and calcium 100 mg. Placebo 1 composition includes 57% linoleic and 30% oleic acid. | [DOC-004 p. 4](../../../../joi190007supp3_prod.pdf#page=4) |
| R-N-011 | Independent duplicate testing included 6 supplements and 5 placebos. Reported average active values: selenium 30 micrograms (SD 0.4), EPA 67.9 g/100g FAME (SD 0.85), DHA 14.6 g/100g FAME (SD 1.55); placebo selenium 0.03 micrograms/kg (SD 0.03) and EPA/DHA <0.1 gram. These are product-assay descriptors, not trial outcome results. | [DOC-004 p. 5](../../../../joi190007supp3_prod.pdf#page=5) |
| R-N-012 | F-BA dose: up to 21 sessions—up to 15 individual 30-minute sessions (single or double 1-hour meetings) followed by 6 group sessions of up to 10 people for about 1 hour. Dietary targets include 300-400 g/day vegetables; 2-3 fruit pieces/day; fish 3 times/week; meat reduced to 300 g/week; pulses/legumes 3 times/week; and 3 low-fat-dairy servings/day. | [DOC-004 p. 6](../../../../joi190007supp3_prod.pdf#page=6) |
| R-N-013 | MCID/interpretation definitions (described for treatment rather than prevention): PHQ-9 MCID 2-3 points by 1-SEM or 4-6 by 2-SEM; PHQ-9 cutoffs 5/10/15/20 for mild/moderate/moderate-severe/severe. IDS-SR30 has no MCID reported and cutoffs 14/26/39/49 for mild/moderate/severe/very severe. GAD-7 MCID 2-3 (1-SEM) or 4-6 (2-SEM), and cutoffs 5/10/15 for mild/moderate/severe. EQ-5D-5L MCID 0.074. | [DOC-004 p. 7](../../../../joi190007supp3_prod.pdf#page=7) |
| R-N-014 | F-BA compliance threshold is prespecified as 8 of 21 sessions. Appendix rationale reports that therapy effects typically occur in first 2-8 sessions, cites average 6 sessions, notes up to 20 COBRA sessions with >=8 as threshold, and explains that 8/21 is at least half of the 15 individual sessions. These are rationale quantities, not this trial's outcomes. | [DOC-004 pp. 8-9](../../../../joi190007supp3_prod.pdf#page=8) |
| R-N-015 | Baseline measures include sex, age, education, smoking, alcohol (AUDIT), physical activity (SQUASH), BMI kg/m2, and prior-month supplement use. Adherence was a priori >=8/21 F-BA sessions and >=70% supplements over 12 months; supplement adherence calculation is supplements taken / total received from provided/returned jar weights. Self-report was collected at 3/6/9/12 months; agreement kappas are 0.73 and 0.70 for supplements 1 and 2. | [DOC-004 p. 12](../../../../joi190007supp3_prod.pdf#page=12) |
| R-N-016 | Further measures: body-weight change (kg, absolute and relative), diet-quality score, and serum nutrient change are 12-month minus baseline. A 250-item GA2LEN FFQ is used. Eleven food-group intakes sum to a MooDFOOD score range 0 (poor adherence) to 77 (optimal). At baseline and 12 months, nonfasting serum samples were in a subset n=211-331 (22-32%), stored at -80 degrees C, for selenium, folic acid, and 25-hydroxyvitamin D. | [DOC-004 p. 12](../../../../joi190007supp3_prod.pdf#page=12) |
| R-N-017 | Hospitalizations are registered from all follow-up interviews or dropout reason; deaths from dropout reason. At 12 months, participants report whether they believed allocation was supplements, placebo, or unknown. No resulting frequencies are reported. | [DOC-004 p. 13](../../../../joi190007supp3_prod.pdf#page=13) |
| R-S-008 | CACE is defined as intervention effect among those receiving intervention as intended while retaining randomization through instrumental-variable use. Assumptions: two latent classes (compliers/noncompliers); randomization yields similar complier proportion in arms, so control-arm latent compliance is estimated from treatment arm; exclusion restriction; and a structural-equation-model analysis retaining the full sample. The estimate is described as original intervention-effect estimate divided by treatment-arm complier proportion. | [DOC-004 pp. 14-15](../../../../joi190007supp3_prod.pdf#page=14) |

### Administrative/no-applicable pages

| Unit | Mapping result | Exact location |
|---|---|---|
| DOC-004 pp. 10-11 | Reference-list continuation for the F-BA compliance-cutoff rationale. No trial result table, figure, participant count, effect estimate, or additional prespecified analysis relationship on these assigned pages. | [DOC-004 p. 10](../../../../joi190007supp3_prod.pdf#page=10), [p. 11](../../../../joi190007supp3_prod.pdf#page=11) |
| DOC-004 pp. 24-25 | Reference-list entries only. They provide citations for appendices but contain no result-relevant numerical/statistical relationship from this study. | [DOC-004 p. 24](../../../../joi190007supp3_prod.pdf#page=24), [p. 25](../../../../joi190007supp3_prod.pdf#page=25) |
| DOC-004 assigned scope overall | No trial results table or figure is printed on the assigned pages. All quantitative items above are eligibility, intervention/product, scale, adherence, planned-analysis, or measurement definitions. | [DOC-004 p. 3](../../../../joi190007supp3_prod.pdf#page=3) |

## DOC-005 — data-sharing statement

Source: [joi190007supp4_prod.pdf — PDF p. 1](../../../../joi190007supp4_prod.pdf#page=1).

| Unit | Mapping result | Exact location |
|---|---|---|
| DOC-005 p. 1 | Administrative data-sharing statement. Data are marked available after approval of an analysis plan by the publication committee; access is restricted to approved researchers and specified purposes. It names no analytic result, sample, outcome value, table, figure, statistical model, or quantitative relationship applicable to this review. | [DOC-005 p. 1](../../../../joi190007supp4_prod.pdf#page=1) |

## Scope accounting

- Assigned source pages read directly: 5 (DOC-003) + 15 (DOC-004) + 1 (DOC-005) = **21 PDF pages**.
- Mapper-local numeric/reporting relationships: **17** (`R-N-001` through `R-N-017`).
- Mapper-local statistical relationships: **8** (`R-S-001` through `R-S-008`).
- Results tables/figures in assigned scope: **0**. Actual trial result values are not printed in these source units.
- No candidate determination was made in this mapping artifact.
