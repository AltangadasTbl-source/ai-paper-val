# Main quantitative evidence mapping

## Scope, provenance, and coverage

Assigned and completed: DOC-001, `jama_huffman_2018_oi_170166.pdf`, physical pages 1–12 (printed pages 567–578), document role REPORT. Source SHA-256: 11311a6bb5c7a4be734ed60776b308f525ad101671ccc8d34bab18735aaca5f5. This is a fresh reconstruction from source-linked evidence assets, with no prior candidate or report conclusions used. Scope and contract were read completely. Source inventory, evidence inventory, source coverage, coverage manifest, and tooling record were read. No supplied source or reused asset was modified.

Reused native and layout text: `.ai_paper_validation/review_1_5_2/preprocessing/native_text/jama_huffman_2018_oi_170166.txt` and `.ai_paper_validation/review_1_5_2/preprocessing/layout_text/jama_huffman_2018_oi_170166.txt`. Engines: historical Poppler pdftotext; curator confirms current native text reproduction with Poppler 25.03.0. Physical page boundaries were read with awk form-feed records. Reused rendered images DOC-001-04.png through DOC-001-09.png were visually inspected; historic engine pdftoppm, 180 dpi, under `.ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/`. These resolve rotated flow and graph structure and table alignment. No new extraction derivative, OCR, fallback environment, or GPU use was required.

All links below are relative to this artifact's directory and identify physical source pages. Numeric IDs N001–N189 are local main-mapping identifiers. Statistical keys S001–S154 cross-reference the rows rather than duplicate evidence. Support mapping IDs are a separate namespace until merged by the coordinator. A row may contain several printed quantities belonging to the same result. Figure 2 has 60 distinct cohort-step-outcome relationships even though compact vectors share one row per cohort. No diagnosis or judgment is made here.

| Physical page | Printed page | Complete inspected content | Mapping | Status |
|---:|---:|---|---|---|
| 1 | 567 | Abstract design, group and step counts, primary result, population | N001–N006; S001 | COMPLETE |
| 2 | 568 | Key Points, background numeric context, design, randomization | N007–N009; S002 | COMPLETE |
| 3 | 569 | Intervention allocation, endpoint definitions, statistical methods and decision rules | S003–S008 | COMPLETE |
| 4 | 570 | Figure 1, all 20 flow boxes, legend and caption | N021–N040 | COMPLETE |
| 5 | 571 | Table 1, all 27 rows and footnotes; recruitment/exclusion and monitoring narrative | N010–N015; N041–N067; S009–S035 | COMPLETE |
| 6 | 572 | Table 2, all 21 rows and footnotes; baseline and process narrative | N016–N020; N068–N088; S036–S056; N173–N176; S093 | COMPLETE |
| 7 | 573 | Table 3, all 10 rows and footnotes; process and primary-result narrative | N089–N098; S057–S076; N177–N186 | COMPLETE |
| 8 | 574 | Figure 2, 60 markers and intervals, repeated 30 denominators per panel; secondary/post hoc text | N113–N172; N187–N189; S091,S094–S154 | COMPLETE |
| 9 | 575 | Figure 3, all 14 rows, axes/caption; expanded endpoint and discussion | N099–N112; N189; S077–S092 | COMPLETE |
| 10 | 576 | Discussion quantitative context, limitations, conclusions | N008; S008; narrative match keys | COMPLETE |
| 11 | 577 | Administrative material, contributors, disclosures, funding, references 1–11 | No additional applicable trial-result relationship | COMPLETE; NO_APPLICABLE_NEW_RESULT |
| 12 | 578 | References 12–26 | No additional applicable trial-result relationship | COMPLETE; NO_APPLICABLE_NEW_RESULT |

Coverage: 12 total, 12 reusable-backed, 0 fresh-required, 12 mapped. Scientific gaps: none. Derivative limitation: Figure 2 supplies graphical point estimates and 95% CI bars without printed numeric labels. All 60 are mapped below; approximate coordinates are expressly graphical readings, not exact source numerals. Exact numeric graph coordinates cannot be extracted from printed text. No person-time denominator, hazard ratio, relative risk, or reported standard error is present. The only reported P value is the incomplete-follow-up comparison P < .001; statistical decision rules also print alpha levels and z boundaries.

## Population, time, model, and decision keys

