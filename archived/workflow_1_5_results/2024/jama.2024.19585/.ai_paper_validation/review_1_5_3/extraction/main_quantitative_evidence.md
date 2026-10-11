# Main Quantitative Evidence Map — DOC-001

## Scope and method

- **Assigned direct source:** `jama_dupuis_2024_oi_240111_1733431204.38761.pdf` (DOC-001), PDF pp. 1-11 only.
- **Source authority:** the supplied PDF; each location below uses `jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=N`.
- **Reusable locators used:** the complete one-page native-text set at `document_outputs/DOC-001/native_text/page-001.txt` through `page-011.txt`; rendered source pages `document_outputs/DOC-001/images/page-005.png` through `page-009.png` for Figure 1, Tables 1-3, and Figure 2.
- **Fresh direct confirmation:** `pdftotext -layout` was run directly on DOC-001 and saved as `preprocessing/main_quantitative_mapper/DOC-001-layout.txt`. The PDF reports 11 pages. Rendered pages 5-9 were visually inspected against the source for the displayed figures and tables. No OCR was needed.
- **Boundary:** this is an evidence/relationship map, not candidate diagnosis or adjudication. Values repeated in the abstract, key points, narrative, tables, figures, captions, and footnotes are retained as matching occurrences.

## Page coverage and no-applicable units

| PDF page | Result-relevant content mapped | Mapping status |
|---|---|---|
| 1 | Abstract: design, randomized sites, enrolled population, primary/secondary outcome definitions, primary and emergency-department results | COMPLETE |
| 2 | Key Points, site randomization, eligibility, care-pathway adoption/adaptation/rejection percentages | COMPLETE |
| 3 | Outcome scales, assessment times, power assumptions, analysis model and covariates | COMPLETE |
| 4 | Results narrative: flow totals, missingness, ICC, completed assessments, primary and sensitivity results, individual outcome summary | COMPLETE |
| 5 | Figure 1 participant/site flow and narrative documentation/intervention counts, proportions, and P values | COMPLETE |
| 6 | Table 1 baseline population; continuation of intervention narrative; repeated emergency-department result | COMPLETE |
| 7 | Table 2 primary and secondary patient-reported outcome values and all adjusted statistics/intervals/P values | COMPLETE |
| 8 | Figure 2, an unlabeled stacked-percent display of all 15 SSPedi symptoms at baseline and week 8 | COMPLETE; no exact bar-segment values printed |
| 9 | Table 3 encounter means, SDs, rates, distributions, effects, intervals, P values, and footnotes | COMPLETE |
| 10 | Conclusion/limitations narrative, including the 3.8-point total-SSPedi reduction claim | COMPLETE |
| 11 | References only; no result-relevant quantitative relationship applicable | COMPLETE — no applicable unit |

## Study population, scales, timing, and analysis labels

