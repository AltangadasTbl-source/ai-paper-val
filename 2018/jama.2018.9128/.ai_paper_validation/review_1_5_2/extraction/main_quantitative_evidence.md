# Main quantitative evidence map — DOC-001

**Scope:** `jama_barkin_2018_oi_180075.pdf`, PDF pp. 1-11 (printed pp. 450-460).  Fresh direct PDF/layout evidence and the corresponding fresh rendered pages were used.  This is an evidence map, not a candidate list or adjudication.

**Conventions:** `MN` records map numeric/reporting relationships; `MS` records map inferential-statistical relationships. `Match key` identifies repeated representations for later cross-source comparison. Values are printed values; any calculation is expressly labelled derived. BMI is kg/m² unless stated otherwise.

## Page coverage register

| PDF page | Printed page | Result-relevant content mapped | Status |
|---|---:|---|---|
| 1 | 450 | Abstract: trial population, intervention/control allocation, baseline/retention summaries, primary and significant secondary results | COMPLETE |
| 2 | 451 | Design/setting/eligibility, randomization/intervention time structure; reference to Supplement 1 protocol/SAP | COMPLETE |
| 3 | 452 | CONSORT flow; primary/secondary outcome definitions | COMPLETE |
| 4 | 453 | Measurement schedule, sample-size target, primary and secondary analysis definitions, cohort summary | COMPLETE |
| 5 | 454 | Table 1, baseline participant characteristics (first portion) | COMPLETE |
| 6 | 455 | Table 1 continuation; primary-outcome results and secondary-outcome narrative | COMPLETE |
| 7 | 456 | Secondary/post-hoc/adherence narrative; Figures 2-3 | COMPLETE |
| 8 | 457 | Table 2 secondary outcomes and footnotes; adverse-event count | COMPLETE |
| 9 | 458 | Table 3 post-hoc obesity outcomes and footnotes; matching discussion claims | COMPLETE |
| 10 | 459 | Discussion/conclusion claims; no new numerical results beyond references/funding identifiers | COMPLETE |
| 11 | 460 | References only; no applicable article-result relationship | COMPLETE |

## Trial, population, definitions, and flow

