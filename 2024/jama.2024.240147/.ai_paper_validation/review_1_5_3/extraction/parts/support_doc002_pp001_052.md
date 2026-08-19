# Support quantitative evidence map — DOC-002 pp. 1–52

## Scope, authority, and status

- **Direct source:** `joi240147supp1_prod_1738701765.28701.pdf`, PDF pp. 1–52 (DOC-002 only).
- **Scope completed:** all 52 assigned PDF pages: supplement index; original trial protocol v1.4, dated 30 September 2021 (pp. 2–35); and the opening pages of final protocol v1.8, dated 21 November 2022 (pp. 36–52).
- **Evidence method:** `.ai_paper_validation/preprocessed/DOC-002.txt` was used as a page-delimited locator/transcription aid. Direct current-PDF layout extraction was performed for pp. 1–52. PDF render inspection confirmed the intervention-process table on pp. 21–22 and the statistical-analysis/violation text on pp. 25–26. The PDF is the authority for the transcriptions below.
- **Nature of evidence:** these pages are protocol/SAP-adjacent planning material, not trial-result tables. They define outcomes, intervention thresholds, anticipated sample size/power, planned models, missing-data rules, sensitivity/subgroup analyses, and administrative monitoring. No workbook, CSV, DOC/DOCX, formula cell, or cached workbook value is in this assigned source unit.
- **Candidate work:** none performed. This is a relationship inventory only; it does not diagnose, rank, reject, or register quality-control candidates.

## Page-complete coverage record

| PDF pages | Content and mapping disposition |
|---|---|
| 1 | Supplement index. Administrative/locator only: identifies original protocol v1.4 (starts p. 2), final protocol v1.8 (starts p. 36), protocol-change summary (p. 78), and original/final SAP (p. 80). No result-relevant quantitative relationship on this page. |
| 2–4 | Original protocol title/date/version and contents. Administrative/locator only; contents identify the planned statistical-analysis section at pp. 25–26. |
| 5–10 | Original-protocol general information, investigators/sites/DMSC, and abbreviations. No result-relevant quantitative relationship beyond administrative identifiers; no applicable result table or statistic. |
| 11–13 | Original-protocol synopsis: objective/outcome, treatment thresholds, outcome time windows, planned sample-size totals, and AE tracking schedule mapped below. |
| 14 | Original-protocol investigator contact continuation. No applicable quantitative result relationship. |
| 15–16 | Background and study objectives: external contextual quantities and the trial's primary outcome/time window mapped below. |
| 17–18 | Recruitment/randomisation: timing, allocation ratio, stratification, blocks (unspecified size), and two blinded assessors per centre mapped below. |
| 19 | Consent/follow-up timing definitions (24-hour deliberation, 30-day thresholds, 6- and 12-month follow-up) mapped below. |
| 20–22 | Intervention text and the visual intervention-process table. All dose/flow, saturation, duration, ABG timing, and intubation-transition rules mapped below. |
| 23–24 | Outcome definitions, collection frequency, data elements, and ABG time-point-selection rule mapped below. |
| 25–26 | Outcome definitions, anticipated event rates/power, analysis population, missing-data, model/test, adjustment, and subgroup/sensitivity/violation rules mapped below. |
| 27–31 | Safety/event monitoring and administration. The event timing, interim review counts, and quoted pilot desaturation counts are mapped; other drug/accounting, ethics, personnel, archive, and funding text is administrative. |
| 32 | Protocol-change governance only. No applicable quantitative result relationship. |
| 33 | Figure 1 participant timeline and Figure 2 study-progress timeline. Direct PDF page contains only figure labels without extractable numeric outcome/statistical data; no applicable quantitative result relationship. |
| 34–35 | References only. No applicable quantitative result relationship. |
| 36–38 | Final protocol v1.8 title/date/version and contents. Administrative/locator only; it places the later full statistical-analysis material at pp. 62 onward, outside this shard. |
| 39–46 | Final-protocol investigator/site/DMSC information and abbreviations. No applicable quantitative result relationship. |
| 47–49 | Final-protocol synopsis. It repeats the mapped primary objective, intervention thresholds, outcomes, sample totals, and event-monitoring schedule. The matching material is explicitly retained as a final-version occurrence below. |
| 50 | Final-protocol investigator contact continuation. No applicable quantitative result relationship. |
| 51–52 | Final-protocol background/objectives/eligibility opening. It repeats the contextual quantities and primary outcome; pp. 53 onward, including final-protocol intervention/analysis text, is outside this shard. |

