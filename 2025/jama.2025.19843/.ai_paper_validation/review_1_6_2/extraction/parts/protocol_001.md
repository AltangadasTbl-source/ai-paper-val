# DOC-002 protocol mapping: PDF pages 1–51

Runtime canonical ID: /root/protocol_mapping_001. Fresh support-mapping shard. Exact source: joi250087supp1_prod_1766516490.96011.pdf, PDF pages 1–51 only. Role: PLAN throughout. Complete original protocol version 1.1 occupies PDF pp.3–47 (printed pp.1–45). Version 2.0 cover/signature/contents occupy assigned pp.48–51. Scientific contents of later versions are assigned elsewhere.

Coverage: 51 of 51 pages mapped; 49 reusable-backed and 2 fresh-required. No scientific coverage gaps. Forty-seven relationship groups QP1-001–QP1-047 follow; each may contain explicitly enumerated related components. Matching main-paper keys are semantic keys for subsequent matching, not assertions that the report contains every planned endpoint. No candidates were diagnosed, and no old review conclusions were read. No Office, workbook or CSV source occurs in the assigned scope; formulas and cached workbook values are not applicable.

## Extraction provenance

Reusable locator: .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/layout_all_pages.txt (historical pdftotext version unspecified). All 51 assigned form-feed records were read in bounded page ranges 1–9, 10–13, 14–17, 18–28, 29–38 and 39–51; p45 was reread independently because a combined output was truncated. No unassigned source page was read. Normative scope, review contract, tooling record, source inventory, evidence-asset inventory, source coverage and coverage manifest were read.

Fresh native text, sorted reading-order text and rendered images were produced for exact PDF pp.4 and49. Text is empty because both are scanned signature pages, not blank pages. Both fresh 200-dpi images were visually inspected. PyMuPDF 1.26.4 rendered on the CPU; no OCR was necessary. Run-level GPU authorization did not change these derivative engines. The exact derivatives are native-004.txt, layout-004.txt, page-004.png, native-049.txt, layout-049.txt and page-049.png under .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/. Engine for native text: PyMuPDF; for layout: PyMuPDF sorted reading order; for rendering: PyMuPDF CPU at200dpi. Sources and reused assets remain unchanged.

