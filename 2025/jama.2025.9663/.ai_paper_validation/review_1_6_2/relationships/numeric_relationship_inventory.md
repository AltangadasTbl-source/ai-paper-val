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
# Numeric relationships — support scope

Scope DOC-003 REPORT pp1–29; DOC-002 PLAN pp1–28.39 grouped relationships. Every table-group record incorporates all values in the corresponding complete source-page transcription in extraction/support_quantitative_evidence.md; this is a complete row-preserving map, not a table sample. Each displayed row, subgroup denominator and percentage is independently available in that durable evidence. C=conservative,U=usual. Numeric definitions are cross-linked to statistical IDs when necessary. None is a finding or adjudication.

| ID | Role/source location | Complete mapped quantity and relationship | Matching main-paper key / checks enabled |
|---|---|---|---|
| N1001 | REPORT DOC-003p1 | Contents lists eTables1/2 as qualityassessment/serology and eTable3sites/eTable4characteristics; actual pages15–20 have site1,additional2,representative3,datacollection4 | Caption/content attribution, no changed number inferred |
| N1002 | REPORT DOC-003p2 | Exposure mean(SD),median(IQR),mean differences95%CI;100%-equivalenth,1hour100%=2hours60.5%; roomairzero; target88–92%,below88%,above92%; first10days,≥3hourfailure | Treatment separation/adherence; Table2 oxygen exposure |
| N1003 | REPORT DOC-003p5 | Declinedconsent minimal90day survival only, no secondary outcomes | CONSORT denominator/populations |
| N1004 | REPORT DOC-003p8 | eFigure1 sites axis0–100,patientrecruitment0–18000,May2021–Nov2024; no printed monthly cell values | Enrollment16500/sites97 |
| N1005 | REPORT DOC-003p9 | N2489;7frequencycurves overall/oxygenonly; SpO2/SaO280–100%,PaO20–200mmHg,FiO2.21–1; ypercentage;mmHg×.133=kPa | Oxygen exposure distributions |
| N1006 | REPORT DOC-003p10 | Full6panel contributor vectors days0,2,4,6,8,10: SpO2 U1237,1011,801,639,501,403/C1252,1012,777,609,499,400; oxygenonly U1237,837,637,500,378,287/C1252,647,493,386,313,240; SaO2 U1037,900,710,568,444,361/C1070,918,714,558,460,371; oxygenonly U1037,745,563,449,336,254/C1070,586,451,353,291,222; PaO2 U1156,1009,800,638,500,403/C1171,1007,775,609,499,400; oxygenonly U1156,836,636,499,377,287/C1171,645,493,386,313,240 | Time-specificcontributors distinguished from total enhancedN2489 |
| N1007 | REPORT DOC-003p11 | eFigure4 N2489;mean95%CI(patientmedian),first10days,dateMay2021–May2024,sitepatientsequence1–500;FiO2.21–.4,SpO290–98%; no printed points | Exposure separation over calendar/patientsequence |
| N1008 | REPORT DOC-003p12 | eFigure5 risk0/90/180/270/360:C7067/4544/4126/3767/3371,U7178/4669/4231/3855/3479;intervaleventsC2523/137/81/59,U2509/131/86/71;removed66=C28+U38;342(2.1%) interval/leftcensored;reverseKM followupC365(277–365),U365(292–365)days | Mortality90day/1year populations/censoring |
| N1009 | REPORT DOC-003p13 | eFigure6 C7327/U7444;death−1,free days0–29;CDF0–1 and stacked0–1 | Daysalive/organfree30day |
| N1010 | REPORT DOC-003p14 | All13 eFigure7 rows retained in clarified table;C/Ucountspercent,RD95%CI,OR95%CI;interactionPs.18,.98,.36,.18,.03 | Posthoc subgroup mortality90day; population and adjustedcontrast |
| N1011 | REPORT DOC-003pp15,16 | eTable1 every97 site count retained;Sunderland863 throughWalton1,total16500; all named site counts in full transcription | Totalrandomized/sites |
| N1012 | REPORT DOC-003p17 | eTable2 all baseline rows C8230/U8204;age mean58(16) both;age7binscountspercent;body-system9bins denominator7286/7405;priorhospital3.3(8.1)[7293]/3.3(7.7)[7419]d;priorMV5.3(3.5)[8230]/5.3(3.5)[8204]h;SpO296.0(3.5)/95.9(3.7);FiO2.51(.21)both;PaO2104(48)[7638]/103(48)[7620];riskmedian.27(.09–.56)[6882]/.26(.09–.55)[7014];APACHE16.9(6.5)[7317]/16.9(6.7)[7437]; all rows/footnotes retained | Table1 additionalbaseline; within-display counts |
| N1013 | REPORT DOC-003p18 | eTable3 every trial16500/CMP207857 row retained:age,sex,ethnic5bins,deprivation5bins,BMI5bins,respiratory343/14746(2.3)/4401/206153(2.1),pregnant98/4473(2.2)/2584/63653(4.1),risk.34(.29)[13896]/.34(.31)[206957],APACHE16(12–21)[14754]/15(11–21)[200385]; complete printed denominators/percents in transcription | Representativeness,within-display quantities |
| N1014 | REPORT DOC-003pp19,20 | All eTable4 cells first10N952/random1537/standard13945;7agebins,2sex,5ethnic,5BMI,9bodysystems,4diagnosticgroups,COVID,4SpO2bins,4PaO2/FiO2bins;allcontinuousmedianIQR/meanSD/No and footnotes retained. Diagnosticlabels printedsepsis364/513/4566,HIE66/160/1278,brain19/23/321,none503/841/7780;label association preserved exactly | Data collection group totals2489+13945=16434; Table1 stratificationkeys |
| N1015 | REPORT DOC-003p21 | All13eTable5 rows C1252/U1237 with variable-specific1248/1230,etc; all meanSD/medianIQR and differences95%CI retained; dose20.3(27.4)[1234]/28.7(31.9)[1216],difference−8.4(−10.8,−6.0),percent−29.3(−37.6,−20.9) | Table2 oxygen exposure; C−Umeancontrast |
| N1016 | REPORT DOC-003pp22,23 | All eTable6 cells for first10C486/U466 and randomC766/U771,13exposurekeys+relative dose; all meanSD/medianIQR/denominators/95%CI retained | Exposuregroup partition:486+766=1252,466+771=1237;meanweightedcomparisons |
| N1017 | REPORT DOC-003p24 | Missingcountpercent:PaO2/FiO21176(7.2),ethnic1630(9.9),primary40(.2),ICUstay1653(10.1),hospitalstay1677(10.2),organfree1639(10.0),ICUdeath1647(10.0),hospitaldeath1641(10.0),60day1412(8.6),1year1661(12.7)/reached13052; allotherbaseline0(.0) | Missingness denominators16434 except1year13052 |
| N1018 | REPORT DOC-003p25 | All eTable8 meanSD/No and survivor-specificmediansIQR retained:ICUoverall11.0(13.0)[7333]/11.4(13.8)[7448],survivor5211/5290,nonsurvivor2122/2158;hospital22.9(23.1)[7323]/23.1(23.3)[7434],survivor4791/4906,nonsurvivor2532/2528;organfree12.9(12.2)[7327]/12.8(12.1)[7444];surviving4933/5054;all3organ-specific summaries | Secondarycontinuous outcomes; subsetweightedmeans/death−1 |
| N1019 | REPORT DOC-003p26 | eTable9 all14specified/other event rows with eventNo/patientNo(percent) retained;any58(.7)/29(.4) patients,C8230/U8204;AF16events14patients vs15/13;supraventricular12/12vs8/8;myocardial19/19vs11/11;mesenteric7/7vs0;eventsoverlap notsumofunique people | Safety results/denominator |
| N1020 | REPORT DOC-003p27 | eTable10 all7trials/allcharacteristics/targets/achievedmeasurements/differences retained;UKROX16434,MV16434,target90%(88–92%),usualcare,achievedSpO293.3/95.2,difference2%;PaO271.5/79.5,difference8.0;FiO2.31/.35,difference.04;footnote mixed mean/median/timeweightedestimated definitions | Separation values, heterogeneousmetric caveat |
| N1021 | PLAN DOC-002pp1–3 | Original/finalprotocol,SAP,changes;v1.1dated14December2020 | Versionmatching, no prospective amendments inferred |
| N1022 | PLAN DOC-002p7 | Adult≥18,FiO2>.21,priorrandomization90dayexcluded,ECMOexcluded;twoarms | Eligibility |
| N1023 | PLAN DOC-002p8 | Target16500;90dayprimary;secondaryICU/hospitaldeath,60day,1year,ICU/hospitalstay90day,EQ5D5L90day;economiccost,QALY,NMB90day | Outcomehierarchy |
| N1024 | PLAN DOC-002p11 | ARRabsolute reduction,RRRrelative,FiO2fraction,SpO2saturation,QALY | Units and measureidentity |
| N1025 | PLAN DOC-002p12 | Historical184000annualICU,>30%(55000)MV;12ICUs,7dayABGs;metaRR1.21(1.03–1.43),OR1.22(1.12–1.33),ICUROX1000 | Background distinct from current sampleinputs |
| N1026 | PLAN DOC-002p13 | Historical4RCTs1983,RR.91(.75–1.09),ARDS205;337312admissions,96028(29%)MV,34%hospitaldeath,anticipated37%90day;current16500 | Sampleinputs locator for other shard; historical values not trialresults |
| N1027 | PLAN DOC-002p14 |16500=41%MegaROX intended;90%power,ARR2.5%90day;feasibilitytarget60/recruited34,SpO288–92%vs≥96% | Plannedpower/target intervention distinguished feasibility |
| N1028 | PLAN DOC-002p15 |100ICUs;secondary60day,1year,HrQoL90day,stay90day | Prospectiveendpoints/site administration |
| N1029 | PLAN DOC-002p16 |Adult≥18,MVcriteria,FiO2>.21,eligible≤12hourwindow,priortrial90day/ECMO/clinician exclusion | Analysispopulationeligibility |
| N1030 | PLAN DOC-002p17 |1:1 randomizationcentralvariableblocks;site,HIE,sepsis,brainexceptHIEstrata | Randomizationunit/strata |
| N1031 | PLAN DOC-002p20 |Originaltarget90–93%,lowestoxygenat/justabove90%;dataretentionbeforewithdrawal | Interventiondefinition/version |
| N1032 | PLAN DOC-002p21 |UpperSpO293%,alarms89/94%,roomair21%;endsICUdischarge/90day,restartsreadmission90day;usualnoupperalarm | Interventionduration/target |
| N1033 | PLAN DOC-002p22 |TerminateinterventionwhenECMO/HBOTstarts;SAEdefinitions | Safetypopulation ascertainment |
| N1034 | PLAN DOC-002p23 |SpecifiedexpectedSAEsuntilICUdischarge/90day,readmissionrestart | Safetywindow |
| N1035 | PLAN DOC-002pp24,25 |UnexpectedoxygenrelatedSAEs,deathnotSAE;24hourreport,15calendarREC;flowchartcorroborates | Outcome/safety distinction |
| N1036 | PLAN DOC-002p26 |Basic14000,enhanced2500(15%),85%routinefields;first10persitethenrandom sampling | Enhancedpopulation versus fieldspercentage |
| N1037 | PLAN DOC-002p27 |Table1 14000/16500,2500/16500;botheligibility/consent/SAE,enhancedcontact/adherence/90dayHrQoL/resource | Prespecifiedcollection/outcomeavailability |
| N1038 | PLAN DOC-002p28 |Pilotmonths7–12includedfinalanalysis;sites>50/20–50/<20,recruit≥75/40–75/<40%anticipated | Progressiondecisionrule |
| N1039 | PLAN DOC-002p28 |PilotSpO2separation≥3/1.5–3/<1.5%ORFiO2≥.1/.05–.09/<.05;adherence≥75/50–75/<50%cases | Plannedseparation/adherence thresholds |

