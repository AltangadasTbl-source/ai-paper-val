# Global Inferential-Statistical Relationship Inventory

Stable global IDs are assigned in deterministic source/page/shard order. Each entry preserves its mapper-local provenance and full mapped evidence. Every relationship has status `PASS_1_COMPLETE` and `PASS_2_COMPLETE` in the two distinct statistical checker artifacts.

## S001 — Sample-size statistical plan

- **Mapper-local relationship:** M-S001
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location:** PDF p. 3.
- **Direct observation:** `90%` power, two-sided alpha `5%`, planned `18%` versus `8%` abstinence, ICC `0.02`, design effect `1.5`, 20% attrition.
- **Rule candidate:** planning computation can only be assessed with stated cluster-size/design-effect/attrition conventions; map separately from observed effect estimates.


## S002 — Analysis methods and stated decision convention

- **Mapper-local relationship:** M-S002
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location:** PDF p. 3 Statistical Analysis.
- **Direct observation:** mixed-effects categorical models include intervention fixed effect and post-hoc covariates age, sex, education, occupation, smoking duration with cluster random effects; logistic regression, Bayesian hierarchical logistic model (brms) with 95% credible intervals, ICC from lme4 mixed-effects logistic variance components; death compared by Cox proportional-hazards frailty model adjusting site-level clustering; secondary outcomes exploratory and no multiple-comparison adjustment; analyses two-sided and `P<.05` statistically significant.
- **Rule candidate:** comparisons of reported RR/HR/ICC must retain model, adjustment, analysis set, and interval type (confidence versus credible) distinctions.


## S003 — Primary ITT verified abstinence effect

- **Mapper-local relationship:** M-S003
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Locations / match key:** PDF pp. 1, 4, 6; `ITT-primary-abstinence|month-6|CO<10ppm`.
- **Direct observation:** RR `3.0 (95% CI, 2.0-4.9)`, primary proportions `41.7%` versus `15.3%`, counts `300/720` versus `55/360`, absolute difference `26.4 (21.0-31.6)`, ICC `0.18`.
- **Rule candidate:** match effect estimate to the CO <10 ppm ITT result; inspect point estimate/CI ordering and narrative/table/abstract identity.


## S004 — Primary adjusted and CO-threshold sensitivity effects

- **Mapper-local relationship:** M-S004
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Locations:** PDF pp. 4 and 6.
- **Direct observation:** adjusted primary RR `3.2 (2.2-5.2)`, ICC `0.18`; CO <6 ppm ITT crude RR `3.7 (2.4-5.8)`, ICC `0.16`, adjusted RR `3.9 (2.4-6.9)`, ICC `0.18`; CO <6 ppm PP crude RR `3.6 (2.14-6.87)`, ICC `0.17`, adjusted RR `3.8 (2.3-7.7)`, ICC `0.18`.
- **Rule candidate:** threshold, ITT/PP status, and adjustment are necessary match fields; confidence intervals should contain their printed point estimate.


## S005 — Primary PP verified abstinence effect

- **Mapper-local relationship:** M-S005
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location:** PDF p. 6 Table 2.
- **Direct observation:** CO <10 ppm PP crude RR `2.9 (2.0-4.7)`, ICC `0.19`; adjusted RR `3.1 (2.1-5.2)`, ICC `0.19`; counts `300/667` versus `55/318`.
- **Rule candidate:** denominator linkage to Figure 1 non-loss counts and interval containment, preserving PP label.


## S006 — Self-reported-only continuous abstinence effect

- **Mapper-local relationship:** M-S006
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location:** PDF p. 6 Table 2.
- **Direct observation:** crude RR `2.7 (1.8-4.1)`, ICC `0.19`; adjusted RR `2.8 (1.9-42)`, ICC `0.19`; counts `342/720` versus `70/360`; absolute difference `28.1 (22.6-33.5)`.
- **Rule candidate:** check CI containment and label/scale; record that `42` is source-printed and direct-render confirmed (M-N018).


## S007 — Point-abstinence effects

- **Mapper-local relationship:** M-S007
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location:** PDF p. 6 Table 2.
- **Direct observation:** week 9 crude RR `2.6 (1.8-3.9)`, ICC `0.19`; adjusted `2.7 (1.8-4.3)`, ICC `0.18`. Month 6 crude RR `2.7 (2.0-3.8)`, ICC `0.19`; adjusted `2.7 (1.9-4.0)`, ICC `0.19`.
- **Rule candidate:** match last-7-day timepoint and ITT label; assess CI containment/ordering and crude-versus-adjusted field identity.


## S008 — TB-treatment-success effects

- **Mapper-local relationship:** M-S008
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Locations:** PDF pp. 1, 5, 6.
- **Direct observation:** crude RR `1.2 (0.9-1.6)`, ICC `0.16`; adjusted RR `1.2 (0.9-1.5)`, ICC `0.15`; counts/proportions `643/720, 89.3%` versus `308/360, 85.6%`; absolute difference `3.8 (-0.5 to 8.2)`.
- **Rule candidate:** match treatment-success definition (`cured + completed`) and RR model; inspect CI containment and cross-occurrence identity.


## S009 — Mortality/death survival-model relationship

- **Mapper-local relationship:** M-S009
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Locations:** PDF pp. 1, 5, 6.
- **Direct observation:** death `25/720, 3.5% (2.2-5.0)` mHealth versus `27/360, 7.5% (5.0-10.7)` usual care; absolute difference `4 (1.0-7.1)`; adjusted HR `0.4 (0.2-0.9)` using shared-frailty Cox model; no crude RR/ICC reported (NA).
- **Rule candidate:** distinguish a risk/proportion difference from a Cox HR and preserve the table’s unnamed absolute-difference direction convention.


