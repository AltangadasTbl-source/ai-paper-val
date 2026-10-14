# Fresh quantitative map: DOC-003, PDF pages 1–35

Scope: every assigned PDF page 1–35 of `joi250084supp2_prod_1765403089.61751.pdf`. Document role: REPORT, based on retrospective methods, results displays and intervention descriptions. This shard contains no prospective protocol/SAP. Source-relative links below use the four-level path from this extraction part to the package root. No earlier candidate, screening, classification, checker or report was read. No scientific diagnosis is made here.

Evidence: curator-listed reusable native/layout text for pp1–33; reusable source-matched rendered images and native captions for pp34–35. Exact full page transcripts are retained below so that every numeric definition, code statement, table label, footer and footnote remains available rather than selected examples. Fresh visual inspection covered images on pp12,32,33 using bundled `pdf_tools.py render` with user-authorized `/home/juliz/venvs/stt/bin/python`, PyMuPDF1.28.0, CPU,200dpi. New derivatives: `.ai_paper_validation/review_1_6_2/preprocessing/results001-p012.png`, `results001-p032.png`, `results001-p033.png`. No fresh OCR. Screenshots are illustrative app/hardware content, not participant outcome values.

## One-page completion ledger

| PDF page | Content and complete mapping status |
|---:|---|
| 1 | COMPLETE: cover/source identity; no applicable quantitative relationship |
| 2 | COMPLETE: contents list and method/result table pointers; no trial value |
| 3 | COMPLETE: contents, eTables3–19; all population/title matching pointers retained |
| 4 | COMPLETE: contents, eTables19–20 and references; no trial value |
| 5 | COMPLETE: study group/DSMB administrative names; no applicable relationship |
| 6 | COMPLETE: remaining DSMB member; no applicable relationship |
| 7 | COMPLETE: primary endpoint rationale, historical surrogate values; N001/S001 |
| 8 | COMPLETE: A1C measurement rules, device baseline/follow-up counts; N002/S002 |
| 9 | COMPLETE: discordant A1C device transitions and percentages; N003 |
| 10 | COMPLETE: Tanita scale/annual inspection; measurement definition N004 |
| 11 | COMPLETE: activity devices,33/368 initial GT9X users,30-day battery; N005 |
| 12 | COMPLETE: visually inspected hardware illustration; no trial-result quantity |
| 13 | COMPLETE: MVPA definition/wear/missingness/aggregation; S003/N006 |
| 14 | COMPLETE: R code imports,10-minute minimum bouts and output thresholds; S004 |
| 15 | COMPLETE: R code nonwear90min/validday840min/cutpoints and summary inputs; S004 |
| 16 | COMPLETE: R code imputation and all three bout calls; S004 |
| 17 | COMPLETE: R code merge/export; S004 |
| 18 | COMPLETE: data quality/source handling and6/12-month outcome derivation; S005 |
| 19 | COMPLETE: stratification and30-day program-start requirement; S006 |
| 20 | COMPLETE: baseline/6/12-month visits and contact rules; N007 |
| 21 | COMPLETE: AI intervention10notifications/day and tracking definition; N008 |
| 22 | COMPLETE:19lessons months1–6;6lessons months7–12; N008 |
| 23 | COMPLETE: algorithm1.0 and input missingness not imputed; S007 |
| 24 | COMPLETE: individual adaptive intervention mechanism; S007 |
| 25 | COMPLETE: pretraining pooled/trial individual learning; S007 |
| 26 | COMPLETE: physical activity/app engagement reward definitions; S007 |
| 27 | COMPLETE: primary/per-protocol cohort definitions; S008 |
| 28 | COMPLETE: eFigures1–4/eTables1–4 statistical and population definitions; S009–S010 |
| 29 | COMPLETE: eTables4–13 definitions/tests/visit windows; S011–S015 |
| 30 | COMPLETE: eTables13–18 definitions/MICE/pattern-mixture/actigraphy sensitivities; S016–S019 |
| 31 | COMPLETE: eTables19 cluster definitions and20 AE units; S020–S021 |
| 32 | COMPLETE: visual eFigure1 app examples; no participant-result value |
| 33 | COMPLETE: visual eFigure2 app examples; no participant-result value |
| 34 | COMPLETE: visual eFigure3 four adjusted outcome rows/captions; N009–N012/S022–S025 |
| 35 | COMPLETE: visual eFigure4 thirteen subgroup/overall rows/captions; N013–N025/S026–S038 |

