# Support Quantitative Evidence Mapping

## Scope and evidence boundary

Complete mapping of DOC-002 `joi170166supp1_prod.pdf` (protocol, PDF pp. 1-32), DOC-003 `joi170166supp2_prod.pdf` (SAP, PDF pp. 1-9), and DOC-004 `joi170166supp3_prod.pdf` (online supplement, PDF pp. 1-27). Current-run native and layout text were used throughout. DOC-004 pp. 3-16 are image-only in the current PDF extraction and were read only through the user-authorized, SHA-matched existing OCR record described in `evidence_asset_inventory.md`; no OCR was run. DOC-004 pp. 17-27 were also visually confirmed in current-run renders.

This is an evidence map, not candidate adjudication. “Reported” refers to content printed in the support source; protocol/SAP values are planned-design values unless explicitly reported as results in DOC-004.

## DOC-002 — protocol

### Result-relevant design and endpoint definitions

- **PDF p. 6-7:** cluster-randomized stepped-wedge trial. Five steps; four-month baseline; cohorts 2-5 implement at months 8, 12, 16, and 20; total duration 2 years. Figure 1 labels `n = 12-14 hospitals per cohort`; study summary states 60-70 clinics/hospitals and 15,750 subjects. Primary outcome is 30-day MACE rate, compared before/after implementation while accounting for hospital, cohort, and time cluster effects.
- **PDF p. 9:** primary endpoint is the 30-day composite major adverse event rate: death, myocardial infarction, stroke, and major GUSTO bleeding. Secondary domains: 30-day health-related quality of life (SAQ), economic effects, medication prescription rates, healthy-lifestyle discharge advice, and in-hospital/30-day expanded MACE. Eligible patients have STEMI or NSTEMI.
- **PDF p. 10:** age eligibility is 18 years or older. Five steps are planned over two years; minimum four-month all-hospital baseline; subsequent cohort implementation at 4, 8, 12, 16, and 20 months. A 2,200-patient subset is asked to complete SAQ and micro-economic assessment.
- **PDF pp. 12-13:** in-hospital database entry is within 7 days of discharge; 30-day follow-up/SAQ/economic data entry is within 48 hours of contact. Follow-up is 30 days after hospitalization and no further.
- **PDF p. 18:** repeats the primary MACE definition and lists secondary endpoints. Sample-size design: alpha 0.05; 15,000 anticipated patients; 80% power to detect 2.4% difference from baseline 10.4% 30-day MACE; increased to 15,750 for up to 5% loss between discharge and 30-day follow-up. These are protocol design parameters, not outcomes.
- **PDF p. 19:** one interim analysis is planned, including enrollment and serious adverse events; DSMB has five named members.
- **PDF p. 21:** 5% source-document audit and separate random 5% sample of discharged patients for existence confirmation; data supplied biweekly and aggregated quarterly. These are monitoring quantities, not trial outcomes.
- **PDF pp. 25-26:** consent text restates 30-day contact, 15,750 hoped-for enrolment, approximately 30-minute contact, and the two optional survey domains.

### Page-complete record

| PDF pages | Mapping disposition |
|---|---|
| 1-5 | Title, administrative material, contents, abbreviations, and headings only; no result-relevant quantitative relationship beyond document identity. |
| 6-7 | Stepped-wedge schedule, hospital/subject targets, endpoint/model definition mapped above. |
| 8 | Background/rationale only; no source-specific result relationship. |
| 9-10 | Objectives, endpoint, eligibility, schedule, 2,200 subset mapped above. |
| 11 | Treatment-plan narrative; no additional quantitative relationship. |
| 12-13 | Data capture and 30-day follow-up definitions/timings mapped above. |
| 14-17 | Time/events, withdrawals, adverse-event definitions and reporting logistics; no reported result or additional inferential parameter. |
| 18-19 | Endpoint repetition, sample-size parameters, one interim analysis, five-member DSMB mapped above. |
| 20 | Consent/privacy administration; no result relationship. |
| 21 | 5%/5% audit and reporting frequencies mapped above. |
| 22-24 | Administration, retention, references; no result-relevant relationship. |
| 25-30 | Consent forms; pp. 25-26 contain 30-day/15,750/30-minute quantitative repeats mapped above; remaining pages have form signatures/contact templates only. |
| 31-32 | Contact-detail templates only; no applicable result relationship. |

