# Support quantitative evidence map

Stage: support_quantitative_mapper. Runtime agent: root/support_mapper. Scope: DOC-002 physical PDF pages 1–20 (REPORT) and DOC-003 physical PDF pages 1–7 (PLAN). All 27 units are mapped; no scientific coverage gaps. Fresh scientific mapping uses source-matched reusable native/layout text and visual inspection of all four embedded eFigures. No legacy candidate, checker, screening, classification, disposition, or final report was read.

## Evidence provenance and conventions

All 27 units have usable reusable extraction; fresh-required units = 0. The page blocks below retain complete source text so every displayed row, code, footnote, estimate, interval, P value and definition is available without selection. Results-supplement pp. 1–5 and protocol pp. 1–7 use Poppler pdftotext layout range files in review_1_5_1/preprocessing; result pp. 6–20 use source-matched native page texts in preprocessing/jama2019-14231-supplement-1/native_text. All four figure images (physical pp. 8, 11, 16, 18) were visually inspected from source-matched preprocessing/jama2019-14231-supplement-1/images. Image renderer version is unrecorded in reused metadata. Native text does not capture embedded chart values; the figure mapping below supplies those relationships. No OCR or new derivative was needed. Exact supplied source pages remain authoritative.

The population is patients with type 2 diabetes and obesity, metabolic surgery versus matched nonsurgical usual care. Main matching keys are outcome, population/risk-set exclusions, index-date time, effect measure, contrast, model, and subgroup. The supplied study is an observational matched cohort. Baseline medication rows describe prevalence and are not mutually exclusive. Event rates, cumulative incidence, adjusted HRs, and modeled longitudinal differences are distinct quantities. All statistical relationship IDs in this shard are S101–S126; all numeric relationship IDs are N101–N118. Each ID groups a coherent family, and every member is listed in the keyed source blocks. These are mapping IDs, not findings or candidates. No inclusion judgments are made here.

## Page-complete coverage

| Source | Physical page | Role | Content and mapped relationships | Status |
|---|---:|---|---|---|
| DOC-002 | 1 | REPORT | Contents and supplement provenance; no outcome estimate; pointers mapped | COMPLETE |
| DOC-002 | 2 | REPORT | eTable 1 endpoint/cohort diagnosis and procedure codes; nephropathy threshold; N101, S101 | COMPLETE |
| DOC-002 | 3 | REPORT | eTable 2 adverse-event diagnosis and intervention definitions, first part; N102, S102 | COMPLETE |
| DOC-002 | 4 | REPORT | eTable 2 abdominal surgical interventions continuation and reference provenance; N102, S102 | COMPLETE |
| DOC-002 | 5 | REPORT | eTable 3 all 12 medication classes, two counts and percentages per row; N103 | COMPLETE |
| DOC-002 | 6 | REPORT | eTable 4 all eight outcome-specific rates/differences/bootstrap intervals plus death composites; N104, S103 | COMPLETE |
| DOC-002 | 7 | REPORT | eTable 5 eight outcomes × three years × two treatments, 48 estimates/95% CIs; N105, S104 | COMPLETE |
| DOC-002 | 8 | REPORT | eFigure 1 all 16 subgroup HRs/CIs, eight interaction tests and model rules; S105 | COMPLETE |
| DOC-002 | 9 | REPORT | eTable 6 eight adjusted HRs/CIs, eight treatment tests, eight PH tests; S106 | COMPLETE |
| DOC-002 | 10 | REPORT | eTable 7 eight outcomes × three years = 24 time-varying HRs/CIs; S107 | COMPLETE |
| DOC-002 | 11 | REPORT | eFigure 2 four treatment/BMI curves per outcome, both panels and axes; N106, S108 | COMPLETE |
| DOC-002 | 12 | REPORT | eTable 8 13 displayed rows × four times = 52 estimate/98.8% CI/test triplets; N107, S109 | COMPLETE |
| DOC-002 | 13 | REPORT | eTable 9 six variables × five times × four counts = 120 count cells; N108 | COMPLETE |
| DOC-002 | 14 | REPORT | eTable 10 five times × two denominator counts; N109 | COMPLETE |
| DOC-002 | 15 | REPORT | eTable 11 six interventions × four times = 24 incidence estimates/95% CIs; N110, S110 | COMPLETE |
| DOC-002 | 16 | REPORT | eFigure 3 four nutritional trend panels, all axes/treatment keys/caption; N111, S111 | COMPLETE |
| DOC-002 | 17 | REPORT | Five date samples × three matching ratios; all outcome sensitivity summaries; N112, S112 | COMPLETE |
| DOC-002 | 18 | REPORT | eFigure 4 eight outcomes × 15 datasets = 120 graphic HR/CI pairs; S113 | COMPLETE |
| DOC-002 | 19 | REPORT | Time-varying model and all 24 repeated HR/CIs; E-value definition and primary narrative; S107, S114 | COMPLETE |
| DOC-002 | 20 | REPORT | eTable 12 eight pairs of E-values; 40 risk-factor HRs/CIs with exact directions; N113, S115 | COMPLETE |
| DOC-003 | 1 | PLAN | Contents/protocol and amendment pointers; no quantitative result | COMPLETE |
| DOC-003 | 2 | PLAN | Original protocol identity, cohort/surgery inclusion/exclusion and dates; N114, S116 | COMPLETE |
| DOC-003 | 3 | PLAN | Control cohort selection, matching, T2DM algorithm and base cohort; N115, S117, S118 | COMPLETE |
| DOC-003 | 4 | PLAN | Six individual endpoints and both composite endpoint definitions; N116, S119 | COMPLETE |
| DOC-003 | 5 | PLAN | Outcome risk-set exclusions and all collected variable groups; S120, S121 | COMPLETE |
| DOC-003 | 6 | PLAN | Rates, Cox adjustment, PH testing, imputation, alpha/CI/multiplicity, sensitivity design; N117, S122, S123, S124, S125 | COMPLETE |
| DOC-003 | 7 | PLAN | Disclosed August amendment: early/late adverse events and E-value analyses; N118, S126 | COMPLETE |

## Numeric relationship inventory and exact matching keys

| ID | Locations | Relationship members and matching key |
|---|---|---|
| N101 | DOC-002 p2 eTable 1 | Every diagnosis/procedure code in 16 conditions/procedure categories; preserve code systems and primary-diagnosis bolding instruction. Codes are identifiers, not event counts. Nephropathy requires at least two eGFR measures below 60 mL/min, separated by ≥90 days, no intervening value ≥60, MDRD equation. Match main endpoint definitions and plan p4. |
| N102 | DOC-002 pp3–4 eTable 2 | Acute pulmonary complications; acute renal failure plus dialysis; DVT/PE; transfusion; TPN; endoscopy; interventional radiology; cholecystectomy; abdominal wall hernia; abdominal surgery including revisions, adhesions, internal hernia and other procedures. Each full code list is retained in source blocks; conjunctive renal/dialysis condition retained. Match main adverse-event results and protocol amendment. |
| N103 | DOC-002 p5 eTable 3 | Surgery N=2287, matched nonsurgical N=11435; 12 rows: alpha-glucosidase 6(0.3)/26(0.2); amylin 7(0.3)/27(0.2); biguanides 1530(67.9)/7606(66.5); bile acid sequestrants 8(0.3)/55(0.5); dopamine agonists 3(0.1)/14(0.1); DPP-4 214(9.4)/1202(10.5); GLP-1 270(11.8)/841(7.4); insulin 776(33.9)/3806(33.3); meglitinides 20(0.9)/79(0.7); sulfonylureas 509(22.3)/3404(29.8); SGLT2 43(1.9)/143(1.3); thiazolidinediones 286(12.5)/1083(9.5). All percentages as printed; match baseline index-date medication classification, not follow-up drug denominators. |
| N104 | DOC-002 p6 eTable 4 | Surgery/control cause-specific rates per 100 patient-years at eight years: primary 4.51/7.45; secondary 2.11/3.64; death 1.19/2.22; HF .92/2.49; CAD 1.03/1.55; cerebrovascular .45/.73; nephropathy .89/2.07; AF 1.14/1.77. Parentheses give outcome-or-death composites: HF 1.84/3.7; CAD 1.98/3.36; cerebrovascular 1.55/2.74; nephropathy 1.77/3.47; AF 2.16/3.42. Differences and CI are S103; do not match these rates to risk percentages. |
| N105 | DOC-002 p7 eTable 5 | All 48 cumulative incidence percentages at 2,5,8 years, exact outcome/treatment/time keys in source block. Eight-year primary 30.8(27.6,34) vs47.7(46.1,49.2); secondary17(14.3,19.7) vs27.6(26.2,29); death10(7.8,12.2) vs17.8(16.6,19). Match main cumulative incidence displays using time and risk sets. |
| N106 | DOC-002 p11 eFigure 2 | HbA1c (%) and percent taking noninsulin drugs versus time0–4 years; surgery/nonsurgery × baseline BMI<35/≥35 kg/m². Graphical values have no printed numeric point labels; no exact digitization implied. All eight curves inspected. |
| N107 | DOC-002 p12 eTable 8 | Thirteen rows: weight pounds and equivalent kg; HbA1c%; protein, albumin, hemoglobin g/dL; vitaminD25 ug/L; six medication classes expressed in percentage points. All four time points1,2,5,8 have exact estimate/CI/P cells in source block. Weight kg estimates −25.7,−33.4,−20.5,−20.3; HbA1c −1.5,−1.6,−1.0,−1.1. Table heading says average change from baseline in surgery vs nonsurgery. Match main longitudinal change summaries with S109 model key. |
| N108 | DOC-002 p13 eTable 9 | All120 counts retained, distinguished as total observations vs distinct patients available after each time point0,1,2,5,8, surgery/nonsurgery; six variables HbA1c, weight, albumin, hemoglobin, protein, vitaminD25. These are repeated-measure availability counts, not randomized or endpoint risk-set totals. |
| N109 | DOC-002 p14 eTable 10 | Medication proportion sample sizes at0,1,2,5,8 years respectively surgery/control:2287/11433,1820/10309,1444/8762,784/4235,348/1219. Exact title/key retained. |
| N110 | DOC-002 p15 eTable 11 | All24 cumulative intervention incidences/95% CIs at1,2,5,8 years, surgery only; six rows TPN, endoscopy, interventional radiology, abdominal surgical procedure, abdominal wall hernia repair, cholecystectomy. Abdominal surgery excludes hernia repair/cholecystectomy. |
| N111 | DOC-002 p16 eFigure 3 | Four nutritional absolute mean trend panels0–8 years: albumin/hemoglobin/protein g/dL and vitaminD25 ug/L, surgery/nonsurgery. No printed exact point estimates. All eight curves inspected; match eTable8 differences by model/scale before comparison. |
| N112 | DOC-002 pp17–18 | Five random date assignments × ratios1:1,1:5,1:10 =15 datasets. Significant HRs in all15 for primary,secondary,death,HF,nephropathy;13 cerebrovascular,12CAD,11AF. Full model, treatment surgery/control; no individual graphic estimate has numeric annotation. |
| N113 | DOC-002 p20 eTable12 | E-value pairs for HR/upper95% limit: primary2.15/1.92;secondary2.62/2.11;death2.81/2.13;HF4.69/3.52;CAD2.27/1.55;cerebrovascular2.35/1.31;nephropathy4.46/3.29;AF1.9/1.21. All40 comparison risk-factor HRs and intervals retained, including changing reference categories. |
| N114 | DOC-003 p2 | Jan6,2019 original protocol; EHR throughDec31,2018; surgery throughDec31,2017; age18–80;BMI≥30;T2DM HbA1c>6.4% or medication;closest priorBMI required. ED admission5-day exclusion;cancer1-year;EF<20%;liver/heart/lung transplant;upperGI cancer/peptic-ulcer hospitalization exclusions. |
| N115 | DOC-003 p3 | Controls:single random surgical index date;last follow-up on/before date excluded;death before orwithin30days excluded;HbA1c<6.5 ANDno diabetes medication excluded;age<18/>80;BMI<30;closest prior BMI otherwise nearest absolute-time value. Five replicated control derivations. Base T2DM cohort approximatelyN287438, earliest datesJan1,1998–Dec31,2017. Abnormal glucose random>200mg/dL or fasting>125mg/dL. |
| N116 | DOC-003 pp4–5 | Six individual outcomes death,CAD,cerebrovascular,HF,nephropathy,AF;primary composite of all six;secondary death,MI,ischemic stroke. First occurrence after index date;baseline conditions omitted from composite definitions;individual historical outcome excluded from risk set;nephropathy excludes baseline eGFR<60/history dialysis. |
| N117 | DOC-003 p6 | Rates per100patient-years;five imputed datasets;alpha.05;95%CI;five date samples ×three matching ratios=15datasets;single1:5 dataset reported;time-varying HRs2,5,8 years;R3.5.0. |
| N118 | DOC-003 p7 | AmendmentAug2,2019;early adverse events<90days aftersurgery;late interventions until last follow-up;E-values for all8composite/individual endpoints, HR point and95%CI limitclosest null. |

