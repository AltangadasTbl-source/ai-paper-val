# Support 001 statistical relationship inventory

**Scope:** DOC-002 `joi190079supp1_prod.pdf` PDF pp. 1-21. Local IDs are shard-local (`A-S001` onward), not stable package IDs. The document is a protocol/SAP, so planned definitions and inferential rules are mapped separately from historical STOP-PD statistics it cites.

| Local ID | PDF page(s) | Statistical relationship and direct evidence | Definition/checkability |
|---|---:|---|---|
| A-S001 | 3 | H1: continuing sertraline+olanzapine is associated with lower relapse risk than sertraline+placebo. | Primary planned contrast; relapse is the endpoint. |
| A-S002 | 3 | H2: continuation has higher weight, total cholesterol, triglycerides in randomized phase. | Secondary planned safety contrast. |
| A-S003 | 3 | H3: older age has less open-label weight gain. | Secondary planned age association. |
| A-S004 | 6 | Historical remission OR=1.28, 95% CI 1.12-1.47, P<.001. | Effect/CI direction coherent (CI entirely >1); model details are not reproduced on this page. |
| A-S005 | 6 | Historical 41.9% vs23.9%, chi-square(1)=9.53, P=.002; NNT=5.6. | Proportion contrast and test are explicitly linked. |
| A-S006 | 6 | Historical 66.7% vs49.2%, chi-square(1)=4.4, P=.036; NNT=5.7. | Proportion contrast and test are explicitly linked. |
| A-S007 | 6 | Historical age remission OR=1.05, 95% CI .80-1.37, P=.75. | CI contains 1 and P is nonsignificant directionally; no contradiction observed. |
| A-S008 | 6 | Historical weight F(1,226)=14.51, P=.0002; glucose t(211)=2.65, P=.009. | F/t statistics, df, P, units and stated age direction are supplied. |
| A-S009 | 6 | Historical PK variability t(166)=.36, P=.72; magnitude unequal-variances t(102)=1.0, P=.32. | Separate tests for variability/magnitude; means/SDs and n groups supplied. |
| A-S010 | 7 | Historical glucose age-by-time F(3,149)=3.16, P<.03; triglycerides .08, total cholesterol .07, LDL .09. | Fixed-effect test statement; model specification is not given in this passage. |
| A-S011 | 10-12 | HOMA is primary glycemic measure calculated from fasting glucose/insulin; HbA1c is secondary. PK magnitude=AUC/average concentration; variability=Cpred/obs. | Measure definitions/scale labels required for later comparison. |
| A-S012 | 12 | Primary relapse composite and time-to-relapse definition. | Specifies threshold-based event components and origin/time scale (weeks after randomization). |
| A-S013 | 13 | General inference: transformations as needed; t tests continuous, Mann-Whitney ordinal, chi-square categorical; ITT for primary analyses; H1-H3 two-tailed alpha .05. | Planned test-family/alpha definitions. |
| A-S014 | 13-14 | H1 Cox PH model and Kaplan-Meier descriptives; censor at discontinuation/end follow-up; predictors treatment/site/remission group/age; conditional covariates require P<=.05 and r>.30. | Defines model, censoring, time scale, adjustment, and selection rule. |
| A-S015 | 14 | Cox diagnostics: compare prior-week HAM-D for dropout/non-dropout; assess constant hazards through treatment x vulnerable-period interaction. | Planned noninformative-censoring/PH-related checks; no result supplied. |
| A-S016 | 14 | H2 separate mixed-effects linear models; repeated counts 15/5; LR tests for quadratic time, treatment-site, treatment-time; reject H0 if latter interaction significant. | Planned model/test sequence and stated decision rule. |
| A-S017 | 14 | H3 mixed-effects linear model; age fixed effect; LR quadratic time and age-time; reject H0 if interaction significant. | Planned model/test rule, open-label setting. |
| A-S018 | 14-15 | E1 age moderation is magnitude-focused and has no significance testing. E2 uses one genotype/model Cox/mixed models after call rate, MAF, HWE filters. | Explicit exploratory status and no-significance instruction for E1; P<.001 HWE filter for E2. |
| A-S019 | 15 | Table 2: H1 simulation power, two-tailed alpha .05, N=176/88 per group, survival analysis using S+ `survfit`. | Six printed assumption/power scenarios mapped in A-N022. |
| A-S020 | 16 | Table 3: SAS PROC MIXED power, ICC .50 lipids and .95 weight; stated >=.80 / >.80 targets and standardized effects. | Model/power assumptions and units mapped in A-N024. |
| A-S021 | 16 | Attrition sensitivity: mixed models valid under ignorable attrition; pattern-mixture and Intent-to-Attend covariate comparisons. | Planned assumption checks/sensitivity analyses. |
| A-S022 | 19 | Annual reliability: ICC .93-.98 GRID HAM-D and .69-.84 DAS conviction. | Historical reliability coefficients; scale-specific. |

## Statistical observation status

- All printed P values in the assigned pages are nonzero displays. `DISPLAY_ZERO_NOT_CANDIDATE` is not applicable.
- No inferential candidate is assigned in this mapper artifact. The p. 21 versus pp. 7/17 recruitment-number conflict is tracked as numeric relationship A-N027, not an inferential incompatibility.
- Missing definitions that limit only deeper verification: historical STOP-PD model details for the p. 6 ORs and the precise historical model for p. 7 age-by-time tests are not supplied in the assigned passages. This prevents model reconstruction but does not negate mapping of the printed statistics.

## No-applicable statistical units

PDF p. 1 (contents), and the non-table administrative narrative on pp. 17-21, contain no additional planned hypothesis test or result-relevant inferential statistic beyond A-S022 and the associated quantitative data-quality metrics.
