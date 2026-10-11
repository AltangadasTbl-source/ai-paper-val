# Support quantitative evidence map — DOC-002 pp. 1–52

## Scope, authority, and status

- **Direct source:** `joi240147supp1_prod_1738701765.28701.pdf`, PDF
  pp. 1–52 (DOC-002 only).
- **Scope completed:** all 52 assigned PDF pages: supplement index;
  original trial protocol v1.4, dated 30 September 2021 (pp. 2–35); and
  the opening pages of final protocol v1.8, dated 21 November 2022
  (pp. 36–52).
- **Evidence method:** `.ai_paper_validation/preprocessed/DOC-002.txt`
  was used as a page-delimited locator/transcription aid. Direct
  current-PDF layout extraction was performed for pp. 1–52. PDF render
  inspection confirmed the intervention-process table on pp. 21–22 and
  the statistical-analysis/violation text on pp. 25–26. The PDF is the
  authority for the transcriptions below.
- **Nature of evidence:** these pages are protocol/SAP-adjacent planning
  material, not trial-result tables. They define outcomes, intervention
  thresholds, anticipated sample size/power, planned models,
  missing-data rules, sensitivity/subgroup analyses, and administrative
  monitoring. No workbook, CSV, DOC/DOCX, formula cell, or cached
  workbook value is in this assigned source unit.
- **Candidate work:** none performed. This is a relationship inventory
  only; it does not diagnose, rank, reject, or register quality-control
  candidates.

## Page-complete coverage record

| PDF pages | Content and mapping disposition |
|----|----|
| 1 | Supplement index. Administrative/locator only: identifies original protocol v1.4 (starts p. 2), final protocol v1.8 (starts p. 36), protocol-change summary (p. 78), and original/final SAP (p. 80). No result-relevant quantitative relationship on this page. |
| 2–4 | Original protocol title/date/version and contents. Administrative/locator only; contents identify the planned statistical-analysis section at pp. 25–26. |
| 5–10 | Original-protocol general information, investigators/sites/DMSC, and abbreviations. No result-relevant quantitative relationship beyond administrative identifiers; no applicable result table or statistic. |
| 11–13 | Original-protocol synopsis: objective/outcome, treatment thresholds, outcome time windows, planned sample-size totals, and AE tracking schedule mapped below. |
| 14 | Original-protocol investigator contact continuation. No applicable quantitative result relationship. |
| 15–16 | Background and study objectives: external contextual quantities and the trial’s primary outcome/time window mapped below. |
| 17–18 | Recruitment/randomisation: timing, allocation ratio, stratification, blocks (unspecified size), and two blinded assessors per centre mapped below. |
| 19 | Consent/follow-up timing definitions (24-hour deliberation, 30-day thresholds, 6- and 12-month follow-up) mapped below. |
| 20–22 | Intervention text and the visual intervention-process table. All dose/flow, saturation, duration, ABG timing, and intubation-transition rules mapped below. |
| 23–24 | Outcome definitions, collection frequency, data elements, and ABG time-point-selection rule mapped below. |
| 25–26 | Outcome definitions, anticipated event rates/power, analysis population, missing-data, model/test, adjustment, and subgroup/sensitivity/violation rules mapped below. |
| 27–31 | Safety/event monitoring and administration. The event timing, interim review counts, and quoted pilot desaturation counts are mapped; other drug/accounting, ethics, personnel, archive, and funding text is administrative. |
| 32 | Protocol-change governance only. No applicable quantitative result relationship. |
| 33 | Figure 1 participant timeline and Figure 2 study-progress timeline. Direct PDF page contains only figure labels without extractable numeric outcome/statistical data; no applicable quantitative result relationship. |
| 34–35 | References only. No applicable quantitative result relationship. |
| 36–38 | Final protocol v1.8 title/date/version and contents. Administrative/locator only; it places the later full statistical-analysis material at pp. 62 onward, outside this shard. |
| 39–46 | Final-protocol investigator/site/DMSC information and abbreviations. No applicable quantitative result relationship. |
| 47–49 | Final-protocol synopsis. It repeats the mapped primary objective, intervention thresholds, outcomes, sample totals, and event-monitoring schedule. The matching material is explicitly retained as a final-version occurrence below. |
| 50 | Final-protocol investigator contact continuation. No applicable quantitative result relationship. |
| 51–52 | Final-protocol background/objectives/eligibility opening. It repeats the contextual quantities and primary outcome; pp. 53 onward, including final-protocol intervention/analysis text, is outside this shard. |

## Quantitative and reporting relationship inventory

Provisional IDs are unique to this extraction part and are intended for
coordinator reconciliation to package-wide `N` and `S` identifiers.
“Main-paper key” is a semantic matching key, not a claim that a matching
main-paper result has been confirmed in this mapper pass.

