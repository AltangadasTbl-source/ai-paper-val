# Main-paper quantitative evidence reconstruction

Agent: /root/main_mapping. Mandatory fresh main quantitative mapper. Exact scope: DOC-001, jama_thille_2019_oi_190108.pdf, physical PDF pages 1-11 (printed pages 1465-1475). Document role: REPORT throughout. Newly reasoned mapping, using source-matched reusable derivatives; no old candidate or report conclusions read. No scientific judgments or candidate diagnoses are made here.

## Provenance and reading conventions

Canonical native text: pages 1-9, `.ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/native_text/page-NNN.txt`; pages 10-11, `.ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-001-main-article_page-NNN.txt`. Each numbered file was read. Curator has independently recorded exact-source Poppler transcription matches. Reusable rendered images visually inspected: `.ai_paper_validation/document_outputs/DOC-001-main-article/preprocessing/rendered_pages/page-003-03.png`, `page-005-05.png`, `page-006-06.png`, `page-007-07.png`, `page-008-08.png`. These show Figure 1, all Table 1, Table 2, Figure 2 and both Figure 3 panels, including risk counts and footnotes. No fresh derivatives, OCR, or fallback environment were needed. Direct tools available per tooling_record.md; legacy images are locators, with exact source remaining final authority.

Every location below means the named row/paragraph on the linked physical page. Values are printed transcriptions, not replacements. A = high-flow nasal oxygen alone, analyzed n=302; B = high-flow nasal oxygen alternating with noninvasive ventilation (NIV), analyzed n=339. Randomized denominators are separately 306 and 342. In baseline rows paired values are A then B. `count (%)` means numerator and printed percentage with group denominator unless a different denominator is explicit. Mean (SD), median (IQR), and measurement units are retained separately. Outcome differences compare B minus A; the Table 2 column prints “Absolute Difference, % (95% CI)” even alongside length-of-stay rows. No CI method or continuous-outcome test is imputed.

## Complete page coverage

| Source unit | Content inspected and mapped | Status |
|---|---|---|
| DOC-001 p1 | Abstract population, dates, intervention allocation, primary and secondary effect tuples, secondary-outcome count | COMPLETE |
| DOC-001 p2 | Background quantitative claims; Key Points; enrollment definitions; allocation and stratification; intervention timing | COMPLETE |
| DOC-001 p3 | Figure 1 every node and exclusion count; Figure 1 footnote; intervention targets and timing | COMPLETE |
| DOC-001 p4 | Outcome definitions, sample-size parameters, full analysis rules, participant narrative | COMPLETE |
| DOC-001 p5 | Every Table 1 first-page row, grouping, denominator and scale | COMPLETE |
| DOC-001 p6 | Every Table 1 continuation row and footnote; treatment exposure; primary and secondary narratives | COMPLETE |
| DOC-001 p7 | Exploratory and subgroup results; adjusted analyses; Figure 2 axes, risk table, log-rank P and caption; discussion numeric claims | COMPLETE |
| DOC-001 p8 | Every Table 2 row; both Figure 3 axes, risk tables, log-rank P and caption; repeated discussion rates and durations | COMPLETE |
| DOC-001 p9 | Rescue-use and reintubated mortality interpretations; eligibility restatement; conclusion; correction notice | COMPLETE |
| DOC-001 p10 | Article disclosures, funding and study-group listing; no new applicable quantitative results (reference bibliographic digits not result units) | COMPLETE_NO_APPLICABLE_NEW_RESULTS |
| DOC-001 p11 | References only; no applicable new quantitative results; external cited studies not inspected | COMPLETE_NO_APPLICABLE_RESULTS |

## Numeric and reporting relationship inventory

