# Main Quantitative Evidence Map — DOC-001

## Scope, method, and completeness

- **Direct source:** `jama_sun_2024_oi_240088_1746815064.14747.pdf` (DOC-001), PDF pages 1-11.
- **Assigned units:** all 11 PDF pages. The reusable per-page native/layout files were used as locators; direct PDF text extraction confirmed the source identity, page count, and mapped printed values. The retained renders were also consulted for the spatially formatted Figure 1, Table 1, Figure 2, Table 2, and Figure 3 on PDF pages 5-9. Direct-source PDF locations below use `jama_sun_2024_oi_240088_1746815064.14747.pdf#page=N`.
- **Relationship convention:** `N` records numeric, denominator, population, time, count/rate, scale, and label relationships. `S` records an effect estimate, interval, P value, test/model, or other inferential relationship. A record may cite a narrative occurrence of the same relationship without duplicating its printed values.
- **Coverage result:** all assigned page units were inspected. No candidate diagnosis or adjudication is made in this artifact.

## Page-unit coverage

| PDF page | Result-relevant content mapped | Status |
|---:|---|---|
| 1 | Abstract population, intervention denominators, primary and component outcome results, adverse/procedural rates, dates and eligibility thresholds | MAPPED |
| 2 | Trial setting, eligibility/risk-factor thresholds, allocation and medication regimen | MAPPED |
| 3 | Outcome definitions, score scales, follow-up windows, sample-size assumptions | MAPPED |
| 4 | Analysis population/model/test rules and complete participant-population narrative | MAPPED |
| 5 | Figure 1 flow; primary, secondary, and post-hoc narrative outcome claims | MAPPED |
| 6 | Table 1 baseline data; post-hoc and adverse-event narrative results | MAPPED |
| 7 | Figure 2 subgroup results; procedural event rates and discussion claims | MAPPED |
| 8 | Table 2 outcome data and footnotes | MAPPED |
| 9 | Figure 3 time-to-event/landmark estimates and matching discussion claims | MAPPED |
| 10 | Conclusion and narrative matching the primary comparison; no new numeric result table/figure | MAPPED |
| 11 | References only; no applicable trial result, statistic, or quantitative relationship | NO-APPLICABLE-RESULT-UNIT |

## Study population, intervention, outcomes, and analysis definitions

| ID | Exact source location | Reconstructed relationship and printed values |
|---|---|---|
| N001 | PDF p. 1, abstract; PDF p. 4, Patient Population | Randomized population: **512**. Confirmed eligible/primary-analysis population: **501**, balloon angioplasty plus aggressive medical management (BA) **249** and aggressive medical management (AMM) **252**. |
| N002 | PDF p. 1, abstract | Randomized open-label, blinded-end-point trial at **31** centers in China; recruitment November 8, 2018-April 2, 2022; final follow-up April 3, 2023. |
| N003 | PDF pp. 1-2 | Eligibility/time/population definition: age **35-80 y**; recent TIA **<90 d** or ischemic stroke **14-90 d** before enrollment; qualifying major-artery atherosclerotic stenosis **70%-99%**. |
| N004 | PDF pp. 1-3 | BA and AMM both received aggressive medical management. BA procedure was recommended within **3 business days**; submaximal balloon inflation diameter was **50%-70%** of proximal artery diameter. Aspirin **100 mg daily** was for follow-up and clopidogrel **75 mg daily** for first **90 d**; platelet aggregation rate **>40%** or CYP2C19 loss-of-function allele defined clopidogrel resistance. |
| N005 | PDF p. 3 | Follow-up schedule: baseline, angiography day, discharge, **30 ± 7 d**, **90 ± 7 d**, **6 mo ± 14 d**, **1 y ± 30 d**, then 6-month intervals through 3 y; reported analysis is the **1-y** result. |
| N006 | PDF p. 3 | Primary composite: any stroke or death within **30 d** after enrollment/procedure, or qualifying-territory ischemic stroke or qualifying-artery revascularization after **30 d through 12 mo/1 y**. Revascularization timing and criteria are printed there. |
| N007 | PDF p. 3 | Secondary-outcome definitions include 30-d, 90-d, 1-y, 24-mo, and 36-mo windows; mRS scale **0-6** (higher = greater disability); EuroQol-5-Dimensions score **0-100** (0 worst, 100 best); restenosis is stenosis **>70%** or increase **30%**. Outcomes at 24/36 months are explicitly not reported. |
| N008 | PDF pp. 3-4 | Original sample-size plan: **802** (**401/group**) assuming AMM composite rate **12%**, BA relative-risk reduction **50%**, and one interim analysis. Updated assumptions were AMM **15%** and BA **7%**; revised target **512** (**256/group**), power **80%**, two-sided type-I error **.05**, attrition **10%**, and no interim analysis. |
| S001 | PDF p. 4, Statistical Analysis | Primary analysis population is eligible participants who received treatment, analyzed by randomization group; primary 1-y composite compared with Kaplan-Meier/log-rank; HR and **95% CI** from Cox proportional-hazards model; center effect not adjusted in main analysis. |
| S002 | PDF p. 4 | Schoenfeld residual proportional-hazards test: **P = .12**. Survival curves crossed at **30 d**, motivating post-hoc landmark analysis and separate component reporting. |
| S003 | PDF p. 4 | mRS 90-d and 12-mo shift planned with ordinal logistic regression, but proportional-odds assumption not met; authors switched to assumption-free ordinal analysis and calculate a generalized OR using Wilcoxon-Mann-Whitney. Two-sided tests use **P < .05**; no multiplicity correction for secondary outcomes; CIs are **95%** and not adjusted for multiplicity. |

