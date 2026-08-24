# Fresh Support Quantitative Map — DOC-002

## Scope and method

- **Source:** `joi180015supp1_prod.pdf` (protocol 005, version date 23 February 2011), PDF pp. 1-37.
- **Fresh evidence used:** direct PDF page extraction with `pdftotext -layout`; visually prepared table pages in `preprocessing/rendered_pages/DOC-002-p7.png` through `DOC-002-p30.png` were used to retain table structure. Native/layout text was readable; no OCR was needed.
- **Mapper-local handles:** `D2-Nxx` are numeric/reporting relationships; `D2-Sxx` are statistical/inferential relationships. They are local handles only, not global `N`/`S` IDs. A handle can group repeated instances of the same explicitly matched protocol quantity.
- **Scope result:** pp. 1-30 contain result-relevant planned outcomes, definitions, assumptions, tables, or supporting performance data. pp. 31-37 are reference-list continuation only; no result-relevant protocol relationship is present there.
- **Candidate status:** all items below are extraction/mapping records, not adjudications. Candidate leads are kept separate and have no disposition.

## Trial frame, populations, timing, and principal quantities

| Local handle | PDF page(s) | Printed evidence / relationship | Reproducible identity, population, time, scale, or unit |
|---|---:|---|---|
| D2-N01 | 1, 7-10, 15 | Cluster randomised Bedside-PEWS trial; **22 hospitals**; hospital-level allocation, balanced 1:1 within bed-size strata (<200 vs >=200 eligible ward beds). | Cluster = participating hospital; eligible patients are >37 weeks gestation and <18 years, admitted to eligible inpatient wards; intervention is ward documentation/care system and control is standard care. |
| D2-N02 | 1, 9-10 | Outcomes assessed 18 months: **6 months/26 weeks baseline + 12 months/52 weeks intervention = 78 weeks**; intervention begins 7 months/31 weeks after baseline start, after a 5-week run-in. | Same calendar assessment length in each arm; hospital-level baseline and post-randomisation comparison. |
| D2-N03 | 1, 10 | Primary outcome: all-cause hospital mortality among eligible inpatients who were cared for in an eligible ward during the stay; includes deaths with DNR orders. | Excludes deaths exclusively in PICU/NICU/emergency department; measure is a death proportion/rate with hospital as analysis cluster. |
| D2-N04 | 1, 10-12, 24 | Main secondary outcome: Significant Clinical Deterioration Event (SCDE): significant respiratory/circulatory therapy or CPR in 12 h before transfer or 1 h after transfer, or ward death without DNR. | Composite; transfer is ward-to-PICU; excludes pre-existing DNR. Table 5 supplies its seven-point treatment/death classification. |
| D2-N05 | 1, 11-13 | Additional clinical outcomes: resuscitation intensity, potentially preventable cardiac arrest, unplanned hospital/PICU readmission within 48 h, PIM predicted mortality, PICU mortality, PELOD, and 28-day ventilator-free days. | PICU subgroup is urgent admissions from a ward; readmissions and mortality are represented per 1,000 hospital discharges. |
| D2-N06 | 1, 12-14, 16 | Process outcomes: stat calls, code blue calls, urgent ICU/MET-RRT consultations, vital-sign documentation, staff perceptions. Resource outcomes: hospital/PICU LOS and ventilation, dialysis, ECMO, plasmapheresis and nitric-oxide days. | Call/event rates are per 1,000 patient-days; documentation sample = five centrally randomised patients/week and preceding 24 h. |
| D2-N07 | 1, 14-15 | Planning mortality target: baseline **5.1/1,000**, 18% relative risk reduction (RRR), 0.9 deaths/1,000 stated absolute reduction, k=0.15, power 0.8/80%, two-sided alpha=0.05, 20 hospitals; planned 22 allowing 1-2 losses. | Mortality sample-size assumptions; k is stated as between-hospital coefficient of variation. Related power-appendix versions are mapped at D2-N32-D2-S18. |

## Outcome and measurement definitions

