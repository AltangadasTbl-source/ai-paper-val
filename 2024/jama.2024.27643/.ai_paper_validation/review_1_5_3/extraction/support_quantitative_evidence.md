# Canonical Support Quantitative Evidence Map

## Scope, authority, and complete-coverage summary

- **Canonical assigned scope:** the complete disjoint support mapping union from `coverage_manifest.md`: DOC-002 PDF pp. 1-229; DOC-003 PDF pp. 1-130; DOC-004 PDF pp. 1-26; DOC-005 PDF pp. 1-6; and DOC-006 PDF p. 1 (**392/392 physical PDF pages mapped**).
- **Direct-source/provenance partition:** DOC-002 (229 pages), DOC-003 (130 pages), DOC-005 (6 pages), and DOC-006 (1 page) were fresh-required and freshly direct-mapped. DOC-004 (26 pages) was reusable-backed by source-matched native page text, with retained renders used for table/figure confirmation; its component map records this provenance. No Office, workbook, CSV, formula cell, or cached/displayed workbook value exists in the supplied support scope.
- **Source and page order:** the retained component maps below are arranged DOC-002 pp. 1-76, 77-152, 153-229; DOC-003 pp. 1-65, 66-130; then DOC-004 pp. 1-26, DOC-005 pp. 1-6, and DOC-006 p. 1. The original component text is retained losslessly, including direct-source locations, statistical definitions, tables, figures, sensitivity/subgroup material, units, labels, matching keys, no-applicable records, and extraction limitations.
- **Coverage result:** DOC-002 229/229; DOC-003 130/130; DOC-004 26/26; DOC-005 6/6; DOC-006 1/1. These pages partition all assigned support units. No scientific-coverage gap is reported by any component.
- **Counts retained from component maps:** six disjoint component maps; DOC-002 pp. 77-152 reports 11 quantitative/definition and 4 inferential/statistical local records; DOC-002 pp. 153-229 reports 12 protocol/population/analysis-rule, 11 table/figure/displayed-result/instrument, and 12 administrative/operational records; DOC-004 maps eTables 1-5 and one eFigure. Other components use detailed page/table/relationship inventories rather than a compatible numeric record scheme, so no artificial deduplicated relationship total is asserted.
- **No-applicable coverage:** every component expressly records its no-applicable pages. DOC-005 pp. 1-6 and DOC-006 p. 1 have no result-relevant support content, while their administrative content is retained. DOC-004 pp. 1 and 26 are likewise recorded as administrative/end matter.
- **Boundary:** evidence mapping only; this artifact does not diagnose, register, rank, or adjudicate any candidate.

---

## DOC-002 — HEALEY ALS Platform Trial Protocol (fresh direct-source mapping)

### PDF pp. 1-76

# DOC-002 Support Quantitative Evidence Map — PDF Pages 1-76

## Scope and method

- **Source authority:** `joi240158supp1_prod_1742927563.7611.pdf`, HEALEY ALS Platform Trial Protocol, Version 5.0, protocol date 2022-12-15. This is a supplied protocol/administrative source, not a results publication.
- **Assigned, complete scope:** physical PDF pages 1-76 of 229. The printed protocol page numbers run from 1 of 83 through 76 of 83; source locations below always use physical PDF pages.
- **Direct fresh extraction:** `pdftotext` native and `pdftotext -layout`, each for PDF pp. 1-76, saved in `preprocessing/support-001/doc002_p001_p076_native.txt` and `preprocessing/support-001/doc002_p001_p076_layout.txt`.
- **Targeted direct visual confirmation:** rendered source pages 14, 15, 17, 18, 25, and 26 saved under `preprocessing/support-001/`. Figure 1 and Figure 2 values below were visually confirmed against the PDF source. Native/layout text was readable for all 76 pages; CPU OCR was not needed.
- **Boundary:** This map records definitions, proposed design parameters, endpoints, assessment rules, figures, tables, labels, units, and statistical plans. It does not diagnose a consistency candidate or draw conclusions about implementation or outcomes. No actual trial-result table is present in this assigned protocol segment.

## Quantitative/statistical relationship inventory for this shard

| Local relationship key | Type | Direct source location | Evidence mapped |
|---|---|---|---|
| DOC002-N01 | protocol identity | PDF p. 1 | IND 144126; protocol date 12/15/2022; Version 5.0. |
| DOC002-N02 | allocation/design | pp. 11-12, 17-18, 20, 27, 34, 42, 60 | Two-stage allocation: equal assignment among available regimens, then active:placebo 3:1 within a regimen; participants/site staff blinded within regimen but not to regimen. |
| DOC002-N03 | planned size/arms | pp. 11-12, 17-18, 60, 63, 65 | Example/recommended regimen size 160; Figure 1/2 depict approximately 120 active and 40 placebo. Actual size is RSA-specific. |
| DOC002-S01 | endpoint/model | pp. 12, 25-27, 51-52, 60-65 | Default primary endpoint is change through Week 24 in ALSFRS-R total score and survival; Bayesian shared-parameter function/survival primary model and DRR treatment effect are specified. |
| DOC002-N04 | timing/visit windows | pp. 14-18, 40-46, 61 | Screening -42 to -1 days; baseline Day 0; Weeks 2, 4, 8, 12, 16, 20, 24 with stated day windows; primary data time points 0, 4, 8, 12, 16, 20, 24 weeks. |
| DOC002-N05 | eligibility thresholds | pp. 29-31 | Age >=18 years, weakness onset <=36 months, VC >=50% predicted; stable riluzole >=30 days; edaravone at least one typically 14-day cycle; Relyvrio/Albrioza >=30 days; specified safety thresholds. |
| DOC002-N06 | interim/adaptation rule | pp. 27, 60-65 | Interim begins with >=40 randomized participants having opportunity for >=24 weeks; every 12 weeks; default non-binding futility only. Success and futility probability thresholds/operating values mapped. |
| DOC002-S02 | shared-control population | pp. 61-63 | ITT active participants plus within-regimen, concurrent shared, and non-concurrent shared controls; concurrent window 6 months = 180 days; repeat-participant handling. |
| DOC002-S03 | endpoint-scale definition | pp. 51-52, 73-75 | ALSFRS-R contains 12 ordinal activities rated 0-4, total 0-48, higher is better; item labels and response anchors mapped. |
| DOC002-S04 | SVC measurement rule | p. 52 | Upright SVC; 3 trials required; up to 5 if variability of highest vs second highest is >=10% in first 3; record best 3; highest VC for eligibility; >=3 measurable post-screening trials; predicted values use Quanjer GLI equations. |
| DOC002-S05 | safety summary definitions | pp. 55-59, 64-65 | Safety set is participants initiating treatment; summaries include counts and proportions by MedDRA category, continuous values/change from baseline, Kaplan-Meier time-to-death/death-equivalent, CTCAE classifications. |

## Page-level source map

### PDF pp. 1-10

- **p. 1 — applicable administrative identity.** HEALEY ALS Platform Trial; regulatory sponsor Merit Cudkowicz; IND 144126; funding sponsor Healey Center for ALS at Mass General; protocol date 12/15/2022; Version 5.0.
- **p. 2 — table of contents, no standalone result-relevant relationship.** Identifies sections with quantitative content later in this source: objectives/endpoints p. 25, population pp. 29-30, randomization p. 33, assessments pp. 49-53, statistics pp. 60-65.
- **p. 3 — table of contents, no standalone result-relevant relationship.** Identifies schedule timing through Week 24, statistics sections including sample-size justification, and appendices.
- **p. 4 — table of contents, no standalone result-relevant relationship.** Identifies endpoint, safety, and statistical section locations; no values beyond page-location metadata.
- **p. 5 — table of contents, no standalone result-relevant relationship.** Identifies appendices: El Escorial p. 71, ALSFRS-R p. 73, C-SSRS baseline p. 76.
- **p. 6 — no applicable result-relevant content.** Protocol approval signature page.
- **p. 7 — no applicable result-relevant content.** Compliance statement.
- **p. 8 — no applicable result-relevant content.** Site-investigator signature template.
- **p. 9 — applicable label definitions.** Defines ALSFRS-R, ATE, C-SSRS, FVC, HHD, ITT, N (typically participants), and other abbreviations used by later quantitative relationships.
- **p. 10 — applicable label definitions.** Defines PAV, RSA, SVC, VC, and WOCBP, among other abbreviations.

### PDF pp. 11-18 — protocol summary, Schedule of Activities, and figures

- **p. 11 — applicable design/denominator definition.** A perpetual platform uses one Master Protocol; each investigational product has an RSA that gives product-specific population, sample size, arms, dose, and assessment detail. Eligible consented participants are assigned with equal probability among active regimens. Enrollment stops in a regimen upon predefined futility/success (if applicable) or target randomized number. Each regimen's size depends on anticipated effect size, variability, and arms.
- **p. 12 — applicable primary/secondary endpoint and allocation definitions.** Within a regimen, active:matching-placebo randomization is 3:1. Up to approximately 80 US centers. Placebo-controlled treatment maximum is 24 weeks; ATE duration is RSA-specific. Default primary endpoint: change from baseline through Week 24 in ALSFRS-R total score and survival. Secondary endpoints: change through Week 24 in SVC, isometric HHD/grip strength, and survival.
- **p. 13 — applicable endpoint labels.** Safety endpoints are treatment-emergent AEs/SAEs, laboratory and ECG changes/abnormalities, and treatment-emergent suicidal ideation/behavior. Exploratory endpoints are changes in biofluid biomarkers and patient-reported outcomes.
- **pp. 14-15 — Table: Schedule of Activities (applicable table).** Minimum schedule: Master Protocol screening clinic -42 to -1 days; RSA screening (RSA-defined); Baseline Day 0; Week 2 phone Day 14 +/-3; Week 4 clinic Day 28 +/-7; Week 8 clinic Day 56 +/-7; Week 12 phone Day 84 +/-3; Week 16 clinic Day 112 +/-7; Week 20 phone Day 140 +/-3; Week 24 clinic Day 168 +/-7; follow-up safety call RSA-defined. ALSFRS-R is scheduled at screening, baseline, Weeks 4, 8, 12, 16, 20, 24. SVC is screening, baseline, Weeks 8, 16, 24. Muscle strength is baseline, Weeks 8, 16, 24. PROs are baseline, Weeks 8, 16, 24. C-SSRS, blood/urine biomarkers, optional DNA, CSF, dosing, compliance, exit questionnaire, and vital-status determination have the displayed schedule. Footnotes: screening must occur 42 days to 1 day before baseline; height is cm and screening-only; vital status at placebo-controlled end and at LPLV; remote restrictions and other collection exceptions are specified.
- **p. 16 — applicable Schedule footnotes.** FVC may substitute only for Master Protocol screening eligibility under restrictions. Visits may be phone/telemedicine under stated conditions. Drug-accountability check-in occurs at phone visits but accountability is not done there.
- **p. 17 — Figure 1, applicable visual schema (source-render confirmed).** Example: approximately 650 consent/screen, approximately 500 pass Master Protocol inclusion/exclusion, approximately 150 screen fail. Three simultaneous regimens (A/B/C); each has second randomization 3:1 with 160 participants, shown as active arm(s) 120 and placebo arm(s) 40. Intervention A may have multiple dosing levels. Caption says this is an example and actual regimen size is RSA-specific.
- **p. 18 — Figure 2, applicable visual workflow (source-render confirmed).** Example shows screening then a 6-month treatment period; approximately 160 randomized 3:1 to approximately 120 active and approximately 40 placebo. Timeline: Master screening, RSA screening, baseline, Weeks 2/4/8/12/16/20/24, RSA-specific off-drug follow-up. Caption says study visits are over 24 weeks and actual regimen size is RSA-specific.

### PDF pp. 19-24 — ethics and platform/RSA administrative specifications

- **p. 19 — no applicable result-relevant content.** Ethics/consent procedures only.
- **p. 20 — applicable allocation rule.** Eligible participants are assigned to a regimen; those meeting regimen criteria are randomized 3:1 to active or matching placebo. Reassignment across multiple regimens is possible if eligible.
- **p. 21 — applicable population definition.** Master Protocol eligibility is required for Master enrollment; additional RSA eligibility is required for regimen enrollment.
- **p. 22 — contextual quantitative statements, not a trial result.** ALS median onset age 55 years, average survival 3-5 years after first symptoms, approximate incidence 2/100,000, prevalence about 5/100,000, and less than 10% estimated clinical-research participation. These are background claims, not outcomes of this protocol.
- **p. 23 — applicable shared-placebo definition.** Traditional trials generally have two or three arms; the platform investigates multiple products in parallel/sequentially and compares them to a shared placebo group under a common Master Protocol.
- **p. 24 — applicable RSA parameter definition.** Each RSA specifies product-specific additional eligibility, biomarkers/safety assessments, primary endpoint, maximum sample size, arms including multiple doses, and interim-analysis details.

### PDF pp. 25-31 — objectives, design, and population

- **pp. 25-26 — Table: Objectives and Endpoints (applicable table).** Primary objective: efficacy on ALS disease progression; endpoint: ALSFRS-R total score and survival. Secondary: SVC, isometric HHD/grip strength, and survival. Safety: treatment-emergent AE/SAE; laboratory and ECG parameters/clinically significant abnormalities; suicidal ideation/behavior. Exploratory: biofluid biomarkers and patient-reported outcomes. Labels distinguish primary, secondary, safety, and exploratory endpoints.
- **p. 27 — applicable design/interim rule.** Perpetual multicenter, multi-regimen randomized placebo-controlled adaptive platform. Regimen/treatment duration/follow-up are RSA-specific. Primary endpoint assessed every 4 weeks, site or phone. Interim analyses begin when at least one regimen has 40 randomized participants with opportunity for at least 24 weeks follow-up; all actively enrolling regimens are reviewed every 12 weeks. A regimen can stop for futility (all) or success (applicable only); default is futility only.
- **p. 28 — applicable adaptation rule.** A regimen ends at accrual/maximal exposure and participants complete placebo-controlled follow-up through Week 24; multi-dose/other variation allocation rules must be in its RSA.
- **p. 29 — applicable population thresholds.** Inclusion: ALS diagnostic categories, age >=18 years, consent/procedure ability, weakness onset <=36 months at screening, VC >=50% predicted via SVC (or in-person FVC only under pandemic restriction), stable riluzole >=30 days or none, >=1 edaravone cycle (typically 14 days) or none, swallowing ability, site accessibility, and Relyvrio/Albrioza started >=30 days or none.
- **p. 30 — applicable exclusion thresholds.** ALT or AST >3 times ULN and eGFR <30 mL/min/1.73 m2 are exclusionary irrespective of symptoms. Other criteria include cancer history condition, investigational ALS treatment within 5 half-lives or 30 days, whichever is longer, contraception duration through trial plus 3 months (or RSA-specified), and unresolved rescreen conditions/washout.
- **p. 31 — applicable medication/onset definitions.** Riluzole stability 30 days, edaravone >=1 typically 14-day cycle, Relyvrio/Albrioza >=30 days. ALS symptom onset is first muscle-weakness symptom and must be no more than 36 months before screening.

### PDF pp. 32-40 — enrollment, allocation, treatment, and general assessment procedures

- **p. 32 — applicable population/accounting definition.** EDC records screen-failure reasons and all within-regimen randomized participants irrespective of whether treated.
- **p. 33 — applicable randomization definition.** Tiered randomization uses IRT; consent/re-consent workflow and demographic/screen-failure data are specified.
- **p. 34 — applicable allocation/blinding rule.** Stage 1 equal randomization among available regimens; stage 2 3:1 active:placebo after regimen eligibility. Each active intervention has its own concurrent randomized placebo control. Participants, investigators, and site staff are unblinded to regimen assignment but blinded to treatment within regimen through ATE.
- **p. 35 — applicable ITT/follow-up definition.** People discontinuing investigational product are encouraged to remain under ITT follow-up through Week 24 and ATE; minimum outcome collection encouraged includes ALSFRS-R, AEs, concomitant medication, C-SSRS, and other measures. Follow-up safety call not required if ITT follow-up lasts at least 28 days.
- **p. 36 — applicable administrative termination rule.** Sponsor may terminate Master Protocol or individual regimen at any time or interim; RSA can define regimen-specific termination criteria.
- **p. 37 — applicable arm/placebo definition.** Each active agent has a matching placebo; multiple arms may represent dose, frequency, or route. Shared placebo is described as feasible under Master Protocol assessments.
- **p. 38 — applicable administrative measurement/accountability rule.** Storage temperature is controlled, monitored, and recorded at least daily; product-specific dosage/compliance detail is RSA-specific.
- **p. 39 — no applicable result-relevant content.** Concomitant/prohibited-medication documentation; no quantitative parameter besides non-result recordkeeping.
- **p. 40 — applicable measurement/timing rule.** Baseline Day 0 is the first investigational-product administration; capacity assessed first; outcomes measured by the same qualified/certified evaluator where possible. Remote specified visits are Weeks 4, 8, and 16; ordered remote procedures include ALSFRS-R, AE review, C-SSRS, concomitant medications, and IP accountability/compliance.

### PDF pp. 41-54 — visits, clinical measures, endpoints, and sample collection