All REPORT table cells and footnotes are retained in full in source-page sections, which remain the transcription authority for grouped entries. PLAN original version numeric values were image-corroborated on every assigned page; potential cross-version matching requires final/amendment scopes owned by other agents.
# Numeric and reporting relationships: plan-b

Scope DOC-002 PLAN physical PDF pages29–56; all28 pages covered in extraction/parts/plan-b.md. 15 distinct N relationships. Source locations below refer to supplied `joi250042supp1_prod_1753377747.92525.pdf`; links resolve relative to this part. Values visually confirmed from every corresponding source-linked page image. These are mapping records, without candidate selection or checker conclusions.

| ID | Exact PLAN location | Printed quantitative relationship and labels | Semantic report matching key / plan correspondence |
|---|---|---|---|
| N2001 | [PDF29](../../../joi250042supp1_prod_1753377747.92525.pdf#page=29), v1.1 outcomes | Clinical primary90-day all-cause mortality; secondary ICU/hospital mortality and ICU/acute-hospital length censored90 days,60-day/one-year mortality,HrQoL EQ-5D-5L90 days; economic primary incremental costs/QALYs/net monetary benefit90 days, economic secondary EQ-5D-5L90 days,resources/costs90 days,lifetime incremental cost-effectiveness | Primary90-day mortality; clinical secondary status/time; economic outcome hierarchy; compare final summary N2011 with version context |
| N2002 | [PDF29](../../../joi250042supp1_prod_1753377747.92525.pdf#page=29), v1.1 §4.1 | CMP96,028 and Risk II82,075 source populations; assumed37%control90-day mortality,34.5%intervention; ARR2.5 percentage points,RRR6.8%;90%power;15,444 total evaluable,6%allowance,16,500 total recruitment | Trial sample-size inputs and planned population; companion S2001; significance/test details not stated on page |
| N2003 | [PDF29](../../../joi250042supp1_prod_1753377747.92525.pdf#page=29), v1.1 §4.1 | Eight patients/unit/month; half eligible median;100 ICUs;two years;6-month staggered opening | Recruitment-feasibility context, not result denominator |
| N2004 | [PDF30](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30), v1.1 §4.2.3 | Detailed inpatient resource/adherence follow-up15%participants; regression predicts resource use for all trial participants;90-day economic horizon | Detailed monitored subset vs full trial and economic analysis population; S2009 |
| N2005 | [PDF31](../../../joi250042supp1_prod_1753377747.92525.pdf#page=31), v1.1 §4.2.3 | HrQoL measured15%at90 days and predicted for all; survivors baseline utility0,linear interpolation to90-day EQ-5D, decedents0QALYs; net benefit values gains£20,000/QALY minus incremental costs;mean95%CI90-day increments | Economic utility/cost/net-benefit identity; S2010–S2012 |
| N2006 | [PDF39](../../../joi250042supp1_prod_1753377747.92525.pdf#page=39), v1.1 Appendix2 | Conservative oxygen: upper alarm94%,lower89%; if SpO2>93%, reduce FiO2 until SpO2<94%;lowest FiO2 for SpO2=90%;if SpO2<90%,increase until>89%;off supplemental oxygen lower alarm89%and same initiation rule;lower alarm may be reduced if clinically indicated | Conservative target/dose algorithm and deviation footnote; distinct from historical feasibility88%–92%in N2015 |
| N2007 | [PDF40](../../../joi250042supp1_prod_1753377747.92525.pdf#page=40), v1.1 Appendix2 | Usual oxygen: no upper SpO2alarm;lower89%, reducible if clinically indicated | Usual-treatment intervention definition; compare conservative arm N2006 |
| N2008 | [PDF41](../../../joi250042supp1_prod_1753377747.92525.pdf#page=41), v1.1 Appendix3 | Expected SAEs after randomization until critical-care discharge:sinus/supraventricular tachycardia,atrial fibrillation,myocardial ischaemia/infarction,mesenteric ischaemia | Safety ascertainment window and expected-event classification |
| N2009 | [PDF47](../../../joi250042supp1_prod_1753377747.92525.pdf#page=47), summary; [PDF48](../../../joi250042supp1_prod_1753377747.92525.pdf#page=48), summary continuation; [PDF56](../../../joi250042supp1_prod_1753377747.92525.pdf#page=56), v1.8 §3.3 | Age≥18;invasive MV after unplanned ICU admission OR initiated in ICU;FiO2>0.21 at enrolment;prior randomization last90 days/current ECMO/clinically indicated or contraindicated arm excluded;12-hour eligibility-to-enrolment window explicitly in §3.3 | Eligibility and repeat-randomization analysis unit; summary/body correspondence; S2017 |
| N2010 | [PDF48](../../../joi250042supp1_prod_1753377747.92525.pdf#page=48); [PDF53](../../../joi250042supp1_prod_1753377747.92525.pdf#page=53); [PDF54](../../../joi250042supp1_prod_1753377747.92525.pdf#page=54), v1.8 | Recruitment target16,500;standalone90%power for2.5%ARR90-day mortality; planned16,500 contribution to individual-patient meta-analysis | Updated protocol target vs original N2002; current standalone vs pooled analysis S2015 |
| N2011 | [PDF48](../../../joi250042supp1_prod_1753377747.92525.pdf#page=48), v1.8 summary; [PDF54](../../../joi250042supp1_prod_1753377747.92525.pdf#page=54) and [PDF55](../../../joi250042supp1_prod_1753377747.92525.pdf#page=55), objectives | Primary90-day all-cause mortality. Secondary:in-hospital mortality censored90 days;mortality ICU discharge/60 days/one year;ICU/acute-hospital duration censored90 days;days alive/free organ support30 days,death worst ordinal category;support respiratory/cardiovascular/renal CCMDS;EQ-5D-5L90 days. Economic primary costs/QALYs/net benefit90 days;secondary HrQoL/resources/costs90 days,lifetime cost-effectiveness | Full updated endpoint/status hierarchy; original N2001; clinical organ-support-free endpoint S2013 |
| N2012 | [PDF51](../../../joi250042supp1_prod_1753377747.92525.pdf#page=51), v1.8 abbreviations | ARR=absolute risk reduction;RRR=relative risk reduction;FiO2=fractional inspired oxygen concentration;SpO2=peripheral arterial oxygen saturation;QALY=quality-adjusted life year;INB=incremental net benefit | Unit/effect-measure/label identity; CI on this abbreviation page is Chief Investigator, statistical intervals spelled out in local model text |
| N2013 | [PDF52](../../../joi250042supp1_prod_1753377747.92525.pdf#page=52), v1.8 background | Historical184,000 annual UK admissions,>30%(55,000)MV;oxygen21%–100%,historical guidanceSpO2>96%;12ICUs/7-dayABGs/10ARDSstudies;prior meta-analysisRR1.21(95%CI1.03–1.43),OR1.22(1.12–1.33);ICU-ROX1000 | Background context only, not current-trial results, endpoints or intervention targets |
| N2014 | [PDF53](../../../joi250042supp1_prod_1753377747.92525.pdf#page=53), v1.8 background/rationale | Prior ICU-ROXSpO2 91%–96%,ventilator-free days28;four RCTs1983,RR0.91(95%CI0.75–1.09);ARDS205/28-day survival;CMP337,312 admissions,96,028(29%)MV,34%hospital mortality,37%anticipated90-day;>3000 annual lives extrapolated;COVIDMV72% | Background evidence and37%planning-risk provenance; historical estimates distinct from current treatment results |
| N2015 | [PDF54](../../../joi250042supp1_prod_1753377747.92525.pdf#page=54); [PDF55](../../../joi250042supp1_prod_1753377747.92525.pdf#page=55), v1.8 §1.5–3.2 | Historical feasibility target60,two sites,recruited34,SpO2 conservative88%–92%,control≥96%;current routine-data design additional primary collection15%;100NHS ICUs,current patient-level randomized registry-embedded trial | Historical feasibility intervention distinguished from actual UK-ROX algorithm;monitoring subset/full population;individual randomization |

Relationship count15; IDs N2001,N2002,N2003,N2004,N2005,N2006,N2007,N2008,N2009,N2010,N2011,N2012,N2013,N2014,N2015. Administrative/bibliographic-only page numbers and quantities are explicitly covered in extraction but yield no additional result-relevant numeric relationship. No unassigned-source comparison was performed.
# Numeric and reporting relationships: plan-c

Complete disjoint scope DOC-002 PLAN physical PDF pp57–88; 32 mapped pages. Source links in companion extraction map resolve supplied PDF. All rows are inputs for independent checking, not findings. Matching main/report key indicates what to match; no unassigned report page was read.

| Relationship ID | PLAN source location | Printed inputs, units and relationships | Matching result/plan key |
|---|---|---|---|
| N3001 | p57§3.4.1 | 1:1 conservative/usual allocation; variable permuted blocks | Randomisation arms/ratio |
| N3002 | p57§3.4.2 | Randomise/start assigned treatment no later12hours after eligibility | Intervention initiation |
| N3003 | pp58–60 consent | 24–48hours approach after capacity; consultee24–48hours randomisation ideally;14working-day postdischarge contact,≥3calls | Consent/flow context, peripheral timings |
| N3004 | p60§3.4.4;p76§8.5.2 | Retain accrued data unless removal; primary alive/dead90days only for specified refusal/NDOO | Primary denominator/missingness |
| N3005 | p61§3.6.1;p83Appendix2 | Target90±2%; alarms<88%/>92%; oxygen SpO2≤92%; FiO2 reduce toward90% | Conservative treatment target |
| N3006 | p61;p84Appendix2 | At21% oxygen/room air keep exposure, upper alarm off; lower88% | Room-air exception |
| N3007 | pp61–62 | Intervention to ICU discharge or90days sooner; restart ICU readmission within90days; ECMO/HBOT terminates | Treatment duration/exposure |
| N3008 | p61§3.6.2;p85 | Usual care clinician-set target/lower alarm; no upper alarm | Usual oxygen arm |
| N3009 | p64§3.7.3;p65Figure1 | All randomised safety to discharge/90days first, restart readmission;24-hour CTU and15calendar-day REC notification | Safety outcome denominator/window |
| N3010 | p66§3.8;p67Table1 | Basic14,000, enhanced2,500(15%), total16,500;14,000/16,500 and2,500/16,500 | Enhanced adherence/HrQoL sample |
| N3011 | p66 | 85% trial data fields routine; first10/site prospectively, then randomly sampled across site/arm/time | Collection design, field fraction distinct from patient fraction |
| N3012 | p67Table1 | Both columns eligibility/consent/SAE/linkedmortality/linkedresource; only enhanced contact/adherence/EQ5D/resource questionnaire | Sample eligibility for each display |
| N3013 | p68§3.9 | Follow-up90days; questionnaire≤15minutes; nonresponder3weeks after posting; inpatient originalstay no resource questionnaire |90-day patient-reported outcomes |
| N3014 | p68§3.9.1 | SWAT1:1 thank-you/no-card; completion proportion,response time,completeness; current inpatients excluded | Ancillary follow-up experiment |
| N3015 | pp68–70 pilot | Pilotmonths10–15; analysismonth17; included in full trial | Primary population/internal pilot |
| N3016 | p69Table2 | SitesGreen>50,Amber20–50,Red<20 | Pilot decision criterion |
| N3017 | p69Table2 | RecruitmentGreen≥75%,Amber40–75%,Red<40% anticipated per-site/month | Pilot decision criterion |
| N3018 | p69Table2 | SeparationGreenSpO2≥3% ORFiO2≥0.1; Amber(SpO2 1.5–3% ANDFiO2<0.1)OR(SpO2<3% ANDFiO2 0.05–0.09); RedSpO2<1.5% ANDFiO2<0.05 | Pilot decision criterion, exact printed boundary logic |
| N3019 | p69Table2 | AdherenceGreen≥75%,Amber50–75%,Red<50%; ventilator/supplementaloxygen adjustment per protocol | Pilot adherence |
| N3020 | p69§3.10.2 | ClinicalPRIMARY90-day all-cause mortality; economicPRIMARYincremental cost/QALY/NMB90days | Full primary outcome hierarchy |
| N3021 | p69§3.10.2 | ClinicalSECONDARYICU/hospitaldeath censored90days,mortality60days/1year,ICU/hospitalstay censored90days,ordinal organ-support-free30days deathworst,EQ5D90days | Full clinical secondary hierarchy |
| N3022 | p69§3.10.2 | EconomicSECONDARYEQ5D90days,resourcecost90days,lifetimeincrementalcosteffectiveness | Economic hierarchy |
| N3023 | p70§4.1 | HistoricCMP96,028/RiskII82,075;90daybaseline37%,intervention34.5%,ARR2.5percentagepoints,RRR6.8% | Sample size effect assumption |
| N3024 | p70§4.1 | 90%power,total15,444;6%refusal/withdrawal/loss;target16,500 | Sample size and inflation |
| N3025 | p70§4.1 | 8patients/unit/month,100ICUs,2years,6-monthstagger | Recruitment feasibility, peripheral except population/decision relevance |
| N3026 | pp71,73 | Twointerims after4,500 and10,000 recruitment/followup90days;P<0.001 | Interim/stopping specification |
| N3027 | p71§4.2.3 | CEA15%sample;90dayhorizon;NMB£20,000/QALY×incrementalQALYs−incrementalcost | Economic model units |
| N3028 | p71§4.2.3 | Survivorutility0atbaseline,linear90day interpolation;decedents0QALYs;mean95%CIs | QALY definition and CEA intervals |
| N3029 | pp81,82,87 | v1.1Dec2020;v1.2Mar2021 oxygen90–93→90±2,pilot7→10;v1.8Oct2024 addsSECONDARYordinal30dayorgan-support-free | Disclosed amendment timing/status |
| N3030 | p88cover | SAPv1.0 references protocolv1.5(12Apr2022) | Supplied plan version identity |

No count/estimate/test results occur in this prospective shard; historic power inputs retained as supplied. References pp78–80 and administrative-only paragraphs have no additional result-relevant relationship. All units explicitly recorded in companion evidence map.
# Numeric and definition relationships: PLAN DOC-002 pp89–120

Independent source-image readings. All rows are PLAN. Locations are physical PDF pages of joi250042supp1_prod_1753377747.92525.pdf; evidence URLs from this part are ../../../joi250042supp1_prod_1753377747.92525.pdf#page=N. Match keys are outcome/population/contrast/time/model descriptors for merging, not scientific conclusions. No candidate judgments are made. OCR gaps are resolved visually in all numerical rows. Scope includes all administrative/reference pages as explicitly recorded in extraction/parts/plan-d.md.

| ID | Exact locations | Printed quantitative relationship, label, unit and context | Matching key / linked statistical record |
|---|---|---|---|
| N4001 | p90 version history | SAP v1.0, 07/11/2022; first complete SAP before first-interim data lock. | Original SAP timing |
| N4002 | pp93–94 objectives; pp116–117 | Primary clinical90-day all-cause mortality; primary economic90-day NMB from incremental costs/QALYs; other objectives ICU/hospital mortality censored90 days, 60-day/one-year mortality, ICU/hospital stay censored90 days, HrQoL90 days, lifetime NMB. Original pp93–94 do not list organ-support-free days; final p117 does. | Endpoint hierarchy; S4001 |
| N4003 | p94 §§2.1–2.2; p117 | Patient randomization1:1; conservative SpO2 target90%(±2%) versus usual oxygen; variable permuted blocks, site and four mutually exclusive strata HIE, sepsis, acute brain injury excludingHIE, none. Hierarchy HIE>sepsis>acute brain injury; COVID not stratification. | Allocation/intervention; S4002 |
| N4004 | p94 §2.3; p117 | Anticipated90-day mortality37%; absolute reduction2.5 percentage points to34.5%; stated relative reduction6.8%; power90%, alpha5%; total required15, 444; allowance6% refusal/withdrawal/loss; recruit16, 500. Historical supporting datasetsCMP N96, 028 andRiskII N82, 075. | Sample-size inputs; S4003 |
| N4005 | p94 §2.3–2.4; p117 | Recruitment8 patients/unit/month, 100 ICUs, two years, opening over6 months; all outcomes superiority. Recruitment premises are administrative contextual quantities. | Recruitment/superiority; S4004 |
| N4006 | p95 Table1; p118 | Green/amber/red sites>50/20–50/<20; recruitment≥75%/40–75%/<40% anticipated per site/month; pilot months10–15, analysis month17. | Pilot progression |
| N4007 | p95 Table1; p118 | Green separation SpO2≥3% OR FiO2≥0.1; amber(SpO2 1.5–3% AND FiO2<0.1)OR(SpO2<3% AND FiO2 0.05–0.09); redSpO2<1.5% AND FiO2<0.05. Separation is group difference of median of each patient's median. | Pilot separation; S4005 |
| N4008 | p95 Table1; p118 | Green adherence≥75%cases; amber50–75%; red<50%. Footnote defines percentage as conservative-group patients with one or more adjudicated protocol deviation. | Pilot adherence definition; S4005 |
| N4009 | p95 footnote; p118 | Deviation while oxygen: failure to reduce FiO2 if>21% whenSpO2>92% for≥3 hours; 22%or23% treated21% for deviation only. Pilot enrolled participants included main trial. | Adherence/pilot population; S4005, S4009 |
| N4010 | p96 §§2.6–2.7; p119 | Two interim analyses after4, 500 and10, 000 complete90-day follow-up/linked outcome; Peto–Haybittle P<0.001 effectiveness or harm; no futility/conditional power; extra analyses ifDMEC requests. Trial ends all90 day follow-up; CMP linkagewithin30 days, reextractwithin15 days afterdeath-link receipt; censor beyond90 days. | Interim/decision; S4006 |
| N4011 | p96 §2.8; p119 | Enhanced sample2, 500(15%):first10/site≈1, 000 plusrandomsubsequent≈1, 500; subsequent probability10%, blocksize10 by site/treatment. Hourly respiratory type/SpO2/FiO2/PaO2/SaO2 day0anddays1–10 whileICU; surviving consenting sample receivesEQ-5D-5L/resource questionnaire90 days. | Enhanced-data sample/time; S4007 |
| N4012 | p97 §3.1; p120 | Two-sided P<0.05 unless otherwise specified; effect95%CIs; no multiple-testing adjustment; subgroup interpretation uses credibility criteria. | Inferential levels; S4008 |
| N4013 | p97 §3.2; p120 §3.2 | Group mean(SD), median(IQR) of each patient's medianSpO2/FiO2 overall/onoxygen; differences95%CIs. Time within90±2%,>92%,<88% mean(SD)/median(IQR). Originalp97 respiratorysupport totalhours randomization toendday10 by type/overall withmean-difference95%CI; final p120 replaces this displayed bullet with totaloxygen dose. Hourlyplotsdays1–10 withcountsatfoot forSpO2, FiO2, SaO2, PaO2. | Exposure/descriptors; S4009 |
| N4014 | p98 §§3.2.2–3.3 | Adherence patient-level no protocol deviation; reportconservative-group n/%≥1deviation andadjudicated eventsnotdeviations. ITT assignment regardlesstarget/adherence; knownprimary outcomeincluded; repeat randomizationallowed≥90 days afterprior, may appear multiple times. | Population/adherence; S4010 |
| N4015 | p98 §§4.1–4.2 | Flow n assessed, eligible, ineligiblewithreasons, randomized, eligible-not-randomized; detailed n/% inclusionfailure amongscreened, exclusion amonginclusion-eligible, notrandomized amongeligible. Adult≥18, enrollwithin12 hoursofeligibility. | Flowdenominators/eligibility |
| N4016 | p99 §§4.2–4.4 | FiO2>0.21 at enrollment; unplannedICUadmission/invasiveMVstartedICU; exclude priorrandomizationlast90 days, currentECMO, clinician armindication/contraindication. Flowlost/included/excludedprimary. Mortality/stay include availableoutcomes despite consentunavailable/refusalunlesscomplete withdrawal. | Eligibility/primarypopulation; S4011 |
| N4017 | p100 §§4.4–4.6 | Completewithdrawals summarized/excluded; questionnaireloss percentage denominator90-daysurvivors enhancedsubset; numeratorincludes trueunavailable, withdrawn, no questionnaire consent. Comparequestionnairecompleters withenhanced noncompletingsurvivors andallsurvivors. Baselines summarizedwithouttests. | Follow-up/population; S4012–S4013 |
| N4018 | p101 §4.6 | Age mean SD/median IQR, n/%18–29, 30–39, 40–49, 50–59, 60–69, 70–79, 80+; sexmale/female, ethnicityWhite/Mixed/Asian/Black/Other n%; BMI<18.5, 18.5–<25, 25–<30, 30–<40,≥40; severerespiratorydisease, priorhospital/MVduration; strata, COVIDn%; SpO2/FiO2/PaO2mean SD/median IQR; PFcategories<100, 100–<200,≥200mmHg; ICNARCpredictedrisk/APACHEIImean SD/median IQR. | Baseline definitions; S4013 |
| N4019 | p101 §5.1 | Primarydeathanycauseby90 daysafterrandomization. Interimonly acutehospitalmortalitycensored90 days may replace ifdeathlinksubstantially delayed. | Primarydefinition/interimproxy; S4014 |
| N4020 | p102 §§5.2.1–5.2.2 | ICUdeathbefore dischargecare<Level2; acutehospitaldeathbefore dischargeincludingtransferstootheracutehospitals; bothcensored90 days.60 day/oneyeardeathanycausebyrespective times; oneyearanalysis excludespatientswithoutreachingoneyearwhentrialends. | Secondarymortality; S4015 |
| N4021 | p102 §5.2.3 | ICUdurationlinear time randomization to firstdischarge/death plusreadmissionduration sameacutehospitalstay. Hospitalduration calendardays randomization to acutehospital discharge/death. | Lengthofstaydefinition; S4016 |
| N4022 | p102 §5.2.4 | HrQoLEQ-5D-5L90 days, sentonly enhanced-data90-daysurvivors; 2, 500(15%) initiallyselected. | HrQoLpopulation/time; S4017 |
| N4023 | p103 §5.3.1 | Primary adjustedRD frommarginal probabilities; conditional OR andmodeled RRsupplementary.95%CI2.5th/97.5th percentiles 2000 bootstrap samples. Age, SpO2, PF eachrestricted cubic spline3 knots. | Primaryestimand/CI/model; S4018–S4020 |
| N4024 | p104 §§6.1–6.2 | Primaryeconomic NMBincrementalcost/QALY90 days; secondaryHrQoL90 day, resource/cost90 day, lifetimecost/QALY/NMB. | Economicstatus; S4024 |
| N4025 | p105 §6.3 | Resourceandutilitypredictionall patientsfrom15%enhanceddata, survivorquestionnaires; train/testvalidation. Utility5L mapped3LDSU; QALY90 daysAUC, survivorbaselineEQ5D0withlinear interpolationto90 day; decedentsbefore90 dayzeroQALYs. | Utility/QALYdefinition; S4025 |
| N4026 | p105 §6.3 | Incrementalnetbenefit=£20, 000perQALY×QALYgain−incrementalcost; means95%CIsincrementalcost/QALY/netbenefit90 days. | Economicmeasure; S4025 |
| N4027 | p105 §6.3 | SURcorrelatedcosts/QALY; ICC>10% impliesmultilevel SURelse single level; baselineadjustmentsasprimary clinical; all clinical subgroups; acceptabilitycurves/sensitivities. | Economicmodeldecision; S4026 |
| N4028 | p106 §6.3.2 | LifetimesurvivalparametricWeibull/exponential/lognormal/loglogistic/Gompertz; fit/plausibilitygeneralpopulation; afterexcessmortalitygeneralpopulationrates/utilities; 90 dayutilitywithagedecrementduringexcessperiod; 90 daymorbiditycostprojection. | Lifetimeeconomic; S4028 |
| N4029 | p107 §§7–9 |20MICEimputeddatasets, Rubinpooling; SAEsrandomization to ICU discharge/90 dayincludingreadmissions; Fisherpatients≥1event; eventtotals/patientn/%by type/group. Stata/MP16.1orupdate, Rpossible. | Missingness/safety; S4029–S4031 |
| N4030 | p111 cover | SAP v1.1; protocol v1.8 dated14October2024. | Finalplanidentity |
| N4031 | p113 version history | v1.1dated25/11/2024; added30 dayorgan-support-free secondary, heterogeneitysection, expandedmissing data, totaloxygendose, calendar-timeadjustment; beforerecruitmentcompletion, blindedstatisticians. | Disclosedamendment |
| N4032 | p117 objectives | Finaladded30-daydaysalive/freeorgansupport, alongsideotherobjectivesalreadylistedN4002. | Organ-support-freedaysstatus |
| N4033 | p120 §3.2.1 | MeantotalO2dose100%-equivalenthours, roomairzeroextra; 1 hour100%or2 hours60.5% eachoneequivalenthour; cumulatedexposurecurves. Sourceequivalenceimplies excessFiO2 normalization above21%; formula inference T×(FiO2−0.21)/0.79 flaggedasderived, notprinted. | Oxygendose/unitdefinition |
| N4034 | p120 §3.2.1 | Fourpathwaygroups:SpO2>92%roomair; SpO2>92%additionaloxygen; SpO288–92%; SpO2<88%(hypoxaemia). Noformaltests. Additionaloxygen>92%isgroupconservativeprotocolshouldexclude. | Exposurepathwaypopulation |
# Numeric relationship inventory — plan-e

Exactly DOC-002 PLAN physical pages 121–136. Complete visual source-linked reading; provenance and full page map in `extraction/parts/plan-e.md`. Values are planned definitions/inputs, not observed trial results. Companion S records carry inferential logic. Relative evidence links resolve from this part's directory to the supplied PDF.

| ID | Source location (PLAN) | Printed quantitative definition, unit and denominator | Matching key / companion |
|---|---|---|---|
| N5001 | [p121](../../../joi250042supp1_prod_1753377747.92525.pdf#page=121), deviation continuation | FiO2 22% or 23% treated as 21% for deviation identification only, not other comparisons; report number of queried events determined not deviations | Protocol deviation/oxygen exposure; S5001 |
| N5002 | [p121](../../../joi250042supp1_prod_1753377747.92525.pdf#page=121), §3.3 | Repeat randomization ≥90 days after previous, if eligible again; patients can enter analysis multiple times | Analysis unit/ITT; S5002 |
| N5003 | [p121](../../../joi250042supp1_prod_1753377747.92525.pdf#page=121), §4.1 | Flow counts screened/eligible/ineligible/randomized/not randomized; exclusion percentages among inclusion-eligible; nonrandomization percentages among fully eligible | CONSORT denominators; S5003 |
| N5004 | [p121](../../../joi250042supp1_prod_1753377747.92525.pdf#page=121)–[p122](../../../joi250042supp1_prod_1753377747.92525.pdf#page=122), §4.2 | Age ≥18 years; enrolled ≤12 hours after eligibility; supplemental oxygen FiO2 >0.21; exclude randomization within past 90 days | Inclusion/exclusion and recruitment; S5003 |
| N5005 | [p122](../../../joi250042supp1_prod_1753377747.92525.pdf#page=122)–[p123](../../../joi250042supp1_prod_1753377747.92525.pdf#page=123), §§4.3–4.5 | Primary included/excluded/lost counts; complete withdrawals counted by group but excluded from analysis; refusal/withdrawal counts and % by group | Analysis denominator/consent; S5004–S5005 |
| N5006 | [p123](../../../joi250042supp1_prod_1753377747.92525.pdf#page=123), §4.5 | Questionnaire loss at 90 days as % of enhanced-subset survivors; loss includes unavailable data, withdrawal, and no questionnaire consent; mortality loss % by group | Follow-up denominator; S5005 |
| N5007 | [p124](../../../joi250042supp1_prod_1753377747.92525.pdf#page=124), §4.6 | Age mean(SD), median(IQR), categories 18–29,30–39,40–49,50–59,60–69,70–79,80+; sex/ethnicity n(%) | Baseline demographics; S5006 |
| N5008 | [p124](../../../joi250042supp1_prod_1753377747.92525.pdf#page=124), §4.6 | BMI categories <18.5,18.5–<25,25–<30,30–<40,≥40; prior hospital duration and invasive MV duration since critical-care admission | Baseline medical history; S5006 |
| N5009 | [p124](../../../joi250042supp1_prod_1753377747.92525.pdf#page=124), §4.6 | SpO2,FiO2,PaO2 mean(SD)/median(IQR); PaO2/FiO2 categories <100,100–<200,≥200 mmHg; ICNARC/APACHE II first 24 hours | Baseline physiology/severity; S5007 |
| N5010 | [p124](../../../joi250042supp1_prod_1753377747.92525.pdf#page=124)–[p125](../../../joi250042supp1_prod_1753377747.92525.pdf#page=125), §§5.1–5.2.1 | Primary all-cause mortality by 90 days; ICU/hospital mortality censored day 90; ICU discharge to below Level2 | Primary/secondary mortality; S5008–S5010 |
| N5011 | [p125](../../../joi250042supp1_prod_1753377747.92525.pdf#page=125), §5.2.2 | Secondary all-cause mortality by 60 days and one year; trial ends last patient's day 90, exclude participants not reaching one year | Secondary mortality horizon; S5011 |
| N5012 | [p125](../../../joi250042supp1_prod_1753377747.92525.pdf#page=125), §5.2.3 | ICU duration linear time randomization to discharge/death plus subsequent same-hospital-stay ICU admissions; hospital duration calendar days randomization to discharge/death | Length-of-stay unit; S5012 |
| N5013 | [p125](../../../joi250042supp1_prod_1753377747.92525.pdf#page=125)–[p126](../../../joi250042supp1_prod_1753377747.92525.pdf#page=126), §5.2.4 | Organ-support composite day1=randomization day through day30; death ≤30 score −1; survivor free days from calendar-day respiratory/cardiovascular/renal support; outside ICU free; CMPv3.1 total support=max(three support-day totals), cap30 | Organ-support-free composite; S5013–S5014 |
| N5014 | [p126](../../../joi250042supp1_prod_1753377747.92525.pdf#page=126), §5.2.5 | EQ-5D-5L at day 90 in enhanced-subset survivors; enhanced target 2500 (15%) | HRQoL collection population; S5015 |
| N5015 | [p126](../../../joi250042supp1_prod_1753377747.92525.pdf#page=126), §5.3.1 | Age/SpO2/PaO2:FiO2 restricted cubic splines 3 knots each; randomization calendar 2-week periods, spline7 knots | Primary adjustment; S5016 |
| N5016 | [p127](../../../joi250042supp1_prod_1753377747.92525.pdf#page=127), §5.3.1 continuation | 2000 bootstrap samples; confidence limits 2.5th and97.5th percentiles; RD difference in whole-cohort marginal risks | Primary RD95% CI; S5018–S5019 |
| N5017 | [p127](../../../joi250042supp1_prod_1753377747.92525.pdf#page=127), §5.3.2 | Four mutually exclusive diagnostic strata; COVID yes/no; ethnicity; joint interaction test for >2 categories | Confirmatory subgroup; S5020–S5022 |
| N5018 | [p127](../../../joi250042supp1_prod_1753377747.92525.pdf#page=127)–[p128](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128), §5.3.3 | Initial causal forest50,000 trees; retain importance >0.2×mean importance; half data identify subgroup, remaining half estimate | Exploratory HTE; S5023–S5025 |
| N5019 | [p128](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128), §5.3.4 | Mortality n(%); stay/support-free mean(SD)/median(IQR), overall and by discharge survival status | Secondary display labels; S5026–S5028 |
| N5020 | [p128](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128)–[p129](../../../joi250042supp1_prod_1753377747.92525.pdf#page=129), §§6.1–6.2 | Primary economic NMB at90 days; secondary HRQoL,resource/cost at90 days and lifetime cost/QALY/NMB | Economic endpoint hierarchy; S5029 |
| N5021 | [p129](../../../joi250042supp1_prod_1753377747.92525.pdf#page=129), §6.3 | Enhanced random15% for questionnaires; EQ-5D utility0 at randomization; linear interpolation to day 90; deaths through90 assigned zeroQALY | HRQoL/QALY derivation; S5030–S5032 |
| N5022 | [p130](../../../joi250042supp1_prod_1753377747.92525.pdf#page=130), §6.3 | Incremental NMB=£20,000 perQALY×incremental QALY−incremental cost; incremental means95%CIs at90 days | Economic effect/unit; S5033 |
| N5023 | [p130](../../../joi250042supp1_prod_1753377747.92525.pdf#page=130), §6.3 | ICC>10% multilevelSUR; ICC≤10% single-levelSUR | Economic clustering decision; S5034 |
| N5024 | [p131](../../../joi250042supp1_prod_1753377747.92525.pdf#page=131), §7 | Missing FiO2 imputed0.21 when respiratory support none; recorded>0.21 queried; interval-missing exposure carried forward | Oxygen exposure missingness; S5040 |
| N5025 | [p132](../../../joi250042supp1_prod_1753377747.92525.pdf#page=132), §7 continuation | Twenty MICE datasets; computational alternative five imputed datasets and1000 bootstrap replications | Outcome missingness/uncertainty; S5041–S5043 |
| N5026 | [p132](../../../joi250042supp1_prod_1753377747.92525.pdf#page=132), §8 | SAE ≥1 patient count/% versus event counts; all randomized inICU randomization through90 days including readmissions; comparison until discharge/day 90 | Safety denominators/window; S5044 |
| N5027 | [p132](../../../joi250042supp1_prod_1753377747.92525.pdf#page=132), §9 | Stata/MP17.0 or later; R/other packages for specific analyses | Software definition; S5045 |
| N5028 | [p136](../../../joi250042supp1_prod_1753377747.92525.pdf#page=136), SAP change summary | v1.0 7November2022 before interim lock; v1.1 25November2024 before recruitment completion; five changes, including day30 organ-support secondary and calendar adjustment | Explicit amendment chronology; S5046–S5047 |

Count: 28 numeric records. Every numeric-bearing assigned page is represented; pp133–135 references do not introduce independent trial numeric inputs. No fresh OCR/native derivatives were required after full visual reading of fresh/reused page images. No calculated results or candidate classifications are embedded here.
