# Main quantitative evidence map — Workflow 1.6.2

Scope: DOC-001 `jama_bot_2019_oi_190007.pdf`, all 11 PDF pages, document role REPORT. Runtime agent: `01a12952-18dd-7ad1-859f-41f68cf99a98`; role main_quantitative_mapper; gpt-6.1-sol/medium. Fresh reconstruction from source-matched reusable layout, not prior scientific decisions. No judgments or candidate selection are made in this map.

Primary locator: `.ai_paper_validation/review_1_6_1/preprocessing/recheck/main-layout.txt`, one-based form-feed pages 1–11. Curator verified exact equality with current direct Poppler 26.01.0 layout extraction. Additional inspected image: `.ai_paper_validation/document_outputs/DOC-001/rendered_pages/page_007.png` for all Figure 2 panels. Historical image renderer version unrecorded. No new rendering/OCR was necessary; compute device CPU. Reused assets and sources preserved.

IDs N001–N071 track numeric relationships; S001–S040 track statistical relationships. Each grouped row explicitly maps all constituent values; grouping is for coherent display/contrast relationships, not sampling. All source pages have an explicit unit record. PDF printed article pages 858–868 correspond to PDF pages 1–11.

## Unit coverage

| Source unit | Exact source | Mapping | Fresh-required status |
|---|---|---|---|
| PDF p. 1 | [Abstract](../../../jama_bot_2019_oi_190007.pdf#page=1) | Trial, population, intervention, event, estimate and safety abstract values; N001–N006, N065, S001–S003 | Reusable-backed COMPLETE |
| PDF p. 2 | [Key Points and Methods](../../../jama_bot_2019_oi_190007.pdf#page=2) | Factorial marginal event counts; recruitment, eligibility, intervention, randomization; N001, N007, N008, S004 | Reusable-backed COMPLETE |
| PDF p. 3 | [Figure 1](../../../jama_bot_2019_oi_190007.pdf#page=3) | Every screening, exclusion, allocation, follow-up and analysis cell and footnote; N009–N020 | Reusable-backed COMPLETE |
| PDF p. 4 | [Outcomes and methods](../../../jama_bot_2019_oi_190007.pdf#page=4) | All scales, time points, adherence definitions, sample-size inputs and analyses; N021–N024, S005–S010 | Reusable-backed COMPLETE |
| PDF p. 5 | [Table 1](../../../jama_bot_2019_oi_190007.pdf#page=5) | Every baseline row and footnote value; N025–N055 | Reusable-backed COMPLETE |
| PDF p. 6 | [Table 2 and Results](../../../jama_bot_2019_oi_190007.pdf#page=6) | Every primary/post-hoc table cell, footnote, attrition and adherence claim; N056–N060, S011–S019 | Reusable-backed COMPLETE |
| PDF p. 7 | [Figure 2 and Results](../../../jama_bot_2019_oi_190007.pdf#page=7) | Every panel/scale/count/caption; MDD narrative copies and rates; N061–N064, S001–S003, S011–S013, S020 | Reusable-backed COMPLETE |
| PDF p. 8 | [Table 3 and Results](../../../jama_bot_2019_oi_190007.pdf#page=8) | Every outcome/contrast/time row, coefficient, CI, P, Cohen D and footnote; narrative/sensitivity/CACE/safety/concealment; N065–N068, S021–S039 | Reusable-backed COMPLETE |
| PDF p. 9 | [Discussion and Conclusions](../../../jama_bot_2019_oi_190007.pdf#page=9) | Interpretation copies, adherence timing, power/attrition statements; N069–N071, S040 | Reusable-backed COMPLETE |
| PDF p. 10 | [Article information and references](../../../jama_bot_2019_oi_190007.pdf#page=10) | Inspected entire page. No applicable trial result quantities: affiliations, contributions, investigators, disclosures, support, references; grant and bibliographic numbers are administrative | Reusable-backed NO_APPLICABLE |
| PDF p. 11 | [References](../../../jama_bot_2019_oi_190007.pdf#page=11) | Inspected entire page. No applicable trial result quantities: references 19–40, bibliographic/instrument names retained as context only | Reusable-backed NO_APPLICABLE |

## Population, numeric and display relationships

Group shorthand in every four-column tuple below: P0 = placebo/no therapy (257); P1 = placebo/therapy (256); S0 = supplement/no therapy (256); S1 = supplement/therapy (256). Factor levels: supplements versus placebo; therapy versus no therapy. Figure 1 instead prints S1,S0,P1,P0 left to right, explicitly retained below. Table 1 percentages use its respective column n unless the source provides another definition.

| ID | Location | Quantity, context and all printed values | Matching locations / relation |
|---|---|---|---|
| N001 | pp.1,2,6,9 | 2×2 factorial randomized individual trial, n=1025 adults, 4 European countries; 1-year intervention/follow-up; recruitment July30 2015–October12 2016, trial through October13 2017 | Abstract, Key Points, design, Results, Discussion |
| N002 | p.1 abstract | P0 257, P1 256, S0 256, S1 256 | Figure1 p.3; Table1 p.5; Results p.6 |
| N003 | p.1 abstract | Mean age46.5 years; 772 women(75%); mean BMI31.4; 779(76%) completed | Table1 age/sex/BMI; Figure1 month12 and attrition p.6 |
| N004 | pp.1,6–7 | 105(10%) developed MDD over12mo; P0 25(9.7%), P1 26(10.2%), S0 32(12.5%), S1 22(8.6%) | Table2 footnotes c–f; Key Points marginal counts |
| N005 | p.1 abstract | One death S1; hospitalized P0 24,P1 24,S0 26,S1 24 | p.8 safety totals98 hospitalized,1 died |
| N006 | pp.1–2 | Daily dose1412mg omega3; selenium30μg; folic acid400μg; vitaminD3 20μg + calcium100mg;2 pills/day×1year; p.2 EPA:DHA ratio3:1 | Intervention definitions; no dose conversions inferred |
| N007 | p.2 Key Points | Supplements54(10.5%) vs placebo51(9.9%); therapy48(9.4%) vs no therapy57(11.1%) | Table2 marginal n512 intervention /513 control; p.7 rates |
| N008 | p.2 eligibility | Age18–75; BMI25–40kg/m²; PHQ9≥5; no current MDD in past6mo; assessments3,6,12mo | Abstract p.1; flow p.3; outcomes p.4 |
| N009 | p.3 Figure1 | Online5965; excluded3730; eligible telephone2235; no telephone462; completed1773; telephone exclusions523; baseline eligible1250; unwilling/unable225; randomized1025 | p.6 narrative copies of5965,2235,1773,1250,1025 |
| N010 | p.3 Figure1 online exclusions | 1451 BMI<15 or>40;623 antidepressants past6mo;591 no contact;566 PHQ<5;268 PHQ missing;220 none answered;11 age<18/>75 | Printed BMI threshold retained literally; sum relation3730 |
| N011 | p.3 Figure1 telephone exclusions | 259 current depressive disorder;97 antidepressant/psychological therapy past6mo;44 supplement prescribed/not willing stop;38 psychiatric disorder;26 unwilling visit;18 BMI<25;15 pregnant/planning;12 other mood;7 bariatric;4 did not understand;3 severe medical | Sum relation523; psychiatric footnote lists bipolar,schizophrenia,psychosis,eating,anxiety,alcohol/drug/substance addiction |
| N012 | p.3 Figure1 allocation | S1 256,S0 256,P1 256,P0 257; all received intervention as randomized; analysis includes same counts | Sum1025; intention-to-treat footnote all regardless received/withdrawal, missing multiple imputed |
| N013 | p.3 Figure1 month3 MDD measured | S1 209,S0 202,P1 215,P0 205 | Attrition total194 of1025 p.6 |
| N014 | p.3 Figure1 month6 MDD measured | S1 193,S0 185,P1 197,P0 196 | Attrition254 p.6 |
| N015 | p.3 Figure1 month12 MDD measured | S1 191,S0 194,P1 198,P0 196 | Completers779 p.1; attrition246 p.6 |
| N016 | p.3 Figure1 S1 loss | Cumulative65 = no-time25,lost-contact12,physical8,mental3,other17 | Defined no MDD measurement at12mo |
| N017 | p.3 Figure1 S0 loss | Cumulative62 = no-time18,lost-contact17,physical8,mental3,other13,unknown3 | Same definition |
| N018 | p.3 Figure1 P1 loss | Cumulative58 = no-time21,lost-contact17,physical7,mental3,other10 | Same definition |
| N019 | p.3 Figure1 P0 loss | Cumulative61 = no-time19,lost-contact17,physical10,mental5,other9,unknown1 | Same definition |
| N020 | pp.3,6 Table2 | Figure1 cumulative loss246; Table2 dropout239 defined no12mo completion AND no MDD at earlier measurement | Distinct denominators/definitions explicitly retained |
| N021 | p.4 therapy | Maximum21 sessions:15 individual+6 group over1year; no active attention control | Abstract21; adherence≥8/21 |
| N022 | p.4 outcome scales | PHQ9 0–27 higher worse; IDS30-SR0–84 higher worse; GAD7 0–21 higher worse; EQ5D5L utility0–1 higher better, England tariff; TFEQ-R18 three factors0–100 higher poorer eating; other secondary eating/food intake/activity/sedentary/body weight perception listed | Article reports mental-health secondary PHQ,IDS,GAD,utility only; time-to-MDD post hoc |
| N023 | p.4 adherence | A priori good adherence≥8/21 therapy and ≥70% supplement use during12mo | p.6 pill adherence narrative says more than70%; p.9≥8/21 |
| N024 | p.4 sample size inputs | Preventive reduction25–50% background; assumed33% reduction, active20% vs control30% onset;392 participants(196 in each of4 combinations) printed; two interventions; two-sidedα=.05,power.90;attrition22%;250 per combination;absolute difference10% | S005 statistical design; all printed wording preserved |
| N025 | p.5 Table1 sex | Men77(30.0),63(24.6),63(24.6),50(19.5);women180(70.0),193(75.4),193(75.4),206(80.5) | n257,256,256,256; abstract772 women |
| N026 | p.5 Table1 age mean(SD),y | 45.7(13.2),46.1(12.8),47.2(13.3),47.1(12.7) | Abstract age46.5 |
| N027 | p.5 Table1 age median(IQR),y | 47(36–55),47(37–55),48(38–58),47(38–56) | Same population |
| N028 | p.5 Germany | 70(27.2),67(26.2),69(27.0),71(27.7) | Site strata |
| N029 | p.5 UK | 64(24.9),63(24.6),64(25.0),63(24.6) | Site strata |
| N030 | p.5 Spain | 64(24.9),64(25.0),62(24.2),62(24.2) | Site strata |
| N031 | p.5 Netherlands | 59(23.0),62(24.2),61(23.8),60(23.4) | Site strata |
| N032 | p.5 education low | 25(9.7),21(8.2),31(12.1),26(10.2) | No/primary/lower-secondary education |
| N033 | p.5 education middle | 124(48.2),141(55.1),120(46.9),113(44.1) | Upper-secondary/postsecondary nontertiary/short-cycle tertiary |
| N034 | p.5 education high | 108(42.0),94(36.7),105(41.0),117(45.7) | Bachelor’s or higher/equivalent |
| N035 | p.5 history MDD | 83(32.3),89(34.8),88(34.4),83(32.4) | Stratification/adjustment |
| N036 | p.5 ≥2 episodes | 59(23.0),53(20.7),62(24.2),58(22.7) | Nested history category; denominators column n |
| N037 | p.5 current smoker | 53(20.6),50(19.5),35(13.7),47(18.4) | Baseline |
| N038 | p.5 alcohol drinks/wk median(IQR) | All four1.0(0.2–3.7) | Baseline |
| N039 | p.5 physical activity h/d median(IQR) | 7.8(6.1–9.5),7.8(5.6–10.0),7.9(5.9–10.2),7.5(5.3–9.7) | Commute walking/cycling,work,household,leisure,sport |
| N040 | p.5 BMI mean(SD) | 31.4(4.1),31.2(3.9),31.3(4.0),31.7(3.9) | Weightkg/heightm²; abstract31.4 |
| N041 | p.5 PHQ mean(SD) | 7.3(4.1),7.3(4.4),7.9(4.4),7.1(4.0) | Baseline; marginal means p.8 |
| N042 | p.5 PHQ median(IQR) | 7(4–10),6(4–10),7(5–10),6(4–9) | Thresholds≥5 mild,≥10 moderate |
| N043 | p.5 IDS mean(SD) | 21.3(9.8),21.6(10.5),22.8(10.2),21.4(9.8) | Baseline |
| N044 | p.5 IDS median(IQR) | 20(14–27),21(13–29),21(15–30),20(14–28) | Thresholds≥14 mild,≥26 moderate |
| N045 | p.5 anxiety GAD mean(SD) | 5.8(4.4),6.2(4.5),5.7(3.8),5.4(3.8) | Baseline; marginal means p.8 |
| N046 | p.5 GAD median(IQR) | All four5(3–7) except P1 5(3–9) | Thresholds≥5 mild,≥10 moderate |
| N047 | p.5 utility mean(SD) | 0.87(0.11),0.86(0.13),0.86(0.12),0.86(0.12) | 0 death,1 full health,England tariff |
| N048 | p.5 utility median(IQR) | 0.88(0.82–0.94),0.87(0.81–0.95),0.87(0.81–0.94),0.88(0.81–0.94) | Baseline |
| N049 | p.5 diet score mean(SD) | 51.7(7.6),51.9(6.9),51.6(6.8),51.4(6.9) | Range0–77,higher Mediterranean adherence |
| N050 | p.5 prior supplements | 77(30.0),86(33.6),78(30.5),79(30.9) | Baseline |
| N051 | p.5 diet footnote g | Median vegetables2.8/day;fruit1.9/day;fish1.5/week;legumes1/week;meat5/week | 11 score components, whole sample |
| N052 | p.5 diet footnote g | Whole grains67% total grains; low-fat dairy0.9/day;olive oil33% total dressings/oils/fats | Same |
| N053 | p.5 diet footnote g | Soft drinks0.14/day;processed food1.6/day;alcohol0.14/day | Same |
| N054 | p.5 table labels | All four group headers No.(%) participants n257,256,256,256; continuous row exceptions explicitly mean(SD) or median(IQR) | Every Table1 row above |
| N055 | pp.4–5 scales | PHQ0–27,IDS0–84,GAD0–21,utility0–1,diet0–77; sign meanings retained in N022,N042,N044,N046,N047,N049 | Scale definitions match results interpretation |
| N056 | p.6 Table2 primary totals | Placebo n513/events51/dropouts113; supplements512/54/126; no therapy513/57/122;therapy512/48/117;interaction NA/NA/NA | Events sum105 in each factor; dropout sum239 |
| N057 | p.6 Table2 post-hoc person-months | Placebo4656/events51/dropouts113;supplements4488/54/126;no therapy4503/57/122;therapy4641/48/117;interaction NA | Time to event or censoring; sums9144 in each factor |
| N058 | p.6 Table2 footnotes | c:P0 25/257(9.7%),P1 26/256(10.2%);d:S0 32/256(12.5%),22/256(8.6%) printed as supplements WITHOUT therapy again;e:P0 25/257,S0 32/256;f:P1 26/256,S1 22/256;g:interaction | Literal d labeling retained; other occurrences N004 |
| N059 | p.6 attrition | Missing primary3mo194(19%),6mo254(25%),12mo246(24%);dropouts before12mo or onset239(23%).Secondary missing baseline29–32,3mo206–211,6mo275–278,12mo268 | Figure1,N013–N020; Figure2 completer counts |
| N060 | p.6 adherence | Among12mo participants77% >70% pill adherence;among therapy randomized71%≥8/21; individual median14/15(IQR6–15),group0/6(IQR0–4) | a priori definitions N023; p.9 timing |
| N061 | p.7 Figure2 PHQ panelsA/B | Available-data n at0,3,6,12mo:996,819,750,757,identical A/B; x ticks0,3,6,9,12; y0–30 step5 | PHQ0–27 possible scale; no9mo observation printed |
| N062 | p.7 Figure2 IDS panelsA/B | Available n994,817,747,757 at0,3,6,12; x0,3,6,9,12; y0–60 step10 | IDS0–84 possible scale; no exact plotted estimates labeled |
| N063 | p.7 Figure2 GAD/utility panelsA/B | GAD n993,815,747,757;y0–25 step5. Utility n993,814,747,757;y0–1 step.2. x0,3,6,9,12 | Same available-data counts A/B |
| N064 | p.7 MDD rates | Placebo51(9.9%;1.1/100 person-months),supplements54(10.5%;1.2),no therapy57(11.1%;1.3),therapy48(9.4%;1.0) | N056–N057; abstract/Key Points |
| N065 | p.8 safety | Hospitalized98,died1 during12mo,judged unrelated | p.1 hospitalization group counts sum98; deathS1 |
| N066 | p.8 unadjusted GAD | Baseline therapy5.8,no therapy5.8;12mo no therapy3.9,therapy3.2 | Available score context; adjusted S032 differs in analysis |
| N067 | p.8 unadjusted PHQ | Baseline placebo7.3,supplements7.5;12mo placebo4.1,supplements4.9 | Available score context; adjusted S021,S022 |
| N068 | p.8 concealment | Believe multinutrients:P0 8.2%,P1 10.4%,S0 25.5%,S1 43.7%;P<.001;40.4% of questionnaire completers do not know allocation | eAppendix13 pointer; no denominators printed here |
| N069 | p.9 discussion | n1025;2 strategies and combination;1year cumulative onset, no effect;MDD onset lower than expected/reduced power;approximately quarter lost | N001,N004,N059; primary S001–S003 |
| N070 | p.9 adherence | About three-quarters meet criteria;individual sessions first6mo well attended,group subsequent6mo not;≥8/21 in CACE discussion | N060,S037 |
| N071 | p.9 background/limitations | Review9 RCTs of vitaminD,other historical trials mentioned;not trial result comparisons.1year predefined follow-up;4-country factorial trial | Context only; no external evidence read |

## Statistical relationships

All inferential intervals below are printed 95% CIs. Null is1 for OR/HR and0 for coefficients/mean differences. Each contrast uses factor effect coding −1 control,+1 intervention unless expressly described otherwise. Coefficient magnitude is distinct from the between-group difference; Table3 instructs multiplying coefficients AND CI limits by2. No standard errors or test statistics are printed; none inferred as source values. Directions below are the source descriptions, not a diagnostic conclusion.

| ID | Exact location | Endpoint, population, method and printed result | Linked numeric/model evidence |
|---|---|---|---|
| S001 | pp.1,6,7 | 12mo cumulative MDD,supplements:logistic OR1.06(0.87–1.29),P=.57 (P only pp.6–7);n512 vs513;no significant effect | ITT,MI100,site/history,joint factorial model S006;N004,N056 |
| S002 | pp.1,6,7 | 12mo MDD,therapy:OR0.93(0.76–1.13),P=.47;no significant effect | Same model;N007,N056 |
| S003 | pp.1,6,7 | 12mo MDD,supplements×therapy:OR0.93(0.76–1.14),interactionP=.48;abstract calls combination;not significant | Same joint model |
| S004 | p.2 randomization | Equal probability four arms;permuted blocks8–12;stratified site and lifetime depression history;participants/therapists/researchers supplement-blind,outcome researchers therapy-blind;primary and reported secondary ITT analyses blinded | Randomization is individual; N001,N002 |
| S005 | p.4 sample size | 2×2;primary outcome;20% active vs30% control;33% relative reduction;two-sidedα=.05,power.90;392 participants(196 each of4 combinations);22% attrition→250 per combination;10% absolute clinical difference | All printed inputs N024 retained without normalization |
| S006 | p.4 statistical methods | All randomized irrespective intervention/withdrawal;two interventions effect coded−1/+1,jointly main effects+interaction;all analyses site/history adjusted;endpoint missing MAR multiple imputation100 datasets,Rubin pooling | Primary S001–S003;Cox S011–S013;Table3 adjustments S036 |
| S007 | p.4 primary outcome | Cumulative12mo MDD via MINI5.0 depression section at3,6,12mo,DSMIV episode definition;logistic regression | N008,N022;S001–S003 |
| S008 | p.4 post hoc Cox | Time to first MDD onset3,6,12mo or last available measurement;Cox proportional hazards;scaled Schoenfeld test assumption metP>.05 | S011–S013;N057 |
| S009 | p.4 secondary outcomes | GEE longitudinal ANCOVA,exchangeable correlation;dependent repeated3,6,12mo;adjust baseline respective outcome;overall and12mo tested;secondary findings exploratory due multiple comparisons | Table3 GEE and robust regression distinctions S036 |
| S010 | pp.4,6 sensitivity/statistical settings | GEE without MI as missing-data sensitivity;Cohen D baseline→12mo between interventions from MI;CACE MI structural equations in STATA primary and secondary12mo;R3.4.4 geepack/mice;two-sided thresholdP=.05 | S037–S039 |
| S011 | pp.6–7 | Post hoc time-to-MDD supplements HR1.05(0.86–1.27),P=.65 | N057,S008;no significant effect |
| S012 | pp.6–7 | Time-to-MDD therapy HR0.91(0.75–1.10),P=.32 | Same |
| S013 | pp.6–7 | Time-to-MDD interaction HR0.91(0.75–1.11),P=.36 | Same |
| S014 | p.6 Table2 references | Placebo and no-therapy OR/HR1[Reference];interaction patients/events/dropouts/time NA | Reference coding plus S006;not crude contrasts specified |
| S015 | p.6 primary missingness | No between-four-arm missing-rate difference at3moP=.47 | N013,N059;test method not named here |
| S016 | p.6 primary missingness | No difference6moP=.62 | N014,N059 |
| S017 | p.6 primary missingness | No difference12moP=.91 | N015,N059 |
| S018 | p.6 secondary missingness | Secondary missingness rates did not differ across arms;no P printed | N059 |
| S019 | p.6 Table2 footnote b | Multiple imputed;adjusted interventions,site,history;therapy/pills effect-coded(−1,1) | S001–S003,S011–S013;CI95% |
| S020 | p.7 secondary interaction | No significant supplements×therapy interactions for any secondary scores;P range.41–.98 | Table3 interaction exclusion;S036 |
| S021 | p.8 Table3 PHQ supplements overall | Coefficient0.33(0.12–0.53),P=.002 | Overall GEE;mean difference narrative0.65(0.25–1.06),P=.002;higher symptom follow-up |
| S022 | p.8 Table3 PHQ supplements12mo | Coefficient0.28(0.05–0.50),P=.02;CohenD0.10 | Robust linear;mean difference narrative0.56(0.11–1.01),P=.02;N067 |
| S023 | p.8 Table3 PHQ therapy overall | −0.13(−0.33–0.07),P=.19 | Overall GEE;no therapy effect reported |
| S024 | p.8 Table3 PHQ therapy12mo | −0.17(−0.39–0.06),P=.14;D−0.02 | Robust linear |
| S025 | p.8 Table3 IDS supplements overall | 0.60(0.15–1.05),P=.01 | Narrative adjusted mean difference1.20(0.29–2.10),P=.01;higher symptom follow-up |
| S026 | p.8 Table3 IDS supplements12mo | 0.36(−0.19–0.90),P=.20;D0.05 | Robust linear |
| S027 | p.8 Table3 IDS therapy overall | −0.23(−0.67–0.22),P=.32 | Overall GEE |
| S028 | p.8 Table3 IDS therapy12mo | −0.28(−0.83–0.27),P=.31;D0.006 | Robust linear |
| S029 | p.8 Table3 GAD supplements overall | 0.25(0.08–0.42),P=.004 | Narrative mean difference0.50(0.16–0.84),P=.004 |
| S030 | p.8 Table3 GAD supplements12mo | 0.14(−0.04–0.33),P=.13;D0.10 | Robust linear |
| S031 | p.8 Table3 GAD therapy overall | −0.16(−0.32–0.01),P=.06 | Overall GEE |
| S032 | p.8 Table3 GAD therapy12mo | −0.24(−0.42–−0.06),P=.01;D−0.07 | Narrative adjusted mean difference−0.48(−0.84–−0.12),P=.01;lower anxiety;N066 |
| S033 | p.8 Table3 utility supplements overall | −0.006(−0.012–0.000),P=.052 | Overall GEE;higher utility better |
| S034 | p.8 Table3 utility supplements12mo | −0.002(−0.008–0.005),P=.61;D−0.07 | Robust linear |
| S035 | p.8 Table3 utility therapy overall/12mo | Overall0.002(−0.003–0.008),P=.44;12mo0.004(−0.002–0.009),P=.23;D0.08 | Both time-specific rows explicitly retained |
| S036 | p.8 Table3 footnotes a–e | Two factors jointly;site/history/baseline adjusted;−1/+1;interactions omitted because none significant;overall longitudinal GEE on MI;12mo robust linear on MI;multiply estimate+CI×2 for adjusted mean difference;CohenD baseline/12mo means+pooledSD MI | Every Table3 result S021–S035;N022 |
| S037 | p.8 CACE | Primary therapy OR0.78(0.64–0.95),significant accounting adherence;no supplement primary effect;similar secondary effects | eAppendix12;N023,N060;S010 |
| S038 | pp.4,8 effect modification | Methods:site/history interaction terms;baseline symptoms post hoc. Results paragraph calls site,history,baseline analyses post hoc:therapy PHQ12mo larger reduction at higher baseline PHQ;supplement follow-up GAD higher at higher baseline GAD;therapy utility12mo larger UK than Netherlands | eAppendix10;no numeric coefficients here;description preserved |
| S039 | p.8 sensitivity/concealment | Non-MI depression/anxiety/utility estimates comparable;eAppendix11. Believing allocation differsP<.001 across groups | N068;CACE separate S037 |
| S040 | p.9 interpretation | Neither intervention/combination reduces1year MDD;lower-than-expected onset reduces power;therapy anxiety benefit12mo but no other secondary mental-health effect;adherence-based lower MDD onset;higher baseline symptoms post hoc therapy benefit;quarter attrition balanced | Matching S001–S003,S032,S037,S038;no numerical power recalculation printed |

## Figure 2 graphical relationships

All eight subpanels were inspected in the reusable exact-page image. A contrasts supplements (dark blue intervention) with placebo (light blue control); B contrasts therapy (dark blue) with no therapy (light blue). Both contain PHQ, IDS, GAD and utility at baseline/3/6/12 months. Caption defines median as inner horizontal line, IQR25th–75th percentiles as box, whiskers1.5×IQR beyond25th/75th,dots other values,diamonds means. Data are available observations, not multiple-imputed adjusted estimates. Each symptom panel broadly falls across follow-up; utility broadly rises. Supplement PHQ means at12mo are above placebo; therapy GAD mean at12mo is below no therapy. No exact numerical box/whisker/mean annotations are printed, so coordinates are not invented. N061–N063 retain every displayed participant count and axis tick. Table3 and narrative carry the inferential comparisons; the plotted raw distributions are distinct quantities.

## Cross-location matching index and contextual definitions

- Primary cumulative events: abstract p.1 → Key Points p.2 → Table2 p.6 → narrative pp.6–7 → Discussion/conclusions p.9. Match factor marginals separately from four combination groups.
- Logistic estimates: abstract p.1 → Table2 p.6 → narrative p.7. All are effect-coded adjusted MI estimates. Abstract interaction wording is preserved as combination, with explicit interactionP=.48.
- Post-hoc Cox: Table2 p.6 → narrative p.7; exposure times and censoring definition connect to observed events, not cumulative loss alone.
- Analysis population: Figure1 includes all1025; Figure2 is outcome/time-specific available n; Table2 dropouts exclude previous MDD; sample-size calculation and baseline Table1 use their expressly printed denominators.
- Secondary estimates: Table3 coefficients versus narrative adjusted mean differences, with Table3×2 instruction. GEE overall versus robust-linear12mo distinguished; Cohen D is separately standardized from baseline/follow-up means and pooledSD.
- Supplemental pointers: p.4 eAppendixes1–7 recruitment,interventions,outcomes,measures,CACE methods; p.6 eAppendix8 adherence; p.7 eAppendix9 four-group plots; p.8 eAppendixes10–13 moderation,sensitivity,CACE,concealment. Other source contents are outside this mapper's disjoint scope.

## Completeness and limitations

Mapped11/11 units, reusable11,fresh-required0; scientific gaps0. Every displayed quantitative row, all inferential results, all narrative copies and result-relevant footnotes are included. Two reference/administrative pages carry explicit no-applicable records. Exact Figure2 coordinates are not numerical printed values; graphical scales/distributions and counts have been mapped without treating approximate coordinates as exact estimates. No raw data are supplied in this scope and no individual-level reconstruction is attempted. No new extraction derivatives were produced. Full source-matched page transcriptions follow for traceability and to retain wording and layout, including nonapplicable reference pages; they are locator aids, never final authority.

## Complete page transcription aid

### DOC-001 PDF page 1

Source: [PDF page 1](../../../jama_bot_2019_oi_190007.pdf#page=1)

```text
              Research



              JAMA | Original Investigation

              Effect of Multinutrient Supplementation and Food-Related
              Behavioral Activation Therapy on Prevention of Major
              Depressive Disorder Among Overweight or Obese Adults
              With Subsyndromal Depressive Symptoms
              The MooDFOOD Randomized Clinical Trial
              Mariska Bot, PhD; Ingeborg A. Brouwer, PhD; Miquel Roca, PhD; Elisabeth Kohls, PhD; Brenda W. J. H. Penninx, PhD; Ed Watkins, PhD;
              Gerard van Grootheest, MSc; Mieke Cabout, MSc; Ulrich Hegerl, PhD; Margalida Gili, PhD; Matthew Owens, PhD; Marjolein Visser, PhD;
              for the MooDFOOD Prevention Trial Investigators


                                                                                                                                     Editorial page 842
                 IMPORTANCE Effects of nutritional interventions on the prevention of major depressive                               Related article page 869
                 disorder (MDD) in overweight adults are unknown.
                                                                                                                                     Supplemental content
                 OBJECTIVE To examine the effect of 2 nutritional strategies (multinutrient supplementation,                         CME Quiz at
                 food-related behavioral activation therapy) and their combination for prevention of a new                           jamanetwork.com/learning
                 MDD episode in overweight adults with subsyndromal depressive symptoms.                                             and CME Questions page 897

                 DESIGN, SETTING, AND PARTICIPANTS This multicenter 2 × 2 factorial randomized clinical trial
                 included overweight adults (body mass index, 25-40) with elevated depressive symptoms
                 (Patient Health Questionnaire-9 [PHQ-9] scores ⱖ5) and no MDD episode in the past 6
                 months from 4 European countries. A total of 1025 adults were randomized (July 30,
                 2015-October 12, 2016) and followed up for 1 year (October 13, 2017).

                 INTERVENTIONS Daily multinutrient supplements (1412-mg omega-3 fatty acids, 30-μg
                 selenium, 400-μg folic acid, and 20-μg vitamin D3 plus 100-mg calcium) vs placebo and 21
                 individual or group therapy sessions vs none (blinded to researchers) for 1 year. Participants
                 were allocated to placebo without therapy (n = 257), placebo with therapy (n = 256),
                 supplements without therapy (n = 256), and supplements with therapy (n = 256).

                 MAIN OUTCOME AND MEASURES Cumulative 1-year onset of MDD via the Mini International
                 Neuropsychiatric Interview at 3, 6, and 12 months. Logistic regression using effect-coded
                 variables (−1 indicating control, 1 indicating intervention) evaluated intervention effects both
                 individually and in combination (interaction) on MDD onset.

                 RESULTS Among 1025 participants (mean age, 46.5 years; 772 women [75%]; mean BMI, 31.4), 779
                 (76%) completed the trial. During the 12-month follow-up, 105 (10%) developed MDD: 25 (9.7%)
                 patients in the placebo without therapy, 26 (10.2%) in the placebo with therapy, 32 (12.5%) in the
                 supplement without therapy, and 22 (8.6%) in the supplement with therapy group. None of the
                 treatment strategies affected MDD onset. The odds ratio (OR) for supplements was 1.06 (95% CI,
                 0.87-1.29); for therapy, 0.93 (95% CI, 0.76-1.13); and for their combination, 0.93 (95% CI, 0.76-1.14;
                 P for interaction, .48). One person in the supplementation with therapy group, died. Twenty-four
                 patients in each of the placebo groups and 24 patients in the supplementation with therapy group               Author Affiliations: Author
                 were hospitalized, and 26 patients in the supplementation-only group were hospitalized.                        affiliations are listed at the end of this
                                                                                                                                article.
                 CONCLUSIONS AND RELEVANCE Among overweight or obese adults with subsyndromal                                   Group Information: The MooDFOOD
                 depressive symptoms, multinutrient supplementation compared with placebo and                                   Prevention Trial Investigators are
                                                                                                                                listed at the end of this article.
                 food-related behavioral activation therapy compared with no therapy did not reduce
                                                                                                                                Corresponding Author: Marjolein
                 episodes of major depressive disorder during 1 year. These findings do not support the use of
                                                                                                                                Visser, PhD, Department of Health
                 these interventions for prevention of major depressive disorder.                                               Sciences, Faculty of Science and
                                                                                                                                Amsterdam Public Health research
                 TRIAL REGISTRATION ClinicalTrials.gov Identifier: NCT02529423                                                  institute, Vrije Universiteit
                                                                                                                                Amsterdam, De Boelelaan 1085, 1081
                                                                                                                                HV Amsterdam, the Netherlands
                 JAMA. 2019;321(9):858-868. doi:10.1001/jama.2019.0556                                                          (m.visser@vu.nl).


        858                                                                                                                                    (Reprinted) jama.com

                                                      © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC-001 PDF page 2

Source: [PDF page 2](../../../jama_bot_2019_oi_190007.pdf#page=2)

```text
              Effect of Behavioral Therapy and Supplements on MDD Among Overweight and Obese Adults                                  Original Investigation Research




              M
                          ajor depressive disorder (MDD) is a common psychi-
                          atric disorder (lifetime prevalence, 17%),1 ranking as              Key Points
                          the second leading contributor of years lived with
                                                                                              Question What is the effect of multinutrient supplementation and
              disability.2 Prevention may offer an important opportunity to                   food-related behavioral activation therapy on prevention of a new
              reduce the global disease burden of MDD.3                                       episode of major depressive disorder among overweight or obese
                   One preventive strategy for MDD might be to modify diet.                   adults with subsyndromal depressive symptoms?
              Prospective studies have found that better adherence to higher
                                                                                              Findings In this 2 × 2 factorial randomized clinical trial that
              quality diets is associated with reduced future onset of de-                    included 1025 adults, there was no significant difference in
              pressive symptoms.4 Food-related behaviors, like unhealth-                      episodes of major depressive disorder over 1 year of follow-up with
              ful eating styles,5 have been cross-sectionally related to in-                  multinutrient supplementation vs placebo (54 [10.5%] vs 51
              creased depressive symptoms. Recent randomized clinical                         [9.9%]) or with food-related behavioral activation therapy vs no
              trials (RCTs) found that dietary improvement strategies re-                     therapy (48 [9.4%]) vs 57 [11.1%]).
              duced depressive symptoms in depressed adults relative to con-                  Meaning These findings do not support the use of multinutrient
              trol conditions,6,7 but there remains a clear lack of RCTs test-                supplementation or food-related behavioral activation therapy for
              ing dietary strategies to prevent depression.8                                  prevention of major depressive disorder.
                   Similarly, observational studies have suggested that lower
              levels of specific nutrients (eg, omega-3 polyunsaturated fatty
              acids, folic acid, vitamin D, selenium) are related to higher lev-          tionnaire (PHQ-9) scores of 5 or higher15 but having no cur-
              els of depressive symptoms.9,10 Some—but not all—nutritional                rent MDD episode in past 6 months (Mini International
              supplement intervention studies have indicated that nutrient                Neuropsychiatric Interview 5.0 [MINI 5.0]).16 (See eAppen-
              supplementation may reduce depressive symptoms in those                     dix 1 in Supplement 3 for recruitment details and eligibility.)
              with MDD.11                                                                 All eligible participants were invited to visit one of the study
                   To date, few experimental studies have directly evalu-                 sites for a baseline interview. The interview, physical mea-
              ated the effect of changing diet, food-related behavior, or nu-             surements, blood sampling were conducted by trained re-
              trients on preventing MDD8,12 and none to our knowledge have                search assistants or nurses. Furthermore, participants com-
              specifically targeted overweight and obese individuals, who                 pleted self-report questionnaires. Follow-up assessments took
              are a particularly relevant population, given their increased risk          place at 3, 6, and 12 months.
              of MDD and the key role of diet in these conditions.13 There-
              fore, the MooDFOOD depression prevention trial examined the                 Randomization
              effect of 2 different nutritional strategies (multinutrient supple-         At the end of the baseline interview, participants were ran-
              mentation, food-related behavioral activation therapy) and                  domized with equal probability to (1) placebo supplements
              their combination for prevention of a new MDD episode in over-              without therapy; (2) placebo supplements with therapy;
              weight people with subsyndromal depressive symptoms.                        (3) multinutrient supplements without therapy; or (4) mul-
                                                                                          tinutrient supplements with therapy by a permuted block
                                                                                          randomization (block sizes ranging from 8-12; https://www.
                                                                                          sealedenvelope.com). Randomization was stratified by study
              Methods                                                                     site and participants’ lifetime history of depression status
              Study Design                                                                (Figure 1). After randomization, researchers dispensed
              This study was a 2 × 2 factorial RCT performed between July                 supplements to participants according to unique randomiza-
              30, 2015, and October 13, 2017, in 4 European countries                     tion codes. Participants, therapists, and researchers were
              (Germany, Spain, United Kingdom, and the Netherlands). For                  blinded to supplement allocation. Participants of food-
              full details of trial design and protocol see Roca et al14 and              related behavioral activation intervention therapy were con-
              Supplement 1. For the statistical analysis plan, see Supple-                tacted directly by the therapist, ensuring that researchers
              ment 2. Ethics approval was provided by the human research                  assessing follow-up outcomes remained blind to this inter-
              ethics boards of the 4 study sites. All participants provided writ-         vention status. Statistical analyses on the primary outcome
              ten informed consent. This article reports on primary and sec-              and the reported secondary outcomes in which participants
              ondary mental health outcomes as assessed up to 12 months.                  were analyzed according to their randomization group were
                                                                                          carried out blinded for randomization.
              Recruitment and Eligibility Criteria
              Participants were recruited to participate in a study investi-              Interventions
              gating new strategies to improve mood and well-being through                Multinutrient Supplements
              changes in diet and lifestyle by the study sites (located in                Patients received either multinutrient supplements (1412 mg
              Leipzig, Germany; Palma de Mallorca, Spain; Exeter, United                  of eicosapentaenoic and docosahexaenoic omega-3 poly-
              Kingdom; and Amsterdam, the Netherlands). Main eligibility                  unsaturated fatty acids [PUFAs]; ratio, 3:1), 30 μg of sele-
              criteria were age between 18 and 75 years, body mass index                  nium, 400 μg of folic acid, and 20 μg of vitamin D3 coupled
              (BMI, calculated as weight in kilograms divided by height in                with 100 mg of calcium) or placebo, each were provided in
              meters squared) between 25 and 40, having at least mild de-                 2 pills per day, taken daily for 1 year (see eAppendix 2
              pressive symptoms as operationalized by Patient Health Ques-                in Supplement 3 for details).

              jama.com                                                                                    (Reprinted) JAMA March 5, 2019 Volume 321, Number 9          859

                                                      © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC-001 PDF page 3

Source: [PDF page 3](../../../jama_bot_2019_oi_190007.pdf#page=3)

```text
              Research Original Investigation                                            Effect of Behavioral Therapy and Supplements on MDD Among Overweight and Obese Adults




              Figure 1. Flow of Participants Through the MooDFOOD Depression Prevention Trial


                                                                                    5965 Individuals completed online
                                                                                         screening questionnaire


                                                                                                                  3730 Excluded
                                                                                                                       1451 BMI <15 or >40
                                                                                                                        623 Antidepressant use in past 6 mo
                                                                                                                        591 No contact information
                                                                                                                        566 PHQ score <5
                                                                                                                        268 PHQ score missing
                                                                                                                        220 None of the questions answered
                                                                                                                         11 Age <18 y or >75 y


                                                                                   2235 Eligible for telephone screening


                                                                                                                    462 Excluded (no telephone screening)


                                                                                 1773 Completed the telephone screening


                                                                                                              523 Excluded
                                                                                                                  259 Current depressive disorder
                                                                                                                   97 Antidepressant or psychological therapy
                                                                                                                        in the last 6 mo
                                                                                                                   44 Supplements prescribed or not willing
                                                                                                                       to stop taking supplements
                                                                                                                   38 Psychiatric disordera
                                                                                                                   26 Not prepared to visit study center
                                                                                                                   18 BMI <25
                                                                                                                   15 Pregnant or planning to become pregnant
                                                                                                                   12 Other mood disorder
                                                                                                                    7 Bariatric surgery
                                                                                                                    4 Did not understand study information
                                                                                                                    3 Severe medical disease


                                                                                  1250 Eligible for baseline measurement


                                                                                                               225 Excluded (unwilling or not able to participate)



                                                                                            1025 Randomized



                     256 Randomized to receive                  256 Randomized to receive                   256 Randomized to receive                    257 Randomized to receive
                         supplements and therapy                    supplements alone                           placebo and therapy                          placebo alone
                         256 Received intervention                  256 Received intervention                   256 Received intervention                    257 Received intervention
                              as randomized                              as randomized                               as randomized                                as randomized


                    MDD measurement at follow-up               MDD measurement at follow-up                MDD measurement at follow-up                 MDD measurement at follow-up
                   209 At month 3                             202 At month 3                              215 At month 3                                205 At month 3
                   193 At month 6                             185 At month 6                              197 At month 6                                196 At month 6
                   191 At month 12                            194 At month 12                             198 At month 12                               196 At month 12
                     65 Cumulative loss to follow-upb           62 Cumulative loss to follow-upb           58 Cumulative loss to follow-upb              61 Cumulative loss to follow-upb
                        25 No time or not interested               18 No time or not interested               21 No time or not interested                  19 No time or not interested
                        12 Lost contact                            17 Lost contact                            17 Lost contact                               17 Lost contact
                         8 Physical health                          8 Physical health                          7 Physical health                            10 Physical health
                         3 Mental health                            3 Mental health                            3 Mental health                               5 Mental health
                        17 Other                                   13 Other                                   10 Other                                       9 Other
                                                                    3 Unknown                                                                                1 Unknown


                  256 Included in the primary analysisc      256 Included in the primary analysisc       256 Included in the primary analysisc        257 Included in the primary analysisc


              a
                  Bipolar disorder, schizophrenia, psychosis, eating disorder, anxiety disorder,         group, including all participants randomized regardless of the intervention
                  alcohol, drug, or substance addiction.                                                 actually received or of study withdrawal. Missing data were multiple imputed.
              b
                  Cumulative loss to follow-up is defined as having no MDD measurement at              BMI indicates body mass index; MDD, major depressive disorder; PHQ, Patient
                  month 12.                                                                            Health Questionnaire.
              c
                  The primary analysis included all participants according to their randomization




        860   JAMA March 5, 2019 Volume 321, Number 9 (Reprinted)                                                                                                                 jama.com

                                                              © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC-001 PDF page 4

Source: [PDF page 4](../../../jama_bot_2019_oi_190007.pdf#page=4)

```text
              Effect of Behavioral Therapy and Supplements on MDD Among Overweight and Obese Adults                           Original Investigation Research



              Food-Related Behavioral Activation Therapy                                  risk groups were found to reduce the onset of depression by
              Food-related behavioral activation therapy consisted of a                   25% to 50%. 3 Assuming a 33% reduction of MDD onset
              protocol-based intervention that incorporated standard                      between active (20% MDD onset) vs control conditions (30%
              behavioral activation approaches. Behavioral activation is                  MDD onset),26,27 392 participants (196 in each of the 4 pos-
              effective in depression treatment 17 and includes self-                     sible intervention combinations) were needed to evaluate
              monitoring, functional analysis, and activity scheduling.                   the main effect of each of the 2 nutritional interventions
              Food-related behavioral activation applied these proven                     (vs respective control) assuming a 2-sided test at α = .05 and
              techniques to improve mood by changing dietary habits,                      a power of (1−β) = .90. Assuming a follow-up attrition rate of
              food-related behaviors (eg, snacking), increasing positive                  22%, 250 participants per intervention combination were
              behaviors, and emphasizing a Mediterranean-style diet,                      needed. This corresponds to an absolute difference of 10%,
              which has been related to reduced depression onset. 4                       which is consistent with the assumed clinically relevant dif-
              A maximum of 21 sessions were provided (15 individual,                      ference in depression onset, estimated by consulting clinical
              6 group) for 1 year (see eAppendix 3 in Supplement 3). No                   experts and stakeholders (eg, health insurance companies),
              active (eg, attention) control condition was provided in                    reported in a previous depression prevention trial.28
              those receiving no therapy.
                                                                                          Statistical Methods
              Outcomes                                                                    Participants were analyzed according to their randomization
              Primary Outcome                                                             group, including all participants randomized regardless
              The primary outcome was the 12-month cumulative onset of                    of intervention actually received or study withdrawal. The 2
              an episode of MDD, defined according to standard psychiat-                  nutritional interventions were effect coded (−1 indicating
              ric Diagnostic and Statistical Manual of Mental Disorders (Fourth           control and 1 indicating intervention) and jointly modeled to
              Edition) criteria and was measured with the depression sec-                 efficiently study main effects and interactions as recom-
              tion of the MINI 5.016 at 3, 6, and 12 months.                              mended for factorial designs.29 All analyses were adjusted for
                                                                                          study site and history of MDD. Missing data for the trial end
              Secondary Outcomes                                                          points were accounted for using multiple imputation under the
              Secondary trial outcomes were depression severity (PHQ-9,                   missing at random assumption into 100 data sets. Results were
              range 0-27, with higher values indicating higher severity,15                pooled using the Rubin rules.30
              Inventory of Depressive Symptomatology; IDS30-SR, range                          Logistic regression analyses were conducted to estimate
              0-84, with higher values indicating higher severity),18 anxi-               effects of the interventions on the primary outcome. Cox pro-
              ety severity (Generalized Anxiety Disorder 7 Item Scale                     portional hazard modeling was used to study intervention
              [GAD-7], range 0-21, with higher values indicating higher                   effects on time to first MDD onset (3, 6, or 12 months for
              severity),19 health-related quality of life (utility, EuroQol               either MDD onset or last available measurement) as post hoc
              instrument [EQ-5D-5L],20 using the value sets for England,21                analysis. Scaled Schoenfeld residuals were used to test
              range 0-1, with higher values indicating better health utility),            the proportionality of hazard assumption, which was
              eating behavior (3-factor eating questionnaire [TEFQ-R18],                  met (P > .05). For secondary outcomes, generalized estimat-
              all 3 factors ranging from 0-100, with higher values indicat-               ing equations (GEE) longitudinal analysis of covariance
              ing poorer eating behavior) 22 food behavior, food intake                   (ANCOVA) with an exchangeable correlation structure was
              (Global Allergy and Asthma European Network [GA2LEN]                        used,31 modeling outcomes at 3, 6, and 12 months as depen-
              food frequency questionnaire 23 ), physical activity and                    dent variables and adjusting for their corresponding baseline
              sedentary behavior (short questionnaire to assess health-                   values. Overall follow-up effects (including all follow-up
              enhancing physical activity [SQUASH]24), and body weight                    assessments) and 12-month effects of the interventions for
              perception (Stunkard et al25). This article reports on the men-             these secondary follow-up outcomes were tested.31 Because
              tal health secondary outcomes depression severity (PHQ-9,15                 of the potential for type I error due to multiple comparisons,
              IDS30-SR),18 anxiety severity (GAD-7),19 and utility (EQ-5D-                findings for analyses of secondary end points should be inter-
              5L; eAppendix 4 in Supplement 3).20,21 Time to onset of first               preted as exploratory. Effect modification of study site and
              MDD episode was included for post hoc analyses.                             history of MDD was investigated with their corresponding
                                                                                          interaction terms with the interventions. Similarly, effect
              Other Measures                                                              modification by baseline symptom severity was included as
              Good adherence to interventions (attending ≥8 of 21 therapy                 post hoc analyses.
              sessions, and taking ≥70% of the supplements during the 12                       As GEE are known to be robust for missing data, GEE lon-
              months) was defined a priori. A detailed description of these               gitudinal ANCOVA without multiple imputation was carried
              and other measures can be found in eAppendixes 5 and 6 in                   out as sensitivity analyses. A Cohen D value was calculated
              Supplement 3.                                                               for each baseline, 12-month follow-up difference in second-
                                                                                          ary outcome between the intervention groups,32 using mul-
              Sample Size                                                                 tiple imputed data. Furthermore, complier average causal
              Sample size was based on the primary outcome and                            effect (CACE) analyses33,34 were carried out with the multiple
              accounted for the 2 × 2 factorial design. At the time the                   imputed data using structural equation modeling within
              trial was designed, effective preventive interventions in high-             STATA, to provide an estimate of intervention effects taking

              jama.com                                                                                 (Reprinted) JAMA March 5, 2019 Volume 321, Number 9      861

                                                      © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC-001 PDF page 5

Source: [PDF page 5](../../../jama_bot_2019_oi_190007.pdf#page=5)

```text
              Research Original Investigation                                           Effect of Behavioral Therapy and Supplements on MDD Among Overweight and Obese Adults




              Table 1. Baseline Sample Characteristics of the Trial Stratified by Intervention Group

                                                                  No. (%) of Participants
                                                                  Placebo                                                           Supplements
                                                                  Without Food-Related            With Food-Related                 Without Food-Related               With Food-Related
                                                                  Behavioral                      Behavioral                        Behavioral                         Behavioral
                                                                  Activation Therapy              Activation Therapy                Activation Therapy                 Activation Therapy
                                                                  (n = 257)                       (n = 256)                         (n = 256)                          (n =256)
                  Sex
                    Men                                           77 (30.0)                       63 (24.6)                         63 (24.6)                          50 (19.5)
                    Women                                         180 (70.0)                      193 (75.4)                        193 (75.4)                         206 (80.5)
                  Age, y
                    Mean (SD)                                     45.7 (13.2)                     46.1 (12.8)                       47.2 (13.3)                        47.1 (12.7)
                    Median (IQR)                                  47 (36-55)                      47 (37-55)                        48 (38-58)                         47 (38-56)
                  Site
                    Germany                                       70 (27.2)                       67 (26.2)                         69 (27.0)                          71 (27.7)
                    United Kingdom                                64 (24.9)                       63 (24.6)                         64 (25.0)                          63 (24.6)
                    Spain                                         64 (24.9)                       64 (25.0)                         62 (24.2)                          62 (24.2)
                    The Netherlands                               59 (23.0)                       62 (24.2)                         61 (23.8)                          60 (23.4)
                  Educationa
                    Low                                           25 (9.7)                        21 (8.2)                          31 (12.1)                          26 (10.2)
                    Middle                                        124 (48.2)                      141 (55.1)                        120 (46.9)                         113 (44.1)
                    High                                          108 (42.0)                      94 (36.7)                         105 (41.0)                         117 (45.7)
                  History of MDD                                  83 (32.3)                       89 (34.8)                         88 (34.4)                          83 (32.4)
                    ≥2 Episodes                                   59 (23.0)                       53 (20.7)                         62 (24.2)                          58 (22.7)
                  Current smoker                                  53 (20.6)                       50 (19.5)                         35 (13.7)                          47 (18.4)
                  Alcohol use, median (IQR), drinks/wk            1.0 (0.2-3.7)                   1.0 (0.2-3.7)                     1.0 (0.2-3.7)                      1.0 (0.2-3.7)
                  Physical activity, median (IQR), h/db           7.8 (6.1-9.5)                   7.8 (5.6-10.0)                    7.9 (5.9-10.2)                     7.5 (5.3-9.7)
                  BMI, mean (SD)                                  31.4 (4.1)                      31.2 (3.9)                        31.3 (4.0)                         31.7 (3.9)
                  Depression severity
                    PHQ-9c
                         Mean (SD)                                7.3 (4.1)                       7.3 (4.4)                         7.9 (4.4)                          7.1 (4.0)
                         Median (IQR)                             7 (4-10)                        6 (4-10)                          7 (5-10)                           6 (4-9)
                    IDSd
                         Mean (SD)                                21.3 (9.8)                      21.6 (10.5)                       22.8 (10.2)                        21.4 (9.8)
                         Median (IQR)                             20 (14-27)                      21 (13-29)                        21 (15-30)                         20 (14-28)
                  Anxiety severitye
                    Mean (SD)                                     5.8 (4.4)                       6.2 (4.5)                         5.7 (3.8)                          5.4 (3.8)
                    Median (IQR)                                  5 (3-7)                         5 (3-9)                           5 (3-7)                            5 (3-7)
                  Health utilityf
                    Mean (SD)                                     0.87 (0.11)                     0.86 (0.13)                       0.86 (0.12)                        0.86 (0.12)
                    Median (IQR)                                  0.88 (0.82-0.94)                0.87 (0.81-0.95)                  0.87 (0.81-0.94)                   0.88 (0.81-0.94)
                  MooDFOOD diet score, mean (SD)g                 51.7 (7.6)                      51.9 (6.9)                        51.6 (6.8)                         51.4 (6.9)
                  Prior (multi)-nutrient supplement use           77 (30.0)                       86 (33.6)                         78 (30.5)                          79 (30.9)
                                                                                                    e
              Abbreviations: BMI, body mass index, calculated as weight in kilograms divided            Higher values (range, 0-21) indicate greater severity (ⱖ5 indicates mild
              by height in meters squared; EQ5D5L, EuroQol 5 dimension 5 level;                         anxiety; ⱖ10 moderate anxiety).
              GAD-7, Generalized Anxiety Disorder 7; IDS, Inventory of Depressive                   f
                                                                                                        Higher values (range, 0-1) indicate higher health utility (0, death; 1, full health).
              Symptomatology; IQR, interquartile range; MDD, major depressive disorder;                 Health utility is based on the tariff of England, which is an algorithm that can
              PHQ-9, Patient Health Questionnaire 9.                                                    be used to attach values to all health states derived from the health-related
              a
                  Low represents no education, primary education, or lower secondary                    quality-of-life EQ5D5L instruments, reflecting a country-specific preference
                  education; middle, upper secondary education; postsecondary nontertiary               on health states.
                  education, short-cycle tertiary education; high, bachelor’s degree or higher      g
                                                                                                        Higher values (range, 0-77) indicate better adherence to the
                  or equivalent level.                                                                  Mediterranean-style diet. The median intakes of each of the 11 MooDFOOD
              b
                  Represents the number of hours per day spent on commuting (walking and                diet score components were vegetables (2.8 times per day), fruit (1.9 times
                  cycling) and on work-related, household, leisure time, and sport activities.          per day), fish (1.5 times per week), legumes or pulses (1 times per week), meat
              c
                  Higher values (range, 0-27) indicate greater severity (ⱖ5 indicates mild              (5 times per week), whole grain products (67% of total grains), low-fat dairy
                  depression; ⱖ10, moderate depression).                                                (0.9 times per day), olive oil (33% of total dressings, cooking oils, and fats),
              d
                                                                                                        soft drinks (0.14 times per day), processed food (1.6 times per day), and
                  Higher values (range, 0-84) indicate greater severity (ⱖ14 indicates mild
                                                                                                        alcohol (0.14 times per day).
                  depression; ⱖ26 , moderate depression).



        862   JAMA March 5, 2019 Volume 321, Number 9 (Reprinted)                                                                                                                  jama.com

                                                             © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC-001 PDF page 6

Source: [PDF page 6](../../../jama_bot_2019_oi_190007.pdf#page=6)

```text
              Effect of Behavioral Therapy and Supplements on MDD Among Overweight and Obese Adults                                               Original Investigation Research




              Table 2. Effect of Supplements and Food-Related Behavioral Activation Therapy on Major Depressive Disorder Onset
                                                                                                      No. of Follow-up
                                                    No. of Patients              No. of Events        Dropoutsa                  Imputed OR (95% CI)b           P Valueb
                  Primary Outcome: 12-mo MDD Onset
                  Placeboc                          513                          51                   113                        1 [Reference]
                  Supplementsd                      512                          54                   126                        1.06 (0.87-1.29)               .57
                  Food-related behavioral
                  activation therapy
                    Noe                             513                          57                   122                        1 [Reference]
                    Yesf                            512                          48                   117                        0.93 (0.76-1.13)               .47
                  Supplements by therapyg           NA                           NA                   NA                         0.93 (0.76-1.14)               .48
                  Post Hoc Outcome: Time to MDD Onset
                                                    Time to Event                                                                HR (95% CI)
                                                    or Censoring
                                                    (Person-Months)
                  Placebo                           4656                         51                   113                        1 [Reference]
                  Supplements                       4488                         54                   126                        1.05 (0.86-1.27)               .65
                  Food-related behavioral
                  activation therapy
                    No                              4503                         57                   122                        1 [Reference]
                    Yes                             4641                         48                   117                        0.91 (0.75-1.10)               .32
                  Supplements by therapyg           NA                           NA                   NA                         0.91 (0.75-1.11)               .36
                                                                                                  d
              Abbreviations: HR, hazard ratio; MDD, major depressive disorder; NA, not                Thirty-two of 256 participants (12.5%) in the supplements without therapy
              applicable; OR, odds ratio.                                                             group and 22 of 256 (8.6%) in the supplements without therapy group.
              a                                                                                   e
                  No. that did not complete 12 mo follow-up and had no MDD at previous                Twenty-five of 257 participants (9.7%) in the placebo group without therapy
                  follow-up measurements.                                                             and 32 of 256 (12.5%) in the supplements without therapy group.
              b                                                                                   f
                  Derived from multiple imputed data. Models were adjusted for interventions,         Twenty-six of 256 participants (10.2%) in the placebo with therapy group and
                  site and history of MDD. Food-related behavioral activation therapy and pills       22 of 256 (8.6%) in the supplements with therapy group.
                  were effect-coded (−1,1).                                                       g
                                                                                                      Interaction between therapy and supplements.
              c
                  Twenty-five of 257 participants (9.7%) in the placebo without therapy group
                  and 26 of 256 (10.2%) in the placebo group with therapy.


              into account good adherence with the interventions, while                           months, and 246 (24%) at 12 months (Figure 1). In total, 239
              retaining the benefits of randomization for both primary and                        participants (23%) dropped out before the 12-month
              secondary 12-month follow-up outcomes (eAppendix 7 in                               follow-up or before the onset of MDD (the main outcome)
              Supplement 3). Analyses were conducted with R (version                              occurred. Missing rates for the primary outcome did not dif-
              3.4.4), using the packages geepack for the GEE analyses and                         fer between the 4 intervention groups at 3 months (P = .47),
              mice for multiple imputation. The 2-sided significance                              6 months (P = .62), and 12 months (P = .91). Missing rates for
              threshold was set at P = .05.                                                       the secondary outcomes of depressive symptoms, anxiety
                                                                                                  symptoms, and health utility scores obtained through self-
                                                                                                  report questionnaires were slightly higher: number of indi-
                                                                                                  viduals with missing data at baseline was 29 to 32, at 3
              Results                                                                             months 206 to 211, at 6 months 275 to 278, and at 12 months
              Description of Participants                                                         268 for these outcomes. These missing rates did not differ
              Between July 30, 2015, and October 12, 2016, 5965 individu-                         across intervention groups.
              als visited the online screening questionnaire, 2235 partici-
              pants fulfilled the key inclusion criteria, 1773 participants                       Adherence to Interventions
              completed the subsequent telephone screening, and 1250                              Adherence for each group is described in eAppendix 8 in
              were deemed eligible for the trial. After subsequent exclu-                         Supplement 3. Of all 12-month follow-up participants, pill
              sion of individuals not willing or able to participate, 1025                        weight data indicated that 77% of participants had adherence
              adults were randomly allocated to the 4 groups: placebo                             of more than 70% to the supplements or placebo. Of those
              without therapy (n = 257), placebo with therapy (n = 256),                          randomized to the therapy groups, 71% attended 8 or more of
              multinutrient supplements without therapy (n = 256), and                            the 21 sessions. A median of 14 of 15 individual sessions were
              multinutrient supplements w ith therapy (n = 256)                                   attended (interquartile range [IQR], 6-15), and a median of 0
              (Figure 1). Table 1 shows the baseline characteristics of the                       of 6 group sessions (IQR, 0-4) were attended, indicating that
              intervention groups.                                                                adherence to individual sessions was highest.

              Follow-up Attrition                                                                 Onset of MDD
              The number of participants not taking part in follow-up                             One hundred five participants (10%) developed an MDD
              assessment were 194 (19%) at 3 months, 254 (25%) at 6                               episode during the 12-month follow-up (Table 2): 25 partici-

              jama.com                                                                                                (Reprinted) JAMA March 5, 2019 Volume 321, Number 9            863

                                                            © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC-001 PDF page 7

Source: [PDF page 7](../../../jama_bot_2019_oi_190007.pdf#page=7)

```text
              Research Original Investigation                                                                                                 Effect of Behavioral Therapy and Supplements on MDD Among Overweight and Obese Adults




              Figure 2. Course of Depressive Symptoms, Anxiety Symptoms, and Health Utility per Intervention Group

                       A Supplements

                                             30                                                                        60                                                                25                                          1.0




                                                                                    Inventory of Depressive Symptoms
                                             25                                                                        50
                                                                                                                                                                                         20                                          0.8




              Patient Health Questionnaire                                                                                                                Generalized Anxiety Disorder
                                             20                                                                        40
                                                                                                                                                                                         15                                          0.6

                                                                                                                                                                                                                           Utility
                                             15                                                                        30

                                                                                                                                                                                         10                                          0.4
                                             10                                                                        20

                                                                                                                                                                                          5                                          0.2
                                             5                                                                         10


                                             0                                                                          0                                                                0                                            0

                                                   0      3     6      9     12                                              0    3     6     9    12                                          0     3     6    9    12                     0     3     6    9    12
                                                           Follow-up, mo                                                           Follow-up, mo                                                     Follow-up, mo                                Follow-up, mo
              No. of participants                                                   No. of participants                                                  No. of participants                                               No. of participants
                                                  996   819    750          757                                             994   817   747        757                                        993   815   747        757                   993   814   747        757


                       B                     Food-related behavioral activation therapy

                                             30                                                                        60                                                                25                                          1.0




                                                                                    Inventory of Depressive Symptoms
                                             25                                                                        50
                                                                                                                                                                                         20                                          0.8




              Patient Health Questionnaire                                                                                                                Generalized Anxiety Disorder
                                             20                                                                        40
                                                                                                                                                                                         15                                          0.6

                                                                                                                                                                                                                           Utility
                                             15                                                                        30

                                                                                                                                                                                         10                                          0.4
                                             10                                                                        20

                                                                                                                                                                                          5                                          0.2
                                             5                                                                         10


                                             0                                                                          0                                                                 0                                           0
                                                   0      3     6      9     12                                              0    3     6     9    12                                          0     3     6    9    12                     0     3     6    9    12
                                                           Follow-up, mo                                                           Follow-up, mo                                                     Follow-up, mo                                Follow-up, mo
              No. of participants                                                   No. of participants                                                  No. of participants                                               No. of participants
                                                  996   819    750          757                                             994   817   747        757                                        993   815   747        757                   993   814   747        757


              The boxplot inner horizontal lines represent the median, the boxes represent                                                                 bars indicate the intervention; the light blue bars, control. The No. of
              the interquartile range (25% and 75%), the vertical whiskers represent the 1.5                                                               participants represents the number of persons who completed the secondary
              interquartile range beyond the 25th and 75th percentiles, and the dots                                                                       outcomes at the different time points. Data shown are the available data.
              represent all other values. The diamonds represent the means. The dark blue


              pants (9.7%) receiving placebo alone, 26 (10.2%) receiving                                                                                   0.86-1.27; P = .65) or therapy (HR, 0.91; 95% CI, 0.75-1.10;
              placebo with therapy, 32 (12.5%) receiving supplements                                                                                       P = .32) or significant supplements × therapy interaction
              alone, and 22 (8.6%) receiving supplements with therapy.                                                                                     (HR, 0.91; 95% CI, 0.75-1.11; P for interaction, .36) on the time
              Considering the main effect of each intervention, the num-                                                                                   to first onset of MDD (Table 2).
              bers of participants who developed MDD were 51 participants
              (9.9%; 1.1 per 100 person-months) receiving placebo, 54                                                                                      Depressive Symptoms, Anxiety Symptoms,
              (10.5%; 1.2 per 100 person-months) receiving supplements,                                                                                    and Health Utility
              57 (11.1%; 1.3 per 100 person-months) not receiving therapy,                                                                                 Figure 2 shows boxplots and means of the secondary out-
              and 48 (9.4%; 1.0 per 100 person-months) receiving therapy.                                                                                  come scores at baseline and at 3, 6, and 12 months stratified
              Logistic regression using effect-coded intervention variables                                                                                by food-related behavioral activation and supplement groups
              (−1,1) showed no significant effect of supplements (OR, 1.06;                                                                                (see eAppendix 9 in Supplement 3 for figure stratified by the
              95% CI, 0.87-1.29; P = .57) or food-related behavioral activa-                                                                               4 intervention combinations). There were no significant supple-
              tion therapy (OR, 0.93, 95% CI, 0.76-1.13; P = .47) or signifi-                                                                              ment × food-related behavioral activation therapy interac-
              cant supplements × therapy interaction (OR, 0.93; 95% CI,                                                                                    tions for any of the secondary outcome scores (P values for in-
              0.76-1.14, P for interaction, .48) on the onset of MDD. There                                                                                teraction ranged from .41 to .98). Table 3 presents effects on
              was no significant effect of supplements (HR, 1.05; 95% CI,                                                                                  secondary outcomes. Food-related behavioral activation

        864   JAMA March 5, 2019 Volume 321, Number 9 (Reprinted)                                                                                                                                                                                            jama.com

                                                                                                                       © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC-001 PDF page 8

Source: [PDF page 8](../../../jama_bot_2019_oi_190007.pdf#page=8)

```text
              Effect of Behavioral Therapy and Supplements on MDD Among Overweight and Obese Adults                                                      Original Investigation Research




              Table 3. Effect of Supplements and Food-Related Behavioral Activation Therapy on Secondary Outcomesa

                                                      Overall Follow-up Effect Using All Follow-upsb                   Effect at 12 Month Follow-upc
                  Outcomes                            Estimate (95% CI)d                       P Value                 Estimate (95% CI)d                   P Value       Cohen D Valuee
                  Patient Health Questionnaire 9
                  Supplements vs placebo              0.33 (0.12 to 0.53)                      .002                    0.28 (0.05 to 0.50)                  .02           0.10
                  With vs without food-related        −0.13 (−0.33 to 0.07)                    .19                     −0.17 (−0.39 to 0.06)                .14           −0.02
                  behavioral activation therapy
                  Inventory of Depressive Symptomatology
                  Supplements vs placebo              0.60 (0.15 to 1.05)                      .01                     0.36 (−0.19 to 0.90)                 .20           0.05
                  With vs without food-related        −0.23 (−0.67 to 0.22)                    .32                     −0.28 (−0.83 to 0.27)                .31           0.006
                  behavioral activation therapy
                  Generalized Anxiety Disorder 7
                  Supplements vs placebo              0.25 (0.08 to 0.42)                      .004                    0.14 (−0.04 to 0.33)                 .13           0.10
                  With vs without food-related        −0.16 (−0.32 to 0.01)                    .06                     −0.24 (−0.42 to −0.06)               .01           −0.07
                  behavioral activation therapy
                  Utility
                  Supplements vs placebo              −0.006 (−0.012 to 0.000)                 .052                    −0.002 (−0.008 to 0.005)             .61           −0.07
                  With vs without food-related        0.002 (−0.003 to 0.008)                  .44                     0.004 (−0.002 to 0.009)              .23           0.08
                  behavioral activation therapy
              Abbreviation: estimate, unstandardized regression coefficient.                                 longitudinal (GEE) analyses using effect-coded interventions based on
              a
                  The 2 interventions were modeled together. All models were adjusted                        multiple imputed data.
                                                                                                         c
                  for study site, history of major depressive disorder, and for the baseline                 Estimates were obtained from robust linear regression analyses based on
                  value of the corresponding outcome measure. Food-related                                   multiple imputed data.
                  behavioral activation therapy and pills were effect-coded (−1,1),                      d
                                                                                                             To obtain adjusted mean differences in outcomes between the intervention
                  supplement × food-related activation interaction therapy interaction                       conditions, the estimates and 95% CIs should be multiplied by 2.
                  effects were not included in the model because none of the interactions                e
                                                                                                             The Cohen D value was calculated from baseline and 12-month follow-up
                  were statistically significant.
                                                                                                             means and pooled standard deviations obtained from multiple imputed data.
              b
                  Estimates were obtained from generalized estimating equations




              therapy was significantly related to lower GAD scores at 12                                higher, (2) the use of supplements resulted in higher
              months (adjusted mean difference, −0.48; 95% CI, −0.84 to                                  follow-up anxiety scores when the baseline anxiety severity
              −0.12; P = .01). The unadjusted baseline GAD score for both the                            scores were higher, and (3) that the effect of food-related
              therapy and nontherapy group was 5.8. At 12 months, the un-                                behavioral activation on health utility scores at 12 months
              adjusted score was 3.9 for the nontherapy group vs 3.2 for the                             was larger in the United Kingdom than in the Netherlands.
              therapy group. No effect of therapy on other secondary out-                                Sensitivity analyses for depression, anxiety, and health utility
              comes was found.                                                                           scores without multiple imputed data gave comparable effect
                  There was a significant effect of supplements on overall                               estimates (eAppendix 11 in Supplement 3). The results of the
              follow-up measures of the PHQ (adjusted mean difference,                                   Complier Average Causal Effect (CACE) analyses were consis-
              0.65; 95% CI, 0.25-1.06; P = .002), the IDS (adjusted mean                                 tent with the original analyses, finding no effect of supple-
              difference, 1.20; 95% CI, 0.29-2.10; P = .01), and the GAD (ad-                            ments on the primary outcome, and similar effects for sec-
              justed mean difference, 0.50; 95% CI, 0.16-0.84; P = .004)                                 ondary outcomes (eAppendix 12 in Supplement 3). The CACE
              scores. There was also a significant effect on PHQ scores at                               analyses found a significant effect of food-related behavioral
              the 12-month follow-up (adjusted mean difference, 0.56;                                    activation therapy on the primary outcome (OR, 0.78; 95%
              95% CI, 0.11-1.01; P = .02). The unadjusted baseline PHQ for                               CI, 0.64-0.95), accounting for treatment adherence.
              those taking placebo was 7.3 vs 7.5 for those taking supple-
              ments. The unadjusted 12-month PHQ score for placebo was                                   Adverse Events and Concealment
              4.1 vs 4.9 for supplements. This indicates less improvement                                Ninety-eight participants were hospitalized and 1 participant
              in depressive and anxiety symptoms for supplements relative                                died during the 12-month follow-up, these events were judged
              to placebo.                                                                                as unrelated to interventions (eAppendix 8 in Supplement 3).
                                                                                                         Those receiving placebo were less likely to believe they were
              Effect Modification and Sensitivity Analyses                                               taking multinutrients than did those receiving multinutri-
              The eAppendix 10 in Supplement 3 shows the results of post                                 ents (placebo without therapy, 8.2%; placebo with therapy,
              hoc effect modification analyses by study site, history of                                 10.4%; multinutrients without therapy, 25.5%; and multi-
              depression, and baseline symptoms scores. These analyses                                   nutrients with therapy, 43.7%; P < .001; eAppendix 13 in
              suggested that (1) the effect of food-related behavioral activa-                           Supplement 3). Of those completing the questions on conceal-
              tion therapy on PHQ at 12 months was more favorable (larger                                ment at the 12-month follow-up, 40.4% reported that they did
              reduction) when the baseline PHQ depression severity was                                   not know their allocation.

              jama.com                                                                                                       (Reprinted) JAMA March 5, 2019 Volume 321, Number 9           865

                                                              © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC-001 PDF page 9

Source: [PDF page 9](../../../jama_bot_2019_oi_190007.pdf#page=9)

```text
              Research Original Investigation                                   Effect of Behavioral Therapy and Supplements on MDD Among Overweight and Obese Adults



                                                                                             fect size comparable with that reported in (meta-analytic) stud-
              Discussion                                                                     ies of psychological interventions for depression.28,35,40 In a
                                                                                             post hoc analysis, a more beneficial effect of food-related be-
              This multicenter trial involving 1025 overweight individuals                   havioral activation therapy on depressive symptoms for those
              with subsyndromal depressive symptoms showed no effect                         with higher baseline depression scores was observed. This sug-
              from multinutrient supplements, food-related behavioral ac-                    gests that with sufficient dose and a higher-risk sample, food-
              tivation therapy, or their combination on the 1-year cumula-                   related behavioral activation therapy might prevent depres-
              tive onset of MDD.                                                             sion, although this requires further study. It would be relevant
                   To our knowledge, this is the first randomized trial evalu-               to study which characteristics make participants more likely
              ating the effectiveness of 2 nutritional strategies and their com-             to adhere to the intervention, to identify persons who may ben-
              bination for the prevention of depression in a high-risk group                 efit from it.
              of overweight people. Despite the large sample size and selec-                      The strengths of this study are the randomized 2 × 2 fac-
              tion of people with elevated depressive symptoms, the onset                    torial design, the inclusion of participants from 4 countries with
              of MDD was lower than expected, which reduced the statisti-                    different background characteristics and dietary patterns, the
              cal power to detect a statistically significant effect. Compari-               large sample size compared with other prevention studies of
              sons of intervention effects with other trials are difficult due               depression,35 the intervention and follow-up period of 1 year,
              to methodological and sample differences. Compared with pre-                   the efficient testing of multiple nutrients, the blinded design,
              vious trials testing preventive psychological strategies for de-               its measurement of multiple outcome assessments, and the ac-
              pression that found significant effects,35 our sample had on av-               tive adherence monitoring.
              erage lower initial levels of depressive symptoms and lower
              likelihood of having a history of MDD, making them less vul-                   Limitations
              nerable to MDD onset.                                                          This study has several limitations. First, the onset of MDD
                   The adherence to both interventions was adequate, with                    was lower than expected, which resulted in lower power to
              about three-quarters fulfilling predefined adherence criteria for              detect significant effects, if present. However, because pla-
              the interventions. For food-related behavioral activation, the in-             cebo outperformed supplements for some secondary out-
              dividual sessions in the first 6 months were well attended, but                comes, it is unlikely that inclusion of an adequately powered
              the group sessions in the subsequent 6 months were not.                        sample would favor supplements for the prevention of
                   This study showed that multinutrient supplements con-                     depression. Second, a considerable number of participants
              taining omega-3 PUFAs, vitamin D, folic acid, and selenium nei-                (about a quarter) was lost to follow-up. Although this number
              ther reduced depressive symptoms, anxiety symptoms, nor im-                    was balanced between intervention groups, attrition bias
              proved health utility measures. In fact, they appeared to result               cannot be ruled out. Third, those who received placebo were
              in slightly poorer depressive and anxiety symptoms scores                      less likely to believe they were taking multinutrients, which
              compared with placebo. Despite substantial evidence of ob-                     suggests that the blinding of participants was not optimal.
              servational studies linking lower nutrient levels to higher de-                Fourth, participants were not selected based on deficiencies
              pressive symptoms, similar to our findings, a review of 9 RCTs                 in the specific nutrients provided. It is conceivable that defi-
              found no support that vitamin D could prevent depression in                    cient individuals will be more likely to benefit from supple-
              older adults.12 For omega-3 PUFAs, one RCT involving mild to                   mentation, but studies addressing this are scarce.12 Fifth, no
              moderately depressed individuals—a population that is some-                    active control group for the food-related behavioral activa-
              what comparable with our sample—also showed no favorable                       tion therapy component was present. Sixth, the predefined
              effect of omega-3 PUFAs on depressive symptoms.36 No ef-                       follow-up time of this study was 1 year, which might have
              fect of folic acid combined with vitamin B6 and B12 was found                  been too short to detect an effect.
              on the onset of depression in older men37 and older women.38
              Furthermore, Rayman et al39 found no effect of selenium on
              mood in older adults. Overall, the studies available thus far,
              including our trial, do not support the use of nutritional supple-
                                                                                             Conclusions
              mentation in the prevention of depression.12                                   Among overweight or obese adults with subsyndromal de-
                   Food-related behavioral activation therapy had a signifi-                 pressive symptoms, multinutrient supplementation com-
              cant effect on reduction in anxiety symptoms at 12 months but                  pared with placebo and food-related behavioral activation
              not on any of the other secondary mental health outcomes.                      therapy compared with no therapy did not reduce episodes of
              When accounting for a priori defined intervention adherence                    major depressive disorder during 1 year. These findings do not
              (ie, attending ≥8 of 21 sessions), food-related behavioral acti-               support the use of these interventions for prevention of ma-
              vation therapy was related to lower MDD onset, with an ef-                     jor depressive disorder in this population.


              ARTICLE INFORMATION                                 research institute, GGZ inGeest Specialized Mental   Amsterdam, Amsterdam, the Netherlands
              Accepted for Publication: January 28, 2019.         Health Care, Amsterdam, the Netherlands (Bot,        (Brouwer, Cabout, Visser); Institut Universitari d’
                                                                  Penninx, van Grootheest); Department of Health       Investigació en Ciències de la Salut, Idisba, Rediapp,
              Author Affiliations: Amsterdam UMC, Vrije           Sciences, Faculty of Science and Amsterdam Public    University of Balearic Islands, Palma de Mallorca,
              Universiteit, Psychiatry, Amsterdam Public Health   Health research institute, Vrije Universiteit        Spain (Roca, Gili); Department of Psychiatry and



        866   JAMA March 5, 2019 Volume 321, Number 9 (Reprinted)                                                                                                  jama.com

                                                         © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC-001 PDF page 10

Source: [PDF page 10](../../../jama_bot_2019_oi_190007.pdf#page=10)

```text
              Effect of Behavioral Therapy and Supplements on MDD Among Overweight and Obese Adults                                                Original Investigation Research



              Psychotherapy, University Leipzig, Medical Faculty,      of the trial were staff members at the respective        6. Jacka FN, O’Neil A, Opie R, et al. A randomised
              Leipzig, Germany (Kohls, Hegerl); Department of          institutions and received no further compensation.       controlled trial of dietary improvement for adults
              Psychology, University of Exeter, Exeter, United         Conflict of Interest Disclosures: Dr Roca reported       with major depression (the ‘SMILES’ trial). BMC Med.
              Kingdom (Watkins, Owens).                                receiving grants from the European Union and             2017;15(1):23. doi:10.1186/s12916-017-0791-y
              Author Contributions: Dr Bot had full access to all      research funding from Janssen and Lundbeck               7. Parletta N, Zarnowiecki D, Cho J, et al.
              of the data in the study and takes responsibility for    outside the submitted work. Dr Penninx reported          A Mediterranean-style dietary intervention
              the integrity of the data and the accuracy of the        receiving grants from Janssen Research and               supplemented with fish oil improves diet quality
              data analysis.                                           Boehringer Ingelheim. Dr Watkins reported                and mental health in people with depression:
              Concept and design: Bot, Brouwer, Roca, Kohls,           receiving royalties for a therapy manual in              A randomized controlled trial (HELFIMED). Nutr
              Penninx, Watkins, van Grootheest, Cabout,                Behavioural Activation/Cognitive Behavioural             Neurosci. 2017;1-14. doi:10.1080/1028415X.2017.
              Gili, Visser.                                            Therapy from Guilford Press; and honorarium for          1411320
              Acquisition, analysis, or interpretation of data: Bot,   running workshops in his rumination-focused              8. Opie RS, O’Neil A, Itsiopoulos C, Jacka FN. The
              Brouwer, Kohls, Penninx, Watkins, van Grootheest,        cognitive behavioral therapy from different national     impact of whole-of-diet interventions on
              Cabout, Hegerl, Gili, Owens, Visser.                     cognitive behavioral therapy organizations               depression and anxiety: a systematic review of
              Drafting of the manuscript: Bot, Roca, Kohls, Gili,      worldwide. Dr Hegerl reported receiving personal         randomised controlled trials. Public Health Nutr.
              Owens, Visser.                                           fees from Lundbeck, Janssen Pharmaceutica,               2015;18(11):2074-2093. doi:10.1017/
              Critical revision of the manuscript for important        Servier, Bayer Pharma, and Medice.                       S1368980014002614
              intellectual content: Brouwer, Kohls, Penninx,           Funding/Support: Funding for this article was
              Watkins, van Grootheest, Cabout, Hegerl, Gili,                                                                    9. Milaneschi Y, Hoogendijk W, Lips P, et al. The
                                                                       provided by the European Union FP7 MooDFOOD              association between low vitamin D and depressive
              Owens, Visser.                                           Project Multi-country Collaborative Project on the
              Statistical analysis: Bot, Watkins, Owens.                                                                        disorders. Mol Psychiatry. 2014;19(4):444-451. doi:
                                                                       Role of Diet, Food-related Behavior, and Obesity in      10.1038/mp.2013.36
              Obtained funding: Brouwer, Penninx, Gili, Visser.        the Prevention of Depression (grant agreement
              Administrative, technical, or material support: Kohls,   613598). This work is supported in the United            10. Sarris J, Murphy J, Mischoulon D, et al.
              Penninx, Watkins, van Grootheest, Cabout,                Kingdom by the National Institute for Health             Adjunctive nutraceuticals for depression:
              Owens, Visser.                                           Research (NIHR), through the Primary Care                a systematic review and meta-analyses. Am J
              Supervision: Bot, Brouwer, Roca, Kohls, Penninx,         Research Network and the NIHR Exeter Clinical            Psychiatry. 2016;173(6):575-587. doi:10.1176/appi.ajp.
              Watkins, Hegerl, Gili, Owens, Visser.                    Research Facility.                                       2016.15091228
              MooDFOOD Prevention Trial Investigators: We              Role of the Funder/Sponsor: The funders had no           11. Mocking RJT, Harmsen I, Assies J, Koeter MWJ,
              thank further all nonauthor members of this trial:       role in the design and conduct of the study;             Ruhé HG, Schene AH. Meta-analysis and
              Bep Verkerk, post-BSc (data manager, GGZ inGeest         collection, management, analysis, and                    meta-regression of omega-3 polyunsaturated fatty
              Specialized Mental Health Care, Amsterdam, the           interpretation of the data; preparation, review, or      acid supplementation for major depressive
              Netherlands), Nadine Paans, MSc (field center            approval of the manuscript; and decision to submit       disorder. Transl Psychiatry. 2016;6(3):e756. doi:10.
              therapist and research assistant, Amsterdam UMC,         the manuscript for publication.                          1038/tp.2016.29
              Vrije Universiteit, Amsterdam, the Netherlands),                                                                  12. Okereke OI, Singh A. The role of vitamin D in the
              Carisha Thesing, MSc (field center therapist,            Data Sharing Statement: See Supplement 4
                                                                                                                                prevention of late-life depression. J Affect Disord.
              Amsterdam UMC, Vrije Universiteit, Amsterdam,            Additional Contributions: We thank Mohammod              2016;198:1-14. doi:10.1016/j.jad.2016.03.022
              the Netherlands), Deborah Gibson-Smith, MSc              Mostazir, MSc (College of Life and Environmental
              (field center research assistant, Amsterdam UMC,         Sciences, University of Exeter) for his assistance       13. Milaneschi Y, Simmons WK, van Rossum EFC,
              Vrije Universiteit, Amsterdam, the Netherlands),         with the CACE analyses, and Adriaan Hoogendoorn,         Penninx BW. Depression and obesity: evidence of
              Melany Horsfall, MSc (field center coordinator, GGZ      PhD (GGZ inGeest Specialized Mental Health Care,         shared biological mechanisms. Mol Psychiatry.
              inGeest Specialized Mental Health Care,                  Amsterdam, the Netherlands) for his advice for the       2019;24(1):18-33. doi:10.1038/s41380-018-0017-5
              Amsterdam, the Netherlands), Lena Weiss, MSc             statistical analyses. Neither received compensation      14. Roca M, Kohls E, Gili M, et al; MooDFOOD
              (field center research assistant, Amsterdam UMC,         for their roles.                                         Prevention Trial Investigators. Prevention of
              Vrije Universiteit, Amsterdam, the Netherlands),                                                                  depression through nutritional strategies in
              Amy Romijn, PhD (field postdoctoral research             REFERENCES                                               high-risk persons: rationale and design of the
              associate, University of Exeter, Exeter, United          1. Kessler RC, Wang PS. The descriptive                  MooDFOOD prevention trial. BMC Psychiatry. 2016;
              Kingdom), Hannah Bunce, MSc (field center                epidemiology of commonly occurring mental                16(1):192. doi:10.1186/s12888-016-0900-z
              associate research fellow), Owain Winfield, BSc          disorders in the United States. Annu Rev Public          15. Kroenke K, Spitzer RL, Williams JBW. The
              (research therapist, University of Exeter, Exeter,       Health. 2008;29:115-129. doi:10.1146/annurev.            PHQ-9: validity of a brief depression severity
              United Kingdom), Harriet Bunker-Smith, MSc (field        publhealth.29.020907.090847                              measure. J Gen Intern Med. 2001;16(9):606-613.
              center associate research fellow, University of                                                                   doi:10.1046/j.1525-1497.2001.016009606.x
              Exeter, Exeter, United Kingdom), Fern Durbridge,         2. Vos T, Flaxman AD, Naghavi M, et al. Years lived
              BSc (field center associate research fellow,             with disability (YLDs) for 1160 sequelae of 289          16. Sheehan DV, Lecrubier Y, Sheehan KH, et al.
              University of Exeter, Exeter, United Kingdom),           diseases and injuries 1990-2010: a systematic            The Mini-International Neuropsychiatric Interview
              Caterina Versari Molinares, MSc (research intern,        analysis for the Global Burden of Disease Study          (M.I.N.I.): the development and validation of a
              University of Exeter, Exeter, United Kingdom),           2010. Lancet. 2012;380(9859):2163-2196. doi:10.          structured diagnostic psychiatric interview for
              Atikah Sapar, BSc (research intern, University of        1016/S0140-6736(12)61729-2                               DSM-IV and ICD-10. J Clin Psychiatry. 1998;59(suppl
              Exeter, Exeter, United Kingdom), Miquel Tortella,        3. Cuijpers P, Beekman ATF, Reynolds CF III.             20):22-33. http://www.ncbi.nlm.nih.gov/pubmed/
              PhD (field center coinvestigator, UIB, Palma de          Preventing depression: a global priority. JAMA.          9881538.
              Mallorca, Spain), Clara Homar Covas, MSc (field          2012;307(10):1033-1034. doi:10.1001/jama.2012.271        17. Ekers D, Webster L, Van Straten A, Cuijpers P,
              center research and therapist, UIB, Palma de             4. Molendijk M, Molero P, Ortuño                         Richards D, Gilbody S. Behavioural activation for
              Mallorca, Spain), M. Angeles Pérez-Ara, PhD (field       Sánchez-Pedreño F, Van der Does W, Angel                 depression; an update of meta-analysis of
              center research assistant, UIB, Palma de Mallorca,       Martínez-González M. Diet quality and depression         effectiveness and sub group analysis. PLoS One.
              Spain), Adoración Castro Gracia, MSc (field center       risk: a systematic review and dose-response              2014;9(6):e100100. doi:10.1371/journal.pone.
              research assistant, UIB, Palma de Mallorca, Spain),      meta-analysis of prospective studies. J Affect Disord.   0100100
              José Luis Reig, MSc (field center therapist, UIB,        2018;226:346-354. doi:10.1016/j.jad.2017.09.022          18. Rush AJ, Gullion CM, Basco MR, Jarrett RB,
              Palma de Mallorca, Spain), Jana Hoesel (field center                                                              Trivedi MH. The Inventory of Depressive
              study nurse, ULEI, Leipzig, Germany), Ezgi Dogan,        5. Paans NPG, Bot M, van Strien T, Brouwer IA,
                                                                       Visser M, Penninx BWJH. Eating styles in major           Symptomatology (IDS): psychometric properties.
              MD (field center research fellow, ULEI, Leipzig,                                                                  Psychol Med. 1996;26(3):477-486. doi:10.1017/
              Germany), Sabrina Baldofski, PhD (field center           depressive disorder: Results from a large-scale
                                                                       study. J Psychiatr Res. 2018;97:38-46. doi:10.1016/j.    S0033291700035558
              therapist, ULEI, Leipzig, Germany), and Nicole
              Mauche, MSc (field center therapist). All members        jpsychires.2017.11.003                                   19. Spitzer RL, Kroenke K, Williams JBW, Löwe B.
                                                                                                                                A brief measure for assessing generalized anxiety



              jama.com                                                                                                (Reprinted) JAMA March 5, 2019 Volume 321, Number 9                867

                                                            © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```

### DOC-001 PDF page 11

Source: [PDF page 11](../../../jama_bot_2019_oi_190007.pdf#page=11)

```text
              Research Original Investigation                                         Effect of Behavioral Therapy and Supplements on MDD Among Overweight and Obese Adults



              disorder: the GAD-7. Arch Intern Med. 2006;166           interventions. Am J Psychiatry. 2008;165(10):1272-      35. van Zoonen K, Buntrock C, Ebert DD, et al.
              (10):1092-1097. doi:10.1001/archinte.166.10.1092         1280. doi:10.1176/appi.ajp.2008.07091422                Preventing the onset of major depressive disorder:
              20. EuroQol Group. EuroQol—a new facility for the        27. van’t Veer-Tazelaar PJ, van Marwijk HWJ,            a meta-analytic review of psychological
              measurement of health-related quality of life.           van Oppen P, et al. Stepped-care prevention of          interventions. Int J Epidemiol. 2014;43(2):318-329.
              Health Policy. 1990;16(3):199-208. doi:10.1016/          anxiety and depression in late life: a randomized       doi:10.1093/ije/dyt175
              0168-8510(90)90421-9                                     controlled trial. Arch Gen Psychiatry. 2009;66(3):      36. Rogers PJ, Appleton KM, Kessler D, et al.
              21. Devlin NJ, Shah KK, Feng Y, Mulhern B,               297-304. doi:10.1001/archgenpsychiatry.2008.555         No effect of n-3 long-chain polyunsaturated fatty
              van Hout B. Valuing health-related quality of life:      28. Buntrock C, Ebert DD, Lehr D, et al. Effect of      acid (EPA and DHA) supplementation on depressed
              An EQ-5D-5L value set for England. Health Econ.          a web-based guided self-help intervention for           mood and cognitive function: a randomised
              2018;27(1):7-22. doi:10.1002/hec.3564                    prevention of major depression in adults with           controlled trial. Br J Nutr. 2008;99(2):421-431. doi:
                                                                       subthreshold depression. JAMA. 2016;315(17):1854-       10.1017/S0007114507801097
              22. de Lauzon B, Romon M, Deschamps V, et al;
              Fleurbaix Laventie Ville Sante Study Group. The          1863. doi:10.1001/jama.2016.4326                        37. Ford AH, Flicker L, Thomas J, Norman P,
              Three-Factor Eating Questionnaire-R18 is able to         29. Collins LM, Dziak JJ, Kugler KC, Trail JB.          Jamrozik K, Almeida OP. Vitamins B12, B6, and folic
              distinguish among different eating patterns in a         Factorial experiments: efficient tools for evaluation   acid for onset of depressive symptoms in older
              general population. J Nutr. 2004;134(9):2372-2380.       of intervention components. Am J Prev Med. 2014;        men: results from a 2-year placebo-controlled
              doi:10.1093/jn/134.9.2372                                47(4):498-504. doi:10.1016/j.amepre.2014.06.021         randomized trial. J Clin Psychiatry. 2008;69(8):
                                                                                                                               1203-1209. doi:10.4088/JCP.v69n0801
              23. Garcia-Larsen V, Luczynska M, Kowalski ML,           30. Rubin DB. Multiple Imputation for Nonresponse
              et al; GA2LEN-WP 1.2 ‘Epidemiological and Clinical       in Surveys. New York, NY: Wiley; 2004.                  38. Okereke OI, Cook NR, Albert CM,
              Studies’. Use of a common food frequency                                                                         Van Denburgh M, Buring JE, Manson JE. Effect of
                                                                       31. Twisk JWR, Bosman L, Hoekstra T, Rijnhart J,        long-term supplementation with folic acid and
              questionnaire (FFQ) to assess dietary patterns and       Welten M, Heymans M. Different ways to estimate
              their relation to allergy and asthma in Europe: pilot                                                            B vitamins on risk of depression in older women.
                                                                       treatment effects in randomised controlled trials.      Br J Psychiatry. 2015;206(4):324-331. doi:10.1192/
              study of the GA2LEN FFQ. Eur J Clin Nutr. 2011;65        Contemp Clin Trials Commun. 2018;10(June):80-85.
              (6):750-756. doi:10.1038/ejcn.2011.15                                                                            bjp.bp.114.148361
                                                                       doi:10.1016/j.conctc.2018.03.008
              24. Wendel-Vos GCW, Schuit AJ, Saris WHM,                                                                        39. Rayman M, Thompson A, Warren-Perry M,
                                                                       32. Morris SB. Estimating effect sizes from             et al. Impact of selenium on mood and quality of
              Kromhout D. Reproducibility and relative validity of     pretest-posttest-control group designs. Organ Res
              the short questionnaire to assess health-enhancing                                                               life: a randomized, controlled trial. Biol Psychiatry.
                                                                       Methods. 2008;11(2):364-386. doi:10.1177/               2006;59(2):147-154. doi:10.1016/j.biopsych.2005.
              physical activity. J Clin Epidemiol. 2003;56(12):1163-   1094428106291059
              1169. doi:10.1016/S0895-4356(03)00220-8                                                                          06.019
                                                                       33. Angrist JD, Imbens GW, Rubin DB.                    40. Bellón JA, Moreno-Peral P, Motrico E, et al.
              25. Stunkard AJ, Sørensen T, Schulsinger F. In: Kety     Identification of Causal Effects Using Instrumental
              S, Roland L, Sidman R, Matthysse S, eds. Use of the                                                              Effectiveness of psychological and/or educational
                                                                       Variables. J Am Stat Assoc. 1996;91(434):444-455.       interventions to prevent the onset of episodes of
              Danish Adoption Register for the Study of Obesity        https://dash.harvard.edu/handle/1/3382969. doi:10.
              and Thinness. The Geneti. New York, NY: Raven Press;                                                             depression: A systematic review of systematic
                                                                       1080/01621459.1996.10476902                             reviews and meta-analyses. Prev Med. 2015;76
              1983.
                                                                       34. Emsley R, Dunn G, White IR. Mediation and           (suppl):S22-S32. doi:10.1016/j.ypmed.2014.11.003
              26. Cuijpers P, van Straten A, Smit F, Mihalopoulos      moderation of treatment effects in randomised
              C, Beekman A. Preventing the onset of depressive         controlled trials of complex interventions. Stat
              disorders: a meta-analytic review of psychological       Methods Med Res. 2010;19(3):237-270. doi:10.1177/
                                                                       0962280209105014




        868   JAMA March 5, 2019 Volume 321, Number 9 (Reprinted)                                                                                                          jama.com

                                                            © 2019 American Medical Association. All rights reserved.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/30/2026

```
