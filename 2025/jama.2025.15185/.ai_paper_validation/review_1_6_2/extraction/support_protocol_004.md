# Support protocol mapping shard PR4

## Scope, authority, and derivative record

- Exact complete scope: DOC-002, `joi250066supp1_prod_1761597796.4601.pdf`, physical PDF pages 73–94 inclusive, 22 distinct pages. Document role: PLAN throughout.
- Source-relative evidence links below resolve from this extraction directory via `../../../joi250066supp1_prod_1761597796.4601.pdf#page=N`.
- Every page was opened and visually read from its supplied source-linked reusable image `.ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc002/page-N.png`, N=73,…,94. No old scientific conclusions were read. Existing protocol text was unusable; images were readable at 1275×1650. No higher-resolution rendering was necessary. No Office/workbook/CSV source is in this shard; formulas and cached workbook values are not applicable.
- Bundle identity: continuation of protocol version 1.4, dated 28.02.2023, whose title starts at physical p47 and approval page at p48, as directly confirmed by the disjoint protocol-2 mapper and communicated by the coordinator. No version/date header appears within physical pp73–94; identity is joined from that title-page map. These pages continue sections 6–17 without another protocol title/version boundary.
- Fresh derivative engine: Tesseract 5.5.0, English, CPU, `--psm 6`, `OMP_THREAD_LIMIT=1`. Exact bounded command: `for n in $(seq 73 94); do OMP_THREAD_LIMIT=1 tesseract ".ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc002/page-$n.png" ".ai_paper_validation/review_1_6_2/preprocessing/protocol_004/page-$n" -l eng --psm 6 2>>.ai_paper_validation/review_1_6_2/preprocessing/protocol_004/ocr-engine.log; done`. Outputs are one `page-N.txt` per assigned page. An initial default-thread attempt was interrupted while page73 remained empty; the bounded one-thread retry replaced that new derivative. Sources and reusable images were preserved. Visual page reading is authoritative for this map; OCR is a transcription aid.
- Local relationship keys PR4-N### and PR4-S### are unique to this shard. The coordinator can assign global N/S IDs when merging. Matching main-paper keys describe the outcome/design relationship for subsequent matching, without reading unassigned main-paper material or diagnosing candidates.

## Exhaustive page coverage

| Physical page | Inspected content | Applicable record keys | Mapping status |
|---|---|---|---|
| 73 | PRECIS design figure; allocation, treatment phases, follow-up phases | PR4-N001, PR4-N002, PR4-S001 | COMPLETE |
| 74 | Bias minimization; allocation and masking; population and eligibility pointer | PR4-N003, PR4-S002 | COMPLETE |
| 75 | Assignment; withdrawal and dose modification | PR4-N004, PR4-N005 | COMPLETE |
| 76 | Intervention identity/dose/route; compliance; withdrawn data | PR4-N006, PR4-S003 | COMPLETE |
| 77 | Concomitant treatments and standardized rehabilitation | PR4-N007, PR4-N008 | COMPLETE |
| 78 | Drug accountability; primary assessment; secondary safety windows | PR4-N009, PR4-N010, PR4-S004 | COMPLETE |
| 79 | Pre-screening; baseline tests; dosing; visits2/3 | PR4-N011, PR4-N012 | COMPLETE |
| 80 | Visits3–6; transition; optional long-term extension | PR4-N013, PR4-N014 | COMPLETE |
| 81 | Visits7–9; AE/SAE definitions | PR4-N015, PR4-N016 | COMPLETE |
| 82 | Safety causality and grading tables; SAE reporting | PR4-N017, PR4-N018 | COMPLETE |
| 83 | Safety reporting/follow-up and recorded AE/SAE variables | PR4-N019, PR4-N020 | COMPLETE |
| 84 | Observational safety; primary hypothesis; sample-size inputs | PR4-N021, PR4-S005, PR4-S006 | COMPLETE |
| 85 | Power sensitivity figure; walking/PROMIS power; safety stopping | PR4-N022, PR4-S007, PR4-S008 | COMPLETE |
| 86 | Populations; primary model; every sensitivity specification | PR4-S009, PR4-S010, PR4-S011 | COMPLETE |
| 87 | Secondary models; exploratory analyses; interim/safety/missingness | PR4-S012, PR4-S013, PR4-S014, PR4-S015 | COMPLETE |
| 88 | Data collection, dropout record, database closure, archival procedures | PR4-N023 | COMPLETE |
| 89 | Monitoring, privacy, biological secondary outcomes; publication/funding | PR4-N024 | COMPLETE |
| 90 | Insurance section only | No applicable quantitative/design relationship | COMPLETE |
| 91 | References1–24; p24 continues on next page | No applicable quantitative/design relationship; citations only | COMPLETE |
| 92 | Reference24 continuation and references25–43 start | No applicable quantitative/design relationship; citations only | COMPLETE |
| 93 | Reference43 continuation and references44–66 | No applicable quantitative/design relationship; citations only | COMPLETE |
| 94 | References67–79; appendix titles I–V | PR4-N025; citations supply no new planned analysis | COMPLETE |

