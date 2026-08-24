# Statistical consistency pass 1

## Scope, evidence, and decision rules

This fresh pass independently reviewed every canonical statistical relationship, `S001` through `S067`, against the new direct-source native and coordinate-layout assets for DOC-001, DOC-002, and DOC-003. It used the canonical inventory, its two fresh provisional mapping parts, the fresh main/support quantitative extractions, and the numeric relationship inventory only to locate matching denominators and definitions. No legacy audit derivative or web source was used.

Checks applied where relevant were: point-estimate containment in its displayed interval; interval endpoint ordering; estimate/interval and label/direction agreement; agreement of the matched repeated result after population, time, contrast, model, and precision were matched; and P-value/interval compatibility only where the supplied article/table establishes an adjusted 95% CI and a separately printed P value for the same displayed contrast. The main article states that tests were two-sided and that comparative cumulative incidences/absolute differences with 95% CIs were adjusted for the listed patient and hospital characteristics (DOC-001 PDF p. 4); the Table 2 and Table 3 footnotes identify that same adjustment set. The supplied material does not define a common variance estimator, degrees of freedom, or an exact CI-to-P construction, so no exact reconstructed P value was used as a decision rule. Any diagnostic approximation below is expressly non-authoritative.

`NO_QUALIFYING_CONTRADICTION` means the displayed values were compatible at the available precision, or any apparent difference was explained by a supplied distinct population, time point, denominator, outcome, or model. `DEFINITION_LIMITATION_RECORDED` means the complete display was checked but a requested exact compatibility calculation is not source-defined. No mapped relationship contains `P = 0`, `p = 0.000`, or equivalent; consequently no `DISPLAY_ZERO_NOT_CANDIDATE` record was required.

## Per-relationship results

