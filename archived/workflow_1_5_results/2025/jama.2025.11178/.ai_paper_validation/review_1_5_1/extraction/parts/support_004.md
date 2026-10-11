# Support quantitative evidence mapping — support-004

## Scope, authority, and extraction method

Assigned, complete, disjoint source scope: DOC-003 (`joi250046supp2_prod_1755300121.15087.pdf`) PDF pp. 20-29; DOC-004 (`joi250046supp3_prod_1755300121.15087.pdf`) PDF pp. 1-7; and DOC-005 (`joi250046supp4_prod_1755300121.15587.pdf`) PDF pp. 1-14. This is 31 source pages (10 + 7 + 14).

DOC-003 pp. 20-29 were mapped from the direct PDF. Its native text extraction has a font-encoding defect; direct rendered-page inspection was used for the result/statistics pages and readable portions of direct layout text were used only as a locator. DOC-004 pp. 1-7 were freshly mapped from direct layout text. DOC-005 pp. 2-11 and 13-14 use the curated usable normalized text as a locator and were mapped to the direct PDF; p. 1 was freshly directly extracted; p. 12 was directly rendered because the reusable native extraction is sparse. DOC-005 p. 12 is a deliberately blank continuation page (only publisher copyright line), so has no result-relevant content.

This artifact is an evidence map, not a candidate diagnosis or adjudication. Local relationship labels are shard-local and intentionally do not assign package-wide N/S identifiers.

## Per-page coverage

| Source / page | Coverage / content | Result-relevant mapping status |
|---|---|---|
| DOC-003 p. 20 | Demographics/baseline characteristics and start of primary effectiveness analysis | MAPPED: SAP-D3-R01 to R03 |
| DOC-003 p. 21 | Primary model definition, intervention enhancement sensitivity analysis, secondary-outcome analysis | MAPPED: SAP-D3-R04 to R06 |
| DOC-003 p. 22 | Moderator/subgroup analyses and mediation-analysis introduction | MAPPED: SAP-D3-R07 to R08 |
| DOC-003 p. 23 | Mediation model and treatment-effect decomposition | MAPPED: SAP-D3-R09 |
| DOC-003 p. 24 | Economic evaluation plan | MAPPED: SAP-D3-R10 |
| DOC-003 p. 25 | Health-care cost categories/definitions | MAPPED: SAP-D3-R11 |
| DOC-003 p. 26 | Serious adverse event monitoring plan | MAPPED: SAP-D3-R12 |
| DOC-003 p. 27 | DSMB monitoring/procedures | NO APPLICABLE RESULT-RELEVANT QUANTITATIVE RELATIONSHIP; administrative safety monitoring only |
| DOC-003 p. 28 | References | NO APPLICABLE RESULT-RELEVANT QUANTITATIVE RELATIONSHIP |
| DOC-003 p. 29 | References | NO APPLICABLE RESULT-RELEVANT QUANTITATIVE RELATIONSHIP |
| DOC-004 p. 1 | TIDieR supplement title/front matter | NO APPLICABLE RESULT-RELEVANT QUANTITATIVE RELATIONSHIP |
| DOC-004 p. 2 | Intervention descriptions: why/materials/procedures | MAPPED: TIDIER-D4-R01 |
| DOC-004 p. 3 | Continuation of materials/staff/procedures | MAPPED: TIDIER-D4-R02 |
| DOC-004 p. 4 | Training and intervention delivery | MAPPED: TIDIER-D4-R03 |
| DOC-004 p. 5 | Engagement-contact and access details | MAPPED: TIDIER-D4-R04 |
| DOC-004 p. 6 | Intervention fidelity/actual implementation | MAPPED: TIDIER-D4-R05 |
| DOC-004 p. 7 | References | NO APPLICABLE RESULT-RELEVANT QUANTITATIVE RELATIONSHIP |
| DOC-005 p. 1 | Supplement title/front matter | NO APPLICABLE RESULT-RELEVANT QUANTITATIVE RELATIONSHIP |
| DOC-005 p. 2 | Outcome-measure definitions/scales | MAPPED: RES-D5-R01 to R06 |
| DOC-005 p. 3 | Intervention-adherence eFigure 1 caption | MAPPED: RES-D5-R07 |
| DOC-005 p. 4 | Missing-data criteria, observed missingness, imputation definition | MAPPED: RES-D5-R08 to R10 |
| DOC-005 p. 5 | Imputation/weighted GEE estimation and nonresponse weighting | MAPPED: RES-D5-R11 to R12 |
| DOC-005 p. 6 | Weight-model continuation | MAPPED: RES-D5-R13 |
| DOC-005 p. 7 | eTables 1-2: follow-up patterns and covariate selection | MAPPED: RES-D5-R14 to R15 |
| DOC-005 p. 8 | eTable 3: imputation step-1 model | MAPPED: RES-D5-R16 |
| DOC-005 p. 9 | eTable 4: weighted primary estimation model | MAPPED: RES-D5-R17 |
| DOC-005 p. 10 | eTables 5-6: nonresponse logistic model and weights | MAPPED: RES-D5-R18 |
| DOC-005 p. 11 | eTable 7: complete-case and extreme-assumption sensitivity analyses | MAPPED: RES-D5-R19 |
| DOC-005 p. 12 | Blank copyright continuation page; direct rendered source confirms no table/figure/text | NO APPLICABLE RESULT-RELEVANT QUANTITATIVE RELATIONSHIP |
| DOC-005 p. 13 | Protocol-change subset-analysis definition | MAPPED: RES-D5-R20 |
| DOC-005 p. 14 | eTable 8: protocol-change subset results | MAPPED: RES-D5-R21 |

