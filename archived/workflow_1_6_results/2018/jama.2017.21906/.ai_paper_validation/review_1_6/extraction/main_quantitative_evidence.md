# Main-paper quantitative evidence map

Scope: DOC-001, jama_huffman_2018_oi_170166.pdf, all physical pages 1-12 (printed pages 567-578). Document role REPORT. All units reusable-backed; no fresh-required unit. Direct source controls evidence. Locators: reusable pdftotext layout/native text under review_1_5_2/preprocessing and rendered DOC-001 p.1/pp.4-10. Engine of reused text: historical pdftotext; current tooling Poppler 25.03.0. Figures 1, 2 and 3 visually inspected in reusable source-bound images. No OCR, Python extraction, GPU or web used. Numeric transcription below retains printed precision; mapped relationships are observations, with no candidate diagnosis. Every link targets physical PDF page. N/S IDs here are main-specific preliminary IDs; coordinator may assign package-global IDs while preserving crosswalk.

## Complete page coverage

| Physical page | Printed page | Mapped scope | Status |
|---|---|---|---|
| 1 | 567 | Abstract design, flow, characteristics, outcome and adjusted effects | COMPLETE |
| 2 | 568 | Key Points; background quantities; recruitment, randomization, time and strata definitions | COMPLETE |
| 3 | 569 | Intervention timing, outcome definitions, sample size, power, models and significance rules | COMPLETE |
| 4 | 570 | Figure 1 all control-step and intervention cohort-step boxes and exclusions | COMPLETE |
| 5 | 571 | Table 1 all 27 numeric rows and footnotes; recruited/excluded totals and quality assurance | COMPLETE |
| 6 | 572 | Table 2 all 21 rows and footnotes; follow-up, participant and process prose | COMPLETE |
| 7 | 573 | Table 3 all 10 rows and footnotes; process and primary outcome prose | COMPLETE |
| 8 | 574 | Figure 2 both panels, all 30 cohort-step cells each; mortality/expanded-event prose | COMPLETE |
| 9 | 575 | Figure 3 all 14 subgroups; expanded-event continuation; subgroup and discussion claims | COMPLETE |
| 10 | 576 | Discussion external comparator quantities, limitations and conclusions | COMPLETE |
| 11 | 577 | Author/funder/site list and bibliographic citations; no new applicable trial result | COMPLETE_NO_APPLICABLE_NEW_RESULT |
| 12 | 578 | Bibliographic references only; no applicable trial result | COMPLETE_NO_APPLICABLE_NEW_RESULT |

## N001 / S001 — Abstract and Key Points identities