| ID | Direct-source evidence and relationship | Exact location |
|---|---|---|
| N001 | Cluster randomized trial at 20 US pediatric oncology sites; 10 sites assigned to symptom screening and 10 to usual care. | PDF p. 1; PDF p. 2; PDF p. 5 Figure 1 |
| N002 | Eligible population: English- or Spanish-speaking patients newly diagnosed with cancer, aged 8-18 years, planned for chemotherapy, radiotherapy, or operation; enrollment within 28 days after treatment initiation or diagnosis, whichever was later. | PDF p. 2 |
| N003 | Enrollment/follow-up dates: enrollment July 2021-August 2023 in abstract; results specify July 27, 2021-August 22, 2023; final follow-up October 18, 2023. | PDF p. 1; PDF p. 4 |
| N004 | The intervention prompted symptom screening 3 times weekly through SPARK; the control group received usual care. | PDF p. 2; PDF p. 3 |
| N005 | Care-pathway template statements: 40.8% adopted, 48.7% adapted, and 6.4% rejected; site-specific rejection range 3.7%-18.5%. | PDF p. 2 |
| N006 | Primary outcome: self-reported total SSPedi at week 8, sum of 15 item scores, range 0-60; 0=no bothersome symptoms and 60=most bothersome symptoms; recall period “yesterday or today.” | PDF p. 1; PDF p. 3; PDF p. 7 Table 2 footnote a |
| N007 | Individual SSPedi symptom scale: 15 symptoms, each score 0-4; Figure 2 labels 0 least/not at all bothered and 4 most/extremely bothered. | PDF p. 3; PDF p. 8 Figure 2/caption |
| N008 | PROMIS Fatigue uses the past-7-day recall and is scaled to mean (SD) 50 (10) against the US general population; higher score=more fatigue. | PDF p. 1; PDF p. 3; PDF p. 7 Table 2 footnote a |
| N009 | PedsQL 3.0 Acute Cancer Module has eight domains, scale 0-100, past-7-day recall, higher score=better health. | PDF p. 1; PDF p. 3; PDF p. 7 Table 2 footnote a |
| N010 | Patient-reported outcomes were measured at baseline, week 4 (±1 week), and week 8 (±1 week); documentation/intervention window was 3 days, from 1 day before through 1 day after the week-4 and week-8 assessment points. | PDF p. 3 |
| N011 | Unplanned encounters were emergency-department visits, unplanned clinic visits, and unplanned hospitalizations over 8 weeks; no participant had less than 8 weeks of follow-up. | PDF p. 3; PDF p. 9 Table 3 footnote a |
| N012 | Planned sample size/power inputs: 444 participants; 85% power; minimal clinically important difference 3; within-cluster SD 8.8; ICC 0.021; alpha=.05; baseline covariate explaining 20% of variance; 10% missing data. | PDF p. 3 |
| S001 | Primary analysis: patient-level week-8 total SSPedi in mixed linear regression with random site effect; fixed treatment, age (8-10, 11-14, 15-18), diagnosis group (leukemia/lymphoma, solid/brain tumor), and two cluster-level stratification covariates. Effect=adjusted mean difference with 95% CI; P is based on difference in mean week-8 score, not mean change. | PDF p. 3; PDF p. 7 Table 2 footnotes b-c |
| S002 | Individual SSPedi symptoms used mixed-effects proportional-odds models with random site effect and fixed treatment plus two stratification variables; effect=OR with 95% CI. | PDF p. 4; PDF p. 7 Table 2 footnote b |
| S003 | PROMIS Fatigue and PedsQL domains used the primary-outcome approach; documentation/intervention comparisons used mixed or fixed-effects logistic regression with OR/95% CI; encounter comparisons used mixed-effects Poisson regression with random site effect and the two stratification variables. | PDF p. 4; PDF p. 9 Table 3 footnote b |
| S004 | All significance tests were 2-sided and P<.05 was the stated significance criterion; analyses used R 4.3.2. | PDF p. 4 |

## Enrollment and analysis populations

| ID | Direct-source evidence and relationship | Exact location |
|---|---|---|
| N013 | Overall enrolled population: 445 participants, 221 at intervention sites and 224 at control sites; 15 enrolled as medical-record-review-only participants. | PDF p. 1; PDF p. 4; PDF p. 5 Figure 1 |
| N014 | Overall baseline age/sex: median (range) age 14.8 (8.1-18.9) years; 262/445 (58.9%) male. | PDF p. 1; PDF p. 4 |
| N015 | Results narrative screening/enrollment totals: 687 patients assessed for eligibility, 530 approached, and 445 enrolled between July 27, 2021, and August 22, 2023. The Figure 1 branch totals provide the matching 364+323=687 screened and 265+265=530 invited/approached counts. | PDF p. 4; PDF p. 5 Figure 1 |
| N016 | Figure 1 site flow: 20 invited and randomized sites; 10 symptom-screening sites and 10 usual-care sites. | PDF p. 5 Figure 1 |
| N017 | Figure 1 symptom-screening site flow: 472 considered; 108 missed; 364 screened; 99 excluded (42 physician preference [32 not under oncology care/unable to approach, 4 disease status/progression, 2 psychosocial issues, 4 no reason], 26 outside trial network, 16 cognitive disability, 8 language, 3 visual impairment, 3 no parent, 1 cancer not disclosed); 265 invited; 44 declined (29 not interested, 12 too stressed/overwhelmed, 2 no reason, 1 too busy); 221 enrolled. | PDF p. 5 Figure 1 |
| N018 | Figure 1 usual-care site flow: 387 considered; 64 missed; 323 screened; 58 excluded (13 physician preference, 7 disease status/progression, 4 psychosocial issues, 2 no reason, 15 outside trial network, 14 cognitive disability, 7 language, 4 visual impairment, 3 no parent, 2 cancer not disclosed); 265 invited; 41 declined (20 not interested, 19 too stressed/overwhelmed, 2 too busy); 224 enrolled. | PDF p. 5 Figure 1 |
| N019 | Symptom-screening follow-up: 217 agreed to patient-reported outcomes; 198 completed all 8-week surveys including SSPedi; 19 did not complete all surveys (7 missed window, 4 omitted SSPedi, 3 too sick/overwhelmed, 2 declined, 2 switched to medical-record review only, 1 moved off study); 4 medical-record-review only; 198 primary, 202 secondary patient-reported, and 220 medical-record-review analysis participants. | PDF p. 5 Figure 1 |
| N020 | Usual-care follow-up: 213 agreed to patient-reported outcomes; 209 completed all 8-week surveys including SSPedi; 4 did not complete 8-week patient-reported outcomes (2 missed window, 1 declined, 1 switched to medical-record review only); 11 medical-record-review only; 209 primary, 209 secondary patient-reported, and 224 medical-record-review analysis participants. | PDF p. 5 Figure 1 |
| S005 | Declining participation: 16.6% at intervention vs 15.5% at control sites; P=.81, described as no significant difference. | PDF p. 4 |
| N021 | Missing week-8 SSPedi scores: 38/445 (8.5%) overall and 23/430 (5.3%) among non-medical-record-review-only participants. | PDF p. 4 |
| N022 | The results narrative says only 1 participant did not complete the planned observations. Completed SSPedi counts: symptom screening 216 baseline, 208 week 4, 198 week 8; usual care 213 baseline, 207 week 4, 209 week 8. | PDF p. 4 |
| N023 | Observed posterior 8-week total-SSPedi ICC median 0.06 (95% credible interval 0.01-0.16); site-size coefficient of variation 0.61. | PDF p. 4 |

