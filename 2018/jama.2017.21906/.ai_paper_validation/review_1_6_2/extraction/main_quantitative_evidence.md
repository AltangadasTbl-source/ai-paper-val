# Main quantitative evidence reconstruction

Scope: DOC-001, `jama_huffman_2018_oi_170166.pdf`, physical PDF pages 1–12, printed pages 567–578. Every location has document role REPORT. Reconstruction is from the supplied article, reusable Poppler native/layout text, and corresponding page images, independently of previous scientific review artifacts. Source SHA-256: 11311a6bb5c7a4be734ed60776b308f525ad101671ccc8d34bab18735aaca5f5. No diagnoses or candidate judgments are made here.

Source links below are relative to this extraction artifact. A page link identifies the direct source; the row label identifies the within-page location. C = control/usual care, I = intervention/tool kit. Unless stated otherwise, quantities are participant-level, C is the reference, contrasts are I minus C or I versus C, differences in binary outcomes use percentage points, and all printed intervals are 95% CIs. Nulls are 0 for differences and coefficients, 1 for ORs. No result-specific P value, test statistic, or standard error is printed unless explicitly recorded. The final inferential threshold and sidedness are in S006.

Reusable locators: `.ai_paper_validation/review_1_5_2/preprocessing/native_text/jama_huffman_2018_oi_170166.txt` (all pages), corresponding layout file (all pages, with known ordering limitations at pp.4,8), saved 180-dpi corresponding images pp.1,4–10, and corresponding 120-dpi images pp.2,3 in `.ai_paper_validation/review_1_6_1/preprocessing/`. Engine: Poppler pdftotext/pdftoppm, CPU; exact source correspondence assessed by the curator. No fresh OCR or extraction was required. Page 11–12 native text contains no result-bearing diagram or table.

## Page coverage

