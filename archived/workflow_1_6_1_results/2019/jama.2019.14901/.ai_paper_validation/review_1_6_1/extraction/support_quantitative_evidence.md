# Support quantitative evidence map

Fresh support mapper runtime: `01a128dd-1b8f-7d40-98dd-4089fca540b7`. Assigned scope: DOC-002 PDF pp.1–48 (PLAN), DOC-003 PDF pp.1–9 (REPORT), DOC-004 PDF p.1 (administrative REPORT). All 58 pages inspected; 57 reusable-backed pages and one fresh-required page mapped. No source or reusable asset modified, no historical scientific conclusions read, no web used. The keys below are local relationship groups; every row in their attached transcription belongs to the group and is included in review scope. They do not diagnose candidates.

## Methods and derivative provenance

Page-specific reusable native/layout text used for DOC-002 pp.1–48 from `.ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-002-protocol_page-NNN.txt`, DOC-003 pp.1–9 from `.ai_paper_validation/document_outputs/DOC-003-results-supplement/preprocessing/native_text/page-NNN.txt`, and DOC-004 p.1 from `.ai_paper_validation/review_1_5_1/preprocessing/native_text/DOC-004-data-sharing-statement_page-001.txt`. Source identity and current native/layout agreement were established by curator. Their detailed fitness and hashes remain in the new evidence-asset inventory; derivatives are transcription aids, not authority for candidate confirmation.

Fresh-required DOC-002 p.42 was directly extracted, rendered and visually inspected in full. Direct Poppler 26.01.0 commands:

```sh
pdftotext -layout -f 42 -l 42 joi190108supp1_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/support/protocol-p42-layout.txt
pdftoppm -f 42 -l 42 -singlefile -r 180 -png joi190108supp1_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/support/protocol-p42
tesseract .ai_paper_validation/review_1_6_1/preprocessing/support/protocol-p42.png .ai_paper_validation/review_1_6_1/preprocessing/support/protocol-p42-ocr -l eng --psm 6
```

Outputs are respectively `preprocessing/support/protocol-p42-layout.txt`, `preprocessing/support/protocol-p42.png`, and `preprocessing/support/protocol-p42-ocr.txt`, relative to the review directory. OCR engine Tesseract 5.5.0 CPU. Native extraction contains heading/footer only; the embedded form is visually readable. OCR misreads inequalities and omits form cells; English manual transcription below uses the image, preserving its printed thresholds. No fallback environment or GPU. Reusable DOC-003 p.4 and p.9 images were viewed in full; renderer/version is not recorded in their legacy metadata and is not inferred.

## Complete page coverage

