# DOC-002 protocol map, shard PR1

## Scope, identity, and extraction provenance

Exact scope: physical PDF pages 1–24 of `joi250066supp1_prod_1761597796.4601.pdf` (DOC-002). Document role throughout: PLAN, determined from prospective clinical-study protocol content. All 24 pages were inspected, including administrative and background content; this artifact makes no candidate or inclusion decisions. No other source pages or old scientific conclusions were used.

Cover p1 and signature p2 identify protocol version 1.1 dated 30 November 2018. The synopsis p7 labels itself version 1.0 dated 2 November 2018. These are location-specific printed version labels; no amendment history is inferred. Links below are physical PDF pages, relative from this extraction artifact to the supplied source.

Reusable locator assets: `.ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc002/page-01.png` through `page-24.png`, unchanged. Current CPU engine Tesseract 5.5.0, English, `--psm 3`; per-page text and OCR log are in `.ai_paper_validation/review_1_6_2/preprocessing/protocol_001/`. Command pattern: `tesseract REUSED_PAGE_IMAGE OWNED/page-NN -l eng --psm 3`. Reusable rendering engine/version not independently established. Native protocol text is unusable, so readable images and their new OCR are used. Source image p9 explicitly governs the symbols ≤7 days and ≥3 points: OCR transcription initially returned `<7` and `>3`. Page13's rotated schedule is mapped visually because its OCR is unusable. One fresh Poppler 26.01.0 CPU render was made for p20's small historical forest plot: `pdftoppm -f 20 -l 20 -r 200 -singlefile -png joi250066supp1_prod_1761597796.4601.pdf .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/page-20-detail`.

No workbook, formula/cached-value source, CSV, or Office unit is in this shard. Values below are printed plan values, not reported ESTREL trial results. Local keys use PR1 prefixes; coordinator may map them into the unified N/S inventory. Main-paper matching keys name outcomes/design concepts without importing main-paper evidence.

## Complete page coverage

| Physical page | Content inspected | Mapping keys / explicit no-applicable record |
|---:|---|---|
| 1 | Protocol cover | PR1-N001: intervention identity, version/date |
| 2 | Signatures | PR1-N001: version/date confirmation; no result or analysis specification |
| 3 | Table of contents | No result-relevant numeric relationship; administrative pointers only |
| 4 | Contents continued | No result-relevant numeric relationship; administrative pointers only |
| 5 | Contents continued | Visit windows listed; PR1-N007; analysis chapter pointers only |
| 6 | Contents continued | No result-relevant numeric relationship; administrative pointers only |
| 7 | Study synopsis identity/background/objective | PR1-N001, PR1-N002; 6 prior RCTs contextual |
| 8 | Synopsis outcomes and design | PR1-N002 through N005; PR1-S001 |
| 9 | Synopsis eligibility, allocation, visits | PR1-N006, N007; PR1-S001 |
| 10 | Synopsis doses, sample size, analyses | PR1-N008, N009; PR1-S002 through S004 |
| 11 | Abbreviations | PR1-N010: analysis-set/scale abbreviations; no operational population definition |
| 12 | Abbreviations continued | PR1-N010; no independent quantitative relationship |
| 13 | Study schedule matrix | PR1-N007, N011; full visual schedule inspection |
| 14 | Study flow chart | PR1-N007, N008; all visit/dosing phases |
| 15 | Administrative structure | No result-relevant numeric relationship; personnel and contact details only |
| 16 | DSMC, TSC, ethics/registration | PR1-S005; drug identity corroboration |
| 17 | Ethics, consent | PR1-N006 consent/aphasia criteria; administrative 15-day/90-day/1-year reporting deadlines do not define trial analyses |
| 18 | Confidentiality, termination, amendments; background start | PR1-S005: permitted early termination, amendment disclosure; no numeric stopping boundary here |
| 19 | Background prior trials and ESTREL rationale | PR1-N012: supplied historical quantitative context; ESTREL early inclusion and tid administration rationale |
| 20 | Background/product and historical meta-analysis figure | PR1-N013, PR1-S006; historical context, not ESTREL outcomes |
| 21 | Dose rationale, placebo, risks/benefits | PR1-N008, N014; adverse-event risk window |
| 22 | Population rationale and objectives | PR1-N002, N006, N015 |
| 23 | Further/safety objectives and primary outcome | PR1-N002, N003, N016, N017 |
| 24 | All-patient secondary outcome definitions | PR1-N018 through N022 |

