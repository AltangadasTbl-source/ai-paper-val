# Main quantitative evidence mapping — DOC-001

## Scope and evidence basis

- **Assigned source:** `DOC-001`, `jama_saynorea_2019_oi_190106_1635377898.43062.pdf`.
- **Assigned units:** PDF pages 1-14, all mapped. Pages 1-10 contain result-relevant displays or matching narrative; pages 11-14 contain discussion, conclusions, article information, and references, with the page-12 correction notice recorded below.
- **Reusable locator:** `.ai_paper_validation/document_outputs/DOC-001/main_layout.txt` (14 PDF pages).
- **Direct-source confirmation:** `pdftotext -layout -f 1 -l 14` on the assigned PDF produced text byte-identical to the reusable layout extraction. PDF SHA-256: `9da22a99ae26fb643cd89b38f256e3c9363a5d94df39a32513cfa1ff0928612b`.
- **Extraction convention:** `MAIN-Nxxx` denotes a numeric/reporting relationship and `MAIN-Sxxx` an inferential-statistical relationship. A single table row can have both keys. Values are transcribed as printed; a minus sign is the printed direction. All group contrasts are intervention minus control unless the row states otherwise.
- **Direct evidence links:** every cited page is this source PDF, `jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=N`.

## Page coverage and result-relevant mapping

| PDF page | Coverage | Result-relevant content / no-applicable-unit record |
|---:|---|---|
| 1 | COMPLETE | Abstract: population, allocation, follow-up, primary score result, and matching conclusion. |
| 2 | COMPLETE | Key Points (matching primary result), design and eligibility definitions, intervention quantities. |
| 3 | COMPLETE | Figure 1 participant flow; outcome measurement time points and score definitions. |
| 4 | COMPLETE | Table 1 baseline data; analysis populations, exclusions, imputation, models, and results narrative. |
| 5 | COMPLETE | Table 2 dietary-score results and footnotes; primary-outcome narrative. |
| 6 | COMPLETE | Figure 2 (distribution display) and narrative dietary/food-group results. |
| 7 | COMPLETE | Table 3, first portion. |
| 8 | COMPLETE | Table 3 continuation; narrative food, energy/nutrient, risk-factor results. |
| 9 | COMPLETE | Figure 3 descriptive distribution display; no printed individual plotted coordinates. |
| 10 | COMPLETE | Figure 4 clinically meaningful-change proportions, CIs, and P values. |
| 11 | COMPLETE | Discussion/limitations/conclusion only; repeated qualitative claims, no new result numbers. |
| 12 | COMPLETE | Article information; correction states an eTable 1 outcome was measured at 1- and 3-year follow-up, not a result estimate. |
| 13 | COMPLETE | Article information/references; no applicable result relationships. |
| 14 | COMPLETE | References; no applicable result relationships. |

## Population, design, and matching anchors

