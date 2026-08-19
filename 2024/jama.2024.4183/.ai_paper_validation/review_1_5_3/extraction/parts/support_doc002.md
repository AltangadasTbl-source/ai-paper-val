# DOC-002 Support Evidence Mapping — Protocol 2014-0213

## Scope and method

- **Direct source:** `joi240036supp1_prod_1716416466.00349.pdf` (45 PDF pages), titled *Varenicline and Combined NRT for Initial Smoking Cessation and Rescue Treatment in Smokers: A Randomized Pilot Trial*; protocol 2014-0213, dated August 23, 2023.
- **Assigned unit scope:** PDF pages 1-45, all fresh-required. All 45 pages were directly extracted from the current source using native and layout text. Targeted visual confirmation was performed for Figure 1 (p. 10), Table 1 (pp. 16-17), the data-analysis formula and contrasts (pp. 28-30), Figure 2 (p. 32), Table 2 (p. 33), and Table 3 (p. 34).
- **Fresh derivatives:** `preprocessing/support_doc002/native_all_pages.txt`, `layout_all_pages.txt`, `native_p1.txt` through `native_p45.txt`, `layout_p1.txt` through `layout_p45.txt`, and targeted `render_p10.png`, `render_p16.png`, `render_p17.png`, `render_p28.png` through `render_p34.png`.
- **Source-link convention:** all locations below refer to `joi240036supp1_prod_1716416466.00349.pdf#page=N`.
- **Matching main-paper keys:** `Protocol 2014-0213`; smoking-cessation SMART; Phase I `VAR 2 mg` versus `NRT + Lozenge (NPL)`; Week 6 response/non-response; Phase II continuation, switch, or augmentation; primary Week 12/EOT seven-day point-prevalence abstinence with expired CO verification; planned N=500 study participants (plus up to 10 pilot participants). These keys identify planned support relationships only and do not assert that a main-paper occurrence has been located.

## Result-relevant planned population, interventions, endpoints, and definitions

| Key | Direct source evidence | Matching key / quantitative interpretation |
|---|---|---|
| DOC002-N01 | The design is double-blind, two-group Phase I with up to 510 smokers: up to 10 pilot and 500 study participants. Initial randomization is NPL (21-mg patch plus ad-lib 2-mg lozenge) or VAR (2-mg total daily dose). Non-abstainers at Week 6 undergo Phase II re-randomization to continuation, switching, or augmentation. | Population and design denominator key. The power simulations and Table 3 explicitly use N=500, not 510. |
| DOC002-N02 | Eligibility: age 18-75; average at least 5 cigarettes/little cigars/cigarillos per day during the 2 preceding months and expired CO at least 6 ppm; if under 5 cigarettes, positive cotinine test. | Study-population and smoking-status definition. Location: pp. 7-8. |
| DOC002-N03 | Figure 1 shows the Phase I/II decision paths: NPL or VAR 2 mg; at Week 6, `Quit` continues initial treatment and `No Quit` receives NPL/VAR continuation, NPL+ (high-dose patch plus lozenge), VAR 2 mg, or VAR+ (3 mg), conditional on initial treatment. | Treatment/response-path matching key. Location: p. 10 (visual confirmation). |
| DOC002-N04 | Week 6 is Visit 5; EOT Week 12 is Visit 8; follow-ups are Visit 9 at 3 months post-quit and Visit 10 at 6 months post-quit. Table 1 gives days from quit of 34 (V5), 78 (V8), 108 (V9), and 181 (V10). | Time-point matching key. Table 1: pp. 16-17 (visual confirmation). |
| DOC002-N05 | Primary outcome: EOT seven-day point-prevalence abstinence, defined as no smoking for the past 7 days. Data are collected at all contacts with timeline follow-back (TLFB). | Endpoint definition and scale: binary abstinent/nonabstinent. Location: p. 20. |
| DOC002-N06 | Secondary abstinence outcomes: prolonged and continuous abstinence at 3 and 6 months. The prolonged-abstinence grace period ends 2 weeks after EOT; relapse is smoking 5 or more cigarettes from then to a future point. Continuous abstinence is assessed over the 4 weeks after EOT (EOT plus 30 days). | Secondary-endpoint definitions. Location: p. 20. |
| DOC002-N07 | In-person abstinence reports are to be verified by expired CO under 6 ppm and/or salivary cotinine under 15 ng/mL at follow-up. Participants unavailable for TLFB are considered nonabstinent. Urine cotinine represents exposure over the prior 24-36 hours; subsequent cotinine values under 15 ng/mL are a cross-check when expired CO is unavailable. | Biochemical-verification threshold, missing-data classification, and unit key. Location: p. 20. Note the eligibility CO threshold is at least 6 ppm (DOC002-N02) whereas abstinence verification is under 6 ppm. |
| DOC002-N08 | Phase I medication begins one day after randomization and 7 days before quit. VAR dosing: 0.5 mg/day on days 1-3, 0.5 mg twice daily on days 4-7, then 1 mg twice daily. NPL: active 21-mg patch plus ad-lib 2-mg lozenge. At Week 6, abstainers continue to Week 12; non-abstainers are re-randomized. VAR+ adds 1 mg with the PM dose (3 mg total daily); NPL+ adds a 21-mg patch (42 mg total daily). | Exposure and dose key. Locations: pp. 24-25. |
| DOC002-N09 | Adaptive randomization/minimization stratifies by motivation, gender, and race. The protocol estimates screening at least 1,000 people to obtain the planned eligible population. | Randomization and recruitment denominator context. Location: p. 7. |
| DOC002-N10 | Affect, withdrawal, craving, and nicotine reinforcement outcomes (PANAS, CES-D, WSWS, mCEQ) are planned for generalized linear models at Weeks 6 and 12. Adverse-event probabilities are planned for Beta-Binomial models. | Secondary-outcome/model key. Locations: pp. 7 and 30. |

