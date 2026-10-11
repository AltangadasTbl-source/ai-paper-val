# Main Quantitative Evidence Map — DOC-001-MAIN

## Scope, method, and completeness

- **Direct source:** `jama_sarraj_2024_oi_240006_1708623114.96234.pdf` (14 PDF pages).
- **Assigned units:** PDF pp. 1-14, all mapped. Reusable native text, the historical page map, and renders for pp. 5-9 were used only as locators. Each recorded value was confirmed against the direct PDF using fresh native/layout extraction; fresh derivatives are in `preprocessing/DOC-001-MAIN/`.
- **Identifiers:** `N` records are numeric/reporting relationships; `S` records are inferential-statistical relationships. They are source observations and inventory records, not candidate findings or judgments.
- **Common source definitions:** EVT = endovascular thrombectomy; MM = medical management; mRS = modified Rankin Scale, 0 (no residual deficit/symptoms) through 6 (death). Primary ordinal analyses merge mRS 5 and 6. aGenOR = adjusted generalized odds ratio; aGenOR >1 favours/better 90-day mRS outcome with EVT. Table 2 and Table 3 print `aRR` expanded as “absolute risk reduction,” while their footnotes state that aRR >1 indicates a higher rate ratio for mRS 0-2, 0-3, and 5-6; aRD = absolute risk difference. All table 2/3 effect labels are preserved exactly.

## Page coverage and no-applicable records

| PDF page | Direct-source mapping result |
|---:|---|
| 1 | Abstract population, intervention, outcome scale, and primary reported estimates mapped below. |
| 2 | Study-population eligibility/randomization descriptions mapped; no separate result table, figure, or inferential result. |
| 3 | Imaging/outcome definitions and prespecified quantitative thresholds mapped; no results table. |
| 4 | Analysis populations, models, aggregate results, and ASPECTS treatment-effect narrative mapped. |
| 5 | Table 1 and CTP/MRI-core treatment-effect narrative mapped. |
| 6 | Figure 1 and within-EVT association narrative mapped. |
| 7 | Figure 2, Table 2, and mismatch-count narrative mapped. |
| 8 | Figure 3 axes/labels and mismatch/discordance narrative mapped; curves provide no printed point estimates. |
| 9 | Table 3 and follow-up-infarct narrative mapped. |
| 10 | Follow-up-infarct, age/time association, and quantitative discussion claims mapped. |
| 11 | Discussion and limitations numerical claims mapped. |
| 12 | Conclusion repeats the qualitative result claim; no new result-relevant printed number or estimate. |
| 13 | Administrative material and references only: no applicable result-relevant quantitative unit. |
| 14 | References only: no applicable result-relevant quantitative unit. |

## Population, analysis sets, definitions, and models