## Table 1 — baseline demographic characteristics

Table 1 population is symptom screening n=221 and usual care n=224 unless a row supplies another denominator. All values are No. (%) except the two reported medians.

| ID | Characteristic: symptom screening vs usual care | Exact location |
|---|---|---|
| N075 | Male 133 (60.2%) vs 129 (57.6%); female 88 (39.8%) vs 95 (42.4%). | PDF p. 6 Table 1 |
| N024 | Age, median (range), years: 15.0 (8.1-18.9) vs 14.7 (8.1-18.9). | PDF p. 6 Table 1 |
| N025 | Age 8-10 years 33 (14.9%) vs 37 (16.5%); 11-14 years 77 (34.8%) vs 85 (37.9%); 15-18 years 111 (50.2%) vs 102 (45.5%). | PDF p. 6 Table 1 |
| N026 | Race denominators: n=177 vs n=183. American Indian/Alaska Native 2 (1.1%) vs 4 (2.2%); Asian 13 (7.3%) vs 7 (3.8%); Black/African American 13 (7.3%) vs 14 (7.7%); Native Hawaiian/Other Pacific Islander 14 (7.9%) vs 1 (0.5%); White 113 (63.8%) vs 145 (79.2%); more than one race 22 (12.4%) vs 12 (6.6%). | PDF p. 6 Table 1 |
| N027 | Ethnicity denominators: n=208 vs n=202. Hispanic/Latino 85 (40.9%) vs 63 (31.2%); not Hispanic/Latino 123 (59.1%) vs 139 (68.8%). | PDF p. 6 Table 1 |
| N028 | First language English or Spanish 211 (95.5%) vs 197 (87.9%); inpatient at enrollment 88 (39.8%) vs 88 (39.3%). | PDF p. 6 Table 1 |
| N029 | Preferred patient-reported-outcome language: English 203 (91.9%) vs 201 (89.7%); Spanish 13 (5.9%) vs 12 (5.4%); not applicable/not available 5 (2.3%) vs 11 (4.9%). The footnote attributes not applicable to medical-record-review-only participants and not available to the immediate withdrawal. | PDF p. 6 Table 1 and footnote b |
| N030 | Guardian married 138 (62.4%) vs 141 (62.9%); guardian employed full/part time 125 (56.6%) vs 127 (56.7%); guardian college graduate or higher 120 (54.3%) vs 133 (59.4%); annual household income >=$60,000: 78 (35.3%) vs 103 (46.0%). | PDF p. 6 Table 1 |
| N031 | Cancer diagnosis: leukemia 89 (40.3%) vs 62 (27.7%); solid tumor 73 (33.0%) vs 86 (38.4%); lymphoma 50 (22.6%) vs 61 (27.2%); brain tumor 9 (4.1%) vs 15 (6.7%). | PDF p. 6 Table 1 |
| N032 | Metastatic disease 45 (20.4%) vs 80 (35.7%); diagnosis-to-enrollment median (IQR) days 23 (16-29) vs 21 (13-28). | PDF p. 6 Table 1 |
| N033 | Planned/received treatment: chemotherapy 210 (95.0%) vs 207 (92.4%); radiotherapy 20 (9.0%) vs 18 (8.0%); surgical procedure 23 (10.4%) vs 36 (16.1%). | PDF p. 6 Table 1 |