| Local handle | PDF page(s) | Printed evidence / relationship | Reproducible rule |
|---|---:|---|---|
| D2-N08 | 11, 24 | Children’s Resuscitation Intensity Scale has seven ordered categories: early transfer; intermediate transfer; respiratory; circulatory; late transfer; CPR; death. SCDE=No for categories 1-2 and Yes for 3-7. | Table 5 is the defining table; individual criteria appear below. |
| D2-N09 | 24 | Early transfer: <60 mL/kg IV/IO fluid in 12 h before transfer, no IV/IO inotrope/vasoactive medication and no positive-pressure ventilation in those 12 h. Intermediate: non-invasive positive-pressure ventilation in 12 h, not intubated at transfer; scheduled-procedure anaesthetic ventilation excluded. | Categories 1-2, SCDE=No. |
| D2-N10 | 24 | Respiratory: intubated or endotracheally ventilated at transfer, or intubated within 1 h after PICU admission. Circulatory: >60 mL/kg IV/IO fluid in 12 h plus any IV/IO inotrope/vasopressor at transfer or in preceding 12 h; may include positive-pressure ventilation. | Categories 3-4, SCDE=Yes. Units explicitly mL/kg and hours. |
| D2-N11 | 24 | Late transfer = respiratory plus circulatory support before transfer. CPR = chest compressions before ward departure or within 1 h after PICU admission, or ECMO before/within 1 h. Death = ward death without DNR (including death despite/intended CPR). | Categories 5-7, SCDE=Yes. |
| D2-N12 | 10-12, 24 | Urgent PICU admission: departure from event location <6 h after admission initiation; initiation is confirmed admission or definite possible post-surgical PICU need. OR-initiated PICU admissions are urgent irrespective of delay. | For a ward-to-OR-to-PICU path, transfer clock starts at ward-to-OR departure; unexpected OR events not anticipated for PICU at ward departure are not clinical deterioration events. |
| D2-N13 | 11-12, 28 | Potentially preventable cardiac arrest: ward arrest without preceding DNR, described on p.11 as Children’s Resuscitation Intensity Scale 6 or 7; independently rated 1-6. Consensus rating >4 on p.11 (then lists 4,5,6 as qualifying), and Table 7 says rating >=4 is high preventability. | Two blinded physician reviewers; discordance discussion, then third reviewer (>10 years paediatric hospital practice) if needed; report pre-discussion kappa. Express event rate per 1,000 patient-days. |
| D2-N14 | 12 | Hospital readmission and PICU readmission: within 48 h, operationalised as before midnight of second complete day/third midnight after discharge. | Hospital/PICU mortality and unplanned readmission represented per 1,000 hospital discharges. |
| D2-N15 | 12, 15 | Ventilator-free days = days alive and without invasive ventilation in 28 days from PICU admission, recorded for first PICU admission in each period; discharge within 28 days assumed alive and not ventilated. | Excludes re-admission from ventilator-free-day calculation to avoid double counting. |
| D2-N16 | 12-14 | Patient day = any presence in designated area during a 24-h day (00:00-23:59); hospital days exclude PICU/NICU; ICU days include whole/part PICU days. | End of baseline/intervention treats patients as hospital-discharged. |
| D2-N17 | 12-14 | Five random patients/week: count HR, RR, SBP, temperature, transcutaneous O2 saturation, respiratory effort, oxygen therapy, capillary refill measurements in preceding 24 h; also physician visits, nurse:patient ratio and continuous monitoring. | Staff survey administered at baseline month 2 and months 3 and 9 after randomisation begins. Five percent of randomly selected ICU records compared to source data. |

## Statistical and analysis-plan map

