# Complete support quantitative evidence map — Workflow 1.6

Scope: DOC-002, joi190103supp1_prod.pdf physical pages 1–20 (REPORT); DOC-003, joi190103supp2_prod.pdf physical pages 1–7 (PLAN). Runtime UUID: 01a12882-33e4-7cd2-9bdd-f27b095e87fc. All 27 assigned pages mapped. Reusable-backed 27; fresh-required 0; scientific gaps 0. No source/reused asset edited. No legacy scientific conclusions, candidates, or selective evidence maps read. This is extraction and relationship mapping; no candidate diagnosis or adjudication.

Method: source-linked raw native/layout text inspected completely. Existing native/layout extraction engines are legacy pdftotext/PDF extraction, version not recorded; curator validated against direct Poppler 26.01.0. Figure pages 8, 11, 16, 18 were visually inspected using their existing PNGs (legacy render engine/version not recorded). Every displayed scalar value in the assigned PDFs is preserved in the complete page transcripts below. Graph-only results are separately mapped visually; no exact scalar value is invented from a curve. One targeted fresh direct render was made for DOC-002 p2 to retain primary-diagnosis bold formatting; no OCR, Python extraction, or fallback needed. Protocol and amendment opened throughout, including administrative/contents sections. There are no provided Office/workbook/CSV sources; workbook formulas, cached/displayed workbook values, and Office stable locations are NOT_APPLICABLE.

## Physical-page coverage

| Source | Physical page | Content and relationship scope | Status |
|---|---:|---|---|
| DOC-002 REPORT | 1 | Complete contents, eTable/eFigure titles, page references, time points and units | MAPPED; no standalone study result |
| DOC-002 REPORT | 2 | eTable 1 all diagnosis/procedure codes, nephropathy numeric definition, primary-diagnosis footnote | MAPPED |
| DOC-002 REPORT | 3 | eTable 2 all diagnosis/intervention codes and combinations | MAPPED |
| DOC-002 REPORT | 4 | eTable 2 continuation, all procedure codes, source footnote | MAPPED |
| DOC-002 REPORT | 5 | eTable 3 all 12 medication count/percentage rows and both sample sizes | MAPPED |
| DOC-002 REPORT | 6 | eTable 4 all 8 event-rate rows, 5 death-composite pairs, differences/CIs/bootstrap definition | MAPPED |
| DOC-002 REPORT | 7 | eTable 5 all 48 cumulative-incidence estimate/CI cells, 8 endpoints × 3 times × 2 groups | MAPPED |
| DOC-002 REPORT | 8 | eFigure 1 all 16 subgroup estimate/CI rows, 8 interaction P values, covariate replacement definition | MAPPED; visual |
| DOC-002 REPORT | 9 | eTable 6 all 8 HR/CI/P/PH-P rows | MAPPED |
| DOC-002 REPORT | 10 | eTable 7 all 24 time-varying HR/CI cells, spline definition | MAPPED |
| DOC-002 REPORT | 11 | eFigure 2 all 8 curves/bands, BMI/treatment/time/unit legends | MAPPED; visual |
| DOC-002 REPORT | 12 | eTable 8 all 52 estimate/98.8%-CI/P cells and test footnotes | MAPPED |
| DOC-002 REPORT | 13 | eTable 9 all 30 variable/time rows × 4 count columns | MAPPED |
| DOC-002 REPORT | 14 | eTable 10 all 5 time rows × 2 treatment sample sizes | MAPPED |
| DOC-002 REPORT | 15 | eTable 11 all 24 intervention cumulative-incidence/CI cells, Kaplan–Meier and exclusions | MAPPED |
| DOC-002 REPORT | 16 | eFigure 3 all 8 curves/bands, nutritional units/time legends and narrative | MAPPED; visual |
| DOC-002 REPORT | 17 | All sensitivity design counts, ratios, 15 datasets and significance counts for 8 endpoints | MAPPED |
| DOC-002 REPORT | 18 | eFigure 4 all 120 HR/95%-CI plotted estimates: 8 endpoints × 5 iterations × 3 ratios | MAPPED; visual |
| DOC-002 REPORT | 19 | Full repeated eTable 7, time-varying definition/reference, E-value definition and numerical interpretation | MAPPED |
| DOC-002 REPORT | 20 | eTable 12 all 16 E-values and 40 cardiovascular-risk-factor HR/CI rows and contrasts | MAPPED |
| DOC-003 PLAN | 1 | Administrative contents: original protocol and amendment physical locations | MAPPED; NO_APPLICABLE standalone numeric study result |
| DOC-003 PLAN | 2 | Original protocol date, data boundary, surgical cohort criteria and index-date definition; all codes | MAPPED |
| DOC-003 PLAN | 3 | Comparator criteria, assignment repeats, matching direction/ratio/covariates, T2DM algorithm/background cohort | MAPPED |
| DOC-003 PLAN | 4 | All 6 endpoints, codes, renal definition, both composite definitions | MAPPED |
| DOC-003 PLAN | 5 | Risk-set exclusions, all covariate/data definitions and UMLS mapping | MAPPED |
| DOC-003 PLAN | 6 | Full analysis, rates, Cox, PH tests, imputation/SE rules, alpha/CI/software, sensitivity rules, references | MAPPED |
| DOC-003 PLAN | 7 | Amendment date, early-event boundary, late-event proxies, nutritional outcomes, E-value scale/8 endpoints | MAPPED |

