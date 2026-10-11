# Statistical consistency review — fresh pass 2

Lossless merge of three independently completed disjoint scopes. All 348 registered statistical relationships received pass 2. The pass-2 candidate C010 arose from S415 after independent screening; the initial stable set was C001–C009.

# Statistical checker — pass 2 main and plan shard

Runtime agent: /root/statistics_pass2_main; fresh gpt-6.1-sol/high, distinct from pass 1. Exact relationship scope: S001–S110, all 110. Complete ledger C001–C009, all screening rows and mechanical recheck facts, and all 35 original checker exclusions were revisited. QUALITY_CONTROL_SCOPE.md and the 1.6.2 review contract were read completely. Source-linked main/plan tuples, direct selected-page stdout and current exact-source recheck renders were reread; REPORT versus PLAN roles follow content. Other fresh pass 2 shards own S201–S320 and S321–S438. No source/reused artifact was changed, no web or old conclusions used, and no new preprocessing derivative produced.

Primary diagnostics independently recomputed from the printed inputs: SE=sqrt(11.6²/475+11.4²/480)=.7443347; normal 95% CI around−.27≈[−1.72887, 1.18887]. These are diagnostic approximations, not the authors' exact t test or df. Six missing of 961=.6243496%<1%; complete-case rule agrees. Normal sample-size diagnostic 2×25×(1.959964+.841621)²=392.4439 versus 397/arm is within display precision, and the explicit 20% increase produces 476.4 versus 476. Binary identity precision gaps were independently recomputed for all ten rows, with only ARDS/infection above.05; C001 records that already included question.

Source confidence/significance levels are 95%/.05 and P values explicitly two-sided. Every effect tuple was checked for endpoint order, containment, direction and null/P agreement. Distinct attributed analyses would remain alternatives for a reproduced interval/test conflict, never reasons to remove it. Exact SE/test inversion requires source definitions; no covariance, model, df, variance or estimand mapping is inferred. Superiority is supported only where the stated rule permits it; the primary conclusion is absence of superiority, subgroup conclusion exploratory, with no equivalence/noninferiority margin or efficacy interim boundary supplied.

## Every assigned relationship

