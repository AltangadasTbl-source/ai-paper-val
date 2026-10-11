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
# Support protocol mapping shard PR3

Scope: DOC-002, `joi250066supp1_prod_1761597796.4601.pdf`, physical PDF pages 49–72, exactly 24 units. Document role: PLAN throughout. Protocol version 1.4, 28 February 2023, explicitly printed on physical page 53 (synopsis). Protocol internal page numbers are physical PDF page minus 46 in this version (for example, physical page 69 corresponds to protocol page 23). Physical PDF locations govern links. No previous conclusions were read; no candidates are diagnosed here.

All 24 reusable page images were opened and read visually. Their paths are `.ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc002/page-N.png`, N = 49 through 72. They are source-linked rendered-page aids; exact supplied PDF is the final evidence authority. No additional rendering was needed. CPU OCR: Tesseract 5.5.0, English. Initial command per page: `tesseract REUSED_IMAGE preprocessing/protocol_003/page-N -l eng --psm 3`; rerun with `OMP_THREAD_LIMIT=1 tesseract REUSED_IMAGE preprocessing/protocol_003/page-N-fast -l eng --psm 6`. All output paths in those commands are under `.ai_paper_validation/review_1_6_2/`. Logs have corresponding `.log` suffixes. PSM 6 OCR is a locator/transcription aid, especially limited for the sideways schedule on p59; the visual table is mapped below. No source or reused artifact was changed. No fresh-required units in this scope; readable reusable images cover all 24 pages. Native text was designated unusable by the curator. No workbook formulas, cached values, or structured cells exist in the assigned PDF units.

## Page-complete evidence inventory

Each PR3 key below is a local mapping key, not a candidate ID. Matching main-paper keys are semantic labels for coordinator reconciliation, without reading main-paper units outside this disjoint assignment.