## Relationship groups and matching keys

The following local group keys organize evidence for the coordinator/checkers to assign complete global N/S IDs. They are not candidate IDs. Every row/cell in the page transcripts is included in its corresponding group; tests are not restricted to group summaries. Numeric groups SUP-N01–SUP-N18 (18); statistical groups SUP-S01–SUP-S13 (13). Main-paper keys name content for matching without reopening an unassigned main source.

| Local numeric key | Source, exact unit | Complete scope and comparison identity | Matching main-paper key |
|---|---|---|---|
| SUP-N01 | DOC-002 p1 | Every contents title, page number, percentage/rate unit, all time-point lists | Main references to eTables/eFigures |
| SUP-N02 | DOC-002 p2 eTable1 | All ICD/CPT/HCPCS identifiers, logical code combinations, nephropathy ≥2 eGFR<60 mL/min measurements ≥90 days apart with no intervening ≥60, MDRD; bold requires primary diagnosis | Main eligibility, outcome definitions; PLAN pp2–4 |
| SUP-N03 | DOC-002 pp3–4 eTable2 | Every adverse-event diagnosis/procedure code, dialysis conjunction, intervention category, excluded/included procedure definitions | Main adverse events and interventions; PLAN p7 |
| SUP-N04 | DOC-002 p5 eTable3 | 12 medication classes, count and displayed percentage in surgical N2287 and matched nonsurgical N11435; classes may overlap | Main baseline medication classes and cohort sizes |
| SUP-N05 | DOC-002 p6 eTable4 | 8 cause-specific rate pairs per100 patient-years, 5 individual-outcome/death-composite pairs, nonsurgical−surgical rate differences and CI; title includes '(%)'; bootstrap1000 | Main Table2 event rates, event-rate contrasts |
| SUP-N06 | DOC-002 p7 eTable5 | All 8 endpoints ×2 groups ×years2,5,8 cumulative incidence (%) and 95%CI | Main Table2 8-year cumulative incidence; primary/death narrative |
| SUP-N07 | DOC-002 p8 eFigure1 | All subgroup cutpoints, 16 HR/CI rows and 8 interaction P values | Main subgroup narrative, primary endpoint |
| SUP-N08 | DOC-002 pp9–10 and19 | All 8 overall HR/CI/P/PH-P tuples, all24 time-varying HR/CI tuples, p19 repeated24, textual table-number reference | Main Table2 adjusted HR/CI/P; sensitivity narrative |
| SUP-N09 | DOC-002 p11 eFigure2 | HbA1c and non-insulin medication curves by2 treatments ×2 BMI categories, four-year horizon | Main BMI subgroup and metabolic medication trajectory |
| SUP-N10 | DOC-002 p12 eTable8 | 13 variables ×years1,2,5,8 estimate/98.8%CI/P; lbs/kg paired weights, percentages and nutritional units, test definitions | Main weight/HbA1c/medication difference estimates, nutritional narrative |
| SUP-N11 | DOC-002 p13 eTable9 | All120 count cells:6 measures ×years0,1,2,5,8 ×total observations/distinct patients ×2 groups; measurements AFTER each time point | Main longitudinal observation population and figure trajectories |
| SUP-N12 | DOC-002 p14 eTable10 | All10 medication proportion sample-size cells at years0,1,2,5,8; baseline2287/11433 | Main baseline N and medication proportion analysis |
| SUP-N13 | DOC-002 p15 eTable11 | 6 interventions ×years1,2,5,8,24 cumulative incidence/95%CI cells; Kaplan–Meier; abdominal surgery excludes abdominal-wall hernia/cholecystectomy | Main8-year intervention incidence and adverse events |
| SUP-N14 | DOC-002 p16 eFigure3 | 4 nutritional panels ×2 treatments, years0–8; units and narrative; eTable8 matching | Main adverse-event/nutritional narrative; PLANp7 |
| SUP-N15 | DOC-002 pp17–18 | 5 assignments ×3 ratios=15 datasets;8 outcomes; significance counts15/15 for5 endpoints,13 cerebrovascular,12 coronary,11 AF; all120 plotted HR/CI pairs; legend ratio labels | Main matching and sensitivity analysis description; PLANp6 |
| SUP-N16 | DOC-002 pp19–20 |8 paired E-values,40 known-factor HR/CI rows, all contrast directions; p19 primary HR0.61(0.55,0.69),E2.15/1.92, wording '5-component MACE',4 known factors | Main primary composite label/E-value narrative and Table2 HR; PLANp7 |
| SUP-N17 | DOC-003 pp2–5 | Original date2019-01-06; EHR through2018-12-31; surgery through2017-12-31; all age/BMI/HbA1c/glucose/EF/time exclusions, index assignment/matching, approximate cohort287438,date1998-01-01–2017-12-31,6+2 endpoints/risk sets/all covariates/codes | Main Methods eligibility/cohort derivation/definitions/baseline variables |
| SUP-N18 | DOC-003 pp6–7 | All planned rates/models/alpha/CI/imputation datasets/software/15 sensitivity datasets/years2,5,8; amendment2019-08-02;early<90days;8 E-value endpoints | Main statistical methods, sensitivity, adverse events and supplement result definitions |

