# Main-paper quantitative evidence reconstruction

## Scope and provenance

Assigned scope: DOC-001, REPORT, jama_brenner_2019_oi_190039.pdf, physical PDF pages 1-7 (printed 1686-1692). All pages were read completely from the source-matched canonical normalized layout assets A040-A046. Canonical path: .ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-N.txt. These are legacy Poppler layout text; the curator compared each against current direct pdftotext 26.01.0. Additional direct inspection: `pdftotext -layout -f 5 -l 5 "jama_brenner_2019_oi_190039.pdf" -` (Poppler 26.01.0, stdout, no derivative written). Reused full-page image A049 was visually inspected for Table 2/3 alignment and labels. No new OCR, Python extraction, source mutation, reused-asset mutation, or historical scientific conclusion input was used. Direct PDF remains authority.

Local MAIN-N IDs identify numeric relationship groups; local MAIN-S IDs identify inferential or method relationships. Global checker inventories may assign their own N/S IDs with a crosswalk. Every row retains its result-specific values; a group is a complete relationship, not a sampling limit. The 48 numeric groups and 49 inferential/method groups total 97 mapped relationships. Counts and denominators calculated from printed cells below are explicitly derived, not source-printed sample totals. No checking judgment or candidate diagnosis is made.

## Page coverage