## Primary outcome, symptom outcomes, fatigue, and quality of life — Table 2

Table 2 baseline denominators are symptom screening n=216 and usual care n=213; week-8 SSPedi denominators are n=198 and n=209. Other PRO denominators are n=216/n=213 at baseline and n=202/n=209 at week 8. Table footnotes define the continuous-outcome adjusted model and individual-symptom OR model in S001-S003.

| ID | Outcome: baseline screening vs usual care; week-8 screening vs usual care; unadjusted effect; adjusted effect; adjusted P value | Exact location |
|---|---|---|
| S006 / N034 | **Total SSPedi, mean (SD):** 11.8 (8.2) vs 13.5 (8.2); 7.9 (7.2) vs 11.4 (8.7); mean difference -3.7 (95% CI -6.3 to -1.1); adjusted -3.8 (-6.4 to -1.2); P=.007. Matching abstract/key-points/narrative claims give 7.9 vs 11.4 and adjusted mean difference -3.8 (95% CI -6.4 to -1.2). | PDF p. 1; PDF p. 2; PDF p. 4; PDF p. 7 Table 2 |
| S007 / N035 | **Feeling disappointed/sad, score 3-4:** 12 (5.6%) vs 15 (7.0%); 5 (2.5%) vs 11 (5.3%); OR 0.46 (0.24-0.89); adjusted OR 0.46 (0.26-0.83); P=.01. | PDF p. 7 Table 2 |
| S008 / N036 | **Feeling scared/worried:** 11 (5.1%) vs 23 (10.8%); 6 (3.0%) vs 7 (3.3%); OR 0.58 (0.38-0.88); adjusted 0.57 (0.38-0.85); P=.005. | PDF p. 7 Table 2 |
| S009 / N037 | **Feeling cranky/angry:** 9 (4.2%) vs 10 (4.7%); 5 (2.5%) vs 12 (5.7%); OR 0.43 (0.29-0.63); adjusted 0.43 (0.29-0.63); P<.001. | PDF p. 7 Table 2 |
| S010 / N038 | **Problems thinking/remembering:** 15 (6.9%) vs 11 (5.2%); 7 (3.5%) vs 14 (6.7%); OR 0.60 (0.38-0.95); adjusted 0.62 (0.42-0.90); P=.01. | PDF p. 7 Table 2 |
| S011 / N039 | **Changes in body/face look:** 23 (10.6%) vs 24 (11.3%); 4 (2.0%) vs 21 (10.0%); OR 0.51 (0.30-0.89); adjusted 0.52 (0.31-0.88); P=.01. | PDF p. 7 Table 2 |
| S012 / N040 | **Feeling tired:** 57 (26.4%) vs 74 (34.7%); 28 (14.1%) vs 52 (24.9%); OR 0.52 (0.36-0.74); adjusted 0.52 (0.36-0.74); P<.001. | PDF p. 7 Table 2 |
| S013 / N041 | **Mouth sores:** 8 (3.7%) vs 12 (5.6%); 0 (0.0%) vs 8 (3.8%); OR 0.49 (0.28-0.86); adjusted 0.48 (0.27-0.85); P=.01. | PDF p. 7 Table 2 |
| S014 / N042 | **Headache:** 8 (3.7%) vs 21 (9.9%); 10 (5.1%) vs 10 (4.8%); OR 0.60 (0.41-0.89); adjusted 0.61 (0.41-0.90); P=.01. | PDF p. 7 Table 2 |
| S015 / N043 | **Hurt/pain other than headache:** 10 (4.6%) vs 16 (7.5%); 11 (5.6%) vs 11 (5.3%); OR 0.70 (0.48-1.03); adjusted 0.69 (0.47-1.01); P=.06. | PDF p. 7 Table 2 |
| S016 / N044 | **Tingly/numb hands or feet:** 10 (4.6%) vs 11 (5.2%); 4 (2.0%) vs 10 (4.8%); OR 0.76 (0.50-1.15); adjusted 0.76 (0.50-1.15); P=.19. | PDF p. 7 Table 2 |
| S017 / N045 | **Throwing up/feeling like throwing up:** 23 (10.6%) vs 29 (13.6%); 19 (9.6%) vs 27 (12.9%); OR 0.81 (0.50-1.34); adjusted 0.80 (0.51-1.26); P=.34. | PDF p. 7 Table 2 |
| S018 / N046 | **Feeling more/less hungry:** 49 (22.7%) vs 51 (23.9%); 15 (7.6%) vs 35 (16.7%); OR 0.63 (0.43-0.94); adjusted 0.63 (0.44-0.90); P=.01. | PDF p. 7 Table 2 |
| S019 / N047 | **Changes in taste:** 31 (14.4%) vs 34 (16.0%); 11 (5.6%) vs 25 (12.0%); OR 0.56 (0.33-0.93); adjusted 0.56 (0.34-0.90); P=.02. | PDF p. 7 Table 2 |
| S020 / N048 | **Constipation:** 16 (7.4%) vs 20 (9.4%); 2 (1.0%) vs 9 (4.3%); OR 0.53 (0.27-1.06); adjusted 0.55 (0.31-0.95); P=.03. | PDF p. 7 Table 2 |
| S021 / N049 | **Diarrhea:** 18 (8.3%) vs 10 (4.7%); 4 (2.0%) vs 6 (2.9%); OR 0.38 (0.19-0.75); adjusted 0.37 (0.19-0.73); P=.004. The narrative says odds were reduced for all 15 symptoms and statistically significant for 12 of 15. | PDF p. 4; PDF p. 7 Table 2 |
| S022 / N050 | **PROMIS Fatigue mean (SD):** 53.9 (12.1) vs 54.6 (12.1); 49.3 (13.3) vs 49.8 (12.9); mean difference -0.5 (-3.5 to 2.4); adjusted -0.7 (-4.0 to 2.5); P=.64. Narrative says no significant difference. | PDF p. 4; PDF p. 7 Table 2 |
| S023 / N051 | **PedsQL pain and hurt mean (SD):** 69.8 (26.6) vs 68.8 (24.8); 76.2 (26.5) vs 76.1 (24.2); difference -0.1 (-6.1 to 6.0); adjusted 0.2 (-5.9 to 6.2); P=.95. | PDF p. 7 Table 2 |
| S024 / N052 | **PedsQL nausea:** 73.9 (23.4) vs 69.2 (20.7); 71.1 (23.1) vs 70.4 (23.3); difference 0.9 (-5.7 to 7.6); adjusted 1.3 (-4.9 to 7.6); P=.66. | PDF p. 7 Table 2 |
| S025 / N053 | **PedsQL procedural anxiety:** 66.4 (30.3) vs 62.8 (29.1); 75.8 (27.9) vs 71.1 (26.1); difference 3.5 (-4.5 to 11.4); adjusted 3.0 (-4.5 to 10.5); P=.41. | PDF p. 7 Table 2 |
| S026 / N054 | **PedsQL treatment anxiety:** 77.7 (26.3) vs 76.0 (23.4); 83.9 (22.2) vs 80.4 (23.0); difference 2.9 (-3.4 to 9.3); adjusted 2.9 (-3.4 to 9.1); P=.34. | PDF p. 7 Table 2 |
| S027 / N055 | **PedsQL worry:** 64.7 (26.6) vs 62.8 (22.8); 72.9 (24.4) vs 69.5 (24.4); difference 3.1 (-2.8 to 9.1); adjusted 3.6 (-2.4 to 9.6); P=.22. | PDF p. 7 Table 2 |
| S028 / N056 | **PedsQL cognitive problems:** 70.3 (21.2) vs 69.1 (20.6); 75.3 (21.5) vs 74.5 (21.4); difference 0.9 (-5.4 to 7.2); adjusted 1.2 (-5.5 to 7.9); P=.71. | PDF p. 7 Table 2 |
| S029 / N057 | **PedsQL perceived physical appearance:** 74.7 (25.0) vs 73.2 (26.4); 77.6 (23.8) vs 77.3 (24.6); difference 0.2 (-5.1 to 5.4); adjusted 0.6 (-5.0 to 6.1); P=.83. | PDF p. 7 Table 2 |
| S030 / N058 | **PedsQL communication:** 77.8 (21.3) vs 73.2 (21.7); 79.6 (21.2) vs 77.8 (21.2); difference 1.8 (-2.6 to 6.3); adjusted 1.8 (-3.1 to 6.6); P=.45. Narrative says all adjusted PedsQL mean differences were >0 and none statistically significant. | PDF p. 4; PDF p. 7 Table 2 |
| S031 / N059 | Sensitivity/ad hoc reported results: baseline total SSPedi adjusted mean difference -1.8 (95% CI -3.5 to -0.1), P=.04; baseline-adjusted sensitivity analyses did not alter the primary finding; fully adjusted baseline-to-week-8 difference mean difference -3.0 (95% CI -5.2 to -0.8). | PDF p. 4 |