## Statistical relationship inventory

| ID | Location and role | Analysis specification, population/time/contrast, and all members |
|---|---|---|
| S101 | DOC-002 p2 REPORT | Endpoint identification thresholds/codes and MDRD-based nephropathy definition. Main matching: individual endpoint and baseline-history risk-set rules. Full code table below. |
| S102 | DOC-002 pp3–4 REPORT | Adverse-event codes and intervention definitions; renal failure requires dialysis procedure combination; transfusion from blood datamart. Definitions apply to surgery cohort safety outcomes. |
| S103 | DOC-002 p6 REPORT | Eight differences control minus surgery in eight-year cause-specific rate per100patient-years;1000bootstrap samples,95%CI. Primary2.94(2.42,3.48);secondary1.53(1.18,1.87);death1.03(.76,1.29);HF1.57(1.32,1.82);CAD.52(.29,.77);cerebrovascular.28(.12,.43);nephropathy1.18(.93,1.42);AF.63(.36,.88). |
| S104 | DOC-002 p7 REPORT | All48cumulative incidence/95%CIs across eight endpoints ×time2/5/8 ×treatment. Exact source cells below. Not adjustedHR or event-rate estimates. |
| S105 | DOC-002 p8 REPORT | Sixteen fully-adjusted subgroup treatmentHRs/95%CIs plus eight treatment×subgroup interactionP values. Each original covariate removed then replaced with binary subgroup and its treatment interaction; age/eGFR split at median. Full rows below. |
| S106 | DOC-002 p9 REPORT | Eight Cox treatmentHRs/95%CIs with treatmentP/PH-testP: primary.61(.55,.69),<.001/.89;secondary.62(.53,.72),<.001/.76;death.59(.48,.72),<.001/.63;HF.38(.30,.49),<.001/.65;CAD.69(.54,.87),.002/.24;cerebrovascular.67(.48,.94),.02/.10;nephropathy.40(.31,.52),<.001/.46;AF.78(.62,.97),.03/.04. HR contrast surgery/nonsurgery. Main match fully-adjusted endpoint HRs. |
| S107 | DOC-002 pp10,19 REPORT | Twenty-four time-varying treatmentHRs/95%CIs, eight endpoints ×2/5/8years, repeated verbatim p19. Fully-adjusted Cox treatment term replaced by restricted cubic spline of observed follow-up time interacted with treatment. Exact24pairs below. Distinguish from constantHR inS106. |
| S108 | DOC-002 p11 REPORT | Four curves per panel for HbA1c% and noninsulin medication proportion over0–4years, stratified baselineBMI35 threshold. Surgery red;usualcare teal;BMI<35solid;≥35dashed. Bands present;confidence level not stated onpage. Main matching longitudinal HbA1c/medication, not composite endpoints. |
| S109 | DOC-002 p12 REPORT | All52estimate/CI/P triplets. Four-knot spline interacted with treatment compares metabolic/nutritional mean changes;two-sample proportions test medication at eachtime. Bonferroni-corrected98.8%CIs. Asterisks printed withP values retained below;asterisk decision threshold is not separately defined onpage. Modelled means and proportion differences distinguished. No unreported model covariance or sidedness inferred. |
| S110 | DOC-002 p15 REPORT | Twenty-four surgery-only intervention cumulative incidences;Kaplan–Meier;95%CI;times1,2,5,8. Sixintervention definitions fromeTable2. Abdominalsurgeryexclusions infootnote. |
| S111 | DOC-002 p16 REPORT | Eight nutritional absolute mean curves over0–8years;redsolid surgery;tealdashed nonsurgery;bands withlevelnotstatedonpage. Narrative modest nutritional deficiencies;earlypostoperative vitaminDincrease attributed as possible explanation to supplements. Compare mean levels to difference analyses only withS109 matching. |
| S112 | DOC-002 p17 REPORT | Fifteen-dataset sensitivity of fullyadjustedCoxHRs to five randomdateassignments and three matching ratios. Outcome-by-outcome significance counts N112. Reportedmanuscript one1:5dataset. |
| S113 | DOC-002 p18 REPORT | Eightfacets ×fiveiterations ×threeratios =120graphicalHR/95%CI pairs. Full outcome/time/ratio/axis keys below. Curves/pairs inspected without digitizing unprinted numerical values. |
| S114 | DOC-002 p19 REPORT | E-value definition: minimum association onrisk-ratioscale unmeasuredconfounder needs withboth treatment/outcome conditional onmeasuredcovariates to explain association. PrimaryHR.61(.55,.69),Evalue2.15,CIlimit1.92; narrative references5-componentMACE asprinted. Supplied text doesnotgive conversion formula;do not supply externalformula. |
| S115 | DOC-002 p20 REPORT | All16Evalues and40comparisonHR/95%CIs;comparisonriskfactors smoking(two contrasts),hypertension,dyslipidemia,insulin. Exact directional referencegroups below;not assumeuniformdirection. Fullyadjustedmodels;comparisonHRs shown for magnitude, not treatment effects. |
| S116 | DOC-003 p2 PLAN | Original observational matched-cohort objective; cohort entry/exclusions; index date is first qualifying bariatric surgery. Individual patient is the analysis unit. Procedure codes and age/BMI/T2DM criteria are mapped in N114. |
| S117 | DOC-003 p3 PLAN | Control algorithm starts from base T2DM cohort, excluding surgical patients even if subsequently excluded; one random surgical date; survival/BMI/eligibility rules in N115. Five replicas assess baseline characteristics, model estimates and prediction accuracy. |
| S118 | DOC-003 p3 PLAN | Printed matching orientation is each nonsurgical patient to five surgical patients, propensity score with logit link, MatchIt in R. Covariates: index date, age, BMI categories 30–35/35–40/40+, gender, insulin, Ohio/Florida, diabetes-complication composite (CAD, HF, cerebrovascular, peripheral vascular disease, neuropathy, nephropathy, dialysis). Plan p6 separately states reporting ratio 1:5. Modified Kho T2DM algorithm and all five qualifying combinations are retained below. |
| S119 | DOC-003 p4 PLAN | Primary composite has six components; secondary composite has three. First event after index; baseline conditions omitted from composite. Individual definitions include diagnostic codes and eGFR requirements. Death ascertainment uses EHR plus Social Security/State Death Indices if unknown. |
| S120 | DOC-003 p5 PLAN | Each individual endpoint excludes patients with history of that endpoint at index; nephropathy excludes baseline eGFR <60 and dialysis history. These define endpoint-specific populations. |
| S121 | DOC-003 p5 PLAN | All baseline variables specified for adjustment via p6. Demographics: DOB, gender, race, median zip income, weight, BMI, insurance, smoking, location. Medical history: hypertension, dyslipidemia, CAD, cerebrovascular disease, HF, nephropathy, neuropathy, peripheral arterial disease, AF, COPD, dialysis. Labs: HbA1c, creatinine, eGFR, SBP/DBP, LDL, HDL, triglycerides, UACR. Medications: insulin, noninsulin drugs, ACE-I/ARB, other antihypertensives, statin/other lipid drugs, aspirin, warfarin. UMLS identifiers and associated dates. No workbook formulas or cached values are supplied. |
| S122 | DOC-003 p6 PLAN | Rates from index per 100 patient-years; cumulative incidence; fully adjusted Cox PH HRs for each outcome; all baseline variables adjust confounding; treatment PH test uses Grambsch–Therneau weighted residuals. Match main constant HR models and S106. |
| S123 | DOC-003 p6 PLAN | Within each outcome dataset, five MICE imputations; predictive mean matching for numeric, logistic regression for binary, polytomous logistic regression for categorical variables; Rubin formula gives imputation-corrected SEs of estimates and contrasts. |
| S124 | DOC-003 p6 PLAN | Weight-loss percent and HbA1c over time between treatments; alpha .05; 95% CIs where applicable; secondary endpoints have no multiplicity adjustment and are exploratory; R3.5.0. No margin, sample-size/power, or stopping rule is present. |
| S125 | DOC-003 p6 PLAN | Sensitivity of fully adjusted HRs: five index-date samples × matching ratios 1:1/1:5/1:10; all 15 analyses; one 1:5 dataset reported; time-varying HRs at 2,5,8 years. No detailed spline implementation on plan page. |
| S126 | DOC-003 p7 PLAN | August 2 amendment explicitly responds to journal peer review; adds early <90-day and late intervention adverse events, hemoglobin/protein/albumin/vitamin D; E-values for all eight endpoints, HR and 95% CI limit closest to null; conditional risk-ratio definition. Disclosed amendment chronology is retained. |