## S010 — Default and treatment-failure low-event rows

- **Mapper-local relationship:** M-S010
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location:** PDF p. 6 Table 2.
- **Direct observation:** default and failure have NA in crude RR, crude ICC, adjusted RR/HR, and adjusted ICC columns; footnote attributes inability to estimate mixed-effects models to very low event numbers across clusters. Default counts `22/720` versus `7/360`; failure `1/720` versus `2/360`.
- **Rule candidate:** verify NA is consistent with the stated low-event model limitation and avoid treating NA as a zero effect estimate.


## S011 — Adherence comparison P value

- **Mapper-local relationship:** M-S011
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Locations:** PDF pp. 1 and 5.
- **Direct observation:** mean adherence `174.3 (SD 21.5)` versus `178.0 (SD 12.1)` days; `P=.23`.
- **Rule candidate:** no test statistic, SE, exact test, or CI is printed in DOC-001. Retain the P value as an unpaired reported inferential value; do not infer a compatibility calculation without the missing inputs.


## S012 — Bayesian cluster-model result

- **Mapper-local relationship:** M-S012
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Locations:** PDF pp. 4 and 7.
- **Direct observation:** Bayesian hierarchical model showed heterogeneity of cluster quitting probabilities, with generally higher fitted rates in mHealth; figure presents posterior means and 95% credible-interval whiskers, no printed numeric values.
- **Rule candidate:** check label consistency (credible, not confidence, intervals) and graphical claims only; no exact interval arithmetic can be reproduced from the figure.


## S013 — Results/discussion qualitative inferential wording

- **Mapper-local relationship:** M-S013
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Locations:** PDF pp. 4-5, 8.
- **Direct observation:** primary association described as persisting after covariate adjustment; CO <6 sensitivity described as consistent/robust; point abstinence higher; adherence similar; death probability significantly higher in usual care; observed ICC `0.19` described as higher than planned `0.02` while primary effect remained statistically significant.
- **Rule candidate:** narrative interpretation should be matched to the appropriate result/model/threshold. “Significantly” has an explicit paper convention of two-sided P<.05 but no death P value is printed in DOC-001.


## S014 — Display-zero check

- **Mapper-local relationship:** M-S014
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Scope result:** No `P=0`, `p=0.000`, or equivalent display-zero P value appears in DOC-001 pp. 1-9.
- **Direct observation:** The sole explicit p value in the main-paper result narrative is `P=.23` for adherence.

## Mapping limitations

- Figure 2 supplies graphical marks and exact cluster follow-up sizes but not printed numerical posterior means, observed proportions, or credible-interval endpoints; this map does not estimate plotted values.
- Main-paper narrative directs some detailed evidence to Supplement 2 (eTables/eFigure); those exact supplement records are intentionally outside this DOC-001-only shard.
- Direct PDF text on p. 6 and direct image rendering agree that the adjusted self-reported-only interval endpoint is printed as `42`; this map preserves that exact source value without deciding its meaning.

## Counts

- Numeric/reporting relationships: **20** (`M-N001`-`M-N020`).
- Inferential-statistical relationships: **14** (`M-S001`-`M-S014`).
- PDF coverage: **9/9 pages complete**; one no-applicable-results reference page (PDF p. 9).
# Support Quantitative Evidence Map — DOC-002, PDF pp. 1-32

## Scope and evidence method

**Direct source:** `joi250093supp1_prod_1768590553.08963.pdf`, PDF pp. 1-32 (printed protocol pages: cover/contents, then pp. 2-32 as displayed). All 32 assigned PDF pages were visually inspected from the current-run 180-dpi renders under `preprocessing/DOC-002/page_images/`; the cited PDF page is the authoritative source location. Native/layout extraction was unusable due to font-encoding garble. Tesseract was not used because the assigned run established it was nonresponsive.

This is an evidence map, not a candidate assessment. “Direct observation” transcribes or summarizes what is visibly printed; “calculation/check key” states only a supplied-source-grounded reconciliation or matching rule for downstream review. No C IDs or adjudications are made here.

## Per-page coverage

| PDF page | Printed content / coverage disposition | Result-relevant quantitative content mapped |
|---:|---|---|
| 1 | Supplement 1 table of contents | No applicable result relationship; identifies protocol/SAP components. |
| 2 | Earlier protocol v4.0 cover | Version/date 19 April 2023; administrative context only. |
| 3 | Earlier-protocol contents, part 1 | No applicable result relationship; contents include sample size/statistics sections. |
| 4 | Earlier-protocol contents, part 2 | No applicable result relationship; contents include sample size/statistics sections. |
| 5 | Earlier-protocol contents, part 3 | No applicable result relationship; contents include sample size/statistics sections. |
| 6 | Latest protocol v6.0 abbreviations | No applicable result relationship. |
| 7 | Latest protocol introduction/rationale | N001. |
| 8 | Objectives and endpoints | N002-N004. |
| 9 | Secondary-endpoint definitions and design | N005, S001. |
| 10 | Country table and sample-size paragraph | N006-N007; S002-S003. |
| 11 | Eligibility/exclusion criteria | N008. |
| 12 | Enrolment and consent | N009. |
| 13 | Withdrawal, randomisation, allocation-flow start | N010-N011. |
| 14 | Allocation-flow continuation | N011. |
| 15 | Intervention A and pilot | N012-N013. |
| 16 | Intervention A delivery schedule; intervention B | N014. |
| 17 | Intervention B/C and assessment schedule table | N015. |
| 18 | Visit-window rules and data collection | N016. |
| 19 | Data collection/source documentation | N017. |
| 20 | Data retention/case-report/data management | N018. |
| 21 | Direct data access/data entry | No additional result relationship; data-management context. |
| 22 | Data storage | N019. |
| 23 | QA/training table | No applicable result relationship. |
| 24 | CO/cotinine QA and data monitoring | No additional numeric/statistical result relationship. |
| 25 | Monitoring/direct access | No applicable result relationship. |
| 26 | Statistics and data analysis/sample-size calculation | N020; S004-S005. |
| 27 | Cost-effectiveness analysis | N021; S006. |
| 28 | Statistical analysis/sample handling | S007. |
| 29 | Translation/adverse events/audit | N022. |
| 30 | Committee/collaborators | N023. |
| 31 | Collaborators/GCP | No additional result relationship. |
| 32 | PI responsibilities/informed consent/site staff | No applicable result relationship. |

