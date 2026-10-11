# Main-paper quantitative evidence map

Fresh mandatory mapper runtime: `01a128dc-ff7f-7141-8b09-40baa2432582`; role `qc161_main_quantitative_mapper`, configured gpt-6.1-sol/medium. Exact scope: DOC-001, `jama_thille_2019_oi_190108.pdf`, all PDF pages 1–11, REPORT by published results content. This artifact reconstructs evidence only; it makes no candidate judgments.

## Evidence provenance and complete page coverage

Read the scope, review contract, settings, tooling record, source inventory, source coverage, evidence-asset inventory, and coverage manifest. Reused page-specific native/layout text for pp.1–9 from `.ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-NNN.txt`, and pp.10–11 from `.ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-001-main-article_page-NNN.txt`, where NNN is the exact zero-padded page. Text engine recorded by curator as direct PDF extraction, Poppler-compatible. Reusable images `.ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-007-07.png` and `.ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-008-08.png` were visually inspected for Figure 2, all Table 2 values, and both Figure 3 panels; existing image engine unrecorded. No new preprocessing derivative, Python extraction, OCR, external source, or historical candidate/report conclusions used. There are no fresh-required main-paper pages.

All links below resolve to the supplied source using the exact PDF page. Since this artifact is in `review_1_6_1/extraction/`, source links use `../../../`.

