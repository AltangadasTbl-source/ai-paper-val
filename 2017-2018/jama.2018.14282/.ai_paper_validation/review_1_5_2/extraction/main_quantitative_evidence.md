# Main-article quantitative evidence extraction — DOC-001

## Scope and source assets

Complete fresh mapping of `jama_azoulay_2018_oi_180109.pdf`, PDF pages 1-9 (DOC-001). Native and layout text were usable for every page. Result-relevant pages 1-8 were also freshly rendered; page 9 was administrative/reference material and was not rendered. Source links below are relative to this artifact.

| PDF page | Fresh evidence assets | Result-relevant quantitative coverage |
|---|---|---|
| 1 | `preprocessing/native_text/pages/DOC-001/p001.txt`; `preprocessing/layout_text/pages/DOC-001/p001.txt`; `preprocessing/rendered_pages/DOC-001-p001.png` | Abstract: trial size, baseline summaries, primary and named secondary outcomes. |
| 2 | `preprocessing/native_text/pages/DOC-001/p002.txt`; `preprocessing/layout_text/pages/DOC-001/p002.txt`; `preprocessing/rendered_pages/DOC-001-p002.png` | Key Points, eligibility thresholds, recruitment/ICU counts, randomization and treatment parameters. |
| 3 | `preprocessing/native_text/pages/DOC-001/p003.txt`; `preprocessing/layout_text/pages/DOC-001/p003.txt`; `preprocessing/rendered_pages/DOC-001-p003.png` | Figure 1 flow; outcome scales; sample-size and analysis specifications. |
| 4 | `preprocessing/native_text/pages/DOC-001/p004.txt`; `preprocessing/layout_text/pages/DOC-001/p004.txt`; `preprocessing/rendered_pages/DOC-001-p004.png` | Table 1 baseline counts, denominators, percentages, medians/IQRs, and analysis specifications. |
| 5 | `preprocessing/native_text/pages/DOC-001/p005.txt`; `preprocessing/layout_text/pages/DOC-001/p005.txt`; `preprocessing/rendered_pages/DOC-001-p005.png` | Table 2, patients/interventions/results narrative, primary outcome. |
| 6 | `preprocessing/native_text/pages/DOC-001/p006.txt`; `preprocessing/layout_text/pages/DOC-001/p006.txt`; `preprocessing/rendered_pages/DOC-001-p006.png` | Figure 2 risk sets; secondary and post-hoc outcomes. |
| 7 | `preprocessing/native_text/pages/DOC-001/p007.txt`; `preprocessing/layout_text/pages/DOC-001/p007.txt`; `preprocessing/rendered_pages/DOC-001-p007.png` | Figure 3 subgroup counts, HRs/CIs, interaction P values. |
| 8 | `preprocessing/native_text/pages/DOC-001/p008.txt`; `preprocessing/layout_text/pages/DOC-001/p008.txt`; `preprocessing/rendered_pages/DOC-001-p008.png` | Discussion/conclusion repeats of effect direction and exploratory-secondary-analysis qualification. |
| 9 | `preprocessing/native_text/pages/DOC-001/p009.txt`; `preprocessing/layout_text/pages/DOC-001/p009.txt` | No applicable trial result relationship: data-sharing pointer and references only. |

## Extracted result-relevant evidence by source location

### PDF p. 1 — Abstract

- Population/design: 776 adult immunocompromised patients with AHRF, 32 ICUs in France, May 19, 2016 to December 31, 2017; 1:1 allocation, n=388 high-flow and n=388 standard oxygen.
- Randomized/completed: 778 randomized; 776 (99.7%) completed. Median age 64 years (IQR 54-71); 259 (33.3%) women.
- Baseline: respiratory rate 33/min (IQR 28-39) vs 32/min (27-38); PaO2:FIO2 136 (96-187) vs 128 (92-164); SOFA 6 (4-8) in both groups.
- Day-28 mortality: 35.6% vs 36.1%; difference −0.5% (95% CI −7.3% to +6.3%); HR 0.98 (95% CI 0.77-1.24); P=.94.
- IMV: 38.7% vs 43.8%; difference −5.1% (95% CI −12.3% to +2.0%). Other stated results: PaO2:FIO2 150 vs 119, difference 19.5 (4.4-34.6); respiratory rate at 6 h 25/min vs 26/min, difference −1.8/min (−3.2 to −0.2); ICU stay 8 vs 6 d, difference 0.6 (−1.0 to +2.2); ICU infection 10.0% vs 10.6%, difference −0.6% (−4.6 to +4.1); hospital stay 24 vs 27 d, difference −2 d (−7.3 to +3.3).