## DOC-003 SAP relationships (direct PDF pp. 20-29)

- **SAP-D3-R01 — baseline descriptive definitions (p. 20).** Age, sex, race, and ethnicity will be summarized by treatment group. Continuous variables use mean, median, SD, minimum, and maximum; categorical variables use frequencies, percentages, and tabulations. Baseline means pre-randomization function/symptom scores, comorbidity and predictors of outcomes, moderation, or dropout.
- **SAP-D3-R02 — prespecified subgroup cut points (p. 20).** Sex (male); age >=65 years; race/ethnicity (White/non-Hispanic, Black or African American/non-Hispanic, Hispanic, Other); rural/medically underserved residence; multiple pain conditions (>1 by ICD diagnosis); mood disorder (anxiety/depression by ICD diagnosis); and negative/poor social determinants of health.
- **SAP-D3-R03 — primary outcome/hypotheses (p. 20).** Primary endpoint is MCID, defined as a 30% reduction in overall BPI-SF pain-severity score, at 3 months. Hypotheses expect both painTRAINER and virtual coach-led CBT-CP to have a higher proportion reaching MCID than usual care at 3 months; the analogous 6- and 12-month hypotheses are secondary-time-point hypotheses.
- **SAP-D3-R04 — primary inferential model (pp. 20-21).** Binary MCID at 3, 6, and 12 months is modeled with modified Poisson regression (Poisson family, log link) using GEE, independent working correlation, and robust sandwich SEs. The model accommodates within-person and within-health-coach correlation, includes intervention-by-time interactions, and treats usual care and 3 months as references. Adjustment variables: baseline pain severity; stratification variables sex, clinical site, rural/medically underserved residence; and a-priori predictors multisite pain and co-occurring mental-health condition. The direct formula is `log(E(Yij)) = beta0 + beta1 Int1i + beta2 Int2i + beta3 T6ij + beta4 T12ij + beta5 Int1i*T6ij + beta6 Int2i*T6ij + beta7 Int1i*T12ij + beta8 Int2i*T12ij + betaz Zi`.
- **SAP-D3-R05 — intervention enhancement and analysis population (p. 21).** The painTRAINER engagement enhancement (motivational-interviewing language in onboarding) was implemented 2021-08-09 after approximately 140 participants had enrolled; planned sensitivity analysis repeats primary analysis among those randomized after that date. All analyses use ITT, including all randomized individuals regardless of engagement/exposure.
- **SAP-D3-R06 — secondary outcomes/models (p. 21).** Secondary outcomes: overall pain severity, pain intensity (MCID and overall), pain-related interference (MCID and overall), social-role function, physical function, and patient global impression of change. Continuous outcomes use linear regression; binary/count outcomes use Poisson regression; longitudinal estimates use GEE with independent working correlation and robust sandwich SEs, intervention-by-time interaction, 3-month primary secondary endpoint, and baseline pain severity plus all stratification variables as covariates.
- **SAP-D3-R07 — moderator/subgroup scope (p. 22).** Prespecified heterogeneity analyses cover sex, age, race/ethnicity, rural/medically underserved residence, multiple pain conditions, mood disorders, and negative social determinants. The source specifies a subgroup-interaction analysis structure but no result values on this page.
- **SAP-D3-R08 — mediator-analysis scope (p. 22).** The SAP introduces analysis of mediators of intervention effect; no achieved numeric result is reported here.
- **SAP-D3-R09 — mediation analysis model (p. 23).** Mediator change from baseline to 6 months is modeled with linear regression. The stated next step estimates reduction in treatment effect after removing mediator effect; this is a planned decomposition, not a reported effect estimate.
- **SAP-D3-R10 — economic-evaluation estimands (p. 24).** Planned economic evaluation estimates incremental cost per additional patient attaining MCID (30% BPI pain-severity reduction) at 12 months and quality-adjusted life-years using the EQ-5D-5L. Cost-effectiveness uses a net-benefits framework across willingness-to-pay values; subgroup net-benefit regression and sensitivity analyses are planned. These are definitions/plans, not results.
- **SAP-D3-R11 — cost categories (p. 25).** Pain-related medications are classified by medication class (including opioids); pain-related in-person encounters use ICD-10 diagnostic codes. Categories include primary care, occupational therapy, physical therapy, and specialist medical care. These labels define cost inputs, not displayed results.
- **SAP-D3-R12 — safety-event monitoring (p. 26).** Given sample size, inpatient hospitalizations and deaths may occur; prior behavioral-intervention trials did not identify study-related serious adverse events. The page specifies monitoring/recording procedure, not event counts or comparative safety results.

