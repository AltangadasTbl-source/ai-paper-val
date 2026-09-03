# DOC-003 Complete Support Quantitative Evidence Map

## Scope, method, and source authority

- **Direct source:** `joi250042supp2_prod_1753377747.93025.pdf`, PDF pp. 1-29 (29/29 mapped).
- **Derivative use:** existing normalized text was used as a locator for pp. 2-27; retained OCR/rendering as a locator for pp. 8-27. Fresh direct-PDF native/layout extraction was used for pp. 1, 28, and 29. Every fact below was confirmed against the direct PDF; PDF p. 14 was additionally rendered and visually read because the forest-plot values are not represented in native extraction.
- **No-applicable units:** pp. 3-5 (consent/data-collection narrative; p. 3 contains the randomization deadline), p. 28-29 (references only). They contain no new result table/figure; their quantitative definitions/references are captured where relevant below.
- **Matching main-paper anchors:** direct-source main PDF reports 16,500 randomized; primary-analysis n=16,434 (8230 conservative, 8204 usual); enhanced-data n=2489 (1252, 1237); primary 90-d mortality 35.4% versus 34.9%, adjusted RD 0.7 percentage points (95% CI -0.7 to 2.0), P=.28; and oxygen exposure 20.3 versus 28.7 100%-equivalent hours, difference -8.4 (95% CI -10.8 to -6.0). These identities match the named DOC-003 relationships unless explicitly noted below.

## Definitions, populations, and analysis rules

### D3-N001 — Treatment-exposure measurement and adherence rule

**Direct source location:** DOC-003 PDF p. 2.

In enhanced-data patients, SpO2, FIO2, SaO2, and PaO2 are patient-median summaries (mean [SD], median [IQR], between-group mean difference with 95% CI), both overall and while receiving oxygen. Time is summarized for room air with SpO2 >92%, oxygen with SpO2 >92%, target SpO2 88-92%, and SpO2 <88%. Cumulative O2 dose is 100%-equivalent hours: room air=zero additional O2; 1 h at 100% O2 or 2 h at 60.5% O2=1 equivalent hour. Conservative-group potential deviation: FIO2 >0.21 plus SpO2 >92% with no FIO2 reduction for >=3 consecutive h, over the first 10 d or refusal, ICU discharge, or death, whichever first. Usual care has no adherence assessment.

### D3-N002 — Consent/data completeness and outcome availability definition

**Direct source location:** DOC-003 PDF pp. 3-5.

Eligible patients were randomized no later than 12 h after eligibility (p. 3). Patients declining/withdrawing but retaining data have only the primary survival status (alive/dead) at 90 d; secondary outcomes are unavailable (p. 5). Enhanced collection includes hourly SpO2, FIO2, and arterial blood gases (p. 5). This explains outcome-specific denominators; it is not itself a discrepancy.

### D3-N003 — Clinical outcome definitions

**Direct source location:** DOC-003 PDF pp. 6-7.

Primary outcome: all-cause death by 90 d after randomization. ICU/hospital deaths are censored at 90 d. Sixty-day and 1-y mortality use analogous time definitions; some did not reach 1-y and were excluded. ICU duration is linear time from randomization to first ICU discharge/death plus later ICU admissions in the same hospitalization; hospital duration is calendar days to hospital discharge/death. Days alive/free of organ support at 30 d is ordinal: death by day 30=-1; support means respiratory, cardiovascular, or renal support; surviving days are calendar days without support, day 1 through 30. Version-3.1 CMP records use the maximum of organ-support days, capped at 30.

## Figures

### D3-N004 — eFigure 1, recruitment diagram

**Direct source location:** DOC-003 PDF p. 8. **Status:** graphical content is not recoverable as text and carries no legible numeric result in the direct rendering available for this mapping; main-paper flow is the matching source for recruitment counts. No additional relationship registered.

### D3-N005 — eFigure 2, oxygen-measurement distributions

**Direct source location:** DOC-003 PDF p. 9.

