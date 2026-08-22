# Stable Inferential and Statistical Relationship Inventory

## Scope and normalization rule

This inventory normalizes every inferential/statistical lane record from the completed extraction maps. Every stable `S` ID maps to one lane record, with source provenance and match key retained. Similar methods, planning statements, or result families remain separate unless their complete record is identical; no lane record was merged away. This is a coverage inventory, not a candidate assessment.

- **Stable inferential/statistical relationships:** 23 (`S001`-`S023`).
- **Lane composition:** 12 main records (`MS001`-`MS012`) and 11 support records (`SS001`-`SS011`).
- **Genuine identical merges:** none.

| Stable ID | Lane ID | Direct source location | Inferential/statistical relationship coverage | Match key / numeric cross-reference |
|---|---|---|---|---|
| S001 | MS001 | DOC-001 PDF p. 3, Sample Size and Power Calculations | Main-paper power statement: prevalence 10%, 90% power, two-sided alpha=.05, 24-point difference (60% vs 36%). | `power; prev=10%; diff=24pp; 60vs36; alpha=.05; two-sided`; N032 |
| S002 | MS002 | DOC-001 PDF p. 3, Statistical Analyses | Main CI/test methods: Wald/Agresti-Coull and Agresti-Caffo, binomial GLM interactions, two-sided P<.05, no multiplicity adjustment. | `methods; Agresti-Coull; Agresti-Caffo; binomial_GLM; two-sided` |
| S003 | MS003 | DOC-001 PDF p. 3, Sensitivity Analysis | GLMM with site random intercept and LRT of zero variance. | `sensitivity_analysis; GLMM; site_random_intercept; LRT` |
| S004 | MS004 | DOC-001 PDF pp. 1, 3-5, Abstract/Primary Endpoint/Table 2 | Primary all-participant quantitative 10.2 sensitivity contrast, 95% CI and P=.14. | `T2; all; quantitative; 10.2; day2_scheduled`; N013 |
| S005 | MS005 | DOC-001 PDF pp. 1, 4-5, Abstract/Primary Endpoint/Table 2 | Primary all-participant quantitative 17.0 sensitivity contrast, 95% CI and P=.32. | `T2; all; quantitative; 17.0; day2_scheduled`; N014 |
| S006 | MS006 | DOC-001 PDF pp. 4-5, Secondary Endpoints/Table 2 | All-participant quantitative 10.2 specificity contrast, 95% CI and P<.001. | `T2; all; quantitative; 10.2; day2_scheduled`; N013 |
| S007 | MS007 | DOC-001 PDF pp. 4-5, Secondary Endpoints/Table 2 | All-participant quantitative 17.0 specificity contrast, 95% CI and P=.008. | `T2; all; quantitative; 17.0; day2_scheduled`; N014 |
| S008 | MS008 | DOC-001 PDF pp. 4-5, Secondary Endpoints/Table 2 | All-participant qualitative sensitivity/specificity contrasts, CIs, P=.048 and P<.001. | `T2; all; qualitative; 10.2; day2_scheduled`; N015 |
| S009 | MS009 | DOC-001 PDF pp. 4-5, Secondary Endpoints/Table 2 | Sex-specific sensitivity/specificity range narrative and sex-interaction P=.08-.49. | sex-specific `T2` keys; N016-N021 |
| S010 | MS010 | DOC-001 PDF pp. 4-5, Secondary Endpoints/Table 3 | Narrative statement of no significant day-2 PPV/NPV differences in ITS/per-protocol analyses. | `T3; all; all tests; day2; ITT + stated PP`; N022-N024 |
| S011 | MS011 | DOC-001 PDF p. 5, Sensitivity Analysis | LRT site random-intercept results P=.16-.50 and retained no-random-intercept model. | `GLMM site random intercept; LRT; P=.16-.50`; S022-S023 |
| S012 | MS012 | DOC-001 PDF pp. 1-2, 5-6, Abstract/Key Points/Discussion/Conclusion | Repeated conclusion of no significant primary sensitivity increase, linked to the two primary contrasts. | `conclusion; MN013+MN014; primary quantitative day2`; N013-N014 |
| S013 | SS001 | DOC-002 PDF p. 11, §§3.2-3.4 | Protocol endpoint family: primary FOBGold sensitivity; secondary PPV/NPV, specificity, AUC, LR, sex/multiple-day/SAE outcomes. | `primary_sensitivity_FOBGold_predefined_cutpoint` |
| S014 | SS002 | DOC-002 PDF pp. 28-29, §7.1 | Protocol confirmatory comparison, CI/diagnostic metrics and ROC/AUC plan; protocol day 3/SAP day 2 alignment. | `protocol_primary_FOBGold_day3_vs_SAP_day2` |
| S015 | SS003 | DOC-002 PDF pp. 28-29, §7.2 | Protocol power plan: 10% prevalence, 100 diseased/group, placebo 36%, alpha .05 with continuity correction, 90% power, 60% overall/70% sex-specific sensitivity. | `power_10percent_100pergroup_36to60_90power`; S001 |
| S016 | SS004 | DOC-003 PDF p. 7, §§5.1-5.3 | SAP planned CONSORT/baseline/compliance tables and chi-square/Fisher tests. | `CONSORT_baseline_chisquare_Fisher_compliance` |
| S017 | SS005 | DOC-003 PDF p. 8, §5.4 | SAP primary sensitivity/null, day-2 set, adjusted CI methods and two-sided P threshold. | `primary_ITS_or_PP_day2_sensitivity_Agresti`; S002/S004/S005 |
| S018 | SS006 | DOC-003 PDF p. 8, §5.5 | SAP definitions/formulas for specificity, PPV, NPV, LR, ROC, and utilization metrics. | `definitions_specificity_PPV_NPV_LR_ROC_NNT`; N013-N030 |
| S019 | SS007 | DOC-003 PDF p. 8, §5.5 | SAP secondary testing, adjusted CIs, total/partial ROC AUC methods, and binomial-logit mixed model. | `secondary_AUC_partial0.8_DeLong_bootstrap_GLMM` |
| S020 | SS008 | DOC-003 PDF p. 9, §§5.5-5.6 | SAP day-wise, subgroup and interaction-test plan. | `subgroups_sex_age60_smoking_BMI25_advanced_adenoma` |
| S021 | SS009 | DOC-003 PDF p. 9, §7 | SAP change to ITS day-2 primary analysis and Fisher missingness-allocation test. | `primary_analysis_changed_to_ITS_day2_missing_Fisher` |
| S022 | SS010 | DOC-004 PDF p. 8, eTable 6, All | All-participant site random-intercept SDs and LRT P values by test/cutoff/outcome. | `eTable6_site_random_intercept_all_ITS_day2`; S003/S011 |
| S023 | SS011 | DOC-004 PDF p. 8, eTable 6, Men/Women | Sex-specific site random-intercept SDs and LRT P values by test/cutoff/outcome. | `eTable6_site_random_intercept_sex_ITS_day2`; S003/S011 |

## Extraction provenance

- Main lane source: `extraction/main_quantitative_evidence.md` (`MS001`-`MS012`).
- Support lane source: `extraction/support_quantitative_evidence.md` (`SS001`-`SS011`).
- Exact printed estimates, intervals, P values, model labels, populations, and source locations remain in those lane maps; this stable inventory gives the complete downstream `S`-ID coverage set.

## Two-pass completion

- Statistical pass 1 explicitly recorded `PASS_1_COMPLETE` for S001-S023 in `checkers/statistical_pass_1.md`.
- A different fresh statistical agent explicitly recorded `PASS_2_COMPLETE` for S001-S023 in `checkers/statistical_pass_2.md`.
- Pass 2 reviewed C001-C005 and added no new candidate proposal.