## DOC-004 intervention implementation relationships (direct PDF pp. 1-7)

- **TIDIER-D4-R01 — intervention dose/procedure (pp. 2-3).** painTRAINER provides eight self-completed online sessions, 30-45 minutes each. Health Coach provides eight one-to-one sessions, 45-60 minutes each, by telephone/videoconference according to participant preference. The control is usual care plus resource material.
- **TIDIER-D4-R02 — training quantity/fidelity thresholds (pp. 3-4).** Health-coach training includes 16 practice sessions (two for each of eight sessions); proficiency requires 100% fidelity for session content and 80% fidelity for core CBT skills. This is an implementation threshold, not an outcome estimate.
- **TIDIER-D4-R03 — online-program access/engagement (p. 4).** Participants had 12-month access. The engagement process includes outreach when registration/session 1 has not occurred within the stated interval; no comparative efficacy result is displayed here.
- **TIDIER-D4-R04 — observed outreach (p. 5).** Of 776 painTRAINER-assigned participants, 356 (45.9%) completed an outreach call. For these 356, mean completed outreach calls was 1.8 (range 1-7) and mean call length was 4 minutes.
- **TIDIER-D4-R05 — observed coach-session fidelity (p. 6).** 299 of 4,626 completed sessions were reviewed (6.5%): 193 training-to-proficiency sessions (5%) and 106 later sessions (5%). Eight of 299 sessions required redo for session-content fidelity (2.7%); 11 of 299 did not reach the 80% CBT-principles fidelity criterion (3.7%).

## DOC-005 outcome definitions, models, and results (direct PDF pp. 1-14)