All35 assigned units mapped. Scientific coverage gaps: none. Derivative limitation: native text on figures34–35 contains captions only; visual transcription supplies all plotted numbers. Workbook/Office/CSV sources: none assigned; displayed R code describes CSV processing but the referenced raw CSV files are not supplied.

## Quantitative and method relationship map

IDs are shard-local `R1-` keys; coordinator may assign global N/S IDs without changing contents. Numeric counterparts and inferential rows cross-reference rather than duplicate. Matching main-paper keys refer to outcome/population/timepoint/model names; the main-paper mapper owns source values there.

| Local key | Source | Complete quantitative relationship and matching key |
|---|---|---|
| R1-N001 / R1-S001 | [p7](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=7) | Endpoint selection rationale: historical5–7%weight loss;4%loss+150min/week;1kg=2.2lb;16%diabetes risk reduction/kg;100kg=220lb and4%loss=8.8lb,approximately64%risk reduction stated;150min/week without weight target associated with44%risk reduction and2.9kg average loss; historical meta-analysis26–50%risk reduction;0.2 percentage-point A1C improvement at1year benchmark contrasted with historical0.1%improvement and Finnish intervention−0.1/control+0.1. These are historical context, not current trial effect estimates. Matching main key: composite primary endpoint definition. |
| R1-N002 / R1-S002 | [p8](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=8) | A1C devices: Afinion2 baseline334/follow-up282; A1CNow+33/30; serum1/0. Follow-up12months. Point-of-care devices FDA-cleared,CLIA-waived,NGSP-certified;results within5min. A1CNow+ failure two consecutive QC messages; prior test within3months; alternative assay offered if change≤−0.9 or≥+0.8points, described as outside95%CI versus venous assay. Matching main keys: A1C baseline/follow-up denominators and point-of-care measurement. |
| R1-N003 | [p9](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=9) | Device transitions baseline→12months: Afinion→A1CNow+6(1.6%trial population), reverse1(0.27),serum→Afinion0(0),Afinion→serum0(0),serum→A1CNow+1(0.27);total8(2.2). |
| R1-N004 | [p10](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=10) | Body weight TanitaWB-100A;annual inspection;remove footwear/accessories/jackets. Matching main key: measured body weight change. |
| R1-N005 | [p11](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=11) | ActiGraphGT9X-BT Link/CPIW;33 of368randomized initiallyGT9X-BT and switched with prior data retrieved;CPIW30-day battery;3G upload hub. Matching main key: actigraphy instrument and physical activity outcome. |
| R1-N006 / R1-S003 | [p13](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=13) | Seven consecutive wear days per visit;baseline plus monthly,total12visits and maximum11postbaseline periods. Counts/min;MVPA vector magnitude≥3941;validday≥10h wear;90consecutive zero minutes define nonwear;interpolation inside valid days;invalid days assigned0MVPA. Valid daily MVPA averaged within visit;≥10consecutive-minute bouts separately counted/duration. Weekly MVPA summed over valid wear periods/divided by number available. Less than5of7assigned days means noncompliant and0weekly PA. Matching main keys: ≥150weekly-minute component and missing actigraphy handling. |
| R1-S004 | [pp14–17](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=14) | Printed R code explicitly defines bouts_min10,bouts_maxInf;midnight_to_midnight;get_wear_flag(nonwear_0s_minimum_window90);get_valid_day_flag(validday_nonwear_maximum_window840);ac_imp=impute_missing_data(ac_mid,wnw,valid.long). `activity_stats(ac,timestamp)` plus sedentary_thres2185,2859,3941 called using `ac`;summary counts/day/wear-time from1853 output. Three calls to `BoutsOfPA(ac,valid.long,timestamp,bouts_min=bouts_min,bouts_max=bouts_max)` are printed under2185/2859/3941 names,without a threshold argument in any displayed call. `BoutsOfPA.R` is sourced but not supplied as a separate file. Summary and bout tables merge on id,visit,site;CSV export,row.namesFALSE. Code and prose are distinct mapped statements, with no assumed library semantics. Full code preserved below. |
| R1-S005 | [p18](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=18) | gt3x→CSV→dailyMVPA STATA.dta;PI/research staff assess6/12-month outcomes using those data plusREDCap. Missing wear periods investigated for participant noncompliance versus absent staff downloads. Matching main keys: PA computation and outcome missingness. |
| R1-S006 | [p19](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=19) | Block-stratified randomization by baselineA1C and recruitment site;open-label;biostatistician unmasked forDSMB reporting. Human classes within30days of randomization;otherwise randomization temporarily halted. Matching main key: randomization strata/design. |
| R1-N007 | [p20](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=20) | Three in-person visits:baseline,6months,12months;automated wear/visit reminders. Matching main key: visit schedule. |
| R1-N008 | [pp21–22](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=21) | AI notifications capped10/day,fewer with high adherence;19CDC-based lessons months1–6;6lessons months7–12. Smartphone and manual activity tracking;Bluetooth/manual weight;nutrition tracking. Matching main key: assigned12-month AI intervention dose/content. |
| R1-S007 | [pp23–26](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=23) | JITAIalgorithm1.0;only collected input data used,no input imputation;no human processing. Pretrial model trained pooled across historical users,trial updates individual-only with separate state/action histories,no realtime cross-user pooling. Reward favors active minutes with diminishing returns;app openings near notifications indicate engagement. Matching main key: intervention individualization versus statistical cluster sensitivity. |
| R1-S008 | [p27](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=27) | Primary analysis=all randomized;per-protocol=all randomized completing12-month visit and no prohibited steroids/antihyperglycemics/weight-loss drugs. Matching main keys: randomized analysis and restricted12-month sensitivity population. |
| R1-S009 | [p28](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=28) | eFigure3 randomized population,age-adjustedRD in percentage points,one-sided95%CI,12months;age imbalance adjustment;negativeAI−Human denotes lowerAI achievement;NI margin−15pp,CI must not cross. Method index calls outcomes primary and secondary. Matching main key: age-adjusted primary outcome/components. |
| R1-S010 | [p28](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=28) | eFigure4 randomized subgroup bysite,sex,age,baselineA1C,BMI;RD/one-sided95%CI,NI−15pp;negativeAI−Human lowerAI frequency;exploratory,no multiplicity/formal testing. Matching main key: subgroup analysis. |
| R1-S011 | [pp28–29](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=28) | eTables1a/b app version/release/count-percent startersAI;2Human program4CDCsites,count-percent assignment;3full randomized baseline;4randomized/per-protocol eligibility criteria fastingglucose100–125mg/dLprior1year orstudyA1C5.7–6.4%baseline orclinicA1C5.7–6.4%prior1year;chi-squared proportions/Wilcoxon rank-sum continuous. Matching main keys: intervention version,baseline/eligibility. |
| R1-S012 | [p29](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=29) | eTables5baseline bysite,6A1C<5.7versus5.7–6.4,7completion status use mainTable1 methods. eTable8records missing-data frequency/handling/rationale. Matching main key: baseline/attrition/missing-data methods. |
| R1-S013 | [p29](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=29) | eTable9visit windows6month168–196days,12month351–379days;days outside window described relative to lastday;mean summarized among outside-window only;chi-squared proportions/Wilcoxon continuous. Matching main key: outcome timepoint. |
| R1-S014 | [p29](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=29) | eTable10randomized prohibited steroid/weight-loss/antihyperglycemic use;GLP1agonists classified antihyperglycemic;participant-level/arm-level;chi-squared.10bpercent participants byarm.11per-protocol baseline. Matching main key: postrandomization prohibited drugs/analysis eligibility. |
| R1-S015 | [pp29–30](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=29) | eTable12unique component combinations among composite achievers,denominator numberachievers withinarm/overall:≥5%weight loss;≥4%loss+≥150min/weekPA;≥0.2%HbA1creduction.13diabetes-rangeA1C6and/or12months forces endpointfailure regardlessweight/PA;diagnosis notadjudicated,two confirmatory tests needed. Matching main keys: primary composite/diabetes exclusions/components. |
| R1-S016 | [p30](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=30) | eTable14per-protocol continuousbodyweight/A1C change andweeklyPA12months.15per-protocol primary/secondarybinary,main statistical methods. Matching main key: continuous measures/restricted population. |
| R1-S017 | [p30](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=30) | eTable16:primary missing12month=failure;MAR MICE sensitivity baselineweight,PA,A1C,demographics,studygroup,engagement(group-normalizedAIweeksuse/Humansessionattendance);20imputed datasets,Rubin rules. Matching main key: multiple-imputation sensitivity. |
| R1-S018 | [p30](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=30) | eTable17pattern-mixture:AI noncompleters0%success,Human noncompleters37.8%success asobserved completers;directional conservativeAI sensitivity. Matching main key: MNAR/pattern-mixture NI sensitivity. |
| R1-S019 | [p30](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=30) | eTable18a:primary nonwear0weeklyPA;best-case thosewithout100%Actigraphcompliance assigned150weeklymin hadtheyworn.18b:allparticipants attain150min/week. Bothrandomized. Matching main key: physicalactivity sensitivity. |
| R1-S020 | [p31](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=31) | eTable19a:fourHumanDPPclusters1–4,allAI fifthcluster,cluster-robuststandarderrors.19b:clusterIDsite+calendarmonthrandomization toapproximateHuman cohorts/AI appversions. Matching main key: NIcluster sensitivities. |
| R1-S021 | [p31](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=31) | Printed method-index rows18/19 additionallydescribe diabetes-rangeA1C andcontinuousoutcomes asabove;preservetheseindexlabels separately.20a=randomized participantswith≥1AE plusAEfrequency bycategory/grade/relatedness/condition;20b/20c=countofevents bygrade/relatedness;20dcondition+grade+intervention. Matching main key: adverseevents participants-versus-events distinction. |