| ID | Exact location and printed evidence | Population/time/contrast/model/scale/direction | Applicable rule and match key |
|---|---|---|---|
| MN001 | p1 abstract: 610 parent-child pairs; enrollment Aug 2012-May 2014; 36-mo follow-up Oct 2015-Jun 2017; p2: 54 physicians' offices/community settings, Nashville; child age 3-5 y | Randomized parent-child pairs; trial frame | Identity/setting key `TRIAL_FRAME` |
| MN002 | p1 abstract: intervention n=304, 12 weekly skills sessions + monthly coaching for 9 mo + 24-mo sustainability; control n=306, 6 school-readiness sessions over 36 mo | Intervention vs control; 36-mo program | Allocation/denominator key `ALLOC_304_306` |
| MN003 | p2: eligible BMI >=50th and <95th percentile; p3: BMI = kg/m²; p3: primary BMI trajectory over 36 mo; 7 prespecified secondary outcomes and one post-hoc obesity outcome listed | Child eligibility/outcome definitions | Measure/threshold key `BMI_DEFINITION_OUTCOMES` |
| MN004 | p2: randomization stratified by community center and parent language; permuted blocks 2-6 | Individual randomized pairs | Randomization-label key `RANDOMIZATION` |
| MN005 | p3 Figure 1: 2126 assessed; 1516 excluded = 612 did not meet inclusion +486 unable schedule/contact +418 declined; 610 randomized | Screening flow | Derived: 612+486+418=1516; 2126-1516=610. Key `CONSORT_SCREEN` |
| MN006 | p3 Figure 1: intervention 304 randomized, 301 received, 3 did not receive (dropped immediately); control 306 randomized/306 received | Allocated groups | Derived: 301+3=304. Key `CONSORT_ALLOCATION` |
| MN007 | p3 Figure 1 intervention BMI measured/missing/cumulative loss: 3 mo 288/9/7; 9 mo 282/13/9; 12 mo 275/18/11; 24 mo 280/6/18; 36 mo retained 278/missing 26 | Intervention arm follow-up; missing may be later measure versus permanent loss per caption | At each time, measured+missing+cumulative loss=304 (derived); key `CONSORT_I_FOLLOWUP` |
| MN008 | p3 Figure 1 control BMI measured/missing/cumulative loss: 3 mo 277/25/4; 9 mo 282/13/11; 12 mo 276/15/15; 24 mo 267/18/21; 36 mo retained 272/missing 34 | Control arm follow-up | At each time, measured+missing+cumulative loss=306 (derived); key `CONSORT_C_FOLLOWUP` |
| MN009 | p3 Figure 1: all randomized included in primary analysis: intervention 304, control 306; intention-to-treat regardless of missing data | Primary-analysis population | Identity to `ALLOC_304_306`; key `PRIMARY_ITT` |
| MN010 | p4: data at baseline and 3, 9, 12, 24, 36 mo; height nearest 0.1 cm and weight nearest 0.1 kg; annual accelerometer 24 h/d for 7 consecutive days; diet recall 2 weekdays +1 weekend day | Measurement schedule and units | Timing/measurement key `DATA_SCHEDULE` |
| MN011 | p4: power analysis: two-tailed alpha=.05, 90% power, standardized effect size 0.4, final n=480 required; 600 planned with 80% anticipated retention | Planning, not observed effect | Planning-statistics key `SAMPLE_SIZE_PLAN` |
| MN012 | p4 Results: 36-mo retention 91.4% intervention and 88.9% control; baseline child mean(SD) age 4.3(0.9), 51.9% female, 91.4% Hispanic/Latino, 65.7% BMI 50th-85th and 34.3% 85th-95th; US-born children 96.4%; adult Mexico 63.6%, El Salvador 9.4%, Honduras 6.6%, Guatemala 6.1%; WIC/SNAP 87.5%, food insecurity 42.6% | Overall randomized cohort baseline summary | Match keys `RETENTION_36M`, `BASELINE_COHORT` |
| MN013 | p6 Table 1 footnotes: all randomized included; BMI-category denominators n=302/301 and 2 below 50th, 5 >=95th excluded from categories but ITT analyses; waist summary total 568 nonpregnant, 42 not measured due to pregnancy; Hispanic acculturation eligible n=556 (278/278), score 4-20; CES-D 20 questions, range 0-60, high >=16; food security score 0-6 (0-1/2-4/5-6); center-use original 6-point scale dichotomized never/at least once | Definitions/missingness applicable to Table 1 | Denominator/scale key `T1_FOOTNOTES` |

## Baseline Table 1 (pp. 5-6)

