# Numeric applicability checks: numeric_support_s_301_388.md

Source-bounded shard, 88 mapped S IDs, all NUMERIC_COMPLETE. These preserve original stable S IDs and cross-reference the inferential inventory. REPORT main rows, REPORT results support rows, and PLAN prospective rows retain source roles from the mapper records. Percentage arithmetic uses half-unit printed-input intervals and printed percentage ±0.05 for one decimal. Fitted-model effects are not treated as crude risks; effect identity diagnostics are labelled explicitly.

### S301

| S301 | DOC-002 p.11 | Original power: 356/group, two-sided .05, 80%, 30% high vs40% low, RR .75; dropout5%, 374/group, total748. Match sample size narrative. |

**Numeric check: NUMERIC_COMPLETE.** 356+356=712;374+374=748. Nominal5% dropout adjustment712/.95=749.47 differs1.47 from748; allowing printed input half-units yields overlap or relative gap <.05. No numeric finding.

### S302

| S302 | DOC-002 p.11 | Revised power: first618 patients collapsed incidence lower than expected; control .20, RR .75, power80%, overall alpha .05, max1912 accounting for efficacy/futility monitoring, 5% dropout target2013; East6.0. |

**Numeric check: NUMERIC_COMPLETE.** 1912/.95=2012.6316 rounds2013. Sequential maximum1912 is distinct from recruited target2013 and analyzed1976.

### S303

| S303 | DOC-002 pp.12-13 | Randomization: center-balanced website, take account of intermediate/high ARISCAT risk subgroups; permuted block length6, 1:1. Outcome assessor blinded; intervention/intraoperative collector unblinded. Match main center stratification and block6. |

**Numeric check: NUMERIC_COMPLETE.** Allocation1:1 and block6 consist3 per arm; actual1011/1002 need not exactly balance globally due incomplete blocks and stratification.

### S304

| S304 | DOC-002 pp.5,12,22,31 | Primary collapsed composite first5 postoperative days, ≥1 component qualifies; aspiration pneumonitis, bronchospasm, mild/moderate/severe respiratory failure, ARDS, pulmonary infection, atelectasis, cardiac pulmonary edema, pleural effusion, pneumothorax, new infiltrates. Match main primary outcome, all12 components. |

**Numeric check: NUMERIC_COMPLETE.** Primary list contains12 components; composite≥1 is union, not additive sum.

### S305

| S305 | DOC-002 pp.5,12 | Secondary item/status list: intraoperative complications (desaturation SpO2≤92% >1min; RM hypotension systolic<90mmHg >2min), postoperative invasive/noninvasive support, unexpected ICU admission/readmission30days, hospital readmission30days, hospital-free days90, mortality90, extrapulmonary complications, wound healing. Other parameters: systemic pulmonary inflammation, lung injury, distal-organ injury markers. Compare supplied updated SAP and reported secondary/exploratory status. |

**Numeric check: NUMERIC_COMPLETE.** Secondary status/time definitions retained; no outcome event count printed here.

### S306

| S306 | DOC-002 p.22 | Nonbinding group sequential gamma−4 alpha/beta; looks50/75/100%, N956/1434/1912. Tuples(info fraction,N,cumulative alpha,beta,Z efficacy,Z futility,H1 efficacy crossing,H1 futility crossing):(.5,956,.006,.024,≥2.75,<.225,.234,.024);(.75,1434,.018,.071,≥2.432,<.929,.296,.047);(1,1912,.05,.2,≥2.012,<2.012,.271,.129). Efficacy P≤.006/.015/.044; futility P>.82/.35/.044. Match reported alpha/interim decisions. |

**Numeric check: NUMERIC_COMPLETE.** Information fractions ×1912 yield956/1434/1912 exactly. Cumulative alpha .006,.018,.05 and beta .024,.071,.2 nondecreasing. H1 efficacy probabilities.234+.296+.271=.801≈80%; futility.024+.047+.129=.200. Inferential boundaries passed to statistical lanes.

### S307

| S307 | DOC-002 p.23 | Primary efficacy printed wording: “odds ratio relative risks” and “95% confidence levels interval” calculated using logistic regression; image confirms both phrases present without strikeout. Continuous normal:t-test, mean(SD); nonnormal:Mann-Whitney, median(IQR); categorical:χ²/Fisher or RR; time-dependent:proportional hazard adjusted for baseline imbalance. |

**Numeric check: NUMERIC_COMPLETE.** Source numerical definition/analysis specification retained; no printed event numerator, denominator or disjoint count partition applies. No numeric finding from this relationship; complete statistical/cross-source checking is separate.

### S308

| S308 | DOC-002 p.23 | A priori SAP before data collection end; only primary confirmatory, all other analyses exploratory; ITT; blinded statistical expert; significance P=.05;95% confidence; SPSS. Match updated SAP methods and reported analysis. |

**Numeric check: NUMERIC_COMPLETE.** Source numerical definition/analysis specification retained; no printed event numerator, denominator or disjoint count partition applies. No numeric finding from this relationship; complete statistical/cross-source checking is separate.

### S309

| S309 | DOC-003 pp.1-2 | Deleted old interim at50%,n374; early termination RR<.5 (high<20%,low40%) or RR>2(high>80%,low40%), DSMB decision, undisclosed except termination; v2.4.2 no interim. v2.5 adds revised interim rules mirrored in S306 and revised size mirrored in S302. |

**Numeric check: NUMERIC_COMPLETE.** Old interim374=.5×748; thresholds .20/.40=.5 and.80/.40=2 match stated ratios. Supplied version changes distinguish old/revised decisions.