| Provisional ID | Source location(s) | Printed relationship / definition | Main-paper key for matching |
|----|----|----|----|
| DOC002A-N01 | pp. 11–13, 16, 23, 47–49, 52 | **Primary composite outcome:** incidence of 30-day mortality and/or major respiratory complications (pneumonia and ARDS) within 30 days. The intervention is restrictive versus liberal oxygen for the first/eight initial hours after trauma. | `PRIMARY_COMPOSITE_30D_DEATH_OR_MAJOR_RESPIRATORY_COMPLICATION` |
| DOC002A-N02 | pp. 13, 23, 49 | **Secondary outcomes/time points:** mortality at 30 days and 12 months; major respiratory complications within 30 days; HOS/ICU length of stay and days alive outside ICU; ventilation time until day 30, days alive without ventilation, re-intubations within day 30; post-discharge pneumonia within day 30; hypoxaemia episodes during intervention (saturation \<90%); surgical-site infection within day 30; EQ-5D-5L and GOSE at 6 and 12 months. | `SECONDARY_OUTCOMES_30D_6M_12M` |
| DOC002A-N03 | pp. 12, 20–22, 48 | **Restrictive oxygen definition:** for eight hours, lowest oxygen delivery at least 21% to ensure SpO2 target =94%; only participants at FiO2=0.21/no supplemental oxygen can saturate \>94%. For non-intubated participants with saturation \<94%, use the lowest 0–15 L/min flow producing 94%; pre-oxygenation before intubation is usual care. | `INTERVENTION_RESTRICTIVE_OXYGEN_SPO2_94` |
| DOC002A-N04 | pp. 12, 20–22, 48 | **Liberal oxygen definition:** non-intubated: 15 L O2/min by non-rebreather mask in prehospital/trauma bay/transport, reducible to \>=12 L/min in OR/ICU/PACU/ward if arterial saturation \>=98%; intubated: FiO2=1.0 in prehospital/trauma bay/transport, reducible to \>=0.6 in OR/ICU/PACU/ward if arterial saturation \>=98%. | `INTERVENTION_LIBERAL_OXYGEN_FLOW_FIO2` |
| DOC002A-N05 | pp. 17, 20–22, 24 | **Timing and treatment measurements:** enrolment/intervention begins at T0 and continues eight hours; trauma-bay initiation must not be delayed \>90 minutes after hospital arrival. Two ABGs: T1 = hour 1 +/-30 min and T6 = hour 6 +/-2 h after randomisation; if unavailable at T1, draw as soon as possible; if \>2 ABGs occur, enter the ABGs closest to T1/T6. Ventilated oxygen/saturation is automatically tracked; non-ventilated values are recorded hourly. | `INTERVENTION_DURATION_AND_ABG_TIMING` |
| DOC002A-N06 | pp. 13, 25–26, 28, 30, 49 | **Planned sample/count framework:** include up to 1,600; stop at 710 per arm/1,420 total with 30-day follow-up. Inclusion continues while 30-day follow-up is assessed. DMSC review is planned after 355 (~25% of sample-size estimate) and 710 (~50%). Final trial report is after 1,420 participants with complete 30-day, 6-, and 12-month follow-up. | `PLANNED_SAMPLE_SIZE_1420_710_PER_ARM` |
| DOC002A-N07 | p. 15, repeated p. 51 | External/pilot contextual quantities: hyperoxaemia reported as 16–50% in mechanically ventilated patients; cited studies of 152,000 and 14,000 patients, and 2,928 ICU patients with low versus high targets 8 vs 12 kPa for max 90 days; TRAUMOX1 N=41, 24-h intervention; prior medians \[IQR\] 7 \[4–10\] min to randomisation and 51 \[29.0–67.5\] min trauma-to-bay arrival. These are background citations/planning context, not TRAUMOX2 outcomes. | `CONTEXT_TRAUMOX1_AND_BACKGROUND` |
| DOC002A-N08 | pp. 25–26 | **Sample-size assumptions:** TRAUMOX1 primary composite =20% restrictive and 33% liberal. Assumed trauma mortality 6–12%; VAP incidence almost 30%. With 710/arm, protocol states capacity to detect a 33% risk reduction if liberal primary-outcome incidence is 15%, with 80% power and 5% significance. Arithmetic implication of a 33% relative reduction from 15% is approximately 10% in restrictive arm; this latter value is not printed on these pp. 25–26 but appears later in the final SAP outside this shard. | `SAMPLE_SIZE_PRIMARY_OUTCOME_ASSUMPTIONS` |
| DOC002A-N09 | pp. 25–26 | **Analysis population/missingness:** modified intention-to-treat primary analysis excludes post-randomisation participants with no injuries (ISS=0); per-protocol removes \>=1 major protocol violation. If \<5% of required data missing: complete-case. If \>5% missing and not MCAR: inverse-probability weighting; sensitivity analysis will test missing-data assumptions. | `ANALYSIS_POPULATION_AND_MISSING_DATA` |
| DOC002A-N10 | pp. 26 | **Major-protocol-violation operational thresholds:** restrictive arm: supplemental oxygen plus arterial saturation \>=98%, or PaO2 \>=14 kPa. Liberal arm: no supplemental oxygen at any time point, or saturation \<=94% while oxygen is below 15 L/min (non-intubated) or FiO2=1.0 (intubated). | `PER_PROTOCOL_MAJOR_VIOLATIONS` |
| DOC002A-N11 | pp. 27–29, 49 | Safety event measurement schedule: AE/SAE chart review once in first 24 h, then every third day to discharge, maximum 30 days; SAE notification within 24 h; SUSAR fatal/life-threatening report \<=7 d plus follow-up \<=8 d (15 d total); other SUSAR \<=15 d. In TRAUMOX1, seven desaturation episodes (SpO2 \<90%) in restrictive arm, median 87% \[87–89\]; five of seven SpO2 \<89% episodes occurred in two participants. | `SAFETY_EVENTS_AND_HYPOXAEMIA` |
| DOC002A-N12 | pp. 17–18 | Randomisation design: 1:1, variable block sizes (sizes not stated in v1.4), stratified by centre/pre-hospital base and intubation at inclusion; allocation uses concealed envelopes. At least two blinded primary-outcome assessors at each centre. | `RANDOMISATION_AND_BLINDING` |
| DOC002A-N13 | pp. 19, 23–24 | Consent and follow-up timing: 24-h next-of-kin/patient deliberation; participant consent ceases if capacity absent 30 days after trauma; if next of kin cannot be contacted, follow-up continues at day 30, 6 months, 12 months. | `FOLLOW_UP_AND_CONSENT_WINDOWS` |
| DOC002A-N14 | pp. 25–26 | Outcome-defining labels: pneumonia per CDC; ARDS per Berlin definition; traumatic brain injury severe AIS \>=5, moderate AIS 3–4, mild AIS 1–2. | `OUTCOME_AND_SUBGROUP_DEFINITIONS` |