## Numeric/reporting relationships


## S015 — Trial type, superiority/non-inferiority contrast

- **Mapper-local relationship:** A-S001
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 9 labels Phase 3 superiority (A vs C) and Phase 4 non-inferiority (A vs B); each has 12-month duration, composed of 6-month recruitment and 6-month follow-up.
- **Definition/check key:** Do not compare or pool phase results without retaining the different inferential objective and comparator.


## S016 — Phase-3 power and effect assumptions

- **Mapper-local relationship:** A-S002
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 10 specifies 90% power at 5% significance for Phase 3, 16 A versus 8 C clusters, and assumed 6-month abstinence proportions 18% versus 8%.
- **Definition/check key:** This is a design/power assumption. It is not an observed RR, CI, P value, or participant-level analysis result.


## S017 — Phase-4 non-inferiority design assumption

- **Mapper-local relationship:** A-S003
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 10 specifies Phase 4 90% power at a one-sided 2.5% level, 20 clusters each in A and B, 18% face-to-face abstinence at 6 months, and 8% non-inferiority margin; source explains the margin preserves at least 50% of the 16-percentage-point established effect.
- **Definition/check key:** Retain one-sided alpha, margin scale (absolute percentage points as printed), reference arm, and preservation rule before any compatibility check.


## S018 — Repeated power specification

- **Mapper-local relationship:** A-S004
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 26 repeats the Phase-3 and Phase-4 power, alpha, assumed abstinence, cluster allocation, non-inferiority margin, and preservation parameters in A-S002/A-S003.
- **Definition/check key:** Match this text to the same design relationships while preserving the N020 44/48-facility wording difference for separate verification.


## S019 — Planned primary outcome model and effect measure

- **Mapper-local relationship:** A-S005
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 28 says outcomes will primarily use a missing-at-random architecture: generalized linear mixed models with log link and underlying Poisson distribution, clusters as random effect/random intercept; analyses account for clustering; crude and adjusted relative risks (RRs) and corresponding 95% CIs will be estimated.
- **Definition/check key:** Compatible result matching requires RR (not odds ratio), stated crude/adjusted status, 95% CI, random-intercept cluster handling, and missing-at-random model context.


## S020 — Cost-effectiveness uncertainty plan

- **Mapper-local relationship:** A-S006
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 27 specifies non-parametric bootstrap resampling, 5,000 replications, 95% ICER confidence intervals, and CEACs estimating probability cost-effective at varying one-QALY thresholds. It additionally specifies complete-case analysis for participants with complete costs/QALYs at all time points and pattern-mixture sensitivity analyses for multiple-imputation assumptions.
- **Definition/check key:** These are analytic methods/sensitivity definitions. Do not treat a future ICER CI or CEAC probability as supplied unless an observed result location is also present.


## S021 — Missing-data and analysis-unit rules

- **Mapper-local relationship:** A-S007
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Direct observation:** PDF p. 28 assigns the primary outcome analyses to missing-at-random GLMMs (A-S005); PDF p. 27 provides complete-case and pattern-mixture sensitivity analyses for economic outcomes. Cluster is the randomisation/analysis clustering unit, with individual participants supplying outcomes.
- **Definition/check key:** Only compare a reported analysis after aligning outcome domain (clinical vs economic), missing-data strategy, cluster adjustment, population, comparator, and time point.

## Direct PDF cross-occurrence index for downstream matching

| Key | PDF pages | Exact repeated/linked content |
|---|---|---|
| Sample-size plan | 10, 26 | Same 2,384 total; Phase-3/Phase-4 allocations, power, alpha, abstinence assumptions, margin, natural-cessation/effect/preservation calculations. Facility wording differs: 44 on p. 10; 48 on p. 26. |
| Allocation/recruitment plan | 10, 13-14, 26 | 2,384 total; 16 A/8 C clusters in Phase 3 and 20/20 A/B Phase 4; flow diagram supplies 24/40-site and 904/1,480-patient components. |
| Primary abstinence timing/definition | 8, 10, 26, 28 | Month-6 cessation endpoint definition on p. 8; 6-month design assumptions pp. 10/26; planned RR/CI model p. 28. |
| Economic analysis | 17-19, 27 | Economic data collection schedule and sources pp. 17-19; EQ-5D-5L/QALY/ICER/bootstrap methods p. 27. |

## Limitations

This shard is limited to DOC-002 PDF pp. 1-32. It maps a protocol/SAP source containing planned definitions, design assumptions, and analysis methods rather than observed paper results. It does not inspect DOC-002 pp. 33-109, the main paper, DOC-003, legacy review outputs, or external sources.
# Support Quantitative Evidence Map — DOC-002 PDF pp. 33-64

