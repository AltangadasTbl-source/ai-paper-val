# DOC-001 Numeric Relationship Inventory

Scope: REPORT main article PDF pages 1-11. Fresh independent mapping of reusable raw native/OCR/image evidence. C = conservative oxygen therapy, U = usual oxygen therapy. Every row is an assessment-ready relationship, not a finding. Locations are one-based physical PDF pages in `jama_martin_2025_oi_250042_1753377747.91025.pdf`. All numeric inputs are printed; count-to-percentage assessment uses n/d ×100 with half-unit display intervals. Model effects are tracked in the statistical part and must not be equated with crude ratios. No person-time rate, printed test statistic, or printed standard error appears in these pages.

| ID | Exact source location | Printed inputs and matching claims | Definition / assessment hook |
|---|---|---|---|
| N001 | p1 abstract; p2 Key Points; p4 Figure1/narrative | 16500 randomized; C8258 U8242; 97 ICUs | Arm sum, abstract/flow agreement; randomized population differs from analyzed population. |
| N002 | p1 abstract; p4 Figure1/narrative | Primary observed data 16394: C8211 U8183 | Sum available-case counts; distinguish imputed n16434. |
| N003 | p1 abstract; p4 narrative; p5 Table1 age/sex | Both groups median age60 (IQR48-71); females5652 (38.2%) | Female count2803+2849; sex-available denominators7340+7465 rather than all randomized. |
| N004 | p1 abstract; p6 oxygen exposure; p7 Figure2C | Exposure29% lower abstract; 29.3% body; C20.3 U28.7 100%-equivalent h; difference−8.4 | Relative reduction(28.7−20.3)/28.7; rounded abstract; standardization defined p3. |
| N005 | p1 abstract; p2 Key Points; p6 outcomes; p8 Table2 | 90-day deaths C2908/8211(35.4%), U2858/8183(34.9%) | Count/denominator percentages and all matching locations; inferential effect S010-S012. |
| N006 | p2 population/randomization; p3 interventions | ≥18y; enroll within12h; previous randomization within90d excluded; 1:1; variable blocks; stratify site and HIE/sepsis/brain injury/none; no blinding | Analysis unit individual; hierarchical diagnostic strata; eligibility/contrast anchors for plan comparison. |
| N007 | p1 objective/intervention; p2 Key Points/objective; p3 interventions; p9 conclusion | SpO2 target90%, range88%-92%; alarms below88%/above92%; upper alarm may cease at FiO2=.21; usual therapy no minimum FiO2/upper alarm; until90d/discharge, restart if ICU readmission | Match intervention duration and target; no mandated usual target. |
| N008 | p3 data collection | Hourly SpO2/FiO2 for10d; ~15% enhanced; first10/site then random10% later; extended if unacceptable adherence | Enhanced subset denominator definitions; selected cohort not full trial. |
| N009 | p3 exposure definition | FiO2 above.21:1h at1.0 or2h at.605 =1 100%-equivalent h; additional79% maximum/hour | Exposure = integral(FiO2−.21)/.79; example units and equivalent scaling. |
| N010 | p4 Figure1 top boxes | Screened52747; initial exclusions3514=3239 FiO2=.21 age eligible +243<18 FiO2 eligible +32 both; inclusion49233 | Components, subtraction and eligibility criteria. |
| N011 | p4 Figure1 middle boxes | Exclusion10754=10582 arm indicated/contraindicated +108 prior90d randomization +64 ECMO; narrative potentially eligible38479 |49233−10754 and sum exclusion reasons. |
| N012 | p4 Figure1 nonrandomized box |21979 eligible not randomized=14865 missed/late +6589 clinical decision +272 nonclinical +213 prospectively refused +40 no reason | Sum reasons; 38479−21979=16500. Clinical reasons imminent extubation/discharge/transfer/death/withdrawal. |
| N013 | p4 Figure1 arms/narrative | C8258 treated as randomized,28 all-data removal →8230; U8242 treated as randomized,38 removal →8204; total66(.4%) removed | Flow subtraction, totals and removal percent of16500. |
| N014 | p4 Figure1/narrative | Analyzed16434=C8230+U8204; observedC8211/U8183; another40(.2%) unlinked and imputed | Missing arm counts19/21; 40 of analyzed/randomized; retained when unlinked. |
| N015 | p4 Figure1 | Secondary linkage consent C7463 U7595 | Consent availability compared with observed secondary outcome denominators, allowing outcome-specific availability. |
| N016 | p4 Figure1/narrative/footnotee |12mo follow-up C6534 U6518=13052; 3382 not yet12mo at final linkage |13052+3382=16434; death registration linkage March2025,90d follow-up February2025; enrollment May4,2021-Nov27,2024. |
| N017 | p4 narrative; p5 Table1 diagnosis | Combined HIE1504(9.2%), sepsis5443(33.1%), brain injury363(2.2%), none9124(55.5%); COVID1099(6.7%) | Sum diagnostic strata16434 and arm counts; COVID overlaps diagnostic strata. |
| N018 | p4 narrative; p7 Figure2 baseline | Enhanced2489=C1252+U1237 | Match baseline figure contributor counts and subset selection. |
| N019 | p4-p6 narrative | COVID13.4% first10/site; 5.3% random subsequent; 6.4% standard | Different data-collection cohorts; denominators not printed here, linked eTable4. |
| N020 | p5 Table1 age | C60(48-71)[8230]; U60(48-71)[8204] years | Median and IQR order, population; matches pp1/4. |
| N021 | p5 Table1 sex | FemaleC2803/7340(38.2), U2849/7465(38.2); maleC4537/7340(61.8), U4616/7465(61.8) | Sex categories sum each denominator; consent footnotea. |
| N022 | p5 Table1 ethnic Asian | C263/7340(3.6), U243/7465(3.3) | Per-arm percentage and ethnicity sum N027. |
| N023 | p5 Table1 ethnic Black | C138/7340(1.9), U153/7465(2.0) | Per-arm percentage. |
| N024 | p5 Table1 ethnic White | C6072/7340(82.7), U6207/7465(83.1) | Per-arm percentage. |
| N025 | p5 Table1 ethnic Mixed | C52/7340(.7), U60/7465(.8) | Per-arm percentage. |
| N026 | p5 Table1 ethnic Other/not stated | C815/7340(11.1), U802/7465(10.7) | Per-arm percentage; other includes Chinese/not dictionary groups per footnoteb. |
| N027 | p5 Table1 ethnic block | C263+138+6072+52+815; U243+153+6207+60+802 | Exhaustive categories sum7340/7465, printed percentages approximately100%. |
| N028 | p5 Table1 BMI<18.5 | C264/7111(3.7), U259/7225(3.6) | BMI kg/m²; percentages. |
| N029 | p5 Table1 BMI18.5-<25 | C2291/7111(32.2), U2299/7225(31.8) | Percentages. |
| N030 | p5 Table1 BMI25-<30 | C2129/7111(29.9), U2250/7225(31.1) | Percentages. |
| N031 | p5 Table1 BMI30-<40 | C1918/7111(27.0), U1881/7225(26.0) | Percentages. |
| N032 | p5 Table1 BMI≥40 | C509/7111(7.2), U536/7225(7.4) | Percentages; five BMI categories sum7111/7225. |
| N033 | p5 Table1 severe respiratory disease | C171/7310(2.3), U172/7436(2.3) | Percentages; shortness of breath light activity, evident within6mo. |
| N034 | p5 Table1 prior hospital stay | C1(1-3)[7293], U1(1-3)[7419] d | Median/IQR and available n. |
| N035 | p5 Table1 prior invasive ventilation; p4 narrative | C5(2-8)[8230], U5(2-8)[8204] h | Median/IQR; calculated critical care admission; narrative time to randomization. |
| N036 | p5 Table1 diagnosis sepsis | C2738/8230(33.3), U2705/8204(33.0) | Percentage; hierarchical mutually exclusive strata, sepsis lower priority than HIE. |
| N037 | p5 Table1 diagnosis HIE | C754/8230(9.2), U750/8204(9.1) | Percentage. |
| N038 | p5 Table1 diagnosis brain injury except HIE | C183/8230(2.2), U180/8204(2.2) | Percentage. |
| N039 | p5 Table1 diagnosis none | C4555/8230(55.3), U4569/8204(55.7) | Percentage; four strata sum8230/8204. |
| N040 | p5 Table1 COVID | C536/8230(6.5), U563/8204(6.9) | Percentage; not exclusive diagnostic stratum. |
| N041 | p5 Table1 SpO2 median; p4 narrative | C97(94-99)[8230], U96(94-99)[8204]% | Median/IQR and saturation unit. |
| N042 | p5 Table1 SpO2<88 | C138/8230(1.7), U146/8204(1.8) | Baseline saturation category percentage. |
| N043 | p5 Table1 SpO288-92 | C995/8230(12.1), U1085/8204(13.2) | Baseline category percentage. |
| N044 | p5 Table1 SpO293-95 | C1979/8230(24.0), U1913/8204(23.3) | Baseline category percentage. |
| N045 | p5 Table1 SpO2>95 | C5118/8230(62.2), U5060/8204(61.7) | Percentage; categories sum8230/8204. |
| N046 | p5 Table1 FiO2 | C.45(.35-.60)[8230], U.45(.35-.60)[8204] | Median/IQR; fraction rather than percentage display. |
| N047 | p5 Table1 PaO2 | C90(75-116)[7638], U89(74-114)[7620]mm Hg | Median/IQR; conversion to kPa multiply .133, also ratio conversion. |
| N048 | p5 Table1 PaO2:FiO2≤100 | C933/7638(12.2), U936/7620(12.3) | Baseline ratio categories mm Hg/fraction. |
| N049 | p5 Table1 ratio>100 to≤200 | C2635/7638(34.5), U2664/7620(35.0) | Percentage. |
| N050 | p5 Table1 ratio>200 to≤300 | C1978/7638(25.9), U1977/7620(25.9) | Percentage; OCR <300 resolved as ≤300 by image. |
| N051 | p5 Table1 ratio>300 | C2092/7638(27.4), U2043/7620(26.8) | Percentage; categories sum7638/7620. |
| N052 | p5 Table1 ICNARC H-2023 | C.35(.29)[6882], U.34(.29)[7014], mean(SD) predicted death | First24h physiology excluding PaO2/FiO2 plus age/history/dependency/CPR/ventilation/source/reason. |
| N053 | p5 Table1 APACHEII | C16(12-21)[7317], U16(12-21)[7437], median(IQR) | Scale0-71, higher more severe; first24h physiology except PaO2/FiO2, age/prior health. |
| N054 | p6 exposure FiO2 | Mean(SD) of participant median C.31(.14), U.35(.15) | Participant-level median then mean; not overall hourly median; eTable5/Figure2 link. |
| N055 | p6 exposure oxygenation | Mean(SD) median SpO2 C93.3(2.8)%, U95.1(2.4)% and median PaO2 C71.5(13.9), U79.5(17.9)mm Hg | Unit distinction despite adjacent mm Hg after SpO2 wording; eTable5 counterparts. |
| N056 | p6 target-range exposure | Mean(SD) hours SpO288-92 C62.6(62.3), U27.2(39.1) |10d enhanced data; does not require supplemental oxygen per Figure2 footnote. |
| N057 | p6 exposure no supplemental oxygen | Mean(SD) hours above target without supplemental oxygen C39.7(55.1), U26.1(45.1) | Category matched to Figure2B >92 without oxygen. |
| N058 | p6 exposure hypoxemia | Mean(SD) hours SpO2<88 C3.2(6.5), U2.3(7.3) | Figure2B category; 10d enhanced sampling. |
| N059 | p6 adherence; p9 limitations | C526(42.1%) with≥1 nonadherence periods; 10.6% ICU time; total2271 periods≥3h | EnhancedC1252 denominator; time denominator not printed in main, not participant fraction. |
| N060 | p6 adherence reasons |857 staffing/lack awareness +413 other priority +127 lowPaO2 +265 unsupported clinical suspension +609 undocumented | Sum to2271; periods not people. |
| N061 | p6 adverse events | C58(.7%), U29(.4%) serious events reported participants | Full analyzed group comparator n8230/8204 source context; eTable9 anchor; not enhanced-only denominator. |
| N062 | p7 Figure2A FiO2 contributors | days0,2,4,6,8,10:U1237,1011,801,639,501,403; C1252,1012,777,609,499,400 | MeanFiO2 axis.2-.6; oxygen-exposure curve C lower U; declining contributor counts. |
| N063 | p7 Figure2A SpO2 with oxygen contributors | days0,2,4,6,8,10:U1237,837,637,500,378,287; C1252,647,493,386,313,240 | MeanSpO2 with oxygen axis88-100%; differing contributors from all FiO2 data expected subset. |
| N064 | p7 Figure2B | Five categories >92 without oxygen; >95 with oxygen; 93-95 with oxygen; 88-92; <88; proportion0-100%; time0-10d | C counts1252,1012,777,609,499,400; U1237,1011,801,639,501,403; 88-92/<88 regardless oxygen. No exact curve ordinates printed. |
| N065 | p7 Figure2C | Cumulative100%-equivalent h axis0-30; time0-10d; U aboveC throughout | Contributors as N062; matches20.3/28.7 endpoint narrative without invented curve digitization. |
| N066 | p8 Table2 ICU stay | OverallC6.6(3.1-13.3)[7333], U6.8(3.1-13.8)[7448]; survivorsC7.3(3.6-14.9)[5211], U7.7(3.8-15.3)[5290]; nonsurvivorsC4.9(1.7-10.4)[2122], U4.6(1.7-9.8)[2158]d | Median/IQR; survivor+nonsurvivor n sums; duration n may differ from mortality availability. |
| N067 | p8 Table2 acute hospital stay; p6 narrative | OverallC14(7-30)[7323], U14(7-31)[7434]; survivorsC20(11-40)[4791], U21(10-42)[4906]; nonsurvivorsC7(3-14)[2532], U7(3-13)[2528]d | Median/IQR; n sums; narrative survivor match. |
| N068 | p8 Table2 organ-support-free days | C16(−1-25)[7327], U16(−1-25)[7444]d; survivor componentsC23(16-26)[4933], U23(15-26)[5054]d | Composite death≤30d score−1; calendar day1-30 including randomization; respiratory/cardiovascular/renal support on any part of day. |
| N069 | p8 Table2 30d mortality | C2435/7449(32.7), U2427/7573(32.0) | Components of composite differ available n; count/percentage. |
| N070 | p8 Table2 ICU mortality | C2122/7334(28.9), U2161/7453(29.0) | Censor90d; compare count to duration-specific n only after outcome availability matching. |
| N071 | p8 Table2 acute hospital mortality | C2533/7335(34.5), U2535/7458(34.0) | Censor90d; per-arm percentages. |
| N072 | p8 Table2 60d mortality | C2637/7449(35.4), U2617/7573(34.6) | Per-arm percentages; secondary linkage consent population. |
| N073 | p8 Table2 1y mortality | C2295/5636(40.7), U2314/5755(40.2) | Per-arm percentages; available one-year outcomes differ from reached-follow-up13052. |
| N074 | p9 Figure3 HIE | C437/754(58.0), U438/748(58.6) | Observed90d subgroup denominators, compare baseline after missing outcomes. |
| N075 | p9 Figure3 sepsis | C1010/2734(36.9), U986/2699(36.5) | Per-arm percentages. |
| N076 | p9 Figure3 brain injury exceptHIE | C78/183(42.6), U83/179(46.4) | Per-arm percentages. |
| N077 | p9 Figure3 no prespecified diagnostic subgroup | C1383/4540(30.5), U1351/4557(29.6) | Four diagnosis rows sum total90d deaths2908/2858 and denominators8211/8183. |
| N078 | p9 Figure3 COVID no | C2665/7677(34.7), U2577/7623(33.8) | Percentages and complement N079. |
| N079 | p9 Figure3 COVID yes | C243/534(45.5), U281/560(50.2) | yes+no deaths/denominators sum total90d observed; baselineCOVID536/563 includes missing outcomes. |
| N080 | p9 Figure3 ethnic Asian | C98/263(37.3), U90/241(37.3) | Per-arm percentages; ethnicity available subset. |
| N081 | p9 Figure3 ethnic Black | C35/138(25.4), U50/152(32.9) | Percentages. |
| N082 | p9 Figure3 ethnic White | C2236/6070(36.8), U2215/6201(35.7) | Percentages. |
| N083 | p9 Figure3 ethnic Mixed | C12/52(23.1), U15/60(25.0) | Percentages. |
| N084 | p9 Figure3 ethnic Other/not stated | C296/808(36.6), U294/796(36.9) | Percentages; ethnic available rows sum7331/7450 and2677/2664 deaths; no assumption totals equal all analyzed. |
| N085 | p3 sample size | CMP96028(Apr28,2017-Mar2019), RiskII82075(Apr2014-Mar2016); usual90d risk37%; C34.5%; ARR2.5pp; 6%loss; n16500; 90% power; P<.05 | Historical datasets are inputs only; independent power reproduction S002; no raw-data access. |
| N086 | p2 background; p6-p8 discussion | Meta-analysis13trials10632adults; priorUKSpO2~96%; ongoing trial minimumFiO2.3; UK-ROX more participants than all prior combined; separation smaller than other trials | Supplied contextual claims and eTable10 link; external claims not independently searched; not treated as UK-ROX estimates. |
| N087 | p10-p11 end matter | Citations1-25; contributor/funding/investigator disclosures; Supplement3 investigators/Supplement4 sharing referenced, not supplied direct sources | No result-relevant numerical relationship in these units beyond bibliography; no inferred missing supplied units. |
