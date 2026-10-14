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

## Complete reusable page-text transcripts, read fresh for mapping

The following transcripts preserve all quantitative statements/code/table-method rows on assigned text-backed units, including administrative and pointer material. They are derivative locators; exact source pages remain authoritative. Figures34–35were transcribed visually above and their nativecaptions appear below.

### PDF page 01 — reused layout text

```text
                           Supplemental Online Content



Mathioudakis N, Lalani B, Abusamaan MS, et al; for the AI-DPP Study Group. An AI-
Powered Lifestyle Intervention vs Human Coaching in the Diabetes Prevention Program.
JAMA. Published online October 27, 2025. doi:10.1001/jama.2025.19563




Supplement 2. eMethods
eFigures and eTables
eReferences




This supplemental material has been provided by the authors to give readers additional information
about their work.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 02 — reused layout text

```text
                                     Supplementary Appendix
Table of Contents

LIST OF STUDY GROUP................................................................................................................... 5

ADDITIONAL METHODS.................................................................................................................. 7

   SELECTION OF PRIMARY ENDPOINT ............................................................................................................... 7

   A1C MEASUREMENT ................................................................................................................................. 8

   BODY WEIGHT MEASUREMENT ................................................................................................................... 10

   PHYSICAL ACTIVITY MEASUREMENT ............................................................................................................. 11

   PHYSICAL ACTIVITY DATA PROCESSING ........................................................................................................ 13

   DATA QUALITY PROCESSES ....................................................................................................................... 18

   RANDOMIZATION .................................................................................................................................... 19

   STUDY TEAM’S INTERACTIONS WITH PARTICIPANTS .......................................................................................... 20

   DESCRIPTION OF SWEETCH INTERVENTION .................................................................................................... 21

   SWEETCH ALGORITHM OVERVIEW ............................................................................................................... 24

   DEFINITIONS OF STUDY COHORTS ............................................................................................................... 27

   SUMMARY OF METHODS FOR SUPPLEMENTARY FIGURES AND TABLES NOT INCLUDED IN MAIN MANUSCRIPT ..................... 28

SUPPLEMENTARY FIGURES AND TABLES ....................................................................................... 32

   EFIGURE 1. SCREENSHOTS OF PERSONALIZED PUSH NOTIFICATIONS AND NUTRITIONAL SUPPORT IN SWEETCH APP ........ 32


   EFIGURE 2 SCREENSHOTS OF CONNECTED HEALTH TRACKING AND EDUCATIONAL CONTENT IN SWEETCH APP .............. 33


   EFIGURE 3. FOREST PLOT OF ADJUSTED BINARY OUTCOME DIFFERENCES ............................................................. 34


   EFIGURE 4 EXPLORATORY SUBGROUP ANALYSIS OF PRIMARY OUTCOME ............................................................... 35


   ETABLE 1A. AI-DPP UPDATES DURING TRIAL PERIOD ...................................................................................... 36


   ETABLE 1B. AI-DPP UPDATES DURING TRIAL PERIOD ...................................................................................... 37


   ETABLE 2. HUMAN-DPP BREAKDOWN BY SITE ............................................................................................... 38


© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 03 — reused layout text

```text
  ETABLE 3. BASELINE CHARACTERISTICS OF THE RANDOMIZED POPULATION ........................................................... 39


  ETABLE 4. DPP ELIGIBILITY BREAKDOWN ...................................................................................................... 41


  ETABLE 5. BASELINE CHARACTERISTICS BY SITE .............................................................................................. 42


  ETABLE 6. BASELINE CHARACTERISTICS BY BASELINE A1C STATUS ...................................................................... 44


  ETABLE 7. BASELINE CHARACTERISTICS BY TRIAL COMPLETION STATUS ................................................................ 46


  ETABLE 8A. MISSING DATA: SURVEY DATA..................................................................................................... 48


  ETABLE 8B. MISSING DATA: ACTIGRAPHY DATA .............................................................................................. 49


  ETABLE 8C. MISSING DATA: 12-MONTH MEASURES ........................................................................................ 50


  ETABLE 9. ADHERENCE TO FOLLOW-UP SCHEDULE ......................................................................................... 51


  ETABLE 10A. PARTICIPANTS ON PROHIBITED MEDICATIONS ............................................................................... 52


  ETABLE 10B. PROHIBITED MEDICATION ........................................................................................................ 52


  ETABLE 11. BASELINE CHARACTERISTICS FOR PARTICIPANTS WITH 12-MONTH OUTCOME DATA WHO DID NOT INITIATE
  PROHIBITED MEDICATIONS ........................................................................................................................ 53


  ETABLE 12 DISTRIBUTION OF OUTCOMES ACHIEVED AMONG PARTICIPANTS WHO MET COMPOSITE OUTCOME ............... 55


  ETABLE 13. PARTICIPANTS WITH DIABETES-RANGE A1C ................................................................................... 56


  ETABLE 14 CONTINUOUS OUTCOMES .......................................................................................................... 57


  ETABLE 15. ANALYSIS RESTRICTED TO PARTICIPANTS WITH 12-MONTH DATA WHO DID NOT INITIATE PROHIBITED
  MEDICATIONS ........................................................................................................................................ 58

  ETABLE 16. SENSITIVITY ANALYSIS IMPUTING OUTCOMES IN THOSE WITH MISSING 12 MONTH OUTCOMES DATA USING
  MULTIPLE IMPUTATION BY CHAIN EQUATIONS ................................................................................................ 59

  ETABLE 17. SENSITIVITY ANALYSIS OF PRIMARY ENDPOINT: PATTERN MIXTURE MODEL ASSUMING DIFFERENTIAL OUTCOME
  RATES AMONG NON-COMPLETERS ............................................................................................................. 60

  ETABLE 18A. SENSITIVITY ANALYSIS OF PRIMARY ENDPOINT: “BEST -CASE” SCENARIO FOR ACTIGRAPH NON-WEAR PERIODS
  .......................................................................................................................................................... 61

  ETABLE 18B. SENSITIVITY ANALYSIS OF PRIMARY ENDPOINT: ASSUMING ATTAINMENT OF PHYSICAL ACTIVITY GOAL FOR ALL
  PARTICIPANTS ........................................................................................................................................ 61


  ETABLE 19A SENSITIVITY ANALYSIS USING CLUSTER-ROBUST STANDARD ERRORS BY DPP SITE .................................. 62




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 04 — reused layout text

```text
   ETABLE 19B SENSITIVITY ANALYSIS USING CLUSTER-ROBUST STANDARD ERRORS BY SITE AND MONTH OF RANDOMIZATION
   .......................................................................................................................................................... 62

   ETABLE 20A. ADVERSE EVENTS BY CATEGORY ................................................................................................ 63


   ETABLE 20B. ADVERSE EVENTS BY GRADE ..................................................................................................... 64


   ETABLE 20C. ADVERSE EVENTS BY RELATEDNESS TO ASSIGNED INTERVENTION ....................................................... 65


   ETABLE 20D. ADVERSE EVENTS BY CONDITION AND GRADE ............................................................................... 66