## Statistical-analysis plan and formulas

| Key | Direct source evidence | Formula, definition, or planned comparison |
|---|---|---|
| DOC002-S01 | Five planned effects: Aim 1 among Week-6 responders; Aim 2 among initial-NPL nonresponders; Aim 3 among initial-VAR nonresponders; exploratory Aim 4 augmentation interaction; exploratory Aim 5 switching interaction. Primary analytic approach is Bayesian and the primary endpoint is EOT seven-day point prevalence with expired CO. | Location: p. 27. |
| DOC002-S02 | Continuous, dichotomous, and time-to-event outcomes use linear, logistic, and proportional-hazards regression, respectively (PROC GENMOD/PHREG); longitudinal analyses use generalized linear mixed models (PROC MCMC). Primary analyses are intention-to-treat with missing observations imputed as smoking. Secondary analyses use joint modeling under ignorable missingness; sensitivity analysis addresses missingness and pattern-mixture models address nonignorable missing patterns. | Location: p. 28. |
| DOC002-S03 | Priors: proportion comparisons use Beta(a=1,b=1). Linear, logistic, and Cox regression coefficients use Normal(mean=0, variance=1×10^6) priors on linear, log-odds, and log scales. Level-1 variances use Inverse Gamma(shape=0.001, scale=0.001); level-2 variances use Uniform(0,1000). Optimistic, pessimistic, and skeptical priors are planned for sensitivity analysis. | Location: p. 28. |
| DOC002-S04 | Coding: initial VAR and NPL are 1 and -1, respectively. For nonresponders, continuation is 1 versus all others 0; augmentation is 1 versus all others 0; switching is -1 versus all others 0. | Location: p. 28. |
| DOC002-S05 | Logistic model at 12 weeks: `logit(y) = β0 + β1*a1 + β2*anr21 + β3*anr22 + β4*anr23 + β5*a1*anr21 + β6*a1*anr22 + β7*a1*anr23`, where `a1` denotes initial treatment and `anr21`, `anr22`, `anr23` denote nonresponder continuation, augmentation, and switching vectors. | Formula visually confirmed on p. 28. |
| DOC002-S06 | Derived outcome-cell linear predictors: NRT+Loz responders `β0−β1`; Var 2mg responders `β0+β1`; NRT nonresponders continuing NRT+Loz `β0−β1+β2−β5`; NRT nonresponders to 2×NRT+Loz `β0−β1+β3−β6`; NRT nonresponders to Var 2mg `β0−β1−β4+β7`; Var nonresponders continuing Var 2mg `β0+β1+β2+β5`; Var nonresponders to Var 3mg `β0+β1+β3+β6`; Var nonresponders to NRT+Loz `β0+β1−β3+β7`. | Locations: pp. 28-29; visual confirmation of formulas. |
| DOC002-S07 | Aim 1 contrast: Var 2mg responders minus NRT+Loz responders equals `(β0+β1)−(β0−β1)`. Aim 2 compares, among initial-NPL nonresponders, Var versus NPL continuation, NPL+ versus NPL continuation, and Var versus NPL+. Aim 3 compares, among initial-VAR nonresponders, VAR+ versus VAR continuation and VAR+ versus NPL. | Locations: pp. 29-30; specific contrasts printed. |
| DOC002-S08 | Exploratory Aim 4 contrast: initial VAR nonresponders augmented to Var 3mg minus initial NPL nonresponders augmented to 2×NRT+Loz equals `(β0+β1+β3+β6)−(β0−β1+β3−β6)`. Exploratory Aim 5 contrast: NPL nonresponders switching to Var 2mg minus VAR nonresponders switching to NRT+Loz equals `(β0−β1−β4+β7)−(β0+β1−β3+β7)`. | Location: p. 30; visual confirmation. |
| DOC002-S09 | Moderation at Week 6 is planned for motivation, dependence level, and nicotine metabolic ratio (normal versus slow), using baseline covariate, treatment assignment, and their interaction. Initial interactions use vague neutral priors; skeptical informative priors are planned for sensitivity analysis. | Locations: pp. 7 and 30. |
| DOC002-S10 | The protocol states a posterior probability greater than 0.90 that the postulated effect exists, expressed as `Pr(Pr θ > 0 | data) > 0.90`, is sufficient to warrant further evaluation. | Decision threshold as printed. Location: p. 31; visual confirmation. The nested notation is preserved rather than normalized. |
| DOC002-S11 | Figure 2 and Tables 2-3 are Monte Carlo planning outputs, not observed trial results. Figure 2 parameters describe prior point estimates and 95% credible intervals; K=1,000 simulations determine predictive power. | Locations: pp. 31-34. |