| S ID | Exact source location and role | Supplied relationship and printed values | Independent pass-2 reassessment and named limitation | Pass 1 | Pass 2 |
|---|---|---|---|---|---|
| S001 | REPORT DOC-001 pp 1, 2, 5, 6 Table 2; PLAN DOC-003 p12 | VFD 28 n475/480, means 15.2(SD 11.6)/15.5(11.4), medians 21(IQR 0–26)/21(0–26), MD−.27[−1.74, 1.19], P=.71, t test | Primary count 475+480=955 and six missing reconcile; CI contains MD and zero; P=.71 agrees. Diagnostic SE .7443 and normal CI [−1.7289, 1.1889] are compatible; no t variant/df assumed. C004/C005/C006 concern definition/model/analysis availability, not this numerical tuple. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S002 | REPORT DOC-001 p6 Table 2 | Survivor ventilation means 5.4(SD 6.6)/6.0(7.3), medians 3(1–6)/3(1–8), MD−.56[−1.61,.49], no P | Survivor-only means and MD agree within half-unit mean allowances; CI ordered and contains MD/zero. Survivor n and test definition absent; no randomized-arm n substituted. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S003 | REPORT DOC-001 pp 1, 6 Table 2 | ICU LOS means 9.6(SD 13.3)/9.2(9.9), medians 6(3–11)/6(3–11), MD.39[−1.09, 1.89], P=.58, inverse Gaussian GLM | CI contains .39 and zero; P=.58 nonsignificant; GLM mean estimand distinct from Figure 2C discharge HR. Link/variance unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S004 | REPORT DOC-001 pp 1, 6 Table 2 | Hospital LOS means 20.4(SD 23.8)/21.0(21.1), medians 14(6–26)/15(8–26), MD−.60[−3.52, 2.31], P=.68, inverse Gaussian GLM | CI contains −.60 and zero; P=.68 nonsignificant; mean LOS distinct from Figure 2D discharge HR. Link/variance unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S005 | REPORT DOC-001 p6 Table 2 | ICU mortality 132/450(29.3%)/115/458(25.1%), RR 1.11[.96, 1.27], P=.15; Wald approximation CI/χ² P | 132/450 and 115/458 percentages reconcile; RR CI contains 1.11 and 1; .15 agrees. Shared binary identity belongs C001; this row's point-gap ratio .03713 is screened by precision. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S006 | REPORT DOC-001 p6 Table 2 | Hospital mortality 151/477(31.7%)/140/484(28.9%), RR 1.06[.93, 1.22], P=.35 | 151/477 and 140/484 percentages reconcile; RR CI contains 1.06 and 1; .35 agrees. This row's point-gap ratio .01852 is below precision threshold. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S007 | REPORT DOC-001 pp 1, 6 Table 2 | Day 28 deaths 166/476(34.9%)/155/483(32.1%), HR 1.12[.90, 1.40], P=.30, Cox | Deaths 166/476 versus 155/483 and percentages agree; HR CI contains 1.12/1, P=.30 agrees, abstract copy matches. Cox HR not substituted with a crude risk ratio. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S008 | REPORT DOC-001 pp 1, 6, 7 Figure 2B | Day 90 deaths 186/476(39.1%)/181/479(37.8%), HR 1.07[.87, 1.31], P=.54, Cox | Deaths 186/476 versus 181/479 and percentages agree; HR 1.07/.87–1.31 and P=.54 match abstract, Table 2 and Figure 2B; event-time inputs unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S009 | REPORT DOC-001 pp 1, 6 Table 2 | ARDS 17/448(3.8%)/23/462(5.0%), RR.86[.59, 1.24], P=.38 | C001 retains ARDS identity gap .05948; printed .86/.59–1.24/.38 has ordered CI, containment, null agreement and matching copies. C002 supplies separate case-definition question. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S010 | REPORT DOC-001 pp 1, 6 Table 2 | Pneumonia 19/450(4.2%)/17/462(3.7%), RR 1.07[.78, 1.47], P=.67 | Printed 1.07/.78–1.47/.67 agrees in direction, containment and nonsignificance; source percentages reconcile. Exact estimator/conditioning question remains shared C001 context. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S011 | REPORT DOC-001 pp 1, 6 Table 2 | Pneumothorax 8/448(1.8%)/6/462(1.3%), RR 1.16[.73, 1.84], P=.55 | Printed 1.16/.73–1.84/.55 agrees in direction, containment and nonsignificance; event percentages reconcile. Half-input point gap .01922 does not separately qualify. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S012 | REPORT DOC-001 pp 1, 6 Table 2 | Atelectasis 51/449(11.4%)/52/464(11.2%), RR 1.00[.81, 1.23], P=.94 | Printed 1.00/.81–1.23/.94 includes null and estimate; near-null direction allows rounding; event percentages reconcile. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S013 | REPORT DOC-001 p6 Table 2 | Extrapulmonary infection 20/448(4.5%)/28/463(6.0%), RR.84[.60, 1.18], P=.28 | C001 retains infection identity gap .07487; printed .84/.60–1.18/.28 includes estimate/null and ordered limits; event percentages reconcile. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S014 | REPORT DOC-001 p6 Table 2 | Extrapulmonary sepsis 12/448(2.7%)/16/463(3.5%), RR.87[.56, 1.33], P=.50 | Printed .87/.56–1.33/.50 includes estimate/null; event percentages reconcile; half-input point gap .03415 does not separately qualify. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S015 | REPORT DOC-001 p6 Table 2/narrative | Delirium 149/343(43.4%)/132/361(36.6%), RR 1.15[.99, 1.34], P=.06 | Printed 1.15/.99–1.34/.06 includes estimate/null and supports nonsignificant narrative; 149/343 and 132/361 percentages reconcile. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S016 | REPORT DOC-001 p6 Table 2 | Tracheostomy 54/477(11.3%)/52/484(10.7%), RR 1.03[.84, 1.26], P=.78 | Printed 1.03/.84–1.26/.78 includes estimate/null; 54/477 and 52/484 percentages reconcile; model identity not invented. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S017 | REPORT DOC-001 pp 4, 6; PLAN DOC-003 p15 | Primary stratification random-effects GLMM, hospital/intubation location, P=.72 | Reported stratification-random-effects P=.72 is distinct from four-covariate sensitivity absent under C006. No estimate/CI supplied for exact GLMM reproduction. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S018 | REPORT DOC-001 pp 6, 8 narrative | Inside ICU MD−2.50[−4.63,−.36]; outside 1.45[−.52, 3.43]; interactionP=.01, printed IQR labels | Inside estimate−2.50 lies within−4.63–−.36; outside 1.45 within−.52–3.43. Interaction .01 tests a between-stratum contrast, not either CI's null. C007 model replacement retained; IQR naming excluded. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S019 | REPORT DOC-001 p7 Figure 2A | Liberation HR.99[.86, 1.14], P=.92, increasing free-from-ventilation curves | Liberation HR.99/.86–1.14/.92 includes estimate/null and direction matches curves. SAP specifies log-rank curve comparison; report does not identify every event-time P's producing test; no unsupported equivalence between tests imposed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S020 | REPORT DOC-001 p7 Figure 2B | Survival HR 1.07[.87, 1.31], P=.54, decreasing survival curves | Survival figure HR 1.07/.87–1.31/.54 exactly matches mortality tuple S008; decreasing survival and mortality hazard direction coexist. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S021 | REPORT DOC-001 p7 Figure 2C | ICU LOS HR.94[.80, 1.09], P=.41; remaining-in-ICU curves | Discharge HR.94/.80–1.09/.41 contains estimate/null; remaining-in-ICU display coherent; do not equate discharge HR with mean-day difference. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S022 | REPORT DOC-001 p7 Figure 2D | Hospital LOS HR 1.02[.87, 1.19], P=.83; remaining-in-hospital curves | Discharge HR 1.02/.87–1.19/.83 contains estimate/null; remaining-in-hospital display coherent; precise event coding absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S023 | REPORT DOC-001 p7 Figure 2A caption | Schoenfeld residualsP=.68 | Residual P=.68 does not trigger stated PH replacement at .05; no test statistic/df reconstructed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S024 | REPORT DOC-001 p7 Figure 2B caption | Schoenfeld residualsP=.13 | Residual P=.13 does not trigger stated PH replacement at .05; no test statistic/df reconstructed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S025 | REPORT DOC-001 p7 Figure 2C caption | Schoenfeld residualsP=.21 | Residual P=.21 does not trigger stated PH replacement at .05; no test statistic/df reconstructed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S026 | REPORT DOC-001 p7 Figure 2D caption | Schoenfeld residualsP=.82 | Residual P=.82 does not trigger stated PH replacement at .05; no test statistic/df reconstructed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S027 | REPORT DOC-001 p7 Figure 2A caption | Observation period median(IQR)4.4[3.7, 5.1]/4.3[3.4, 5.2]days | Medians 4.4/4.3 are inside ordered 3.7–5.1/3.4–5.2 ranges; observation periods not equated to survivor duration. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S028 | REPORT DOC-001 p7 Figure 2B caption | Median survival observation time not computed because minimum observed value .60 | Minimum .60 wording resolved as survival probability remaining above .50; no conflicting numerical time identified; terminology excluded. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S029 | REPORT DOC-001 p7 Figure 2C caption | Observation period median(IQR)8[7, 8]/8[6, 9]days | Medians 8/8 fall inside 7–8/6–9; these observation summaries do not state same estimand/population as mean/median Table 2 LOS. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S030 | REPORT DOC-001 p7 Figure 2D caption | Observation period median(IQR)21[19, 23]/21[20, 24]days | Medians 21/21 fall inside 19–23/20–24; observation summaries distinct from Table 2 LOS distributions. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S031 | REPORT DOC-001 pp 1, 2, 6–8 | No overall VFD/LOS/mortality/pulmonary superiority; subgroup exploratory | No primary superiority follows from P=.71 and null-containing CI; no equivalence conclusion or margin assumed. Subgroup conclusion remains exploratory. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S032 | REPORT DOC-001 pp 2, 4; PLAN DOC-003 pp 5, 12 | Low strategy superior for VFD; two-sided .05 and 95% CI | Source explicitly supplies superiority, two-sided .05 and 95% CI; matching report inference coherent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S033 | REPORT DOC-001 p4; PLAN DOC-003 p12 | No multiplicity adjustment; secondary analyses exploratory; two-sided 5% | No multiplicity adjustment and exploratory secondaries are explicitly stated; do not impose an unstated protected familywise criterion. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S034 | REPORT DOC-001 pp 4, 6 footnotea; PLAN DOC-003 p12 | Primary t test/mean difference 95% CI | Patient-level randomization and continuous primary outcome match stated two-group t test; no preference-based method observation. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S035 | REPORT DOC-001 pp 4, 6, 7; PLAN DOC-003 p13 | LOS inverse-Gaussian mean differences plus Cox HR/KM | Two explicit LOS models report distinct quantities; conflicting P values are not inferred by mapping means to discharge hazards. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S036 | REPORT DOC-001 pp 4, 6 footnotec; PLAN DOC-003 p13 | Binary RR, Wald likelihood-ratio approximation 95% CI andχ² hypothesis test | Source RR/Wald-approximation/chi-square statement and shared C001 identity question retained. No additional CI/P null conflict in ten rows; no unreported adjustment assumed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S037 | REPORT DOC-001 pp 4, 7; PLAN DOC-003 p13 | Cox survival, all-cause death/randomization, lost follow-up censored; alternative parametric if PH fails | Lost-follow-up censoring and PH replacement rule stated; residual tests do not invoke alternative model; event/censor inputs absent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S038 | REPORT DOC-001 p4; PLAN DOC-003 p12 | Tidal-volume repeated measures, random hospital/patient intercepts, continuous time | Random patient/hospital intercepts match patient repeated measures and multicenter data; fitted window unavailable, reviewed at S088. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S039 | REPORT DOC-001 p4; PLAN DOC-003 p11 | Primary missing<1%, complete-case only | Six missing/961=.62435% below 1%; complete-case analysis matches stated trigger and source flow. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S040 | REPORT DOC-001 p7; PLAN DOC-003 pp 11–12; DOC-002 pp 30, 33, 36 | ITT random assignment except consent withdrawal; complete cases | Assigned randomized arms retained; complete cases and consent exclusions explicitly defined. ITT terminology alone does not alter numerical population. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S041 | REPORT DOC-004 p10 eFigure 1; REPORT DOC-001 pp 1, 5–6 | Primary empirical cumulative VFD distribution, 0–28 days, blacklow/redintermediate, noP/CI/n | Direct source-matched eFigure 1 read: ordered 0–28 horizontal scale, low/intermediate legend and approximate median crossing 21 agree. No exact digitization or death-zero rule supplied. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S042 | PLAN DOC-002 pp 10, 19, 33; PLAN DOC-003 p8; REPORT DOC-001 p4 | VFD 28 after ICU admission versus calculated from randomization | C004 retains repeated ICU-admission plan anchor versus report randomization; SAP day 1 origin unspecified. Different events cannot be resolved by numerical rounding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S043 | PLAN DOC-002 pp 17, 19; PLAN DOC-003 p11; REPORT DOC-001 p4 | Planned 952=2×476 total; enrolled 961 | 952 planned versus 961 actual are distinct target/enrollment quantities; 476×2=952; no substituted planned analyzed n. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S044 | PLAN DOC-002 pp 18–19; DOC-003 p11; REPORT DOC-001 p4 | Difference 1 day,means 23/24,SD 5,power 80%, two-group t,two-sided.05,n397 before inflation | Normal-power diagnostic 392.44/arm versus 397 within precision threshold; exact power algorithm absent. No exact reproduction asserted; original model replacement separately C005. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S045 | PLAN DOC-002 p19; REPORT DOC-001 p4 | 397 increased 20%=476.4/arm, printed 476; report allows 20% dropout | 397×1.20=476.4 matches printed 476. Alternative divide-by-.8 convention gap ratio .03371≤.05; not a sample-size finding. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S046 | PLAN DOC-002 pp 10, 16, 26; DOC-003 pp 3, 6; REPORT DOC-001 p2 | Individual patient, parallel two-arm randomized trial | Individual patient, parallel two-arm randomization agrees with independent primary comparison; no cluster allocation assumed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S047 | PLAN DOC-002 p26; DOC-003 p7; REPORT DOC-001 p2 | Allocation 1: 1, random blocks, center/intubation strata | 1: 1 random blocks and center/intubation stratification match; block 2–6 report detail adds no contradiction; stratified sensitivity present. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S048 | PLAN DOC-002 pp 30, 36; DOC-003 pp 6, 11–12; REPORT DOC-001 pp 2–3 | Deferred consent within 24h, exclusion/replacement if no consent | Deferred consent within 24h and replacement/exclusion stated; displayed enrolled population does not claim to include all pre-consent randomizations. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S049 | PLAN DOC-002 pp 17–18; DOC-003 pp 6–7; REPORT DOC-001 p2 | Ventilation anticipated>24h, inclusionwithin 1h of ICUstart/arrival, priorventilation≤12h | Within 1h intended randomization and≤12h pre-ICU ventilation match; observed timing does not redefine source intended eligibility. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S050 | PLAN DOC-002 pp 17–18, 48; DOC-003 p7; REPORT DOC-001 p2 | ARDS excluded clinically; protocol permits PF<200 if explicitnoARDS/no directrisk | C003 retained from complete original and later rule sets: no-direct-risk-factor condition absent later. Do not treat omission as mere prose or assert actual enrollment/count impact. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S051 | PLAN DOC-002 p20; DOC-003 p7; REPORT DOC-001 pp 3, 5 | PBW male 50+.91(height−152.4),female 45.5+.91(height−152.4)kg | Both sex-specific PBW equations and cm/kg units match all supplied occurrences; dose denominator coherent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S052 | PLAN DOC-002 pp 20–22; DOC-003 pp 7–8; REPORT DOC-001 p2 | Lowstart 6,target 4,step 1 mL/kgPBW/h,PSVmin 5 cmH 2O and intoleranceexceptions | Low start 6/minimum 4/step 1 and support 5 match; above-target acceptance at>6 versus>8 alone supplies no prohibition of 6–8. No achieved-dose change inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S053 | PLAN DOC-002 pp 20–22; DOC-003 p8; REPORT DOC-001 p2 | Comparisonstart 10,target 8–10,pressurecap 25 cmH 2O | Comparison start 10, target 8–10 and pressure 25 match; high/intermediate terminology excluded. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S054 | PLAN DOC-002 p23; REPORT DOC-001 p3 | Assigned intervention resumed if reintubated through 28 days | Assigned strategy resumed on reintubation within 28 days; report/plan intervention duration agrees. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S055 | PLAN DOC-002 pp 23, 49; DOC-003 p8; REPORT DOC-001 pp 3–4 | Unassistedbreathing≥24h,extubationwithout reintubation 24h,tracheostomyunassisted 24h | Qualifying unassisted periods and 24h tracheostomy/extubation definitions support primary composite; no preferred operational criterion imposed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S056 | PLAN DOC-002 p26; DOC-003 p8; REPORT DOC-001 p4 | Daysalive/free 1–28, include additional ventilationperiods; ventilation>28→0 | Report explicitly sums recurrent unassisted periods; clinical composite ingredients agree apart from C004 time origin. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S057 | REPORT DOC-001 p4; DOC-004 p10; PLAN DOC-003 p8 | Alive/free composite wording but no explicit instruction assigning 0 to every deathbefore 28 | No supplied instruction assigns zero to every pre-day 28 death; CDF-versus-mortality comparison cannot assume that rule or exact curve coordinates. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S058 | PLAN DOC-002 p33; DOC-003 pp 12, 21; REPORT DOC-001 p4 | Original Cox→updated Student t primary analysis | C005 retained under Route A, category 5 despite prospective disclosed update: original primary Cox replaced by t-test. Updated model/report agreement does not remove the original planned-analysis relationship. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S059 | PLAN DOC-002 p33; DOC-003 pp 12–13 | ContinuousnormalmeanSD/t; otherwisemedianIQR/Mann–Whitney; binaryχ²/Fisher; time-dependentPH | General original secondary-method text and specific updated models treated in dated-plan context; no preferred alternative analysis or unexplained model assumption. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S060 | PLAN DOC-002 pp 26, 33; DOC-003 pp 9, 21; REPORT DOC-001 p4 | Day 28 mortality added as secondary in updatedplan | Day 28 mortality prospectively added and reported as secondary, with explicit disclosure; F-XS-004 already screened, no absent promised original result or status change. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S061 | PLAN DOC-002 pp 26, 28; DOC-003 p13; REPORT DOC-001 pp 4, 6 | ICU/hospital/day 28/day 90 mortality; day 28/90 KM/Cox | Specified mortality timepoints and current KM/Cox plan agree; binary ICU/hospital and time-to-event 28/90 analyses remain distinct. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S062 | PLAN DOC-003 p13; REPORT DOC-001 p6 | ICU/hospitalmortality RR versus day 28/90 HR | RR versusHR labels explicitly distinguish binary and event-time outcomes; C001 concerns conditioning of binary estimates, not replacement of HR with crude ratio. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S063 | PLAN DOC-003 p13; REPORT DOC-001 p4 | LOS distribution selected by deviance from truncatedPoisson/gamma/inverseGaussian, reportedinverseGaussian | Inverse Gaussian is one stated planned right-tailed candidate family; absent deviances/link alone supplies no contradictory number or producing model. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S064 | PLAN DOC-002 pp 26–28, 48; DOC-003 pp 9, 13; REPORT DOC-001 pp 1, 4, 6 | NewARDS,VAP,atelectasis,pneumothorax; planascertainmentto 28 days/ICUdischarge | C002 retained: generic new-ARDS/Berlin definition and specific moderate/severe collection leave grade-defined event set unresolved for 17/448 and 23/462. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S065 | PLAN DOC-002 pp 10, 15, 27–28; REPORT DOC-001 pp 4, 6 | Sedative cumulativeuse/duration secondary | Sedative result summaries present; source three-day display does not prove replacement of complete-course planned collection. F-XS-007 already screened. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S066 | PLAN DOC-002 pp 10, 15, 27–28; REPORT DOC-001 pp 4, 6 | NMBA cumulativeuse/duration excludingintubation | NMBA results present and source excludes intubation dosing prospectively; no supplied statement contradicts that exclusion or proves full-course replacement. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S067 | PLAN DOC-002 pp 27–28; REPORT DOC-001 pp 4, 6 | ICUdelirium, CAM–ICU sourceascertainment | CAM-ICU ascertainment plan and reported delirium result coexist; no alternative operational definition printed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S068 | PLAN DOC-002 pp 27–28; REPORT DOC-001 p4 | ICUacquiredweakness plannedsecondary, unavailable reliabledata/notreported | Reliable ICU-weakness data unavailable and nonreporting expressly disclosed; non-key secondary omission is outside planned-primary/key-secondary category. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S069 | PLAN DOC-002 pp 27, 29; REPORT DOC-001 pp 4, 6 | Bloodproduct transfusion secondary | Blood-product secondary comparisons present; no planned-outcome nonreporting claim; tuple reproduction owned by support shard. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S070 | PLAN DOC-002 pp 10, 15, 27–29; REPORT DOC-001 p4 | Needfor reducingdeadspace secondary | Dead-space measure remains named secondary; lack of additional non-key tuple does not establish changed status or primary/key result omission. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S071 | PLAN DOC-002 pp 27, 29–30; REPORT DOC-001 p4 | Selectedpatient EAdi plannedsecondary, unreliabledata/notreported | Selected-patient EAdi unavailable and expressly unreported; no changed status or contradictory numerical output. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S072 | PLAN DOC-002 pp 27, 30; REPORT DOC-001 p4 | Selectedcenter VOC plannedsecondary, unreliabledata/notreported | Selected-center VOC unavailable and expressly unreported; no changed status or contradictory numerical output. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S073 | PLAN DOC-002 pp 10, 15, 26–27; REPORT DOC-001 p4 | Asynchrony objective versus absent detailedsecondarylist/result | Asynchrony objective/list detail differs without supplied status reclassification, key-secondary designation or conflicting clinical result; excluded non-key omission. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S074 | PLAN DOC-002 p33; DOC-003 pp 13–14, 22; REPORT DOC-001 pp 4, 6 | Per-protocol primaryVFD comparison; majorviolationexclusionsfirst 2 days, low>6/high<8 outsideexceptions | C006 retains per-protocol VFD specification and supplied-result absence; complete cases are not a substitute. Exact exclusions/sizes/output or withdrawal needed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S075 | PLAN DOC-002 p33; DOC-003 p14; REPORT DOC-001 p4 | Primary subgroup pneumonia versusotherreason | Pneumonia primary-VFD subgroup definition matches; individual tuples owned by support; C007 shared producing distribution retained. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S076 | PLAN DOC-002 p33; DOC-003 p14; REPORT DOC-001 p4 | Primary subgroup sepsis/nonsepsis | Sepsis subgroup definition matches; individual tuples owned by support; C007 distribution retained. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S077 | PLAN DOC-003 p14; REPORT DOC-001 p4 | Primary subgroupPF≤200/>200 | PF≤200/>200 threshold matches; C003 determines governing eligibility context; C007 producing model retained. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S078 | PLAN DOC-003 p14; REPORT DOC-001 p4 | Primary subgroup LIPS≥4/<4 | LIPS≥4/<4 threshold matches; distribution change belongs C007; no imagined subgroup n. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S079 | PLAN DOC-003 p14; REPORT DOC-001 p4 | Primary subgroup clinical/surgical | Clinical/medical versus surgical definitions match field context; distribution change belongs C007; terminology excluded. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S080 | PLAN DOC-003 p14; REPORT DOC-001 p4 | Primary subgroupSAPSII≥50/<50 | SAPSII≥50/<50 threshold matches; distribution change belongs C007; no invented cutpoint. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S081 | PLAN DOC-003 p14; REPORT DOC-001 p4 | Primary subgroupprerandomizationventilation>6/≤6h | >6/≤6h definition matches, but C009 exact supplementary layout leaves effect-to-population assignment unresolved; no subgroup n used to select row. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S082 | PLAN DOC-003 p14; REPORT DOC-001 pp 4, 6, 8 | Primary subgroupintubationinside/outsideICU | Inside/outside definition matches; main effects/interaction agree with eTable 5; significant interaction remains exploratory under unadjusted rule and C007 model change. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S083 | PLAN DOC-003 pp 14, 22; REPORT DOC-001 p4; DOC-004 p9 | Primary subgrouphigh/lowrespiratoryrate,splitfirst 2 daysmedian | C006 retains missing respiratory-rate subgroup; prospective list and matrix updated list both include it. Matrix reporting claim is contextual, no additional P_P. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S084 | PLAN DOC-003 pp 14, 22; REPORT DOC-001 p4 | Updatedsubgroupinteractionzero-inflatedGLM→reportedGaussianGLM; matrixposthocchange | C007 retains zero-inflated versusGaussian producing model under Route A, category 5, explicit post-hoc disclosure retained; no model-induced numerical effect claimed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S085 | PLAN DOC-003 pp 14–15, 21; REPORT DOC-001 pp 4, 6 | Primarysensitivityzero-inflatedGLMadjustingage,LIPS,SAPSII,PF | C006 retains four-covariate sensitivity absence; stratification-random-effects P=.72 cannot stand for a different covariate GLM. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S086 | PLAN DOC-003 p15; REPORT DOC-001 pp 4, 6 | Secondprimarysensitivityzero-inflatedGLMM,stratarandomeffects | Second sensitivity present as random-effects P=.72. Report omits distribution detail; absence alone does not reproduce a different specified distribution. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S087 | PLAN DOC-003 pp 15, 22; REPORT DOC-001 pp 4, 6 | Mechanical-power mediation of primaryVFD; derive drivingpressure/flow fromcollecteddata | C006 retains mechanical-power mediation absence; descriptive driving pressure and respiratory rate do not supply treatment-to-VFD mediation output. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S088 | PLAN DOC-003 p12; REPORT DOC-001 pp 4–5; DOC-004 pp 5–7 | Plannedtidalvolume mixedrepeatedmeasures first 7 days versus printed tables first 3 days | Seven-day planned mixed model versus three-day printed summaries reviewed: fitted report window undefined, so no direct model-window replacement established. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S089 | PLAN DOC-003 p12; REPORT DOC-001 p4 | Histogram and D’Agostino–Pearson normalityassessment; baseline count%,medianIQR | Unprinted histograms/normality diagnostics alone are not a method inconsistency; no numerical result contradicts stated diagnostics. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S090 | PLAN DOC-003 p11; REPORT DOC-001 p4 | >1% primarymissing triggers MI+estimatingequations | >1% primary missing-data trigger not reached by 6/961; no unstated imputation required. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S091 | REPORT DOC-001 pp 1, 3, 6; PLAN DOC-003 pp 11–12 | Primaryavailable 475/480 fromrandomized 477/484 | 477−2=475 and 484−4=480; 955 available primary cases agree across flow, abstract and Table 2; no analysis-size conflict. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S092 | REPORT DOC-001 p6; PLAN DOC-003 p11 | Secondary header 475/481; row-specific totals vary | Secondary header 475/481 does not override explicit row-specific denominators; complete cases may vary by endpoint; no one global denominator imposed. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S093 | PLAN DOC-002 p31; DOC-003 p10 | FirstDSMB safety after 150 patients | First safety review after 150 matches sources; no efficacy significance boundary supplied. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S094 | PLAN DOC-003 pp 10–11; REPORT DOC-001 p2 | Statistician safetyanalyses versus nointerimanalyses/committee blindprimaryendpoint | Safety analyses versus no interim analyses resolved by distinct safety/efficacy purpose and primary-endpoint blinding; wording exclusion retained. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S095 | PLAN DOC-002 pp 31–32, 42; DOC-003 pp 10–11; REPORT DOC-001 p2 | Suspendif unforeseen disadvantage; DSMBrecommendedcontinuation | Unforeseen-disadvantage suspension and DSMB continuation statements have no printed incompatible quantitative criterion; no alpha spending invented. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S096 | PLAN DOC-002 p31; DOC-003 p10 | DSMB 6–8 monththen 6 monthly versus first 150 thenfollowingyear | DSMB calendar difference peripheral; first 150 common and no primary decision margin changes. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S097 | PLAN DOC-002 pp 11, 16, 34; REPORT DOC-001 p4 | Primary CEincrementalcostperICUdayavoided; costscollected/analysisnotreported | Primary economic label belongs ancillary CE section/Other parameters; report explicitly defers it. Current screening excludes this constituent; not re-emitted. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S098 | PLAN DOC-002 pp 27, 34; REPORT DOC-001 p4 | SecondaryCEincrementalcostperventilationdayavoided | Secondary economic measure shares deferred ancillary scope; no clinical primary/key-secondary effect or decision-rule change shown. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S099 | PLAN DOC-002 p34 | Cost=volume×unitprice; ICER=Δcost/Δeffect | Costs=volume×unit price and ICER=Δcost/Δeffect coherent; no supplied numerical costs/effects for reproduction. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S100 | PLAN DOC-002 pp 34–35 | Nonparametricbootstrap 95% ICERintervals/probabilitycosteffective | Bootstrap 95% ICER uncertainty explicitly planned; no supplied competing statistical output or preference-based method question. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S101 | PLAN DOC-002 p35 | One/multiwaysensitivity; PSA 10, 000 second-orderMonteCarlosimulations | 10, 000 simulations and one/multi-way sensitivity specifications coherent; no conflicting supplied count or result. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S102 | PLAN DOC-002 p35 | MethodofmomentsmeanSE; gamma costs; normal/lognormal effects | Mean/SE moment matching with gamma costs and normal/lognormal effects stated; no supplied fitted parameters to test. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S103 | PLAN DOC-002 p35 | Academic/nonacademiceconomicsubgroups | Academic/nonacademic economic subgroups ancillary and without conflicting report effect; no clinical subgroup omission added. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S104 | PLAN DOC-002 p35; DOC-003 p11 | Economic>10% MI versusclinicalprimary>1% MI | Economic 10% and clinical-primary 1% imputation triggers explicitly scope different outcomes; no plan-internal mismatch. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S105 | PLAN DOC-002 pp 33–34 | EconomicITT and clinicalITT | Economic and clinical ITT principles consistent with source consent rules; no arithmetic population discrepancy. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S106 | PLAN DOC-002 p34 | Economichorizon<1 year,nodiscount | Economic horizon<1 year and no discounting internally coherent; no supplied contrary time horizon. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S107 | PLAN DOC-002 pp 10, 15, 26–27; DOC-003 pp 3, 9, 21; REPORT DOC-001 p4 | Primary/secondary/otheroutcomehierarchy, updatedsummarylists fewersecondaryoutcomes | Shorter included-outcome lists do not assert status demotion of existing measures; amended/post-hoc outcomes retain disclosed status; F-XS-004 not re-emitted. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S108 | PLAN DOC-003 pp 21–22; REPORT DOC-001 pp 4, 6 | Change-matrix original/update/inpaper/posthoccolumns | Matrix read by content: PLAN comparison annotation corroborates C005–C007; its in-paper respiratory-rate list does not prescribe a conflicting prospective model/list. C006 P_R only. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S109 | REPORT DOC-001 pp 6, 8; PLAN DOC-003 p12 | InteractionP=.01; exploratory ICUintubationresult; unadjustedtests | P=.01 subgroup interaction and exploratory discussion agree with explicitly unadjusted .05; no protected superiority or equivalence claim inferred. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S110 | REPORT DOC-001 pp 2, 4; PLAN DOC-003 pp 5, 12 | No noninferiority/equivalence design/margin or efficacyinterimrule in package | No noninferiority/equivalence margin or efficacy interim/stopping alpha rule supplied; no conventional margin, boundary or sidedness added. | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Complete ledger and screening implications

