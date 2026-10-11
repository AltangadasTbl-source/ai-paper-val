# Support quantitative evidence: results, implemented code, administrative material

Mandatory support_quantitative_mapper stage. Complete disjoint assignment: DOC-004 physical PDF pages 1–27, DOC-005 pages 1–8, DOC-006 page 1, DOC-007 page 1. Total 37 unique units, all 37 mapped. Document role REPORT throughout, assigned by content. This is extraction and relationship mapping only; no finding selection or candidate diagnosis is performed. Local keys N-Rxxx and S-Rxxx identify numeric and statistical relationships for coordinator numbering. They do not reuse historical review IDs.

Scope, review contract, source inventory, source coverage and assigned evidence inventory were read. Sources remain authority. Reused DOC-004/DOC-005/DOC-007 native layouts and DOC-004 page images 10–27, and DOC-006 page image 1 were used as transcription aids. All 19 distinct assigned images were visually inspected, below the 32-image context bound. Fresh direct-source layout corroboration for readable text used Poppler pdftotext 26.01.0, CPU: `pdftotext -layout SOURCE OUTPUT`, with outputs `preprocessing/support_results/DOC-004-direct-layout.txt`, `DOC-005-direct-layout.txt`, `DOC-007-direct-layout.txt`. Existing image-render engine version is historical/unrecorded. No OCR, fallback environment, Office extractor, source modification, or external evidence was used. Formula/cached workbook distinctions are not applicable: no workbook exists in this assignment.

## Complete page coverage

| Source/unit | Content and mapping | Status |
|---|---|---|
| DOC-004 p1 | Cover, eTable/eFigure index; no independent result | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-004 p2 | Contents and page locators; no independent result | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-004 p3 | Trial committees, medication production and affiliations; no statistical result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-004 p4 | Centers: 13 acute and 11 rehabilitation; administrative counts N-R001 | COMPLETE |
| DOC-004 p5 | Continuation of rehabilitation-center list; no independent result | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-004 p6 | Analysis software and quality-control description S-R001 | COMPLETE |
| DOC-004 p7 | Imputation, pooling, disclosed SAP deviations S-R002/S-R003 | COMPLETE |
| DOC-004 p8 | PRAI questions/definition S-R004 | COMPLETE |
| DOC-004 p9 | Distal motor item scoring S-R005 | COMPLETE |
| DOC-004 p10 | eTable 1 baseline counts and continuous summaries N-R002 | COMPLETE |
| DOC-004 p11 | eTable 1 continuation N-R002 | COMPLETE |
| DOC-004 p12 | FAS/mITT definitions and narrative estimand results S-R006/S-R007 | COMPLETE |
| DOC-004 p13 | eTable 2 estimands 1–8 S-R007 | COMPLETE |
| DOC-004 p14 | eTable 3 post hoc estimands 9–11 S-R008 | COMPLETE |
| DOC-004 p15 | eTable 4 all ten secondary-outcome rows N-R003/S-R009 | COMPLETE |
| DOC-004 p16 | eTable 5 all SAE rows N-R004 | COMPLETE |
| DOC-004 p17 | eTable 6 all AE rows N-R005 | COMPLETE |
| DOC-004 p18 | eTables 7 and 8: all coefficients/CIs/P values and F-tests S-R010/S-R011 | COMPLETE |
| DOC-004 p19 | eTable 9: prespecified AE list S-R012 | COMPLETE |
| DOC-004 p20 | eFigure 1 inclusion/exclusion thresholds S-R013 | COMPLETE |
| DOC-004 p21 | eFigure 2 schedule, every assessment group and footnote S-R014 | COMPLETE |
| DOC-004 p22 | eFigure 3 all printed site totals, axis/time labels N-R006 | COMPLETE |
| DOC-004 p23 | eFigure 4 estimand forest plot and legends 1–3 S-R015 | COMPLETE |
| DOC-004 p24 | eFigure 4 legend continuation 5–8 S-R015 | COMPLETE |
| DOC-004 p25 | eFigure 5 all center/arm/scale labels, grouping rule N-R007 | COMPLETE |
| DOC-004 p26 | eFigure 6 spline predictions and axis labels S-R016 | COMPLETE |
| DOC-004 p27 | eFigure 7 PH1–PH3, subgroup cutoff and labels S-R017 | COMPLETE |
| DOC-005 p1 | Collaborator roster: Aarau, Baden, Lausanne; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p2 | Collaborator roster: Lausanne, Fribourg, Hirslanden; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p3 | Collaborator roster: Bern, Basel; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p4 | Collaborator roster: Basel; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p5 | Collaborator roster: Basel, Zurich; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p6 | Collaborator roster: Graubünden, Münsterlingen, St. Gallen, Felix Platter; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p7 | Collaborator roster: Felix Platter, Rheinfelden; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p8 | Collaborator roster: Rheinfelden, Valens; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-006 p1 | Implemented R main analysis code, lines 1–35 S-R018 | COMPLETE |
| DOC-007 p1 | Data availability and request conditions S-R019; no quantitative result | COMPLETE, NO_APPLICABLE_RESULT |