| Physical page | Direct location | Complete mapped content | Relationship coverage | Status |
|---|---|---|---|---|
| 1 | [p.1](../../../jama_huffman_2018_oi_170166.pdf#page=1), abstract | Design/calendar; allocation counts at all steps; eligibility, follow-up, age/sex/STEMI; outcome definition; primary result and conclusion; medication/tobacco and adverse-event claims | N001,N008–N010; S001–S004,S057,S064–S066 | COMPLETE |
| 2 | [p.2](../../../jama_huffman_2018_oi_170166.pdf#page=2), introduction, Key Points, Methods | Background quantities, Key Points results; design, hospitals, participant eligibility, randomized unit, concealment and strata | N001,N013; S001,S003,S057 | COMPLETE |
| 3 | [p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3), Methods | Intervention exposure/training; every outcome component/status; sample-size inputs; all primary, secondary, subgroup, post hoc, ITT, interim and multiplicity specifications | N001; S001–S008 | COMPLETE |
| 4 | [p.4](../../../jama_huffman_2018_oi_170166.pdf#page=4), Figure 1 | All control-step and cohort-step enrolled, lost, analyzed, excluded and exclusion-component counts; hospital and calendar labels; caption | N002–N008; S001,S005 | COMPLETE |
| 5 | [p.5](../../../jama_huffman_2018_oi_170166.pdf#page=5), Table 1, Methods/Results | All 27 baseline rows, group sizes, denominators, crude differences/intervals, footnotes and conversions; outcome monitoring and total flow narrative | N008,N011,N012; S008–S035 | COMPLETE |
| 6 | [p.6](../../../jama_huffman_2018_oi_170166.pdf#page=6), Table 2, Results | All 21 process/time rows, eligible denominators, adjusted differences/ORs/coefficients, nonestimable rows, footnotes; missing-follow-up comparison, baseline aggregates and matching process narrative | N009,N010; S036–S056,S092 | COMPLETE |
| 7 | [p.7](../../../jama_huffman_2018_oi_170166.pdf#page=7), Table 3, Results | All ten primary/secondary rows, counts, percentages, both adjusted analyses, ICCs and footnotes; every process narrative value and primary/sensitivity claim | S036–S066 | COMPLETE |
| 8 | [p.8](../../../jama_huffman_2018_oi_170166.pdf#page=8), Figure 2, Results | Both panels, every plotted estimate/interval, all 30 contributor counts repeated in both panels, axis/legend/caption; mortality and post hoc claims | S058,S081–S091 | COMPLETE |
| 9 | [p.9](../../../jama_huffman_2018_oi_170166.pdf#page=9), Figure 3, Results/Discussion | All 14 subgroup rows with counts/denominators/rates/differences/ORs/CIs; forest axis/reference/direction/precision; post hoc result continuation and all matching conclusions | S057–S080,S091 | COMPLETE |
| 10 | [p.10](../../../jama_huffman_2018_oi_170166.pdf#page=10), Discussion/Limitations/Conclusions | Subgroup consistency, ICC/power and multiplicity claims; external descriptive quantities; final primary conclusion | N013; S002,S006,S057,S067–S080 | COMPLETE |
| 11 | [p.11](../../../jama_huffman_2018_oi_170166.pdf#page=11), article information/references | No applicable new trial quantitative relationship. Named investigators, grants, and bibliographic numbers; registry sample citation already mapped in N013 | N013 corroborating reference only | COMPLETE; NO_APPLICABLE_NEW_RESULT |
| 12 | [p.12](../../../jama_huffman_2018_oi_170166.pdf#page=12), references | No applicable new trial quantitative relationship. Reference numbering, years, volumes/pages and cited publication titles only | None | COMPLETE; NO_APPLICABLE_RESULT |

## Numeric relationships

### N001 — Calendar, randomized units and exposure

[p.1](../../../jama_huffman_2018_oi_170166.pdf#page=1) abstract; [p.2](../../../jama_huffman_2018_oi_170166.pdf#page=2) Methods; [p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3) Interventions; [p.4](../../../jama_huffman_2018_oi_170166.pdf#page=4) Figure 1. Hospitals are randomized clusters; participants are consecutively presenting STEMI/NSTEMI patients. 63 hospitals; five one-way crossover steps after step 0; six 4-month periods over 24 months. Study November 10,2014–November 9,2016; final follow-up December 31,2016. Steps: 0 November 10,2014–March 9,2015; 1 March 10–July 9,2015; 2 July 10–November 9,2015; 3 November 10,2015–March 9,2016; 4 March 10–July 9,2016; 5 July 10–November 9,2016. Cohorts 1–5: 12,13,13,13,12 hospitals. Sites informed two weeks before crossover; 12 or13 per step; randomization strata anticipated ≤200,201–500,501–1000,>1000 participants. Hospitals required two quality-team individuals. Training 90–120 minutes/site; no transition period; allocation determined by admission date. Monthly audit reports and biweekly central monitoring. No person-time total is printed.

### N002 — Figure 1 control period counts

[p.4](../../../jama_huffman_2018_oi_170166.pdf#page=4), upper control blocks. Row tuple: hospitals; enrolled; lost to follow-up; included in analysis; excluded; cardiac markers missing/not elevated; transferred after thrombolysis without further treatment; admitted outside study period; timeline discrepancy. Unprinted exclusion categories are recorded as absent, not imputed zero.

| Step | Printed tuple |
|---|---|
| 0 | 63;3107;42;2915;192;172;18;absent;2 |
| 1 | 51;2765;45;2649;116;101;15;absent;absent |
| 2 | 38;2328;54;2251;77;67;10;absent;absent |
| 3 | 25;1450;27;1422;28;25;3;absent;absent |
| 4 | 12;844;2;829;15;9;2;4;absent |
| 5 | No control block; abstract explicitly n=0 |

### N003 — Figure 1 intervention cohort 1

[p.4](../../../jama_huffman_2018_oi_170166.pdf#page=4), green blocks; 12 hospitals; steps1–5. Tuple enrolled;lost;included;excluded;markers;transferred;outside period;timeline.

| Step | Printed tuple |
|---|---|
| 1 | 706;2;662;44;43;1;absent;absent |
| 2 | 593;6;542;51;47;3;absent;1 |
| 3 | 757;0;654;103;101;2;absent;absent |
| 4 | 659;3;605;54;52;1;absent;1 |
| 5 | 675;10;648;27;16;4;7;absent |

### N004 — Figure 1 intervention cohort 2

[p.4](../../../jama_huffman_2018_oi_170166.pdf#page=4), blue blocks;13 hospitals; steps2–5; tuple as N003.

| Step | Printed tuple |
|---|---|
| 2 | 790;18;723;67;62;5;absent;absent |
| 3 | 821;4;785;36;34;2;absent;absent |
| 4 | 764;6;727;37;34;3;absent;absent |
| 5 | 627;28;600;27;26;1;absent;absent |

### N005 — Figure 1 intervention cohort 3

[p.4](../../../jama_huffman_2018_oi_170166.pdf#page=4), purple blocks;13 hospitals; steps3–5; tuple as N003. At steps3,4 the display says “Analyzed”; at step5 “Included in analysis.”

| Step | Printed tuple |
|---|---|
| 3 | 1076;10;993;83;64;19;absent;absent |
| 4 | 1071;8;1022;49;19;29;absent;1 |
| 5 | 991;7;964;27;20;7;absent;absent |

### N006 — Figure 1 intervention cohort 4

[p.4](../../../jama_huffman_2018_oi_170166.pdf#page=4), red blocks;13 hospitals; tuple as N003. Step4:895;7;860;35;32;2;absent;1. Step5:637;7;627;10;9;1;absent;absent.

### N007 — Figure 1 intervention cohort 5

[p.4](../../../jama_huffman_2018_oi_170166.pdf#page=4), yellow block;12 hospitals; step5 tuple as N003:1001;9;896;105;21;4;80;absent.

### N008 — Recruitment, exclusion and allocation totals

[p.1](../../../jama_huffman_2018_oi_170166.pdf#page=1) interventions/results; [p.2](../../../jama_huffman_2018_oi_170166.pdf#page=2) Key Points; [p.5](../../../jama_huffman_2018_oi_170166.pdf#page=5) Results; [p.6](../../../jama_huffman_2018_oi_170166.pdf#page=6) Results. Recruited22,557 from63 hospitals; excluded markers954, transfer132, outside-period91, timeline6; eligible21,374; I11,308(53%), C10,066(47%). Abstract C step0–5 counts2915,2649,2251,1422,829,0; I counts0,662,1265,2432,3214,3735. Figure1 supports cohort-specific inputs N002–N007; excluded persons and lost-follow-up persons are distinct categories. Figure1 caption: all hospitals approached agreed and were included; single randomization before enrollment; lost participants include three unsuccessful contact attempts and sites not performing follow-up; lost participants remained in analysis. Hospital distribution narrative:67% private,14% government affiliated with medical colleges,19% nonprofit/charity; Table1 exact hospital counts S026–S028.

### N009 — Overall descriptive baseline

[p.1](../../../jama_huffman_2018_oi_170166.pdf#page=1) Results: mean age60.6(SD12.0)y;16,183 men(76%);13,689 STEMI(64%). [p.6](../../../jama_huffman_2018_oi_170166.pdf#page=6) Participants: mean60.6y;76% men;31% tobacco history;44% diabetes;64% STEMI. C symptom-to-door median240(IQR120–840)min; I255(111–825)min. All group-specific inputs/intervals are in S009–S025; overall denominator21,374.

### N010 — Follow-up population

[p.1](../../../jama_huffman_2018_oi_170166.pdf#page=1) Results:21,079(99%) completed. [p.5](../../../jama_huffman_2018_oi_170166.pdf#page=5) Results:30-day follow-up99%. [p.6](../../../jama_huffman_2018_oi_170166.pdf#page=6) Results:295(1%) incomplete outcomes among21,374;215 not followed by enrolling site;80 unreachable after3 attempts. Site contact rule also [p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3) Outcomes; Figure1 counts N002–N007. Table3 header continues full randomized eligible C10,066/I11,308; S005 states ITT. Troponin comparison S092.

### N011 — Monitoring quantities

[p.5](../../../jama_huffman_2018_oi_170166.pdf#page=5), Statistical Analysis continuation: one site with unusually high reinfarction rate led to quality-assurance sampling10% of cases and corresponding controls; two additional sites identified;13 primary-outcome changes(1% of overall events). Primary component counts in S057–S063; no sampling denominator printed. Software Stata14,SAS9.4,R3.3.0,StatTag3.0.

### N012 — Table 1 unit conversions

[p.5](../../../jama_huffman_2018_oi_170166.pdf#page=5), Table1 footnotes: LDL mg/dL to mmol/L ×0.0259; triglycerides mg/dL to mmol/L ×0.0113; creatinine mg/dL to μmol/L ×88.4; glucose mg/dL to mmol/L ×0.0555. IQR=interquartile range; incomplete-variable totals printed. Hemoglobin row unit is printed mg/dL and retained exactly in S025.

### N013 — Background/external quantitative context

[p.2](../../../jama_huffman_2018_oi_170166.pdf#page=2), introduction:2015 global fatal MI7.3million(95% uncertainty interval6.8–7.8million); prior Kerala registry25,748 patients/125 hospitals; sampling frame125 also Methods. [p.10](../../../jama_huffman_2018_oi_170166.pdf#page=10), Discussion: CPACS-3 >29,000 Chinese participants; 2014 ACTION-GWTG in-hospital mortality6.4% STEMI/3.4% NSTEMI. These are cited contextual values, not ACS QUIK result populations; no external verification performed. Registry25,748 repeated in reference4 [p.11](../../../jama_huffman_2018_oi_170166.pdf#page=11).

## Statistical relationships

### S001 — Design and intervention allocation

[p.1](../../../jama_huffman_2018_oi_170166.pdf#page=1) abstract; [p.2](../../../jama_huffman_2018_oi_170166.pdf#page=2) Study Design/Randomization; [p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3) Interventions; [p.4](../../../jama_huffman_2018_oi_170166.pdf#page=4) caption. Cluster randomized stepped wedge, central computer randomization stratified in four projected-recruitment groups; hospitals cross C→I once; participants and personnel unblinded; hospital cohort concealed until two weeks before crossover. Numeric design/time/exposure inputs N001; all individual results refer to admission-date allocation. Usual care versus tool kit: audit/feedback, admission/discharge order sets, patient education, emergency care and quality training. No transition period; no randomized drug dose is specified.

### S002 — Sample-size and power relationship

[p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3), Statistical Analysis:target15,750 participants,63 hospitals,five steps,80% power,2.4% absolute reduction in MACE,two-sided α=.05,5% loss,ICC0.05. Effect based on leading/lagging hospitals in previous observational work. Baseline event probability not stated in this paragraph. [p.10](../../../jama_huffman_2018_oi_170166.pdf#page=10), Limitations:observed ICCs higher than anticipated reduced power; event rates lower and care higher than anticipated; authors consider material change to primary estimate unlikely. Observed outcome ICCs S057–S066; achieved sample N008.

### S003 — Outcomes and status

[p.1](../../../jama_huffman_2018_oi_170166.pdf#page=1) Main Outcomes; [p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3) Outcomes. Primary30-day composite death/reinfarction/stroke/major GUSTO bleeding; reinfarction Third Universal Definition; bleeding intracerebral hemorrhage or hemodynamic compromise requiring treatment. Secondary30-day all-cause/cardiovascular mortality,in-hospital mortality,30-day reinfarction/stroke/major bleeding,optimal in-hospital medication,optimal discharge medication,tobacco advice. In-hospital composite aspirin+ADP antagonist+anticoagulant+β-blocker; statin additionally predefined but not collected. Discharge composite aspirin+ADP antagonist+statin+β-blocker. ADP agents clopidogrel/prasugrel/ticagrelor. Post hoc expanded composite adds incident in-hospital heart failure,cardiogenic shock,cardiac arrest. Table3 definitions S057–S066; expanded result S091. Outcomes assessed at sites in person/telephone and reported centrally; assessors not blinded.

### S004 — Model specifications and contrasts

[p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3), Statistical Analysis; Table2 [p.6](../../../jama_huffman_2018_oi_170166.pdf#page=6); Table3 [p.7](../../../jama_huffman_2018_oi_170166.pdf#page=7). Primary mixed-effects logistic regression:random hospital effect,fixed time effect for each4-month step. Secondary additional GRACE covariates age,sex,MI type,systolic BP,heart rate,creatinine,acute heart failure,cardiogenic shock,resuscitated cardiac arrest. Baseline descriptions unadjusted and adjusted for clustering/time. Reported ORs I versus C; risk differences I minus C. Table2 footnote b literally states ORs/β-coefficients “are calculated as the difference in marginal effects” in mixed-effects logistic or quantile regression including random-effects term for clustering and temporal trends. Table3 footnote a uses corresponding wording for ORs and random hospital effect; primary additionally time-adjusted. These labels are transcribed without reinterpretation.

### S005 — Analysis population and missing outcomes

[p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3), Statistical Analysis:all results ITT; prespecified participant-level results reported. N008/N010 contain recruited/eligible/followed denominators. [p.7](../../../jama_huffman_2018_oi_170166.pdf#page=7), Primary Analysis:similar primary results after multiple imputation of missing/lost-follow-up data; hypothetical missing-event scenarios and multiple imputation gave broader range but plausible results consistent with primary analysis. No main-paper imputation counts, specific scenarios, or numerical sensitivity estimates printed. Table2 excludes medication contraindications and uses eligible reported process denominators; discharged-only measures and EF≤40% restriction specified; Table3 medication/tobacco restricted denominators as below.

### S006 — Interim, significance and multiplicity rules

[p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3), Statistical Analysis:interim12months,only study biostatisticians unblinded; O’Brien–Fleming stopping boundary z>2.797,two-sided significance .005 interim; z>1.977,two-sided .048 final. No additional a priori secondary-outcome multiplicity adjustment; secondary analyses exploratory. [p.10](../../../jama_huffman_2018_oi_170166.pdf#page=10), Limitations repeats no multiple-comparison adjustment. Result displays use95%CIs; no result-specific z/P is supplied except S092.

### S007 — Subgroups and post hoc interaction

[p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3), Statistical Analysis:prespecified age,sex,STEMI/NSTEMI,hospital size,type; interactions tested. Figure3 full rows S067–S080; no subgroup interaction P values printed in main paper. Post hoc exposure-time interaction with adjusted30-day MACE; [p.8](../../../jama_huffman_2018_oi_170166.pdf#page=8) results overall similar,eTable6 pointer. Post hoc expanded composite S091. [p.9](../../../jama_huffman_2018_oi_170166.pdf#page=9) Figure3 narrative and [p.10](../../../jama_huffman_2018_oi_170166.pdf#page=10) Discussion claim similar/consistent effects across prespecified subgroups despite between-hospital heterogeneity; eFigure1A residual plot,eFigure1B crude within-hospital differences,eFigure2A/B temporal outcomes cited, no corresponding main-paper numbers.

### S008 — Monitoring/statistical implementation

[p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3) Statistical Analysis continuation [p.5](../../../jama_huffman_2018_oi_170166.pdf#page=5):biweekly risk-based central monitoring,blinded site surveys following high reinfarction site,13 primary-event changes; quantities N011. Software versions N011. Data/code location printed but not accessed. No additional method is inferred.

### Table 1 complete baseline relationships: S009–S035

Direct location for every following row: [p.5](../../../jama_huffman_2018_oi_170166.pdf#page=5), Table1 “Baseline Characteristics of ACS QUIK Patients and Hospitals by Intervention and Control Group,” exact named row. C n10,066/I n11,308 unless variable-specific n shown. Differences explicitly **crude I minus C**,95%CI; no test/P/model adjustment in this display. Binary differences percentage points; continuous differences same unit as row. Each row contains both its raw numerical and interval relationship; no separate N duplicate. Hospital row n denotes hospitals, whereas C/I values denote patients. Matching overall narrative N009 and hospital distribution N008; no unprinted baseline P values inferred.

| ID | Row/unit/statistic | C printed value | I printed value | Crude difference (95% CI) |
|---|---|---|---|---|
| S009 | Age,mean(SD),years | 60.3(12.0) | 60.9(12.1) | 0.6(0.3 to1.0) |
| S010 | Male,n(%) | 7654(76.0) | 8529(75.4) | −0.6(−1.8 to0.5) |
| S011 | Tobacco history,n(%) | 3772(37.5) | 2842(25.1) | −12.3(−13.6 to−11.1) |
| S012 | Diabetes history,n(%) | 4151(41.2) | 5333(47.2) | 5.9(4.6 to7.3) |
| S013 | Transferred from other facility,n(%) | 4202(41.7) | 4199(37.1) | −4.6(−5.9 to−3.3) |
| S014 | No insurance,n(%) | 6878(68.3) | 8664(76.6) | 8.3(7.1 to9.5) |
| S015 | STEMI,n(%) | 6921(68.8) | 6768(59.9) | −8.9(−10.2 to−7.6) |
| S016 | Symptom-to-door,median(IQR),min | 240(120–840),n9711 | 255(111–825),n10,849 | 15(4 to26) |
| S017 | Weight,mean(SD),kg | 63.6(9.8),n10,065 | 63.3(9.6),n11,304 | −0.3(−0.5 to0.0) |
| S018 | Systolic BP,mean(SD),mmHg | 138.1(29.1),n10,061 | 139.0(28.9),n11,303 | 0.9(0.1 to1.7) |
| S019 | Heart rate,mean(SD),per min | 80.0(18.7),n10,065 | 79.9(19.1),n11,303 | −0.1(−0.6 to0.5) |
| S020 | Initial troponin,median(IQR),ng/mL | 1.6(0.4–8.0),n4566 | 1.1(0.2–4.4),n4483 | −0.5(−0.7 to−0.4) |
| S021 | LDL cholesterol,mean(SD),mg/dL | 126.2(40.3),n7288 | 119.1(41.2),n7542 | −7.1(−8.4 to−5.8) |
| S022 | Triglycerides,median(IQR),mg/dL | 121(89–167),n7308 | 122(90–163),n7552 | 1(−1 to3) |
| S023 | Creatinine,median(IQR),mg/dL | 1.0(0.8–1.2),n4246 | 1.0(0.9–1.2),n9589 | 0.0(0.0 to0.0) |
| S024 | Fasting glucose,median(IQR),mg/dL | 124(98–172),n6658 | 130(105–180),n6740 | 6(4 to8) |
| S025 | Hemoglobin,mean(SD),printed mg/dL | 13.3(2.0),n9763 | 13.2(2.0),n11,079 | −0.1(−0.2 to0.0) |
| S026 | Government,hospitals n9; patients n(%) | 4097(40.7) | 3036(26.8) | −13.9(−15.1 to−12.6) |
| S027 | Nonprofit/charity,hospitals n12 | 2785(27.7) | 2964(26.2) | −1.5(−2.7 to−0.3) |
| S028 | Private,hospitals n42 | 3184(31.6) | 5308(46.9) | 15.3(14.0 to16.6) |
| S029 | Extra large >1000,hospitals n5 | 1853(18.4) | 1707(15.1) | −3.3(−4.3 to−2.3) |
| S030 | Large501–1000,hospitals n15 | 3561(35.4) | 4962(43.9) | 8.5(7.2 to9.8) |
| S031 | Medium201–500,hospitals n24 | 3847(38.2) | 3568(31.6) | −6.7(−7.9 to−5.4) |
| S032 | Small≤200,hospitals n19 | 805(8.0) | 1071(9.5) | 1.5(0.7 to2.2) |
| S033 | Cath lab installed during study,hospitals n3 | 171(1.7) | 325(2.9) | 1.2(0.8 to1.6) |
| S034 | No cath lab,hospitals n17 | 1998(19.8) | 1554(13.7) | −6.1(−7.1 to−5.1) |
| S035 | Cath lab yes,hospitals n43 | 7897(78.5) | 9429(83.4) | 4.9(3.9 to6.0) |

### Table 2 complete process/time relationships: S036–S056

Direct location for each row: [p.6](../../../jama_huffman_2018_oi_170166.pdf#page=6), Table2 “Characteristics and Association of Process of Care and Time-Based Outcomes by Treatment Group, Adjusted for Within-Hospital Clustering and Temporal Trends.” Headers C n10,066/I n11,308. Printed raw numerator/eligible reported denominator(%); medication contraindications excluded, discharge only among discharged, ACE/ARB only discharged EF≤40%. Differences column printed “Difference,%(95%CI)” for all rows, including minute-valued time rows; coefficient rows marked c. Footnote model/measure wording S004. All effect intervals95%; I versus C; no P printed. For time rows median/IQR and n are recorded, final column β rather than OR; no unstated calculation imposed.

| ID | Row | C | I | Difference (95% CI) | OR or β (95% CI) |
|---|---|---|---|---|---|
| S036 | Prehospital aspirin | 1696/10,052(16.9) | 2100/11,300(18.6) | 3.80(2.08 to5.52) | 1.40(1.21–1.62) |
| S037 | Prehospital thrombolysis,STEMI | 25/6921(0.4) | 37/6768(0.5) | −0.04(−0.76 to0.68) | 0.95(0.40–2.28) |
| S038 | In-hospital aspirin | 9858/10,042(98.2) | 11,027/11,286(97.7) | −0.05(−0.95 to0.84) | 0.98(0.69–1.39) |
| S039 | In-hospital second antiplatelet | 9861/10,050(98.1) | 11,112/11,297(98.4) | −0.05(−0.89 to0.79) | 0.98(0.67–1.43) |
| S040 | In-hospital β-blocker | 3676/9874(37.2) | 4638/10,885(42.6) | 6.25(4.10 to8.40) | 1.46(1.29–1.65) |
| S041 | In-hospital anticoagulant | 8602/10,051(85.6) | 9654/11,281(85.6) | 2.60(0.87 to4.33) | 1.27(1.09–1.49) |
| S042 | Echocardiography | 9209/10,066(91.5) | 10,516/11,308(93.0) | 5.62(3.35 to7.89) | 2.50(1.95–3.21) |
| S043 | Diagnostic angiography | 6181/10,066(61.4) | 6500/11,308(57.5) | Nonestimable | Nonestimable |
| S044 | PCI | 5282/10,066(52.5) | 5271/11,308(46.6) | −1.66(−3.27 to−0.04) | 0.87(0.77–0.99) |
| S045 | Primary PCI,STEMI | 3476/6921(50.2) | 3234/6768(47.8) | −1.87(−3.85 to0.11) | 0.86(0.73–1.01) |
| S046 | Door-to-balloon,STEMI,median(IQR),min | 65(53–105),n4022 | 77(55–118),n3639 | 6.18(−4.78 to17.14) | β13.00(3.64–22.36) |
| S047 | Thrombolysis,STEMI | 1596/6921(23.1) | 1571/6768(23.2) | 5.56(3.21 to7.91) | 1.59(1.33–1.92) |
| S048 | Door-to-needle,STEMI,median(IQR),min | 44(30–67),n1455 | 45(27–75),n1433 | 0.40(−5.23 to6.03) | β5.00(−5.20–15.20) |
| S049 | Any reperfusion,STEMI | 5067/6921(73.2) | 4805/6768(71.0) | 3.43(0.87 to6.00) | 1.24(1.06–1.46) |
| S050 | Rescue PCI,STEMI | 644/6891(9.3) | 1031/6767(15.2) | 2.45(0.51 to4.38) | 1.39(1.08–1.79) |
| S051 | Discharge aspirin | 8777/8998(97.5) | 10,360/10,559(98.1) | 1.36(0.23 to2.49) | 1.65(1.15–2.37) |
| S052 | Discharge second antiplatelet | 8824/9011(97.9) | 10,377/10,580(98.1) | 0.41(−0.31 to1.13) | 1.24(0.86–1.79) |
| S053 | Discharge β-blocker | 5808/8894(65.3) | 6799/10,178(66.8) | 6.69(4.43 to8.95) | 1.48(1.30–1.68) |
| S054 | Discharge statin | 8700/9006(96.6) | 10,289/10,579(97.3) | 1.21(0.07 to2.35) | 1.42(1.04–1.92) |
| S055 | Discharge ACE inhibitor/ARB,EF≤40% | 534/1029(51.9) | 643/1495(43.0) | 6.57(0.58 to12.57) | 1.45(1.03–2.04) |
| S056 | Cardiac rehabilitation referral | 2362/9228(25.6) | 3322/10,791(30.8) | Nonestimable | Nonestimable |

Matching narrative claims and exact copies: [p.6](../../../jama_huffman_2018_oi_170166.pdf#page=6), Results: S036 I18.6%/C16.9%,RD3.80(2.08–5.52),OR1.40(1.21–1.62); S037 both<1%; S038/S039 both>95% and similar; S040 I43%/C37%,RD6.25(4.10–**8.10**),OR1.46(CI continuation1.29–1.65 on p.7). [p.7](../../../jama_huffman_2018_oi_170166.pdf#page=7), Results: S041 I86%/C86%,RD2.60(0.87–4.33),OR1.27(1.09–1.49); S042 I93%/C92%,RD5.62(3.35–7.89),OR2.50(1.95–3.21); S047 I23%/C23%,RD5.56(3.21–7.91),OR1.59(1.33–1.92); S049 I71%/C73%,RD3.43(0.87–6.00),OR1.24(1.06–1.46); S050 I15%/C9%,RD2.45(0.51–4.38),OR1.39(1.08–1.79); S043 lower I58%/C61%; S044 lower I47%/C53%,RD−1.66(−3.27 to−0.04),OR0.87(0.77–0.99); S051 I98%/C98%,RD1.36(0.23–2.49),OR1.65(1.15–2.37); S053 I67%/C65%,RD**6.63**(4.43–8.95),OR**1.47**(1.30–1.68); S054 I97%/C97%,RD1.21(0.07–2.35),OR1.42(1.04–1.92); S055 I43%/C52%,RD6.57(0.58–12.57),OR1.45(1.03–2.04); S056 I31%/C26%; S052 and tobacco advice described high>95% and similar. Printed differences between copies are retained verbatim without adjudication. [p.1](../../../jama_huffman_2018_oi_170166.pdf#page=1) abstract and [p.9](../../../jama_huffman_2018_oi_170166.pdf#page=9) Discussion summarize higher medication/reperfusion use; p.9 specifically higher reperfusion,thrombolytic,anticoagulation and discharge aspirin/β-blocker/statin/ACE-ARB, with no extra numbers. There is no main-paper numerical narrative for S045,S046,S048 beyond table values.

### Table 3 complete primary/secondary relationships: S057–S066

Every row: [p.7](../../../jama_huffman_2018_oi_170166.pdf#page=7), Table3 “Unadjusted and Adjusted Primary and Secondary Trial Outcomes Using Mixed-Effects Logistic Regression Models That Account for Within-Hospital Clustering and Clustering and Temporal Trends.” C10,066/I11,308 headers; raw n(%), cluster-adjusted difference/OR, primary analysis difference/OR additionally time-adjusted, outcome ICC. Differences%,95%CIs; OR null1. Footnote a wording S004. Clinical outcome denominator full header; restricted eligible medication/tobacco denominators not numerically printed in this table. Rows S064 eligible for all in-hospital medications,S065 discharged and eligible all discharge medications,S066 discharged baseline smokers. All components/definitions S003; no P/test/SE in rows.

| ID | Outcome | C n(%) | I n(%) | Cluster difference(95%CI) | Cluster OR(95%CI) | Primary difference(95%CI) | Primary OR(95%CI) | ICC |
|---|---|---|---|---|---|---|---|---|
| S057 | 30-day MACE | 645(6.4) | 602(5.3) | −0.51(−1.28 to0.26) | 0.92(0.81–1.04) | −0.09(−1.32 to1.14) | 0.98(0.80–1.21) | 0.15 |
| S058 | 30-day mortality | 509(5.1) | 445(3.9) | −0.65(−1.34 to0.03) | 0.87(0.75–1.00) | −0.28(−1.35 to0.80) | 0.94(0.74–1.19) | 0.18 |
| S059 | 30-day cardiovascular mortality | 494(4.9) | 434(3.8) | −0.58(−1.24 to0.09) | 0.88(0.76–1.02) | −0.26(−1.31 to0.80) | 0.94(0.74–1.20) | 0.19 |
| S060 | In-hospital mortality | 331(3.3) | 321(2.8) | −0.05(−0.58 to0.47) | 0.98(0.82–1.17) | −0.23(−1.07 to0.60) | 0.93(0.70–1.22) | 0.18 |
| S061 | 30-day reinfarction | 121(1.2) | 135(1.2) | 0.12(−0.31 to0.55) | 1.08(0.82–1.42) | 0.50(−0.24 to1.24) | 1.39(0.87–2.22) | 0.33 |
| S062 | 30-day stroke | 60(0.6) | 90(0.8) | 0.20(−0.05 to0.45) | 1.34(0.94–1.93) | 0.14(−0.23 to0.52) | 1.24(0.71–2.15) | 0.14 |
| S063 | 30-day major GUSTO bleeding | 19(0.2) | 30(0.3) | 0.13(−0.05 to0.30) | 1.56(0.84–2.88) | 0.23(−0.05 to0.52) | 2.34(0.93–5.89) | 0.20 |
| S064 | Optimal in-hospital medication | 3122(31.7) | 3878(35.8) | 8.61(6.98 to10.23) | 1.70(1.57–1.85) | 6.00(3.90 to8.11) | 1.45(1.28–1.64) | 0.40 |
| S065 | Optimal discharge medication | 5454(61.8) | 6483(64.0) | 9.97(8.32 to11.61) | 1.73(1.59–1.87) | 8.66(6.30 to11.03) | 1.61(1.42–1.82) | 0.28 |
| S066 | Tobacco cessation advice | 3526(96.0) | 2618(94.7) | 0.30(−1.20 to1.80) | 1.06(0.80–1.39) | 0.30(−2.15 to2.76) | 1.06(0.67–1.67) | 0.37 |

S057 matching claims: [p.1](../../../jama_huffman_2018_oi_170166.pdf#page=1) abstract I5.3%/C6.4%,adjusted RD−0.09%(−1.32 to1.14),OR0.98(0.80–1.21),not statistically significant; no reduction conclusion. [p.2](../../../jama_huffman_2018_oi_170166.pdf#page=2) Key Points C6.4%/I5.3%,not significant after cluster/time adjustment. [p.7](../../../jama_huffman_2018_oi_170166.pdf#page=7) Primary Analysis repeats unadjusted5.3/6.4,clusterOR0.92(0.81–1.04),primaryRD−0.09(−1.32 to1.14)/OR0.98(0.80–1.21),not significant; Figure2A pointer. [p.9](../../../jama_huffman_2018_oi_170166.pdf#page=9) Discussion and [p.10](../../../jama_huffman_2018_oi_170166.pdf#page=10) Conclusions repeat no reduction30-day composite. S058 matching [p.8](../../../jama_huffman_2018_oi_170166.pdf#page=8) Secondary Analyses:I3.9%/C5.1%,clusterOR0.87(0.75–1.00),primaryRD−0.28(−1.35 to0.80)/OR0.94(0.74–1.19),not significant after temporal adjustment; Figure2B; no material change with GRACE covariates,eTable5; in-hospital outcomes similar overall. S066 p.1 no tobacco counseling effect;p.7 high and similar. Abstract states no unexpected adverse events, without an event denominator/count. Other clinical outcomes p.9 “not different between groups.”

### Figure 3 complete subgroup relationships: S067–S080

Each row: [p.9](../../../jama_huffman_2018_oi_170166.pdf#page=9), Figure3 “Effect of Quality Improvement Tool Kit Intervention on 30-Day Major Adverse Cardiovascular Events by Prespecified Subgroups After Adjustment for Within-Hospital Clustering and Temporal Trends.” I displayed first; C reference. Full30-day MACE definition S003. Raw events/total(%), adjusted percentage-point difference and adjusted OR with95%CIs. Model S004 and subgroup interaction specification S007; no interaction P printed. Forest plot log-like OR axis ticks0.3,1.0,3.0; vertical null1; left favors I/right favors C. Marker size reflects precision; arrows for intervals beyond plotted right boundary. Differences and estimates retained exactly.

| ID | Subgroup | I events/total(%) | C events/total(%) | Adjusted difference(95%CI) | Adjusted OR(95%CI) |
|---|---|---|---|---|---|
| S067 | Age<50y | 58/2079(2.8) | 68/2045(3.3) | 1.42(−0.71 to3.54) | 1.53(0.83–2.79) |
| S068 | Age50–69y | 297/6606(4.5) | 326/5863(5.6) | −0.57(−2.02 to0.88) | 0.89(0.67–1.19) |
| S069 | Age≥70y | 247/2623(9.4) | 251/2158(11.6) | −0.23(−3.32 to2.85) | 0.98(0.71–1.35) |
| S070 | Male | 375/8529(4.4) | 409/7654(5.3) | 0.05(−1.32 to1.41) | 1.01(0.78–1.31) |
| S071 | Female | 227/2779(8.2) | 236/2412(9.8) | −0.57(−3.13 to2.00) | 0.93(0.67–1.29) |
| S072 | STEMI | 400/6768(5.9) | 465/6921(6.7) | 0.57(−1.01 to2.14) | 1.09(0.85–1.40) |
| S073 | NSTEMI | 202/4540(4.4) | 180/3145(5.7) | −1.46(−3.49 to0.57) | 0.75(0.51–1.10) |
| S074 | Extra large>1000,hospitals n5 | 51/1707(3.0) | 76/1853(4.1) | 1.83(−0.80 to4.46) | 1.68(0.85–3.32) |
| S075 | Large501–1000,hospitals n15 | 168/4962(3.4) | 212/3561(6.0) | −1.56(−3.58 to0.46) | 0.71(0.47–1.08) |
| S076 | Medium201–500,hospitals n24 | 292/3568(8.2) | 310/3847(8.1) | −1.47(−3.76 to0.83) | 0.83(0.62–1.11) |
| S077 | Small<201,hospitals n19 | 91/1071(8.5) | 47/805(5.8) | 2.28(−2.24 to6.79) | 1.45(0.70–3.04) |
| S078 | Government,hospitals n9 | 158/3036(5.2) | 275/4097(6.7) | −0.55(−2.56 to1.47) | 0.90(0.61–1.33) |
| S079 | Nonprofit,hospitals n12 | 186/2964(6.3) | 193/2785(6.9) | −0.62(−3.43 to2.20) | 0.91(0.59–1.40) |
| S080 | Private,hospitals n42 | 258/5308(4.9) | 177/3184(5.6) | 0.89(−1.19 to2.97) | 1.16(0.82–1.64) |

### Figure 2 complete plotted relationships: S081–S090

Direct location for every row [p.8](../../../jama_huffman_2018_oi_170166.pdf#page=8), Figure2 “Unadjusted Temporal Trends in 30-Day Major Adverse Cardiovascular Event Rates and Mortality Rates.” PanelA30-day MACE; panelB30-day mortality. All six steps0–5,all five cohorts; y axes% ticks0,2,4,6,8,10,12,14; x steps0,1,2,3,4,5. Open circles C,solid I; green cohort1,blue2,purple3,red4,yellow5. C until cohort-specific crossover; I thereafter. Error bars95%CIs. **Graph-only readings below are approximate visual transcriptions, not printed exact numbers; about ±0.2 percentage-point positional precision.** Each cell is approximate estimate(lower,upper) in percent; every point and both interval endpoints are represented. No event numerator, P, SE, precise interval engine or numerical CI endpoint is printed. These records do not infer counts from pixels.

| ID | Panel/cohort | Step0 | Step1 | Step2 | Step3 | Step4 | Step5 |
|---|---|---|---|---|---|---|---|
| S081 | A/cohort1 | 3.4(2.0,4.9) C | 3.8(2.6,5.6) I | 2.4(1.4,4.2) I | 2.6(1.6,4.2) I | 3.1(2.0,5.0) I | 5.7(4.1,7.8) I |
| S082 | A/cohort2 | 5.8(3.8,8.6) C | 4.5(2.7,7.2) C | 7.9(6.1,10.1) I | 5.7(4.3,7.5) I | 4.4(3.0,6.3) I | 3.7(2.4,5.4) I |
| S083 | A/cohort3 | 9.8(7.9,12.0) C | 10.0(8.1,12.1) C | 8.8(7.0,11.0) C | 7.6(6.0,9.4) I | 6.7(5.3,8.5) I | 5.4(4.1,7.1) I |
| S084 | A/cohort4 | 3.4(2.0,5.5) C | 7.0(5.3,9.3) C | 5.6(4.1,7.6) C | 7.8(6.0,10.1) C | 6.0(4.6,7.9) I | 5.1(3.6,7.2) I |
| S085 | A/cohort5 | 6.3(4.7,8.4) C | 4.9(3.5,6.8) C | 4.8(3.4,6.7) C | 4.6(3.3,6.4) C | 4.6(3.3,6.3) C | 6.2(4.7,7.9) I |
| S086 | B/cohort1 | 3.0(1.8,5.1) C | 2.7(1.7,4.4) I | 2.0(1.1,3.7) I | 2.3(1.4,3.9) I | 2.6(1.6,4.3) I | 1.7(0.9,3.1) I |
| S087 | B/cohort2 | 3.3(1.8,5.6) C | 4.2(2.5,6.7) C | 5.9(4.4,8.0) I | 5.1(3.8,6.9) I | 3.2(2.1,4.8) I | 3.0(1.9,4.8) I |
| S088 | B/cohort3 | 7.6(5.9,9.6) C | 7.3(5.8,9.3) C | 7.4(5.8,9.4) C | 5.6(4.3,7.1) I | 5.5(4.2,7.1) I | 4.0(2.9,5.5) I |
| S089 | B/cohort4 | 2.3(1.2,4.2) C | 5.6(4.0,7.7) C | 4.2(3.0,6.0) C | 6.3(4.7,8.5) C | 4.0(2.9,5.6) I | 4.5(3.2,6.4) I |
| S090 | B/cohort5 | 5.3(3.8,7.2) C | 3.1(2.0,4.8) C | 4.2(2.9,6.0) C | 3.9(2.7,5.5) C | 4.1(2.9,5.7) C | 4.4(3.2,6.0) I |

Exact printed contributor counts, **identical in both panels**, step0–5: cohort1 439,662,542,654,605,648; cohort2 400,379,723,785,727,600; cohort3 858,910,827,993,1022,964; cohort4 477,629,730,679,860,627; cohort5 741,731,694,743,829,896. These are cohort×step analysis counts, distinct from Figure1 enrolled counts; crossover and included totals N002–N008. Narrative p.7 S057 points to panelA;p.8 S058 to panelB. [p.9](../../../jama_huffman_2018_oi_170166.pdf#page=9) Discussion states lower MACE/mortality intervention rates in first step compared with other steps and lists possible reasons smaller sample/estimate instability,contamination,baseline characteristics,chance; no new numeric result.

### S091 — Expanded post hoc composite

[p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3) post hoc specification; [p.8](../../../jama_huffman_2018_oi_170166.pdf#page=8) Secondary/Post Hoc Analyses continued [p.9](../../../jama_huffman_2018_oi_170166.pdf#page=9). Outcome30-day MACE plus incident in-hospital heart failure/cardiogenic shock/cardiac arrest; I7.0%/C9.1% unadjusted; clusterOR0.89(95%CI0.80–1.00); cluster+time adjustedRD−1.34%(−2.72 to0.04),OR0.84(0.70–1.00). eTable7 pointer; no main-paper event numerator or restricted denominator printed. [p.9](../../../jama_huffman_2018_oi_170166.pdf#page=9) Discussion says post hoc analysis led to lower expanded MACE rate and should be hypothesis-generating; other secondary clinical outcomes not different; possible medication/reperfusion improvements,recruitment/detection bias,chance. No P supplied; specification S004/S006.

### S092 — Follow-up availability troponin comparison

[p.6](../../../jama_huffman_2018_oi_170166.pdf#page=6), Results:unadjusted baseline characteristics included versus missing follow-up generally similar except initial troponin lower in included,1.3ng/mL versus4.6ng/mL; **P<.001**; eTable1 Supplement3 pointer. Main narrative does not state statistic type,dispersion,comparison-specific denominator,test name or sidedness; N010 supplies follow-up groups21,079 versus295. This contrast is follow-up status rather than randomized I/C; do not substitute Table1 randomized-arm medians S020.

## Mapping limitations

All12 physical pages are mapped:12 reusable-backed,0 fresh-required,0 scientific coverage gaps. Article has Tables1–3 and Figures1–3; no Table4 is present. 13 numeric relationships N001–N013 and92 statistical relationships S001–S092,105 total. Every displayed table and subgroup row is separately assigned; graphical trajectories are coherent cohort/outcome relationships containing all six points and both limits. Figure2 exact rates/CI endpoints are not printed; all60 estimates and120 endpoints are represented as approximate visual readings with explicit precision, and all contributor counts are exact. This graphical-precision limitation does not omit a source unit. Restricted Table3 medication/tobacco denominators and main-paper imputation numerical details are not supplied in this article; their printed definitions and supplement pointers are mapped without assuming unseen values. Sources and reusable assets were not modified; no old review conclusions, external sources, Python extraction, or OCR were used.