## Participant flow and population characteristics

| ID | Exact source location | Reconstructed relationship and printed values |
|---|---|---|
| N009 | PDF p. 4, Patient Population; PDF p. 5, Figure 1 | **1409** assessed; **897** excluded; **512** randomized. Exclusions in Figure 1: no consent **326**; severe stenosis outside target vessel **238**; qualifying event ≤2 weeks **89**; angiographic stenosis <70% **73**; target-artery occlusion **46**; antiplatelet intolerance/active bleeding diathesis **43**; contrast allergy **35**; aneurysm/vascular malformation **24**; enrolled elsewhere **23**. |
| N010 | PDF pp. 4-5 | Randomized allocations: BA **256**, AMM **256**. Pre-primary-analysis removals: BA consent withdrawal **7** leaving **249**; AMM consent withdrawal **3** plus erroneous randomization number **1** leaving **252**. Thus **11** consent/administrative exclusions yield **501** primary-analysis participants. |
| N011 | PDF p. 5, Figure 1 | Post-adjudication/per-protocol flow: BA **16** excluded (crossed to AMM **7**; ischemic stroke onset ≤2 wk **4**; tandem lesion **2**; lesion length >15 mm **1**; balloon-expanding stent first **1**; target-artery occlusion **1**) leaving **233**. AMM **14** excluded (crossed to BA **5**; stroke ≤2 wk **2**; tandem lesion **1**; lesion >15 mm **2**; stenosis <70% **2**; target-artery occlusion **1**; aneurysm **1**) leaving **238**. |
| N012 | PDF p. 4 | Lead center accounts for **258/501 (51.5%)**. Overall median (IQR) age **58.0 (52.0-65.0) y**; male **343 (69.1%)**; Han Chinese **494 (98.6%)**. |
| N013 | PDF p. 4; PDF p. 6, Table 1 | Overall qualifying event: TIA **78 (15.6%)**, ischemic stroke **423 (84.4%)**. Among the 423 strokes: artery-to-artery embolism **135 (31.9%)**, isolated border-zone infarct **69 (16.3%)**, perforator **42 (9.9%)**, mixed **177 (41.8%)**. Mixed-mechanism patients with border-zone infarct **100**; total border-zone infarct **169 (40.0%)**, AMM **40.9%**, BA **39.1%**. |
| N014 | PDF p. 4; PDF p. 6, Table 1 | Time since last TIA/stroke to randomization, median (IQR): BA **34 (21-53) d**, AMM **32 (22-51) d**. BA procedure timing median (IQR) **2 (1-2) d** after enrollment/randomization. |
| N015 | PDF p. 4; PDF p. 6, Table 1 | Overall stenosis categories: 60%-69% **2 (0.4%)**; 70%-79% **289 (57.6%)**; 80%-89% **163 (32.5%)**; 90%-99% **45 (9.0%)**; 100% **2 (0.4%)**. |

## Table 1: baseline group data

**Location:** PDF p. 6, Table 1. All entries are BA **n=249** versus AMM **n=252**; percentages are group percentages, except unlabelled zero counts. The narrative population statements on PDF p. 4 are matched in N012-N015.

