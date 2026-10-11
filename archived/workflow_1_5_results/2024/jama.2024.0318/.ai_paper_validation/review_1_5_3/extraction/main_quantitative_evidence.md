# Main Quantitative Evidence Map — DOC-001

## Scope, source identity, and method

- **Assigned source and complete unit scope:** `DOC-001`, `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`, PDF pp. 1-11 (all 11 source pages).
- **Source SHA-256:** `0f153cf27727015b19cf33ba400d4c0cc36e20f58a1b85c08f74bd61f1d06647`.
- **Reusable locators:** `document_outputs/DOC-001/preprocessing/normalized_text/page-001.txt` through `page-011.txt`; source-matched renders for pp. 3-8.
- **Fresh mapper confirmation derivatives:** `review_1_5_3/preprocessing/main/DOC-001_pp1-11_direct_layout.txt`, `DOC-001_pp3-8_direct_layout.txt`, and direct PDF renders `DOC-001_direct_confirm-04.png` through `-08.png`. Native/layout text was usable; no OCR was required.
- **Conventions:** N IDs are numeric/reporting relationships; S IDs are inferential/model relationships. Values reproduce printed source values. “Difference” is retained with the source’s stated direction/definition. This is an evidence map only, not a candidate assessment or judgment.

## Page-level coverage record

| PDF page | Result-relevant unit(s) mapped | Relationship IDs | Status |
|---:|---|---|---|
| 1 | Abstract population, follow-up, primary effects, remission, deaths, and narrative conclusion | N001-N006; S001-S004 | COMPLETE |
| 2 | Key Points; eligibility/outcomes/definitions; analysis model and conversion rule | N007-N009; S005-S006 | COMPLETE |
| 3 | Figure 1 flow; baseline/follow-up narrative; HbA1c, procedure, sensitivity, remission, and medication results | N010-N018; S007-S013 | COMPLETE |
| 4 | Table 1 baseline characteristics and continuation of results narrative | N019-N021; S014-S015 | COMPLETE |
| 5 | Figure 2 panels A-D and numbers at risk | N022-N025 | COMPLETE |
| 6 | Table 2 outcome rows/footnotes and weight narrative | N026-N039; S016-S029 | COMPLETE |
| 7 | Figure 3, BMI subgroup, adverse-event and crossover/revision narrative | N040-N045; S030-S034 | COMPLETE |
| 8 | Table 3 counts/percentages and footnotes; matching discussion values | N046-N047 | COMPLETE |
| 9 | Discussion/limitations/conclusion: matching qualitative claims; no new main-study numerical result beyond results already mapped | N048 | COMPLETE — no additional applicable result table/figure |
| 10 | End matter and references only | — | COMPLETE — no applicable main-study result relationship |
| 11 | References only | — | COMPLETE — no applicable main-study result relationship |

## Population, analysis frame, labels, and definitions

### N001 — Abstract population and follow-up

- **Location:** PDF p. 1, Abstract Results; matched narrative PDF p. 3, Results.
- **Population/time:** 262 of 305 eligible participants (86%) enrolled in long-term follow-up; pooled analysis of four US single-center randomized trials conducted May 2007-August 2013, observational follow-up through July 2022; median follow-up 11 years.
- **Descriptive values:** mean (SD) age 49.9 (8.3) years; BMI 36.4 (3.5); 68.3% women; 31% Black; 67.2% White. Medical/lifestyle crossover to surgery: 25% during follow-up.
- **Narrative match:** PDF p. 3 reports 262/305 (86%), the same demographics, BMI 36.4 (3.5), and median (range) follow-up 11 (7-15) years.

### N007 — Eligibility and outcome definitions

- **Location:** PDF p. 2, Methods: Study design and Primary and Secondary Outcomes.
- **Population:** original eligibility: type 2 diabetes, BMI 27-45, age 18-65 years; four centers/trials.
- **Primary outcome:** between-group difference in percent change in HbA1c from baseline to 7 years; results to 12 years for those reaching that point before closure.
- **Secondary outcomes/labels:** change over time in HbA1c; HbA1c <7.0%; diabetes remission, defined as HbA1c <6.5% without diabetes medication for at least 3 months and assessed annually; weight, BMI, lipids, blood pressure, medication use, major cardiovascular adverse events, and microvascular complications. Results are by randomized group and surgical procedure type.

### N008 — Scale and conversion rule

- **Location:** PDF p. 2, Methods; Table 1/Table 2 footnotes, PDF pp. 4 and 6.
- **Rule/unit:** HbA1c mmol/mol = 10.93 × HbA1c − 23.50. Table footnotes state conversion factors for glucose (0.0555), cholesterol (0.0259), triglycerides (0.0113), and creatinine (88.4), with displayed source units mg/dL or μmol/L as applicable.