REFERENCES .............................................................................................................................. 69




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 05 — reused layout text

```text
LIST OF STUDY GROUP

Group Name: AI-DPP Study Group

Principal Investigator:

    -   Nestoras Mathioudakis, MD MHS; Division of Endocrinology, Diabetes and Metabolism,
        Department of Medicine, Johns Hopkins University School of Medicine, Baltimore, MD, USA

Contributors:

    -   Benjamin Lalani, B.S.; Division of Endocrinology, Diabetes & Metabolism, Department of
        Medicine, Johns Hopkins University School of Medicine, Baltimore, MD, USA
    -   Mohammed S. Abusamaan, MD MPH; Division of Endocrinology, Diabetes and Metabolism,
        Department of Medicine, Johns Hopkins University School of Medicine, Baltimore, MD, USA
    -   Adrian Dobs, MD MHS; Division of Endocrinology, Diabetes and Metabolism, Department of
        Medicine, Johns Hopkins University School of Medicine, Baltimore, MD, USA
    -   Jeromie Ballreich, PhD MHS; Department of Health Policy and Management, Johns Hopkins
        Bloomberg School of Public Health, Baltimore, MD, USA
    -   Nisa Maruthur, MD, MHS; Division of General Internal Medicine, Department of Medicine,
        Johns Hopkins University School of Medicine, Baltimore, MD, USA
    -   John McGready, PhD; Department of Biostatistics, Johns Hopkins Bloomberg School of Public
        Health, Baltimore, MD, USA
    -   Kristin Riekert, PhD; Division of Pulmonary and Critical Care Medicine, Department of
        Medicine, Johns Hopkins University, Baltimore, MD, USA
    -   Amal Wanigatunga, PhD; Department of Epidemiology, Johns Hopkins Bloomberg School of
        Public Health, Baltimore, MD, USA
    -   Brian Kane, MD; Tower Health Medical Group Family Medicine, Reading, PA, USA
    -   Aliyah Shehadeh, B.S.; Division of Endocrinology, Diabetes & Metabolism, Department of
        Medicine, Johns Hopkins University School of Medicine, Baltimore, MD, USA
    -   Defne Alver, B.S. M.H.S.; Division of Endocrinology, Diabetes & Metabolism, Department of
        Medicine, Johns Hopkins University School of Medicine, Baltimore, MD, USA
    -   Benjamin Ringham, B.S. M.S.; Division of Endocrinology, Diabetes & Metabolism, Department
        of Medicine, Johns Hopkins University School of Medicine, Baltimore, MD, USA
    -   Fatmata Vandi, B.S. M.S.; Division of Endocrinology, Diabetes & Metabolism, Department of
        Medicine, Johns Hopkins University School of Medicine, Baltimore, MD, USA
    -   Daniel Zade, B.S.; Division of Endocrinology, Diabetes & Metabolism, Department of Medicine,
        Johns Hopkins University School of Medicine, Baltimore, MD, USA
    -   Pamela Marrero, CCRP; Reading Hospital Tower Health, Reading, Pennsylvania
    -   Amy Schiller, B.S.; Reading Hospital Tower Health, Reading, Pennsylvania
    -   Mary (Ellie) Alderfer, M.S.N, R.N.; Reading Hospital Tower Health, Reading, Pennsylvania

Data Safety and Monitoring Board:

    -    Nae-Yuh Wang, Ph.D; Division of General Internal Medicine, Department of Medicine, Johns
         Hopkins University School of Medicine, Baltimore, Maryland
     - John McGready, Ph.D; Department of Biostatistics, Johns Hopkins Bloomberg School of Public
         Health, Baltimore, Maryland
     - Seth Martin, M.D. M.H.S; Division of Cardiology, Department of Medicine, Johns Hopkins
         University School of Medicine, Baltimore, Maryland
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 06 — reused layout text

```text
    -   Sara Benjamin-Neelon, Ph.D J.D. M.P.H; Department of Health, Behavior, and Society, Johns
        Hopkins Bloomberg School of Public Health, Baltimore, MD




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 07 — reused layout text

```text
ADDITIONAL METHODS

Selection of Primary Endpoint

In this trial, we assessed the CDC’s benchmark for type 2 diabetes risk reduction, which has been
validated in previous studies as a reliable surrogate for decreased incidence of diabetes.

Both the DPP and Finnish DPP reported a significant reduction in diabetes incidence among individuals
achieving 5% to 7% weight loss.1,2 While the specific recommendation of a 4% weight loss combined
with 150 minutes of physical activity is not derived from a single study, it represents a pragmatic and
meaningful goal. The DPP found that each kilogram (2.2 lbs) of weight loss corresponded to a 16%
reduction in diabetes risk3; thus, a 4% weight loss for an individual weighing 100 kg (220 lbs) equates to
approximately 8.8 lbs, potentially reducing diabetes risk by around 64%.

Furthermore, individuals who met the physical activity benchmark of 150 minutes per week, but not the
weight loss target, experienced a 44% decrease in diabetes risk, independent of their modest average
weight loss of approximately 2.9 kg.3 A systematic review and meta-analysis also demonstrated that
engaging in 150 minutes of moderate physical activity weekly is associated with a 26% to 50% reduction
in the risk of developing diabetes.4

Lastly, the benchmark of a 0.2% improvement in A1C at one year is supported by findings from the
original DPP, which reported a 0.1% A1C improvement in the lifestyle intervention group at one year2;
thus, a 0.2% point reduction would indicate even greater improvement in metabolic control. Similarly, in
the Finnish DPP, the intervention group experienced a mean A1C reduction of 0.1% at one year, while the
control group saw an increase of 0.1%.5




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 08 — reused layout text

```text
A1C Measurement

Study Member Obtaining A1C Measurements

A1C measurements were obtained by trained and certified research staff. For the A1CNow+ test kit,
research staff were required to complete and successfully pass a pts Diagnostics training course and
receive a certificate. For the Afinion™ 2, research staff were required to successfully complete the
training provided by Johns Hopkins Medicine on the employee MyLearning platform.

Instruments Used for A1C Measurements

A1C measurements were obtained using FDA-cleared, CLIA-waived, and NGSP-certified point-of-care
devices, including the Afinion™ 2 Analyzer, Siemens DCA Vantage, and A1CNow+ test kit. These tests
required a fingerstick blood sample, with results available within 5 minutes. All A1C testing was
conducted by a trained research coordinator.