- **p. 41 — applicable assessment rule.** Preferred screening eligibility capacity is SVC by certified evaluator/portable spirometer; later missing SVC due restrictions/disability/reason is skipped, recorded, and a protocol deviation reported. Lists screening measurements.
- **p. 42 — applicable enrollment/denominator definition.** Signing Master consent counts as enrolled. If regimen-eligible, second randomization is 3:1. Screen failures must record demographics, failure reason, and assessed criteria.
- **p. 43 — applicable rescreen/timing and baseline definition.** Re-screen after futility/success or completed Week 24 is after 30 days or 5 half-lives, whichever longer; other discontinuation permits rescreen only after the projected Week 24 date. Baseline includes within-regimen randomization, SVC, HHD, ALSFRS-R, PROs, biomarkers, and other listed measures.
- **p. 44 — applicable visit windows.** Week 2 = 14 +/-3 days; Week 4 = 28 +/-7 days; Week 8 = 56 +/-7 days. Lists assessments for each visit, including ALSFRS-R and SVC/HHD at Week 8.
- **p. 45 — applicable visit windows.** Week 12 = 84 +/-3 days; Week 16 = 112 +/-7 days; lists repeated outcomes including SVC/HHD/ALSFRS-R at Week 16 and CSF as RSA-defined.
- **p. 46 — applicable visit windows and endpoint timing.** Week 20 = 140 +/-3 days; Week 24 = 168 +/-7 days. Week 24 collects SVC, HHD, ALSFRS-R, PROs, ECG, safety/biomarker samples, C-SSRS, exit questionnaire. Follow-up safety-call timing is RSA-specific.
- **p. 47 — applicable missingness/protocol-deviation definition.** RSA defines required early-termination outcomes; defines minor/major deviations and specifies missed visits/procedures that are and are not deviations.
- **p. 48 — applicable survival/vital-status definition.** For every randomized participant, record date of death or PAV status/date last known alive and PAV-free through placebo-controlled follow-up (generally Week 24), plus a second check near LPLV; later ascertainment is possible.
- **p. 49 — applicable units/clinical-variable rule.** Weight kg or lb; BP mmHg; pulse/minute; respiratory rate/minute; temperature degrees C or F; height cm or inches at screening only. Safety lab schedule: screening/baseline as RSA-defined, Weeks 4, 8, 16, 24/early termination. eGFR uses MDRD equation; creatinine clearance uses Cockcroft-Gault.
- **p. 50 — applicable safety-measure definitions.** Coagulation measures at screening and Week 16. Standard 12-lead ECG at screening and schedule-defined later visits. C-SSRS baseline version assesses lifetime suicidality.
- **p. 51 — applicable endpoint-scale definition.** Since-Last-Visit C-SSRS is used after baseline. ALSFRS-R: approximately 5 minutes, 12 functional activities, each 0-4, total 0-48, higher = better; stated test-retest reliability >0.88 for all items.
- **p. 52 — applicable measurement rules.** SVC upright by portable spirometer/face mask; 3 trials required, up to 5 if highest vs second-highest variability >=10% among first 3, only best 3 recorded, highest for eligibility, >=3 measurable after screening; predicted and percent-predicted values by Quanjer GLI equations. HHD tests six proximal bilateral groups plus stated distal muscles. Bilateral hand grip in pounds. Certification: ALSFRS-R annually; SVC/HHD every 2 years.
- **p. 53 — applicable specimen unit/timing.** DNA baseline (may be later if baseline not obtained/unusable); blood biomarkers for all participants; urine at baseline, Weeks 8/16/24, up to 10 mL; coagulation at screening and Week 16; LP/CSF RSA-defined.
- **p. 54 — contextual numerical safety statement, not trial result.** Cited external LP experience reports <2.6% post-LP headache and one patient in >1,000 with headache >5 days; no other local/general complications. This is background citation content, not a result of this protocol.

### PDF pp. 55-59 — adverse-event definitions and reporting

- **p. 55 — applicable endpoint label definition.** AE vs suspected ADR definitions; outcome-measure results are collected/analyzed separately rather than recorded as AEs.
- **p. 56 — applicable outcome/AE distinction and SAE criteria.** Worsening SVC, ALSFRS-R, and muscle strength are not AEs; disease progression symptoms are AEs. Lists SAE criteria 1-5 including death and hospitalization.
- **p. 57 — applicable SAE criteria and safety-data definition.** Lists SAE criteria 6-7; AEs collected through participation and reviewed monthly. At each visit AE variables include type, onset/resolution, severity, seriousness, and causality.
- **p. 58 — applicable categorical definitions/timing.** Severity categories mild/moderate/severe; related/not related definitions. AE records include description, severity, seriousness, dates, relationship, action, and outcome. Reportable SAE/event is sent to CC within 24 hours of site notice.
- **p. 59 — applicable safety comparison definition.** DSMB receives blinded enrollment/labs/deviations. Death, respiratory failure, and routine-procedure hospitalization are not individually expedited because anticipated in this population; DSMB reviews aggregate analysis and an IND safety report follows if events occur more frequently in an active group than concurrent placebo.

### PDF pp. 60-70 — statistical plan and data management

- **p. 60 — applicable primary statistical definition.** M-SAP Appendix I takes precedence over protocol if conflict. Primary endpoint is change through Week 24 in ALSFRS-R and survival. Bayesian shared-parameter analysis compares regimen active treatment to shared placebo. Primary survival event is death or PAV: noninvasive/invasive mechanical ventilation >22 hours/day for >7 consecutive days; PAV date is first consecutive day. Recommended design: 160 randomized within regimen.
- **p. 61 — applicable ITT/shared-control/timepoint definition.** Analysis includes ALSFRS-R at 0, 4, 8, 12, 16, 20, 24 weeks plus substitute early/missed-visit measures and survival through 24 weeks. ITT includes active, within-regimen controls, concurrent shared controls, and non-concurrent shared controls. Concurrent controls are randomized within 6 months (180 days) of first and last randomization in analysis regimen.
- **p. 62 — applicable model/missing-data definition.** Bayesian shared-parameter model: repeated-measures ALSFRS-R functional component plus exponential proportional-hazards survival component joined by a shared treatment effect. DRR is the ratio of active-to-placebo disease-progression rate (ALSFRS-R and mortality). Includes participant intercept/slope random effects, covariates, and regimen slope random effects. Uses all data; accommodates death and missing-at-random; no primary-analysis imputation; sensitivity analyses investigate missingness.
- **p. 63 — applicable repeat/multiple-dose/interim/success definitions.** Repeat participants after 30 days or 5 half-lives, whichever longer, are analyzed as new participants/regimen-specific baseline and conditional independent observations. Multiple-dose primary is pooled active doses vs shared control; secondary analyses evaluate doses separately. Interims require 40 randomized (30 active, 10 control) and >=24-week opportunity, occur every 12 weeks. Success posterior probability has simulation-calibrated overall one-sided Type I error 2.5%.
- **p. 64 — applicable futility/secondary/sensitivity/safety definitions.** Futility if posterior probability of at least 10% slowing versus placebo is <5%; non-binding. Secondary joint-rank test ranks survival through 24 weeks then ALSFRS-R change to last jointly observed visit; summed ranks analyzed by covariate-adjusted linear regression. Sensitivity analysis varies shared-control population, assumptions, and missingness. Safety set is all initiating treatment; continuous observed/change-from-baseline summaries; Kaplan-Meier time-to-death/death equivalent.
- **p. 65 — applicable safety summary/sample-size operating characteristics.** AEs summarized by counts and proportion of participants with any TEAE by MedDRA system organ class/high-level/preferred term and severity/relatedness/outcome; labs by CTCAE grade and low/normal/high; shift tables by treatment group. Simulations: null one-sided Type I error 2.4% per regimen, average 14-month regimen duration, 28% early-futility probability. Power to detect 25%/30%/35% slowing with common function/survival effect: 61%/77%/88%; with no survival benefit and 30% functional slowing, 72%; with negative survival and 30% functional slowing, 68%; <1% futility stopping chance in these scenarios.
- **p. 66 — applicable data-quality rules.** SAE entered into EDC and reported to CC within 24 hours of site awareness; EDC contains logic/range checks and in-form rules.
- **p. 67 — applicable monitoring/denominator information.** DSMB receives blinded and unblinded summary frequencies of clinical AEs and safety labs per regimen; placebo data across regimens are compiled into one report.
- **p. 68 — applicable timing/identifier values.** Event-of-interest: AE special interest within 24 hours of dose and severe unexpected SAE reported to DSMB within 1 business day of CC awareness. NeuroGUID is 11 characters; uses 128-bit SSL, ten identifying data elements, and produces a unique alphanumeric string.
- **p. 69 — applicable source/eCRF reconciliation rule.** eCRF data derived from source should be consistent; discrepancies require explanation. Retention: records for two years after marketing approval, or two years after discontinued investigation if no application.
- **p. 70 — no applicable result-relevant content.** Publication/data-sharing/registration administration; no result value. (The supplied source mentions ClinicalTrials.gov, but this extraction did not access the web.)

### PDF pp. 71-76 — appendices and measurement instruments

- **p. 71 — applicable diagnostic-category definitions.** El Escorial appendix: UMN/LMN signs considered across four CNS regions; clinically definite ALS requires both signs in three regions; clinically probable requires signs in at least two with UMN rostral to LMN.
- **p. 72 — applicable diagnostic-category/table definitions.** Laboratory-supported probable and possible ALS categories are defined. Table 1 maps LMN/UMN signs to brainstem, cervical, thoracic, and lumbosacral regions.
- **p. 73 — applicable ALSFRS-R instrument.** Items 1-4 (speech, salivation, swallowing, handwriting) each use scores 4 to 0; item 5a begins (cutting food/utensils without gastrostomy). These anchors define the total score referenced as 0-48 on p. 51.
- **p. 74 — applicable ALSFRS-R instrument.** Completes item 5a; alternate item 5b for gastrostomy; items 6-9 (dressing/hygiene, turning in bed, walking, climbing stairs) all scored 4 to 0.
- **p. 75 — applicable ALSFRS-R instrument.** Completes item 9 and gives respiratory items R-1 dyspnea, R-2 orthopnea, R-3 respiratory insufficiency, each 4 to 0. Item 0 respiratory insufficiency is invasive mechanical ventilation by intubation/tracheostomy, relevant to PAV/survival-endpoint terminology.
- **p. 76 — applicable C-SSRS baseline instrument.** Suicidal ideation categories 1-5 are ordered from wish to be dead to specific plan/intent. The severity type is 1-5, where 1 is least and 5 most severe. Frequency response coding is 1 less than weekly, 2 weekly, 3 two-to-five times/week, 4 daily/almost daily, 5 many times/day. Duration coding: 1 seconds/minutes, 2 <1 hour, 3 1-4 hours, 4 4-8 hours/most day, 5 >8 hours/persistent-continuous. This is a baseline measurement form, not an outcome table.

## Matching main-paper keys and handoff notes

- **Main-paper matching keys:** ALSFRS-R total score; survival/death; PAV/death equivalent; SVC; HHD/grip strength; Week 24; active versus placebo; 3:1 randomization; ITT; shared/concurrent placebo controls; AE/SAE/TEAE; C-SSRS; active-treatment extension; and the regimen-specific analysis population.
- **Required matching qualifiers before cross-source comparison:** regimen/RSA identity, protocol version/date, treatment contrast, analysis population, shared-control definition, follow-up period, endpoint component, model/adjustment, and whether a value is a recommended/example design parameter versus an actual reported outcome.
- **No workbook, CSV, DOC, DOCX, formula, cached workbook value, or formula/display distinction exists in this assigned PDF scope.**
- **No unsupported coverage gap:** all physical PDF pp. 1-76 were freshly extracted and inspected. Pages marked no applicable are explicitly recorded above.

---

### PDF pp. 77-152

# Support quantitative evidence map — support-002

## Scope and direct-source method

- **Source ID:** DOC-002, `joi240158supp1_prod_1742927563.7611.pdf` (229-page supplied PDF; source authority).
- **Exact assigned units:** PDF pp. 77–152 inclusive (76 physical PDF pages), all fresh-required.
- **Fresh extraction:** `pdftotext` native and `pdftotext -layout` were run directly for pp. 77–152. Outputs are `preprocessing/support-002/doc002_p077_p152_native.txt` and `preprocessing/support-002/doc002_p077_p152_layout.txt`.
- **Targeted direct renders:** PDF pp. 101, 103, and 105–111 were rendered for table/figure structure. CPU Tesseract was used only where the native text was absent or materially incomplete: pp. 106–111 and pp. 139–148. The PDF, not OCR, remains the authority.
- **Document identity within these pages:** pp. 77–83 are the tail of the Master Protocol v5.0; pp. 84–152 are Regimen-Specific Appendix C (CNM-Au8), v3.0 dated 2020-06-03. Its printed internal page numbering runs 1–71 across PDF pp. 84–154.
- **Relationship IDs:** local IDs below are durable mapper locators only. They are not candidate IDs or adjudications.

## Page-complete applicability map

| PDF page(s) | Direct-source content and applicability |
|---|---|
| 77–81 | C-SSRS lifetime/since-last-visit assessment form: result-relevant measurement definitions and ordinal labels mapped below. |
| 82–83 | Reference-list continuation only; **no applicable result-relevant quantitative content**. |
| 84 | Regimen appendix title page; **no applicable result-relevant quantitative content**. |
| 85–87 | Table of contents only; it contains navigational internal-page numbers, but no result definition or reported result. **No applicable result-relevant quantitative content.** |
| 88 | Signature/attestation page; **no applicable result-relevant quantitative content**. |
| 89–90 | Abbreviation list; labels (including ALSAQ-40, ALSFRS-R, AUC, CNS-BFS, PD, PK, SVC) provide terminology but no numerical result. |
| 91–97 | Regimen summary and schedules of activities: planned sample allocation, timing, intervention, measurement schedule, and footnotes mapped below. |
| 98–100 | Background/rationale narrative. Quantitative context and product concentration/dosing are mapped below. |
| 101–111 | Product-characteristic table and preclinical figures/results, including printed statistics, units, samples, tests, and figure labels, mapped below. |
| 112–137 | Objectives/endpoints, design, intervention tables, safety margins, visit timing, outcomes, PK/PD definitions, and regimen statistical considerations mapped below. |
| 138 | ALSAQ-40 appendix title only; scale content begins at p. 139. |
| 139–146 | ALSAQ-40 form. Native text layer is blank except page furniture; direct render plus CPU OCR confirms its 40-item, two-week recall response form. Result-relevant scale definitions mapped below; individual questionnaire prose is not reported trial-result data. |
| 147–148 | CNS-BFS form. Three-domain 21-item scoring form and labels mapped below. |
| 149–152 | Reference-list continuation only; **no applicable result-relevant quantitative content**. |

## Protocol and regimen definitions, populations, intervention, and timing

### N-D002-001 — Regimen design, population, allocation, and follow-up

- **Locations:** [DOC-002 — PDF p. 91](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=91>), [PDF p. 92](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=92>), [PDF p. 114](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=114>), and [PDF p. 115](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=115>).
- **Definition/contrast:** multi-center randomized, placebo-controlled, double-blind regimen of oral CNM-Au8 30 mg or 60 mg versus colour-matched placebo. Active:placebo allocation is 3:1; active participants are allocated equally between 30 mg and 60 mg.
- **Planned numbers:** 160 randomized: 120 active and 40 placebo; active is 60 at 30 mg/day and 60 at 60 mg/day. Approximately 60 US centres. Enrollment stops when pre-defined futility criteria are met or the target randomized number is reached.
- **Timing:** maximum placebo-controlled treatment 24 weeks. Participants either have a 28-day follow-up phone call or may enter an OLE planned for at least 52 weeks. The summary gives up to 34 weeks for non-OLE participation (6-week screening + 24-week treatment + 4-week safety follow-up) and approximately 86 weeks with the 52-week OLE; about 10 visits in each stated phase. Section 4.3 describes approximately 24 weeks double-blind plus an additional 52 weeks open label.
- **Population rule:** participant must meet Master Protocol eligibility and the regimen exclusion is history of allergy to gold/gold salts/colloidal gold.

### N-D002-002 — Placebo-controlled and OLE assessment schedule

- **Locations:** [PDF pp. 93–97](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=93>), [PDF pp. 125–133](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=125>).
- **Placebo-controlled visits:** baseline Day 0; Week 2 Day 14 ±3; Week 4 Day 28 ±7; Week 8 Day 56 ±7; Week 12 Day 84 ±3; Week 16 Day 112 ±7; Week 20 Day 140 ±3; Week 24/early termination Day 168 ±7; safety call 28 days after last dose ±3 days. Screening windows are Master Protocol −42 to −1 days and regimen-specific −41 to 0 days. The maximum interval between placebo-controlled visits is 64 days.
- **OLE visits:** Weeks 2, 4, 8, 12, 16, 20, 24, 28, 40, and 52 after the placebo-controlled Week 24 visit; stated day targets/windows include 14 ±3, 28 ±10, 56 ±7, 84 ±3, 112 ±7, 140 ±3, 168 ±3, 196 ±14, 280 ±14, and 364 ±14. OLE maximum visit windows are 64 days for Weeks 8/16 and 96 days for Weeks 28/40/52.
- **Repeated measures:** ALSFRS-R is scheduled throughout both periods; SVC, CNS-BFS, ALSAQ-40, voice, PK/PD samples, C-SSRS, laboratory tests, adverse-event review, drug accountability and vital status have the schedule marks and footnotes on pp. 93–97. The exact calendar rules and special remote-visit omissions are stated in N-D002-012.

### N-D002-003 — Intervention composition, dose, route, and compliance definition

- **Locations:** [PDF pp. 98, 116–119](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=116>), [PDF p. 122](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=122>).
- **Product/dose:** a 60-mL bottle contains CNM-Au8 at 250 μg/mL (15 mg) or 500 μg/mL (30 mg); two bottles each morning give 120 mL/day and 30 mg/day or 60 mg/day. The matched placebo also has two 60-mL bottles/day and 120 mL/day. Administration is oral once daily at about the same time (±1 hour), at least 30 minutes before food; it may be by mouth or gastric tube.
- **Table 2 / Table 3 labels:** each active/placebo dose is two bottles daily, 60 mL/bottle. Per bottle NaHCO3 is 32.8 mg in all three products; Au is 15 mg (30-mg regimen), 30 mg (60-mg regimen), and not applicable for placebo; USP purified water is 60 mL each. Storage: 15–25°C (59–77°F), mean kinetic temperature not over 25°C; 15–30°C (59–86°F) excursions allowed.
- **Dose modification:** no anticipated adjustment during placebo-controlled treatment. With Medical Monitor approval, tolerance-related down-titration is one bottle daily, followed by possible re-challenge to two bottles; no drug holidays. In OLE, blinded dose is maintained and prior placebo recipients are re-randomized to 30 or 60 mg.
- **Compliance analysis-set definition:** bottle counts/logs; per-protocol intake should be 80%–120% of planned dose. A missed same-day dose must not be doubled.

## Endpoints and measurement definitions

### S-D002-001 — Primary analysis endpoint and model

