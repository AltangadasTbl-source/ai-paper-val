# DOC-003 Support Evidence Extraction: PDF pages 1-24

## Scope and evidence method

- **Direct source:** `joi200066supp2_prod.pdf` (DOC-003), PDF pages 1-24 of 48.
- **Scope status:** COMPLETE for this assigned disjoint unit. All 24 pages were mapped.
- **Authority:** Direct PDF pages were rendered and visually inspected. Fresh `pdftotext -layout` output was used only to locate and transcribe table cells; the rendered PDF was the authority where layout mattered. No OCR was needed because the native PDF text and visual tables were legible.
- **Main-paper matching convention:** Keys below identify the corresponding main-result concept for later exact cross-source matching; this shard does not assign main-paper locations or adjudicate agreement.

## Page-by-page coverage map

| PDF page | Content | Result relevance and extraction status |
|---:|---|---|
| 1 | Supplement contents, eTables 1-7b and subgroup/sensitivity narrative listed | Administrative contents only; no result values. NOT APPLICABLE for quantitative extraction. |
| 2 | Supplement contents, eTables 8-15, eFigure, eMethods, eReferences listed | Administrative contents only; no result values. NOT APPLICABLE for quantitative extraction. |
| 3 | eTable 1, beginning | Baseline randomized-group counts, means, SDs, age/sex/race distributions; mapped in N300. |
| 4 | eTable 1, continuation | Baseline race, education, income, BMI, Charlson score, hypertension and cholesterol medication; mapped in N300. |
| 5 | eTable 1, continuation | Diabetes, smoking, alcohol, activity, hormone/multivitamin/vitamin-D use; mapped in N300. |
| 6 | eTable 1, continuation | Calcium, dietary intake, biomarkers, and location; mapped in N300. |
| 7 | eTable 1 end and footnotes a-e | Midwest/location and omega-3 randomization; units and missingness/definition footnotes; mapped in N300. |
| 8 | eTable 1 footnotes f-l | Intake definitions and 25(OH)D conversion; mapped in N300. |
| 9 | eTable 2, beginning | PHQ-8 change subgroup estimates, participant counts, 95% CIs, and interaction P values; mapped in N301/S300. |
| 10 | eTable 2, continuation | Additional subgroups, estimates, CIs, interaction P values; mapped in N301/S300. |
| 11 | eTable 2 end | Activity, region, and omega-3 subgroups; mapped in N301/S300. |
| 12 | eTable 2 analytic footnotes | Response-profile model, covariates, averaging period, interaction definition, post-hoc BMI designation; mapped in S300. |
| 13 | Subgroup-results narrative | Depression-risk subgroup narrative and PHQ-8 subgroup interpretation; mapped in S301 and N301. |
| 14 | eTable 3 and beginning footnote | Censored-after-antidepressant PHQ-8 longitudinal sensitivity; mapped in N302/S302. |
| 15 | eTable 3 footnote continuation | Model and contrast definitions; mapped in S302. |
| 16 | eTable 4 | Questionnaire respondent adherence numerators/denominators and percentages by year; mapped in N303. |
| 17 | eTable 5 | Pill-adherence/outside-vitamin-D censoring Cox sensitivity; events, HRs, CIs, P values; mapped in N304/S303. |
| 18 | eTable 5 endpoint footnotes | Composite primary outcome and incident/recurrent secondary outcome definitions; mapped in S303. |
| 19 | eTable 6a | Incident-CVD-censoring Cox sensitivity; events, HRs, CIs, P values; mapped in N305/S304. |
| 20 | eTable 6a endpoint footnotes and eTable 6b beginning | CVD time-dependent-covariate sensitivity begins; mapped in N306/S305. |
| 21 | eTable 6b end and footnotes | CVD covariate model and endpoint definitions; mapped in S305. |
| 22 | eTable 7a | Incident-cancer-censoring Cox sensitivity; events, HRs, CIs, P values; mapped in N307/S306. |
| 23 | eTable 7a footnote and eTable 7b | Total-cancer time-dependent-covariate sensitivity; mapped in N308/S307. |
| 24 | eTable 7b footnotes | Cancer covariate model and endpoint definitions; mapped in S307. |

## Extracted result-relevant evidence

### eTable 1: randomized baseline characteristics (PDF pages 3-8)

The randomized denominators are vitamin D3 **N=9181** and placebo **N=9172**. Key reported values are: age mean (SD), 67.5 (7.0) and 67.4 (7.1); men 4641 (50.6%) and 4689 (51.1%); women 4540 (49.5%) and 4483 (48.9%). Age categories 50-54, 55-64, 65-74, and >=75 total 9181 and 9172 within their respective groups. Race/ethnicity denominators are 8999 and 8990; category counts total those denominators. Charlson categories 0, 1, and >=2 points total 9181 and 9172. Smoking categories total 9134 and 9133; alcohol categories total 9050 and 9042.