### S005 — Primary analytic model and contrast

- **Location:** PDF pp. 2-3, Statistical Analysis.
- **Population/contrast/time:** intention-to-treat comparison of change in HbA1c from baseline to 7 years between medical/lifestyle and bariatric-surgery randomized groups.
- **Model label:** linear mixed-effect model for percent change in HbA1c, fixed effects for group, visit, group × visit, site, baseline HbA1c; random participant intercept. Least-square means at each visit; group comparison by a linear contrast.

### S006 — Other analysis labels

- **Location:** PDF p. 3, Statistical Analysis.
- **Model/definitions:** per-protocol sensitivity accounting for medical/lifestyle-to-surgery crossover by inverse-probability weighting; binary outcomes summarized as percentages and analyzed by generalized estimating equations controlling for site and baseline HbA1c, with sandwich-method standard errors. Secondary-outcome results were not adjusted for multiple testing. BMI <35 exploratory analyses use the same models. Death/loss to follow-up assumed random censoring; monotone missing data considered missing at random.

## Abstract and key-point results

### N002 / S001 — HbA1c at 7 years

- **Locations:** PDF p. 1, Abstract Results; PDF p. 2, Key Points; PDF p. 3, Results; Table 2, PDF p. 6.
- **Contrast and values:** medical/lifestyle baseline 8.2%, decrease 0.2% (95% CI, −0.5% to 0.2%) to 8.0%; bariatric-surgery baseline 8.7%, decrease 1.6% (95% CI, −1.8% to −1.3%) to 7.2%. Printed group difference in change: −1.4% (95% CI, −1.8% to −1.0%; P < .001).
- **Narrative match:** Key Points says a 1.4% between-group HbA1c difference at 7 years; Results identifies Table 2/Figure 2A and says surgery values were lower after baseline.

### N003 / S002 — HbA1c at 12 years

- **Locations:** PDF p. 1, Abstract Results; PDF p. 2, Key Points; PDF p. 3, Results; narrative points to eTable 2 in Supplement 2.
- **Contrast/effect:** printed between-group difference in change −1.1% (95% CI, −1.7% to −0.5%; P = .002).
- **Narrative match:** Key Points gives 1.1% at 12 years; Results states the source direction as −1.1%.

### N004 / S003 — Diabetes remission at 7 and 12 years

- **Locations:** PDF p. 1, Abstract Results; PDF pp. 4, 6-7, Results/Table 2/Figure 3.
- **7 years:** medical/lifestyle 6.2% vs bariatric surgery 18.2%; abstract P = .02; Table 2 group odds ratio 3.39 (95% CI, 1.25-9.17), P = .02; Results rounds this to OR 3.4 (95% CI, 1.3-9.2).
- **12 years:** medical/lifestyle 0.0% vs bariatric surgery 12.7%, P < .001 (abstract); Results states the difference remained statistically significant at 12 years (P < .001).
- **Definition:** HbA1c <6.5% and no diabetes medication (Figure 3 footnote adds “not receiving any medications for diabetes”).

### N005 / S004 — Deaths and adverse-event narrative

- **Locations:** PDF p. 1 Abstract; PDF pp. 7-8 Results/Table 3.
- **Values:** abstract: four deaths (2.2%), two in each group; Table 3: 2/96 (2.1%) medical/lifestyle and 2/166 (1.2%) bariatric surgery. Abstract states no group difference in major cardiovascular adverse events and says anemia, fractures, and gastrointestinal adverse events were more common after bariatric surgery.

### N009 — Key Points matching claim

- **Location:** PDF p. 2, Key Points.
- **Claim:** bariatric surgery yielded superior glycemic control with a between-group HbA1c difference of 1.4% at 7 years and 1.1% at 12 years, less diabetes-medication usage, and higher diabetes-remission rates. This is a narrative summary of N002-N004 and N034-N036.

### N006 — Abstract conclusion claim

- **Location:** PDF p. 1, Conclusion and Relevance.
- **Claim:** after 7-12 years, people originally randomized to surgery had superior glycemic control, less diabetes medication use, and higher diabetes-remission rates than those originally randomized to medical/lifestyle intervention. This matches N002-N004 and N015/N038.

## Participant flow, baseline population, and Figures

### N010 — Figure 1 participant flow

- **Location:** PDF p. 3, Figure 1, source-render confirmed.
- **Flow:** 355 randomized: STAMPEDE 155, SLIMM-T2D 88, TRIABETES 69, CROSSROADS 43. Thirty-nine withdrew before intervention; 316 eligible (145, 78, 61, and 32 respectively). Fourteen excluded: 12 withdrew/lost to follow-up and 2 died; 305 available for long-term follow-up and randomized. Original allocations: 193 bariatric surgery (106 Roux-en-Y gastric bypass, 49 sleeve gastrectomy, 38 adjustable gastric banding) and 122 medical/lifestyle. Enrolled ARMMS-T2D: 166 and 96, respectively.
- **Footnote:** three participants lost to follow-up in original trials were successfully rerecruited.
- **Narrative match:** adjacent Results text gives 355, 39, 316, 9 later consent withdrawals, 2 deaths, 305 available, and 262 enrolled.