The A1CNow+ test kit was a portable device used primarily for home study visits (PTS Diagnostics).
Although FDA-approved and NGSP-certified, it exhibited a larger mean bias compared to laboratory-
based measurements and other point-of-care devices (Afinion™ 2 Analyzer and Siemens DCA Vantage).
Additionally, A1CNow+ was more susceptible to interference from hemoglobinopathies (e.g., sickle cell
trait or disease) and rheumatoid factor.

To mitigate potential inaccuracies, a screening protocol was implemented for participants requesting
home study visits:

    •   Participants with conditions known to interfere with the A1CNow+ test were excluded from
        home testing and instead scheduled for in-clinic testing using more accurate devices (Afinion™ 2
        Analyzer or Siemens DCA Vantage).
    •   If an A1CNow+ test produced a quality control error message, the test was repeated with a
        second sample.
    •   A1CNow+ failure was defined as two consecutive quality control or error messages during the
        same visit.
    •   If an A1CNow+ result deviated significantly (≤ -0.9 or ≥ +0.8 points) from a prior A1C
        measurement within the past three months (i.e., outside the 95% confidence interval for
        A1CNow+ compared to venous sample A1C), an alternative A1C test was offered at the clinical
        research unit or a Labcorp facility.

The following table summarizes the number of participants who underwent A1C testing using each device
at baseline and at the 12-month follow-up:

 A1C Measurement Device/Method                     Baseline (n)        12-Month Follow-up (n)
 Afinion™ 2 Analyzer                               334                 282
 A1CNow+                                           33                  30
 Serum (Labcorp facility)                          1                   0

Additionally, some participants transitioned between different A1C testing methods between baseline and
follow-up:

Participants with A1C measurements with discordant devices:
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 09 — reused layout text

```text
 Baseline Device → 12-Month Follow-up Device                       No. of Participants (% of Trial
                                                                   Population)
 Afinion™ 2 Analyzer → A1CNow+                                     6 (1.6)
 A1CNow+ → Afinion™ 2 Analyzer                                     1 (0.27)
 Serum → Afinion™ 2 Analyzer                                       0 (0)
 Afinion™ 2 Analyzer → Serum                                       0 (0)
 Serum → A1CNow+                                                   1 (0.27)
 Total                                                             8 (2.2)




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 10 — reused layout text

```text
Body Weight Measurement

Study Member Obtaining Body Weight Measurements

Performed by trained research coordinators.

Instruments Used

All body weight measurements were taken via the Tanita WB-100A Digital Medical Scale. Scales were
inspected by the Johns Hopkins Clinical Engineering annually. Before taking the weight measurements,
participants were asked to use the bathroom, if needed, remove footwear, accessories such as wallets or
keys, and jackets.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 11 — reused layout text

```text
Physical Activity Measurement

Study Member Obtaining Physical Activity Measurements

Performed by trained research coordinators.

Instruments Used

ActiGraph provided a cloud-based service platform, CenterPoint, which enabled automated and manual
capture of actigraphy data from the ActiGraph monitor. At the baseline visit, participants were provided
with (1) the ActiGraph activity monitor, (2) a CenterPoint (CP) data hub, (3) charging dock, (4) power
cable, and (5) USB cable, along with a participant guide containing detailed instructions (pictured below).
The CP data hub used a 3G cellular connection (covered by the study team) to transmit data from the
activity monitor to the study team via the CenterPoint cloud software, without relying on participants’
home WiFi. Using Bluetooth technology, the data hub automatically captured data when the monitor was
in proximity. In addition, participants were instructed to upload raw data after each wear period by
physically connecting the activity monitor to the data hub using the USB cable and charging dock. This
ensured that raw high-resolution acceleration data were transmitted reliably. The study team monitored
participant compliance remotely via CenterPoint, which tracked both Bluetooth-based and manual data
uploads.

The instruments used to measure physical activity (MVPA) were the ActiGraph GT9X-BT Link and
Centrepoint Insight Watch (CPIW) — FDA-cleared devices that can distinguish non-wear time from
physical inactivity. Due to connectivity and uploading issues with some participants in the beginning of
the trial, the study investigators decided to switch from the GT9X-BT to CPIW watch, to ensure the
integrity and completeness of trial data. Among the 368 randomized participants, 33 were assigned to the
GT9X-BT at baseline and as the switch took place, they were provided with the new CPIW and their data
from the GT9X-BT was retrieved.

Both devices captured and recorded high-resolution raw acceleration data, which were converted into a
variety of objective activity measures. The CPIW, which was the newer model of the ActiGraph wrist
monitor, had an extended 30-day battery life, allowing for continuous wear time during the scheduled
wear period. This minimized participant burden and the potential for missing data associated with
frequent device charging.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 12 — reused layout text

```text
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 13 — reused layout text

```text
Physical Activity Data Processing

Accelerometry Data Collection and Processing

Physical activity data were collected from participants using ActiGraph accelerometry devices (GT9X or
CPIW) worn on the wrist. Participants were instructed to wear the devices for seven consecutive days
during each scheduled visit, with each 7-day collection representing a typical week within that month.
This approach allowed for sampling of physical activity while accounting for secular trends such as
weather and holidays. Data collection occurred at baseline and continued monthly for a total of 12 visits.

The accelerometers recorded activity counts per minute, which were processed to identify moderate-to-
vigorous physical activity (MVPA) using Montoye’s cut point of 3941 counts per minute. This threshold
was selected based on validated criteria for classifying MVPA in adults.6 Activity data were collected as
raw timestamped files in CSV format and imported into R for processing.

Data Preprocessing

For each file, accelerometry data were extracted, and relevant columns were renamed for consistency.
The timestamp data were parsed to accurately reflect the date and time of each observation. Data were
segmented into daily epochs from midnight to midnight to ensure standardized processing. Only days
with at least 10 hours of wear time were considered valid for subsequent analysis. Wear and non-wear
periods were identified using a 90-minute window of consecutive zero counts as the criterion for non-
wear detection.7 Valid wear days were determined by applying a threshold of at least 10 hours of wear
time per day. Missing data within valid days were imputed using interpolation methods to ensure
continuity in physical activity monitoring. Days without valid accelerometry were assigned zero minutes
of MVPA to reflect the assumption that no moderate-to-vigorous activity was performed during those
periods.

MVPA Calculation

Activity intensity was classified as MVPA if the vector magnitude of accelerometer counts per minute
was equal to or greater than 3941. For each valid wear day, the total number of MVPA minutes was
computed and averaged across valid days for each visit. Additionally, sustained bouts of MVPA lasting at
least 10 consecutive minutes were identified using the same threshold of 3941 counts per minute. The
number of these bouts and the total duration spent in them were calculated for each valid wear day. The R
code that was used for this calculation is provided below.

Aggregation of MVPA Across Visits

To obtain the average MVPA minutes per week across the study period, the total MVPA minutes per
week from all valid wear periods were summed and divided by the number of available wear periods
(maximum of 11 post-baseline visits). This approach provided an average estimate of weekly MVPA
throughout the 12-month follow-up period.

Actigraphy Compliance

If the participant did not wear their monitor for at least 5 of their 7 assigned days, they were considered
noncompliant. In this case, the participant was assigned 0 minutes for physical activity for that week (See
eTable18 for further details and rationale).

© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 14 — reused layout text

```text
R Code for MVPA Calculation