| ID | Variable/scale | BA | AMM |
|---|---|---:|---:|
| N016 | Age, median (IQR), y | 58.0 (52.0-65.0) | 58.0 (52.0-65.0) |
| N017 | Male; female, No. (%) | 172 (69.1); 77 (30.1) | 171 (67.9); 81 (32.1) |
| N018 | Hypertension; hyperlipidemia; diabetes, No. (%) | 181 (72.7); 176 (70.7); 82 (32.9) | 185 (73.4); 191 (75.8); 87 (34.5) |
| N019 | Antiplatelet before latest qualifying event; statin before latest event; current smoking, No. (%) | 118 (47.4); 123 (49.4); 60 (24.1) | 113 (44.8); 126 (50.0); 66 (26.2) |
| N020 | Qualifying event: TIA; ischemic stroke, No. (%) | 34 (13.7); 215 (86.4) | 44 (17.5); 208 (82.5) |
| N021 | Stroke mechanism, No. (% of ischemic-stroke group): artery-to-artery embolism; isolated border-zone; perforator; mixed | 78 (36.3); 37 (17.2); 18 (8.4); 82 (38.1) | 57 (27.4); 32 (15.4); 24 (12); 95 (45.7) |
| N022 | Qualifying artery, No. (%): middle cerebral; basilar; internal carotid; vertebral | 143 (57.4); 73 (29.3); 21 (8.4); 12 (4.8) | 154 (61.1); 73 (29.0); 8 (3.2); 17 (6.8) |
| N023 | mRS 0-1 at admission, No. (%); NIHSS median (IQR), scale 0-42 | 227 (91.2); 0 (0-2) | 231 (91.7); 0 (0-2) |
| N024 | NIHSS 0-1; 2-4; 5-10, No. (%) | 186 (74.7); 51 (20.5); 12 (4.8) | 187 (74.2); 51 (20.5); 14 (5.6) |
| N025 | Symptomatic-artery stenosis 60%-69%; 70%-79%; 80%-89%; 90%-99%; 100%, No. (%) | 0; 140 (56.2); 83 (33.3); 25 (10.4); 1 (0.4) | 2 (0.8); 149 (59.1); 80 (31.7); 20 (7.9); 1 (0.4) |
| N026 | Time last event to randomization, median (IQR), d: all; TIA; stroke | 34.0 (21.0-53.0); 33.0 (21.0-56.0); 34.0 (20.0-51.0) | 32.0 (22.0-51.0); 33.0 (19.0-47.0); 32.0 (22.0-51.0) |

Table 1 footnotes specify mRS **0-6** (higher disability), NIHSS **0-42** (higher neurologic deficit), and WASID-method stenosis assessment; they supply the scale/label context for N023-N025.

## Primary and secondary outcome results

### Main primary result and matching narrative occurrences

| ID | Exact source locations | Reconstructed relationship |
|---|---|---|
| N027 | PDF p. 5, Primary Outcome; PDF p. 8, Table 2; PDF p. 9, Figure 3 | Primary time-to-first-event composite: BA **11/249 (4.4%)**, AMM **34/252 (13.5%)**; incidence difference **−9.1% (95% CI, −14.0 to −4.1)**. |
| S004 | PDF p. 1 abstract; PDF p. 5; PDF p. 8 Table 2; PDF p. 9 Figure 3; PDF p. 10 Conclusions | Matched primary contrast (BA vs AMM): **HR 0.32 (95% CI, 0.16-0.63), P < .001** (Table 2/figure use “to”; abstract uses hyphen). Table footnote identifies P as a log-rank-test P for a time-to-event composite; Cox model is defined in S001. Abstract and conclusion state BA lowered the composite risk. |
| N028 | PDF p. 8, Table 2 footnote b | Components do not sum to the primary-composite total because BA **1** and AMM **10** participants had multiple events; first event only is used for the composite, but individual components are separately counted. |

### Table 2 outcome inventory

**Location:** PDF p. 8, Table 2. Unless stated otherwise, values are BA **n=249** versus AMM **n=252**, the specified time window, count (percentage), incidence difference with **95% CI**, then HR with **95% CI** and P. “NA” is printed where not applicable. Superscript **a** identifies a post-hoc analysis.

