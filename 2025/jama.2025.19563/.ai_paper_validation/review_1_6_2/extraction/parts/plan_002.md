# Support quantitative mapping — plan shard 002

Scope: DOC-002, `joi250084supp1_prod_1765403089.61351.pdf`, exact PDF pages 31–60. Document role: PLAN by content (prospective trial protocol and its questionnaire appendices). All 30 assigned pages were opened visually. This extraction records specifications without candidate diagnosis or adjudication. Local relationship keys below are shard keys for coordinator integration into the complete N/S inventory.

## Evidence and tooling

Source-authoritative locators are PDF page and printed section/line numbers. Reused image family: `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/p031-p060/page-NN.png`, for pp. 31–44, 46–53, 55–60. Historical render engine unknown as recorded by curator. Native/layout glyph extraction was not used scientifically. Reused pp. 45 and 54 returned an unsupported-image decoder response; neither failure was treated as page content. Each was freshly rendered from the supplied source and visually inspected using `/home/juliz/venvs/stt/bin/python workflow_1_6_2/scripts/pdf_tools.py render joi250084supp1_prod_1765403089.61351.pdf --page N OUTPUT`. Engine: PyMuPDF 1.28.0, CPU, 200 dpi. Outputs: `.ai_paper_validation/review_1_6_2/preprocessing/plan002-page045.png` and `.ai_paper_validation/review_1_6_2/preprocessing/plan002-page054.png`. No OCR was needed for this shard; all printed content was legible visually. No other Python extraction or image-editing helper was used. No source/reused asset was changed.

## Page-by-page closure

| PDF page | Inspected content | Mapping disposition | Exact relationship keys |
|---|---|---|---|
| 31 | §§6.6–7.4 rescue, withdrawal, lost follow-up, completion; §8 home visits | COMPLETE; endpoint-related population/time definitions mapped | P2-N01, P2-S01 |
| 32 | §8.1 planned CONSORT diagram; §8.2 physical examination | COMPLETE; planned counts and measurement units mapped | P2-N02, P2-N03 |
| 33 | §8.2 lab, activity, questionnaires, attendance; §8.3 safety | COMPLETE; outcome measurement/validity and timing mapped | P2-N04, P2-N05, P2-N06, P2-S02 |
| 34 | §§8.4.1–8.4.3 AE/SAE definitions, severity, causality | COMPLETE; safety outcome definitions mapped | P2-N07 |
| 35 | §§8.4.3–8.4.5 AE expectedness, windows, reporting/stopping | COMPLETE; safety windows and trigger mapped | P2-N08, P2-S03 |
| 36 | §§8.4.6–8.5 safety reporting, pregnancy; §9.1 hypotheses | COMPLETE; safety population and NI assumptions mapped | P2-N09, P2-S04 |
| 37 | §§9.1–9.4.1 hypotheses, NI rationale, sample size, populations, models | COMPLETE; all statistical specifications mapped | P2-S04, P2-S05, P2-S06, P2-S07, P2-S08 |
| 38 | §§9.4.2–9.4.8 missingness, site, adjustment, within-arm, primary/secondary models | COMPLETE; all analysis and outcome specifications mapped | P2-S09, P2-S10, P2-S11, P2-S12, P2-S13, P2-S14 |
| 39 | §9.4.8 continuation; §9.4.9 cost-effectiveness; §9.4.10 heading | COMPLETE; questionnaire tests, missingness and economic plans mapped | P2-S09, P2-S14, P2-S15 |
| 40 | §§9.4.10–12 safety, interim, summaries; §10 ethics/consent/closure | COMPLETE; analysis population and interim rule mapped | P2-S16, P2-S17 |
| 41 | §10.1.4 closure continuation, privacy/storage/governance | COMPLETE; qualitative stopping circumstances mapped; remaining administrative material has no applicable quantitative result element | P2-S17 |
| 42 | governance chart, §10.1.8 DSMB; monitoring | COMPLETE; site identifiers and monitoring timing recorded; no additional statistical decision rule | P2-N10 |
| 43 | monitoring, lab QC, data-management/security | COMPLETE; collection systems and units mapped; security/roles no applicable result relationship | P2-N11 |
| 44 | retention, deviations, publication/data sharing, conflicts | COMPLETE; no applicable result-relevant quantitative analysis or endpoint specification | None |
| 45 | §10.2 abbreviations | COMPLETE via fresh direct render; terminology keys mapped | P2-N12 |
| 46 | abbreviations continuation | COMPLETE; no additional applicable quantitative result relationship | None |
| 47 | §11.1 PAR-Q, seven items and clearance rule | COMPLETE; eligibility decision rule mapped | P2-N13 |
| 48 | §11.2 physician clearance template | COMPLETE; intervention targets/duration mapped | P2-N14 |
| 49 | §11.3 demographics form beginning | COMPLETE; baseline variables/categories mapped | P2-N15 |
| 50 | demographics education continuation | COMPLETE; education categories mapped | P2-N15 |
| 51 | §11.4 medical history/medication form | COMPLETE; possible covariate definitions mapped | P2-N16 |
| 52 | §11.5 stage of exercise change, four-item coding | COMPLETE; scale and full classification rule mapped | P2-N17 |
| 53 | §11.6 self-reported activity | COMPLETE; recall interval/unit mapped | P2-N18 |
| 54 | §11.7 dietary assessment, eight-item score | COMPLETE via fresh direct render; all cutoffs and score mapped | P2-N19 |
| 55 | §11.8 apps/devices, seven yes/no items | COMPLETE; descriptive predictor variables mapped | P2-N20 |
| 56 | §11.9 adapted NPART description and first items | COMPLETE; planned predictor use and coding mapped | P2-N21, P2-S18 |
| 57 | NPART social, memory, health and life-quality items | COMPLETE; ordered response scales/recall windows mapped | P2-N21 |
| 58 | NPART footnote and technology tables | COMPLETE; item count/coding mapped | P2-N21 |
| 59 | blank except line/page identifiers | COMPLETE; no applicable quantitative content | None |
| 60 | §11.10 acceptability questionnaire items 1–18 | COMPLETE; response scale and reverse-coded items mapped | P2-N22 |