The following R code was used to preprocess wrist-worn ActiGraph data and compute total and bouted
MVPA using vector magnitude thresholds.

rm(list = ls())
# Set working directory to "code" folder
setwd('D:/OneDrive - Johns Hopkins/1 Studies/1 Ongoing/DDP trial/Accelerometry/code')

# Load packages and source bout calculation function
source('BoutsOfPA.R')
library(lubridate)
library(dplyr)
library(readr)
library(arctools)

# Define file path
file_path <- "D:/OneDrive - Johns Hopkins/1 Studies/1 Ongoing/DDP trial/Accelerometry/csv/"
files <- dir(file_path, recursive = TRUE)
files <- files[grep('.csv', files)]

# Bouts definition
bouts_min <- c(10)
bouts_max <- c(Inf)

# Summarize MVPA Activity
out_activity <- data.frame(
  id = numeric(),
  visit = numeric(),
  site = numeric(),
  tas = numeric(),
  n_days = numeric(),
  n_valid_days = numeric(),
  wear_time_on_valid_days = numeric(),
  min_spent_active_1853 = numeric(),
  min_spent_active_2185 = numeric(),
  min_spent_active_2859 = numeric(),
  min_spent_active_3941 = numeric(),
  stringsAsFactors = FALSE
)

pb <- txtProgressBar(min = 0, max = length(files), style = 3)

for (j in 1:length(files)) {
 name <- files[j]
 name.full <- paste0(file_path, name)

 id <- substr(name, 1, 3)
 visit <- substr(name, 5, 6)
 site <- substr(name, 8, 11)

© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 15 — reused layout text

```text
 datai <- read.csv(name.full)
 colnames(datai) <- c("timestamp", "serialnumber", "axis1", "axis2", "axis3", "steps", "vectormagnitude",
"capsense")

    ac <- datai$vectormagnitude
    timestamp <- ymd_hms(datai$timestamp)
    tas <- datai$serialnumber[nrow(datai)]

    ac_mid <- midnight_to_midnight(ac, timestamp)
    wnw <- get_wear_flag(ac_mid, nonwear_0s_minimum_window = 90)
    valid.long <- get_valid_day_flag(wnw, validday_nonwear_maximum_window = 840)
    ac_imp <- impute_missing_data(ac_mid, wnw, valid.long)

    result_summary_1853 <- activity_stats(ac, timestamp)
    result_summary_2185 <- activity_stats(ac, timestamp, sedentary_thres = 2185)
    result_summary_2859 <- activity_stats(ac, timestamp, sedentary_thres = 2859)
    result_summary_3941 <- activity_stats(ac, timestamp, sedentary_thres = 3941)

    active <- data.frame(cbind(
      id, visit, site, tas,
      result_summary_1853$n_days,
      result_summary_1853$n_valid_days,
      result_summary_1853$wear_time_on_valid_days,
      result_summary_1853$time_spent_active,
      result_summary_2185$time_spent_active,
      result_summary_2859$time_spent_active,
      result_summary_3941$time_spent_active
    ))

    out_activity <- rbind(out_activity, active)
    setTxtProgressBar(pb, j)
}

close(pb)

colnames(out_activity) <- c(
  "id", "visit", "site", "tas",
  "n.weardays", "n.valid.weardays", "minutes.on.valid.weardays",
  "minutes.active.1853", "minutes.mvpa.2185",
  "minutes.lmvpa.2859", "minutes.mvpa.3941"
)

# MVPA Bouts Calculation
out_bouts <- data.frame(
 id = numeric(),
 visit = numeric(),
 site = numeric(),
 n.mvpa.10toInf_bouts.2185 = numeric(),
 minutes.mvpa.10toInf_bouts.2185 = numeric(),

© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 16 — reused layout text

```text
    n.lmvpa.10toInf_bouts.2859 = numeric(),
    minutes.lmvpa.10toInf_bouts.2859 = numeric(),
    n.mvpa.10toInf_bouts.3941 = numeric(),
    minutes.mvpa.10toInf_bouts.3941 = numeric(),
    stringsAsFactors = FALSE
)

pb <- txtProgressBar(min = 0, max = length(files), style = 3)

for (j in 1:length(files)) {
 name <- files[j]
 name.full <- paste0(file_path, name)

    id <- substr(name, 1, 3)
    visit <- substr(name, 5, 6)
    site <- substr(name, 8, 11)

 datai <- read.csv(name.full)
 colnames(datai) <- c("timestamp", "serialnumber", "axis1", "axis2", "axis3", "steps", "vectormagnitude",
"capsense")

    ac <- datai$vectormagnitude
    timestamp <- ymd_hms(datai$timestamp)

    ac_mid <- midnight_to_midnight(ac, timestamp)
    wnw <- get_wear_flag(ac_mid, nonwear_0s_minimum_window = 90)
    valid.long <- get_valid_day_flag(wnw, validday_nonwear_maximum_window = 840)
    ac_imp <- impute_missing_data(ac_mid, wnw, valid.long)

 bouts_2185 <- BoutsOfPA(ac, valid.long, timestamp, bouts_min = bouts_min, bouts_max =
bouts_max)[, -c(1:3)]
 bouts_2859 <- BoutsOfPA(ac, valid.long, timestamp, bouts_min = bouts_min, bouts_max =
bouts_max)[, -c(1:3)]
 bouts_3941 <- BoutsOfPA(ac, valid.long, timestamp, bouts_min = bouts_min, bouts_max =
bouts_max)[, -c(1:3)]

    bouts <- data.frame(cbind(
      id, visit, site,
      bouts_2185$n.bouts_from10toInf_minutes,
      bouts_2185$time.spent.in.bouts_from10toInf_minutes,
      bouts_2859$n.bouts_from10toInf_minutes,
      bouts_2859$time.spent.in.bouts_from10toInf_minutes,
      bouts_3941$n.bouts_from10toInf_minutes,
      bouts_3941$time.spent.in.bouts_from10toInf_minutes
    ))

    out_bouts <- rbind(out_bouts, bouts)
    setTxtProgressBar(pb, j)
}


© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 17 — reused layout text

