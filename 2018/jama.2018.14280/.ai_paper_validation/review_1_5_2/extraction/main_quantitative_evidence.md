# Main-paper quantitative evidence map — DOC-001

## Scope and source basis

Fresh mapping of all nine PDF pages of `jama_simonis_2018_oi_180108.pdf` (DOC-001). Native and layout text were inspected, with rendered PDF pages 1, 3, 5, 6, and 7 checked for the abstract, Figure 1, Table 1, Table 2, and Figure 2. PDF pages below are physical PDF pages. This is an evidence inventory, not a candidate assessment.

## Population, allocation, and flow

| Provisional ID | Exact location | Printed evidence and quantitative relationship | Cross-source key |
|---|---|---|---|
| MN001 | PDF p. 1, Abstract; p. 5, Results | Enrollment was 961 (65% male), median age 68 years (IQR 59-76); randomized intervention groups were low tidal volume n=477 and intermediate tidal volume n=484. The two allocations sum to 961. | POP:ITT-961; ALLOC:477:484 |
| MN002 | PDF p. 3, Figure 1; p. 5, Results | 3695 assessed; 2734 excluded = 961 ineligible + 1773 eligible but not enrolled; the two exclusion subgroups sum to 2734; 3695 − 2734 = 961 randomized. | FLOW:screened-to-randomized |
| MN003 | PDF p. 3, Figure 1 | Ineligible n=961: pulmonary disease 323, ventilation >12 h 268, ARDS 193, uncontrolled intracranial pressure 98, thromboembolism 50, age <18 y 27, pregnant 2; listed reasons sum to 961. | FLOW:ineligible-961 |
| MN004 | PDF p. 3, Figure 1 | Eligible but not enrolled n=1773: missed 705, other study 348, no deferred consent 296, no randomization time 256, transfer within 1 d 57, physician decision 55, accidental double randomization 12, other 44; listed reasons sum to 1773. | FLOW:not-enrolled-1773 |
| MN005 | PDF p. 3, Figure 1; p. 5, Results | Randomized low/intermediate = 477/484; primary-analysis data 475/480 and lost-to-follow-up 2/4. Each analysis count plus loss equals its allocated group; total loss is 6, matching the Results statement that day-28 follow-up was incomplete for 6. | FLOW:analysis-475:480; FOLLOWUP:6 |
| MN006 | PDF p. 2, Methods | Six Netherlands ICUs; trial dates September 1, 2014 to August 20, 2017; 1:1 allocation; random blocks minimum 2 and maximum 6; stratification by center and intubation location. | DESIGN:6ICU; RAND:1:1 |

## Intervention, outcome definition, and analysis-population quantities

| Provisional ID | Exact location | Printed evidence and quantitative relationship | Cross-source key |
|---|---|---|---|
| MN007 | PDF p. 2, Interventions | Low strategy began at 6 mL/kg PBW, decreased 1 mL/kg PBW hourly to minimum 4; minimum pressure support 5 cm H2O; >8 mL/kg PBW accepted under minimum support. Intermediate strategy began at 10 mL/kg PBW; if plateau pressure >25 cm H2O, it decreased 1 mL/kg PBW hourly; maximum airway pressure <25 cm H2O under pressure support. | INT:tidal-volume-targets |
| MN008 | PDF p. 3, Methods | PBW equations: men 50 + 0.91 × (height cm −152.4); women 45.5 + 0.91 × (height cm −152.4). Strategies continued maximum 28 days. | SCALE:PBW; TIME:28d |
| MN009 | PDF p. 4, Outcomes | Primary outcome: days alive and free from invasive ventilation at day 28; unassisted breathing must exceed 24 consecutive hours; qualifying periods after repeated intubation were summed. >28 ventilation days were assigned zero ventilator-free days. One additional day approximated a 15% reduction of expected ventilation time. | OUTCOME:VFD28-definition |
| MN010 | PDF p. 4, Statistical Analysis | Planned sample 952 (476/group), 80% power for a 1-day difference, baseline SD 5 days, alpha .05, allowing 20% dropout. Primary t tests with 95% superiority CIs; sensitivity generalized linear mixed model with hospital and intubation location random effects. | PLAN:primary-power; MODEL:primary |
| MN011 | PDF p. 4, Statistical Analysis | ICU/hospital stay and mortality used Kaplan-Meier curves and Cox proportional-hazard HRs; survival from randomization to all-cause death/censoring. Other binary outcomes used RR and 95% CI (Wald likelihood-ratio approximation) and chi-square P values; ICU/hospital stay estimate used inverse-Gaussian generalized linear models. All P values two-sided; alpha .05; primary missingness <1%, complete-case analysis. | MODEL:survival; MODEL:binary; P:two-sided |

