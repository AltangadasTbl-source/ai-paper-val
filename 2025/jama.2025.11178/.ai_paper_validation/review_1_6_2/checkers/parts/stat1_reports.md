# Statistical pass 1 — supplementary REPORT shard

Fresh agent: /root/stat1_reports; gpt-6.1-sol; high effort; FRESH_SPAWN. The coordinator records the actual spawn runtime ID in agent_execution_manifest.md.

Exact scope: DOC-005 PDF pages 1–16 and 19, eTables 1–10 and eFigures 1–2; inferential and statistical-method content of DOC-004 PDF pages 1–7 and DOC-006 worksheet eTable 3, A1:J115. DOC-005 eTable 11, PDF pages 17–18, belongs to the separate raw-score shard; MAIN inference rows and PLAN-internal statistical relationships belong to separate peers. All compared locations below are REPORT by content.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Scientific input was limited to exact supplied sources and current fresh source maps. No prior 1.6.2 conclusions, candidate sets or screening records were read. Fresh source renders confirmed every cited PDF row. Direct permitted Office extraction confirmed workbook cells. Source-unit scientific gaps: none. No web used.

Pass-1 coverage: **63 stable relationships, S201–S263**, each explicitly PASS_1_COMPLETE in statistics/parts/reports_inventory.md. **6 findings; 9 excluded-observation rows.** Repeated instances of each pattern are consolidated. Proposed domains and relationship types pre-fill human review; no adjudication is assigned.

## Findings

### F-ST1-201

**Title:** Linear-imputation 95% intervals exclude zero while the corresponding P values exceed .05.

**Relationships:** S208; related method records S204, S205. Proposed primary relationship type: S_W; all relationships: S_W.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.8, eTable 3](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), seven rows listed below; REPORT [DOC-005 PDF pp.4–5, imputation method](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5). REPORT [DOC-001 PDF p.4, Statistical Analysis](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) supplies the shared two-sided α=.05 test definition and corroborates, rather than conflicts with, the supplement.

**Printed values:**

| eTable 3 row | Estimate | Printed 95% CI | P value |
|---|---:|---|---:|
| Pattern: 2 observed follow-ups | −0.28 | −0.47, −0.08 | .150 |
| Pattern: 1 observed follow-up | −0.20 | −0.36, −0.03 | .226 |
| Pattern 2, painTRAINER interaction | −0.30 | −0.58, −0.02 | .280 |
| Pattern 2, Health Coach interaction | −0.47 | −0.74, −0.19 | .090 |
| Site 3 | 0.19 | 0.08, 0.29 | .069 |
| Site 4 | 0.15 | 0.05, 0.24 | .124 |
| Second Education: AA degree (reference High school or less) row | 0.16 | 0.07, 0.25 | .077 |

**Rule and calculation:** For each printed 95% interval, 0 is outside its limits, while the corresponding printed P is greater than .05. These are individual coefficient rows of the reported linear GEE imputation model, with working independence and robust standard errors accounting for coach and participant clustering. For example, −.47 < −.28 < −.08 < 0 but P=.150; 0 < .08 < .19 < .29 but P=.069. All seven estimates are contained in their intervals and their endpoints are ordered. The conflict concerns interval-versus-test significance. The display-precision rule is inapplicable to Route A category 1; no relative-discrepancy calculation is used to screen this pattern out.

**Focus area:** B, estimate and test logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route A, category 1.
**Affected result or extracted value:** Significance and uncertainty of the missingness-pattern, pattern-by-arm, site and education coefficients used in the primary-outcome imputation model.
**Why context does not resolve it:** Each row contains the conflicting interval and P value under a 95% CI column and the common .05 test level. This is an always-register interval-versus-P pattern. The immediate table and accompanying method do not state that the columns represent different analyses.

**Alternatives and missing definitions:** P values and intervals might use different variance estimates, coefficient tests or confidence constructions, or one printed column might summarize a different analysis. The source does not supply the coefficient-test family, degrees of freedom or numeric standard errors needed to reconstruct the exact P values. Such an alternative must be stated by the human reviewer; it does not remove the directly printed null-significance conflict. No normal-Wald approximation is used as the reproduction criterion.