Other explicit denominator/proportion data include education 8078/9162 (88.2%) versus 8087/9153 (88.4%); income >=$30,000, 6900/8257 (83.6%) versus 6885/8223 (83.7%); hypertension, 4570/9129 (50.1%) versus 4628/9133 (50.7%); cholesterol medication, 3366/9143 (36.8%) versus 3258/9130 (35.7%); diabetes, 1186/9164 (12.9%) versus 1122/9161 (12.3%); women-only current hormone use, 462/4462 (10.4%) versus 477/4408 (10.8%); multivitamin use, 4107/9046 (45.4%) versus 4066/9038 (45.0%); supplemental vitamin D use, 4076/9181 (44.4%) versus 4054/9172 (44.2%); and calcium use, 1908/9181 (20.8%) versus 1845/9172 (20.1%).

For complete cell-level transcription, vitamin D3/placebo values are: age 50-54, 319 (3.5%)/333 (3.6%); 55-64, 2967 (32.3%)/2998 (32.7%); 65-74, 4630 (50.4%)/4601 (50.2%); >=75, 1265 (13.8%)/1240 (13.5%). Race: non-Hispanic White 6552 (72.8%)/6545 (72.8%); Black 1705 (19.0%)/1702 (18.9%); Hispanic (not African American) 362 (4.0%)/346 (3.9%); Asian/Pacific Islander 144 (1.6%)/150 (1.7%); American Indian/Alaskan Native 78 (0.9%)/72 (0.8%); other/unknown 158 (1.8%)/175 (2.0%). Charlson 0 point 7744 (84.4%)/7796 (85.0%); 1 point 1234 (13.4%)/1171 (12.8%); >=2 points 203 (2.2%)/205 (2.2%). Smoking never/past/current: 4836 (53.0%)/4902 (53.7%), 3727 (40.8%)/3681 (40.3%), and 571 (6.3%)/550 (6.0%). Alcohol never/rarely, monthly, weekly, daily: 2700 (29.8%)/2774 (30.7%), 663 (7.3%)/656 (7.3%), 3309 (36.6%)/3151 (34.9%), and 2378 (26.3%)/2461 (27.2%).

Dietary intake mean (SD), vitamin D3/placebo: milk servings/day 0.7 (0.9)/0.7 (0.9), n=17927; other vitamin-D-fortified-food servings/day 0.6 (0.8)/0.6 (0.7), n=18077; dark-meat-fish servings/week 1.0 (1.4)/1.0 (1.7), n=18053; other fish/seafood servings/week 1.1 (1.8)/1.1 (1.7), n=18064. Biomarkers: 25(OH)D 31.2 (9.8)/31.1 (10.0), n=11417; EPA 0.6 (0.4)/0.6 (0.4), n=11229; DHA 2.0 (0.7)/2.0 (0.7), n=11237. Location southeast/northeast/west/midwest: 2484 (27.1%)/2547 (27.8%), 2528 (27.5%)/2475 (27.0%), 2139 (23.3%)/2149 (23.4%), and 2030 (22.1%)/2000 (21.8%). Omega-3 randomization active/placebo: 4608 (50.2%)/4563 (49.8%) and 4573 (49.8%)/4609 (50.3%).

Units/definitions: BMI is kg/m2 and is weight in kilograms divided by height in meters squared; BMI data were missing for 2.4% of participants. Physical activity is MET-hours/week, reported as median (IQR): 16.8 (5.5-32.7) and 17.0 (5.6-33.5). Biomarkers are ng/ml; 25(OH)D is 31.2 (9.8) and 31.1 (10.0), with conversion to nmol/l by multiplying by 2.5. The table says percentages may not total 100 because of rounding and that there were no significant baseline-group differences.

**Main-paper matching key:** randomized baseline cohort: vitamin D3 N=9181, placebo N=9172; baseline covariate table.

### eTable 2 and subgroup narrative: PHQ-8 change (PDF pages 9-13)

eTable 2 reports adjusted mean differences in PHQ-8 change, vitamin D3 versus placebo, averaged over years 1-5, with 95% CIs and interaction P values. The subgroup values are fully inventoried in S300. Participant totals vary by available subgroup information; examples include women 9023, men 9330; age 50-64 6617, 65-74 9231, >=75 2505; and randomized omega-3 active 9171, placebo 9182.

The PDF explicitly defines the analyses as general linear response-profile models with time as indicator variables and control for age, sex, and n-3 fatty-acid randomization group. A P-interaction is the subgroup x treatment x follow-up-time interaction. BMI categories were a non-prespecified/post-hoc subgroup analysis. The narrative says no interaction was statistically significant and PHQ-8 subgroup effects did not vary; interaction tests were not adjusted for multiple comparisons. It separately reports depression-risk subgroup narrative values: women P-interaction=0.10; normal versus higher BMI P-interaction=0.06; among baseline vitamin-D users HR=0.87 (95% CI 0.73-1.04); among baseline 25(OH)D >=20 ng/ml HR=0.89 (95% CI 0.77-1.04).

**Main-paper matching key:** main Figure 3 depression-risk subgroup analysis (explicitly named on PDF page 13); PHQ-8 subgroup mean-change result.

### eTable 3: antidepressant-censoring PHQ-8 sensitivity (PDF pages 14-15)

