# Workflow 1.6.1 Support Mapping: SAP, Results, and Data Sharing

Status: COMPLETE. Exact assigned scope: DOC-003 PDF pp. 1-30 (PLAN), DOC-004 PDF pp. 1-29 (REPORT), DOC-005 PDF p. 1 (administrative REPORT): 60 unique pages, all mapped. This extraction records source evidence and matching keys only; scientific checking and inclusion decisions belong to later independent stages. No old candidate, checker, screening, classification, or report content was read. All supplied sources and reusable assets were preserved.

## Provenance, engines, and completeness

Whole-document reusable layouts are source-matched per the current curator: `.ai_paper_validation/review_1_5_1/preprocessing/DOC-003_supp2_layout_fresh.txt` (30 pages); `.ai_paper_validation/document_outputs/DOC-004/supp3_layout.txt` (29 pages); `.ai_paper_validation/review_1_5_1/preprocessing/DOC-005_supp4_layout_fresh.txt` (1 page). Native extraction engine: pdftotext 26.01.0, layout mode. The full page-separated transcription below preserves every displayed table row, estimate, confidence interval, P value, unit, label, and footnote, including source wording and display precision. The preceding semantic index identifies comparisons and model/population keys. Neither index nor transcription replaces the direct source as final authority.

Reused RapidOCR ONNX Runtime CPU text and retained renders for DOC-004 pp. 4, 6, 8, 13, 20 were opened; continuation values and footnotes were visually inspected against the retained page images. Retained eFigure renders pp. 25-27, table renders pp. 7, 10, 21, and DOC-005 p. 1 were visually inspected. Retained render executable/version is unrecorded. Native/OCR agreement is satisfactory for those continuation rows; OCR line order is less reliable than native layout and visual columns. Copyright-only, footnote-only, affiliation and administrative units were explicitly opened rather than inferred from extraction size.

SAP figures embedded on pp. 7 and 15 were not represented numerically in reusable native text. Fresh targeted direct-source rendering closed that visual derivative gap using local CPU Poppler pdftoppm 26.01.0:

- `pdftoppm -f 7 -l 7 -singlefile -scale-to 1800 -png joi190106supp2_prod_1635377898.49605.pdf .ai_paper_validation/review_1_6_1/preprocessing/sap-results-sap-p7`
- `pdftoppm -f 15 -l 15 -singlefile -scale-to 1800 -png joi190106supp2_prod_1635377898.49605.pdf .ai_paper_validation/review_1_6_1/preprocessing/sap-results-sap-p15`

New derivatives: `preprocessing/sap-results-sap-p7.png` and `preprocessing/sap-results-sap-p15.png`, both directly visually inspected. No fresh OCR was necessary. No Office, workbook, or CSV is supplied in this scope; workbook formulas and cached/displayed values are therefore not applicable. Administrative URLs and addresses were read as supplied text, without network access or contact.

## Exact per-page coverage

Every row is COMPLETE. Source link targets are relative to this extraction directory.

| Source | PDF page | Role | Inspected content and mapped key | Status |
|---|---:|---|---|---|
| DOC-003 | 1 | PLAN | SAP cover, article identity; no applicable result values | COMPLETE |
| DOC-003 | 2 | PLAN | Administrative version 2, July 2019; protocol date; SAP-ADMIN | COMPLETE |
| DOC-003 | 3 | PLAN | Contributors and signatures; no applicable quantitative relationship | COMPLETE |
| DOC-003 | 4 | PLAN | Background and comparative intervention objectives; SAP-OBJECTIVES | COMPLETE |
| DOC-003 | 5 | PLAN | Two primary endpoints, secondary/intermediate endpoints; SAP-ENDPOINTS | COMPLETE |
| DOC-003 | 6 | PLAN | Trial design, 6874 participants, household randomization, alpha; SAP-DESIGN | COMPLETE |
| DOC-003 | 7 | PLAN | Sample-size inputs, superiority, visually inspected Figure 1; SAP-POWER | COMPLETE |
| DOC-003 | 8 | PLAN | Interim stopping boundaries and final analysis schedule; SAP-DECISIONS | COMPLETE |
| DOC-003 | 9 | PLAN | Table 1 clinical and anthropometric endpoint timeline, every row | COMPLETE |
| DOC-003 | 10 | PLAN | Table 1 continued, every intermediate-marker row | COMPLETE |
| DOC-003 | 11 | PLAN | Table 1 continued, substudies, clinically meaningful thresholds | COMPLETE |
| DOC-003 | 12 | PLAN | Outcome assessments, 95% CI, multiplicity m=27, control adherence | COMPLETE |
| DOC-003 | 13 | PLAN | Intervention adherence, ITT/per-protocol/as-treated populations | COMPLETE |
| DOC-003 | 14 | PLAN | Table 2 full screening comparison, eligibility | COMPLETE |
| DOC-003 | 15 | PLAN | Eligibility continuation and visually inspected full recruitment Figure 2 | COMPLETE |
| DOC-003 | 16 | PLAN | Withdrawal/loss definitions, qualitative baseline descriptors | COMPLETE |
| DOC-003 | 17 | PLAN | Quantitative baseline descriptors, MI criteria | COMPLETE |
| DOC-003 | 18 | PLAN | MI continuation; stroke duration and exclusions | COMPLETE |
| DOC-003 | 19 | PLAN | Cardiovascular mortality, weight measurement, secondary definitions | COMPLETE |
| DOC-003 | 20 | PLAN | Heart failure, peripheral artery disease thresholds | COMPLETE |
| DOC-003 | 21 | PLAN | VTE and pulmonary embolism criteria | COMPLETE |
| DOC-003 | 22 | PLAN | AF, diabetes, nephropathy quantitative criteria | COMPLETE |
| DOC-003 | 23 | PLAN | Nephropathy continuation, cancer/dementia/depression/fracture definitions | COMPLETE |
| DOC-003 | 24 | PLAN | Secondary definitions, dietary intermediate markers, Cox model | COMPLETE |
| DOC-003 | 25 | PLAN | Mixed models, household/center effects, covariates, 5% thresholds | COMPLETE |
| DOC-003 | 26 | PLAN | Assumptions, sensitivity/subgroups, 20 imputations, causal analysis | COMPLETE |
| DOC-003 | 27 | PLAN | Per-protocol censoring indicators, weights, harms; references begin | COMPLETE |
| DOC-003 | 28 | PLAN | References inspected; no new trial-result quantitative relationship | COMPLETE |
| DOC-003 | 29 | PLAN | References inspected; no new trial-result quantitative relationship | COMPLETE |
| DOC-003 | 30 | PLAN | References continuation/end; no new trial-result relationship | COMPLETE |
| DOC-004 | 1 | REPORT | Supplement cover/index; all eTable/eFigure captions | COMPLETE |
| DOC-004 | 2 | REPORT | eTable 1 all four score definitions and all component rules | COMPLETE |
| DOC-004 | 3 | REPORT | eTable 2 MI foods: olive oil through whole grains | COMPLETE |
| DOC-004 | 4 | REPORT | eTable 2 refined-grain continuation and model footnotes; visual/OCR | COMPLETE |
| DOC-004 | 5 | REPORT | eTable 2 legumes through total yogurt | COMPLETE |
| DOC-004 | 6 | REPORT | eTable 2 fermented dairy and model footnotes; visual/OCR | COMPLETE |
| DOC-004 | 7 | REPORT | eTable 2 low/whole-fat dairy, alcohol, red wine; visual | COMPLETE |
| DOC-004 | 8 | REPORT | Copyright-only separator, visually inspected, no applicable relationship | COMPLETE |
| DOC-004 | 9 | REPORT | eTable 3 completer scores and all MCID derivations | COMPLETE |
| DOC-004 | 10 | REPORT | eTable 3 special er-MedDiet counts; eTable 4 starts | COMPLETE |
| DOC-004 | 11 | REPORT | eTable 4 cereal continuation, whole/refined grain through meat | COMPLETE |
| DOC-004 | 12 | REPORT | eTable 4 processed meat/pastries then dairy through alcohol | COMPLETE |
| DOC-004 | 13 | REPORT | eTable 4 alcohol/red-wine continuation and footnotes; visual/OCR | COMPLETE |
| DOC-004 | 14 | REPORT | eTable 5 completer nutrients: energy through MUFA | COMPLETE |
| DOC-004 | 15 | REPORT | eTable 5 remaining seven nutrients, definitions, footnotes | COMPLETE |
| DOC-004 | 16 | REPORT | eTable 6 baseline-replacement sensitivity, four scores | COMPLETE |
| DOC-004 | 17 | REPORT | eTable 7 baseline-replacement foods, olive oil through cereals | COMPLETE |
| DOC-004 | 18 | REPORT | eTable 7 whole grains through pastries | COMPLETE |
| DOC-004 | 19 | REPORT | eTable 7 dairy through red wine | COMPLETE |
| DOC-004 | 20 | REPORT | eTable 7 model/dispersion footnotes only; visual/OCR | COMPLETE |
| DOC-004 | 21 | REPORT | eTable 8 baseline-replacement nutrients, energy through MUFA | COMPLETE |
| DOC-004 | 22 | REPORT | eTable 8 remaining seven nutrients and all footnotes | COMPLETE |
| DOC-004 | 23 | REPORT | eTable 9 MI and completer risk factors, weight through HDL | COMPLETE |
| DOC-004 | 24 | REPORT | eTable 9 remaining factors, imputation fractions/predictors/conversions | COMPLETE |
| DOC-004 | 25 | REPORT | eFigure 1 four panels, 24 bars, CI marks, all P annotations; visual | COMPLETE |
| DOC-004 | 26 | REPORT | eFigure 2 seven favorable-change pairs, labels, CI marks, P; visual | COMPLETE |
| DOC-004 | 27 | REPORT | eFigure 3 twelve nutrients x two times x two arms; visual | COMPLETE |
| DOC-004 | 28 | REPORT | Additional affiliations inspected; no applicable result relationship | COMPLETE |
| DOC-004 | 29 | REPORT | Additional affiliations continuation; no applicable result relationship | COMPLETE |
| DOC-005 | 1 | REPORT | Data-sharing statement inspected; no applicable quantitative relationship | COMPLETE |

## SAP semantic relationship inventory

Local keys are reusable semantic locators, not canonical N/S IDs. The full source transcription below includes every supporting numerical definition and table row.

| Local key | Source location | Complete relationship and matching main-paper key |
|---|---|---|
| SAP-ADMIN | DOC-003 pp. 1-3 | Trial registration 89898870, July 24 2014; SAP v1 November 2018, v2 July 2019; protocol April 3 2018, accessed July 2 2019. Match trial/SAP identification. Contributors/signatures contain no analysis definition. |
| SAP-OBJECTIVES | pp. 4-5 | Contrast intensive energy-reduced MedDiet + physical activity + behavioral weight-loss support against nonintensive unrestricted MedDiet/usual care. Two primary outcomes: composite nonfatal MI/nonfatal stroke/CV death, and weight loss/maintenance. Composite components not separately analyzed. Intermediate diet/adherence and nutrient intake are explicitly listed. Match intervention description and outcome hierarchy. |
| SAP-DESIGN | p. 6 | Parallel 6-year multicenter RCT, 6874 participants/23 centers. Randomization by center, sex, age <65/65-70/>70, blocks of 6; household members together; later household entrants assigned same arm. Sample-size alpha two-tailed 0.05. Match analysis unit, stratification, clustering, randomized population. |
| SAP-POWER | pp. 6-7 | CV control incidence at least 10% over 6 years; anticipated HR 0.70 (followed by superscript reference 2 in the source); dropout up to 20%; required 2400/arm, planned 3000/arm=6000; about 300 per center=150/arm. Weight change assumptions control 1 kg/intervention 3 kg, difference 2 kg, SD 8 kg, power 0.80, reported required 337/arm; earlier expected loss 3-4.5 kg. Superiority framework for primary, secondary and intermediate outcomes. Match sample-size and framework. |
| SAP-POWER-FIGURE | p. 7 Figure 1, direct render | Title: underlying event rate 10% (overall) in 6 yr. Horizontal sample size each group, tick 1000 to 5000 by 500; vertical power .4 to 1 by .1. Three increasing curves: blue HR=.65, red HR=.70, black HR=.75. No exact point labels; preserve full three curves and input labels rather than assigning interpolated point values. |
| SAP-DECISIONS | p. 8 | O'Brien-Fleming overall alpha .05; interim median follow-up 3 years P=.0005; 5 years P=.014; final median 8 years P=.045. Active intervention 6 years, follow-up 2 additional years, total 8 years/participant; diabetes 7 years (expected 620 cases), Parkinson and cancer 10 years. Match interim/multiplicity and time horizon, preserving distinct outcome-specific follow-up. |
| SAP-TIMELINE | pp. 9-11 Table 1 | Every clinical, intermediate and substudy row retained verbatim below; columns M6,Y1,Y6,Y7,Y8,Y9,Y10. Weight/waist/diet/BP/self-report PA marked M6,Y1,Y6. Diet definitions 17-item erMedDiet and 14-item MedDiet. Renal CKD eGFR<60 mL/min/1.73m2 and UACR>=30 mg/g. Footnotes *1 and 3 years, #5 years; SBP meaningful -5 mmHg; triglycerides -10%; HDL +5%; LDL -5%. Match diet/PA assessment schedule and risk-factor definitions. |
| SAP-ASSESSMENT | p. 12 | Weight and waist duplicated yearly; clinical outcomes yearly blinded record review; blood specimens odd years and 8 years. Match measurement and analysis time. |
| SAP-MULTIPLICITY | p. 12 | Primary outcomes nominal 95% CI, P<.05, no multiplicity adjustment; secondary nominal 95% CI plus ancillary Bonferroni (1-alpha/m) intervals with m=27; source footnote enumerates all 27 comparisons. Match CI confidence level and adjustment of each reported outcome, preserving distinction from interim thresholds. |
| SAP-ADHERENCE | pp. 12-13 | Control >=10/14; intervention weight loss + increased leisure PA MET-min/week or improved chair fitness + >=12/17. Match adherence scale and threshold, not interchangeable score maxima. |
| SAP-POPULATION | p. 13 | Main ITT randomized assignment; full-data and multiple-imputation analyses. Per-protocol weight censoring intervention persistently <12/17 OR persistently decreased PA AND chair fitness on two consecutive yearly assessments; control persistently <10/14. Other outcomes add persistent weight gain to intervention censoring. As-treated classification by diet/weight/PA irrespective of arm; CVD mediation with time-varying mediators/confounders in counterfactual framework. Match complete-case, ITT, sensitivity population and mediation. |
| SAP-SCREENING | p. 14 Table 2 | 2803 nonrandomized versus 6874 randomized; every mean/SD, percentage and P retained below. Eligibility men55-75, women60-75, BMI>=27 and<40 kg/m2, >=3 MetS criteria. Match trial flow and analysis population; screening table values remain descriptive. |
| SAP-FLOW | p. 15 Figure 2, direct render | 9677 assessed; first1195 excluded=706 refusal+489 criteria; 8482 received telephone;1232 refusal;7250 third screening;376 excluded=333 refusal+43 criteria;6874 randomized=6066 individual+808 couples. Control3468=3052 individual+416 couples; intervention3406=3014 individual+392 couples. Two-week intervals between three screenings. Follow-up to be added for final analyses. Match main flow household and randomized totals; this PLAN flow has no published-analysis exclusions. |
| SAP-WITHDRAWAL | pp. 15-16 | Approx50% women and diabetes<=27% cohort stated; yearly visits/charts and death index when 1 year information absent; loss defined >=2 years with no information; consent withdrawal stops future access. Match loss-to-follow-up and imputation population. |
| SAP-ENDPOINT-DEFINITIONS | pp. 17-24 | All primary/secondary diagnostic rules retained below. MI biomarker>99th percentile plus qualifying condition; stroke>24h/ >=24h symptoms with silent infarction/hemorrhage excluded; duplicate weight mean; HF reduced EF<40%, objective findings and timing; PAD ankle-brachial<=.90; AF<200ms/>300bpm; diabetes HbA1c>=6.5%, FPG>=126mg/dL after>=8h, 2h/random>=200mg/dL,75g load; albumin>=30mg/24h or UACR>=30mg/g, 2/3 specimens3-6months; depression treatment>6months; gout uric acid>7mg/dL. All remaining qualitative endpoint distinctions preserved. Match endpoint definitions rather than applying diagnostic rules to dietary scores. |
| SAP-DIET-MARKERS | p. 24 | 17-item energy-restricted score intervention or14-item control plus143-item FFQ; BP/lipids/glucose/renal/uric acid/HbA1c/CRP/liver yearly; medication percentages and questionnaire scores yearly. Match dietary measurement instrument and intermediate outcome role. |
| SAP-MODEL | pp. 24-25 | Cox for primary/secondary except weight/waist; baseline allocation to event; censor at latest visit/record, database close, or death for fatal outcomes. Weight/BMI/waist multilevel repeated-measure linear mixed models with random intercept, household correlation, center random factor (explicit for weight/waist). Within-arm and between-arm changes. Match mixed-model household/center account and contrast. |
| SAP-CLINICAL-CHANGE | p. 25 | Weight meaningful -5%: baseline86.5kg ->4.3kg; BMI baseline32.5 ->1.6kg/m2; waist108cm ->5.4cm. Supporting historical loss3-6kg and58% diabetes reduction, earlier observational OR .38(.19,.79) for BMI loss3-7%, prior waist loss4.4cm retained as rationale rather than current trial outcomes. Match risk-factor clinical threshold. |
| SAP-COVARIATES | pp. 25-26 | Main crude ITT; robust household variance; center-stratified Cox. Additional composite: center strata+sex,age,education,smoking,hypertension,dyslipidemia,diabetes,CHD family history,BMI,waist/height,PA MET-min/day. Weight additionally adjusted center,sex,age,education,smoking,hypertension,dyslipidemia,diabetes,CHD family history,PA. Secondary may add specific covariates. Match primary model versus additional adjustment. |
| SAP-ASSUMPTIONS | p. 26 | Schoenfeld residual/time-varying-covariate tests; if nonproportional add confounder strata, then period-specific effects. Match model-assumption treatment. |
| SAP-SENSITIVITY | p. 26 | Main completer ITT, repeated ITT with multiple imputation; primary per-protocol. Subgroups sex,median age,education2 levels,diabetes,MetS3 vs>=4,smoking,obese/nonobese,baseline erMedDiet score. Match reported subgroup/sensitivity selection and missing-data alternatives. |
| SAP-IMPUTATION | p. 26 | MICE STATA mi,20 imputations per missing measure, outcomes missing among lost>=2years. Predictors sex,age,smoking,leisurePA,BMI,weight,diabetes,hypertension,hypercholesterolemia,CHD family history,arm,second household member,education. Match imputation count,predictors,outcomes and eligible missingness. |
| SAP-PER-PROTOCOL | pp. 26-27 | IPW/G-formula. Aj=1 adherence,0 otherwise; artificial censoring whenAj=0. Cj incomplete attendance within12months; Nj=1 attendance,0 no; amongNj=1,Rj=1 missingAj; amongNj=1,Rj=0 censor ifAj=0. Stabilized inverse probability weights conditional on measured pre/postrandomization prognostic factors. Match analysis-population/censoring logic. |
| SAP-HARMS | p. 27 | Headache,fatigue,constipation,increased bowel rhythm collected6months then yearly; percentage by arm in primary-outcome report. Match adverse-event reporting. |

## Results table schema and complete matching index

Interpretation schema for eTables2-8: each named variable has baseline values for both arms and two separate 6-/12-month change rows. Changes show each arm's modeled mean (95% CI), the modeled between-group difference (95% CI), and its P value. Baseline dispersion remains SD or IQR as explicitly printed; the eTable4 first olive-oil row prints `mean (SD)` while the global footnote says median(IQR), and both statements are preserved. Models incorporate site and household couples as random factors. P-test type/sidedness is not separately specified by these table footnotes; do not assume a crude subtraction or independent-sample test. eTable9 has two separate missing-data/population blocks and 12-month changes only.