### S310

| S310 | DOC-004 p.1 | SAP finalized20Jan2018, endorsed before last inclusion/database lock/statistical analysis. Primary five-day collapsed12-component PPC,at least1; secondary severePPC excludes mild respiratory failure,extrapulmonary complications,intraoperative events,unexpected ICU,wound healing,in-hospital mortality,hospital-free days90. Complete status list retained, including definitions. |

**Numeric check: NUMERIC_COMPLETE.** Source numerical definition/analysis specification retained; no printed event numerator, denominator or disjoint count partition applies. No numeric finding from this relationship; complete statistical/cross-source checking is separate.

### S311

| S311 | DOC-004 pp.1-2 | Missing-data rule:complete-case all outcomes; primary missing>1% triggers sensitivity multiple imputation+estimating-equation methods. Modified ITT excludes withdrawal-consent/canceled surgery losses; source data checks25%; locking after resolution/all efforts. Match reported analysis population/missing handling. |

**Numeric check: NUMERIC_COMPLETE.** 8/1984=.4032%, below primary missing-data sensitivity trigger1%; actual primary analyzed set1976 excludes losses. No percentage/count conflict.

### S312

| S312 | DOC-004 p.2 | Distributions histograms+D’Agostino-Pearson; baseline counts(%),mean(SD),median(IQR); two-sided5% except primary adjusted interim; no multiplicity adjustment generally; R2016. Ventilation/vitals compare after intubation,1h,last hour. |

**Numeric check: NUMERIC_COMPLETE.** Source numerical definition/analysis specification retained; no printed event numerator, denominator or disjoint count partition applies. No numeric finding from this relationship; complete statistical/cross-source checking is separate.

### S313

| S313 | DOC-004 p.2 | Primary RR+95%CI “Wald’s likelihood ratio approximation test”,χ² hypothesis,alpha.044; Kaplan-Meier time-to-PPC and log-rank. Match main primary analysis and eFigure8. |

**Numeric check: NUMERIC_COMPLETE.** Source numerical definition/analysis specification retained; no printed event numerator, denominator or disjoint count partition applies. No numeric finding from this relationship; complete statistical/cross-source checking is separate.

### S314

| S314 | DOC-004 p.2 | Binary secondary RR95%CI same Wald approximation andχ²; hospital-free days90 Student t mean difference; consistency mean ratio GAM zero-inflated beta. Match reported Table3+hospital-free days specification. |

**Numeric check: NUMERIC_COMPLETE.** Source numerical definition/analysis specification retained; no printed event numerator, denominator or disjoint count partition applies. No numeric finding from this relationship; complete statistical/cross-source checking is separate.

### S315

| S315 | DOC-004 pp.2-3 | Five prespecified subgroup dichotomies:nonlaparoscopic/laparoscopic;BMI<40/≥40;baselineSpO2<96/≥96;peripheral/upper abdominal (cranial umbilical incision);waist-to-hip<1/≥1. Interaction subgroup×arm in GLM,forest plot. Match main subgroup display. |

**Numeric check: NUMERIC_COMPLETE.** Five paired subgroup dichotomies match Figure2; each contributor denominator checked in S092–S101.

### S316

| S316 | DOC-004 p.3 | Sensitivity GLMM with center random effects; component count Mann-Whitney and proportional odds logistic OR95%CI. Match eTable9 random/count and main count. |

**Numeric check: NUMERIC_COMPLETE.** Source numerical definition/analysis specification retained; no printed event numerator, denominator or disjoint count partition applies. No numeric finding from this relationship; complete statistical/cross-source checking is separate.

### S317

| S317 | DOC-004 p.3 | Individual component GLM Bonferroni99.58%CI,1−.05/12=.9958; common-effect multivariate GEE OR; average relative effect averages component-specific distinct-effects GEE coefficients,test average0. Match eFigure12 and eTable9. |

**Numeric check: NUMERIC_COMPLETE.** 1−.05/12=.9958333, or99.5833%, agreeing99.58%. Twelve components counted.

### S318

| S318 | DOC-004 p.3 | Heterogeneity treatment×component distinct-effects GEE; a posteriori clinical severity weights with multivariate common-effect GEE OR. Both analyses explicitly planned; match eTable9/eFigure12 and narrative. |

**Numeric check: NUMERIC_COMPLETE.** Source numerical definition/analysis specification retained; no printed event numerator, denominator or disjoint count partition applies. No numeric finding from this relationship; complete statistical/cross-source checking is separate.

### S319

| S319 | p.22 eTable1 operational ARISCAT | Historical multivariate OR95%CI,beta,risk score for all predictors; risk score summed rounded coefficient×10;intermediate/high≥26. All15 row/reference tuples retained in transcript, source populationn1624. Matches PLAN Appendix i. |

**Numeric check: NUMERIC_COMPLETE.** Historical predictors and beta×10 rounded operational scores checked as defined; n1624 is separate historical multivariate sample, not trial denominator.

### S320

| S320 | p.24 eTable3 fluids | Total fluid mean(SD)1898(1401)/1882(1352),P.79; crystalloid count920(93.0)/928(94.0),P.37 andvolume1838(1306)/1841(1298),P.97; synthetic colloid74(7.5)/56(5.7),P.10,volume50(211)/35(171),P.09;HES45(4.6)/32(3.2),P.13,volume32(178)/21(139),P.15;gelatine31(3.1)/24(2.4),P.34,volume17(104)/13(102),P.38;dextran1(.1)/0(0),P.99,volume1(15.9)/0(0),P.32. VolumemL,continuousmeanSD; multiple fluid types not necessarily mutually exclusive. |