## eFigure 3: adjusted binary outcomes, source page34

Source [DOC-003p34](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=34), REPORT. Visual numbers supplement caption-onlynative extraction. All4 rows display age-adjusted AI−Human riskdifference andlowerendpoint ofone-sided95%CI,percentagepoints;noPvalue printed. Time12months. NIreference−15pp;negativeestimate lowerAIachievement;CI mustnotcrossNIthreshold. Componentintervals descriptive/exploratory,no multiplicity/noformaltests. HbA1creduction restricted baselineprediabetesAI130/Human130.

| Numeric key | Statistical key | Outcome | AI-DPP n/N(%) | Human-DPP n/N(%) | Age-adjusted RD (one-sided95%lowerlimit),pp |
|---|---|---|---|---|---|
| R1-N009 | R1-S022 | Diabetesriskreductionbenchmark12months |58/183(31.7)|59/185(31.9)|−2.0(−9.8)|
| R1-N010 | R1-S023 |5%weightloss|31/183(16.9)|37/185(20.0)|−3.4(−9.8)|
| R1-N011 | R1-S024 |4%weightloss+150minweeklyPA|23/183(12.6)|23/185(12.4)|0.3(−4.7)|
| R1-N012 | R1-S025 |0.2%A1Creduction|35/130(26.9)|35/130(26.9)|−1.6(−10.7)|

