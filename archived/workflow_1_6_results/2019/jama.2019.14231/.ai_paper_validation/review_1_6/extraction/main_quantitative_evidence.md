# Main quantitative evidence map — Workflow 1.6

## Scope and provenance

Runtime ID: 01a12882-140f-7461-abff-e4b82f713701; canonical task /root/main_mapper. Source DOC-001, REPORT, jama_aminian_2019_oi_190103.pdf, physical PDF pp. 1–12, printed pp. 1271–1282. All 12 pages mapped; reusable-backed 12, fresh-required 0. No scientific coverage gap. Only raw source-matched per-page native text under .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/ was used as extraction input. Existing images pp. 3, 5, 6, 7, 8, 9, 10 were visually inspected to assign table columns, panels, axes, labels, and captions. These are reusable legacy renderings (engine unrecorded); curator validated native text against direct Poppler 26.01.0. No fresh derivative or OCR was needed. Direct source remains final authority. No candidate conclusions or old extraction-map conclusions read. No diagnoses or judgments made.

All links below are relative to this artifact. Source pages use ../../../jama_aminian_2019_oi_190103.pdf#page=N. Scalar table cells retain printed precision; parentheses mean IQR for median rows and percent for count rows. A dash in a range separates endpoints; negative signs are retained. The article contains Table 1 (two pages), Table 2, and Figures 1–5. Table 3 is not present.

Numeric relationships N001–N020 are complete grouped inventories, with each baseline row and each risk set retained below as a separately addressable row within its group. Inferential relationships S001–S024 are enumerated without significance-based selection. Downstream global inventories may expand numeric groups into individual scalar or row IDs; the explicit row labels and source pages are the matching keys. No reported test statistic or numerical standard error occurs in the main article; standard-error method is recorded.

## Physical-page coverage