## DOC-003 — SAP

### Analysis and endpoint definitions

- **PDF pp. 2-3:** primary objective/outcome is 30-day MACE; cluster-randomized stepped-wedge design with five steps, four-month baseline, implementation at months 8/12/16/20 for later cohorts, and one planned interim comparison. Figure 2 says `n = 12 hospitals per cohort` (a planned design label).
- **PDF p. 4:** sample-size parameters: STATA v12; ICC 0.05; alpha 0.05; 15,000 patients; 80% power; 2.4% detectable difference; 10.4% baseline 30-day MACE; 15,750 after allowing up to 5% dropout. Primary MACE = all-cause death, MI, stroke, and GUSTO major bleeding.
- **PDF p. 5:** secondary endpoints define medication composites and a 2,200-subject sub-study. “Concordance” is >80% of recommended drugs (in-hospital and discharge) in its association analysis.
- **PDF p. 6:** intention-to-treat includes all database-recorded patients during the 24-month period; intervention exposure follows randomization; random-effects models address within-cluster correlation. Continuous summaries: n, mean, SD, median, minimum, maximum; categorical: n and %. Missing 30-day data arise after outpatient follow-up or three telephone attempts and are planned for complete-case and multiple-imputation sensitivity analyses.
- **PDF p. 7:** primary analysis is mixed-effects logistic regression for 30-day MACE, with random hospital effects and fixed time effect within every four-month period. Baseline is tabulated by implementation order, 12 clusters in 5 groups. Prespecified participant subgroup cut-points: age <65 and >65 years; sex; STEMI versus NSTEMI. Secondary binary endpoints use mixed-effects logistic regression.
- **PDF p. 8:** interim efficacy analysis after one year. O’Brien-Fleming boundaries: interim `z=2.797`, `p<0.005`; final `z=1.977`, `p<0.048`. Serious/unanticipated events are captured; safety reports semi-annually.

### Page-complete record

| PDF pages | Mapping disposition |
|---|---|
| 1 | Title/version/approval page; no result-relevant relationship. |
| 2-3 | Objectives and stepped-wedge schedule/primary outcome mapped above. |
| 4 | Sample size, endpoint definition, ICC and power parameters mapped above. |
| 5 | Secondary endpoints, composite definitions, 2,200 sub-study and >80% concordance mapped above. |
| 6 | ITT population, descriptive conventions, missingness definition and sensitivity methods mapped above. |
| 7 | Primary model, time period, cluster design and subgroup definitions mapped above. |
| 8 | Secondary modeling and interim z/P thresholds mapped above. |
| 9 | DSMB administrative frequency (at least once per year); no additional result relationship. |

## DOC-004 — online supplement

### eAppendix / toolkit (PDF pp. 1-16)

- **p. 1-2:** supplement title and eAppendix title; no outcome table.
- **pp. 3-4 (authorized OCR):** sample audit-feedback report template, aggregation date Dec 31, 2014 11:59:59 PM and publish date Jan 10, 2015; inclusion summary contains example quarterly counts/labels but is a template/sample report, not the trial analytic dataset.
- **p. 5 (authorized OCR):** R3M means three consecutive months; inclusion status Yes includes a month in aggregated/comparison statistics and No excludes it. Median/50th percentile, 90th percentile, and box-and-whisker definitions are stated.
- **pp. 6-9 (authorized OCR):** toolkit sample defines composite/performance measures as proportions of eligible opportunities met. It lists 11 acute/discharge measures, 11 STEMI measures, 8 NSTEMI measures, and 6 discharge measures; individual measures include aspirin, beta blocker, statin, LV function, ACE-I/ARB for LVSD, thrombolysis within 30 minutes, primary PCI within 90 minutes, median arrival-to-PCI time, reperfusion, smoking advice, and cardiac-rehabilitation referral. Page 9 defines door-to-last-ECG metric as proportion of AMI patients with ECG within 10 minutes of arrival. OCR-derived display values on these template charts are not used as trial-outcome values because their visual labels/denominators are not source-confirmed.
- **pp. 10-14 (authorized OCR):** template participant graphs and care metrics; visual values are not mapped as outcome estimates because source image evidence was not freshly rendered and OCR is insufficiently reliable for exact plotted numbers. Labels cover admissions, age, sex, arrival/ECG times, medications, procedures, reperfusion, clinical events, bleeding, and discharge medication.
- **pp. 15-16 (authorized OCR):** admission/discharge checklists specify 5-minute ECG completion and 5-minute physician interpretation targets, aspirin 325 mg admission then 75 mg daily, alternative P2Y12 doses (clopidogrel 600 mg then 75 mg daily; prasugrel 60 mg then 10 mg daily; ticagrelor 180 mg then 90 mg twice daily), nitroglycerin 0.4 mg SL every 5 min PRN with repeat x2, and EF <40% ACE-I/ARB condition. These are care-toolkit instructions, not results.