## Administrative and statistical definitions

### N-R001 — Centers

Source [DOC-004 p4](../../../joi250066supp3_prod_1761597796.4701.pdf#page=4), continuation p5. Acute centers n=13: Basel, Zurich, Fribourg, Bern, Lausanne, St. Gallen, Münsterlingen, Winterthur, Baden, Graubünden, Aarau, Hirslanden Zurich, Sion. Rehabilitation centers n=11: Felix Platter Basel, Rheinfelden, HFR Meyriez-Murten, Zihlschlacht, Zurich Lengg, Cereneo Vitznau, Bad Zurzach, Valens, Zurich Wald, Rheinburg Walzenhausen, Sion. Administrative site keys can match enrollment figure; no outcome estimates on these pages.

### S-R001 — Software and quality control

[DOC-004 p6](../../../joi250066supp3_prod_1761597796.4701.pdf#page=6). R 4.3.1 released June 16, 2023. Packages: dplyr 1.1.4; data.table 1.14.8; tidyr 1.3.0; forcats 1.0.0; plyr 1.8.9; purrr 1.0.2; tibble 3.2.1; tidyselect 1.2.0; lme4 1.1-35.1; MASS 7.3-60; Matrix 1.6-3; mice 3.16.0; mitml 0.4-5; glmnet 4.1-8; survey 4.2-1; survival 3.5-7; e1071 1.7-13; nnet 7.3-19; rpart 4.1.19; class 7.3-22; ggplot2 3.4.4; scales 1.2.1; grid 4.3.1; gtable 0.3.4; colorspace 2.1-0; munsell 0.5.0; assertthat 0.2.1; boot 1.3-28; DBI 1.1.3; digest 0.6.36; stringr 1.5.1; stringi 1.8.4; tools 4.3.1. Independently verified statistician code, cross-checked key dataset elements, and validated tables/figures against underlying data. Package listing does not identify which model produced each result; actual code is S-R018.

### S-R002 — Imputation and pooling

[DOC-004 p7](../../../joi250066supp3_prod_1761597796.4701.pdf#page=7). 100 multiple imputations using chained equations. Generated imputed values displayed in plots; model fit in each imputed dataset; estimates and variances combined using Rubin's rules into one estimate and variance per parameter. Missing/incomplete FMA imputed at item level; secondary outcomes at summary-score level. Potential-harm outcomes not imputed. Match main-paper missing-data/statistical-analysis keys and supplied SAP estimand/MI specification; no external imputation model assumed.

### S-R003 — Disclosed SAP deviations

Same p7: introductory text states two deviations, followed by three numbered items. Record each item rather than selecting by count: (1) mRS for participants who died before three months was set to 6 rather than imputed; (2) missing subjective PRAI not imputed; (3) secondary-outcome adjusted mean difference initially stated for affected side in SAP, calculation performed for unaffected side. The third item describes a wording change and authors' supplied rationale; no mapper judgment. Match main-paper mRS/PRAI/secondary FMA and supplied SAP endpoint/imputation keys.

### S-R004 — PRAI

[DOC-004 p8](../../../joi250066supp3_prod_1761597796.4701.pdf#page=8). Two questions: whether participant noticed improvement in deficits caused by stroke since last study visit; if yes, whether improvement is meaningful in daily life. English meanings recorded from bilingual printed questions. Match eTable 4 PRAI no relevant improvement, main-paper PRAI and SAP relevance definition. No additional numeric outcome on p8.

### S-R005 — Distal motor scoring

[DOC-004 p9](../../../joi250066supp3_prod_1761597796.4701.pdf#page=9). Examiner holds forearm, requests maximum finger extension; if no extension places fingers fully extended and observes flexion for 5 seconds. Only first attempt graded, no repetition of instructions/testing. Score 0 normal/no flexion after 5 seconds; 1 some extension after 5 seconds but not fully extended, uncommanded movement unscored; 2 no voluntary extension after 5 seconds, movement at other times unscored. Match eligibility NIHSS/distal-paresis key. Supplied references are locators only; no external sources consulted.

## N-R002 — Complete eTable 1 baseline map

[DOC-004 p10](../../../joi250066supp3_prod_1761597796.4701.pdf#page=10) and [p11](../../../joi250066supp3_prod_1761597796.4701.pdf#page=11). Values in columns Overall / Placebo / Levodopa. Population N 610 / 303 / 307. Counts are printed No. (%) unless otherwise stated. Every continuous row retains printed label and dispersion type. Match main baseline Table 1 by row, population and time; descriptive copies remain descriptive rather than model effects.

| Printed row | Overall | Placebo | Levodopa |
|---|---|---|---|
| N | 610 | 303 | 307 |
| Median age [IQR], years | 73 [64–82] | 74 [64–84] | 72 [62–81] |
| Female sex | 252 (41.3) | 133 (43.9) | 119 (38.8) |
| Median BMI [IQR] | 25.7 [23.4 28.7] | 25.3 [23.1,28.1] | 26.0 [23.5,29.1] |
| Hypertension | 435 (71.3) | 213 (70.3) | 222 (72.3) |
| Diabetes | 144 (23.6) | 64 (21.1) | 80 (26.1) |
| Hyperlipidemia | 291 (47.7) | 152 (50.2) | 139 (45.3) |
| Smoking | 127 (20.8) | 59 (19.5) | 68 (22.1) |
| Atrial fibrillation | 95 (15.6) | 61 (20.1) | 34 (11.1) |
| Coronary heart disease | 99 (16.2) | 47 (15.5) | 52 (16.9) |
| Dementia | 20 (3.3) | 9 (3.0) | 11 (3.6) |
| Movement disorder | 11 (1.8) | 5 (1.7) | 6 (2.0) |
| Depression | 41 (6.7) | 18 (5.9) | 23 (7.5) |
| Prior ischemic stroke | 82 (13.4) | 43 (14.2) | 39 (12.7) |
| Prior hemorrhagic stroke | 11 (1.8) | 6 (2.0) | 5 (1.6) |
| Prior median mRS [IQR] | 0.0 [0.0,1.0] | 0.0 [0.0,1.0] | 0.0 [0.0,0.0] |
| Prestroke home | 596 (97.7) | 294 (97.0) | 302 (98.4) |
| Prestroke nursing home | 9 (1.5) | 5 (1.7) | 4 (1.3) |
| Prestroke other | 5 (0.8) | 4 (1.3) | 1 (0.3) |
| Stroke ischemic | 519 (85.1) | 259 (85.5) | 263 (85.7) |
| Stroke hemorrhagic | 91 (14.9) | 44 (14.5) | 44 (14.3) |
| MCA affected | 460 (75.4) | 230 (75.9) | 230 (74.9) |
| MCA bilateral | 16 (2.6) | 6 (2.0) | 10 (3.3) |
| MCA right | 278 (45.6) | 136 (44.9) | 142 (46.3) |
| MCA left | 166 (27.2) | 88 (29.0) | 78 (25.4) |
| ACA affected | 68 (11.1) | 31 (10.2) | 37 (12.1) |
| ACA bilateral | 4 (0.7) | 2 (0.7) | 2 (0.7) |
| ACA right | 23 (3.8) | 11 (3.6) | 12 (3.9) |
| ACA left | 41 (6.7) | 18 (5.9) | 23 (7.5) |
| PCA affected | 60 (9.8) | 33 (10.9) | 27 (8.8) |
| PCA bilateral | 8 (1.3) | 5 (1.7) | 3 (1.0) |
| PCA right (p11) | 35 (5.7) | 20 (6.6) | 15 (4.9) |
| PCA left | 17 (2.8) | 8 (2.6) | 9 (2.9) |
| Vertebrobasilar affected | 108 (17.7) | 45 (14.9) | 63 (20.5) |
| Vertebrobasilar bilateral | 4 (0.7) | 1 (0.3) | 3 (1.0) |
| Vertebrobasilar right | 59 (9.7) | 28 (9.2) | 31 (10.1) |
| Vertebrobasilar left | 45 (7.4) | 16 (5.3) | 29 (9.4) |
| Median FMA total, affected, randomization [IQR] | 34.0 [14.0,54.0] | 33.0 [13.0,52.8] | 35.0 [14.8,55.3] |
| Median FMA upper, affected, randomization [IQR] | 18.0 [6.0,34.0] | 17.5 [6.0,34.0] | 20.0 [6.0,35.0] |
| Median FMA lower, affected, randomization [IQR] | 14.0 [6.5,21.0] | 14.0 [7.0,21.0] | 15.0 [6.0,21.0] |
| Median NIHSS at randomization [IQR] | 8.2 (3.9) | 8.3 (3.8) | 8.2 (3.9) |
| Median mRS randomization [IQR] | 4 [4,5] | 4 [4,5] | 4 [4,5] |
| Median stroke-onset to randomization time [IQR] | 7 [5,10] | 8 [5,10] | 7 [5–11] |
| IV thrombolysis | 120 (19.7) | 66 (21.8) | 54 (17.6) |
| Bridging therapy | 33 (5.4) | 13 (4.3) | 20 (6.5) |
| Endovascular therapy | 81 (13.3) | 44 (14.5) | 37 (12.1) |

Footnotes: IQR interquartile range; MCA middle cerebral artery; ACA anterior cerebral artery; PCA posterior cerebral artery; mRS modified Rankin Scale; NIHSS printed National Health Institutes Stroke Scale; FMA Fugl-Meyer Motor Assessment. NIHSS row's printed label and parenthesized values retained without reinterpreting the dispersion. Stroke-onset time units are not expressly printed in this row; preserve source label, seek matching main/SAP unit.

## Estimands and populations

### S-R006 — Population and intervention definitions

[DOC-004 p12](../../../joi250066supp3_prod_1761597796.4701.pdf#page=12). FAS paragraph begins all randomized included, then states MICE imputes missing FMA among survivors to three months and those dying before three-month assessment excluded. Modified ITT = FAS with complete three-month FMA. Intervention = levodopa plus standardized rehabilitation versus placebo plus standardized rehabilitation. Match main primary population, complete-case sensitivity and SAP estimand populations. The row-specific death inclusions below are retained separately from the generic population definition.

### S-R007 — eTable 2 and matching narrative

[DOC-004 p13](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13), narrative p12. Printed table effect-column title: Estimated Effect of Levodopa: Mean Difference on FMA, [CI]. Contrast levodopa versus placebo, three-month visit, intention-to-treat/randomized assignment unless indicated. Numeric CIs as printed; narrative specifies 95%. Match main primary FMA total score/estimand sensitivity results and SAP estimands by number, not generic treatment-policy name alone.

| Estimand | Population, endpoint and intercurrent-event rule | Summary | Printed effect [CI] | N |
|---|---|---|---|---:|
| 1, primary endpoint, treatment policy | FAS; FMA at three months; analyzed by randomization irrespective of intercurrent events | Mean difference between treatment arms | −0.90 [−3.78,1.98] | 582 |
| 2, treatment policy II | Modified ITT; complete FMA at three months; randomized assignment | Mean difference | −0.39 [−3.33,2.56] | 551 |
| 3, treatment policy III | FAS label; three-month FMA; FMA of deaths imputed | Mean difference | −0.98 [−3.77,1.81] | 610 |
| 4, composite using win-ratios | FAS label; death and FMA at three months; randomized assignment | Printed difference in win-ratio at three months, win ratio [95% CI] | 1.06 [0.86,1.26] | 610 |
| 5, hypothetical | FAS; three-month FMA; exclude SAE causing motor impairment before visit (recurrent stroke, fractures, comparable complications) | Mean difference | −1.41 [−4.31,1.49] | 545 |
| 6, on treatment | FAS; three-month FMA; exclude intake <80% of study medication | Mean difference | −0.57 [−3.73,2.58] | 496 |
| 7, on treatment II | FAS; three-month FMA; exclude at least one week with fewer than five rehabilitation sessions/week in a four-week period | Mean difference | 0.19 [−3.11,3.49] | 450 |
| 8, on treatment III | FAS; three-month FMA; exclude visit outside window | Mean difference | −0.33 [−3.31,2.65] | 524 |

Narrative p12 repeats estimands 2,3,5,6,7,8 with same values. Narrative estimand 4 calls the composite win-ratio result an odds ratio and prints 1.06 (95% CI 0.86 to 1.25); preserve both narrative and table effect labels and upper limits. No P values printed for estimand table rows. No excluded-count arithmetic assumed beyond printed N and stated rules.

### S-R008 — eTable 3 post hoc estimands

[DOC-004 p14](../../../joi250066supp3_prod_1761597796.4701.pdf#page=14). Same effect-column title and contrast as eTable 2. All described as post hoc.

| Estimand | Population, endpoint and rule | Effect [CI] | N |
|---|---|---|---:|
| 9, treatment policy | FAS; change in FMA baseline to three months; randomized assignment irrespective of intercurrent events | −0.90 [−3.78,1.98] | 582 |
| 10, treatment policy IV | All randomized; three-month FMA; death before visit assigned worst possible FMA=0 | −0.03 [−3.27,3.21] | 610 |
| 11, on treatment IV | FAS; three-month FMA; exclude those with at least one week <5 sessions/week over four weeks and intake <80% | 0.32 [−3.25,3.89] | 395 |

Population-level summary mean difference between arms for all three. Matching keys: main post hoc change-score, death-as-zero, combined adherence/rehabilitation sensitivity, eFigure 7 PH1/PH2. Do not silently reinterpret printed conjunction in estimand 11.

## N-R003 / S-R009 — eTable 4 complete secondary outcomes

[DOC-004 p15](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15). Time three months except FMA total affected five weeks. Printed effect-column title for the whole table is Estimated Effect of Levodopa: Mean Difference on FMA, [CI]. Table does not give model formula or P values; match main outcome-specific method and scale instead of treating all rows as FMA mean differences. Placebo/levodopa continuous summaries mean (SD), mRS median [IQR], PRAI count (%). SMD means standardized mean difference. N printed total participants. Each row is an independent numeric/inferential relationship with suffix .01–.10.

| Row | Placebo | Levodopa | SMD | Effect [CI] | N |
|---|---|---|---:|---|---:|
| .01 FMA total unaffected, 3 months | 89.14 (10.32) | 89.67 (9.87) | 0.052 | 0.63 [−0.72,1.99] | 582 |
| .02 FMA upper affected, 3 months | 39.12 (19.19) | 39.20 (19.30) | 0.004 | −0.73 [−2.97,1.50] | 582 |
| .03 FMA lower affected, 3 months | 22.88 (6.90) | 22.91 (7.28) | 0.003 | −0.13 [−1.02,0.77] | 582 |
| .04 FMA total affected, 5 weeks | 56.27 (25.20) | 57.37 (26.70) | 0.042 | 0.02 [−2.81,2.84] | 582 |
| .05 NIHSS, 3 months | 4.20 (3.37) | 4.02 (3.39) | 0.054 | −0.14 [−0.61,0.33] | 582 |
| .06 PROMIS 29, 3 months | 65.11 (13.79) | 64.74 (14.33) | 0.026 | −0.37 [−3.34,2.61] | 582 |
| .07 PROMIS 10, 3 months | 29.87 (5.74) | 30.04 (5.73) | 0.031 | 0.18 [−0.98,1.33] | 582 |
| .08 mRS, 3 months | 3.00 [2.00,4.00] | 3.00 [2.00,4.00] | 0.034 | 0.93 [0.69,1.23] | 596 |
| .09 Rivermead Mobility Index, 3 months | 9.89 (4.73) | 9.70 (4.85) | 0.041 | −0.33 [−1.04,0.37] | 582 |
| .10 PRAI no relevant improvement, 3 months | 51 (18.89), n=270 | 51 (18.48), n=276 | dash | dash | 546 |

Footnote expansions: FMA Fugl-Meyer Motor Assessment; PROMIS 10/29 Patient-Reported Outcomes Measurement Information System; NIHSS National Institutes Stroke Score; mRS modified Rankin Scale; PRAI patient-reported assessment of relevance of motor improvement; CI confidence interval; IQR interquartile range. Link outcome keys to main Table 2/secondary narrative and SAP corresponding endpoints, imputation and outcome model. No effect reconstructed from raw group mean differences; printed modeled effect remains distinct.

## N-R004 — eTable 5 complete SAE counts

[DOC-004 p16](../../../joi250066supp3_prod_1761597796.4701.pdf#page=16). Columns Overall / Placebo / Levodopa. Title serious adverse events; raw n printed, no explicit unique-participant denominator for event categories. Header No. (%) under severity/outcome, but cells print counts only. Match main safety counts and distinguish event versus participant quantities using main context.

| Row | Overall | Placebo | Levodopa |
|---|---:|---:|---:|
| n | 255 | 129 | 126 |
| Participants died | 28 | 17 | 11 |
| Hospitalization | 212 | 102 | 110 |
| Permanent/significant incapacity or disability | 23 | 13 | 10 |
| Life-threatening | 16 | 10 | 6 |
| Severity severe, daily activities impossible | 103 | 54 | 49 |
| Severity moderate, interferes with daily activities | 106 | 54 | 52 |
| Severity mild, tolerable | 46 | 21 | 25 |
| Outcome continuing | 6 | 4 | 2 |
| Outcome recovered/resolved with sequelae | 76 | 40 | 36 |
| Outcome study participant died | 29 | 18 | 11 |
| Outcome unknown | 0 | 0 | 0 |
| Outcome recovered/resolved | 142 | 65 | 77 |
| Outcome other | 2 | 2 | 0 |

No test, effect, interval, or P value supplied here. Both differently named death rows are retained independently; their measurement units are not collapsed.

## N-R005 — eTable 6 complete AE counts

[DOC-004 p17](../../../joi250066supp3_prod_1761597796.4701.pdf#page=17). Prespecified adverse events of interest, Overall / Placebo / Levodopa. Header No. (%) but counts alone printed. No participant denominator or test printed. Match main harm outcome and AE category definition S-R012.

| Row | Overall | Placebo | Levodopa |
|---|---:|---:|---:|
| n | 145 | 67 | 79 |
| Intensity mild | 58 | 29 | 29 |
| Intensity moderate | 86 | 37 | 49 |
| Intensity severe | 2 | 1 | 1 |
| Outcome ongoing | 1 | 0 | 1 |
| Outcome resolved with sequel | 29 | 13 | 16 |
| Outcome resolved without sequel | 116 | 54 | 62 |
| Drug relation certain | 2 | 1 | 1 |
| Drug relation possible | 66 | 32 | 34 |
| Drug relation Probably | 23 | 7 | 16 |
| Drug relation Unassessable | 2 | 2 | 0 |
| Drug relation unlikely | 39 | 15 | 24 |
| Drug relation unrelated | 14 | 10 | 4 |

Definitions: mild tolerable; moderate interferes with daily activities; severe daily activities impossible; probably likely; unassessable unclassifiable. Retain printed Overall n=145; no normalization to summed categories.

## S-R010 — eTable 7 interaction model

[DOC-004 p18](../../../joi250066supp3_prod_1761597796.4701.pdf#page=18). Visually transcribed embedded table. Title model including interaction between baseline FMA and treatment group, with baseline FMA. Visit 3/main analysis. Term names identify centered baseline affected-side FMA and levodopa contrast.

| Term | Estimate | CI | p |
|---|---:|---|---|
| (Intercept) | 62.51 | [60.45,64.57] | <0.001 |
| fma_affected.Visit_1.cent | 0.78 | [0.69,0.87] | <0.001 |
| medicationLevodopa | −0.90 | [−3.78,1.99] | 0.542 |
| fma_affected.Visit_1.cent:medicationLevodopa | 0.00 | [−0.12,0.12] | 0.971 |

Printed caption: main analysis Visit 3, including interaction between baseline and follow-up, estimated levodopa treatment effect. Spline model with basic spline 3 degrees of freedom significantly better than no-spline model: F-test p<0.01 for all imputations. Preserve title's baseline/treatment interaction and caption's baseline/follow-up phrase as distinct printed model descriptions. Match main post hoc baseline interaction and primary effect, SAP model checks; no main-effect formula substituted for this interaction model.

## S-R011 — eTable 8 spline model

Same source p18, visually transcribed. Title model without interaction between baseline FMA and treatment group, baseline FMA modeled using splines (3 df).

| Term | Estimate | CI | p |
|---|---:|---|---|
| (Intercept) | 20.09 | [14.28,25.90] | <0.001 |
| bs(fma_affected.Visit_1.cent, 3)1 | 64.73 | [46.34,83.13] | <0.001 |
| bs(fma_affected.Visit_1.cent, 3)2 | 57.52 | [43.48,71.56] | <0.001 |
| bs(fma_affected.Visit_1.cent, 3)3 | 77.49 | [61.68,93.31] | <0.001 |
| medicationLevodopa | −0.87 | [−3.65,1.92] | 0.541 |

Caption main analysis Visit 3, FMA total score, baseline FMAA spline, estimated levodopa effect; no evidence for interaction between spline-baseline FMAA and medication, F-test p>0.75 for all imputations. Separate overall interaction test from medication main-effect P. Match main post hoc nonlinear baseline analysis and eFigure 6.

## S-R012 — Prespecified harm endpoint content

[DOC-004 p19](../../../joi250066supp3_prod_1761597796.4701.pdf#page=19). Complete eTable 9 list: nausea; vomiting; taste disturbances; dry mouth; anorexia; arrhythmias; postural hypotension; syncope (brief unconsciousness due to reduced brain blood flow); drowsiness including sudden sleep; fatigue; dementia; psychoses (distorted perception of reality); hallucinations; confusion; euphoria; abnormal dreams; insomnia; depression; anxiety; dizziness; dystonia (involuntary contractions); dyskinesia (inability to control voluntary movements); chorea (sudden face/shoulder twitching). No counts per named AE, test or estimate on this page. Match main prespecified AE reporting and prospective list by content.

## S-R013 — Eligibility and exclusion

[DOC-004 p20](../../../joi250066supp3_prod_1761597796.4701.pdf#page=20). All eFigure 1 criteria mapped. Inclusion: acute ischemic or intracerebral hemorrhagic stroke ≤7 days before randomization, excludes subarachnoid hemorrhage/cerebral venous sinus thrombosis; meaningful hemiparesis NIHSS motor arm+motor leg+limb ataxia sum ≥3, distal arm paresis equivalent to one item; randomization ≥24 hours after thrombolysis/thrombectomy; in-hospital rehabilitation needed; capable of standardized rehabilitation; consent participant/next of kin. Exclusion: age<18; Parkinson's; levodopa mandatory per physician; inability/unwillingness to comply with drug intake/procedures (oral, nasogastric, PEG); severe aphasia unable two-stage commands; prestroke mRS>3; prior hemiparesis; hypersensitivity or contraindication to levodopa/carbidopa; pregnancy/breastfeeding/intended pregnancy, childbearing-age pregnancy test; lack of reliable contraception throughout trial (oral/injected/implanted, intrauterine, or investigator accepted), surgical sterilization/hysterectomy or postmenopause>2 years considered outside childbearing potential. Match main eligibility/randomization and protocol criteria; no numeric result on page.

## S-R014 — Complete schedule and assessment groups

[DOC-004 p21](../../../joi250066supp3_prod_1761597796.4701.pdf#page=21), visually inspected schedule. Prescreen day −7 to 0; enrollment/randomization day 0 Visit 1; intervention dose escalation days 1–6, transition day X, full-dose days 7–34, taper days 35–39; Visit 2 end treatment 5 weeks ±7 days; Visit 3 primary outcome 3 months ±14 days; Visit 4 six months ±20 days; Visit 5 twelve months ±30 days; Visits 6–9 telephone follow-up 24,36,48,60 months each ±30 days; unscheduled end-of-study visit on withdrawal/discontinuation.

Consent/randomization/drug and therapy booklet at enrollment; medication group A levodopa/group B placebo assigned enrollment and intervention phases through taper, marked end treatment at Visit 2. Inclusion/exclusion prescreen and enrollment; demographics prescreen; history and pregnancy at enrollment; physical examination enrollment, Visits 2–5 and unscheduled; rehabilitation concomitant therapies enrollment, intervention/transition/full dose/taper, Visits 2–5, unscheduled; concomitant medication those points plus telephone Visits 6–9; accountability enrollment and Visit 2, unscheduled conditional; optional blood sampling enrollment.

Outcome rows: FMA (primary) enrollment, Visits 2–5, unscheduled; NIH Stroke Scale prescreen, enrollment, Visits 2–5, unscheduled; mRS enrollment, Visits 2–9, unscheduled; PROMIS-10 Visits 2–9, unscheduled; PROMIS-29 Visits 2–5, unscheduled; patient-reported improvement Visits 2–9, unscheduled; Rivermead Mobility Index enrollment, Visits 2–9, unscheduled. Optional selected-center rows Action Research Arm Test, Box and Block Test, Jamar dynamometer Test, Motricity index, Trunk control, 10-meter walk and Montreal Cognitive Assessment: enrollment, Visits 2–5, unscheduled; functional ambulation categories additionally Visits 6–9. Optional daily activity movement sensors enrollment and Visits 2–5, unscheduled. Mortality/all cause and any recurrent stroke monitored intervention/transition/full dose/taper, Visits 2–9, unscheduled; AE/SAE intervention through Visit 3 and conditional unscheduled, no scheduled marks after Visit 3.

Footnotes: transition has no in-person visit, data collection on transfer acute-to-rehabilitation any intervention day; double asterisk optional/selected centers, blood may be sampled baseline or any follow-up; unscheduled visit upon discontinuation/consent withdrawal, [x] accountability only before treatment end and AE/SAE only before Visit 3; unscheduled outcomes subject to participant approval. Main matching keys primary three-month window, intervention 39-day regimen, secondary outcome times/status, extended observation; role remains REPORT schedule, not separate PLAN.

## N-R006 — Enrollment figure printed totals

[DOC-004 p22](../../../joi250066supp3_prod_1761597796.4701.pdf#page=22), eFigure 3. All n=610; University Hospital Basel n=318; University Hospital Zurich n=70; Hôpital de Fribourg n=57; Inselspital Bern n=52; CHUV Lausanne n=25; Klinik Hirslanden Zürich n=24; Kantonsspital St. Gallen n=19; Kantonsspital Münsterlingen n=15; Kantonsspital Winterthur n=13; Kantonsspital Baden n=8; Kantonsspital Graubünden n=8; Kantonsspital Aarau n=1. Y-axis Patients included, ticks 0,200,400,600. X-axis Date of randomization, ticks 2020,2021,2022,2023,2024. Curves show cumulative recruitment; exact recruitment dates and intermediate counts not printed, so not digitized. Match main total randomized and administrative centers only.

## S-R015 — eFigure 4 forest plot

[DOC-004 p23](../../../joi250066supp3_prod_1761597796.4701.pdf#page=23), continued [p24](../../../joi250066supp3_prod_1761597796.4701.pdf#page=24). Title total FMA estimands at three months, levodopa vs placebo. X-axis Adjusted Mean Difference (FMMA points), ticks −4,−2,0,2; null line 0, left favoring placebo, right favoring levodopa. Rows 1,2,3,5,6,7,8; estimand 4 not plotted because displayed ratio elsewhere. Every plotted interval crosses 0; point 7 is to right, other points to left. No numeric estimate/CI annotation; numeric counterparts are S-R007, not digitized from pixels. Caption 1 excludes deaths (primary treatment policy), 2 missing/incomplete complete case, 3 deaths imputed. Continuation 5 excludes motor-impairing SAE hypothetical/on treatment phrase; 6 intake<80%; 7 fewer rehabilitation therapies; 8 out-of-range three-month visits. Caption-based contrast and units captured; matching main sensitivity results use S-R007.

## N-R007 — eFigure 5 by-center display

[DOC-004 p25](../../../joi250066supp3_prod_1761597796.4701.pdf#page=25). Title FMA at three months by treatment arm and center. Five facets HFR, INS, USB, USZ, other; each Placebo/Levodopa. Y-axis FMMA affected side (change Visit 1 to Visit 3), ticks −50,0,50; x-axis medication. Points, boxes/medians/whiskers without numeric summaries or sample-size annotations. Centers with <50 recruitments pooled Other. All facet labels, arms, axis quantity and threshold captured; no exact medians/quantiles inferred from graphics. Matching key baseline-to-three-month change, eTable 3 estimand 9, main center/subgroup display; title and actual axis quantities retained separately.

## S-R016 — eFigure 6 spline graphic

[DOC-004 p26](../../../joi250066supp3_prod_1761597796.4701.pdf#page=26). Title nonlinear association between baseline and three-month FMA (spline model); plot title Predicted values of fma affected Visit 3. Y-axis fma affected Visit 3, ticks 30,60,90. X-axis fma affected Visit 1.cent, ticks −40,−20,0,20,40,60. Increasing nonlinear red prediction curve with shaded band; no numeric prediction limits, treatment contrast, sample sizes or band confidence-level label printed. Caption says Figure 4: main estimate including FMAA at baseline as spline, estimated marginal effects. Capture figure label as printed without changing source. Matches spline terms/test S-R011 and baseline predictor center in code.

## S-R017 — eFigure 7 post hoc/subgroups

[DOC-004 p27](../../../joi250066supp3_prod_1761597796.4701.pdf#page=27). Rows PH1,PH2,PH3; x-axis estimate ticks −6,−3,0,3; y-axis model; null vertical 0. Top legend black comment, green moderate–severe impairment, purple very severe impairment. PH1 black near 0, PH2 black right of 0, PH3 green right and purple left; all four horizontal intervals cross 0. No exact numeric effect/CI/P/N annotations, so no digitization or invented precision. Caption PH1 primary analysis model with death missing outcomes imputed as 0; PH2 primary model excluding low baseline intake and minimal documented rehabilitation; PH3 baseline FMA severe ≤35 vs mild-to-moderate >35. Preserve caption and top-legend severity names separately. PH1 matches eTable 3 estimand 10, PH2 estimand 11; PH3 matches main baseline severity subgroup/post hoc analysis, with printed cutoff 35. Label alone does not identify quantitative subgroup effects to finer precision than their graphical sign/null crossing.

## S-R018 — Implemented main analysis code

[DOC-006 p1](../../../joi250066supp5_prod_1761597796.4751.pdf#page=1), printed lines 1–35; visually read usable image, no usable historical code text relied upon. Title ESTREL Main Analysis Code. Packages ggplot2 and mice lines 4–5. Lines 8–10 load raw dat/dat.rda and dat/mice0.rds (comment imputations on FAS), define N.imp as length(mice0$imp[[1]]); number of imputations is data-driven in code, no literal 100 here. Lines 13–16 raw boxplot/jitter by medication with y my.data[, ep], white outlier color, theme_bw and ylab(ep.name). Lines 19–21 comments identify fma_affected.Visit_3 primary endpoint, fma_affected.Visit_1.cent centered baseline, medication randomized group.

Exact analysis formula lines 22–23: `model <- with(mice0, lm(fma_affected.Visit_3 ~ fma_affected.Visit_1.cent + medication))`. Pool/return lines 25–26: `summary(pool(model))`. Diagnostic lines 29–35 set par(mfrow=c(2,2)), loop i over 1:N.imp, fit same formula using `data = complete(my.data = mice0, i)`, plot with main paste0("Imputation: ", i), then par(mfrow=c(1,1)). This is implemented ordinary linear model of follow-up affected-side FMA on centered baseline and treatment, pooled over imputed FAS data. No treatment/baseline interaction, spline, center covariate/random term, additional covariate or outcome change expression appears in the main formula. Diagnostic formula identical. Missing-data generation and raw data not supplied in this PDF; no raw-data execution attempted. Match main primary analysis, S-R002 pooling, S-R007 estimand 1, S-R008 change-score analysis and SAP main model. Code's plotted variables ep/ep.name are referenced but not defined in this page; preserve that boundary without assumptions.

## S-R019 — Data-sharing scope and availability

[DOC-007 p1](../../../joi250066supp6_prod_1761597796.4801.pdf#page=1). Publication September 22, 2025; trial registry identifier NCT03735901 and BASEC-ID 2018-02021. Printed Data available: No. Subsequent explanation trial data can be made available on reasonable request to corresponding author, with detailed proposal, objectives and SAP; additional material may be requested; approvals sponsor-investigator/corresponding author, steering committee and center principal investigators; compatibility ethics/regulatory and consent checked. Administrative evidence, no numeric result, planned decision rule, or supplied participant dataset. Neither online registry nor request pathway accessed.

## Matching and completeness handoff

Exact source-page links above are package-relative from this extraction file. All source matching uses result identity, endpoint/time, population, contrast, adjustment/model and statistical scale; figures with no printed numeric values are recorded as graphical-only evidence. N-R002 row keys span all baseline rows; N-R003/S-R009 .01–.10 span all secondary outcomes; N-R004/N-R005 span all harm counts; S-R007 estimands 1–8 and S-R008 9–11 are complete; S-R010/S-R011 cover all coefficient/test rows. Administrative units were opened individually through usable page-preserving layouts; no unit omitted by assuming absence of extraction means absence of content.

Coverage: DOC-004 27/27, DOC-005 8/8, DOC-006 1/1, DOC-007 1/1. Reusable-backed units 37, fresh-required 0, scientific gaps 0. Limitations: native extraction lacks embedded graphic/table values on DOC-004 p18 and graphic pages21–23,25–27 and code DOC-006 p1, all closed by visual mapping. Exact graphical-only values in center boxplots, spline curve/band and subgroup forest plot are not printed and are not assigned artificial precision. No additional workbook/CSV/DOC/DOCX support within assignment. No old conclusions used.