**Exact human question:** Which analysis, variance estimate and confidence-interval construction produced the seven listed eTable 3 intervals and P values, and which interval and P value should be extracted for each coefficient?

### F-ST1-202

**Title:** Significant coefficient P values accompany 95% intervals printed with a null-valued endpoint.

**Relationships:** S209 and S210. Proposed primary relationship type: S_W; all relationships: S_W.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.9, eTable 4, Age ≥65 and second AA education rows](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); REPORT [DOC-005 PDF p.10, eTable 5, PEG score row](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10). Shared significance definition: REPORT DOC-001 PDF p.4, all tests two-sided α=.05; this is corroborating context.

**Printed values:**

| Location and row | Effect | Printed 95% CI | P |
|---|---:|---|---:|
| eTable 4, Age ≥65 vs <65 | RR 1.15 | 1, 1.33 | .046 |
| eTable 4, second Education: AA degree vs HS or less | RR 1.16 | 1, 1.33 | .046 |
| eTable 5, PEG score | OR 0.96 | 0.92, 1.00 | .037 |

**Rule and calculation:** The ratio null is 1. The printed lower endpoint equals 1 in both eTable 4 rows, and the printed upper endpoint equals 1.00 in the eTable 5 row. Thus each displayed 95% interval includes the null, while its corresponding P is below .05. Point containment and interval ordering hold. The scope explicitly exempts interval-versus-P comparisons from display-precision screening; these boundary cases are therefore registered even though rounding can plausibly explain an exact endpoint close to 1.

**Focus area:** B, estimate and test logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route A, category 1.
**Affected result or extracted value:** The printed 95% intervals and significance of age and education effects in the primary estimation model and PEG in the response-weight model.
**Why context does not resolve it:** The displayed interval includes its null and the P value is significant at the stated level. Route A category 1 requires registration; presumed unrounded endpoints cannot substitute for supplied printed values.

**Alternatives and missing definitions:** A true lower endpoint slightly above 1, or upper endpoint slightly below 1, may have rounded to the printed null; different interval and test constructions are another possibility. The source does not provide unrounded endpoint values or separate coefficient-test definitions. These are alternatives for human adjudication.

**Exact human question:** What are the unrounded 95% endpoints and the associated test definitions for these three rows, and how should their printed intervals and P values be represented for extraction?

### F-ST1-203

**Title:** The stated final weight-model covariates differ from the fitted weight-model display.

**Relationships:** S203, S207, S210, S256 and S262. Proposed primary relationship type: S_W; all relationships: S_W. DOC-006 only corroborates selection-test context and does not create an S_C conflict.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.7, eTable 2, final additional variables for the nonresponse weight model](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); REPORT [DOC-005 PDF p.10, eTable 5, complete logistic weight-model coefficient display](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); REPORT [DOC-005 PDF pp.4–5, selection and weighting methods](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5).

**Printed values and statements:** eTable 2 lists additional weighting variables as PEG score, PHQ-8, GAD-7, any negative social determinant of health, and education (any college vs HS degree or less). Its base-variable list does not include employment. eTable 5 contains the first four of these variables, has no education coefficient, and instead reports Not employed OR1.49 (95% CI1.11–2.00), P=.008. The narrative describes adding the selected covariates to the final logistic model used to create weights for the primary analysis.

**Rule and calculation:** Compare membership of the explicitly stated final additional-covariate set with the full fitted-model coefficient set. Stated education has no displayed coefficient; displayed employment is absent from the final weighting list and the base list. This is a logical model-attribution comparison, with no rounding calculation applicable. Changing the treatment reference group in a logistic fit does not account for exchanging these covariates.

**Focus area:** C, statistical method logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route B.
**Affected result or extracted value:** The nonresponse weights used in the primary weighted MCID analysis and the reported employment OR in the weighting model.
**Why context does not resolve it:** Both displays identify the final weight model, but they specify different applied adjustment sets. The table does not disclose an omitted education coefficient, substitution or subsequent model revision. A reader cannot identify which covariate set generated the actual weights from these statements.

**Alternatives and missing definitions:** Education may have been used but omitted from the displayed model, the final list may refer to an earlier selection stage, or employment may have been added subsequently. The workbook shows employment significant in both selection families (H18<.001, I18=.0228), but that corroboration does not resolve the printed final-model discrepancy. No preference for including either predictor is proposed.