## Scope and method

- **Direct source:** `joi250093supp1_prod_1768590553.08963.pdf` (DOC-002), PDF pages 33-64.
- **Authority and fresh inspection:** the direct PDF was visually inspected page by page using the freshly rendered 180-dpi JPEGs `review_1_5_1/preprocessing/DOC-002/page_images/page-033.jpg` through `page-064.jpg`. The displayed PDF page number changes within this assigned PDF range: PDF pp. 33-40 are printed pp. 33-40 of a preceding protocol; PDF p. 41 begins a later protocol, whose printed pages run 0-23 across PDF pp. 41-64.
- **Extraction limitation:** native/layout text is font-encoding garble. Tesseract was reported nonresponsive and was not awaited or used. All transcribed values below come from the page images/direct PDF visual authority.
- **Nature of this evidence:** these pages are prospective protocol material, not observed main-study results. `B-` identifiers are local relationship IDs only; they are not candidate IDs or adjudications.
- **Main-paper matching keys for later cross-source review:** Quit4TB; mTB-Tobacco; cluster randomized trial; Bangladesh/Pakistan; Phase 3 superiority (intervention A vs usual care/control C); Phase 4 non-inferiority (intervention A vs face-to-face behavioural support B); continuous abstinence / biochemically verified abstinence at 6 months; week 9; 6 months; planned N/cluster counts and allocation.

## Page-by-page coverage

| PDF page | Printed page | Coverage result |
|---:|---:|---|
| 33 | 33 | Administrative/data-protection training and confidentiality; no result-relevant quantitative relationship. |
| 34 | 34 | Protocol deviation, retention, and end-of-study administrative timings (3 months, 3 days, 24 hours, 3 years, 90/15 days); no trial result or statistical relationship. |
| 35 | 35 | Administrative reporting timings (1 year) and insurance; no result-relevant relationship. |
| 36 | 36 | Stakeholder engagement; no result-relevant quantitative relationship. |
| 37 | 37 | Publication/authorship administrative timings (5 years, 30 days, 3 months); no result-relevant relationship. |
| 38 | 38 | Authorship policy; no result-relevant quantitative relationship. |
| 39 | 39 | References 1-10; no protocol result-relevant relationship. |
| 40 | 40 | References 11-17; no protocol result-relevant relationship. |
| 41 | 0 | Later protocol cover/identity, version 6.0 dated 7 March 2025; no outcome relationship. |
| 42 | 1 | Contents, including sections locating endpoints, sample size, and statistics; no standalone quantitative relationship. |
| 43 | 2 | Contents continuation; no standalone quantitative relationship. |
| 44 | 3 | Abbreviation table; no result-relevant quantitative relationship. |
| 45 | 5 | Background burden/effect statements and primary objective; mapped as contextual quantitative claims in B-N001. |
| 46 | 6 | Primary/secondary endpoint definitions; design, country table, and high-level sample-size/power assumptions; B-N002 through B-S003. |
| 47 | 7 | Inclusion/exclusion thresholds; B-N004. |
| 48 | 8 | Participant selection; consent and travel reimbursement values; B-N005. |
| 49 | 9 | Withdrawal rules and cluster allocation ratio/variables; B-N006. |
| 50 | 10 | Diagram 1, Phase 3 and Phase 4 recruitment/allocation counts; B-N007. |
| 51 | 11 | Intervention A/PPI and pilot N; B-N008. |
| 52 | 12 | Intervention A message dose/schedule and Phase 2 pilot; B-N009. |
| 53 | 13 | Intervention B session durations/times; assessment schedule; B-N010-B-N011. |
| 54 | 14 | Assessment schedule continuation, visit windows, TAM sampling narrative/table; B-N012-B-N014. |
| 55 | 15 | Data collection instrument scale; B-N015. |
| 56 | 16 | Data retention and case-report-form provisions; no result-relevant quantitative relationship beyond longitudinal data context. |
| 57 | 17 | Data handling; no result-relevant quantitative relationship. |
| 58 | 18 | Data storage/retention; no result-relevant quantitative relationship. |
| 59 | 19 | QA/data monitoring procedures; no result-relevant quantitative relationship. |
| 60 | 20 | Monitoring schedule; no result-relevant quantitative relationship. |
| 61 | 20 | Direct access/data-breach administrative material; no result-relevant quantitative relationship. |
| 62 | 21 | Statistics section: overall planned N and pilot design/allocation; B-N016-B-N017. |
| 63 | 22 | Phase 3 sample-size, attrition, ICC/design-effect, and recruitment-flow calculations; B-S004-B-N020. |
| 64 | 23 | Phase 4 non-inferiority, attrition, design-effect, and recruitment-flow calculations; B-S006, B-N020-B-N021. |

## Quantitative and reporting relationship inventory

### Objectives, endpoint definitions, and prospective outcome scale


## S022 — Four-phase design, contrasts, and timing

- **Mapper-local relationship:** B-S001
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 46 (printed p. 6), lines 1328-1337 (`joi250093supp1_prod_1768590553.08963.pdf#page=46`).
- **Direct observation:** multi-centre cluster-randomised controlled trial with four phases: phase 1 PPI consultation; phase 2 pilot; phase 3 superiority trial, mTB-Tobacco A vs usual care/control C, lasting `12 months` (`6` recruitment + `6` follow-up); phase 4 non-inferiority trial, A vs face-to-face behavioural support B, another `12 months` (`6` + `6`).
- **Source-grounded rule:** effect estimates must be matched to phase, comparator, superiority/non-inferiority framework, cluster unit, and follow-up time before cross-source comparison.


