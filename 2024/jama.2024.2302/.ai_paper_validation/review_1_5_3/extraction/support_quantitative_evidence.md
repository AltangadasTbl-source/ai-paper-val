# Support Quantitative Evidence Map

## Scope, method, and boundaries

- **Assigned direct-source scope completed:** PDF-002 pages 1-25; PDF-003 pages 1-10; PDF-004 pages 1-8; DOCX-001 `w:p` paragraphs 1-237 and `w:tbl` tables 1-5.
- **Direct extraction:** fresh `pdftotext` native and layout text was made for every assigned PDF page. PDF-004 pages 2-5 were also directly rendered and visually checked against the PDF because the reusable text has corrupted glyphs. PDF-002 figures 1-2 were directly rendered because native text did not carry their labels. The DOCX OpenXML structure was directly counted; its legacy candidate prose was deliberately not read or used for discovery.
- **Relationship identifiers in this mapper artifact:** `N-SUP-*` and `S-SUP-*` are mapper-local, source-stable IDs. The coordinator must assign the final package-wide `N###`/`S###` IDs without collapsing distinct relationships.
- **Candidate boundary:** This is an extraction map, not candidate diagnosis. The SAP's own stated protocol clarification is recorded verbatim as a source relationship for later cross-source checking; no legacy DOCX assertion was used.
- **Matching main-paper keys:** `MP-PRIMARY-SAE` = early versus late infants with at least one SAE in the 10-month study period; `MP-HOSPITAL-DAYS` = total hospital days during that period; `MP-TRIAL-POPULATION` = randomized and analysis populations; `MP-NEURODEVELOPMENT` = BSID-III follow-up; `MP-CENTER` = site/randomization-centre information.

## Complete unit coverage

| Source and units | Result-relevant extraction and status |
|---|---|
| PDF-002 pp. 1-4 | Protocol identity, hypotheses, outcome definitions, and historical/pilot context mapped below. |
| PDF-002 p. 5 | Table 1 pilot RCT fully mapped below. |
| PDF-002 p. 6 | Figure 1 directly rendered; timeline/sample labels mapped below. |
| PDF-002 p. 7 | Figure 2 directly rendered; it is a blank CONSORT template with `n =` placeholders, explicitly no observed flow counts. |
| PDF-002 pp. 8-10 | Recruitment, eligibility, treatment timing, and administrative site table inspected; only definitions/timing are result-relevant. |
| PDF-002 pp. 11-15 | Primary/secondary definitions, BSID scale, sample-size/power table, model plan, subgroup and stopping rules mapped below. |
| PDF-002 pp. 16-17 | Administration/governance and trial-commencement material inspected; no additional result-relevant quantitative relationship beyond the recorded pilot/start dates and monitoring cadence. |
| PDF-002 pp. 18-22 | Bibliography only: no applicable trial-result relationship. |
| PDF-002 pp. 23-24 | SAE definition table and ascertainment window mapped below. |
| PDF-002 p. 25 | Protocol-change log mapped; version 7 changes interim monitoring to approximately 200 infants and adds final Bayesian analyses. |
| PDF-003 pp. 1-10 | SAP identity, definitions, populations, models, priors, sensitivity/subgroup plans, and missing-data rule mapped below. |
| PDF-004 p. 1 | Supplement cover and table list only; no standalone quantitative result. |
| PDF-004 pp. 2-4 | eTable 1 directly visually confirmed and fully mapped below. |
| PDF-004 p. 5 | eTable 2 directly visually confirmed and fully mapped below. |
| PDF-004 p. 6 | eTable 3 centre-by-centre randomization counts mapped below. |
| PDF-004 pp. 7-8 | Acknowledgments/personnel only: no applicable result-relevant quantitative relationship. |
| DOCX-001 P001-P009; T1; P010-P039; T2; P040-P106; T3; P107-P168; T4; P169-P227; T5; P228-P237 | Complete structural mapping. This legacy-named auxiliary has 237 paragraph elements and 5 contained tables. Each listed paragraph/table unit is **NOT APPLICABLE FOR SCIENTIFIC DISCOVERY**: only legacy candidate assertions may be present, and none was read, transcribed, matched, or used. T1 follows P009, T2 P039, T3 P106, T4 P168, and T5 P227. |