### N011 — Baseline/follow-up descriptive narrative

- **Location:** PDF p. 3, Results.
- **Values:** randomized analysis groups: medical/lifestyle n = 96, surgery n = 166. Mean (SD) age 49.9 (8.3) years; women 68.3%; Black 31%; White 67.2%; BMI 36.4 (3.5); 96 (36.6%) baseline BMI <35; baseline HbA1c 8.5% (1.5%); median (range) follow-up 11 (7-15) years.

### N017 / S012 — Postbaseline HbA1c trajectory claim

- **Location:** PDF p. 3, Results; Figure 2A, PDF p. 5.
- **Claim/statistical label:** despite higher baseline values in the surgery group, its HbA1c levels were lower at all postbaseline points; P < .001. Figure 2A is the least-square-estimate trajectory described in N022.

### N018 / S013 — Remission comparison at 12 years and procedure comparison label

- **Location:** PDF p. 4, Results.
- **Values/claim:** remission group difference remains statistically significant at 12 years, P < .001. Procedure-specific remission rates at 7 years are 24.5% Roux-en-Y, 15.2% sleeve, and 8.9% adjustable band; comparisons between procedures were not statistically significant.

### N019 — Table 1 participant counts and demographic baseline values

- **Location:** PDF p. 4, Table 1 (N = 262), direct-render confirmed.
- **Columns:** medical/lifestyle n = 96; bariatric surgery n = 166; surgery subgroups: Roux-en-Y n = 89, sleeve n = 41, adjustable band n = 36.
- **Age mean (SD), y:** 51.4 (6.8); 49.0 (9.0); 49.1 (9.0); 48.3 (7.7); 49.6 (10.3).
- **Sex, No. (%):** women 62 (64.6), 117 (70.5), 61 (68.5), 32 (78.0), 24 (66.7); men 34 (35.4), 49 (29.5), 28 (31.5), 9 (22.0), 12 (33.3).
- **Race, No. (%):** Black 35 (36.5), 46 (27.7), 23 (25.8), 13 (31.7), 10 (27.8); White 59 (61.5), 118 (71.1), 64 (71.9), 28 (68.3), 26 (72.2); Other 2 (2.1), 2 (1.2), 2 (2.3), 0, 0. Footnote: Other includes two Asian participants and two reporting more than one race.

### N020 — Table 1 anthropometric/laboratory baseline values

- **Location:** PDF p. 4, Table 1; column order is N019.
- **Mean (SD):** waist cm 113.7 (9.6) [n=95], 115.0 (9.9), 116.1 (9.9), 113.3 (10.2), 114.5 (9.7); weight kg 105.6 (15.5), 103.5 (15.3), 105.2 (15.3), 100.2 (16.7), 103.1 (13.0); BMI 36.2 (3.4), 36.6 (3.6), 37.0 (3.4), 36.3 (4.2), 35.9 (3.2); BMI <35 No. (%) 40 (41.7), 56 (33.7), 26 (29.2), 15 (36.6), 15 (41.7).
- **Blood pressure/duration:** SBP mm Hg 129.7 (15.8), 134.4 (17.7), 135.0 (18.4), 135.8 (19.9), 131.6 (12.7); DBP 79.5 (9.6), 80.4 (10.0), 80.7 (9.8), 81.9 (12.2), 78.2 (7.2); diabetes duration y 8.8 (5.2), 8.3 (5.5), 8.8 (5.9), 7.8 (4.6), 7.5 (5.1).
- **Laboratory:** HbA1c % 8.2 (1.2), 8.7 (1.7), 8.7 (1.6), 9.4 (1.6), 8.2 (1.8); HbA1c <7.0%, No. (%) 11 (11.5), 20 (12.0), 9 (10.1), 0, 11 (30.6); fasting glucose mg/dL 156.5 (50.0) [n=95], 172.0 (69.7), 171.0 (69.5), 172.1 (66.1), 174.6 (75.9); total cholesterol 172.6 (38.5) [n=95], 179.6 (44.8), 176.1 (40.7), 191.2 (46.8), 174.9 (50.7); HDL 44.3 (13.2) [n=95], 42.9 (11.6), 43.6 (11.8), 45.5 (12.2), 38.1 (9.0); LDL 96.3 (33.2) [n=94], 100.3 (34.2) [n=159], 96.3 (31.8) [n=88], 110.8 (41.0), 97.8 (28.7) [n=30].
- **Median (IQR)/mean (SD):** triglycerides mg/dL 140.0 (92.5-221.5) [n=95], 145.0 (103.0-231.8), 143.0 (100.0-239.0), 160.0 (120.0-214.0), 142.5 (94.0-251.5); serum creatinine mg/dL 0.7 (0.2) [n=95], 0.7 (0.2), 0.7 (0.2), 0.7 (0.2), 0.8 (0.2); urine albumin:creatinine ratio 6.0 (4.0-14.5) [n=74], 9.0 (4.0-22.5) [n=119], 7.5 (3.0-28.0) [n=62], 9.0 (7.0-22.0), 6.0 (3.8-12.2) [n=16].

