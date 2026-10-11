# Statistical Relationship Inventory — Pass 1

## Scope and method

- **Pass status:** PASS_1_COMPLETE.
- **Source scope:** all result-relevant statistical/inferential material mapped in DOC-001 (main article, PDF pp. 1-11), DOC-002 (protocol, PDF pp. 1-65), DOC-003 (Supplement 2, PDF pp. 1-22), and DOC-004 (data-sharing statement, PDF p. 1; no applicable inferential result).
- **Stable inventory:** 151 IDs: S001-S148 plus S028a, S028b, and S029a. Every record below is PASS_1_COMPLETE. “CI” means the confidence interval as printed; no unprinted confidence level, sidedness, degrees of freedom, covariance, variance estimator, multiplicity rule, or estimand is inferred.
- **Common main-result model definition:** unless a row specifies otherwise, DOC-001/DOC-003 continuous results use the supplied ITT mixed model with fixed group, visit, group-by-visit, site, and baseline value/HbA1c plus a participant random intercept; year-specific least-square means and linear contrasts. Binary results use supplied GEE with group, visit, group-by-visit, site, baseline HbA1c, and sandwich SEs. DOC-003 pp. 4-5 supplies these definitions; the primary year-7 contrast is two-sided in the protocol (DOC-002 pp. 26-27). The source does not supply the exact CI confidence level, degrees of freedom, all secondary-outcome sidedness, or row-specific covariance/variance details.
- **Check keys:** `Containment/order` checks that an estimate lies between correctly ordered endpoints; `direction/label` checks sign, stated direction, outcome/scale, contrast, and matched repetition; `compatibility` is only an explicitly labelled diagnostic where compatible definitions are supplied. It never substitutes for the reported analysis.

## Main article statistical relationships

