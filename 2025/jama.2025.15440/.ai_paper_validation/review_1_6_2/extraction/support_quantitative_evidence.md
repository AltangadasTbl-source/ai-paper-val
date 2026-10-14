# Support quantitative evidence map — Workflow 1.6.2

Scope: DOC-002 protocol, all 26 physical PDF pages; DOC-003 SAP, all 24 pages; DOC-004 results supplement, all 11 pages. Total 61 mapped pages. The protocol and SAP are PLAN documents; results supplement is REPORT. No Office, workbook, CSV or other supplied support sources exist, so formulas/cached workbook values are not applicable. This map records source evidence and matching keys without diagnosing candidates. N101–N111 and S101–S124 are disjoint from main-paper identifiers.

Read controls: QUALITY_CONTROL_SCOPE.md; workflow_1_6_2/review_contract.md; current source inventory, evidence-asset inventory, source coverage and tooling record. No old findings, screens, classifications or reports were read. Reused SAP pages 7–22 and result pages 1,4–11 were read as transcription aids. Every fresh-required SAP page 1–6,23–24 and results page 2–3 was extracted with the recorded temporary interpreter and pdf_tools.py text --first N --last N OUTPUT --layout (PyMuPDF 1.26.4, CPU, sorted reading order). Derivatives: preprocessing/support-mapper-sap-N.txt and preprocessing/support-mapper-result-N.txt. Protocol pages 1–26 were freshly rendered by the coordinator using PyMuPDF 1.26.4, 200 dpi CPU, and OCR used user-approved RapidOCR 1.4.4 / ONNX Runtime CUDA 1.28.0 on RTX 5070 via PowerShell. Protocol page text and images: preprocessing/doc002-page-NNN-gpu-ocr.txt and preprocessing/doc002-page-NNN.png. No duplicate OCR was launched here.

Native protocol font mapping is unusable. OCR can omit individual lines and rotate table strings; manual image reading supplies the quantitative tables and decision rules below. These image-based transcriptions take precedence over raw OCR strings reproduced in the appendix. Particularly, protocol page 11 actually prints `aged≥54` in the diagram; it is not silently changed to the nearby inclusion criterion ≥65. OCR artifacts such as rotated `%06`, `70o0`, `25o0`, `5 oo0` and partial missing sentences are not taken as source numbers. Protocol table 4 female patch rate is visually 3.09%; OCR 3.09% agrees, and rates are preserved as printed.

## Complete physical-page coverage

Every row below is mapped; no scientific coverage gap remains. A no-applicable-content record means the complete page was opened and contains only identity, navigation, administration, background or bibliographic matter, rather than an uninspected unit.

| Source | Page | Role | Content mapped | Relationship IDs |
|---|---:|---|---|---|
| DOC-002 | 1 | PLAN | Version 2.0, 2021-06-08, ISRCTN15544176; cover/contacts; no quantitative result | N111 |
| DOC-002 | 2 | PLAN | Complete contents; no substantive analysis specification beyond pointers | N111 |
| DOC-002 | 3 | PLAN | Contents continuation; no substantive quantitative result | N111 |
| DOC-002 | 4 | PLAN | Synopsis: population, 2500–5000, two-week patch, 2.5-year primary, subgroup/5-year secondary | N108, S101, S102, S103 |
| DOC-002 | 5 | PLAN | Abbreviations; no applicable quantitative result | N111 |
| DOC-002 | 6 | PLAN | Historical/background epidemiology and screening studies; read completely, not AMALFI result/design inputs except rationale | N111 |
| DOC-002 | 7 | PLAN | Historical SCAF stroke-risk evidence and screening rationale; no AMALFI result | N111 |
| DOC-002 | 8 | PLAN | Historical screening trials and Zio pilot: 1600, median 12.7 days, 99.1% analyzable; source background | N111 |
| DOC-002 | 9 | PLAN | Age/sex rationale and primary definition GP record at 2.5 years | S101, S102 |
| DOC-002 | 10 | PLAN | Secondary status, 5-year design, care discretion, follow-up 1/2.5/5 plus 20 years | S102, S103, S115 |
| DOC-002 | 11 | PLAN | Figure 1 complete design labels; eligibility and exclusions | N109, S101, S102, S103, S115 |
| DOC-002 | 12 | PLAN | Consent, 1:1 individual minimization, open label, no sham patch, GP management | S115 |
| DOC-002 | 13 | PLAN | Two-week intervention; EQ-5D, withdrawal/end study; usual-care AF assumptions | N108, S113, S115 |
| DOC-002 | 14 | PLAN | 0.7% annual control; 3.75% patch estimate; Figure 2; initial/extended sample sizes | N108, N110, S113 |
| DOC-002 | 15 | PLAN | ITT, chi-square primary/subgroup, permutation secondary, heterogeneity; age 75 exploratory | S101, S102, S103, S115 |
| DOC-002 | 16 | PLAN | Nonrandomized anticoagulation/hospitalization comparison; long-term exploratory events; data storage | S111, S112 |
| DOC-002 | 17 | PLAN | Ethical/regulatory, finance/insurance/publication; no additional applicable quantitative analysis | N111 |
| DOC-002 | 18 | PLAN | CHA2DS2-VASc scoring table, all eight components | N109 |
| DOC-002 | 19 | PLAN | Model a+bt, preemption e+ft, first six months, 2% extra; primary rationale/power assumptions | N110, S116, S117, S118 |
| DOC-002 | 20 | PLAN | Tables 1–2 complete annual projection and nine sample-size rows | N110, S116 |
| DOC-002 | 21 | PLAN | Table 3 all five whole-trial assumption/power rows | N108, S117 |
| DOC-002 | 22 | PLAN | Table 4 all six age/sex subgroup assumption/power rows | N108, S118 |
| DOC-002 | 23 | PLAN | References 1–13 opened; no applicable new quantitative relationship | N111 |
| DOC-002 | 24 | PLAN | References 14–25 opened; no applicable new quantitative relationship | N111 |
| DOC-002 | 25 | PLAN | References 26–37 opened; no applicable new quantitative relationship | N111 |
| DOC-002 | 26 | PLAN | Reference 38 opened; no applicable new quantitative relationship | N111 |
| DOC-003 | 1 | PLAN | SAP v1.2 26 June 2025 aligned protocol v2.0 8 June 2021; no results | N111 |
| DOC-003 | 2 | PLAN | Complete contents part 1; no new numeric relationship | N111 |
| DOC-003 | 3 | PLAN | Complete contents part 2; no new numeric relationship | N111 |
| DOC-003 | 4 | PLAN | Roles/responsibilities; no applicable result/decision rule | N111 |
| DOC-003 | 5 | PLAN | Primary/secondary objectives, age 80/sex; deviations described/justified | S101, S102, S103 |
| DOC-003 | 6 | PLAN | Eligibility age 65, sex-specific score, intervention 14 days, urgent thresholds | N109, S115, S124 |
| DOC-003 | 7 | PLAN | ITT, usual care, ideal 5-year outcome rationale | S101, S103, S115 |
| DOC-003 | 8 | PLAN | Figure 1 and actual primary 2.5-year GP-record definition; secondary introduction | S101, S102, S103 |
| DOC-003 | 9 | PLAN | Secondary status, exploratory status, null, minimization variables, blinding | S102, S103, S107, S115 |
| DOC-003 | 10 | PLAN | Self-report eligibility/minimization; primary-care extract 1/2.5/5 years; national datasets | S104, S115 |
| DOC-003 | 11 | PLAN | Healthcare dataset continuation, annual 2022–2027, up to 25 years; EQ-5D/timepoints | S104, S112 |
| DOC-003 | 12 | PLAN | No formal DMC/interim safety or efficacy; ITT; primary-care follow-up definitions | S104, S115 |
| DOC-003 | 13 | PLAN | National follow-up; prerandom AF and OAC months; primary no censoring | S101, S104, S108, S109 |
| DOC-003 | 14 | PLAN | Secondary/OAC right censoring, imputation later; baseline descriptive variables | S103, S104, S109, N102 |
| DOC-003 | 15 | PLAN | Baseline sources/missingness and medication groups | N102 |
| DOC-003 | 16 | PLAN | Baseline shell denominators 5040/2520/2520; completeness framework | N102, N108, S104 |
| DOC-003 | 17 | PLAN | Follow-up day 913/1826; adherence metrics; all patch findings | N101, N103, N105, N106, S123, S124 |
| DOC-003 | 18 | PLAN | Primary chi-square; age 80/sex heterogeneity; secondary permutation formula; sensitivity GP/HES | S101, S102, S103, S104, S105 |
| DOC-003 | 19 | PLAN | Exploratory time-to-AF/log-rank, 2.5-year known-AF time, OAC proportions/exposure | S106, S107, S108, S109 |
| DOC-003 | 20 | PLAN | OAC log-rank, clinical descriptive events, nonrandom groups/definitions | S110, S111, S112 |
| DOC-003 | 21 | PLAN | GP reporting date definition; nonprespecified analyses; economic/power inputs | S111, S113 |
| DOC-003 | 22 | PLAN | Sample-size extension, power, no planned adjustment, alpha/multiplicity | S113, S114 |
| DOC-003 | 23 | PLAN | CIs 95%; software/references; no additional result | S114 |
| DOC-003 | 24 | PLAN | CHA2DS2-VASc appendix all components | N109 |
| DOC-004 | 1 | REPORT | Contents eMethods, eTables 1–3, eFigures 1–4; no extra results | N111 |
| DOC-004 | 2 | REPORT | eMethods:14-day monitoring, ≥30 s AF,13 arrhythmias, thresholds/reporting | S124, S115 |
| DOC-004 | 3 | REPORT | eMethods references 1–7; no new applicable quantitative relationship | N111 |
| DOC-004 | 4 | REPORT | eTable 1 complete metrics and reason rows and 166 denominator note | N101 |
| DOC-004 | 5 | REPORT | eTable 2 age/sex/ethnicity/BMI/score/history/medications | N102, S119 |
| DOC-004 | 6 | REPORT | eTable 2 medication continuation, every P/footnote | N102, S119 |
| DOC-004 | 7 | REPORT | eTable 3 all 13 condition rows,2520/2126 denominators, thresholds | N103, S124 |
| DOC-004 | 8 | REPORT | eFigure 1 five complete rows, P, heterogeneity,95% CI/caption | N104, S120, S121, S122 |
| DOC-004 | 9 | REPORT | eFigure 2 six AF histograms/axes, grouped 9/29/20/42% | N105, S124 |
| DOC-004 | 10 | REPORT | eFigure 3 KM0–6 months,89/34/18/10/8/7/6, seven pre-report events | N107, S123 |
| DOC-004 | 11 | REPORT | eFigure 4 six AF/AFL histograms/axes, grouped 10/26/18/46% | N106, S124 |

## Numeric relationship inventory

| ID | Role and exact locator | Quantity/population/unit and matching key |
|---|---|---|
| N101 | REPORT DOC-004 p4 eTable 1 | Patch adherence and durations, all 2520 randomized; copied complete below; main patch-wear/adherence paragraph and participant-flow keys |
| N102 | REPORT DOC-004 pp 5–6 eTable 2; PLAN DOC-003 pp 14–16 | All baseline rows with overall 2520, ECG 2126, no ECG 394; row percentages; every P/test footnote below; main baseline and patch compliance keys |
| N103 | REPORT DOC-004 p7 eTable 3 | Complete 13 condition rows; count/2520 and count/2126; main patch AF 89, AF with flutter 15, flutter alone 13 keys |
| N104 | REPORT DOC-004 p8 eFigure 1 | Primary-or-secondary-care sensitivity AF at 2.5 years overall and age 80/sex; complete five rows below; main primary-care-only figure must match outcome source before comparison |
| N105 | REPORT DOC-004 p9 eFigure 2 | AF-only 89 patch cases, six histogram panels; grouped longest AF episode percentages 9,29,20,42; all axes/labels below; main patch AF burden/duration key |
| N106 | REPORT DOC-004 p11 eFigure 4 | AF and/or flutter metrics, six panels; grouped percentages 10,26,18,46; no printed total in caption, compatible population key AF/AFL rather than AF alone |
| N107 | REPORT DOC-004 p10 eFigure 3 | KM from urgent patch report to first GP AF, restricted 89 AF; risk counts 89,34,18,10,8,7,6 at months 0–6; seven prior GP-record participants event immediately after day 0 |
| N108 | PLAN DOC-002 pp 4,14–15,21–22; DOC-003 pp 16,21–22 | Initial 2500, extended up to 5000; shell 5040/2520/2520; complete power rows and assumptions below; main sample-size/rationale key |
| N109 | PLAN DOC-002 pp 4,9,11,18; DOC-003 pp 6,24 | Age≥65; score≥3 men/≥4 women; no known AF/flutter; diagram p11 literally aged≥54; eight score components below |
| N110 | PLAN DOC-002 pp 14,19–20 | Model/projection complete below: annual 0.7% control; preemption 70/60/50/40/30%; 2% additional; first 6 months patch detection; cumulative control 0.70–3.50%, active 3.96–5.50% |
| N111 | All assigned identity/admin/background/reference pages | Complete no-applicable-content map above. Historical studies are background rather than AMALFI results. Exact per-page text appendix retained for transparent coverage |

## Statistical relationship inventory

| ID | Exact location and role | Complete specification/result and matching main-paper key |
|---|---|---|
| S101 | PLAN DOC-002 pp 4,9,11,15; DOC-003 pp 5,8,13,18 | Primary: proportion with AF recorded in primary-care records between randomization and 2.5 years; all randomized, ITT; chi-square; ratio of proportions 95% CI; no censoring. Pre-randomization AF alone is not endpoint, later record required. Death/withdrawal/loss without AF before 2.5 years treated as no AF. Match primary outcome/model/population |
| S102 | PLAN DOC-002 pp 4,10–11,15; DOC-003 pp 8–9,18 | Secondary: primary AF proportion by age <80/≥80 and sex; chi-square per subgroup, heterogeneity between two subgroups. Secondary assessed regardless primary result. Protocol p11 diagram lists only age for proportion, synopsis/narrative specify both age and sex. Match main subgroup figure and prespecified status |
| S103 | PLAN DOC-002 pp 4,10–11,15; DOC-003 pp 5,7–9,14,18 | Secondary at 5 years: mean time with known AF overall/age 80/sex; no AF contributes zero; days from first post-randomization GP AF to date 5 years/death/withdrawal if earlier. Permutation test; protocol specifies heterogeneity. SAP empirical P=(1+s)/(n+1), s = number of simulations with difference at least observed, n = total. Missing/withdrawal handling later before unblinded analyses; imputation procedure later. Match 5-year follow-up status |
| S104 | PLAN DOC-003 pp 10–14,16–18 | Primary care follow-up earliest death, consent withdrawal, loss via GP move to nonparticipant practice, day 913/1826; national data earliest death, withdrawal, day 913/1826. Randomization day 0. Secondary time after AF censored at death/withdrawal/day 1826 independently of GP follow-up length; imputation for lost participants without known AF later. Complete follow-up separately for GP/dispensing; number/% to 913/1826 and average follow-up planned. Match source-specific follow-up and missingness |
| S105 | PLAN DOC-003 p18; REPORT DOC-004 p8 | Sensitivity primary and secondary outcomes using AF in GP or HES; AF counts irrespective of care location. Result five rows below; primary and secondary source distinction mandatory |
| S106 | PLAN DOC-003 p19 | Exploratory time to AF at 2.5/5 years: randomization to first post-randomization GP AF; censor at earliest death, withdrawal, primary care loss, day 913/1826; cumulative incidence curves, log-rank test; median among diagnosed. Match main cumulative time-to-AF curve |
| S107 | PLAN DOC-003 p19 §6.4.2 | Time with known AF at 2.5 years explicitly exploratory, replicates 5-year secondary on a shorter window; same null/permutation procedures §6.2. Match main mean AF duration at 30 months/outcome status |
| S108 | PLAN DOC-003 pp 13,19 | Exploratory OAC participants post-randomization, chi-square proportions and median months to first among users; direct OAC/VKA exclude rivaroxaban 2.5 mg BID; first month after randomization contributes, month of randomization classed baseline; 30/60 months or death/withdrawal if earlier; AF status not required. Match main OAC counts/proportions |
| S109 | PLAN DOC-003 pp 13–14,19 | Exploratory OAC quantitative exposure distinct calendar months with likely exposure, mean in each arm, permutation test; same baseline/right censoring rules; derivation in separate document not provided. Match main OAC exposure months |
| S110 | PLAN DOC-003 p20 | Exploratory cumulative incidence months to first OAC to 30/60 months; censor at month of death/withdrawal; log-rank. Match main OAC cumulative curve |
| S111 | PLAN DOC-002 p16; DOC-003 pp 20–21 | Nonrandomized exploratory screen-vs-clinical AF: protocol OAC and hospitalization; SAP three groups patch+GP, GP only in either arm, patch without GP; OAC after month of first GP AF (groups 1/2) or after month of patch AF report to GP (group 3); email report date precedes automated letter; report interval patch-to-GP in group 1. Match main post-AF anticoagulation/diagnosis route |
| S112 | PLAN DOC-002 p16; DOC-003 pp 11–12,20 | Long-term clinical exploratory events: hospitalizations all/CV, ischaemic stroke, major bleeding, all-cause/CV death; SAP numbers/proportions, no hypothesis testing, not powered; future details later. National data up to 25 years. No formal DMC and no interim safety/efficacy assessment planned. Match clinical events/report status |
| S113 | PLAN DOC-002 pp 13–15; DOC-003 pp 21–22 | Sample-size inputs 0.7% per year control→1.75% at 2.5 years, initial patch 3.75%,2.5-year active 4.4%; initial 2500/1250 each >90% power 2p<.05, ratio about 2.5; extension 5000 based on 1250 baseline/patch, blind to total AF,>90% power 2p<.01 for 2.5 or 2-fold; age 80/sex ~90% 2p<.05. Protocol around 3000 >.90 at .05 for ratio 2,4100 at .01. Model details N110/S116–118. Match power rationale |
| S114 | PLAN DOC-003 pp 22–23 | No a priori baseline adjustment for primary/secondary; conditional adjustment if significant imbalance overall/subgroup, minimization expected to prevent imbalance. Two-sided alpha<.05; no formal multiplicity adjustment for primary/secondary/exploratory including subgroups; interpretive allowance; 95% CIs primary/secondary. SAS 9.4/R 4.2.2/RStudio 2024.12.1 Build 563 or later. Match adjusted/unadjusted main estimates and multiplicity |
| S115 | PLAN DOC-002 pp 10–13; DOC-003 pp 6–10,12; REPORT DOC-004 p2 | Individual 1:1 allocation, central CTSU minimization, open label, no sham; single 2-week Zio XT versus usual care. SAP minimization age <75/≥75, sex, residual CHA excluding age/sex0–1,2,3–6, from self-report. ITT all randomized irrespective of adherence. GP manages independently. Patch reports not combined with other clinical outcomes before main unblinding. Match main randomization/intervention/model |
| S116 | PLAN DOC-002 pp 19–20 Table 2 | Nine comparison-time/power/sample-size rows below; alpha .05, power 90%, total n continuity corrected,1:1 equal groups; raw model inputs N110. Match initial sample-size calculation |
| S117 | PLAN DOC-002 p21 Table 3 | Five whole-trial assumption/power rows below; total n at .05/.01 at 90% power; power 2500.05,4000.05/.01,5000.05/.01; first row original assumptions 4.41/1.75 ratio 2.52; interim patch 4.09% starred |
| S118 | PLAN DOC-002 p22 Table 4 | All six age 80/age 75/sex subgroup rows below; ratio 2.5 throughout; n needed in subgroup at 90% power and total trial 4000/5000 powers; interim patch rates starred |
| S119 | REPORT DOC-004 pp 5–6 eTable 2 | Every baseline comparison/P recorded below. Footnote: chi-square categorical; Mantel-Haenszel trend ordinal; two-sample T normal/Mann-Whitney U nonnormal; exclude missing; ethnicity white vs all other nonmissing. Row percentages give compliance within each category, not column prevalence |
| S120 | REPORT DOC-004 p8 eFigure 1 overall | Sensitivity 251/2520 (9.96%) vs 207/2520 (8.21%); absolute 1.75%(95% CI .16,3.33); ratio 1.21 (1.02,1.45); P=.03; 95% CI unadjusted for multiplicity; directional right = more AF patch. Match sensitivity overall |
| S121 | REPORT DOC-004 p8 eFigure 1 age | <80:142/1715 (8.28%) vs 110/1744 (6.31%), RD 1.97%(.24,3.71), ratio 1.31 (1.03,1.67);≥80:109/805 (13.54%) vs 97/776 (12.50%), RD 1.04%(-2.28,4.36), ratio 1.08 (.84,1.40). Heterogeneity P=.28. Match sensitivity age 80 |
| S122 | REPORT DOC-004 p8 eFigure 1 sex | Women 105/1180 (8.90%) vs 70/1180 (5.93%), RD 2.97%(.86,5.08), ratio 1.50 (1.12,2.01); men 146/1340 (10.90%) vs 137/1340 (10.22%), RD .67%(-1.66,3.00), ratio 1.07 (.85,1.33). Heterogeneity P=.07. Match sensitivity sex |
| S123 | REPORT DOC-004 p10 eFigure 3; PLAN DOC-003 p17 | KM urgent patch report to first primary care AF among patch AF 89; seven post-randomization GP AF before urgent patch report counted at risk day 0, event immediately after; numbers at risk monthly 0–6 below; no P/CI printed. Match report-to-GP delay |
| S124 | REPORT DOC-004 pp 2,7,9,11; PLAN DOC-003 pp 6,17 | Patch AF≥30 s continuous AF-compatible tracing; 13 arrhythmias plus sinus/noise algorithm and technician review, no manual overread by study team. Urgent AF/flutter, sustained VT/VF, pauses>6 s, complete/MobitzII/high-grade AV block; VT and SVT>30 s sustained/≤30 s non-sustained. AF burden percentage of monitoring time, duration hours, day of first episode, heart-rate beats/min. Match patch 89 AF / 102 AF-or-flutter and duration measure |