## Figure 2

| ID | Direct-source evidence and relationship | Exact location |
|---|---|---|
| N060 | Figure 2 is a visual stacked-percent display for the 15 SSPedi symptoms at baseline and week 8, separately for usual care and symptom screening. It uses score categories 0, 1, 2, 3, and 4 and a 0%-100% participant axis. The caption gives week-8 n=198 symptom screening and n=209 usual care. Exact segment percentages are not printed, so no unsupported visual measurement was transcribed. | PDF p. 8 Figure 2 |

## Documentation and intervention narrative occurrences

| ID | Direct-source evidence and relationship | Exact location |
|---|---|---|
| S032 / N061 | Symptom documentation: fatigue 43/220 (19.5%) vs 61/224 (27.2%), P=.04; changes in hunger 22/220 (10.0%) vs 37/224 (16.5%), P=.03. Narrative says documentation was more common in usual care for both. | PDF pp. 4-5 narrative |
| S033 / N062 | Any intervention: sadness 52/220 (23.6%) vs 82/224 (36.6%), P=.05; anxiety 54/220 (24.5%) vs 96/224 (42.9%), P=.01. Narrative says intervention was more common in usual care for both. | PDF p. 5 narrative |
| N063 | Symptom-specific intervention among all participants: pain 40 patients (18.2%) in screening vs 9 (4.0%) usual care; peripheral neuropathy 8 (3.6%) screening; changes in hunger 10 (4.5%) screening; constipation 15 (6.8%) screening vs 5 (2.2%) usual care. | PDF pp. 5-6 narrative |
| N064 | Among participants with any symptom, symptom-specific intervention: pain 25/73 (34.2%) vs 5/95 (5.3%); peripheral neuropathy 6/57 (10.5%) vs 0/70; changes in hunger 6/111 (5.4%) vs 0/130. | PDF p. 5 narrative |
| N065 | Among participants with severely bothersome symptoms, symptom-specific intervention: feeling sad 4/5 (80.0%) vs 2/11 (18.2%); nausea/vomiting 7/19 (36.8%) vs 2/27 (7.4%). | PDF pp. 5-6 narrative |
| N066 | Narrative states symptom-specific intervention was significantly more common with symptom screening for pain, peripheral neuropathy, and changes in hunger among all participants; for constipation among all participants; and for sadness, pain, and nausea/vomiting among those with SSPedi score >=3. No corresponding exact effect estimates/P values are printed in DOC-001. | PDF p. 6 narrative |