Coverage count: 30/30 mapped; 28 reusable-image pages and 2 fresh-render pages used. Pages with no independent applicable quantitative element: 44, 46, 59. No scientific coverage gap. No workbook formulas, cached workbook values, CSV data, or Office documents occur in this assigned PDF-only scope.

## Numeric definitions, measurements, and planned operational quantities

### P2-N01 — rescue, participant retention and completion

Location: PDF p.31 §§6.6,7.1–7.4, lines930–966. A1C ≥6.5% during the trial triggers physician notification for possible type2 diabetes evaluation; glucose-lowering medication is clinician discretion. Nonengagement in either dDPP or hDPP does not remove efficacy/adverse-event follow-up. Incident diabetes participants remain eligible to continue; new glycemic-control medications are recorded. Participants who signed consent, were randomized, received intervention, and subsequently withdraw or discontinue are stated to be replaced. Lost follow-up is failure to return for the 12-month visit combined with inability to contact; missed visit rescheduling sought within30days and, where possible,3telephone contacts before final lost-follow-up designation. Completer/off-study requires completed12-month study visit; hDPP additionally requires12months elapsed from first hDPP visit, except never-attenders for whom that requirement does not apply. Matching main-paper keys: flow/ITT denominator; incident diabetes/antihyperglycemic exposure; study-completion and program-completion distinct constructs.

### P2-N02 — planned CONSORT counts

Location: PDF p.32 §8.1 diagram. Assess eligibility approximately460; randomize368; allocate184 dDPP and184 hDPP. Excluded, intervention received/not received, lost follow-up, discontinuation, analyzed, and analysis-exclusion counts are blank prospective fields, not reported observations. Planned total identity:184+184=368. Matching main key: randomized sample/allocation and planned versus achieved recruitment.

### P2-N03 — physical examination units

Location: PDF p.32 §8.2 lines984–986. Height nearest0.1cm by portable stadiometer; weight nearest0.1kg by portable digital scale; same scale used for all participants for each measurement; light clothing/no shoes/void before weighing. Match: body-weight outcome units and ascertainment.

