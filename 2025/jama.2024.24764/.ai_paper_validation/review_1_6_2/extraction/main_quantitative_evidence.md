# Complete main-paper quantitative evidence map

Scope: DOC-001, REPORT, `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF pages 1-11. All 11 reusable-backed pages newly mapped; zero fresh-required pages. This artifact records source evidence and matching relationships, without candidate diagnosis. Local relationship identifiers M001-M137 are reserved to this map; global numeric and statistical identifiers are assigned by the checkers. Each table row is one relationship record, potentially containing both arm values or all members of a defined count partition.

## Provenance and complete page coverage

Source SHA-256: 61596edb2b6c950b02356e49a5fe61c48c0ebacb60d347855a51be0f1e676b52. Sources and reusable assets were read only. Controls read: complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md; source_inventory.md; evidence_asset_inventory.md; source_coverage.md; tooling_record.md.

Preferred reusable complete text: `.ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/normalized_text/native_text.txt`, legacy normalized pypdf native text (version not retained), exact source-page headers, all 11 pages. Alignment companion: `.ai_paper_validation/review_1_5_3/preprocessing/numeric_direct/DOC-001_pp03-09_layout.txt`, legacy geometric layout extraction, version not retained, seven form-feed records matching PDF pages 3-9. The companion and complete text were read across the assigned scope. Full-page images `.ai_paper_validation/document_outputs/JAMA2024-24764-MAIN/page_images/page-03.png`, `page-08.png`, and `page-09.png` were visually inspected for flow, outcome-table values/footnotes, and forest-plot row alignment. These are eligible source-matched reusable rasters; rendering engine/version not retained. No new extraction, rendering or OCR was required; no GPU inference was performed by this mapper.

| PDF page | Printed page | Units inspected and mapped | Coverage |
|---|---:|---|---|
| 1 | 853 | Abstract: setting, intervention, primary and secondary results and conclusion | COMPLETE |
| 2 | 854 | Introduction, eligibility, individual randomization, Key Points | COMPLETE |
| 3 | 855 | Figure 1 and all footnotes; minimization; treatment pressure/duration | COMPLETE |
| 4 | 856 | Outcomes, full statistical analysis, recruitment | COMPLETE |
| 5 | 857 | Every Table 1 baseline row | COMPLETE |
| 6 | 858 | Table 1 continuation; participant narrative; adherence; primary/secondary/safety results; discussion | COMPLETE |
| 7 | 859 | Every Table 2 row and footnote; discussion including historical evidence context and assessment-method change | COMPLETE |
| 8 | 860 | Every Table 3 row and footnote; assessment-method event fractions | COMPLETE |
| 9 | 861 | Every Figure 2 row, interaction P value, axis/legend/footnote; limitations | COMPLETE |
| 10 | 862 | Mortality/generalizability narrative; conclusion; article information and references | COMPLETE |
| 11 | 863 | References only; no applicable trial-result quantitative unit | COMPLETE; NO_APPLICABLE_TRIAL_RESULT |

In all paired values below, order is iNPWT then surgeon's preference. Default arm denominator for Tables 1 and 2 is 411 then 410. Brackets [n] indicate an explicitly printed available-case count, not an inferential analysis sample size. Percentages in those tables are retained as printed; the header population, a reported total available count, and any row-specific denominator are recorded separately. No assumption of mutually exclusive staffing levels or of a crude effect estimate is made.

## Abstract, Key Points, design, flow and method relationships

| ID | Exact location | Evidence and matching relationship | Kind |
|---|---|---|---|
| M001 | PDF p1 abstract design; p2 Ethics; p4 Recruitment | Phase 3, assessor-masked, pragmatic, individual-participant randomized trial; 22 UK hospitals/centers and 12 Australian; recruitment December 18, 2018-May 25, 2021; follow-up 30 days; database closure August 25, 2021 | Population/time |
| M002 | PDF p1 abstract interventions; p2 randomization; p3 Figure 1; p4 Recruitment | Allocation 1:1; abstract arms n=411/410; total randomized 840 (UK 536/Australia 304). Figure initial arms 424/416; 19 excluded before trial data, leaving 821 and arms 411/410 | Count linkage |
| M003 | PDF p1 abstract results; p3 Figure 1; p6 primary narrative; p8 Table 3; p9 Figure 2 | 52 postrandomization exclusions in abstract; primary analysis 394/394. SSI 112/394 (28.4%) versus 108/394 (27.4%); adjusted RR 1.03 (95% CI 0.83-1.28), P=.78. Table 3 percentages 28/27 and adjusted RD 0.010 (−0.050 to 0.071); Figure 2 events 112/108 and same RR. Key Points p2 repeats total 840 and percentages 28.4/27.4 with no statistically significant difference at 30 days | Primary count/estimate/test |
| M004 | PDF p1 abstract demographics; p6 Results; p5 Table 1 | Overall age mean 63.8 years, range 18.8-95.3; 52% female abstract; 390 (48%) male p6; group age and sex rows below | Population linkage |
| M005 | PDF p1 abstract outcomes/results; p6 Secondary/Discussion; p8 Table 3 | Seven secondary outcomes; six no significant difference. Abstract combined-country LOS median (IQR) 8 (6-14) versus 9 (6-14.5) days, ratio geometric means 0.96 (0.88-1.06), P=.21; matches p6/Table 3. No effect on SSI conclusion; one secondary pain-at-day7 effect described below | Outcome/claim linkage |
| M006 | PDF p2 Eligibility | UK age ≥16; Australia ≥18; incision ≥5 cm; primary fascia and skin closure; includes laparoscopic-assisted/extraction/conversion if incision ≥5 cm. Excludes abdominal operation in previous 3 months, planned reopening within 30 days, not expected to survive beyond 30 days | Population/endpoint window |
| M007 | PDF pp2-3 Randomization | Individual 1:1 minimization with random component; covariates confirmed operative contamination (clean, clean-contaminated, contaminated, dirty), stoma at end of operation, recruiting center. Randomization during skin closure; patients and surgeons unmasked, formal assessors masked | Design/analysis linkage |
| M008 | PDF p3 intervention; p4 continuation | PICO 7 topical iNPWT; −80 mm Hg; intended duration 7 days or discharge first; ≥1 replacement dressing allowed; immediate replacement not nonadherence. Control any simple dressing/glue/no dressing; excludes iNPWT and silver/honey/iodine active dressings | Intervention/duration |
| M009 | PDF p3 Figure 1 upper flow | 2916 screened; 2076 excluded; exclusion counts 709 ineligible, 525 staff unavailable, 497 not identified before procedure, 132 declined, 34 procedure did not proceed, 34 initially laparoscopic converted open, 27 dressing unavailable, 23 suspended recruitment, 95 other/unknown; 840 randomized | Flow total/partition |
| M010 | PDF p3 Figure 1 footnote a | Ineligibility reasons: recent abdominal operation 286; incapacity/unable consent 114; not emergency laparotomy 100; expected reopening ≤30 days 56; unable/unwilling day30 follow-up 49; incision <5 cm 47; skin not primarily closed 26; representative unavailable 22; age <16 years 9 | Flow reason partition |
| M011 | PDF p3 Figure 1 iNPWT branch | 424 randomized; 13 excluded (11 did not consent, 2 requested removal); 411 remaining; 404 received as randomized, 6 did not, 1 undetermined; 12 further exclusions (5 withdrew, 5 died, 2 lost); 399 completed day30; 394 primary analysis; 5 completed follow-up but CDC data insufficient | Flow nested counts |
| M012 | PDF p3 Figure 1 control branch | 416 randomized; 6 excluded (5 did not consent, 1 requested removal); 410 remaining; 402 received as randomized, 8 did not; 12 further exclusions (8 died, 2 withdrew, 2 lost); 398 completed day30; 394 primary analysis; 4 completed follow-up but CDC data insufficient | Flow nested counts |
| M013 | PDF p3 Figure 1 footnotes b/c | 25 deaths total (10/15); 12 supplied primary outcome data before death (5/7) and were included; missing CDC criteria prevented primary outcome computation despite day30 completion. Footnote death time not explicitly limited to 30 days; mortality-within30 rows have separate window | Death/analysis inclusion |
| M014 | PDF p4 Outcomes | Primary SSI up to day30, operation day0; CDC superficial or deep incisional SSI, either/both binary yes. Assess days7-10 or earlier discharge, before reoperation, near/after day30, intervening diary. If dropout/death with prior SSI count event; without prior SSI, missing outcome | Primary outcome/missingness |
| M015 | PDF p4 Outcomes | Secondary LOS; wound-related complications excluding SSI and other complications, 6-level Clavien-Dindo to day30; wound-related readmission within30; primary-laparotomy pain 10-point visual analogue days7/30; SF-12 days7/30; EQ-5D-5L days7/14/21/30; SAEs and mortality to day30 | Outcome definitions/times |
| M016 | PDF p4 Statistical Analysis | Sample size: detect 40% relative SSI reduction / 10% absolute difference, 25% control to 15% iNPWT, 90% power, type I error 5% (α=.05), 20% attrition; 420 per arm, total840 | Sample-size inputs |
| M017 | PDF p4 Statistical Analysis | Complete-case available data without imputation, intention-to-treat by randomized group. Model-based effects adjust minimization covariates; center random effect; baseline scores where appropriate; all effects 95% CIs. SAS9.4 and Stata17 | Analysis set/adjustment |
| M018 | PDF p4 Statistical Analysis; p8 Table 3 footnotes a/b | Primary mixed-effects binomial regression: log link adjusted RR, identity link adjusted RD. Categorical secondary measures analyzed similarly. RR<1 and absolute difference<0 favor iNPWT; null RR=1/RD=0 | Model/measure identity |
| M019 | PDF p4 sensitivity methods; p6 Primary | Prespecified sensitivity analyses: per-protocol; day30 assessment in 30-44-day window; exclude SSI solely diary identified; best/worst-case SSI imputation. Post hoc tipping-point MNAR analysis (results supplement eFigure4). Main per-protocol RR1.00 (0.80-1.25), P=.98; main claim robust all preplanned sensitivity analyses | Sensitivity analysis/test |
| M020 | PDF p4 secondary analysis; p8 Table 3 footnote c | LOS mixed-effect linear model after log transform; exponentiate to adjusted ratio geometric means. Longitudinal SF-12/EQ-5D-5L mixed-effect linear regression adjusted mean difference, treatment×time interaction, independent covariance structure | Secondary method |
| M021 | PDF p4 subgroup methods; p6 Primary/Discussion; p9 Figure 2 | Primary-only prespecified subgroups include contamination, stoma, operation, skin preparation, BMI, country; pandemic-related included assessment-method and date before/after March11,2020. Binomial model subgroup×treatment interaction. Figure also displays incision length <15/≥15 cm. No differential subgroup treatment effect claimed | Subgroup model/claims |
| M022 | PDF p4 Recruitment | 840 total; UK536/Australia304; 19 withdrawals before trial data: 16 Australia consent paperwork and 3 withdrawals. Remaining821; arms411/410 | Recruitment linkage |

## Every Table 1 quantitative row

Location for M023-M050 is PDF p5 Table 1; M051-M058 PDF p6 Table 1 continuation. Counts (percent) retain the printed header population 411/410 unless an explicit row denominator is shown. These are baseline descriptive values, not treatment estimates.

| ID | Row/quantity | iNPWT | Surgeon's preference | Unit/denominator context |
|---|---|---|---|---|
| M023 | Age mean (SD) | 63.8 (15.9) | 63.7 (16.4) | years |
| M024 | Sex male/female | 204 (49.6); 207 (50.4) | 186 (45.4); 224 (54.6) | counts (%); two-category partition |
| M025 | BMI mean (SD) [n] | 27.1 (7.4) [398] | 27.2 (7.0) [388] | kg/m² |
| M026 | Smoking total; never/current/previous | 405; 220 (53.5); 95 (23.1); 90 (21.9) | 402; 223 (54.4); 70 (17.1); 109 (26.6) | available totals separate from arm-header denominators |
| M027 | Diabetes | 40 (9.7) | 40 (9.8) | counts (%) |
| M028 | Diabetes diet controlled | 13/40 (32.5) | 9/40 (22.5) | explicit diabetes denominator |
| M029 | Diabetes tablet controlled | 16/40 (40.0) | 21/40 (52.5) | explicit diabetes denominator |
| M030 | Diabetes insulin controlled | 11/40 (27.5) | 10/40 (25.0) | explicit diabetes denominator |
| M031 | Albumin mean (SD) [n] | 33.9 (8.4) [406] | 34.6 (8.0) [405] | g/L |
| M032 | Immunosuppressive therapy | 39 (9.5) | 41 (10.0) | counts (%) |
| M033 | Clinically jaundiced/bilirubin>50 μmol/L | 4 (1.0) | 1 (0.2) | counts (%); numeric threshold |
| M034 | Active malignancy | 84 (20.4) | 76 (18.5) | counts (%) |
| M035 | Country UK/Australia | 264 (64.2); 147 (35.8) | 265 (64.6); 145 (35.4) | count partition; retained population |
| M036 | Clean contamination | 98 (23.8) | 99 (24.1) | minimization category |
| M037 | Clean-contaminated | 175 (42.6) | 176 (42.9) | minimization category |
| M038 | Contaminated | 81 (19.7) | 79 (19.3) | minimization category |
| M039 | Dirty | 57 (13.9) | 56 (13.7) | minimization category |
| M040 | Stoma preexisting | 22 (5.3) | 27 (6.6) | counts (%) |
| M041 | Stoma formed in operation | 131 (31.9) | 126 (30.7) | counts (%) |
| M042 | ASA I normal healthy | 29 (7.1) | 29 (7.1) | counts (%) |
| M043 | ASA II mild systemic disease | 162 (39.4) | 157 (38.3) | counts (%) |
| M044 | ASA III severe systemic disease | 173 (42.1) | 178 (43.4) | counts (%) |
| M045 | ASA IV constant threat to life | 43 (10.5) | 43 (10.5) | counts (%) |
| M046 | ASA V moribund | 4 (1.0) | 3 (0.7) | counts (%) |
| M047 | Antibiotics on induction | 310 (75.4) | 332 (81) | counts (%) |
| M048 | Antibiotics during procedure | 80 (19.5) | 61 (14.9) | counts (%) |
| M049 | Antibiotics induction and procedure | 8 (1.9) | 8 (2.0) | counts (%) |
| M050 | Antibiotics continued postoperatively | 234 (56.9) | 236 (57.6) | counts (%) |
| M051 | Skin preparation total | 411 | 409 | explicit available counts |
| M052 | 2% alcoholic chlorhexidine | 192 (46.7) | 183 (44.6) | counts (%); concentration retained |
| M053 | 0.5% alcoholic chlorhexidine | 56 (13.6) | 62 (15.1) | counts (%) |
| M054 | Aqueous povidone-iodine | 54 (13.1) | 52 (12.7) | counts (%) |
| M055 | Alcoholic povidone-iodine | 44 (10.7) | 46 (11.2) | counts (%) |
| M056 | 2% aqueous chlorhexidine | 34 (8.3) | 32 (7.8) | counts (%) |
| M057 | 0.5% aqueous chlorhexidine | 28 (6.8) | 33 (8.0) | counts (%) |
| M058 | Other preparation | 3 (0.7) | 1 (0.2) | counts (%) |

Table 1 footnotes (p6): BMI weight kg/height m squared; albumin g/L to g/dL divide by10; bilirubin μmol/L to mg/dL divide by17.104. Narrative p6 repeats BMI27.1; ASA III-V 444/821 (54%); contamination clean197/821 (24%), clean-contaminated351/821 (43%), contaminated160/821 (19%), dirty113/821 (14%); cross-links M025, M036-M039, M044-M046.

## Every Table 2 quantitative row

Exact location: PDF p7 Table 2, both columns and continuation. Default denominator 411/410; medians have explicitly printed available n. Footnotes: colonic includes large intestine/rectum; noncolonic includes stomach, duodenum, jejunum, ileum; nonbowel other abdominal organs/structures; wound-edge devices both1- and2-ring; adhesive drape applied before incision; consultant attending/staff, registrar fellowship/senior resident, senior house officer first2 training years. Staffing rows are recorded without assuming exclusivity.

| ID | Row/quantity | iNPWT | Surgeon's preference | Unit/context |
|---|---|---|---|---|
| M059 | Actual procedure colonic/noncolonic/nonbowel/other | 202 (49.1); 97 (23.6); 112 (27.3); 0 | 198 (48.3); 99 (24.1); 112 (27.3); 1 (0.2) | count category partition |
| M060 | Approach midline/nonmidline/laparoscopic-assisted or converted | 359 (87.3); 18 (4.4); 34 (8.3) | 366 (89.3); 9 (2.2); 35 (8.5) | count category partition |
| M061 | Incision length median (IQR) [n] | 20 (15-25) [395] | 17.3 (14-23) [392] | cm |
| M062 | WHO checklist | 402 (97.8) | 402 (98.0) | counts (%) |
| M063 | MRSA colonization | 3 (0.7) | 9 (2.2) | counts (%) |
| M064 | Malignancy present | 106 (25.8) | 110 (26.8) | intraoperative, distinct from baseline active malignancy |
| M065 | Blood loss available total | 407 | 406 | total for blood-loss row set |
| M066 | Blood loss <100 | 274 (66.7) | 249 (60.7) | mL |
| M067 | Blood loss100-500 | 115 (28.0) | 144 (35.1) | mL |
| M068 | Blood loss501-1000 | 16 (3.9) | 9 (2.2) | mL |
| M069 | Blood loss>1000 | 2 (0.5) | 4 (1.0) | mL |
| M070 | Intraoperative transfusion | 13 (3.2) | 15 (3.7) | counts (%) |
| M071 | Inotropes at operation end | 74 (18.0) | 79 (19.3) | counts (%) |
| M072 | Wound-edge protection device | 107 (26.0) | 99 (24.1) | counts (%) |
| M073 | Triclosan suture | 3 (0.7) | 8 (2.0) | counts (%) |
| M074 | Local anesthetic catheters | 169 (41.1) | 205 (50.0) | counts (%) |
| M075 | Drape iodine/plain | 18 (4.4); 68 (16.5) | 23 (5.6); 64 (15.6) | counts (%) |
| M076 | Wound wash povidone/saline-water/other | 72 (17.5); 104 (25.3); 21 (5.1) | 73 (17.8); 113 (27.6); 20 (4.9) | counts (%) |
| M077 | Gloves changed before closing | 148 (36.0) | 148 (36.1) | counts (%) |
| M078 | Instruments changed before closing | 39 (9.5) | 39 (9.5) | counts (%) |
| M079 | Skin closure staples/continuous/interrupted | 233 (56.7); 178 (43.3); 0 | 215 (52.4); 190 (46.3); 5 (1.2) | counts (%) |
| M080 | Operating surgeon consultant/registrar/SHO | 319 (77.6); 123 (29.9); 4 (1.0) | 318 (77.6); 110 (26.8); 1 (0.2) | counts (%), all printed staffing levels |
| M081 | Fascia closer consultant/registrar/SHO | 201 (48.9); 218 (53.0); 26 (6.3) | 193 (47.1); 225 (54.9); 15 (3.7) | counts (%), all printed staffing levels |
| M082 | Skin closer consultant/registrar/SHO | 115 (28); 214 (52.1); 96 (23.4) | 102 (24.9); 241 (58.8); 73 (17.8) | counts (%), all printed staffing levels |
| M083 | Duration median (IQR) [n] | 120 (90-180) [408] | 120 (90-180) [405] | minutes |

## Adherence, outcomes and every Table 3 row

| ID | Exact location | Paired printed evidence and relation | Inferential context |
|---|---|---|---|
| M084 | PDF p6 Adherence; p3 Figure 1 | Allocation adherence98% both arms; as randomized404/411 and402/410; iNPWT duration≥3days or earlier discharge382/411 (93%); all7days or earlier discharge264/411 (64%) | treatment receipt/duration |
| M085 | PDF p8 Table 3 primary row | SSI112/394 (28) versus108/394 (27); absolute0.010 (−0.050 to0.071); relative1.03 (0.83 to1.28); P=.78 | M003 counts, M018 links, adjusted RD/RR, 95% CI |
| M086 | PDF p8 Table 3 UK LOS; p6 Secondary | Median(IQR)9 (7-15) versus11 (7-16) days; ratio geometric means0.91 (0.82-1.02); P=.12 | log-transformed adjusted model; UK only |
| M087 | PDF p8 Table 3 combined LOS; p1/p6 | Median(IQR)8 (6-14) versus9 (6-14.5) days; ratio geometric means0.96 (0.88-1.06); P=.21 | UK+Australia; M005/M020 |
| M088 | PDF p8 Table 3 SF-12 PCS day30 | Mean(SD)36.1 (9.8) versus37.2 (10.2); absolute difference−0.86 (−2.83 to1.11); P=.39 | adjusted mean difference; range0-100, higher better |
| M089 | PDF p8 Table 3 SF-12 MCS day30 | Mean(SD)46.9 (11.8) versus47.7 (12.0); absolute difference−1.90 (−4.28 to0.47); P=.12 | adjusted mean difference; range0-100, higher better |
| M090 | PDF p8 Table 3 pain day7; p6 Secondary/Discussion | Mean(SD)2.6 (2.1) versus3.0 (2.2); mean difference−0.41 (−0.70 to−0.12); P=.01; narrative difference0.4 points, lower iNPWT, small absolute magnitude | scale1-10 per footnote:1 no pain,10 worst; p4 visual analogue; p6 discussion10-point Likert |
| M091 | PDF p8 Table 3 pain day30 | Mean(SD)1.8 (1.5) versus1.8 (1.6); absolute difference−0.06 (−0.28 to0.16); P=.61 | same pain scale |
| M092 | PDF p8 Table 3 dressing acceptability | Mean(SD)2.5 (2.5) versus2.1 (2.2); no effect estimate/CI/P printed | scale1-10;1 completely acceptable,10 totally unacceptable; time not printed in row |
| M093 | PDF p8 Table 3 readmission; p6 Secondary | Wound-related hospital readmission11/399 (3) versus11/398 (3); absolute0.010 (−0.014 to0.034); relative1.02 (0.45 to2.31); P=.96 | adjusted RD and RR columns; within30-day narrative; denominator distinct from primary |
| M094 | PDF p8 Table 3 wound complications; p6 Secondary | Within30days73/392 (19) versus71/397 (18); absolute0.007 (−0.046 to0.060); relative1.04 (0.78 to1.39); P=.79 | wound complications excluding SSI per M015; adjusted RD/RR |
| M095 | PDF p8 Table 3 Clavien-Dindo | Grade I none/conservative/on-ward53/47; II antibiotic16/17; III radiological/surgical4/7; IV ITU0/0; V death0/0 | printed counts, not percentages; grades correspond73/71 wound complications |
| M096 | PDF p8 Table 3 SAE; p6 Safety | Participants with SAE158/411 (38) versus165/410 (40); SAE events237/259; narrative total496, >1 SAE possible per participant | descriptive safety counts, no CI/P |
| M097 | PDF p8 Table 3 mortality; p6 Safety; p10 limitations | Death within30days10/411 (2) versus14/410 (3); p6 precise2.4%/3.4%, overall3%; p10 overall30-day mortality2.9%; Figure1 footnote total25 (10/15), separately recorded M013 | explicit within30-day endpoint; no CI/P |
| M098 | PDF p6 Safety | Enterocutaneous fistula0/411 versus1/410; adverse skin reaction5/411 versus2/410 | descriptive SAE-specific counts |
| M099 | PDF p8 Table 3 footnotes a-g | All analyses adjusted minimization covariates; treatment effects RR except marked; RR<1/absolute<0 favor iNPWT; LOS geometric ratios; SF-12 scale0-100; pain/acceptability1-10; Clavien-Dindo referenced | model, effect labels, units/direction; absolute continuous rows under header Difference |
| M100 | PDF p8 Discussion assessment | In-person SSI77/214 (36%) versus78/209 (37%); video15/72 (21%) versus16/76 (21%); phone9/76 (12%) versus13/76 (17%); combined video21%, combined phone14%; overall SSI28% | source-specific fractions; linked Figure2 assessment rows, not identical numerator to all SSI cases |

## Every Figure 2 quantitative row

Location: PDF p9 Figure2. Columns explicitly are numbers of patients with SSI within30days; n=394 in each overall arm header, not printed subgroup denominators. Effects are relative risks with95% CIs. Group-level P values belong to subgroup×treatment interactions under M021, not individual row-effect tests. Axis ticks0.2,0.5,1,2,3; left of1 favors iNPWT, right favors surgeon's preference. No individual-row P values are printed. Pandemic subgroup footnote applies to UK-based patients only. Image inspection confirms line alignment and restores concatenated counts in native text.

| ID | Subgroup row | SSI events iNPWT/control | RR (95% CI) | Interaction P |
|---|---|---|---|---|
| M101 | Primary analysis | 112/108 | 1.03 (0.83-1.28) | none printed |
| M102 | Contamination clean | 18/24 | 0.75 (0.43-1.28) | .28 for contamination |
| M103 | Contamination clean-contaminated | 44/35 | 1.28 (0.87-1.89) | same interaction |
| M104 | Contamination contaminated | 29/23 | 1.20 (0.77-1.87) | same interaction |
| M105 | Contamination dirty | 21/26 | 0.84 (0.55-1.29) | same interaction |
| M106 | Stoma no | 70/59 | 1.19 (0.89-1.60) | .14 for stoma |
| M107 | Stoma yes | 42/49 | 0.86 (0.62-1.19) | same interaction |
| M108 | Bowel colonic | 60/60 | 0.96 (0.72-1.28) | .81 for procedure |
| M109 | Bowel noncolonic | 29/28 | 1.09 (0.71-1.66) | same interaction |
| M110 | Nonbowel | 23/20 | 1.14 (0.67-1.94) | same interaction |
| M111 | BMI<18.5 underweight | 5/4 | 0.93 (0.30-2.89) | .81 for BMI |
| M112 | BMI18.5-24.9 healthy | 33/37 | 0.94 (0.62-1.41) | same interaction |
| M113 | BMI25.0-29.9 overweight | 30/30 | 0.94 (0.62-1.42) | same interaction |
| M114 | BMI≥30.0 obese | 41/32 | 1.18 (0.82-1.70) | same interaction |
| M115 | Incision<15cm | 21/22 | 1.28 (0.76-2.16) | .42 for incision |
| M116 | Incision≥15cm | 90/81 | 1.01 (0.79-1.29) | same interaction |
| M117 | 2% alcoholic chlorhexidine | 51/44 | 1.10 (0.79-1.55) | .68 for preparation |
| M118 | Aqueous povidone-iodine | 19/16 | 1.15 (0.69-1.94) | same interaction |
| M119 | Other skin preparation | 42/48 | 0.92 (0.65-1.30) | same interaction |
| M120 | UK | 79/73 | 1.08 (0.83-1.40) | .52 for country |
| M121 | Australia | 33/35 | 0.92 (0.61-1.39) | same interaction |
| M122 | In-person wound visualization | 77/78 | 0.96 (0.75-1.23) | .67 for assessment |
| M123 | Remote video/image visualization | 15/16 | 1.02 (0.54-1.91) | same interaction |
| M124 | Remote without visualization | 9/13 | 0.67 (0.31-1.48) | same interaction |
| M125 | UK before March11,2020 | 60/55 | 1.11 (0.83-1.50) | .68 for pandemic |
| M126 | UK on/after March11,2020 | 19/18 | 0.98 (0.58-1.65) | same interaction |

## Remaining narrative, matching and non-applicable units

| ID | Exact location | Evidence/relationship | Quantitative relevance |
|---|---|---|---|
| M127 | PDF p6 demographic narrative | Mean age63.8, range18.8-95.3, male390 (48%); BMI27.1; ASA III-V444/821 (54%); contamination197/821 (24%),351/821 (43%),160/821 (19%),113/821 (14%) | Matching of Table1 and abstract as recorded above |
| M128 | PDF p6 Discussion; p1 conclusion; p2 Meaning; p10 Conclusion | No reduction SSI; sensitivity robust/preplanned subgroups consistent; majority secondary no difference except day7 pain; routine use unsupported | Result-to-interpretation linkage M003/M019/M021/M090 |
| M129 | PDF pp7-8 assessment discussion | Follow-up initially face-to-face; Australian opening permitted video; early2020 onward nearly all remote due pandemic; differences in method-specific SSI rates, no differential randomized-group misclassification expected | Context for M100 and assessment/pandemic subgroups |
| M130 | PDF p9 Limitations | CDC primary binary yes/no, no severity or SSI subtype detail; Clavien-Dindo all-complication scoring stated equal; no meaningful SSI severity benefit expected; assessors masked, intervention visible; children excluded | Endpoint interpretation/analysis context, no additional estimate/test |
| M131 | PDF p10 mortality limitation | Current30-day mortality2.9% compared with cited UK audit9.6%; states exclusion of unlikely30-day survivors (example ASA class5); single iNPWT product generalizability | Trial mortality linkage M097; external benchmark retained as supplied contextual claim only |
| M132 | PDF p2 Introduction | SSI after emergency laparotomy up to40%; emergency abdominal surgery9.1%-21.1% total surgical activity; iNPWT device unit cost US$150-$180; 3 bellwether procedures; 2018 guidance | Historical/context quantities, not trial-result relationships; no external checking |
| M133 | PDF p7 Discussion | Cited meta-analysis RR0.61;28 SSI-reporting RCTs,7 with>100/arm,2 of those found effective, none emergency-laparotomy-focused;2 large RCTs published2020 without benefit | Supplied historical context, no trial inferential relationship and no external checking |
| M134 | PDF p8 Table3; p4 longitudinal method | PCS/MCS day30 mean-difference estimates are longitudinal adjusted-model outputs, not raw differences in printed descriptive means; quality-of-life narrative refers supplementary eTables2-4 including EQ-5D not printed numerically in main | Matched method/result linkage; main supplies no EQ-5D estimate |
| M135 | PDF p4 secondary outcomes; p8 Table3; p1 abstract | Outcome list and status: main p4 includes complications/readmission/pain/QoL/LOS/SAE; Table3 groups Primary, Secondary, Secondary safety, SAEs and displays dressing acceptability; p1 total7 secondary outcomes | Status/definition map for report-to-plan comparison, no adjudication |
| M136 | PDF p3 Figure1; pp1/4/6/8/9 matching locations | Initial randomized840; retained821; completed day30 797; primary788. Flow arms before/after exclusion and outcome-specific denominators are individually transcribed M002/M009-M014/M085/M093-M097 | Complete population linkage across main report |
| M137 | PDF pp10-11 article information/references; all page footers | Article information, authors, conflicts/funding, citations1-23, registration identifiers, journal dates/pages, DOI, copyright/download stamps: no additional trial count/estimate/test; p11 references only | Explicit no-applicable-unit record; contextual numbers M131-M133 preserved separately |

## Locator links and evidence-transcription limits

Main-source locators from this extraction artifact are [abstract](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=1), [eligibility and Key Points](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=2), [flow](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=3), [methods](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4), [baseline](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=5), [narrative and baseline continuation](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=6), [intraoperative](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7), [outcomes](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8), [subgroups](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=9), [mortality context](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=10), and [references](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=11).

Native multicolumn order concatenates separate Figure2 counts (BMI underweight displayed as54; remote count as91 3), and moves rows out of sequence. Geometric layout and visually inspected page9 provide the separate values5/4 and9/13 and restore the exact subgroup interaction-P alignment. Figure1 native branch text similarly mixes arm order; visually inspected page3 fixes all branch attribution. These derivative reading-order ambiguities are explicitly resolved in this map and are not source diagnoses.

No standard errors, test statistics, rates per person-time, person-time denominators or additional inferential values are printed in the assigned main source. Main continuous outcome rows do not print analysis n; raw group descriptions and modeled contrasts are distinct quantities. Missing subgroup denominators are not imputed from baseline population rows. Full exact-source recheck remains mandatory for any downstream registered candidate. Legacy extraction engine versions are unavailable; this provenance limitation creates no unmapped scientific page.

Completion: 11/11 source pages mapped, 137 local relationship records, no scientific coverage gap, no fresh OCR need.