## Quantitative and reporting relationship inventory

Provisional IDs are unique to this extraction part and are intended for coordinator reconciliation to package-wide `N` and `S` identifiers. “Main-paper key” is a semantic matching key, not a claim that a matching main-paper result has been confirmed in this mapper pass.

| Provisional ID | Source location(s) | Printed relationship / definition | Main-paper key for matching |
|---|---|---|---|
| DOC002A-N01 | pp. 11–13, 16, 23, 47–49, 52 | **Primary composite outcome:** incidence of 30-day mortality and/or major respiratory complications (pneumonia and ARDS) within 30 days. The intervention is restrictive versus liberal oxygen for the first/eight initial hours after trauma. | `PRIMARY_COMPOSITE_30D_DEATH_OR_MAJOR_RESPIRATORY_COMPLICATION` |
| DOC002A-N02 | pp. 13, 23, 49 | **Secondary outcomes/time points:** mortality at 30 days and 12 months; major respiratory complications within 30 days; HOS/ICU length of stay and days alive outside ICU; ventilation time until day 30, days alive without ventilation, re-intubations within day 30; post-discharge pneumonia within day 30; hypoxaemia episodes during intervention (saturation <90%); surgical-site infection within day 30; EQ-5D-5L and GOSE at 6 and 12 months. | `SECONDARY_OUTCOMES_30D_6M_12M` |
| DOC002A-N03 | pp. 12, 20–22, 48 | **Restrictive oxygen definition:** for eight hours, lowest oxygen delivery at least 21% to ensure SpO2 target =94%; only participants at FiO2=0.21/no supplemental oxygen can saturate >94%. For non-intubated participants with saturation <94%, use the lowest 0–15 L/min flow producing 94%; pre-oxygenation before intubation is usual care. | `INTERVENTION_RESTRICTIVE_OXYGEN_SPO2_94` |
| DOC002A-N04 | pp. 12, 20–22, 48 | **Liberal oxygen definition:** non-intubated: 15 L O2/min by non-rebreather mask in prehospital/trauma bay/transport, reducible to >=12 L/min in OR/ICU/PACU/ward if arterial saturation >=98%; intubated: FiO2=1.0 in prehospital/trauma bay/transport, reducible to >=0.6 in OR/ICU/PACU/ward if arterial saturation >=98%. | `INTERVENTION_LIBERAL_OXYGEN_FLOW_FIO2` |
| DOC002A-N05 | pp. 17, 20–22, 24 | **Timing and treatment measurements:** enrolment/intervention begins at T0 and continues eight hours; trauma-bay initiation must not be delayed >90 minutes after hospital arrival. Two ABGs: T1 = hour 1 +/-30 min and T6 = hour 6 +/-2 h after randomisation; if unavailable at T1, draw as soon as possible; if >2 ABGs occur, enter the ABGs closest to T1/T6. Ventilated oxygen/saturation is automatically tracked; non-ventilated values are recorded hourly. | `INTERVENTION_DURATION_AND_ABG_TIMING` |
| DOC002A-N06 | pp. 13, 25–26, 28, 30, 49 | **Planned sample/count framework:** include up to 1,600; stop at 710 per arm/1,420 total with 30-day follow-up. Inclusion continues while 30-day follow-up is assessed. DMSC review is planned after 355 (~25% of sample-size estimate) and 710 (~50%). Final trial report is after 1,420 participants with complete 30-day, 6-, and 12-month follow-up. | `PLANNED_SAMPLE_SIZE_1420_710_PER_ARM` |
| DOC002A-N07 | p. 15, repeated p. 51 | External/pilot contextual quantities: hyperoxaemia reported as 16–50% in mechanically ventilated patients; cited studies of 152,000 and 14,000 patients, and 2,928 ICU patients with low versus high targets 8 vs 12 kPa for max 90 days; TRAUMOX1 N=41, 24-h intervention; prior medians [IQR] 7 [4–10] min to randomisation and 51 [29.0–67.5] min trauma-to-bay arrival. These are background citations/planning context, not TRAUMOX2 outcomes. | `CONTEXT_TRAUMOX1_AND_BACKGROUND` |
| DOC002A-N08 | pp. 25–26 | **Sample-size assumptions:** TRAUMOX1 primary composite =20% restrictive and 33% liberal. Assumed trauma mortality 6–12%; VAP incidence almost 30%. With 710/arm, protocol states capacity to detect a 33% risk reduction if liberal primary-outcome incidence is 15%, with 80% power and 5% significance. Arithmetic implication of a 33% relative reduction from 15% is approximately 10% in restrictive arm; this latter value is not printed on these pp. 25–26 but appears later in the final SAP outside this shard. | `SAMPLE_SIZE_PRIMARY_OUTCOME_ASSUMPTIONS` |
| DOC002A-N09 | pp. 25–26 | **Analysis population/missingness:** modified intention-to-treat primary analysis excludes post-randomisation participants with no injuries (ISS=0); per-protocol removes >=1 major protocol violation. If <5% of required data missing: complete-case. If >5% missing and not MCAR: inverse-probability weighting; sensitivity analysis will test missing-data assumptions. | `ANALYSIS_POPULATION_AND_MISSING_DATA` |
| DOC002A-N10 | pp. 26 | **Major-protocol-violation operational thresholds:** restrictive arm: supplemental oxygen plus arterial saturation >=98%, or PaO2 >=14 kPa. Liberal arm: no supplemental oxygen at any time point, or saturation <=94% while oxygen is below 15 L/min (non-intubated) or FiO2=1.0 (intubated). | `PER_PROTOCOL_MAJOR_VIOLATIONS` |
| DOC002A-N11 | pp. 27–29, 49 | Safety event measurement schedule: AE/SAE chart review once in first 24 h, then every third day to discharge, maximum 30 days; SAE notification within 24 h; SUSAR fatal/life-threatening report <=7 d plus follow-up <=8 d (15 d total); other SUSAR <=15 d. In TRAUMOX1, seven desaturation episodes (SpO2 <90%) in restrictive arm, median 87% [87–89]; five of seven SpO2 <89% episodes occurred in two participants. | `SAFETY_EVENTS_AND_HYPOXAEMIA` |
| DOC002A-N12 | pp. 17–18 | Randomisation design: 1:1, variable block sizes (sizes not stated in v1.4), stratified by centre/pre-hospital base and intubation at inclusion; allocation uses concealed envelopes. At least two blinded primary-outcome assessors at each centre. | `RANDOMISATION_AND_BLINDING` |
| DOC002A-N13 | pp. 19, 23–24 | Consent and follow-up timing: 24-h next-of-kin/patient deliberation; participant consent ceases if capacity absent 30 days after trauma; if next of kin cannot be contacted, follow-up continues at day 30, 6 months, 12 months. | `FOLLOW_UP_AND_CONSENT_WINDOWS` |
| DOC002A-N14 | pp. 25–26 | Outcome-defining labels: pneumonia per CDC; ARDS per Berlin definition; traumatic brain injury severe AIS >=5, moderate AIS 3–4, mild AIS 1–2. | `OUTCOME_AND_SUBGROUP_DEFINITIONS` |