**Numeric check: NUMERIC_COMPLETE.** All reported agent/fluid count-percent entries checked, allowing overlapping recipients and available-case denominators; no qualifying numeric discrepancy.

920/989=93.0233%; half-unit [92.9257,93.1209]%; gap/printed=0.00000; 928/987=94.0223%; half-unit [93.9241,94.1206]%; gap/printed=0.00000

74/989=7.4823%; half-unit [7.4280,7.5367]%; gap/printed=0.00000; 56/987=5.6738%; half-unit [5.6203,5.7273]%; gap/printed=0.00000

45/989=4.5501%; half-unit [4.4972,4.6029]%; gap/printed=0.00000; 32/987=3.2421%; half-unit [3.1899,3.2945]%; gap/printed=0.00000

31/989=3.1345%; half-unit [3.0824,3.1866]%; gap/printed=0.00000; 24/987=2.4316%; half-unit [2.3797,2.4835]%; gap/printed=0.00000

1/989=0.1011%; half-unit [0.0505,0.1517]%; gap/printed=0.00000; 0/987=0.0000%; half-unit [0.0000,0.0507]%; gap/printed=0.00000

### S321

| S321 | p.25 eTable4 vasoactive/inotropic drugs | Need491(49.6)/439(44.5),P.02;dopamine0/2(.2),P1,mg0(0)/0(1.5),P.16;norepinephrine164(16.6)/154(15.6),P.55,mg.3(1.2)/.2(1.2),P.36;phenylephrine232(23.5)/190(19.3),P.02,mg.7(5.5)/.5(4.4),P.26;epinephrine14(1.4)/15(1.5),P.85,mg0(.7)/0(.7),P.37;dobutamine1(.1)/1(.1),P1,mg0(.9)/0(0),P.32. Allcountpercent anddose tuples retained. |

**Numeric check: NUMERIC_COMPLETE.** All reported agent/fluid count-percent entries checked, allowing overlapping recipients and available-case denominators; no qualifying numeric discrepancy.

491/989=49.6461%; half-unit [49.5705,49.7218]%; gap/printed=0.00000; 439/987=44.4782%; half-unit [44.4051,44.5514]%; gap/printed=0.00000

0/989=0.0000%; half-unit [0.0000,0.0506]%; gap/printed=0.00000; 2/987=0.2026%; half-unit [0.1519,0.2534]%; gap/printed=0.00000

164/989=16.5824%; half-unit [16.5235,16.6414]%; gap/printed=0.00000; 154/987=15.6028%; half-unit [15.5443,15.6614]%; gap/printed=0.00000

232/989=23.4580%; half-unit [23.3957,23.5205]%; gap/printed=0.00000; 190/987=19.2503%; half-unit [19.1899,19.3107]%; gap/printed=0.00000

14/989=1.4156%; half-unit [1.3643,1.4669]%; gap/printed=0.00000; 15/987=1.5198%; half-unit [1.4684,1.5712]%; gap/printed=0.00000

1/989=0.1011%; half-unit [0.0505,0.1517]%; gap/printed=0.00000; 1/987=0.1013%; half-unit [0.0506,0.1521]%; gap/printed=0.00000

### S322

| S322 | p.26 eTable5 anesthesia agents | Every agent row andP preserved in transcript;five sections volatile3,IV7,analgesic9,muscle paralyzing8,reversal2 =29 agent rows. n989/987,count(%),not exclusive classes. Match main anesthetic management/total IV/neuromuscular blocking agent observations. |

**Numeric check: NUMERIC_COMPLETE.** All reported agent/fluid count-percent entries checked, allowing overlapping recipients and available-case denominators; no qualifying numeric discrepancy.

469/989=47.4216%; half-unit [47.3471,47.4962]%; gap/printed=0.00000; 468/987=47.4164%; half-unit [47.3418,47.4911]%; gap/printed=0.00000

401/989=40.5460%; half-unit [40.4750,40.6171]%; gap/printed=0.00000; 411/987=41.6413%; half-unit [41.5696,41.7131]%; gap/printed=0.00000

40/989=4.0445%; half-unit [3.9919,4.0971]%; gap/printed=0.00000; 37/987=3.7487%; half-unit [3.6962,3.8013]%; gap/printed=0.00000

927/989=93.7310%; half-unit [93.6331,93.8290]%; gap/printed=0.00000; 911/987=92.2999%; half-unit [92.2025,92.3974]%; gap/printed=0.00000

278/989=28.1092%; half-unit [28.0445,28.1740]%; gap/printed=0.00000; 287/987=29.0780%; half-unit [29.0127,29.1434]%; gap/printed=0.00000

37/989=3.7412%; half-unit [3.6887,3.7936]%; gap/printed=0.00000; 40/987=4.0527%; half-unit [4.0000,4.1054]%; gap/printed=0.00000

144/989=14.5602%; half-unit [14.5023,14.6181]%; gap/printed=0.00000; 136/987=13.7791%; half-unit [13.7215,13.8368]%; gap/printed=0.00000

7/989=0.7078%; half-unit [0.6569,0.7587]%; gap/printed=0.00000; 7/987=0.7092%; half-unit [0.6582,0.7603]%; gap/printed=0.00000

78/989=7.8868%; half-unit [7.8322,7.9413]%; gap/printed=0.00000; 79/987=8.0041%; half-unit [7.9494,8.0588]%; gap/printed=0.00000

38/989=3.8423%; half-unit [3.7898,3.8948]%; gap/printed=0.00000; 31/987=3.1408%; half-unit [3.0886,3.1931]%; gap/printed=0.00000