For each N=4 or49, these bundled helper commands were executed with the corresponding zero-padded output filename:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text joi250087supp1_prod_1766516490.96011.pdf --first N --last N .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/native-NNN.txt
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text joi250087supp1_prod_1766516490.96011.pdf --first N --last N .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/layout-NNN.txt --layout
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render joi250087supp1_prod_1766516490.96011.pdf --page N .ai_paper_validation/review_1_6_2/preprocessing/protocol_001/page-NNN.png
```

## Complete page ledger

Every row is COMPLETE. Not applicable means inspected and no result-relevant quantitative relationship was present. Historical numerical context is retained separately from prospective trial design.

| PDF page | Inspected content and quantitative applicability | Relationship groups |
|---:|---|---|
| 1 | Protocol cover, investigator/contact details; no trial quantity | Identity context |
| 2 | Bundle version index and changes pointer | QP1-001 |
| 3 | Original protocol cover, version1.1 and project identity | QP1-001 |
| 4 | Fresh scanned signed original protocol page, not blank | QP1-002 |
| 5 | Original contents, sections1–11; pointers only, not applicable | Contents inspected |
| 6 | Original contents, sections12–18; pointers only, not applicable | Contents inspected |
| 7 | Summary rationale and30-day primary objective | QP1-003,004 |
| 8 | Success/competing risks, secondary endpoints, subgroups, inclusion | QP1-004–021 |
| 9 | Exclusions, intervention and initial measurement schedule | QP1-021–025 |
| 10 | Follow-up status, sample size, administrative timeline | QP1-026,027 |
| 11 | Historical ECMO outcomes and pharmacokinetics | QP1-028,029 |
| 12 | Historical SURVIVE, LeoPARDS, LICORN, LEVO-CTS, CHEETAH | QP1-030–033 |
| 13 | Historical CHEETAH and observational ECMO series | QP1-033,034 |
| 14 | Primary and complete secondary objectives | QP1-004–020 |
| 15 | Detailed primary competing-risk definition and secondary outcomes | QP1-004–020 |
| 16 | Superiority design and stochastic minimization | QP1-035,036 |
| 17 | Blinding/unblinding and placebo appearance; no additional quantity | QP1-022 context |
| 18 | Consent table, treatment timing and baseline data definitions | QP1-023–025 |
| 19 | Daily collection and protocolized weaning decision thresholds | QP1-025,037 |
| 20 | D30/D60 status, participation duration and schedule table | QP1-026,027 |
| 21 | Standard-care table, withdrawal and drug stopping thresholds | QP1-038 |
| 22 | Retained data, SAE follow-up, trial cancellation | QP1-038,039 |
| 23 | Complete inclusion/exclusion list | QP1-021 |
| 24 | Consent, screening reasons, recruitment table | QP1-027,040 |
| 25 | Pharmacokinetics, vial concentration and packaging | QP1-029,041 |
| 26 | Drug dose, preparation table and ECMO management | QP1-022,041,042 |
| 27 | Common management, prohibited drug, efficacy window | QP1-042,043 |
| 28 | Safety event definitions | QP1-044 |
| 29 | AE severity/causality table and notification rules | QP1-044 |
| 30 | Notification exemptions and refractory hypotension threshold | QP1-038,044 |
| 31 | Monthly death monitoring, safety imbalance and AE thresholds | QP1-039,044 |
| 32 | SAE resolution and sponsor assessment; no efficacy quantity | QP1-044 |
| 33 | Administrative safety-reporting timelines | QP1-044 |
| 34 | DSMB safety remit; data-management administration | QP1-039 |
| 35 | Statistical overview, alpha, descriptive summaries and adjustment | QP1-045 |
| 36 | ITT exception, event/censor coding and time definitions | QP1-004,005,046 |
| 37 | Fine–Gray, secondary models, sample-size inputs and alpha | QP1-047 |
| 38 | Pre-unblinding amendment rule and principal ITT | QP1-046 |
| 39 | Missing CRF data coding and audit trail | QP1-046 |
| 40 | Consent/emergency enrollment; administrative, no additional quantity | QP1-021 context |
| 41 | Sponsor halt and amendment approval; administrative | QP1-039,046 context |
| 42 | Archives, funding, insurance and publication; no trial result | Not applicable |
| 43 | Publication/registration placeholder; no trial result | Not applicable |
| 44 | Bibliography1–16; no new trial relationship | Historical reference locators |
| 45 | Bibliography17–30; no new trial relationship | Historical reference locators |
| 46 | Bibliography31–38, including Latouche sample-size reference | QP1-047 reference |
| 47 | Addenda/scales/product pointers; no new quantitative relationship | Scale identities inspected |
| 48 | Version2.0 cover, date and project identity | QP1-001 |
| 49 | Fresh scanned second-version signature/approval page, not blank | QP1-002 |
| 50 | Version2.0 contents1–11; pointers only | Not applicable |
| 51 | Version2.0 contents12–18; pointers only | Not applicable |

## Complete relationship map

All entries have document role PLAN. Direct evidence links below resolve to the supplied PDF. Other page numbers in each entry are also exact PDF locators. Historical studies have no matching LEVOECMO trial-result key.

### QP1-001 — Version provenance

[PDFp2](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=2) lists original1.1,12/04/2020; second2.0,05/31/2023; final3.0,06/26/2024; summary of changes. [p3](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=3) prints version1.1 of04/12/2020, P170914J and EUDRACT2019-004319-29. [p48](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=48) prints version2.0 of31/05/2023. Preserve date strings: index and covers use different day/month conventions. Footer April2018 is template date. Matching key: protocol version/amendment provenance.

### QP1-002 — Fresh signature pages

[p4](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=4), printed2/45: research codeP170914J, version1.1 of04/12/2020; investigator date appears2/7/2021 (administrative handwriting uncertainty); sponsor stamp19JUL2021; CPP and ANSM date placeholders remain dotted. [p49](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=49), printed2/46: version2.0 of31/05/2023; investigator handwriting18/7/2023; sponsor signature/date unfilled; CPP OuestIII approval04/01/2021 and ANSM authorization30/11/2020. Matching key: administrative version identity, no efficacy result.

### QP1-003 — Pharmacologic summary

p7: action up to7–9days through active metabolite; single24h perfusion rationale. Pharmacologic context rather than outcome follow-up. Key: intervention-duration rationale.

### QP1-004 — Primary endpoint and windows

[pp7–8](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=8),[p14](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=14),[p15](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=15): time to successful ECMO weaning within30days after randomization. Success requires survival without ECMO, another mechanical circulatory device or heart transplantation for30days after removal. All removals up toD30 considered; removalD30 requires success ascertainment throughD60. No event after30days enters event-time analysis; those remaining on ECMO or without defined event censoredD30. p14 places unsuccessful weaning at attempted-weaning date. Key: primary outcome, status, window and event timing.

### QP1-005 — Competing risks, censoring and time definitions

pp8,15,[p36](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=36): successful weaning is event of interest. Competing events: death beforeD30 without weaning and unsuccessful weaning (death, repeat ECMO, another device or transplant within30days after removal). Time to successful weaning = weaning date minus randomization date. Unsuccessful time = removal date minus randomization date. Death time = death date minus randomization date. Lost-follow-up time = latest-news date minus randomization date, censored. Other patients censored at time30days. p15 rejects days alive without ECMO as primary because death on ECMO produces tied0days. Key: event coding, competing risks and time formulas.

### QP1-006 — Mortality

pp8,14,15: secondary mortalityD30 andD60. p20 records living/dead and death date/hour. p37 survival analysis restricted to60days. Key: mortality status and time points.

### QP1-007 — ECMO duration

pp8,14,15: total support duration inclusion–D30 and inclusion–D60. Key: ECMO duration and window.

### QP1-008 — ECMO-free days

pp8,14,15: number of ECMO-free days inclusion–D30/D60. No further zero-assignment algorithm printed here. Key: ECMO-free days, secondary status and window.

### QP1-009 — ICU duration

pp8,14,15: ICU stay duration. p20 records ICU discharge status/dateD30/D60. Key: ICU duration.

### QP1-010 — Hospital duration

pp8,14,15: hospitalization duration. p20 records hospital discharge status/dateD30/D60. Key: hospital duration.

### QP1-011 — Cardiovascular composite

pp8,14,15: major adverse cardiovascular eventsD30/D60 comprising death, cardiac transplant, escalation to permanentLVAD, stroke, dialysis and rehospitalization for heart failure. Key: composite components, status and time.

### QP1-012 — Organ failure

pp8,14,15: days with organ failure defined bySOFA and days alive without organ failure inclusion–D30. p14 says days without organ failure; pp8,15 expressly include alive condition. p47 listsSOFA addendum. No specific score threshold printed here. Key: SOFA/organ-failure duration and alive-free days.

### QP1-013 — Catecholamine support duration

pp8,14,15: duration of hemodynamic support with catecholamines. Key: secondary support duration.

### QP1-014 — Hemodynamic support-free days

pp8,14,15: days alive without hemodynamic support inclusion–D30. Key: alive support-free days and window.

### QP1-015 — Ventilation duration

pp8,14,15: duration of mechanical ventilation. Key: secondary ventilation duration.

### QP1-016 — Ventilator-free days

pp8,14,15: days alive without mechanical ventilation inclusion–D30 and inclusion–D60. Key: alive ventilation-free days and windows.

### QP1-017 — LV function

pp8,14,15: echocardiographic LV functionD30 after randomization. Key: LV function, secondary status and assessment time.

### QP1-018 — Hemodynamic time outcomes

pp8,14,15: time to improvement in systolic/diastolic/meanBP and heart rate; time to stabilization. No single numerical improvement threshold printed. Weaning readiness separatelyp19. Key: hemodynamic improvement/stabilization outcomes.

### QP1-019 — Drug reactions

pp8,14,15: incidence of atrial fibrillation, other supraventricular arrhythmias, ventricular arrhythmias including tachycardia/fibrillation/torsades, and hypokalemia. Key: adverse-reaction outcomes and secondary status.

### QP1-020 — Outcome subgroups

pp8,14,15: primary and secondary endpoints in prespecified acuteMI, myocarditis, post-cardiac-surgery and post-cardiac-arrest subgroups. No interaction-test specification printed. These groups are distinct from allocation factors below. Key: prespecified etiology subgroup analyses.

### QP1-021 — Eligibility/population

pp8–9,[p23](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=23): adults with refractory acute cardiogenic shock, VA-ECMO in preceding48h, recovery likely, relative/surrogate consent or emergency enrollment. Twenty exclusions: age<18; pregnancy/lactation; ECMO>48h; resuscitation>30min before ECMO; irreversible neurological pathology; end-stage cardiomyopathy without recovery hope; mechanicalMI complication; aortic regurgitation>II; ECMO for pulmonary embolism; cardiotoxic intoxication; afterLVAD; heart-transplant recipient; moribund/SAPSII>90; ChildB/C cirrhosis or other severe hepatic insufficiency; chronic dialysis; levosimendan hypersensitivity; torsades history; epilepsy; guardianship/permanent legal incompetence; another interventional study. pp24,40 permit emergency randomization then subsequent consent. Key: eligibility and randomized population.

### QP1-022 — Dose and comparator

[p9](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=9),[p26](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=26): continuousIV24h, no initial bolus; start0.15μg/kg/min, increase0.20μg/kg/min after2h if no rate-limiting effects. Riboflavin placebo reproduces yellow color, identical route/procedure/duration. p17 states double blinding and ICU nurse preparation. Key: randomized dose/duration/comparator.

### QP1-023 — Start window

p18: start as soon as possible, no later than24h after randomization; infusion24h. Key: intervention timing.

### QP1-024 — Baseline covariate definitions

p18: McCabe/Jackson, Charlson, SAPSII, SOFA; severe LV dysfunction byNYHA/EF; hepatic insufficiency bilirubin>100μmol/L or albumin<35g/L without another cause. Immunocompromised yes/no. Key: baseline prognostic definitions when matched to adjustment.

### QP1-025 — Repeated measurement schedule

pp9–10,18–19: baselineD1, thenD2–D30 or death/ICU discharge; p19 says days1,2,3…30. BP/HR, catecholamine doses, ventilation/RRT yes/no, urine output, potassium/ionogram, lactate, blood gases, WBC, platelets, renal/hepatic markers, SOFA, ECG. Echo: LVEF, LV outflowVTI and lateral mitral-annulus systolic TissueDoppler velocity. ECMO: FiO2, membrane ventilation, pump speed/flow, clots, blockage/change, hemolysis, cannulation hemorrhage/infection and leg ischemia. No repeated-measures model printed here. Key: measurement windows and physiological endpoints.

### QP1-026 — Status follow-up and schedule table

pp10,20: D30/D60 vital/ECMO status, repeat ECMO, other support, transplant, ventilation, ICU/hospital discharge and dates. Contact details at ICU discharge permitD60 collection. p20 table: D1 information/consent/randomization/history/dispensing; clinical exam, ECG/echoD1 andD2–D30 or death/discharge; AE/vital/ECMO statusD1, subsequent period andD60; continuation consent during follow-up andD60 if not obtained. Key: ascertainment schedule.

### QP1-027 — Enrollment and timeline

p10:206 subjects,103/arm;13sites;24months recruitment,2months participation,26months total,0.7subjects/site/month. p20:60days participation/follow-up,24h treatment. p24 recruitment table:206;13sites;24months;15.8subjects/site (printed15,8);0.66subjects/site/month. Key: planned sample size; site/calendar projections administrative.

### QP1-028 — Historical ECMO context

p11: long-term survival70–80% myocarditis/poisoning,40–50%MI,15–25% refractory cardiac arrest; hemorrhage10–20%, cannulation infection/bacteremia10–15%, limb ischemia5–10%, stroke5%. p30 historical mortality40–60%; p31 historical58%. No LEVOECMO-result counterpart.

### QP1-029 — Pharmacokinetics

pp11–12,25: half-life60min, clearance300mL/min, protein binding97%, equilibrium4–8h; active metabolite half-life about3days. p25 discusses effects through48h and historical24h levosimendan versus48h dobutamine. No trial-result counterpart.

### QP1-030 — Historical SURVIVE

p12: n1327; loading12μg/kg then0.1–0.2μg/kg/min for additional23h; BNP first5days; mortality180days26% versus28%, HR0.91,[0.74–1.13],P0.40. Levosimendan versus dobutamine, historical.

### QP1-031 — Historical LeoPARDS

p12:0.1μg/kg/min then0.2 for20–22h; mean±SD SOFA6.68±3.96 versus6.06±3.89,P0.053; D28 mortality34.5% versus30.9%,P0.43. Historical placebo comparison.

### QP1-032 — Historical LICORN/LEVO-CTS

p12: n336/n882, prophylactic0.1μg/kg/min24h from anesthesia. LICORN composite: prolonged catecholamines, LV assist, RRT. LEVO-CTS: death,RRT,perioperativeMI,mechanical assist. Low cardiac output22% in LEVO-CTS; approximately half needed catecholamines>24h in both. No group differences stated. Historical.

### QP1-033 — Historical CHEETAH

pp12–13: LVEF<25%, high-dose inotropes/IABP;0.025–0.2μg/kg/min without loading for up to48h or ICU discharge; futility stop after506. D30 deaths32(12.9%) versus33(12.8%), absoluteRD0.1percentage points,95%CI−5.7to5.9,P0.97; mean infusion0.07μg/kg/min. This is not LEVOECMO stopping.

### QP1-034 — Historical observational ECMO results

p13: Affronti successful weaning83.3% versus27.3%,P0.498. Tafer ECMO-free days22 versus9, D30 mortality24% versus56%,P<0.05; n80,37treated. Distelmaier n240,75%treated; weaningHR0.41,95%CI0.22–0.80,P0.008; printed lower30-day adjustedHR0.52,CI0.30–0.89,P0.016 and long-term survival adjustedHR0.64,CI0.42–0.98,P0.04. Baseline EuroSCORE P<0.001,SAPS3 P0.02,LVEF P0.04. Preserve historical label wording; no trial-result counterpart.

### QP1-035 — Design

pp15–16: multicenter phaseIII, randomized double-blind placebo-controlled superiority, two arms1:1. Consecutive eligible patients proposed for inclusion. Key: design/hypothesis and patient randomization.

### QP1-036 — Allocation

[p16](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=16): centralized24h CleanWeb service; minimization probability0.8 after first20 patients allocated by balanced randomization. Balance by center and primary etiology: acuteMI,myocarditis,post-heart-surgery,other causes. Key: allocation factors/minimization and corresponding analysis adjustment; post-arrest is not separately listed among allocation factors.

### QP1-037 — Weaning thresholds

[p19](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=19): daily trial when MBP>60mmHg on no/low vasopressors and pulsatile waveform≥24h. Reduce flow to66%,33%, then1–1.5L/min. Persistent MBP<60 stops trial and restores100%flow. Weanable: aorticVTI≥12cm,LVEF>20–25%,TDSa≥6cm/s at minimal flow. Same management in both groups. Key: primary endpoint decision rule.

### QP1-038 — Drug stopping and withdrawal

pp21–22: temporary suspension/permanent drug stop ordinarily retains enrollment; premature exit death,lost follow-up or consent withdrawal. Stop drug for anaphylaxis,VF,torsades,VT or MBP<45mmHg>60min despite two500mL crystalloid boluses AND norepinephrine≥4μg/kg/min OR epinephrine≥2μg/kg/min. Existing data usable unless objection/consent restriction; p22 permits pre-exit data. SAE monitoring30days after stop and until resolved. Key: population, intervention discontinuation and safety thresholds.

### QP1-039 — Monitoring/stopping

pp22,31,34: sponsor/ANSM may stop onDSMB recommendation for SUSARs or arm differences requiring benefit-risk reassessment, new product information or unmet enrollment. All deaths extracted monthly forDSMB/safety review; mortality imbalance or above expectation can trigger urgent measures. DSMB primarily monitors safety, may monitor efficacy especially when interim analyses exist; first meeting before enrollment. No numeric efficacy boundary, efficacy-interim schedule or alpha-spending rule specified here. Key: interim/stopping rules. Administrative notification15days after cancellation.

### QP1-040 — Flow denominator records

pp16,24: eligible non-enrolled registry/reasons; consent absence, physician refusal, team unavailable/missed, another trial. p36 records included/analysed numbers, exclusion reasons, deviations, inclusion curve andCONSORT flow. Key: flow and analysis denominators.

### QP1-041 — Dose-preparation table

[p25](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=25):2.5mg/mL (printed2,5),5mL vials,3vials/box,storage+2to+8°C. [p26](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=26) table: weight40–46kg,1flask,250mL glucose,8mL/h atH1–H2 and11mL/h atH3–H24;47–89kg,2flasks,500mL,16 and22mL/h;90–132kg,3flasks,1000mL,32 and44mL/h. No explicit dose-conversion formula printed. Key: delivered intervention dose/duration/units.

### QP1-042 — Common management targets

pp26–27: flow3.5–5L/min; PaO2 65–90mmHg or arterial saturation>90%; PaCO2 40–45mmHg; perfusionist at least every48h. aPTT55–70sec or antiXa0.4–0.6IU/mL; free hemoglobin every48h. Transfusion threshold9–10g/dL, possibly7–8 if stable without myocardial ischemia; platelet<20G/L or severe thrombopenia with bleeding. Key: common management/endpoint context, no observed trial estimates.

### QP1-043 — Concomitant treatment and efficacy period

pp26–27: other inotropes permitted, dobutamine preferred; open-label levosimendan prohibited throughout study; p27 also excludes digoxine among additional inotropes. Physician assures24h infusion compliance. Efficacy evaluation randomizationD1 throughD60. Key: intervention duration/contamination and follow-up.

### QP1-044 — Safety labels and thresholds

pp28–33: AE need not be causal, AR is causal; serious death/life-threat/hospitalization/prolongation/disability/congenital abnormality; unexpected against reference information. p29 severity mild/moderate/serious by daily-activity impact; WHO-UMC causality certain/probable/possible/unlikely. Table footnotes: all points reasonably complied with; drug intake or study procedures. p30 while onECMO only treatment-related deaths require immediate notification; VF/torsades/VT exempt from immediate notification onECMO, but notified immediately after weaning along with refractory hypotension(QP1-038). Natural-course deaths/ICU-relatedSAEs remain recorded. p31 drug effects include hypotension grades1/2,<30%MAP decrease; moderate tachycardiaHR<110bpm; hypokalemia3–3.5mmol/L; premature ventricular/atrial contractions,AF,nausea,vomiting,diarrhea,constipation,dizziness,headache,insomnia. Events monitored until resolution. Regulatory nonfatal SUSAR15days, additional reports8days, annualDSUR within60days of authorization anniversary. Key: safety ascertainment, with regulatory timing administrative.

### QP1-045 — Statistical overview

[p35](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=35): all comparisons two-sided typeI error5%. Descriptives overall/bygroup. Comparative analyses systematically unadjusted and adjusted for baseline prognostic factors potentially imbalanced, model appropriate to variable type/distribution. Qualitative n/%; quantitative n,mean,SD,95%CI mean,median,range,IQR. Censored KM/cumulative incidence and15/30/60day rates with95%CIs where appropriate. SAS/R latest version at analysis. Key: alpha/sidedness, adjustment and summary definitions; no named required prognostic covariate here.

### QP1-046 — Populations and missingness

[p36](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=36): ITT all randomized except consent withdrawal requesting no analysis. [p38](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=38): principal ITT original randomized group, all data regardless treatment changes. pp36,38 detailedSAP validated by scientific committee; modifications before database unblinding and committee validation. p39 codes missingCRF data and retains audit trail. No quantitative imputation algorithm or missingness assumption specified in assigned pages. Lost-follow-up censoring and retained early-exit data above; no replacementp37. Key: ITT denominator, consent exception, missing data andSAP timing.

### QP1-047 — Inferential models and sample-size inputs

[p37](../../../../joi250087supp1_prod_1766516490.96011.pdf#page=37): primary cumulative incidence at15/30days with95%CIs. Fine–Gray group comparison/prognostic adjustment; subdistributionHR with95%CI. Schoenfeld residuals for proportional hazards; loglinearity of quantitative covariates studied. Cumulative incidence plotted nonparametrically or from model. Secondary qualitative χ², correctedχ² orFisher, logistic model for adjustment/exploratory; quantitative Student t-test (printed twice) or Mann–Whitney–Wilcoxon, linear regression adjustment. Mortality KM with95%CI only within60days, time from randomization to death regardless prior weaning, censor at latest news/end60days; logrank comparison andCox adjustment. Sample size: control successful-weaning cumulative incidence50% with competing death/weaning failure, based on30day cohort; target subdistributionHR1.75,alpha5%,power80%,101successful-weaning events,206subjects=103/arm. Latouche etal[38], p46 citation2004 StatMed23:3263–3274. No explicit formula or further censoring/competing-incidence inputs printed. No replacements; two-sided5% reiterated. No explicit multiplicity family/hierarchy, adjusted secondaryalpha, sensitivity specification or formal interim boundary in assigned original protocol. Outcomes listed as secondary, none explicitly key secondary. Keys: primary Fine–Gray/sHR, secondary model/test identity, power/sample size, alpha and multiplicity/interim rules.

## Closure and limitations

Every assigned protocol, administrative and bibliography page was opened. No LEVOECMO observed-result table/figure occurs here. Historical data remain historical. Applicable tables were summarypp7–10, consentp18, schedule/standard-carepp20–21, recruitmentp24, preparationp26 and causalityp29; all content relevant to result matching is mapped. No Office formulas/cached values, trial sensitivity result displays or result figures occur. The sole transcription uncertainty is administrative handwriting onp4, not a result-relevant quantity. Fresh native-text absence onpp4,49 was resolved by direct rendering and visual mapping; no scientific coverage gap remains.