| Local statistical key | Exact source | Inferential scope including every row/cell | Definition and matching |
|---|---|---|---|
| SUP-S01 | DOC-002 p6 eTable4 |8 difference/95%CI tuples | 1000-bootstrap-sample CI for nonsurgical−surgical8-year event rates per100patient-years; no P given |
| SUP-S02 | DOC-002 p7 eTable5 |48 estimate/95%CI tuples | Cumulative incidence(%),8 endpoints,2 treatments,2/5/8years |
| SUP-S03 | DOC-002 p8 eFigure1 |16 HR/95%CI tuples and8 interaction P values | Fully-adjusted Cox replacing original covariate with binary subgroup plus treatment interaction; age/eGFR split by medians |
| SUP-S04 | DOC-002 p9 eTable6 |8 HR/95%CI/association-P/PH-P tuples | Surgical vs nonsurgical relative instantaneous risk; PH P distinguished from association P |
| SUP-S05 | DOC-002 pp10,19 eTable7 |24 unique time-varying HR/95%CI tuples in two complete occurrences | Treatment×restricted-cubic-spline(observed follow-up time); years2,5,8 |
| SUP-S06 | DOC-002 p11 eFigure2 |8 curves with visible shaded bands | HbA1c mean and noninsulin-medication percentage,4years,2BMI×2treatments; band confidence level not specified on page |
| SUP-S07 | DOC-002 p12 eTable8 |52 estimate/98.8%CI/P tuples | Four-knot spline×treatment for metabolic/nutritional mean changes; two-sample proportions test per time for medications; Bonferroni-corrected98.8%CIs, stars preserved |
| SUP-S08 | DOC-002 p15 eTable11 |24 cumulative-incidence/95%CI tuples | Kaplan–Meier, interventions after metabolic surgery, years1/2/5/8 |
| SUP-S09 | DOC-002 p16 eFigure3 |8 trend curves/shaded bands | Nutritional mean,2groups,8years; band confidence level not specified on page |
| SUP-S10 | DOC-002 pp17–18 eFigure4 |120 graphical HR/95%CI pairs plus complete15-dataset significance narrative | Fully-adjusted Cox,8 endpoints,5 iterations,3matching ratios |
| SUP-S11 | DOC-002 pp19–20 eTable12 |16 E-values plus40 HR/95%CI tuples and interpretive text | E-value on RR scale for HR and upper95%limit; no conversion formula printed; exact risk-factor reference levels retained |
| SUP-S12 | DOC-003 p6 |All planned inferential definitions | Cause-specific rates per100patient-years;fully-adjusted CoxPH;weighted-residual PH test;5MICE datasets;PMM/logistic/polytomous imputation;RubinSE;alpha0.05;95%CI;secondary outcomes unadjusted/exploratory;R3.5.0;all15sensitivity datasets |
| SUP-S13 | DOC-003 p7 |Planned E-value definition | RR scale,minimum association with both treatment/outcome conditional on measured covariates;all8endpoints,point HR and closest-to-null95%CI limit;amendment date retained |

