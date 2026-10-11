# Main-paper quantitative evidence map

Runtime agent: 01a128dc-926b-7a82-afaf-ecf5979714d5. Scope: DOC-001, jama_flint_2019_oi_190079.pdf, PDF pages 1–10 (printed pages 622–631). Document role: REPORT. Fresh scientific mapping of every source page; reusable-backed pages 10; fresh-required pages 0; mapped pages 10. No candidate diagnosis or adjudication is made here.

Controls read: QUALITY_CONTROL_SCOPE.md; workflow_1_6_1/review_contract.md; source_coverage.md; evidence_asset_inventory.md; tooling_record.md. Evidence engines: reusable legacy native PDF text and normalized native/OCR text, with reusable legacy PDF raster page images for pages 3, 5, 6, 7, 8, 9. All six images were visually inspected for box counts, column alignment, footnotes, curve labels, and table values. No new extraction engine, OCR, or fallback environment was needed. Source pages remain authority; derivatives are locators. The native text's rotated Table 4 reading order is resolved from its page image, and the HADS normal threshold is visually read as ≤7 rather than the missing-symbol native rendition.

Links below are relative to this artifact's extraction directory. Abbreviations O = sertraline plus olanzapine; P = sertraline plus placebo. Unless explicitly stated, randomized denominators are O=64, P=62. Values retain source display precision. A row is a matching relationship, potentially containing multiple value fields or categories; numerical tuples include every displayed field. Inferential relationships are separately indexed S001–S040 and refer to the numeric evidence without duplicating source scope.

## Page completion

| PDF page | Printed page | Mapped content | Status |
|---|---:|---|---|
| 1 | 622 | Abstract design, populations, primary and all eight metabolic outcomes, duplicate keys | COMPLETE |
| 2 | 623 | Key Points, eligibility, phase and dosing definitions, declared aims | COMPLETE |
| 3 | 624 | Every Figure 1 flow box and subcategory; near-remission and RCT eligibility | COMPLETE |
| 4 | 625 | Randomization, endpoints, outcome schedules, safety definitions, power, primary and mixed-model specifications | COMPLETE |
| 5 | 626 | Every Table 1 numerical row and footnote; missingness/pattern-mixture and medication sensitivity methods | COMPLETE |
| 6 | 627 | Every Table 2 numerical row and scale footnote; multiplicity and primary Cox results | COMPLETE |
| 7 | 628 | Every Table 3 row; Figure 2 labels, risks, follow-up and test; all modeled secondary results, safety and sensitivity results | COMPLETE |
| 8 | 629 | Every Table 4 row, denominators, raw distributions and change intervals; hospitalization and discussion claims | COMPLETE |
| 9 | 630 | Every Table 5 row and threshold; limitation/completion narratives and conclusion | COMPLETE |
| 10 | 631 | Administrative disclosures, sponsor roles, references and data-sharing pointer; no applicable study-result quantities | COMPLETE_NO_APPLICABLE_RESULTS |

## Numeric relationships: abstract, eligibility, flow and design