## Unplanned health care encounters — Table 3

Table 3 uses symptom screening n=220 and usual care n=224. It gives means (SD), crude rates per 100 patient-weeks, distributions of encounter numbers, an absolute rate difference per 100 patient-weeks with 95% credible interval, and adjusted Poisson rate ratios with 95% CI and P value. The footnote says the absolute rate difference came from marginalizing over a mixed-effects Poisson model containing treatment and random site effect only.

| ID | Encounter outcome: screening vs usual care; absolute rate difference (95% CrI); adjusted rate ratio (95% CI); P | Exact location |
|---|---|---|
| S034 / N067 | **Total ED visits + unplanned clinic visits + admissions:** mean (SD) 1.82 (2.34) vs 1.12 (1.62); 22.8 vs 14.0 per 100 patient-weeks; difference 6.13 (-1.56 to 14.51); rate ratio 1.46 (0.97-2.19); P=.07. Distribution 0:95 (43.2%) vs117 (52.2%); 1:22 (10.0%) vs40 (17.9%); 2:42 (19.1%) vs34 (15.2%); 3:22 (10.0%) vs11 (4.9%); 4:17 (7.7%) vs11 (4.9%); 5:5 (2.3%) vs6 (2.7%); >=6:17 (7.7%) vs5 (2.2%). | PDF p. 9 Table 3 |
| S035 / N068 | **Emergency-department visits:** mean (SD) 0.77 (1.12) vs 0.45 (0.81); 9.6 vs 5.6 per 100 patient-weeks; difference 3.38 (-0.57 to 7.94); rate ratio 1.72 (1.03-2.87); P=.04. Distribution 0:126 (57.3%) vs155 (69.2%); 1:49 (22.3%) vs48 (21.4%); 2:25 (11.4%) vs14 (6.2%); 3:12 (5.5%) vs5 (2.2%); 4:7 (3.2%) vs1 (0.4%); 5:0 vs1 (0.4%); >=6:1 (0.5%) vs0. Matching abstract/narrative claims report means 0.77 (1.12) vs 0.45 (0.81) and rate ratio 1.72 (95% CI 1.03-2.87). | PDF p. 1; PDF p. 6; PDF p. 9 Table 3 |
| S036 / N069 | **Unplanned clinic visits:** mean (SD) 0.40 (1.09) vs 0.24 (0.58); 5.1 vs 3.0 per 100 patient-weeks; difference -0.01 (-3.23 to 3.04); rate ratio 1.01 (0.41-2.50); P=.99. Distribution 0:174 (79.1%) vs182 (81.2%); 1:27 (12.3%) vs34 (15.2%); 2:11 (5.0%) vs5 (2.2%); >=3:8 (3.6%) vs3 (1.3%). | PDF p. 9 Table 3 |
| S037 / N070 | **Unplanned hospital admissions:** mean (SD) 0.65 (0.93) vs 0.43 (0.81); 8.1 vs 5.4 per 100 patient-weeks; difference 2.28 (-0.59 to 5.16); rate ratio 1.40 (0.96-2.03); P=.08. Distribution 0:130 (59.1%) vs161 (71.9%); 1:51 (23.2%) vs40 (17.9%); 2:28 (12.7%) vs13 (5.8%); 3:8 (3.6%) vs9 (4.0%); 4:3 (1.4%) vs1 (0.4%). | PDF p. 9 Table 3 |

