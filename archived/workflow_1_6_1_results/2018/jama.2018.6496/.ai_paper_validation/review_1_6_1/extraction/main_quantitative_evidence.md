# Main-paper quantitative evidence map

Scope: DOC-001, jama_driver_2018_oi_180054.pdf, all physical PDF pages 1-11 (printed 2179-2189). All content has role REPORT. This artifact reconstructs evidence only; it assigns no findings or candidate judgments. Internal M IDs are mapper IDs for later canonical N/S assignment. B denotes randomized bougie and T randomized endotracheal tube + stylet unless explicitly stated otherwise. Counts have denominator B=381, T=376 unless a row prints its own denominator. Differences are B minus T; proportions/differences are percentage points, durations seconds, HRs dimensionless. All intervals are printed 95% CIs unless explicitly IQR/SD. Inferential families are linked to methods M006-M009 below. No rates, person-time, reported standard errors or test-statistic values appear in this main paper.

## Provenance and complete page coverage

Read completely: QUALITY_CONTROL_SCOPE.md; workflow_1_6_1/review_contract.md; this run's source/evidence inventories, coverage manifest and tooling record. Used source-matched reusable A001 native text and A004 layout text, Poppler 25.03.0 correspondence as established by curator. Form-feed records locate exact physical pages. Visually inspected source-matched 200-dpi rendered pages A011-A015 (physical pp.5-9), including all table-column alignment and Figure 2 curves/censoring ticks. Native/layout text suffices on other pages; p.11 has no quantitative trial display. No OCR, new extraction, fallback, GPU, outside source or earlier review conclusions used. Sources and reusable derivatives were untouched.