| Stable ID | PASS_1 status | Evidence and checks completed | Result |
|---|---|---|---|
| S001 | PASS_1_COMPLETE | DOC-001 p. 4; DOC-002 p. 17. Planned 4,800/40 clusters, 80% power, 5% significance, ICC .02, and 5% target improvement matched across the two supplied locations. Exact sample-size reconstruction is not defined. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S002 | PASS_1_COMPLETE | DOC-001 pp. 1, 5, 7. Composite 88.2 vs 84.8, difference 3.54 (CI .68-6.40), absolute-difference P=.02, and ORPA 1.39 (1.12-1.72), P=.003 agree in direction, interval containment, and matched repeats. | NO_QUALIFYING_CONTRADICTION |
| S003 | PASS_1_COMPLETE | DOC-001 pp. 1, 5, 7. All-or-none 53.8 vs 47.8, difference 6.69 (-.41-13.79), P=.06, ORPA 1.19 (.85-1.67), P=.31 are directionally and interval/P compatible at printed precision. | NO_QUALIFYING_CONTRADICTION |
| S004 | PASS_1_COMPLETE | DOC-001 pp. 1, 5, 8. Three-month vascular events 93/2400 vs 127/2400, difference -2.03 (-3.51 to -.55), P=.007; HR .65 (.49-.86), P=.002. Repeated values match and both effect directions favor intervention. | NO_QUALIFYING_CONTRADICTION |
| S005 | PASS_1_COMPLETE | DOC-001 pp. 1, 5, 8. Six-month vascular events 150/2400 vs 186/2400, difference -2.18 (-4.0 to -.35), P=.02; HR .72 (.57-.90), P=.004. | NO_QUALIFYING_CONTRADICTION |
| S006 | PASS_1_COMPLETE | DOC-001 pp. 1, 5, 8 and Figure 2A. Twelve-month vascular events 218/2400 vs 282/2400, difference -3.13 (-5.28 to -.97), P=.005; HR .72 (.60-.87), P<.001. Narrative, table, and figure agree. | NO_QUALIFYING_CONTRADICTION |
| S007 | PASS_1_COMPLETE | DOC-001 p. 4; Table 2 p. 7; Table 3 p. 8; DOC-002 pp. 18-19. Supplied GEE/logistic/Cox/binary-link model labels, 95% CI convention, adjustment set, two-sided threshold, and exploratory-secondary qualification are consistent. No common variance/df rule is supplied for exact P reconstruction. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S008 | PASS_1_COMPLETE | DOC-001 pp. 5, 8. Three-month disability 418/2180 vs 443/2105, difference -3.72 (-6.7 to -.79), P=.01; OR .76 (.63-.91), P=.002. Direction and interval/P signs agree. | NO_QUALIFYING_CONTRADICTION |
| S009 | PASS_1_COMPLETE | DOC-001 pp. 5, 8. Six-month disability 326/2058 vs 360/2009, difference -3.86 (-6.60 to -1.13), P=.006; OR .74 (.61-.89), P=.002. | NO_QUALIFYING_CONTRADICTION |
| S010 | PASS_1_COMPLETE | DOC-001 pp. 5, 8. Twelve-month disability 236/1852 vs 264/1798, difference -3.13 (-5.80 to -.46), P=.02; OR .74 (.59-.93), P=.01. | NO_QUALIFYING_CONTRADICTION |
| S011 | PASS_1_COMPLETE | DOC-001 p. 5; DOC-003 p. 8. Sensitivity composite 85.3 vs 80.9/80.91, difference 4.20 (1.77-6.63), absolute-difference P<.001, ORPA 1.36 (1.11-1.67), ORPA P=.003. Main text reports the latter P after the ORPA; eTable separates both P columns. | NO_QUALIFYING_CONTRADICTION |
| S012 | PASS_1_COMPLETE | DOC-001 p. 7. rtPA <=3 h: 46/212 vs 23/204, 7.3 (-5.3 to 19.9), P=.26; ORPA 3.18 (.94-10.78), P=.06. Point, interval, direction, and labels agree. | NO_QUALIFYING_CONTRADICTION |
| S013 | PASS_1_COMPLETE | DOC-001 p. 7. Early antithrombotics: 2307/2353 vs 2253/2330, 1.5 (-.3 to 3.2), P=.10; ORPA 1.93 (.94-3.95), P=.07. | NO_QUALIFYING_CONTRADICTION |
| S014 | PASS_1_COMPLETE | DOC-001 p. 7. Dysphagia: 2255/2328 vs 2040/2139, 1.6 (-2.1 to 5.3), P=.41; ORPA 2.49 (.84-7.40), P=.10. | NO_QUALIFYING_CONTRADICTION |
| S015 | PASS_1_COMPLETE | DOC-001 p. 7. DVT prophylaxis: 178/645 vs 66/592, 15.6 (3.3-27.9), P=.01; ORPA 2.42 (1.02-5.72), P=.04. Positive-difference and ORPA directions agree. | NO_QUALIFYING_CONTRADICTION |
| S016 | PASS_1_COMPLETE | DOC-001 p. 7. Discharge antithrombotics: 2272/2324 vs 2141/2305, 4.2 (-.6 to 8.9), P=.09; ORPA 2.29 (.86-6.11), P=.10. | NO_QUALIFYING_CONTRADICTION |
| S017 | PASS_1_COMPLETE | DOC-001 p. 7. AF anticoagulation: 63/155 vs 39/137, 12.9 (-5.8 to 31.6), P=.18; ORPA 1.80 (.68-4.75), P=.23. | NO_QUALIFYING_CONTRADICTION |
| S018 | PASS_1_COMPLETE | DOC-001 p. 7. LDL lowering: 1415/1481 vs 1439/1547, 2.4 (-1.6 to 6.4), P=.25; ORPA 1.35 (.67-2.73), P=.40. | NO_QUALIFYING_CONTRADICTION |
| S019 | PASS_1_COMPLETE | DOC-001 p. 7. Antihypertensive: 1510/1838 vs 1372/1771, 6.1 (-.6 to 12.7), P=.07; ORPA 1.44 (.94-2.20), P=.10. | NO_QUALIFYING_CONTRADICTION |
| S020 | PASS_1_COMPLETE | DOC-001 p. 7. Antidiabetic: 653/728 vs 557/663, 5.0 (.8-9.3), P=.02; ORPA 1.57 (1.08-2.28), P=.02. | NO_QUALIFYING_CONTRADICTION |
| S021 | PASS_1_COMPLETE | DOC-001 p. 8 Figure 2A and Table 3. HR .72 (.60-.87), P<.001 matches the 12-month vascular-event outcome and stated log-rank context. Figure uses the same event/time definition. | NO_QUALIFYING_CONTRADICTION |
| S022 | PASS_1_COMPLETE | DOC-001 p. 8 Figure 2B and Table 3. Death HR .86 (.68-1.09), P=.21 is compatible with an interval containing 1 and matched 12-month death result. | NO_QUALIFYING_CONTRADICTION |
| S023 | PASS_1_COMPLETE | DOC-001 p. 8 Table 3. In-hospital death 11/2400 vs 23/2400; adjusted absolute difference -.7% (95% CI -1.1 to .2), reported P=.009; HR .96 (.90-1.02), P=.14. The absolute-difference CI includes 0 whereas the P value in that CI column is below .05. | SP1-001 |
| S024 | PASS_1_COMPLETE | DOC-001 p. 8. Three-month death 66/2400 vs 76/2400, difference -1.0 (-2.1 to .1), P=.08; HR .81 (.57-1.15), P=.23. | NO_QUALIFYING_CONTRADICTION |
| S025 | PASS_1_COMPLETE | DOC-001 p. 8. Six-month death 103/2400 vs 101/2400, difference -.5 (-1.7 to .6), P=.38; HR .97 (.73-1.29), P=.81. Distinct displayed crude counts do not override the adjusted effect columns. | NO_QUALIFYING_CONTRADICTION |
| S026 | PASS_1_COMPLETE | DOC-001 p. 8. Twelve-month death 139/2400 vs 160/2400, difference -1.5 (-3.0 to -.0), P=.05; HR .86 (.68-1.09), P=.21. The rounded `-.0` endpoint and `.05` are boundary-compatible at displayed precision. | NO_QUALIFYING_CONTRADICTION |
| S027 | PASS_1_COMPLETE | DOC-001 p. 5. Symptomatic ICH 1/46 (2.2%) vs 2/23 (8.7%), P=.26. Direction agrees with counts; no named test/CI/variance rule permits further mechanical compatibility testing. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S028 | PASS_1_COMPLETE | DOC-002 p. 17. Protocol sample-size parameters repeat S001 (80% power, 5% significance, ICC .02, 5% target). | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S029 | PASS_1_COMPLETE | DOC-002 p. 18. Planned descriptive summaries specify proportion, mean (SD), and median (IQR) by distribution. No printed result conflict is present. | NO_QUALIFYING_CONTRADICTION |
| S030 | PASS_1_COMPLETE | DOC-002 p. 18. Planned chi-square, Student t, and Mann-Whitney U tests are appropriately scoped to univariate categorical/continuous comparisons. No mapped P is asserted to be a uniquely reconstructable application of one of them. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S031 | PASS_1_COMPLETE | DOC-002 pp. 18-19. GEE and population-average OR/mean-difference, each with 95% CI, match the main article's composite/performance-measure modeling description. | NO_QUALIFYING_CONTRADICTION |
| S032 | PASS_1_COMPLETE | DOC-002 pp. 19-20. Kaplan-Meier and proportional-hazards Cox plan for events/mortality at the stated time points matches the article outcome model labels. | NO_QUALIFYING_CONTRADICTION |
| S033 | PASS_1_COMPLETE | DOC-003 p. 2. Baseline composite has no numerical P but explicitly says no statistically significant cluster-group difference; 80.2 vs 79.5 is a pre-randomization, not trial-outcome, comparison. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S034 | PASS_1_COMPLETE | DOC-003 p. 5 eTable 2. Age P=.81 accompanies matched 65 (56-74) versus 64 (56-74) groups. Exact test assignment is not printed in this table. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S035 | PASS_1_COMPLETE | DOC-003 p. 5 eTable 2. Male 2497/3949 vs 546/851, P=.61; direction and denominators are coherent. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S036 | PASS_1_COMPLETE | DOC-003 p. 5 eTable 2. Ischemic stroke 1137/3949 vs 251/851, P=.68. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S037 | PASS_1_COMPLETE | DOC-003 p. 5 eTable 2. Diabetes 890/3949 vs 196/851, P=.75. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S038 | PASS_1_COMPLETE | DOC-003 p. 5 eTable 2. Hypertension 2552/3949 vs 538/851, P=.44. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S039 | PASS_1_COMPLETE | DOC-003 p. 5 eTable 2. Dyslipidemia 285/3949 vs 62/851, P=.94. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S040 | PASS_1_COMPLETE | DOC-003 p. 5 eTable 2. CAD/previous MI 512/3949 vs 97/851, P=.21. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S041 | PASS_1_COMPLETE | DOC-003 p. 5 eTable 2. Atrial fibrillation 200/3949 vs 45/851, P=.79. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S042 | PASS_1_COMPLETE | DOC-003 p. 5 eTable 2. Ever smoking 1736/3949 vs 380/851, P=.71. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S043 | PASS_1_COMPLETE | DOC-003 p. 5 eTable 2. Admission NIHSS 3 (2-6) vs 3 (2-6), P=.99; NIHSS scale is supplied as 0-42. | NO_QUALIFYING_CONTRADICTION; DEFINITION_LIMITATION_RECORDED |
| S044 | PASS_1_COMPLETE | DOC-003 p. 6. Three-month ischemic stroke: -0.57 (-1.91 to .76), P=.40; HR .89 (.59-1.36), P=.59. Both intervals contain null and directions match event counts 44 vs 55. | NO_QUALIFYING_CONTRADICTION |
| S045 | PASS_1_COMPLETE | DOC-003 p. 6. Three-month hemorrhagic stroke: -.35 (-.92 to .22), P=.23; HR .85 (.40-1.83), P=.68. | NO_QUALIFYING_CONTRADICTION |
| S046 | PASS_1_COMPLETE | DOC-003 p. 6. Three-month MI: -.10 (-.36 to .17), P=.48; HR .58 (.13-2.67), P=.48. | NO_QUALIFYING_CONTRADICTION |
| S047 | PASS_1_COMPLETE | DOC-003 p. 6. Three-month vascular death: -1.43 (-2.33 to -.54), P=.001; HR .62 (.42-.92), P=.02. | NO_QUALIFYING_CONTRADICTION |
| S048 | PASS_1_COMPLETE | DOC-003 p. 6. Six-month ischemic stroke: -1.40 (-2.82 to -.02), P=.05; HR .72 (.53-.99), P=.04. Both are rounded boundary displays compatible with their directions. | NO_QUALIFYING_CONTRADICTION |
| S049 | PASS_1_COMPLETE | DOC-003 p. 6. Six-month hemorrhagic stroke: -.25 (-.80 to .30), P=.38; HR .92 (.46-1.82), P=.80. | NO_QUALIFYING_CONTRADICTION |
| S050 | PASS_1_COMPLETE | DOC-003 p. 6. Six-month MI: -.03 (-.35 to .29), P=.86; HR .78 (.27-2.24), P=.64. Equal event counts do not require adjusted HR=1 under the supplied Cox model. | NO_QUALIFYING_CONTRADICTION |
| S051 | PASS_1_COMPLETE | DOC-003 p. 6. Six-month vascular death: -1.06 (-2.08 to -.04), P=.04; HR .78 (.56-1.10), P=.16. Absolute difference and HR are distinct labeled measures. | NO_QUALIFYING_CONTRADICTION |
| S052 | PASS_1_COMPLETE | DOC-003 p. 6. Twelve-month ischemic stroke: -1.84 (-3.45 to -.23), P=.03; HR .73 (.57-.93), P=.01. | NO_QUALIFYING_CONTRADICTION |
| S053 | PASS_1_COMPLETE | DOC-003 p. 6. Twelve-month hemorrhagic stroke: -.08 (-.71 to .55), P=.80; HR 1.02 (.55-1.88), P=.96. | NO_QUALIFYING_CONTRADICTION |
| S054 | PASS_1_COMPLETE | DOC-003 p. 6. Twelve-month MI: -.13 (-.46 to .21), P=.45; HR .71 (.30-1.67), P=.43. | NO_QUALIFYING_CONTRADICTION |
| S055 | PASS_1_COMPLETE | DOC-003 p. 6. Twelve-month vascular death: -1.94 (-3.26 to -.62), P=.004; HR .71 (.54-.94), P=.02. | NO_QUALIFYING_CONTRADICTION |
| S056 | PASS_1_COMPLETE | DOC-003 pp. 6-7. eTable 3 explicitly says a patient may have different new vascular events; thus component-event sums need not equal the main-table number of patients with any new vascular event. The adjustment footnote matches the stated covariate set. | NO_QUALIFYING_CONTRADICTION |
| S057 | PASS_1_COMPLETE | DOC-003 p. 8. Sensitivity composite: mean difference 4.20 (1.77-6.63), P<.001; ORPA 1.36 (1.11-1.67), P=.003. Main p. 5 and eTable agree after matching P to its respective column. | NO_QUALIFYING_CONTRADICTION |
| S058 | PASS_1_COMPLETE | DOC-003 p. 8. Sensitivity rtPA <2 h: 46/254 vs 23/238, 5.81 (-4.57 to 16.19), P=.27; ORPA 2.60 (.76-8.87), P=.13. This is overall-population sensitivity analysis, distinct from S012 eligible-patient denominators. | NO_QUALIFYING_CONTRADICTION |
| S059 | PASS_1_COMPLETE | DOC-003 p. 8. Sensitivity early antithrombotics: 2.68 (.48-4.87), P=.02; ORPA 1.73 (1.05-2.87), P=.03. Overall-population denominators distinguish it from S013. | NO_QUALIFYING_CONTRADICTION |
| S060 | PASS_1_COMPLETE | DOC-003 p. 8. Sensitivity dysphagia: 1.72 (-1.95 to 5.40), P=.36; ORPA 2.37 (.69-8.18), P=.17. Denominators/model distinguish it from S014. | NO_QUALIFYING_CONTRADICTION |
| S061 | PASS_1_COMPLETE | DOC-003 p. 8. Sensitivity DVT: 14.79 (3.16-26.42), P=.01; ORPA 2.09 (.95-4.62), P=.07. Denominators/model distinguish it from S015. | NO_QUALIFYING_CONTRADICTION |
| S062 | PASS_1_COMPLETE | DOC-003 p. 8. Sensitivity discharge antithrombotics: 5.32 (.44-10.20), P=.03; ORPA 1.89 (.99-3.64), P=.05. Denominators/model distinguish it from S016. | NO_QUALIFYING_CONTRADICTION |
| S063 | PASS_1_COMPLETE | DOC-003 p. 8. Sensitivity AF anticoagulation: 12.90 (-3.51 to 29.3), P=.12; ORPA 1.78 (.61-5.14), P=.29. | NO_QUALIFYING_CONTRADICTION |
| S064 | PASS_1_COMPLETE | DOC-003 p. 8. Sensitivity lipid lowering: 2.46 (-2.03 to 6.95), P=.28; ORPA 1.17 (.61-2.24), P=.63. | NO_QUALIFYING_CONTRADICTION |
| S065 | PASS_1_COMPLETE | DOC-003 p. 8. Sensitivity antihypertensive: 6.32 (-.58 to 13.21), P=.07; ORPA 1.47 (.97-2.23), P=.07. | NO_QUALIFYING_CONTRADICTION |
| S066 | PASS_1_COMPLETE | DOC-003 p. 8. Sensitivity antidiabetic: 6.16 (1.70-10.62), P=.007; ORPA 1.59 (1.11-2.23), P=.01. | NO_QUALIFYING_CONTRADICTION |
| S067 | PASS_1_COMPLETE | DOC-003 p. 9. eTable 4 defines the adjustment covariates and ORPA; all sensitivity effects in S057-S066 use that supplied population-average OR label. | NO_QUALIFYING_CONTRADICTION |