| Key | Relationship and printed values | Population/time/contrast/model or label | Exact source location and matching occurrence |
|---|---|---|---|
| MAIN-N001 | Enrolled/randomized: 6874; intervention 3406; control 3468. | Spain, 23 centers; men/women aged 55-75; randomized 1:1. | PDF p.1 Abstract; p.2 Methods; p.3 Figure 1; p.4 Results. |
| MAIN-N002 | Randomized participants: mean (SD) age 65.0 (4.9) y; 3406 (52%) men. | All randomized. | PDF p.1 Abstract. |
| MAIN-N003 | 6583 (96%) completed 12-month follow-up/included main analysis. | Main analysis. | PDF p.1 Abstract; p.4 Results. |
| MAIN-N004 | Main-analysis groups: intervention 3272; control 3311; total 6583; men 3406 and women 3177. | Excluded from randomized cohort if no baseline food-frequency questionnaire or energy outside limits. | PDF p.3 Figure 1; p.4 Results. |
| MAIN-N005 | Exclusions: intervention 134 = 106 energy-limit + 28 missing baseline food-frequency questionnaire; control 157 = 132 + 25; total 291 = 238 + 53. | Figure 1 and Results. Energy limits: women 500-3500 kcal/d, men 800-4000 kcal/d. | PDF p.3 Figure 1; p.4 Statistical Analysis and Results. |
| MAIN-N006 | Individually randomized: 2892 intervention, 2909 control; randomized by couples: 380 intervention, 402 control. | Main-analysis participants. | PDF p.3 Figure 1. |
| MAIN-N007 | Nutritional information unavailable: 6 months 410 intervention/428 control; 12 months 439/368. Completer sensitivity samples: 6 months 2862/2883; 12 months 2833/2943. | Post hoc completer-only sensitivity analyses. | PDF p.3 Figure 1. |
| MAIN-N008 | Primary endpoint: baseline-to-12-month er-MedDiet change, range 0-17, higher is greater adherence, minimal clinically important difference 1 point. Secondary ranges: MEDAS 0-14; MDS 0-9; PDQS 0-42, higher is better dietary quality. | Measurement labels/scales. | PDF p.1 Abstract; p.3 Outcomes; p.4 Outcomes; p.5 Table 2 footnotes. |
| MAIN-N009 | Intervention recommended approximately 30% of estimated energy requirements, approximately 600 kcal/d; olive oil 1 L/mo and nuts 125 g/mo free; total mixed nuts 500 g/mo recommended. | Intervention versus energy-unrestricted control. | PDF p.1 Abstract; p.2 Methods; p.3 Methods. |
| MAIN-N010 | Imputed missing nutritional values: 12.7% at 6 months and 12.2% at 12 months. Eight imputations per missing measurement. | Principal analysis; follow-up, not baseline, values imputed. | PDF p.4 Results and Statistical Analysis. |
| MAIN-S001 | Mixed-effects linear models; 3-level random intercepts: site, participant, cluster family; Table 2/3 contrasts calculated with site and intracluster-correlation (couples) random factors. Two-sided tests; P < .05 significant; secondary analyses exploratory/no type-I adjustment. | Model and inferential convention required to interpret all Table 2/3 contrasts. | PDF p.4 Statistical Analysis; p.5 Table 2 footnote b; pp.7-8 Table 3 footnote b. |

## Baseline characteristics — Table 1

All Table 1 records are `MAIN-N011`-`MAIN-N020`; intervention/control denominators are 3272/3311 except education, 3240/3285. Location: PDF p.4, Table 1.

| Key | Characteristic, intervention | Control | Population/unit/label |
|---|---|---|---|
| MAIN-N011 | Men 1702 (52%); women 1570 (48%). | Men 1704 (51%); women 1607 (49%). | Count (%), main analysis. |
| MAIN-N012 | Age, mean (SD), 65.0 (4.9) y. | 65.0 (4.9) y. | Main analysis. |
| MAIN-N013 | Current smoker 436 (13%); former smoker 1366 (42%). | 379 (11%); 1486 (45%). | Count (%), main analysis. |
| MAIN-N014 | Education: primary or less 1540 (48%); secondary 997 (31%); university 703 (21%). | 1647 (50%); 902 (28%); 736 (22%). | Count (%); education denominators 3240/3285. |
| MAIN-N015 | Weight, mean (SD), 86.7 (13.0) kg. | 86.4 (13.0) kg. | Main analysis. |
| MAIN-N016 | BMI, mean (SD), 32.5 (3.4). | 32.5 (3.5). | kg/m²; BMI calculated as kg/m². |
| MAIN-N017 | Waist circumference, mean (SD), 108 (9.6) cm. | 108 (9.7) cm. | Main analysis. |
| MAIN-N018 | Physical activity, median (IQR), 1709 (839-3202) MET min/wk. | 1902 (867-3371). | Main analysis. |
| MAIN-N019 | Baseline group sizes and baseline characteristics described as similar. | Narrative matching Table 1. | PDF p.4 Results. |
| MAIN-N020 | Clinically meaningful thresholds: ≥5% reduction for BMI, weight, waist, total/LDL/non-HDL cholesterol and cholesterol:HDL ratio; ≥5 mm Hg systolic or ≥2.5 mm Hg diastolic BP reduction; ≥5% HDL increase; 10% triglyceride reduction. | Defines Figure 4 percentage labels. | PDF p.4 Outcomes; p.10 Figure 4. |