## Statistical-definition inventory

| Provisional ID | Source location(s) | Statistical relationship / planned analysis | Main-paper key for matching |
|---|---|---|---|
| DOC002A-S01 | pp. 25–26 | Power design: 710 per arm; 33% relative risk reduction target; 80% power; two-sidedness is not stated; significance level 5%; anticipated liberal incidence 15%. No formula is displayed. | `POWER_AND_SAMPLE_SIZE_PRIMARY_OUTCOME` |
| DOC002A-S02 | p. 26 | Primary composite comparison: logistic regression, reported as OR with 95% CI; adjusted for age, sex, centre, intubated at randomisation (yes/no), and known pneumonia at admission (under treatment). | `PRIMARY_ANALYSIS_ADJUSTED_OR_95CI` |
| DOC002A-S03 | p. 26 | Secondary outcomes: Fisher exact test/Chi-square test for categorical data; “competing risk survival analyses for continuous data”; 5% significance level. Exact test-selection criteria, survival estimand, and competing event are not specified on these pages. | `SECONDARY_ANALYSES_TESTS_AND_SIGNIFICANCE` |
| DOC002A-S04 | pp. 25–26 | Modified intention-to-treat excludes ISS=0/no-injury post-randomisation participants; per-protocol excludes participants with >=1 major violation. | `MITT_AND_PER_PROTOCOL_POPULATIONS` |
| DOC002A-S05 | p. 26 | Missing-data decision rule: <5% complete-case; >5% and not MCAR, inverse probability weighting; sensitivity analysis for missing-data assumptions. | `MISSING_DATA_DECISION_RULE` |
| DOC002A-S06 | p. 26 | Prespecified subgroups: initially intubated within one hour (yes/no); ICU admission (yes/no); moderate/severe TBI (yes/no); COPD (yes/no); hypoxaemia episodes; prehospital versus in-hospital enrolment. Additional ISS-adjusted analysis. Interaction/modeling and multiplicity approach are not stated here. | `PRESPECIFIED_SUBGROUPS_AND_ISS_ADJUSTMENT` |
| DOC002A-S07 | pp. 30, 49 | Interim/DMSC framework: blinded interim analysis at 355 and 710 participants with 30-day follow-up; original protocol says early-stop criteria to be decided by steering committee. No alpha-spending or formal boundary is supplied in this scope. | `INTERIM_ANALYSIS_DMSC` |
| DOC002A-S08 | pp. 11–13, 23, 47–49 | Primary estimand label is an incidence/rate of a composite endpoint within 30 days, not a rate per person-time. Components are mortality and pneumonia/ARDS; timing and composite construction are explicit. | `PRIMARY_ENDPOINT_MEASURE_LABEL` |