| Local handle | PDF page(s) | Printed statistical definition | Population/contrast/model/output |
|---|---:|---|---|
| D2-S01 | 1, 16 | Descriptive/unadjusted data: mean, median, variance, IQR or proportions with 95% CIs; report baseline and intervention periods for each hospital. | Cluster trial; baseline event rates use six months prospective data. |
| D2-S02 | 1, 16 | Primary mortality: logit regression. Dependent variable = logit(proportion dying) in each hospital. Predictors = treatment-arm dummy, baseline mortality logit, hospital-size stratum; weighted by hospital size. | Effect contrast: Bedside-PEWS vs standard care after baseline and stratum adjustment. |
| D2-S03 | 16 | Same logit model for ICU mortality after urgent ward-initiated PICU admission, ICU mortality after OR-initiated urgent PICU admission, unplanned hospital readmission within 48 h, and all-cause mortality following DNR. | Hospital-level outcomes, treatment dummy/baseline logit/size stratum, hospital-size weighting. |
| D2-S04 | 1, 16 | Poisson regression using hospital-level aggregated count data for SCDE, code blue, stat calls and urgent ICU consultation per 1,000 patient-days. Predictors = treatment dummy, baseline event rate, hospital-size stratum. | Rate/count outcomes; supplied denominator=patient-days. |
| D2-S05 | 16 | Linear regression on within-hospital mean for resuscitation-intensity nature, ward patient-days, PIM2, PELOD, ventilator-free days, ICU-patient days, and therapy days (ventilation, ECMO, dialysis, plasmapheresis, nitric oxide). | Predictors=arm dummy, baseline mean, size stratum; weighted by hospital size. |
| D2-S06 | 16 | Documentation: identical linear model but no weighting because equal records per hospital; compares number of seven named vital-sign items/all-seven-item documentation. Further linear models compare vital signs, physician visits, nurse:patient ratio, continuous ECG and pulse-ox monitoring with calculated PEWS scores. | Adjust baseline event rates and strata; exact model of calculated-score relationship not further specified. |
| D2-S07 | 16-17 | Surveys descriptive; between-group comparisons via hospital-size-weighted linear regression. A-priori subgroups: >=200 vs <200 eligible beds; MET-RRT yes/no; paediatric ECMO yes/no; urgent ward-initiated PICU admission. | One outcome analysis only; no interim analysis. Exploratory relation of education survey to documentation/interaction survey and documentation review. |
| D2-S08 | 7-9 | Allocation: concealed until study measurements begin; revealed in week 2; half in each size stratum allocated to intervention. Analytic team blinded to allocation; outcomes site coordinators not blinded. | Randomisation unit hospital; two strata defined by <200 vs >=200 eligible ward beds. |
| D2-S09 | 7-8 | Training fidelity: competence requires ICC >0.90 and no score >2 points different from electronic gold standard after 10 vital-sign sets across three scenarios. | Historical observed ICC 0.92 educator/new staff; 0.90 for 786 repeated real-patient scores; one score >2 points different. |
| D2-S10 | 8 | Run-in weekly audit: minimum 40 12-h documentation periods; aims are >80% calculated scores within 2 points, >5/7 items in >80% of scored records, and >80% of patients within recommendation frequency. | Four days/week from second implementation week, review latest 12 h in 10-15 random patients/day. |
| D2-S11 | 11-12 | Cardiac-arrest preventability: independent two-reviewer ratings; consensus procedure; pre-discussion Cohen-type kappa stated but calculation conventions not supplied. | Six-level scale; rate per 1,000 patient-days. |

## Supporting performance/background numerical evidence

| Local handle | PDF page(s) | Printed values and labels | Relationship / limitation |
|---|---:|---|---|
| D2-N18 | 1, 4-5 | Bedside-PEWS: 7 items, score 0-26; original score 16 items. Single-centre score AUROC 0.91, sensitivity 83%, specificity 95% at score 8; summary says identified 82% with >=1 h notice. Multi-centre: 2,074 patients/4 hospitals, AUCROC 0.87. | Performance evidence, not trial outcome. P1 says ICC 0.92; p5 gives frontline survey 96%/98 and 97%/98; 280 professional survey (80 community, 200 referral). |
| D2-N19 | 2-4 | Background: arrest 0.1-20/1,000 ward children; hospital survival 30-50%; nearly 5,000 annual Canadian/US ward code-blue events; mortality 28% after code blue vs 14% urgent ICU before code blue; >80% identifiable >=1 h. | Historical/contextual quantities; causal comparability not defined. |
| D2-N20 | 3-4 | Adult MET RCT: 120,000 patients/23 hospitals, calling criteria <50% in urgent ICU, about 90% meeting criteria referred. Other adult ward study: 16 wards, 800-bed hospital, 32 weeks, mortality OR 0.52 (95% CI 0.32-0.85). | External background only. |
| D2-N21 | 4-6 | Melbourne: 10/24 (42%) arrest cases identified; 40% of 150 Ontario code-blue events had preceding activation. Brighton external cohort 2,979 children, 51 PICU transfers, AUC 0.89/sensitivity 78%/specificity 82% at threshold 5. Cardiff AUC 0.86/sensitivity 69%/specificity 90% at threshold 2. | Supporting score-performance summaries. |
| D2-N22 | 6, 21 | Systematic review search retrieved 1,069 references; one additional Brighton study; Ovid MEDLINE 1950-present updated 8 Sep 2009; Cochrane rerun found four reviews, one relevant. | Search table records sets 1-5 and all-child (0-18y) limit. |