## Dietary pattern scores — Table 2 and matching narrative

Table 2 population: multiple-imputation all randomized included participants, intervention n=3272 and control n=3311. Baseline entries are `MAIN-N021`-`MAIN-N024`; follow-up score/change records include an inferential key because each has a modelled between-group difference and P value. Exact table/footnote location: PDF p.5 Table 2.

| Numeric key / statistical key | Score, time | Intervention mean (SD) | Control mean (SD) | Between-group difference (95% CI); P | Narrative/match target |
|---|---|---:|---:|---|---|
| MAIN-N021 | er-MedDiet baseline | 8.5 (2.6) | 8.6 (2.7) | — | PDF p.1 Abstract; p.5 Primary Outcome. |
| MAIN-N025 / MAIN-S002 | er-MedDiet 6 mo score; change | 12.9 (2.8); 4.4 (3.4) | 10.8 (2.8); 2.2 (3.5) | 2.2 (2.0 to 2.3); <.001 | Table only. |
| MAIN-N026 / MAIN-S003 | er-MedDiet 12 mo score; change | 13.2 (2.7); 4.7 (3.5) | 11.1 (2.8); 2.5 (3.4) | 2.2 (2.1 to 2.4); <.001 | PDF p.1 Abstract; p.2 Key Points; p.5 narrative; p.6 continuation. |
| MAIN-N022 | MDS baseline | 4.3 (1.7) | 4.3 (1.6) | — | Table only. |
| MAIN-N027 / MAIN-S004 | MDS 6 mo score; change | 5.0 (1.6); 0.7 (2.4) | 4.6 (1.6); 0.3 (2.5) | 0.4 (0.3 to 0.5); <.001 | Table only. |
| MAIN-N028 / MAIN-S005 | MDS 12 mo score; change | 5.1 (1.6); 0.8 (2.5) | 4.5 (1.6); 0.2 (2.4) | 0.6 (0.5 to 0.7); <.001 | Table only. |
| MAIN-N023 | MEDAS baseline | 7.6 (1.9) | 7.6 (1.9) | — | Table only. |
| MAIN-N029 / MAIN-S006 | MEDAS 6 mo score; change | 10.6 (1.8); 3.0 (2.4) | 9.6 (1.9); 2.0 (2.5) | 1.0 (0.9 to 1.1); <.001 | Table only. |
| MAIN-N030 / MAIN-S007 | MEDAS 12 mo score; change | 10.8 (1.7); 3.2 (2.4) | 9.7 (1.9); 2.1 (2.5) | 1.1 (1.0 to 1.2); <.001 | Table only. |
| MAIN-N024 | PDQS baseline | 21.1 (3.7) | 21.1 (3.7) | — | PDF p.6 Secondary Outcomes. |
| MAIN-N031 / MAIN-S008 | PDQS 6 mo score; change | 27.8 (3.6); 6.7 (6.8) | 25.8 (3.7); 4.7 (7.4) | 2.0 (1.6 to 2.3); <.001 | Table only. |
| MAIN-N032 / MAIN-S009 | PDQS 12 mo score; change | 28.0 (3.5); 6.9 (7.0) | 25.5 (3.6); 4.4 (7.0) | 2.4 (2.1 to 2.8); <.001 | PDF p.6 narrative. |