## Embedded figure mapping

### DOC-002 physical p8 eFigure1 — S105

[Supplied page](../../../joi190103supp1_prod.pdf#page=8). Primary composite endpoint, surgery versus usual care, adjusted HR<1 labelled decreased risk and>1increasedrisk; axis marked0.4,1.0,1.2 with intermediate unlabeledticks; reference1.

| Subgroup variable | First level: HR (95% CI) | Second level: HR (95% CI) | Interaction P |
|---|---|---|---:|
| Gender | Male .58(.49,.69) | Female .64(.56,.74) | .35 |
| Age years | <54 .57(.47,.68) | ≥54 .57(.50,.66) | .93 |
| BMI kg/m² | <40 .62(.49,.78) | ≥40 .61(.54,.69) | .90 |
| HbA1c % | <7 .62(.52,.74) | ≥7 .60(.52,.70) | .80 |
| eGFR ml/min | <91 .61(.54,.70) | ≥91 .62(.51,.75) | .94 |
| Insulin | No .63(.55,.73) | Yes .59(.50,.70) | .53 |
| Sulfonylureas | No .63(.55,.72) | Yes .60(.49,.74) | .72 |
| Lipid-lowering medications | No .61(.52,.73) | Yes .62(.53,.71) | .98 |

All plotted estimates/intervals correspond to displayed row values. Age/eGFR median dichotomization; model replacement/interaction rule capturedS105. Caption describes consistency across subgroups, rather than equality of subgroupHRs.

### DOC-002 physical p11 eFigure2 — N106/S108

[Supplied page](../../../joi190103supp1_prod.pdf#page=11). Two panels; timeaxis0,1,2,3,4years. LeftHbA1c% ticks6.0,6.5,7.0,7.5;rightnoninsulindiabetesmedication% ticks40,60,80,100. Surgeryred/nonsurgeryteal;BMI<35solid/≥35dashed. Lefttealsolidnear7.5throughout;tealdashedapproximately7.6withslightvariation;redsurgerycurvesfallrapidlyfromabout7.4,thenreturnupward,withsolidgenerallyabovedashedafterearlyfall. Righttealcurvesnear80%;redcurvesdropinitiallyandremainwellbelowteal,solidgenerallyabovedashed. All four curves per panel andshadedbands inspected;exact numerical estimates and CIs are not annotated and therefore are not claimed. Trenddirections,units,stratificationandtime areavailableforcomparison;meanlevelsdifferfromchangecontrasts.

### DOC-002 physical p16 eFigure3 — N111/S111

[Supplied page](../../../joi190103supp1_prod.pdf#page=16). Timeaxis0,2,4,6,8years. Fourpanels:albumin(g/dL) ticks3.4,3.6,3.8;vitaminD25(ug/L) ticks30,35;hemoglobin(g/dL) ticks10.5,11,11.5,12;protein(g/dL) ticks6.4,6.6,6.8,7.0. Redsolidsurgery andtealdashednonsurgery,shadedbands. Albuminrednear3.8mostoftimebeforefallat8years,tealnear3.65–3.75afterearlydecline. VitaminDredrapidriseabove35thenfluctuates/approachesteal;tealincreasessteadilyfromabout27.5to32.5. Hemoglobinbothfluctuateanddecline,withredfalllate;proteinredgenerallybelowtealwithlatefall. Allcurvesinspected;exactpoints/intervalsnotprinted. CaptioneTable8pointerandnutritionalinterpretationretained.

### DOC-002 physical p18 eFigure4 — S113

[Supplied page](../../../joi190103supp1_prod.pdf#page=18). Eightfacets:primary,secondary,all-causemortality,CAD,cerebrovasculardisease,HF,nephropathy,Afib. Eachfacetincludesiterations1–5withallthree matchingratios. Graphiclegend labels1:1(redcircle),5:1(greentriangle),10:1(bluesquare);narrative labels1:1,1:5,1:10. YaxisHR(95%CI),ticks0,.2,.4,.6,.8,1,1.2;null1isvisuallyavailable. No120pairs haveprintednumericalannotations. Every facet, iteration and ratio was inspected;primaryaround.6;secondary.5–.7;death.5–.7;CAD.6–.9;cerebrovascular.55–.8;HF.3–.45;nephropathy.35–.45;AF.65–.95. Thesearevisualranges,notexactextractionvalues. WiderCIvariationgenerally1:1;allprimary/secondary/death/HF/nephropathyCIupperlimitsbelow1;someCAD/cerebrovascular/AFintervalsreach/cross1. Exactsignificancecountsareprintedonnarrativep17(N112). No numerical digitization or external model inference was undertaken.

## Complete source-linked text blocks

The following are unedited usable source transcriptions. Page headings identify physicalPDFpage; repeated table onp19 isretained. Every displayed table row and definition is covered by the inventories above. Textlayeromissionofembeddedfigures isclosedbythevisualmappingabove. Diagnosis identifiers are retainedverbatim toavoid changingendpointdefinitions. These text blocks are scientific evidence transcriptions, not classifications.

### DOC-002 physical PDF page 1 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=1)

```text
                                                   Supplementary Online Content 1


Aminian A, Zajichek A, Arterburn DE, et al. Association of metabolic surgery with major adverse cardiovascular outcomes in patients
with type 2 diabetes and obesity. JAMA. doi:10.1001/jama.2019.14231


eTable 1. Diagnosis and Procedure Codes………………………………………………........................................................................2
eTable 2. Diagnosis and Intervention Codes for Adverse Events of Metabolic Surgery…………………………………………………………….3
eTable 3. Class of Diabetes Medications at the Index Date.…………………………………………..……………………………………...................5
eTable 4. Cause-Specific Event Rates (%) per 100 Patient-Years of Follow-up at 8 Years, for Each Study Outcome
Stratified by Surgical and Non-surgical Patients.……………………………………………..…………………………………...................................6
eTable 5 Cumulative Incidence Estimates (%) and 95% Confidence Intervals at 2, 5, and 8 Years After the
Index Date for Each Study Outcome Stratified by Surgical and Non-surgical Patients……………………………………………..……………….7
eFigure 1. Association of Metabolic Surgery Compared With Usual Care for the Primary Composite Endpoint in
Key Subgroups in the Fully-Adjusted Cox Models……………………………………….…….…………………………………...................................8
eTable 6 Hazard Ratios (95% CIs) and P Values From Cox Models Comparing the Relative Instantaneous Risk of
Each Outcome for Surgical Vs. Non-surgical Patients………………………………………………………………………………................................9
eTable 7. Time-Varying Hazard Ratios and 95% CIs at 2, 5, and 8 Years After the Index Date Comparing Surgical
and Non-surgical Patients From a Fully-Adjusted Cox Model for Each Outcome………………………………………………………………………..10
eFigure 2. Mean Trend Curve of HbA1c (%) and Proportions of Patients Taking Non-insulin Diabetes Drugs Over
Four Years of Follow-up Categorized by the Treatment Group (Metabolic Surgery Vs. Usual Care) and the
BMI (≥35 vs. <35 kg/m2) at the Index Date……………………………………………………………………………………………………………………………….11
eTable 8. Average Change in Metabolic and Nutritional Variables From Baseline and in Proportions of Patients Taking
Diabetes and Cardiovascular Medications (%) at 1, 2, 5, and 8 Years of Follow-up in Surgical vs. Non-surgical
Patients………………………………………………………………………………............................................................................................12
eTable 9. Total Number of Observations and Number of Distinct Patients With Available Measurements After Each
Time-Point Following the Index Date for Metabolic and Nutritional Values by Treatment………………………………………………………….13
eTable 10. Sample Size for Computing Proportions of Patients Taking Diabetes and Cardiovascular Drugs Over Time
at 0, 1, 2, 5, and 8 Years After the Index Date by Treatment Group………..……………………………………………………………………..........14
eTable 11. Cumulative Incidence Estimates (%) and 95% CIs for Interventions at 1, 2, 5, and 8 Years After Metabolic
Surgery…………..………………………………………………………………….............................................................................................15
eFigure 3. Mean Trend Curve of Nutritional Variables of Interest Over Eight Years of Follow-Up in the Surgical
and Non-surgical Patients………………………………………………………………………………....................................................................16
Sensitivity Analyses………………………………………………………………......................................................................................17
         Matching and Index Date Sampling...……………………………………………………………………………………………………………………..17
         eFigure 4. Hazard Ratios and 95% Confidence Intervals for Metabolic Surgery Versus No Surgery From
         Fully-Adjusted Cox Models for Each Outcome for Five (5) Iterations of Index Date Random Sampling and
         Three (3) Different Matching Ratios (Total of 15 Datasets)...……………………………………………………………………………………….18
         Time-Varying Hazard Ratios………...………………………......….………………………………………………………………………………………..19
         E-Value…...………………………………………………………………….………………………………………………………………………………………………….19
         eTable 12. E-Value for the Effect of Metabolic Surgery on Each Outcome (and its Upper Limit of 95% CI) in
         Fully-Adjusted Cox Models….…………………………………………………...…………….…….........................................................20


This supplementary material as been provided by the authors to give readers additional information about their work.




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 2 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=2)

```text
                                                                                                                  2


eTable 1. Diagnosis and Procedure Codes
 Atrial fibrillation                      ICD9: 427.31
                                          ICD10: i48.0, i48.1, i48.2, i48.91
                                          CPT: 93650, 93653, 93656, 93657
 Bariatric surgery                        CPT-4: 43633, 43634, 43770, 43775, 43644, 43645, 43659, 43842,
                                          43843, 43844, 43845, 43846, 43847
                                          ICD9: 44.31, 43.82, 44.95, 43.89, 44.38, 44.39, 44.68
                                          HCPCS: S2082, S2085
 Cancer                                   ICD9: 140.XX-172.XX, 174.XX-209.XX
                                          ICD10: C00.XX-C43.XX, C45.XX-C96.XX, D03.XX, D3A.XX, D45.XX
 Cerebrovascular event                    ICD9 (diagnoses): 433.X1, 434.X1, 436.0, 430.X, 431.X
                                          ICD9 (procedure): 38.12, 0.61, 0.63
                                          CPT-4: 37215, 37216, 0075T, 0076T, 35301, 37205, 37206
 COPD                                     ICD9: 491.0, 491.1, 491.2X, 491.8, 491.9, 492.0, 492.8, 496
 Coronary artery disease                  ICD9 (diagnoses): 410.X, 411.X, 411.X AND 414.X
                                          ICD9 (procedure): 36.01, 36.02, 36.03, 36.05, 36.06, 36.07, 36.10,
                                          36.11, 36.12, 36.13, 36.14, 36.15, 36.16, 36.17, 36.19, 36.31, 36.32,
                                          36.33, 36.64
                                          CPT-4: 92982, 92984, 92995, 92996, 92980, 92981, 33510, 33511,
                                          33512, 33513, 33514, 33516, 33517, 33518, 33519, 33521, 33522,
                                          33523, 33530, 33533, 33534, 33535, 33536, 93539, 93540
 Diabetic neuropathy                      ICD9: 250.6, 357.2
 Dyslipidemia                             ICD9: 272.0, 272.1, 272.2, 272.3, 272.4
 GI Cancer                                ICD9: 150.X, 151.X, 152.X, 157.X, 199.X, 531.X, 532.X, 533.X
 Heart failure                            ICD9: 428.0, 428.1, 428.20, 428.21, 428.22, 428.23, 428.30, 428.31,
                                          428.32, 428.33, 428.40, 428.41, 428.42, 428.43, 428.9
 Hypertension                             ICD9: 401.X, 402.X, 403.X, 404.X, 405.X
 Ischemic stroke                          ICD-9: 433.X1, 434.X1
                                          ICD-10: i63.X and i63.XX and i63.XXX
 Liver, lung, heart transplant            ICD9: V42.1, V42.6, V42.7, V42.83, V42.84
 Myocardial infarction                    ICD-9: 410.X, 410.XX
                                          ICD-10: i21.X and i21.XX, i22.X and i22.XX, i23.X and i23.XX
 Nephropathy                              >= two (2) measures of eGFR less than 60 mL/min separated by at
                                          least 90 days without any intervening values >= 60 mL/min. The
                                          eGFR is approximated using MDRD equation.
 Peripheral arterial disease              ICD9: 440.20, 440.21, 440.22, 440.23, 440.24, 440.29, 440.31,
                                          440.32, 443.81, 443.89, 443.9, 447.1, 249.7, 250.7
 *Bolded text indicates it must be a primary diagnosis




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 3 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=3)

```text
                                                                                                         3

eTable 2. Diagnosis and Intervention Codes for Adverse Events of Metabolic Surgery*
 Diagnosis Codes
                               Diagnostic code 518.51, 518.81, 997.39. Or, procedure code for
 Acute pulmonary
                               intubation (96.04), tracheostomy (31.1, 31.29), or mechanical
 complications
                               ventilation (31.74, 93.7, 93.9, 96.7, 96.71, 96.72).
                               Diagnostic code for acute renal failure (584.9, 586, 997.5, V56.0,
 Acute renal failure requiring
                               V56.1) when combined with a procedure code for hemodialysis (38.95,
 dialysis
                               39.95, 54.98).
                               Diagnostic codes for deep vein thrombosis (451.2, 451.81, 451.83,
                               451.84, 451.89, 451.9, 453.4, 453.40, 453.41, 453.42, 453.8, 671.30 to
 Venous thromboembolism        671.35, 671.40, 671.42, 671.43, 671.90 to 671.94).
 (deep vein thrombosis and     Diagnostic codes for pulmonary embolism (415.1, 416.2, 453.1, 453.2,
 pulmonary embolism)           453.9, 639.6, 673.2).
                               Procedure code for pulmonary embolism (36013, 36014, 36015,
                               37191).
                               Extracted from Cleveland Clinic blood datamart with appropriate
 Transfusion
                               identification codes
 Intervention and Procedure Codes
 Total parenteral nutrition    ICD-9 procedure code 99.15
                               43200-04, 43215-28, 43232-36, 43239, 43243, 43245-51, 43255-58,
 Endoscopic intervention       43450, 43453, 43456, 43458, 44360, 44361, 44376.
                               42.21-42.29, 44.22, 44.43, 45.11-45.14
                               36000, 36556, 36558, 36561, 36563, 36565, 36566, 36569, 36571-
 Interventional radiology
                               36590
 Cholecystectomy               47490, 47562-47564, 47600-47610
                               44050, 49560-49572, 49585-49590, 49650-49659, 49900, 43659,
 Repair of abdominal wall
                               S2075, S2077
 hernia
                               53.1x-53.8x
                               Diagnostic laparoscopy (ICD-9 54.21) and exploratory laparotomy
                               (54.11)

                               Lysis of adhesions: ICD-9 54.51, 54.59

                               Repair of internal hernia: ICD-9 53.9

                               RYGB, AGB, sleeve and VGB:
                               ICD-9: 43.82, 43.89, 44.31, 44.38, 44.39, 44.68, 44.95
                               CPT-4: 43633, 43644, 43645, 43770, 43773, 43775, 43776, 43842,
                               43843, 43844, 43846, 43847, 43848, 43888, S2082, S2085

                               Duodenal switch: ICD-9: 43.7, 45.51, 45.91
 Abdominal surgical
 procedure                     Revision GJ: CPT-4: 43860,43865

                               Additional revisional bariatric procedures:
                               ICD-9: 44.0 to 44.03, 44.89, 45.28, 45.29, 45.51, 46.01 to 46.03, 46.2,
                               46.64, 54.5,
                               54.75, 54.95
                               CPT-4: 43610, 44850




                               Percutaneous/laparoscopic:
                               ICD-9: 39.41, 39.98, 46.71, 46.73, 46.75, 46.94, 50.61, 54.0, 54.12,
                               54.19, 54.20, 54.22-.29, 54.91, 54.92


© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 4 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=4)

```text
                                                                                                                                   4

                                        CPT-4: 43653, 44180, 44186, 44200,44202, 44203, 44238, 49000,
                                        49002, 49010, 49020, 49021, 49040, 49041, 49060, 49061, 49320,
                                        49322, 49323, 49329

                                        Abscess: CPT-4: 49020,49406

                                        Reoperation ulcers: CPT-4: 43840, 44180, 44602, 49905

                                        PEG tube/revision NOS/VGB: CPT-4: 43750, 43760, 43761, 43848,
                                        43860, 44373

                                        Other procedures:
                                        ICD-9: 42.81, 42.84, 42.9, 42.92, 43.0, 43.11, 43.19, 43.42, 43.5, 43.7,
                                        43.99, 44.13, 44.29, 44.49, 44.5, 44.62, 44.63, 44.99, 45.02, 45.19,
                                        45.61, 45.62, 45.91, 46.39, 46.62, 46.71, 46.73, 46.75, 46.79, 46.81,
                                        46.82, 46.85, 46.93, 46.99
                                        CPT-4: 10022, 10030, 10160, 43300, 43305, 43310, 43312, 43500,
                                        43631, 43752,
                                        43832, 43840, 43845, 43850, 43870, 43880, 43999, 44005, 44021,
                                        44055,
                                        44120, 44121, 44125, 44130, 44500, 44602, 44620, 44799, 48000,
                                        49080, 49407, 49440, 49441, 49446, 49451, 49460, 49999

 * ICD-9 and CPT-4 diagnosis and procedure codes were adapted and modified from:
           •   Li RA, Liu L, Arterburn D, et al. Five-year Longitudinal Cohort Study of Reinterventions After Sleeve Gastrectomy
               and Roux-en-Y Gastric Bypass. Ann Surg. 2019 Jun 7. doi:10.1097/SLA.0000000000003401.
           • Flum D, Belle S, King W, et al. Longitudinal Assessment of Bariatric Surgery (LABS) Consortium. Perioperative
               safety in the Longitudinal Assessment of bariatric Surgery. N Engl J Med. 2009;361:445-54.




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 5 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=5)

```text
                                                                           5

eTable 3. Class of Diabetes Medications at the Index Date
    Diabetes Medications        Metabolic Surgery    Matched Nonsurgical
                                     (N=2287)              (N=11435)
 Alpha-glucosidase Inhibitors         6 (0.3%)              26 (0.2%)
 Amylin Analog                        7 (0.3%)              27 (0.2%)
 Biguanides                       1530 (67.9%)           7606 (66.5%)
 Bile Acid Sequestrants               8 (0.3%)              55 (0.5%)
 Dopamine Receptor Agonists           3 (0.1%)              14 (0.1%)
 DPP-4 Inhibitors                   214 (9.4%)           1202 (10.5%)
 GLP-1 Receptor Agonists           270 (11.8%)             841 (7.4%)
 Insulins                          776 (33.9%)           3806 (33.3%)
 Meglitinides                        20 (0.9%)              79 (0.7%)
 Sulfonylureas                     509 (22.3%)           3404 (29.8%)
 SGLT2 Inhibitors                    43 (1.9%)             143 (1.3%)
 Thiazolidinediones                286 (12.5%)            1083 (9.5%)




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 6 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=6)

```text
                                                                                                                 6

eTable 4. Cause-Specific Event Rates (%) per 100 Patient-Years of Follow-up at 8 Years, for Each Study
utcome Stratified by Surgical and Non-surgical Patients
                                            Rate per 100                  Difference in event rate per
                                           patient-yearsa                      100 patient-years
                                      Surgical    Nonsurgical            Estimate    95% Confidence
                                       Group          Group                              Intervalb
 Primary composite                      4.51            7.45               2.94         (2.42, 3.48)
 Secondary composite                    2.11            3.64               1.53         (1.18, 1.87)
 All-cause mortality                    1.19            2.22               1.03         (0.76, 1.29)
 Heart failure                       0.92 (1.84)     2.49 (3.7)            1.57         (1.32, 1.82)
 Coronary artery disease             1.03 (1.98)    1.55 (3.36)            0.52         (0.29, 0.77)
 Cerebrovascular disease             0.45 (1.55)    0.73 (2.74)            0.28         (0.12, 0.43)
 Nephropathy                         0.89 (1.77)    2.07 (3.47)            1.18         (0.93, 1.42)
 Atrial fibrillation                 1.14 (2.16)    1.77 (3.42)            0.63         (0.36, 0.88)
 a
  The composite rates of death with each individual outcome are also shown in parentheses.
 b
  95% bootstrap CI’s (1000 samples) for the difference in 8-year event rate per 100 patient-years (nonsurgical
 control group – metabolic surgery) for each outcome and treatment group.




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 7 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=7)

```text
                                                                                                       7

eTable 5. Cumulative Incidence Estimates (%) and 95% Confidence Intervals at 2, 5, and 8 Years After
the Index Date for Each Study Outcome Stratified by Surgical and Non-surgical Patients
                  Cumulative incidence estimates (%) and 95% confidence intervals
                               Year 2                   Year 5                   Year 8
                     Surgical Nonsurgical      Surgical    Nonsurgical  Surgical    Nonsurgical
                      Group         Group       Group         Group      Group         Group
 Primary                7.6           12.2       17.7          30.4       30.8          47.7
 composite           (6.4,8.8)    (11.5,12.8) (15.6,19.7)   (29.4,31.5) (27.6,34)    (46.1,49.2)

 Secondary                3.3         5.5           8.8         15.5           17           27.6
 composite             (2.5,4.1)   (5.1,6.0)    (7.2,10.4)   (14.7,16.4)   (14.3,19.7)   (26.2,29.0)

 All-cause                1.8         3.2          4.9          10.1           10           17.8
 mortality             (1.2,2.4)   (2.8,3.5)    (3.7,6.1)    (9.4,10.8)    (7.8,12.2)    (16.6,19.0)

 Heart failure            1.5         4.2          3.8          10.4           6.8          18.9
                       (1.0,2.1)   (3.8,4.6)    (2.6,4.9)    (9.7,11.2)     (4.9,8.6)    (17.6,20.2)

 Coronary artery          1.7         2.9          4.2           6.8           7.9          11.6
 disease               (1.1,2.3)   (2.6,3.3)    (3.1,5.3)     (6.2,7.4)     (5.9,9.8)    (10.5,12.6)

 Cerebrovascular          0.7         1.3          2.2           3.1           4.1           5.6
 disease               (0.3,1.1)   (1.1,1.5)    (1.4,3.0)     (2.7,3.5)     (2.7,5.5)     (4.9,6.3)

 Nephropathy              1.4         2.3          3.9           8.8           6.1          16.3
                       (0.8,2.0)   (2.0,2.7)    (2.8,5.1)     (8.0,9.5)     (4.4,7.8)    (15.0,17.6)

 Atrial fibrillation      2.3         2.7          4.8           7.6           7.9          13.6
                       (1.6,3.1)   (2.4,3.0)    (3.6,6.0)     (7.0,8.2)     (6.1,9.7)    (12.5,14.7)




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 8 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=8)

```text
                                                                                                                                      8



     eFigure 1. Association of Metabolic Surgery Compared With Usual Care for the Primary
            Composite Endpoint in Key Subgroups in the Fully-Adjusted Cox Models




Adjusted hazard ratios were obtained after individually removing the original variable from the fully-adjusted Cox model and
replacing it with the dichotomous sub-group variable as well as its interaction with the treatment variable. For example, the continuous
BMI covariate was replaced by the dichotomous version and it’s interaction with the treatment. P-values for the interaction between
each variable and the surgical indicator from the fully-adjusted model are also displayed. Age and eGFR were categorized based on
their median values. The figure would indicate that the results were consistent across key subgroups.




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 9 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=9)