### eTable 1 — complete versus missing 30-day follow-up (PDF p. 17)

Groups are complete follow-up `n=21,079` and missing follow-up `n=295`; difference column is printed as intervention minus control (as labelled, although its group labels are complete/missing). All following values are `complete; missing; printed difference (95% CI)`: age years `60.6 (12.1); 60.0 (11.6); -0.6 (-2.0 to 0.8)`; male `15,973 (75.8%); 210 (71.2%); -4.6 (-9.8 to 0.6)`; tobacco `6,489 (30.8%); 125 (42.4%); 11.6 (5.9 to 17.3)`; diabetes `9,351 (44.4%); 133 (45.1%); 0.7 (-5.0 to 6.4)`; transferred `8,270 (39.2%); 131 (44.4%); 5.2 (-0.5 to 10.9)`; no insurance `15,322 (72.7%); 220 (74.6%); 1.9 (-3.1 to 6.9)`; STEMI `13,514 (64.1%); 175 (59.3%); -4.8 (-10.4 to 0.9)`; symptom-to-door min median (IQR) `246 (119-830); 266 (110-915); 21 (-38 to 80)`; weight kg `63.5 (9.7); 62.6 (9.3); -0.9 (-2.0 to 0.2)`; systolic BP mmHg `138.5 (28.9); 138.9 (32.5); 0.4 (-2.9 to 3.7)`; heart rate bpm `79.9 (18.9); 82.9 (19.1); 3.0 (0.8 to 5.2)`; troponin ng/ml median (IQR) `1.3 (0.3-5.7); 4.6 (0.9-32.0); 3.3 (0.1 to 6.5)`; LDL mg/dl `122.4 (40.8); 131.4 (46.0); 9.0 (3.2 to 14.8)`; triglycerides mg/dl median (IQR) `121 (89-165); 128 (93-186); 7 (-3 to 17)`; creatinine mg/dl median (IQR) `1.0 (0.9-1.2); 1.0 (0.9-1.3); 0.1 (-0.2 to 0.3)`; glucose mg/dl median (IQR) `127 (102-176); 128 (107-188); 1 (-6 to 8)`; hemoglobin mg/dl `13.2 (2.0); 13.2 (2.1); 0.0 (-0.3 to 0.2)`.

### eTable 2 — marginal baseline effects (PDF p. 18)