Additional Table 2 quantities: er-MedDiet imputed values 463 at 6 months and 517 at 12 months; MDS, MEDAS, and PDQS each 838 at 6 months and 807 at 12 months (`MAIN-N033`, PDF p.5 Table 2 footnote a). Footnotes define a 1-point er-MedDiet minimally clinically important difference; MDS 1 point; MEDAS 1 point; PDQS likely 2-point increment (`MAIN-N034`, PDF p.5). Contextual reported association in the MDS footnote: 2-point MDS increase, approximately 1 SD, associated with 25% relative all-cause-mortality reduction, coefficient log(0.75)=−0.2877; 1 MDS point (0.5 SD) corresponds to 13% relative reduction and HR exp(−0.2877/2)=0.87. MEDAS footnote reports 1-point increment associated with 10% composite cardiovascular-endpoint risk reduction, HR 0.90 (95% CI 0.85-0.96), and 6% total-mortality reduction, HR 0.94 (0.89-0.99) (`MAIN-S010`, PDF p.5; contextual external/unpublished associations, not trial contrasts).

`MAIN-S011` (PDF p.6): the intervention er-MedDiet improvement is reported as a 55% relative increase (95% CI 55%-56%; P<.001), matching Table 2’s 4.7-point intervention change. Figure 2 displays score distributions at baseline and 12 months in each group, range 0-17, median/IQR/1.5×IQR boxplot convention, but provides no printed bin counts or plotted coordinate labels (`MAIN-N035`, PDF p.6 Figure 2).

## Food-group narrative results

| Numeric key / statistical key | Printed result, population/time/unit | Exact location |
|---|---|---|
| MAIN-N036 / MAIN-S012 | Refined grains baseline 779 g/wk in both groups; 12-month change intervention −535 g/wk (95% CI −559 to −510), control −226 (−249 to −203); between-group −309 (−340 to −277), P<.001. | PDF p.6 narrative. |
| MAIN-N037 / MAIN-S013 | Pastries baseline control 114 g/wk, intervention 121; 12-month within-group control −60 (−67 to −53), intervention −109 (−116 to −102); between-group −49 (−59 to −39), P<.001. | PDF p.6 narrative. |
| MAIN-N038 / MAIN-S014 | Red-meat 12-month between-group difference −39 g/wk (−51 to −28), P<.001. | PDF p.6 narrative. |
| MAIN-N039 / MAIN-S015 | Vegetables baseline control 2130 g/wk, intervention 2168; 12-month within-group changes control 137 (100-175), intervention 347 (306-389); between-group 210 (157-263), P<.001. | PDF pp.6-8 narrative continuation. |
| MAIN-N040 / MAIN-S016 | Fruits 12-month between-group difference 197 g/wk (118-276), P<.001. Nuts baseline 60 g/wk both groups; 12-month between-group 35 g/wk (27-43), P<.001. | PDF p.8 narrative. |

## Energy and nutrient outcomes — Table 3

Table 3 population/model: multiple-imputation all randomized participants, intervention n=3272/control n=3311; 838 values imputed at 6 months and 807 at 12 months. Values are intervention/control mean (SD), except explicitly median (IQR); contrast is intervention minus control. Location: PDF pp.7-8, Table 3.

