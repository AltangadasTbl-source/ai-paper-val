# Main-paper quantitative evidence map

Scope: DOC-001, jama_wang_2018_oi_180070.pdf, physical PDF pages 1–10 (printed pages 245–254). Document role: REPORT throughout. Mapping status: COMPLETE, 10/10 pages; fresh-required units: 0; scientific gaps: 0. Runtime task: /root/main_mapper; named role qc16_main_quantitative_mapper, gpt-6.1-sol/medium, fresh spawn.

This is a source transcription and relationship map, with no candidate diagnosis or adjudication. M-N001–M-N070 are 70 provisional numeric/definition relationship groups; M-S001–M-S046 are 46 provisional statistical relationship groups. Keys are local map keys, not coordinator-assigned final inventory IDs. Each row may contain several matched scalar observations. The same reported result at several locations is cross-referenced rather than counted repeatedly. Every numeric table cell and every displayed inferential result is included.

## Evidence and tools

Read QUALITY_CONTROL_SCOPE.md, workflow_1_6/review_contract.md, tooling_record.md, source_coverage.md and evidence_asset_inventory.md. Reusable assets consulted: review_1_5_2/preprocessing/layout_text/DOC-001.txt, and rendered_pages/DOC-001-p06.png and DOC-001-p08.png for visual alignment/transcription. Reused historical derivatives have engine limitations documented in the asset inventory; they are aids, and the supplied PDF is authority. Current direct Poppler 25.03.0 pdftotext -layout confirmation of physical p.8 was saved to preprocessing/main-direct-page-08.txt using `pdftotext -layout -f 8 -l 8 jama_wang_2018_oi_180070.pdf .ai_paper_validation/review_1_6/preprocessing/main-direct-page-08.txt`. No Python extraction, OCR, installation or GPU use. Source-matched reusable native text covers all ten pages. Visual p.6 preserves the printed 13.05 percentage; p.8 preserves in-hospital death interval endpoint 0.2 and separate HR/OR columns exactly.

## Page completion ledger

