# Complete main-paper quantitative evidence map

DOC-001: `jama_flint_2019_oi_190079.pdf`, physical pages1-10 (journal622-631), REPORT throughout. Fresh mandatory mapper runtime01a12865-5284-7fd3-8b3b-5e3162260ca4, gpt-6.1-sol/medium. O=sertraline+olanzapine; P=sertraline+placebo. Local keys are match locators; coordinator owns global N/S IDs. No candidate diagnosis or adjudication.

All10 reusable native pages read: `.ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-001.txt` through `page-010.txt` (legacy PyMuPDF native extraction; historical version unavailable). Rendered pages003,005,006,007,008,009 visually inspected (legacy PyMuPDF PDF render; historical version unavailable), including both figures/all tables. No old candidate/decision/report input. No fresh-required units, OCR, fallback or GPU. Source links below resolve relative to this artifact at `../../../jama_flint_2019_oi_190079.pdf#page=N`.

## Page completion

| Physical page | Journal page | Complete scope | Status |
|---|---:|---|---|
|1|622|Abstract/design/population/medication/all outcomes/conclusion|COMPLETE|
|2|623|Background/methods/eligibility/remission/Key Points|COMPLETE|
|3|624|Whole Figure1/footnote/near-remission/randomization eligibility|COMPLETE|
|4|625|Randomization/taper/visits/relapse/secondary scales/power/models|COMPLETE|
|5|626|Whole Table1/all footnotes/models/missingness/sensitivity|COMPLETE|
|6|627|Whole Table2/all footnotes/statistical conventions/conversions/primary result|COMPLETE|
|7|628|Whole Table3/Figure2/covariates/NNT/sensitivity/secondary/tolerability|COMPLETE|
|8|629|Whole Table4/footnotes/hospitalization/discussion/limitations|COMPLETE|
|9|630|Whole Table5/footnotes/limitations/conclusion/administrative remainder|COMPLETE|
|10|631|All administrative and references1-35 inspected; no additional applicable trial results|COMPLETE_NO_APPLICABLE_NEW_RESULTS|

Total10; reusable10; fresh-required0; mapped10; scientific gaps none. Limitations: graphical survival coordinates approximate, historical engine versions unavailable, some prose pages lack renders. Every assigned unit mapped.

## Population, time, scale, model, and inference definitions