## Statistical-definition inventory

| Provisional ID | Source location(s) | Statistical relationship / planned analysis | Main-paper key for matching |
|----|----|----|----|
| DOC002A-S01 | pp. 25–26 | Power design: 710 per arm; 33% relative risk reduction target; 80% power; two-sidedness is not stated; significance level 5%; anticipated liberal incidence 15%. No formula is displayed. | `POWER_AND_SAMPLE_SIZE_PRIMARY_OUTCOME` |
| DOC002A-S02 | p. 26 | Primary composite comparison: logistic regression, reported as OR with 95% CI; adjusted for age, sex, centre, intubated at randomisation (yes/no), and known pneumonia at admission (under treatment). | `PRIMARY_ANALYSIS_ADJUSTED_OR_95CI` |
| DOC002A-S03 | p. 26 | Secondary outcomes: Fisher exact test/Chi-square test for categorical data; “competing risk survival analyses for continuous data”; 5% significance level. Exact test-selection criteria, survival estimand, and competing event are not specified on these pages. | `SECONDARY_ANALYSES_TESTS_AND_SIGNIFICANCE` |
| DOC002A-S04 | pp. 25–26 | Modified intention-to-treat excludes ISS=0/no-injury post-randomisation participants; per-protocol excludes participants with \>=1 major violation. | `MITT_AND_PER_PROTOCOL_POPULATIONS` |
| DOC002A-S05 | p. 26 | Missing-data decision rule: \<5% complete-case; \>5% and not MCAR, inverse probability weighting; sensitivity analysis for missing-data assumptions. | `MISSING_DATA_DECISION_RULE` |
| DOC002A-S06 | p. 26 | Prespecified subgroups: initially intubated within one hour (yes/no); ICU admission (yes/no); moderate/severe TBI (yes/no); COPD (yes/no); hypoxaemia episodes; prehospital versus in-hospital enrolment. Additional ISS-adjusted analysis. Interaction/modeling and multiplicity approach are not stated here. | `PRESPECIFIED_SUBGROUPS_AND_ISS_ADJUSTMENT` |
| DOC002A-S07 | pp. 30, 49 | Interim/DMSC framework: blinded interim analysis at 355 and 710 participants with 30-day follow-up; original protocol says early-stop criteria to be decided by steering committee. No alpha-spending or formal boundary is supplied in this scope. | `INTERIM_ANALYSIS_DMSC` |
| DOC002A-S08 | pp. 11–13, 23, 47–49 | Primary estimand label is an incidence/rate of a composite endpoint within 30 days, not a rate per person-time. Components are mortality and pneumonia/ARDS; timing and composite construction are explicit. | `PRIMARY_ENDPOINT_MEASURE_LABEL` |

## Version occurrences and cross-source matching notes

- v1.8 pp. 47–52 repeats the v1.4 synopsis/background/objective material
  from pp. 11–16, but adds final administrative registration identifiers
  (EudraCT 2021-000556-19, ClinicalTrials.gov NCT05146700, ethics
  H-21018062) and changes the setting language at p. 52 from “within the
  EU” to “within continental Europe.” These are protocol-version facts,
  not trial-result comparisons.
- The final protocol’s full intervention, analysis, and major-violation
  sections begin after this shard (pp. 53, 62–63 respectively); they
  must be mapped by the distinct pp. 53–103 support shard rather than
  inferred here.
- No table of observed trial results, figure with observed counts, P
  value, confidence interval, effect estimate, sensitivity-result value,
  subgroup-result value, or displayed formula occurs in pp. 1–52. The
  visual intervention table on pp. 21–22 is a protocol operational table
  and its thresholds have been transcribed in DOC002A-N03 through N05.
- There is no matching main-paper key supplied in this support source as
  an explicit identifier. The semantic keys above identify the intended
  matching target for the main mapper/cross-source reviewer; all
  required population, time window, contrast, measure, and adjustment
  labels are retained to prevent a false match.

## Extraction counts and limitations

- PDF pages inspected/mapped: **52/52**.
- Result-relevant numeric/reporting relationships: **14** provisional
  numeric relationships (DOC002A-N01–N14).
- Inferential/statistical definitions: **8** provisional statistical
  relationships (DOC002A-S01–S08).
- Tables/figures with quantitative operational content: **1** two-page
  intervention-process table (pp. 21–22); **0** observed-result tables
  or figures.
- Explicit no-applicable result units: **27 pages** (1–10, 14, 32–35,
  36–46, 50; p. 33’s unquantified timeline figures are included within
  that count); administrative content was opened rather than assumed
  irrelevant.
- Gaps/limitations: no scientific-coverage gap in assigned pp. 1–52. The
  source does not provide final-protocol analysis details until later
  pages, a displayed power formula, exact block sizes in v1.4,
  sidedness, multiplicity adjustment, or an observed main-paper result;
  these are absent from this assigned range, not inferred.

# Support quantitative evidence map — support-002

## Scope and method

Assigned disjoint scope: DOC-002
`joi240147supp1_prod_1738701765.28701.pdf` pp. 53-103; DOC-003
`joi240147supp2_prod_1738701765.29201.pdf` pp. 1-26; DOC-004
`joi240147supp3_prod_1738701765.30201.pdf` pp. 1-3; DOC-005
`joi240147supp4_prod_1738701765.30701.pdf` p. 1 (81 PDF pages total).

