# Main quantitative evidence map — Workflow 1.6.2

Scope: DOC-001, REPORT, `jama_flint_2019_oi_190079.pdf`, all PDF pages 1–10 (printed pages 622–631). Fresh scientific mapping of all reusable-backed pages; no fresh-required page gap. This is an evidence map, with no candidate diagnosis or adjudication. Numeric IDs N001–N079 and inferential IDs S001–S039 are reserved for this main-paper scope. A table row is one relationship comprising both arms and all displayed components, rather than one ID per number.

Evidence provenance: reusable `.ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-NNN.txt` for all 10 pages was read as a locator. Direct Poppler `pdftotext -layout jama_flint_2019_oi_190079.pdf .ai_paper_validation/review_1_6_2/preprocessing/main_mapping/direct_layout.txt` supplies a new full-source layout derivative. Direct Poppler CPU `pdftoppm -f 3 -l 9 -scale-to 1800 -png jama_flint_2019_oi_190079.pdf .ai_paper_validation/review_1_6_2/preprocessing/main_mapping/direct-page` supplies seven exact-source images, pp.3–9. Figures and every table were visually inspected against those images. No OCR or fallback was needed. Direct-source text and images govern the transcription. No old scientific conclusions were read.

All locations below are exact PDF pages; source link base from this artifact is [DOC-001](../../../jama_flint_2019_oi_190079.pdf#page=1). O means sertraline plus olanzapine (randomized n=64); P means sertraline plus placebo (randomized n=62). These shorthand labels never imply crude/model equivalence.

## Unit coverage and applicability

| PDF page | Printed page | Complete applicability map |
|---|---:|---|
| 1 | 622 | Abstract: population, design, treatment, completion, age/sex/dose summaries, relapse counts and Cox result, all eight anthropometric/metabolic estimates and intervals, 36-week conclusion. |
| 2 | 623 | Key Points repeat relapse population/counts/percentages and significance. Methods define all three phases, acute eligibility, remission, dose targets, exclusions, hypothesis and aims. Background literature figures are contextual and are not trial result relationships. |
| 3 | 624 | Complete Figure 1 participant flow and treatment/analysis sets; near-remission, stabilization and MMSE eligibility definitions. |
| 4 | 625 | Allocation, strata, intervention/taper, assessments, outcome and safety definitions, power/revised sample, Cox/mixed-model specifications. |
| 5 | 626 | Complete Table 1 baseline rows and footnotes; continuation of random-intercept Poisson, missingness/pattern-mixture and metabolic drug sensitivity models. |
| 6 | 627 | Complete Table 2 and scale footnotes; multiplicity/sidedness/significance, software/conversions, primary result and first covariate result. |
| 7 | 628 | Complete Table 3; complete Figure 2 counts, axes, intervals/caption; remaining Cox results, NNT/sensitivity, all eight secondary results, drug counts, SAS and other safety results. |
| 8 | 629 | Complete Table 4 (all eight outcomes, both arms, all available n and intervals), footnote/conversions; psychiatric hospitalization fraction; matching discussion claims. |
| 9 | 630 | Complete Table 5 (all four rows/definitions/counts/percentages/differences/intervals); numerical limitations and conclusion; administrative author/disclosure material has no additional trial relationships. |
| 10 | 631 | Read in full: funder/disclosures, contribution/data-sharing pointer, references. No applicable original trial result/statistical relationship; bibliographic years/pages, grant numbers and cited external literature are not quantitative outcomes of this trial. |

## Numeric relationships

Every percentage below is printed, and its natural count/column denominator is retained for checking; no adjusted estimate is replaced by a crude computation.

| ID | Exact location | Quantity, population/time, printed relationship and matching occurrence |
|---|---|---|
| N001 | p.1 abstract Design; p.2 Methods; p.9 Conclusions | RCT 36 weeks, 4 academic centers, age ≥18; acute treatment up to 12 weeks, stability 8 weeks; November 2011–June 2017, final follow-up June 13, 2017. p.2 eligibility is age 18–85. |
| N002 | p.1 abstract Results | Randomized 126; mean age 55.3 (SD 14.9) years; 78 women (61.9%); 114 completed (90.5%). Matching arm age/sex values N018,N022 and flow N015,N016. |
| N003 | p.1 Intervention/Results; p.2 Key Points; p.6 Primary Outcome; p.3 Figure 1 | O n=64, P n=62; relapses O 13 (20.3%), P 34 (54.8%); same printed counts in each location. All continued sertraline. |
| N004 | p.1 abstract Results; p.6 Table 2 dosage | Median sertraline 150 mg/d (IQR 150–200), olanzapine 15 mg/d (IQR 10–20); both arm dosage summaries repeat these values in Table 2. |
| N005 | p.3 Figure 1 top | 350 consented and assessed; 81 excluded: 60 not eligible, 16 withdrew consent, 5 other; 269 started open-label treatment. p.6 Results describes 269 as enrolled. |
| N006 | p.3 Figure 1 acute discontinuation | 74 discontinued: 31 consent withdrawal, 21 insufficient response/clinical worsening, 7 not appropriate for research, 5 adverse events, 1 medical event, 9 other. 195 completed acute treatment. |
| N007 | p.3 Figure 1 acute-to-stabilization | 195 acute completers; 33 excluded for symptoms not remitting; 162 entered open-label stabilization. |
| N008 | p.3 Figure 1 stabilization discontinuation | 15 discontinued: 4 clinical worsening, 2 consent withdrawal, 1 death not suicide, 1 not appropriate for research, 7 other; 147 completed stabilization. |
| N009 | p.3 Figure 1 randomization gate | 147 stabilization completers; 21 not randomized (12 not eligible, 9 did not consent); 126 randomized. |
| N010 | p.3 Figure 1 O treatment | 64 randomized O; 59 received treatment as randomized; 5 did not (3 discontinued, 2 switched to open-label olanzapine). |
| N011 | p.3 Figure 1 P treatment | 62 randomized P; 60 received treatment as randomized; 2 did not (1 discontinued, 1 switched to open-label olanzapine). |
| N012 | p.3 Figure 1 O analysis | 64 primary analysis; 43 completed remission/near remission; 13 relapsed; 8 discontinued (1 death not suicide, 5 consent withdrawal, 1 moved, 1 transport problems). |
| N013 | p.3 Figure 1 P analysis | 62 primary analysis; 24 completed remission/near remission; 34 relapsed; 4 discontinued (1 medical event, 3 consent withdrawal). |
| N014 | pp.2–3 Participants | HDRS-17 acute ≥21, SADS delusion severity ≥3 and ≥2 on any of 3 DAS conviction items. Remission no delusions/hallucinations and HDRS≤10 for 2 consecutive weeks; near remission after 12 weeks no delusions/hallucinations, HDRS 11–15, ≥50% baseline reduction, CGI very/much improved; after 8-week stabilization MMSE≥24 for 36-week RCT. IQCODE 26-item mean ≥4 excluded; substance disorder prior 3 months; type 1 diabetes excluded. |
| N015 | p.4 Randomization/Intervention | Individual randomization 1:1, block sizes 4–8, age strata 18–59/60–85, remission vs near remission and site. Sertraline open label throughout; olanzapine vs identical placebo double blind; 4-week taper. Weekly assessments first 8 weeks then every 4 weeks through week 36/relapse/early termination; assessments sought after medication discontinuation until randomized course completed or relapse. |
| N016 | pp.2,4 medication/outcomes | Acute targets sertraline 150–200 mg/d (50-mg pills), olanzapine 15–20 mg/d (5-mg pills). Weight/waist every visit; fasting lipids, glucose, HbA1c RCT baseline, every 8 weeks, termination. Primary relapse: ≥1 of DSM-IV depressive episode; HDRS≥18; SCID delusions/hallucinations; suicide plan/attempt, mania/hypomania, or psychiatric hospitalization. Relapse exits study to usual care. |
| N017 | p.4 safety definitions; p.6 Table 2 footnotes | EPS baseline/every 4 weeks/termination. SAS Methods range 0–40, Table 2 excluding head dropping range 0–36. Barnes global 0–5, incident baseline 0 then ≥2. Methods AIMS each 10 items range 0–5; Table 2 overall severity 0–4. UKU each 48 items 0–3; present with 2-point increase or score 3 or 4 plus baseline increase. Adverse weight gain/loss >7% above/below premorbid weight; incident falls each visit; SAE definition death/life-threatening/disability/hospitalization. |
| N018 | p.5 Table 1 Age | Mean(SD) y: O 55.0(15.1), P 55.7(14.9). Column denominators 64,62. |
| N019 | p.5 Table 1 Age 18–59 | O 36(56.2%), P 36(58.1%). |
| N020 | p.5 Table 1 Age ≥60 | O 28(43.8%), P 26(41.9%). |
| N021 | p.5 Table 1 Men | O 27(42.2%), P 21(33.9%). |
| N022 | p.5 Table 1 Women | O 37(57.8%), P 41(66.1%); sum women 78 matches p.1. |
| N023 | p.5 Table 1 White | O 54(84.4%), P 49(79.0%). |
| N024 | p.5 Table 1 Black | O 6(9.4%), P 9(14.5%). |
| N025 | p.5 Table 1 Other race | O 4(6.3%), P 4(6.5%); footnote includes American Indian/Alaska Native, Asian, Native Hawaiian/other Pacific Islander, unknown/not reported. |
| N026 | p.5 Table 1 Hispanic ethnicity | O 6(9.4%), P 9(14.5%). |
| N027 | p.5 Table 1 Single | O 19(29.7%), P 15(24.2%). |
| N028 | p.5 Table 1 Married | O 28(43.8%), P 35(56.5%). |
| N029 | p.5 Table 1 Separated/divorced | O 12(18.8%), P 7(11.3%). |
| N030 | p.5 Table 1 Widowed | O 5(7.8%), P 5(8.1%). |
| N031 | p.5 Table 1 Education | Mean(SD) y O 14.4(3.2), P 13.4(3.9). |
| N032 | p.5 Table 1 Living with others | O 46(71.9%), P 49(79.0%). |
| N033 | p.5 Table 1 Living alone | O 17(26.6%), P 10(16.1%). |
| N034 | p.5 Table 1 Senior residence | O 1(1.6%), P 1(1.6%). |
| N035 | p.5 Table 1 Inpatient at acute enrollment | O 41(64.1%), P 46(74.2%). |
| N036 | p.5 Table 1 Cornell | O 16(25.0%), P 15(24.2%). |
| N037 | p.5 Table 1 Massachusetts | O 15(23.4%), P 14(22.6%). |
| N038 | p.5 Table 1 Pittsburgh | O 9(14.1%), P 10(16.1%). |
| N039 | p.5 Table 1 Toronto | O 24(37.5%), P 23(37.1%). |
| N040 | p.5 Table 1 ≥2 lifetime episodes | O 47(73.4%), P 47(75.8%). |
| N041 | p.5 Table 1 Current episode duration | Median(IQR) months O 5.5(3–12), P 5.5(2–12), P n=60. |
| N042 | p.5 Table 1 First episode onset age | Median(IQR) y O 37(24–50), n=62; P 35(18–51), n=61. |
| N043 | p.5 Table 1 Suicide attempt current episode | O 13(20.3%), P 12(19.4%). |
| N044 | p.5 Table 1 Treatment resistance | O 3(4.7%), P 5(8.1%); footnote antidepressant-antipsychotic ATHF score≥3 or ≥7 ECT treatments current episode. |
| N045 | p.5 Table 1 Hyperlipidemia | O 18(29.0%), P 19(29.7%); no row-specific denominator printed. |
| N046 | p.5 Table 1 Hypertension | O 17(26.6%), P 22(35.5%). |
| N047 | p.5 Table 1 Diabetes | O 12(18.8%), P 15(24.2%). |
| N048 | p.5 Table 1 Premorbid weight | Mean(SD) lb O 166.6(34.6), n=60; P 171.4(40.2), n=59; most recent known pre-episode weight; lb×0.45 to kg. |
| N049 | p.6 Table 2 HDRS-17 | Mean(SD) O 5.3(3.6), P 5.6(3.6); range 0–52 higher severity, mean 5 remission. |
| N050 | p.6 Table 2 SADS delusion 1 | O 64(100%), P 62(100%); range 1–7, higher severity, 1 absent. |
| N051 | p.6 Table 2 SADS hallucination 1 | O 64(100%), P 62(100%); range 1–3, 1 absent,3 definite. |
| N052 | p.6 Table 2 HADS anxiety | Median(IQR) O 5.0(2.0–8.0), P 4.0(1.0–7.0), P n=61. Range 0–21 higher severity, ≤7 normal (source image resolves native control glyph). |
| N053 | p.6 Table 2 CORE | Median(IQR) O 1.0(0–3.0), P 1.0(0–4.8); range 0–54 higher psychomotor severity, median1 minimal. |
| N054 | p.6 Table 2 CIRS-G | Median(IQR) O 3.0(1.0–6.0), P 3.0(2.0–5.8); excludes psychiatric illness category; range 0–52, higher cumulative illness, median3 low. |
| N055 | p.6 Table 2 MMSE | Mean(SD) O 28.1(1.9), P 27.9(2.0); range 0–30 higher better; mean28 normal. |
| N056 | p.6 Table 2 DKEFS trail 4 vs5 | Mean(SD) O 7.9(3.5), n=61; P 8.1(3.6), n=59; cognitive flexibility; scores1–19, higher better, normative mean10. |
| N057 | p.6 Table 2 DKEFS color interference condition3 | Mean(SD) O 8.6(2.9), n=60; P 7.6(2.8), n=58; inhibition; footnote h discusses both executive tasks and scale; row printed superscript i points to Barnes footnote. Footnote i Barnes range0–5, higher severity,0 absent. |
| N058 | p.6 Table 2 Barnes global >0 | Printed O 3.0(4.7), P 2.0(3.2) under No.(%) heading. |
| N059 | p.6 Table 2 AIMS overall >0 | Printed O 2.0(3.1), P 2.0(3.2), No.(%); global0–4,0 absent. |
| N060 | p.6 Table 2 SAS | Median(IQR) O 1.0(0–2.0), P 1.0(0–2.0); excludes head dropping, range0–36 higher severity,0 absent. |
| N061 | p.7 Table 3 Depression/no psychosis | O 5, P18 relapse events. |
| N062 | p.7 Table 3 Psychosis/no depression | O0, P1. |
| N063 | p.7 Table 3 Depression and psychosis | O4, P11. |
| N064 | p.7 Table 3 Suicide plan/attempt | O0, P3. |
| N065 | p.7 Table 3 Mania/hypomania | O0, P0. |
| N066 | p.7 Table 3 Psychiatric hospitalization | O6, P11; footnotes: >1 event in some relapse cases; hospitalization for depression/psychosis/suicidality/mania/hypomania. Categories are not mutually exclusive participant totals. |
| N067 | p.7 Figure 2 | Kaplan–Meier proportion free of relapse, y ticks0,.2,.4,.6,.8,1.0; x weeks0,4,8,12,16,20,24,28,32,36. O risk counts64,60,57,56,52,52,49,47,44,43; P62,54,39,36,32,31,28,26,25,24. Source visual shows O above P throughout later follow-up; shaded95% CIs, no numerical curve estimates/limits printed. |
| N068 | p.7 Figure 2 caption; p.9 Limitations | Median observation O36 weeks(IQR24.8–36), P19.5(IQR5.3–36). p.9 50% of P observed≤20 weeks. |
| N069 | p.7 Primary Outcome; p.8 Discussion | NNT with O to prevent1 relapse=2.8; p.7 wording “Based on the HR”; p.8 repeats2.8. Post hoc Cox excludes7 medication-discontinuing participants retained for assessments. |
| N070 | p.7 Secondary Outcomes | Statins started/changed12 participants (O6,P6); hypoglycemics3 (O2,P1); sensitivity excludes pertinent metabolic observations from change/start onward; results qualitatively similar. |
| N071 | p.7 EPS | Incident akathisia O4.7%,P4.8%; all but1 mild. Incident tardive dyskinesia O0%,P3.2%. Counts not printed in this paragraph. |
| N072 | p.7 Adverse Effects | UKU events reported at least once, list introduced as >5%: weight gain O17.2%,P4.8%; weight loss7.8%,4.8%; sleepiness/sedation7.8%,3.2%; orthostatic dizziness7.8%,3.2%; nausea/vomiting3.1%,8.1%. |
| N073 | pp.7–8 Adverse Effects | ≥1 falls O20/64(31.3%),P11/62(17.7%). ≥1 SAE O12/64(18.8%),P12/62(19.4%). One O death ruptured aortic aneurysm; all other SAEs hospitalization. Relapse psychiatric hospitalization O6/13(46.2%),P11/34(32.3%). |
| N074 | p.9 Limitations; p.8 Discussion | 45% switched to P did not relapse; majority of P relapses within first12 weeks, O relapses distributed over36 weeks. p.8 weight gain O/loss P, total cholesterol declines in both with greater P decline; no significant triglyceride/glucose/HbA1c trajectory difference. |
| N075 | p.8 Table 4 heading/footnote; p.7 narrative | Unadjusted within-group baseline-to-termination changes; difference may not equal termination minus baseline because missing data. Means(SD), except triglyceride/glucose medians(IQR), difference95%CIs. Full rows below under S017–S032. |
| N076 | p.9 Table 5 Total cholesterol | Incident≥1 fasting value above both own baseline and240mg/dL; O9/64(14.1%),P6/62(9.7%); absolute unadjusted O−P difference4.3 percentage points(95%CI−8 to17.2). |
| N077 | p.9 Table 5 LDL | Incident≥1 value above own baseline and160mg/dL; O9/64(14.1%),P6/62(9.7%); difference4.3(−8 to17.2) percentage points. |
| N078 | p.9 Table 5 Triglycerides | Incident≥1 value above baseline and200mg/dL; O4/64(6.3%),P2/62(3.2%); difference3.0(−6.7 to13.3) percentage points; footnote exact CI. |
| N079 | p.9 Table 5 Glucose | Incident≥1 value above baseline and126mg/dL; O4/64(6.3%),P4/62(6.5%); difference−0.2(−9.9 to9.9) percentage points; exact CI. p.7 says no statistically significant incident-high group differences. |

## Inferential relationships

Intervals are printed 95% CIs. All tests are 2-sided with overall5% significance (p.6); secondary P values use post hoc Holm stepdown, so paper describes secondary inference as exploratory. p.4 mixed models are model-based; Table4 is a separate unadjusted within-group analysis. S001–S007 Cox covariates are from the same primary multivariable model except post hoc S007.

| ID | Exact location | Estimate, interval, test, model and contrast |
|---|---|---|
| S001 | p.1 abstract; pp.6–7 Primary Outcome | O versus P relapse HR0.25, CI0.13–0.48, P<.001; treatment plus age/remission/site Cox; statistically significant lower relapse risk. Count correspondence N003. |
| S002 | p.6 Primary Outcome | Age young vs old HR0.78, CI0.42–1.46, P=.44. Age strata N015. |
| S003 | p.7 Primary Outcome | Remission vs near-remission baseline HR2.45, CI0.98–6.13, P=.06. |
| S004 | p.7 Primary Outcome | Massachusetts vs Cornell HR1.53, CI0.62–3.76, P=.36. |
| S005 | p.7 Primary Outcome | Pittsburgh vs Cornell HR1.09, CI0.39–2.98, P=.88. |
| S006 | p.7 Primary Outcome | Toronto vs Cornell HR1.80, CI0.81–4.03, P=.15. |
| S007 | p.7 sensitivity | Post hoc excludes7 retained medication-discontinuers, O vs P HR0.22, CI0.11–0.43, P<.001. |
| S008 | p.1 abstract; p.7 secondary | Weight treatment×linear time O−P daily rate0.13lb, CI0.11–0.15; adjustedP<.001; significantly higher. |
| S009 | p.1 abstract; p.7 secondary | Waist daily interaction0.009inches, CI0.004–0.014; adjustedP=.002; significantly higher. |
| S010 | p.1 abstract; p.7 secondary | Total cholesterol daily interaction0.29mg/dL, CI0.13–0.45; adjustedP=.003; significantly higher. |
| S011 | p.1 abstract; p.7 secondary | LDL daily interaction0.04mg/dL, CI−0.01 to0.10; adjustedP=.57; not significantly different. |
| S012 | p.1 abstract; p.7 secondary | HDL daily interaction−0.01mg/dL, CI−0.03 to0.01; adjustedP=.99; not significantly different. |
| S013 | p.1 abstract; p.7 secondary | Triglyceride daily interaction−0.153mg/dL, CI−0.306 to0.004; adjustedP=.25; not significantly different; p.5 specifies pattern-mixture-averaged estimates for this outcome. |
| S014 | p.1 abstract; p.7 secondary | Glucose daily interaction−0.02mg/dL, CI−0.12 to0.08; adjustedP=.99; not significantly different. |
| S015 | p.1 abstract; p.7 secondary | HbA1c daily interaction−0.0002 printed unit mg/dL, CI−0.0021 to0.0016; adjustedP=.99; not significantly different. Table4 scale is %. Both unit labels retained literally. |
| S016 | p.7 EPS | SAS weekly change O−P0.022points, CI0.009–0.036, adjustedP=.009; significantly higher O. Poisson mixed-effects model with overdispersion described pp.4–5; eFigure9 trajectory pointer. |
| S017 | p.8 Table4 Weight O | Baseline participant n cell blank;178.6(SD39.4)lb; termination n62,183.6(40.9); mean change5.7,CI3.3–8.1. |
| S018 | p.8 Table4 Weight P | Baseline n60,182.5(39.8)lb; termination n59,180.2(42.1); mean change−3.1,CI−5.4 to−0.8. |
| S019 | p.8 Table4 Waist O | Baseline n63,38.1(5.4)in; termination n59,38.5(5.2); mean change0.6,CI0.1–1.1. |
| S020 | p.8 Table4 Waist P | Baseline n58,39.4(5.7)in; termination n55,38.4(6.4); mean change−0.8,CI−1.5 to−0.2. |
| S021 | p.8 Table4 Total cholesterol O | Baseline n63,209.0(51.3)mg/dL; termination n63,204.8(51.3); mean change−4.7,CI−14.9 to5.6. |
| S022 | p.8 Table4 Total cholesterol P | Baseline participant n cell blank;220.4(46.8)mg/dL; termination n59,197.4(48.2); mean change−22.3,CI−32.7 to−11.9. |
| S023 | p.8 Table4 LDL O | Baseline n62,132.5(42.1)mg/dL; termination n63,128.9(42.3); mean change−2.8,CI−12.6 to6.9. |
| S024 | p.8 Table4 LDL P | Baseline n cell blank;137.7(38.7)mg/dL; termination n59,122.1(44.2); mean change−16.0,CI−25.8 to−6.2. |
| S025 | p.8 Table4 HDL O | Baseline n63,54.4(19.6)mg/dL; termination n63,49.7(16.1); mean change−5.0,CI−9.1 to−0.9. |
| S026 | p.8 Table4 HDL P | Baseline n cell blank;56.0(16.0)mg/dL; termination n59,52.2(16.0); mean change−3.5,CI−6.2 to−0.9. |
| S027 | p.8 Table4 HbA1c O | Baseline n63,5.9(1.5)%; termination n62,5.7(1.1); mean change−0.2,CI−0.5 to0.2. |
| S028 | p.8 Table4 HbA1c P | Baseline n cell blank;5.9(1.2)%; termination n58,5.9(1.0); mean change0.1,CI−0.1 to0.2. |
| S029 | p.8 Table4 Triglyceride O | Baseline n63,median134(IQR90–186)mg/dL; termination n63,133(87–206); median change−3.9,CI−18 to12. |
| S030 | p.8 Table4 Triglyceride P | Baseline n cell blank;median121(IQR95–169)mg/dL; termination n59,107(80–153); median change−18,CI−25 to−7. |
| S031 | p.8 Table4 Glucose O | Baseline n63,median90(IQR83–99)mg/dL; termination n63,92(87–104); median change1.4,CI−1.8 to5. |
| S032 | p.8 Table4 Glucose P | Baseline n cell blank;median93(IQR85–100)mg/dL; termination n59,94(85–106); median change2.8,CI−3.6 to6.0. |
| S033 | p.7 Figure2 caption | Group comparison log-rankP<.001, Kaplan–Meier relapse-free survival;95% shaded CIs; observation times N068. |
| S034 | p.4 Power Analysis | Original sample176 randomized,80% power,20% group difference in relapse risk,up to15% attrition;20% means NNT5. After3 recruitment years revised128 approved by NIMH/DSMB because higher than anticipated overall relapse risk. Exact assumed arm risks/significance input not given in this paragraph; supplied plan is separate mapping scope. |
| S035 | p.4 Statistical Analyses | All randomized included. Primary Cox covariates treatment and3 randomization stratification variables: age,remission status,site. PH confirmed complementary log-log visual inspection and Schoenfeld residual correlation tests with time; no numerical diagnostic statistics. Medication-discontinuation exclusion post hoc. |
| S036 | pp.4–5 Statistical Analyses; p.7 Secondary | Anthropometric/metabolic linear mixed models: participant random intercept and random slope continuous time; fixed site,time,treatment,treatment×time. p.7 explicitly says linear and quadratic effects of time; daily rate cannot extrapolate cumulative linear change. eFigures1–8 trajectories are matched supplemental results. No random-slope variances or SEs printed. |
| S037 | pp.4–5 Statistical Analyses | SAS Poisson mixed-effects regression with overdispersion; participant random intercept,fixed site,time,treatment,treatment×time. Mixed models valid under MAR. Pattern mixture each outcome investigated early-termination-pattern dependence; estimates likely not biased except triglycerides, for which pattern-mixture-averaged estimates reported. |
| S038 | pp.5–6 Statistical Analyses; pp.7–9 Results | Statin/hypoglycemic sensitivity post hoc with later pertinent values excluded; incident-high group comparisons post hoc. Incidence akathisia/tardive dyskinesia, UKU,falls,SAE descriptive. SAS9.4; all tests2-sided,overall5% primary/secondary; Holm secondary adjustment post hoc,secondary interpretation exploratory. Table5 four difference/CI relationships N076–N079 are additionally inferential and included in this record rather than assigned duplicate S IDs. |
| S039 | pp.6,8,9 conversion footnotes | Cholesterol mg/dL×0.0259→mmol/L; glucose×0.0555; triglycerides×0.0113; lb×0.45→kg; inches×2.54→cm. These distinguish units for S008–S032 and incident thresholds; no standardized effects/rates per person-time printed. |

## Cross-location and downstream handoff

Primary match set: N002/N003/N005–N013 (abstract/Key Points/flow/body), S001 (abstract/body), S033 and N067/N068 (Figure2/caption), N069 (body/discussion NNT). Secondary match set: S008–S015 appears with the same printed estimates and intervals in abstract and body; adjusted P values only body. These model effects are separate from within-arm Table4 S017–S032. Methods explain missingness and quadratic time; all these distinctions must remain during checks. SAS S016 is weekly and supplemental eFigure9, whereas other model slopes are daily. No standard errors or explicit test statistics are printed anywhere in the main paper. No inferential group comparison is printed for Table1/2, which are descriptive; Table3 permits overlapping events. Table5 N076–N079 has unadjusted absolute percentage-point differences and95%CIs, no printed P values; footnote marks triglyceride/glucose intervals exact.

Applicability coverage:10/10 pages mapped. Numeric relationship count79; inferential relationship count39; total118. Fresh-required units0; fresh direct layout and seven direct rendered pages supplement reusable locators. Gaps: none in scientific page/row/result coverage. Unprinted inputs (e.g., individual trajectories, Table4 blank P baseline n cells, exact model covariance output) remain unprinted rather than imputed. All source-linked numeric and model labels were retained; no source/reused artifact changed.