| Source | PDF page | Mapped content / applicability |
|---|---:|---|
| DOC-002 | 1 | Protocol title, version 4, 17 October 2017; no result values. |
| DOC-002 | 2 | Trial protocol identity and approval 20 September 2016; no applicable results. |
| DOC-002 | 3 | Contents: primary/secondary outcome and eligibility locations; no independent result. |
| DOC-002 | 4 | Contents: treatment, follow-up, statistics, subgroup and sample-size locations. |
| DOC-002 | 5 | Contents: benefits and appendices; no independent result. |
| DOC-002 | 6 | Signatures dated 17 October 2017; no applicable quantitative relationship. |
| DOC-002 | 7 | Abbreviations, physiological units and scale names; no outcome result. |
| DOC-002 | 8 | Synopsis background: mortality 25–50%, reintubation overall 15%, high-risk 20–25%; background only. |
| DOC-002 | 9 | Synopsis primary day-7 endpoint and six secondary outcome families. |
| DOC-002 | 10 | Synopsis secondary mortality, eligibility, cardiac/lung definitions. |
| DOC-002 | 11 | Synopsis exclusions, planned N=650, duration 36 months recruitment/3 months participation/51 months total with 39 study+12 analysis. |
| DOC-002 | 12 | Responsibilities and sponsor contacts; no applicable relationship. |
| DOC-002 | 13 | Investigator/statistician/scientific committee; no applicable relationship. |
| DOC-002 | 14 | Rationale: 30–50% mortality, 15% overall failure, high-risk 20–25%; historical evidence only. |
| DOC-002 | 15 | Historical trial numbers and effects, mapped below; not current-trial results. |
| DOC-002 | 16 | HFNC rationale and historical literature; no current-trial effect estimate. |
| DOC-002 | 17 | Full six-study historical Table 1; endpoint day-7 rationale. |
| DOC-002 | 18 | Risk-factor rationale, historical >30% vs <10% failure and PaO2/FiO2 <200 mm Hg; no current result. |
| DOC-002 | 19 | Preliminary cohorts and risk estimates; treatment minimum 48h rationale. |
| DOC-002 | 20 | Innovation/equipoise: intubated >24h, age >65, approximately half eligible, hypercapnia 15%, NIV practice 20%; bibliography begins. |
| DOC-002 | 21 | Bibliography entries 6–19; no applicable current relationship. |
| DOC-002 | 22 | Bibliography entries 20–34; no applicable current relationship. |
| DOC-002 | 23 | Bibliography entries 35–50; no applicable current relationship. |
| DOC-002 | 24 | Bibliography entries 51–56; no applicable current relationship. |
| DOC-002 | 25 | Primary and all six secondary objective/outcome families. |
| DOC-002 | 26 | All eligibility and ten exclusion criteria. |
| DOC-002 | 27 | Recruitment flow and weaning readiness. |
| DOC-002 | 28 | Weaning test settings/duration, pre-extubation blood gas. |
| DOC-002 | 29 | Randomization strata/allocation, HFNC control and withdrawal/weaning treatment. |
| DOC-002 | 30 | NIV treatment, duration, acute respiratory failure and start of reintubation definition. |
| DOC-002 | 31 | Remaining reintubation criteria, rescue NIV rule and baseline/H1 collection. |
| DOC-002 | 32 | H6/H12–24/H24–48/day3–7/day14/ICU/day90 collection and durations/N. |
| DOC-002 | 33 | ITT and all main/secondary statistical specifications. |
| DOC-002 | 34 | Mortality/subgroup analyses, power/sample size and expected intervention rate. |
| DOC-002 | 35 | Expected control rate and historical basis. |
| DOC-002 | 36 | Data management and monitoring; no additional statistical decision rule. |
| DOC-002 | 37 | eCRF/source checking, intercurrent events at end, 15-year archiving; no additional statistical method. |
| DOC-002 | 38 | Ethics, registry, amendments approved by ethics committee; no statistical stopping rule. |
| DOC-002 | 39 | Confidentiality/publication and feasibility historical FLORALI N=300; no current result. |
| DOC-002 | 40 | Feasibility ~8 eligible/center/month, expected 1 inclusion/center/month; benefits, background NIV 10%; no new analysis rule. |
| DOC-002 | 41 | Complete schedule table mapped below. |
| DOC-002 | 42 | Fresh direct image: weaning form; all thresholds, cells and decision sequence mapped below. |
| DOC-002 | 43 | Helsinki history/preamble/general principles 1–5; not trial-specific quantitative evidence. |
| DOC-002 | 44 | Helsinki principles 6–15; not trial-specific quantitative evidence. |
| DOC-002 | 45 | Helsinki principles 16–22 including generic risk monitoring; no trial-specific interim or stopping boundary. |
| DOC-002 | 46 | Helsinki trial access/ethics/privacy/consent 23–26; no trial-specific quantitative relationship. |
| DOC-002 | 47 | Helsinki consent 27–32/placebo heading; no trial-specific quantitative relationship. |
| DOC-002 | 48 | Helsinki placebo/access/registration/publication/practice 33–37; no trial-specific quantitative relationship. |
| DOC-003 | 1 | Contents of all five eTables and survival eFigure. |
| DOC-003 | 2 | eTable 1: every respiratory-failure/criterion/reintubation-cause row and P value. |
| DOC-003 | 3 | eTable 2 admission/eligibility/extubation characteristics, all four groups and P values. |
| DOC-003 | 4 | eTable 2 ventilator/weaning rows, exact numerator/denominator pairs and P values. |
| DOC-003 | 5 | All eTable 2 footnotes: SAPS II, overlapping disease, SOFA and weaning definitions. |
| DOC-003 | 6 | eTable 3: all hypercapnic primary/secondary rows, estimates, intervals and P values. |
| DOC-003 | 7 | eTable 4: all nonhypercapnic primary/secondary rows, estimates, intervals and P values. |
| DOC-003 | 8 | eTable 5: every center 1–30 and total, three numerator/denominator/percentage columns. |
| DOC-003 | 9 | eFigure: directly inspected reusable full image, axes/legend/P/risk counts mapped below. |
| DOC-004 | 1 | Administrative data sharing: data available No; no applicable quantitative result or analysis specification. |

## Numeric relationship groups

