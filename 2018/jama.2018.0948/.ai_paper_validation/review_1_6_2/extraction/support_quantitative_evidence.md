# Support quantitative evidence — protocol shard

## Scope, source identity and method

DOC-002, `joi180015supp1_prod.pdf`, every physical PDF page 1–37, is PLAN by prospective content. Every page bears Protocol 005 version date 23 February 2011; no second protocol version or amendment is supplied inside this document. Printed page and physical PDF page numbers agree. This shard does not inspect DOC-003/004 or the main paper. Matching keys below identify the quantities to match downstream, without asserting report agreement or diagnosing candidates.

All 37 units are reusable-backed; fresh-required units 0; mapped units 37; scientific gaps 0. Primary representation: `.ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180015supp1_prod.txt` (134434 characters). All 37 form-feed-delimited pages were read in bounded chunks using `awk`; source-linked inventory already establishes byte agreement with current direct pdftotext 25.03.0. Selective visual checks used inherited PNGs DOC-002-p19.png, DOC-002-p24.png and DOC-002-p29.png (original rendering engine unrecorded; current checks on CPU). These three pages are below the 32-page visual batch bound. No new derivative, rendering or OCR was necessary. Native `>` before an underlined comparator is not reliable: the visual Table 1 ICU call thresholds are **≥**, transcribed below. Sources and reusable assets are unmodified. Exact text appendix reproduces selected pages to retain complete table entries and operational abstraction fields.

Runtime agent ID: 01a129b3-5402-7d02-a860-33eb6970b900. No prior scientific conclusions were read.

## Page-specific coverage

| PDF page | Content and mapped quantitative scope | Completion |
|---|---|---|
| 1 | Protocol summary: design, population, hierarchy, intervention, timing, regression types and mortality power inputs | COMPLETE |
| 2 | Background motivation and historical rates; 22-hospital trial overview. No new prospective analysis specification beyond summary | COMPLETE |
| 3 | Primary mortality rationale; prospective baseline-rate measurement. Historical trial results distinguished from EPOCH | COMPLETE |
| 4 | Development/validation performance and score ranges; prospective intervention score identity. No new EPOCH outcome analysis | COMPLETE |
| 5 | Four intervention components, reliability, preparation, three research questions and hypothesis | COMPLETE |
| 6 | Literature search, clinical rationale, equipoise. No applicable new trial numeric result or statistical decision rule | COMPLETE_NO_NEW_APPLICABLE |
| 7 | Intervention implementation, education duration, 10-score/3-scenario competency evaluation and ICC rule | COMPLETE |
| 8 | Run-in targets, randomization strata, allocation, contamination and blinding | COMPLETE |
| 9 | Cluster and patient eligibility; exclusions; 52-week intervention and 26-week baseline/5-week run-in | COMPLETE |
| 10 | Primary mortality and main secondary SCDE definitions; DNR inclusion/exclusion; 78-week observation | COMPLETE |
| 11 | Eight secondary clinical outcomes begin; seven-point intensity scale, preventability rating/consensus procedures | COMPLETE |
| 12 | Clinical outcomes continue; units, denominators, readmission timing, ICU admission windows, 28-day VFDs; process outcomes | COMPLETE |
| 13 | Resource outcomes, exit survey sampling, denominator collection and boundary discharge rule | COMPLETE |
| 14 | Measurement quality control, survey timing, primary/SCDE power and participation inputs | COMPLETE |
| 15 | SCDE power completion, 22-cluster participation, compliance, VFD follow-up assumption | COMPLETE |
| 16 | Complete primary/secondary analysis specifications, prespecified subgroups, no interim analysis | COMPLETE |
| 17 | Exploratory survey associations, independent statistician review, randomization procedures and DSMC remit | COMPLETE |
| 18 | Steering oversight; no new applicable outcome, inferential rule or numeric result | COMPLETE_NO_NEW_APPLICABLE |
| 19 | Table 1 comparative score/calling-criteria development values, thresholds, AUC and range footnotes; historical validation data | COMPLETE |
| 20 | Table 2 all 22 validation rows with counts, median/IQR, P and AUC/CI; historical validation data | COMPLETE |
| 21 | Table 3 search strategy; 1069 references, 4 Cochrane reviews, 1 additional reference. No new applicable trial result/design | COMPLETE_NO_NEW_APPLICABLE |
| 22 | Table 4 phases 1–4, implementation timing and local plan requirements | COMPLETE |
| 23 | Table 4 phases 5–7, education and 5-week/20-bed run-in | COMPLETE |
| 24 | Table 5 all seven resuscitation categories, SCDE membership and transfer/PICU definitions | COMPLETE |
| 25 | Table 6 age, diagnoses, devices, prior ICU/event and procedure abstraction definitions | COMPLETE |
| 26 | Table 6 vital signs, interventions, investigation windows and units | COMPLETE |
| 27 | Table 6 96-hour infection window and legend, including printed scale-rating statement | COMPLETE |
| 28 | Table 7 all six preventability ratings and ≥4 legend; supplied appendix list | COMPLETE |
| 29 | Power appendix mortality baseline table, two scenarios and shared cluster assumptions | COMPLETE |
| 30 | Power appendix SCDE historical rates and planned effect; code-blue/stat-call power inputs | COMPLETE |
| 31 | References 1–22 only; no applicable new trial quantitative relationship | COMPLETE_NO_APPLICABLE |
| 32 | References 23–43 only; no applicable new trial quantitative relationship | COMPLETE_NO_APPLICABLE |
| 33 | References 44–65 only; no applicable new trial quantitative relationship | COMPLETE_NO_APPLICABLE |
| 34 | References 66–82 only; no applicable new trial quantitative relationship | COMPLETE_NO_APPLICABLE |
| 35 | References 83–104 only; no applicable new trial quantitative relationship | COMPLETE_NO_APPLICABLE |
| 36 | References 105–128 only; no applicable new trial quantitative relationship | COMPLETE_NO_APPLICABLE |
| 37 | References 129–131 only: PELOD, sample-size method, cluster CONSORT. No new applicable relationship or formula | COMPLETE_NO_APPLICABLE |

## Prospective design and analysis-population keys