### P2-N04 — A1C ascertainment

Location: PDF p.33 lines987–993. A1CNow+ fingerstick measurement, result in5minutes, performed by research coordinator; repeat with second sample after device message. Two quality-control messages during a visit define device failure, excluding displayed readings <4.0 or >13.0 from that failure count; device failure requires central-laboratory serum hemoglobin A1C for that visit. Match: A1C outcome and measurement substitution.

### P2-N05 — device activity and validity

Location: PDF p.33 lines994–1006. ActiGraph GTX9X-BT Link wrist monitor;7consecutive days at enrollment and approximately every1month throughout trial; device returned at12-month visit. Reminders3days before and on scheduled day. Participants blinded to device data; CentrePoint synchronization/remote compliance monitoring. If actual wear comprises <75% of the7-day period, repeat7consecutive days as soon as noted and disregard prior incomplete/invalid data. This validity definition is separate from analysis missingness rules. Match: objective PA units, outcome derivation, valid-record selection.

### P2-N06 — self-report, questionnaires and attendance data

Location: PDF p.33 lines1007–1032. Preceding-week moderate/brisk activity minutes via survey in week before ActiGraph; no activity recorded as0minutes; nonresponders contacted by phone. Baseline/follow-up questionnaires with incomplete responses collected by phone or visit. DPP attendance/content tracking linked to local program, with existing CDC outcome measures supplied. Brief AE evaluation at6- and12-month visits. Match: self-reported PA, questionnaires, program attendance, safety timepoints.

### P2-N07 — safety definitions

Location: PDF p.34 §§8.4.1–8.4.3. AE includes untoward medical occurrence/disease/injury/clinical sign including abnormal laboratory finding regardless of investigational-device relation; only clinically significant laboratory abnormalities reported as AE. SAE includes death; life-threatening illness/injury; permanent functional impairment/body-structure damage; inpatient hospitalization or prolongation; intervention preventing those outcomes. Planned hospitalization for pre-existing condition/protocol procedure without serious deterioration excluded. Device deficiencies with potential serious outcomes included. Mild/minimal treatment/no activity interference; moderate/reduced daily functioning; severe/interrupted work or significant impairment/incapacity and potentially life-threatening. Causality categories definitely/probably/possibly/not related, based on chronology and clinical judgment. Match: adverse-event table outcome/status definitions.

### P2-N08 — safety windows and trigger

Location: PDF p.35 §§8.4.3.3–8.4.5 lines1090–1130. Walking/light-moderate PA emphasized. Exercise cardiovascular events considered unexpected; directly PA-related muscle soreness/fatigue/musculoskeletal injuries expected. Pre-existing baseline condition not AE unless deteriorates. Capture AE regardless of relation from consent until7days after participation for nonserious AE and30days for SAE (§8.4.4 lines1111–1113). §8.4.5 lines1123–1125 instead labels those windows Grades1–2 and Grades3–5. Follow events until resolution/stabilization. Five Grade3 AEs judged probably related trigger immediate PI notification to IRB/DSMB/NIH and ad-hoc DSMB meeting; NIH may terminate activities posing unreasonable risk. Both printed window formulations preserved; no conclusion is assigned here.

### P2-N09 — pregnancy and reporting

Location: PDF p.36 §§8.4.6–8.5. Existing/planned pregnancy excluded at screening; incident pregnancy requires withdrawal. Death/life-threatening-event PI notification24hours and sponsor/IRB report within3workingdays; other SAE sponsor/IRB ≤10workingdays; FDA unanticipated-device notice ≤10calendardays. No statistical efficacy rule in these operational reporting deadlines. Match: withdrawal population and safety follow-up.

### P2-N10 — site/DSMB context

Location: PDF p.42 chart and §10.1.8 lines1426–1434. Recruiting sites Johns Hopkins Medicine and Reading Health System; DSMB at least semiannually evaluates safety and efficacy by arm under future charter. No numerical efficacy stopping boundary stated here. Match: planned site adjustment and interim-analysis context.

### P2-N11 — data systems