Baseline adjusted means are 1.08 (1.05-1.11), n=9181, for vitamin D3 and 1.13 (1.09-1.16), n=9172, for placebo. Vitamin D3 versus placebo mean differences in change are year 1 -0.01 (-0.06, 0.04), P=.71; year 2 0.02 (-0.03, 0.08), P=.45; year 3 0.01 (-0.05, 0.07), P=.82; year 4 -0.01 (-0.07, 0.05), P=.80; year 5 0.02 (-0.05, 0.09), P=.64; and average years 1-5 0.00 (-0.04, 0.05), P=.89. The single treatment x time P-interaction is .88 (5 degrees of freedom). Follow-up row counts (vitamin D3/placebo) are 8479/8438, 8282/8260, 8032/7993, 7590/7455, and 5181/5096 for years 1 through 5.

The separately printed within-group adjusted mean changes (95% CI), vitamin D3/placebo, are: year 1 0.02 (-0.02, 0.05)/0.03 (-0.01, 0.06); year 2 0.06 (0.02, 0.10)/0.04 (-0.00, 0.08); year 3 0.07 (0.03, 0.11)/0.07 (0.02, 0.11); year 4 0.04 (0.00, 0.08)/0.05 (0.01, 0.09); and year 5 0.17 (0.12, 0.22)/0.15 (0.10, 0.20).

The response-profile model controls for age, sex, and fish-oil randomization group. It censors PHQ-8 scores after initiation of antidepressants. Within-group adjusted mean changes and between-group adjusted differences are separately labelled; the last row is the years-1-5 average versus baseline.

**Main-paper matching key:** PHQ-8 longitudinal mean-change sensitivity, antidepressant-censoring variant.

### eTable 4: participant-reported pill adherence (PDF page 16)

The table is restricted to participants responding to compliance questionnaires and labels values as percent of pills taken. Vitamin D3 and placebo values are respectively: baseline 9181/9181 (100.0%) and 9172/9172 (100.0%); year 1 8237/8688 (94.8%) and 8128/8590 (94.6%); year 2 7793/8448 (92.2%) and 7681/8341 (92.1%); year 3 7485/8180 (91.5%) and 7367/8097 (91.0%); year 4 7103/7771 (91.4%) and 6920/7644 (90.5%); year 5 4665/5148 (90.6%) and 4524/5036 (89.8%).

**Main-paper matching key:** adherence/compliance denominators and percent-of-pills-taken result.

### eTables 5-7b: Cox-model sensitivity results and endpoint definitions (PDF pages 17-24)

Every table labels group Ns (vitamin D3 n=9181; placebo n=9172) and the group entries as numbers of participants with the event. The primary endpoint is a composite of reported clinician diagnosis of depression, treatment for depression, and/or PHQ-8 >=10; total depression is all incident plus recurrent depression. Incident depression is among people with no past history; recurrent depression is among those with past history who were not under treatment or active in the past 2 years. Each table reports HR (95% CI) and P value, and says analyses were not adjusted for multiple comparisons.

- **eTable 5:** additional censoring at less than two-thirds study-pill use or >800 IU/d outside vitamin D. Total: 468/486, HR 0.94 (0.83-1.07), P=.35; incident: 350/362, 0.94 (0.81-1.09), .40; recurrent: 118/124, 0.99 (0.77-1.28), .97. Cox model controls age, sex, and marine-3 fatty-acid randomization group.
- **eTable 6a:** additional censoring at incident CVD. Total 598/606, 0.99 (0.88-1.10), .80; incident 453/446, 1.01 (0.89-1.15), .87; recurrent 145/160, 0.95 (0.76-1.19), .64. Controls age, sex, and marine-3 fatty-acid randomization group.
- **eTable 6b:** additional adjustment for CVD as a time-dependent covariate. Total 609/625, 0.97 (0.87-1.09), .60; incident 459/461, 0.99 (0.87-1.13), .87; recurrent 150/164, 0.95 (0.76-1.18), .63. Controls age, sex, time-dependent CVD, and marine-3 fatty-acid randomization group.
- **eTable 7a:** additional censoring at incident cancer. Total 590/602, 0.98 (0.87-1.10), .70; incident 445/441, 1.00 (0.88-1.14), .96; recurrent 145/161, 0.94 (0.75-1.18), .61. Controls age, sex, and marine-3 fatty-acid randomization group.
- **eTable 7b:** additional adjustment for total cancer as a time-dependent covariate. Total 609/625, 0.97 (0.87-1.09), .62; incident 459/461, 0.99 (0.87-1.13), .88; recurrent 150/164, 0.95 (0.76-1.19), .67. Controls age, sex, time-dependent malignant cancer, and marine-3 fatty-acid randomization group.

**Main-paper matching key:** primary total-depression HR and secondary incident/recurrent-depression HR results; sensitivity variants defined by censoring/adjustment rather than the primary analysis.

## Candidate-routing note

No source-grounded candidate is asserted or assigned in this mapper artifact. Table totals that can be checked from the displayed entries reconcile (for example, total events equal incident plus recurrent events in every eTable 5-7b row). Any cross-document comparison or statistical compatibility assessment requires matching population, censoring, model, and test details from the main-paper mapping and later statistical passes.
