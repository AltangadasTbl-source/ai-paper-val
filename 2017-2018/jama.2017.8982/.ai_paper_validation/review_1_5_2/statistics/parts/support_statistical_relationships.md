# Support Statistical Relationship Inventory Part

Fresh source mapping for DOC-002 and DOC-003. These are relationship records for the two later independent statistical passes; no candidate ID or adjudication is assigned here.

## S1001 — Cluster/factorial primary-model definition

- **Location:** DOC-002 PDF p. 13.
- **Direct observation:** 2×2 factorial trial; randomization at hospital level; GEE multiple logistic regression accounts for within-hospital clustering. Initial model includes NQI, mHealth and multiplicative interaction indicators; hospital pre-intervention prevalence and infant age at follow-up are specified covariates; individual/hospital confounders may be included.
- **Population/time/contrast/model/measure:** mothers with 2-5-month outcome surveys; intervention/control factorial contrasts; binary outcomes, logistic GEE.
- **Match key:** `GEE_logistic_primary_safe_sleep_outcomes`.
- **Required pass checks:** population/randomization level; effect-model labels; interaction decision rule; protocol versus reported main model.

## S1002 — Primary outcomes and interaction branching rule

- **Location:** DOC-002 p. 13.
- **Direct observation:** outcomes are supine position, not bed sharing, pacifier use and avoiding soft bedding. If interaction significant, interaction model describes NQI, mHealth and combined effects; if nonsignificant, a main-effects model estimates separate NQI/mHealth effects. Combined-versus-each individual intervention is two contrasts from model intervention/interaction parameters.
- **Population/time/contrast/model/measure:** four binary safe-sleep outcomes, 2-5-month follow-up. **Match key:** `protocol_primary_outcomes_interaction_rule`.
- **Required pass checks:** exact outcome label/direction; P/interaction/model consistency where final article supplies matched results.

## S1003 — Protocol multiplicity and significance definition

- **Location:** DOC-002 p. 13; also p. 14 simulation scenario.
- **Direct observation:** Bonferroni adjustment for four safe-sleep outcome intervention tests; overall 2-tailed alpha .05, comparison-wise alpha .0125.
- **Population/time/contrast/model/measure:** planned inference. **Match key:** `protocol_bonferroni_4_outcomes_alpha_0.0125`.
- **Required pass checks:** do not assume this planned adjustment is the final reported Hochberg procedure; compare only like analysis/population/decision rules.

## S1004 — Secondary mediation and breastfeeding model definitions

- **Location:** DOC-002 p. 13.
- **Direct observation:** Baron-Kenny mediation sequence: GEE linear regression for mediator, GEE logistic regression for sleep position, attenuation after mediator control. Breastfeeding outcomes: exclusive/any breastfeeding in two weeks pre-follow-up and at discharge; GEE logistic models.
- **Population/time/contrast/model/measure:** secondary planned analyses. **Match key:** `protocol_secondary_mediation_breastfeeding_GEE`.
- **Required pass checks:** only compare if a matched final result appears; no inference from absence.

## S1005 — Simulated power relationship

- **Location:** DOC-002 p. 14.
- **Direct observation:** simulated categorical-outcome GEE scenario: baseline prevalence .50-.60; each intervention +10 percentage points; both +20 points; ICC .002; Bonferroni alpha .0125; 96% power for either main effect and 80% for combined versus one intervention.
- **Population/time/contrast/model/measure:** protocol projection, not observed effect. **Match key:** `protocol_power_1600_1280_ICC_0.002`.
- **Required pass checks:** clearly separate planning power from observed P values/CIs.

## S1006 — eTable 2 respondent/nonrespondent chi-square tests

- **Location:** DOC-003 pp. 3-4.
- **Direct observation:** footnote says P compares respondents with nonrespondents. Chi-square P values: infant sex .5206; parity .2039; maternal age <.0001; race/ethnicity <.0001; education <.0001; marital status <.0001; household income <.0001.
- **Population/time/contrast/model/measure:** 1,263 respondents versus 337 nonrespondents at enrollment; categorical characteristics; chi-square P.
- **Match key:** `respondent_nonrespondent_chisquare_etab2`.
- **Required pass checks:** count/category-total reconciliation, P label and display (not a literal-zero issue); no unprovided test assumptions.

## S1007 — eTable 4 imputation-analysis model/adjustment definition

