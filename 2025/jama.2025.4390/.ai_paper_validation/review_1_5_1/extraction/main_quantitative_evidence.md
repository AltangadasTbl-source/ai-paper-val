# DOC-001 Main-Paper Quantitative Evidence Map

## Scope and method

- **Direct source:** `jama_garrison_2025_oi_250019_1749674951.29054.pdf` (12 PDF pages; current-source SHA-256 is recorded in `source_hashes_before.sha256`).
- **Scope completed:** every PDF page 1-12, directly extracted from this current PDF with `pdftotext` native and `pdftotext -layout` output. Fresh files are `preprocessing/main/doc001_p01_native.txt` through `doc001_p12_native.txt` and corresponding `_layout.txt` files.
- **Location convention:** `jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=N` refers to PDF page N. `N` IDs are numeric/reporting relationships and `S` IDs are inferential/statistical relationships. These are evidence-map IDs only, not candidate IDs or judgments.
- **Study match key:** BedMed pragmatic randomized clinical trial; community-dwelling Canadian adults with hypertension taking at least one once-daily antihypertensive; comparison is all once-daily medication at bedtime versus morning; randomized ITT denominators 1677 versus 1680.

## Page 1 — title page and abstract

| ID | Directly observed quantitative relationship | Match key and exact source location |
|---|---|---|
| N001 | Recruitment March 31, 2017-May 26, 2022; final follow-up December 22, 2023; 436 primary-care clinicians in 5 Canadian provinces; randomized 1:1: bedtime n=1677, morning n=1680 (total 3357). | Trial design/population; `...pdf#page=1` abstract. |
| N002 | Randomized cohort: 56.4% female; median age 67 years; 53.7% on monotherapy; median follow-up 4.6 years in each group. | Overall cohort/timepoint; `...pdf#page=1` abstract. |
| N003/S001 | Composite primary event rates: bedtime 2.3 versus morning 2.4 per 100 patient-years; adjusted HR 0.96 (95% CI 0.77-1.19), P=.70. Outcome is time to first all-cause death or hospitalization/ED visit for stroke, ACS, or heart failure. | Primary outcome; adjusted Cox comparison; `...pdf#page=1` abstract. Repeated with exact table values in N046/S011. |

## Page 2 — methods and eligibility context

| ID | Directly observed quantitative relationship | Match key and exact source location |
|---|---|---|
| N004 | Recruitment source: 436 clinicians (429 family physicians, 7 nurse practitioners) across 5 provinces; participant eligibility included age >=18 years and one or more once-daily BP-lowering medicine. Recruitment dates and observation end repeat N001. | Trial population; `...pdf#page=2` Methods. |
| N005 | Prespecified diuretic adherence context: about three-fourths of monotherapy participants were adherent to bedtime use at 6 months. | Medication-level adherence/interim assessment; `...pdf#page=2` Participants. |
| N006 | Background trial quantities retained as contextual, non-BedMed match keys: MAPEC 2156 adults (2000-2009), reported 61% MACE reduction; Hygia 19,084 (2008-2018), 45% reduction; TIME 21,104 (2011-2021), no benefit. | External-study narrative; `...pdf#page=2` Introduction. |

## Page 3 — intervention, outcomes, power, and interim analysis

| ID | Directly observed quantitative relationship | Match key and exact source location |
|---|---|---|
| N007 | Randomization is 1:1, permuted blocks of 10 or 12, stratified by province. Follow-up contacts at 1 week, 6 weeks, 6 months, then every 6 months; cognitive testing at 18 months. | Allocation/follow-up schedule; `...pdf#page=3` Intervention. |
| N008 | Outcome-source coverage: administrative health data available for 92.6%; unavailable for 7.4%, of whom 90.3% lived in Ontario or Saskatchewan; blinded adjudication committee has 3 physicians. | Outcome ascertainment population; `...pdf#page=3` Outcomes. |
| N009 | Secondary definitions: cognitive decline at 18 months is >=2-point Short Blessed Test worsening; new cognitive impairment is a new score >=10 or new dementia diagnosis. Safety recall timepoint is prior month for light-headedness, fainting, and falling; EQ-5D-5L assessed at 12 months. | Outcome/scale/timepoint definitions; `...pdf#page=3` Secondary Outcomes. |
| S002 | Planned event-driven survival analysis: detect/exclude 25% reduction (HR <=0.75), power 0.80, 1:1 allocation, two-sided type-I error .05; required 379 events, inflated 7% to target 406 for projected 5% withdrawal/loss. | Sample-size design; `...pdf#page=3` Sample Size. |
| S003 | Interim analysis May 18, 2022: n=155 primary outcomes; DSMB comprised 5 members. Stopping consideration: P<=.001 for primary benefit or P<=.05 for harm for any outcome; committee recommended continuation twice (including October 28, 2022). | Interim monitoring rule; `...pdf#page=3` Interim Analysis. |

