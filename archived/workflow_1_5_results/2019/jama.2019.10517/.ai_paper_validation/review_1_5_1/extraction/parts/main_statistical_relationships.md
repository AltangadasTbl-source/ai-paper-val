# DOC-001 Inferential-Statistical Relationship Map

All locations refer to direct PDF pages in `jama_flint_2019_oi_190079.pdf`. These are relationship records only; no candidate ID, judgment, or adjudication is assigned.

| Local ID | Location(s) | Population, model, contrast, and reported values | Checkability / status for later statistical passes |
|---|---|---|---|
| MS001 | pp. 1,6-7 | All-randomized primary Cox model: olanzapine+sertraline vs placebo+sertraline relapse risk, adjusted for three randomization strata: HR 0.25, 95% CI 0.13-0.48, P<.001. | CI contains HR and is ordered; matched across abstract/results. |
| MS002 | pp. 6-7 | Primary Cox covariates: age young vs old HR 0.78 (0.42-1.46), P=.44; remission vs near remission HR 2.45 (0.98-6.13), P=.06; Massachusetts vs Cornell HR 1.53 (0.62-3.76), P=.36; Pittsburgh vs Cornell HR 1.09 (0.39-2.98), P=.88; Toronto vs Cornell HR 1.80 (0.81-4.03), P=.15. | Each CI contains its HR; stated references are essential to sign/direction interpretation. |
| MS003 | p. 7 | Post hoc sensitivity Cox model excluding seven medication discontinuers who remained under research assessment: HR 0.22 (0.11-0.43), P<.001. | CI ordered/contains estimate; population differs from MS001. |
| MS004 | p. 7 Figure 2 | Kaplan-Meier group comparison, log-rank P<.001; 95% CI shading; observation distributions reported. | P corresponds to an explicitly distinct log-rank test, not necessarily the Cox-model P. |
| MS005 | p. 7 | Linear mixed-model treatment-by-linear-time effect: weight 0.13 lb/day (0.11-0.15), adjusted P<.001. | CI excludes zero; effect differs from Table 4 raw change. |
| MS006 | p. 7 | Linear mixed-model interaction: waist 0.009 in/day (0.004-0.014), adjusted P=.002. | CI excludes zero. |
| MS007 | p. 7 | Linear mixed-model interaction: total cholesterol 0.29 mg/dL/day (0.13-0.45), adjusted P=.003. | CI excludes zero. |
| MS008 | p. 7 | Linear mixed-model interactions: LDL 0.04 (-0.01 to 0.10), P=.57; HDL -0.01 (-0.03 to 0.01), P=.99; triglyceride -0.153 (-0.306 to 0.004), P=.25; glucose -0.02 (-0.12 to 0.08), P=.99; HbA1c -0.0002 (-0.0021 to 0.0016), P=.99; printed units are mg/dL/day in narrative. | All CIs include zero; P values post hoc Holm adjusted. HbA1c unit must be compared with table scale separately. |
| MS009 | p. 7 | Overdispersed Poisson mixed-effects result: Simpson-Angus weekly change higher with olanzapine by 0.022 points (0.009-0.036), adjusted P=.009. | CI excludes zero; measure scale is defined in Table 2 footnote. |
| MS010 | p. 4-5 | Modelling/multiplicity specification: linear mixed models include random intercept/slope and fixed site/time/treatment/interaction; pattern-mixture models assess early termination; triglyceride is pattern-mixture averaged; tests are two-sided at overall 5%; post hoc Holm adjustments for secondary outcomes. | Required labels for comparing MS005-MS009; no unreported calculation inferred. |
| MS011 | p. 4 | Sample-size calculation: n=176 for 80% power to detect a 20% relapse-risk difference with <=15% attrition; revised approved n=128 due to higher anticipated overall relapse risk. | Planning relationship; actual n=126. |
| MS012 | p. 8 Table 4 | Unadjusted within-arm baseline-to-termination differences with 95% CIs for eight measures per arm. | Table expressly warns displayed difference may not equal simple termination-baseline due to missing data; not a treatment-effect comparison. |
| MS013 | p. 9 Table 5 | Post hoc incident-high-metabolic-value absolute unadjusted between-group differences with 95% exact CIs: total/LDL 4.3% (-8 to 17.2), triglycerides 3.0% (-6.7 to 13.3), glucose -0.2% (-9.9 to 9.9). | Exact-CI footnote; no P values reported. |
