# Statistical Relationship Inventory — Pass 1

## Scope and conventions

Pass 1 covered the supplied direct sources in their entirety: DOC-001 `jama_dupuis_2024_oi_240111_1733431204.38761.pdf` (pp. 1-11), DOC-002 `joi240111supp1_prod_1733431204.57929.pdf` (pp. 1-46), and DOC-003 `joi240111supp2_prod_1733431204.76024.pdf` (pp. 1-23): **80 PDF pages**. Source locations below are direct-source PDF pages. The two canonical extraction maps were used as locators and coverage maps; their cited printed values were checked as statistical relationships, not imported as prior findings.

`PASS_1_COMPLETE` means that the stated relationship was checked for point-estimate containment, endpoint ordering, sign/direction, effect-measure/scale labels, and matching repeated locations. Interval/P/test/statistic/SE compatibility was assessed only where the source supplied compatible definitions. `No raw candidate emitted` is a pass-1 discovery result, not an adjudication or a statement about validity.

| ID | Inferential relationship and direct-source location(s) | Pass-1 checks and missing-definition note | Pass-1 result | Status |
|---|---|---|---|---|
| S001 | Primary week-8 total-SSPedi mixed linear model: adjusted mean difference, 95% CI, two-sided P; DOC-001 pp. 3,7; DOC-002 pp. 11,36; DOC-003 pp. 9,22. | Continuous-scale direction (lower is less symptom burden), contrast, and repeated labels agree. CI contains estimate and endpoints order. Source does not state CI construction, df, variance estimator, or covariance. | No raw candidate emitted. | PASS_1_COMPLETE |
| S002 | Individual SSPedi proportional-odds OR model; DOC-001 pp. 4,7; DOC-002 pp. 11,36-37; DOC-003 pp. 20,22. | OR is for a higher/worse score; OR<1 direction agrees with labels and narrative. All printed 95% CIs order and contain the OR. No CI/test construction or random-effect variance is supplied. | No raw candidate emitted. | PASS_1_COMPLETE |
| S003 | PROMIS/PedsQL linear models, documentation/intervention logistic models, and encounter Poisson models; DOC-001 pp. 4,7,9; DOC-002 pp. 12,37-39; DOC-003 pp. 13-17,22. | Effect measures and scale directions are separately labeled. Model definitions do not provide a common test/CI construction across all submodels. | No raw candidate emitted. | PASS_1_COMPLETE |
| S004 | Two-sided significance convention P<.05; DOC-001 p. 4; DOC-002 pp. 10-14,33-40. | Explicit two-sided rule applies where frequentist P is reported; not transferred to Bayesian credible-region/probability results. | No raw candidate emitted. | PASS_1_COMPLETE |
| S005 | Participation-decline comparison: 16.6% vs 15.5%, P=.81; DOC-001 p.4; DOC-003 p.22. | Matched repeated values agree. Test type, denominator-specific variance, and exact test are absent. | No raw candidate emitted. | PASS_1_COMPLETE |
| S006 | Primary treatment effect: adjusted MD -3.8 (95% CI -6.4 to -1.2), P=.007; DOC-001 pp.1,2,4,7,10; DOC-003 pp.9,18-19. | Estimate is contained; ordered CI is wholly below 0 and direction matches symptom scale and narrative. Repeated locations agree; compatible linear-model definitions are supplied, but df/CI calculation are absent. | No raw candidate emitted. | PASS_1_COMPLETE |
| S007 | Sad symptom adjusted OR .46 (.26-.83), P=.01; DOC-001 p.7; DOC-003 p.20. | Ordered CI contains OR; OR<1 agrees with higher/worse outcome direction; figure repeat agrees. | No raw candidate emitted. | PASS_1_COMPLETE |
| S008 | Worried symptom adjusted OR .57 (.38-.85), P=.005; DOC-001 p.7; DOC-003 p.20. | Containment, order, direction, and repeated figure agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S009 | Angry symptom adjusted OR .43 (.29-.63), P<.001; DOC-001 p.7; DOC-003 p.20. | Containment, order, direction, and repeated figure agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S010 | Thinking/remembering adjusted OR .62 (.42-.90), P=.01; DOC-001 p.7; DOC-003 p.20. | Containment, order, direction, and repeated figure agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S011 | Body/face adjusted OR .52 (.31-.88), P=.01; DOC-001 p.7; DOC-003 p.20. | Containment, order, direction, and repeated figure agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S012 | Tired adjusted OR .52 (.36-.74), P<.001; DOC-001 p.7; DOC-003 p.20. | Containment, order, direction, and repeated figure agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S013 | Mouth-sores adjusted OR .48 (.27-.85), P=.01; DOC-001 p.7; DOC-003 p.20. | Containment, order, direction, and repeated figure agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S014 | Headache adjusted OR .61 (.41-.90), P=.01; DOC-001 p.7; DOC-003 p.20. | Containment, order, direction, and repeated figure agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S015 | Other-pain adjusted OR .69 (.47-1.01), P=.06; DOC-001 p.7; DOC-003 p.20. | Containment/order and direction agree; interval crosses 1 consistently with rounded P. | No raw candidate emitted. | PASS_1_COMPLETE |
| S016 | Tingling adjusted OR .76 (.50-1.15), P=.19; DOC-001 p.7; DOC-003 p.20. | Containment/order and direction agree; interval crosses 1 consistently with rounded P. | No raw candidate emitted. | PASS_1_COMPLETE |
| S017 | Vomiting adjusted OR .80 (.51-1.26), P=.34; DOC-001 p.7; DOC-003 p.20. | Containment/order and direction agree; interval crosses 1 consistently with rounded P. | No raw candidate emitted. | PASS_1_COMPLETE |
| S018 | Hunger adjusted OR .63 (.44-.90), P=.01; DOC-001 p.7; DOC-003 p.20. | Containment, order, direction, and repeated figure agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S019 | Taste adjusted OR .56 (.34-.90), P=.02; DOC-001 p.7; DOC-003 p.20. | Containment, order, direction, and repeated figure agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S020 | Constipation adjusted OR .55 (.31-.95), P=.03; DOC-001 p.7; DOC-003 p.20. | Containment, order, direction, and repeated figure agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S021 | Diarrhea adjusted OR .37 (.19-.73), P=.004; DOC-001 pp.4,7; DOC-003 p.20. | Containment/order/direction agree; figure and “12 of 15” narrative agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S022 | PROMIS fatigue adjusted MD -.7 (-4.0 to 2.5), P=.64; DOC-001 pp.4,7. | CI contains estimate and crosses 0; higher=worse scale agrees with interpretation. No repeated inferential estimate in supplement. | No raw candidate emitted. | PASS_1_COMPLETE |
| S023 | PedsQL pain adjusted MD .2 (-5.9 to 6.2), P=.95; DOC-001 p.7; DOC-003 p.21. | Containment/order; positive=higher/better direction; figure repeat agrees. | No raw candidate emitted. | PASS_1_COMPLETE |
| S024 | PedsQL nausea adjusted MD 1.3 (-4.9 to 7.6), P=.66; DOC-001 p.7; DOC-003 p.21. | Containment/order/direction and figure repeat agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S025 | PedsQL procedural-anxiety adjusted MD 3.0 (-4.5 to 10.5), P=.41; DOC-001 p.7; DOC-003 p.21. | Containment/order/direction and figure repeat agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S026 | PedsQL treatment-anxiety adjusted MD 2.9 (-3.4 to 9.1), P=.34; DOC-001 p.7; DOC-003 p.21. | Containment/order/direction and figure repeat agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S027 | PedsQL worry adjusted MD 3.6 (-2.4 to 9.6), P=.22; DOC-001 p.7; DOC-003 p.21. | Containment/order/direction and figure repeat agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S028 | PedsQL cognitive-problems adjusted MD 1.2 (-5.5 to 7.9), P=.71; DOC-001 p.7; DOC-003 p.21. | Containment/order/direction and figure repeat agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S029 | PedsQL appearance adjusted MD .6 (-5.0 to 6.1), P=.83; DOC-001 p.7; DOC-003 p.21. | Containment/order/direction and figure repeat agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S030 | PedsQL communication adjusted MD 1.8 (-3.1 to 6.6), P=.45; DOC-001 pp.4,7; DOC-003 p.21. | Containment/order/direction; figure and narrative repeats agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S031 | Baseline ad-hoc adjusted MD -1.8 (-3.5 to -.1), P=.04; DOC-001 p.4; DOC-003 p.10. | Containment/order/direction; source identifies analysis as ad hoc. No model variance/CI construction supplied. | No raw candidate emitted. | PASS_1_COMPLETE |
| S032 | Week-8 baseline-adjusted sensitivity MD -3.0 (-5.2 to -.8), P=.01; DOC-001 p.4; DOC-003 p.18. | Containment/order/direction agree. Baseline is explicitly described as on the intervention pathway; this is not treated as a cross-model contradiction. | No raw candidate emitted. | PASS_1_COMPLETE |
| S033 | Documentation effects: tired OR .62 (.39-.97), P=.04; hunger OR .54 (.30-.95), P=.03; DOC-001 pp.4-5; DOC-003 pp.13-15. | Main narrative numerator/denominator values, direction, and eTable 10 effects agree. eTable 10 says mixed or fixed logistic according to events; per-cell model choice, CI construction, and test are absent. | No raw candidate emitted. | PASS_1_COMPLETE |
| S034 | Any-intervention effects: sad OR .51 (.26-.99), P=.05; worried OR .40 (.19-.83), P=.01; DOC-001 p.5; DOC-003 pp.13-15. | Main narrative and eTable 10 agree. Event-dependent mixed/fixed model selection prevents unsupported interval/P reconstruction. | No raw candidate emitted. | PASS_1_COMPLETE |
| S035 | All-encounter adjusted Poisson RR 1.46 (.97-2.19), P=.07; DOC-001 p.9; DOC-003 p.17. | CI contains RR and crosses 1; Poisson label, direction and repeat agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S036 | ED adjusted Poisson RR 1.72 (1.03-2.87), P=.04; DOC-001 pp.1,6,9; DOC-003 p.17. | CI contains RR, lies above 1, direction and repeated abstract/narrative/table values agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S037 | Clinic RR 1.01 (.41-2.50), P=.99 and hospital RR 1.40 (.96-2.03), P=.08; DOC-001 p.9; DOC-003 p.17. | Both CIs contain RRs and cross 1; directions, labels and alternative-model table agree. | No raw candidate emitted. | PASS_1_COMPLETE |
| S038 | Final planned power simulation: 4,000 trials, two-sided alpha .05, ICC/difference grid, focal 85.2%; DOC-002 pp.10,24,33-34. | Planned simulation result, not observed study inference. ICC .000 is an ICC value, not a P-value display zero. | No raw candidate emitted. | PASS_1_COMPLETE |
| S039 | Final SAP planned models, imputation, and effect definitions; DOC-002 pp.11-14,35-40. | Plans match reported model families sufficiently for label/estimand comparisons; planned model options are not assumed to identify the actually used alternative for every result. | No raw candidate emitted. | PASS_1_COMPLETE |
| S040 | Protocol background external survival comparison 31.2 (24.5-39.6) vs 26.0 (22.1-30.9), P=.03; DOC-002 pp.3-4,19-20. | Both group intervals are ordered/contain point estimates. Comparator/test/model and survival estimand are not supplied in this package. | No raw candidate emitted. | PASS_1_COMPLETE |
| S041 | Protocol background instrument validation: ICC .88 (.82-.92), .76 (.71-.80); MD 7.8 (6.4-9.2), P<.001; responsiveness 5.6 (3.8-7.5), P<.001; DOC-002 pp.3-4,19-20. | Containment/order and effect labels agree. Study populations, tests, and CI construction are not supplied. | No raw candidate emitted. | PASS_1_COMPLETE |
| S042 | eTable 6 week-8 model: intercept and seven non-reference covariate estimates/95% CIs/Ps, including intervention effect; DOC-003 p.9. | Each printed estimate is contained in ordered CI. All P directions are compatible at displayed precision. Same underlying model as S001/S006; no separate CI/test construction stated. | No raw candidate emitted. | PASS_1_COMPLETE |
| S043 | eTable 7 baseline ad-hoc model: intercept and seven non-reference covariate estimates/95% CIs/Ps; DOC-003 p.10. | Each estimate is contained in ordered CI; treatment row matches S031. Model is explicitly ad hoc; CI/test construction absent. | No raw candidate emitted. | PASS_1_COMPLETE |
| S044 | eTable 8: 15 post-hoc severely-bothersome symptom absolute risk differences with 95% credible intervals; DOC-003 p.11. | Every RD is contained in ordered credible interval. Outcome=score 3/4 and measure=absolute risk difference are explicitly labeled; Bayesian interval is not paired with a frequentist P. | No raw candidate emitted. | PASS_1_COMPLETE |
| S045 | eTable 10 documentation: 15 symptoms × all participants, SSPedi>=1, SSPedi>=3 (45 OR/CI/P comparisons); DOC-003 pp.13-15. | Every OR is contained in an ordered printed CI; outcome/denominator cohorts are labeled. Source says mixed **or** fixed logistic depending on events, but does not give per-cell method, CI method, test statistic, SE, or covariance. Diagnostic CI/P comparisons were not used as candidate rules. The common header says `Difference (95% CI)` while eMethods calls the reported logistic estimate an odds ratio. | One raw label/measure candidate recorded below, shared with S046-S047. | PASS_1_COMPLETE |
| S046 | eTable 10 any intervention: 15 symptoms × all participants, SSPedi>=1, SSPedi>=3 (45 OR/CI/P comparisons); DOC-003 pp.13-15. | Every OR is contained in an ordered printed CI; cohort-specific denominators and non-symptom-specific outcome label are explicit. Per-cell model/test/CI method is missing as in S045. The common header says `Difference (95% CI)` while eMethods calls the reported logistic estimate an odds ratio. | One raw label/measure candidate recorded below, shared with S045/S047. | PASS_1_COMPLETE |
| S047 | eTable 10 symptom-specific intervention: 15 symptoms × all participants, SSPedi>=1, SSPedi>=3 (45 OR/CI/P comparisons); DOC-003 pp.14-15. | Every OR is contained in an ordered printed CI and distinguishes symptom-specific from any intervention. Per-cell mixed/fixed choice, CI method, test statistic and SE are missing. The common header says `Difference (95% CI)` while eMethods calls the reported logistic estimate an odds ratio. | One raw label/measure candidate recorded below, shared with S045-S046. | PASS_1_COMPLETE |
| S048 | eTable 12 all/ED/clinic/hospital Poisson primary, frequentist negative-binomial, and Bayesian negative-binomial RRs; DOC-003 p.17. | Each RR is contained in ordered CI/credible region. Frequentist Ps are not compared to Bayesian probability/credible-region results; negative-binomial ED frequentist nonconvergence is directly reported. | No raw candidate emitted. | PASS_1_COMPLETE |
| S049 | Sensitivity: unadjusted-strata-only MD -3.7 (-6.3,-1.1), P=.008; DOC-003 p.18. | Containment/order/direction agree. Different covariate set is explicit, so not compared as the same estimand as S006. | No raw candidate emitted. | PASS_1_COMPLETE |
| S050 | Sensitivity: square-root MD -.7 (-1.1,-.3), P=.003; DOC-003 p.18. | Containment/order agree on transformed scale. Transformed estimate is not directly numerically compared with untransformed S006. | No raw candidate emitted. | PASS_1_COMPLETE |
| S051 | Sensitivity: chemotherapy subset MD -3.8 (-6.4,-1.2), P=.01; DOC-003 p.18. | Containment/order/direction agree. Different population is explicit; same printed effect/CI as S006 is not treated as an identity contradiction because P may use a subset-specific test. | No raw candidate emitted. | PASS_1_COMPLETE |
| S052 | Sensitivity: baseline-adjusted MD -3.0 (-5.2,-.8), P=.01; DOC-003 p.18. | Containment/order/direction agree; matches S032. | No raw candidate emitted. | PASS_1_COMPLETE |
| S053 | Baseline-to-week-8 slope .5 (.4-.6), P<.001; DOC-003 p.18. | Containment/order and positive association direction agree. Regression form, SE, df and CI method absent. | No raw candidate emitted. | PASS_1_COMPLETE |
| S054 | Missing-data sensitivity grid: complete case, MICE, low/high quartile, best/worst case (six MD/CI/P results); DOC-003 p.19. | Every MD is contained in ordered CI. Imputation scenario and population/model differ by row; no unsupported common-test reconstruction. | No raw candidate emitted. | PASS_1_COMPLETE |
| S055 | eFigure 2 15 symptom adjusted OR/CI results; DOC-003 p.20. | All 15 values/CI endpoints agree with S007-S021; figure direction explicitly says OR<1 is lower/less bothersome. | No raw candidate emitted. | PASS_1_COMPLETE |
| S056 | eFigure 3 eight PedsQL adjusted MD/CI/P results; DOC-003 p.21. | All eight values, CIs, Ps, scale direction and model label agree with S023-S030. | No raw candidate emitted. | PASS_1_COMPLETE |
| S057 | eText participation/physician-preference comparisons: seven P values and two percentage/median comparisons; DOC-003 p.22. | Directions and population comparators are explicit. Test types, df, and denominator/variance definitions are absent. | No raw candidate emitted. | PASS_1_COMPLETE |

