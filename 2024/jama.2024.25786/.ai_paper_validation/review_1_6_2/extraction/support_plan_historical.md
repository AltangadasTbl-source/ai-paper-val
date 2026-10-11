# Historical and early final protocol support mapping

Status: COMPLETE. Runtime task ID: /root/plan_mapper_historical. Model/effort: gpt-6.1-sol/medium. Exact disjoint scope: DOC-002, `joi240147supp1_prod_1738701765.28701.pdf`, PDF pp. 1-61 only. Document role: PLAN throughout. This includes the cover, complete original protocol v1.4 dated 30 September 2021 (pp. 2-35), and final protocol v1.8 dated 21 November 2022 pp. 36-61. Pages 62-103 are assigned elsewhere and were not used here. All 61 assigned pages were opened and mapped; 60 reusable-backed pages and one fresh-required page, p. 33. No scientific diagnosis, findings, or candidate IDs are assigned. Mapper-local PLAN001-PLAN025 are relationship groups, not globally assigned N/S IDs.

Controls read: QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md and settings.toml, current source_inventory.md, evidence_asset_inventory.md, source_coverage.md, coverage_manifest.md, tooling_record.md. Reused asset: `.ai_paper_validation/preprocessed/DOC-002.txt`, page-marked native text, pypdf historical version unrecorded, SHA-256 055d963cff21a70ab3d659cff668bab699b371ac0968d702f1ef5aecd92f2cc9. Every assigned page's full reusable text was read; no old scientific conclusion was used. The source remains final authority. The native text was read in bounded page groups using awk and exact SOURCE PAGE markers.

Evidence links below are relative to this artifact. Every source page uses `../../../joi240147supp1_prod_1738701765.28701.pdf#page=N`. Matching main-paper keys identify concepts to join to the separately assigned main-paper map; they are not claims that a comparison has been checked.

## Fresh extraction provenance and p. 33 visual map

Compute device CPU. Direct Poppler 26.01.0 commands:

- `pdftotext -f 33 -l 33 joi240147supp1_prod_1738701765.28701.pdf .ai_paper_validation/review_1_6_2/preprocessing/plan-historical/native-p033.txt`
- `pdftotext -layout -f 33 -l 33 joi240147supp1_prod_1738701765.28701.pdf .ai_paper_validation/review_1_6_2/preprocessing/plan-historical/layout-p033.txt`
- `pdftoppm -f 33 -l 33 -singlefile -r 120 -png joi240147supp1_prod_1738701765.28701.pdf .ai_paper_validation/review_1_6_2/preprocessing/plan-historical/page-p033`

All succeeded. Outputs: native-p033.txt, layout-p033.txt, page-p033.png in the unique preprocessing directory above. Native/layout contain captions, not figure content. The complete render was visually inspected; all required labels are readable. OCR was not needed. No fallback, GPU, Office conversion, workbook formulas or cached/displayed workbook values apply to this PDF-only scope.