- **Location:** [PDF p. 112](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=112>).
- **Primary efficacy objective/endpoint:** efficacy of CNM-Au8 versus placebo on ALS disease progression, measured as change in ALSFRS-R using a **Bayesian repeated-measures model that accounts for loss to follow-up due to mortality**.
- **Analysis label:** the page provides no effect estimate, interval, posterior criterion, or numerical result; this is a statistical definition requiring matching to the Master Protocol/SAP when cross-source mapping.

### N-D002-004 — Secondary, safety, and exploratory endpoint labels

- **Location:** [PDF pp. 112–113](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=112>).
- **Secondary efficacy:** change in SVC; change in muscle strength measured by hand-held dynamometry and grip strength; survival.
- **Safety:** treatment-emergent adverse/serious adverse events; laboratory and ECG changes/clinically significant abnormalities; treatment-emergent suicidal ideation and behaviour.
- **Exploratory:** quantitative voice changes; active versus placebo difference in the proportion with **≥6-point ALSFRS-R decline from baseline to Week 24**; biofluid-neurodegeneration biomarkers; patient-reported-outcome changes.

### N-D002-005 — ALSAQ-40 and CNS-BFS measurement scales

- **Locations:** [PDF pp. 135, 138–148](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=135>).
- **ALSAQ-40:** patient self-report health-status outcome of subjective well-being in ALS/motor-neuron disease; 40 questions. The direct form uses a two-week recall period. Items 1–30 use a five-category frequency/ability response frame including Never, Rarely, Sometimes, Often, and Always/cannot perform or walk at all when applicable; items 31–40 use Never, Rarely, Sometimes, Often, Always. The eight form pages (PDF pp. 139–146) are image-only in the native layer and were directly rendered/OCR-confirmed. No trial score/value is printed.
- **CNS-BFS:** patient self-report endpoint/clinical measure with 21 questions in three domains: salivation (7), speech (7), swallowing (7). Salivation/swallowing use Does Not Apply=1, Rarely=2, Occasionally=3, Frequently=4, Most of the Time=5. Speech adds Unable to Communicate by Speaking=6. The form supplies domain-total fields and an overall-score field but no computation rule or observed score. On PDF pp. 147–148 it shows the domain item counts and response labels.

### N-D002-006 — C-SSRS safety assessment definitions and coding

- **Locations:** [PDF pp. 77–81](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=77>).
- **Ideation screen:** five ordered ideation types: wish to be dead; non-specific active thoughts; active ideation with any method but no intent; active ideation with some intent but no specific plan; active ideation with specific plan and intent. If questions 1 and 2 are both negative, proceed to suicidal behaviour; if question 2 is positive, ask 3–5; any positive 1/2 triggers intensity section. The most severe ideation type is numbered 1–5.
- **Intensity labels:** frequency 1=less than once/week, 2=once/week, 3=2–5 times/week, 4=daily/almost daily, 5=many times/day. Duration 1=few seconds/minutes, 2=<1 hour/some time, 3=1–4 hours/a lot of time, 4=4–8 hours/most of day, 5=>8 hours/persistent/continuous. Controllability 1=easily controlled through 5=unable to control, with 0=does not attempt; deterrents and reasons-for-ideation also have ordered 1–5 plus 0=does not apply.
- **Behaviour/count fields:** actual, interrupted, and aborted attempts have yes/no and blank total-number fields; preparatory acts and suicidal behaviour are yes/no. Actual lethality/medical damage is coded 0–5 (no/very minor damage through death). Potential lethality is completed only where actual lethality=0 and is coded 0–2 (not likely injury; injury but not death; likely death despite care). The forms are measurement definitions only; no participant values appear.

### N-D002-007 — Voice, PK, PD, and biomarker definitions

- **Locations:** [PDF pp. 134–137](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=134>).
- **Voice:** in addition to clinic recordings, two recordings weekly via Android/iOS app. Tasks: five fixed plus five randomly selected sentences, consonant-vowel sequence, sustained phonation, and one-breath counting. App/AI identifies vocal attributes; trained personnel QC individual recordings.
- **PK:** whole-blood Au and plasma riluzole concentrations are pre-dose. The first 40 riluzole-taking Regimen-C participants to reach Week 8 are to be assessed by DSMB/unblinded designee for population-PK changes for CNM-Au8 versus placebo at Weeks 4 and 8; no result is printed.
- **PD:** pre-dose plasma, whole blood, urine. Potential metabolomic markers: NAD+, NADH, NADP+, NADPH, ATP, ADP, AMP, GSSG, GSH; disease-progression markers may include urinary p75ECD and serum neurofilament light chain.

### S-D002-002 — Regimen statistical considerations

- **Location:** [PDF p. 137](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=137>).
- **Definition:** default Master Protocol statistical design applies with one stated deviation: **no interim analyses for early success**. Clinical-trial simulation is used for operating characteristics (details in regimen SAP). The primary analysis shares all controls from other regimens, justified by minor eligibility differences and no expected systematic primary-endpoint difference across control groups.

## Tables, formulas, quantitative preclinical evidence, and statistical labels

### N-D002-008 — Table 1: CNM-Au8 particle characteristics

- **Location:** [PDF p. 101](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=101>), visually confirmed from a direct render.
- **Columns/assumptions:** CNM-Au8 500 μg/mL, 60-mL dose; disc-like minimum (aspect 0.2) versus spherical maximum (aspect 1.0).
- **Rows:** median diameter 13 nm; volume 2.3×10^2 versus 1.2×10^3 nm³; surface area 3.2×10^2 versus 5.3×10^2 nm²; Au atoms/nanocrystal 1.4×10^4 versus 6.8×10^4; molecular weight 2.7×10^3 versus 1.3×10^4 kDa; total surface area/mL 3.6×10^2 versus 1.2×10^2 cm²; nanocrystals/mL 1.1×10^14 versus 2.3×10^13; nanocrystals/60-mL dose 3.4×10^15 versus 6.8×10^14.

### S-D002-003 — Figure 1 and Figure 2 preclinical NADH/NAD statistics

- **Location:** [PDF p. 103](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=103>), direct render.
- **Figure 1A:** NADH absorbance at 339 nm (cm⁻¹) over time in minutes, for 26 μM NADH in 5.7 mM NaHCO3 with 3.4 μg/mL Au; comparator labels are CNM-Au8, NIST 10-nm, NIST 30-nm, and NADH control/no GNPs.
- **Figure 1B:** relative NADH oxidation rate (a.u.) versus GNPs at [Au] about 3.4 μg/mL. Caption/footnote: *P<0.05 versus control, one-way ANOVA followed by Dunnett's test.
- **Figure 2:** effects of CNM-Au8 on NAD+ and NADH levels in primary rodent mesencephalic cultures; bar panels use quantity of NAD+ (μM) and ratio of NAD+/NADH, respectively. Dose labels include control, CNM-Au8 10/100/500/1,000 ng/mL, and BDNF 50 ng/mL; the same P<0.05 versus control one-way ANOVA/Dunnett label applies. Values are plotted graphically without a supplied numeric table.

### S-D002-004 — Figures 4–9 preclinical effects and printed tests

- **Locations:** [PDF pp. 105–111](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=105>), direct renders and targeted OCR.
- **Figure 4:** SOD/ROS generation. Panel A is Abs 450 nm, cm⁻¹ (t=20 minutes), a.u. (SEM) for CNM-Au8 1000/750/500/250 and vehicle. Panel B is mean intensity (a.u.) over time (seconds) for control, buffer, and 0.3/1/3 μg/mL; marked comparisons ** and **** are drawn. Panel C is mean intensity (a.u.) over time (seconds) with rotenone for buffer, 0.3, 1, and 3 μg/mL; an asterisk is drawn. Graphic values are not tabulated.
- **Figure 5:** CNM-Au8 effects on OPC differentiation (O4+ cells) and glycolytic ATP in MO3.13 oligodendrocytes at 72 hours, plotted as mean ± SEM. Stated analysis: one-way ANOVA, P<0.05.
- **Figure 6:** rat motor-neuron glutamate-excitotoxicity experiments. Cultures were pre-treated on day 11; riluzole was pre-treatment for 1 hour; day-13 glutamate was 20 minutes then treatment for 48 hours. Outcomes/labels include MAP-2 motor-neuron survival, neurite-network area, and cytoplasmic TDP-43. Figure panels state *P<0.05 versus glutamate, one-way ANOVA followed by PLSD Fisher's test; illustrated glutamate concentration is 20 μM.
- **Figure 7:** iPSC-derived normal human motor neurons exposed to SOD1A4V ALS-participant astrocytes for 14 days. Panels quantify Tuj1, Isl1/2, and ChAT by CNM-Au8 dose (ng/mL); exact bar heights are graphical, not tabulated.
- **Murine study narrative:** rapidly progressive model: N=15/group, clinical-onset P=0.13 (Mantel-Cox), lack of brainstem atrophy P<0.05 (unpaired t test); other functional measures not significant. Slower model: N=20 female mice, 10/group, balanced for weight; stated life spans approximately 157 versus 129 days for the two strain contexts.
- **Figure 8:** slower SOD1G93A model, locomotor efficacy: A neurological score P=0.0074 (two-way ANOVA); B weights-hold P<0.01 (two-way ANOVA); C horizontal-bar P<0.05 (two-way ANOVA); D/E home-wheel velocity including periods Days 71–100, 101–130, 131–160 and P<0.0001 (two-tailed t test). Axes are age (weeks/days), score, test units, or wheel-running velocity as plotted.
- **Figure 9:** survival proportions Kaplan–Meier plot, Breslow–Wilcoxon P=0.0302 and hazard ratio 0.3730, CNM-Au8 versus vehicle; x-axis days alive (120–180) and y-axis survival proportions (%) (0–100).

### N-D002-009 — Animal/human safety-margin tables and exposure relationship

- **Locations:** [PDF pp. 119–122](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=119>).
- **Table 4, 21-day HED body-surface-area dose ratios for 60-kg human:** rat NOAEL 40 mg/kg/day=240 mg/m²; safety margins at human 15/30/60/90 mg (9.3/18.5/37.0/55.5 mg/m²) are 25.9/13.0/6.5/4.3. Canine NOAEL 90 mg/kg/day=1800 mg/m²; corresponding margins 194.6/97.3/48.6/32.4.
- **Table 5, 21-day AUC(0–24) animal:human ratio:** human AUCs at 15/30/60/90 mg are 32.3/41.4/50.3/66.0 ng·hr/mL. Rat NOAEL 40 mg/kg/day, animal AUC 106 ng·hr/mL, margins 3.3/2.6/2.1/1.6. Canine NOAEL 90 mg/kg/day, animal AUC 596, margins 18.5/14.4/11.8/9.0. Footnote: animal AUC is male/female average at end of study.
- **Table 6, chronic AUC ratio:** rat 6-month NOAEL 40 mg/kg/day, AUC 209, margins 6.5/5.0/4.2/3.2; canine 9-month NOAEL 10 mg/kg/day, AUC 440, margins 13.6/10.6/8.7/6.7, in the same human-dose order. The text states 30.6 hr·ng/mL mean AUC for rodent neuroprotection and 50.3 hr·ng/mL at human 60 mg, supporting 15–30 mg minimum human-equivalent exposure; selected ALS doses are 30 and 60 mg/day.

### N-D002-010 — Safety thresholds and follow-up rules

- **Locations:** [PDF pp. 123–124](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=123>).
- **Human prior exposure:** Phase-1 doses 15, 30, 60, 90 mg; stated well tolerated up to 90 mg/day over 21 consecutive days. No human ALS trials at the time of document.
- **Laboratory alert table:** ALT/AST >3× ULN; creatinine >1.5× baseline; platelet count <75,000/mm³. These prompt further investigation but do not mandate reduction/discontinuation.

### N-D002-011 — Schedule-specific assessment rules and administrative timing

- **Locations:** [PDF pp. 93–97](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=93>) and [PDF pp. 125–133](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=125>).
- **Footnoted definitions:** vital signs are weight, systolic/diastolic pressure, respiratory rate, heart rate, temperature; height is Master Screening only. Clinical safety labs: CBC/differential, chemistry, thyroid function, urinalysis; OLE table also labels liver tests. Pregnancy tests are as applicable. AEs after consent are recorded.
- **Collection rules:** whole blood/plasma pre-dose at baseline and Week 24; plasma pre-dose Week 4/8. Vital status is death/death-equivalent date or last-known-alive date, determined for each randomized participant at end of placebo-controlled follow-up and again at last-patient-last-visit if alive.
- **Visit-specific timing:** Week 2/12/20 placebo telephone visits at 14±3/84±3/140±3 days; Week 4/8 at 28±7/56±7; Week 16 112±7; Week 24 168±7; safety call 28±3 after last dose. Early termination during placebo/OLE calls for Week-24/OLE-Week-52 assessments respectively and the stated 28±3 safety-call rule.
- **Remote visits:** during pandemic remote schedules, blood/urine PK/PD samples are not collected by home health agency and must be recorded as such; this is an administrative collection rule, not an observed missing-data result.

## Non-applicable / limitations record

- **No reported human efficacy, safety, participant-flow, laboratory, PK, PD, or trial-result values occur in pp. 77–152.** This shard contains protocol/regimen definitions, planned quantities, forms, and preclinical rationale; its values must not be represented as observed results.
- **Image-only form content:** ALSAQ-40 pages 139–146 required direct render plus CPU OCR because native/layout text did not contain form questions. The form-level counts, two-week recall, and response labels were confirmed; no scores were printed.
- **Graph-only preclinical values:** Figures 1, 2, 4–9 provide plotted points/bars/curves but no source data table. Axis units, treatment labels, sample sizes where printed, and test/P-value/HR labels are mapped; unprinted precise graphical readings are not fabricated.
- **No workbook, CSV, DOC/DOCX, formula cells, or cached workbook values are in this assigned source unit.**

## Completion counts

- **Assigned/mapped physical source units:** 76/76 PDF pages (pp. 77–152).
- **Pages with result-relevant quantitative/measurement/statistical content:** 64 pages (77–81, 89–137, and 139–148).
- **Explicit no-applicable pages:** 12 pages (82–88, 138, and 149–152); pp. 85–87 are navigational contents only.
- **Mapped local quantitative/definition relationships:** 11 `N-D002` records.
- **Mapped local inferential/statistical relationships:** 4 `S-D002` records.
- **Coverage gap:** none for the assigned direct PDF pages. Figure data are only graphically displayed where noted; that is a source limitation, not a page-coverage gap.

---

### PDF pp. 153-229

# Support quantitative evidence map — support-003

## Scope, authority, and extraction record

- **Direct source:** `joi240158supp1_prod_1742927563.7611.pdf` (DOC-002), PDF pp. 153-229 inclusive (77 physical PDF pages).
- **Authority:** the supplied PDF is the authority. Its internal document page numbering begins at PDF p. 155 (`Page 1 of 75`).
- **Fresh direct-source work:** native and layout text were freshly extracted across the complete assigned range with `pdftotext -f 153 -l 229` and `pdftotext -layout -f 153 -l 229`; output files are in `preprocessing/support-003/doc002_p153_p229_native.txt` and `preprocessing/support-003/doc002_p153_p229_layout.txt`.
- **Targeted visual/OCR work:** native text on PDF pp. 213-221 omitted the image-only ALSAQ-40 forms. Those pages were freshly rendered at 250 dpi and CPU-OCRed with Tesseract; direct-page PNG and OCR outputs are in `preprocessing/support-003/` with the page number in each filename. Figures/tables on PDF pp. 174-175, 177-183, and 195 were also rendered and OCR-assisted for labels, axes, and footnotes. Source PDF layout remains authoritative where chart text is rasterized or OCR is incomplete.
- **Matching main-paper key:** HEALEY ALS Platform Trial, Regimen C / CNM-Au8; randomized placebo-controlled comparison of active CNM-Au8 (30 mg or 60 mg once daily) versus matched placebo; 24-week double-blind period; ALSFRS-R primary disease-severity endpoint; shared-control master-platform analysis. These are matching keys, not an adjudication or cross-source conclusion.
- **Boundary:** this is an evidence map only. No candidate, consistency diagnosis, or conclusion about any relationship is made here.

## Quantitative/statistical definitions, populations, and analysis rules