## Pass-1 coverage notes

* **Stable S records:** 57 (S001-S057). The three eTable 10 records deliberately retain all 135 printed model comparisons in their stated 15×3 scope, including each individual estimate, interval, and P value; they are not sampled.
* **Raw statistical candidates:** 1. The candidate is not assigned a `C` ID in this pass; its exact source comparator and rule are recorded below for coordinator registration.
* **Display-zero records:** 0. No P-value display zero was found. `0.000` at DOC-002 pp. 10, 24, and 34 is the ICC row of planned power tables, not a P value.
* **Diagnostic approximations:** none used to create a candidate. In particular, eTable 10’s extreme sparse-data ORs were not reverse-engineered into P values because the source does not provide the per-cell model fallback, CI construction, test statistic, SE, or variance estimator.

## Raw candidate for coordinator registration (no C ID assigned here)

**eTable 10 effect-measure header versus stated logistic estimand.** DOC-003 eTable 10 on pp. 13-15 labels its effect column `Difference (95% CI)` for documentation, any intervention, and symptom-specific intervention. DOC-003 eMethods p. 22 states that each of those analyses fit a logistic regression model to estimate an **odds ratio**, and the table itself reports multiplicative values such as 0.53 (0.28, 1.01), 17.96 (1.03, 313.1), and 5.30 (2.50, 11.24). Under the supplied-source model definition, `Difference` conflicts with the stated odds-ratio effect measure. Direct observation is the differing printed label versus method definition; the cause and intended presentation require human adjudication.