## Page 4 — participant flow, analysis population, and retention

| ID | Directly observed quantitative relationship | Match key and exact source location |
|---|---|---|
| N010 | Figure 1 flow: 5073 assessed; 1716 excluded = 1249 not interested + 375 not eligible + 87 physician advice + 5 other. Not-eligible details: 207 glaucoma/high IOP, 68 no BP-lowering medication, 43 no hypertension, 32 no fixed sleep schedule, 14 outside province, 8 only twice-daily BP medicines, 3 did not control timing. 3357 randomized = 1677 bedtime + 1680 morning; all included in primary analysis. | Participant-flow arithmetic; `...pdf#page=4`, Figure 1. |
| N011 | Figure 1 follow-up: bedtime: 266 withdrew interview follow-up (213 electronic, 53 not electronic), 63 lost (59 electronic, 4 not), 177 did not take >=1 BP medicine at allocated time at 6 months among 1518 respondents. Morning: 244 withdrew (202 electronic, 42 not), 58 lost (56 electronic, 2 not), 53 did not take >=1 at allocated time among 1567 respondents. | Participant flow/adherence; `...pdf#page=4`, Figure 1. |
| S004 | Primary analysis is ITT/as-randomized Cox proportional hazards; most other outcomes use Cox or Poisson; non-survival analyses use available data without imputation; two-sided threshold P<.05. Per-protocol sensitivity excludes baseline beta-blocker or diuretic users (but not diuretic-nondiuretic combination users). | Analysis/model population; `...pdf#page=4` Statistical Analysis. |
| N012 | Narrative cohort summary: 56% female, median age 67; 18% diabetes, 11% CAD, 7% CKD; drug-class proportions ACE inhibitor 36%, ARB 30%, CCB 29%, diuretic 27%, combination pill 18%, beta-blocker 17%, other 1%. | Overall baseline summary; `...pdf#page=4` Results. Detailed arms in N013-N017. |
| N013 | Complete-loss/withdrawal: 101/3357 (3.0%), bedtime 57/1677 (3.4%), morning 44/1680 (2.6%). Active follow-up withdrawal/loss but administrative tracking: 530/3357 (15.8%), bedtime 272/1677 (16.2%), morning 258/1680 (15.4%). Median observation 4.6 years. | Follow-up population; `...pdf#page=4` Results. |

## Pages 5-6 — Table 1 baseline characteristics

All Table 1 values use randomized denominators bedtime n=1677 and morning n=1680 unless a category itself signals a smaller response denominator. Values below are `bedtime; morning`, exactly as displayed.