Every card C001–C009, its source-linked ledger facts, independent inclusion decision(s), and mechanical recheck facts was reread. No existing observation is re-emitted. These are pass-2 implications, not adjudications or new evidence-state assignments.

| Candidate | Relationship implications after direct rereading | Remaining exact definition or result needed |
|---|---|---|
| C001 | statistical_results, S_W only. S005/S006/S009–S016 share the binary-label/method context; ARDS and extrapulmonary infection alone exceed the point-identity precision rule, with half-input intervals [.722479,.803849] versus printed [.855,.865] and [.705568,.772108] versus [.835,.845], relative gaps .05948/.07487. No separate CI-versus-P null conflict. | Conditioning variable, estimand, producing binary estimator, any adjustment or standardization, and its interval calculation. Reverse-conditioned numerical proximity remains diagnostic. |
| C002 | protocol_report, P_R with P_P retained. S009/S064 use the abstract key-secondary ARDS result; specific moderate/severe collection and generic all-grade criteria leave which case set produced 17/448 and 23/462 unresolved. Text omission alone is not asserted to prove broadening. | Whether mild cases were counted and the governing ascertainment statement/amendment. |
| C003 | protocol_report, P_R with P_P retained. S049/S050/S077 use different complete eligibility rule sets: original low-PF exception requires no direct ARDS risk factor; later lists lack it. Primary-population applicability remains the named result, without a claim about altered enrolled count. | Governing eligibility version/date and whether the attending/no-direct-risk-factor condition remained operational. |
| C004 | protocol_report, P_R only. S001/S042/S056 compare ICU-admission versus randomization origins; SAP unspecified day 1 is context and creates no extra P_P. No numerical MD or P conflict. | Governing VFD 28 origin/amendment and whether every analyzed window used it. |
| C005 | protocol_report, P_R and P_P. S034/S044/S058 retain original primary Cox versus updated/reported t test under Route A, category 5. Explicit prospective pre-lock SAP disclosure is retained; neither that disclosure nor the time-to-liberation Cox result removes the replaced primary-VFD analysis relationship. | Whether updated SAP formally superseded the original model and whether original primary Cox output exists in supplied material. |
| C006 | protocol_report, P_R only. S074/S083/S085/S087 retain exactly four clinical-primary-VFD analysis families: per-protocol, four-covariate zero-inflated sensitivity, respiratory-rate subgroup and mechanical-power mediation. Updated respiratory-rate plan and matrix reporting annotation do not prescribe opposing prospective plans. S097/S098 ancillary economics remains excluded under comparison tiers. | Four outputs/population sizes/estimands or documented withdrawal of each; meaning of matrix respiratory-rate in-paper annotation. |
| C007 | protocol_report, P_R only. S018/S075–S084/S109 retain zero-inflated-to-Gaussian subgroup producing distribution replacement under Route A, category 5, with explicit post-hoc CLT rationale. Prespecified definitions versus post-hoc distribution remain distinct; no model-induced numerical change is inferred. | Producing specification/amendment timing and any zero-inflated subgroup outputs. |
| C008 | statistical_results, S_W only. Direct source-matched supplement p6 rendering confirms 8(5–1). Median[7.5, 8.5], Q1[4.5, 5.5], Q3[.5, 1.5] cannot reconcile; minimum median-Q3 gap 6 gives 6/1=6. Existing Route A, category 2 is numerical magnitude/order, not an IQR-versus-P claim. | Intended upper quartile and original summary output. |
| C009 | report_internal_inconsistency, S_W only. S081 links >6/≤6h definition to direct source-rendered displaced labels: first tuple−.29[−7.04, 6.45], second−.21[−1.72, 1.28]. Both contain zero and interaction .98 tests a different null. Sequence and horizontal alignment do not select a unique tuple-to-population mapping. | Explicit subgroup-to-row mapping or subgroup counts/output. |