**Exact human question:** Did the logistic model generating the primary nonresponse weights include education, employment, both or another set, and which coefficient display and final-variable list describe that model?

### F-ST1-204

**Title:** Education coding and repeated coefficient labels leave the applied education adjustment unclear.

**Relationships:** S203, S208, S209 and S261. Proposed primary relationship type: S_W; all relationships: S_W. Workbook categories are corroboration only.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.7, eTable 2, additional imputation/estimation variables](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); REPORT [DOC-005 PDF p.8, eTable 3, all education coefficient rows](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); REPORT [DOC-005 PDF p.9, eTable 4, all education coefficient rows](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=9). REPORT DOC-006 eTable 3 A12:A16 provides distinct HS/associate/college/graduate categories as corroboration.

**Printed values and statements:** eTable 2 specifies education as “any college vs. HS degree or less.” eTable 3 prints three education coefficients: AA degree −.02 (−.11,.08), P=.866; a second AA degree .16 (.07,.25), P=.077; Graduate degree .39 (.29,.49), P<.001, all versus high school or less. eTable 4 likewise prints AA degree RR.97 (.82,1.16), P=.770; a second AA degree RR1.16 (1,1.33), P=.046; Graduate degree RR1.35 (1.13,1.61), P<.001.

**Rule and calculation:** A single binary any-college indicator is a different adjustment specification from three category-versus-reference coefficients. Further, two different coefficients have the same AA label and reference within each complete fitted model. The supplied category list makes a college label plausible for one row but does not state that mapping. This is a model-definition and numeric-result-attribution comparison; display precision does not resolve category assignment.

**Focus area:** C, statistical method logic; B, estimate attribution.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route B.
**Affected result or extracted value:** The education adjustment in the primary imputation and estimation models, and the coefficient/RR assigned to associate versus college education.
**Why context does not resolve it:** The immediate coefficient tables offer two different estimates for the same labeled category, while the selection table specifies a binary contrast. Guessing which row belongs to the college category does not establish the coding actually used or the coefficient a data extractor should assign.

**Alternatives and missing definitions:** The applied education covariate may have been a four-level factor with one repeated label, or the selected binary covariate may have been expanded for the reported fits. The source does not explicitly disclose a recoding or map the duplicate labels. This observation is consolidated across both models because it is one education-definition pattern, rather than a separate finding for each repeated label.

**Exact human question:** Was education coded as any-college versus HS-or-less or as a multilevel factor in each primary model, and which category corresponds to each of the two printed AA rows?

### F-ST1-205

**Title:** Restricted primary subset analyses list a smaller covariate set than the primary estimation model.

**Relationships:** S220 and S263. Proposed primary relationship type: S_W; all relationships: S_W.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.13, Protocol Change Subset Analyses](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=13); REPORT [DOC-005 PDF p.14, eTable 8, footnote b](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14); REPORT [DOC-005 PDF p.4, Adjustment](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); REPORT [DOC-005 PDF p.7, eTable 2, final imputation/estimation list](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7).

**Printed values and statements:** The subset narrative says eTable 8 shows “results of the primary analysis restricting to subsets of the randomized population.” The primary imputation/estimation selection list adds education and unemployment, and the fitted models display both. eTable 8 footnote b instead lists sex, age, site, rural/urban residence, more than one musculoskeletal condition, mental-health diagnosis and baseline pain severity, without education or employment.

**Rule and calculation:** The stated restricted-primary-analysis model attribution and the explicit subset adjustment list do not name the same adjustment set. This is a logical analysis-definition comparison; no numeric rounding test applies. It concerns the explicit covariates, rather than inferring the absence of imputation or weighting from silence.

**Focus area:** C, statistical method logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route B.
**Affected result or extracted value:** All eTable 8 adjusted percentages, RR and NNT estimates in the pre-enhancement, post-enhancement and reminder-letter subset analyses, including the 3-month primary-outcome subset estimates.
**Why context does not resolve it:** The narrative identifies a restricted version of the primary analysis, while the footnote describes a base-only adjustment. No explanation says that additional primary covariates were dropped, reselected or merely omitted from the footnote. The actual analysis producing these estimates is therefore not identifiable from the supplied description.