## Figure 2 simulation inputs (planning parameters)

Figure 2 (p. 32; visual confirmation) supplies the following prior probability, interval, and beta-distribution labels. Values are planning inputs and should not be matched as observed study results.

| Phase I / Week 6 state | Phase II path / Week 12 outcome | Printed probability and interval | Printed beta distribution |
|---|---|---:|---|
| NRT + Lozenge response | NRT + Lozenge | 0.48, 0.38-0.58 at Week 6; outcome 0.50, 0.40-0.60 | Week 6 `Beta(193,210)`; outcome `Beta(47.3,47.3)` |
| NRT + Lozenge nonresponse | NRT + Lozenge | 0.02, 0.0007-0.0978 | `Beta(1.02,35.48)` |
| NRT + Lozenge nonresponse | 2×NRT + Lozenge | 0.20, 0.10-0.34 | `Beta(8.90,34.6)` |
| NRT + Lozenge nonresponse | Varenicline 2 mg | 0.40, 0.25-0.57 | `Beta(14.4,21.5)` |
| Varenicline 2 mg response | Varenicline 2 mg | 0.50, 0.40-0.60 at Week 6; outcome 0.75, 0.65-0.83 | Week 6 `Beta(785,869)`; outcome `Beta(62.2,21.0)` |
| Varenicline 2 mg nonresponse | Varenicline 2 mg | 0.15, 0.05-0.30 | `Beta(4.35,23.1)` |
| Varenicline 2 mg nonresponse | NRT + Lozenge | 0.20, 0.15-0.26 | `Beta(42.8,170.0)` |
| Varenicline 2 mg nonresponse | Varenicline 3 mg | 0.40, 0.26-0.55 | `Beta(17.3,25.7)` |

## Tables and planned power results

### Table 1 — Study Time Line and Procedures

Table 1 spans pp. 16-17. It schedules screening (visits -1 and 0), Phase I randomization (V1), V5/Week 6, EOT V8/Week 12, V9/3-month follow-up, and V10/6-month follow-up. It identifies TLFB abstinence questionnaire, expired CO, urine cotinine/saliva alternatives, adverse-event monitoring, medication counts, behavioral counseling, and questionnaires. Footnotes specify that EMA daily diary is completed daily for 84 treatment-phase days; EMA assessments are daily for two weeks in each treatment phase; urine cotinine is collected at V9/V10 if in person and saliva may substitute; and V1 medication starts the next day. This table is the timepoint/measurement operational key for DOC002-N04 through DOC002-N07.

### Table 2 — Average simulated cell estimates

