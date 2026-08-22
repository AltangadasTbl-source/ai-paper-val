# Support quantitative extraction: DOC-004 and DOC-005

## Scope and method

- **DOC-004:** `joi200126supp3_prod_1607962892.5372.pdf`, PDF pages 1-20. Reused native page text was read for every page. Direct-PDF rendering was additionally inspected for pages 8-12 (all five figures) because those pages contain graphical values/labels not fully represented in text.
- **DOC-005:** `joi200126supp4_prod_1607962892.5372.pdf`, PDF page 1. Fresh direct `pdftotext` native and layout extraction was performed; the two outputs agree.
- **No workbook, spreadsheet, CSV, DOC, or DOCX unit is assigned.** No formula or cached workbook value applies.
- Locations below use source PDF page numbers. “Main-paper key” is a matching key, not an assertion that the matching main-paper occurrence has yet been adjudicated.

## Page-by-page evidence map

| Source page | Result-relevant content and definitions | Main-paper key / mapping note |
|---:|---|---|
| DOC-004 p.1 | Contents identifies eFigures 1-5 and eTables 1-6; no results beyond the index. | `SUPP03_CONTENTS` |
| p.2-3 | Assessments: baseline then 6- and 12-month visits; 24-hour pause before randomization; rate-control target resting HR <=100 bpm. Baseline and follow-up include ECG, QoL, 6MWD and NTproBNP; echo is repeated only at 12 months. | `ASSESSMENT_SCHEDULE`, `HR_TARGET` |
| p.4 | Digoxin dose 62.5-250 micrograms daily (default 125), loading dose twice daily dose on day 1; bisoprolol 1.25-15 mg daily (default 2.5). Uptitration visits: digoxin mean 1.4 (SD 0.6, range 1-3); beta-blocker mean 1.5 (SD 0.9, range 1-6). Combination treatment permitted for persistent HR >100 beats/min. | `TREATMENT_DOSE`, `UPTITRATION_VISITS`, `HR_TARGET` |
| p.5 | SF36 domains and PCS/MCS range 0-100; higher = better health; normalized presentation mean 50 using UK survey values, whereas SAP primary analysis used raw scores. SF36 MCID described as 0.5 SD and 4.1-9.2 in HF mortality-anchored work. EQ-5D VAS 0-100; index 0 (death)-1 (complete health), mapped to England EQ-5D-3L value set, MCID 0.18. AFEQT overall/subscales 0-100; higher = better QoL; 5-point change clinically important. | `QOL_SCALE_DEFINITIONS`, `SF36_PCS_6M_PRIMARY` |
| p.6 | Echo: three index beats averaged for LVEF and E/e′; index beat requires preceding minus pre-preceding RR interval <60 ms. Diastolic dysfunction: average E/e′ >=15, or if <15 then >=2 of IVRT <=65 ms, mitral E deceleration <=120 ms, average E/e′ >=11, PV diastolic deceleration <=220 ms. | `ECHO_DEFINITION` |
| p.7 | No result-relevant numeric result; names Q-station version 3.5 and Illustrator 23.1. | `NO_APPLICABLE_RESULT` |
| p.8, eFigure 1 | Flowchart: baseline, 6-month and 12-month visits; inclusion age >=60 years; permanent AF and symptomatic breathlessness NYHA class II or more. Exclusion includes HR <60 bpm, MI within last 6 months, decompensated HF within 14 days, and major surgery within 3 months. No participant counts are printed in the diagram. | `ELIGIBILITY`, `ASSESSMENT_SCHEDULE` |
| p.9, eFigure 2 | 12-lead ECG HR means with 95% CIs at baseline/end titration/6m/12m; figure text says no significant between-arm differences at any time point. End-uptitration 24-hour HR: digoxin 79 +/-11 vs beta-blocker 74 +/-11 beats/min, P=.020. Plot supports approximate 12-lead means already tabulated precisely in eTable 2. | `HR_12LEAD`, `HR_24H_UPTITRATION` |
| p.10, eFigure 3 | Prespecified 6-month SF36 PCS subgroup forest plot: eight subgroup mean differences/CIs and four interaction P values; direction axis: positive favors digoxin. Additional post-hoc baseline HR <100 vs >=100 subgroup interaction P=.80, non-significant. | `SF36_PCS_6M_SUBGROUP` |
| p.11, eFigure 4 | QoL figure. 6-month no significant arm differences. At 12 months visual labels: PF P=.05, RP P=.05, vitality P=.013, global health P=.049, EQ-5D VAS P=.038. Panel A normalized SF36 mean 50 UK population; Panel B raw SF36. Domain abbreviations/labels are defined. | `QOL_12M`, `SF36_SCALE` |
| p.12, eFigure 5 | NYHA Sankey denominators: digoxin baseline n=80, 6m n=76, 12m n=73; beta-blocker n=80, 6m n=74, 12m n=72. No baseline class I in either group. Mean-score adjusted difference (digoxin minus beta-blocker): 6m -0.55 (95% CI -0.73,-0.38), P<.001; 12m -0.58 (-0.76,-0.39), P<.001. Negative favors digoxin. | `NYHA_6M`, `NYHA_12M` |
| p.13, eTable 1 | Medication attendance, use, doses, range, levels and add-on agents at 6m/12m; values transcribed in numeric inventory. | `MEDICATION_6M`, `MEDICATION_12M` |
| p.14, eTable 2 | Resting and post-exertion HR means/SDs, Ns, adjusted differences/95% CIs/P values at 6m and 12m. Models adjust baseline score, gender, age, baseline mEHRA and LVEF; difference references beta-blocker. Footnote says higher values represent better QoL, an apparently generic label incongruent with heart-rate outcomes and flagged as candidate potential for human review. | `HR_TABLE_6M`, `HR_TABLE_12M` |
| p.15, eTable 3 | Normalized SF36 and EQ-5D means/SDs, adjusted differences/95% CIs/P values at 6m/12m. Same adjustment/reference definition; higher means better QoL. | `GENERIC_QOL_6M`, `GENERIC_QOL_12M` |
| p.16, eTable 4 | AFEQT means/SDs and adjusted differences/95% CIs/P values at 6m/12m. Same adjustment/reference definition; four subscales are post-hoc. | `AFEQT_6M`, `AFEQT_12M` |
| p.17, eTable 5 | Adverse-event patient counts/percentages, event counts, totals and at-least-one-event comparison. Numerator/percentage and event totals are transcribed below. | `ADVERSE_EVENTS_12M` |
| p.18, eTable 6 | Contextual prior-study table: N=716, 665, 200, 155, 102 and 30, with stated clinically important changes 4.8, 4, 8.9, 3.8 and 12; not RATE-AF trial results. | `CONTEXT_SF36_LITERATURE` |
| p.19-20 | References only; publication years, volumes and pages are bibliographic, not trial-result evidence. | `NO_APPLICABLE_RESULT` |
| DOC-005 p.1 | Data Sharing Statement: data available “No”; requests directed to sponsor through corresponding author, subject to a data-use agreement. No result-relevant quantitative relationship, statistic, table, figure, formula, or data value. | `NO_APPLICABLE_RESULT` |