| Local key | Role/source page | Complete relationship and matching main-paper key |
|---|---|---|
| U-N001 | PLAN DOC-002 pp.9–10,25 | Primary reintubation within 7 days after planned extubation; compare main primary outcome narrative/table/figure. |
| U-N002 | PLAN DOC-002 pp.9–10,25 | Secondary: reintubation at 48h,72h,ICU discharge; respiratory failure by day7; treatment beyond48h; support-free days through14d including intubation,NIV,HFNC; ICU/hospital stays; mortality ICU,hospital,day28,day90. Compare main secondary definitions/outcomes. |
| U-N003 | PLAN DOC-002 pp.10–11,26 | Ventilation at least24h in synopsis, >24h in detailed criteria; planned extubation after successful trial; age>65 or chronic cardiac/lung disease. Cardiac: EF≤45%, ischemic disease, chronic atrial fibrillation, prior cardiogenic edema. Lung: COPD, obesity-hypoventilation, restrictive disease; suspected disease PaCO2>45, BMI>30 where applicable. Ten exclusions as below. |
| U-N004 | PLAN DOC-002 p.27 | Screen all intubated patients; before planned-extubation screening remove deaths/transfers, tracheotomy without extubation, terminal/unplanned extubation; then ventilation<24h and do-not-reintubate. Compare main flow/population. |
| U-N005 | PLAN DOC-002 pp.27–28 | Readiness RR≤35, SpO2>90% on FiO2≤40% or PaO2/FiO2≥150 with PEEP≤8; RASS +1 to−2, minimal/no vasopressors, no continuous sedation. Trial T-piece or PS7 cmH2O with PEEP0, 30min–2h; blood gas at end. |
| U-N006 | PLAN DOC-002 pp.29–30 | HFNC50 L/min, FiO2 targeting SpO2≥92%, ≥48h; after48h if no ARF weaning HFNC30 L/min FiO2 30%; ARF requires continued/restarted treatment in24h increments. |
| U-N007 | PLAN DOC-002 pp.29–30 | NIV≥12h/day ≥48h, first session≥4h, subsequent≥2h, nights22:00–06:00 if possible; PS≥5 cmH2O, tidal6–8 mL/kg, PEEP5–10, ramp0.1–0.2s, cycling25–30% peak flow, oxygen target≥92%; HFNC50 between sessions. |
| U-N008 | PLAN DOC-002 p.30 | ARF≥2: RR>25 for≥2h; clinical distress; pH<7.35 and PaCO2>45; FiO2≥50% for SpO2≥92% or PaO2/FiO2≤150. Compare main respiratory-failure definition. |
| U-N009 | PLAN DOC-002 pp.30–31 | Reintubation respiratory failure≥2: RR>35; clinical distress; pH<7.35 and PaCO2>45; FiO2≥80% for saturation≥92% or ratio≤100. Other sufficient indications: systolic<90 or mean<65 with vasopressors; Glasgow<12 or agitation; cardiac/respiratory arrest. Rescue NIV if used should terminate/intubate after2h persistent ARF. |
| U-N010 | PLAN DOC-002 pp.31–32 | Baseline and H1,H6,H12–24,H24–48, daily3–7,day14,ICU discharge,day90 assessments; blood gas under HFNC control/NIV intervention; later gases if available/applicable. Participation3 months, recruitment36 months, total51 months (36 study+12 analysis printed here), N650. |
| U-N011 | PLAN DOC-002 p.41 | Schedule rows: eligibility before trial; information/nonopposition every listed stage; randomization inclusion; demographics before trial+inclusion; SOFA/SAPS inclusion; clinical inclusion,H1,H6/12–24/24–48,3–7; treatment/weaning before+inclusion; ventilatory inclusion,H1,intermediate,3–7; gases before,inclusion(end trial),H1,intermediate,3–7; ARF/reintubation H1,intermediate,3–7; status/stay H1,intermediate,3–7,14/ICU,28/90. |
| U-N012 | PLAN DOC-002 p.42 | Fresh image form thresholds and scored cough/secretions detailed below; compare main weaning procedure/definitions. |
| U-N013 | PLAN DOC-002 pp.14–20,34–35 | Historical rationale and Table1 results, distinct from current trial; complete historical transcription below. |
| U-N014 | REPORT DOC-003 p.2 | eTable1 population302 HFNC alone/339 HFNC+NIV; all displayed outcome/criterion/cause rows reproduced in page transcription; main ARF and ICU-reintubation matching keys. Criteria and causes need not be mutually exclusive. |
| U-N015 | REPORT DOC-003 p.3 | eTable2 baseline four population cells254/276 nonhypercapnic and48/63 hypercapnic; all admission/risk/weaning rows, disease counts overlap by footnote. Match main baseline Table1 population and subgroup definitions. |
| U-N016 | REPORT DOC-003 p.4 | eTable2 ventilator and spontaneous trial rows; exact four cough denominators239/263/45/59 and secretion242/265/46/61. All printed percentages preserved, no normalization. Match main cough/secretions baseline. |
| U-N017 | REPORT DOC-003 p.5 | SAPS II17 variables, range0–163, higher worse; SOFA6 variables range0–24, higher worse; multiple cardiac/lung disease possible; simple first-trial success,difficult within7d after failed first trial,prolonged>7d. |
| U-N018 | REPORT DOC-003 p.6 | Hypercapnic48/63, all13 primary/secondary outcomes with arm values; main day7 subgroup comparison and total outcomes. |
| U-N019 | REPORT DOC-003 p.7 | Nonhypercapnic254/276, all13 primary/secondary outcomes; main subgroup/total outcome comparison. |
| U-N020 | REPORT DOC-003 p.8 | Thirty centers, all3 count/denominator/% columns and total95/641,55/302,40/339; match main analyzed cohort and day7 counts. |
| U-N021 | REPORT DOC-003 p.9 | Survival eFigure overall cohort risk counts at0,15,30,45,60,75,90: HFNC302,284,268,260,251,242,237; NIV339,314,298,286,280,280,277. Caption extubation-to90; x-axis printed Days Since Intubation; y survival probability ticks1.0,.9,.8,.7 and axis break. Blue HFNC-alone/orange HFNC+NIV. End levels visually about.78/.82; no exact coordinates extracted. |

## Inferential and planned statistical relationship groups