Location: PDF p.43 §10.1.11. REDCap eCRFs, clinical/medication/lab data from source documents; dDPP real-time smartphone data weight and PA minutes/week linked to participant ID. ActiGraph CentrePoint used for device PA. Lab QC annual; site audits minimum3-month intervals. These latter operational intervals do not define outcome-analysis timepoints. Match: measurement origin; dDPP engagement/objective PA distinct data streams.

### P2-N12 — terminology keys

Location: PDF p.45 §10.2 abbreviation table. dDPP=digital diabetes prevention program; hDPP=human coach-based diabetes prevention program; ITT=intention-to-treat; JITAI=just-in-time adaptive intervention; LSMEANS=least-squares means; QOL=quality of life; SAP=statistical analysis plan. P.46 continuation gives SOA/SOC/SOP/UP/US/WHO expansions without new statistical definitions. Match: group and analysis terminology only; expansion does not establish a fitted model.

### P2-N13 — PAR-Q eligibility

Location: PDF p.47 §11.1. Seven yes/no screening items cover heart condition/activity restriction, exertional chest pain, past-month resting chest pain, dizziness/loss of consciousness, bone/joint aggravation, blood-pressure/heart medication, other reason against activity. ≥1yes triggers physician clearance before enrollment/randomization. Match: screened versus randomized population.

### P2-N14 — intervention goals in physician template

Location: PDF p.48 §11.2 lines1583–1590.12-month trial; local CDC-recognized lifestyle program versus digital program of app+body-weight scale. Goals5%weight loss, healthy diet,150minutes/week moderate-intensity activity; gradual goal attainment. These are counseling targets, not independently the exact logical composite definition. Match: randomized intervention duration and goals.

### P2-N15 — demographics variables

Location: PDF pp.49–50 §11.3 (15-item form heading). Sex female/male. Marital status single/married/significant other/divorced/legally separated/widowed/declined/other. Race American Indian/Alaskan Native; Asian; Black/African American; White/Caucasian; more than one race; Native Hawaiian/other Pacific Islander; declined; other; unknown. Ethnicity Hispanic/Latino versus non-Hispanic/Latino plus declined/unknown. Education elementary, middle, high school graduate, some college or more, associate, bachelor, master, doctorate. Name/IDs/date of birth/address also collected but not numerical outcome results. Match: main baseline demographics; age/race/sex/subgroup covariates.

### P2-N16 — comorbidities/medication variables

Location: PDF p.51 §11.4. Resolved history versus active diagnosis categories: hypertension, hypertriglyceridemia, hyperlipidemia, coronary artery disease, PCOS, smoking, depression, anxiety, bipolar disorder, stroke, TIA, peripheral vascular disease, back pain, osteoarthritis, hypothyroidism, asthma, COPD, hepatitisB/C, malignancy, insomnia/sleep disorder, other. Current generic medication names free text. Match: baseline differences and adjustment for glucose-influencing medications; no effect estimate shown.

### P2-N17 — exercise stage-of-change instrument

Location: PDF p.52 §11.5. Four yes/no items: Q1 currently active ≥30min/week; Q2 intent to become more active within next6months; Q3 currently regular activity (regular=30min/day on≥5days/week); Q4 regular activity for past6months. Score classification: all four no=precontemplation; Q1/Q3/Q4 no,Q2yes=contemplation; Q1/Q2yes,Q3/Q4no=preparation; Q1/Q3yes,Q4no,Q2either=action; Q1/Q3/Q4yes,Q2either=maintenance. Match: stage-of-change questionnaire outcome/predictor. These activity thresholds have instrument-specific meanings.

### P2-N18 — self-reported activity form

Location: PDF p.53 §11.6. Survey/phone week preceding ActiGraph; asks total moderate/brisk activity minutes completed in preceding week, explicitly minutes/week not hours. Example30min on5days=150minutes. Optional free-text activity comment. Match: weekly self-reported PA.

### P2-N19 — dietary score

