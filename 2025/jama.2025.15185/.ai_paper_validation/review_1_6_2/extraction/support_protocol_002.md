# Support quantitative evidence: protocol shard 002

## Scope, identity, provenance

Exact disjoint scope: DOC-002, `joi250066supp1_prod_1761597796.4601.pdf`, physical PDF pages 25–48 inclusive (24 pages). Document role: PLAN throughout. Pages25–46 continue protocol version 1.1 dated 30 November 2018, as identified by the source inventory/preceding protocol cover; no new version cover occurs within those pages. Physical p47 begins Clinical Study Protocol version **1.4, 28.02.2023**; p48 repeats that version/date in its approval text. Preserve these version boundaries when matching later results. No conclusions or candidates are generated here.

All24 reusable source-linked PNG pages were opened and visually read, individually, at `.ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc002/page-N.png`, N=25…48. Text was supplemented by fresh CPU Tesseract5.5.0 OCR, English, PSM3; derivative commands/status are recorded in `../preprocessing/protocol_002/derivative_record.md`. Historical protocol native/layout text is not usable scientific text and was not used. No new PDF renders; no sources or historical assets modified. Physical source pages, rather than OCR, determine the readings below. OCR glyph normalization is limited to visually confirmed transcription (e.g. ≤ and ≥); it does not change source numbers. No workbook/CSV is present in assigned scope, so formula-versus-cache distinction is not applicable.