| ID | Relationship and exact printed values | Population/time/contrast/model/scale | Direct source location |
|---|---|---|---|
| N001 | SELECT2 randomized **352** adults aged **18-85 years**, across **31** global centers, October 2019-September 2022. | Trial population; EVT vs MM. | [PDF p. 1](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=1>), abstract. |
| N002 | **336/352** analyzed after **16** exclusions: **12** imaging-quality and **4** loss-to-follow-up; randomized groups were **168 EVT** and **168 MM**. | Exploratory-analysis population; 90-day outcome. | [PDF p. 4](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>), Results. |
| N003 | Two randomized MM patients crossed to EVT; as-treated groups are **170 EVT** and **166 medical care only**. | As-treated analyses in Tables 2-3. | [PDF p. 4](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>), Results; [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Table 2. |
| N004 | Primary outcome: 90-day mRS distribution, 0-6; scores 5 and 6 merged for primary analysis. Secondary thresholds: mRS 0-2, 0-3, and 5-6; neurologic worsening = NIHSS increase **>=4** at 24 h (+/-6 h). | Outcome scale/definitions. | [PDF p. 3](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3>), Outcomes. |
| N005 | Ischemic core definitions: CT perfusion relative cerebral blood flow **<30%**; MR diffusion apparent diffusion coefficient **<620 x 10^-6 mm2/s**; critically hypoperfused tissue Tmax **>6 s**. | Imaging units and thresholds. | [PDF p. 2](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=2>), Imaging Evaluation; [PDF p. 5](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=5>), Table 1 footnote. |
| N006 | Composite core = larger of CT hypodensity and CTP/MRI core. Mismatch definitions: ratio **>=1.8** and volume **>=15 mL**; ratio **>=1.2** and volume **>=10 mL**. Discordance definitions use ASPECTS <6/core <70 mL or ASPECTS >=6/core >=70 mL; ASPECTS <6/core >=70 mL is concordant. | Definitions used in strata/figures/tables. | [PDF p. 3](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3>), Imaging Evaluation. |
| S001 | Primary/treatment-strata ordinal mRS analyses use probabilistic index models (PIMs), reporting aGenOR and 95% CI. Secondary treatment outcomes use modified Poisson regression with robust SE; heterogeneity uses a treatment-by-characteristic interaction. | ITT treatment-effect analyses. | [PDF p. 4](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>), Statistical Analysis. |
| S002 | Within-treatment-group associations use similar models; g-computation estimates generalized odds as functions of core, ASPECTS, and mismatch volume with bootstrapped CIs. Two-sided tests, P<.05 significance; exploratory/no multiple-comparison adjustment; STATA release 17 and R 4.2.2. | As-treated association models; stated testing convention. | [PDF p. 4](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>), Statistical Analysis. |

## Aggregate results and baseline Table 1 (intention-to-treat)

| ID | Relationship and exact printed values | Population/scale | Direct source location |
|---|---|---|---|
| N007 | Median age **67 years (IQR 58.5-75)**; **139/336 (41.4%)** female. | Included exploratory population. | [PDF p. 4](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>). |
| N008 | Noncontrast CT and CT/MR perfusion were within **60 min** for **308/336 (92%)**; interval median **6 min (IQR 2-13)**. Follow-up imaging: MRI **8/336 (2%)**, CT **328/336 (98%)**. | Included population. | [PDF p. 4](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>). |
| N009 | Overall median ASPECTS **4 (IQR 3-5)**; CT hypodensity **86 mL (49-114)**; CTP/MR diffusion core **73 mL (46-107)**; composite core **101 mL (72-138)**. | Included population, baseline imaging. | [PDF p. 4](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>). |
| S003 | CT hypodensity exceeded CTP/MRI core in **203/336 (60%)**. Last-known-well-to-randomization median was **727 min (IQR 422-1004)** when CT hypodensity was larger versus **372 min (251-664)** when CTP/MRI core was larger; **P<.001**. | Post hoc comparison. | [PDF p. 4](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>). |
| N010 | At randomization 0-3 h, **81%** had larger CTP/MRI core; at 21-24 h, **14%** had larger CTP/MRI core. | Timing strata, eFigure 4 cited. | [PDF p. 4](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>). |
| N011 | Table 1 demographics: EVT/MM age **66 (59-75)/67 (58-75)**; female **68/168 (40.5%)/71/168 (42.3%)**; male **100 (59.5)/97 (57.7)**. Race/ethnicity, EVT/MM: Asian **5 (3.0)/3 (1.8)**; Black **24 (14.3)/24 (14.3)**; Native Hawaiian/Pacific Islander **2 (1.2)/0**; White **124 (73.8)/125 (74.4)**; other/unknown **13 (7.8)/16 (9.5)**. | ITT, n=168 each. | [PDF p. 5](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=5>), Table 1. |
| N012 | Table 1 clinical variables, EVT/MM: transferred **97 (57.7)/103 (61.3)**; hypertension **131 (78.0)/121 (72.0)**; diabetes **50 (29.8)/54 (32.1)**; atrial fibrillation **44 (26.2)/38 (22.6)**; coronary artery disease **39 (23.5)/25 (15.4)**; congestive heart failure **19 (11.3)/19 (11.3)**; ischemic stroke **18 (10.7)/13 (7.7)**; TIA **4 (2.4)/8 (4.8)**; left hemisphere **76 (45.2)/71 (42.3)**; NIHSS **19 (15-23)/19 (15-22)**. | ITT, n=168 each. | [PDF p. 5](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=5>), Table 1. |
| N013 | Table 1 imaging, EVT/MM: ICA **75 (44.6)/64 (38.1)**, MCA M1 **86 (51.2)/96 (57.1)**, MCA M2 **7 (4.2)/8 (4.8)**; tandem occlusion **54 (32.1)/43 (25.6)**; ASPECTS **4 (3-5)/4 (4-5)**; composite core **103 (70-139)/99 (74-137) mL**; CTP used **165 (98.2)/163 (97.0)** and MR DWI **3 (1.8)/5 (3.0)**. | ITT, n=168 each. | [PDF p. 5](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=5>), Table 1. |
| N014 | Table 1 remaining imaging/time/treatment, EVT/MM: CTP/MRI core **70 (40-110)/77 (48-104) mL**; CT hypodensity **84 (46-114)/87 (49-113) mL**; Tmax>6 s **161 (117-206)/166 (119-213) mL**; last-known-well-to-randomization **545 (307-919)/596 (347-934) min**; arrival-to-CT **16 (9-27)/16 (7-24) min**; arrival-to-CTP **26 (18-42)/25 (13-36) min**; thrombolytic **33 (19.6)/28 (16.8)**; tenecteplase **4 (12.5)/1 (3.7)**; general anesthesia **100 (59.9)/not applicable**. | ITT, n=168 each. | [PDF p. 5](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=5>), Table 1. |

## EVT versus medical management: 90-day ordinal mRS (Figure 1, ITT)

**Model/contrast:** aGenOR (95% CI), EVT versus MM; adjusted for age, presentation NIHSS, last-known-well-to-randomization, and core volume, except that core volume is omitted for core-volume strata. `aGenOR >1` means better 90-day mRS outcome with EVT. The Table/Figure strata total 336 participants within each stratification.

| ID | Stratum: n; EVT median (IQR) vs MM median (IQR); aGenOR (95% CI); interaction P | Direct source location |
|---|---|---|
| S004 | ASPECTS 0-2: **19; 6 (5-6) vs 6 (5-6); 1.52 (0.94-2.46)**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1. |
| S005 | ASPECTS 3-5: **277; 4 (3-6) vs 5 (4-6); 1.82 (1.40-2.35); P interaction=.80** across 0-2/3-5/6-10. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1; narrative p.4. |
| S006 | ASPECTS 6-10: **40; 5 (3-6) vs 6 (4-6); 1.55 (0.81-2.98)**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1. |
| S007 | ASPECTS 3: **73; 4 (3-6) vs 6 (4-6); 1.71 (1.04-2.81)**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1. |
| S008 | ASPECTS 4: **88; 4 (3-6) vs 5 (4-6); 2.01 (1.19-3.40)**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1. |
| S009 | ASPECTS 5: **116; 3 (2-6) vs 4 (3-6); 1.85 (1.22-2.79); P interaction=.80** across scores 3/4/5. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1; narrative p.4. |
| S010 | Core <70 mL: **156; 3 (2-6) vs 4 (3-6); 1.78 (1.24-2.56)**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1. |
| S011 | Core >=70 mL: **180; 5 (4-6) vs 6 (4-6); 1.63 (1.23-2.16); P interaction=.92**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1; abstract p.1. |
| S012 | Core <100 mL: **236; 4 (2-6) vs 5 (4-6); 1.91 (1.44-2.55)**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1. |
| S013 | Core >=100 mL: **100; 6 (4-6) vs 6 (5-6); 1.41 (0.99-2.02); P interaction=.29**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1; abstract p.1. |
| S014 | Core <150 mL: **296; 4 (3-6) vs 5 (4-6); 1.82 (1.42-2.34)**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1. |
| S015 | Core >=150 mL: **40; 6 (4-6) vs 6 (5-6); 1.47 (0.84-2.56); P interaction=.29**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1; abstract p.1. |
| S016 | No mismatch, ratio >=1.2/volume >=10 mL: **29; 4 (4-6) vs 5 (4-6); 2.11 (0.97-4.58)**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1. |
| S017 | Mismatch, ratio >=1.2/volume >=10 mL: **307; 4 (3-6) vs 5 (4-6); 1.75 (1.38-2.24); P interaction=.96**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1. |
| S018 | No mismatch, ratio >=1.8/volume >=15 mL: **120; 5 (4-6) vs 6 (4-6); 1.68 (1.17-2.40)**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1. |
| S019 | Mismatch, ratio >=1.8/volume >=15 mL: **216; 4 (2-6) vs 5 (4-6); 1.79 (1.33-2.42); P interaction=.92**. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), Figure 1. |