| Physical page | Direct source link | Mapped content | Coverage |
|---|---|---|---|
| 1 | [PDF p.1](../../../jama_driver_2018_oi_180054.pdf#page=1) | Abstract population, allocation, outcomes and inferential claims; matching map M001, M074-M079, M101 | COMPLETE |
| 2 | [PDF p.2](../../../jama_driver_2018_oi_180054.pdf#page=2) | Key Points, eligibility, outcome subgroup ascertainment, randomization; background numbers separated | COMPLETE |
| 3 | [PDF p.3](../../../jama_driver_2018_oi_180054.pdf#page=3) | Randomization strata, intervention, measurement, outcome definitions, power and statistical methods M002-M008 | COMPLETE |
| 4 | [PDF p.4](../../../jama_driver_2018_oi_180054.pdf#page=4) | Figure 1 all branches/footnotes M010-M018; statistical-method continuation M006-M009; enrollment/operators M019 | COMPLETE |
| 5 | [PDF p.5](../../../jama_driver_2018_oi_180054.pdf#page=5) | Table 1 all rows M020-M049; narrative results, HRs M091-M092, process M099 | COMPLETE |
| 6 | [PDF p.6](../../../jama_driver_2018_oi_180054.pdf#page=6) | Table 2 all rows and footnotes M050-M073 | COMPLETE |
| 7 | [PDF p.7](../../../jama_driver_2018_oi_180054.pdf#page=7) | Table 3 all results and footnotes M074-M090; rescue narrative M098-M099 | COMPLETE |
| 8 | [PDF p.8](../../../jama_driver_2018_oi_180054.pdf#page=8) | Figure 2 complete axes/risk counts/caption M091; Table 4 complete M093-M098; complication narrative and discussion matches | COMPLETE |
| 9 | [PDF p.9](../../../jama_driver_2018_oi_180054.pdf#page=9) | Table 5 all rows M100-M109; discussion/limitations M110 | COMPLETE |
| 10 | [PDF p.10](../../../jama_driver_2018_oi_180054.pdf#page=10) | Limitations and conclusions linked M110; article information/references have no additional trial quantities | COMPLETE |
| 11 | [PDF p.11](../../../jama_driver_2018_oi_180054.pdf#page=11) | References only; no applicable additional quantitative trial relationship | COMPLETE_NO_ADDITIONAL_RELATIONSHIP |

## Design, analysis and denominators

| ID | Exact source location | Reconstructed relationship/specification |
|---|---|---|
| M001 | p.1 abstract; pp.2,4-5 enrollment | 757 randomized; 757 (100%) completed; B381/T376; 380 with at least one difficult-airway characteristic; mean age46 y; women230 (30%). Dates September2016-August2017. Eligibility age≥18, emergency orotracheal intubation using Macintosh blade; direct/video allowed. Primary subgroup B198/T182. |
| M002 | pp.2-3 Patient Selection/Randomization | Allocation1:1; permuted random blocks2,4,6,8,10; strata obesity or cervical immobilization vs neither. All difficult-airway characteristics elicited after intubation, subjectively without formal definition: fluids obscuring view, obstruction/edema, obesity, short neck, small mandible, large tongue, facial trauma, cervical immobilization. |
| M003 | p.3 Trial Outcomes; p.7 footnotes | First-attempt success = successful tube placement with first device passed during first laryngoscope insertion. No device passed on first insertion counts failure. Duration from blade insertion to removal. Hypoxemia saturation<90%, or decrease>10% if initial saturation<90%; real-time pulse oximetry during or within1min after attempt. Primary success among ≥1 difficult characteristic; secondary overall success, success without hypoxemia, duration, esophageal intubation, hypoxemia. |
| M004 | p.3 Statistical Analysis | Power:374 difficult-airway patients,80%, absolute difference9%, expected95% vs86%,2-sided alpha.05. Sample-size formula/software/continuity correction/allocation assumption beyond randomization1:1 not specified. No a priori overall-cohort calculation; expected benefit without difficulty<5%, infeasible sample. Trial stopped when >374 difficult-airway patients enrolled; achieved380. All enrolled in final analysis. |
| M005 | p.3 Measurements/procedures | Outcome collection randomization until1min after end of first attempt; stopwatch duration. Unblinded physicians/associates. Discrepant success adjudicated with retrospective video; blinded radiograph abstractor assessed pneumothorax. Intervention70cm,15French/5mm single-use straight coudé bougie; tube/stylet25°-35° bend, straight-to-cuff. Rescue device selection discretionary after initial failure. |
| M006 | pp.3-4 Statistical Analysis | Principal intention-to-treat analyses: primary difficult-airway subset, overall secondary and other secondary outcomes; between-group difference of proportions or median difference with95%CI. Continuous effects Hodges-Lehmann median between-group differences/95%CIs; binary significance chi-square; continuous Wilcoxon rank sum; all2-sided.05. Methods for arm percentage CI and difference CI not named. |
| M007 | p.4 Statistical Analysis | Difficult-airway effect modification tested by interaction. Unplanned exploratory clinical-interest subgroups, interaction for each; no multiple-comparison corrections. Interaction test model/link/scale not specified. |
| M008 | pp.4-5 Statistical Analysis/Secondary Outcomes; p.8 Figure2; pp.9-10 interpretation | First-attempt duration Kaplan-Meier, log-rank; unadjusted Cox proportional hazards HR for first-attempt success, T reference. Schoenfeld residuals and visualization assess proportionality. Failed attempt endings indicated by censoring ticks. Assumption not upheld; limitations explicitly restrict interpretation. Event=success, time=attempt duration; patient-level times/censor table not supplied. |
| M009 | p.4 Statistical Analysis; p.5 Primary Outcome | Post hoc clustering by individual physician analysis, details/results deferred eTable1 in Supplement2. Missing data remain missing, no imputation. One midpoint futility-only interim under DSMB; no superiority assessment and no alpha adjustment. Stata15.1. Exact futility rule/results deferred Supplement2. |

## Participant flow: Figure 1, PDF p.4

| ID | Branch or footnote | Complete numbers/context |
|---|---|---|
| M010 | Eligibility partition | Assessed3768; excluded3011; randomized/enrolled757; enrolled with difficult characteristic380. |
| M011 | Not meeting inclusion criteria | 2938: not intubated2785; age<18 61; prisoners28; known upper-airway distortion27; non-Macintosh22; known/expected pregnancy15. |
| M012 | Eligible not randomized | 73: too rapid30; no research staff20; physician refused16; patient/representative declined6; unknown1. |
| M013 | B allocation | Randomized381: received randomized372; tube+stylet first4; no device5. Difficult subgroup198: received randomized191; tube first2; no device5. Primary analysis198; subgroup analysis381. |
| M014 | T allocation | Randomized376: received randomized345; bougie first25; no device6. Difficult subgroup182: received randomized161; bougie first18; no device3. Primary analysis182; subgroup analysis376. |
| M015 | Physician refusal footnote a | Data15/16 refused patients; bougie all15; first-attempt success14/15 (93%); reasons anticipated difficulty/rapid intubation. These nonrandomized patients not trial denominator. |
| M016 | Crossover footnote a | Of25 T patients with bougie-first deviation,23 successes (92%). Reasons combined with refusal above. p.10 repeats7% T bougie-first. |
| M017 | No-device footnote b | All11 (B5/T6) no passage after initial laryngoscope insertion are first-attempt failures, intubated on later attempts. Distinguishes first-device attempt from laryngoscope insertion for Table4. |
| M018 | Allocation-adherence narrative pp.4-5 | 98% B,92% T. Figure1 distinguishes intervention-as-randomized from no-device category; all participants included in ITT. |
| M019 | Trial physicians p.4 | 51 unique physicians;44 intubated B≥1 and40 T≥1; intubations/physician median8,IQR1-26,range1-61. Groups overlap. |

## Baseline: Table 1, PDF p.5

Values B then T; percentages use381/376 unless explicit. Characteristics may overlap. No tests/effects displayed.

| ID | Row | B | T |
|---|---|---|---|
| M020 | Age mean(SD),y | 46(18) | 46(18) |
| M021 | Men | 272(71%) | 255(68%) |
| M022 | BMI mean(SD),kg/m² | 28(7) | 28(7) |
| M023 | Heart rate mean(SD),beats/min | 108(25 [closing parenthesis absent in print] | 107(25) |
| M024 | Systolic pressure mean(SD),mmHg | 135(30) | 134(32) |
| M025 | Initial oxygen saturation median(IQR),% | 99(95-100) | 99(96-100) |
| M026 | Initial saturation<90% | 44/352(13%) | 40/344(12%) |
| M027 | Initial saturation<80% | 21/352(6%) | 11/344(3%) |
| M028 | Medical intubation | 318(83%) | 315(84%) |
| M029 | Altered mental status | 185(49%) | 173(46%) |
| M030 | Cardiac arrest | 32(8%) | 23(6%) |
| M031 | Septic shock | 21(6%) | 27(7%) |
| M032 | Seizure | 20(5%) | 28(7%) |
| M033 | Asthma/COPD/heart failure/pneumonia | 16(5%) | 23(7%) |
| M034 | Other medical | 44(14%) | 41(13%) |
| M035 | Trauma indication | 63(17%) | 61(16%) |
| M036 | Traumatic brain injury | 29(8%) | 23(6%) |
| M037 | Other trauma | 34(9%) | 38(10%) |
| M038 | Any difficult-airway characteristic | 198(52%) | 182(48%) |
| M039 | Blood/vomit in airway | 83(22%) | 67(18%) |
| M040 | Obesity judged by physician | 57(15%) | 68(18%) |
| M041 | Cervical immobilization | 49(13%) | 36(10%) |
| M042 | Large tongue | 31(8%) | 34(9%) |
| M043 | Short neck | 28(7%) | 28(7%) |
| M044 | Facial trauma | 20(5%) | 12(3%) |
| M045 | Small mandible | 14(4%) | 18(5%) |
| M046 | Airway obstruction/edema | 8(2%) | 4(1%) |
| M047 | Initial vital-sign missingness footnote b | Heart rate29; pressure94; saturation19 | Heart rate32; pressure91; saturation24 |
| M048 | Footnote b totals/measurement | Missing heart rate61,pressure185,saturation43; first vitals after enrollment before intubation; absent monitor/unreliable waveform. | BMI measured chart weight/height, kg/m². |
| M049 | Obesity footnote c | BMI≥30 but physician did not classify obese64 | Same68;132 combined meanBMI34; physician-obese meanBMI37. |

## Process measures: Table 2, PDF p.6

Each ID contains all displayed numeric and inferential relationships in its row. Differences are proportions B minus T, except saturation median difference. Binary tests chi-square; saturation Wilcoxon/Hodges-Lehmann per M006. B/T denominator381/376 except explicit fractions. All intervals95%CI.

| ID | Measure | B | T | Difference (CI) | P |
|---|---|---|---|---|---|
| M050 | Non-rebreather | 267(70%) | 276(73%) | -3(-10 to3) | .31 |
| M051 | Flush-rate among non-rebreather | 204/267(76%) | 210/276(76%) | 0(-7 to7) | .93 |
| M052 | Bag/mask | 47(12%) | 37(10%) | 2(-2 to7) | .27 |
| M053 | Noninvasive positive-pressure | 18(5%) | 24(6%) | -2(-5 to2) | .32 |
| M054 | Extraglottic | 27(7%) | 17(5%) | 3(-1 to6) | .13 |
| M055 | Any sedative | 338(89%) | 341(91%) | -2(-6 to2) | .37 |
| M056 | Etomidate | 332(87%) | 333(89%) | -1(-6 to3) | .54 |
| M057 | Ketamine | 4(1%) | 4(1%) | 0(-1 to1) | .99 |
| M058 | Any neuromuscular blockade | 366(96%) | 367(98%) | -2(-4 to1) | .23 |
| M059 | Succinylcholine | 214(56%) | 229(61%) | -5(-12 to2) | .19 |
| M060 | Rocuronium | 147(39%) | 137(36%) | 2(-5 to9) | .54 |
| M061 | Sniffing position | 222(58%) | 244(65%) | -7(-14 to0) | .06 |
| M062 | Neutral cervical spine | 117(31%) | 96(26%) | 5(-1 to12) | .11 |
| M063 | Extension without sniffing | 39(10%) | 32(9%) | 2(-2 to6) | .42 |
| M064 | Start oxygen saturation median(IQR),% | 100(98-100) | 100(98-100) | 0(0 to0) | .60 |
| M065 | Start saturation<90% | 22/360(6%) | 27/343(8%) | -2(-6 to2) | .36 |
| M066 | Start saturation<80% | 13/360(4%) | 8/343(2%) | 1(-1 to4) | .32 |
| M067 | Apneic nasal-cannula oxygenation | 221(58%) | 227(60%) | -2(-9 to5) | .51 |
| M068 | Operator senior/fellow PGY≥3 | 318(83%) | 334(89%) | -5(-10 to0) | .03 |
| M069 | Operator junior PGY≤2 | 57(15%) | 37(10%) | 5(0 to10) | .03 |
| M070 | Faculty | 8(2%) | 5(1%) | 1(-1 to3) | .42 |
| M071 | C-MAC Macintosh | 362(95%) | 366(97%) | -2(-5 to0) | .10 |
| M072 | GlideScope Titanium MAC | 12(3%) | 8(2%) | 1(-1 to3) | .38 |
| M073 | Macintosh direct | 7(2%) | 2(1%) | 1(0 to3) | .10 |

The next rows have suffixed internal IDs so all main relationships remain independently addressable.

| ID | Measure | B | T | Difference (CI) | P |
|---|---|---|---|---|---|
| M073a | Screen never used | 218/377(58%) | 182/372(49%) | 9(2 to16) | .02 |
| M073b | Screen entire attempt | 78/377(21%) | 90/372(24%) | -4(-9 to2) | .25 |
| M073c | Screen during device passage | 75/377(20%) | 98/372(26%) | -6(-12 to0) | .04 |
| M073d | Best view grade1 | 269/373(72%) | 269/359(75%) | -3(-9 to4) | .39 |
| M073e | Grade2 | 74/373(20%) | 62/359(17%) | 3(-3 to8) | .39 |
| M073f | Grade3 | 27/373(7%) | 23/359(6%) | 1(-3 to4) | .66 |
| M073g | Grade4 | 3/373(1%) | 5/359(1%) | -1(-2 to1) | .44 |
| M073h | Actual bougie first | 372(98%) | 25(7%) | 91(88 to94) | <.001 |
| M073i | Actual tube+stylet first | 4(1%) | 345(92%) | -91(-94 to-88) | <.001 |
| M073j | No device first | 5(1%) | 6(2%) | 0(-2 to1) | .75 |
| M073k | Footnote missingness/denominators | Start saturation missing21; screen missing4; view missing8 | Start saturation missing33; screen missing4; view missing17 | Initial/start/during saturation are distinct measurements | — |
| M073l | Footnote operator/medications | No-sedative78 total;53(68%) prehospital sedative/cardiac arrest, B31/T22. Other sedatives and paralytics not listed. Final operator shown;8 operator changes,4/group. | Sniffing=neck flexion/atlanto-occipital extension; apneic cannula left during intubation. View grades1 all/most glottis,2 posterior/arytenoid only,3 epiglottis only,4 neither. | — | — |

## Trial outcomes: Table 3, PDF p.7

Binary percentages and arm CIs separately displayed. Median rows contain median(IQR), not numerator/denominator. Effects95%CI; binary difference percentage points, continuous difference Hodges-Lehmann seconds. Main P binary chi-square/continuous Wilcoxon per M006; interaction method unspecified M007. NA printed for all-patient interaction analyses per footnote a. Subgroups labeled unplanned. Immediate source/narrative occurrences are mapped in last column.

| ID | Outcome/population | B count or median; % (CI) | T count or median; % (CI) | Difference (CI) | P; interaction P | Matches |
|---|---|---|---|---|---|---|
| M074 | Primary success, difficult-airway n380 | 191/198;96(93 to99) | 150/182;82(76 to88) | 14(8 to20) | <.001;.36 | Abstractp1,Key Pointsp2,Primaryp5,Discussionp8/10 |
| M075 | Difficult-airway success without hypoxemia | 156/191;82(76 to87) | 123/177;69(63 to76) | 12(3 to21) | .006;.61 | Abstract outcome listp1 |
| M076 | Difficult-airway duration,s | 39(29 to52) | 40(27 to63) | -1(-6 to3) | .50;.17 | Figure2 uses event-time method instead M091 |
| M077 | All-patient success n757 | 373/381;98(96 to99) | 328/376;87(83 to90) | 11(7 to14) | <.001;NA | Abstractp1,Secondaryp5,Discussionp8-10 |
| M078 | All-patient success without hypoxemia | 317/371;85(81 to89) | 282/366;77(72 to81) | 8(3 to14) | .003;NA | Abstract outcome listp1 |
| M079 | All-patient duration,s | 38(29 to51) | 36(25 to54) | 1(4 to-1) | .24;NA | Abstractp1 says38vs36 no significant difference; visualp7 confirms printed CI order4 to-1 |
| M080 | Blood/vomit success n150 | 79/83;95(88 to99) | 55/67;82(71 to90) | 13(3 to23) | .01;.31 | BaselineM039 |
| M081 | Cervical immobilization success n85 | 49/49;100(93 to100) | 28/36;78(61 to90) | 22(9 to36) | .001;.25 | Narrativep5 100vs78;baselineM041 |
| M082 | Obesity success n125 | 55/57;96(88 to100) | 51/68;75(63 to85) | 21(10 to33) | .001;.63 | Narrativep5 96vs75;baselineM040 |
| M083 | No difficult characteristic success n377 | 182/183;99(97 to100) | 178/194;92(87 to95) | 8(4 to12) | <.001;.36 | Narrativep5;Discussionp8/10 |
| M084 | C-MAC success all patients | 356/362;98(96 to99) | 321/366;88(84 to91) | 11(7 to14) | <.001;.46 | Discussionp8-9;processM071 |
| M085 | Grade1 success | 265/269;99(96 to100) | 258/269;96(93 to98) | 3(0 to5) | .07;.04 | M073d |
| M086 | Grade2 success | 72/74;97(91 to100) | 41/62;66(53 to78) | 31(19 to44) | <.001;.13 | M073e |
| M087 | Grade3 success | 26/27;96(81 to100) | 11/23;48(27 to69) | 48(27 to71) | <.001;.17 | M073f |
| M088 | Grade4 success | 3/3;100(29 to100) | 2/5;40(5 to85) | 60(17 to100) | .09;.78 | M073g |
| M089 | By actual first device,all757 | 392/402;98(95 to99) | 309/355;87(83 to90) | 10(7 to14) | <.001;NA | No-device patients assigned randomized device for this row,footnotee |
| M090 | Duration only successful first attempts,s | 38(29 to51) | 34(23 to47) | 4(2 to7) | <.001;.03 | Narrativep5 labels unplanned post hoc subgroup |

Table3 footnote b repeats M003 hypoxemia and incomplete valid pulse waveforms. Footnote c duration blade insertion/removal. Footnote d short neck,small mandible,obstruction/edema,facial trauma,large tongue success subgroups not displayed because too few patients for valid group comparison; no numerical results supplied. Denominators for duration medians not printed. p.5 narrative combines Cormack-Lehane grades2-4: success97%vs60%; this corresponds to displayed grade-specific counts B101/104,T54/90 (derived grouping only, not a printed extra estimate/CI/P). Immediate narrative says no significant difficult-airway interaction,P.36, matchingM074/M083.

## Time-to-success relationships

| ID | Location/population | Printed statistical relationships and figure data |
|---|---|---|
| M091 | p.5 narrative;p.8 Figure2; difficult-airway n380 | HR first-attempt success B vs T1.29(1.04-1.60),log-rankP.02. X time seconds0,30,60,90,120,150,180;Y successfully intubated%0,20,40,60,80,100. Risk counts at these times B198,146,37,13,3,3,0;T182,127,56,9,3,3,1. Orange B curve below T briefly around30s,above after roughly40s; B approaches100%,Tplateau below100%. Vertical ticks indicate ≥1 failed attempt ending,not successes. Caption: PH not upheld. Curves are KM cumulative success,not raw endpoint proportions; exact unprinted time-event values unavailable. |
| M092 | p.5 narrative;all757 | SupplementeFigure1: HRBvsT1.12(.97-1.30),log-rankP.12; no significant between-group difference. Same unadjusted Cox/reference. Main p.9 describes duration shorter on Cox basis for difficult group,similar overall; pp.9-10 explicitly PH limitation. |

## Failed-attempt rescue: Table 4, PDF p.8

Population B8/T48 first-attempt failures; percentages use these denominators. Same laryngoscope insertion can contain a second device after first-device failure. No statistical effects/tests shown.

| ID | Successful technique | B | T |
|---|---|---|---|
| M093 | Same first insertion,bougie | 0 | 34(71%) |
| M094 | Same first insertion,tube+stylet | 0 | 1(2%) |
| M095 | Second insertion,bougie | 6(75%) | 6(13%) |
| M096 | Second insertion,tube+stylet | 0 | 3(6%) |
| M097 | Second attempt,different device | 0 | 2(4%);1 intubating laryngeal mask,1 cricothyrotomy |
| M098 | >2 attempts | 2(25%) | 2(4%);3of4 third-attempt bougie;fourth tracheal abnormality,several attempts4.0mm stylet/tube |

M094 footnote: T patient's bougie first failed,tube+stylet succeeded on same insertion. Narrativep7:56(7%) initial failures, rescue bougie49,intubating laryngeal mask1,cricothyrotomy1; narrative does not assert that these exhaust all56. Rescue table partitions56 across rows.

## Other process outcomes and complications

| ID | Source | Relationship |
|---|---|---|
| M099 | pp.5,7 Other Outcomes; p.9 discussion | Bougie used444 patients across trial;tracheal clicks404(91%),hold-up283(64%),tube resistance31(7%). Rotation90° counterclockwise/readvancement successful all except1;that1 later successful bougie. Hold-up occurs depthabout30cm;absence by35cm indicates esophageal position. Discussionp9 resistance7% phrased bougie-group intubations; exact per-randomized-arm resistance count not supplied. |

Table5 PDFp9 below: counts denominatorB381/T376 except hypoxemia fractions; differencepercentage points,95%CI; chi-squareP underM006. Direct airway injury has blank difference/P cells,not inferred values.

| ID | Complication | B | T | Difference (CI) | P |
|---|---|---|---|---|---|
| M100 | Any complication | 66(17%) | 63(17%) | 1(-5 to6) | .83 |
| M101 | Hypoxemia | 47/371(13%) | 50/364(14%) | -1(-6 to4) | .67 |
| M102 | Pneumothorax diagnosed after intubation | 9(2%) | 9(2%) | 0(-2 to2) | .99 |
| M103 | Pneumothorax without clear cause | 1(<1%) | 3(1%) | -1(-2 to1) | .31 |
| M104 | Lip laceration | 7(2%) | 3(1%) | 1(-1 to3) | .21 |
| M105 | Witnessed aspiration | 3(1%) | 1(<1%) | 1(-1 to2) | .32 |
| M106 | Iatrogenic oropharynx/perilaryngeal bleeding | 2(1%) | 2(1%) | 0(-1 to1) | .99 |
| M107 | Dental trauma | 1(<1%) | 1(<1%) | 0(-1 to1) | .99 |
| M108 | Esophageal intubation | 0 | 3(1%) | -1(-2 to0) | .08 |
| M109 | Direct airway injury | 0 | 0 | blank | blank |

M100 footnotea composite counts each person once even if>1 complication. M101 footnoteb saturation definitionM003 and unavailable valid waveforms. M103 footnotec clear causes chest trauma/rib fractures or chest-compression resuscitation;none of4 unexplained pneumothoraces had definitively identified etiology. Abstractp1 and narrativep8 repeat hypoxemia13vs14% no significant difference; narrativep8 repeats esophageal0vs3(1%).

## Remaining matched claims, background and absent inputs

M110 is the report-interpretation relationship: pp.9-10 primary subgroup determined postrandomization because not all difficult-airway characteristics ascertainable before intubation; benefit described both with/without difficulty; T bougie-first deviations7%,higher success in deviations than T overall; PH assumption not upheld limits duration interpretation; conclusion significantly higher success with provisional generalizability. pp.8-9 C-MAC use>96% combined and B C-MAC success98%;nearly one-third incomplete grade2-4 views;screen use narrative mapsM073a-c. No independent physician-level effect or corrected HR printed in main report.

Background numerical statements were read and isolated from trial arithmetic: p.2 estimated310000 US intubations in2014;registry2002-2012 adverse eventsabout12%,initial success85%/failure15%;routine bougie<5%;estimated difficult-airway prevalence60%;institution109000 annual visits. p.8 comparison studies78%vs current82%,91%vs current92%,>13000 intubations success86.9%vs current87%,meta-analysis>42000 success84.1%,external C-MAC91%vs current98%;p.9 helicopter protocol>98%. No external literature was accessed or these historical quantities treated as trial observations. p.10-11 reference years/volumes/pages/publication dates and administrative numbers are fully inspected and have no additional applicable trial relationship.

Inputs not supplied in main source: patient-level event times and pulse-oximetry records; exact CI construction for binary estimates/differences; sample-size calculation formula and correction; interaction model/link; numerical clustering analysis (deferred supplied supplement); interim cutoff/calculations (deferred supplied supplement); continuous-row contributing counts; overlap among individual difficult-airway features. These are mapping limits on mechanical reproduction, not missing page coverage or findings.

Total:122 internal relationship records (M001-M110 plus M073a-M073l). Each table result includes every displayed component rather than treating component numbers as separate issues. All11 assigned units are mapped;no fresh-required units;no scientific coverage gaps. Inferential relationships: design/methodM002-M009, processM050-M073/M073a-j,outcomeM074-M090,timeM091-M092,complicationM100-M108; report interpretationM110. Numeric-only relationships remain available for complete numeric review. The next annex preserves full source-linked page text for exact narrative/footnote wording, without importing old review outputs.

## Page-by-page source-linked layout transcription annex

### DOC-001 physical PDF page 1

Source: [jama_driver_2018_oi_180054.pdf](../../../jama_driver_2018_oi_180054.pdf#page=1)

```text
                      Research


                    JAMA | Original Investigation

                    Effect of Use of a Bougie vs Endotracheal Tube and Stylet
                    on First-Attempt Intubation Success Among Patients
                    With Difficult Airways Undergoing Emergency Intubation
                    A Randomized Clinical Trial
                    Brian E. Driver, MD; Matthew E. Prekker, MD; Lauren R. Klein, MD; Robert F. Reardon, MD; James R. Miner, MD; Erik T. Fagerstrom, BA;
                    Mitchell R. Cleghorn, BS; John W. McGill, MD; Jon B. Cole, MD


                                                                                                                                            Supplemental content
                       IMPORTANCE The tracheal tube introducer, known as the bougie, is typically used to aid                               CME Quiz at
                       tracheal intubation in poor laryngoscopic views or after intubation attempts fail. The effect of                     jamanetwork.com/learning
                       routine bougie use on first-attempt intubation success is unclear.                                                   and CME Questions page
                                                                                                                                            2229
                       OBJECTIVE To compare first attempt intubation success facilitated by the bougie vs the
                       endotracheal tube + stylet.

                       DESIGN, SETTING, AND PATIENTS The Bougie Use in Emergency Airway Management (BEAM)
                       trial was a randomized clinical trial conducted from September 2016 through August 2017 in
                       the emergency department at Hennepin County Medical Center, an urban, academic
                       department in Minneapolis, Minnesota, where emergency physicians perform all
                       endotracheal intubations. Included patients were 18 years and older who were consecutively
                       admitted to the emergency department and underwent emergency orotracheal intubation
                       with a Macintosh laryngoscope blade for respiratory arrest, difficulty breathing,
                       or airway protection.

                       INTERVENTIONS Patients were randomly assigned to undergo the initial intubation attempt
                       facilitated by bougie (n = 381) or endotracheal tube + stylet (n = 376).

                       MAIN OUTCOMES AND MEASURES The primary outcome was first-attempt intubation success
                       in patients with at least 1 difficult airway characteristic (body fluids obscuring the laryngeal
                       view, airway obstruction or edema, obesity, short neck, small mandible, large tongue, facial
                       trauma, or the need for cervical spine immobilization). Secondary outcomes were
                       first-attempt success in all patients, first-attempt intubation success without hypoxemia,
                       first-attempt duration, esophageal intubation, and hypoxemia.

                       RESULTS Among 757 patients who were randomized (mean age, 46 years; women, 230
                       [30%]), 757 patients (100%) completed the trial. Among the 380 patients with at least 1
                       difficult airway characteristic, first-attempt intubation success was higher in the bougie group
                       (96%) than in the endotracheal tube + stylet group (82%) (absolute between-group
                       difference, 14% [95% CI, 8% to 20%]). Among all patients, first-attempt intubation success
                                                                                                                                        Author Affiliations: Department of
                       in the bougie group (98%) was higher than the endotracheal tube + stylet group (87%)                             Emergency Medicine, Hennepin
                       (absolute difference, 11% [95% CI, 7% to 14%]). The median duration of the first intubation                      County Medical Center, Minneapolis,
                       attempt (38 seconds vs 36 seconds) and the incidence of hypoxemia (13% vs 14%) did not                           Minnesota (Driver, Prekker, Klein,
                                                                                                                                        Reardon, Miner, Fagerstrom, McGill,
                       differ significantly between the bougie and endotracheal tube + stylet groups.
                                                                                                                                        Cole); Department of Medicine,
                                                                                                                                        Division of Pulmonary and Critical
                       CONCLUSIONS AND RELEVANCE In this emergency department, use of a bougie compared with                            Care, Hennepin County Medical
                       an endotracheal tube + stylet resulted in significantly higher first-attempt intubation success                  Center, Minneapolis, Minnesota
                                                                                                                                        (Prekker); University of Minnesota
                       among patients undergoing emergency endotracheal intubation. However, these findings should
                                                                                                                                        School of Medicine, Minneapolis
                       be considered provisional until the generalizability is assessed in other institutions and settings.             (Cleghorn).
                                                                                                                                        Corresponding Author: Brian E.
                       TRIAL REGISTRATION clinicaltrials.gov Identifier: NCT02902146                                                    Driver, MD, Department of
                                                                                                                                        Emergency Medicine, 701 Park Ave,
                       JAMA. 2018;319(21):2179-2189. doi:10.1001/jama.2018.6496                                                         Mail Stop R2, Minneapolis, MN 55415
                       Published online May 16, 2018.                                                                                   (briandriver@gmail.com).



                                                                                                                                                                  (Reprinted) 2179
                                                           © 2018 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### DOC-001 physical PDF page 2

Source: [jama_driver_2018_oi_180054.pdf](../../../jama_driver_2018_oi_180054.pdf#page=2)

```text
                 Research Original Investigation                                             Comparison of Intubation Techniques in Patients With Difficult Airways




                 I
                     t has been estimated that in 2014 endotracheal intubation
                     was performed 310 000 times in US emergency depart-                 Key Points
                     ments (EDs).1 This procedure is potentially life-saving for
                                                                                         Question In patients admitted to the emergency department
                 patients who are critically ill, yet has inherent risk.2 A multi-       with difficult airway characteristics undergoing orotracheal
                 center registry of ED intubations, reporting data from 2002-            intubation with a Macintosh laryngoscope blade, does a bougie
                 2012, found that approximately 12% of intubations resulted in           facilitate higher first-attempt intubation success than an
                 an adverse intubation-related event.3 Of factors within an emer-        endotracheal tube + stylet?
                 gency physician’s control, successful endotracheal intuba-              Findings In this randomized clinical trial that included 757 adults,
                 tion on the initial attempt is important to reduce the likeli-          bougie use resulted in significantly higher first-attempt intubation
                 hood of adverse events. 4 A large ED intubation registry                success than an endotracheal tube + stylet (96% vs 82%) for
                 described first-attempt intubation success rates of 85%, de-            those with a difficult airway characteristic.
                 spite increasing adoption of video laryngoscopy.3 The 15% first-        Meaning Although bougie use led to a higher likelihood of
                 attempt failure rate highlights an opportunity to improve the           first-attempt intubation success, further research is needed to
                 safety and efficiency of this critical procedure.                       assess generalizability to other institutions and settings.
                      The tracheal tube introducer (known as the bougie), a
                 simple, inexpensive device first described by Macintosh5 in
                 1949 to facilitate orotracheal intubation, may improve first-        US 45 Code of Federal Regulations, Section 46.116, Waiver of
                 attempt success.6 However, the bougie has been used in less          Informed Consent for Emergency Research. If the patient
                 than 5% of ED first attempts3 and reserved primarily for pa-         was able to communicate or an appropriate surrogate deci-
                 tients with poor laryngeal views or as a rescue device when          sion maker was present, the opportunity to object to study
                 initial intubation attempts fail.7 Routine bougie use was asso-      enrollment was offered.
                 ciated with increased first-attempt success in a retrospective
                 study in the ED6; however, to our knowledge, there have not          Patient Selection
                 been randomized clinical trials assessing its efficacy.              Patients 18 years and older consecutively admitted to the
                      Accordingly, the Bougie Use in Emergency Airway Man-            ED who would undergo orotracheal intubation were eli-
                 agement (BEAM) trial was designed to evaluate the bougie in          gible if the attending emergency physician planned to use a
                 a randomized comparison with an endotracheal tube + stylet           Macintosh laryngoscope blade on the first attempt; both di-
                 in ED patients with at least 1 characteristic predictive of diffi-   rect and video laryngoscopy were allowed. Prisoners, pa-
                 cult laryngoscopy or intubation because these patients would         tients known or assumed to be pregnant, and patients with
                 be most likely to benefit from the bougie. It was hypoth-            known distortion of the upper airway or glottic structures
                 esized that the bougie would facilitate higher first-attempt in-     (eg, angioedema, epiglottitis, laryngeal mass, or malignancy)
                 tubation success than the endotracheal tube + stylet among           were excluded. In the latter group, the bougie has been shown
                 ED patients with a difficult airway characteristic (primary out-     to be advantageous and it was considered to be unethical to
                 come) and all ED patients undergoing orotracheal intubation          include them in the trial.8 Bougie use with hyperangulated
                 (secondary outcome).                                                 blades was not studied because it can be difficult to pass the
                                                                                      bougie, and it is more common to use a steel stylet.9
                                                                                           It has been estimated that approximately 60% of patients
                                                                                      in the ED undergoing endotracheal intubation have anatomic
                 Methods                                                              or other features associated with difficulty obtaining an
                 Trial Design and Setting                                             adequate laryngeal view and passing the endotracheal
                 This randomized clinical trial was conducted from Septem-            tube.4,10 After completion of the procedure, the intubating
                 ber 2016 through August 2017 in the ED of an urban, aca-             emergency physician recorded whether any of the following
                 demic level I trauma center with 109 000 annual ED visits. All       difficult airway characteristics were present: body fluid(s)
                 endotracheal intubations are performed by either emergency           obscuring the laryngeal view, airway obstruction or edema,
                 medicine residents (usually postgraduate year 3 or higher) or        obesity, short neck, small mandible, large tongue, facial
                 attending emergency physicians. All residents receive exten-         trauma, or cervical spine immobilization.4,10,11 These charac-
                 sive training in endotracheal intubation with both an endo-          teristics were not defined formally and physicians deter-
                 tracheal tube + stylet and bougie, including didactics, hands-on     mined their presence subjectively. Patients with at least 1 of
                 sessions with all direct and video laryngoscopes, simulation         these characteristics were analyzed as the primary trial end
                 sessions, and intubation of patients during rotations in com-        point. Querying the intubating physician after intubation was
                 munity EDs earlier in training. The Hennepin County Medical          necessary because it is not possible to ascertain all difficult
                 Center institutional review board approved the trial protocol,       airway characteristics before intubation. This approach facili-
                 available in Supplement 1.                                           tated analysis of the effect of the bougie in patients with and
                     Patients undergoing emergency endotracheal intuba-               without difficult airway characteristics.
                 tion are generally not able to provide informed consent. As
                 use and nonuse of the bougie were both standard of care in           Randomization and Trial Procedures
                 this ED, and any differential risk between the groups was            Eligible patients were randomly assigned in a 1:1 ratio to oro-
                 deemed to be minimal, this trial was conducted under the             tracheal intubation using either the bougie or endotracheal

          2180   JAMA June 5, 2018 Volume 319, Number 21 (Reprinted)                                                                                     jama.com

                                                       © 2018 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### DOC-001 physical PDF page 3

Source: [jama_driver_2018_oi_180054.pdf](../../../jama_driver_2018_oi_180054.pdf#page=3)

```text
                    Comparison of Intubation Techniques in Patients With Difficult Airways                                         Original Investigation Research



                    tube + stylet for the initial attempt. Randomization was per-            sician reported whether a clicking sensation was felt as the bou-
                    formed before the start of the trial with the use of a computer-         gie passed over tracheal rings, and whether a “hold-up” sign
                    generated assignment sequence in permuted blocks of ran-                 was felt as the bougie stopped in a bronchus.15
                    dom sizes of 2, 4, 6, 8, and 10. In an attempt to balance the                 Because of inherent difficulties with blinding of an intuba-
                    number of patients with a difficult airway characteristic in both        tion device, physicians and research assistants were not blinded.
                    intervention groups, the randomization had 2 strata: those with          Discrepant reporting of first-attempt success between the re-
                    obesity or cervical immobilization and those without obesity             search associate and intubating physician were adjudicated by
                    or cervical immobilization. Intervention assignments were                an investigator who retrospectively reviewed video of the in-
                    placed inside a folded sheet of paper in sequentially num-               tubation captured on motion-activated, ceiling-mounted cam-
                    bered, opaque envelopes. A research associate opened the next            eras used in the ED critical care bays for quality assurance and
                    envelope in the appropriate strata to determine intervention             improvement. A trained and blinded abstractor reviewed the
                    allocation after patient enrollment and before laryngoscopy.             final postintubation chest radiograph read for all patients to de-
                         The intubation procedure, including patient position-               termine if a pneumothorax was present. Pneumothoraces were
                    ing, preoxygenation strategy, use of neuromuscular block-                considered to be possibly related to intubation unless the pa-
                    ade (ie, rapid sequence intubation), cricoid pressure, choice            tient had chest trauma with rib fractures or had received chest
                    of Macintosh-style laryngoscope, and whether to view the                 compressions in the setting of cardiac arrest.
                    video screen, was at the discretion of the emergency physi-
                    cian. The ED had 2 laryngoscopes with reusable Macintosh-                Trial Outcomes
                    style blades capable of both direct and video laryngoscopy               The primary outcome was first-attempt intubation success, de-
                    (C-MAC Macintosh blade [KARL STORZ] and GlideScope Tita-                 fined as successful endotracheal tube placement with the first
                    nium MAC [Verathon]); a nonvideo, direct Macintosh laryn-                device passed (bougie or endotracheal tube + stylet) during the
                    goscope was also available. The bougie used for this study is            first laryngoscope insertion. If neither a bougie nor endotra-
                    a 70-cm long, 15 French (5-mm diameter), malleable, semi-                cheal tube + stylet were inserted into the mouth during the first
                    rigid, straight, single-use bougie with a coudé tip (SunMed).            laryngoscope insertion, the attempt was counted as a failure.
                    Bougie bending was not stipulated; intubating physicians                 Secondary outcomes included hypoxemia, first-attempt du-
                    chose whether and how to bend the bougie.                                ration, and esophageal intubation. Hypoxemia was defined as
                         In all patients, the best possible view of the larynx was ob-       an oxyhemoglobin saturation less than 90% (or, if the at-
                    tained using direct or video laryngoscopy. In the bougie group,          tempt began with a saturation <90%, an absolute decrease in
                    the operator attempted to pass the bougie into the trachea. If           saturation of >10%) by continuous pulse oximetry. The dura-
                    successful, an assistant loaded the endotracheal tube over the           tion of an intubation attempt was defined as the time elapsed
                    bougie and the operator guided the tube through the vocal                between insertion and removal of the laryngoscope blade from
                    cords and into the trachea to the desired depth while keeping            the patient’s mouth.
                    the laryngoscope in the mouth.12 If resistance was encoun-
                    tered when passing the endotracheal tube over the bougie (pre-           Statistical Analysis
                    sumably from the bevel-tip of the tube catching on the aryte-            This study was powered to detect a between-group differ-
                    noid cartilages), the tube was retracted 2 centimeters, rotated          ence in first-attempt intubation success among patients with
                    90° counterclockwise, and readvanced into the trachea.12,13 In           at least 1 difficult airway characteristic (a subset of all en-
                    the endotracheal tube + stylet group, the operator attempted             rolled patients). A minimum clinically important difference in
                    to intubate the trachea with an endotracheal tube + stylet with          first-attempt intubation success has not been defined in the
                    a “straight-to-cuff” shape and a bend angle of 25° to 35°.14 If          literature to guide trial planning. Therefore, based on a previ-
                    difficulty in passage was encountered, the intubator could               ously published study of bougie use in the ED, we estimated
                    withdraw, rotate, or reshape the tube and stylet as needed. The          that a sample of 374 patients with difficult airway character-
                    stylet was left in place until the tube was advanced to the de-          istic(s) would provide 80% power to detect an absolute dif-
                    sired position in the trachea. In both groups, if the trachea was        ference of 9% in first-attempt intubation success (95% vs 86%)6
                    not intubated with the initial device, any change in equip-              with a 2-sided α of .05. No a priori sample size calculation was
                    ment was at the discretion of the operator, including cross-             performed for the analysis that included all enrolled pa-
                    over to bougie or endotracheal tube + stylet. Correct tube po-           tients, which included patients without a difficult airway char-
                    sition was confirmed with waveform capnography.                          acteristic, as we anticipated the difference in first-attempt suc-
                                                                                             cess for patients without predicted difficulty would be less than
                    Measurements                                                             5%, which would require a sample size not feasible for this
                    A trained research associate prospectively collected process             study. The number of patients with a difficult airway charac-
                    and outcome data from patient randomization until 1 minute               teristic was monitored and the trial stopped when more than
                    following the end of the first intubation attempt, including the         374 such patients were enrolled. All enrolled patients were in-
                    duration of the first attempt using a handheld stopwatch and             cluded in the final analysis.
                    whether the attempt was successful. After the procedure, the                  The principal trial analyses were performed in the inten-
                    intubating physician recorded additional data on a standard-             tion-to-treat population. The primary analysis of those with
                    ized collection form (Supplement 2), including the presence              a difficult airway characteristic, the secondary analysis of the
                    of specific difficult airway characteristics. In addition, the phy-      overall study cohort, and secondary outcomes were compared

                    jama.com                                                                                (Reprinted) JAMA June 5, 2018 Volume 319, Number 21      2181

                                                              © 2018 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### DOC-001 physical PDF page 4

Source: [jama_driver_2018_oi_180054.pdf](../../../jama_driver_2018_oi_180054.pdf#page=4)

```text
                 Research Original Investigation                                                                      Comparison of Intubation Techniques in Patients With Difficult Airways




                 Figure 1. Flow of Patients Through the Study


                                                  3768 Individuals assessed for eligibility


                                                                             3011 Excluded
                                                                                  2938 Did not meet inclusion criteria
                                                                                        2785 Not intubated
                                                                                           61 Younger than 18 y
                                                                                           28 Prisoners
                                                                                           27 Had known distortion of the upper airway
                                                                                           22 Not intubated with Macintosh laryngoscope
                                                                                           15 Known or expected pregnancy
                                                                                    73 Met inclusion criteria but were not randomized                 Difficult airway characteristics were
                                                                                           30 Intubated too quickly to enroll                         defined as body fluids obscuring the
                                                                                           20 No research staff available                             laryngeal view, airway obstruction or
                                                                                           16 Physician refused enrollmenta
                                                                                                                                                      edema, obesity, short neck, small
                                                                                            6 Patient or legally authorized representative
                                                                                              declined enrollment                                     mandible, large tongue, facial trauma,
                                                                                            1 Unknown                                                 or the need for cervical spine
                                                                                                                                                      immobilization.
                                                                                                                                                      a
                                                                                                                                                          Of the 16 patients who were refused
                                                      757 Randomized and enrolled
                                                                                                                                                          randomization by the physician,
                                                          380 Had a difficult airway                                                                      data are available for 15. The bougie
                                                              characteristic                                                                              was used in all 15 cases, with
                                                                                                                                                          first-attempt success in 14 of 15
                                                                                                                                                          patients (93%). Reasons for
                         381 Randomized to intubation using               376 Randomized to intubation using                                              protocol deviations and refusal
                             a bougie                                         endotracheal tube and stylet                                                included anticipated difficult airway
                             372 Received intervention as                     345 Received intervention as                                                and perceived need for more rapid
                                  randomized                                      randomized
                                4 Had endotracheal tube and                    25 Had bougie passed first
                                                                                                                                                          intubation. Of the 25 patients in the
                                  stylet passed first                           6 Had no device passedb                                                   endotracheal tube + stylet group
                                5 Had no device passedb                                                                                                   with a protocol deviation (a bougie
                                                                          182 Had a difficult airway characteristic                                       was passed first rather than an
                         198 Had a difficult airway characteristic            161 Received intervention as
                             191 Received intervention as                          randomized
                                                                                                                                                          endotracheal tube + stylet), 23 had
                                  randomized                                   18 Had bougie passed first                                                 first-attempt success (92%).
                               2 Had tracheal tube passed first                 3 Had no device passedb                                               b
                                                                                                                                                          These patients, after laryngoscope
                               5 Had no device passedb                                                                                                    insertion, did not have passage
                                                                                                                                                          of a bougie or endotracheal
                            198 Included in primary analysis                  182 Included in primary analysis                                            tube + stylet attempted. All were
                                                                                                                                                          considered to have first-attempt
                            381 Included in subgroup analysis                 376 Included in subgroup analysis
                                                                                                                                                          failure and were intubated on
                                                                                                                                                          subsequent attempts.

                 by calculating the difference in the proportions or median dif-                           1 interim analysis evaluating for futility was completed at the
                 ference, as appropriate, between groups, and the associated                               midpoint of the trial (Supplement 2). Because this interim
                 95% CI. Hodges-Lehmann median between-group differ-                                       analysis assessed only for futility and not superiority, no ad-
                 ences and the associated 95% CIs were calculated for continu-                             justments were made to the significance threshold. Stata
                 ous variables. Tests of significance were completed using the                             (StataCorp), version 15.1, was used for data analysis.
                 χ2 test for binary outcomes and the Wilcoxon rank sum test
                 for continuous outcomes, using a 2-sided threshold of .05. Be-
                 cause the primary outcome analysis was performed on the sub-
                 group of patients with a difficult airway characteristic, we
                                                                                                           Results
                 tested for the effect modification of this variable with a test                           Trial Patients
                 of interaction. In addition, the duration of the first intubation                         A total of 380 patients with a difficult airway characteristic were
                 attempt was analyzed using Kaplan-Meier estimates and a log-                              enrolled. Figure 1 shows the flow of patients into the trial. In
                 rank test; hazard ratios were estimated using an unadjusted                               total, 757 patients were enrolled and randomized to be intu-
                 Cox proportional hazards model. Schoenfeld residuals and data                             bated using either the bougie (381 patients, including 198 with
                 visualization were used to test for proportionality.                                      a difficult airway characteristic) or an endotracheal tube + sty-
                      Unplanned subgroup analyses were performed for vari-                                 let (376 patients, including 182 with a difficult airway charac-
                 ables of clinical interest. These analyses were exploratory in                            teristic). There were 51 unique emergency physicians who in-
                 nature, and a test of interaction for each subgroup was per-                              tubated at least 1 patient in the trial; 44 physicians intubated
                 formed. No corrections were made for multiple comparisons.                                patients randomized to the bougie group on the first intuba-
                 In addition, because individual physician intubation ability can                          tion attempt, whereas 40 physicians intubated patients ran-
                 affect first-attempt success, a post hoc analysis accounting for                          domized to the endotracheal tube + stylet group. The me-
                 clustering by physician was also completed.                                               dian number of intubations per physician was 8 (interquartile
                      Missing data were left as such, and imputation was not per-                          range, 1-26; range, 1-61). Adherence to the randomized allo-
                 formed. A data and safety monitoring board was established;                               cation was 98% in the bougie group and 92% in the endotra-

          2182   JAMA June 5, 2018 Volume 319, Number 21 (Reprinted)                                                                                                                 jama.com

                                                                     © 2018 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### DOC-001 physical PDF page 5

Source: [jama_driver_2018_oi_180054.pdf](../../../jama_driver_2018_oi_180054.pdf#page=5)

```text
                    Comparison of Intubation Techniques in Patients With Difficult Airways                                                      Original Investigation Research



                    cheal tube + stylet group. The 2 groups were well balanced in
                                                                                             Table 1. Baseline Characteristics of Patients Admitted to the Emergency
                    terms of patient characteristics and clinical indications for in-        Department Undergoing Orotracheal Intubation Using a Bougie
                    tubation (Table 1) and intubation process measures (Table 2).            vs an Endotracheal Tube + Stylet
                                                                                                                                                              Endotracheal
                    Primary Outcome                                                                                                             Bougie Group, Tube + Stylet
                                                                                                                                                No. (%)       Group, No. (%)
                    Among the 380 patients with at least 1 difficult airway char-                Characteristic                                 (n = 381)     (n = 376)
                    acteristic, first-attempt intubation success was higher in the               Age, mean (SD), y                               46 (18)           46 (18)
                    bougie group (96%) than in the endotracheal tube + stylet                    Men                                            272 (71)         255 (68)
                    group (82%); absolute between-group difference, 14% (95% CI,                 BMI, mean (SD)a                                 28 (7)            28 (7)
                    8%-20%). An analysis accounting for clustering by physician
                                                                                                 Heart rate, mean (SD), beats/minb              108 (25          107 (25)
                    did not significantly change the study results (eTable 1 in
                                                                                                 Systolic blood pressure, mean (SD),            135 (30)         134 (32)
                    Supplement 2).                                                               mm Hgb
                                                                                                 Oxygen saturation, median (IQR), %b             99 (95-100)       99 (96-100)
                    Secondary Trial Outcomes                                                       <90%b                                         44/352 (13)       40/344 (12)
                    Among the study population as a whole, first-attempt intuba-                   <80%b                                         21/352 (6)        11/344 (3)
                    tion success in the bougie group (98%) was higher than the en-               Indication for intubation
                    dotracheal tube + stylet group (87%); absolute difference, 11%                 Medical                                      318 (83)         315 (84)
                    (95% CI, 7%-14%). For patients without any difficult airway                        Altered mental status                    185 (49)         173 (46)
                    characteristics, first-attempt intubation success in the bou-                      Cardiac arrest                            32 (8)            23 (6)
                    gie group was 99% compared with 92% in the endotracheal                            Septic shock                              21 (6)            27 (7)
                    tube + stylet group (absolute difference, 8% [95% CI, 4%-
                                                                                                       Seizure                                   20 (5)            28 (7)
                    12%]). There was no significant interaction between bougie use
                                                                                                       Asthma, COPD, heart failure,              16 (5)            23 (7)
                    and presence of difficult airway characteristics on the out-                       pneumonia
                    come of first-attempt intubation success (P = .36). Table 3 pro-                   Other                                     44 (14)           41 (13)
                    vides secondary outcomes of this trial.                                        Trauma                                        63 (17)           61 (16)
                         In exploratory analyses, the effect of the bougie over a en-                  Traumatic brain injury                    29 (8)            23 (6)
                    dotracheal tube + stylet in facilitating first-attempt intuba-                     Other                                     34 (9)            38 (10)
                    tion success was also present in several subgroups, including                Difficult airway characteristic present        198 (52)         182 (48)
                    patients requiring cervical in-line immobilization (100% vs                    Blood or vomit in airway                      83 (22)           67 (18)
                    78%, respectively), obese patients (96% vs 75%), and pa-                       Obesityc                                      57 (15)           68 (18)
                    tients with incomplete glottic views on laryngoscopy corre-                    Cervical immobilization                       49 (13)           36 (10)
                    sponding to Cormack-Lehane grades 2 to 4 (97% vs 60%)                          Large tongue                                  31 (8)            34 (9)
                    (Table 3).
                                                                                                   Short neck                                    28 (7)            28 (7)
                         Kaplan-Meier estimates of time until first-attempt intu-
                                                                                                   Facial trauma                                 20 (5)            12 (3)
                    bation success for patients with a difficult airway character-
                                                                                                   Small mandible                                14 (4)            18 (5)
                    istic are displayed in Figure 2. There was a significant differ-
                                                                                                   Airway obstruction or edema                     8 (2)            4 (1)
                    ence in intubation times between the 2 groups (log-rank
                    P = .02; hazard ratio for first-attempt intubation success in the        Abbreviations: BMI, body mass index (calculated as weight in kilograms divided
                                                                                             by height in meters squared); COPD, chronic obstructive pulmonary disease;
                    bougie group, 1.29 [95% CI, 1.04-1.60], with endotracheal
                                                                                             IQR, interquartile range.
                    tube + stylet group as reference). Kaplan-Meier estimates in-            a
                                                                                                 BMI was calculated by chart review using a measured weight and height.
                    cluding all patients are displayed in eFigure 1 in Supplement            b
                                                                                                 Initial vital signs were the first vital signs after enrollment but before
                    2. There was no significant difference between groups (log-                  intubation. Not all had initial vital signs available due to not being connected to
                    rank P value, 0.12; hazard ratio for the bougie group, 1.12 [95%             the monitor or unreliability of the oximetry waveform: 61 (29 in bougie group;
                    CI, 0.97-1.30], with endotracheal tube + stylet group as refer-              32 in endotracheal tube + stylet group), 185 (94 in bougie group; 91 in
                                                                                                 endotracheal tube + stylet group), and 43 (19 in bougie group; 24 in
                    ence). Analysis of scaled Schoenfeld residuals and data visu-                endotracheal tube + stylet group) patients had no heart rate, systolic blood
                    alization demonstrated that the assumption of proportional                   pressure, and oxygen saturation, respectively, available before intubation.
                    hazards was not upheld. In an unplanned, post hoc subgroup               c
                                                                                                 Sixty-four patients in the bougie group and 68 patients in the endotracheal
                    analysis including only patients with a successful first at-                 tube + stylet group had a BMI of ⱖ30 but were not classified as obese by the
                                                                                                 intubating physician; these 132 patients had a mean BMI of 34. Those
                    tempt, the bougie use resulted in a longer median first-
                                                                                                 considered obese by the intubating physician had a mean BMI of 37.
                    attempt duration than the endotracheal tube (38 seconds vs
                    34 seconds; absolute difference, 4 seconds [95% CI, 2-7])
                    (Table 3).                                                               a hold-up sign upon bougie advancement (caused by the dis-
                                                                                             tal bougie wedging in a bronchus at a bougie depth of about
                    Other Outcomes                                                           30 cm, thus confirming correct placement; if no hold-up oc-
                    In total, the bougie was used in 444 patients; tracheal clicks           curs by 35 cm, this indicates esophageal placement), the
                    (tactile vibrations felt by the operator as the bougie tip scrapes       hold-up sign was reported in 283 intubations (64%). During in-
                    along the tracheal rings) were reported in 404 intubations               tubation over a bougie, the endotracheal tube tip met resis-
                    (91%). Although it was not mandated that the operator verify             tance on the arytenoid cartilages in 31 patients (7%); in all but

                    jama.com                                                                                          (Reprinted) JAMA June 5, 2018 Volume 319, Number 21              2183

                                                              © 2018 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### DOC-001 physical PDF page 6

Source: [jama_driver_2018_oi_180054.pdf](../../../jama_driver_2018_oi_180054.pdf#page=6)

```text
                 Research Original Investigation                                                                    Comparison of Intubation Techniques in Patients With Difficult Airways




                 Table 2. Intubation Process Measures Among Patients Admitted to the Emergency Department Undergoing Orotracheal Intubation Using a Bougie
                 vs an Endotracheal Tube + Stylet
                                                                                                                                          Endotracheal
                                                                                                                 Bougie Group,            Tube + Stylet
                                                                                                                 No. (%)                  Group, No. (%)       Difference, %
                     Measure                                                                                     (n = 381)                (n = 376)            (95% CI)              P Value
                     Preoxygenation
                       Non-rebreather mask                                                                       267 (70)                 276 (73)              −3 (−10 to 3)          .31
                       Non-rebreather mask at flush rate oxygen, No. of patients/total patients with             204/267 (76)             210/276 (76)            0 (−7 to 7)          .93
                       non-rebreather masks (%)
                       Bag and mask ventilation                                                                    47 (12)                  37 (10)               2 (−2 to 7)          .27
                       Noninvasive positive pressure ventilation                                                   18 (5)                   24 (6)              −2 (−5 to 2)           .32
                       Extraglottic device                                                                         27 (7)                   17 (5)                3 (−1 to 6)          .13
                     Preintubation sedative, anya                                                                338 (89)                 341 (91)              −2 (−6 to 2)           .37
                       Etomidate                                                                                 332 (87)                 333 (89)              −1 (−6 to 3)           .54
                       Ketamine                                                                                     4 (1)                    4 (1)                0 (−1 to 1)          .99
                     Preintubation neuromuscular blockade, anyb                                                  366 (96)                 367 (98)              −2 (−4 to 1)           .23
                       Succinylcholine                                                                           214 (56)                 229 (61)              −5 (−12 to 2)          .19
                       Rocuronium                                                                                147 (39)                 137 (36)                2 (−5 to 9)          .54
                     Patient position for intubation
                       Sniffing positionc                                                                        222 (58)                 244 (65)              −7 (−14 to 0)          .06
                       Neutral cervical spine                                                                    117 (31)                   96 (26)               5 (−1 to 12)         .11
                       Cervical spine extension without sniffing position                                          39 (10)                  32 (9)                2 (−2 to 6)          .42
                     Oxygen saturation at start of intubation attempt, median (IQR), %d                          100 (98-100)             100 (98-100)            0 (0 to 0)           .60
                       <90%, No. of patients/total patients with data (%)d                                         22/360 (6)               27/343 (8)          −2 (−6 to 2)           .36
                       <80%, No. of patients/total patients with data (%)d                                         13/360 (4)                8/343 (2)            1 (−1 to 4)          .32
                     Apneic oxygenation with nasal cannulae                                                      221 (58)                 227 (60)              −2 (−9 to 5)           .51
                     Operatorf
                       Emergency medicine senior resident or fellow (postgraduate year 3 or higher)              318 (83)                 334 (89)              −5 (−10 to 0)          .03
                       Emergency medicine junior resident (postgraduate year 2 or below)                           57 (15)                  37 (10)               5 (0 to 10)          .03
                       Emergency medicine faculty                                                                   8 (2)                    5 (1)                1 (−1 to 3)          .42
                     Laryngoscope used
                       C-MAC Macintosh blade                                                                     362 (95)                 366 (97)              −2 (−5 to 0)           .10
                       GlideScope Titanium MAC blade                                                               12 (3)                    8 (2)                1 (−1 to 3)          .38
                       Macintosh direct laryngoscope                                                                7 (2)                    2 (1)                1 (0 to 3)           .10
                     Video screen use for video laryngoscopy, No. of patients/total patients with data (%)g
                       Screen never used                                                                         218/377 (58)             182/372 (49)            9 (2 to 16)          .02
                       Screen viewed for entire attempt                                                            78/377 (21)              90/372 (24)         −4 (−9 to 2)           .25
                       Screen viewed during passage of tube or bougie into glottis                                 75/377 (20)              98/372 (26)         −6 (−12 to 0)          .04
                     Best Cormack-Lehane view, No. of patients/total patients with data (%)h
                       Grade 1 (best view)                                                                       269/373 (72)             269/359 (75)          −3 (−9 to 4)           .39
                       Grade 2                                                                                     74/373 (20)              62/359 (17)           3 (−3 to 8)          .39
                       Grade 3                                                                                     27/373 (7)               23/359 (6)            1 (−3 to 4)          .66
                       Grade 4 (worst view)                                                                         3/373 (1)                5/359 (1)          −1 (−2 to 1)           .44
                     First device entered into mouth after laryngoscope
                       Bougie                                                                                    372 (98)                   25 (7)              91 (88 to 94)        <.001
                       Endotracheal tube + stylet                                                                   4 (1)                 345 (92)             −91 (−94 to −88)      <.001
                       Laryngoscope withdrawn before attempted passage of bougie or endotracheal                    5 (1)                    6 (2)                0 (−2 to 1)          .75
                       tube + stylet
                                                                                                        e
                 Abbreviation: IQR, interquartile range.                                                    Nasal cannula left in place during intubation.
                 a                                                                                      f
                     Of the 78 patients without sedative administration, 53 (68%; 31 and 22 in the          This lists the final intubating physician. During the course of intubation,
                     bougie and endotracheal tube + stylet groups, respectively) had received               a change of intubating physician occurred 8 times total, 4 times per group.
                     sedation prehospital or were in cardiac arrest. Sedatives other than ketamine      g
                                                                                                            Video screen use was determined by the intubating physician, and
                     or etomidate are not listed.                                                           documented on the postintubation data form. There were 4 missing values
                 b
                     Drugs other than succinylcholine and rocuronium are not listed.                        in each group.
                 c                                                                                      h
                     The sniffing position was defined as flexion of the neck and extension                 Grade 1: all or most of the glottic opening seen; grade 2: only the posterior
                     of the atlanto-occipital joint to align the external auditory meatus with the          portion of the glottis or only arytenoid cartilages are visible; grade 3: only the
                     sternal notch.                                                                         epiglottis but no portion of the glottis is visible; grade 4: neither the glottis nor
                 d
                     Twenty-one patients in the bougie group and 33 patients in endotracheal                the epiglottis can be seen. There are missing data for 8 patients in the bougie
                     tube + stylet group did not have an oxygen saturation at the start of the              group and 17 patients in the endotracheal tube + stylet group.
                     attempt due to an unreliable oximetry waveform.



          2184   JAMA June 5, 2018 Volume 319, Number 21 (Reprinted)                                                                                                                   jama.com

                                                                   © 2018 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### DOC-001 physical PDF page 7

Source: [jama_driver_2018_oi_180054.pdf](../../../jama_driver_2018_oi_180054.pdf#page=7)

```text
                    Comparison of Intubation Techniques in Patients With Difficult Airways                                                                 Original Investigation Research




                    Table 3. Trial Outcomes Among Patients Admitted to the Emergency Department Undergoing Orotracheal Intubation Using a Bougie
                    vs an Endotracheal Tube + Stylet
                                                                                                                Endotracheal Tube + Stylet
                                                                        Bougie Group                            Group
                                                                        No. With                                No. With
                                                                        Event/ Total                            Event/ Total                      Difference                   Interaction
                        Outcome                                         No. of Patients   % (95% CI)            No. of Patients   % (95% CI)      (95% CI)           P Value   P Valuea
                        Primary Outcome
                        First-attempt intubation success, patients      191/198            96 (93 to 99)        150/182           82 (76 to 88)   14 (8 to 20)       <.001     .36
                        with any difficult airway characteristic
                        (n = 380)
                        Planned Secondary Outcomes
                        Patients with any difficult airway
                        characteristic
                        (n = 380)
                          First-attempt intubation success              156/191            82 (76 to 87)        123/177           69 (63 to 76)   12 (3 to 21)        .006     .61
                          without hypoxemiab
                          First-attempt duration,                        39 (29 to 52)                           40 (27 to 63)                    −1 (−6 to 3)        .50      .17
                          median (IQR), sc
                        All patients (N = 757)
                          First-attempt intubation success, overall     373/381            98 (96 to 99)        328/376           87 (83 to 90)   11 (7 to 14)       <.001     NA
                          First-attempt intubation success              317/371            85 (81 to 89)        282/366           77 (72 to 81)     8 (3 to 14)       .003     NA
                          without hypoxemiab
                          First-attempt duration, median (IQR), sc       38 (29 to 51)                           36 (25 to 54)                      1 (4 to −1)       .24      NA
                        Unplanned Subgroup Analyses
                        First-attempt intubation success by
                        individual difficult airway characteristicd
                          Blood or vomit in airway (n = 150)             79/83             95 (88 to 99)         55/67            82 (71 to 90)   13 (3 to 23)        .01      .31
                          Cervical immobilization (n = 85)               49/49            100 (93 to 100)        28/36            78 (61 to 90)   22 (9 to 36)        .001     .25
                          Obesity (n = 125)                              55/57             96 (88 to 100)        51/68            75 (63 to 85)   21 (10 to 33)       .001     .63
                        First-attempt intubation success,               182/183            99 (97 to 100)       178/194           92 (87 to 95)     8 (4 to 12)      <.001     .36
                        no difficult airway characteristic (n = 377)
                        First-attempt intubation success when           356/362            98 (96 to 99)        321/366           88 (84 to 91)   11 (7 to 14)       <.001     .46
                        C-MAC used, all patients
                        First-attempt intubation success by
                        Cormack-Lehane view, all patients
                          Grade 1                                       265/269            99 (96 to 100)       258/269           96 (93 to 98)     3 (0 to 5)        .07      .04
                          Grade 2                                        72/74             97 (91 to 100)        41/62            66 (53 to 78)   31 (19 to 44)      <.001     .13
                          Grade 3                                        26/27             96 (81 to 100)        11/23            48 (27 to 69)   48 (27 to 71)      <.001     .17
                          Grade 4                                         3/3             100 (29 to 100)         2/5             40 (5 to 85)    60 (17 to 100)      .09      .78
                        First-attempt intubation success by actual      392/402            98 (95 to 99)        309/355           87 (83 to 90)   10 (7 to 14)       <.001     NA
                        first device entered into mouth after
                        laryngoscope, all patientse
                        First-attempt duration if first attempt          38 (29 to 51)                           34 (23 to 47)                      4 (2 to 7)       <.001     .03
                        successful, median (IQR), sc
                    Abbreviations: IQR, interquartile range; NA, not applicable.                                laryngoscope blade entered the mouth to when the blade was removed from
                    a
                        The interaction P value column displays NA for analyses that included                   the mouth.
                                                                                                            d
                        all patients.                                                                           Short neck, small mandible, airway obstruction or edema, facial trauma and
                    b
                        Oxyhemoglobin saturations were recorded in real time by research associates.            large tongue subgroups are not displayed because there were too few patients
                        Hypoxemia was defined as an oxyhemoglobin saturation <90% (or, if the                   with these characteristics to make a valid comparison between groups.
                                                                                                            e
                        attempt began with a saturation <90%, an absolute decrease in saturation of             Those that had the laryngoscope withdrawn before attempted passage of the
                        >10%) during or within 1 min after completion of the intubation attempt. Valid          bougie or endotracheal tube + stylet were considered to have the randomized
                        pulse oximetry waveform during intubation was not available for all patients.           device passed first for this analysis.
                    c
                        Intubation duration was defined as the time elapsed from when the



                    1 of these patients, the tube was rotated 90° counterclock-                             cessful with the help of several rescue techniques including
                    wise and advanced without resistance into the trachea. In 1 pa-                         the bougie in 49 patients, the intubating laryngeal mask air-
                    tient, the tube could not be advanced, both tube and bougie                             way in 1 patient, and cricothyrotomy in 1 patient (Table 4).
                    were removed, and intubation was ultimately successful with
                    a bougie on a subsequent attempt.                                                       Complications
                         Among the 56 patients (7%) in both groups who were not                             Complications were infrequent and occurred with a similar fre-
                    intubated on the first attempt, subsequent attempt(s) were suc-                         quency in both groups (Table 5). The incidence of hypoxemia

                    jama.com                                                                                                      (Reprinted) JAMA June 5, 2018 Volume 319, Number 21          2185

                                                                      © 2018 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### DOC-001 physical PDF page 8

Source: [jama_driver_2018_oi_180054.pdf](../../../jama_driver_2018_oi_180054.pdf#page=8)

```text
                 Research Original Investigation                                                                                          Comparison of Intubation Techniques in Patients With Difficult Airways




                 Figure 2. Duration of the First Intubation Attempt Until Successful                                          Table 4. Successful Technique After Failed First Attempt Among Patients
                 Intubation Using a Bougie vs Endotracheal Tube + Stylet Among Patients                                       Admitted to the Emergency Department Undergoing Orotracheal
                 With 1 or More Difficult Airway Characteristics                                                              Intubation With a Bougie vs Endotracheal Tube + Stylet
                                                                                                                                                                                          Endotracheal
                                                       100
                                                                       Bougie use                                                                                        Bougie Group     Tube + Stylet Group
                                                                                                                                  Attempt Detail                         (n = 8)          (n = 48)
                                                                                       Endotracheal tube + stylet
                                                       80                                                                         Same (first) laryngoscopic insertion




                           Successfully Intubated, %
                                                                                                                                    Bougie                               0                34 (71)
                                                       60
                                                                                                                                    Endotracheal tube + stylet           0                  1 (2)a
                                                                                                                                  Second laryngoscopic insertion
                                                       40
                                                                                                                                    Bougie                               6 (75)             6 (13)
                                                       20                                                                           Endotracheal tube + stylet           0                  3 (6)
                                                                                                       Log−rank P = .02           Second attempt with different          0                  2 (4)
                                                        0                                                                         intubating deviceb
                                                             0   30      60           90         120         150      180
                                                                                                                                  >2 Attemptsc                           2 (25)             2 (4)
                                                                                    Time, s
                 No. at risk                                                                                                  a
                                                                                                                                  This patient had the bougie used first, which failed, and the endotracheal
                  Bougie        198                              146     37           13          3           3           0       tube + stylet was used on the same attempt to successfully intubate
                  Endotracheal 182                               127     56            9          3           3           1
                  tube + stylet                                                                                                   the patient.
                                                                                                                              b
                                                                                                                                  One was rescued with an intubating laryngeal mask airway; 1 had
                 The hazard ratio for first-attempt success in the bougie group was 1.29 (95% CI,                                 a cricothyrotomy.
                                                                                                                              c
                 1.04 to 1.60), with endotracheal tube + stylet group as reference. Vertical ticks                                Three of 4 were intubated on the third attempt with a bougie; the fourth had
                 mark the time point when the intubation attempt for ⱖ1 patients ended in                                         a tracheal abnormality and was intubated after several attempts
                 failure. The assumption of proportional hazards over time was not upheld.                                        with 4.0 mm stylet and endotracheal tube.



                 during intubation was similar between the bougie group (13%)                                                      If emergency physicians in this trial had inadequate
                 and the endotracheal tube + stylet group (14%). No patients                                                  training or experience intubating with an endotracheal
                 had an esophageal intubation in the bougie group, and 3 pa-                                                  tube + stylet (because the majority of ED intubations at this
                 tients (1%) had esophageal intubation in the endotracheal                                                    institution utilized a bougie prior to this trial6), between-
                 tube + stylet group (Table 5).                                                                               group differences in first-attempt intubation success could
                                                                                                                              have been biased away from the null. The first-attempt suc-
                                                                                                                              cess in the endotracheal tube and stylet group in this trial,
                                                                                                                              however, compares favorably with success rates reported
                 Discussion                                                                                                   elsewhere using this same strategy. For example, in patients
                 In this trial, orotracheal intubation with a bougie on the ini-                                              with 1 or more difficult airway characteristics, Sakles et al23
                 tial intubation attempt compared with intubation using a sty-                                                reported a first-attempt success rate of 78% when a video
                 let and endotracheal tube led to improved first-attempt intu-                                                laryngoscope was used compared with 82% in this study for
                 bation success in patients with at least 1 difficult airway                                                  endotracheal tube + stylet. In the same study,23 Sakles et al,
                 characteristic. In light of the significant association between                                              examining patients without any difficult airway characteris-
                 first-attempt intubation success and fewer intubation-                                                       tics, reported a first-attempt success rate of 91% when a
                 related adverse events in previous research,4,16-19 the bougie                                               video laryngoscope was used compared with 92% in this
                 may be beneficial as a primary intubation device rather than                                                 study for endotracheal tube + stylet. Describing more than
                 solely as a rescue adjunct.                                                                                  13 000 resident physician intubations in the ED (not distin-
                       Several hypotheses could explain the mechanism by which                                                guishing those with a difficult airway), Brown et al3 reported
                 the bougie affects first-attempt intubation success. First, by                                               first-attempt success of 86.9%, which is similar to the 87%
                 virtue of its smaller diameter compared with the endotra-                                                    observed in this trial among all patients randomized to an
                 cheal tube, the bougie obscures less of the operator’s view of                                               endotracheal tube + stylet. Furthermore, a meta-analysis of
                 the glottic inlet as it approaches, allowing the trachea to be in-                                           more than 42 000 ED intubations reported first-attempt suc-
                 tubated more easily and confidently. Second, the bougie has                                                  cess to be 84.1%.24 Taken together, these comparisons argue
                 advantages when an incomplete view of the glottis is ob-                                                     against inferior institutional performance intubating with
                 tained (Cormack-Lehane grade 2-4), as was the case in nearly                                                 endotracheal tube + stylet in the current trial.
                 one-third of patients in this study. In this instance, the coudé                                                  Because more than 96% of patients were intubated using
                 tip can be placed under the epiglottis and can blindly enter the                                             the C-MAC Macintosh blade for the initial attempt, this study
                 glottic opening8,15,20-22; clicking against tracheal rings during                                            can essentially be seen as a comparison of first attempt intu-
                 passage and holding up when the tip lodges in the bronchial                                                  bation success using the C-MAC Macintosh blade with or with-
                 tree, providing tactile feedback of proper placement.15 The bou-                                             out the bougie. First-attempt success using the C-MAC
                 gie likely has a higher chance of blindly accessing the glottic                                              Macintosh blade in a large ED registry was 91%,3 which con-
                 opening when compared with the larger-caliber endotra-                                                       trasts to first-attempt success achieved in this study using
                 cheal tube.                                                                                                  C-MAC Macintosh blade with a bougie achieved in this study

          2186   JAMA June 5, 2018 Volume 319, Number 21 (Reprinted)                                                                                                                                   jama.com

                                                                                     © 2018 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### DOC-001 physical PDF page 9

Source: [jama_driver_2018_oi_180054.pdf](../../../jama_driver_2018_oi_180054.pdf#page=9)

```text
                    Comparison of Intubation Techniques in Patients With Difficult Airways                                                                Original Investigation Research




                    Table 5. Intubation Complications Among Patients Admitted to the Emergency Department Undergoing Orotracheal Intubation Using a Bougie
                    vs an Endotracheal Tube + Stylet
                                                                                                              Endotracheal
                                                                              Bougie Group, No.               Tube + Stylet Group,
                                                                              of Patients (%)                 No. of Patients (%)               Difference, %
                        Complication                                          (n = 381)                       (n = 376)                         (95% CI)                  P Value
                        Any complicationa                                     66 (17)                         63 (17)                            1 (−5 to 6)              .83
                        Hypoxemia, No. of patients/total patients             47/371 (13)                     50/364 (14)                       −1 (−6 to 4)              .67
                        with data (%)b
                        Pneumothorax diagnosed after intubation                9 (2)                           9 (2)                             0 (−2 to 2)              .99
                        Pneumothorax postintubation                            1 (<1)                          3 (1)                            −1 (−2 to 1)              .31
                        without clear causec
                        Lip laceration                                         7 (2)                           3 (1)                             1 (−1 to 3)              .21
                        Witnessed aspiration during intubation                 3 (1)                           1 (<1)                            1 (−1 to 2)              .32
                        Iatrogenic bleeding from oropharynx                    2 (1)                           2 (1)                             0 (−1 to 1)              .99
                        or perilaryngeal structures
                        Dental trauma                                          1 (<1)                          1 (<1)                            0 (−1 to 1)              .99
                        Esophageal intubation                                  0                               3 (1)                            −1 (−2 to 0)              .08
                        Direct airway injury                                   0                               0
                    a
                        Some patients had >1 complication and were only counted once in this                 pulse oximetry waveform during intubation was not available for all patients.
                        composite variable.                                                                  A valid pulse oximetry waveform was not available for all patients.
                    b                                                                                    c
                        Oxyhemoglobin saturations were recorded in real time by research associates.         Clear causes included chest trauma with rib fractures or patients who received
                        Hypoxemia was defined as an oxyhemoglobin saturation <90% (or, if the                chest compressions as part of cardiopulmonary resuscitation. None of these 4
                        attempt began with a saturation <90%, an absolute decrease in saturation of          patients had the etiology of the pneumothorax definitively identified.
                        >10%) during or within 1 min after completion of the intubation attempt. Valid



                    (98%). This supports the finding that the bougie could                               on the anterior larynx after passing through the glottis; this
                    have incremental benefit in improving first-attempt success                          is remedied by slight withdrawal of the bougie, rotation of
                    in the ED and suggests an expanded role for expansion of                             the tip posteriorly, and advancement.13 Few instances of
                    the role of the bougie beyond difficult airways15,21,22,25 and                       bougie-related complications have been reported in the
                    rescue after failed attempts. 7, 25-27 To our knowledge,                             literature,29-33 and the bougie is generally viewed as a safe
                    first-attempt success in the ED as high as 98% has not previ-                        device34,35; this trial supports this view, with complications
                    ously been reported using any combination of airway devices                          being rare in both groups without clear causative links. Use of
                    or algorithms, though introduction of a new intubation pro-                          the hold-up sign, however, may increase the risk of pneumo-
                    tocol combining the C-MAC video laryngoscope and the bou-                            thorax, especially if the bougie does not have a coudé tip,
                    gie in a helicopter system improved first-attempt success                            which allows penetration of the bougie into smaller, more
                    to above 98%.28                                                                      fragile bronchi.32,36 Because of the danger of the hold-up
                         The trial data may be interpreted as supporting greater ease                    sign, it should not be sought when the intubator knows the
                    of use of the bougie compared with the endotracheal                                  bougie has been correctly placed into the trachea, either by
                    tube + stylet. A greater proportion of operators using the bou-                      visualization of the bougie anterior to the arytenoid carti-
                    gie vs the endotracheal tube never viewed the video laryn-                           lages or detection of tracheal clicks. If sought, the intubator
                    goscopy screen during the procedure (Table 2). Similarly, al-                        should do so gently.
                    though bougie use requires the additional step of placing the
                    endotracheal tube over the bougie, the duration of the first at-                     Limitations
                    tempt with bougie use was shorter (based on the results of the                       This study has several limitations. First, these data are from
                    Cox proportional hazard model) for patients with a difficult air-                    a single institution with a history of bougie use,13,37 hence
                    way characteristic and similar when considering all patients.                        the results may not be generalizable to physicians less
                    Because laryngeal views were comparable between groups,                              familiar with its use. Second, difficult airway characteristics
                    these findings suggest that passing the device into the tra-                         were based on a subjective assessment of the patient before
                    chea is simpler with a bougie compared with an endotracheal                          and during intubation and may be subject to a wide range of
                    tube + stylet.                                                                       interpretation; although interphysician agreement esti-
                         Challenges may be anticipated when learning or perform-                         mates for these difficult airway characteristics have not
                    ing bougie-assisted orotracheal intubation. The endotracheal                         been established, prior work has demonstrated increased
                    tube can encounter resistance at the arytenoid cartilages                            first-attempt failure and intubation-associated complica-
                    when being passed over a bougie. This was observed in 7%                             tions when at least 1 characteristic is present. 4,11 Third,
                    of intubations in the bougie group, but was remedied by                              because not all difficult airway characteristics were ascer-
                    slight withdrawal of the tube, 90° counterclockwise rotation,                        tainable before intubation, we could not stratify randomiza-
                    and readvancement in all cases except 1 (Figure S1 in Supplement                     tion by difficult airway characteristics; therefore the pri-
                    2).12,13 The coudé tip of the bougie can occasionally impinge                        mary analysis represented a postrandomization subgroup

                    jama.com                                                                                                  (Reprinted) JAMA June 5, 2018 Volume 319, Number 21             2187

                                                                    © 2018 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### DOC-001 physical PDF page 10

Source: [jama_driver_2018_oi_180054.pdf](../../../jama_driver_2018_oi_180054.pdf#page=10)

```text
                 Research Original Investigation                                                                 Comparison of Intubation Techniques in Patients With Difficult Airways



                 analysis. However, first-attempt success with bougie use                              first-attempt success and time to intubation. Differential
                 was higher than the endotracheal tube + stylet in subgroups                           treatment of the groups by unblinded emergency physicians
                 both with and without a difficult airway characteristic.                              is also of lesser concern, as first-attempt success in the
                 Fourth, this trial used a single-use, straight bougie with a                          endotracheal tube + stylet group in this trial was similar to
                 coudé tip. These results may not generalize to bougies pack-                          previous studies. Seventh, the assumption of proportional
                 aged in a curled position, which may be more difficult to                             hazards between groups for first-attempt duration was not
                 advance into the glottis.38                                                           upheld, which limits interpretation for this outcome.
                      Fifth, 7% of patients randomized to the endotracheal                             Eighth, patients who underwent intubation with hyperan-
                 tube + stylet group were intubated using a bougie on the                              gulated laryngoscopes were excluded; thus, the results do
                 first attempt (protocol violation); this was ascribed to antici-                      not generalize to these devices.
                 pated difficulty or need for rapid intubation. This bias
                 toward the null had little consequence on the trial results,
                 as intubation success for protocol violations changing from
                 endotracheal tube to bougie was higher than first-attempt
                                                                                                       Conclusions
                 success for the endotracheal tube + stylet group. Sixth, it                           In this emergency department, use of a bougie compared with
                 was not possible to conceal group allocation by blinding the                          an endotracheal tube + stylet resulted in significantly higher
                 emergency physicians and research assistants to the device                            first-attempt intubation success among patients undergoing
                 used for the initial intubation attempt. Biased assessment of                         emergency endotracheal intubation. However, these find-
                 outcomes by research assistants was minimized by objec-                               ings should be considered provisional until the generalizabil-
                 tive definitions of primary and secondary outcomes, such as                           ity is assessed in other institutions and settings.



                 ARTICLE INFORMATION                                      2. Cook T, Behringer EC, Benger J. Airway                12. Dogra S, Falconer R, Latto IP. Successful difficult
                 Accepted for Publication: April 24, 2018.                management outside the operating room:                   intubation: tracheal tube placement over a
                                                                          hazardous and incompletely studied. Curr Opin            gum-elastic bougie. Anaesthesia. 1990;45(9):774-
                 Published Online: May 16, 2018.                          Anaesthesiol. 2012;25(4):461-469.                        776.
                 doi:10.1001/jama.2018.6496
                                                                          3. Brown CA III, Bair AE, Pallin DJ, Walls RM;           13. McGill J. Difficulty passing the bougie. https:
                 Author Contributions: Dr Driver had full access to       NEAR III Investigators. Techniques, success, and         //hqmeded.com/difficulty-passing-the-bougie-2/.
                 all of the data in the study and takes responsibility    adverse events of emergency department adult             Accessed January 20, 2017.
                 for the integrity of the data and the accuracy of the    intubations. Ann Emerg Med. 2015;65(4):363-370.
                 data analysis.                                                                                                    14. Levitan RM, Pisaturo JT, Kinkle WC, Butler K,
                 Concept and design: Driver, Klein, Reardon, Miner,       4. Sakles JC, Chiu S, Mosier J, Walker C, Stolz U.       Everett WW. Stylet bend angles and tracheal tube
                 Fagerstrom, Cole.                                        The importance of first pass success when                passage using a straight-to-cuff shape. Acad Emerg
                 Acquisition, analysis, or interpretation of data: All    performing orotracheal intubation in the                 Med. 2006;13(12):1255-1258.
                 authors.                                                 emergency department. Acad Emerg Med. 2013;20            15. Kidd JF, Dyson A, Latto IP. Successful difficult
                 Drafting of the manuscript: Driver, Klein,               (1):71-78.                                               intubation: use of the gum elastic bougie.
                 McGill, Cole.                                            5. Macintosh RR. An aid to oral intubation. BMJ.         Anaesthesia. 1988;43(6):437-438.
                 Critical revision of the manuscript for important        1949;1(4591):28.                                         16. Hasegawa K, Shigemitsu K, Hagiwara Y, et al;
                 intellectual content: Driver, Prekker, Klein, Reardon,   6. Driver B, Dodd K, Klein LR, et al. The bougie and     Japanese Emergency Medicine Research Alliance
                 Miner, Fagerstrom, Cleghorn, Cole.                       first-pass success in the emergency department.          Investigators. Association between repeated
                 Statistical analysis: Driver, Klein.                     Ann Emerg Med. 2017;70(4):473-478.                       intubation attempts and adverse events in
                 Obtained funding: Miner.                                                                                          emergency departments: an analysis of a
                 Administrative, technical, or material support:          7. Combes X, Le Roux B, Suen P, et al.
                                                                          Unanticipated difficult airway in anesthetized           multicenter prospective observational study. Ann
                  Driver, Reardon, Miner, Fagerstrom, Cleghorn.                                                                    Emerg Med. 2012;60(6):749-754.
                 Supervision: Driver, Reardon, Miner, McGill, Cole.       patients: prospective validation of a management
                                                                          algorithm. Anesthesiology. 2004;100(5):1146-1150.        17. Mort TC. Emergency tracheal intubation:
                 Conflict of Interest Disclosures: All authors have                                                                complications associated with repeated
                 completed and submitted the ICMJE Form for               8. Driver BE, McGill JW. Emergency department
                                                                          airway management of severe angioedema: a video          laryngoscopic attempts. Anesth Analg. 2004;99(2):
                 Disclosure of Potential Conflicts of Interest. Dr                                                                 607-613.
                 Miner reported grant funding from Securisyn              review of 45 intubations. Ann Emerg Med. 2017;69
                 Medical. No other disclosures were reported.             (5):635-639.                                             18. Rognås L, Hansen TM, Kirkegaard H, Tønnesen E.
                                                                          9. Levitan RM, Heitz JW, Sweeney M, Cooper RM.           Pre-hospital advanced airway management by
                 Meeting Presentation: This article was presented                                                                  experienced anaesthesiologists: a prospective
                 at the Society for Academic Emergency Medicine           The complexities of tracheal intubation with direct
                                                                          laryngoscopy and alternative intubation devices.         descriptive study. Scand J Trauma Resusc Emerg Med.
                 on May 16, 2018.                                                                                                  2013;21:58.
                                                                          Ann Emerg Med. 2011;57(3):240-247.
                 Additional Contributions: We thank the Hennepin                                                                   19. Duggan LV, Minhas KS, Griesdale DE, et al.
                 County Medical Center residents and Research             10. Sakles JC, Mosier J, Chiu S, Cosentino M, Kalin L.
                                                                          A comparison of the C-MAC video laryngoscope to          Complications increase with greater than one
                 Associate Program for their contribution to                                                                       endotracheal intubation attempt: experience
                 research in emergency medicine. They did not             the Macintosh direct laryngoscope for intubation in
                                                                          the emergency department. Ann Emerg Med.                 in a Canadian adult tertiary-care teaching
                 receive compensation for their contributions.                                                                     center. J Clin Anesth. 2014;26(2):167.
                                                                          2012;60(6):739-748.
                                                                                                                                   doi:10.1016/j.jclinane.2013.12.005
                 REFERENCES                                               11. Joshi R, Hypes CD, Greenberg J, et al. Difficult
                                                                          airway characteristics associated with first-attempt     20. Nolan JP, Wilson ME. Orotracheal intubation in
                 1. Rui PKK. National Hospital Ambulatory Medical                                                                  patients with potential cervical spine injuries: an
                 Care Survey: 2014 emergency department                   failure at intubation using video laryngoscopy in the
                                                                          intensive care unit. Ann Am Thorac Soc. 2017;14(3):      indication for the gum elastic bougie. Anaesthesia.
                 summary tables. https://www.cdc.gov/nchs/data                                                                     1993;48(7):630-633.
                 /nhamcs/web_tables/2014_ed_web_tables.pdf.               368-375.
                 Accessed February 5, 2018.                                                                                        21. Nolan JP, Wilson ME. An evaluation of the gum
                                                                                                                                   elastic bougie: intubation times and incidence of
                                                                                                                                   sore throat. Anaesthesia. 1992;47(10):878-881.


          2188   JAMA June 5, 2018 Volume 319, Number 21 (Reprinted)                                                                                                           jama.com

                                                                 © 2018 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```

### DOC-001 physical PDF page 11

Source: [jama_driver_2018_oi_180054.pdf](../../../jama_driver_2018_oi_180054.pdf#page=11)

```text
                    Comparison of Intubation Techniques in Patients With Difficult Airways                                                              Original Investigation Research



                    22. Latto IP, Stacey M, Mecklenburgh J,                 gynecologic, and thyroid surgery. Anesthesiology.         33. Kadry M, Popat M. Pharyngeal wall
                    Vaughan RS. Survey of the use of the gum elastic        2011;114(1):25-33.                                        perforation—an unusual complication of blind
                    bougie in clinical practice. Anaesthesia. 2002;57(4):   27. Jabre P, Combes X, Leroux B, et al. Use of gum        intubation with a gum elastic bougie. Anaesthesia.
                    379-384.                                                elastic bougie for prehospital difficult intubation.      1999;54(4):404-405.
                    23. Sakles JC, Patanwala AE, Mosier JM, Dicken JM.      Am J Emerg Med. 2005;23(4):552-555.                       34. Hodzovic I, Latto IP, Henderson JJ. Bougie
                    Comparison of video laryngoscopy to direct              28. Ångerman S, Kirves H, Nurmi J. A before-and-          trauma—what trauma? Anaesthesia. 2003;58(2):
                    laryngoscopy for intubation of patients with            after observational study of a protocol for use of the    192-193.
                    difficult airway characteristics in the emergency       C-MAC video laryngoscope with a Frova introducer in       35. Rai MR. The humble bougie… 40 years and still
                    department. Intern Emerg Med. 2014;9(1):93-98.          pre-hospital rapid sequence intubation. Anaesthesia.      counting? Anaesthesia. 2014;69(3):199-203.
                    24. Park L, Zeng I, Brainard A. Systematic review       2018;73(3):348-355.                                       36. Marson BA, Anderson E, Wilkes AR, Hodzovic I.
                    and meta-analysis of first-pass success rates in        29. Smith BL. Haemopneumothorax following                 Bougie-related airway trauma: dangers of the
                    emergency department intubation: creating a             bougie-assisted tracheal intubation. Anaesthesia.         hold-up sign. Anaesthesia. 2014;69(3):219-223.
                    benchmark for emergency airway care. Emerg Med          1994;49(1):91.
                    Australas. 2017;29(1):40-47.                                                                                      37. McGill JW, Vogel EC, Rodgerson JD. Use of the
                                                                            30. Özcan ATD, Balcı CA, Aksoy ŞM, Uğur G,                gum elastic bougie as an adjunct for orotracheal
                    25. Gataure PS, Vaughan RS, Latto IP. Simulated         Kanbak O, Müderrris T. Upper airway injury caused         intubation in the emergency department. Acad
                    difficult intubation: comparison of the gum elastic     by gum elastic bougie. Uttar Pradesh, India: Int J Case   Emerg Med. 2000;7:526-527.
                    bougie and the stylet. Anaesthesia. 1996;51(10):        Rep Images; 2017:8.
                    935-938.                                                                                                          38. Levitan RM. Avoiding common laryngoscopy
                                                                            31. Arndt GA, Cambray AJ, Tomasson J. Intubation          errors, part II. Emergency Physicians Monthly.
                    26. Amathieu R, Combes X, Abdi W, et al.                bougie dissection of tracheal mucosa and                  http://epmonthly.com/article/avoiding-common
                    An algorithm for difficult airway management,           intratracheal airway obstruction. Anesth Analg.           -laryngoscopy-errors-part-ii/. Accessed
                    modified for modern optical devices (Airtraq            2008;107(2):603-604.                                      January 10, 2018.
                    laryngoscope; LMA CTrach): a 2-year prospective
                    validation in patients for elective abdominal,          32. Prabhu A, Pradhan P, Sanaka R, Bilolikar A.
                                                                            Bougie trauma—it is still possible. Anaesthesia.
                                                                            2003;58(8):811-813.




                    jama.com                                                                                                   (Reprinted) JAMA June 5, 2018 Volume 319, Number 21         2189

                                                                © 2018 American Medical Association. All rights reserved.
Downloaded from jamanetwork.​com by University of Arizona Health Sciences Library user on 08/​24/​2026

```