| ID | Directly observed quantitative relationship | Match key and exact source location |
|---|---|---|
| N014 | Age median (IQR), years: 67 (60-73); 67 (61-73). Age >=75: 370 (22.1%); 369 (22.0%). Sex: female 950 (56.6%); 943 (56.1%); male 727 (43.4%); 737 (43.9%). | Baseline Table 1; `...pdf#page=5`. |
| N015 | Race/ethnicity: Asian 42 (2.5%);34 (2.0%); Black 7 (0.4%);7 (0.4%); Hispanic/Latino 5 (0.3%);4 (0.2%); Indigenous 29 (1.7%);22 (1.3%); Southeast Asian/Indian 17 (1.0%);20 (1.2%); White 1565 (93.3%);1587 (94.5%); >1 race 9 (0.5%);5 (0.3%); declined 3 (0.2%);1 (<0.1%). | Baseline Table 1; self-selected categories; `...pdf#page=5`. |
| N016 | Province: Alberta 1200 (71.5%);1200 (71.4%); British Columbia 235 (14.0%);236 (14.0%); Manitoba 130 (7.8%);131 (7.8%); Ontario 74 (4.4%);75 (4.5%); Saskatchewan 38 (2.3%);38 (2.3%). Chronotype: early bird 881 (52.5%);859 (51.1%); night owl 477 (28.5%);495 (29.5%); neither 319 (19.0%);326 (19.4%). | Baseline Table 1; `...pdf#page=5`. |
| N017 | Smoking: 122 (7.3%);121 (7.2%). Exercise days median (IQR): 3 (0-5);3 (0-5); never exercises: 434 (25.9%);458 (27.3%). BMI median (IQR): 28.8 (25.7-33.0);28.9 (25.7-32.9). Physically frail: 299 (17.8%);307 (18.3%). EQ-5D-5L median (IQR): 80 (70-90);80 (75-90). | Baseline Table 1; `...pdf#page=5`. |
| N018 | Short Blessed Test: <=3: 1376 (82.1%);1403 (83.5%); 4-6: 248 (14.8%);224 (13.3%); 7-9: 33 (2.0%);29 (1.7%); >=10: 19 (1.1%);23 (1.4%); declined: 1 (<0.1%);1 (<0.1%). | Baseline Table 1; score 0-28 and interpretive footnote on `...pdf#page=6`. |
| N019 | Comorbidities (page 5): sleep apnea 377 (22.5%);341 (20.3%); diabetes 289 (17.2%);311 (18.5%); CAD 172 (10.3%);188 (11.2%). | Baseline Table 1; `...pdf#page=5`. |
| N020 | Comorbidities (continued): CKD 119 (7.1%);129 (7.7%); COPD 86 (5.1%);80 (4.8%); stroke 75 (4.5%);75 (4.5%); heart failure 28 (1.7%);32 (1.9%); hip fracture 22 (1.3%);27 (1.6%); none 876 (52.2%);877 (52.2%). | Baseline Table 1; `...pdf#page=6`. |
| N021 | Number of BP medicines: 1: 895 (53.4%);908 (54.0%); 2: 588 (35.1%);577 (34.3%); 3: 155 (9.2%);170 (10.1%); >=4: 39 (2.3%);25 (1.5%). | Baseline Table 1; `...pdf#page=6`. |
| N022 | BP medication type: ACE inhibitor 584 (34.8%);631 (37.6%); ARB 536 (32.0%);471 (28.0%); CCB 479 (28.2%);489 (29.1%); diuretic 446 (26.6%);472 (28.1%); combination pill 315 (18.8%);300 (17.9%); beta-blocker 289 (17.2%);278 (16.5%); other 26 (1.6%);21 (1.3%). | Baseline Table 1; `...pdf#page=6`. |
| N023 | Scale definitions: frailty score 0-8, >=3 physically frail; EQ-5D-5L range 0-100 and higher is better; BMI kg/m2; Short Blessed score 0-28, 5-9 questionable impairment and >=10 impairment consistent with dementia. | Baseline Table 1 footnotes; `...pdf#page=6`. |

## Page 6 — primary outcome, sensitivity analysis, and adherence

| ID | Directly observed quantitative relationship | Match key and exact source location |
|---|---|---|
| N024 | Event target was reduced before interim analysis from 406 to 255, then trial ended with 336 observed primary outcomes. | Event-target/timepoint narrative; `...pdf#page=6`. |
| S005 | ITT primary result repeats N003/S001: median 4.6 years each arm; 2.3 versus 2.4 events/100 patient-years; adjusted HR 0.96 (0.77-1.19), P=.70; unadjusted HR 0.94 (0.76-1.17); no reported PH-assumption violation. | Primary Cox analysis; `...pdf#page=6`. |
| S006 | Post hoc per-protocol sensitivity, no baseline beta-blocker/diuretic: bedtime n=1042, morning n=1023; median 4.7 years; rates 1.7 versus 1.8/100 patient-years; unadjusted HR 0.94 (0.68-1.28); adjusted HR 0.90 (0.65-1.23), P=.50. | Per-protocol comparison; `...pdf#page=6`. |
| N025 | Medication adherence: at 6 months, 83% of bedtime versus 95% of morning once-daily medicines taken as allocated; at least one once-daily medicine at allocated time: 88% versus 97%. Per-allocation medicines: 1% morning at lunch, 5% bedtime at dinner. At 72 months, at least one compliant medicine: 70% versus 88%. | Medication-level and participant-level adherence/timepoints; `...pdf#page=6`. |

## Page 7 — Figure 2, ABPM, quality of life, and discussion quantities

