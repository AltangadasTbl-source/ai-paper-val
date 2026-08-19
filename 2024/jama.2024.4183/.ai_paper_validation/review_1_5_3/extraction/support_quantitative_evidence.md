# Canonical support quantitative evidence map

**Canonical scope:** Lossless merge of the complete, disjoint DOC-002 (45 PDF pages) and DOC-003 (36 PDF pages) support-mapping parts. This artifact preserves source evidence, relationship keys, page-complete records, matching keys, counts, and limitations only; it contains no candidate diagnosis or adjudication.

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
# DOC-003 support quantitative evidence map

## Scope, identity, and fresh-extraction record

- **Source ID and exact scope:** DOC-003, `joi240036supp2_prod_1716416466.01349.pdf`, PDF pages 1-36 inclusive (36 of 36 source pages; all fresh-required).
- **Source identity:** author-supplied supplemental online content for Cinciripini PM et al, *Therapeutic strategies for smoking cessation after initial treatment failure with varenicline or combined nicotine replacement: a randomized clinical trial*, JAMA, doi:10.1001/jama.2024.4183.
- **Fresh direct-source methods:** `pdfinfo` confirmed 36 pages. Fresh native and layout text were extracted directly from the PDF for every page, respectively at `preprocessing/support_doc003/native_p1.txt` through `native_p36.txt` and `preprocessing/support_doc003/layout_p1.txt` through `layout_p36.txt`; combined outputs are `native_all_pages.txt` and `layout_all_pages.txt`. Rendered visual confirmation was performed from the direct PDF for pp. 15, 16, and 19 (`figure_page-15.png`, `figure_page-16.png`, and `table_page-19.png`). No legacy derivative or old review conclusion was used.
- **Coverage result:** 36/36 pages mapped. Pages 1-3 are contents/front matter only; page 36 is references only. Their no-independent-result status is explicitly recorded below. Pages 4-13 contain protocol/SAP/administrative analysis content and are mapped rather than skipped.
- **Notation:** CNRT is combined nicotine replacement; CNRT+ is two 21-mg patches plus a 2-mg lozenge; VAR is varenicline 2 mg/day; VAR+ is varenicline 3 mg/day. EOT is end of treatment (week 12); TQD is target quit date; CA is continuous abstinence; ARD is absolute risk difference; CrI is credible interval; CI is confidence interval; IQR is interquartile range; SD is standard deviation.

## Page-level map