**Alternatives and missing definitions:** The primary model may have been refitted with only base covariates in subsets, additional predictors may have been reselected, or the footnote may abbreviate a fuller adjustment set. Any of these could be internally coherent if stated; the observation asks which was used and does not propose a preferred subset analysis.

**Exact human question:** Which covariates were included in each eTable 8 subset estimation model, and does “primary analysis restricting to subsets” mean the full primary adjustment set or the base-only set listed in footnote b?

### F-ST1-206

**Title:** Reminder-letter 6-month PT-versus-UC NNT does not reproduce from the printed adjusted percentages under the stated reciprocal method.

**Relationships:** S228; method S220. Proposed primary relationship type: S_W; all relationships: S_W. The numeric checker independently identified related MAIN occurrences; this shard registers its assigned occurrence for the inclusion screener to consolidate as appropriate.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.14, eTable 8, Reminder Letters Added, 6-month row, PT and UC adjusted percentages and PT-versus-UC NNT](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14); REPORT same page, footnote d defining NNT.

**Printed values:** PT35.6% (30.6,41.4); UC21.3% (17.5,26.1); PT-versus-UC NNT8 (5,14). Footnote d defines NNT as one over the difference in adjusted improvement percentages (using probability units).

**Rule and calculation:** NNT=100/(35.6−21.3)=100/14.3=6.99300699. Give each printed percentage its half-unit interval: PT[35.55,35.65], UC[21.25,21.35]. Their difference is[14.20,14.40] percentage points, so the recomputed NNT interval is[100/14.40,100/14.20]=[6.94444444,7.04225352]. The printed integer NNT8 has half-unit interval[7.5,8.5]. The gap is7.5−7.04225352=.45774648; relative discrepancy=.45774648/8=.05721831>.05. The same reciprocal check across all45 contrasts in eTables7–8 leaves the other44 within the display-precision threshold; the method reproduces the other rows under that rule. Ceiling the reciprocal of the printed percentage centers6.99300699 gives7, but the true unrounded reciprocal may lie as high as7.04225352, whose ceiling is8. Thus an unstated upward-integer convention remains an alternative for this row too; no ceiling rule is assumed for the half-unit reproduction comparison. Endpoint uncertainty of the NNT confidence interval is not recomputed because the risk-difference variance is absent.

**Focus area:** B, estimate and test logic; C, statistical method logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route A, category 4.
**Affected result or extracted value:** The PT-versus-UC adjusted NNT for pain-severity MCID at6 months among participants randomized after3/31/2022.
**Why context does not resolve it:** The specified reciprocal method reproduces the other rows within the scope threshold, but this printed8 remains separated by more than5% after input/output display precision. The printed result is an always-register reproducing-method discrepancy.

**Alternatives and missing definitions:** The NNT may have been calculated from another risk-difference estimand or model despite footnote d, or a different percentage pair may have been used. The printed row and footnote do not disclose another calculation. This card does not prescribe a replacement value.

**Exact human question:** What risk difference and calculation produced the printed NNT8 for the reminder-letter 6-month PT-versus-UC comparison, and is it the reciprocal of the same adjusted percentages printed in that row?

## Excluded observations

Only apparent issues decided against emission are listed; checks that reconcile remain in the S records.