Mapped units: 24/24. Fresh-required units assigned to this shard: zero (all have reusable images). Scientific gaps: none within assigned pages. Detailed statistical chapter and subsequent outcome pages are outside this shard and must be mapped by other assignments. The RMI paragraph continues on p25, outside this shard; no continuation is invented here.

## Planned trial relationships

### PR1-N001 — Identity, version, drug

[pp1–2](../../../joi250066supp1_prod_1761597796.4601.pdf#page=1), [p7](../../../joi250066supp1_prod_1761597796.4601.pdf#page=7). ESTREL = Enhancement of Stroke Rehabilitation with Levodopa, randomized placebo-controlled clinical study protocol; phase III, risk category C. Cover/signature: 1.1, 30.11.2018; synopsis: 1.0, 02.11.2018. Product levodopa/carbidopa 100/25 mg; placebo comparator. Registration identifiers remain prospective placeholders on these pages. Matching key: ESTREL intervention/protocol identity.

### PR1-N002 — Primary objective and outcome/time origin

[p7](../../../joi250066supp1_prod_1761597796.4601.pdf#page=7), [p8](../../../joi250066supp1_prod_1761597796.4601.pdf#page=8), [p22](../../../joi250066supp1_prod_1761597796.4601.pdf#page=22), [p23](../../../joi250066supp1_prod_1761597796.4601.pdf#page=23). Patient-relevant enhancement of functional recovery after acute ischemic stroke, comparing levodopa with placebo added to standardized rehabilitation based on motor-learning principles. Primary outcome is between-group difference of final FMMA total scores measured 3 months after randomization. It is a score difference, with no composite components. Primary objective p22 says difference of final scores; p23 calls it the primary efficacy outcome. Background p20 describes the primary time point as 3 months post-stroke; this is separately preserved as background wording, without resolving or diagnosing the comparison. Matching key: primary 3-month FMMA total.

### PR1-N003 — FMMA measurement scale and clinically relevant target

[p23](../../../joi250066supp1_prod_1761597796.4601.pdf#page=23). Each scale item: ordinal 0 cannot perform, 1 partially performs, 2 fully performs. Total range 0–100, where 0 denotes no movements and 100 normal movements; upper limb component 66 points, lower limb 34 points. Trained outcome assessor performs all assessments. Cited minimum clinically important differences: 5.25 upper-extremity points and 6 lower-extremity points. ESTREL treats 6 total FMMA points between groups as patient-relevant for the primary endpoint. Matching keys: total/upper/lower FMMA; patient-relevant 6-point difference.

### PR1-N004 — Secondary outcomes in all patients (synopsis)

[p8](../../../joi250066supp1_prod_1761597796.4601.pdf#page=8). Status is explicitly secondary for each item below:

| Outcome | Contrast/measure | Scheduled times after randomization |
|---|---|---|
| FMMA total | Between-group score difference | 5 weeks (end of treatment), 6 months, 12 months |
| FMMA upper extremity | Between-group score difference | 5 weeks, 3, 6, 12 months |
| FMMA lower extremity | Between-group score difference | 5 weeks, 3, 6, 12 months |
| NIH Stroke Scale | Between-group score difference | 5 weeks, 3, 6, 12 months |
| Modified Rankin Scale | Between-group difference | 5 weeks, 3, 6, 12 months |
| PROMIS-10 | Between-group difference in patient-reported outcome | 5 weeks, 3, 6, 12 months |
| PROMIS-29 | Between-group difference in patient-reported outcome | 5 weeks, 3, 6, 12 months |
| Patient-reported relevance of motor improvement | Between-group difference | 5 weeks, 3, 6, 12 months |
| Rivermead Mobility Index | Between-group score difference | 5 weeks, 3, 6, 12 months |
| Mortality | Relative risk | No specific window in this synopsis row |
| Recurrent stroke | Relative risk | No specific window in this synopsis row |
| Rehospitalization | Relative risk | No specific window in this synopsis row |
| Serious adverse events | Relative risk | No specific window in this synopsis row |
| Selected other adverse events possibly related to IMP | Relative risk | No specific window in this synopsis row |

Matching keys: named outcomes and follow-up times; preserve outcome status independently of any later SAP/report status.

### PR1-N005 — Secondary outcomes in selected-center subsets (synopsis)

[p8](../../../joi250066supp1_prod_1761597796.4601.pdf#page=8). Each is explicitly a between-group difference in a subset of patients in selected centers, at 5 weeks, 3, 6, and 12 months: Action Research Arm Test; Box-and-Block Test; Jamar dynamometer; Motricity Index; Trunk Control Test; Functional Ambulation Categories; 10-meter walk test; Montreal Cognitive Assessment; daily-life activities measured with movement sensors. Matching keys: each named test; subset versus all-patient analysis.

### PR1-N006 — Eligibility criteria, item-by-item

[p9](../../../joi250066supp1_prod_1761597796.4601.pdf#page=9), with consent/aphasia elaboration [p17](../../../joi250066supp1_prod_1761597796.4601.pdf#page=17) and population rationale [p22](../../../joi250066supp1_prod_1761597796.4601.pdf#page=22).

Inclusion: (1) acute ischemic stroke ≤7 days before randomization; (2) clinically meaningful hemiparesis, defined as ≥3 points on arm plus leg motor NIHSS items; (3) 24-hour latency after thrombolysis or thrombectomy; (4) inpatient rehabilitation required; (5) capability to participate in standardized rehabilitation; (6) informed consent from patient or next of kin.

Exclusion: (1) age <18 years; (2) Parkinson disease; (3) levodopa mandatory in treating physician's judgment; (4) inability/unwillingness to comply with procedures or drug intake orally, through nasogastric tube, or through percutaneous endoscopic gastrostomy; (5) severe aphasia, unable to follow two-stage commands; (6) prior dependence in basic daily activities, prestroke mRS >3; (7) pre-existing hemiparesis; (8) known levodopa/carbidopa hypersensitivity or other contraindications according to the supplied protocol's Swiss product-information pointer; (9) pregnancy, breast-feeding, intent to become pregnant; childbearing-age women require pregnancy testing; (10) lack of safe contraception throughout study duration. Acceptable methods include oral/injectable/implantable contraception, intrauterine devices, or another method individually judged sufficiently reliable. Surgical sterilization/hysterectomy or menopause >2 years removes childbearing-potential classification.

P17: no emergency inclusion; next-of-kin consent for impaired understanding requires additional independent-physician consent, with deferred participant consent as soon as possible at follow-up. P22 excludes hemorrhagic stroke, repeats ≥3 motor NIHSS points and inpatient rehabilitation, and sets maximum stroke-to-Visit1 window to 7 days. It distinguishes inability to follow commands from inability to understand consent despite capability to undertake procedures. Matching keys: recruited/analysis-population eligibility, ischemic-stroke-only population, severity threshold, prestroke independence.

### PR1-S001 — Design, allocation, blinding

[pp8–9](../../../joi250066supp1_prod_1761597796.4601.pdf#page=8). Multicenter randomized parallel-group placebo-controlled superiority trial; allocation ratio 1:1; center stratification using a standard minimization algorithm. Randomization/enrollment takes place in acute care. Patients, care providers, investigators, outcome assessors, and all study personnel blinded. Participants transition to rehabilitation centers during treatment. No operational randomization algorithm probabilities or analysis-set eligibility are specified here. Matching key: randomization design and allocation strata.

### PR1-N007 — Visit windows, timing, study flow

[p5](../../../joi250066supp1_prod_1761597796.4601.pdf#page=5), [pp9–10](../../../joi250066supp1_prod_1761597796.4601.pdf#page=9), [p13](../../../joi250066supp1_prod_1761597796.4601.pdf#page=13), [p14](../../../joi250066supp1_prod_1761597796.4601.pdf#page=14). Prescreening day −7 to 0; Visit1 screening/consent/enrollment/randomization day0. Medication starts day after randomization. Dose escalation day1–6, full dosage day7–34, taper day35–39. Visit2 5 weeks ±7 days, end of treatment. Visit3 primary outcome 3 months ±14 days. Visit4 long-term follow-up 6 months ±20 days. Visit5 long-term follow-up 12 months ±30 days. Interventional/main-study phase extends through Visit3; observational phase contains Visits4/5. Transition from acute to rehabilitation center is day x during treatment. Unscheduled end-of-study visit allowed at discontinuation/consent withdrawal; outcome assessment performed with participant approval. Matching key: all outcome assessment windows and time origin.

### PR1-N008 — Randomized intervention dose/duration and taper

[p10](../../../joi250066supp1_prod_1761597796.4601.pdf#page=10), [p14](../../../joi250066supp1_prod_1761597796.4601.pdf#page=14), [p20](../../../joi250066supp1_prod_1761597796.4601.pdf#page=20), [p21](../../../joi250066supp1_prod_1761597796.4601.pdf#page=21). White capsules contain levodopa100 mg/carbidopa25 mg, or matching placebo; all receive standardized rehabilitative therapy. Total planned administration 39 days. Day1–3 morning only; day4–6 morning and lunchtime; day7–34 three times daily; day35–37 morning and lunchtime; day38–39 morning only. Full dosage therefore supplies 300/75 mg per day (arithmetic description, not an additional printed prescription). P21 says fixed escalation because immediate treatment response is not expected, monitor tolerability, dose adaptations allowed if required, and taper carefully over 5 days for safety. Placebo is identical in appearance, texture, and taste. Matching key: randomized treatment dose, 39-day course, dose escalation/taper.

### PR1-N009 / PR1-S002 — Planned sample size and power inputs

[p10](../../../joi250066supp1_prod_1761597796.4601.pdf#page=10). Planned enrollment 610 over 37 months; assumed dropout10%, leaving549 evaluable. FMMA normally distributed, SD25 points;548 patients permit detection of a6-point mean levodopa–control difference at3 months,80% power, two-sided significance5%. Preserve both printed549 evaluable and548 power-analysis patients without silently merging them. Overall study duration50 months; planned first participant02-2019 and last participant out12-2022. Anticipated12 acute and7 rehabilitation centers are administrative context. Matching key: sample-size assumptions, target effect, type-I level, power.

### PR1-S003 — Synopsis primary and secondary analyses

[p10](../../../joi250066supp1_prod_1761597796.4601.pdf#page=10). Primary dependent variable FMMA at3 months. Mixed-effects model: baseline FMMA covariate and two-level treatment factor (levodopa versus placebo) as fixed effects; center as random factor. Secondary outcomes use regression models appropriate to data type. No further covariates, interaction terms, subgroup specifications, estimand, confidence level, or multiplicity hierarchy appear in this synopsis. Matching key: adjusted primary model and center handling.

### PR1-S004 — Missing-data plan

[p10](../../../joi250066supp1_prod_1761597796.4601.pdf#page=10). Missing data addressed using multiple imputation by chained equations. No imputation count, predictor set, pooling formula, death handling, or missingness assumption is supplied in these assigned pages. Their absence is a mapping fact, not an issue diagnosis. Matching key: primary missing-data handling.

### PR1-N010 — Analysis/scale abbreviations without definitions

[pp11–12](../../../joi250066supp1_prod_1761597796.4601.pdf#page=11). FAS = full analysis set; ITT = intention to treat; PP = per protocol; FMMA(UE/LE) = Fugl-Meyer Motor Assessment upper/lower extremity; NIHSS; mRS; PROMIS; RMI; ARAT; BBT; JDT; MI; MoCA; FAC; TCT;10MWT. No operational FAS/ITT/PP success/exclusion criteria in assigned pages; detailed population definitions must come from later source units. Matching key: analysis-set identity.

### PR1-N011 — Schedule matrix and footnotes

[p13](../../../joi250066supp1_prod_1761597796.4601.pdf#page=13). Schedule groups: prescreening; enrollment Visit1; interventional/main-study escalation, transition, full-dose, taper, Visits2/3; observational Visits4/5; unscheduled end-of-study. Assessments include eligibility, demographics, medical history, female pregnancy test, baseline concomitant rehabilitation, subsequent rehabilitation information, concomitant treatment, drug accountability, and optional blood sampling. Outcome rows explicitly list FMMA primary, NIHSS, mRS, PROMIS10, PROMIS29, patient relevance of motor improvement, RMI, ARAT, BBT, Jamar dynamometer, Motricity Index, trunk control, FAC,10-meter walk, MoCA, daily-life movement sensors, clinical stroke recurrence, all-cause mortality, and AE/SAE. Follow-up outcome columns show assessment at5 weeks,3,6,12 months and at the unscheduled visit. Footnotes: transition data collected only on the acute-to-rehabilitation transfer day; double-asterisk tests/sensors and blood sampling only in selected centers; blood sampling may occur at baseline or any follow-up; unscheduled visit for discontinuation/withdrawal; bracketed drug-accountability assessment applies only before end of treatment or before Visit3 for AE/SAE; outcome assessments at unscheduled visit require participant approval. No numerical result is printed in the matrix. Matching key: all-patient versus selected-center tests, follow-up timing, safety collection.

### PR1-S005 — Monitoring and early stopping

[p16](../../../joi250066supp1_prod_1761597796.4601.pdf#page=16), [p18](../../../joi250066supp1_prod_1761597796.4601.pdf#page=18). Independent DSMC monitors mortality, recurrent stroke, SAEs; an independent statistician supplies individual-treatment-unblinded safety data. Investigators, CTU study-conduct staff and trial statistician remain blinded to safety-monitoring data/analyses. DSMC does not review/evaluate efficacy data. It recommends stopping/continuing/amending according to section11.3 (outside assigned scope). P18 permits early termination for ethical concerns, insufficient recruitment, safety risk, changes in accepted practice, or early evidence of harm; no numeric threshold on these pages. Substantial amendments require CEC/competent-authority approval, with documented emergency deviations to protect participants and reporting afterward; non-substantial amendments communicated through annual safety reporting. Matching key: safety interim analyses and early-stopping decision rule.

### PR1-N014 — Dose/risk-window rationale

[p21](../../../joi250066supp1_prod_1761597796.4601.pdf#page=21), [p22](../../../joi250066supp1_prod_1761597796.4601.pdf#page=22). Expected peak levodopa effect0.5–2 hours after oral dose; prior studies administered single dose at least30 or45–60 minutes before therapy, with0–15 minutes acceptable in one protocol. Historical100 mg single dose chosen against25/200 mg alternatives, with3 dose levels discussed. Potential treatment AEs expected during5-week treatment or maximum7 weeks thereafter, within3 months after randomization; no IMP treatment effects expected in observational3–12-month phase after washout. These are rationale statements, not observed ESTREL safety outcomes. Matching key: planned safety observation window.

### PR1-N015 — Secondary objectives

[pp22–23](../../../joi250066supp1_prod_1761597796.4601.pdf#page=22). Secondary objectives: improved self-assessed physical function; improved general health, pain, mood, anxiety, fatigue, social participation; sustained motor-function improvement; selective hand/wrist movement; higher proportion walking without another person's assistance; less severe impairment; greater daily-living activity; quality-of-life improvement; cognitive performance; no increased all-cause mortality, recurrent stroke, or SAEs. Each is prospectively secondary; no subgroup hypothesis or multiplicity ranking here. Matching keys: outcome hierarchy/status.

### PR1-N016 — Further objectives

[p23](../../../joi250066supp1_prod_1761597796.4601.pdf#page=23). Further objective(a): compare3-month functional outcome of ESTREL participants with nonparticipants using Swiss Stroke Registry routine data. Further objective(b): collect genetic/other biomarkers and routine/observational brain imaging (CT,MRI,fMRI) to explain treatment response. No numerical model specified. Matching keys: external registry comparison and exploratory biomarker analysis, preserving further-objective status.

### PR1-N017 — Safety objectives

[p23](../../../joi250066supp1_prod_1761597796.4601.pdf#page=23). Compare occurrence of mortality, recurrent stroke, SAEs, and prespecified non-serious possibly IMP-related AEs between groups (definition points to10.1.1 outside this shard). No safety composite is stated here. Matching keys: individual safety outcomes and prespecified non-serious AEs.

### PR1-N018 — NIHSS and mRS definitions/status

[p24](../../../joi250066supp1_prod_1761597796.4601.pdf#page=24). All-patient secondary NIHSS measures overall clinical deficit in acute phase/follow-up. All-patient secondary mRS measures activity-level outcome at3 months; simplified mRS questionnaire permitted.3-month mRS in Swiss Stroke Registry supports external nonparticipant comparison. No mRS dichotomization threshold or score distribution model specified here. Matching keys: NIHSS/mRS analysis, independent walking/activity outcomes.

### PR1-N019 — PROMIS scoring/statistical definition

[p24](../../../joi250066supp1_prod_1761597796.4601.pdf#page=24). PROMIS based on item-response theory; each scale general-population mean50, SD10; minimal clinically important difference deemed one-half SD (5 points by arithmetic). These are scale reference values, not trial summaries. Matching keys: PROMIS T-score scale and clinically important threshold.

### PR1-N020 — PROMIS-29 domains and item scales

[p24](../../../joi250066supp1_prod_1761597796.4601.pdf#page=24). All-patient secondary PROMIS29 covers(1) physical function,(2) anxiety,(3) depression,(4) fatigue,(5) sleep disturbance,(6) ability to participate in social roles/activities,(7) pain interference,(8) pain intensity. Domains1–7 each4 questions, scored at1 of5 levels. Pain-intensity visual analogue scale0–10. Matching keys: seven PROMIS29 scales and pain-intensity outcome; scale direction not supplied here.

### PR1-N021 — PROMIS-10 and patient relevance of improvement

[p24](../../../joi250066supp1_prod_1761597796.4601.pdf#page=24). PROMIS10 addresses general health, quality of life, pain, mood, anxiety, fatigue, social participation. Patient relevance asks whether motor function improved since preceding study visit and, if yes, whether improvement matters in personal perception. Compare improvement in FMMA with patient-reported relevance. No respondent threshold or binary-event estimator specified here. Matching keys: PROMIS10 outcomes; patient-reported motor improvement and relevance.

### PR1-N022 — Rivermead Mobility Index definition

[p24](../../../joi250066supp1_prod_1761597796.4601.pdf#page=24). RMI all-patient secondary activity measure,15 items (bed movement, transfer, walking, stairs),0–15 points. Both clinician and patient perspectives described. Historical minimal detectable change2.2 points; clinically meaningful difference not established. RMI≥7 denotes ability to walk inside with an aid without assistance. This paragraph introduces DARS primary independent-walking outcome and continues on p25, requiring the next shard. Matching keys: RMI score and walking-independence threshold.

## Supplied historical context (not ESTREL trial results)

### PR1-N012 — Earlier studies and design rationale

[p19](../../../joi250066supp1_prod_1761597796.4601.pdf#page=19). Initial trial: stroke3 weeks–6 months earlier,100 mg levodopa/day for3 weeks,47 analyzed; Rivermead motor assessment difference3.9,95%CI0.55–7.2; sustained3 weeks after stopping. Two subsequent factorial RCTs included29 levodopa-treated total. Aphasia study:100 mg/day eight weeks after stroke. DARS:100 mg before therapy, independent walking at8 weeks,OR0.78,95%CI0.53–1.1;22(SD10) sessions during6 weeks (<3/week); comparator guideline3h/weekday; drug45–60 minutes before therapy,0–15 acceptable; expected50% relative increase in walking independently8 weeks after randomization. ESTREL rationale: tid administration, motor-learning-based standardized therapy, include as early as possible but≤7 days after stroke. These historical numbers have no ESTREL trial numerator/denominator role.

### PR1-N013 / PR1-S006 — Figure1 historical meta-analysis

[p20](../../../joi250066supp1_prod_1761597796.4601.pdf#page=20). Supplied figure titled meta-analysis of levodopa and motor recovery;6 RCTs,8 study/subgroup rows. Contrast levodopa versus control, standardized mean difference, inverse variance random effects,95%CI. Forest axis −2,−1,0,1,2; negative favors control, positive levodopa. Printed row values below were read from source render:

| Study/subgroup | Levodopa mean, SD, n | Control mean, SD, n | Weight | SMD [95% CI] | Year |
|---|---|---|---:|---|---:|
| Celik2004 | 9.1,4.5,14 | 7.3,4.5,12 |12.1%|0.39[−0.39,1.17]|2004|
| Acler2005 |23,6,10|22,6,10|10.7%|0.16[−0.72,1.04]|2005|
| Scheidtmann2005 |15.4,3.48,22|11.3,3.48,25|14.5%|1.16[0.54,1.78]|2005|
| Sonde2007 with AMPH |22.6,7.8,3|37.9,23.7,5|5.3%|−0.67[−2.17,0.83]|2007|
| Sonde2007 without AMPH |25.9,10.6,6|39.4,9.1,7|7.1%|−1.28[−2.52,−0.04]|2007|
| Lokk2011 without MPH |66.3,31.7,20|53.4,34.4,20|14.4%|0.38[−0.24,1.01]|2011|
| Lokk2011 with MPH |57.7,37.1,19|57,35.3,19|14.3%|0.02[−0.62,0.65]|2011|
| DARS2015 |3.1,3.1,308|3.3,3,295|21.7%|−0.07[−0.23,0.09]|2015|
| Total |n402|n393|100.0%|0.15[−0.25,0.55]|—|

Heterogeneity tau²0.18,chi²21.20,df7,P=.003,I²67%; overall effect Z0.73,P=.46. Caption: Celik Rivermead change from baseline at6 weeks; Acler/Scheidtmann Rivermead at5/6 weeks; Sonde FM leg+arm at3 months, leg used in figure; Lokk FM3 months; DARS ABILHAND8 weeks. Sensitivity exclusion of Celik or Sonde arm-score substitution described as consistent and not explaining heterogeneity; no numerical sensitivity result printed. AMPH=amphetamine; MPH=methylphenidate. Search date17 August2017. These remain supplied background plan context; do not treat them as reported ESTREL endpoints or population totals.

### PR1-N023 — Historical safety context

[p21](../../../joi250066supp1_prod_1761597796.4601.pdf#page=21). DARS mean SAEs per patient1.2(SD0.6) within8 weeks; no between-group difference stated. Associated levodopa/carbidopa AEs named dyskinesia,nausea,dizziness,headache. This informs predefined ESTREL AE monitoring but is not an ESTREL safety result.

## Handoff and limitations

Complete disjoint coverage24/24 pages. Numeric/design keys PR1-N001 through PR1-N023 (23); statistical keys PR1-S001 through PR1-S006 (6), with N009/S002 and N013/S006 intentionally cross-referenced rather than duplicated. No observed ESTREL results, workbook formulas, cached values, or computed result outputs occur in this shard. Explicitly preserved primary/secondary/further/safety statuses, every listed outcome, timing, scale, dose phase, eligibility item, and available sample-size/model/missing-data/monitoring statements. Detailed analysis populations, sensitivity/subgroup analysis methods, multiplicity, exact stopping boundaries and later outcome definitions occur outside assigned scope; no unsupported specification is inferred.

Derivative completion note: OCR texts exist for all24 pages, total62039 bytes, below the200000-character shard bound. The initial sequential `--psm 3` batch ended with exit143 after completing p20 and starting p21; p21–24 were subsequently produced successfully using `OMP_THREAD_LIMIT=1 timeout 45s tesseract REUSED_PAGE_IMAGE OWNED/page-NN -l eng --psm 6`. They had already been mapped visually before the successful rerun. P13 OCR remains unreadable because of page rotation, and p20 OCR's small forest-plot cells are garbled; their image-based mappings above govern. Fresh renders1 (p20), reusable page-image scope24, no fresh OCR engine or GPU. No scientific unit remains unmapped.