[Page 33](../../../joi240147supp1_prod_1738701765.28701.pdf#page=33), Figure 1, Participant timeline: trauma precedes ENROLMENT PROCESS; T0 (hour 0), “Intervention is initiated”; INTERVENTION ends at T8, “Intervention is completed”; FOLLOW-UP has 30 days, “Mortality”, “Pneumonia and ARDS”; 6 months, “EQ-5D-5L”, “GOSE”; 12 months, “Mortality”, “EQ-5D-5L”, “GOSE”. Figure 2, Timeline of study progress: WRITING THE PROTOCOL, APPROVALS RECEIVED, INCLUSION, DATA MANAGEMENT, MANUSCRIPT DRAFT READY. Spring 2021: applications on approvals are handed in; Fall 2021: first inclusion of a patient; Spring 2023: “1420 patients with a 30-day follow-up are included”; Fall 2023: manuscript drafting; Winter 2024: submission of primary paper. Figure 1 maps intervention/outcome windows; Figure 2 supplies prospective recruitment/analysis timing and 1420 follow-up target, not trial results.

## Relationship groups

### PLAN001 — Version, design and direction

Locations: pp. 1,2,5,11-12,16,18,36,39,47-48,52,54. Cover identifies original v1.4, final v1.8, change summary p.78, SAP v1.0 dated 11 January 2023 p.80. Original registration number EudraCT 2021-000556-19; final adds NCT05146700 and H-21018062. Both versions specify international, multicentre, parallel-group, superiority randomized controlled trial, outcome assessor- and analyst-blinded, treating staff/recruiting team aware of allocation. Objective/hypothesis is restrictive versus liberal oxygen in the first eight hours following trauma, hypothesized lower rate of 30-day mortality and/or major respiratory complications within 30 days. No noninferiority/equivalence margin appears in this scope. Key: trial design, comparison direction, intervention duration, primary composite.

### PLAN002 — Eligibility, item by item

Locations: original pp.12,16; final [p.48](../../../joi240147supp1_prod_1738701765.28701.pdf#page=48) synopsis and [p.52](../../../joi240147supp1_prod_1738701765.28701.pdf#page=52) sections 3.2-3.3. Exact final section list:

1. “Patients aged ≥18 years, including fertile women*”
2. “Blunt or penetrating trauma mechanism”
3. “Direct transfer from the scene of accident to one of the participating trauma centres”
4. “Trauma team activation”
5. “The enrolling physician must initially expect a hospital length of stay for 24 hours or longer”

Footnote: no added risk for enrolment of fertile women, oxygen administration approved for this group. Exclusion list:

1. “Patients in cardiac arrest before or on admission”
2. “Patients with a suspicion of carbon monoxide intoxication”
3. “Patients with no/minor injuries after secondary survey will be excluded if they are expected to be discharged <24 hours”

Original has these same criteria. These define recruited population separately from original analysis-specific ISS=0 exclusion in PLAN015. Keys: age, trauma mechanisms, direct admission, activation, expected stay, exclusion/modified intention-to-treat population. No inferred additional exclusion is added.

### PLAN003 — Randomization, unit, stratification, allocation concealment

Locations: original pp.17-18; final [p.53](../../../joi240147supp1_prod_1738701765.28701.pdf#page=53)-54. Individual trial participants randomized 1:1, variable block sizes, stratified by centre (prehospital base or trauma centre) and tracheal intubation at inclusion. Independent biostatistician generates randomization table outside REDCap; allocation sequence and block sizes known only by statistician, concealed from investigators. Concealed envelopes held prehospital/in-hospital, containing allocation, matching study ID and instructions/data sheet. Prehospital inclusion optional; physician obtains proxy consent following local rules before opening envelope. Trauma-bay final wording allows including physician such as trauma leader or attending anaesthesiologist; original specifies trauma team leader. Key: randomization strata and primary adjustment for centre/intubation.

### PLAN004 — Initiation, exposure clock and continuation

Locations: original pp.12,17,20,22; final pp.48,53,56,58-59. Treatment initiated at enrolment, T0, continues eight hours; trauma-bay initiation “must not be delayed more than 90 minutes after hospital arrival”. Restrictive labelled intervention and liberal control. Prehospital or trauma-bay initiation depends on centre. Intubation during intervention changes delivery mode but continues same randomized arm. Pre-oxygenation as usual prior to intubation. PEEP at physician discretion. Key: time from trauma/randomization, eight-hour exposure, intubation transitions.

### PLAN005 — Restrictive oxygen specification

Locations: original pp.12,20-22; final [p.56](../../../joi240147supp1_prod_1738701765.28701.pdf#page=56), scheme pp.57-58. Exact final prose: “The restrictive group will receive the lowest dosage of oxygen (≥21%) ensuring an arterial oxyhemoglobin saturation (SpO2) target = 94% either using no supplemental oxygen, a nasal cannula, a non-rebreather mask (non-intubated trial participants) or manual/mechanical ventilation (intubated trial participants). Pre-oxygenation should be done as usual prior to intubation. Only trial participants receiving an FiO2 = 0.21 can saturate >94%.” Scheme nonintubated: if saturation <94%, lowest O2 flow between 0-15 L/min ensuring saturation=94%; only no-supplemental-oxygen participants may saturate >94%. Scheme intubated prehospital/trauma bay permits FiO2=0.21 “(or lowest possible)” for saturation >94%; transport/OR/ICU/PACU/ward specify 0.21. Key: arm definition, SpO2 target and permitted exceptions; flow L/min versus dimensionless FiO2 fraction.

### PLAN006 — Liberal oxygen specification

Locations: original pp.12,20-22; final p.48 and [p.56](../../../joi240147supp1_prod_1738701765.28701.pdf#page=56), scheme pp.57-58. Nonintubated: 15 L O2/min via non-rebreather mask prehospital, trauma bay, intrahospital transportation; OR/ICU/PACU/ward may reduce to ≥12 L O2/min if arterial oxygen saturation ≥98%. Intubated: FiO2=1.0 prehospital, trauma bay, transportation; OR/ICU/PACU/ward may reduce to FiO2≥0.6 if arterial oxygen saturation≥98%. Scheme OR nonintubated column describes preoxygenation/intubation then ventilation at FiO2≥0.6 subject to saturation≥98%; ICU/PACU/ward nonintubated mask flow≥12 L/min under same saturation criterion. Key: randomized dose, reduction rule, delivered oxygen summaries.

### PLAN007 — Oxygen and ABG observation windows

Locations: original pp.22-24; final pp.58-61. Two arterial blood gases during intervention: first hour 1±30 minutes after randomization (T1; intervention initiation hour0), obtain as soon as possible if inaccessible at T1; second hour6±2 hours (T6). If extra ABGs obtained, choose closest to specified T1/T6 slots for data entry. Nonventilated caregivers track dosage/saturation every hour; ventilated data automatically tracked through ventilator/electronic record and also noted on collection sheet. Every participant has hourly dosage/saturation paper records. Key: intervention hourly data, oxygen dose and blood gas time points.

### PLAN008 — Primary outcome and ascertainment

Locations: original pp.11,13,16,18,23; final pp.47,49,52,54,[59](../../../joi240147supp1_prod_1738701765.28701.pdf#page=59). Exact final section3.6.1: “The primary outcome will be the incidence of 30-day mortality and/or major respiratory complications (pneumonia and ARDS) within 30 days (combined endpoint).” Primary status retained in all listed locations. At least two allocation-blinded specialists in anaesthesia, intensive care, emergency medicine or similar at each centre assess in-hospital lung complications, with allocation information concealed. Key: composite event, all-cause mortality component, pneumonia, ARDS, 30-day window, assessors.

### PLAN009 — Complete secondary outcome list and hierarchy

Locations: original synopsis p.13 and section3.6.2 p.23; final synopsis [p.49](../../../joi240147supp1_prod_1738701765.28701.pdf#page=49), exact final sections [p.59](../../../joi240147supp1_prod_1738701765.28701.pdf#page=59)-60:

1. “Mortality at 30 days and 12 months after trauma”
2. “Major respiratory complications (pneumonia and ARDS) within 30 days”
3. “HOS LOS, ICU LOS and days alive outside the ICU”
4. “Time on mechanical ventilation (until 30 days), days alive without mechanical ventilation and number of re-intubations within 30 days”
5. “Pneumonia post-discharge within 30 days”
6. “Episodes of hypoxaemia during intervention (saturation <90%)”
7. “Surgical site infections within 30 days”
8. “EQ-5D-5L score at 6 and 12 months post-trauma”
9. “GOSE score at 6 months and 12 months post-trauma”

Final synopsis uses “Hospital length of stay (HOS LOS), Intensive Care Unit length of stay (ICU LOS)” and repeats 6 months and12 months for EQ-5D-5L. All nine are designated secondary here; no key/exploratory split is specified on these pages. Do not infer status from subsequent SAP outside this shard. Keys: secondary outcome hierarchy/components, mortality, respiratory complications, HOS/ICU LOS, alive outside ICU, ventilation duration/free days/reintubation, postdischarge pneumonia, hypoxaemia, surgical infection, long-term quality-of-life/functional outcomes.

### PLAN010 — Operational outcome definitions and subgroup scale

Locations: original p.25; final [p.61](../../../joi240147supp1_prod_1738701765.28701.pdf#page=61), section3.7.3: “Pneumonia will be defined as per the CDC criteria.” Reference21. “ARDS will be defined as per the Berlin definition.” Reference22. “Traumatic brain injury will be defined as”: “Severe: AIS ≥5”; “Moderate: AIS 3–4”; “Mild: AIS 1–2”. Same original definitions. CDC and Berlin reference names supplied on p.35; full external criteria are not reproduced in these assigned pages and were not obtained externally. Keys: pneumonia/ARDS definition, AIS-based moderate/severe TBI subgroup; do not substitute GCS severity.

### PLAN011 — Data sources and additional recorded variables

Locations: original p.24; final p.60. Medical-record data: age/sex/height/weight; prehospital vital signs, trauma mechanism, prior oxygen indication, SpO2, supplemental oxygen yes/no, intubation yes/no, flow/FiO2; ISS and full injuries; transportation mode; date/time trauma, scene arrival/departure, trauma bay, ICU/ward, intubation/extubation/reintubation, surgery/duration; hospital/ICU LOS; arrival vital signs/ABG if available; pneumonia, ARDS, surgical infection, sepsis; myocardial infarction/cerebral ischaemia; AE/SAE; prior heart/lung/other disease; active smoking; brain-injury specifics and other cerebral complications; death date. These variables are not all designated secondary outcomes by section3.6.2. Mortality status through registries if possible/local practice. EQ-5D-5L/GOSE by telephone participant/next-of-kin/caregiver. Postdischarge pneumonia via prescribed medicines in countries where available. Keys: outcome collection/analysis covariates; distinction between data collection and outcome status.

### PLAN012 — Consent, withdrawal and follow-up availability

Locations: original pp.18-20,23; final pp.54-56,59. Emergency temporarily incompetent participants; Denmark first proxy before inclusion, second after; local rules elsewhere. Next-of-kin then participant consent sought when possible. Each offered 24-hour decision time; inclusion continues pending decision. If participant unable to consent within30 days, next-of-kin accepted as final. If still unable and next-of-kin unidentifiable/uncontactable, no further consent attempts at day30; guardian proxy sustains follow-up day30,6months,12months. Participant/next-of-kin may withdraw any time/any reason; investigator may withdraw any time; reason stored eCRF. No numerical withdrawal count here. Key: consent exclusions/flow, follow-up and attrition.

### PLAN013 — Clinical departures and brain oxygen monitoring

Locations: original p.24; final p.60. Optional continuous intraparenchymal brain oxygen monitoring under local practice for TBI in neurosurgical ICU; placement/early-hour reliability discussed. Any participant may have protocol deviation if clinically justified by treating physician, documented including justification in REDCap. Original p.29: if saturation unmeasurable e.g. hypovolaemia/hypothermia, physician chooses/documents treatment; resume allocation when measurable. Key: protocol departures and per-protocol exclusion, intervention measurements.

### PLAN014 — Sample size assumptions and accrual target

Locations: original [p.25](../../../joi240147supp1_prod_1738701765.28701.pdf#page=25)-26, synopsis p.13; final synopsis p.49; p.33 Figure2. Original assumptions: TRAUMOX1 composite20% restrictive,33% liberal; literature mortality6-12%, post-trauma VAP almost30%. “With 710 trial participants in each arm, we will be able to detect a 33% risk reduction with a restrictive supplemental oxygen strategy (with 80% power at the 5% significance level) if the incidence of our primary outcome is 15% in the liberal group.” No printed sample-size equation, sidedness or further computation method in this scope. Enrolment stops at1420 evaluable with30-day follow-up; maximum1600 as enrolment continues while evaluating follow-up. Both synopses explicitly710 each arm, total1420 with30-day follow-up. Figure2 states1420 with30-day follow-up. Key: sample-size/power assumptions and stopping accrual; no recalculated sample size assigned here.

### PLAN015 — Original analysis population and per-protocol set

Locations: original pp.25-26. Exact statements: “Our primary analysis will be a modified intention-to-treat analysis, but a per-protocol analysis will also be carried out.” “In the primary analysis, we will exclude trial participants where no injuries are found defined as ISS = 0.” Per-protocol: all participants with≥1 major protocol violation removed; definitions in PLAN020. Detailed SAP including prespecified subgroups to be made. No analysis population specification is present within the assigned final-protocol pp.36-61 beyond recruitment/withdrawal criteria; final statistical section begins p.62 assigned elsewhere. Key: modified ITT ISS=0 exclusion and PP exclusion rules.

### PLAN016 — Original primary model, measure, interval, adjustments

Location: original [p.26](../../../joi240147supp1_prod_1738701765.28701.pdf#page=26). Exact: “The primary composite outcome will be compared between the two groups using logistic regression reported as Odds Ratio (OR) with 95% CI.” “The primary analysis will be adjusted for age, sex, centre, intubated at randomisation (yes/no), and known pneumonia on admission (under treatment).” “We will use a 5% significance level. Any changes or additional analyses will be reported.” Statistician performs analysis. No explicit coding/reference category, interaction, robust variance or model formula here. Key: primary adjusted OR,95%CI, age/sex/centre/intubation/pneumonia adjustment, significance. Main map must establish actual reported model independently.

### PLAN017 — Original secondary analyses and multiplicity scope

Location: original p.26. “Secondary outcomes will also be compared between the two groups using Fisher’s exact test/Chi2 test for categorical data and competing risk survival analyses for continuous data.” Significance5%. No secondary multiplicity adjustment or hierarchical testing rule is stated within the assigned original protocol, and final statistical section is beyond scope. This records text presence only, without judging later specification. Key: secondary tests, continuous outcomes/competing risks, multiplicity.

### PLAN018 — Original missing data and sensitivity rule

Location: original p.26. Exact: “If less than 5% of data required for any specific analysis on primary or secondary outcomes are missing, a complete case analysis will be performed. If more than 5% are missing, and it is concluded that data are not ‘missing completely at random’ (MCAR criterion), inverse probability weighting will be used to correct this bias. A sensitivity analysis on the assumptions used for missing data will be done to verify robustness.” Source does not explicitly assign the exactly5% case or >5% MCAR case in this paragraph. Reference25 p.35: Mallinckrodt/Lin/Molenberghs, structured sensitivity framework, Pharmaceutical Statistics2013;12:1-6. Key: primary/secondary completeness threshold, MCAR, IPW, missing-data sensitivity.

### PLAN019 — Original complete prespecified subgroup/sensitivity list

Location: original p.26. Exact: “Pre-specified subgroup analyses will be made on trial participants initially intubated (within one hour of the accident) (yes/no), trial participants with ICU admission (yes/no), trial participants with moderate and severe traumatic brain injuries (yes/no), trial participants with chronic obstructive pulmonary disease (yes/no), episodes with hypoxaemia as well as an analysis on trial participants enrolled prehospital versus in-hospital. An analysis adjusted for Injury Severity Score will also be conducted.” Items: initially intubated≤1hour after accident; ICU admission; moderate/severe TBI (AIS definitions PLAN010); COPD; episodes with hypoxaemia; prehospital versus hospital inclusion; additional ISS-adjusted analysis. Separate PP PLAN015 and missing-data sensitivity PLAN018. No interaction estimator/test specified in this paragraph. Key: all listed subgroup analyses and ISS sensitivity; distinguish initial-intubation subgroup from intubation-at-randomization covariate.

### PLAN020 — Original major protocol violations

Location: original p.26 section3.8.1, exclusions affect PP. Restrictive arm during intervention: supplemental oxygen AND arterial oxygen saturation≥98% recorded on data sheet; OR recorded PaO2≥14kPa. Liberal arm during intervention: no supplemental oxygen at any recorded time; OR recorded saturation≤94% when oxygen<15 L O2/min via non-rebreather mask if nonintubated, or FiO2<1.0 if intubated. Source bullets preserved as separate printed criteria; no unprinted consecutive-time-point requirement added. Key: PP population/exposure departures, PaO2 threshold. Final violation specification p.62 is assigned elsewhere.

### PLAN021 — Original interim, monitoring and stopping decisions

Location: original [p.30](../../../joi240147supp1_prod_1738701765.28701.pdf#page=30)-31. Independent DMSC includes statistician; meets at complete30-day follow-up of355 (approximately25% sample-size estimation) and710 (approximately50%). Biostatistician performs interim analysis before meeting on blinded sponsor/investigator data. “Criteria for premature termination will be decided by steering committee.” Sponsor reports overall SAE number yearly. Statistician still awaited p.9 and31; final membership p.45 names Brice Ozenne, biostatistician. No numeric interim stopping boundary supplied within original scope. Key: interim timing, stopping rule, blinded analysis; final charter pp.68-73 assigned elsewhere.

### PLAN022 — Original safety endpoints, timing and limits

Locations: pp.13,27-28. AE: any untoward occurrence with medicinal product, not necessarily causal. Record only atelectasis and airway mucosal irritability as AE; all SAE registered. SAE includes inpatient/prolonged hospitalization, persistent/significant disability/incapacity, congenital anomaly, life-threatening event/death. SUSAR serious suspected reaction inconsistent with reference safety information. Correlation labels1unrelated,2possibly related,3probably related,4related. Assess record once first24hours, then every third day until discharge, maximum30days. SAE automatic sponsor/coordinator notification within24hours; potential SUSAR within24hours; fatal/life-threatening report≤7days, follow-up≤8more days(total15); others≤15days; annual SUSAR report. Reporting end after last visit of1420 with complete30day,6/12month follow-up, authorities≤90days, EudraCT results≤1year after termination. These are planned monitoring/reporting quantities, not observed safety counts. Key: AE/SAE ascertainment and safety-status distinction.

### PLAN023 — Original and final participant timeline

Locations: original p.23 pointer and freshly inspected [p.33](../../../joi240147supp1_prod_1738701765.28701.pdf#page=33); final p.59 pointer to figure1 whose actual page75 is outside this scope. Figure1 transcription above records T0/T8,30day,6month,12month endpoints completely. It independently places mortality/pneumonia/ARDS at30days and mortality at12months; EQ-5D-5L/GOSE at6/12months. Key: outcome windows and follow-up.

### PLAN024 — Administrative scope opened, applicability explicitly assessed

Locations: original pp.5-9,14,27-32; final pp.39-45,50. Contacts, site lists, drug handling/accounting, funding, archiving and ethics were opened. No report outcome counts on those pages. Original centre requirement p.16: definitive care, registry, approximately400trauma/year, all EU; final p.52 changes geographic wording to continental Europe. Contact lists add sites/staff; these are administrative locations, not randomized/analyzed totals. Original p.31:10year document retention; funding4years,6,326,084DKK, centre150euro/completely documented participant after30days, additional350,000DKK personal grant. Original p.30 publication authorship additional author/100complete participants. Original p.32 changes only steering committee; p.29 substantial changes require regulatory prior review except immediate hazard, then report promptly. Original progress plan p.30 and figure2: approvals spring2021, first inclusion autumn2021, completed enrolment spring2023, analysis/drafting autumn2023, submission beginning2024. No applicable primary/key-secondary quantitative result from contact/funding/drug-accounting units; these numbers are preserved as context only. Key: disclosed plan versions and amendments; administrative calendar not a result comparison.

### PLAN025 — Background assumptions and supplied references

Locations: original p.15,29,34-35; final p.51. Background data have no TRAUMOX2 result status: mechanically ventilated hyperoxaemia16-50%; recommendation FiO2 80% intraoperatively and2-6hours afterward; cohorts152,000 and14,000; PaO2 around18kPa; prior ICU trial2928participants,8vs12kPa,max90days; TRAUMOX1 N41,24hour intervention, randomization median[IQR]7[4-10]min and trauma-to-bay51[29.0-67.5]min, motivates8hours/current early inclusion. Original p.29 pilot desaturation seven episodes<90%, median87%[87-89]; five/seven<89% in two participants (one postextubation, another cardiac arrest). No historical result is substituted for this trial. Supplied p.35 references relevant to interpretation:18TRAUMOX1 pilot,19SPIRIT2013,20REDCap,21CDC pneumonia2021,22Berlin ARDS2012,23TBI definition2016,24trauma fatality2004,25missing-data framework2013,26EU regulation536/2014,27critical-care SAE2008,28Helsinki2013,29GCP E6(R2)2016. Page34 references1-15 are background only. No referenced external source accessed. Key: sample-size assumptions, intervention rationale and named definitions.

## Explicit page coverage

All rows COMPLETE. “No applicable” records mean the entire page was inspected and contains no result-relevant relationship beyond the stated identity/navigation/administrative context; they do not mean the unit was skipped.

| PDF page | Coverage content | Relationship groups / applicability |
|---|---|---|
| 1 | Bundle cover/version map | PLAN001 |
| 2 | Original protocol cover | PLAN001 |
| 3 | Original contents | No applicable result; navigation opened |
| 4 | Original contents continued | No applicable result; navigation opened |
| 5 | Original general information | PLAN001,PLAN024; contacts no applicable result |
| 6 | Original investigators | PLAN024; no applicable result |
| 7 | Original investigators/sites | PLAN024; no applicable result |
| 8 | Original sites/DMSC | PLAN024; no applicable result |
| 9 | Original DMSC/registration | PLAN021,PLAN024 |
| 10 | Abbreviations | FiO2 fraction; AIS/ISS/GCS/ARDS/GOSE/LOS definitions mapped |
| 11 | Original synopsis design/objective | PLAN001,PLAN008 |
| 12 | Original synopsis eligibility/doses | PLAN002,PLAN004-PLAN006 |
| 13 | Original outcomes/accrual/safety | PLAN008,PLAN009,PLAN014,PLAN022 |
| 14 | Original coordinating contact | PLAN024; no applicable result |
| 15 | Original rationale | PLAN025 |
| 16 | Original objective/design/eligibility | PLAN001,PLAN002,PLAN024 |
| 17 | Original recruitment/randomization | PLAN003,PLAN004 |
| 18 | Original concealment/assessors/consent | PLAN003,PLAN008,PLAN012 |
| 19 | Original consent follow-up | PLAN012; legal text assessed, no separate quantitative result |
| 20 | Original consent/doses/scheme start | PLAN004-PLAN006,PLAN012 |
| 21 | Original oxygen scheme | PLAN004-PLAN006 |
| 22 | Original scheme/ABG windows/footnote | PLAN004-PLAN007 |
| 23 | Original tracking/withdrawal/outcomes | PLAN007-PLAN009,PLAN012,PLAN023 |
| 24 | Original recorded variables/departures/ABGs | PLAN007,PLAN011,PLAN013 |
| 25 | Original biobank/data/definitions/power | PLAN010,PLAN014,PLAN015; biobank no applicable result |
| 26 | Original analyses/missingness/subgroups/violations | PLAN015-PLAN020 |
| 27 | Original drug accounting/safety definitions | PLAN022,PLAN024 |
| 28 | Original safety/event/end reporting | PLAN022 |
| 29 | Original ethics/departures/pilot data | PLAN013,PLAN024,PLAN025 |
| 30 | Original progress/publication/interim | PLAN021,PLAN024 |
| 31 | Original DMSC/archiving/funding | PLAN021,PLAN024 |
| 32 | Original changes | PLAN024 |
| 33 | Fresh full-page figure inspection, figures1/2 | PLAN014,PLAN023,PLAN024 |
| 34 | Original references1-15 | PLAN025; no independent trial result |
| 35 | Original references16-29 | PLAN025; named definitions/assumptions |
| 36 | Final protocol cover | PLAN001 |
| 37 | Final contents | No applicable result; navigation opened |
| 38 | Final contents continued | No applicable result; navigation opened |
| 39 | Final general information | PLAN001,PLAN024; contacts no applicable result |
| 40 | Final investigators | PLAN024; no applicable result |
| 41 | Final investigators | PLAN024; no applicable result |
| 42 | Final investigators | PLAN024; no applicable result |
| 43 | Final investigators/sites | PLAN024; no applicable result |
| 44 | Final sites/DMSC | PLAN024; no applicable result |
| 45 | Final statistician/registration | PLAN001,PLAN021,PLAN024 |
| 46 | Final abbreviations | Same quantitative terminology as p.10 |
| 47 | Final synopsis design/objective | PLAN001,PLAN008 |
| 48 | Final synopsis eligibility/doses | PLAN002,PLAN004-PLAN006 |
| 49 | Final synopsis outcomes/accrual/safety | PLAN008,PLAN009,PLAN014,PLAN022 |
| 50 | Final coordinating contact | PLAN024; no applicable result |
| 51 | Final rationale | PLAN025 |
| 52 | Final objectives/design/eligibility | PLAN001,PLAN002,PLAN024 |
| 53 | Final recruitment/randomization | PLAN003,PLAN004 |
| 54 | Final concealment/assessors/consent | PLAN003,PLAN008,PLAN012 |
| 55 | Final consent/follow-up | PLAN012; legal text assessed, no separate quantitative result |
| 56 | Final consent/intervention/doses | PLAN004-PLAN006,PLAN012 |
| 57 | Final scheme, prehospital/bay/transport | PLAN004-PLAN006 |
| 58 | Final scheme, transport/OR/ICU/ABG start | PLAN004-PLAN007 |
| 59 | Final ABGs/withdrawal/outcomes | PLAN007-PLAN009,PLAN012,PLAN023 |
| 60 | Final outcomes/data/departures | PLAN009,PLAN011,PLAN013 |
| 61 | Final ABG/data/biobank/definitions | PLAN007,PLAN010; biobank no applicable result |

## Handoff and limits

Counts: 61/61 pages mapped; 60 reusable-backed plus1fresh-required;25 relationship groups;2freshly inspected figures;0Office sources,0workbook formula/cached-value pairs. Original statistical specifications fully covered pp.25-26 and interim p.30. Final statistical specifications begin p.62 and are deliberately delegated, as are final timeline p.75, changes pp.78-79 and SAP pp.80-103. No scientific coverage gap within assigned scope. Source-based limitations: original missing-data paragraph does not explicitly state exactly5% or >5%MCAR branch; no original sample-size formula/sidedness, model coding, numeric interim stopping boundary or subgroup interaction estimator is printed in this scope. These are extraction facts, not diagnoses. Historical native engine version unrecorded; p.33 figure gap closed by direct CPU render. All sources and reused assets preserved.