F-XS-004 and F-XS-007 are already SCREENED_OUT in the screening log and are not re-emitted. Independent rereading finds that amended day 28 mortality retains its disclosed secondary status, and the three post-hoc additions are not called prespecified in a compared source. Thus there is no reproduced Route A, category 5 status change or unavailable promised original analysis from those additions. Three-day sedative/NMBA summaries versus full-course collection do not state that ascertainment stopped or the planned endpoint was replaced; non-key additional-result absence does not promote the observation to Route A, category 5.

Four pass-1 interpretation updates are recorded without changing stable IDs or source values: S050 now cross-references existing C003; S058 retains existing C005 even though the amendment is disclosed; S064 cross-references existing C002; S097/S098 use the independent ancillary-economic constituent exclusion rather than treating it as part of C006. All are already represented in the screening/ledger/recheck record; there is no additional finding.

## Excluded observations

This table revisits all 35 pre-existing checker exclusion rows, consolidating seven repeated occurrences into 28 distinct apparent-observation patterns. Origin rows are counted from the five named checker tables, starting at 1; they identify audit provenance, not finding IDs. Each pattern retains exactly one reason code. No reconciled check is added as an excluded observation. No original excluded pattern meets an unrecorded Route A category after exact-source rereading; an interval-versus-P conflict would be emitted even for different attributed analyses and would never be screened by precision. The support tuple shards independently revisit their assigned statistical tuples.