| Local key | Role/source page | Specification or complete tested relationship group |
|---|---|---|
| U-S001 | PLAN DOC-002 pp.29,28,34 | Individual randomized1:1, central web randomization stratified center and PaCO2>45 vs nonhypercapnia at end trial; last ventilated gas substitutes if end-trial unavailable. |
| U-S002 | PLAN DOC-002 p.33 | SAS9.2; intention-to-treat after blind committee validation of inclusion/exclusion. Eligibility verified via recorded case reports; ineligible included subjects/loss to follow-up described; protocol deviations case-by-case. |
| U-S003 | PLAN DOC-002 p.33 | Descriptive continuous median/IQR/extremes or mean/SD with missing-count indication; categorical frequency/percentage. No trial-specific imputation method specified across assigned plan. |
| U-S004 | PLAN DOC-002 p.33 | Primary day7 reintubation percentages compared by chi-square. |
| U-S005 | PLAN DOC-002 p.33 | Predictors: t-test/Mann–Whitney continuous; chi-square/Fisher categorical; univariate logistic OR/95%CI. |
| U-S006 | PLAN DOC-002 p.33 | Multivariable logistic after testing interactions: maximum includes p<.20 associated variables plus forced literature variables; backward stepwise elimination retains p<.05 and forced variables. Named forced covariates not listed here. |
| U-S007 | PLAN DOC-002 p.33 | Enrollment-to-reintubation Kaplan–Meier/log-rank; Cox p<.20 entry, backward selection p<.05 final; labeled adjusted relative risk and HR/95%CI. |
| U-S008 | PLAN DOC-002 pp.33–34 | Secondary reintubation and ARF same method as primary; free days/stays t-test or Mann–Whitney; mortality KM/log-rank ICU,hospital,28,90. |
| U-S009 | PLAN DOC-002 p.34 | Mortality Cox: in absence of interaction, univariate p<.20 maximal model; manual backward, final p<.05; adjusted relative risk and HR/95%CI. |
| U-S010 | PLAN DOC-002 p.34 | Prespecified primary AND secondary subgroup analyses: PaCO2>45 vs other; underlying cardiac or respiratory disease; T-piece vs minimum PS weaning test. |
| U-S011 | PLAN DOC-002 pp.34–35 | Power80%, two-sidedα.05, control18%, intervention10%, absolute8 percentage points, N590; +10% secondary exclusions →650. Expected intervention day7 10% (prior NIV/standard15%,day48h10%); control day7 15–20% (prior standard28%). |
| U-S012 | PLAN DOC-002 pp.1–48 | No trial-specific multiplicity hierarchy, noninferiority margin, interim efficacy analysis or numerical stopping boundary located. Generic ethical risk monitoring in Helsinki appendix is not a numerical trial rule. No separate SAP/source supplied. |
| U-S013 | REPORT DOC-003 p.2 | Every eTable1 count/percentage pair and P contrast HFNC alone302 vs HFNC+NIV339; values reproduced below; statistical test not specified locally. |
| U-S014 | REPORT DOC-003 pp.3–4 | Every eTable2 P contrast within each PaCO2 stratum, all baseline/ventilator/weaning data below; test/model details not specified locally. |
| U-S015 | REPORT DOC-003 p.6 | Every13 hypercapnic outcome absolute difference/95%CI/P combination, main point day7−12.9 (−27.1 to−0.1), P.0489. Difference sign NIV−HFNC. Stays labeled median/IQR but differences not labeled median differences in supplement. |
| U-S016 | REPORT DOC-003 p.7 | Every13 nonhypercapnic absolute difference/95%CI/P combination; day7−5.0 (−11.2 to1.1),P.1057. Difference sign NIV−HFNC. Stays labeled median/IQR; estimator not specified locally. |
| U-S017 | REPORT DOC-003 p.9 | Overall survival KM, log-rank P=.37, caption follow-up extubation→day90, full risk table U-N021; match main mortality follow-up/test narrative. |

## Full protocol operational transcription and historical evidence

Ten exclusions in pp.11,26: traumatic brain injury; peripheral neuromuscular cause of intubation; long-term NIV for chronic lung disease; long-term CPAP for obstructive sleep apnea; NIV contraindication; unplanned extubation (next planned extubation may qualify after reintubation); do-not-reintubate order; no insurance; protected persons (minor/pregnancy/breastfeeding/guardianship/judicial or administrative restrictions); opposition.