| PDF page | Complete mapped contents | Status |
|---|---|---|
| [1](../../../jama_thille_2019_oi_190108.pdf#page=1) | Abstract, all quantitative occurrences, trial identity and corrected publication identity | COMPLETE |
| [2](../../../jama_thille_2019_oi_190108.pdf#page=2) | Key Points; population; randomization; intervention start; background distinguished from current results | COMPLETE |
| [3](../../../jama_thille_2019_oi_190108.pdf#page=3) | Entire participant-flow figure, caption, interventions and physiologic targets | COMPLETE |
| [4](../../../jama_thille_2019_oi_190108.pdf#page=4) | Entire outcome definitions, statistical analysis, sample size, participant narrative | COMPLETE |
| [5](../../../jama_thille_2019_oi_190108.pdf#page=5) | Every Table 1 row, main headings and scales | COMPLETE |
| [6](../../../jama_thille_2019_oi_190108.pdf#page=6) | Every continued Table 1 row and footnote; descriptive treatment delivery; primary/secondary narrative | COMPLETE |
| [7](../../../jama_thille_2019_oi_190108.pdf#page=7) | Figure 2, every exploratory result, subgroup and adjusted analyses, discussion quantities | COMPLETE |
| [8](../../../jama_thille_2019_oi_190108.pdf#page=8) | Every Table 2 row; both Figure 3 panels, risk tables, axes, caption; discussion matching occurrences | COMPLETE |
| [9](../../../jama_thille_2019_oi_190108.pdf#page=9) | Discussion matching rescue/mortality claims; conclusion; dated correction disclosure; remaining administrative material has no applicable current-result relationship | COMPLETE |
| [10](../../../jama_thille_2019_oi_190108.pdf#page=10) | Disclosures, funding, contributors, data-sharing pointer and references inspected; no applicable quantitative relationship beyond administrative/background numbers | COMPLETE_NO_APPLICABLE |
| [11](../../../jama_thille_2019_oi_190108.pdf#page=11) | References inspected; no applicable current-study quantitative relationship | COMPLETE_NO_APPLICABLE |

## Reading conventions

C = high-flow nasal oxygen alone (control), I = high-flow nasal oxygen alternating with noninvasive ventilation (intervention). Unless a row specifies otherwise, analyzed populations are C=302 and I=339. Table 1 column order is C then I. Percentages in Table 1 are counts/column population unless exact alternate denominator is printed. Table 2 differences use I minus C; its heading is "Absolute Difference, % (95% CI)" and its length-of-stay rows are individually labeled median (IQR), days. Do not assume a method for continuous-outcome differences beyond the supplied description. No person-time rate, reported test statistic, or standard error value is displayed. SD and IQR are explicitly distinguished. Text and table occurrences are retained separately wherever their precision or values differ.

## Numeric and reporting relationships

### Flow, analysis population, time and implementation

| Key | Source location | Quantity, label, population/time and matching occurrences |
|---|---|---|
| M-N001 | pp.1,3,4 | Randomized total 648; C=306, I=342. Abstract results mean(SD) age 70(10) y and women 219(34%) attributed to randomized patients; narrative p.4 repeats these. Trial abstract design states 641 patients; results 641 completed; Key Points p.2 included 641; p.4 analysis total 641. |
| M-N002 | p.3 Figure 1 | 3121 extubated at 30 ICUs April 2017–January 2018; 1460 excluded = 927 low risk +414 intubated <24 h +101 under law protection/nonaffiliated health system +18 minor; 1661 high-risk extubated after at least 24 h mechanical ventilation. |
| M-N003 | p.3 Figure 1 | 692 excluded from 1661 =274 do-not-reintubate +182 long-term NIV/CPAP at home +119 unplanned extubation +41 NIV contraindication +39 chronic neuromuscular disease +37 traumatic brain injury; 969 eligible. p.4 narrative repeats 3121,30,969. |
| M-N004 | p.3 Figure 1 | 321 not included =270 no staff/logistic issues +51 declined; 648 randomized. |
| M-N005 | pp.3,4 | C:306 assigned,302 received,4 did not receive (2 law protection,2 missing). I:342 assigned,339 received,3 did not receive (1 law protection,1 died before extubation,1 missing). p.4 seven secondarily excluded:3 protected,1 died,3 missing primary outcome. |
| M-N006 | pp.3,4 | C302 and I339 included in intention-to-treat analysis and 90-d follow-up. p.4 analyzed all randomized extubated patients with completed primary outcome, by randomization regardless of applied treatment. |
| M-N007 | pp.1,2,3 | Recruitment April 2017–January 2018; follow-up until April 2018; 30 ICUs France. Adults intubated >24 h ready after successful breathing trial; high risk >65 y or chronic cardiac/lung disease. Left ventricular dysfunction defined ejection fraction ≤45%. Figure 1 threshold wording at least24 h. Data locked January 2019. |
| M-N008 | pp.2,3 | C prescribed high flow ≥48 h,50 L/min,SpO2≥92%,temperature37°C. I NIV immediate,first session≥4 h,≥12 h/day during first48 h,night encouraged; pressure support≥5 cm H2O,target tidal volume6–8 mL/kg predicted body weight,PEEP5–10 cm H2O,SpO2≥92%; high flow between sessions. Blood gases1 h after start,under C high flow vs I NIV. Stop at48 h if no respiratory failure or continue until recovery. |
| M-N009 | pp.4,6 | Ventilation pre-extubation pooled median5 d,IQR3–10; difficult/prolonged206/641(32%); hypercapnia111(17%) PaCO2>45 mm Hg. Table1 counts provide weaning components and Figure3 strata. |
| M-N010 | p.6 | Initial C high-flow gas50(5) L/min,FIO2 .41(.13); initial I pressure support7.8(2.5) cm H2O,PEEP5.3(1.1),FIO2 .34(.10),tidal8.6(2.9) mL/kg predicted body weight; all mean(SD). |
| M-N011 | p.6 | I delivered NIV22(9) h first48 h,mean13 h first24 h;≤4 h because intolerance20 patients(6%). C high flow42(11) h first48 h. |
| M-N012 | pp.6–7 | Continued assigned treatment beyond48 h: I86(25%),C106(35%); I-C −9.7%,95%CI−16.8 to−2.6,P<.01. |
| M-N013 | p.7 | Reintubation criteria among100 reintubated in ICU:96% pooled; I39/41(95%),C57/59(97%); difference−1.5%,CI−13.0 to7.4,P=.99. |
| M-N014 | p.7 | Reintubation reasons:88 severe respiratory failure,37 neurological,16 hemodynamic,10 respiratory/cardiac arrest; references eTable1. Criteria can coexist (definitions p.4). |
| M-N015 | pp.7,9 | Of C88 postextubation respiratory failure,28(32%) rescue NIV,mean(SD)20(18)h;12/28(43%) required reintubation. p.9 approximately one-third received rescue NIV in case of respiratory failure. |
| M-N016 | pp.7,9 | No severe adverse events attributable to randomization group. p.9 mortality of reintubated patients exceeding30%; Table2 C21/59 and I11/41,pooled32/100. |

### Table 1: all baseline rows (C versus I)

Every following row is from [Table 1 p.5](../../../jama_thille_2019_oi_190108.pdf#page=5), unless p.6 explicitly specified. Counts are No.(%) and continuous quantities mean(SD), except medians explicitly labeled.

| Key | Row/scale | C | I |
|---|---|---|---|
| M-N017 | Age,y | 70(10) | 69(10) |
| M-N018 | Men | 195(65) | 230(68) |
| M-N019 | Women | 107(35) | 109(32) |
| M-N020 | Body mass index | 28(6) | 28(7) |
| M-N021 | SAPS II at admission | 55(17) | 55(20) |
| M-N022 | Intubation:acute respiratory failure | 158(52) | 167(49) |
| M-N023 | Intubation:coma | 55(18) | 57(17) |
| M-N024 | Intubation:shock | 30(10) | 37(11) |
| M-N025 | Intubation:cardiac arrest | 26(9) | 35(10) |
| M-N026 | Intubation:surgery | 28(9) | 35(10) |
| M-N027 | Intubation:other | 5(2) | 8(2) |
| M-N028 | Age>65 y risk factor | 223(74) | 237(70) |
| M-N029 | Underlying chronic cardiac disease | 145(48) | 161(47) |
| M-N030 | Ischemic heart disease | 78(26) | 88(26) |
| M-N031 | Atrial fibrillation | 58(19) | 45(13) |
| M-N032 | Left ventricular dysfunction | 39(13) | 52(15) |
| M-N033 | History cardiogenic pulmonary edema | 21(7) | 25(7) |
| M-N034 | Underlying chronic lung disease | 87(29) | 126(37) |
| M-N035 | COPD | 64(21) | 86(25) |
| M-N036 | Obesity-hypoventilation syndrome | 16(5) | 20(6) |
| M-N037 | Chronic restrictive pulmonary disease | 12(4) | 24(7) |
| M-N038 | SOFA day extubation | 4.2(2.5) | 4.4(2.7) |
| M-N039 | Mechanical ventilation duration,median(IQR),d | 5(3–9) | 6(3–11) |
| M-N040 | Weaning:simple | 203(67) | 232(68) |
| M-N041 | Weaning:difficult | 92(31) | 93(27) |
| M-N042 | Weaning:prolonged | 7(2) | 14(4) |
| M-N043 | Assist-control ventilation before SBT | 42(14) | 49(14) |
| M-N044 | Pressure-support ventilation before SBT | 260(86) | 290(86) |
| M-N045 | Pressure support,cm H2O | 9.6(2.8) | 9.3(2.9) |
| M-N046 | PEEP,cm H2O | 5.7(1.6) | 5.9(1.6) |
| M-N047 | Tidal volume,mL | 468(125) | 479(144) |
| M-N048 | Tidal volume,mL/kg | 7.7(2.4) | 7.9(2.5) |
| M-N049 | Respiratory rate,breaths/min | 22(7) | 22(6) |
| M-N050 | FIO2,% | 35(10) | 35(11) |
| M-N051 | FIO2,median(IQR),% | 30(30–40) | 30(30–40) |
| M-N052 | PaO2:FIO2,mm Hg | 274(93) | 275(89) |
| M-N053 | pH,units | 7.45(.06) | 7.45(.05) |
| M-N054 | PaCO2,mm Hg | 40(8) | 40(8) |
| M-N055 | p.6 SBT:T-piece | 188(62) | 206(61) |
| M-N056 | p.6 SBT:low pressure support | 114(38) | 133(39) |
| M-N057 | p.6 SBT duration,median(IQR),min | 60(30–60) | 60(30–60) |
| M-N058 | p.6 Systolic arterial pressure,mm Hg | 136(21) | 136(22) |
| M-N059 | p.6 Diastolic arterial pressure,mm Hg | 67(14) | 68(16) |
| M-N060 | p.6 Heart rate,bpm | 92(17) | 92(18) |
| M-N061 | p.6 Respiratory rate,breaths/min | 23(6) | 23(6) |
| M-N062 | p.6 SpO2,% | 96(3) | 96(3) |
| M-N063 | p.6 PaO2,mm Hg,mean(SD)[No.] | 87(28)[221] | 86(27)[241] |
| M-N064 | p.6 pH,mean(SD)[No.] | 7.45(.06)[221] | 7.45(.05)[241] |
| M-N065 | p.6 PaCO2,mm Hg,mean(SD)[No.] | 39(8)[221] | 40(9)[241] |
| M-N066 | p.6 Steroids pre-extubation | 42(14) | 53(16) |
| M-N067 | p.6 Ineffective cough,No./No.(%) | 65/284(23) | 86/322(27) |
| M-N068 | p.6 Abundant secretions,No./No.(%) | 121/288(42) | 114/326(35) |
| M-N069 | p.6 Participating centers | 30(100) | 30(100) |
| M-N070 | p.6 Patients/center,median(IQR) | 10(9–25) | 13(9–23) |
| M-N071 | p.6 Table1 footnotes/scales | BMI=kg/m²; SAPS II17 variables,range0–163,higher worse,score55 predicted mean43% survival; SOFA6 variables,range0–24,higher worse,score4–5 predicted survival>90%; disease categories can overlap; simple=first SBT success,difficult=failed first but extubated within7 days,prolonged=>7 days | Same definitions |

### Table 2: all outcome counts/distributions

All rows below are from [p.8 Table 2](../../../jama_thille_2019_oi_190108.pdf#page=8). Inference is separately cross-referenced to M-S IDs; no duplication of statistical evidence is implied.

| Key | Outcome/time/hierarchy | C | I | Statistical key |
|---|---|---|---|---|
| M-N072 | Primary:reintubation day7 | 55(18) | 40(12) | M-S007 |
| M-N073 | Secondary:postextubation respiratory failure day7 | 88(29) | 70(21) | M-S008 |
| M-N074 | Secondary:reintubation48 h | 36(12) | 24(7) | M-S009 |
| M-N075 | Secondary:reintubation72 h | 47(16) | 30(9) | M-S010 |
| M-N076 | Secondary:reintubation until ICU discharge | 59(20) | 41(12) | M-S011 |
| M-N077 | Secondary:ICU stay,median(IQR),d | 11(7–19) | 12(7–19) | M-S012 |
| M-N078 | Secondary:hospital stay,median(IQR),d | 23(15–39) | 25(15–42) | M-S013 |
| M-N079 | Secondary:ICU mortality | 26(9) | 21(6) | M-S014 |
| M-N080 | Secondary:hospital mortality | 46(15) | 54(16) | M-S015 |
| M-N081 | Secondary:day28 mortality | 33(11) | 39(12) | M-S016 |
| M-N082 | Secondary:day90 mortality | 65(21) | 62(18) | M-S017 |
| M-N083 | Exploratory:meeting reintubation criteria during ICU | 65(22) | 49(14) | M-S018 |
| M-N084 | Exploratory:mortality or reintubation ICU | 64(21) | 51(15) | M-S019 |
| M-N085 | Exploratory:mortality of reintubated patients | 21/59(36) | 11/41(27) | M-S020 |

### Figures, narrative matches and remaining quantity definitions

| Key | Location | Complete reconstruction |
|---|---|---|
| M-N086 | p.7 Figure2 | Overall Kaplan-Meier time from extubation to reintubation: x-axis days0,1,2,3,4,5,6,7;y-axis patients requiring reintubation,%0,5,10,15,20,25. C curve above I at day7; printed log-rank P=.02. Risk C302,276,265,253,248,246,244,243; I339,321,314,308,305,294,292,291, aligned day0–7. Caption median observation7 d,IQR7–7,both groups. |
| M-N087 | p.8 Figure3A | Hypercapnic PaCO2>45 mm Hg;x days0–7;y%0,5,10,15,20,25. Risk C48,44,44,39,38,37,37,37; I63,63,61,59,58,58,58,58. C curve above I;log-rank P=.049. Caption median observation7 d,IQR7–7,both groups. |
| M-N088 | p.8 Figure3B | Nonhypercapnic PaCO2≤45 mm Hg;same axes. Risk C254,232,221,214,210,209,207,206; I276,258,253,249,247,236,234,233. C curve above I;log-rank P=.11. Caption median observation7 d,IQR7–7,both groups. |
| M-N089 | pp.1,2,6,8 | Primary exact abstract I40/33911.8%(CI8.4–15.2),C55/30218.2%(CI13.9–22.6);Key Points11.8 versus18.2; narrative p.6 same precision, Table2 whole%12 versus18, discussion p.8 repeats18.2 and11.8. |
| M-N090 | pp.1,6,8 | Secondary respiratory failure abstract/narrative I21%,C29%,difference−8.7%,CI−15.2 to−1.8,P=.01;Table2 I70(21),C88(29),difference−8.5%,same CI/P. Both occurrences transcribed without normalization. |
| M-N091 | pp.1,7,8 | ICU-discharge reintubation abstract I12%,C20%,difference−7.4%,CI−13.2 to−1.8,P=.009; narrative p.6 says rates48 h,72 h,ICU discharge lower;Table2 corresponding counts/statistics. |
| M-N092 | pp.1,7,8 | ICU mortality abstract I6%,C9%,difference−2.4%,CI−6.7 to1.7,P=.25; p.7 narrative mortality ICU,hospital,day90 no significant difference;Table2 counts and estimates. Abstract 11 prespecified secondary outcomes,6 no significant difference. |
| M-N093 | p.7 | One-hour PaO2:FIO2 I291(97),C254(113) mm Hg; hypercapnia I21%,C19%; M-S022,023. Median time to reintubation I33 h(IQR7–81),C39 h(IQR12–67);M-S024. |
| M-N094 | p.7 | Hypercapnic111 patients:reintubation I8%,C21%,difference−12.9%,CI−27.1 to−.1,P=.049;nonhypercapnic530 patients:I13%,C18%,difference−5.0%,CI−11.2 to1.1,P=.10;Figure3 defines stratum group populations. |
| M-N095 | pp.4,7 | Primary definition within7 days of planned extubation. Immediate reintubation if≥1 severe respiratory,hemodynamic vasopressor,neurological GCS<12,or arrest criterion. Severe respiratory failure requires≥2:rate>35/min,distress/accessory muscles,pH<7.25 AND PaCO2>45,FIO2≥80% to SpO2≥92%,or PaO2:FIO2≤100 mm Hg. Secondary respiratory failure requires≥2:rate>25/min,distress,pH<7.35 AND PaCO2>45,FIO2≥50% to SpO2≥92%,or PaO2:FIO2≤150 mm Hg. |
| M-N096 | pp.7–9 | Discussion prior/background population hypercapnia20–30%; preliminary reintubation15%; estimated control>15%; overall15% with absolute≥5% reduction equivalent one-third relative reduction; current reported18.2/11.8. Intro background10–15%,high-risk>20%,10% receive NIV; these are cited context rather than current outcomes. Comparison prior treatment24 h versus current≥48 h. p.9 conclusion repeats reduced reintubation claim. |
| M-N097 | p.9 | Supplied article discloses correction February25,2020 concerning intervention description, exploratory outcomes, and x-axis labels Figures2/3. This is source-version context; no earlier version compared or read. |

## Statistical relationships and complete method map

Each M-S row is a distinct relationship to be assigned a global statistical inventory ID by the coordinator/checker. Confidence intervals are95%; result differences are I minus C unless stated. Source establishes two-tailed significance P<.05, primary χ², categorical reintubation/respiratory-failure/mortality χ², and Kaplan-Meier log-rank; it does not give a specific continuous-outcome comparison or interval algorithm. No distributional assumptions beyond printed methods are supplied here.

| Key | Exact source location | Estimate/test/method relationship and complete evidence |
|---|---|---|
| M-S001 | p.2 Randomization | Computer-generated centralized web system,permuted blocks4,1:1 assignment,stratification center and PaCO2≤45/>45 mm Hg measured end SBT or before SBT if unavailable. |
| M-S002 | p.4 Statistical Analysis | Sample size590,power80%,two-sidedα=.05,control reintubation18%,intervention10%,absolute8%; inflated to650 for potential secondary exclusions,described increased10%. |
| M-S003 | p.4 Statistical Analysis | Predefined SAP; analysis all randomized extubated primary-outcome-complete patients,assigned group regardless of applied treatment. Primary proportions comparedχ². |
| M-S004 | p.4 Statistical Analysis | Kaplan-Meier time-to-reintubation log-rank day7; predefined-time reintubation,respiratory failure day7,ICU/hospital mortalityχ²; time-to-death Kaplan-Meier/log-rank day90. |
| M-S005 | pp.4,6 Table1 footnote a | Logistic primary adjustment PaCO2 stratum and potential baseline imbalance,P<.05 defines imbalance; only underlying chronic lung disease ultimately included among unbalanced variables. Table1 chronic lung disease P=.02; baseline text all other characteristics similar. Results OR95%CI. |
| M-S006 | p.4 Statistical Analysis | Post hoc random-effects multilevel logistic hospital random effect,treatment fixed effect. PaCO2 subgroup primary/secondary after interaction test. Secondary endpoints exploratory because multiple comparisons/type I error;two-tailedP<.05;SAS9.4. |
| M-S007 | pp.1,6,8 | Primary day7 reintubation:I40/33911.8%(8.4–15.2),C55/30218.2%(13.9–22.6);RD−6.4%(−12.0 to−.9),P=.02. Table2 rounds proportions12/18; primaryχ². |
| M-S008 | pp.1,6,8 | Secondary respiratory failure day7:I70/33921%,C88/30229%;Table2 RD−8.5%(−15.2 to−1.8),P=.01;abstract/narrative RD−8.7% with same CI/P.χ² specified. |
| M-S009 | p.8 | Reintubation48 h:I24/3397%,C36/30212%;RD−4.8%(−9.6 to−.3),P=.04. |
| M-S010 | p.8 | Reintubation72 h:I30/3399%,C47/30216%;RD−6.7%(−11.9 to−1.7),P=.009. |
| M-S011 | pp.1,6,8 | Reintubation through ICU:I41/33912%,C59/30220%;RD−7.4%(−13.2 to−1.8),P=.009. |
| M-S012 | p.8 | ICU stay median(IQR)C11(7–19),I12(7–19)d;printed difference.5(−1.6 to2.6),P=.55,under shared "Absolute Difference,%" heading;no row-specific comparison method stated. |
| M-S013 | p.8 | Hospital stay median(IQR)C23(15–39),I25(15–42)d;printed difference2.3(−1.4 to6.1),P=.31,same shared heading and unspecified continuous comparison method. |
| M-S014 | pp.1,7,8 | ICU mortality:I21/3396%,C26/3029%;RD−2.4%(−6.7 to1.7),P=.25;not significantly different. |
| M-S015 | pp.7,8 | Hospital mortality:I54/33916%,C46/30215%;RD.7%(−5.0 to6.3),P=.80;not significantly different. |
| M-S016 | p.8 | Day28 mortality:I39/33912%,C33/30211%;RD.6%(−4.4 to5.5),P=.82. |
| M-S017 | pp.7,8 | Day90 mortality:I62/33918%,C65/30221%;RD−3.2%(−9.5 to2.9),P=.30;not significantly different. Survival curve separately in supplied supplement. |
| M-S018 | p.8 | Meeting reintubation criteria during ICU:I49/33914%,C65/30222%;RD−7.1%(−13.1 to−1.1),P=.02. |
| M-S019 | p.8 | Mortality/reintubation ICU:I51/33915%,C64/30221%;RD−6.2%(−12.2 to−.2),P=.04. |
| M-S020 | p.8 | Mortality of ICU-reintubated:I11/4127%,C21/5936%;RD−8.8%(−25.7 to9.9),P=.35. |
| M-S021 | pp.6–7 | Treatment beyond48 h:I86/33925%,C106/30235%;RD−9.7%(−16.8 to−2.6),P<.01;11th prespecified secondary definition p.4,not a Table2 row. |
| M-S022 | p.7 | One-hour PaO2:FIO2 mean(SD)I291(97),C254(113) mm Hg;difference37.0(19.7 to54.3),P<.001. Exploratory,no displayed exact contributor counts in main narrative. |
| M-S023 | p.7 | One-hour hypercapniaI21%,C19%;RD1.2%(−5.4 to7.7),P=.72;exploratory,no displayed exact contributor counts in main narrative. |
| M-S024 | p.7 | Reintubation time median(IQR)I33(7–81),C39(12–67)h;difference−5.0(−42.0 to32.0),P=.76;not significantly different;no row-specific inference method named. |
| M-S025 | p.7 | Among ICU-reintubated,meeting criteria:I39/4195%,C57/5997%;RD−1.5%(−13.0 to7.4),P=.99;pooled100,96%. |
| M-S026 | p.7 Figure2 | Overall Kaplan-Meier reintubation curves day7:log-rankP=.02,median observation7(IQR7–7)d;M-N086 contains all plotted numeric labels/risk counts. |
| M-S027 | p.7 | PaCO2 stratum by treatment primary-outcome interactionP=.25;no significant interaction. |
| M-S028 | pp.7,8 Figure3A | Hypercapnic111,C48,I63;primary reintubationI8%,C21%;RD−12.9%(−27.1 to−.1),P=.049;Figure3A log-rankP=.049. Keep proportion test and log-rank labels separately. |
| M-S029 | pp.7,8 Figure3B | Nonhypercapnic530,C254,I276;primary reintubationI13%,C18%;RD−5.0%(−11.2 to1.1),narrativeP=.10;Figure3B log-rankP=.11. Keep proportion test and log-rank labels separately. |
| M-S030 | p.7 | Primary logistic adjusted PaCO2≤45/>45 and underlying chronic lung disease:OR.60(.38–.93),P=.02,I versus C;lower odds narrative. |
| M-S031 | p.7 | Post hoc hospital random-effect adjustment:primaryP=.02 without andP=.02 with hospital random effect;reference eTable5,exact effect estimates not printed in main. |
| M-S032 | pp.1,2,7,9 | Overall conclusion decreased primary reintubation with intervention matches primary estimates;abstract11 secondary6 no significant difference; narrative secondary reintubation/respiratory failure significant and mortality nonsignificant; secondary inference explicitly exploratory. |

## Handoff accounting and limitations

Mapped11/11 PDF pages; reusable-backed11,fresh-required0; no scientific gaps. Local keys M-N001–M-N097 (97 numeric/reporting relationships) and M-S001–M-S032 (32 inferential/method relationships), total129; numeric/statistical cross-references intentionally track separate aspects of matching evidence. Every displayed Table1/2 row and Figure1/2/3 count,label,axis,caption and risk-table value is mapped. Appended reference/admin pages10–11 were inspected and explicitly recorded as no applicable current-study relationships. Do not interpret background reference numbers as trial outcomes.

Named reporting limits for downstream checking: main narrative does not specify continuous-outcome difference/test/CI method or exact one-hour contributor counts; unreported inputs should remain unreported rather than inferred. Graph curves were mapped by printed axes,groups,direction and risk counts; no unprinted event-time coordinates were estimated. Existing reusable image renderer metadata is absent,although native/layout values and current source identity were curated; candidate recheck must use the exact supplied direct-source page. No source or reusable asset was changed.
