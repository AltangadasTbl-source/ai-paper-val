# Main article complete quantitative evidence map

Owner: /root/main_mapper; fresh qc162_main_quantitative_mapper, gpt-6.1-sol / medium. Scope: DOC-001, REPORT, jama_aminian_2019_oi_190103.pdf, PDF pages 1–12, printed pages 1271–1282. All 12 units mapped; 12 reusable-backed, 0 fresh-required. This artifact records evidence and matching relationships without candidate judgments. Local M identifiers are mapper records; the numeric and statistical checkers assign package-wide N/S identifiers.

Method: read every reusable page-native text from `.ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-NNN.txt`; these were verified against every direct source page by the asset curator. Visually inspected reusable source render of PDF p7 to preserve Table 2 alignment and all printed values. Direct p7 text confirmation: `pdftotext -layout -f 7 -l 7 jama_aminian_2019_oi_190103.pdf .ai_paper_validation/review_1_6_2/preprocessing/main-mapper-page-007-layout.txt`; Poppler 26.01.0, CPU. No OCR or fallback was needed. Reused assets unchanged. Exact links below are relative to this extraction directory.

## Population, flow, design and inferential context

| Record | Source | Relationship, population, definitions and printed values |
|---|---|---|
| M001 | [p1 abstract](../../../jama_aminian_2019_oi_190103.pdf#page=1) | Retrospective matched cohort, Cleveland Clinic Health System; adults with type 2 diabetes and obesity; base 287438 in 1998–2017; surgery 2287; matching 1:5; controls 11435; total 13722; follow-up through December 2018. Exposure metabolic gastrointestinal surgery vs usual care. BMI ≥30. |
| M002 | [p2 Methods](../../../jama_aminian_2019_oi_190103.pdf#page=2) | EHR through December 31, 2018; base cohort diagnosis dates January 1, 1998–December 31, 2017, n287438. Surgery index date first metabolic surgery; controls receive a single randomly sampled date from surgery index-date distribution. Ohio/Florida centers. No random assignment of exposure. |
| M003 | [p2 eligibility](../../../jama_aminian_2019_oi_190103.pdf#page=2) | Inclusion age18–80, BMI≥30 kg/m², HbA1c≥6.5% or ≥1 diabetes medication. Surgery exclusions: solid-organ transplant; ejection fraction<20% any time before index; active cancer; GI cancer within1y; ED admission within5d; gastroesophageal cancer or peptic-ulcer diagnoses/procedures during surgical hospitalization. Controls exclude first diabetes diagnosis after assigned date, last follow-up on/before date, already dead or death≤30d afterward, and failure of surgical criteria1–8. |
| M004 | [p3 Figure1](../../../jama_aminian_2019_oi_190103.pdf#page=3) | Base287438 splits2818 surgery-coded/284620 nonsurgical; 61 surgery-coded excluded on chart review leaving2757; surgery enrollment exclusion470 leaves2287. Nonsurgical195677 excluded =116031 diabetes after assigned date +79646 no subsequent follow-up, leaves88943. Enrollment exclusion49676 leaves39267; unmatched27832 leaves11435. Matched ratio1:5. |
| M005 | [p3 Figure1 surgery exclusions](../../../jama_aminian_2019_oi_190103.pdf#page=3) | Overlapping reasons explicitly allowed: no documented diabetes240; BMI133; cancer99; ED≤5d29; age24; transplant19; EF<20%13. Footnote diabetes exclusion HbA1c<6.5% and no medication at index. |
| M006 | [p3 Figure1 control exclusions](../../../jama_aminian_2019_oi_190103.pdf#page=3) | Overlapping reasons explicitly allowed: no/missing BMI39821; age12004; no diabetes9888; cancer3291; EF<20%1006; transplant855; ED≤5d537; death≤30d87. Footnote same diabetes rule as M005. |
| M007 | [pp2–3 endpoint](../../../jama_aminian_2019_oi_190103.pdf#page=2) | Primary extended MACE6: all-cause death; coronary events (unstable angina/MI/coronary intervention or surgery); cerebrovascular events (ischemic/hemorrhagic stroke/carotid intervention or surgery); HF; nephropathy; AF. First occurrence after index. Secondary composite3: all-cause death, MI, ischemic stroke. Other secondary endpoints six primary components. Abstract says seven prespecified secondary outcomes. |
| M008 | [p3 risk rules](../../../jama_aminian_2019_oi_190103.pdf#page=3) | No participant excluded from composite assessments; conditions/events present at baseline omitted from composite count during follow-up. Illustrative history of MI means recurrent MI does not count, incident stroke does. For five individual nonmortality outcomes, prior condition eliminates patient only from that outcome's subsequent risk assessment. Death sourced from EHR/Social Security/State Death Indices. |
| M009 | [pp3–4 matching](../../../jama_aminian_2019_oi_190103.pdf#page=4) | Doubly robust propensity-score matching plus outcome regression. Nearest neighbor1:5; logistic logit score with7 a priori confounders: index date, age, sex, BMI category30–34.9/35–39.9/≥40, Ohio/Florida, insulin, diabetes end-organ complications. All Table1 baseline variables included in fully adjusted Cox models for all8 outcomes. |
| M010 | [p4 survival methods](../../../jama_aminian_2019_oi_190103.pdf#page=4) | Cause-specific event rates per100 patient-years from index; 8y cumulative incidence Kaplan–Meier; ARD8y and percentile95%CI from1000 bootstrap iterations. PH treatment assumption by weighted residuals Grambsch–Therneau. Table2 ARD orientation control−surgery; HR instantaneous risk surgery/control. |
| M011 | [p4 missing data](../../../jama_aminian_2019_oi_190103.pdf#page=4) | Within each outcome dataset, baseline missing values imputed by chained equations into5 datasets; predictive mean matching numeric, logistic binary, polytomous logistic categorical; Rubin formula for imputation-corrected standard errors of estimates/contrasts. Numeric SEs not printed in main article. |
| M012 | [p4 subgroup and longitudinal](../../../jama_aminian_2019_oi_190103.pdf#page=4) | Primary subgroups individually interact variable with treatment in fully adjusted Cox; association P/CI estimated. Four-knot spline×treatment for mean metabolic/nutritional change; two-sample proportions test medication prescriptions at1,2,5,8y. Significance .05 two-sided; CI95%; secondary findings exploratory owing to multiple comparisons; R3.5.0. |
| M013 | [p4 sensitivity](../../../jama_aminian_2019_oi_190103.pdf#page=4) | Random nonsurgical date assignment repeated5 times; matching1:1,1:5,1:10 gives15 datasets; all8 outcomes fully adjusted Cox HR/CI. Time-varying HR at2,5,8y using restricted cubic spline of observed follow-up×treatment in adjusted Cox. E-value assesses unmeasured confounding robustness. |
| M014 | [p4 procedures/BMI](../../../jama_aminian_2019_oi_190103.pdf#page=4) | Surgery2287=RYGB1443[63%]+sleeve730[32%]+band109[5%]+duodenal switch5. BMI≥40:1713[75%];35–39.9:465[20%];30–34.9:109[5%]. Table1 counterpart uses one-decimal percentages. |
| M015 | [p4 follow-up](../../../jama_aminian_2019_oi_190103.pdf#page=4) | Overall median3.9y(IQR1.9–6.1); nonsurgery4.0(2.1–6.1); surgery3.3(1.2–6.3). Abstract overall matches; Figure2 and Figure3 mortality captions give same group values. |
| M016 | [p4 balance narrative](../../../jama_aminian_2019_oi_190103.pdf#page=4) | 37 baseline covariates. Surgery/control medians weight126.5/120.2kg,BMI45.1/42.6,age52.5/54.8y; surgery/control dyslipidemia74/65%,hypertension85/75%,black19/25%,current smoking7/14%,aspirin32/40%. Abstract female65.5/64.2%,age52.5/54.8,BMI45.1/42.6,HbA1c7.1/7.1%. Matching Table1 rows retained below. |

## Table 1 complete display

[PDF p5](../../../jama_aminian_2019_oi_190103.pdf#page=5), continued [PDF p6](../../../jama_aminian_2019_oi_190103.pdf#page=6). Columns surgery n2287 / unmatched nonsurgical n39267 / standardized difference before / matched nonsurgical n11435 / standardized difference after. Counts are No.(%); continuous values median(IQR). Signed differences preserved exactly. Rows M017–M080 are enumerated in display order below; every row has five printed comparison columns. The layout transcription follows after the row inventory and is part of this map, including every printed count, IQR and standardized difference.

M017 index date; M018 women; M019 men; M020 age; M021 BMI; M022 BMI30–34.9; M023 BMI35–39.9; M024 BMI≥40; M025 weight; M026 white; M027 black; M028 other race; M029 race missing; M030 zip-income; M031 income missing; M032 never smoker; M033 former smoker; M034 current smoker; M035 smoking missing; M036 Ohio; M037 Florida; M038 hypertension; M039 dyslipidemia; M040 peripheral neuropathy; M041 HF; M042 CAD; M043 COPD; M044 nephropathy; M045 AF; M046 peripheral arterial disease; M047 MI; M048 cerebrovascular disease; M049 ischemic stroke; M050 dialysis; M051 HbA1c; M052 HbA1c missing; M053 systolic BP; M054 systolic BP missing; M055 diastolic BP; M056 diastolic BP missing; M057 eGFR; M058 eGFR missing; M059 HDL-C; M060 HDL-C missing; M061 LDL-C; M062 LDL-C missing; M063 triglycerides; M064 triglycerides missing; M065 UACR; M066 UACR missing; M067 any noninsulin medication; M068 zero noninsulin classes; M069 one class; M070 two classes; M071≥3 classes; M072 insulin; M073 lipid lowering; M074 renin–angiotensin inhibitors; M075 other antihypertensive; M076 aspirin; M077 warfarin; M078 standardized-difference definition; M079 clinical units/conversions; M080 medication/renal definitions.

M078 footnote: standardized differences described as absolute value of difference in means or proportions (surgery−control) divided by pooled SD. Table prints both positive and negative values; this map preserves its wording and values without assigning a judgment. M079 BMI kg/m²; BP mmHg; eGFR mL/min; HbA1c%; HDL/LDL/triglycerides mg/dL; UACR mg/g; zip income dollars; weight kg; cholesterol conversion×.0259 mmol/L and triglycerides×.0113. M080 eGFR MDRD approximation; drug class detail eTable3; renin–angiotensin includes ACE inhibitors/ARBs.


```text
              Table 1. Characteristics of Metabolic Surgery Patients and Nonsurgical Control Patients at the Index Date Before and After Matching
                                              Metabolic Surgery     Nonsurgical          Standardized Difference    Matched Nonsurgical Control   Standardized Difference
               Baseline Variable              (n = 2287)            (n = 39 267)a        Before Matchingb           (n = 11 435)                  After Matchingb
               Demographic Data
               Index date,                    1/2013                6/2014               −42.6                      7/2013                        −15.9
               median (IQR)                   (7/2010-4/2015)       (5/2012-2/2016)                                 (5/2011-4/2015)
               Sex, No. (%)
                 Women                        1499 (65.5)           20 372 (51.9)        28.0                       7339 (64.2)                   2.9
                 Men                          788 (34.5)            18 895 (48.2)        −28.0                      4096 (35.8)                   −2.9
               Age, median (IQR), y           52.5 (43.7-60.5)      61.6 (53.1-68.9)     −75.3                      54.8 (46.2-62.5)              −19.9
               BMI, median (IQR)c             45.1 (40-51.8)        35.9 (32.7-60.6)     113.5                      42.6 (39.4-47.2)              34.4
               BMI category,
               No. (%)
                 30-34.9                      109 (4.8)             17 110 (43.6)        −101.7                     495 (4.3)                     2.1
                 35-39.9                      465 (20.3)            11 320 (28.8)        −19.8                      2595 (22.7)                   −5.7
                 ≥40                          1713 (74.9)           10 837 (27.6)        107.4                      8345 (73.0)                   4.4
               Weight,                        126.5                 104.8                88.3                       120.2                         27.8
               median (IQR), kg               (110.2-148.0)         (93.0-119.0)                                    (106.8-136.5)
               Race, No. (%)
                 White                        1734 (75.8)           29 014 (73.9)        4.45                       7994 (69.9)                   13.3
                 Black                        441 (19.3)            8138 (20.7)          −3.6                       2804 (24.5)                   −12.7
                 Other                        54 (2.4)              874 (2.2)            0.9                        234 (2.1)                     2.1
                 Missing                      58 (2.5)              1241 (3.2)           −3.8                       403 (3.5)                     −5.8
               Annual zip code income,        49 855                50 378               0.7                        48 732                        10.8
               median (IQR), $                (39 964-62 273)       (37 958-65 536)                                 (36 951-61 512)
                 Missing, No. (%)             70 (3.1)              494 (1.3)            12.4                       125 (1.1)                     13.8
               Smoking status,
               No. (%)
                 Never                        1231 (53.8)           18 087 (46.1)        15.6                       5615 (49.1)                   9.5
                 Former                       828 (36.2)            15 531 (39.6)        −6.9                       4012 (35.1)                   2.3
                 Current                      170 (7.4)             5051 (12.9)          −18.1                      1607 (14)                     −21.5
                 Missing                      58 (2.5)              598 (1.5)            7.2                        201 (1.8)                     5.4
               Location, No. (%)
                 Ohio                         1816 (79.4)           35 482 (90.4)        −30.9                      9834 (86.0)                   −17.5
                 Florida                      471 (20.6)            3785 (9.6)           30.9                       1601 (14.0)                   17.5
               Medical History, No. (%)
               Hypertension                   1953 (85.4)           30 308 (77.2)        21.2                       8565 (74.9)                   26.5
               Dyslipidemia                   1686 (73.7)           27 717 (70.6)        7.0                        7457 (65.2)                   18.6
               Peripheral                     242 (10.6)            4569 (11.6)          −3.4                       1203 (10.5)                   0.2
               neuropathy
               Heart failure                  238 (10.4)            4470 (11.4)          −3.1                       1342 (11.7)                   −4.2
               Coronary artery                237 (10.4)            5863 (14.9)          −13.8                      1104 (9.7)                    2.4
               disease
               COPD                           206 (9.0)             4179 (10.6)          −5.5                       1188 (10.4)                   −4.7
               Nephropathy                    191 (8.4)             5069 (12.9)          −14.8                      1219 (10.7)                   −7.8
               Atrial fibrillation            152 (6.6)             3242 (8.3)           −6.1                       701 (6.1)                     2.1
               Peripheral arterial            123 (5.4)             3426 (8.7)           −13.1                      755 (6.6)                     −5.2
               disease
               Myocardial                     55 (2.4)              1201 (3.1)           −4.0                       211 (1.8)                     3.9
               infarction
               Cerebrovascular                42 (1.8)              1703 (4.3)           −14.5                      358 (3.1)                     −8.3
               disease
               Ischemic stroke                34 (1.5)              1385 (3.5)           −13.1                      298 (2.6)                     −7.9
               Dialysis                       14 (0.6)              322 (0.8)            −2.5                       78 (0.7)                      −0.9

                                                                                                                                                               (continued)




              jama.com                                                                                         (Reprinted) JAMA October 1, 2019 Volume 322, Number 13        1275

```

```text
               Table 1. Characteristics of Metabolic Surgery Patients and Nonsurgical Control Patients at the Index Date Before and After Matching (continued)
                                                    Metabolic Surgery     Nonsurgical            Standardized Difference         Matched Nonsurgical Control      Standardized Difference
                   Baseline Variable                (n = 2287)            (n = 39 267)a          Before Matchingb                (n = 11 435)                     After Matchingb
                   Clinical and Laboratory Data
                   HbA1c, median (IQR), %           7.1 (6.3-8.2)         7 (6.4-8.1)            −2.3                            7.1 (6.4-8.4)                    −11.4
                     Missing, No. (%)               159 (7.0)             4899 (12.5)            −18.7                           1288 (11.3)                      −15.0
                   Blood pressure,
                   median (IQR), mm Hg
                     Systolic                       138 (127-148)         130 (120-142)          31.6                            130 (121-142)                    30.1
                         Missing, No. (%)           0                     234 (0.6)              −10.9                           54 (0.5)                         –9.7
                     Diastolic                      71 (65-79)            76 (69-82)             −35.3                           78 (70-84)                       −44.2
                         Missing, No. (%)           0                     234 (0.6)              −10.9                           54 (0.5)                         –9.7
                   eGFR, median (IQR), mL/mind      90 (72-108)           86 (68-105)            11.5                            92 (72-112)                      −8.1
                     Missing                        1 (0)                 1620 (4.1)             −28.9                           432 (3.8)                        −27.5
                   HDL-C, median (IQR), mg/dL       44 (37-52)            43 (36-52)             1.6                             43 (36-51)                       4.9
                     Missing, No. (%)               792 (34.6)            12 966 (33.0)          3.4                             3512 (30.7)                      8.4
                   LDL-C, median (IQR), mg/dL       92 (72-115)           89 (68-114)            5.5                             93 (72-118)                      −4.9
                     Missing, No. (%)               208 (9.1)             10 469 (26.7)          −47.1                           2947 (25.8)                      −45.1
                   Triglycerides,                   146 (101-209)         143 (101-205)          1.8                             146 (103-208)                    −1.4
                   median (IQR), mg/dL
                     Missing, No. (%)               160 (7)               6538 (16.7)            −30.2                           1816 (15.9)                      −28.2
                   UACR, median (IQR), mg/g         14 (6-40)             14 (5-40)              −0.5                            14 (5-43)                        −3.8
                     Missing, No. (%)               1003 (43.9)           14 665 (37.4)          13.3                            4224 (36.9)                      14.1
                   Medication History
                   Noninsulin diabetes              1869 (81.7)           32 428 (82.6)          −2.2                            9253 (80.9)                      2.1
                   medication, No. (%)e
                     0                              418 (18.3)            6839 (17.4)            2.2                             2182 (19.1)                      −2.1
                     1                              1088 (47.6)           18 206 (46.4)          2.4                             5218 (45.6)                      3.9
                     2                              560 (24.5)            10 084 (25.7)          −2.8                            2929 (25.6)                      −2.6
                     ≥3                             221 (9.7)             4138 (10.5)            −2.9                            1106 (9.7)                       0
                   Insulin, No. (%)                 776 (33.9)            10 811 (27.5)          13.9                            3806 (33.3)                      1.4
                   Lipid-lowering                   1195 (52.3)           23 963 (61.0)          −17.8                           5998 (52.5)                      −0.4
                   medications, No. (%)
                   Renin-angiotensin system         1396 (61.0)           25 375 (64.6)          −7.4                            7102 (62.1)                      −2.2
                   inhibitors, No. (%)f
                   Other antihypertensive           1649 (72.1)           28 710 (73.1)          −2.2                            8066 (70.5)                      3.5
                   medications, No. (%)
                   Aspirin                          731 (32.0)            18 961 (48.3)          −33.8                           4627 (40.5)                      −17.8
                   Warfarin                         190 (8.3)             3207 (8.2)             0.5                             943 (8.2)                        0.2
               Abbreviations: BMI, body mass index; COPD, chronic obstructive pulmonary                      or proportions between the groups (metabolic surgery − nonsurgical control
               disease; eGFR, estimated glomerular filtration rate; HbA1c, glycated                          group) divided by pooled standard deviation.
               hemoglobin; HDL-C, high-density lipoprotein cholesterol; LDL-C, low-density               c
                                                                                                             Calculated as weight in kilograms divided by height in meters squared.
               lipoprotein cholesterol; UACR, urinary albumin-creatinine ratio.                          d
                                                                                                             Approximated using the Modification of Diet in Renal Disease (MDRD)
               SI conversion factors: To convert HDL-C and LDL-C values to mmol/L, multiply                  Study equation.
               by 0.0259; triglyceride values to mmol/L, multiply by 0.0113.                             e
                                                                                                             Class of diabetes medications has been detailed in eTable 3 in Supplement 1.
               a
                   Starting with the base cohort of 287 438 patients with type 2 diabetes,               f
                                                                                                             Including angiotensin-converting enzyme inhibitors and angiotensin
                   an algorithm (Figure 1) was implemented that resulted in a total of 39 267
                                                                                                             receptor blockers.
                   nonsurgical patients before matching (see Methods).
               b
                   Standardized differences are the absolute value of the difference in means




               coronary artery events, cerebrovascular events, heart failure,                            outcomes, except for atrial fibrillation (P values testing the pro-

```

## All eight outcome results and inferential tuples

All rows below are [Table2 PDF p7](../../../jama_aminian_2019_oi_190103.pdf#page=7). Confidence level95%. Cumulative incidence percentages are Kaplan–Meier at8y. ARD percentage points is labeled control−surgery, percentile bootstrap1000 iterations. HR and P come from fully adjusted Cox surgery/control, all baseline Table1 variables. Columns are preserved as printed, with no substitution from arithmetic.

| Record and endpoint | Initial risk surgery/control | Surgery8y %(95%CI) | Control8y %(95%CI) | ARD8y %(95%CI) | HR(95%CI) | P | Matching main-paper locations |
|---|---|---|---|---|---|---|---|
| M081 Primary extended MACE | 2287/11435 | 30.8(27.6–34.0) | 47.7(46.1–49.2) | 16.9(13.1–20.4) | .61(.55–.69) | <.001 | abstract p1; Key Points p2 HR.61; body p4; Figure2A p7; Discussion p9 rounded31%/48% |
| M082 Secondary three-component MACE | 2287/11435 | 17.0(14.3–19.7) | 27.6(26.2–29.0) | 10.6(7.5–13.6) | .62(.53–.72) | <.001 | body p4; Figure2B p7; Discussion p9 significant lower |
| M083 All-cause mortality | 2287/11435 | 10.0(7.8–12.2) | 17.8(16.6–19.0) | 7.8(5.1–10.2) | .59(.48–.72) | <.001 | abstract p1; body p4; Figure3A p8; Discussion p9 ARD7.8% |
| M084 Heart failure | 2049/10093 | 6.8(4.9–8.6) | 18.9(17.6–20.2) | 12.9(10.4–15.1) | .38(.30–.49) | <.001 | body p6; Figure3B p8; Discussion pp10–11 lower |
| M085 Coronary artery disease | 2050/10331 | 7.9(5.9–9.8) | 11.6(10.5–12.6) | 4.2(1.9–6.8) | .69(.54–.87) | .002 | body p6 calls coronary artery events; Figure3C p8 |
| M086 Cerebrovascular disease | 2245/11077 | 4.1(2.7–5.5) | 5.6(4.9–6.3) | 1.8(−.03 to3.4) | .67(.48–.94) | .02 | body p6 calls cerebrovascular events; Figure3D p8 |
| M087 Nephropathy | 1937/9190 | 6.1(4.4–7.8) | 16.3(15.0–17.6) | 11.1(8.8–13.6) | .40(.31–.52) | <.001 | body p6; Figure3E p8; Discussion p11 lower |
| M088 Atrial fibrillation | 2135/10734 | 7.9(6.1–9.7) | 13.6(12.5–14.7) | 6.5(4.4–8.7) | .78(.62–.97) | .03 | body p6; Figure3F p8; Discussion p11 lower |

M089 [p4 counts](../../../jama_aminian_2019_oi_190103.pdf#page=4): primary surgery385/control3243; secondary composite194/1765; deaths112/1111, occurring by study end rather than numerators of fixed8y crude risk. Primary count and deaths repeat abstract p1. M090 [p4 subgroup statement](../../../jama_aminian_2019_oi_190103.pdf#page=4): no heterogeneity from interaction by sex, age, BMI, HbA1c, eGFR, insulin, sulfonylurea, lipid lowering, with exact numeric subgroup results delegated to support evidence eFigure1. M091 [p6 PH statement](../../../jama_aminian_2019_oi_190103.pdf#page=6): PH satisfied for composite and individual outcomes except AF; eTable6 assumption tests, eTable7 AF and all-outcome time-varying HRs, eTable5 cumulative incidence at2,5,8y. Main paper does not print those assumption P values.

## Figure 2 and Figure 3 complete risk sets and captions

Times0,2,4,6,8 years since index; all figures show control blue above surgery orange. Figure2A/B HR/CI/P identical to M081/M082, plotted cumulative incidence% with ticks0,10,20,30,40,50. Figure3A–F HR/CI/P identical to M083–M088, ticks0,5,10,15,20%. Curves are displays of the same matched endpoint definitions, not extra printed event counts.

| Record / source / panel | Controls risk counts at0,2,4,6,8y | Surgery risk counts at0,2,4,6,8y | Caption observation median(IQR), controls then surgery |
|---|---|---|---|
| M092 [p7 Figure2A](../../../jama_aminian_2019_oi_190103.pdf#page=7), primary | 11435,8050,4791,2244,838 | 2287,1372,910,535,293 | 4.0(2.1–6.1)y;3.3(1.2–6.3)y |
| M093 [p7 Figure2B](../../../jama_aminian_2019_oi_190103.pdf#page=7), secondary | 11435,8645,5543,2826,1130 | 2287,1438,991,610,336 | same as primary |
| M094 [p8 Figure3A](../../../jama_aminian_2019_oi_190103.pdf#page=8), death | 11435,8844,5789,3005,1224 | 2287,1460,1017,629,353 | 4.0(2.1–6.1)y;3.3(1.2–6.3)y |
| M095 [p8 Figure3B](../../../jama_aminian_2019_oi_190103.pdf#page=8), HF | 10093,7572,4845,2468,991 | 2049,1281,895,552,317 | 4.1(2.2–6.2)y;3.3(1.1–6.4)y |
| M096 [p8 Figure3C](../../../jama_aminian_2019_oi_190103.pdf#page=8), CAD | 10331,7776,4958,2516,995 | 2050,1283,878,538,299 | 4.0(2.1–6.1)y;3.3(1.1–6.4)y |
| M097 [p8 Figure3D](../../../jama_aminian_2019_oi_190103.pdf#page=8), cerebrovascular | 11077,8474,5492,2847,1149 | 2245,1418,982,607,338 | 4.0(2.1–6.1)y;3.3(1.1–6.3)y |
| M098 [p8 Figure3E](../../../jama_aminian_2019_oi_190103.pdf#page=8), nephropathy | 9190,7056,4515,2262,893 | 1937,1216,838,506,293 | 4.1(2.2–6.2)y;3.3(1.1–6.3)y |
| M099 [p8 Figure3F](../../../jama_aminian_2019_oi_190103.pdf#page=8), AF | 10734,8152,5212,2660,1072 | 2135,1328,915,555,319 | 4.0(2.1–6.1)y;3.3(1.1–6.3)y |

The Figure3 caption explicitly removes prior cases for five individual nonmortality outcomes. Compare initial risk counts with Table1 history values only after endpoint definition matching (nephropathy definitions are in supplement). Figure2 caption preserves composite6 and composite3 definitions and first occurrence after index.

## Weight, glycemia, prescriptions and surgical safety

| Record | Source | Complete printed quantitative relationship |
|---|---|---|
| M100 | [p7 body](../../../jama_aminian_2019_oi_190103.pdf#page=7) | At8y mean body-weight reduction surgery29.1kg(95%CI28.8–29.3),control8.7kg(8.6–8.9),difference20.3kg(20.1–20.6). HbA1c difference in change from baseline at8y1.1 percentage points(1.0–1.2),P<.001. eTable8/eFigure2 match keys. |
| M101 | [p9 Figure4A](../../../jama_aminian_2019_oi_190103.pdf#page=9) | Total weight loss%; y-axis percent change%(95%CI),ticks0,−5,−10,−15,−20,−25 (bottom display also labels0); x0,2,4,6,8y. Delta14.7%(95%CI14.5–14.9),P<.001. Surgery greater weight loss. Smoothed mean percentage weight lost from baseline; shaded95%CIs. |
| M102 | [p9 Figure4B](../../../jama_aminian_2019_oi_190103.pdf#page=9) | Absolute HbA1c values% with95%CI,y-axis5.5–8.0 at.5 steps;x0,2,4,6,8y. Delta1.1%(95%CI1.0–1.2),P<.001; caption delta concerns change from baseline difference at8y, not absolute HbA1c levels. Four-knot spline time×treatment; point counts/eTable8/eTable9. |
| M103 | [p7 medication text](../../../jama_aminian_2019_oi_190103.pdf#page=7) | Lower use in surgery of noninsulin diabetes medication,insulin,renin–angiotensin blockers,other antihypertensives,lipid-lowering,aspirin; reference Figure5,eTable8,eFigure2. Quantities represent prescription orders, as explained p11. |
| M104 | [p10 Figure5A](../../../jama_aminian_2019_oi_190103.pdf#page=10) | Noninsulin medications,P<.001,surgery lower at8y; y proportion taking drug%(95%CI),ticks10,30,50,70,90;x0,2,4,6,8y. |
| M105 | [p10 Figure5B](../../../jama_aminian_2019_oi_190103.pdf#page=10) | Insulin,P=.008,surgery lower at8y;same axes. |
| M106 | [p10 Figure5C](../../../jama_aminian_2019_oi_190103.pdf#page=10) | Renin–angiotensin system inhibitors,P<.001,surgery lower at8y;same axes. |
| M107 | [p10 Figure5D](../../../jama_aminian_2019_oi_190103.pdf#page=10) | Other antihypertensives,P<.001,surgery lower at8y;same axes. |
| M108 | [p10 Figure5E](../../../jama_aminian_2019_oi_190103.pdf#page=10) | Lipid-lowering,P<.001,surgery lower at8y;same axes. |
| M109 | [p10 Figure5F](../../../jama_aminian_2019_oi_190103.pdf#page=10) | Aspirin,P<.001,surgery lower at8y;same axes. |
| M110 | [p10 Figure5 caption](../../../jama_aminian_2019_oi_190103.pdf#page=10) | Proportions computed every tenth of a year from index through8y; pointwise95%CIs,shaded regions; P from Fisher exact test comparing8y proportions. Renin–angiotensin includes ACE inhibitors/ARBs. eTable8/eTable10 supply statistical comparisons/sample size. Main figure gives curves, not numeric group proportions/CI endpoints or counts. Method text p4 names two-sample proportions test. |
| M111 | [p7 safety](../../../jama_aminian_2019_oi_190103.pdf#page=7) | Postoperative stay median2d(IQR2–3).90d complications: bleeding transfusion68(3.0%);pulmonary58(2.5%);VTE22(1.0%);cardiac17(.7%);dialysis4(.2%);cerebrovascular0. Surgery group2287 denominator. |
| M112 | [p7 safety](../../../jama_aminian_2019_oi_190103.pdf#page=7) | Within90d abdominal surgical intervention109(4.8%);death15(.7%);early endoscopy16.7%,interventional radiology1.6%,parenteral nutrition1.4%. No counts printed for latter three in main. Longer follow-up reinterventions eTable11; nutritional hemoglobin,protein,albumin,vitaminD eTable8/eFigure3. |
| M113 | [pp8–9 sensitivity](../../../jama_aminian_2019_oi_190103.pdf#page=9) | Fully adjusted Cox15 cohorts,all8 outcomes,HR/95%CI from each;eFigure4. Narrative says differences negligible relative to single1:5 cohort. E-values vs measured-risk-factor HRs,eTable12,interpretation unmeasured confounder unlikely to account for associations. No numerical E-values in main. |
| M114 | [p9 Discussion](../../../jama_aminian_2019_oi_190103.pdf#page=9) | MACE48% control/31% surgery;all6 individual prespecified outcomes significantly lower;three-component composite lower;8y mortality ARD7.8%. Observational hypothesis-generating; confirmation by RCT needed, repeats conclusion p11. |
| M115 | [p11 limitations](../../../jama_aminian_2019_oi_190103.pdf#page=11) | No severity-based baseline matching/adjustment; mortality cause unavailable; prescription orders need not equal actual use; long-term adverse events without intervention not assessed; between-procedure comparisons not performed because unequal distribution and need new comparable cohorts; <10% controls exposed to new GLP-1/SGLT2 drugs. No extra printed sample count. |
| M116 | [pp9–11 contextual quantities](../../../jama_aminian_2019_oi_190103.pdf#page=9) | Literature contextual values retained as non-study: Look AHEAD weight loss8.6/.7% at1y,6.0/3.5% at9y; Fisher HR.60 macrovascular/.33 mortality at5y and event rates2–3fold below current; SOS343 surgery/260 control,vertical banded gastroplasty66%,band18%;p11 meta-analysis nonsurgical weight loss5%,prior albuminuria resolution50%,prior nephropathy incidence59%lower at5y. These are not observations in this cohort and not reconstructed through external literature. |

## Explicit page coverage and match keys

| PDF page | Units inspected and mapped | Relevant mapper records | No-applicable portions |
|---|---|---|---|
| 1 | Complete abstract,design,populations,baseline summaries,primary/mortality tuples | M001,M007,M015,M016,M081,M083,M089 | Affiliations/contact/publication bibliographic dates; no quantitative cohort relationships there |
| 2 | Key Points,base cohort,surgery/control selection,endpoint start | M002,M003,M007,M081 | Background qualitative literature narrative; no additional study result tuple |
| 3 | Complete Figure1 and all reason counts/footnotes;composite/individual risk definitions;other outcomes;statistical-method start | M004–M009 | No omitted figure branches or reason rows |
| 4 | Full statistical methods/imputation/subgroup/sensitivity;cohort procedures/BMI/follow-up;primary/secondary/death narrative | M009–M016,M081–M083,M089,M090 | No extra printed test statistic or SE |
| 5 | Entire Table1 first page,all rows and columns | M017–M050 | Page furniture/bibliographic header |
| 6 | Entire Table1 continuation,all rows/columns/units/footnotes;individual outcomes and PH narrative | M051–M080,M091 | Page furniture |
| 7 | Both Figure2 panels,all risk counts/caption;8 Table2 rows and footnotes;weight/glycemia/medication/adverse-event narrative | M081–M093,M100,M103,M111,M112 | None of the result displays omitted |
| 8 | All6 Figure3 panels,risk counts/caption;sensitivity start | M094–M099,M113 | None of the outcome panels omitted |
| 9 | Both Figure4 panels/caption;sensitivity continuation;Discussion with study and literature numbers | M101,M102,M113,M114,M116 | Literature statements do not create this study's outcome records |
| 10 | All6 Figure5 panels/caption;Discussion continuation | M104–M110,M114,M116 | No numerical curve values inferred from unlabeled graphical coordinates |
| 11 | Study interpretations,limitations,conclusion;contextual quantities;article information | M114–M116 | Article information/authorship/publication/funding has no result-applicable quantitative relationship |
| 12 | Full disclosure/funding/sponsor/contribution sections and references1–31 | No new M relationship | Explicit no-applicable unit: bibliographic volume/page/year/DOI numbers and funding identifiers are not study quantities; no new outcome, denominator, model or test tuple |

Cross-source match keys supplied for checker/support-map joins: eTable1 endpoint definitions; eTable2 procedure codes; eTable3 medication classes; eTable4 events/person-years/rates; eTable5 risk at2,5,8y; eTable6 PH; eTable7 time-varying HR; eTable8 longitudinal effects; eTable9 metabolic/nutritional contributors; eTable10 medication contributors; eTable11 reinterventions; eTable12 E-value; eFigure1 primary subgroups; eFigure2 cardiometabolic trends; eFigure3 nutrition; eFigure4 sensitivity cohorts. PLAN comparison keys: endpoint status/composite definition;index-date population and exclusions;matching ratio/covariates;analysis models;missing-data method;subgroup analyses;longitudinal and medication tests;sensitivity sampling/matching;confidence/significance and secondary multiplicity treatment. These are join instructions, not diagnosed observations.

## Completion and extraction limits

116 locally numbered relationship records, including 64 baseline row/definition records, eight complete outcome tuples, eight complete risk-set/caption records, six medication panel records, design/method relationships and every matching main narrative. Every displayed number in Table1 is retained in the layout transcription; every Table2 result and Figure2–5 printed result is retained above. No main-paper forest plot exists; forest-plot/subgroup/sensitivity results are in the supplied results supplement, assigned to the support mapper. No direct-source unit remains unmapped. No missing input prevents main mapping. Exact person-years, cause-specific rates, subgroup estimates, E-values, longitudinal contributor counts and numerical graph-curve coordinates are not printed in the main article; source cross-references identify supplied supplement locations for all but the curve coordinates. Unlabeled plotted coordinates were not promoted to printed exact values. Raw participant data/model covariance/bootstrap draws are not supplied in this article; those inputs are outside extraction scope. No candidate selection, comparison adjudication or old candidate/report conclusion was used.