| Numeric key / statistical key | Variable and time | Intervention | Control | Difference (95% CI); P |
|---|---|---:|---:|---|
| MAIN-N041 | Total energy baseline, kcal/d | 2355 (555) | 2369 (555) | — |
| MAIN-N042 / MAIN-S017 | Total energy 6-mo change | −173 (537) | −76 (501) | −97 (−122 to −72); <.001 |
| MAIN-N043 / MAIN-S018 | Total energy 12-mo change | −176 (543) | −74 (501) | −102 (−129 to −75); <.001 |
| MAIN-N044 | Total protein baseline, %/d | 16.8 (2.8) | 16.8 (2.8) | — |
| MAIN-N045 / MAIN-S019 | Total protein 6-mo change | 1.2 (2.9) | 0.2 (2.7) | 1.0 (0.9 to 1.2); <.001 |
| MAIN-N046 / MAIN-S020 | Total protein 12-mo change | 1.1 (3.0) | 0 (2.7) | 1.1 (1.0 to 1.3); <.001 |
| MAIN-N047 | Total carbohydrate baseline, %/d | 40.7 (6.8) | 40.4 (6.9) | — |
| MAIN-N048 / MAIN-S021 | Total carbohydrate 6-mo change | −3.4 (7.0) | −1.9 (6.8) | −1.5 (−1.8 to −1.1); <.001 |
| MAIN-N049 / MAIN-S022 | Total carbohydrate 12-mo change | −3.7 (6.9) | −2.3 (6.8) | −1.4 (−1.8 to −1.0); <.001 |
| MAIN-N050 | Total fat baseline, %/d | 39.5 (6.6) | 39.7 (6.5) | — |
| MAIN-N051 / MAIN-S023 | Total fat 6-mo change | 2.5 (7.1) | 1.9 (6.9) | 0.6 (0.3 to 1.0); <.001 |
| MAIN-N052 / MAIN-S024 | Total fat 12-mo change | 2.9 (7.1) | 2.4 (6.9) | 0.5 (0.1 to 0.9); .007 |
| MAIN-N053 | SFA baseline, %/d | 9.9 (2.0) | 10.0 (2.0) | — |
| MAIN-N054 / MAIN-S025 | SFA 6-mo change | −1.0 (2.0) | −0.6 (2.0) | −0.5 (−0.6 to −0.4); <.001 |
| MAIN-N055 / MAIN-S026 | SFA 12-mo change | −0.9 (2.0) | −0.6 (1.9) | −0.4 (−0.5 to −0.3); <.001 |
| MAIN-N056 | MUFA baseline, %/d | 20.5 (4.7) | 20.6 (4.6) | — |
| MAIN-N057 / MAIN-S027 | MUFA 6-mo change | 3.5 (5.6) | 2.4 (5.3) | 1.1 (0.9 to 1.4); <.001 |
| MAIN-N058 / MAIN-S028 | MUFA 12-mo change | 3.9 (5.6) | 3.0 (5.3) | 0.9 (0.6 to 1.2); <.001 |
| MAIN-N059 | MUFA:SFA ratio baseline | 2.1 (0.5) | 2.1 (0.5) | — |
| MAIN-N060 / MAIN-S029 | MUFA:SFA ratio 6-mo change | 0.6 (0.7) | 0.4 (0.6) | 0.3 (0.2 to 0.3); <.001 |
| MAIN-N061 / MAIN-S030 | MUFA:SFA ratio 12-mo change | 0.7 (0.7) | 0.5 (0.7) | 0.2 (0.2 to 0.2); <.001 |
| MAIN-N062 | PUFA baseline, %/d | 6.4 (1.9) | 6.4 (1.8) | — |
| MAIN-N063 / MAIN-S031 | PUFA 6-mo change | 1.3 (2.3) | 0.8 (2.1) | 0.5 (0.4 to 0.6); <.001 |
| MAIN-N064 / MAIN-S032 | PUFA 12-mo change | 1.3 (2.2) | 0.8 (2.1) | 0.4 (0.3 to 0.5); <.001 |
| MAIN-N065 | Total alcohol baseline, %/d, median (IQR) | 1.0 (0 to 4) | 2.0 (0 to 4) | — |
| MAIN-N066 / MAIN-S033 | Total alcohol 6-mo change, mean (SD) | −0.3 (3.0) | −0.1 (3.0) | −0.2 (−0.4 to 0); .01 |
| MAIN-N067 / MAIN-S034 | Total alcohol 12-mo change, mean (SD) | −0.3 (3.0) | −0.1 (3.0) | −0.2 (−0.4 to 0.1); .01 |
| MAIN-N068 | Fiber baseline, g/wk | 184 (62.7) | 182 (59.9) | — |
| MAIN-N069 / MAIN-S035 | Fiber 6-mo change | 40 (70.8) | 16 (60.6) | 23 (20 to 27); <.001 |
| MAIN-N070 / MAIN-S036 | Fiber 12-mo change | 37 (68.5) | 18 (62.8) | 19 (16 to 23); <.001 |
| MAIN-N071 | Long-chain omega-3 baseline, g/wk, median (IQR) | 5 (4 to 9) | 5 (4 to 9) | — |
| MAIN-N072 / MAIN-S037 | Long-chain omega-3 6-mo change, mean (SD) | 1.1 (3.9) | 0.5 (3.6) | 0.6 (0.4 to 0.8); <.001 |
| MAIN-N073 / MAIN-S038 | Long-chain omega-3 12-mo change, mean (SD) | 1.1 (4.1) | 0.4 (3.6) | 0.7 (0.5 to 0.9); <.001 |
| MAIN-N074 | Cholesterol baseline, mg/wk | 2651 (793) | 2687 (825) | — |
| MAIN-N075 / MAIN-S039 | Cholesterol 6-mo change | −224 (779) | −169 (780) | −54 (−94 to −14); .008 |
| MAIN-N076 / MAIN-S040 | Cholesterol 12-mo change | −216 (823) | −209 (784) | −7 (−49 to 35); .74 |
| MAIN-N077 | Sodium baseline, g/wk, median (IQR) | 22 (18 to 27) | 22 (18 to 27) | — |
| MAIN-N078 / MAIN-S041 | Sodium 6-mo change, mean (SD) | −3.0 (6.8) | −1.8 (6.5) | −1.2 (−1.6 to −0.9); <.001 |
| MAIN-N079 / MAIN-S042 | Sodium 12-mo change, mean (SD) | −3.2 (7.1) | −1.9 (6.9) | −1.3 (−1.6 to −0.9); <.001 |