| ID | Exact source location; population/time/contrast/model/measure | Estimate, CI, P/test/statistic/SE as printed | Pass-1 checks and result |
|---|---|---|---|
| S001 | DOC-001 pp. 1, 3, 6; ITT randomized groups, year 7; HbA1c net change, surgery minus medical/lifestyle; mixed model/linear contrast | −1.4% (95% CI, −1.8% to −1.0%); P < .001 | Containment/order and negative direction are compatible; abstract, Results, Table 2 and Key Points match to stated precision. Exact P/CI reconstruction not performed: CI level and row-specific variance/df absent. |
| S002 | DOC-001 pp. 1, 3; DOC-003 pp. 15-16; ITT groups, year 12; HbA1c net change, surgery minus medical/lifestyle | Main: −1.1% (−1.7% to −0.5%), P = .002. eTable 2: −1.1% (−1.7% to −0.5%), P < .001 | Estimate/CI containment and direction agree. Matched P values differ; recorded as proposal P1-02 below. eTable 2 time-label conflict is separately recorded as P1-01. |
| S003 | DOC-001 pp. 1, 3-4, 6-7; randomized groups, remission at 7 and 12 years; binary GEE/OR | Year 7: 6.2% vs 18.2%, OR 3.39 (1.25-9.17), P = .02; text rounds OR 3.4 (1.3-9.2). Year 12: 0.0% vs 12.7%, P < .001 | OR is within ordered positive CI and direction agrees with percentages; repeated year-7 values match with rounding. Year-12 P is coherent display notation, not a display-zero issue. Exact test/CI compatibility unavailable for the 12-year rate because no reported OR/SE/test statistic. |
| S004 | DOC-001 pp. 1, 7-8; deaths/adverse-event narrative | Four deaths, two per group; no group difference in major cardiovascular adverse events | Descriptive/no printed effect estimate, CI, test, or P; no inferential compatibility check available. |
| S005 | DOC-001 pp. 2-3; primary ITT HbA1c contrast at year 7 | Linear mixed-effect model, specified fixed effects/random intercept; least-square means and linear contrast | Model/contrast/scale labels match DOC-003 pp. 4-5 and DOC-002 pp. 26-27. |
| S006 | DOC-001 p. 3; secondary and sensitivity analysis definitions | IPW per-protocol; GEE binary outcomes with sandwich SE; no secondary multiplicity adjustment | Labels match DOC-003 pp. 4-5. No inference is made about an unreported variance estimator or multiplicity adjustment beyond this text. |
| S007 | DOC-001 p. 3; procedure types, year-7 HbA1c change | RYGB −1.7% (−2.0 to −1.3); sleeve −2.0% (−2.6 to −1.5); AGB −0.8% (−1.3 to −0.2); AGB vs sleeve P=.007; AGB vs RYGB P=.03; RYGB vs sleeve not significant | Every estimate lies within ordered CI and signs agree with “less improvement” for AGB. Multiple-pairwise adjustment is supplied in DOC-003 p. 4 but individual test/SE/df are absent; no exact compatibility calculation. |
| S008 | DOC-001 p. 3; DOC-003 p. 5; year-7 IPW per-protocol HbA1c | Medical 0.1% (−0.5 to 0.7); surgery −1.4% (−1.7 to −1.2); difference −1.5% (−2.1 to −0.9), P < .001 | Containment/order and direction agree; IPW/robust-sandwich labels are supplied. Exact P/CI diagnostic unavailable because confidence level, effective sample/weights, and variance details are not printed. |
| S009 | DOC-001 pp. 3-4, 6; year-7 binary outcomes | Remission OR 3.4 (1.3-9.2), P=.02; HbA1c <7% OR 3.2 (1.8-5.9), P<.001; HbA1c <6.5% P=.002 | OR directions/intervals agree with rates and Table 2 rounded values. The narrative uses ≤6.5% while Table 2 uses <6.5%; this is a label comparator for cross-lane review, not a statistical inference determination here. |
| S010 | DOC-001 pp. 4, 6; diabetes medication outcomes | Surgery lower than baseline, P<.001; medical change P=.19 at year 7 and P=.12 at year 12; insulin 16% vs 56%, P<.001; incretin use P<.001 | Direction/narrative labels are compatible with Table 2 at year 7. Exact model/test definition for each longitudinal statement is not individually printed. |
| S011 | DOC-001 p. 6; weight loss | Year 7 medical 8.3% (6.1-10.5), surgery 19.9% (18.1-21.6), P<.001; year 12 10.8% (8.2-13.5) vs 19.3% (17.3-21.3), P<.001 | Ordered intervals and direction agree; matched eFigure 2 year-7 ITT values agree. No separate group-difference estimate is printed in the narrative for these rows. |
| S012 | DOC-001 pp. 3, 5; postbaseline HbA1c trajectory | Surgery lower at all postbaseline points; P<.001 | Figure lines are LS estimates but no exact labels are printed; direction matches exact year-7 result. No per-visit test/statistic or model contrast is printed. |
| S013 | DOC-001 p. 4; 12-year remission and procedure comparison | 12-year P<.001; 7-year procedure rates 24.5%, 15.2%, 8.9%, no significant procedure differences | Direction/labels are compatible with S003/S009; individual procedure test statistics and adjustment details are not printed. |
| S014 | DOC-001 p. 4; Table 1 labels | No. (%), mean (SD), central value (IQR), and available-measurement n labels | Scale/label check: bracketed n is measurement availability, not randomized group total; no inferential estimate. |
| S015 | DOC-001 pp. 3, 6; Table 2 framework | Model-derived changes; numeric difference=surgery change minus medical change; binary difference=surgery-year-7 odds divided by medical-year-7 odds | Effect-measure/scale labels are explicit; raw displayed means are not used as a substitute for model-derived changes. |
| S016 | DOC-001 p. 6; Table 2 year-7 HbA1c | Medical −0.2 (−0.5 to 0.2); surgery −1.6 (−1.8 to −1.3); difference −1.4 (−1.8 to −1.0), P<.001 | All interval/order/sign checks compatible; matches S001. |
| S017 | DOC-001 p. 6; fasting glucose, year 7 | −3.8% (−14.8 to 7.2); −14.1% (−22.0 to −6.3); difference −10.3% (−23.6 to 2.9), P=.13 | Containment/order and null-crossing interval agree with non-small P directionally; exact compatibility not calculated. |
| S018 | DOC-001 p. 6; weight, year 7 | −8.3% (−10.5 to −6.1); −19.9% (−21.6 to −18.1); difference −11.6% (−14.3 to −8.9), P<.001 | Containment/order/sign compatible; matches S011/eFigure 2. |
| S019 | DOC-001 p. 6; SBP, year 7 | −1.1% (−3.9 to 1.7); −3.4% (−5.6 to −1.2); difference −2.3% (−5.8 to 1.1), P=.19 | Compatible interval ordering/null crossing and narrative of no group difference. |
| S020 | DOC-001 p. 6; DBP, year 7 | −4.3% (−7.0 to −1.6); −6.0% (−8.1 to −3.8); difference −1.7% (−5.0 to 1.7), P=.32 | Compatible interval ordering/null crossing. |
| S021 | DOC-001 p. 6; LDL, year 7 | 5.5% (−3.3 to 14.3); 10.8% (3.8 to 17.9); difference 5.4% (−5.6 to 16.3), P=.34 | Compatible interval ordering/null crossing and narrative. |
| S022 | DOC-001 p. 6; HDL, year 7 | 20.5% (14.5-26.6); 37.4% (32.6-42.3); difference 16.9% (9.4-24.4), P<.001 | Compatible interval ordering/direction and narrative. |
| S023 | DOC-001 p. 6; total cholesterol, year 7 | −0.7% (−5.6 to 4.1); 4.9% (1.0-8.7); difference 5.6% (−0.4 to 11.6), P=.07 | Compatible interval ordering/null crossing. |
| S024 | DOC-001 p. 6; triglycerides, year 7 | 2.3% (−8.6 to 13.2); −19.0% (−27.8 to −10.2); difference −21.3% (−34.9 to −7.8), P=.002 | Compatible interval ordering/direction and narrative. |
| S025 | DOC-001 p. 6; serum creatinine, year 7 | 9.5% (1.8-17.1); 10.5% (4.4-16.7); difference 1.1% (−8.4 to 10.5), P=.83 | Compatible interval ordering/null crossing. |
| S026 | DOC-001 p. 6; urine albumin:creatinine ratio, year 7 | Fold change 1.3 (0.9-1.9); 0.9 (0.7-1.2); difference −0.4 (−1.0 to 0.1), P=.10 | Estimate/interval direction compatible under supplied fold-change scale; difference is not a ratio and is labelled as printed. |
| S027 | DOC-001 p. 6; remission, year 7 | Within-group OR 10.4 (0.4-279.4), 36.2 (1.9-699.0); group OR 3.39 (1.25-9.17), P=.02 | Positive ORs lie within positive CIs and group direction matches rates/S003. |
| S028 | DOC-001 p. 6; diabetes medication, year 7 | OR 0.10 (0.01-3.27), 0.03 (0.01-0.11); group OR 0.09 (0.03-0.24), P<.001 | Positive ORs within ordered CI and direction matches lower surgery use. |
| S028a | DOC-001 p. 6; oral/GLP1 only, year 7 | OR 0.53 (0.29-0.97), 0.74 (0.46-1.20); group OR 0.98 (0.53-1.82), P=.95 | Positive ORs within ordered CI; group CI includes 1, compatible with P directionally. |
| S028b | DOC-001 p. 6; insulin and/or oral/GLP1, year 7 | OR 1.93 (1.07-3.46), 0.18 (0.11-0.31); group OR 0.13 (0.06-0.29), P<.001 | Positive ORs within ordered CI; direction compatible. |
| S029 | DOC-001 p. 6; HbA1c <7%, year 7 | OR 2.77 (1.38-5.54), 6.42 (3.63-11.4); group OR 3.22 (1.76-5.88), P<.001 | Positive ORs within ordered CI; direction matches percentages/S009. |
| S029a | DOC-001 p. 6; HbA1c <6.5%, year 7 | OR 2.30 (1.19-4.47), 4.44 (2.46-8.01); group OR 2.89 (1.48-5.64), P=.002 | Positive ORs within ordered CI; label is `<6.5%` in Table 2. |
| S030 | DOC-001 p. 7; BMI subgroups, year 7 | HbA1c difference −1.2 (−1.8 to −0.5) lower BMI and −1.5 (−2.1 to −1.0) higher BMI; comparison P=.40. Weight differences 14.8% (10.8-18.8), P<.001 and 9.2% (5.6-12.9), P=.03 | Containment/order/direction compatible. The printed positive weight-loss differences use the source’s direction, unlike negative HbA1c differences. |
| S031 | DOC-001 pp. 6-7; clinical/lipid narrative | No group SBP/LDL difference; HDL P<.001; triglycerides P=.002; neither creatinine nor urine ratio difference | Cross-location repetitions match S019/S021-S026. |
| S032 | DOC-001 pp. 7-8; major events | Events described as similar except selected safety outcomes | Table 3 does not print group effect estimate/CI/P; no test compatibility check. |
| S033 | DOC-001 p. 7; crossover/conversion/revision label | Procedure groups no significant differences except combined endpoint more common in medical/lifestyle | Exact test/statistic is not printed on this page; source label held for Supplement 2 comparison. |
| S034 | DOC-001 p. 8; Table 3 safety labels | Event definitions and exclusions | Measure labels present; Table 3 contains no inferential estimates/P values. |
| S035 | DOC-003 pp. 4-6; shared statistical definitions | ITT model; four-category secondary multiplicity adjustment; GEE sandwich SE; MAR; chi-square/Fisher for adverse events | Definitions match S005-S006. These definitions support label checks only where outcome/table scope matches. |