## Embedded-figure transcription and full graphical mapping

### eFigure 1 — [DOC-002 p8](../../../joi190103supp1_prod.pdf#page=8), REPORT

Fully-adjusted HR (95%CI) for surgery versus usual care, primary composite endpoint. Null1.0; left decreased risk, right increased risk; displayed axis ticks0.4,1.0,1.2. The original covariate is replaced with a dichotomous subgroup variable and its treatment interaction. Age/eGFR are categorized by medians. Interaction P applies to the pair, not an individual treatment HR.

| Variable | First level HR(95%CI) | Second level HR(95%CI) | Interaction P |
|---|---|---|---:|
| Gender | Male0.58(0.49,0.69) | Female0.64(0.56,0.74) |0.35|
| Age years | <54:0.57(0.47,0.68) | ≥54:0.57(0.50,0.66) |0.93|
| BMI kg/m² | <40:0.62(0.49,0.78) | ≥40:0.61(0.54,0.69) |0.90|
| HbA1c % | <7%:0.62(0.52,0.74) | ≥7%:0.60(0.52,0.70) |0.80|
| eGFR ml/min | <91:0.61(0.54,0.70) | ≥91:0.62(0.51,0.75) |0.94|
| Insulin | No0.63(0.55,0.73) | Yes0.59(0.50,0.70) |0.53|
| Sulfonylureas | No0.63(0.55,0.72) | Yes0.60(0.49,0.74) |0.72|
| Lipid-lowering medications | No0.61(0.52,0.73) | Yes0.62(0.53,0.71) |0.98|

### eFigure 2 — [DOC-002 p11](../../../joi190103supp1_prod.pdf#page=11), REPORT

Two panels; all four curves and their shaded bands inspected in each. Treatment legend Surgery(red) and No surgery(turquoise). BMI <35(solid) versus ≥35(dashed) kg/m² at index date. X ticks0,1,2,3,4years. HbA1c(%) y ticks6.0,6.5,7.0,7.5. Non-insulin diabetes medication percent y ticks40,60,80,100. No point estimates or band endpoints are printed; exact series cannot be recovered as displayed scalar data.

All curve identities: HbA1c/Surgery/<35, HbA1c/Surgery/≥35, HbA1c/No surgery/<35, HbA1c/No surgery/≥35; Noninsulin%/Surgery/<35, Noninsulin%/Surgery/≥35, Noninsulin%/No surgery/<35, Noninsulin%/No surgery/≥35. Surgery HbA1c drops early then rises; ≥35 surgery remains below<35 surgery after the early fall; nonsurgical curves remain near7.5–7.6. Surgical medication curves drop early; solid stays above dashed; nonsurgical curves stay near80%. These are visual descriptions, not new numerical estimates. Confidence level of shading is unspecified on this page. This subgroup display has a four-year horizon distinct from eTable8's eight-year overall analysis.

### eFigure 3 — [DOC-002 p16](../../../joi190103supp1_prod.pdf#page=16), REPORT

Four panels, each Surgery(red solid) and No surgery(turquoise dashed) plus shaded bands; all8curves inspected through8years. X ticks0,2,4,6,8. Albumin(g/dL), y ticks3.4,3.6,3.8; VitaminD25(ug/L), y ticks30,35; Hemoglobin(g/dL), y ticks10.5,11.0,11.5,12.0; Protein(g/dL),y ticks6.4,6.6,6.8,7.0. Exact curve/band coordinates are graph-only; no scalar tables printed. Albumin surgical curve starts near3.8, remains above nonsurgical for much follow-up then falls at8years. VitaminD surgery rises early then varies and converges with nonsurgical near8years. Hemoglobin curves vary and cross, with surgery lower at8years. Protein surgery remains lower. Source text calls nutritional differences modest and proposes routine vitamin/supplement use as explanation for early vitaminD rise; eTable8 provides numeric estimates. Band confidence level is not specified on this page.