### PDF pp. 2-3 — methods, definitions, Figure 1, and analysis plan

- Eligibility/scale parameters: age >=18 years; AHRF PaO2 <60 mm Hg or SpO2 <90% on room air, tachypnea >30/min, and oxygen need >=6 L/min. Randomization strata: center, oxygen flow >9 versus <=9 L/min, vasopressors, and ICU time <=2 versus >=3 d; fixed block size 4. Treatment initiated within 15 min; high-flow initiated 50 L/min and FIO2 100%, >=50 L/min in first 3 d, up to 60 L/min as needed, SpO2 target >=95%.
- Outcome labels/scales: primary all-cause mortality within 28 days. Secondary IMV by day 28; respiratory rate normal 12-20/min; PaO2:FIO2 normal 500-600 and <300 severe gas-exchange dysfunction; comfort 0 (severe discomfort) to 10 (perfect comfort); dyspnea 0 (no dyspnea) to 10 (severe dyspnea); ICU/hospital length of stay and ICU-acquired infection incidence.
- Figure 1: 1464 assessed; 686 excluded = 524 not meeting criteria +95 declined +67 other; 778 randomized =389 per group. High-flow: 376 received allocated intervention, 13 did not (1 withdrew consent, 12 discomfort), 0 lost, 388 primary analysis (1 excluded). Standard: 358 received allocated intervention, 31 did not (1 withdrew consent, 30 received high-flow), 0 lost, 388 primary analysis (1 excluded). Exclusion reasons were unavailable in all centers.
- Sample-size/interim specifications: anticipated standard mortality 30% and high-flow 20%; alpha 5%; 779 (389/group) for 90% power. Interim at 100 deaths, Haybittle-Peto P threshold .001. ITT includes randomized allocation except withdrawn consent; no missing/incomplete-data exclusions. Mortality Kaplan-Meier with day-28 ICU administrative censoring; absolute risk difference and univariable Cox HR/95% CI; PH check P=.72. IMV has death without IMV competing risk, nonparametric cumulative incidence/Gray test and cause-specific Cox HR. ICU infection chi-square; other named continuous outcomes Wilcoxon rank-sum; ICU/hospital mortality RR. All reported P values 2-sided; P<.05 significant; R 3.1.0.

### PDF p. 4 — Table 1 and methods continuation

- Table 1 denominators are 388 high-flow and 388 standard. Exact displayed baseline values are mapped in `MAIN-N009` through `MAIN-N017`: sex; chronic comorbidity; underlying condition and its subcategories; treatment/ transplant fractions; randomization timing; postextubation; SOFA/SAPS II; goals of care; pre-randomization respiratory variables and oxygen therapy.
- Table 1 footnotes define chronic respiratory insufficiency; Charlson range 19-114; underlying-condition component counts (acute myeloid leukemia n=123, non-Hodgkin lymphoma n=97, myeloma n=41; solid tumor lung n=72, digestive n=60, breast n=30; steroids n=174; kidney transplant n=46, liver n=19); SOFA range 0-24 and score 7-9 mortality risk 15%-20%; SAPS II 0-163 and score 36 mortality risk 18%-20%.
- Methods continuation: subgroup Cox HRs use the listed stratification variables; Gail-Simon interaction test; secondary analyses exploratory because no multiplicity handling; post hoc site/frailty and intubated-patient analyses.

### PDF p. 5 — Table 2 and results narrative