## Matching narrative/abstract claims retained for cross-source checking

| ID | Claim and linked quantified relationship | Exact location |
|---|---|---|
| N071 | Abstract states 445 enrolled, median age 14.8 (8.1-18.9), 58.9% male; 8-week SSPedi 7.9 (7.2) vs 11.4 (8.7); adjusted mean difference -3.8 (95% CI -6.4 to -1.2); 12/15 symptoms statistically significantly reduced; no fatigue/quality-of-life difference; ED means and rate ratio as N068/S035. | PDF p. 1 |
| N072 | Key Points state 8-week total SSPedi range 0-60, 7.9 vs 11.4, adjusted mean difference -3.8. | PDF p. 2 |
| N073 | Results narrative repeats the primary adjusted estimate/P and says 12/15 symptom effects significant, PROMIS fatigue not significantly different, all PedsQL adjusted mean differences >0 but none significant. | PDF p. 4 |
| N074 | Discussion/conclusion state symptom screening reduced overall symptom scores, did not improve PROMIS Fatigue/PedsQL domains, and increased symptom-specific intervention; limitations say a 3.8-point total-SSPedi reduction was demonstrated. | PDF pp. 6, 9-10 |

## Inventory totals and limitations

- **Numeric/reporting relationships:** 75 grouped relationships (N001-N075; N075 is assigned after the initial map sequence to preserve the completed IDs). Each table row with many cells retains every printed value, numerator, denominator, percentage, dispersion value, interval, and label in its evidence text.
- **Inferential/statistical relationships:** S001-S037 (37 relationships), covering each printed model label, effect estimate, interval, P value, population/time/contrast, and the analysis/footnote rules needed to interpret it.
- **Direct-source page coverage:** 11/11 complete. Page 11 is explicitly no-applicable for result-relevant quantitative evidence.
- **Limitations/gaps:** no scientific-coverage gap in assigned DOC-001. Figure 2 prints a categorical stacked-percent graphic but no exact segment values, so the map preserves the plotted scale, groups, categories, and caption denominators without inventing measurements. Detailed documentation/intervention tables are cited as Supplement 2 and are outside this assigned DOC-001-only scope.