160/989=16.1780%; half-unit [16.1193,16.2367]%; gap/printed=0.00000; 158/987=16.0081%; half-unit [15.9494,16.0669]%; gap/printed=0.00000

7/989=0.7078%; half-unit [0.6569,0.7587]%; gap/printed=0.00000; 8/987=0.8105%; half-unit [0.7595,0.8616]%; gap/printed=0.00000

539/989=54.4995%; half-unit [54.4214,54.5776]%; gap/printed=0.00000; 570/987=57.7508%; half-unit [57.6709,57.8307]%; gap/printed=0.00000

239/989=24.1658%; half-unit [24.1031,24.2286]%; gap/printed=0.00000; 208/987=21.0740%; half-unit [21.0127,21.1353]%; gap/printed=0.00000

331/989=33.4681%; half-unit [33.4007,33.5357]%; gap/printed=0.00000; 339/987=34.3465%; half-unit [34.2785,34.4146]%; gap/printed=0.00000

320/989=32.3559%; half-unit [32.2890,32.4229]%; gap/printed=0.00000; 313/987=31.7123%; half-unit [31.6456,31.7790]%; gap/printed=0.00000

2/989=0.2022%; half-unit [0.1516,0.2529]%; gap/printed=0.00000; 0/987=0.0000%; half-unit [0.0000,0.0507]%; gap/printed=0.00000

236/989=23.8625%; half-unit [23.7999,23.9251]%; gap/printed=0.00000; 239/987=24.2148%; half-unit [24.1519,24.2777]%; gap/printed=0.00000

308/989=31.1426%; half-unit [31.0763,31.2089]%; gap/printed=0.00000; 280/987=28.3688%; half-unit [28.3038,28.4339]%; gap/printed=0.00000

27/989=2.7300%; half-unit [2.6781,2.7820]%; gap/printed=0.00000; 24/987=2.4316%; half-unit [2.3797,2.4835]%; gap/printed=0.00000

66/989=6.6734%; half-unit [6.6195,6.7274]%; gap/printed=0.00000; 51/987=5.1672%; half-unit [5.1139,5.2205]%; gap/printed=0.00000

1/989=0.1011%; half-unit [0.0505,0.1517]%; gap/printed=0.00000; 2/987=0.2026%; half-unit [0.1519,0.2534]%; gap/printed=0.00000

5/989=0.5056%; half-unit [0.4548,0.5564]%; gap/printed=0.00000; 2/987=0.2026%; half-unit [0.1519,0.2534]%; gap/printed=0.00000

47/989=4.7523%; half-unit [4.6993,4.8053]%; gap/printed=0.00000; 48/987=4.8632%; half-unit [4.8101,4.9164]%; gap/printed=0.00000

847/989=85.6421%; half-unit [85.5483,85.7360]%; gap/printed=0.00000; 848/987=85.9169%; half-unit [85.8228,86.0112]%; gap/printed=0.00000

240/989=24.2669%; half-unit [24.2041,24.3298]%; gap/printed=0.00000; 234/987=23.7082%; half-unit [23.6456,23.7709]%; gap/printed=0.00000

4/989=0.4044%; half-unit [0.3537,0.4552]%; gap/printed=0.00000; 3/987=0.3040%; half-unit [0.2532,0.3548]%; gap/printed=0.00000

438/989=44.2872%; half-unit [44.2142,44.3601]%; gap/printed=0.00000; 434/987=43.9716%; half-unit [43.8987,44.0446]%; gap/printed=0.00000

290/989=29.3225%; half-unit [29.2572,29.3880]%; gap/printed=0.00000; 295/987=29.8886%; half-unit [29.8228,29.9544]%; gap/printed=0.00000

### S323

| S323 | p.27 eTable6 surgical characteristics | Priority elective962(97.8)/958(97.6),emergency13(1.3)/11(1.1),urgent9(.9)/13(1.3),globalP.64;position supine357(36.2)/367(37.2),Trendelenburg86(8.7)/69(7.0),reverse486(49.3)/491(49.8),lithotomy17(1.7)/16(1.6),seated39(4.0)/43(4.4),globalP.69;wound clean514(52.1)/525(53.2),clean-contaminated461(46.8)/450(45.6),contaminated10(1.0)/7(.7),dirty1(.1)/4(.4),globalP.46;abdominal pressure14.7(3.6)/14.5(2.1)mmHg,P.17. |

**Numeric check: NUMERIC_COMPLETE.** Priority category sums984/982; positioning985/986; wound986/986. Percentages reconstruct category-specific assessed totals and differ from header-based values by <0.05 relative. All category counts positive and ≤989/987. Multiple missingness subsets do not establish contradictory final population.

962/989=97.2700%; half-unit [97.1703,97.3698]%; gap/printed=0.00389; 958/987=97.0618%; half-unit [96.9620,97.1617]%; gap/printed=0.00398

13/989=1.3145%; half-unit [1.2633,1.3657]%; gap/printed=0.00000; 11/987=1.1145%; half-unit [1.0633,1.1657]%; gap/printed=0.00000

9/989=0.9100%; half-unit [0.8590,0.9611]%; gap/printed=0.00000; 13/987=1.3171%; half-unit [1.2658,1.3685]%; gap/printed=0.00000

357/989=36.0971%; half-unit [36.0283,36.1659]%; gap/printed=0.00000; 367/987=37.1834%; half-unit [37.1139,37.2529]%; gap/printed=0.00000