## S023 — High-level Phase 3 superiority planning assumptions

- **Mapper-local relationship:** B-S002
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 46 (printed p. 6), lines 1343-1359 (`joi250093supp1_prod_1768590553.08963.pdf#page=46`).
- **Direct observation:** protocol states total planned `2,716` smokers with TB, approximately `43` recruits from `63` health facilities/clusters, allowing `10%` with no primary-outcome data and including the first `16` pilot participants. For Phase 3, A versus C has `90%` power at `5%` significance; `18` clusters are randomised to A and `9` to C; usual-care abstinence is assumed `8%` and mTB-Tobacco abstinence `18%` at 6 months.
- **Repeated occurrence:** the 2,716/16 total and Phase-3 assumptions recur in B-N007 and B-S004. The 63-site figure is arithmetically compatible with 27 Phase-3 plus 36 Phase-4 sites in B-N007.


## S024 — High-level conditional Phase 4 non-inferiority planning assumptions

- **Mapper-local relationship:** B-S003
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 46 (printed p. 6), lines 1350-1359 (`joi250093supp1_prod_1768590553.08963.pdf#page=46`).
- **Direct observation:** if A is superior to C, Phase 4 has `90%` power at `1-sided 2.5%` to establish non-inferiority of mobile to face-to-face, comparing `18` clusters in each A and B. Face-to-face abstinence is `18%` at six months; the non-inferiority margin is `8%`; natural cessation is `2%`; established face-to-face effect is `16% (18%-2%)`; and the `8%` margin preserves at least `50% (8/16)` of that effect.
- **Repeated occurrence:** these Phase-4 assumptions recur in B-S006. They are prospective conditions/definitions, not a reported non-inferiority analysis.


## S025 — Phase 3 power and base sample-size assumptions

- **Mapper-local relationship:** B-S004
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 63 (printed p. 22), lines 1884-1909 (`joi250093supp1_prod_1768590553.08963.pdf#page=63`).
- **Direct observation:** Phase 3 compares A with C, assumes `90%` power, `5%` significance, usual-care abstinence `8%`, mTB-Tobacco abstinence `18%` at 6 months, and intervention/control sample-size ratio `2`; calculated base `n=587`. It plans `27` sites, allocation `18` A and `9` C. It then states `20%` attrition: `N = N0 + N0*20%`; `N = 587 + (587*0.2) = 704`; sample/cluster `704/27 = 26`.
- **Source-grounded statistical rule:** compare later Phase-3 inferential reporting only if it shares phase, A/C contrast, 6-month abstinence outcome, cluster design, and the stated 90%/5% assumptions. The page does not provide an observed effect, CI, test statistic, or P value.


## S026 — Phase 3 ICC/design-effect calculation and recruitment inflation

- **Mapper-local relationship:** B-S005
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 63 (printed p. 22), lines 1899-1920 (`joi250093supp1_prod_1768590553.08963.pdf#page=63`).
- **Direct observation:** cRCT calculation uses `27` clusters, `26` participants/cluster, ICC `0.02`, and formula `DE = 1 + ρ(m-1)`, where m is cluster subjects and ρ is intra-cluster correlation. Printed: `DE = 1 + 0.02(26-1) = 1.50`; `ESS = effective sample size = 704 * 1.50 ≈ 1080 (40 subjects for each site)`. Diagram then gives Phase-3 recruitment `1080`, `27` sites, Bangladesh `15×40=600`, Pakistan `12×40=480`, A Bangladesh 10/Pakistan 8 and control Bangladesh 5/Pakistan 4, all 40/site.
- **Arithmetic comparison rule:** displayed DE calculation is 1.50. The literal product 704×1.50 is 1,056, while the document displays approximately 1,080 and separately sets 40/site×27=1,080. The source does not state the rounding/allocation convention linking 1,056 to 1,080. Preserve all three numbers and the formula for later statistical checking.


## S027 — Phase 4 non-inferiority assumptions and base sample size

- **Mapper-local relationship:** B-S006
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 64 (printed p. 23), lines 1923-1953 (`joi250093supp1_prod_1768590553.08963.pdf#page=64`).
- **Direct observation:** conditional on A superior to C, Phase 4 assumes `90%` power and `1-sided 2.5%` non-inferiority level for mobile versus face-to-face; `18` clusters each in A and B; face-to-face abstinence `18%` at six months; non-inferiority margin `8%`; natural cessation `2%`; stated face-to-face effect `16% (18%-2%)`; margin preserves at least `50% (8/16)` of that effect. Mobile/face-to-face ratio is `1:1`; calculated base `n=864`.
- **Source-grounded statistical rule:** any Phase-4 result comparison must retain one-sided 2.5%, A/B comparison, non-inferiority margin, six-month endpoint, and cluster design. These are planning assumptions, not reported Phase-4 results.


## S028 — Phase-3 superiority planning

- **Mapper-local relationship:** C-S001
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Source.** DOC-002 p. 65 (`#page=65`) and p. 82 (`#page=82`).

**Definition.** Phase 3 compares intervention A with usual-care control, targets 6-month abstinence, with 90% power and 5% significance; planned rates are 18% versus 8%.  The trial is cluster randomized and p. 82 supplies ICC 0.02 and design effect 1.50.  No test statistic, observed CI, or P value is reported.


## S029 — Phase-4 non-inferiority planning

- **Mapper-local relationship:** C-S002
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Source.** DOC-002 pp. 65 and 82 (`#page=65`, `#page=82`).