## Complete supplementary result transcription

### N101 — eTable 1, DOC-004 page 4

All 2520 randomized to patch. Wore and returned: 2126 (84.4%); randomization to activation: median 10 days (IQR 6–18); wear: median 13.9 days (13.2–14.0); analyzable: median 13.5 days (12.6–13.9); suitable data: 98.8% (95.8–99.6). Worn ≥10.5 days (75% recommended time): 1960 (77.8%); worn <10.5 days: 166 (6.6%); returned unworn: 188 (7.5%); not returned: 206 (8.2%). Among 166 early removals: attachment 43 (25.9%), skin 18 (10.8%), other 8 (4.8%), unknown 97 (58.4%). IQR means interquartile range; SD means standard deviation. The printed footnote explicitly specifies percent of 166. All durations/percentages are medians and IQRs except count (%).

### N102 / S119 — eTable 2, DOC-004 pages 5–6

Columns: overall patch N=2520; ECG N=2126 (84.4%); no ECG N=394 (15.6%); P. Counts/percentages are row percentages.

| Characteristic | Overall | ECG data | No ECG data | P printed |
|---|---:|---:|---:|---|
| Age <75 |683|577 (84.5%)|106 (15.5%)|.75 / .62 trend for age categories|
| Age≥75,<80 |1032|876 (84.9%)|156 (15.1%)|same age comparison|
| Age≥80 |805|673 (83.6%)|132 (16.4%)|same age comparison|
| Age mean(SD), years |77.7 (5.9)|77.6 (5.9)|77.8 (6.1)|.50|
| Male |1340|1137 (84.9%)|203 (15.1%)|.47 sex comparison|
| Female |1180|989 (83.8%)|191 (16.2%)|same sex comparison|
| Asian |27|20 (74.1%)|7 (25.9%)|.17 ethnicity comparison|
| Black |2|2 (100.0%)|0 (0.0%)|same ethnicity comparison|
| White |2045|1738 (85.0%)|307 (15.0%)|same ethnicity comparison|
| Other |21|17 (81.0%)|4 (19.0%)|same ethnicity comparison|
| Missing ethnicity |425|349 (82.1%)|76 (17.9%)|excluded from P|
| BMI <25 kg/m² |488|422 (86.5%)|66 (13.5%)|.07 / .03 trend BMI categories|
| BMI 25 to <30 |751|639 (85.1%)|112 (14.9%)|same BMI comparison|
| BMI≥30 |571|466 (81.6%)|105 (18.4%)|same BMI comparison|
| Missing BMI |710|599 (84.4%)|111 (15.6%)|excluded from P|
| BMI mean(SD) |28.2 (5.2)|28.0 (5.0)|29.3 (6.1)|<.001|
| CHA2DS2VASc<3 |33|31 (93.9%)|2 (6.1%)|<.001 / <.001 trend|
| Score 3 |685|596 (87.0%)|89 (13.0%)|same score comparison|
| Score 4 |983|846 (86.1%)|137 (13.9%)|same score comparison|
| Score≥5 |819|653 (79.7%)|166 (20.3%)|same score comparison|
| Score median(IQR) |4 (3–5)|4 (3–5)|4 (4–5)|<.001|
| Hypertension |2255|1908 (84.6%)|347 (15.4%)|.32|
| Diabetes |713|582 (81.6%)|131 (18.4%)|.02|
| Stroke/TIA |485|395 (81.4%)|90 (18.6%)|.05|
| CKD stage≥3 |438|366 (83.6%)|72 (16.4%)|.61|
| Thromboembolism |271|216 (79.7%)|55 (20.3%)|.03|
| MI |269|226 (84.0%)|43 (16.0%)|.87|
| Heart failure |244|191 (78.3%)|53 (21.7%)|.006|
| Peripheral arterial disease |214|170 (79.4%)|44 (20.6%)|.04|
| Statin |1739|1462 (84.1%)|277 (15.9%)|.54|
| RAAS inhibition |1599|1341 (83.9%)|258 (16.1%)|.36|
| PPI/H2 antagonists |1265|1065 (84.2%)|200 (15.8%)|.81|
| Calcium-channel blockers |1200|996 (83.0%)|204 (17.0%)|.07|
| Diuretics |713|593 (83.2%)|120 (16.8%)|.30|
| Aspirin/dipyridamole |705|585 (83.0%)|120 (17.0%)|.23|
| Beta-blockers |619|529 (85.5%)|90 (14.5%)|.39|
| P 2Y12 inhibition |363|300 (82.6%)|63 (17.4%)|.33|
| OAC |174|137 (78.7%)|37 (21.3%)|.03|
| Direct OAC |128|101 (78.9%)|27 (21.1%)|.08|
| VKA |59|47 (79.7%)|12 (20.3%)|.31|
| Insulin |117|94 (80.3%)|23 (19.7%)|.22|

Footnotes: row percentages give compliance within baseline category. Chi-square for categorical variables, Mantel-Haenszel trend for ordinal variables; two-sample T-test for normal continuous variables and Mann-Whitney U-test for nonnormal continuous variables. Missing data excluded from P. Ethnicity P compares white versus any other nonmissing group. Other consists of multiracial n=10 and secondary-care 'any other ethnicity' code S n=11. RAAS means renin angiotensin aldosterone system. Prior diagnoses and medications are measured at or prior to randomization, rather than post-randomization events.

### N103 — eTable 3, DOC-004 page 7

| Condition | n | % randomized 2520 | % wore/returned 2126 |
|---|---:|---:|---:|
| AF |89|3.53|4.19|
| AF without flutter |74|2.94|3.48|
| AF with flutter |15|.60|.71|
| Flutterwithout AF |13|.52|.61|
| Complete AV block |5|.20|.24|
| High-grade AV block |10|.40|.47|
| Second-degree Mobitz II |8|.32|.38|
| Second-degree 2:1 |1|.04|.05|
| Pauses>6 seconds |6|.24|.28|
| Sustained VT>30 seconds |2|.08|.09|
| Non-sustained VT≤30 seconds |676|26.83|31.80|
| Sustained SVT>30 seconds |134|5.32|6.30|
| Non-sustained SVT≤30 seconds |1772|70.32|83.35|

Flutter without AF through sustained VT are headed 'Other findings resulting in urgent reporting to GP'. The last three rows are headed 'Non-urgent findings'. AV means atrioventricular; GP means general practitioner. These condition counts need not partition participants.

### N104 / S120–S122 — eFigure 1, DOC-004 page 8

| Stratum | Patch AF/n(%) | Usual care AF/n(%) | Absolute difference 95% CI | Ratio 95% CI |
|---|---|---|---|---|
| <80 years |142/1715 (8.28%)|110/1744 (6.31%)|1.97%(.24%,3.71%)|1.31 (1.03,1.67)|
| ≥80 years |109/805 (13.54%)|97/776 (12.50%)|1.04%(-2.28%,4.36%)|1.08 (.84,1.40)|
| Females |105/1180 (8.90%)|70/1180 (5.93%)|2.97%(.86%,5.08%)|1.50 (1.12,2.01)|
| Males |146/1340 (10.90%)|137/1340 (10.22%)|.67%(-1.66%,3.00%)|1.07 (.85,1.33)|
| Overall |251/2520 (9.96%)|207/2520 (8.21%)|1.75%(.16%,3.33%)|1.21 (1.02,1.45), P=.03|

Age heterogeneity P=.28; sex heterogeneity P=.07. Endpoint is a primary care OR secondary care record of AF between randomization and 2.5 years. Ratio forest axis: .5, .75, 1, 1.25, 1.5, 2; reference 1; dashed overall ratio; right means more AF in patch, left means more AF in usual care. Square area represents statistical information, diamond represents overall result; 95% CI unadjusted for multiplicity; significant P<.05 if the CI does not cross 1. The caption calls the overall ratio the primary outcome within this sensitivity display; the outcome-source definition remains as printed.

### N105 / N106 / S124 — eFigures 2 and 4, DOC-004 pages 9 and 11

Both figures have panels A: day of first episode within monitoring; B: percentage time in AF (or AF/AFL); C: longest episode in hours; D: longest episode grouped; E: maximum heart rate in beats/min; F: minimum heart rate in beats/min. Vertical axes show number of participants. AF-only figure, page 9, D labels: [30 sec,6 min) 9%, [6 min,6 hr) 29%, [6 hr,24 hr) 20%, ≥24 hr 42%. AF/AFL figure, page 11, D labels: 10%, 26%, 18%, 46% respectively. A: x day ticks 1–14 and y 0–60 every 5; B: x <1,10,20,…100%, y 0–40 every 5; C: x 0,48,96,144,192,240,288,336 hours, y 0–50 every 5; D: y 0–50 every 5; E: x 75,100,125,150,175,200,225 beats/min, y 0/5/10/15; F: x 0,25,50,75,100,125,150 beats/min, y 0/5/10/15. Images were opened to read all panels. Histogram bars have no printed individual count labels; no exact bin counts were inferred from pixels. In AF-only A the first-day bar is about 51 visually, but 51 is not a printed numeric label and is not treated as an exact source count. These images retain complete continuous distributions for visual checking. Grouped percentage D is the printed extractable distribution. No P/CI appears in these histograms.

For the combined AF/AFL matching key, 102 is derived as 89 AF plus 13 flutter without AF from eTable 3; it is not a total printed in the eFigure 4 caption.

### N107 / S123 — eFigure 3, DOC-004 page 10

KM y-axis: 0,20,40,60,80,100%; x: months from urgent patch report, 0–6. At risk monthly: month 0:89; 1:34; 2:18; 3:10; 4:8; 5:7; 6:6. Seven participants whose post-randomization GP AF record predates the urgent patch report are included at risk on day 0 and counted as an event immediately after. Restricted to patch-detected AF. No printed median, P or CI; no coordinates were digitized as exact numbers.

## Complete protocol and SAP quantitative plan transcription

### N109 — score and eligibility

Protocol page 18 and SAP page 24: heart failure/LV systolic dysfunction 1; hypertension with consistent BP above 140/90 mmHg or treated 1; age ≥75 two; diabetes 1; prior stroke/TIA/thromboembolism 2; vascular disease PAD/MI/aortic plaque 1; age 65–74 one; female sex 1. Eligibility: age ≥65, score ≥3 men/≥4 women, consent; known AF/flutter or latex allergy excluded. Protocol page 11 Figure 1 literally prints age ≥54 in its box; nearby §6.2 prints ≥65. All text is preserved for later comparison; no candidate diagnosis is assigned here.

### N110 — protocol page 19 model and page 20 Table 1

Diagnosis probability: time-dependent Poisson process parameter a+bt, slightly increasing with time. Early patch preemption probability e+ft decreases with time. a, b selected for annual 0.7% usual care during years 1 and 2; preemption 70/60/50/40/30% in years 1–5; extra 2% patch diagnoses not otherwise found within 5 years; patch-related early detection evenly over the first 6 months. Values printed below are percent, annual/cumulative as headed.

| Year end | Control within year | Control cumulative | Preempted fraction | Diagnosed by patch | Additional not patch within year | Active within year including extra 2% | Active cumulative |
|---|---:|---:|---:|---:|---:|---:|---:|
|1|.70|.70|70|.49|.21|3.96|3.96|
|2|.70|1.40|60|.42|.28|.28|4.24|
|3|.70|2.10|50|.35|.35|.35|4.59|
|4|.70|2.80|40|.28|.42|.42|5.01|
|5|.70|3.50|30|.21|.49|.49|5.50|

Protocol page 14 Figure 2 shows control red squares/active green triangles over 0–5 years, cumulative 0–6% with 0–5 year x-axis; precise annual/half-year numbers are retained in Tables 1–2 rather than approximated from the curve. Initial 1250 per arm/2500 total gives >90% power for 1.75% versus 4.4% at 2.5 years, ratio about 2.5, 2p<.05. Extended up to 5000 using 1250 participants randomized before 1 February 2021 and observed adherence/patch AF; around 3000 needed for >90% at .05 for ratio 2, 4100 at .01. SAP page 22 states extended 5000 improves precision for 2.5-fold difference with >90% power at .01 versus .05; preserves >90% power at .01 for 2-fold difference; age 80 and sex approximately 90% at .05; quality-of-life power improves. Protocol estimates about 500 AF cases over 5 years in the nonrandomized assessment rationale.

### S116 — protocol page 20 Table 2 sample size, all rows

Alpha .05, power 90% each; printed total sample size is continuity corrected; equal 1:1 groups. Comparison time is years, proportions are percent.

| Time | Control | Active | Total n |
|---|---:|---:|---:|
|1|.70|3.96|1019|
|1.5|1.05|4.10|1261|
|2|1.40|4.24|1565|
|2.5|1.75|4.41|1914|
|3|2.10|4.59|2348|
|3.5|2.45|4.80|2825|
|4|2.80|5.01|3406|
|4.5|3.15|5.25|4004|
|5|3.50|5.50|4711|

### S117 — protocol page 21 Table 3, all rows

All population 100%; active 2.5-year rate = patch rate ×1.177; n needed is total at 90% power. Powers are percent; `.05`/`.01` refer to printed 2p. Starred 4.09% is interim patch AF detection rate.

| Assumption | Patch% | Active 2.5-year % | Ratio active/control | Implied control % | N at 90% power, alpha .05 | N at 90% power, alpha .01 | Power at total 2500, alpha .05 | Power at total 4000, alpha .05 | Power at total 4000, alpha .01 | Power at total 5000, alpha .05 | Power at total 5000, alpha .01 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|Original whole trial|3.75|4.41|2.52|1.75|1914|2649|96|100|99|100|99|
|Whole trial|3.75|4.41|2.5|1.77|1941|2687|96|100|99|100|100|
|Whole trial interim|4.09*|4.82|2.5|1.93|1773|2454|97|100|99|100|100|
|Whole trial ratio 2|3.75|4.41|2|2.21|2939|4088|84|97|89|99|96|
|Whole trial interim ratio 2|4.09*|4.82|2|2.41|2684|3732|88|98|92|99|97|

### S118 — protocol page 22 Table 4, all rows

Ratio 2.5 each; active 2.5-year rate = patch rate ×1.177. Patch rates starred as interim; n needed is in the subgroup at 90% power. Powers are for total trial 4000/5000, rather than subgroup n.

| Subgroup | Population % | Patch% | Active 2.5-year % | Implied control % | N at 90% power, alpha .05 | N at 90% power, alpha .01 | Power at total 4000, alpha .05 | Power at total 4000, alpha .01 | Power at total 5000, alpha .05 | Power at total 5000, alpha .01 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|Age <80|64|2.78|3.27|1.31|2642|3658|89|73|95|85|
|Age≥80|36|6.28|7.39|2.95|1135|1571|96|87|99|95|
|Age <75|25|2.52|2.96|1.18|2924|4048|41|20|52|34|
|Age≥75|75|4.62|5.44|2.18|1563|2164|100|98|100|100|
|Males|54|4.94|5.82|2.33|1458|2018|98|92|99|98|
|Female|46|3.09|3.64|1.46|2367|3276|80|60|89|75|

Protocol §8.5.1 age 75 split is exploratory because the <75 subgroup has limited power. SAP contains age 80/sex secondary analyses and the exploratory analyses listed in S106–S112; the complete source-text appendix below ensures every printed specification remains available.

## Source links, coverage limits and derivative record