| ID | Directly observed quantitative relationship | Match key and exact source location |
|---|---|---|
| N026 | Figure 2 risk sets (years 0,1,2,3,4,5,6): bedtime 1677,1623,1514,1229,1002,674,245; morning 1680,1624,1506,1219,1000,667,263. Median follow-up: bedtime 4.6 (IQR 2.9-5.4), morning 4.6 (2.8-5.4) patient-years. | Composite event curve; `...pdf#page=7`, Figure 2. |
| S007 | Figure 2 adjusted HR 0.96 (0.77-1.19); unadjusted HR 0.94 (0.76-1.17). Adjusted Cox covariates: age, sex, frailty, smoking, non-BP medicines, EQ-5D-5L, prior-6-month hospitalization, HF, diabetes, CAD, stroke/TIA, CKD, dialysis, BMI >35/<20, sleep apnea, exercise days, province. | Primary outcome Cox model; `...pdf#page=7`, Figure 2 caption. |
| N027/S008 | Prespecified 24-hour ABPM sample: 151 per arm (302 total), median 9.6 months; stated 90% power to detect MAPEC overnight-systolic difference. Day systolic 133.8 vs 136.2 mm Hg, P=.15; day diastolic 75.2 vs 75.6, P=.72; overnight systolic 116.5 vs 123.9, difference -7.4 (95% CI -11.2 to -3.7), P<.001; overnight diastolic 62.9 vs 65.5, difference -2.7 (-4.9 to -0.4), P=.02. BP <130/80: 41.1% vs 32.5%, P=.12. | Bedtime vs morning ABPM; `...pdf#page=7`. |
| N028/S009 | One-year EQ-5D-5L (0-100): bedtime mean 78.9 (SD 15.2), morning 79.5 (SD 14.6), absolute difference -0.75 (95% CI -1.69 to 0.19), P=.12. | Secondary QoL; `...pdf#page=7`. |
| N029 | Contextual discussion figures: Spanish registry morning n=35,129, evening/bedtime n=6723, median 9.7 years; MAPEC/Hygia reported 61%/45% MACE and 57%/45% mortality reductions; cited Cochrane included trials total 3 deaths and 24 serious adverse events. | External comparison, not a BedMed endpoint; `...pdf#page=7`. |

## Page 8 — Table 2 primary, secondary, and safety outcomes

Table conventions: survival rows give events, median follow-up (IQR) patient-years, rate/100 patient-years, absolute rate difference, and HR (95% CI). Poisson rows give count/percentage or mean (SD), absolute percentage difference where printed, and RR (95% CI). Table footnote identifies HR rows; falling, syncope, lightheadedness, subjective vision worsening, cognitive decline, and new impairment as RR rows.

| ID | Directly observed quantitative relationship | Match key and exact source location |
|---|---|---|
| N030/S010 | Composite primary: bedtime 163 events, median 4.6 (2.9-5.4), rate 2.30; morning 173, 4.6 (2.8-5.4), 2.44; difference -0.14; HR 0.96 (0.77-1.19), P=.70. | Table 2 primary; `...pdf#page=8`. |
| N031/S011 | All-cause mortality: 81, 4.7 (3.1-5.5), 1.11 vs 94, 4.7 (3.1-5.5), 1.28; difference -0.18; HR 0.90 (0.67-1.22), P=.50. Stroke hospitalization/ED: 27, 4.7 (3.0-5.5), 0.37 vs 32, 4.7 (3.0-5.5), 0.44; -0.07; HR 0.86 (0.52-1.44), P=.57. MI/ACS hospitalization/ED: 48, 4.7 (3.0-5.5),0.67 vs 39,4.6 (2.9-5.5),0.54; +0.13; HR 1.25 (0.82-1.91), P=.30. HF hospitalization/ED: 30,4.7 (3.0-5.5),0.41 vs 43,4.7 (2.9-5.5),0.59; -0.18; HR 0.72 (0.45-1.15), P=.17. | Primary components; `...pdf#page=8`, Table 2. |
| N032/S012 | All-cause unplanned hospitalization/ED: 993, 2.2 (1.0-4.0),23.26 vs 1047,2.2 (0.9-3.9),25.15; -1.89; HR 0.93 (0.85-1.02), P=.10. | Secondary efficacy; `...pdf#page=8`, Table 2. |
| N033/S013 | Nonvertebral fracture: 152,4.5 (2.8-5.4),2.18 vs 166,4.5 (2.8-5.4),2.40; -0.22; HR 0.92 (0.74-1.14),P=.44. Hip fracture: 20,4.7 (3.0-5.5),0.27 vs 31,4.6 (2.9-5.5),0.43; -0.15; HR 0.65 (0.37-1.15),P=.14. | Postural-hypotension safety; `...pdf#page=8`, Table 2. |
| N034/S014 | Falling mean (SD) % of interviews: 4.9 (11.7) vs 5.0 (11.2); RR 0.96 (0.86-1.07),P=.47. Syncope: 0.6 (3.8) vs 0.6 (4.1); RR 1.28 (0.93-1.75),P=.12. Lightheadedness: 18.8 (25.2) vs 20.3 (26.2); RR 0.95 (0.90-1.00),P=.06. | Interview-level safety measures; `...pdf#page=8`, Table 2. |
| N035/S015 | New glaucoma: 43,4.7 (3.0-5.5),0.60 vs 39,4.6 (2.9-5.5),0.54; +0.06; HR 1.13 (0.73-1.74),P=.58. Subjective worsening vision: 420 (25.0%) vs 411 (24.5%); difference +0.5%; RR 1.02 (0.89-1.17),P=.74. | Vision safety; `...pdf#page=8`, Table 2. |
| N036/S016 | Cognitive decline at 18 months: 376/1446 (26.0%) vs 395/1493 (26.5%); difference -0.5%; RR 0.98 (0.85-1.13),P=.82. New impairment consistent with dementia: 89 (5.3%) vs 83 (4.9%); +0.4%; RR 1.12 (0.83-1.51),P=.48. Nursing-home admission: 38,4.7 (3.0-5.5),0.52 vs 26,4.7 (3.0-5.5),0.36; +0.17; HR 1.38 (0.83-2.27),P=.21. | Cognitive/nursing-home safety; `...pdf#page=8`, Table 2. |
| N037 | Definitions: subjective vision means "much worse" at any follow-up or "slightly worse" at >=2; cognitive decline means >=2-point Short Blessed change; nursing home is group living where participant no longer controls medicine timing. | Outcome label/scale definitions; `...pdf#page=8`, Table 2 footnotes. |