| Location | Observation and independent route/precision reappraisal, with origin rows | Reason code |
|---|---|---|
| REPORT [main p5 Table 1](../../../jama_simonis_2018_oi_180108.pdf#page=5) | Implicit baseline denominators versus 477/484: septic-shock 82/477 gives half-input[17.068, 17.314] versus printed 17.6±.05, gap ratio.01339; LIPS gaps≈.0027/.0028. Category 3 inspected; all remaining gaps≤.05. Numeric row 1. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [results p8 eTable 4](../../../joi180108supp3_prod.pdf#page=8) | Eight count/percentage cells versus 477/484: recomputed ranges[66.911, 67.261],[68.627, 68.976],[57.906, 58.237],[56.244, 56.567],[10.995, 11.228],[12.281, 12.513],[75.916, 76.285],[72.755, 73.113]; printed 70.6, 72.1, 61.1, 59.1, 11.7, 13.0, 80.0, 76.4±.05; relative gaps.04658,.04263,.04604,.04202,.03609,.03362,.04581,.04237. Category 3 reviewed; all≤.05. Numeric row 2; support-B row 1. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [main p6](../../../jama_simonis_2018_oi_180108.pdf#page=6), [p7 Figure 2](../../../jama_simonis_2018_oi_180108.pdf#page=7) | Different outcome-specific contributors/initial risk sets are not asserted to be the same analysis population; hospital time-to-event 458/456 versus secondary 475/481 does not reproduce a primary-population contradiction. Numeric row 3. | PERIPHERAL_COMPARISON |
| REPORT [main p6](../../../jama_simonis_2018_oi_180108.pdf#page=6), [results p9](../../../joi180108supp3_prod.pdf#page=9) | IQR name versus 95% CI for identical subgroup MD endpoints is a terminology difference with immediately identifiable matched values; neither containment nor null/P reading reverses. Numeric row 4; cross-source row 3; main/plan pass 1 row 1. | TERMINOLOGY_OR_WORDING |
| REPORT [main p6 Table 2](../../../jama_simonis_2018_oi_180108.pdf#page=6) | Global mean-difference heading coexists with explicit RR/HR row quantities and footnotes; does not select a different numerical estimand at extraction. C001 is the independent binary-conditioning question. Numeric row 5. | CONTEXT_RESOLVES |
| REPORT [results pp 5–7](../../../joi180108supp3_prod.pdf#page=5) | Subtracting marginal pressure medians or multiplying separate ventilation medians is not a source-stated reproducing identity; no method reproduces those medians as a general identity. Numeric row 6. | CONDITIONAL_OR_UNREPORTED |
| PLAN [protocol p20](../../../joi180108supp1_prod.pdf#page=20), [SAP p6](../../../joi180108supp2_prod.pdf#page=6); REPORT [main p2](../../../jama_simonis_2018_oi_180108.pdf#page=2) | High/higher/conventional/intermediate names refer to the same 10 start/8–10 target/25 cap comparison. No number, direction or reference changes. Cross-source row 1; main/plan pass 1 row 2. | TERMINOLOGY_OR_WORDING |
| PLAN [SAP p14](../../../joi180108supp2_prod.pdf#page=14); REPORT [main p4](../../../jama_simonis_2018_oi_180108.pdf#page=4), [results p9](../../../joi180108supp3_prod.pdf#page=9) | Clinical versus medical subgroup wording resolves immediately against surgical; not C009's displaced numerical attribution. Cross-source row 2. | TERMINOLOGY_OR_WORDING |
| PLAN [SAP p6](../../../joi180108supp2_prod.pdf#page=6); REPORT [main pp 1–2](../../../jama_simonis_2018_oi_180108.pdf#page=1) | Expected ventilation>24h versus expected not extubated in next 24h names the same intended eligibility concept; no distinct analyzed population established by phrasing alone. Cross-source row 4. | TERMINOLOGY_OR_WORDING |
| PLAN [protocol p17](../../../joi180108supp1_prod.pdf#page=17); REPORT [main p3](../../../jama_simonis_2018_oi_180108.pdf#page=3) | Other-study participation appears under exclusion versus eligible-not-enrolled; 348 outside randomization in either reading and no analysis-size change. Cross-source row 5. | PERIPHERAL_COMPARISON |
| PLAN [protocol p23](../../../joi180108supp1_prod.pdf#page=23); REPORT [main p3](../../../jama_simonis_2018_oi_180108.pdf#page=3) | Extubation-pressure<versus≤ and following-day versus following-shift operational details do not alter supplied primary/key-secondary result, population size or statistical rule. Cross-source row 6. | PERIPHERAL_COMPARISON |
| PLAN [protocol p31](../../../joi180108supp1_prod.pdf#page=31), [SAP p10](../../../joi180108supp2_prod.pdf#page=10) | DSMB calendar differs; first 150 safety review and continuation agree; no efficacy boundary supplied or changed. Cross-source row 7; main/plan pass 1 row 6. | PERIPHERAL_COMPARISON |
| PLAN [SAP p12](../../../joi180108supp2_prod.pdf#page=12); REPORT [main pp 4–5](../../../jama_simonis_2018_oi_180108.pdf#page=4), [results pp 5–8](../../../joi180108supp3_prod.pdf#page=5) | Seven-day planned respiratory model/display versus three-day printed summaries: the fitted model window is unreported, so a change in producing model cannot be established from an abbreviated display. No clinical primary/key result absent solely on this basis. Cross-source row 8; main/plan pass 1 row 7, consolidated using the missing-window reason. | CONDITIONAL_OR_UNREPORTED |
| PLAN [protocol p17](../../../joi180108supp1_prod.pdf#page=17), [SAP p3](../../../joi180108supp2_prod.pdf#page=3); REPORT [main p2](../../../jama_simonis_2018_oi_180108.pdf#page=2) | Five/six sites and August 20/22 recruitment dates are administrative; no analysis-population or planned statistical-rule difference asserted. Cross-source row 9. | PERIPHERAL_COMPARISON |
| PLAN [SAP p8](../../../joi180108supp2_prod.pdf#page=8); REPORT [main p2](../../../jama_simonis_2018_oi_180108.pdf#page=2) | Accept>6 versus>8 at minimum support does not prohibit 6–8 or establish changed prescribed strategy/achieved quantitative dose; missing prohibition cannot be invented. Cross-source row 10. | CONDITIONAL_OR_UNREPORTED |
| PLAN [SAP p8](../../../joi180108supp2_prod.pdf#page=8); REPORT [main p6](../../../jama_simonis_2018_oi_180108.pdf#page=6) | Survivor-duration summaries under primary block describe primary composite component; source still names one primary VFD endpoint, no status change stated. Cross-source row 11. | CONTEXT_RESOLVES |
| PLAN [SAP p9](../../../joi180108supp2_prod.pdf#page=9); REPORT [main p4](../../../jama_simonis_2018_oi_180108.pdf#page=4) | Exploratory secondary analyses after unadjusted testing retain secondary outcome labels; source does not reclassify prespecified outcomes. Category 5 reviewed, no reproduced status change. Cross-source row 12. | TERMINOLOGY_OR_WORDING |
| PLAN [protocol pp 27, 34–35](../../../joi180108supp1_prod.pdf#page=34); REPORT [main p4](../../../jama_simonis_2018_oi_180108.pdf#page=4) | Explicitly deferred cost analysis is ancillary Other parameters/CE section. Primary within CE does not designate clinical trial primary/key secondary; comparison-tier gate supplies no qualifying clinical-result/population/rule effect. Already independently screened constituent, not re-emitted. Cross-source row 13. | PERIPHERAL_COMPARISON |
| PLAN [protocol pp 27–30](../../../joi180108supp1_prod.pdf#page=27), [SAP p9](../../../joi180108supp2_prod.pdf#page=9); REPORT [main p4](../../../jama_simonis_2018_oi_180108.pdf#page=4) | Unavailable weakness/EAdi/VOC and non-key asynchrony/selected-center result omission: no changed status, abstract key-secondary designation or primary/key-secondary analysis promised here. Clinical-primary families are separately C006. Cross-source row 14; main/plan pass 1 row 9. | PERIPHERAL_COMPARISON |
| PLAN [SAP p14](../../../joi180108supp2_prod.pdf#page=14) | Prespecified post-hoc phrase is terminology; enumerated producing/omitted analyses are already C006/C007 rather than screened through that phrase. Main/plan pass 1 row 3. | TERMINOLOGY_OR_WORDING |
| REPORT [main p7 Figure 2B](../../../jama_simonis_2018_oi_180108.pdf#page=7) | Minimum observed.60 where median survival uncomputed resolves as probability staying>.50; no conflicting numerical time or supplied units require a changed number. Main/plan pass 1 row 4. | TERMINOLOGY_OR_WORDING |
| PLAN [SAP pp 10–11](../../../joi180108supp2_prod.pdf#page=10); REPORT [main p2](../../../jama_simonis_2018_oi_180108.pdf#page=2) | Statistician safety analyses versus no interim analyses differentiated by safety/efficacy context and primary-endpoint blinding; no efficacy test or boundary shown. Main/plan pass 1 row 5. | TERMINOLOGY_OR_WORDING |
| REPORT [main p4](../../../jama_simonis_2018_oi_180108.pdf#page=4), [p6](../../../jama_simonis_2018_oi_180108.pdf#page=6), [results p10 eFigure 1](../../../joi180108supp3_prod.pdf#page=10) | CDF zero jump versus mortality would require unstated all-deaths-zero rule and exact curve counts. Definition counts alive/free periods, does not explicitly impose that convention. Main/plan pass 1 row 8. | CONDITIONAL_OR_UNREPORTED |
| PLAN [protocol p19](../../../joi180108supp1_prod.pdf#page=19); REPORT [main p4](../../../jama_simonis_2018_oi_180108.pdf#page=4) | Alternative retention calculation[396.5/.805, 397.5/.795]=[492.5466, 500] versus 476±.5 has minimum gap 16.0466/476=.03371≤.05; actual stated 20% multiplication gives 476.4. Category 4/sample-size route inspected, not reproduced beyond precision. Main/plan pass 1 row 10. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [results p6](../../../joi180108supp3_prod.pdf#page=6), [p12](../../../joi180108supp3_prod.pdf#page=12), [p5](../../../joi180108supp3_prod.pdf#page=5) | PSV VT day 2 P=.027/.03 intervals[.0265,.0275]/[.025,.035] overlap. Diagnostic uncorrected Pearson P≈.390901/.715260 versus.40/.71 has residual relative gaps≈.01025/.000367 even before input allowances. No CI/significance contradiction; diagnostics do not select producing test. Support-A row 1. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [results p9 eTable 5](../../../joi180108supp3_prod.pdf#page=9), [main p4](../../../jama_simonis_2018_oi_180108.pdf#page=4) | Hypothetical normal independent contrast SE=CIwidth/3.92 yields P≈.473 versus pneumonia.16, but no stated CI-to-interaction model/estimand mapping, df, covariance or variance estimator. It fails precision reproduction for other pairs as well (sepsis≈.188/.17, admission≈.203/.23), so category 4 cannot promote it; subgroup CIs test different nulls from interaction. Category 1 needs corresponding analysis/null, not an assumed mapping. Support-B row 2. | CONDITIONAL_OR_UNREPORTED |
| REPORT [results p7 eTable 3](../../../joi180108supp3_prod.pdf#page=7) | 7/20 printed 35. reads 35%; no substituted digit/value. Category 2 not implicated. Support-B row 3. | NOTATION_OR_TYPOGRAPHY |
| REPORT [results p9 eTable 5](../../../joi180108supp3_prod.pdf#page=9) | Mean() footer omits dispersion abbreviation while ± values and separate 95% CI column stay identifiable; no changed printed numerical value or row assignment. Support-B row 4. | NOTATION_OR_TYPOGRAPHY |

## Findings, completion and limitations

New findings: 0. No F-ST2 heading is generated for a reconciled check, an already screened observation, or an unreported detail alone. Existing IDs and screening decisions remain available for the fresh independent auditor; this shard does not append candidates or assign adjudication labels.

Every one of 110 assigned relationships has PASS_2_COMPLETE. Exclusion audit: 35 original rows, 28 consolidated apparent patterns, 0 promoted rows. Existing ledger implications: all 9 IDs. Four pass-1 interpretation updates as described above; 0 numerical transcription/location repairs; 0 scientific coverage gaps. Canonical merge is the coordinator's responsibility.

Intrinsic limits: unavailable individual event/censor data; survivor/subgroup sample sizes; exact t variant/df; inverse-Gaussian link/variance estimator; binary conditioning/model/interval algorithm; every event-time P's producing-test mapping; fitted longitudinal time window; exact curve coordinates; missing clinical-primary outputs/amendments; intended PEEP upper quartile and prior-ventilation row mapping. Missing definitions cannot suppress a reproduced Route A conflict, and no preferred method is proposed. No fresh tooling derivative was needed; all direct-source/reused assets are preserved.

Artifacts: checkers/parts/statistical_pass_2_main_plan.md and statistics/parts/pass2_main_plan_closure.md.



# Statistical pass 2 — support shard A

Runtime task ID: /root/statistics_pass2_support_a. Model: gpt-6.1-sol. Reasoning effort: high. Fresh statistical pass-2 shard, distinct from /root/statistics_pass1_support_a. The coordinator's spawn runtime identifier is the manifest authority.

Exact scope: REPORT DOC-004, joi180108supp3_prod.pdf, eTable 1 physical p5, all 48 variable–occasion tuples S201–S248; eTable 2 physical p6, all 72 variable–mode–occasion tuples S249–S320; matching nine panels in eFigures 2–4 physical pp11–13, associated with existing S250–S252, S274–S276 and S294–S296. Every assigned relationship was revisited. No outside-shard relationship or new S ID was added.

The complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read. Pass-2 inputs include the complete nine-ID candidate ledger, the entire initial inclusion screen, every mechanical recheck fact, the support-A tuple inventory, and all 35 excluded-observation rows in the numeric, cross-source, and three statistical-pass-1 checker parts: numeric 6, cross-source 14, main/plan statistical pass 1 10, support-A statistical pass 1 1, and support-B statistical pass 1 4. The initial tally of 32 omitted the cross-source table's final three rows; those rows have now been reread against all five Route A categories and the display-precision rule. They concern exploratory/secondary status wording without a changed status, deferred ancillary economics, and incomplete non-key outcome lists without a changed status or missing primary/key-secondary result. They add no numerical/test/count/reproducing-method conflict in S201–S320 and no new finding within this shard. Six original excluded rows bear directly on this shard; their four consolidated patterns are reconsidered below. Outside-shard source verification remains with the other pass-2 assignments.

Counts: 120 relationships; 120 PASS_2_COMPLETE records; 0 new findings; 4 consolidated excluded-observation rows; 0 scientific coverage gaps. One existing included issue, C008, remains associated with S313 and is not re-emitted. No candidate, classification, source, reused asset or pass-1 part was modified.

## Source-grounded pass-2 checks

Fresh selected-page direct layout extraction from the supplied results PDF confirmed every printed tuple in [eTable 1 p5](../../../joi180108supp3_prod.pdf#page=5) and [eTable 2 p6](../../../joi180108supp3_prod.pdf#page=6). The current exact-source recheck p6 rendering was visually reread, including 8 (5–1). The current exact-source renderings of [eFigure 2 p11](../../../joi180108supp3_prod.pdf#page=11), [eFigure 3 p12](../../../joi180108supp3_prod.pdf#page=12), and [eFigure 4 p13](../../../joi180108supp3_prod.pdf#page=13) were visually reread for all nine panels. They establish mode, day, variable, legend, axes, median direction and P-value attribution. Exact quantiles or counts were not invented by digitizing curves.

Both tables define continuous entries as median (interquartile range). Across 112 continuous tuples, 111 have ordered quartiles containing the median in both arms; the remaining tuple is the already included S313/C008. These IQRs are distributions, not confidence intervals for a between-arm estimate. None of the 120 tuples supplies a between-arm estimate CI, standard error or test statistic. No interval-versus-null-P conflict is therefore established from IQR overlap. Equal or nearly equal medians do not require nonsignificance, and separated medians do not require significance, without the actual distributions and producing analysis.

The [main REPORT p4](../../../jama_simonis_2018_oi_180108.pdf#page=4) specifies two-sided P values, .05 significance without multiplicity adjustment, exploratory secondary analyses, and longitudinal tidal-volume mixed models with random hospital/patient intercepts and continuous time. The [SAP PLAN p12](../../../joi180108supp2_prod.pdf#page=12) specifies repeated-measures tidal-volume modeling over seven days. These passages do not map a specific algorithm, covariance, variance estimator or degrees of freedom to each separate continuous mode/day P value or distribution panel. No such mapping is inferred. No superiority/noninferiority/equivalence margin, sample-size calculation, interim or stopping conclusion occurs in these assigned displays. Their decision-rule checks have no applicable local output.

The eight contributor totals in eTable 2 match eTable 1 exactly when summed over modes: after titration 309+110+33=452 and 362+73+28=463; day 1 129+225+37=391 and 214+164+32=410; day 2 61+211+49=321 and 68+223+52=343; day 3 46+181+45=272 and 42+192+62=296. These are contributors, not an invented per-variable measured sample size. The Other Mode footer explicitly defines that category; maximum versus plateau pressure is also defined by availability. After titration is a post-randomization occasion, not a pretreatment baseline.

For S241–S248, ABG denominators are printed explicitly, and the footer explains missing ABG measurements. All 16 fractions match their one-decimal percentages within display allowances. Respiratory acidosis requires both pHa<7.35 and PaCO2>45 mmHg. A labelled uncorrected Pearson chi-square diagnostic, chi-square=(a/n−c/m)^2/[p(1−p)(1/n+1/m)] with p=(a+c)/(n+m), gives respectively 25.241131, .736138, .133080, 4.858885, 56.037643, 8.740373, 2.139663 and 3.862067. One-degree-of-freedom asymptotic diagnostic P values are approximately 5.059e−7, .390901, .715260, .027504, 7.110e−14, .003112, .143533 and .049389. These reproduce the display-precision/significance readings and do not establish a row conflict. This diagnostic is not asserted as the authors' table-specific implementation; the source does not explicitly map a continuity correction or sparse-data implementation to these rows.

All nine matched figure panels agree in contrast and direction with the table. Eight display P<.001 in both places. S275 displays .027 in the figure and .03 in the table; their half-unit intervals overlap. No cross-source candidate is created by those matching copies.

## Complete-ledger and recheck implications

All nine stable IDs and their exact remaining human questions were read before closure. C001–C007 and C009 concern other assigned relationships or package-wide definitions, not independent numerical contradictions in these 120 tuples. In particular, S201–S320 respiratory-rate and pressure summaries are not the absent respiratory-rate VFD subgroup or mechanical-power mediation output in C006. Its classification is P_R only; the matrix reporting annotation is context, not a conflicting prospective plan. C007 concerns the VFD subgroup producing distribution, not these ventilator-summary P values. No new model-to-table mapping is inferred from either candidate.

For S313/C008, the source prints intermediate Other Mode PEEP 8 (5–1), low 5 (5–10), P=.50, with intermediate header 28. Median allowance [7.5,8.5], Q1 [4.5,5.5] and Q3 [.5,1.5] remain disjoint where containment/order require agreement. The admissible Q3 interval from the median is [7.5,infinity), giving a minimum gap 6 and relative discrepancy 6/1=6; Q1-to-Q3 gap is at least 3. Endpoint reversal still cannot contain the median. The current screen and recheck ground C008 in Route A category 2, without treating IQR as an effect CI. The intended Q3 is absent; no replacement value is selected. This existing screened observation is not re-emitted.

## Findings

No new F-ST2 finding is emitted. Every apparent issue reconsidered within the assigned scope either remains an existing screened issue or fails reproduction under an always-register category after the rules below.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 eTable 2 p6 PSV VT day 2 S275 versus eFigure 3 p12; eTable 1 p5 S242/S243 | Figure .027 allows [.0265,.0275] and table .03 allows [.025,.035], gap zero. For binary diagnostics .390901 versus .40, the point diagnostic to printed interval [.395,.405] gap is .004099/.40=.01025; .715260 versus .71 interval [.705,.715] gap is .000260/.71=.000367. Both are at most .05 even before count/input allowance. No estimate CI or test conflict is involved. This revisits the support-A pass-1 precision row and retains one consolidated pattern. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 eTables 1/2 pp5–6, median driving pressure, plateau pressure, PEEP, minute ventilation, tidal volume and respiratory rate | Separate marginal medians do not imply median driving pressure equals median plateau pressure minus median PEEP, or median minute ventilation equals the product of separate tidal-volume and respiratory-rate medians. No supplied identity or method reproducing the other rows establishes that arithmetic on marginal medians. This rereads the numeric checker's pp5–7 exclusion within the assigned pp5–6 scope; it does not screen out a reproduced category-4 row. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-003 SAP p12 versus REPORT DOC-004 eTables 1/2 pp5–6 and eFigures 2–4 pp11–13; REPORT DOC-001 pp4–5 | Seven-day planned longitudinal modeling and three-day descriptive tables/panels do not establish that the reported model used only three days: main p4 gives the longitudinal specification but no shorter fitted window. No claimed-prespecified analysis is absent from the plan, no primary/key-secondary analysis result is established as missing by these descriptive displays, and no changed window is stated. This consolidates the cross-source and main/plan pass-1 exclusions relevant to this shard. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 protocol p20 and DOC-003 SAP p6; REPORT DOC-001 p2 and DOC-004 table/figure arm legends | Higher/high versus intermediate describes the same comparator contrast: the plan gives 8–10 mL/kg PBW and main p2 starts the intermediate arm at 10 mL/kg PBW with the stated pressure limit; table/figure legends identify low versus intermediate consistently. The naming difference changes no printed number, direction or reference arm. This consolidates the cross-source and main/plan terminology exclusions relevant to this shard. | TERMINOLOGY_OR_WORDING |

No reproduced route-A observation is screened out above. Category 1 is not subjected to the numerical .05 relative rule; the precision row contains no confidence interval or null-test conflict. Category 3 count checks use the printed row denominators, not substituted headers. Category 4 cannot be established from arithmetic on distinct marginal medians. Category 5 is not inferred merely from three displayed descriptive occasions.

## Explicit pass-2 relationship closure

Each row below records the completed source reread, count/denominator, estimate/interval, P/test, method and matched-result implications. The paired statistics artifact retains the full source-linked printed tuples and these same explicit PASS_2_COMPLETE records. C means continuous-median/IQR reread with no new conflict; B means binary fraction/percentage and labelled test diagnostic reread with no new conflict; F means a matching figure panel was also reread; E means existing C008, not re-emitted. Missing per-row continuous test/model inputs are limitations, not substituted analyses.

| S ID | Pass-2 check outcome | Pass 2 |
|---|---|---|
| S201 | C; no new finding | PASS_2_COMPLETE |
| S202 | C; no new finding | PASS_2_COMPLETE |
| S203 | C; no new finding | PASS_2_COMPLETE |
| S204 | C; no new finding | PASS_2_COMPLETE |
| S205 | C; no new finding | PASS_2_COMPLETE |
| S206 | C; no new finding | PASS_2_COMPLETE |
| S207 | C; no new finding | PASS_2_COMPLETE |
| S208 | C; no new finding | PASS_2_COMPLETE |
| S209 | C; no new finding | PASS_2_COMPLETE |
| S210 | C; no new finding | PASS_2_COMPLETE |
| S211 | C; no new finding | PASS_2_COMPLETE |
| S212 | C; no new finding | PASS_2_COMPLETE |
| S213 | C; no new finding | PASS_2_COMPLETE |
| S214 | C; no new finding | PASS_2_COMPLETE |
| S215 | C; no new finding | PASS_2_COMPLETE |
| S216 | C; no new finding | PASS_2_COMPLETE |
| S217 | C; no new finding | PASS_2_COMPLETE |
| S218 | C; no new finding | PASS_2_COMPLETE |
| S219 | C; no new finding | PASS_2_COMPLETE |
| S220 | C; no new finding | PASS_2_COMPLETE |
| S221 | C; no new finding | PASS_2_COMPLETE |
| S222 | C; no new finding | PASS_2_COMPLETE |
| S223 | C; no new finding | PASS_2_COMPLETE |
| S224 | C; no new finding | PASS_2_COMPLETE |
| S225 | C; no new finding | PASS_2_COMPLETE |
| S226 | C; no new finding | PASS_2_COMPLETE |
| S227 | C; no new finding | PASS_2_COMPLETE |
| S228 | C; no new finding | PASS_2_COMPLETE |
| S229 | C; no new finding | PASS_2_COMPLETE |
| S230 | C; no new finding | PASS_2_COMPLETE |
| S231 | C; no new finding | PASS_2_COMPLETE |
| S232 | C; no new finding | PASS_2_COMPLETE |
| S233 | C; no new finding | PASS_2_COMPLETE |
| S234 | C; no new finding | PASS_2_COMPLETE |
| S235 | C; no new finding | PASS_2_COMPLETE |
| S236 | C; no new finding | PASS_2_COMPLETE |
| S237 | C; no new finding | PASS_2_COMPLETE |
| S238 | C; no new finding | PASS_2_COMPLETE |
| S239 | C; no new finding | PASS_2_COMPLETE |
| S240 | C; no new finding | PASS_2_COMPLETE |
| S241 | B; no new finding | PASS_2_COMPLETE |
| S242 | B; no new finding | PASS_2_COMPLETE |
| S243 | B; no new finding | PASS_2_COMPLETE |
| S244 | B; no new finding | PASS_2_COMPLETE |
| S245 | B; no new finding | PASS_2_COMPLETE |
| S246 | B; no new finding | PASS_2_COMPLETE |
| S247 | B; no new finding | PASS_2_COMPLETE |
| S248 | B; no new finding | PASS_2_COMPLETE |
| S249 | C; no new finding | PASS_2_COMPLETE |
| S250 | C, F; no new finding | PASS_2_COMPLETE |
| S251 | C, F; no new finding | PASS_2_COMPLETE |
| S252 | C, F; no new finding | PASS_2_COMPLETE |
| S253 | C; no new finding | PASS_2_COMPLETE |
| S254 | C; no new finding | PASS_2_COMPLETE |
| S255 | C; no new finding | PASS_2_COMPLETE |
| S256 | C; no new finding | PASS_2_COMPLETE |
| S257 | C; no new finding | PASS_2_COMPLETE |
| S258 | C; no new finding | PASS_2_COMPLETE |
| S259 | C; no new finding | PASS_2_COMPLETE |
| S260 | C; no new finding | PASS_2_COMPLETE |
| S261 | C; no new finding | PASS_2_COMPLETE |
| S262 | C; no new finding | PASS_2_COMPLETE |
| S263 | C; no new finding | PASS_2_COMPLETE |
| S264 | C; no new finding | PASS_2_COMPLETE |
| S265 | C; no new finding | PASS_2_COMPLETE |
| S266 | C; no new finding | PASS_2_COMPLETE |
| S267 | C; no new finding | PASS_2_COMPLETE |
| S268 | C; no new finding | PASS_2_COMPLETE |
| S269 | C; no new finding | PASS_2_COMPLETE |
| S270 | C; no new finding | PASS_2_COMPLETE |
| S271 | C; no new finding | PASS_2_COMPLETE |
| S272 | C; no new finding | PASS_2_COMPLETE |
| S273 | C; no new finding | PASS_2_COMPLETE |
| S274 | C, F; no new finding | PASS_2_COMPLETE |
| S275 | C, F; no new finding | PASS_2_COMPLETE |
| S276 | C, F; no new finding | PASS_2_COMPLETE |
| S277 | C; no new finding | PASS_2_COMPLETE |
| S278 | C; no new finding | PASS_2_COMPLETE |
| S279 | C; no new finding | PASS_2_COMPLETE |
| S280 | C; no new finding | PASS_2_COMPLETE |
| S281 | C; no new finding | PASS_2_COMPLETE |
| S282 | C; no new finding | PASS_2_COMPLETE |
| S283 | C; no new finding | PASS_2_COMPLETE |
| S284 | C; no new finding | PASS_2_COMPLETE |
| S285 | C; no new finding | PASS_2_COMPLETE |
| S286 | C; no new finding | PASS_2_COMPLETE |
| S287 | C; no new finding | PASS_2_COMPLETE |
| S288 | C; no new finding | PASS_2_COMPLETE |
| S289 | C; no new finding | PASS_2_COMPLETE |
| S290 | C; no new finding | PASS_2_COMPLETE |
| S291 | C; no new finding | PASS_2_COMPLETE |
| S292 | C; no new finding | PASS_2_COMPLETE |
| S293 | C; no new finding | PASS_2_COMPLETE |
| S294 | C, F; no new finding | PASS_2_COMPLETE |
| S295 | C, F; no new finding | PASS_2_COMPLETE |
| S296 | C, F; no new finding | PASS_2_COMPLETE |
| S297 | C; no new finding | PASS_2_COMPLETE |
| S298 | C; no new finding | PASS_2_COMPLETE |
| S299 | C; no new finding | PASS_2_COMPLETE |
| S300 | C; no new finding | PASS_2_COMPLETE |
| S301 | C; no new finding | PASS_2_COMPLETE |
| S302 | C; no new finding | PASS_2_COMPLETE |
| S303 | C; no new finding | PASS_2_COMPLETE |
| S304 | C; no new finding | PASS_2_COMPLETE |
| S305 | C; no new finding | PASS_2_COMPLETE |
| S306 | C; no new finding | PASS_2_COMPLETE |
| S307 | C; no new finding | PASS_2_COMPLETE |
| S308 | C; no new finding | PASS_2_COMPLETE |
| S309 | C; no new finding | PASS_2_COMPLETE |
| S310 | C; no new finding | PASS_2_COMPLETE |
| S311 | C; no new finding | PASS_2_COMPLETE |
| S312 | C; no new finding | PASS_2_COMPLETE |
| S313 | E; existing C008, 8 (5–1), gap 6, relative gap 6; no re-emission | PASS_2_COMPLETE |
| S314 | C; no new finding | PASS_2_COMPLETE |
| S315 | C; no new finding | PASS_2_COMPLETE |
| S316 | C; no new finding | PASS_2_COMPLETE |
| S317 | C; no new finding | PASS_2_COMPLETE |
| S318 | C; no new finding | PASS_2_COMPLETE |
| S319 | C; no new finding | PASS_2_COMPLETE |
| S320 | C; no new finding | PASS_2_COMPLETE |

## Provenance, limitations and handoff

New targeted derivative: preprocessing/st2-a-tables-layout.txt, direct Poppler pdftotext 25.03.0, CPU; command `pdftotext -layout -f 5 -l 6 joi180108supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/st2-a-tables-layout.txt`. No OCR was needed. The two-page extraction is a transcription aid checked against the supplied PDF's location and current exact-source p6 rendering; it is not an independent scientific source. Other exact-source rereads used selected-page stdout for main pp2/4, protocol p20 and SAP pp6/12. Current rendered assets inspected: preprocessing/recheck-results-p6.png and preprocessing/recheck-results-figure-11.png, -12.png and -13.png, direct Poppler pdftoppm 25.03.0, CPU, as documented in the mechanical recheck. No duplicated full appendix derivative was created.

No assigned source unit, tuple or matching panel remains uncovered. Exact reproduction of continuous P values remains unavailable because the individual observations, variable-specific measured sample sizes, row-to-test/model mapping, covariance, variance estimator and degrees of freedom are not supplied. These limits were recorded for every continuous tuple through outcome C or E and are not inferred from convention. The eight binary Pearson calculations are explicitly diagnostics; the exact table-specific sparse-data/continuity-correction procedure is not supplied. Curve coordinates were not digitized. C008's intended upper quartile remains the existing human question. No evidence state, adjudication, severity or correction was assigned by this pass.

Outputs: checkers/parts/statistical_pass_2_support_a.md and statistics/parts/pass2_support_a_closure.md. Both have exactly 120 explicit PASS_2_COMPLETE tuple rows. The coordinator can merge the closure records into the canonical relationship inventory without changing the pass-1 parts.


# Statistical pass 2 — support shard B

- Runtime agent ID: /root/statistics_pass2_support_b.
- Model / reasoning effort: gpt-6.1-sol / high.
- Start mode: FRESH_SPAWN; this runtime is different from every pass-1 runtime.
- Exact scope: DOC-004 REPORT, joi180108supp3_prod.pdf physical pages 7–9; S321–S438, all 72 eTable 3 mode/variable/occasion tuples, all 30 eTable 4 rows, and all 16 eTable 5 subgroup effect/95% CI rows with all eight shared interaction tests.
- Pass-2 closure: 118/118 relationships, each explicitly PASS_2_COMPLETE below and in statistics/parts/pass2_support_b_closure.md.
- New findings: 1, F-ST2-501. Excluded observations: 4 consolidated rows. Scientific coverage gaps: 0.

QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Pass 2 reread the complete current C001–C009 ledger, initial screening log, mechanical recheck, all assigned pass-1 relationship records, and all 35 Excluded observations rows across the numeric, cross-source and three statistical-pass-1 artifacts. Earlier review conclusions and the web were not scientific inputs.

Exact supplied pp7–9 were reread using direct Poppler 25.03.0 `pdftotext -layout -f 7 -l 9 joi180108supp3_prod.pdf -`; exact main REPORT pp4 and 6 and PLAN SAP p14 were likewise reread with selected-page direct layout stdout. Current source-matched recheck/screening extracts were used for searching relevant definitions. Visual reading used the current independently source-confirmed p9 recheck rendering and curator-matched reusable pp7–8 images. Existing render provenance is Poppler 25.03.0 CPU for preprocessing/recheck-results-p9.png and UNKNOWN_LEGACY_RENDERER for reused review_1_5_2/preprocessing/rendered_pages/joi180108supp3_prod-p7.png and -p8.png. No fresh derivative was necessary; supplied sources, reused assets, pass-1 parts and canonical inventory were preserved.

## Rules applied to every assigned record

**T3-CONT:** All 48 eTable 3 continuous tuples were source-matched for arm, mode and occasion. Each median is contained in its ordered IQR. These are marginal medians/IQRs, not effect CIs; overlap, equal rounded medians or separate marginal-summary arithmetic cannot determine the between-arm P value. Row-specific continuous tests, raw ranks, test statistics and SEs are absent. No unavailable model or normal/rank test was assumed.

**T3-COUNT:** All 24 eTable 3 binary tuples were reread for numerator, denominator, percentage, P attribution and endpoint definition. Each count is at most its denominator and each ABG denominator is at most the printed mode contributor count for that arm/occasion. Every percentage reconciles under the displayed-input/output half-unit allowances and 0.05 relative-gap cutoff, including the 74/264 versus 27.9% cell and 6/161 versus 3.8% cell. The table explicitly says that smaller ABG denominators reflect missing measurements. Arterial pH<7.25 and respiratory acidosis (pH<7.35 AND PaCO2>45) are distinct endpoints. Both-zero rows show a dash, not a positive-count contradiction. Exact binary test variants are not supplied for this display.

**T4-IQR:** Every eTable 4 median is contained in its ordered IQR. Equal rounded medians/IQRs do not imply equal raw distributions, including lowest RASS day 3 P=.01 and colloid-volume P=.97. P is not an IQR-null test. Row-specific tests, SEs, test statistics and raw distributions are absent. S415 additionally has the newly emitted duration-window finding.

**T4-COUNT:** Explicit fractions and the seven rescue-therapy count/header-denominator pairs reconcile under the half-unit rule. The four implicit-denominator use rows have the arithmetic gaps listed below, all screened by relative discrepancy at most 0.05. No available-data denominator was invented to reconcile them. Counts and percentages were checked within the display, rather than dismissed as peripheral descriptive results.

**T5:** All 16 subgroup estimates remain in ordered 95% CIs. Low-minus-intermediate direction agrees with the half-unit allowances of the displayed means and estimate. Only the ICU subgroup CI excludes zero. The eight P values test interaction between subgroup and randomized arm, not each subgroup's treatment effect. Main REPORT p4 establishes Gaussian GLMs, two-sided reported P, alpha .05, no multiplicity adjustment and exploratory secondary analyses. It does not give subgroup n, CI-producing estimator, link, covariates, covariance, variance estimator, degrees of freedom or the CI-to-interaction estimator mapping. Missing details alone are not findings. No noninferiority/equivalence margin, efficacy interim boundary or numerical stopping conclusion applies to these displays.

## Recheck and cross-lane implications

The full ledger/recheck was considered without re-emitting any already screened issue. C006 has P_R only: the matrix's in-paper annotation is not an opposing prospective PLAN. C006's absent respiratory-rate primary-VFD subgroup is not supplied by any eTable 3 respiratory measurement or by eTable 5's eight pairs. C007's prospective zero-inflated versus reported Gaussian subgroup model applies to all S423–S438 and remains a planned-versus-reported issue, with the disclosed change retained. C003's eligibility question contextualizes S427–S428 without claiming a changed subgroup count. C009's exact visual row-attribution question is preserved for S435–S436, with no inferred category assignment or subgroup n. C001's binary-RR identity does not transfer to these mean-difference or percentage rows. C004/C005's primary endpoint/model comparisons and C002/C008's separate source tuples yield no further conflict in the assigned displays.

The main p6 and eTable 5 ICU/outside-ICU effects, limits and interaction P agree numerically. Calling the matching limits IQR in narrative is already considered by the screening/recheck and does not create another interval-versus-test finding. The visual C009 reading remains exactly as rechecked. No complete-case, randomization denominator, subgroup sample size, covariance or variance estimator was inferred from clinical convention.

## Recalculated display-precision check for the eight implicit percentages

For count a, header n and percentage p, recomputed percentage interval is [100(a−.5)/(n+.5), 100(a+.5)/(n−.5)]; p has ±.05 percentage-point allowance. Values below are independently recalculated.

| eTable 4 arm/row | Printed count/header and % | Recomputed interval (%) | Remaining gap / printed % |
|---|---|---|---:|
| Low sedative | 320/477; 70.6 | [66.910995,67.261280] | .046582 |
| Intermediate sedative | 333/484; 72.1 | [68.627451,68.976215] | .042632 |
| Low analgesic | 277/477; 61.1 | [57.905759,58.237146] | .046037 |
| Intermediate analgesic | 273/484; 59.1 | [56.243550,56.566701] | .042019 |
| Low neuromuscular blockade | 53/477; 11.7 | [10.994764,11.227702] | .036094 |
| Intermediate neuromuscular blockade | 60/484; 13.0 | [12.280702,12.512927] | .033621 |
| Low vasopressor | 363/477; 80.0 | [75.916230,76.285414] | .045807 |
| Intermediate vasopressor | 353/484; 76.4 | [72.755418,73.112720] | .042373 |

These are at most .05, so no reproduced route-A category-3 observation remains. This conclusion follows the numerical precision rule, not an assumption that these rows use smaller denominators.

## Shared interaction-test diagnostic review

The following is a **diagnostic approximation only**: derive SE from each CI width/3.92 and assume independent normal subgroup contrasts, giving z=|MD1−MD2|/sqrt(SE1²+SE2²), then a two-sided normal P. The half-unit ranges allow each printed MD and endpoint ±.005; 3.92 is held fixed as part of the diagnostic. No diagnostic is substituted for the reported Gaussian GLM.

| Shared S pair / subgroup | Printed interaction P | Diagnostic P | Diagnostic range from displayed MD/CI inputs |
|---|---:|---:|---|
| S423/S424 pneumonia | .16 | .473232 | [.469184,.477284] |
| S425/S426 sepsis | .17 | .187943 | [.185337,.190567] |
| S427/S428 oxygenation | .32 | .318242 | [.314467,.322031] |
| S429/S430 LIPS | .96 | .958165 | [.952831,.963477] |
| S431/S432 admission | .23 | .203439 | [.200747,.206147] |
| S433/S434 SAPS II | .26 | .254384 | [.250286,.258508] |
| S435/S436 prior ventilation | .98 | .981895 | [.979615,.984172] |
| S437/S438 intubation location | .01 | .007769 | [.007469,.008079] |

For pneumonia, the diagnostic SEs are 6.68/3.92=1.704082 and 3.26/3.92=.831633; contrast 1.36 gives z=.717231 and P≈.473232. Source P=.16 remains a different printed interaction test, and its two constituent subgroup CIs both include zero. Comparing that interaction P with either subgroup CI would compare different null hypotheses. The source does not establish that the pairwise-independent CI-width contrast is the interaction estimator. Numerical agreement for several other pairs is not evidence of the missing covariance/estimator mapping; sepsis and admission also differ under this diagnostic. Route A category 4 concerns a printed estimate or interval that a reproducing method does not reproduce; this diagnostic instead calculates a P under additional assumptions and does not reproduce a source-supported estimate/interval construction. Category 1 would apply to a reproduced interval/test conflict, but the two separate subgroup-effect CIs are not a CI for their interaction, and no source-supported compatibility conflict is established. The exclusion is therefore based on an assumed additional analysis relationship, not on dismissing a reproduced conflict because its production mechanism is unavailable.

## Prior checker exclusion reread

All 35 rows were independently reread against route A categories 1–5 and the display-precision rule: numeric 6; cross-source 14; statistical pass 1 main/plan 10; support A 1; support B 4. Source tuples outside S321–S438 remain owned by the other fresh pass-2 shards; their source-level closure is not claimed here. This shard independently revisited the eTable 4 count/percentage rows, eTable 5 pneumonia diagnostic and interval terminology, clinical/medical category wording, three-day display versus longer descriptive plan, the “35.” percentage, and empty dispersion parenthesis. None of those prior excluded rows establishes an additional reproduced always-register observation in this assigned scope. The newly found S415 numerical duration/window question was not a prior exclusion and is emitted below.

## Findings

### F-ST2-501

**Title:** The reported vasopressor-duration quartile leaves its time window unclear.

**Relationships:** S415.

**Exact locations and document roles:** REPORT [DOC-004 results supplement, physical p8, eTable 4 title, “Days of vasopressor use” row in both treatment arms, and median/interquartile-range footer](../../../joi180108supp3_prod.pdf#page=8). The same REPORT's [physical p7, eTable 3 title and four occasion headings](../../../joi180108supp3_prod.pdf#page=7) supplies a source-grounded alternative counting convention, not a second conflicting document. Both compared title and numerical row are REPORT within the results supplement.

**Printed values:** The eTable 4 title says “during the first three days.” “Days of vasopressor use” is 2 (1–4) in the low arm and 2 (1–4) in the intermediate arm, with P=.87. Its footer defines the summaries as median (interquartile range). The vasopressor footnote defines the qualifying drugs/dose but supplies no duration-counting rule or separate window for this row.

**Rule and calculation:** An accumulated duration confined to three elapsed days is bounded by 3 days, so its upper quartile cannot exceed 3. The upper-quartile reading 4 permits [3.5,4.5] under half-unit display allowances. The admissible upper-quartile interval for a duration bounded by 3 is [0,3], leaving gap 3.5−3=0.5 days, and relative discrepancy 0.5/4=0.125, above 0.05. The title describes a specified observation window, not a rounded numerical estimate; its three-day window is not enlarged by rounding. This calculation establishes the consequence of the printed elapsed-duration reading; it does not assert that the authors counted elapsed days rather than calendar days. The median and quartile endpoints are ordered and contain the median, and no conflict with P=.87 is asserted.

**Focus area:** C, an analysis description unclear about the time window/counting unit producing a printed duration; B, time-window attribution of a quantitative result.

**Proposed review domain:** report_internal_inconsistency.

**Proposed relationship type / all relationships:** S_W / S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The low- and intermediate-arm vasopressor-duration distributions 2 (1–4) days, particularly whether the extracted 4-day upper quartile describes a three-day truncated elapsed duration, a count of calendar days touched, or a longer treatment course.

**Why context does not resolve it:** The title supplies a three-day horizon, while the printed upper quartile is four days. The nearby sedative, analgesic and neuromuscular-blockade duration rows do not identify an alternative rule for vasopressors. eTable 3, under a similar first-three-days title, lists the randomization-day occasion separately from days 1–3; that makes calendar-day counting or an additional partial day a plausible alternative, but does not define how eTable 4's duration was calculated. The footer gives the summary type only, and the vasopressor footnote gives the drug/dose definition only. This quantity-to-window assignment affects the duration a reader extracts, rather than merely varying the wording of the same unambiguous quantity. The quantity-changing-label comparison is in scope.

**Alternatives and missing definition:** Counting every calendar date with vasopressor exposure, including the randomization date plus days 1–3, could yield four counted dates without exceeding three elapsed days. The row could instead summarize a longer treatment course despite the table-wide title, or the intended quartile/title could differ. No alternative is chosen. Needed definitions are the row's exposure-window start/end and whether “days” means elapsed time or calendar dates touched. This is separate from screened F-XS-007: it compares a supplied numerical vasopressor quartile with its own table's horizon, not a planned full-course sedative/blocker endpoint with a reported partial-period summary.

**Exact human question:** What exposure window and counting rule produced the “Days of vasopressor use” summaries 2 (1–4) in both arms of eTable 4, and how does the 4-day upper quartile relate to the table's stated first-three-day horizon?

## Excluded observations

Only apparent issues decided not to emit appear here; checks that reconcile and already screened findings are in their relationship records.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 p8 eTable 4, four use rows, both arms | All eight count/header/percentage gaps independently recomputed above remain at most .05 after half-unit allowances. They therefore do not meet reproduced route A category 3. Consolidates the numeric and support-B pass-1 occurrences. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 p9 eTable 5, eight pairs, particularly S423/S424; REPORT main p4 method | Independent normal CI-width interaction diagnostic ≈.473 versus pneumonia P=.16 is not a source-supported estimator linkage. No interaction CI is printed; individual subgroup CIs and the shared interaction P test different nulls. The diagnostic table and named missing mappings above explain why no category-1 or category-4 conflict is reproduced. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 p7 eTable 3 Other mode, after-titration respiratory acidosis | Printed “35.” for 7/20 has unambiguous numerical reading 35%, with no changed number or magnitude. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-004 p9 eTable 5 footer | Empty parentheses in “Data are mean ()” do not alter the mean, ± dispersion entries or separately defined mean-difference 95% CIs. No numerical conflict follows from the missing dispersion abbreviation. | NOTATION_OR_TYPOGRAPHY |

## Explicit relationship closure

Every row records completion even where a producing-analysis definition is absent. The rules and precise missing definitions are given above; absent inputs were not supplied by convention.

| S ID | Exact REPORT source / row | Occasion | Pass 2 record |
|---|---|---|---|
| S321 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S322 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S323 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S324 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S325 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S326 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S327 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S328 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S329 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S330 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S331 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S332 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S333 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S334 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S335 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S336 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S337 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S338 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S339 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S340 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S341 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S342 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S343 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S344 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S345 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S346 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S347 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S348 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S349 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S350 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S351 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S352 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S353 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S354 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S355 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S356 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S357 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S358 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S359 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S360 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S361 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S362 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S363 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S364 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S365 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S366 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S367 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S368 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S369 | [DOC-004 p7 eTable 3 Other, FiO2](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S370 | [DOC-004 p7 eTable 3 Other, FiO2](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S371 | [DOC-004 p7 eTable 3 Other, FiO2](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S372 | [DOC-004 p7 eTable 3 Other, FiO2](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S373 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S374 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S375 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S376 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S377 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S378 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S379 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S380 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S381 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S382 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S383 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S384 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S385 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S386 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S387 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S388 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S389 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S390 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S391 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S392 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S393 | [DOC-004 p8 eTable 4 Sedative infusion](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; recalculated implicit count/header gap≤.05; no new finding |
| S394 | [DOC-004 p8 eTable 4 Days sedative administration](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S395 | [DOC-004 p8 eTable 4 Analgesic infusion](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; recalculated implicit count/header gap≤.05; no new finding |
| S396 | [DOC-004 p8 eTable 4 Days analgesic administration](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S397 | [DOC-004 p8 eTable 4 Lowest RASS day 1](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S398 | [DOC-004 p8 eTable 4 Lowest RASS day 2](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S399 | [DOC-004 p8 eTable 4 Lowest RASS day 3](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S400 | [DOC-004 p8 eTable 4 Neuromuscular blockade](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; recalculated implicit count/header gap≤.05; no new finding |
| S401 | [DOC-004 p8 eTable 4 Days neuromuscular blockade](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S402 | [DOC-004 p8 eTable 4 Fluid balance 24h day 1 mL](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S403 | [DOC-004 p8 eTable 4 Fluid balance 24h day 2 mL](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S404 | [DOC-004 p8 eTable 4 Fluid balance 24h day 3 mL](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S405 | [DOC-004 p8 eTable 4 Use colloids](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S406 | [DOC-004 p8 eTable 4 Volume colloids](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S407 | [DOC-004 p8 eTable 4 Volume crystalloids](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S408 | [DOC-004 p8 eTable 4 Transfusion red blood cells](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S409 | [DOC-004 p8 eTable 4 Units red blood cells](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S410 | [DOC-004 p8 eTable 4 Transfusion fresh frozen plasma](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S411 | [DOC-004 p8 eTable 4 Units fresh frozen plasma](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S412 | [DOC-004 p8 eTable 4 Transfusion platelets](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S413 | [DOC-004 p8 eTable 4 Units platelets](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S414 | [DOC-004 p8 eTable 4 Use vasopressors](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; recalculated implicit count/header gap≤.05; no new finding |
| S415 | [DOC-004 p8 eTable 4 Days vasopressors](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; ordered IQR; F-ST2-501 time-window question |
| S416 | [DOC-004 p8 eTable 4 Decreasing instrumental dead space](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S417 | [DOC-004 p8 eTable 4 Recruitment maneuvers](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S418 | [DOC-004 p8 eTable 4 Prone positioning](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S419 | [DOC-004 p8 eTable 4 Inhaled nitric oxide](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S420 | [DOC-004 p8 eTable 4 High frequency oscillatory ventilation](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S421 | [DOC-004 p8 eTable 4 Extracorporeal membrane oxygenation](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S422 | [DOC-004 p8 eTable 4 Extracorporeal CO2 removal](../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S423 | [DOC-004 p9 eTable 5 Pneumonia](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S424 | [DOC-004 p9 eTable 5 Non-Pneumonia](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S425 | [DOC-004 p9 eTable 5 Sepsis yes](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S426 | [DOC-004 p9 eTable 5 Sepsis no](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S427 | [DOC-004 p9 eTable 5 PaO2/FiO2 ≤200](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context; C003 eligibility context |
| S428 | [DOC-004 p9 eTable 5 PaO2/FiO2 >200](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context; C003 eligibility context |
| S429 | [DOC-004 p9 eTable 5 LIPS ≥4](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S430 | [DOC-004 p9 eTable 5 LIPS <4](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S431 | [DOC-004 p9 eTable 5 Admission clinical](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S432 | [DOC-004 p9 eTable 5 Admission surgical](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S433 | [DOC-004 p9 eTable 5 SAPS II ≥50](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S434 | [DOC-004 p9 eTable 5 SAPS II <50](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S435 | [DOC-004 p9 eTable 5 Pre-randomization ventilation numerical line 1; duration label displaced](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context; C009 retained attribution question; no category assignment |
| S436 | [DOC-004 p9 eTable 5 Pre-randomization ventilation numerical line 2; printed beside >6 h](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context; C009 retained attribution question; no category assignment |
| S437 | [DOC-004 p9 eTable 5 Start ventilation ICU](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S438 | [DOC-004 p9 eTable 5 Start ventilation outside ICU](../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |

## Limitations and completion

118/118 S records and all eight shared interaction tests revisited. One new source-grounded finding, four excluded-observation rows, zero scientific coverage gaps. Intrinsic missing definitions remain row-specific continuous/sparse tests, subgroup n, CI-producing methods, interaction estimator mapping/link/covariance/variance/df, and S415 duration window/counting rule. No source or historical asset was modified, no web/legacy scientific conclusion was used, and canonical inventory updates are left to the coordinator.