Weaning form [DOC-002 p.42](../../../joi190108supp1_prod.pdf#page=42), translated from direct image: daily morning assessment for every intubated patient without continuous sedation regardless of ventilator mode. Step1 requires all four: RR≤35/min and SpO2≥92% with FiO2≤40% and PEEP≤8cmH2O; no noradrenaline/adrenaline vasopressors; awake/responds appropriately, −2≤RASS≤+1; no continuous hypnovel/propofol/sufentanil. If all four present, spontaneous breathing test on artificial nose after morning nursing for1h. Oxygen3L/min for FiO2 30%,6L/min for40%. Form columns pretrial,5min,trial end H1 or failure. Poor tolerance rows O2>6L/min,SpO2<90%,RR>35/min,HR>140/min,systolic<90 or>180mmHg,distress(retractions,sweating,agitation,mottling). Stop at1h or any single poor-tolerance criterion. Record observations/duration before reconnection, circle failed criteria, obtain arterial gas if line present, reconnect prior settings. If success, Step2 extubatable assessment: cough absent0/weak1/good2/very good3; secretions absent0/scant1/abundant2/very abundant3; congestion risk yes if secretions2or3 AND cough0or1; laryngeal edema cuff-leak assessment by physiotherapist/physician/resident. Step3 extubation by medical decision; yes/no/today/reason fields. Embedded form version1 May2014; surrounding protocol version4 October2017. No patient values entered.

Historical six-trial Table1 [DOC-002 p.17](../../../joi190108supp1_prod.pdf#page=17), NIV vs standard oxygen (not current trial):

| Study | Arm N | All reported results |
|---|---|---|
| Nava2005 | 48/49,3 centers | Reintubation4(8%)/12(24%),P.027; ICU mortality3(6%)/9(18%),P.064. |
| Ferrer2006 | 79/83,2 centers | ARF13(16%)/27(33%),P.029; reintubation9(11%)/18(22%),P.12; infections18(23%)/27(33%),NS; ICU mortality2(3%)/12(14%),P.015. |
| Ferrer2009 | 54/52,3 centers | ARF8(15%)/25(48%),P<.0001; reintubation6(11%)/10(19%),P.37; pneumonia3(6%)/9(17%),P.12; ICU mortality3(6%)/4(8%),P.71;day90 mortality6(11%)/16(31%),P.024. |
| Khilnani2011 | 20/20,1 center | COPD; reintubation5(25%)/3(15%),P.44; ICU stay18.3±7.9 vs16.1±6.3d,P.34. |
| Su2012 | 202/204,3 centers | Ventilation≥48h; failure30(15%)/27(13%),P.62; reintubation21(10%)/16(8%),P.37; ICU death3(1.5%)/2(1%),P.64. |
| Ornico2013 | 20/18,1 center | Ventilation≥3d for ARF; reintubation1(5%)/7(39%),P.016; hospital death0%/4(22%),P.041. |

Historical narrative p.15 trial totals97,162,106,400,38 and overall reintubation~10% in the described large study; historical NIV≥8h/day first48h, others24h; hypercapnia>45. pp.18–19 preliminary >800 ventilated; first168 extubations/26 failures, age>65 risk29%, chronic cardiac/lung23%, both34%, neither9%; subsequent cohort reintubation28%→15%,P.03. Background NIV survey11% of all,approximately20–25% high-risk; p.19 prior NIV beyond24h in>20%. These are historical or administrative context, not additional current-trial outcomes.

## Full results-supplement transcription

The following complete English page transcriptions preserve every table cell, label, unit and footnote. They are grouped by the U-N/U-S keys above. Direct source remains authoritative. Supplement table values are displayed values; no workbook formulas/cached values or Office/CSV units exist in the assigned package.

### DOC-003 PDF page 002

[Direct source page](../../../joi190108supp2_prod.pdf#page=2)

```text
eTable 1. Comparison of Patients Who Met Criteria for Postextubation Respiratory Failure and for
Reintubation According to Randomization Group


                                                              High-flow nasal   High-flow nasal     P
                                                               oxygen alone     oxygen with NIV   value
                                                                 (n=302)            (n=339)
 Post-extubation respiratory failure at day 7, No. (%)            88 (29)           70 (21)        .02
  - Respiratory rate > 25 breaths per minute, No. (%)             74 (24)           63 (19)        .07
  - Clinical signs suggesting respiratory distress, No. (%)       57 (19)           46 (14)        .07
  - Respiratory acidosis, No. (%)                                 21 (7)            18 (5)         .38
  - Hypoxemia, No. (%)                                            52 (17)           36 (11)        .02
 Reintubation up until ICU discharge, No. (%)                     59 (20)           41 (12)       .009
 Criteria for reintubation
 - Severe respiratory failure, No. (%)                            46 (15)           42 (12)        .30
  Respiratory rate > 35 breaths per minute, No. (%)               34 (11)           32 (9)         .45
  Clinical signs suggesting respiratory distress, No. (%)         39 (13)           37 (11)        .43
  Respiratory acidosis, No. (%)                                   12 (4)             9 (3)         .35
  Hypoxemia, No. (%)                                              24 (8)            19 (6)         .24
 - Hemodynamic failure, No. (%)                                   10 (3)             6 (2)         .21
 - Neurological failure, No. (%)                                  18 (6)            19 (6)         .85
 - Respiratory or cardiac arrest, No. (%)                          7 (2)             3 (1)         .20
 Reasons for reintubation
 Cardiogenic pulmonary edema, No. (%)                             9 (3)             7 (2)          .46
 Upper airway obstruction, No. (%)                                6 (2)             6 (2)          .84
 Aspiration, No. (%)                                              1 (0)             2 (1)          .99
 Pneumonia, No. (%)                                               7 (2)             3 (1)          .14
 Atelectasis, No. (%)                                             9 (3)             4 (1)          .11
 Pleural effusion, No. (%)                                        2 (1)             3 (1)          .75
 Pneumothorax, No. (%)                                            1 (0)             2 (1)          .99
 Inability to clear secretions, No. (%)                           18 (6)            18 (5)         .72
 Ineffective cough, No. (%)                                       12 (4)            9 (3)          .35
 Weakness of respiratory muscles, No. (%)                         15 (5)            9 (3)          .12
 Hypoventilation, No. (%)                                         0 (0)             2 (1)          .50
 Hypercapnic coma, No. (%)                                        4 (1)             1 (0)          .14
 Septic shock, No. (%)                                            4 (1)             1 (0)          .14
 Cardiogenic shock, No. (%)                                       2 (1)             0 (0)          .22
 Hemorrhage, No. (%)                                              3 (1)             0 (0)          .07
 Neurologic event, No. (%)                                        7 (2)             7 (2)          .83
 Surgery, No. (%)                                                 3 (1)             1 (0)          .26




© 2019 American Medical Association. All rights reserved.

```

### DOC-003 PDF page 003

[Direct source page](../../../joi190108supp2_prod.pdf#page=3)

```text
eTable 2. Characteristics of the Patients According to PaCO2 Level at Baseline

                                                 Non-hypercapnic patients (PaCO2 ≤ 45   Hypercapnic patients (PaCO2 > 45 mm
                                                              mm Hg)                                    Hg)

                                                 High-flow      High-flow        P      High-flow      High-flow       P
                                                   nasal       nasal oxygen    value      nasal          nasal       value
                                                  oxygen         with NIV                oxygen       oxygen with
                                                   alone         (n=276)                  alone           NIV
                                                  (n=254)                                (n=48)         (n=63)
 Characteristics of the patients at admission
 Age, mean (SD), years                             70 (10)        69 (10)      .3492      70 (9)         67 (11)     .1613
 Male sex, No. (%)                                167 (66)        190 (69)     .4481      28 (58)        40 (63)     .5805
 Body-mass index, mean (SD), kg/m2                 28 (6)          28 (7)      .8387      31 (7)         31 (9)      .8397
 SAPS II at admission, mean (SD), points A         56 (18)        56 (20)      .9481      54 (16)        51 (19)     .4512
 Main reason for intubation, No. (%)                                           .8290                                   --
 Acute respiratory failure                        123 (48)        126 (46)                35 (73)        41 (65)
 Coma                                              47 (19)        47 (17)                 8 (17)         10 (16)
 Shock                                             27 (11)        33 (12)                  3 (6)          4 (6)
 Cardiac arrest                                    24 (9)         34 (12)                  2 (4)          1 (2)
 Surgery                                           28 (11)        28 (10)                  0 (0)         7 (11)
 Other reason                                       5 (2)           8 (3)                   0              0
 Risk factors of extubation failure
 Age > 65 years, No. (%)                          188 (74)        199 (72)     .6199      35 (73)        38 (60)     .1658
 Underlying chronic cardiac disease, No. (%) B    126 (50)        138 (50)     .9278      19 (40)        23 (37)     .7407
    Ischemic heart disease, n                        66              77                     12             11
    Atrial fibrillation, n                           50              35                     8              10
    Left ventricular dysfunction, n                  33              46                     6              6
    History of cardiogenic pulmonary edema, n        17              20                     4              5
 Underlying chronic lung disease, No. (%) B        54 (21)        80 (29)      0.0409     33 (69)        46 (73)     0.6230
    Chronic obstructive pulmonary disease, n         42              55                     22             31
    Obesity-hypoventilation syndrome, n              9               7                      7              13
    Chronic restrictive pulmonary disease, n         7               21                     5              3
 Characteristics of the patients the day of
 extubation
 SOFA score, mean (SD), points C                  4.3 (2.7)       4.4 (2.6)    .4970     3.6 (1.6)      4.3 (3.1)    .1484
 Duration of mechanical ventilation, median        5 (3–9)        6 (3–10)     .1319     6 (4–10)       5 (3–12)     .4787
 (IQR), days
 Weaning difficulty No. (%) D                                                  .5533                                 .3187
    Simple weaning                                177 (70)        194 (70)                26 (54)        38 (60)
    Difficult weaning                              70 (27)        70 (25)                 22 (46)        23 (37)
    Prolonged weaning                               7 (3)          12 (5)                  0 (0)          2 (3)




© 2019 American Medical Association. All rights reserved.

```

### DOC-003 PDF page 004

[Direct source page](../../../joi190108supp2_prod.pdf#page=4)

```text
                                           Non-hypercapnic patients (PaCO2 ≤ 45 mm   Hypercapnic patients (PaCO2 > 45 mm Hg)
                                                             Hg)

                                            High-flow      High-flow nasal     P       High-flow        High-flow        P
                                              nasal         oxygen with      value        nasal           nasal        value
                                           oxygen alone          NIV                  oxygen alone     oxygen with
                                             (n=254)           (n=276)                   (n=48)            NIV
                                                                                                         (n=63)
 Ventilator settings before the
 spontaneous breathing trial
 Assist-control ventilation, No. (%)          37 (15)          45 (16)       .5806       5 (10)            4 (6)       .4367
 Pressure-support ventilation, No. (%)        217 (85)        231 (84)       .5806       43 (90)          59 (94)      .4367
 Pressure-support level, mean (SD), cm        9.4 (2.7)       9.2 (3.0)      .4147      10.4 (2.9)       9.9 (2.2)     .3163
 H2O
 PEEP, mean (SD), cm H2O                      5.7 (1.6)       5.8 (1.5)      .1580      5.9 (1.7)        6.0 (1.9)     .7207
 Tidal volume, mean (SD), ml                 480 (125)        480 (143)      .9664      409 (110)       479 (147)       .009
 Tidal volume, mean (SD), ml/kg               7.9 (2.4)       7.9 (2.5)      .9582      6.7 (1.6)        7.7 (2.3)     .0086
 Respiratory rate, mean (SD),                  22 (7)          22 (6)        .7534       23 (6)           22 (7)       .4974
 breaths/min
 FiO2, mean (SD), %                            34 (9)          35 (11)       .3846       38 (10)          37 (10)      .7881
 PaO2:FiO2, mean (SD), mm Hg                  281 (93)        281 (88)       .9926      236 (79)         247 (91)      .4927
 pH, mean (SD), units                       7.45 (0.06)      7.45 (0.05)     .6397     7.43 (0.05)      7.43 (0.05)    .9343
 PaCO2, mean (SD), mm Hg                       37 (6)          37 (8)        .3584       51 (7)           51 (8)       .6504
 Characteristics at the end of the
 spontaneous breathing trial
 T-piece trial, No. (%)                       161 (63)        172 (62)       .7996       27 (56)          34 (54)      .8108
 Low level of pressure-support, No. (%)       93 (37)         104 (38)       .7996       21 (44)          29 (46)      .8108
 Duration, median (IQR), min                 60 (30-60)      60 (30-60)      .5452     60 (30-72)       60 (30-60)     .3719
 Systolic arterial pressure, mean (SD),       135 (21)        135 (23)       .7474      140 (20)         136 (21)      .3383
 mm Hg
 Diastolic arterial pressure, mean (SD),      66 (14)          68 (16)       .4308       71 (13)          69 (16)      .4674
 mm Hg
 Heart rate, mean (SD), beats/min             92 (17)          91 (18)       .3496       90 (19)          96 (18)      .0903
 Respiratory rate, mean (SD),                  23 (6)          23 (6)        .2576       24 (6)           23 (7)       .4892
 breaths/min
 SpO2, mean (SD), %                            97 (3)          97 (3)        .7770       95 (3)           95 (3)       .9510
 PaO2, mean (SD), mm Hg                       89 (29)          87 (27)       .6288       75 (14)          81 (27)      .2201
 pH, mean (SD), units                       7.46 (0.06)      7.46 (0.05)     .4922     7.42 (0.04)      7.43 (0.05)    .5496
 PaCO2, mm Hg                                  37 (5)          37 (5)        .9777       53 (7)           52 (9)       .4431
 Steroids administration before               35 (14)          38 (14)       .9970       7 (15)           15 (24)      .2270
 extubation
 Ineffective cough, No./total No. (%)       51/239 (21)      70/263 (27)     .1674     14/45 (69)       16/59 (73)     .6561
 Abundant secretions, No./total No. (%)    101/242 (42)      91/265 (34)     .0864     20/46 (57)       23/61 (62)     .5465
Abbreviations: NIV = Non-invasive ventilation; SAPS = Simplified Acute Physiology Score; SOFA = Sepsis-related Organ Failure
Assessment.

                                                                                                                          4

```

### DOC-003 PDF page 005

[Direct source page](../../../joi190108supp2_prod.pdf#page=5)

```text
A The Simplified Acute Physiology Score (SAPS) II was calculated from 17 variables at admission. Scores range from 0 to 163, with higher

scores indicating more severe disease and higher mortality risk.
B Patients could have more than one underlying chronic cardiac or lung disease.
C The Sepsis-related Organ Failure Assessment (SOFA) was calculated from 6 variables the day of extubation. Scores range from 0 to

24, with higher scores indicating more severe organ failure and higher mortality risk.
D Weaning difficulty was defined as following: simple weaning included patients extubated after success of the first spontaneous

breathing trial, difficult weaning included patients who failed the first spontaneous breathing trial and were extubated within the 7
following days, and prolonged weaning included patients extubated more than 7 days after the first spontaneous breathing trial.




                                                                                                                                      5

```

### DOC-003 PDF page 006

[Direct source page](../../../joi190108supp2_prod.pdf#page=6)

```text
eTable 3. Primary and Secondary Outcomes in Hypercapnic Patients (PaCO2 > 45 mm Hg)

                                                High-flow        High-flow nasal        Absolute              P
                                                   nasal          oxygen with           difference          value
                                               oxygen alone            NIV                (95 CI)
                                                  (n=48)             (n=63)
 Primary outcome
 Reintubation at day 7, No. (%)                    10 (21)            5 (8)          -12.9 (-27.1 to -      .0489
                                                                                           0.1)
 Secondary outcomes
 Post-extubation respiratory failure at day        24 (50)           14 (22)         -27.8 (-43.8 to -      .0022
 7, No. (%)                                                                                9.8)
 Reintubation at 48 hours, No. (%)                  4 (8)             2 (3)         -5.2 (-16.6 to 4.0)     .2337
 Reintubation at 72 hours, No. (%)                 9 (19)             4 (6)          -12.4 (-26.1 to -      .0441
                                                                                          0.10)
 Reintubation up until ICU discharge, No.          10 (21)            6 (9)         -11.3 (-25.7 to 2.0)    .0928
 (%)
 Patient meeting reintubation criteria             11 (23)            7 (11)        -11.8 (-26.5 to 2.1)    .0946
 during ICU stay, No. (%)
 Length of stay in ICU, median (IQR) days        13 (9–18)          13 (7–20)        0.6 (-4.0 to 5.2)      .7592
 Length of stay in hospital, median (IQR)        24 (15–29)        26 (15–36)        2.5 (-4.9 to 9.9)      .4234
 days
 Mortality in ICU, No. (%)                         5 (10)             2 (3)         -7.2 (-19.2 to 2.4)     .1199
 Mortality or reintubation in ICU, No. (%)         11 (23)            6 (9)         -13.4 (-27.9 to 0.3)    .0523
 Mortality in ICU of reintubated patients,       4/10 (40)           2/6 (33)       -6.7 (-43.9 to 36.7)    .9999
 No. (%)
 Mortality in hospital, No. (%)                    7 (15)             8 (13)        -1.9 (-15.9 to 10.8)    .7735
 Mortality at day 90, No. (%)                      11 (23)           12 (19)        -3.9 (-19.6 to 11.0)    .6183
Abbreviations: NIV = Non-invasive ventilation; 95 CI = 95% confident interval; ICU = intensive care unit.




                                                                                                               6

```

### DOC-003 PDF page 007

[Direct source page](../../../joi190108supp2_prod.pdf#page=7)

```text
eTable 4. Primary and Secondary Outcomes in Nonhypercapnic Patients (PaCO2 ≤ 45 mm Hg)

                                               High-flow nasal       High-flow         Absolute            P
                                                oxygen alone        nasal oxygen       difference        value
                                                   (n=254)            with NIV           (95 CI)
                                                                      (n=276)
 Primary outcome
 Reintubation at day 7, No. (%)                     45 (18)            35 (13)     -5.0 (-11.2 to 1.1)   .1057
 Secondary outcomes
 Post-extubation respiratory failure at day         64 (25)            56 (20)     -4.9 (-12.0 to 2.2)   .1775
 7, No. (%)
 Reintubation at 48 hours, No. (%)                  32 (13)            22 (8)      -4.6 (-10.0 to 0.6)   .0785
 Reintubation at 72 hours, No. (%)                  38 (15)            26 (9)      -5.5 (-11.2 to 0.0)   .0505
 Reintubation up until ICU discharge                49 (19)            35 (13)     -6.6 (-12.9 to -0.4) .0374
 Patient meeting reintubation criteria              54 (21)            42 (15)     -6.0 (-12.6 to 0.5)   .0712
 during ICU stay, No. (%)
 Length of stay in ICU, median (IQR), days        11 (7–19)          12 (7–18)      0.5 (-1.8 to 2.8)    .4087
 Length of stay in hospital, median (IQR),        23 (15–40)         25 (15–43)     2.0 (-2.2 to 6.2)    .4181
 days
 Mortality in ICU, No. (%)                          21 (8)             19 (7)       -1.4 (-6.1 to 3.2)   .5548
 Mortality or reintubation in ICU, No. (%)          53 (21)            45 (16)     -4.6 (-11.2 to 2.1)   .1766
 Mortality in ICU of reintubated patients,        17/49 (35)          9/35 (26)      -8.9 (-27.1 to      .3801
 No. (%)                                                                                 11.2)
 Mortality in hospital, No. (%)                     39 (15)            46 (17)      1.3 (-5.0 to 7.5)    .6808
 Mortality at day 90, No. (%)                       54 (21)            50 (18)      -3.8 (-9.9 to 3.6)   .3626
Abbreviations: NIV = Non-invasive ventilation; ICU = intensive care unit.




                                                                                                           7

```

### DOC-003 PDF page 008

[Direct source page](../../../joi190108supp2_prod.pdf#page=8)

```text
eTable 5. Number of Patients Included per Center and Reintubation Rates per Center According to
Randomization Group.

             Reintubation rates         Reintubation rates in the         Reintubation rates in the
             per center at day 7   high-flow nasal oxygen alone group   non-invasive ventilation group
 Center 1        1/38 (3%)                     1/19 (5%)                          0/19 (0%)
 Center 2        3/32 (9%)                     0/16 (0%)                         3/16 (19%)
 Center 3        1/14 (7%)                      0/7 (0%)                          1/7 (14%)
 Center 4        5/32 (16%)                   2/15 (13%)                         3/17 (18%)
 Center 5        7/13 (54%)                    3/6 (50%)                          4/7 (57%)
 Center 6        4/27 (15%)                   2/13 (15%)                         2/14 (14%)
 Center 7        6/23 (26%)                   6/10 (60%)                          0/13 (0%)
 Center 8        3/12 (25%)                    2/5 (40%)                          1/7 (14%)
 Center 9        7/34 (21%)                   5/17 (29%)                         2/17 (12%)
 Center 10       2/22 (9%)                    2/10 (20%)                          0/12 (0%)
 Center 11       5/24 (21%)                   3/11 (27%)                         2/13 (15%)
 Center 12        0/3 (0%)                      0/1 (0%)                          0/2 (0%)
 Center 13       5/25 (20%)                   3/12 (25%)                         2/13 (15%)
 Center 14       8/24 (33%)                   6/11 (55%)                         2/13 (15%)
 Center 15       3/24 (13%)                   2/12 (17%)                          1/12 (8%)
 Center 16       4/23 (17%)                   1/10 (10%)                         3/13 (23%)
 Center 17       4/25 (16%)                    1/12 (8%)                         3/13 (23%)
 Center 18       1/7 (14%)                     1/2 (50%)                          0/5 (0%)
 Center 19       0/11 (0%)                      0/5 (0%)                          0/6 (0%)
 Center 20       5/48 (10%)                   3/25 (12%)                          2/23 (9%)
 Center 21       4/17 (24%)                    1/8 (13%)                          3/9 (33%)
 Center 22       1/6 (17%)                     1/2 (50%)                          0/4 (0%)
 Center 23       3/40 (8%)                    2/19 (11%)                          1/21 (5%)
 Center 24       1/31 (3%)                     1/14 (7%)                          0/17 (0%)
 Center 25        0/6 (0%)                      0/3 (0%)                          0/3 (0%)
 Center 26       2/21 (10%)                   2/10 (20%)                          0/11 (0%)
 Center 27       2/9 (22%)                     1/4 (25%)                          1/5 (20%)
 Center 28       4/30 (13%)                   3/14 (21%)                          1/16 (6%)
 Center 29       1/4 (25%)                      0/2 (0%)                          1/2 (50%)
 Center 30       3/16 (19%)                    1/7 (14%)                          2/9 (22%)
 Total         95/641 (15%)                  55/302 (18%)                       40/339 (12%)


                                                                                                    8

```

### DOC-003 PDF page 9 visual transcription

[Direct source eFigure](../../../joi190108supp2_prod.pdf#page=9). Title: Kaplan-Meier Curves of the Cumulative Probability of Survival From Extubation to Day 90. Population: Overall population. Vertical axis cumulative probability of survival, visible .7,.8,.9,1.0 ticks and break below .7. Horizontal axis Days Since Intubation, ticks0,15,30,45,60,75,90. Legend labels orange High-flow nasal oxygen with NIV; blue High-flow nasal oxygen alone. Log-rank P=.37. No HR or confidence interval printed. Risk table:

| Days | 0 | 15 | 30 | 45 | 60 | 75 | 90 |
|---|---:|---:|---:|---:|---:|---:|---:|
| High-flow nasal oxygen alone | 302 | 284 | 268 | 260 | 251 | 242 | 237 |
| High-flow nasal oxygen with NIV | 339 | 314 | 298 | 286 | 280 | 280 | 277 |

### DOC-004 PDF page 1 administrative map

[Direct source](../../../joi190108supp3_prod.pdf#page=1): data sharing statement identifies the trial and publication2 October2019, DOI10.1001/jama.2019.14901. Data available: No. No quantitative clinical outcome, prospective population definition, or statistical model is present. Not applicable for quantitative relationship generation.

## Completion and limitations

DOC-00248/48 pages, DOC-0039/9 pages, DOC-0041/1 pages mapped:58/58. Local group inventory21 numeric groups U-N001–U-N021 and17 inferential groups U-S001–U-S017, with all individual table rows retained within their groups. Both checkers must cover every row, not sample representative rows. Plans and administrative units without applicable evidence explicitly recorded above. Native DOC-002p42 omits the embedded form; fresh direct visual transcription closes that scientific coverage gap. Its OCR aid misreads inequality glyphs and omits cells, so image transcription controls. DOC-003p9 native text is sparse but reusable image closes the figure mapping. Exact curve coordinates are not printed and are not treated as extracted numeric estimates. No unresolved source-page coverage gap; no supplied workbook/Office/CSV sources.