| Source location | Direct-source mapping |
|---|---|
| PDF p. 162 (internal p. 8) | Protocol summary: randomized, double-blind test of CNM-Au8 **30 mg and 60 mg** versus placebo. The two doses were selected to give at least comparable human AUC exposure to efficacious nonclinical animal exposures. |
| PDF p. 163 (p. 9) | Planned regimen population is approximately **160** participants, allocated **3:1 active:placebo** (**120 active:40 placebo**); active participants are divided equally: **60 at 30 mg/day** and **60 at 60 mg/day**. Approximately **60 US centers**. Maximum placebo-controlled duration: **24 weeks**. Planned participant duration without OLE: up to **34 weeks** (6-week screening + 24-week double-blind + 4-week safety follow-up), approximately **10** placebo-controlled visits. Enrollment stops at the planned total or pre-defined futility criteria. |
| PDF pp. 164-166 (pp. 10-12) | Placebo-controlled schedule: screening −42 to −1 days; regimen screening −41 to 0; baseline Day 0; Week 2 Day 14 ±3; Week 4 Day 28 ±7; Week 8 Day 56 ±7; Week 12 Day 84 ±3; Week 16 Day 112 ±7; Week 20 Day 140 ±3; Week 24/early termination Day 168 ±7; follow-up **28 days after last dose ±3 days**. Maximum gap between placebo-controlled visits: **64 days**. PK footnote: whole blood/plasma predose at baseline and Week 24; plasma predose at Weeks 4 and 8. Vital-status definition is date of death/death equivalent or date last known alive for every randomized participant. |
| PDF pp. 167-168 (pp. 13-14) | Optional OLE schedule: Week 2 Day 14 +3; Week 4 Day 28 ±7; Week 8 Day 56 ±7; Week 12 Day 84 ±3; Week 16 Day 112 ±7; Week 20 Day 140 ±3; Week 24 Day 168 ±3; Week 28 Day 196 ±14, then every 12 weeks ±14. OLE visit-gap maxima are **64 days** through Week 16 and **96 days** from Week 28 onward. OLE blood/urine biomarker collection is Week 16, 28, 52 and every 24 weeks thereafter for regimen-specific collection; ALSAQ-40 is Week 28 and every 24 weeks thereafter. |
| PDF pp. 184-185 (pp. 30-31) | **Primary efficacy endpoint:** change in ALSFRS-R total score, analyzed with a **Bayesian repeated-measures model** that accounts for mortality-related loss to follow-up. Secondary endpoints: SVC change, HHD/grip-strength change, and survival. Exploratory endpoints include quantitative voice characteristics, biofluid biomarkers, patient-reported outcomes, home spirometry, and active-versus-placebo difference in the proportion with **≥6-point ALSFRS-R decline** from baseline to Week 24. Safety endpoints are treatment-emergent AEs/SAEs, laboratory and ECG changes/clinically significant abnormalities, and treatment-emergent suicidal ideation/behavior. |
| PDF p. 186 (p. 32) | Multi-center randomized placebo-controlled study of **30 mg** and **60 mg** oral daily CNM-Au8 versus color-matched placebo. Allocation is **3:1 active:placebo**, with equal allocation between active doses. The comparator is sodium-bicarbonate solution in USP water, color-matched to active. |
| PDF p. 188 (p. 34) | Approximately **160 randomized**. Eligible population must meet master-protocol eligibility plus this regimen's sole listed exclusion: history of allergy to gold, gold salts, or colloidal gold. Planned double-blind treatment is approximately **24 weeks**; OLE may follow. |
| PDF pp. 196, 201-203 (pp. 42, 47-49) | Per-protocol treatment compliance is defined as **80%-120%** of planned dose, assessed at specified in-clinic visits by bottle count/log. The Week 2, 12, and 20 telephone visits are **14 ±3**, **84 ±3**, and **140 ±3** days after baseline, respectively; Week 24/early termination is **168 ±7** days. Follow-up safety call is **28 ±3** days after last dose. Early termination during the placebo-controlled period uses Week-24 assessments; in OLE it uses OLE Week-52 assessments. |
| PDF pp. 208-209 (pp. 54-55) | Voice samples are collected **twice per week**; each app session includes **5 fixed** sentences and **5 randomly selected** sentences, plus consonant-vowel repetition, sustained phonation, and single-breath counting. ALSAQ-40 is a **40-question** self-report PRO. CNS-BFS has **3 domains** (swallowing, speech, salivation) and **21 questions**. Home spirometry is remote forced vital capacity using MIR Spirobank Smart, with **3-5** vital-capacity maneuvers. |
| PDF p. 210 (p. 56) | Riluzole population PK: the first **40** riluzole-taking participants randomized to Regimen C who reach Week 8 are reviewed by the DSMB or unblinded DSMB PK designee for CNM-Au8-versus-placebo changes in riluzole population PK parameters at Weeks **4 and 8**. Au whole-blood and riluzole plasma collections are predose. PK/PD analytic plans are separate and not supplied in this source unit. |
| PDF p. 212 (p. 58) | Statistical design follows default master-protocol Appendix I except **no interim analyses for early success**. Operating characteristics are quantified using clinical-trial simulation (details referred to the regimen SAP). Primary analysis shares **all controls from other regimens**; stated rationale is minor RSA eligibility differences and no expected systematic primary-endpoint differences among controls across regimens. |

## Tables, figures, displayed results, units, and footnotes

| Source location | Evidence map |
|---|---|
| PDF pp. 171-172 (pp. 17-18), Table 1 | Product definition: CNM-Au8 suspension is **500 μg/mL** and each 60-mL dose has an estimated **100-500 trillion** highly faceted Au nanocrystals. Median diameter **13 nm**; corresponding nanocrystal composition stated as approximately **13,000-66,000 Au atoms** and molar mass **2.7 × 10^3 to 1.3 × 10^4 kDa**. Table 1, for 500 μg/mL and a 60-mL dose, gives disc-like (aspect 0.2) / spherical (aspect 1.0) values: volume **2.3×10^2 / 1.2×10^3 nm³**; surface area **3.2×10^2 / 5.3×10^2 nm²**; atoms/nanocrystal **1.4×10^4 / 6.8×10^4**; molecular weight **2.7×10^3 / 1.3×10^4 kDa**; total surface area per mL **3.6×10^2 / 1.2×10^2 cm²**; nanocrystals/mL **1.1×10^14 / 2.3×10^13**; nanocrystals per 60-mL dose **3.4×10^15 / 6.8×10^14**. |
| PDF pp. 174-175 (pp. 20-21), Figures 1-2 | Figure 1 compares CNM-Au8 with NIST citrated AuNPs at **10 nm** and **30 nm**. Figure 1A condition: **26 μM NADH**, **5.7 mM NaHCO₃**, **3.4 μg/mL Au**; y-axis is NADH absorbance at **339 nm** (cm⁻¹), x-axis time (minutes 0-30). Figure 1B uses the same NADH/NaHCO₃ condition and Au approximately 3.4 μg/mL; outcome is relative NADH oxidation rate (arbitrary units). Narrative labels CNM-Au8 activity significantly superior. Figure 2 is labeled as effects on NAD+ and NADH levels in primary rodent mesencephalic cultures; displayed bars use concentration groups including CNM-Au8 and BDNF control. Footnote: `* p < 0.05 vs control condition`, **one-way ANOVA followed by Dunnett's test**. Exact bar heights are rasterized/not numerically tabulated. |
| PDF pp. 176-178 (pp. 22-24), Figures 4-5 | Narrative reports dose-dependent ROS reduction in differentiating oligodendrocyte precursor-cell primary cultures with CNM-Au8. Figure 4 panels: SOD activity assay; ROS generation in purified murine OPC cultures; ROS generation in murine OPC cultures plus rotenone. Figure 5 covers OPC differentiation (O4+ cells) in isolated murine OPCs and glycolytic ATP in MO3.13 oligodendrocytes at **72 hr**, shown as mean ± SEM. Caption states one-way ANOVA **p < 0.05**. The PDF supplies chart labels and inferential threshold but not a numerical table of bar values. |
| PDF pp. 178-180 (pp. 24-26), Figure 6 | In-vitro rat-embryo (E14) ventral-spinal-cord culture: seed Day 11 pretreatment with CNM-Au8 or vehicle; riluzole positive control is **1 hour** pretreatment before glutamate; on Day 13 glutamate is applied for **20 minutes**, then riluzole/CNM-Au8 for **48 hours** before fixation. Outcomes: MAP-2 motor-neuron survival, neurite length/network area, cytoplasmic TDP-43. Figure 6A survival and Figure 6B neurite network charts use `* p < 0.05 vs glutamate`, one-way ANOVA followed by PLSD Fisher's test. Figure 6D shows cytoplasmic TDP43 with one-way ANOVA followed by PLSD Fisher's test. Displayed concentrations/bar heights are graphical rather than tabulated. |
| PDF pp. 180-181 (pp. 26-27), Figure 7 | Healthy human iPSC-derived motor neurons were co-cultured with SOD1A4V astrocytes for **14 days** under CNM-Au8 doses or vehicle. Outcomes shown are Tuj1, Isl1/2, and ChAT marker measures versus dose (ng/mL), with narrative calling effects significant and dose-dependent. Exact plotted values/statistical footnote are not legible as a tabulated source value. |
| PDF pp. 181-183 (pp. 27-29), Figures 8-9 | Rapid SOD1G93A mixed SJL/C57BL6 study: clinical-onset improvement `p=0.13` (Mantel-Cox), lack of brainstem atrophy `p<0.05` (unpaired t test), **N=15 animals/group**; other functional measures not significant. Slow C57BL/6-congenic study: **N=20 female mice, 10/group**, random assignment at 4 weeks, treatment in drinking water; weekly testing begins Week 8. Figure 8: ALS TDI neurological score `p=0.0074`, two-way ANOVA; weight-hold `p<0.01`, two-way ANOVA; horizontal-bar `p<0.05`, two-way ANOVA; home-wheel-by-period `* p<0.05`, `**** p<0.0001`, two-tailed t test. Figure 8 axes include age in weeks/days, neurological-score scaling, test measures, and wheel-running velocity. Figure 9 Kaplan-Meier survival: Breslow-Wilcoxon `p=0.0302`, hazard ratio **0.3730**, x-axis days alive (120-180), groups CNM-Au8 and vehicle. |
| PDF pp. 189-190 (pp. 35-36), Tables 2-3 | **Table 2 (double blind):** CNM-Au8 30 mg / CNM-Au8 60 mg / matched placebo. Total daily dosage **30 mg / 60 mg / NA**; concentration **250 μg/mL / 500 μg/mL / NA**; volume/bottle **60 mL each**; **2 bottles/day**, daily volume **120 mL**, oral once daily, same time (±**1 hour**). OLE can use either two 60-mL bottles or one 120-mL bottle. **Table 3:** NaHCO₃/bottle **32.8 mg / 32.8 mg / 32.8 mg / 65.5 mg** (30-mg, 60-mg, placebo, 30-mg OLE); Au/bottle **15 mg / 30 mg / NA / 30 mg**; USP purified water **60 / 60 / 60 / 120 mL**. Quality labels: NaHCO₃ ACS/USP identity, Au ASTM B562-95 and USP <233>, water USP total organic carbon/conductivity. |
| PDF pp. 192-195 (pp. 38-41), Tables 4-6 and Figure 10 | Reported Phase-1 doses are **15, 30, 60, 90 mg**. Dose-ratio safety margins are stated as **26×-4×** rodents and **195×-32×** canines; top 90-mg human dose has a minimum **4×** rat NOAEL margin. **Table 4:** Rat NOAEL 40 mg/kg/day, 240 mg/m²; margins 25.9, 13.0, 6.5, 4.3 at 15/30/60/90 mg (9.3/18.5/37.0/55.5 mg/m²). Canine NOAEL 90 mg/kg/day, 1800 mg/m²; margins 194.6, 97.3, 48.6, 32.4. **Table 5 (21-day AUC(0-24), ng·hr/mL):** human AUC 32.3/41.4/50.3/66.0 at 15/30/60/90 mg; rat NOAEL 40 mg/kg/day, AUC 106, margins 3.3/2.6/2.1/1.6; canine NOAEL 90 mg/kg/day, AUC 596, margins 18.5/14.4/11.8/9.0. Footnote: animal AUC is average male/female end-of-study value. **Table 6 (chronic):** rat 6-month NOAEL 40 mg/kg/day, AUC 209, margins 6.5/5.0/4.2/3.2; canine 9-month NOAEL 10 mg/kg/day, AUC 440, margins 13.6/10.6/8.7/6.7, with the same human AUC series and footnote. Figure 10 displays Day-21 whole-blood Au exposure AUC(0-24), geometric mean: **32.3, 41.4, 50.3, 66.0 hr·ng/mL** across first-in-human doses and a preclinical efficacy value **30.6 hr·ng/mL**. |
| PDF p. 196 (p. 42) | Selected trial doses: **30 mg/day** and **60 mg/day**. Product compliance between **80% and 120%** planned dose is the stated per-protocol threshold. |
| PDF p. 198 (p. 44) | Regimen lab-alert thresholds: ALT and AST `>3× ULN`; creatinine `>1.5× baseline`; platelets `<75,000/mm³`. Alerts are informational, not mandatory dose reduction/discontinuation criteria. |
| PDF pp. 213-221 (pp. 59-67), Appendix I ALSAQ-40 | The form uses a **2-week** recall period and **40 items**. Items 1-30 have response options Never, Rarely, Sometimes, Often, Always/cannot perform activity at all (walking-function wording: Always/cannot walk at all); items 31-40 have Never, Rarely, Sometimes, Often, Always. Domains apparent from item blocks: physical mobility 1-10, ADL/independence 11-20, eating/speech 21-30, emotional functioning 31-40. It is an instrument form; the source supplies no scoring formula, total, direction transform, or observed result. |
| PDF pp. 222-223 (pp. 68-69), Appendix II CNS-BFS | CNS-BFS form: three 7-item domains, total **21 items**. Sialorrhea and swallowing response values are Does Not Apply **(1)**, Rarely **(2)**, Occasionally **(3)**, Frequently **(4)**, Most of the Time **(5)**. Speech uses those values plus Unable to Communicate by Speaking **(6)**. Domain totals (Sialorrhea, Speech, Swallowing) and an Overall Score are blank fields; no scoring formula, observed score, or analytic direction is supplied. |

## Administrative, protocol, and no-applicable-unit record

| PDF pages | Complete mapping outcome |
|---|---|
| 153-154 | Reference-list continuation for the preceding supplied protocol material. No result-relevant quantitative relationship, endpoint, statistical definition, table, figure, or formula in this assigned unit. |
| 155 | Regimen-Specific Appendix C title: CNM-Au8, date **07 November 2022**, version **6.0**. No result relationship beyond document/version identity. |
| 156-158 | Table of contents: maps internal pages and sections, including statistics at internal p. 58 and appendices at pp. 59/68. Administrative locator; no independent result values. |
| 159 | Investigator signature/administrative compliance page. No applicable result-relevant quantitative content. |
| 160-161 | Abbreviation definitions relevant to mapped units: ALSAQ-40, AUC/AUC(0-24), CNS-BFS, HED, mg, mL, ng, nm, NOAEL, OLE, PD, SVC, and related labels. No result relationship apart from unit/label definitions carried into the map. |
| 169-170 | ALS background narrative includes epidemiologic/context values: incidence approximately **1 in 100,000**, familial ALS **5%-10%** of cases. These are cited background, not trial results or defined trial analysis relationships. |
| 173 | Background rationale includes age bands **21-26**, **33-36**, and **59-68** years in cited 31P-MRS research. No regimen trial result/table/analysis rule is supplied on this page. |
| 187 | Internal document page 33 carries only running header/footer. No applicable result-relevant content. |
| 197 | Risk narrative: nonclinical NOAEL up to **10 mg/kg/day** canine and **40 mg/kg/day** rat; healthy-volunteer dosing up to **90 mg/day for 21 consecutive days**. No new trial endpoint or analytic rule. |
| 199-207 | Operational visit instructions are mapped in the definitions table above. Additional operational details: designated remote-eligible placebo visits are Weeks 4, 8, 16; OLE remote-eligible visits include 4, 8, 16, 28, 40; PK/PD blood/urine are not collected by home-health agency during remote visits. No observed treatment result is reported. |
| 224-229 | Reference list only. No result-relevant quantitative relationship, endpoint, table, figure, formula, or source result appears in these assigned pages. |

## Completeness summary

- **Assigned direct-source units inspected:** 77/77 PDF pages (PDF pp. 153-229).
- **Fresh native/layout extraction:** 77/77 pages. **Targeted CPU OCR:** 9 image-only questionnaire pages (PDF pp. 213-221), plus visual confirmation for 10 figure/table pages.
- **Result-relevant mapped content:** 12 protocol/population/analysis-rule records; 11 table/figure/displayed-result/instrument records; 12 administrative or operational records. Tables mapped: 1-6. Figures mapped: 1, 2, 4-10 (Figure 3 is not labeled or present in the supplied assigned internal-page sequence). Instruments mapped: ALSAQ-40 and CNS-BFS.
- **Explicit no-applicable direct-source units:** PDF pp. 153-154, 159, 187, and 224-229; the table of contents and title/abbreviation pages are recorded as administrative/unit-label content rather than silently omitted.
- **Gaps/limitations:** Chart-bar heights and several rasterized dose labels are graphical without an accompanying numerical data table. They are recorded as graphical rather than converted to fabricated exact values. The separate master protocol, regimen SAP, Manual of Procedures, laboratory manual, DSMB charter, and PK/PD analysis plans are referenced but are not part of this assigned DOC-002 page range; their absent definitions are therefore not inferred.

---

## DOC-003 — Master and regimen-specific statistical analysis plans (fresh direct-source mapping)

### PDF pp. 1-65

# Support Evidence Map — DOC-003, PDF pp. 1-65

## Scope and direct-source method

- **Source authority:** `joi240158supp2_prod_1742927563.7711.pdf`, a 130-page PDF. This part maps only physical PDF pages 1-65; it does not infer or cover PDF pp. 66-130.
- **Fresh extraction:** native and layout `pdftotext` were run directly against PDF pp. 1-65. Page-specific layout outputs are retained under `preprocessing/support-004/` as `doc003_p001_layout.txt` through `doc003_p065_layout.txt`; combined outputs are `doc003_p001_p065_native.txt` and `doc003_p001_p065_layout.txt`.
- **Document structure:** PDF pp. 1-62 are the HEALEY ALS Platform Trial Master Statistical Analysis Plan (M-SAP), version 3.0 dated 06 February 2023. PDF pp. 63-65 begin the RGC (CNM-Au8) regimen-specific SAP, version 1.0 dated 17 March 2022.
- **Scope boundary:** this is an evidence and relationship map only. It does not diagnose, rank, register, or adjudicate candidates.

## Page-level coverage and no-applicable records

| PDF pages | Content and mapping outcome |
|---|---|
| 1 | M-SAP cover and approvals: version 3.0, protocol version 5.0 dated 15 December 2022, SAP dated 06 February 2023. No result-relevant quantitative relationship beyond document/version identity. |
| 2-5 | M-SAP revision history. Result-relevant revisions include: at least two completed SVC maneuvers; log transformation of serum/CSF NfL; death-alone survival endpoint; time-at-risk/censoring convention; updated covariates, analysis sets, HHD0/HHD0[2], placebo imputation, and subgroup specifications. No results table or outcome values. |
| 6-7 | Table of contents only. No applicable quantitative result beyond section/page locator. |
| 8-31 | M-SAP design, endpoints, measurement definitions, analysis sets, estimands, analysis models, safety summaries, subgroup rules, and validation tolerances; mapped below. |
| 32 | Appendix I cover/table of contents and change summary. No outcome table; it locates the master protocol recommended statistical analysis, design, and simulation report. |
| 33-44 | Appendix I primary analysis, priors, thresholds, diagnostics, and sensitivity-analysis definitions; mapped below. |
| 45-61 | Appendix I simulations, simulation parameter tables, operating-characteristic tables, and example-trial figures; mapped below. |
| 62 | Reference only (CAFS citation). No applicable result-relevant quantitative content. |
| 63 | RGC R-SAP title/approval page. Regimen is RGC: CNM-Au8; Master Protocol v4.0 dated 31 August 2020; RSA v5.0 dated 22 November 2021; Master SAP v1.0 dated 24 June 2020; R-SAP v1.0 dated 17 March 2022. No analysis result. |
| 64 | RGC R-SAP approval signatures only. No applicable quantitative content. |
| 65 | RGC R-SAP revision history: v1.0, 17 March 2022, initial version. No applicable quantitative content. |