Source links relative to this artifact: [Protocol](../../../joi250068supp1_prod_1760999665.28862.pdf#page=1), [SAP](../../../joi250068supp2_prod_1760999665.29862.pdf#page=1), [Results supplement](../../../joi250068supp3_prod_1760999665.30362.pdf#page=1). Every location above uses physical PDF page N. Add #page=N to the same source when citing a particular table/statement; document page and physical page agree across these sources. Derivative source precedence: original rendered page, then readable text. Complete rows were mapped; no support page remains uninspected. Limitations: raw OCR omits some lines and rotates protocol tables; relevant decision rules and all pages 20–22 tables were visually read and fully transcribed above. Histogram individual bars lack printed counts and are available visually without assuming exact integer heights. No other formulas/cached values exist. Separate outcome-derivation and health-economics plans cited by the SAP are not supplied and cannot be reconstructed.

## Full page-text locator appendix

The following transcription aids retain all assigned source text, including admin/background/references, as read. They are not final authority. Manual protocol quantitative table and missing-line transcription above takes precedence. The retained combined SAP layout has physical-page footer numbers7–22 and formfeeds; no page was sampled or skipped.

### DOC-002 physical PDF page 1 — PLAN, fresh GPU OCR

```text
Date and version No:2021-06-08 Version 2.0
ISRCTN15544176
AMALFl: Active Monitoring for AtriaL Fibrillation
A randomized controlled trial of screening for silent atrial fibrillation in
high-risk individuals.
Ethics Ref:
19/LO/0220
Date and Version No:
2021-06-08 V2.0
Chief Investigator:
ProfessorLouiseBowman
Investigators:
Professor Barbara Casadei
Dr GuilhermePessoa-Amorim
Dr Nicholas Jones
Dr ChristineA'Court
Mr Richard Bulbulia
Mrs Georgina Buck
Sponsor:
University of Oxford
Funder:
NIHR, Oxford Biomedical Research Centre (BRC)
Chief Investigator
Signature:
AMALFl Central Coordinating Office, Clinical Trial Service Unit,
Richard Doll Building, Old Road Campus, Roosevelt Drive, Oxford OX3 7LF, UK
Tel:Freephone 08081645080
or: +44 (0) 1865 743884
Email: amalfi@ndph.ox.ac.uk, website: www.amalfitrial.org

```

### DOC-002 physical PDF page 2 — PLAN, fresh GPU OCR

```text
Date and version No: 2021-06-08 Version 2.0
ISRCTN 15544176
TABLEOFCONTENTS
1.
SYNOPSIS
2.
ABBREVIATIONS.
3.
BACKGROUNDANDRATIONALE
6
3.1 AF: A global health problem associated with substantial morbidity and mortality.
6
3.2 DetectingSCAF
6
3.3 Is stroke risk different in SCAF?.
3.4 Wilson & Jungner criteria for screening
3.5 Approaches to screening for SCAF
8
4.
STUDYAIMS.
9
5.
STUDYDESIGN.
.10
6.
PARTICIPANTIDENTIFICATION
11
6.1 Study Participants.
11
6.2 Inclusion Criteria.
11
6.3 Exclusion Criteria
11
7.
STUDYPROCEDURES
11
7.1 Recruitment.
11
7.2 Enrolment and Eligibility Assessment
12
7.3 Informed Consent.
12
7.4 Randomization, blinding and code-breaking.
12
7.5 ZioPatch administration.
13
7.6 EQ-5D questionnaires..
13
7.7 Discontinuation/Withdrawal of Participants from Study.
13
7.8Definition of End of Study
13
8.
STATISTICSANDANALYSIS
13
8.1 Initial assumptions
13
8.2 Sample size and predicted number of diagnoses.
14
8.3 Analysis of outcome measures.
15
8.5Exploratoryassessments
15
9.
DATAMANAGEMENT
16
9.1 Access to Data
.16
9.2 Data Recording and Record Keeping.
16
10.E
ETHICALANDREGULATORYCONSIDERATIONS.
16
11.FINANCE ANDINSURANCE
17

```

### DOC-002 physical PDF page 3 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN 15544176
12.PUBLICATIONPOLICY.
17
13.Appendix1:Calculation of theCHA2DS2-VAScscore
18
14. Appendix 2: Modelling of expected prevalence of AF over time and statistical power calculations . 19
* interim AF detection rate by patch
.22
15.REFERENCES
23

```

### DOC-002 physical PDF page 4 — PLAN, fresh GPU OCR

```text
Date and versionNo:2021-06-08Version2.0
ISRCTN15544176
1. SYNOPSIS
Study Title
AMALFl (Active Monitoring for AtriaL Fibrillation): A randomized controlled
trial of screening for silent atrial fibrillation in high-risk individuals.
Short title
AMALFI
Study Design
Randomized controlled trial
Study
Individuals with a CHA2DS2-VASc score ≥ 3 (men) or ≥ 4 (women), aged ≥ 65
Participants
years without known atrial fibrillation (AF) identified from primary care
records.
PlannedSample
At least 2500 and up to 5000 (including up to 2500 randomized to the Zio
Size
Patch and 2500 to the control arm)
Primary
To assess the effect of 2 weeks of continuous monitoring using Zio Patch on
Objective
the proportion of participants diagnosed with AF compared to usual care at
2.5 years of follow up from randomization (i.e. at around the midpoint of a
proposed 5-year screeninginterval).
Secondary
To assess the effect of 2 weeks of continuous monitoring using Zio Patch on:
Objective
i) the proportion of participants diagnosed with AF compared to usual care
at 2.5 years of follow-up in subgroups split by age (<80 and ≥80 years) and by
sex;
ji) the mean times with AF diagnosed compared to usual care after 5 years of
follow-up from randomization in the overall cohort, and in subgroups split by
age (<80 and ≥80 years) and by sex.
Protocol
CTSU_AMALFI 1
Number
ISRCTN number
15544176

```

### DOC-002 physical PDF page 5 — PLAN, fresh GPU OCR

```text
Date and version No: 2021-06-08 Version 2.0
ISRCTN15544176
2.ABBREVIATIONS
AF
Atrial Fibrillation
AHRE
Atrial High Rate Episodes
CHA2DS2-VASc
Ischaemic stroke risk prediction tool for patients with AF (see Appendix 1)
CTSU
Clinical Trial Service Unit & Epidemiological Studies Unit
ECG
Electrocardiogram
FDA
Food & Drug Administration
GCP
Good Clinical Practice
GP
General Practitioner
HRA
Health Research Authority
NHS
National Health Service
NIHR
National Institute for Health Research
SCAF
Silent/sub-clinical AF