## Baseline table: every displayed row

Table 1 is on PDF p. 5 and compares low n=477 with intermediate n=484. Values are median (IQR) unless labelled No. (%). Higher SAPS II, LIPS, and SOFA values mean greater severity/risk as footnoted.

| Provisional ID | Table 1 printed values: low vs intermediate | Cross-source key |
|---|---|---|
| MN012 | Age y 68 (59-76) vs 67 (58-75); male 312 (65.4%) vs 309 (63.8%); BMI 24.9 (22.6-28.7) vs 25.5 (23.0-28.3); PBW kg 70.1 (60.6-76.0) vs 69.7 (59.7-75.1). | BASE:demography |
| MN013 | SAPS II 52 (40-63) vs 51 (39-62), scale 0-163; LIPS 4.5 (3.0-7.0) vs 4.5 (3.0-6.5), scale 0-33.5; LIPS ≥4 high-risk; at-risk ARDS 292 (61.6%) vs 290 (60.3%); SOFA 8 (6-11) vs 8 (6-10), scale 0-24; septic shock 82 (17.6%) vs 74 (15.5%). | BASE:severity |
| MN014 | Tobacco: never 106 (22.3%) vs 111 (23.0%); current 97 (20.4%) vs 97 (20.1%); previous 75 (15.8%) vs 80 (16.6%); unknown 197 (41.5%) vs 194 (40.2%). Each group’s categories sum to 475, not the allocated totals 477/484. | BASE:tobacco; DENOM:475 |
| MN015 | Alcohol: none 121 (25.5%) vs 92 (19.1%); 0-5 drinks/week 47 (9.9%) vs 61 (12.7%); 6-14/week 26 (5.5%) vs 30 (6.2%); >2/day 59 (12.4%) vs 56 (11.6%); unknown 222 (46.7%) vs 243 (50.4%). Each group’s categories sum to 475/482. | BASE:alcohol; DENOM:475:482 |
| MN016 | ICU admission: surgical 82 (17.3%) vs 79 (16.4%); medical 393 (82.7%) vs 403 (83.6%); each sums to its randomized total. Initial ICU intubation 209 (43.8%) vs 215 (44.4%). | BASE:admission; INTUBATION:ICU |
| MN017 | Intubation reason: cardiac arrest 110 (23.1%) vs 120 (24.8%); postoperative 82 (17.2%) vs 79 (16.3%); pneumonia 77 (16.1%) vs 77 (15.9%); sepsis 50 (10.5%) vs 46 (9.5%); airway protection 39 (8.2%) vs 39 (8.1%); cardiac failure 28 (5.9%) vs 17 (3.5%). | BASE:intubation-reason-A |
| MN018 | Intubation reason continued: head trauma/brain surgery 25 (5.2%) vs 31 (6.4%); aspiration 20 (4.2%) vs 24 (5.0%); non-septic shock 8 (1.7%) vs 10 (2.0%); airway obstruction 7 (1.5%) vs 1 (0.2%); neuromuscular disease 6 (1.3%) vs 3 (0.6%); hypercapnic respiratory failure 4 (0.8%) vs 10 (2.0%); other respiratory failure 4 (0.8%) vs 4 (0.8%); trauma 3 (0.6%) vs 4 (0.8%); other causes 14 (2.9%) vs 19 (3.9%). Listed categories sum to 477/484. | BASE:intubation-reason-B |
| MN019 | Hours ventilated before randomization 0.9 (0.3-2.0) vs 0.9 (0.4-2.1). Ventilation mode: volume-controlled 143 (30.0%) vs 154 (31.8%); pressure support 98 (20.5%) vs 91 (18.8%); pressure-controlled 236 (49.5%) vs 239 (49.4%); modes sum to 477/484. | BASE:pre-rand-ventilation |
| MN020 | Before randomization: tidal volume mL/kg PBW 7.0 (6.0-8.3) vs 7.3 (6.3-8.8); plateau pressure cm H2O 18.0 (14.7-21.0) vs 20.0 (16.0-24.0); respiratory rate/min 20 (16-22) vs 20 (16-22); PEEP cm H2O 7 (5-8) vs 7 (5-8); driving pressure cm H2O 11.0 (8.7-14.0) vs 13.0 (10.0-16.0). | BASE:respiratory-A |
| MN021 | Before randomization continued: FiO2 0.50 (0.40-0.70) vs 0.50 (0.40-0.65); PaO2/FiO2 mm Hg 197 (127-298) vs 195 (133-300); PaCO2 mm Hg 42.7 (37.5-50.2) vs 42.7 (36.0-51.0); arterial pH 7.31 (7.22-7.38) vs 7.30 (7.22-7.38). | BASE:respiratory-B |