I used the corresponding complete page-delimited native-text assets as
location/transcription aids. Direct PDF layout/text was checked for
DOC-003 pp. 13-25, and direct rendered PDF pages were visually checked
for DOC-003 p. 13 (eFigure) and DOC-002 p. 103 (template CONSORT
figure). PDFs are authoritative. No source was changed. This is an
evidence map, not a candidate assessment.

Relationship labels below are local, descriptive mapper keys for later
consolidation; they are not candidate IDs. “Main-paper match key”
identifies the result/definition label that later cross-source mapping
can match, not a claimed discrepancy.

## DOC-002: protocol and SAP (pp. 53-103)

### Protocol intervention, outcome, and operational definitions (pp. 53-75)

| Local key | Direct location | Extracted result-relevant relationship / definition | Main-paper match key |
|----|----|----|----|
| N-SB001 | DOC-002 PDF pp. 53-54 | Randomisation is 1:1, in variable blocks, stratified by centre/pre-hospital base and intubation at inclusion. Intervention starts at T0, continues 8 hours, and trauma-bay initiation must not be delayed \>90 minutes after hospital arrival. | Randomisation / allocation; intervention duration |
| N-SB002 | DOC-002 PDF pp. 56-59 | Restrictive strategy: lowest oxygen dosage \>=21% to target SpO2 =94%; FiO2=0.21 (or lowest possible) is required to allow saturation \>94%. Liberal strategy: non-intubated 15 L O2/min initially, reducible to \>=12 L/min at saturation \>=98%; intubated FiO2=1.0 initially, reducible to \>=0.6 at saturation \>=98%. Figure scheme gives the same thresholds. Two ABGs: T1 = 1 hour +/-30 minutes and T6 = 6 hours +/-2 hours after randomisation; hourly oxygen/saturation registration. | Oxygen intervention characteristics; Table 2 intervention data |
| N-SB003 | DOC-002 PDF pp. 59-61 | Primary outcome: incidence of 30-day mortality and/or major respiratory complications (pneumonia and ARDS) within 30 days. Secondary outcomes include 30-day and 12-month mortality; pneumonia/ARDS within 30 days; ventilation time, ventilator-free days and re-intubations within 30 days; post-discharge pneumonia, hypoxaemia (SpO2 \<90%), surgical-site infection within 30 days; EQ-5D-5L and GOSE at 6 and 12 months. | Primary/key secondary outcome; exploratory outcomes |
| S-SB001 | DOC-002 PDF p. 62 | Planned sample size: 710/arm; detect 33% risk reduction at 80% power and 5% significance if liberal primary-outcome incidence is 15%; goal 1420 evaluable participants and maximum 1600 while 30-day follow-up is evaluated. Primary analysis modified ITT excluding ISS=0/no-injury participants; logistic regression OR (95% CI), adjusted for age, sex, centre, intubation at randomisation, and pneumonia under treatment on admission. Categorical secondary outcomes: Fisher exact/Chi-square; continuous: competing-risk survival analyses; 5% significance. Missingness: \<5% complete case; \>5% and not MCAR: inverse-probability weighting plus sensitivity analysis. | Analysis population; primary model; sample-size basis |
| S-SB002 | DOC-002 PDF pp. 62-63 | Per-protocol excludes \>=1 major oxygen protocol violation. Restrictive: non-intubated supplemental O2 \>=3 L/min AND SpO2 \>=98% at two consecutive hourly values; intubated FiO2 \>0.4 AND SpO2 \>=98% at two consecutive hourly values. Liberal: non-intubated O2 \<3 L/min for two consecutive hourly values; intubated FiO2 \<0.4 for two consecutive hourly values. Prespecified subgroups: initially intubated \<=1 hour, ICU admission, moderate/severe TBI, COPD, hypoxaemia, prehospital vs in-hospital; ISS-adjusted analysis. | Table 2 major violations; per-protocol and subgroup analyses |
| N-SB004 | DOC-002 PDF pp. 64-65 | AE/SAE definitions: AE includes any untoward occurrence; SAE includes admission/prolonged admission, persistent/significant disability, congenital anomaly/birth defect, life-threatening event, or death. Only first atelectasis (radiologist assessed) or airway-mucosa irritability during admission is recorded as AE; all SAEs recorded. Monitoring once in first 24 hours then every third day, maximum 30 days. | eTable 9 adverse events |
| N-SB005 | DOC-002 PDF pp. 66-67 | Protocol reports TRAUMOX1 restrictive-arm desaturation: 7 episodes with SpO2 \<90%, median 87% (IQR 87-89); five of seven \<89% episodes occurred in two participants. Planned DMSC meetings after 355 (~25%) and 710 (~50%) participants with 30-day follow-up. | Hypoxaemic episodes; DMSC/sample size |
| S-SB003 | DOC-002 PDF pp. 69-70 | DMSC raw outcome coding: 30-day death, pneumonia, and ARDS each coded 0=no, 1=yes, 999=missing; blank=not entered/still pending. DMSC analyses 2x2 tables stratified by blinded group. Suggested stopping guidance: mortality relative risk whose lower 95% CI \>2 (irrespective of numerator group); no futility stopping before 1420 complete 30-day follow-ups. | Outcome coding; interim-analysis/stopping definition |
| N-SB006 | DOC-002 PDF p. 74 | Funding quantity: 4 years; 6,326,084 DKK grant; participating centre receives EUR150 per completely documented participant after 30 days; additional personal grant 350,000 DKK. Administrative/funding quantities, not trial results. | No main-paper results match expected |