## Figure 2 and within-group imaging associations (Table 2, as-treated)

| ID | Relationship and exact printed values | Population/model | Direct source location |
|---|---|---|---|
| N015 | Figure 2 mRS 0/1/2/3/4/5/6 percentages: core <100 mL, EVT n=**117**: **2/6/18/22/15/8/30**; MM n=**119**: **2/8/14/23/20/0/34**. | ITT; printed rounded percentages. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Figure 2A. |
| N016 | Figure 2 mRS 0/1/2/3/4/5/6 percentages: core >=100 mL, EVT n=**51**: **2/6/10/20/10/0/53**; MM n=**49**: **2/4/0/16/16/0/61**. | ITT; printed rounded percentages. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Figure 2B. |
| N017 | Table 2 mRS median (IQR): EVT **4 (3-6)**; MM **5 (4-6)**. | As-treated EVT n=170; MM n=166. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Table 2. |
| S020 | mRS distribution per 1-point ASPECTS decrease: EVT aGenOR **0.91 (0.82-1.00)**; MM **0.89 (0.80-0.99)**; interaction **P=.83**. | Table 2; adjusted for age, NIHSS, last-known-well-to-randomization. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Table 2. |
| S021 | mRS distribution per 10-mL core increment: EVT aGenOR **0.92 (0.89-0.95)**; MM **0.95 (0.92-0.98)**; interaction **P=.20**. | Table 2 model. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Table 2; abstract p.1. |
| N018 | mRS 0-2: EVT **34/170 (20.0%)**; MM **12/166 (7.2%)**. | As-treated. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Table 2. |
| S022 | mRS 0-2 per ASPECTS point decrease: EVT aRR **0.94 (0.81-1.09)**; MM **0.81 (0.57-1.14)**; interaction **P=.41**. Per 10-mL core increment: EVT **0.89 (0.84-0.95)**; MM **0.91 (0.80-1.03)**; interaction **P=.58**. | Table 2 model/printed aRR label. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Table 2. |
| N019 | mRS 0-3: EVT **66/170 (38.8%)**; MM **30/166 (18.1%)**. | As-treated. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Table 2. |
| S023 | mRS 0-3 per ASPECTS point decrease: EVT aRR **1.00 (0.90-1.12)**; MM **0.92 (0.72-1.19)**; interaction **P=.73**. Per 10-mL core increment: EVT **0.91 (0.87-0.95)**; MM **0.91 (0.85-0.98)**; interaction **P=.25**. | Table 2 model/printed aRR label. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Table 2. |
| N020 | mRS 5-6: EVT **77/170 (45.3%)**; MM **101/166 (60.8%)**. | As-treated. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Table 2. |
| S024 | mRS 5-6 per ASPECTS point decrease: EVT aRR **1.04 (0.93-1.15)**; MM **1.03 (0.95-1.11)**; interaction **P=.86**. Per 10-mL core increment: EVT **1.05 (1.02-1.08)**; MM **1.03 (1.01-1.05)**; interaction **P=.37**. | Table 2 model/printed aRR label. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Table 2. |
| S025 | In EVT, unadjusted-for-volume ASPECTS association aGenOR **0.91 (0.82-1.00)** per decrease; after adding CTP/MRI core, aGenOR **0.96 (0.86-1.07)**. Narrative describes core increment effects: mRS aGenOR **0.92 (0.89-0.95)**; mRS 0-2 aRR **0.89 (0.84-0.95)**; mRS 0-3 aRR **0.91 (0.87-0.95)**; mRS 5-6 aRR **1.05 (1.02-1.08)** per 10 mL. | EVT associations; eFigure 14 and Table 2 cited. | [PDF p. 6](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>). |