```text
                                                                                         9



eTable 6. Hazard Ratio’s (95% CIs) and P Values From Cox Models Comparing the Relative
Instantaneous Risk of Each Outcome for Surgical Vs. Non-surgical Patients
 Outcome                          HR (95% CI)            P-value      PH P-value*
 Primary composite                0.61 (0.55, 0.69)      <0.001       0.89
 Secondary composite              0.62 (0.53, 0.72)      <0.001       0.76
 All-cause mortality              0.59 (0.48, 0.72)      <0.001       0.63
 Heart failure                    0.38 (0.30, 0.49)      <0.001       0.65
 Coronary artery disease          0.69 (0.54, 0.87)      0.002        0.24
 Cerebrovascular disease          0.67 (0.48, 0.94)      0.02         0.10
 Nephropathy                      0.40 (0.31, 0.52)      <0.001       0.46
 Atrial fibrillation              0.78 (0.62, 0.97)      0.03         0.04
 * P-values testing the proportion-hazards assumption for each outcome.




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 10 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=10)

```text
                                                                                                                                                        10

eTable 7. Time-Varying Hazard Ratios and 95% CIs at 2, 5, and 8 Years After the Index Date
Comparing Surgical and Non-surgical Patients From a Fully-Adjusted Cox Model for Each
Outcome
                                                  Years since index date
 Outcome                                   2                 5                 8
 Primary                           0.57 (0.49, 0.65) 0.78 (0.66, 0.93) 0.79 (0.64, 0.97)
 Secondary                         0.51 (0.42, 0.63) 0.82 (0.65, 1.04) 0.73 (0.56, 0.95)
 All-cause mortality               0.43 (0.33, 0.57) 0.69 (0.50, 0.95) 0.80 (0.56, 1.15)
 Heart failure                     0.31 (0.23, 0.41) 0.40 (0.31, 0.53) 0.52 (0.35, 0.79)
 Coronary artery disease           0.52 (0.38, 0.69) 1.03 (0.71, 1.51) 0.99 (0.64, 1.51)
 Cerebrovascular disease           0.68 (0.45, 1.04) 1.29 (0.77, 2.15) 0.60 (0.28, 1.25)
 Nephropathy                       0.41 (0.30, 0.58) 0.40 (0.26, 0.61) 0.46 (0.30, 0.70)
 Atrial fibrillation               0.68 (0.52, 0.89) 0.88 (0.62, 1.25) 0.65 (0.42, 1.00)