## Numeric/reporting relationships

### N-SUP-001 — Protocol primary outcome and planned contrast

- **Locations:** [PDF-002 p. 2](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=2>), pp. 3, 11-14, and 23-24.
- **Main key:** `MP-PRIMARY-SAE`.
- **Printed definition:** proportion of infants with `>1 SAE` from enrollment through 10 months after enrollment; ascertainment is by masked adjudication. The protocol elsewhere uses “at least one SAE” / `≥1 SAE` in planned analysis wording; retain the printed threshold wording at each location.
- **Planned contrast/value:** late repair versus early repair; hypothesized 10 percentage-point absolute reduction, described once as RR 0.66 and number needed to harm 10 for early repair. The original protocol sample-size formulation is 30% early versus 20% late.
- **Labels/time/units:** infant-level proportion/percentage, 10-month window, early repair before discharge at about 38 weeks PMA versus late repair about 5 months after discharge / 55-60 weeks PMA.

### N-SUP-002 — Protocol major secondary outcomes and BSID scale

- **Locations:** PDF-002 pp. 2-3 and 11-13; PDF-003 pp. 2-4 and 7-8.
- **Main keys:** `MP-HOSPITAL-DAYS`; `MP-NEURODEVELOPMENT`.
- **Hospital days:** total hospital days from enrollment through 10 months after enrollment; hypothesis is 3 fewer median days with late repair. Correct design values later given as median 8, mean 18 (early) and median 5, mean 13 (late), under a log-normal distribution.
- **BSID-III:** assessment at 22-26 months corrected age; hypothesis is 0.4 SD / 6 points higher cognitive composite score with late repair. Composite mean 100, SD 15; score below 70 is significant delay; a child unable to complete the cognitive scale because of severe neurological/developmental delay is assigned 54. The design assumes 200 assessed infants.

### N-SUP-003 — Pilot RCT Table 1

- **Location:** [PDF-002 p. 5](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=5>), Table 1 and footnotes.
- **Main keys:** historical context only; no direct final-result match.
- **Groups:** early `N=19`; late `N=20*`.
- **Rows (early; late):** estimated gestational age weeks `28.9 (24-32); 28.4 (25-34)`; birth weight g `959 (520-1,550); 958 (500-2,710)`; PMA at operation weeks `38.4 (34-49); 48.6 (33-61)**`; operation weight kg `2.55 (1.8-4.0); 3.9 (1.3-8.9)`; postoperative apnea/bradycardia `4/19 (21%); 0`; reintubation/failure to extubate `5/19 (26%); 2/12 (17%)`; any anesthetic AE `9/19 (47%); 2/12 (17%)`; postoperative LOS median (range) `8 (1-206); 1 (0-30)`; medical attention for IH reduction `0; 6/12 (50%)`; death after IH repair `0; 0`.
- **Footnotes:** 8 late-group infants did not have repair during the study period: 2 died after NICU discharge, 5 lost to follow-up, 1 had no identifiable IH at follow-up. Six had repair before 55 weeks PMA (range 33-49): 4 incarceration and 2 parental/provider preference. These denominators explain the late operative-event denominator 12.

### N-SUP-004 — Protocol study-design figure and eligibility/timing definitions

- **Locations:** [PDF-002 p. 6](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=6>) Figure 1; pp. 8-11.
- **Main keys:** `MP-TRIAL-POPULATION`; `MP-PRIMARY-SAE`; `MP-NEURODEVELOPMENT`.
- **Directly rendered Figure 1 labels:** identify/consent approximately 2 weeks before anticipated NICU discharge; randomization approximately 36 weeks PMA (study time zero); early repair approximately 38 weeks PMA; late repair approximately 55 weeks PMA; prospective SAE measurement approximately 10 months, `N=586`; neurodevelopmental assessment at 22-26 months corrected age.
- **Eligibility:** GA below 37 weeks 0 days, NICU/other nursery at a participating site, surgeon-diagnosed IH, and parent consent/provider willingness to randomize. Randomization is stratified by site and GA strata `<28` versus `>28` weeks in the protocol wording.

