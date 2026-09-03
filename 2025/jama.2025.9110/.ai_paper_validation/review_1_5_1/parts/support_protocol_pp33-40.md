# Support quantitative evidence map — Protocol pp. 33-40

## Scope and method

- **Source ID:** `JAMA2025_9110_D02_PROTOCOL`
- **Direct source:** `joi250040supp1_prod_1753124024.37199.pdf`
- **Assigned physical PDF pages:** 33-40 (8 of 40 pages), complete and disjoint.
- **Fresh-source requirement:** all eight pages had no reusable page derivative. Fresh `pdftotext -layout` files and 150-dpi direct PDF renders were created only in `preprocessing/protocol-002/`. The layout text has unusable font encoding. Direct rendered source pages were therefore inspected visually and are the authority. A CPU-only Tesseract attempt did not provide usable text under concurrent CPU load; this did not leave a source-coverage gap because each rendered page was directly inspected.
- **Scope boundary:** these pages are protocol references plus the start and methods of the PRO-SCAN CT-imaging sub-study. They contain prospective definitions and feasibility assumptions, not post-randomization results. No comparison with the main-paper printed result is asserted here; matching keys are supplied for cross-source matching.

## Page-by-page coverage

| PDF page | Direct-source content and coverage determination |
|---:|---|
| 33 | References 27-37 only. No result-relevant quantitative relationship on this page. |
| 34 | References 38-49 only. No result-relevant quantitative relationship on this page. |
| 35 | References 50-54; begins Appendix 4/PRO-SCAN sub-study. Records the external-background statement of an **18% decrease in quadriceps skeletal-muscle mass in the first 10 days of ICU admission**. This is not a TARGET Protein trial result. |
| 36 | PRO-SCAN background, aims, and first hypothesis. Maps external-background prevalence (60%-70%), study design key, co-primary aims, CT-derived L3 muscle cross-sectional area (CSA) measure, and sub-study hypothesis. |
| 37 | Remaining hypotheses, outcome definitions, design, and eligibility time window. Maps L3 CSA low-muscle-mass cutoffs, day-90 outcome timing, greater-than-7-day exposure definition, and CT eligibility window. |
| 38 | Study procedures, measurement definitions, data collection and prospective analysis plan. Maps subsequent-scan minimum interval, CSA calculation rule and units, observation days, competing-risks framework, random effects, robust SEs, exploratory/multiplicity statement, and planned software. |
| 39 | Feasibility/sample projection and data-management content. Maps anticipated parent recruitment, site count, CT-substudy projected counts and scan-repeat assumptions. |
| 40 | Administrative ethics/authorship content. The thresholds of 10 paired images and three contributors are authorship rules, not result-relevant quantitative relationships; no applicable result relationship. |

## Numeric/reporting relationships

| Provisional ID | Exact printed evidence and location | Relationship / definition | Matching key and mapping note |
|---|---|---|---|
| P2-N001 | p.35: “observational studies reporting a **18% decrease** in quadriceps skeletal muscle mass in the first **10 days** of ICU admission.” | External background estimate; percent change in quadriceps muscle mass over first 10 ICU days. | `PRO-SCAN; skeletal muscle mass; ICU; 10 days`. Background only, not a trial-result comparator. |
| P2-N002 | p.36: “**60-70%** of patients admitted to ICU have lower than normal muscle mass.” | External background prevalence range. | `PRO-SCAN; low muscle mass; ICU prevalence`. Background only. |
| P2-N003 | p.37: low muscle mass at ICU admission is CT-derived L3 skeletal-muscle CSA “defined as **<170 cm² for males and <110 cm² for females**.” | Sex-specific binary classification threshold; distinguish from continuous baseline CSA and later CSA change. | `PRO-SCAN; low/normal muscle mass; L3 CSA; sex-specific threshold`. |
| P2-N004 | p.37: clinical outcomes include “days alive and out of hospital at **day 90** and mortality”; secondary exposure is “greater than **7 days** of augmented dietary protein.” | Outcome time point and exposure-duration subgroup definition. | `PRO-SCAN; day-90; days alive and out of hospital; mortality`; `PRO-SCAN; >7 days augmented protein`. |
| P2-N005 | p.37: CT eligibility is from “**72 hours before** ICU admission until **48 hours after** TARGET Protein study EN was commenced.” | Image-selection time window for eligible participants. | `PRO-SCAN; CT eligibility; 72 h before ICU; 48 h after EN`. |
| P2-N006 | p.38: a subsequent CT scan must be taken a minimum of “**5 days** after the initial scan.” | Follow-up image criterion for the first co-primary outcome (change in muscle mass). | `PRO-SCAN; subsequent CT; >=5 days; muscle-mass change`. |
| P2-N007 | p.38: skeletal-muscle CSA “in **cm²** will be computed by summing the skeletal muscle tissue pixels and multiplying by the surface area of each pixel”; density is mean radiologic attenuation at L3 “measured in **HU**.” | Measurement formula and distinct scales: CSA is area; density is mean attenuation. | `PRO-SCAN; L3 CSA; cm²; pixel-area calculation`; `PRO-SCAN; L3 muscle density; HU`. |
| P2-N008 | p.38: daily nutrition data will be extracted on days “**1-5, 10, 20, 30 and 90**.” | Prespecified longitudinal data-collection schedule; values include daily nutrition, EN volume, parenteral nutrition/protein supplements, and EN start/stop times. | `PRO-SCAN; nutrition data; days 1-5/10/20/30/90`. |
| P2-N009 | pp.38-39: anticipated TARGET Protein recruitment “over **3,000** patients from **8** participating sites”; feasibility estimate **20** patients/year/site with >=1 CT gives **160** patients (**80** each group); estimated **20%** with >=2 CT scans and **5%** with >2 scans; “over **200** CT scans” anticipated. | Prospective feasibility/sample projection. Internal arithmetic: 20 × 8 = 160 and 160 / 2 = 80, both reconcile exactly. The >200 scans statement is a projection using repeat-scan assumptions, not an observed total. | `PRO-SCAN; feasibility; 3000; 8 sites; 160; 80/group; CT scans`; prospective only. |