### N021 — Table 1 medication baseline values

- **Location:** PDF p. 4, Table 1; column order is N019.
- **No. (%):** statins 71 (74.0), 121 (72.9), 66 (74.2), 31 (75.6), 24 (66.7); ACEi/ARB 65 (67.7), 108 (65.1), 63 (70.8), 25 (61.0), 20 (55.6); ACEi 59 (61.5), 78 (47.0), 47 (52.8), 17 (41.5), 14 (38.9); insulin 36 (37.5), 82 (49.4), 46 (51.7), 17 (41.5), 19 (52.8); β-blockers 16 (16.7), 30 (18.2), 15 (16.9), 6 (14.6), 9/35 (25.7); ARB 8 (8.3), 30 (18.1), 16 (18.0), 8 (19.5), 6 (16.7).

### S014 — Baseline table scale and missing-value labels

- **Location:** PDF p. 4, Table 1.
- **Label rule:** demographic/medication entries are No. (%); anthropometric and most laboratory entries are mean (SD); triglycerides and urine albumin:creatinine are presented as central value (IQR) despite the table’s printed “mean (SD)” row heading. Bracketed n values identify available measurements; they are not the randomized group totals.

### S015 — Baseline-to-year-7 comparison framework

- **Location:** PDF pp. 3 and 6, Statistical Analysis/Table 2 footnotes.
- **Rule:** Table 2 contrasts model-derived changes rather than arithmetic subtraction of displayed raw baseline/year-7 means; its numeric comparison is surgery change minus medical/lifestyle change and its binary comparison is a year-7 odds ratio. This source-specified distinction applies to all S016-S029a rows.

### N022 — Figure 2 HbA1c trajectories and risk counts

- **Location:** PDF p. 5, Figure 2A-B, source-render confirmed.
- **Metric/scale:** least-square HbA1c estimates (%) at annual visits 0-12; raw-data boxplots display median, mean, IQR, and whiskers to highest/lowest values within 1.5 × IQR. No exact plotted estimate labels are printed; the source provides exact numbers at risk.
- **A, group numbers at risk (years 0-12):** surgery 166, 164, 160, 157, 147, 152, 118, 136, 119, 126, 119, 100, 83; medical/lifestyle 96, 92, 88, 86, 80, 86, 78, 82, 72, 71, 68, 55, 31.
- **B, procedure numbers at risk (years 0-12):** adjustable band 36,35,33,34,34,30,29,33,22,24,23,10,16; Roux-en-Y 89,88,86,84,75,82,60,70,65,68,63,58,40; sleeve 41,41,41,39,38,40,29,33,32,34,33,32,27.
- **Narrative match:** p. 3 says surgery HbA1c was lower at every postbaseline point (P < .001).

### N023 — Figure 2 weight-loss trajectories and risk counts

- **Location:** PDF p. 5, Figure 2C-D, source-render confirmed.
- **Metric/scale:** least-square percentage weight-loss estimates at annual visits 0-12, with raw-data boxplots; no exact plotted estimate labels printed.
- **C, group numbers at risk (years 0-12):** surgery 166,164,161,158,144,149,122,139,121,126,121,106,85; medical/lifestyle 96,91,84,86,79,78,77,75,73,73,70,60,34.
- **D, procedure numbers at risk (years 0-12):** adjustable band 36,34,33,32,31,29,32,31,22,24,25,12,18; Roux-en-Y 89,89,87,86,75,81,60,74,64,68,62,61,41; sleeve 41,41,41,40,38,39,30,34,35,34,34,33,26.

### N024 — Figure 2 display conventions

- **Location:** PDF p. 5, Figure 2 caption.
- **Display rule:** lines/dots are model least-square estimates; boxplots are raw data; horizontal box lines are medians, dots are means, box ends are IQR, and whiskers span the highest/lowest values within 1.5 × IQR. The figure has annual-visit x axes 0-12 and HbA1c % or weight-loss % y axes.

### N025 — Figure 2 relationship claims matched to narrative