**Definition.** Phase 4 compares A mTB-Tobacco with B face-to-face support; 90% power, one-sided 2.5% level, 8% non-inferiority margin, 18% assumed B abstinence, and 50% preservation of the stated 16% B-versus-natural-cessation effect.  No observed estimate/CI/P value is reported.


## S030 — Cost-effectiveness uncertainty analysis

- **Mapper-local relationship:** C-S003
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Source.** DOC-002 pp. 65–66 (`#page=65`, `#page=66`).

**Definition.** Phase 3 uses incremental cost-effectiveness (mTB-Tobacco above usual care), EQ-5D-5L/QALYs, 12-month horizon, cost/QALY and cost/additional-quitter ratios.  Phase 4 compares costs/QALYs and ICERs.  Planned uncertainty methods: nonparametric bootstrap **5,000** replications, ICER **95%** confidence intervals, CEACs, complete-case analysis, and pattern-mixture multiple-imputation sensitivity analysis.  This is a plan; no evaluated ICER/value is printed.


## S031 — Primary trial statistical model

- **Mapper-local relationship:** C-S004
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Source.** DOC-002 p. 66 (`#page=66`).

**Definition.** Outcomes are primarily analyzed under missing-at-random using generalized linear mixed models with a log link and underlying Poisson distribution; clusters are random effects via a random intercept.  Crude and adjusted RRs and corresponding 95% CIs are planned.  This is a model/measure definition that matches the primary outcome context, not an observed analysis result.


## S032 — Interim and descriptive analysis

- **Mapper-local relationship:** C-S005
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Source.** DOC-002 p. 89 (`#page=89`).

**Definition.** An independent statistician conducts Phase-3 interim analysis to decide progression to Phase 4 or early termination.  Baseline continuous variables use means/SDs or medians/IQRs by distribution; categorical variables use frequencies/percentages.  Distribution diagnostics include histograms, Q-Q plots, skewness, and kurtosis.  No interim boundary or observed result is printed.


## S033 — Primary abstinence analysis

- **Mapper-local relationship:** C-S006
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Source.** DOC-002 p. 90 (`#page=90`).

**Definition.** At 6 months, report agreement between self-report and biochemical verification by trial arm and report abstinent number/proportion by arm.  Complete-case group differences use risk difference and RR with 95% CIs.  A mixed-effects logistic regression treats site as random effect; stated output is RR with 95% CI and P value.  Primary analysis is ITT; dropout/incomplete outcome data are treated as continuing smokers.

**Interpretive limitation.** A logistic regression conventionally has an odds-ratio coefficient; the source does not explain any transformation or marginal standardization used to express it as RR.  This is a named missing definition, not proof of an inconsistency.


## S034 — Secondary analyses and low-frequency AE rule

- **Mapper-local relationship:** C-S007
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Source.** DOC-002 pp. 90–91 (`#page=90`, `#page=91`).

**Definition.** Secondary TB outcomes use appropriate descriptive/inferential models over available timepoints.  A chi-squared test compares any AE and serious AE between mHealth/control when at least **10 patients** have one or more events; low-frequency AEs use an exact test.  EQ-5D-5L baseline/6-month scores use a mixed-effects model with site random effect, treatment, time, and treatment×time fixed effects; estimated marginal means/intergroup differences have 95% CIs and P values.


## S035 — Adjusted, complete-case, and subgroup analyses

- **Mapper-local relationship:** C-S008
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Source.** DOC-002 pp. 91–92 (`#page=91`, `#page=92`).

**Definition.** Adjusted mixed-effects logistic models account for site clustering and adjust for sociodemographics, tobacco form, education, and smoking duration; treatment effect is stated as RR with 95% CI.  Missing-outcome sensitivity repeats logistic regression in available-outcome patients and reports abstinent number/proportion for self-report and CO-verified outcome by arm, plus coefficient/95% CI/P value.  Subgroups include age <40 vs ≥40 years; education (none/primary/more than primary); occupation (active employment/business vs dependents/retired); gender; and smoking duration <24 vs ≥24 years.  Each gets a mixed-effects model with site random intercept and RR/95% CI.  No subgroup effects are reported.


## S036 — Template-table measure and test labels

- **Mapper-local relationship:** C-S009
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


**Source.** DOC-002 pp. 93–96 (`#page=93`–`#page=96`).

**Definition.** These are explicitly templates with blank cells, not results.  They specify baseline tables with m-Health/control, chi-square and P columns for categorical variables; tobacco-type counts n(%); tobacco-use continuous fields with n, median (IQR), mean (SD), Z value, and P value; and smoking-behavior fields with chi-square/t/z and P.  No numeric value, test statistic, effect, or result may be extracted from blank template cells.

## Candidate and limitation summary

Two local observations need cross-source/recheck handling if the coordinator judges them candidate-ready: C-N006 (Phase-3 design-effect calculation wording/numeric relationship) and C-N009 (MPSS stated range against stated five 5-point domains).  All other mapped relationships are plans, definitions, administrative quantities, or blank templates in this assigned span.  No display-zero P-value issue appears.

# Support Quantitative Evidence Map — DOC-002 pp. 97-109 and DOC-003 pp. 1-16

## Scope and evidence method

This is a source-grounded extraction map, not a candidate diagnosis or adjudication. `D-N` and `D-S` are local relationship identifiers for this part only. Direct PDF pages are the authority. DOC-002 pp. 97-109 were individually visually inspected from the current-run 180-dpi JPEGs because its native/layout extraction is font-encoding garble. DOC-003 pp. 1-2 were checked using fresh layout text and direct PDF; pp. 3-16 used the page-addressable reused normalized text and page images, visually confirmed against the direct PDF/rendered-page representation.