| Source page | Exact contents mapped | Reusable aid | Fresh-required | Status |
|---|---|---|---|---|
| [1](../../../jama_brenner_2019_oi_190039.pdf#page=1) | Abstract design, participants, dose, outcome, results, conclusions | A040 | No | COMPLETE |
| [2](../../../jama_brenner_2019_oi_190039.pdf#page=2) | Background quantities, Key Points, eligibility, endpoint definition, collection schedule, randomization start | A041 | No | COMPLETE |
| [3](../../../jama_brenner_2019_oi_190039.pdf#page=3) | Randomization, processing, laboratory, outcomes, power, statistical methods, population/sample narrative, primary result start | A042 | No | COMPLETE |
| [4](../../../jama_brenner_2019_oi_190039.pdf#page=4) | Figure and footnotes; Table 1 and footnote; primary/secondary/per-protocol narrative; adverse events | A043 | No | COMPLETE |
| [5](../../../jama_brenner_2019_oi_190039.pdf#page=5) | Entire Tables 2/3, headers, abbreviations and footnotes; site analysis and discussion | A044 and A049; direct page-5 layout stdout | No | COMPLETE |
| [6](../../../jama_brenner_2019_oi_190039.pdf#page=6) | Discussion quantitative design/dose/time statements, limitations, conclusions, article information | A045 | No | COMPLETE |
| [7](../../../jama_brenner_2019_oi_190039.pdf#page=7) | Funding, acknowledgments, data-sharing pointer, all references | A046 | No | COMPLETE: no applicable trial numeric or inferential result; bibliographic numerals are not trial evidence |

No scientific coverage gaps remain. No fresh-required pages were assigned. No trial rate, person-time quantity, hazard ratio, odds ratio, risk ratio, standardized effect, standalone standard error, numerical test statistic, or median outcome is reported. Reported laboratory transit median/IQR is retained below. No trial outcome figure other than the participant-flow Figure appears.

## Numeric population, design, flow, descriptive and occurrence map

All page locations below refer to DOC-001 and the PDF links in the coverage table. A = aspirin and P = placebo throughout. Statements about other studies are marked background, rather than treated as trial outcomes.

| Local ID | Exact page/section | Printed relationship, unit and population | Matching locations or derived denominator |
|---|---|---|---|
| MAIN-N001 | p1 abstract Design/Interventions; p2 design; p4 Figure | 2422 randomized; A 1208, P 1214; adults 40-80 y; 14 gastroenterology practices + 4 hospitals = 18 centers; enrollment June 2013-November 2016; final follow-up January 27, 2017 | p2 Key Points repeats 2422 and 40-80 y; p3 Results repeats 2422; p5 Discussion and p6 Conclusions repeat eligibility ages |
| MAIN-N002 | p1 Objective/Interventions; p2 design/Key Points; p3 packaging; p4/5 titles; p6 discussion | Single oral 300-mg aspirin tablet vs placebo, 2 days before stool sampling; aspirin without enteric coating; placebo cellulose, lactosemonohydrate, magnesium stearate | Same contrast governs all trial results; p6 proposed 75/100 mg are future-research doses, not assigned doses |
| MAIN-N003 | p1 abstract Results | Among 2422 randomized patients, mean (SD) age 59.6 (7.9) y; 1219 men, 50% | p3 analyzed-population narrative repeats mean 59.6 y but not SD; Table 1 sex counts belong to 2134 analyzed |
| MAIN-N004 | p1 abstract Results; p3 Results; p4 Figure | 2134 analyzed; 288 dropped out/excluded; A 1075, P 1059 | Derived 1075+1059=2134; 2422-2134=288 |
| MAIN-N005 | p1 abstract Results; p3 Results; p4 Table 1 | 78% primary screening and 22% diagnostic colonoscopy in analyzed population; p6 limitations repeats 22% diagnostic | Exact Table 1 counts and missing indication retained MAIN-N023/024 |
| MAIN-N006 | p1 abstract Results; p3 Results | 224 advanced neoplasms (10.5%), including 8 CRC (0.4%) and 216 advanced adenoma (10.1%) | Table 1 most advanced finding MAIN-N025/026; denominator analyzed 2134 |
| MAIN-N007 | p2 introductory paragraphs | Background global CRC deaths approximately 860000/year; FIT detects majority 70%-80% CRC at >90% specificity, minority of advanced adenomas | Background, no trial numerator/denominator provided |
| MAIN-N008 | p2 Trial Design and Trial Population | Advanced neoplasm = CRC or advanced adenoma of size ≥1 cm, tubulovillous/villous components, or high-grade dysplasia | Definition applies Tables 1-3 and all sensitivity/specificity/PPV/NPV |
| MAIN-N009 | p2 collection procedures | 4 collection kits for each of 2 FITs; baseline + scheduled days 2, 3, 4 after tablet; 1 stool sample per scheduled day, 4 overall; subsequent-day postponement allowed; all before bowel preparation; colonoscopy within 3 months recruitment | Primary scheduled day 2 vs exact actual day 2 distinction MAIN-S037/038 |
| MAIN-N010 | p3 randomization continuation/data processing | Randomized blocks of 20 tablets: 10 each group; colonoscopy/histology entered by 2 independent blinded reviewers | Randomization unit participant; allocation individual tablet within block |
| MAIN-N011 | p3 Laboratory Methods | Storage 2°C-8°C; sampling-to-arrival median 4 days, IQR 3-5 days; quantitative analytical range 0.03-142 μg Hb/g feces | Laboratory timing/range, not outcome distribution |
| MAIN-N012 | p3 Results | 93.6% of analyzed participants aged 45-74; mean age 59.6 y; similar sex proportions and demographic/clinical distributions in A/P | Table 1 age bands MAIN-N015-022; derived 1997/2134 for 45-74 |
| MAIN-N013 | p3 Results, returned/valid samples paragraph | Quantitative scheduled day 2 valid samples: A 1030 (95.8%), P 1012 (95.6%); qualitative A 974 (90.6%), P 969 (91.5%) | Percent denominators A1075/P1059; Table 2 cell sums MAIN-N040-048; external eTable 2 locator only |
| MAIN-N014 | p4 Table 1 Sex | A men 547 (50.9%), women 528 (49.1%); P men 528 (49.9%), women 531 (50.1%); columns A n1075/P n1059 | Sex totals to analyzed groups; randomized men 1219 belongs MAIN-N003 |
| MAIN-N015 | p4 Table 1 Age <45 y | A26 (2.4%), P30 (2.8%) | A1075/P1059 |
| MAIN-N016 | p4 Table 1 Age 45-49 y | A63 (5.9%), P52 (4.9%) | A1075/P1059 |
| MAIN-N017 | p4 Table 1 Age 50-54 y | A165 (15.3%), P164 (15.5%) | A1075/P1059 |
| MAIN-N018 | p4 Table 1 Age 55-59 y | A315 (29.3%), P318 (30.0%) | A1075/P1059 |
| MAIN-N019 | p4 Table 1 Age 60-64 y | A232 (21.6%), P216 (20.4%) | A1075/P1059 |
| MAIN-N020 | p4 Table 1 Age 65-69 y | A144 (13.4%), P153 (14.4%) | A1075/P1059 |
| MAIN-N021 | p4 Table 1 Age 70-74 y | A92 (8.6%), P83 (7.8%) | A1075/P1059 |
| MAIN-N022 | p4 Table 1 Age ≥75 y | A38 (3.5%), P43 (4.1%) | A1075/P1059 |
| MAIN-N023 | p4 Table 1 Primary indication | Screening A805 (77.9%), P794 (78.2%); diagnostic A228 (22.1%), P221 (21.8%) | Nonmissing denominators derived A1033/P1015, pooled2048 |
| MAIN-N024 | p4 Table 1 footnote a | Indication missing A42/P44 participants | Analyzed A1075/P1059 minus nonmissing A1033/P1015 |
| MAIN-N025 | p4 Table 1 Most advanced finding | CRC A3 (0.3%), P5 (0.5%); advanced adenoma A112 (10.4%), P104 (9.8%) | Denominators A1075/P1059; derived neoplasms A115/P109; total224 |
| MAIN-N026 | p4 Table 1 Most advanced finding | Nonadvanced adenoma A286 (26.6%), P280 (26.4%); none of above A674 (62.7%), P670 (63.3%) | Denominators A1075/P1059; derived without advanced neoplasm A960/P950 |
| MAIN-N027 | p4 Figure aspirin allocation | Randomized1208; received intervention as randomized1131; did not receive as randomized or dropped out77 | 1208=1131+77 |
| MAIN-N028 | p4 Figure placebo allocation | Randomized1214; received placebo as randomized1153; did not receive as randomized or dropped out61 | 1214=1153+61 |
| MAIN-N029 | p4 Figure aspirin follow-up/analysis | Underwent colonoscopy1131; included1075; excluded from primary analysis56 | 1131=1075+56 |
| MAIN-N030 | p4 Figure aspirin exclusion reasons | No stool32; samples sent after colonoscopy2; history blood in stool20; aspirin takers2 | 32+2+20+2=56 |
| MAIN-N031 | p4 Figure placebo follow-up/analysis | Underwent colonoscopy1153; included1059; excluded from primary analysis94 | 1153=1059+94 |
| MAIN-N032 | p4 Figure placebo exclusion reasons | No stool56; history blood in stool30; history CRC5; aspirin takers3 | 56+30+5+3=94 |
| MAIN-N033 | p4 Figure footnotes a/b/c | Eligibility-assessed count not collected; no sample/information = dropout; completed colonoscopy = followed up | Figure total randomized2422; derived colonoscopy2284 and primary postcolonoscopy exclusions150 |
| MAIN-N034 | p4 adverse-events paragraph | A11 adverse events in7 participants; 2 serious events in2 participants requiring hospitalization, acute appendicitis and acute suppurative cholangitis with acute kidney injury, regarded unrelated to drug; P6 adverse events in5 participants, no serious events; all recovered | No explicit safety-population denominator printed here |
| MAIN-N035 | p4 combined-sample narrative | At least1 positive among up to3 samples scheduled days2,3,4; higher sensitivities/lower specificities both arms; little change in between-arm sensitivity differences | eTable3 external match locator; no numeric result in main beyond collection rule |
| MAIN-N036 | p6 discussion/limitations | Designed effect absolute sensitivity increase24%; primary samples reduced approximately4% through exclusions; limited advanced-neoplasm sample; secondary analyses no multiplicity adjustment | Power MAIN-S042; no explicit denominator for approximate4% statement |
| MAIN-N037 | p6 dose/timing discussion | Tested300 mg single dose; proposed75 or100 mg single/multiple future tablets; primary FIT2 days after aspirin; repeated-day sensitivity analysis not suggesting improved diagnostic performance | Future dose proposals separate from randomized exposure |
| MAIN-N038 | p3 Outcomes | Quantitative primary cutoffs17 μg Hb/g feces (manufacturer),10.2 μg Hb/g feces (qualitative cutoff); qualitative cutoff10.2 | Table headers p5 show17.0/10.2, units μg Hb/g; p1 abstract and p2 Key Points repeat two thresholds |
| MAIN-N039 | p7 references | Reference7 title mentions2235 external screening-colonoscopy participants; references18/19 identify Agresti-Coull/Caffo; reference20 lme4 version1.1-21; reference21 variance-component testing | No trial results on page; bibliography values not trial data |
| MAIN-N040 | p5 Table2 all quantitative10.2 | Complete diagnostic counts/denominators below | Sensitivity MAIN-S001, specificity MAIN-S002, PPV MAIN-S019, NPV MAIN-S020 |
| MAIN-N041 | p5 Table2 all quantitative17.0 | Complete diagnostic counts/denominators below | MAIN-S003/004/021/022 |
| MAIN-N042 | p5 Table2 all qualitative10.2 | Complete diagnostic counts/denominators below | MAIN-S005/006/023/024 |
| MAIN-N043 | p5 Table2 men quantitative10.2 | Complete diagnostic counts/denominators below | MAIN-S007/008/025/026 |
| MAIN-N044 | p5 Table2 men quantitative17.0 | Complete diagnostic counts/denominators below | MAIN-S009/010/027/028 |
| MAIN-N045 | p5 Table2 men qualitative10.2 | Complete diagnostic counts/denominators below | MAIN-S011/012/029/030; Table3 test label blank |
| MAIN-N046 | p5 Table2 women quantitative10.2 | Complete diagnostic counts/denominators below | MAIN-S013/014/031/032 |
| MAIN-N047 | p5 Table2 women quantitative17.0 | Complete diagnostic counts/denominators below | MAIN-S015/016/033/034 |
| MAIN-N048 | p5 Table2 women qualitative10.2 | Complete diagnostic counts/denominators below | MAIN-S017/018/035/036 |

## Table 2 diagnostic counts and all four result denominators

Exact location: [DOC-001 PDF p5 Table 2](../../../jama_brenner_2019_oi_190039.pdf#page=5). Title: Sensitivity and Specificity for Detecting Advanced Neoplasms at Day 2 After a Single 300-mg Aspirin Dose or Placebo. Footnote a: Results of the intention-to-screen analysis. Test cutoff unit μg Hb/g. Abbreviations: TP true-positive, FN false-negative, TN true-negative, FP false-positive, Hb hemoglobin. Counts appear under No. of Detections for each randomized group. All percentages and differences relate to advanced neoplasms. Same count matrix supports predictive-value Table 3. Denominator rules reconstructed from count labels: sensitivity TP/(TP+FN); specificity TN/(TN+FP); PPV TP/(TP+FP); NPV TN/(TN+FN). No person-time enters these proportions.

| ID | Population/test/cutoff | A TP/FN/TN/FP | P TP/FN/TN/FP | Derived A/P total | Derived A/P sensitivity denominator | Derived A/P specificity denominator | Derived A/P PPV denominator | Derived A/P NPV denominator |
|---|---|---|---|---|---|---|---|---|
| MAIN-N040 | All quantitative10.2 | 45/67/755/163 | 31/71/807/103 | 1030/1012 | 112/102 | 918/910 | 208/134 | 822/878 |
| MAIN-N041 | All quantitative17.0 | 32/80/842/76 | 23/79/863/47 | 1030/1012 | 112/102 | 918/910 | 108/70 | 922/942 |
| MAIN-N042 | All qualitative10.2 | 35/66/732/141 | 22/78/798/71 | 974/969 | 101/100 | 873/869 | 176/93 | 798/876 |
| MAIN-N043 | Men quantitative10.2 | 33/44/360/90 | 15/39/387/68 | 527/509 | 77/54 | 450/455 | 123/83 | 404/426 |
| MAIN-N044 | Men quantitative17.0 | 25/52/408/42 | 13/41/424/31 | 527/509 | 77/54 | 450/455 | 67/44 | 460/465 |
| MAIN-N045 | Men qualitative10.2 | 28/43/354/74 | 12/43/400/48 | 499/503 | 71/55 | 428/448 | 102/60 | 397/443 |
| MAIN-N046 | Women quantitative10.2 | 12/23/395/73 | 16/32/420/35 | 503/503 | 35/48 | 468/455 | 85/51 | 418/452 |
| MAIN-N047 | Women quantitative17.0 | 7/28/434/34 | 10/38/439/16 | 503/503 | 35/48 | 468/455 | 41/26 | 462/477 |
| MAIN-N048 | Women qualitative10.2 | 7/23/378/67 | 10/35/398/23 | 475/466 | 30/45 | 445/421 | 74/33 | 401/433 |

## Every Table 2 inferential endpoint

Table2 p5: sensitivity/specificity estimates and differences printed as %, intervals95%. Contrast A minus P; difference unit percentage points. Population intention-to-screen, scheduled day2, single300-mg aspirin/placebo. Statistical-method context p3: Wald-adjusted proportion intervals Agresti-Coull and difference intervals Agresti-Caffo, PropCIs; two-sided significance P<.05; no multiple-testing adjustments. Individual group intervals are not printed in this table. P values absent from table; matching narrative supplies the P values listed below. Exact method generating individual reported outcome P values is not expressly named beyond the general two-sided criterion. Counts/denominators linked by MAIN-N040-048.

| ID | Count link and endpoint | A % | P % | A−P, % (95% CI) | Printed P and matching occurrences |
|---|---|---:|---:|---|---|
| MAIN-S001 | N040 sensitivity all quantitative10.2 | 40.2 | 30.4 | 9.8 (−3.1 to22.2) | P=.14 p1 abstract and p4 primary; estimates p2 Key Points; p3 primary start |
| MAIN-S002 | N040 specificity all quantitative10.2 | 82.2 | 88.7 | −6.4 (−9.6 to−3.2) | P<.001 p4 secondary |
| MAIN-S003 | N041 sensitivity all quantitative17.0 | 28.6 | 22.5 | 6.0 (−5.7 to17.5) | P=.32 p1 abstract and p4 primary; estimates p2 Key Points |
| MAIN-S004 | N041 specificity all quantitative17.0 | 91.7 | 94.8 | −3.1 (−5.4 to−0.8) | P=.008 p4 secondary |
| MAIN-S005 | N042 sensitivity all qualitative10.2 | 34.7 | 22.0 | 12.7 (0.1 to24.7) | P=.048 p4 secondary, difference described12.7 percentage points higher |
| MAIN-S006 | N042 specificity all qualitative10.2 | 83.8 | 91.8 | −8.0 (−11.0 to−4.9) | P<.001 p4 secondary, difference described8.0 points lower |
| MAIN-S007 | N043 sensitivity men quantitative10.2 | 42.9 | 27.8 | 15.1 (−1.6 to30.6) | No individual P printed; p4 male range summary |
| MAIN-S008 | N043 specificity men quantitative10.2 | 80.0 | 85.1 | −5.1 (−10.0 to−0.1) | No individual P printed; p4 male range summary |
| MAIN-S009 | N044 sensitivity men quantitative17.0 | 32.5 | 24.1 | 8.4 (−7.5 to23.3) | p4 range minimum8.4 with same interval |
| MAIN-S010 | N044 specificity men quantitative17.0 | 90.7 | 93.2 | −2.5 (−6.1 to1.1) | p4 range minimum2.5 points lower with same signed interval |
| MAIN-S011 | N045 sensitivity men qualitative10.2 | 39.4 | 21.8 | 17.6 (1.3 to32.6) | p4 range maximum17.6 with same interval |
| MAIN-S012 | N045 specificity men qualitative10.2 | 82.7 | 89.3 | −6.6 (−11.2 to−2.0) | p4 range maximum6.6 points lower with same signed interval |
| MAIN-S013 | N046 sensitivity women quantitative10.2 | 34.3 | 33.3 | 1.0 (−19.1 to21.4) | p4 women sensitivity described similar |
| MAIN-S014 | N046 specificity women quantitative10.2 | 84.4 | 92.3 | −7.9 (−12.0 to−3.8) | p4 women specificity described lower |
| MAIN-S015 | N047 sensitivity women quantitative17.0 | 20.0 | 20.8 | −0.8 (−17.9 to17.2) | p4 women sensitivity described similar |
| MAIN-S016 | N047 specificity women quantitative17.0 | 92.7 | 96.5 | −3.7 (−6.7 to−0.8) | p4 women specificity described lower |
| MAIN-S017 | N048 sensitivity women qualitative10.2 | 23.3 | 22.2 | 1.1 (−17.7 to20.9) | p4 women sensitivity described similar |
| MAIN-S018 | N048 specificity women qualitative10.2 | 84.9 | 94.5 | −9.6 (−13.5 to−5.5) | p4 women specificity described lower |

## Every Table 3 inferential endpoint

Exact location: [DOC-001 PDF p5 Table 3](../../../jama_brenner_2019_oi_190039.pdf#page=5). Title: Positive and Negative Predictive Values for Detecting Advanced Neoplasms at Day 2 After a Single 300-mg Aspirin Dose or Placebo. Footnote a intention-to-screen analysis. Abbreviations Hb hemoglobin, PPV positive predictive value, NPV negative predictive value. Columns A PPV/NPV, P PPV/NPV, Difference (95% CI) PPV/NPV. Cutoff μg Hb/g. The column does not print a percent symbol for PPV/NPV; values are percentages in the diagnostic context; contrast differences interpreted as percentage points. The third Men test-name cell is blank in canonical text, direct layout and visually inspected image; its10.2 cutoff and values are retained under that exact row rather than silently filling the cell. MAIN-N045 provides the corresponding diagnostic count row, labeled Qualitative in Table2. Every individual P is unreported in Table3. Group-specific CIs are unreported. Method/contrast/population context as Table2 above. p4 narrative says overall no significant differences, neither intention-to-screen nor per-protocol; per-protocol outcomes are in external eTable5.

| ID | Count link / exact population-test row / endpoint | A value | P value | Difference (95% CI) |
|---|---|---:|---:|---|
| MAIN-S019 | N040 All quantitative10.2 PPV | 21.6 | 23.1 | −1.5 (−10.7 to7.4) |
| MAIN-S020 | N040 All quantitative10.2 NPV | 91.8 | 91.9 | −0.1 (−2.7 to2.5) |
| MAIN-S021 | N041 All quantitative17.0 PPV | 29.6 | 32.9 | −3.2 (−17.2 to10.5) |
| MAIN-S022 | N041 All quantitative17.0 NPV | 91.3 | 91.6 | −0.3 (−2.8 to2.3) |
| MAIN-S023 | N042 All qualitative10.2 PPV | 19.9 | 23.7 | −3.8 (−14.4 to6.5) |
| MAIN-S024 | N042 All qualitative10.2 NPV | 91.7 | 91.1 | 0.6 (−2.1 to3.3) |
| MAIN-S025 | N043 Men quantitative10.2 PPV | 26.8 | 18.1 | 8.8 (−3.0 to19.8) |
| MAIN-S026 | N043 Men quantitative10.2 NPV | 89.1 | 90.8 | −1.7 (−5.9 to2.4) |
| MAIN-S027 | N044 Men quantitative17.0 PPV | 37.3 | 29.5 | 7.8 (−10.3 to24.8) |
| MAIN-S028 | N044 Men quantitative17.0 NPV | 88.7 | 91.2 | −2.5 (−6.4 to1.4) |
| MAIN-S029 | N045 Men third row, test-name blank,10.2 PPV | 27.5 | 20 | 7.5 (−6.4 to20.2) |
| MAIN-S030 | N045 Men third row, test-name blank,10.2 NPV | 89.2 | 90.3 | −1.1 (−5.3 to3.0) |
| MAIN-S031 | N046 Women quantitative10.2 PPV | 14.1 | 31.4 | −17.3 (−31.8 to−2.5) |
| MAIN-S032 | N046 Women quantitative10.2 NPV | 94.5 | 92.9 | 1.6 (−1.7 to4.8) |
| MAIN-S033 | N047 Women quantitative17.0 PPV | 17.1 | 38.5 | −21.4 (−42.2 to0.8) |
| MAIN-S034 | N047 Women quantitative17.0 NPV | 93.9 | 92 | 1.9 (−1.4 to5.2) |
| MAIN-S035 | N048 Women qualitative10.2 PPV | 9.5 | 30.3 | −20.8 (−37.8 to−4.0) |
| MAIN-S036 | N048 Women qualitative10.2 NPV | 94.3 | 91.9 | 2.3 (−1.1 to5.8) |

## Analysis-method, statistical-design and narrative relationships

| ID | Exact location | Complete source-grounded relationship and quantitative inputs | Match key or bounded unreported input |
|---|---|---|---|
| MAIN-S037 | p3 Outcomes; p1 Main Outcome | Primary sensitivity quantitative FIT, advanced neoplasms, scheduled day2 after tablet, two predefined cutoffs17 and10.2 μg Hb/g; main analysis intention-to-screen | MAIN-S001/003; not actual exact-day per-protocol |
| MAIN-S038 | p3 Outcomes; p4 eTable4 narrative | Prespecified per-protocol approach uses samples collected exactly day2. Men differences of greater magnitude than intention-to-screen; lower quantitative cutoff difference23.2 points (95% CI5.0 to39.5), qualitative difference22.5 (4.5 to38.6); specificity differences similar between approaches | Cutoff10.2, men, A−P; group estimates/counts/P not printed in main; external eTable4 match locator |
| MAIN-S039 | p3 Statistical Analyses | Analyze participants in randomized group; exclude consent withdrawals or no samples/information as dropouts; exclude no precolonoscopy stool from primary | MAIN-N004 and Figure exclusions; analyze available stool, not every randomized participant |
| MAIN-S040 | p3 Statistical Analyses | R3.4.0; Wald-adjusted CI for sensitivity/specificity: Agresti-Coull; differences: Agresti-Caffo; PropCIs package | Table2/3 difference intervals95%; individual group intervals not shown in main |
| MAIN-S041 | p3 Statistical Analyses; p4 sex interaction narrative | Interaction P from binomial generalized linear model; sex×intervention interaction P all nonsignificant, range.08-.49 | Exact P per endpoint, link and coefficient estimates not printed in main; Table2 sex-stratified endpoints |
| MAIN-S042 | p3 Sample Size and Power; p6 discussion/limitations | Assumed advanced-neoplasm prevalence10%;90% power; two-sided α=.05; day2 sensitivity contrast60% vs36%, absolute24 percentage points | No target total or attrition inflation printed in main sample-size paragraph; not designed for moderate/small differences stated p6 |
| MAIN-S043 | p3 Statistical Analyses; p6 limitations | Statistical significance two-sided P<.05; no multiple-testing adjustments; secondary outcomes exploratory; p6 repeats multiple secondary analyses without adjustments | Applies printed P values and conclusions; no multiplicity-adjusted threshold reported |
| MAIN-S044 | p3 Outcomes | Prespecified reported secondary: quantitative specificity, PPV/NPV; sensitivity gain combining days2-4; qualitative sensitivity/specificity/PPV/NPV; sex-specific sensitivity/specificity/PPV/NPV both tests; serious adverse events. Further secondary likelihood ratios and AUC not reported in article | Links all secondary Table2/3 results and MAIN-N034/035; no invented numerical likelihood ratio/AUC |
| MAIN-S045 | p3 Sensitivity Analysis; p5 Sensitivity Analysis | For each main intention-to-screen outcome, generalized linear mixed model random intercept for site using lme4; likelihood-ratio test null zero random-intercept variance. P range0.16-0.50, never significant; model without random intercept retained | External eTable6 locator; numerical variance/test statistics, family, link, covariates not printed in main |
| MAIN-S046 | p4 multiple samples narrative; p6 sampling discussion | At least1 positive up to3 scheduled days2-4 produces higher sensitivity/lower specificity both arms and little change in arm sensitivity differences; p6 says sensitivity analyses do not suggest multiple days improve diagnostic performance | External eTable3; numerical multi-day estimates absent from main |
| MAIN-S047 | p4 PPV/NPV narrative | Table3 and eTable5 described as PPV/NPV at day2; overall no significant differences, neither intention-to-screen nor per-protocol | MAIN-S019-036; "overall" wording preserved without assigning a judgment to subgroup intervals |
| MAIN-S048 | p1 Conclusions; p2 Key Points Meaning; p5 Discussion opening; p6 Conclusions | Single aspirin dose versus placebo did not significantly increase quantitative FIT sensitivity for advanced colorectal neoplasms at two predefined cutoffs in adults40-80 not using antithrombotics | MAIN-S001/003; p2 Findings lists40.2 vs30.4 and28.6 vs22.5, and no statistically significant difference |
| MAIN-S049 | p4 sex-specific narrative | Men sensitivity point estimates8.4 (CI−7.5 to23.3) to17.6 (1.3 to32.6) points higher; specificity2.5 (−6.1 to1.1) to6.6 (−11.2 to−2.0) points lower; women similar sensitivity but lower specificity | MAIN-S007-018; all interaction P nonsignificant.08-.49 linked MAIN-S041 |

## Complete occurrence and cross-document matching keys

Primary quantitative10.2 sensitivity: p1 Results -> p2 Findings -> p3 Primary End Point start -> p4 Primary End Point continuation -> p5 Table2 All quantitative10.2 -> p1/p2/p5/p6 conclusion occurrences MAIN-S048. Primary quantitative17.0 sensitivity: p1 Results -> p2 Findings -> p4 Primary End Point -> p5 Table2 All quantitative17.0 -> same conclusion occurrences. The abstracts report randomized demographics before mentioning2134 analyzed; do not substitute Table1 analyzed-population demographics for randomized values.

Specificities all quantitative10.2/17.0 and qualitative10.2 and qualitative sensitivity: p4 Secondary End Points -> corresponding p5 Table2 cells. Men ranges/women directional claims: p4 Secondary End Points -> all corresponding sex Table2 rows. Sex interactions: p3 method -> p4 range claim -> supplied supplement for individual interaction P values. Per-protocol men sensitivity differences: p3 population definition -> p4 eTable4 narrative -> supplied supplement, never Table2 intention-to-screen. Combined-day results: p3 secondary definition -> p4 eTable3 narrative -> p6 sampling discussion -> supplied supplement. Predictive values: p3 secondary definition -> p4 Table3/eTable5 narrative -> all p5 Table3 cells; match intention-to-screen to Table3 and per-protocol to external eTable5. Site model: p3 random-intercept method -> p5 retained-model decision -> external eTable6. The support mapper owns those external sources; no support values were imported into this disjoint artifact.

Baseline Table1 has column n1075/n1059. Sex, age and most-advanced-finding rows use these full denominators. Colonoscopy indication uses nonmissing1033/1015 and the exact footnote42/44 missing. Flow Figure distinguishes randomized, received, colonoscopy, primary inclusion, and no-receipt/dropout; eligibility-assessed count expressly absent. Scheduled valid day2 FIT denominators differ by test and are exactly reconstructible from Table2 cells. For each sex/test/cutoff row, the diagnostic count link is reused for PPV and NPV, without substituting sensitivity denominators for positive/negative predictive-value denominators.

## Boundaries and gaps

All assigned pages and every table/figure/footnote/result narrative were mapped. Zero uncovered pages or unreadable result cells. No direct fresh-required units arose. Unreported inputs retained as absent: exact outcome P-value test construction; group-specific Table2/3 intervals; individual sex interaction P values; main sample-size target and attrition assumptions; actual adverse-event denominator; numerical site-model test statistics/variances; numerical multi-day and per-protocol results beyond the narrative contrasts. These are source reporting limits for later reviewers, not scientific-coverage gaps or candidates. No conclusions from old candidate or report artifacts were read.

Audit precision repair: MAIN-S045 source description is generalized linear mixed model; its family/link are not explicitly supplied. The inferred family label was removed; numerical evidence and source locations are unchanged.