Control `n=10,066`, intervention `n=11,308`; values are control; intervention; difference (intervention-control, 95% CI): age years `60.7 (60.0,61.3); 60.7 (60.1,61.3); 0.0 (-0.5 to 0.6)`; male `%` `75.3 (73.2,77.4); 75.7 (73.8,77.6); 0.4 (-1.6 to 2.4)`; tobacco `%` `30.9 (27.2,34.5); 29.1 (25.6,32.6); -1.8 (-3.9 to 0.4)`; diabetes `%` `45.4 (42.6,48.2); 47.9 (45.2,50.6); 2.5 (0.1 to 4.8)`; transferred `%` `28.5 (23.4,33.5); 35.2 (29.7,40.7); 6.7 (4.8 to 8.7)`; no insurance `%` `78.5 (72.5,84.5); 78.0 (72.0,84.0); -0.5 (-2.1 to 1.1)`; STEMI `%` `66.5 (60.7,72.3); 64.7 (58.8,70.5); -1.8 (-3.7 to 0.2)`; symptom-door min `243 (193,293); 265 (162,368); 22 (-82 to 126)`; weight kg `64.6 (63.8,65.5); 63.7 (62.9,64.6); -0.9 (-1.4 to -0.5)`; SBP mmHg `140.0 (137.7,142.2); 139.4 (137.3,141.6); -0.6 (-1.9 to 0.8)`; heart rate bpm `80.7 (79.6,81.8); 80.9 (79.8,81.9); 0.2 (-0.7 to 1.1)`; troponin `1.7 (0.9,2.5); 1.1 (0.8,1.5); -0.6 (-1.3 to 0.1)`; LDL `124.0 (121.0,127.0); 122.5 (119.6,125.4); -1.5 (-3.8 to 0.8)`; triglycerides `121 (109,133); 121 (113,130); 1 (-11 to 12)`; creatinine `1.0 (0.9,1.1); 1.0 (1.0,1.0); 0.0 (-0.1 to 0.1)`; glucose `124 (114,134); 130 (125,135); 6 (-3 to 14)`; hemoglobin `13.2 (13.1,13.4); 13.2 (13.0,13.3); 0.0 (-0.1 to 0.1)`. Difference is from mixed-effects logistic, linear, or quantile regression with random hospital effect and temporal-trend term.

### eTables 3-4 — baseline by step (PDF pp. 19-20)

- **eTable 3, p. 19:** ten displayed step/group columns: step 1 control `2915`; step 2 control/intervention `2649/662`; step 3 `2251/1265`; step 4 `1422/2432`; step 5 `829/3214`; step 6 intervention `3735`. It provides all listed baseline characteristics by column: age, male, tobacco, diabetes, transfer, insurance, STEMI, symptom-door time, weight, SBP, heart rate, troponin, LDL, triglycerides, creatinine, glucose, hemoglobin. Serum creatinine is NA in step 1 and step 2 control/intervention; all later values are printed. Full cell values are preserved in the current-run layout text at this PDF page.
- **eTable 4, p. 20:** step denominators `2915, 3311, 3516, 3854, 4043, 3735` for steps 1-6. It gives the same 17 baseline characteristics, using mean (SD), n (%), or median (IQR) as labelled. It explicitly says serum creatinine was not collected until step 3; values for steps 1-2 are `NA`. Full row values are in the current-run layout text at this page.

### eTables 5-7 — adjusted outcomes (PDF pp. 21-23)