### eFigure 4 — [DOC-002 p18](../../../joi190103supp1_prod.pdf#page=18), REPORT

All8panels inspected: Primary, Secondary, All-cause mortality, Coronary artery disease, Cerebrovascular disease, Heart failure, Nephropathy, Afib. All5sampling iterations(1,2,3,4,5) and all3ratios in every panel:120point/95%CI pairs. Legend shows1:1(red circle),5:1(green triangle),10:1(blue square); p17 prose expresses ratios1:1,1:5,1:10. Y axis Hazard ratio(95%CI), ticks0.0,0.2,0.4,0.6,0.8,1.0,1.2; x Index date sampling iteration. Every point lies below1.0; graphical intervals crossing1.0 occur in coronary, cerebrovascular and Afib panels. Graph does not print point/interval-endpoint scalars, so no exact decimal reconstruction is asserted. Every pair remains available for direct source graphical recheck by endpoint/iteration/ratio; no outcome, iteration or ratio sampled or omitted.

Complete graphical units, each cell includes iterations1,2,3,4,5 and their five intervals:

| Endpoint |1:1 graphical pair units|5:1 graphical pair units|10:1 graphical pair units|Textual significant datasets (p17)|
|---|---|---|---|---:|
|Primary|1,2,3,4,5|1,2,3,4,5|1,2,3,4,5|15|
|Secondary|1,2,3,4,5|1,2,3,4,5|1,2,3,4,5|15|
|All-cause mortality|1,2,3,4,5|1,2,3,4,5|1,2,3,4,5|15|
|Coronary artery disease|1,2,3,4,5|1,2,3,4,5|1,2,3,4,5|12|
|Cerebrovascular disease|1,2,3,4,5|1,2,3,4,5|1,2,3,4,5|13|
|Heart failure|1,2,3,4,5|1,2,3,4,5|1,2,3,4,5|15|
|Nephropathy|1,2,3,4,5|1,2,3,4,5|1,2,3,4,5|15|
|Atrial fibrillation|1,2,3,4,5|1,2,3,4,5|1,2,3,4,5|11|

## Protocol quantitative and statistical definitions

PLAN role applies to all7pages, including background numbers, codes and the amendment. Original2019-01-06 and amendment2019-08-02 are distinct versions within the same PLAN bundle. Complete wording follows in page transcripts; this index retains relationships needed to match REPORT methods/results.

- p2: EHR through2018-12-31; surgical procedures through2017-12-31; HbA1c>6.4% or diabetes medication; age18–80years; BMI≥30kg/m², closest prior BMI required; first eligible surgery index date; ED admission within5days, active cancer/GI cancer within1year and any prior EF<20% exclusions; prior liver/heart/lung transplant exclusions; five named Ohio/Florida surgical facility entries across two states.
- p3: each comparator gets one random surgical index date; exclude last follow-up≤date, death before or within30days after assigned date, HbA1c<6.5% and no medication, age<18 or>80, BMI<30, transplantation, ED admission within5days, cancer within1year, EF<20%. Comparator BMI closest prior, otherwise closest absolute time. Repeat assignment5times. Matching text: 'Each non-surgical patient ... to five (5) surgical patients'; propensity score logit, MatchIt; index date, age, BMI categories30–35/35–40/40+, gender, insulin, Ohio vs Florida, and complication composite (CAD/HF/cerebrovascular/peripheral vascular/neuropathy/nephropathy/dialysis). Five alternative T2DM algorithm conditions, including T2DM code twice plus outpatient insulin. Random glucose>200mg/dL or fasting>125mg/dl. Background approximately N287438, earliest T2DM dates1998-01-01 through2017-12-31.
- p4: six components mortality,CAD,cerebrovascular,HF,nephropathy,AF. Primary composite1–6 first occurrence after index, conditions in baseline history omitted from follow-up composite. Secondary composite mortality+MI+ischemic stroke, similarly first event and baseline-condition omissions. Nephropathy two eGFR<60 measures separated≥90days, no intervening≥60, MDRD with creatinine. All endpoint codes preserved below.
- p5: for each individual endpoint remove baseline history from risk set; renal also exclude baseline eGFR<60 or dialysis history. All extracted demographics, histories, labs and medications listed below; all dated events track changes over time. These data identify planned adjustment variables, not achieved dataset counts.
- p6: cause-specific event rates per100patient-years, from index date; cumulative incidence and fully-adjusted CoxPH HR; all baseline variables adjust confounding; treatment PH assumption tested with Grambsch–Therneau weighted residuals. Five MICE datasets; numeric predictive mean matching, binary logistic, categorical polytomous logistic; Rubin formula for imputation-corrected SE of estimates/contrasts. Compare weight-loss percent and HbA1c over time. Significance0.05;95%CI where applicable; secondary endpoints without multiplicity adjustment and exploratory. R3.5.0. Assignment five times ×matching1:1/1:5/1:10 gives15datasets; all analyses on all15, reported one1:5dataset. Time-varying HR at2/5/8years. Named statistical equations/methods are references, not printed algebraic formulas.
- p7: amendment explicitly added during peer review. Early adverse events<90days; late events through last follow-up using nutritional/endoscopic/radiologic/surgical interventions as proxies. Nutritional hemoglobin/protein/albumin/vitaminD. E-value RR-scale minimum confounder association with treatment AND outcome conditional on measured covariates, HR point and95%limit closest to null for all8composite/individual endpoints. No E-value conversion formula or direct computation inputs beyond reported estimates are printed.