- **RES-D5-R01 — pain outcomes/MCID (p. 2).** Overall pain-severity score is mean of 11 modified BPI-SF items (0-10; higher=worse); pain intensity is mean of 4 BPI-SF items (0-10; higher=worse); pain-related interference is mean of 7 BPI-SF items (0-10; higher=worse). MCID is >=30% decrease from baseline in pain score.
- **RES-D5-R02 — PHQ-8 (p. 2).** Sum of eight 0-3 items, range 0-24, higher=worse depression; cut points 10 moderate, 15 moderately severe, 20 severe.
- **RES-D5-R03 — GAD-7 (p. 2).** Sum of seven 0-3 items, range 0-21, higher=worse anxiety; cut points 5 mild, 10 moderate, 15 severe.
- **RES-D5-R04 — PROMIS sleep (p. 2).** Six 1-5 items are summed and converted to T-score (mean 50, SD 10); higher=worse sleep disturbance. T-score >=60 indicates moderate (60-70) to severe (>70) disturbance.
- **RES-D5-R05 — PROMIS social roles (p. 2).** Four 1-5 items are summed/converted to T-score (mean 50, SD 10); higher=better participation. T-score <=40 indicates moderate (40-30) to severe (<30) limitation.
- **RES-D5-R06 — PROMIS physical function (p. 2).** Six 1-5 items are summed/converted to T-score (mean 50, SD 10); higher=better function. T-score <=40 indicates moderate (40-30) to severe (<30) limitation.
- **RES-D5-R07 — adherence figure (p. 3).** eFigure 1 is a histogram of completed-session counts among painTRAINER and Virtual Health Coach participants. The page contains the figure caption but no tabulated numeric values in the reusable text.
- **RES-D5-R08 — missing-data trigger and completeness (p. 4).** SAP trigger for MNAR imputation plus nonresponse weighting: 3-month primary-outcome missingness >15% or differential by arm. 3-month completeness: 1,798/2,331 (77.1%) overall; UC 621/777 (79.9%), PT 542/776 (69.8%), HC 635/778 (81.6%). All three time points observed: 1,568/2,331 (67.3%); missing every follow-up: 295/2,331 (12.7%).
- **RES-D5-R09 — missing-pattern/imputation model (pp. 4-5).** Among participants with any follow-up: one observed follow-up 8.1%, two 12.1%, three 67.3%. Step-1 pattern-mixture GEE linear model imputes change in pain severity with arm, time, arm-by-time, outcome-observation pattern, pattern-by-arm, and specified covariates; independent correlation/robust SEs account for coach clustering and repeated observations. Missing baseline covariates are imputed with available-data population means.
- **RES-D5-R10 — covariate-selection rule (p. 4).** Candidate covariate enters imputation/estimation model if, in separate logistic missingness and modified-Poisson MCID models adjusted for base factors, it is significant at 0.10 in both. This is a model-selection definition.
- **RES-D5-R11 — primary weighted estimator (p. 5).** Step 2 fits binary MCID on the imputed data using Poisson GEE with robust sandwich SEs. The nonresponse model is logistic for having >=1 follow-up; predictors include arm, base covariates, and covariates associated with both MCID and follow-up. Predicted probabilities form scaled analysis weights; stated purpose is ATE among all randomized people.
- **RES-D5-R12 — all-follow-up missingness by arm (p. 5).** No follow-up: UC 74/777 (9.5%), PT 133/776 (17.1%), HC 88/778 (11.3%), total 295/2,331 (12.7%).
- **RES-D5-R13 — weight-model outputs referenced (p. 6).** eTable 5 contains the fitted weight model; eTable 6/eFigure 1 summarize predicted probabilities/weights.
- **RES-D5-R14 — eTable 1 follow-up counts (p. 7).** Randomized total 2,331 (UC 777, PT 776, HC 778). Follow-up 3/6/12 months: 1,798/1,790/1,861 overall (77.1%/76.8%/79.8%); UC 621/622/639; PT 542/547/583; HC 635/621/639. At least one follow-up 2,036 (87.3%; UC 703, PT 643, HC 690). One/two/three observed follow-ups: 188/283/1,568 overall.
- **RES-D5-R15 — eTable 2 covariates (p. 7).** Base model includes arm, sex, age, site, rural/underserved residence, multisite pain, and co-occurring mental-health conditions. Final added imputation/estimation covariates: education and unemployment. Final added weight covariates: PEG, PHQ-8, GAD-7, any negative SDOH, and education.
- **RES-D5-R16 — eTable 3 imputation step 1 (p. 8).** Linear outcome change in pain severity: 6,108 observations, 2,036 persons, 659 missing values. Key estimates (95% CI; P): intercept -1.24 (-1.42,-1.06; <.001); PT vs UC 0.49 (0.39,0.59; <.001); HC vs UC 0.45 (0.36,0.54; <.001); 6 months 0.13 (0.07,0.19; .025); 12 months 0.31 (0.24,0.38; <.001). Full table additionally reports pattern, interaction, baseline-adjustment and demographic covariates, with displayed CIs/P values.
- **RES-D5-R17 — eTable 4 primary weighted estimator (p. 9).** Poisson model, binary 30% pain-severity improvement: 6,108 observations, 2,036 persons, sum of weights 6,108. At 3 months: PT vs UC RR 1.28 (1.06-1.55; .010); HC vs UC 1.54 (1.30-1.82; <.001); HC vs PT 1.20 (1.03-1.40; .019). At 6 months: PT vs UC 1.44 (1.21-1.70; <.001); HC vs UC 1.62 (1.39-1.90; <.001); HC vs PT 1.13 (0.98-1.30; .086). At 12 months: PT vs UC 1.32 (1.13-1.54; <.001); HC vs UC 1.41 (1.25-1.59; <.001); HC vs PT 1.07 (0.96-1.19; .215). The table also presents adjustment-covariate RRs/CIs/P values.
- **RES-D5-R18 — eTables 5-6 weight model (p. 10).** Logistic outcome is any observed follow-up. Versus PT: UC OR 2.05 (1.50-2.79; <.001), HC OR 1.68 (1.25-2.26; <.001); c-statistic 0.679. Predicted follow-up probability mean 0.88, SD 0.07, min 0.50, P25/P50/P75 0.85/0.90/0.93, max 0.98. Analysis weights: sum 2,036, mean 1.00, SD 0.09, min 0.89, P25/P50/P75 0.94/0.97/1.03, max 1.75.
- **RES-D5-R19 — eTable 7 prespecified missing-data sensitivity results (p. 11).** Complete-case set at 3 months n=1,798 (UC=621, PT=542, HC=635); extreme worst/best-case set n=2,331 (UC=777, PT=776, HC=778). Table gives adjusted MCID percentages, RR (95% CI), omnibus Wald P, and NNT (95% CI) at 3/6/12 months. Complete-case 3-month adjusted % PT/HC/UC = 32.2/35.5/24.0, RR PT-UC 1.34 (1.12-1.61), HC-UC 1.48 (1.24-1.75), HC-PT 1.10 (0.94-1.29), omnibus P<.001. Worst/best-case 3-month % = 22.7/29.3/39.4, RRs 0.58 (0.49-0.67), 0.74 (0.65-0.85), and 1.29 (1.09-1.52), omnibus P<.001. Footnotes define GEE modified-Poisson adjusted means/RRs, omnibus Wald test, and NNT/NNH interpretation when risk-difference CI crosses zero.
- **RES-D5-R20 — protocol-change subsets (p. 13).** painTRAINER engagement enhancement began 2021-08-09 after 454 enrolled; prespecified subset restricts to later randomization. Follow-up-letter analysis, after 2022-03-31, is post hoc; stated later follow-up was 82.7% at 3 months and 90.1% with >=1 follow-up.
- **RES-D5-R21 — eTable 8 subset results (p. 14).** Three subsets with adjusted MCID %, RRs (95% CI), omnibus P, and NNT: pre-enhancement (N=454; 366 >=1 follow-up; 3-month UC/PT/HC=152/149/153), enhancement (N=1,877; 1,670 >=1; UC/PT/HC=512/448/527), and reminder-letter (N=1,038; 935 >=1; UC/PT/HC=296/262/300). At 3 months, respectively: pre-enhancement PT/HC/UC 20.5/28.5/21.3; RR PT-UC 0.96 (0.59-1.57), HC-UC 1.34 (0.92-1.95), P=.138. Enhancement 28.0/32.7/20.4; RR 1.37 (1.11-1.69), 1.60 (1.33-1.93), P<.001. Reminder letters 31.6/34.1/20.5; RR 1.54 (1.18-2.01), 1.67 (1.30-2.14), P<.001. Table provides corresponding 6- and 12-month estimates and repeats the modified-Poisson/GEE, omnibus-P, and NNT/NNH definitions.