### N-SUP-005 — Protocol sample size, power, and Table 4

- **Locations:** [PDF-002 pp. 12-13](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=12>); PDF-003 pp. 3-4.
- **Main keys:** `MP-TRIAL-POPULATION`, `MP-PRIMARY-SAE`, `MP-HOSPITAL-DAYS`.
- **Primary design:** 293 per group (`N=586`) gives 80% power, two-sided alpha 0.05, for 30% versus 20% (10% absolute difference). Assumptions: 20 eligible infants/year/site, 60% randomization, 95% 10-month follow-up, 19 sites, 615 randomized over about 2.5 years, and 586 assessed.
- **Table 4, infants/group: SAE 10% difference power; 3-day median hospital-day difference power:** `293: 80%; 98%`; `250: 73%; 97%`; `200: 64%; 92%`; `150: 52%; 81%`.
- **Secondary design:** 98% power for the specified hospital-day difference and a 0.4-SD/6-point BSID difference with 200 infants assessed at 22-26 months.

### N-SUP-006 — Protocol SAE, harm, and ascertainment definitions

- **Locations:** PDF-002 pp. 4, 11, and 23-24; PDF-003 p. 7.
- **Main key:** `MP-PRIMARY-SAE`.
- **Core definition:** an SAE is an unintended injury/complication caused by healthcare management resulting in escalation of care, disability at discharge, death, prolonged hospital stay, or subsequent hospital admission. The ascertainment period is enrollment through 10 months post-enrollment.
- **Table 3/appendix event set:** death; ECMO; cardiac arrest; CPR; hypotension treated with vasoactive drugs; apnea treated with increased respiratory support; local/regional anesthetic toxicity; prolonged intubation/ventilation (`>48` hours postoperation, for those not ventilated preoperation); unplanned reintubation; intraoperative unplanned extubation; IH incarceration/strangulation/recurrence; reoperation; adjacent-organ injury; deep wound disruption; deep SSI within 30 days plus a listed criterion; and other SAE requiring intervention. Harm is assigned for infants with at least one SAE using NCC MERP categories E-I.
- **Reliability/monitoring quantities:** random 10% inter-coordinator reliability assessment; post-operative direct questioning from operation start to 24 hours post-operation; interaction about 5 minutes.

### N-SUP-007 — Protocol interim stopping, accrual, and changes

- **Locations:** PDF-002 pp. 14-15 and 25; PDF-003 p. 4.
- **Main keys:** `MP-TRIAL-POPULATION`; `MP-PRIMARY-SAE`; `MP-HOSPITAL-DAYS`.
- **Plan:** approximately 200 infants with 10-month data for interim assessment. Safety outcomes: death and prolonged hospital stay `>30` days post-surgery; stopping for probability of increased harm `>90%` in either arm. Efficacy stopping: probability of decreased SAEs `>95%` in either arm. Neutral prior describes 50:50 a priori likelihood.
- **Accrual:** 240 randomized/year in years 1 and 2, then 120 in first half of year 3; site corrective action if below 40% randomization among eligible infants at six months; notification to families/providers `<8` weeks after results available.
- **Version 7 (2019):** replaces two interim safety analyses at 33% and 66% enrollment with December 2019 safety/efficacy analysis at approximately 200 infants and adds final Bayesian primary/major-secondary analysis.

### N-SUP-008 — SAP purpose, treatment definition, sample-size timing, and explicit protocol clarification