Frequency distributions for SpO2, SaO2, PaO2, and FIO2 in enhanced-data patients, N=2489, split by usual versus conservative therapy. Axes: SpO2/SaO2 80-100%; PaO2 0-200 mm Hg; FIO2 0.21-1.00; y axes are percentage values/measurements (0-15%, 0-20%, and FIO2 0-50%). PaO2 conversion: multiply by 0.133 for kPa. This figure provides distributional context, not exact tabulated proportions.

### D3-N006 — eFigure 3, longitudinal enhanced-data denominators

**Direct source location:** DOC-003 PDF p. 10.

Mean SpO2, SaO2, PaO2 (overall and when receiving O2) over days 0,2,4,6,8,10; N=2489. Exact plotted ordinate values are graphical. Denominators (usual/conservative): SpO2 overall 1237/1252, 1011/1012, 801/777, 639/609, 501/499, 403/400; SpO2 with O2 1237/1252, 837/647, 637/493, 500/386, 378/313, 287/240; SaO2 overall 1037/1070, 900/918, 710/714, 568/558, 444/460, 361/371; SaO2 with O2 1037/1070,745/586,563/451,449/353,336/291,254/222; PaO2 overall 1156/1171,1009/1007,800/775,638/609,500/499,403/400; PaO2 with O2 1156/1171,836/645,636/493,499/386,377/313,287/240. PaO2 conversion multiply 0.133.

### D3-N007 — eFigure 4, separation over calendar time/within-site sequence

**Direct source location:** DOC-003 PDF p. 11.

Running-line smoother of mean (95% CI) patient-median FIO2 (axis 0.21-0.40) and SpO2 while receiving O2 (axis 90-98), by randomization date May 2021-May 2024 and patient sequence 1-500, N=2489. This supports maintained exposure separation but does not print pointwise values. It matches main-paper discussion of maintained separation.

### D3-S001 — eFigure 5, 1-y time-to-death analysis

**Direct source location:** DOC-003 PDF p. 12.

All-cause cumulative mortality through 360 d: hazard ratio 1.01 (95% CI 0.96-1.05), P=.82. At risk/events (conservative/usual): day 0 7067 (2523)/7178 (2509); day 90 4544 (137)/4669 (131); day 180 4126 (81)/4231 (86); day 270 3767 (59)/3855 (71); day 360 3371/3479. All randomized patients included for HR except 66 who requested all data removed (28/38). 342 (2.1%) known deaths <=90 d lack death date and are interval/left censored as specified. Plot includes linkage-consenting patients only. Reverse-KM median (IQR) follow-up: 365 d (277-365) conservative, 365 d (292-365) usual. Main-paper match: adjusted HR 1.01 (0.96-1.05).

### D3-N008 — eFigure 6, organ-support outcome distribution

**Direct source location:** DOC-003 PDF p. 13.

Distribution of days alive/free of organ support at 30 d: conservative n=7327 and usual n=7444. Death is -1; Panel A cumulative curves and Panel B stacked proportions. The caption defines curve height at day 20 as survivors with <=20 days free plus deaths. No printed numeric bin heights. Main-paper match: medians 16 (-1 to 25) in both and adjusted proportional OR 1.01 (0.96-1.07), P=.64.

### D3-S002 — eFigure 7, post-hoc subgroup 90-d mortality

**Direct source location:** DOC-003 PDF p. 14 (direct visual confirmation).

Adjusted multilevel logistic-regression ORs, adjusted for site, diagnostic subgroup, age, SpO2, PaO2/FIO2, confirmed/highly suspected COVID-19, and randomization date; interaction P tests are for OR.