## Complete scalar/text evidence by physical page

The following complete raw page transcripts preserve all result-relevant numerical cells, inference labels, codes, units, footnotes, tables, repeated tables, sensitivity and protocol statements. Form-feed page boundaries are converted to explicit physical-page headings; all source text is preserved. Native extraction does not contain embedded figure values; the visual transcriptions above close that coverage. Row alignment in these native texts follows the source layout; ordered columns are retained in page headers. No diagnosis is embedded in this transcript.

### DOC-002 REPORT physical page 1 — [Source](../../../joi190103supp1_prod.pdf#page=1)

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

### DOC-002 REPORT physical page 2 — [Source](../../../joi190103supp1_prod.pdf#page=2)

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

### DOC-002 REPORT physical page 3 — [Source](../../../joi190103supp1_prod.pdf#page=3)

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

### DOC-002 REPORT physical page 4 — [Source](../../../joi190103supp1_prod.pdf#page=4)

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

### DOC-002 REPORT physical page 5 — [Source](../../../joi190103supp1_prod.pdf#page=5)

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

### DOC-002 REPORT physical page 6 — [Source](../../../joi190103supp1_prod.pdf#page=6)

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

### DOC-002 REPORT physical page 7 — [Source](../../../joi190103supp1_prod.pdf#page=7)

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

### DOC-002 REPORT physical page 8 — [Source](../../../joi190103supp1_prod.pdf#page=8)

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

### DOC-002 REPORT physical page 9 — [Source](../../../joi190103supp1_prod.pdf#page=9)

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

### DOC-002 REPORT physical page 10 — [Source](../../../joi190103supp1_prod.pdf#page=10)

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

### DOC-002 REPORT physical page 11 — [Source](../../../joi190103supp1_prod.pdf#page=11)

```text
                                                                                       11

 eFigure 2. Mean Trend Curve of HbA1c (%) and Proportions of Patients Taking Non-insulin
Diabetes Drugs Over Four Years of Follow-up Categorized by the Treatment Group (Metabolic
         Surgery Vs. Usual Care) and the BMI (≥35 vs. <35 kg/m2) at the Index Date




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 REPORT physical page 12 — [Source](../../../joi190103supp1_prod.pdf#page=12)

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

### DOC-002 REPORT physical page 13 — [Source](../../../joi190103supp1_prod.pdf#page=13)

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

### DOC-002 REPORT physical page 14 — [Source](../../../joi190103supp1_prod.pdf#page=14)

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

### DOC-002 REPORT physical page 15 — [Source](../../../joi190103supp1_prod.pdf#page=15)

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

### DOC-002 REPORT physical page 16 — [Source](../../../joi190103supp1_prod.pdf#page=16)

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

### DOC-002 REPORT physical page 17 — [Source](../../../joi190103supp1_prod.pdf#page=17)

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

### DOC-002 REPORT physical page 18 — [Source](../../../joi190103supp1_prod.pdf#page=18)

```text
                                                                             18


  eFigure 4. Hazard Ratios and 95% Confidence Intervals for Metabolic Surgery
 Versus No Surgery From Fully-Adjusted Cox Models for Each Outcome for Five
 (5) Iterations of Index Date Random Sampling and Three (3) Different Matching
                            Ratios (Total of 15 Datasets)