- **Locations:** [PDF-003 pp. 2-4](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=2>).
- **Main keys:** `MP-PRIMARY-SAE`; `MP-HOSPITAL-DAYS`; `MP-TRIAL-POPULATION`.
- **SAP primary endpoint:** infants with at least one SAE from enrollment to 10 months; trial is 1:1 early/late, site- and GA-stratified. Early: before discharge, approximately 38 weeks PMA. Late: after discharge and over 55 weeks PMA, typically about 5 months after discharge.
- **Sample size/interim result:** 293/group, 586 total, planned 615 allowing follow-up; April 2021 enrolment stopped after interim analysis found 97% probability of decreased SAE rate in late group, crossing pre-specified 95% efficacy threshold.
- **Printed SAP clarification, retained for later comparison:** secondary hospital-day hypothesis is 8 early versus 5 late (3 days), and the SAP states that the original final protocol page 3 printed 18 early versus 15 late, “which is incorrect”; it says the correct values were on final protocol page 12. This is a source-linked relationship, not an adjudication in this map.

### N-SUP-009 — SAP analysis populations, outcomes, and summaries

- **Locations:** PDF-003 pp. 5-8.
- **Main keys:** `MP-TRIAL-POPULATION`, `MP-PRIMARY-SAE`, `MP-HOSPITAL-DAYS`, `MP-NEURODEVELOPMENT`.
- **mITT:** all randomized infants with an ascertained primary outcome. **PP:** received randomized early/late intervention and has a determined primary outcome.
- **Baseline summaries:** categorical variables as number/percentage; continuous as mean/SD/range if normal and median/IQR/range if skewed.
- **Outcome definitions:** primary is any SAE to 10 months. Secondary includes highest NCC MERP harm level, total hospital days (randomization-to-discharge + readmission + postsurgery days), prolonged stay `>30` days postsurgery, NICU and postsurgery LOS, IH repair occurrence, BSID-III cognitive score, and any AE rate.

### N-SUP-010 — SAP sensitivity, subgroup, and missing-data definitions

- **Locations:** [PDF-003 pp. 9-10](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=9>).
- **Main keys:** `MP-PRIMARY-SAE`; `MP-HOSPITAL-DAYS`; `MP-NEURODEVELOPMENT`.
- **Sensitivity:** mITT primary analysis additionally adjusts for important imbalanced baseline covariates; PP primary analysis also occurs.
- **Subgroups:** mITT primary and major-secondary treatment-effect modifiers: GA (`<28`/`>28` weeks), BPD, maternal education `<12` years, prenatal care, difficult-to-reduce IH, gender, race/ethnicity; additional exploratory laparoscopic versus open repair and distance from facility. Subgroup results are to supply point estimates, 95% credible intervals, and benefit/harm probabilities.
- **GA association:** continuous GA with spline/polynomial; interaction with final GA term and intervention for primary outcome. **Missing data:** no imputation.

### N-SUP-011 — eTable 1: ineligible and non-consented enrollment counts