- **Location:** DOC-003 p. 8.
- **Direct observation:** aR (%) is adjusted risk for control/intervention; aRD derives from logistic-regression odds ratios/CIs; P values are logistic-regression values adjusted for multiple outcomes by Hochberg; interaction P is test for multiplicative logistic-regression interaction. Covariates: infant age/sex and maternal age, parity, race, education, marital status, income, hospital pre-study SAFE outcome rate; soft-bedding model has no SAFE rate.
- **Population/time/contrast/model/measure:** imputed age ≥60-day survey data; factorial effects, adjusted risk/risk difference.
- **Match key:** `imputation_aR_aRD_definitions`; **required pass checks:** adjustment/model identity versus main results; OR-to-aR transformation label; CI/P compatibility only under supplied comparable model.

## S1008 — Imputed supine-position NQI and mHealth effects

- **Location:** DOC-003 p. 7.
- **Direct observation:** NQI aRC=78.8, aRNQI=81.6, aRD=2.8 (-3.7,7.9), P=.38. mHealth aRC=78.8, aRmH=87.8, aRD=9.0 (4.2,12.6), P=.003. Multiplicative interaction P=.05.
- **Population/time/contrast/model/measure:** imputed N=400/cell; usual supine sleep past 2 weeks at ≥60 days; adjusted logistic model.
- **Match key:** `imputation_supine_adjusted_effects`.
- **Required pass checks:** aRD contained in CI; sign/direction; P/CI coherence under Hochberg model; interaction/main-effect interpretation and cross-analysis population.

## S1009 — Imputed room-sharing NQI and mHealth effects

- **Location:** DOC-003 p. 7.
- **Direct observation:** NQI aRC=69.7, aRNQI=73.6, aRD=3.9 (-1.1,8.4), P=.38. mHealth aRC=69.7, aRmH=81.7, aRD=12.0 (8.1,15.3), P<.001. Interaction P=.55.
- **Population/time/contrast/model/measure:** imputed age ≥60 days, usual room sharing without bedsharing past 2 weeks; adjusted logistic model.
- **Match key:** `imputation_roomsharing_adjusted_effects`.
- **Required pass checks:** CI/sign/P label and outcome direction; Hochberg display.

## S1010 — Imputed soft-bedding NQI and mHealth effects

- **Location:** DOC-003 p. 7.
- **Direct observation:** NQI aRC=67.4, aRNQI=70.8, aRD=3.4 (-2.6,8.9), P=.38. mHealth aRC=67.4, aRmH=79.1, aRD=11.7 (6.9,15.8), P<.001. Interaction P=.50.
- **Population/time/contrast/model/measure:** imputed age ≥60 days, no soft bedding past 2 weeks; adjusted logistic model, without pre-study SAFE soft-bedding rate.
- **Match key:** `imputation_softbedding_adjusted_effects`.
- **Required pass checks:** CI/sign/P label, covariate exception and outcome direction.

## S1011 — Imputed pacifier-use NQI and mHealth effects

- **Location:** DOC-003 pp. 7-8.
- **Direct observation:** NQI aRC=60.2, aRNQI=65.9, aRD=5.7 (-1.0,11.9), P=.38. mHealth aRC=60.2, aRmH=67.0, aRD=6.8 (0.0,12.8), P=.05. Interaction P=.84.
- **Population/time/contrast/model/measure:** imputed age ≥60 days, any (usually/sometimes) pacifier past 2 weeks; adjusted logistic model.
- **Match key:** `imputation_pacifier_adjusted_effects`.
- **Required pass checks:** boundary rounding at CI 0.0, sign/direction/P coherence only under stated adjusted model; no candidate solely from formatting.

## S1012 — Race/ethnicity post hoc frequency display

- **Location:** DOC-003 pp. 9-11.
- **Direct observation:** eTable 5 provides unadjusted frequency counts/percentages for BF/BF control vs SS/SS combined intervention, by All/White/Black/Hispanic/Other, for four safe-sleep outcomes. eFigure plots percentages only and excludes Other; eTable title says age ≥60 days while eFigure says >60 days.
- **Population/time/contrast/model/measure:** post hoc stratified frequency display; no effect estimate, CI, test or adjustment printed.
- **Match key:** `posthoc_race_ethnicity_control_vs_combined_safe_sleep`.
- **Required pass checks:** raw count/denominator/percent relationships; figure-table identity; strict versus inclusive age label; do not infer significance/testing not provided.

## Statistical coverage status

All 12 S relationships are assigned to both later statistical passes. No supplied support P value is printed as an isolated `P=0`/`p=0.000`; `P<.001` records are inequality displays and require ordinary model-compatible review, not a display-zero candidate rule.