| PDF page | Content and result-relevance | Quantitative/statistical extraction or explicit no-applicable record |
|---|---|---|
| 1 | Supplement title and contents | **No independent result values.** Identifies eAppendices 1-5, eFigures 1-3, and eTables 1-12. |
| 2 | Table of contents, first part | **No independent result values.** Gives document locations: appendices pp. 4-13, figures pp. 14-16, eTables 1-7 pp. 17-31. |
| 3 | Table of contents, continuation | **No independent result values.** Gives eTables 8-12 pp. 32-35 and references p. 36; the printed references entry says “Error! Bookmark not defined.” |
| 4 | Behavioral counseling and sample-size planning | Protocol/SAP quantities: Phase 1 had two 15-minute in-clinic and three telephone counseling visits; Phase 2 had two in-clinic and one telephone visit. TQD was 7 days after randomization; Phase-1 clinic visits were 7 days before and 34 days after TQD; telephone sessions were 1, 24, and 30 days after TQD. Phase-2 visits were 7, 21, and 42 days after rerandomization; medication checks were 5 minutes, one day before and 3 days after TQD in Phase 1, and 3 and 14 days after rerandomization in Phase 2. Planned primary outcome is 7-day point-prevalence abstinence; initial estimates used 12-week continuous abstinence because seven-day point prevalence was unavailable. |
| 5 | Sample-size modeling and start of inverse-probability weighting (IPW) appendix | Plausible abstinence distributions were approximately plus/minus 2-17 percentage points around each cell point estimate. A 95% posterior probability of benefit is described as 5% probability of lack of benefit or harm across the posterior range. Simulations sampled specified beta distributions, analyzed with logistic regression and neutral coefficient priors `Normal(mu=0, sigma=1000)` in log form. |
| 6 | IPW randomization and coding definitions | Phase-1 randomization probability `p=0.5`; Phase-2 abstainers stay on treatment with `p=1`; Phase-1 non-abstainers are rerandomized to continue/increase/switch with printed `p=0.33`. Printed weights: week 6, `1/0.5=2.0`; week-12 Phase-1 abstainers, `1/(0.5*1)=2`; week-12 Phase-1 non-abstainers, `1/(0.5*0.33)=6.06`. R version 4.3/brms; weights multiply each observation’s log-posterior contribution. Coding: initial VAR/NPL (printed term) `1/-1`; continuation `1` versus all others `0`; augmentation `1` versus all others `0`; switch `-1` versus all others `0`. |
| 7 | Logistic model and cell definitions | Twelve-week logistic model: `logit(y)=beta0+beta1*a1+beta2*anr21+beta3*anr22+beta4*anr23+beta5*a1*anr21+beta6*a1*anr22+beta7*a1*anr23`. The page prints the eight cell linear predictors for CNRT/VAR, Phase-1 abstainers, and non-abstainer continuation/increase/switch pathways. Initial proportion priors are `Beta(a=1,b=1)`; linear/logistic/Cox coefficients `Normal(mean=0, variance=1 x 10^6)`; level-1 variance `Inverse Gamma(shape=0.001, scale=0.001)`; level-2 variance `Uniform(0,1000)`. |
| 8 | Prior revision and simulation performance definition | Printed original log-scale 95% CrI `-1960 to 1960`; a nonconvergent interaction gave an odds ratio `3.60 x 10^239`. Intercept prior was changed to `Normal(0, variance=10)`, whose printed prior odds 95% CrI is `3.07 x 10^-9 to 325,215,956`; treatment priors remained `Normal(0, variance=1 x 10^6)`. Superiority is `HA: OR>1`; posterior-benefit thresholds are 0.80, 0.85, 0.90, 0.95; `K=1000`; planned sample `N=500`; all superiority hypotheses had greater than 80% chance of detecting 0.80 posterior probability of benefit. |
| 9 | Secondary-outcome definition and summary | Meta-analytic ARD cited as 0.089. Prespecified confirmation is `Pr(OR>1|data)>0.80`. Secondary CA outcomes are EOT+30 and six months; the study was not powered for frequentist differences at those time points. For week-6 non-abstainers, ETables 9 and 10 report ARDs/95% CrIs and posterior probability of a non-zero difference; ETable 11 compares Phase-1 abstainers continuing CNRT versus VAR. CNRT non-abstainers: `n=191`, switch VAR 10% (`n=51`) or CNRT+ 8% (`n=50`) versus CNRT continuation 3% (`n=90`), each posterior probability `>99%`. |
| 10 | Secondary summary and detailed EOT+30 CNRT results | VAR Phase-1 non-abstainers `n=157`: only VAR+ 8% (`n=39`) benefited versus continuation 0% (`n=42`). At six months, CNRT+ 3% and VAR+ 2% versus 0% continuation had non-zero-difference probabilities 96% and 99%. For EOT+30, text prints CNRT non-abstainer switch/VAR `1.0% (7.0%-1.3%)`, CNRT+ `8.0% (5.0%-1.1%)`, CNRT continuation `3.0% (2.0%-5.0%)`; then prints ARD CNRT+ minus continuation `5.0% (1.0%-8.0%)`, VAR switch minus continuation `6.0% (3.0%-1.0%)`, and CNRT+ minus VAR switch `-2.0% (-6.0%-3.0%)`, with posterior probabilities `>99%`, `>99%`, and 79%, respectively. These printed narrative values have exact matching figure/table keys below; no diagnostic conclusion is made here. |
| 11 | Detailed EOT+30 VAR and six-month CNRT results | EOT+30 VAR non-abstainers: VAR+ `8.0% (5.0%-1.1%)`, switch CNRT `0.0% (0.0%-0.0%)`, continuation VAR `0.0% (0.0%-0.0%)`; VAR+ versus continuation and switch each prints ARD `8.0% (5.0%-1.1%)`, posterior probability `>99%`. EOT+30 Phase-1 abstainers: CNRT `67% (58%-75%)`, VAR `56% (48%-63%)`; printed posterior probability 97% and ARD `1.1% (-1.0%-22%)`. Six-month CNRT non-abstainers: switch VAR `4% (2%-6%)`, CNRT+ `6% (4%-9%)`, CNRT continue `3% (2%-5%)`; printed ARDs/probabilities: CNRT+ `3% (0%-6%)`, 96%; VAR switch `1% (-2%-3%)`, 66%; CNRT+ minus VAR switch `2% (-1%-6%)`, 88%. The page cross-references E-Table 7 for the switch comparison; table key for these outcome contrasts is E-Table 9. |
| 12 | Detailed six-month VAR/abstainer results and post-hoc DTE definition | VAR non-abstainers at six months: VAR+ `2% (1%-5%)`, switch CNRT `0% (0%-0%)`, continue VAR `0% (0%-0%)`; VAR+ minus each comparator prints `2% (1%-5%)`, posterior probability `>99%`; CNRT relative to continue prints `0.0% (0.0%,0%)`. Phase-1 abstainers: CNRT `39% (30%-48%)`, VAR `40% (33%-47%)`; text prints posterior probability 55% and ARD `1.0% (1.3%-1.1%)`, described as a small VAR-continuation benefit. Post-hoc DTE analysis uses IPW for rerandomized nonresponders and data augmentation for responders; GEE with robust standard errors. |
| 13 | DTE interpretation | ETable 12 is defined as frequentist-GEE point estimates and 95% CIs for average week-12 abstinence by full Phase-1/Phase-2 pathway. It states confidence intervals are not posterior distributions and therefore do not support probabilities of the alternative hypothesis. No new numeric result beyond the ETable 12 key. |
| 14 | EFigure 1: anticipated primary-outcome probabilities | Design/prior figure. Week-6 anticipated probabilities: CNRT abstainers `0.48, 0.38-0.58`, `Beta(193,210)`; VAR abstainers `0.50, 0.40-0.60`, `Beta(785,869)`. Week-12 cell priors: CNRT abstainer continue CNRT `0.50, 0.40-0.60`, `Beta(47.3,47.3)`; CNRT non-abstainer continue `0.02, 0.0007-0.0978`, `Beta(1.02,35.48)`; switch VAR `0.40, 0.25-0.57`, `Beta(14.4,21.5)`; CNRT+ `0.20, 0.10-0.34`, `Beta(8.90,34.6)`; VAR abstainer continue `0.75, 0.65-0.83`, `Beta(62.2,21.0)`; VAR non-abstainer continue `0.15, 0.05-0.30`, `Beta(4.35,23.1)`; switch CNRT `0.20, 0.15-0.26`, `Beta(42.8,170.0)`; VAR+ `0.40, 0.26-0.55`, `Beta(17.3,25.7)`. |
| 15 | EFigure 2: EOT+30 CA (visual confirmation) | Direct-PDF visual read: CNRT abstainer/continue CNRT `36/54`, 67%, 95% CrI 58%-75%; VAR abstainer/continue VAR `49/88`, 56%, 48%-63%; CNRT non-abstainer/switch VAR `5/51`, 10%, 7%-13%; CNRT non-abstainer/CNRT+ `4/50`, 8%, 5%-11%; CNRT non-abstainer/continue CNRT `3/90`, 3%, 2%-5%; VAR non-abstainer/switch CNRT `0/41`, 0%, 0%-0%; VAR non-abstainer/VAR+ `3/39`, 8%, 5%-11%; VAR non-abstainer/continue VAR `0/77`, 0%, 0%-0%. The caption defines `N(abst)/N(total)`, `p(abst)`, and 95% CrI. |
| 16 | EFigure 3: six-month CA (visual confirmation) | Direct-PDF visual read: CNRT abstainer/continue CNRT `21/54`, 39%, 30%-48%; VAR abstainer/continue VAR `35/88`, 40%, 33%-47%; CNRT non-abstainer/switch VAR `2/51`, 4%, 2%-6%; CNRT non-abstainer/CNRT+ `3/50`, 6%, 4%-9%; CNRT non-abstainer/continue CNRT `3/90`, 3%, 2%-5%; VAR non-abstainer/switch CNRT `0/41`, 0%, 0%-0%; VAR non-abstainer/VAR+ `1/39`, 2%, 1%-5%; VAR non-abstainer/continue VAR `0/77`, 0%, 0%-0%. |
| 17 | ETable 1: planned simulation cell estimates | Averaged over `K=1000`: Phase-1 abstainers CNRT `0.504 (0.441-0.566)`, VAR `0.749 (0.692-0.801)`; Phase-2 non-abstainers CNRT→CNRT `0.029 (0.017-0.047)`, CNRT→CNRT+ `0.204 (0.160-0.255)`, CNRT→VAR `0.399 (0.343-0.458)`, VAR→VAR `0.159 (0.120-0.203)`, VAR→VAR+ `0.404 (0.347-0.463)`, VAR→CNRT `0.201 (0.157-0.251)`. Values are simulation/planning outputs, not the observed secondary-outcome estimates on pp. 15-16. |
| 18 | ETable 2: simulated power | For `N=500`, posterior thresholds `.80/.85/.90/.95`: VAR>CNRT Phase-1 abstainers power `.948/.980/.974/.963`, average effect `.240 (.160-.327)`; CNRT non-abstainers VAR switch>CNRT continue `.999/.999/.999/.998`, `.370 (.309-.431)`; CNRT+>CNRT continue `.964/.957/.951/.939`, `.175 (.125-.228)`; VAR switch versus CNRT+ `.878/.863/.842/.819`, `.195 (.119-.269)`; VAR non-abstainers VAR+ versus VAR continue `.930/.922/.915/.895`, `.245 (.172-.316)`; VAR+ versus CNRT switch `.917/.905/.890/.859`, `.202 (.127-.288)`. |
| 19 | ETable 3 baseline/demographic table, part 1 | Eight cells are CNRT→abstainer→CNRT (`N=54`), CNRT→non-abstainer→VAR (`N=51`), CNRT→non-abstainer→CNRT (`N=90`), CNRT→non-abstainer→CNRT+ (`N=50`), VAR→abstainer→VAR (`N=88`), VAR→non-abstainer→CNRT (`N=41`), VAR→non-abstainer→VAR (`N=77`), VAR→non-abstainer→VAR+ (`N=39`). Exact rows for age, sex, NIH race/ethnicity, employment, education, household income, and carbon monoxide (ppm) are in fresh `layout_p19.txt`; the direct rendered page confirms the printed VAR→non-abstainer→CNRT “Other” entry is `4.9 (2)` under an `n (%)` row. |
| 20 | ETable 3 baseline/demographic table, part 2 and footnotes | Exact eight-cell rows in fresh `layout_p20.txt`: cigarettes/day median (IQR), FTCD total-score median (IQR), years smoking mean (SD), and age of smoking initiation median (IQR). Definitions: CO eligibility required at least 6 ppm; FTCD is a 6-item, 0-10 scale where higher is more dependence and score 5 or higher is generally moderate-to-severe. |
| 21 | ETable 4: primary-outcome ARD/NNT | Seven-day point-prevalence EOT contrasts: CNRT abstainer versus VAR abstainer ARD 6%, 95% CrI -4% to 16%, NNT 16; CNRT non-abstainer CNRT+ versus stay ARD 6%, 2%-11%, NNT 16; CNRT non-abstainer switch VAR versus stay ARD 6%, 2%-10%, NNT 17; CNRT+ versus switch VAR ARD 0%, -5%-6%, NNT 378; VAR non-abstainer VAR+ versus stay ARD 18%, 13%-23%, NNT 6; switch CNRT versus VAR stay ARD 3%, 1%-4%, NNT 39; VAR+ versus switch CNRT ARD 20%, 16%-26%, NNT 5. NNT is number needed to treat. |
| 22-25 | ETable 5: Phase-1 adverse events | Complete fresh table transcription is in `layout_p22.txt` through `layout_p25.txt` (each row has system, specific AE, CNRT N/estimated rate/95% CrI, and VAR N/estimated rate/95% CrI). The table defines N as event count and the estimate as an IPW estimated rate. It covers cardiovascular; dermatologic; ear/nose/throat; gastrointestinal; general disorders; hematologic; infection; injuries; investigations; metabolic; musculoskeletal; neoplasms; neurologic; psychiatric; reproductive; respiratory; vascular; and immunologic systems. Caption statement: no AE difference exceeded 2% except nausea in VAR; descriptive, no multiple-comparison correction. Key printed nausea values: CNRT N=17, estimate 7.17, CrI 4.39-10.83; VAR N=54, estimate 22.19, CrI 17.31-27.65. |
| 26-30 | ETable 6: Phase-2 adverse events | Complete fresh table transcription is in `layout_p26.txt` through `layout_p30.txt`. Every printed AE row has four arms—CNRT continue, CNRT+, VAR continue, VAR+—with n, IPW estimated rate, and 95% CrI. The table compares each increase condition with its corresponding continuation and the two increase conditions; it includes cardiovascular, dermatologic, ear/nose/throat, gastrointestinal, general, hematologic, infection, injuries, investigations, metabolic, musculoskeletal, neoplasms, neurologic, psychiatric, reproductive, respiratory, vascular, immunologic, and endocrine AEs. Caption statement: no difference exceeded 2% with non-overlapping CrI; descriptive and no multiple-comparison correction. |
| 31 | ETable 7: Phase-1 compliance | CNRT and VAR each `N=245`. Mean visit compliance 89 (SD 21) and 87 (21). Mean medication taken: varenicline 85 (24, placebo) and 87 (22); NRT patch 84 (23) and 84 (23, placebo). Total NRT lozenges, median (IQR): 76 (9.75-140) and 80 (22-135.5, placebo). Medication data incomplete/missing for 1/245 and 3/245, respectively. |
| 32 | ETable 8: Phase-2 compliance | Eight phase-2 cells as on ETable 3, with counts 54, 51, 50, 50, 88, 41, 42, 39. Exact visit and medication-compliance rows are in `layout_p32.txt`. Missing medication data: 3/54, 2/51, 7/88, 1/41, 2/42, 1/39 (footnotes a-f); asterisks mark placebo. Note that the CNRT non-abstainer continuation column is printed `N=50` here, while the EFigures and ETable 3 outcome cell key use 90. |
| 33 | ETable 9: secondary non-abstainer ARDs | EOT+30 versus respective continuation: CNRT switch VAR 6% (3%-10%), CNRT+ 5% (1%-8%), VAR switch CNRT 0% (0%-0%), VAR+ 8% (5%-11%); non-zero probabilities >99%, >99%, 50%, >99%. Six months: 1% (-2%-3%), 3% (0%-6%), 0% (0%-0%), 2% (1%-5%); probabilities 66%, 96%, 50%, >99%. Difference is increase/switch minus continuation; EOT+30 is week 12 plus 30 days; six months is post-TQD. |
| 34 | ETable 10: increase versus switch ARDs | Reference is switch (increase minus switch). EOT+30: CNRT+ versus VAR -2% (-6%-3%), probability 79%; VAR+ versus CNRT 8% (5%-11%), >99%. Six months: CNRT+ versus VAR 2% (-1%-6%), 89%; VAR+ versus CNRT 2% (1%-5%), >99%. |
| 35 | ETables 11 and 12 | ETable 11 (CNRT versus VAR among Phase-1 abstainers): EOT+30 CA ARD 11% (-1%-22%), probability non-zero 97%; six-month CA ARD 1% (-11%-12%), probability 56%. ETable 12 GEE DTE week-12 probabilities/95% CIs: VAR,VAR,VAR 0.21 (0.03-0.70); VAR,VAR,CNRT 0.30 (0.04-0.80); VAR,VAR,VAR+ 0.42 (0.05-0.90); CNRT,CNRT,CNRT 0.19 (0.02-0.74); CNRT,CNRT,VAR 0.30 (0.03-0.87); CNRT,CNRT,CNRT+ 0.31 (0.03-0.87). Nomenclature order is Phase-1 treatment, Phase-2 treatment if abstinent, then Phase-2 treatment if non-abstinent. |
| 36 | References | **No independent result-relevant support values.** Administrative bibliography only; it records cited publication years, volumes, pages, and DOIs. |