## Version occurrences and cross-source matching notes

- v1.8 pp. 47–52 repeats the v1.4 synopsis/background/objective material from pp. 11–16, but adds final administrative registration identifiers (EudraCT 2021-000556-19, ClinicalTrials.gov NCT05146700, ethics H-21018062) and changes the setting language at p. 52 from “within the EU” to “within continental Europe.” These are protocol-version facts, not trial-result comparisons.
- The final protocol's full intervention, analysis, and major-violation sections begin after this shard (pp. 53, 62–63 respectively); they must be mapped by the distinct pp. 53–103 support shard rather than inferred here.
- No table of observed trial results, figure with observed counts, P value, confidence interval, effect estimate, sensitivity-result value, subgroup-result value, or displayed formula occurs in pp. 1–52. The visual intervention table on pp. 21–22 is a protocol operational table and its thresholds have been transcribed in DOC002A-N03 through N05.
- There is no matching main-paper key supplied in this support source as an explicit identifier. The semantic keys above identify the intended matching target for the main mapper/cross-source reviewer; all required population, time window, contrast, measure, and adjustment labels are retained to prevent a false match.

## Extraction counts and limitations

- PDF pages inspected/mapped: **52/52**.
- Result-relevant numeric/reporting relationships: **14** provisional numeric relationships (DOC002A-N01–N14).
- Inferential/statistical definitions: **8** provisional statistical relationships (DOC002A-S01–S08).
- Tables/figures with quantitative operational content: **1** two-page intervention-process table (pp. 21–22); **0** observed-result tables or figures.
- Explicit no-applicable result units: **27 pages** (1–10, 14, 32–35, 36–46, 50; p. 33's unquantified timeline figures are included within that count); administrative content was opened rather than assumed irrelevant.
- Gaps/limitations: no scientific-coverage gap in assigned pp. 1–52. The source does not provide final-protocol analysis details until later pages, a displayed power formula, exact block sizes in v1.4, sidedness, multiplicity adjustment, or an observed main-paper result; these are absent from this assigned range, not inferred.