- **eTable 5, p. 21:** OR (95% CI) under four sensitivity adjustments (GRACE covariates; transfer status; insurance; prehospital aspirin). In that order: 30-day MACE `1.06 (0.77-1.44); 0.98 (0.80-1.21); 0.97 (0.79-1.20); 0.99 (0.80-1.22)`; mortality `0.98 (0.67-1.43); 0.94 (0.74-1.19); 0.93 (0.73-1.18); 0.95 (0.75-1.20)`; CV mortality `1.00 (0.68-1.47); 0.94 (0.74-1.19); 0.93 (0.73-1.18); 0.95 (0.75-1.20)`; in-hospital mortality `1.07 (0.65-1.76); 0.92 (0.70-1.22); 0.91 (0.69-1.20); 0.93 (0.71-1.23)`; reinfarction `1.39 (0.74-2.60); 1.38 (0.86-2.21); 1.39 (0.87-2.22); 1.40 (0.87-2.24)`; stroke `0.93 (0.46-1.89); 1.23 (0.70-2.14); 1.21 (0.70-2.12); 1.23 (0.70-2.15)`; GUSTO bleed `2.90 (0.77-10.87); 2.33 (0.93-5.88); 2.26 (0.89-5.71); 2.35 (0.93-5.92)`; optimal in-hospital medication `2.19 (1.83-2.62); 1.47 (1.29-1.66); 1.45 (1.28-1.64); 1.47 (1.30-1.66)`; optimal discharge medication `1.50 (1.27-1.78); 1.61 (1.42-1.82); 1.61 (1.43-1.83); 1.61 (1.42-1.82)`; tobacco advice `0.84 (0.42-1.67); 1.05 (0.67-1.66); 1.05 (0.66-1.66); 1.07 (0.68-1.69)`. Footnotes define GRACE covariates, GUSTO bleed, medication composites, smoker denominator, and MACE.
- **eTable 6, p. 22:** clustering/temporal trend/time-exposure interaction OR (95% CI): MACE `1.14 (0.76-1.70)`; mortality `0.98 (0.63-1.52)`; CV mortality `1.00 (0.64-1.56)`; in-hospital mortality `1.43 (0.83-2.46)`; reinfarction `2.81 (0.79-9.94)`; stroke `2.06 (0.58-7.36)`; GUSTO bleeding `2.53 (0.50-12.94)`; in-hospital medication `0.87 (0.70-1.07)`; discharge medication `1.45 (1.12-1.88)`; tobacco advice `0.99 (0.37-2.66)`. Footnotes define the same composite denominators and MACE.
- **eTable 7, p. 23:** control/intervention `N=10,066/11,308`; event data and models: MACE plus incident HF/shock/arrest `919 (9.1%)/795 (7.0%); cluster RD -0.86 (-1.72,-0.01), OR 0.89 (0.80,1.00); primary RD -1.34 (-2.72,0.04), OR 0.84 (0.70,1.00); ICC 0.15`; HF `227 (2.3%)/191 (1.7%); -0.03 (-0.45,0.40), 0.99 (0.79,1.24); -0.52 (-1.22,0.17), 0.76 (0.54,1.07); ICC 0.23`; shock `217 (2.2%)/170 (1.5%); -0.06 (-0.42,0.30), 0.96 (0.77,1.21); -0.20 (-0.80,0.40), 0.89 (0.62,1.27); ICC 0.25`; arrest `206 (2.0%)/237 (2.1%); 0.16 (-0.31,0.62), 1.08 (0.87,1.33); -0.20 (-0.94,0.55), 0.91 (0.65,1.28); ICC 0.20`. OR is intervention versus control; RD is intervention minus control; mixed-effects logistic models use hospital random effect, with temporal trends additionally in primary analysis.

### eFigures (PDF pp. 24-27)

- **p. 24, eFigure 1A:** residuals and 95% CIs for hospital MACE rate, by five cohorts. Residual is hospital departure from mean MACE rate (zero = mean); CI not crossing zero differs at 5% level; left is lower and right higher MACE. Model is multilevel mixed-effects logistic regression with hospital random effect and temporal-trend adjustment.
- **p. 25, eFigure 1B:** unadjusted within-hospital difference in 30-day MACE rate, displayed as `Control - Intervention, %`; bubble size is participant count; cohorts 1-5 labelled. Plot scale is -50 to 25% and hospital rank order roughly 0-60; individual plotted values are graphical and no exact data labels are printed.
- **p. 26, eFigure 2A:** unadjusted 30-day MACE % with 95% CIs by hospital, cohort, intervention/control and steps 0-5; each point is one hospital. Values are graphical without printed exact labels.
- **p. 27, eFigure 2B:** same display structure for 30-day mortality % with 95% CIs; values are graphical without printed exact labels.

### DOC-004 page-complete record

| PDF pages | Mapping disposition |
|---|---|
| 1-2 | Title/eAppendix title; no applicable numerical result. |
| 3-16 | Authorized OCR only; toolkit/sample-report definitions, dates, targets and template limitations mapped above. |
| 17 | eTable 1 all displayed baseline/follow-up values mapped above. |
| 18 | eTable 2 all displayed marginal effects/CI/model definition mapped above. |
| 19 | eTable 3 all baseline grid characteristics mapped; full cells in current-run layout source. |
| 20 | eTable 4 all baseline grid characteristics and serum-creatinine collection definition mapped. |
| 21-23 | eTables 5-7 all adjusted outcome values, effect measures, intervals, denominators and footnotes mapped above. |
| 24-27 | eFigures 1A-2B labels, direction/scales, models and graphical-value limitations mapped above. |