| PDF page | Printed page | Location | Mapped scope | Status |
|---|---:|---|---|---|
| 1 | 1271 | [Abstract](../../../jama_aminian_2019_oi_190103.pdf#page=1) | Cohort, baseline repetitions, primary/mortality full inference, 6/3/7 endpoint counts, dates | COMPLETE |
| 2 | 1272 | [Methods and Key Points](../../../jama_aminian_2019_oi_190103.pdf#page=2) | Cohort, eligibility thresholds, population, index/follow-up definitions, primary endpoint | COMPLETE |
| 3 | 1273 | [Figure 1 and Methods](../../../jama_aminian_2019_oi_190103.pdf#page=3) | Every flow box and exclusion count; overlap footnotes; endpoint risk definitions | COMPLETE |
| 4 | 1274 | [Methods and Results](../../../jama_aminian_2019_oi_190103.pdf#page=4) | Models/tests, procedures, follow-up, covariate repetitions, primary/secondary/mortality results | COMPLETE |
| 5 | 1275 | [Table 1](../../../jama_aminian_2019_oi_190103.pdf#page=5) | Every demographic/history row, all three cohorts and both standardized-difference columns | COMPLETE |
| 6 | 1276 | [Table 1 continued and Results](../../../jama_aminian_2019_oi_190103.pdf#page=6) | Every clinical/laboratory/missingness/medication row; all footnotes; PH and time-varying claims | COMPLETE |
| 7 | 1277 | [Figure 2, Table 2, Results](../../../jama_aminian_2019_oi_190103.pdf#page=7) | Both panels, both risk sets, all eight outcome rows and footnotes, metabolic and adverse-event results | COMPLETE |
| 8 | 1278 | [Figure 3 and sensitivity text](../../../jama_aminian_2019_oi_190103.pdf#page=8) | Six panels with HR/CI/P, every risk set, outcome-specific follow-up IQRs | COMPLETE |
| 9 | 1279 | [Figure 4 and Discussion](../../../jama_aminian_2019_oi_190103.pdf#page=9) | Two panels with mean differences/CI/P; spline caption; study and cited-background numerical claims | COMPLETE |
| 10 | 1280 | [Figure 5 and Discussion](../../../jama_aminian_2019_oi_190103.pdf#page=10) | Six panels, all P values, axes, proportions/pointwise CI and Fisher-test caption | COMPLETE |
| 11 | 1281 | [Discussion, Limitations, Conclusion](../../../jama_aminian_2019_oi_190103.pdf#page=11) | Current-study exposure <10%, result direction/E-value claims; cited-background values | COMPLETE |
| 12 | 1282 | [Article information and References](../../../jama_aminian_2019_oi_190103.pdf#page=12) | No applicable new study-result numerical relationship; bibliographic identifiers/date/volume/page/grant numbers are not result quantities | COMPLETE_NO_APPLICABLE_NEW_RESULT |

## N001: Cohort and Figure 1 flow

Locations: abstract p. 1; Key Points and cohort derivation p. 2; Figure 1 with caption/footnotes p. 3; Results p. 4; Table 1 headings pp. 5–6 and footnote a p. 6.

| Flow location | Printed count/definition |
|---|---|
| Initial screen | 287438 total patients with diagnosis of type 2 diabetes; Cleveland Clinic Health System; 1998–2017 |
| Surgical codes | 2818 had metabolic/bariatric surgery codes |
| Nonsurgical branch | 284620 nonsurgical controls |
| Chart-review exclusions | 61 no metabolic/bariatric surgery on chart review |
| Surgical potentially eligible | 2757 |
| Nonsurgical first exclusions | 195677 total; 116031 diagnosis of diabetes after assigned date; 79646 no follow-up after assigned date |
| Nonsurgical potentially eligible | 88943 |
| Surgical enrollment exclusions | 470 total; 240 no documented type 2 diabetes before surgery; 133 no BMI criteria; 99 cancer; 29 ED admission within 5 d before surgery; 24 no age criteria; 19 prior organ transplant; 13 ejection fraction <20% |
| Nonsurgical enrollment exclusions | 49676 total; 39821 no BMI criteria or missing BMI; 12004 no age criteria; 9888 no documented type 2 diabetes; 3291 cancer; 1006 ejection fraction <20%; 855 prior organ transplant; 537 ED admission within 5 d; 87 died within 30 d after assigned date |
| Eligible nonsurgical before matching | 39267 |
| Matching exclusions | 27832 not matched in 1:5 process |
| Included surgical | 2287 |
| Included matched nonsurgical | 11435 (1:5) |
| Total analytical cohort | 13722 |

Figure 1 footnote a: some patients met multiple exclusion criteria, so enrollment-reason counts are overlapping. Footnote b: HbA1c <6.5% and no diabetes medication at index excludes a patient. Caption: BMI ≥30 before matching; propensity match to 5 controls using 7 a priori potential confounders (index date, age, sex, BMI, location, insulin, end-organ complications). Figure 1 text uses “type 2 diabetes medllitus”; retained here as a locator, not a scientific quantity.

## N002: Eligibility, population, outcome, and time definitions

Methods pp. 2–3; abstract p. 1. Source EHR through December 31, 2018; base diagnosis January 1, 1998–December 31, 2017. Surgical index = first metabolic surgery; nonsurgical index = a single randomly assigned surgical index date. Inclusion ages 18–80 y, BMI ≥30 kg/m², HbA1c ≥6.5% or at least 1 diabetes medication. Exclusions: liver/heart/lung transplant, severe heart failure ejection fraction <20% any time before index, active cancer, gastrointestinal cancer code within 1 y before index, ED admission within 5 d, gastroesophageal cancer/peptic ulcer diagnosis or procedure during surgical admission. Controls additionally exclude diabetes diagnosis after assigned date, follow-up on/before assigned date, already dead or death within 30 d after assigned date, and criteria 1–8 from surgery.

Primary extended MACE = 6-component first occurrence of all-cause mortality, coronary artery events (unstable angina, myocardial infarction, coronary intervention/surgery), cerebrovascular events (ischemic/hemorrhagic stroke, carotid intervention/surgery), heart failure, nephropathy, atrial fibrillation. Secondary composite = 3-component all-cause mortality, myocardial infarction, ischemic stroke. Other 6 secondary endpoints = individual primary components; total 7 secondary outcomes and 8 primary-plus-secondary modeled outcomes. Composite assessments exclude no patients, but baseline conditions do not count as new events. Individual nonfatal endpoints exclude patients with that same prior condition from that endpoint's risk assessment only. Death source combines EHR, Social Security, and State Death Indices. Weight, HbA1c, and prescription dates track longitudinal metabolic/drug outcomes. Major surgical complications window 90 d. Nutritional variables: hemoglobin, protein, albumin, vitamin D.

## N003: Quantitative methods and inferential metadata

Statistical Analysis pp. 3–4; Table 2 footnotes p. 7; Figure 4 caption p. 9; Figure 5 caption p. 10.

Baseline summaries median (IQR) and number (%). Doubly robust estimation combines propensity score and outcome regression. Propensity logistic model uses logit link and nearest-neighbor 1:5 match using 7 confounders; BMI categories 30–34.9, 35–39.9, ≥40; Ohio vs Florida. Cause-specific event rates per 100 patient-years from index estimated by study group; actual rates/person-time not printed in main article (eTable 4 locator). Kaplan–Meier cumulative incidence at 8 y; ARD as nonsurgical minus surgical, 95% percentile bootstrap CI from 1000 iterations/samples. Fully adjusted Cox proportional hazards for all 8 outcomes; all Table 1 baseline variables adjust potential confounding. HR is surgery versus nonsurgical relative instantaneous risk. Weighted-residual Grambsch–Therneau PH tests. Baseline missingness multiply imputed by chained equations into 5 datasets; predictive mean matching numeric, logistic binary, polytomous logistic categorical; Rubin formula imputation-corrected SEs.

Subgroup primary analyses individually add treatment-by-variable interaction to fully adjusted Cox; P/CI estimated. Longitudinal metabolic/nutritional mean changes use 4-knot spline on time interacted with treatment. Methods specify 2-sample proportions test for prescribed medications at 1, 2, 5, 8 y. Figure 5 caption independently specifies Fisher exact test at 8 y. Two-sided significance .05; 95% CIs; secondary outcomes exploratory due multiple comparisons. R version 3.5.0.

Sensitivity: random control index assignment 5 times, matching 1:1, 1:5, 1:10 yielding 15 datasets; fully adjusted Cox all outcomes. Time-varying HR at 2, 5, 8 y using restricted cubic spline of observed follow-up time interacted with treatment. E-value robustness to unmeasured confounding. These are definitions and locations, not calculations or diagnoses.

## N004: Surgical procedures and BMI distribution

Results p. 4. Surgical cohort denominator 2287: Roux-en-Y gastric bypass 1443 (63%); sleeve gastrectomy 730 (32%); adjustable gastric banding 109 (5%); duodenal switch 5 (no percentage printed). BMI ≥40: 1713 (75%); 35–39.9: 465 (20%); 30–34.9: 109 (5%). Table 1 prints more precise BMI percentages 74.9, 20.3, 4.8. Procedures and BMI categories are distinct classifications, not interchangeable counts.

## N005: Follow-up quantities

Abstract p. 1 and Results p. 4: overall median 3.9 y (IQR 1.9–6.1), nonsurgical 4.0 (2.1–6.1), surgical 3.3 (1.2–6.3). Figure 2 caption p. 7 repeats both group values for both composites. Figure 3 caption p. 8 provides outcome-specific observation times:

| Outcome | Nonsurgical median (IQR), y | Surgical median (IQR), y |
|---|---|---|
| Mortality | 4.0 (2.1–6.1) | 3.3 (1.2–6.3) |
| Heart failure | 4.1 (2.2–6.2) | 3.3 (1.1–6.4) |
| Coronary artery disease | 4.0 (2.1–6.1) | 3.3 (1.1–6.4) |
| Nephropathy | 4.1 (2.2–6.2) | 3.3 (1.1–6.3) |
| Cerebrovascular disease | 4.0 (2.1–6.1) | 3.3 (1.1–6.3) |
| Atrial fibrillation | 4.0 (2.1–6.1) | 3.3 (1.1–6.3) |

## N006: Complete Table 1 baseline scalar rows

Source pp. 5–6. Column order is surgical n=2287; unmatched nonsurgical n=39267; standardized difference before matching; matched nonsurgical n=11435; standardized difference after matching. Every printed scalar is retained. Counts are patients, not events or rates; missing percentages use corresponding cohort denominator. Median quantities and IQR retain printed units.

| Page | Baseline row/unit | Surgical | Unmatched nonsurgical | SD before | Matched nonsurgical | SD after |
|---:|---|---|---|---:|---|---:|
| 5 | Index date, median (IQR), month/year | 1/2013 (7/2010–4/2015) | 6/2014 (5/2012–2/2016) | −42.6 | 7/2013 (5/2011–4/2015) | −15.9 |
| 5 | Women, n (%) | 1499 (65.5) | 20372 (51.9) | 28.0 | 7339 (64.2) | 2.9 |
| 5 | Men, n (%) | 788 (34.5) | 18895 (48.2) | −28.0 | 4096 (35.8) | −2.9 |
| 5 | Age, median (IQR), y | 52.5 (43.7–60.5) | 61.6 (53.1–68.9) | −75.3 | 54.8 (46.2–62.5) | −19.9 |
| 5 | BMI, median (IQR), kg/m² | 45.1 (40–51.8) | 35.9 (32.7–60.6) | 113.5 | 42.6 (39.4–47.2) | 34.4 |
| 5 | BMI 30–34.9, n (%) | 109 (4.8) | 17110 (43.6) | −101.7 | 495 (4.3) | 2.1 |
| 5 | BMI 35–39.9, n (%) | 465 (20.3) | 11320 (28.8) | −19.8 | 2595 (22.7) | −5.7 |
| 5 | BMI ≥40, n (%) | 1713 (74.9) | 10837 (27.6) | 107.4 | 8345 (73.0) | 4.4 |
| 5 | Weight, median (IQR), kg | 126.5 (110.2–148.0) | 104.8 (93.0–119.0) | 88.3 | 120.2 (106.8–136.5) | 27.8 |
| 5 | White, n (%) | 1734 (75.8) | 29014 (73.9) | 4.45 | 7994 (69.9) | 13.3 |
| 5 | Black, n (%) | 441 (19.3) | 8138 (20.7) | −3.6 | 2804 (24.5) | −12.7 |
| 5 | Other race, n (%) | 54 (2.4) | 874 (2.2) | 0.9 | 234 (2.1) | 2.1 |
| 5 | Race missing, n (%) | 58 (2.5) | 1241 (3.2) | −3.8 | 403 (3.5) | −5.8 |
| 5 | Annual zip-code income, median (IQR), $ | 49855 (39964–62273) | 50378 (37958–65536) | 0.7 | 48732 (36951–61512) | 10.8 |
| 5 | Income missing, n (%) | 70 (3.1) | 494 (1.3) | 12.4 | 125 (1.1) | 13.8 |
| 5 | Never smoking, n (%) | 1231 (53.8) | 18087 (46.1) | 15.6 | 5615 (49.1) | 9.5 |
| 5 | Former smoking, n (%) | 828 (36.2) | 15531 (39.6) | −6.9 | 4012 (35.1) | 2.3 |
| 5 | Current smoking, n (%) | 170 (7.4) | 5051 (12.9) | −18.1 | 1607 (14) | −21.5 |
| 5 | Smoking missing, n (%) | 58 (2.5) | 598 (1.5) | 7.2 | 201 (1.8) | 5.4 |
| 5 | Ohio, n (%) | 1816 (79.4) | 35482 (90.4) | −30.9 | 9834 (86.0) | −17.5 |
| 5 | Florida, n (%) | 471 (20.6) | 3785 (9.6) | 30.9 | 1601 (14.0) | 17.5 |
| 5 | Hypertension, n (%) | 1953 (85.4) | 30308 (77.2) | 21.2 | 8565 (74.9) | 26.5 |
| 5 | Dyslipidemia, n (%) | 1686 (73.7) | 27717 (70.6) | 7.0 | 7457 (65.2) | 18.6 |
| 5 | Peripheral neuropathy, n (%) | 242 (10.6) | 4569 (11.6) | −3.4 | 1203 (10.5) | 0.2 |
| 5 | Heart failure, n (%) | 238 (10.4) | 4470 (11.4) | −3.1 | 1342 (11.7) | −4.2 |
| 5 | Coronary artery disease, n (%) | 237 (10.4) | 5863 (14.9) | −13.8 | 1104 (9.7) | 2.4 |
| 5 | COPD, n (%) | 206 (9.0) | 4179 (10.6) | −5.5 | 1188 (10.4) | −4.7 |
| 5 | Nephropathy, n (%) | 191 (8.4) | 5069 (12.9) | −14.8 | 1219 (10.7) | −7.8 |
| 5 | Atrial fibrillation, n (%) | 152 (6.6) | 3242 (8.3) | −6.1 | 701 (6.1) | 2.1 |
| 5 | Peripheral arterial disease, n (%) | 123 (5.4) | 3426 (8.7) | −13.1 | 755 (6.6) | −5.2 |
| 5 | Myocardial infarction, n (%) | 55 (2.4) | 1201 (3.1) | −4.0 | 211 (1.8) | 3.9 |
| 5 | Cerebrovascular disease, n (%) | 42 (1.8) | 1703 (4.3) | −14.5 | 358 (3.1) | −8.3 |
| 5 | Ischemic stroke, n (%) | 34 (1.5) | 1385 (3.5) | −13.1 | 298 (2.6) | −7.9 |
| 5 | Dialysis, n (%) | 14 (0.6) | 322 (0.8) | −2.5 | 78 (0.7) | −0.9 |
| 6 | HbA1c, median (IQR), % | 7.1 (6.3–8.2) | 7 (6.4–8.1) | −2.3 | 7.1 (6.4–8.4) | −11.4 |
| 6 | HbA1c missing, n (%) | 159 (7.0) | 4899 (12.5) | −18.7 | 1288 (11.3) | −15.0 |
| 6 | Systolic BP, median (IQR), mm Hg | 138 (127–148) | 130 (120–142) | 31.6 | 130 (121–142) | 30.1 |
| 6 | Systolic BP missing, n (%) | 0 | 234 (0.6) | −10.9 | 54 (0.5) | −9.7 |
| 6 | Diastolic BP, median (IQR), mm Hg | 71 (65–79) | 76 (69–82) | −35.3 | 78 (70–84) | −44.2 |
| 6 | Diastolic BP missing, n (%) | 0 | 234 (0.6) | −10.9 | 54 (0.5) | −9.7 |
| 6 | eGFR, median (IQR), mL/min | 90 (72–108) | 86 (68–105) | 11.5 | 92 (72–112) | −8.1 |
| 6 | eGFR missing, n (%) | 1 (0) | 1620 (4.1) | −28.9 | 432 (3.8) | −27.5 |
| 6 | HDL-C, median (IQR), mg/dL | 44 (37–52) | 43 (36–52) | 1.6 | 43 (36–51) | 4.9 |
| 6 | HDL-C missing, n (%) | 792 (34.6) | 12966 (33.0) | 3.4 | 3512 (30.7) | 8.4 |
| 6 | LDL-C, median (IQR), mg/dL | 92 (72–115) | 89 (68–114) | 5.5 | 93 (72–118) | −4.9 |
| 6 | LDL-C missing, n (%) | 208 (9.1) | 10469 (26.7) | −47.1 | 2947 (25.8) | −45.1 |
| 6 | Triglycerides, median (IQR), mg/dL | 146 (101–209) | 143 (101–205) | 1.8 | 146 (103–208) | −1.4 |
| 6 | Triglycerides missing, n (%) | 160 (7) | 6538 (16.7) | −30.2 | 1816 (15.9) | −28.2 |
| 6 | UACR, median (IQR), mg/g | 14 (6–40) | 14 (5–40) | −0.5 | 14 (5–43) | −3.8 |
| 6 | UACR missing, n (%) | 1003 (43.9) | 14665 (37.4) | 13.3 | 4224 (36.9) | 14.1 |
| 6 | Noninsulin diabetes medication, n (%) | 1869 (81.7) | 32428 (82.6) | −2.2 | 9253 (80.9) | 2.1 |
| 6 | Noninsulin medication count 0, n (%) | 418 (18.3) | 6839 (17.4) | 2.2 | 2182 (19.1) | −2.1 |
| 6 | Noninsulin medication count 1, n (%) | 1088 (47.6) | 18206 (46.4) | 2.4 | 5218 (45.6) | 3.9 |
| 6 | Noninsulin medication count 2, n (%) | 560 (24.5) | 10084 (25.7) | −2.8 | 2929 (25.6) | −2.6 |
| 6 | Noninsulin medication count ≥3, n (%) | 221 (9.7) | 4138 (10.5) | −2.9 | 1106 (9.7) | 0 |
| 6 | Insulin, n (%) | 776 (33.9) | 10811 (27.5) | 13.9 | 3806 (33.3) | 1.4 |
| 6 | Lipid-lowering medications, n (%) | 1195 (52.3) | 23963 (61.0) | −17.8 | 5998 (52.5) | −0.4 |
| 6 | Renin–angiotensin system inhibitors, n (%) | 1396 (61.0) | 25375 (64.6) | −7.4 | 7102 (62.1) | −2.2 |
| 6 | Other antihypertensives, n (%) | 1649 (72.1) | 28710 (73.1) | −2.2 | 8066 (70.5) | 3.5 |
| 6 | Aspirin, n (%) | 731 (32.0) | 18961 (48.3) | −33.8 | 4627 (40.5) | −17.8 |
| 6 | Warfarin, n (%) | 190 (8.3) | 3207 (8.2) | 0.5 | 943 (8.2) | 0.2 |

## N007: Table 1 footnotes and matching narrative

Table 1 footnote b p. 6 defines standardized differences as “the absolute value of the difference in means or proportions between the groups (metabolic surgery − nonsurgical control group) divided by pooled standard deviation.” No numerical pooled SD supplied. The printed signed columns are retained without interpreting this definition. Footnote c BMI = weight kg / height m squared. Footnote d eGFR approximated using MDRD Study equation. Footnote e drug classes in eTable 3. Footnote f renin–angiotensin includes ACE inhibitors and angiotensin receptor blockers. SI factors: HDL/LDL mg/dL to mmol/L ×0.0259; triglycerides ×0.0113.

Abstract p. 1 repeats female 65.5% vs 64.2%, age 52.5 vs 54.8 y, BMI 45.1 vs 42.6, HbA1c 7.1% vs 7.1%; baseline covariates described as balanced. Results p. 4 calls 37 baseline covariates mostly balanced; repeats weight 126.5 vs 120.2 kg, BMI 45.1 vs 42.6, dyslipidemia 74% vs 65%, hypertension 85% vs 75%, controls older 54.8 vs 52.5 y, black 25% vs 19%, current smoking 14% vs 7%, aspirin 40% vs 32%. These last comparisons reverse the presentation order to control vs surgery. No numerical significance tests printed for baseline comparisons.

## N008 and S001–S008: Complete Table 2 and matching outcome results

Source p. 7, Table 2. All CIs are 95%. No. at risk is baseline eligible population for that endpoint, not 8-y remaining risk set. CI8 = Kaplan–Meier cumulative incidence at 8 y, percent. ARD = absolute 8-y nonsurgical minus surgical risk, percent; 95% percentile bootstrap interval (1000 samples). HR/CI/P = fully adjusted Cox surgery vs nonsurgical, adjusting all Table 1 baseline variables.

| Statistical ID | Endpoint | Surgical n | Surgical CI8 (95% CI), % | Nonsurgical n | Nonsurgical CI8 (95% CI), % | ARD (95% CI), % | Adjusted HR (95% CI) | P |
|---|---|---:|---|---:|---|---|---|---|
| S001 | Primary extended 6-component MACE | 2287 | 30.8 (27.6–34.0) | 11435 | 47.7 (46.1–49.2) | 16.9 (13.1–20.4) | 0.61 (0.55–0.69) | <.001 |
| S002 | Secondary 3-component MACE | 2287 | 17.0 (14.3–19.7) | 11435 | 27.6 (26.2–29.0) | 10.6 (7.5–13.6) | 0.62 (0.53–0.72) | <.001 |
| S003 | All-cause mortality | 2287 | 10.0 (7.8–12.2) | 11435 | 17.8 (16.6–19.0) | 7.8 (5.1–10.2) | 0.59 (0.48–0.72) | <.001 |
| S004 | Heart failure | 2049 | 6.8 (4.9–8.6) | 10093 | 18.9 (17.6–20.2) | 12.9 (10.4–15.1) | 0.38 (0.30–0.49) | <.001 |
| S005 | Coronary artery disease | 2050 | 7.9 (5.9–9.8) | 10331 | 11.6 (10.5–12.6) | 4.2 (1.9–6.8) | 0.69 (0.54–0.87) | .002 |
| S006 | Cerebrovascular disease | 2245 | 4.1 (2.7–5.5) | 11077 | 5.6 (4.9–6.3) | 1.8 (−0.03 to 3.4) | 0.67 (0.48–0.94) | .02 |
| S007 | Nephropathy | 1937 | 6.1 (4.4–7.8) | 9190 | 16.3 (15.0–17.6) | 11.1 (8.8–13.6) | 0.40 (0.31–0.52) | <.001 |
| S008 | Atrial fibrillation | 2135 | 7.9 (6.1–9.7) | 10734 | 13.6 (12.5–14.7) | 6.5 (4.4–8.7) | 0.78 (0.62–0.97) | .03 |

Every S001–S008 includes both group cumulative-incidence CIs, ARD/CI and HR/CI/P as distinct measures within a matched endpoint group. They must not be presumed to share the same test or CI construction.

## N009: Narrative and abstract outcome occurrences

| Page/location | Matched group | Every printed quantity or statistical claim |
|---|---|---|
| 1 abstract Results | S001 | 385 surgical and 3243 nonsurgical primary events; CI8 30.8% (27.6–34.0) vs 47.7% (46.1–49.2), P<.001; ARD 16.9% (13.1–20.4); adjusted HR 0.61 (0.55–0.69) |
| 1 abstract Results | S003 | 112 surgical and 1111 nonsurgical deaths; CI8 10.0% (7.8–12.2) vs 17.8% (16.6–19.0); ARD 7.8% (5.1–10.2); adjusted HR 0.59 (0.48–0.72); all 7 prespecified secondary outcomes significant in favor of surgery |
| 2 Key Points | S001 | 13722 patients, including 2287 surgery/11435 controls; significant lower MACE risk, HR 0.61 |
| 4 Primary End Point | S001 | 385/3243 primary events; same CI8/CI, ARD/CI and HR/CI as abstract; P<.001; no interaction heterogeneity across sex, age, BMI, HbA1c, eGFR, insulin, sulfonylurea, lipid-lowering use |
| 4 Secondary End Points | S002 | 194 surgical and 1765 nonsurgical secondary events; CI8 17.0% vs 27.6%; ARD 10.6% (7.5–13.6); HR 0.62 (0.53–0.72); significant lower incidence |
| 4 Secondary End Points | S003 | 112/1111 deaths; same CI8/CI, ARD/CI, HR/CI as abstract |
| 4→6 continuation | S004–S008 | Other 5 individual endpoints significantly lower; event rates/ARD referred to Table 2/eTables 4–5 |
| 9 Discussion | S001–S008 | Cumulative incidence described as 48% control vs 31% surgery; all 6 prespecified individual outcomes significantly lower; narrower 3-component outcome also significantly lower; 8-y mortality ARD 7.8% |
| 10–11 Discussion | S004,S007,S008 | Lower heart failure despite lower cardiovascular medication use; lower atrial fibrillation risk; lower diabetic nephropathy incidence |
| 11 Conclusion | S001 | Significantly lower incident MACE risk; observational finding requires randomized trial confirmation |

## N010: Figure 2 complete risk sets and axes

Source p. 7. Two Kaplan–Meier cumulative-incidence panels; x = years since index 0,2,4,6,8; y percent 0,10,20,30,40,50. Orange surgery curve and blue-gray nonsurgical curve separately labeled. Panel A HR 0.61 (95% CI 0.55–0.69), P<.001 (S001). Panel B HR 0.62 (0.53–0.72), P<.001 (S002). Caption endpoint definitions and group observation times are N002/N005. No numerical confidence band endpoints printed in this figure.

| Panel/group | At 0 y | 2 y | 4 y | 6 y | 8 y |
|---|---:|---:|---:|---:|---:|
| A Primary nonsurgical | 11435 | 8050 | 4791 | 2244 | 838 |
| A Primary surgical | 2287 | 1372 | 910 | 535 | 293 |
| B Secondary nonsurgical | 11435 | 8645 | 5543 | 2826 | 1130 |
| B Secondary surgical | 2287 | 1438 | 991 | 610 | 336 |

## N011: Figure 3 complete risk sets and axes

Source p. 8. Six Kaplan–Meier panels, y cumulative incidence (%) 0,5,10,15,20; x years since index 0,2,4,6,8. Surgical vs nonsurgical labels retained. Every HR/CI/P is printed in the corresponding panel and matches the values transcribed under S003–S008: A mortality S003 P<.001; B heart failure S004 P<.001; C coronary S005 P=.002; D cerebrovascular S006 P=.02; E nephropathy S007 P<.001; F atrial fibrillation S008 P=.03. Caption excludes baseline condition for each of 5 nonfatal endpoints only and supplies all observation-time values in N005.

| Panel/group | At 0 y | 2 y | 4 y | 6 y | 8 y |
|---|---:|---:|---:|---:|---:|
| A Mortality nonsurgical | 11435 | 8844 | 5789 | 3005 | 1224 |
| A Mortality surgical | 2287 | 1460 | 1017 | 629 | 353 |
| B Heart failure nonsurgical | 10093 | 7572 | 4845 | 2468 | 991 |
| B Heart failure surgical | 2049 | 1281 | 895 | 552 | 317 |
| C Coronary nonsurgical | 10331 | 7776 | 4958 | 2516 | 995 |
| C Coronary surgical | 2050 | 1283 | 878 | 538 | 299 |
| D Cerebrovascular nonsurgical | 11077 | 8474 | 5492 | 2847 | 1149 |
| D Cerebrovascular surgical | 2245 | 1418 | 982 | 607 | 338 |
| E Nephropathy nonsurgical | 9190 | 7056 | 4515 | 2262 | 893 |
| E Nephropathy surgical | 1937 | 1216 | 838 | 506 | 293 |
| F Atrial fibrillation nonsurgical | 10734 | 8152 | 5212 | 2660 | 1072 |
| F Atrial fibrillation surgical | 2135 | 1328 | 915 | 555 | 319 |

## N012 and S009–S013: Metabolic continuous outcomes, Figure 4

| Statistical ID | Location | Quantity, time, unit, contrast and printed inference |
|---|---|---|
| S009 | p.7 Results | Surgical mean body-weight reduction at 8 y 29.1 kg (95% CI 28.8–29.3); spline model N003; no separate P printed |
| S010 | p.7 Results | Nonsurgical mean body-weight reduction at 8 y 8.7 kg (95% CI 8.6–8.9); no separate P printed |
| S011 | p.7 Results | Between-group mean weight-reduction difference at 8 y 20.3 kg (95% CI 20.1–20.6); no separate P printed |
| S012 | p.9 Figure 4A | Mean total percent weight-loss difference at 8 y Δ=14.7% (95% CI 14.5–14.9), P<.001; percent scale, not kg |
| S013 | p.7 Results and p.9 Figure 4B | Difference in mean HbA1c changes from baseline at 8 y 1.1% (95% CI 1.0–1.2), P<.001 |

Figure 4 caption: smoothed mean percent weight lost from baseline and absolute HbA1c (%) trends; shaded 95% CIs; differences estimated by flexible regression with 4-knot time spline interacting treatment. Comparison and samples in eTables 8–9. Panel A is labeled “Total weight loss, %”; y “Percent Change, % (95% CI)”, printed ticks 0, −5, −10, −15, −20, −25, and a lower printed 0 tick retained exactly; x 0,2,4,6,8 y. Panel B labeled “HbA1c value, %”; y “HbA1c, % (95% CI)”, 5.5,6.0,6.5,7.0,7.5,8.0; x same. Curves show labeled groups; no exact pointwise curve estimates or confidence endpoints are numerically printed beyond Δ. Do not digitize curves into reported data. Figure 4A plotted surgery reductions are negative percent-change values; its Δ is positive difference magnitude as printed.

## N013 and S014–S019: Figure 5 medication proportions and tests

Source p. 10; longitudinal results p. 7; discussion pp. 9,11. All 6 panels plot taking-drug proportion (%) with 95% pointwise CI shading, separate surgery/control labels. Each x-axis years since index 0,2,4,6,8; each y-axis 10,30,50,70,90 %. Proportions computed every tenth of a year starting at index through 8 y. No numeric proportions, counts, or CI endpoints are printed at individual timepoints; numerical samples/comparisons are located in eTables 8,10. Caption specifies Fisher exact P comparing groups at 8 y, while Methods N003 specifies 2-sample proportions testing at 1,2,5,8 y.

| Statistical ID | Panel | Drug | Printed 8-y P | Matched baseline row |
|---|---|---|---|---|
| S014 | A | Noninsulin diabetes medication | <.001 | N006 noninsulin use |
| S015 | B | Insulin | .008 | N006 insulin |
| S016 | C | Renin–angiotensin system inhibitors | <.001 | N006 renin–angiotensin |
| S017 | D | Other antihypertensives | <.001 | N006 other antihypertensives |
| S018 | E | Lipid-lowering medication | <.001 | N006 lipid-lowering |
| S019 | F | Aspirin | <.001 | N006 aspirin |

Narrative p.7: all six uses significantly lower after surgery compared with usual care. Caption defines renin–angiotensin inhibitors as ACE inhibitors and angiotensin receptor blockers. Prescription orders measured, not confirmed consumption (p.11 Limitations). Figure 5 contains no warfarin panel.

## N014: Perioperative adverse-event quantities

Source p. 7, Adverse Events After Metabolic Surgery. Surgical denominator 2287. Median postoperative hospital stay 2 d (IQR 2–3). In 90 d: bleeding requiring transfusion 68 (3.0%); pulmonary adverse events 58 (2.5%); venous thromboembolism 22 (1.0%); cardiac events 17 (0.7%); renal failure requiring dialysis 4 (0.2%); no cerebrovascular events (zero stated, no percent printed); abdominal surgical intervention 109 (4.8%); mortality 15 (0.7%). Early postoperative endoscopy 16.7%, interventional radiology 1.6%, parenteral nutrition 1.4% (no counts printed). Events/procedures can overlap; no mutually exclusive total stated. Postoperative nutritional/endoscopic/radiologic/surgical cumulative incidence in eTable11; nutritional trajectories in eTable8/eFigure3; these are supplied-support matching locators, not main printed scalars.

## N015 and S020: Subgroup interaction relationships

Source p.4 Primary End Point, Methods p.4. Primary fully adjusted Cox treatment interaction individually for sex, age, BMI, HbA1c, eGFR, insulin, sulfonylurea, lipid-lowering use. Narrative states interaction testing revealed no heterogeneity. No interaction P/CI values printed in main; eFigure1 in results supplement contains numeric counterparts. All eight subgroup variables retained. S020 tracks these linked primary subgroup inferential claims as one complete main-only group pending support scalar expansion.

## N016 and S021: Proportional-hazards relationships

Source p.6 continuation, Methods p.4. Weighted-residual test; main narrative states PH satisfied for primary/secondary composite and individual outcomes except atrial fibrillation. P values in eTable6; atrial-fibrillation time-varying HRs in eTable7. No numeric P/statistic in main. S021 retains every outcome's linked PH claim for support matching.

## N017 and S022–S024: Sensitivity, time-varying inference, E-value

S022: Methods p.4 and sensitivity text pp.8–9; 5 random index assignments ×3 matching ratios (1:1,1:5,1:10) =15 datasets, fully adjusted Cox 8 outcomes each; main reports negligible HR differences between those 15 and manuscript single 1:5 cohort; all HR/CIs in eFigure4. No main numerical HR values for sensitivity models.

S023: Methods p.4 and Results p.6; time-varying HR at 2,5,8 y, restricted cubic spline of follow-up interacted treatment; cumulative incidence eTable5 and time-varying HR eTable7 for all endpoints. No time-varying numerical main estimates.

S024: Methods p.4, sensitivity p.9, Limitations p.11; E-values examined for all 8 endpoints, compared with HR estimates of known cardiovascular risk factors (eTable12); statement unmeasured confounder unlikely to account for association. Main p.11 states magnitudes of known MACE risk-factor associations smaller than estimated E-values for primary/secondary endpoints. No numerical main E-value or risk-factor HR.

## N018: Current-study exposure and contextual numerical claims

Main p.11 Limitations: less than 10% of nonsurgical patients exposed to newer diabetes medications, including GLP-1 agonists and SGLT-2 inhibitors; no exact count/time-specific denominator printed. No quantitative comparison of metabolic surgery procedures performed; separate new matched cohorts would be needed. Severity of baseline medical conditions not matching/adjustment basis; relates to population/model definition, not a printed estimate.

## N019: Cited-background quantities retained separately

These are claims printed in this REPORT, not outputs of its main 13722-patient cohort. They may be compared only with supplied evidence, not external literature. Discussion p.9: Look AHEAD weight loss 8.6% vs 0.7% at 1 y and 6.0% vs 3.5% at 9 y, no reduction in MACE; Fisher et al diabetes/BMI>35, 5-y macrovascular HR 0.60 and mortality HR 0.33, annual event rates 2–3 times lower than current; SOS diabetes subgroup 343 surgery/260 controls, vertical banded gastroplasty 66% and banding 18% (p.9→10 continuation). Main p.11: meta-analysis 5% nonsurgical weight loss did not alter atrial-fibrillation incidence; prior studies albuminuria resolved in 50%; another matched cohort nephropathy 59% lower at 5 y; safety improved over last 2 decades. No CI/P printed for these historical values.

## N020: Labels, source matching, and absence records

Main source has no Table3 and no numerical raw event rates per 100 patient-years, person-time totals, numerical standard errors, test statistics, or numeric E-values. Numeric event counts appear only for primary/secondary/mortality and postoperative outcomes. Nonfatal event counts/rates are supplement matching targets. Kaplan–Meier cumulative incidence at 8 y is distinguished from raw event fraction and incidence density. Table2 labels coronary artery disease/cerebrovascular disease correspond to Methods coronary/cerebrovascular event definitions; no assumption that myocardial infarction or ischemic stroke alone equals the broad individual endpoint. Composite outcomes share baseline cohort but have different remaining risk sets.

All inferential display values are positive numeric P thresholds or decimals; no displayed P=0 occurs. Page12 contains funding/conflict/author information and reference bibliographic quantities only, with no additional main-study result scalar. Bibliographic years, DOI numbers, volume/page numbers, trial registry NCT03955952, grant R01-DK105960, author address numbers, and downloaded dates are identity/metadata, not study numerators, denominators, outcomes, or statistical tests.

## Handoff counts and limitations

Physical pages complete: 12/12. Numeric grouped relationships: 20 (N001–N020). Complete Table1: 61 scalar rows (34 on p.5, 27 on p.6), including 3 population columns and 2 standardized-difference columns. Table2: 8 outcome rows, each including 2 populations, 2 cumulative-incidence/CI triples, ARD/CI, HR/CI/P. Figures: 1 flow chart, 2 composite panels, 6 individual panels, 2 continuous panels, 6 medication panels; total 17 figure units (flow counted as one), all mapped. Risk sets: 16 group rows ×5 timepoints =80 counts. Statistical grouped relationships: 24 (S001–S024), covering all printed inference and linked inferential claims with no omitted nonsignificant or unquantified main claim. Main-only inference groups requiring numerical support counterparts are explicitly retained rather than assigned artificial numbers. Exact pointwise curve coordinates and confidence-band endpoints are not printed as scalars, so recorded as graphical trends with axis/caption definitions; no digitization inferred. No scientific coverage gap or tool limitation. Every scalar/footnote has a physical source-page locator; page12 explicitly no applicable new result.

For checker shard sizing, the 24 S groups contain 43 distinct printed inferential tuples: 32 outcome tuples (8 endpoints ×2 group KM estimates/CI, 1 ARD/CI, 1 HR/CI/P), 5 continuous estimate/CI tuples, and 6 P-only drug comparisons. S020–S024 preserve additional unquantified main inferential claims for exact support matching. Repeated abstract/narrative/figure values do not increase the count of distinct tuples. Visual inspection of existing source-linked page3 and page8 images additionally confirmed every flow-chart exclusion location and all individual-endpoint panel/risk-set assignments. The 61 Table1 rows exclude page-coverage ledger rows.