| ID | Outcome/time/measure | BA | AMM | Difference (95% CI) | Effect statistic/P |
|---|---|---:|---:|---|---|
| S005 | Any stroke or all-cause death within 30 d (component; also listed as secondary) | 8 (3.2%) | 4 (1.6%) | 1.6% (−1.1 to 4.3) | HR 2.05 (0.62-6.81); P=.24 |
| S006 | Qualifying-artery ischemic stroke beyond 30 d-1 y, post hoc | 1 (0.4%) | 19 (7.5%) | −7.1% (−10.5 to −3.8) | HR 0.05 (0.01-0.39); no P printed in row |
| S007 | Qualifying-artery revascularization beyond 30 d-1 y, post hoc | 3 (1.2%) | 21 (8.3%) | −7.1% (−10.8 to −3.5) | HR 0.14 (0.04-0.47); no P printed in row |
| S008 | Stroke in qualifying-artery territory or all-cause death within 90 d | 7 (2.8%) | 10 (4.0%) | −1.2% (−4.3 to 2.0) | HR 0.72 (0.27-1.88); P=.49 |
| S009 | Stroke outside qualifying-artery territory within 90 d | 2 (0.8%) | 0 | 0.8% (−0.3 to 1.9) | HR NA; P=.15 |
| S010 | mRS at 90 d, median (IQR), scale 0-6 | 0 (0-0) | 0 (0-1) | NA | generalized OR 1.21 (1.03-1.38); P=.01 |
| S011 | Stroke in qualifying-artery territory or all-cause death within 1 y | 8 (3.2%) | 23 (9.1%) | −5.9% (−10.1 to −1.7) | HR 0.35 (0.16-0.78); P=.01 |
| S012 | Qualifying-artery revascularization within 1 y | 4 (1.6%) | 24 (9.5%) | −7.9% (−11.9 to −4.0) | HR 0.16 (0.06-0.47); P<.001 |
| S013 | Stroke outside qualifying-artery territory within 1 y | 3 (1.2%) | 4 (1.6%) | −0.4% (−2.4 to −1.7) | HR 0.76 (0.17-3.40); P=.72 |
| S014 | mRS at 1 y, median (IQR), scale 0-6 | 0 (0-0) | 0 (0-1) | NA | generalized OR 1.26 (1.06-1.45); P=.01 |
| S015 | Combined vascular events within 1 y | 10 (4.0%) | 26 (10.3%) | −6.3% (−10.8 to −1.8) | HR 0.38 (0.19-0.80); P=.01 |
| N029 | Table 2, combined-event components | Stroke: BA **9 (3.6%)**, AMM **26 (10.3%)**, difference **−6.7% (−11.1 to −2.3)**. Myocardial infarction: **0/0**, NA. Vascular death: BA **1 (0.4%)**, AMM **0**, difference **0.4% (−0.4 to 1.2)**. |
| N030 | Table 2 | EuroQol-5-Dimensions at 1 y, median (IQR): BA **100 (100-100)**, AMM **100 (100-100)**; P=.40; no incidence-difference or HR field is printed. |
| N031 | Table 2 footnotes c-d, g | Revascularization may be acute qualifying-artery occlusion with deficit needing specified intervention, or symptom-driven elective revascularization. For the 30-d event outcome: any stroke BA **7/249 (2.8%)**, AMM **4/252 (1.6%)**; death BA **1/249 (0.4%)**, AMM **0%**. Death within 1 y BA **1/249 (0.4%)**, AMM **1/252 (0.4%)**. |
| N032 | Table 2 footnote f | The 90-d and 1-y mRS estimates are generalized ORs; values **>1** mean a more favorable mRS shift toward better outcomes for BA than AMM. |

### Narrative result claims matched to Table 2/primary evidence

| ID | Exact source location | Relationship (including matching source-table/figure occurrence) |
|---|---|---|
| N033 | PDF p. 1 abstract; PDF p. 5, Secondary Outcomes; PDF p. 8 Table 2 | 30-d stroke/all-cause death: BA **3.2%**, AMM **1.6%**; exact row and inferential result are S005. |
| N034 | PDF p. 1 abstract; PDF p. 5; PDF p. 8 Table 2 | Beyond 30 d-1 y qualifying-territory ischemic stroke: BA **0.4%**, AMM **7.5%**; revascularization: BA **1.2%**, AMM **8.3%**. These match S006/S007. |
| S016 | PDF p. 5, Secondary Outcomes; PDF p. 8 Table 2 | Narrative repeats Table 2: qualifying-territory stroke/all-cause death at 1 y **3.2% vs 9.1%; HR 0.35 (0.16-0.78); P=.01**; revascularization **1.6% vs 9.5%; HR 0.16 (0.06-0.47); P<.001**; combined events **4.0% vs 10.3%; HR 0.38 (0.19-0.80); P=.01**; mRS generalized OR **1.21 (1.03-1.38), P=.01** at 90 d and **1.26 (1.06-1.45), P=.01** at 1 y. |
| N035 | PDF p. 5, Secondary Outcomes | BA qualifying-artery restenosis within 1 y **15.7%**; TIA or stroke clearly related to restenosis **2.0%** (eTable 4 is the cited support location). |
| S017 | PDF p. 6, Post Hoc Outcomes; Table 2/Figure 3 | Narrative repeats post-hoc components: qualifying-territory stroke beyond 30 d-1 y **0.4% vs 7.5%** and revascularization **1.2% vs 8.3%**, BA lower. Center-adjusted primary result: **HR 0.32 (95% CI, 0.16-0.62), P=.001**; center-by-treatment interaction **P=.10**. Removing revascularization: BA **3.6%**, AMM **9.1%; HR 0.39 (0.18-0.85), P=.01**. |