```text
close(pb)

colnames(out_bouts) <- c(
  "id", "visit", "site",
  "n.mvpa.10toInf_bouts.2185", "minutes.mvpa.10toInf_bouts.2185",
  "n.lmvpa.10toInf_bouts.2859", "minutes.lmvpa.10toInf_bouts.2859",
  "n.mvpa.10toInf_bouts.3941", "minutes.mvpa.10toInf_bouts.3941"
)

# Merge Summary Data and Export
combine_summary <- merge(out_activity, out_bouts, by = c("id", "visit", "site"))

write.csv(
 combine_summary,
 "D:/OneDrive - Johns Hopkins/1 Studies/1 Ongoing/DDP trial/Accelerometry/result/DPP_MVPA and
bouts_07012022.csv",
 row.names = FALSE

)




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 18 — reused layout text

```text
Data Quality Processes

Clinical data (including adverse effects and concomitant medications) and laboratory data were entered
into REDCap (Research Electronic Data Capture), a 21 CFR Part 11-compliant data capture system
provided by Johns Hopkins University. The data system included password protection and internal quality
checks, for any source of data that had impacts on the trial’s outcomes for each participant. These quality
measures included missing data algroups and automatic range checks for BMI, weight, A1C, Proof of
A1C measurement, height, Actigraph physical activity start and end dates, and whether Actigraph
physical activity was completed, to identify data that appeared inconsistent, incomplete, or inaccurate,
clinical data were entered directly from the source documents.

To obtain, assess, and convert the Actigraph physical activity data, research coordinators and staff were
trained to work with multiple Centrepoint test accounts, which included only test data created by staff and
no actual participant data. After each month of physical activity completion, research coordinators and
staff downloaded and exported the participants’ data in SafeDesktop in the form of a gt3x file. During the
conversions and analysis of files, research staff and coordinators carefully assessed the participants’ wear
period data to identify any missing wear periods. For those with missing wear periods, research staff
would check the REDCap participant files for any particular notes, and CentrePoint to ensure that the data
was missing due to participants not complying, rather than the staff missing the wear periods from the
CentrePoint platform.

In terms of analyzing, assessing, and converting the physical activity data, several conversions and steps
were required, which were completed in SafeDesktop provided by Johns Hopkins. Physical activity data
was first downloaded in gt3x format and placed in SafeDesktop, where it was then converted to CSV
files. CSV files were then converted to Moderate to Vigorous Physical Data (MVPA) per day in a
STATA .dta file. The PI and research staff trained in STATA used this converted data and data exported
from REDCap to assess physical activity outcomes and completion at 6-months and 12-months. To
ensure quality of outcome data, the STATA log file that demonstrated the outcomes after coding was also
uploaded to REDCap, where research coordinators would run the log file for each participant.

Research staff and coordinators the Reports feature in REDCap to create different reports for analysis
purposes and identifying missing or incorrect values for different variables and fields. Reports were also
used to summarize overall data and increase the efficiency of the data analysis, management, and quality
control process.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 19 — reused layout text

```text
Randomization

Since a higher value of A1C at baseline represented the strongest risk factor for progression to incident
diabetes and demand for glucose-lowering medications, we used a block stratified randomization
approach by baseline A1C value and recruitment site to ensure that groups were balanced.

This trial was conducted in an open-label manner to ensure pragmatic integrity. The randomization, and
collection of participant data (e.g., weight, height) were completed by research coordinators to ensure
efficiency. This also ensured efficient communication between research staff and local DPPs and
prevented challenges that would’ve arisen if research staff were also blinded to treatment. The trial’s
biostatistician was also unmasked to conduct required reporting to the DSMB.

Due to the Human-DPPs rolling basis enrollment, based on amount of interested participants and
instructor availability, research staff were responsible for ensuring that there were classes starting within
30 days of randomization for the participants assigned to the Human-DPP group. If this was not the case,
randomization for the period was halted until at least one program start date became available within 30
days.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 20 — reused layout text

```text
Study Team’s Interactions with Participants

Research coordinators and staff purposefully did not actively engage with the study participants to
maintain the real-world and pragmatic replication aspect of the trial.

Overall, there were 3 in-person interactions and visits that the participants had with research staff. These
visits took place at Baseline, 6-Month, and 12-Month time points of the trial, where laboratory and survey
data collected from the participants.

To further eliminate unnecessary contact with the participants, any reminders regarding upcoming study
visits, upcoming actigraph wear period, or end of wear period were automated based on the study
schedule of each participant. Staff and coordinators were only allowed to contact patients via phone call,
email, and REDCap text messaging to inquire about scheduling the participant for their study visit,
Actigraph troubleshooting, and Actigraph data collection and upload. Participants who reached out to the
coordinators and staff with inquiries related to their Human-DPP or AI-DPP interventions were given the
interventions contact information, with no further intervention assistance from the research staff and
coordinators.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 21 — reused layout text

```text
Description of Sweetch Intervention

The Sweetch app is a fully automated, AI-driven digital diabetes prevention program designed to
facilitate behavioral change through personalized coaching, self-tracking, and adaptive interventions. The
intervention is grounded in behavioral science, reinforcement learning, and persuasive systems design,
utilizing Just-in-Time Adaptive Interventions (JITAI) to optimize participant engagement.

Core Behavioral Change Mechanisms:

Sweetch integrates multiple evidence-based Behavior Change Techniques (BCTs), including:

    •   Goal setting – Adaptive, AI-driven goal recommendations for physical activity, weight loss, and
        nutrition.
    •   Self-monitoring – Real-time tracking of steps, weight, and dietary intake.
    •   Personalized feedback – AI-generated insights on progress and compliance.
    •   Contextual recommendations – AI-driven push notifications based on user behavior and
        environmental data.
    •   Reinforcement learning – AI dynamically adjusts coaching strategies based on user engagement.
    •   Gamification elements – Leaderboards, challenges, and achievements for motivation.

AI-Driven Personalization

Sweetch's personalization engine leverages:

    1. Historical Data: User demographics, baseline physical activity, weight, and dietary patterns.
    2. Real-Time Contextual Data: Location, calendar events, environmental factors (e.g., weather, time
       of day).
    3. Dynamic Behavioral Data: App interactions, step counts, weight fluctuations, goal adherence.
    4. AI Adaptation Mechanism: The reinforcement learning algorithm continuously refines
       recommendations based on user responsiveness, progressively optimizing engagement.

Key Features of the Sweetch App

A. Digital Coaching and Just-in-Time Adaptive Interventions

    •   AI-generated push notifications sent when participants are most likely to engage.
    •   Messages tailored to individual goals (e.g., increasing physical activity, reducing calorie intake,
        completing educational modules).
    •   Push notifications dynamically adjust based on real-world compliance and user responsiveness.
    •   Limited to 10 notifications per day (fewer if adherence is high).
    •   Participants can toggle notifications on/off but cannot modify their timing or frequency.

B. Physical Activity Tracking

    •   Automatically detects step counts and movement patterns via smartphone accelerometers.
    •   Manual input option for activities not passively tracked (e.g., swimming, Pilates, cycling).
    •   AI suggests incremental increases in activity levels based on individual capacity.

C. Weight Tracking
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 22 — reused layout text

```text
    •   Bluetooth-enabled body weight scale auto-syncs with the app.
    •   Option for manual weight entry if not using a digital scale.
    •   AI provides feedback on weight trends and adaptive goal adjustments.