| Subgroup / level | Conservative No./Total (%) | Usual No./Total (%) | RD % (95% CI) | OR (95% CI) | Interaction P |
|---|---:|---:|---:|---:|---:|
| Predicted-death-risk tertile: lowest | 244/2270 (10.7) | 218/2352 (9.3) | +1.5 (-0.1 to +3.2) | 1.19 (0.98-1.45) | .18 (set) |
| middle | 713/2307 (30.9) | 728/2317 (31.4) | -0.1 (-2.7 to +2.6) | 1.00 (0.88-1.13) | |
| highest | 1553/2297 (67.6) | 1532/2330 (65.8) | +1.8 (-0.9 to +4.6) | 1.09 (0.96-1.23) | |
| APACHE II: lowest tertile | 573/2834 (20.2) | 572/2915 (19.6) | +0.6 (-1.3 to +2.6) | 1.04 (0.91-1.20) | .98 (set) |
| middle | 794/2140 (37.1) | 784/2139 (36.7) | +1.3 (-1.5 to +4.0) | 1.06 (0.93-1.21) | |
| highest | 1306/2335 (55.9) | 1294/2368 (54.6) | +1.4 (-1.3 to +4.0) | 1.06 (0.94-1.20) | |
| PaO2/FIO2 <=100 | 521/1007 (51.7) | 496/1015 (48.9) | +3.0 (-1.0 to +7.1) | 1.15 (0.95-1.38) | .36 (set) |
| >100-<=200 | 1098/2806 (39.1) | 1115/2828 (39.4) | -0.0 (-2.4 to +2.4) | 1.00 (0.89-1.12) | |
| >200-<=300 | 688/2127 (32.3) | 700/2127 (32.9) | -0.5 (-3.1 to +2.2) | 0.98 (0.85-1.12) | |
| >300 | 601/2271 (26.5) | 547/2213 (24.7) | +1.8 (-0.6 to +4.2) | 1.11 (0.96-1.28) | |
| Data: standard | 2434/6959 (35.0) | 2409/6951 (34.7) | +0.6 (-0.8 to +2.1) | 1.03 (0.96-1.11) | .18 (set) |
| enhanced-random | 274/766 (35.8) | 290/767 (37.8) | -2.6 (-7.1 to +2.0) | 0.88 (0.70-1.10) | |
| enhanced-first 10 | 200/486 (41.2) | 159/465 (34.2) | +7.3 (+1.5 to +13.1) | 1.43 (1.08-1.90) | .03 |

## Tables

### D3-N009 — eTable 1, site-level randomization counts

**Direct source location:** DOC-003 PDF pp. 15-16. **Result:** 97 named sites; total 16,500, matching main-paper randomization total. Exact values are in the source rows, ranging from Sunderland Royal Hospital 863 through The Walton Centre 1; no subgroup estimate/statistic. Summing the stated site counts yields the printed total 16,500 (arithmetic check passed).

### D3-N010 — eTable 2, additional treatment-group characteristics

**Direct source location:** DOC-003 PDF p. 17. **Population:** 8230 conservative/8204 usual.

Age mean(SD) 58(16)/58(16); age categories 18-29 459(5.6)/420(5.1), 30-39 721(8.8)/766(9.3), 40-49 1070(13.0)/1106(13.5), 50-59 1790(21.7)/1729(21.1), 60-69 1910(23.2)/1937(23.6), 70-79 1790(21.7)/1700(20.7), >=80 490(6.0)/546(6.7). Admission-system counts / denominators: cardiovascular 1379/7286 (18.9)/1338/7405 (18.1); dermatological 136(1.9)/120(1.6); endocrine-metabolic-thermoregulation-poisoning 697(9.6)/729(9.8); gastrointestinal 1461(20.1)/1525(20.6); genitourinary 255(3.5)/272(3.7); hematological/immunological 57(0.8)/72(1.0); musculoskeletal 104(1.4)/105(1.4); neurological 830(11.4)/862(11.6); respiratory 2367(32.5)/2382(32.2). Prior stay mean(SD)[n] d 3.3(8.1)[7293]/3.3(7.7)[7419]; invasive ventilation h 5.3(3.5)[8230]/5.3(3.5)[8204]; SpO2% 96.0(3.5)/95.9(3.7); FIO2 0.51(0.21)/0.51(0.21); PaO2 mm Hg 104(48)[7638]/103(48)[7620]; ICNARCH risk median(IQR) 0.27(0.09-0.56)[6882]/0.26(0.09-0.55)[7014]; APACHE II mean(SD) 16.9(6.5)[7317]/16.9(6.7)[7437]. PaO2 conversion 0.133; APACHE range 0-71, higher=worse.

