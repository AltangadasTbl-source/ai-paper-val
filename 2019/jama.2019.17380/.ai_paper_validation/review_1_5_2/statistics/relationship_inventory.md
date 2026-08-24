# Canonical Statistical Relationship Inventory

## Merge record

- **Complete statistical relationship count:** 44.
- **PASS_1_COMPLETE:** All S001 through S044 have explicit records in `checkers/statistical_pass_1.md`.
- **PASS_2_COMPLETE:** All S001 through S044 have explicit records in `checkers/statistical_pass_2.md`, including the final C001 through C004 repair refresh.
- **Main mapping:** `MS001`-`MS025` → `S001`-`S025` (25 relationships).
- **Support mapping:** `US001`-`US019` → `S026`-`S044` (19 relationships).
- This merge retains mapper wording, printed values, source locations, comparison boundaries, and limitations without scientific reinterpretation.

| Source part | Provisional IDs | Canonical IDs | Count |
|---|---|---|---:|
| main_statistical_relationships.md | MS001-MS025 | S001-S025 | 25 |
| support_statistical_relationships.md | US001-US019 | S026-S044 | 19 |

## DOC-001 main article (S001-S025)

| ID | Inferential relationship / model / printed statistic | Exact location |
|---|---|---|
| S001 | Planned primary comparison: each active-placebo eGFR-change difference; 80% power for 2.3 mL/min/1.73m², two-sided α=.05, assuming 80% follow-up. | p.3 sample size |
| S002 | Primary linear mixed model: random intercept; baseline/year2/year5 time; treatment×time; age/sex and time interactions; eGFR additionally baseline ACR and its time interaction. | p.3 data analysis |
| S003 | Primary treatment test is treatment×year-5 interaction; 2-tailed P<.05; multiple-imputation M=20 with Rubin rules. | p.3 data analysis |
| S004 | Secondary categorical analyses: Cox proportional hazards; proportional-hazards assumption tested with Schoenfeld residuals. | p.3 data analysis; p.6 statement no significant violations |
| S005 | Vitamin-D biomarker contrast at year2: 41.4 (SD11.0) vs29.8 (11.1) ng/mL, P<.001. | p.4 retention/adherence |
| S006 | Omega-3-index contrast at year2:3.6% (SD1.0) vs2.3% (0.8), P<.001. | p.4 retention/adherence |
| S007 | Vitamin-D primary table result at year5: difference0.9 (95%CI −0.7 to2.5), P=.25. | p.4 results; p.8 Table2 |
| S008 | Omega-3 primary table result at year5: difference0.9 (−0.7 to2.6), P=.27. | p.4 results; p.8 Table2 |
| S009 | Factorial treatment-assignment interaction P=.42. | p.4 results |
| S010 | Full analytic eGFR mean change −12.7 (−13.6 to−11.7); complete case n=932, −12.4 (−13.3 to−11.4). | p.4 results |
| S011 | Composite secondary vitamin-D: HR0.92 (0.68-1.25); narrative says not significant. | p.4 results; p.9 Table3 |
| S012 | Composite secondary omega-3: HR1.11 (0.81-1.50); narrative says not significant. | p.4 results; p.9 Table3 |
| S013 | Vitamin-D ≥40% eGFR decline: HR0.97 (0.63-1.51), P=.90. | p.9 Table3 |
| S014 | Vitamin-D ACR doubling/final≥30: HR1.34 (1.00-1.80), P=.05. | p.9 Table3 |
| S015 | Omega-3 ≥40% eGFR decline: HR0.99 (0.64-1.54), P=.97. | p.9 Table3 |
| S016 | Omega-3 ACR doubling/final≥30: HR1.08 (0.81-1.44), P=.60. | p.9 Table3 |
| S017 | Table3 P values explicitly test null HR=1; HRs are Cox-model estimates. | p.9 Table3 footnotes |
| S018 | Vitamin-D Fig.3 subgroup interaction P sequence .58,.36,.15,.18,.79,.42; corresponding subgroup-row assignment needs visual layout confirmation. | p.8 Fig.3 |
| S019 | Omega-3 Fig.4 subgroup interaction P sequence .72,.70,.73,.51,.42; corresponding subgroup-row assignment needs visual layout confirmation. | p.9 Fig.4 |
| S020 | Figures 3-4 treatment effects are adjusted active-placebo differences in eGFR change baseline-year5, adjusted age/sex/baseline ACR. | pp.8-9 Fig. captions |
| S021 | Narrative: no significant subgroup heterogeneity for either intervention; no significant correlation of biomarker change with eGFR change. | p.4 results |
| S022 | Prespecified secondary outcomes stated exploratory owing to potential type-I error from multiple comparisons. | p.3 data analysis |
| S023 | Narrative reports approximate 3-fold ACR rise and no significant assignment difference; Table3 provides time-to-doubling inferential estimands rather than the continuous ACR effect (referenced eTable6 in support). | p.4 results; p.9 Table3 footnote |
| S024 | Discussion says 95% CIs excluded eGFR-decline differences considered reasonable surrogate (0.75/y=3.75/5y); this is an interpretation of the primary CIs. | p.7 discussion |
| S025 | Post-hoc ≥40% eGFR decline/kidney failure and ≥30%-decline composites reported not significant, with details in Supplement2 eTable10. | p.4 results |