## Statistical relationships and definitions

| Provisional ID | Exact printed evidence and location | Statistical relationship / required distinction | Matching key |
|---|---|---|---|
| P2-S001 | p.36: “large binational, multicentre, **cluster-randomised** trial”; p.37: “cluster randomised, cross-sectional, double cross-over, registry-embedded, pragmatic clinical trial.” | Design/population key. Sub-study uses a subset with routine-care CT images; preserve this distinction when matching any main-paper analysis population. | `TARGET Protein; cluster randomised; PRO-SCAN subset; CT images`. |
| P2-S002 | pp.36-37: co-primary aims are treatment effect on CT-derived L3 CSA change and effect modification/association of lower-than-normal admission muscle mass with clinical outcomes; secondary aims assess L3 density change and >7-day exposure. | Distinct estimands/outcomes: CSA change, low-muscle-mass interaction/clinical outcomes, density change, and exposure-duration analysis must not be conflated. | `PRO-SCAN; co-primary; CSA change`; `PRO-SCAN; low muscle mass; clinical outcomes`; `PRO-SCAN; L3 density`; `PRO-SCAN; >7-day exposure`. |
| P2-S003 | p.38: baseline skeletal-muscle area/clinical-outcome association assessed as continuous covariate and, depending on observed relationships, binary low/normal variable; hospital death interactions for study group with age, gender, and sepsis explored. | Prospective model specification: continuous versus binary coding is conditional on observed relationships; interaction terms are exploratory. | `PRO-SCAN; baseline CSA; continuous/binary; hospital death; age/gender/sepsis interaction`. |
| P2-S004 | p.38: for outcomes where death is competing event (duration of invasive mechanical ventilation, ICU/hospital LOS), “competing risks regression” using cumulative-incidence framework per Fine and Gray; site random effect if study numbers allow; robust-SE CIs for all models. | Competing-risk method applies to listed duration outcomes, not necessarily hospital death. Site random effect is conditional; CIs use robust standard errors. | `PRO-SCAN; Fine-Gray; competing risks; ventilation duration; ICU LOS; hospital LOS; robust SE`. |
| P2-S005 | p.38: all analyses exploratory; no adjustment for multiple comparisons; P values “provided for perspective only, rather than dichotomous statistical significance”; planned Stata/MP 17.0. | Multiplicity/P-value interpretation definition. No printed P=0 occurs in this scope, so no `DISPLAY_ZERO_NOT_CANDIDATE` record is needed. | `PRO-SCAN; exploratory; no multiplicity adjustment; P values perspective only`. |

## Candidate seeds and checks

- **Candidate seeds:** none. These pages state protocol definitions, assumptions, and reference material; no internally contradictory printed numeric, denominator, measure-label, or statistical relationship was observed within this assigned scope.
- **Arithmetic check:** P2-N009's explicit 20 per site × 8 sites = 160 and 160/2 = 80 per group reconcile.
- **DISPLAY_ZERO_NOT_CANDIDATE:** no display-zero P value in this scope.
- **Limitation for later cross-source review:** P2-N001, P2-N002, and P2-N009 are external/prospective contextual quantities, respectively, and must not be treated as observed main-trial results without an exact matched population/time/contrast. P2-S003/S004 are prospective and conditional model language, not confirmation of the analysis ultimately reported.

## Completion statement

All eight assigned physical PDF pages were directly inspected. Page coverage is complete: 2 pages with no applicable content (33-34), 1 administrative/no-applicable page (40), and 5 pages with mapped support relationships (35-39). Counts: **9 numeric/reporting relationships, 5 statistical relationships, 0 candidate seeds**.