### D3-N011 — eTable 3, representativeness

**Direct source location:** DOC-003 PDF p. 18. Randomized n=16,500 versus potentially eligible CMP admissions n=207,857. Age median(IQR)[n] 60(48-71)[16434]/60(47-71)[207857]. Sex: female 5652/14805(38.2)/79268/207852(38.1); male 9153(61.8)/128584(61.9). Ethnicity Asian 506(3.4)/11192(5.4), Black 291(2.0)/6634(3.2), Mixed 112(0.8)/1873(0.9), White 12279(82.9)/161432(77.7), Other/not stated 1617(10.9)/26726(12.9), all first denominator 14805, second 207857. IMD quintiles 1-5: 1972(13.7),2502(17.4),2953(20.6),3114(21.7),3827(26.6) / 30956(15.3),35488(17.6),39385(19.5),44676(22.1),51338(25.4), denominators 14368/201843. BMI <18.5 523(3.6)/7071(3.5), 18.5-<25 4590(32.0)/70125(35.0),25-<30 4379(30.5)/63445(31.7),30-<40 3799(26.5)/47845(23.9),>=40 1045(7.3)/11907(5.9), denominators 14336/200393. Severe respiratory disease 343/14746(2.3)/4401/206153(2.1); pregnancy 98/4473(2.2)/2584/63653(4.1); ICNARCH mean(SD)[n] 0.34(0.29)[13896]/0.34(0.31)[206957]; APACHE median(IQR)[n] 16(12-21)[14754]/15(11-21)[200385].

### D3-N012 — eTable 4, data-collection strata

**Direct source location:** DOC-003 PDF pp. 19-20. Strata first-10 n=952; enhanced-random n=1537; standard n=13,945; sum=16,434 (main primary-analysis population). The direct source prints complete strata-specific demographics, diagnoses, SpO2/FIO2/PaO2 and severity values. Key reconciliation checks: age-group counts per stratum sum 952/1537/13945; diagnosis strata sum likewise; SpO2 categories sum 952/1537/13945; PaO2/FIO2 category counts sum to available 899/1428/12931. Exact values: first/random/standard: age median 60(47-71)/59(47-71)/60(48-71), mean 58(16) each; COVID 128(13.4)/82(5.3)/889(6.4); SpO2 median 96(94-99)/96(94-98)/97(94-99), mean 95.8(4.0)/95.9(3.4)/96.0(3.6); FIO2 median .50(.35-.70)/.45(.35-.65)/.45(.35-.60); PaO2 median 90(74-116)[899]/88(74-111)[1428]/89(75-116)[12931]; APACHE median 16(12-21)[890]/16(13-21)[1391]/16(12-21)[12473]. See direct source rows pp.19-20 for every printed category count and denominator.

### D3-N013 — eTable 5, pooled enhanced-data oxygen exposure

**Direct source location:** DOC-003 PDF p. 21. Conservative/usual n=1252/1237. Means(SD)[n], difference(95% CI): median FIO2 .31(.14)[1248]/.35(.15)[1230], -.04(-.05,-.03); with O2 .35(.13)[1225]/.37(.14)[1228], -.02(-.03,-.01). SpO2% 93.3(2.8)/95.1(2.4), -1.8(-2.0,-1.6); with O2 93.3(3.0)/95.2(2.6), -2.0(-2.2,-1.8). SaO2% 94.1(2.7)[1123]/95.5(2.7)[1091], -1.4(-1.6,-1.2); with O2 94.0(2.8)[1095]/95.6(2.9)[1086], -1.6(-1.8,-1.4). PaO2 mmHg 71.5(13.9)[1241]/79.5(17.9)[1227], -8.0(-9.3,-6.7); with O2 73.8(22.8)[1217]/81.4(19.3)[1225], -7.6(-9.3,-5.9). Hours room air + SpO2>92:39.7(55.1)[1234]/26.1(45.1)[1216],+13.6(9.6,17.6); oxygen + SpO2>92:41.4(45.6)/95.4(72.9),-54.0(-58.8,-49.2); SpO2 88-92:62.6(62.3)/27.2(39.1),+35.5(31.4,39.6); SpO2<88:3.2(6.5)/2.3(7.3),+.9(.4,1.4); total equivalent O2 h 20.3(27.4)/28.7(31.9),-8.4(-10.8,-6.0), percentage difference -29.3(-37.6,-20.9). Medians(IQR) are printed on p.21 and consistent in direction. Exact main-paper match for FIO2 and total O2 exposure.