## Study design, populations, endpoints, labels, and units

### Core design and population (PDF pp. 8-11)

- The perpetual multicentre, multi-regimen platform compares each distinct investigational product with placebo. An RSA supplies regimen-specific target population, extra criteria, sample size, dose/frequency, and assessments (p. 8).
- Eligibility includes age **at least 18 years**, weakness onset **within 36 months** of screening, and SVC **at least 50% predicted** by age, sex, and height; recruitment is from approximately **60** US NEALS sites (p. 9).
- Participants are first allocated with equal probability among applicable regimens, then allocated within regimen **3:1 active:placebo** by permuted blocks. Stratification is every combination of use/non-use of riluzole, edaravone, and sodium phenylbutyrate/taurursodiol at master-protocol screening (pp. 9-10).
- Double-blind treatment is up to **28 weeks** unless the RSA states otherwise. Clinic visits are at weeks **4, 8, 16, 24**; telephone visits at weeks **2, 12, 20**, plus a call **28 days after last dose** (p. 9). The schedule specifies baseline Day 0 and Week 24 Day 168 (±7 days), with corresponding Week 2 Day 14 (±3), Week 4 Day 28 (±7), Week 8 Day 56 (±7), Week 12 Day 84 (±3), Week 16 Day 112 (±7), and Week 20 Day 140 (±3) (pp. 10-11).
- Vital status is date of death/death equivalent or date last known alive at placebo-controlled follow-up end, generally Week 24, and is redetermined at last participant's last visit if alive (p. 11 footnote 9).

### Endpoint and scale definitions (PDF pp. 13-16)