- Table 2 exact outcomes: mortality 138/388 (35.6%) vs 140/388 (36.1%), RD −0.5% (−7.3 to 6.3), HR .98 (.77-1.24), P=.94; IMV 150 (38.7%) vs 170 (43.8%), RD −5.1% (−12.3 to 2.0), cause-specific HR .85 (.68-1.06), P=.17; infection 39 (10.0%) vs 41 (10.6%), RD −.6% (−4.6 to 4.1), cause-specific HR 1.01 (.96-1.06), P=.91; ICU mortality 123 (31.7%) vs 122 (31.4%), RD .3% (−6.3 to 6.8), RR 1.01 (.82-1.24), P=.64; hospital mortality 160 (41.2%) vs 162 (41.7%), RD −.5% (−7.5 to 6.4), RR .99 (.84-1.17), P=.77; ICU stay 8 (4-14) vs 6 (4-13), mean difference .6 (−1.0 to 2.2), P=.07; hospital stay 24 (14-40) vs 27 (15-42), mean difference −2 (−7.3 to 3.3), P=.60. No loss to follow-up; binary mean difference means absolute risk difference, quantitative mean difference means difference in means.
- Results repeat the randomized/completed numbers, baseline respiratory values, 320 bacterial pneumonia, 91 invasive fungal infection including 59 Pneumocystis, 80 underlying-disease lung involvement; 32 (4.1%) baseline DNR/DNI (16/group), later 37 (4.8%; 20 vs 17) acquired such status. High-flow intolerance: 12 (3%) switch, 3 died. Standard devices: 29.5%, 23.5%, 40.6%, 6.4%; among 30 (7.7%) switched standard patients, 14 (46.7%) died. Interim P=.94 after 100 deaths.

### PDF p. 6 — Figure 2 and secondary/post-hoc outcomes

- Figure 2 mortality curve: log-rank P=.85; risk sets high-flow 388,365,338,322,305,292,275,266,261,256,0 and standard 388,360,336,318,301,287,272,263,263,253,0 at days 0,3,...,30. Median survival not reached in either group.
- Secondary narrative repeats IMV and gives cause-specific HR .85 (.68-1.06), P=.17; respiratory rate 25 vs 26/min at 6 h, mean difference −1.8 (−3.2 to −.3); PaO2:FIO2 150 vs 119, difference 19.5 (4.4-34.6) through day 4; table-2 ICU/hospital/infection results. The abstract’s upper CI for respiratory-rate difference is −.2 whereas this narrative prints −.3; both locations are retained for cross-source review.
- Post hoc: center effect mortality P=.33, intubation P=.07; vasopressors/renal replacement 153 (19.7%) high-flow and 31 (4.0%) standard; high-flow duration 2 d (IQR 1-5), discharge oxygen 3 L/min, IMV time 1 d (0-2), difference −.5 d (−1.2 to .1); intubated mortality 55.3% vs 52.3%, RD +3% (−8.5 to +14.5), P=.65; limitation decisions 170 (21.9%), 135 (79.4%) deaths; cancer versus noncancer mortality RD +1.8% (−10.8 to +14.3), P=.50; day-90 mortality 46.9% vs 48.2%.

### PDF p. 7 — Figure 3

- Figure 3 contains day-28-mortality and IMV subgroup event/total records, HRs/95% CIs and interaction P values. Every displayed subgroup row is transcribed in `MAIN-S014` and `MAIN-S015`, including all-patient rows (mortality 138/388 vs 140/388, HR 1.02 [.81-1.29]; IMV 150/388 vs 170/388, HR 1.17 [.94-1.46]). Figure uses Gail-Simon interaction test; squares are proportional to subgroup size except all-patient open squares; error bars are 95% CIs.

### PDF pp. 8-9

- Page 8 reiterates no significant day-28 mortality reduction and states secondary analyses are exploratory because repeated testing can produce false positives. No new numeric trial-effect estimate is printed.
- Page 9: no applicable result relationship (data-sharing statement points to Supplement 3; remaining content is references).

All source locations: [DOC-001 PDF](../../../jama_azoulay_2018_oi_180109.pdf#page=1).