### D3-N014 — eTable 6, oxygen exposure by enhanced-data stratum

**Direct source location:** DOC-003 PDF pp. 22-23. First-10 conservative/usual 486/466; random-sample 766/771. Each row gives conservative-minus-usual mean difference (95% CI). First/random: SpO2 -2.1(-2.5,-1.7)/-1.6(-1.9,-1.3); SpO2 with O2 -2.3(-2.7,-1.9)/-1.7(-2.0,-1.4); FIO2 -.04(-.06,-.02)/-.05(-.06,-.04); FIO2 with O2 -.02(-.04,-.00)/-.03(-.04,-.02); SaO2 -1.6(-2.0,-1.2)/-1.3(-1.6,-1.0); SaO2 with O2 -1.7(-2.1,-1.3)/-1.6(-1.9,-1.3); PaO2 -8.7(-10.8,-6.6)/-7.5(-9.1,-5.9); PaO2 with O2 -8.3(-11.1,-5.5)/-7.2(-9.3,-5.1); room-air/SpO2>92 h +11.4(4.9,17.9)/+15.1(10.0,20.2); oxygen/SpO2>92 h -59.8(-67.8,-51.8)/-50.4(-56.4,-44.4); SpO2 88-92 h +37.7(30.6,44.8)/+34.0(29.0,39.0); SpO2<88 h +1.1(.2,2.0)/+.8(.1,1.5); total O2 h -9.2(-13.4,-5.0)/-7.9(-10.7,-5.1), percentage -29.5(-42.9,-16.0)/-29.0(-39.3,-18.8). Group means/SD/n and medians/IQR are printed in full on pp.22-23; all differences are directionally concordant with D3-N013.

### D3-S003 — eTable 7, missing-data / imputation rules

**Direct source location:** DOC-003 PDF p. 24. Baseline missing: allocated treatment, age, diagnosis, COVID, SpO2, randomization date 0(0.0); PaO2/FIO2 1176(7.2), singly imputed using SpO2/FIO2 (Brown 2016); ethnic group 1630(9.9), no imputation except complete-case ethnic subgroup. Primary 90-d mortality missing 40(0.2), logit, auxiliary hospital-stay duration. Secondary: ICU stay 1653(10.1), censored; hospital stay 1677(10.2), censored; organ-support outcome 1639(10.0), ordered logit, auxiliary 90-d and ICU-discharge mortality; ICU mortality 1647(10.0), logit; hospital mortality 1641(10.0), logit plus hospital stay; 60-d mortality 1412(8.6), logit plus 90-d/1-y; 1-y 1661(12.7), logit, n reached 1-y=13052. Censoring is 1 h ICU /1 d hospital after randomization. Main paper matches 40/16,434 (0.2%) primary missing and n=13,052 reached one year.

### D3-N015 — eTable 8, continuous secondary-outcome summaries

