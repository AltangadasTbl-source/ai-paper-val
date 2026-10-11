# Support quantitative mapping — DOC-003, PDF pp. 1-30

## Scope and source handling

- **Direct source:** `joi250084supp2_prod_1765403089.61751.pdf`, PDF pp. 1-30 only (all fresh-required).
- **Fresh extraction:** page-specific native and layout text were created with `pdftotext -f N -l N` and `pdftotext -layout -f N -l N` for every assigned page. Outputs are under `preprocessing/DOC-003/p001-p030/native/` and `preprocessing/DOC-003/p001-p030/layout/`.
- **Authority:** the direct PDF is authoritative. Layout text was adequate to transcribe the two small tables on pp. 8-9 and the method table on pp. 27-30; targeted OCR was not required for this scope.
- **Mapping convention:** `D3A-N` records numeric/population/definition relationships and `D3A-S` records inferential or formal statistical-method relationships. These are extraction keys, not candidates or adjudications.

## Unit completion record

| PDF pages | Content | Result-relevant quantitative mapping status |
|---|---|---|
| 1 | Supplement cover | No applicable numeric/statistical result. |
| 2-4 | Table of contents | No independent result; indexes eFigures/eTables and their later PDF pages. |
| 5-6 | Study-group list | No applicable numeric/statistical result. |
| 7-30 | Additional methods, definitions, and methods-to-eTable/eFigure keys | Mapped below. |

## Numeric, denominator, population, unit, and definition relationships