- **Locations:** PDF pp. 3 and 6, Results; Figure 2A-D, PDF p. 5.
- **Claim:** Figure 2A supports lower postbaseline HbA1c after surgery; Figure 2B supports procedure-type comparison; Figure 2C-D display group/procedure weight-loss trajectories. Exact source-printed effect values are in N012, N016, and N026/N028 rather than inferred from the graph.

### N040 — Figure 3 remission trajectory

- **Location:** PDF p. 7, Figure 3, source-render confirmed.
- **Metric/definition:** annual percentage achieving remission; remission is HbA1c <6.5% and no diabetes medication.
- **Numbers of participants (years 0-12):** medical/lifestyle 96,92,87,82,78,84,76,79,72,70,67,55,31; bariatric surgery 166,164,151,149,140,146,108,131,116,125,117,99,82.
- **Narrative match:** PDF pp. 3-4 gives 0.5% versus 50.8% at year 1, and 6.2% versus 18.2% at year 7. The figure prints no exact annual percentage labels beyond the plotted scale.

## Results narrative: HbA1c, remission, medication, and weight

### N012 / S007 — HbA1c procedure-type comparisons at year 7

- **Location:** PDF p. 3, Results, points to Figure 2B.
- **Values:** Roux-en-Y change −1.7% (95% CI, −2.0% to −1.3%); sleeve −2.0% (−2.6% to −1.5%); adjustable band −0.8% (−1.3% to −0.2%). Improvement after adjustable band was less than sleeve (P = .007) and Roux-en-Y (P = .03). The text states no significant difference between Roux-en-Y and sleeve improvements.

### N013 / S008 — Per-protocol HbA1c sensitivity at year 7

- **Location:** PDF p. 3, Results, points to eFigure 2A in Supplement 2.
- **Model/contrast:** inverse-probability-weighted per-protocol sensitivity accounting for 25% crossover.
- **Values:** medical/lifestyle change 0.1% (95% CI, −0.5% to 0.7%); surgery −1.4% (−1.7% to −1.2%); between-group difference −1.5% (−2.1% to −0.9%; P < .001).

### N014 / S009 — Remission and glycemic-control results at 7 years

- **Locations:** PDF pp. 3-4, Results; Table 2 PDF p. 6.
- **Remission:** year-1 0.5% medical/lifestyle versus 50.8% surgery. Year-7 6.2% vs 18.2%, OR 3.4 (95% CI, 1.3-9.2; P = .02); surgery procedure subgroup rates: Roux-en-Y 24.5%, sleeve 15.2%, adjustable band 8.9%; between-procedure comparisons not statistically significant.
- **HbA1c <7.0%:** 26.7% medical/lifestyle vs 54.1% surgery at 7 years; OR 3.2 (95% CI, 1.8-5.9; P < .001). HbA1c ≤6.5% stated as similarly different, P = .002; Table 2 labels the outcome as `<6.5%`.

### N015 / S010 — Medication-use results

- **Locations:** PDF pp. 4 and 6, Results; Table 2 PDF p. 6.
- **Values:** baseline diabetes-medication use 99.0% medical/lifestyle and 97.6% (162/166) surgery. Surgery use 38.0% (62/163) at year 1 and 60.5% (72/119) at year 7; text says the group remained lower than baseline during follow-up (P < .001). Medical/lifestyle medication use did not significantly change: P = .19 at year 7 and P = .12 at year 12. At year 7, insulin use: 16% surgery vs 56% medical/lifestyle, P < .001. Incretin/GLP1 agonist use was higher in medical/lifestyle at all annual visits, P < .001.

### N016 / S011 — Weight-loss results

- **Locations:** PDF p. 6, Results/Table 2/Figure 2C-D.
- **7 years:** medical/lifestyle 8.3% weight loss (95% CI, 6.1%-10.5%); surgery 19.9% (18.1%-21.6%), P < .001. Roux-en-Y 22.7% vs adjustable band 14.0%, P < .001; sleeve 19.7% did not differ significantly from other procedures.
- **12 years:** medical/lifestyle 10.8% (95% CI, 8.2%-13.5%) vs surgery 19.3% (17.3%-21.3%), P < .001.
- **BMI ≤25:** year 7 2.7% medical/lifestyle vs 14.4% surgery; year 12 0% vs 15.3%.
- **Per protocol:** year-7 weight loss 5.6% medical/lifestyle vs 20.4% surgery; year-12 7.7% vs 19.4% after crossover accounting.

## Table 2: year-7 outcomes, effect labels, intervals, and P values