Table 2 (p. 33; visual confirmation) reports average point estimates and average 95% interval estimates across K=1,000 simulations:

| Cell / effect | Average point estimate | Average 95% interval estimate |
|---|---:|---|
| Responders: NRT+Loz | 0.504 | 0.441-0.566 |
| Responders: Var 2mg | 0.749 | 0.692-0.801 |
| NRT+Loz nonresponders → NRT+Loz | 0.029 | 0.017-0.047 |
| NRT+Loz nonresponders → 2×NRT+Loz | 0.204 | 0.160-0.255 |
| NRT+Loz nonresponders → Var 2mg | 0.399 | 0.343-0.458 |
| Var 2mg nonresponders → Var 2mg | 0.159 | 0.120-0.203 |
| Var 2mg nonresponders → Var 3mg | 0.404 | 0.347-0.463 |
| Var 2mg nonresponders → NRT+Loz | 0.201 | 0.157-0.251 |

### Table 3 — Predictive power and simulated effect contrasts

Table 3 (p. 34; visual confirmation) reports posterior-probability thresholds of 0.80, 0.85, 0.90, and 0.95; predictive power to detect `Pr(θ>0)`; and one average point estimate plus 95% credible interval for each effect.

| Planned effect | Predictive power at posterior thresholds 0.80 / 0.85 / 0.90 / 0.95 | Average point estimate (95% credible interval) |
|---|---|---|
| Phase I responders, Aim 1 | 0.948 / 0.980 / 0.974 / 0.963 | 0.240 (0.160-0.327) |
| Phase II after NPL nonresponse: VAR vs NPL, Aim 2 | 0.999 / 0.999 / 0.999 / 0.998 | 0.370 (0.309-0.431) |
| Phase II after NPL nonresponse: NPL+ vs NPL, Aim 2 | 0.964 / 0.957 / 0.951 / 0.939 | 0.175 (0.125-0.228) |
| Phase II after NPL nonresponse: printed `VAR vs NPL`, Aim 2 | 0.878 / 0.863 / 0.842 / 0.819 | 0.195 (0.119-0.269) |
| Phase II after VAR nonresponse: VAR+ vs VAR, Aim 3 | 0.930 / 0.922 / 0.915 / 0.895 | 0.245 (0.172-0.316) |
| Phase II after VAR nonresponse: VAR+ vs NPL, Aim 3 | 0.917 / 0.905 / 0.890 / 0.859 | 0.202 (0.127-0.288) |
| Treatment Phase I × augmentation, exploratory Aim 4 | 0.885 / 0.875 / 0.862 / 0.837 | 0.199 (0.123-0.274) |
| Treatment I × switching, exploratory Aim 5 | 0.899 / 0.885 / 0.872 / 0.846 | 0.198 (0.123-0.272) |

The p. 33 narrative states all superiority hypotheses have more than 80% chance of detecting a 0.90 probability of benefit for N=500. It also states that the absolute risk reduction 0.089 from a cited meta-analysis is smaller than the lower-bound 95% credible limits for all Table 3 contrasts. This is a planning/narrative comparison, not an observed study result.

## Reconciliation-relevant source links for downstream checking (not candidate determinations)

- **DOC002-R01:** In Figure 2, the printed Week-6 Varenicline 2-mg response label is `0.50, 0.40-0.60` with `Beta(a=785,b=869)`. The beta mean calculated directly from the printed parameters is `785/(785+869)=0.4746`. Preserve both the displayed probability/interval and the printed parameters when checking any parameter-to-label relationship.
- **DOC002-R02:** Under Table 3's `Treatment Phase II Following Non-Response to NPL / Hypothesis Tests Aim 2`, the third printed effect label is `VAR vs. NPL`, with average point estimate 0.195 (0.119-0.269). Table 2 has NRT+Loz nonresponder estimates 0.399 for `→ Var 2mg`, 0.204 for `→ 2×NRT+Loz`, and 0.029 for `→ NRT+Loz`; `0.399−0.204=0.195`. The p. 29 Aim-2 formula lists three contrasts in order: Var versus continuation, augmentation versus continuation, and Var versus augmentation. These are source locations and arithmetic inputs for a later checker; no candidate conclusion is made here.

## Contextual historical numbers and non-result administrative content

