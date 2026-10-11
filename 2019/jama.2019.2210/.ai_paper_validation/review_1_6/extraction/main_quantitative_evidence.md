# Main quantitative evidence map — Workflow 1.6

Scope: DOC-001, `jama_urashima_2019_oi_190023.pdf`, physical PDF pages 1–9, document role REPORT. Runtime UUID: 01a12865-6081-79f1-b75e-7630d977e2a1. All nine pages are reusable-backed; no fresh-required unit was assigned. This is an evidence reconstruction only, with no candidate diagnosis or adjudication. Local M keys identify mapped relationship bundles; checkers assign canonical N/S identifiers. Within each bundle all displayed components remain in scope independently.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6/review_contract.md; current source inventory, source coverage and tooling record; all DOC-001 rows of evidence-asset inventory. Source-linked layout-native locators read: `.ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/native_text/page-001.txt` through `page-008.txt`. Page 9 locator: `.ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-009.txt` (PyMuPDF, historical version unspecified). Layout-native engine unspecified in existing inventory. Reusable rendered pages 5 and 7 were visually inspected to preserve table alignment, printed direction language, Figure 3 caption and every risk row. No OCR, fallback, new derivative, source modification, or old candidate/report input was used. Direct-source recheck remains mandatory for eventual candidates.

Values below preserve printed precision. D = randomized vitamin D; P = placebo. Unless stated otherwise, comparisons are D versus P, efficacy population is randomized 251 versus 166, intervals are printed 95% CIs, and time starts at randomization. Counts and percentages are distinct from survival estimates and cumulative hazard/incidence. Table 1 genotype and baseline biomarker denominators require attention to measured/nonmissing categories rather than assumption that each is 251/166; displayed table headers nevertheless name randomized arms.

## Page completion