## Table 1 — score/calling-criteria entries (p.19)

| Local handle | Origin; instrument | Printed score/triggers, development, threshold; operating values |
|---|---|---|
| D2-N23 | Bristol 2005 | 10 triggers +3 diagnosis-related criteria + staff concern; expert opinion; sensitivity 99%, specificity 63%; ICU threshold >1 criterion; AUCROC 0.52. |
| D2-N24 | Brighton 2005 | Score 0-11, 7 items; expert opinion (Tucker 2009); sensitivity 71%, specificity 91%; threshold score >5; AUCROC 0.53. |
| D2-N25 | Toronto 2006 | Score 0-26, 9 static +7 dynamic; Delphi consensus/statistical item selection; sensitivity 78%, specificity 95%; threshold >5; AUCROC 0.87. |
| D2-N26 | Melbourne 2006 | 8 triggers + concern; expert opinion; no sensitivity/specificity; threshold >1 criterion; AUCROC 0.73. |
| D2-N27 | Cincinnati 2007 | 4 subjective triggers + staff/parental concern; expert review local data; no sensitivity/specificity; threshold >1 criterion; AUCROC NA. |
| D2-N28 | Baltimore 2008 | 8 subjective items, two arrest types + concern; expert opinion; no sensitivity/specificity; threshold >1 criterion; AUCROC NA. |
| D2-N29 | Cardiff 2009 | Score 0-8, 7 items; expert consensus; sensitivity 70%, specificity 90%; suggested threshold >2; AUCROC 0.62. |
| D2-N30 | Bedside PEWS 2009 | Score 0-26, 7 items; expert opinion/statistical item reduction; sensitivity 82%, specificity 93%; threshold >8; AUCROC 0.87. |

Table 1 footnote evidence: objective components evaluated in **2,074 patients at 4 hospitals**. Heart-rate range >20 bpm: **86% case, 40% control**; >30 bpm: **74% case, 22% control**. Respiratory-rate range >20 breaths/min: **57% case, 7% control**; >30: **34% case, 3% control**. Age ranges used for operationalisation: <3 months, 3-12 months, 1-4 years, 5-12 years, >12 years. `AUCROC` explicitly means area under receiver operating characteristics curve.

## Table 2 — Bedside-PEWS performance entries (p.20)

**Handle D2-S12.** Table columns are control N/median score (IQR), case N/median score (IQR), P value, and AUCROC (95% CI); all rows compare control with case patients. `IQR`=interquartile range.

| Category | Control | Case | P; AUCROC (95% CI) |
|---|---:|---:|---|
| All | 1,388; 2 (1-4) | 686; 8 (5-12) | <.0001; 0.87 (0.85-0.89) |
| Urgent ICU | 772; 2 (1-4) | 381; 10 (7-13) | <.0001; 0.92 (0.90-0.94) |
| Code Blue | 616; 2 (1-4) | 305; 6 (3-10) | <.0001; 0.81 (0.78-0.84) |
| <3 months | 333; 2 (1-4) | 190; 7 (4-10) | <.0001; 0.83 (0.79-0.86) |
| 3-<12 months | 362; 2 (1-4) | 164; 8 (6-11) | <.0001; 0.86 (0.82-0.90) |
| 1-<5 years | 286; 2 (1-4) | 134; 9 (5-13) | <.0001; 0.90 (0.87-0.93) |
| 5-12 years | 221; 2 (1-3) | 110; 10 (5-13) | <.0001; 0.89 (0.84-0.93) |
| >12 years | 186; 3 (2-4) | 88; 11 (6-14) | <.0001; 0.91 (0.87-0.95) |
| Hospital 1 | 658; 2 (1-4) | 324; 9 (6-12) | <.0001; 0.88 (0.85-0.90) |
| Hospital 2 | 478; 1 (1-3) | 238; 6 (4-9) | <.0001; 0.89 (0.86-0.92) |
| Hospital 3 | 164; 5 (2-6) | 80; 12 (9-15.5) | <.0001; 0.91 (0.87-0.95) |
| Hospital 4 | 88; 2 (1-3) | 44; 9 (4-12) | <.0001; 0.89 (0.83-0.96) |
| Transplant | 73; 2 (1-3) | 58; 11 (7-12) | <.0001; 0.94 (0.90-0.98) |
| Heart disease | 386; 3 (2-5) | 233; 8 (6-11) | <.0001; 0.84 (0.81-0.88) |
| Severe cerebral palsy | 34; 2 (1-4) | 62; 10 (7-13) | <.0001; 0.92 (0.86-0.98) |
| Tracheostomy | 36; 4 (1.5-5.5) | 57; 7 (4-11) | <.0001; 0.76 (0.67-0.86) |
| Feeding tube | 112; 3 (1-5) | 138; 10 (6-13) | <.0001; 0.86 (0.82-0.91) |
| Home oxygen | 27; 5 (2-7) | 47; 8 (6-11) | <.0001; 0.79 (0.69-0.90) |
| Seizures >15 min | 6; 2 (2-4) | 47; 6 (3-10) | 0.1146; 0.74 (0.48-0.99) |
| >3 services | 136; 3 (1-5) | 164; 9 (6-12) | <.0001; 0.87 (0.83-0.91) |
| >10 medications/day | 109; 3 (2-5) | 162; 10 (6-13) | <.0001; 0.85 (0.81-0.90) |
| Recent primary-service transfer | 5; 1 (0-2) | 18; 7 (3-8) | 0.0040; 0.89 (0.75-1.00) |