- **Contextual literature numbers, not trial results:** pp. 3-5, 24, and 35-38 contain cited epidemiologic, efficacy, safety, or meta-analytic values. Examples include the 73-person 3-mg varenicline study (40% abstinence; 22 adverse events/30%; 2 discontinuations); 44 versus 44 historical groups with 4/44 (9%) versus 11/44 (25%), χ²=3.94, p=.05, OR=3.33, 95% CI 1.12-11.45; and cited historical odds ratios and safety frequencies. These were mapped as external context only and are not main-paper matching keys.
- **Administrative/protocol quantitative content retained:** pp. 11-15 define screening, visit windows, missed-visit handling, and medication/compliance procedures; pp. 21-23 define adverse-event reporting/CTCAE grading and blinded assessment procedures; pp. 24-26 define dosing, blood-pressure actions (15% increase plus >160/100; discontinuation at >180/110), blinding, counseling (4 in-person + 4 phone visits, up to 4 support calls, 10-15 minutes), and compensation (up to $594, including up to $84 EMA and $30 EMA-return bonus); p. 27 describes an up-to-10-person open-label pilot. These operational details may define a reported population or exposure but do not themselves report trial results.

## Explicit page-complete coverage

| PDF pages | Coverage finding |
|---|---|
| 1-2 | Administrative title and contents only; no result-relevant quantitative relationship. |
| 3-5 | Background and external literature numeric context; study design, Phase I/II treatments, Week 6/12 times, and planned N=500 mapped in DOC002-N01/N03/N08. |
| 6-7 | Specific aims, planned endpoints/models, target population and randomization mapped in DOC002-N01/N05/N09/N10 and DOC002-S01/S09. |
| 8-9 | Eligibility population and smoking-status thresholds mapped in DOC002-N02; remaining exclusion criteria are administrative eligibility content. |
| 10 | Figure 1 visually mapped in DOC002-N03; population description is recruitment context. |
| 11-15 | Fresh-reviewed operational procedures. Quantitative endpoint-relevant visit, biochemical, follow-up, and compliance details mapped in DOC002-N04/N07/N08; remaining consent/procedure text has no additional result relationship. |
| 16-17 | Table 1 and footnotes visually mapped; schedule and measurement definitions recorded above. |
| 18-19 | Questionnaire/scale descriptions: secondary measures only; no observed results. Instrument item counts/scales and reliability are external descriptive context. |
| 20 | Primary/secondary abstinence definitions, CO/cotinine verification, and missing-data classification mapped in DOC002-N05/N06/N07. |
| 21-23 | Adverse-event grading/reporting and assessment administration reviewed; no observed result or additional planned inferential relationship beyond DOC002-N10. |
| 24-26 | Medication, dose, blinding, counseling, and compensation operational quantities mapped in DOC002-N08 and administrative note above. |
| 27-31 | Complete data-analysis plan, population/endpoint, models, priors, coding, formulas, contrasts, and Bayesian threshold mapped in DOC002-S01 through DOC002-S11. |
| 32 | Figure 2 visually mapped in full. All eight probability/distribution paths are transcribed above. |
| 33 | Table 2 visually mapped in full and Table 3 narrative/power interpretation mapped. |
| 34 | Table 3 visually mapped in full. |
| 35-39 | Protection-of-human-subjects material and cited historical safety/efficacy context reviewed. No trial result, planned test, or matching main-paper result beyond previously mapped exposure/safety definitions. |
| 40-45 | References only; no result-relevant quantitative relationship. |

## Handoff counts and limitations

- **Direct source units mapped:** 45 of 45 PDF pages; 0 reusable units relied on in this shard; 45 fresh-required units complete.
- **Tables mapped:** 3 (Table 1, Table 2, Table 3). **Figures mapped:** 2 (Figure 1, Figure 2). **Core planned numeric/endpoint/population relationships:** 10. **Core planned statistical/model relationships:** 11. **Reconciliation-relevant links recorded:** 2. **Simulation cell estimates transcribed:** 8. **Planned Table 3 effect rows transcribed:** 8.
- **No-applicable units:** pp. 1-2 and 40-45; other non-result administrative pages are explicitly recorded in the page-complete table rather than inferred absent.
- **Limitations:** This protocol contains planned analyses and simulation outputs, not observed trial results. It does not provide a protocol version crosswalk to a published main paper. Formula glyphs in native text were corrupted, so formulas and Figure 2/Table 1-3 values were confirmed from source-page rendering. No OCR was needed because native/layout text was usable and visuals resolved the relevant content.