Matching main-paper keys: primary composite/randomized/12months/ageadjustment; componentweight5%,weight4%+PA150,A1C0.2 restrictedprediabetes. Axis −20,−15,−10,−5,0;solidNIline−15,dottednull0;leftAIinferior/rightAInoninferior. Counts are observed;adjustedRDmustremain distinguished from crude RD.

## eFigure 4: exploratory primary-outcome subgroups, source page35

Source [DOC-003p35](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=35), REPORT. Visual transcription. Outcome diabetesriskreductionat12months;AI−HumanRDpp,one-sided95%lowerbound;noPvalues,noformalhypothesistesting,no multiplicityadjustment. NIline−15;null0;negativeAI−HumanlowerAIachievement. Plot axis−30,−20,−10,0,10,20,30. Model label isriskdifference withoutage-adjustmentdescriptor inthisdisplay;do nottransfereFigure3adjustmenttoit.

| Numeric key | Statistical key | Subgroup | AI-DPP n/N(%) | Human-DPP n/N(%) | RD(lower95%endpoint),pp |
|---|---|---|---|---|---|
|R1-N013|R1-S026|Overallpopulation|58/183(31.7)|59/185(31.9)|−0.2(−8.2)|
|R1-N014|R1-S027|Baltimore,MD|36/120(30.0)|43/123(35.0)|−5.0(−14.9)|
|R1-N015|R1-S028|Reading,Pennsylvania|22/63(34.9)|16/62(25.8)|9.1(−4.4)|
|R1-N016|R1-S029|Female|36/121(29.8)|42/139(30.2)|−0.5(−9.9)|
|R1-N017|R1-S030|Male|22/62(35.5)|17/46(37.0)|−1.5(−16.9)|
|R1-N018|R1-S031|Age<65years|32/119(26.9)|40/148(27.0)|−0.1(−9.1)|
|R1-N019|R1-S032|Age≥65years|26/64(40.6)|19/37(51.4)|−10.7(−27.7)|
|R1-N020|R1-S033|BaselineA1C<6.0%|37/123(30.1)|38/135(28.1)|1.9(−7.4)|
|R1-N021|R1-S034|BaselineA1C≥6.0%|21/60(35.0)|21/50(42.0)|−7.0(−22.4)|
|R1-N022|R1-S035|Overweight|17/55(30.9)|13/47(27.7)|3.2(−11.7)|
|R1-N023|R1-S036|ClassIobesity|20/70(28.6)|23/57(40.4)|−11.8(−25.7)|
|R1-N024|R1-S037|ClassIIobesity|11/33(33.3)|16/47(34.0)|−0.7(−18.5)|
|R1-N025|R1-S038|ClassIIIobesity|10/25(40.0)|7/34(20.6)|19.4(−0.5)|

BMIfootnote:overweight25.0–29.9,classI30.0–34.9,classII35.0–39.9,classIII≥40.0kg/m². Matching mainkeys: overallprimaryrandomized12month/crudeRD;site,sex,age65,A1C6.0,BMIclassification subgroups. Subgroups partition counts and denominators within each variable;thetable retainsallstrata explicitly.

## Non-result illustrations and administrative units

Pp1–6provideidentity,contents andstudypersonnel only;contents/tablepointers retainedbelow asmatching metadata. P12hardwarepictures showGT9X-BT/CPIW,CPdatahub,chargingdock,powercable,USBcable. P32eFigure1shows illustrative30minactivitynotification andnutritiondemo833cal with45%carbs/15%fat/30%protein,othermeal-componentdisplayvalues;these areapp examples,nottrialparticipants/results. P33eFigure2illustrates10lbweightgoal,60mindailyactivitygoal,5/5days,100minprogress,waistline41.2in/4.5%/1.5%examples;educationalappcontent isnotendpointdata. No denominator/effect/testrelationship fromtheseexamples pertains tothetrial.