**Direct source location:** DOC-003 PDF p. 25. Conservative/usual: ICU stay mean(SD)[n] overall 11.0(13.0)[7333]/11.4(13.8)[7448], survivors 12.3(14.1)[5211]/12.8(14.9)[5290], nonsurvivors 7.8(9.3)[2122]/7.8(9.9)[2158]; hospital 22.9(23.1)[7323]/23.1(23.3)[7434], survivors 29.1(24.9)[4791]/29.5(25.0)[4906], nonsurvivors 11.3(12.7)[2532]/10.9(12.9)[2528]. DAWOS 12.9(12.2)[7327]/12.8(12.1)[7444]; among survivors 19.6(9.1)[4933]/19.3(9.1)[5054]. Respiratory-free median 25(18-27)/24(17-27), mean20.9(9.1)/20.5(9.1); cardiovascular median23(16-27)/23(16-26),mean20.1(8.6)/19.8(8.8); renal median30(30-30)/30(30-30),mean28.7(4.3)/28.5(4.7), all survivor n=4933/5054. Counts reconcile (ICU survivor+nonsurvivor=overall; hospital likewise).

### D3-N016 — eTable 9, serious adverse events

**Direct source location:** DOC-003 PDF p. 26. Population 8230/8204. Any SAE patients 58(0.7)/29(0.4); event count intentionally blank at aggregate level. Specified event counts and patients: sinus 2;2(<.1)/1;1(<.1), supraventricular 12;12(.1)/8;8(.1), AF 16;14(.2)/15;13(.2), MI 19;19(.2)/11;11(.1), mesenteric 7;7(.1)/0;0. Other: bradycardia, bradycardic/asystole, cardiac arrest, cardiovascular instability, brain ischemic CT, multiple cerebral infarcts, respiratory arrest, severe hypoxemia each 1;1(<.1)/0;0; pneumothorax 0;0/2;1(<.1). Period randomization to ICU discharge or 90 d, whichever first. Main-paper match: 58 versus 29 patients.

### D3-N017 — eTable 10, achieved oxygenation across trials

**Direct source location:** DOC-003 PDF p. 27. UK-ROX is 2025; recruitment 05/2021-11/2024; 16,434 with data and mechanically ventilated; SpO2 mode; lower target 90%(88-92), PaO2 about60; higher usual care. Achieved lower/higher: SpO2 93.3/95.2 (difference 2%); PaO2 71.5/79.5 (8.0); FIO2 .31/.35 (.04). Values match eTable5. Cross-trial columns are contextual; footnote says reporting methods differ (median/mean/time-weighted) and values may be estimated, so they are not same-analysis comparators.

## Candidate observations for coordinator (not adjudications)

### D3-C01 — Contents-page eTable identities conflict with the actual eTable pages

**Exact direct-source locations:** DOC-003 PDF p.1 contents versus p.15 `eTable 1. Patients randomized by site`, p.17 `eTable 2. Additional patient characteristics`, p.18 `eTable 3. Representativeness of patients recruited to the UK-ROX trial`, and p.19 `eTable 4. Patient baseline characteristics by data collection group`.

**Direct observation:** p.1 instead labels eTable 1 `Results of quality assessment per study`, eTable 2 `Diagnostic performance of serological tests – test combinations`, eTable 3 `Patients randomized by site`, and eTable 4 `Additional patient characteristics`. The p.1 titles for eTables 1-4 therefore do not identify the same numbered tables printed on pp.15-19; p.1's eTable3/4 descriptions correspond in topic to actual eTable1/2 but have wrong table numbers. eTables 5-10 on p.1 correctly match their printed table numbers/titles.

**Reproducible rule:** a contents entry’s stated eTable number and title should identify the same numbered eTable in the same supplied PDF. **Human question:** whether p.1 is an uncorrected contents/template list. **Category if registered:** Measure, label, or scale inconsistency (document navigation/label identity); Pending Human Adjudication. This is one identity-rule observation, not four separately merged candidates.

## Mapping completeness / limitations

- All 29 PDF pages were read against the direct PDF; reusable evidence was only a locator. No source/reused asset was changed.
- Raster figures provide axes and/or plotted marks where text extraction does not preserve values; page 14 was visually confirmed. Pointwise values in eFigures 2-4 and bin heights in eFigure6 are not printed in the PDF and should not be digitized as exact values.
- No display-zero P-value observation was registered: none in this source created a display-zero candidate.