## Main outcomes and repeated narrative/abstract claims

| Provisional ID | Exact locations | Printed evidence and relationship | Cross-source key |
|---|---|---|---|
| MN022 | PDF p. 1 Abstract; p. 5 Results; p. 6 Table 2 | Primary-analysis n=475/480. VFD day 28: mean (SD) 15.2 (11.6) vs 15.5 (11.4); median (IQR) 21 (0-26) vs 21 (0-26); mean difference −0.27, 95% CI −1.74 to 1.19, P=.71. Abstract repeats medians, n, difference/CI/P. | OUT:VFD28 |
| MN023 | PDF p. 6 Table 2 | Surviving-patient ventilation days: mean (SD) 5.4 (6.6) vs 6.0 (7.3); median (IQR) 3 (1-6) vs 3 (1-8); mean difference −0.56, 95% CI −1.61 to 0.49 (no P displayed). | OUT:vent-days-survivors |
| MN024 | PDF p. 1 Abstract; p. 6 Table 2; p. 7 Figure 2C | Secondary n=475/481. ICU stay: mean (SD) 9.6 (13.3) vs 9.2 (9.9); median (IQR) 6 (3-11) vs 6 (3-11); mean difference 0.39 (−1.09 to 1.89), P=.58. Abstract repeats medians/difference/CI/P. Figure 2C instead reports HR 0.94 (0.80-1.09), P=.41 and risk sets 458/456 at day 0. | OUT:ICU-stay |
| MN025 | PDF p. 1 Abstract; p. 6 Table 2; p. 7 Figure 2D | Hospital stay: mean (SD) 20.4 (23.8) vs 21.0 (21.1); median (IQR) 14 (6-26) vs 15 (8-26); mean difference −0.60 (−3.52 to 2.31), P=.68. Abstract repeats median/difference/CI/P. Figure 2D reports HR 1.02 (0.87-1.19), P=.83 and risk sets 458/456 at day 0. | OUT:hospital-stay |
| MN026 | PDF p. 1 Abstract; p. 6 Table 2 | ICU mortality: 132/450 (29.3%) vs 115/458 (25.1%), RR 1.11 (0.96-1.27), P=.15. Hospital mortality: 151/477 (31.7%) vs 140/484 (28.9%), RR 1.06 (0.93-1.22), P=.35. | OUT:mortality-ICU-hospital |
| MN027 | PDF p. 1 Abstract; p. 6 Table 2; p. 7 Figure 2B | 28-day mortality: 166/476 (34.9%) vs 155/483 (32.1%), HR 1.12 (0.90-1.40), P=.30. 90-day mortality: 186/476 (39.1%) vs 181/479 (37.8%), HR 1.07 (0.87-1.31), P=.54. Abstract repeats both; Figure 2B repeats 90-day HR/CI/P and shows day-0 risk sets 476/479. | OUT:mortality-28-90 |
| MN028 | PDF p. 1 Abstract; p. 6 Table 2 | ARDS 17/448 (3.8%) vs 23/462 (5.0%), RR 0.86 (0.59-1.24), P=.38; pneumonia 19/450 (4.2%) vs 17/462 (3.7%), RR 1.07 (0.78-1.47), P=.67. Both repeat in abstract. | OUT:ARDS-pneumonia |
| MN029 | PDF p. 1 Abstract; p. 6 Table 2 | Pneumothorax 8/448 (1.8%) vs 6/462 (1.3%), RR 1.16 (0.73-1.84), P=.55; atelectasis 51/449 (11.4%) vs 52/464 (11.2%), RR 1.00 (0.81-1.23), P=.94. Both repeat in abstract. | OUT:pneumothorax-atelectasis |
| MN030 | PDF p. 6 Table 2 | Extrapulmonary infection 20/448 (4.5%) vs 28/463 (6.0%), RR 0.84 (0.60-1.18), P=.28; extrapulmonary sepsis 12/448 (2.7%) vs 16/463 (3.5%), RR 0.87 (0.56-1.33), P=.50. | OUT:infection-sepsis |
| MN031 | PDF p. 6 Table 2 | Delirium 149/343 (43.4%) vs 132/361 (36.6%), RR 1.15 (0.99-1.34), P=.06; need for tracheostomy 54/477 (11.3%) vs 52/484 (10.7%), RR 1.03 (0.84-1.26), P=.78. | OUT:delirium-tracheostomy |
| MN032 | PDF p. 5 Results | Start-of-ventilation-to-randomization median 0.88 h (IQR 0.36-2.01); ICU-ventilation-start-to-randomization median 0.57 h (0.23-1.00). First three days: tidal volumes/airway pressures significantly different; plateau/driving pressure lower and respiratory rate higher in low group; minute ventilation, PEEP, PaO2 and FiO2 not significantly different; PaCO2 higher and pH lower in low group. Detailed numerical values are supplied in DOC-004 eTables/eFigures. | INT:timing; OUT:ventilator-physiology |
| MN033 | PDF p. 6 Results | Stratified sensitivity model result consistent with primary analysis, P=.72. Narrative states no group differences in median ICU/hospital stays, ICU/hospital/28/90-day mortality, ARDS, pneumonia, severe atelectasis, pneumothorax, delirium, and specified therapies. | OUT:narrative-secondary |
| MN034 | PDF p. 6 Results | Exploratory interaction by intubation location: inside ICU mean difference −2.50 (IQR −4.63 to −0.36) versus outside ICU mean difference 1.45 (IQR −0.52 to 3.43); P for interaction=.01. The display calls the intervals IQR. | OUT:subgroup-intubation-location |