| ID | Exact printed values | Population/time/scale | Rule and match key |
|---|---|---|---|
| MN014 | p5 child sex: female 154/304 (50.7%) intervention; 162/306 (52.9%) control | Baseline children | Count/percent key `T1_CHILD_SEX` |
| MN015 | p5 child age 4.3(0.9) y vs 4.3(0.9); BMI 16.7(0.8) vs 16.6(0.8); BMI z 0.83(0.48) vs 0.82(0.46) | Baseline children I vs C; mean(SD) | Measure/scale key `T1_CHILD_ANTHRO` |
| MN016 | p5 BMI categories: I n=302, 50-84.9:193(63.9), 85-94.9:109(36.1); C n=301, 203(67.4),98(32.6) | Baseline children; percentile categories | Each arm categories sum to stated n (derived); `T1_BMI_CATEGORY` |
| MN017 | p5 waist cm: 53.0(3.4), n=303 vs 53.1(3.0), n=305; triceps mm:9.5(2.7),n=300 vs9.7(2.3),n=304 | Baseline children | Units/missingness key `T1_CHILD_WAIST_SKIN` |
| MN018 | p5 physical activity: n=302 each; wear-time median(Q1,Q3) 1077(954,1122) vs1070(959,1121) min; rest/sedentary 638.1(120.2) vs634.3(119.9); light 288.4(59.4) vs290.1(56.6); MVPA 84.1(30.3) vs86.0(31.4) | Baseline daily minutes | Activity-category/unit key `T1_PA` |
| MN019 | p5 diet: I n=304, C n=305; energy kcal 1184(334) vs1202(429); fat %28.5(5.2) vs28.2(5.3); carbohydrates %55.4(6.1) vs56.1(6.6); protein %16.1(3.2) vs15.7(3.3) | Baseline daily diet | Percentage-scale key `T1_DIET` |
| MN020 | p5 child race, I n=303/C n=304: Hispanic Mexican 187(61.7)/202(66.5); Hispanic non-Mexican 92(30.4)/74(24.3); non-Hispanic Black 19(6.3)/17(5.6); White 2(0.7)/4(1.3); other 3(1.0)/7(2.3) | Baseline children | Categories sum to arm n (derived); `T1_CHILD_RACE` |
| MN021 | p5 adult sex/age/BMI: female 300(98.7)/300(98.0); age 32.5(6.2)/31.6(5.8) y; BMI 29.8(6.2)/29.4(5.3) | Baseline adult participants | `T1_ADULT_SEX_ANTHRO` |
| MN022 | p5 adult waist 97.7(13.4),n=285 vs96.7(11.9),n=283 cm; triceps 31.5(9.2) vs31.3(8.7) mm | Baseline adults | Units/missingness; `T1_ADULT_WAIST_SKIN` |
| MN023 | p5 adult race: Mexican 183(60.2)/204(66.7); Hispanic non-Mexican95(31.3)/74(24.1); Black19(6.3)/20(6.5); White4(1.3)/5(1.6); other3(1.0)/3(1.0) | I n=304/C n=306 inferred from table heading | Categories sum to arm n (derived); `T1_ADULT_RACE` |
| MN024 | p5 time in US median(Q1,Q3) 10.0(8.0,14.0),n=303 vs10.0(7.0,13.0),n=306 y; acculturation 4.0(4.0,7.0),n=274 vs4.0(4.0,6.0),n=272 | Baseline adults; acculturation range 4-20 | `T1_US_ACCULTURATION` |
| MN025 | p5 employment I n=303/C n=306: full-time51(16.8)/57(18.6), part-time52(17.2)/67(21.9), not working200(66.0)/182(59.5) | Baseline adults | Categories sum to n (derived); `T1_EMPLOYMENT` |
| MN026 | p5 marital I n=303/C n=305: married/living as married260(85.8)/244(80.0), single43(14.2)/61(20.0) | Baseline adults | Categories sum to n (derived); `T1_MARITAL` |
| MN027 | p5 relationship I n=303/C n=306: mother293(96.7)/296(96.7), father3(1.0)/6(2.0), other7(2.3)/4(1.3) | Baseline adult-child relationship | Categories sum to n (derived); `T1_RELATIONSHIP` |
| MN028 | p6 WIC/SNAP:257(85.1),n=302 vs273(89.8),n=304 | Baseline households | Count/percent key `T1_WIC_SNAP` |
| MN029 | p6 income: <=$14,999 85(28.0)/89(29.1); $15,000-24,999 90(29.6)/82(26.8); $25,000-34,999 39(12.8)/37(12.1); $35,000-49,999 7(2.3)/9(2.9); >=$50,000 2(0.7)/2(0.7); don't know/no answer81(26.6)/87(28.4) | I/C denominators 304/306 | Categories sum to arm n (derived); `T1_INCOME` |
| MN030 | p6 education: <HS182(59.9)/192(62.7); >=HS122(40.1)/114(37.3) | I/C denominators 304/306 | Categories sum to arm n; `T1_EDUCATION` |
| MN031 | p6 CES-D high>=16:71(23.4),n=303 vs59(19.3),n=306 | Baseline adults; 0-60 scale | `T1_CESD` |
| MN032 | p6 food security I n=302/C n=304: secure165(54.6)/183(60.2); insecure no hunger86(28.5)/87(28.6); insecure hunger51(16.9)/34(11.2) | Baseline households; score bands supplied in N013 | Categories sum n; `T1_FOOD_SECURITY` |
| MN033 | p6 center use I n=303/C n=305: never216(71.3)/211(69.2); at least once87(28.7)/94(30.8) | Baseline parent report; dichotomized scale | Categories sum n; baseline key `CENTER_USE_BASELINE` |