```

### DOC-002 physical PDF page 6 — PLAN, fresh GPU OCR

```text
Date andversionNo:2021-06-08Version 2.0
ISRCTN15544176
3.BACKGROUNDANDRATIONALE
3.1 AF: A global health problem associated with substantial morbidity and mortality
Atrial fibrillation (AF) is a rapidly growing public health and economic burden.1 The global number
of individualswith clinicallydiagnosed AFwas estimatedtobe33 millionin2010 and is expected
to double by 2050.12 Based on clinical cases, 9 million people above the age of 55 years are
expected to have AF in Europe alone; this number is predicted to rise to about 18 million by 2060
diabetes and hypertension.3 AF is associated with substantial morbidity and mortality (mostly
secondary to an increased risk of stroke),reduced quality of life, and a considerable financial
burden.1,24 In the UK, the cost of caring for patients with AF and its complications in the year 2000
accounted for around 1-2% of total NHS expenditure.5
These figures arelikely to underestimate the trueprevalence ofAF,as analysis ofprolonged ECG
monitoring in patients presenting in sinus rhythm has detected silent/sub-clinical AF (SCAF)
episodes in around 6-45% of subjects, depending on the type and duration of monitoring, the
characteristics of the study population (in particular, age and medical history), and the definition
of AF.6 sCAF may have a significant impact on health and disability;7 for example, it may be linked
which represent approximately 25% of all ischaemic strokes).8-10
3.2DetectingSCAF
AkeylimitingfactorinthedetectionofSCAFistheshort-lastingandinfrequentnatureofthe
low specificity and sensitivity for AF diagnosis. A systematic review, including 30 studies and over
122,oo0 participants, found that the prevalence of SCAF detected by single time-point screening
(by ECG or pulse palpation) was modest (1.0%, 95% Cl 0.89-1.04% in all participants and 1.4%
without known AF aged 75-76 detected SCAF in 0.5% of their cohort on the first ECG. However,
with repeated intermittent ECGs (mean 26 per participant) over a two week period, this
proportion increased to 3%.14
By contrast, long-term ECG monitoring using an implanted device in very high-risk older patients
detected a SCAF rate (AF episodes lasting ≥ 5 minutes) of 34% per person year (95% Cl, 28-43%).
In these very high-risk patients, longer durations of SCAF were also common, with rates of AF ≥30
minutes, ≥6 hours and ≥24 hours being ~22%, ~7%, and ~3% per person year, respectively.11
Similarly, in patients with a recent cryptogenic stroke (in whom AF was initially excluded by 12-
lead ECG and 24 hours or longer Holter ECG recordings), long-term ECG monitoring using an
implanted cardiac monitor detected AF in 8.9% of participants at 6 months (vs. 1.4% in those
allocated to standard care).10 The EMBRACE study found a 5-fold increase in AF detection using a
30-day event recorder compared to conventional ECG monitoring.9
In summary, whilst the reported prevalence of SCAF varies depending on the screening
significant proportion of individuals with undetected AF across healthcare systems and for these
individuals,strokemaybeSCAF'sfirst clinical manifestation.

```

### DOC-002 physical PDF page 7 — PLAN, fresh GPU OCR

```text
Date and version No:2021-06-08Version 2.0
ISRCTN15544176
3.3IsstrokeriskdifferentinSCAF?
Patients with clinically diagnosed AF have a five-fold increase in the risk of ischaemic stroke.
Strokesthatarerelated tounderlyingAFhavebeenassociatedwithgreaterneurologicaldeficit
and an increased risk of permanent disability compared to non-embolic strokes.9,15 Effective
prevention ofthromboembolicevents is available and well-established.Oralanticoagulationwith
either a vitaminK antagonist or a direct oral anticoagulant(DoAC), when used appropriately in
patients with AF and a CHA2DS2-VASc score ≥2 (see Appendix 1), can reduce stroke risk by up to
  a   s    si    o   g
assess them for oral anticoagulation.
There are limited data to allow a comparison of outcomes in patients with SCAF versus clinically
diagnosed AF. A meta-analysis, which included only 2 randomized trials and 4 observational
difference in outcomes(andwide confidence intervals)betweenthose withSCAFvs thosewith
symptomatic AF: all-cause death (RR 1.38, 95% CI 0.82-2.17); cardiovascular death (RR 0.85, 95%
Cl 0.53-1.36); and stroke/thromboembolism (RR 1.72, (95% Cl 0.59-5.08).17 However, the
significant heterogeneity across these studies may account for the lack of difference in outcomes.
Rhythm data recorded by cardiac implanted electronic devices have also been used to assess the
relative risk of stroke in patients with device-detected SCAF. In contrast to studies with
documented 12-lead ECG evidence of AF, implanted devices may also detect other atrial
tachyarrhythmias or be over-sensing and thus they refer to"atrial high rate episodes"(AHRE)
withcut-offratesand durationsvaryingbetweenstudies.6TheASSERTtrial studied 2500patients
history of AF, and interrogated the devices for AHRE (defined as atrial episodes at a rate of >190
beat/min lasting at least 6 minutes) at 3 months after implantation.18 After a mean follow-up of
2.5 years, those found to have subclinical AHRE in the first 3-months had a 2.5-fold increase in
about half of what would be expected in similar patients with persistent AF.18 More recently, the
ASSERTinvestigatorshaveexamined therelationshipbetweendurationofAHREepisodesand the
occurrenceofstroke orsystemicembolismand found thatpatientswithAHREdurationbetween
6 minutes and 24 hours were not significantly different from patients without SCAF. Only AHRE
episodes >24 hours were associated with an increased risk of ischaemic stroke or systemic
embolism.19
ontheSCAFburdenandthepresenceofestablishedriskfactorsforischaemicstroke.
3.4 Wilson &Jungner criteria for screening
Screening for AF would adhere to many of theWilson&Jungner principles for a screening
prevalence between 1 and 35% depending on age, risk factors, duration of monitoring and
definition of AF in terms of duration of arrhythmia. There is a range of potential approaches to
screening, including non-invasive tests with a high degree of acceptability to participants.AFis an
important risk factor for stroke and there is an established,highly effective preventative
treatment for AF-associated thromboembolic events in the form of anticoagulation.Failure to
identify and treat AF leavespatients at a considerablyhigher risk of stroke,disability and death.

```

### DOC-002 physical PDF page 8 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
There are precedents from other successful screening programmes. For instance, in 2o03 the UK
established the first national screening programme in the world for diabetic retinopathy. Retinal
yet diabetic retinopathy was the leading cause of blindness in diabetic adults. Relying on primary
it was technically difficult and not given protected time in routine care. Retinal photography at
that time required expensive equipment and highly skilled staff. As a result diabetic retinopathy
was typically not diagnosed until late-stage, irreversible disease had developed. Nationwide
obtained from screening now allows the healthcare team to identify individuals who would
benefit from early intervention, thereby slowing or preventing disease progression.21,22
3.5ApproachestoscreeningforSCAF
infrequent and thus potentially difficult to capture. Screening for SCAF has previously been
suggested and trialled, although a Cochrane review found only one study met their inclusion
screening with a single ECG increased AF detection over usual care (OR 1.58, 95% Cl 1.10 - 2.29;
and OR 1.57, 95% Cl 1.08 - 2.26, respectively).23 Opportunistic screening appeared to be more
for systematic screening.24 However, opportunistic screening relies on healthcare professionals
adding to theirusual dailywork a taskwhich may oftenbe overlooked.Furthermore,single time-
point ECGs can considerably under-estimate the prevalence of SCAF and so a systematic approach
with a prolonged period of screening may improve detection rates and reduce the number of
subsequent adverse events (e.g. stroke).
Morerecently theREHEARSE-AFinvestigators randomized 10o0 UKpatients≥65years oldwith a
CHADS-VASc score ≥2 totwice-weekly ambulatoryECG monitoring(30 seconds of singlelead
monitoring using the AliveCor Kardia monitor attached to a WiFi-enabled iPod,“iECG")versus
routine care.Over the 12-month study period there was a 4-fold increase in AF diagnosis in the
iECG group compared with routine care (19 vs 5, HR 3.9, 95% CI 1.4-10.4,p=0.007) at a cost of
around f8oo0 per AF diagnosis. The device was reported to be easy to use and acceptable to this
group of patients.25
The Zio Patch (iRhythm Technologies, San Francisco CA) is a non-invasive single lead ECG
monitoring device. Unlike a Holter monitor, the Zio Patch is discrete and water-resistant, and
allows the person wearing it to participate in all routine daily activities with minimal disruption.
In a pilot study among about 1600 participants of UK Biobank, acceptability was good and the
median wear time was 12.7 days with a median analysable ECG time of 99.1%. iRhythm
Technologies have developed and validated an automated system that processes and analyses
the ECG data (the ZEUS system) using beat-by-beat QRS detection and a sophisticated analysis
algorithm to detect rhythm disturbances such as AF and atrial flutter, their rate, frequency and
duration and the total AF burden. The output of the automated analysis is checked by a trained
operator and a detailedreport isprovided to theGPbymail.FDAapproval hasbeenreceived to
use the Zio Patch and the ZEUS algorithm in clinical practice, and the system was launched in the
UK in October 2014. The device has been subject to NICE evaluation.26

```

### DOC-002 physical PDF page 9 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
3.6AFscreeningaccordingtoage
the optimal age group in whom screening should be performed. The prevalence of clinically diagnosed
AF is associated with increasing age (from 0.1% in adults <55 years, to 9% in those aged ≥80
years).27 It is therefore reasonable to expect that subclinical atrial fibrillation is also more frequent
in older populations - hence, screening yield (i.e. the proportion of new AF found in a particular
Given that any downstream clinical benefits from screening will be determined by the amount of
subclinical AF detected (versus a control group), screening older populations may yield larger
differencesinAF detection,initiation of anticoagulation,and reductioninembolic stroke(also as
stroke risk is higherin older people). This "enrichment" based on age may dictate more favourable
cost-effectivenessassessments.
However, older patients also have increased healthcare contact and are more likely to undergo
cardiac monitoring for clinical purposes (other than screening)，potentially increasing the
potential Quality-Adjusted Life years to be gained from medical interventions, may have physical
or cognitive limitations that hinder their participation in screening programmes, and have
were to be detected. Assessment of the impact of screening for SCAF in younger and older age
groups will help inform the choice of population for any future screening programme.
3.7AFscreeningaccordingtosex
AF incidence is ~50% higher in males (potentially explained by higher cardiovascular risk factor
prevalence), with women typically developing AF about 10 years later than men.28,29 This
difference could potentially mean that screening for AF would be more effective in men than
women.23 However, the lifetime risk of developing AF may be similar in both sexes (>30%), as
outcomes.For example,whilemenaremorelikely to attendcolorectalscreening than
women,30,31 they may be more reluctant to contact their healthcare providers and less likely to
attend healthcare services.32,33 Confirmation of screening efficacy and cost-effectiveness in both
4.STUDYAIMS
TheAMALFl trialaimstodetermine the effect of 2 weeks of continuous non-invasiveECG
a follow up period of 5years among high-riskindividuals.Practiceguidelines recommend oral
burden.34,35 By targeting the screening to those older than 65 years and with a CHA2DS2-VASc
identified with SCAF can be directly informed by current guidelines.35
Theprimary outcome is diagnosis of AF(asrecorded in the electronic GPrecord)by2.5years of
follow up from randomization (i.e. at around the midpoint of a proposed 5-year screening
interval).

```

### DOC-002 physical PDF page 10 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
The secondaryoutcomesfor the studyinclude assessment of theprimary outcomein subgroups
splitbyage(<80and≥80years)andbysexat2.5years,aswellastheeffectofmonitoringonthe
times with AF diagnosed (as above) by 5 years of follow-up in the overall cohort and in the same
subgroups.
Furtheranalyseswillalsoincludecost-effectivenessassessmentsaimedatcapturingdifferences
in healthcare resources, jointly with differences in health-related quality of life, AF cases and
futureAF-relatedevents.
5.STUDYDESIGN
AMALFl is a randomized controlled trial comparing a single 2-week screening period for AF with
theZioPatchtousualcareinindividualswithnohistoryofAFandelevatedriskofstroke,based
on the CHAzDS2-VASc score (see Appendix 1). Eligible participants will be identified via an
electronic search of GP practice data, approached by mail by their GP and offered the opportunity
to participate. In total, at least 2500 and up to 5000 participants will be randomized to Zio Patch
or usual care and will be followed-up for an average of about 25 years (Figure 1), initially via their
GP records for the primary and secondary outcomes and then via NHS Digital only. A preliminary
feasibility study will be conducted to identify and resolve potential practical issues, e.g. difficulties
with patients self-administering devices.
Participants in the Zio Patch arm will be sent a barcoded Zio Patch to self-administer,36 which will
be returned by post directly to the UK iRhythm office for processing before the data is sent to
iRhythm's laboratories in the USA for analysis. A report detailing any AF episodes and burden over
the duration of ECG recording will be sent by iRhythm to the Central Coordinating Office, CTSU,
whowillbeabletolinkthereporttotheindividualparticipantviathepatchbarcode.Thestudy
team will thenprovide relevant informationrelated to the presence and duration of AF to the
participant's GP. The study team will not directly initiate treatment or act on the information from
the Zio Patch data. Instead, a letter detailing relevant results related to the diagnosis of AF will be
sent back to the participant's GP. The subsequent management will be at the discretion of the
GP,allowing the doctor and participant to discuss the management strategy, including
anticoagulation,independently.
Relevant outcome data from the electronic health record (including both GP-held data and
centrally-held data from NHS Digital) data will be collected at about 1 year from randomization*,
analyses)andat5yearsfromrandomization(foranalysisofthesecondaryoutcomeofmean
timeswithAF andrespective subgroupanalyses).Data items will include documentation of AF
diagnosis in the GP record,medication use (including anticoagulants) and hospital attendance
and admission information.Furtherfollowup,via NHS Digital central records,will then takeplace
atintervalsoverthefollowing20years.
*Although the primary and secondary outcomes will be based on data collected at 2.5 and 5 years respectively from
randomization,apreliminarydata collectionwill beundertakenat1yeartoensurethatfullfollow-upinformationis
availableforparticipantswhomovetoadifferentGPpracticeorwhodiepriortothe2.5yeardatacollection.

```

### DOC-002 physical PDF page 11 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
Figure 1: Outline of trial design
Highriskpopulation,identifiedfromprimarycareelectronicrecords:
aged≥54;CHA2DS2-VASc≥3(men),≥4(women)
Randomiseupto5oo0individuals
Up to2500:ScreeningforSCAF
Up to 2500:Usual care
(ZioPatchtobewornfor2weeks)
Follow-upfor5years
KeyoutcomesobtainedfromelectronicGPrecords
Primary outcome
·ProportionofparticipantswithnewdiagnosisofAF2.5yearsafterrandomisation(overallcohort)
Secondaryoutcomes
ProportionofparticipantswithnewdiagnosisofAF2.5yearsafterrandomisation(<80and≥80years)
·Mean timeswithAF diagnosed5years after randomisation
(overallcohort,andseparatelyin<80 and≥80years,and menandwomen)
6.PARTICIPANTIDENTIFICATION
6.1 Study Participants
Participants are eligible for randomization if they satisfy all the inclusion and exclusion criteria
and their GP is agreeable to their participation.
6.2InclusionCriteria
·
Male or Female, aged ≥65 years old.
CHA2DS2-VASc score ≥3 in men or ≥4 in women (see Appendix 1)
Participant is willing and able to give informed consent for participation in the study.
6.3ExclusionCriteria
The participant may not enter the study if ANY of the following apply:
Known to have AF or atrial flutter
Latex allergy (given the potential for an allergic reaction to the Zio Patch).
7.STUDYPROCEDURES
7.1 Recruitment
GP practices (identified via local Clinical Research Networks and by direct approach) will identify
eligible patients by running a predetermined electronic search of the practice database using the
relevant local primary care software e.g. EMis, SystemOne. An invitation letter, including an
information leaflet, consent form, and Freepost return envelope, will then be sent by post (or, if

```

### DOC-002 physical PDF page 12 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
practical, electronically via email) by the GP. Web-based and written study information will be
available toprovide potentialparticipants withfurtherinformation to help themmake an
informed decision as to whether to participate. A 24-hour Freephone service (established by CTSU
for other large heart disease trials) will be available for study participants, their carers or their
doctors to discuss any aspects of the study with experienced clinical staff at the coordinating
centre.
7.2EnrolmentandEligibilityAssessment
There will be no face to face confirmation of eligibility. Participants will be asked to complete a
baseline randomization questionnaire at the time of enrolment. This will include basic
demographicinformation aswell as medical information to confirm baseline CHA2DS2-VASc score
(e.g. history of hypertension, stroke or diabetes, see Appendix 1).
7.3InformedConsent
All participants will be required to provide written informed consent by returning a completed
consent form to the coordinating centre. Information for participants regarding the study will be
availableonthestudywebsiteandinwrittenform.Therewillbetheoptionfortelephoneoremail
enquiries to be made to the study team for any questions prior to enrolment. It will be clearly
stated that the participant is free to withdraw from the study at any time for any reason without
prejudice to future care, without affecting their legal rights, and with no obligation to give the
reasonfor withdrawal.The participantwill be allowed asmuch time aswished to consider the
information, and the opportunity to question the study team, their GP or other independent
parties to decide whether they will participate in the study. The original signed consent form will
be retained at the central coordinating office and a copy will be returned to all participants who
subsequently go on tobe randomized into the trial.
7.4 Randomization, blinding and code-breaking
Participantswhoindicate on the randomization questionnaire that they are eligible and willing to
join the trial, and provide written consent will be randomized by the central computer in CTSU,
using a minimisation algorithm to ensure balance by important baseline variables.37
Eligible patients will be randomized in a 1:1 ratio to a single 2-week ECG monitoring period with
the Zio Patch versus usual care. The study will not employ a sham-patch and neither the trial team
nor the participants will be blinded to the intervention.Allparticipants will receive a letter
informing them which group them have been assigned to. The participant's GP will be notified
that the participant has been randomized and the study arm; a copy of the participant's consent
form (signature page) will also be included for reference. For all participants screened with the
ZioPatch,GP'swill besenttheECGfindingsrelated tothepresence and duration ofAFepisodes,
monitoring). Participants will also be sent this results letter, along with a cover letter. Future
management of the monitoring results will be at the GPs discretion.Additional findings will also
be communicated to GPs if considered to be clinically important. A complete monitoring report
(including all incidental findings) will not be routinely provided to GPs but will be available if
required.

```

### DOC-002 physical PDF page 13 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
7.5ZioPatch administration
For those participants randomized to receive the Zio Patch, the device will be posted to their
home address with instructions on how to apply and care for it. Email and Freephone telephone
advice lines will be available for those who need support or encounter problems.
Participants will be asked to wear the Zio Patch continuously for 2 weeks. A return envelope will
be provided so that, once the two weekperiod is completed,participants can postback the device
for analysis. If participants do not return the device, efforts will be made by the research team to
contact them to encourage them to return the device.
7.6EQ-5Dquestionnaires
In order to inform the planned cost-effectiveness analyses, randomized participants will be asked
to self-complete an EQ-5D questionnaire (either via postal or digital methods) once recruitment
hasbeencompletedandatabout2.5yearsafterwards.
7.7 Discontinuation/Withdrawal of Participants from Study
Each participant has the right to withdraw from the study at any time, which will be made clear
during the consent process. Any withdrawals will be recorded in the study database, including,
whereavailable,thereasonfordoingso.
7.8 Definition of End of Study
Theendofstudyisdefinedasthedateof thelastelectronicdatadownload(fromeithercentral
registries (NHS Digital) or from a participating GP practice. For the primary comparison, data will
be sought at 2.5 years after randomization. For the secondary outcome of mean times with AF,
further data will be sought at 5 years after randomization. However it is intended to continue to
request longer-term data fromNHSDigital(forupto25years afterrandomization) in order to
(see Section 8.4).
8.STATISTICSANDANALYSIS
8.1 Initialassumptions
Study duration:Logically,the lengthof the study should be the proposed time between
screenings if this were put into practice. This will be achieved through the assessment of the
secondary outcome of mean times with AF diagnosed at 5 years. However, a follow-up period of
25 years is proposed in AMALFl to allow for further research.
in this population is unclear. Data from a 2014/2015 screening initiative across Dorset Clinical
the age of 65 who had a one-off pulse check while attending a flu clinic.38 However the proportion
of attendees receiving a pulse check varied considerably between practices, ranging from 8% to
78% of individuals, with an average of 51%. So, among all those aged ≥65 years old SCAF may only
be detected opportunistically in about 0.3-0.4% per annum.

```

### DOC-002 physical PDF page 14 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
The AMALFI population (with elevated CHA2DS2-VASc score) will tend to be at somewhat higher
risk of SCAF, and so we anticipate that usual care with opportunistic screening by the GP may
identify AF in about 0.7% per annum.
AF detection with screening: The incidence of SCAF detection by screening with Zio Patch is
unknown in this high risk population. Among 70o0 people aged 75 screened with intermittent
ECGs over a 2-week period, the rate of detection of SCAF was about 3%.14 However, in AMALFl
the monitoring will be continuous for two weeks (likely to provide higher rates of detection).
Taking into account a moderate level of non-compliance with the patch, we estimate that a two-
week screeningwith ZioPatch maylead to a diagnosis of AFin around 3.75% participants.Details
ofthe assumptions andmodelling ofthe rates for the purposes of thestatisticalpower
calculationscanbefound in appendix2.
AF detection after the screening period: In the screening group it is anticipated that further cases
will continue to be identified by usual care after screening. These rates are assumed to increase
with time from screening to converge with the rate found by usual care (0.7% per annum) and
range from 0.2% during the first year following randomization, to 0.5% during the fifth year (see
Appendix 2).
8.2Samplesizeandpredictednumberofdiagnoses
Given theassumptionsabove,the expectedprevalenceofAF over time intheAMALFI trialis
shown in Figure 2 (see Appendix 2 forstatistical model and calculations).
Figure 2:Estimated cumulative percent of participants diagnosed with AF
6%
Percent diagnosed with AF
5%%
Controlarm:Cumulative%
ofpatientsdiagnosedwith
3%
AFby theendof thetime
period
2%
Activearm:Cumulative%of
1%
patientsdiagnosedwithAF
by theendofthetimeperiod
0%
0
1
2
3
4
5
Time from randomization (years)
than90%power todetect the estimated differenceinproportionwith a diagnosis of AF at 2.5
overall sample sizewasset at25o0 participants.
As recruitment progressed, it became apparent that the trial would be able to achieve its initial
possibility of extending recruitment in a cost-effective way. Based on over 1250 participants
detection rates by patch, a larger sample size of up to 5oo0 participants provides increased

```

### DOC-002 physical PDF page 15 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
be required to maintain >90% at 2p<0.05 if the ratio were to be 2 instead of 2.5 as predicted, with
4100 participants required to maintain >90% power at 2p<0.01). Furthermore an increase in
samplesize allowsforreliableassessmentoftheeffectsofscreeningforSCAFintheproposed
subgroups (by age and by sex).
8.3Analysisofoutcomemeasures
The fundamental assessments of efficacy will involve an “intention-to-treat" analysis among all
randomized patients of allocation to screening versus allocation to usual care, irrespective of
compliance.
Analysisoftheprimaryoutcome:
AFat 2.5years offollowupin allthoserandomizedtoscreeningversus allthose
randomized tousual care.
Analysisofthesecondaryoutcomes:
Thechi-squaretestwillbeusedtocomparetheproportionofparticipantsdiagnosedwith
AF at 2.5 years of follow up in those randomized to screening versus those randomized to
usual care separately by age subgroups of <80 and ≥80 years and by sex subgroups at
Mean durations of time with AF diagnosed after 5 years of follow-up from randomization
in all those randomized to screening compared to all those randomized to usual care will
be compared using a permutation test to assess statistical significance (in the overall
randomization, with a test for heterogeneity between the two subgroups). Those with no
diagnosis of AF by the end of the study will contribute zero time with AF.
8.4 Cost-effectiveness analyses
will also inform a cost-effectiveness analysis aimed at capturing differences in healthcare
quality of life (based on the standard EQ-5D questionnaire), AF cases, and AF-related events.
Details of theseanalyseswill bedescribed ina separate analysisplan.
8.5Exploratoryassessments
Assessment of the effects of screening for SCAF in those ≥75 years old is of interest from a clinical
perspective. This age threshold is included in the calculation of the CHA2DS2-VASc score and all
individuals ≥75 years old would warrant consideration for initiation of anticoagulation if AF were
to be detected. However, based on the initial randomization of 1250 participants and their
observed adherence to wearing the patch, age distributions and AF detection rates by patch, even
a trial of 5000 participants would have limited statistical power in the subgroup aged <75 years

```

### DOC-002 physical PDF page 16 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
at randomization.Therefore,the confirmation of the study resultsinthese two subgroupswill be
performed as an exploratory assessment only.
8.5.2 Rates of anticoagulation and hospitalization between screen-detected and clinically-
detectedAF(non-randomizedassessment)
With only about 5o0 cases of AF expected during the 5-year period of the trial, a randomized
comparison of the effects of screening for SCAF on the prevention of AF-related morbidity and
mortality would have very low statistical power. However, in orderto explore the potential clinical
impact of screening we will perform an exploratory retrospective non-randomized comparison of
rates of anticoagulation and of hospitalization (inpatient and outpatient) among those who were
by Zio Patch screening or by usual care. It is recognised that such non-randomized comparisons
have considerable limitations. However it is hypothesised that the mode of diagnosis of AF may
influence future management decisions (for example the decision whether to anticoagulate or
in exploring such potential clinical management biases.
8.5.3 Long-term assessments
After the end of the scheduled study period, information about hospitalizations, medications, and
other clinical eventswill continue tobe collected from NHS Digital on all surviving participants
(unless theyhavewithdrawnconsent)foruptoanadditional20years.Thesedatawillbeused
for longer-term exploratory assessments of the clinical impact of screening.
9.DATAMANAGEMENT
9.1AccesstoData
Direct access will be granted to authorised representatives from the Sponsor and host institution
for monitoring and/or audit of the study to ensure compliance with regulations.
9.2 Data Recording and Record Keeping
protected and following an operating procedure for data handling. Access to the data is granted
on a 'need-to-know' basis, authorised by the study managers. All personal identifiers will be
strongly encrypted and eachparticipant allocated a study number at the point of enrolment. It
willbepossibletocheckback against theinitialstudynumber allocationtoidentifyindividual
participants when necessary in the case of safety reasons or when needing to contact practices
with results or request follow-up data.
All data will be held securely on computer servers managed by the University of Oxford, analysed
by appropriately qualified staff with access restricted as appropriate for their role in the study,
and used only for the medical research purposes outlined in this protocol. The data will be held
for at least 25 years after the completion of the study and only used for the AMALFl study.
10.ETHICALANDREGULATORYCONSIDERATIONS
TheChief Investigatorwillensurethatthisstudyis conducted in accordancewith theprinciples
oftheDeclarationofHelsinki,andofGoodClinicalPracticeandinaccordancewithrelevant

```

### DOC-002 physical PDF page 17 — PLAN, fresh GPU OCR

```text
Date andversionNo:2021-06-08Version 2.0
ISRCTN15544176
regulations. The protocol, informed consent form, participant information sheet and any
proposed advertising material (including all relevant substantial amendments to the original
approved documents) will be submitted to the Health Research Authority (HRA) for written
approval. The Chief Investigator shall submit once a year throughout the study,or on request, an
Annual Progress report to the REC Committee, HRA (where required) host organisation and
Sponsor. In addition, an End of Study notification and final report will be submitted to the same
parties.
11.FINANCEANDINSURANCE
The study is funded by the National Institute for Health Research (NlHR) Oxford Biomedical
Research Centre (BRC). iRhythm is providing additional support by providing the Zio Patches and
reporting service free ofcharge during the AMALFl study.The Universityhas a specialist insurance
policy in place which would operate in the event of any participant suffering harm as a result of
their involvement in the research (Newline Underwriting Management Ltd, at Lloyd's of London).
12.PUBLICATIONPOLICY
The Investigators (see page 1) will be involved in reviewing drafts of the manuscripts, abstracts,
press releases and any otherpublications arising from thestudy.Authorswill acknowledge that
the study was funded by the National Institute for HealthResearch(NlHR)Oxford Biomedical
Research Centre(BRC).Authorship will be determined in accordance with the ICMJE guidelines
and other contributors will be acknowledged.

```

### DOC-002 physical PDF page 18 — PLAN, fresh GPU OCR

```text
Date and versionNo:2021-06-08Version2.0
ISRCTN15544176
13. Appendix 1: Calculation of the CHA2DS2-VASc score
Condition
Points
C
Congestive heart failure (or Left ventricular systolic dysfunction)
1
H
Hypertension: blood pressure consistently above 140/90 mmHg
1
(or treated hypertension on medication)
A2
Age ≥75 years
2
D
Diabetes Mellitus
1
S2
PriorStrokeorTIAor thromboembolism
2
V
Vascular disease (e.g. peripheral artery disease, myocardial
1
infarction, aortic plaque)
A
Age 65-74years
1
Sc
Sex category (i.e. female sex)
1

```

### DOC-002 physical PDF page 19 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
14.Appendix 2: Modelling of expected prevalence of AF over time and statistical power
calculations
Primaryoutcomeconsiderations:
(i.e. potentially 5 years). The ideal primary outcome would be the time with AF diagnosed within
5 years of randomization, with those not getting AF having a time of zero with AF. The rationale
is that this represents the window of opportunity for intervention. However, a more pragmatic
alternative outcome,which allowsfora more timelyassessmentof thevalue ofscreeningwith
the ZioPatch,would be the proportion with AF around the middle of the study. The areas under
the curves shown in Figure 2 (see protocol Section 8) give the expected mean times spent with
AF and are mostly driven by the proportions with AF in the middle of the trial. Hence the
proportionof participants withAF at 2.5 years has been chosen as the primary outcome for
AMALFI.
AssumptionsforFigure2(seeprotocolSection8):
Theprobabilityof being diagnosed with AFisatimedependentPoissonprocesswith aparameter
slightly increasing with time, a+bt. Additionally, we assume that if someone would have had AF
diagnosed at time t, there is a decreasing probability e+ft that it would be pre-empted by patch
relatedearlydetectionof AF.We thenchosea and bso that theAFdiagnosisrates duringyears
1 and 2 were both 0.7% per annum, the anticipated detection rate with usual care.
e and fwere chosen to allowfor non-compliance and togive decreasingprobabilities over time
of AFs that would have been diagnosed during a time period being pre-emptively detected by
patch (70% inthe first year,60%in the second year, 50% in the third,40% in the fourth and 30%
in the fifthyear).An additional probability of 2%was assumed for patch related early detection
of AF when no AF would have been detected within 5 years. It is assumed that patch related early
detection of AF occurs evenly over the first 6 months from randomization. Table 1 below gives
the estimated cumulative % of participants being diagnosed with AF at the end of each year,
based onthis model and theassumptions described inSection8 of theprotocol.
Samplesizecalculation:
with AF at half yearly points up to 5 years. It is assumed that participants are randomized 1:1 to
give to equal numbers in the control and active arms. The 2.5 year row is highlighted as being a
suitable mid-study comparison time point for a proposed screening interval of 5 years.
Table 3 provides a summary of power calculations for different samples sizes made possible by
an extension in recruitment of up to 5oo0 participants for the whole cohort and under different
assumptionsregardingAFdetectionratios.Table 4providesthe same calculationsfor different
ageandsexsubgroups.

```

### DOC-002 physical PDF page 20 — PLAN, fresh GPU OCR

```text
Cumulative %
of patients
diagnosed
with AF by
end of year
3.96%
4.24%
4.59%
5.01%
5.50%
(including 2% extra found
 diagnosed with AF during 
% of patients diagnosed
withAFwithintheyear
wouldn't have been
by Zio Patch, who
years 1-5)
3.96%
0.28%
0.35%
0.42%
0.49%
Active arm
patients found to
have AF within the
Additional % of
year, but not with
(continuity corrected)
ISRCTN 15544176
Zio Patch
Total sample size
Page 20 of 26
0.21%
0.28%
0.35%
0.42%
0.49%
1019
1261
1565
1914
2348
2825
3406
4004
4711
 diagnosed
patients
by Zio
% of
Patch
0.49%
0.42%
0.35%
0.28%
0.21%
Power
%06
%06
%06
%06
%06
%06
%06
%06
%06
Table 2- sample size calculations based on the initial assumptions
% of patients who
would have been
found to have AF in
year i, but found up
front by Zio Patch
19/LO/0220
Alpha
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
70%
%09
50%
40%
30%
Expectedproportionwith
Active arm
3.96%
4.10%
4.24%
4.41%
4.59%
4.80%
5.01%
5.25%
5.50%
Ethics Ref:
 AF at time point
ProfessorLouiseBowman
2021-06-08Version2.0
Cumulative %
 of patients
diagnosed
with AF by
end of year
0.70%
1.40%
2.10%
2.80%
3.50%
Control arm
Placebo arm
0.70%
1.05%
1.40%
1.75%
2.10%
2.45%
2.80%
3.15%
3.50%
AMALFI
 % of patients
diagnosed
within the
with AF
Date and version No:
year
0.70%
0.70%
0.70%
0.70%
0.70%
Comparison
time point
Chief Investigator:
1.5
2
3
3.5
5
4
5
Short Title:
Year
end
1
2
3
4
5

```

### DOC-002 physical PDF page 21 — PLAN, fresh GPU OCR

```text
total of
2p<0.01
Power
5000,
100%
100%
%66
%96
for
97%
total of
2p<0.05
Power
5000,
100%
100%
100%
%66
%66
for
Resultingpowerandsamplesizes
for total
Power
of 4000,
2p<0.01
%66
%66
%66
89%
92%
Power
for total
of 4000,
2p<0.05
100%
100%
100%
97%
98%
for total
of 2500,
2p<0.05
Power
%96
%96
97%
84%
88%
ISRCTN15544176
Page 21 of 26
needed
n total
%06 1
power,
p<0.01
2649
2687
2454
4088
3732
needed
n total
%06
power,
p<0.05
1914
1941
1773
2939
2684
detection
Implied
controls
AFrate
(based
1.75%
1.77%
1.93%
2.21%
2.41%
ratio)
.=
on
19/LO/0220
rates in
control
active
Ratio
ofAF
arms
2.52
Vs
2.5
2.5
2
2
rate in
active
arm at
(patch
ratex
1.177)
4.41%
4.41%
4.82%
years
4.41%
4.82%
Total
2.5
Ethics Ref:
AF
Assumptions
Professor Louise Bowman
2021-06-08 Version 2.0
* interim AF detection rateby patch
detected
AFrate
through
patch in
4.09%*
4.09%*
betweenactiveandcontrolgroups
active
3.75%
3.75%
3.75%
arm
population
AMALFI
Percent of
100%
100%
100%
100%
100%
Date and version No:
Chief Investigator:
assumptions)
Whole trial
Whole trial
Whole trial
Whole trial
Whole trial
(original 
Short Title:
Group

```

### DOC-002 physical PDF page 22 — PLAN, fresh GPU OCR

```text
total of
2p<0.01
Power
5000,
34%
100%
for
85%
95%
98%
75%
total of
2p<0.05
Power
5000,
Resulting power and sample sizes
100%
for
95%
%66
52%
%66
89%
total of
2p<0.01
Power
4000,
for
73%
87%
20%
98%
92%
%09
Power
for total
of 4000,
2p<0.05
100%
89%
%96
41%
98%
80%
ISRCTN 15544176
Page 22 of 26
n needed
subgroup
for 90%
power,
p<0.01
3658
1571
4048
2164
2018
3276
ul
 xas pue ase Aq sashieue dnousqns jof suoeinojeo azis aldwes pue samod - t alqei
nneeded
subgroup
for 90%
power,
p<0.05
2642
1135
2924
1563
1458
2367
=
detection
Implied
controls
AF rate
(based
ratio)
1.31%
2.95%
1.18%
2.18%
2.33%
1.46%
.=
on
19/LO/0220
control
active
Ratio
ofAF
rates
arms
ul
VS
Total AFrate
years (patch
rate x 1.177)
arm at 2.5
in active
Ethics Ref:
Assumptions
Professor Louise Bowman
2021-06-08 Version 2.0
3.27%
7.39%
2.96%
5.44%
5.82%
3.64%
 * interim AF detection rate by patch
AFrate
detected
through
patch in
active
arm*
2.78%
6.28%
2.52%
4.62%
4.94%
3.09%
AMALFI
Percent of
population
Date and version No:
64%
36%
25%
75%
54%
46%
Chief Investigator:
Age <80
Age ≥80
Age<75
Age ≥75
Female
Short Title:
Group
Males

```

### DOC-002 physical PDF page 23 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
15.REFERENCES
1.
Chugh SS, Havmoeller R, Narayanan K, et al. Worldwide Epidemiology of Atrial Fibrillation:
A Global Burden of Disease 2010 Study. Circulation. 2014;129(8):837-847.
doi:10.1161/CIRCULATIONAHA.113.005119
2.
Miyasaka Y, Barnes ME, Gersh BJ, et al. Secular Trends in Incidence of Atrial Fibrillation in
Olmsted County, Minnesota, 1980 to 2000, and Implications on the Projections for Future
Prevalence. Circulation. 2006;114(2):119-125. doi:10.1161/CIRCULATIONAHA.105.595140
3.
Krijthe BP, Kunst A, Benjamin EJ, et al. Projections on the number of individuals with atrial
fibrillation in the European Union, from 2000 to 2060. Eur Heart J. 2013;34(35):2746-2751.
doi:10.1093/eurheartj/eht280
4.
Ball J, Carrington MJ, McMurray JJV, Stewart S. Atrial fibrillation: Profile and burden of an
evolving epidemic in the 21st century. IntJ Cardiol.2013;167(5):1807-1824.
doi:10.1016/j.ijcard.2012.12.093
5.
Stewart S, Murphy N, Walker A, McGuire A, McMurray JJV. Cost of an emerging epidemic:
an economic analysis of atrial fibrillation in the UK. Heart. 2004;90(3):286-292.
doi:10.1136/hrt.2002.008748
6.
Freedman B, Camm J, Calkins H,et al. Screening for Atrial Fibrillation:A Report of the AF-
SCREEN International Collaboration. Circulation. 2017;135(19):1851-1867.
doi:10.1161/CIRCULATIONAHA.116.026693
7.
Glotzer TV, Ziegler PD. Cryptogenic stroke: Is silent atrial fibrillation the culprit? Heart
Rhythm. 2015;12(1):234-241.doi:10.1016/j.hrthm.2014.09.058
8.
Sacco RL, Ellenberg JH, Mohr JP, et al. Infarcts of undetermined cause:The NINCDS stroke
data bank.Ann Neurol.1989;25(4):382-390.doi:10.1002/ana.410250410
9.
Gladstone DJ, Spring M, Dorian P, et al. Atrial Fibrillation in Patients with Cryptogenic
Stroke. N Engl J Med. 2014;370(26):2467-2477. doi:10.1056/NEJMoa1311376
10. Sanna T, Diener H-C, Passman RS, et al. Cryptogenic Stroke and Underlying Atrial
Fibrillation. N Engl J Med. 2014;370(26):2478-2486. doi:10.1056/NEJMoa1313600
11.
Healey JS, Alings M, Ha A, et al. Subclinical Atrial Fibrillation in Older Patients. Circulation.
2017;136(14):1276-1283.doi:10.1161/CIRCULATIONAHA.117.028845
12. Brambatti M, Connolly SJ, Gold MR, et al. Temporal Relationship Between Subclinical Atrial
Fibrillation and Embolic Events. Circulation. 2014;129(21):2094-2099.
doi:10.1161/CIRCULATIONAHA.113.007825
13. Lowres N, Neubeck L, Redfern J, Freedman SB. Screening to identify unknown atrial
fibrillation. A systematic review. Thromb Haemost. 2013;110(2):213-222.
doi:10.1160/TH13-02-0165

```

### DOC-002 physical PDF page 24 — PLAN, fresh GPU OCR

```text
Date and versionNo:2021-06-08 Version 2.0
ISRCTN15544176
14. Svennberg E, Engdahl J, Al-Khalili F, Friberg L, Frykman V, Rosenqvist M. Mass Screening for
Untreated Atrial Fibrillation: The STROKESTOP Study. Circulation. 2015;131(25):2176-2184.
doi:10.1161/CIRCULATIONAHA.114.014343
15. Lamassa M, Di Carlo A, Pracucci G, et al. Characteristics, Outcome, and Care of Stroke
AssociatedWithAtrialFibrillationinEurope:DataFroma MulticenterMultinational
2001;32(2):392-398. doi:10.1161/01.STR.32.2.392
16. Hart RG, Sherman DG, Easton JD, Cairns JA.Prevention of stroke in patients with
nonvalvular atrial fibrillation. Neurology. 1998;51(3):674-681. doi:10.1212/WNL.51.3.674
17. Xiong Q, Proietti M, Senoo K, Lip GYH. Asymptomatic versus symptomatic atrial fibrillation:
A systematicreview ofage/gender differences and cardiovascular outcomes.IntJ Cardiol.
2015;191:172-177. doi:10.1016/j.ijcard.2015.05.011
Evaluation in pacemaker patients and the atrial fibrillation Reduction atrial pacing Trial
(ASSERT). Am Heart J. 2006;152(3):442-447. doi:10.1016/j.ahj.2006.02.016
19. Van Gelder IC, Healey JS, Crijns HJGM, et al. Duration of device-detected subclinical atrial
fibrillation and occurrence of stroke in ASSERT. Eur Heart J. 2017;38(17):1339-1344.
doi:10.1093/eurheartj/ehx042
20. Wilson JMG, Jungner G, Organization WH. Principles and practice of screening for disease.
Publishedonline1968.AccessedMarch4,2019.
https://apps.who.int/iris/handle/10665/37650
21. Arun CS, Al-Bermani A, Stannard K, Taylor R. Long-term impact of retinal screening on
significant diabetes-related visual impairment in the working age population. Diabet Med.
2009;26(5):489-492. doi:10.1111/j.1464-5491.2009.02718.x
22. Misra A, Bachmann MO, Greenwood RH, et al.Trends in yield and effects of screening
intervals during 17 years of a large UK community-based diabetic retinopathy screening
programme. Diabet Med. 2009;26(10):1040-1047. doi:10.1111/j.1464-5491.2009.02820.x
23. Moran PS, Teljeur C, Ryan M, Smith SM. Systematic screening for the detection of atrial
fibrillation. Cochrane Database Syst Rev. 2016;(6):CD009586.
doi:10.1002/14651858.CD009586.pub3
24. Fitzmaurice DA, Hobbs FD, Jowett S, et al. Screening versus routine practice in detection of
2007;335(7616):383. doi:10.1136/bmj.39280.660567.55
25. Halcox JPJ, Wareham K, Cardew A, et al. Assessment of Remote Heart Rhythm Sampling
Using the AliveCor Heart Monitor toScreenforAtrial Fibrillation: The REHEARSE-AF Study.
Circulation. 2017;136(19):1784-1794. doi:10.1161/CIRCULATIONAHA.117.030583

```

### DOC-002 physical PDF page 25 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
26. NICE. Zio Service for Detecting Cardiac Arrhythmias. Medtech Innovation Briefing [MIB101]
Published Date:March 2017.(Ed.Excellence,N.1.f.H.a.C.)
(Https://Www.Nice.Org.Uk/Advice/Mib101, 2017).
27.Go AS, Hylek EM, Phillips KA, et al. Prevalence of Diagnosed Atrial Fibrillation in Adults:
and Risk Factors In Atrial Fibrillation (ATRIA) Study. JAMA. 2001;285(18):2370-2375.
doi:10.1001/jama.285.18.2370
28.1
Magnussen C, Niiranen TJ, Ojeda FM, et al. Sex Differences and Similarities in Atrial
Fibrillation Epidemiology,Risk Factors,and Mortalityin Community Cohorts:Results From
the BiomarCaRE Consortium (Biomarker for Cardiovascular Risk Assessment in Europe).
Circulation. 2017;136(17):1588-1597. doi:10.1161/CIRCULATIONAHA.117.028981
29. Benjamin EJ, Levy D, Vaziri SM, D'Agostino RB, Belanger AJ, Wolf PA. Independent risk
factors for atrial fibrillation in a population-based cohort. The Framingham Heart Study.
JAMA.1994;271(11):840-844.
30. Friedemann-Sanchez G, Griffin JM, Partin MR. Gender differences in colorectal cancer
31. Wardle J, Miles A, Atkin W. Gender differences in utilization of colorectal cancer screening.
J Med Screen.2005;12(1):20-27.doi:10.1258/0969141053279158
32. Peate I. Men's attitudes towards health and the implications for nursing care. Br J Nurs
33.Centre for Disease Control. Utilization of Ambulatory Medical Care by Women: United
States, 1997-98. Series Report 13, No. 149, 2001.; 2001.Accessed May 25, 2021.
www.cdc.gov/nchs/data/series/sr_13/sr13_149.pdf
34. January CT, Wann LS, Alpert JS, et al. 2014 AHA/ACC/HRS Guideline for the Management of
Patients With Atrial Fibrillation. J Am Coll Cardiol. 2014;64(21):e1-e76.
doi:10.1016/j.jacc.2014.03.022
35. Kirchhof P, Benussi S, Kotecha D, et al. 2016 ESC Guidelines for the management of atrial
fibrillation developed in collaboration with EACTS.EurHeart J.2016;37(38):2893-2962.
doi:10.1093/eurheartj/ehw210
36.Engel JM, Chakravarthy N, Katra RP, Mazar S, Libbus I, Chavan A. Estimation of patient
compliance in application of adherent mobile cardiac telemetry device. In:2011 Annual
2011:1536-1539.doi:10.1109/IEMBS.2011.6090448
37. Pocock SJ, Simon R. Sequential treatment assignment with balancing for prognostic factors
in the controlled clinical trial. Biometrics. 1975;31(1):103-115.

```

### DOC-002 physical PDF page 26 — PLAN, fresh GPU OCR

```text
DateandversionNo:2021-06-08Version2.0
ISRCTN15544176
38.OpportunisticScreeningforAtrialFibrillationforover65YearOldsduringFluClinics and
Anticoagulation for the Prevention of Stroke in Primary Care.(Ed. Group, D.C.C.).
(http://www.londonscn.nhs.uk/wp-content/uploads/2017/07/dorset-ccg.pdf, 2015).

```

### DOC-003 physical PDF page 1 — PLAN, fresh layout

```text
                                    xxxx





           Statistical Analysis Plan
                       Version 1.2

                    Date: 26 June 2025

          Aligned with protocol version: 2.0, 08 June 2021

                     IRAS no: 234837

                 REC ref: 19/LO/0220

                     ISRCTN: 15544176





AMALFI Statistical Analysis Plan v1.2 2025_06_26                                            1
```

### DOC-003 physical PDF page 2 — PLAN, fresh layout

```text
Table of Contents

1   Roles and responsibilities ................................................................................................................... 4
2   Introduction .............................................................................................................................................. 5

3  Background .............................................................................................................................................. 5

        Rationale .......................................................................................................................................... 5

          Trial objectives ............................................................................................................................... 5

          Trial design ...................................................................................................................................... 6

           Eligibility............................................................................................................................................ 6

    3.4.1    Inclusion criteria .................................................................................................................... 6

    3.4.2    Exclusion criteria ................................................................................................................... 6

         Intervention ..................................................................................................................................... 6

       Outcome comparisons ................................................................................................................ 7

    3.6.1   Primary outcome assessment ......................................................................................... 7

    3.6.2   Secondary outcome assessments.................................................................................. 8

    3.6.3    Exploratory outcomes ......................................................................................................... 9

    3.6.4   Outcome derivation ............................................................................................................. 9

        Hypothesis framework ................................................................................................................ 9

       Randomisation ............................................................................................................................... 9

        Blinding ............................................................................................................................................. 9

         Data collection schedule ........................................................................................................ 9

    3.10.1  Self-reported medical history .......................................................................................... 9

    3.10.2  Primary care data............................................................................................................... 10

    3.10.3  Healthcare systems data ................................................................................................ 10

    3.10.4  Health-related quality of life data ................................................................................ 11

    3.10.5  End of study .......................................................................................................................... 11

         Data monitoring ...................................................................................................................... 12

            Trial reporting ........................................................................................................................... 12

4   Analysis populations .......................................................................................................................... 12

        Population definitions ................................................................................................................ 12

       Length of follow-up .................................................................................................................... 12

    4.2.1   Primary care records ......................................................................................................... 12

    4.2.2    National datasets (medication dispensing) .............................................................. 13

        Censoring ....................................................................................................................................... 13



AMALFI Statistical Analysis Plan v1.2 2025_06_26                                            2
```

### DOC-003 physical PDF page 3 — PLAN, fresh layout

```text
    4.3.1    Left-censoring (pre-randomisation records) ............................................................ 13

    4.3.2    Right-censoring (post-randomisation records) ....................................................... 13

5   Descriptive analyses ........................................................................................................................... 14

         Participant throughput .............................................................................................................. 14

        Baseline characteristics of randomised arms .................................................................. 14

       Completeness and length of follow-up ............................................................................... 16

       Adherence to the study intervention.................................................................................... 17

        Cardiac monitoring findings in the active arm ................................................................. 17

6   Comparative analyses   ..................................................................................................................... 18

        Primary outcome ......................................................................................................................... 18

       Secondary outcomes ................................................................................................................. 18

         Sensitivity analyses .................................................................................................................... 18

        Exploratory outcomes ................................................................................................................ 19

    6.4.1   Time to AF detection within a period of 2.5 and 5 years after randomisation
          19

    6.4.2   Time spent with a known diagnosis of AF within a period of 2.5 years after
    randomisation ....................................................................................................................................... 19

    6.4.3   Rates of oral anticoagulation use ................................................................................ 19

    6.4.4   Long-term assessments of the clinical impact of screening  ............................. 20

       Non-randomised comparisons............................................................................................... 20

    6.5.1   Rates of  oral anticoagulation between screen-detected and  clinically-
    detected AF (non-randomised assessment) ............................................................................. 20

        Non-pre-specified exploratory analyses ............................................................................ 21

        Health economics ........................................................................................................................ 21

       Power calculations ..................................................................................................................... 21

    6.8.1   Power calculations for the primary outcome ........................................................... 21

       Adjustment for baseline characteristics ............................................................................. 22

           Significance levels and adjustment of p-values for multiplicity ............................ 22

7   Statistical software ............................................................................................................................. 23

8   References .............................................................................................................................................. 23

9   Appendices ............................................................................................................................................ 24

       Appendix I: CHA2DS2-VASc Scoring system .................................................................... 24





AMALFI Statistical Analysis Plan v1.2 2025_06_26                                            3
```

### DOC-003 physical PDF page 4 — PLAN, fresh layout

```text
1     Roles and responsibilities
Trial statisticians

Mrs Georgina Buck, Professor Sarah Parish (up until March 2023), Dr Charlie Harper

       Role: To develop the protocol, the statistical analysis plan, and the baseline
characteristics and outcomes derivation document, to prepare analysis datasets, and
conduct the final comparative analyses

Trial investigators

Professor Louise Bowman, Professor Barbara Casadei, Mr Richard Bulbulia, Dr Guilherme
Pessoa-Amorim, Dr Rohan Wijesurendra, Dr Christine A’Court, Dr Nicholas Jones

       Role: To develop the protocol and the statistical analysis plan, oversee the conduct
of the trial, and collect trial data

Trial IT systems and programmers

Rijo Kurien, Ola Murawksa

      Role: To develop and maintain the randomisation and trial management systems
and the clinical databases





AMALFI Statistical Analysis Plan v1.2 2025_06_26                                            4
```

### DOC-003 physical PDF page 5 — PLAN, fresh layout

```text
2     Introduction

This document outlines the proposed analyses concerning results from the AMALFI (Active
Monitoring for AtriaL FIbrillation) trial (ISCRTN 15544176), which is investigating the
impact of remote screening for asymptomatic atrial fibrillation with 14-day continuous
cardiac monitoring on long-term atrial fibrillation (AF) detection.

The planned analyses described here include the trial primary and secondary outcomes,
as well as some pre-specified exploratory analyses. Presentation of these results will
follow the strategy outlined here. Subsequent, additional, non-pre-specified exploratory
analyses will not be bound by this strategy.

Any deviations from the statistical analysis plan will be described and justified in the final
report. The analysis  will be carried out by  identified, appropriately  qualified and
experienced statisticians, who will ensure the integrity of the data during their processing.

3    Background
     Rationale

AF screening has been proposed as a way to prevent stroke by increasing detection of
asymptomatic AF, which might otherwise be missed in usual care. Opportunistic screening
(e.g. pulse-palpation, 12-lead ECG) during healthcare consultations is recommended by
some clinical practice guidelines1. However, international taskforces do not recommend
systematic AF screening, citing the uncertainty regarding both clinical utility and cost-
effectiveness.

AMALFI  is  testing  the  hypothesis  that AF  screening  in people aged 65+ with
cardiovascular risk factors using 14-day ECG monitoring (Zio XT, iRhythm Technologies,
San Francisco, CA, USA) would be cost-effective and lead to increased and earlier AF
detection over 5 years. The trial is comparing mail-based AF screening versus usual care
in this population.

      Trial objectives

The primary objective is to provide reliable estimates of the effect of remote screening for
asymptomatic AF on long-term AF prevalence among individuals aged 65 or more with
additional cardiovascular risk factors. This aim is reflected in the primary outcome of
proportion of participants with a diagnosis of AF (as recorded in primary care data) within
a period of up to 2.5 years after randomisation in each allocation arm.

The secondary objectives are to determine the effect of screening on the mean time spent
with a known diagnosis of AF during a period of up to 5 years after randomisation in each
arm, i.e. the actionable time period for preventative intervention that would be gained by
screening.

Separately, both outcomes specified above will also be assessed by subgroups of age (<80
vs ≥80 years) and sex.



AMALFI Statistical Analysis Plan v1.2 2025_06_26                                            5
```

### DOC-003 physical PDF page 6 — PLAN, fresh layout

```text
       Trial design

This is a remote, streamlined, open-label, randomised controlled trial. Data collection will
be performed mainly through healthcare systems data.

       Eligibility

Eligibility to the study was established based on primary care data available at each
participating GP practice, as recorded at the time of recruitment to the trial (i.e. individuals
were invited if their medical records suggested they were potentially eligible).

3.4.1    Inclusion criteria

Individuals were eligible to enter the trial if all of the following were true (at the point of
eligibility assessment):

      Male or Female, aged ≥65 years old.
      CHA2DS2-VASc score ≥3 in men or ≥4 in women (Appendix I)
       Willing and able to give informed consent for participation in the study (NB
      informed consent was collected remotely by post).

3.4.2    Exclusion criteria

Individuals could not enter the study if EITHER of the following applied:

      Known to have AF or atrial flutter at the point of eligibility assessment (before
        invitation)
      Latex allergy (to reduce the risk of skin reactions in individuals with a history of
       previous reactions to latex, although this was not strictly necessary because latex
         is not a component of the Zio XT device); NB the existence of a potential previous
       latex allergy was identified based on an initial screening assessment using a self-
       reported question (following the initial invitation), and subsequent confirmation via
       telephone with a study clinician.

      Intervention

Participants allocated to the active (screening) arm of the study received a cardiac
monitoring patch (Zio XT) by post, along with instructions on how to apply it, and were
asked to wear it for two weeks. Once the monitoring period was over, participants were
asked to return the patch by mail to iRhythm for analysis. A full cardiac monitoring report
from the analysis of the patch was provided electronically to the study team by iRhythm,
and shared with the participant’s GP immediately by email  if AF or other findings
considered to be clinically relevant (i.e. atrial flutter, sustained ventricular tachycardia or
fibrillation; pauses lasting over 6s; complete heart block, Mobitz type  II, or high grade
atrioventricular block) were found. Separately, the study team received regular structured
data extracts from iRhythm including  all ECG findings. These data were used to
automatically generate a summary  results  letter  (focused on  the presence and
characteristics of any AF found, including AF burden and maximum and minimum AF rate),
which was mailed to each participant and their GP whether or not AF was detected (i.e.



AMALFI Statistical Analysis Plan v1.2 2025_06_26                                            6
```

### DOC-003 physical PDF pages 7–22 — PLAN, reusable complete layout

```text
GPs were contacted twice if AF was present). Subsequent care was at the discretion of
the GP.

Participants allocated to the control (usual care) arm of the study were not requested to
perform any actions directly related to the study, with clinical care remaining at the
discretion of their GP.

        Outcome comparisons
All comparisons of primary, secondary, and exploratory outcomes involve comparing
outcomes among all participants allocated at randomisation to screening versus all
participants allocated to the usual care arm (i.e. “intention-to-treat” analysis), unless
otherwise specified (i.e. non-randomised comparisons).

3.6.1      Primary outcome assessment
The primary objective of this study is to provide reliable estimates of the long-term efficacy
of AF screening. Conceptually, this may be interpreted as the actionable time window of
opportunity for intervention which results, or is gained, from screening. This window is
represented by the difference in areas under the cumulative incidence curves (i.e. time with
a known diagnosis of AF) between the active and control arms, with those not having AF
contributing zero time with known diagnosis (Figure 1). The timeframe for such an
assessment of long-term efficacy ought to represent a proposed time interval between
screening events if translated into clinical practice - for example 5 years. Hence, the ideal
primary outcome for this study would be the amount of time spent with a known diagnosis
of AF for each participant during a period of 5 years from randomisation onwards (i.e. the
actionable time period). For example, if AF was diagnosed approximately 1 year after
randomisation, then the time period spent with a known diagnosis of AF from
randomisation up to 5 years is 4 years.




AMALFI Statistical Analysis Plan v1.2 2025_06_26                                            7
        Figure 1 - Estimated cumulative percent of participants diagnosed with AF




Figure legend - Each curve represents the cumulative proportion of new AF diagnoses in the
active arm (small triangles) and control arm (small squares). The primary outcome is the
proportion of people with AF recorded within primary care records within 2.5 years after
randomisation in each arm (large solid triangle and square). The difference between both is
represented by the double-headed arrow. The secondary outcome is the mean time spent
with an AF diagnosis over a period of 5 years after randomisation (from the date of first
post-randomisation AF record until right-censoring at 5 years after randomisation, or
death/withdrawal if earlier); this is represented by the area-under-the-curve for each curve
(active arm and control arm). The difference between both is the dashed area between the
curves.
However, a more easily interpretable and timely assessment of the expected value of the
proposed screening approach can be performed by assessing the proportion with AF
detected in each arm within a period of 2.5 years from randomisation – which, based on
the statistical modelling performed of the expected AF rates during follow-up, is the
largest driver of the expected mean time spent with a known diagnosis of AF within a
period of 5 years from randomisation. Further details can be found in the study protocol.

Therefore, the primary outcome assessment will involve an intention-to-treat comparison
among all randomised participants allocated to screening versus usual care on the
presence of a record of AF (as recorded in primary care data) occurring between
randomisation and 2.5 years after randomisation (i.e. at around the midpoint of a
proposed 5-year screening interval).

3.6.2      Secondary outcome assessments
The secondary outcome assessments for the study will involve intention-to-treat
comparisons among all randomised participants allocated to screening versus usual care
on:




AMALFI Statistical Analysis Plan v1.2 2025_06_26                                         8
        the presence of a post-randomisation record of AF within a period of 2.5 years from
         randomisation (as in the primary outcome assessment) by subgroups of age (<80
         and ≥80 years) and, separately, sex
        time spent with a known AF diagnosis within a period of 5 years from
         randomisation (as described in the previous section), in the overall cohort and in
         the same subgroups mentioned above.

The secondary outcomes described will be assessed regardless of the results of the
primary outcome.

3.6.3      Exploratory outcomes
A number of exploratory outcomes will also be assessed to complement the information
provided by the primary and secondary outcomes. These are listed in detail in Section 6.4.

3.6.4      Outcome derivation
The detailed derivation of outcomes included in statistical analyses will be described in a
separate document.

         Hypothesis framework
For each of the primary and secondary outcomes, the null hypothesis will be that there is
no true difference in effect between the two study arms.

         Randomisation
Eligible patients were randomised in a 1:1 ratio to be sent an ECG monitoring patch (Zio
XT) to be self-applied and worn for a single 2-week period, versus usual care (i.e. not being
sent a patch), by the central computer in CTSU, using a minimisation algorithm to ensure
balance by important baseline variables (age [<75, ≥75 years], sex, and residual
CHA2DS2VASc score excluding age and sex [residual score 0-1, 2, 3-6]).2

         Blinding
This is an open-label study. As such, participants, their GPs, and the trial team are aware
of study arm allocation. However, while the study is in progress, access to tabular results
of study outcomes by randomised allocation will not be available to the research team, the
chief investigators, trial statisticians, or GPs. Patch monitoring data may be interrogated
to ascertain the rate of new AF diagnoses found via patch as the trial progresses.
However, neither patch data nor records of study arm allocation will be combined with
clinical data from other sources in a way that could potentially lead to unblinding prior to
preparation and production of the main trial analyses.

           Data collection schedule
3.10.1     Self-reported medical history
Upon inclusion in the trial, each participant was required to complete and return by post a
questionnaire which asked about relevant parts of their medical history to establish



AMALFI Statistical Analysis Plan v1.2 2025_06_26                                           9
eligibility. These included the components of the CHA2DS2-VASc score, and a question
about previous allergies to latex (the latter used as a screening assessment to identify
patients who might not be eligible for the trial). Self-reported information on the
components of the CHA2DS2-VASc score was used to inform the minimisation
randomisation algorithm and will be used in descriptive analyses.

3.10.2     Primary care data
Extracts from electronic primary care records will be performed via each of the
participating GP practices at three time points (counted from the date of randomisation of
the last participant randomised at each practice):

        at least 1 year after randomisation (to establish data extraction feasibility and
         allow collection of preliminary data);
        at least 2.5 years after randomisation (to support analysis of the outcomes
         specified at 2.5 years after randomisation); and
        at least 5 years after randomisation (for analysis of the outcomes specified at 5
         years after randomisation).

Data extracted from primary care records will include information on ethnicity, body mass
index, medical diagnoses, symptoms, medication prescriptions, referrals to secondary
care, procedures and diagnostic tests, and appointments/contacts with practice staff (for
clinical or administrative reasons).

3.10.3     Healthcare systems data
Healthcare systems data (in addition to primary care records) will be requested from
medical databases including those held by NHS England and equivalent bodies. This will
include the following datasets as specified in the table below.


 Dataset                    Event type             Reference


 Medicines dispensed Medication dispensing         https://digital.nhs.uk/data-and-
 in Primary Care NHS in the community              information/data-tools-and-
 Business    Services                              services/data-services/medicines-
 Authority       data                              dispensed-in-primary-care-nhsbsa-
 product (Dispensing                               data
 dataset)


 Civil Registrations of Death registrations        https://digital.nhs.uk/services/data-
 Death                                             access-request-service-dars/dars-
                                                   products-and-services/data-set-
                                                   catalogue/civil-registrations-of-death




AMALFI Statistical Analysis Plan v1.2 2025_06_26                                        10
 Emergency      Care A&E       department https://digital.nhs.uk/data-and-
 Dataset (ECDS)      attendance           information/data-collections-and-
                                          data-sets/data-sets/emergency-care-
                                          data-set-ecds


 Hospital      Episode Outpatient                       https://digital.nhs.uk/services/hospital-
 Statistics Outpatients appointments                 in episode-statistics
 (HESOP)                secondary care




 Hospital    Episode Hospitalisations
 Statistics Admitted
 Patient        Care
 (HESAPC)


 Hospital    Episode Critical                      care
 Statistics   Critical admissions
 Care (HESCC)



These data will be used to complement primary care data to identify relevant baseline
characteristics, characterise medication and healthcare use, and to collect other
information of interest which is expected not be captured adequately in primary care data
(such as deaths and need for hospitalisation, for example due to a bleed).

The datasets specified will be requested from NHS England or other institutions on an
annual basis, starting from 2022 and at least until the end of 2027 (i.e. during the
scheduled study period for the assessment of the primary and secondary outcomes). Data
may continue to be requested for up to 25 years from randomisation for all surviving
participants (unless they have withdrawn consent).

Further information on use of linked data, namely specific derivation procedures and which
data points each dataset will contribute to, will be specified in a separate document.

3.10.4     Health-related quality of life data
Health-related quality of life data will be collected using self-reported EQ-5D-5L
questionnaires. These will be mailed to the entire cohort simultaneously, at two time
points: 1) once recruitment to the trial is complete, and 2) after the results of the primary
outcome are published. Further details on the use of these data will be specified in a
separate health-economics analysis plan.

3.10.5     End of study
The main trial period is scheduled up until 5 years from randomisation. The end of study is
defined as the date of the last electronic data download at 5 years after randomisation


AMALFI Statistical Analysis Plan v1.2 2025_06_26                                               11
(from either central registries, including NHS England or others, or from a participating GP
practice). However, it is intended that data may continue to be requested from NHS
England (for up to 25 years after randomisation) in order to undertake longer-term
exploratory assessments of the clinical impact of allocation to screening.

           Data monitoring
The trial does not have a formal data monitoring committee, and no interim data
monitoring assessments are planned (to investigate either safety or efficacy).

Specific procedures for storing and handling data collected as part of the trial will be
described in a separate data management document.

           Trial reporting
The trial will be reported according to the principles of the CONSORT statement.3 It is
anticipated that the study will produce one publication describing the study rationale,
design, and baseline characteristics of recruited participants, one publication focused on
analyses of the primary and secondary outcomes at 2.5 years after randomisation, and a
subsequent publication with results from the secondary outcomes assessed at 5 years
after randomisation. However, further publications may be produced.


4          Analysis populations
        Population definitions
Unless otherwise specified, all comparative analyses between study arms will use the
intention-to-treat principle – i.e. including all randomised participants, regardless of
whether they subsequently adhered to the randomised allocation.

        Length of follow-up
4.2.1      Primary care records
Length of follow-up in the primary care records will be calculated as time from
randomisation to the earliest of:

       death;
       withdrawal of consent (complete withdrawal of consent, or withdrawal of
        permission for GP to share information about important illnesses);
       loss to follow-up in primary care records, defined for each participant as the date
        of a known change of GP practice to a practice not taking part in AMALFI (identified
        from either direct reporting to the study team, or GP practice codes assigned to
        dispensing records in the nationwide dispensing dataset); or
       study day 913 or study day 1826 (where day of randomisation is study day 0) –
        i.e. after 2.5 or 5 years have elapsed – according to the timeframe specified for
        assessment of each outcome.




AMALFI Statistical Analysis Plan v1.2 2025_06_26                                         12
4.2.2      National datasets
Length of follow-up in the national datasets (section 3.10.3) will be calculated as time from
randomisation to the earliest of:

       death;
       withdrawal of consent (complete withdrawal of consent, or withdrawal of
        permission for NHS England) to share information about important illnesses);
       study day 913 or study day 1826 (where day of randomisation is study day 0) –
        i.e. after 2.5 or 5 years have elapsed.

        Censoring
4.3.1      Left-censoring (pre-randomisation records)
4.3.1.1 Primary and secondary outcomes
In the event that AF diagnoses occurring pre-randomisation are identified, such diagnoses
will not count towards the primary or secondary outcomes, but their numbers will be
reported. For the avoidance of doubt, individuals for whom a pre-randomisation AF
diagnosis is identified will be included in the intention-to-treat analysis, in the study arm
they were allocated to. These individuals, who had AF first recorded before randomisation,
will only be counted as having an AF endpoint event if they also have a subsequent record
of AF post-randomisation. Pre-randomisation records will be discarded as it is considered
that at least some of these could have been wrongly entered into the primary care records
or entered retrospectively, otherwise these patients would not have been identified as
potentially eligible following the electronic eligibility search performed.

4.3.1.2 Outcomes of oral anticoagulation exposure
As the nationwide dataset on medication dispensing only provides the calendar month
and year in which a dispensing record occurred, with no exact dates, it is not possible to
discern whether anticoagulation during the month of randomisation is prior to or post
randomisation. Therefore, for any outcomes assessing post-randomisation exposure to
oral anticoagulation, only records occurring in the months after the month of
randomisation will contribute. Records of medication use prior to or during the month of
randomisation will be counted as medication prior to randomisation.

4.3.2      Right-censoring (post-randomisation records)
4.3.2.1 Primary outcome and subgroup analyses of the primary outcome
No censoring will be applied when assessing the primary outcome (the presence of a
record of AF, as recorded in primary care data, occurring between randomisation and 2.5
years after randomisation) or subgroup analyses of the primary outcome. Further details
on the planned hypothesis testing approach for these outcomes are included in Section
6.1.




AMALFI Statistical Analysis Plan v1.2 2025_06_26                                          13
4.3.2.2 Secondary outcomes of time spent with AF diagnosis at 5 years
For the secondary outcome of time spent with a known AF diagnosis within a period of 5
years after randomisation, and its corresponding subgroup analyses, right-censoring will
be applied at the earliest of death, study withdrawal, or on study day 1826.

For the avoidance of doubt, while information on fact and timing AF diagnoses will only
be captured from primary care records, the analysis of time spent with (i.e. after) a known
AF diagnosis spans from the date of diagnosis to date of death. Therefore, while the length
of follow-up is defined by the length of primary care data collection, the relevant right-
censoring time point is the earliest of date of death, withdrawal, or on study day 1826.

Additionally, a data imputation procedure will be specified at a later stage to handle loss
to follow-up in primary care records in participants without a known diagnosis of AF by
the time of loss to follow-up.

4.3.2.3 Outcomes of oral anticoagulation exposure
For any outcomes assessing exposure to oral anticoagulation, right-censoring will be
applied at the earliest of calendar month of death, withdrawal, or the 30th calendar month
(for 2.5 year analyses) or 60th calendar month (for 5 year analyses) post-randomisation.




5          Descriptive analyses
        Participant throughput
The flow of participants through the trial will be summarised using a CONSORT diagram.
The flow diagram will describe the numbers of participants invited, randomly allocated,
adherence to patch, withdrawals of consent, and losses to follow-up (e.g. moved GP,
death during follow-up).

           Baseline characteristics of randomised arms
The following characteristics, derived from self-reported medical history on the
randomisation form and the electronic records, will be described separately for
participants in each arm, at randomisation:

       Age (mean age, and grouped by <75, 75 to 79 and ≥80 years at randomisation)
       Sex
       Ethnicity (split into White, Black, Asian, Mixed/Other, and missing)
       Body mass index (mean and grouped by <25, 25 to <30, ≥30 kg/m2, and missing)
       CHA2DS2VASc score (median and grouped as score 3, 4, or 5 or more)
       CHA2DS2VASc components
       Chronic kidney disease (stage 3 or higher vs no CKD)
       Use of oral anticoagulation (prior to or in the month of randomisation)
       Use of other relevant treatments (prior to or in the month of randomisation):
           o Statins



AMALFI Statistical Analysis Plan v1.2 2025_06_26                                        14
            o   Aspirin or dipyridamole
            o   P2Y12 inhibition
            o   RAAS inhibition
            o   Beta-blockers
            o   Diuretics
            o   Calcium-channel blockers (diltiazem, verapamil, dihydropyridines)
            o   Insulin
            o   Proton-pump inhibitors or H2-antagonists

The number and percentage will be presented for binary and categorical variables. The
mean and standard deviation or the median and the interquartile range will be presented
for continuous variables, as appropriate. Counts of participants with missing data for each
parameter will also be presented, with missing data defined as unavailability in the linked
healthcare systems data required to ascertain each parameter (e.g. primary care data for
body mass index; medication dispensing data for medications; both primary data and HES
data for ethnicity). A shell table is provided below:




AMALFI Statistical Analysis Plan v1.2 2025_06_26                                        15
                                                                           Study allocation
                                                        Overall,       Patch,          Control,
Characteristic
                                                       N = 5,040      N = 2,520       N = 2,520
Age, mean (SD)
 - <75
 - 75-79
 - ≥80
Female sex
Ethnicity
 - White
 - Black
 - Asian
 - Mixed/Other
 - Missing
Body mass index (BMI), mean (SD)
 - <25 kg/m2
 - 25 to <30 kg/m2
 - ≥30 kg/m2
 - Missing
CHA2DS2VAsc score, median (IQR)
 - 3
 - 4
 - ≥5
Heart failure
Hypertension
Diabetes
Stroke or TIA
Thromboembolism
Myocardial infarction
Peripheral arterial disease
Chronic kidney disease (stage ≥3)
Medication exposure prior to randomisation
 - Oral anticoagulation
 - Statin
 - Aspirin or dipyridamole
 - P2Y12 inhibition
 - RAAS inhibition
 - Beta-blockers
 - Diuretics
 - Calcium-channel blockers
 - Insulin
 - Proton-pump inhibitors or H2-antagonists
    Number of participants with no available primary care data: n= XX
    Number of participants with no available nationwide dispensing data: n=XX


            Completeness and length of follow-up
    All reasonable efforts will be taken to minimise loss to follow-up. While data collection is
    entirely electronic, efforts undertaken to minimise loss to follow-up (in primary care


    AMALFI Statistical Analysis Plan v1.2 2025_06_26                                         16
records) include close communication with GP practices to ensure data are extracted and
transferred in a timely manner, troubleshooting issues with data extraction and transfers,
and cross-checking numbers of participants with data received from each practice with
those expected based on recruitment records (and investigating and correcting any
discrepancies). Losses to follow-up are therefore expected to be few given the use of
remote data collection procedures and a combination of data from local primary care
records and a wealth of nationwide datasets.

The number and percentage of participants with follow-up information to day 913 (2.5
years) and day 1,826 (5 years) will be reported for each relevant comparison, as well as
the average length of follow-up time available (as further described in Section 4.2). These
will be reported separately for primary care data (to be used for the primary and secondary
outcomes) and nationwide dispensing data (to be used for exploratory outcomes of oral
anticoagulation exposure).

        Adherence to the study intervention
The number and proportions of participants allocated to the active (screening) arm who
wore a patch and for whom any length of patch monitoring data is available will be
reported, and taken to represent overall adherence to the study intervention. The median
time spent wearing a patch and the median proportion of patch data suitable for analysis
will also be reported, as well as the median time between randomisation and the date the
patch was activated (for those who wore it). Additionally, baseline characteristics of
participants in the active arm will be reported separately for those who wore vs those who
did not wear a patch. Reasons for non-adherence to patch will also be reported.

        Cardiac monitoring findings in the active arm
Heart rhythm findings detected by the ECG patch will be reported for participants in the
active arm of the study who wore a patch. These will include:

       Rate of new AF detection via patch during the monitoring period (number and
        proportion)
       Characteristics of AF detected via patch
           o Burden (i.e. proportion of time spent in AF during the monitoring period)
           o Longest AF episode duration (in hours)
           o Maximum heart rate during AF episodes
           o Minimum heart rate during AF episodes
           o Time to first AF episode during the monitoring period (in days)
       Frequency of other arrhythmias found through monitoring (e.g. atrial flutter,
        supraventricular tachycardias, non-sustained and sustained ventricular
        tachycardias, atrioventricular block of different degrees)

Additionally, for participants with AF detected via patch, the time between patch reporting
date and the date of the first AF record in primary care records will also be reported.




AMALFI Statistical Analysis Plan v1.2 2025_06_26                                        17
6          Comparative analyses
        Primary outcome
The chi-square test will be used to compare the proportion of participants with a record
of AF in primary care data within a period of 2.5 years after randomisation in all those
randomised to screening versus all those randomised to usual care. Proportions in each
arm will be presented, along with the ratio of proportions and the associated 95%
confidence interval.

Individuals who had AF recorded before randomisation will only be counted as having an
AF endpoint event if they also have a subsequent record of AF post-randomisation.
Individuals with no record of AF during this time frame who died, were withdrawn, or lost
to follow-up from the primary care records before 2.5 years from randomisation will be
counted as having no record of AF.

        Secondary outcomes
The chi-square test will be used to compare the proportion of participants with AF
recorded within a period of 2.5 years after randomisation in those randomised to screening
versus those randomised to usual care, separately by age subgroups of <80 and ≥80 years
and, separately, by sex subgroups at randomisation, with a test for heterogeneity of the
results between the two subgroups.

As the characteristics of the distributions of mean time spent with a known AF diagnosis
cannot be predicted beforehand, choice of a parametric statistical hypothesis test a priori
could be inappropriate. Therefore, a permutation test4 will be used to compare the mean
duration of time with AF diagnosed at 5 years after randomisation in all those randomised
to screening compared to all those randomised to usual care (in the overall cohort and,
separately, by age and by sex subgroups, as above). Duration of time with AF diagnosed
will be defined as days from date of the first post-randomisation AF record in the primary
care data to 5 years after randomisation (or date of death or withdrawal if this is earlier).
Those with no diagnosis of AF by the end of the study will contribute zero time with AF.
Details on a procedure to handle participants who withdrew or were lost to follow-up with
no record of AF before 5 years will be specified at a later stage (but before any unblinded
data analyses are undertaken). The empirical p value for the difference will be calculated
as (1+s)/(n+1) where s = the number of simulations where the difference in mean time with
a known AF diagnosis is at least the observed difference and n=total number of
simulations.

        Sensitivity analyses
Sensitivity analyses of the primary and secondary outcomes will be performed using AF
diagnoses captured in either primary care records or secondary care records (i.e. from
Hospital Episode Statistics datasets) – i.e. an AF diagnosis will be counted regardless of
where it was recorded in primary care or secondary care records.




AMALFI Statistical Analysis Plan v1.2 2025_06_26                                          18
        Exploratory outcomes
6.4.1  Time to AF detection within a period of 2.5 and 5 years after
randomisation
Cumulative incidence curves for AF detection up to 2.5 years and 5 years after
randomisation will also be presented, and the difference between randomised arms will
be assessed as an exploratory outcome. Time to AF detection will be defined as the time
from randomisation to first post randomisation primary care record of AF, censoring at the
earliest of date of death, withdrawal, loss to follow-up in the primary care records, or day
913 (2.5-year analysis) / day 1826 (5-year analysis). Statistical hypothesis testing will be
performed using the log-rank test. The median time to first AF record after randomisation
in primary records (i.e. from randomisation to first post-randomisation record) will also be
presented for each arm for people who have a diagnosis of AF.

6.4.2    Time spent with a known diagnosis of AF within a period of 2.5 years
after randomisation
The outcome of time spent with a known diagnosis of AF within a period of 2.5 years after
randomisation (i.e. replicating the secondary outcome of time spent with a known
diagnosis of AF within a period of 5 years after randomisation, but within a shorter period)
will be assessed as an exploratory outcome alongside analyses of the primary outcome
(proportion of participants with a post-randomisation record of AF at 2.5 years after
randomisation). The hypothesis testing framework and procedures for this exploratory
outcome will follow those outlined for the secondary outcome of time spent with a known
diagnosis of AF within a period of 5 years after randomisation (as specified in section 6.2).

6.4.3      Rates of oral anticoagulation use
To explore the impact of AF screening on post-randomisation oral anticoagulation use
(including direct oral anticoagulants and vitamin K antagonists, but excluding rivaroxaban
2.5mg twice daily1), the following exploratory outcomes will be assessed:

    1. Total number of participants with a post-randomisation record (presented using
       counts and proportions in each randomised arm, and tested using a chi-square
       test). Median time to first post-randomisation record (in calendar months) will also
       be presented for people with oral anticoagulation recorded, separately for each
       randomised arm.
    2. Total quantitative post-randomisation exposure, defined as total number of distinct
       calendar months with evidence of likely exposure to oral anticoagulation, as further
       described in a separate document (presented using means in each randomised
       arm, and tested using a permutation test).

All outcomes will be calculated in both study arms, up to 30 and 60 months after
randomisation (or month of death or withdrawal if earlier). These assessments will be

1
  Rivaroxaban 2.5mg BD is the dose used for cardiovascular risk reduction alongside
antiplatelet therapy in people with established cardiovascular disease, and not for clinical
anticoagulation purposes, hence excluded here


AMALFI Statistical Analysis Plan v1.2 2025_06_26                                          19
performed regardless of whether AF was recorded during the follow-up period (as any
impact of screening on clinical outcomes would depend on an increase in overall
anticoagulation exposure, not just anticoagulation for AF).

Cumulative incidence curves for months to first post-randomisation oral anticoagulant
record up to 30 and 60 months after randomisation will also be presented. These analyses
will also be censored at the month of death or withdrawal. Statistical hypothesis testing
will be performed using the log-rank test.

6.4.4      Long-term assessments of the clinical impact of screening
Although the trial is not powered to show a statistically significant difference in clinical
outcomes between study arms, numbers and proportions of the following events in each
arm will be reported in future analyses focused on long-term impacts of screening (with
no hypothesis testing performed):

       Hospitalisations (total and for cardiovascular causes)
       Ischaemic stroke
       Major bleeding
       All-cause and cardiovascular death

Details on the nature of such analyses and associated outcome identification will be
specified at a later stage.

        Non-randomised comparisons
6.5.1   Rates of oral anticoagulation between screen-detected and clinically-
detected AF (non-randomised assessment)
In order to explore the potential impact of AF detection modality (screen vs clinically-
detected) on clinical management, an exploratory, retrospective, non-randomised
comparison of rates of post-randomisation oral anticoagulation use will be performed
among the following non-randomised groups:

    1. AF detected on patch + AF recorded in post-randomisation primary care records
    2. AF recorded in post-randomisation primary care records only (amongst those
       randomised to either treatment arm)
    3. AF detected on patch + no post-randomisation primary care record of AF

Anticoagulation use will be defined as:

    -   For participants with AF detected in primary care records (groups 1 and 2):
        presence of an anticoagulation record after the month of the first post-
        randomisation AF primary care record;
    -   For participants with AF detected on patch but not on primary care records (group
        3): presence of an anticoagulation record after the month of reporting of an AF
        diagnosis to the GP.




AMALFI Statistical Analysis Plan v1.2 2025_06_26                                         20
For participants with AF detected on patch and AF recorded in post-randomisation
primary care records (group 1), the time interval between AF diagnosis reporting to the GP
and date of first post-randomisation AF record in primary care data will also be reported.
The date of AF diagnosis reporting to the GP will be considered as the date on which the
cardiac monitoring report was emailed directly to the GP by the study team, not the (later)
date on which the automated results letter was mailed to both the participant and their
GP (as described in Section 3.5).

        Non-pre-specified exploratory analyses
Additional analyses not specified in this statistical analysis plan may be performed if
deemed to be of scientific interest. These will be clearly identified as exploratory and non-
pre-specified, and due allowance will be made in their interpretation.

        Health economics
In addition to investigating the impact of screening on AF detection rates, the results from
AMALFI will also inform a broader cost-effectiveness analysis aimed at capturing
differences in healthcare resources (e.g. GP visits, medications, hospital visits), as well as
differences in health-related quality of life (based on the standard EQ-5D-5L
questionnaire), AF cases, and AF-related events in combination with data from external
cohorts. Details of these analyses will be described in a separate analysis plan.

        Power calculations
6.8.1      Power calculations for the primary outcome
The sample size for this study was initially specified as 2,500 but was later increased to
5,000. The underlying assumptions are as follows:

AF detection via usual care: A 2015 UK study on opportunistic AF screening during flu
vaccinations suggests the yearly rate of asymptomatic AF detection through usual care is
~0.7% among those who receive a pulse check (with approximately half those who had a
flu vaccination receiving a pulse check).5 Thus, if considering the entire population aged 65
years or more (of whom only some will have pulse checks), the rate of newly-detected AF
is expected to be half, at ~0.3-0.4%/year. As AMALFI participants will generally have a
higher cardiovascular risk than the general population, the yearly AF detection rate was
estimated to be ~0.7%/year. Over a 2.5 year period, the new AF detection rate via usual
care is expected to be 1.75% (0.7% x 2.5 years), based on a time dependent Poisson
process (a+bt) with a parameter b slightly increasing with time.

AF detection via screening: In STROKESTOP, screening with twice-daily, 30 second ECG
over 14 days in 75 year-olds detected new AF in 3.0%.6 It is expected that continuous
monitoring with the Zio XT during a similar period of time in AMALFI will result in higher
AF detection rates. However, patch screening will not detect all AF cases in the active arm,
due to non-compliance with the patch, false negatives, or AF episodes not occurring at the
time of screening; thus, additional AF cases will continue to be detected through usual care
in this arm. Taking into consideration a moderate level of non-adherence and false-
negatives (i.e. AF missed during the monitoring period by chance), it was estimated that


AMALFI Statistical Analysis Plan v1.2 2025_06_26                                           21
screening would lead to newly-detected AF in about 3.75% of individuals, with additional
new AF cases found via usual care throughout the duration of study. Over a 2.5-year
period, it is estimated that the total new AF detection rate in the active arm will be 4.4%.
This estimate takes the same Poisson process used in the usual care arm (with expected
annual AF incidence 0.7%) and assumes that 70% of AFs that would have been detected
in year 1 were found by patch, 60% year 2, and 50% year 3.

Sample size calculations: Based on these assumptions, an initial sample size of 2,500
individuals (1,250 in each arm) was set to provide >90% power to detect the expected
difference in proportions of newly-detected AF between arms at 2.5 years (1.75% versus
4.4%; ratio: approximately 2.5) at two-sided p (2p) <0.05.

Modifications to the sample size: AMALFI completed recruitment of the initial sample size
of 2,500 in mid-2021, without exhausting the available pool of interested GP practices or
the funding available for recruitment activities. Based on an interim analysis of baseline
characteristics and Zio XT AF detection rates in 1,250 randomised participants (but
blinded to total AF detection rates in both arms), the investigators decided to extend the
target study size to 5,000. This extension allowed:

1. Improved precision to detect the estimated 2.5-fold difference in AF proportions
between the two arms at 2.5 years (>90% power at 2p<0.01 vs 0.05);

2. Preserved power if the difference between arms were smaller than expected (i.e. >90%
power at 2p<0.01 for a 2-fold difference) – e.g. due to high AF detection rates through
usual care in the control arm;

3. Good power to analyse the primary outcome by subgroups for age (<80 and ≥80 years)
and, separately, sex at randomisation, with ~90% power at 2p<0.05 in both assessments;

4. Improved power to detect differences in health-related quality of life (health economics
analyses).

        Adjustment for baseline characteristics
No adjustment of the primary or secondary outcomes based on baseline characteristics is
planned a priori. Adjustments may be performed if significant imbalances between arms
(for the overall cohort or any of the pre-specified subgroup analyses) are later found.
However, it is expected that the minimisation randomisation algorithm employed (based
on age, sex, and self-reported residual CHA2DS2VASc score) will prevent or at least reduce
the possibility of such imbalances.

           Significance levels and adjustment of p-values for multiplicity
The statistical significance level will be set as a two-sided alpha<0.05. Formal statistical
adjustment for multiple hypothesis testing will not be made for the primary, secondary and
exploratory outcomes (including subgroup analyses). However, due allowance for multiple
testing will be made in the interpretation of the secondary and exploratory results: the
larger the number of events on which a comparison is based, and the more extreme the



AMALFI Statistical Analysis Plan v1.2 2025_06_26                                         22

```

### DOC-003 physical PDF page 23 — PLAN, fresh layout

```text
P-value after any allowance has been made for the nature of the particular comparison
(i.e. primary or secondary; pre-specified or exploratory), the more reliable the comparison
and, hence, the more definite any finding will be considered. 95% confidence intervals will
be presented for comparisons of the primary and secondary outcomes.

7      Statistical software

SAS version 9.4 and/or R version 4.2.2 in RStudio version 2024.12.1. Build 563 (or later)
for Windows will be used for all statistical analyses and plotting.

8     References

1.     Hindricks G, Potpara T, Dagres N, et al. 2020 ESC Guidelines for the diagnosis and
management of atrial fibrillation developed in collaboration with the European Association
for Cardio-Thoracic Surgery (EACTS). European Heart Journal 2021;42:373-498. doi:
10.1093/eurheartj/ehaa612
2.    Pocock  SJ, Simon  R. Sequential treatment assignment with balancing  for
prognostic factors in the controlled clinical trial. Biometrics 1975;31:103-115. doi:
3.     Schulz KF, Altman DG, Moher D. CONSORT 2010 Statement: updated guidelines
for reporting parallel group randomised trials. BMC Medicine 2010;8. doi: 10.1186/1741-
7015-8-18
4.     Lachin JM. Statistical properties of randomization in clinical  trials. Controlled
Clinical Trials 1988;9:289-311. doi: 10.1016/0197-2456(88)90045-1
5.    Arathoon N. Opportunistic Screening for Atrial Fibrillation for over 65 Year Olds
during Flu Clinics and Anticoagulation for the Prevention of Stroke in Primary Care.  .
https://aftoolkit.co.uk/wp-content/uploads/2020/04/dorset-ccg.pdf
6.    Svennberg E, Friberg L, Frykman V, et al. Clinical outcomes in systematic screening
for atrial fibrillation (STROKESTOP): a multicentre, parallel group, unmasked, randomised
controlled trial. The Lancet 2021;398:1498-1506. doi: 10.1016/s0140-6736(21)01637-8





AMALFI Statistical Analysis Plan v1.2 2025_06_26                                           23
```

### DOC-003 physical PDF page 24 — PLAN, fresh layout

```text
9    Appendices
     Appendix I: CHA2DS2-VASc Scoring system

 Item  Condition                                                                  Points

  C    Congestive heart failure (or Left ventricular systolic dysfunction)                1

        Hypertension: blood pressure consistently above 140/90 mmHg (or treated       1  H
        hypertension on medication)

  A2   Age ≥75 years                                                     2

  D    Diabetes Mellitus                                                   1

   S2    Prior Stroke or TIA or thromboembolism                                  2

        Vascular disease (e.g. peripheral artery disease, myocardial infarction, aortic      1
  V        plaque)

  A   Age 65–74 years                                                   1

  Sc   Sex category (i.e. female sex)                                          1





AMALFI Statistical Analysis Plan v1.2 2025_06_26                                           24
```

### DOC-004 physical PDF page 1 — REPORT

```text
Source PDF: joi250068supp3_prod_1760999665.30362.pdf
Source PDF page: 1
Extraction method: native PDF text

Supplemental Online Content
Wijesurendra R, Pessoa-Amorim G, Buck G, et al. Remote screening for
asymptomatic atrial fibrillation: the AMALFI randomized clinical trial. JAMA.
Published online August 29, 2025. doi:10.1001/jama.2025.15440

eMethods
eTable 1. Patch usage metrics
eTable 2. Baseline characteristics by patch ECG data availability
eTable 3. Patch-detected conditions
eFigure 1. Proportions, absolute differences and ratios of proportions of
participants with a primary care or secondary care record of atrial fibrillation (AF)
between randomization and 2.5 years by randomized  allocation overall and in age
and sex subgroups
eFigure 2. Patch-detected atrial fibrillation metrics
eFigure 3. Kaplan-Meier plot of time from urgent patch report to first primary
care record of atrial fibrillation (AF), restricted to those with  patch-detected AF
eFigure 4. Patch-detected atrial fibrillation and/or flutter (AF/AFL) metrics
This supplemental material has been provided by the authors to give readers
additional information about their work.
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.

```

### DOC-004 physical PDF page 2 — REPORT

```text
eMethods

Patch monitor

The Zio XT patch is a single lead (modified lead II ECG) applied to the chest that records up to 14 days of continuous
ECG data which has been Food and Drug Administration (FDA) cleared and UK Conformity Assessed (UKCA)
approved. Previous studies have shown higher diagnostic yield and lower retesting rates with Zio XT compared to
shorter duration, intermittent monitoring, and other long-term continuous monitoring devices.1-3 Home-based
application and activation of the Zio XT has been previously used in clinical trials and in clinical practice and has
been shown to have comparable wear time and analyzable time compared to in-clinic application4.

After the 14-day period (or before, if the patch fell off or was removed), participants were asked to mail the patch
back to the manufacturer using a pre-paid return mailer. A reminder letter was sent to those who had not returned
their patch after several weeks.

The recorded ECG data were analyzed by iRhythm using a validated proprietary deep-learning algorithm that is
capable of detecting 13 arrhythmias (including atrial fibrillation [AF]), plus sinus rhythm and noise. The algorithm
has previously shown high diagnostic performance when compared with a committee of certified cardiologists.5 AF
was defined as the presence of at least 30s of continuous AF-compatible tracing during monitoring. ECG findings
were reviewed and classified by qualified cardiovascular technicians at iRhythm,1 and a technician report of
preliminary findings was provided to the study team using a secure web-based system. No manual classification or
over-read were performed by the study team. Automated alert systems were in place for AF and other arrhythmias
considered by the study team to be clinically actionable (i.e., atrial flutter; sustained ventricular tachycardia or
fibrillation; pauses lasting over 6s; complete heart block, Mobitz type II, or high-grade atrioventricular block), which
were communicated to general practitioners (GPs) immediately by secure email. Separately, the study team
received regular structured data extracts from iRhythm including all ECG findings, which were used to automatically
generate results letters that were sent to GPs, with copies to participants. The letters detailed the presence or
absence of AF, along with duration, heart rate, and burden. GPs managed any findings at their discretion as part of
clinical care; no guidance on the management of AF or other arrhythmias was provided by AMALFI, besides
referencing relevant guidelines.6,7





   © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 physical PDF page 3 — REPORT

```text
eMethods References

1.      Turakhia MP, Hoang DD, Zimetbaum P, et al. Diagnostic Utility of a Novel Leadless Arrhythmia Monitoring
Device. The American Journal of Cardiology. 2013;112(4):520-524. doi:10.1016/j.amjcard.2013.04.017
2.     Reynolds MR, Passman R, Swindle J, et al. Comparative effectiveness and healthcare utilization for
ambulatory cardiac monitoring strategies in Medicare beneficiaries. American Heart Journal. 2024;269:25-34.
doi:10.1016/j.ahj.2023.12.002
3.      Barrett PM, Komatireddy R, Haaser S, et al. Comparison of 24-hour Holter Monitoring with 14-day Novel
Adhesive Patch Electrocardiographic Monitoring. The American Journal of Medicine. 2014;127(1):95.e11-95.e17.
doi:10.1016/j.amjmed.2013.10.003
4.     Goergen JA, Peigh G, Hsu M, et al. Comparison of data quality and monitoring completion rates between
clinic and self-applied ECG patches. Heart Rhythm. 2023;20(3):407-413. doi:10.1016/j.hrthm.2022.11.020
5.     Hannun AY, Rajpurkar P, Haghpanahi M, et al. Cardiologist-level arrhythmia detection and classification in
ambulatory electrocardiograms using a deep neural network. Nature Medicine. 2019;25(1):65-69.
doi:10.1038/s41591-018-0268-3
6.     NICE Guideline - Atrial fibrillation: diagnosis and management. https://www.nice.org.uk/guidance/ng196
(National Institute for Health and Care Excellence.) (2021).
7.     Van Gelder IC, Rienstra M, Bunting KV, et al. 2024 ESC Guidelines for the management of atrial fibrillation
developed in collaboration with the European Association for Cardio-Thoracic Surgery (EACTS). European Heart
Journal. 2024;45(36):3314-3414. doi:10.1093/eurheartj/ehae176





   © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 physical PDF page 4 — REPORT

```text
Source PDF: joi250068supp3_prod_1760999665.30362.pdf
Source PDF page: 4
Extraction method: native PDF text

eTable 1. Patch usage metrics
Randomized to patch
(N = 2520)
Wore and returned patch - n (%)
2126 (84.4%)
Days from randomization to patch activation - Median (IQR)
10 (6 - 18)
Days wore patch - Median (IQR)
13.9 (13.2 - 14.0)
Days patch data analyzable - Median (IQR)
13.5 (12.6 - 13.9)
Percentage of patch data suitable for analysis - Median (IQR)
98.8 (95.8 - 99.6)
Patch worn ≥10.5 days (75% recommended time) - n (%)
1960 (77.8%)
Patch worn but <10.5 days - n (%)
166 (6.6%)
Reasons patch removed - n (%)*
Patch attachment problems
43 (25.9%)
Skin reaction
18 (10.8%)
Other
8 (4.8%)
Unknown
97 (58.4%)
Patch returned unworn - n (%)
188 (7.5%)
Patch not returned - n (%)
206 (8.2%)
IQR=Interquartile range, SD=Standard deviation. * Percent of the 166 who wore the patch <10·5 days
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.

```

### DOC-004 physical PDF page 5 — REPORT

```text
Source PDF: joi250068supp3_prod_1760999665.30362.pdf
Source PDF page: 5
Extraction method: native PDF text

eTable 2. Baseline characteristics by patch ECG data availability
Overall in
Patch group
N = 2520
Patch ECG
data
N = 2126
(84.4%)
No patch ECG
data
N = 394
(15.6%)
P-value
Age at randomization (years) - n (%)
<75
683
577 (84.5%)
106 (15.5%)
0.75/0.62 (trend)
≥75, <80
1032
876 (84.9%)
156 (15.1%)
≥80
805
673 (83.6%)
132 (16.4%)
Mean (SD)
77.7 (5.9)
77.6 (5.9)
77.8 (6.1)
0.50
Sex - n (%)
Males
1340
1137 (84.9%)
203 (15.1%)
0.47
Females
1180
989 (83.8%)
191 (16.2%)
Race and ethnicitya - n (%)
Asian
27
20 (74.1%)
7 (25.9%)
0.17
Black
2
2 (100.0%)
0 (0.0%)
White
2045
1738 (85.0%)
307 (15.0%)
Otherb
21
17 (81.0%)
4 (19.0%)
Missing
425
349 (82.1%)
76 (17.9%)
Body mass index (kg/m2) - n (%)
<25
488
422 (86.5%)
66 (13.5%)
0.07/0.03 (trend)
25 to <30
751
639 (85.1%)
112 (14.9%)
≥30
571
466 (81.6%)
105 (18.4%)
Missing
710
599 (84.4%)
111 (15.6%)
Mean (SD)
28.2 (5.2)
28.0 (5.0)
29.3 (6.1)
<0.001
CHA2DS2VAsc score - n (%)
<3
33
31 (93.9%)
2 (6.1%)
<0.001/<0.001 (trend)
3
685
596 (87.0%)
89 (13.0%)
4
983
846 (86.1%)
137 (13.9%)
≥5
819
653 (79.7%)
166 (20.3%)
Median (IQR)
4 (3 - 5)
4 (3 - 5)
4 (4 - 5)
<0.001
Prior diagnoses at randomization - n (%)
Hypertension
2255
1908 (84.6%)
347 (15.4%)
0.32
Diabetes
713
582 (81.6%)
131 (18.4%)
0.02
Stroke or TIA
485
395 (81.4%)
90 (18.6%)
0.05
Chronic kidney disease (stage ≥3)
438
366 (83.6%)
72 (16.4%)
0.61
Thromboembolism
271
216 (79.7%)
55 (20.3%)
0.03
Myocardial infarction
269
226 (84.0%)
43 (16.0%)
0.87
Heart failure
244
191 (78.3%)
53 (21.7%)
0.006
Peripheral arterial disease
214
170 (79.4%)
44 (20.6%)
0.04
Medication prior to randomization - n (%)
Statin
1739
1462 (84.1%)
277 (15.9%)
0.54
RAAS inhibition
1599
1341 (83.9%)
258 (16.1%)
0.36
Proton-pump inhibitors or H2-antagonists
1265
1065 (84.2%)
200 (15.8%)
0.81
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.

```

### DOC-004 physical PDF page 6 — REPORT

```text
Source PDF: joi250068supp3_prod_1760999665.30362.pdf
Source PDF page: 6
Extraction method: native PDF text

Overall in
Patch group
N = 2520
Patch ECG
data
N = 2126
(84.4%)
No patch ECG
data
N = 394
(15.6%)
P-value
Calcium-channel blockers
1200
996 (83.0%)
204 (17.0%)
0.07
Diuretics
713
593 (83.2%)
120 (16.8%)
0.30
Aspirin or dipyridamole
705
585 (83.0%)
120 (17.0%)
0.23
Beta-blockers
619
529 (85.5%)
90 (14.5%)
0.39
P2Y12 inhibition
363
300 (82.6%)
63 (17.4%)
0.33
Oral anticoagulation
174
137 (78.7%)
37 (21.3%)
0.03
Direct oral anticoagulant
128
101 (78.9%)
27 (21.1%)
0.08
Vitamin K antagonist
59
47 (79.7%)
12 (20.3%)
0.31
Insulin
117
94 (80.3%)
23 (19.7%)
0.22
IQR = Interquartile range, SD = standard deviation, RAAS =Renin Angiotensin Aldosterone System. Row
percentages are presented to provide the compliance rate within each category of baseline characteristic. Chi-
square p-values are presented for categorical factors with the Mantel- Haenszel test for trend also presented
for ordinal categorical factors. Two-sample T-test and Mann-Whitney U-test p-values are presented for
continuous data with normal and non-normal distributions respectively. Missing data is excluded in the
calculation of p-values. aP-value compares white versus any other non-missing race and ethnicity group. bOther
category includes multiracial ethnicities (n=10) and 'any other ethnicity' (code S) recorded in secondary care
(n=11).
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.

```

### DOC-004 physical PDF page 7 — REPORT

```text
Source PDF: joi250068supp3_prod_1760999665.30362.pdf
Source PDF page: 7
Extraction method: native PDF text

eTable 3. Patch-detected conditions
Number of
participants
with condition
detected
% of those
randomized to
patch
(N = 2520)
% of those who
wore and
returned patch
(N = 2126)
Atrial fibrillation
89
3·53%
4·19%
Atrial fibrillation without flutter
74
2·94%
3·48%
Atrial fibrillation with flutter
15
0·60%
0·71%
Other findings resulting in urgent reporting to GP
Atrial flutter without fibrillation
13
0·52%
0·61%
Complete AV block
5
0·20%
0·24%
High grade AV block
10
0·40%
0·47%
AV block second degree Mobitz II
8
0·32%
0·38%
AV block second degree 2:1
1
0·04%
0·05%
Pauses lasting longer than 6 seconds
6
0·24%
0·28%
Sustained ventricular tachycardia (>30 seconds)
2
0·08%
0·09%
Non-urgent findings
Non-sustained ventricular tachycardia (≤30 seconds)
676
26·83%
31·80%
Sustained supraventricular tachycardia (>30 seconds)
134
5·32%
6·30%
Non-sustained supraventricular tachycardia (≤30 seconds)
1772
70·32%
83·35%
AV = Atrioventricular, GP = General practitioner
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.

```

### DOC-004 physical PDF page 8 — REPORT

```text
Source PDF: joi250068supp3_prod_1760999665.30362.pdf
Source PDF page: 8
Extraction method: native PDF text

0.5
0.75
1
1.25
1.5
2

< 80 years
≥ 80 years
Females
Males
Overall
Age at randomization
Sex
Ratio of proportions
(95% Confidence Interval)
1.31 ( 1.03 to  1.67)
1.08 ( 0.84 to  1.40)
1.50 ( 1.12 to  2.01)
1.07 ( 0.85 to  1.33)
1.21 ( 1.02 to  1.45), p = 0.03
Heterogeneity p = 0.28
Heterogeneity p = 0.07
AF/Participants (%)
Patch group
Usual care group
142/1715 (8.28%)
109/805 (13.54%)
105/1180 (8.90%)
146/1340 (10.90%)
251/2520 (9.96%)
110/1744 (6.31%)
97/776 (12.50%)
70/1180 (5.93%)
137/1340 (10.22%)
207/2520 (8.21%)
Absolute difference
(95% Confidence Interval)
1.97% (0.24%, 3.71%)
1.04% (-2.28%, 4.36%)
2.97% (0.86%, 5.08%)
0.67% (-1.66%, 3.00%)
1.75% (0.16%, 3.33%)
Ratio of proportions
 (95% Confidence Interval)
More AF in
usual care group
More AF in
patch group
eFigure 1. Proportions, absolute differences and ratios of proportions of participants with a primary care or secondary care record of atrial
fibrillation (AF)  between randomization and 2.5 years by randomized allocation overall and in age and sex subgroups. Ratios of proportions
in subgroups are plotted as squares with the size of each square proportional to the amount of statistical information available. The primary outcome
of ratio of proportions overall is represented by a diamond. The horizontal lines and the width of the diamond represent 95% confidence intervals (not
adjusted for multiplicity), and the dashed vertical line indicates the overall ratio of proportions for the effect of patch group on AF.  Squares or a
diamond to the right of the solid vertical line indicate a higher proportion of AF in the patch group, but the comparison is only significant (at p<0.05) if
the horizontal line, or diamond, does not overlap with the solid vertical line.
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.

```

### DOC-004 physical PDF page 9 — REPORT

```text
Source PDF: joi250068supp3_prod_1760999665.30362.pdf
Source PDF page: 9
Extraction method: native PDF text

(A)                                                                                                                                                                                                                                                                                                    (B)

                              60                                                                                                                                                                                                                                                                                                     40
                              55                                                                                                                                                                                                                                                                                                     35
                              50
                              45                                                                                                                                                                                                                                                                                                     30
                              40                                                                                                                                                                                                                                                                                                     25
                              35
                              30                                                                                                                                                                                                                                                                                                     20
                              25                                                                                                                                                                                                                                                                                                     15
                              20
                              15                                                                                                                                                                                                                                                                                                     10
                              10                                                                                                                                                                                                                                                                                                          5
                                   5
                                   0               1                                      2                                      3                                      4                                      5                                      6                                      7                                      8                                      9                             10                    11                    12                    13                    140<1                                         10                                          20                                          30                                          40                                          50                                          60                                          70                                          80                                          90                                 100

                                                                Day of first episode of AF in monitoring period                                                                                                                                                                                                                                                                                                         Percentage time in AF

        (C)                                                                                                                                                                                                                                                                                                    (D)

                              50                                                                                                                                                                                                                                                                                                     50
                              45                                                                                                                                                                                                                                                                                                     45
                              40                                                                                                                                                                                                                                                                                                     40                                                                                                                                                                                                             42%
                              35                                                                                                                                                                                                                                                                                                     35
                              30                                                                                                                                                                                                                                                                                                     30                                                                                        29%
                              25                                                                                                                                                                                                                                                                                                     25
                              20                                                                                                                                                                                                                                                                                                     20                                                                                                                                                   20%
                              15                                                                                                                                                                                                                                                                                                     15
                              10                                                                                                                                                                                                                                                                                                     10                                9%
                                   5                                                                                                                                                                                                                                                                                                      5
                                   0                                                                                                                                                                                                                                                                                                      0         [30sec,6min)                                    [6min,6hr)                                                            [6hr,24hr)                                                                                                     ≥       24hr
                                          0                                                                                   48                                                                          96                                                                 144                                                        192                                                        240                                                        288                                                        336
                                                                            Duration of longest AF episode, in hours                                                                                                                                                                                                                                                              Duration of longest AF episode, grouped

        (E)                                                                                                                                                                                                                                                                                                    (F)

                   15                                                                                                                                                                                                                                                                                                      15

                   10                                                                                                                                                                                                                                                                                                      10

                         5                                                                                                                                                                                                                                                                                                      5

                         0           75                                                                                     100                                                                            125                                                                            150                                                                            175                                                                            200                                                                            22500                                                                                                            25                                                                                                   50                                                                                                   75                                                                                          100                                                                                 125                                                                                 150

                                                                           Maximum hear t rate, beats per minute                                                                                                                                                                                                                                                                   Minimum hear t rate, beats per minute
eFigure 2. Patch-detected atrial fibrillation metrics.                              (A) Day of first episode (B) Burden (C) Duration of longest episode, in hours
(D)        Duration of longest episode, grouped (E) Maximum hear t rate during episode (F) Minimum hear t rate during episode

```

### DOC-004 physical PDF page 10 — REPORT

```text
Source PDF: joi250068supp3_prod_1760999665.30362.pdf
Source PDF page: 10
Extraction method: native PDF text

100%

                                         80%

                                         60%

                                         40%

                                         20%

                                                 0%0                                                                                                                                                                                                                                                                                                                                             1                                                                                                                                                                                                                                                                                                                                             2                                                                                                                                                                                                                                                                                                                                             3                                                                                                                                                                                                                                                                                                                                             4                                                                                                                                                                                                                                                                                                                                             5                                                                                                                                                                                                                                                                                                                                             6

                                                                                                                                                                                                                                                                                                                                                                               Months from urgent patch repor t

  Number at risk
                                                                    89                                                                                                                               34                                                                                                                                                                                                                                                                                                                       18                                                                                                                                                                                                                                                                                                                       10                                                                                                                                                                                                                                                                                                                                  8                                                                                                                                                                                                                                                                                                                                             7                                                                                                                                                                                                                                                                                                                                             6

 eFigure 3. Kaplan−Meier plot of time from urgent patch report to first primary care record of atrial fibrillation (AF), restricted to
those with patch−detected AF. The number of participants at risk at the start of each month is shown beneath the figure. The seven
participants with a post−randomization record of AF in the primary care record that pre−dates the urgent patch report are included in the
number at risk at day 0 and counted as an event immediately after this.

```

### DOC-004 physical PDF page 11 — REPORT

```text
Source PDF: joi250068supp3_prod_1760999665.30362.pdf
Source PDF page: 11
Extraction method: native PDF text

(A)                                                                                                                                                                                                                                                                                          (B)

                            60                                                                                                                                                                                                                                                                                           40
                            55                                                                                                                                                                                                                                                                                           35
                            50
                            45                                                                                                                                                                                                                                                                                           30
                            40                                                                                                                                                                                                                                                                                           25
                            35
                            30                                                                                                                                                                                                                                                                                           20
                            25                                                                                                                                                                                                                                                                                           15
                            20
                            15                                                                                                                                                                                                                                                                                           10
                            10                                                                                                                                                                                                                                                                                                5
                                 5
                                 0              1                                      2                                      3                                      4                                      5                                      6                                      7                                      8                                      9                             10                    11                    12                    13                    140<1                                         10                                          20                                          30                                          40                                          50                                          60                                          70                                          80                                          90                                 100

                                                    Day of first episode of AF/AFL in monitoring period                                                                                                                                                                                                                                                                                         Percentage time in AF/AFL

       (C)                                                                                                                                                                                                                                                                                          (D)

                            50                                                                                                                                                                                                                                                                                           50                                                                                                                                                                                                       46%
                            45                                                                                                                                                                                                                                                                                           45
                            40                                                                                                                                                                                                                                                                                           40
                            35                                                                                                                                                                                                                                                                                           35
                            30                                                                                                                                                                                                                                                                                           30                                                                                      26%
                            25                                                                                                                                                                                                                                                                                           25
                            20                                                                                                                                                                                                                                                                                           20                                                                                                                                              18%
                            15                                                                                                                                                                                                                                                                                           15
                            10                                                                                                                                                                                                                                                                                           10                             10%

                                 5                                                                                                                                                                                                                                                                                            5
                                 0                                                                                                                                                                                                                                                                                            0         [30sec,6min)                                    [6min,6hr)                                                            [6hr,24hr)                                                                                                     ≥       24hr
                                         0                                                                                   48                                                                          96                                                                 144                                                        192                                                        240                                                        288                                                        336
                                                               Duration of longest AF/AFL episode, in hours                                                                                                                                                                                                                                                 Duration of longest AF/AFL episode, grouped

       (E)                                                                                                                                                                                                                                                                                          (F)

                  15                                                                                                                                                                                                                                                                                           15

                  10                                                                                                                                                                                                                                                                                           10

                       5                                                                                                                                                                                                                                                                                             5

                       0            75                                                                                     100                                                                            125                                                                            150                                                                            175                                                                            200                                                                            22500                                                                                                            25                                                                                                   50                                                                                                   75                                                                                          100                                                                                 125                                                                                 150

                                                                        Maximum hear t rate, beats per minute                                                                                                                                                                                                                                                         Minimum hear t rate, beats per minute
eFigure 4. Patch         -detected atrial fibrillation and/or flutter (AF/AFL) metrics.  (A) Day of first episode (B) Burden (C) Duration of longest
episode, in hours (D) Duration of longest episode, grouped (E) Maximum heart rate during episode (F) Minimum heart rate during episode.

```