## Exact tables and graphical values

### eTable 1 (DOC-004 p.13): medication use

| Arm / measure | 6 months | 12 months |
|---|---:|---:|
| Digoxin: attended | 76 | 73 |
| Digoxin: still receiving digoxin | 73 (96.1%) | 70 (95.9%) |
| Digoxin dose, mean micrograms (SD) | 160.5 (55.4) | 158 (57) |
| Digoxin dose range, micrograms | 62.5-250 | 62.5-250 |
| Digoxin level, mean micrograms/L (SD) | 0.78 (0.31) | 0.72 (0.27) |
| Digoxin + diltiazem | 3 (3.9%) | 5 (6.8%) |
| Beta-blocker: attended | 74 | 72 |
| Beta-blocker: still receiving bisoprolol | 59 (79.7%) | 58 (80.6%) |
| Bisoprolol dose, mean mg (SD) | 3.2 (1.8) | 3.3 (2.1) |
| Bisoprolol dose range, mg | 1.0-10.0 | 1.0-10.0 |
| Any beta-blocker | 66 (89.2%) | 65 (90.3%) |
| Other beta-blocker: nebivolol | 7 (9.5%) | 7 (9.7%) |
| Beta-blocker + diltiazem | 1 (1.4%) | 1 (1.4%) |

### eTable 2 (DOC-004 p.14): heart rate

All entries are mean (SD) beats/min unless stated; group order is digoxin, beta-blocker. Baseline Ns, then follow-up Ns, are printed in headers.

| Outcome | Baseline | 6m | 6m adjusted difference (95% CI), P | 12m | 12m adjusted difference (95% CI), P |
|---|---|---|---|---|---|
| 12-lead ECG | 100.3 (16.8), 99.2 (19.2) (n=80,80) | 76.9 (12.1), 74.8 (11.6) (n=76,74) | 1.5 (-2.0,5.1), .40 | 75.4 (9.9), 74.3 (11.2) (n=73,72) | 0.3 (-3.0,3.5), .87 |
| Apex, 30 sec | 98.3 (15.1), 99.0 (16.8) | 78.4 (10.5), 76.2 (11.1) | 2.1 (-1.1,5.3), .20 | 78.3 (9.2), 76.2 (10.6) | 1.7 (-1.3,4.7), .26 |
| Radial, 30 sec | 87.8 (12.0), 86.9 (10.3) | 76.2 (9.7), 73.9 (10.8) | 1.8 (-1.5,5.1), .29 | 76.0 (9.0), 73.8 (10.0) | 1.5 (-1.7,4.6), .35 |
| Peripheral pulse deficit | -10.3 (9.4), -12.1 (12.0) | -2.3 (3.9), -2.3 (4.2) | 0.1 (-1.2,1.5), .83 | -2.3 (5.1), -2.3 (3.2) | 0.4 (-1.1,1.8), .60 |
| Post-walk radial, 30 sec | 99.9 (19.6),103.7 (20.2) (n=80,79) | 90.5 (19.1),89.8 (18.2) (n=74,73) | 1.2 (-5.0,7.5), .70 | 90.1 (15.9),87.3 (15.2) (n=71,69) | 2.2 (-3.3,7.7), .43 |
| Post-walk minus resting radial | 12.1 (17.8),16.8 (20.7) | 14.3 (19.6),15.8 (16.4) | -0.8 (-7.0,5.3), .79 | 13.9 (13.8),13.7 (15.4) | 0.1 (-5.1,5.4), .96 |