- **Primary efficacy endpoint:** change from baseline through Week 24 in disease severity measured by **ALSFRS-R total score and survival** (p. 13).
- **Secondary efficacy endpoints:** Week-24 change in isometric HHD/grip strength, SVC respiratory function, and survival (p. 13). Exploratory categories: biofluid biomarkers and patient-reported outcomes. Safety includes treatment-emergent adverse/serious adverse events, laboratory and ECG changes/abnormalities, and suicidal ideation/behavior; safety proportions use the applicable Safety sample denominator (p. 13).
- **ALSFRS-R:** 12 clinician-interview items in four domains; each is 0-4 and higher is better function. Total is 0-48; domains are 0-12: bulbar Q1-Q3, fine motor Q4-Q6, gross motor Q7-Q9, respiratory R1-R3/Q10-Q12 (p. 13). Pre-baseline delta-FRS is `(48 - baseline ALSFRS-R) / months from symptom-weakness onset to baseline`; months = day difference × `12/365.25`; an imprecise onset date is imputed to the fifteenth of the month (pp. 13-14).
- **SVC:** maximum slowly exhaled volume after maximal inhalation. It uses 3-5 manoeuvres, with a minimum of **2 completed SVC manoeuvres** for a visit; one pulmonary-function-lab maximum vital capacity from a slow or forced manoeuvre is acceptable. Maximum volume is percent predicted using GLI FVC normals based on sex, age, height, ethnicity; age is days from birth divided by 365.25. Higher is better respiratory function (p. 14). The page provides the self-identified-to-GLI race mapping: American Indian/Alaska Native and Native Hawaiian/Pacific Islander→Mixed/Other; Asian→South East Asian; Black/African American→African American; White/Unknown/Not reported→Caucasian; more than one race→Mixed/Other.
- **HHD/grip:** 3-5 maximum efforts, maximum force in pounds. Eleven muscles are tested bilaterally plus bilateral grip, for **24 muscle/muscle-group assessments**. Each nonzero-baseline muscle’s value becomes percentage change from baseline; percentages are averaged into upper-extremity, lower-extremity, and global averages; higher is better retention (pp. 14-15).
- **HHD0/HHD0[2]:** time from baseline to first/second post-baseline zero-strength occurrence in a muscle nonzero at baseline. They are composite endpoints with death/death-equivalent and are censored at completed Week 24 or earlier of Week-24-window end/date last known alive; larger times mean longer preservation (p. 15).
- **NfL:** serum and CSF NfL below the quantitation limit are imputed at the limit; serum/CSF NfL is log transformed for all analyses (p. 15).
- **Survival:** primary survival is death or death equivalent; secondary is death alone. Death equivalent is permanent assisted ventilation (PAV): >**22 hours/day** noninvasive or invasive mechanical ventilation for >**7 consecutive days**. PAV initiation is the first consecutive day, imputed to the fifteenth if only month known. Baseline PAV is censored at baseline for composite survival. Time at risk begins at baseline and ends at completed Week 24 or earlier Week-24-window end/date last known alive (p. 15).
- **King's ALS stage:** stages 1, 2, 3, 4a, 4b; bulbar involvement is an ALSFRS-R bulbar item <4, upper limb Q4 or Q5A <4, lower limb Q8 <4, nutrition failure gastrostomy for >50% nutrition, and respiratory failure Q10/R1=0 or Q12/R3<4 (p. 16).
- **DILI definitions:** ALT or AST >3×ULN with total bilirubin >1.5×ULN; ALT/AST >3×ULN with bilirubin >2×ULN; and the latter with ALP <2×ULN (potential Hy's law), all same-day values (pp. 16-17).

### Analysis sets and reporting rules (PDF pp. 12, 17-18)

- Continuous summaries: n, mean, median, SD, IQR, range. Categorical summaries: count, denominator, percentage (p. 12). Results normally use 3 significant figures; percentages 0.1 percentage point; P values: two digits if ≥0.095, three if 0.00095-<0.095, and `<0.001` if smaller (p. 12).
- One primary analysis: final significance criterion controls one-sided type-I error <0.025 absent early futility; secondaries use closed testing to two-sided FWER <0.05, with nominal comparison-wise P values reported (p. 12).
- Missing baseline outcome uses last observed pretreatment value. Missing baseline covariates use their mean (after transformation where relevant). An off-schedule early-termination value may replace the closest missed scheduled visit while preserving visit sequence; no other carry-forward (p. 12). Mixed-model estimates assume missing at random conditional on observed values (p. 13).
- **FAS:** focal-regimen randomized participants plus specified-regimen placebo participants with opportunity for placebo-controlled follow-up, analyzed as randomized; post-permanent-discontinuation observations retained if on study; post-data-lock observations excluded; persons not meeting ALS diagnostic criteria excluded (p. 17).
- **ECC:** FAS subset randomized from 180 days before the applicable regimen's first randomization through 180 days after its last, exclusive. **ERO:** FAS subset randomized within one regimen. **ECM:** FAS subset in regimens with same administration route. **EPP:** FAS subset initiating study treatment and meeting R-SAP compliance conditions, classified as treated; rules can truncate data for time-dependent events (p. 17).
- **STF:** initiated treatment in focal regimen plus eligible specified-regimen placebo initiators, analyzed as actually received; post-discontinuation observations retained if on study and post-data-lock observations excluded. **STN:** STF same-administration subset. **SRO:** STF regimen-only subset (pp. 17-18).

## Main estimands and planned statistical analyses

### Primary Bayesian shared-parameter analysis (PDF pp. 18, 33-41)

- **Matching key for main-paper results:** active versus placebo; FAS/primary ITT population; ALSFRS-R change through Week 24 plus composite death/death-equivalent survival; effect label **disease rate ratio (DRR)**. Match only if regimen, R-SAP/RSA, population, survival definition, time horizon, and model are the same.
- Primary estimand: relative rate of disease progression, active relative to placebo, assuming active treatment slows mean time to death/death equivalent by the same proportion as the mean ALSFRS-R functional progression rate. Population is FAS; variables are time to death/death equivalent and ALSFRS-R rate from baseline to Week 24. Death/death-equivalent excludes subsequent ALSFRS-R and is handled by composite strategy/mortality component. Other discontinuation uses treatment policy, retains post-discontinuation data, no post-treatment imputation, and assumes MAR. Population summary is mean ratio of active to placebo hazard/progression rate (p. 18).
- Primary population includes all active participants in analysis regimen, concurrent within-regimen control, and RSA-specified shared controls, excluding participants not meeting ALS diagnostic criteria. Function records are baseline/0, 4, 8, 12, 16, 20, 24 weeks plus substitute early-termination/off-schedule records; no function contribution after composite survival event. Concurrent shared controls are within six months = **180 days** before start or after finish of analysis-regimen randomization. Interim uses ongoing data; final excludes ongoing participants (pp. 34-35).
- Functional component is Bayesian repeated measures among survivors; mortality component is exponential proportional hazards to composite death/death-equivalent through 24 weeks. One shared treatment effect is common to function and mortality. ALSFRS-R visits are actual-week values rounded to nearest day. Model shown on p. 36: `Y_ij = (alpha_r(i),t(i) + gamma_i) - beta_i × exp(theta_t(i)+delta X_i+rho_d(i)+eta_r(i)) × (j×12/52) + epsilon_ij`; residual is normal with regimen/treatment-specific variance. Mortality hazard is `lambda_i = lambda_0 exp(theta_t(i))`.
- DRR = `exp(theta_T)`; placebo DRR=1 (`theta_0=0`). DRR<1 means slower function/mortality progression on active. DRR 0.75 means 25% slowing; 0.25 means 75% slowing. Active-treatment DRR prior is Uniform(0,2) (p. 37).
- Priors/parameters: arm-regimen mean baseline `alpha_R,T ~ Normal(38,10^2)`; participant intercept `gamma_i ~ Normal(0,sigma_gamma^2)`, `sigma_gamma ~ Uniform(0,10)`; slope `beta_i ~ Normal(mu_beta,sigma_beta,T(i)^2)`, `mu_beta ~ Normal(1,1^2)`, `sigma_beta,T ~ Uniform(0,2)` (p. 38). Nonanalysis regimen effect has `eta_r ~ Normal(0,sigma_eta^2)` and `1/sigma_eta^2 ~ Gamma(1,0.05^2)`; time trend uses `rho_0=0`, `rho_d ~ Normal(rho_d-1,sigma_rho^2)`, `sigma_rho~Uniform(0,2)` (p. 39). Covariates are time since onset, delta-FRS, baseline log NfL, baseline riluzole, edaravone, sodium phenylbutyrate/taurursodiol use; all mean centered, missing values mean imputed, transformed means post-transform; `delta_c ~ Normal(0,1^2)` (p. 39). Residual SD `sigma_R,T~Uniform(0,4)`; placebo monthly hazard `lambda_0~Gamma(0.01,1)` with stated mean 0.01, SD 0.1 (p. 40).
- Posterior uses MCMC with **at least 500,000** draws and thinning 10, with final count guided by convergence/effective sample size. Report mean and 95% credible interval for active DRR, `Pr(DRR<1)`, and `Pr(DRR<0.9)` (p. 40).
- Interims start when one regimen has **40 randomized participants** with opportunity for ≥24-week follow-up, then about every **12 weeks**. A regimen becomes eligible with 40 qualifying randomized; typical final analysis follows opportunity for Week 24 among **120 active and 40 control** participants (pp. 40-41). Default final success is `Pr[exp(theta_1)<1] > .979`; this was selected for 2.5% type-I error across null simulations except the slower-analysis-regimen scenario. Futility is `Pr[exp(theta_1)<.9] < .05` (p. 41).

### Secondary/supportive analyses (PDF pp. 19-30)

- Hierarchical sequence in FAS: (1) upper-limb HHD/grip average percent change among nonzero baseline manoeuvres at Week 24; (2) SVC percent predicted at Week 24 using GLI; (3) lower-limb HHD average percent change; (4) freedom from death/PAV baseline to Week 24. If primary Bayesian analysis is significant, each can be significant in sequence at two-sided P<0.05; following first failure, lower endpoints cannot be significant (p. 19).
- Repeated-measures model applies ALSFRS-R total/domain, HHD upper/lower/global percentage, SVC percent predicted, creatinine, NfL, weight across FAS/ECC/ERO/ECM/EPP. Fixed effects: visit, treatment, treatment×visit, onset and onset×visit, delta-FRS and interaction, baseline log-NfL and interaction, riluzole/edaravone/sodium phenylbutyrate-taurursodiol and interactions; covariance is unstructured. >3 contributing regimens gets random regimen intercepts; ≤3 gets fixed regimen effects. The primary contrast is adjusted active-placebo difference in Week-24 change with **95% Wald confidence bounds** (pp. 19-20). Its estimand is conditional-mean active-placebo difference in absolute Week-24 change in FAS, using treatment policy after discontinuation and MAR/no imputation, and positive difference in beneficial direction supports benefit (p. 21).
- Random-slopes model uses month since baseline = days×12/365.25, treatment×month, same covariates/interactions, participant random intercept/slope, and regimen random intercept/slope if >3 regimens (otherwise fixed regimen and regimen×month). Primary estimate is active-placebo slope difference with 95% Wald bounds; positive beneficial-direction slope difference supports benefit (pp. 21-23).
- Survival analyses cover FAS, ECC, ERO, ECM, EPP, STF, STN, SRO. Summarize endpoint proportion/time. If >10% reach endpoint, estimate time to 10% event with Kaplan-Meier and complementary-log-log confidence bounds. Compare log-rank; if each arm has ≥1 event, estimate unadjusted and covariate-adjusted Cox HR with profile likelihood bounds. Adjusted model covariates: age, time since onset, delta-FRS, log NfL, riluzole, edaravone, sodium phenylbutyrate/taurursodiol, plus random gamma regimen frailty dropped for nonconvergence/≤3 regimens (p. 23).
- **CAFS:** FAS/ECC/ERO/ECM/EPP joint rank of survival then functional change. Pair scores -1/0/1 and participant rank sums; inference via Wilcoxon rank-sum or covariate-adjusted rank-sum regression (p. 23). All combinations: survival death/death-equivalent or death alone; function ALSFRS-R/HHD upper/SVC/HHD lower; unadjusted t-approximate Wilcoxon or adjusted mixed model using onset, delta-FRS, log-NfL, medication covariates, with random regimen effect for ≥3 regimens or fixed otherwise (p. 24).
- HHD0/HHD0[2] compare interval-censored first/second zero strength by interval-censored nonparametric maximum likelihood and interval-censored Cox in FAS/ECC/ERO/ECM/EPP. First analysis has all 11 HHD muscles plus grip, up to 24 bilateral assessments; second selects four bilateral groups/grip most often reaching zero, up to 8 (p. 24).
- Placebo multiple imputation applies to ALSFRS-R, upper HHD%, SVC%, lower HHD% in FAS/ERO with **50** datasets. Earlier visits predict missing values via placebo-only linear regressions adjusted for onset, delta-FRS, log-NfL and medication covariates. Bounds: ALSFRS-R 0-48; HHD/SVC 0 to missing-indicator upper boundary (pp. 24-25).
- Sensitivity: robust linear mixed model with smoothed Huber rho and tuning for 95% asymptotic normal-data efficiency; composite death/24-week ALSFRS-R endpoint with exponential-tilting weights; subgroup random-slopes interactions; and placebo-control cross-regimen comparisons (pp. 25-26).
- Subgroups include age <65/≥65; female/male; white/minority with >5% prevalence; Hispanic/non-Hispanic; medication yes/no; BMI <25, 25-<30, ≥30 kg/m2; CKD eGFR ≥90, 60-89, <60 mL/min/1.73m2; delta-FRS median split; onset <18/≥18 months; early disease requiring all ALSFRS-R items ≥2, SVC ≥80% predicted, onset <24 months; bulbar/nonbulbar; median NfL; and site threshold ≥5 per arm. Unknown/missing one group; “other” is excluded if prevalence ≤5%. Report group estimate, within-level difference, pairwise difference-of-differences, and F test for >2 levels (pp. 25-26).
- Safety: TEAEs report event counts plus person counts/proportions; ≥5% term threshold for selected tabulations. Overall/≥5% TEAE incidence uses Poisson log-link regression, log-week exposure offset, rates per **100 participant-years**, delta-method 95% CIs (p. 27). ECG special-concern thresholds: QTcF >480 or >500 ms; QTcF rise >60 ms; PR rise >25% to >200 ms; HR rise >25% to <50 or >100 bpm; QRS rise >25% to >110 ms (p. 28). Study-drug exposure is days initiation-to-final-safety inclusive or initiation-to-withdrawal inclusive less interrupted intervals; individual missed doses are not subtracted unless logged (p. 29).
- Validation requires exact replication for integer counts (treatment/visit endpoint counts, events, affected and at-risk counts) and relative agreement within **0.1% of common mean** for estimates, SEs, confidence bounds, and P values (p. 30).

## Appendix I simulations and operating characteristics

### Simulation setup (PDF pp. 45-48)

- Simulation draws PRO-ACT placebo participants with ≥3 ALSFRS-R measurements across ≥24 weeks. The current subset has onset <3 years and SVC/FVC >50%, **N=2175**, mean participant slope **-1.03 ALSFRS-R points/month** (SD **0.76**), residual SE **1.77** (p. 45). Simulated visits: 0,4,8,12,16,20,24 weeks. Formula is displayed as `Y_i,j ~ Normal(gamma_i + (beta_i+theta_t(i))×(j×12/52), sigma_i^2)`, theta0=0 and theta1 selected so `(mean beta + theta1)/mean beta = 1 - assumed % slowing` (p. 45).
- Simulations use three concurrent regimens; other two are null. The document says **10,000 clinical trials** are simulated per scenario/treatment effect (pp. 46,48).
- Table 5.2.1 (pp. 46-47): accrual 40 participants/month (sensitivity 20,60); nonmortality dropout 2%/month (4%,6%); other-regimen enrollment 1 month apart (3,6); all-regimen ALSFRS-R slopes PRO-ACT (10% slower/less variable, 10% faster/more variable); measurement error PRO-ACT (10% less,10% more); analysis-regimen slope difference none (10% slower,10% faster); measurement-error difference none (10% less,10% more); 24-week mortality 5% (10%,20%).
- Table 5.2.2 (p. 47) treatment effects: Null 0% slowing/HR 1.0; common mortality/function benefit 25%/.75, 30%/.70, 35%/.65; no mortality benefit 30%/1.0; worse mortality 30%/1.3.

### Tables and figures containing numeric results (PDF pp. 49-61)

- **Table 6.1.1, Base scenarios with early futility (p. 49):** rows `% slowing, mortality HR, mean duration months, probability success, probability early futility, mean estimated DRR`: 0%,1,14,0.024,0.28,1.05; 25%,.75,15,0.61,0.01,0.75; 30%,.7,15,0.77,0.00,0.69; 35%,.65,15,0.88,0.00,0.64; 30%,1,15,0.72,0.00,0.71; 30%,1.3,15,0.68,0.01,0.72.
- **Table 6.1.2, observed DRR by duration/outcome (p. 49):** interim 1/7 months: early-futility mean 1.35, min 1.13; interim 2/10: 1.21, 1.08; interim 3/13: 1.16,1.05; final/16: success mean 0.65, maximum 0.82. The table labels DRR as `1 - % slowing`.
- **Table 6.2.1, mortality/function integration, no early futility (p. 50):** base 5% mortality: null type-I 0.024/mean DRR1.01; true DRR/HR .70 power .77/mean .69; functional .70, mortality 1.0 power .72/mean .71; functional .70, mortality 1.3 power .68/mean .72. At 10% mortality: 0.023/1.01; .77/.69; .67/.72; .57/.75. At 20%: .024/1.01; .77/.69; .56/.75; .35/.81.
- **Tables 6.2.2 and 6.2.3, simulated mortality example trials (p. 53; explanatory thresholds p. 52):** columns are placebo deaths, treatment deaths, mortality DRR(HR), function DRR, common DRR, CAFS P, posterior Pr(DRR<1). Table 6.2.2 (placebo deaths=18): treatment deaths 11/13/14/17/18/19/21/23/24/26/27/29; mortality DRR .68/.81/.87/1.04/1.10/1.15/1.27/1.36/1.41/1.48/1.52/1.58; function DRR .73/.72/.73/.73/.73/.73/.73/.71/.71/.71/.71/.73; common DRR .73/.73/.74/.76/.77/.78/.79/.80/.81/.82/.84/.88; CAFS P .002/.003/.005/.013/.015/.022/.028/.035/.056/.091/.135/.233; posterior .994/.991/.988/.982/.975/.973/.972/.956/.950/.948/.908/.853. Table 6.2.3 (placebo deaths=11): treatment deaths 6/7/8/9/10/11/12/13/14/16/17/19; mortality DRR .66/.77/.87/.96/1.06/1.13/1.21/1.27/1.33/1.45/1.49/1.57; function DRR .72/.72/.74/.74/.73/.74/.74/.73/.74/.73/.74/.75; common .71/.73/.74/.75/.75/.78/.78/.78/.80/.80/.82/.85; CAFS P .001/.003/.004/.006/.009/.013/.014/.017/.028/.036/.058/.085; posterior .998/.993/.992/.988/.982/.979/.976/.975/.961/.959/.939/.917. Asterisks are printed on the first four rows of Table 6.2.2 and first six rows of Table 6.2.3.
- **Figures 6.2.1-6.2.2 (pp. 54-55):** Example Trial 1 visual displays respectively 18 placebo/17 treatment deaths and 18 placebo/21 treatment deaths; no additional selectable text values beyond captions.
- **Table 6.3 (p. 56):** Base null type-I .024, mean DRR1.01; alternative DRR .70 power .77, mean .69. Analysis-regimen ALSFRS-R slower: .060,.96,.85,.66; faster: .010,1.05,.67,.72; lower residual error: .024,1.01,.79,.69; higher error: .023,1.01,.75,.69.
- **Figures 6.3.1-6.3.3 narrative values (pp. 57-60):** Figure 6.3.1 null trial: matched-control Week-24 mean about -4.5; other shared controls -6.5 and -7.2; shared-control DRR .73, posterior .990, CAFS one-sided P .0063; regimen-only DRR .91, posterior .683, CAFS P .5525. Figure 6.3.2 null: matched -4.0; others -7.0,-7.0; shared Bayesian DRR .90/posterior .714 and CAFS P .0026; regimen-only DRR 1.0/posterior .51/CAFS P .3675. Figure 6.3.3 positive: matched -5.9; others -5.9,-7.2; shared DRR .67/posterior .998/CAFS P .0088; regimen-only DRR .73/posterior .931/CAFS P .1102. Figure captions identify Figure 6.3.1 as null DRR=1.0 differences across regimens, 6.3.2 as null DRR=1.00, 6.3.3 as positive DRR=.70 with no differences.
- **Table 6.4 (p. 61):** rows `scenario: null type-I/mean DRR; alternative power/mean DRR`: Base .024/1.01; .77/.69. Slower accrual .025/1.01; .77/.69. Faster .020/1.01; .76/.69. 4% dropout .024/1.01; .74/.69. 6% .024/1.01; .71/.69. Regimen start 3 months apart .023/1.02; .67/.70. 6 months apart .021/1.03; .56/.71. ALSFRS-R slower all regimens .023/1.01; .75/.69. Faster .023/1.01; .78/.69. Lower residual error .023/1.01; .79/.69. Higher .023/1.01; .75/.69.

## Cross-source matching keys and limitations

- **Primary key:** HEALEY ALS Platform Trial, regimen-specific active versus placebo, FAS/primary shared-control ITT population, Week-24 ALSFRS-R plus survival composite, Bayesian shared-parameter DRR. A paper result with a different R-SAP/RSA, master protocol version, survival endpoint, population, or analysis time is not a direct numeric match.
- **Secondary keys:** Week-24 repeated-measures active-placebo mean difference (95% Wald CI); random-slopes active-placebo slope difference; Cox HR/time-to-10%-event survival analysis; CAFS death/death-equivalent or death-alone plus designated functional endpoint; HHD0/HHD0[2]; placebo multiple imputation; subgroup interaction estimates.
- **Support-specific limitation:** pp. 45-61 report simulated operating characteristics and example trials, not observed RGC or paper participant outcomes. Figures 6.2.1-6.3.3 were text-mapped from captions and nearby narrative; their graphical plotted coordinates are not independently transcribed. No OCR was needed because direct text was usable.

---

### PDF pp. 66-130

# Support quantitative evidence map — support-005

## Scope, authority, and extraction record

- **Direct source:** `joi240158supp2_prod_1742927563.7711.pdf` (DOC-003), PDF pp. 66-130 only.
- **Direct-source authority:** the supplied PDF. The range contains the March 17, 2022 R-SAP Version 1.0 on PDF pp. 66-93 and the later July 22, 2022 R-SAP Version 3.0 on PDF pp. 94-130. Version 3.0 is the later plan; Version 1.0 and the revision history remain mapped as versioned matching context, not discarded.
- **Fresh direct extraction:** `pdftotext -f 66 -l 130` and `pdftotext -layout -f 66 -l 130`; outputs are `preprocessing/support-005/doc003_p066_p130_native.txt` and `preprocessing/support-005/doc003_p066_p130_layout.txt`.
- **Targeted visual confirmation:** direct PDF renders of pp. 106, 120, and 122 confirm the schedule layout and the printed repeated-measures and random-slopes equations. No OCR was required because the native/layout text was readable.
- **Boundary:** this is an evidence and definitions map only. It does not diagnose or register candidates.

## Page-complete applicability record

| PDF pages | Version / content | Applicability record |
|---|---|---|
| 66-68 | Version 1.0 abbreviations | No reported results. Definitions/labels only (e.g., FAS, EPP, R-SAP, SVC, TEAE); retained as label keys. |
| 69-70 | Version 1.0 table of contents | No result-relevant quantitative content beyond the section-location map. |
| 71-93 | Version 1.0 R-SAP body | Result-relevant planned endpoints, estimands, definitions, analysis sets, formulas, sensitivity/subgroup rules, and safety/disposition summary rules mapped below. |
| 94-95 | Version 3.0 title/approval pages | Administrative version identifiers only; no reported results or quantitative relationship. |
| 96-98 | Version 3.0 revision history | Result-relevant change log; maps changed survival time points, CAFS/supportive analyses, endpoint labels, formulas, covariates, and analysis-set rules. |
| 99-101 | Version 3.0 abbreviations | No reported results. Definitions/labels only, including DRR, ECM, SI, p75[ECD], PAV, STF, SVC, TEAE, and ULN. |
| 102-103 | Version 3.0 table of contents | No result-relevant quantitative content beyond the section-location map. |
| 104-130 | Version 3.0 R-SAP body | Result-relevant planned endpoints, estimands, definitions, models, formulas, sensitivity/subgroup rules, safety, and disposition summary rules mapped below. |

All 65 assigned PDF page units are mapped. Pages explicitly with no applicable result-relevant content are 66-70, 94-95, and 99-103; their administrative/label role is recorded above.

## Cross-source matching keys

Use these keys only after matching population, timing, contrast, analysis version, and precision in the main paper. Main-paper match candidates are: pooled active CNM-Au8 (30 mg/d plus 60 mg/d) versus placebo; individual 30 mg/d or 60 mg/d versus placebo; FAS/ITT and shared-placebo populations; Week 24 placebo-controlled period; ALSFRS-R total score/change/slope; DRR; CAFS; SVC percent-predicted/change; survival/PAV-free survival/death equivalent; HHD/HHD0/HHD02; ALSAQ-40 domains/SI; CNS-BFS; FVC/home spirometry; serum/CSF NfL; urinary p75[ECD]; adverse-event incidence rate per 100 participant-years; and safety-laboratory alert thresholds. Version 3.0 is the primary planned-specification key.

## Versioned study-design and endpoint relationships

### Allocation, dose, schedule, population, and timing

- **PDF pp. 71-75 (V1.0) and pp. 104-108 (V3.0):** RGC compares orally administered CNM-Au8 30 mg/d and 60 mg/d with placebo. Randomization is **3:3:2**, stratified by riluzole use, edaravone use, both, or neither. The active pooled comparison is both dosage groups versus placebo; individual-dose comparisons are exploratory (pp. 76 and 109).
- **PDF pp. 72-74 and pp. 105-107:** Each bottle is 60 mL. The 30-mg/d formulation is 250 micrograms/mL, 15 mg per bottle; the 60-mg/d formulation is 500 micrograms/mL, 30 mg per bottle. A normal dose is two 60-mL bottles daily; one bottle daily is permitted after down-titration. The schedule runs Baseline/Day 0, Week 2 (Day 14 plus/minus 3), Week 4 (Day 28 plus/minus 7), Week 8 (Day 56 plus/minus 7), Week 12 (Day 84 plus/minus 3), Week 16 (Day 112 plus/minus 7), Week 20 (Day 140 plus/minus 3), Week 24 (Day 168 plus/minus 7), and a final call 28 days after last dose plus/minus 3 days. Table footnotes specify that blood/urine samples are collected before the first daily dose; whole blood and urine only at Baseline and Week 24/early termination; home voice recording is twice weekly outside clinic visits.
- **PDF pp. 76-77 and pp. 109-110:** Primary endpoint is ALSFRS-R total score. Key secondary endpoints are CAFS, SVC change, and survival (time to death or death equivalent). Exploratory outcomes include ALSFRS-R domains; HHD percentages/HHD0/HHD02; listed voice metrics; biofluid biomarkers; ALSAQ-40 and CNS-BFS; CNM-Au8 concentration/PD measures; home spirometry; specified time-to-event composites; a composite standardized slope; and the time to a 6-point ALSFRS-R decline. Safety alert thresholds are ALT or AST >3 times ULN, creatinine >1.5 times baseline, and platelet count <75,000/mm3.

### Outcome definitions, units, formulas, and censoring

- **ALSFRS-R / delta-FRS — PDF p. 77 (V1.0); p. 111 (V3.0):** pre-baseline slope is `(48 - baseline ALSFRS-R total score) / months from onset of symptomatic weakness to Baseline`. V3.0 defines months as `days from onset to Baseline × 12 / 365.25` and imputes an imprecise onset date as the fifteenth day of its month. Time to a 6-point decline is a composite with death/death equivalent, whichever occurs first, censored at the last ALSFRS-R assessment through the Week 24 window.
- **SVC and home FVC — PDF p. 78 (V1.0); p. 111 (V3.0):** age is `days from birth to assessment / 365.25`; GLI race correspondence is American Indian/Alaska Native, Native Hawaiian/Pacific Islander, or multiple race to Mixed/Other; Asian to South East Asian; Black/African American to African American; White, Unknown, and Not reported to Caucasian. Home spirometry uses 3-8 coached maneuvers; maximum accepted FVC is converted to percent-predicted using GLI sex, age, screening height, and race norms. Higher percent-predicted values indicate better respiratory function.
- **HHD — PDF p. 78 (V1.0); p. 112 (V3.0):** HHD0 is a death/death-equivalent composite. HHD02 is time from Baseline to the second post-baseline zero-strength recording in a muscle nonzero at baseline, or death/death equivalent first; both are censored at the last HHD assessment through Week 24 and are exploratory.
- **Voice and biomarker measurement — PDF pp. 79, 112:** voice task counts are 5 prespecified sentences and 5 randomly selected sentences, plus consonant-vowel repetition, sustained phonation, and a single-breath count; metrics are maximum phonation time, pause rate, breathy quality, pitch instability, voicing regulation, articulatory precision, speaking rate, articulation rate, and monotonicity. V3.0 adds a baseline predicted vital capacity from voice plus age, sex, race, height, and weight. V3.0 biomarker definitions: serum creatinine (kinetic Jaffe), serum/CSF NfL (Simoa), and urinary p75[ECD] (sandwich ELISA), with p75[ECD] normalized to urinary creatinine; values below quantitation for NfL/p75[ECD] are imputed at the limit of quantitation; serum/CSF NfL is log-transformed.
- **ALSAQ-40 — PDF p. 112:** each of five domains is mean completed domain items ×25 (range 0-100); a domain is missing if >20% of items are missing, otherwise missing items are mean-imputed from completed same-assessment items. SI is the mean of five domain scores and is missing if any domain is missing. Higher values mean worse quality of life.
- **Survival and PAV — PDF pp. 79, 113:** PAV means >22 hours/day noninvasive or invasive ventilation for >7 consecutive days. V3.0 imputes an imprecise PAV initiation date to the fifteenth of the month. Death/death-equivalent and death-alone risks begin at Baseline and are evaluated at Week 24 and later assessment approximately at last RGC participant placebo-controlled follow-up; primary survival analysis is PAV-free survival to Week 24.
- **King's stage and clinical events — PDF pp. 80, 113-114:** King's scale uses stages 1-3 for number of involved CNS regions and 4a/4b for nutritional/respiratory failure. Threshold labels: bulbar question 1/2/3 <4; upper limb question 4 or 5A <4; lower limb question 8 <4; nutrition gastrostomy >50%; respiratory question 10/R-1 =0 or question 12/R-3 <4. Clinical-event risks begin at Baseline; relevant pre-existing events exclude participants as applicable; death/death-equivalent is an outcome in each composite. Censoring is Week 24 if completed, consent withdrawal, or last known endpoint status before Week-24-window end; King's stage 4a/4b is interval-censored between ALSFRS-R assessments.
- **PK and safety laboratory definitions — PDF pp. 81, 114-115:** V1.0 riluzole sample plan: first 40 riluzole users reaching Week 8 plus 10 nonusers at Baseline, with HPLC/UV at 263 nm. V3.0 specifies LC/MS/MS (Covance M10125, Study 8454-985). DILI criteria require same-day measures: ALT/AST >3×ULN plus TBL >1.5×ULN; ALT/AST >3×ULN plus TBL >2×ULN; and ALT/AST >3×ULN plus TBL >2×ULN with ALP <2×ULN (potential Hy's law).

## Analysis populations, estimands, and inferential definitions

- **Analysis sets — PDF p. 82 (V1.0); pp. 115-116 (V3.0):** FAS is randomized RGC plus specified-regimen placebo, by randomized treatment; post-discontinuation observations may remain, post-data-lock observations are excluded, and non-ALS diagnoses are excluded. STF is treated RGC plus eligible shared placebo by actual treatment. V3.0 defines ECM as the FAS subset with orally administered regimen study drug. EPP is treated FAS without protocol deviations affecting scientific integrity; V3.0 specifies truncation rules, including clinical events through 28 days after a dosing-nonadherence censoring event. FAS/ECM/EPP/STF/STN include shared placebo from regimens A/B/D; only B/D contribute to ECM/STN because A is subcutaneous and B/D oral.
- **Primary DRR — PDF p. 83 (V1.0); pp. 116-117 (V3.0):** Bayesian shared-parameter repeated-measures ALSFRS-R model that incorporates mortality; primary FAS, sensitivity ERO (and ECM in V3.0), supportive EPP. Estimand: pooled active 30/60 mg/d relative rate of disease progression versus placebo, assuming proportional slowing of mean time to death/death equivalent and mean ALSFRS-R progression. Variables: death/death equivalent time and ALSFRS-R change through Week 24. Mortality uses a composite-variable strategy; nondeath discontinuation uses treatment policy; post-treatment missing data are not imputed and are missing at random. Summary is mean ratio of active-to-placebo hazard or progression rate. Futility stopping is possible; no early success stop.
- **Multiplicity — PDF p. 84 (V1.0); pp. 117-118 (V3.0):** hierarchy CAFS, then SVC, then survival; conditional on significant primary DRR, successive two-sided `p < 0.05`, stopping declarations after first nonsignificant result. Stated familywise type-I error is 5%; nominal comparison-wise p values also reported.
- **CAFS — PDF pp. 84-85 (V1.0); pp. 118-119 (V3.0):** pairwise rank first by death/death-equivalent time, otherwise absolute ALSFRS-R change at last jointly observed visit. Population FAS; pooled active versus placebo; estimand is the stochastic probability active ranks higher; summary difference in mean ranks. V1 uses Wilcoxon `proc npar1way`. V3 primary code is adjusted `proc mixed` with sx2bl, dFRS, baseline riluzole, baseline edaravone, treatment, one-sided upper confidence bound; Rank is sum of -1/0/1 pairwise ranks. V3 supporting analyses use SVC, multiple imputation for early termination/withdrawal/loss, death alone, specified covariate adjustments including NfL, and unadjusted last-jointly-observed comparisons.
- **Repeated-measures model — PDF p. 85 (V1.0); pp. 119-121 (V3.0):** continuous endpoints include ALSFRS-R, HHD percentages, SVC, home FVC, creatinine, NfL, ALSAQ-40, CNS-BFS; V3 adds urinary p75[ECD] and ALSAQ-40 domains/SI. V3 fixed effects are discrete visit, three-level treatment, treatment×visit, and centered symptom-onset time/delta-FRS/riluzole/edaravone with visit interactions; random regimen intercept, participant unstructured repeated covariance; REML. Equation 1: `Yij = ak(i) + gamma1 ti + gamma2,j vj + gamma3' zi + gamma4,j ti vj + gamma5,j' zi vj + epsilonij`; `ak ~ N(0, sigma_r^2)`, residual vector `~ N(0,R)`, and `Cov(bk(i),epsilonij)=0`. Primary estimate is adjusted active-versus-placebo 24-week change with 95% Wald bounds. V3 contrast uses weights `2 0 0 -2; -1 0 0 1; -1 0 0 1`, divisor 2. Post-discontinuation data remain; death-related missingness is not imputed (MAR). NfL supportive analysis adds centered NfL and NfL×visit.
- **Survival — PDF pp. 85-86 (V1.0); pp. 121-122 (V3.0):** pooled active FAS death/death-equivalent endpoint; log-rank estimand is deviation in expected survival times, summary difference in survival curves; post-treatment missingness not imputed under MCAR. If log-rank significant, direction is interpreted with unadjusted Cox hazard ratio. V3 includes baseline age in adjusted models and ECM in analysis sets. Listings use study day of death/death equivalent/last known alive.
- **Random slopes — PDF pp. 86-87 (V1.0); pp. 122-123 (V3.0):** target is active-versus-placebo difference in conditional mean slope through Week 24. V3 uses month `days ×12/365.25`, treatment and covariate-by-month terms, random regimen and participant intercepts/slopes with unstructured covariance. Equation 2: `Yij = gamma1 + a0k(i) + b0i + gamma2 ti + gamma3'zi + (gamma4 + a1k(i) + b1i + gamma5 ti + gamma6'zi)mij + epsilonij`; regimen and participant random-effect covariance matrices are Sigma_r and Sigma_p, residual variance sigma_e^2, and all are uncorrelated. Contrast is treatment×month `-2 1 1`, divisor 2, with 95% Wald bounds. V3 adds NfL and NfL×month in a supportive clinical-endpoint model.
- **Clinical-event, composite, voice, MI, subgroup analyses — PDF pp. 87-89 (V1.0); pp. 123-126 (V3.0):** clinical events are survival-parallel analyses with interval censoring for King's stage and 6-point ALSFRS-R decline; King's stage is stratified by baseline stage. The composite standardizes each participant's ALSFRS-R/SVC/ALSAQ-40 random slope to mean 0, variance 1 then averages them; it uses ANOVA/least-squares contrasts, and V3 adjusts symptom-onset time, delta-FRS, riluzole, edaravone, optionally NfL. Voice B-spline model has knots 8/16 weeks, four fixed B-spline terms, three treatment levels, random regimen intercept/slopes, five random participant B-splines, AR(1) residuals, specified fallback covariance simplifications, 24-week active-placebo adjusted-mean contrast, 95% Wald bounds, and V3 NfL support. Placebo MI uses 50 imputations, sequential FCS regression at Week 8/16/24, placebo-only MNAR model observations, with ALSFRS-R bounds 0-48. Subgroups include detailed age, sex, race/ethnicity, weight/BMI, CKD/eGFR, onset timing, baseline scores, SVC, urate, NfL, delta-FRS, site (and V3 onset site) thresholds on pp. 89/126; unknown/missing is a group, other retained only if >5% except TEAE subgroups, and convergence fallbacks are specified.

## Safety, rates, proportions, and other planned summary relationships

- **PDF pp. 90-91 (V1.0); pp. 127-128 (V3.0):** CNM-Au8 concentrations below quantitation are replaced by half the lower limit. Summary measures: N, N/% BLQ, arithmetic mean, median, SD, min/max, geometric mean, geometric CV `sqrt(exp(variance(log concentration))-1)`, and 95% geometric-mean confidence bounds under log normality. Cmax versus ALSFRS-R slope is exploratory. TEAE window is first double-blind dose through final safety visit, death, 28 days after last dose (early termination/loss), or first OLE dose; COVID interval is 5 days before symptom onset to symptom resolution or earlier 91 days after onset/end of double-blind follow-up. TEAE proportions are not tested. TEAE incidence-rate differences—not ratios—are reported per 100 participant-years, with comparison-wise 95% CIs from delta-method variance.
- **PDF pp. 91, 128:** safety-laboratory shift tables classify CTCAE v5.0 toxicity, include maximum postbaseline toxicity and visit-specific shifts. Per treatment/safety sample, proportions with ALT >3×ULN, AST >3×ULN, creatinine >1.5× baseline, platelets <75,000/mm3, or any of these are tabulated versus baseline; absolute values and change from baseline use mean, SD, median, and range.
- **PDF pp. 91-93 and pp. 128-130:** disposition summarizes consent, screening failure, nonassignment/nonrandomization, death/withdrawal/termination/loss, 24-week completion, and safety-follow-up/OLE by stated populations. Exposure is calculated three ways: initiation to final safety assessment inclusive; initiation to withdrawal inclusive less interruption intervals (individual missed doses generally not subtracted); and initiation to earlier final placebo-period contact or 28 days post-last dose inclusive. Blindedness uses Fisher exact testing for active-treatment guesses, overall and among at-least-somewhat-sure respondents, and confidence bounds for proportion differences. Protocol deviations and COVID-missed assessments are summarized by treatment group/type/visit as stated.

## Version linkage and matching caution

The V3.0 revision history (PDF pp. 96-98) explicitly changes the V1.0 specification: dual survival time points and Week-24 PAV-free primary survival; added CAFS/SVC supportive and imputed analyses; detailed delta-FRS and ALSAQ-40/SI calculations; ECM and EPP handling; adjusted CAFS; removal of shared-baseline treatment assumptions; NfL covariate analyses; and MI FCS. When comparing a main-paper result with the supplement, match it to the effective V3.0 endpoint, population, covariate set, analysis set, and Week-24/later time point before treating any difference as a relationship for checking.

## Limitations / gaps

No scientific-coverage gap within pp. 66-130. The R-SAP is a planned-analysis source; it contains no realized treatment-effect result tables in this page range. Several details are delegated to the M-SAP, MPRDR, PK plan, PD plan, or separate reports, which are named source dependencies rather than inferred here.

---

## DOC-004 pp. 1-26; DOC-005 pp. 1-6; DOC-006 p. 1

# Support Quantitative Evidence Map — support-006

## Scope, method, and completion

- **Assigned direct-source units:** DOC-004 `joi240158supp3_prod_1742927563.7911.pdf`, PDF pp. 1-26 (reusable-backed); DOC-005 `joi240158supp4_prod_1742927563.8061.pdf`, PDF pp. 1-6 (fresh-required); and DOC-006 `joi240158supp5_prod_1742927563.8111.pdf`, PDF p. 1 (fresh-required).
- **Completed units:** 33/33 PDF pages. DOC-004 reusable page-native text was read completely and table/figure pages were checked against direct-PDF text and fresh 120-dpi source renders (pp. 14-25). DOC-005 and DOC-006 were freshly extracted from the direct PDFs with `pdftotext` native and layout modes; their fresh layout/native files are under `preprocessing/support-006/`.
- **Evidence convention:** every PDF location below is a physical PDF page (not the printed supplemental page number). This is an evidence map, not a candidate diagnosis. Values are transcribed as displayed; a zero P value is not present in this shard.
- **Main-paper matching keys:** `HEALEY ALS Platform Trial; Regimen C (CNM-Au8); CNM-Au8 pooled active versus shared placebo; FAS; ERO/regimen-only; ALSFRS-R; SVC; PAV; DRR; serum/plasma NfL; TEAE`.

## DOC-004: eMethods, result tables, and eFigure

### Administrative/protocol and analysis definitions (pp. 1-13)

- **p. 1:** contents page: eMethods; eTables 1-5; eFigure. This page contains no result values beyond the contents labels.
- **pp. 2-4, Trial design/randomization/intervention:** randomized, double-blind, placebo-controlled Regimen C at 54 NEALS centers, enrolled July 2020-March 2022. Eligibility includes ALS disease duration **<=36 months** and vital capacity **>=50% predicted**. Regimen allocation and within-regimen treatment schedules were stratified by riluzole/edaravone use (**4 strata**); treatment blocks were size **8** (**3** 30-mg, **3** 60-mg, **2** placebo). Allocation was **3:3:2** to 60 mg, 30 mg, and placebo. Trial duration **24 weeks**; clinic weeks **0, 4, 8, 16, 24**, telephone weeks **2, 12, 20**, final telephone follow-up week **28**. Each daily dose used two **60-mL** bottles; each contained **30 mg** for the 60-mg dose or **15 mg** for the 30-mg dose.
- **pp. 5-7, endpoints/populations:** primary endpoint is change from baseline through 24 weeks in ALSFRS-R plus survival, modeled jointly. Secondary outcomes in hierarchy: (1) CAFS, joint rank of ALSFRS-R decline and survival free of PAV; PAV means ventilation **>22 h/day for >7 days**; (2) percent-predicted-normal SVC decline; (3) survival free of PAV. The primary combined-dose analysis compares 30-mg plus 60-mg CNM-Au8 with placebo; dose-specific analyses are prespecified exploratory. FAS includes all Regimen-C active, Regimen-C placebo, and placebo from Regimens A/B/D; regimen-only analyses include Regimen-C participants. Safety FAS excludes shared-placebo participants known ineligible because of gold allergy. Longitudinal primary-analysis visits are weeks **0, 4, 8, 12, 16, 20, 24** (early termination/ad hoc visits may substitute).
- **pp. 7-9, primary model/statistical definition:** Bayesian shared-parameter function/survival model. Disease rate ratio (DRR) is the ALSFRS-R-slope ratio in the functional component and hazard ratio in the survival component; **DRR <1** indicates slower progression and **DRR 0.50** denotes **50%** slowing. Illustrations: 6-point decline over 6 months in control would occur over 12 months at DRR 0.50; median survival 9 months in control would be 18 months at DRR 0.50. Function component: covariate-adjusted linear repeated-measures model; survival component: exponential proportional-hazards model; shared controls handled in Bayesian hierarchical meta-analytic framework. MCMC used **at least 500,000** posterior samples with thinning **10**. Futility interim starts at **40** randomized active participants (**30** active, **10** placebo), every **12 weeks** thereafter; stop if posterior probability is **<5%** that CNM-Au8 slows ALSFRS-R decline by **>=10%**. No early-success rule.
- **pp. 10-12, secondary/exploratory statistical definitions:** SVC is assessed with repeated-measures linear mixed and random-slopes models (months since onset, prebaseline delta-FRS, baseline riluzole/edaravone and time interactions; FAS models include random regimen-specific intercepts). Death, PAV/death-equivalent, and hospitalization are Cox proportional-hazards outcomes with delta-FRS, onset months, riluzole, edaravone, and age; a supportive analysis adds baseline serum NfL and NfL-by-visit. Serum Simoa testing uses two replicates; repeats occur for below-detection/one replicate or replicate CV **>25%**; <LOQ values are imputed with assay LOD. NfL is log transformed before analysis. Serum NfL FAS is prespecified but a regimen-only analysis is reported because plates differed; plasma NfL is described as post hoc. MMRM covariates are delta-FRS, onset months, riluzole, edaravone, covariate-by-visit and treatment-by-visit. Prespecified neurofilament analysis excludes no outliers; a post-hoc sensitivity exclusion (<**4 pg/mL** or <**2%** of a participant maximum) removes **one** placebo baseline NfL observation. Exploratory time-to-event Cox analyses include hospitalization, feeding tube, assisted ventilation, King stage 4, death, and death/PAV; King stage is interval censored, other variables right censored.
- **p. 13, subgroup model:** prespecified subgroups are riluzole, edaravone, age (<65/65+), sex, race, ethnicity, weight, BMI, chronic kidney disease, onset (<18/18+ months), El Escorial/onset, symptom severity, early disease, urate (<5.5/>=5.5 mg/dL), serum NfL median split, site of onset, delta-FRS median split, and site (sites with <5 pooled). A random-slopes model includes subgroup, subgroup-by-time, and subgroup-by-treatment-by-time for primary/secondary efficacy endpoints.

### eTable 1 — ALSFRS-R observed distribution (p. 14)

Table columns are CNM-Au8 pooled, shared placebo, and regimen placebo, each as **n; mean (SD)**. Values by visit are:

| Visit | CNM-Au8 pooled | Shared placebo | Regimen placebo |
|---|---|---|---|
| Baseline | 120; 34.3 (6.6) | 164; 35.1 (6.7) | 41; 36.1 (5.9) |
| Week 4 | 120; 33.0 (7.0) | 160; 34.5 (7.0) | 40; 35.4 (6.7) |
| Week 8 | 115; 32.3 (7.3) | 155; 33.4 (7.4) | 38; 34.3 (7.1) |
| Week 12 | 115; 31.4 (7.7) | 152; 32.7 (7.9) | 39; 33.7 (7.9) |
| Week 16 | 110; 30.5 (7.7) | 148; 31.8 (8.3) | 36; 32.5 (7.5) |
| Week 20 | 111; 29.7 (7.8) | 143; 31.2 (8.6) | 36; 32.6 (7.9) |
| Week 24 | 111; 29.1 (7.9) | 143; 30.2 (8.7) | 35; 31.4 (8.2) |

### eTable 2 — Bayesian shared-parameter primary efficacy analysis (p. 15)

| Parameter | Median | Mean (SD) | 95% credible interval | Pr(DRR <1.0) | Pr(DRR <0.9) |
|---|---:|---:|---|---:|---:|
| DRR, function and mortality | 0.96 | 0.97 (0.099) | (0.783, 1.175) | 0.6450 | 0.2505 |
| ALSFRS-R slope, Regimen-C placebo with sharing (points/month) | -1.03 | -1.03 (0.073) | (-1.181, -0.894) | — | — |
| ALSFRS-R slope, pooled CNM-Au8 (points/month) | -1.00 | -1.00 (0.075) | (-1.143, -0.847) | — | — |
| Mortality event rate, shared placebo (events/month) | 0.010 | 0.010 (0.0026) | (0.0054, 0.0154) | — | — |
| Mortality event rate, pooled CNM-Au8 (events/month) | 0.009 | 0.009 (0.0025) | (0.0052, 0.0150) | — | — |
| Covariate: months since onset | 1.03 | 1.03 (0.046) | (0.938, 1.120) | — | — |
| Covariate: prebaseline slope | 1.39 | 1.40 (0.079) | (1.255, 1.565) | — | — |
| Covariate: edaravone use | 1.13 | 1.13 (0.101) | (0.949, 1.344) | — | — |
| Covariate: riluzole use | 1.03 | 1.03 (0.093) | (0.854, 1.220) | — | — |

Footnote/label: DRR = disease rate ratio. Model covariates: baseline edaravone, baseline riluzole, months since symptom onset, and prebaseline ALSFRS-R slope.

### eTable 3A — FAS repeated-measures secondary/exploratory results (p. 16)

Outcome columns are 24-week change estimate by active and shared placebo, then active minus shared-placebo difference (SE), 95% CI, P value.

| Contrast and endpoint | Active change | Shared-placebo change | Difference (SE) | 95% CI | P |
|---|---:|---:|---:|---|---:|
| Pooled CNM-Au8 (n=120) vs shared placebo (n=164): ALSFRS-R total score | -5.47 (0.43) | -5.51 (0.36) | 0.0 (0.55) | -1.03, 1.11 | 0.94 |
| Pooled: SVC (% predicted) | -9.32 (1.36) | -8.53 (1.15) | -0.78 (1.77) | -4.25, 2.68 | 0.66 |
| CNM-Au8 30 mg (n=59) vs shared placebo (n=164): ALSFRS-R | -5.70 (0.59) | -5.51 (0.36) | -0.19 (0.69) | -1.53, 1.16 | 0.79 |
| 30 mg: SVC (% predicted) | -7.84 (1.84) | -8.53 (1.15) | 0.69 (2.19) | -3.55, 4.92 | 0.75 |
| CNM-Au8 60 mg (n=61) vs shared placebo (n=164): ALSFRS-R | -5.24 (0.59) | -5.51 (0.36) | 0.27 (0.68) | -1.07, 1.60 | 0.69 |
| 60 mg: SVC (% predicted) | -10.79 (1.99) | -8.53 (1.15) | -2.26 (2.29) | -6.75, 2.24 | 0.33 |

### eTable 3B — ERO/regimen-only repeated-measures results (p. 17)

| Contrast and endpoint | Active change | Regimen-placebo change | Difference (SE, if shown) | 95% CI | P |
|---|---:|---:|---:|---|---:|
| Pooled CNM-Au8 (n=120) vs regimen placebo (n=41): ALSFRS-R | -5.45 (0.44) | -5.39 (0.71) | -0.07 (0.83) | -1.71, 1.57 | 0.94 |
| Pooled: SVC (% predicted) | -9.57 (1.38) | -6.74 (2.29) | -2.83 (2.67) | -8.10, 2.44 | 0.29 |
| Pooled: plasma NfL (% change) | -2.3 | 7.9 | -9.5 | -18.0, 0 | 0.04 |
| Pooled: serum NfL (% change) | 0.4 | 26.8 | -26.4 | -50.3, -2.6 | 0.03 |
| CNM-Au8 30 mg (n=59): ALSFRS-R | -5.56 (0.60) | -5.39 (0.71) | -0.17 (0.93) | -2.00, 1.66 | 0.85 |
| 30 mg: SVC (% predicted) | -7.61 (1.86) | -6.74 (2.29) | -0.87 (2.94) | -6.69, 4.95 | 0.77 |
| 30 mg: plasma NfL (% change) | -1.3 | 7.9 | -8.5 | -18, 2 | 0.10 |
| 30 mg: serum NfL (% change) | 1.4 | 26.8 | -25.5 | -52.2, 1.3 | 0.06 |
| CNM-Au8 60 mg (n=61): ALSFRS-R | -5.35 (0.61) | -5.39 (0.71) | 0.04 (0.93) | -1.79, 1.87 | 0.97 |
| 60 mg: SVC (% predicted) | -11.53 (1.98) | -6.74 (2.29) | -4.79 (3.03) | -10.76, 1.19 | 0.12 |
| 60 mg: plasma NfL (% change) | -3.4 | 7.9 | -10.5 | -20, 0 | 0.04 |
| 60 mg: serum NfL (% change) | -0.5 | 26.8 | -27.4 | -45.1, -0.7 | 0.05 |

Footnote/labels: FAS includes shared placebos; ERO includes regimen-specific placebo only. ALSFRS-R, SVC, CI, SE, and NfL are defined in the source; `GMR – geometric mean ratio`. Serum/plasma NfL were modeled on a log scale then exponentiated to original scale. Models adjust for time since symptom onset, prebaseline ALSFRS-R slope, baseline edaravone, baseline riluzole, and their interactions with visit.

### eTable 4 — subgroup forest plot, pooled CNM-Au8 versus shared placebo (pp. 18-20)

Measure is ALSFRS-R slope (points/month) with displayed interval; difference is active minus placebo slope with 95% CI. The caption states that every subgroup CI crosses no difference. The P values displayed on selected subgroup headings are interaction/group-comparison P values as laid out in the source.

| Subgroup level | CNM-Au8 slope | Placebo slope | Difference (95% CI) | P if displayed |
|---|---|---|---|---:|
| All participants | -0.98 (-1.13,-0.82) | -1.01 (-1.13,-0.88) | 0.03 (-0.16,0.23) | — |
| Riluzole N / Y | -1.07 (-1.39,-0.75) / -0.95 (-1.12,-0.78) | -0.88 (-1.15,-0.61) / -1.05 (-1.19,-0.90) | -0.19 (-0.60,0.22) / 0.10 (-0.12,0.32) | 0.22 |
| Edaravone N / Y | -1.00 (-1.17,-0.83) / -0.91 (-1.22,-0.60) | -0.96 (-1.10,-0.81) / -1.17 (-1.43,-0.90) | -0.04 (-0.27,0.18) / 0.26 (-0.14,0.66) | 0.19 |
| Neither / riluzole only / edaravone only / both | -1.15 (-1.49,-0.81) / -0.94 (-1.14,-0.75) / -0.49 (-1.45,0.47) / -0.96 (-1.28,-0.64) | -0.82 (-1.10,-0.54) / -1.01 (-1.18,-0.83) / -1.38 (-2.27,-0.49) / -1.15 (-1.43,-0.88) | -0.33 (-0.77,0.10) / 0.06 (-0.20,0.32) / 0.89 (-0.42,2.20) / 0.19 (-0.23,0.61) | — |
| Age <65 / >=65 | -0.97 (-1.15,-0.80) / -0.95 (-1.23,-0.68) | -1.03 (-1.18,-0.88) / -0.95 (-1.19,-0.71) | 0.05 (-0.18,0.28) / 0.00 (-0.36,0.36) | 0.81 |
| Sex F / M | -0.98 (-1.22,-0.74) / -0.99 (-1.18,-0.80) | -1.10 (-1.33,-0.87) / -0.97 (-1.12,-0.81) | 0.12 (-0.21,0.45) / -0.02 (-0.27,0.22) | 0.50 |
| Race: White | -0.95 (-1.10,-0.80) | -1.01 (-1.14,-0.88) | 0.06 (-0.14,0.25) | — |
| Ethnicity: not Hispanic/Latino | -0.97 (-1.13,-0.82) | -1.01 (-1.14,-0.88) | 0.04 (-0.16,0.24) | — |
| Weight <56 / 56-<77 / 77-<150 kg | -1.39 (-2.02,-0.76) / -0.93 (-1.18,-0.68) / -0.95 (-1.14,-0.75) | -1.14 (-1.73,-0.55) / -1.04 (-1.25,-0.83) / -0.97 (-1.14,-0.80) | -0.25 (-1.11,0.60) / 0.11 (-0.21,0.43) / 0.03 (-0.23,0.28) | — |
| BMI <18.5 / 18.5-<25 / 25-<30 / 30-<40 / >=40 kg/m2 | -0.43 (-1.50,0.63) / -1.03 (-1.29,-0.78) / -0.95 (-1.18,-0.72) / -1.00 (-1.32,-0.68) / -0.35 (-1.26,0.56) | -1.40 (-2.30,-0.49) / -1.07 (-1.28,-0.85) / -0.93 (-1.13,-0.73) / -1.09 (-1.36,-0.82) / -0.15 (-1.05,0.76) | 0.96 (-0.43,2.35) / 0.03 (-0.30,0.36) / -0.02 (-0.33,0.28) / 0.09 (-0.33,0.50) / -0.21 (-1.49,1.07) | — |
| CKD stage <=1 / stage 2 | -0.99 (-1.16,-0.81) / -0.92 (-1.22,-0.63) | -1.04 (-1.20,-0.88) / -0.92 (-1.15,-0.69) | 0.05 (-0.18,0.29) / 0.00 (-0.38,0.37) | — |
| Onset <18 / >=18 months | -0.99 (-1.28,-0.69) / -0.96 (-1.18,-0.75) | -0.95 (-1.22,-0.68) / -1.04 (-1.23,-0.85) | -0.04 (-0.37,0.30) / 0.08 (-0.16,0.32) | 0.59 |
| Definite+<18 / not definite+<18 months | -1.05 (-1.40,-0.71) / -0.95 (-1.12,-0.77) | -1.25 (-1.65,-0.86) / -0.97 (-1.11,-0.84) | 0.20 (-0.29,0.69) / 0.03 (-0.19,0.24) | 0.53 |
| All ALSFRS-R items >=2 / >=1 item <2 | -0.99 (-1.31,-0.67) / -0.99 (-1.17,-0.81) | -0.88 (-1.11,-0.65) / -1.08 (-1.25,-0.91) | -0.11 (-0.50,0.27) / 0.09 (-0.13,0.32) | 0.38 |
| NfL <median / >=median | -0.85 (-1.07,-0.64) / -1.04 (-1.25,-0.83) | -0.95 (-1.12,-0.78) / -1.07 (-1.26,-0.88) | 0.10 (-0.17,0.36) / 0.03 (-0.25,0.31) | 0.74 |
| dFRS <median / >=median | -0.84 (-1.07,-0.62) / -1.16 (-1.41,-0.90) | -0.91 (-1.09,-0.72) / -1.14 (-1.36,-0.93) | 0.06 (-0.21,0.34) / -0.01 (-0.29,0.27) | 0.70 |

### eTable 5 — TEAEs (pp. 21-24)

Columns are pooled CNM-Au8 **N=120**, CNM-Au8 30 mg **N=59**, CNM-Au8 60 mg **N=61**, shared placebo **N=163**, and regimen-specific placebo **N=41**. Every cell is `participants n (percent), event count`; the title includes events with >=5% incidence in either group. Exact rows, in the above column order:

- **p. 21:** Any TEAE: 111 (92.5%), 723; 54 (91.5%), 293; 57 (93.4%), 430; 146 (89.6%), 889; 38 (92.7%), 228. Mild: 41 (34.2%), 500; 21 (35.6%), 205; 20 (32.8%), 295; 68 (41.7%), 673; 13 (31.7%), 151. Moderate: 44 (36.7%), 165; 22 (37.3%), 66; 24 (39.3%), 99; 53 (32.5%), 164; 15 (36.6%), 61. Severe: 24 (20%), 58; 11 (18.6%), 22; 13 (21.3%), 36; 25 (15.3%), 47; 10 (24.4%), 16. Serious TEAEs: 16 (13.3%), 20; 6 (10.2%), 9; 10 (16.4%), 11; 15 (9.2%), 21; 7 (17.1%), 12. Treatment-related serious TEAE: 0 (0.0%), 0; 0 (0.0%), 0; 0 (0.0%), 0; 2 (1.2%), 3; 1 (2.4%), 2. Deaths: 4 (3.3%), 4; 1 (1.7%), 1; 3 (4.9%), 3; 4 (2.5%), 4; 2 (4.9%), 2. Leading to study-drug withdrawal: 8 (6.7%), 8; 4 (6.8%), 4; 4 (6.6%), 4; 11 (6.7%), 17; 3 (7.3%), 4. Leading to study-drug interruption: 9 (7.5%), 15; 6 (10.2%), 11; 3 (4.9%), 4; 12 (7.4%), 24; 4 (9.8%), 6.
- **p. 22:** Leading to reduction: 3 (2.5%), 5; 0 (0.0%), 0; 3 (4.9%), 5; 5 (3.1%), 12; 1 (2.4%), 1. Fall: 26 (21.7%), 44; 13 (22.0%), 22; 13 (21.3%), 22; 43 (26.4%), 79; 13 (31.7%), 17. Muscular weakness: 24 (20.0%), 39; 10 (16.9%), 18; 14 (23.0%), 21; 45 (27.6%), 67; 12 (29.3%), 17. Diarrhoea: 23 (19.2%), 33; 9 (15.3%), 12; 14 (23.0%), 21; 12 (7.4%), 14; 4 (9.8%), 5. Nausea: 17 (14.2%), 21; 9 (15.3%), 10; 8 (13.1%), 11; 14 (8.6%), 16; 6 (14.6%), 8. Fatigue: 13 (10.8%), 17; 6 (10.2%), 8; 7 (11.5%), 9; 30 (18.4%), 33; 9 (22.0%), 9. Headache: 17 (14.2%), 26; 9 (15.3%), 17; 8 (13.1%), 9; 19 (11.7%), 23; 4 (9.8%), 6. Neuromyopathy: 14 (11.7%), 21; 6 (10.2%), 8; 8 (13.1%), 13; 22 (13.5%), 33; 6 (14.6%), 7. Constipation: 17 (14.2%), 19; 4 (6.8%), 4; 13 (21.3%), 15; 20 (12.3%), 24; 3 (7.3%), 4. Dyspnoea: 13 (10.8%), 14; 7 (11.9%), 8; 6 (9.8%), 6; 10 (6.1%), 11; 4 (9.8%), 5. Dysarthria: 15 (12.5%), 16; 9 (15.3%), 10; 6 (9.8%), 6; 11 (6.7%), 13; 2 (4.9%), 2. Dysphagia: 10 (8.3%), 10; 6 (10.2%), 6; 4 (6.6%), 4; 18 (11.0%), 22; 5 (12.2%), 6. Oedema peripheral: 7 (5.8%), 13; 2 (3.4%), 3; 5 (8.2%), 10; 12 (7.4%), 15; 4 (9.8%), 4. Tension headache: 7 (5.8%), 10; 1 (1.7%), 1; 6 (9.8%), 9; 10 (6.1%), 15; 4 (9.8%), 4.
- **p. 23:** Urinary tract infection: 10 (8.3%), 13; 4 (6.8%), 6; 6 (9.8%), 7; 10 (6.1%), 10; 1 (2.4%), 1. Arthralgia: 6 (5.0%), 12; 3 (5.1%), 8; 3 (4.9%), 4; 6 (3.7%), 6; 3 (7.3%), 3. Vomiting: 6 (5.0%), 9; 4 (6.8%), 5; 2 (3.3%), 4; 6 (3.7%), 6; 2 (4.9%), 2. Amyotrophic lateral sclerosis: 8 (6.7%), 10; 2 (3.4%), 2; 6 (9.8%), 8; 1 (0.6%), 1; 0 (0.0%), 0. Skin laceration: 6 (5.0%), 7; 2 (3.4%), 2; 4 (6.6%), 5; 4 (2.5%), 8; 2 (4.9%), 2. Cough: 7 (5.8%), 7; 1 (1.7%), 1; 6 (9.8%), 6; 4 (2.5%), 4; 1 (2.4%), 1. Decreased appetite: 5 (4.2%), 5; 2 (3.4%), 2; 3 (4.9%), 3; 12 (7.4%), 13; 3 (7.3%), 3. Insomnia: 5 (4.2%), 6; 0 (0.0%), 0; 5 (8.2%), 6; 2 (1.2%), 2; 2 (4.9%), 2. Salivary hypersecretion: 5 (4.2%), 6; 1 (1.7%), 1; 4 (6.6%), 5; 9 (5.5%), 9; 2 (4.9%), 2. Depression: 3 (2.5%), 3; 1 (1.7%), 1; 2 (3.3%), 2; 8 (4.9%), 8; 4 (9.8%), 4. Faeces discoloured: 7 (5.8%), 7; 1 (1.7%), 1; 6 (9.8%), 6; 0 (0.0%), 0; 0 (0.0%), 0. Post-traumatic pain: 4 (3.3%), 4; 2 (3.4%), 2; 2 (3.3%), 2; 6 (3.7%), 6; 3 (7.3%), 3. Weight decreased: 2 (1.7%), 2; 0 (0.0%), 0; 2 (3.3%), 2; 5 (3.1%), 5; 5 (12.2%), 5. Pain in extremity: 5 (4.2%), 7; 1 (1.7%), 1; 4 (6.6%), 6; 9 (5.5%), 10; 1 (2.4%), 1.
- **p. 24:** Pruritus: 6 (5.0%), 8; 0 (0.0%), 0; 6 (9.8%), 8; 4 (2.5%), 6; 0 (0.0%), 0. Dizziness: 4 (3.3%), 4; 3 (5.1%), 3; 1 (1.6%), 1; 10 (6.1%), 13; 2 (4.9%), 3. Increased upper airway secretion: 5 (4.2%), 6; 3 (5.1%), 4; 2 (3.3%), 2; 4 (2.5%), 4; 1 (2.4%), 1. Anxiety: 4 (3.3%), 4; 0 (0.0%), 0; 4 (6.6%), 4; 8 (4.9%), 8; 2 (4.9%), 2. COVID-19: 3 (2.5%), 3; 2 (3.4%), 2; 1 (1.6%), 1; 11 (6.7%), 11; 3 (7.3%), 3. Pulmonary embolism: 5 (4.2%), 5; 1 (1.7%), 1; 4 (6.6%), 4; 2 (1.2%), 2; 1 (2.4%), 1. Sinusitis: 6 (5.0%), 6; 4 (6.8%), 4; 2 (3.3%), 2; 0 (0.0%), 0; 0 (0.0%), 0. Asthenia: 4 (3.3%), 5; 0 (0.0%), 0; 4 (6.6%), 5; 2 (1.2%), 2; 1 (2.4%), 1. Back pain: 5 (4.2%), 6; 3 (5.1%), 4; 2 (3.3%), 2; 4 (2.5%), 10; 0 (0.0%), 0. Flatulence: 5 (4.2%), 5; 0 (0.0%), 0; 5 (8.2%), 5; 0 (0.0%), 0; 0 (0.0%), 0. Complication associated with device: 3 (2.5%), 4; 3 (5.1%), 4; 0 (0.0%), 0; 3 (1.8%), 3; 0 (0.0%), 0. Alanine aminotransferase increased: 3 (2.5%), 3; 3 (5.1%), 3; 0 (0.0%), 0; 2 (1.2%), 2; 0 (0.0%), 0. Aspartate aminotransferase increased: 3 (2.5%), 3; 3 (5.1%), 3; 0 (0.0%), 0; 1 (0.6%), 1; 0 (0.0%), 0.

### eFigure — serum NfL sensitivity analysis (p. 25)

Longitudinal samples are baseline, week 4 (plasma only), week 8 (serum only), week 16, and week 24. Exclude NfL <**4 pg/mL** or <**2%** of an individual's maximum, removing **one** baseline measure for **one** participant. Values use natural-log scale; plotted result is difference of least-square means. Back-transformed change: regimen placebo **+11.6%**, combined-dose CNM-Au8 **+0.8%**; placebo-versus-CNM-Au8 difference in change of geometric mean **+9.7%** (95% CI **-0.1% to +18.5%**, **P=0.051**).

- **p. 26:** rights/end matter only; explicitly no applicable quantitative result.

## DOC-005: nonauthor collaborators (fresh-direct extraction, pp. 1-6)

All six pages are a roster of the HEALEY ALS Platform Trial Study Group, persons, degrees, institution/location, and role/contribution. Fresh native and layout text were reviewed page by page. The only printed quantities are administrative page markers (`1 of 6` through `6 of 6`) and template/version `v 02-22`; no endpoints, study population totals, treatment denominators, results, statistics, units, formulas, tables of results, figures, sensitivity/subgroup results, or main-paper quantitative matching keys occur. **No-applicable result-relevant support unit: DOC-005 pp. 1-6.**

## DOC-006: data-sharing statement (fresh-direct extraction, p. 1)

Administrative content was completely reviewed. It identifies ClinicalTrials.gov IDs **NCT04297683** and **NCT04414345**, says data available: **No**, describes the sharing-review committee and temporary restrictions on placebo data, and states that analyses/design simulations were programmed in **SAS v9.4 or later**, **R v4.0 or later**, or **JAGS v4.3 or later**; code is not publicly available while the trial is ongoing. It contains no outcome estimate, denominator, result table/figure, statistical test result, effect measure, interval, P value, or result-relevant formula. **No-applicable result-relevant support unit: DOC-006 p. 1.**

## Mapping handoff counts and limitations

- **Source pages mapped:** DOC-004 26/26; DOC-005 6/6; DOC-006 1/1; total **33/33**.
- **Result-bearing tables/figures mapped:** eTables 1-5 and one eFigure (**6** labeled result displays); eMethods definitions and prespecified sensitivity/subgroup/statistical relationships mapped across pp. 2-13.
- **Administrative no-applicable pages:** DOC-004 pp. 1 and 26; DOC-005 pp. 1-6; DOC-006 p. 1 is data-sharing administration (software/version statements retained above).
- **Limitations/gaps:** none for assigned source-page coverage. Exact table values are source-PDF authoritative; native extraction of the multi-column TEAE table was corroborated against direct source-PDF text and fresh page renders. No OCR was needed.