D. Nutrition Tracking

    •   Users log meals, snacks, and beverages, with AI-generated calorie balance insights.
    •   Adaptive dietary recommendations provided based on reported intake.
    •   Reinforcement learning optimizes dietary interventions by adjusting the complexity of nutritional
        feedback.

E. T2D Prevention Educational Modules

    •   Core Phase (Months 1-6): 19 in-app CDC-based diabetes prevention lessons.
    •   Maintenance Phase (Months 7-12): 6 lessons reinforcing behavioral change.
    •   Delivery Format: Text, video, and interactive content.

F. Gamification & Engagement Features

    •   My Achievements: Tracks milestones and provides motivational reinforcement.
    •   My Challenges: AI-curated challenges to promote habit formation.
    •   My Competitions & Leaderboard: Social comparison features to foster engagement.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 23 — reused layout text

```text
The following describes the Sweetch intervention according to the components of the CONSORT-AI
Extension reporting guidelines8:

 Checklist Item       Details
 Version of the AI    JITAI algorithm 1.0
 Algorithm Used
 Acquisition and      Data is collected automatically from the user's smartphone and connected devices
 Selection of Input   (Apple Health, Google Health, activity data, location, calendar data--when
 Data                 permissions are enabled). Users can also manually input data, including meal logs,
                      activities not detected by sensors (e.g., swimming), and weight measurements.
 Handling of Poor-    Only collected data is used; missing data is not imputed.
 Quality or
 Missing Data
 Human-AI             Data is processed exclusively by the AI system. No human intervention is
 Interaction in       involved in data processing. The AI autonomously selects goal recommendations,
 Data Handling        educational content, and the timing of notifications.
 Output of the AI     The AI system determines which notifications to send, when to send them, and the
 Intervention         content of messages, optimizing for behavior change based on user data.
 Role of AI           The AI does not engage in clinical decision-making. It provides behavioral
 Outputs in           nudges, goal-setting recommendations, and habit-forming prompts but does not
 Decision-Making      make clinical determinations.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 24 — reused layout text

```text
Sweetch Algorithm Overview

Algorithm Overview

Sweetch is an AI-powered health technology platform designed to predict, prevent, and manage chronic
diseases through hyper-personalized, real-time behavioral interventions. It functions as a fully automated
digital health coach that dynamically adapts to each user's needs, delivering just-in-time nudges, risk
insights, and motivation to support sustained healthy behaviors.

The Sweetch platform includes an adaptive behavioral intervention system that delivers personalized,
just-in-time adaptive interventions (JITAIs) encouraging health-promoting behaviors such as increased
physical activity and weight loss. Central to this system is a decision-making framework optimized for
environments with partial feedback and evolving user states.

The user journey begins with an initial setup phase. During onboarding, Sweetch collects foundational
data including the user’s health history, conditions, daily routines, and goals. Simultaneously, user
profiling engines analyze behavioral and physiological traits, habitual patterns, and contextual
information to generate a "digital blueprint"—a persona that forms the basis for personalization. An initial
engagement engine uses this data to calibrate early interactions and recommendations.

After the initial setup, the platform enters a continuous adaptation phase driven by Incremental Change
Engines (ICEs) and Incremental Change Programs (ICPs), which personalize each user’s care journey.
The core personalization framework includes a messaging module that tailors content and delivery by
analyzing factors like response time, patient profile, and user input—continually optimizing for
adherence. The user’s digital blueprint is updated dynamically as the system operates in a feedback loop:
Sense & Collect Data → Analyze → Respond (Plan, Adapt, Interact). This adaptive cycle refines
interventions in real time to deliver the most effective content, features, and goals for each user. User
profiling and context engines continuously supply ICEs with updated behavioral and contextual data,
allowing the system to evolve with the user's habits, routines, responsibilities, and preferences.

Personalization Framework

Sweetch’s adaptive mechanism operates by learning an engagement strategy that maximizes user
adherence and behavioral outcomes over time. Each interaction is treated as a decision point where the
system evaluates potential actions (e.g., content, tone, timing) and selects the most appropriate one based
on the user’s current context. This selection process balances testing new options and repeating successful
ones.

The core loop involves:

    •   State recognition: Ingesting contextual information (e.g., activity level, location, time of day)
    •   Action selection: Choosing an intervention from a predefined set (e.g., motivational message,
        physical activity prompt)
    •   Response assessment: Capturing user responses (e.g., engagement, step count increase)
    •   Strategy update: Adjusting future decisions based on observed outcomes, refining personalization
        continuously

Algorithm Structure


© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 25 — reused layout text

```text
The personalization engine in the Sweetch system was developed and pre-trained on pooled
(cross-user) historical data prior to the trial, but during the trial itself, the deployed algorithm
component operated at the individual level only.

Preclinical phase (training):

The model was initially developed using historical data from multiple users (anonymized and aggregated)
to estimate general responsiveness patterns to various intervention messages and timing strategies. This
approach allowed for learning baseline expected effects of intervention types on physical activity and app
engagement.

Deployment phase (trial):

In the live intervention, no cross-user data pooling was used for real-time decision-making. The engine
maintained separate state/action histories per participant. Each participant’s own past app usage and
behavioral activities determined the intervention policy updates for that individual. In other words, the
system personalized interventions purely on individual-level feedback once deployed.

Data Sources for Learning and Personalization

The algorithm is powered by multimodal data streams that enable context-aware personalization:

    1. User Behavior Data
          a. Interaction with app content.
          b. Activity completion
    2. Sensor Data
          a. Physical activity data from smartphones and wearables
          b. Location (e.g. home, work. venues like Gym, Supermarket, Restaurants)
          c. Time of day
    3. Health and Demographic Data
          a. Age, sex, clinical diagnoses
          b. Clinical parameters like BMI
          c. Goals achievements

Decision-Making Strategy

The adaptive mechanism relies on three foundational elements:

    a. Balancing Exploration and Exploitation

The system includes an explicit strategy for testing new intervention options while prioritizing effective
ones. A probabilistic approach was used to occasionally select less optimal messages to support continued
learning. This balance shifted over time, with more exploration early and more exploitation as the system
gathered user data. Each user followed an independent adaptation path.

    b. Response Feedback Loop

  The algorithm used a feedback system focused on two primary outcomes:


© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 26 — reused layout text

```text
        •    Physical activity, measured by active minutes, with diminishing returns to avoid over-
             promotion
        •    App engagement, measured by app open in proximity to prompt sending