`MAIN-N080`/`MAIN-S043` (PDF p.8 narrative) match Table 3: total energy baseline control 2369 (555) versus intervention 2355 (555) kcal/d and 12-month contrast −102 kcal/d (−129 to −75), P<.001; carbohydrate 12-month contrast −1.4% (−1.8% to −1.0%), P<.001; MUFA baseline control 20.6% (4.6) and intervention 20.5% (4.7), within-group 12-month changes 3.0% (2.8%-3.2%) and 3.9% (3.7%-4.1%), respectively, P<.001 each, between-group 0.9% (0.6%-1.2%), P<.001. It also states all differences in eFigure 3 are expressed in baseline-SD units (`MAIN-N081`, PDF p.8).

## Cardiovascular risk-factor figures and matching narrative

`MAIN-N082` (PDF p.9 Figure 3): displays intervention/control distributions of 6- and 12-month changes, in common baseline-SD units, for body weight, waist circumference, BMI, serum/HDL/LDL/non-HDL cholesterol, total cholesterol:HDL ratio, triglycerides, systolic BP, and diastolic BP. Caption specifies median, IQR, and whiskers to 1.5×IQR; no exact individual plotted coordinates or numeric summary labels are printed, so none are transcribed.

| Numeric key / statistical key | Figure 4, 12-month clinically meaningful change: intervention % (95% CI) | Control % (95% CI) | Threshold / P value |
|---|---:|---:|---|
| MAIN-N083 / MAIN-S044 | Body weight 40.6 (38.7-42.5) | 12.2 (11.0-13.5) | Reduction >5%; <.001 |
| MAIN-N084 / MAIN-S045 | Waist circumference 39.5 (37.6-41.3) | 13.5 (12.2-14.8) | Reduction >5%; <.001 |
| MAIN-N085 / MAIN-S046 | BMI 40.5 (38.6-42.4) | 12.5 (11.3-13.8) | Reduction >5%; <.001 |
| MAIN-N086 / MAIN-S047 | Total cholesterol 37.5 (35.7-39.4) | 34.3 (32.5-36.1) | Reduction >5%; .02 |
| MAIN-N087 / MAIN-S048 | HDL cholesterol 45.6 (43.7-47.6) | 40.0 (38.1-41.8) | Increase >5%; <.001 |
| MAIN-N088 / MAIN-S049 | LDL cholesterol 41.4 (39.5-43.3) | 40.2 (38.3-42.1) | Reduction >5%; .36 |
| MAIN-N089 / MAIN-S050 | Non-HDL cholesterol 43.6 (41.7-45.5) | 37.5 (35.7-39.4) | Reduction >5%; <.001 |
| MAIN-N090 / MAIN-S051 | Total cholesterol/HDL ratio 48.4 (46.5-50.4) | 41.3 (39.4-43.2) | Reduction >5%; <.001 |
| MAIN-N091 / MAIN-S052 | Triglycerides 47.3 (45.4-49.2) | 38.2 (36.3-40.0) | Reduction >10%; <.001 |
| MAIN-N092 / MAIN-S053 | Systolic BP 47.5 (45.6-49.5) | 41.8 (39.9-43.7) | Reduction >5 mm Hg; <.001 |
| MAIN-N093 / MAIN-S054 | Diastolic BP 48.1 (46.2-50.1) | 44.3 (42.4-46.2) | Reduction 2.5 mm Hg; .005 |

