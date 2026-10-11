# Complete Statistical relationship inventory

All mapper relationship rows retained. Canonical IDs follow relationships/id_crosswalk.md. Source context, definitions and complete page coverage are in the four mapping artifacts; derivatives are locators and supplied sources remain final authority.


### Mapping provenance: extraction/main_quantitative_evidence.md

## Statistical relationships: all printed trial estimates, intervals and P values

Table 2 is [PDF p7](../../../jama_cooper_2018_oi_180132.pdf#page=7), titled Primary and Secondary Outcomes, Adverse Events, and Subgroups. Its footnote says intention-to-treat; n/N(%) unless otherwise indicated. Primary binary, mortality and adverse-event comparisons are stated to be unadjusted χ² equal-proportions tests (p3), 2-sided P<.05 (p4), with RR and risk difference and95% CIs. All Table 2 CI levels below are95%; the source reports no numeric χ² statistics or standard errors. Outcome contrasts H vs C; differences H−C. The printed estimates are transcribed without recalculation or reassignment to neighboring rows.

| ID | Outcome/population and time | H n/N (%) | C n/N (%) | Absolute difference pp (95% CI) | RR (95% CI) | P | Exact source / matching claim |
|---|---|---|---|---|---|---|---|
| S001 | Primary favorable GOS-E5–8, observed6-mo primary evaluation set | 117/240 (48.8) | 111/226 (49.1) | −0.4 (−9.4 to8.7) | 0.99 (0.82–1.19) | .94 | p7 Table2; p5 Primary Outcome exact same; p1 abstract prints risk difference **0.4%** with CI−9.4% to8.7%, RR/P same; p2 Key Points48.8/49.1 and nonsignificant; p7 Figure3/p8 conclusion no neurologic benefit |
| S002 | Severity-adjusted favorable6-mo GOS-E using IMPACT-TBI | — | — | — | 0.98 (0.87–1.11) | .75 | p7 Table2; p5 result similar after IMPACT-TBI extended adjustment; hierarchical multivariable log-binomial/random strata p3–4 |
| S003 | Ordinal6-mo GOS-E | — | — | — | **OR**0.97 (0.71–1.34) | .88 | [p5 Secondary Outcomes](../../../jama_cooper_2018_oi_180132.pdf#page=5); ordinal logistic, proportional odds justified score test p4; no adjusted ordinal estimate printed main |
| S004 | Hospital death, ITT observed hospital mortality | 52/260 (20.0) | 43/239 (18.0) | 2.0 (−4.9 to8.9) | 1.11 (0.77–1.60) | .57 | p7 Table2; mortality discharge endpoint p3 |
| S005 | Death6 mo, mortality set distinct from primary evaluation | 54/256 (21.1) | 44/239 (18.4) | 2.7 (−4.3 to9.7) | 1.15 (0.80–1.64) | .45 | p7 Table2; p5 Secondary Outcomes repeats entire row; p4 Figure1 denominators |
| S006 | Time to death, censored6 mo/last known contact | — | — | — | **HR**1.13 (0.76–1.69) | .54 | [p5 Secondary Outcomes](../../../jama_cooper_2018_oi_180132.pdf#page=5), eFigure2 pointer; Cox PH, KM/log-rank description p4 |
| S007 | Pneumonia within10 d randomization | 143/260 (55.0) | 123/240 (51.3) | 3.8 (−5.0 to12.5) | 1.07 (0.91–1.27) | .40 | p7 Table2; p1 abstract/p5 narrative repeat rates; eTable6 pointer |
| S008 | Bacteremia within10 d | 19/260 (7.3) | 12/240 (5.0) | 2.3 (−1.9 to6.5) | 1.46 (0.72–2.95) | .29 | p7 Table2 |
| S009 | Other infection within10 d | 36/260 (13.8) | 38/240 (15.8) | −2.0 (−8.2 to4.3) | 0.87 (0.57–1.33) | .53 | p7 Table2 |
| S010 | New/increased intracranial bleeding within10 d | 47/260 (18.1) | 37/240 (15.4) | 2.7 (−3.9 to9.2) | 1.23 (0.43–3.5) | .70 | p7 Table2 exact row visually aligned; p1/p5 repeat rates |
| S011 | New significant extracranial bleeding within10 d | 8/260 (3.1) | 6/240 (2.5) | 0.6 (−2.3 to3.5) | 1.17 (0.79–1.74) | .43 | p7 Table2 exact row visually aligned |
| S012 | Favorable6-mo GOS-E, surgically removed hematoma YES | 22/66 (33.3) | 27/68 (39.7) | −6.4 (−22.6 to9.9) | 0.84 (0.54–1.32) | .44 | p7 Table2; footnote c interaction.43; primary set partition |
| S013 | Same subgroup NO | 95/174 (54.6) | 84/158 (53.2) | 1.4 (−9.3 to12.2) | 1.03 (0.84–1.25) | .79 | p7 Table2; same interaction.43 |
| S014 | Favorable6-mo GOS-E, any intracranial mass lesion MarshallV+VI YES | 22/69 (31.9) | 28/71 (39.4) | −7.6 (−23.4 to8.3) | 0.81 (0.52–1.27) | .35 | p7 Table2; footnote d interaction.33; primary set partition |
| S015 | Same subgroup NO | 95/171 (55.6) | 83/155 (53.5) | 2.0 (−8.8 to12.8) | 1.04 (0.85–1.27) | .72 | p7 Table2; same interaction.33 |
| S016 | Treatment×surgically evacuated hematoma interaction | Subgroup S012 | Subgroup S013 | — | — | .43 | p7 Table2 footnote c; logistic treatment/subgroup interaction p4; p6 no significant interaction |
| S017 | Treatment×any intracranial hematoma interaction | Subgroup S014 | Subgroup S015 | — | — | .33 | p7 Table2 footnote d; p4 interaction method; p6 no significant interaction |
| S018 | Pneumonia per-protocol (population defined compliance/eligibility),10 d | 70.5% (no n/N main text) | 57.1% (no n/N main text) | 13.3% (2.4% to24.2%) | 1.23 (1.04–1.47) | .02 | [p6 continuation Per-Protocol and As-Treated Analyses](../../../jama_cooper_2018_oi_180132.pdf#page=6); explicitly unadjusted RR; eTable9 pointer; p8 discussion increased pneumonia |
| S019 | Pneumonia as-treated,10 d | 70.7% (no n/N main text) | 54.6% (no n/N main text) | 16.1% (5.7% to26.5%) | 1.29 (1.09–1.53) | .003 | p6 continuation; explicitly unadjusted RR; eTable11 pointer |

## Statistical relationships: methods and complete narrative claims without new numeric estimates

These entries preserve claims and specifications needed for checking. They are not inferred numeric results. Sidedness2-sided and significance threshold P<.05 apply to main-paper analyses, except historical context and sample-size P=.05 inputs. Secondary outcomes explicitly exploratory because no multiple-comparison adjustment. Main paper prints no numerical test statistics or standard errors for any relationship.

| ID | Exact source location | Complete method/result relationship; named missing numeric information |
|---|---|---|
| S020 | [p5 Per-Protocol and As-Treated Analyses](../../../jama_cooper_2018_oi_180132.pdf#page=5), [p6 continuation](../../../jama_cooper_2018_oi_180132.pdf#page=6) | No significant baseline differences in per-protocol/as-treated groups; favorable primary outcomes not different between either set of groups (eTables8–11). No primary effect estimates/CIs/P printed here. Pneumonia S018/S019 separately reported increased. |
| S021 | [p6 Per-Protocol continuation](../../../jama_cooper_2018_oi_180132.pdf#page=6) | Per-protocol/as-treated sensitivity analyses remain consistent (eFigures5/7). Cooling compliance sensitivity majority first72 h instead96 h per p4. No numeric main-paper estimates printed. |
| S022 | [p6 Post hoc Analyses](../../../jama_cooper_2018_oi_180132.pdf#page=6), [p7 continuation](../../../jama_cooper_2018_oi_180132.pdf#page=7) | Missing-primary-outcome scenarios show no significant H/C differences (eTable12); evaluable adequate-cooling-dose vs controls shows no significant favorable proportion differences (eTable13). Main paper gives no scenario counts/effect estimates/P values. |
| S023 | [p5 Additional Outcomes](../../../jama_cooper_2018_oi_180132.pdf#page=5) | No significant between-group differences for time to reach target (eTable7), mechanical ventilation days, ICU/hospital stays, mean6-mo GOS-E and unfavorable GOS-E among survivors (eTable5). Method p4: cooled time-to33°C relationship with favorable outcome via unadjusted χ² equal proportions; no time-category cutpoints or numeric results in main paper. |
| S024 | [p3 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=3) | Sample-size relationship N049:500 planned allows withdrawals/dropouts/consent/crossover and interim analyses;364 evaluable detects15-point improvement from50% with82% power,2-sided P=.05. Final510 after blinded withdrawal/loss review2017. No explicit numeric attrition allowance, interim alpha spending or formula in main paragraph; supplied plan source assigned to support mapper. |
| S025 | [p2 Trial Design and Oversight](../../../jama_cooper_2018_oi_180132.pdf#page=2), [p3 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=3) | Blinded planned interim conduct/progress/safety125/250 then safety300/350/400/450; sample size allowed interims. Main paper states no numeric stopping boundary or observed interim test result; Supplement1 referenced. |
| S026 | [p3 treatment and rewarming](../../../jama_cooper_2018_oi_180132.pdf#page=3) | Intervention definition N006/N007 connects primary contrast early prophylactic H vs controlled C: at least72 h at33°C (35°C with bleeding concerns), ICP-dependent up to7 d, target rewarming≤0.25°C/h and recurrence-triggered recooling. Life-threatening presumed bleeding permits35°C or C; both groups can receive other ICP treatment, C cooling wraps for pyrexia/refractory ICP. |
| S027 | [p3 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=3), [p4 continuation](../../../jama_cooper_2018_oi_180132.pdf#page=4) | All a-priori analyses according to randomized group excluding withdrawn consent unless otherwise indicated; no missing-data imputation. Binary primary/mortality/AE: unadjusted χ² equal proportions, frequency(%), RR/RD95%CI. Sensitivity hierarchic multivariable log-binomial adjusts extended IMPACT-TBI probability and randomization strata(location/site) as random effects; adjusted RR95%CI S002. Extended IMPACT factors age,motor GCS,pupils,CT Marshall,hypotension,hypoxia. p8 note says article updated2018-11-12 to correct mention of IMPACT-TBI in Methods. |
| S028 | [p4 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=4), [p5 result](../../../jama_cooper_2018_oi_180132.pdf#page=5) | Ordinal GOS-E logistic regression, proportional-odds assumption justified by score test, OR95%CI. Source does not print score-test statistic/P or exact numeric coding direction. Outcome scale/order is defined N048 and Figure3. Result S003 unadjusted H vs C. |
| S029 | [p4 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=4), [p5 result](../../../jama_cooper_2018_oi_180132.pdf#page=5) | Survival Cox proportional hazards censored6 mo/last contact, Kaplan–Meier and corresponding log-rank test; PH visually assessed using log-cumulative hazard plots. S006 HR/P in main narrative; no attribution of the printed P to a specific Cox coefficient vs log-rank computation beyond method wording. |
| S030 | [p4 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=4) | Prespecified evacuated hematoma/any significant intracranial hematoma effect heterogeneity by logistic treatment×subgroup interaction; S012–S017. Cooling-time-to33°C/favorable comparison unadjusted χ² equal proportions reported frequencies(%); no main numerical result. |
| S031 | [p4 analysis compliance](../../../jama_cooper_2018_oi_180132.pdf#page=4) | Prespecified per-protocol/as-treated both first exclude eligibility failures; cooling compliance≤35°C >48 h in96 h; noncompliers excluded(per-protocol) or transferred opposite group(as-treated). Sensitivity majority first72 h replaces96 h; post hoc missingness and adequate-dose analyses. Connects full protocol293(H132/C161) N004 and outcomes S018–S023. |
| S032 | [p4 Statistical Analysis end](../../../jama_cooper_2018_oi_180132.pdf#page=4) | SAS9.4;2-sided P<.05; no multiple-comparison adjustment, all secondary outcomes exploratory. No noninferiority/equivalence margin in the main report; trial primary question is effectiveness/improvement rather than a printed margin-based claim. |
| S033 | [p4 Results](../../../jama_cooper_2018_oi_180132.pdf#page=4), [p5 continuation](../../../jama_cooper_2018_oi_180132.pdf#page=5), [p6 Figure2](../../../jama_cooper_2018_oi_180132.pdf#page=6) | Core temperature described significantly lower in H first96 h; ICP similar during induction/maintenance/rewarming and therapy intensity similar (eFigure1/eTable4). Figure2 observed boxplots without imputation; main paper supplies no P/test/model for either trajectory claim, no numerical summary of mean daily ICP. p8 repeats no ICP/therapy-intensity effect. |
| S034 | [p1 conclusion](../../../jama_cooper_2018_oi_180132.pdf#page=1), [p2 Key Points](../../../jama_cooper_2018_oi_180132.pdf#page=2), [p7 Discussion](../../../jama_cooper_2018_oi_180132.pdf#page=7), [p8 Conclusions](../../../jama_cooper_2018_oi_180132.pdf#page=8) | H did not improve favorable6-mo neurologic outcomes; Key Points rates48.8%/49.1% nonsignificant. Discussion says no benefit in secondary outcomes including mortality, predefined subgroups/per-protocol/as-treated. Conclusion tied to S001 rather than an equivalence claim. |
| S035 | [p3 sample-size motivation](../../../jama_cooper_2018_oi_180132.pdf#page=3) | Historical RR1.46,CI1.12–1.92,P=.006 and<45-y subgroup50% improvement,P=.02 underpin15-point hypothesized effect. These supplied-source historical associations are kept distinct from POLAR estimates; neither model/test/sidedness of original historical studies reconstructed. |
| S036 | [p5 Patient Characteristics/Table1](../../../jama_cooper_2018_oi_180132.pdf#page=5), [p4 Results](../../../jama_cooper_2018_oi_180132.pdf#page=4) | Baseline groups described similar in all respects; Table1 all descriptive rows N015–N040, no comparative P values. Numeric quartile/median ordering remains literal (ISS C20.0,IQR20.5–35.0); no diagnostic calculation or judgment performed. |


### Mapping provenance: extraction/parts/plan_001.md

## Statistical relationships

| Provisional ID | Exact source position | Printed statistical definition and inputs | Matched result key / prospective context |
|---|---|---|---|
| S037 | [PDF p.14 §6.3](../../../joi180132supp1_prod.pdf#page=14), p.18 §8.1–8.2, p.69 §6.3 | Null no difference between assigned arms in proportions of favourable six-month neurological outcomes; alternative early sustained cooling increases favourable outcomes. Final Version9 repeats null/no-difference primary aim. | Primary superiority comparison; no noninferiority/equivalence margin specified. |
| S038 | [PDF p.27 §15.1](../../../joi180132supp1_prod.pdf#page=27) | Fixed-size full compliance/follow-up primary power: n364 (182 per arm),80% two-sided power,50% versus65%,15%ARI. N065 attrition/compliance/interim inflation. The primary section here does not separately print alpha; final testing level is in §15.3. | Sample-size reproduction inputs; do not fill in unprinted test family/formula. |
| S039 | [PDF p.28 secondary power](../../../joi180132supp1_prod.pdf#page=28) | Proportional-odds cumulative logit applied to eight-level GOSE category vector; ln(OR)=.62;182 evaluable per arm; one-sided linear-rank test of equal multinomial probabilities versus stochastic superiority;96% one-sided power; alpha=.05. | Secondary ordinal-GOSE power; no category-probability vector printed in this paragraph, so complete mechanical reproduction needs inputs elsewhere. |
| S040 | [PDF p.28 §15.2](../../../joi180132supp1_prod.pdf#page=28), p.25 §14.1 | Independent Monash statisticians ITT. Baseline/outcome variables Student t-test/chi-squared as appropriate. Patients with cooling withdrawn followed and analyzed on ITT; full protocol data also for those excluded at any stage. | Primary analyzed population and report method matching. Consent withdrawal data permission treated separately in p.25 §13.5. |
| S041 | [PDF p.28 §15.2](../../../joi180132supp1_prod.pdf#page=28) | Six-month favourable/unfavourable neurological dichotomy, QOL, favourable proportions in survivors, mortality proportions compared by stratified Mantel–Haenszel test and logistic regression adjusting for relevant covariates. No actual covariate names or missing-data algorithm in this paragraph. | Planned primary/binary outcome analysis, stratification and adjusted model key. |
| S042 | [PDF p.28 §15.2](../../../joi180132supp1_prod.pdf#page=28) | Time-to-event nonparametric Kaplan–Meier and semiparametric Cox proportional-hazards regression. | Survival methods; exact time-to-event endpoint/time origin not specified here, resolve elsewhere without inference. |
| S043 | [PDF p.28 §15.2](../../../joi180132supp1_prod.pdf#page=28), p.19 §9.2 | Adjusted proportional-odds cumulative logit for eight-level six-month GOSE; relevant covariates unspecified. Outcome wording probability equal/greater GOSE compared with lesser GOSE. | Ordinal GOSE secondary analysis, effect direction higher GOSE better. |
| S044 | [PDF p.28 §15.2](../../../joi180132supp1_prod.pdf#page=28), pp.15,19 secondary outcomes | Tertiles-of-risk sliding dichotomy: unfavourable/favourable six-month GOSE boundary differentiated by each subject's baseline prognostic risk. No risk model, covariates, numeric risk cutoffs or tertile GOSE boundaries supplied in this paragraph. | Sliding-dichotomy planned secondary result. |
| S045 | [PDF p.28 §15.3](../../../joi180132supp1_prod.pdf#page=28) | One interim safety analysis at50% enrolment, independent DSMC; Haybittle–Peto applied mortality between arms; normal approximation to discrete binomial difference in mortality proportions; standardized statistic absolute Z≥3. Assuming no early stop, no practical final adjustment; final conventional P<.05. | Prospective stopping/interim/multiplicity rule, original version. Later DSMC rules/amendments must be matched by version. |
| S046 | [PDF p.22 §12.17](../../../joi180132supp1_prod.pdf#page=22), §12.14 | Individual eligible patients randomized normothermia/hypothermia using closed envelopes and block randomisation. Stratified by ambulance, stated consequent stratification by centre because specific crews feed specific hospitals. Outcome assessed by blinded trained research staff; treatment staff not blinded because temperature apparent. | Randomisation/stratification and primary model assessment; ambulance is stratification unit, not asserted treatment cluster. |
| S047 | [PDF p.25 §14.1](../../../joi180132supp1_prod.pdf#page=25), pp.40,45 forms | Survivors interviewed at six months after randomisation by single trained blinded assessor using standardized telephone eight-grade GOSE and QOL; lost-to-follow-up recorded explicitly.5% assumed follow-up loss in sample size. No imputation or sensitivity procedure stated on these assigned original-protocol pages. | Missingness and outcome assessment; absence here is an extraction fact, not a diagnosed reporting issue. |


### Mapping provenance: extraction/parts/plan_002.md

## Statistical relationships

| ID | Source locations (PLAN) | Exact planned relationship / definition / inputs | Matching main-paper key / context |
|---|---|---|---|
| S048 | [p 72 §§8/9.1](../../../joi180132supp1_prod.pdf#page=72); p 81 §14.1; pp 90/105 | Primary proportion favourable GOSE 5–8 six months following injury; null no difference cooling versus standard normothermia; unfavourable GOSE 1–4 death/severe disability, favourable moderate/good recovery; p 81 follow-up six months post-randomisation | Primary favourable GOSE binary result; time anchors preserved |
| S049 | pp 72–73 §9.2 | Secondary six-month GOSE ordered probability equal/higher versus less by proportional odds; separately sliding dichotomy; QOL EQ5 D/SF12; favourable survivors; all-cause mortality hospital discharge/six months; bleeding/infection; economics | Secondary outcome list, including two ordinal/dichotomy approaches |
| S050 | p 73 §9.2 | Test interaction time to 33°C with dichotomised GOSE in cooling group; interaction cooling effect on six-month neurological function and surgically evacuated mass lesions | Prespecified timing and mass-lesion interactions |
| S051 | p 78 §12.17 | Individual eligible patient 1:1, concealed sequential opaque envelope/block randomisation; stratified four-level region × two-level enrolment setting | Randomisation strata/design |
| S052 | p 81 §14.1; p 84 §15.2 | ITT all randomly assigned except withdrawn consent for all trial data and patients not fulfilling inclusion criteria AND never receiving intervention; full protocol data collected even excluded; later cooling withdrawal still followed and ITT analysed | Full analysis set/exclusions and withdrawal |
| S053 | p 81 §14.1; pp 103–104 instrument | Central single trained blinded assessor telephone eight-level GOSE and EQ5 D/SF12 in six-month survivors/proxies; form distinguishes lost follow-up/alive unscorable; this shard does not specify imputation | Primary missing outcome and blinded ascertainment definitions; missing method must be sourced elsewhere |
| S054 | p 83 §15.1.2 | Fixed two independent arms 182 each, total 364; favourable .50→.65, RRI .30, ARI .15; 80% two-sided power; alpha not explicitly stated in this paragraph, default decision rule p 84; inflation 5% loss then 12% cooling noncompliance (8+2+2), then .7% interim, target 500 | Original sample size reproduction inputs; distinguish noncompliance from excluded outcomes |
| S055 | p 84 §15.1.3 | Original two interim Haybittle–Peto 3 SD at 125/250 for mortality/unfavourable; amended 11 planned interim analyses, ten joint outcome/mortality, penultimate 450 only 28-day mortality; 300–450 increments 50; East approximate χ², 366 evaluable power 82.3% versus 83%; final ±1.996 SD/P=.0459; inflation 4% versus .7% | Amended monitoring and final significance threshold; schedule statement literal |
| S056 | p 84 §15.1.3 | Unless specified otherwise two-sided hypothesis tests/95%CI; final significance level not adjusted for multiplicity, clearly defined primary outcome | Sidedness/CI/multiplicity |
| S057 | p 84 §15.1.4 | Proportional odds with 182 per arm one-sided power 96% at alpha .05 for reference improvement; declared potential power gain | Secondary power assumptions distinct from primary two-sided |
| S058 | p 84 §15.2 | Midpoint dichotomised GOSE binomial random variable, unadjusted RR95%CI plus RD95%CI and OR95%CI | Primary estimand/effect-measure identity |
| S059 | p 84 §15.2 | Ordinal GOSE proportional odds OR partial proportional odds model | Secondary ordinal model options |
| S060 | p 84 §15.2 | Binary hospital/six-month mortality/AE log-binomial for RR and identity-binomial for RD, both 95%CI | Binary secondary estimates |
| S061 | p 84 §15.2 | QOL/other continuous linear regression robust standard errors for potential non-normality/unequal variation | QOL model/variance |
| S062 | p 84 §15.2 | Favourable GOSE with mortality compared by SACE, effect among subpopulation that would survive under either arm | Survivor average causal effect; not crude survivor subset |
| S063 | p 84 §15.2 | Time-to-event KM/logrank, unadjusted and adjusted Cox HR95%CI | Mortality/survival estimates |
| S064 | p 85 §15.2 | Health-care payer cost per additional favourable GOSE5–8 at six months and per additional QALY; EQ5 D3 L utility six months; ICU/acute/postacute resource costs through six months | Secondary economic design |
| S065 | p 85 §15.2 | Prespecified subgroups (i) Marshall CT V, (ii) V or VI; covariate × treatment interaction in appropriate regression | Mass-lesion subgroup treatment interaction |
| S066 | p 85 §15.2 | Sensitivity primary/secondary adjust for prespecified baseline covariates AND any substantial between-arm imbalance; individual covariate names not listed here | Adjusted sensitivity model covariates; do not infer from absent names |
| S067 | p 84–85 §15.2 | Explore as-treated/per-protocol and average causal effect of cooling with noncompliance; PP=compliant assigned cooling versus all assigned control; AT=actual received treatment | PP/AT and noncompliance causal models |
| S068 | pp 85–86 §16 | Primary/total mortality/SAE DSMC monitoring; initial six months after 25%/50% recruitment, additional 300/350/400/450; primary and mortality 180 d except 450 28-day mortality; no futility early stopping plan | Interim monitoring outcome/windows and no-futility rule |
| S069 | p 108 §30.1.4 | AKI500=250/arm, 80% power two-sided P=.05; continuous difference .25 SD (SD approximately 24%→6%); binary 9%→3% six-point difference 80% approximate power | Nested renal power, peripheral to main primary unless report relies on it |
| S070 | pp 108–109 §§30.1.3/5/6/7 | AKI eGFR decline/creatinine rise worst up to 10 d; Risk/Injury/Failure classification; AKI-free days 10 d; distribution check/log transform; univariate tests, adjust baseline imbalances/known covariates; binary multiple logistic if data sufficient; log biomarker linear; time-event Cox/KM; Stata≥9; two-sided .05 | Nested renal endpoint/model |
| S071 | p 109 §30.2.4 | Renal biomarkers n 50, 80% power r=.4 continuous correlation two-sided .05; within-patient correlation unknown so increment in repeat-measurement power cannot exactly be calculated; day 1–3 change 25/arm 80% power .8 SD difference alpha .05 | Nested biomarker power |
| S072 | p 110 §30.2.7 | Anticipate lognormal biomarkers/log transform, adjust imbalances/known covariates repeated-measures ANOVA; treatment × time; associations biomarkers with renal function/RIFLE/survival logistic and ROC area | Nested renal biomarker repeated-measure/statistical definitions |
| S073 | pp 114–115 §31.1.3/4/5 | BEAR primary mean daily measured energy first 72 h, hypothesis≥20% lower; secondary first 7 d, treatment phases/fever>39°C; measured-versus-Schofield/fixed prescription ratios and delivered nutrition ratios; objective follows mechanical ventilation throughout | Nested energy endpoints and ratio denominators |
| S074 | p 118 §31.1.12 | BEAR cohort 478 rationale, mean 2000 cal SD400, difference 400 cal, 16/arm 80% two-sided .05; 20% noncompletion→20/arm; appropriate statistics normal/nonparametric | Nested energy power/analysis |
| S075 | p 119 §32.1.4/5; p 120 | Brain biomarker 40/arm total 80; pilot Spearman r=.4542, reference .45, >80% power two-sided .05 with 40 per group; biomarker concentrations versus six-month GOSE; normality/log transform, multiple linear regression, two-way ANOVA group over time, GraphPad Prism 5, P=.05 | Nested brain biomarker correlation/longitudinal analysis |
| S076 | pp 122–126 §33.1.5/14 | TEG primary POLAR versus non-POLAR coagulation; secondary same hypothermic patient blood tested normothermic; between-arm 48–72 h/120±12 h and same-sample 33/37°C comparisons; mixed linear model individual random effects, normality/log transform, changes from baseline first if asymmetric then nonlinear model if needed; SAS9.2, two-sided .05 | Nested coagulation repeated/paired data structure |
| S077 | pp 129–132 §34.1.5/11/12 | PK within-patient cooling 34–35 versus normothermia 36.5–38, 10 convenience patients, primary plasma concentration; secondary clearance/Vd/half-life; noncompartmental and NONMEM nonlinear mixed effects/PBPK, between/within-patient variability temperature, demographic/clinical/therapeutic influence | Nested PK model and paired contrast |
| S078 | [p 132 §34.1.12](../../../joi180132supp1_prod.pdf#page=132) | Prediscontinuation plasma concentration assumed steady-state Css mg/L; CLTOT L/h=total dose administered preceding 60 min (mg/h)/Css (mg/L); AUC0–∞ linear trapezoid plus printed 'product of the last measured plasma concentration multiplied by the terminal slope'; no slope sign/unit/definition supplied in this paragraph | Printed nested PK formula; preserve literal phrase without substituting external formula |
| S079 | p 132 §34.1.12 | Continuous mean(SD)/median[IQR], categorical counts%; within-patient paired Student t/Wilcoxon signed rank/McNemar if assumptions met; SPSS22 | Nested PK summaries/paired tests |


### Mapping provenance: extraction/parts/support_003.md

## Statistical relationships

Every indexed block includes all inferential rows in its page transcription, including row-level intervals, tests, model labels and footnotes. H versus N is the contrast unless X/Y masking is specified. Whole-table blocks preserve every relationship without selecting potential findings.

| ID | Exact source scope | Statistical definition, results and matching key |
|---|---|---|
| S080 | DOC-002 pp144,150–153 | V2→V3: N500 and0.7% interim inflation. Secondary proportional odds lnOR=.62, one-sided linear rank test,182/group,96% power, alpha=.05; sliding dichotomy added; all withdrawn patients followed. Two interim analyses125/256, P<.005, conventional3SD Haybittle-Peto; finalP<.05, no futility. These are amendment-history specifications. |
| S081 | DOC-002 pp163–170 | TEG compares treatment/control and within-patient33/37°C at48–72 h and120±12 h; normality assessment, log transformation where appropriate, mixed linear model with patient random effects, baseline changes then nonlinear modeling if necessary; SAS9.2; two-sidedP=.05. Ancillary plan. |
| S082 | DOC-002 pp174–175 | V8 modified ITT excludes withdrawn consent and ineligible patients never receiving intervention; extra DSMC monitoring300/350/400/450. Key: primary analysis population. |
| S083 | DOC-002 pp178–179 | V9 SAP finalizedMay2017; initial125/250 six-month mortality; later300/350/400 six-month favorable outcome/mortality and450 28-day mortality; no futility. CACE added for binary/continuous compliance; distinguishes causal assignment effect from received-treatment effect. |
| S084 | DOC-002 p180 | Target500→510 because consent withdrawals2.5% versus2% and loss7% versus5%; letter expressly states compensation for study power. |
| S085 | DOC-002 pp183–187 | 12June2018 update states additions before data lock and unblinded access. Clinically relevant dose>48 h at≤35°C within96 h; severe TBI/eligibility subset. PP excludes known noncompliant early deaths but retains compliant/unknown status; AT crosses known noncompliance and retains compliant/unknown early deaths. Depth analyses remain additional. Figures specify adjustment only for baseline extended IMPACT;13June correction adds48–96 h death boxes. |
| S086 | DOC-002 p188 | Charter: two125/250 interims, normal binomial difference, three-SD boundary|Z|≥3, approximatelyP<.001; primary dichotomized GOS-E or DSMC-selected mortality; no futility. Final|Z3|≥1.975, P=.048 versus1.960; final alpha=.05, no other multiplicity adjustment. |
| S087 | DOC-002 pp189–190 | 2015 masked interim: all11 row comparisons/P plus block curves. GOS-E deathP=.83, unfavorableP=.26, unfavorable survivalP=.28, mean scoreP=.23. No stopping recommendation printed in assigned pages. |
| S088 | DOC-002 pp191–192 | 2016 masked interim: all13 comparisons/P plus curves. GOS-E deathP=.88, favorable/unfavorableP=.53, unfavorable survivalP=.58, mean scoreP=.49,180-day mortalityP=.78. Explicit denominators321 outcome/341 survival. |
| S089 | DOC-002 pp193–194 | 2017 masked interim: all13 comparisons/P plus curves. GOS-E deathP=.98, favorable/unfavorableP=.68, unfavorable survivalP=.63, mean scoreP=.65,180-day mortalityP=.91. Explicit denominators364 outcome/390 survival. |
| S090 | DOC-003 p4 | eFigure1: least-square means and95%CI from longitudinal mixed linear modeling, patient random effect; temperature/ICP during36 h rewarming. All9 graphical positions, without exact labels. |
| S091 | DOC-003 p5 | eFigure2: unadjusted six-month mortality HR1.13(.76–1.69), P=.54; plot logrankP=.5349. Kaplan-Meier survival curves, censoring ticks and risk rows. |
| S092 | DOC-003 p6 | eTable2: locationP=.24; randomization-time comparisonsP=.98/.58. Descriptive cooling-time quantiles and counts retained separately. |
| S093 | DOC-003 p8 | eTable4: all process comparisons and P values below; ICP/CPP index definitions, saline standardized3%, mannitol20%, first10-day versus entire-ICU durations. |
| S094 | DOC-003 p9 | eTable5: all5 comparisons P=.06,.33,.74,.86,.71; GOS-E mean and unfavorable scores among survivors are different outcomes. |
| S095 | DOC-003 p10 | eTable6: all cardiac/infection/bleeding/ICP comparisons P<.0001,.66,1.00,.88,.40,.29,.53,.43,.70,.67; hypothermia-only induction/maintenance hypotension has no N contrast. |
| S096 | DOC-003 p11 | eTable7: favorable proportions/95%CI for four time-to33°C categories; omnibusP=.09, not category-specificP. |
| S097 | DOC-003 pp12–14 | PP definition>48 h at≤35°C within96 h and severe TBI/eligibility; early-death compliance rules. All baseline tests eTable8 retained. PrimaryRR1.02(.79–1.32), P=.86; printed severity-adjusted RR 'for favorable outcome'1.04(.65–1.69), P=.86. Outcome124/151 versus baseline132/161 versus death132/160. |
| S098 | DOC-003 p14 | PP hospital deathRR1.10(.71–1.71),P=.66; six-month death1.11(.72–1.70),P=.65; pneumonia1.23(1.04–1.47),P=.02; bacteremia2.13(.92–4.93),P=.07; other infection1.02(.63–1.64),P=.95; intracranial bleeding1.09(.68–1.76),P=.71; extracranial bleeding.41(.08–1.98),P=.25. All paired counts below. |
| S099 | DOC-003 p14 | PP hematoma yesRR.79(.44–1.42),P=.43; no1.10(.83–1.45),P=.51; interactionP=.31. Mass lesion yes.78(.44–1.40),P=.40; no1.10(.83–1.45),P=.51; interactionP=.29. All counts below. |
| S100 | DOC-003 p15 | PP96 h temperature curves,17 positions with interval bars; blue H/orange N. This page gives no additional model or confidence-level caption for bars. |
| S101 | DOC-003 p16 | PP sensitivity uses72 h AUC below35°C, linear trapezoidal method ignoring missing observations, majority-cooling criterion; kappa.93(.90–.97). Favorable55/120 versus69/151; unadjustedRR1.00(.77–1.30),P=.98. |
| S102 | DOC-003 pp17–19 | AT definition>48 h at≤35°C within96 h; known noncompliance crosses groups, early compliant/unknown status retained. All baseline tests eTable10 retained. PrimaryRR1.06(.83–1.35),P=.65; printed severity-adjusted RR 'for unfavorable outcome'1.11(.70–1.76),P=.65. Outcome125/184, baseline133/196, death133/195. |
| S103 | DOC-003 p19 | AT hospital deathRR1.16(.76–1.77),P=.50; six-month death1.14(.75–1.72),P=.55; pneumonia1.29(1.09–1.53),P=.003; bacteremia1.88(.88–4.00),P=.10; other infection1.16(.73–1.85),P=.53; intracranial bleeding.98(.63–1.53),P=.94; extracranial bleeding.29(.07–1.32),P=.09. All counts below. |
| S104 | DOC-003 p19 | AT hematoma yesRR.81(.46–1.45),P=.48; no1.14(.87–1.48),P=.34; interactionP=.27. Mass lesion yes.80(.45–1.43),P=.45; no1.14(.87–1.48),P=.34; interactionP=.25. All counts below. |
| S105 | DOC-003 p20 | AT72 h AUC/trapezoidal majority-cooling rule assigns treatment actually received, including rescue N→H. Favorable56/121 versus85/188; unadjustedRR1.02(.80–1.31),P=.85. |
| S106 | DOC-003 p21 | Missingness worst case: H missing bad/N missing good.117/260,45.0%(38.8–51.2) versus125/240,52.1%(45.6–58.5); RR.86(.72–1.04),RD−7.1(−15.8–1.7),P=.11. Unadjusted chi-square test for equal proportions. |
| S107 | DOC-003 p21 | Missingness best case: H missing good/N missing bad.137/260,52.7%(46.5–58.9) versus111/240,46.3%(39.8–52.7); RR1.14(.95–1.36),RD6.4(−2.3–15.2),P=.15. Unadjusted chi-square test for equal proportions. |
| S108 | DOC-003 p21 | Multiple imputation: MAR conditional on all available baseline/hospital-discharge data; predictive mean matching,11 datasets. CMH test for stratified proportions, RR and RD with Miettinen-Nurminen score confidence limits for stratum RD. H133,51.1%(45.1–57.2); N121,50.4%(44.1–56.7); RR1.00(.95–1.06),RD.7(−8.0–9.5),P=.88. Exact printed method and estimate identity retained. |
| S109 | DOC-003 p22 | Post hoc adequate cooling H124 versus all N226: favorableOR.91(.59–1.41),P=.68; adjusted timeOR.95(.55–[printed275]1.64),P=.84. Hierarchical logistic regression, random site/setting effects. Baseline comparisons use chi-square, t or Wilcoxon tests. Mean randomization1.73(.78)/2.00(1.04) h,P=.01; narrative16 min difference. |
| S110 | DOC-003 p23 | eTable13: all baseline tests/footnotes; median randomization1.6(1.0–2.5)/2.1(1.1–2.8) h,P=.02, distinct from mean-basedP=.01. Temperature available75/136. No respecification of main primary trial model. |


## Statistical pass completion

Pass 1: all 110 canonical relationships have explicit PASS_1_COMPLETE records in checkers/statistical_pass_1.md, fresh runtime /root/statistics_1. Pass 2 subsequently completed after stable ledger, screening and exact-source recheck. Per-ID completion is preserved in the checker artifact; no ID is omitted.

Pass 2: all110 relationships have explicit PASS_2_COMPLETE records, fresh runtime /root/statistics_2, distinct from /root/statistics_1. No new qualifying finding; no pass-2 inclusion-screen wave required. Both completion tables are copied below without removing any row.


## Per-relationship pass-1 completion

| S ID | Pass 1 status | Check result and rationale |
|---|---|---|
| S001 | PASS_1_COMPLETE | Primary counts, unadjusted RR/RD, null-containing CI and chi-square P reconcile; abstract sign screened. |
| S002 | PASS_1_COMPLETE | Adjusted RR interval ordered/containing, direction/test coherent; model-versus-crude comparison excluded. |
| S003 | PASS_1_COMPLETE | Ordinal OR interval contains estimate/null; rounding and unprinted coefficient test prevent unique inversion. |
| S004 | PASS_1_COMPLETE | Hospital mortality counts/RR/RD/P reconcile; one unavailable N hospital outcome is distinct from six-month set. |
| S005 | PASS_1_COMPLETE | Six-month mortality RR 1.14577/P .453996 reconcile; death denominator matched to Figure 1. |
| S006 | PASS_1_COMPLETE | HR/CI/direction coherent; survival and logrank matched without forcing coefficient-test equality. |
| S007 | PASS_1_COMPLETE | Pneumonia risks/RR 1.07317/P .401146 reconcile. |
| S008 | PASS_1_COMPLETE | Bacteremia risks/RR 1.46154/P .285058 reconcile. |
| S009 | PASS_1_COMPLETE | Other infection RR .874494/P .531864 reconcile. |
| S010 | PASS_1_COMPLETE | Intracranial unadjusted RR/P blocks do not reconcile; F-ST1-001 consolidated bleeding pattern. |
| S011 | PASS_1_COMPLETE | Extracranial unadjusted RR/P blocks do not reconcile; same F-ST1-001. |
| S012 | PASS_1_COMPLETE | Hematoma-yes counts/RR .839506/P .443828 reconcile. |
| S013 | PASS_1_COMPLETE | Hematoma-no counts/RR 1.02696/P .793606 reconcile; strata partition primary set. |
| S014 | PASS_1_COMPLETE | Mass-lesion-yes RR .808489/P .351126 reconcile. |
| S015 | PASS_1_COMPLETE | Mass-lesion-no RR 1.03748/P .716224 reconcile; partition totals match. |
| S016 | PASS_1_COMPLETE | InteractionP .43 corresponds logistic subgroup interaction, not either within-subgroup P. |
| S017 | PASS_1_COMPLETE | InteractionP .33 corresponds the separate lesion interaction; nonsignificant claim coherent. |
| S018 | PASS_1_COMPLETE | PP pneumonia counts in eTable 9 give RR 1.23295/P .018773 and positive RD. |
| S019 | PASS_1_COMPLETE | AT pneumonia eTable 11 gives RR 1.29464/P .003317; CI/direction coherent. |
| S020 | PASS_1_COMPLETE | All PP/AT baseline tests/outcome rows read; primary nonsignificant statements match eTables 9/11. |
| S021 | PASS_1_COMPLETE | PP/AT 72-hour sensitivity primary estimates remain nonsignificant; outcome and compliance subsets matched. |
| S022 | PASS_1_COMPLETE | Worst/best/MI and adequate-cooling statements matched; primary randomized contrast remains separate. |
| S023 | PASS_1_COMPLETE | Other-outcome tests read; time-to 33°C equal-proportions relationship raises F-ST1-002. |
| S024 | PASS_1_COMPLETE | Power/target inputs compared with final plan; formula-specific approximations screened as conditional. |
| S025 | PASS_1_COMPLETE | Interim schedule matched to dated amendments; no supplied stopping decision conflicts. |
| S026 | PASS_1_COMPLETE | Intervention durations/targets and operative rewarming flow matched; context resolves summarized anchors/ceiling. |
| S027 | PASS_1_COMPLETE | Randomized-group/no-imputation and hierarchical adjusted model read; bleeding unadjusted specification supports F-ST1-001. |
| S028 | PASS_1_COMPLETE | Ordinal model/score-check description coherent; exact score/coding absence recorded. |
| S029 | PASS_1_COMPLETE | Cox/KM/logrank, censoring and visual PH check distinguished; no guessed covariance/test. |
| S030 | PASS_1_COMPLETE | Logistic interactions coherent; stated unadjusted cooling-time comparison supports F-ST1-002. |
| S031 | PASS_1_COMPLETE | Eligibility, compliance and early-death rules matched to SAP update/results populations. |
| S032 | PASS_1_COMPLETE | Two-sided .05/unadjusted multiplicity/exploratory status explicit; no equivalence margin assumed. |
| S033 | PASS_1_COMPLETE | Temperature/ICP graphics and process tests read; no exact trajectory test invented from boxplots. |
| S034 | PASS_1_COMPLETE | No-improvement conclusion matched to nonsignificant primary estimate, not read as equivalence. |
| S035 | PASS_1_COMPLETE | Historical RR/CI/P kept separate; historical tests not reconstructed externally. |
| S036 | PASS_1_COMPLETE | Main baseline table contains no inferential P; peripheral descriptive observations excluded. |
| S037 | PASS_1_COMPLETE | Superiority/null/no-difference aim consistent with randomized primary comparison. |
| S038 | PASS_1_COMPLETE | Original power inputs/attrition/noncompliance read; unprinted planning formula prevents unique reproduction. |
| S039 | PASS_1_COMPLETE | One-sided ordinal power recognized; category probabilities unavailable for exact calculation. |
| S040 | PASS_1_COMPLETE | Original ITT/withdrawal follow-up matched to revised final population definitions. |
| S041 | PASS_1_COMPLETE | Original stratified/logistic primary methods superseded by dated final plan context. |
| S042 | PASS_1_COMPLETE | Original KM/Cox specifications coherent with final/report survival methods. |
| S043 | PASS_1_COMPLETE | Original adjusted ordinal method compared with final unadjusted ordinal specification; versions distinguished. |
| S044 | PASS_1_COMPLETE | Sliding dichotomy definition read; report deferral and non-key-secondary status retained. |
| S045 | PASS_1_COMPLETE | Original single interim 3 SD rule matched chronologically to later schedule; approximate P shorthand screened. |
| S046 | PASS_1_COMPLETE | Individual randomization and ambulance/centre strata do not imply cluster-randomized treatment. |
| S047 | PASS_1_COMPLETE | Original six-month ascertainment/missingness forms read; no missing-data method inferred from absence. |
| S048 | PASS_1_COMPLETE | Final favorableGOSE 5–8 endpoint/null/time anchor matches report; hours-scale anchor wording resolved. |
| S049 | PASS_1_COMPLETE | All final secondary endpoint models/distinct ordinal/sliding outcomes read; key status not invented. |
| S050 | PASS_1_COMPLETE | Time and lesion interactions matched to report statistical method; timing result separately examined. |
| S051 | PASS_1_COMPLETE | Individual 1:1/strata/block design supports independent-arm and sensitivity descriptions. |
| S052 | PASS_1_COMPLETE | Final full-analysis exceptions and later cooling withdrawal follow-up distinguished. |
| S053 | PASS_1_COMPLETE | Blinded assessor/GOSE and lost/unscorable form definitions read; no imputation inference. |
| S054 | PASS_1_COMPLETE |364/384/496/500 power/inflation sequence read; formula uncertainty and dilution alternative recorded. |
| S055 | PASS_1_COMPLETE | East 82.3%, amended monitoring and .0459 final rule read; visit/outcome count and robust decisions screened. |
| S056 | PASS_1_COMPLETE | Two-sided 95%CI and primary multiplicity statement coherent; report exploratory distinction retained. |
| S057 | PASS_1_COMPLETE | One-sided 96% ordinal planning example separate from two-sided reported tests; missing category vector named. |
| S058 | PASS_1_COMPLETE | Final primary binomial/RR/RD/OR specification matched; report primary RR/RD reconcile. |
| S059 | PASS_1_COMPLETE | Proportional/partial-proportional model options consistent with report's justified proportional assumption. |
| S060 | PASS_1_COMPLETE | Binary log/identity-binomial estimates compatible with report's RR/RD labeling outside bleeding issue. |
| S061 | PASS_1_COMPLETE | Robust continuous linear-regression plan read; no supplied main QOL model result depends on absent detail. |
| S062 | PASS_1_COMPLETE | SACE explicitly distinct from crude favorable-survivor percentages; no estimand equivalence assumed. |
| S063 | PASS_1_COMPLETE | KM/logrank/unadjusted and adjusted Cox plan read; reported HR direction/CI coherent. |
| S064 | PASS_1_COMPLETE | Economic endpoint/QALY/cost windows read; deferred non-key result not registered. |
| S065 | PASS_1_COMPLETE | Prespecified lesion strata and treatment interaction matched to main Table 2; no statistical conflict. |
| S066 | PASS_1_COMPLETE | Adjustment intention read with report's named IMPACT/strata model; absent individual covariates not invented. |
| S067 | PASS_1_COMPLETE | PP/AT/compliance causal estimands distinguished; dated dose update resolves operational subsets. |
| S068 | PASS_1_COMPLETE | Monitoring primary/mortality windows/no-futility rule matched;11 tests versus 6 visits resolved. |
| S069 | PASS_1_COMPLETE | AKI approximate continuous/binary power checked diagnostically; no main result reliance. |
| S070 | PASS_1_COMPLETE | AKI endpoints, transforms and model types read; no supplied paired/independent contradiction relied on by report. |
| S071 | PASS_1_COMPLETE | Renal correlation/change power inputs coherent approximately; unknown repeated correlation expressly disclosed. |
| S072 | PASS_1_COMPLETE | Renal repeated-measure interaction/logistic/ROC specifications read; ancillary/nonreported scope screened. |
| S073 | PASS_1_COMPLETE | BEAR 72-hour/7-day/treatment-period endpoints and ratio denominators distinguished. |
| S074 | PASS_1_COMPLETE | Energy 400/400 effect and 16→20 attrition power approximately coherent; no reported dependent value. |
| S075 | PASS_1_COMPLETE | Brain biomarker correlation 40/group and repeated-group analysis read; exact rank power unprinted. |
| S076 | PASS_1_COMPLETE | TEG between/within-patient contrast consistent with patient random-effects model. |
| S077 | PASS_1_COMPLETE | PK 10 patient convenience/paired-temperature and mixed model defined coherently. |
| S078 | PASS_1_COMPLETE | Clearance units reconcile; terminal-slope AUC phrase preserved with missing definition, ancillary scope excluded. |
| S079 | PASS_1_COMPLETE | PK paired t/Wilcoxon/McNemar choices conditional on stated within-patient structure/assumptions. |
| S080 | PASS_1_COMPLETE | Scanned V 2→V 3 sample/interim/ordinal changes visually checked; versions and explicit 3 SD rule retained. |
| S081 | PASS_1_COMPLETE | Full TEG data structure/model/amendment read; paired/repeated structure accounted for. |
| S082 | PASS_1_COMPLETE | V 8 modified ITT and extra safety schedule explain later final-plan specifications. |
| S083 | PASS_1_COMPLETE | V 9 May 2017 SAP context, monitoring outcome windows and CACE addition read; no raw survivor equivalence assumed. |
| S084 | PASS_1_COMPLETE |500→510 blinded attrition rationale read; no fully specified revised power formula to contradict. |
| S085 | PASS_1_COMPLETE | SAP dose/eligibility/early-death rules and IMPACT-only adjustment templates visually checked against results. |
| S086 | PASS_1_COMPLETE | Charter 3 SD/.048 final and no-futility rules read; approximateP shorthand/context exclusions recorded. |
| S087 | PASS_1_COMPLETE | All 11 masked 2015 tests/category and block tables checked; no stopping-boundary crossing printed. |
| S088 | PASS_1_COMPLETE | All 13 masked 2016 tests/category and survival denominators checked; no stopping decision conflict. |
| S089 | PASS_1_COMPLETE | All 13 masked 2017 tests/category/survival denominators checked; no unprinted recommendation inferred. |
| S090 | PASS_1_COMPLETE | All 9 rewarming positions visually checked for interval containment/order; patient random effects/95%CI explicit. |
| S091 | PASS_1_COMPLETE | KM curve/HR/logrank/null direction coherent; caption terminology and test-attribution exclusions recorded. |
| S092 | PASS_1_COMPLETE | All location/time comparisons read; exact median-based P unavailable without distributions. |
| S093 | PASS_1_COMPLETE | Every process comparison/interval/definition checked; sparse/continuous test reconstruction limited, wrapped P screened. |
| S094 | PASS_1_COMPLETE | All 5 outcomes checked; mean 4.2 withP .86 permits rounded differences; survivor denominator coherent. |
| S095 | PASS_1_COMPLETE | All adverse-event tests checked; supplement bleeding P assignments support F-ST1-001. |
| S096 | PASS_1_COMPLETE | All 4 time-bin proportions/CIs/P checked; stated equal-proportions mapping raises F-ST1-002. |
| S097 | PASS_1_COMPLETE | All PP baseline/primary/adjusted rows read; unadjusted primary RR 1.02361/P .858283 reconcile. |
| S098 | PASS_1_COMPLETE | All 7 PPsecondary outcome count/RR/CI/P rows checked; pneumonia significant/exploratory and others coherent. |
| S099 | PASS_1_COMPLETE | All 4 PPsubgroup estimates and 2 interactionP values checked; partitions/directions/intervals coherent. |
| S100 | PASS_1_COMPLETE | All 17 PPtemperature positions visually checked; bars contain plotted centers; unprinted level/model not assumed. |
| S101 | PASS_1_COMPLETE | PP 72-hour sensitivity counts/RR 1.00302/P .981933/kappaCI checked; AUC cutoff absent, not inferred. |
| S102 | PASS_1_COMPLETE | All AT baseline/primary/adjusted rows checked; primaryRR 1.05912/P .648119 coherent; explicit unfavorable adjusted label retained. |
| S103 | PASS_1_COMPLETE | All 7 ATsecondary count/RR/CI/P rows checked; pneumoniaRR 1.29464/P .003317 coherent. |
| S104 | PASS_1_COMPLETE | All 4 ATsubgroup estimates/2 interactionP values checked; no null/claim/direction conflict. |
| S105 | PASS_1_COMPLETE | AT 72-hour sensitivityRR 1.02363/P .854003 reconcile; no inferred AUC threshold or imputation. |
| S106 | PASS_1_COMPLETE | Worst-casecounts/RR .864/RD−7.08333/P .113325 reconcile and remain nonsignificant. |
| S107 | PASS_1_COMPLETE | Best-caseRR 1.13929/RD 6.44231/P .150027 reconcile; null-containing intervals ordered. |
| S108 | PASS_1_COMPLETE | MI row, MAR/PMM/11 datasets/CMH/score method read; no stratification/pooling variance inferred; model comparison excluded. |
| S109 | PASS_1_COMPLETE | Adequate-dose OR/adjusted OR contain null;16-minute mean-time contrast coherent;275 token excluded. |
| S110 | PASS_1_COMPLETE | All post hoc baseline tests/footnotes checked; mean versus median P distinguished and peripheral values screened. |

## Per-relationship pass-2 completion

| S ID | Pass 2 status | Check result and recheck implications |
|---|---|---|
| S001 | PASS_2_COMPLETE | Exact primary counts yield RR .992568, RD −.365044 and diagnostic P .937204; null-containing intervals and nonsignificant narrative agree. Abstract sign remains typography. |
| S002 | PASS_2_COMPLETE | Adjusted RR .98 lies within .87–1.11, includes the null and matches nonsignificant interpretation; no crude/model identity imposed. |
| S003 | PASS_2_COMPLETE | Ordinal OR .97 lies within .71–1.34; direction and nonsignificance agree. Actual coefficient test, covariance and coding are not reconstructed from convention. |
| S004 | PASS_2_COMPLETE | Hospital RR 1.111628/P .568097 match printed 1.11/.57; 239 N hospital outcomes are kept separate from the primary outcome set. |
| S005 | PASS_2_COMPLETE | Mortality 54/256 versus 44/239 yields RR 1.145774/P .453996; death denominators match the stated six-month mortality set. |
| S006 | PASS_2_COMPLETE | HR 1.13 within .76–1.69 has mortality direction consistent with survival curves; log-rank and coefficient tests are not forced to coincide. |
| S007 | PASS_2_COMPLETE | Pneumonia RR 1.073171/P .401146 agree with table/abstract; CI contains estimate and null. |
| S008 | PASS_2_COMPLETE | Bacteremia RR 1.461538/P .285058 agree within precision; ordered null-containing CI and direction coherent. |
| S009 | PASS_2_COMPLETE | Other infection RR .874494/P .531864 agree; negative risk difference and RR below one describe the same direction. |
| S010 | PASS_2_COMPLETE | Source/recheck independently retain C004 intracranial count-to-RR and cross-source P mismatch; no duplicate finding or authorized reassignment. |
| S011 | PASS_2_COMPLETE | Source/recheck retain paired C004 extracranial mismatch as the same pattern; no additional candidate or assumed CI estimator. |
| S012 | PASS_2_COMPLETE | Hematoma-yes RR .839506/P .443828 reconcile; proportions, RD and nonsignificant interval direction agree. |
| S013 | PASS_2_COMPLETE | Hematoma-no RR 1.026957/P .793606 reconcile; 66+174=240 and 68+158=226 partition the primary population. |
| S014 | PASS_2_COMPLETE | Mass-lesion-yes RR .808489/P .351126 reconcile; negative RD and null-containing ratio interval coherent. |
| S015 | PASS_2_COMPLETE | Mass-lesion-no RR 1.037483/P .716225 reconcile; 69+171=240 and 71+155=226 partition primary denominators. |
| S016 | PASS_2_COMPLETE | Interaction .43 is assigned to treatment-by-evacuated-hematoma model, not a within-subgroup test; nonsignificant interaction claim agrees. |
| S017 | PASS_2_COMPLETE | Interaction .33 belongs to the distinct mass-lesion comparison; no inference from the difference between subgroup P values. |
| S018 | PASS_2_COMPLETE | PP pneumonia 93/132 versus 92/161 yields RR 1.232955/P .018773; positive RD and excluding-null CI support the stated exploratory increase. |
| S019 | PASS_2_COMPLETE | AT pneumonia 94/133 versus 107/196 yields RR 1.294638/P .003317; main and supplementary result attribution agree. |
| S020 | PASS_2_COMPLETE | All PP/AT baseline and primary rows revisited; no significant primary or baseline difference claim conflicts with the supplied tests. Modeled rows remain distinct. |
| S021 | PASS_2_COMPLETE | PP/AT 72-hour sensitivity results matched to their own populations; no significant primary difference is reproduced, without inventing a numeric AUC cutoff. |
| S022 | PASS_2_COMPLETE | Worst/best/imputed missingness and adequate-dose post hoc statements match the supplied rows; none replaces the primary randomized contrast. |
| S023 | PASS_2_COMPLETE | All other-outcome narrative tests matched; C003 timing attribution retains bounded df/category/implementation limitations and no new finding. |
| S024 | PASS_2_COMPLETE | Main 364 evaluable/82% and final plan East 366/82.3% remain approximate context, not a uniquely specified contradictory planning computation. |
| S025 | PASS_2_COMPLETE | Amended safety schedule matched by version; no supplied stopping recommendation conflicts with a stated threshold. |
| S026 | PASS_2_COMPLETE | C001 report-versus-plan duration ambiguity is retained; cooling anchor/rate summaries resolve under detailed instructions. Actual received duration is not inferred. |
| S027 | PASS_2_COMPLETE | Randomized-group/no-imputation main methods and adjusted random-strata model read; explicit unadjusted adverse-event analysis sustains C004 identity check. |
| S028 | PASS_2_COMPLETE | Ordinal model and score-check statement are internally coherent; absent score statistic, coding and coefficients are named limitations, not substitute findings. |
| S029 | PASS_2_COMPLETE | Cox censoring, KM/log-rank and visual PH assessment distinguished; no missing variance/test output guessed. |
| S030 | PASS_2_COMPLETE | Logistic subgroup interactions agree with attributed tests; cooling-time chi-square family supports only the bounded C003 method/result question. |
| S031 | PASS_2_COMPLETE | Clinical eligibility, >48-hour/≤35°C compliance and early-death rules match the supplied SAP update and separate PP/AT denominators. |
| S032 | PASS_2_COMPLETE | Two-sided .05 and unadjusted exploratory secondary status explicitly retained; screened F-XS-003 not re-emitted, no equivalence rule inferred. |
| S033 | PASS_2_COMPLETE | Temperature/ICP trajectories and process tests revisited; repeated measurements and boxplots do not supply an exact unprinted trajectory test. |
| S034 | PASS_2_COMPLETE | No-improvement conclusion matches nonsignificant primary superiority result; neither equivalence nor a margin-based claim is supplied. |
| S035 | PASS_2_COMPLETE | Historical RR/CI/P remain rationale rather than POLAR results; unprinted historical models/tests are not reconstructed externally. |
| S036 | PASS_2_COMPLETE | Numeric lane C002 within-cell quantile ordering incorporated and visually confirmed; other baseline comparisons remain peripheral and no primary denominator changes. |
| S037 | PASS_2_COMPLETE | Prospective no-difference null/increased-favorable alternative matches the reported superiority question; no noninferiority/equivalence margin is stated. |
| S038 | PASS_2_COMPLETE | Original 182 per arm/80% and .50→.65 inputs revisited; continuity/formula and dilution assumptions are not inferred as the original implementation. |
| S039 | PASS_2_COMPLETE | One-sided ordinal power is explicitly planning-only; category probabilities and rank-test implementation missing for exact reproduction. |
| S040 | PASS_2_COMPLETE | Withdrawal of cooling preserves follow-up; consent-data withdrawal and later modified-ITT exceptions distinguished from treatment cessation. |
| S041 | PASS_2_COMPLETE | Original stratified/logistic analysis language is versioned; final primary unadjusted binomial specification supplies later operative context. |
| S042 | PASS_2_COMPLETE | Original KM/Cox time-to-event specifications are coherent with final/report survival descriptions; no time origin invented. |
| S043 | PASS_2_COMPLETE | Original adjusted ordinal model and later proportional/partial-proportional options matched by version; report supplies a coherent ordinal model. |
| S044 | PASS_2_COMPLETE | Risk-dependent sliding dichotomy distinguished from fixed midpoint; unprinted risk cutoffs and deferred non-key result do not create a new issue. |
| S045 | PASS_2_COMPLETE | Original single interim mortality/three-SD rule remains historical; later dated monitoring expansion prevents conflicting-version inference. |
| S046 | PASS_2_COMPLETE | Individual allocation with ambulance/site stratification is distinguished from cluster treatment assignment; adjusted random-strata description does not contradict design. |
| S047 | PASS_2_COMPLETE | Original blinded six-month assessment/lost-follow-up definitions read; missingness handling is resolved from report/post hoc methods, not guessed from this paragraph. |
| S048 | PASS_2_COMPLETE | Final favorable GOS-E 5–8/no-difference primary endpoint matches report; nearby injury/randomization time anchors do not identify competing six-month results. |
| S049 | PASS_2_COMPLETE | Final ordinal/sliding/QOL/survivor/mortality/AE/economic definitions distinguished; no key-secondary status inferred for deferred analyses. |
| S050 | PASS_2_COMPLETE | Prospective cooling-time and mass-lesion analyses matched; no separate new planned-method finding about C003 category attribution. |
| S051 | PASS_2_COMPLETE | Individual 1:1 allocation/block/region-setting strata support independent-arm count checks; no unprinted variance or clustering estimator inferred. |
| S052 | PASS_2_COMPLETE | Full-analysis consent/ineligible-never-treated exceptions and treatment-withdrawal follow-up distinguished; additional exclusion counts remain unavailable. |
| S053 | PASS_2_COMPLETE | Blinded GOSE assessment and lost/unscorable forms are compatible with observed primary set; no raw outcome categories assigned to missing cases. |
| S054 | PASS_2_COMPLETE | 364→384→496→500 inputs revisited; 5% loss and noncompliance dilution are distinct, while exact planning/inflation implementation remains unavailable. |
| S055 | PASS_2_COMPLETE | East power/amended monitoring/.0459 final boundary read directly; eleven outcome tests versus six visits resolved, F-XS-003 screen preserved. |
| S056 | PASS_2_COMPLETE | Two-sided hypothesis/95% CI and primary multiplicity statement coherent with report's exploratory-secondary treatment; exact look-level implementation unavailable. |
| S057 | PASS_2_COMPLETE | One-sided 96% ordinal planning example distinguished from report's two-sided inference; absent multinomial category vector prevents exact reproduction. |
| S058 | PASS_2_COMPLETE | Final primary binomial RR/RD/OR definitions read; reported primary RR/RD reconcile, and absence of an extra OR does not identify a different underlying primary comparison. |
| S059 | PASS_2_COMPLETE | Proportional/partial-proportional options and report's score-based proportional choice are internally coherent; no preferred model proposed. |
| S060 | PASS_2_COMPLETE | Log/identity-binomial secondary estimates preserve RR/RD identity; main explicit unadjusted rows reconcile except existing C004 attribution. |
| S061 | PASS_2_COMPLETE | Robust continuous regression plan accounts for stated variation concerns; no supplied QOL result depends on an unreported contradictory method. |
| S062 | PASS_2_COMPLETE | SACE estimand distinguishes survival under both assignments from crude observed-survivor percentages; no equivalence asserted between them. |
| S063 | PASS_2_COMPLETE | KM/log-rank and unadjusted/adjusted Cox plan matched to actual HR and curve; missing coefficient-test attribution retained. |
| S064 | PASS_2_COMPLETE | Economic favorable-outcome/QALY cost windows read; deferred non-key economic result remains outside eligible discrepancy comparisons. |
| S065 | PASS_2_COMPLETE | Prespecified Marshall V and V/VI effect-modification terms match report subgroup partitions and interaction attribution. |
| S066 | PASS_2_COMPLETE | Adjustment plan and report's named IMPACT/random-strata model matched; unlisted individual plan covariates are not inferred as omitted contradictory steps. |
| S067 | PASS_2_COMPLETE | PP, AT and noncompliance causal effects remain distinct estimands; dated eligibility/dose update explains operational subset rules. |
| S068 | PASS_2_COMPLETE | Primary/mortality monitoring windows and no-futility rule matched; supplied interim results are distant from stopping boundaries. |
| S069 | PASS_2_COMPLETE | AKI .25-SD/six-point power assumptions remain approximate ancillary calculations; no reported main/key result relies on a competing specification. |
| S070 | PASS_2_COMPLETE | AKI transforms/endpoints/logistic/linear/survival methods matched to their stated data structures; no contradictory main-result step identified. |
| S071 | PASS_2_COMPLETE | Correlation/change planning inputs read; repeated-measure covariance is explicitly unknown and not filled by assumption. |
| S072 | PASS_2_COMPLETE | Renal treatment-by-time/log-transform/logistic/ROC definitions remain coherent ancillary prospective methods with no supplied dependent key result. |
| S073 | PASS_2_COMPLETE | BEAR 72-hour, seven-day and phase-specific quantities and prediction/delivery denominators distinguished; no shared-value attribution conflict. |
| S074 | PASS_2_COMPLETE | Energy effect 400/400, approximately 16 per arm and 20% noncompletion to 20 per arm reconcile approximately; no exact unprinted planning test inferred. |
| S075 | PASS_2_COMPLETE | Brain biomarker .45 correlation/40 per group and longitudinal definitions read; exact rank-power variance and data are unavailable, ancillary scope preserved. |
| S076 | PASS_2_COMPLETE | TEG within-patient temperature and repeated sampling align with patient random effects; between-group and within-person contrasts distinguished. |
| S077 | PASS_2_COMPLETE | PK convenience sample and paired-temperature/mixed-model definitions read; no inference that this sample is the main randomized outcome population. |
| S078 | PASS_2_COMPLETE | Clearance mg/h divided by mg/L has L/h units; literal terminal-slope AUC wording has undefined slope, but no reported key result depends on it. |
| S079 | PASS_2_COMPLETE | Paired t/Wilcoxon/McNemar choices correspond to stated paired design and assumption conditions; no preferred alternative method proposed. |
| S080 | PASS_2_COMPLETE | Amendment-history power/sample/three-SD specifications matched to later versions; approximate P shorthand and original look counts are not current conflicting rules. |
| S081 | PASS_2_COMPLETE | Ancillary TEG repeated/paired structure is accounted for by patient random effects; no reported key analysis relies on a missing independent-sample step. |
| S082 | PASS_2_COMPLETE | Dated modified-ITT and expanded monitoring amendments give prospective context; unprinted additional exclusion count not assumed. |
| S083 | PASS_2_COMPLETE | Final SAP context/CACE and late mortality window retained; treatment-assignment causal effect is distinguished from received-treatment estimand. |
| S084 | PASS_2_COMPLETE | Blinded target 500→510 and observed attrition rationale read directly; exact revised power formula unavailable and not inferred from simple loss division. |
| S085 | PASS_2_COMPLETE | Source-matched update/corrected flow images independently read; eligibility, clinically relevant dose, early deaths and IMPACT-only subset adjustment retained. |
| S086 | PASS_2_COMPLETE | Historical charter three-SD/.048 final/no-futility rules distinguished from final Version 9 .0459; nominal-versus-look interpretation preserves the screen. |
| S087 | PASS_2_COMPLETE | All 2015 masked outcome/category tests and block displays revisited; no printed primary/mortality stopping-boundary crossing, treatment allocation remains masked. |
| S088 | PASS_2_COMPLETE | All 2016 masked tests read; 321 outcome versus 341 survival denominators explicitly reflect missing-GOSE survivors, not a primary-count contradiction. |
| S089 | PASS_2_COMPLETE | All 2017 masked tests read; 364 GOSE versus 390 survival denominators and outcome totals coherent; no stopping recommendation invented. |
| S090 | PASS_2_COMPLETE | Nine plotted centers and 95% bars independently viewed; interval order/containment coherent and patient random-effect model accommodates repeated rewarming measures. |
| S091 | PASS_2_COMPLETE | KM curves/risk rows/HR and log-rank independently viewed; survival direction coherent, complementary caption resolved and exact common-test attribution absent. |
| S092 | PASS_2_COMPLETE | All location/time tests revisited; count comparison coherent, median-test probabilities require unprinted distributions and implementation. |
| S093 | PASS_2_COMPLETE | Every process comparison and denominator/window definition revisited; continuous tests cannot be recreated from medians and wrapped <.0001 is typography. |
| S094 | PASS_2_COMPLETE | All five other-outcome tests revisited; survivor 69/186 versus 71/182 and observed GOSE denominators match; equal rounded means do not force equal raw means or P = 1. |
| S095 | PASS_2_COMPLETE | All adverse-event rows revisited; existing C004 retains bleeding P attachments, sparse cardiac P values do not establish an unspecified exact/corrected-test contradiction. |
| S096 | PASS_2_COMPLETE | Four timing-category proportions/intervals and merged P visually reread; C003 retains diagnostic .043327/.160498 and missing category/implementation facts without re-emission. |
| S097 | PASS_2_COMPLETE | All PP baseline/primary/adjusted rows read; primary 58/124 versus 69/151 RR/P reconcile, and 132/161 baseline versus 132/160 mortality sets remain matched to their endpoints. |
| S098 | PASS_2_COMPLETE | All seven PP secondary RR/CI/P/count rows independently recomputed; direction/containment and exploratory pneumonia significance coherent. |
| S099 | PASS_2_COMPLETE | Four PP subgroup estimates/counts plus two interaction P values revisited; each pair partitions primary totals, and interaction is a separate model test. |
| S100 | PASS_2_COMPLETE | All 17 PP temperature centers/bars independently viewed and ordered/containing; unprinted bar confidence level/model not inferred. |
| S101 | PASS_2_COMPLETE | PP 72-hour sensitivity counts/RR/P and kappa interval agree; AUC classification threshold and covariance unavailable, not guessed. |
| S102 | PASS_2_COMPLETE | All AT baseline/primary/adjusted rows revisited; primary RR/P reconcile and adjusted unfavorable label is preserved rather than forced to match a crude favorable OR. |
| S103 | PASS_2_COMPLETE | All seven AT secondary count/RR/CI/P rows recomputed; printed precision/direction coherent, pneumonia remains explicitly exploratory. |
| S104 | PASS_2_COMPLETE | Four AT subgroup rows and two interaction tests revisited; partition totals and estimate/interval direction agree without inventing interaction coefficients. |
| S105 | PASS_2_COMPLETE | AT 72-hour sensitivity 56/121 versus 85/188 yields RR 1.023627/P .854003; rescue crossover and classification threshold are not inferred beyond the text. |
| S106 | PASS_2_COMPLETE | Worst-case allocation 117/260 versus 125/240 reproduces RR/RD/P and nonsignificant intervals; exact missingness assignment matched. |
| S107 | PASS_2_COMPLETE | Best-case allocation 137/260 versus 111/240 reproduces RR/RD/P and nonsignificant intervals; point estimates lie within ordered limits. |
| S108 | PASS_2_COMPLETE | PMM/MAR/11 datasets and CMH/score method read; modeled RR and marginal RD need not share a crude variance. Strata, pooling and estimand mapping remain unavailable. |
| S109 | PASS_2_COMPLETE | Adequate-dose OR .91 and adjusted OR .95 have coherent null-containing intervals; separate time-imbalance adjustment and 16-minute mean contrast retained, inserted token screened. |
| S110 | PASS_2_COMPLETE | All post hoc baseline rows/footnotes revisited; median/rank P .02 versus mean P .01 describe distinct summaries, with no primary model respecification. |