## Primary outcome and figures

| ID | Exact location and printed evidence | Population/time/contrast/model/scale/direction | Rule and match key |
|---|---|---|---|
| MN034 | p6: at 36 mo child BMI mean(SD) 17.8(2.2) intervention and17.8(2.1) control; p1 abstract repeats 17.8(2.2)/17.8(2.1); p2 Key Points repeats means 17.8 both groups | Observed BMI, 36 mo, I vs C | Cross-location match `BMI36_MEANS` |
| MS001 | p6: adjusted BMI difference at 36 mo B=0.05, 95%CI -0.29 to0.38, P=.79 | ITT mixed-effects analysis, I-C BMI at 36 mo | CI contains 0; `BMI36_ADJ` |
| MS002 | p6 and p7 Figure 3: linear intervention effect (BMI difference/year) B=-0.082, 95%CI -0.246 to0.082, P=.33 | Model-estimated I-C linear trajectory coefficient, BMI/year | CI contains 0; match `BMI_LINEAR` |
| MS003 | p6 and p7 Figure 3: quadratic intervention effect (BMI difference/year²) B=0.032, 95%CI -0.014 to0.078, P=.18 | Model-estimated I-C quadratic trajectory coefficient, BMI/year² | CI contains 0; match `BMI_QUADRATIC` |
| MS004 | p1 abstract, p6, p7 Figure 3: joint likelihood-ratio test P=.39; p4 says linear/quadratic effects jointly zero, df=2, .05 level | Prespecified primary outcome, 36-mo trajectory | `BMI_JOINT_LRT`; narrative says no significant effect |
| MS005 | p4: 2-level time-within-child mixed-effects regression; maximum likelihood, unstructured covariance, missing at random; age baseline and condition covariates for intercept/linear/quadratic, sex intercept only; quadratic selected a priori; time continuous years since baseline | Primary-model labels/definitions | Model-definition key `BMI_PRIMARY_MODEL` |
| MN035 | p7 Figure 2 total observed BMI: I 298 baseline,279 3mo,280 9mo,274 12mo,278 24mo,276 36mo; C302,271,280,275,266,272 | Figure boxplot observations; differs in described quantity from CONSORT BMI-measured values | Do not equate without definition; `FIG2_OBS_N` |
| MN036 | p7 Figure 2 y-axis labels 10,15,20,25,30 BMI and x-axis 0,3,9,12,24,36 mo; caption defines median, IQR, 1.5*IQR whiskers, outlier dots | Observed BMI plot; scale/summary definition | Figure-scale key `FIG2_SCALE` |
| MN037 | p7 Figure 3: panels x-axis 0,12,24,36 mo; panel A fitted mean BMI y-axis 16-18; panel B I-C fitted difference y-axis -0.4 to0.4 and zero=no difference; shaded 95%CIs; A n=304/306 | Model-estimated trajectories/difference plot | Graphical scale and direction key `FIG3_SCALE` |

## Secondary outcomes (Table 2, p. 8; narrative pp. 1, 6-7)