The treatment term in the fully-adjusted Cox models above were replaced with a restricted cubic-spline on the observed follow-up time interacted with
the treatment group.




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 11 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=11)

```text
                                                                                       11

 eFigure 2. Mean Trend Curve of HbA1c (%) and Proportions of Patients Taking Non-insulin
Diabetes Drugs Over Four Years of Follow-up Categorized by the Treatment Group (Metabolic
         Surgery Vs. Usual Care) and the BMI (≥35 vs. <35 kg/m2) at the Index Date




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 12 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=12)

```text
                                                                                                                                                                                 12


eTable 8. Average Change in Metabolic and Nutritional Variables From Baseline and in Proportions of Patients Taking
Diabetes and Cardiovascular Medications (%) at 1, 2, 5, and 8 Years of Follow-up in Surgical vs. Non-surgical Patients
                                                                                             Time since index date (years)
                                                              1                                2                             5                                   8
 Category      Variable                           Estimate (98.8%         P-       Estimate (98.8%       P-      Estimate (98.8%            P-       Estimate (98.8%         P-
                                                        CI)              value           CI)           value            CI)                value           CI)              value
 Metabolic
               Weight (lbs.)                      -56.6 (-57.1, -56.1)   <0.001*   -73.7 (-74.4, -73.0)   <0.001*   -45.2 (-45.9, -44.6)   <0.001*   -44.8 (-45.5, -44.1)   <0.001*
               Weight (kg)                        -25.7 (-25.9, -25.4)   <0.001*   -33.4 (-33.7, -33.1)   <0.001*   -20.5 (-20.8, -20.2)   <0.001*   -20.3 (-20.6, -20.0)   <0.001*
               HbA1c (%)                            -1.5 (-1.6, -1.4)    <0.001*     -1.6 (-1.7, -1.5)    <0.001*     -1.0 (-1.1, -0.9)    <0.001*     -1.1 (-1.2, -1.0)    <0.001*
 Nutritional
               Protein (g/dL)                        -0.5 (-0.6, -0.5)  <0.001*      -0.5 (-0.5, -0.5)   <0.001*       -0.3 (-0.3, -0.3)  <0.001*      -0.3 (-0. 3, -0.3)  <0.001*
               Albumin (g/dL)                        -0.3 (-0.3, -0.3)  <0.001*      -0.2 (-0.2, -0.1)   <0.001*       -0.1 (-0.1, -0.1)  <0.001*       -0.2 (-0.2, -0.1)  <0.001*
               Hemoglobin (g/dL)                     -0.6 (-0.6, -0.5)  <0.001*      -0.4 (-0.4, -0.3)   <0.001*         -0.1 (-0.2, 0)   <0.001*       -0.2 (-0.2, -0.1)  <0.001*
               Vitamin D 25 (ug/L)                     6.4 (5.0, 7.7)   <0.001*       4.1 (2.6, 5.7)     <0.001*        -0.9 (-2.7, 0.9)   0.19          -1.4 (-4.4, 1.7)   0.27
 Medications (%)
               Non-insulin diabetes medications     -50 (-52.9, -47.1)  <0.001* -51.5 (-54.6, -48.3) <0.001* -47.4 (-51.9, -42.9) <0.001* -37.9 (-45.3, -30.6) <0.001*
               Insulin                              -8.3 (-11.1, -5.4)  <0.001*     -9.1 (-12.3, -5.9)   <0.001*      -9.1 (-13.7, -4.6)  <0.001*      -8.1 (-15.5, -0.7)  0.008*
               Renin-Angiotensin system             -25 (-28.1, -21.9)  <0.001* -26.6 (-30.1, -23.1) <0.001* -27.5 (-32.3, -22.7) <0.001*             -26.4 (-34, -18.8)   <0.001*
               inhibitors
               Other antihypertensive                 -2.7 (-5.6, 0.3)    0.02       -3.4 (-6.7, -0.2)    0.007*      -7.7 (-12.1, -3.2)  <0.001*     -10.6 (-17.6, -3.7)  <0.001*
               medications
               Lipid-lowering medications          -16.7 (-19.8, -13.5) <0.001* -21.1 (-24.5, -17.6) <0.001* -26.4 (-31.1, -21.7) <0.001* -28.3 (-35.8, -20.8) <0.001*
               Aspirin                             -24.5 (-27.1, -21.9) <0.001* -24.4 (-27.4, -21.4) <0.001* -25.9 (-30.2, -21.6) <0.001*                 -27 (-34, -20)   <0.001*
