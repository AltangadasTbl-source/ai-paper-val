# PLAN evidence map: DOC-002 PDF pages 65–72

## Scope, provenance and coverage

Fresh agent mapping of the exact assigned eight physical PDF pages of `joi250116supp1_prod_1771885794.26255.pdf`. Content is prospective SAP material and therefore `PLAN`. Printed SAP pages are 3–10; physical PDF page = printed SAP page + 62. This shard does not inspect preceding pages or report sources. Main-paper matching keys below identify quantities to match and do not assert reported values or candidate findings.

All eight readable retained page images were opened and visually inspected: `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/pp065_072/page-65.png` through `page-72.png`. Also inspected `confirm-69.png` and `confirm-70.png`; these confirm the corresponding readable page images. `confirm-71.png` could not be decoded by the image viewer, but the complete readable `page-71.png` supplied coverage. Retained render engine/version and compute device are undocumented, as recorded by the curator. No new rendering, text extraction or OCR derivative was produced. Native/layout files are catalogued as glyph-corrupted or empty and were not used to transcribe scientific values. New CPU OCR was not used. The current tooling record authorizes pinned PyMuPDF 1.26.4 CPU rendering if needed, with user-requested GPU OCR context; neither was needed for this shard.

Direct-source evidence links below are relative to this artifact and use physical PDF pages. Thirty local evidence records cover all quantitative/statistical definitions and administrative units in this shard. Canonical relationship IDs are left to the coordinator.

| Physical PDF page | Printed page | Opened content | Local evidence records | Mapped status |
|---|---:|---|---|---|
| 65 | 3 | Background, study design, flow and ITT definition | P3-001, P3-002, P3-003 | COMPLETE |
| 66 | 4 | ITT withdrawal exclusion, baseline presentation, primary definition and imputation | P3-004, P3-005, P3-006, P3-007 | COMPLETE |
| 67 | 5 | Primary threshold, raw test, adjusted model, site covariate, immune secondary endpoint | P3-008, P3-009, P3-010, P3-011, P3-012 | COMPLETE |
| 68 | 6 | Survivor SOFA, 28-/90-day mortality, day-15 SOFA and imputation | P3-013, P3-014, P3-015, P3-016 | COMPLETE |
| 69 | 7 | Day-15 SOFA formula/test/survivor mean, immune reversal definition | P3-017, P3-018, P3-019, P3-020 | COMPLETE |
| 70 | 8 | Immune reversal continuation, infection resolution, safety, secondary significance, severity subgroup start | P3-021, P3-022, P3-023, P3-024, P3-025 | COMPLETE |
| 71 | 9 | Severity cutoff and subgroup analyses; antibiotic appropriateness | P3-025, P3-026, P3-027 | COMPLETE |
| 72 | 10 | Antibiotic subgroup continuation, subgroup significance, exploratory ROC, reference | P3-027, P3-028, P3-029, P3-030 | COMPLETE |

## Page 65: printed SAP page 3

### P3-001 — Trial purpose and administrative design context