## Mismatch and post hoc imaging relationships

| ID | Relationship and exact printed values | Population/model | Direct source location |
|---|---|---|---|
| N021 | Using CTP/MRI core, no mismatch: **29/336 (8.6%)** for ratio >=1.2/volume >=10 mL and **120/336 (35.7%)** for ratio >=1.8/volume >=15 mL. | Included population. | [PDF p. 7](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), narrative. |
| S026 | Time-to-randomization vs mismatch: P for trend **.71** (ratio >=1.2/volume >=10); absence of mismatch decreased with time under ratio >=1.8/volume >=15 (**P<.001**); no-mismatch proportion increased with core for both definitions (**P<.001** for each trend). | eFigures 5-6 cited; direction as printed. | [PDF p. 8](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8>). |
| N022 | Composite-core post hoc mismatch: **262/336 (78.0%)** with mismatch at ratio >=1.2/volume >=10, and **125/336 (37.2%)** at ratio >=1.8/volume >=15. Text also states mismatch proportion changes from **91%** (CTP definition) to **78%** (composite definition). | Post hoc, eTable 7 cited. | [PDF p. 8](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8>); [PDF p. 11](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=11>). |
| N023 | Figure 3 displays modeled probabilities (with 95% CI axes) for mRS 0-2, 0-3, and 5-6 over core 0-300 mL, plus aGenOR for >=1-point mRS improvement over core 0-250 mL; no numerical point estimates are printed. | EVT and MM curves; model-derived display. | [PDF p. 8](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8>), Figure 3. |
| N024 | Narrative discussion: core >=100 mL EVT recipients had approximately **80%** mRS 4 or worse and **1 in 5** independent ambulation; no count or exact denominator printed for this prose approximation. | Discussion. | [PDF p. 10](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10>). |