86/989=8.6957%; half-unit [8.6407,8.7506]%; gap/printed=0.00000; 69/987=6.9909%; half-unit [6.9367,7.0451]%; gap/printed=0.00000

486/989=49.1405%; half-unit [49.0652,49.2160]%; gap/printed=0.00069; 491/987=49.7467%; half-unit [49.6709,49.8226]%; gap/printed=0.00000

17/989=1.7189%; half-unit [1.6675,1.7704]%; gap/printed=0.00000; 16/987=1.6211%; half-unit [1.5696,1.6726]%; gap/printed=0.00000

39/989=3.9434%; half-unit [3.8909,3.9960]%; gap/printed=0.00000; 43/987=4.3566%; half-unit [4.3038,4.4095]%; gap/printed=0.00000

514/989=51.9717%; half-unit [51.8949,52.0486]%; gap/printed=0.00003; 525/987=53.1915%; half-unit [53.1139,53.2691]%; gap/printed=0.00000

461/989=46.6127%; half-unit [46.5387,46.6869]%; gap/printed=0.00135; 450/987=45.5927%; half-unit [45.5190,45.6665]%; gap/printed=0.00000

10/989=1.0111%; half-unit [0.9601,1.0622]%; gap/printed=0.00000; 7/987=0.7092%; half-unit [0.6582,0.7603]%; gap/printed=0.00000

1/989=0.1011%; half-unit [0.0505,0.1517]%; gap/printed=0.00000; 4/987=0.4053%; half-unit [0.3544,0.4562]%; gap/printed=0.00000

### S324

| S324 | p.28 dyspnea day1 | cm mean(SD),No:1.8(1.5),912/1.8(1.4),917;P.53 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S325

| S325 | p.28 dyspnea day2 | 1.4(1.0),840/1.5(1.0),844;P.57 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S326

| S326 | p.28 dyspnea day3 | 1.4(.9),619/1.3(.8),617;P.68 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S327

| S327 | p.28 dyspnea day4 | 1.3(.9),461/1.3(.8),459;P.79 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S328

| S328 | p.28 dyspnea day5 | 1.2(.9),336/1.2(.8),330;P.78 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S329

| S329 | p.28 thoracic day1 | 1.6(1.3),914/1.7(1.4),913;P.52 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S330

| S330 | p.28 thoracic day2 | 1.3(.8),838/1.4(3.9),841;P.34 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S331

| S331 | p.28 thoracic day3 | 1.2(.6),620/1.2(.6),617;P.94 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S332

| S332 | p.28 thoracic day4 | 1.1(.5),461/1.2(.5),459;P.20 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S333

| S333 | p.28 thoracic day5 | 1.1(.4),336/1.1(.5),330;P.16 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S334

| S334 | p.28 abdominal rest day1 | 2.7(1.8),950/2.9(1.9),958;P.10 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S335

| S335 | p.28 abdominal rest day2 | 2.1(1.5),881/2.1(1.4),889;P.31 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S336

| S336 | p.28 abdominal rest day3 | 1.8(1.3),647/1.8(1.2),650;P.94 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S337

| S337 | p.28 abdominal rest day4 | 1.6(1.2),469/1.6(1.0),475;P.75 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S338

| S338 | p.28 abdominal rest day5 | 1.5(1.0),346/1.5(1.0),337;P.83 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S339

| S339 | p.28 abdominal incident day1 | 3.7(2.4),916/3.7(2.3),929;P.52 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S340

| S340 | p.28 abdominal incident day2 | 2.8(2.0),837/2.9(1.9),857;P.51 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S341

| S341 | p.28 abdominal incident day3 | 2.4(1.7),615/2.4(1.7),627;P.55 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S342

| S342 | p.28 abdominal incident day4 | 2.0(1.5),458/2.1(1.5),459;P.69 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S343

| S343 | p.28 abdominal incident day5 | 1.9(1.4),339/1.9(1.5),333;P.58 |

**Numeric check: NUMERIC_COMPLETE.** Printed available-case contributor counts are positive, ≤989/987, and decline over days within each outcome. Distinct outcomes have distinct contributor subsets; neither full randomized denominators nor a cross-day sum is required. Mean within possible VAS0–10; SD positive. No numeric count discrepancy.

### S344

| S344 | p.29 PP collapsed primary PPC | 186/917(20.3)/209/912(22.9);effect .92(.82–1.04),P.17 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 186/917=20.2835%; half-unit [20.2180,20.3492]%; gap/printed=0.00000
- 209/912=22.9167%; half-unit [22.8493,22.9841]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S344 | p.29 PP collapsed primary PPC | 186/917; 209/912 | 0.92 | 0.88510 | [0.87965, 0.89058] | 0.02654 | 0.92374 | At most 0.05 |

### S345

| S345 | p.29 PP mild respiratory failure | 119/917(13.0)/140/912(15.4);.90(.78–1.04),P.15 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 119/917=12.9771%; half-unit [12.9155,13.0387]%; gap/printed=0.00000
- 140/912=15.3509%; half-unit [15.2877,15.4142]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S345 | p.29 PP mild respiratory failure | 119/917; 140/912 | 0.90 | 0.84537 | [0.83790, 0.85289] | 0.04679 | 0.90395 | At most 0.05 |

### S346

| S346 | p.29 PP moderate respiratory failure | 38/917(4.1)/51/912(5.6);.84(.66–1.07),P.15 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 38/917=4.1439%; half-unit [4.0872,4.2008]%; gap/printed=0.00000
- 51/912=5.5921%; half-unit [5.5342,5.6500]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S346 | p.29 PP moderate respiratory failure | 38/917; 51/912 | 0.84 | 0.74104 | [0.72339, 0.75905] | 0.09042 | 0.84519 | Above 0.05 |