| Local block key | Exact source pages | Population / missingness | Variables, all retained | Matching main-paper key |
|---|---|---|---|---|
| SUP-T1 | DOC-004 p.2 | Definition, no analysis sample | erMedDiet17,MDS9,MEDAS14,PDQS42: all components, alcohol rules, a-d scoring footnotes | Dietary score definitions/measurement methods |
| SUP-T2 | pp.3-7 | Multiple imputation, all randomized; printed N3272/N3311; p3 prints both arm headings as Intervention group; continuation p5/p7 names Control | Olive oil, refined oil,EVOO,nuts,fruits,vegetables,cereals,whole grains,refined grains,legumes,fish,meat,red meat,processed meat,pastries,dairy,total yogurt,fermented dairy,low-fat dairy,whole-fat dairy,total alcohol,red wine; 22 variables, all g/week | Food-group outcomes at6/12months; title/pointers to eTable2 |
| SUP-T3 | pp.9-10 | Completers; general n2862/2883 at6months,n2833/2943 at12months; erMedDiet * n3030/3090 and2971/3095 | Four scores,8 inferential change rows; score-specific counts and all MCID rationale | Main score results with complete-case sensitivity distinguished from MI |
| SUP-T4 | pp.10-13 | Completers n2862/2883 at6months,n2833/2943 at12months | Same22 food variables asT2,44 change rows, all g/week | Completer sensitivity for eachT2 food-group outcome |
| SUP-T5 | pp.14-15 | Completers n2862/2883 at6months,n2833/2943 at12months | Energy kcal/day; protein,carbohydrate,total fat,SFA,MUFA,PUFA,alcohol %E; ratioMUFA:SFA; fiber,long-chainomega3,sodium g/week; cholesterol mg/week;13 variables,26 change rows | Main nutrient table and Figure3 nutrient effects; completer sensitivity |
| SUP-T6 | p.16 | All randomized n3272/3311; replace all missing with baseline | Four scores,8 change rows; zero-change imputation alternative | Same four main scores, distinguish baseline replacement fromMI and completers |
| SUP-T7 | pp.17-20 | All randomized n3272/3311; replace all missing with baseline | Same22 foods asT2;44 change rows | Same food outcomes, baseline-replacement sensitivity |
| SUP-T8 | pp.21-22 | All randomized n3272/3311; replace all missing with baseline | Same13 nutrients asT5;26 change rows | Same main nutrient outcomes, baseline-replacement sensitivity |
| SUP-T9-MI | pp.23-24 | MI n3272/3311 | Weightkg,waistcm,BMIkg/m2,cholesterol/LDL/HDL/nonHDL/triglyceridesmg/dL,cholesterol:HDL ratio,SBP/DBPmmHg;11 baseline pairs and11 change rows | Main anthropometric/risk-factor results and weight-change analysis |
| SUP-T9-CC | pp.23-24 | Completers n2840/2946 | Same11 risk factors; separate baseline pairs and11 change rows | Same risk factors with completer sensitivity |

Row-level local keys are deterministic: `SUP-T{table}-{variable}-{baseline|6mo|12mo}`, appending `-MI` or `-CC` for eTable9. Variable labels and every numeric cell occur in the page-linked full transcription below; no table row is omitted. Counts: 122 variable/population blocks;122 baseline rows plus222 inferential change rows=344 numerical table rows across eTables2-9. eTable1 definition cells and figure series are additional. This is a coverage count, not a candidate count.

## Result-specific footnote and formula keys

- SUP-MODEL: eTables2-9 baseline SD/IQR as printed; changes mean95%CI via mixed effects with site and couple correlation random factors. No OR/RR/HR is presented for the current dietary mean-change comparisons.
- SUP-SCORE-DIRECTION: all four scores higher=healthier; ranges17,9,14,42. eTable1 MDS positive >=sex median and negative <=sex median; alcohol women5-25g/day,men10-50; erMedDiet alcohol men2-3/women1-2 glasses/day; MEDAS wine>=7glasses/week. PDQS 21 components=13 positive+8 negative; positive0/1/2points for0-1/2-3/>=4servings/week, negative reversed. Full component labels retained in transcription.
- SUP-MCID: DOC-004p9 MDS2points about1SD,25% relative all-cause mortality reduction; log(.75)=-.2877 and exp(-.2877/2)=.87 for1point/.5SD/about13% reduction; MCID1point. MEDAS1point linked in supplied rationale to HR.90(.85,.96) CV and.94(.89,.99) mortality; MCID1point also erMedDiet; PDQS probably2points,SD3.7. These are source-provided rationale, not new external evidence.
- SUP-T9-IMPUTATION: chained equations predictors arm,sex,age,smoking,education,PA,baselineBMI,energy,baseline target variable. Fractions imputed: BMI5%,weight4.7%,waist9.4%,cholesterol10.1%,HDL10.8%,LDL10.9%,nonHDL10.9%,cholesterol:HDL10.9%,triglycerides10.3%,SBP6.1%,DBP6.2%. Convert cholesterol/HDL/LDLmg/dL to mmol/L by x.0259; triglycerides byx.0113.
- SUP-PRINTED-CELLS: retain all printed source values without silent normalization, including DOC-004p7 red-wine intervention median33(0,29), p13 median4(0,29), p19 median0(0,29); p22 control baseline cholesterol2687(825),p15 2682(794). Source values are locators for checking, not findings.

## Complete visual figure series

### SUP-F1 — DOC-004 p.25, eFigure1

Four panels, each intervention purple/controlgray at baseline,6months,12months; mean score with95%CI marks. Numeric means/CI bounds are not printed on individual bars. Full matching series are the four score rows in the main dietary-score results and eTables3/6 with the appropriate missingness distinction; add displayed baseline means to displayed changes only as a rounded descriptive aid, never as exact modeled follow-up values. All panel series are preserved:

| Panel | Range/title | Baseline P | 6-month P | 12-month P | Visual series |
|---|---|---|---|---|---|
| erMedDiet | 0-17points; axis ticks0,3,6,9,12,15,18 | .13 | <.001 | <.001 | Arms both about8.5baseline; intervention about12.5/12.7 vscontrol10.3/10.6; all six95%CI bars |
| MEDAS | 0-14points; axis ticks0,3,6,9,12 | .42 | <.001 | <.001 | Arms about7.6baseline; intervention about10/10.2 vscontrol9/9.1; all six95%CI bars |
| MDS | 0-9points; axis ticks0,2,4,6,8 | .98 | <.001 | <.001 | Both about4.3baseline; intervention about4.5at6/12 vscontrolabout4.0; all six95%CI bars |
| PDQS | 0-42points; axis ticks0,10,20,30,40 | .76 | <.001 | <.001 | Both about21baseline; intervention about25.5at6/12 vscontrolabout23; all six95%CI bars |

P values compare arm means, per caption. Approximate plotted heights above are visually described, not exact extracted numbers; exact means/limits require the source's tabular matches or underlying data. No point digitization was performed.

### SUP-F2 — DOC-004 p.26, eFigure2

Title favorable dietary changes after12months. Seven bar pairs, purple intervention/graycontrol; yaxis percentage participants(95%CI), ticks0,20,40,60,80,100. Caption P compares proportions. Preserve printed labels by horizontal bar position separately from approximate bar height; source does not print CI bounds or denominator counts here.

| Change | Printed purple label | Printed gray label | P annotation | Approximate plotted purple/gray heights (%) |
|---|---:|---:|---|---|
| Decreased fat | 34% | 32% | .14 | 32/34 |
| Increased MUFA | 72% | 77% | <.001 | 77/72 |
| Increased MUFA:SFA | 79% | 86% | <.001 | 86/79 |
| Increased fruit | 58% | 63% | <.001 | 63/58 |
| Increased vegetables | 56% | 64% | <.001 | 64/56 |
| Decreased meat | 60% | 62% | .08 | 62/60 |
| Decreased sugary dessert | 59% | 58% | <.001 | 68/60 |

All14bars andCI marks were inspected. Do not substitute a label for graphical geometry or infer denominators from other tables without a matching source definition. Matching main-paper key: proportions making intended favorable changes, distinguish these proportions from amount-of-change outcomes in food/nutrient tables.

### SUP-F3 — DOC-004 p.27, eFigure3

Two columns6months/12months; each column contains all12nutrients listed below, with intervention purple andcontrolgray box/whisker series. Horizontal scale SD,ticks-3,-2,-1,0,1,2,3. Caption defines common units of baseline standard deviations. No numeric quartile/whisker limits, P values, or exact standardized coordinates are printed; no CI interpretation is assigned to these box/whisker marks.48 arm/time series mapped; raw amount-of-change matching keys are main nutrient results and SUP-T5/T8, not identical statistical summaries.

| Variable | Plot-unit label | Visual relative location at both times; all four series inspected |
|---|---|---|
| Energy | Energy intake,(SD) | Intervention shifted lower than control; both distributions cross0 |
| Protein | Protein intake,%kcal(SD) | Intervention shifted higher; both cross0 |
| Carbohydrate | CHO intake,%kcal(SD) | Intervention shifted lower; both cross0 |
| Fat | Fat intake,%kcal(SD) | Intervention shifted higher; both cross0 |
| SFA | SFA intake,%kcal(SD) | Intervention shifted lower; both cross0 |
| MUFA | MUFA intake,%kcal(SD) | Intervention shifted higher; both cross0 |
| MUFA:SFA | RATIO MUFA:SFA,(SD) | Intervention shifted higher; both cross0 |
| PUFA | PUFA intake,%kcal(SD) | Intervention shifted higher; both cross0 |
| Fiber | FIBER intake,(SD) | Intervention shifted higher; both cross0 |
| Cholesterol | CHOLESTEROL intake,(SD) | Distributions largely overlap around0 |
| Long-chainomega3 | w-3 intake,(SD) | Intervention shifted higher; both cross0 |
| Alcohol | Alcohol intake,%kcal(SD) | Narrower distributions around0; intervention slightly lower |

## No-applicable records and limitations

DOC-005p1 states deidentified participant data available with publication, restricted to external research following project purposes after steering-committee proposal approval; supporting documents:none; analyses:specified purpose. No result-relevant statistical model, value, denominator, or decision rule is present. DOC-004p8 is copyright-only; pp28-29 are affiliations only. DOC-003p1/3 and reference-only pp28-30 have no new quantitative trial relationship; all were read in full and remain mapped.

Scientific coverage gaps: None. Extraction limitations: exact unlabelled figure points, CI bounds, box/whisker statistics, and power-curve points cannot be recovered as exact numerical values from these supplied plots. All full series, panels, scales, labels and captions are nevertheless covered. No implied raw-data or external-data reconstruction was attempted. Additional SAP figure renders were generated as documented; no source/reused-asset modification, Python extraction/OCR, web access, or GPU use occurred.

## Full page-linked source transcription

This lossless transcription is an integral part of the map. It records all344 quantitative table rows, eTable1 scoring cells, SAPTable1/2 rows, all source footnotes and all administrative content. Line-wrapped negative intervals/P values retain original layout; visual checks above supply graphic content absent from native text. All links end in the exact PDF page.

### DOC-003 PDF p. 1 — PLAN

[SAP source p. 1](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=1>)

```text
                     Supplementary Online Content


Sayón-Orea C, Razquin C, Bulló M, et al. Effect of a nutritional and behavioral
intervention on energy-reduced Mediterranean diet adherence among patients
with metabolic syndrome [published October 15, 2019]. JAMA.
doi:10.1001/jama.2019.14630



Supplement 2. Statistical analysis plan

This supplementary material has been provided by the authors to give readers
additional information about their work.

```

### DOC-003 PDF p. 2 — PLAN

[SAP source p. 2](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=2>)

```text
 1   SECTION 1: ADMINISTRATIVE INFORMATION

 2

 3   Title and trial registration

 4

 5       Effect of an energy-reduced Mediterranean diet, physical activity and behavioral
 6   intervention on the primary prevention of cardiovascular disease – Statistical analysis plan

 7

 8       Trial registered at the International Standard Randomized Controlled Trial (ISRCT;
 9   http://www.isrctn.com/ISRCTN89898870) with number 89898870 and a registration date of 24
10   July 2014.

11   SAP version: 2

12

13       SAP version 1- date November 2018

14       SAP version 2- date: July 2019

15   Protocol version

16       April 3rd, 2018

17

18      Available at: https://www.predimedplus.com/wp-content/uploads/2016/07/Protocolo-
19   PREDIMED_PLUS_eng_Jan2014_12-03-2018-y-April_2018_03-04-2018.pdf

20

21       Accessed: July 2nd, 2019

22

23   SAP revisions

24

25       July 2019

26

27

28


                                                    1

```

### DOC-003 PDF p. 3 — PLAN

[SAP source p. 3](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=3>)

```text
29   Roles and responsibility

30      SAP contributors:
31          1. Person writing the SAP

32                Estefanía Toledo, MD, MHP, PhD and Alfredo Gea, DPharm, PhD

33                Department of Preventive Medicine and Public Health, University of Navarra

34                CIBER Fisiopatología de la Obesidad y Nutrición

35

36          2. Senior statistician responsible

37                Miguel A. Martínez-González, MD, PhD, MPH, Professor of Epidemiology

38                Jesus López-Fidalgo, PhD, Professor of Statistics

39
40          3. Chief investigator/clinical lead: Jordi Salas-Salvadó, Miguel A. Martínez-González
41

42   Signatures

43

44      ________________________________

45      Estefanía Toledo

46

47      ________________________________

48      Alfredo Gea

49

50      ________________________________

51      Miguel A Martínez-González

52

53      ________________________________

54      Jesús López Fidalgo

55

56      ________________________________

57      Jordi Salas-Salvadó

                                                        2

```

### DOC-003 PDF p. 4 — PLAN

[SAP source p. 4](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=4>)

```text
58   SECTION 2: INTRODUCTION

59   Background and rationale

60       The completed PREDIMED (in Spanish: PREvención con DIeta MEDiterránea) cardiovascular
61   primary prevention trial (Martinez-González et al, 2012) successfully demonstrated that long-
62   term adherence to an unrestricted-energy Mediterranean diet (MedDiet) supplemented with
63   extra-virgin olive oil (EVOO) or mixed nuts reduced the incidence of major clinical events of
64   cardiovascular disease (CVD) in older individuals at high risk. Final results were republished in
65   2018 showing an approximately 30% relative reduction in the risk for the composite primary
66   end-point of stroke, myocardial infarction and cardiovascular death (Estruch et al, 2018).
67   However, the PREDIMED trial only tested changes in the composition of the overall diet, not in
68   other lifestyle aspects such as total energy intake (as it was ad libitum), physical activity, or
69   weight loss.

70        The rationale for the new PREDIMED-Plus randomized controlled trial (RCT) is to go
71   beyond the intervention delivered in PREDIMED and to answer one of the most important
72   questions for clinical practice in the context of the current unprecedented obesity pandemic
73   (The GBD 2015 Obesity Collaborators, 2017; González-Muniesa et al, 2017): is intentional
74   weight loss (using diet and physical activity) able to bring about a substantial reduction in
75   clinical CVD events in the long-term? Our main hypothesis is that by addressing 3 new lifestyle
76   factors (energy reduction with a high-quality dietary pattern, increased physical activity (PA)
77   and weight loss) an even stronger reduction in the risk of hard CVD end-points will be attained
78   (Martinez-González et al, 2018).

79       PREDIMED-Plus is expected to obtain synergy from the beneficial effects of a high-quality
80   diet (a MedDiet) plus an intensive weight-loss intervention (using energy reduction and
81   physical activity) on CVD incidence. This strategy should have positive effects on weight loss
82   (focused on loss of fat mass) and long-term weight-loss maintenance, as shown in a 2-year
83   randomized trial comparing an energy-reduced MedDiet versus low-fat versus low-
84   carbohydrate diets (Shai et al, 2008; Schwarzfuchs et al, 2012).

85

86   Objectives

87        Our long-term objective is to provide effective treatment for reducing excessive CVD
88   morbidity and mortality in overweight and obese adults, irrespective of whether the
89   participants are diabetic at the beginning of the study. To achieve this goal, we will compare
90   the effects on CVD rates of an intensive lifestyle and weight loss intervention program based
91   on the traditional Mediterranean diet and including increased physical activity, energy
92   reduction and behavioral support (intervention group) with those of a non-intensive
93   intervention program that provides both education on the traditional Mediterranean diet for
94   the prevention of CVD in accordance with the principles outlined in the PREDIMED trial and
95   usual care by primary healthcare professionals (control group). The importance of attending
96   visits to healthcare professionals will be stressed and general recommendations on
97   management of the metabolic syndrome will be provided to the control group.

98

99



                                                      3

```

### DOC-003 PDF p. 5 — PLAN

[SAP source p. 5](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=5>)

```text
100       Main specific objectives

101      To evaluate the effect of an intensive weight-loss-oriented lifestyle intervention program
102   based on a traditional Mediterranean diet with energy reduction, increased physical activity
103   and behavioral therapy on 2 primary end-points:

104      1. The incidence of CVD (a composite of non-fatal myocardial infarction, non-fatal stroke
105   and cardiovascular death)

106       2. Weight loss and long-term maintenance of weight-loss

107      Importantly, the 3 different components of the primary CVD end-point, namely stroke,
108   myocardial infarction and cardiovascular death, will not be analyzed separately.

109

110       Specific secondary objectives

111       This intensive intervention program is likely to result in reductions of:
112           - waist circumference
113           - acute coronary syndromes
114           - coronary revascularization
115           - transient ischemic attack
116           - total mortality
117           - heart failure
118           - peripheral artery disease
119           - venous thrombosis
120           - atrial fibrillation
121           - type-2 diabetes
122           - complications of type-2 diabetes (diabetic nephropathy, diabetic retinopathy and
123                 diabetic polyneuropathy)
124           - total cancer
125           - cancer in main sites (breast, prostate, colorectal, lung and stomach)
126           - gallstone disease
127           - symptomatic gout
128           - neurodegenerative disorders (dementia and Parkinson’s disease)
129           - unipolar depression
130           - osteoporotic fractures
131           - cataract surgery
132           - surgery for obesity
133           - eating behavior disorders

134       We will also address the effect of the intervention on the following intermediate outcomes:
135   nutrient intake and adherence to an overall healthy dietary pattern, systolic and diastolic
136   blood pressure, serum lipid concentrations, fasting glucose, glycated hemoglobin and uric acid,
137   kidney function, liver function, C-reactive protein, anti-hypertensive, anti-diabetic and lipid-
138   lowering medication needs, ECG traits, cognitive function, quality of life, and
139   psychopathological scales.

140      We will also store plasma, serum, peripheral cells and urine samples to evaluate other
141   hypotheses in the future, depending on availability of additional funding.



                                                       4

```

### DOC-003 PDF p. 6 — PLAN

[SAP source p. 6](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=6>)

```text
142   SECTION 3: STUDY METHODS

143   Trial design

144       The PREDIMED-Plus trial is a 6-year parallel-group, multicenter RCT involving 6,874
145   participants recruited in 23 Spanish recruiting centers. The main aim is to assess the effect of
146   an intensive weight-loss intervention based on an energy-reduced Mediterranean diet
147   (erMedDiet), PA promotion, and behavioral support on CVD events in comparison with a
148   control group receiving usual care, including the recommendation to follow an unrestricted-
149   energy MedDiet without advice to increase PA. The primary end point is a combination of CVD
150   events (non-fatal myocardial infarction, non-fatal stroke and cardiovascular death).

151       A detailed description of the intervention can be found in the trial protocol
152   (https://bit.ly/2OZsv3n).

153

154   Randomization

155       For the baseline visit, each recruiting center randomly assigned eligible candidates to one
156   of two groups, intensive intervention group or usual care (control) group, using a centrally-
157   controlled,       computer-generated         random-number         system       (available    at:
158   www.predimedplus.com). The University of Navarra, Department of Preventive Medicine and
159   Public Health was responsible for the randomization procedure by which participants were
160   randomly assigned with stratification by center, sex, and age group (<65, 65-70, >70 years) in
161   blocks of 6. However, during the randomization stage, centers and staff were blinded to this
162   block size in order to ensure absolutely blinded randomization. Members of the same
163   household were randomized together. The recruiting centers entered the participants’
164   identification criteria into the internet-based system in a blind manner, without any possible
165   foretelling of the group that the participant will be allocated. Therefore, a completely blinded
166   randomization procedure was used. The system automatically assigned each participant or
167   members of the same household to their allocated groups according to a random and
168   unpredictable algorithm, out of the control of any staff involved in the trial.

169       Once this occurred, the assigned group could not be changed. In the specific cases of other
170   members of the same household who were recruited at a different time than the first
171   recruited member of the same household, the last member of the same household entering
172   the study was assigned (not randomized) to the same study arm as the first member of that
173   household in order to ensure high compliance with the intervention, peer support, and also to
174   avoid contamination and potential conflicts between members of the same household.

175

176   Sample size

177        We will determine the effect of the intensive weight-loss lifestyle intervention with an
178   energy-reduced Mediterranean diet on the two primary outcomes below, assuming a two-
179   tailed alpha error of 0.05.

180       1. Effect of the intervention on incident CVD (exclusively, a composite non-fatal myocardial
181   infarction, non-fatal stroke, and cardiovascular death). The cumulative projected incidence
182   after including as primary events the cardiovascular composite of stroke, cardiovascular deaths


                                                       5

```

### DOC-003 PDF p. 7 — PLAN

[SAP source p. 7](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=7>)