© 2019 American Medical Association. All rights reserved.

```

### DOC-002 REPORT physical page 19 — [Source](../../../joi190103supp1_prod.pdf#page=19)

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

### DOC-002 REPORT physical page 20 — [Source](../../../joi190103supp1_prod.pdf#page=20)

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

### DOC-003 PLAN physical page 1 — [Source](../../../joi190103supp2_prod.pdf#page=1)

```text
                              Supplementary Online Content 2


Aminian A, Zajichek A, Arterburn DE, et al. Association of metabolic surgery with major
adverse cardiovascular outcomes in patients with type 2 diabetes and obesity. JAMA.
doi:10.1001/jama.2019.14231


Original Study Protocol …..…………………………………….………………………..2
Amendment to Study Protocol ……………………………….………………………….7

```

### DOC-003 PLAN physical page 2 — [Source](../../../joi190103supp2_prod.pdf#page=2)

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

### DOC-003 PLAN physical page 3 — [Source](../../../joi190103supp2_prod.pdf#page=3)

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

### DOC-003 PLAN physical page 4 — [Source](../../../joi190103supp2_prod.pdf#page=4)

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

### DOC-003 PLAN physical page 5 — [Source](../../../joi190103supp2_prod.pdf#page=5)

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

### DOC-003 PLAN physical page 6 — [Source](../../../joi190103supp2_prod.pdf#page=6)

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

### DOC-003 PLAN physical page 7 — [Source](../../../joi190103supp2_prod.pdf#page=7)

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

## Formatting recovery and derivative provenance

Direct visual render of [DOC-002 p2](../../../joi190103supp1_prod.pdf#page=2) retains eTable1 bold code formatting omitted by raw text. In the coronary artery disease diagnosis list, the standalone 411.X is bold; within '411.X AND 414.X', 414.X is bold and the preceding 411.X is regular. In the GI Cancer diagnosis list, 531.X, 532.X, 533.X are bold. Footnote: bold text indicates it must be a primary diagnosis. Remaining displayed code entries are regular. This formatting is evidence for outcome/eligibility code definitions, not an adjudication.

Fresh derivative: .ai_paper_validation/review_1_6/preprocessing/support-supp1-p02-primary-diagnosis.png. Engine: direct pdftoppm, Poppler26.01.0, local CPU. Exact command: `pdftoppm -f 2 -l 2 -singlefile -scale-to 1700 -png joi190103supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/support-supp1-p02-primary-diagnosis`. The render supplements a reusable-backed page and does not change the fresh-required unit partition.

## Complete tuple counts and handoff limitations

- Printed unique result estimate/interval tuples:220 = eTable4(8) +eTable5(48) +eFigure1(16) +eTable6(8) +eTable7(24) +eTable8(52) +eTable11(24) +eTable12known-factorHRs(40). Complete eTable7 duplication p19 adds24printed occurrences without24new unique results. Eight subgroup interaction P values are additional tests; eight PH P values are separate from association P values. All P values, interval confidence levels, star markers, and model labels are retained.
- Additional printed E-value scalars:16;120graph-only HR/95%CI pairs in eFigure4;16trend curves/bands across eFigures2–3. No exact data points or band endpoints are printed in these graphical series. Every graphical unit was inspected; source graphics are authority for further comparisons. E-value numerical conversion formula is not supplied. Trend shading confidence level is not specified on those pages. These are supplied-evidence precision/definition limits, not scientific coverage gaps.
- Numeric relationship groups18; inferential groups13. Potential shard split below120tuples: scalar shard1 eTable4+5/eFigure1/eTable6/eTable7=104; scalar shard2 eTable8+11/eTable12known-factorHR=116; separate graphical shard eFigure4=120; trend/E-value/PLAN rules by13group keys as needed. Do not merge distinct outcome/time/group/model results merely to reduce counts.
- All12eTables,4eFigures and3sensitivity sections mapped, including full longitudinal years and exact protocol/amendment content. No supplied spreadsheet/CSV/Office source; no workbook formula/cache distinction applies. Scientific-coverage gaps:None. Raw-text formatting gap on eTable1 closed by direct visual render. Fresh-required unit gaps:None. No candidate count or finding threshold was used.