## Matching keys for main-paper/cross-source review

1. Primary endpoint: MCID = >=30% reduction in overall BPI-SF pain severity from baseline, primary time point 3 months; arms PT, HC, UC; ITT/randomized target population.
2. Main adjusted primary effect family: modified Poisson GEE, log link, robust/sandwich SEs, independent working correlation; population-average RR; baseline pain severity, sex, site, rural/underserved residence, multisite pain, and mental-health condition adjustment. DOC-005 adds MNAR pattern-mixture imputation plus scaled nonresponse weights.
3. Main observed follow-up denominators: randomized 2,331 = UC 777 + PT 776 + HC 778; 3-month observed 1,798 = 621 + 542 + 635.
4. Key source-result comparisons available for later cross-source matching: eTable 4 adjusted RR at 3/6/12 months; eTable 7 complete-case and worst/best-case sensitivity results; eTable 8 enhancement/reminder-letter subsets; intervention fidelity/adherence counts in DOC-004.

## Limitations

The DOC-003 direct-PDF native text has unusable character encoding. Mapped statistical definitions and quantitative sample-size/model details were confirmed from direct rendered pages; pp. 27-29 were mapped as administrative/reference no-applicable units. DOC-005 p. 3 exposes only an adherence-figure caption in available text, so individual histogram-bin values require direct visual reading if a later checker needs them. No candidate, disposition, or legacy audit conclusion was consulted.