| ID | Exact source location | Printed quantities, labels and aligned relationships |
|---|---|---|
| N001 | [p1 abstract Design/Results](../../../jama_thille_2019_oi_190108.pdf#page=1); p4 Study Participants | 30 French ICUs; enrollment April 2017-January 2018, follow-up through April 2018; 648 randomized, 641 completed/analyzed; randomized mean (SD) age 70 (10) y, women 219 (34%). Design names 641 patients while Results names randomized 648. |
| N002 | [p1 Interventions](../../../jama_thille_2019_oi_190108.pdf#page=1); p3 allocation nodes; p4 Results | A randomized 306, B randomized 342; A analyzed 302, B analyzed 339; total analysis 641. Random allocation ratio 1:1 is planned (p2), actual numbers recorded separately. |
| N003 | [p3 Figure 1 top two nodes](../../../jama_thille_2019_oi_190108.pdf#page=3); p4 Results | Extubated 3121 at 30 ICUs, April 2017-January 2018; 1460 excluded, remaining 1661 high-risk extubated after at least 24 h mechanical ventilation. |
| N004 | [p3 Figure 1 first exclusion box](../../../jama_thille_2019_oi_190108.pdf#page=3) | 1460 exclusions: low risk 927; intubated <24 h 414; law protection or nonaffiliation to health system 101; minor 18. |
| N005 | [p3 Figure 1 middle nodes](../../../jama_thille_2019_oi_190108.pdf#page=3) | High risk 1661; excluded 692; eligible 969. Exclusions: do-not-reintubate 274; home NIV or CPAP 182; unplanned extubation 119; NIV contraindication 41; chronic neuromuscular disease 39; traumatic brain injury 37. |
| N006 | [p3 Figure 1 eligible/randomized nodes](../../../jama_thille_2019_oi_190108.pdf#page=3); p4 Results | Eligible 969; not included 321 = no staff/logistics 270, declined 51; randomized 648. |
| N007 | [p3 Figure 1 A branch](../../../jama_thille_2019_oi_190108.pdf#page=3) | Randomized 306; received as randomized 302; did not receive 4: law protection 2, missing data 2; included intention-to-treat and 90-d follow-up 302. |
| N008 | [p3 Figure 1 B branch](../../../jama_thille_2019_oi_190108.pdf#page=3); p4 exclusions narrative | Randomized 342; received as randomized 339; did not receive 3: law protection 1, died before extubation 1, missing data 1; included intention-to-treat and 90-d follow-up 339. Across groups narrative excluded 7: law protection 3, death 1, missing primary outcome 3. |
| N009 | [p2 Methods/Randomization](../../../jama_thille_2019_oi_190108.pdf#page=2); p3 Figure 1 footnote | Adults intubated >24 h; high risk age >65 y OR chronic cardiac/lung disease. Cardiac left ventricular dysfunction LVEF ≤45%; PaCO2 strata ≤45 vs >45 mm Hg at end of spontaneous trial (or before trial if absent); blocks 4 participants; 1:1 allocation, center stratification. Figure says after at least 24 h. |
| N010 | [p2 Interventions](../../../jama_thille_2019_oi_190108.pdf#page=2); p3 intervention paragraphs | A high-flow at least 48 h; flow 50 L/min; SpO2 ≥92%; humidifier 37°C. B immediately after extubation, first NIV session ≥4 h, ≥12 h/day over 48 h; minimum pressure support 5 cm H2O; tidal target 6-8 mL/kg predicted body weight; PEEP 5-10 cm H2O; SpO2 ≥92%; blood gases 1 h after initiation; both groups minimum 48 h. |
| N011 | [p4 Outcomes severe failure definition](../../../jama_thille_2019_oi_190108.pdf#page=4) | Immediate reintubation if any one indication: severe respiratory failure, vasopressors, Glasgow Coma Scale <12, arrest. Severe respiratory failure requires ≥2 criteria: respiratory rate >35/min, distress, pH <7.25 AND PaCO2 >45 mm Hg, FIO2 ≥80% to maintain SpO2 ≥92%, or PaO2:FIO2 ≤100 mm Hg. |
| N012 | [p4 Outcomes respiratory failure definition](../../../jama_thille_2019_oi_190108.pdf#page=4) | Postextubation respiratory failure requires ≥2: respiratory rate >25/min, distress, pH <7.35 AND PaCO2 >45 mm Hg, FIO2 ≥50% to maintain SpO2 ≥92%, or PaO2:FIO2 ≤150 mm Hg. Distinct from severe failure. |
| N013 | [p4 Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=4); p1 Main Outcomes | Primary reintubation proportion within 7 days after planned extubation. Secondary reintubation 48 h, 72 h, ICU discharge; respiratory failure within 7 d; continuation beyond 48 h; ICU/hospital stays; mortality ICU, hospital, day28, day90. Eleven secondary endpoints. Exploratory gases at1h, time to reintubation, criteria, reasons, rescue NIV, ICU reintubation or death, reintubated mortality. |
| N014 | [p4 Statistical Analysis sample size](../../../jama_thille_2019_oi_190108.pdf#page=4) | Required 590, power80%, estimated A18% vs B10%, absolute8%, two-sided alpha .05; inflated10% to650 for secondary exclusions. |
| N015 | [p5 Table1 Age](../../../jama_thille_2019_oi_190108.pdf#page=5) | Mean(SD) age y A70(10), B69(10); analyzed denominators302/339, distinct randomized summary N001. |
| N016 | [p5 Table1 Sex](../../../jama_thille_2019_oi_190108.pdf#page=5) | Men A195(65), B230(68); women A107(35), B109(32). Both sex categories partition their respective analyzed populations. |
| N017 | [p5 Table1 BMI](../../../jama_thille_2019_oi_190108.pdf#page=5); p6 footnote b | Mean(SD) BMI A28(6), B28(7); definition kilograms divided by meters squared. |
| N018 | [p5 Table1 SAPS II](../../../jama_thille_2019_oi_190108.pdf#page=5); p6 footnote c | Admission mean(SD) SAPS II A55(17), B55(20). Calculated from17 variables, score0-163, higher worse disease/mortality risk. Printed interpretation: score55 predicted mean43% chance of survival. |
| N019 | [p5 Table1 Main reason acute respiratory failure](../../../jama_thille_2019_oi_190108.pdf#page=5) | A158(52), B167(49). Main-reason categories N019-N024 collectively form group totals. |
| N020 | [p5 Table1 Coma](../../../jama_thille_2019_oi_190108.pdf#page=5) | A55(18), B57(17). |
| N021 | [p5 Table1 Shock](../../../jama_thille_2019_oi_190108.pdf#page=5) | A30(10), B37(11). |
| N022 | [p5 Table1 Cardiac arrest](../../../jama_thille_2019_oi_190108.pdf#page=5) | A26(9), B35(10). |
| N023 | [p5 Table1 Surgery](../../../jama_thille_2019_oi_190108.pdf#page=5) | A28(9), B35(10). |
| N024 | [p5 Table1 Other reason](../../../jama_thille_2019_oi_190108.pdf#page=5) | A5(2), B8(2). |
| N025 | [p5 Table1 age risk](../../../jama_thille_2019_oi_190108.pdf#page=5) | Age >65 y A223(74), B237(70); risk factors overlap. |
| N026 | [p5 Table1 cardiac disease](../../../jama_thille_2019_oi_190108.pdf#page=5) | Any chronic cardiac A145(48), B161(47). Footnote d: patients could have >1 cardiac or lung disease; constituent diagnoses are not exclusive. |
| N027 | [p5 Table1 ischemic heart disease](../../../jama_thille_2019_oi_190108.pdf#page=5) | A78(26), B88(26). |
| N028 | [p5 Table1 atrial fibrillation](../../../jama_thille_2019_oi_190108.pdf#page=5) | A58(19), B45(13). |
| N029 | [p5 Table1 left ventricular dysfunction](../../../jama_thille_2019_oi_190108.pdf#page=5) | A39(13), B52(15); LVEF definition N009. |
| N030 | [p5 Table1 prior cardiogenic pulmonary edema](../../../jama_thille_2019_oi_190108.pdf#page=5) | A21(7), B25(7). |
| N031 | [p5 Table1 lung disease](../../../jama_thille_2019_oi_190108.pdf#page=5); p6 footnote a; p4 Results | Any chronic lung A87(29), B126(37). Only baseline significant difference per footnote a, P=.02 (S001); narrative says higher B. |
| N032 | [p5 Table1 COPD](../../../jama_thille_2019_oi_190108.pdf#page=5) | A64(21), B86(25). |
| N033 | [p5 Table1 obesity-hypoventilation](../../../jama_thille_2019_oi_190108.pdf#page=5) | A16(5), B20(6). |
| N034 | [p5 Table1 restrictive pulmonary disease](../../../jama_thille_2019_oi_190108.pdf#page=5) | A12(4), B24(7). |
| N035 | [p5 Table1 SOFA](../../../jama_thille_2019_oi_190108.pdf#page=5); p6 footnote e | Extubation-day mean(SD) A4.2(2.5), B4.4(2.7). Calculated6 variables, score0-24, higher worse organ failure/mortality risk; score4-5 predicted mean survival >90%. |
| N036 | [p5 Table1 ventilation duration](../../../jama_thille_2019_oi_190108.pdf#page=5); p4 last Results paragraph | Median(IQR) days A5(3-9), B6(3-11); pooled narrative median5(IQR3-10). |
| N037 | [p5 Table1 weaning difficulty](../../../jama_thille_2019_oi_190108.pdf#page=5); p6 footnote f and narrative | Simple A203(67), B232(68); difficult A92(31), B93(27); prolonged A7(2), B14(4). Pooled difficult/prolonged206/641 (32%). Simple success first trial; difficult failed first but extubated within7 following days; prolonged >7d after first trial. |
| N038 | [p5 Table1 ventilator mode](../../../jama_thille_2019_oi_190108.pdf#page=5) | Assist-control A42(14), B49(14); pressure-support A260(86), B290(86). Mode categories partition groups. |
| N039 | [p5 Table1 pretrial pressure support](../../../jama_thille_2019_oi_190108.pdf#page=5) | Mean(SD) cm H2O A9.6(2.8), B9.3(2.9). |
| N040 | [p5 Table1 pretrial PEEP](../../../jama_thille_2019_oi_190108.pdf#page=5) | Mean(SD) cm H2O A5.7(1.6), B5.9(1.6). |
| N041 | [p5 Table1 pretrial tidal volume](../../../jama_thille_2019_oi_190108.pdf#page=5) | Mean(SD) mL A468(125), B479(144); mL/kg A7.7(2.4), B7.9(2.5). |
| N042 | [p5 Table1 pretrial respiratory rate](../../../jama_thille_2019_oi_190108.pdf#page=5) | Mean(SD) breaths/min A22(7), B22(6). |
| N043 | [p5 Table1 pretrial FIO2](../../../jama_thille_2019_oi_190108.pdf#page=5) | Mean(SD) % A35(10), B35(11); median(IQR) A30(30-40), B30(30-40). Fraction-vs-percent distinguished from N060. |
| N044 | [p5 Table1 pretrial PaO2:FIO2](../../../jama_thille_2019_oi_190108.pdf#page=5) | Mean(SD) mm Hg A274(93), B275(89). |
| N045 | [p5 Table1 pretrial pH](../../../jama_thille_2019_oi_190108.pdf#page=5) | Mean(SD) units A7.45(.06), B7.45(.05). |
| N046 | [p5 Table1 pretrial PaCO2](../../../jama_thille_2019_oi_190108.pdf#page=5) | Mean(SD) mm Hg A40(8), B40(8). |
| N047 | [p6 Table1 trial type](../../../jama_thille_2019_oi_190108.pdf#page=6) | T-piece A188(62), B206(61); low pressure support A114(38), B133(39); categories partition groups. |
| N048 | [p6 Table1 trial duration](../../../jama_thille_2019_oi_190108.pdf#page=6) | Median(IQR) min A60(30-60), B60(30-60). |
| N049 | [p6 Table1 arterial pressure](../../../jama_thille_2019_oi_190108.pdf#page=6) | Mean(SD) mm Hg systolic A136(21), B136(22); diastolic A67(14), B68(16). |
| N050 | [p6 Table1 heart rate](../../../jama_thille_2019_oi_190108.pdf#page=6) | Mean(SD) bpm A92(17), B92(18). |
| N051 | [p6 Table1 respiratory rate](../../../jama_thille_2019_oi_190108.pdf#page=6) | End-trial mean(SD) breaths/min A23(6), B23(6), distinct pretrial N042. |
| N052 | [p6 Table1 SpO2](../../../jama_thille_2019_oi_190108.pdf#page=6) | End-trial mean(SD) % A96(3), B96(3). |
| N053 | [p6 Table1 PaO2](../../../jama_thille_2019_oi_190108.pdf#page=6) | End-trial mean(SD)[No.] mm Hg A87(28)[221], B86(27)[241]. Measurements use221/241, not full302/339. |
| N054 | [p6 Table1 pH](../../../jama_thille_2019_oi_190108.pdf#page=6) | End-trial mean(SD)[No.] units A7.45(.06)[221], B7.45(.05)[241]. |
| N055 | [p6 Table1 PaCO2](../../../jama_thille_2019_oi_190108.pdf#page=6) | End-trial mean(SD)[No.] mm Hg A39(8)[221], B40(9)[241]; stratification permits pretrial fallback N009. |
| N056 | [p6 Table1 steroids](../../../jama_thille_2019_oi_190108.pdf#page=6) | Administration before extubation A42(14), B53(16). |
| N057 | [p6 Table1 ineffective cough](../../../jama_thille_2019_oi_190108.pdf#page=6) | A65/284(23), B86/322(27); item-specific measured denominators explicit. |
| N058 | [p6 Table1 abundant secretions](../../../jama_thille_2019_oi_190108.pdf#page=6) | A121/288(42), B114/326(35); item-specific denominators explicit. |
| N059 | [p6 Table1 centers](../../../jama_thille_2019_oi_190108.pdf#page=6) | Participating centers n30; centers participating A30(100), B30(100); patients per center median(IQR) A10(9-25), B13(9-23); center and patient units distinct. |
| N060 | [p6 initial settings narrative](../../../jama_thille_2019_oi_190108.pdf#page=6) | A mean(SD) flow50(5)L/min and FIO2 fraction .41(.13); B pressure support7.8(2.5)cm H2O, PEEP5.3(1.1), FIO2 fraction .34(.10), tidal volume8.6(2.9)mL/kg predicted body weight. |
| N061 | [p6 exposure narrative](../../../jama_thille_2019_oi_190108.pdf#page=6) | B NIV22(9)h mean(SD) in first48h; mean13h in first24h; ≤4h due intolerance20(6%). A high-flow42(11)h in first48h. |
| N062 | [p6 pooled hypercapnia](../../../jama_thille_2019_oi_190108.pdf#page=6); p7 subgroup narrative; p8 Figure3 initial risk | Hypercapnic PaCO2 >45mm Hg111(17%) of641; nonhypercapnic530. Figure strata A48/B63 (111), A254/B276 (530). |
| N063 | [p7 continuation narrative](../../../jama_thille_2019_oi_190108.pdf#page=7); p6 start of paragraph | Beyond48h for incomplete recovery B86(25%), A106(35%); contrast S016. This secondary outcome appears in narrative rather than Table2. |
| N064 | [p7 reintubation criteria narrative](../../../jama_thille_2019_oi_190108.pdf#page=7) | ICU reintubated total100; 96% met criteria; B39/41(95%), A57/59(97%); contrast S020; Table2 criteria-in-all-patients denominator differs, S013. |
| N065 | [p7 reasons narrative](../../../jama_thille_2019_oi_190108.pdf#page=7) | Severe respiratory failure88; neurological37; hemodynamic16; respiratory/cardiac arrest10, among100 reintubated. Matched eTable1 is assigned to support mapper; exclusivity not asserted by main narrative. |
| N066 | [p7 rescue NIV narrative](../../../jama_thille_2019_oi_190108.pdf#page=7); p9 first paragraph | Among A88 with postextubation respiratory failure,28(32%) rescue NIV; mean(SD) rescue duration20(18)h;12(43%) of28 reintubated. p9 calls approximately one-third of patients treated with high-flow alone receiving rescue in case of respiratory failure. |
| N067 | [p7 adverse-event paragraph](../../../jama_thille_2019_oi_190108.pdf#page=7) | No severe adverse events attributable to randomization group (zero statement, no count denominator supplied). |
| N068 | [p7 Figure2 axes/caption](../../../jama_thille_2019_oi_190108.pdf#page=7) | Kaplan-Meier time from extubation to reintubation; x0-7d every1d, y patients requiring reintubation %0-25 every5%; A upper endpoint around18%, B lower around12%; median observation7d(IQR7-7) both; log-rank P=.02 S026. No pointwise CIs shown. |
| N069 | [p7 Figure2 A risk row](../../../jama_thille_2019_oi_190108.pdf#page=7) | Day0,1,2,3,4,5,6,7 at risk A302,276,265,253,248,246,244,243. |
| N070 | [p7 Figure2 B risk row](../../../jama_thille_2019_oi_190108.pdf#page=7) | Day0,1,2,3,4,5,6,7 at risk B339,321,314,308,305,294,292,291. Risk counts are not automatically event counts. |
| N071 | [p8 Figure3A axes/caption](../../../jama_thille_2019_oi_190108.pdf#page=8) | Hypercapnia >45mm Hg; same x0-7d and y0-25% scales as Fig2; median observation7(IQR7-7) both; endpoints A around21%, B around8%; log-rank P=.049 S027. |
| N072 | [p8 Figure3A A risk row](../../../jama_thille_2019_oi_190108.pdf#page=8) | Day0-7 A48,44,44,39,38,37,37,37. |
| N073 | [p8 Figure3A B risk row](../../../jama_thille_2019_oi_190108.pdf#page=8) | Day0-7 B63,63,61,59,58,58,58,58. |
| N074 | [p8 Figure3B axes/caption](../../../jama_thille_2019_oi_190108.pdf#page=8) | Nonhypercapnia ≤45mm Hg; same axes and observation7(IQR7-7); endpoints A around18%, B around13%; log-rank P=.11 S028 (narrative proportion comparison P=.10 S022). |
| N075 | [p8 Figure3B A risk row](../../../jama_thille_2019_oi_190108.pdf#page=8) | Day0-7 A254,232,221,214,210,209,207,206. |
| N076 | [p8 Figure3B B risk row](../../../jama_thille_2019_oi_190108.pdf#page=8) | Day0-7 B276,258,253,249,247,236,234,233. Figures permit overall/stratum risk alignments at each day. |
| N077 | [p1 abstract secondary count](../../../jama_thille_2019_oi_190108.pdf#page=1); p4 Outcomes; p7 continuation; p8 Table2 | Eleven prespecified secondary outcomes, six with no significant difference per abstract; full endpoint listing N013 and Table2 S003-S012 plus continuation S016 preserve distinct categories/times. |
| N078 | [p2 background](../../../jama_thille_2019_oi_190108.pdf#page=2); p7 Discussion; p8 Discussion | Background ready-for-separation failure10%-15%, high-risk >20%, only10% receive prophylactic NIV; two small RCTs lower reintubation. Discussion hypercapnic20%-30% high-risk, prior study day7 reintubation15%, expected control >15%; overall baseline around15%, absolute ≥5% corresponds relative one-third; p8 actual18.2%/11.8%, prior comparator intervention24h vs current≥48h. External cited studies not consulted. |
| N079 | [p9 Limitations](../../../jama_thille_2019_oi_190108.pdf#page=9); p8 Table2 mortality reintubated | Reintubated mortality “exceeding30%”; matching A21/59(36%), B11/41(27%), pooled32/100 from printed counts; p9 eligibility again >65y or chronic disease. |
| N080 | [p9 Correction notice](../../../jama_thille_2019_oi_190108.pdf#page=9); p1 footer | Accepted September9,2019; published October2,2019; corrected February25,2020. Supplied notice names clarified intervention in Abstract/Methods, exploratory outcome data corrections, and Figure2/3 x-axis corrections. Map current supplied version without reconstructing absent prior versions. No source result standard errors, person-time rates or test statistics are printed in the main article. |

## Inferential-statistical relationship inventory

All intervals here are 95% CIs. The p4 methods specify two-tailed P<.05; chi-square for primary proportions, other reintubation times, respiratory failure and mortality ICU/hospital; Kaplan-Meier/log-rank separately for time to reintubation at7d and death90d. Secondary findings exploratory due multiplicity. Missing continuous-outcome test or CI construction is not imputed.

| ID | Exact source location and matching occurrence | Complete printed inferential tuple and context |
|---|---|---|
| S001 | [p6 Table1 footnote a](../../../jama_thille_2019_oi_190108.pdf#page=6); p5 lung row; p4 narrative | Chronic lung disease A87/302(29%), B126/339(37%), P=.02; only significant baseline difference per footnote. |
| S002 | [p8 Table2 primary](../../../jama_thille_2019_oi_190108.pdf#page=8); p1 Results; p6 Primary Outcome; p2 Key Points; p8 Discussion | Day7 reintubation A55/302, B40/339, rounded18%/12% table. Abstract/narrative B11.8%(8.4-15.2), A18.2%(13.9-22.6); B-A difference−6.4%(−12.0 to−0.9), P=.02; chi-square primary per p4. KeyPoints11.8 vs18.2. Narrative says lower B; separate log-rank S026. |
| S003 | [p8 Table2 respiratory failure](../../../jama_thille_2019_oi_190108.pdf#page=8); p1 Results; p6 Secondary Outcomes | Day7 A88/302(29%), B70/339(21%); Table2 difference−8.5%(−15.2 to−1.8), P=.01. Abstract and p6 narrative print difference−8.7%(same CI), P=.01; preserve each transcription. |
| S004 | [p8 Table2 48h](../../../jama_thille_2019_oi_190108.pdf#page=8); p6 narrative | Reintubation48h A36/302(12%), B24/339(7%), difference−4.8%(−9.6 to−0.3), P=.04; narrative significant lower B. |
| S005 | [p8 Table2 72h](../../../jama_thille_2019_oi_190108.pdf#page=8); p6 narrative | A47/302(16%), B30/339(9%), difference−6.7%(−11.9 to−1.7), P=.009. |
| S006 | [p8 Table2 ICU reintubation](../../../jama_thille_2019_oi_190108.pdf#page=8); p1 abstract; p6 narrative; p7 total100 | Up to ICU discharge A59/302(20%), B41/339(12%), difference−7.4%(−13.2 to−1.8), P=.009; abstract12 vs20%; narrative significantly lower B. |
| S007 | [p8 Table2 ICU stay](../../../jama_thille_2019_oi_190108.pdf#page=8) | Median(IQR) days A11(7-19), B12(7-19), displayed difference0.5(−1.6 to2.6), P=.55. Column heading “Absolute Difference, % (95% CI)” is shared across table. Difference estimand/test not specified in main. |
| S008 | [p8 Table2 hospital stay](../../../jama_thille_2019_oi_190108.pdf#page=8) | Median(IQR) days A23(15-39), B25(15-42), difference2.3(−1.4 to6.1), P=.31; same shared heading; no difference-estimator definition printed. |
| S009 | [p8 Table2 ICU mortality](../../../jama_thille_2019_oi_190108.pdf#page=8); p1 abstract; p7 narrative | A26/302(9%), B21/339(6%), difference−2.4%(−6.7 to1.7), P=.25. Abstract6 vs9, same tuple; not significant. |
| S010 | [p8 Table2 hospital mortality](../../../jama_thille_2019_oi_190108.pdf#page=8); p7 narrative | A46/302(15%), B54/339(16%), difference0.7%(−5.0 to6.3), P=.80; narrative not significant. |
| S011 | [p8 Table2 day28 mortality](../../../jama_thille_2019_oi_190108.pdf#page=8) | A33/302(11%), B39/339(12%), difference0.6%(−4.4 to5.5), P=.82. |
| S012 | [p8 Table2 day90 mortality](../../../jama_thille_2019_oi_190108.pdf#page=8); p7 narrative | A65/302(21%), B62/339(18%), difference−3.2%(−9.5 to2.9), P=.30. P4 additionally specifies death90d log-rank; matching supplemental eFigure assigned support. |
| S013 | [p8 Table2 criteria during ICU stay](../../../jama_thille_2019_oi_190108.pdf#page=8) | Patients meeting reintubation criteria A65/302(22%), B49/339(14%), difference−7.1%(−13.1 to−1.1), P=.02; all analyzed denominator distinct from S020 among actual reintubated. |
| S014 | [p8 Table2 mortality OR reintubation ICU](../../../jama_thille_2019_oi_190108.pdf#page=8) | A64/302(21%), B51/339(15%), difference−6.2%(−12.2 to−0.2), P=.04; composite event. |
| S015 | [p8 Table2 mortality reintubated](../../../jama_thille_2019_oi_190108.pdf#page=8); p9 discussion N079 | A21/59(36%), B11/41(27%), difference−8.8%(−25.7 to9.9), P=.35; conditional on ICU reintubation. |
| S016 | [p7 first paragraph](../../../jama_thille_2019_oi_190108.pdf#page=7); p6 paragraph beginning | Continuation beyond48h B86/339(25%) vs A106/302(35%), difference−9.7%(−16.8 to−2.6), P<.01. |
| S017 | [p7 Exploratory Outcomes gases](../../../jama_thille_2019_oi_190108.pdf#page=7) | At1h PaO2:FIO2 mean(SD) B291(97) vs A254(113)mm Hg, difference37.0(19.7 to54.3), P<.001; B assessed on NIV, A on high-flow (p3). Item-specific gas denominators not printed here. |
| S018 | [p7 Exploratory Outcomes hypercapnia](../../../jama_thille_2019_oi_190108.pdf#page=7) | At1h hypercapnia B21% vs A19%, difference1.2%(−5.4 to7.7), P=.72; no numerator/measurement denominator printed in main paragraph. |
| S019 | [p7 time to reintubation](../../../jama_thille_2019_oi_190108.pdf#page=7) | Median(IQR) B33(7-81)h vs A39(12-67)h; displayed difference−5.0(−42.0 to32.0), P=.76; not significant; difference estimand/test unspecified here. |
| S020 | [p7 criteria among reintubated](../../../jama_thille_2019_oi_190108.pdf#page=7) | B39/41(95%) vs A57/59(97%), pooled96% of100; difference−1.5%(−13.0 to7.4), P=.99; definition N011. |
| S021 | [p7 hypercapnic subgroup](../../../jama_thille_2019_oi_190108.pdf#page=7); p8 Figure3A | N111, PaCO2 >45; day7 B8% vs A21%, difference−12.9%(−27.1 to−0.1), P=.049. Figure initial denominators B63/A48; source main does not print event numerators in this paragraph. Figure log-rank separately S027. |
| S022 | [p7 nonhypercapnic subgroup](../../../jama_thille_2019_oi_190108.pdf#page=7); p8 Figure3B | N530, PaCO2 ≤45; day7 B13% vs A18%, difference−5.0%(−11.2 to1.1), P=.10; figure initial B276/A254. Figure log-rank separately P=.11 S028. |
| S023 | [p7 interaction](../../../jama_thille_2019_oi_190108.pdf#page=7); p4 Statistical Analysis | PaCO2-at-enrollment stratum by treatment interaction for primary, P=.25; narrative no significant interaction; type/statistic of interaction test not printed. |
| S024 | [p7 adjusted primary](../../../jama_thille_2019_oi_190108.pdf#page=7); p4 analysis model | B vs A adjusted OR0.60(0.38-0.93), P=.02; adjusted for PaCO2≤45/>45 and chronic lung disease, multiple logistic regression, day7 reintubation. |
| S025 | [p7 hospital random-effect paragraph](../../../jama_thille_2019_oi_190108.pdf#page=7); p4 model | Post hoc multilevel logistic regression: treatment fixed effect, hospital random effect; P=.02 without hospital random effect and P=.02 after hospital random-effect adjustment; narrative lower B; main no separate post hoc OR/CI printed; cross-source target eTable5. |
| S026 | [p7 Figure2](../../../jama_thille_2019_oi_190108.pdf#page=7); p4 KM methods | Overall time-to-reintubation day7 Kaplan-Meier log-rank P=.02; axes/caption N068 and complete risk rows N069-N070. Distinct test from primary chi-square S002. |
| S027 | [p8 Figure3A](../../../jama_thille_2019_oi_190108.pdf#page=8) | Hypercapnic time-to-reintubation day7 Kaplan-Meier log-rank P=.049; risk rows N072-N073. Distinct time-to-event test from subgroup proportion comparison. |
| S028 | [p8 Figure3B](../../../jama_thille_2019_oi_190108.pdf#page=8) | Nonhypercapnic time-to-reintubation day7 Kaplan-Meier log-rank P=.11; risk rows N075-N076. Distinct from narrative proportion P=.10. |
| S029 | [p4 Statistical Analysis full rules](../../../jama_thille_2019_oi_190108.pdf#page=4) | All randomized extubated with completed primary analyzed by assignment regardless applied treatment. Primary chi-square; predefined reintubation, respiratory failure, ICU/hospital mortality chi-square; log-rank for reintubation7d/death90d. Logistic adjustment: baseline imbalance P<.05, only chronic lung included plus PaCO2 strata; OR95%CI; interaction before subgroup analysis; two-tailed .05; secondary exploratory multiplicity; SAS9.4. Sample-size power80%, alpha.05, 590 before10% inflation650 (N014). No test statistic/SE/CI method supplied here. |

## Alignment and completeness notes for downstream reviewers

- Primary tuple links abstract, Key Points, Results, Table2, Figures2/3 and discussion, with test differences preserved. Statistical rows include every printed P value in result or footnote content; S029 captures analysis thresholds and calculation settings.
- All Table1 rows are mapped, including each main-intubation category, overlapping comorbidity subcategory, measured-subset denominator, and footnote scale. Totals are relationships to check, not evaluated diagnoses.
- Every Table2 inferential row is mapped. Continuation beyond48h is retained as the eleventh secondary endpoint outside that table. All exploratory narrative tuples, adjusted/interaction analyses and all figure risk numbers are included.
- Figure line endpoints are visual approximations only; printed percentages and inferential tuples carry exact numerical authority. No exact event counts were inferred from risk-table decrements.
- Main-paper text does not establish continuous difference estimators, all gas sample sizes, all interval methods, or rescue/reintubation reason exclusivity. Those are named missing definitions for checking, not omitted coverage. The supplied supplement may add definitions; support mapper owns it.
- Background numerical literature summaries are mapped as current REPORT statements but do not trigger external-source searches. Reference metadata, affiliations, registration codes and journal pagination are not patient outcomes.

## Completion record

Mapped source units: 11/11. Reusable-backed:11; fresh-required:0. Relationship count:109 (N001-N080 =80; S001-S029 =29). Every unit complete, including two explicit no-applicable-new-result pages. Scientific coverage gaps: none. Derivative limitations: none for assigned coverage. No additional shard files required; artifact below context bounds. Candidate decisions: not performed by mapper.