Location: PDF p.54 §11.7. Eight-item Starting the Conversation assessment referring to past few months. Three ordered response columns scored0/1/2; sum0–16, lower=healthier. Item thresholds in column order: fast food times/week <1,1–3,≥4; fruit servings/day ≥5,3–4,≤2; vegetable servings/day ≥5,3–4,≤2; soda/sweet tea glasses/day <1,1–2,≥3; beans/chicken/fish times/week ≥3,1–2,<1; regular snack chips/crackers times/week ≤1,2–3,≥4; sweets times/week ≤1,2–3,≥4; added margarine/butter/meat fat very little/some/a lot. Match: dietary assessment score/scale/direction.

### P2-N20 — apps/devices baseline predictors

Location: PDF p.55 §11.8, seven yes/no items: weight-monitoring app; any home weight scale; automatically smartphone-connected digital weight scale; nutrition app; PA/exercise app; health-data app; wearable fitness tracker. App yes responses allow names. Match: technology exposure/digital engagement predictor; no quantitative outcome result.

### P2-N21 — adapted NPART variables/scales

Location: PDF pp.56–58 §11.9. Heading28items; footnote original36items minus8already on demographic form. Employment employed1 with hours/week; unemployed/jobseeking, unemployed/not seeking, retired, disabled coded0. Occupation classes manager1,professionals2,technicians3,clerical4,service/sales5,agriculture/forestry/fishery6,craft7,machine/plant8,elementary9,armed forces10,never worked11. Partner and living alone yes1/no0. Past12-month care/social participation and friend/neighborhood-contact frequency almost daily4,weekly3,monthly2,less1; children contact almost daily5,weekly4,monthly3,less2,nochildren1. Desired social contact much more4,little more3,not more2,less1. Memory/general-health5verygood to1verybad. Health limitation past6months severely3,limited not severely2,none1. Health-care help frequency4daily to1less. Life quality5verygood,4good,3neither,2poor,1verypoor. Ten internet mastery activities (email,shopping,news,banking,institution access,downloads/games,radio/TV,video calls,social networking,messaging)5excellent/4good/3fair/2poor/1verypoor. Three technology benefit items (everyday support,health monitoring,professional contact) yes3/maybe2/no1. Four device-use frequency items(computer,mobile phone,smartphone/tablet,smartTV/gameconsole) daily5,weekly4,monthly3,lessmonthly2,never1. Scales and codings are form response values, not observed trial means.

### P2-N22 — acceptability questionnaire beginning

Location: PDF p.60 §11.10; heading32items, assigned page contains items1–18, continuation belongs to next shard. Five-category Likert response strongly disagree/disagree/neutral/agree/strongly agree, ordinarily1/2/3/4/5; reverse-coding5/4/3/2/1 for item15(frustrating) and item17(lacked expected functions/information). Items cover interesting advice,fun,motivation,appropriateness,capacity,activity,diet,weight,doctor usefulness,diabetes risk,useful tools,ease of routine,instructions,understandable information,frustration,navigation,missing functions,convenience. Match: acceptability score and reverse-item direction. No overall total-score definition appears on p.60.

## Statistical and planned-analysis relationships

### P2-S01 — ITT follow-up despite nonengagement

Location p.31 §§7.1–7.4. Retain nonengaging randomized participants for efficacy/safety; incident diabetes can continue; completion and program-start-duration definitions separate. Compare with p.37 population language in P2-S07 and main-paper analysis denominator; this extraction does not resolve or diagnose differences.

### P2-S02 — validity versus missing-data handling

Location p.33 §8.2. Repeat activity measurement below75%wear and discard incomplete record. Compare with analysis missingness trigger >5% and100%-valid-PA complete-case rule pp.38–39 (P2-S09). Relevant quantities distinguish wear-time validity within a record from missing outcome data across participants/timepoints.

### P2-S03 — safety decision rule

Location p.35 §8.4.5 lines1126–1130. Five probably-related Grade3AEs require immediate notifications and ad-hoc DSMB; NIH unreasonable-risk determination can end investigations. This is a safety review trigger, separate from planned efficacy interim analysis (P2-S16).

### P2-S04 — NI hypothesis/margin and expected success