## Intervention, population, assessments, and safety map

### PR4-N001 — Design and intervention phases

[Physical p73](../../../joi250066supp1_prod_1761597796.4601.pdf#page=73), section6.1 continuation. Eligible consenting patients are randomized 1:1 to levodopa/carbidopa versus matching placebo. Three phases: days1–3 one morning dose daily; days4–6 morning plus lunchtime; days7–34 three times daily; taper days35–37 morning plus lunchtime; days38–39 morning only. Both comparison groups receive standardized rehabilitative therapies. Enrollment, randomization, allocation, and onset occur in acute stroke unit before transfer to rehabilitation. Main-paper matching key: randomized intervention dose/duration and allocation contrast.

### PR4-N002 — Follow-up phases and PRECIS figure

[Physical p73](../../../joi250066supp1_prod_1761597796.4601.pdf#page=73). Total participation12 months: interventional phase randomization through Visit3 at3 months; observational phase thereafter through Visit5 at12 months, duration9 months. Main intervention said to end5 weeks post-randomization; pharmacokinetic wash-out rationale places the interventional endpoint at3 months. In-person visits1 baseline,2 end treatment,3 primary assessment; long-term visits4 at6 months,5 at12 months. Therapy number/duration and transfer information collected at acute-to-rehabilitation transition. Figure2 PRECIS radial scale runs1–5: eligibility4; recruitment4; setting5; organization5; delivery flexibility4; adherence flexibility4; follow-up2; primary-outcome relevance2; primary-analysis inclusion5. These are graphical design scores, not trial efficacy results. Matching key: visit windows and primary outcome timing.

### PR4-S001 — Screening and consent chronology

[Physical p73](../../../joi250066supp1_prod_1761597796.4601.pdf#page=73). Eligibility refers to study synopsis. Screening in acute care center; consent/inclusion after entry to ward, e.g. IMC/stroke unit or neurology ward; no emergency inclusion. All participants described as eligible and signed informed consent before randomization. Matching key: randomization population and timing; actual criterion list resides outside this shard and is not inferred.

### PR4-N003 / PR4-S002 — Allocation, masking, and target population

[Physical p74](../../../joi250066supp1_prod_1761597796.4601.pdf#page=74), §§6.2–7.2. Visit1 random allocation, center stratification; CTU Basel implements in CDMA secuTrial a standard minimization algorithm balancing within each stratum. Allocation probability80% to the group that minimizes the difference within patient's stratum, avoiding predictable alternation. Investigators, participants, therapists/physicians/nurses, outcome assessors, and statistician blinded throughout; independent Bichsel pharmacy labels/packages/dispenses; matching placebo and active product identical aspect/texture/taste except blinded randomization number. DSMC safety monitoring unblinded. Trained specific-instrument personnel perform all primary/secondary outcome assessments. Population: acute stroke ≤7 days after symptom onset, clinically meaningful hemiparesis requiring inpatient rehabilitation. Planned610 patients; treatment days1–39; transition to rehabilitation during treatment. All inclusion and none of exclusion criteria required with no exceptions; complete list refers to synopsis outside shard. Prescreening days0–7 since onset. Matching keys: center adjustment/minimization, masking, recruited population,610 target.

### PR4-N004 — Assignment/consent

[Physical p75](../../../joi250066supp1_prod_1761597796.4601.pdf#page=75), §7.3. Consent participant or next-of-kin precedes study-specific procedures and Visit1 inclusion. Randomization instant at inclusion, computer-generated in CDMA; allocation via secuTrial. No emergency inclusion. Travel refund20 CHF/patient/visit for visits outside routine follow-up is administrative, without analysis relevance. Matching key: enrolled/randomized population.

### PR4-N005 — Withdrawal and dosing modification rules

[Physical p75](../../../joi250066supp1_prod_1761597796.4601.pdf#page=75), §7.4. Nighttime adverse reactions allow1-1-0 dose regimen: morning/noon/evening0. Early discharge defined earlier than5 weeks minus7 days after randomization; encourage medication continuation until scheduled5-week Visit2. If participant declines continuation, stop full treatment and taper over following5 days, provide last5-day study drugs. Unscheduled end-study visit at discontinuation/withdrawal ±3 days. If AE/SAE/SUSAR relationship to drug at least probable, reduce dose or discontinue temporarily/permanently as medically appropriate and agreed by patient. Stop study drug if (i) levodopa contraindication develops per appendixIII, (ii) treating physician requires open levodopa, or (iii) treating physician judges significant health risk from continuation. Prefer non-dopaminergic drugs for treatable conditions such as restless legs syndrome before Visit3. Follow-up after treatment or consent withdrawal refers to §9.1.3. Matching keys: adherence/per-protocol criteria, intervention reduction, discontinuation and continued observation.

### PR4-N006 / PR4-S003 — Active and control product, compliance, withdrawn data

[Physical p76](../../../joi250066supp1_prod_1761597796.4601.pdf#page=76), §§8.1–8.5. Active IMP levodopa100mg/carbidopa25mg, oral day1 through39 after Visit1. NG or PEG delivery allowed if unable to swallow capsules, minimize duration and document in medical record/CDMA. Control matching placebo, same administration/duration/phases. Product capsules identical appearance/texture/taste, shelf life expected12 months; room storage15–25°C. Study-site nurses administer during hospitalization; encourage continued medication after early discharge with plan. Capsules numbered for total39 days; returned capsule count at Visit2 documents compliance. Withdrawal-of-consent data collected up to withdrawal will be analyzed. Pregnancy urine/blood test before enrollment for childbearing potential; contraception rule continues next page. Matching keys:100/25mg dose;39-day treatment; adherence and inclusion of pre-withdrawal data.

### PR4-N007 — Concomitant medication categories and restrictions

[Physical p77](../../../joi250066supp1_prod_1761597796.4601.pdf#page=77), §8.6 plus §8.5 continuation. Contraception during days1–39 and one month after, using oral/injectable/implantable or intrauterine contraception. Off-label medical products intended to enhance stroke rehabilitation/recovery prohibited until3-month primary assessment. At each visit eCRF categories: antiplatelets; anticoagulants; antihypertensives; statins; serotonin-reuptake inhibitors; serotonin-noradrenalin reuptake inhibitors; benzodiazepines; neuroleptic drugs; antiepileptic drugs; antidiabetic drugs; analgesics; immunosuppressive/immunomodulating drugs; antibiotics. Mandatory levodopa requires trial-medication discontinuation but participant stays as off-study-medication patient. Interactions refer to appendixIII. Matching key: concomitant treatment policy and retained follow-up after discontinuation.

### PR4-N008 — Rehabilitation intensity and elements

[Physical p77](../../../joi250066supp1_prod_1761597796.4601.pdf#page=77). Same standardized motor-learning rehabilitation across randomized arms. Five elements: (i) active voluntary specific task-related movements rather than passive therapy; (ii) exercises individually adapted and increasingly challenging with improvement; (iii) feedback/knowledge of performance; (iv) repetition with rests; (v) motivation through goal setting, coaching, positive feedback. Three rehabilitative care sessions per workday: physical, occupational, speech/swallowing, neuropsychological if needed. At least two sessions standardized motor rehabilitation by trained physical/occupational therapists. Record each participant's treatment type and minutes/hours. Prefer shorter more frequent sessions in early monitored stroke unit. Matching keys: standardized rehabilitation comparator, therapy dose and adherence.

### PR4-N009 / PR4-S004 — Primary endpoint assessment

[Physical p78](../../../joi250066supp1_prod_1761597796.4601.pdf#page=78), §9.1.1. Primary outcome between-group difference in FMMA scores measured3 months ±14 days after randomization, Visit3. Trained assessors require FMMA training certification; scores entered into CRF. Three-month assessment filmed; video centrally assessed at Basel by blinded assessor. All primary-assessment personnel blinded. Matching key: primary FMMA between-arm difference,3-month timepoint, assessor method.

### PR4-N010 — Secondary and safety assessment windows

[Physical p78](../../../joi250066supp1_prod_1761597796.4601.pdf#page=78), §§9–9.1.2. Blood samples in predefined centers approximately10mL whole blood in EDTA, stored−20°C, for secondary outcomes. Complete secondary outcome/time definitions refer to §5.2 and schedule outside shard. Secondary outcome personnel trained and certified as in9.1.1. During interventional Visits1–3, record all-cause mortality, any recurrent stroke, all SAEs and pre-specified nonserious AEs possibly IMP-related. During observational3–12 months record all-cause mortality and any recurrent stroke. At Visit2 return/count all capsules and enter eCRF. Matching keys: safety denominator/window, mortality/stroke/AE definitions; biomarker secondary status.

### PR4-N011 — Screening and baseline instruments

[Physical p79](../../../joi250066supp1_prod_1761597796.4601.pdf#page=79), §§9.1.3–9.2.2. Data before withdrawal may be used in analyses. Prescreening labelled day−7 to0 before randomization; allow24h latency following thrombolysis/thrombectomy before prescreening/enrollment due to potential early recovery. Meaningful hemiparesis NIHSS≥3 for arm plus leg motor functions. Visit1 day0: written consent, eligibility, demographics/medical history/physical exam/concomitant medication. Mandatory pre-allocation baseline FMMA, NIHSS, mRS, RMI. Selected-center only ARAT, BBT, JDT, MI, TCT, FAC,10MWT, MoCA, daily activity movement sensors. Randomization via eCRF day0; start drug following day1. Matching keys: baseline FMMA adjustment; motor eligibility threshold; selected-center exploratory instruments.

### PR4-N012 — Repeated dosing and short-term windows

[Physical p79](../../../joi250066supp1_prod_1761597796.4601.pdf#page=79), §§9.2.3–9.2.5. Explicit levodopa100mg/carbidopa25mg versus placebo1:1 day1–39; dose schedule same as PR4-N001. Visit2 end-treatment in person5 weeks±7 days after randomization; record concomitant treatment number/length/type and physical examination. Harm: any pre-specified nonserious possible IMP AE or SAE, any recurrent stroke, all-cause death. Count remaining/returned drug capsules in log/eCRF. Visit3 in person3 months±14 days after randomization. Matching keys: randomized intervention,5-week assessment and3-month primary window.

### PR4-N013 — Main follow-up and transition

[Physical p80](../../../joi250066supp1_prod_1761597796.4601.pdf#page=80), §§9.2.5–9.4. Visit3 examination/concomitant medication and post-treatment therapies; nonserious pre-specified possible IMP AE or SAE, stroke and mortality. Visit4 in person6 months±20 days; physical exam, medication/post-treatment therapies, outcomes per schedule, recurrent stroke/all-cause mortality. Visit5 in person12 months±30 days, procedures identical to4. Transition non-in-person assessment documents acute-center therapy number/length/type, drug transfer, harm since randomization including AE/SAE/death/stroke, destination rehabilitation center. Unscheduled end-study visit refers schedule/§7.4. Matching keys: FMMA and secondary outcome follow-up times;3–12-month safety window.

### PR4-N014 / PR4-N015 — Optional ESTREL-LONGTERM

[Physical p80](../../../joi250066supp1_prod_1761597796.4601.pdf#page=80) and [physical p81](../../../joi250066supp1_prod_1761597796.4601.pdf#page=81), §§9.5–9.5.4. Optional extension: annual structured telephone visits for next4 years, new written informed consent after postal contact (short phone contact if no postal response). Visit6 24months±30days; Visit7 36months±30days; Visit8 48months±30days; Visit9 60months±30days post-randomization. Later consent may omit Visit6 in favor of next scheduled Visit7–9. Document medication, recurrent stroke, all-cause mortality. Assess mRS, RMI, FAC, patient-rated improvement, PROMIS-10; no clinical exam. Patient can provide written information or through next-of-kin. Subsequent visits identical to6. Nonanonymized centrally transferred telephone data destroyed at study end. Matching keys: long-term exploratory assessments versus core12-month follow-up.

### PR4-N016 — Interventional safety definitions and complete AE list

[Physical p81](../../../joi250066supp1_prod_1761597796.4601.pdf#page=81), §§10.1–10.1.2. Collect/investigate/document all-cause death, any recurrent stroke, all SAEs and pre-specified nonserious AEs up to3 months Visit3. AE any untoward medical occurrence, not necessarily causal; includes unfavorable/unintended sign or abnormal laboratory result, symptom or disease temporally associated with product. Pre-specified AEs: nausea; vomiting; taste disturbances; dry mouth; anorexia; arrhythmias; postural hypotension; syncope; drowsiness including sudden sleep; fatigue; dementia; psychoses; hallucinations; confusion; euphoria; abnormal dreams; insomnia; depression; anxiety; dizziness; dystonia; dyskinesia; chorea. Syncope description transient unconsciousness from reduced cerebral blood flow; psychoses distorted reality; dystonia involuntary contractions; dyskinesia inability to control voluntary movements; chorea sudden face/shoulder twitching. SAE criteria (each sufficient): death; life-threatening; inpatient hospitalization/prolongation; persistent/significant disability/incapacity; congenital anomaly/birth defect. Further serious medical events continue next page. Matching keys: safety event definitions and pre-specified adverse-event set.

### PR4-N017 — Causality and severity tables

[Physical p82](../../../joi250066supp1_prod_1761597796.4601.pdf#page=82). Important events jeopardizing health or requiring intervention to prevent listed serious outcomes also considered serious. SAEs followed until resolution/stabilization including after trial end for ongoing events. Causality assessed by local investigator and sponsor: Definitely=temporal relation, improvement after dechallenge, recurrence after rechallenge or other proof; Probably=temporal relation, improvement after dechallenge, no other evident cause; Possibly=temporal relation, other possible cause; Unlikely=assessable reaction not fulfilling above; Not related=causality ruled out. Dechallenge improvement considered only if applicable. Unexpected reaction nature/severity inconsistent with product information. SUSAR=related SAE both serious and unexpected. CTCAE Version5,27November2017 grades:1 mild/asymptomatic or mild symptoms, observation only/no intervention;2 moderate/minimal local/noninvasive intervention, limits instrumental ADL;3 severe/medically significant but not immediately life-threatening, hospitalization/prolongation indicated, disabling/limits self-care ADL;4 life-threatening/urgent intervention;5 AE-related death. Semicolon in grade definitions means “or.” Matching keys: safety attribution, severity category and SUSAR.

### PR4-N018 / PR4-N019 — Safety reporting and follow-up

[Physical p82](../../../joi250066supp1_prod_1761597796.4601.pdf#page=82) and [physical p83](../../../joi250066supp1_prod_1761597796.4601.pdf#page=83). SAE sponsor notification immediate/max24h; deaths to CEC/other Swiss committees within7days. SUSAR fatal7days, other15days; report via BASEC and Swissmedic for B/C categories; notify all investigators same timeline. Safety signals sponsor24h; sponsor to CEC/Swissmedic7days and immediate investigator notification. Pregnancy/breastfeeding/lack contraception excluded; pregnant participants immediately withdraw. Pregnancy during treatment or within30days after drug discontinuation reported within24h, follow maternal/child outcome. Annual safety report once yearly. At Visit3 unresolved SAE/nonserious pre-specified possibly related AE followed locally as medically indicated without further EDCS recording; sponsor may request ongoing-event information. Matching key: safety capture window versus post-Visit3 follow-up.

### PR4-N020 — Complete recorded safety variable lists

[Physical p83](../../../joi250066supp1_prod_1761597796.4601.pdf#page=83), §10.1.4. For each nonserious AE of interest and AE leading to drug discontinuation: verbatim description; start/stop date; maximum intensity grade; serious yes/no; investigator study-drug causality yes/no; frequency single/intermittent/continuous; action concerning medication; outcome. Additional SAE variables: verbatim description and evaluation severity/outcome/expectedness; date met serious criteria; date investigator aware; criteria present; hospitalization date; discharge date; probable death cause; death date; autopsy report if performed; autopsy result; study-procedure causality; other-medication causality; concomitant medication/medical history at SAE. Matching key: safety data definitions and drug discontinuation events.

### PR4-N021 — Observational safety and serious event rule

[Physical p84](../../../joi250066supp1_prod_1761597796.4601.pdf#page=84), §10.2. Observational3–12months: all-cause mortality, any recurrent stroke, Serious Events under HRO Art20. Immediate protective-measure notification sponsor24h/ethics7days. HRO Art21 serious event: adverse event not excludable as attributable to biological-material sampling or health-data collection AND (a) unexpected inpatient treatment/prolongation OR (b) permanent/significant incapacity/disability OR (c) life-threatening/death. If occurs, research project interrupted, ethics notified7days. Matching key: safety endpoint definition after3months and interruption rule.

## Statistical design and complete analysis map

### PR4-S005 — Primary hypothesis

[Physical p84](../../../joi250066supp1_prod_1761597796.4601.pdf#page=84), §11.1. Levodopa plus standardized rehabilitation for5 weeks starting soon after acute stroke is superior to placebo plus standardized rehabilitation, yielding at least6-point higher FMMA at3months. No noninferiority/equivalence margin in this shard. Matching key: superiority primary FMMA contrast/timepoint/clinically relevant difference.

### PR4-S006 — All sample-size and power assumptions

[Physical p84](../../../joi250066supp1_prod_1761597796.4601.pdf#page=84), §11.2. Target6-point between-group FMMA difference at3months; two-sample t-test power calculation because uncertain baseline–follow-up correlation prevented estimating baseline-adjustment power gain. Normal FMMA distribution, SD25points; source describes this slightly more conservative than FLAME placebo FMMA35.1,SD22 atday90. Baseline correlation assumed high without reliable numeric input; adjustment expected to increase rather than decrease power. Evaluable sample548 total;1:1 allocation; power80%; two-sided significance5%. Allow10% dropout, recruit305/arm,610 total. Applying placebo mean35.1 gives active expected41.1. DARS has no FMMA information; historical FLAME trial ischemic moderate/severe motor deficit context supplies assumption. These are planning/historical inputs, not ESTREL observed results. Matching key:610 randomized target,6-point difference,SD25,80% power,5% alpha,10% dropout,primary baseline adjustment.

### PR4-N022 / PR4-S007 — Sample-size sensitivity figure and additional power

[Physical p85](../../../joi250066supp1_prod_1761597796.4601.pdf#page=85), Figure3 and §11.2 continuation. Figure title assumedSD25points; x axis assumed treatment difference(points), labelled5,6,7,8,9; y axis sample size ticks200,400,600; three curves power0.7,0.8,0.9. Highlighted power0.8 curve at differenceθ=6 andN=548. Caption curves smoothed for illustration. Novel PROMIS tool intended patient-reported improvement at3months with80% power; less empirical evidence, so primary sample-size calculation uses traditional scores. Walking independent defined RMI≥7, at5weeks. Assume placebo45% walking independently;610 recruitment said sufficient at80% power,5% significance for active57%, absolute12% increase, relative27%. Matching keys: PROMIS secondary assessment/power; RMI independence threshold/time; planning57%vs45%.

### PR4-S008 — Efficacy and safety stopping, composite

[Physical p85](../../../joi250066supp1_prod_1761597796.4601.pdf#page=85), §11.3. No efficacy stopping rule. Safety may terminate per DSMC recommendation. DSMB monitors “primary composite safety events”: (i) death of any cause, (ii) recurrent stroke, (iii) occurrence of SAEs. Composite safety risk alert thresholds to be defined in DSMC charter considering DARS. No numeric threshold printed in shard. Matching keys: safety composite components/status, efficacy/safety stopping/interim decision.

### PR4-S009 — Every analysis population

[Physical p86](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86), §§11.4–11.4.1. Detailed SAP finalized before database closure, version controlled at CTU Basel. Full analysis set(FAS)=all randomized; intention-to-treat, treatment as randomized. Complete-case set=FAS patients without missing baseline or3-month FMMA. Per-protocol(PP)=FAS with ≥80% prescribed levodopa/carbidopa/placebo OR justified reduced dosage per§7.4 (1-1-0/day), plus ≥5rehabilitation sessions/week. All analyzed as randomized. Report withdrawals for each arm and compare qualitatively. Matching keys:all-randomized ITT population; PP medication/rehabilitation thresholds; complete-case FMMA.

### PR4-S010 — Primary model, effects, significance, and timing

[Physical p86](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86), §11.4.2. Primary endpoint FMMA3months after treatment onset. Mixed effects model: baseline FMMA covariate; treatment two-level factor “levodopa” versus “placebo”; index event type acute ischemic versus hemorrhagic stroke, all fixed effects. Random intercept for each center. Analysis after study termination/database closure at CTU Basel according to SAP. Two-sided5% significance. Planned contrast: treatment difference in baseline-adjusted3-month FMMA with center random intercept and stroke type. Matching keys:primary FMMA adjusted between-group effect; model baseline/center/stroke type; two-sidedalpha. The time origin here is recorded as printed (“after onset of treatment”); assessment section9.1.1 separately says after randomization. Mapping records both locations without diagnosis.

### PR4-S011 — Every primary sensitivity/exploratory analysis, covariate, and population

[Physical p86](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86) and [physical p87](../../../joi250066supp1_prod_1761597796.4601.pdf#page=87), §11.4.3. Endpoint FMMA3months.

(a) Explore treatment-effect heterogeneity across centers graphically using center-stratified results.

(b) Repeat main model adding treatment×index-event-type interaction (ischemic versus hemorrhagic).

(c) Exploratory analyses including each listed variable: age; sex; dementia; baseline selective hand/wrist movement; cortical dysfunction (aphasia/neglect/hemianopia); patient-self-reported fatigue; SSRI treatment; mild extrapyramidal motor symptoms by treating physician; reduced mimics by treating physician. Compare results with main analysis.

(d) Repeat main analysis in complete-case set excluding imputed primary outcome or baseline FMMA; compare with main analysis.

(e) Repeat on PP set and compare with main; investigate protocol-deviation influence. For major protocol deviations consider marginal structural models.

Last sentence printed: all analyses except(c) and(d) performed on FAS. This sentence is preserved along with PP specification(e), without harmonization. Matching keys:prespecified subgroup/sensitivity list, interaction model; complete-case and PP comparisons; extra covariate list; protocol-deviation method.

### PR4-S012 — Secondary outcomes and model-specific rules

[Physical p87](../../../joi250066supp1_prod_1761597796.4601.pdf#page=87), §11.4.4. Secondary outcomes use regression appropriate to data type, adjustment as main analysis, including baseline measures where available. Binary: logistic generalized linear model with logit link, binomial distribution. Continuous: linear model. Ordinal: ordinal logistic regression. Inspect models as primary; severe assumption violations/high-leverage outliers allow transformation or other methods including nonparametric tests or robust regression. Each model presents treatment difference, P value,95%CI; two-sided5% significance for all analyses. Summary tables/graphs describe all endpoints. FAS includes all randomized, ITT as assigned. No additional multiplicity adjustment is specified on this page. Matching keys:secondary model types, adjustment,confidence95%,alpha5%,treatment contrasts,reported model implementation.

### PR4-S013 — Exploratory markers/genomics and further analysis

[Physical p87](../../../joi250066supp1_prod_1761597796.4601.pdf#page=87), §11.4.4 continuation. Exploratory genetic/other biomarkers, including routine-care MRI or observational imaging, may influence response. Examples COMT rs4633 exon5,rs4680 exon6; adjustment may reduce variation/increase power. High-density SNP microarrays examine copy-number variation and genomic imbalance relation to stroke outcome. Future individual-participant meta-analysis with similar trials such as DARS intended. Further exploratory analyses may follow clinically relevant study findings. Matching keys:exploratory status of biomarkers/genetic interaction/adjustments; no numeric model coefficient or genetic subgroup threshold prescribed here.

### PR4-S014 — Interim, safety analysis, deviations, reporting

[Physical p87](../../../joi250066supp1_prod_1761597796.4601.pdf#page=87), §§11.4.5–11.4.7. No interim analysis planned. Safety detailed examination of pre-specified events,AEs,SAEs. Estimate proportion with≥1pre-specified adverse event by treatment group. DSMC monitoring refers§1.6. Deviations from statistical plan reported CEC/CA; substantial required deviations lead protocol amendment. All protocol/detailed-SAP analysis deviations listed and justified separately in final statistical report. Matching keys:safety patient proportion numerator,interim plan,disclosed statistical amendments.

### PR4-S015 — Missingness and dropout

[Physical p87](../../../joi250066supp1_prod_1761597796.4601.pdf#page=87), §11.5. Up to10%dropout considered in sample size. Missing data handled using multiple imputation by chained equations (VanBuuren2011), predictive models generate clinically reasonable imputations. Sensitivity complete-case approach assesses impact. No imputation number,model-variable list,or missingness distribution assumption specified on this page; absence is a map limitation of specification, not a finding. Matching keys:MICE primary handling;complete-case sensitivity;dropout allowance.

## Administrative and nonapplicable units

### PR4-N023 — Data integrity procedures

[Physical p88](../../../joi250066supp1_prod_1761597796.4601.pdf#page=88), §12. Records one eCRF/unique identifier per enrolled participant; electronic audit trail. Participant withdrawal reason on eCRF dropout form. Database locked when entry complete, monitoring complete, queries resolved; entire dataset exported/transferred securely to statistician and principal investigator; analysis by independent CTU Basel statistician. All study/source/export data archived≥10years. No efficacy estimate,additional endpoint,model,power,or decision rule here. Matching key:database lock relative to final SAP,withdrawal record.

### PR4-N024 — Secondary biosample status and no additional quantitative rule

[Physical p89](../../../joi250066supp1_prod_1761597796.4601.pdf#page=89), §§12.3–14.1. Secondary genetic/biomarker blood collection at selected centers requires separate consent independent of primary participation. Coded stored locally then centrally Basel. Monitoring frequency/extent in separate monitoring plan. Privacy/publication and Swiss grant33IC30_179667 administrative. No new endpoint contrast,analysis threshold,or result-relevant count. Matching key:selected-center biomarker secondary/exploratory collection.

### PR4-N025 — References and appendix boundaries

[Physical p90](../../../joi250066supp1_prod_1761597796.4601.pdf#page=90): insurance only; no applicable quantitative/statistical relationship.

[Physical p91](../../../joi250066supp1_prod_1761597796.4601.pdf#page=91): references1–24 only; no new trial quantity or prospective design specification.

[Physical p92](../../../joi250066supp1_prod_1761597796.4601.pdf#page=92): reference24 continuation,25–43; no new trial quantity or prospective design specification.

[Physical p93](../../../joi250066supp1_prod_1761597796.4601.pdf#page=93): reference43 continuation,44–66; no new trial quantity or prospective design specification. Product information link and cited measurement studies are references only, not imported evidence.

[Physical p94](../../../joi250066supp1_prod_1761597796.4601.pdf#page=94): references67–79 including MICE citation79; no additional method prescription beyond§11.5. Appendix titles I local principal investigators;II TSC members;III levodopa/carbidopa product characteristics;IV existing levodopa-versus-control stroke studies;V genetic/biomarker analyses. Appendix contents not supplied within these final pages and not inferred. No new secondary definition or model beyond mapped reference/pointer.

## Final shard accounting

22/22 assigned pages visually inspected and mapped. Local relationship records:25 numeric/definition keys(PR4-N001–PR4-N025) and15 statistical/design keys(PR4-S001–PR4-S015); many records preserve multiple related printed statements and lists. Five pages90–94 contain no additional prospective quantitative relationship beyond appendix titles/pointers, explicitly accounted above. Zero fresh source renders;22 bounded fresh CPU OCR text derivatives on reusable images. No scientific coverage gap. Reusable machine-text gap closed by direct page-image inspection. Protocol version/date title is outside assigned scope; coordinator cross-shard confirmation identifies version1.4 dated28.02.2023 at physicalp47 and approval pagep48. This cross-shard identity is not a claim that this mapper opened unassignedp47.

Final derivative check: all22 `page-N.txt` outputs are nonempty; total77554bytes, below the200000-character bound. Page74 was individually retried with the identical single-thread CPU Tesseract command after an empty intermediate derivative was observed; final size3780bytes. Engine log is empty (no engine warnings). No page was omitted for derivative quality.