**Location for N026-N039 and S016-S029:** PDF p. 6, Table 2, direct-render confirmed. Columns are medical/lifestyle baseline n=96 and year 7 n=82; surgery baseline n=166 and year 7 n=136. Baseline/year-7 entries are mean (SD) or median (IQR). Changes and comparisons are least-square estimates (95% CI). Footnote b: HbA1c is a net change; urine albumin:creatinine is fold change (year 7/baseline); other numeric rows are relative percentage change; binary rows are year-7/baseline odds ratios. Footnote c: numeric group difference = surgery 7-year change minus medical/lifestyle 7-year change; binary difference = odds of surgery outcome divided by medical/lifestyle outcome at year 7. Fasting glucose includes in-person-visit measurements only.

| ID | Outcome, unit/scale | Medical: baseline; year 7; change (95% CI) | Surgery: baseline; year 7; change (95% CI) | Group difference (95% CI); P value |
|---|---|---|---|---|
| N026 / S016 | HbA1c, mean (SD), % | 8.2 (1.2); 8.0 (1.8); −0.2 (−0.5 to 0.2) | 8.7 (1.7); 7.2 (1.4); −1.6 (−1.8 to −1.3) | −1.4 (−1.8 to −1.0); <.001 |
| N027 / S017 | Fasting glucose, mean (SD), mg/dL | 156.5 (50.0); 144.6 (57.3); −3.8% (−14.8% to 7.2%) | 172.0 (69.7); 125.1 (47.0); −14.1% (−22.0% to −6.3%) | −10.3% (−23.6% to 2.9%); .13 |
| N028 / S018 | Weight, mean (SD), kg | 105.6 (15.5); 96.2 (16.6); −8.3% (−10.5% to −6.1%) | 103.5 (15.3); 83.6 (15.8); −19.9% (−21.6% to −18.1%) | −11.6% (−14.3% to −8.9%); <.001 |
| N029 / S019 | SBP, mean (SD), mm Hg | 129.7 (15.8); 128.7 (15.7); −1.1% (−3.9% to 1.7%) | 134.4 (17.7); 128.6 (15.3); −3.4% (−5.6% to −1.2%) | −2.3% (−5.8% to 1.1%); .19 |
| N030 / S020 | DBP, mean (SD), mm Hg | 79.5 (9.6); 74.6 (9.7); −4.3% (−7.0% to −1.6%) | 80.4 (10.0); 74.3 (10.4); −6.0% (−8.1% to −3.8%) | −1.7% (−5.0% to 1.7%); .32 |
| N031 / S021 | LDL, mean (SD), mg/dL | 96.3 (33.2); 97.6 (36.6); 5.5% (−3.3% to 14.3%) | 100.3 (34.2); 103.1 (36.4); 10.8% (3.8% to 17.9%) | 5.4% (−5.6% to 16.3%); .34 |
| N032 / S022 | HDL, mean (SD), mg/dL | 44.3 (13.2); 52.0 (17.0); 20.5% (14.5% to 26.6%) | 42.9 (11.6); 56.5 (16.5); 37.4% (32.6% to 42.3%) | 16.9% (9.4% to 24.4%); <.001 |
| N033 / S023 | Total cholesterol, mean (SD), mg/dL | 172.6 (38.5); 171.7 (41.6); −0.7% (−5.6% to 4.1%) | 179.6 (44.8); 181.4 (40.6); 4.9% (1.0% to 8.7%) | 5.6% (−0.4% to 11.6%); .07 |
| N034 / S024 | Triglycerides, median (IQR), mg/dL | 140 (92.5-221.5); 125 (88-178.3); 2.3% (−8.6% to 13.2%) | 144 (103-231); 107 (82-142); −19.0% (−27.8% to −10.2%) | −21.3% (−34.9% to −7.8%); .002 |
| N035 / S025 | Serum creatinine, mean (SD), mg/dL | 0.7 (0.2); 0.8 (0.4); 9.5% (1.8% to 17.1%) | 0.7 (0.2); 0.8 (0.2); 10.5% (4.4% to 16.7%) | 1.1% (−8.4% to 10.5%); .83 |
| N036 / S026 | Urine albumin:creatinine ratio, median (IQR) | 6 (4-12); 8 (4-13.5); 1.3 (0.9 to 1.9) | 9 (4.5-23); 6 (4-10); 0.9 (0.7 to 1.2) | −0.4 (−1.0 to 0.1); .10 |
| N037 / S027 | Remission of diabetes, % | 0.6; 6.2; OR 10.4 (0.4 to 279.4) | 0.6; 18.2; OR 36.2 (1.9 to 699.0) | OR 3.39 (1.25 to 9.17); .02 |
| N038 / S028 | Diabetes medication use, % | 99.0; 96.0; OR 0.10 (0.01 to 3.27) | 97.6; 60.5; OR 0.03 (0.01 to 0.11) | OR 0.09 (0.03 to 0.24); <.001 |
| N038a / S028a | Oral/GLP1 only, % | 57.3; 40.0; OR 0.53 (0.29 to 0.97) | 47.0; 44.5; OR 0.74 (0.46 to 1.20) | OR 0.98 (0.53 to 1.82); .95 |
| N038b / S028b | Insulin and/or oral/GLP1, % | 41.7; 56.0; OR 1.93 (1.07 to 3.46) | 50.6; 16.0; OR 0.18 (0.11 to 0.31) | OR 0.13 (0.06 to 0.29); <.001 |
| N039 / S029 | HbA1c <7.0%, % | 11.7; 26.7; OR 2.77 (1.38 to 5.54) | 15.5; 54.1; OR 6.42 (3.63 to 11.4) | OR 3.22 (1.76 to 5.88); <.001 |
| N039a / S029a | HbA1c <6.5%, % | 8.3; 17.3; OR 2.30 (1.19 to 4.47) | 12.0; 37.7; OR 4.44 (2.46 to 8.01) | OR 2.89 (1.48 to 5.64); .002 |