| Key | Exact direct-PDF location | Extracted relationship and printed values | Population/time/contrast/scale or downstream matching key |
|---|---|---|---|
| D3A-N001 | p. 7, Selection of Primary Endpoint | Endpoint rationale reports 5%-7% weight loss in prior DPPs; each kg (2.2 lb) weight loss corresponds to 16% diabetes-risk reduction; 4% loss for 100 kg (220 lb) is approximately 8.8 lb and is described as potentially about 64% risk reduction. | Context only; percentages are external-rationale statements, not trial result estimates. Preserve weight-loss / physical-activity / A1C endpoint-component labels. |
| D3A-N002 | p. 7 | Physical-activity benchmark: 150 min/week, without the weight-loss target, is stated to correspond to 44% lower diabetes risk independent of approximately 2.9 kg mean loss; cited meta-analysis range 26%-50%. | Context only; establishes `150 minutes/week` unit and threshold used in later composite-outcome keys. |
| D3A-N003 | p. 7 | A1C endpoint rationale: 0.2 percentage-point improvement at 1 year; previous intervention 0.1% improvement versus control 0.1% increase. | Context only; establishes A1C percentage-point direction and 12-month time point. |
| D3A-N004 | p. 8, A1C Measurement table | A1C device counts: baseline Afinion 2 Analyzer 334, A1CNow+ 33, serum 1; 12-month follow-up Afinion 282, A1CNow+ 30, serum 0. | Device-method denominator components: baseline total 368; 12-month listed total 312. Match to randomized population and 12-month A1C availability, not necessarily identical to an outcome-analysis denominator. |
| D3A-N005 | p. 8, A1C measurement protocol | A1CNow+ repeat/failure rules: repeat after a quality-control error; failure is two consecutive QC/error messages in one visit; alternative test if deviation from a prior measurement within 3 months is <= -0.9 or >= +0.8 A1C points (stated outside a 95% CI). | Measurement-definition key for A1C values; threshold is in A1C percentage points. |
| D3A-N006 | p. 9, discordant-device table | Device transitions: Afinion-to-A1CNow+ 6 (1.6%); A1CNow+-to-Afinion 1 (0.27%); serum-to-Afinion 0 (0); Afinion-to-serum 0 (0); serum-to-A1CNow+ 1 (0.27%); total 8 (2.2%). | Percent denominator labeled trial population; the listed total percentage is compatible with 8/368 at displayed rounding. Link to N004 and N007. |
| D3A-N007 | p. 11, Physical Activity Measurement | Among 368 randomized participants, 33 were assigned GT9X-BT at baseline before the switch to CPIW. | Randomized-population denominator key. Device assignment is measurement context, not an intervention arm count. |
| D3A-N008 | p. 13, Accelerometry collection | Wrist accelerometers worn 7 consecutive days per scheduled visit; baseline then monthly for 12 visits; average weekly MVPA across follow-up sums valid post-baseline wear-period weekly minutes and divides by available periods, maximum 11 post-baseline visits. | Defines PA aggregation, time unit (minutes/week), and maximum follow-up periods. Match to physical-activity components/results. |
| D3A-N009 | p. 13, preprocessing and compliance | Valid day requires >=10 hours wear time; nonwear is a 90-minute consecutive-zero-count window. Participants wearing the monitor fewer than 5 of 7 assigned days are noncompliant and assigned 0 physical-activity minutes for that week. | Defines missingness/zero-assignment rule and denominator/measurement status for MVPA. |
| D3A-N010 | p. 13, MVPA calculation | MVPA defined as vector-magnitude counts/minute >=3941 (Montoye cut point); sustained bouts are >=10 consecutive minutes at the same threshold. | Defines activity scale and threshold; preserve distinction between total MVPA and bouted MVPA. |
| D3A-N011 | pp. 14-17, R code | Code imports raw CSV records, derives ID/visit/site from file name, uses a 90-minute nonwear and 840-minute maximum nonwear setting for valid-day flag, and outputs `minutes.mvpa.3941` plus 10-to-infinity-minute bout counts/durations at 2185, 2859, and 3941 thresholds. | Computational-definition key; code uses `ac` rather than the calculated imputed object in shown `activity_stats` calls, so retain source wording/code exactly for later human comparison rather than infer an implementation correction. |
| D3A-N012 | p. 20 | Participant interactions: 3 in-person study visits at baseline, 6 months, and 12 months. | Follow-up-schedule key. |
| D3A-N013 | p. 21, Sweetch intervention | Push notifications limited to 10/day (fewer when adherence high). | Intervention-exposure definition; not a trial outcome. |
| D3A-N014 | p. 22, educational modules | Core phase months 1-6 includes 19 lessons; maintenance months 7-12 includes 6 lessons. | Intervention-program dose/time key. |
| D3A-N015 | p. 23, CONSORT-AI table | Version is JITAI algorithm 1.0; missing app data are not imputed; app-generated outputs include goal recommendations, educational content, and notification timing. | Algorithm/intervention label key; distinguish app-data missingness from trial-outcome missingness. |
| D3A-N016 | pp. 24-26, Algorithm Overview | Deployment uses individual participant state/action history, while preclinical training used pooled historical cross-user data; feedback outcomes are active minutes and app opens in proximity to a prompt. | Analysis-unit / intervention-mechanism key. No numerical trial result reported. |
| D3A-N017 | p. 27, Definitions of study cohorts | Primary Analysis = all randomized participants. Per Protocol = randomized participants who completed 12-month visit and did not use prohibited steroids, antihyperglycemics, or weight-loss medications. | Population-definition key for every primary-analysis/per-protocol result and eTable 11/14/15. |
| D3A-N018 | p. 28, eFigure 3 method | Age-adjusted risk difference (aRD) in percentage points; one-sided 95% CI; primary and secondary diabetes-risk-reduction outcomes at 12 months; reference noninferiority line -15 percentage points. Negative aRD = lower outcome-achievement frequency in AI-DPP than Human-DPP. | Matching key for eFigure 3 and main-paper binary outcomes: contrast AI-DPP minus Human-DPP; age-adjusted; one-sided 95% CI; noninferiority threshold -15 pp. |
| D3A-N019 | p. 28, eFigure 4 method | Subgroup risk differences in percentage points with one-sided 95% CIs by site, sex, age, baseline A1C, and BMI category; same -15 pp noninferiority reference and negative-direction definition. | Matching key for eFigure 4; subgroup analyses exploratory. |
| D3A-N020 | pp. 28-29, eTables 1-11 method descriptions | eTable 1b is number/percent of AI-DPP members starting each version; eTable 2 is number/percent of Human-DPP members assigned to one of four sites; eTable 4 eligibility criteria are fasting glucose 100-125 mg/dL, study A1C 5.7%-6.4%, or clinic A1C 5.7%-6.4%; eTable 9 windows are day 168-196 (6-month) and 351-379 (12-month); eTable 10 concerns prohibited antihyperglycemic, weight-loss, or steroid medication, with GLP-1 receptor agonists classified as antihyperglycemic. | Cross-occurrence keys for later tables. eTable 3/5/6/7 use the randomized population; eTable 11 uses per protocol. Preserve A1C and glucose units and window endpoints. |
| D3A-N021 | p. 29, eTable 12 method | Composite outcome components: >=5% weight loss; >=4% weight loss plus >=150 minutes/week physical activity; or >=0.2% HbA1c reduction. Each unique-component-combination proportion = number in combination / number meeting composite outcome, separately by arm and overall. | Denominator-definition key for eTable 12; denominator is composite achievers, not all randomized participants. |
| D3A-N022 | pp. 29-30, eTables 13-18 methods | eTable 13 records primary-analysis participants with diabetes-range A1C at 6 and/or 12 months; they fail endpoint regardless of weight/PA; diabetes diagnosis was not adjudicated and needs two confirmatory tests. eTable 14 is per-protocol 12-month continuous weight/A1C/weekly-PA changes; eTable 15 is per-protocol binary outcomes. | Outcome/population matching keys; distinguish diabetes-range measurement from adjudicated diabetes diagnosis. |
| D3A-N023 | p. 30, eTable 16 method | Primary analysis classifies no 12-month visit as treatment failure. Sensitivity multiple imputation by chained equations assumes missing at random; includes group, baseline weight/PA/A1C, demographics, and group-normalized engagement; 20 imputed data sets combined with Rubin's rules. | Missing-data sensitivity definition and matching key for eTable 16. |
| D3A-N024 | p. 30, eTable 17 method | Pattern-mixture sensitivity: AI-DPP noncompleters imputed 0% primary-outcome success; Human-DPP noncompleters imputed observed-completer rate 37.8%; stated directional bias against AI-DPP. | Missing-not-at-random sensitivity definition and numeric assumption key. |
| D3A-N025 | p. 30, eTables 18a-18b methods | Primary analysis gives 0 weekly PA to assigned-period Actigraph nonwear. eTable 18a “best case” assumes participants with <100% compliance would attain 150 weekly minutes; eTable 18b assumes all participants attain 150 min/week. | Physical-activity missingness sensitivity definitions and endpoint-component matching keys. |