### SAP (pp. 80-103)

| Local key | Direct location | Extracted result-relevant relationship / statistical definition | Main-paper match key |
|----|----|----|----|
| S-SB004 | DOC-002 PDF pp. 82, 85 | SAP fixes block sizes 4, 6, 8; 1:1 allocation and centre/intubation strata. Sample size is 1420 (710/arm), including stated 3.5% dropout; planned 33% relative reduction from 15% liberal to 10% restrictive, absolute difference 5 percentage points, 80% power, 5% level. DMSC interim points: 355 (25%) and 710 (50%); no futility stopping before 1420. | Randomisation; sample-size calculation; interim analysis |
| S-SB005 | DOC-002 PDF pp. 85-86 | Two-sided 5% tests and 95% CIs. Exploratory-outcome P values and 95% CIs assessed under Benjamini-Hochberg FDR control at 5%. mITT: all randomised except secondary exclusions after diagnostics expected to discharge within 24h because few/no injuries; per protocol=mITT minus \>=1 major violation. | Statistical methods/footnotes; mITT and per-protocol denominators |
| S-SB006 | DOC-002 PDF pp. 88-89 | Primary and key secondary outcomes: logistic regression OR with 95% CI adjusted for stratification variables; additional primary model adjusts strata, age, sex, ISS, and first available post-trauma GCS. GEE uses including base as clustering variable. Differential attrition is adjusted by inverse probability of being observed; probability model uses baseline characteristics/allocation and variance is adjusted in GEE. Exploratory outcomes use logistic or linear regression according to outcome type, same covariate adjustment, Benjamini-Hochberg evaluation. | eTable 4/5/6 adjusted effects; eTable 7 subgroups |
| S-SB007 | DOC-002 PDF pp. 88-91 | Subgroups: initially intubated \<=1h, ICU admission, moderate/severe TBI (AIS \>=3), known lung disease, hypoxaemia during intervention (SpO2 \<90%), prehospital vs in-hospital, ISS \>15. For withdrawn consent, event within available period is retained; otherwise time-dependent outcome is missing and IPW is used. SAS 9.4 stated. | eTable 7; missing-data method |
| N-SB007 | DOC-002 PDF pp. 97-102 | SAP Tables 1-4 define the data fields and units: baseline age, sex, cm, kg, smoking/comorbidities, mechanism and injury scores; vital signs mmHg/bpm/min/SpO2/Celsius/GCS 3-15; during 8 hours, hourly median SpO2, oxygen flow L/min, FiO2, ABGs (PaO2 kPa or mmHg; Hb mmol/L; lactate mmol/L), and violation/deviation flags; primary/key outcomes as 30-day yes/no; exploratory outcomes include ventilator hours and days, ICU/HOS LOS, infections and hypoxaemia. Table 3 defines primary composite and blinded assessment; pneumonia is CDC PNEU/VAP and ARDS Berlin mild/moderate/severe. Table 4 excludes elective-surgery ventilation, uses only primary admission for HOS LOS, and defines transfer/discharge handling. Supplemental Table 1 defines AE/SAE categories, maximum 30-day first AE, and SAE classification as SUSAR/SAR/SAE. | Table 1/2 definitions; eTables 3-9 labels and units |
| N-SB008 | DOC-002 PDF p. 103 | SAP Figure 1 is a placeholder/template CONSORT flow diagram: all participant numbers are `XXXX`/`XXX`/`XX`, not observed results. It lists assessment/exclusion, total randomised/included, allocations, 30-day exclusions, and primary analysis branches. | Main-paper CONSORT flow; no numerical comparator available |

### Explicit no-applicable units — DOC-002

Pages 53-61, 63-75, and 78-103 were inspected as mapped above where they
contain a quantitative threshold, definition, table, figure, SAP method,
or planned/observed value. The remaining parts contain no additional
result-relevant relationship beyond the mapped context: pp. 54-56
consent/blinding prose; pp. 60-61 data-management prose; pp. 63-65
drug/safety administration beyond definitions; pp. 71-73 DMSC
membership/signatures/change-log beyond mapped coding; pp. 74-75
archiving/funding/timeline figure without data; pp. 76-77 and 94-96
references; pp. 78-79 protocol-change log (only quantitative change
mapped: restrictive intubated threshold changed from FiO2 \>=0.4 to
\>0.4); p. 80-81 SAP title/signature pages; pp. 83-84 background/design
prose; pp. 92-93 dissemination/status (status: 913 enrolled as of 11
February 2023, expected final inclusion early 2024; planning/status, no
analyzed result).

## DOC-003: results supplement (pp. 1-26)

### Methods, definitions, and eFigure (pp. 1-13)