The reward mechanism placed greater emphasis on physical activity to support health outcomes, while
engagement served as a proxy for adherence.

    c. Context-Aware Action Selection

 Decisions were informed by a rich set of user-specific and situational features, including:

    •       Temporal (e.g., time of day)
    •       Spatial (e.g., location)
    •       Behavioral (e.g., recent activity trends)
    •       Psychographic (e.g., response to prior interventions)

These variables shaped which actions were selected and when, ensuring high contextual relevance.

Action Options

Interventions varied in:

    •       Content: motivational tips, reminders, feedback
    •       Tone: encouraging, directive
    •       Timing: immediate or scheduled




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 27 — reused layout text

```text
Definitions of study cohorts

 Cohort                                   Definition
 Primary Analysis                         All randomized participants
 Per Protocol                             All randomized participants who completed 12-month study
                                          visit and did not use any prohibited medications (steroids,
                                          antihyperglycemics, weight loss medications)




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 28 — reused layout text

```text
Summary of methods for supplementary figures and tables not included in main manuscript

 Table/Figure         Population            Description of Method
 eFigure 1            –                     Screenshots of Personalized Push Notifications and
                                            Nutritional Support in Sweetch appintervention were
                                            obtained directly from Sweetch Health Ltd.
 eFigure 2            –                     Screenshots of Connected Health Tracking and
                                            Educational Content in the Sweetch App were obtained
                                            directly from Sweetch Health Ltd.
 eFigure 3            Randomized            The forest plot presents age-adjusted risk differences
                      Population            (aRD) (percentage points) with one-sided 95% CIs for the
                                            primary and secondary outcomes of diabetes risk reduction
                                            at 12 months. The reference line at -15 percentage points
                                            represents the non-inferiority margin. The AI-DPP
                                            intervention is considered non-inferior to Human-DPP if
                                            the one-sided CI does not cross this threshold. Risk
                                            difference adjusted for variables imbalanced at baseline
                                            (age). Negative aRD values indicate a lower outcome
                                            achievement frequency in the AI-DPP group compared to
                                            the Human-DPP group.
 eFigure 4            Randomized            The forest plot presents risk differences (percentage
                      Population            points) with one-sided 95% CIs for the secondary analysis
                                            (subgroup analysis by site, sex, age, baseline A1C, and
                                            BMI category). The reference line at -15 percentage points
                                            represents the non-inferiority margin. The AI-DPP
                                            intervention is considered non-inferior to Human-DPP if
                                            the one-sided CI does not cross this threshold. Negative
                                            risk difference values indicate a lower outcome
                                            achievement frequency in the AI-DPP group compared to
                                            the Human-DPP group. No multiplicity adjustment was
                                            applied as these analyses are exploratory and not intended
                                            for formal hypothesis testing.
 eTable 1             Randomized            The Sweetch application underwent multiple updates
                      Population AI-DPP     during the study. eTable 1a summarizes each version’s
                      group                 release date, key features, and eTable 1b summarizes the
                                            number (and percent) of AI-DPP participants who began
                                            the program in that version.
 eTable 2             Randomized            Participants assigned to the Human-DPP group received
                      Population Human-     their DPP program via synchronous Zoom sessions. Each
                      DPP group             participant was linked to one of four CDC-recognized DPP
                                            sites based on study site affiliation. The table summarizes
                                            each site’s name, location, CDC recognition status, and
                                            number (and percent) of Human-DPP participants
                                            assigned.
 eTable 3             Randomized            Baseline characteristics reported for full randomized
                      Population            cohort using methods as described for Main Manuscript,
                                            Table 1.
 eTable 4             Randomized            Proportions of participants meeting laboratory criteria for
                      Population, Per       DPP eligibility. DPP eligibility determined by: (1) Fasting
                      protocol              glucose 100–125 mg/dL within the past year, (2) Study
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 29 — reused layout text

```text
                                            A1C 5.7%–6.4% during baseline visit, (3) Clinic A1C
                                            5.7%–6.4% within the past year. Definitions of Study A1C
                                            and Clinic A1C are provided in the Methods section of the
                                            main manuscript. Chi-squared test used to compare
                                            differences in proportions and Wilcoxon rank-sum test
                                            used to compare continuous measures by group.
 eTable 5             Randomized            Baseline characteristics reported by randomization site
                      Population            using methods as described for the Main Manuscript,
                                            Table 1.
 eTable 6             Randomized            Baseline Characteristics by Baseline A1C Status,
                      Population            comparing A1C < 5.7% and 5.7% – 6.4%, using methods
                                            as described for Main Manuscript, Table 1.
 eTable 7             Randomized            Baseline Characteristics by Trial Completion Status,
                      Population            comparing study completers to study drop-outs, using
                                            methods as described for Main Manuscript, Table 1.
 eTable 8             –                     Frequency, handling method, and rationale for handling
                                            method of missing data was recorded.
 eTable 9             Randomized            In-window was defined as completing a 6-month visit
                      Population            within 168–196 days from baseline and a 12-month visit
                                            within 351–379 days from baseline. Days outside of
                                            window was calculated as the days from the relevant study
                                            window to the last day in that window. Mean days outside
                                            of window were summarized for participants who were
                                            outside of window by assigned group. Chi-squared test
                                            was used to compare differences in proportions of
                                            participants outside window. Wilcoxon rank-sum test used
                                            to compare continuous measures by group.
 eTable 10            Randomized            Proportion of patients who received prohibited
                      Population            antihyperglycemic, weight loss, or steroid medications by
                                            assigned group. GLP-1 receptor agonists were classified as
                                            antihyperglycemic agents for the purposes of
                                            classification. Information displayed by study group and at
                                            the participant level. Chi-squared test used for comparison
                                            between study groups.
 eTable 10b           Randomized            Percentage of participants on prohibited medications by
                      Population            study group.
 eTable 11            Per protocol          Baseline characteristics reported for the per protocol
                                            cohort by assigned group using methods as described for
                                            Main Manuscript, Table 1.
 eTable 12            Randomized            Participants who achieved the composite outcome were
                      Population            further classified according to which individual component
                                            outcomes they met (≥5% weight loss, ≥4% weight loss
                                            plus ≥150 minutes/week of physical activity, or ≥0.2%
                                            HbA1c reduction). Proportions were calculated as the
                                            number of participants achieving each unique combination
                                            of outcome components divided by the total number of
                                            participants who met the composite outcome, separately
                                            for each study arm and overall.
 eTable 13            Randomized            Participants within the Primary Analysis cohort who had a
                      Population            diabetes-range A1C during the 6-month and/or 12-month
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 30 — reused layout text

```text
                                            visit were recorded. These participants were marked
                                            having failed to achieve endpoint, regardless of body
                                            weight and physical activity improvements. Our study did
                                            not adjudicate the diagnosis of diabetes, which requires
                                            two confirmatory tests.
 eTable 14            Per Protocol          Changes in continuous measures of secondary endpoints
                                            (body weight, A1C) and weekly physical activity at 12
                                            months.
 eTable 15            Per protocol          Primary outcome and secondary binary outcomes analyzed
                                            within the per protocol population using statistical
                                            methods described in the Main Manuscript.
 eTable 16            Randomized            In the primary analysis, participants who did not return for
                      Population            their 12-month visit were classified as treatment failures.
                                            As a sensitivity analysis, missing 12-month outcome data
                                            were addressed using multiple imputation by chained
                                            equations, under the assumption that data were missing at
                                            random. The imputation model included study group,
                                            baseline values (weight, physical activity, A1C),
                                            demographic characteristics, and program engagement
                                            metrics (weeks wherein AI-DPP was used for AI-DPP
                                            participants and session attendance for Human-DPP
                                            participants, normalized within each group). Twenty
                                            imputed datasets were generated and combined using
                                            Rubin’s rules.
 eTable 17            Randomized            As a sensitivity analysis to assess potential violations of
                      Population            the missing at random assumption, we conducted a pattern
                                            mixture model analysis in which outcome achievement
                                            rates were differentially imputed for participants with
                                            missing 12-month data. Specifically, we assumed that all
                                            AI-DPP non-completers failed to achieve the primary
                                            outcome (0% success), while Human-DPP non-completers
                                            were assumed to have the same outcome achievement rate
                                            as observed among completers in that group (37.8%). This
                                            scenario imposes a directional bias against the AI-DPP and
                                            provides a conservative test of non-inferiority.
 eTable 18a           Randomized            For the individuals who did not wear their Actigraph
                      Population            monitor during their assigned periods, weekly physical
                                            activity was assumed to be 0 in the primary analysis
                                            (representing a “worst case” scenario). In this sensitivity
                                            analysis of the primary endpoint, we identified individuals
                                            who did not meet 100% Actigraph compliance and
                                            assumed that they would have achieved 150 weekly min of
                                            physical activity had they worn their Actigraph monitor.
                                            The table in this section displays the results of this “best-
                                            case” scenario sensitivity analysis.
 eTable 18b           Randomized            Given the limitations of the physical activity measurement
                      Population            described in the main manuscript, we conducted a
                                            sensitivity analysis of the primary outcome where we
                                            assumed all participants attained the 150 min/week
                                            physical activity guideline.
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 31 — reused layout text