### S347

| S347 | p.29 PP severe respiratory failure | 25/917(2.7)/35/912(3.8);.83(.61–1.11),P.18 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 25/917=2.7263%; half-unit [2.6703,2.7823]%; gap/printed=0.00000
- 35/912=3.8377%; half-unit [3.7808,3.8947]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S347 | p.29 PP severe respiratory failure | 25/917; 35/912 | 0.83 | 0.71039 | [0.68563, 0.73590] | 0.10734 | 0.82633 | Above 0.05 |

### S348

| S348 | p.29 PP ARDS | 3/917(.3)/1/912(.1);1.50(.84–2.64),P.62 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 3/917=0.3272%; half-unit [0.2725,0.3819]%; gap/printed=0.00000
- 1/912=0.1096%; half-unit [0.0548,0.1646]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S348 | p.29 PP ARDS | 3/917; 1/912 | 1.50 | 2.98364 | [1.65577, 6.96945] | 0.10051 | 1.49754 | Above 0.05 |

### S349

| S349 | p.29 PP bronchospasm | 11/917(1.2)/10/912(1.1);1.04(.69–1.57),P.84 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 11/917=1.1996%; half-unit [1.1444,1.2548]%; gap/printed=0.00000
- 10/912=1.0965%; half-unit [1.0411,1.1519]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S349 | p.29 PP bronchospasm | 11/917; 10/912 | 1.04 | 1.09400 | [0.99346, 1.20524] | 0.00000 | 1.04531 | At most 0.05 |

### S350

| S350 | p.29 PP infiltrates | 14/917(1.5)/14/912(1.5);.99(.68–1.44),P.99 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 14/917=1.5267%; half-unit [1.4714,1.5821]%; gap/printed=0.00000
- 14/912=1.5351%; half-unit [1.4795,1.5908]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S350 | p.29 PP infiltrates | 14/917; 14/912 | 0.99 | 0.99455 | [0.92495, 1.06939] | 0.00000 | 0.99723 | At most 0.05 |

### S351

| S351 | p.29 PP infection | 10/917(1.1)/9/912(1.0);1.05(.68–1.61),P.83 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 10/917=1.0905%; half-unit [1.0354,1.1457]%; gap/printed=0.00000
- 9/912=0.9868%; half-unit [0.9315,1.0422]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S351 | p.29 PP infection | 10/917; 9/912 | 1.05 | 1.10505 | [0.99346, 1.22990] | 0.00000 | 1.05031 | At most 0.05 |

### S352

| S352 | p.29 PP aspiration | 2/917(.2)/1/912(.1);1.33(.59–2.96),P1.00 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 2/917=0.2181%; half-unit [0.1635,0.2728]%; gap/printed=0.00000
- 1/912=0.1096%; half-unit [0.0548,0.1646]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S352 | p.29 PP aspiration | 2/917; 1/912 | 1.33 | 1.98909 | [0.99346, 4.97818] | 0.00000 | 1.33042 | At most 0.05 |

### S353

| S353 | p.29 PP pleural effusion | 38/917(4.1)/18/912(2.0);1.37(1.14–1.65),P.01 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 38/917=4.1439%; half-unit [4.0872,4.2008]%; gap/printed=0.00000
- 18/912=1.9737%; half-unit [1.9178,2.0296]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S353 | p.29 PP pleural effusion | 38/917; 18/912 | 1.37 | 2.09960 | [2.01377, 2.19040] | 0.46626 | 1.36872 | Above 0.05 |

### S354

| S354 | p.29 PP atelectasis | 38/917(4.1)/50/912(5.5);.85(.67–1.09),P.18 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 38/917=4.1439%; half-unit [4.0872,4.2008]%; gap/printed=0.00000
- 50/912=5.4825%; half-unit [5.4247,5.5403]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S354 | p.29 PP atelectasis | 38/917; 50/912 | 0.85 | 0.75586 | [0.73772, 0.77438] | 0.08308 | 0.85528 | Above 0.05 |

### S355

| S355 | p.29 PP cardiopulmonary edema | 15/917(1.6)/7/912(.8);1.36(1.02–1.82),P.09 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 15/917=1.6358%; half-unit [1.5804,1.6912]%; gap/printed=0.00000
- 7/912=0.7675%; half-unit [0.7123,0.8228]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S355 | p.29 PP cardiopulmonary edema | 15/917; 7/912 | 1.36 | 2.13117 | [1.92069, 2.37421] | 0.40860 | 1.36590 | Above 0.05 |

### S356

| S356 | p.29 PP pneumothorax | 1/917(.1)/2/912(.2);.66(.13–3.29),P.62 |

**Numeric check: NUMERIC_COMPLETE.** Both event count-percent pairs agree under half-unit intervals. Binary composite is a union, not sum. Printed effect identity investigated in F-NUM-001; diagnostic precision row below distinguishes qualifying gaps from corroborating occurrences.

- 1/917=0.1091%; half-unit [0.0545,0.1637]%; gap/printed=0.00000
- 2/912=0.2193%; half-unit [0.1644,0.2743]%; gap/printed=0.00000

Diagnostic table columns: ID, outcome, counts, printed effect, event-risk ratio, event-risk half-unit interval, relative gap, transposed-table ratio, precision category.

| S356 | p.29 PP pneumothorax | 1/917; 2/912 | 0.66 | 0.49727 | [0.19869, 0.99564] | 0.00000 | 0.66448 | At most 0.05 |