```text
183   and all non-fatal acute myocardial infarctions with positive high-sensitivity troponin tests after
184   6 years will be at least 10% in the control group, based on the observed results in the
185   PREDIMED trial after 4.8 years (which did not include high-sensitivity troponin tests). The
186   hazard ratio (HR) for the combined primary endpoint is anticipated to be 0.702 and will
187   probably be even lower (greater protective effect) after considering that in the PREDIMED trial
188   no energy reduction was implemented, physical activity was not encouraged, and weight loss
189   was not a target of the intervention. Under these assumptions, therefore, even if the dropout
190   rates were to reach 20%, the required sample size would be 2,400 per group (see Figure 1). To
191   be conservative, however, we planned to recruit 6,000 participants and assign 3,000
192   participants to each group. The participants were recruited at 23 recruiting centers, each of
193   which had the goal of recruiting, educating and following approximately 300 participants, 150
194   in the control group and 150 in the intensive intervention group.

195




196

197        Figure 1. Estimation of the sample size required per intervention group in the PREDIMED-
198                                               PLUS trial

199

200        2. Effect of the intervention on weight change. Based on previous studies, we can expect a
201   minimum weight change for participants in the control group and a weight loss of 3-4.5 kg for
202   those in the intensive lifestyle intervention group, with a standard deviation of 8 kg (Shai et al,
203   2008; Sacks et al, 2009; Look AHEAD Research Group, 2010). Assuming that our intervention
204   will have only a small effect on weight change and calculating the sample size according to a
205   weight change of 1 kg in the usual care group, a weight change of 3 kg in the intensive lifestyle
206   intervention group (net difference = 2 kg), and a standard deviation of 8 kg, in order to achieve
207   a statistical power of 0.80 we would need a sample size of only 337 in each group. Since the
208   number of participants to be recruited is much higher than this figure, the statistical power
209   needed to reach this objective is largely guaranteed.

210

211   Framework

212       Framework: superiority hypothesis testing.

213       Assessment of primary, secondary and intermediate outcomes will be based on this
214   framework.


                                                        6

```

### DOC-003 PDF p. 8 — PLAN

[SAP source p. 8](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=8>)

```text
215

216   Statistical interim analyses and stopping guidance

217       Data from the PREDIMED-PLUS trial will be analyzed after 3 years of median follow-up,
218   after 5 years of median follow-up, and at the end of the trial. For methodological reasons but
219   especially for ethical motives, suitable follow-up for a trial must include at least one interim
220   analysis (Schulz and Grimes, 2005). However, to preserve an overall alpha error of 0.05,
221   interim analyses have to be penalized. We will use the O’Brien and Fleming boundaries
222   (O'Brien and Fleming, 1979). With this method, the boundaries are stricter at the earlier stages
223   of the study than at the later ones. Applying this rule leads to the following p values for
224   stopping the trial (Schulz and Grimes, 2005):

225              First interim analysis (median follow-up: 3 years); threshold p value: 0.0005.
226              Second interim analysis (median follow-up: 5 years); p value: 0.014.
227              Final analysis (median follow-up: 8 years); p value: 0.045

228

229   Timing of final analysis

230       Active intervention will be implemented during the first 6 years of trial duration (this 6-
231   year period does not correspond to the median follow-up time, because all participants will
232   homogeneously complete 6 years of intervention) and they will be followed-up for two further
233   years to assess incident outcomes (Table 1). Thus, the total duration of the trial will be 8 years
234   for each participant.

235       Information will be collected for 8 years after the baseline visit date for each participant.

236        Overall, hard clinical end-points will be assessed only after completion of the 8-year
237   follow-up period. The only exceptions will be:

238       a) Type 2 diabetes–follow-up 7 years: according to the Diabetes Prevention Impact
239          Toolkit (https://nccd.cdc.gov/Toolkit/DiabetesImpact/), the expected number of
240          incident type 2 diabetes cases among participants initially free of diabetes during the
241          first 7 years is high (620), so that we expect to have sufficient statistical power after 7
242          years of follow-up.
243       b) Parkinson’s disease–follow-up 10 years: the incidence of Parkinson’s disease is lower
244          than for other reported outcomes so that participants will be followed for 10 years to
245          ensure a high-enough statistical power
246       c) Cancer: we will consider not only overall cancer but also specific cancers as outcomes.
247          In order to have a sufficient number of cases after breaking down by cancer location
248          and to allow for a long-enough induction time, participants will be followed-up for 10
249          years.

250

251




                                                         7

```

### DOC-003 PDF p. 9 — PLAN

[SAP source p. 9](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=9>)

```text
252     Table 1. Timeline for reported outcomes
                                                                                                                           Follow-up
                                                Outcomes                                                 M-6   Y-1   Y-6    Y-7    Y-8   Y-9   Y-10
      Primary
      1. Composite endpoint of cardiovascular death, non-fatal myocardial infarction or stroke                                     X
      2. Body weight change                                                                               X    X     X
      Secondary
      3. Death from any cause                                                                                                      X
      4. Waist circumference change                                                                       X    X     X
      5. Incidence of acute coronary syndrome (unstable angina)                                                                    X
      6. Incidence of coronary revascularization (percutaneous or surgical)                                                        X
      7. Incidence of atrial fibrillation                                                                                          X
      8. Incidence of peripheral artery disease                                                                                    X
      9. Incidence of heart failure                                                                                                X
      10. Incidence of type-2 diabetes                                                                                      X
      11 Incidence of type-2 diabetes complications (diabetic nephropathy, diabetic retinopathy and
                                                                                                                                   X
        diabetic polyneuropathy)
      12. Incidence of dementia/Alzheimer’s disease                                                                                X
      14. Incidence of other dementias, diagnosed when there are cognitive or behavioral
                                                                                                                                   X
        (neuropsychiatric) symptoms (see protocols)
      15. Incidence of Parkinson’s disease                                                                                                      X
      16. Incidence of major unipolar depression                                                                                   X
      17. Incidence of osteoporotic fractures                                                                                      X
      18. Incidence of gallstone disease or cholecystectomy                                                                        X
      19. Incidence of symptomatic gout                                                                                            X
      20. Incidence of transient ischemic attack                                                                                   X
      21. Incidence of cataract surgery                                                                                            X
      22. Incidence of venous thromboembolism                                                                                      X
      23. Incidence of total cancer and specific cancers in main cancer sites (breast, prostate, lung,
                                                                                                                                                X
        colorectal, or stomach)



                                                                                    8

```

### DOC-003 PDF p. 10 — PLAN

[SAP source p. 10](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=10>)

```text
253
      Secondary (continued):                                                                              M-6   Y-1   Y-6   Y-7   Y-8   Y-9   Y-10
      24. Eating behavior disorders                                                                                                X
      25. Surgery for obesity                                                                                                      X
      Other intermediate outcomes are changes in:
      27. Overall diet (17-item score of adherence to the energy-reduced Mediterranean diet and
                                                                                                           X    X     X
       14-item score of Mediterranean diet) and nutrient intake
      28. Blood pressure (Systolic1 and Diastolic blood pressure)                                          X    X     X
      28. Fasting blood glucose and hemoglobin A1C levels                                                  X    X                 X
      29. Serum lipid concentrations (triglycerides2, cholesterol, and HDL3 and LDL4 cholesterol)          X    X                 X
      30. Renal function (changes in estimated glomerular filtration rate (eGFR) and urine
       microalbumin-to-creatinine ratio (UACR), incidence and reversion of chronic kidney disease               X     X#          X
                                       2
       (CKD, eGFR<60 ml/min/1.73m ) and microalbuminuria (UACR≥30 mg/g))
      31. Uric acid levels                                                                                                        X
       32. Liver function (liver fat content and non-invasive markers of liver status such as
                                                                                                                                   X
        aspartate aminotransferase, alanine aminotransferase, gamma-glutamyltransferase)
       33. Inflammation markers (C-reactive protein and white blood cell counts and its subtypes
                                                                                                                                   X
        (neutrophil, lymphocyte, monocyte, basophils, and eosinophil))
       34. Other intermediate markers of cardiovascular risk (circulating levels of fasting serum
        insulin, leptin, C-peptide, hs-CRP, interleukin-6 (IL-6), IL-8, IL-18, tumor necrosis factor-α,          X
        MCP-1, and regulated on activation, normal T-cell expressed and secreted cytokines
       35. Results of ECGs and alterations of the cardiac rhythm                                                                   X
       36. Quality of life (Short -Form 36 quality of life scale)                                                            X
       37. Cognitive function (including 6 tests: Mini-Mental State Examination, clock drawing test,
        semantic and phonemic verbal fluency test, the reverse series of digits test (WAIS-III) and                    X
        trail making test)
       38. Psychological and neuropsychological scores (including 3 tests: Beck Depression
        Inventory (BDI-II), multidimensional scale of weight locus control and screening for                           X
        comorbid eating disorders with diagnostic criteria)
       39. Medication use (anti-hypertensive, anti-diabetic and lipid-lowering medication)                             X


                                                                                        9

```

### DOC-003 PDF p. 11 — PLAN

[SAP source p. 11](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=11>)

```text
254
        Other intermediate outcomes are changes in (continued):                                          M-6      Y-1     Y-6      Y-7     Y-8     Y-9     Y-10
      40. Total physical activity (PA), light-PA, and moderate-to-vigorous PA measured by
                                                                                                           X       X       X
       periodically administered REGICOR Short Physical Questionnaire (self-reported data)
      41. Reversal of obesity, metabolic syndrome (MetS) and specific criteria for the MetS
       (abdominal obesity, hypertriglyceridemia, low HDL-cholesterol levels, high blood pressure,                                   X
       and high fasting plasma glucose concentrations).
      42. Total physical activity (PA), light-PA, and moderate-to-vigorous PA measured using
                                                                                                                           X
       objective methods, such as accelerometry
      43. Bone density and body composition measured with DXA*                                                             X
      44. Ambulatory blood pressure, obtained by 24-hour ABPM                                                              X
      Other sub-studies
      45. Analysis of the results in relation to genetic studies (DNA and mRNA)                                                    X?
      46. Epigenetic studies and overexpression of microRNAs                                                                       X?
      47. Composition and function of intestinal microbiota by pyrosequencing                                     X*
      48. Metabolomics, transcriptomics and proteomics                                                                             X?

255        *At 1 year and 3 years of follow-up. #At 5 years of follow-up.
256            1: Besides assessing systolic blood pressure as a continuous trait, we will also assess a 5 mm Hg systolic blood pressure reduction as a clinically
257   meaningful change (Stamler et al, 1991).
258            2: Besides assessing triglycerides as a continuous trait, we will also assess a 10% triglyceride reduction as a clinically meaningful change. The
259   reduction of serum triglycerides has been associated with reduced coronary heart disease rates in clinical trials of hypotriglyceridemic agents (Miller, 2011),
260   but no algorithm relating percent triglyceride decrease to percent risk reduction has been developed. In the general population, there is a graded increase in
261   risk with increasing fasting or nonfasting triglycerides (Nordestgaard, 2014), hence a 10% reduction can be considered clinically meaningful.
262            3: Besides assessing HDL-cholesterol as a continuous trait, we will also assess a 5% HDL-cholesterol increase as a clinically meaningful change
263   (Gordon, 1989)
264            4: Besides assessing LDL-cholesterol as a continuous trait, we will also assess a 5% LDL-cholesterol reduction as a clinically meaningful change
265   (Cholesterol Treatment Trialists’ Collaboration, 2010)




                                                                                      10

```

### DOC-003 PDF p. 12 — PLAN

[SAP source p. 12](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=12>)

```text
266   Timing of outcome assessments

267       Weight and waist circumference are measured in duplicate by trained study personnel at
268   the yearly follow-up visits.

269       Other primary and secondary outcomes will be ascertained yearly by systematic review of
270   the participants’ medical charts by medical doctors who are blinded to the intervention group.
271   Codified copies of the medical reports in which the outcome is described will be sent to the
272   Event Ascertainment Committee whose members will confirm the outcome.

273       Blood specimens are collected at odd-year visits and after 8 years of follow-up.



274   SECTION 4: STATISTICAL PRINCIPLES

275   Confidence intervals and p values

276        Primary outcomes:
277        Given that the list of primary outcomes has been defined a priori and that there is
278   substantial evidence that suggests a potential beneficial effect of the intervention on the
279   considered outcomes, we understand that no adjustment for multiplicity will be necessary. We
280   will present point estimates together with 95% confidence intervals. P-values below 0.05 will
281   be deemed as statistically significant.

282       Secondary outcomes:
283       We will present two forms of confidence intervals for the secondary outcomes: nominal
284   confidence intervals and, only as ancillary analyses, multiple-testing-adjusted confidence
285   intervals. Nominal 95% confidence intervals will describe results from a single outcome
286   assessment. We will also estimate multiple-testing-adjusted confidence intervals based on the
287   Bonferroni procedure (1-/m confidence intervals, where m is the number of comparisons1)
288   for secondary outcomes, where m is the total number of secondary outcomes, namely m=27.
289   Our reports will primarily focus on nominal confidence intervals based on coherence and
290   biological plausibility for interpretation of our findings, but we will also add multiple-testing-
291   adjusted confidence intervals for secondary outcomes, only as ancillary analyses.

292

293   Adherence

294       Adherence in the control group will be defined as achieving a score of at least 10 points in
295   the 14-item screener of adherence to the traditional Mediterranean diet (Schröder et al, 2011).


          1
            The total number of comparisons will be 27: 1) death from any cause, 2) change in waist
      circumference, 3) acute coronary syndrome (unstable angina) or coronary revascularization
      (percutaneous or surgical), 4) atrial fibrillation, 5) peripheral artery disease, 6) heart failure, 7) type-2
      diabetes, 8) diabetic nephropathy, 9) diabetic retinopathy, 10) diabetic polyneuropathy, 11) overall
      dementia and Alzheimer’s disease 12) Parkinson’s disease, 13) Major unipolar depression, 14)
      osteoporotic fractures, 15) gallstone disease or cholecystectomy, 16) symptomatic gout, 17) transient
      ischemic attack, 18) cataract surgery, 19) venous thromboembolism, 20) total cancer, 21) breast cancer,
      22) prostate cancer, 23) lung cancer, 24) colorectal cancer, 25) stomach cancer, 26) eating behavior
      disorder, and 27) surgery for obesity.

                                                             11

```

### DOC-003 PDF p. 13 — PLAN

[SAP source p. 13](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=13>)

```text
296       Adherence in the intervention group will be defined as:
297       1) weight loss in comparison with baseline weight,
298       2) increased physical activity according to self-reported leisure-time physical activity
299          (Minnesota questionnaire assessing METS-min/wk) or improvement in physical fitness
300          according to the chair-test, and
301       3) achieving a score of at least 12 points in the 17-item screener of adherence to an
302          energy-reduced Mediterranean diet.

303

304   Analysis populations

305        Main analyses will be conducted based on an intention-to-treat approach (each participant
306   will remain in the randomly allocated group). Intention-to-treat analyses will be conducted
307   based on a) participants with full data only and b) analysis with multiple imputation for missing
308   data.

309       For the per-protocol analysis for weight change, participants in the intervention group will
310   be censored if:
311       a) they show a persistent score of adherence to the energy-reduced Mediterranean diet
312           below 12 points in two consecutive yearly assessments, or
313       b) they show a persistent decrease in physical activity (self-reported information) and
314           physical fitness (chair test) compared with the baseline information in two consecutive
315           yearly assessments.
316
317          and participants in the control group will be censored if they show a persistent score
318   of adherence to the Mediterranean diet (14-item score, based on ad libitum energy intake)
319   below 10 points in two consecutive yearly assessments.

320       In the per-protocol analysis for other outcomes, participants in the intervention group will
321   be censored if:
322       c) they show a persistent score of adherence to the energy-reduced Mediterranean diet
323            below 12 points in two consecutive yearly assessments, or
324       d) they show a persistent decrease in physical activity (self-reported information) and
325            physical fitness (chair test) compared with the baseline information in two consecutive
326            yearly assessments, or
327       e) they show a persistent weight gain compared with the baseline weight in two
328            consecutive yearly assessments
329
330          and participants in the control group will be censored if they show a persistent score
331   of adherence to the Mediterranean diet (14-item score, based on ad libitum energy intake)
332   below 10 points in two consecutive yearly assessments.
333
334        We will also perform analysis on an as-treated basis, classifying participants according to
335   their adherence to Mediterranean diet, weight loss and physical activity level, independently
336   of their assigned intervention. This analysis will be complemented with formal analyses of
337   mediation for the primary outcome (CVD). We will adapt the approaches proposed by Lange
338   (Lange et al, 2011) and Lin (Lin et al, 2017), including time-varying mediators and confounders.
339   These approaches model the mediation effect in a counterfactual framework and can estimate
340   the direct effect and indirect effects of the lifestyle intervention on CVD risk. Thus, we can
341   evaluate the mediation effects of both weight loss and through improvement in diet quality
342   and physical fitness beyond the effects of weight loss.

                                                       12

```

### DOC-003 PDF p. 14 — PLAN

[SAP source p. 14](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=14>)

```text
343   SECTION 5: TRIAL POPULATION

344   Screening data

345       Table 2 shows the characteristics of the participants who attended the first screening visit
346   but were not finally included in the trial and the participants who were finally randomized.

347         Table 2. Description of participants who attended the first screening visit but were not finally
348                         included in the trial and participants who were randomized.
      Characteristics at baseline                                  Non-            Randomized              p value
                                                              randomized
      N                                                            2803                 6874                  -
      Age (mean years, SD)                                       65.9 (5.1)          64.9 (4.9)           <0.001
      Female sex (%)                                               53.8                 48.5              <0.001
      Baseline weight (mean kg, SD)                             84.4 (14.0)          87.0 (13.0)          <0.001
      Baseline waist (mean cm, SD)                              109.9 (9.8)          110.4 (8.6)           0.005
      Waist-to-height ratio                                      66.2 (6.5)          66.4 (5.5)            0.090
      Baseline BMI (kg/m2; mean, SD)                             32.4 (4.3)          32.7 (3.4)           <0.001
      Obesity (%)                                                  66.4                 75.1              <0.001
      Smoking
                Current smoker (%)                                 13.3                 12.5               0.261
                Former smoker (%)                                  35.6                 43.4              <0.001
      Self-reported diabetes (%)                                   29.0                 27.2               0.074
      Family history of premature CHD (%)                          14.4                 16.8               0.004
      High blood cholesterol (%)                                   67.9                 69.3               0.178
      Total cholesterol (mean mg/dl, SD)                        201.8 (43.6)        202.6 (40.0)           0.375
      LDL cholesterol (mean mg/dl, SD)                          122.7 (34.4)        123.9 (34.1)           0.163
      HDL cholesterol (mean mg/dl, SD)                          49.8 (13.3)          47.8 (11.8)          <0.001
      Triglycerides (mean mg/dl, SD)                            161.7 (84.8)        170.3 (91.3)          <0.001
      Glucose (mean mg/dl, SD)                                  114.6 (32.7)        114.8 (30.7)           0.794
      Hypertension (%)                                             77.8                 83.1              <0.001
      Non-European origin (%)                                       2.9                  2.5               0.318
      Willingness to change diet (mean, SD)                      2.5 (0.7)            2.7 (0.5)           <0.001


349   Eligibility

350       Candidates for the PREDIMED-PLUS trial (Martínez-González et al, 2018) were adults aged
351   55-75 years for men and 60-75 years for women with a body mass index ≥27 and <40 kg/m2
352   who met at least three criteria for the metabolic syndrome (Alberti et al, 2009). These criteria
353   must be taken into consideration in view of evidence of the beneficial role of the
354   Mediterranean diet on metabolic syndrome (Kastorini et al, 2011, Babio et al, 2014), insulin


                                                           13

```

### DOC-003 PDF p. 15 — PLAN

[SAP source p. 15](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=15>)

```text
355   resistance and diabetes (Salas-Salvadó et al, 2014), especially when accompanied by a program
356   of physical activity for endurance (Fernández et al, 2012). Approximately, 50% of the study
357   population is made of women and diabetic participants do not exceed 27% of the total cohort.
358   Individuals who participated in the PREDIMED trial were not eligible to participate in
359   PREDIMED-PLUS.

360   Recruitment

361      Figure 2 shows the flow-chart of participants in the PREDIMED-Plus trial.




362

363       Figure 2. Flow-chart of participant recruitment and randomization in the PREDIMED-Plus
364                                                trial.

365

366      Information on follow-up will be added to this flow-chart for final analyses.


                                                      14

```

### DOC-003 PDF p. 16 — PLAN

[SAP source p. 16](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=16>)

```text
367

368   Withdrawal/follow-up

369       Follow-up will be based on:

370       -   yearly follow-up visits
371       -   yearly systematic review of medical charts
372       -   consultation of the National Death Index for participants with no information on
373           follow-up for 1 year

374       Participants will be considered to be lost-to-follow-up if there is no available information in
375   the above-mentioned sources of information for at least 2 years.

376       Participants who withdraw have several alternatives such as:
377       - no longer willing to be contacted but not reluctant to have their medical charts
378           reviewed. In this case, participants will be follow-up based on the available
379           information in their medical records
380       - explicitly asking to cancel their participation or withdraw their consent: they will be
381           considered withdrawals and their future information will no longer be accessed.

382       The number of participants in each of these categories will be included in the study flow-
383       chart. Information on losses-to-follow-up and withdrawals according to allocation group
384       will be summarized as:
385       - number of participants who were lost-to-follow-up for at least 2 years
386       - participants who asked to cancel their participation or withdrew their consent.

387

388   Baseline participants’ characteristics

389       Description of participants’ baseline characteristics will include:

390       -   Number of participants in each intervention group
391       -   Number of participants individually randomized and number of participants
392           randomized together with another person from the same household
393
394       A. Qualitative traits: summarized with number and percentages:
395             - Female sex
396             - Obesity
397             - Smoking status: never, former, current
398             - Self-reported baseline diabetes
399             - Self-reported family history of coronary heart disease
400             - Self-reported baseline high blood cholesterol
401             - Self-reported baseline hypertension
402             - Self-reported previous depression
403             - Educational level
404             - Origin: European vs. non-European
405             - Marital status
406             - Living alone
407             - Being retired
408             - Previous weight-loss dieting
409

                                                        15

```