## DOC-002 through DOC-004 support sources (S026-S044)

| ID | Exact source location | Printed statistical relationship / definition | Required later comparison boundary |
|---|---|---|---|
| S026 | DOC-003 PDF pp.2-4 | Cystatin-C post-shift calibration multiplier 5.49/5.961; harmonization `0.006801+1.037603×pre-shift`; QC r=.999. | Laboratory transform, not an outcome test. |
| S027 | DOC-002 PDF p.17 | Original ACR ANCOVA/log transform and eGFR equation; alpha=.05, no multiple-comparison correction; chi-square for composite proportions; rank-sum if indicated. | Original plan, year-4, not automatically equivalent to final plan. |
| S028 | DOC-002 PDF p.18 | Original factorial interaction equation beta4 on log(ACR4); P<.05 interaction rule; additive contrast defined as joint-active difference versus sum of two single-active differences. | Need matched outcome/scale/timepoint to compare. |
| S029 | DOC-002 PDF pp.18-19 | Original hypothesis-test equations: exp(beta2)-1 is relative ACR percent-change difference; eGFR beta2 is active-v-placebo difference. | ANCOVA plan; baseline adjustment explicit. |
| S030 | DOC-002 PDF pp.19-20 | Original power model assumptions and displayed power table, including 90% at 17% ACR and 2.6 eGFR. | Projection only; no observed effect inference. |
| S031 | DOC-002 PDF p.23 | Haybittle-Peto interim rule z=3, P=.0027; multiple looks. | Parent monitoring rule; not a reported P value. |
| S032 | DOC-002 PDF p.32 | Final addendum missing-data plan: chained-equation MI for missing y5 eGFR with baseline plus y2 eGFR/ACR; 10 datasets and Rubin rules. | Final-plan model distinction from original complete-case text. |
| S033 | DOC-002 PDF p.32 | Final factorial mixed interaction model; categorical time j=0,2,5; random patient effect; beta6 P<.05 is interaction evidence. | Final interaction definition. |
| S034 | DOC-002 PDF pp.32-33 | Final primary random-intercept mixed model: beta3 = active-D3 vs placebo difference in eGFR change; 95% CI/P for effect; inference year5 only. ACR log-continuous; discrete Cox for categorical secondary outcomes. | Match test/model/endpoint before CI/P checks. |
| S035 | DOC-002 PDF p.33 | Simulation 2,000 replications; n=1,058, two-sided alpha=.05; 80% power for 2.3 mL/min/1.73m2 at y5. | Projection only. |
| S036 | DOC-003 PDF p.9 | eTable 4 eGFR: linear mixed model adjusted age/sex/baseline urine ACR, MI; P tests year5 difference in change. D .87 (-.83,2.58), P=.32; omega .09 (-1.61,1.80), P=.92. | Same endpoint/model/contrast for interval-P compatibility. |
| S037 | DOC-003 PDF p.10 | eTable 5 eGFR adherent: same mixed-model/MI footnote; D .89 (-.74,2.52), P=.28; omega .42 (-1.22,2.06), P=.61. | Sensitivity population differs from S036. |
| S038 | DOC-003 PDF p.11 | eTable 6 uACR mixed model adjusted age/sex, MI; P tests y5 change difference; ratio effects D .99 (.84,1.17), P=.90; omega .96 (.81,1.14), P=.64. | Ratio/null=1, not eGFR difference/null=0. |
| S039 | DOC-003 PDF p.12 | eTable 7 paired uACR: same model/MI, D 1.03 (.86,1.22), P=.77; omega .93 (.78,1.11), P=.44. | Paired baseline/y5 subset. |
| S040 | DOC-003 PDF p.13 | eTable 8 adherent uACR: D 1.02 (.85,1.22), P=.87; omega .99 (.83,1.19), P=.94. | Adherent population. |
| S041 | DOC-003 PDF p.14 | eTable 9 UTI-excluded uACR: D .99 (.84,1.17), P=.90; omega .98 (.83,1.16), P=.80. | Visit-exclusion sensitivity. |
| S042 | DOC-003 PDF p.15 | eTable 10 post-hoc Cox regression HRs, P tests HR=1; eight HR/CI/P records. | HR/null=1 and event-rate versus HR distinction. |
| S043 | DOC-003 PDF p.17 | eFigure 1 correlations, changes marker baseline-y2/eGFR baseline-y5, complete available data. Correlation coefficients/plot values unavailable in native text. | No coefficient or P inferred. |
| S044 | DOC-003 PDF pp.18-19 | eFigure 2/3 subgroup ACR difference-in-change estimates adjusted age/sex. Plot estimates/CIs/P/subgroup strata unavailable in native text. | No inferential reconciliation possible without direct visual values. |

## Carried-forward limitations

No permitted renderer/layout extractor was available. Figure 3/4 P values were read in native segment order and are preserved, but row-to-P alignment is not asserted without visual confirmation. No inferential conclusion or quality-control candidate is made here.

Statistical coverage limitation: no `P=0` display occurs in the mapped usable support text. All CIs, P values, effect measures, model labels, and definitions exposed by the fresh native text are listed above. DOC-004 contains no inferential result.