| ID | Exact printed values | Population/time/contrast/model/scale | Rule and match key |
|---|---|---|---|
| MS006 | Energy 12mo: data I227(74.7), mean1157(306); C225(73.5),1261(351); adjusted difference -88.5, CI -142.1 to-34.9, P=.001, corrected .003 | kcal/day; I-C; OLS adjusted baseline outcome, age, sex | CI excludes 0; `ENERGY_12` |
| MS007 | Energy 24mo: I229(75.3),1212(380); C209(68.3),1296(372); diff -82.8, CI -144.6 to-21.1, P=.009, corrected .009 | kcal/day | `ENERGY_24` |
| MS008 | Energy 36mo: I227(74.7),1227(363); C219(71.6),1323(397); diff -99.4, CI -160.7 to-38.0, P=.002, corrected .003; p1 abstract says adjusted -99.4 [CI -160.7,-38.0], corrected .003; p6 narrative calls 99.4 fewer, CI 38.0-160.7, P=.002/corrected .003 | kcal/day, I-C; signed table/abstract versus magnitude prose | Cross-source `ENERGY_36` |
| MS009 | Fat % 12/24/36mo: I n/mean 227(74.7)/28.2(5.0),229(75.3)/27.8(5.5),227(74.7)/28.6(5.1); C225(73.5)/28.5(4.7),209(68.3)/28.4(4.8),219(71.6)/28.9(5.2); differences -0.3[-1.2,0.5], -0.6[-1.6,0.3], -0.4[-1.4,0.5]; P .45,.20,.36; corrected .45,.45,.45 | Percentage energy; I-C | All CIs contain 0; `FAT_12_24_36` |
| MS010 | Carbohydrate % 12/24/36: I 227(74.7)/55.1(5.9),229(75.3)/54.9(6.3),227(74.7)/54.2(6.0); C225(73.5)/55.2(5.8),209(68.3)/55.5(5.6),219(71.6)/54.7(5.8); differences 0.1[-0.9,1.2],-0.4[-1.5,0.7],-0.3[-1.4,0.7]; P .83,.45,.53; corrected .83,.80,.80 | Percentage energy; I-C | All CIs contain 0; `CARB_12_24_36` |
| MS011 | Protein % 12/24/36: I227(74.7)/16.7(3.1),229(75.3)/17.3(3.3),227(74.7)/17.2(3.3); C225(73.5)/16.3(3.2),209(68.3)/16.1(3.1),219(71.6)/16.4(3.0); differences0.2[-0.3,0.8],1.0[0.4,1.5],0.7[0.2,1.3]; P .46,.001,.01; corrected .46,.003,.02 | Percentage energy; I-C | `PROTEIN_12_24_36`; p6 prose says greater at 24/36 |
| MS012 | Sedentary min 12/24/36: I230(75.7)/619.9(130.0),252(82.9)/635.5(121.7),248(81.6)/663.6(117.5); C232(75.8)/618.5(131.9),222(72.5)/646.8(124.6),234(76.5)/660.0(120.5); diffs -2.2[-12.8,8.4],-1.5[-11.7,8.6],3.6[-6.5,13.6]; P .68,.77,.49; corrected .77,.77,.77 | Daily min; I-C; plus mean wear time adjustment | All CIs contain 0; `SEDENTARY_12_24_36` |
| MS013 | MVPA min 12/24/36: I230(75.7)/85.2(32.2),252(82.9)/80.9(31.0),248(81.6)/76.2(31.8); C232(75.8)/83.5(31.9),222(72.5)/83.3(33.1),234(76.5)/78.6(29.3); diffs1.7[-2.7,6.1],-0.2[-4.7,4.4],-1.7[-6.0,2.5]; P .45,.95,.43; corrected .68,.95,.68 | Daily min; I-C; plus wear-time adjustment | All CIs contain 0; `MVPA_12_24_36` |
| MS014 | Center use 12mo: I259(85.2), attending147(56.8); C258(84.3),101(39.1); adjusted RR1.47 [1.22,1.76], P<.001/corrected<.001 | At least once vs never, parent report; Poisson robust SE, baseline use adjusted | `CENTER_12` |
| MS015 | Center use 24mo: I263(86.5),145(55.1); C243(79.4),110(45.3); RR1.21[1.02,1.44], P=.03/corrected .03 | Same measure/model | `CENTER_24` |
| MS016 | Center use 36mo: I259(85.2),147(56.8); C248(81.0),110(44.4); RR1.29[1.08,1.53], P=.004/corrected .006; p1 abstract reports 56.8%/44.4%, RR1.29[1.08,1.53], corrected .006; p7 narrative matches | Same measure/model | Cross-source `CENTER_36` |
| MN038 | p8 footnotes: dietary/physical adjusted differences adjusted for baseline outcome, age baseline, sex; physical also mean daily wear time. P values corrected for 3 comparisons via Benjamini-Hochberg. Center RR Poisson robust-SE/baseline-center-use adjusted. Accelerometer vector magnitude; original 6-point center scale labels specified. | Table 2 model and scale labels | `T2_FOOTNOTES` |
| MN039 | p8: one parent fractured ankle while roller-skating at community-center event; no additional intervention-related adverse events | Adverse events | Count statement key `ADVERSE_EVENTS` |