### DOC-003 PDF p. 17 — PLAN

[SAP source p. 17](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=17>)

```text
410       B. Quantitative traits: summarized with means and standard deviations:
411             - Age
412             - Baseline weight
413             - Baseline waist circumference
414             - Baseline waist-to-height ratio
415             - Baseline body weight
416             - Total cholesterol
417             - LDL cholesterol
418             - HDL cholesterol
419             - Triglycerides
420             - Glucose
421             - Systolic blood pressure
422             - Diastolic blood pressure
423             - Leisure-time physical activity
424             - Chair test
425             - Adherence to the energy-restricted Mediterranean diet
426             - Adherence to the traditional Mediterranean diet
427             - Total energy intake
428             - Total fat intake
429             - Carbohydrate intake
430             - Protein intake
431             - Alcohol intake
432             - Dietary fiber intake
433             - Willingness to change diet



434   SECTION 6: ANALYSIS

435   Outcome definitions

436       A. Primary outcomes

437   1. Non-fatal acute coronary syndrome (acute myocardial infarction), non-fatal stroke or
438      cardiovascular mortality.

439   1.a. Acute myocardial infarction (MI) are defined according to the third universal definition of
440      MI on behalf of the Joint ESC/ACCF/AHA/WHF Task Force as evidence of myocardial
441      necrosis in a clinical setting consistent with acute myocardial ischemia.

442          Any one of the following criteria meets the diagnosis for MI:

443       • Detection of a rise and/or fall of cardiac biomarker values [preferably cardiac troponin
444        (cTn)] with at least one value above the 99th percentile upper reference limit (URL)

445           AND

446           • At least one of the following:

447                   (i)     Symptoms of ischemia.

448                   (ii)    New or presumed new significant ST-segment–T wave (ST–T) changes
449                           or new left bundle branch block.

                                                      16

```

### DOC-003 PDF p. 18 — PLAN

[SAP source p. 18](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=18>)

```text
450                  (iii)   Development of pathological Q waves in the ECG.

451                  (iv)    Imaging evidence of new loss of viable myocardium or new regional
452                          wall motion abnormality.

453                  (v)     Identification of an intracoronary thrombus by angiography.

454           Prior MI

455           Any one of the following criteria meets the diagnosis for prior MI:

456           • Pathological Q waves with or without symptoms in the absence of non-ischemic
457       causes.

458           • Imaging evidence of a region of loss of viable myocardium that is thinned and fails
459       to contract, in the absence of a non-ischemic cause.

460           • Pathological findings of a prior MI

461   1.b. Stroke is defined as an acute neurological deficit lasting more than 24 hours caused by an
462        abrupt impairment of brain function due to blockage of blood flow in a particular artery
463        supplying the brain (thrombosis or arterial embolism) or a cerebral haemorrhage.

464           Ischemic Stroke is defined following the updated definition of stroke for the 21st
465       Century: A Statement for Healthcare Professionals from the American Heart
466       Association/American Stroke Association as an episode of neurological dysfunction
467       caused by focal cerebral, spinal, or retinal infarction. Central nervous system (CNS)
468       infarction is brain, spinal cord, or retinal cell death attributable to ischemia, based on:

469          1. Pathological, imaging, or other objective evidence of cerebral, spinal cord, or
470             retinal focal ischemic injury in a defined vascular distribution;

471          2. Clinical evidence of cerebral, spinal cord, or retinal focal ischemic injury based on
472             symptoms persisting ≥24 hours or until death, and exclusion of other potential
473             causes such as hypoglycaemia or seizures.

474           Silent CNS infarction are not considered as a primary end-point if defined as imaging
475       or neuropathological evidence of CNS infarction without a history of acute neurological
476       dysfunction attributable to the lesion.

477           Hemorrhagic Stroke. Stroke caused by intracerebral hemorrhage is defined as rapidly
478       developing clinical signs of neurological dysfunction attributable to an intracerebral
479       hemorrhage, defined as a focal collection of blood within the brain parenchyma or
480       ventricular system that is not caused by trauma. Stroke caused by subarachnoid
481       hemorrhage is defined as a rapidly developing signs of neurological dysfunction and/or
482       headache because of bleeding into the subarachnoid space, which is not caused by
483       trauma.

484            Silent cerebral hemorrhage is not considered as primary end-point. It is defined as a
485       focal collection of chronic blood products within the brain parenchyma, subarachnoid
486       space, or ventricular system detected at neuroimaging or neuropathological examination
487       that is not caused by trauma and without a history of acute neurological dysfunction
488       attributable to the lesion.

                                                      17

```

### DOC-003 PDF p. 19 — PLAN

[SAP source p. 19](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=19>)

```text
489   1.c. Cardiovascular mortality: Includes sudden death and non-sudden cardiovascular death.

490             Sudden (cardiac) death is due to cessation of cardiac activity with hemodynamic
491         collapse, typically due to sustained ventricular tachycardia/ventricular fibrillation. It may
492         be:

493         — Witnessed instantaneously in a previously stable patient. This may occur with or
494         without preceding signs or symptoms, or may occur immediately following sudden
495         dyspnea, light-headedness, or palpitations.

496        — Unwitnessed. Patient found dead who at the time of last witnessed contact was in
497          his/her usual state of health without medical complaints or obvious difficulty. This
498          applies to patients dying during sleep.

499             Non-sudden cardiac death: Includes deaths of patients from acute pulmonary edema
500         with severe, progressive heart failure, cardiogenic shock, or after a recent cardiac surgical
501         procedure.

502             Non-cardiac vascular death: Includes deaths due to thromboembolic events, stroke,
503         dissecting aneurysm and peripheral artery disease.

504   2. Weight change. The study nurse records weight in duplicate at each follow-up visit. The
505      measurements are made according to the study manual of operations and with participants
506      dressed in light clothing and no shoes and accessories. The mean of the two measurements
507      will be used.

508

509        B. Secondary outcomes

510   1. Total mortality. This endpoint comprises all causes of death, including those from CVD (see
511       point 1c of primary end-point), as well as trauma, renal failure, neoplasia, sepsis, suicide
512       and death of undetermined cause. All deaths will be confirmed by reviewing the National
513       Death Index.

514   2. Changes in waist circumference. The study nurse measures waist circumference at each
515       follow-up visit according to the manual of operations.

516   3. Non-ST-segment elevation acute coronary syndrome (unstable angina): The diagnosis of
517      unstable angina is made following the definition of the ESC Guidelines for the management
518      of acute coronary syndromes in patients presenting without persistent ST-segment
519      elevation; It requires the presence of at least one of the following clinical characteristics:

520                a. Prolonged (>20 min) anginal pain at rest.

521                b. New onset (de novo) angina (Class II or III of the Classiﬁcation of the Canadian
522            Cardiovascular Society).

523               c. Recent destabilization of previously stable angina with at least Canadian
524            Cardiovascular Society Class III angina characteristics (crescendo angina).

525   4.    Coronary revascularization (percutaneous or surgical): The two main indications for
526        percutaneous or surgical revascularization are:

                                                        18

```

### DOC-003 PDF p. 20 — PLAN

[SAP source p. 20](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=20>)

```text
527            1) Patients with unstable angina or non-ST-segment elevation acute coronary syndrome.

528            2) Patients considered likely to benefit from such surgery on the basis of the location and
529               severity of chest pain, the number of vessels affected, and the presence of left
530               ventricular dysfunction.

531   5. Heart failure. Acute and chronic heart failure (HF) is a syndrome in which patients have
532      typical symptoms and signs resulting from an abnormality of cardiac structure or function.
533      The cardinal manifestations of HF are dyspnea and fatigue, which may limit exercise
534      tolerance, and fluid retention, which may lead to pulmonary and/or splanchnic congestion
535      and/or peripheral edema.

536        5.a. The diagnosis of HF with Reduced Ejection Fraction requires three conditions to be
537             satisfied: 1. Symptoms typical of HF; 2. Signs typical of HF and 3. Reduced ejection
538             fraction (< 40%)

539        5.b. The diagnosis of HF with Preserved Ejection Fraction requires four conditions to be
540             satisfied: 1. Symptoms typical of HF; 2. Signs typical of HF; 3. Normal or only mildly
541             reduced left ventricular ejection fraction and non-dilated left ventricle; and 4. Relevant
542             structural heart disease (left ventricular hypertrophy/left atrium enlargement) and/or
543             diastolic dysfunction

544        5.c. A Heart Failure event may include hospitalization or an urgent outpatient visit. In this
545             setting the event needs to meet ALL of the following criteria:

546        -        The patient exhibits documented new or worsening symptoms of HF on presentation,
547                 including at least ONE of the following: Dyspnea, decreased exercise tolerance, fatigue
548                 or other symptoms of worsened end-organ perfusion or volume overload.

549            -    The patient has objective evidence of new or worsening HF, consisting of at least TWO
550                 physical examination findings OR one physical examination finding and at least ONE
551                 laboratory criterion), including: Physical examination findings considered to be due to
552                 heart failure, including new or worsened peripheral edema, increasing abdominal
553                 distention or ascites (in the absence of primary hepatic disease),
554                 rales/crackles/crepitations at pulmonary auscultation, increased jugular venous
555                 pressure and/or hepatojugular reflux, S3 gallop, and clinically significant or rapid
556                 weight gain thought to be related to fluid retention

557                - Laboratory evidence of new or worsening HF, if obtained within 24 hours of
558                  presentation, including: Increased B-type natriuretic peptide (BNP)/ N-terminal pro-
559                  BNP (NT-proBNP) concentrations OR cardiological evidence of pulmonary congestion
560                  OR echocardiographic data of congestion or decreased cardiac output.

561                - The patient receives initiation or intensification of specific treatment for HF.

562   6.       Peripheral artery disease. Ascertainment is made according to the Inter-Society
563            Consensus for the Management of Peripheral Arterial Disease (TASC II) and ESC Guidelines
564            for the diagnosis of peripheral artery disease. For participants with intermittent
565            claudication, aged 60-69 with one cardiovascular risk factor, or aged ≥70 years and a
566            resting ankle-brachial systolic pressure index ≤0.90, or an abnormal echo-Doppler
567            examination, magnetic resonance imaging, or arteriography are considered as diagnostic
568            (confirmed case).

                                                               19

```

### DOC-003 PDF p. 21 — PLAN

[SAP source p. 21](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=21>)

```text
569   7. Venous thromboembolism (VTE): all VTE need to satisfy the standard diagnosis criteria for
570      venous thrombosis or Pulmonary (thromb-) Embolism (PE) in the general population (see
571      below 1-3). The diagnosis should be confirmed by objective imaging techniques (including
572      echography, phlebography, pulmonary computed tomography angiography (angioCTA),
573      NMR, etc.) and not only be based on the clinical suspicion.

574   Standard diagnosis criteria for VTE in clinical studies:

575   1. Deep venous thrombosis, defined as the loss of venous compressibility or the inability of
576      filling the deep vein intraluminal segment at the lower/upper limbs, as detected by
577      echography with venous compression or phlebography, respectively.

578   • The presence of thrombus at the distal lower limb (distal from the popliteal vein) qualifies
579     for primary VTE only if it is asymptomatic.

580   • All proximal thrombus qualify for final primary end-point if detected by imaging techniques
581     (echography or radiology), regardless of whether it is or not asymptomatic.

582   2. Pulmonary Embolism (PE) is defined as:

583   Contrast pulmonary arteriography:

584   • Defects in intraluminal filling, as contrasted with two projections.

585   • Sudden stoppage of the contrast in one or several vessels with a diameter greater than 2.5
586     mm

587   • Pulmonary scintigraphy based on ventilation/perfusion (V/Q):

588   o A V/Q-pulmonary scintigraphy with high probability of PE in patients with no low clinical
589     probability of PE.

590   • Pulmonary angiography using computed tomography:

591   o Defects in filling sub-segmental or more proximal vessels

592   3. Fatal PE is defined as:

593   • Death exclusively caused by PE and/or its confirmation at autopsy or using radiology
594     techniques

595   Important considerations:

596   a) Superficial venous thrombophlebitis should not be described as VTE.

597   b) It is highly recommended to describe VTE according to the anatomic position:

598   • Lower limbs

599   • Upper limbs

600   • Pulmonary embolism

601   • Others: vessels at the splanchnic level, cerebral veins, etc.

                                                         20

```

### DOC-003 PDF p. 22 — PLAN

[SAP source p. 22](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=22>)

```text
602   c) The description of the VTE is highly convenient (for instance, distal to popliteal vein vs.
603      proximal VTE; sub-segmental level vs. central PE)

604   d) VTE associated with a central catheter (for instance, deep venous thrombosis at the upper
605      limbs) should be reported separately.

606   e) Incidental VTE should be differenced from any other symptomatic events.

607   8. Atrial fibrillation (AF): AF is defined following the Guidelines of the American College of
608      Cardiology Foundation/American Heart Association Task Force on Practice Guidelines
609      together with the European Society of Cardiology, the European Heart Rhythm Association,
610      and the Heart Rhythm Society, as a cardiac arrhythmia with the following characteristics:

611          (1) The surface ECG shows ‘absolutely’ irregular RR intervals, i.e., RR intervals that do
612      not follow a repetitive pattern.

613          (2) There are no distinct P waves on the surface ECG. Some apparently regular atrial
614      electrical activity may be seen in some EKG leads, most often in lead V1.

615          (3) The atrial cycle length (when visible), i.e., the interval between two atrial
616      activations, is usually variable and <200 ms (>300 bpm).

617

618   9. Type 2-diabetes. New-Onset Type 2 Diabetes cases are diagnosed following the
619      recommendations of the American Diabetes Association:

620      1. HbA1C ≥6.5%. This test should be performed in a laboratory using a method that is
621         National Glycohemoglobin Standardization Program (NGSP) certified and standardized
622         to the DCCT assay. OR

623      2. Fasting plasma glucose (FPG) ≥126 mg/dL (7.0 mmol/L). Fasting is defined as no caloric
624         intake for at least 8 hours OR

625      3. Two-hour plasma glucose (PG) ≥ 200 mg/dL (11.1 mmol/L) during an oral glucose
626         tolerance test (OGTT). This test should be performed as described by the WHO, using a
627         glucose load containing the equivalent of 75 g anhydrous glucose dissolved in water OR

628      4. In a patient with classic symptoms of hyperglycemia or hyperglycemic crisis, a random
629          plasma glucose ≥200 mg/dL (11.1 mmol/L).

630          In the absence of unequivocal hyperglycemia, results should be confirmed by repeat
631      testing according to the guidelines of the American Diabetes Association.

632   10. Type-2 diabetes complications. Participants are assessed yearly for microvascular
633      complications of diabetes:

634      1. Diabetic nephropathy: Kidney disease in diabetes is defined based on the alteration of
635         glomerular filtration rate (GFR) and /or the presence of persistent albuminuria at levels
636         of 30 mg/24 h or more (normal albumin excretion is currently defined as < 30 mg/24 h).
637         GFR is estimated through a quantitative formula, the CKD-Epi equation, that measures
638         the progression of kidney involvement. Persistent albuminuria is determined by the
639         urine albumin to creatinine ratio (normal <30 mg albumin/g creatinine) in a routine

                                                      21

```

### DOC-003 PDF p. 23 — PLAN

[SAP source p. 23](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=23>)

```text
640          morning urine sample. Because of variability in urinary albumin excretion, two of three
641          morning specimens collected within a 3- to 6-month period should be abnormal before
642          considering a patient to have developed increased urinary albumin excretion or a
643          progression of albuminuria. The presence of one or two of the above criteria indicates
644          renal disease in these patients and the requirement for appropriate follow-up for
645          progression of renal disease according to the guidelines of the American Diabetes
646          Association.

647      2. Diabetic retinopathy: Diagnosed by ophthalmologic examination and/or treatment with
648         laser photocoagulation according to the guidelines of the American Diabetes
649         Association.

650      3. Diabetic polyneuropathy: Diagnosed by clinical symptoms, neurological examination and
651         results of electrophysiological studies of peripheral nerves according to the guidelines of
652         the American Diabetes Association.

653          *Kidney damage defined as abnormalities in urine, blood, or imaging tests.

654   11. Cancer. All cancers except non-melanoma skin cancer are considered. Cancer cases are
655      coded according to the International Classification of Diseases (ICD 10) of the World Health
656      Organization.

657   12. Dementia/Alzheimer’s disease. Cases are ascertained according to the Recommendations
658       from the National Institute on Aging and the Alzheimer´s Association workgroup
659       (McKhann et al, , 2011) or if a diagnosis of dementia is reported by a neurologist.

660   13. Other dementias: Cases are ascertained according to McKhann et al, 2011 criteria (see
661       below) or if a diagnosis of dementia is reported by a neurologist.

662   Dementia is diagnosed when there are cognitive or behavioral (neuropsychiatric) symptoms
663      that: 1. Interfere with the ability to function at work or at usual activities; and 2.
664      Represent a decline from previous levels of cognitive functioning; and 3. Are not
665      explained by delirium or major psychiatric disorder; 4. Cognitive impairment is detected
666      and diagnosed through a combination of (1) history-taking from the patient and a
667      knowledgeable informant and (2) an objective cognitive assessment; 5. The cognitive or
668      behavioral impairment involves a minimum of two cognitive domains.

669   14. Parkinson’s disease. Cases are ascertained according to the diagnostic criteria described
670       by Hughes et al (1992) or if reported by a neurologist.

671   15. Unipolar depression. The diagnosis must be made according to the DSM-V criteria. In this,
672       definition major depression, persistent depression, and other depressions included in
673       Depressive Disorders (DSM V) are accepted. Diagnosis of depression made by primary
674       care physicians or psychiatrist in participants treated with antidepressant drugs for more
675       than 6 moths is accepted. If this is the case, ICD 10 (International Statistical Classification
676       of Diseases and Related Health Problems, 10th version) diagnosis of depressive episodes
677       are also accepted. For physicians and psychiatrists not using ICD 10 or DSM V, a positive
678       response to the two questions included in the NICE clinical guidelines is recommended
679       (https://www.nice.org.uk).

680   16. Osteoporotic fractures. Low-energy fracture is defined as the fracture produced by a
681       same-level fall. Fractures are identified from X-rays reports obtained from at least two


                                                        22

```

### DOC-003 PDF p. 24 — PLAN

[SAP source p. 24](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=24>)

```text
682        radiological reports. High trauma fractures, potentially pathological fractures (e.g., cancer
683        or Paget’s disease), or fractures of the head, fingers and toes are not considered.

684   17. Gallstone disease or cholecystectomy: Gallstone disease is diagnosed according to the
685       findings obtained by imaging techniques including abdominal ultrasonography, computed
686       tomography or magnetic resonance imaging. Diagnosis of cholecystectomy require the
687       corresponding surgical report.

688   18. Symptomatic gout: Defined following the criteria of the American College of Rheumatology.
689        Typically, the disease first presents as arthritis that is acute and episodic, but can be
690        recurrent. Gout can also present as chronic arthritis of one or more joints. This clinical
691        picture is built on a foundation of an excess body burden of uric acid, manifested in part
692        by hyperuricemia, which is defined as serum uric acid levels greater than 7.0 mg/dL.

693   19. Transient Ischemic Attack: The diagnosis must be made according to the Scientific
694       Statement of the American Heart Association/American Stroke Association Stroke Council:
695       a transient episode of neurological dysfunction caused by focal brain, spinal cord, or
696       retinal ischemia, without acute infarction demonstrated by neuroimaging, preferably
697       magnetic resonance imaging techniques.

698   20. Cataract surgery: Defined by a medical report of cataract surgery.

699   21. Surgery for obesity: Defined by a medical report of bariatric surgery.

700

701       C. Intermediate markers

702       Changes in nutrient intake and dietary patterns will be determined by changes in the 17-
703   item score of adherence to the energy-restricted Mediterranean diet (intensive intervention
704   group) or the 14-item score (control group) and by changes in food and nutrient intake
705   determined by the 143-item food frequency questionnaire administered during follow-up.

706        Changes in systolic and diastolic blood pressure, serum lipid concentrations, fasting
707   glucose levels, renal function, uric acid, hemoglobin A1C, C-reactive protein, and liver function
708   are evaluated yearly for the duration of the intervention.

709        Yearly, are also evaluated the percentage of participants in each group requiring anti-
710   hypertensive, anti-diabetic or lipid-lowering medication, results of ECGs, cognitive function,
711   quality of life, and psychological and neuropsychological questionnaire scores.

712

713   Analysis methods

714       Analysis methods

715       For primary and secondary outcomes –except for changes in weight and waist
716   circumference– Cox regression models will be used for assessing the association between the
717   intervention and the outcome. Time-at-risk will be given by the time between the baseline visit
718   (in which the participants learn about their allocation group) and the date the outcome
719   happened. For those participants who are right censored, follow-up will finish at the last
720   available date of follow-up (last visit or last date in medical records, whichever occur later). For

                                                        23

```