Location pp.36–37 §9.1 lines1171–1195. Digital versus human-coached NI design; success=attainment of binary composite CDC benchmark. Assumed50%success in each arm; stated equivalence limit d=15%. π_s denotes hDPP success; π_e denotes dDPP success. Null standard percentage exceeds experimental by15or more percentage points: printed H0:π_s≥π_e+15; alternative Ha:π_s−15<π_e. Percent-scale15 corresponds to0.15on proportion scale. NI direction therefore rules out hDPP advantage≥15points. Narrative says experimental π_s−15or better. Exact glyph formulas preserved. Historical rationale:5%weight-loss-at12months contrast46.7% (95%CI43.1%–50.2%) for lifestyle versus placebo; margin/full effect≈32%, described below50%recommended threshold. Five participating hDPP program data:50%5%-weight-loss success (range47%–60%);50%4%-weight-loss+150minPA (29%–80%), completers. Anticipated ITT hDPP success30%–40%but50%used for largest sample requirement. Historical values are margin rationale, not trial results.

### P2-S05 — sample-size assumptions and confidence rule

Location p.37 §9.2 lines1197–1204.1:1randomization; alpha5%; power80%;50%success per arm;138analyzable each,total276.25%12-month attrition gives184each,total368. Stated objective: if truly no difference,276participants gives80%certainty upper limit of one-sided95%CI excludes hDPP advantage>15%. Match main: margin, sidedness, alpha/power/retention assumptions. Printed numbers preserved for independent reproduction.

### P2-S06 — unadjusted primary testing declaration

Location p.37 §9.3 lines1206–1211. All primary effectiveness statistical analyses stated unadjusted; two-sided significance tests stated. Preserve alongside NI one-sided95%confidence statement in §9.2, and model statements below; no conclusion assigned by mapper.

### P2-S07 — analysis populations

Location p.37 §9.3. ITT evaluate all participants by initial allocation regardless of adherence or protocol violations/deviations; effectiveness analyses exclude study withdrawal or consent withdrawal. Effectiveness ITT population; PP population program completers in each group as defined §3.3, for CDC benchmarking. Safety ITT on p.40 §9.4.10. Program-completer exact definition outside this shard; coordinator joins preceding-shard §3.3. Match report: ITT/modifiedITT/full analysis set, treatment received, withdrawals, PP.

### P2-S08 — general inferential methods and clustering

Location p.37 §9.4.1 lines1215–1225. Pool both sites. Exploratory distribution/outlier/missingness examination. Mean/median/frequency baseline summaries; categorical proportion/frequency. Baseline continuous group comparisons unpaired t-tests or Wilcoxon signed-rank test as printed; categorical chi-square or Fisher exact. Between-group primary/secondary ITT outcomes mixed-effects logistic regression to account for within-program-site clustering. Continuous secondary outcomes linear regression; binary secondary logistic regression. Regression interaction terms evaluate effect modification. Match report: primary logistic/mixed-effects model, random site/program structure, continuous models and interaction tests.

### P2-S09 — missingness and complete-case sensitivity

Location p.38 §9.4.2 lines1227–1232 and p.39 lines1274–1279. Low expected A1C/weight missingness among completers; PA monthly device compliance may generate missingness. If >5%data for PA missing, primary analysis based on multiple imputation; sensitivity complete-case defined100%PA data on p.38 and100%valid PA data on p.39. If findings differ significantly interpret primary in light of sensitivity. No imputation model, number of imputations, or distribution is specified on assigned pages; missingness trigger preserved. Match main/report supplement missing-data analysis.

### P2-S10 — study-site sensitivity

Location p.38 §9.4.4 lines1240–1243. All outcome measures sensitivity analyses account for Johns Hopkins Hospital versus Reading Hospital, investigating treatment or treatment-response differences by study site. Match reported site-adjusted/stratified/interaction sensitivity models.

### P2-S11 — covariate sensitivity and primary model

Location p.38 §9.4.5 lines1245–1250 and §9.4.7 lines1259–1263. Primary analyses unadjusted. If baseline characteristics differ or exposures to potential confounders such as steroids/antihyperglycemics arise, supportive multivariable logistic/linear models include relevant covariates. Primary CDC-benchmark attainment dependent variable; treatment arm primary exposure; ITT logistic regression. Adjusted models include variables statistically significantly different in univariate between-arm baseline/study-period analyses, including glucose-influencing medication and incident diabetes. Match primary adjustment status and supportive model covariate list.