### S357

| S357 | p.30 center random-effect | OR.86(.68–1.08),P.19;95%CI/P mixed-effect center random. Match S316. |

**Numeric check: NUMERIC_COMPLETE.** Reported mixed-effect/proportional-odds/GEE effect measure distinguished from crude risks; no displayed counts permit recreating fitted OR. No numeric identity finding from assuming an unreported model.

### S358

| S358 | p.30 component count | OR.88(.72–1.09),P.25;95%CI proportional odds logistic;P Wilcoxon rank-sum. MeanSD/medianIQR mapped N319. Match S316 and eFigure12. |

**Numeric check: NUMERIC_COMPLETE.** Count mean totals353/989≈.35693,376/987≈.38095 reconcile under required half-unit input intervals; count 0 median/IQR compatible with incidence<50%.

### S359

| S359 | p.30 common-effect GEE | OR.93(.80–1.08),P.37;single treatment effect all12 components. Match S317 and eFigure12. |

**Numeric check: NUMERIC_COMPLETE.** Reported mixed-effect/proportional-odds/GEE effect measure distinguished from crude risks; no displayed counts permit recreating fitted OR. No numeric identity finding from assuming an unreported model.

### S360

| S360 | p.30 treatment×component GEE | No OR/CI printed;P.11,heterogeneity across12 components. Match S318. |

**Numeric check: NUMERIC_COMPLETE.** Reported mixed-effect/proportional-odds/GEE effect measure distinguished from crude risks; no displayed counts permit recreating fitted OR. No numeric identity finding from assuming an unreported model.

### S361

| S361 | p.30 average relative effect GEE | OR-labeled.99(.94–1.05),P.98;P model estimates then averages12 distinct treatment effects;CI confidence95%. Match S317 and eFigure12. |

**Numeric check: NUMERIC_COMPLETE.** Reported mixed-effect/proportional-odds/GEE effect measure distinguished from crude risks; no displayed counts permit recreating fitted OR. No numeric identity finding from assuming an unreported model.

### S362

| S362 | 31/eFigure1 | Sequential design drawing:enrollment956,1434,1912 excludes dropouts;Z vertical−4to4. Upper positive boundary harm,lower negative efficacy;central symmetric futility region. Boundary absoluteZ roughly2.75,2.432,2.012;futility absoluteZ roughly.225,.929,2.012;precise numerical companions are PLAN p.22 S306. Match primary enrollment/interim alpha. |

**Numeric check: NUMERIC_COMPLETE.** Sequential enrollment956/1434/1912 agrees exact planned information fractions and excludes dropouts; no trial analyzed-total conflict.

### S363

| S363 | 32/eFigure2 | Tidal volume mL/kgPBW;five times after intubation,1st,2nd,3rd,last hour. Open lowPEEP,dark highPEEP;mean and95%CI bars;mixed linear time×groupP=.081. Both groups near7.1–7.3 at all5 times;no precise coordinates printed. Match main ventilation variables and SAP repeated time comparisons. |

**Numeric check: NUMERIC_COMPLETE.** Five temporal means per arm and confidence bars mapped; direction/axis units agree with main physiological summaries. No printed contributor count or exact point coordinate is available; no precise invented scalar calculation.

### S364

| S364 | 33/eFigure3 | PEEP cmH2O,five same times;mean95%CI;mixed linear time×groupP<.001. Highnear11.5initial then12;lownear4throughout. Directions/reference openlow,darkhigh. |

**Numeric check: NUMERIC_COMPLETE.** Five temporal means per arm and confidence bars mapped; direction/axis units agree with main physiological summaries. No printed contributor count or exact point coordinate is available; no precise invented scalar calculation.

### S365

| S365 | 34/eFigure4 | Inspiratory peak pressure cmH2O read from anesthesia ventilator;five times;mean95%CI;mixed linear time×groupP<.001. Highroughly26initial and28later;lowroughly23initial and26–27later;no printed exactmeans. |

**Numeric check: NUMERIC_COMPLETE.** Five temporal means per arm and confidence bars mapped; direction/axis units agree with main physiological summaries. No printed contributor count or exact point coordinate is available; no precise invented scalar calculation.

### S366

| S366 | 35/eFigure5 | SpO2%,five times;mean95%CI;mixed linear time×groupP<.001. Highroughly98.0–98.3;lowroughly97.5initial,96.6at1h,96.9–97.1later. No precise point labels. |

**Numeric check: NUMERIC_COMPLETE.** Five temporal means per arm and confidence bars mapped; direction/axis units agree with main physiological summaries. No printed contributor count or exact point coordinate is available; no precise invented scalar calculation.

### S367

| S367 | 36/eFigure6 | Driving pressure cmH2O=plateau−PEEP;five times;mean95%CI;mixed linear time×groupP<.001. Highroughly11.3initial,12.2at1h/2h,12.1at3h,11.8last;lowroughly15.4initial,17.9at1h/2h,17.9at3h,17.4last. No exact point/bound numeric labels. |

**Numeric check: NUMERIC_COMPLETE.** Five temporal means per arm and confidence bars mapped; direction/axis units agree with main physiological summaries. No printed contributor count or exact point coordinate is available; no precise invented scalar calculation.

### S368

| S368 | 37/eFigure7 | FiO2%,five times;mean95%CI;mixed linear time×groupP<.001. Bothnear57–58initial;highnear45.5–46.3later;lownear48.5–50later. No printed exactmeans. |