Figure 4 source location is PDF p.10. Its plotted horizontal boxplots use the same median/IQR/1.5×IQR convention, but exact plot summary values are not printed (`MAIN-N094`).

`MAIN-N095`/`MAIN-S055` (PDF p.8 narrative) state that, except LDL cholesterol, favorable intervention-versus-control changes in the Figure 3/eTable 9 risk factors were significant and clinically meaningful. Explicit narrative matches: waist baseline 108 cm in both groups and 12-month contrast −3.3 cm (−3.6 to −2.9), P<.001; systolic BP baseline 139 mm Hg control and 140 intervention and 12-month contrast −1.9 (−2.7 to −1.1), P<.001. This narrative does not print the Table/Figure 3 point-estimate values for all other factors.

## Other matching claims and limits of the main-paper evidence

- `MAIN-N096` (PDF p.2 Key Points) repeats the primary intervention/control increases, 4.7 versus 2.5 points, range 0-17 and minimal clinically important difference 1 point; it matches `MAIN-N026`/`MAIN-S003` but does not repeat the CI or P value.
- `MAIN-N097` (PDF pp.1, 11) repeats the qualitative conclusion that the intervention produced a significantly greater 12-month increase in diet adherence; it matches `MAIN-S003` and contains no additional numeric estimate.
- `MAIN-N098` (PDF p.8) reports 18 intervention versus 3 control interactions in 6 months, characterized as 6-fold higher intervention contact; it is a treatment-delivery quantity, not an outcome contrast.
- `MAIN-N099` (PDF p.11) reports 36 interactions during the first year; this is a discussion-level treatment-delivery statement and is distinct from the p.8 six-month 18-versus-3 comparison.
- `MAIN-N100` (PDF p.12) correction notice: corrected November 1, 2021, for eTable 1 in Supplement 2 to indicate bone density and body composition measured with DXA at 1- and 3-year follow-up. This provides no corrected result number within the assigned main-paper source.

## Relationship totals and limitations

- **Numeric/reporting relationships mapped:** 100 (`MAIN-N001` through `MAIN-N100`).
- **Inferential-statistical relationships mapped:** 55 (`MAIN-S001` through `MAIN-S055`). These include all printed main-paper Table 2/3 modelled contrasts and P values, food narrative contrasts, Figure 4 P values, and contextual reported HRs where printed.
- **Direct-source coverage:** all 14 assigned PDF pages inspected through a fresh native/layout extraction matching the reusable locator.
- **Limitations:** Figure 2, Figure 3, and Figure 4 boxplots do not print individual-bin counts or exact plotted medians/IQRs/whisker coordinates; they are recorded as display/label relationships only. Main-paper narrative refers to supplement eTables/eFigures, but their quantitative contents are outside this assigned DOC-001 scope. No OCR was required because the fresh native layout extraction was usable and exactly matched the reusable layout artifact.