[Page1](../../../jama_flint_2019_oi_190079.pdf#page=1):36-week RCT,4 centers,age≥18,acute≤12 weeks,8-week remission/near-remission stabilization; November2011-June2017,last follow-upJune13,2017. Randomized126,age mean(SD)55.3(14.9)years,women78(61.9%),completed114(90.5%),O64/P62. Randomization median sertraline150mg/day(IQR150-200),olanzapine15mg/day(IQR10-20). Key Points [p2](../../../jama_flint_2019_oi_190079.pdf#page=2) repeats126,age≥18,36weeks,O13(20.3%)/P34(54.8%) relapses,significant difference. p6:269 enrolled,126 randomized,O64/P62. Abstract completion quantity preserved without imposing flow definition.

[p2](../../../jama_flint_2019_oi_190079.pdf#page=2):acute enrollment ages18-85,major depressive episode≥1 delusion,HDRS17≥21,SADS delusion≥3,Delusion Assessment Scale≥2 on any3 conviction items. Exclusions include IQCODE26-item mean≥4,substance abuse/dependence preceding3months,type1 diabetes. Acute sertraline target150-200mg/day in50mg pills,olanzapine15-20mg/day in5mg pills. Remission=no delusions/hallucinations,HDRS≤10 for2 consecutive weeks. Near-remission after12weeks=no psychosis,HDRS11-15 with≥50% baseline reduction,CGI very much/much improved. [p3](../../../jama_flint_2019_oi_190079.pdf#page=3):after8-week stabilization still remission/near-remission,MMSE≥24 eligible36-week RCT. Background STOP-PD12-week duration historical. Protocol aims1/2 reported,age/metabolic/genetic additional aims not reported.

[p4](../../../jama_flint_2019_oi_190079.pdf#page=4):computer randomization1:1,blocks4-8,strata ages18-59 vs60-85,remission vs near-remission,site. Sertraline continues; blinded O continuation/placebo switch over4-week taper. Visits weekly first8weeks,then every4weeks to36weeks/relapse/termination. Drug discontinuers followed where possible. Relapse≥1:DSM-IV depressive episode,HDRS17≥18,SCID psychosis,suicide plan/attempt,mania/hypomania,psychiatric hospitalization. Relapse ends study. Weight/waist each visit;fasting lipids/glucose/HbA1c baseline/every8weeks/termination;extrapyramidal baseline/every4weeks/termination.

p4 scale definitions:Simpson-Angus0-40 higher worse;Barnes global0-5 higher worse,incident baseline0/subsequent≥2;AIMS0-5 each10items higher worse,incident Schooler-Kane;UKU0-3 each48items higher worse,adverse effect2-point rise or score3or4 with increase (wording preserved). Weight adverse gain/loss>7% above/below premorbid most-recent known pre-episode weight. Falls each visit;serious event death/life-threatening/significant disability/hospitalization.

p4 power:planned176 randomized,80% power,20% relapse-risk difference,≤15% attrition,NNT5 prevent1 relapse,analogy1year antidepressant continuation. After3years recruitment revised128 approved following higher overall relapse risk. These are design/power quantities.

[p4-6 models](../../../jama_flint_2019_oi_190079.pdf#page=4):all randomized analysis,Cox treatment/age/remission/site,PH complementary-log-log inspection and Schoenfeld residual-time correlation tests(no numbers). Post hoc Cox excludes medication-discontinuing participants retaining assessment. Linear mixed participant random intercept/continuous-time random slope,fixed site/time/treatment/treatment×time. p7 explicitly linear+quadratic time,daily rates cannot extrapolate to cumulative linear change. Simpson-Angus Poisson mixed with overdispersion,random intercept,fixed site/time/treatment/interaction. MAR;pattern-mixture early termination investigations,triglyceride pattern-mixture-averaged estimates. Statin/hypoglycemic sensitivity excludes data from start/change onward. SAS9.4,all tests2-sided,overall5%,secondary P Holm stepdown adjusted post hoc/exploratory. Table4 post hoc unadjusted within-group mean/median changes;Table5 post hoc unadjusted between-group differences,exactCI only b rows. No printed SE,test statistic,person-time total,or log-rank statistic.

[p6 conversions](../../../jama_flint_2019_oi_190079.pdf#page=6),repeated Tables4/5:cholesterol mg/dL→mmol/L×0.0259;glucose×0.0555;triglycerides×0.0113;lb→kg×0.45;inches→cm×2.54. HbA1c Table4 unit%,abstract/p7 daily estimate printed mg/dL.

## Figure1 complete participant flow

[p3](../../../jama_flint_2019_oi_190079.pdf#page=3),visual inspected. Counts; treatment receipt and final disposition different stages.

|Key|Node|Total/detail|
|---|---|---|
|FLOW01|Consented/assessed|350|
|FLOW02|Excluded|81:not eligible60;withdrew16;other5|
|FLOW03|Started open-label sertraline/olanzapine|269|
|FLOW04|Acute discontinuation|74:withdrew31;insufficient response/worsening21;not appropriate research7;adverse5;medical1;other9|
|FLOW05|Completed acute|195|
|FLOW06|Symptoms not remitted excluded|33|
|FLOW07|Entered stabilization|162|
|FLOW08|Stabilization discontinued|15:worsening4;withdrew2;died not suicide1;not appropriate research1;other7|
|FLOW09|Completed stabilization|147|
|FLOW10|Not randomized|21:not eligible12;did not consent9|
|FLOW11|Randomized|126:O64/P62|
|FLOW12|O received allocation|59;not as randomized5:discontinued3;open-label olanzapine2|
|FLOW13|P received allocation|60;not as randomized2:discontinued1;open-label olanzapine1|
|FLOW14|O primary analysis|64:completed remission/near-remission43;relapsed13;discontinued8:died not suicide1,withdrew5,moved1,transport1|
|FLOW15|P primary analysis|62:completed remission/near-remission24;relapsed34;discontinued4:medical1,withdrew3|

Footnote a inappropriate research examples repeated nonadherence assessments/medications open-label acute/stabilization. All reasons retained. Abstract114 completed separate printed quantity; no assumed definition.

## Table1 all rows

[p5](../../../jama_flint_2019_oi_190079.pdf#page=5),Characteristics of Study Participants,O n64/P n62,No.(%) unless specified. Acute clinical baseline distinct from randomization. Explicit restricted n retained.

|Key/row|O|P|
|---|---|---|
|T1-01 Age mean(SD)y|55.0(15.1)|55.7(14.9)|
|T1-02 Age18-59|36(56.2)|36(58.1)|
|T1-03 Age≥60|28(43.8)|26(41.9)|
|T1-04 Men|27(42.2)|21(33.9)|
|T1-05 Women|37(57.8)|41(66.1)|
|T1-06 White|54(84.4)|49(79.0)|
|T1-07 Black|6(9.4)|9(14.5)|
|T1-08 Other race|4(6.3)|4(6.5)|
|T1-09 Hispanic|6(9.4)|9(14.5)|
|T1-10 Single|19(29.7)|15(24.2)|
|T1-11 Married|28(43.8)|35(56.5)|
|T1-12 Separated/divorced|12(18.8)|7(11.3)|
|T1-13 Widowed|5(7.8)|5(8.1)|
|T1-14 Education mean(SD)y|14.4(3.2)|13.4(3.9)|
|T1-15 With others|46(71.9)|49(79.0)|
|T1-16 Alone|17(26.6)|10(16.1)|
|T1-17 Senior residence|1(1.6)|1(1.6)|
|T1-18 Inpatient acute enrollment|41(64.1)|46(74.2)|
|T1-19 Cornell|16(25.0)|15(24.2)|
|T1-20 Massachusetts|15(23.4)|14(22.6)|
|T1-21 Pittsburgh|9(14.1)|10(16.1)|
|T1-22 Toronto UHN|24(37.5)|23(37.1)|
|T1-23 ≥2 lifetime depressive episodes|47(73.4)|47(75.8)|
|T1-24 Episode duration median(IQR)mo|5.5(3-12)|5.5(2-12),n60|
|T1-25 First episode age median(IQR)y|37(24-50),n62|35(18-51),n61|
|T1-26 Current suicide attempt|13(20.3)|12(19.4)|
|T1-27 Current resistance|3(4.7)|5(8.1)|
|T1-28 Hyperlipidemia|18(29.0)|19(29.7)|
|T1-29 Hypertension|17(26.6)|22(35.5)|
|T1-30 Diabetes|12(18.8)|15(24.2)|
|T1-31 Premorbid weight mean(SD)lb|166.6(34.6),n60|171.4(40.2),n59|

Footnotes:a Other includes American Indian/Alaska Native,Asian,Native Hawaiian/other Pacific Islander,unknown/not reported;b resistance antidepressant+antipsychotic rating≥3 Antidepressant Treatment History Form or≥7 electroconvulsive treatments current episode;c weight most recent known pre-episode;lb×0.45kg. Preserve living arrangement and diagnosis cells without filling unprinted categories/denominators.

## Table2 all randomization rows and footnotes

[p6](../../../jama_flint_2019_oi_190079.pdf#page=6),Clinical Characteristics at Randomization,O n64/P n62;No.(%) except explicit mean(SD)/median(IQR). Barnes/AIMS count decimals printed as such.

|Key/row|O|P|
|---|---|---|
|T2-01 HDRS17 mean(SD),a|5.3(3.6)|5.6(3.6)|
|T2-02 SADS delusion1,b|64(100)|62(100)|
|T2-03 SADS hallucination1,c|64(100)|62(100)|
|T2-04 HADS anxiety median(IQR),d|5.0(2.0-8.0)|4.0(1.0-7.0),n61|
|T2-05 CORE median(IQR),e|1.0(0-3.0)|1.0(0-4.8)|
|T2-06 CIRS-G median(IQR),f|3.0(1.0-6.0)|3.0(2.0-5.8)|
|T2-07 MMSE mean(SD),g|28.1(1.9)|27.9(2.0)|
|T2-08 DKEFS trail-making4 vs5 scaled mean(SD),h|7.9(3.5),n61|8.1(3.6),n59|
|T2-09 DKEFS color-word condition3 final weighted scaled mean(SD),i|8.6(2.9),n60|7.6(2.8),n58|
|T2-10 Barnes global>0,no row superscript|3.0(4.7)|2.0(3.2)|
|T2-11 AIMS overall>0,j|2.0(3.1)|2.0(3.2)|
|T2-12 Simpson-Angus median(IQR),k|1.0(0-2.0)|1.0(0-2.0)|
|T2-13 Sertraline median(IQR)mg/day|150(150-200)|150(150-200)|
|T2-14 Olanzapine median(IQR)mg/day|15(10-20)|15(10-20)|

Exact footnote labels:a HDRS0-52 higher worse,mean5 remission;b delusion1-7 higher worse,1 absent;c hallucination1-3,1 absent/3 definite;d HADS0-21 higher worse,≤7 normal(native control character resolved from image);e CORE0-54 higher worse,median1 minimal;f CIRS excluding psychiatric0-52 higher worse,median3 low physical illness;g MMSE0-30 higher better,mean28 normal;h defines BOTH trail-making flexibility and color-word inhibition,both scaled1-19 higher better,10 normative mean;i describes Barnes global0-5 higher worse,0 absent;j AIMS global0-4 higher worse,0 absent;k Simpson-Angus excluding head-dropping0-36 higher worse,0 absent. Row superscripts and footnote content retained independently.

## Primary inferential/survival results

|Key|Source|Population/contrast/model|Estimate/95%CI|P or statement|
|---|---|---|---|---|
|PRI01|p1,p2,p6|36-week relapse O13/64 vs P34/62|20.3% vs54.8%|Key Points significant|
|PRI02|p1,p6|All-randomized adjusted Cox O vsP,age/remission/site|HR0.25(0.13-0.48)|<.001|
|PRI03|p6|Same Cox young vsold|HR0.78(0.42-1.46)|.44|
|PRI04|p7|Same Cox remission vsnear-remission|HR2.45(0.98-6.13)|.06|
|PRI05|p7|Same Cox Massachusetts vsCornell|HR1.53(0.62-3.76)|.36|
|PRI06|p7|Same Cox Pittsburgh vsCornell|HR1.09(0.39-2.98)|.88|
|PRI07|p7|Same Cox Toronto vsCornell|HR1.80(0.81-4.03)|.15|
|PRI08|p7|Post hoc Cox excluding7 medication discontinuers retaining assessments|HR0.22(0.11-0.43)|<.001|
|PRI09|p7,p8|O number treated prevent1 relapse|NNT2.8|p7 says based on HR;p8 repeat|
|PRI10|p7 Fig2|Kaplan-Meier free-relapse O/P,log-rank|shading95%CI,no exact intervals printed|<.001|
|PRI11|p7 Fig2|Observed duration weeks|O median36(IQR24.8-36);P19.5(IQR5.3-36)|p9:50% P observed≤20weeks|

[p7 Figure2](../../../jama_flint_2019_oi_190079.pdf#page=7):x time weeks0,4,8,12,16,20,24,28,32,36;y proportion free-relapse0,.2,.4,.6,.8,1. Exact printed at-risk table:

|Week|0|4|8|12|16|20|24|28|32|36|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|O|64|60|57|56|52|52|49|47|44|43|
|P|62|54|39|36|32|31|28|26|25|24|

Graphical approximations only:O starts1.0/ends~.78,P starts1.0/ends~.44,O aboveP after initial steps. No exact curve coordinates/CI endpoints/event/censor times printed. p8 majority P relapses first12weeks,O across36.

## Table3 all relapse event counts

[p7 Table3](../../../jama_flint_2019_oi_190079.pdf#page=7),Number of Relapse Events,O/P column headers without new n. Overall relapsers13/34 separate.

|Key/row|O|P|
|---|---:|---:|
|T3-01 Depression,no psychosis|5|18|
|T3-02 Psychosis,no depression|0|1|
|T3-03 Depression+psychosis|4|11|
|T3-04 Suicide plan/attempt|0|3|
|T3-05 Mania/hypomania|0|0|
|T3-06 Psychiatric hospitalization|6|11|

Footnote a more than1 event in some relapse cases;b hospitalization for depression/psychosis/suicidality/mania/hypomania. Overlapping event counts,not mutually exclusive participant count. p8 hospitalized relapsers O6/13(46.2%),P11/34(32.3%) exact displayed percentage.

## All secondary model results

[p1 abstract](../../../jama_flint_2019_oi_190079.pdf#page=1),[p7 narrative](../../../jama_flint_2019_oi_190079.pdf#page=7):treatment×linear-time interaction,O vsP,daily rate,95%CI,P Holm-adjusted in narrative. Abstract same estimates/CIs without P. Linear/quadratic time cannot extrapolate cumulatively.

|Key/outcome|Estimate/unit|95%CI|AdjustedP|Narrative|
|---|---|---|---|---|
|SEC01 Weight|0.13lb|0.11 to0.15|<.001|higher/significant|
|SEC02 Waist|0.009inches|0.004 to0.014|.002|higher/significant|
|SEC03 Total cholesterol|0.29mg/dL|0.13 to0.45|.003|higher/significant|
|SEC04 LDL|0.04mg/dL|−0.01 to0.10|.57|not different|
|SEC05 HDL|−0.01mg/dL|−0.03 to0.01|.99|not different|
|SEC06 Triglyceride|−0.153mg/dL|−0.306 to0.004|.25|not different,pattern-mixture averaged|
|SEC07 Glucose|−0.02mg/dL|−0.12 to0.08|.99|not different|
|SEC08 HbA1c|−0.0002mg/dL|−0.0021 to0.0016|.99|not different|

eFigures1-8 Supplement2 trajectories matched;Table4 separate post hoc raw within-group changes. p8 O gain/P loss,total cholesterol decreases both greater P decline,no significant triglyceride/glucose/HbA1c group-trajectory differences.

SEC09 p7 sensitivity:statin starts/changes12 O6/P6;hypoglycemic3 O2/P1,qualitatively similar results,no estimates supplied. SEC10 p7 Table5 incidence differences not statistically significant,no P supplied,power possibly insufficient.

## Table4 all cells

[p8 Table4](../../../jama_flint_2019_oi_190079.pdf#page=8),visually inspected rotated source. O header n64/P n62. Values mean(SD) except triglyceride/glucose median(IQR). Difference mean(95%CI) except triglyceride/glucose median(95%CI). `blank` means unprinted sample-count cell,not inferred n. Baseline blank O weight,P all except weight/waist. All terminal n printed.

|Key/outcome/unit|O baseline n,value|O termination n,value|O difference(95%CI)|P baseline n,value|P termination n,value|P difference(95%CI)|
|---|---|---|---|---|---|---|
|T4-01 Weight lb|blank,178.6(39.4)|62,183.6(40.9)|5.7(3.3-8.1)|60,182.5(39.8)|59,180.2(42.1)|−3.1(−5.4 to−0.8)|
|T4-02 Waist inches|63,38.1(5.4)|59,38.5(5.2)|0.6(0.1 to1.1)|58,39.4(5.7)|55,38.4(6.4)|−0.8(−1.5 to−0.2)|
|T4-03 Total cholesterol mg/dL|63,209.0(51.3)|63,204.8(51.3)|−4.7(−14.9 to5.6)|blank,220.4(46.8)|59,197.4(48.2)|−22.3(−32.7 to−11.9)|
|T4-04 LDL mg/dL|62,132.5(42.1)|63,128.9(42.3)|−2.8(−12.6 to6.9)|blank,137.7(38.7)|59,122.1(44.2)|−16.0(−25.8 to−6.2)|
|T4-05 HDL mg/dL|63,54.4(19.6)|63,49.7(16.1)|−5.0(−9.1 to−0.9)|blank,56.0(16.0)|59,52.2(16.0)|−3.5(−6.2 to−0.9)|
|T4-06 HbA1c %|63,5.9(1.5)|62,5.7(1.1)|−0.2(−0.5 to0.2)|blank,5.9(1.2)|58,5.9(1.0)|0.1(−0.1 to0.2)|
|T4-07 Triglyceride mg/dL medians|63,134(90-186)|63,133(87-206)|−3.9(−18 to12)|blank,121(95-169)|59,107(80-153)|−18(−25 to−7)|
|T4-08 Glucose mg/dL medians|63,90(83-99)|63,92(87-104)|1.4(−1.8 to5)|blank,93(85-100)|59,94(85-106)|2.8(−3.6 to6.0)|

Footnote a difference may not equal termination minus baseline because missing data. Preserve differences distinct from subtraction of marginal means/medians. Paired n/CI method/P not supplied. HbA1c unit% explicitly;conversions above. No person-time.

## Table5 all cells/thresholds

[p9 Table5](../../../jama_flint_2019_oi_190079.pdf#page=9),Post Hoc Outcome Number of Participants Who Experienced an Incident High Fasting Metabolic Value in RCT. O n64/P n62;Absolute Unadjusted Difference Between Groups,%(95%CI),signed O−P.≥1 value higher than BOTH participant baseline and threshold;≥1 observation count,not threshold≥.

|Key/outcome|Threshold mg/dL|O count(%)|P count(%)|Difference percentage points(95%CI)|Footnotes|
|---|---:|---|---|---|---|
|T5-01 Total cholesterol|240|9(14.1)|6(9.7)|4.3(−8 to17.2)|a|
|T5-02 LDL|160|9(14.1)|6(9.7)|4.3(−8 to17.2)|a|
|T5-03 Triglyceride|200|4(6.3)|2(3.2)|3.0(−6.7 to13.3)|a,b exactCI|
|T5-04 Glucose|126|4(6.3)|4(6.5)|−0.2(−9.9 to9.9)|a,b exactCI|

No numerical P. a definition higher baseline AND threshold;b exactCI only triglyceride/glucose. Conversions above. Total/LDL identical counts/differences retained as separate rows.

## Other tolerability/narrative matches

[p7](../../../jama_flint_2019_oi_190079.pdf#page=7),[p8 continuation](../../../jama_flint_2019_oi_190079.pdf#page=8). Descriptive except Simpson-Angus;no inferential P for other rows.

|Key/outcome|O|P|
|---|---|---|
|TOL01 Incident akathisia|4.7%|4.8%|
|TOL02 Akathisia severity|All except1 mild,pooled|Exception group unspecified|
|TOL03 Incident tardive dyskinesia|0%|3.2%|
|TOL04 Simpson-Angus weekly change O vsP|0.022points,95%CI0.009-0.036,adjustedP=.009|reference,O higher|
|TOL05 UKU weight gain≥once|17.2%|4.8%|
|TOL06 Weight loss≥once|7.8%|4.8%|
|TOL07 Sleepiness/sedation≥once|7.8%|3.2%|
|TOL08 Orthostatic dizziness≥once|7.8%|3.2%|
|TOL09 Nausea/vomiting≥once|3.1%|8.1%|
|TOL10 ≥1 fall|20/64(31.3%)|11/62(17.7%)|
|TOL11 ≥1 serious adverse event|12/64(18.8%)|12/62(19.4%)|
|TOL12 Ruptured aortic aneurysm death|1|No corresponding death reported|
|TOL13 Other serious events|All others hospitalization,no event total|Hospitalization,no event total|
|TOL14 Psychiatric hospitalization relapsers|6/13(46.2%)|11/34(32.3%)|

UKU list introduced as effects in>5% of participants;group percentages supplied,pooled numerator/denominator unprinted. Do not infer exact counts from percentages. Simpson-Angus eFigure9 trajectory reference;weekly points wording retained separately from Poisson model definition,no transform rule supplied.

[p8-9 discussion/limitations](../../../jama_flint_2019_oi_190079.pdf#page=8):NNT2.8;majority P relapse first12weeks,O across36;O weight gain/P loss;total cholesterol decline both,steeper P;no triglyceride/glucose/HbA1c trajectory difference. Historical reference-study ages18-65 distinct from trial.4-week taper repeated;50% P observed≤20weeks;45% switched placebo did not relapse and described as benefiting from weight/lipid decline. p1,p2,p9 conclusion O lowers36-week relapse risk balanced weight gain. No new conclusion estimate.

## Accounting and limitations

Grouped keys:FLOW15,T1 31,T2 14,PRI11,T3 6,SEC10,T4 8,T5 4,TOL14=113 quantitative match records retaining all components/repeated occurrences. Additional complete prose definition relationships:eligibility/time/outcome/scales/model/adjustment/power/conversions/quantitative narrative. Distinct inferential relationships:7 Cox(PRI02-08),1 log-rank(PRI10),8 secondary(SEC01-08),16 within-group Table4(8×2),4 Table5 differences,1 Simpson-Angus(TOL04)=37. Repeated abstract/narrative not new analyses.

p10 all references1-35 and administrative statements inspected:no additional applicable current-trial results. Grants MH62446,MH62518,MH62565,MH62624 and bibliographic numbers are identifiers. No source unit omitted. No candidate diagnosis or disposition assigned.