A four-knot spline interacted with treatment was used for comparing mean changes in metabolic and nutritional variables, and two-sample proportions test was used for medication
data at each time point.
98.8% (Bonferroni-corrected) confidence intervals are displayed with each estimate.




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 13 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=13)

```text
                                                                                              13




eTable 9. Total Number of Observations and Number of Distinct Patients With Available
Measurements After Each Time-Point Following the Index Date for Metabolic and
Nutritional Values by Treatment
                                       Metabolic Surgery               Nonsurgical Group
   Variable       Time since         Total no.     No. distinct      Total no.     No. distinct
                  index date       observations      patients      observations      patients
                    (years)
 HbA1c                 0                9291                1716      54614            8076
                       1                6413                1290      44208            7172
                       2                4784                 970      34713            6087
                       5                1970                 494      13192            2917
                       8                 630                 187       3196             851
 Weight                0               61646                2278     263913           10718
                       1               42497                1790     218461            9733
                       2               33071                1434     174631            8436
                       5               14586                 790      69110            4244
                       8                5034                 351      17359            1318
 Albumin               0               19778                1969      94023            8871
                       1               13629                1516      77739            7971
                       2               10547                1207      62365            6845
                       5                4605                 640      24881            3395
                       8                1730                 265       6416            1035
 Hemoglobin            0               30043                2279     127046            8802
                       1               18137                1525     105555            7907
                       2               14201                1213      84975            6768
                       5                6382                 649      34037            3382
                       8                2293                 271       8626            1031
 Protein               0               18628                1965      83880            8824
                       1               12682                1511      68872            7922
                       2                9782                1203      54884            6785
                       5                4156                 639      21598            3345
                       8                1541                 262       5651            1013
 Vitamin D             0                5360                1409      11438            3660
 (25)                  1                3696                1103       9469            3208
                       2                2583                 800       7513            2693
                       5                1038                 373       2942            1241
                       8                 350                 138        771             358




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 14 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=14)

```text
                                                                                    14




eTable 10. Sample Size for Computing Proportions of Patients Taking Diabetes and
Cardiovascular Drugs Over Time at 0, 1, 2, 5, and 8 Years After the Index Date by
Treatment Group
     Time since index      Metabolic        Nonsurgical
       date (years)        Surgery            Group
 0                           2287             11433
 1                           1820             10309
 2                           1444              8762
 5                            784              4235
 8                            348              1219




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 15 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=15)

```text
                                                                                                                                15




eTable 11. Cumulative Incidence Estimates (%) and 95% CIs for Interventions at 1, 2, 5, and 8 Years After
Metabolic Surgery
                                                                        Years since metabolic surgery
 Intervention                                            1                    2                 5                    8
 Total parenteral nutrition                         1.5 (1, 2.1)        1.8 (1.2, 2.4)    2.1 (1.5, 2.8)       2.9 (1.9, 3.9)
 Endoscopy                                       23.9 (22.1, 25.7)     30.1 (28, 32.1)  44.2 (41.6, 46.8)      52 (48.7, 55)
 Interventional radiology                          2.6 (1.9, 3.2)       3.3 (2.5, 4.1)    6.8 (5.4, 8.1)     10.4 (8.3, 12.4)
 Abdominal surgical procedure*                     5.9 (4.9, 6.9)       8.1 (6.9, 9.3)  12.1 (10.4, 13.7)   13.8 (11.8, 15.7)
 Repair of abdominal wall hernia                   2.8 (2.1, 3.6)       5.7 (4.6, 6.8)   8.7 (7.3, 10.2)      11.1 (9.1, 13)
 Cholecystectomy                                   1.4 (0.9, 1.9)       3.5 (2.6, 4.3)    6.5 (5.2, 7.8)      9.7 (7.7, 11.7)
 Cumulative incidence estimates (%) by the Kaplan-Meier method.
 *Not including repair of abdominal wall hernia and cholecystectomy.




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 16 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=16)

```text
                                                                                                               16


eFigure 3. Mean Trend Curve of Nutritional Variables of Interest Over Eight Years
             of Follow-Up in the Surgical and Non-surgical Patients




       Although nutritional deficiencies have been described after metabolic surgery, longitudinal comparisons in
       this cohort of patients showed only modest nutritional deficiencies after metabolic surgery compared with
       nonsurgical patients who had usual care (eTable 8 for estimates).

       Routine administration of vitamins and supplements after surgery may explain the observed increase in
       vitamin D level in surgical patients in the first few years following metabolic surgery.




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 17 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=17)

```text
                                                                                                                    17


SENSITIVITY ANALYSES
   A. Matching and index date sampling
      It was of interest to assess the sensitivity of the hazard ratio estimates from the fully-adjusted Cox models
      to two (2) components of the process used in obtaining non-surgical controls:


                –     Random-sampling of index dates
                –     Matching ratio

       The surgical index dates were randomly assigned to non-surgical controls five (5) times, and the matching
       ratio was tested at 1:1, 1:5, and 1:10, thus creating 15 datasets. The full-adjusted Cox models were run on
       each dataset (for all outcomes) and the hazard ratios and 95% confidence intervals for the treatment
       variable were obtained for each. The eFigure 4 displays the sampled index date iteration on the x-axis, the
       hazard ratio estimate on the y-axis, and individual curves for each matching ratio, for each outcome.


       As expected, the most amount of variation across the index date sampling datasets comes from a lower
       matching ratio (1:1) but stabilizes as the matching ratio gets larger. Overall, the differences in hazard ratios
       comparing the risk of 8 endpoints in surgical patients versus nonsurgical patients appear to be negligible in
       absolute terms in 15 datasets, and the estimates reported in the manuscript from a single dataset (with 1:5
       matching) would be reasonable.

       In the examined 15 datasets, HRs for primary and secondary composite endpoints, all-cause mortality, heart
       failure, and nephropathy were consistently significant. The HRs comparing the risk of incident
       cerebrovascular disease, coronary artery disease, and atrial fibrillation in surgical patients versus
       nonsurgical patients were significant in 13, 12, and 11 datasets, respectively.




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 18 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=18)

```text
                                                                             18


  eFigure 4. Hazard Ratios and 95% Confidence Intervals for Metabolic Surgery
 Versus No Surgery From Fully-Adjusted Cox Models for Each Outcome for Five
 (5) Iterations of Index Date Random Sampling and Three (3) Different Matching
                            Ratios (Total of 15 Datasets)




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 19 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=19)

```text
                                                                                                                    19


   B. Time-varying hazard ratios
      It was of interest to assess estimates of time-varying hazard ratios for surgical vs. non-surgical patients at 2,
      5, and 8 years following the index date. The treatment term in the fully-adjusted Cox models above were
      replaced with a restricted cubic-spline on the observed follow-up time interacted with the treatment group.
      eTable 4 displays adjusted hazard ratios and 95% confidence intervals at 2, 5, and 8 years after the index
      date.


eTable 7. Time-Varying Hazard Ratios and 95% CIs at 2, 5, and 8 Years After the Index
Date Comparing Surgical and Non-surgical Patients From a Fully-Adjusted Cox Model for
Each Outcome
                                              Years since index date
 Outcome                               2                 5                 8
 Primary                       0.57 (0.49, 0.65) 0.78 (0.66, 0.93) 0.79 (0.64, 0.97)
 Secondary                     0.51 (0.42, 0.63) 0.82 (0.65, 1.04) 0.73 (0.56, 0.95)
 All-cause mortality           0.43 (0.33, 0.57) 0.69 (0.50, 0.95) 0.80 (0.56, 1.15)
 Heart failure                 0.31 (0.23, 0.41) 0.40 (0.31, 0.53) 0.52 (0.35, 0.79)
 Coronary artery disease       0.52 (0.38, 0.69) 1.03 (0.71, 1.51) 0.99 (0.64, 1.51)
 Cerebrovascular disease       0.68 (0.45, 1.04) 1.29 (0.77, 2.15) 0.60 (0.28, 1.25)
 Nephropathy                   0.41 (0.30, 0.58) 0.40 (0.26, 0.61) 0.46 (0.30, 0.70)
 Atrial fibrillation           0.68 (0.52, 0.89) 0.88 (0.62, 1.25) 0.65 (0.42, 1.00)



   C. E-Value
   As described by VanderWeele and Ding, the E-value (expressed on the risk ratio scale) represents the minimum
   strength of association that an unmeasured confounder would need to demonstrate for both the treatment and
   outcome, conditional on the measured covariates, to fully explain away a specific treatment–outcome
   association. A small E-value implies little unmeasured confounding would be needed to explain away an effect
   estimate. It was of interest to estimate the E-values (both for the HR estimates, and for their upper limit of 95%
   CI) of the 8 major study endpoints (eTable 12).
   In the current study, the observed association of metabolic surgery on the primary outcome was HR of 0.61
   [95% CI 0.55 to 0.69]. Based on the calculated E-value for the primary end-point, the observed HR of 0.61
   could be explained away by an unmeasured confounder that was associated with both the treatment and the
   outcome by a risk ratio of 2.15-fold each, above and beyond the measured confounders, but weaker
   confounding could not do so; the confidence interval of HR could be moved to include the null by an
   unmeasured confounder that was associated with both the treatment and the outcome by a risk ratio of 1.92-fold
   each, above and beyond the measured confounders, but weaker confounding could not do so.
   In other words, the calculated E-value of 2.15 would mean that residual confounding could explain the observed
   association if there exists an unmeasured covariate having a relative risk association at least as large as 2.15
   with both 5-component MACE and with metabolic surgery. Hazard ratios were calculated for 4 well known risk
   factors associated with the study endpoints (smoking, hypertension, dyslipidemia and insulin use) (eTable 12).
   E-values well above the HR’s for these known risk factors would suggest there is an unmeasured or unknown
   confounder that has a substantially greater effect on the endpoint than well-established cardiovascular risk
   factors, which is unlikely.
   Examining the E-values for all secondary study endpoints and comparing with the HR estimates of known
   cardiovascular risk factors for these endpoints (eTable 12) indicates it would be highly unlikely that an
   unmeasured confounder exists that could explain away the favorable association between metabolic surgery and
   study endpoints.




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 physical PDF page 20 — REPORT

[Supplied source](../../../joi190103supp1_prod.pdf#page=20)

```text
                                                                                                                             20