## Cross-location matching keys retained for later independent checking

These are source-location keys and printed values, not candidate diagnoses or adjudications.

1. **Secondary EOT+30 outcome cell: CNRT Phase-1 non-abstainer, switch to VAR.** EFigure 2 p. 15 is `5/51`, 10%, 95% CrI 7%-13%; ETable 9 p. 33 gives switch-minus-CNRT-continuation ARD 6% (3%-10%) with `>99%`; narrative p. 9 says 10% (`n=51`), while detailed narrative p. 10 prints `1.0% (7.0%-1.3%)` and ARD `6.0% (3.0%-1.0%)`.
2. **Secondary EOT+30 outcome cell: CNRT Phase-1 non-abstainer, CNRT+.** EFigure 2 p. 15 is `4/50`, 8%, 5%-11%; ETable 9 p. 33 ARD 5% (1%-8%), `>99%`; detailed narrative p. 10 prints `8.0% (5.0%-1.1%)`.
3. **Secondary EOT+30 outcome cell: VAR Phase-1 non-abstainer, VAR+.** EFigure 2 p. 15 is `3/39`, 8%, 5%-11%; ETable 9 p. 33 ARD 8% (5%-11%), `>99%`; narrative p. 11 prints 8.0% with `5.0%-1.1%` in both cell and ARD statements.
4. **Secondary EOT+30 Phase-1 abstainers, CNRT versus VAR.** EFigure 2 p. 15 gives 67% (58%-75%) versus 56% (48%-63%); ETable 11 p. 35 reports 11% (-1%-22%), probability 97%; narrative p. 11 prints ARD `1.1% (-1.0%-22%)`.
5. **Secondary six-month Phase-1 abstainers, CNRT versus VAR.** EFigure 3 p. 16 gives 39% (30%-48%) versus 40% (33%-47%); ETable 11 p. 35 reports 1% (-11%-12%), probability 56%; narrative p. 12 prints `1.0% (1.3%-1.1%)` and describes a VAR-continuation benefit. Direction/reference definition must be checked against ETable 11’s header before any conclusion.
6. **Secondary six-month CNRT non-abstainer, switch VAR.** EFigure 3 p. 16 gives `2/51`, 4% (2%-6%); ETable 9 p. 33 reports switch-minus-continuation ARD 1% (-2%-3%), probability 66%; narrative p. 11 names ETable 7 rather than ETable 9 for this comparison.
7. **Phase-2 cell denominators.** The outcome/baseline key is 54, 51, 90, 50, 88, 41, 77, 39 (pp. 15-16 and 19); ETable 8 p. 32 prints 54, 51, 50, 50, 88, 41, 42, 39. Its column labels and compliance populations require definition matching rather than automatic equivalence.
8. **ETable 3 p. 19 label/value orientation.** Under race/ethnicity `Other`, VAR Phase-1 non-abstainer→CNRT is directly printed `4.9 (2)` although the row label is `n (%)`; all other populated cells use count followed by percent. This exact printed form is retained as a label/value matching key.

## Completion and limitations

- **Mapped pages:** 36/36; **no-applicable pages:** 1-3 and 36 (independent result values absent, but administrative contents/references recorded); **tables/figures mapped:** 3 figures and 12 eTables; **appendix/protocol sections mapped:** 5.
- **Fresh extraction gaps:** none. Direct text was usable on all pages; visual confirmation was necessary only for the plotted image-only numerical columns of EFigures 2-3 and the ambiguous ETable 3 cell orientation.
- **Boundary:** This artifact records source evidence and matched keys for subsequent numeric/statistical checking. It does not assign candidate IDs, diagnoses, severity, validity, or adjudication.