- Evidence: [DOC-002 PDF p.65](../../../joi250116supp1_prod_1771885794.26255.pdf#page=65), `PLAN`, Background and Study design.
- ImmunoSep has been running since January 2021 in six European countries: Germany, Greece, Italy, Netherlands, Romania and Switzerland. Sponsor: Hellenic Institute for the Study of Sepsis. Competitive enrolment between study sites.
- Prospective multicenter randomized placebo-controlled phase 2 trial; the Study design paragraph specifies 24 study sites. Registration identifiers EudraCT 2020-005768-74 and NCT04990232. Directive 2001/20/EC appears as regulatory context.
- Intervention strategy: biomarker/laboratory-selected personalized adjunctive immunotherapy against fulminant hyper-inflammation or immunoparalysis, compared with placebo. This page does not specify doses, allocation ratio or duration.
- Matching keys: randomized placebo-controlled phase 2 design; immune-state-directed intervention. Administrative dates, site count, registration and approvals mapped, with no numerical result attached.

### P3-002 — Planned participant-flow reporting

- Evidence: [DOC-002 PDF p.65](../../../joi250116supp1_prod_1771885794.26255.pdf#page=65), `PLAN`, Study population.
- CONSORT display to report screened, inclusion/exclusion criteria, enrolled, eligible but not enrolled, reasons for non-inclusion, randomized per group, received allocated interventions, withdrew informed consent and had primary-outcome data.
- These are planned count categories, not actual participant numbers. No totals or event counts are printed.
- Matching keys: report flow diagram and primary-analysis denominators.

### P3-003 — ITT definition and comparator

- Evidence: [DOC-002 PDF p.65](../../../joi250116supp1_prod_1771885794.26255.pdf#page=65), continued on [p.66](../../../joi250116supp1_prod_1771885794.26255.pdf#page=66), `PLAN`, Study population.
- Trial analysis is based on intent-to-treat principles. ITT is defined as patients randomized to one arm of treatment.
- Comparators: personalized immunotherapy consisting of anakinra or interferon gamma versus placebo.
- Matching keys: report analysis-population definition; randomized-arm contrast.

## Page 66: printed SAP page 4

### P3-004 — Withdrawal exclusion from ITT

- Evidence: [DOC-002 PDF p.66](../../../joi250116supp1_prod_1771885794.26255.pdf#page=66), `PLAN`, opening continuation.
- Patients withdrawing informed consent after randomization are removed from ITT.
- Matching keys: ITT exclusions, consent withdrawals, randomized versus analyzed denominator. No withdrawal count is supplied here.

### P3-005 — Baseline descriptors and measurement labels

- Evidence: [DOC-002 PDF p.66](../../../joi250116supp1_prod_1771885794.26255.pdf#page=66), `PLAN`, Patient baseline demographics.
- Baseline demographics, APACHE II, Charlson Comorbidity Index (CCI), and baseline SOFA: mean and SD when normally distributed; median and quartiles for the distribution described in the source as “non-linear”. Baseline laboratory values: means and SD.
- Frequencies: infection focus, Sepsis-3 septic shock, mechanical ventilation, vasopressors, continuous renal replacement therapy (CCRT as printed), antibiotics and microbiology. Pre-enrolment serum ferritin and HLA-DR expression on CD14/CD45-positive cells also reported.
- Matching keys: baseline definitions, scale labels, mean/SD versus median/quartile format. No baseline values are printed in this shard.

### P3-006 — Primary efficacy endpoint and SOFA aggregation

- Evidence: [DOC-002 PDF p.66](../../../joi250116supp1_prod_1771885794.26255.pdf#page=66), `PLAN`, Primary study endpoint.
- Primary efficacy endpoint is comparative difference in number of patients achieving a 1.4 decrease from baseline to mean total SOFA from day 2 until day 9 after randomization.
- Mean is sum of SOFA values on days 2–9, eight values, divided by eight.
- Printed formula: `ΔSOFA score by day 9 = SOFA score of day 1 − [mean SOFA score of days 2 to 9]`.
- A positive change corresponds to reduced mean organ-dysfunction score relative to day 1. Binary threshold is completed on p.67, recorded separately in P3-008.
- Matching keys: primary SOFA response, baseline day 1, days 2–9 average, >1.4 threshold, randomized immunotherapy/placebo comparison.

### P3-007 — Primary SOFA missing-value rules

- Evidence: [DOC-002 PDF p.66](../../../joi250116supp1_prod_1771885794.26255.pdf#page=66), `PLAN`, Primary study endpoint.
- For death before day 9: replace missing SOFA values by 24, explicitly called maximum SOFA.
- For discharge home before day 9: carry forward last recorded SOFA. For loss to follow-up: carry forward last recorded SOFA.
- Rules apply before forming eight-day mean. The source does not specify an additional rule for sporadic missing values here.
- Matching keys: primary death imputation and last-observation-carried-forward handling.

## Page 67: printed SAP page 5

### P3-008 — Primary binary threshold

- Evidence: [DOC-002 PDF p.67](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67), `PLAN`, opening continuation.
- Achieving primary endpoint: ΔSOFA by day 9 **more than 1.4 points**. Not achieving: ΔSOFA equal to or less than 1.4 points.
- This is an explicit `>1.4` versus `≤1.4` split, not an inferred threshold.
- Matching keys: primary responder numerator and threshold.

### P3-009 — Primary unadjusted test and effect measure

- Evidence: [DOC-002 PDF p.67](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67), `PLAN`, raw analysis.
- Compare achievement of 1.4-point decrease in treatment group versus placebo with Fisher exact test. Calculate odds ratios and 95% confidence intervals.
- Matching keys: primary raw Fisher P value, OR and 95% CI; comparator immunotherapy versus placebo. No OR orientation formula or numerical estimate is supplied here.

### P3-010 — Primary confirmatory stepwise logistic regression

- Evidence: [DOC-002 PDF p.67](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67), `PLAN`, primary model.
- One stepwise logistic regression further confirms primary analysis. Dependent variable: achievement of primary endpoint.
- Listed independent variables: baseline APACHE II continuous; CCI continuous; SOFA score continuous; study site as a binomial variable (construction P3-011).
- ORs and 95% CIs calculated. Any two-sided P value <0.05 is considered statistically significant.
- The extracted list preserves exactly the printed covariate list; no additional variable, entry/removal threshold or interaction is inferred.
- Matching keys: adjusted primary OR, logistic model, covariate specification, two-sided alpha .05.

### P3-011 — Site covariate construction

- Evidence: [DOC-002 PDF p.67](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67), `PLAN`, fourth model bullet.
- Site binomial variable generated after analyzing enrolment frequencies in each site. Here the SAP states 31 study sites have participated; anticipated up to 8% of enrolled patients from one site.
- Sites contributing **more than 8%** of enrolled patients are pooled as “Patients coming from large sites”; all remaining patients pooled as “Patients coming from other sites”.
- Matching keys: primary regression site adjustment, data-defined >8% site grouping. Administrative site numbers remain separately recorded without a scientific comparison judgment.

### P3-012 — Secondary primary-endpoint achievement by immune state

- Evidence: [DOC-002 PDF p.67](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67), `PLAN`, Secondary endpoints, Achievement of the primary endpoint according to the state of immune activation.
- Treatment groups compared for primary achievement with Fisher exact test separately for MALS and sepsis-induced immunoparalysis.
- ORs and 95% CIs calculated according to Mantel and Haenszel. ORs for achievement in the two immune strata compared using Breslow-Day and Tarone tests.
- Prospective status: secondary endpoint section. Matching keys: MALS/immunoparalysis primary-response subgroup ORs, heterogeneity tests.

## Page 68: printed SAP page 6

### P3-013 — Secondary survivor-only SOFA, days 1–9

- Evidence: [DOC-002 PDF p.68](../../../joi250116supp1_prod_1771885794.26255.pdf#page=68), `PLAN`, opening immune-state continuation.
- Within each immune state, mean SOFA compared only for survivors until day 9 using Student t test.
- Formula enumerates SOFA days **1 through 9**, summed and divided by **9**. This is a survivor continuous mean, distinct from the primary days 2–9 binary response.
- Matching keys: survivor-only mean SOFA by immune phenotype, day 1–9 window, t test.

### P3-014 — Secondary 28-day mortality

- Evidence: [DOC-002 PDF p.68](../../../joi250116supp1_prod_1771885794.26255.pdf#page=68), `PLAN`, Impact of immunotherapy on 28-day mortality.
- Kaplan-Meier survival curves for placebo and immunotherapy; comparisons via Cox regression, reporting hazard ratios and 95% CIs.
- Subgroup analysis for MALS and sepsis-induced immunoparalysis.
- Additionally report mortality frequencies, compare with Fisher exact test, calculate ORs and 95% CIs.
- Matching keys: 28-day mortality as secondary outcome, time-to-event HR versus binary OR, immune-stratum analysis. No Cox covariates or censoring rule is specified in this paragraph.

### P3-015 — Secondary 90-day mortality

- Evidence: [DOC-002 PDF p.68](../../../joi250116supp1_prod_1771885794.26255.pdf#page=68), `PLAN`, Impact of immunotherapy on 90-day mortality.
- Kaplan-Meier survival curves and Cox regression comparisons; subgroups MALS and sepsis-induced immunoparalysis.
- Mortality frequencies also compared with Fisher exact test, calculating ORs and 95% CIs.
- This paragraph does not explicitly repeat HR/CI reporting for its Cox comparison, although P3-014 does so for 28 days. No inference about additional model specification is made.
- Matching keys: 90-day mortality as secondary outcome, survival curves/Cox analysis and binary OR, immune-stratum analysis.

### P3-016 — Secondary day-15 SOFA and missing values

- Evidence: [DOC-002 PDF p.68](../../../joi250116supp1_prod_1771885794.26255.pdf#page=68), continued on [p.69](../../../joi250116supp1_prod_1771885794.26255.pdf#page=69), `PLAN`, Change of mean total SOFA score on day 15 of the end of treatment.
- Mean SOFA days 2–15 = sum of 14 values divided by 14. Death before day 15: missing values 24. Discharge home before day 15: last SOFA carried forward. Loss to follow-up: last SOFA carried forward.
- Matching keys: secondary day 15 response, days 2–15 window, death and LOCF handling, end-of-treatment time point.

## Page 69: printed SAP page 7

### P3-017 — Secondary day-15 response formula and binary rule

- Evidence: [DOC-002 PDF p.69](../../../joi250116supp1_prod_1771885794.26255.pdf#page=69), `PLAN`, opening continuation.
- Printed formula: `ΔSOFA score by day 15 = SOFA score of day 1 − [mean SOFA score of days 2 to 15]`.
- Response: ΔSOFA by day 15 >1.4 points; non-response ≤1.4 points.
- Literal surrounding wording retained for the checker: introductory sentence refers to change “until day 9” before the formula explicitly says day 15; non-achieving category uses “primary endpoint” within this secondary endpoint paragraph. No candidate judgment is made here.
- Matching keys: day 15 secondary binary response definition and threshold.

### P3-018 — Secondary day-15 response test and subgroup analysis

- Evidence: [DOC-002 PDF p.69](../../../joi250116supp1_prod_1771885794.26255.pdf#page=69), `PLAN`, day 15 treatment comparison.
- Fisher exact test for treatment groups; ORs and 95% CIs according to Mantel and Haenszel. Also analyze separately MALS and sepsis-induced immunoparalysis.
- Matching keys: day 15 response OR, Fisher P value, Mantel-Haenszel interval, immune subgroups.

### P3-019 — Secondary survivor-only SOFA, days 1–15

- Evidence: [DOC-002 PDF p.69](../../../joi250116supp1_prod_1771885794.26255.pdf#page=69), `PLAN`, survivor mean.
- Within MALS/immunoparalysis, mean SOFA compared only for survivors until day 15 via Student t test.
- Formula lists SOFA days 1 through 15, divided by 15. Printed formula omits plus signs between days 10/11/12; the enumerated day values and denominator are retained without a candidate judgment.
- Matching keys: survivor-only continuous SOFA average, day 1–15 window, immune phenotype, t test. Distinct from days 2–15 binary secondary response.

### P3-020 — Secondary immune reversal endpoint

- Evidence: [DOC-002 PDF p.69](../../../joi250116supp1_prod_1771885794.26255.pdf#page=69), `PLAN`, Impact of personalized immunotherapy on reversal of hyper-inflammation or immunoparalysis.
- Endpoint described as censored at day 15 end of treatment.
- MALS: at least 15% decrease from baseline serum ferritin. Split by achievement by day 15; death before 15 counts as not achieving ferritin decrease. Later sentence literally says “achieving at least 15% of baseline ferritin”; the preceding definition and concluding reference to decrease are retained together.
- Sepsis-associated immunoparalysis: restoration of Quantibrite to **above 8,000 AB/C**, with serum ferritin **below 4,420 ng/ml**.
- Matching keys: secondary immune reversal, day 15, MALS ferritin reduction≥15%, immunoparalysis Quantibrite>8,000 AB/C and ferritin<4,420 ng/mL, death as failure.

## Page 70: printed SAP page 8

### P3-021 — Immune reversal continuation and analysis

- Evidence: [DOC-002 PDF p.70](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70), `PLAN`, opening continuation.
- Immunoparalysis achievement by day 15 described as Quantibrite above 8,000 AB/C; dying before day 15 counts as non-achievement. The opening continuation does not repeat the ferritin restriction on p.69.
- Treatment comparison: Fisher exact test; ORs and 95% CIs according to Mantel and Haenszel; also analyze separately MALS and sepsis-induced immunoparalysis.
- Matching keys: immune reversal frequencies, ORs/CIs, phenotype definitions, death handling.

### P3-022 — Secondary infection resolution

- Evidence: [DOC-002 PDF p.70](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70), `PLAN`, Impact of personalized immunotherapy on infection resolution.
- Endpoint censored at day 15. Binary resolved/not resolved infection for which enrolled. Infection-specific criteria referred to study protocol reference 1; no criteria are repeated in this shard.
- Fisher exact comparison; ORs and 95% CIs according to Mantel and Haenszel. Same tests separately for primary bacteremia, community-acquired pneumonia, hospital-acquired pneumonia, ventilator-associated pneumonia, and MALS/immunoparalysis strata.
- Matching keys: secondary infection resolution, day 15, baseline infection types, immune strata, OR/Fisher analysis. Death-as-failure rule not stated in this paragraph.

### P3-023 — Safety analysis

- Evidence: [DOC-002 PDF p.70](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70), `PLAN`, Safety.
- Incidence of serious and non-serious treatment-emergent adverse events (TEAEs) compared between groups in each immune stratum, MALS and sepsis-induced immunoparalysis, using Fisher exact test.
- Matching keys: safety outcome status, TEAE incidence, seriousness categories, immune-stratum denominator. No event counts, time window or exposure denominator printed here.

### P3-024 — Secondary significance rule

- Evidence: [DOC-002 PDF p.70](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70), `PLAN`, closing secondary analysis paragraph.
- All secondary endpoint analyses: any **two-sided P<0.05** considered statistically significant.
- No multiplicity adjustment or testing hierarchy is specified on this page. This is a record of the printed rule, not a judgment about analysis choice.
- Matching keys: secondary alpha/sidedness and any report multiplicity statement.

### P3-025 — Severity subgroup definition by ROC/Youden

- Evidence: [DOC-002 PDF p.70](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70), continued on [p.71](../../../joi250116supp1_prod_1771885794.26255.pdf#page=71), `PLAN`, Subgroup analyses for severity.
- APACHE II, CCI and SOFA values before study drug used to form subgroups. Cutoffs derived by plotting ROC curves discriminating 28-day mortality in the **entire ITT population**.
- From ROC coordinates estimate Youden index; use resulting cutoff to convert each severity score to a binary variable.
- Matching keys: prospective severity-subgroup selection procedure, data-derived thresholds, baseline timing, full ITT mortality 28 outcome. No numerical score cutoffs printed.

## Page 71: printed SAP page 9

### P3-026 — Severity subgroups: primary response and mortality 28/90

- Evidence: [DOC-002 PDF p.71](../../../joi250116supp1_prod_1771885794.26255.pdf#page=71), `PLAN`, three named severity subgroup outcome paragraphs.
- For **primary endpoint achievement**, **28-day mortality**, and **90-day mortality**, calculate ORs separately by baseline APACHE II, CCI and SOFA cutoffs before drug, within allocated placebo/immunotherapy groups and MALS/immunoparalysis groups as stated.
- ORs compared with Breslow-Day and Tarone tests in each of the three paragraphs.
- Matching keys: three outcomes × three severity scores, immune/treatment stratification, heterogeneity tests. No numerical ORs, CIs or cutoff values printed here.

### P3-027 — Antibiotic appropriateness subgroup

- Evidence: [DOC-002 PDF p.71](../../../joi250116supp1_prod_1771885794.26255.pdf#page=71), continued on [p.72](../../../joi250116supp1_prod_1771885794.26255.pdf#page=72), `PLAN`, Subgroup analyses for efficacy of antibiotics.
- Rationale mentions healthcare-associated infections, multidrug-resistant bacteria and empirically prescribed antibiotics.
- Appropriate empirical antibiotics: antibiotics administered at start of study drug placebo/immunotherapy to which isolated pathogen is susceptible according to antibiogram once known.
- Primary endpoint analyzed separately for those receiving appropriate versus non-appropriate antibiotics.
- Matching keys: prospective antibiotic-appropriateness primary-response subgroup, start-of-study-drug timing, microbiologic susceptibility definition. No numerical frequencies or separate test method specified in this paragraph.

## Page 72: printed SAP page 10

### P3-028 — Subgroup significance rule

- Evidence: [DOC-002 PDF p.72](../../../joi250116supp1_prod_1771885794.26255.pdf#page=72), `PLAN`, opening analysis continuation.
- All subgroup analyses: any P value **<0.05** considered statistically significant. This sentence does not explicitly repeat sidedness.
- Matching keys: subgroup alpha and any report multiplicity/sidedness statements.

### P3-029 — Exploratory ROC endpoint

- Evidence: [DOC-002 PDF p.72](../../../joi250116supp1_prod_1771885794.26255.pdf#page=72), `PLAN`, Exploratory endpoint.
- ROC comparisons for APACHE II, CCI, SOFA day 1, SOFA change by day 9, SOFA change by day 15, predicting death after 28 and 90 days.
- Analysis for total enrolled patients, placebo-allocated patients, and patients with MALS/sepsis-induced immunoparalysis as stated. Aim: define cutoff of each studied variable for future sepsis trial endpoints.
- Prospective status: **exploratory**, not primary or secondary in this SAP heading.
- Matching keys: exploratory mortality prediction ROC, baseline/day 9/day 15 predictors, populations, outcome 28/90, AUC/cutoff reporting if present in report. No AUC estimates, tests of AUC differences or cutoffs printed.

### P3-030 — Reference and shard-wide absence records

- Evidence: [DOC-002 PDF p.72](../../../joi250116supp1_prod_1771885794.26255.pdf#page=72), `PLAN`, Reference.
- Supplied reference 1 identifies Kotsaki et al., ImmunoSep international double-blind, double-dummy, placebo-controlled randomized clinical trial study protocol, BMJ Open 2022;12:e067251. Reference mapped as an administrative/source pointer; no external literature accessed.
- No tables, figures, cached workbook values or numerical trial results appear on these eight pages. The explicit SOFA formulas, thresholds, denominators, units and significance rules above cover the printed mathematical content.
- No sample-size calculation, power assumption, allocation ratio, noninferiority/equivalence margin, interim/stopping boundary, SAP version/date, or standalone sensitivity-analysis section is printed within assigned pp.65–72. Their package-wide presence/absence must be established by the other disjoint PLAN shards; this record does not infer absence elsewhere.
- End-of-treatment day 15 appears as endpoint timing. Drug doses or prescribed treatment duration are not independently specified in this shard. No PLAN version fact can be transcribed from the assigned eight pages.

## Handoff

Mapped 8/8 assigned reusable-backed pages, with 30 local evidence records P3-001 through P3-030. Fresh-required count for this shard 0. Quantitative units fully visually readable; scientific-coverage gaps 0. Derivative limitation: glyph-corrupted/empty native text; undecodable redundant confirm-71 image. Both resolved for scientific mapping by readable full-page images. No candidates diagnosed and no source, reused asset or shared coordinator artifact modified.