## Inferential and formal statistical-method relationships

| Key | Exact direct-PDF location | Test/model/interval relationship | Population, contrast, direction, and matching key |
|---|---|---|---|
| D3A-S001 | p. 8 | Device-discordance threshold is stated as outside a 95% CI for A1CNow+ versus venous A1C when deviation <= -0.9 or >= +0.8 points. | Measurement-quality rule; no test statistic or P value supplied. |
| D3A-S002 | p. 28, eFigure 3 method | Age-adjusted risk difference, one-sided 95% CI, noninferiority if CI does not cross -15 percentage points. | Randomized population; AI-DPP minus Human-DPP; 12 months; primary/secondary binary diabetes-risk-reduction outcomes. |
| D3A-S003 | p. 28, eFigure 4 method | Subgroup risk differences, one-sided 95% CIs, -15 percentage-point noninferiority line; no multiplicity adjustment because exploratory and not intended for formal hypothesis testing. | Randomized population; site/sex/age/baseline-A1C/BMI subgroup strata; AI-DPP minus Human-DPP. |
| D3A-S004 | p. 29, eTable 4 method | Chi-squared test compares group proportions; Wilcoxon rank-sum compares continuous measures. | Randomized population and per-protocol eligibility breakdown; matching key for eTable 4 P values/tests. |
| D3A-S005 | p. 29, eTable 9 method | Chi-squared test compares proportions outside visit window; Wilcoxon rank-sum compares continuous days outside window. | Randomized population; 6- and 12-month schedule windows defined in N020. |
| D3A-S006 | p. 29, eTable 10 method | Chi-squared test for between-group comparison of prohibited-medication proportions. | Randomized population; AI-DPP versus Human-DPP. |
| D3A-S007 | p. 30, eTable 16 method | Twenty chained-equation imputed data sets are combined using Rubin's rules under missing-at-random assumption. | Randomized primary analysis; 12-month missing outcome sensitivity. |

## Table/figure and main-paper match register

| Direct-PDF location | Result-relevant later object or main-paper key | Required identity fields before any cross-source comparison |
|---|---|---|
| pp. 8-9 | A1C measurement-method/availability statements | baseline versus 12-month; device method; count versus trial-population percentage; A1C availability versus outcome-analysis population. |
| pp. 13-17 | Main-paper physical-activity and composite-endpoint components; eTables 14, 16-18 | MVPA threshold 3941 counts/min; valid-day/nonwear/compliance rule; visit aggregation; 0-minute assignment rule; primary versus sensitivity scenario. |
| p. 27 | Main-paper and eTable primary-analysis/per-protocol results | all randomized versus completed-12-month/no-prohibited-medication cohort. |
| p. 28 | eFigure 3 and main-paper binary outcomes | AI-DPP minus Human-DPP; age-adjusted RD; percentage points; one-sided 95% CI; -15 pp threshold; 12 months. |
| p. 28 | eFigure 4 | subgroup definition; RD percentage points; one-sided 95% CI; exploratory/no multiplicity adjustment; -15 pp threshold. |
| pp. 28-30 | eTables 1-18 | exact table number; listed population; outcome/time point; count/proportion denominator; model/test; primary, per-protocol, or stated sensitivity condition. |

## Limitations of this shard

- Pages 1-30 contain definitions and methods only; their indexed eFigures/eTables begin at PDF p. 32 and were outside this assigned scope. No numerical results from those later pages were inferred.
- Native/layout text was usable. The blank PDF p. 12 was explicitly inspected and has no applicable content.
- This artifact deliberately records no candidate diagnosis, calculation conclusion, or adjudication.