Internal count checks recorded for later review: All controls = 772+616 = 1,388 and all cases =381+305=686; hospital control/case subtotals also sum to 1,388/686. Disease/device rows overlap and are not expected to sum.

## Tables 3-7 and implementation/measures details

| Local handle | PDF page(s) | Mapped quantitative/definition entries |
|---|---:|---|
| D2-N31 | 22-23 | Table 4 implementation: phase 1/2 4-8 months pre-implementation; phase 3 two-day course 2-4 months pre-frontline education; phase 4 1-3 months pre-education; phase 5 4 h frontline session over 3 months (2 h small-group, 6-8 people/educator, 2 h interactive) and physician 90-min session; phase 6 >=20-bed ward 5 weeks before go-live; phase 7 hospital-wide implementation. |
| D2-N32 | 25-27 | Table 6 abstraction: age in months if <1 y else years; 9 severity markers; recent procedure list (14 categories, with duplicated printed code 2 for cardiac without bypass and catheterisation); medications in 25 h before event plus administration hour; vital/respiratory/circulatory data from 13 h before event; infection samples from prior 96 h; summary <300 words. Lab windows: closest to 48 h and >24 h; closest to 12 h with <24/>12 h; closest to 1 h with <12/>1 h; number of tests <24/>1 h; record normal limits. |
| D2-N33 | 26 | Vital signs: HR, RR, SBP, DBP, transcutaneous O2 saturation, capillary refill, respiratory effort, temperature, consciousness (GCS/Comfort), pupils. Fluid total mL/kg averaged hourly; vasoactives yes/no (dopamine, milrinone, amrinone, norepinephrine, epinephrine, prostaglandin); radiology lookback 48 h. |
| D2-N34 | 28 | Table 7 rating scale: 1 virtually no evidence, 2 slight/modest, 3 not quite likely (<50/50 close call), 4 more than likely (>50/50 close call), 5 strong, 6 virtually certain. Table legend: >=4 high degree of preventability. |

## Power/sample-size appendix and arithmetic map

