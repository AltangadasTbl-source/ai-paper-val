# Support Quantitative Evidence Map

## Scope and method

Fresh direct-source mapping of DOC002 (`joi180054supp1_prod.pdf`, protocol, PDF pp. 1-25) and DOC003 (`joi180054supp2_prod.pdf`, supplementary online content, PDF pp. 1-13). Evidence was read from the fresh CPU-OCR page text in `preprocessing/ocr_text/` and visually checked against the fresh rendered PNGs for DOC003 pp. 2 and 4, whose table/figure layout was material. This is an evidence inventory, not candidate adjudication. Provisional IDs are local to this file and must be renumbered by the coordinator into package-wide `N`/`S` inventories.

Matching-main keys are descriptive keys for later cross-source matching; they are not assertions that the main paper uses identical wording.

## DOC002 — protocol quantitative and inferential relationships

| Local ID | Exact support location | Printed evidence / relationship | Population, contrast, time point, labels and units | Matching-main key |
|---|---|---|---|---|
| SUP-N001 | DOC002#page=8-9, §§2.1-2.2 | Primary outcome: first-pass success. It is placement of ETT in trachea on the first attempt. An attempt begins with laryngoscope entering the mouth and ends when the laryngoscope leaves the mouth **or** the operator switches tube device (ETT/bougie), even if the blade remains. | Eligible adult ED orotracheal intubations with a Macintosh blade; bougie vs no-bougie first attempt. Binary success. | PRIMARY_FIRST_ATTEMPT_SUCCESS_DEFINITION |
| SUP-N002 | DOC002#page=9, §2.2(1) | First-pass success without hypoxemia requires both first-pass success and no hypoxemia. Hypoxemia is SpO2 <90% at any point during intubation, or >10% absolute fall from baseline if baseline <90%; observation begins with first attempt and ends 1 minute after ETT-cuff inflation. | Secondary binary outcome; pulse-oximetry percentage and 1-minute window. | FIRST_ATTEMPT_SUCCESS_WITHOUT_HYPOXEMIA |
| SUP-N003 | DOC002#page=9, §2.2(2) | Time to intubation (first attempt only) is elapsed time from beginning of intubation attempt to ETT-cuff inflation when tube is in trachea. | Secondary continuous time outcome, seconds implied by stopwatch procedure. | FIRST_ATTEMPT_DURATION_PROTOCOL_DEFINITION |
| SUP-N004 | DOC002#page=9, §2.2(3-4) | Esophageal intubation is ETT passage into esophagus with subsequent ventilation then removal; a transient passage removed during the attempt does not count. Hypoxemia uses the definition in SUP-N002. | Secondary safety/outcome definitions; binary event. | ESOPHAGEAL_INTUBATION_AND_HYPOXEMIA_DEFINITIONS |
| SUP-N005 | DOC002#page=10, §§3.1-3.2 | Attempts: research assistant observes/records; physician also reports number; discrepancies are resolved by stabilization-case video. SpO2 is recorded at start and every 20 seconds through 1 minute after cuff inflation; lowest SpO2 is also recorded even outside a 20-second interval. Time is recorded by stopwatch; physician form records esophageal intubation. | Outcome measurement rule; 20-second sampling interval and 1-minute post-cuff window. | OUTCOME_ASCERTAINMENT_AND_SPO2_SAMPLING |
| SUP-N006 | DOC002#page=11, §4.1.1 | Eligible patients randomized 1:1 to GEB or no GEB for first attempt; permuted blocks of 2, 4, 6, 8, 10; stratification: (1) any cervical collar, obesity by gestalt, or apparent facial/neck trauma, versus (2) none. | Randomization, allocation and stratification definitions. | RANDOMIZATION_AND_DIFFICULT_AIRWAY_STRATA |
| SUP-S001 | DOC002#page=11, §4.1 | Phase IV, randomized, unblinded, single-center, two-arm trial. Primary aim is whether first-pass success differs by more than 9% absolute between GEB first attempt and no GEB. | Design and stated absolute-difference threshold. | DESIGN_AND_PRIMARY_ABSOLUTE_DIFFERENCE |
| SUP-N007 | DOC002#page=12, §4.3 | Participation starts at enrollment and ends 1 minute after successful intubation; no further patient/EMR data collected. | Follow-up/observation endpoint. | STUDY_DURATION |
| SUP-N008 | DOC002#page=13, §§5.1-5.3 | Primary analysis subgroup is any of: cervical immobility, obesity, large tongue, short neck, small mandible, facial/neck trauma, airway edema, blood in airway, or vomit in airway. All enrolled patients are secondary analysis. Inclusion: ED orotracheal intubation with Macintosh blade (video/direct) and presumed age >=18; exclusions: known upper-airway/perilaryngeal distortion, prisoner/under arrest, known/suspected pregnancy. | Analysis-population and eligibility definitions; 9 listed difficult-airway characteristics. | DIFFICULT_AIRWAY_SUBGROUP_AND_ELIGIBILITY |
| SUP-N009 | DOC002#page=14 | Residents perform approximately 98% of endotracheal intubations, stated in consent/risk justification. | Administrative/contextual quantity; not an outcome. | OPERATOR_CONTEXT |
| SUP-N010 | DOC002#page=17-18, §§7.3-7.5 | Baseline vital signs immediately after randomization; attempt data in real time; second attempt may use any device/strategy. AEs monitored continuously while in ED; DSMB reviews qualifying SAEs; requested assessment within 5 working days. | Data-collection/timing and safety-monitoring rules. | SAFETY_AND_SECOND_ATTEMPT_RULES |
| SUP-S002 | DOC002#page=19, §8.1 | Categorical variables: number and percentage per category, missing category as needed. Continuous: n, mean, median, SD, minimum, maximum. Time-to-event: Kaplan-Meier 25th/50th/75th percentiles with two-sided 95% CIs and percentage censored. Formal hypothesis tests for primary/key secondary outcomes are two-sided at alpha=.05. | Statistical-display and inferential rules. | STATISTICAL_GENERAL_CONSIDERATIONS |
| SUP-S003 | DOC002#page=19, §8.2 | Assumes GEB first-pass success 95% and no-GEB 86% (9% absolute difference); 80% power; 374 difficult-airway patients, 187/group. Plan: enroll 1 calendar year or until 1,000 patients, whichever first; anticipated 30-40% difficult airway; if <374 difficult-airway patients, discuss extension. Stata 12.1 command: `sampsi 0.95 0.86, p(0.8)`. | Planned sample-size calculation and stopping/enrollment quantities. | SAMPLE_SIZE_AND_ENROLLMENT_PLAN |
| SUP-N011 | DOC002#page=20, §8.4.1 | ITT primary-outcome population: all randomized patients endotracheally intubated, excluding intubations with a device other than Macintosh blade. No attempted intubation = screening failure. Main outcome is ITT patients with any difficult-airway characteristic; all enrolled patients also presented. | Analysis-population / denominator definition. | ITT_AND_PRIMARY_ANALYSIS_POPULATION |
| SUP-S004 | DOC002#page=20, §8.5 | Primary outcome: chi-square comparison of treatment groups, primary difficult-airway subset and secondary all-enrolled analysis. Categorical/continuous secondary outcomes: appropriate CI of between-group difference, stratified by any difficult-airway characteristic; other data descriptive. | Planned tests, contrasts, stratification and estimate type. | OUTCOME_ANALYSIS_METHODS |
| SUP-N012 | DOC002#page=20-21, §8.6.1 | If both RA and physician forms missing, review video for first-pass success without hypoxemia; if video unavailable, exclude from analysis. For secondary outcomes, video resolves missing values; if unavailable, exclude from relevant-outcome analysis. | Missing-data/exclusion rule. | MISSING_DATA_RULES |
| SUP-S005 | DOC002#page=21, §8.6.2 | Interim at 500 enrolled, primary outcome only. Stop early only for futility. Sensitivity analysis assumes n=1,000, equal allocation; no-GEB success unchanged in second half; GEB success 15% higher absolute than first half (capped at 100%); stop if no first-pass-success difference. | Interim/futility definition and statistical assumptions. | INTERIM_FUTILITY_ANALYSIS |