## Table 3: mismatch within treatment groups (as-treated)

**Model:** adjusted for age, NIHSS, last-known-well-to-randomization, and CTP/MRI core; mismatch versus no-mismatch reference within each treatment group. Table 3 prints all values below.

| ID | Exact printed relationship | Direct source location |
|---|---|---|
| N025 | Ratio >=1.2/volume >=10: mRS no-mismatch/mismatch medians, EVT **4 (3.5-6), n=8 / 4 (3-6), n=162**; MM **5 (4-6), n=21 / 5 (4-6), n=145**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| S027 | Same definition, mRS effect: EVT aGenOR **0.84 (0.39 to 1.82)**; MM **0.78 (0.48 to 1.27)**; interaction **P=.88**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| N026 | Same definition, mRS 0-2 no/mismatch: EVT **0/8 / 34/162 (21.0%)**; MM **1/21 (4.8%) / 11/145 (7.6%)**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| S028 | Same definition, mRS 0-2: MM aRR **1.01 (0.21 to 4.92)**, aRD **-0.001 (-0.138 to 0.136)**; EVT effect cell is blank. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| N027 | Same definition, mRS 0-3 no/mismatch: EVT **2/8 (25.0%) / 64/162 (39.5%)**; MM **4/21 (19.0%) / 26/145 (17.9%)**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| S029 | Same definition, mRS 0-3: EVT aRR **1.04 (0.26 to 4.21)**, aRD **0.010 (-0.344 to 0.364)**; MM aRR **0.49 (0.22 to 1.05)**, aRD **-0.139 (-0.289 to 0.012)**; interaction **P=.47**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| N028 | Same definition, mRS 5-6 no/mismatch: EVT **3/8 (37.5%) / 74/162 (45.7%)**; MM **14/21 (66.7%) / 87/145 (60.0%)**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| S030 | Same definition, mRS 5-6: EVT aRR **1.33 (0.52 to 3.44)**, aRD **0.178 (-0.109 to 0.465)**; MM aRR **1.10 (0.78 to 1.56)**, aRD **0.075 (-0.129 to 0.279)**; interaction **P=.65**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| N029 | Ratio >=1.8/volume >=15: mRS no-mismatch/mismatch medians, EVT **5 (4-6), n=59 / 4 (2-6), n=111**; MM **5 (4-6), n=61 / 5 (4-6), n=105**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| S031 | Same definition, mRS effect: EVT aGenOR **0.89 (0.57 to 1.38)**; MM **0.92 (0.63 to 1.32)**; interaction **P=.92**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| N030 | Same definition, mRS 0-2 no/mismatch: EVT **6/59 (10.2%) / 28/111 (25.2%)**; MM **2/61 (3.3%) / 10/105 (9.5%)**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| S032 | Same definition, mRS 0-2: EVT aRR **1.20 (0.44 to 3.28)**, aRD **0.033 (-0.124 to 0.191)**; MM aRR **1.09 (0.26 to 4.57)**, aRD **0.003 (-0.097 to 0.103)**; interaction **P=.75**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| N031 | Same definition, mRS 0-3 no/mismatch: EVT **14/59 (23.7%) / 52/111 (46.8%)**; MM **6/61 (9.8%) / 24/105 (22.9%)**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| S033 | Same definition, mRS 0-3: EVT aRR **1.03 (0.56 to 1.88)**, aRD **0.009 (-0.164 to 0.181)**; MM aRR **0.87 (0.39 to 1.92)**, aRD **-0.032 (-0.155 to 0.090)**; interaction **P=.60**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| N032 | Same definition, mRS 5-6 no/mismatch: EVT **31/59 (52.5%) / 46/111 (41.4%)**; MM **43/61 (70.5%) / 58/105 (55.2%)**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |
| S034 | Same definition, mRS 5-6: EVT aRR **1.18 (0.82 to 1.70)**, aRD **0.092 (-0.071 to 0.255)**; MM aRR **1.05 (0.79 to 1.38)**, aRD **0.037 (-0.117 to 0.191)**; interaction **P>.99**. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3. |