## Per-page coverage

| Source/page | Content and result relevance | Coverage outcome |
|---|---|---|
| DOC-002 PDF p. 97 | Blank CRF fields for prior quit attempt, smoking duration, age starting, and SUTS; site IDs 3000-3007. | No completed participant/result values; template labels retained in D-N001. |
| DOC-002 PDF p. 98 | Blank primary-abstinence, mixed-model, and verified-abstinence subgroup templates; site IDs 3008-3015. | No displayed estimates; template definitions retained in D-N002. |
| DOC-002 PDF p. 99 | Continuation of blank subgroup template; site IDs 3016-3017. | No result values. |
| DOC-002 PDF p. 100 | Glossary. | Definitions retained in D-N003. |
| DOC-002 PDF pp. 101-109 | mTB-Tobacco intervention SMS log with numbered messages, schedule markers, times, and character counts. | Protocol intervention content; timing/quantity definitions retained in D-N004; no analysis results. |
| DOC-003 PDF p. 1 | Supplement contents. | No result values. |
| DOC-003 PDF p. 2 | Trial Steering Committee member list. | No result values. |
| DOC-003 PDF p. 3 | eTable 1, screening and ineligibility counts. | D-N005. |
| DOC-003 PDF p. 4 | eTable 2, prior quit attempts by cluster and arm. | D-N006. |
| DOC-003 PDF p. 5 | eTable 3, TB-treatment-adherence summaries and z/P pairs. | D-N007, D-S001. |
| DOC-003 PDF p. 6 | eTable 4, causes of death. | D-N008. |
| DOC-003 PDF p. 7 | Kaplan-Meier survival plot. | D-N009. |
| DOC-003 PDF p. 8 | eTable 5, cluster recruitment and abstinence rates. | D-N010. |
| DOC-003 PDF p. 9 | eTable 6, cluster death counts/rates. | D-N011. |
| DOC-003 PDF pp. 10-11 | eTable 7, cluster characteristics and unadjusted RRs. | D-N012, D-S002. |
| DOC-003 PDF p. 12 | eTable 8, subgroup RRs for verified abstinence. | D-N013, D-S003. |
| DOC-003 PDF pp. 13-14 | eTable 9, post-hoc ITT sensitivity analysis after exclusion of deaths and footnotes. | D-N014, D-S004. |
| DOC-003 PDF pp. 15-16 | eTable 10, adverse-event categories, counts/percentages, test statistics, and P values. | D-N015, D-S005. |

## DOC-002 protocol and administrative evidence


## S037 — TB-treatment adherence by month

- **Mapper-local relationship:** D-S001
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF p. 5, eTable 3.
- **Direct observation:** For months 1-6, respectively, mHealth median(IQR) is 30(30-30) each month; mean(SD) is 29.87(1.345), 29.59(2.757), 29.39(3.894), 29(5.092), 28.56(6.049), 27.88(7.397). Control median(IQR) is 30(30-30) each month; mean(SD) is 29.9(0.2), 29.8(0.6), 29.7(2.3), 29.5(3.3), 29.5(3.3), 29.3(3.9). Total: mHealth 180(180-180), 174.3(21.501); control 180(180-180), 178.0(12.1).
- **Statistical observation (D-S001):** Printed z/P pairs for month 1 through total are -0.86/0.388, 0.44/0.656, 1.64/0.101, 0.44/0.657, 0.95/0.34, 1.85/0.064, and 1.19/0.232. Test name, sidedness, and population denominators are not printed on this page.
- **Matching/main-paper key:** secondary outcome, TB-treatment adherence over months 1-6.


## S038 — Cluster characteristics and unadjusted relative risks

- **Mapper-local relationship:** D-S002
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF pp. 10-11, eTable 7.
- **Direct observation:** The 27 site rows provide age mean(SD), male n(%), smoking-duration mean(SD) in years, education categories (no formal, primary, middle, higher) and occupation (employed, dependent, retired). Each row is a cluster, usually n=40; exceptions visibly include site 1015 male 39(97.5), 2003 male 38(95), 2004 male 34(85), 2005 male 39(97.5), 2006 male 38(95), 2007 male 33(82.5), 2008 male 32(80), 2009 male 35(87.5), 2010 male 36(90), and 2011 male 39(97.5). Exact row values are on the cited two pages.
- **Statistical observation (D-S002):** Printed unadjusted relative risks (95% CI), in the order of displayed characteristics, are age 1.03 (1.01-1.04), male 0.83 (0.34-2.02), smoking duration 0.97 (0.95-0.99), education no-formal 1 [reference], primary 1.32 (0.88-1.97), middle 1.91 (1.16-3.15), higher 1.86 (1.16-2.99), occupation employed 1 [reference], dependent 2.01 (1.30-3.09), retired 1.00 (0.43-2.31).
- **Matching/main-paper key:** cluster-level characteristics, reference categories, and unadjusted relative-risk analysis.


## S039 — Subgroup analysis of verified 6-month abstinence

- **Mapper-local relationship:** D-S003
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF p. 12, eTable 8.
- **Direct observation / statistical observation:** Unadjusted RR (95% CI) for verified abstinence at month 6: all 2.890 (1.983-4.709); age <40 2.672 (1.472-4.857), >=40 2.953 (2.048-5.092); no formal education 2.880 (1.566-5.542), primary years 1-5 2.638 (1.849-4.07), secondary or above >=6 years 2.719 (1.348-4.83); active job/business 2.989 (1.933-4.885), dependent/retired 2.587 (1.329-3.986); smoking duration <24 years 3.511 (1.884-7.127), >=24 years 2.446 (1.550-3.911); reading SMS yes 2.769 (1.743-4.318), no 2.198 (1.288-3.299).
- **Matching/main-paper key:** verified abstinence at 6 months; effect measure explicitly labelled RR and 95% CI.