## Page 9 — Figure 3 subgroup effects

Figure 3 outcome is the composite primary outcome. First pair after each subgroup is bedtime/morning events, then displayed rate/100 patient-years, then HR (95% CI); P is interaction P. All CIs are unadjusted; interaction Cox includes the Figure 2 covariates, characteristic, and treatment-by-characteristic term.

| ID | Directly observed quantitative relationship | Match key and exact source location |
|---|---|---|
| S017 | All patients: 163/173 events; displayed rates 71.0/71.0; HR 0.96 (0.77-1.19). Sex: male 80/94,30.5/30.4, HR 0.81 (0.59-1.09); female 83/79,40.5/40.6, 1.17 (0.86-1.61); interaction P=.10. Age >=75: yes 77/81,14.9/14.5,0.92 (0.67-1.27); no 86/92,56.1/56.5,0.97 (0.72-1.31); P=.87. | Figure 3; `...pdf#page=9`. |
| S018 | Frailty: yes 47/50,12.4/12.7, HR 1.15 (0.75-1.76); no 116/123,58.6/58.3,0.88 (0.68-1.14); P=.22. Polypharmacy: yes 80/91,23.0/22.4,0.90 (0.66-1.22); no 83/82,48.0/48.6,1.03 (0.75-1.40); P=.49. Health score <=75: yes 91/77,28.5/25.1,1.11 (0.81-1.51); no 72/96,42.5/45.9,0.83 (0.61-1.13); P=.14. | Figure 3; `...pdf#page=9`. |
| S019 | Resistant hypertension: yes 33/46,7.7/7.0, HR 0.71 (0.45-1.14); no 130/127,63.3/64.0,1.06 (0.83-1.36); P=.07. Heart failure: yes 6/15,1.1/1.1,0.36 (0.10-1.25); no 157/158,69.8/69.9,1.00 (0.80-1.24); P=.16. Diabetes: yes 37/50,12.5/12.5,0.71 (0.45-1.12); no 126/123,58.5/58.5,1.08 (0.84-1.39); P=.05. | Figure 3; `...pdf#page=9`. |
| S020 | CAD: yes 38/46,7.0/7.3, HR 0.88 (0.55-1.39); no 125/127,63.9/63.7,0.97 (0.75-1.24); P=.93. Stroke/TIA: yes 16/25,4.6/4.8,0.78 (0.38-1.61); no 147/148,66.4/66.2,0.97 (0.77-1.23); P=.57. Sleep apnea: yes 37/38,16.0/14.4,0.76 (0.47-1.22); no 126/135,55.0/56.6,1.00 (0.78-1.28); P=.54. | Figure 3; `...pdf#page=9`. |
| S021 | CKD: yes 19/25,4.8/4.8, HR 1.12 (0.55-2.29); no 144/148,66.2/66.2,0.95 (0.76-1.20); P=.97. Sedentary: yes 50/60,17.7/18.3,0.88 (0.60-1.29); no 113/113,53.2/52.7,0.99 (0.76-1.29); P=.69. | Figure 3; `...pdf#page=9`. |
| S022 | ACE inhibitor: yes 54/78,24.4/25.8, HR 0.74 (0.52-1.05); no 109/95,46.6/45.2,1.14 (0.86-1.51); P=.05. ARB: yes 56/39,22.8/19.7,1.07 (0.70-1.64); no 107/134,48.2/51.3,0.93 (0.72-1.20); P=.44. Beta-blocker: yes 59/55,11.6/10.9,1.04 (0.71-1.52); no 104/118,59.4/60.1,0.91 (0.70-1.19); P=.54. | Figure 3; `...pdf#page=9`. |
| S023 | CCB: yes 64/75,19.2/19.8, HR 0.92 (0.65-1.30); no 99/98,51.7/51.2,0.99 (0.74-1.31); P=.66. Diuretic: yes 50/63,18.6/19.6,0.91 (0.62-1.33); no 113/110,52.4/51.4,0.97 (0.74-1.27); P=.43. Combination BP medicine: yes 20/23,14.1/13.4,0.95 (0.49-1.85); no 143/150,56.9/57.6,0.93 (0.74-1.17); P=.72. | Figure 3; `...pdf#page=9`. |