## Follow-up infarct, age/time, and quantitative narrative claims

| ID | Relationship and exact printed values | Population/model | Direct source location |
|---|---|---|---|
| S035 | Follow-up infarct volume: EVT median **170 mL (IQR 123-268)** vs MM **168 mL (110-253)**; **P=.43**. | Post hoc. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>). |
| N033 | MR diffusion follow-up **n=204 (61%)**: infarct growth successful reperfusion **68 mL (37-142)**, MM **95 mL (56-125)**, unsuccessful reperfusion **125 mL (76-179)**. | Post hoc; eTable 11 cited. | [PDF p. 9](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>). |
| N034 | CTP/MRI core >=10 mL larger than follow-up infarct in **3 patients (<1%)**. | eTable 13 cited. | [PDF p. 10](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10>). |
| S036 | Independent ambulation after EVT: per 1-year age aRR **0.97 (0.96-0.99)**; per 10-min imaging-to-reperfusion/end aRR **0.97 (0.93-1.00)**; last-known-well-to-reperfusion/end aRR **1.00 (0.99-1.00)** and described as not significant. | EVT predictive associations; eFigures 18-19 cited. | [PDF p. 10](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10>). |
| N035 | Limitations describe follow-up imaging acquisition at **1-7 days**; MRI pretreatment subgroup was too small to draw conclusions. They also state few patients had core **>150 mL** or no mismatch, without a new numerical count. | Limits on interpretation. | [PDF p. 11](<../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=11>). |

## Mapping limitations

- All 14 assigned PDF pages were directly inspected through a current PDF extraction. Table and figure numeric displays on pp. 5-9 were additionally checked against the direct PDF layout and the existing rendered pages.
- Figure 3 provides axes and graphical curves, but no printed point estimates; this map records its labels, scale, and the absence of point labels rather than estimating values from pixels.
- Several main-text results cite Supplement 5 eFigures/eTables for further values. They are recorded here as cross-source locators only; their numeric contents belong to the disjoint support-source mapping scope.