| Key | Exact source location | Content and quantitative/design relationship | Matching result or design key |
|---|---|---|---|
| PR3-001 | [PDF p49](../../../joi250066supp1_prod_1761597796.4601.pdf#page=49) | Local investigator protocol-agreement signature page; Prof. Philippe Lyrer, University Hospital Basel. No applicable quantitative result, statistical specification, endpoint definition, or population count. | Administrative, no applicable result |
| PR3-002 | [PDF p50](../../../joi250066supp1_prod_1761597796.4601.pdf#page=50) | Table of contents: synopsis internal p7; abbreviations p11; administration p15; ethics p16; background p18; objectives p22; outcomes p23; selected-center secondary assessments p25; further assessments p26. Locator content only, no independent quantitative analysis. | Version 1.4 locator |
| PR3-003 | [PDF p51](../../../joi250066supp1_prod_1761597796.4601.pdf#page=51) | Continued contents: treatment day1–39; Visit2 5 weeks ±7 days; Visit3 3 months ±14 days; Visit4 6 months ±20 days; Visit5 12 months ±30 days; optional Visits6–9 at 24,36,48,60 months each ±30 days. These point to full specifications. | Visit windows/intervention duration |
| PR3-004 | [PDF p52](../../../joi250066supp1_prod_1761597796.4601.pdf#page=52) | Contents: statistical methods internal p38; sample size p38; statistical termination criteria p39; analysis populations, primary analysis and sensitivity analysis p40; secondary/interim/safety analyses and missing data p41. These sections are outside this shard; contents do not establish their detailed specification. | Statistical-section locators |
| PR3-005 | [PDF p53](../../../joi250066supp1_prod_1761597796.4601.pdf#page=53) | Synopsis establishes version1.4, 28.02.2023; ESTREL; NCT03735901; Phase III; category C. Primary objective is patient-relevant functional recovery with levodopa versus placebo added to standardized rehabilitation based on motor-learning principles. Background mentions a meta-analysis of 6 RCTs; historical context only. | Protocol version; treatment objective |
| PR3-006 | [PDF p54](../../../joi250066supp1_prod_1761597796.4601.pdf#page=54) | Primary outcome: between-group FMMA score difference measured 3 months after randomization. Secondary endpoint list and trial design are transcribed item by item below. Multicenter randomized 1:1 parallel-group placebo-controlled superiority trial; patients, care-providers, investigators, assessors blinded. | Primary FMMA; secondary outcome status; design |
| PR3-007 | [PDF p55](../../../joi250066supp1_prod_1761597796.4601.pdf#page=55) | Six inclusion and ten exclusion criteria, detailed below. Randomization 1:1, stratified by center, standard minimization algorithm. Levodopa100mg/carbidopa25mg three times daily versus matching placebo, both with standardized rehabilitation. All participants/personnel blinded; treatment starts the day after randomization, escalation/full-dose/tapering phases. In-person assessments at5 weeks and3 months; observational follow-up6/12 months; optional annual telephone visits for4 additional years. | Eligibility; minimization; intervention; follow-up |
| PR3-008 | [PDF p56](../../../joi250066supp1_prod_1761597796.4601.pdf#page=56) | Treatment39 days; dose schedule, sample-size/power assumptions, planned calendars, center numbers, primary model and missing-data specification, transcribed below. | Dosing; sample size; mixed model; imputation |
| PR3-009 | [PDF p57](../../../joi250066supp1_prod_1761597796.4601.pdf#page=57) | Definitions: FAS=full analysis set; ITT=intention to treat; PP=per protocol; FMMA(UE/LE)=Fugl-Meyer Motor Assessment upper/lower extremity; NIHSS, mRS, PROMIS, ARAT, BBT, FAC, JDT, MI, MoCA. Abbreviations provide no inclusion/exclusion rule for the analysis sets. | Scale/analysis-set labels |
| PR3-010 | [PDF p58](../../../joi250066supp1_prod_1761597796.4601.pdf#page=58) | Remaining abbreviations: RMI=Rivermead Mobility Index; SAE=serious adverse event; SD=standard deviation; TCT=Trunk Control Test; 10MWT=10-meter-walk-test; other administrative abbreviations. No independent quantitative relationship. | Secondary-scale labels |
| PR3-011 | [PDF p59](../../../joi250066supp1_prod_1761597796.4601.pdf#page=59) | Complete sideways study schedule, visually read, with rows, timepoints, optional assessments and discontinuation footnotes mapped below. No observed participant counts. | Outcome timing; extended observation; safety windows |
| PR3-012 | [PDF p60](../../../joi250066supp1_prod_1761597796.4601.pdf#page=60) | Flow chart: prescreening day−7 to0; consent/screening/baseline/randomization; levodopa/carbidopa versus matching placebo1:1; escalation day1–6, full-dose day7–34, taper day35–39; transfer to rehabilitation center any treatment-phase day x; Visits2–9 timing as below. Primary assessment explicitly Visit3. | Design/primary timepoint/duration |
| PR3-013 | [PDF p61](../../../joi250066supp1_prod_1761597796.4601.pdf#page=61) | Sponsor, investigator, statistician, supplier and monitoring contacts. No applicable quantitative result or statistical decision specification. | Administrative, no applicable result |
| PR3-014 | [PDF p62](../../../joi250066supp1_prod_1761597796.4601.pdf#page=62) | Independent DSMC monitors mortality, recurrent stroke, SAEs; independent statistician supplies data unblinded to individual treatment; investigators and CTU trial statistician remain blinded to safety data/analyses. Efficacy evaluation outside DSMC scope. Stopping/continuing/amending recommendations refer to11.3; no numeric boundary on this page. Registration and category C repeat. | Safety monitoring; efficacy-interim scope |
| PR3-015 | [PDF p63](../../../joi250066supp1_prod_1761597796.4601.pdf#page=63) | Administrative reporting: premature end/interruption reported within15 days; regular end within90 days; final report within1 year. Consent requires no emergency inclusion; severe sensory aphasia unable to follow two-stage commands excluded; next-of-kin consent possible where participant cannot understand contents; consent precedes any procedure. No applicable result count or statistical decision boundary. | Eligibility/consent; administrative deadlines |
| PR3-016 | [PDF p64](../../../joi250066supp1_prod_1761597796.4601.pdf#page=64) | Early termination circumstances: ethical concerns; insufficient recruitment; participant safety doubtful/at risk; changed accepted clinical practice; early evidence of experimental-treatment harm. Safety stopping refers to mortality/recurrent stroke/SAE monitoring and11.3. Amendment approval and emergency exceptions; no numeric decision threshold printed. Background begins. | Safety stopping/amendment context |
| PR3-017 | [PDF p65](../../../joi250066supp1_prod_1761597796.4601.pdf#page=65) | Background prior-trial quantities, listed below, plus ESTREL rationale: three daily doses; standardized motor-learning rehabilitation; inclusion≤7 days poststroke; primary FMMA measurement described here as3 months poststroke. This preserves the time origin as printed without converting to randomization time. | Intervention; timing wording |
| PR3-018 | [PDF p66](../../../joi250066supp1_prod_1761597796.4601.pdf#page=66) | White capsules levodopa100mg/carbidopa25mg or placebo; historical 6-RCT meta-analysis with8 subgroup rows, detailed below; sensitivity analyses in its caption are historical meta-analysis methods, not ESTREL prespecified analyses. | Dose; background meta-analysis |
| PR3-019 | [PDF p67](../../../joi250066supp1_prod_1761597796.4601.pdf#page=67) | Dose rationale:100/25mg TID; escalation days1–6; taper days35–39 over5 days; dose adaptation allowed under7.4. Prior-dose/timing rationale recorded below. Prespecified intervention-related AE examples dyskinesia,nausea,dizziness,headache; expected harm within5-week treatment or≤7 subsequent weeks, within3 months after randomization; no IMP AE expected in3–12-month observational phase. | Dose modification; safety assessment timeframe |
| PR3-020 | [PDF p68](../../../joi250066supp1_prod_1761597796.4601.pdf#page=68) | Population: acute ischemic/intracerebral hemorrhagic stroke, NIH motor arm/leg/ataxia total≥3, in-hospital rehabilitation; severe aphasia unable to follow2-stage commands excluded; proxy consent for those capable of procedures but unable to comprehend full information; maximum stroke-onset-to-Visit1 window7 days. Primary objective: between-group final FMMA scores3 months after randomization. Secondary objectives a–g continue next page. | Population; primary final-score contrast; secondary aims |
| PR3-021 | [PDF p69](../../../joi250066supp1_prod_1761597796.4601.pdf#page=69) | Secondary aims h–j; further objectives and safety objectives; FMMA definition and patient-relevant threshold below. Primary efficacy endpoint is between-group score difference3 months after randomization. Secondary assessments may be limited to selected centers to reduce burden. | Outcome status; FMMA scale/threshold |
| PR3-022 | [PDF p70](../../../joi250066supp1_prod_1761597796.4601.pdf#page=70) | All-patient secondary assessments NIHSS,mRS,PROMIS29/PROMIS10,patient relevance of motor improvement,RMI; PROMIS and RMI scale definitions below. No effect estimates from ESTREL. | Secondary outcomes/scoring/independent walking |
| PR3-023 | [PDF p71](../../../joi250066supp1_prod_1761597796.4601.pdf#page=71) | Interventional safety outcomes and observational mortality/stroke; selected-center secondary scales MI,TCT,ARAT,BBT,FAC,10MWT,JDT,MoCA,sensor activity, with definitions below. | Safety outcomes; selected-center secondary outcomes |
| PR3-024 | [PDF p72](../../../joi250066supp1_prod_1761597796.4601.pdf#page=72) | Sensor measures continued; further selected-center genetic/blood/imaging biomarker assessment explicitly exploratory; no within-trial imaging. Safety outcome section refers to5.2.1. Design: randomized1:1 superiority with blinded groups; hypothesis levodopa plus standardized rehabilitation gives≥6 points higher FMMA at3 months; planned enrollment610. PRECIS design assessment refers toFigure2 on subsequent page outside assigned scope. | Exploratory outcome status; superiority hypothesis; planned enrollment |

## Primary/statistical specifications (PR3-006, PR3-008, PR3-020, PR3-021, PR3-024)

- Primary outcome is the between-group difference of final FMMA scores at3 months after randomization. Scale total0–100; upper extremity0–66 and lower extremity0–34. Items use0=cannot perform,1=partially,2=fully. Trained outcome assessor performs assessments. Literature thresholds on p69:5.25 upper-extremity points and6 lower-extremity points; trial adopts6 total points as patient-relevant. Hypothesis p72: at least6 points higher with levodopa.
- Synopsis primary model p56: mixed effects; baseline FMMA covariate; treatment two-level factor levodopa versus placebo and event type acute ischemic versus hemorrhagic stroke as fixed effects; center random factor. Secondary outcomes: regressions appropriate to data type. Missing data: multiple imputation by chained equations.
- Sample-size synopsis p56:610 planned randomized participants over37 months;10% dropout;549 evaluable; normal FMMA SD25 points;548 patients enable6-point mean between-group difference at3 months with80% power, two-sided5% significance. Printed549 evaluable and548 required are retained separately. No formula or software specified on this page.
- Definitions p57 name FAS, ITT, PP, but this shard does not contain full analysis-set membership criteria. The detailed population/primary/sensitivity/secondary/interim/missing-data sections are located at internal40–41, physical86–87, beyond this shard. No subgroup covariate list, detailed sensitivity-analysis procedure, multiplicity hierarchy, alpha-spending rule, or numeric DSMC stopping boundary is specified within assigned pages. This is a disjoint-scope boundary, not an uncovered-unit gap.

## Intervention, population and operational windows (PR3-007, PR3-008, PR3-011, PR3-012)

Intervention: levodopa100mg/carbidopa25mg per dose or matching placebo, with standardized motor-learning rehabilitative therapy. Total39 treatment days beginning day after randomization. Days1–3 morning only; days4–6 morning+lunch; days7–34 three daily doses; days35–37 morning+lunch; days38–39 morning only. Placebo follows the identical scheme. Dose adaptation permitted for tolerability, pointer7.4; no adaptation algorithm in this shard.

Inclusion criteria p55, individually: (1) acute ischemic or hemorrhagic stroke≤7 days before randomization; hemorrhagic means intracerebral hemorrhage excluding subarachnoid hemorrhage and cerebral venous sinus thrombosis; (2) meaningful hemiparesis, total≥3 points on NIHSS motor arm,motor leg,limb ataxia; distal arm paresis equivalent to one of these; (3) randomization≥24 hours after thrombolysis/thrombectomy; (4) in-hospital rehabilitation required; (5) capable of standardized rehabilitation; (6) patient or next-of-kin informed consent.

Exclusion criteria p55, individually: (1) age<18; (2) Parkinson disease; (3) levodopa mandatory by treating physician judgment; (4) unable/unwilling to comply including drug intake oral/nasogastric/PEG; (5) severe aphasia unable to follow two-stage commands; (6) prestroke basic-ADL dependence, prestroke mRS>3; (7) pre-existing hemiparesis; (8) levodopa/carbidopa hypersensitivity or other contraindications per appended product characteristics; (9) pregnancy/breastfeeding/planned pregnancy during study, with pregnancy test required for childbearing-age women; (10) lack of safe contraception: childbearing potential and unwilling/not using medically reliable method throughout study; oral/injected/implanted/intrauterine or other investigator-accepted methods; surgically sterilized/hysterectomized or postmenopausal>2 years not considered childbearing potential.

Visit1 day0; prescreening day−7 to0. Visit2 5 weeks±7 days=end treatment; Visit3 3 months±14 days=primary endpoint; Visit4 6 months±20 days; Visit5 12 months±30 days. Optional long-term telephone Visits6–9:24,36,48,60 months±30 days. Treatment-phase rehabilitation transfer occurs day x; inpatient visit data collection on transfer day only. Planned enrollment610; synopsis administrative duration75 months; first-in03/2019; interventional last-out08/2024; clinical observation last-out05/2025; extended phone observation last-out05/2029;11 acute and10 rehabilitation centers. These calendars/center counts are prospective administrative descriptors.

## Outcome status and definitions (PR3-006, PR3-020–024)

Synopsis p54 secondary outcomes:
1. FMMA total at5 weeks,6 months,12 months; FMMA UE and LE at5 weeks,3,6,12 months.
2. NIHSS,mRS,PROMIS10/29,patient relevance of motor improvement,RMI at5 weeks,3,6,12 months.
3. Relative risks of mortality,recurrent stroke,serious AEs,selected other IMP-related AEs. The text `re-hospitalization` is visibly struck through in this synopsis; it is not silently retained as active wording.
4. Selected-center secondary assessments at5 weeks,3,6,12 months: ARAT,BBT,Jamar dynamometer,MI,trunk control,FAC,10MWT,MoCA,daily-life movement sensors.

Secondary objective items p68–69: (a) patient-self-assessed physical function; (b) self-assessed general health,pain,mood,anxiety,fatigue,social participation; (c) long-term sustainability of relevant motor improvement; (d) selective hand/wrist movement; (e) independent walking without another person; (f) less severe impairment; (g) higher ADL activity; (h) quality of life; (i) cognition; (j) no harm signals of increased all-cause mortality,recurrent stroke,SAEs.

Further objectives p69: compare3-month functional outcome with nonparticipants using Swiss Stroke Registry routine data; collect genetic/other biomarkers and routine/observational CT,MRI,fMRI for explanatory treatment-response analysis. Further assessments p72 explicitly call genetic/blood-marker analyses exploratory; blood collected at baseline or any follow-up. No study imaging performed; routine/observational imaging used for ischemic/hemorrhagic lesion type,location,volume.

Safety p69,p71: compare mortality,recurrent stroke,SAEs and prespecified nonserious IMP-related AEs. Interventional phase captures all-cause mortality,any recurrent stroke,SAEs,prespecified nonserious related AEs; observational3–12-month phase captures all-cause mortality and any recurrent stroke. Safety status coexists with secondary status in the synopsis; no composite is defined here.

Scale details:
- PROMIS scales mean50, SD10 in general population; minimum clinically important difference half SD. PROMIS29 domains:physical function,anxiety,depression,fatigue,sleep disturbance,social roles/activities,pain interference,pain intensity. First7 domains each4 questions,5 response levels; pain intensity visual analogue0–10. PROMIS10 general health/QoL/pain/mood/anxiety/fatigue/social participation.
- Patient relevance: improved motor function since last study visit? If yes, personally relevant? FMMA improvement compared with this report.
- RMI15 items,0–15; postural adjustment,transfer,walking,stairs. Minimum detectable change2.2 points; no established clinically meaningful difference stated. RMI≥7 corresponds to independent walking without another person.
- MI UE and LE subscales each0–100, isometric strength.
- TCT4 items each0–25; sitting-balance task30 seconds without trunk/feet support.
- ARAT4 subtests:grasp6 items,grip4,pinch6,gross movement3.
- BBT unilateral gross dexterity,number of wooden cubes transferred between2 compartments in60 seconds.
- FAC0–5, independent walking with/without aid and walking-surface type.
- 10MWT speed/cadence on10-meter track at comfortable and maximum speed.
- JDT grip strength affected and unaffected upper limb.
- MoCA0–30.
- Sensors:gyroscope,acceleration,magnetometer,pressure; activity counts/arm use and physical activity lying,sitting,standing,walking.

## Complete study-schedule map (PR3-011)

Columns: prescreen day−7 to0; Visit1 day0; dose escalation day1–6; rehabilitation transfer day x; full dose day7–34; taper day35–39; Visit2 5 weeks±7d; Visit3 3mo±14d; Visit4 6mo±20d; Visit5 12mo±30d; optional phone Visits6–9 24/36/48/60mo±30d; unscheduled visit.

Operational rows: consent/randomization/study-drug dispensing and protocol distribution atVisit1; inclusion/exclusion,demographics,medical history,pregnancy test at prescreen/Visit1; drug administration during escalation,transfer,full dose,taper; physical examination Visit1,transfer,Visits2–5,and unscheduled; concomitant rehabilitative therapies Visit1,treatment phases,transfer,Visit2,and unscheduled; concomitant medication Visit1,transfer,taper,Visits2–5,and unscheduled; drug accountability Visit1,transfer,Visit2,conditional unscheduled; blood sampling optional atbaseline/any follow-up.

Outcome rows: FMMA,NIHSS atVisit1,Visits2–5,unscheduled; mRS atVisit1,Visits2–9,unscheduled; PROMIS10,patient relevance,RMI atVisits2–9,unscheduled; PROMIS29 atVisits2–5,unscheduled. Selected-center ARAT,BBT,JDT,MI,TCT,FAC,10MWT,MoCA,sensor activity atVisit1,Visits2–5,unscheduled; optional blood sampling as above. Mortality and recurrent stroke collected atVisit1,treatment phases/transfer,Visits2–9,unscheduled. AE/SAE atVisit1,treatment phases/transfer,Visits2–3,conditional unscheduled; no AE/SAE checkmarks in clinical/telephone observational columns.

Schedule footnotes: transition in-person visit only on day of transfer, any treatment-phase day; starred selected-center assessments optional; blood sampling atbaseline or any follow-up. Unscheduled end-of-study visit on discontinuation/consent withdrawal; bracketed drug-accountability assessment only before treatment end, bracketed AE/SAE assessment only beforeVisit3. Other unscheduled outcome assessments require participant approval.

## Historical context quantities, retained separately (PR3-017–019)

These belong to prior studies cited in the plan, not ESTREL observations or ESTREL analysis specifications.

p65: first trial stroke3 weeks–6 months; levodopa100mg/day for3 weeks; Rivermead motor difference3.9 points,95%CI0.55–7.2; effect persisted3 weeks after cessation;47 analyzed; two factorial trials29 total levodopa recipients. Aphasia study100mg/day8 weeks after onset. DARS independent walking8 weeks OR0.78,95%CI0.53–1.15; average22(SD10) rehabilitation sessions during8 weeks, <3/week; cited recommendation3h/week; dosing45–60min before therapy,0–15min accepted; expected50% walking-rate increase. p67 prior timing≥30min or45–60min, accepted0–15min; oral peak0.5–2h; experimental single doses25,100,200mg; DARS SAE mean1.2(SD0.6) within8 weeks.

p66 historical Figure1, random-effects inverse-variance standardized mean difference,95%CI:

| Study/row | Levodopa mean,SD,n | Control mean,SD,n | Weight | SMD [95%CI] |
|---|---|---|---|---|
| Celik2004 |9.1,4.5,14 |7.3,4.5,12 |12.1% |0.39[−0.39,1.17] |
| Acler2005 |23,6,10 |22,6,10 |10.7% |0.16[−0.72,1.04] |
| Scheidtmann2001 |15.4,3.48,22 |11.3,3.48,25 |14.5% |1.16[0.54,1.78] |
| Sonde2007 with AMPH |22.6,7.8,3 |37.9,23.7,5 |5.3% |−0.67[−2.17,0.83] |
| Sonde2007 without AMPH |25.9,10.6,6 |39.4,9.1,7 |7.1% |−1.28[−2.52,−0.04] |
| Lokk2011 without MPH |66.3,31.7,20 |53.4,34.4,20 |14.4% |0.38[−0.24,1.01] |
| Lokk2011 with MPH |57.7,37.1,19 |57,35.3,19 |14.3% |0.02[−0.62,0.65] |
| Ford2019 DARS |3.1,3.1,308 |3.3,3,295 |21.7% |−0.07[−0.23,0.09] |
| Total |n402 |n393 |100.0% |0.15[−0.25,0.55] |

Heterogeneity tau²0.18; chi²21.20,df7,P.003; I²67%; overall Z0.73,P.46. Figure axis favors control left of0 and levodopa right. Caption: Celik RMA change6 weeks; Acler/Scheidtmann RMA5/6 weeks; Sonde FM leg at3 months used here; Lokk FM3 months; DARS ABILHAND8 weeks. Historical sensitivity excluding Celik or using Sonde arm FM did not explain heterogeneity. AMPH=amphetamine; MPH=methylphenidate.

## Completion and limitations

Mapped24/24 pages; missing scientific units0; unreadable scientific content0. Administrative/no independent quantitative-result pages49,50,52,58,61,63 remain explicitly documented. Page59 OCR is limited by orientation, closed by full visual table inspection. No new rendering; CPU OCR only. Detailed statistical-section contents beyond page72 are assigned elsewhere and were not read by this mapper. All extracted statements retain version/date, population/time/scale/status and source-page keys. The shard has24 page keys plus itemized endpoint/eligibility/statistical/schedule relationships; coordinator should assign global N/S identifiers when merging.

OCR completion record: all24 PSM6 outputs finished successfully, total74,352 bytes. The slower initial PSM3 pass was interrupted after the completed PSM6 pass, exit130; partial initial outputs are retained only as tooling derivatives. No unfinished OCR/render process remains. Total retained OCR content is below200,000 characters; all visual scientific mapping is complete.
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
# DOC-003 complete SAP and addendum quantitative/design map

Scope: DOC-003, `joi250066supp2_prod_1761597796.4701.pdf`, physical PDF pages 1–18, all inspected visually. Local relationship keys use prefix SAP; coordinator can assign global N/S IDs. No candidate discovery or diagnosis is performed here. All content is PLAN by prospective objectives, definitions, and planned analyses. The cover and repeated watermark say Final Report; no realized trial estimates, event counts, confidence intervals or P values occur in this document. Classification is by content rather than watermark.

## Evidence and tooling provenance

Read QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md, current source coverage, source inventory, DOC-003 evidence asset inventory, and tooling record. Reused source-linked renders: `.ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc003/page-01.png` through `page-18.png`, each opened visually. Reusable native layout is blank and does not supply scientific evidence. Each page is readable; no fresh higher-resolution rendering needed. Fresh OCR is an auxiliary locator/transcription aid and was generated on CPU with Tesseract 5.5.0, English, PSM 3:

```bash
for n in $(seq -w 1 18); do
  tesseract .ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc003/page-$n.png .ai_paper_validation/review_1_6_2/preprocessing/sap_mapper/page-$n -l eng --psm 3
done
```

Completed outputs: `preprocessing/sap_mapper/page-01.txt` through `page-05.txt`, relative to review_1_6_2. The OCR loop terminated with exit 143 before completion; pages 6–18 were mapped visually and do not require OCR to close scientific coverage. Source images, not OCR, determine all entries below. No supplied or preexisting artifacts were changed. No workbook, cached values, formulas or CSV records are within this shard.

Every source link below is relative from this extraction artifact to package root, using `../../../joi250066supp2_prod_1761597796.4701.pdf#page=N`.

## Complete page coverage

| Physical page | Content role | Complete mapped content | Keys | Status |
|---|---|---|---|---|
| 1 | PLAN | Cover, September 27, 2024; study title Enhancement of Stroke Rehabilitation with Levodopa; internal DKF ID me16Engelter; background reference to meta-analysis of 6 RCTs, historical rather than current-trial result | SAP-001 | COMPLETE |
| 2 | PLAN | Primary and secondary objectives; 100/25 mg three times daily; FMMA at 3 months | SAP-002 | COMPLETE |
| 3 | PLAN | Randomized multicenter superiority design and entire Figure 1 visit/treatment flow | SAP-003 | COMPLETE |
| 4 | PLAN | FAS/mITT and mortality footnote; all 6 inclusion criteria and first 8 exclusion criteria | SAP-004, SAP-005 | COMPLETE |
| 5 | PLAN | Remaining 2 exclusion criteria; primary outcome scale, scoring and components; secondary outcome list and footnote | SAP-005, SAP-006, SAP-007 | COMPLETE |
| 6 | PLAN | Mobility threshold; harm outcomes and horizons; 5 intercurrent events; estimand framework and primary treatment attribute | SAP-007, SAP-008, SAP-009 | COMPLETE |
| 7 | PLAN | Primary estimand continuation, complete-case estimand II, FAS/death-imputation estimand III | SAP-009 | COMPLETE |
| 8 | PLAN | Composite/death win-ratio estimand and mortality footnote, hypothetical estimand, on-treatment I start | SAP-009, SAP-013 | COMPLETE |
| 9 | PLAN | On-treatment I continuation, on-treatment II, measurement-window estimand, independent DSMB safety assessment | SAP-009, SAP-015 | COMPLETE |
| 10 | PLAN | Baseline summaries, primary model/inference/diagnostics/footnote, all secondary-model rules | SAP-010, SAP-011 | COMPLETE |
| 11 | PLAN | Missing data, imputation/pooling, center interaction, secondary-estimand analysis and full win-ratio algorithm/decision/multiplicity footnote | SAP-012, SAP-013, SAP-014 | COMPLETE |
| 12 | PLAN | Remaining estimand models; all 7 subgroup definitions and interaction analysis; R version | SAP-014, SAP-016 | COMPLETE |
| 13 | PLAN | Signatures dated September 27, 2024 and Pocock 2012 reference; no additional applicable quantitative relationship | SAP-001 | COMPLETE; quantitative content not applicable beyond metadata |
| 14 | PLAN | Addendum Final Report from 04.10.2024; contents and page pointers; no numeric results | SAP-017 | COMPLETE; quantitative content not applicable beyond metadata |
| 15 | PLAN | Complete 7-row clinical subgroup table: dichotomies and prior direction hypotheses | SAP-016 | COMPLETE |
| 16 | PLAN | Biomarker subgroup table, all 6 biomarkers/panels, hypothesis directions and panel analytes | SAP-018 | COMPLETE |
| 17 | PLAN | Biomarker-table continuation; 2 genetic subgroup rows and other exploratory genetic analyses | SAP-018, SAP-019 | COMPLETE |
| 18 | PLAN | All 4 predefined analysis rows, positivity-dependence labels, direction hypotheses, dated signature | SAP-020 | COMPLETE |

18/18 unique pages mapped. Reusable-backed units 18; fresh-required units 0; OCR locator derivatives completed for pages 1–5; all 18 pages independently opened visually. No uninspected source unit or scientific coverage gap.

## Design, populations, eligibility and intervention

### SAP-001 — identity and historical material

[Page 1](../../../joi250066supp2_prod_1761597796.4701.pdf#page=1): cover dated September 27, 2024; Methods & Statistics, study title Enhancement of Stroke Rehabilitation with Levodopa, internal DKF ID me16Engelter, Document Status Final Report. Background refers to 6 historical RCTs and their differing populations, stroke types, dose/duration, follow-up and outcome measures; these are background statements, not ESTREL trial results or sample-size inputs. Footer on substantive SAP pages identifies September 20, 2024, revision 264857, numbered 1–13. [Page 13](../../../joi250066supp2_prod_1761597796.4701.pdf#page=13) sponsor-investigator and trial-statistician signatures dated 27.9.2024; reference is Pocock, Ariti, Collier & Wang 2012, win ratio, European Heart Journal 33(2):176–182. Reference is only mapped as supplied; no external source accessed.

### SAP-002 — objectives and contrast

[Page 2](../../../joi250066supp2_prod_1761597796.4701.pdf#page=2): levodopa/carbidopa 100/25 mg three times daily versus placebo, each added to standardized rehabilitation. Primary: improved functional recovery after 3 months in acute ischemic or hemorrhagic stroke, quantified using FMMA. Secondary objective: effects on survival and general health. Main-paper matching keys: randomized contrast, dose/frequency, primary FMMA and 3-month horizon.

### SAP-003 — study design and Figure 1

[Page 3](../../../joi250066supp2_prod_1761597796.4701.pdf#page=3): randomized multicenter superiority trial, 1:1 levodopa/carbidopa versus matching placebo. Figure 1 is a schedule, not participant-flow counts:

| Stage/visit | Printed time/window | Content |
|---|---|---|
| Prescreening | day −7 to 0 | Prior to baseline |
| Visit 1 | Baseline | Informed consent, screening, baseline clinical assessments, randomization |
| Dose escalation | day 1–day 6 | Treatment phase |
| Full dose | day 7–day 34 | Study treatment |
| Taper | day 35–day 39 | Tapering phase |
| Transition | day x during treatment | Transition to rehabilitation center |
| Visit 2 | 5 weeks ±7 days | End of treatment |
| Visit 3 | 3 months ±14 days | Primary outcome assessment; end of interventional phase |
| Visit 4 | 6 months ±20 days | Long-term clinical follow-up |
| Visit 5 | 12 months ±30 days | Long-term clinical follow-up |
| Visit 6 | 24 months ±30 days | Telephone follow-up, optional extension |
| Visit 7 | 36 months ±30 days | Telephone follow-up, optional extension |
| Visit 8 | 48 months ±30 days | Telephone follow-up, optional extension |
| Visit 9 | 60 months ±30 days | Telephone follow-up, optional extension |

Interventional phase bracket covers baseline to primary assessment; observational clinical phase covers visits 4–5; optional extended telephone phase covers visits 6–9. Main matching keys: allocation, study superiority status, intervention duration, 5-week treatment visit, 3/6/12-month outcome visits and outcome window.

### SAP-004 — analysis sets and death handling

[Page 4](../../../joi250066supp2_prod_1761597796.4701.pdf#page=4), section 3.2:

- Full analysis set FAS: all randomized patients.
- Missing FMMA in patients surviving to Visit 3: multiple imputation by chained equations, section 6.
- Patients who died before Visit 3: not imputed except Treatment policy strategy III.
- Footnote 1: deceased before Visit 3 remain in FAS but contribute only to Treatment policy III and composite strategy.
- Modified intention-to-treat mITT: all FAS patients with complete FMMA at Visit 3.

These set definitions must be carried together with estimand-specific inclusion rather than using FAS alone as a denominator definition. Main matching keys: randomized set, primary analysis population, survivor imputation, complete case, death sensitivity/composite analyses.

### SAP-005 — every eligibility criterion

[Pages 4–5](../../../joi250066supp2_prod_1761597796.4701.pdf#page=4), sections 3.3–3.4. Inclusion, item by item:

1. Acute ischemic or hemorrhagic stroke ≤7 days before randomization; hemorrhagic means intracerebral hemorrhage excluding subarachnoid hemorrhage and cerebral venous sinus thrombosis.
2. Clinically meaningful hemiparesis: total ≥3 points from NIH stroke scale motor arm, motor leg, limb ataxia; distal arm paresis equivalent to one of those items.
3. Randomization ≥24 hours after thrombolysis or thrombectomy.
4. In-hospital rehabilitation required.
5. Capable of standardized rehabilitation participation.
6. Informed consent from patient or next of kin.

Exclusion, item by item:

1. Age <18 years.
2. Parkinson disease.
3. Levodopa mandatory under treating physician judgment.
4. Inability/unwillingness to follow procedures including drug intake orally, nasogastric or percutaneous endoscopic gastrostomy tube.
5. Severe aphasia, unable to follow two-stage commands.
6. Previously dependent in basal activities of daily living, prestroke mRS >3.
7. Preexisting hemiparesis.
8. Hypersensitivity to levodopa/carbidopa or other contraindications under appended product-characteristic summary.
9. Pregnancy, breastfeeding or intended pregnancy; women of childbearing age must have pregnancy test for eligibility (p5).
10. Lack of safe contraception: unwilling/not using medically reliable method for whole study, with oral/injectable/implantable contraception, intrauterine device or other investigator-approved reliable method described. Surgical sterilization/hysterectomy or postmenopause >2 years means not childbearing potential (p5).

Eligibility definitions map target population and NIH/mRS thresholds; not realized analysis counts.

## Outcome hierarchy, scales, time points and harm

### SAP-006 — primary endpoint scale

[Page 5](../../../joi250066supp2_prod_1761597796.4701.pdf#page=5), section 4.1: final FMMA score at Visit 3, rather than an unadjusted change-score outcome. Stroke-specific motor impairment index. Item scale: 0 cannot perform, 1 performs partially, 2 performs fully, a 3-point ordinal scale. Total 0 (no movements) to 100 (normal movements): upper extremity 66, lower extremity 34. All assessment by trained outcome assessor. Section 5.2 footnote on p10 states baseline-adjusted final-score difference is equivalent to baseline-adjusted between-arm difference in change from baseline to Visit 3. Main matching keys: FMMA total, 3 months, 0–100, upper/lower components and adjusted final/change contrast.

### SAP-007 — every secondary outcome and horizon

[Pages 5–6](../../../joi250066supp2_prod_1761597796.4701.pdf#page=5), section 4.2: secondary outcomes assessed at Visit 2 end treatment, Visit 3 end interventional phase, Visits 4–5 long-term follow-up, except explicit harm horizons. No separate designation as key secondary occurs in this SAP.

| Outcome | Definition/status and horizon |
|---|---|
| FMMA total | Secondary at Visits 2, 4, 5; Visit 3 total is primary per footnote 2. Printed list ends with “Visit 5 months”; visit schedule establishes Visit 5 at 12 months. |
| FMMA upper extremity | Separate secondary score, 66-point component |
| FMMA lower extremity | Separate secondary score, 34-point component |
| FMMA affected side | Secondary; bilateral pathology excluded from this analysis per p10 |
| Stroke severity | NIH Stroke Scale Score |
| Disability/dependence | Modified Rankin Scale mRS |
| Patient-reported outcome | PROMIS-29 |
| Patient-reported outcome | PROMIS 10, 10-question short form |
| Patient assessment | Relevance of motor improvement; no numeric scale specified here |
| Mobility | Rivermead Mobility Index; continuous plus binary ability to walk independently, score ≥7, for comparison with DARS |
| Potential harm | All-cause mortality through Visit 5 |
| Potential harm | Recurrent stroke through Visit 5 |
| Potential harm | Serious adverse events through Visit 3 |
| Potential harm | Nonserious adverse events possibly related to IMP through Visit 3 |

Main matching keys: each endpoint status, score/component, horizon, independent-walking ≥7 threshold, harm definitions and mortality/recurrent-stroke horizons.

## Estimands and intercurrent events

### SAP-008 — full intercurrent-event catalogue

[Page 6](../../../joi250066supp2_prod_1761597796.4701.pdf#page=6), section 4.3: estimand has five attributes: treatment, population, endpoint, population-level summary, handling of intercurrent events. Five listed events:

(a) Death before Visit 3.

(b) SAE causing motor-impairing event before Visit 3, e.g., recurrent stroke, fracture, comparable complication.

(c) Intake <80% of study medication.

(d) At least one week with <5 rehabilitation sessions/week in a 4-week period.

(e) Visit 3 outside its window.

Primary analysis treatment policy; other estimands supportive only. Main matching keys: death, SAE, medication adherence 80%, rehabilitation 5/week over 4 weeks, primary visit window.

### SAP-009 — all eight estimands and each attribute

[Pages 6–9](../../../joi250066supp2_prod_1761597796.4701.pdf#page=6). Each estimand uses levodopa plus standardized rehabilitation versus placebo plus standardized rehabilitation. Endpoint ordinarily FMMA at Visit 3; summary ordinarily between-treatment-arm mean difference; randomized assignment is retained. The table spells out all departures.

| Section/name | Population | Endpoint | Population summary | Intercurrent-event handling |
|---|---|---|---|---|
| 4.3.1 Primary treatment policy | FAS as 3.2; survivor primary FMMA analysis as mortality footnote states | Visit 3 FMMA | Mean difference between arms | Analyze by randomization irrespective of events; survivor missing FMMA imputed under 3.2/6 |
| 4.3.2 Treatment policy II, complete case | mITT, complete Visit 3 FMMA | Visit 3 FMMA | Mean difference | Randomized assignment irrespective of events; complete observed endpoint |
| 4.3.3 Treatment policy III, FAS including deaths | FAS including deaths before Visit 3 | Visit 3 FMMA | Mean difference | Randomized assignment irrespective of events; FMMA for deceased also imputed |
| 4.3.4 Composite using win-ratios | FAS including deaths; footnote 3 says no FMMA needed for deceased | Death and Visit 3 FMMA | Printed “difference in win-ratio” at Visit 3 | Randomized assignment irrespective of events; death worst possible outcome; unmatched win-ratio algorithm on p11 |
| 4.3.5 Hypothetical | FAS minus participants with event (b) | Visit 3 FMMA | Mean difference | Exclude motor-impairing SAE before Visit 3; retain randomized assignment |
| 4.3.6 On treatment / While on treatment | FAS minus participants with event (c) | Visit 3 FMMA | Mean difference | Exclude intake <80%; retain randomized assignment |
| 4.3.7 On treatment II / While on treatment II | FAS minus participants with event (d) | Visit 3 FMMA | Mean difference | Exclude inadequate documented rehabilitation; retain randomized assignment |
| 4.3.8 Measured according to protocol / While measured according to protocol | FAS minus participants with event (e) | Visit 3 FMMA | Mean difference | Exclude assessments outside predefined Visit 3 window; retain randomized assignment |

Populations retain 3.2 death-handling context except death-inclusive III and composite. Blue text in source marks departures from primary estimand. Section 7.1 p11 prints “Treatment policy strategy III, complete case analysis” as the model heading; section 4.3.3 definition above explicitly specifies imputation of deceased patients. Both labels are transcribed without reconciliation or diagnosis. Main matching keys: complete case, death-imputation, composite, SAE exclusion, ≥80% medication adherence, rehabilitation adherence, outcome-window exclusion and sensitivity status.

## Models, inference and missing data

### SAP-010 — descriptive and primary analysis

[Page 10](../../../joi250066supp2_prod_1761597796.4701.pdf#page=10), sections 5.1–5.2:

- Demographic/baseline summaries in FAS and mITT, stratified by treatment arm.
- Categorical data frequencies/percentages; continuous mean/SD; nonnormal continuous median/IQR.
- Footnote 4 considers extra baseline tables restricted to the model-used patients for an estimand if its result deviates from main estimand.
- Primary FMMA Visit 3 modeled using linear model with baseline FMMA covariate and two-level treatment factor levodopa versus placebo as variable of interest.
- Treatment effect presented with P value and 95% CI; interpreted as FMMA mean difference levodopa versus placebo at Visit 3, adjusted for baseline.
- Footnote 5: adjusted final-score difference equivalent to adjusted difference in change from baseline to Visit 3.
- Model assumptions checked including residuals and leverage; data transformation considered if assumptions violated.
- Alpha 0.05, two-sided.
- Primary model specifies baseline FMMA and treatment; center and treatment×center are assigned separately to exploratory heterogeneity analysis p11.

Main matching keys: baseline-adjusted linear model, factor/reference contrast, mean difference, 95% CI, two-sided .05 and transformation/diagnostic provisions.

### SAP-011 — all secondary analysis rules

[Page 10](../../../joi250066supp2_prod_1761597796.4701.pdf#page=10), section 5.3:

- All secondary outcomes except potential harm use data-type appropriate regression, adjusted for baseline when available.
- Binary: logistic regression, GLM logit link with binomial distribution.
- Continuous: linear model.
- Ordinal: ordinal logistic regression.
- Diagnostics as primary; severe assumption violations/high-leverage outliers may prompt transformations, nonparametric tests or robust regression.
- Potential harm summarized by treatment arm.
- All secondary outcomes also descriptive tables/graphs, possibly separate publications if useful.
- Primary estimand applies to every secondary analysis; FMMA affected side excludes bilateral pathology.

Main matching keys: binary/ordinal/continuous model identities, baseline adjustment, harm descriptive analyses and affected-side exclusions.

### SAP-012 — missing-data and pooling specification

[Page 11](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11), section 6:

- Number missing reported for every variable.
- 100 multiple imputations using chained equations.
- Imputation-generated values displayed in plots.
- Fit analysis model to each imputed data set.
- Combine estimates and variances using Rubin's rules for single parameter estimate/variance across imputations.
- Missing secondary outcomes imputed like primary analysis.
- Potential-harm outcomes not imputed.
- Mortality rules from 3.2/4.3 govern which primary/sensitivity values are imputed.

No list of imputation predictors, seed or imputation-specific distributions is supplied on these pages. This is an extraction statement only. Main matching keys: 100 MICE imputations, Rubin pooling, survivor versus deceased imputation, harm not imputed.

### SAP-013 — win-ratio calculation, hierarchy and decision

[Page 11](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11), section 7.1 and footnote 6:

- Composite variable strategy uses unmatched Pocock et al 2012 approach.
- Every levodopa patient compared with every placebo patient.
- Rule 1: survivor to Visit 3 wins over death before Visit 3.
- Rule 2: if both die before Visit 3, longer survival wins.
- Rule 3: printed “If both patients survive up to end of study,” higher FMMA wins. Endpoint definition in 4.3.4 is FMMA Visit 3; both printed timing statements retained.
- Win ratio = number of comparisons won by treatment divided by number won by placebo.
- 95% CI estimated using 1000 bootstrap samples following cited statistical appendix.
- Repeat analysis on each imputed data set.
- CI excluding 1 taken as evidence of between-arm difference and discussed similarly to conventional sensitivity result P<0.05.
- Footnote 6: all analyses in section sensitivity analyses, no correction for multiple testing; discuss in context of primary analysis, not standalone evidence.

No separate tie algorithm or explicit cross-imputation bootstrap-CI pooling formula printed. Main matching keys: death/FMMA composite, pairwise hierarchy, unmatched win ratio, 1000 bootstrap, CI null 1, multiplicity/supportive status.

### SAP-014 — secondary-estimand, center and subgroup analysis

[Pages 11–12](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11), section 7:

- Exploratory treatment heterogeneity across centers: add center and treatment×center to main model; plot stratified by center or groups of centers.
- Same primary-estimand model for policy II and policy III under section 7.1 headings, hypothetical, while on treatment I/II, and while measured according to protocol.
- Composite strategy method separately specified SAP-013.
- Each subgroup uses primary estimand, same main model plus subgroup variable and subgroup×treatment additional fixed effect.
- Subgroups displayed as forest plot.
- Underlying subgroup hypotheses prespecified with ICEMAN before subgroup analysis and recorded in addendum.
- Analyses performed in R 4.3.1 or higher.

Main matching keys: exploratory center interactions, same-model sensitivity analyses, subgroup interaction terms/forest plot, subgroup hypothesis/addendum, software.

### SAP-015 — safety oversight and absent design inputs

[Page 9](../../../joi250066supp2_prod_1761597796.4701.pdf#page=9), section 4.4: endpoints for potential harm considered important; DSMB investigates safety independently of results presented in this document. Main result considered potentially high impact for stroke management. Across all 18 pages no numerical power, sample-size calculation, anticipated effect/SD, loss inflation, noninferiority/equivalence margin, interim efficacy boundary, quantitative stopping rule or randomized stratum definition appears. Therefore those inputs cannot be extracted from this SAP shard; protocol shard may supply them. This is a complete-scope absence record rather than candidate reasoning.

## Addendum: complete subgroup and predefined-analysis tables

### SAP-016 — all seven clinical subgroup rows

[Page 12](../../../joi250066supp2_prod_1761597796.4701.pdf#page=12) lists groups; [page 15](../../../joi250066supp2_prod_1761597796.4701.pdf#page=15) provides table of dichotomization and prior hypothesized effect modification:

| Subgroup | Dichotomy | Prior direction/magnitude hypothesis |
|---|---|---|
| Age | <median vs ≥median | Younger may obtain more pronounced levodopa motor-learning enhancement than older, attributed to neuroplasticity/learning capacity |
| Sex | Male vs female | No expected difference in direction or magnitude of levodopa effect |
| Selective hand/wrist movement at baseline | NIHSS Distal Motor Function subscore 0 vs >0 | No expected levodopa effect difference with/without selective movement |
| Cortical dysfunction | Sum of NIHSS Best Language, Extinction and Inattention, Visual subscores 0 vs >0 | No expected treatment effect difference; dysfunction may affect learning and lead to poorer recovery |
| Baseline SSRI use | Yes vs no | No expected levodopa effect difference |
| Stroke type | Acute ischemic vs intracerebral hemorrhage | No expected levodopa effect difference |
| Baseline FMMA severity | <median vs ≥median | No expected levodopa effect difference across severity levels |

Page 12 baseline FMMA subgroup has no printed cutoff; page 15 supplies median split. Median numeric values not supplied in this document. Main matching keys: all seven subgroup definitions and predicted younger direction; separate 0/>0 selective-movement/cortical cutoffs; baseline-treatment and stroke-type labels.

### SAP-017 — addendum identity

[Page 14](../../../joi250066supp2_prod_1761597796.4701.pdf#page=14): Addendum to Methods & Statistics, Version Final Report from 04.10.2024. Contents references clinical ICEMAN subgroup hypotheses p2, biomarker hypotheses p4, genetic subgroup p5, predefined analyses p6. Physical addendum pages are 14–18; contents numbering is retained as supplied, not used to reassign PDF page locators. [Page 18](../../../joi250066supp2_prod_1761597796.4701.pdf#page=18) signature dated Basel 4.10.2024. All addendum entries are hypotheses and analyses to be performed, hence PLAN.

### SAP-018 — every biomarker table entry

[Pages 16–17](../../../joi250066supp2_prod_1761597796.4701.pdf#page=16), heading Prespecified Hypotheses of Biomarker Subgroups with ICEMAN. Column named Dichotomization lists biomarker names rather than numerical cutpoints. Each hypothesis anticipates concentration-associated differences in direction or magnitude of stroke recovery, while not anticipating levodopa treatment-effect difference between high and low concentrations.

| Category | Biomarker/panel | Printed concentration hypothesis |
|---|---|---|
| Neuroaxonal injury | Neurofilament light chain NfL | Recovery varies with NfL concentration; no levodopa effect modification high vs low |
| Neuroaxonal injury | Tau | Recovery varies with Tau concentration; no levodopa effect modification high vs low |
| Myocardial injury/dysfunction | Hs-troponinT | Recovery varies with Hs-troponinT; no levodopa effect modification high vs low |
| Myocardial injury/dysfunction | NT-pro-BNP | Recovery varies with NT-pro-BNP; no levodopa effect modification high vs low |
| Aging processes of immune system | GDF-15 | Recovery varies with GDF-15; no levodopa effect modification high vs low |
| Aging processes of immune system | Senescence-associated secretory phenotype panel | Recovery varies with panel; no levodopa effect modification high vs low; statement continues on p17 |

Panel contains exactly the listed analytes: IL-1b, IL-6, IL-10, MCP-1, TNFa, MMP-1, osteopontin. Numeric concentration thresholds, units, standardized panel score and separate fitted-model specification are not printed here. Main matching keys: biomarker exploratory/prespecified subgroup status and all names/threshold availability.

### SAP-019 — every genetic table entry

[Page 17](../../../joi250066supp2_prod_1761597796.4701.pdf#page=17), Prespecified Hypotheses of Genetic Subgroup Analyses with ICEMAN:

| SNP/label | Dichotomy | Hypothesis |
|---|---|---|
| Rs1842681 | Homozygous/heterozygous | Risk allele of SNP rs1842681 might contribute to unfavorable stroke recovery |
| ApoE | Homozygous/heterozygous | ApoE risk allele might contribute to unfavorable recovery among hemorrhagic stroke patients |

All other planned genetic analyses, including levodopa score, copy number variation and SNPs, exploratory because evidence on genetics in stroke recovery is limited. Specific risk-allele identity, numeric score definition, genetic model or multiplicity rule for this table not printed. Main matching keys: listed hypotheses, hemorrhagic-only ApoE hypothesis, exploratory status of other genetic analyses.

### SAP-020 — all four predefined analysis rows

[Page 18](../../../joi250066supp2_prod_1761597796.4701.pdf#page=18), Predefined Analyses. Table columns: Planned Analyses; Dependent on a positive result; A priori hypothesized direction of effect modification.

| Planned analysis | Printed dependence | Full analysis/hypothesis content |
|---|---|---|
| ESTREL participants versus Swiss Stroke Registry patients | NO | Compare participant outcomes to similarly affected national/Swiss registry nonparticipants; hypothesize better recovery among ESTREL participants |
| Type/amount of rehabilitation with and without levodopa | YES/NO | Investigate type/amount impact on motor recovery and whether levodopa effect depends on type/amount; greater motor rehabilitation built on motor-learning principles expected to improve recovery; levodopa effect hypothesized influenced by extent incorporating these principles |
| Levodopa association with poststroke fatigue | Blank | Motivational properties may be associated with reduced poststroke fatigue |
| Levodopa association with poststroke depression | Blank | Motivational properties may be associated with reduced poststroke depression |

No realized effects or numeric outcomes in this table. Blank dependence cells are retained rather than assigned an inferred status. Main matching keys: predefined registry/rehabilitation/fatigue/depression analyses and their dependence/status statements.

## Mapping summary and limits

Twenty local keyed relationship groups SAP-001–SAP-020 cover every assigned page and every table/figure item. Scientific analysis relationships are SAP-002–SAP-004, SAP-006–SAP-016, SAP-018–SAP-020; metadata/eligibility are separately retained where they define matching context. No realized inferential results occur. All pages reviewed, including signatures/contents and administrative material. No candidate IDs, findings, screening or dispositions supplied. No old AI conclusions read. Limits: image-only source requires visual reading/OCR locator; no unreadable source content; no scientific coverage gaps. Inputs not present within these 18 pages are explicitly named above and must not be imported from outside this assigned shard.
# Support quantitative evidence: results, implemented code, administrative material

Mandatory support_quantitative_mapper stage. Complete disjoint assignment: DOC-004 physical PDF pages 1–27, DOC-005 pages 1–8, DOC-006 page 1, DOC-007 page 1. Total 37 unique units, all 37 mapped. Document role REPORT throughout, assigned by content. This is extraction and relationship mapping only; no finding selection or candidate diagnosis is performed. Local keys N-Rxxx and S-Rxxx identify numeric and statistical relationships for coordinator numbering. They do not reuse historical review IDs.

Scope, review contract, source inventory, source coverage and assigned evidence inventory were read. Sources remain authority. Reused DOC-004/DOC-005/DOC-007 native layouts and DOC-004 page images 10–27, and DOC-006 page image 1 were used as transcription aids. All 19 distinct assigned images were visually inspected, below the 32-image context bound. Fresh direct-source layout corroboration for readable text used Poppler pdftotext 26.01.0, CPU: `pdftotext -layout SOURCE OUTPUT`, with outputs `preprocessing/support_results/DOC-004-direct-layout.txt`, `DOC-005-direct-layout.txt`, `DOC-007-direct-layout.txt`. Existing image-render engine version is historical/unrecorded. No OCR, fallback environment, Office extractor, source modification, or external evidence was used. Formula/cached workbook distinctions are not applicable: no workbook exists in this assignment.

## Complete page coverage

| Source/unit | Content and mapping | Status |
|---|---|---|
| DOC-004 p1 | Cover, eTable/eFigure index; no independent result | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-004 p2 | Contents and page locators; no independent result | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-004 p3 | Trial committees, medication production and affiliations; no statistical result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-004 p4 | Centers: 13 acute and 11 rehabilitation; administrative counts N-R001 | COMPLETE |
| DOC-004 p5 | Continuation of rehabilitation-center list; no independent result | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-004 p6 | Analysis software and quality-control description S-R001 | COMPLETE |
| DOC-004 p7 | Imputation, pooling, disclosed SAP deviations S-R002/S-R003 | COMPLETE |
| DOC-004 p8 | PRAI questions/definition S-R004 | COMPLETE |
| DOC-004 p9 | Distal motor item scoring S-R005 | COMPLETE |
| DOC-004 p10 | eTable 1 baseline counts and continuous summaries N-R002 | COMPLETE |
| DOC-004 p11 | eTable 1 continuation N-R002 | COMPLETE |
| DOC-004 p12 | FAS/mITT definitions and narrative estimand results S-R006/S-R007 | COMPLETE |
| DOC-004 p13 | eTable 2 estimands 1–8 S-R007 | COMPLETE |
| DOC-004 p14 | eTable 3 post hoc estimands 9–11 S-R008 | COMPLETE |
| DOC-004 p15 | eTable 4 all ten secondary-outcome rows N-R003/S-R009 | COMPLETE |
| DOC-004 p16 | eTable 5 all SAE rows N-R004 | COMPLETE |
| DOC-004 p17 | eTable 6 all AE rows N-R005 | COMPLETE |
| DOC-004 p18 | eTables 7 and 8: all coefficients/CIs/P values and F-tests S-R010/S-R011 | COMPLETE |
| DOC-004 p19 | eTable 9: prespecified AE list S-R012 | COMPLETE |
| DOC-004 p20 | eFigure 1 inclusion/exclusion thresholds S-R013 | COMPLETE |
| DOC-004 p21 | eFigure 2 schedule, every assessment group and footnote S-R014 | COMPLETE |
| DOC-004 p22 | eFigure 3 all printed site totals, axis/time labels N-R006 | COMPLETE |
| DOC-004 p23 | eFigure 4 estimand forest plot and legends 1–3 S-R015 | COMPLETE |
| DOC-004 p24 | eFigure 4 legend continuation 5–8 S-R015 | COMPLETE |
| DOC-004 p25 | eFigure 5 all center/arm/scale labels, grouping rule N-R007 | COMPLETE |
| DOC-004 p26 | eFigure 6 spline predictions and axis labels S-R016 | COMPLETE |
| DOC-004 p27 | eFigure 7 PH1–PH3, subgroup cutoff and labels S-R017 | COMPLETE |
| DOC-005 p1 | Collaborator roster: Aarau, Baden, Lausanne; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p2 | Collaborator roster: Lausanne, Fribourg, Hirslanden; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p3 | Collaborator roster: Bern, Basel; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p4 | Collaborator roster: Basel; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p5 | Collaborator roster: Basel, Zurich; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p6 | Collaborator roster: Graubünden, Münsterlingen, St. Gallen, Felix Platter; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p7 | Collaborator roster: Felix Platter, Rheinfelden; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-005 p8 | Collaborator roster: Rheinfelden, Valens; no quantitative result/design rule | COMPLETE, NO_APPLICABLE_RESULT |
| DOC-006 p1 | Implemented R main analysis code, lines 1–35 S-R018 | COMPLETE |
| DOC-007 p1 | Data availability and request conditions S-R019; no quantitative result | COMPLETE, NO_APPLICABLE_RESULT |

## Administrative and statistical definitions

### N-R001 — Centers

Source [DOC-004 p4](../../../joi250066supp3_prod_1761597796.4701.pdf#page=4), continuation p5. Acute centers n=13: Basel, Zurich, Fribourg, Bern, Lausanne, St. Gallen, Münsterlingen, Winterthur, Baden, Graubünden, Aarau, Hirslanden Zurich, Sion. Rehabilitation centers n=11: Felix Platter Basel, Rheinfelden, HFR Meyriez-Murten, Zihlschlacht, Zurich Lengg, Cereneo Vitznau, Bad Zurzach, Valens, Zurich Wald, Rheinburg Walzenhausen, Sion. Administrative site keys can match enrollment figure; no outcome estimates on these pages.

### S-R001 — Software and quality control

[DOC-004 p6](../../../joi250066supp3_prod_1761597796.4701.pdf#page=6). R 4.3.1 released June 16, 2023. Packages: dplyr 1.1.4; data.table 1.14.8; tidyr 1.3.0; forcats 1.0.0; plyr 1.8.9; purrr 1.0.2; tibble 3.2.1; tidyselect 1.2.0; lme4 1.1-35.1; MASS 7.3-60; Matrix 1.6-3; mice 3.16.0; mitml 0.4-5; glmnet 4.1-8; survey 4.2-1; survival 3.5-7; e1071 1.7-13; nnet 7.3-19; rpart 4.1.19; class 7.3-22; ggplot2 3.4.4; scales 1.2.1; grid 4.3.1; gtable 0.3.4; colorspace 2.1-0; munsell 0.5.0; assertthat 0.2.1; boot 1.3-28; DBI 1.1.3; digest 0.6.36; stringr 1.5.1; stringi 1.8.4; tools 4.3.1. Independently verified statistician code, cross-checked key dataset elements, and validated tables/figures against underlying data. Package listing does not identify which model produced each result; actual code is S-R018.

### S-R002 — Imputation and pooling

[DOC-004 p7](../../../joi250066supp3_prod_1761597796.4701.pdf#page=7). 100 multiple imputations using chained equations. Generated imputed values displayed in plots; model fit in each imputed dataset; estimates and variances combined using Rubin's rules into one estimate and variance per parameter. Missing/incomplete FMA imputed at item level; secondary outcomes at summary-score level. Potential-harm outcomes not imputed. Match main-paper missing-data/statistical-analysis keys and supplied SAP estimand/MI specification; no external imputation model assumed.

### S-R003 — Disclosed SAP deviations

Same p7: introductory text states two deviations, followed by three numbered items. Record each item rather than selecting by count: (1) mRS for participants who died before three months was set to 6 rather than imputed; (2) missing subjective PRAI not imputed; (3) secondary-outcome adjusted mean difference initially stated for affected side in SAP, calculation performed for unaffected side. The third item describes a wording change and authors' supplied rationale; no mapper judgment. Match main-paper mRS/PRAI/secondary FMA and supplied SAP endpoint/imputation keys.

### S-R004 — PRAI

[DOC-004 p8](../../../joi250066supp3_prod_1761597796.4701.pdf#page=8). Two questions: whether participant noticed improvement in deficits caused by stroke since last study visit; if yes, whether improvement is meaningful in daily life. English meanings recorded from bilingual printed questions. Match eTable 4 PRAI no relevant improvement, main-paper PRAI and SAP relevance definition. No additional numeric outcome on p8.

### S-R005 — Distal motor scoring

[DOC-004 p9](../../../joi250066supp3_prod_1761597796.4701.pdf#page=9). Examiner holds forearm, requests maximum finger extension; if no extension places fingers fully extended and observes flexion for 5 seconds. Only first attempt graded, no repetition of instructions/testing. Score 0 normal/no flexion after 5 seconds; 1 some extension after 5 seconds but not fully extended, uncommanded movement unscored; 2 no voluntary extension after 5 seconds, movement at other times unscored. Match eligibility NIHSS/distal-paresis key. Supplied references are locators only; no external sources consulted.

## N-R002 — Complete eTable 1 baseline map

[DOC-004 p10](../../../joi250066supp3_prod_1761597796.4701.pdf#page=10) and [p11](../../../joi250066supp3_prod_1761597796.4701.pdf#page=11). Values in columns Overall / Placebo / Levodopa. Population N 610 / 303 / 307. Counts are printed No. (%) unless otherwise stated. Every continuous row retains printed label and dispersion type. Match main baseline Table 1 by row, population and time; descriptive copies remain descriptive rather than model effects.

| Printed row | Overall | Placebo | Levodopa |
|---|---|---|---|
| N | 610 | 303 | 307 |
| Median age [IQR], years | 73 [64–82] | 74 [64–84] | 72 [62–81] |
| Female sex | 252 (41.3) | 133 (43.9) | 119 (38.8) |
| Median BMI [IQR] | 25.7 [23.4 28.7] | 25.3 [23.1,28.1] | 26.0 [23.5,29.1] |
| Hypertension | 435 (71.3) | 213 (70.3) | 222 (72.3) |
| Diabetes | 144 (23.6) | 64 (21.1) | 80 (26.1) |
| Hyperlipidemia | 291 (47.7) | 152 (50.2) | 139 (45.3) |
| Smoking | 127 (20.8) | 59 (19.5) | 68 (22.1) |
| Atrial fibrillation | 95 (15.6) | 61 (20.1) | 34 (11.1) |
| Coronary heart disease | 99 (16.2) | 47 (15.5) | 52 (16.9) |
| Dementia | 20 (3.3) | 9 (3.0) | 11 (3.6) |
| Movement disorder | 11 (1.8) | 5 (1.7) | 6 (2.0) |
| Depression | 41 (6.7) | 18 (5.9) | 23 (7.5) |
| Prior ischemic stroke | 82 (13.4) | 43 (14.2) | 39 (12.7) |
| Prior hemorrhagic stroke | 11 (1.8) | 6 (2.0) | 5 (1.6) |
| Prior median mRS [IQR] | 0.0 [0.0,1.0] | 0.0 [0.0,1.0] | 0.0 [0.0,0.0] |
| Prestroke home | 596 (97.7) | 294 (97.0) | 302 (98.4) |
| Prestroke nursing home | 9 (1.5) | 5 (1.7) | 4 (1.3) |
| Prestroke other | 5 (0.8) | 4 (1.3) | 1 (0.3) |
| Stroke ischemic | 519 (85.1) | 259 (85.5) | 263 (85.7) |
| Stroke hemorrhagic | 91 (14.9) | 44 (14.5) | 44 (14.3) |
| MCA affected | 460 (75.4) | 230 (75.9) | 230 (74.9) |
| MCA bilateral | 16 (2.6) | 6 (2.0) | 10 (3.3) |
| MCA right | 278 (45.6) | 136 (44.9) | 142 (46.3) |
| MCA left | 166 (27.2) | 88 (29.0) | 78 (25.4) |
| ACA affected | 68 (11.1) | 31 (10.2) | 37 (12.1) |
| ACA bilateral | 4 (0.7) | 2 (0.7) | 2 (0.7) |
| ACA right | 23 (3.8) | 11 (3.6) | 12 (3.9) |
| ACA left | 41 (6.7) | 18 (5.9) | 23 (7.5) |
| PCA affected | 60 (9.8) | 33 (10.9) | 27 (8.8) |
| PCA bilateral | 8 (1.3) | 5 (1.7) | 3 (1.0) |
| PCA right (p11) | 35 (5.7) | 20 (6.6) | 15 (4.9) |
| PCA left | 17 (2.8) | 8 (2.6) | 9 (2.9) |
| Vertebrobasilar affected | 108 (17.7) | 45 (14.9) | 63 (20.5) |
| Vertebrobasilar bilateral | 4 (0.7) | 1 (0.3) | 3 (1.0) |
| Vertebrobasilar right | 59 (9.7) | 28 (9.2) | 31 (10.1) |
| Vertebrobasilar left | 45 (7.4) | 16 (5.3) | 29 (9.4) |
| Median FMA total, affected, randomization [IQR] | 34.0 [14.0,54.0] | 33.0 [13.0,52.8] | 35.0 [14.8,55.3] |
| Median FMA upper, affected, randomization [IQR] | 18.0 [6.0,34.0] | 17.5 [6.0,34.0] | 20.0 [6.0,35.0] |
| Median FMA lower, affected, randomization [IQR] | 14.0 [6.5,21.0] | 14.0 [7.0,21.0] | 15.0 [6.0,21.0] |
| Median NIHSS at randomization [IQR] | 8.2 (3.9) | 8.3 (3.8) | 8.2 (3.9) |
| Median mRS randomization [IQR] | 4 [4,5] | 4 [4,5] | 4 [4,5] |
| Median stroke-onset to randomization time [IQR] | 7 [5,10] | 8 [5,10] | 7 [5–11] |
| IV thrombolysis | 120 (19.7) | 66 (21.8) | 54 (17.6) |
| Bridging therapy | 33 (5.4) | 13 (4.3) | 20 (6.5) |
| Endovascular therapy | 81 (13.3) | 44 (14.5) | 37 (12.1) |

Footnotes: IQR interquartile range; MCA middle cerebral artery; ACA anterior cerebral artery; PCA posterior cerebral artery; mRS modified Rankin Scale; NIHSS printed National Health Institutes Stroke Scale; FMA Fugl-Meyer Motor Assessment. NIHSS row's printed label and parenthesized values retained without reinterpreting the dispersion. Stroke-onset time units are not expressly printed in this row; preserve source label, seek matching main/SAP unit.

## Estimands and populations

### S-R006 — Population and intervention definitions

[DOC-004 p12](../../../joi250066supp3_prod_1761597796.4701.pdf#page=12). FAS paragraph begins all randomized included, then states MICE imputes missing FMA among survivors to three months and those dying before three-month assessment excluded. Modified ITT = FAS with complete three-month FMA. Intervention = levodopa plus standardized rehabilitation versus placebo plus standardized rehabilitation. Match main primary population, complete-case sensitivity and SAP estimand populations. The row-specific death inclusions below are retained separately from the generic population definition.

### S-R007 — eTable 2 and matching narrative

[DOC-004 p13](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13), narrative p12. Printed table effect-column title: Estimated Effect of Levodopa: Mean Difference on FMA, [CI]. Contrast levodopa versus placebo, three-month visit, intention-to-treat/randomized assignment unless indicated. Numeric CIs as printed; narrative specifies 95%. Match main primary FMA total score/estimand sensitivity results and SAP estimands by number, not generic treatment-policy name alone.

| Estimand | Population, endpoint and intercurrent-event rule | Summary | Printed effect [CI] | N |
|---|---|---|---|---:|
| 1, primary endpoint, treatment policy | FAS; FMA at three months; analyzed by randomization irrespective of intercurrent events | Mean difference between treatment arms | −0.90 [−3.78,1.98] | 582 |
| 2, treatment policy II | Modified ITT; complete FMA at three months; randomized assignment | Mean difference | −0.39 [−3.33,2.56] | 551 |
| 3, treatment policy III | FAS label; three-month FMA; FMA of deaths imputed | Mean difference | −0.98 [−3.77,1.81] | 610 |
| 4, composite using win-ratios | FAS label; death and FMA at three months; randomized assignment | Printed difference in win-ratio at three months, win ratio [95% CI] | 1.06 [0.86,1.26] | 610 |
| 5, hypothetical | FAS; three-month FMA; exclude SAE causing motor impairment before visit (recurrent stroke, fractures, comparable complications) | Mean difference | −1.41 [−4.31,1.49] | 545 |
| 6, on treatment | FAS; three-month FMA; exclude intake <80% of study medication | Mean difference | −0.57 [−3.73,2.58] | 496 |
| 7, on treatment II | FAS; three-month FMA; exclude at least one week with fewer than five rehabilitation sessions/week in a four-week period | Mean difference | 0.19 [−3.11,3.49] | 450 |
| 8, on treatment III | FAS; three-month FMA; exclude visit outside window | Mean difference | −0.33 [−3.31,2.65] | 524 |

Narrative p12 repeats estimands 2,3,5,6,7,8 with same values. Narrative estimand 4 calls the composite win-ratio result an odds ratio and prints 1.06 (95% CI 0.86 to 1.25); preserve both narrative and table effect labels and upper limits. No P values printed for estimand table rows. No excluded-count arithmetic assumed beyond printed N and stated rules.

### S-R008 — eTable 3 post hoc estimands

[DOC-004 p14](../../../joi250066supp3_prod_1761597796.4701.pdf#page=14). Same effect-column title and contrast as eTable 2. All described as post hoc.

| Estimand | Population, endpoint and rule | Effect [CI] | N |
|---|---|---|---:|
| 9, treatment policy | FAS; change in FMA baseline to three months; randomized assignment irrespective of intercurrent events | −0.90 [−3.78,1.98] | 582 |
| 10, treatment policy IV | All randomized; three-month FMA; death before visit assigned worst possible FMA=0 | −0.03 [−3.27,3.21] | 610 |
| 11, on treatment IV | FAS; three-month FMA; exclude those with at least one week <5 sessions/week over four weeks and intake <80% | 0.32 [−3.25,3.89] | 395 |

Population-level summary mean difference between arms for all three. Matching keys: main post hoc change-score, death-as-zero, combined adherence/rehabilitation sensitivity, eFigure 7 PH1/PH2. Do not silently reinterpret printed conjunction in estimand 11.

## N-R003 / S-R009 — eTable 4 complete secondary outcomes

[DOC-004 p15](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15). Time three months except FMA total affected five weeks. Printed effect-column title for the whole table is Estimated Effect of Levodopa: Mean Difference on FMA, [CI]. Table does not give model formula or P values; match main outcome-specific method and scale instead of treating all rows as FMA mean differences. Placebo/levodopa continuous summaries mean (SD), mRS median [IQR], PRAI count (%). SMD means standardized mean difference. N printed total participants. Each row is an independent numeric/inferential relationship with suffix .01–.10.

| Row | Placebo | Levodopa | SMD | Effect [CI] | N |
|---|---|---|---:|---|---:|
| .01 FMA total unaffected, 3 months | 89.14 (10.32) | 89.67 (9.87) | 0.052 | 0.63 [−0.72,1.99] | 582 |
| .02 FMA upper affected, 3 months | 39.12 (19.19) | 39.20 (19.30) | 0.004 | −0.73 [−2.97,1.50] | 582 |
| .03 FMA lower affected, 3 months | 22.88 (6.90) | 22.91 (7.28) | 0.003 | −0.13 [−1.02,0.77] | 582 |
| .04 FMA total affected, 5 weeks | 56.27 (25.20) | 57.37 (26.70) | 0.042 | 0.02 [−2.81,2.84] | 582 |
| .05 NIHSS, 3 months | 4.20 (3.37) | 4.02 (3.39) | 0.054 | −0.14 [−0.61,0.33] | 582 |
| .06 PROMIS 29, 3 months | 65.11 (13.79) | 64.74 (14.33) | 0.026 | −0.37 [−3.34,2.61] | 582 |
| .07 PROMIS 10, 3 months | 29.87 (5.74) | 30.04 (5.73) | 0.031 | 0.18 [−0.98,1.33] | 582 |
| .08 mRS, 3 months | 3.00 [2.00,4.00] | 3.00 [2.00,4.00] | 0.034 | 0.93 [0.69,1.23] | 596 |
| .09 Rivermead Mobility Index, 3 months | 9.89 (4.73) | 9.70 (4.85) | 0.041 | −0.33 [−1.04,0.37] | 582 |
| .10 PRAI no relevant improvement, 3 months | 51 (18.89), n=270 | 51 (18.48), n=276 | dash | dash | 546 |

Footnote expansions: FMA Fugl-Meyer Motor Assessment; PROMIS 10/29 Patient-Reported Outcomes Measurement Information System; NIHSS National Institutes Stroke Score; mRS modified Rankin Scale; PRAI patient-reported assessment of relevance of motor improvement; CI confidence interval; IQR interquartile range. Link outcome keys to main Table 2/secondary narrative and SAP corresponding endpoints, imputation and outcome model. No effect reconstructed from raw group mean differences; printed modeled effect remains distinct.

## N-R004 — eTable 5 complete SAE counts

[DOC-004 p16](../../../joi250066supp3_prod_1761597796.4701.pdf#page=16). Columns Overall / Placebo / Levodopa. Title serious adverse events; raw n printed, no explicit unique-participant denominator for event categories. Header No. (%) under severity/outcome, but cells print counts only. Match main safety counts and distinguish event versus participant quantities using main context.

| Row | Overall | Placebo | Levodopa |
|---|---:|---:|---:|
| n | 255 | 129 | 126 |
| Participants died | 28 | 17 | 11 |
| Hospitalization | 212 | 102 | 110 |
| Permanent/significant incapacity or disability | 23 | 13 | 10 |
| Life-threatening | 16 | 10 | 6 |
| Severity severe, daily activities impossible | 103 | 54 | 49 |
| Severity moderate, interferes with daily activities | 106 | 54 | 52 |
| Severity mild, tolerable | 46 | 21 | 25 |
| Outcome continuing | 6 | 4 | 2 |
| Outcome recovered/resolved with sequelae | 76 | 40 | 36 |
| Outcome study participant died | 29 | 18 | 11 |
| Outcome unknown | 0 | 0 | 0 |
| Outcome recovered/resolved | 142 | 65 | 77 |
| Outcome other | 2 | 2 | 0 |

No test, effect, interval, or P value supplied here. Both differently named death rows are retained independently; their measurement units are not collapsed.

## N-R005 — eTable 6 complete AE counts

[DOC-004 p17](../../../joi250066supp3_prod_1761597796.4701.pdf#page=17). Prespecified adverse events of interest, Overall / Placebo / Levodopa. Header No. (%) but counts alone printed. No participant denominator or test printed. Match main harm outcome and AE category definition S-R012.

| Row | Overall | Placebo | Levodopa |
|---|---:|---:|---:|
| n | 145 | 67 | 79 |
| Intensity mild | 58 | 29 | 29 |
| Intensity moderate | 86 | 37 | 49 |
| Intensity severe | 2 | 1 | 1 |
| Outcome ongoing | 1 | 0 | 1 |
| Outcome resolved with sequel | 29 | 13 | 16 |
| Outcome resolved without sequel | 116 | 54 | 62 |
| Drug relation certain | 2 | 1 | 1 |
| Drug relation possible | 66 | 32 | 34 |
| Drug relation Probably | 23 | 7 | 16 |
| Drug relation Unassessable | 2 | 2 | 0 |
| Drug relation unlikely | 39 | 15 | 24 |
| Drug relation unrelated | 14 | 10 | 4 |

Definitions: mild tolerable; moderate interferes with daily activities; severe daily activities impossible; probably likely; unassessable unclassifiable. Retain printed Overall n=145; no normalization to summed categories.

## S-R010 — eTable 7 interaction model

[DOC-004 p18](../../../joi250066supp3_prod_1761597796.4701.pdf#page=18). Visually transcribed embedded table. Title model including interaction between baseline FMA and treatment group, with baseline FMA. Visit 3/main analysis. Term names identify centered baseline affected-side FMA and levodopa contrast.

| Term | Estimate | CI | p |
|---|---:|---|---|
| (Intercept) | 62.51 | [60.45,64.57] | <0.001 |
| fma_affected.Visit_1.cent | 0.78 | [0.69,0.87] | <0.001 |
| medicationLevodopa | −0.90 | [−3.78,1.99] | 0.542 |
| fma_affected.Visit_1.cent:medicationLevodopa | 0.00 | [−0.12,0.12] | 0.971 |

Printed caption: main analysis Visit 3, including interaction between baseline and follow-up, estimated levodopa treatment effect. Spline model with basic spline 3 degrees of freedom significantly better than no-spline model: F-test p<0.01 for all imputations. Preserve title's baseline/treatment interaction and caption's baseline/follow-up phrase as distinct printed model descriptions. Match main post hoc baseline interaction and primary effect, SAP model checks; no main-effect formula substituted for this interaction model.

## S-R011 — eTable 8 spline model

Same source p18, visually transcribed. Title model without interaction between baseline FMA and treatment group, baseline FMA modeled using splines (3 df).

| Term | Estimate | CI | p |
|---|---:|---|---|
| (Intercept) | 20.09 | [14.28,25.90] | <0.001 |
| bs(fma_affected.Visit_1.cent, 3)1 | 64.73 | [46.34,83.13] | <0.001 |
| bs(fma_affected.Visit_1.cent, 3)2 | 57.52 | [43.48,71.56] | <0.001 |
| bs(fma_affected.Visit_1.cent, 3)3 | 77.49 | [61.68,93.31] | <0.001 |
| medicationLevodopa | −0.87 | [−3.65,1.92] | 0.541 |

Caption main analysis Visit 3, FMA total score, baseline FMAA spline, estimated levodopa effect; no evidence for interaction between spline-baseline FMAA and medication, F-test p>0.75 for all imputations. Separate overall interaction test from medication main-effect P. Match main post hoc nonlinear baseline analysis and eFigure 6.

## S-R012 — Prespecified harm endpoint content

[DOC-004 p19](../../../joi250066supp3_prod_1761597796.4701.pdf#page=19). Complete eTable 9 list: nausea; vomiting; taste disturbances; dry mouth; anorexia; arrhythmias; postural hypotension; syncope (brief unconsciousness due to reduced brain blood flow); drowsiness including sudden sleep; fatigue; dementia; psychoses (distorted perception of reality); hallucinations; confusion; euphoria; abnormal dreams; insomnia; depression; anxiety; dizziness; dystonia (involuntary contractions); dyskinesia (inability to control voluntary movements); chorea (sudden face/shoulder twitching). No counts per named AE, test or estimate on this page. Match main prespecified AE reporting and prospective list by content.

## S-R013 — Eligibility and exclusion

[DOC-004 p20](../../../joi250066supp3_prod_1761597796.4701.pdf#page=20). All eFigure 1 criteria mapped. Inclusion: acute ischemic or intracerebral hemorrhagic stroke ≤7 days before randomization, excludes subarachnoid hemorrhage/cerebral venous sinus thrombosis; meaningful hemiparesis NIHSS motor arm+motor leg+limb ataxia sum ≥3, distal arm paresis equivalent to one item; randomization ≥24 hours after thrombolysis/thrombectomy; in-hospital rehabilitation needed; capable of standardized rehabilitation; consent participant/next of kin. Exclusion: age<18; Parkinson's; levodopa mandatory per physician; inability/unwillingness to comply with drug intake/procedures (oral, nasogastric, PEG); severe aphasia unable two-stage commands; prestroke mRS>3; prior hemiparesis; hypersensitivity or contraindication to levodopa/carbidopa; pregnancy/breastfeeding/intended pregnancy, childbearing-age pregnancy test; lack of reliable contraception throughout trial (oral/injected/implanted, intrauterine, or investigator accepted), surgical sterilization/hysterectomy or postmenopause>2 years considered outside childbearing potential. Match main eligibility/randomization and protocol criteria; no numeric result on page.

## S-R014 — Complete schedule and assessment groups

[DOC-004 p21](../../../joi250066supp3_prod_1761597796.4701.pdf#page=21), visually inspected schedule. Prescreen day −7 to 0; enrollment/randomization day 0 Visit 1; intervention dose escalation days 1–6, transition day X, full-dose days 7–34, taper days 35–39; Visit 2 end treatment 5 weeks ±7 days; Visit 3 primary outcome 3 months ±14 days; Visit 4 six months ±20 days; Visit 5 twelve months ±30 days; Visits 6–9 telephone follow-up 24,36,48,60 months each ±30 days; unscheduled end-of-study visit on withdrawal/discontinuation.

Consent/randomization/drug and therapy booklet at enrollment; medication group A levodopa/group B placebo assigned enrollment and intervention phases through taper, marked end treatment at Visit 2. Inclusion/exclusion prescreen and enrollment; demographics prescreen; history and pregnancy at enrollment; physical examination enrollment, Visits 2–5 and unscheduled; rehabilitation concomitant therapies enrollment, intervention/transition/full dose/taper, Visits 2–5, unscheduled; concomitant medication those points plus telephone Visits 6–9; accountability enrollment and Visit 2, unscheduled conditional; optional blood sampling enrollment.

Outcome rows: FMA (primary) enrollment, Visits 2–5, unscheduled; NIH Stroke Scale prescreen, enrollment, Visits 2–5, unscheduled; mRS enrollment, Visits 2–9, unscheduled; PROMIS-10 Visits 2–9, unscheduled; PROMIS-29 Visits 2–5, unscheduled; patient-reported improvement Visits 2–9, unscheduled; Rivermead Mobility Index enrollment, Visits 2–9, unscheduled. Optional selected-center rows Action Research Arm Test, Box and Block Test, Jamar dynamometer Test, Motricity index, Trunk control, 10-meter walk and Montreal Cognitive Assessment: enrollment, Visits 2–5, unscheduled; functional ambulation categories additionally Visits 6–9. Optional daily activity movement sensors enrollment and Visits 2–5, unscheduled. Mortality/all cause and any recurrent stroke monitored intervention/transition/full dose/taper, Visits 2–9, unscheduled; AE/SAE intervention through Visit 3 and conditional unscheduled, no scheduled marks after Visit 3.

Footnotes: transition has no in-person visit, data collection on transfer acute-to-rehabilitation any intervention day; double asterisk optional/selected centers, blood may be sampled baseline or any follow-up; unscheduled visit upon discontinuation/consent withdrawal, [x] accountability only before treatment end and AE/SAE only before Visit 3; unscheduled outcomes subject to participant approval. Main matching keys primary three-month window, intervention 39-day regimen, secondary outcome times/status, extended observation; role remains REPORT schedule, not separate PLAN.

## N-R006 — Enrollment figure printed totals

[DOC-004 p22](../../../joi250066supp3_prod_1761597796.4701.pdf#page=22), eFigure 3. All n=610; University Hospital Basel n=318; University Hospital Zurich n=70; Hôpital de Fribourg n=57; Inselspital Bern n=52; CHUV Lausanne n=25; Klinik Hirslanden Zürich n=24; Kantonsspital St. Gallen n=19; Kantonsspital Münsterlingen n=15; Kantonsspital Winterthur n=13; Kantonsspital Baden n=8; Kantonsspital Graubünden n=8; Kantonsspital Aarau n=1. Y-axis Patients included, ticks 0,200,400,600. X-axis Date of randomization, ticks 2020,2021,2022,2023,2024. Curves show cumulative recruitment; exact recruitment dates and intermediate counts not printed, so not digitized. Match main total randomized and administrative centers only.

## S-R015 — eFigure 4 forest plot

[DOC-004 p23](../../../joi250066supp3_prod_1761597796.4701.pdf#page=23), continued [p24](../../../joi250066supp3_prod_1761597796.4701.pdf#page=24). Title total FMA estimands at three months, levodopa vs placebo. X-axis Adjusted Mean Difference (FMMA points), ticks −4,−2,0,2; null line 0, left favoring placebo, right favoring levodopa. Rows 1,2,3,5,6,7,8; estimand 4 not plotted because displayed ratio elsewhere. Every plotted interval crosses 0; point 7 is to right, other points to left. No numeric estimate/CI annotation; numeric counterparts are S-R007, not digitized from pixels. Caption 1 excludes deaths (primary treatment policy), 2 missing/incomplete complete case, 3 deaths imputed. Continuation 5 excludes motor-impairing SAE hypothetical/on treatment phrase; 6 intake<80%; 7 fewer rehabilitation therapies; 8 out-of-range three-month visits. Caption-based contrast and units captured; matching main sensitivity results use S-R007.

## N-R007 — eFigure 5 by-center display

[DOC-004 p25](../../../joi250066supp3_prod_1761597796.4701.pdf#page=25). Title FMA at three months by treatment arm and center. Five facets HFR, INS, USB, USZ, other; each Placebo/Levodopa. Y-axis FMMA affected side (change Visit 1 to Visit 3), ticks −50,0,50; x-axis medication. Points, boxes/medians/whiskers without numeric summaries or sample-size annotations. Centers with <50 recruitments pooled Other. All facet labels, arms, axis quantity and threshold captured; no exact medians/quantiles inferred from graphics. Matching key baseline-to-three-month change, eTable 3 estimand 9, main center/subgroup display; title and actual axis quantities retained separately.

## S-R016 — eFigure 6 spline graphic

[DOC-004 p26](../../../joi250066supp3_prod_1761597796.4701.pdf#page=26). Title nonlinear association between baseline and three-month FMA (spline model); plot title Predicted values of fma affected Visit 3. Y-axis fma affected Visit 3, ticks 30,60,90. X-axis fma affected Visit 1.cent, ticks −40,−20,0,20,40,60. Increasing nonlinear red prediction curve with shaded band; no numeric prediction limits, treatment contrast, sample sizes or band confidence-level label printed. Caption says Figure 4: main estimate including FMAA at baseline as spline, estimated marginal effects. Capture figure label as printed without changing source. Matches spline terms/test S-R011 and baseline predictor center in code.

## S-R017 — eFigure 7 post hoc/subgroups

[DOC-004 p27](../../../joi250066supp3_prod_1761597796.4701.pdf#page=27). Rows PH1,PH2,PH3; x-axis estimate ticks −6,−3,0,3; y-axis model; null vertical 0. Top legend black comment, green moderate–severe impairment, purple very severe impairment. PH1 black near 0, PH2 black right of 0, PH3 green right and purple left; all four horizontal intervals cross 0. No exact numeric effect/CI/P/N annotations, so no digitization or invented precision. Caption PH1 primary analysis model with death missing outcomes imputed as 0; PH2 primary model excluding low baseline intake and minimal documented rehabilitation; PH3 baseline FMA severe ≤35 vs mild-to-moderate >35. Preserve caption and top-legend severity names separately. PH1 matches eTable 3 estimand 10, PH2 estimand 11; PH3 matches main baseline severity subgroup/post hoc analysis, with printed cutoff 35. Label alone does not identify quantitative subgroup effects to finer precision than their graphical sign/null crossing.

## S-R018 — Implemented main analysis code

[DOC-006 p1](../../../joi250066supp5_prod_1761597796.4751.pdf#page=1), printed lines 1–35; visually read usable image, no usable historical code text relied upon. Title ESTREL Main Analysis Code. Packages ggplot2 and mice lines 4–5. Lines 8–10 load raw dat/dat.rda and dat/mice0.rds (comment imputations on FAS), define N.imp as length(mice0$imp[[1]]); number of imputations is data-driven in code, no literal 100 here. Lines 13–16 raw boxplot/jitter by medication with y my.data[, ep], white outlier color, theme_bw and ylab(ep.name). Lines 19–21 comments identify fma_affected.Visit_3 primary endpoint, fma_affected.Visit_1.cent centered baseline, medication randomized group.

Exact analysis formula lines 22–23: `model <- with(mice0, lm(fma_affected.Visit_3 ~ fma_affected.Visit_1.cent + medication))`. Pool/return lines 25–26: `summary(pool(model))`. Diagnostic lines 29–35 set par(mfrow=c(2,2)), loop i over 1:N.imp, fit same formula using `data = complete(my.data = mice0, i)`, plot with main paste0("Imputation: ", i), then par(mfrow=c(1,1)). This is implemented ordinary linear model of follow-up affected-side FMA on centered baseline and treatment, pooled over imputed FAS data. No treatment/baseline interaction, spline, center covariate/random term, additional covariate or outcome change expression appears in the main formula. Diagnostic formula identical. Missing-data generation and raw data not supplied in this PDF; no raw-data execution attempted. Match main primary analysis, S-R002 pooling, S-R007 estimand 1, S-R008 change-score analysis and SAP main model. Code's plotted variables ep/ep.name are referenced but not defined in this page; preserve that boundary without assumptions.

## S-R019 — Data-sharing scope and availability

[DOC-007 p1](../../../joi250066supp6_prod_1761597796.4801.pdf#page=1). Publication September 22, 2025; trial registry identifier NCT03735901 and BASEC-ID 2018-02021. Printed Data available: No. Subsequent explanation trial data can be made available on reasonable request to corresponding author, with detailed proposal, objectives and SAP; additional material may be requested; approvals sponsor-investigator/corresponding author, steering committee and center principal investigators; compatibility ethics/regulatory and consent checked. Administrative evidence, no numeric result, planned decision rule, or supplied participant dataset. Neither online registry nor request pathway accessed.

## Matching and completeness handoff

Exact source-page links above are package-relative from this extraction file. All source matching uses result identity, endpoint/time, population, contrast, adjustment/model and statistical scale; figures with no printed numeric values are recorded as graphical-only evidence. N-R002 row keys span all baseline rows; N-R003/S-R009 .01–.10 span all secondary outcomes; N-R004/N-R005 span all harm counts; S-R007 estimands 1–8 and S-R008 9–11 are complete; S-R010/S-R011 cover all coefficient/test rows. Administrative units were opened individually through usable page-preserving layouts; no unit omitted by assuming absence of extraction means absence of content.

Coverage: DOC-004 27/27, DOC-005 8/8, DOC-006 1/1, DOC-007 1/1. Reusable-backed units 37, fresh-required 0, scientific gaps 0. Limitations: native extraction lacks embedded graphic/table values on DOC-004 p18 and graphic pages21–23,25–27 and code DOC-006 p1, all closed by visual mapping. Exact graphical-only values in center boxplots, spline curve/band and subgroup forest plot are not printed and are not assigned artificial precision. No additional workbook/CSV/DOC/DOCX support within assignment. No old conclusions used.