- **Locations:** [PDF-004 pp. 2-4](<../../../joi240020supp3_prod_1710443209.75411.pdf#page=2>), direct visual confirmation.
- **Main key:** `MP-TRIAL-POPULATION`.
- **Site-level ineligible due to associated factor affecting timing:** incarceration 10; multiple prior abdominal operations 5; severe respiratory disease 5; ovary/preferred early 4; severe cardiac disease 4; airway anomaly requiring operation 2; contacted too close to anticipated discharge 2; undescended testicle 2; viral URI 2; COVID restriction 2; transfer closer to home/nonparticipating site 2; anticoagulant 1; very large hernia/preferred early 1; too small 1; uncertain hydrocele/hernia 1; coordinate ophthalmology 1; coordinate neurosurgery 1; planning G-tube 1; severe pulmonary hypertension 1; unexplained thrombocytopenia 1; await steroid discontinuation 1; feeding intolerance 1.
- **Parent/guardian refusal (`n=613`):** early 280; late 196; physician timing 71; no reason 66 (sum 613). **Physician refusal (`n=37`):** early 14; late 14; no reason 9 (sum 37). **Other eligible/not consented (`n=16`):** non-English/English-only forms 4; COVID 4; custody 3; incarceration concern in NICU 2; insurance 1; medically unstable 1; cardiac-surgery transfer 1 (sum 16).

### N-SUP-012 — eTable 2: frequentist primary and major secondary results

- **Location:** [PDF-004 p. 5](<../../../joi240020supp3_prod_1710443209.75411.pdf#page=5>), direct visual confirmation.
- **Main keys:** `MP-PRIMARY-SAE`; `MP-HOSPITAL-DAYS`.
- **Primary outcome, infant had at least one SAE:** early `44/159 (28%)`; late `27/149 (18%)`; risk difference (late minus early) `-9.0% (95% CI -16.5% to -2.0%)`, `P=.01`; RR `0.65 (95% CI 0.46-0.92)`, `P=.01`.
- **Hospital days during study period, median (IQR):** early `19.0 (9.8, 35)`; late `16.0 (7, 38)`; RR `0.91 (95% CI 0.74-1.12)`, `P=.36`. The risk-difference and its P-value cells are blank for this count outcome.
- **Table footnote labels:** logistic mixed-effect model for primary outcome, negative-binomial mixed model for hospital days; all models include GA group as covariate and centre random intercept. It adds that frequentist primary analysis used GEE logistic model with exchangeable centre correlation because mixed-effect-model nonconvergence, whereas the stated frequentist/Bayesian models otherwise match.

### N-SUP-013 — eTable 3: all randomized-centre counts

- **Location:** [PDF-004 p. 6](<../../../joi240020supp3_prod_1710443209.75411.pdf#page=6>).
- **Main keys:** `MP-CENTER`; `MP-TRIAL-POPULATION`.
- **Column denominators:** early `n=172`; late `n=166`; overall `N=338`. Each row is early/late/overall count (printed percent): Akron `2/2/4`; Albany `4/2/6`; All Children’s Johns Hopkins `3/4/7`; Amplatz `5/5/10`; Arkansas `16/17/33`; Cardinal Glennon `7/5/12`; Alabama `3/3/6`; Wisconsin `2/0/2`; Memorial Hermann `7/8/15`; Cincinnati `2/0/2`; Cohen `0/1/1`; Columbia `5/5/10`; Connecticut `4/4/8`; Dartmouth `2/0/2`; Dayton `5/5/10`; Duke `11/9/20`; Erlanger `11/10/21`; Le Bonheur `8/8/16`; MUSC `7/7/14`; Nationwide `9/8/17`; Naval San Diego `1/2/3`; Penn State `0/1/1`; Rady/UCSD `1/1/2`; Seattle `1/0/1`; Shands `1/1/2`; Southern California Permanente `6/7/13`; St Louis `2/1/3`; Texas `3/1/4`; Tufts `1/2/3`; UCLA `1/2/3`; UCLA-Harbor `1/2/3`; Iowa `11/13/24`; Nebraska `0/1/1`; Virginia `3/4/7`; Utah/Primary `3/3/6`; Valley `4/2/6`; Vanderbilt `11/13/24`; Women & Children’s Buffalo `6/6/12`; Women & Infants Rhode Island `3/1/4`.
- **Population label warning:** these randomized totals (338) are not the eTable 2 analysis denominators (159+149=308); keep population/endpoint qualification when matching.

## Inferential-statistical definitions and relationships

### S-SUP-001 — Analysis framework and estimands

- **Locations:** PDF-003 pp. 4, 7-8; PDF-002 p. 13; PDF-004 p. 5.
- **Main keys:** all four primary/major-secondary keys.
- **Frequentist reporting:** RR, RD, group mean difference as applicable, with 95% CI. **Bayesian reporting:** posterior median, 95% credible interval, probabilities of benefit/harm and clinically important effect. The SAP calls Bayesian analyses primary and frequentist secondary.
- **Outcome/model labels:** binary logistic, ordinal proportional-odds logistic, count negative binomial, continuous model by outcome; GA group covariate and centre random effect. The protocol describes GLMM binomial log link for the primary outcome, lognormal hospital-day model, and linear mixed model for BSID score. Preserve these source-specific model labels rather than treating them as interchangeable.

### S-SUP-002 — eTable 2 primary SAE statistical relationship

- **Location:** PDF-004 p. 5.
- **Main key:** `MP-PRIMARY-SAE`.
- **Printed result components:** `44/159` versus `27/149`; late-minus-early RD `-9.0%`, 95% CI `-16.5% to -2.0%`, P `.01`; RR `0.65`, 95% CI `0.46-0.92`, P `.01`. Direction, reference direction, interval type, and model statement are all explicit.

### S-SUP-003 — eTable 2 hospital-day statistical relationship

- **Location:** PDF-004 p. 5.
- **Main key:** `MP-HOSPITAL-DAYS`.
- **Printed result components:** medians/IQRs `19.0 (9.8,35)` versus `16.0 (7,38)`; RR `0.91 (0.74-1.12)`, P `.36`; negative-binomial model. The table does not print an RD or a separate P-value in the RD column.

### S-SUP-004 — SAP frequentist/Bayesian computation definitions

- **Locations:** PDF-003 pp. 7-8.
- **Main keys:** `MP-PRIMARY-SAE`; `MP-HOSPITAL-DAYS`; `MP-NEURODEVELOPMENT`.
- **Effect measures:** binary outcomes report RR/RD calculated from logistic model; count outcomes RR; ordinal OR; continuous mean group difference. All outcomes have 95% CIs or 95% CrIs. Benefit/harm probabilities include any effect and at least 3%/5% SAE-risk reduction.
- **MCMC:** Stan via `rstanarm`/`brms`, three chains, at least 5,000 burn-in samples and at least 50,000 additional iterations per chain.

### S-SUP-005 — SAP priors and diagnostics

- **Locations:** PDF-003 p. 8.
- **Categorical/binary prior:** intervention log-OR Normal(mean 0, SD 0.7), stated as OR 1.0 with 95% CrI 0.2-4; count intervention prior centered RR 1.0 with 95% CrI 0.33-3.3; intercept Normal(0,10), GA Normal(0,1), random-intercept SD half-Normal(0,1).
- **Continuous prior:** intervention Normal(0,2), intercept Normal(0,10), GA Normal(0,3), random-intercept SD half-Normal(0,2).
- **Diagnostics:** frequentist residual plots; Bayesian trace plots from three chains, Geweke and Gelman/Rubin checks, and posterior predictive simulation of 1,000 trials.

### S-SUP-006 — Sensitivity and subgroup inferential plan

- **Locations:** PDF-003 p. 9; PDF-002 p. 13.
- **Primary mITT sensitivity/PP relationship:** covariate adjustment for important imbalance and separate PP analysis. The protocol’s interaction prior language is neutral `N(0,1000)`/Uniform(0,1000) for SD parameters with neutral/skeptical interactions; the SAP instead specifies Normal(0, SD 0.6) for interactions. Both are source-specific planned definitions to retain.
- **Subgroup output:** point estimates, 95% CrIs, and benefit/harm probabilities; conservative hierarchical shrinkage toward overall effect.

### S-SUP-007 — Interim inferential rule and observed stop statement

- **Locations:** PDF-002 p. 14; PDF-003 p. 4.
- **Rule:** efficacy probability decreased SAEs `>95%`; safety probability increased harm `>90%`, using Bayesian methods/neutral priors as described.
- **SAP observation:** 97% probability of decreased late-group SAE rate crossed the pre-specified 95% efficacy threshold in April 2021. This is a statistical-result occurrence for later matched-source checking, not a candidate conclusion here.

## Direct-source limitations and handoff notes

- PDF-004 reusable text was visibly corrupted; direct direct-PDF renders, not the corrupted glyphs, supplied the eTable transcriptions above.
- PDF-002 Figure 2 is a prospective blank template, so no actual CONSORT counts are available from that protocol page. This is recorded as no-applicable observed-count content, not inferred missingness.
- DOCX-001 was structurally inspected only. Its legacy candidate assertions are excluded from all scientific relationship and candidate discovery; this restriction is intentional rather than an extraction gap.
- No workbook, spreadsheet formula, cached value, CSV, DOC, or XLS/XLSX source exists in the assigned scope.