eTable 12. E-Value for the Effect of Metabolic Surgery on Each Outcome (and its Upper
Limit of 95% CI) in Fully-Adjusted Cox Models
      Outcome            E-value for HR         E-value for             Variable                Level                HR (95% CI)*
                            estimate           upper limit of
                                                  95% CI
 Primary                       2.15                1.92             Smoking status       Current vs. Never        1.25 (1.13, 1.39)
 composite                                                                               Quit vs. Never           1.13 (1.05, 1.21)
                                                                    Hypertension         Yes vs. No               1.05 (0.95, 1.16)
                                                                    Dyslipidemia         No vs. Yes               1.06 (0.98, 1.16)
                                                                    Insulin Use          Yes vs. No               1.33 (1.23, 1.43)
 Secondary                     2.62                  2.11           Smoking status       Current vs. Never        1.37 (1.19, 1.58)
 composite                                                                               Quit vs. Never           1.14 (1.03, 1.26)
                                                                    Hypertension         No vs. Yes               1.04 (0.91, 1.19)
                                                                    Dyslipidemia         No vs. Yes               1.14 (1.02, 1.29)
                                                                    Insulin Use          Yes vs. No               1.43 (1.3, 1.58)
 All-cause                     2.81                  2.13           Smoking status       Current vs. Never        1.51 (1.25, 1.82)
 mortality                                                                               Quit vs. Never           1.12 (0.98, 1.27)
                                                                    Hypertension         No vs. Yes               1.14 (0.97, 1.35)
                                                                    Dyslipidemia         No vs. Yes               1.3 (1.12, 1.5)
                                                                    Insulin Use          Yes vs. No               1.73 (1.53, 1.97)
 Heart Failure                 4.69                  3.52           Smoking status       Current vs. Never        1.32 (1.09, 1.6)
                                                                                         Quit vs. Never           1.23 (1.07, 1.41)
                                                                    Hypertension         Yes vs. No               1.11 (0.93, 1.33)
                                                                    Dyslipidemia         No vs. Yes               1.27 (1.09, 1.48)
                                                                    Insulin Use          Yes vs. No               1.47 (1.29, 1.67)
 Coronary artery               2.27                  1.55           Smoking status       Current vs. Never        1.51 (1.2, 1.89)
 disease                                                                                 Quit vs. Never           1.29 (1.1, 1.51)
                                                                    Hypertension         No vs. Yes               1.04 (0.83, 1.29)
                                                                    Dyslipidemia         Yes vs. No               1.16 (0.96, 1.41)
                                                                    Insulin Use          Yes vs. No               1.14 (0.97, 1.34)
 Cerebrovascular               2.35                  1.31           Smoking status       Current vs. Never        1.33 (0.95, 1.86)
 disease                                                                                 Quit vs. Never           1.3 (1.04, 1.62)
                                                                    Hypertension         Yes vs. No               1.44 (1.04, 1.98)
                                                                    Dyslipidemia         No vs. Yes               1.08 (0.83, 1.4)
                                                                    Insulin Use          Yes vs. No               1.17 (0.94, 1.47)
 Nephropathy                   4.46                  3.29           Smoking status       Never vs. Current        1.23 (0.96, 1.58)
                                                                                         Quit vs. Never           1.03 (0.88, 1.19)
                                                                    Hypertension         Yes vs. No               1.36 (1.09, 1.69)
                                                                    Dyslipidemia         No vs. Yes               1.17 (0.97, 1.4)
                                                                    Insulin Use          Yes vs. No               1.29 (1.11, 1.5)
 Atrial Fibrillation            1.9                  1.21           Smoking status       Current vs. Never        1.07 (0.85, 1.35)
                                                                                         Quit vs. Never           1.16 (1, 1.34)
                                                                    Hypertension         Yes vs. No               1.1 (0.9, 1.35)
                                                                    Dyslipidemia         No vs. Yes               1.27 (1.07, 1.51)
                                                                    Insulin Use          Yes vs. No               1.06 (0.91, 1.22)
* HR's (95% CI's) for known cardiovascular risk factors for each outcome are shown for comparison of magnitude.




© 2019 American Medical Association. All rights reserved.

```

### DOC-003 physical PDF page 1 — PLAN

[Supplied source](../../../joi190103supp2_prod.pdf#page=1)

```text
                              Supplementary Online Content 2


Aminian A, Zajichek A, Arterburn DE, et al. Association of metabolic surgery with major
adverse cardiovascular outcomes in patients with type 2 diabetes and obesity. JAMA.
doi:10.1001/jama.2019.14231


Original Study Protocol …..…………………………………….………………………..2
Amendment to Study Protocol ……………………………….………………………….7

```

### DOC-003 physical PDF page 2 — PLAN

[Supplied source](../../../joi190103supp2_prod.pdf#page=2)

```text
                                                                                                                  2


                                       STUDY PROTOCOL
                                         (January 6, 2019)
•   Objective
    To assess the association of bariatric and metabolic surgery in patients with type 2 diabetes mellitus
    (T2DM) with various individual and composite cardiovascular outcomes in a matched-cohort analysis

•   Data source
    The data source for all analysis will be Cleveland Clinic’s Electronic Health Record (EHR) through
    12/31/2018.

•   Study protocol
    I.      Cohort derivation
            All patients at the Cleveland Clinic who have (or had) T2DM will be considered for study entry.
            This will serve as the base cohort, though all patients initially considered may not be included in
            the final statistical analysis (see II. for description of the algorithm for identifying T2DM).
            Starting with the base cohort, the final study cohort will be derived in two (2) phases:

                      (1) Identifying bariatric surgeries
                          All patients in the base cohort receiving bariatric surgery who meet the following
                          specifications at the time of surgery will be included:
                               a) Any of the following codes for bariatric procedures:
                                        • CPT: 43633, 43634, 43770, 43775, 43644, 43645, 43659, 43842,
                                             43843, 43844, 43845, 43846, 43847
                                        • ICD: 44.31, 43.82, 44.95, 43.89, 44.38, 44.39, 44.68
                                        • HCPCS: S2082, S2085
                                        (Chart review will be performed to verify the bariatric and metabolic
                                        procedures)
                               b) Has T2DM (HbA1c > 6.4% or on diabetes medication)
                               c) Age between 18-80 years
                               d) BMI ≥ 30 kg/m2
                                        • The closest BMI measurement prior will be used. If no
                                             measurements are available, the patient will be excluded.
                               e) Occurred through 12/31/2017
                               f) Surgery at one (1) of the following Cleveland Clinic locations
                                        • Ohio (Main Campus, Fairview, Hillcrest, Akron), or Florida
                                             (Weston) facilities
                          After inclusion, patients who meet any of the following at the time of surgery will be
                          excluded:
                               a) History of liver, heart or lung transplant
                               b) Emergency department admission within five (5) days prior
                               c) Active cancer/GI cancer diagnosis code within one (1) year prior
                               d) Surgical procedures/diagnoses codes for upper GI cancer and/or peptic ulcer
                                   disease during the hospitalization for bariatric surgery
                               e) History of severe heart failure
                                        • Any ejection fraction <20% prior
                           The date of the first bariatric surgery meeting inclusion/exclusion will be identified
                           for each patient and serve as the index date.

                      (2) Identifying non-surgical comparators
                          Based on the index dates derived in (1), similar patients who did not receive bariatric
                          surgery will be obtained for comparison. Starting with the base cohort, the following
                          algorithm will be implemented
                              a) Remove patients identified in (1)
                                        • Patients who met inclusion but were subsequently excluded will
                                            also be removed

```

### DOC-003 physical PDF page 3 — PLAN

[Supplied source](../../../joi190103supp2_prod.pdf#page=3)

```text
                                                                                                            3

                         b) Randomly assign each patient a single date from the collection of index
                              dates. This will serve as the assigned date for non-surgical patients.
                         c) Exclude patients meeting any of the following at the assigned date:
                                   • Last follow-up on or before the assigned date
                                   • Already dead or died within 30 days after the assigned date
                                               • Serves as a proxy for potential terminally-ill patients
                                   • Does not have T2DM (HbA1c < 6.5% and not on diabetes
                                        medication)
                                   • Age < 18 or Age > 80 years
                                   • BMI < 30
                                               • The closest measurement prior will be used. If none are
                                                 available, the closest measurement in absolute time will
                                                 be used.
                                   • History of liver, heart or lung transplant
                                   • ED admission within 5 days prior
                                   • Active cancer/GI cancer diagnosis code within one (1) year prior
                                   • History of severe heart failure
                                               • Any ejection fraction <20% prior
       The patients identified in (1) and (2) will form the final study cohort in which subsequent
       analysis will be performed. The algorithm described in (2) will be replicated 5 times for a
       sensitivity analysis to assess the variability of baseline characteristics of the non-surgical patients
       at the assigned date, as well as overall model effect estimates and prediction accuracy (See blow,
       Sensitivity Analyses). At this point, the index date and assigned date will collectively be referred
       to as the index date.

               (3) Matching Process
               Each non-surgical patient will be matched with a propensity-score (‘logit’ link) to five (5)
               surgical patients based on the index date, age at index date, BMI at index date
               (categorized as 30-35, 35-40, 40+), gender, insulin use, location (Ohio versus Florida),
               diabetes complications (composite of coronary artery disease, heart failure,
               cerebrovascular disease, peripheral vascular disease, neuropathy, nephropathy, or being
               on dialysis) with the MatchIt package in R.1

II.   Identifying patients with T2DM
      A T2DM prevalence cohort has been previously created using the modified Kho algorithm2 and
      with the following specifications:

                    Based upon ICD9/10 codes, patients with type 1 diabetes mellitus (T1DM) and
                    T2DM were identified. Codes for ketoacidosis were classified as T1DM code.

                    The algorithm was used to calculate the earliest date when a patient record contained
                    any of the following combinations:
                             • T2DM code in the EHR & T2DM medication
                             • T2DM code in the EHR & abnormal glucose*
                             • T2DM medication & abnormal glucose*
                             • T2DM code reordered twice in the EHR & outpatient insulin
                             • Insulin preceded by T2DM medication
                    *Abnormal glucose: Random glucose >200 mg/dL or fasting glucose >125 mg/dl.
                    The earliest date that any of the five (5) conditions above were met was documented
                    as the date in which the patient first met the criteria for T2DM in the Cleveland
                    Clinic system.

      This cohort contains approximately N = 287438 patients whose T2DM dates range from 1/1/1998
      through 12/31/2017.

```

### DOC-003 physical PDF page 4 — PLAN

[Supplied source](../../../joi190103supp2_prod.pdf#page=4)

```text
                                                                                                              4