| Physical page | Printed page | Complete mapped scope | Source |
|---|---|---|---|
| 1 | 245 | Abstract population, enrollment/follow-up dates, primary and secondary definitions, composite/all-or-none and vascular results | [PDF p.1](../../../jama_wang_2018_oi_180070.pdf#page=1) |
| 2 | 246 | Key Points repeated primary results, source hospital frame, enrollment/eligibility/time definitions, contextual quantities | [PDF p.2](../../../jama_wang_2018_oi_180070.pdf#page=2) |
| 3 | 247 | Cluster assignment/intervention exposure, all 9 performance-measure definitions, outcome and denominator definitions | [PDF p.3](../../../jama_wang_2018_oi_180070.pdf#page=3) |
| 4 | 248 | Power assumptions, missingness/imputation, all analysis/model/adjustment definitions, result enrollment/baseline/follow-up summaries | [PDF p.4](../../../jama_wang_2018_oi_180070.pdf#page=4) |
| 5 | 249 | Complete Figure1 flow, precise repeated primary/vascular/disability estimates, symptomatic hemorrhage, sensitivity analysis, significance statements | [PDF p.5](../../../jama_wang_2018_oi_180070.pdf#page=5) |
| 6 | 250 | Every Table1 cell and footnote, primary significance repetition, contextual comparison quantities | [PDF p.6](../../../jama_wang_2018_oi_180070.pdf#page=6) |
| 7 | 251 | Every Table2 row/column/footnote, contextual measure counts and clinical curve interpretation | [PDF p.7](../../../jama_wang_2018_oi_180070.pdf#page=7) |
| 8 | 252 | Every Table3 row/column/footnote, complete Figure2 labels/ticks/risk arrays/inference/caption | [PDF p.8](../../../jama_wang_2018_oi_180070.pdf#page=8) |
| 9 | 253 | Limitations numeric/time claims, repeated conclusions; remaining author/disclosure material has no applicable study quantitative results | [PDF p.9](../../../jama_wang_2018_oi_180070.pdf#page=9) |
| 10 | 254 | Investigator/funding/reference material inspected; no additional applicable study quantitative results. Bibliographic years/volumes/pages, grant IDs and numerals in hospital names are identifiers, not result relationships | [PDF p.10](../../../jama_wang_2018_oi_180070.pdf#page=10) |

## Population, exposure, measurement and analysis keys

All source locations in the remainder refer to the physical pages linked above. Intervention always means multifaceted quality improvement; control means routine care plus stroke registry participation. I/C below is intervention/control; B is prerandomization baseline survey. Tables compare I/C, not B with trial groups.

| Key | Exact locations and printed observations / matching rule inputs |
|---|---|
| M-N001 | p.1 abstract design/interventions/results; p.2 Key Points; p.3 randomization; p.4 Results; p.5 Figure1; p.6 Table1: 40 public hospital clusters, 20 I and 20 C, randomized 1:1; 4800 trial patients, 2400 per arm. Mean cluster size120, range102–145 (p.4). No cluster excluded after inclusion (p.4); Figure1 shows 0 hospitals lost in each arm. |
| M-N002 | p.1 design and p.2 Methods: enrollment August10,2014–June20,2015; 12-month follow-up through July30,2016. p.4: enrollment duration I median 207 days (IQR 182–225), C204 days (159–262). p.9: intervention studied over11 months; follow-up beyond1 year discussed. |
| M-N003 | p.1 abstract: 3980 (82.9%) completed12-month follow-up. p.4: I2003 (83.5%), C1977 (82.4%). p.5 Figure1 follow-up: I397 and C423 patients lost; bottom boxes I2003 and C1977 “Patients included in primary analysis.” Each arm earlier shows2400 enrolled and2400 received allocated intervention/control. p.4 independently states all 4800 included in primary analysis. |
| M-N004 | p.1 abstract/p.4 Results: mean age65 years; women1757 (36.6%). Match against Table1 sex counts and age medians with the statistic labels preserved (medians are not means). |
| M-N005 | p.2 Hospitals: alliance563 hospitals,27 provinces+4 municipalities=31 locations;3 hospital grades primary/secondary/tertiary. p.4 Results:40 hospitals from 18 provinces. p.5 Figure1 footnote:40 randomly invited from 563, selected by tertiary/secondary grade and eastern/central/western region. |
| M-N006 | p.2 Patients: age≥18 years, AIS confirmed on CT/MRI within 7 days after symptom onset; admitted directly or via ED. Hemorrhagic stroke/TIA/cerebral venous sinus thrombosis/noncerebrovascular diseases excluded. Hospital eligibility: secondary/tertiary public hospitals with ED, neurological wards and IV rtPA capacity; primary/private/rural hospitals excluded. |
| M-N007 | p.3 interventions:2 professionals per I hospital attended2-day workshop; daily care plan first 7 days and discharge; performance check at least once weekly. p.5: median monitoring-to-feedback interval7 days. |
| M-N008 | p.1 primary outcomes/p.2 Key Points/p.3 Outcomes:9AIS performance measures,6 same as GWTG-Stroke;4 at beginning and5 at discharge. Co-primary composite and all-or-none; either statistically significant makes study interpreted “positive” (p.3). |
| M-N009 | p.3 Outcomes: all-or-none proportion of patients receiving all eligible measures. Composite total eligible measures performed divided by total eligible measures for each patient, calculated per patient then averaged. p.6: no all-or-none credit for some but not all required measures. p.4 analysis: composite modeled as odds of fulfilling care opportunities, each opportunity a dichotomous observation1 met/0 notmet; example eligible 5 of7, received 3, contributes 5 observations,3 ones and2 zeros. Preserve7 in this example separately from 9predefined measures. |
| M-N010 | p.1/p.2/p.3: new vascular event=(ischemic stroke, hemorrhagic stroke, myocardial infarction or vascular death); disability mRS3–5; all-cause death; follow-up3,6,12 months. p.3 says after initial symptom onset; p.5 introductory Clinical Events says after discharge, then gives time point results. Figure2 x-axis says after stroke symptom onset. In-hospital death is distinct. |
| M-N011 | p.4 symptomatic intracerebral hemorrhage: any type on posttreatment imaging related to any worsening neurological condition, among IV rtPA-treated patients. p.5 actual hemorrhage results mapped M-N060/M-S043. |
| M-N012 | p.4 Sample Size: baseline mean composite80%; comparator GWTG baseline 83.52%→firstyear87.85%, increase4.33%; target4800 patients/40 hospitals, median 120 patients/hospital, detect5% improvement,80%power,5%significance,ICC0.02;2400 per arm and enrollment stopped when each group reached 2400. |
| M-N013 | p.4 missingness: smoking highest missingness1.42%, imputed no smoking;1missing NIHSS imputed median 3. Categorical missing values imputed modes; continuous missing values medians. p.9 repeats missing smoking all nonsmoking as limitation. |
| M-N014 | p.4 Data Analysis: intention-to-treat all outcomes; continuous summarized median/IQR, categorical frequency/percentage; Wilcoxon rank-sum and χ² respectively. Comparative outcomes cumulative incidences and absolute differences95%CIs, adjusted patient/hospital characteristics. GEE within-hospital correlation; logistic for all-or-none and disability; composite effects population average odds ratio ORPA. Vascular events/mortality time-to-event; disability mixed model binary link; Kaplan–Meier and multivariable Cox descriptions preserved. |
| M-N015 | p.4 adjustment list/p.7 Table2a/p.8 Table3a: age,sex,ischemic stroke history,hypertension,diabetes,hyperlipidemia,atrial fibrillation,CAD/previousMI,ever smoking,admissionNIHSS,hospital capacity/grade,region,stroke unit,teaching status,neurological ward beds. No adjustment for multiple comparison for co-primary outcomes; secondary analyses exploratory;2-sided tests;P<.05 threshold;SAS 9.3. Differences and ORPA/HR/OR must remain separate estimands and P columns. |
| M-N016 | p.4 sensitivity method/p.5 result: add contraindicated patients to denominator of overall population, to check improved compliance is not merely smaller denominator from contraindication documentation. eTable4 referenced. |

## Table1 complete extraction: p.6 (printed250)

Each count percentage uses hospital denominator B40/I20/C20 or patient denominator B801/I2400/C2400 according to section. Dispersion parentheses on medians are IQRs. No baseline hypothesis P values are printed in Table1.

| Key | Characteristic | B | I | C |
|---|---|---|---|---|
| M-N017 | Hospitals, No. |40|20|20|
| M-N018 | Grade tertiary / secondary |29(72.5) /11(27.5)|15(75.0)/5(25.0)|14(70.0)/6(30.0)|
| M-N019 | Region eastern / central / western |20(50)/9(22.5)/11(27.5)|10(50.0)/4(20.0)/6(30.0)|10(50.0)/5(25.0)/5(25.0)|
| M-N020 | Stroke unit |25(62.5)|14(70.0)|11(55.0)|
| M-N021 | Teaching hospital |25(62.5)|13(65.0)|12(60.0)|
| M-N022 | Neurological ward beds median(IQR) |77(61–178)|70(60–138)|80(61–152)|
| M-N023 | Annual stroke discharges median(IQR) |401(321–761)|365(317–710)|417(321–785)|
| M-N024 | Patients, No. |801|2400|2400|
| M-N025 | Age median(IQR),years |65(57–75)|65(57–73)|64(56–74)|
| M-N026 | Men |486(60.7)|1553(64.7)|1490(62.1)|
| M-N027 | History ischemic stroke |271(33.8)|666(27.8)|722(30.1)|
| M-N028 | History diabetes |193(24.1)|577(24.0)|509(21.2)|
| M-N029 | History hypertension |542(67.7)|1550(64.6)|1540(64.2)|
| M-N030 | History dyslipidemia |65(8.1)|305(12.7)|291(12.1)|
| M-N031 | CAD/previousMI |126(15.7)|311(13.05)|298(12.4)|
| M-N032 | Atrial fibrillation |67(8.4)|118(4.9)|127(5.3)|
| M-N033 | Ever smoking |339(42.3)|1057(44.0)|1059(44.1)|
| M-N034 | NIHSS admission median(IQR) |4(2–8)|4(2–6)|4(2–6)|
| M-N035 | Transport to ED by EMS |112(14.0)|265(11.0)|236(9.9)|
| M-N036 | Symptom onset→ED within 2h, row labeled proportion% |96(12.0)|254(10.6)|238(9.9)|
| M-N037 | LDL median(IQR),mg/dL |111.97(88.80–135.14)|103.08(81.85–126.25)|103.86(80.69–128.57)|
| M-N038 | Length of stay median(IQR),days |13(10–15)|13(10–15)|12(9.5–15)|

Table1 footnotes: NIHSS range0–42,42mostsevere. LDL conversion to mmol/L ×0.0259 (also p.3 Outcomes and p.7 Table2). CAD coronary artery disease; ED emergency department; EMS emergency medical service. p.4 repeated pooled hospital characteristics:72.5%tertiary,62.5%strokeunit,62.5%teaching; “median annual number of beds of neurological wards”77(IQR 61–178). p.4 says groups balanced except length of stay. Labels retained exactly for comparison.

## Table2 complete extraction: p.7 (printed251)

I/C entries are events/eligiblepatients(%), except composite mean(SD)% (not events/total). AD = adjusted absolute difference in percentage points,95%CI; ratio = adjusted ORPA,95%CI;ICC = intracluster correlation. AD positive favors I (footnotea). Population and adjustment M-N015. Each row creates separate statistical AD and ORPA relationships; do not substitute one P value for the other.

| Numeric key | Outcome | I | C | AD(95%CI)% | AD P/key | ORPA(95%CI) | Ratio P/key | ICC |
|---|---|---|---|---|---|---|---|---|
| M-N039 | Composite mean(SD) |88.2(15.1)|84.8(18.2)|3.5(0.7–6.4)|.02 /M-S001|1.39(1.12–1.72)|.003 /M-S002|0.02|
| M-N040 | All-or-none |1290/2400(53.8)|1147/2400(47.8)|6.7(−0.4–13.8)|.06 /M-S003|1.19(0.85–1.67)|.31 /M-S004|0.07|
| M-N041 | IV rtPA within 3h onset |46/212(21.7)|23/204(11.3)|7.3(−5.3–19.9)|.26 /M-S005|3.18(0.94–10.78)|.06 /M-S006|0.28|
| M-N042 | Early antithrombotics |2307/2353(98.0)|2253/2330(96.7)|1.5(−0.3–3.2)|.10 /M-S007|1.93(0.94–3.95)|.07 /M-S008|0.03|
| M-N043 | Dysphagia screening |2255/2328(96.9)|2040/2139(95.4)|1.6(−2.1–5.3)|.41 /M-S009|2.49(0.84–7.40)|.10 /M-S010|0.24|
| M-N044 | DVT prophylaxis |178/645(27.6)|66/592(11.1)|15.6(3.3–27.9)|.01 /M-S011|2.42(1.02–5.72)|.04 /M-S012|0.36|
| M-N045 | Discharge antithrombotics |2272/2324(97.8)|2141/2305(92.9)|4.2(−0.6–8.9)|.09 /M-S013|2.29(0.86–6.11)|.10 /M-S014|0.23|
| M-N046 | Discharge anticoagulation AF |63/155(40.6)|39/137(28.5)|12.9(−5.8–31.6)|.18 /M-S015|1.80(0.68–4.75)|.23 /M-S016|0.25|
| M-N047 | Discharge lipid-lowering LDL>100mg/dL |1415/1481(95.5)|1439/1547(93.0)|2.4(−1.6–6.4)|.25 /M-S017|1.35(0.67–2.73)|.40 /M-S018|0.16|
| M-N048 | Discharge antihypertensive |1510/1838(82.2)|1372/1771(77.5)|6.1(−0.6–12.7)|.07 /M-S019|1.44(0.94–2.20)|.10 /M-S020|0.08|
| M-N049 | Discharge antidiabetic |653/728(89.7)|557/663(84.0)|5.0(0.8–9.3)|.02 /M-S021|1.57(1.08–2.28)|.02 /M-S022|0.03|

Table2 footnotes and p.3 measurement details: rtPA eligible patients arrived within 2h and treated within 3h of symptom onset (b); early antithrombotic within 48h of hospitalization (c); dysphagia before any oral intake (d); DVT among nonambulatory patients by endhospital day2(e). Discharge antithrombotics list aspirin,clopidogrel,ozagrel,dipyridamole,ticlopidine,cilostazol,LMWH,unfractionatedheparin,warfarin(f). p.3 LDL eligibility >100mg/dL or undocumented LDL; Table2 row shows >100mg/dL. AF/fluter appears in p.3 outcome definition; table row says AF. Definitions and contraindications referenced eTable1. No direct SE or test statistics are printed in this table.

### Matched primary narrative precision and interpretations

p.1 abstract and p.5 Adherence: M-N039/M-S001 composite88.2%vs84.8%,AD3.54%(95%CI0.68%–6.40%),P=.02. p.5 further gives M-S002 ORPA1.39(1.12–1.72),ICC.02,P=.003. p.2 KeyPoints repeats88.2%/84.8%,significant. p.9 Limitations raw composite difference3.4%,smaller than power5%improvement. No model-derived difference should automatically be interpreted as the raw subtraction.

p.1/p.5 M-N040/M-S003 all-or-none53.8%vs47.8%,AD6.69%(−0.41%–13.79%),P=.06. p.5 M-S004 ORPA1.19(.85–1.67),ICC.07,P=.31. p.1/p.2/p.5/p.6/p.9 say not statistically significant/not better. p.5/p.6:all 9 individual measures numerically higher I, only DVT and antidiabetic significant. These interpretations map all individual rows, not just two significant results.

## Table3 complete extraction: p.8 (printed252)

All ADs and ratios footnotea adjusted with M-N015 covariates. New vascular events/death ratio column HR; disability ratio column OR. Blank opposite ratio column is meaningful, not a zero. Disability footnoteb:mRS3–5 function status at3,6,12 months after onset; mixedmodel binarylink used and oddsratio calculated. I/C fractions have the printed denominators, including disability-specific non2400 denominators. Two separate inferential relationships per row.

| Numeric key | Outcome/time | I | C | AD(95%CI)% | AD P/key | Ratio type/value(95%CI) | Ratio P/key |
|---|---|---|---|---|---|---|---|
| M-N050 | New vascular3mo |93/2400(3.9)|127/2400(5.3)|−2.0(−3.5–−0.6)|.007 /M-S023|HR0.65(0.49–0.86)|.002 /M-S024|
| M-N051 | New vascular6mo |150/2400(6.3)|186/2400(7.8)|−2.2(−4.0–−0.4)|.02 /M-S025|HR0.72(0.57–0.90)|.004 /M-S026|
| M-N052 | New vascular12mo |218/2400(9.1)|282/2400(11.8)|−3.1(−5.3–−1.0)|.005 /M-S027|HR0.72(0.60–0.87)|<.001 /M-S028|
| M-N053 | Disability3mo |418/2180(19.2)|443/2105(21.0)|−3.7(−6.7–−0.8)|.01 /M-S029|OR0.76(0.63–0.91)|.002 /M-S030|
| M-N054 | Disability6mo |326/2058(15.8)|360/2009(17.9)|−3.9(−6.6–−1.1)|.006 /M-S031|OR0.74(0.61–0.89)|.002 /M-S032|
| M-N055 | Disability12mo |236/1852(12.7)|264/1798(14.7)|−3.1(−5.8–−0.5)|.02 /M-S033|OR0.74(0.59–0.93)|.01 /M-S034|
| M-N056 | Death in hospital |11/2400(0.5)|23/2400(1.0)|−0.7(−1.1–0.2)|.009 /M-S035|HR0.96(0.90–1.02)|.14 /M-S036|
| M-N057 | Death3mo |66/2400(2.8)|76/2400(3.2)|−1.0(−2.1–0.1)|.08 /M-S037|HR0.81(0.57–1.15)|.23 /M-S038|
| M-N058 | Death6mo |103/2400(4.3)|101/2400(4.2)|−0.5(−1.7–0.6)|.38 /M-S039|HR0.97(0.73–1.29)|.81 /M-S040|
| M-N059 | Death12mo |139/2400(5.8)|160/2400(6.7)|−1.5(−3.0–−0.0)|.05 /M-S041|HR0.86(0.68–1.09)|.21 /M-S042|

### Matched clinical narrative precision and interpretation

M-N050/M-S023:p.1andp.5 vascular3mo3.9%vs5.3%,AD−2.03%(−3.51%–−0.55%);p.1P=.007;p.5HR.65(.49–.86). M-N051/M-S025:p.1/p.5vascular6mo6.3%vs7.8%,AD−2.18%(−4.0%–−0.35%);p.1P=.02;p.5HR.72(.57–.90). M-N052/M-S027:p.1/p.5vascular12mo9.1%vs11.8%,AD−3.13%(−5.28%–−0.97%);p.1P=.005;p.5HR.72(.60–.87). p.1 says significantly reduced each time. p.5 refers Table3/Figure2A and supplementeTable3 components.

M-N053/M-S029:p.5disability3mo19.2%vs21.0%,AD−3.72%(−6.7%–−0.79%),OR.76(.63–.91). M-N054/M-S031:p.5disability6mo15.8%vs17.9%,AD−3.86%(−6.60%–−1.13%),OR.74(.61–.89). M-N055/M-S033:p.5disability12mo12.7%vs14.7%,AD−3.13%(−5.80%–−0.46%),OR.74(.59–.93). p.5lower each time; discussion p.5/p.6/p.7 repeats reduced short/longterm vascular/disability outcomes. Narrative does not provide disability Ps here.

p.5clinical events says “There was no significant difference in total mortality rates in the hospital and at 3, 6, and 12 months (Figure 2B).” Preserve as inference claim aligned to every death row, with separate AD and HR results. p.9 discusses whether mortality differences emerge beyond1 year.

## Other results and Figure2

| Key | Locations and complete printed observations |
|---|---|
| M-N060 | p.5 symptomatic hemorrhage among IVrtPA patients:I1/46(2.2%),C2/23(8.7%),P=.26(M-S043); narrative no significant difference. Treatment counts match Table2rtPA numerator46/23, not eligible denominators212/204. No effect/CI given. |
| M-N061 | p.5SensitivityAnalysis:I85.3%,C80.91%,AD4.20%(95%CI1.77%–6.63%),ORPA1.36(1.11–1.67),P=.003;method includes contraindications in denominator; eTable4 referenced. AD/CI M-S044;ORPA/CI/P M-S045. Only one printed P accompanies bracket; do not silently manufacture a second P. p.8 narrative says clinical effect preserved under sensitivity excluding no contraindicated patients. |
| M-N062 | p.8Figure2A:new vascular events; yCumulativeIncidence,ticks0,.05,.10,.15;xdays after stroke symptom onset,ticks0,90,180,270,360. Control curve upper;I lower. Annotation HR.72(95%CI).60–.87;P<.001(M-S028 matched),same estimates Table3vascular12mo. Plot endpoint visually approximately C.125/I.094; those approximations are visual positions, not printed precise results, not substitutes for table proportions. |
| M-N063 | p.8Figure2A No. at risk at days0,90,180,270,360:Control 2400,2275,2003,1891,1839;Intervention 2400,2308,2098,1989,1952. These are event-specific risksets, not follow-up-completion denominators. |
| M-N064 | p.8Figure2B deaths; same ylabel/ticks0,.05,.10,.15 and xdays after onset0,90,180,270,360. Control aboveI at end;curves close/occasionally cross. AnnotationHR.86(95%CI).68–1.09;P=.21(M-S042 matched),same Table3death12mo. Endpoint visually C≈.070/I≈.060; approximations only. |
| M-N065 | p.8Figure2B No. at risk at days0,90,180,270,360:Control 2400,2327,2080,1979,1951;Intervention 2400,2334,2146,2041,2023. |
| M-N066 | p.8Figure2caption: medianfollow-up I364 days(IQR 364–365),C365 days(IQR 364–365); log-rank test compares days after onset to vascular event or death(M-S046 method relationship). No distinct log-rank statistic or additionalP printed in caption; annotation Ps retained at their visible locations without inferring their analytical provenance. p.7 narrative calls these “HR curves” and says new vascular-event curves almost completely separated in first 30 days; Figure2labels cumulativeincidence. |
| M-N067 | p.5Figure1:40 invited,3excluded “declined to participate”,37agreed,3replacement hospitals added,40randomized. p.4Results:3 hospitalsunexpected inability to conduct trial replaced according characteristics. All2arms20 hospitals allocated and20implemented;2400 patients each enrolled/received allocation;0 hospitals lost;I397/C423 patients lost;20 hospitals each included in primary analysis;I2003/C1977 patients included in primary analysis. See M-N001/M-N003 for population matches. |
| M-N068 | p.2background2.4 millionnewstrokeevents2013;developingcountriesup to 78%globalburden. p.5discussionpublichospitals92%Chinaadmissions. Context only, supplied-reportprinted claims; no external verification. |
| M-N069 | p.6historicalGWTG composite83.52%→93.97%from 2003to 2009;TargetStroke10 keystrategies. p.7PRISMM5 of10performancemeasuressameascurrenttrial. These are reported contextual comparison/label counts; do not align them with trial9measure results. |
| M-N070 | p.9Limitations:rawcompositedifference3.4%vsminimumdetectable5%;11 monthintervention;additionalmortalityfollow-upbeyond1 year. p.1/p.2/p.9conclusion:statistically significant small composite improvement but all-or-none not significant. p.8 interpretationclinicaleffectsizegreaterthanprocesseffectsize,mayonlypartiallybecapturedbyprocessmeasures. These statements reference existingresultkeys rather than new effect estimates. |

## Statistical scope registry

M-S001–M-S022: every Table2 AD/CI/P and ORPA/CI/P separately, row order. M-S023–M-S042: every Table3 AD/CI/P and HR-or-OR/CI/P separately, row order. Matched abstract/narrative/Figure2 locations are recorded above with exact higher precision. M-S043 symptomatic hemorrhage proportions/P; M-S044 sensitivity AD/CI; M-S045 sensitivity ORPA/CI/P; M-S046 Figure2 caption log-rank method and alignment with visible HR/P annotations. All46 groups mapped without significance-based selection. No reported SE or test statistic was located. No displayed-zero P value occurs in mapped main results.

Missing inferential details are reported as definition boundaries, not extraction gaps: main text does not provide formula/SE for adjusted AD CIs; exact relation of log-rank comparison to adjusted annotation Ps is not specified in caption; one sensitivity P appears alongside AD andORPA in one bracket. Checkers must use supplied-plan/result-supplement evidence to align these where available rather than infer unreported details.

## Completion and limitations

All ten pages complete. Every table cell, count/proportion denominator, effect/CI/P/ICC, plot printed quantitative label/risk array, primary/secondary definition, matching narrative value and relevant interpretation is mapped. No source scientific coverage gap. No reuse assets changed. Exact continuous curve data are not tabulated in the source; only the printed ticks, annotations, risksets and visual ordering/approximate endpoints are extractable. Source PDF links are three directories above this artifact and end #page=N. References/funding/author material inspected and explicitly no additional applicable study results.