| Physical page | Printed page | Completed units | Source |
|---|---|---|---|
| 1 | 1361 | Entire abstract, intervention, participant/outcome/precision definitions, all repeated findings; affiliations and bibliographic identifiers have no trial quantitative relationship. | [PDF](../../../jama_urashima_2019_oi_190023.pdf#page=1) |
| 2 | 1362 | Entire introduction, Key Points, eligibility, timing, randomization, intervention and outcome definitions. | [PDF](../../../jama_urashima_2019_oi_190023.pdf#page=2) |
| 3 | 1363 | Entire follow-up/assay/SNP/sample-size/statistical-analysis text and continuation boundary. | [PDF](../../../jama_urashima_2019_oi_190023.pdf#page=3) |
| 4 | 1364 | Entire Figure 1, analysis continuation, population, all efficacy and baseline-subgroup narrative. | [PDF](../../../jama_urashima_2019_oi_190023.pdf#page=4) |
| 5 | 1365 | Both Table 1 columns, every row/footnote, subgroup narrative and post hoc continuation. | [PDF](../../../jama_urashima_2019_oi_190023.pdf#page=5) |
| 6 | 1366 | Figure 2 A–C, every printed risk row/axis/caption observation time; all post hoc, serum-change and safety text. | [PDF](../../../jama_urashima_2019_oi_190023.pdf#page=6) |
| 7 | 1367 | Table 2 all 9 estimate/CI/P triplets, 3 interactions and footnote; Figure 3 A–D all labels/risks/caption times. | [PDF](../../../jama_urashima_2019_oi_190023.pdf#page=7) |
| 8 | 1368 | Table 3 every cell and footnote; entire discussion/limitations/conclusion and supplied background study numbers. | [PDF](../../../jama_urashima_2019_oi_190023.pdf#page=8) |
| 9 | 1369 | Entire article information and references 1–32 inspected. Accepted February 18, 2019; data sharing refers Supplement 3. No new trial result number or inferential relationship. Citation years, volumes, pages, DOI/identifier strings and reference-title durations are bibliographic metadata, not trial outcomes. | [PDF](../../../jama_urashima_2019_oi_190023.pdf#page=9) |

## Population, time, endpoint and analysis definitions

| Key | Exact location | Printed quantitative relationship / definition |
|---|---|---|
| M001 | p.1 abstract design/intervention; p.2 Methods | Entry ages 30–90 years, digestive epithelial cancers esophagus through rectum, clinical stages I–III; pathological stages 0/IV excluded. 2000 IU/d vitamin D3; D n=251 and P n=166; no baseline supplementation or urinary tract stone history. Single Japanese hospital. |
| M002 | p.1 design; p.4 population | Enrollment January 2010; randomized January 2010–April 2016; follow-up ended February 2018. |
| M003 | p.2 Trial Design/Randomization | Allocation 3:2; permuted blocks of 5, no stratification. Usual discharge 5–14 days, first outpatient visit 1–2 weeks later; trial initiation described as 2–4 weeks postoperative. |
| M004 | p.2 Outcomes; p.1 abstract | Primary relapse-free survival: randomization to earliest relapse or any-cause death. Secondary overall survival: randomization to any-cause death; additional relapse, cancer-specific death, noncancer death. Safety fracture, stones, admission-level serious events, new cancer elsewhere after medication starts. |
| M005 | p.3 Follow-up | Monthly first 6 months, every 2 months second 6 months, every 3 months thereafter until 5 years; after 5 years every 3–6 months. Medication bottles every 6 months; annual 25(OH)D. Chemotherapy stage II/III esophageal/gastric and stage III colorectal. Medical stopping does not terminate follow-up. |
| M006 | p.3 Vitamin D Measurements | Radioimmunoassay; annually same calendar month. Blinded duplicates of 19 external-cohort serum samples, correlation coefficient 0.92. |
| M007 | p.3 SNP analyses | VDR FokI rs2228570, BsmI rs1544410, CDX2 rs11568820, ApaI rs7976091, TaqI rs731236; DBP1 rs7041 and DBP2 rs4588; DNA stored −80°C. Supplement 1 eAppendix 1 methods cross-reference. |
| M008 | p.3 Sample Size | Historical cohort 257 colorectal patients; highest vs lowest 25(OH)D quartile 5-year relapse-free survival 13% better. Planning survival D 75%, P 62%; 2-side type I error .05, power 80%, 1% loss; 400 randomized 3:2; 80/year, accrual 5 years, last follow-up 2 years after enrollment, total planned 7 years. These are planning/background values printed in REPORT, not observed trial estimates. |
| M009 | p.3 Statistical Analysis | All randomized included; relapse/death analyzed by randomized group regardless of adherence. Adverse events assessed per protocol. Nelson–Aalen cumulative hazards; Cox HR/95% CI; prespecified low <20, middle 20–40, high >40 ng/mL; missing baseline excluded from subgroup. Treatment, baseline group and product interaction in Cox; low vs middle only due to small high group. 2-sided P<.05; subgroup findings exploratory due to multiple comparisons. |
| M010 | p.3 statistical analysis; p.4 Results | Stata 14.0; planned annual interim analyses after 200 entries, P<.001 Peto stopping. Three interim analyses conducted; stopping rule not met; entries continued beyond 400. |
| M011 | pp.3–4 Post hoc analysis | Schoenfeld residual proportional hazards check. Relapse competing risk = deaths from causes other than relapse; subdistribution HR. Separate age-quartile or stage-I adjustment. MCMC multivariable normal imputation repeated 50 times; predictors age, sex, calcium, alkaline phosphatase and parathyroid hormone. |
| M012 | p.4 continuation; p.6 post hoc | Post hoc subgroups cancer site/stage/pathology/sex/BMI/age; mean trial 25(OH)D (baseline + annual samples) <20, 20–<30, 30–<40, 40–<50, ≥50 ng/mL independent of supplementation. Baseline-to-1-year median change Wilcoxon signed rank; arm change ratios Mann–Whitney. Matching Supplement 2 eTable 1/eFigure 1 A,B and eFigure 2. |
| M013 | p.6 subgroup paragraph | Sex men/women; age ≤65/>65 years; BMI <25/≥25; esophageal/gastric/colorectal; stage I/II/III; adenocarcinoma/nonadenocarcinoma; narrative no significant interactions. Cross-references eFigures 4–9 in Supplement 2. |

## Flow and participant narrative

| Key | Exact location | Printed relationship |
|---|---|---|
| M014 | p.1 abstract; p.4 Figure 1 | Assessed 439; excluded 22 = 15 declined, 5 inclusion criteria not met, 2 other. Abstract: 15 declined, 7 excluded after operation. Randomized 417. |
| M015 | p.4 Figure 1/population; p.1 intervention | D 251 received as randomized and included primary analysis; P 166 received/included; narrative D 60%, P 40%. |
| M016 | p.4 Figure 1 | D 1 lost within 6 months; 23 stopped medication, 14 nonmedical (3 within 1y, 9 between 1–2y, 2 after 2y), 9 medical (4 within 1y, 5 between 1–2y). |
| M017 | p.4 Figure 1 | P 19 stopped medication, 10 nonmedical (2 within 1y, 7 between 1–2y, 1 after 2y), 9 medical (4 within 1y, 5 between 1–2y). |
| M018 | p.4 population narrative | Nonmedical including lost: D 15 (6.0%), P 10 (6.0%); medical D 9 (3.6%), P 9 (5.4%); overall 10.3% stopped before censoring; all 417 efficacy. |
| M019 | p.4 population; p.1 abstract | Randomization median 23.5 (IQR 13–44) postoperative days. One lost at 1 month; follow-up 99.8%. Abstract median follow-up 3.5 (IQR 2.3–5.3) years, maximum 7.6. D 3.5 (2.3–5.4), maximum 7.6; P 3.5 (2.3–5.0), maximum 7.4 years. |
| M020 | p.1 abstract; p.4 population | Abstract all 417, mean age 66, male 66%, esophageal 10%, gastric 42%, colorectal 48%. Body all Japanese, women 34%, median age 66, median BMI 22; sites esophageal 9.6%, stomach 41.7%, small bowel 0.5%, colorectal 48.2%; stages I/II/III 44%/26%/30%. |
| M021 | p.4 population | D median age 67 (IQR 61–75), P 64 (58–71); stage I D 46%, P 40%. |
| M022 | p.4 subgroup; p.8 limitation | Baseline low n=173, middle n=232, high n=5; high not further analyzed. Seven missing 25(OH)D pp.6/8; imputed results consistent, Supplement 2 eTable 2. |

## Table 1 complete cells

Every following row is p.5 Table 1, header No. (%) of Participants; vitamin D (n=251), placebo (n=166). Each pair is printed `count (percentage)`; percent sign omitted in cells as in source. Age in y; baseline biomarker ng/mL. No P, CI or test statistic is displayed in Table 1.

| Key | Row label | D | P |
|---|---|---|---|
| M023 | Male | 173 (69) | 103 (62) |
| M024 | Female | 78 (31) | 63 (38) |
| M025 | Age quartile 35–59 y | 51 (20) | 50 (30) |
| M026 | Age quartile 60–65 y | 55 (22) | 41 (25) |
| M027 | Age quartile 66–73 y | 63 (25) | 48 (29) |
| M028 | Age quartile 74–90 y | 82 (33) | 27 (16) |
| M029 | BMI quartile 15.0–19.7 | 63 (25) | 36 (22) |
| M030 | BMI quartile 19.8–21.8 | 62 (25) | 43 (26) |
| M031 | BMI quartile 21.9–23.7 | 59 (24) | 45 (27) |
| M032 | BMI quartile 23.8–37.3 | 65 (26) | 41 (25) |
| M033 | History of other cancers | 9 (4) | 7 (4) |
| M034 | Hypertension | 103 (41) | 58 (35) |
| M035 | Diabetes mellitus | 44 (18) | 24 (14) |
| M036 | Endocrine disease | 33 (13) | 18 (11) |
| M037 | Cardiovascular disease | 22 (9) | 9 (5) |
| M038 | Chronic kidney disease | 5 (2) | 1 (1) |
| M039 | Asthma | 3 (1.2) | 0 (0.0) |
| M040 | Orthopedic disease | 1 (0.4) | 1 (0.6) |
| M041 | Site: esophagus | 22 (9) | 18 (11) |
| M042 | Site: stomach | 106 (42) | 68 (41) |
| M043 | Site: small bowel | 1 (0.4) | 1 (0.6) |
| M044 | Site: colorectal | 122 (49) | 79 (48) |
| M045 | Cancer stage I | 115 (46) | 67 (40) |
| M046 | Cancer stage II | 63 (25) | 48 (29) |
| M047 | Cancer stage III | 73 (29) | 51 (31) |
| M048 | Adenocarcinoma | 226 (90) | 147 (88) |
| M049 | Squamous cell carcinoma | 22 (9) | 16 (10) |
| M050 | Other pathology | 3 (1) | 3 (2) |
| M051 | Baseline 25(OH)D low <20 | 102 (41) | 71 (44) |
| M052 | Baseline 25(OH)D middle 20–40 | 142 (58) | 90 (56) |
| M053 | Baseline 25(OH)D high >40 | 4 (1.6) | 1 (0.6) |
| M054 | Adjuvant chemotherapy | 88 (35) | 60 (36) |
| M055 | FokI CC | 92 (38) | 57 (36) |
| M056 | FokI CT | 117 (48) | 75 (48) |
| M057 | FokI TT | 36 (15) | 25 (16) |
| M058 | BsmI AA | 14 (6) | 8 (5) |
| M059 | BsmI AG | 42 (18) | 23 (15) |
| M060 | BsmI GG | 175 (76) | 119 (79) |
| M061 | Cdx2 GG | 89 (39) | 49 (33) |
| M062 | Cdx2 GA | 103 (45) | 77 (51) |
| M063 | Cdx2 AA | 38 (17) | 24 (16) |
| M064 | ApaI GG | 96 (42) | 69 (46) |
| M065 | ApaI GT | 104 (45) | 61 (40) |
| M066 | ApaI TT | 31 (13) | 20 (13) |
| M067 | TaqI TT | 172 (74) | 115 (77) |
| M068 | TaqI TC | 54 (23) | 31 (21) |
| M069 | TaqI CC | 5 (2) | 4 (3) |
| M070 | DBP1 TT | 134 (58) | 82 (55) |
| M071 | DBP1 TG | 87 (38) | 57 (39) |
| M072 | DBP1 GG | 10 (4) | 9 (6) |
| M073 | DBP2 CC | 115 (50) | 81 (54) |
| M074 | DBP2 CA | 91 (39) | 58 (39) |
| M075 | DBP2 AA | 25 (11) | 11 (7) |
| M076 | Footnote a | Percentages may not sum to 100% because of rounding. | Applies both arms. |
| M077 | Footnote b | BMI = kg divided by m squared. | Applies both arms. |
| M078 | Footnote c | Neuroendocrine tumor n=4; adenoid cystic carcinoma n=1; unclassified n=1. | Other pathology types stated jointly. |

## Efficacy counts, survival and inferential relationships

All displayed HRs below are D compared with P per main methods and intervention statements. Directly stated interpretation and null/significance language are retained without assessment. No standard errors or numerical test statistics are printed.

| Key | Exact location and matching occurrence | Population / endpoint | Printed values and model |
|---|---|---|---|
| M079 | p.1 Results; p.4 efficacy | All randomized, relapse or death | D 50 (20%), P 43 (26%). |
| M080 | p.1 Results; p.4 efficacy | All randomized, any-cause death | D 37 (15%) of 251, P 25 (15%) of 166. |
| M081 | p.4 efficacy | All randomized, relapse | D 41 (16%), P 36 (22%). |
| M082 | p.4 efficacy | All randomized, cancer-specific death | D 27 (11%), P 16 (10%). |
| M083 | p.4 efficacy | All randomized, noncancer death | D 10 (4%), P 9 (5%). |
| M084 | p.1 abstract; p.2 Key Points; p.4 efficacy; p.6 Figure 2A | All randomized, 5-year relapse-free survival and relapse/death Cox HR | D 77%, P 69%; HR 0.76 (0.50–1.14), P=.18; narrative not significant; abstract/conclusion p.8 same interpretation at 5 years. |
| M085 | p.1 abstract; p.4 efficacy; p.6 Figure 2B | All randomized, 5-year overall survival and death Cox HR | D 82%, P 81%; HR 0.95 (0.57–1.57), P=.83. |
| M086 | p.6 narrative/Figure 2C; p.7 Table 2 | All randomized, relapse competing risk | Subdistribution HR 0.75 (0.48–1.17), P=.21; death other than relapse competing risk. |
| M087 | p.1 abstract; p.4 subgroup; p.7 Figure 3A | Middle baseline 20–40 ng/mL, relapse/death | D 5-year relapse-free survival 85%, P 71%; HR 0.46 (0.24–0.86), P=.02; higher survival narrative. |
| M088 | p.4 subgroup; p.7 Figure 3B | Low baseline <20 ng/mL, relapse/death | HR 1.15 (0.65–2.05); Figure P=.63; narrative no significant difference. |
| M089 | p.1 abstract; p.5 subgroup continuation | Relapse/death treatment-by-middle/low interaction | P=.04, 2-way Cox interaction. |
| M090 | p.5 subgroup; p.7 Figure 3C | Middle baseline, death | HR 0.60 (0.28–1.30); Figure P=.20; no significant difference narrative. |
| M091 | p.5 subgroup; p.7 Figure 3D | Low baseline, death | HR 1.36 (0.66–2.81); Figure P=.41; no significant difference narrative. |
| M092 | p.5 subgroup | Death treatment-by-middle/low interaction | P=.13. SNP subgroup associations not significant, Supplement 2 eFigure 3 A–U. |
| M093 | p.6 competing risk; p.7 Table 2 | Low baseline, relapse | Subdistribution HR 1.18 (0.64–2.19), Table P=.59; no significant difference narrative. |
| M094 | p.6 competing risk; p.7 Table 2 | Middle baseline, relapse | Subdistribution HR 0.44 (0.21–0.89), P=.02; lower cumulative incidence narrative. |
| M095 | p.6 competing risk; p.7 Table 2 | Relapse treatment-by-middle/low interaction | P=.04. |
| M096 | p.7 Table 2 | All randomized cancer-specific death | HR 1.09 (0.58–2.01), P=.80. |
| M097 | p.7 Table 2 | Low baseline cancer-specific death | HR 1.45 (0.63–3.38), P=.38. |
| M098 | p.7 Table 2 | Middle baseline cancer-specific death | HR 0.78 (0.29–2.10), P=.63. |
| M099 | p.7 Table 2 | Cancer-specific death treatment-by-middle/low interaction | P=.35. |
| M100 | p.7 Table 2 | All randomized noncancer death | HR 0.70 (0.29–1.73), P=.44. |
| M101 | p.7 Table 2 | Low baseline noncancer death | HR 1.11 (0.26–4.65), P=.89. |
| M102 | p.7 Table 2 | Middle baseline noncancer death | HR 0.39 (0.11–1.39), P=.15. |
| M103 | p.7 Table 2 | Noncancer death treatment-by-middle/low interaction | P=.27. |
| M104 | p.7 Table 2 footnote a, exact printed text | Effect direction label | “Hazard ratio (HR) values greater than 1 indicate that vitamin D supplementation was associated with a decreased probability of the outcome.” |
| M105 | p.6 age-adjusted narrative | All randomized relapse/death, age-quartile adjusted Cox | Adjusted HR 0.66 (0.43–0.99), P=.048; significantly less cumulative hazard. |
| M106 | p.6 age-adjusted narrative | All randomized death, age-quartile adjusted Cox | Adjusted HR 0.81 (0.48–1.36), P=.42; no significant difference. |
| M107 | p.6 narrative pp.5–6 continuation | PH test, stage-I adjustment, imputation | PH-assumption test not significant, no number; stage-I adjustment no significant differences, no estimates; imputation results consistent, 7 missing baseline, see Supplement 2 eTable 2. |

## Figures: all printed risk counts, scales, captions and observation times

Risk arrays follow years 0,1,2,3,4,5,6 after randomization, in order. These are at-risk counts, not outcome totals. Continuous curve traces have no independently labeled event probabilities beyond axes and inference annotations; no numerical values have been invented by digitization.

| Key | Location | Printed mapping |
|---|---|---|
| M108 | p.6 Figure 2A | Cumulative Hazard of Relapse or Death; y ticks 0,.2,.4,.6,.8; D orange lower trace, P dark upper; HR/P in M084; P risks 166,148,113,84,54,34,16; D 251,222,176,130,93,65,35. |
| M109 | p.6 Figure 2B | Cumulative Hazard of Death; y ticks 0,.2,.4,.6,.8; D/P traces labeled, HR/P M085; P risks 166,160,128,94,62,42,20; D 251,245,196,145,104,73,37. |
| M110 | p.6 Figure 2C | Cumulative Incidence of Relapse, competing-risk analysis; y ticks 0,.2,.4,.6,.8; D orange lower, P dark upper; subdistribution HR/P M086; no risk table displayed. |
| M111 | p.6 Figure 2 caption | Nelson–Aalen A/B, C competing death other than relapse. Relapse/death median observation P 3.0 (IQR 1.9–4.5), D 3.3 (1.9–5.3) years. Death median P 3.5 (2.3–5.0), D 3.5 (2.3–5.4). Competing relapse median P 3.0 (1.9–4.5), D 3.3 (1.9–5.3). |
| M112 | p.7 Figure 3A | Middle 20–40 ng/mL, cumulative hazard relapse/death; y ticks 0,.1,.2,.3,.4,.5; D orange lower/P dark upper; HR/P M087; P risks 90,83,63,49,30,18,9; D 142,132,111,85,58,38,20. |
| M113 | p.7 Figure 3B | Low <20 ng/mL, cumulative hazard relapse/death; same axes; D orange upper/P dark lower terminal traces; HR/P M088; P risks 71,61,46,31,20,13,5; D 102,84,61,43,33,26,15. |
| M114 | p.7 Figure 3C | Middle 20–40 ng/mL, cumulative hazard death; same axes; D orange lower/P dark upper; HR/P M090; displayed P risks 90,88,70,51,34,22,11; D 142,139,115,88,61,41,20. |
| M115 | p.7 Figure 3D | Low <20 ng/mL, cumulative hazard death; same axes; D orange upper/P dark lower terminal; HR/P M091; P risks 71,68,54,39,24,17,7; D 102,100,75,54,40,31,17. |
| M116 | p.7 Figure 3 caption | A/B Nelson–Aalen relapse/death, C/D total deaths, only 5 high >40 ng/mL not evaluated. Exact additional caption statement: “Numbers at risk for panel C are not given because of weighting.” Both statement and displayed C risk row preserved. |
| M117 | p.7 Figure 3 caption | Middle relapse/death median P 3.4 (IQR 1.9–4.5), D 3.8 (2.4–5.3) years. Low relapse/death P 2.8 (1.8–4.4), D 2.5 (1.6–5.2). Middle total deaths P 3.5 (2.3–5.0), D 3.8 (2.5–5.4). Low total deaths P 3.4 (2.1–5.0), D 3.3 (1.9–5.4). |

## Biomarker changes and statistical tests

Tests are Wilcoxon signed rank for within-arm baseline→1-year medians and Mann–Whitney for between-arm change ratios (M012). Serum units and distinct subgroup/overall populations retained. No test statistic or SE printed.

| Key | Location | Printed values |
|---|---|---|
| M118 | p.4 subgroup narrative | D middle baseline 25(OH)D median 26.5 (IQR 23–30) ng/mL →45 (36–57) at 1 year; D low 16 (13–18)→36 (27–47); Supplement 2 eFigure 2. |
| M119 | p.6 changes | D overall 25(OH)D median 21 (16–27)→41 (33–55) ng/mL, P<.001. P overall 21 (15–27)→20 (15–27), P=.91. |
| M120 | p.6 changes | 1-year 25(OH)D change ratio D 87%, P 0%, P<.001; D high sustained over 4 years, P low, Supplement 2 eFigure 2. |
| M121 | p.6 changes | D calcium median 9.3 (8.9–9.6)→9.3 (9.1–9.6) mg/dL, P=.09. P calcium 9.3 (9.0–9.6)→9.3 (9.1–9.5), P=.44. |
| M122 | p.6 changes | Calcium change ratio D 0%, P 0%, P=.10. |

## Table 3 complete safety outcomes

All rows p.8 Table 3 No. (%) of Participants. Columns per protocol adherent until censoring D n=227/P n=147; per protocol adherent for 1 y D n=243/P n=160; randomized D n=251/P n=166. Each below is count (percentage); no inferential test displayed. Abstract p.1 and p.6 narrative repeat adherent-until-censoring fractures and stones only.

| Key | Outcome | Until censoring D / P | For 1 y D / P | Randomized D / P |
|---|---|---|---|---|
| M123 | Fracture | 3 (1.3) / 5 (3.4) | 3 (1.2) / 6 (3.8) | 3 (1.2) / 6 (3.6) |
| M124 | Urinary stones | 2 (0.9) / 0 (0.0) | 4 (1.6) / 2 (1.3) | 4 (1.6) / 4 (2.4) |
| M125 | Severe adverse events | 19 (8.4) / 9 (6.1) | 20 (8.2) / 13 (8.1) | 21 (8.4) / 15 (9.0) |
| M126 | Cancer de novo | 15 (6.6) / 8 (5.4) | 16 (6.6) / 9 (5.6) | 16 (6.4) / 9 (5.4) |
| M127 | Table 3 footnote a | Until censorship or for more than 1 year defines per protocol; one D lost patient considered nonadherent. | Sensitivity-for-safety rationale printed. | No statistical test supplied. |
| M128 | Table 3 footnotes b,c,d | b randomized regardless of adherence; c admission-requiring adverse events; d cancer in organs other than primary site after starting medication. | Applies all outcome rows. | Applies all outcome rows. |
| M129 | p.1 abstract/p.6 Adverse Events | Fracture D 3 (1.3%), P 5 (3.4%); stones D 2 (0.9%), P 0, per protocol until censoring. No patients developed hypercalcemia during follow-up. | Repetitions of M123/M124 and zero hypercalcemia statement. | Follow-up hypercalcemia population not further quantified. |

## Discussion and background numbers supplied in REPORT

These are source statements about external studies, recorded without consulting those publications or transferring their populations into this trial.

| Key | Location | Printed quantitative statement |
|---|---|---|
| M130 | p.2 introduction | In 1989 colon-cancer risk estimated 70% lower for serum 25(OH)D ≥20 vs <20 ng/mL. Prior primary-prevention calcium/vitamin D trial 400 IU/d for 7 years null for colorectal incidence; another 1100 IU/d lower incidence in postmenopausal women. Subgroup cutoffs 20 and 40 ng/mL. |
| M131 | p.8 discussion | Prior lung-cancer RCT 155 patients, 1200 IU/d, did not improve relapse-free/overall survival. Observational meta-analysis 64 studies, 44 165 patients; individual participant meta-analysis 8 cohorts Europe/US and lowest quintiles. |
| M132 | p.8 discussion | VITAL primary prevention dosage 2000 IU/d, 25 871 participants without cancer history; mortality null, post hoc early-follow-up exclusion suggestion. Meta-analysis 3 other RCTs significant lower total cancer mortality although each null. No HR/CI/P printed for these background claims. |
| M133 | p.8 discussion/limitations | Middle 20–40 ng/mL benefit interpreted exploratory with multiple testing and null primary outcomes; dosage 2000 IU/d possibly insufficient low group. Safety not powered for differences. Clinical surveillance every 1–6 months; approximately 10% stopped, self-reported adherence; only 5 high baseline and 7 missing; cutoffs 20/40 ng/mL; conclusion no significant improvement in relapse-free survival at 5 years. |
| M134 | p.9 article information/references | Accepted February 18, 2019; Supplement 3 data-sharing cross-reference; references 1–32 and funding/authorship statements contain no new trial numeric relationship. Reference citation metadata are explicitly no-applicable quantitative-result units. |

## Completion and handoff

Mapped pages 9/9; reusable-backed 9; fresh-required 0; scientific gaps 0. Relationship bundles M001–M134: 134, covering every printed main-paper quantitative component and repeated occurrence, all Table 1/2/3 rows, Figure 1/2/3 panels and captions. Canonical N/S IDs must be assigned by reviewers at the relationship granularity they require; this map intentionally retains bundles rather than treating a row count as a finding count. No candidate IDs, verdicts or classification conclusions are generated here. No person-time incidence-rate denominator, numerical standard error, numerical test statistic, or mean dispersion is reported in the main paper; the abstract mean age 66 lacks dispersion and is not converted to the body's median. Continuous curve values beyond printed coordinates are not digitized. No display-zero P value appears in the mapped main-paper printed results. Derivative metadata engines/versions remain historical unspecified where inventory so states; this is a preprocessing metadata limitation, not missing scientific coverage.