## Post-hoc outcomes, adherence, and discussion

| ID | Exact location and printed evidence | Population/time/contrast/model/scale/direction | Rule and match key |
|---|---|---|---|
| MN040 | p7: at study end ages 6-8 y, overweight I25.4%/C23.5%; obese I35.5%/C34.2%; adaptive eligible I n=39 at3mo,45 at9mo,46 at12mo,102 at24mo | Post-hoc/operational values | `POSTHOC_SUMMARY` |
| MS017 | p7 and p9 Table 3 3mo obesity: I data279(91.8), obese16(5.7); C271(88.6),25(9.2); adjusted RR0.51[0.29,0.92], P=.02, corrected .10 | Obesity >=95th percentile; I/C; Poisson robust SE adjusted baseline BMI, age, sex | `OBESITY_3`; p7 describes pre-correction significance |
| MS018 | p9 9mo: I280(92.1),22(7.9); C280(91.5),30(10.7); RR0.70[0.42,1.15], P=.16, corrected .27 | Same | `OBESITY_9` |
| MS019 | p9 12mo: I274(90.1),30(10.9); C275(89.9),39(14.2); RR0.73[0.48,1.10], P=.13, corrected .27 | Same | `OBESITY_12` |
| MS020 | p9 24mo: I278(91.4),63(22.7); C266(86.9),61(22.9); RR0.92[0.70,1.21], P=.57, corrected .71 | Same | `OBESITY_24` |
| MS021 | p9 36mo: I276(90.8),98(35.5); C272(88.9),93(34.2); RR0.99[0.80,1.22], P=.90, corrected .90 | Same; numeric match to p7 N040 | `OBESITY_36` |
| MN041 | p9 Table 3 footnotes: obesity >=95th percentile CDC curves; RR Poisson robust SE adjusted child baseline BMI, age, sex; P values Benjamini-Hochberg corrected for 5 comparisons | Definitions/model/multiplicity | `T3_FOOTNOTES` |
| MN042 | p7 adherence: intervention dose 92% intensive,87% maintenance,85% sustainability; school-readiness 83% both conditions; no crossover; intervention fidelity99% over 3 y | Intervention implementation over 36 mo | `ADHERENCE` |
| MN043 | p9 discussion: >350 RCTs; 26 contact hours year 1; approximately 100 fewer kcal/day; regional Latino-child obesity prevalence37.7%; parental depression21.4%; food insecurity42.6% | Contextual numerical claims; 42.6 matches p4 cohort summary | `DISCUSSION_NUMERIC` |
| MN044 | p10 conclusion repeats 36-mo intervention did not change BMI trajectory; no new numerical outcome | Conclusion identity to `BMI_JOINT_LRT` | Narrative-match key `PRIMARY_CONCLUSION` |

## Observational reconciliation flags (not candidates)

| Flag | Evidence and bounded observation | Status |
|---|---|---|
| OBS-01 | Figure 2 has observed-BMI totals 298/302 at baseline and 276/272 at 36 mo, whereas Figure 1 reports 278/272 retained with BMI at 36 mo. The Figure 1 caption defines retention as BMI collected and distinguishes missing/loss; Figure 2 caption only says “Total No.” for plotted observations. The intervention counts require source-definition reconciliation before any equality rule is applied. | Flag for later exact-source check; no candidate ID |
| OBS-02 | Table 2 and prose use signed I-C adjusted energy difference -99.4 and CI -160.7 to -38.0; prose expresses the magnitude as “99.4 kcal fewer” and CI 38.0-160.7. These are directionally compatible presentation forms. | No inconsistency inferred |
| OBS-03 | `<.001` P values in Table 2 are finite-precision displays, not display-zero values and not a candidate basis. | Coverage note |

## Limitations

All DOC-001 native/layout text was usable; rendered pages were available for visual checking. Figure 2 does not print individual boxplot statistics, and Figure 3 reports fitted curves graphically rather than a full time-point numerical series; those values are therefore not invented. Supplement-referenced eTables/eFigures are deliberately not mapped here because they are DOC-003 assigned to the support lane.