## Supplement 2: year-12 eTable 2

**Common record for S036-S052:** DOC-003 pp. 15-16, eTable 2; title/columns say “Laboratory and clinical outcomes at year 12 and changes from baseline” and “Year 12.” Continuous rows show LS estimate (95% CI); binary rows show ORs. Footnotes a-c instead say baseline and year-7 data, 7-year changes, and year-7 binary odds. This internal time-label contradiction applies to every S036-S052 and is proposal P1-01, not an assumption that any printed number should be normalized.

| ID | Outcome: printed result | Pass-1 check |
|---|---|---|
| S036 | HbA1c: −0.3 (−0.8,0.1) vs −1.4 (−1.7,−1.1); difference −1.1 (−1.7,−0.5); P<.001 | Containment/order/sign compatible. Same estimate/CI as S002 but P differs from DOC-001 P=.002: P1-02. |
| S037 | Fasting glucose: −6% (−19.6,7.6) vs −11.1% (−20,−2.2); −5.1% (−21,10.9); P=.53 | Ordered intervals; null-crossing difference compatible with P directionally. |
| S038 | Weight: −10.8% (−13.5,−8.2) vs −19.3% (−21.3,−17.3); −8.4% (−11.7,−5.2); P<.001 | Ordered intervals/sign compatible; values match S011 at year 12. |
| S039 | SBP: −4.7% (−8.5,−1) vs −4.5% (−7.1,−1.9); 0.3% (−4.2,4.7); P=.91 | Ordered intervals/null-crossing compatible. |
| S040 | DBP: −7.7% (−11.4,−4) vs −6.6% (−9.1,−4.1); 1.1% (−3.2,5.5); P=.61 | Ordered intervals/null-crossing compatible. |
| S041 | LDL: −7.9% (−19.9,4) vs −11.9% (−20.2,−3.7); −4% (−18.2,10.2); P=.58 | Ordered intervals/null-crossing compatible. |
| S042 | HDL: 16.6% (8.4,24.7) vs 38.1% (32.5,43.7); 21.5% (11.9,31.2); P<.001 | Ordered intervals/direction compatible. |
| S043 | Total cholesterol: −4.2% (−11.1,2.6) vs −5.5% (−10,−.9); −1.2% (−9.3,6.9); P=.77 | Ordered intervals/null-crossing compatible. |
| S044 | Triglycerides: 9.8% (−4.9,24.5) vs −23.3% (−33.3,−13.2); −33.1% (−50.5,−15.7); P<.001 | Ordered intervals/direction compatible. |
| S045 | Creatinine: 29.5% (19.3,39.7) vs 20.3% (13.3,27.3); −9.2% (−21.2,2.9); P=.14 | Ordered intervals/null-crossing compatible. |
| S046 | Urine albumin:creatinine: 2.2 (1.4,3.6) vs 1.5 (1.1,2.1); −.7 (−1.9,.4); P=.20 | Fold-change labels and ordered intervals compatible; non-ratio difference retained as printed. |
| S047 | Remission: 0% vs 12.7%; surgery OR 23.6 (1.2,465.3); group difference NA; P<.001; footnote medical rate 2e-16 | Nonzero surgery OR lies within CI. `0%` is rounded printed rate, not a P-value display zero. Group comparator value is intentionally NA; no missing OR is inferred. |
| S048 | Diabetes medications: 93.8%, OR .06 (.002,2.16) vs 82.6%, .10 (.02,.39); group OR .45 (.15,1.36), P=.16 | Positive ORs within ordered CIs; group CI includes 1, compatible directionally. |
| S049 | Oral/GLP1: 34.4%, OR .45 (.23,.85) vs 53.5%, 1.14 (.70,1.85); group OR 1.80 (.85,3.82), P=.12 | Positive ORs within ordered CIs; group CI includes 1. |
| S050 | Insulin and/or oral/GLP1: 59.4%, OR 2.31 (1.23,4.32) vs 29.1%, .40 (.25,.64); group OR .25 (.10,.58), P=.001 | Positive ORs within ordered CIs and direction compatible. |
| S051 | HbA1c<7%: 29.4%, OR 3.15 (1.20,8.30) vs 54.6%, 6.57 (3.56,12.1); group OR 2.90 (1.15,7.29), P=.02 | Positive ORs within ordered CIs and direction compatible. |
| S052 | HbA1c<6.5%: 19.6%, OR 2.68 (.92,7.81) vs 40.0%, 4.90 (2.54,9.48); group OR 2.75 (1.09,6.90), P=.03 | Positive ORs within ordered CIs and direction compatible. |