**Numeric check: NUMERIC_COMPLETE.** Five temporal means per arm and confidence bars mapped; direction/axis units agree with main physiological summaries. No printed contributor count or exact point coordinate is available; no precise invented scalar calculation.

### S369

| S369 | 38/eFigure8 | First5days PPC,high21.3%,low23.6%,median follow-up4(IQR2–5)days;HRhigh/low.88(95%CI.73–1.06),P=.190;SchoenfeldP=.05. Figureannotation agrees caption HR/CI/P. Caption:median observation time not computed for incidence because maximum observed.23. Blue low higher/red high lower;axisproportion0–.25,days0–5. Match main primary counts/time-to-event. |

**Numeric check: NUMERIC_COMPLETE.** 21.3%/23.6% match211/989 and233/987; Cox HR is distinct from binary RR. At-risk table checked N320; no sum constraint between successive days.

### S370

| S370 | 39/eFigure9 | SeverePPC high11.7%,low13.6%;medianfollow-up4(2–5);HR.85(.66–1.09),P=.197;SchoenfeldP=.28;annotation same. Blue low higher/red high lower;axisproportion0–.15,days0–5. Match severe secondary and SAP S310. |

**Numeric check: NUMERIC_COMPLETE.** 11.7%/13.6% match116/989 and134/987; at-risk rows bounded and nonincreasing. Identical primary/severe risk sequences are a peripheral cross-time-point observation; missing endpoint censoring definitions prevent integer reconciliation.

### S371

| S371 | 40/eFigure10 | Extrapulmonary high16.9%,low15.2%;medianfollow-up4(2–5);HR1.12(.89–1.39),P=.314;SchoenfeldP=.67;annotation same. Blue low lower/red high higher;axisproportion0–.20,days0–5. Match extrapulmonary composite. |

**Numeric check: NUMERIC_COMPLETE.** 16.9%/15.2% match167/989 and150/987; at-risk rows bounded and nonincreasing; Cox HR distinct from event RR.

### S372

| S372 | 41/eFigure11 | Title/yaxis5-daydeath/mortality;caption calls rate “postoperative extra-pulmonary complications” while parenthetical specifies5-daymortality. High.5%,low.3%;medianfollow-up4(2–5);HR1.67(.40–6.97),P=.484;SchoenfeldP=.14. Annotation5dayHRsame;blue low belowred high;axisproportion0–.005,days0–5. All printed labeling retained without resolving a checker observation. |

**Numeric check: NUMERIC_COMPLETE.** .5%/.3% match5/989 and3/987; at-risk rows bounded and nonincreasing. Title, axis and exact HR identify5-day mortality despite caption phrase, a CONTEXT_RESOLVES wording observation.

### S373

| S373 | 42/eFigure12 mildRF | Printed Risk Ratio(99.58%CI):.92[.76,1.12]. High/low contrast,lower favorshigh,higherfavorslow. Match main component and SAP Bonferroni. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S374

| S374 | 42/moderateRF | RR.83[.59,1.17],99.58%CI. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S375

| S375 | 42/severeRF | RR.91[.61,1.34],99.58%CI. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S376

| S376 | 42/aspiration | RR1.33[.41,4.30],99.58%CI. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S377

| S377 | 42/bronchospasm | RR1.09[.62,1.91],99.58%CI. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S378

| S378 | 42/ARDS | RR1.50[.65,3.44],99.58%CI. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S379

| S379 | 42/pulmonary infection | RR1.00[.52,1.90],99.58%CI. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S380

| S380 | 42/atelectasis | RR.88[.64,1.23],99.58%CI. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S381

| S381 | 42/cardiopulmonary edema | RR1.31[.87,1.98],99.58%CI. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S382

| S382 | 42/pleural effusion | RR1.36[1.05,1.76],99.58%CI. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S383

| S383 | 42/pneumothorax | RR.50[.04,5.96],99.58%CI. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S384

| S384 | 42/pulmonary infiltrates | RR.87[.49,1.55],99.58%CI. |

**Numeric check: NUMERIC_COMPLETE.** Component figure risk-ratio values matched to same outcome in main Table3. Printed estimate is not renamed; effect-identity diagnostics and repeated pattern recorded F-NUM-001. No event count printed on this figure row.

### S385

| S385 | 42/global collapsed composite | Under printed “Odds Ratio (95%CI)” heading:.93[.83,1.04]. Match primary main risk estimate and S313,with both printed labels retained. |

**Numeric check: NUMERIC_COMPLETE.** Collapsed composite .93 matches primary printed RR but sits under an OR heading; same effect identity pattern as F-NUM-001, with source heading retained.

### S386

| S386 | 42/global count proportional odds | OR.88[.72,1.09],95%CI. Match eTable9 S358. |

**Numeric check: NUMERIC_COMPLETE.** Reported mixed-effect/proportional-odds/GEE effect measure distinguished from crude risks; no displayed counts permit recreating fitted OR. No numeric identity finding from assuming an unreported model.

### S387

| S387 | 42/global common effectGEE | OR.93[.80,1.08],95%CI. Match eTable9 S359. |

**Numeric check: NUMERIC_COMPLETE.** Reported mixed-effect/proportional-odds/GEE effect measure distinguished from crude risks; no displayed counts permit recreating fitted OR. No numeric identity finding from assuming an unreported model.

### S388

| S388 | 42/global average relative effectGEE | OR.99[.94,1.05],95%CI. Match eTable9 S361. |

**Numeric check: NUMERIC_COMPLETE.** Reported mixed-effect/proportional-odds/GEE effect measure distinguished from crude risks; no displayed counts permit recreating fitted OR. No numeric identity finding from assuming an unreported model.