| Local handle | PDF page(s) | Printed values | Reproducible relationship |
|---|---:|---|---|
| D2-S13 | 14-15, 29 | Mortality calculation: 20 hospitals, alpha .05 two-sided/z=1.96, 80% power, mean beds 119 (p14) or 119.85 (p29), LOS 4 days, occupancy .90, k .15, baseline 5.1/1,000. | Published Hayes-Bennett cluster calculation stated; output: 18% RRR. |
| D2-N35 | 29 | Fourteen listed hospital mortality rates per 1,000 discharges: 2.17, 5.0, 5.08, 6.8, 2.1, 8.4, 7.22, 2.07, 6.98, 7.0, 4.46, 6.5, 2.31, 5.4; printed overall average **5.11**. | Simple unweighted sum/14 = 5.107... -> 5.11; labelled average. |
| D2-N36 | 29 | External reference cohort: 8 years, Pennsylvania hospitals 1994-2001, 678,365 subjects, 2,202 in-hospital deaths, 3.2/1,000. | 2,202/678,365*1,000 = 3.246 -> 3.2/1,000. |
| D2-S14 | 29 | Appendix reports RRR .178 at baseline 5.1/1,000 and .199 at baseline 3.2/1,000. | Under multiplication, .178*5.1=0.9078/1,000 and .199*3.2=0.6368/1,000. |
| D2-N37 | 14, 30 | SCDE planning: 2,322 beds, 99,389 admissions, 397,556 patient-days (LOS 4); source data stated as 1,052 urgent PICU admissions/year from four hospitals, estimated 40% SCDE, stated rate 2/1,000 patient-days. | 99,389*4 =397,556 exactly. SCDE rate formulation needs exact time/site denominator confirmation when rechecked. |
| D2-S15 | 14-15, 30 | 20 sites; SCDE 31% reduction; alpha .05 two-sided, power 80%, k .15; stated absolute reduction .62 events/1,000 patient-days. | At stated baseline 2/1,000, .31*2=.62/1,000. |
| D2-N38 | 30 | Four-hospital 2007-08 table: 55,963 hospital admissions; 62 PICU beds; 7,300 PICU discharges; 1,052 unplanned PICU admits (14.5% of PICU discharges; 18/1,000 hospital discharges); 65 PICU deaths after unplanned admits (6.2%; 1.2/1,000 hospital discharges); 150 code-blue events (3/1,000 discharges; .75/1,000 patient-days). | Checked rounded identities: 1,052/7,300=14.41%; 1,052/55,963*1,000=18.80; 65/1,052=6.18%; 65/55,963*1,000=1.16; 150/55,963*1,000=2.68. |
| D2-S16 | 30 | Code-blue planning: baseline .75/1,000 patient-days, max RRR .41 at 20 referral hospitals, alpha .05, z 1.96, power 80%, beds 119.85, LOS 4, k .15; stated ARR .3/1,000. | .41*.75=.3075/1,000, consistent with rounded .3. |
| D2-S17 | 30 | Stat-call planning: Poisson regression; baseline 8.13/1,000 patient-days; max RRR .181, alpha .05, z 1.96, power 80%, beds 119.85, LOS 4, k .15, n=20; stated ARR 1.45/1,000. | .181*8.13=1.4715/1,000, consistent with rounded 1.45 at displayed precision. |

## Candidate leads for coordinator registration/recheck (no disposition)

1. **D2-LEAD-01 — mortality ARR unit/size conflict.** PDF p.1 calls the 18% mortality RRR an absolute reduction of **0.9 deaths/1,000**; p.14 calls it **0.09%** (also 0.9/1,000); p.29 instead says the same 18% RRR “corresponds to an absolute risk reduction of **0.9%**.” With baseline 5.1/1,000 and appendix RRR .178, multiplication gives 0.9078/1,000 (=0.09078%), not 0.9%. Exact human question: is p.29’s `0.9%` a percent/unit transcription error, or does it refer to another unstated population/denominator?
2. **D2-LEAD-02 — resuscitation-scale category conflict.** Table 5 p.24 places cardiopulmonary resuscitation at category 6 (and ward death at 7), while p.11 explicitly calls cardiac arrest “rated as 6 or 7”; p.27’s Table 6 legend instead says clinical-deterioration events including cardiac arrest are “scale rating 4 or 5.” Exact human question: do the p.27 `4 or 5` labels intend a different scale or conflict with the Table 5 scale used in the same protocol?
3. **D2-LEAD-03 — preventability threshold wording.** P.11 says events with consensus rating “at **>4**” are potentially preventable, but immediately includes ratings **4, 5, and 6**; Table 7 p.28 says rating **4 or more** is high preventability. Exact human question: is the operative threshold >=4 or >4?
4. **D2-LEAD-04 — SCDE/reference data time-denominator alignment.** P.14 describes **1,052 urgent ICU admissions/year** from four hospitals and uses a 40% SCDE estimate/rate 2/1,000 patient-days. P.30 says its 55,963-discharge/1,052-admission/150-code-blue data represent **two years** following 31 January 2007. Exact human question: which stated time period and denominator supplies the 1,052 and the SCDE 2/1,000 rate? No arithmetic inconsistency is asserted until those identities are matched.

## Explicit no-applicable coverage

- PDF pp. 31-37: references only; no result-relevant protocol numeric, statistical, table, outcome, scale, or comparison item to map.
- No formula-bearing workbook/CSV/Office source, cached formula value, or external source was in this assigned document scope.
- No display-zero P-value was found in DOC-002; Table 2 uses `<.0001`, which is a threshold display and is not a candidate basis.