## Pass-2 handoff

Pass 2 must revisit every S001-S057 against the complete cross-lane candidate ledger and mechanical recheck, then append `PASS_2_COMPLETE` to every record without changing these pass-1 observations.

## Pass-2 completion status

This status field supplements, and does not alter, the pass-1 evidence or candidate observations above. The independent pass-2 record is [statistical_pass_2.md](../checkers/statistical_pass_2.md). Every stable relationship was revisited against the full ledger C001-C003 and mechanical recheck facts.

| ID | Pass-2 status | Pass-2 ledger implication |
|---|---|---|
| S001 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S002 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S003 | PASS_2_COMPLETE | C003 confined to eTable 10 header. |
| S004 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S005 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S006 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S007 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S008 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S009 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S010 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S011 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S012 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S013 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S014 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S015 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S016 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S017 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S018 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S019 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S020 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S021 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S022 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S023 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S024 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S025 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S026 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S027 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S028 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S029 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S030 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S031 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S032 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S033 | PASS_2_COMPLETE | C003 header issue already registered; no duplicate. |
| S034 | PASS_2_COMPLETE | C003 header issue already registered; no duplicate. |
| S035 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S036 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S037 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S038 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S039 | PASS_2_COMPLETE | C003 method definition considered; no duplicate. |
| S040 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S041 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S042 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S043 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S044 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S045 | PASS_2_COMPLETE | C003 header/odds-ratio conflict already registered; no duplicate. |
| S046 | PASS_2_COMPLETE | C003 header/odds-ratio conflict already registered; no duplicate. |
| S047 | PASS_2_COMPLETE | C003 header/odds-ratio conflict already registered; no duplicate. |
| S048 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S049 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S050 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S051 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S052 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S053 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S054 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S055 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S056 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
| S057 | PASS_2_COMPLETE | No matched C001-C003 inferential contradiction. |