## Adverse events and procedural outcomes

| ID | Exact source locations | Reconstructed relationship |
|---|---|---|
| N036 | PDF p. 1 abstract; PDF p. 6, Procedural Complications and Adverse Events | sICH: BA **1.2%**, AMM **0.4%**. Asymptomatic intracranial hemorrhage: BA **1.2%**, AMM **0%**. |
| S018 | PDF p. 6 | Disabling stroke: BA **2.4%**, AMM **7.1%; P=.02** (eTable 11 cited). |
| N037 | PDF p. 7 | Within 30 d, all-cause death occurred in BA **1** patient due to sICH. Beyond 30 d-1 y, AMM **1** death was due to motor-vehicle crash. |
| N038 | PDF p. 7 | BA procedural-complication rates: vasospasm **1.2%**; arterial dissection **14.5%**; pseudoaneurysm **0.0%**; arterial occlusion **0.4%**; arterial perforation **0.4%**; arterial rupture **0.0%**; hemorrhage **0.4%**; thrombosis **1.7%**. Abstract gives any procedural complication **17.4%** and dissection **14.5%**. |
| N039 | PDF p. 9, Discussion | In BA, **71.4%** of participants with arterial dissection underwent rescue stenting. |

## Figure 2: primary-outcome subgroup results

**Location:** PDF p. 7, Figure 2. This figure repeats the overall primary outcome from N027/S004 and reports count/total (percentage) plus HR (95% CI). The final column is a P value for interaction at the subgroup-pair level, not a per-subgroup outcome P value. Hypoperfusion was assessed by CT perfusion. For hypoperfusion “No,” AMM had no events and HR is printed **NA**.

| ID | Subgroup (BA vs AMM) | BA | AMM | HR (95% CI) | P interaction |
|---|---|---:|---:|---|---:|
| S019 | Overall | 11/249 (4.4%) | 34/252 (13.5%) | 0.32 (0.16-0.63) | — |
| S020 | Age <65; ≥65 y | 9/176 (5.1%); 2/73 (2.7%) | 23/187 (12.3%); 11/65 (16.9%) | 0.41 (0.19-0.88); 0.16 (0.03-0.70) | .26 |
| S021 | Male; female | 5/172 (2.9%); 6/77 (7.8%) | 19/171 (11.1%); 15/81 (18.5%) | 0.26 (0.10-0.68); 0.41 (0.16-1.05) | .50 |
| S022 | Hypertension yes; no | 9/181 (5.0%); 2/68 (2.9%) | 25/185 (13.5%); 9/67 (13.4%) | 0.36 (0.17-0.77); 0.21 (0.05-0.96) | .53 |
| S023 | Diabetes yes; no | 4/82 (4.9%); 7/167 (4.2%) | 13/87 (14.9%); 21/165 (12.7%) | 0.32 (0.10-0.97); 0.32 (0.14-0.76) | .99 |
| S024 | Smoking yes; no | 1/60 (1.7%); 10/189 (5.3%) | 7/66 (10.6%); 27/186 (14.5%) | 0.15 (0.02-1.24); 0.35 (0.17-0.73) | .46 |
| S025 | eGFR <60; ≥60 mL/min/1.73 m² | 5/88 (5.7%); 6/161 (3.7%) | 16/96 (16.7%); 18/156 (11.5%) | 0.33 (0.12-0.89); 0.32 (0.13-0.80) | .95 |
| S026 | Target-vessel stenosis <80%; ≥80% | 5/140 (3.6%); 6/109 (5.5%) | 15/151 (9.9%); 19/101 (18.8%) | 0.35 (0.13-0.97); 0.28 (0.11-0.71) | .74 |
| S027 | BMI <25; ≥25 | 3/110 (2.7%); 8/139 (5.8%) | 17/110 (15.5%); 17/142 (12.0%) | 0.17 (0.05-0.57); 0.48 (0.21-1.11) | .17 |
| S028 | Hypoperfusion yes; no | 4/103 (3.9%); 1/19 (5.3%) | 16/106 (15.1%); 0/21 | 0.25 (0.08-0.75); NA | .99 |
| S029 | Anterior; posterior circulation | 9/164 (5.5%); 2/85 (2.4%) | 21/162 (13.0%); 13/90 (14.4%) | 0.42 (0.19-0.91); 0.16 (0.04-0.69) | .26 |
| S030 | TIA; ischemic stroke | 1/34 (2.9%); 10/215 (4.7%) | 6/44 (13.6%); 28/208 (13.5%) | 0.21 (0.03-1.75); 0.34 (0.16-0.69) | .67 |