## BMI subgroup, procedures, and safety follow-up

### N041 / S030 — BMI subgroup results at year 7

- **Location:** PDF p. 7, Results, points to eFigure 6 in Supplement 2.
- **Population:** 96 participants with BMI 27 to <35 compared with BMI ≥35 at randomization.
- **HbA1c lower-BMI subgroup:** medical/lifestyle −0.4% vs surgery −1.5%; difference −1.2% (95% CI, −1.8% to −0.5%). Higher-BMI subgroup: −0.1% vs −1.6%; difference −1.5% (−2.1% to −1.0%); interaction/comparison with lower-BMI group P = .40. The source says surgery HbA1c was lower at all points, P < .001.
- **Weight-loss lower-BMI subgroup:** 5.6% medical/lifestyle vs 20.4% surgery; difference 14.8% (95% CI, 10.8%-18.8%), P < .001. Higher-BMI values: 10.1% vs 19.3%; difference 9.2% (5.6%-12.9%); differs from lower-BMI group, P = .03.

### N043 / S031 — Lipid, blood-pressure, and renal narrative matches

- **Location:** PDF p. 7, Results; Table 2, PDF p. 6.
- **Claims:** no significant group differences in SBP or LDL at 7 years; HDL was higher (P < .001) and triglycerides lower (P < .001) over time after surgery. The printed year-7 HDL difference is 16.9% (95% CI, 9.4%-24.4%; P < .001); triglyceride relative changes are 2.3% and −19.0%, P = .002. The source says neither serum creatinine nor urine albumin:creatinine ratio changed significantly between groups.

### N044 / S032 — Major-event comparison narrative

- **Location:** PDF p. 7, Results; Table 3, PDF p. 8.
- **Claim:** cardiovascular and other adverse events are described as similar between groups except fractures, anemia, and low iron; Table 3 is the printed count/percentage evidence. The source does not print a Table 3 effect estimate, interval, or P value.

### N045 / S033 — Crossover/revision outcome label

- **Location:** PDF p. 7, Results.
- **Claim:** procedure groups had no significant differences except combined crossover, conversion, and revision procedures, which were more common in medical/lifestyle. The source supplies component counts in N042 but no numerical group-comparison test statistic on this page.

### S034 — Safety-table definition labels

- **Location:** PDF p. 8, Table 3 footnotes.
- **Definitions:** deaths’ assigned causes are stated; alcohol-associated cirrhosis footnote describes two surgical participants’ prior liver findings and follow-up; cancer excludes nonmelanoma skin cancer. These labels delimit the Table 3 event measures.

### N042 — Deaths, kidney outcomes, retinopathy, and procedure crossover/revision

- **Location:** PDF p. 7, Results.
- **Deaths:** four over 12 years: medical/lifestyle 2 (gunshot injury; disability from strokes leading to death), surgery 2 (cardiac event; COVID-19).
- **Kidney/ocular:** dialysis initiated: 2/96 (2.1%) medical/lifestyle vs 0 surgery; retinopathy: 5/96 (5.2%) vs 2/166 (1.2%).
- **Crossover:** 24/96 (25%) medical/lifestyle participants underwent surgery: 8 Roux-en-Y, 15 sleeve, 1 adjustable band; median (range) time 4.5 (0.4-9.8) years.
- **Surgery revisions:** 15 (9%) underwent conversion/revision: seven band removals without further procedure, four band-to-Roux-en-Y conversions, one band-to-sleeve conversion, three sleeve-to-Roux-en-Y revisions (two acid reflux, one chronic fistula).

### N046 — Table 3 adverse events through 12 years

