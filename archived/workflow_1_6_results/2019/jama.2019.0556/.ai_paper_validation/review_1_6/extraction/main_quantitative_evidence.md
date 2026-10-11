# Main quantitative evidence map — Workflow 1.6

Scope: DOC-001, `jama_bot_2019_oi_190007.pdf`, physical PDF pages 1–11 (printed pages 858–868). Document role: REPORT throughout. All 11 reusable-backed pages were newly mapped; fresh-required pages: zero. This is an evidence reconstruction, without candidate diagnosis or adjudication. Local mapping keys M001–M120 identify 120 disjoint relationship groups; compound groups retain every printed member. Numeric/statistical reviewers assign global N/S tracking IDs and may split compound groups.

Source links below are relative to this extraction file. Main source: [DOC-001](../../../jama_bot_2019_oi_190007.pdf#page=1). Reused locators: `.ai_paper_validation/document_outputs/DOC-001/normalized_text/page_001.txt` through `page_011.txt` (native PyMuPDF extraction); reusable CPU Tesseract OCR for pp.3,5,6,7,8; reusable PyMuPDF 180-dpi rendered pages for pp.3,5,6,7,8. The five reusable images were visually inspected for table, plot, inequality and footnote alignment. Source-matched native text was read on every page. Native text drops some ≥ signs: the visually displayed signs are preserved below. Fresh alignment derivative: `.ai_paper_validation/review_1_6/preprocessing/main-layout-001-011.txt`, direct Poppler pdftotext 26.01.0, command `pdftotext -layout -f 1 -l 11 jama_bot_2019_oi_190007.pdf .ai_paper_validation/review_1_6/preprocessing/main-layout-001-011.txt`. No fresh OCR, GPU, external evidence, old candidate records, or old report conclusions used.

## Population, interventions and methods

| Key | Source location | Exact quantitative relationship and definitions | Matching key / locator |
|---|---|---|---|
| M001 | [p.1 abstract design](../../../jama_bot_2019_oi_190007.pdf#page=1); p.2 Methods | Multicenter 2 × 2 factorial trial; 4 European countries; 1025 adults; randomization July 30, 2015–October 12, 2016; 1-year follow-up ending October 13, 2017. Trial conducted July 30, 2015–October 13, 2017. | M004, M010, M017, M118 |
| M002 | p.1 abstract; [p.2 eligibility](../../../jama_bot_2019_oi_190007.pdf#page=2) | BMI 25–40 kg/m²; age 18–75 years; PHQ-9 ≥5; no current MDD episode in past 6 months (MINI 5.0). BMI calculated kg / m². | M018, M066; supplement eligibility |
| M003 | pp.1–2 interventions | Daily 1412 mg omega-3 EPA/DHA PUFAs, ratio 3:1; selenium 30 μg; folic acid 400 μg; vitamin D3 20 μg plus calcium 100 mg. Supplement or placebo: 2 pills/day for 1 year. | supplement intervention composition |
| M004 | p.1 abstract intervention; p.6 Results; p.3 Figure 1 | Four allocation groups: placebo without therapy 257; placebo with therapy 256; supplements without therapy 256; supplements with therapy 256. | M017–M033, M038–M063 |
| M005 | p.2 Randomization | Equal randomization probability; permuted blocks sized 8–12; stratified by site and lifetime depression history. Participants, therapists, researchers blinded to supplements; researchers assessing outcomes blinded to therapy; primary and reported randomized secondary analyses blinded to randomization. | M013, M078 |
| M006 | [p.4 therapy](../../../jama_bot_2019_oi_190007.pdf#page=4) | Maximum 21 therapy sessions: 15 individual + 6 group over 1 year; no active attention control in no-therapy group. | M072, M113 |
| M007 | p.1 abstract outcome; p.4 Primary Outcome | Primary outcome cumulative 12-month MDD episode onset; DSM-IV criteria, MINI 5.0 depression section at 3, 6, 12 months. | M074–M085 |
| M008 | p.4 Secondary Outcomes | PHQ-9 range 0–27; IDS30-SR range 0–84; GAD-7 range 0–21; higher = more severe. EQ-5D-5L utility England value set stated range 0–1, higher = better utility. Other trial outcomes: TEFQ-R18 3 factors each 0–100 higher = poorer eating behavior; GA2LEN food frequency, SQUASH activity/sedentary behavior, body-weight perception. Main paper reports mental-health secondary outcomes only. | M054–M069, M086–M110 |
| M009 | p.4 Other Measures | A priori good adherence: attending ≥8 of 21 therapy sessions; taking ≥70% supplements during 12 months. | M072, M112, M113 |
| M010 | p.4 Sample Size | Prior effective prevention reduction 25%–50%; assumed MDD onset 20% active versus 30% control, 33% relative reduction, 10% absolute difference; printed required sample “392 participants (196 in each of the 4 possible intervention combinations)”; main effect of each intervention versus respective control; 2-sided α=.05, power (1−β)=.90; attrition 22%; 250 per intervention combination. | PLAN sample-size calculations; no normalization of printed wording |
| M011 | p.4 Statistical Methods | All randomized participants analyzed according to randomized group regardless intervention received/withdrawal. Intervention variables effect coded −1 control, +1 intervention, jointly modeled main effects and interaction. All analyses adjusted site and history MDD. Missing endpoints assumed MAR, 100 imputed data sets, Rubin pooling. | M074–M083, M100 |
| M012 | p.4 Statistical Methods | Primary logistic regression; post hoc Cox time to first MDD onset, event/censoring time 3/6/12 months or last available measure; scaled Schoenfeld proportionality test P>.05. | M074–M085 |
| M013 | p.4 Statistical Methods | Secondary GEE longitudinal ANCOVA, exchangeable correlation; outcomes at 3/6/12 months; adjusted corresponding baseline value; overall follow-up and 12-month effects; exploratory interpretation due to multiple comparisons. Effect modification site/history using intervention interactions; baseline severity post hoc. | M091–M111 |
| M014 | pp.4–6 methods continuation | Sensitivity GEE ANCOVA without imputation; Cohen D from baseline/12-month group differences using imputed data; CACE using imputed structural equation modeling in STATA, accounting good adherence for primary and 12-month secondary outcomes. | M103, M112 |
| M015 | [p.6 Methods continuation](../../../jama_bot_2019_oi_190007.pdf#page=6) | R 3.4.4; geepack GEE, mice multiple imputation; 2-sided significance threshold P=.05. | all inferential results |
| M016 | p.2 Introduction; p.9 Discussion | Context only: MDD lifetime prevalence 17%, second leading contributor years lived with disability; p.9 review of 9 vitamin D RCTs. These are supplied narrative background, not current trial outcomes. | background claims, no external lookup |

## Figure 1 flow: complete reconstruction

[Physical p.3, printed p.860](../../../jama_bot_2019_oi_190007.pdf#page=3). Arm order below follows the figure, unlike Table 1: ST=supplements+therapy; S=supplements alone; PT=placebo+therapy; P=placebo alone. No unprinted zero is inserted for absent unknown-reason rows.

| Key | Figure node / row | Printed values |
|---|---|---|
| M017 | Overall online screening and subsequent steps | 5965 online; 3730 excluded; 2235 eligible telephone; 462 excluded/no telephone screening; 1773 completed telephone; 523 excluded; 1250 eligible baseline; 225 unwilling/unable; 1025 randomized. Repeated p.6 description: 5965,2235,1773,1250,1025. |
| M018 | Online exclusion reasons, first four | 1451 BMI <15 or >40; 623 antidepressant use past 6 mo; 591 no contact information; 566 PHQ <5. Preserve the printed BMI <15 threshold. |
| M019 | Online exclusion reasons, remaining | 268 PHQ missing; 220 none of questions answered; 11 age <18 or >75 y. |
| M020 | Telephone exclusions, first four | 259 current depressive disorder; 97 antidepressant or psychological therapy last 6 mo; 44 supplements prescribed/not willing stop; 38 psychiatric disorder. |
| M021 | Telephone exclusions, middle four | 26 not prepared visit study center; 18 BMI <25; 15 pregnant/planning pregnancy; 12 other mood disorder. |
| M022 | Telephone exclusions, last three | 7 bariatric surgery; 4 did not understand study information; 3 severe medical disease. |
| M023 | Randomized, received intervention, primary analysis | Each of these three rows: ST 256; S 256; PT 256; P 257. |
| M024 | MDD measurement month 3 | ST 209; S 202; PT 215; P 205. |
| M025 | MDD measurement month 6 | ST 193; S 185; PT 197; P 196. |
| M026 | MDD measurement month 12 | ST 191; S 194; PT 198; P 196. |
| M027 | Cumulative loss to follow-up | ST 65; S 62; PT 58; P 61. |
| M028 | No time/not interested | ST 25; S 18; PT 21; P 19. |
| M029 | Lost contact | ST 12; S 17; PT 17; P 17. |
| M030 | Physical health | ST 8; S 8; PT 7; P 10. |
| M031 | Mental health | ST 3; S 3; PT 3; P 5. |
| M032 | Other | ST 17; S 13; PT 10; P 9. |
| M033 | Unknown | S 3; P 1. ST and PT do not print this row. |
| M034 | Figure 1 footnote a | Psychiatric disorders: bipolar, schizophrenia, psychosis, eating/anxiety disorder, alcohol/drug/substance addiction. |
| M035 | Figure 1 footnotes b/c | Cumulative loss defined no MDD measurement at month 12. Primary analysis all randomized regardless treatment/withdrawal; missing data multiple imputed. |
| M036 | p.1 abstract completion | 779 (76%) completed trial. | 
| M037 | p.1 abstract overall characteristics | Mean age 46.5 y; 772 women (75%); mean BMI 31.4. Matches weighted baseline arm characteristics below. |

## Table 1: every baseline row and footnote

[Physical p.5, printed p.862](../../../jama_bot_2019_oi_190007.pdf#page=5). Columns use Table 1 order: P=placebo/no therapy n=257; PT=placebo/therapy n=256; S=supplement/no therapy n=256; ST=supplement/therapy n=256. Values are counts (%) unless labeled mean(SD) or median(IQR). No baseline comparison P values printed.

| Key | Row | P | PT | S | ST |
|---|---|---|---|---|---|
| M038 | Men | 77 (30.0) | 63 (24.6) | 63 (24.6) | 50 (19.5) |
| M039 | Women | 180 (70.0) | 193 (75.4) | 193 (75.4) | 206 (80.5) |
| M040 | Age y mean(SD) | 45.7 (13.2) | 46.1 (12.8) | 47.2 (13.3) | 47.1 (12.7) |
| M041 | Age y median(IQR) | 47 (36–55) | 47 (37–55) | 48 (38–58) | 47 (38–56) |
| M042 | Germany | 70 (27.2) | 67 (26.2) | 69 (27.0) | 71 (27.7) |
| M043 | United Kingdom | 64 (24.9) | 63 (24.6) | 64 (25.0) | 63 (24.6) |
| M044 | Spain | 64 (24.9) | 64 (25.0) | 62 (24.2) | 62 (24.2) |
| M045 | Netherlands | 59 (23.0) | 62 (24.2) | 61 (23.8) | 60 (23.4) |
| M046 | Education low | 25 (9.7) | 21 (8.2) | 31 (12.1) | 26 (10.2) |
| M047 | Education middle | 124 (48.2) | 141 (55.1) | 120 (46.9) | 113 (44.1) |
| M048 | Education high | 108 (42.0) | 94 (36.7) | 105 (41.0) | 117 (45.7) |
| M049 | History MDD | 83 (32.3) | 89 (34.8) | 88 (34.4) | 83 (32.4) |
| M050 | ≥2 episodes | 59 (23.0) | 53 (20.7) | 62 (24.2) | 58 (22.7) |
| M051 | Current smoker | 53 (20.6) | 50 (19.5) | 35 (13.7) | 47 (18.4) |
| M052 | Alcohol drinks/wk median(IQR) | 1.0 (0.2–3.7) | 1.0 (0.2–3.7) | 1.0 (0.2–3.7) | 1.0 (0.2–3.7) |
| M053 | Activity h/d median(IQR) | 7.8 (6.1–9.5) | 7.8 (5.6–10.0) | 7.9 (5.9–10.2) | 7.5 (5.3–9.7) |
| M054 | BMI mean(SD) | 31.4 (4.1) | 31.2 (3.9) | 31.3 (4.0) | 31.7 (3.9) |
| M055 | PHQ-9 mean(SD) | 7.3 (4.1) | 7.3 (4.4) | 7.9 (4.4) | 7.1 (4.0) |
| M056 | PHQ-9 median(IQR) | 7 (4–10) | 6 (4–10) | 7 (5–10) | 6 (4–9) |
| M057 | IDS mean(SD) | 21.3 (9.8) | 21.6 (10.5) | 22.8 (10.2) | 21.4 (9.8) |
| M058 | IDS median(IQR) | 20 (14–27) | 21 (13–29) | 21 (15–30) | 20 (14–28) |
| M059 | GAD anxiety mean(SD) | 5.8 (4.4) | 6.2 (4.5) | 5.7 (3.8) | 5.4 (3.8) |
| M060 | GAD anxiety median(IQR) | 5 (3–7) | 5 (3–9) | 5 (3–7) | 5 (3–7) |
| M061 | Utility mean(SD) | 0.87 (0.11) | 0.86 (0.13) | 0.86 (0.12) | 0.86 (0.12) |
| M062 | Utility median(IQR) | 0.88 (0.82–0.94) | 0.87 (0.81–0.95) | 0.87 (0.81–0.94) | 0.88 (0.81–0.94) |
| M063 | Diet score mean(SD) | 51.7 (7.6) | 51.9 (6.9) | 51.6 (6.8) | 51.4 (6.9) |
| M064 | Prior supplement use | 77 (30.0) | 86 (33.6) | 78 (30.5) | 79 (30.9) |

| Key | Exact Table 1 footnote mapping |
|---|---|
| M065 | a: Low education no/primary/lower secondary; middle upper secondary/postsecondary nontertiary/short-cycle tertiary; high bachelor’s degree or higher/equivalent. b: Activity hours/day commuting walking/cycling plus work, household, leisure and sport. |
| M066 | c: PHQ-9 higher worse, range 0–27; ≥5 mild, ≥10 moderate. d: IDS higher worse, range 0–84; ≥14 mild, ≥26 moderate. e: GAD-7 higher worse, range 0–21; ≥5 mild, ≥10 moderate. |
| M067 | f: Utility higher better, range 0–1; 0 death, 1 full health; England tariff country-specific preference algorithm on EQ5D5L states. |
| M068 | g: Diet score higher better Mediterranean adherence, range 0–77; 11 components; median vegetables 2.8/day, fruit 1.9/day, fish 1.5/week, legumes/pulses 1/week, meat 5/week, whole grains 67% total grains. |
| M069 | g continued: low-fat dairy 0.9/day, olive oil 33% total dressings/cooking oils/fats, soft drinks 0.14/day, processed food 1.6/day, alcohol 0.14/day. |

## Attrition and adherence narrative

[Physical p.6 Results](../../../jama_bot_2019_oi_190007.pdf#page=6).

| Key | Printed relationship and matching scope |
|---|---|
| M070 | Missing MDD follow-up: 194 (19%) at 3 mo, 254 (25%) at 6 mo, 246 (24%) at 12 mo. Total 239 (23%) dropped out before 12-mo follow-up or before MDD onset. Compare M024–M027 and Table 2 dropout definition M078. |
| M071 | Missing-rate comparisons across 4 arms: P=.47 at 3 mo; .62 at 6 mo; .91 at 12 mo. Secondary questionnaire missing baseline 29–32; 3 mo 206–211; 6 mo 275–278; 12 mo 268; narrative no arm difference, no further P printed. Compare Figure 2 M086–M089. |
| M072 | Among all 12-month follow-up participants pill-weight data: 77% adherence “more than 70%”; therapy randomized: 71% attended ≥8 of 21 sessions; individual sessions median 14/15, IQR 6–15; group sessions median 0/6, IQR 0–4. Compare a priori ≥70% M009 and supplement eAppendix 8. |
| M073 | MDD total 105 (10%) across 12 mo; four arms P 25 (9.7%), PT 26 (10.2%), S 32 (12.5%), ST 22 (8.6%) at pp.1,6–7. Exact denominators M004; p.2 Key Points marginal onset supplement 54 (10.5%) vs placebo 51 (9.9%), therapy 48 (9.4%) vs no therapy 57 (11.1%). |

## Table 2: every primary and post hoc row

[Physical p.6 Table 2](../../../jama_bot_2019_oi_190007.pdf#page=6). All confidence intervals 95%; pooled multiple-imputation models adjust interventions/site/history; effect codes −1,+1. Values below are reported coefficients labeled OR/HR, not independently recomputed arm contrasts. Reference rows and interaction NA are retained.

| Key | Endpoint / row | Patients or person-months | Events | Dropouts | Reported estimate (95% CI) | P |
|---|---|---:|---:|---:|---|---|
| M074 | 12-mo MDD placebo | 513 patients | 51 | 113 | 1 [Reference] | blank |
| M075 | 12-mo MDD supplements | 512 patients | 54 | 126 | OR 1.06 (0.87–1.29) | .57 |
| M076 | 12-mo MDD no therapy | 513 patients | 57 | 122 | 1 [Reference] | blank |
| M077 | 12-mo MDD therapy | 512 patients | 48 | 117 | OR 0.93 (0.76–1.13) | .47 |
| M078 | 12-mo MDD supplements by therapy | NA | NA | NA | OR 0.93 (0.76–1.14) | .48 |
| M079 | Time-to-MDD placebo | 4656 person-months | 51 | 113 | 1 [Reference] | blank |
| M080 | Time-to-MDD supplements | 4488 person-months | 54 | 126 | HR 1.05 (0.86–1.27) | .65 |
| M081 | Time-to-MDD no therapy | 4503 person-months | 57 | 122 | 1 [Reference] | blank |
| M082 | Time-to-MDD therapy | 4641 person-months | 48 | 117 | HR 0.91 (0.75–1.10) | .32 |
| M083 | Time-to-MDD supplements by therapy | NA | NA | NA | HR 0.91 (0.75–1.11) | .36 |

M074–M083 footnotes: a, dropouts are those not completing 12 mo and having no MDD at preceding measurements; b, multiple-imputed data, model adjustment interventions/site/history, therapy and pills effect-coded (−1,1); c, 25/257 (9.7%) placebo/no therapy plus 26/256 (10.2%) placebo/therapy; d, exact printed text: “Thirty-two of 256 participants (12.5%) in the supplements without therapy group and 22 of 256 (8.6%) in the supplements without therapy group.” Both occurrences are preserved as printed. e, 25/257 (9.7%) placebo/no therapy plus 32/256 (12.5%) supplements/no therapy; f, 26/256 (10.2%) placebo/therapy plus 22/256 (8.6%) supplements/therapy; g, interaction therapy and supplements. Footnote d visually inspected; do not silently substitute an arm label.

| Key | Matching narrative |
|---|---|
| M084 | p.7 marginal MDD counts/rates: placebo 51 (9.9%), 1.1/100 person-months; supplements 54 (10.5%), 1.2/100; no therapy 57 (11.1%), 1.3/100; therapy 48 (9.4%), 1.0/100. Matching M074–M082 denominators/time. |
| M085 | p.1 abstract repeats all three OR/CI values M075,M077,M078 with interaction P=.48; p.7 repeats all OR/CI/P M075,M077,M078 and HR/CI/P M080,M082,M083. Narrative none significant for MDD onset or time-to-onset. |

## Figure 2: full graph unit map

[Physical p.7 Figure 2](../../../jama_bot_2019_oi_190007.pdf#page=7). Eight plots: A supplement contrast and B therapy contrast, each with PHQ, IDS, GAD, utility. Available observed data, not multiple-imputed. Time locations baseline,3,6,12 months; horizontal axis ticks also 9 months, without a 9-month assessment. No exact graph point, quartile, or whisker values are numerically labeled; those values remain visual evidence rather than fabricated numeric transcriptions. All eight plots visually inspected. Both panels show downward PHQ/IDS/GAD means over time and utility broadly increasing. At month12 supplement PHQ/IDS/GAD diamonds visually above control; therapy symptom diamonds below control; utility diamonds broadly close. These describe plot positions without inferring statistical significance.

| Key | Outcome | Printed participants baseline / 3 / 6 / 12 mo, identical A and B | Y-axis ticks |
|---|---|---|---|
| M086 | Patient Health Questionnaire | 996 / 819 / 750 / 757 | 0,5,10,15,20,25,30 |
| M087 | Inventory of Depressive Symptoms | 994 / 817 / 747 / 757 | 0,10,20,30,40,50,60 |
| M088 | Generalized Anxiety Disorder | 993 / 815 / 747 / 757 | 0,5,10,15,20,25 |
| M089 | Utility | 993 / 814 / 747 / 757 | 0,.2,.4,.6,.8,1.0 |
| M090 | Caption | Median horizontal line; box IQR 25%–75%; whisker 1.5 IQR beyond 25th/75th percentiles; dots other values; diamonds means; dark blue intervention, light blue control; N persons completing secondary outcome at time, available data. | No inferential intervals drawn |
| M091 | p.7 secondary interaction narrative | No significant supplement × therapy interactions for any secondary score; P range .41–.98; four intervention combination graph in supplement eAppendix 9. | Table 3 excludes interactions |

## Table 3: every secondary endpoint inferential result

[Physical p.8 Table 3](../../../jama_bot_2019_oi_190007.pdf#page=8). Supplement versus placebo and therapy versus no therapy. Every estimate is an unstandardized regression coefficient using effect-coded variables (−1,1); reported CI is 95%. “Overall follow-up effect using all follow-ups” and “Effect at 12 Month Follow-up” are separate analyses. Corresponding outcome scales M008/M066/M067.

| Key | Outcome / contrast | Overall coefficient (95% CI) | Overall P | 12-mo coefficient (95% CI) | 12-mo P | Cohen D |
|---|---|---|---|---|---|---|
| M092 | PHQ supplements/placebo | 0.33 (0.12 to 0.53) | .002 | 0.28 (0.05 to 0.50) | .02 | 0.10 |
| M093 | PHQ therapy/no therapy | −0.13 (−0.33 to 0.07) | .19 | −0.17 (−0.39 to 0.06) | .14 | −0.02 |
| M094 | IDS supplements/placebo | 0.60 (0.15 to 1.05) | .01 | 0.36 (−0.19 to 0.90) | .20 | 0.05 |
| M095 | IDS therapy/no therapy | −0.23 (−0.67 to 0.22) | .32 | −0.28 (−0.83 to 0.27) | .31 | 0.006 |
| M096 | GAD supplements/placebo | 0.25 (0.08 to 0.42) | .004 | 0.14 (−0.04 to 0.33) | .13 | 0.10 |
| M097 | GAD therapy/no therapy | −0.16 (−0.32 to 0.01) | .06 | −0.24 (−0.42 to −0.06) | .01 | −0.07 |
| M098 | Utility supplements/placebo | −0.006 (−0.012 to 0.000) | .052 | −0.002 (−0.008 to 0.005) | .61 | −0.07 |
| M099 | Utility therapy/no therapy | 0.002 (−0.003 to 0.008) | .44 | 0.004 (−0.002 to 0.009) | .23 | 0.08 |
| M100 | Footnote a | Joint interventions; site, MDD history, corresponding baseline adjustment; effect-coded pills/therapy (−1,1); supplement × therapy interaction omitted because none significant. | applies M092–M099 | | | |
| M101 | Footnotes b,c | Overall generalized estimating equations longitudinal multiple-imputed analyses; 12-mo robust linear regression multiple-imputed analyses. | distinct model/time scopes | | | |
| M102 | Footnote d | To obtain adjusted between-condition mean differences, estimates AND 95% CIs multiplied by 2. | Compare M104–M108 | | | |
| M103 | Footnote e | Cohen D calculated from baseline and 12-month means and pooled SD obtained from multiple-imputed data. | Compare supplement eAppendix 12 and methodological explanation | | | |

## Narrative secondary results and sensitivity findings

[Physical p.8 text](../../../jama_bot_2019_oi_190007.pdf#page=8).

| Key | Exact printed relationship | Matching location |
|---|---|---|
| M104 | Therapy lower GAD at 12 mo, adjusted mean difference −0.48 (95% CI −0.84 to −0.12), P=.01. | M097 12-mo, footnote d |
| M105 | Supplement overall PHQ adjusted mean difference 0.65 (95% CI 0.25–1.06), P=.002. | M092 overall, footnote d |
| M106 | Supplement overall IDS adjusted mean difference 1.20 (95% CI 0.29–2.10), P=.01. | M094 overall, footnote d |
| M107 | Supplement overall GAD adjusted mean difference 0.50 (95% CI 0.16–0.84), P=.004. | M096 overall, footnote d |
| M108 | Supplement 12-mo PHQ adjusted mean difference 0.56 (95% CI 0.11–1.01), P=.02. | M092 12-mo, footnote d |
| M109 | Unadjusted GAD baseline therapy/no therapy both 5.8; 12 mo no therapy 3.9 versus therapy 3.2. | Figure 2 B and supplement observed/imputed mean definitions |
| M110 | Unadjusted PHQ baseline placebo 7.3 versus supplements 7.5; 12 mo placebo 4.1 versus supplements 4.9; narrative less improvement depressive/anxiety symptoms on supplements, therapy no other secondary effect. | M055, Figure 2 A |
| M111 | Post hoc modifiers: therapy PHQ 12-mo more favorable at higher baseline PHQ; supplements anxiety follow-up higher at higher baseline anxiety; therapy utility 12-mo effect larger UK than Netherlands. No numeric coefficient/P here; supplement eAppendix 10 holds values. Without-imputation sensitivity comparable estimates, supplement eAppendix 11. | Named comparisons/model/time preserved |
| M112 | CACE: no supplement primary effect; similar secondary effects; therapy primary OR 0.78 (95% CI 0.64–0.95), significant, accounting adherence. No P value printed here. | Supplement eAppendix 12; M009/M014 |
| M113 | p.9 Discussion repeats adherence about three-quarters; individual sessions first 6 months well attended, group sessions subsequent 6 months poorly attended; predefined therapy adherence ≥8/21; therapy anxiety effect 12 mo; adherence-adjusted lower MDD; 1-year follow-up. | M006,M009,M072,M104,M112 |

## Adverse events and concealment

| Key | Source | Printed relationship |
|---|---|---|
| M114 | p.1 abstract | One death supplement+therapy. Hospitalization P 24; PT 24; S 26; ST 24 patients. |
| M115 | p.8 adverse events | 98 hospitalized, 1 death during 12-mo follow-up; events judged unrelated interventions. | 
| M116 | p.8 concealment | Believed multinutrient: P 8.2%, PT 10.4%, S 25.5%, ST 43.7%; P<.001; placebo less likely believe multinutrients; supplement eAppendix 13. No denominators printed here. |
| M117 | p.8 concealment | Among completed concealment questions at 12 mo, 40.4% did not know allocation; supplement eAppendix 13. |

## Remaining context and per-page completion

| Key | Source | Result-relevant interpretation or explicit no-applicable unit |
|---|---|---|
| M118 | [p.9 Discussion/Limitations/Conclusions](../../../jama_bot_2019_oi_190007.pdf#page=9) | 1025 overweight individuals; no intervention/combination effect on 1-year cumulative MDD; observed onset lower than expected and lower statistical power; approximately quarter lost to follow-up; randomized 2×2, four countries, one-year intervention/follow-up; placebo outperforming supplements in some secondary outcomes; no active therapy control; no numeric new effect/CI/P. Conclusion matches p.1. |
| M119 | [p.10 article information/references](../../../jama_bot_2019_oi_190007.pdf#page=10) | Author/investigator roles, disclosures, funding, data-sharing pointer and reference citations inspected in full. EU grant 613598 is administrative identifier, not outcome. Bibliographic years/volumes/pages/DOIs and cited title numbers (e.g., 1160 sequelae of 289 diseases, 1990–2010) are reference metadata, no new reported trial quantitative relationship. No applicable inferential/count/denominator units here. |
| M120 | [p.11 references](../../../jama_bot_2019_oi_190007.pdf#page=11) | Continuation references 19–40; source citations for measures, prevention assumptions, factorial design, Rubin pooling, GEE, Cohen D and CACE are locators only. Bibliographic numbers and title duration “2-year” do not report this trial results. No applicable new trial quantitative relationship. |

| Physical page | Printed page | Fully inspected units | Completion |
|---|---:|---|---|
| 1 | 858 | Abstract population/intervention/outcome/analysis, all result numbers, hospitalization/death, conclusions; M001–M007,M036–M037,M073,M085,M114 | COMPLETE |
| 2 | 859 | Key Points marginal outcomes; introduction context; methods eligibility, randomization, supplement quantities; M001–M005,M016,M073 | COMPLETE |
| 3 | 860 | Every Figure 1 node, exclusion category, arm count, follow-up/reason row, footnote; M017–M035 | COMPLETE |
| 4 | 861 | Therapy dose, all outcome scales, adherence definition, full printed sample-size assumptions, all model/analysis definitions; M006–M014 | COMPLETE |
| 5 | 862 | Every Table 1 value/row/column/footnote and diet component; M038–M069 | COMPLETE |
| 6 | 863 | Every Table 2 cell/footnote including exact arm labels; methods continuation, recruitment, missingness tests/counts, adherence; M015,M017,M070–M083 | COMPLETE |
| 7 | 864 | All eight Figure 2 plots, N vectors, axes/legend/caption; primary counts/rates, all OR/HR/P repeats, secondary interaction range; M073,M084–M091 | COMPLETE |
| 8 | 865 | Every Table 3 coefficient/CI/P/D and footnote; all narrative mean differences, observed means, modifiers, sensitivity/CACE, adverse events/concealment; M092–M117 | COMPLETE |
| 9 | 866 | Discussion, limitations, conclusion repetitions and contextual literature statements; M113,M118; no new numeric result | COMPLETE |
| 10 | 867 | Full administrative material and references inspected, explicit no-applicable new trial result; M119 | COMPLETE |
| 11 | 868 | Full references inspected, explicit no-applicable new trial result; M120 | COMPLETE |

Coverage: 11/11 mapped source units; 120 relationship groups (including contextual/definition/no-applicable groups). Quantitative graph positions without printed numeric labels remain directly inspectable visual evidence; no exact numerical reconstruction is claimed. No scientific coverage gap. Precision, model differences, available versus imputed samples, and effect-code scales remain explicit for downstream checkers. Every cited source location is REPORT; any later comparison with a supplied plan requires PLAN role at that other location.