## Figure 3 and later narrative comparison claims

| ID | Exact source locations | Reconstructed relationship |
|---|---|---|
| S031 | PDF p. 9, Figure 3; PDF p. 4 | Main Kaplan-Meier primary estimate repeats **HR 0.32 (95% CI, 0.16-0.63), P<.001**. Numbers at risk at days 0, 60, 120, 180, 240, 300, 365: BA **249, 241, 240, 240, 240, 239, 238**; AMM **252, 236, 232, 228, 226, 222, 218**. |
| S032 | PDF p. 9, Figure 3 footnote; PDF p. 4 | Curves crossed at **30 d** (dashed line); post-hoc landmark estimates are early **HR 2.05 (95% CI, 0.62-6.81)** and after landmark **HR 0.10 (95% CI, 0.03-0.31)**. |
| N040 | PDF p. 9, Discussion | Narrative cross-trial/context values: median (IQR) onset-to-enrollment in BASIS **34 (20-51) d** versus SAMMPRIS **7 (4-16)**, VISSIT **9 (0-42)**, CASSISS **38 (27-75)**; experimental-group ischemic-stroke proportion BASIS **86%**, SAMMPRIS **63%**, VISSIT **62%**, CASSISS **51%**; border-zone infarct BA **39%**, SAMMPRIS **37%**, CASSISS **20%**; AMM border-zone infarct BASIS **40.9%**, CASSISS **21.0%**; AMM 1-y event rate BASIS **9.1%**, CASSISS **7.2%**; AMM hard-TIA revascularization **10/21 (47.6%)**. These are contextual comparisons rather than new primary-analysis estimates. |
| N041 | PDF p. 10, Conclusions; PDF p. 1 abstract | The conclusion repeats the direction/definition of the primary composite through 12 months and the interpretation that BA plus AMM statistically significantly lowered its risk versus AMM alone; no new number is printed on PDF p. 10. |

## Mapper notes for downstream relationship checks

1. The same primary-composite result occurs in abstract, narrative, Table 2, Figure 2 overall, Figure 3, and conclusion (N027/S004/S019/S031/N041). Table 2 explicitly explains why individual component counts do not add to composite event counts (N028).
2. Several component estimates are explicitly marked post hoc in Table 2 (S006/S007); Figure 3 landmark estimates are also post hoc. Maintain their stated time windows and model labels when comparing them.
3. Table 2 calls its point estimate column **“HR ratio (95% CI)”** but uses HR values; mRS rows are footnoted as generalized ORs rather than HRs (S010/S014/N032). This is an exact printed label/scale relationship for later checking, not a candidate assessment.
4. No person-time quantity, standard error, test statistic beyond the stated Schoenfeld P, or displayed display-zero P value is present in DOC-001.

## Counts and limitations

- **Numeric/reporting relationships mapped:** N001-N041 (**41**).
- **Inferential-statistical relationships mapped:** S001-S032 (**32**).
- **Total mapped relationships:** **73** (including explicitly matched narrative/table/figure occurrences; repeated values are cross-referenced rather than counted as separate source units).
- **No-applicable unit:** PDF p. 11 (references only).
- **Limitations:** DOC-001 provides no raw data, person-time totals, standard errors, or supplemental eTable values. Those supporting-source locations are deliberately left to the separately assigned support mapper. Native/layout extraction preserved the table and figure values sufficiently; existing rendered page complements were used for pages 5-9. Direct source PDF remains the authority.