- **Location:** PDF p. 8, Table 3, direct-render confirmed. Columns: medical/lifestyle n=96; surgery n=166; values are No. (%).
- **Death:** 2 (2.1) vs 2 (1.2).
- **Cardiovascular:** coronary revascularization 7 (7.3) vs 15 (9); myocardial infarction 4 (4.2) vs 10 (6); unstable angina 2 (2.1) vs 4 (2.4); significant arrhythmia 4 (4.2) vs 7 (4.2); heart failure 1 (1) vs 5 (3); stroke/transient ischemic attack 3 (3.1) vs 5 (3); peripheral arterial disease 0 vs 2 (1.2); venous thromboembolism 2 (2.1) vs 1 (0.6).
- **Metabolic/gastrointestinal:** severe hypoglycemia 7 (7.3) vs 11 (6.6); diabetic ketoacidosis 1 (1) vs 0; gastric/anastomotic ulcer 2 (2.1) vs 10 (6); bowel obstruction 1 (1) vs 3 (1.8); gastrointestinal leaks 0 vs 1 (0.6); gallstones/cholecystitis 3 (3.1) vs 9 (5.4); pancreatitis 1 (1) vs 3 (1.8); alcohol-associated cirrhosis 0 vs 2 (1.2).
- **Kidney/ocular/transfusion/miscellaneous:** kidney stones 2 (2.1) vs 11 (6.6); initiation of dialysis 2 (2.1) vs 0; retinopathy 5 (5.2) vs 2 (1.2); blindness 1 (1) vs 0; transfusion for anemia 3 (3.1) vs 20 (12); transfusion for gastrointestinal bleeding 2 (2.1) vs 5 (3); fracture 5 (5.2) vs 22 (13.3); cancer (excluding nonmelanoma skin cancer) 4 (4.2) vs 9 (5.4); suicide attempt 0 vs 1 (0.6).
- **Footnotes:** deaths’ causes are listed in N042. The two cirrhosis cases have the stated MASH/steatosis, biopsy, alcohol-use, and 7-/8-year follow-up histories in footnote b.

### N047 — Matching safety narrative and discussion values

- **Locations:** PDF pp. 7-8, Results/Discussion.
- **Narrative match:** source states events were similar except fractures, anemia (hemoglobin <11.5 g/dL), and low iron (<59 μg/dL) were more common after surgery; surgery had lower hemoglobin and higher vitamin B12/vitamin D. It states gastrointestinal events were more common after surgery; no significant procedure-group differences except crossover/conversion/revision combination more common in medical/lifestyle. Discussion rounds remission at year 1/7 to 51%/18% surgery and 0.5%/6% medical/lifestyle; source also restates mean diabetes duration 8 years and mean randomization HbA1c 8.5%.

## Matching discussion/conclusion claims and no-additional-result pages

### N048 — Narrative claims tied to mapped results

- **Locations:** PDF pp. 8-9, Discussion/Conclusions.
- **Claims with mapped evidence:** surgery had more favorable HbA1c, medication use, remission, and weight-loss outcomes at 7 years and up to 12 years; Table 2 supports no between-group SBP/LDL difference and greater HDL/lower triglycerides. The Conclusion says at 7-12 years, people originally randomized to surgery had superior glycemic control, less medication use, and higher remission rates. These are narrative matches to N002-N004, N015-N016, and N026-N039.
- **Additional contextual printed quantities:** a cited prior RCT is described as 5 years/120 participants with a composite outcome in 23% of 57 Roux-en-Y versus 4% of 56 medical/lifestyle participants; another 10-year/60-participant RCT is described as remission 37.5% of 40 surgery versus 5.5% of 18 medical. These are literature-context statements, not outcomes of DOC-001’s study, and are not assigned a separate study-result relationship.

### No-applicable records

- **PDF p. 10:** conflict/funding/data-sharing/end-matter and references; no direct main-study quantitative result, table, figure, statistic, or matching result claim applicable to this mapper scope.
- **PDF p. 11:** references only; no direct main-study quantitative result, table, figure, statistic, or matching result claim applicable.

## Mapping totals and limitations

- **Mapped source units:** 11/11 PDF pages; no scientific-coverage gap in this assigned scope.
- **Relationship records:** 51 numeric/reporting records (N001-N048 plus Table 2 subrows N038a-b and N039a) and 37 inferential/statistical records (S001-S034 plus Table 2 subrows S028a-b and S029a), with cross-references rather than duplicated evidence.
- **Tables/figures:** Figure 1, Table 1, Figure 2A-D, Table 2, Figure 3, and Table 3 were mapped. Direct-PDF visual confirmation was performed for Tables 1-3 and Figures 2-3; Figure 1 was confirmed with its reusable source-matched render and direct layout.
- **Limitations:** Figure 2 and Figure 3 print exact numbers-at-risk but not exact labels for each plotted estimate/percentage; the map preserves their axes, rendering-derived visual relationship, and all printed risk counts rather than manufacturing point values. Supplement-linked eFigures/eTables are documented only where this main article prints values; their underlying pages are outside this assigned disjoint scope.