## Supplement 2: nutritional and safety comparisons

**Common test definition for S053-S145:** DOC-003 pp. 5-6 says adverse events/outcomes are summarized as percentages and compared by chi-square or Fisher exact tests, but does not assign which test to an individual row or give test statistics/df. Therefore only count/percentage direction, source labels, endpoint ordering, and cross-location checks are made; exact P reconstruction is not performed.

| ID | Exact source location and printed comparison | Pass-1 check |
|---|---|---|
| S053 | DOC-003 p.17, eTable 3 anemia: MED 11/87 (12.6); SURG 35/147 (23.8), P=.04; RYGB 25/78 (32.1), .003; SG 8/36 (22.2), .18; AGB 2/33 (6.1), .30 | Counts/percentages and comparator labels agree; each P has no row-specific test designation. |
| S054 | p.17 low iron: 15/88 (17.0); 48/151 (31.8), .01; RYGB 30/81 (37.0), .003; SG 10/37 (27.0), .20; AGB 8/33 (24.2), .37 | Direction/count-rate labels compatible. |
| S055 | p.17 B12 deficiency: 8/88 (9.1);20/151(13.2),.34; RYGB15/81(18.5),.07; SG4/37(10.8),.77; AGB1/33(3.0),.26 | Direction/count-rate labels compatible. |
| S056 | p.17 vitamin D deficiency:23/88(26.1);35/151(23.2),.61; RYGB22/81(27.2),.88; SG2/37(5.4),.008; AGB11/33(33.3),.43 | Direction/count-rate labels compatible. |
| S057 | p.17 hypocalcemia:0/88;1/151(.7),.44; RYGB1/81(1.2),.30; SG0/37 NA; AGB0/33 NA | Zero event counts are counts, not display-zero P values; NA is a printed non-test label. |
| S058 | p.17 elevated PTH:29/88(33.0);66/151(43.7),.10; RYGB41/81(50.6),.02; SG12/37(32.4),.95; AGB13/33(39.4),.51 | Direction/count-rate labels compatible. |
| S059 | p.17 hypoalbuminemia:9/88(10.2);23/151(15.2),.27; RYGB14/81(17.3),.18; SG5/37(13.5),.60; AGB4/33(12.1),.76 | Direction/count-rate labels compatible. |
| S060 | p.17 severe hypoalbuminemia:1/88(1.1);0/151(0), P=.19 | Count/rate labels compatible; zero is a count/percentage, not P display. |
| S061 | DOC-003 p.18, eTable 4 hemoglobin LS means: medical 13.7 SE .2; surgery 13 SE .1; difference −.8 SE .2; P<.001 | Difference direction matches surgery minus medical. Difference and SE are rounded; diagnostic ratio is not calculated because exact unrounded values/test/df are absent. |
| S062 | p.18 iron:83.9 SE3.2;85.3 SE2.5; difference1.4 SE4.1; P=.74 | Direction compatible with surgery minus medical; no exact compatibility calculation. |
| S063 | p.18 vitamin B12:760.8 SE105.1;1173.2 SE80.6; difference412.4 SE132.4; P=.002 | Difference direction/scale compatible. |
| S064 | p.18 vitamin D:35.2 SE1.8;40.5 SE1.4; difference5.3 SE2.3; P=.02 | Difference direction/scale compatible. |
| S065 | p.18 calcium:9.6 SE.04;9.5 SE.03; difference−.1 SE.0; P=.03 | Difference direction compatible. Printed SE `0.0` is finite-precision display; exact inferential compatibility cannot be calculated without unrounded SE and test/df. |
| S066 | p.18 PTH:51.1 SE3.3;60.3 SE2.5; difference9.2 SE4.2; P=.03 | Difference direction/scale compatible. |
| S067 | p.18 albumin:4.1 SE.03;4.1 SE.02; difference−.01 SE.04; P=.72 | Difference direction/scale compatible. |
| S068 | DOC-003 pp.19-20 eTable 5, chest pain through 12 years:10/96(10.4) vs15/166(9.0), P=.71 | Counts/percent labels and supplied chi-square/Fisher family compatible. |
| S069 | pp.19-20 hypertension:2(2.1) vs6(3.6), .71 | Same check. |
| S070 | pp.19-20 foot ulcers:1(1.0) vs4(2.4), .65 | Same check. |
| S071 | pp.19-20 tachycardia:3(3.1) vs3(1.8), .49 | Same check. |
| S072 | pp.19-20 hypotension:4(4.2) vs2(1.2), .20 | Same check. |
| S073 | pp.19-20 sleep apnea:1(1.0) vs2(1.2), 1.00 | Same check. |
| S074 | pp.19-20 carotid vascular disease:2(2.1) vs1(.6), .56 | Same check. |
| S075 | pp.19-20 nausea/vomiting:15(15.6) vs43(25.9), .054 | Same check. |
| S076 | pp.19-20 abdominal pain:10(10.4) vs37(22.3), .02 | Direction matches higher surgery rate and footnote procedure rates. |
| S077 | pp.19-20 GERD:10(10.4) vs29(17.5), .12 | Same check. |
| S078 | pp.19-20 diarrhea:7(7.3) vs20(12.0), .22 | Same check. |
| S079 | pp.19-20 constipation:10(10.4) vs17(10.2), .96 | Same check. |
| S080 | pp.19-20 dysphagia:0(0.0) vs12(7.2), .005 | Zero is count/percentage, not P display; direction compatible. |
| S081 | pp.19-20 hiatal hernia:2(2.1) vs7(4.2), .49 | Same check. |
| S082 | pp.19-20 dumping syndrome:0(0.0) vs8(4.8), .03 | Zero is count/percentage; direction compatible. |
| S083 | pp.19-20 colon polyps:6(6.2) vs7(4.2), .46 | Same check. |
| S084 | pp.19-20 gastrointestinal stricture:0(0.0) vs4(2.4), .30 | Same check. |
| S085 | pp.19-20 hematochezia:1(1.0) vs3(1.8),1.00 | Same check. |
| S086 | pp.19-20 colitis:0(0.0) vs3(1.8),.30 | Same check. |
| S087 | pp.19-20 gastric prolapse:0(0.0) vs2(1.2),.53 | Same check. |
| S088 | pp.19-20 gastroparesis:4(4.2) vs0(0.0),.02 | Direction compatible. |
| S089 | pp.19-20 vertigo/dizziness:9(9.4) vs27(16.3),.12 | Same check. |
| S090 | pp.19-20 depression:14(14.6) vs24(14.5),.98 | Same check. |
| S091 | pp.19-20 concussion/contusion/head injury:2(2.1) vs13(7.8),.058 | Same check. |
| S092 | pp.19-20 neuropathy:7(7.3) vs11(6.6),.84 | Same check. |
| S093 | pp.19-20 memory/cognitive dysfunction:3(3.1) vs6(3.6),.83 | Same check. |
| S094 | pp.19-20 cataracts:12(12.5) vs20(12.0),.91 | Same check. |
| S095 | pp.19-20 blurred/double vision:7(7.3) vs11(6.6),.84 | Same check. |
| S096 | pp.19-20 glaucoma:5(5.2) vs4(2.4),.23 | Same check. |
| S097 | pp.19-20 upper respiratory infection:18(18.8) vs43(25.9),.19 | Same check. |
| S098 | pp.19-20 pneumonia:3(3.1) vs11(6.6),.23 | Same check. |
| S099 | pp.19-20 cellulitis:5(5.2) vs6(3.6),.53 | Same check. |
| S100 | pp.19-20 infection/sepsis:0(0.0) vs2(1.2),.53 | Same check. |
| S101 | pp.19-20 osteomyelitis:1(1.0) vs1(.6),1.00 | Same check. |
| S102 | pp.19-20 COVID-19:1(1.0) vs1(.6),1.00 | Same check. |
| S103 | pp.19-20 severe hyperglycemia:8(8.3) vs14(8.4),.98 | Same check. |
| S104 | pp.19-20 hyperparathyroidism:0(0.0) vs2(1.2),.53 | Same check. |
| S105 | pp.19-20 dehydration:2(2.1) vs14(8.4),.058 | Same check. |
| S106 | pp.19-20 hypokalemia:2(2.1) vs8(4.8),.33 | Same check. |
| S107 | pp.19-20 hyperkalemia:1(1.0) vs0(0.0),.37 | Same check. |
| S108 | pp.19-20 hypercalcemia:0(0.0) vs1(.6),1.00 | Same check. |
| S109 | pp.19-20 back pain:18(18.8) vs36(21.7),.57 | Same check. |
| S110 | pp.19-20 osteoarthritis:8(8.3) vs6(3.6),.10 | Same check. |
| S111 | pp.19-20 renal insufficiency:2(2.1) vs4(2.4),1.00 | Same check. |
| S112 | pp.19-20 acute renal failure:1(1.0) vs2(1.2),1.00 | Same check. |
| S113 | pp.19-20 allergy/intolerance:5(5.2) vs9(5.4),.94 | Same check. |
| S114 | pp.19-20 alcohol abuse:2(2.1) vs7(4.2),.49 | Same check. |
| S115 | pp.19-20 abdominal wall hernia:1(1.0) vs6(3.6),.43 | Same check. |
| S116 | DOC-003 p.21 eTable 6, crossovers/conversions/revisions through 12 years:24/96(25.0) vs15/166(9.0), P<.001 | Direction matches S033/eTable 7 components. |
| S117 | p.21 cholecystectomy 2(2.1) vs7(4.2),.49; lysis 0 vs2(1.2),.53; hernia 0 vs2(1.2),.53; laparoscopy 0 vs2(1.2),.53; laparotomy 0 vs1(.6),1.00 | All procedure rows retain source chi-square/Fisher family; count/percentage labels compatible. |
| S118 | p.21 appendectomy 0 vs2(1.2),.53; colon resection 0 vs2(1.2),.53; hysterectomy 0 vs2(1.2),.53; other abdominal 2(2.1) vs5(3.0),1.00 | Same check. |
| S119 | p.21 leak endoscopy 0 vs1(.6),1.00; dilated-GJ endoscopy 0 vs2(1.2),.53; GI-bleed endoscopy 1(1.0) vs0,.37; other therapeutic 2(2.1) vs5(3.0),1.00; other endoscopy 3(3.1) vs14(8.4),.09 | Same check. |
| S120 | p.21 joint injection 9(9.4) vs6(3.6),.053; fracture procedures1(1.0) vs3(1.8),1.00; joint replacement5(5.2) vs3(1.8),.12; amputation0 vs1(.6),1.00; other orthopedic13(13.5) vs33(19.9),.19 | Same check. |
| S121 | p.21 cataract surgery8(8.3) vs13(7.8),.89; other eye4(4.2) vs6(3.6),.82; vitrectomy2(2.1) vs1(.6),.56; panniculectomy0 vs5(3.0),.16; other plastic2(2.1) vs1(.6),.56 | Same check. |
| S122 | DOC-003 pp.9-13, eFigures 2-6; ITT/PP, medication, clinical and BMI graphics | eFigure 2 ITT weight 8.3%/19.9%, PP 5.6%/20.4%; eFigure 4 P<.001; eFigure 5 P=.16 SBP, <.001 HDL, .83 LDL, <.001 triglycerides; eFigure 6 interaction P=.03 | Displayed lines/SE bars and P labels agree with named model framework and main matched results where same measure/time. Individual graphical exact values not printed. |
| S123 | DOC-002 pp.26-36; protocol primary/multiple-model/power relations | A1 beta_7 surgery-minus-nonsurgical HbA1c percent change, two-sided P<.05; A2 log OR; A3 Bonferroni pairwise; missingness/IPTW; planned Cox/Markov analyses | Planned definitions, not reported study estimates. They corroborate model/scale labels only; no cross-time result is treated as a contradiction. |
| S124 | DOC-002 pp.27-29; protocol power figures | 500 simulations; primary >90% except 30% missing; remission 94.6% at 20% missing; other planned power values | Planning simulation results, not reported inferential outcomes; no containment/P compatibility check applicable. |
| S125 | DOC-002 pp.55-56; parent-trial prior outcomes | Parent study descriptive one-year outcome table, no CI/P/test reported for the listed rows | Separate parent-study context; not matched to pooled long-term estimates without population/time alignment. |
| S126 | DOC-003 p.22/eTable 7; crossover/revision description | 24/96 25%; AGB 1%, SG16%, RYGB8%; revision components; no P | Components sum to the eTable 6 24 medical crossovers and support the combined-label direction; no test printed. |
| S127 | DOC-001 p.5 and DOC-003 pp.8-13 figures; plot conventions | LS estimates/one-SE errors where stated; raw boxplots separately labelled | Model-estimate versus raw-data scales are not conflated. No exact visual-coordinate inference. |
| S128 | DOC-001 pp.7-8 and DOC-003 pp.17-21 safety narrative/table linkage | Narrative says anemia, fractures and GI outcomes more common after surgery; tables supply varying endpoint-specific P values | Matched labels are retained; no unprinted global test is inferred. |
| S129 | DOC-001 p.1/p.3 versus DOC-003 pp.15-16, year-12 HbA1c repetition | −1.1 (−1.7 to −.5) in both locations; P=.002 versus <.001 | Dedicated cross-location P repetition check; proposal P1-02. |
| S130 | DOC-003 pp.15-16 eTable 2 title/columns versus footnotes a-c | Title/columns: Year 12; footnotes: baseline and year-7 data, 7-year changes/comparisons | Dedicated time/measure-label repetition check; proposal P1-01. |
| S131 | DOC-001 p.1 and DOC-003 p.16, year-12 remission | Main 0.0% vs12.7%, P<.001; eTable: 0% vs12.7%, P<.001 and medical 2e-16 footnote | Finite rounding of rate is compatible and not a display-zero P issue. |
| S132 | DOC-001 pp.3,6 and DOC-003 p.9, year-7 weight | 8.3% and19.9% ITT in all matched locations | Values/direction match. |
| S133 | DOC-001 pp.6-7 and DOC-003 p.12, BP/lipids | Main year-7 P=.19 SBP, .34 LDL, <.001 HDL, .002 triglycerides; figure overall P=.16, .83, <.001, <.001 | Not a matched same-time contrast for every value; figures report longitudinal overall comparisons. No contradiction asserted. |
| S134 | DOC-001 p.7 and DOC-003 p.13, BMI subgroup weight | 14.8% lower-BMI and9.2% higher-BMI; P=.03 | Matched values/direction agree. |
| S135 | DOC-001 p.3 and DOC-003 p.5, PP sensitivity description | IPW accounts for medical-to-surgery crossover | Label and estimand description match; no unreported PP test result inferred. |
| S136 | DOC-001 pp.3-8 and DOC-003 pp.3-6, ITT population/time | Randomized treatment groups, annual 7-to-12-year follow-up | Population/time/model labels are compatible; planned protocol counts are not treated as observed counts. |
| S137 | DOC-001 Table 2 and DOC-003 eTable 2, scale labels | Net HbA1c; relative % continuous changes; urine ratio fold change; binary OR | Source-specific differences in time must be retained; no conversion between scales is performed. |
| S138 | DOC-001 p.6 and DOC-003 p.18, LS estimate/SE table labels | Table 2 shows 95% CI; eTable 4 shows SE | Different inferential displays; no direct P/CI/SE calculation because shared confidence convention/df not supplied. |
| S139 | DOC-003 pp.17-21, event/procedure row P values | P=1.00 and ordinary finite values only | No P=0/p=.000 notation occurs in S053-S121; no display-zero classification needed. |
| S140 | DOC-001 S001/S008/S010/S011/S012/S016/S018/S022/S024/S028/S028b/S029 and DOC-003 S036/S038/S042/S044/S050/S051/S116/S122 | Multiple P<.001 values | All are inequality displays, not finite-precision zero. `DISPLAY_ZERO_NOT_CANDIDATE` is not applicable. |
| S141 | DOC-002 protocol p.27 and DOC-003 supplement p.4 | Primary two-sided P<.05 is planned; result-level primary P<.001 | Sidedness is supplied for the planned primary test only. It is not extended by convention to secondary rows. |
| S142 | DOC-003 p.18 eTable 4 | Difference=surgical minus medical, explicit footnote | Direction labels and signs compatible across all seven nutrition LS-mean rows. |
| S143 | DOC-003 p.17 eTable 3 | Each surgery subgroup P compared with medical/lifestyle, explicit footnote | Reference group label explicit; no inference about multiplicity adjustment. |
| S144 | DOC-003 pp.19-21 eTables 5-6 | Chi-squared test or Fisher exact test, explicit footnotes | Exact test choice absent per row; compatibility diagnostics intentionally not performed. |
| S145 | DOC-004 p.1 | No result-relevant inferential statistic | PASS_1_COMPLETE — no applicable statistical relationship. |
| S146 | DOC-001 p.1/P<.001 and DOC-003 p.16/P<.001 remission | P inequality with nonzero contrast | No zero display; no candidate. |
| S147 | DOC-003 p.16 footnote e | Medical remission rate `2e-16`; table display `0%` | Coherent finite-precision display of a rate; it is neither a P value nor candidate discovery evidence. |
| S148 | All sources | Missing-definition register | Not supplied: CI confidence level for many tables, exact secondary test sidedness, row-specific df/test statistic/variance/covariance, exact test assignment for event rows, and exact estimand mapping for eTable 2’s conflicting time labels. These are named limitations, not inferred defects. |