Locations: [abstract](../../../jama_huffman_2018_oi_170166.pdf#page=1), [Key Points and design](../../../jama_huffman_2018_oi_170166.pdf#page=2). Trial dates November 10, 2014-November 9, 2016; last follow-up December 31, 2016. 63 hospitals; 5 predefined crossover steps plus baseline step 0; each step 4 months, total 24 months. Control total 10066, step 0-5 counts 2915,2649,2251,1422,829,0; intervention total 11308, step 0-5 counts 0,662,1265,2432,3214,3735. Eligible randomized participants 21374; mean age 60.6 (SD12.0) years; men 16183 (76%); STEMI 13689 (64%); completed trial 21079 (99%). Primary composite 30-day death/reinfarction/stroke/major bleeding: intervention 5.3%, control 6.4%; adjusted RD -0.09% (95%CI -1.32% to1.14%), OR0.98 (0.80-1.21). Abstract states difference not statistically significant after adjustment, higher medication use including reperfusion, no effect on tobacco counseling, no unexpected adverse events. Key Points repeats 63,21374,30-day6.4%/5.3% and nonsignificance after cluster/time adjustment. Conclusions on pp1/10 repeat no decrease in composite.

## N002 / S002 — Definitions, populations, time, models and inferential conventions

Locations: [methods](../../../jama_huffman_2018_oi_170166.pdf#page=2), [outcomes/statistics](../../../jama_huffman_2018_oi_170166.pdf#page=3). Hospitals recruited from earlier 125-hospital registry plus government hospitals; 2 local quality-team individuals required. 12 or13 hospitals informed of crossover 2 weeks before each step. Projected recruitment strata ≤200,201-500,501-1000,>1000 participants; cluster randomization at hospital, patient assignment by date of admission; no transition period. Training90-120min/site. Monthly audit feedback; central monitoring biweekly. Patient population STEMI or NSTEMI by Third Universal Definition. Primary 30-day MACE includes all-cause death, reinfarction, stroke, major GUSTO bleeding (intracerebral hemorrhage or hemodynamic compromise requiring treatment). Three failed contacts designate lost to follow-up. Secondary individual components, cardiovascular and in-hospital mortality; optimal inpatient aspirin/second antiplatelet/anticoagulant/β-blocker, optimal discharge aspirin/second antiplatelet/statin/β-blocker, tobacco counseling. Inpatient statin predefined but not collected. Expanded MACE additionally incident inpatient heart failure, shock, arrest: post hoc. Time-exposure interaction post hoc. Prespecified subgroup age/sex/STEMI-NSTEMI/hospital size/type.

Target n15750 from63 hospitals/5steps,80%power,2.4%absolute reduction,2-sided α.05;5%loss; assumed ICC.05. Primary mixed-effects logistic model random hospital effect plus fixed time effect each4months. Cluster-only model separately shown. Secondary additionally age,sex,MI type,systolic BP,heart rate,creatinine,acute HF,shock,resuscitated arrest (GRACE covariates). Intention-to-treat; interim12months; O'Brien-Fleming boundaries interim z>2.797,2-sided significance.005; final z>1.977,2-sided significance.048. No further a priori multiple-testing adjustment for secondary outcomes; exploratory. Tables and figures label intervals95%, without supplying one universal calculation for all CI types. Percentages and effects generally1/2 decimals; no explicit rounding algorithm. No person-time, incidence-density units, SEs or realized test statistics printed in main results. Displayed 'rate' means participant event proportion/process uptake, not events/person-time.

## N003 — Figure 1 complete flow

[Figure 1](../../../jama_huffman_2018_oi_170166.pdf#page=4). Control boxes describe hospitals not yet crossed; intervention boxes describe specific cohort. Columns below enrolled;lost follow-up;analyzed;excluded; exclusions as markers/transferred/outside-period/timeline. Lost participants included in analysis, not an additional subtraction. Caption includes both unreachable after3attempts and site did not perform follow-up. Pretrial63 screened/eligible/all agreed, randomization before enrollment, concealed until2weeks pre-crossover.

| Control step | Hospitals | Enrolled | Lost | Analyzed | Excluded | Markers | Transferred | Outside | Timeline |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 Nov10 2014-Mar9 2015 |63|3107|42|2915|192|172|18|0|2|
| 1 Mar10-Jul9 2015 |51|2765|45|2649|116|101|15|0|0|
| 2 Jul10-Nov9 2015 |38|2328|54|2251|77|67|10|0|0|
| 3 Nov10 2015-Mar9 2016 |25|1450|27|1422|28|25|3|0|0|
| 4 Mar10-Jul9 2016 |12|844|2|829|15|9|2|4|0|

| Intervention cohort (hospital n),step | Enrolled | Lost | Analyzed | Excluded | Markers | Transferred | Outside | Timeline |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1(12),1 |706|2|662|44|43|1|0|0|
| 1(12),2 |593|6|542|51|47|3|0|1|
| 1(12),3 |757|0|654|103|101|2|0|0|
| 1(12),4 |659|3|605|54|52|1|0|1|
| 1(12),5 |675|10|648|27|16|4|7|0|
| 2(13),2 |790|18|723|67|62|5|0|0|
| 2(13),3 |821|4|785|36|34|2|0|0|
| 2(13),4 |764|6|727|37|34|3|0|0|
| 2(13),5 |627|28|600|27|26|1|0|0|
| 3(13),3 |1076|10|993|83|64|19|0|0|
| 3(13),4 |1071|8|1022|49|19|29|0|1|
| 3(13),5 |991|7|964|27|20|7|0|0|
| 4(13),4 |895|7|860|35|32|2|0|1|
| 4(13),5 |637|7|627|10|9|1|0|0|
| 5(12),5 |1001|9|896|105|21|4|80|0|

N004 narrative flow [pp5-6](../../../jama_huffman_2018_oi_170166.pdf#page=5):22557 recruited; hospitals67%private,14%government affiliated with medical colleges,19%nonprofit/charity. Excluded954markers,132transfers,91outside,6time discrepancy; eligible21374;30-dayfollow-up99%.295(1%)incomplete=215not followed by enrolling site+80unreachable3attempts. Intervention11308(53%),control10066(47%). Follow-up-complete vs missing initial troponin1.3 vs4.6ng/mL,P<.001 (eTable1 locator); other baseline generally similar. Quality assurance one high-reinfarction site,10%case sampling plus corresponding controls,2additional systematic-error sites,13primary outcome changes(1%of overall events). No raw case details supplied in main.

## N005 / S003-S029 — Table 1 complete cells

[Table 1](../../../jama_huffman_2018_oi_170166.pdf#page=5), control10066,intervention11308. Differences crude intervention-minus-control; percent rows percentage-point differences; continuous rows native units. CI95%. Each row in order is S003 onward, including descriptive-difference intervals. Missing-data sample n explicitly retained.

| Characteristic | Control | Intervention | Difference (95%CI) |
|---|---|---|---|
| Age mean(SD)y |60.3(12.0)|60.9(12.1)|0.6(0.3 to1.0)|
| Male n(%) |7654(76.0)|8529(75.4)|-0.6(-1.8 to0.5)|
| Tobacco history n(%) |3772(37.5)|2842(25.1)|-12.3(-13.6 to-11.1)|
| Diabetes n(%) |4151(41.2)|5333(47.2)|5.9(4.6 to7.3)|
| Transfer n(%) |4202(41.7)|4199(37.1)|-4.6(-5.9 to-3.3)|
| No insurance n(%) |6878(68.3)|8664(76.6)|8.3(7.1 to9.5)|
| STEMI n(%) |6921(68.8)|6768(59.9)|-8.9(-10.2 to-7.6)|
| Symptom-door median(IQR)min |240(120-840),n9711|255(111-825),n10849|15(4 to26)|
| Weight mean(SD)kg |63.6(9.8),n10065|63.3(9.6),n11304|-0.3(-0.5 to0.0)|
| Systolic BP mean(SD)mmHg |138.1(29.1),n10061|139.0(28.9),n11303|0.9(0.1 to1.7)|
| Heart rate mean(SD)/min |80.0(18.7),n10065|79.9(19.1),n11303|-0.1(-0.6 to0.5)|
| Initial troponin median(IQR)ng/mL |1.6(0.4-8.0),n4566|1.1(0.2-4.4),n4483|-0.5(-0.7 to-0.4)|
| LDL mean(SD)mg/dL |126.2(40.3),n7288|119.1(41.2),n7542|-7.1(-8.4 to-5.8)|
| Triglycerides median(IQR)mg/dL |121(89-167),n7308|122(90-163),n7552|1(-1 to3)|
| Creatinine median(IQR)mg/dL |1.0(0.8-1.2),n4246|1.0(0.9-1.2),n9589|0.0(0.0 to0.0)|
| Glucose median(IQR)mg/dL |124(98-172),n6658|130(105-180),n6740|6(4 to8)|
| Hemoglobin mean(SD)mg/dL |13.3(2.0),n9763|13.2(2.0),n11079|-0.1(-0.2 to0.0)|
| Government hospitals n9 |4097(40.7)|3036(26.8)|-13.9(-15.1 to-12.6)|
| Nonprofit/charity hospitals n12 |2785(27.7)|2964(26.2)|-1.5(-2.7 to-0.3)|
| Private hospitals n42 |3184(31.6)|5308(46.9)|15.3(14.0 to16.6)|
| Extra large >1000,hospitals5 |1853(18.4)|1707(15.1)|-3.3(-4.3 to-2.3)|
| Large501-1000,hospitals15 |3561(35.4)|4962(43.9)|8.5(7.2 to9.8)|
| Medium201-500,hospitals24 |3847(38.2)|3568(31.6)|-6.7(-7.9 to-5.4)|
| Small≤200,hospitals19 |805(8.0)|1071(9.5)|1.5(0.7 to2.2)|
| Cath lab installed during study,hospitals3 |171(1.7)|325(2.9)|1.2(0.8 to1.6)|
| Cath lab no,hospitals17 |1998(19.8)|1554(13.7)|-6.1(-7.1 to-5.1)|
| Cath lab yes,hospitals43 |7897(78.5)|9429(83.4)|4.9(3.9 to6.0)|

SI conversions LDL×.0259mmol/L,triglycerides×.0113mmol/L,creatinine×88.4μmol/L,glucose×.0555mmol/L. n supplied for incompletely reported variables. Table1 participant counts under hospital characteristics, hospital counts in row labels. N006 matching prose [p6](../../../jama_huffman_2018_oi_170166.pdf#page=6):overallage60.6,men76%,tobacco31%,diabetes44%,STEMI64%; control symptom-door240(120-840),intervention255(111-825)min.

## N007 / S030-S050 — Table 2 complete cells

[Table 2](../../../jama_huffman_2018_oi_170166.pdf#page=6). Header adjusted within-hospital clustering and temporal trends; control10066/intervention11308. Values No./TotalNo.(%)unless continuous median(IQR). Totals eligible with process reported; contraindications excluded; discharge among discharged; ACEi/ARB among discharged with EF≤40%. Second antiplatelet clopidogrel/prasugrel/ticagrelor. Difference column prints percent heading even time rows. Footnote b: 'Odds ratios and β-coefficients represent effect of intervention compared with control and are calculated as the difference in marginal effects (intervention group minus control group) in a mixed-effects logistic regression or quantile regression model including a random-effects term to account for within-hospital clustering and temporal trends.' Retain wording for measure-label matching. Footnote c identifies β-coefficients for time rows. Each row S030 onward; nonestimable rows retained.

| Measure | Control | Intervention | Difference,%(95%CI) | OR or β(95%CI) |
|---|---|---|---|---|
| Prehospital aspirin |1696/10052(16.9)|2100/11300(18.6)|3.80(2.08 to5.52)|1.40(1.21-1.62)|
| Prehospital thrombolysis STEMI |25/6921(0.4)|37/6768(0.5)|-0.04(-0.76 to0.68)|0.95(0.40-2.28)|
| Inpatient aspirin |9858/10042(98.2)|11027/11286(97.7)|-0.05(-0.95 to0.84)|0.98(0.69-1.39)|
| Inpatient second antiplatelet |9861/10050(98.1)|11112/11297(98.4)|-0.05(-0.89 to0.79)|0.98(0.67-1.43)|
| Inpatient β-blocker |3676/9874(37.2)|4638/10885(42.6)|6.25(4.10 to8.40)|1.46(1.29-1.65)|
| Inpatient anticoagulant |8602/10051(85.6)|9654/11281(85.6)|2.60(0.87 to4.33)|1.27(1.09-1.49)|
| Echocardiography |9209/10066(91.5)|10516/11308(93.0)|5.62(3.35 to7.89)|2.50(1.95-3.21)|
| Diagnostic angiography |6181/10066(61.4)|6500/11308(57.5)|Nonestimable|Nonestimable|
| PCI |5282/10066(52.5)|5271/11308(46.6)|-1.66(-3.27 to-0.04)|0.87(0.77-0.99)|
| Primary PCI STEMI |3476/6921(50.2)|3234/6768(47.8)|-1.87(-3.85 to0.11)|0.86(0.73-1.01)|
| Door-balloon STEMI median(IQR)min |65(53-105),n4022|77(55-118),n3639|6.18(-4.78 to17.14)|β13.00(3.64-22.36)|
| Thrombolysis STEMI |1596/6921(23.1)|1571/6768(23.2)|5.56(3.21 to7.91)|1.59(1.33-1.92)|
| Door-needle STEMI median(IQR)min |44(30-67),n1455|45(27-75),n1433|0.40(-5.23 to6.03)|β5.00(-5.20-15.20)|
| Any reperfusion STEMI |5067/6921(73.2)|4805/6768(71.0)|3.43(0.87 to6.00)|1.24(1.06-1.46)|
| Rescue PCI STEMI |644/6891(9.3)|1031/6767(15.2)|2.45(0.51 to4.38)|1.39(1.08-1.79)|
| Discharge aspirin |8777/8998(97.5)|10360/10559(98.1)|1.36(0.23 to2.49)|1.65(1.15-2.37)|
| Discharge second antiplatelet |8824/9011(97.9)|10377/10580(98.1)|0.41(-0.31 to1.13)|1.24(0.86-1.79)|
| Discharge β-blocker |5808/8894(65.3)|6799/10178(66.8)|6.69(4.43 to8.95)|1.48(1.30-1.68)|
| Discharge statin |8700/9006(96.6)|10289/10579(97.3)|1.21(0.07 to2.35)|1.42(1.04-1.92)|
| Discharge ACEi/ARB |534/1029(51.9)|643/1495(43.0)|6.57(0.58 to12.57)|1.45(1.03-2.04)|
| Rehabilitation referral |2362/9228(25.6)|3322/10791(30.8)|Nonestimable|Nonestimable|

## N008 / S051 — Matched process narrative occurrences

[pp6-7](../../../jama_huffman_2018_oi_170166.pdf#page=6). Narrative order intervention then control. Prehospital aspirin18.6vs16.9%,RD3.80(2.08-5.52),OR1.40(1.21-1.62);prehospital thrombolysis<1%;inpatient aspirin/second antiplatelet>95%/similar. Inpatient β-blocker43vs37%,RD6.25(4.10-8.10),OR1.46(1.29-1.65). Anticoagulant86vs86%,RD2.60(.87-4.33),OR1.27(1.09-1.49). Echo93vs92%,RD5.62(3.35-7.89),OR2.50(1.95-3.21). Thrombolysis23vs23%,RD5.56(3.21-7.91),OR1.59(1.33-1.92);reperfusion71vs73%,RD3.43(.87-6.00),OR1.24(1.06-1.46);rescuePCI15vs9%,RD2.45(.51-4.38),OR1.39(1.08-1.79). Diagnostic angiography58vs61%;PCI47vs53%,RD-1.66(-3.27to-.04),OR.87(.77-.99). Discharge aspirin98vs98%,RD1.36(.23-2.49),OR1.65(1.15-2.37);β-blocker67vs65%,RD6.63(4.43-8.95),OR1.47(1.30-1.68);statin97vs97%,RD1.21(.07-2.35),OR1.42(1.04-1.92);ACEi/ARB EF≤40%,43vs52%,RD6.57(.58-12.57),OR1.45(1.03-2.04);rehab31vs26%. Discharge second antiplatelet and tobacco counseling characterized high>95% and similar. Preserve these distinct occurrences for table/prose matching rather than substitute table values.

## N009 / S052-S061 — Table 3 all cells

[Table 3](../../../jama_huffman_2018_oi_170166.pdf#page=7). Control10066/intervention11308; primary adjusted additionally temporal trends; cluster-only separately. Table title repeats 'clustering and clustering and temporal trends'. Intervals95%. Each row S052 onward. ICC printed per outcome. Table footnote a states odds ratios represent intervention vs control and 'are calculated as the difference in marginal effects (intervention group minus control group)' in mixed-effects logistic random hospital model; primary additionally time. No row P values.

| Outcome | Control No.(%) | Intervention No.(%) | Cluster RD %(CI) | Cluster OR(CI) | Primary RD %(CI) | Primary OR(CI) | ICC |
|---|---|---|---|---|---|---|---|
|30-day MACE|645(6.4)|602(5.3)|-.51(-1.28to.26)|.92(.81-1.04)|-.09(-1.32to1.14)|.98(.80-1.21)|.15|
|30-day mortality|509(5.1)|445(3.9)|-.65(-1.34to.03)|.87(.75-1.00)|-.28(-1.35to.80)|.94(.74-1.19)|.18|
|30-day cardiovascular mortality|494(4.9)|434(3.8)|-.58(-1.24to.09)|.88(.76-1.02)|-.26(-1.31to.80)|.94(.74-1.20)|.19|
|Inpatient mortality|331(3.3)|321(2.8)|-.05(-.58to.47)|.98(.82-1.17)|-.23(-1.07to.60)|.93(.70-1.22)|.18|
|30-day reinfarction|121(1.2)|135(1.2)|.12(-.31to.55)|1.08(.82-1.42)|.50(-.24to1.24)|1.39(.87-2.22)|.33|
|30-day stroke|60(.6)|90(.8)|.20(-.05to.45)|1.34(.94-1.93)|.14(-.23to.52)|1.24(.71-2.15)|.14|
|30-day major GUSTO bleeding|19(.2)|30(.3)|.13(-.05to.30)|1.56(.84-2.88)|.23(-.05to.52)|2.34(.93-5.89)|.20|
|Optimal inpatient medication|3122(31.7)|3878(35.8)|8.61(6.98to10.23)|1.70(1.57-1.85)|6.00(3.90to8.11)|1.45(1.28-1.64)|.40|
|Optimal discharge medication|5454(61.8)|6483(64.0)|9.97(8.32to11.61)|1.73(1.59-1.87)|8.66(6.30to11.03)|1.61(1.42-1.82)|.28|
|Tobacco cessation advice|3526(96.0)|2618(94.7)|.30(-1.20to1.80)|1.06(.80-1.39)|.30(-2.15to2.76)|1.06(.67-1.67)|.37|

Medication composite denominators among eligible for all agents; optimal discharge among discharged eligible; tobacco among discharged baseline smokers. Exact denominators not printed in Table3 rows and should not be silently replaced by column10066/11308. MACE defined death/reinfarction/stroke/major GUSTO bleed. Footnote major bleed intracerebral or hemodynamic compromise requiring treatment. Primary narrative p7 repeats intervention5.3%,control6.4%,clusterOR.92(.81-1.04),primaryRD-.09(-1.32to1.14),OR.98(.80-1.21),not statistically significant after time adjustment; imputation similar, hypothetical missing-event scenarios broader but plausible consistent. No scenario cell values printed here; eTable3/4 locators supplied by support package.

## N010 / S062-S063 — Figure 2 panels A/B complete graphical units

[Figure 2](../../../jama_huffman_2018_oi_170166.pdf#page=8). Unadjusted cohort-step participant event percentages with95%CI bars. PanelA30-dayMACE;PanelB30-daymortality. Y axes0,2,4,6,8,10,12,14%;xsteps0-5. Open control circles before cohort crossover, filled intervention afterward. Five cohorts;30 points per panel,60 total. Exact cohort/step denominators repeat identically in both panels:

| Cohort | Step0 | Step1 | Step2 | Step3 | Step4 | Step5 |
|---|---:|---:|---:|---:|---:|---:|
|1|439|662|542|654|605|648|
|2|400|379|723|785|727|600|
|3|858|910|827|993|1022|964|
|4|477|629|730|679|860|627|
|5|741|731|694|743|829|896|

Every plotted point/bar visually inspected. No numeric point or CI-endpoint labels printed: graphical readings below are approximate visual locators (percentage points, accuracy about0.3), not exact source numbers for arithmetic. Each cell Aestimate/Bestimate; all CI bars are95%, endpoints visually present and not numerically printed. Exact reported result sets must come from labeled source tables where matched.

| Cohort | Step0 A/B | Step1 A/B | Step2 A/B | Step3 A/B | Step4 A/B | Step5 A/B |
|---|---|---|---|---|---|---|
|1|3.4/3.0|3.8/2.7|2.4/2.0|2.6/2.3|3.2/2.7|5.7/1.7|
|2|5.8/3.2|4.5/4.2|7.9/6.0|5.7/5.1|4.4/3.2|3.7/3.0|
|3|9.8/7.6|10.0/7.4|8.8/7.4|7.6/5.5|6.8/5.4|5.4/3.9|
|4|3.4/2.3|7.0/5.6|5.6/4.2|7.8/6.3|6.1/3.9|5.1/4.5|
|5|6.3/5.3|5.0/3.1|4.8/4.2|4.6/3.9|4.6/4.1|6.2/4.4|

Graphical intervals not substituted by calculated binomial bounds: source does not label endpoint values or interval construction. Their full graphical display is available in cited source and reusable image. Caption explicitly95%CIs. Narrative p9 says intervention lower MACE and mortality first step than other steps; assess this as a graphical/narrative relationship with cohort/time/control matching. No Figure4 in main article.

## N011 / S064 — Mortality and expanded MACE prose

[pp8-9](../../../jama_huffman_2018_oi_170166.pdf#page=8). Mortality intervention3.9%,control5.1%;clusterOR.87(.75-1.00);time-adjustedRD-.28(-1.35to.80),OR.94(.74-1.19),not statistically significant;GRACE adjustment did not materially change result;inpatient outcomes similar. Post-hoc time exposure effect similar(eTable6). Expanded MACE intervention7.0%,control9.1%;clusterOR.89(.80-1.00);temporalRD-1.34(-2.72to.04),OR.84(.70-1.00). Expanded endpoint30-dayMACE plus inpatientHF/shock/arrest. p9 discussion characterizes lower expanded MACE rate, other secondary clinical outcomes not different, hypothesis-generating; these claims are separately mapped to the same endpoint/model context without inference.

## N012 / S065-S078 — Figure 3 complete subgroup entries

[Figure 3](../../../jama_huffman_2018_oi_170166.pdf#page=9). Prespecified30-dayMACE subgroup mixed-effects cluster/time adjusted intervention-minus-control differences, odds ratios intervention vs control; intervals95%. Forest horizontal axisOR.3,1.0,3.0;left favors intervention/right control; marker size precision. Each row S065 onward. Plotted points/intervals match numeric row context; intervals above3.0 use arrows. Narrative states similar pattern across age,sex,MI subtype,hospital size/type, and residual heterogeneity by hospital(eFigures1-2).

| Subgroup | Intervention n/N(%) | Control n/N(%) | Adjusted difference %(95%CI) | Adjusted OR(95%CI) |
|---|---|---|---|---|
|Age<50|58/2079(2.8)|68/2045(3.3)|1.42(-.71to3.54)|1.53(.83-2.79)|
|Age50-69|297/6606(4.5)|326/5863(5.6)|-.57(-2.02to.88)|.89(.67-1.19)|
|Age≥70|247/2623(9.4)|251/2158(11.6)|-.23(-3.32to2.85)|.98(.71-1.35)|
|Male|375/8529(4.4)|409/7654(5.3)|.05(-1.32to1.41)|1.01(.78-1.31)|
|Female|227/2779(8.2)|236/2412(9.8)|-.57(-3.13to2.00)|.93(.67-1.29)|
|STEMI|400/6768(5.9)|465/6921(6.7)|.57(-1.01to2.14)|1.09(.85-1.40)|
|NSTEMI|202/4540(4.4)|180/3145(5.7)|-1.46(-3.49to.57)|.75(.51-1.10)|
|Extra large>1000,n5hospitals|51/1707(3.0)|76/1853(4.1)|1.83(-.80to4.46)|1.68(.85-3.32)|
|Large501-1000,n15|168/4962(3.4)|212/3561(6.0)|-1.56(-3.58to.46)|.71(.47-1.08)|
|Medium201-500,n24|292/3568(8.2)|310/3847(8.1)|-1.47(-3.76to.83)|.83(.62-1.11)|
|Small<201,n19|91/1071(8.5)|47/805(5.8)|2.28(-2.24to6.79)|1.45(.70-3.04)|
|Government,n9|158/3036(5.2)|275/4097(6.7)|-.55(-2.56to1.47)|.90(.61-1.33)|
|Nonprofit,n12|186/2964(6.3)|193/2785(6.9)|-.62(-3.43to2.20)|.91(.59-1.40)|
|Private,n42|258/5308(4.9)|177/3184(5.6)|.89(-1.19to2.97)|1.16(.82-1.64)|

## N013 — Discussion/background quantities and no-applicable units

[Backgroundp2](../../../jama_huffman_2018_oi_170166.pdf#page=2):2015global fatalMI7.3million(95%uncertainty interval6.8-7.8million),SouthAsia highest age-standardized incident rate(no numeric rate);priorKerala25748ACS/125hospitals. These are quoted background claims, supplied main content only; no external verification. [Discussionp10](../../../jama_huffman_2018_oi_170166.pdf#page=10):CPACS3>29000Chinese participants;ACTION-GWTG2014inpatientmortality6.4%STEMI,3.4%NSTEMI. Context compares main-event rates but populations/time/type not interchangeable. Higher observedICC vs anticipated; lower events/higher care vsanticipated;secondary no multiple correction;conclusion no decrease30-dayMACE. [p11](../../../jama_huffman_2018_oi_170166.pdf#page=11)named hospital list/support/conflicts and bibliographic numeric volume/page/date values do not introduce result relationships;reference4 title25748ACS repeats background cohort. [p12](../../../jama_huffman_2018_oi_170166.pdf#page=12)references12-26 only, no new scientific numeric cells applicable. Software Stata14,SAS9.4,R3.3.0,StatTag3.0 [p5] identify analysis tools, not result numerators.

## Mapping completion and limitations

12/12 unique pages mapped. All 27Table1 rows,21Table2 rows,10Table3 rows,14Figure3 subgroups,20Figure1 boxes,60Figure2 plotted points and60 associated graphical CI bars,60 repeated Figure2 denominator occurrences mapped. Preliminary main numeric groups N001-N013; statistical groups S001-S080 (80), including intervals and nonestimable labels. Cross-occurrence groups intentionally retain independent printed precision. Main Figure2 only labels denominators/axes/CI level: exact plotted rates and interval endpoints are unavailable as printed numbers; graphical readings are explicitly approximate, and complete visual source exists. This is a precision limitation, not an omitted scientific unit. No other mapping gaps.

## S079 — Follow-up-group initial troponin P value

Location p6 participants paragraph, eTable1 cross-document locator. Included participants initial troponin1.3ng/mL versus missing-follow-up participants4.6ng/mL;P<.001. Main narrative does not print group sample n for this measurement, dispersions, or named test. Preserve this as a separate statistical relationship, not a calculable same-test claim without support inputs. Overall missing-follow-up n295 and complete n21079 are population identities, not automatic troponin denominators.

## S080 — Background uncertainty interval

Location p2 first paragraph: estimated fatal MI worldwide2015,7.3million,95%uncertainty interval6.8-7.8million. This is supplied background REPORT content; 'uncertainty interval' retained rather than relabeled a trial confidence interval. External cited paper is not read or required. No P/test statistic supplied for this relationship.

Final statistical relationship count is80, S001-S080; N001-N013 numeric groups. All three figures and all three tables completed; no Figure4 is present. Table1/Table2/Table3 plus matching process prose visually inspected in source-bound images pp5/6/7 as well as layout locators; no values silently normalized from prose to table or vice versa.

## Coordinator source correction after mechanical recheck

The fresh recheck of direct PDF Figure 1 p. 4 found cohort 2 step 5 prints **28** lost to follow-up; the initial table locator incorrectly recorded **8**. That cell above is corrected with explicit provenance to verification/evidence_recheck.md C017. Control losses sum 170 and intervention losses 125, total 295, matching main p. 6 and eTable 1. The original 8 input and consequent candidate remain preserved in the candidate ledger/recheck, with evidence state not_reproduced. No source/reused artifact changed.