| Local key | Direct location | Extracted relationship / definition | Main-paper match key |
|----|----|----|----|
| N-SB009 | DOC-003 PDF pp. 7-12 | Hourly data: SpO2, oxygen-delivery type, flow L/min, FiO2; missing sheet values replaced by approximated hourly median from medical record. High-flow nasal cannula coded as non-rebreather mask. Of extra ABGs, value closest to 1h +/-30min and 6h +/-2h is used. Primary composite is death and/or pneumonia/ARDS within 30 days; death/major respiratory complications are individual key secondary outcomes. | Intervention data; primary/key secondary definitions |
| N-SB010 | DOC-003 PDF pp. 8-10 | PNEU/VAP definition: VAP requires mechanical ventilation \>2 calendar days (placement day=day 1) and in place on event day/day before; fever \>38C or \>100.4F, WBC \<=4000 or \>=12,000/mm3, or altered mental status for age \>=70 plus imaging and respiratory criteria. Berlin ARDS: onset \<=1 week; bilateral opacities; noncardiac edema; mild PaO2/FiO2 \>200 to \<=300 with PEEP/CPAP \>=5 cmH2O, moderate \>100 to \<=200 with PEEP \>=5, severe \<=100 with PEEP \>=5; altitude \>1000m correction = PaO2/FiO2 x (barometric pressure/760). | Outcome definition/scale |
| N-SB011 | DOC-003 PDF pp. 9-12 | Exploratory definitions: hypoxaemia is count of hourly SpO2 \<90%; ventilator hours are commenced hours (1h15m=2) of positive-pressure ventilation, excluding NIV/HFNC/CPAP and elective surgery ventilation; ventilator-free days and ICU-outside days use commenced days (1h ventilation/ICU=1 day); 25h ICU/HOS stay=2 days. AE only first radiologist-assessed atelectasis or recorded airway irritation, through discharge/max 30d. Major-violation and protocol-deviation definitions as N-SB002/S-SB002. Missing outcomes use IPW; primary IPW logistic model uses allocation, dominant injury type, oxygen supply, psychiatric comorbidity, and Danish personal-ID status; variance adjusted in GEE. | eTables 3, 5, 6, 9; missing-data analysis |
| N-SB012 | DOC-003 PDF p. 13 | eFigure (direct visual check): median (IQR) overall profiles are liberal SpO2 100 (99-100) vs restrictive 97 (96-99); liberal oxygen flow 12 (12-15) L/min vs restrictive 0 (0-1) L/min; liberal FiO2 0.60 (0.60-0.80) vs restrictive 0.28 (0.21-0.36). Panel A plots Pre and hours 1-8; panels B/C hours 1-8. | Figure: oxygen intervention characteristics |

### eTables 1-3 (pp. 14-16)

| Local key | Direct location | Extracted displayed values | Main-paper match key |
|----|----|----|----|
| N-SB013 | DOC-003 PDF p. 14 | eTable 1, groups restrictive N=750/liberal N=758. Enrollment location counts/percentages: Copenhagen CCU1-2 62/750 (8.3)/68/758 (9.0); CCU3 25 (3.3)/21 (2.8); CCU4 25 (3.3)/26 (3.4); CCU5 34 (4.5)/36 (4.7); Ringsted 40 (5.3)/37 (4.9); Billund 21 (2.8)/23 (3.0); Skive 17 (2.3)/18 (2.4); Saltum 2 (0.3)/2 (0.3); Odense CCU 38 (5.1)/39 (5.1); Aarhus CCU 13 (1.7)/13 (1.7); Randers 1 (0.1)/0 (0.0); Lifeliner 2 5 (0.7)/3 (0.4); REGA3 19 (2.5)/16 (2.1); REGA10 3 (0.4)/3 (0.4); REGA14 3 (0.4)/2 (0.3); in-hospital Rigshospitalet 150 (20.0)/160 (21.1), Odense 118 (15.7)/117 (15.4), Aarhus 62 (8.3)/58 (7.7), Erasmus 87 (11.6)/90 (11.9), Bern 25 (3.3)/26 (3.4). Receiving-centre totals (N=1508): Rigshospitalet 335 (44.4)/348 (45.7); Odense 173 (22.9)/177 (23.2); Aarhus 100 (13.3)/93 (12.2); Erasmus 92 (12.2)/93 (12.2); Bern 50 (7.2)/47 (6.7). | Baseline/enrollment site characteristics |
| N-SB014 | DOC-003 PDF p. 15 | eTable 2: BMI kg/m2 median (IQR) 25.0 (22.5-28.1) n=628 / 25.0 (22.8-27.8) n=615. Injury-mechanism counts/denominators/percentages (R/L): motor vehicle 147/742 (19.8)/151/756 (20.0); motorcycle 74 (10.0)/70 (9.3); bicycle 109 (14.7)/108 (14.3); pedestrian 53 (7.1)/50 (6.6); other traffic 14 (1.9)/19 (2.5); firearm 8/724 (1.1)/6/756 (0.8); stabbing 69/742 (9.3)/68/756 (9.0); blunt 51 (6.9)/58 (7.7); fall 0-2m 82 (11.1)/69 (9.1); 2-4m 66 (8.9)/68 (9.0); \>4m 58 (7.8)/57 (7.5); blast 3 (0.4)/4 (0.5); other 8 (1.1)/28 (3.7). Transport: ground 583/747 (78.0)/585/743 (78.7); helicopter 140 (18.7)/141 (19.0); combined 14 (1.9)/9 (1.2); private 1 (0.1)/3 (0.4); walk-in 9 (1.2)/4 (5.3); other 0 (0.0)/1 (0.1). Prior oxygen 333/713 (46.7)/351/718 (48.9); highest SpO2 100 (97-100) n=265 / 99 (97-100) n=285; temperature C 36.5 (35.9-37.0) n=479 / 36.5 (35.9-36.9) n=484. Resuscitation-room surgery: neuro 3/744 (0.4)/1/747 (0.1); cardiothoracic 10 (1.3)/9 (1.2); abdominal 0 (0.0)/4 (0.5); orthopaedic 2 (0.3)/1 (0.1); vascular 1 (0.1)/0 (1.1); other 1 (0.1)/1 (0.1). Continuous values are median (IQR). | Additional baseline characteristics |
| N-SB015 | DOC-003 PDF p. 16 | eTable 3: trauma-to-randomisation min, N=1268: 54 (35-79) n=633 / 52 (33-78) n=635. Oxygen category R/L, n=739/735: none 200 (27.1)/13 (1.8); nasal cannula 171 (23.1)/45 (6.1); non-rebreather 18 (2.4)/340 (46.2); intubated any point 350 (47.4)/337 (45.9). Hb g/dL at 1h: 12.9 (11.4-14.0) n=602 / 12.7 (11.3-14.0) n=603; 6h: 12.5 (10.8-13.7) n=482 / 12.4 (10.6-13.9) n=487. Lactate mmol/L at 1h: 1.5 (0.9-2.5) n=585 /1.4 (0.9-2.4) n=590; 6h: 1.4 (0.9-2.2) n=472 /1.4 (0.9-2.1) n=479. Major violation 50/742 (6.7)/102/744 (13.7); deviation 40/741 (5.4)/17/738 (2.3). Footnote: 8 hourly H1-H8 points; categories sum to 100%, tie assigned to non-rebreather; ABG times as above. | Main-paper Table 2; oxygen intervention characteristics |

