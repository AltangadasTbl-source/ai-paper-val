# DOC-004 SAP visual-coverage repair — PDF pages 16-48

## Repair scope and evidence handling

Directly visually inspected every assigned PDF page of `joi250072supp3_prod_1761000786.6988.pdf` (DOC-004), pp. 16-48, using the source-linked rendered locators `preprocessing/sap_results/sap_visual_16_48/page_16.png` through `page_48.png`. These are the rendered direct PDF pages (their printed internal SAP pagination is pp. 9-41). Native/OCR text is not relied on because the existing font encoding/OCR output was incomplete. This artifact records definitions and prespecified relationships only; it makes no candidate diagnosis.

**Main-paper match key:** BiB randomized comparison of budesonide plus surfactant versus surfactant alone; primary binary composite physiologic BPD or death by 36 weeks PMA; compare final analysis population, endpoint definition, timing, adjustment variables, and effect-measure label before cross-source checking.

## Numeric and reporting relationships

| ID | Exact source | Directly observed relationship / definition |
|---|---|---|
| SAPR-N001 | PDF pp. 16-17 | Randomization: consent before/after birth; infant randomized by 48 h; 1:1 allocation; stratified by NRN site and gestational age `<26 0/7` versus `>=26 0/7` weeks. Sites enrolling `<10` infants in either gestational stratum can be pooled. |
| SAPR-N002 | PDF p. 17 | Block-urn allocation probability formula is displayed: `P_iA = [lambda + min(N_i,-1,A, N_i,-1,C) - N_i,-1,A] / [2 lambda + 2 min(N_i,-1,A, N_i,-1,C) - (i-1)]`; treatment assignment is centralized through DCC/RTI. |
| SAPR-N003 | PDF pp. 18-19 | Primary lock includes all baseline data, all study-drug administrations from study start through maximum 50 h from birth, reportable AEs, reportable concurrent drug exposure through 7 days after last study dose, and GDB/hospital course through discharge/transfer/death/hospitalization up to 120 days chronological age. Long-term lock adds neurodevelopmental and respiratory survey at 22-26 months corrected age. |
| SAPR-N004 | PDF p. 21 | Flow-chart windows: consent/screening/baseline/randomization `<48 h PNA`; study drug `<50 h PNA`; inpatient collection at 7, 28, and 30 days PNA, 36 weeks PMA, 120 days PNA; follow-up 22-26 months corrected age. `X` is intended and `(X)` optional. |
| SAPR-N005 | PDF p. 22 | Analysis populations: SAF = randomized and received at least one study dose, grouped by actual treatment; ITT = all randomized, grouped by assigned arm; mITT = randomized and received at least one study dose, grouped by assigned arm; PP = treatment according to assignment and per protocol through 36 completed weeks PMA/discharge/death/transfer. One infant randomized/treated after consent declined is excluded from every analysis population. |
| SAPR-N006 | PDF p. 23 | Planning values: GDB nonsurvival to 36 weeks PMA 19% and physiologic BPD among survivors 42%, combined ~53%; target extremely preterm values 24%, 45%, combined ~58%; anticipated absolute reduction 10%, 58% to 48%. |
| SAPR-N007 | PDF p. 23, Table 5 | Sample size per arm: 80% power 406 at overall alpha .05/final .044 and 593 at overall .01/final .009; 90% 539/753; 95% 664/900. Text specifies 550/group (1100 total) by robust-Poisson simulation and 1160 total after ~5% attrition. |
| SAPR-N008 | PDF p. 24 | Treatment tables use frequency/percentage for categorical measures; continuous values use mean/SD/median/range as appropriate. All models adjust for NRN site and dichotomous GA; expected stratification maximum tolerable imbalance is 30 for 15 centers x 2 x 2 x 15; overall MTI 66; illustrative total N 1100, 550 x 33 per arm. |
| SAPR-N009 | PDF p. 25 | Primary outcome missingness expected `<5%` per arm; if exceeded, create multiple-imputation data sets, number equal to `100 × fraction missing` (minimum 10), analyze each and combine with Rubin rules. |
| SAPR-N010 | PDF pp. 26-28 | Three efficacy looks: 25%, 50%, 75% of planned infants evaluated for primary outcome or discharged/transferred. Nominal two-sided alpha values: .000015, .0030, .0183, final .0440 (Lan-DeMets/O'Brien-Fleming). Safety looks after first 40 patients (~3%) and then 25%, 50%, 75% of primary-outcome population. |
| SAPR-N011 | PDF pp. 27-28 | Conditional-power futility: recommend stop if upper limit of two-sided 80% CI for conditional power `<0.50` at 50% or `<0.30` at 75%. Table pairs interim Z=0.5 through 2.0 with conditional power/upper-limit values; examples: Z=0.5: .032/.285 at 50%, .002/.016 at 75%; Z=1.0: .198/.668 and .043/.164; Z=2.0: .875/.993 and .723/.908. |
| SAPR-N012 | PDF p. 29 | Only primary outcome is formal hypothesis-tested; secondary analyses are descriptive with 95% CIs. Prespecified heterogeneity factors: NRN site/center, GA group, race, sex; interaction p value `<.1` is a suggested signal, not a stand-alone result. Primary/secondary 36-week assessments may occur to 37 weeks PMA; long-term 22-26 months CA may use 18-30 months corrected age. |
| SAPR-N013 | PDF p. 30 | Disposition summarizes randomized, drug received, NRN status, primary assessment at 36 weeks PMA, and 2-year follow-up. Study drug: one or two doses; first dose within 48 h, optional second `<50 h`; expected outside-delivery-room surfactant percentages are 30% within first 24 h and 10% after 24 h. A dose within 10% of expected dose is per protocol. |
| SAPR-N014 | PDF pp. 32-34 | Primary composite is binary at 36 weeks PMA: `1` death before 36 weeks PMA or alive with physiologic BPD; `0` alive and confirmed negative for physiologic BPD. Secondary death and physiologic BPD are binary. Jensen BPD severity is ordinal: 0 no BPD, 1 grade 1/mild, 2 grade 2/moderate, 3 grade 3/severe; grade 3 separately binary. |
| SAPR-N015 | PDF pp. 33-34 | Postnatal-steroid use: any steroid for evolving BPD/CLD from day 7 through 36 weeks PMA. Severe NDI at 22-26 months CA is binary and requires at least one of: Bayley-III cognitive <70, Bayley-III motor <70, GMFCS level 4-5, hearing impairment despite amplification, severe vision impairment/blindness `<20/200`; composite severe NDI/death is binary. |
| SAPR-N016 | PDF pp. 34-36 | Exploratory NIH-consensus BPD severity uses respiratory status at 28 days or later; invasive-ventilation days are counts at 28 days and 36 weeks PMA; post-window intubation/reintubation is binary, defined by >50 h PNA; open-label surfactant is binary through 7 days after last study drug; recurrent wheezing and chronic coughing are binary at 22-26 months CA. |
| SAPR-N017 | PDF p. 36 | Primary robust-Poisson model has log link for expected binary outcome; response is BPD/death, predictors include treatment (surfactant+budesonide versus surfactant alone), GA stratum and NRN site. |
| SAPR-N018 | PDF pp. 39-40 | Secondary dichotomous components are robust Poisson with site/GA fixed effects; ordinal BPD uses proportional odds (otherwise generalized logit); count outcomes use Poisson, possible zero-inflated model, or linear model if distribution warrants. Safety analysis is SAF/as-treated and descriptive. |
| SAPR-N019 | PDF pp. 40-42 | Reportable AE window: study-drug start through 7 days after last dose. Any AE is binary through 30 days post-treatment. Prespecified binary AEs include early sepsis `<=72 h PNA`, late sepsis `>72 h PNA` through 7 days, hyperglycemia, hypertension, hypotension, prolonged hypoxemia/bradycardia (>=30 seconds), ETT blockage, pulmonary air leak, intracranial hemorrhage (3-day grace), other AE, SIP without NEC, and PVL. |
| SAPR-N020 | PDF pp. 42-44 | SAE definition includes death, prolonged hospitalization, persistent/significant disability/incapacity, medical/surgical intervention to prevent these, or life-threatening condition. Clinical outcomes include death in hospital by 120 days, NEC stage >=2, PDA and its medical/surgical management, ROP stage 3, and composites; Kaplan-Meier time to in-hospital death is planned. Growth at 36 weeks PMA: weight/length/head circumference <10th percentile and Z scores. |
| SAPR-N021 | PDF p. 45 | Reporting: mean/SD at one more significant digit than precision; median/ordinal statistics to original precision; test statistics to two decimals; P values to three decimals if >.001 and `<.001` if less; report p<.05 rather than `p=.05`; round only after analysis, with digit 5 rounding up. |
| SAPR-N022 | PDF p. 48 | Potential displays include subject eligibility/disposition/exposure/baseline, primary overall and GA-stratum efficacy, secondary outcomes, AE/SAE/mortality/clinical/growth tables, CONSORT diagram, AE forest plot, and Kaplan-Meier curves; no data listings. |

## Statistical relationships

| ID | Exact source | Definition / cross-source check anchor |
|---|---|---|
| SAPR-S001 | PDF pp. 24, 36-37 | Primary ITT estimand is covariate-adjusted relative risk from log-link robust Poisson with sandwich variance, adjusted for site and dichotomous GA. Final article should not be compared as an unadjusted RR unless population/model match. |
| SAPR-S002 | PDF p. 37 | Primary null is no effect on probability of BPD/death; two-sided type-I error .05 with interim multiplicity adjustment. SAS code requests `DIST=POISSON LINK=LOG`, estimates treatment RR and CI. |
| SAPR-S003 | PDF pp. 38-39 | Prespecified secondary analyses: PP and SAF/as-treated repetition; baseline covariate adjustment sensitivity; imputation sensitivity under MAR; no further missing-data analysis if negligible. |
| SAPR-S004 | PDF pp. 26, 28 | Safety interim analysis uses robust Poisson, site/GA adjustment, possible pooled sites, GLMM random site or GEE cluster structure; repeated safety tests alpha-spent by Lan-DeMets/Pocock boundary. |
| SAPR-S005 | PDF pp. 26-28 | Efficacy interim ITT analysis repeats primary robust-Poisson model with GA/site adjustment; information time is based on primary-outcome evaluation/discharge/transfer, not merely enrollment. |
| SAPR-S006 | PDF pp. 27-28 | Futility conditional-power equation explicitly uses interim fraction `f`, standard-normal quantiles, and an upper limit based on two-sided 80% CI; rules are planning criteria, not final efficacy thresholds. |
| SAPR-S007 | PDF p. 29 | Multiplicity: only primary endpoint formal; secondary results descriptive/exploratory. Subgroup interaction p<.1 is a screening signal under stated model, not confirmation. |
| SAPR-S008 | PDF pp. 39-40 | Outcome-type model map: binary robust Poisson; ordinal proportional odds/generalized logit; nominal generalized logit; count Poisson/zero-inflated/linear as appropriate. |
| SAPR-S009 | PDF p. 43 | Time-to-death uses Kaplan-Meier with censoring at GDB status; time to death also summarized by median/range. |
| SAPR-S010 | PDF p. 45 | SAP rounding/P-value conventions are display rules; a coherent p-value display below .001 is not a contradiction by itself. |

## Explicit visual page coverage

| PDF page | Direct visual determination |
|---:|---|
| 16 | COMPLETE — consent/randomization timing and kit allocation operational rules; SAPR-N001. |
| 17 | COMPLETE — stratified 1:1 block-urn design and displayed allocation formula; SAPR-N001-N002. |
| 18 | COMPLETE — masking and primary data-lock purpose; SAPR-N003. |
| 19 | COMPLETE — primary/long-term lock data components and 22-26-month follow-up; SAPR-N003. |
| 20 | COMPLETE — data-lock/unmasking continuation; no additional quantitative relationship. |
| 21 | COMPLETE — assessment-flow table/windows; SAPR-N004. |
| 22 | COMPLETE — flow-table footnotes and SAF/ITT/mITT/PP definitions; SAPR-N005. |
| 23 | COMPLETE — planning event rates and sample-size table; SAPR-N006-N007. |
| 24 | COMPLETE — stratification MTI and general statistical rules; SAPR-N008. |
| 25 | COMPLETE — missing-data rule and interim-monitoring introduction; SAPR-N009. |
| 26 | COMPLETE — safety and efficacy interim timing/alpha plan; SAPR-N010. |
| 27 | COMPLETE — conditional-power futility equation/table start; SAPR-N011. |
| 28 | COMPLETE — futility table continuation and center count; SAPR-N011. |
| 29 | COMPLETE — multiplicity, subgroup, assessment-window definitions; SAPR-N012. |
| 30 | COMPLETE — disposition/exposure windows and expected percentages; SAPR-N013. |
| 31 | COMPLETE — baseline summaries and efficacy-analysis table introduction; no additional definition beyond SAPR-N013. |
| 32 | COMPLETE — primary composite/death/physiologic-BPD definitions; SAPR-N014. |
| 33 | COMPLETE — BPD grade/steroid/NDI definitions; SAPR-N014-N015. |
| 34 | COMPLETE — NDI/death composite and exploratory BPD definition; SAPR-N015-N016. |
| 35 | COMPLETE — ventilation/intubation/open-label-surfactant definitions; SAPR-N016. |
| 36 | COMPLETE — wheezing/cough and robust-Poisson primary model; SAPR-N016-N017. |
| 37 | COMPLETE — primary hypothesis, model parameters/code and pooling contingency; SAPR-S001-S002. |
| 38 | COMPLETE — PP/SAF, covariate and missing-data sensitivities; SAPR-S003. |
| 39 | COMPLETE — secondary outcome analysis model map; SAPR-N018/SAPR-S008. |
| 40 | COMPLETE — safety analysis and AE definitions/table start; SAPR-N019. |
| 41 | COMPLETE — prespecified AE table definitions; SAPR-N019. |
| 42 | COMPLETE — AE table continuation and SAE definition; SAPR-N019-N020. |
| 43 | COMPLETE — clinical/growth outcomes and time-to-event plan; SAPR-N020/SAPR-S009. |
| 44 | COMPLETE — growth impairment outcomes and Z scores; SAPR-N020. |
| 45 | COMPLETE — reporting precision/P-value conventions; SAPR-N021/SAPR-S010. |
| 46 | COMPLETE — references only; no applicable result relationship. |
| 47 | COMPLETE — references only; no applicable result relationship. |
| 48 | COMPLETE — potential display inventory; SAPR-N022. |

## Limitations

This SAP is prespecified (version 1.3 dated 2024-09-10), so it is a definition/model comparator and not proof that final results must be identical. Any difference requires checking documented amendments, final analysis set, and the final article's exact reported model. All assigned pages were visually inspected from source-linked renders because text-layer/OCR output was unreliable.