III.   Outcomes
       Patients will be followed starting at the index date for 6 outcomes as follows (see eTable 1 for
       diagnosis codes/definitions):

       1.    All-cause mortality
                –     If deaths are unknown (i.e. not entered into Cleveland Clinic’s EHR), the Social
                      Security and State Death Indices will be searched.

       2.    Coronary artery disease
               –     Myocardial infarction
                        •     ICD9: 410.X, 410.XX
                        •     ICD10: i21.X and i21.XX, i22.X and i22.XX, i23.X and i23.XX
               –     Other
                        •     ICD9: 411.X, 411.X AND 414.X, 36.01, 36.02, 36.03, 36.05, 36.06,
                              36.07, 36.10, 36.11, 36.12, 36.13, 36.14, 36.15, 36.16, 36.17, 36.19, 36.31,
                              36.32, 36.33, 36.64
                        •     CPT: 92982, 92984, 92995, 92996, 92980, 92981, 33510, 33511, 33512,
                              33513, 33514, 33516, 33517, 33518, 33519, 33521, 33522, 33523, 33530,
                              33533, 33534, 33535, 33536, 93539, 93540

       3.    Cerebrovascular disease
               –     Ischemic stroke
                        •     ICD9: 433.X1, 434.X1
                        •     ICD10: i63.X and i63.XX and i63.XXX
               –     Other
                        •     ICD9: 436.0, 430.X, 431.X, 38.12, 0.61, 0.63
                        •     CPT: 37215, 37216, 0075T, 0076T, 35301, 37205, 37206


       4.    Heart failure
                         •     ICD9: 428.0, 428.1, 428.20, 428.21, 428.22, 428.23, 428.30, 428.31,
                               428.32, 428.33, 428.40, 428.41, 428.42, 428.43, 428.9

       5.    Nephropathy
                       •       Two (2) measures of eGFR < 60 separated by at least 90 days with no
                               intervening values >= 60
                         •     eGFR will be computed using the Modification of Diet in Renal Disease
                               (MDRD) Study equation with creatinine levels

       6.    Atrial fibrillation
                           •     ICD9: 427.31
                           •     ICD10: i48.0, i48.2, i48.91
                           •     CPT: 93650, 93653, 93656, 93657

       Primary endpoint
       The primary outcome will consist of the composite of 1-6, recording the first occurrence after the
       index date as the event date. The conditions/events in which a patient had in their history at
       baseline will be omitted from the composite definition in follow-up.

       Secondary endpoints
       The secondary composite outcome will consist of the composite of (1) all-cause mortality, (2)
       myocardial infarction, and (3) ischemic stroke, recording the first occurrence after the index date
       as the event date. The conditions/events in which a patient had in their history at baseline will be
       omitted from the composite definition in follow-up.

```

### DOC-003 physical PDF page 5 — PLAN

[Supplied source](../../../joi190103supp2_prod.pdf#page=5)

```text
                                                                                                          5

      Each of 1-6 will also assessed individually. For each outcome, any patient with a history of that
      outcome at the index date will be eliminated from the risk set. For nephropathy, patients with a
      baseline eGFR < 60 and patients with history of dialysis will also be excluded.

IV.   Data elements
      The following data elements will be extracted from the EHR for each patient in the base cohort
      and used for analysis. Collected variables will be mapped to the Unified Medical Language
      System (UMLS) identifiers.3 (Note: Specific diagnosis, visit, encounter, procedure, prescription,
      and lab dates will be collected with each data element, where applicable, to track changes over
      time)

          •    Demographics
                       • Date of birth
                       • Gender
                       • Race
                       • Median zip code income
                       • Weight
                       • BMI
                       • Insurance
                       • Smoking status
                       • Location
          •    Medical history
                       • Hypertension
                       • Dyslipidemia
                       • Coronary artery disease
                       • Cerebrovascular events
                       • Heart failure
                       • Nephropathy
                       • Diabetic neuropathy
                       • Peripheral arterial disease
                       • Atrial fibrillation
                       • COPD
                       • Being on dialysis
          •    Labs
                       • HbA1c
                       • Creatinine
                       • eGFR
                       • Systolic/diastolic BP
                       • LDL
                       • HDL
                       • Triglyceride levels
                       • Urine albumin: creatinine ratio (UACR)
          •    Medication
                       • Insulin
                       • Non-insulin diabetes medication
                       • ACE-I/ARB
                       • Other antihypertensive medication
                       • Statin (or other cholesterol-lowering medication)
                       • Aspirin
                       • Warfarin

```

### DOC-003 physical PDF page 6 — PLAN

[Supplied source](../../../joi190103supp2_prod.pdf#page=6)

```text
                                                                                                           6

V.     Statistical analysis
       Cause-specific event rates per 100 patient-years of follow-up starting from the index date will be
       estimated for each outcome within each study group. Cumulative incidence estimates and hazard
       ratios (HRs) from a fully-adjusted Cox-PH model will be obtained for each outcome. All baseline
       variables will be included to adjust for potential confounding. The proportional-hazards
       assumptions for the treatment variable will be tested based on weighted residuals as proposed by
       Grambsch and Therneau.4

       Within each outcome dataset, missing values will be multiply-imputed with Multiple Imputation
       by Chained equations to create 5 imputed datasets. Predictive mean matching, logistic regression,
       and polytomous logistic regression will be used for numeric, binary, and categorical variables,
       respectively. Imputation-corrected standard errors of model estimates and contrasts will be
       obtained by Rubin’s formula.5,6

       The percent (%) of weight loss and HbA1c values will also be evaluated over time and compared
       among the surgical and non-surgical groups.

       A significance level of 0.05 will be considered statistically significant, and 95% CIs will be
       reported where applicable. Adjustment for multiple comparisons of secondary endpoints is not
       performed and analyses will be considered as exploratory. All analysis will be done in the R
       statistical programming language (version 3.5.0).7

VI.    Sensitivity analyses
       Sensitivity of the HR estimates from the fully-adjusted Cox models to two components of the
       process used in obtaining non-surgical controls will be assessed: random-sampling of index dates,
       and matching ratio. The sampling of index dates for non-surgical patients will be repeated five (5)
       times, and matching ratios of 1:1, 1:5, and 1:10 will be used in each resulting dataset. All analyses
       will be performed on all 15 datasets to assess sensitivity, though results are reported from one (1)
       dataset using 1:5 matching.

       Furthermore, time-varying HRs for surgical versus non-surgical patients at 2, 5, and 8 years
       following the index date will be estimated. The details of sensitivity analyses and results have
       been mentioned below.

VII.   References
       [1] Ho DE, Imai K, King G, Stuart EA. MatchIt: Nonparametric Preprocessing for Parametric
       Causal Inference. Journal of Statistical Software. 2011;42(8): 1 - 28.

       [2] Kho AN, Hayes MG, Rasmussen-Torvik L, et al. Use of diverse electronic medical record
       systems to identify genetic risk for type 2 diabetes within a genome-wide association study. J Am
       Med Inform Assoc. 2012;19(2):212-8.

       [3] Milinovich A, Kattan MW. Extracting and utilizing electronic health data from Epic for
       research. Ann Transl Med. 2018;6(3):42.

       [4] Grambsch PM, Therneau TM. Proportional hazards tests and diagnostics based on weighted
       residuals. Biometrika. 1994;81(3): 515-526.

       [5] van Buuren S, Groothuis-Oudshoorn K. mice: Multivariate Imputation by Chained Equations
       in R. Journal of Statistical Software 2011; 45(3): 1 - 67.

       [6] Frank E Harrell Jr (2018). rms: Regression Modeling Strategies. R package version 5.1-2.
       https://CRAN.R-project.org/package=rms

       [7] R Core Team (2018). R: A language and environment for statistical computing. R Foundation
       for Statistical Computing, Vienna, Austria. URL https://www.R-project.org/.

```

### DOC-003 physical PDF page 7 — PLAN

[Supplied source](../../../joi190103supp2_prod.pdf#page=7)

```text
                                                                                                                     7


                               AMENDMENT TO STUDY PROTOCOL
                                      (August 2, 2019)
    In order to address the comments raised during the journal pee-review process, the following parts will be added
    to the study protocol.

•   Adverse Events of Metabolic Surgery
    Early (<90 days after surgery) and late adverse events (need for nutritional, endoscopic, radiologic, and surgical
    interventions until last follow-up to serve as proxy to adverse events) after metabolic surgery will be collected
    and reported (see eTable 2 for diagnosis and intervention codes/definitions). Nutritional variables of interests
    are hemoglobin, serum protein, albumin, and vitamin D levels.

•   E-value for Sensitivity Analysis
    Additional sensitivity analysis to assess the potential effects of unmeasured confounders will be added to the
    study by the E-value methodology. The E-value is the minimum strength of association, on the risk ratio scale,
    that an unmeasured confounder would need to have with both the treatment and outcome, conditional on the
    measured covariates, to fully explain away a specific treatment–outcome association.1-3
    For all 8 composite and individual study endpoints, the E-value will be calculated and interpreted for the HR
    estimates and for their limit of 95% CI closest to the null.

•   References
    [1] VanderWeele TJ, Ding P. Sensitivity Analysis in Observational Research: Introducing the E-Value. Ann
    Intern Med. 2017;167(4):268-274.

    [2] Haneuse S, VanderWeele TJ, Arterburn D. Using the E-Value to Assess the Potential Effect of Unmeasured
    Confounding in Observational Studies. JAMA. 2019;321(6):602-603.

    [3] https://www.hsph.harvard.edu/tyler-vanderweele/tools-and-tutorials/

```

## Completion and direct confirmation

All 27 assigned physical pages were inspected and mapped: DOC-002 20/20, DOC-003 7/7. The support inventory contains N101–N118 (18 numeric groups) and S101–S126 (26 statistical groups), with all underlying members retained. There are no scientific coverage gaps. Continuous plots without printed numerical point labels provide graphical relationships rather than exact digitized numbers; original legacy image-renderer version is not recorded. No supplied workbook, CSV, DOC or DOCX exists in this assigned scope.

Direct confirmation command: `pdftotext -f 7 -l 7 -layout joi190103supp2_prod.pdf -` (available direct Poppler tooling). The exact printed amendment date is **August 2, 2019**, on physical PDF page 7. Original protocol is dated January 6, 2019 on physical page 2. No source or reused derivative was modified. The only newly written artifact is this evidence map.