### eTables 4-11 (pp. 17-25)

| Local key | Direct location | Extracted displayed values | Main-paper match key |
|----|----|----|----|
| S-SB008 | DOC-003 PDF p. 17 | eTable 4. Primary: 118/733 (16.1) vs 121/724 (16.7); OR 1.01 (0.75-1.37), P=.94; adjusted OR 0.98 (0.68-1.41), P=.92; adjusted+smoking 1.05 (0.73-1.49), P=.80. Death: 63/733 (8.6) vs 53/724 (7.3); OR 1.28 (0.85-1.92), .23; adjusted 1.37 (0.80-2.38), .25; +smoking 1.37 (0.80-2.33), .26. Major respiratory complications: 65/733 (8.9) vs 78/724 (10.8); OR .84 (.59-1.19), .33; adjusted .84 (.57-1.23), .38; +smoking .90 (.61-1.32), .58. Death/complications assessed within 30d; smoking is active smoking. | Main-paper primary/key secondary outcome table |
| S-SB009 | DOC-003 PDF p. 18 | eTable 5 categorical exploratory outcomes, R vs L, unadjusted/adjusted/adjusted+smoking OR (95% CI), P: hypoxaemia 44/737 (6.0) vs 28/737 (3.8): 1.67 (1.02-2.70), .04; 1.72 (1.04-2.78), .03; 1.69 (1.04-2.78), .04. ICU readmission 17/368 (4.6)/18/352 (5.1): .59 (.26-1.37), .22; .60 (.25-1.43), .25; .57 (.25-1.32), .19. Sepsis 19/736 (2.6)/31/727 (4.3): .55 (.30-1.02), .06; .53 (.29-1.00), .05; .52 (.27-1.00), .05. Surgical-site infection 23/736 (3.1)/32/724 (4.4): .50 (.25-.99), .05; .49 (.26-.93), .03; .51 (.27-.96), .04. Post-discharge pneumonia 27/640 (4.2)/24/620 (3.9): 1.06 (.60-1.85), .86; 1.04 (.59-1.85), .89; 1.03 (.57-1.85), .93. Brain injury 290/738 (39.3)/275/732 (37.6): 1.11 (.88-1.41), .35; 1.05 (.82-1.35), .68; 1.04 (.81-1.33), .74. MI 0/738 (0.0)/1/730 (0.1), no effect/P. Cerebral ischaemia 16/738 (2.2)/10/730 (1.4): 1.56 (.68-3.57), .30; 1.45 (.63-3.45), .38; 1.47 (.64-3.45), .36. ICU admission 374/738 (50.7)/359/736 (48.8): 1.16 (.90-1.49), .24; 1.01 (.76-1.33), .95; 1.01 (.76-1.33), .95. Footnote: hypoxaemia is any hourly SpO2 \<90%; post-discharge denominator limited to discharged \<=30d. | Exploratory outcome table |
| S-SB010 | DOC-003 PDF p. 19 | eTable 6 continuous exploratory outcomes, R/L medians (IQR), followed by mean difference (95% CI), P; adjusted; adjusted+smoking: surgery minutes 114 (64-166) n165 /113 (68-149) n161: 10.3 (-8.8-29.3), .29; 12.6 (-7.4-32.6), .22; 15.4 (-4.3-35.0), .13. Ventilation hours 0 (0-14) n735 /0 (0-12) n725: 4.8 (-7.6-17.2), .45; 3.3 (-8.7-15.2), .59; 3.7 (-8.1-15.6), .54. Ventilator-free days 30 (29-30) n735 /30 (29-30) n723: -.6 (-1.4-.2), .16; -.4 (-1.1-.3), .27; -.5 (-1.2-.2), .20. ICU LOS days 2 (1-9) n368 /2 (1-7) n357: 1.1 (-.2-2.5), .10; 1.0 (-.4-2.3), .17; 1.0 (-.4-2.5), .16. Days alive outside ICU 29 (26-30) n736 /30 (27-30) n724: -.8 (-1.7-.1), .09; -.5 (-1.3-.2), .17; -.6 (-1.3-.2), .12. Hospital LOS days 7 (3-15) n736 /7 (3-15) n728: -.7 (-2.3-.9), .41; -1.0 (-2.3-.6), .23; -1.0 (-2.5-.6), .23. Group columns are medians/IQRs. | Exploratory continuous outcomes |
| S-SB011 | DOC-003 PDF pp. 20-21 | eTable 7 primary-outcome subgroup event rates and OR/adjusted OR (95% CI): all 118/733 (16.1)/121/724 (16.7), 1.01 (.75-1.37)/.98 (.68-1.39); not intubated 56/558 (10.0)/50/543 (9.2), 1.12 (.75-1.67)/1.16 (.73-1.85); intubated 62/175 (35.4)/71/181 (39.2), .90 (.57-1.41)/.76 (.45-1.30); no ICU 42/458 (9.2)/50/481 (10.4), .98 (.64-1.49)/.89 (.56-1.43); ICU 74/271 (27.3)/68/238 (28.6), .96 (.63-1.49)/.98 (.58-1.67); AIS\<3 45/500 (9.0)/48/473 (9.2), 1.06 (.68-1.64)/1.11 (.68-1.85); AIS\>=3 73/233 (31.3)/73/202 (36.1), .81 (.53-1.25)/.83 (.51-1.37); no lung disease 97/667 (14.5)/105/643 (16.3), .88 (.65-1.22)/.95 (.65-1.39); lung disease 19/59 (32.2)/14/69 (20.2), 1.85 (.73-4.55)/1.06 (.40-2.86); prehospital 48/303 (15.8)/54/296 (18.2), .81 (.51-1.28)/.95 (.55-1.64); in-hospital 70/430 (16.3)/67/428 (15.7), 1.19 (.81-1.79)/.98 (.63-1.52); ISS\<=15 22/380 (5.8)/19/389 (4.9), 1.33 (.69-2.56)/1.14 (.56-2.33); ISS\>15 95/352 (27.0)/100/329 (30.4), .86 (.60-1.23)/.93 (.62-1.40). | Subgroup forest/table |
| S-SB012 | DOC-003 PDF p. 22 | eTable 8 per-protocol, group N=700/656. Primary 104/683 (15.2)/105/627 (16.7): OR .98 (.71-1.35), .91; adjusted .97 (.67-1.41), .87; +smoking 1.04 (.71-1.52), .83. Death 54/683 (7.9)/44/627 (7.0): 1.27 (.82-2.00), .29; 1.25 (.70-2.22), .45; 1.22 (.69-2.17), .49. Major respiratory complications 58/685 (8.5)/69/629 (11.0): .78 (.54-1.14), .20; .82 (.54-1.23), .34; .89 (.59-1.33), .58. | Per-protocol outcome table |
| N-SB016 | DOC-003 PDF p. 23 | eTable 9, groups N=750/758: AE atelectasis 207/750 (27.6)/263/758 (34.7), airway-mucosa irritability 16/750 (2.1)/20/758 (2.6). SAE death 63/750 (8.4)/53/758 (7.0), life-threatening 8/750 (1.1)/13/758 (1.7), involved/prolonged LOS 29/750 (3.9)/37/758 (4.9), disability/incapacity 0/750 (0.0)/0/758 (0.0), congenital anomaly/birth defect 0/750 (0.0)/1/758 (0.1). Footnote explains different denominators from outcome tables (observed until possible consent withdrawal), and no SAR or SUSAR. | Adverse-event table |
| N-SB017 | DOC-003 PDF p. 24 | eTable 10: post-randomisation exclusion N=130: 55/750 (45) restrictive and 67/758 (55) liberal. Secondary exclusion N=341: 174/750 (51) and 165/758 (49); two patients have missing randomised-oxygen data, explaining N=341 versus displayed cell counts. | Main-paper Figure 1 post-randomisation exclusions |
| S-SB013 | DOC-003 PDF p. 25 | eTable 11 sensitivity scenarios. Missing not event: primary 118/750 (15.7)/121/758 (16.0), OR .99 (.74-1.33), .96; death 63/750 (8.4)/53/758 (7.0), 1.28 (.86-1.92), .22; respiratory 65/750 (8.7)/78/758 (10.3), .82 (.57-1.16), .26. Missing as event: primary 135//750 (18.0)/155/758 (20.4), .85 (.65-1.11), .24; death 80/750 (10.7)/87/758 (11.4), .93 (.68-1.30), .70; respiratory 82/750 (10.9)/112/758 (14.8), .70 (.52-.95), .02. The primary restrictive cell is printed `135//750`, including the double slash. | Missing-data best/worst case sensitivity |