## S040 — Post-hoc ITT sensitivity analysis excluding deaths

- **Mapper-local relationship:** D-S004
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF pp. 13-14, eTable 9.
- **Direct observation:** Population denominators after exclusion of deaths are mHealth 695 and usual care 333. For biochemically verified abstinence at month 6, <10 ppm: 300/695, 43.2% (39.4-46.9) vs 55/333, 16.5% (12.7-20.9); absolute difference 26.7 (21.2-32.1); crude RR 2.9 (1.8-6.4), crude ICC 0.18; adjusted RR 3.1 (1.9-6.5), adjusted ICC 0.18. For <6 ppm: 264/695, 38.0% (34.4-41.7) vs 38/333, 11.4% (8.2-15.3); difference 26.6 (21.6-31.5); crude RR 3.6 (2.4-5.4), ICC 0.17; adjusted RR 3.8 (2.4-6.2), ICC 0.18.
- **Direct observation, continued:** Week-9 point abstinence: 353/695, 50.8% (47.0-54.6) vs 75/333, 22.5% (18.1-27.4); difference 28.3 (22.4-34.1); crude RR 2.5 (1.7-3.6), ICC 0.20; adjusted RR 2.6 (1.7-3.8), ICC 0.20. Month-6 point abstinence: 400/695, 57.5% (53.8-61.2) vs 82/333, 24.6% (20.1-29.6); difference 32.9 (27.0-38.8); crude RR 2.58 (1.8-3.6), ICC 0.20; adjusted RR 2.7 (1.8-4.0), ICC 0.20. Successful TB treatment: 643/695, 92.5% (90.3-94.4) vs 308/333, 92.5% (89.1-95.1); difference 0 (-3.4-3.5); crude RR 1.1 (0.7-1.6), ICC 0.25; adjusted RR 1.1 (0.7-1.5), ICC 0.23. Defaulted: 22/695, 3.2% (2.0-4.8) vs 7/333, 2.1% (0.8-4.3); difference 1.1 (-1.0-3.1); RRs/ICCs not printed. Treatment failures: 1/695, 0.1% (0.01-0.8) vs 2/333, 0.6% (0.1-2.2); difference 0.5 (-0.4-1.3); RRs/ICCs not printed.
- **Definitions (p. 14):** a=numerator/total group number; b=absolute difference; c=relative risk; d=intraclass correlation coefficient; e=adjusted for age, sex, education, occupation, smoking duration, accounting for clustering and mixed-effects models for RR; f=carbon-monoxide breath-test cutoff values.
- **Matching/main-paper key:** post-hoc sensitivity analysis, ITT population after deaths excluded; distinctions between crude/adjusted RR and ICC are explicit.


## S041 — Adverse events

- **Mapper-local relationship:** D-S005
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF pp. 15-16, eTable 10.
- **Direct observation:** Each event has none/mild/moderate/severe categories reported as mHealth n(%) and control n(%). Group category counts sum to 699 mHealth and 334 control for nausea, diarrhoea, dry mouth, epigastric pain, headache, insomnia, abnormal dreams, irritability, anxiety, palpitations, and musculoskeletal pain.
- **Statistical observation (D-S005):** Printed X2/P pairs: nausea 6.5 with 0.084 (exact-test superscript); diarrhoea 1.0 with 0.825 (exact); dry mouth 31.2 with <.001; epigastric pain 18.2 with <.001 (exact); headache 2.7 with 0.426; insomnia 6.9 with 0.072; abnormal dreams 3.8 with 0.255 (exact); irritability 18.5 with <.001; anxiety 17.1 with <.001; palpitations 5.2 with 0.154 (exact); musculoskeletal pain 8.8 with 0.031. Page 16 defines superscript a as based on Exact test.
- **Matching/main-paper key:** adverse-event outcomes by study arm. The `<.001` presentations are threshold displays, not literal-zero P values.

## Source-linked observations reserved for downstream checking

These statements do not diagnose or adjudicate any candidate.

1. **D-N011:** eTable 6 prints site 2008 as 5 deaths (7.5%). eTable 5 prints 40 recruited at every cluster, including 2008. Any comparison must first confirm that both figures use the same analysis population and denominator; if they do, `5/40` is a relevant arithmetic relationship for a later independent checker.
2. **D-N010/D-N011/D-N014/D-N015:** Denominators vary by outcome and timepoint (cluster recruited n=40; some observed follow-up denominators <40; sensitivity denominators 695/333; adverse-event denominators 699/334). They must not be substituted for one another without a printed population/time match.
3. **D-S001/D-S005:** Test names and detailed test conventions are incompletely provided for some z/P and X2/P pairs. Later statistical review should use only the stated definitions, including the exact-test footnote, and should not infer a test model from the printed summaries alone.

## Limitations

DOC-002 pp. 97-109 contain blank CRF/template material and an intervention SMS log rather than completed trial results; no numerical outcome can be extracted from a blank field. DOC-003 eFigure p. 7 has no printed exact survival estimates or test output, so its values are only qualitative/axis-based. All DOC-003 table values above were confirmed visually against the direct page image; the normalized text was used only to assist exhaustive transcription.

## Inventory count

- **Inferential-statistical relationships:** 41.