| Key | Exact source | Reconstruction |
|---|---|---|
| S001 | [Abstract](../../../jama_huffman_2018_oi_170166.pdf#page=1) | Main primary result: 30-day all-cause death, reinfarction, stroke, or major bleeding; intervention versus control; mixed-effects logistic regression accounting for clustering and temporal trends. Abstract conclusion: intervention did not decrease the composite. |
| S002 | [Design and randomization](../../../jama_huffman_2018_oi_170166.pdf#page=2) | Hospital-level cluster randomized stepped-wedge trial; 63 hospitals; five predefined 4-month crossover steps over 24 months, after usual care. Enrollment November 10, 2014–November 9, 2016; follow-up last date December 31, 2016. Central computer randomization, strata projected enrollment ≤200, 201–500, 501–1000, >1000; cohorts of 12 or 13 sites told assignment 2 weeks before crossover; no blinding of participants/personnel. |
| S003 | [Interventions and outcomes](../../../jama_huffman_2018_oi_170166.pdf#page=3) | Admission date defines intervention/control allocation. No transition period. Site training 90–120 minutes. Tool kit: audit/feedback sent monthly, standardized admission/discharge orders, tobacco/diet/activity education, emergency cardiovascular care and quality training. Usual care according to local practice. Primary MACE at 30 days includes death, Third Universal Definition reinfarction, stroke, GUSTO major bleeding: intracerebral hemorrhage or bleeding with substantial hemodynamic compromise requiring treatment. Follow-up in-person or telephone; lost after 3 unsuccessful attempts. |
| S004 | [Secondary outcomes](../../../jama_huffman_2018_oi_170166.pdf#page=3) | Secondary: 30-day all-cause mortality, cardiovascular mortality, in-hospital mortality, 30-day reinfarction, stroke, major GUSTO bleeding, optimal in-hospital medication, optimal discharge medication, tobacco cessation advice. In-hospital composite aspirin + ADP antagonist (clopidogrel/prasugrel/ticagrelor) + anticoagulant + beta-blocker; in-hospital statin predefined but not collected. Discharge composite aspirin + ADP antagonist + statin + beta-blocker. Post hoc expanded MACE adds in-hospital incident heart failure, cardiogenic shock, cardiac arrest. |
| S005 | [Sample size](../../../jama_huffman_2018_oi_170166.pdf#page=3) | Target 15750 participants, 63 hospitals, 5 steps, power 80%, absolute MACE reduction 2.4%, two-sided alpha .05; assumed loss to follow-up 5%, ICC 0.05. Effect assumption based on leading versus lagging hospital outcomes. No control event-rate input is printed in this paragraph. |
| S006 | [Primary and secondary models](../../../jama_huffman_2018_oi_170166.pdf#page=3) | Primary mixed-effects logistic regression: random cluster (hospital) effect; fixed time effect for every 4-month step. Secondary covariate-adjusted model: age, sex, infarction type, systolic pressure, heart rate, serum creatinine, acute heart failure, cardiogenic shock, resuscitated cardiac arrest (GRACE covariates). Baseline summarized unadjusted and adjusted for cluster/time. Prespecified subgroup interactions: age, sex, STEMI/NSTEMI, hospital size, hospital type. Post hoc time exposed × intervention and expanded endpoint analyses. |
| S007 | [Analysis population and stopping](../../../jama_huffman_2018_oi_170166.pdf#page=3) | All results intention-to-treat. Interim analysis at 12 months; only biostatisticians unblinded. O'Brien–Fleming interim stopping z > 2.797, two-sided significance .005; final z > 1.977, two-sided significance .048. No additional a priori multiple-testing threshold adjustment for secondary outcomes; considered exploratory. |
| S008 | [Missing data and interpretation](../../../jama_huffman_2018_oi_170166.pdf#page=7) | Primary results similar after multiple imputation for missing follow-up/lost participants. Hypothetical missing-event scenarios and imputation yielded a broader range but overall plausible results consistent with primary analysis. No implementation details or numeric imputation result printed here. Page 10 limitations: higher than anticipated ICC reduces power; event rates lower and quality higher than anticipated; secondary analyses not adjusted for multiple comparisons. Conclusions on pp. 1, 2, 9, 10 refer to no decrease in primary 30-day composite. |

## Abstract and narrative numeric context

| ID | Exact location | Printed quantities and matching scope |
|---|---|---|
| N001 | [p. 1, abstract interventions](../../../jama_huffman_2018_oi_170166.pdf#page=1) | Control total 10066, steps 0–5: 2915,2649,2251,1422,829,0. Intervention total 11308, steps 0–5: 0,662,1265,2432,3214,3735. |
| N002 | [p. 1, abstract results](../../../jama_huffman_2018_oi_170166.pdf#page=1) | Eligible randomized 21374; completed 21079 (99%). |
| N003 | [p. 1, abstract population](../../../jama_huffman_2018_oi_170166.pdf#page=1) | Mean age 60.6, SD 12.0 years; men 16183 (76%); STEMI 13689 (64%). |
| N004 | [p. 1, abstract result](../../../jama_huffman_2018_oi_170166.pdf#page=1) | MACE intervention 5.3%, control 6.4%; adjusted RD −0.09% (95% CI −1.32 to 1.14%); adjusted OR 0.98 (0.80–1.21). Matches N089 primary columns. |
| N005 | [p. 1, abstract secondary claim](../../../jama_huffman_2018_oi_170166.pdf#page=1) | Higher medication use including reperfusion; no tobacco cessation counseling effect. No numerical effect printed in this sentence. |
| N006 | [p. 1, abstract safety](../../../jama_huffman_2018_oi_170166.pdf#page=1) | No unexpected adverse events reported; no separate numerical safety denominator printed. |
| N007 | [p. 2, Key Points](../../../jama_huffman_2018_oi_170166.pdf#page=2) | 63 hospitals, 21374 participants; control 6.4%, intervention 5.3% MACE; not statistically significant after cluster/time adjustment. Matches N002, N004, N089. |
| N008 | [pp. 2 and 10, external context](../../../jama_huffman_2018_oi_170166.pdf#page=2) | Background global fatal MI 2015: 7.3 million, 95% uncertainty interval 6.8–7.8 million; prior Kerala registry 25748 admissions, 125 hospitals. Page 10 context: CPACS-3 >29000 Chinese participants; ACTION-GWTG 2014 in-hospital mortality STEMI 6.4%, NSTEMI 3.4%. These are supplied contextual quotations, not ACS QUIK results. |
| N009 | [p. 2, recruitment](../../../jama_huffman_2018_oi_170166.pdf#page=2) | 63 recruited hospitals from prior registry sample n=125; additional government hospitals sought. Hospital eligibility requires 2 willing quality-team individuals. |
| N010 | [p. 5, monitoring](../../../jama_huffman_2018_oi_170166.pdf#page=5) | 1 site high reinfarction prompted quality assurance sampling 10% of cases with corresponding controls; 2 additional sites identified; 13 changes to primary outcome (1% overall events). |
| N011 | [p. 5, recruitment](../../../jama_huffman_2018_oi_170166.pdf#page=5) | 22557 recruited from 63 hospitals; hospitals 67% private, 14% government affiliated with medical colleges, 19% nonprofit/charity. |
| N012 | [p. 5, exclusions](../../../jama_huffman_2018_oi_170166.pdf#page=5) | Cardiac markers missing/not elevated n=954 (NSTEMI only; STEMI with chest pain may not have testing). |
| N013 | [p. 5, exclusions](../../../jama_huffman_2018_oi_170166.pdf#page=5) | Transferred after thrombolysis without further therapy n=132; outside study period n=91; implausible time discrepancies n=6. |
| N014 | [p. 5, follow-up](../../../jama_huffman_2018_oi_170166.pdf#page=5) | 30-day follow-up 99%; 21374 eligible. |
| N015 | [p. 5, software](../../../jama_huffman_2018_oi_170166.pdf#page=5) | Statistical engines Stata 14, SAS 9.4, R 3.3.0; StatTag 3.0 results preparation. No external code accessed. |
| N016 | [p. 6, incomplete follow-up](../../../jama_huffman_2018_oi_170166.pdf#page=6) | 295 (1%) incomplete outcome: 215 not followed by enrolling site; 80 unreachable after 3 contacts. |
| N017 | [p. 6, missingness comparison](../../../jama_huffman_2018_oi_170166.pdf#page=6) | Included versus missing follow-up initial troponin 1.3 vs 4.6 ng/mL; P < .001; eTable 1 pointer. No test specification printed here. |
| N018 | [p. 6, groups](../../../jama_huffman_2018_oi_170166.pdf#page=6) | Intervention 11308 (53%), control 10066 (47%). |
| N019 | [p. 6, overall baseline](../../../jama_huffman_2018_oi_170166.pdf#page=6) | Mean age 60.6 years, men 76%, tobacco history 31%, diabetes history 44%, STEMI 64%. |
| N020 | [p. 6, baseline timing](../../../jama_huffman_2018_oi_170166.pdf#page=6) | Symptom-to-door control median 240 (IQR 120–840) min, intervention 255 (111–825) min. Matches N048. |

## Figure 1 complete flow inventory

All rows: [physical p. 4, Figure 1](../../../jama_huffman_2018_oi_170166.pdf#page=4). C=control, I=intervention. Exclusion reason columns are printed cardiac markers / transferred after thrombolysis without further treatment / outside period / timeline discrepancy; an em dash means no category printed. Lost participants remain included in analysis, per caption. All 63 approached hospitals screened eligible and agreed; randomization occurred at one time before enrollment; hospitals blinded to assigned cohort until 2 weeks before crossover.

Step windows: 0 November 10, 2014–March 9, 2015; 1 March 10–July 9, 2015; 2 July 10–November 9, 2015; 3 November 10, 2015–March 9, 2016; 4 March 10–July 9, 2016; 5 July 10–November 9, 2016. Intervention cohort hospital counts 1–5: 12,13,13,13,12. Control hospital counts steps 0–4: 63,51,38,25,12.

| ID | Phase/cohort | Step | Enrolled | Lost | Included/analyzed | Excluded | Markers | Transfer | Outside | Timeline |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N021 | C all | 0 | 3107 | 42 | 2915 | 192 | 172 | 18 | — | 2 |
| N022 | C remaining | 1 | 2765 | 45 | 2649 | 116 | 101 | 15 | — | — |
| N023 | C remaining | 2 | 2328 | 54 | 2251 | 77 | 67 | 10 | — | — |
| N024 | C remaining | 3 | 1450 | 27 | 1422 | 28 | 25 | 3 | — | — |
| N025 | C remaining | 4 | 844 | 2 | 829 | 15 | 9 | 2 | 4 | — |
| N026 | I cohort 1 | 1 | 706 | 2 | 662 | 44 | 43 | 1 | — | — |
| N027 | I cohort 1 | 2 | 593 | 6 | 542 | 51 | 47 | 3 | — | 1 |
| N028 | I cohort 1 | 3 | 757 | 0 | 654 | 103 | 101 | 2 | — | — |
| N029 | I cohort 1 | 4 | 659 | 3 | 605 | 54 | 52 | 1 | — | 1 |
| N030 | I cohort 1 | 5 | 675 | 10 | 648 | 27 | 16 | 4 | 7 | — |
| N031 | I cohort 2 | 2 | 790 | 18 | 723 | 67 | 62 | 5 | — | — |
| N032 | I cohort 2 | 3 | 821 | 4 | 785 | 36 | 34 | 2 | — | — |
| N033 | I cohort 2 | 4 | 764 | 6 | 727 | 37 | 34 | 3 | — | — |
| N034 | I cohort 2 | 5 | 627 | 28 | 600 | 27 | 26 | 1 | — | — |
| N035 | I cohort 3 | 3 | 1076 | 10 | 993 | 83 | 64 | 19 | — | — |
| N036 | I cohort 3 | 4 | 1071 | 8 | 1022 | 49 | 19 | 29 | — | 1 |
| N037 | I cohort 3 | 5 | 991 | 7 | 964 | 27 | 20 | 7 | — | — |
| N038 | I cohort 4 | 4 | 895 | 7 | 860 | 35 | 32 | 2 | — | 1 |
| N039 | I cohort 4 | 5 | 637 | 7 | 627 | 10 | 9 | 1 | — | — |
| N040 | I cohort 5 | 5 | 1001 | 9 | 896 | 105 | 21 | 4 | 80 | — |

## Table 1 complete baseline inventory

All rows: [physical p. 5, Table 1](../../../jama_huffman_2018_oi_170166.pdf#page=5). Control header n=10066; intervention n=11308. Counts use these denominators except explicit variable-specific n. Differences are crude intervention minus control, footnote b; 95% CIs. Percent differences are percentage points. S009–S035 correspond in order to N041–N067. SD applies to mean rows; IQR applies to median rows. Hospital-category n denotes hospitals, while cell counts denote participants. Footnote a states variable-specific totals for incompletely reported data. Conversion factors: LDL mg/dL ×0.0259 to mmol/L; triglycerides ×0.0113; creatinine ×88.4 to micromol/L; glucose ×0.0555 to mmol/L.

| ID | Variable; unit; category hospital n if relevant | Control | Intervention | Crude difference (95% CI) |
|---|---|---|---|---|
| N041 | Age mean (SD), years | 60.3 (12.0) | 60.9 (12.1) | 0.6 (0.3 to 1.0) |
| N042 | Male n (%) | 7654 (76.0) | 8529 (75.4) | −0.6 (−1.8 to 0.5) |
| N043 | Tobacco history n (%) | 3772 (37.5) | 2842 (25.1) | −12.3 (−13.6 to −11.1) |
| N044 | Diabetes history n (%) | 4151 (41.2) | 5333 (47.2) | 5.9 (4.6 to 7.3) |
| N045 | Transferred n (%) | 4202 (41.7) | 4199 (37.1) | −4.6 (−5.9 to −3.3) |
| N046 | No insurance n (%) | 6878 (68.3) | 8664 (76.6) | 8.3 (7.1 to 9.5) |
| N047 | STEMI n (%) | 6921 (68.8) | 6768 (59.9) | −8.9 (−10.2 to −7.6) |
| N048 | Symptom-to-door median (IQR), min | 240 (120–840), n=9711 | 255 (111–825), n=10849 | 15 (4 to 26) |
| N049 | Body weight mean (SD), kg | 63.6 (9.8), n=10065 | 63.3 (9.6), n=11304 | −0.3 (−0.5 to 0.0) |
| N050 | Systolic pressure mean (SD), mm Hg | 138.1 (29.1), n=10061 | 139.0 (28.9), n=11303 | 0.9 (0.1 to 1.7) |
| N051 | Heart rate mean (SD), /min | 80.0 (18.7), n=10065 | 79.9 (19.1), n=11303 | −0.1 (−0.6 to 0.5) |
| N052 | Initial troponin median (IQR), ng/mL | 1.6 (0.4–8.0), n=4566 | 1.1 (0.2–4.4), n=4483 | −0.5 (−0.7 to −0.4) |
| N053 | LDL mean (SD), mg/dL | 126.2 (40.3), n=7288 | 119.1 (41.2), n=7542 | −7.1 (−8.4 to −5.8) |
| N054 | Triglycerides median (IQR), mg/dL | 121 (89–167), n=7308 | 122 (90–163), n=7552 | 1 (−1 to 3) |
| N055 | Creatinine median (IQR), mg/dL | 1.0 (0.8–1.2), n=4246 | 1.0 (0.9–1.2), n=9589 | 0.0 (0.0 to 0.0) |
| N056 | Fasting glucose median (IQR), mg/dL | 124 (98–172), n=6658 | 130 (105–180), n=6740 | 6 (4 to 8) |
| N057 | Hemoglobin mean (SD), printed mg/dL | 13.3 (2.0), n=9763 | 13.2 (2.0), n=11079 | −0.1 (−0.2 to 0.0) |
| N058 | Government, 9 hospitals | 4097 (40.7) | 3036 (26.8) | −13.9 (−15.1 to −12.6) |
| N059 | Nonprofit/charity, 12 hospitals | 2785 (27.7) | 2964 (26.2) | −1.5 (−2.7 to −0.3) |
| N060 | Private, 42 hospitals | 3184 (31.6) | 5308 (46.9) | 15.3 (14.0 to 16.6) |
| N061 | Extra large >1000, 5 hospitals | 1853 (18.4) | 1707 (15.1) | −3.3 (−4.3 to −2.3) |
| N062 | Large 501–1000, 15 hospitals | 3561 (35.4) | 4962 (43.9) | 8.5 (7.2 to 9.8) |
| N063 | Medium 201–500, 24 hospitals | 3847 (38.2) | 3568 (31.6) | −6.7 (−7.9 to −5.4) |
| N064 | Small ≤200, 19 hospitals | 805 (8.0) | 1071 (9.5) | 1.5 (0.7 to 2.2) |
| N065 | Cath lab installed during study, 3 hospitals | 171 (1.7) | 325 (2.9) | 1.2 (0.8 to 1.6) |
| N066 | No cath lab, 17 hospitals | 1998 (19.8) | 1554 (13.7) | −6.1 (−7.1 to −5.1) |
| N067 | Cath lab yes, 43 hospitals | 7897 (78.5) | 9429 (83.4) | 4.9 (3.9 to 6.0) |

## Table 2 complete process and time inventory

All rows: [physical p. 6, Table 2](../../../jama_huffman_2018_oi_170166.pdf#page=6). S036–S056 correspond to N068–N088 in order. Header totals C=10066, I=11308; each count has its explicit denominator. Footnote a: eligible participants with measure reported; contraindications excluded; discharge outcomes only discharged; discharge ACE inhibitor/ARB only discharged with ejection fraction ≤40%. Second antiplatelet: clopidogrel, prasugrel, ticagrelor. Footnote b states OR and beta-coefficient effect intervention versus control and describes difference in marginal effects, I minus C, in mixed-effects logistic or quantile regression with random effects for clustering and temporal trends. Footnote c marks beta-coefficients for time rows; the separate difference column is headed % even for these time rows. Preserve both columns. All intervals 95%; no row P values printed.

| ID | Measure | Control count/total (%) or median (IQR) | Intervention count/total (%) or median (IQR) | Difference, printed % (95% CI) | OR or beta (95% CI) |
|---|---|---|---|---|---|
| N068 | Prehospital aspirin | 1696/10052 (16.9) | 2100/11300 (18.6) | 3.80 (2.08 to 5.52) | 1.40 (1.21–1.62) |
| N069 | Prehospital thrombolysis, STEMI | 25/6921 (0.4) | 37/6768 (0.5) | −0.04 (−0.76 to 0.68) | 0.95 (0.40–2.28) |
| N070 | In-hospital aspirin | 9858/10042 (98.2) | 11027/11286 (97.7) | −0.05 (−0.95 to 0.84) | 0.98 (0.69–1.39) |
| N071 | In-hospital second antiplatelet | 9861/10050 (98.1) | 11112/11297 (98.4) | −0.05 (−0.89 to 0.79) | 0.98 (0.67–1.43) |
| N072 | In-hospital beta-blocker | 3676/9874 (37.2) | 4638/10885 (42.6) | 6.25 (4.10 to 8.40) | 1.46 (1.29–1.65) |
| N073 | In-hospital anticoagulant | 8602/10051 (85.6) | 9654/11281 (85.6) | 2.60 (0.87 to 4.33) | 1.27 (1.09–1.49) |
| N074 | Echocardiography | 9209/10066 (91.5) | 10516/11308 (93.0) | 5.62 (3.35 to 7.89) | 2.50 (1.95–3.21) |
| N075 | Diagnostic angiography | 6181/10066 (61.4) | 6500/11308 (57.5) | Nonestimable | Nonestimable |
| N076 | PCI | 5282/10066 (52.5) | 5271/11308 (46.6) | −1.66 (−3.27 to −0.04) | 0.87 (0.77–0.99) |
| N077 | Primary PCI, STEMI | 3476/6921 (50.2) | 3234/6768 (47.8) | −1.87 (−3.85 to 0.11) | 0.86 (0.73–1.01) |
| N078 | Door-to-balloon, STEMI, median (IQR) min | 65 (53–105), n=4022 | 77 (55–118), n=3639 | 6.18 (−4.78 to 17.14) | beta 13.00 (3.64–22.36) |
| N079 | Thrombolysis, STEMI | 1596/6921 (23.1) | 1571/6768 (23.2) | 5.56 (3.21 to 7.91) | 1.59 (1.33–1.92) |
| N080 | Door-to-needle, STEMI, median (IQR) min | 44 (30–67), n=1455 | 45 (27–75), n=1433 | 0.40 (−5.23 to 6.03) | beta 5.00 (−5.20–15.20) |
| N081 | Any reperfusion, STEMI | 5067/6921 (73.2) | 4805/6768 (71.0) | 3.43 (0.87 to 6.00) | 1.24 (1.06–1.46) |
| N082 | Rescue PCI, STEMI | 644/6891 (9.3) | 1031/6767 (15.2) | 2.45 (0.51 to 4.38) | 1.39 (1.08–1.79) |
| N083 | Discharge aspirin | 8777/8998 (97.5) | 10360/10559 (98.1) | 1.36 (0.23 to 2.49) | 1.65 (1.15–2.37) |
| N084 | Discharge second antiplatelet | 8824/9011 (97.9) | 10377/10580 (98.1) | 0.41 (−0.31 to 1.13) | 1.24 (0.86–1.79) |
| N085 | Discharge beta-blocker | 5808/8894 (65.3) | 6799/10178 (66.8) | 6.69 (4.43 to 8.95) | 1.48 (1.30–1.68) |
| N086 | Discharge statin | 8700/9006 (96.6) | 10289/10579 (97.3) | 1.21 (0.07 to 2.35) | 1.42 (1.04–1.92) |
| N087 | Discharge ACE inhibitor/ARB, EF ≤40% | 534/1029 (51.9) | 643/1495 (43.0) | 6.57 (0.58 to 12.57) | 1.45 (1.03–2.04) |
| N088 | Cardiac rehabilitation referral | 2362/9228 (25.6) | 3322/10791 (30.8) | Nonestimable | Nonestimable |

## Table 3 complete primary and secondary results

All rows: [physical p. 7, Table 3](../../../jama_huffman_2018_oi_170166.pdf#page=7). Header C=10066, I=11308. Counts/percentages printed as No. (%); clinical endpoints use header denominators; process composites and counseling apply eligibility/discharge definitions below, without printed row-specific denominator. No denominator is inferred from a rounded percentage. Cluster model: hospital random effect; primary model additionally temporal trends (S006). For each N089–N098 row, two statistical relationships are tracked in column order: S057/S058 through S075/S076 (cluster-only, then primary cluster/time). Effect direction I versus C; differences I minus C; intervals 95%; ICC column as printed. Footnote a describes OR as the difference in marginal effects and specifies mixed-effects logistic regression; this text is retained as printed. Footnotes b–e specify GUSTO major bleeding, eligible in-hospital all-medication recipients, eligible discharged all-medication recipients, and discharged baseline smokers respectively.

| ID | Outcome | C count (%) | I count (%) | Cluster difference % (95% CI) | Cluster OR (95% CI) | Primary difference % (95% CI) | Primary OR (95% CI) | ICC |
|---|---|---|---|---|---|---|---|---:|
| N089 | 30-day MACE | 645 (6.4) | 602 (5.3) | −0.51 (−1.28 to 0.26) | 0.92 (0.81–1.04) | −0.09 (−1.32 to 1.14) | 0.98 (0.80–1.21) | 0.15 |
| N090 | 30-day mortality | 509 (5.1) | 445 (3.9) | −0.65 (−1.34 to 0.03) | 0.87 (0.75–1.00) | −0.28 (−1.35 to 0.80) | 0.94 (0.74–1.19) | 0.18 |
| N091 | 30-day cardiovascular mortality | 494 (4.9) | 434 (3.8) | −0.58 (−1.24 to 0.09) | 0.88 (0.76–1.02) | −0.26 (−1.31 to 0.80) | 0.94 (0.74–1.20) | 0.19 |
| N092 | In-hospital mortality | 331 (3.3) | 321 (2.8) | −0.05 (−0.58 to 0.47) | 0.98 (0.82–1.17) | −0.23 (−1.07 to 0.60) | 0.93 (0.70–1.22) | 0.18 |
| N093 | 30-day reinfarction | 121 (1.2) | 135 (1.2) | 0.12 (−0.31 to 0.55) | 1.08 (0.82–1.42) | 0.50 (−0.24 to 1.24) | 1.39 (0.87–2.22) | 0.33 |
| N094 | 30-day stroke | 60 (0.6) | 90 (0.8) | 0.20 (−0.05 to 0.45) | 1.34 (0.94–1.93) | 0.14 (−0.23 to 0.52) | 1.24 (0.71–2.15) | 0.14 |
| N095 | 30-day major GUSTO bleeding | 19 (0.2) | 30 (0.3) | 0.13 (−0.05 to 0.30) | 1.56 (0.84–2.88) | 0.23 (−0.05 to 0.52) | 2.34 (0.93–5.89) | 0.20 |
| N096 | Optimal in-hospital medication | 3122 (31.7) | 3878 (35.8) | 8.61 (6.98 to 10.23) | 1.70 (1.57–1.85) | 6.00 (3.90 to 8.11) | 1.45 (1.28–1.64) | 0.40 |
| N097 | Optimal discharge medication | 5454 (61.8) | 6483 (64.0) | 9.97 (8.32 to 11.61) | 1.73 (1.59–1.87) | 8.66 (6.30 to 11.03) | 1.61 (1.42–1.82) | 0.28 |
| N098 | Tobacco cessation advice | 3526 (96.0) | 2618 (94.7) | 0.30 (−1.20 to 1.80) | 1.06 (0.80–1.39) | 0.30 (−2.15 to 2.76) | 1.06 (0.67–1.67) | 0.37 |

MACE death/reinfarction/stroke/major bleeding is a composite; individual component counts are not asserted to be disjoint. Optimal in-hospital medication is aspirin, ADP antagonist, anticoagulant, beta-blocker among eligible for all. Optimal discharge medication is aspirin, ADP antagonist, statin, beta-blocker among discharged eligible for all. Counseling among discharged baseline smokers. Main text pp. 6–7 uses rounded process percentages and explicit effect values below. The table title contains the words “within-hospital clustering and clustering and temporal trends”; no quantity is altered in transcription.

## Figure 3 complete subgroup results

All rows: [physical p. 9, Figure 3](../../../jama_huffman_2018_oi_170166.pdf#page=9). Endpoint 30-day MACE; model accounts for within-hospital clustering and temporal trends; effect I versus C. All intervals 95%. S077–S090 correspond to N099–N112 in order. Hospital n labels count hospitals; event denominators count participants. Axis adjusted OR ticks 0.3,1.0,3.0, reference line 1; left favors intervention, right favors control. Marker size represents precision of point estimates. Arrowheads mark intervals extending beyond plot limits for extra-large and small hospitals; full numeric intervals are printed. No interaction P values printed here.

| ID | Subgroup | I events/total (%) | C events/total (%) | Adjusted difference % (95% CI) | Adjusted OR (95% CI) |
|---|---|---|---|---|---|
| N099 | Age <50 y | 58/2079 (2.8) | 68/2045 (3.3) | 1.42 (−0.71 to 3.54) | 1.53 (0.83 to 2.79) |
| N100 | Age 50–69 y | 297/6606 (4.5) | 326/5863 (5.6) | −0.57 (−2.02 to 0.88) | 0.89 (0.67 to 1.19) |
| N101 | Age ≥70 y | 247/2623 (9.4) | 251/2158 (11.6) | −0.23 (−3.32 to 2.85) | 0.98 (0.71 to 1.35) |
| N102 | Male | 375/8529 (4.4) | 409/7654 (5.3) | 0.05 (−1.32 to 1.41) | 1.01 (0.78 to 1.31) |
| N103 | Female | 227/2779 (8.2) | 236/2412 (9.8) | −0.57 (−3.13 to 2.00) | 0.93 (0.67 to 1.29) |
| N104 | STEMI | 400/6768 (5.9) | 465/6921 (6.7) | 0.57 (−1.01 to 2.14) | 1.09 (0.85 to 1.40) |
| N105 | NSTEMI | 202/4540 (4.4) | 180/3145 (5.7) | −1.46 (−3.49 to 0.57) | 0.75 (0.51 to 1.10) |
| N106 | Extra large >1000, n=5 hospitals | 51/1707 (3.0) | 76/1853 (4.1) | 1.83 (−0.80 to 4.46) | 1.68 (0.85 to 3.32) |
| N107 | Large 501–1000, n=15 hospitals | 168/4962 (3.4) | 212/3561 (6.0) | −1.56 (−3.58 to 0.46) | 0.71 (0.47 to 1.08) |
| N108 | Medium 201–500, n=24 hospitals | 292/3568 (8.2) | 310/3847 (8.1) | −1.47 (−3.76 to 0.83) | 0.83 (0.62 to 1.11) |
| N109 | Small <201, n=19 hospitals | 91/1071 (8.5) | 47/805 (5.8) | 2.28 (−2.24 to 6.79) | 1.45 (0.70 to 3.04) |
| N110 | Government n=9 hospitals | 158/3036 (5.2) | 275/4097 (6.7) | −0.55 (−2.56 to 1.47) | 0.90 (0.61 to 1.33) |
| N111 | Nonprofit n=12 hospitals | 186/2964 (6.3) | 193/2785 (6.9) | −0.62 (−3.43 to 2.20) | 0.91 (0.59 to 1.40) |
| N112 | Private n=42 hospitals | 258/5308 (4.9) | 177/3184 (5.6) | 0.89 (−1.19 to 2.97) | 1.16 (0.82 to 1.64) |

Narrative pp. 9–10 states a similar pattern across prespecified subgroups despite hospital heterogeneity; eFigure 1A is a hospital residual plot against entire-trial mean; eFigure 1B unadjusted within-hospital intervention/control difference; eFigures 2A/B primary/mortality time trends. No additional numeric subgroup result is printed in those paragraphs.

## Figure 2 complete temporal inventory

All entries: [physical p. 8, Figure 2A and 2B](../../../jama_huffman_2018_oi_170166.pdf#page=8). A=30-day MACE, B=30-day mortality, unadjusted percentages; y axes 0,2,4,6,8,10,12,14%; x steps 0–5. Colors green/blue/purple/red/orange for cohorts 1–5; open circles control, solid circles intervention. Each cohort becomes intervention at its numbered step. Error bars are 95% CIs, method not printed in caption. Graph numbers below are approximate visual readings to about 0.1–0.2 percentage point; the source prints no numerical rate or CI labels. Exact printed denominator vectors are separate. Every graphical result is retained without substituting inferred events.

| Cohort | Exact printed n vector, steps 0,1,2,3,4,5; repeated identically under A and B | Phase vector |
|---|---|---|
| 1 | 439,662,542,654,605,648 | C,I,I,I,I,I |
| 2 | 400,379,723,785,727,600 | C,C,I,I,I,I |
| 3 | 858,910,827,993,1022,964 | C,C,C,I,I,I |
| 4 | 477,629,730,679,860,627 | C,C,C,C,I,I |
| 5 | 741,731,694,743,829,896 | C,C,C,C,C,I |

Each rate cell is point (lower–upper 95% CI), all approximate %. IDs increase in step order within each row.

| IDs for steps 0–5 | Panel/cohort | Step 0 | Step 1 | Step 2 | Step 3 | Step 4 | Step 5 |
|---|---|---|---|---|---|---|---|
| N113–N118 | A cohort 1 | 3.4 (2.0–5.7) | 3.8 (2.6–5.6) | 2.4 (1.4–4.2) | 2.6 (1.6–4.2) | 3.1 (2.0–4.7) | 5.7 (4.1–7.9) |
| N119–N124 | A cohort 2 | 5.8 (3.8–8.6) | 4.5 (2.7–7.2) | 7.9 (6.0–10.2) | 5.7 (4.3–7.5) | 4.4 (3.1–6.3) | 3.7 (2.3–5.5) |
| N125–N130 | A cohort 3 | 9.8 (7.9–12.0) | 10.0 (8.1–12.2) | 8.8 (7.0–11.0) | 7.6 (6.0–9.4) | 6.8 (5.3–8.5) | 5.4 (4.0–7.2) |
| N131–N136 | A cohort 4 | 3.4 (2.0–5.5) | 7.0 (5.2–9.3) | 5.6 (4.1–7.6) | 7.8 (6.0–10.2) | 6.0 (4.6–7.9) | 5.1 (3.6–7.3) |
| N137–N142 | A cohort 5 | 6.3 (4.7–8.4) | 5.0 (3.6–6.8) | 4.8 (3.4–6.7) | 4.6 (3.3–6.4) | 4.6 (3.3–6.3) | 6.1 (4.7–8.0) |
| N143–N148 | B cohort 1 | 3.0 (1.7–5.1) | 2.7 (1.7–4.4) | 2.0 (1.1–3.7) | 2.3 (1.4–3.8) | 2.6 (1.6–4.3) | 1.7 (0.9–3.0) |
| N149–N154 | B cohort 2 | 3.3 (1.8–5.6) | 4.2 (2.5–6.9) | 6.0 (4.5–7.9) | 5.1 (3.7–6.9) | 3.2 (2.0–4.8) | 3.0 (1.8–4.8) |
| N155–N160 | B cohort 3 | 7.6 (5.9–9.6) | 7.4 (5.8–9.3) | 7.4 (5.7–9.4) | 5.5 (4.3–7.2) | 5.5 (4.2–7.1) | 3.9 (2.8–5.4) |
| N161–N166 | B cohort 4 | 2.3 (1.2–4.2) | 5.6 (4.1–7.7) | 4.2 (3.0–6.0) | 6.3 (4.7–8.5) | 4.0 (2.9–5.6) | 4.5 (3.1–6.4) |
| N167–N172 | B cohort 5 | 5.3 (3.8–7.2) | 3.2 (2.1–4.8) | 4.2 (2.8–6.0) | 3.9 (2.6–5.6) | 4.1 (2.9–5.8) | 4.4 (3.2–6.0) |

All 60 graphical intervals were inspected for their relation to their point markers and phase legend. These are descriptive plotted rate/CI relationships, without a reported inferential contrast or P value. The plot is not a table of exact numerical rate values. Caption and axis meanings permit matching by outcome, cohort, step, and phase; flowchart supplies merged control totals and intervention cohort counts. Discussion p. 9 describes lower first-step intervention MACE and mortality than other steps, while noting smaller sample and possible chance, contamination, or baseline differences.

## Matching narrative occurrences: preserve printed numerical values

These rows record narrative occurrences alongside the table result to which they refer; source wording about higher/lower refers to the reported adjusted effect where supplied. Intervention percentage is first in all pairs below. No reconciliation is performed by this mapper.

| ID | Location and target | Printed narrative quantities |
|---|---|---|
| N173 | [p. 6, prehospital aspirin; N068](../../../jama_huffman_2018_oi_170166.pdf#page=6) | 18.6% vs 16.9%; adjusted RD 3.80% (2.08–5.52%); OR 1.40 (1.21–1.62). |
| N174 | [p. 6, prehospital thrombolysis; N069](../../../jama_huffman_2018_oi_170166.pdf#page=6) | Similarly low <1% in both groups. |
| N175 | [p. 6, aspirin/second antiplatelet; N070/N071](../../../jama_huffman_2018_oi_170166.pdf#page=6) | Among eligible without contraindications, rates high >95%, similar both groups. |
| N176 | [pp. 6–7, in-hospital beta-blocker; N072](../../../jama_huffman_2018_oi_170166.pdf#page=6) | 43% vs 37%; adjusted RD 6.25% (4.10–8.10%); OR 1.46 (1.29–1.65), interval continues p. 7. |
| N177 | [p. 7, anticoagulant; N073](../../../jama_huffman_2018_oi_170166.pdf#page=7) | 86% vs 86%; adjusted RD 2.60% (0.87–4.33%); OR 1.27 (1.09–1.49). |
| N178 | [p. 7, echocardiography; N074](../../../jama_huffman_2018_oi_170166.pdf#page=7) | 93% vs 92%; adjusted RD 5.62% (3.35–7.89%); OR 2.50 (1.95–3.21). |
| N179 | [p. 7, STEMI thrombolysis; N079](../../../jama_huffman_2018_oi_170166.pdf#page=7) | 23% vs 23%; adjusted RD 5.56% (3.21–7.91%); OR 1.59 (1.33–1.92). |
| N180 | [p. 7, STEMI reperfusion; N081](../../../jama_huffman_2018_oi_170166.pdf#page=7) | 71% vs 73%; adjusted RD 3.43% (0.87–6.00%); OR 1.24 (1.06–1.46). |
| N181 | [p. 7, STEMI rescue PCI; N082](../../../jama_huffman_2018_oi_170166.pdf#page=7) | 15% vs 9%; adjusted RD 2.45% (0.51–4.38%); OR 1.39 (1.08–1.79). |
| N182 | [p. 7, diagnostic angiography/PCI; N075/N076](../../../jama_huffman_2018_oi_170166.pdf#page=7) | Diagnostic coronary angiography 58% vs 61%; PCI 47% vs 53%; adjusted PCI RD −1.66% (−3.27 to −0.04%); OR 0.87 (0.77–0.99). |
| N183 | [p. 7, discharge aspirin; N083](../../../jama_huffman_2018_oi_170166.pdf#page=7) | 98% vs 98%; adjusted RD 1.36% (0.23–2.49%); OR 1.65 (1.15–2.37). |
| N184 | [p. 7, discharge beta-blocker; N085](../../../jama_huffman_2018_oi_170166.pdf#page=7) | 67% vs 65%; adjusted RD 6.63% (4.43–8.95%); OR 1.47 (1.30–1.68). |
| N185 | [p. 7, discharge statin/ACE/ARB; N086/N087/N088/N084/N098](../../../jama_huffman_2018_oi_170166.pdf#page=7) | Statin 97% vs 97%, adjusted RD 1.21% (0.07–2.35%), OR 1.42 (1.04–1.92). ACE/ARB among EF ≤40%: 43% vs 52%, adjusted RD 6.57% (0.58–12.57%), OR 1.45 (1.03–2.04). Rehabilitation 31% vs 26%. Second antiplatelet and tobacco counseling high >95%, similar between groups. |
| N186 | [p. 7, Primary Analysis; N089](../../../jama_huffman_2018_oi_170166.pdf#page=7) | Unadjusted MACE 5.3% vs 6.4%; cluster OR 0.92 (0.81–1.04); after time adjustment not statistically significant, RD −0.09% (−1.32 to 1.14%), OR 0.98 (0.80–1.21). Similar after imputation; Figure 2A temporal trends pointer. |
| N187 | [p. 8, Secondary and Post Hoc Analyses; N090](../../../jama_huffman_2018_oi_170166.pdf#page=8) | 30-day death 3.9% vs 5.1%; cluster OR 0.87 (0.75–1.00); after temporal adjustment not statistically significant, RD −0.28% (−1.35 to 0.80%), OR 0.94 (0.74–1.19). No material change after GRACE covariates (eTable 5); in-hospital outcomes similar overall. |
| N188 | [p. 8, exposure interaction](../../../jama_huffman_2018_oi_170166.pdf#page=8) | Post hoc test length of time exposed × intervention, to assess longer exposure; overall effects similar (eTable 6); no numeric interaction statistic or P value printed. |
| N189 | [pp. 8–9, expanded endpoint](../../../jama_huffman_2018_oi_170166.pdf#page=8) | Expanded 30-day MACE + incident in-hospital heart failure, cardiogenic shock, cardiac arrest: unadjusted I 7.0%, C 9.1%; cluster OR 0.89 (0.80–1.00); after temporal adjustment RD −1.34% (−2.72 to 0.04%), OR 0.84 (0.70–1.00), continued on p. 9. eTable 7 pointer. |

S091 tracks the expanded-endpoint cluster-only occurrence and S092 the cluster-plus-temporal occurrence in N189. N017 has an additional inferential key S093 for the printed P < .001 comparison of initial troponin by follow-up availability, with unspecified test. S094 tracks the post hoc exposure interaction N188, with the numeric result not printed in the main article. These are locators for complete downstream statistical coverage, not assumptions about supplied supplements.

## Complete matching and handoff index

- Trial population: N001–N003, N007, N011–N014, N016, N018, Figure 1 N021–N040, Table 1 headers, Figure 2 participant vectors, Figure 3 partitions N099–N112.
- Baseline descriptors: abstract N003 and narrative N019/N020 match Table 1 N041–N067 by eligible population and variable-specific denominator. Missingness comparison N017 concerns availability groups rather than randomized phases.
- Primary MACE: abstract N004, Key Points N007, Table 3 N089, text N186, Figure 2A N113–N142, subgroup Figure 3 N099–N112; conclusions pp. 1,2,9,10. Statistical keys S001,S006–S008,S057/S058,S077–S090.
- Mortality: Table 3 N090–N092, Figure 2B N143–N172, text N187. Clinical secondary event components N093–N095 retain distinct outcomes and models. Table 3 medication composites N096–N098 are distinct from individual process components Table 2 N068–N088.
- All Table 2 narrative counterparts: N173–N185; all clinical primary/mortality counterparts N186/N187. Values were transcribed independently as printed; no source values silently normalized.
- Expanded endpoint N189 and exposure interaction N188 correspond to post hoc definitions S004/S006 and supplied supplement pointers. All prespecified subgroup and post hoc model labels and missingness handling statements retained.

Final local relationship count: 189 numeric/reporting relationships N001–N189, including 60 Figure 2 cohort-step-outcome entries; 154 statistical/model relationship keys S001–S154. These counts describe mapping organization, not findings. Every main-paper page is mapped, every table row is retained (27 + 21 + 10 = 58), every Figure 1 flow box is retained (20), every Figure 3 numeric row is retained (14), every Figure 2 plotted point/interval is retained (60), and all corresponding narrative occurrences and footnotes are retained. No main-paper scientific coverage gap remains; exact underlying Figure 2 numerical coordinates are not printed and are recorded only as approximate graphical values.

For downstream statistical coverage, every Figure 2 graphical rate/95% CI pair has a separate statistical-descriptive key, even though no comparison test is printed: S095–S100 = N113–N118; S101–S106 = N119–N124; S107–S112 = N125–N130; S113–S118 = N131–N136; S119–S124 = N137–N142; S125–S130 = N143–N148; S131–S136 = N149–N154; S137–S142 = N155–N160; S143–S148 = N161–N166; S149–S154 = N167–N172. Thus all 60 plotted interval relationships receive downstream statistical-pass coverage. Each consecutive ID maps exactly to the matching step, not to an aggregate vector. Suggested bounded disjoint checker scopes: numeric N001–N100 and N101–N189; statistical S001–S094 and S095–S154. Method keys contain their complete specifications; multiple displayed effects for one outcome/model are not separate observations, while cluster-only versus temporal models have separate keys.