### DOC-003 PDF p. 25 — PLAN

[SAP source p. 25](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=25>)

```text
721   participants with follow-up longer that the closing date of the database, the closing date of the
722   database will be considered as censoring date. Also, for fatal outcomes, date of death will be
723   considered as end of follow-up.

724       For changes in weight, we will used multilevel, mixed-effects linear regression models with
725   repeated measurements with a random intercept and taking into consideration the intra-
726   cluster correlation of members of the same household. We will assess within group changes as
727   well as between group changes during follow-up. The center will be included as a random
728   factor.

729        Also, for weight changes, we will define a weight loss of 5% as clinically meaningful
730   (Williamson et al, 2015). Baseline body weight in the PREDIMED-Plus trial was 86.5 kg, thus a 5%
731   loss is 4.3 kg. Two landmark trials of lifestyle interventions in high-risk population groups (with
732   high BMI and impaired glucose tolerance, like many participants in the PREDIMED-Plus trial)
733   achieved average weight losses of 3–6 kg, translating into highly significant reductions in
734   diabetes risk (Tuomilehto et al, 2001, Knowler et al, 2002). Similar 58% reduction in diabetes
735   risk were observed in both RCTs.

736        As an ancillary analysis to changes in weight, we will assess changes in BMI with BMI as a
737   continuous trait with multilevel, mixed-effects linear regression models with repeated
738   measurements with a random intercept and taking into consideration the intra-cluster
739   correlation of members of the same household. We will assess within group changes as well as
740   between group changes during follow-up. Also, we will consider a 5% loss in BMI as a clinically
741   meaningful change. Baseline BMI in the PREDIMED-Plus cohort was 32.5 kg/m2 hence a 5% loss
742   is 1.6 kg/m2. In a previous large prospective study (Feldman et al, 2017), among participants
743   with baseline BMI 30-34.9 kg/m2, moderate loss (−3.0 to −7.0%) resulted in an OR for diabetes
744   of 0.38 (95% CI, 0.19- 0.79). Therefore, 5% loss in BMI is definitively a change of a sufficient
745   size as to be clinically meaningful.

746       Finally, for waist circumference changes, we will use multilevel, mixed-effects linear
747   regression models with repeated measurements with a random intercept and taking into
748   consideration the intra-cluster correlation of members of the same household and the center
749   as another random factor. We will assess within group changes as well as between group
750   changes during follow-up. As for weight and BMI change, a 5% reduction in waist
751   circumference will be considered as clinically meaningful. Baseline waist circumference was
752   108 cm in the PREDIMED-Plus cohort and a 5% reduction is 5.4 cm. In the cited Finnish study
753   (Tuomilehto et al, 2001) the lifestyle intervention that reduced diabetes risk by 58% resulted in
754   a mean 4.4 cm reduction in waist circumference.

755       Adjustment for covariates

756       Main analyses will be crude analyses based on intention-to-treat approaches. Robust
757   variance estimators will consider the intra-cluster correlation of members of the same
758   household and Cox regression models will be stratified by center.

759       For the combined outcome, additional analyses will be stratified according to recruitment
760   center and adjusted for sex, age, educational level, smoking status, baseline hypertension,
761   baseline dyslipidemia, baseline type 2 diabetes, family history of coronary heart disease, body-
762   mass index, waist-to-height ratio and baseline physical activity (METS-min/d, as derived from
763   the self-reported physical activity questionnaire).

764       When assessing changes in weight as an outcome, models will be also adjusted for
765   recruitment center, sex, age, educational level, smoking status, baseline hypertension,

                                                       24

```

### DOC-003 PDF p. 26 — PLAN

[SAP source p. 26](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=26>)

```text
766   baseline dyslipidemia, baseline diabetes, family history of coronary heart disease, and baseline
767   physical activity.

768       Secondary outcomes may include some further specific confounders.

769       Methods used for assumptions to be checked for statistical methods

770       Proportionality of the hazards will be assessed with Schoenfeld’s residual test and testing
771   time-varying-covariates.

772       Alternative methods to be used if distributional assumptions do not hold

773       If hazards are not proportional, we will reassess the proportionality assumption by
774   including some potential confounders as strata. If hazards remain non-proportional, we will
775   describe the effect of the intervention separately for different follow-up periods.

776       Planned sensitivity analyses for the outcomes

777       Main analyses will be based on an intention-to-treat approach with completers only. As
778   sensitivity analysis, the intention-to-treat approach will be repeated with multiple imputation
779   for missing outcomes (see below).

780       Also, per-protocol analyses will be done for the primary outcome.

781       Planned subgroup analyses

782       Subgroup analyses will be done by sex, age (median age as cut-off point), educational level
783   (2 categories), baseline diabetes, number of criteria for the metabolic syndrome (3 vs. >=4),
784   smoking, body-mass index (obese and non-obese), and baseline score of adherence to the
785   energy-reduced Mediterranean diet.

786

787   Missing data

788       Multivariate imputation will be done with chained equations (STATA “mi” command),
789   generating 20 imputations for each missing measurement from regression equations to predict
790   missing outcomes among participants lost for 2 years or longer. The imputation models
791   included as predictors will be sex, age, smoking, leisure-time physical activity, baseline BMI,
792   baseline weight, prevalent diabetes, prevalent hypertension, prevalent hypercholesterolemia,
793   family history of coronary heart disease, intervention group, being 2nd member of the same
794   household and educational level.

795

796   Additional analyses

797      For the per-protocol analysis, causal inference methods will be used (inverse probability
798   weighting, G-formula) (Estruch et al, 2018).

799      Let Aj be 1 if the participant adheres to the intervention, and 0 otherwise (from the
800   moment on when he/she do no longer adhere to it). The per-protocol effect is the effect of Aj,
801   and can be estimated using the same approach as the intention-to-treat effect with one

                                                      25

```

### DOC-003 PDF p. 27 — PLAN

[SAP source p. 27](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=27>)

```text
802   important difference: individuals are artificially censored at the end of the interval when they
803   deviate from the study protocol because they stopped adhering to the intervention, i.e., when
804   Aj=0.

805        Of course, to determine whether participants adhere during given year, they must provide
806   information on adherence at the subsequent follow-up visit, and for that, they must attend the
807   follow-up visit in the first place. Therefore, there are 3 different censoring mechanisms in this
808   per-protocol analysis of interval studies:

809        1) Incomplete follow-up. This type of censoring arises when individuals do not attend a
810   visit (with a pre-specified period of 12 months). Let Cj be an indicator of censoring by
811   incomplete follow-up at month j.

812       2) Insufficient information to determine adherence among those who attend a visit. Let Nj
813   be an indicator for attending a visit at time j (1: yes, 0: no). Among those with Nj=1, we define
814   the censoring indicator Rj (1: yes, 0: no) for missing information on Aj.

815       3) No adherence. Among those with Nj=1 and Rj=0, participants are censored if Aj=0

816       Censoring by any of the above mechanisms may introduce bias. We will estimate inverse
817   probability weights to adjust for the potential selection bias (Hernán, 2013; Hernán, in press)
818   under the assumption that loss to follow-up, data collection, and adherence were effectively
819   randomized at each time point given the measured pre- and post-randomization prognostic
820   factors. Information on the specific methods that should be used to estimate the probabilities,
821   to compute the stabilized weights, and to fit the models, together with an example, can be
822   found in Estruch et al, 2018, Supplemental appendix, pages 36-38.
823

824   Harms

825       Information on adverse effects (headache, fatigue, constipation and increased bowel
826   rhythm) is collected at 6 months and yearly thereafter. This information will be described as
827   percentage across intervention groups in the report of the primary outcome.

828

829   References

830       Alberti KG, Eckel RH, Grundy SM, Zimmet PZ, Cleeman JI, Donato KA, et al, Harmonizing
831   the metabolic syndrome: a joint interim statement of the International Diabetes Federation
832   Task Force on Epidemiology and Prevention; National Heart, Lung, and Blood Institute;
833   American Heart Association; World Heart Federation; International Atherosclerosis Society;
834   and International Association for the Study of Obesity. Circulation. 2009;120(16):1640-5.

835      Babio N, Toledo E, Estruch R, Ros E, Martínez-González MA, Castañer O, et al,
836   Mediterranean diets and metabolic syndrome status in the PREDIMED randomized trial. CMAJ.
837   2014;186(17):E649-57.

838       Cholesterol Treatment Trialists’ (CTT) Collaboration. Efficacy and safety of more intensive
839   lowering of LDL cholesterol: a meta-analysis of data from 170,000 participants in 26
840   randomised trials. Lancet. 2010;376:1670-81



                                                       26

```

### DOC-003 PDF p. 28 — PLAN

[SAP source p. 28](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=28>)

```text
841       Estruch R, Ros E, Salas-Salvadó J, Covas MI, Corella D, Arós F, et al, Primary prevention of
842   cardiovascular disease with a Mediterranean diet. N Engl J Med. 2018 Jun 21;378(25):e34.

843        Fernández JM, Rosado-Álvarez D, Da Silva Grigoletto ME, Rangel-Zúñiga OA, Landaeta-Díaz
844   LL, Caballero-Villarraso J, López-Miranda J, Pérez-Jiménez F, Fuentes-Jiménez F. Moderate-to-
845   high-intensity training and a hypocaloric Mediterranean diet enhance endothelial progenitor
846   cells and fitness in subjects with the metabolic syndrome. Clin Sci (Lond). 2012;123(6):361-73.

847       Feldman AL, Griffin SJ, Ahern AL, Long GH, Weinehall L, Fhärm E, Norberg M, Wennberg P.
848   Impact of weight maintenance and loss on diabetes risk and burden: a population-based study
849   in 33,184 participants. BMC Public Health. 2017;17(1):170.

850       González-Muniesa P, Martínez-González MA, Hu FB, Després JP, Matsuzawa Y, Loos RJF, et
851   al, Obesity. Nat Rev Dis 2017; 3:17034.

852       Gordon DJ, Probstfield JL, Garrison RJ, et al, High-density lipoprotein cholesterol and
853   cardiovascular disease. Four prospective American studies. Circulation. 1989;79:8–15.

854       Hernán MA, Hernández-Díaz S, Robins JM. Randomized trials analyzed as observational
855   studies. Ann Intern Med 2013;159:560-2.

856       Hernán MA, Robins JM. Causal inference. Boca Raton, FL: Chapman & Hall/CRC (in press).

857        Hughes AJ, Ben-Shlomo Y, Daniel SE, Lees AJ. What features improve the accuracy of
858   clinical diagnosis in Parkinson's disease: a clinicopathologic study. Neurology 1992;42:1142-6.
859   Erratum in: Neurology 1992;42(7):1436.

860       Kastorini CM, Milionis HJ, Esposito K, Giugliano D, Goudevenos JA, Panagiotakos DB. The
861   effect of Mediterranean diet on metabolic syndrome and its components: a meta-analysis of
862   50 studies and 534,906 individuals. J Am Coll Cardiol. 2011;57(11):1299-313.

863        Knowler WC, Barrett-Connor E, Fowler SE, Hamman RF, Lachin JM, Walker EA, Nathan DM,
864   Diabetes Prevention Program Research G. Reduction in the incidence of type 2 diabetes with
865   lifestyle intervention or metformin. N Engl J Med. 2002;346(6):393–403.

866      Lange T, Hansen J V. Direct and Indirect Effects in a Survival Context. Epidemiology.
867   2011;22(4):575-581.

868       Lin S-H, Young JG, Logan R, VanderWeele TJ. Mediation analysis for a survival outcome
869   with time-varying exposures, mediators, and confounders. Stat Med. 2017;36(26):4153-4166.

870       Look AHEAD Research Group, Wing RR. Long-term effects of a lifestyle intervention on
871   weight and cardiovascular risk factors in individuals with type 2 diabetes mellitus: four-year
872   results of the Look AHEAD trial. Arch Intern Med. 2010;170(17):1566-75.

873       Martínez-González MA, Corella D, Salas-Salvadó J, Ros E, Covas MI, Fiol M, et al, Cohort
874   profile: design and methods of the PREDIMED study. Int J Epidemiol 2012; 41:377-85.

875       Martínez-González MA, Buil-Cosiales P, Corella D, Bulló M, Fitó M, Vioque J, et al, Cohort
876   Profile: Design and methods of the PREDIMED-Plus randomized trial. Int J Epidemiol. 2018 Nov
877   22. doi: 10.1093/ije/dyy225. [Epub ahead of print]




                                                      27

```

### DOC-003 PDF p. 29 — PLAN

[SAP source p. 29](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=29>)

```text
878        McKhann GM, Knopman DS, Chertkow H, Hyman BT, Jack CR Jr, Kawas CH, et al. The
879   diagnosis of dementia due to Alzheimer's disease: recommendations from the National
880   Institute on Aging-Alzheimer's Association workgroups on diagnostic guidelines for Alzheimer's
881   disease. Alzheimers Dement. 2011;7(3):263-9.

882       Miller M, Stone NJ, Ballantyne C, Bittner V, Criqui MH, Ginsberg HN, et al. Triglycerides and
883   cardiovascular disease: a scientific statement from the American Heart Association. Circulation.
884   2011;123(20):2292-333.

885      Nordestgaard BG,       Varbo    A.   Triglycerides   and   cardiovascular   disease. Lancet.
886   2014;384:626–35.

887      O'Brien PC, Fleming TR. A multiple testing procedure for clinical trials. Biometrics.
888   1979;35(3):549-56.

889       Sacks FM, Bray GA, Carey VJ, Smith SR, Ryan DH, Anton SD, McManus K, Champagne CM,
890   Bishop LM, Laranjo N, Leboff MS, Rood JC, de Jonge L, Greenway FL, Loria CM, Obarzanek E,
891   Williamson DA. Comparison of weight-loss diets with different compositions of fat, protein,
892   and carbohydrates. N Engl J Med. 2009;360(9):859-73.

893       Salas-Salvadó J, Bulló M, Estruch R, Ros E, Covas MI, Ibarrola-Jurado N, Corella D, Arós F,
894   Gómez-Gracia E, Ruiz-Gutiérrez V, Romaguera D, Lapetra J, Lamuela-Raventós RM, Serra-
895   Majem L, Pintó X, Basora J, Muñoz MA, Sorlí JV, Martínez-González MA. Prevention of diabetes
896   with Mediterranean diets: a subgroup analysis of a randomized trial. Ann Intern Med.
897   2014;160(1):1-10.

898       Schröder H, Fitó M, Estruch R, Martínez-González MA, Corella D, Salas-Salvadó J, et al, A
899   short screener is valid for assessing Mediterranean diet adherence among older Spanish men
900   and women. J Nutr 2011;141(6):1140-5.

901      Schulz KF, Grimes DA. Multiplicity in randomised trials II: subgroup and interim analyses.
902   Lancet 2005;365(9471):1657-61.

903       Schwarzfuchs D, Golan R, Shai I. Four-year follow-up after two-year dietary interventions.
904   N Engl J Med 2012; 367:1373-4.

905       Shai I, Schwarzfuchs D, Henkin Y, Shahar DR, Witkow S, Greenberg I, et al, Weight loss
906   with a low-carbohydrate, Mediterranean, or low-fat diet. N Engl J Med 2008; 359:229-41.

907      Stamler J. Blood pressure and high blood pressure. Aspects of risk. Hypertension 1991;18(3
908   Suppl):I95-107.

909       Stamler R. Implications of the INTERSALT study. Hypertension 1991;17(1Suppl):I16–20.

910      The GBD 2015 Obesity Collaborators. Health effects of overweight and obesity in 195
911   countries over 25 years. N Engl J Med 2017; 377:13-27.

912      Thompson WA Jr. On the treatment of grouped observations in life studies. Biometrics
913   1977;33:463-70.

914       Tuomilehto J, Lindström J, Eriksson JG, Valle TT, Hämäläinen H, Ilanne-Parikka P, Keinänen-
915   Kiukaanniemi S, Laakso M, Louheranta A, Rastas M, Salminen V, Uusitupa M; Finnish Diabetes



                                                       28

```

### DOC-003 PDF p. 30 — PLAN