### P2-S12 — within-arm exploratory analysis

Location p.38 §9.4.6 lines1252–1255. Separate within-hDPP and within-digital analyses explore success-associated factors (printed second arm DPP). hDPP-only additional exploration by study site, hDPP program site, program type(hospital,primarycare,church,community). Match subgroup/engagement/program exploratory results; not a primary comparison.

### P2-S13 — baseline presentation

Location p.38 §9.4.3 lines1234–1238. Demographics(age,race,gender),socioeconomic(employment,education),metabolic comorbidities and baselineA1C/weight reported. Normal continuous distributions mean/SD; nonnormal median/IQR. Match report descriptive unit/population and dispersion labels.

### P2-S14 — secondary outcomes and tests

Location p.38 §9.4.8 lines1266–1271 continuing p.39 lines1272–1273. ITT individual binary CDC-composite outcomes secondary at6and12months via logistic models. A1C change,absoluteweightchange,percentweightchange continuous linear models. Activity continuous average minutes/week by light/moderate/intense,METhours/week,andsteps/day. Acceptability Likert-item responses nonparametric Spearman correlation or chi-square independence; overall Likert scores parametric Pearson correlation or t-test. These printed status/model/timepoint specifications matched to report secondary analyses; exact composite components/thresholds are in prior shard.

### P2-S15 — economic plans

Location p.39 §9.4.9. dDPP versus hDPP12-month and lifetime cost-effectiveness,health-system perspective,discount future costs/effects3%. Lifetime Markov states normal glucose tolerance,impaired fasting glucose,impaired glucose tolerance,type2diabetes,death; trial/literature transition inputs, future diabetes incidence proxied by A1C change. Costs from resource utilization×unitprices; baseline/6/12month history/medication/utilization,publicprices/Medicare; dDPPcompany costs,hDPPMDPPfees. QALYs time-in-state×utility; ICER incremental arm comparison,decision below willingness-to-pay threshold(no numeric threshold here). Univariate and probabilistic sensitivities vary transition/utility/cost; probabilistic acceptability curve. No results on assigned pages. Match planned outcome status if economic analysis reported elsewhere.

### P2-S16 — safety/interim/individual-data reporting

Location p.40 §§9.4.10–12 lines1322–1327. Safety analyses ITT and frequency tables. Explicit no planned interim analysis. Individual data not listed by measure/timepoint; primary/secondary summary measures reported. Match safety denominator and interim rule.

### P2-S17 — qualitative study closure

Location pp.40–41 §10.1.4 lines1363–1375. Suspension/termination for reasonable cause; examples unexpected/significant/unacceptable participant risk,insufficient protocol compliance,insufficiently complete/evaluable data. May resume after concerns addressed to sponsor/IRB satisfaction. No numerical efficacy stopping boundary. This administrative closure is recorded separately from safety trigger and no planned statistical interim analysis.

### P2-S18 — NPART planned predictor use

Location p.56 lines1661–1664. Adapted NPART characterizes nonparticipation in digital-health research; not used to exclude otherwise eligible participants; responses analyzed as predictors of response to digital versus in-person DPP. Match technology/social predictors and effect-modification analyses. This use statement does not specify a model or observed result.

## Handoff and limitations

All assigned source units mapped. Main-paper matching keys are conceptual join keys, because this disjoint agent did not inspect unassigned main/results source pages. The coordinator should integrate these specifications with DOC-001/DOC-003 maps and adjacent plan-shard definitions. No candidate finding IDs are assigned here. Printed formulations that may require comparison were preserved without scientific diagnosis. Reusable image provenance is not independently hashed to the historical source; present package/source identifiers and page sections establish locator identity, with direct-source recheck controlling any eventual candidate evidence. Both decoder failures were fully recovered; no readability limitation remains. GPU OCR generated concurrently by coordinator was not needed or consumed for this shard.