## Figure 2 and captions: all displayed quantitative values

| Provisional ID | Exact location | Printed evidence and relationship | Cross-source key |
|---|---|---|---|
| MN035 | PDF p. 7, Figure 2A | Free-from-invasive-ventilation curve: HR 0.99 (95% CI 0.86-1.14), P=.92. Days 0,3,6,9,12,15,18,21; at-risk intermediate 484,257,176,122,102,85,71,62 and low 476,251,162,117,94,82,71,67. Caption observation median (IQR) 4.4 (3.7-5.1) d low vs 4.3 (3.4-5.2) d intermediate; Schoenfeld-residual P=.68. | FIG:VFD-curve |
| MN036 | PDF p. 7, Figure 2B | 90-day survival curve: HR 1.07 (0.87-1.31), P=.54; days 0,10,20,30,40,50,60,70,80,90; at-risk intermediate 479,375,341,324,322,316,312,308,306,299 and low 476,355,324,312,303,299,296,294,293,291. Caption: median observation time not computed because minimum observed value 0.60; Schoenfeld P=.13. | FIG:90d-survival |
| MN037 | PDF p. 7, Figure 2C | ICU-length-of-stay curve: HR 0.94 (0.80-1.09), P=.41; days 0,5,10,15,20; at-risk intermediate 458,271,134,64,34 and low 450,253,118,72,29. Caption median observation 8.0 (7.0-8.0) d low vs 8.0 (6.0-9.0) d intermediate; Schoenfeld P=.21. | FIG:ICU-stay-curve |
| MN038 | PDF p. 7, Figure 2D | Hospital-length-of-stay curve: HR 1.02 (0.87-1.19), P=.83; days 0,6,12,18,24,30,36,42,48; at-risk intermediate 456,375,270,196,133,93,74,62,49 and low 458,356,262,177,127,93,73,55,39. Caption observation 21.0 (19.0-23.0) d low vs 21.0 (20.0-24.0) d intermediate; Schoenfeld P=.82. | FIG:hospital-stay-curve |

## Repeated qualitative quantitative interpretations and limits

| Provisional ID | Exact location | Printed evidence and relationship | Cross-source key |
|---|---|---|---|
| MN039 | PDF p. 1 Abstract; p. 2 Key Points; p. 6-8 Discussion/Conclusion | All state the low strategy did not produce greater VFD at day 28 / was not more effective; the numerical anchor is MN022. | INTERP:primary-null |
| MN040 | PDF p. 8 Discussion | Discussion describes study as 6 centers, enrolled over 3 years; reported intermediate tidal volume 9 mL/kg PBW and low 7 mL/kg PBW in comparison narrative, while Table 1 is pre-randomization and detailed on-treatment data reside in DOC-004. | DISCUSSION:tidal-volume-summary |

## Location conventions and gaps

All main-paper result displays were legible in fresh layout text and the specified rendered pages. Page 2-4 method quantities were recorded when needed to define reported results. The main article references Supplement 3 for eTables/eFigures and Supplement 2 for plan changes; their detailed values are deliberately not duplicated here because separately assigned support mapping owns those direct sources.