| Location | Observation | Reason code |
|---|---|---|
| DOC-005 PDF p.7, eTable 1 completeness patterns; DOC-006 eTable 3 B3:E3 | Pattern counts 188+283+1568=2039 versus any-followup 2036; PT 644 vs 643 and HC 692 vs 690; implied visits 5458 vs 5449; workbook missing 1-or-2 is 468 versus 188+283=471. Half-unit pattern-total interval [2037.5,2040.5] versus [2035.5,2036.5] leaves gap 1/2036=.000491; visit totals [5455,5461] versus [5447.5,5450.5] leave gap 4.5/5449=.000826; the workbook comparison [470,472] versus [467.5,468.5] leaves gap 1.5/468=.003205. All are ≤.05; arm-total intervals overlap. The pattern is listed once. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-005 PDF pp.11/14, eTables7–8, other NNT point estimates | All44 reciprocal NNT comparisons other than F-ST1-206 either overlap under half-unit input/output intervals or have remaining relative gaps≤.05. Largest excluded gap: reminder-letter6M HC/UC NNT6 versus reciprocal[5.154639,5.208333], printed[5.5,6.5], relative.048611. Other apparent NNT differences are one consolidated display-precision pattern. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-005 PDF p.8, eTable3, quantitative CI-width/P diagnostics beyond the seven null conflicts | A normal-Wald diagnostic SE=(upper−lower)/(2×1.96), then two-sided P from estimate/SE, yields differences for additional rows (for example Time6M estimate.13,CI.07–.19 gives diagnostic z4.247 and Pabout.000022 versus.025). Coefficient-test family, degrees of freedom and interval construction are not stated; a specific exact numerical test cannot be established. The seven direct CI-null/P conflicts remain emitted separately as F-ST1-201. | CONDITIONAL_OR_UNREPORTED |
| DOC-005 PDF p.8, eTable3, arm coefficients versus improvement direction | Positive imputation coefficients cannot alone be interpreted as worse clinical response without a supplied sign convention for the imputation change, the missingness-pattern conditioning and the complete covariate context. No direct printed direction statement for these conditional coefficients conflicts. | CONDITIONAL_OR_UNREPORTED |
| DOC-005 PDF pp.5/9/10, weight normalization description and sums | “Scaled to the study sample size” could be read as2331 rather than2036, but eTable6 explicitly sums to2036, eTable4 to3×2036=6108, and imputation is among any-followup participants. These immediate displays identify the analysis sample for the scaling statement. | CONTEXT_RESOLVES |
| DOC-005 PDF p.7, eTable2 all-model list versus pp.4/8/9 | Baseline pain severity is omitted from eTable2's base-variable list, but the adjustment narrative and both complete primary model displays explicitly include it. Its applied inclusion is immediately identifiable and the omission changes no extractable coefficient assignment. | CONTEXT_RESOLVES |
| DOC-005 PDF p.15, eTable9 title | Title says “adjusted relative risk,” but the page explicitly says no adjustment, weighting or imputation, the coefficient heading says Relative Risk, and footnote b says “without adjustment.” The intended unadjusted analysis is immediately identified; point estimates also agree with the unadjusted proportions. | TERMINOLOGY_OR_WORDING |
| DOC-005 PDF p.16, eTable10 descriptive median heading versus mean-effect footnote | Group medians/IQRs do not need to reproduce between-group mean differences. The effect columns explicitly name means and95%CIs, while the descriptive columns name medians/IQRs; this distinction identifies the quantities a reader extracts. No direct numeric contradiction is established. | CONTEXT_RESOLVES |
| DOC-005 PDF p.3, eFigure1 Virtual Coach/VC labels | Virtual Coach names the Health Coach intervention in the surrounding three-arm trial context; no numeric result is attributed to a different intervention. | TERMINOLOGY_OR_WORDING |

## Checks and limitations

All coefficient, treatment, sensitivity and unadjusted-result tuples in the assigned scope were checked for point containment, endpoint order and direction. All individual CI/P null-level conflicts are registered above. Omnibus P values were matched to their three-arm Wald tests; they were not compared as individual pairwise P values. Printed NNT positive/negative limits were interpreted as the explicitly defined infinity-containing branches, not reversed finite intervals.

The source supplies two-sided α=.05 and95% intervals. It does not supply numeric coefficient standard errors, numeric test statistics, coefficient-test degrees of freedom or full covariance matrices. Exact P/SE/statistic compatibility beyond direct null-level conflicts is consequently not asserted; diagnostic approximations are labeled. The assigned supplement has no power/sample-size calculation, noninferiority/equivalence margin or statistical interim/stopping boundary. Fidelity thresholds in DOC-004 concern treatment delivery, not statistical trial stopping.

No scientific source-coverage gap remains in this assigned scope. Unlabeled histogram bins provide visual direction only, not exact counts. Workbook conversion to PDF is unavailable, but direct cell extraction supplies truthful worksheet/cell locations. Primary durable outputs: statistics/parts/reports_inventory.md and checkers/parts/stat1_reports.md. Fresh renders and Office extraction, with CPU PyMuPDF1.26.4 and the permitted Office helper, are under preprocessing/stat1_reports.