## Provisional candidate emitted by pass 1

### SP1-001 — In-hospital death absolute-difference P value conflicts with its displayed 95% CI

- **Primary category:** Statistical reporting inconsistency.
- **Exact supplied-source location:** DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 8](<../../../jama_wang_2018_oi_180070.pdf#page=8>), Table 3, `Death — In hospital` row.
- **Direct observation:** The adjusted absolute-difference column prints `−0.7 (−1.1 to 0.2)` as a 95% CI and the immediately adjacent P-value column prints `.009`. The same row separately prints HR `.96 (.90 to 1.02)` and its P value `.14`.
- **Consistency rule:** Under the supplied Table 3 labeling, this is a two-sided 95% CI and a P value in the same absolute-difference result column. At the printed precision, a 95% CI that includes the absolute-difference null (0) does not agree with an associated P=.009 (which is below .05) for that same result.
- **Diagnostic calculation (not a replacement analysis):** The displayed CI midpoint is approximately -0.45 percentage points and its half-width approximately 0.65; this gives a rough CI-derived standard error of 0.65/1.96≈0.33 and a rough |z|≈1.36, not an exact reconstruction because the source does not give the CI/P variance estimator or degrees of freedom. The directly observed CI-null/P-threshold discordance, rather than this approximation, is the candidate basis.
- **Matched-result and alternative checks:** No repeated in-hospital absolute-difference P value was located elsewhere in the supplied sources. The HR/P pair is separately labeled and internally compatible (its CI includes 1 and P=.14); it does not resolve the absolute-difference P value. The article does state adjustment and two-sided testing but not whether the displayed absolute-difference CI and P use a special non-common construction.
- **Exact human question:** Does `.009` belong to the in-hospital absolute difference as tabled, and if so what supplied-analysis rule yields that P with `−1.1 to 0.2` as the stated 95% CI? Otherwise, which printed table value is to be corrected?
- **Status:** Pending Human Adjudication. This is a provisional pass-1 candidate, not a stable `C` ID or a final correction.

## Pass-1 completion and limitations

- **Canonical relationships completed:** 67 of 67 (`S001`-`S067`), each explicitly marked `PASS_1_COMPLETE` above.
- **Provisional candidates emitted:** 1 (`SP1-001`).
- **Display-zero exclusion:** no mapped display-zero P values; none were made candidates.
- **Key limitation:** Native-text decimal glyph duplication in DOC-003 was resolved using the fresh coordinate-layout-supported mapper records. Exact P/CI reconstruction was intentionally not attempted where the supplied sources omit an applicable common estimator, sidedness/df rule, covariance structure, or model-to-estimand mapping.