### Explicit no-applicable units — DOC-003

Pages 1-6 contain supplement title, table of contents, investigator/DMSC
and site lists; no result-relevant quantitative relationship other than
the p. 6 site eligibility threshold of approximately 400 trauma-team
activations/year (administrative). Page 26 is references only. All
remaining pp. 7-25 contain result-relevant methods, figure, table, or
footnote evidence and are mapped above.

## DOC-004 and DOC-005

| Source / page scope | Record |
|----|----|
| DOC-004 PDF pp. 1-3 | No applicable result-relevant quantitative content. This is a nonauthor-collaborator roster; the `1 of 3`, `2 of 3`, and `3 of 3` are document pagination, not study results. |
| DOC-005 PDF p. 1 | No analyzed result. Data-sharing statement: deidentified participant data/data dictionary are stated available after long-term 6- and 12-month follow-up publication; availability beginning 03-01-2026 with no end date; all post-hoc analyses; access requires reasonable request/ethics approval. This is administrative rather than a reported outcome. |

## Coverage completion and extraction notes

- DOC-002 mapped pages: 53-103 (51/51). Pages 76-77 and 94-96 are
  references; DOC-002 p. 103 is an explicitly unpopulated template,
  direct visual confirmation completed.
- DOC-003 mapped pages: 1-26 (26/26). The eFigure values were
  transcribed from direct visual inspection; the associated axes are
  SpO2 (%), oxygen flow (L/min), and FiO2, with medians and IQRs.
- DOC-004 mapped pages: 1-3 (3/3), all no-applicable.
- DOC-005 mapped pages: 1/1, administrative no analyzed result.
- Total mapped stable units in this shard: 81/81. No coverage gaps. No
  workbook, spreadsheet, CSV, DOC/DOCX, formula cells, or cached
  workbook/displayed values were supplied in this assigned scope.