## Page 10 — reported limitations and conclusion

| ID | Directly observed quantitative relationship | Match key and exact source location |
|---|---|---|
| N038 | ABPM limitation: cohort 302 volunteers; 57% of invitees declined. Reported bedtime-minus-morning sleep systolic difference -7.4 mm Hg; cited systematic review -2.3 mm Hg and randomized crossover -1.7 mm Hg (nonsignificant). | ABPM interpretation; `...pdf#page=10`. |
| N039 | External comparison: TIME mortality 0.80/100 patient-years versus BedMed 1.20/100 patient-years, stated as 50% higher BedMed mortality. | Contextual rate comparison; `...pdf#page=10`. |
| S024 | Reported primary-CI interpretation: BedMed excluded HR <=0.76 and TIME <=0.82; BedMed planned 25% reduction threshold HR <=0.75. The article states no overlap with corresponding MAPEC/Hygia primary CI, but those CIs are not printed in this main paper. | CI/interpretation label; `...pdf#page=10`. |
| N040 | Trial recruited from 436 practices and had stated overall withdrawal/loss 3%. Conclusion restates no cardiovascular-risk reduction and no safety difference. | Trial conclusion; `...pdf#page=10`. |

## Pages 11-12 — no applicable main-result relationships

- **Page 11 reviewed:** author contributions, disclosures, funding, acknowledgments, and reference list. Numeric strings are publication/grant/reference details, not result-relevant trial quantities; no additional applicable main-paper relationship.
- **Page 12 reviewed:** continuation of reference list only. Numeric strings are bibliographic publication details; no additional applicable main-paper relationship.

## Cross-location matching index and extraction limitations

- **Primary outcome match:** N003/S001 (abstract, p1), S005 (narrative, p6), S007 (Figure 2, p7), N030/S010 (Table 2, p8), and S017 (Figure 3 all-patients row, p9). Exact rate precision differs only as 2.3/2.4 in prose/abstract versus 2.30/2.44 in Table 2; the table, narrative, and Figure 2 share adjusted HR 0.96 (0.77-1.19), while Figure 3 prints an outcome-rate column headed 71.0/71.0 despite the figure's `Rate per 100 patient-years` label. This map records the printed label/value without diagnosis.
- **Baseline match:** N002 (abstract), N012 (narrative), N014-N023 (Table 1); table values preserve arm-specific denominators and rounding.
- **Retention/adherence match:** N011 (Figure 1), N013 (narrative), N025 (narrative medication- and participant-level adherence). Population and timepoint distinctions are retained rather than assumed identical.
- **No OCR limitation:** native/layout extraction was readable for every page; no targeted rendering/OCR was necessary. Tables/Figures 1-3 were verified from fresh layout text and their explicit captions/footnotes. This artifact maps observations and does not make candidate determinations.

**Inventory totals:** 40 `N` relationships (N001-N040) and 24 `S` relationships (S001-S024), all mapped directly from DOC-001 pp.1-12; pp.11-12 explicitly reviewed as no-applicable-result units.