[SAP source p. 30](<../../../joi190106supp2_prod_1635377898.49605.pdf#page=30>)

```text
916   Prevention Study Group. Prevention of type 2 diabetes mellitus by changes in lifestyle among
917   subjects with impaired glucose tolerance. N Engl J Med. 2001;344(18):1343-50.

918        Williamson DA, Bray GA, Ryan DH. Is 5% weight loss a satisfactory criterion to define
919   clinically significant weight loss? Obesity (Silver Spring). 2015;23(12):2319-20.

920

921




                                                    29

```

### DOC-004 PDF p. 1 — REPORT

[Results source p. 1](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=1>)

```text
                                              Supplementary Online Content

Sayón-Orea C, Razquin C, Bulló M, et al. Effect of a nutritional and behavioral intervention on energy-reduced Mediterranean diet
adherence among patients with metabolic syndrome [published October 15, 2019]. JAMA. doi:10.1001/jama.2019.14630

Supplement 3. eTable 1. Definitions of scores capturing the four dietary patterns.
eTable 2. Baseline dietary variables and their changes by randomized treatment group: Foods and foods groups.
eTable 3. Sensitivity analysis. Baseline, 6-month and 12-month changes in quality dietary scores by randomized treatment group:
completers only.
eTable 4. Sensitivity analysis. Baseline, 6-month and 12-month changes in food items by randomized treatment group: completers
only.
eTable 5. Sensitivity analysis. Baseline values, 6-month and 12-month changes in nutrient intake by randomized treatment group:
completers only
eTable 6. Sensitivity analysis. Baseline and 6- and 12- month changes in quality dietary scores by randomized treatment group: All
randomized participants. Replacing all missing values with baseline value.
eTable 7. Sensitivity analysis. Baseline values, 6-month and 12- month changes in food items by randomized treatment group: all
randomized participants. Replacing all missing values with baseline value
eTable 8. Sensitivity analysis. Baseline values, 6-month and 12-month changes in nutrient intake by randomized treatment group:
all randomized participants. Replacing all missing values with baseline value.
eTable 9. Baseline and 12- month change (95% confidence intervals) in risk factors, by treatment group: all randomized 245
participants (multiple imputation [MI]) and completers only.
eFigure 1. Mean values (95% CI) of scores capturing the 4 quality dietary patterns at baseline, at 6 months and at 12 months
according to the randomized treatment group.
eFigure 2. Percentage of participants complying with the intended dietary changes by randomized treatment group
eFigure 3 Changes in nutritional variables (expressed in common units of baseline standard deviations) after 6 and 12 months in
the control and in the intervention group.

This supplementary material has been provided by the authors to give readers additional information about their work.




                                      © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 2 — REPORT

[Results source p. 2](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=2>)

```text
Supplemental eTable 1. Definitions of scores capturing the four dietary patterns.

                         17-item Energy-reduced Mediterranean Diet              Mediterranean           Mediterranean Diet Adherence            Prime Diet Quality Score
                         (er-MedDiet, 0-17 points)                              Diet Score (MDS,        Screener (MEDAS, 0-14 points)           (PDQS, 0-42 points)
                                                                                0 to 9 points),
                                                                                Trichopoulou
 Positively weighted     Olive oil as main culinary fat                         MUFA:SFAa               Olive oil as main culinary fat          Dark leafy green vegetablesc
 components              ≥ 2 servings/d vegetables                              Vegetablesa             ≥ 4 tbs/d olive oil                     Cruciferous vegetablesc
                         ≥ 3 servings/d fruits                                  Fruits and nutsa        ≥ 2 servings/d vegetables               Carrotsc
                         ≥ 3 servings/wk legumes                                Legumesa                ≥ 3 servings/d fruits                   Other vegetablesc
                         ≥ 3 servings/wk fish                                   Fish a                  ≥ 3 servings/wk legumes                 Whole citrus fruitsc
                         ≥ 3 servings/wk nuts                                   Cerealsa                ≥ 3 servings/wk fish                    Other whole fruitsc
                         Preference of poultry (chicken, turkey, or rabbit)                             ≥ 3 servings/wk nuts                    Legumesc
                           over red meats (beef, pork, lamb, hamburgers,                                Preference of poultry (chicken,         Nutsc
                           or sausages)                                                                 turkey, or rabbit) > red meats (beef,   Poultryc
                                                                                                                                                Fishc
                         ≥ 2 servings/wk olive oil sauce with tomato,                                   pork, hamburgers, or sausages)
                                                                                                                                                Eggsc
                           garlic, onion, or leek (sofrito)                                             ≥ 2 servings/wk olive oil sauce
                                                                                                                                                Whole grainsc
                         ≥5 servings/wk of whole grain cereals                                          with tomato, garlic, onion, or leek
                                                                                                                                                Liquid vegetable oilsc
                                                                                                        (sofrito)
 Negatively weighted       <1 servings/wk red or processed meats               Meat and meat                                              Red meatd
                                                                                                        <1 serving/d red or processed meats
                                                                                       b
 components                <1 servings/wk butter or margarine or cream         products                                                   Potatoesd
                                                                                                        <1 serving/d butter or margarine or
                                                                                             b
                           <1 servings/wk carbonated sugar-sweetened           Dairy products      cream                                  Processed meatd
                           beverages                                                               <1 serving/d carbonated sugar-         Whole fat dairyd
                           <3 servings/wk commercial bakery, cakes,                                sweetened beverages                    Refined grains & baked goodsd
                           biscuits, or pastries                                                   <2 servings/wk commercial bakery,      Sugar sweetened beveragesd
                           Avoidance of any added sugar to beverages                               cakes, biscuits, or pastries           Fried foods obtained away
                           ≤ 1 serving/d of white bread                                                                                   from homed
                           < 3 servings/wk of refined grain, pasta or white                                                               Sugary desserts and ice creamd
                           rice
  Alcohol                   2-3 glasses/d for men                              5-25 g/d (women)     ≥7 glasses/wk of wine
                            1-2 glasses/d for women                            10-50 g/d (men)
a
  One point if the consumption was ≥ the sex specific median
b
  One point if the consumption was ≤ the sex specific median
c
  0 points if the consumption was between 0–1 serving/wk; 1 point if the consumption was between 2–3 servings/wk and 2 points if the consumption was ≥4 servings/week.
d
  0 points if the consumption was ≥4 servings/week; 1 point if the consumption was between 2–3 servings/wk and 2 points if the consumption was between 0–1 serving/week.




                                                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 3 — REPORT

[Results source p. 3](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=3>)

```text
Supplemental eTable 2. Baseline dietary variables and their changes by
randomized treatment group: Foods and foods groups.

                                    MULTIPLE IMPUTATION: ALL RANDOMIZED
                                                PARTICIPANTS
 Food and food groups           Intervention group            Intervention                  Between-group
                                                                 group                        difference
                                      N=3,272                   N=3,311                                  p value
 Olive oil (g/week)
  Baseline, median (IQR)           350 (175, 350)            350 (175, 350)
  6-month change                    28 (23 to 33)             32 (28 to 37)             -4 (-11 to 2)     0.20
  12-month change                   36 (31 to 41)             44 (39 to 49)             -8 (-15 to -2)    0.02
 Refined olive oil (g/week)
  Baseline, median (IQR)              0 (0, 70)                 0 (0, 70)
  6-month change                   -38 (-41 to -34)         -34 (-38 to -31)             -3 (-8 to 1)     0.17
  12-month change                  -39 (-42 to -35)         -39 (-42 to -35)             0 (-5 to 5)      0.93
 Extra-virgin olive oil
 (g/week)
   Baseline, median (IQR)           175 (70, 350)            175 (70, 350)
  6-month change                    65 (59 to 70)             66 (61 to 71)              -1 (-9 to 6)     0.71
  12-month change                   75 (69 to 80)             83 (77 to 88)             -8 (-16 to -1)    0.04
 Nuts (g/week)
  Baseline, median (IQR)            60 (28, 165)              60 (14, 165)
  6-month change                  120 (114 to 126)            72 (66 to 77)             49 (41 to 57)    <0.001
  12-month change                 117 (111 to 123)            82 (76 to 87)             35 (27 to 43)    <0.001
 Fruits (g/week)
  Baseline, median (IQR)        2,287 (1,523, 3,200)      2,287 (1,494,
                                                          3,281)
  6-month change                  344 (287 to 401)         158 (104 to 213)             186 (107 to      <0.001
                                                                                           265)
  12-month change                 430 (370 to 491)          233 (177 to 289)            197 (118 to      <0.001
                                                                                           276)
 Vegetables (g/week)
  Baseline, median (IQR)        2,168 (1,621, 2,814)      2,130 (1,596,
                                                          2,863)
  6-month change                  330 (292 to 368)         142 (106 to 178)             188 (135 to      <0.001
                                                                                           241)
  12-month change                 347 (306 to 389)          137 (100 to 175)            210 (157 to      <0.001
                                                                                           263)
 Cereals (g/week)
  Baseline, median (IQR)          877 (627, 1432)           870 (645, 1432)
  6-month change                 -165 (-186 to -143)        -75 (-95 to -55)         -89 (-119 to -      <0.001
                                                                                          60)
  12-month change                -205 (-227 to -183)        -99 (-120 to -79)       -106 (-135 to -      <0.001
                                                                                          77)
 Whole grains (g/week)
  Baseline, median (IQR)            109 (0, 525)               98 (0, 525)
  6-month change                  274 (254 to 293)            61 (42 to 79)             213 (186 to      <0.001
                                                                                           240)
  12-month change                 228 (207 to 248)            59 (40 to 78)             169 (142 to      <0.001
                                                                                           196)




                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 4 — REPORT

[Results source p. 4](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=4>)

```text
 Refined grains (g/week)
   Baseline, median (IQR)         779 (425, 1475)           779 (412, 1474)
   6-month change                -538 (-562 to -515)      -192 (-214 to -170)       -346 (-378 to -   <0.001
                                                                                         314)
   12-month change               -535 (-559 to -510)      -226 (-249 to -203)       -309 (-340 to -   <0.001
                                                                                         277)

IQR, Interquartile range, Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 5 — REPORT

[Results source p. 5](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=5>)

```text
Supplemental eTable 2 (cont). Baseline dietary variables and their changes by
randomized treatment group. Foods and food groups.

                                MULTIPLE IMPUTATION: ALL RANDOMIZED
                                            PARTICIPANTS
 Food and food groups          Intervention           Control group           Between-group difference
                                  group
                                 N=3,272                  N=3,311                               p value
 Legumes (g/week)
   Baseline, median            120 (88, 180)           120 (88, 176)
 (IQR)
   6-month change              37 (34 to 41)            17 (14 to 21)         20 (15 to 25)     <0.001
  12-month change              39 (36 to 43)            18 (15 to 22)         21 (16 to 26)     <0.001
 Fish (g/week)
   Baseline, median           673 (472, 918)           682 (475, 918)
 (IQR)
   6-month change             101 (88 to 114)           41 (29 to 53)         59 (42 to 77)     <0.001
  12-month change             105 (91 to 119)           29 (17 to 42)         75 (58 to 93)     <0.001
 Meat (g/week)
   Baseline, median          993 (760, 1263)          994 (776, 1271)
 (IQR)
   6-month change           -109 (-123 to -95)        -78 (-92 to -65)       -31 (-50 to -11)   0.002
  12-month change           -116 (-130 to -101)      -107 (-120 to -93)       -9 (-28 to 10)     0.37
 Red meat (g/week)
   Baseline, median           290 (150, 497)           300 (150, 520)
 (IQR)
   6-month change           -115 (-123 to -106)       -67 (-75 to -59)       -48 (-59 to -36)   <0.001
  12-month change           -120 (-129 to -111)       -81 (-89 to -72)       -39 (-51 to -28)   <0.001
 Processed meat
 (g/week)
   Baseline, median           227 (143, 317)           227 (143, 322)
 (IQR)
   6-month change             -63 (-68 to -57)        -45 (-50 to -39)       -18 (-26 to -10)   <0.001
  12-month change             -63 (-69 to -57)        -52 (-57 to -46)        -11 (-19 to -3)   0.007
 Pastries (g/week)
   Baseline, median            121 (42, 275)           114 (42, 261)
 (IQR)
   6-month change           -109 (-116 to -102)       -49 (-56 to -42)       -60 (-69 to -50)   <0.001
  12-month change           -109 (-116 to -102)       -60 (-67 to -53)       -49 (-59 to -39)   <0.001
 Dairy (g/week)
   Baseline, median         2100 (1532, 2959)        2200 (1548, 3597)
 (IQR)
   6-month change              16 (-34 to 66)        -137 (-184 to -90)      153 (84 to 222)    <0.001
  12-month change             -41 (-95 to 12)          -190 (-239 to -       149 (80 to 218)    <0.001
                                                            141)
 Total yogurt (g/week)
   Baseline, median            375 (58, 875)           375 (58, 875)
 (IQR)
   6-month change             119 (97 to 141)           9 (-11 to 30)        110 (80 to 140)    <0.001
  12-month change             88 (64 to 111)            -4 (-25 to 17)        92 (62 to 122)    <0.001




                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 6 — REPORT

[Results source p. 6](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=6>)

```text
 Fermented dairy
 (g/week)
   Baseline, median           550 (300, 975)          575 (300, 1025)
 (IQR)
   6-month change             97 (74 to 120)            -5 (-27 to 16)       102 (71 to 134)   <0.001
   12-month change             72 (47 to 96)            -16 (-38 to 7)        87 (56 to 119)   <0.001

IQR, Interquartile range. Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 7 — REPORT

[Results source p. 7](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=7>)

```text
Supplemental eTable 2 (cont). Baseline dietary variables and their changes by
randomized treatment group. Foods and food groups.

                                 MULTIPLE IMPUTATION: ALL RANDOMIZED
                                             PARTICIPANTS
 Food and food groups      Intervention             Control group             Between-group difference
                           group
                                N=3,272                  N=3,311                               p value
 Low-fat dairy (g/week)
   Baseline, median           658 (0, 1,775)          687 (0, 1,775)
 (IQR)
   6-month change            326 (279 to 373)         68 (23 to 113)       258 (193 to 323)      <0.001
   12-month change           267 (217 to 318)          -4 (-50 to 42)      271 (206 to 336)      <0.001
 Whole-fat dairy
 (g/week)
   Baseline, median              0 (0, 375)              0 (0, 375)
 (IQR)
   6-month change           -174 (-196 to -151)     -110 (-132 to -88)      -63 (-95 to -32)     <0.001
   12-month change          -160 (-184 to -135)     -101 (-123 to -78)      -59 (-91 to -27)     <0.001
 Total alcohol intake
 (g/week)
   Baseline, median              32 (5, 98)             36 (5, 103)
 (IQR)
   6-month change             -13 (-16 to -10)          -6 (-9 to -3)         -7 (-11 to -3)      0.001
   12-month change            -12 (-15 to -9)           -4 (-7 to -1)         -8 (-12 to -3)     <0.001
 Red wine (g/week)
   Baseline, median              33 (0, 29)              4 (0, 29)
 (IQR)
   6-month change                1 (-1 to 3)             2 (0 to 4)            -1 (-4 to 1)       0.36
   12-month change               2 (0 to 4)              3 (1 to 5)            -1 (-4 to 1)       0.37

IQR, Interquartile range
Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                          © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 8 — REPORT

[Results source p. 8](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=8>)

```text
© 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 9 — REPORT

[Results source p. 9](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=9>)

```text
Supplemental eTable 3. Sensitivity analysis. Baseline, 6-month and 12-month
changes in quality dietary scores by randomized treatment group: completers
only.

                                                               COMPLETERS ONLY
 Variable                                 Intervention            Control group               Between-group
                                          group                                                 difference
                                            n=2,862 (6 mo)         n=2,883 (6 mo)                         p value
                                           n=2,833 (12 mo)          n=2,943 (12
                                                                        mo)
 17-item er-MedDiet (0 to 17)*
    Baseline, mean (SD)                         8.5 (2.6)              8.6 (2.7)
    6-month change                          4.1 (4.0 to 4.2)       1.8 (1.7 to 1.9)       2.3 (2.2 to 2.5)   <0.001
    12-month change                         4.3 (4.2 to 4.4)       2.0 (1.9 to 2.1)       2.3 (2.1 to 2.4)   <0.001
 MDS (Trichopolou 0 to 9)
    Baseline, mean (SD)                         4.3 (1.7)              4.3 (1.6)
    6-month change                          0.2 (0.1 to 0.2)        -0.3 (-0.4 to -       0.5 (0.4 to 0.6)   <0.001
                                                                         0.3)
    12-month change                         0.2 (0.1 to 0.2)        -0.3 (-0.4 to -       0.5 (0.4 to 0.6)   <0.001
                                                                         0.3)
 MEDAS (0 to 14)
    Baseline, mean (SD)                         7.6 (1.9)              7.6 (1.9)
    6-month change                          2.5 (2.5 to 2.6)       1.4 (1.3 to 1.5)       1.1 (1.0 to 1.3)   <0.001
    12-month change                         2.7 (2.7 to 2.8)       1.6 (1.6 to 1.7)       1.1 (1.0 to 1.2)   <0.001
 PDQS (0 to 42)
    Baseline, mean (SD)                        21.0 (3.7)             21.0 (3.7)
    6-month change                          4.6 (4.5 to 4.8)       2.3 (2.1 to 2.4)       2.4 (2.2 to 2.6)   <0.001
    12-month change                         4.7 (4.5 to 4.8)       2.4 (2.3 to 2.5)       2.3 (2.1 to 2.5)   <0.001

Baseline data are means (SD). 6-month and 12-month change are means (95% CI) calculated using mixed effect
models incorporating site and intra-cluster correlations (couples) as random factors.
er-MedDiet, Energy reduced Mediterranean Diet; MDS, Mediterranean Diet Score, MEDAS, Mediterranean Diet
Adherence Screener; PDQS, Prime Diet Quality Score. The direction of all 4 food patterns is the same: a higher score
means a higher quality of the overall dietary pattern. The possible ranges were 0-17 for er-MedDiet, 0-9 for the MDS,
0-14 for MEDAS, and 0-42 for PDQS.

The minimum clinically important difference (MCID) can be considered 1 point for the MDS, because a 2 point
increment (roughly corresponding to one standard deviation) was associated in the fully adjusted model with a 25%
relative reduction in all-cause mortality (Trichopoulou et al. N Engl J Med 2003;348:2599-608, Table 4), coefficient
= log(0.75) = -0.2877. Therefore, 1 point in the MDS (corresponding to 0.5 SD) will lead to a 13% relative risk
reduction corresponding to a hazard ratio of 0.87, namely exp(-0.2877/2) = 0.87, which can be considered higher than
a minimal clinically significant effect from the subjective point of view of a patient.

For the MEDAS, in the PREDIMED trial, assessed as an observational study, and controlling for potential
confounding, 1-point increment was associated with a 10% reduction in the risk of the composite primary
cardiovascular end-point (multivariable-adjusted hazard ratio= 0.90, 95% CI, 0.85-0.96) and with a 6% reduction in
total mortality (multivariable-adjusted hazard ratio= 0.94, 95% CI, 0.89-0.99) (unpublished data). Therefore, 1 point
should represent a sufficiently important difference for an individual patient.

The 17-item er-MedDiet score basically captures the 14-items of MEDAS with some additions (sufficiently explained
in our main manuscript) that have been repeatedly associated with benefits in previous observational studies with
good control for confounding. Therefore, a 1-point difference can be also accepted as a minimum clinically important
difference.

For the PDQS (range 0 to 42, SD=3.7), the minimum clinically important difference will represent probably a 2-point
increment, given its wider range.




                              © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 10 — REPORT

[Results source p. 10](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=10>)

```text
*The number of participants included in this analysis was: for the intervention group at 6 months n=3,030 and at 12
months n=2,971 and for the control group at 6 months n=3,090 and at 12 months n=3,095




Supplemental eTable 4. Sensitivity analysis. Baseline, 6-month and 12-month
changes in food items by randomized treatment group: completers only.


                                                         COMPLETERS ONLY
 Variable                       Intervention group          Control group           Between-group difference
                                  n=2,862 (6 mo)           n=2,883 (6 mo)                                     p
                                  n=2,833 (12 mo)          n=2,943 (12 mo)                                  value
 Total olive oil (g/week)
   Baseline, mean (SD)             350 (175, 350)            350 (175, 350)
   6-month change                   26 (22 to 31)             29 (25 to 34)               -3 (-10 to 3)      0.34
   12-month change                  34 (30 to 39)             42 (38 to 47)               -8 (-15 to -1)     0.02
 Refined olive oil
 (g/week)
   Baseline, median                   0 (0, 70)                 0 (0, 70)
   (IQR)
   6-month change                  -37 (-41 to -33)         -34 (-38 to -31)               -3 (-8 to 3)      0.32
   12-month change                 -39 (-43 to -35)         -39 (-43 to -35)               0 (-6 to 5)       0.95
 Extra virgin olive oil
 (g/week)
   Baseline, median                 175 (70, 350)            175 (70, 350)
   (IQR)
   6-month change                   63 (57 to 68)             63 (58 to 69)                0 (-8 to 7)       0.90
   12-month change                  73 (68 to 79)             81 (76 to 87)               -8 (-16 to 0)      0.05
 Nuts (g/week)
   Baseline, median                 60 (28, 165)              60 (14, 165)
   (IQR)
   6-month change                 120 (115 to 126)            71 (65 to 76)               50 (42 to 57)     <0.00
                                                                                                              1
   12-month change                117 (111 to 123)            82 (77 to 88)               35 (27 to 43)     <0.00
                                                                                                              1
 Fruits (g/week)
   Baseline, median              2287 (1523, 3200)        2287 (1494, 3281)
   (IQR)
   6-month change                 349 (292 to 406)         165 (108 to 222)          184 (104 to 265)       <0.00
                                                                                                              1
   12-month change                435 (379 to 491)         244 (188 to 299)          192 (113 to 270)       <0.00
                                                                                                              1
 Vegetables (g/week)
   Baseline, median              2173 (1640, 2811)        2135 (1607, 2886)
   (IQR)
   6-month change                 330 (291 to 368)          136 (98 to 174)          193 (139 to 247)       <0.00
                                                                                                              1
   12-month change                350 (311 to 388)         141 (103 to 179)          209 (155 to 263)       <0.00
                                                                                                              1
 Cereals (g/week)
   Baseline, median               885 (641, 1432)           877 (645, 1432)
   (IQR)




                              © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 11 — REPORT

[Results source p. 11](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=11>)

```text
   6-month change           -172 (-194 to -151)       -80 (-102 to -59)         -92 (-122 to -61)    <0.00
                                                                                                       1
   12-month change          -212 (-233 to -190)       -106 (-127 to -84)       -106 (-136 to -75)    <0.00
                                                                                                       1

IQR, Interquartile range
Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




Supplemental eTable 4 cont. Sensitivity analysis. Baseline, 6-month and 12-month
changes in food items by randomized treatment group: completers only.

                                                         COMPLETERS ONLY
 Variable                  Intervention group          Control group                   Between-group difference
                             n=2,862 (6 mo)           n=2,883 (6 mo)                                     p value
                             n=2,833 (12 mo)          n=2,943 (12 mo)
 Whole grains (g/week)
   Baseline, median            109 (0, 525)              98 (0, 525)
   (IQR)
   6-month change            277 (257 to 296)           61 (42 to 81)           215 (188 to 242)         <0.001
   12-month change           231 (211 to 250)           61 (42 to 80)           170 (143 to 197)         <0.001
 Refined grains
 (g/week)
   Baseline, median          779 (425, 1475)           779 (412, 1474)
   (IQR)
   6-month change           -544 (-568 to -519)      -198 (-222 to -174)      -346 (-380 to -311)        <0.001
   12-month change          -539 (-563 to -514)      -227 (-252 to -203)      -311 (-346 to -277)        <0.001
 Legumes (g/week)
   Baseline, median           120 (88, 180)             120 (88, 176)
   (IQR)
   6-month change              38 (35 to 42)            18 (14 to 21)                20 (16 to 25)       <0.001
   12-month change             40 (37 to 43)            19 (16 to 23)                21 (16 to 25)       <0.001
 Fish (g/week)
   Baseline, median           673 (472, 918)           682 (475, 918)
   (IQR)
   6-month change            101 (88 to 113)            40 (28 to 53)                60 (43 to 78)       <0.001
   12-month change           104 (91 to 117)            31 (18 to 44)                73 (55 to 91)       <0.001
 Meat (g/week)
   Baseline, median          993 (760, 1263)           994 (776, 1271)
   (IQR)
   6-month change           -110 (-123 to -96)         -81 (-94 to -67)         -29 (-48 to -10)          0.003
   12-month change          -118 (-133 to -104)       -107 (-121 to -93)         -11 (-31 to 9)              0.27
 Red meat (g/week)
   Baseline, median           290 (150, 497)           300 (150, 520)
   (IQR)
   6-month change           -114 (-122 to -106)        -67 (-75 to -59)         -47 (-59 to -35)         <0.001
   12-month change          -120 (-129 to -112)        -80 (-89 to -71)         -40 (-53 to -28)         <0.001
 Processed meat
 (g/week)



                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 12 — REPORT

[Results source p. 12](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=12>)

```text
   Baseline, median              227 (143, 317)           227 (143, 322)
   (IQR)
   6-month change               -63 (-69 to -57)          -45 (-51 to -39)          -18 (-26 to -9)          <0.001
   12-month change              -64 (-70 to -58)          -52 (-58 to -46)          -11 (-20 to -3)           0.01
 Pastries (g/week)
   Baseline, median              121 (42, 275)             114 (42, 261)
   (IQR)
   6-month change             -109 (-116 to -101)         -49 (-57 to -42)         -59 (-70 to -49)          <0.001
   12-month change            -109 (-116 to -101)         -60 (-67 to -52)         -49 (-60 to -39)          <0.001

IQR, Interquartile range
Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.



Supplemental eTable 4 cont. Sensitivity analysis. Baseline and 6- and 12- month
changes in food items by randomized treatment group: completers only.

                                                             COMPLETERS ONLY
 Variable                        Intervention              Control group                   Between-group difference
                                     group
                                n=2,862 (6 mo)            n=2,883 (6 mo)                                    p value
                                n=2,833 (12 mo)           n=2,943 (12 mo)
 Dairy (g/week)
   Baseline, median (IQR)         2,100 (1,532,         2,200 (1,548, 3,597)
                                      2,959)
   6-month change                 17 (-33 to 67)          -143 (-192 to -93)        159 (89 to 230)          <0.001
   12-month change                -39 (-88 to 11)        -186 (-235 to -137)        148 (78 to 218)          <0.001
 Total yogurt (g/week)
   Baseline, median (IQR)         375 (58, 875)             375 (58, 875)
   6-month change                119 (98 to 140)             6 (-15 to 27)          113 (83 to 143)          <0.001
   12-month change                87 (66 to 109)            -4 (-25 to 17)              91 (61 to 121)       <0.001
 Fermented dairy
 (g/week)
   Baseline, median (IQR)        550 (300, 975)           575 (300, 1,025)
   6-month change                 97 (75 to 119)            -9 (-31 to 14)          105 (74 to 137)          <0.001
   12-month change                72 (49 to 94)             -15 (-37 to 7)              86 (55 to 118)       <0.001
 Low-fat dairy (g/week)
   Baseline, median (IQR)         658 (0, 1,775)            687 (0, 1,775)
   6-month change               327 (280 to 373)            62 (15 to 108)          265 (199 to 331)         <0.001
   12-month change              270 (223 to 317)            -1 (-47 to 45)          271 (206 to 337)         <0.001
 Whole-fat dairy
 (g/week)
   Baseline, median (IQR)           0 (0, 375)                0 (0, 375)
   6-month change              -173 (-197 to -149)        -111 (-135 to -87)        -61 (-95 to -27)         0.001
   12-month change             -159 (-183 to -134)        -99 (-124 to -75)         -59 (-94 to -25)         0.001
 Total alcohol intake
 (g/week)
   Baseline, median (IQR)           32 (5, 98)               36 (5, 103)




                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 13 — REPORT

[Results source p. 13](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=13>)

```text
   6-month change                -13 (-16 to -10)            -6 (-9 to -3)              -7 (-11 to -3)   <0.001
   12-month change                -12 (-15 to -9)            -4 (-7 to -1)              -8 (-12 to -3)   <0.001
 Red wine (g/week)
   Baseline, median (IQR)            4 (0, 29)                 4 (0, 29)
   6-month change                   1 (-1 to 3)               2 (0 to 4)                 -1 (-4 to 2)     0.38
   12-month change                  2 (0 to 4)                3 (1 to 5)                 -1 (-4 to 2)     0.40


IQR, Interquartile range
Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 14 — REPORT

[Results source p. 14](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=14>)

```text
Supplemental eTable 5. Sensitivity analysis. Baseline values, 6-month and 12-
month changes in nutrient intake by randomized treatment group: completers
only.

                                                            COMPLETERS ONLY
 Variable                      Intervention group         Control group                 Between-group difference
                                 n=2,862 (6 mo)          n=2,883 (6 mo)                                  p value
                                 n=2,833 (12 mo)         n=2,943 (12 mo)
 Total energy Intake
 (kcal/d)
   Baseline, mean (SD)              2,355 (544)             2,369 (555)
   6-month change               -173 (-192 to -154)       -78 (-97 to -59)       -95 (-122 to -68)        <0.001
   12-month change              -176 (-196 to -157)        -74(-93to -54)       -103 (-130to -75)         <0.001
 Total protein (%E)
   Baseline, mean (SD)               16.8 (2.8)              16.8 (2.8)
   6-month change                 1.2 (1.1 to 1.3)         0.2 (0.1 to 0.3)          1.0 (0.9 to 1.2)     <0.001
   12-month change                1.1 (1.0 to 1.2)           0 (-.1 to .1)           1.1 (1.0 to 1.2)     <0.001
 Total carbohydrate (%E)
   Baseline, mean (SD)               40.7 (6.8)              40.4 (6.9)
   6-month change                -3.3 (-3.6 to -3.1)     -1.8 (-2.1 to -1.6)    -1.5 (-1.9 to -1.2)       <0.001
   12-month change               -3.7 (-3.9 to -3.4)     -2.3 (-2.5 to -2.0)    -1.4 (-1.8 to -1.1)       <0.001
 Total fat (%E)
   Baseline, mean (SD)               39.5 (6.6)              39.7 (6.5)
   6-month change                 2.5 (2.2 to 2.7)         1.8 (1.5 to 2.0)          0.7 (0.3 to 1.0)     <0.001
   12-month change                2.9 (2.6 to 3.1)         2.3 (2.1 to 2.6)          0.5 (0.2 to 0.9)     0.004
 SFA (%E)
   Baseline, mean (SD)                9.9 (2.0)              10.0 (2.0)
   6-month change                -1.0 (-1.1 to -0.9)     -0.6 (-0.6 to -0.5)    -0.4 (-0.6 to -0.3)       <0.001
   12-month change               -0.9 (-1.0 to -0.9)     -0.6 (-0.7 to -0.5)    -0.4 (-0.5 to -0.3)       <0.001
 MUFA (%E)
   Baseline, mean (SD)               20.5 (4.7)              20.6 (4.6)
   6-month change                 3.5 (3.3 to 3.7)         2.3 (2.1 to 2.5)          1.2 (0.9 to 1.4)     <0.001
   12-month change                3.9 (3.7 to 4.1)         3.0 (2.8 to 3.2)          0.9 (0.6 to 1.2)     <0.001

Baseline data are means (SD)
E, energy; SFA, saturated fatty acids; MUFA, monounsaturated fatty acids
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 15 — REPORT

[Results source p. 15](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=15>)

```text
Supplemental eTable 5 cont. Sensitivity analysis. Baseline values, 6-month and 12-
month changes in nutrient intake by randomized treatment group: completers
only.

                                                               COMPLETERS ONLY
 Variable                              Intervention            Control group               Between-group difference
                                           group
                                      n=2,862 (6 mo)          n=2,883 (6 mo)                                p value
                                      n=2,833 (12 mo)         n=2,943 (12 mo)
 Ratio MUFA:SFA
   Baseline, mean (SD)                     2.1 (0.5)               2.1 (0.5)
   6-month change                      0.6 (0.6 to 0.7)        0.4 (0.4 to 0.4)         0.3 (0.2 to 0.3)    <0.001
   12-month change                     0.7 (0.6 to 0.7)        0.5 (0.4 to 0.5)         0.2 (0.2 to 0.2)    <0.001
 PUFA (%E)
   Baseline, mean (SD)                     6.4 (1.9)               6.4 (1.8)
   6-month change                      1.3 (1.2 to 1.4)        0.8 (0.7 to 0.8)         0.5 (0.4 to 0.6)    <0.001
   12-month change                     1.3 (1.2 to 1.3)        0.8 (0.8 to 0.9)         0.4 (0.3 to 0.5)    <0.001
 Total alcohol (%E)
   Baseline, median (IQR)                   1 (0, 4)               2 (0, 4)
   6-month change                     -0.3 (-0.4 to -0.2)      -0.1 (-0.2 to 0)         -0.2 (-0.4 to 0)     0.02
   12-month change                    -0.3 (-0.4 to -0.1)       0 (-0.1 to 0.1)          -0.3 (-0.4 to -     0.01
                                                                                              0.1)
 Fiber (g/week)
   Baseline, mean (SD)                     184 (63)                182 (60)
   6-month change                       40 (37 to 42)           16 (14 to 19)            24 (20 to 27)      <0.001
   12-month change                      37 (35 to 40)           18 (16 to 21)            19 (16 to 22)      <0.001
 Long chain w-3 fatty acids
 (g/week)
   Baseline, median (IQR)                   5 (4, 9)               5 (4, 9)
   6-month change                      1.1 (0.9 to 1.2)        0.4 (0.3 to 0.6)         0.7 (0.5 to 0.8)    <0.001
   12-month change                     1.1 (1.0 to 1.2)        0.4 (0.3 to 0.6)         0.7 (0.5 to 0.9)    <0.001
 Cholesterol (mg/week)
   Baseline, mean (SD)                   2,651 (793)             2,682 (794)
   6-month change                    -222 (-250 to -194)       -169 (-197 to -          -53 (-93 to -13)    0.009
                                                                    141)
   12-month change                   -218 (-247 to -189)       -206 (-235 to -          -12 (-52 to 29)      0.58
                                                                    178)
 Sodium (g/week)
   Baseline, median (IQR)             22.2 (17.9, 27.1)        22.2 (17.9, 27.4)
   6-month change                     -3.1 (-3.3 to -2.8)     -1.9 (-2.1 to -1.6)        -1.2 (-1.5 to -    <0.001
                                                                                              0.9)
   12-month change                    -3.2 (-3.5 to -3.0)     -1.9 (-2.1 to -1.6)        -1.3 (-1.7 to -    <0.001
                                                                                              1.0)

Baseline data are means (SD) or median (IQR)
E, energy; SFA, saturated fatty acids; MUFA, monounsaturated fatty acids; PUFA, polyunsaturated fatty
acids;
w-3, omega-3
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.



                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 16 — REPORT

[Results source p. 16](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=16>)

```text
Supplemental eTable 6. Sensitivity analysis. Baseline and 6- and 12- month
changes in quality dietary scores by randomized treatment group: All randomized
participants. Replacing all missing values with baseline value.

             REPLACING ALL MISSING VALUES WITH BASELINE VALUE
 Variable                       Intervention group          Control group               Between-group difference
                                       n=3,272                 n=3,311                                   p value
 17-item er-MedDiet (0 to
 17)
   Baseline, mean (SD)                 8.5 (2.6)               8.6 (2.7)
   6-month change                  3.8 (3.7 to 3.9)         1.7 (1.6 to 1.8)          2.1 (2 to 2.3)     <0.001
   12-month change                 3.9 (3.8 to 4.0)         1.9 (1.8 to 2.0)         2.0 (1.9 to 2.2)    <0.001
 MDS (Trichopolou 0 to 9)
   Baseline, mean (SD)                 4.3 (1.7)               4.3 (1.6)
   6-month change                  0.1 (0.1 to 0.2)       -0.3 (-0.4 to -0.2)        0.4 (0.3 to 0.5)    <0.001
   12-month change                 0.1 (0.1 to 0.2)       -0.3 (-0.4 to -0.3)        0.4 (0.4 to 0.5)    <0.001
 MEDAS (0 to 14)
   Baseline, mean (SD)                 7.6 (1.9)               7.6 (1.9)
   6-month change                  2.3 (2.2 to 2.3)         1.3 (1.2 to 1.3)         1.0 (0.9 to 1.1)    <0.001
   12-month change                 2.4 (2.3 to 2.5)         1.5 (1.4 to 1.6)         0.9 (0.8 to 1.0)    <0.001
 PDQS (0 to 42)
   Baseline, mean (SD)                21.0 (3.7)               21.0 (3.7)
   6-month change                  4.0 (3.9 to 4.2)         2.0 (1.8 to 2.1)         2.1 (1.9 to 2.3)    <0.001
   12-month change                 4.0 (3.9 to 4.2)         2.1 (2.0 to 2.3)         1.9 (1.7 to 2.1)    <0.001

Baseline data are means (SD)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.
er-MedDiet, Energy reduced Mediterranean Diet; MDS, Mediterranean Diet Score, MEDAS,
Mediterranean Diet Adherence Screener; PDQS, Prime Diet Quality Score




                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 17 — REPORT

[Results source p. 17](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=17>)

```text
Supplemental eTable 7. Sensitivity analysis. Baseline values, 6-month and 12-
month changes in food items by randomized treatment group: all randomized
participants. Replacing all missing values with baseline value.


            REPLACING ALL MISSING VALUES WITH BASELINE VALUE
 Variable                      Intervention group         Control group                   Between-group difference
                                      n=3,272                    n=3,311                                   p value
 Olive oil (g/week)
   Baseline, median (IQR)          350 (175, 350)            350 (175, 350)
   6-month change                   23 (18 to 27)             26 (22 to 30)               -3 (-9 to 3)      0.27
   12-month change                  30 (26 to 34)             38 (34 to 42)              -7 (-13 to -2)     0.01
 Refined olive oil
 (g/week)
   Baseline, median (IQR)             0 (0, 70)                  0 (0, 70)
   6-month change                 -32 (-35 to -29)           -31 (-34 to -28)             -1 (-5 to 4)      0.72
   12-month change                -33 (-36 to -29)           -35 (-38 to -32)             3 (-2 to 7)       0.26
 EVOO (g/week)
   Baseline, median (IQR)           175 (70, 350)             175 (70, 350)
   6-month change                   54 (49 to 59)             56 (51 to 61)               -3 (-9 to 4)      0.47
   12-month change                  63 (58 to 68)             73 (68 to 78)             -10 (-17 to -3)     0.004
 Nuts (g/week)
   Baseline, median (IQR)           60 (28, 165)               60 (14, 165)
   6-month change                 105 (100 to 110)            61 (56 to 67)              43 (36 to 51)     <0.001
   12-month change                100 (95 to 106)             73 (68 to 78)              28 (20 to 35)     <0.001
 Fruits (g/week)
   Baseline, median (IQR)       2,287 (1,523, 3,200)      2,287 (1,494,
                                                          3,281)
   6-month change                 306 (256 to 356)          144 (94 to 193)             162 (92 to 233)    <0.001
   12-month change                369 (319 to 419)          215 (166 to 265)            154 (83 to 224)    <0.001
 Vegetables (g/week)
   Baseline, median (IQR)       2,168 (1,621, 2,814)      2,130 (1,596,
                                                          2,863)
   6-month change                 287 (254 to 321)          116 (83 to 149)         171 (124 to 218)       <0.001
   12-month change                295 (261 to 328)           126 (93 to 159)        169 (121 to 216)       <0.001
 Cereals (g/week)
   Baseline, median (IQR)         877 (627, 1,432)          870 (645, 1,432)
   6-month change               -152 (-170 to -133)          -70 (-89 to -51)       -82 (-108 to -55)      <0.001
   12-month change              -183 (-202 to -165)         -87 (-106 to -68)       -96 (-123 to -70)      <0.001

IQR, Interquartile range
Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 18 — REPORT

[Results source p. 18](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=18>)

```text
Supplemental eTable 7 cont. Sensitivity analysis. Baseline, 6-month and 12-month
changes in food items by randomized treatment group: all randomized
participants. Replacing all missing values with baseline value.

            REPLACING ALL MISSING VALUES WITH BASELINE VALUE
 Variable                    Intervention group        Control group                     Between-group difference
                                    n=3,272                  n=3,311                                       p value
 Whole grains (g/week)
  Baseline, median                109 (0, 525)              98 (0, 525)
  (IQR)
  6-month change               238 (221 to 255)            54 (37 to 70)          184 (160 to 208)         <0.001
   12-month change             197 (180 to 214)            56 (39 to 73)          141 (117 to 165)         <0.001
 Refined grains (g/week)
  Baseline, median             779 (425, 1,475)          779 (412, 1,474)
  (IQR)
  6-month change              -475 (-496 to -454)      -172 (-193 to -152)      -303 (-332 to -273)        <0.001
   12-month change            -467 (-488 to -446)      -203 (-224 to -182)      -264 (-294 to -235)        <0.001
 Legumes (g/week)
  Baseline, median               120 (88, 180)            120 (88, 176)
  (IQR)
  6-month change                 33 (30 to 36)             14 (11 to 17)               19 (15 to 23)       <0.001
   12-month change               35 (32 to 38)             17 (14 to 20)               17 (13 to 22)       <0.001
 Fish (g/week)
  Baseline, median              673 (472, 918)            682 (475, 918)
  (IQR)
  6-month change                 90 (79 to 101)            35 (23 to 46)               55 (40 to 71)       <0.001
   12-month change               90 (79 to 102)            27 (16 to 38)               63 (47 to 79)       <0.001
 Meat (g/week)
  Baseline, median             993 (760, 1,263)          994 (776, 1,271)
  (IQR)
  6-month change               -95 (-107 to -83)         -70 (-82 to -58)          -25 (-42 to -8)          0.01
   12-month change             -104 (-116 to -92)        -95 (-107 to -83)             -9 (-26 to 8)        0.31
 Red meat (g/week)
  Baseline, median              290 (150, 497)            300 (150, 520)
  (IQR)
  6-month change               -99 (-106 to -92)         -59 (-66 to -51)         -40 (-51 to -30)         <0.001
   12-month change             -104 (-112 to -97)        -71 (-79 to -64)         -33 (-43 to -22)         <0.001
 Processed meat
 (g/week)
   Baseline, median             227 (143, 317)            227 (143, 322)
   (IQR)
   6-month change               -55 (-60 to -50)         -38 (-43 to -33)         -17 (-24 to -10)         <0.001
   12-month change              -55 (-60 to -50)         -47 (-52 to -42)              -9 (-16 to -1)       0.02
 Pastries (g/week)
  Baseline, median               121 (42, 275)            114 (42, 261)
  (IQR)
  6-month change               -94 (-100 to -88)         -42 (-48 to -36)         -52 (-61 to -43)         <0.001
   12-month change              -93 (-99 to -87)         -54 (-60 to -47)         -39 (-48 to -30)         <0.001




                           © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 19 — REPORT

[Results source p. 19](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=19>)

```text
IQR, Interquartile range
Baseline data are median and (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.

Supplemental eTable 7 cont. Sensitivity analysis. Baseline values, 6-month and 12-
month changes in food items by randomized treatment group: all randomized
participants. Replacing all missing values with baseline value.

             REPLACING ALL MISSING VALUES WITH BASELINE VALUE
 Variable                   Intervention             Control group                      Between-group difference
                            group
                                 n=3,272                    n=3,311                                    p value
 Dairy (g/week)
   Baseline, median            2,100 (1,532,          2,200 (1,548, 3,597)
   (IQR)                           2,959)
   6-month change              19 (-24 to 63)          -125 (-168 to -82)         144 (83 to 205)          <0.001
   12-month change             -29 (-72 to 14)        -166 (-209 to -123)         137 (76 to 198)          <0.001
 Total yogurt (g/week)
   Baseline, median            375 (58, 875)              375 (58, 875)
   (IQR)
   6-month change             103 (84 to 122)             7 (-11 to 26)               95 (69 to 122)       <0.001
   12-month change              77 (58 to 96)             -4 (-22 to 15)              81 (54 to 107)       <0.001
 Fermented dairy
 (g/week)
   Baseline, median            550 (300, 975)           575 (300, 1,025)
   (IQR)
   6-month change              83 (64 to 103)             -6 (-25 to 14)              89 (61 to 117)       <0.001
   12-month change              63 (43 to 82)             -14 (-33 to 6)              76 (49 to 104)       <0.001
 Low-fat dairy (g/week)
   Baseline, median            658 (0, 1,775)            687 (0, 1,775)
   (IQR)
   6-month change             283 (243 to 324)            56 (15 to 96)          228 (170 to 285)          <0.001
   12-month change            230 (189 to 271)            -4 (-45 to 36)         234 (177 to 292)          <0.001
 Whole-fat dairy
 (g/week)
   Baseline, median              0 (0, 375)                 0 (0, 375)
   (IQR)
   6-month change           -147 (-167 to -126)         -98 (-118 to -77)         -49 (-78 to -20)         0.001
   12-month change          -130 (-151 to -110)         -87 (-107 to -67)         -44 (-72 to -15)         0.003
 Total alcohol intake
 (g/week)
   Baseline, median              32 (5, 98)                36 (5, 103)
   (IQR)
   6-month change              -12 (-14 to -9)             -5 (-8 to -3)              -6 (-10 to -3)       0.001
   12-month change             -11 (-13 to -8)             -4 (-6 to -1)              -7 (-10 to -3)       <0.001
 Red wine (g/week)
   Baseline, median               0 (0, 29)                 0 (0, 29)
   (IQR)
   6-month change                1 (-1 to 2)                2 (0 to 3)                 -1 (-3 to 1)         0.36
   12-month change                1 (0 to 3)                2 (1 to 4)                 -1 (-3 to 1)         0.36




                          © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 20 — REPORT

[Results source p. 20](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=20>)

```text
IQR, Interquartile range
Baseline data are median (IQR)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 21 — REPORT

[Results source p. 21](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=21>)

```text
Supplemental eTable 8. Sensitivity analysis. Baseline values, 6-month and 12-
month changes in nutrient intake by randomized treatment group: all randomized
participants. Replacing all missing values with baseline value.


            REPLACING ALL MISSING VALUES WITH BASELINE VALUE
 Variable                         Intervention             Control group                Between-group difference
                                  group
                                       n=3,272                  n=3,311                                  p value
 Total energy Intake (kcal/d)
   Baseline, mean (SD)                2,355 (544)             2,369 (555)
   6-month change                 -151 (-168 to -135)       -67 (-83 to -50)     -85 (-108 to -61)       <0.001
   12-month change                -154 (-170 to -137)       -66 (-83 to -49)     -88 (-111 to -64)       <0.001
 Total protein (%E)
   Baseline, mean (SD)                 16.8 (2.8)              16.8 (2.8)
   6-month change                   1.0 (1.0 to 1.1)         0.1 (0 to 0.2)           0.9 (0.8 to 1)     <0.001
   12-month change                  0.9 (0.8 to 1.0)         0 (-0.1 to 0.1)         0.9 (0.8 to 1.1)    <0.001
 Total carbohydrate (%E)
   Baseline, mean (SD)                 40.7 (6.8)              40.4 (6.9)
   6-month change                  -2.9 (-3.1 to -2.7)       -1.6 (-1.8 to -         -1.3 (-1.6 to -1)   <0.001
                                                                  1.4)
   12-month change                 -3.2 (-3.4 to -3.0)       -2.0 (-2.2 to -     -1.2 (-1.5 to -0.9)     <0.001
                                                                  1.8)
 Total fat (%E)
   Baseline, mean (SD)                 39.5 (6.6)              39.7 (6.5)
   6-month change                   2.1 (1.9 to 2.4)        1.6 (1.4 to 1.8)         0.6 (0.3 to 0.9)    <0.001
   12-month change                  2.5 (2.3 to 2.7)        2.1 (1.8 to 2.3)         0.4 (0.1 to 0.8)     .006
 SFA (%E)
   Baseline, mean (SD)                  9.9 (2.0)                10 (2)
   6-month change                  -0.9 (-0.9 to -0.8)       -0.5 (-0.6 to -     -0.4 (-0.5 to -0.3)     <0.001
                                                                  0.4)
   12-month change                 -0.8 (-0.9 to -0.7)       -0.5 (-0.6 to -     -0.3 (-0.4 to -0.2)     <0.001
                                                                  0.5)
 MUFA (%E)
   Baseline, mean (SD)                 20.5 (4.7)              20.6 (4.6)
   6-month change                   3.0 (2.9 to 3.2)        2.0 (1.9 to 2.2)         1.0 (0.8 to 1.2)    <0.001
   12-month change                  3.4 (3.2 to 3.5)        2.6 (2.5 to 2.8)         0.7 (0.5 to 1.0)    <0.001

E, energy; SFA, saturated fatty acids; MUFA, monounsaturated fatty acids
Baseline data are means (SD)
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 22 — REPORT

[Results source p. 22](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=22>)

```text
Supplemental eTable 8 cont. Sensitivity analysis. Baseline values, 6-month and 12-
month changes in nutrient intake by randomized treatment group: all randomized
participants. Replacing all missing values with baseline value.

            REPLACING ALL MISSING VALUES WITH BASELINE VALUE
 Variable                              Intervention            Control group              Between-group difference
                                       group
                                            n=3,272                 n=3,311                                p value
 Ratio MUFA:SFA
   Baseline, mean (SD)                       2.1 (0.5)              2.1 (0.5)
   6-month change                        0.6 (0.5 to 0.6)       0.3 (0.3 to 0.4)        0.2 (0.2 to 0.3)   <0.001
   12-month change                       0.6 (0.6 to 0.6)       0.4 (0.4 to 0.4)        0.2 (0.1 to 0.2)   <0.001
 PUFA (%E)
   Baseline, mean (SD)                       6.4 (1.9)              6.4 (1.8)
   6-month change                        1.1 (1.1 to 1.2)       0.7 (0.6 to 0.7)        0.5 (0.4 to 0.5)   <0.001
   12-month change                       1.1 (1.0 to 1.2)       0.7 (0.7 to 0.8)        0.4 (0.3 to 0.5)   <0.001
 Total alcohol (%E)
   Baseline, median (IQR)                     1 (0, 4)               2 (0, 4)
   6-month change                       -0.3 (-0.4 to -0.2)      -0.1 (-0.2 to 0)       -0.2 (-0.3 to 0)    0.02
   12-month change                      -0.2 (-0.3 to -0.1)      0 (-0.1 to 0.1)        -0.2 (-0.3 to -     0.01
                                                                                             0.1)
 Fiber (g/week)
   Baseline, mean (SD)                       184 (63)               182 (60)
   6-month change                         35 (33 to 37)           14 (12 to 16)          21 (18 to 24)     <0.001
   12-month change                        32 (30 to 34)           16 (14 to 18)          16 (13 to 19)     <0.001
 Long chain w-3 fatty acids
 (g/week)
   Baseline, median (IQR)                     5 (4, 9)               5 (4, 9)
   6-month change                        0.9 (0.8 to 1.1)       0.4 (0.3 to 0.5)        0.6 (0.4 to 0.7)   <0.001
   12-month change                       0.9 (0.8 to 1.1)       0.4 (0.3 to 0.5)        0.6 (0.4 to 0.7)   <0.001
 Cholesterol (mg/week)
   Baseline, mean (SD)                     2,651 (793)            2,687 (825)
   6-month change                        -191 (-216 to -         -147 (-172 to -        -44 (-79 to -8)     0.02
                                              166)                    122)
   12-month change                       -187 (-213 to -         -182 (-207 to -        -6 (-41 to 30)      0.75
                                              162)                    157)
 Sodium (g/week)
   Baseline, median (IQR)               22.2 (17.9, 27.1)      22.2 (17.9, 27.4)
   6-month change                       -2.7 (-2.9 to -2.5)    -1.6 (-1.8 to -1.4)      -1.1 (-1.4 to -    <0.001
                                                                                             0.8)
   12-month change                      -2.8 (-3.0 to -2.6)    -1.7 (-1.9 to -1.4)      -1.1 (-1.4 to -    <0.001
                                                                                             0.8)

Baseline data are means (SD) or median (IQR)
E, energy; SFA, saturated fatty acids; MUFA, monounsaturated fatty acids; PUFA, polyunsaturated fatty
acids; w-3, omega-3
6-month and 12-month change are means (95% CI) calculated using mixed effect models taking into
account site and intra-cluster correlations (couples) as random factors.




                            © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 23 — REPORT

[Results source p. 23](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=23>)

```text
Supplemental eTable 9. Baseline and 12- month change (95% confidence intervals) in risk factors, by treatment group: all randomized
participants (multiple imputation [MI]) and completers only.

                               MULTIPLE IMPUTATION: all randomized participants                                                 COMPLETERS ONLY
 Variable                     Intervention group      Control group         Between-group difference         Intervention group       Control group        Between-group difference
                                   n=3,272               n=3,311                                 p value           n=2,840               n=2,946                                 p value
 Weight, (kg)
   Baseline, mean (SD)            86.5 (12.9)           86.3 (13.0)                                               86.5 (12.9)            86.3 (13)
   12-month change             -3.6 (-3.9 to -3.4)   -0.8 (-1.0 to -0.5)   -2.9 (-3.2 to -2.6)   <0.001        -3.8 (-4.1 to -3.6)   -0.8 (-1.0 to -0.5)   -3.1 (-3.4 to -2.7)   <0.001
 Waist, (cm)
   Baseline, mean (SD)             108 (9.6)             108 (9.7)                                                 107 (9.6)             108 (9.7)
   12-month change             -4.4 (-4.6 to -4.1)   -1.1 (-1.3 to -0.9)   -3.3 (-3.6 to -2.9)   <0.001        -4.4 (-4.7 to -4.2)   -1.1 (-1.3 to -0.9)   -3.3 (-3.7 to -3.0)   <0.001
 BMI, (kg/m2)
   Baseline, mean (SD)             32.6 (3.4)            32.6 (3.5)                                                32.5 (3.4)            32.5 (3.5)
   12-month change             -1.4 (-1.4 to -1.3)   -0.3 (-0.3 to -0.2)   -1.1 (-1.2 to -1.0)   <0.001        -1.4 (-1.5 to -1.3)   -0.3 (-0.4 to -0.2)   -1.1 (-1.3 to -1.0)   <0.001
 Serum cholesterol, (mg/dL)
   Baseline, mean (SD)            197 (37.5)            197 (37.7)                                                 196 (37)             197 (37.6)
   12-month change             -3.0 (-4.2 to -1.7)   -1.8 (-3.1 to -0.6)    -1.1 (-2.9 to 0.7)     0.23        -2.9 (-4.2 to -1.7)   -1.9 (-3.1 to -0.6)   -1.1 (-2.8 to 0.7)     0.24
 LDL-c, (mg/dL)
   Baseline, mean (SD)            121 (32.2)            121 (32.2)                                                 120 (32)             121 (32.1)
   12-month change             -2.9 (-4.0 to -1.8)   -2.3 (-3.4 to -1.2)    -0.6 (-2.2 to 1.0)     0.48        -2.9 (-4.0 to -1.8)   -2.3 (-3.4 to -1.2)   -0.6 (-2.2 to 1.0)     0.45
 HDL-c, (mg/dL)
   Baseline, mean (SD)             48 (11.8)             48 (11.7)                                                 48 (11.9)             48 (11.7)
   12-month change              2.0 (1.7 to 2.3)      0.9 (0.6 to 1.2)      1.1 (0.7 to 1.6)     <0.001         2.2 (1.8 to 2.5)      0.9 (0.6 to 1.2)      1.3 (0.8 to 1.7)     <0.001




                                                              © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 24 — REPORT

[Results source p. 24](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=24>)

```text
Supplemental eTable 9 (cont.). Baseline and 12- month change (95% confidence intervals) in risk factors, by treatment group: all
randomized participants (multiple imputation [MI]) and completers only.

                                 MULTIPLE IMPUTATION: all randomized participants                                                 COMPLETERS ONLY
 Variable                      Intervention group        Control group         Between-group difference         Intervention group        Control group         Between-group difference
                                     n=3,272                n=3,311                                  p value          n=2,840                n=2,946                                 p value
 NonHDL-c, (mg/dL)
   Baseline, mean (SD)              149 (35.1)             149 (35.1)                                                148 (34.7)             149 (34.9)
   12-month change              -4.9 (-6.0 to -3.7)     -2.9 (-4.1 to -1.7)   -1.9 (-3.6 to -0.3)     0.02        -5.2 (-6.4 to -4.0)    -2.7 (-3.9 to -1.6)   -2.5 (-4.2 to -0.8)   0.004
 Ratio Cholesterol:HDL-c
   Baseline, mean (SD)               4.3 (1.1)               4.2 (1)                                                  4.3 (1.1)               4.2 (1)
   12-month change              -0.2 (-0.3 to -0.2)     -0.1 (-0.1 to -0.1)   -0.1 (-0.2 to -0.1)    <0.001       -0.3 (-0.3 to -0.2)    -0.1 (-0.1 to -0.1)   -0.1 (-0.2 to -0.1)   <0.001
 Triglycerides, (mg/dl)
   Baseline, mean (SD)              151 (76.4)             153 (78.3)                                                148 (72.4)             150 (74.1)
   12-month change             -12.8 (-15.4 to -10.3)   -2.9 (-5.4 to -0.4)   -9.9 (-13.6 to -6.3)   <0.001     -14.6 (-17.2 to -12.1)   -4.2 (-6.7 to -1.7)   -10.4 (-14 to -6.9)   <0.001
 SBP, (mmHg)
   Baseline, mean (SD)              140 (17.1)             139 (16.6)                                                139 (17.1)             139 (16.6)
   12-month change              -4.1 (-4.7 to -3.5)     -2.2 (-2.8 to -1.7)   -1.9 (-2.7 to -1.1)    <0.001       -3.9 (-4.5 to -3.3)    -2.2 (-2.7 to -1.6)   -1.7 (-2.6 to -0.9)   <0.001
 DBP, (mmHg)
   Baseline, mean (SD)                81 (10)                81 (9.8)                                                  81 (9.9)               81 (9.7)
   12-month change              -2.4 (-2.8 to -2.1)     -1.5 (-1.8 to -1.2)    -1 (-1.4 to -0.5)     <0.001       -2.5 (-2.8 to -2.2)    -1.5 (-1.8 to -1.2)   -1.0 (-1.5 to -0.6)   <0.001

MI, Multiple imputation; BMI, Body mass index; LDL-c, Low density lipoprotein cholesterol; HDL-c, High density lipoprotein cholesterol; SBP, systolic blood pressure;
DBP, diastolic blood pressure.
Multiple imputation (using chained equations with the following predictors: Intervention group, sex, age at baseline, smoking status, educational level, physical activity,
baseline BMI, total energy intake and the baseline value of the variable that will be imputed.)
% of imputed values: body mass index: 5%, body weight: 4.7%, waist circumference: 9.4%, serum cholesterol: 10.1%, HDL-c: 10.8%, LDL-c: 10.9%, nonHDL-c: 10.9%
ratio cholesterol: HDL: 10.9%, triglycerides: 10.3%, systolic blood pressure: 6.1% and diastolic blood pressure: 6.2%
Baseline data are means (SD). 12-month change are means (95% CI) calculated using mixed effect models taking into account site and intra-cluster correlations (couples) as
random factors. Conversion factors to obtain mmol/L: Cholesterol mg/dL, HDL-c and LDL-c x 0.0259; triglycerides mg/dL x 0.0113.




                                                                 © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 25 — REPORT

[Results source p. 25](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=25>)

```text
Supplemental eFigure 1. Mean values (95% CI) of scores capturing the 4 quality
dietary patterns at baseline, at 6 months and at 12 months according to the
randomized treatment group.




Er-MedDiet, Energy reduced Mediterranean Diet; MDS, Mediterranean Diet Score, MEDAS,
Mediterranean Diet Adherence Screener; PDQS, Prime Diet Quality Score.

The direction of all 4 food patterns is the same: a higher score means a higher quality of the
overall dietary pattern. The possible ranges were 0-17 for er-MedDiet, 0-9 for the MDS, 0-14
for MEDAS, and 0-42 for PDQS, Prime Diet Quality Score.

The p values shown in the graphs correspond to the comparisons of means between intervention
and control groups.




                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 26 — REPORT

[Results source p. 26](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=26>)

```text
Supplemental eFigure 2. Percentage of participants complying with the intended dietary changes after 12 months by randomized treatment group.




                         MUFA, monounsaturated fatty acids; MUFA:SFA, ratio monounsaturated and saturated fatty acids.

               The p values shown in the graphs correspond to the comparisons of proportions between intervention and control groups.




                                                   © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 27 — REPORT

[Results source p. 27](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=27>)

```text
Supplemental eFigure 3 Changes in nutritional variables (expressed in common units of baseline
standard deviations) after 6 and 12 months in the control and in the intervention group.




CHO, carbohydrates; SFA, Saturated fatty acid; MUFA, monounsaturated fatty acid,
PUFA, polyunsaturated fatty acid; w-3, long chain omega-3 fatty acid




                         © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 28 — REPORT

[Results source p. 28](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=28>)

```text
Additional affiliations of authors:

   •   University of Navarra, Department of Preventive Medicine and Public
       Health, IDISNA, Pamplona, Spain:
              Sayón-Orea C, Razquin C, Ruiz-Canela M, Garcia-Arellano A, Toledo E,
              Martinez-Gonzalez MA.
   •   Navarra Regional Health Service, Pamplona, Spain:
              Garcia-Arellano A.
   •   Harvard TH Chan School of Public Health, Department of Nutrition, Boston,
       USA:
              Martinez-Gonzalez MA
   •   University Rovira & Virgili, Department of Biochemistry/Biotechnology,
       Nutrition Unit, Reus, Spain:
              Bullo M, Basora J, Diaz-Lopez A, Salas-Salvado J
   •   University Hospital of Sant Joan de Reus, Nutrition Unit, Reus, Spain &
       Institute of Health Investigation Pere Virgili (IISPV), Reus, Spain:
              Salas-Salvado J
   •   Department of Preventive Medicine, University of Valencia, Valencia,
       Spain:
              Corella D, Sorli JV, Asensio EM
   •   Unit of Cardiovascular Risk and Nutrition, Institute Hospital del Mar of
       Medical Research, Municipal Institute of Medical Investigation (IMIM),
       Barcelona, Spain:
              Fito M, Castañer O, Schröder H, Goday A
   •   Health Research Institute of the Balearic Islands (IdISBa), Palma de
       Mallorca, Spain:
              Romaguera D, Fiol M, Moñino M
   •   Miguel Hernandez University, ISABIAL-FISABIO, Alicante, Spain:
              Vioque J, Navarrete EM, Garcia de la Hera M
   •   Department of Cardiology (OSI) ARABA, University Hospital Araba,
       University of the Basque Country UPV/EHU, Vitoria-Gasteiz, Spain:
              Alonso-Gomez AM, Aros F, Tojal-Sierra L
   •   Department of Nursing, School of Health Sciences, Málaga, Spain:
              Wärnberg J
   •   University of Navarra, Department of Nutrition, Food Sciences, and
       Physiology, Center for Nutrition Research, Pamplona, Spain:
              Martinez JA, Zulet M
   •   Nutritional Genomics and Epigenomics Group, IMDEA Food, CEI UAM +
       CSIc Madrid, Spain:
              Martinez JA, Daimiel L
   •   Nutrition Research Group, Research Institute of Biomedical and Health
       Sciences (IUIBS), University of Las Palmas de Gran Canaria, Las Palmas
       de Gran Canaria, Spain:
              Serra-Majem L, Sanchez-Villegas A
   •   Department of Internal Medicine, IDIBAPS, Hospital Clinic, University of
       Barcelona, Barcelona, Spain:
              Estruch R, Casas R
   •   Virgen de la Victoria Hospital, Department of Endocrinology, Málaga,
       Spain:



                      © 2019 American Medical Association. All rights reserved.

```

### DOC-004 PDF p. 29 — REPORT

[Results source p. 29](<../../../joi190106supp3_prod_1635377898.49725.pdf#page=29>)

```text
           Tinahones FJ, Bernal-Lopez R
•   Biomedical Research Institute of Málaga (IBIMA). University of Málaga,
    Málaga, Spain:
           Tinahones FJ, Bernal-Lopez R, Wärnberg J
•   Department of Family Medicine, Research Unit, Primary Care District of
    Sevilla, Sevilla, Spain:
           Lapetra J, Santos-Lozano JM
•   Lipids and Vascular Risk Unit, Internal Medicine, University Hospital
    Bellvitge, Hospitalet de Llobregat, Barcelona, Spain:
           Pinto X, Corbella E
•   Research Group on Community Nutrition & Oxidative Stress, University of
    Balearic Islands, Palma de Mallorca, Spain:
           Tur JA, Bouzas C
•   Department of Internal Medicine, Maimonides Biomedical Research
    Institute of Cordoba (IMIBIC), Reina Sofia University Hospital, University
    of Cordoba, Cordoba, Spain:
           Lopez-Miranda J
•   Department of Preventive Medicine and Public Health, University of
    Granada, Granada, Spain:
           Bueno-Cavanillas A
•   Division of Preventive Medicine, Faculty of Medicine, University of Jaén,
    Jaén, Spain:
           Delgado-Rodriguez M
•   Department of Endocrinology and Nutrition, Biomedical Research Institute
    of Hospital Clínico San Carlos (IdISSC), Madrid, Spain:
           Matia-Martin P
•   Institute of Biomedicine (IBIOMED), University of León, León, Spain:
           Martin V
•   Department of Endocrinology and Nutrition, IDIBAPS, Hospital Clinic,
    University of Barcelona, Barcelona, Spain:
           Vidal J, Ros E
•   Department of Endocrinology, Foundation Jiménez-Díaz, Madrid, Spain:
           Vazquez C
•   University of Malaga, Department of Preventive Medicine, Malaga, Spain:
           Gomez-Gracia E




                  © 2019 American Medical Association. All rights reserved.

```

### DOC-005 PDF p. 1 — REPORT

[Data-sharing source p. 1](<../../../joi190106supp4_prod_1635377898.50723.pdf#page=1>)

```text
Data Sharing Statement

Data
Data available: Yes
Data types: Deidentified participant data
How to access data: There are restrictions on the availability of data
for the PREDIMED-Plus study, due to the signed consent agreements
around data sharing, which only allow access to external researchers
for research following the project purposes. Requestors wishing to
access the PREDIMED-Plus trial data used in this study can request it
to the PREDIMED-Plus trial Steering Committee:
predimed_plus_scommittee@googlegroups.com.
When available: With publication

Supporting Documents
Document types: None

Additional Information
Who can access the data: to external researchers for research
following the project purposes. Requestors wishing to access the
PREDIMED-Plus trial data used in this study can request it to the
PREDIMED-Plus trial Steering Committee:
predimed_plus_scommittee@googlegroups.com.
T ypes of analyses: Specified purpose
Mechanisms of data availability: after approval of a proposal

```

## Current-run transcription clarification

Statistical pass 1 visually confirmed DOC-003 PDF p. 7: anticipated HR is 0.70 followed by superscript reference 2, rather than decimal 0.702. The SAP-POWER semantic row and its copied checker index now state 0.70 with the citation identified. Raw source-matched transcription and every reused asset remain unchanged; this is a locator clarification, not a registered reporting issue.