### DOC002 page-level disposition (all 25 pages)

| Page | Disposition |
|---:|---|
| 1 | Protocol identity/version dates only; no result-relevant quantitative relationship. |
| 2 | Contents page only; no result-relevant quantitative relationship. |
| 3 | Contents continuation only; no result-relevant quantitative relationship. |
| 4 | Abbreviation list only; no result-relevant quantitative relationship. |
| 5 | Background literature narrative; no protocol result definition or planned analysis relation. |
| 6 | Background external-study counts/rates (301, 99%, 199/200, 96%, 66%) only; not a result of the supplied trial. |
| 7 | Background external-study counts/rates (20/26, 76.9%; 70/88, 79.6%; 3.5%) only; no supplied-trial result. |
| 8 | Study population and primary-outcome heading; mapped in SUP-N001. |
| 9 | Outcome definitions; mapped in SUP-N001 through SUP-N004. |
| 10 | Outcome measurement and SpO2 sampling; mapped in SUP-N005. |
| 11 | Design/randomization/9% aim; mapped in SUP-N006 and SUP-S001. |
| 12 | Safety assessment and one-minute participation endpoint; mapped in SUP-N007 and SUP-N010. |
| 13 | Eligibility and difficult-airway primary subgroup; mapped in SUP-N008. |
| 14 | Consent/administrative text plus 98% operator-context statement; mapped in SUP-N009. |
| 15 | Consent rationale only; no result-relevant quantitative relationship. |
| 16 | Consent/notification timing (study complete one minute after successful intubation); corroborates SUP-N007. |
| 17 | Data collection, second attempt, safety; mapped in SUP-N010. |
| 18 | AE/DSMB monitoring and five-working-day assessment; mapped in SUP-N010. |
| 19 | General statistical rules and sample-size plan; mapped in SUP-S002 and SUP-S003. |
| 20 | ITT, outcome-analysis and missing-data rules; mapped in SUP-N011, SUP-S004, SUP-N012. |
| 21 | Missing-data continuation and interim/futility plan; mapped in SUP-N012 and SUP-S005. |
| 22 | DSMB/administrative content; safety-monitoring context mapped in SUP-N010; no further result relation. |
| 23 | Bibliographic references only; no supplied-trial result. |
| 24 | Bibliographic references only; no supplied-trial result. |
| 25 | Bibliographic references only; no supplied-trial result. |