### eTables 3-4 (DOC-004 pp.15-16): adjusted QoL effects

The displayed measure is adjusted mean difference, digoxin minus beta-blocker, with 95% CI and P. Means/SDs are in the numeric inventory; the exact adjustment formula is baseline score + gender + age at randomization + baseline mEHRA + LVEF.

| Outcome | 6m difference (95% CI), P | 12m difference (95% CI), P |
|---|---|---|
| SF36 PCS | 1.4 (-1.1,3.8), .28 | 1.6 (-1.4,4.7), .29 |
| SF36 MCS | 0.7 (-2.4,3.8), .67 | 1.4 (-1.5,4.2), .34 |
| Physical functioning | 1.3 (-1.4,4.0), .36 | 2.8 (0.0,5.7), .05 |
| Role physical | 2.5 (-0.8,5.8), .14 | 3.4 (0.0,6.9), .05 |
| Bodily pain | 0.2 (-3.0,3.3), .92 | -2.6 (-6.2,1.1), .16 |
| Global health | 1.3 (-1.2,3.8), .30 | 2.8 (0.0,5.6), .05 |
| Vitality | 0.8 (-2.2,3.7), .61 | 3.9 (0.8,7.0), .01 |
| Social function | 2.0 (-1.3,5.3), .23 | 0.9 (-2.7,4.5), .62 |
| Role emotional | 2.9 (-1.2,7.0), .16 | 3.7 (-0.6,8.1), .09 |
| Mental health | -1.1 (-4.2,2.1), .50 | -1.0 (-3.6,1.7), .47 |
| EQ-5D index | -0.01 (-0.08,0.06), .80 | 0.01 (-0.06,0.09), .72 |
| EQ-5D VAS | 3.6 (-1.3,8.5), .15 | 5.5 (0.3,10.6), .04 |
| AFEQT overall | 3.5 (-1.0,7.9), .13 | 4.1 (-0.5,8.7), .08 |
| AFEQT symptoms (post-hoc) | 2.4 (-2.0,6.8), .29 | 1.0 (-3.7,5.7), .67 |
| AFEQT daily activities (post-hoc) | 7.1 (0.9,13.3), .025 | 9.4 (2.9,15.9), .005 |
| AFEQT treatment concern (post-hoc) | 1.1 (-4.6,6.7), .71 | -0.2 (-5.3,5.0), .95 |
| AFEQT treatment satisfaction (post-hoc) | 7.0 (1.4,12.7), .015 | 8.8 (3.3,14.3), .002 |

### eTable 5 (DOC-004 p.17): adverse-event table

Each cell is patients n (%), event n. Digoxin / beta-blocker / total respectively: gastrointestinal upset 5 (6%),5 / 8 (10%),8 / 13 (8%),13; blurred vision 2 (2%),2 / 1 (1%),1 / 3 (2%),3; rash 1 (1%),1 / 0 (0%),0 / 1 (1%),1; peripheral edema 1 (1%),1 / 11 (14%),12 / 12 (7%),13; symptomatic bradycardia 0 (0%),0 / 5 (6%),5 / 5 (3%),5; dizziness 4 (5%),4 / 24 (30%),28 / 28 (17%),32; headache 5 (6%),5 / 9 (11%),11 / 14 (9%),16; lethargy 7 (9%),7 / 30 (38%),37 / 37 (23%),44; upper respiratory symptoms 1 (1%),1 / 13 (16%),15 / 14 (9%),16; symptomatic hypotension 0 (0%),0 / 6 (8%),7 / 6 (4%),7; other 3 (4%),3 / 15 (19%),18 / 18 (11%),21. Total events: 29 / 142 / 171. Patients with >=1 event: 20 (25%) / 51 (64%) / 71 (44%); chi-square group comparison P<.001.

## Candidate potential retained for downstream checking (not candidate IDs)

1. **DOC-004 p.14 eTable 2 footnote a:** models are heart-rate models, but its final sentence says “higher values represent better quality of life in the digoxin arm.” Comparator/rule: the outcome labels and units are beats/min, whereas this copied interpretation is QoL-specific. Potential category: measure/label inconsistency; requires exact matched footnote comparison with eTables 3-4 and main-paper heart-rate table.
2. **DOC-004 p.11 vs p.15 visual/table P labels:** the figure prints .013/.049/.038 for vitality/global health/EQ-5D VAS, while eTable 3 prints .01/.05/.04. The difference may be ordinary display precision, so no contradiction is asserted; downstream must determine the source-specific rounding rule and matched model/time point.