## Pass-1 candidate proposals (no C IDs; Pending Human Adjudication)

### P1-01 — eTable 2 contains internally conflicting time labels

- **Category proposed:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-003 `joi240004supp2_prod_1721756962.82552.pdf` pp. 15-16, eTable 2 title/column headings and footnotes a-c.
- **Direct observation:** the title reads “Laboratory and clinical outcomes at year 12 and changes from baseline,” both descriptive columns read “Year 12,” and the remission footnote says “The 12-year remission rate.” Footnote a instead says its descriptive data are baseline and year-7; footnote b defines several displayed changes as year-7 over baseline; footnote c defines group differences/ORs at year 7.
- **Consistency rule:** a single table’s time label for the same descriptive and inferential columns should identify the same time point, unless the source explicitly distinguishes columns by time.
- **Independent contradiction:** the table’s own Year 12 title/columns/footnote e conflict with footnotes a-c’s repeated Year 7 definitions. This proposal does not rely on any P-value display convention.
- **Human question:** Which time point governs the eTable 2 changes, group comparisons, binary ORs, and their P values, and should the footnotes or heading/columns be corrected?

### P1-02 — matched year-12 HbA1c contrast has different printed P values

- **Category proposed:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf` PDF p. 1 Abstract Results and p. 3 Results; DOC-003 `joi240004supp2_prod_1721756962.82552.pdf` PDF p. 15, eTable 2.
- **Direct observation:** DOC-001 prints the year-12 surgery-minus-medical HbA1c change as −1.1% (95% CI, −1.7% to −0.5%; P = .002). DOC-003 eTable 2 prints the same −1.1 (−1.7, −0.5) in its Year 12 row with P < .001.
- **Consistency rule:** after matching the printed effect estimate, interval, contrast, and stated time point, repeated P values for the same reported result should agree or have a stated reason for differing analyses.
- **Diagnostic limitation:** no test statistic, df, exact variance/covariance, or definitive resolution of eTable 2’s internal time labels is supplied; no independently derived tail probability is used.
- **Human question:** Is the eTable P value intended for a different time point, analysis, or test than the main article’s stated 12-year linear contrast, or is one printed P value incorrect?

## Pass-1 completion and limitations

- **Relationship count:** 151 stable S records, all `PASS_1_COMPLETE`.
- **Candidate proposal count:** 2 distinct proposals, neither assigned a C ID or adjudication.
- **Display-zero handling:** no coherent `P = 0`/`p = 0.000` relationship was found. The `0%` and `2e-16` remission displays are rates, not P values, and were not candidate discovery triggers.
- **Limitations:** exact interval/P/test/SE compatibility was only assessed directionally where source definitions supported it. Missing definitions are listed in S148; visual figures without printed coordinates were not reverse-engineered.

## Pass 2 completion update

- **Pass status:** PASS_2_COMPLETE.
- **Scope:** every stable S record above: S001-S148, S028a, S028b, and S029a (151 records).
- **Durable pass-2 record:** `checkers/statistical_pass_2.md` names every S ID and records its `PASS_2_COMPLETE` status, complete cross-lane-ledger/recheck reconciliation, and the precise definitions missing for any withheld compatibility diagnostic.
- **Per-record update:** S001 `PASS_2_COMPLETE`; S002 `PASS_2_COMPLETE`; S003 `PASS_2_COMPLETE`; S004 `PASS_2_COMPLETE`; S005 `PASS_2_COMPLETE`; S006 `PASS_2_COMPLETE`; S007 `PASS_2_COMPLETE`; S008 `PASS_2_COMPLETE`; S009 `PASS_2_COMPLETE`; S010 `PASS_2_COMPLETE`; S011 `PASS_2_COMPLETE`; S012 `PASS_2_COMPLETE`; S013 `PASS_2_COMPLETE`; S014 `PASS_2_COMPLETE`; S015 `PASS_2_COMPLETE`; S016 `PASS_2_COMPLETE`; S017 `PASS_2_COMPLETE`; S018 `PASS_2_COMPLETE`; S019 `PASS_2_COMPLETE`; S020 `PASS_2_COMPLETE`; S021 `PASS_2_COMPLETE`; S022 `PASS_2_COMPLETE`; S023 `PASS_2_COMPLETE`; S024 `PASS_2_COMPLETE`; S025 `PASS_2_COMPLETE`; S026 `PASS_2_COMPLETE`; S027 `PASS_2_COMPLETE`; S028 `PASS_2_COMPLETE`; S028a `PASS_2_COMPLETE`; S028b `PASS_2_COMPLETE`; S029 `PASS_2_COMPLETE`; S029a `PASS_2_COMPLETE`; S030 `PASS_2_COMPLETE`; S031 `PASS_2_COMPLETE`; S032 `PASS_2_COMPLETE`; S033 `PASS_2_COMPLETE`; S034 `PASS_2_COMPLETE`; S035 `PASS_2_COMPLETE`; S036 `PASS_2_COMPLETE`; S037 `PASS_2_COMPLETE`; S038 `PASS_2_COMPLETE`; S039 `PASS_2_COMPLETE`; S040 `PASS_2_COMPLETE`; S041 `PASS_2_COMPLETE`; S042 `PASS_2_COMPLETE`; S043 `PASS_2_COMPLETE`; S044 `PASS_2_COMPLETE`; S045 `PASS_2_COMPLETE`; S046 `PASS_2_COMPLETE`; S047 `PASS_2_COMPLETE`; S048 `PASS_2_COMPLETE`; S049 `PASS_2_COMPLETE`; S050 `PASS_2_COMPLETE`; S051 `PASS_2_COMPLETE`; S052 `PASS_2_COMPLETE`; S053 `PASS_2_COMPLETE`; S054 `PASS_2_COMPLETE`; S055 `PASS_2_COMPLETE`; S056 `PASS_2_COMPLETE`; S057 `PASS_2_COMPLETE`; S058 `PASS_2_COMPLETE`; S059 `PASS_2_COMPLETE`; S060 `PASS_2_COMPLETE`; S061 `PASS_2_COMPLETE`; S062 `PASS_2_COMPLETE`; S063 `PASS_2_COMPLETE`; S064 `PASS_2_COMPLETE`; S065 `PASS_2_COMPLETE`; S066 `PASS_2_COMPLETE`; S067 `PASS_2_COMPLETE`; S068 `PASS_2_COMPLETE`; S069 `PASS_2_COMPLETE`; S070 `PASS_2_COMPLETE`; S071 `PASS_2_COMPLETE`; S072 `PASS_2_COMPLETE`; S073 `PASS_2_COMPLETE`; S074 `PASS_2_COMPLETE`; S075 `PASS_2_COMPLETE`; S076 `PASS_2_COMPLETE`; S077 `PASS_2_COMPLETE`; S078 `PASS_2_COMPLETE`; S079 `PASS_2_COMPLETE`; S080 `PASS_2_COMPLETE`; S081 `PASS_2_COMPLETE`; S082 `PASS_2_COMPLETE`; S083 `PASS_2_COMPLETE`; S084 `PASS_2_COMPLETE`; S085 `PASS_2_COMPLETE`; S086 `PASS_2_COMPLETE`; S087 `PASS_2_COMPLETE`; S088 `PASS_2_COMPLETE`; S089 `PASS_2_COMPLETE`; S090 `PASS_2_COMPLETE`; S091 `PASS_2_COMPLETE`; S092 `PASS_2_COMPLETE`; S093 `PASS_2_COMPLETE`; S094 `PASS_2_COMPLETE`; S095 `PASS_2_COMPLETE`; S096 `PASS_2_COMPLETE`; S097 `PASS_2_COMPLETE`; S098 `PASS_2_COMPLETE`; S099 `PASS_2_COMPLETE`; S100 `PASS_2_COMPLETE`; S101 `PASS_2_COMPLETE`; S102 `PASS_2_COMPLETE`; S103 `PASS_2_COMPLETE`; S104 `PASS_2_COMPLETE`; S105 `PASS_2_COMPLETE`; S106 `PASS_2_COMPLETE`; S107 `PASS_2_COMPLETE`; S108 `PASS_2_COMPLETE`; S109 `PASS_2_COMPLETE`; S110 `PASS_2_COMPLETE`; S111 `PASS_2_COMPLETE`; S112 `PASS_2_COMPLETE`; S113 `PASS_2_COMPLETE`; S114 `PASS_2_COMPLETE`; S115 `PASS_2_COMPLETE`; S116 `PASS_2_COMPLETE`; S117 `PASS_2_COMPLETE`; S118 `PASS_2_COMPLETE`; S119 `PASS_2_COMPLETE`; S120 `PASS_2_COMPLETE`; S121 `PASS_2_COMPLETE`; S122 `PASS_2_COMPLETE`; S123 `PASS_2_COMPLETE`; S124 `PASS_2_COMPLETE`; S125 `PASS_2_COMPLETE`; S126 `PASS_2_COMPLETE`; S127 `PASS_2_COMPLETE`; S128 `PASS_2_COMPLETE`; S129 `PASS_2_COMPLETE`; S130 `PASS_2_COMPLETE`; S131 `PASS_2_COMPLETE`; S132 `PASS_2_COMPLETE`; S133 `PASS_2_COMPLETE`; S134 `PASS_2_COMPLETE`; S135 `PASS_2_COMPLETE`; S136 `PASS_2_COMPLETE`; S137 `PASS_2_COMPLETE`; S138 `PASS_2_COMPLETE`; S139 `PASS_2_COMPLETE`; S140 `PASS_2_COMPLETE`; S141 `PASS_2_COMPLETE`; S142 `PASS_2_COMPLETE`; S143 `PASS_2_COMPLETE`; S144 `PASS_2_COMPLETE`; S145 `PASS_2_COMPLETE`; S146 `PASS_2_COMPLETE`; S147 `PASS_2_COMPLETE`; S148 `PASS_2_COMPLETE`.