Source link base from this extraction directory: [DOC-002](../../../joi250066supp1_prod_1761597796.4601.pdf#page=25). Matching main-paper keys below are semantic join keys, not assertions about the report; main-paper pages are outside this shard.

## Complete page coverage

| Physical page | Sections/content | Mapping status |
|---:|---|---|
|25|5.2.1 harm continuation;5.2.2 selected-center secondary assessments|COMPLETE; PR2-001…011|
|26|5.2.3 further selected-center assessments;5.3 safety;6.1 design;Figure2|COMPLETE; PR2-012…015|
|27|6.1 intervention/visits;6.2 minimization and masking;6.3 unblinding start|COMPLETE; PR2-016…020|
|28|6.3 unblinding;7 population/eligibility/recruitment/allocation;7.4 withdrawal start|COMPLETE; PR2-021…024|
|29|7.4 discontinuation;8.1 intervention/control/package/storage|COMPLETE; PR2-024…027|
|30|8.2 dose modifications;8.3 adherence;8.4 withdrawal;8.5 preventive measures;8.6 concomitant interventions|COMPLETE; PR2-028…032|
|31|8.6 rehabilitation;8.7 accountability;8.8 returned capsules;9 assessments|COMPLETE; PR2-033…035|
|32|9.1 primary/secondary/harm/withdrawal outcomes;9.2 screening/baseline|COMPLETE; PR2-036…040|
|33|9.2 treatment and visits2/3;9.3 visits4/5;9.4 transition|COMPLETE; PR2-041…046|
|34|9.4 transition/unscheduled;10.1 safety and definitions, causality table start|COMPLETE; PR2-047…050|
|35|Causality table continuation; unexpected/SUSAR;CTCAE grades;reporting|COMPLETE; PR2-050…053|
|36|Pregnancy/reporting;10.1.4 follow-up/data variables;10.2 observational safety|COMPLETE; PR2-054…057|
|37|10.2 serious-event rule;11.1 hypothesis;11.2 sample size|COMPLETE; PR2-058…061|
|38|Figure3 sample size;PROMIS/walking power;11.3 termination/composite safety|COMPLETE; PR2-062…065|
|39|11.4 SAP/populations/primary/sensitivity/secondary analysis|COMPLETE; PR2-066…073|
|40|11.4 secondary/exploratory/interim/safety/deviations;11.5 missing data;12.1 eCRF start|COMPLETE; PR2-074…080|
|41|12.1–12.3 data archiving/management/monitoring|COMPLETE; administrative only, PR2-081|
|42|12.4–12.6 audits/confidentiality/specimen storage;13 publication;14 funding;15 insurance|COMPLETE; no additional result-relevant quantitative/statistical relationship; selected-center consent corroborates PR2-012|
|43|16 references1–24(part)|COMPLETE; no applicable trial quantitative relationship, bibliographic numbers only|
|44|References24–43|COMPLETE; no applicable trial quantitative relationship, bibliographic numbers only|
|45|References44–67(part)|COMPLETE; no applicable trial quantitative relationship, bibliographic numbers only|
|46|References67–78;17 appendix list|COMPLETE; no additional trial relationship; source reference78 names MICE, linked to PR2-080|
|47|Version1.4 protocol cover|COMPLETE; PR2-082|
|48|Version1.4 signature/approval page|COMPLETE; PR2-083|

## Quantitative, outcome and intervention relationships

| Local key | Physical source page/section | Printed definition/value/design statement | Matching report key |
|---|---|---|---|
|PR2-001|[p25](../../../joi250066supp1_prod_1761597796.4601.pdf#page=25),5.2.1|Harm in interventional phase: mortality(all cause), recurrent stroke(any), SAEs, prespecified nonserious AEs possibly related to IMP; observational phase3–12months: mortality(all cause), recurrent stroke(any).|Safety outcomes/collection windows|
|PR2-002|p25,5.2.2|Selected-center secondary assessments determined by each site contract, not universally required.|Optional outcomes/analysis denominator|
|PR2-003|p25,5.2.2|Motricity Index: UE and LE subscales each0–100; isometric strength.|MI upper/lower|
|PR2-004|p25,5.2.2|Trunk Control Test:4items, item scores0–25; sitting balance tests30seconds without trunk/feet support.|TCT|
|PR2-005|p25,5.2.2|ARAT four subtests: grasp6items, grip4, pinch6, gross movement3; upper-extremity activity/object handling.|ARAT|
|PR2-006|p25,5.2.2|BBT: number of wooden cubes moved between compartments in60seconds, unilateral gross manual dexterity/affected upper limb.|BBT|
|PR2-007|p25,5.2.2|FAC score0–5, independent walking with/without aid, type of walking surface.|FAC|
|PR2-008|p25,5.2.2|10MWT walking speed and cadence over10m at comfortable and maximum speeds.|10MWT|
|PR2-009|p25,5.2.2|Jamar dynamometer grip/forearm strength, affected and unaffected upper extremities.|Grip strength|
|PR2-010|p25,5.2.2|MoCA score0–30, mild cognitive impairment screening.|MoCA|
|PR2-011|p25,5.2.2|Movement sensors: daily-life physical activity/upper limb use; gyroscope, acceleration, magnetometer, pressure data; activity counts(arm usage); physical states lay/sit/stand/walk.|Sensor outcomes|
|PR2-012|p26,5.2.3; p31,9; p42,12.6|Genetic/blood biomarkers are further selected-center exploratory assessments; sampling baseline or any follow-up visit to generate response-heterogeneity hypotheses. Approx10ml EDTA blood, storage−20°C; optional consent independent of main-study consent, centrally collected.|Exploratory biomarkers|
|PR2-013|p26,5.2.3|Imaging biomarkers: source prints “Now imaging will be performed within the ESTREL study, however” followed by use of routine/observational CT,(functional)MRI to identify response markers including ischemic lesion type/location/volume. This is retained literally; no interpretation of the word “Now” is imposed.|Exploratory imaging|
|PR2-014|p26,6.1|Multicenter parallel placebo-controlled superiority trial,1:1 allocation; patients/care providers/investigators/outcome assessors blinded. Levodopa plus standardized rehabilitation over5weeks soon after acute stroke expected to yield at least6points higher FMMA at3months; planned610patients.|Design, primary hypothesis, enrollment target|
|PR2-015|p26 Figure2; p27 caption|PRECIS design radar radial labels1–5; domains eligibility/recruitment/setting/organization/flexibility delivery/flexibility adherence/follow-up/primary outcome/primary analysis. Visual radial scores respectively4,5,5,5,4,4,2,2,5. Scores entered by consensus; design description, not treatment outcomes.|Design context only|
|PR2-016|[p27](../../../joi250066supp1_prod_1761597796.4601.pdf#page=27),6.1|Dose escalation days1–3 morning only;4–6 morning/noon; full dose days7–34 TID; taper35–37 morning/noon;38–39 morning only. Both groups standardized rehabilitation; enrollment/allocation/treatment onset acute stroke unit before rehabilitation transfer.|Randomized dose/duration|
|PR2-017|p27,6.1|Participation12months: interventional3months randomization→Visit3; observational9months afterVisit3→Visit5. Main intervention ends5weeks; in-person baseline/end-treatment/primary outcome then6- and12-month visits.|Time origin/phase/follow-up|
|PR2-018|p27,6.2|Center stratification, standard minimization within stratum;80% allocation probability to group minimizing imbalance, avoiding predictable alternation; implemented by CTU Basel in secuTrial.|Randomization/stratification|
|PR2-019|p27,6.2.1|Investigators, participants, therapists/physicians/nurses, outcome assessors and statistician blinded throughout; independent distributor; identical aspect/texture/taste. Safety DSMC not blinded.|Masking/analysis|
|PR2-020|p27,6.2.2|All primary/secondary assessments by personnel trained in specific assessment instruments.|Measurement procedure|
|PR2-021|p27–28,6.3|Safety-required unblinding by authorized investigators through secuTrial, documented in integrated audit trail.|Masking exceptions|
|PR2-022|p28,7/7.1|Acute ischemic stroke printed “≤7 since stroke symptom onset”, clinically meaningful hemiparesis requiring inpatient rehabilitation; hemorrhagic stroke excluded.610planned; treatment day1–39; all synopsis inclusion criteria and no exclusions, no exceptions. Full itemwise synopsis criteria are outside this shard.|Eligibility/population|
|PR2-023|p28,7.2/7.3|Prescreen day0–7 since symptoms, written participant/next-of-kin consent before study-specific procedures, after ward admission; no emergency inclusion. Instant computer-generated allocation at enrollmentVisit1. Administrative travel refund20CHF/patient/visit.|Eligibility/randomization origin|
|PR2-024|p28–29,7.4|Night adverse reactions permit dosage1-1-0 per day. Early discharge earlier than5weeks minus7days: encourage continuation toVisit2; if declined stop full treatment and taper5days. Unscheduled end visit withdrawal/discontinuation day±3days.|Dose modification/adherence/end visit|
|PR2-025|p29,7.4|AE/SAE/SUSAR with at least probable study-drug relation may reduce, temporarily or permanently discontinue dose; also contraindication, medically mandatory open levodopa, or physician-assessed significant health risk. Prefer nondopaminergic treatment for new levodopa-treatable conditions beforeVisit3.|Intercurrent events|
|PR2-026|p29,8.1.1–8.1.2|Levodopa100mg/carbidopa25mg orally days1–39 afterVisit1; NG/PEG allowed for inability to swallow, minimum possible period/documented. Matching placebo identical route/duration/phases.|Randomized drug and control|
|PR2-027|p29–30,8.1.3–8.1.4|Capsules identical; expected shelf life12months; storage15–25°C away from light.|Drug handling, no outcome relationship|
|PR2-028|p30,8.3|Study-site nurses administer during expected inpatient acute/rehabilitation period. Discharge beforeVisit2: encourage protocol continuation with medication plan. Drugs numbered for complete39days; returned capsule number recorded atVisit2.|Compliance measure|
|PR2-029|p30,8.4|All study data collected up to withdrawal will be analyzed.|Analysis population/missingness|
|PR2-030|p30,8.5|Pregnancy test before enrollment; contraception during day1–39 and one month thereafter.|Eligibility/safety window|
|PR2-031|p30,8.6|Off-label product intended to enhance stroke rehabilitation/recovery prohibited until3-month primary-outcome visit.|Concomitant intervention restriction|
|PR2-032|p30,8.6|Concomitant drugs recorded each visit: antiplatelets, anticoagulants, antihypertensives, statins, serotonin-reuptake inhibitors, serotonin-noradrenaline reuptake inhibitors, benzodiazepines, neuroleptics, antiepileptics, antidiabetics, analgesics, immunosuppressive/immunomodulating drugs, antibiotics.|Concomitant treatment definition|
|PR2-033|p30–31,8.6|Both groups same standardized motor-learning rehabilitation: active patient-initiated task-specific exercise; individually progressive/challenging exercise; performance feedback; repetitions/rest; goals/coaching/positive feedback.3rehabilitative sessions per workday; at least2sessions standardized motor rehabilitation from trained physical/occupational therapists. Record amount(minutes/hours)/type; early phase shorter more frequent sessions preferred.|Rehabilitation randomized cointervention/dose|
|PR2-034|p31,8.6|If physician considers levodopa mandatory, study medication discontinued but patients remain as “off-study-medication-patients”.|Intercurrent-event population retention|
|PR2-035|p31,8.7/8.8|Drug receipt and batch accounting; returned capsules counted atVisit2 and entered eCRF.|Adherence/capsule count|
|PR2-036|[p32](../../../joi250066supp1_prod_1761597796.4601.pdf#page=32),9.1.1|Primary outcome between-group FMMA score difference measured3months±14days after randomization(Visit3). Certified/trained personnel; eCRF score;3-month assessment also filmed and supplied to Basel for central blinded rating. All primary assessors blinded.|Primary endpoint/time/central rating|
|PR2-037|p32,9.1.2/9.1.2.1|Secondary outcomes by trained certified assessors; full definitions/timepoints cross-referenced to5.2/schedule. InterventionalVisit1–3: all-cause mortality, any recurrent stroke, SAEs and prespecified nonserious possibly related AEs;3–12months mortality/recurrent stroke.|Secondary/safety outcome windows|
|PR2-038|p32,9.1.3|Data through premature withdrawal “may be used for further analyses”; procedures refer7.4.|Withdrawal analysis rule|
|PR2-039|p32,9.2.1|Prescreen day−7 to0 before randomization;24h latency after thrombolysis/thrombectomy before screening/enrollment; meaningful hemiparesis NIHSS≥3 for arm plus leg motor functions.|Enrollment criteria/timing|
|PR2-040|p32,9.2.2|Visit1 day0, final eligibility/consent/baseline before allocation. Mandatory baseline FMMA,NIHSS,mRS,RMI; selected centers ARAT,BBT,JDT,MI,TCT,FAC,10MWT,MoCA,sensors.|Baseline covariates/outcome availability|
|PR2-041|p33,9.2.3|Treatment starts day after randomization(day1),100/25mg vs placebo1:1 through39; schedule repeats PR2-016 exactly.|Intervention time origin/schedule|
|PR2-042|p33,9.2.4|Visit2 at5weeks±7days; end-treatment in-person; record cointervention number/length/type; outcomes per schedule; harm any prespecified possibly related nonserious AE or SAE, any recurrent stroke, all-cause mortality; returned capsules counted.|End treatment visit/safety/adherence|
|PR2-043|p33,9.2.5|Visit3 at3months±14days; primary in-person; concomitant medication/therapy post-treatment; same harms asVisit2.|Primary visit window|
|PR2-044|p33,9.3.1|Visit4 at6months±20days, first observational in-person; concomitant drug/therapy; any recurrent stroke and all-cause mortality.|6-month endpoint window|
|PR2-045|p33,9.3.2|Visit5 at12months±30days, second observational in-person, same procedures asVisit4.|12-month endpoint window|
|PR2-046|p33–34,9.4|Acute→rehabilitation transition non-in-person data: concomitant therapies number/length/type; transfer drug; harms since randomization AE/SAE,all-cause mortality,any recurrent stroke; rehabilitation center identity. Unscheduled end follows schedule/7.4.|Transition/intercurrent safety data|
|PR2-047|p34,10.1|Printed safety text: all-cause mortality, any recurrent stroke, SAEs and prespecified nonserious AEs documented “up to3months(i.e.Visit2) after study enrolment”. Both time and visit label retained as printed, without diagnosis.|Safety collection limit/visit label|
|PR2-048|p34,10.1.2|AE any untoward occurrence associated temporally with medicinal product whether causally related or not, including abnormal laboratory findings.|AE outcome definition|
|PR2-049|p34,10.1.2|Prespecified AEs: nausea,vomiting,taste disturbance,dry mouth,anorexia,arrhythmias,postural hypotension,syncope,drowsiness(including sudden sleep),fatigue,dementia,psychoses,hallucinations,confusion,euphoria,abnormal dreams,insomnia,depression,anxiety,dizziness,dystonia,dyskinesia,chorea.|Prespecified AE list|
|PR2-050|p34–35,10.1.2/table|SAE death,life-threatening,inpatient admission/prolongation,persistent/significant disability/incapacity,congenital anomaly/birth defect; important medical events jeopardizing health or needing intervention also serious. Causality: definitely temporal/dechallenge/rechallenge(or other proof); probably temporal/dechallenge/no other cause; possibly temporal/other cause possible; unlikely any assessable reaction not meeting foregoing; not related causal relationship ruled out. Dechallenge considered only where applicable.|SAE/causality definitions|
|PR2-051|p35,10.1.2|Unexpected drug reaction nature/severity inconsistent with product info; SUSAR related to product and both serious/unexpected. CTCAE version5,27Nov2017 severity grades1mild,2moderate limiting instrumentalADL,3severe/medically significant hospitalization/disability limiting self-careADL,4life-threatening urgent intervention,5death related toAE.|Safety grading/classification|
|PR2-052|p35,10.1.3|SAE report immediately/max24h to sponsor; fatal SAE ethics within7days; SUSAR within7days if fatal or15days other; signals sponsor24h, ethics/regulator7days.|Safety operational decision timelines|
|PR2-053|p35–36,10.1.3|Pregnancy/breastfeeding/lack contraception excluded; pregnancy immediately withdrawn; pregnancy during treatment or30days after discontinuation reported within24h; annual safety report once/year.|Eligibility/intercurrent event/safety follow-up|
|PR2-054|p36,10.1.4|Unresolved SAEs and possibly related prespecified nonseriousAEs atVisit3 followed medically as long indicated, without further EDCS recording.|Safety ascertainment after main phase|
|PR2-055|p36,10.1.4|NonseriousAEs of interest/discontinuation AEs collect verbatim description,start/stop dates,max intensity,seriousness,causality yes/no,frequency(single/intermittent/continuous),study-medication action,outcome.|AE quantities/data structure|
|PR2-056|p36,10.1.4|AdditionalSAE data: event severity/outcome/expectedness,serious criteria date,investigator awareness date,criteria,hospitalization/discharge dates,probable cause/date death,autopsy report/results,causality study procedure/other medication,concomitant drug/history.|SAE quantities/data structure|
|PR2-057|p36,10.2|Observational phase3–12months records all-cause mortality,any recurrent stroke,SeriousEvents underHRO20; immediate protective action sponsor24h/ethics7days.|Observational safety definition|
|PR2-058|p36–37,10.2.2|HRO21 serious event cannot exclude attribution to sample collection/health-data collection, and requires unplanned inpatient treatment/prolongation,life-threatening ordeath; if occurs research interrupted and ethics informed within7days.|Observational stopping rule|

## Statistical relationships, populations and decision rules

All locations below are physical pages in DOC-002 (PLAN). Each row is a semantic key for matching the corresponding report analysis; it does not diagnose a candidate.

| Local key | Page and section | Planned relationship, definition and inputs | Matching report key |
|---|---|---|---|
| PR2-059 | [p37](../../../joi250066supp1_prod_1761597796.4601.pdf#page=37),11.1 | Primary superiority hypothesis: levodopa plus standardized rehabilitation over 5 weeks, starting soon after stroke, yields at least 6 points higher FMMA at 3 months than placebo plus rehabilitation. | Primary hypothesis |
| PR2-060 | p37,11.2 | Power based on 6-point FMMA difference at 3 months; normally distributed FMMA, SD25. Historical FLAME placebo mean35.1, SD22, day90 used as background, yielding illustrative active mean41.1. Baseline/follow-up within-patient correlation assumed high but no reliable estimate; power calculation assumes t-test without quantifying baseline-adjustment gain. | Sample-size assumptions |
| PR2-061 | p37,11.2 | 548 patients,1:1 allocation,80% power,two-sided 5% significance,normal SD25,mean difference6. Allow 10% dropout→305 per arm,total610. No sample-size formula printed. | Sample size/power/dropout |
| PR2-062 | [p38](../../../joi250066supp1_prod_1761597796.4601.pdf#page=38),Figure3 | Assumed SD25 points; sample-size sensitivity to treatment difference(points). Curves power0.7,0.8,0.9,smoothed for illustration; annotated θ=6,N=548 on power0.8 curve. X ticks5,6,7,8,9; y sample-size ticks200,400,600; no tabulated curve values. | Power sensitivity figure |
| PR2-063 | p38,paragraph below Figure3 | Trial also designed for 80% power to detect patient-reported PROMIS improvements at 3 months, but less empirical support for novel measure in this population; sample-size calculation based primarily on traditional scores. No quantitative PROMIS difference/SD here. | PROMIS power rationale |
| PR2-064 | p38,second paragraph | Total610 evaluates walking ability,RMI≥7(as DARS). Assume45% placebo independently walking at5weeks;80% power,5% significance to detect12 percentage-point increase to57% active. Printed interpretation absolute12% or relative27% increase. | RMI walking/time/power |
| PR2-065 | p38,11.3 | No efficacy stopping rules. Safety termination possible on DSMC recommendation. DSMB monitors primary composite safety: death(any cause),recurrent stroke,SAEs. Composite risk alert thresholds to be defined in DSMC charter taking DARS findings into account; no numeric threshold here. | Safety composite/stopping |
| PR2-066 | [p39](../../../joi250066supp1_prod_1761597796.4601.pdf#page=39),11.4 | Detailed summaries/statistical analyses in SAP; finalized before database closure,version controlled at CTU Basel. | SAP timing |
| PR2-067 | p39,11.4.1 | FAS all randomized patients; ITT according to randomly allocated treatment. Complete cases all FAS patients without missing FMMA at baseline or3months. All patients analyzed by allocation; withdrawal reasons by group and qualitatively compared. | FAS/ITT/complete cases |
| PR2-068 | p39,11.4.1 | PP: FAS patients receiving at least80% prescribed levodopa/carbidopa or placebo,or justified reduced dose1-1-0/day under7.4; also at least5 rehabilitation sessions/week. | PP adherence criteria |
| PR2-069 | p39,11.4.2 | Primary endpoint FMMA3months “after onset of treatment”. Mixed-effects model: baseline FMMA covariate and two-level treatment factor(levodopa vs placebo) fixed effects; random intercept for each center. Analysis after termination/database closure;two-sided5% significance. | Primary model/time origin |
| PR2-070 | p39,11.4.3a | Primary FMMA3months sensitivity: exploratory treatment heterogeneity across centers through graphical display stratified by center. | Center heterogeneity |
| PR2-071 | p39,11.4.3b | Exploratory covariates itemwise: age;sex;dementia;selective hand/wrist movement at baseline;cortical dysfunction(aphasia/neglect/hemianopia);fatigue(patient self-report);SSRI treatment;mild extrapyramidal motoric symptoms(physician judgment);reduced impetus(physician judgment). Compare results with main analysis. | Prespecified exploratory covariates |
| PR2-072 | p39,11.4.3c–d | Repeat main analysis in complete cases(exclude imputation of primary endpoint or baseline FMMA) and PP set to examine protocol deviations. Consider marginal structural models for major deviations. All analyses except complete-case/PP on FAS. | Complete-case/PP sensitivity |
| PR2-073 | p39–40,11.4.4 | Secondary regression appropriate to data type,adjusted as main analysis,baseline measures where available. Binary: logistic(GLM logit link/binomial distribution);continuous: linear;ordinal: ordinal logistic. Inspect models as main analysis;severe assumption violations/high-leverage outliers→consider transformations,nonparametric tests,or robust regression. | Secondary models |
| PR2-074 | [p40](../../../joi250066supp1_prod_1761597796.4601.pdf#page=40),11.4.4 | Each model presents estimated treatment difference,P value,95% CI;two-sided5% significance. Endpoints also descriptive tables/graphs;FAS/all randomized/allocated-group ITT. No multiplicity adjustment or outcome hierarchy specified on assigned statistical pages. | Effect measure/CI/P/multiplicity |
| PR2-075 | p40,11.4.4 | Exploratory genetic/other biomarker(routine imaging/fMRI included) response analyses;examples COMT rs4633 exon5,rs4680 exon6;genomic imbalance using high-density SNP microarrays/copy number variation. Future individual-patient-data meta-analysis intended;additional exploratory analyses possibly triggered by relevant findings. | Exploratory prespecification |
| PR2-076 | p40,11.4.5 | Interim analysis not planned. | Interim rule |
| PR2-077 | p40,11.4.6 | Detailed examination of prespecified events,AEs,SAEs;estimate by treatment group proportion of patients with at least one prespecified AE;DSMC close monitoring. | Safety estimand |
| PR2-078 | p40,11.4.7 | Analysis deviations reported to CEC/CA;substantial needed deviations→protocol amendment. All protocol/detailed SAP analysis deviations listed and justified in separate final statistical report section. | Disclosed deviations |
| PR2-079 | p40,11.5 | Up to10% dropout considered in sample-size calculation;careful study conduct to minimize missing data. | Missing-data assumption |
| PR2-080 | p40,11.5;p46 reference78 | Missing data addressed by multiple imputation by chained equations(Van Buuren2011);predictive models create clinically reasonable imputations;impact assessed by complete-case sensitivity. Number of imputations,predictor list,and pooling details not printed on assigned pages. Reference78 identifies MICE publication;no external source consulted. | Primary missing data |
| PR2-081 | p40–41,12.1–12.3 | Unique eCRF identifier per patient;withdrawal reason recorded;database blocked after completion/monitoring/query resolution;complete dataset exported to statistician/PI;independent CTU Basel statistical analysis;minimum10-year archive. Administrative procedure,no further inferential relationship. | Database closure |
| PR2-082 | [p47](../../../joi250066supp1_prod_1761597796.4601.pdf#page=47),cover | New protocol version1.4 dated28.02.2023;ESTREL,NCT03735901;risk categoryC;investigational levodopa/carbidopa100/25mg. | Latest protocol identity/dose |
| PR2-083 | [p48](../../../joi250066supp1_prod_1761597796.4601.pdf#page=48),approval | Sponsor/trial statistician approval text explicitly version1.4 dated28.02.2023;blank place/date/signature fields. Statistician Sabine Schädelin,CTU Basel. | Version boundary |

## Coverage and handoff

Complete:24/24 assigned physical pages;83 local relationship/context keys PR2-001…083. PR2-015 is a visually read design-context figure, not an inferential result. Pages42–46 have no additional trial quantitative relationship (p42 selected-center consent and p46 MICE reference only corroborate existing keys);p41 administrative content explicitly mapped as PR2-081. Two figures inspected: Figure2 PRECIS(p26),Figure3 sample-size sensitivity(p38). Tables inspected: causality(p34–35),CTCAE(p35). No scientific coverage gaps. Synopsis itemwise eligibility and full outcome schedule are in other disjoint shards and are cross-referenced rather than assumed missing. No treatment result estimate/CI/P value,workbook formula/cache,or CSV cell occurs on assigned pages.