```text
 eTable 19a           Randomized            Participants in the h-DPP group were referred to one of
                      Population            four distinct DPP programs. While all programs followed
                                            the CDC’s PreventT2 curriculum and fidelity standards,
                                            some heterogeneity in delivery may exist. In this
                                            sensitivity analysis, we clustered standard errors by DPP
                                            site, treating the four Human-DPPs as distinct clusters
                                            (clusters 1–4), and assigned all AI-DPP participants to a
                                            fifth cluster.
 eTable 19b           Randomized            To more granularly approximate potential groupings and
                      Population            shared exposure, we created a variable denoting the site
                                            and calendar month of randomization for each participant.
                                            This variable (cluster ID) reflects the fact that Human-DPP
                                            participants randomized in the same month and at the same
                                            DPP site were more likely to be referred to the same
                                            cohort, or AI-DPP participants randomized in the same
                                            month were more likely to be exposed to the same app
                                            version. In this sensitivity analysis, we clustered standard
                                            errors by cluster ID.
 eTable 18            Randomized            Participants within the Primary Analysis cohort who had a
                      Population            diabetes-range A1C during the 6-month and/or 12-month
                                            visit were recorded. These participants were marked
                                            having failed to achieve endpoint, regardless of body
                                            weight and physical activity improvements. Our study did
                                            not adjudicate the diagnosis of diabetes, which requires
                                            two confirmatory tests.
 eTable 19            Per protocol          Changes in continuous measures of secondary endpoints
                                            (body weight, A1C) and weekly physical activity at 12
                                            months.
 eTable 20a           Randomized            Adverse events reported by category, grade, relatedness to
                      Population            the participants’ assigned intervention, and by condition.
                                            Tables reported number of participants with at least one
                                            adverse event by study group, and frequency of adverse
                                            events.
 eTable 20b           Randomized            Adverse events reported by grade. The table reports
                      Population            number of adverse events in each study group.
 eTable 20c           Randomized            Adverse events reported by relatedness to the participants’
                      Population            assigned intervention. The table reports number of adverse
                                            events in each study group.
 eTable 20d           Randomized            Adverse events reported by condition and grade and
                      Population            assigned intervention.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 32 — reused layout text

```text
SUPPLEMENTARY FIGURES AND TABLES

eFigure 1. Screenshots of Personalized Push Notifications and Nutritional Support in Sweetch App

 A. Personalized Push Notifications




 B. Advanced photo-based meal analysis / Nutrition Tracking




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 33 — reused layout text

```text
eFigure 2 Screenshots of Connected Health Tracking and Educational Content in Sweetch App

    A. Weight and Activity Tracking / Connected Devices




    B. Educational Content




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.

```

### PDF page 34 — reused native captions; visual numbers above

```text
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.
eFigure 3. Forest Plot of Adjusted Binary Outcome Differences

1The forest plot presents age-adjusted risk differences (percentage points) with one-sided 95% CIs for the primary
and elements of the composite primary analysis at 12 months. The reference line at -15 percentage points represents
the non-inferiority margin. The AI-DPP intervention is considered non-inferior to Human-DPP if the one-sided CI
does not cross this threshold. Negative RD values indicate a lower outcome achievement frequency in the AI-DPP
group compared to the Human-DPP group.
295% confidence intervals for elements of the composite primary analysis outcomes are presented for descriptive
purposes only. No multiplicity adjustment was applied as these analyses are exploratory and not intended for formal
hypothesis testing.
3Analysis of the 0.2% A1C reduction outcome applies only for participants with A1C in the prediabetes range at the
study baseline visit (AI-DPP: n=130; H-DPP: n=130)

```

### PDF page 35 — reused native captions; visual numbers above

```text
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI
training, and similar technologies.
eFigure 4 Exploratory Subgroup Analysis of Primary Outcome

1The forest plot presents risk differences (percentage points) with one-sided 95% CIs for the primary analysis. The
reference line at -15 percentage points represents the non-inferiority margin. The AI-DPP intervention is considered
non-inferior to Human-DPP if the one-sided CI does not cross this threshold.
2Negative risk difference values indicate a lower outcome achievement frequency in the AI-DPP group compared to
the Human-DPP group.
395% confidence intervals for subgroup analyses are presented for descriptive purposes only. No multiplicity
adjustment was applied as these analyses are exploratory and not intended for formal hypothesis testing.4BMI
Classification: Overweight: BMI 25.0–29.9 kg/m2; Class I Obesity: BMI 30.0–34.9 kg/m2; Class II Obesity: BMI
35.0–39.9 kg/m2; Class III Obesity: BMI ≥40.0 kg/m2.

```