## DOC003 — supplementary results, definitions, and form fields

| Local ID | Exact support location | Printed evidence / relationship | Population, contrast, time point, labels and units | Matching-main key |
|---|---|---|---|---|
| SUP-S006 | DOC003#page=2-3, eTable 1 | eTable accounts for clustering by physician. Primary difficult-airway outcome (N=380): Bougie 191/198, 96% (95% CI 93%-99%); ETT+stylet 150/182, 82% (76%-88%); difference 14% (7%-21%), P<.001, interaction P=.35. Intraclass coefficient <.001 (95% CI <.001 to .03); upper CI bound used. | Primary outcome; difficult-airway population; Bougie vs ETT+stylet. | PRIMARY_DIFFICULT_AIRWAY_CLUSTERED_ANALYSIS |
| SUP-S007 | DOC003#page=2-3, eTable 1 | Difficult-airway planned secondary: success without hypoxemia: 156/191, 82% (76%-87%) vs 123/177, 69% (63%-76%); difference 12% (2%-22%), P=.015, interaction P=.61. First-attempt duration median (IQR): 39 s (29-52) vs 40 s (27-63); difference -1 s (-6 to 3), P=.31, interaction P=.17. | N=380 difficult-airway subgroup. Binary and time outcomes. | DIFFICULT_AIRWAY_SECONDARIES_CLUSTERED |
| SUP-S008 | DOC003#page=2-3, eTable 1 | All-patient outcomes (N=757): overall first-attempt success Bougie 373 (98%, 96%-99%) vs ETT+stylet 328 (87%, 83%-90%), difference 11% (6%-15%), P<.001. Success without hypoxemia: 317/371, 85% (81%-89%) vs 282/366, 77% (72%-81%), difference 8% (2%-15%), P=.02. Duration median (IQR): 38 s (29-51) vs 36 s (25-54), difference 1 s (-1 to 4), P=.95. Interaction is n/a for all-patient analyses. | All randomized patients, group headings Bougie N=381 / ETT N=376; outcome-specific denominators where shown. | ALL_PATIENT_CLUSTERED_SECONDARIES |
| SUP-N013 | DOC003#page=3, eTable footnotes | Table values are no. (%; 95% CI), except duration; difference is proportion or median difference with 95% CI. Columns Bougie/ETT unchanged from primary analysis; difference/P/interaction recalculated for clustering. Hypoxemia: saturation <90%, or baseline <90% with >10% absolute decrease, during or within 1 minute after attempt; valid waveform unavailable for all. Duration: blade entered mouth to blade removed. | Definitions, unit seconds and percentage points; missing waveform caveat. | ETABLE_FOOTNOTES_HYPOXEMIA_DURATION_CLUSTERING |
| SUP-S009 | DOC003#page=4, eFigure 1 | Kaplan-Meier estimates of time until successful first-attempt intubation, all patients. Risk sets/patients not intubated at 0,30,60,90,120,150,180 s: Bougie 381,276,70,19,6,3,0; ETT 376,245,85,19,8,4,2. Log-rank P=.12. Hazard ratio for first-attempt success, Bougie vs ETT+stylet reference, 1.12 (95% CI .97-1.30). Proportional-hazards assumption not upheld; ticks indicate failed attempts. | Time-to-event figure; seconds; all patients. | KM_FIRST_ATTEMPT_DURATION_ALL_PATIENTS |
| SUP-N014 | DOC003#page=5, eFigure 2 | If ETT passage meets arytenoid resistance, withdraw 1-2 cm, rotate 90 degrees counterclockwise, then readvance. | Procedural diagram; centimeters/degrees; not an outcome. | TUBE_PASSAGE_MANEUVER |
| SUP-S010 | DOC003#page=6, eAppendix 1 | Interim after 507 enrolled: Bougie first-pass success 250/257 (97%); ETT+stylet 213/250 (85%). Uses protocol futility assumptions (n=1,000, equal allocation; no-GEB unchanged; GEB 15% absolute higher, capped 100%); trial not stopped for futility. | Interim primary outcome; group denominators sum to 507. | INTERIM_ANALYSIS_OBSERVED_RESULTS |
| SUP-N015 | DOC003#page=7 | Data form: prehospital intubation attempted yes/no; intubator training categories G1, G2, G3, G4+/Fellow, Faculty, PA, Other. Indication requires one best medical or trauma choice; trauma subtype blunt/penetrating. | Case-report-form variable definitions; categorical, no results. | POSTINTUBATION_FORM_BASELINE_VARIABLES |
| SUP-N016 | DOC003#page=8 | Preoxygenation device category is an ordered 0-9 scale (none through other); highest O2 flow is <=15 LPM or flush rate; head-of-bed elevation >=30 degrees yes/no; nasal cannula during attempts yes/no. | Form labels/units, including LPM and degrees. | POSTINTUBATION_FORM_PREOXYGENATION |
| SUP-N017 | DOC003#page=9 | Sedative and paralytic categories; order of sedative/paralytic; intubation-position categories; difficult-airway form items include blood/vomit, short neck, cervical immobilization, small mandible, obesity, obstruction/edema, facial trauma, large tongue. | Form covariates and difficult-airway label set. | POSTINTUBATION_FORM_DIFFICULT_AIRWAY_VARIABLES |
| SUP-N018 | DOC003#page=10 | Attempt #1 begins when laryngoscope blade enters mouth and ends when blade removed. Captures device, video-screen use, first device, and whether initial device successful or switch occurred; bougie-to-ETT switch excludes passage of ETT over bougie. | Attempt/process and switching definitions. | POSTINTUBATION_FORM_ATTEMPT_ONE_DEFINITION |
| SUP-N019 | DOC003#page=11-12 | Attempt #2 uses the same blade-in/blade-out rule and captures device, screen use, first rescue device, success/switch, later course, bougie clicks/hard stop, arytenoid resistance outcomes, and ETT confirmation (waveform CO2, auscultation, sonographic sliding signs, none). | Rescue-attempt, device and confirmation definitions. | POSTINTUBATION_FORM_RESCUE_AND_CONFIRMATION |
| SUP-N020 | DOC003#page=13 | Complications captured as selectable: direct airway injury; witnessed aspiration; cardiac arrest during/within 5 min; cardiac arrest/death in ED at any time; iatrogenic bleeding; pharyngeal laceration; dental/lip trauma; esophageal intubation. | Safety-event labels and 5-minute time boundary. | POSTINTUBATION_FORM_COMPLICATIONS |