**P-DESIGN**, [pp.1](../../../joi180015supp1_prod.pdf#page=1), [8](../../../joi180015supp1_prod.pdf#page=8), [9](../../../joi180015supp1_prod.pdf#page=9), [15](../../../joi180015supp1_prod.pdf#page=15): hospital-cluster randomized trial, 22 hospitals, 1:1 allocation. Detailed strata are <200 versus ≥200 eligible inpatient ward beds (p.8); the summary prints >200 and <200 beds (p.1). Half of hospitals within each stratum receive Bedside PEWS. Hospitals need >200 annual eligible pediatric admissions, <18 years and >37 weeks gestational age, pediatric physicians and ≥1 PICU. All eligible inpatient wards participate. No individual consent is anticipated (~100000 eligible inpatients, ~2300 inpatient beds), distinct from staff survey consent. The 20-hospital power base allows loss of 1–2 hospitals, giving 22 recruited hospitals.

**P-POPULATION**, [p.9](../../../joi180015supp1_prod.pdf#page=9): eligible inpatient wards exclude PICU, OR and other anesthetist-supervised procedure areas. ED admitted patients are eligible only if the same ward documentation is used; a separate ED chart makes that area ineligible. High-dependency/constant-observation/step-down areas count as PICU where PICU physicians have whole/joint clinical responsibility and can write orders. Exclude hospitals planning a new medical emergency team, already using ward severity scores, or unable to accept randomization. Exclude patients <37 weeks gestational age throughout admission, exclusively NICU, and directly admitted to PICU who die before PICU discharge with no eligible ward exposure. The protocol describes these operational populations but does not explicitly name ITT, per-protocol, imputation or a hospital dropout analysis.

**P-TIME**, [pp.8](../../../joi180015supp1_prod.pdf#page=8), [9](../../../joi180015supp1_prod.pdf#page=9), [10](../../../joi180015supp1_prod.pdf#page=10): 26 weeks (6 months) baseline, 5-week run-in, then 52 weeks (12 months) intervention. Intervention begins week 31/7 months after baseline start. Equal 78 weeks of outcome observation across arms, excluding run-in from the baseline+intervention observation sum. Allocation revealed in second week (p.8); randomization in first week and notification within 10 days (p.17). Analytic team blinded; frontline/site outcome collectors cannot be blinded. Baseline rates are used to adjust secular/study effects.

**P-INTERVENTION**, [pp.7](../../../joi180015supp1_prod.pdf#page=7), [8](../../../joi180015supp1_prod.pdf#page=8), [22](../../../joi180015supp1_prod.pdf#page=22), [23](../../../joi180015supp1_prod.pdf#page=23): documentation-based Bedside PEWS replaces routine vital-sign documentation in ward areas; four components are score, embedded chart, score-matched care recommendations and education. Electronic chart adaptation includes all 7 items. Local names may change without changing recommendations. Control retains standard care, existing calling criteria/expert identification, staffing and MET-RRT. Education starts 3 months before run-in; p.7 describes 2-hour group sessions (6–8 staff/educator) plus 1–2 hours interactive use; Table 4 p.23 describes 4 hours total (2+2), plus 90-minute physician instruction. Instructor course 2 days. Table 4 has documentation modifications 4–8 months before implementation, care recommendation localization 4–8 months before frontline education, instructor course 2–4 months before frontline education, local plan 1–3 months before frontline education. Run-in 20–30 beds (p.15), ≥20 beds (Table 4), 5 weeks before go-live. Competency: 10 vital-sign sets across 3 cases; ICC >.90 and no score >2 points from electronic standard. From week 2, 4 days/week, review preceding 12 hours of documentation in 10–15 randomly selected patients/day; ≥40 reviewed periods/week. Targets: >80% scores within 2 points; >5/7 items used for >80% scores; >80% patients assessed at recommended frequency. Interim implementation data reviewed ≥2 times/week; week-4 target failure reviewed by steering group. This implementation monitoring is distinct from the explicitly absent interim outcome analysis.

## Planned outcome hierarchy and operational quantities

| Local map key | Status/population/time/quantity | Exact location and main-paper matching key |
|---|---|---|
| P-PRIMARY | All-cause hospital mortality, primary. All eligible patients with any eligible ward care, including anticipated DNR deaths; exclude exclusive PICU/NICU/ineligible ED care. Death during index stay, rate per 1000 discharges in power appendix | pp.1,10,16,29; hospital mortality, DNR, eligible hospital discharges |
| P-SCDE | **Main secondary outcome**: significant respiratory/circulatory therapy or CPR in 12 h before ward→PICU transfer or 1 h after; or ward death without preceding DNR. Treatments, not code-blue activation, define event. DNR excludes anticipated deaths; DNR after begun resuscitation does not exclude event | pp.10–11,24; significant clinical deterioration events/composite and component thresholds |
| P-INTENSITY | Additional clinical secondary #1: nature of deterioration, seven-point Children's Resuscitation Intensity Scale, treatment in 12 h before/1 h after transfer and ward death. Direct ward→PICU and ward→OR→PICU admissions count if initiated on ward. OR-initiated admissions do not count as deterioration | pp.11,24; clinical deterioration/resuscitation intensity |
| P-PREVENTABLE | Clinical secondary #2: potentially preventable ward cardiac arrest without preceding DNR, intensity categories 6/7. Six-point preventability scale, independent blinded reviewers followed by consensus. Source rendering confirms p.11 prints “at ≥4”, then explicitly includes ratings 4,5,6; native text loses the comparator underline; p.28 legend says “4 or more” | pp.11–12,27–28; potentially preventable cardiac arrest and adjudication |
| P-READMIT-H | Clinical secondary #3: unplanned hospital readmission within 48 h, operationally before third midnight following discharge. Rate per 1000 hospital discharges | p.12; unplanned hospital readmissions |
| P-READMIT-I | Clinical secondary #4: unplanned PICU readmission within 48 h after PICU discharge to eligible ward; before midnight of second complete day/third midnight. Rate per 1000 hospital discharges | p.12; unplanned ICU/PICU readmissions |
| P-PIM | Clinical secondary #5: PIM predicted mortality following urgent PICU admission from ward; model specification calls it PIM2 | pp.12,16; PICU admission severity/PIM2 |
| P-MORT-I | Clinical secondary #6: PICU mortality after urgent ward-origin PICU admission. p.12 denominators says PICU mortality per 1000 hospital discharges; p.16 separately plans ward-initiated and OR-initiated urgent admission analyses | pp.12,16; PICU mortality and population distinction |
| P-PELOD | Clinical secondary #7: PELOD score for first 24 h and whole PICU stay after urgent ward-origin admission | pp.12,14,16; organ dysfunction/PELOD |
| P-VFD | Clinical secondary #8: days alive without invasive ventilation in 28 days from PICU admission. First PICU admission only within each baseline/intervention period; repeat admissions retain all other ICU outcomes. Discharged before day 28 assumed alive and ventilator-free | pp.12,15; ventilator-free days and follow-up assumption |
| P-STAT | Process secondary #1: immediate physician attendance requested for ward patient | pp.12,16,30; stat calls per 1000 patient-days |
| P-CODE | Process secondary #2: immediate resuscitation-team/equipment assistance/code-blue calls | pp.12,16,30; code-blue events per 1000 patient-days |
| P-CONSULT | Process secondary #3: new urgent ICU/MET-RRT consult episodes; repeated patients count if urgent call leads to unplanned/earlier review, planned reviews excluded | pp.12,16; urgent ICU/MET consultations per 1000 patient-days |
| P-DOCUMENT | Process secondary #4: per-24-h count of documented HR, RR, SBP, temperature, oxygen saturation, respiratory effort, oxygen therapy and capillary refill in 5 centrally randomized patients/week. Also physician visits, nurse:patient ratio and continuous monitoring. p.16 comparison lists seven PEWS items and all-seven documentation | pp.12,14,16; documentation/vital-sign completeness |
| P-SURVEY | Process secondary #5: documentation/interaction survey of frontline staff, 2 pages/<10 minutes. Administered month 2 of baseline, months 3 and 9 after start of randomization phase | pp.13–14,16–17; frontline perceptions |
| P-RESOURCE | Secondary resource use: hospital LOS in all hospitals; following urgent ICU admission ICU LOS and ventilation, dialysis, ECMO, nitric oxide days. Dialysis includes intermittent/continuous hemofiltration, hemodialysis, peritoneal dialysis, plasmapheresis and red-cell exchange. Analysis separately names plasmapheresis | pp.13–14,16; ICU therapies, LOS/patient-days |
| P-EXIT | Exit survey 3 months after 12-month intervention; local intent related to before/after event rates. Maximum 10 leaders/site; minimum CEO/CNO/surgery/medicine leaders; >80/>120/>180 beds add 2/4/6 leaders. Descriptive analysis and size-weighted linear between-group comparisons | pp.13,16; administrative exit survey |

### SCDE component table (Table 5)

[PDF p.24](../../../joi180015supp1_prod.pdf#page=24), PLAN. Visual inspection confirms all entries:

| Scale | Label | Definition | SCDE |
|---|---|---|---|
| 1 | Early transfer | <60 mL/kg IV/IO resuscitation in preceding 12 h; no IV/IO inotrope/vasoactive agent and no bag-mask/endotracheal positive-pressure ventilation in preceding 12 h | No |
| 2 | Intermediate transfer/non-invasive respiratory | Positive-pressure ventilation in preceding 12 h but not intubated at transfer, including mask PAP; exclude ventilation under anesthesia for scheduled procedure | No |
| 3 | Respiratory | Intubated and/or endotracheal ventilation at transfer, or intubation within 1 h of PICU admission | Yes |
| 4 | Circulatory | **>60 mL/kg** IV/IO fluids in preceding 12 h **and** any IV/IO inotrope/vasopressor at transfer or during preceding 12 h; may include category-2 ventilation | Yes |
| 5 | Late transfer | Respiratory [3] and circulatory [4] support before transfer | Yes |
| 6 | Cardiopulmonary resuscitation | Chest compressions on ward or within 1 h PICU admission, or ECMO instituted before/within 1 h PICU admission | Yes |
| 7 | Death | Ward death without DNR order; may occur despite CPR/intended CPR; no transfer | Yes |

Transfer time ordinarily means arrival in PICU; urgent departure is <6 h after initiation. For ward→OR→PICU, transfer time instead begins at ward departure to OR, and OR treatments other than CPR are excluded from deterioration classification. Unanticipated OR events requiring PICU are excluded. Table 5's PICU footnote says routinely admitted patients include children beyond neonatal period <12 years; p.9 patient eligibility is <18. Both statements are retained with location, without choosing a scope reading. Broad urgent PICU admission definition p.12 includes OR-initiated admission irrespective of initiation-to-departure time, whereas deterioration is ward-origin.

### Preventability/adjudication and measurement details

[pp.11](../../../joi180015supp1_prod.pdf#page=11), [12](../../../joi180015supp1_prod.pdf#page=12), [25](../../../joi180015supp1_prod.pdf#page=25), [26](../../../joi180015supp1_prod.pdf#page=26), [27](../../../joi180015supp1_prod.pdf#page=27), [28](../../../joi180015supp1_prod.pdf#page=28): two physicians independently rate cases; >5 years independent practice, standardized training and 20 practice reviews, reviewer ICC evaluated. Concordant rating is consensus; discordance discussed; third physician >10 years practice facilitates agreement and determines rating if unresolved. Report pre-discussion kappa. Preventable arrests per 1000 patient-days. Table 7 ratings: 1 virtually no evidence; 2 slight/modest; 3 less than 50/50 close call; 4 more than 50/50 close call; 5 strong evidence; 6 virtually certain. Legend says ≥4 high preventability.

Table 6 abstraction retains months age if <1 year else years; primary/secondary diagnoses; home oxygen, tracheostomy, feeding tube, central/other permanent vascular access, arterial line, prior PICU discharge in last 2 days/>2 days/no prior ICU (includes NICU), prior LOS <1/>1 week, prior arrest. Procedures in preceding 7 days classified by organ/system and free-text primary/two secondary procedures. Medications in preceding 25 h with administration hour; 13 h of vital signs, consciousness/pupils, oxygen/nebulized/positive-pressure support, fluids mL/kg averaged per hour, transfusion, vasoactive yes/no and urine output. Investigations in preceding 48 h; specified values closest to 48 h (>24 h), 12 h (<24/>12 h), 1 h (<12/>1 h), number of tests <24/>1 h, upper/lower normal limits. Chest X-ray/neuroimaging/echo in preceding 48 h. Cultures sampled within 96 h, site investigator excludes contaminants, <300-word anonymized event summary. p.27 legend prints cardiac-arrest deterioration “scale rating 4 or 5”; p.11 uses 6/7. Both exact locations retained. Not an adjudicated issue at mapping.

[pp.13](../../../joi180015supp1_prod.pdf#page=13), [14](../../../joi180015supp1_prod.pdf#page=14): hospital/PICU discharges and ward/PICU days recorded at hospital discharge. Patient-day = any part of 00:00–23:59 in area; ward hospital days exclude PICU/NICU; ICU days whole/part PICU day. At end of baseline and intervention, patients are regarded as discharged from inpatient ward and PICU. DNR date/time, location of death and pre-CPR status recorded; daily transfer/death screening. Five randomly selected patients/week document preceding 24 h; 5% random ICU outcome/resource records compared with source during site visits. Hospital characteristics at first week; weeks 22–24; 54–56; 81–83. Measurement sources overlap (hospital systems, ICU admission/discharge records, paging logs, mortuary/code-blue logs, staff and charts); no derived database/raw patient data supplied.

## Complete planned inferential relationships

[PDF p.16](../../../joi180015supp1_prod.pdf#page=16), PLAN. Descriptives: means, medians, variances, IQRs, proportions with 95% CIs; baseline/intervention outcomes for each hospital; baseline from 6-month prospective observation.

| Local model key | Dependent quantity and model | Covariates, weighting and contrast |
|---|---|---|
| P-MODEL-PRIMARY | Logit regression; **logit of proportion dying in each hospital** | Treatment-arm indicator, baseline mortality logit, hospital-size stratum; hospital-size weighted; Bedside PEWS vs standard care |
| P-MODEL-LOGIT | Identical logit model for (a) ward-initiated urgent admission PICU mortality, (b) OR-initiated urgent admission PICU mortality, (c) 48-h unplanned hospital readmission, (d) all-cause mortality following DNR | Identical specification to primary |
| P-MODEL-POISSON | Hospital-aggregated counts: SCDE, code-blue, stat, urgent ICU consults; rates per 1000 patient-days | Treatment arm, baseline event rate, hospital-size stratum. An explicit offset/link or weighting is not printed in this paragraph |
| P-MODEL-LINEAR | Within-hospital mean for deterioration intensity, ward patient-days, PIM2, PELOD, VFDs, ICU patient-days, therapy days (ventilation, ECMO, dialysis, plasmapheresis, nitric oxide) | Treatment arm, baseline mean, hospital-size stratum; hospital-size weighted |
| P-MODEL-DOCUMENT | Identical linear regression for frequency of vital-sign documentation; seven PEWS items and all-seven count | Baseline event rates and hospital strata; **unweighted**, because same number of records/hospital |
| P-MODEL-PRACTICE | Linear models comparing documented vital signs, physician visits, nurse:patient ratio, continuous ECG and pulse oximeter monitoring “with the Bedside PEWS scores calculated from the abstracted clinical data” | Printed comparison wording retained; all analyses baseline-/stratum-adjusted |
| P-MODEL-SURVEY | Documentation/interaction, post-education and post-study decision-maker survey: descriptive; between-group comparisons linear regression | Hospital-size weighted |

Prespecified subgroups on p.16: (1) hospital <200 versus ≥200 eligible ward beds (same stratification as randomization), (2) hospital with vs without MET, (3) hospital with ECMO for children, (4) patients with urgent PICU admission initiated on ward. No interaction test formula or subgroup-specific multiplicity rule is supplied. No other sensitivity analysis or imputation method is specified in this protocol. p.10 additionally plans frequency of DNR orders and analyses in patients with/without DNR.

**P-INTERIM** p.16: “The study outcome analyses will be performed once. There will be no interim analysis.” No efficacy/futility boundary, noninferiority/equivalence margin or outcome multiplicity adjustment is specified. p.17 DSMC reviews study-associated adverse events and a steering report describing first 18 months; independent statistician reviews primary data, analyses and report before steering interpretation. These oversight reviews are distinguished from interim outcome testing. p.17 exploratory work relates post-education survey responses to documentation/interaction surveys and vital-sign documentation in implementing hospitals, identified as thesis work. Quality of life explicitly not measured (p.14).

## Sample-size and power relationships

**P-POWER-MORT**, [pp.1](../../../joi180015supp1_prod.pdf#page=1), [14](../../../joi180015supp1_prod.pdf#page=14), [15](../../../joi180015supp1_prod.pdf#page=15), [29](../../../joi180015supp1_prod.pdf#page=29): published cluster method (Hayes/Bennett), no algebraic formula printed. Summary: 22 hospitals, absolute reduction **0.9 deaths/1000 admissions**, relative reduction **18%**, k=.15, power .8, alpha .05, baseline 5.1/1000. Main power paragraph: 20 hospitals, relative reduction 18%, absolute risk reduction **0.09%**, alpha .05 two-sided, power 80%, mean 119 beds, LOS 4 days, occupancy .90, k .15 (coefficient of mortality variation between hospitals), baseline 5.1/1000; recruit 22 for 1–2 losses. Participating sites total 2322 beds, 99389 admissions, 397556 patient-days, LOS 4 days. Appendix p.29 prints 18% relative reduction corresponding to absolute reduction **0.9%**. Appendix assumptions: n=20 hospitals, alpha .05, z=1.96, power 80%, average beds **119.85**, LOS 4, occupancy .90, k=.15. Logistic scenarios: relative reduction .178 at baseline 5.1/1000 discharges; .199 at baseline 3.2/1000 discharges. These displayed quantities are retained separately rather than harmonized.

Mortality baseline table p.29 (deaths/1000 discharges): Sick Children 2.17; BC 5.0; John Hopkins 5.08; Stollery 6.8; St Justine 2.1; McMaster 8.4; Eastern Ontario 7.22; Centre Mere-Enfant CHUQ 2.07; London 6.98; South Eastern Ontario 7.0; St George's 4.46; Dallas 6.5; IWK 2.31; Alberta 5.4; overall average 5.11. Alternative historical Pennsylvania cohort: 1994–2001, 678365 subjects, 2202 in-hospital deaths, rate 3.2/1000. This historical table informs power; it is not EPOCH mortality results.

**P-POWER-SCDE**, [pp.14](../../../joi180015supp1_prod.pdf#page=14), [15](../../../joi180015supp1_prod.pdf#page=15), [30](../../../joi180015supp1_prod.pdf#page=30): p.14 describes four Ontario hospitals, 1052 urgent ICU admissions/year and estimates 40% as SCDE, producing baseline 2/1000 patient-days. At 20 sites, 31% relative reduction, alpha .05 two-sided, power 80%, k .15; modest k justified by baseline adjustment. Appendix p.30 describes 2 years of data after 31 January 2007: hospital admissions/discharges 55963, PICU beds 62, PICU discharges 7300, unplanned PICU admissions 1052 (14.5% PICU discharges; 18/1000 hospital discharges), post-unplanned PICU deaths 65 (6.2% unplanned discharges; 1.2/1000 hospital discharges), code blue 150 (3/1000 hospital discharges; .75/1000 patient-days). Prior-era comparator mortality 15.1% is historical only. LOS 4 days based on 397556/99389; estimated SCDE 2/1000 patient-days; 20 sites, 31% reduction, power 80%, alpha .05, k .15, absolute reduction .62 events/1000 patient-days.

**P-POWER-CODE**, p.30: .75 code-blue events/1000 patient-days, 20 hospitals, relative reduction .41, alpha .05, z 1.96, power 80%, 119.85 beds, LOS 4, k .15; printed absolute reduction “0.3/1000 events per thousand patient days”. Preserve printed unit rather than infer normalization.

**P-POWER-STAT**, p.30: Poisson regression; 8.13 stat calls/1000 patient-days at Sick Children, relative reduction .181, alpha .05, z 1.96, power 80%, beds 119.85, LOS 4, k .15, n20; absolute reduction 1.45 calls/1000 patient-days.

## Historical validation and peripheral quantitative tables

These supplied values are mapped to distinguish them from trial outcomes. pp.1–6: 7-item Bedside PEWS range 0–26; single-center AUC .91, sensitivity 82% summary/83% detail, specificity 95% detail at score8; 2074 patients/4 hospitals multicenter AUC .87; score reliability ICC .92; 98 frontline staff (96% acceptable speed, 97% confidence maintained/improved); 280 care-recommendation respondents (80 community/200 referral). Earlier 16-item PEWS at threshold5 AUC .91, sensitivity78%, specificity95%; Brighton cohort 2979/51 PICU transfers AUC .89, sensitivity78%, specificity82% at5; Cardiff AUC .86, sensitivity69%, specificity90% at2. These study-specific values are not assumed to be the same population as Table 1 objective-component comparisons.

Table 1 p.19 compares objective components in common 2074-patient/4-hospital dataset. AUCs Bristol .52, Brighton .53, Toronto .87, Melbourne .73, Cincinnati NA, Baltimore NA, Cardiff .62, Bedside .87. Visually confirmed ICU thresholds: Bristol ≥1 criterion; Brighton score≥5; Toronto score≥5; Melbourne≥1; Cincinnati≥1; Baltimore≥1; Cardiff score≥2 suggested; Bedside score≥8. Development sensitivity/specificity pairs: Bristol99/63; Brighton71/91; Toronto78/95; Cardiff70/90; Bedside82/93%; Melbourne/Cincinnati/Baltimore not supplied. Score ranges/items and range-footnote percentages are retained in exact appendix below. Table 2 p.20 full 22-row validation grid is retained there with counts, median/IQR, P, AUC/95%CI; all-case 686 versus control1388 (2074 total). Historical validation P values must not be matched to EPOCH mortality tests.

Figures 1–6, Case Report Form, questionnaire, Instructor Course and Research IT appendices are mentioned in body but not present as displays/attachments within these 37 pages. Table 3 is search strategy, not trial-results extraction. There are no workbook formulas, cached values, CSV or Office cells in this shard.

## Limitations and handoff

No scientific-coverage gap remains: all 37 source pages mapped. The text is a locator/transcription aid; any subsequent registered finding requires exact PDF confirmation. Inherited render engine is unrecorded. Full detailed main-paper matching is performed downstream across disjoint mapper artifacts. This mapper assigns no findings, candidates, dispositions or classification. Local P-* keys are source map keys, for coordinator/checkers to cross-reference into global N/S relationship IDs.

## Exact page-text appendix

The selected reusable page transcriptions below retain all historical table rows and operational fields in their native reading order. Underlined ≥ threshold signs in Table 1 are clarified above by direct visual inspection. Physical page markers are added by awk and are not source content.

### DOC-002 physical PDF page 19 — exact reusable native text

```text
Evaluating processes of care & the outcomes of children in hospital (EPOCH): a cluster randomized trial of
the Bedside Paediatric Early Warning System.
PI: Christopher Parshuram Research Protocol
Table 1:
Scores and calling criteria to identify children at risk of near or actual cardiopulmonary arrest.
Origin

Description

Development

Bristol
2005

Expert opinion

Brighton
2005

10 triggers plus
+3 diagnosis
related criteria
+ staff concern
Score 0-11,
7 items

Toronto
2006

Score 0-26
9 static 7 dynamic

Melbourne
2006

8 triggers
+ concern

Cincinnati
2007

4 subjective
triggers
+ staff concern
+ parental
concern
8 subjective items
2 types of ‘arrest’
+ concern
Score 0-8
7 items

Baltimore
2008
Cardiff
2009
Bedside
PEWS
2009

ICU call
threshold
>1 criteria

AUC
ROC
0.52

Sens 99% Spec 63%
Expert opinion
(Tucker 2009)
Sens 71% Spec 91%
Delphi Consensus and
statistical item selection
Sens 78% Spec 95%
Expert opinion
No sens or specificity

Score > 5

Expert review of local
data
No sens or specificity

>1 criteria

Expert opinion

>1 criteria

No sens or specificity
Expert Consensus
Sens 70% Spec 90%

Score >2
suggested

0.53
Score > 5
0.87
>1 criteria
0.73

NA

Score 0-26
7 items

NA
0.62

Expert opinion,
Score > 8
statistical item
0.87
reduction
Sens 82% Spec 93%
Scores and calling criteria to identify children at risk for near and actual cardiopulmonary arrest. We evaluated
the objective components in the dataset describing the 2074 patients in 4 paediatric hospitals. Limitations of
the data to evaluate change of heart rate and respiratory rate more than 20 or 30 above ‘baseline’ were
operationalized by using the mean for all control and case patients in each age range (<3m, 3-12months, 1-4
years, 5-12 years, >12 years) and looking for deviation from this number. The range (maximum-minimum) of
the reported measurements of heart rate for each patient was more than 20 beats per minute in 86% of case
and 40% of control-patients, and the range was more than 30 beats per minute in 74% of case and 22% of
control patients. The range of reported Respiratory Rate Measurements was greater than 20 breaths per
minute in 57% of case and 7% of control patients, and was more than 30 breaths per minute in 34% of case
and 3% of control patients.
AUCROC= Area Under the Receiver Operating Characteristics Curve.

Protocol 005 version date 23 February 2011

Page

19


```


### DOC-002 physical PDF page 20 — exact reusable native text

```text
Evaluating processes of care & the outcomes of children in hospital (EPOCH): a cluster randomized trial of
the Bedside Paediatric Early Warning System.
PI: Christopher Parshuram Research Protocol
Table 2
Performance of the Bedside-PEWS score in 2074 hospitalized children
Patient
Category
All

Control patients

Case patients

N

N

Score Median
(IQR)
1388
2 (1-4)

686

Score Median
(IQR)
8 (5-12)

p
<.0001

AUCROC
(95%CI)
0.87 (0.85-0.89)

Urgent ICU
772
2 (1-4)
381
10 (7-13)
<.0001
0.92 (0.90-0.94)
Code Blue
616
2 (1-4)
305
6 (3-10)
<.0001
0.81 (0.78-0.84)
Age
<3 months
333
2 (1-4)
190
7 (4-10)
<.0001
0.83 (0.79-0.86)
3-<12 months
362
2 (1-4)
164
8 (6-11)
<.0001
0.86 (0.82-0.90)
1-<5 years
286
2 (1-4)
134
9 (5-13)
<.0001
0.90 (0.87-0.93)
5-12 years
221
2 (1-3)
110
10 (5-13)
<.0001
0.89 (0.84-0.93)
>12 years
186
3 (2-4)
88
11 (6-14)
<.0001
0.91 (0.87-0.95)
Hospital
1
658
2 (1-4)
324
9 (6-12)
<.0001
0.88 (0.85-0.90)
2
478
1 (1-3)
238
6 (4-9)
<.0001
0.89 (0.86-0.92)
3
164
5 (2-6)
80
12 (9-15.5)
<.0001
0.91 (0.87-0.95)
4
88
2 (1-3)
44
9 (4-12)
<.0001
0.89 (0.83-0.96)
Chronic Disease
Transplant
73
2 (1-3)
58
11 (7-12)
<.0001
0.94 (0.90-0.98)
Heart Disease
386
3 (2-5)
233
8 (6-11)
<.0001
0.84 (0.81-0.88)
Severe Cerebral
34
2 (1-4)
62
10 (7-13)
<.0001
0.92 (0.86-0.98)
Palsy
Medical Device
Tracheostomy
36
4 (1.5-5.5)
57
7 (4-11)
<.0001
0.76 (0.67-0.86)
Feeding Tube
112
3 (1-5)
138
10 (6-13)
<.0001
0.86 (0.82-0.91)
Home Oxygen
27
5 (2-7)
47
8 (6-11)
<.0001
0.79 (0.69-0.90)
Acute condition
Seizures>15
6
2 (2-4)
47
6 (3-10)
0.1146
0.74 (0.48-0.99)
min
Complexity
>3 services
136
3 (1-5)
164
9 (6-12)
<.0001
0.87 (0.83-0.91)
>10
109
3 (2-5)
162
10 (6-13)
<.0001
0.85 (0.81-0.90)
medications/day
Administrative
Recent primary
5
1 (0-2)
18
7 (3-8)
0.0040
0.89 (0.75-1.00)
service transfer
IQR= Interquartile range. The hospitals are Hospital for Sick Children, Birmingham Children’s Hospital,
Stollery Children’s Hospital and Ste. Justines Hospital. AUCROC= Area Under the Receiver Operating
Characteristics Curve.

Protocol 005 version date 23 February 2011

Page

20


```


### DOC-002 physical PDF page 25 — exact reusable native text

```text
Evaluating processes of care & the outcomes of children in hospital (EPOCH): a cluster randomized trial of
the Bedside Paediatric Early Warning System.
PI: Christopher Parshuram Research Protocol
Table 6
Abstraction to evaluate the potential preventability of cardiac arrest.
Age
Diagnoses
Primary and Secondary

In months if less than 1 year, otherwise in years
Diagnoses represent active problems or a treated problem.
Primary = the main diagnosis
Secondary = clinically relevant but less relevant than the overarching main
diagnosis.
See Case Report form

Severity of Illness

1 home oxygen
2 tracheostomy
3 percutaneous – enteral feeding tube
4 permanent vascular access central line
5 permanent vascular access other than central line
6 Arterial line in-situ
7 PICU discharge (during this hospitalization) in last 2 days, >2 days or no
ICU admission during this hospitalization (includes NICU admission).
8 Length of hospital stay before event: <1 week, > 1 week
9 previous cardiac arrest (in this hospital admission).

Recent procedures

Procedures. (indicate all that apply)
In the last 7 days...
1 Cardiac – with cardiopulmonary bypass
2 Cardiac – without cardiopulmonary bypass
2 Cardiac – catherization
3 Vascular (includes major endvascular procedures, open surgery)
4 Vascular – insertion / removal of permanent vascular access
5 Central Nervous System
6 Spinal / other neurologic-orthopaediac surgery
7 Craniofacial
8 Orthopaedic (not spinal)
9 Ear Nose and Throat
10 Thoracic (not cardiac or vascular)
11 Abdominal surgery
12 Dental
13 Plastic / Cutaneous and, or muscular
14 Opthalmologic Surgery

Acute Problems

A Free Text Primary Procedure
B Free Text Secondary Procedure 1
C Free Text Secondary Procedure 2
1 Seizures
2 CNS other
3 ENT
4 Respiratory

Protocol 005 version date 23 February 2011

Page

25


```


### DOC-002 physical PDF page 26 — exact reusable native text

```text
Evaluating processes of care & the outcomes of children in hospital (EPOCH): a cluster randomized trial of
the Bedside Paediatric Early Warning System.
PI: Christopher Parshuram Research Protocol
5 Circulatory
6 Renal
7 Hepatic
A Free Text description
Medications
Vital Signs

Respiratory
Intervention
Circulatory
Intervention

Investigations

Radiology

List of medications given in the 25 hours before the event and the hour in
which they were administered.
From 13 hours before event until time of event: Documented
Heart Rate, Respiratory Rate, Systolic Blood Pressure, Diastolic blood
pressure, Trans-cutaneous oxygen Saturation, Capillary Refill Time,
Respiratory Effort, Temperature, Level of Consciousness (Glasgow Coma
Scale, Comfort scale) pupil size.
From 13 hours before event until time of event: Documented
Oxygen therapy
Nebulized therapy
Positive pressure ventilation
From 13 hours before event until time of event: Documented
Intravenous Fluid therapy (total fluids input) expressed in ml /kg averaged
over each hour
Transfusion
VasoActive Agents (as yes / no) : Dopamine, Milrinone, Amrinone,
NorEpinephrine, Epinephrine, Prostaglandin
Urinary output
Two most recent sets of blood results if drawn in the last 48 hours.
For each of the following laboratory investigations: we will record the value
[a] closest to 48 hrs before and >24 hours before
[b] closest to 12 hrs before AND <24 h & >12 h before event
[c] closest to one hr before AND <12 h & >1hr before event
[d] number of tests of the specified type assessed <24 h & >1 h before event
[e] are relevant upper and lower limit of normal for the test
Inflammatory Markers: C-Reactive Protein, Erythrocyte Sedimentation Rate,
Procalcitonin.
Full Blood count: Haemoglobin, White Cell Count, Bands, Platelet Count
Electrolytes: Sodium, Potassium, Calcium (total), Calcium Ionized, Magnesium
Blood Gas arterial: PaO2, PaCO2, HCO3 (measured, calculated), pH.
Blood Gas mixed venous: PaO2, PaCO2, HCO3 (measured, calculated), pH.
Metabolic: Ammonia, Lactate (not peripheral) Glucose,
Liver Tests: Aspartate and Alanine Aminotransferase, Bilirubin (conjugated,
and un-conjugated), Lactate Dehydrogenase, International Normalized Ratio
(INR), Partial Prothrombin Time.
Chest XRay in 48 hours before event: not done / new or worsening infiltratesabnormality / unchanged / normal.
Neuroimaging in 48 hours before event: not done / lesion new or expanding /
normal / unchanged
Echocardiogram in 48 hours before event: not done / deteriorating cardiac
function / improving cardiac function / normal function / unchanged.

Protocol 005 version date 23 February 2011

Page

26


```


### DOC-002 physical PDF page 27 — exact reusable native text

```text
Evaluating processes of care & the outcomes of children in hospital (EPOCH): a cluster randomized trial of
the Bedside Paediatric Early Warning System.
PI: Christopher Parshuram Research Protocol
Infection

Other relevant data

From samples taken in the 96 hours before event:
Confirmed Positive Blood Culture: Yes / no and list organism
Positive Microbiologic Specimen from other site
1 CNS
2 Respiratory Tract
3 Urine
4 Drain – other (specified)
Confirmed positive cultures are judged not to be contaminants by the
reporting site investigator.
Short < 300 word summary (clinical data referenced to event time, no patient
identifiers)

Legend
Items to be documented for clinical deterioration events that include a cardiac arrest (scale rating 4 or 5).
After abstraction items will be reviewed by the site investigator, and submitted anonymously to the data coordinating center. The data will then be presented in a standard format – including the use of the Bedside
PEWS documentation record – for evaluation of preventability by a multi-disciplinary adjudication panel.

Protocol 005 version date 23 February 2011

Page

27


```


### DOC-002 physical PDF page 28 — exact reusable native text

```text
Evaluating processes of care & the outcomes of children in hospital (EPOCH): a cluster randomized trial of
the Bedside Paediatric Early Warning System.
PI: Christopher Parshuram Research Protocol
Table 7
Preventability criteria
Ratin
Category
g
1
Virtually no evidence of preventability
2
Slight to modest evidence of preventability
3
Preventability not quite likely (less than 50/50, but “close call”)
4
Preventability more than likely (more than 50/50, but “close call”)
5
Strong evidence of preventability
6
Virtually certain evidence of preventability
Legend
Preventability criteria, as used in the Canadian Adverse Events Study. A rating of 4 or more was regarded as a
high degree of preventability.126

Appendices

1 Power & Sample Size
2 Case Report Form- see separate attachment

Protocol 005 version date 23 February 2011

Page

28


```


### DOC-002 physical PDF page 29 — exact reusable native text

```text
Evaluating processes of care & the outcomes of children in hospital (EPOCH): a cluster randomized trial of
the Bedside Paediatric Early Warning System.
PI: Christopher Parshuram Research Protocol

Power & Sample Size Appendix
Power Calculations were determined using Hayes RJ, Bennett S: Simple sample size calculation for clusterrandomized trials. Int J Epidemiol 1999; 28: 319-26. Reference 129.
[1] All Cause Hospital Mortality
Baseline rate data are presented from participating hospital. We estimate that this study will have sufficient
power to demonstrate 18% relative risk reductions in all cause mortality this corresponds to an absolute risk
reduction of 0.9%.
Baseline Data
Participating Paediatric Hospital
All Cause Mortality
/ 1000 discharges
The Hospital for Sick Children
2.17
BC Children's Hospital
5.0
John Hopkins Hospital
5.08
Stollery Children's Hospital
6.8
St Justine Children's Hospital
2.1
McMaster Hospital
8.4
Children's Hospital of Eastern Ontario
7.22
Centre Mere-Enfant du CHUQ
2.07
London Health Sciences Center
6.98
South Eastern Ontario Health Sciences Centre
7.0
St George's Hospital
Children's Medical Center Dallas
IWK Health Centre
Alberta Children's Hospital
Overall Average Rate

4.46
6.5
2.31
5.4
5.11

Reference: Feudtner 2009 (Reference #108)
8 year cohort
Pennsylvania hospitals from 1994-2001
[includes Referral and Community Hospitals]
678,365 subjects
2,202 deaths during hospitalization

3.2

Analytic Method: Logistic regression
Relative Risk
Baseline Rate
Reduction
0.178
5.1 / 1000 discharges.
0.199
3.2 / 1000 discharges
Assumptions: n=20 hospitals: alpha=0.05, z=1.96, power=80%, average bed size=119.85, length of stay=4,
0.90 average occupancy, k=0.15.

Protocol 005 version date 23 February 2011

Page

29


```


### DOC-002 physical PDF page 30 — exact reusable native text

```text
Evaluating processes of care & the outcomes of children in hospital (EPOCH): a cluster randomized trial of
the Bedside Paediatric Early Warning System.
PI: Christopher Parshuram Research Protocol
[2] Significant Clinical Deterioration Events in four major paediatric referral hospitals in 2007-8
Hospital
Admissions
PICU Beds
PICU Discharges
Unplanned PICU
Admits

55963

62
7300
1052
N
14.5%
/PICU Discharges
18
/1000 Hospital Discharges
PICU Mortality
65
N
following Unplanned
6.2%
/Unplanned Discharges
Admits
1.2
/1000 Hospital Discharges
Total Code Blue
150
N
Events
3
/1000 Hospital Discharges
0.75
/1000 Patient Days
Data are from The Ontario Paediatric Critical Care Response Team Collaborative report (Kotsakis 2009).
They represent 2 years of data from the four largest paediatric referral hospitals in Ontario. In the two years
following 31 January 2007, there were 55963 Hospital Discharges, 1052 Urgent PICU admissions, and 150
Code Blue events (after the introduction of MET-RRT at each site). ICU mortality was overall 6.2% following
urgent ICU admission – lower than the 15.1% in our single center data from an earlier era.
Assuming an average hospital length of stay of 4 days (397,556 patient days /99,389 discharges – data from
participating referral hospitals), we estimate a rate of SCDE of 2/1000 patient days. With 20 sites we will be
able to show a 31% reduction in significant clinical deterioration events (80% power, alpha=0.05, k= 0.15).
This corresponds to an absolute risk reduction of 0.62 events per 1000 patient days.
[3] Code Blue Events
These immediate calls for medical assistance from a resuscitation team occur at a rate of 0.75/1000 Patient
Days. With this rate the maximum relative risk reduction that can be shown with 20 referral hospitals is 0.41
(alpha=0.05, z=1.96, power=80%, an average bed size of 119.85, a length of stay of 4, k=0.15.) This is an
absolute risk reduction of 0.3/1000 events per thousand patient days.
[4] Stat Calls
Method: Poisson regression
Preliminary Data 8.13 stat calls per 1000 patient days at the Hospital for Sick Children. The maximum relative
risk reduction that can be shown is 0.181 (alpha=0.05, z=1.96, power=80%, an average bed size of 119.85, a
length of stay of 4, k=0.15, n=20, baseline rate=8.13 per 1000 patient days). This corresponds to an absolute
risk reduction of 1.45 calls per thousand patient days.

Protocol 005 version date 23 February 2011

Page

30


```

# SAP and Results-Supplement Quantitative Evidence Map

Scope: DOC-003 `joi180015supp2_prod.pdf` PDF pp. 1-7 (PLAN SAP); DOC-004 `joi180015supp3_prod.pdf` PDF pp. 1-14 (REPORT). All 21 assigned reusable-backed pages mapped; fresh-required pages: 0. Runtime ID: 01a129b3-7125-73e0-8869-d73f37059c71. No sources, reused assets, or other agents' files were changed. No old scientific conclusions were used. This is extraction, with no candidate diagnosis.

## Provenance and completeness

Read the complete scope and review contract, current source inventory, source coverage, evidence-asset inventory, coverage manifest and tooling record. The complete reusable layout representations of both assigned sources were read; their page-specific contents are preserved below as locator/transcription aids. The curator established byte-identical current text for DOC-003, readable text for DOC-004 apart from graphical ordering. Native/layout representations are not final authority for a future candidate. All page assignments are explicit below.

CPU visual inspection: DOC-004 pp. 2 and 4 were inspected first in reusable PNGs (original render engine unrecorded), then in fresh direct-source Poppler pdftoppm 25.03.0 120-dpi PNGs. DOC-004 pp. 11 and 12 reusable PNGs were also inspected for table alignment and the printed glyph following 80. No OCR or fallback interpreter was needed. No workbook, formula-cache, CSV, Office, or other structured support source exists in this shard; executable-looking SAP R code is printed plan text, not an executed analysis or workbook formula.

Fresh derivatives, source locations and engines:

| Source unit | Command | Output | Engine/device |
|---|---|---|---|
| DOC-004 p. 2 | `pdftoppm -f 2 -l 2 -singlefile -r 120 -png joi180015supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/sap-results-DOC004-p2` | preprocessing/sap-results-DOC004-p2.png | Poppler pdftoppm 25.03.0; CPU |
| DOC-004 p. 4 | `pdftoppm -f 4 -l 4 -singlefile -r 120 -png joi180015supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/sap-results-DOC004-p4` | preprocessing/sap-results-DOC004-p4.png | Poppler pdftoppm 25.03.0; CPU |

Evidence links below are package-relative from this artifact's directory. Main-paper matching keys name outcomes/analyses and are locator keys for the main mapper/checkers; this shard does not make independent scientific completion claims for main/protocol pages owned by other mappers. `SAP-*` and `RES-*` are bounded extraction keys; downstream inventories assign global N/S IDs without collisions.

## Per-page coverage

| Source/page | Content opened and mapped | Status |
|---|---|---|
| DOC-003 p. 1 | Hospital-level analysis unit; numerator/denominator; GEE; binary links/predictors; beginning R code | COMPLETE |
| DOC-003 p. 2 | Binary group/individual identity-link code; baseline zero handling; count-model specification | COMPLETE |
| DOC-003 p. 3 | Count log/identity R code; person-time scaling; continuous heading | COMPLETE |
| DOC-003 p. 4 | Gaussian patient GEE; eight relative-scale model sensitivity specifications; identity-scale specifications begin | COMPLETE |
| DOC-003 p. 5 | Remaining identity-scale sensitivity specifications; six shell-table outcome/denominator/model mappings | COMPLETE |
| DOC-003 p. 6 | ECMO and MET subgroup analyses; treatment-by-subgroup GEE interaction | COMPLETE |
| DOC-003 p. 7 | Patient-level ICU aggregation, exclusion across periods, nine outcome definitions | COMPLETE |
| DOC-004 p. 1 | Cover/content list: two figures and five tables; no standalone result values | COMPLETE; no-applicable numeric display |
| DOC-004 p. 2 | eFigure 1: all 21 mortality points, treatment/line styles, axes, discharge-size legend; direct-source rendering | COMPLETE |
| DOC-004 p. 3 | eFigure 1 caption, hospital allocation/run-in, size meaning, fit meaning, 0.01 adjusted difference | COMPLETE |
| DOC-004 p. 4 | eFigure 2: all eight bins for both arms, axes/legend; direct-source rendering | COMPLETE |
| DOC-004 p. 5 | eFigure 2 caption; weekly sampling, observation definition; 5420/2588/2832 counts; threshold claim | COMPLETE |
| DOC-004 p. 6 | eTable 1 outcome definitions: death, DNR, composite deterioration, arrest, preventability, urgent ICU, readmissions, VFD start | COMPLETE |
| DOC-004 p. 7 | eTable 1 remaining definitions: calls, documentation, ICU/technology days, PELOD/PIM ranges and transformation | COMPLETE |
| DOC-004 p. 8 | Definition/data-collection note; prespecified perception-survey outcomes not reported | COMPLETE |
| DOC-004 p. 9 | eTable 2: 21 hospital rows plus two arm totals; discharges, death and non-DNR death counts/rates; allocation keys | COMPLETE |
| DOC-004 p. 10 | eTable 2 denominator continuation: discharges and per-thousand scale | COMPLETE |
| DOC-004 p. 11 | eTable 3: 21 hospital rows plus two totals; patient-days and three event count/rate pairs, both periods | COMPLETE |
| DOC-004 p. 12 | eTable 4: 19 displayed outcome rows; 14 difference/95% CI/P triplets; patient counts/exclusion | COMPLETE |
| DOC-004 p. 13 | eTable 4 model/aggregation/footnotes: baseline GEE, mean/risk difference, PIM transform, PELOD range | COMPLETE |
| DOC-004 p. 14 | eTable 5: ten anticipated/actual input/result pairs; Bayesian k interval | COMPLETE |

## PLAN statistical relationships and matching keys

| Key | Source | Complete relationship/specification | Main/report matching key |
|---|---|---|---|
| SAP-01 | [pp. 1-2](../../../joi180015supp2_prod.pdf#page=1) | Primary analysis hospital-level; every hospital observed baseline and intervention. Binary outcome events/discharges; repeatable count events/patient-days. GEE clustered by hospital, exchangeable correlation. | Hospital-level primary mortality and secondary event-rate models |
| SAP-02 | [pp. 1-2](../../../joi180015supp2_prod.pdf#page=2) | Binomial GEE has two analyses: logit for log odds, identity for probability. Predictors intervention indicator and same hospital baseline log odds/probability. Baseline logit calculation adds 0.5 numerator and 1 denominator when x=0. Group OR code `cbind(x,n-x)~Intervention+logitBaseline`, binomial default link. Group and individual RD code use identity link; individual y=1 event, 0 none. | Adjusted mortality OR/RD; mortality without DNR; binary ICU outcomes |
| SAP-03 | [pp. 2-3](../../../joi180015supp2_prod.pdf#page=3) | Poisson GEE repeat-event counts: log link log-rate, identity link rate; intervention plus baseline corresponding log-rate/rate. Narrative says log(patient-days) offset. Baseline log rate adds 0.5 event if x=0. Printed log code `geeglm(x ~offset(log(N)+Intervention + logBaseline, ... corstr="exchangeable"))` is preserved exactly in appendix. | Adjusted secondary count rate ratios and rate differences |
| SAP-04 | [p. 3](../../../joi180015supp2_prod.pdf#page=3) | Identity Poisson code constructs `Nlin <- N/1000`, `GNlin <- N*(d$Group=="BedsidePEWS")`, `EPOCH$$BNlin <- EPOCH$N*(EPOCH$Baseline)`; formula `x~Nlin+GNlin+BNlin-1`. Comments call Nlin usual-care intercept; NlinG rate-difference coefficient; NlinB baseline-rate slope. Exact syntax/labels, not normalized, below. | Count rate-difference implementation and unit per 1000 patient-days |
| SAP-05 | [p. 4](../../../joi180015supp2_prod.pdf#page=4) | Patient continuous outcomes in Tables 2/S4 modeled Gaussian GEE, large-sample robustness rationale; comments y continuous, hospital grouping, x0 hospital baseline mean. Printed response formula `x ~Intervention + x0`; exchangeable correlation. | Documentation/ICU continuous adjusted mean differences |
| SAP-06 | [p. 4](../../../joi180015supp2_prod.pdf#page=4) | Eight logit/log-rate sensitivities: post-only GEE; post-only GLMER; pre+post GEE time-by-treatment; pre+post GLMER time-by-treatment; baseline-adjusted post GEE; baseline-adjusted post GLMER; weighted linear logit/log-rate with weight inverse variance and baseline covariate; quasi-binomial logistic or Poisson regression on post data with baseline logit/log rate. | Model-choice sensitivity reporting |
| SAP-07 | [pp. 4-5](../../../joi180015supp2_prod.pdf#page=5) | Five probability/rate sensitivities: post-only identity GEE; pre+post identity GEE time-by-treatment; baseline-adjusted post identity GEE; weighted linear post probabilities/rates with printed inverse variance-probability or inverse variance-weight wording; quasi-binomial post regression with baseline probability, binomial/Poisson variance and identity link. | Model-choice sensitivity reporting on absolute scale |
| SAP-08 | [p. 5](../../../joi180015supp2_prod.pdf#page=5) | Shell table headed continuous outcomes: resuscitation calls B_rt/B_PatientDays versus P_rt/P_PatientDays; stat calls sc; urgent ICU consultations rr; urgent ICU admissions uicu; unplanned ICU readmissions icur/PatientDischargesICU; unplanned hospital readmission __hr/PatientDischarges. Every row labels Poisson. | Calls, urgent ICU, readmissions denominators |
| SAP-09 | [p. 6](../../../joi180015supp2_prod.pdf#page=6) | Exactly two subgroup analyses: hospitals with/without ECMO service and with/without MET service; same methods; intervention-vs-usual-care estimate within each; single GEE one-term treatment-by-subgroup interaction tests subgroup effect. | ECMO and rapid-response/MET subgroup displays |
| SAP-10 | [p. 7](../../../joi180015supp2_prod.pdf#page=7) | Patient ICU analyses: multiple admissions collapsed to one patient; patients appearing in both periods excluded. Total LOS=sum; average LOS=mean; admission PIM=mean; predicted mortality=inverse-logit mean probability across admissions; VFD=first admission; technology days=sum MV+NO+ECMO+dialysis; any technology use binary (HFOV/ECMO/NO/dialysis/MV); PELOD24h and whole-stay PELOD averaged across admissions. | eTable 4 aggregation/exclusion and main urgent-ICU secondary analyses |

## REPORT figure and definition relationships

RES-01, [eFigure 1 p. 2](../../../joi180015supp3_prod.pdf#page=2) and [caption p. 3](../../../joi180015supp3_prod.pdf#page=3): mortality per 1000 discharges, baseline x-axis versus intervention y-axis; displayed major axis ticks 0,2,4,6 and unit grid. All 21 hospital IDs A-U appear; exact printed point coordinates are the two all-cause mortality rate columns in eTable 2 p. 9, copied completely in the appendix. Direct view has A-J turquoise and K-U salmon; legend Usual Care salmon dotted fitted line, BedsidePEWS turquoise dashed fitted line. Grey dashed diagonal denotes identity. Discharge-size legend 2000,5000,10000,20000. Hospital A/C/H extended run-in. Caption text is preserved verbatim below, including its own color/style description and assertion that fitted lines are visually coincident, no significant primary difference, adjusted absolute difference 0.01 per thousand discharges. Matching main key: primary all-cause mortality, allocation, adjusted RD. No graphical fitted coefficients or numerical CIs are printed; do not manufacture these from image pixels.

RES-02, [eFigure 2 p. 4](../../../joi180015supp3_prod.pdf#page=4) and [caption p. 5](../../../joi180015supp3_prod.pdf#page=5): most-recent documentation contains 0-7 of seven observation types. Y-axis percent of observations (0 through 90 in steps 10), usual-care salmon, BedsidePEWS turquoise. Graphical heights, approximate visual readings only (not numerical labels), are:

| Number observation types | Usual Care approximate % | BedsidePEWS approximate % |
|---:|---:|---:|
| 0 | 1.9 | 0.2 |
| 1 | 3.3 | 0.1 |
| 2 | 4.1 | approximately 0 |
| 3 | 8.7 | 0.1 |
| 4 | 21.0 | 0.5 |
| 5 | 28.4 | 12.5 |
| 6 | 31.7 | 85.7 |
| 7 | 0.8 | 0.8 |

No exact bin counts, numerical bar labels, P value or CI printed. Caption total 5420 post-randomization patients = BedsidePEWS2588 + usual-care2832. Each hospital each study week: five randomly selected inpatients admitted ≥24 h; last simultaneously documented observation set. Types HR, respiratory rate, systolic BP, saturation, respiratory effort, capillary refill, oxygen therapy. Zero possible if temperature only; maximum seven. Narrative states ≥5 types significantly more frequent in BedsidePEWS. Matching key: documentation completeness/frequency/≥5 types in main outcome table.

RES-03, [eTable 1 pp. 6-7](../../../joi180015supp3_prod.pdf#page=6): all outcome definitions preserved in appendix. Quantitative anchors: hospital mortality includes DNR; death without DNR defined at death. Significant deterioration/late ICU composite one-or-more: ventilation at ICU admission/intubation within 1h; >60mL/kg fluid during prior12h and/or inotrope/vasopressor during transfer/prior12h; chest compression before transfer or within1h and/or ECMO before/within1h; ward death or death within1h urgent ICU without DNR. Arrest is subset and includes first1h urgent ICU. Preventability assessed by two blinded reviewers; ratings4,5,6 qualify, rating4 more-than50/50 close call. Urgent ICU departure<6h after initiation; operating/recovery admissions urgent regardless timing. Readmission before third midnight after discharge (second full calendar day). VFD alive/no-invasive-MV over28d beginning admission, first ICU admission each period. Urgent consult requested<15min. Documentation seven types counted across24h in five patients/hospital/week. Whole/part calendar/study days for ICU LOS, MV/dialysis/ECMO/NO; PELOD first24h and whole stay, range0-71, higher worse. PIM2 first12h; larger indicates death risk; minimum -8.4137→0.02%; PaO2=40 and base excess=-35 yields+9.7778→99.9%; no finite upper bound. Matching keys: endpoint definitions, outcome status, ICU resource-use definitions.

RES-04, [p. 8](../../../joi180015supp3_prod.pdf#page=8): explicit statement that prespecified frontline-staff and hospital-administrator perception surveys are not reported here. This page has no further numerical results. Matching key: protocol outcome/status and report omissions.

## REPORT hospital tables

RES-05, [eTable 2 p. 9](../../../joi180015supp3_prod.pdf#page=9) and [denominator p. 10](../../../joi180015supp3_prod.pdf#page=10): exact 21 rows and both totals preserved below. Each row carries baseline discharges, post discharges, total discharges, baseline/all-cause deaths(rate), post deaths(rate), baseline/no-DNR deaths(rate), post/no-DNR deaths(rate). Death rates per1000 discharges, not per patient-days. Each row is its own count/denominator/rate relationship; each hospital's total is baseline+post; every total column is aggregate of respective A-J or K-U cells. eFigure1 uses the same hospital IDs, baseline/post all-cause rates and post discharges for size. BedsidePEWS10 hospitals A-J, usual-care11 K-U, each ordered by ward-bed count. Geography is administrative context only; full text retained.

| Arm | Baseline/post/total discharges | Baseline/post mortality n(rate/1000) | Baseline/post non-DNR mortality n(rate/1000) |
|---|---|---|---|
| BedsidePEWS | 26664 / 50173 / 76837 | 52(1.95) / 97(1.93) | 26(0.98) / 42(0.84) |
| Usual Care | 46718 / 94366 / 141084 | 61(1.31) / 147(1.56) | 16(0.34) / 47(0.50) |

Matching main keys: primary mortality count/discharge distribution, secondary no-DNR mortality, hospital allocation and study flow. No modeled comparative estimate or P value is printed in this table.

RES-06, [eTable 3 p. 11](../../../joi180015supp3_prod.pdf#page=11): exact 21 rows and both totals below. Baseline/post patient-days; deterioration, cardiac-arrest, potentially-preventable-arrest n(rate/1000 patient-days) for each period. Each row is a count/denominator/rate relationship and arm-total aggregation. A-J BedsidePEWS, K-U usual-care. Table numeric data use same hospital IDs as eTable2/eFigure1. The glyph after baseline BedsidePEWS deterioration80 is visually present in the reusable page (appears beta/ß); do not treat as extra digit; raw layout retains `80ß(0.62)`.

| Arm | Baseline/post patient-days | Deterioration baseline/post | Arrest baseline/post | Potentially preventable arrest baseline/post |
|---|---|---|---|---|
| BedsidePEWS | 129700 / 251859 | 80(0.62) / 127(0.50) | 15(0.12) / 27(0.11) | 11(0.08) / 21(0.08) |
| Usual Care | 162497 / 307584 | 144(0.89) / 259(0.84) | 18(0.11) / 32(0.10) | 12(0.07) / 29(0.09) |

Matching main keys: secondary deterioration, arrest and potentially preventable arrest count/rates and hospital/patient-day distributions. No comparative inferential outputs in this table.

## REPORT patient ICU relationships

RES-07, [eTable 4 p. 12](../../../joi180015supp3_prod.pdf#page=12) and [methods/footnotes p. 13](../../../joi180015supp3_prod.pdf#page=13): four descriptive columns are BedsidePEWS baseline, BedsidePEWS post, usual-care baseline, usual-care post. Urgent-ICU patient denominators393,686,531,967. Fifty-five patients(3.2%) with admissions in both periods removed. Four groups' complete descriptive values, including every mean/SD and median/IQR, remain in appendix. There are20 displayed rows:1 contributor,15 inferential,4 median/IQR. All comparisons adjust hospital baseline outcome, cluster by hospital with GEE; continuous outcomes including day counts use linear mean-difference estimates; binary use binomial identity risk differences. Contrast key BedsidePEWS minus usual care post with baseline adjustment, not crude between-column subtraction. Units for binary outputs percentage points; continuous outputs same unit as row. All intervals95%.

| Local statistical key | Outcome | Difference | Lower95% | Upper95% | P | Measure/unit |
|---|---|---:|---:|---:|---:|---|
| RES-07a | ICU mortality | -1.55 | -4.90 | 1.80 | 0.36 | risk difference, percentage points |
| RES-07b | PIM2 predicted mortality | 0.69 | -0.54 | 1.92 | 0.27 | probability difference, percentage points; inverse-logit probabilities |
| RES-07c | PIM2 | 0.13 | -0.11 | 0.37 | 0.29 | mean difference, score |
| RES-07d | Total ICU LOS | 1.28 | -0.97 | 3.53 | 0.27 | mean difference, days/patient |
| RES-07e | Mean ICU LOS | 1.04 | -0.91 | 2.99 | 0.29 | mean difference, days/admission averaged per patient |
| RES-07f | Ventilator-free days | 0.26 | -1.04 | 1.57 | 0.69 | mean difference, days first admission |
| RES-07g | MV days | 0.69 | -0.99 | 2.36 | 0.42 | mean difference, days/patient |
| RES-07h | MV use | -0.93 | -7.46 | 5.61 | 0.78 | risk difference, percentage points |
| RES-07i | HFOV use | -1.17 | -2.52 | 0.19 | 0.09 | risk difference, percentage points |
| RES-07j | Nitric oxide use | -0.38 | -1.91 | 1.15 | 0.63 | risk difference, percentage points |
| RES-07k | ECMO use | -1.03 | -2.45 | 0.38 | 0.15 | risk difference, percentage points |
| RES-07l | Dialysis use | 0.96 | -1.25 | 3.17 | 0.40 | risk difference, percentage points |
| RES-07m | ICU technology days | 1.13 | -0.99 | 3.25 | 0.30 | mean difference, combined days/patient |
| RES-07n | PELOD ICU | -0.12 | -1.62 | 1.37 | 0.87 | mean difference, score |
| RES-07o | PELOD24h | -0.29 | -1.06 | 0.49 | 0.47 | mean difference, score |

Footnote a: eight non-DNR patients died before urgent ICU admission, four per arm. Footnote b: predicted deaths=sum patient inverse logits `1/(1+exp(-PIM))`; rounded nearest integer, percentages of all patients. Means of PIM/PELOD across multiple ICU stays; total and mean LOS both calculated; first-admission VFD. PIM and PELOD range/direction definitions repeated from eTable1. Matching main key: urgent ICU admissions, ICU mortality/resource use and secondary continuous outcomes; match patient analysis to patient analysis, not admission counts.

## REPORT sample-size inputs/results

RES-08, [eTable 5 p. 14](../../../joi180015supp3_prod.pdf#page=14): anticipated versus actual values below. Post-hoc tabulation compares2009 power assumptions with trial quantities; baseline-rate/constant-cluster-size/intercluster-variation labels. k Bayesian recalculation with95% CI0.43(0.17-0.77). Matching main/protocol keys: sample size and power assumptions, achieved primary/event counts, actual intercluster variability.

| Quantity | Anticipated | Actual | Unit |
|---|---:|---:|---|
| Hospitals | 20 | 21 | clusters |
| Ward pediatric beds | 2397 | 2085 | beds |
| Patient discharges | 99389 | 144539 | discharges |
| Patient days | 397556 | 559443 | days |
| Intercluster k | 0.15 | 0.43 | coefficient of variation |
| Between-cluster SD sigma_c | 0.00076 | 0.00071 | mortality probability scale |
| Mortality | 5.1 | 1.7 | per1000 discharges |
| Deaths | 507 | 244 | events |
| Deterioration/late ICU | 2.0 | 0.69 | per1000 patient-days |
| Deterioration events | 795 | 386 | events |

## Limitations and handoff

Scientific coverage gaps: none across21 assigned pages. The graph has unlabeled bar heights and fitted-line coefficients, so approximate graphics cannot be promoted to exact printed values. SAP code is displayed plan code and has not been executed; the supplied package contains no patient/raw datasets for execution, and raw-data audit is outside scope. Existing rendering engine is unrecorded for reusable PNGs; direct-source renders close figure-layout needs on pp.2/4. Old scientific outputs were not read. All direct-source decisions remain for the independent checker/screener/rechecker stages.

The appendix retains all exact hospital-level cells, all patient descriptive values, all code text and all definitions/footnotes, with page delimiters so checkers can reconstruct every relationship rather than rely on summaries.

## Complete source-linked layout transcription: DOC-003

### DOC-003 PDF page 1

```text
 1   Primary / Secondary Analysis
 2
 3
 4   Analysis Plan
 5
 6   The primary analysis was a hospital-level analysis. All hospitals had observations on the baseline
 7   period and on the intervention period. There are two types of outcome variables:
 8           those for which a patient can experience once, such as Hospital Mortality (binary)
 9           those for which a patient can experience more than once, such as Clinical
10              Deterioration Events (count).
11
12   For each outcome a ‘numerator’ and a ‘denominator’ was identified. For a binary outcome, the
13   numerator was the number of events in a hospital during a particular period (baseline or
14   intervention), and the denominator was the number of discharges. For a count outcome the
15   numerator was the number of events in a hospital during a particular period, and the denominator
16   was the number of patient-days. See following table for variable and macro names.
17
18   Generalized estimating equations (GEE) methods were used to account for clustering by
19   hospital, with an exchangeable correlation structure.
20
21   Binary outcomes:
22   For a binary outcome, a GEE binomial model was used. There were two separate analyses, both
23   using the number of events (x) and the number of discharges (n):
24
25   -   a logit link was used, so that the log-odds of the outcome was modelled as a function of the
26       predictors
27   -   an identify link was used, so that the probability of the outcome was modelled as a function
28       of the predictors
29
30   The predictor variables were:
31
32          (1) the treatment dummy indicator and
33          (2) the corresponding summary statistic (log odds or probability) for that hospital during
34          the baseline period.
35
36   R code for GEE model of binary outcomes at the group level
37
38   # load geepack library
39   # n is the number of discharges at a hospital
40   # x is the number of events at that hospital in the post-
41   #   randomization period
42   # Hospital is the categorical variable indicating which hospital
43   #   the above numbers come from
44   # logitBaseline logit of baseline probability for this hospital,

     EPOCH SAP                                                                                           1

```

### DOC-003 PDF page 2

```text
45   #   calculated with addition of 0.5 to numerator and 1 to
46   #   denominator if x = 0
47   # probBaseline baseline probability for this hospital,
48
49
50
51   #model for log-odds of outcome at the group level
52
53   GEEfit.OR <- geeglm(cbind(x, n-x)~Intervention + logitBaseline,
54                             id = Hospital,
55                             family = binomial,
56                             data=EPOCH,
57                             corstr = "exchangeable")
58
59
60   # model for probability of outcome at the group level
61
62   GEEfit.RD <- geeglm(cbind(x, n-x)~Intervention + probBaseline,
63                      id = Hospital,
64                      family =binomial(link=make.link("identity")),
65                      data=EPOCH,
66                      corstr = "exchangeable")
67
68
69   # model for probability of outcome at the indovidual level
70
71   # y = 1 for outcome, 0 for no outcome
72
73   GEEfit.RD <- geeglm(y~Intervention + probBaseline,
74                       id = Hospital,
75                      family =binomial(link=make.link("identity")),
76                      data=EPOCH,
77                      corstr = "exchangeable")
78
79
80   Count outcomes:
81
82   For a count outcome, a GEE Poisson model was used. There were two separate analyses, both
83   using the number of events (x) and the number of patient-days (time):
84
85   -   a log link was used, so that the log-rate was modelled as a function of the predictors
86   -   an identify link was used, so that the rate was modelled as a function of the predictors
87
88   Both models included the number of patient days. With the log link, include log(patient days) as
89   the offset. With the identity link, the code below shows how patient days were included
     EPOCH SAP                                                                                      2

```

### DOC-003 PDF page 3

```text
 90
 91   The predictor variables were
 92           (1) the treatment dummy indicator and
 93           (2) the corresponding summary statistic (log rate or rate) for that hospital during the
 94           baseline period.
 95   See following example R code for details.
 96
 97   # Modelling the log-rate
 98   # N is the number of patient days in the post-randomization
 99   #     period
100   # x is the number of events in the post-randomization period
101   # Hospital is the categorical variable indicating which hospital
102   #   the above numbers come from
103   # logBaseline is log of baseline rate for this hospital,
104   #   calculated with addition of 0.5 to numerator if x = 0
105   # Baseline is baseline rate for this hospital
106
107
108   geefit.RR <- geeglm(x ~offset(log(N)+Intervention + logBaseline,
109                       id = Hospital,
110                       family = poisson,
111                       data=EPOCH,
112                       corstr = "exchangeable"))
113
114   # The linear model needs this rearrangement of the data to
115   # incorporate the time at risk
116   # Nlin – its coefficient is the usual care intercept
117   # NlinG – its coefficient is the rate difference
118   # NlinB – its coefficient is the increase in the rate per unit
119   #    increase of the baseline rate
120
121    EPOCH$Nlin            <- EPOCH$N/1000
122    EPOCH$GNlin           <- EPOCH$N*(d$Group=="BedsidePEWS")
123    EPOCH$$BNlin          <- EPOCH$N*(EPOCH$Baseline)
124
125   # modelling the rate
126
127    geefit.RD <- geeglm(x~Nlin+GNlin+BNlin-1,
128                       id = Hospital,
129                       family = poisson("identity"),
130                       data=EPOCH,
131                       corstr = "exchangeable"))
132
133   Continuous outcomes at the individual level:
134

      EPOCH SAP                                                                                         3

```

### DOC-003 PDF page 4

```text
135   The patient level continuous outcomes in Tables 2 and S4 were also modelled with a GEE, using
136   a Gaussian model. Although the data are not normal at the individual level, the large sample size
137   and the robustness of GEE implies that comparisons of means are largely unaffected by this non-
138   normality.
139
140   For an individual-level outcome, these models all had the same structure
141
142   # y is a continuous outcome for a patient
143   # Hospital is the hospital the patient is in
144   # x0 is the mean value at baseline for the hospital a
145   # patient is in
146
147   geefit.RR <- geeglm(x ~Intervention + x0,
148                       id = Hospital,
149                       data=EPOCH,
150                       corstr = "exchangeable")
151
152
153   Sensitivity to model choice
154
155   As the results of the analysis of cluster RCTs can vary somewhat with the method of analysis,
156   models for odds ratios, probabilities, and rate ratios were also run using several other approaches
157
158   Logit and log-rate models
159      GEE on only post-intervention values
160      Generalized linear mixed effects regression model (GLMER) on only post-intervention
161          values
162      GEE with both pre and post values as outcomes, estimating interaction between time and
163          intervention
164      GLMER with both pre and post values as outcomes, estimating interaction between time
165          and intervention
166      GEE on post-intervention values with baseline value as a covariate
167      Generalized linear mixed effects regression model (GLMER) on post-intervention values
168          with baseline value as a covariate
169      Weighted linear model (weight = 1/(variance of logit) or weight = 1/variance (log-rate)))
170          for logits (or log-rates), with baseline logit (or log-rate)as covariate.
171      Quasibinomial logistic or Poisson regression (which allows for more variance than the
172          binomial or Poisson) on post-data, with baseline logit (or log rate) as covariate
173
174   Models for probability or rate
175       GEE on only post-intervention values (binomial or Poisson variance, identity link)
176       GEE with both pre and post values as outcomes, estimating interaction between time and
177          intervention (binomial or Poisson variance, identity link)


      EPOCH SAP                                                                                         4

```

### DOC-003 PDF page 5

```text
178          GEE on post-intervention values with baseline value as a covariate (binomial or Poisson
179           variance, identity link)
180          Weighted linear model for post-probabilities (weight=1/(variance probability) or
181           1/(variance weight)), with baseline probability or rate as covariate
182          Quasibinomial regression (which allows for more variance than the binomial or Poisson)
183           on post-data, with baseline probability as covariate (binomial or Poisson variance,
184           identity link)
185
186   Shell Tables
187
188   Continuous outcomes
      Resuscitation     B_rt/B_PatientDays            P_rt/P_PatientDays           Poisson
      Team Calls

      Stat Calls        B_sc/B_PatientDays            P_sc/P_PatientDays           Poisson

      Urgent ICU        B_rr/B_PatientDays            P_rr/P_PatientDays           Poisson
      Consultations

      Urgent ICU        B_uicu/B_PatientDays          P_uicu/P_PatientDays         Poisson
      Admissions

      Unplanned ICU     B_icur/                       P_icur/                      Poisson
      Readmissions      B_PatientDischargesICU        P_PatientDischargesICU

      Unplanned         B__hr/                        P__hr/                       Poisson
      Hospital          B_PatientDischarges           P_PatientDischarges
      Readmission
189




      EPOCH SAP                                                                                     5

```

### DOC-003 PDF page 6

```text
190
191
192   Subgroup Analysis Plan
193
194   Two subgroup analyses are planned using the same methodology described in the previous
195   section. In the first, ECMO, the hospitals will be divided into two groups: those that have ECMO
196   service and those who do not. In the second, MET, the hospitals will be divided into two groups:
197   those that have MET service and those who do not.
198
199   For each subgroup analysis, the treatment effect (BedsidePEWS vs. usual care) will be estimated
200   in each group of hospitals and the presence of a subgroup effect will be assessed in a single GEE
201   model with a one-term treatment by subgroup interaction term.
202




      EPOCH SAP                                                                                       6

```

### DOC-003 PDF page 7

```text
203   ICU Analysis
204
205
206   Analysis Plan
207
208   This was a patient-level analysis that followed the same general procedures as outlined above.
209   However, the data has a record for each admission to the ICU, and a patient may have more than
210   one admission; the table below shows how these were handled. Furthermore, a few patients had
211   admissions to the same ICU in both study periods; these patients were eliminated from this
212   analysis. The analysis was done with one record per patient as described in the table below.
213
      Outcome                              Description of the per patient outcome variable


      Total length of stay                 The sum over admissions of the lengths of stay


      Average length of stay               The average over admissions of the lengths of stay


      PIM at admission                     The average over admissions of the PIM at admission


      PIM II Prediction Mortality (/1000   The average probability over admissions of the PIM
      urgent ICU discharges)               II predicted mortality
      (inverse-logit of PIM)

      Ventilation Free Days                The days free of ventilation for the first admission


      Days of technology use               Sum of all days over all admissions of mechanical
                                           ventilation days, nitric oxide days, ECMO days and
                                           dialysis days

      Use of a technology (HFOV,           Binary indicator of whether the technology was used
      ECMO, NO. Dialysis, MV)              on any of the days in the ICU.

      24-hour PELOD                        The average over admissions of the PELOD score for
                                           the first 24 hours

      PELOD ICU Stay                       The average over admissions of the PELOD score for
                                           the entire admission
214




      EPOCH SAP                                                                                    7

```

## Complete source-linked layout transcription: DOC-004

Graphical layout on PDF pp. 2 and 4 is given precedence by the direct visual mapping above. The appendix faithfully retains native extraction ordering and embedded duplicate graphical labels; these are not assumed to be visible extra displays.

### DOC-004 PDF page 1

```text
                                              Supplementary Online Content


Parshuram CS, Dryden-Palmer K, Farrell C, et al, for the Canadian Critical Care Trials Group and the EPOCH
Investigators. Effect of a pediatric early warning system on all-cause mortality in hospitalized pediatric patients: the
EPOCH randomized clinical trial. JAMA. doi:10.1001/jama.2018.0948




eFigure 1. Hospital mortality per thousand hospital discharges
eFigure 2. Documented clinical observations in randomly selected patients
eTable 1. Study outcome definitions
eTable 2. Hospital level outcomes: mortality, mortality without ‘do not resuscitate’ order
eTable 3. Hospital-level outcomes: significant clinical deterioration, cardiac arrest and potentially preventable cardiac
arrest
eTable 4. Per patient analysis of ICU resource utilisation
eTable 5. Study sample pre-trial assumptions and post-trial calculations




This supplementary material has been provided by the authors to give readers additional information about their work.




© 2018 American Medical Association. All rights reserved.

```

### DOC-004 PDF page 2

```text
Figure S1                                                                                                            Hospital mortality per thousand hospital discharges




                                                                                                    Hospital Mortality per 1000 Hospital Discharges
                                                                                                  Hospital Mortality per 1000 Hospital Discharges
                                                                                                             6
                                                                    6




 Deaths perper1000


               1000discharges
                               duringintervention
                                       intervention    period
                                                                                                                                                   H                                            Discharges




                                                     Deaths per 1000 discharges during intervention period
                                                                                                                                                                                                             5000
                                                                                                                                                                                                   Group




    Deaths          discharges during             period
                                                                                                                                                                                                        Usual Care
                                                                                                                                                                                                            10000
                                                                                                             4                                                                                          BedsidePEWS
                                                                    4
                                                                                                                                                                                                             15000
                                                                                                                                                                                                   Discharges
                                                                                                                                                                                                                2000

                                                                                                                 M                   P                 U                                                        5000
                                                                                                                                                                                                             20000


                                                                                                                                                                                                                10000
                                                                                                                                                   G
                                                                                                                                                                                                             25000
                                                                                                             2                                         JE
                                                                    2                                                                                                                                           20000
                                                                                                                                 I
                                                                                                                             S                                                                  Group
                                                                                                                                         Q
                                                                                                                 B                                                                                 Usual Care
                                                                                                                             O
                                                                                                                 L                       R                                                         BedsidePEWS
                                                                                                                            T K                             D
                                                                                                                                                                                        C
                                                                                                                               N
                                                                                                                           F
                                                                                                             0
                                                                    0                                            A
                                                                                                                      0                        2                        4                   6
                                                                                                                 0                 Deaths 2per 1000 discharges during4baseline period   6
                                                                                                                                 Deaths per 1000 discharges during baseline period
                                                                                                                             Deaths per 1000 discharges during baseline period

```

### DOC-004 PDF page 3

```text
All cause hospital mortality rates in baseline and post-randomization periods are presented by hospital. The letter in centre
of each circle is an identifier that can be used to link to other cluster-level (hospital) data in Table S3 and Table S4. Hospitals
A to J inclusive were randomized to the BedsidePEWS and amongst these Hospital A, C and H had extended run-in phases.
Hospitals K to U inclusive were randomized to usual care.
The dashed line is the line of identity where the baseline and post-randomization period mortality rate are the same.
Hospitals implementing the BedsidePEWS are marked in salmon and usual care hospitals are in blue. Each circle represents a
hospital. The circle center reflects the co-ordinates of the baseline and post-randomization mortality rates. The circle size is
proportional to the number of discharges during the intervention period of that hospital. Thus hospital with larger circles are
contributing more data and will have narrower 95% confidence intervals for the true values of their mortality rates.
The colored lines represent the linearized fitted relationships between mortality in baseline and post-randomization phases
in intervention (dotted salmon line) and usual care hospitals (dashed blue line). These lines are visually co-incident -
consistent with the finding of no significant difference in the primary analysis and the baseline adjusted absolute difference
of 0.01 per thousand patient discharges.




© 2018 American Medical Association. All rights reserved.

```

### DOC-004 PDF page 4

```text
            Figure S2                            Documented clinical observations in randomly selected patients




                                        90
                                                       Group
                                                          UsualCare
                                                          Usual  Care
                                        80                BedsidePEWS
                                                          BedsidePEWS


                                                       Discharges
        3                                    4             5    2000    6        7
       Number 4of70Vitals                           5             6         7
                                                                5000
umber of Vitals
                                                                10000
                                        60




            Percent of Observations
                                                                20000




               Percentage of Patients
                                        50




                                        40




                                        30
                                             6
riod

                                        20




                                        10




                                         0


                                                   0                1       2         3           4          5          6     7
                                                                                     Number in
                                                               Number clinical observations  of most
                                                                                                Vitals recent documentation

```

### DOC-004 PDF page 5

```text
Each study week at each hospital, five patients who had been admitted to an inpatient ward for at least 24-hours were
randomly selected for documentation review. Documentation of Heart Rate, Respiratory Rate, Systolic Blood Pressure,
Saturation, Respiratory Effort, Capillary Refill, and Oxygen Therapy measurements were reviewed by trained study co-
ordinators. The most recent set of clinical observations was identified and the number of different types of these clinical
observations was abstracted. A set of clinical observations was regarded as those that were documented as being from the
same time. The minimum number of clinical observations from the seven in the BedsidePEWS score was zero (for example if
only temperature was documented) and the maximum was seven (if all clinical observation types in the BedsidePEWS score
were used).
The figure describes the last set of clinical observations taken from 5420 randomly selected patients in the post-
randomization period. The histogram shows the relative frequency distributions in 2588 patients in BedsidePEWS hospitals
and 2832 patients in usual care hospitals. Few of these randomly selected patients had 7 clinical observation types
documented, however the proportion of observation sets with 5 or more clinical observation types was significantly greater
in BedsidePEWS hospitals than usual care hospitals.




© 2018 American Medical Association. All rights reserved.

```

### DOC-004 PDF page 6

```text
eTable 1. Study outcome definitions

Study Outcome                       Definition
Hospital Mortality                  Death of an eligible inpatient as determined by local practice. This definition intentionally
                                    included children with Do Not Resuscitate orders (DNR), to ensure that we did not exclude
                                    children who had survived earlier resuscitation events that may have been impacted by the
                                    intervention.
Mortality without Not For           Death in an eligible patient where there was not a documented Do Not Resuscitate order at
Resuscitation Order                 the time of death.
Significant Clinical                Late ICU Admission was defined using the Children’s Resuscitation Intensity Scale. It was a
Deterioration Event (Late           composite measure comprised of one or more of:
ICU Admission)                      [a] Intubation and/or receiving endotracheal ventilation at the time of ICU admission or
                                    intubated within 1 hour after Urgent ICU admission
                                    [b] >60 ml/kg intravenous or intraosseous fluid resuscitation given in the 12 hours before
                                    transfer, and/or administration of any intravenous or intraosseous inotrope or vasopressor at
                                    the time of transfer or at any stage in the 12 hours before transfer.
                                    [c] Chest compressions (cardiopulmonary resuscitation) before transfer from ward area or
                                    within 1 hour of ICU admission or ECMO instituted before or within 1 hour of ICU admission.
                                    [d] Death on an inpatient ward, or within an hour of urgent ICU admission in patients without
                                    DNR order. Death may have occurred despite cardiopulmonary resuscitation or if there was
                                    the intent to perform cardiopulmonary resuscitation and patient was pronounced dead
                                    without cardiopulmonary resuscitation.
Cardiac Arrest                      The provision of chest compressions for clinical signs of low or absent cardiac output in
                                    eligible patients without a Do Not Resuscitate Order. Cardiac arrest could also occur in eligible
                                    patients without DNR, with vital signs absent, where chest compressions were not started, and
                                    the patient was determined to have died. Cardiac Arrest was a subset of the above clinical
                                    deterioration event, and included events occurring within in the first hour of urgent ICU
                                    admission.
Potentially Preventable             The potential preventability of cardiac arrest events was the degree to which ‘events may have
Cardiac Arrest                      been avoided given the application of reasonable current standards of practice by an average
                                    practitioner and system anticipated to manage the condition in question’
                                    Assessment of the potential preventability of cardiac arrest was made for all cardiac arrests.
                                    Anonymized, delinked clinical data was presented in a standardized format and potential
                                    preventability was rated by two blinded physician reviewers. Potential preventability ratings of
                                    4: ‘more than likely (more than 50/50, but “close call”);’ 5: ‘strong evidence of preventability;’ 6:
                                    ‘virtually certain evidence of preventability’ were defined as ‘potentially preventable’ cardiac
                                    arrest events.
Urgent ICU Admission                Was an admission to the Pediatric ICU with departure from the event location in less than six
                                    hours from the time the ICU admission was initiated. Initiation was defined as the time when
                                    the ICU admission was confirmed, or confirmed as a ‘definite possibility following surgery’ in
                                    cases where post-operative care in the ICU might be required. ICU admissions initiated intra-
                                    operatively or from the recovery room were regarded as urgent ICU admissions, irrespective of
                                    the time between initiation and departure from the Operating room.
Unplanned ICU                       Re-admission before midnight of the second full calendar day after ICU discharge. Thus, re-
Readmission                         admission occurred before the 3rd midnight following ICU discharge.
Unplanned Hospital                  Re-admission to any inpatient area in the hospital before midnight of the second day full
Readmission                         calendar day after discharge. Thus, re-admission occurred before the 3rd midnight following
                                    hospital discharge.
Ventilator-free Days                Days alive and without invasive mechanical ventilation in the 28 days beginning at ICU
© 2018 American Medical Association. All rights reserved.

```

### DOC-004 PDF page 7

```text
Study Outcome                       Definition
                                    admission. This was recorded for the first ICU admission during each of the baseline and the
                                    post-randomization periods.
Urgent Consultations to the         New urgent consultations were the consultation to ICU expertise – as one or both of an ICU
ICU or Rapid Response               consultation or formal rapid response team for an eligible patient in an eligible inpatient unit.
team                                Consultations were requested to occur in less than 15 minutes. Planned reviews of patients
                                    previously consulted were excluded. Patients who have been previously consulted on were
                                    regarded as having a new consult if an urgent call was made that resulted in an unplanned or
                                    earlier than planned review.
Immediate (‘Stat’) Calls to         Calls for immediate specific physician attendance to provide patient care to an eligible patient
Physicians                          admitted to an inpatient ward.
Immediate Call to                   Calls for immediate medical assistance from the resuscitation team and equipment for an
Resuscitation Team                  eligible patient in an eligible inpatient unit.
Documentation Frequency             The frequency with which each of the clinical observations of the BedsidePEWS score (heart
                                    rate, respiratory rate, systolic blood pressure, transcutaneous oxygen saturation, respiratory
                                    effort, oxygen therapy, capillary refill) were documented in 24 hours. These data were
                                    abstracted from five randomly selected eligible patients each week in each hospital.
ICU Length of Stay                  The number of whole or part study days (00:00:00 – 23:59:59) a given patient was in the ICU.
ICU Mortality                       Death in ICU of an eligible patient, either during the course of an urgent or elective ICU
                                    admission
Mechanical Ventilation              The number of whole or part calendar days of invasive mechanical ventilation provided during
Days                                the ICU stay
Dialysis Days                       The number of whole or part calendar days of dialysis provided during the ICU stay. ‘Dialysis’
                                    included hemo-filtration and hemodialysis techniques used either intermittently and
                                    continuously (or both), peritoneal dialysis, plasmaphersis and red-cell exchange.
ECMO Days                           The number of whole or part calendar days of extracorporeal membrane oxygenation therapy
                                    provided during the ICU stay
Nitric Oxide Days                   The number of whole or part study days of inhaled nitric oxide therapy provided during the
                                    ICU stay.
PELOD                               The Pediatric Logistic Organ Dysfunction score was calculated for the first 24 hours after ICU
                                    admission and for the ICU stay.
                                    Scores for Pediatric Logistic Organ Dysfunction (PELOD) can range from 0 to 71; higher PELOD
                                    score describes more severe organ dysfunction.
Pediatric Index of Mortality        The Pediatric Index of Mortality (version 2) was calculated from diagnosis and physiologic data
                                    from the first 12 hours of urgent ICU admission. A greater PIM-2 score indicates greater
                                    probability of death. The minimum possible score of -8.4137 corresponds to 0.02% predicted
                                    ICU mortality. Technically the PIM-2 score has no upper bound due to the possible inputs for
                                    Base Excess and PaO2. However, with Pa02 of 40 and BE at -35 the PIM score is +9.7778 and
                                    predicted mortality is 99.9%.




© 2018 American Medical Association. All rights reserved.

```

### DOC-004 PDF page 8

```text
The study outcomes are presented with the definitions applied at each site. Data were collected by research coordinators
trained by the research team at the data coordinating center (Center for Safety Research). Data quality review included
review for completeness of case report forms, source data verification, and electronic review for internal consistency of
submitted data. The pre-specified outcomes not reported here are those from the perception surveys of frontline staff and
hospital administrators.

ICU: Intensive Care Unit; DNR Do Not Resuscitate; ECMO: Extracorporeal Membrane Oxygenator Therapy.




© 2018 American Medical Association. All rights reserved.

```

### DOC-004 PDF page 9

```text
eTable 2. Hospital level outcomes: mortality, mortality without ‘do not resuscitate’ order

      Discharges                                            Mortality                           Mortality without DNR
      Baseline   Post-                       Total          Baseline      Post-                 Baseline        Post-randomization
      n          randomization               n              n (/103       randomization         n (/10 3
                                                                                                                n (/103 discharges)
                 n                                          discharges)   n (/103 discharges)   discharges)

Hospitals with Bedside Paediatric Early Warning System
A   467          837                1304       0 (0)                      0 (0)                 0 (0)           0 (0)
B   677          1643               2320       0 (0)                      2 (1.22)              0 (0)           0 (0)
C   663          1250               1913       4 (6.03)                   1 (0.8)               2 (3.02)        1 (0.80)
D   1256         2915               4171       4 (3.18)                   2 (0.69)              2 (1.59)        0 (0)
E   2131         4287               6418       6 (2.82)                   9 (2.10)              5 (2.35)        6 (1.4)
F   4143         8049               12192      3 (0.72)                   3 (0.37)              1 (0.24)        1 (0.12)
G   3689         7037               10726      9 (2.44)                   18 (2.56)             3 (0.81)        3 (0.43)
H   2022         4034               6056       5 (2.47)                   21 (5.21)             0 (0)           13 (3.22)
I   6698         11370              18068      8 (1.19)                   22 (1.93)             8 (1.19)        14 (1.23)
J   4918         8751               13669      13 (2.64)                  19 (2.17)             5 (1.02)        4 (0.46)

All   26664          50173                   76837          52 (1.95)     97 (1.93)             26 (0.98)       42 (0.84)

Hospitals with Usual Care
K   3472         7285                        10757          4 (1.15)      6 (0.82)              1 (0.29)        1 (0.14)
L   2526         5642                        8168           0 (0)         5 (0.89)              0 (0)           2 (0.35)
M 1978           3811                        5789           0 (0)         12 (3.15)             0 (0)           2 (0.52)
N   1762         3672                        5434           2 (1.14)      2 (0.54)              1 (0.57)        0 (0)
O   2232         4638                        6870           2 (0.90)      5 (1.08)              0 (0)           1 (0.22)
P   2819         5471                        8290           4 (1.42)      17 (3.11)             1 (0.35)        7 (1.28)
Q   3497         6440                        9937           6 (1.72)      9 (1.4)               1 (0.29)        4 (0.62)
R   3545         7327                        10872          6 (1.69)      7 (0.96)              1 (0.28)        2 (0.27)
S   3266         5886                        9152           3 (0.92)      9 (1.53)              0 (0)           6 (1.02)
T   13308        26956                       40264          11 (0.83)     21 (0.78)             7 (0.53)        8 (0.30)
U   8313         17238                       25551          23 (2.77)     54 (3.13)             4 (0.48)        14 (0.81)

All   46718          94366                   141084         61 (1.31)     147 (1.56)            16 (0.34)       47 (0.50)

Data are from 21 hospitals in the EPOCH Cluster Randomized Trial of the Bedside Paediatric Early Warning System
(BedsidePEWS) versus usual care. The participating hospitals were in Belgium (Queen Fabiola Children’s University Hospital,
Brussels); Canada (Alberta Children’s Hospital, Calgary; British Columbia Children’s Hospital, Vancouver; Children’s Hospital –
London Health Sciences Centre, London; CHU de Quebec – Universite Laval, Quebec city; CHU Sainte-Justine, Montréal;
Izaak Walton Killam Health Centre, Halifax; McMaster Children’s Hospital, Hamilton; Montreal Children’s Hospital, Montreal;
Saint John Regional Hospital, Saint John; SickKids, Toronto; Stollery Children’s Hospital, Edmonton; Victoria General Hospital,
Victoria); Ireland (Temple Street Children’s University Hospital, Our Lady’s Children’s Hospital, both in Dublin); Italy (Bambino
Gesù Children’s Hospital, IRCCS, Rome); New Zealand (Starship Children’s Hospital, Auckland); The Netherlands (Erasmus MC
Sophia, Rotterdam); and United Kingdom (St Georges University Hospitals NHS Foundation Trust, Kings College Hospital
NHS Foundation Trust , Imperial College Healthcare NHS Trust, Bart’s Health NHS Trust, The Royal Brompton & Harefield
NHS Trust all in London).

The letter in the first column is an identifier that can be used to link to other cluster-level (hospital) data in Table S3 and
Figure S1. Hospitals A to J inclusive were randomized to the BedsidePEWS and are ranked from least to greatest number of
pediatric ward beds. Hospitals K to U inclusive were randomized to usual care. They are ranked from the least to the greatest
number of pediatric ward beds.

© 2018 American Medical Association. All rights reserved.

```

### DOC-004 PDF page 10

```text
The numbers of discharges from the baseline and post-randomization periods are used as denominators to calculate
mortality rates per thousand hospital discharges. These data were reviewed and approved by site investigators at each site.




© 2018 American Medical Association. All rights reserved.

```

### DOC-004 PDF page 11

```text
eTable 3. Hospital-level outcomes: significant clinical deterioration, cardiac arrest, potentially preventable cardiac arrest

      Patient Days                      Significant Clinical             Cardiac Arrest               Potentially Preventable
                                        Deterioration                                                 Cardiac Arrest
      Baseline     Post-                Baseline     Post-               Baseline    Post-            Baseline      Post-
                   Randomization                     Randomization                   Randomizatio                   Randomizatio
                                                                                     n                              n
      N            N            n/103        n/103 patient-              n/103       n/103 patient-   n/103
                                                                                                                    n/103 patient-
                                patient-     days                        patient-    days             patient-      days
                                days                                     days                         days
Hospitals with Bedside Paediatric Early Warning System
A    1133      2270             0 (0)        0 (0)                       0 (0)       0 (0)            0 (0)        0 (0)
B    1876      5135             1 (0.53)     0 (0)                       0 (0)       0 (0)            0 (0)        0 (0)
C    5283      10443            4 (0.76)     8 (0.77)                    2 (0.38)    1 (0.10)         2 (0.38)     1 (0.10)
D    4965      9555             11 (2.22)    11 (1.15)                   1 (0.20)    2 (0.21)         1 (0.20)     2 (0.21)
E    8662      17779            9 (1.04)     15 (0.84)                   0 (0)       1 (0.06)         0 (0)        1 (0.06)
F    10392     23522            5 (0.48)     7 (0.30)                    2 (0.19)    3 (0.13)         1 (0.10)     2 (0.09)
G    17238     34438            19 (1.10)    23 (0.67)                   5 (0.29)    9 (0.26)         4 (0.23)     8 (0.23)
H    23244     47145            13 (0.56)    21 (0.45)                   2 (0.09)    3 (0.06)         1 (0.04)     2 (0.04)
I    30571     56231            10 (0.33)    23 (0.41)                   2 (0.07)    5 (0.09)         1 (0.03)     3 (0.05)
J    26336     45341            8 (0.30)     19 (0.42)                   1 (0.04)    3 (0.07)         1 (0.04)     2 (0.04)

All    129700      251859               80ß(0.62)       127(0.50)        15 (0.12)   27(0.11)         11 (0.08)    21 (0.08)

Hospitals with Usual Care
K    10164      22431                   5 (0.49)            8 (0.36)     1 (0.10)    0 (0)            1 (0.10)     0 (0)
L    6655       13034                   13 (1.95)           27 (2.07)    1 (0.15)    0 (0)            0 (0)        0 (0)
M    8941       16388                   4 (0.45)            18 (1.10)    0 (0)       3 (0.18)         0 (0)        3 (0.18)
N    8917       16888                   1 (0.11)            1 (0.06)     1 (0.11)    0 (0)            1 (0.11)     0 (0)
O    11705      22810                   6 (0.51)            13 (0.57)    1 (0.09)    2 (0.09)         1 (0.09)     1 (0.04)
P    12126      22113                   3 (0.25)            5 (0.23)     2 (0.16)    2 (0.09)         2 (0.16)     2 (0.09)
Q    13335      25093                   11 (0.82)           10 (0.4)     2 (0.15)    4 (0.16)         1 (0.07)     4 (0.16)
R    16077      33678                   9 (0.56)            17 (0.5)     2 (0.12)    4 (0.12)         2 (0.12)     4 (0.12)
S    14304      24762                   1 (0.07)            5 (0.20)     0 (0)       0 (0)            0 (0)        0 (0)
T    28698      49117                   41 (1.43)           62 (1.26)    2 (0.07)    5 (0.10)         1 (0.03)     4 (0.08)
U    31575      61270                   50 (1.58)           93 (1.52)    6 (0.19)    12 (0.20)        3 (0.10)     11 (0.18)

All    162497        307584             144 (0.89)          259 (0.84)   18 (0.11)   32 (0.10)        12 (0.07)    29 (0.09)

Data are from 21 hospitals in the EPOCH Cluster Randomized Trial of the Bedside Paediatric Early Warning System
(BedsidePEWS) versus usual care. The letter in the first column is an identifier that can be used to link to other cluster-level
(hospital) data in Table S2 and Figure S1. Hospitals A to J inclusive were randomized to the BedsidePEWS and are ranked
from least to greatest number of pediatric ward beds. Hospitals K to U inclusive were randomized to usual care. They are
ranked from the least to the greatest number of pediatric ward beds. The numbers of patient days from the baseline and
post-randomization periods are used as dominators to calculate event rates per thousand patient days. These data were
reviewed and approved by site investigators at each site.




© 2018 American Medical Association. All rights reserved.

```

### DOC-004 PDF page 12

```text
eTable 4. Per patient analysis of ICU resource use

                                  BedsidePEWS                   Usual Care
                                           Post-                          Post-               Difference              p-
                               Baseline    Randomization     Baseline     Randomization       (95% CI)                value
Urgent ICU Admission
                               393             686           531           967                -                       -
 N
Mortality (%)a
                               31 (7.9%)       42 (6.1%)     28 (5.3%)     67 (6.9%)          -1.55 (-4.90 to 1.80)   0.36
 N (%)
PIM-2 Predicted
Mortalityb                     21 (5.4%)       38 (5.5%)     25 (4.8%)     44 (4.6%)          0.69 (-0.54 to 1.92)    0.27
 N (%)
PIM-2c
                               -4 (1.6)        -3.9 (1.5)    -3.9 (1.4)    -3.9 (1.3)         0.13 (-0.11 to 0.37)    0.29
 mean (std dev)
ICU Total LOS
                               8.6 (14.6)      9.4 (14.2)    9.4 (14.5)    9 (15)             1.28 (-0.97 to 3.53)    0.27
 mean (std dev)
ICU Total LOS
                               4 (2, 8)        4 (2, 9)      5 (2, 9.5)    4 (2, 9)           -                       -
 median (IQR)
ICU Mean LOS
                               7.4 (12.3)      7.8 (11.2)    8 (12.4)      7.4 (12)           1.04 (-0.91 to 2.99)    0.29
 mean (std dev)
ICU Mean LOS
                               4 (2 -8)        4 (2 -8)      4 (2-8)       4 (2-8)            -                       -
 median (IQR)
Ventilator free days
                               23.7 (8.0)      23.9 (7.8)    24.3 (7.0)    24 (7.6)           0.26 (-1.04 to 1.57)    0.69
 mean (std dev)
Ventilator free days
                               28 (23, 28)     28 (24, 28)   28 (24, 28)   28 (24, 28)                                -
 median (IQR)
MV Days
                               3.9 (10.6)      4.1 (10.1)    4 (10.3)      3.7 (10.3)         0.69 (-0.99 to 2.36)    0.42
 mean (std dev)
MV Use                                                       220
                               164 (41.7%)     287 (41.8%)                 400 (41.4%)        -0.93 (-7.46 to 5.61)   0.78
 N (%)                                                       (41.4%)
HFOV Use
                               23 (5.9%)       25 (3.6%)     15 (2.8%)     30 (3.1%)          -1.17 (-2.52 to 0.19)   0.09
 N (%)
Nitric Oxide Use
                               19 (4.8%)       27 (3.9%)     20 (3.8%)     29 (3%)            -0.38 (-1.91 to 1.15)   0.63
 N (%)
ECMO Use
                               10 (2.5%)       9 (1.3%)      6 (1.1%)      17 (1.8%)          -1.03 (-2.45, 0.38)     0.15
 N (%)
Dialysis Use
                               9 (2.3%)        27 (3.9%)     12 (2.3%)     27 (2.8%)          0.96 (-1.25 to 3.17)    0.40
 N (%)
ICU Technology Days
 mean (std dev)                4.6 (12.2)      5.1 (13.9)    4.5 (11.4)    4.1 (11.3)         1.13 (-0.99 to 3.25)    0.30

ICU Technology Days
                               0 (0-5)         0 (0- 4)      0 (0- 4)      0 (0- 4)           -                       -
 median (IQR)
PELOD ICUd
                               9.3 (9.4)       9.6 (9)       10.2 (9.9)    10 (9.4)           -0.12 (-1.62 to 1.37)   0.87
 mean (std dev)
PELOD 24hd
                               6.7 (7.7)       6.6 (7.4)     6.9 (7.5)     7 (7.6)            -0.29 (-1.06 to 0.49)   0.47
 mean (std dev)

Analyses of Urgent ICU admission were performed using patient-level data. The 55 patients (3.2%) who had admissions in
both periods were removed from this analysis. For proportions of patients the denominators were the number of patients
admitted in each period. Both the per-patient total and per-patient mean duration of ICU stay were calculated to account for
patients with more than one admission in a particular period (baseline or post-randomization). The per-patient mean values

© 2018 American Medical Association. All rights reserved.

```

### DOC-004 PDF page 13

```text
of PIM-2 and PELOD across all ICU stays were used for patients with more than one admission. The number of Ventilator
Free Days was calculated for the first ICU admission only.
Data are presented as mean and standard deviations, and for ICU length of stay, Ventilator Free Days and the Number of
ICU Technology days per patient the median and interquartile range data are also presented. All comparisons adjusted for
the hospital-specific baseline value of each outcome and used generalized estimating equation approach to account for
clustering within hospital. Comparisons for continuous variables (including those that count numbers of days) used a linear
model to estimate mean differences (and their 95% CIs) and comparisons for binary variables used a binomial model with an
identity link to estimate risk differences (and their 95% CIs).

BedsidePEWS; Bedside Paediatric Early Warning System; ICU Intensive Care Unit; PIM-2: Pediatric Index of Mortality version
2; MV Mechanical Ventilation; HFOV High Frequency Oscillatory Ventilation; ECMO Extra Corporeal Membrane Oxygenator
therapy; PELOD: pediatric logistic organ dysfunction; 95%CI: Ninety-five percent Confidence Interval for the associated
estimate. IQR Interquartile range; Std. dev.; Standard deviation.

a. Eight patients without Do Not Resuscitate Orders Died before urgent ICU admission. There were 4 in each group.
b. PIM-2 predicted total mortality was calculated by summing the inverse logit (1/(1+exp(-PIM)) of the PIM-2 score from
each patient. Predicted numbers were rounded to the nearest integer and also shown as a percentage of the total number of
patients.
c. Severity of illness at ICU admission used the Pediatric Index of Mortality (PIM-2). A greater PIM-2 score indicates greater
probability of death. The minimum possible score of -8.4137 corresponds to 0.02% predicted ICU mortality. Technically the
PIM-2 score has no upper bound due to the possible inputs for Base Excess and PaO2. However, with Pa02 of 40 and BE at -
35 the PIM score is +9.7778 and predicted mortality is 99.9%.
d. In-ICU organ dysfunction used the PEdiatric Logistic Organ Dysfunction (PELOD) score for the first 24 hours and for the
duration of ICU. Scores for PELOD can range from 0 to 71; higher PELOD score describes more severe organ dysfunction.




© 2018 American Medical Association. All rights reserved.

```

### DOC-004 PDF page 14

```text
eTable 5. Study sample pre-trial assumptions and post-trial calculations

                                                    Anticipated   Actual
Hospitals                                           20            21
Pediatric Beds (ward)                               2397          2085

Patient discharges                                   99,389       144,539
Patient days                                        397,556       559,443
Inter-cluster coefficient of variation (k)          0.15          0.43
Between cluster standard deviation                  0.00076       0.00071
(σc)
Mortality                                           5.1           1.7
   /1000 patient discharges
Deaths                                              507           244
SCDE (Late ICU admission)                           2.0           0.69
 /1000 patient days
SCDE events                                         795           386

Post-hoc tabulation of assumptions used for the power calculation (baseline rates, constant cluster size, inter-cluster
variation) showing important differences between the best available 2009 calculations and those derived from the trial data.
The k (CV) and its 95% confidence interval were recalculated using Bayesian methods to be 0.43 (0.17-0.77).
Amongst the studied hospitals there were fewer pediatric ward (non-ICU) beds, and more patient-discharges and patient-
days than were initially anticipated. Amongst study outcome events, there were fewer events than anticipated – with half the
number of deaths and significant clinical deterioration events.

SCDE; Significant Clinical Deterioration Event. ICU; Intensive Care Unit.




© 2018 American Medical Association. All rights reserved.

```

## Source-render alignment from independent quality audit

Protocol p.11 visually prints ≥4 for preventability, consistent with ratings 4,5,6 and p.28; native text omits the underline. The raw layout appendix remains a locator transcription; the source rendering is authoritative. This comparator alignment creates no new supplied-source candidate.