| ID | Source location | Quantity, definition, population/time and matching locations |
|---|---|---|
| N001 | [p1 abstract design](../../../jama_flint_2019_oi_190079.pdf#page=1) | 36-week RCT; 4 academic centers; age ≥18 years; acute treatment up to 12 weeks; remission/near-remission sustained for 8 weeks. Recruitment November 2011–June 2017; last follow-up June 13, 2017. Matches pp2–4 phase/intervention methods. |
| N002 | [p1 abstract population](../../../jama_flint_2019_oi_190079.pdf#page=1) | Randomized 126; O64/P62; age mean(SD) 55.3(14.9) years; women78(61.9%); completed trial114(90.5%). Matches p2 Key Points, p3 Figure1, p5 Table1 and p6 participant narrative. Completion is recorded as the source wording, with Figure1 endpoint categories separately retained. |
| N003 | [p1 abstract medication](../../../jama_flint_2019_oi_190079.pdf#page=1) | At randomization sertraline median150 IQR150–200 mg/d; olanzapine median15 IQR10–20 mg/d. All continued sertraline. Matches p6 Table2 separate arm distributions. |
| N004 | [p1 primary result](../../../jama_flint_2019_oi_190079.pdf#page=1) | Relapse O13(20.3%)/64 versus P34(54.8%)/62; HR0.25,95%CI0.13–0.48,P<.001. Matches p2 Key Points (counts/percentages, statistical significance), p3 Figure1, pp6–7 Cox narrative, p7 Figure2 related survival result. |
| N005 | [p2 eligibility](../../../jama_flint_2019_oi_190079.pdf#page=2) | Acute enrollment age18–85; DSM-IV-TR major depression with ≥1 delusion; HDRS17≥21; delusion severity≥3; ≥2 on any of 3 conviction items. IQCODE mean≥4 is exclusion; substance abuse/dependence within preceding3 months; type1 diabetes excluded. |
| N006 | [pp2–3 phase eligibility](../../../jama_flint_2019_oi_190079.pdf#page=3) | Acute target sertraline150–200 mg/d in50-mg pills and olanzapine15–20 mg/d in5-mg pills. Remission: absent delusions/hallucinations, HDRS17≤10 for2 consecutive weeks. Near remission after12 acute weeks: absent psychosis, HDRS11–15, ≥50% baseline HDRS reduction, CGI much/very much improved. After8-week stabilization, maintained full/near remission and MMSE≥24 required for36-week RCT. |
| N007 | [p3 Figure1 initial eligibility](../../../jama_flint_2019_oi_190079.pdf#page=3) | Assessed350; excluded81 = not eligible60 + withdrew consent16 + other5; open-label treatment269. |
| N008 | [p3 Figure1 acute phase](../../../jama_flint_2019_oi_190079.pdf#page=3) | Acute discontinuation74: withdrew31, insufficient response/clinical worsening21, inappropriate participation7, adverse events5, medical event1, other9. Completed acute195; symptom nonremission exclusion33; stabilization entry162. |
| N009 | [p3 Figure1 stabilization](../../../jama_flint_2019_oi_190079.pdf#page=3) | Stabilization discontinuation15: worsening4, withdrew2, died nonsuicide1, inappropriate participation1, other7. Completed147; not randomized21: ineligible12, declined randomization9. Randomized126. Footnote inappropriate participation includes repeated nonadherence with assessments or medication. |
| N010 | [p3 Figure1 allocation](../../../jama_flint_2019_oi_190079.pdf#page=3) | O64: received as randomized59; did not5 (discontinued3, switched open-label olanzapine2). P62: received60; did not2 (discontinued1, switched open-label olanzapine1). |
| N011 | [p3 Figure1 O outcomes](../../../jama_flint_2019_oi_190079.pdf#page=3) | Primary analysis64; remission/near-remission completion43; relapse13; discontinuation8 (nonsuicide death1, withdrew5, moved1, transportation1). |
| N012 | [p3 Figure1 P outcomes](../../../jama_flint_2019_oi_190079.pdf#page=3) | Primary analysis62; remission/near-remission completion24; relapse34; discontinuation4 (medical event1, withdrew3). |
| N013 | [p4 allocation/intervention](../../../jama_flint_2019_oi_190079.pdf#page=4) | Computer randomization1:1, blocks4–8; strata age18–59 vs60–85, remission vs near-remission, site. Blinded olanzapine substitution/taper4 weeks; weekly assessments first8 weeks, then every4 weeks until week36, relapse or termination; research follow-up attempted after medication discontinuation. |
| N014 | [p4 relapse definition](../../../jama_flint_2019_oi_190079.pdf#page=4) | ≥1: SCID DSM-IV major depressive episode; HDRS17≥18; SCID psychosis; other worsening (suicide plan/attempt, mania/hypomania, psychiatric hospitalization). Relapse causes study exit/usual care. No noninferiority/equivalence margin is stated. |
| N015 | [p4 measurement schedule](../../../jama_flint_2019_oi_190079.pdf#page=4) | Weight/waist each visit; fasting lipids, glucose,HbA1c at RCT baseline,every8 weeks,termination. Extrapyramidal symptoms baseline,every4 weeks,termination. Falls each visit. |
| N016 | [p4 safety definitions](../../../jama_flint_2019_oi_190079.pdf#page=4) | Simpson-Angus total0–40 higher worse; Barnes global0–5 higher worse; AIMS0–5 each10 items higher worse. Incident akathisia baseline0 then≥2; tardive dyskinesia Schooler-Kane criteria. UKU0–3 each48 items; adverse effect2-point increase or score3/4 with increase. Weight adverse thresholds >7% above/below premorbid. Serious events death,life-threatening including suicide attempt,disability/incapacity,hospitalization. These are definitions, not assumptions about counts. |
| N017 | [p4 power](../../../jama_flint_2019_oi_190079.pdf#page=4) | Original randomized target176;80% power;20% relapse-risk difference;up to15% attrition;20% difference corresponds to NNT5. Revised randomized target128 approved3 years after recruitment start because higher anticipated overall relapse. No arm-specific risk assumptions or revised numerical power are supplied on this page. |

## Table 1: every displayed row

Location for N018–N049: [PDF p5 Table1](../../../jama_flint_2019_oi_190079.pdf#page=5). Columns O64/P62; count(%) unless named otherwise. Acute clinical entries refer to acute-phase baseline, not randomization baseline.

| ID | Variable/unit | O | P |
|---|---|---|---|
| N018 | Age mean(SD),years |55.0(15.1)|55.7(14.9)|
| N019 | Age18–59;≥60 |36(56.2);28(43.8)|36(58.1);26(41.9)|
| N020 | Men;women |27(42.2);37(57.8)|21(33.9);41(66.1)|
| N021 | White;Black;other race |54(84.4);6(9.4);4(6.3)|49(79.0);9(14.5);4(6.5)|
| N022 | Hispanic ethnicity |6(9.4)|9(14.5)|
| N023 | Single |19(29.7)|15(24.2)|
| N024 | Married |28(43.8)|35(56.5)|
| N025 | Separated/divorced |12(18.8)|7(11.3)|
| N026 | Widowed |5(7.8)|5(8.1)|
| N027 | Education mean(SD),years |14.4(3.2)|13.4(3.9)|
| N028 | Living with others |46(71.9)|49(79.0)|
| N029 | Living alone |17(26.6)|10(16.1)|
| N030 | Senior residence |1(1.6)|1(1.6)|
| N031 | Inpatient enrollment |41(64.1)|46(74.2)|
| N032 | Cornell site |16(25.0)|15(24.2)|
| N033 | Massachusetts site |15(23.4)|14(22.6)|
| N034 | Pittsburgh site |9(14.1)|10(16.1)|
| N035 | Toronto site |24(37.5)|23(37.1)|
| N036 | ≥2 lifetime depressive episodes |47(73.4)|47(75.8)|
| N037 | Episode duration median(IQR),months |5.5(3–12)|5.5(2–12),n60|
| N038 | First episode onset median(IQR),years |37(24–50),n62|35(18–51),n61|
| N039 | Current-episode suicide attempt |13(20.3)|12(19.4)|
| N040 | Current-episode treatment resistance |3(4.7)|5(8.1)|
| N041 | Hyperlipidemia |18(29.0)|19(29.7)|
| N042 | Hypertension |17(26.6)|22(35.5)|
| N043 | Diabetes |12(18.8)|15(24.2)|
| N044 | Premorbid weight mean(SD),lb |166.6(34.6),n60|171.4(40.2),n59|
| N045 | Table1 footnote resistance |Combination antidepressant/antipsychotic ATHF score≥3 or≥7 ECT treatments during current episode|Same definition|
| N046 | Table1 footnote weight |Most recent known weight before current depression;lb to kg multiply0.45|Same definition|
| N047 | Table1 other race |American Indian/Alaska Native,Asian,Native Hawaiian/other Pacific Islander,unknown/not reported|Same definition|
| N048 | Table1 table population |Randomized participants,64|Randomized participants,62|
| N049 | Baseline matching key |Sociodemographic and acute baseline distributions; p1 pooled demographics|Distinct from Table2 randomization baseline|

## Table 2: every displayed row and quantitative scale footnote

Location for N050–N065: [PDF p6 Table2](../../../jama_flint_2019_oi_190079.pdf#page=6). O64/P62. Values are randomization baseline; n deviations are explicit.

| ID | Variable | O | P | Scale/context |
|---|---|---|---|---|
| N050 | HDRS17 mean(SD) |5.3(3.6)|5.6(3.6)|0–52,higher more depression;mean5 remission|
| N051 | SADS delusion=1;hallucination=1 |64(100);64(100)|62(100);62(100)|Delusion1–7,hallucination1–3;1 absent,3 definite hallucination|
| N052 | HADS anxiety median(IQR) |5.0(2.0–8.0)|4.0(1.0–7.0),n61|0–21,higher more anxiety,≤7 normal|
| N053 | CORE median(IQR) |1.0(0–3.0)|1.0(0–4.8)|0–54,higher more psychomotor change;median1 minimal|
| N054 | CIRS-G median(IQR) |3.0(1.0–6.0)|3.0(2.0–5.8)|Psychiatric illness omitted;0–52,higher cumulative illness;median3 low|
| N055 | MMSE mean(SD) |28.1(1.9)|27.9(2.0)|0–30,higher cognition;mean28 normal|
| N056 | DKEFS trail4 vs5 scaled mean(SD) |7.9(3.5),n61|8.1(3.6),n59|Cognitive flexibility,scale1–19,higher better,normative mean10|
| N057 | DKEFS color-word3 weighted scaled mean(SD) |8.6(2.9),n60|7.6(2.8),n58|Inhibition,scale1–19,higher better,normative mean10|
| N058 | Barnes global>0,count(%) |3.0(4.7)|2.0(3.2)|Global0–5,higher severity,0 absent|
| N059 | AIMS overall>0,count(%) |2.0(3.1)|2.0(3.2)|Tardive dyskinesia global0–4,higher worse,0 absent|
| N060 | Simpson-Angus median(IQR) |1.0(0–2.0)|1.0(0–2.0)|Excludes head-dropping item,total0–36,higher worse,0 absent|
| N061 | Sertraline median(IQR),mg/d |150(150–200)|150(150–200)|Matches p1 pooled dosage|
| N062 | Olanzapine median(IQR),mg/d |15(10–20)|15(10–20)|Matches p1 pooled dosage|
| N063 | Table2 table population |64|62|All randomized participants unless specific n|
| N064 | Scale footnote attachment |DKEFS color-word row carries superscript i; footnote h describes both executive tasks; footnote i describes Barnes|Same printed arrangement|Definitions transcribed from visible text without judgment|
| N065 | SI conversions p6 methods |Cholesterol×0.0259;glucose×0.0555;triglycerides×0.0113|lb×0.45;inches×2.54|mg/dL to mmol/L;lb to kg;in to cm|

## Relapse events and Figure 2

Location for N066–N075: [PDF p7 Table3,Figure2 and narrative](../../../jama_flint_2019_oi_190079.pdf#page=7).

| ID | Matching quantity | O | P | Context |
|---|---|---|---|---|
| N066 | Depression without psychosis |5|18|Relapse event types,not mutually exclusive persons|
| N067 | Psychosis without depression |0|1|Table3|
| N068 | Depression and psychosis |4|11|Table3|
| N069 | Suicide plan/attempt |0|3|Table3|
| N070 | Mania/hypomania |0|0|Table3|
| N071 | Psychiatric hospitalization |6|11|For depression,psychosis,suicidality,mania/hypomania;more than1 event may occur in a relapse|
| N072 | Figure2 at-risk counts at weeks0,4,8,12,16,20,24,28,32,36 |64,60,57,56,52,52,49,47,44,43|62,54,39,36,32,31,28,26,25,24|Kaplan-Meier risk sets,not independent outcome counts|
| N073 | Median observation(IQR),weeks |36(24.8–36)|19.5(5.3–36)|Figure2 caption|
| N074 | Figure2 plotted quantity |Proportion free of relapse;curve above P|Proportion free of relapse;curve below O|x=time,wk0–36 by4; y0–1.0 by0.2;shaded95%CI;group log-rankP<.001;no exact curve-point labels|
| N075 | NNT and follow-up narrative |NNT2.8 to prevent1 relapse,based on HR (source wording)|Majority placebo relapses within first12 weeks|NNT repeated p8; O relapses distributed over36 weeks; p9 says50% P observed≤20 weeks and45% P did not relapse|

## Safety numerical relationships

Location for N076–N086: [PDF p7 safety](../../../jama_flint_2019_oi_190079.pdf#page=7), with continuation [PDF p8](../../../jama_flint_2019_oi_190079.pdf#page=8).

| ID | Quantity | O | P | Context |
|---|---|---|---|---|
| N076 | Incident akathisia |4.7%|4.8%|All but1 case mild;baseline0 then≥2|
| N077 | Incident tardive dyskinesia |0%|3.2%|Schooler-Kane definition|
| N078 | Adverse weight gain |17.2%|4.8%|UKU adverse effects at least once;listed when>5% participants|
| N079 | Adverse weight loss |7.8%|4.8%|Weight definitions >7% premorbid deviation|
| N080 | Sleepiness/sedation |7.8%|3.2%|At least once|
| N081 | Orthostatic dizziness |7.8%|3.2%|At least once|
| N082 | Nausea/vomiting |3.1%|8.1%|At least once|
| N083 | ≥1 fall |20/64(31.3%)|11/62(17.7%)|During trial|
| N084 | ≥1 serious adverse event |12/64(18.8%)|12/62(19.4%)|O death1 ruptured aortic aneurysm;all others hospitalization|
| N085 | Hospitalization among relapse patients |6/13(46.2%)|11/34(32.3%)|p8 continuation;matching Table3 psychiatric hospitalization|
| N086 | Medication started/changed |Statins6;hypoglycemic2|Statins6;hypoglycemic1|Totals12 statin,3 hypoglycemic;post hoc metabolic sensitivity excludes subsequent pertinent data|

## Table 4: raw baseline-to-termination distributions and within-arm change

N087 is the complete eight-row raw longitudinal relationship group, expanded below. Location: [PDF p8 Table4](../../../jama_flint_2019_oi_190079.pdf#page=8). Each cell lists n;mean(SD) except triglycerides and glucose, which list n;median(IQR). Difference is termination minus baseline,unadjusted; 95%CI. Footnote: differences may not equal difference of displayed summaries because of missing data. These are post hoc within-group results, not treatment×time modeled estimates. O table-header n64,P n62.

| Variable/unit | O baseline | O termination | O difference(95%CI) | P baseline | P termination | P difference(95%CI) |
|---|---|---|---|---|---|---|
| Weight,lb |63;178.6(39.4)|62;183.6(40.9)|5.7(3.3–8.1)|60;182.5(39.8)|59;180.2(42.1)|−3.1(−5.4 to−0.8)|
| Waist,in |63;38.1(5.4)|59;38.5(5.2)|0.6(0.1–1.1)|58;39.4(5.7)|55;38.4(6.4)|−0.8(−1.5 to−0.2)|
| Total cholesterol,mg/dL |63;209.0(51.3)|63;204.8(51.3)|−4.7(−14.9–5.6)|60;220.4(46.8)|59;197.4(48.2)|−22.3(−32.7 to−11.9)|
| LDL,mg/dL |62;132.5(42.1)|63;128.9(42.3)|−2.8(−12.6–6.9)|60;137.7(38.7)|59;122.1(44.2)|−16.0(−25.8 to−6.2)|
| HDL,mg/dL |63;54.4(19.6)|63;49.7(16.1)|−5.0(−9.1 to−0.9)|60;56.0(16.0)|59;52.2(16.0)|−3.5(−6.2 to−0.9)|
| HbA1c,% |63;5.9(1.5)|62;5.7(1.1)|−0.2(−0.5–0.2)|60;5.9(1.2)|58;5.9(1.0)|0.1(−0.1–0.2)|
| Triglyceride,mg/dL |63;134(90–186)|63;133(87–206)|−3.9(−18–12)|60;121(95–169)|59;107(80–153)|−18(−25 to−7)|
| Glucose,mg/dL |63;90(83–99)|63;92(87–104)|1.4(−1.8–5)|60;93(85–100)|59;94(85–106)|2.8(−3.6–6.0)|

Table4 SI conversion factors: cholesterol0.0259,glucose0.0555,triglycerides0.0113 from mg/dL to mmol/L;lb0.45 to kg;in2.54 to cm. Discussion matching claims: O weight gain/P weight loss; total cholesterol decreased both with greater P decline; no significant between-group trajectory difference triglyceride/glucose/HbA1c. These trajectory claims match modeled S015–S019, not the within-arm differences above.

## Table 5: incident high fasting metabolic value

N088 is the complete four-row binary endpoint group, expanded below. Location: [PDF p9 Table5](../../../jama_flint_2019_oi_190079.pdf#page=9). Every incident definition requires ≥1 value strictly above both RCT baseline and named threshold. Columns O64/P62; absolute unadjusted O-minus-P difference in percentage points(95%CI). Triglyceride and glucose intervals explicitly marked exact. Narrative p7 says no statistically significant group differences, post hoc.

| Endpoint/threshold,mg/dL | O count(%) | P count(%) | Difference%(95%CI) |
|---|---|---|---|
| Total cholesterol240 |9(14.1)|6(9.7)|4.3(−8–17.2)|
| LDL160 |9(14.1)|6(9.7)|4.3(−8–17.2)|
| Triglycerides200 |4(6.3)|2(3.2)|3.0(−6.7–13.3),exactCI|
| Glucose126 |4(6.3)|4(6.5)|−0.2(−9.9–9.9),exactCI|

N089: [p9 limitations/conclusion](../../../jama_flint_2019_oi_190079.pdf#page=9). Four-week antipsychotic taper reiterated;50% placebo observed≤20 weeks;45% switched to placebo did not relapse. Conclusion continuing O versus P reduces relapse over36 weeks with weight-gain tradeoff. [p8](../../../jama_flint_2019_oi_190079.pdf#page=8) cites external trial age18–65 as contextual generalizability discussion; it is not supplied trial evidence or an analysis population. [p10](../../../jama_flint_2019_oi_190079.pdf#page=10) contains no new result relationship; grants,dates,journal references and bibliographic page numbers are administrative.

## Statistical relationships: complete main-paper inventory

Population unless specified: all126 randomized; treatment contrast O versus P. Statistical methods pp4–6 are keyed to the results below. No published SE or test statistic is printed in this main report; named P values and95%CIs are fully enumerated. S001–S040 are inferential relationships, with grouped method specifications deliberately separate from numeric-table groups.

| ID | Exact source location | Statistical relationship and complete matching key |
|---|---|---|
| S001 | [p4 power](../../../jama_flint_2019_oi_190079.pdf#page=4) | Original176 randomized,80% power,20% risk difference,15% attrition,NNT5; revised128 after3 years,higher overall relapse. Relates N017. |
| S002 | [p4 Cox methods](../../../jama_flint_2019_oi_190079.pdf#page=4) | Primary time-to-relapse Cox PH; treatment plus age category,remission category,site (all randomization strata). PH checked with complementary log-log plots and Schoenfeld residual correlation with time. All randomized included. |
| S003 | [pp6–7 primary Cox](../../../jama_flint_2019_oi_190079.pdf#page=6) | Adjusted treatment HR0.25,95%CI0.13–0.48,P<.001; O13/64,P34/62. Same estimate/interval/P p1; counts also p2,p3. See N004. |
| S004 | [p6 age covariate](../../../jama_flint_2019_oi_190079.pdf#page=6) | Young(18–59) versus old(60–85) HR0.78,95%CI0.42–1.46,P=.44,same adjusted primary Cox. |
| S005 | [p7 remission covariate](../../../jama_flint_2019_oi_190079.pdf#page=7) | Remission versus near remission HR2.45,95%CI0.98–6.13,P=.06,same adjusted primary Cox. |
| S006 | [p7 site covariate](../../../jama_flint_2019_oi_190079.pdf#page=7) | Massachusetts versus Cornell HR1.53,95%CI0.62–3.76,P=.36. |
| S007 | [p7 site covariate](../../../jama_flint_2019_oi_190079.pdf#page=7) | Pittsburgh versus Cornell HR1.09,95%CI0.39–2.98,P=.88. |
| S008 | [p7 site covariate](../../../jama_flint_2019_oi_190079.pdf#page=7) | Toronto versus Cornell HR1.80,95%CI0.81–4.03,P=.15. |
| S009 | [p7 Figure2 caption](../../../jama_flint_2019_oi_190079.pdf#page=7) | Kaplan-Meier proportion relapse-free over0–36 weeks;log-rankP<.001,shaded95%CIs. Distinct from covariate-adjusted Cox. Full risks/follow-up N072–N074. |
| S010 | [p7 sensitivity](../../../jama_flint_2019_oi_190079.pdf#page=7) | Post hoc Cox excluding7 who discontinued assigned medication but remained assessed;HR0.22,95%CI0.11–0.43,P<.001. Methods p4. Group split is not printed in this sentence; Figure1 allocation differences N010 available as separate context. |
| S011 | [p7 NNT](../../../jama_flint_2019_oi_190079.pdf#page=7) | NNT2.8 to prevent1 relapse,source attributes calculation to HR; repeated p8. No NNT formula/time-specific control survival is printed. |
| S012 | [p7 weight modeled result](../../../jama_flint_2019_oi_190079.pdf#page=7) | Treatment×linear-time daily-rate difference0.13 lb/day,95%CI0.11–0.15,Holm-adjustedP<.001;O higher. Abstract p1 identical estimate/CI,significant. |
| S013 | [p7 waist modeled result](../../../jama_flint_2019_oi_190079.pdf#page=7) | Daily-rate difference0.009 inches/day,95%CI0.004–0.014,adjustedP=.002;O higher. Abstract p1 identical estimate/CI,significant. |
| S014 | [p7 total-cholesterol result](../../../jama_flint_2019_oi_190079.pdf#page=7) | Daily-rate difference0.29 mg/dL/day,95%CI0.13–0.45,adjustedP=.003;O higher. Abstract p1 identical estimate/CI,significant. |
| S015 | [p7 LDL result](../../../jama_flint_2019_oi_190079.pdf#page=7) | Daily-rate difference0.04 mg/dL/day,95%CI−0.01–0.10,adjustedP=.57;not significant;abstract p1 identical estimate/CI. |
| S016 | [p7 HDL result](../../../jama_flint_2019_oi_190079.pdf#page=7) | Daily-rate difference−0.01 mg/dL/day,95%CI−0.03–0.01,adjustedP=.99;not significant;abstract p1 identical estimate/CI. |
| S017 | [p7 triglyceride result](../../../jama_flint_2019_oi_190079.pdf#page=7) | Daily-rate difference−0.153 mg/dL/day,95%CI−0.306–0.004,adjustedP=.25;pattern-mixture-averaged estimate per p5;not significant;abstract p1 identical estimate/CI. |
| S018 | [p7 glucose result](../../../jama_flint_2019_oi_190079.pdf#page=7) | Daily-rate difference−0.02 mg/dL/day,95%CI−0.12–0.08,adjustedP=.99;not significant;abstract p1 identical estimate/CI. |
| S019 | [p7 HbA1c result](../../../jama_flint_2019_oi_190079.pdf#page=7) | Daily-rate difference−0.0002 with printed unit mg/dL,95%CI−0.0021–0.0016,adjustedP=.99;not significant;abstract p1 same unit/value/CI. Table4 raw HbA1c units% retained separately in N087. |
| S020 | [p7 Simpson-Angus result](../../../jama_flint_2019_oi_190079.pdf#page=7) | Weekly change difference0.022 points,95%CI0.009–0.036,adjustedP=.009;O higher;Poisson mixed-effects method pp4–5;trajectory eFigure9 pointer. |
| S021 | [p4 mixed models](../../../jama_flint_2019_oi_190079.pdf#page=4) | Anthropometric/metabolic linear mixed models:participant random intercept and random slope(continuous time);fixed site,time,treatment,treatment×time. p7 adds linear and quadratic time effects,explicitly prohibits extrapolating daily coefficients to cumulative linear36-week change. |
| S022 | [pp4–5 Poisson method](../../../jama_flint_2019_oi_190079.pdf#page=5) | Simpson-Angus Poisson mixed-effects regression with overdispersion;participant random intercept;fixed site,time,treatment,treatment×time. Outcome scale at p6 Table2 excludes head dropping,total0–36. |
| S023 | [p5 missingness](../../../jama_flint_2019_oi_190079.pdf#page=5) | More relapse/early termination in P leads to missed outcomes; mixed models valid under MAR; pattern-mixture models examine treatment effect by termination pattern and adjust when needed. Report says likely no bias except triglycerides,for which pattern-mixture-averaged estimates reported. |
| S024 | [pp5,7 sensitivity](../../../jama_flint_2019_oi_190079.pdf#page=5) | Post hoc exclude metabolic data after initiating/changing statins or hypoglycemics;12 statin(6/6),3 hypoglycemic(2/1);qualitatively similar results,no alternate coefficients printed. |
| S025 | [p6 multiplicity](../../../jama_flint_2019_oi_190079.pdf#page=6) | All tests2-sided,overall5% primary/secondary significance;secondary P Holm stepdown adjusted post hoc,hence exploratory. SAS9.4. No secondary-adjustment family listing beyond stated multiple secondary outcomes. |
| S026 | [p8 Table4 weight](../../../jama_flint_2019_oi_190079.pdf#page=8) | Raw within-arm mean change95%CI O5.7(3.3–8.1),P−3.1(−5.4 to−0.8)lb;sample/distribution fields N087;post hoc unadjusted. |
| S027 | [p8 Table4 waist](../../../jama_flint_2019_oi_190079.pdf#page=8) | O0.6(0.1–1.1),P−0.8(−1.5 to−0.2)in;post hoc raw within-arm mean change. |
| S028 | [p8 Table4 total cholesterol](../../../jama_flint_2019_oi_190079.pdf#page=8) | O−4.7(−14.9–5.6),P−22.3(−32.7 to−11.9)mg/dL;post hoc raw within-arm mean change. |
| S029 | [p8 Table4 LDL](../../../jama_flint_2019_oi_190079.pdf#page=8) | O−2.8(−12.6–6.9),P−16.0(−25.8 to−6.2)mg/dL;post hoc raw within-arm mean change. |
| S030 | [p8 Table4 HDL](../../../jama_flint_2019_oi_190079.pdf#page=8) | O−5.0(−9.1 to−0.9),P−3.5(−6.2 to−0.9)mg/dL;post hoc raw within-arm mean change. |
| S031 | [p8 Table4 HbA1c](../../../jama_flint_2019_oi_190079.pdf#page=8) | O−0.2(−0.5–0.2),P0.1(−0.1–0.2)%;post hoc raw within-arm mean change. |
| S032 | [p8 Table4 triglyceride](../../../jama_flint_2019_oi_190079.pdf#page=8) | O−3.9(−18–12),P−18(−25 to−7)mg/dL;post hoc raw within-arm median difference. |
| S033 | [p8 Table4 glucose](../../../jama_flint_2019_oi_190079.pdf#page=8) | O1.4(−1.8–5),P2.8(−3.6–6.0)mg/dL;post hoc raw within-arm median difference. |
| S034 | [p9 Table5 total cholesterol](../../../jama_flint_2019_oi_190079.pdf#page=9) | Binary incident high outcome,O9/64,P6/62;absolute unadjusted difference4.3 percentage points,95%CI−8–17.2;threshold240 mg/dL plus above individual baseline. |
| S035 | [p9 Table5 LDL](../../../jama_flint_2019_oi_190079.pdf#page=9) | Binary outcome,O9/64,P6/62;difference4.3 points,95%CI−8–17.2;threshold160 plus above baseline. |
| S036 | [p9 Table5 triglyceride](../../../jama_flint_2019_oi_190079.pdf#page=9) | Binary outcome,O4/64,P2/62;difference3.0 points,exact95%CI−6.7–13.3;threshold200 plus above baseline. |
| S037 | [p9 Table5 glucose](../../../jama_flint_2019_oi_190079.pdf#page=9) | Binary outcome,O4/64,P4/62;difference−0.2 points,exact95%CI−9.9–9.9;threshold126 plus above baseline. |
| S038 | [pp6–7 post hoc binary methods](../../../jama_flint_2019_oi_190079.pdf#page=6) | Incident high metabolic counts compared post hoc;no group difference significant p7. Main paper does not print associated P values or interval algorithm beyond Table5 exact labels. |
| S039 | [p6 descriptive safety](../../../jama_flint_2019_oi_190079.pdf#page=6) | Incidence akathisia/tardive dyskinesia,UKU adverse effects,falls,SAEs explicitly descriptive;N076–N085. No inferential comparison,SE or CI assigned. |
| S040 | [pp1,2,8,9 conclusions](../../../jama_flint_2019_oi_190079.pdf#page=9) | Primary conclusion:O reduces36-week relapse relative P;tradeoff weight gain. Discussed secondary direction:O gain/P loss,greater total-cholesterol decline P,no triglyceride/glucose/HbA1c trajectory difference. Matches S003,S012–S019;age-associated metabolic and genetic aims explicitly deferred p2. |

## Completeness and boundaries

Mapped relationships: 89 numeric/reporting IDs (N001–N089) and 40 statistical IDs (S001–S040), total129 relationship records. The grouped N087/N088 rows expand all eight Table4 and all four Table5 endpoints; corresponding S026–S037 track each inferential result individually. All 10 assigned PDF pages inspected; no scientific coverage gaps. No exact unprinted plotted coordinates, person-time, SEs or test statistics are invented. The main paper supplies no person-time rate endpoint; daily/weekly units refer to longitudinal change coefficients. Every primary, secondary, baseline and safety entry is retained without filtering by significance. Administrative/reference numerals on p10 are explicitly no-applicable study-result units. No legacy candidate, checker, screening, adjudication or final-report artifact was read.

Coordinator transcription update: Numeric checker direct visual confirmation of Table 4 on DOC-001 PDF p.8 establishes olanzapine waist baseline n=63. N087 was updated from 62 to the source value 63. This concerns the new map transcription only; no source or reused artifact was modified and it is not a registered candidate.