### DOC003 page-level disposition (all 13 pages)

| Page | Disposition |
|---:|---|
| 1 | Supplement contents; identifies eTable/eFigure/appendices but contains no additional result. |
| 2 | eTable result rows; mapped in SUP-S006 through SUP-S008. Rendered PNG visually checked. |
| 3 | eTable footnotes and analysis definitions; mapped in SUP-N013. |
| 4 | Kaplan-Meier figure, risk sets, HR/CI/log-rank P and PH caveat; mapped in SUP-S009. Rendered PNG visually checked. |
| 5 | Procedural figure with 1-2 cm and 90-degree maneuver; mapped in SUP-N014. |
| 6 | Interim observed results and futility decision; mapped in SUP-S010. |
| 7 | Postintubation form baseline variables; mapped in SUP-N015. |
| 8 | Postintubation form preoxygenation definitions/scales; mapped in SUP-N016. |
| 9 | Postintubation form medication, position and difficult-airway fields; mapped in SUP-N017. |
| 10 | First-attempt timing/device/switch definitions; mapped in SUP-N018. |
| 11 | Second-attempt timing/device definitions; mapped in SUP-N019. |
| 12 | Second-attempt result/confirmation and bougie-event fields; mapped in SUP-N019. |
| 13 | Complication labels and timing boundary; mapped in SUP-N020. |

## Cross-document matching signals for later review (not candidate IDs)

1. **Time-to-intubation definition requires exact matching.** DOC002#page=9 defines time from beginning of attempt to ETT-cuff inflation (SUP-N003). DOC003#page=3 defines duration from blade entering mouth to blade removal (SUP-N013); DOC003#page=4 describes time until successful intubation (SUP-S009). These are not textually identical endpoints. Later reviewers must determine whether they refer to a matched reported endpoint and, if so, whether the main paper explains an amendment or separate measure. No candidate is assigned here.

2. **Attempt boundary/switch rule requires exact matching.** DOC002#page=9 makes switching tube device an end of the first attempt even if the blade remains in the mouth (SUP-N001), whereas DOC003#page=10 defines the form's attempt boundary as blade-in to blade-out while separately recording a device switch (SUP-N018). Later matching must determine how first-attempt success was operationalized in reported analyses. No candidate is assigned here.

3. **Primary difficult-airway denominators.** The clustered eTable's 191/198 and 150/182 sum to its N=380 (SUP-S006), while its all-patient headings are N=381 and N=376 (SUP-S008). The differing denominators are explicitly outcome/subgroup-specific and are not a discrepancy by themselves.

4. **Interim arithmetic.** DOC003#page=6 denominators 257+250=507 and displayed percentages round to 97% and 85% (SUP-S010). No arithmetic signal identified in the supplied supplement.

## Mapping limitations

- The fresh `source_coverage.md` and evidence-asset inventory were not yet present at the time this mapper read the assigned scope; all source locations above are direct PDF page locations and fresh OCR/PNG paths.
- OCR was visually checked for the material table and Kaplan-Meier figure. The protocol and form text were legible in fresh OCR; no source was modified and no legacy audit derivative or external source was used.
