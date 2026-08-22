# Support Numeric Relationship Inventory Part

Fresh mapping source: DOC-002 PDF pp. 1-21 and DOC-003 PDF pp. 1-12. `Direct observation` means printed source evidence; any arithmetic is a diagnostic check only. Each relationship is pending downstream checking, not a candidate.

## N1001 — Protocol factorial allocation and planned follow-up

- **Location:** DOC-002 PDF p. 5 (Figure 1 and C1).
- **Printed values:** 32 SAFE hospitals; 16 selected; 4 arms; 4 hospitals/arm; 1,600 mothers = 100/hospital = 400/arm; estimated 80% follow-up = 320/arm.
- **Population/time/contrast/measure:** planned mothers at selected hospitals; arm allocation; enrollment and follow-up count/proportion.
- **Direct observation / diagnostic derivation:** direct. Diagnostic identities: 16×100=1,600; 4×400=1,600; 400×0.80=320.
- **Cross-document match key:** `design_2x2_factorial_16_hospitals_1600_enrolled`; `followup_80_percent_1280_expected`.
- **Applicable checks:** totals, group allocation, rate-versus-count distinction, planned versus observed population.

## N1002 — Protocol intervention exposure timing

- **Location:** DOC-002 p. 8.
- **Printed values:** mHealth begins within 72 hours of enrollment; twice weekly until 2 months; each video ~2 minutes; 5-7 videos anticipated.
- **Population/time/contrast/measure:** enrolled mothers, group-assigned email/video intervention; time/frequency/duration.
- **Direct observation:** yes. **Cross-document match key:** `mhealth_exposure_timing_frequency`. **Checks:** time/label consistency only.

## N1003 — Protocol focus-group quantitative plan

- **Location:** DOC-002 pp. 8-9.
- **Printed values:** infant <6 months; at least weekly email access; 3-5 groups/subgroup, extended to saturation; 6-8 participants/group; $50 maternal and $25 staff gift cards.
- **Population/time/contrast/measure:** formative focus-group plan, not trial outcome. **Direct observation:** yes. **Checks:** no trial comparator; retain as definition only.

## N1004 — SAFE hospital/source population and recruitment target

- **Location:** DOC-002 p. 9.
- **Printed values:** hospitals deliver ≥100 newborns/year; 32 hospitals; ~40 mothers/hospital/year; ~1,250/year in 2011-2013; target 25% Black enrollment; all 8 completed quarter-1 hospitals offered letters.
- **Population/time/contrast/measure:** pretrial SAFE sampling/recruitment definition.
- **Direct observation:** yes. **Cross-document match key:** `SAFE_baseline_source_population`. **Checks:** planned versus observed distinction; no outcome arithmetic required.

## N1005 — Eligibility/recruitment yield plan

- **Location:** DOC-002 p. 10.
- **Printed values:** 100 mothers/hospital; 85% eligible; 75% of eligible agree; approach ~160 mothers to recruit 100; follow-up 2-5 months; one infant randomly selected for multiple births.
- **Population/time/contrast/measure:** planned hospital-level recruitment and mother/infant analysis definition.
- **Direct observation / diagnostic derivation:** direct; 160×0.85×0.75=102, consistent with approximate 100 target.
- **Cross-document match key:** `planned_recruitment_100_per_hospital`; **checks:** approximation/rounding and analysis unit.

## N1006 — Follow-up schedule and response targets

- **Location:** DOC-002 pp. 11-12.
- **Printed values:** follow-up single survey at 2-5 months; second email one week after initial email if incomplete; telephone one week later; minimum 10 calls; first and then 2-week-later second mail survey; $10 follow-up gift card; 80% SAFE response rate.
- **Population/time/contrast/measure:** enrolled mothers/follow-up procedures.
- **Direct observation:** yes. **Cross-document match key:** `followup_maternal_survey_2_to_5_months`; `followup_response_rate_80_percent`. **Checks:** time window and rate/count match.

## N1007 — Protocol planned analysis sample and power inputs

- **Location:** DOC-002 p. 14.
- **Printed values:** 100×16=1,600; 400/group; 80% follow-up gives 320/group/1,280 overall; baseline prevalence 0.50-0.60; 10- and 20-percentage-point scenarios; alpha .05/.0125; ICC .002; power 96% main effect and 80% combined-versus-one.
- **Population/time/contrast/measure:** planned group-randomized simulation, categorical outcomes.
- **Direct observation / diagnostic derivation:** direct; arithmetic identities above. **Cross-document match key:** `protocol_power_1600_1280_ICC_0.002`. **Checks:** distinguish power projection from observed estimate.

## N1008 — Protocol timeline totals

- **Location:** DOC-002 p. 15.
- **Printed values:** baseline SAFE data for 2 years; 5-year plan (2012-2017); projected 200 mothers per marked recruitment period; projected follow-ups shown as 80/160; final text specifies 1,600 mothers.
- **Population/time/contrast/measure:** operational projection. **Direct observation:** yes. **Cross-document match key:** `planned_1600_enrollment_timeline`. **Checks:** planned-total reconciliation.

## N1009 — eTable 2 respondent status totals

- **Location:** DOC-003 pp. 3-4.
- **Printed values:** respondents 1,263; nonrespondents 337; total 1,600. Follow-up age total counts: 917, 172, 87, 87 (percent 72.7,13.6,6.9,6.9).
- **Population/time/contrast/measure:** enrolled mothers at birth hospital; response to maternal follow-up; infant age at follow-up.
- **Direct observation / diagnostic derivation:** direct; 1,263+337=1,600; age counts sum 1,263.
- **Cross-document match key:** `enrolled_1600_followed_1263_lost_337`; **checks:** totals/denominators, percentage rounding, main-paper flow identity.

## N1010 — eTable 2 demographic categories and respondent comparison

- **Location:** DOC-003 pp. 3-4.
- **Printed values:** complete count/percent triplets for sex, parity, maternal age, race/ethnicity, education, marital status, and income are transcribed in `extraction/support_quantitative_evidence.md` under eTable 2. P values: sex .5206; parity .2039; each of age, race, education, marital status and income <.0001.
- **Population/time/contrast/measure:** respondents versus nonrespondents at enrollment; categorical counts/within-status percentages.
- **Direct observation:** yes. **Cross-document match key:** `respondent_demographics_table1`. **Checks:** mutually exclusive category sums; denominator/proportion; chi-square label/P display.

## N1011 — eTable 3 SAFE group denominators and characteristics

- **Location:** DOC-003 pp. 5-6.
- **Printed values:** BF/BF N=417; SS-NQI/BF-mH N=387; BF-NQI/SS-mH N=421; SS/SS N=379. All displayed count/percent values for sex, parity, age, race, education, marital status, income, and follow-up age are transcribed in the extraction artifact.
- **Population/time/contrast/measure:** pre-study SAFE participants used for baseline rates; four future assignment group strata.
- **Direct observation / diagnostic derivation:** direct; N total 417+387+421+379=1,604.
- **Cross-document match key:** `SAFE_baseline_table2_group_denominators_417_387_421_379`; **checks:** category sums, denominator/proportion, match to main Table 2 baseline rates.

## N1012 — eTable 4 imputed cell denominators and unadjusted supine outcome

- **Location:** DOC-003 p. 7.
- **Printed values:** N=400 for each randomized cell; usual supine counts 315 (78.8%), 302 (75.5%), 348 (87.0%), 364 (90.9%).
- **Population/time/contrast/measure:** imputation analysis, age ≥60 days, usual sleep position past two weeks; four cells BF/BF, SS-NQI/BF-mH, BF-NQI/SS-mH, SS/SS.
- **Direct observation / diagnostic derivation:** direct; displayed counts / 400 reproduce percentages to one decimal.
- **Cross-document match key:** `imputation_supine_four_cells`; **checks:** denominator/proportion, imputation-versus-complete-case label.

## N1013 — eTable 4 room-sharing counts/percents

- **Location:** DOC-003 p. 7.
- **Printed values:** 279 (69.7%), 298 (74.6%), 316 (79.0%), 340 (85.0%), each N=400.
- **Population/time/contrast/measure:** usual room sharing without bedsharing, past two weeks, imputed age ≥60-day analysis. **Direct observation:** yes; counts/400 reproduce values. **Match key:** `imputation_roomsharing_four_cells`. **Checks:** denominator/proportion and label distinction room sharing vs bedsharing.

## N1014 — eTable 4 no-soft-bedding counts/percents

- **Location:** DOC-003 p. 7.
- **Printed values:** 270 (67.4%), 271 (67.7%), 310 (77.5%), 326 (81.6%), each N=400.
- **Population/time/contrast/measure:** no soft bedding, past two weeks, imputed age ≥60-day analysis. **Direct observation:** yes; counts/400 reproduce values. **Match key:** `imputation_soft_bedding_four_cells`. **Checks:** denominator/proportion and definition match.

## N1015 — eTable 4 any-pacifier counts/percents

- **Location:** DOC-003 p. 7.
- **Printed values:** 241 (60.2%), 264 (66.1%), 274 (68.6%), 295 (73.7%), each N=400.
- **Population/time/contrast/measure:** any pacifier use, past two weeks, imputed age ≥60-day analysis. **Direct observation:** yes; counts/400 reproduce values. **Match key:** `imputation_pacifier_four_cells`. **Checks:** denominator/proportion and definition match.

## N1016 — eTable 4 effect-measure/definition footnotes

- **Location:** DOC-003 p. 8.
- **Printed values/labels:** adjusted risk (aR, %) for control/intervention; aRD calculated from logistic-regression odds ratios and CIs; outcomes covariate-adjusted; soft bedding lacks pre-study SAFE rate; soft-bedding item list; any-pacifier definition `usually` or `sometimes`.
- **Population/time/contrast/measure:** applies N1012-N1015. **Direct observation:** yes. **Match key:** `imputation_aR_aRD_definitions`. **Checks:** measure/label/scale, adjustment consistency, rate-vs-count.

## N1017 — eTable 5 sleep-position stratified counts/percents

- **Location:** DOC-003 p. 9.
- **Printed values:** BF/BF: All 243/303 (80.2%), White 82/91 (90.1%), Black 55/83 (66.3%), Hispanic 82/99 (82.8%), Other 24/30 (80.0%). SS/SS: 294/318 (92.5%), 116/127 (91.3%), 60/70 (85.7%), 106/109 (97.2%), 12/12 (100%).
- **Population/time/contrast/measure:** race/ethnicity strata, age ≥60 days, control vs combined safe-sleep intervention. **Direct observation:** yes. **Match key:** `race_stratified_sleep_position_control_vs_combined`. **Checks:** count/denominator/percent; subgroup totals; outcome label.

## N1018 — eTable 5 room-sharing stratified counts/percents

- **Location:** DOC-003 p. 9.
- **Printed values:** BF/BF 205/291 (70.5%), 64/88 (72.7%), 53/78 (67.9%), 70/95 (73.7%), 18/30 (60.0%); SS/SS 269/313 (85.9%), 108/126 (85.7%), 57/66 (86.4%), 93/109 (85.3%), 11/12 (91.7%) for All/White/Black/Hispanic/Other.
- **Population/time/contrast/measure:** as N1017, room sharing without bedsharing. **Direct observation:** yes. **Match key:** `race_stratified_roomsharing_control_vs_combined`. **Checks:** denominator/percent, label distinction.

## N1019 — eTable 5 pacifier-use stratified counts/percents

- **Location:** DOC-003 p. 9.
- **Printed values:** BF/BF 174/291 (59.8%), 53/89 (59.6%), 51/77 (66.2%), 57/95 (60.0%), 13/30 (43.3%); SS/SS 240/315 (76.2%), 100/127 (78.7%), 46/68 (67.6%), 84/108 (77.8%), 10/12 (83.3%).
- **Population/time/contrast/measure:** as N1017, any pacifier use. **Direct observation:** yes. **Match key:** `race_stratified_pacifier_control_vs_combined`. **Checks:** denominator/percent and definition.

## N1020 — eTable 5 no-soft-bedding stratified counts/percents

- **Location:** DOC-003 p. 10.
- **Printed values:** BF/BF 202/299 (67.6%), 69/90 (76.7%), 52/80 (65.0%), 60/98 (61.2%), 21/31 (67.7%); SS/SS 262/320 (81.9%), 106/128 (82.8%), 56/70 (80.0%), 90/110 (81.8%), 10/12 (83.3%).
- **Population/time/contrast/measure:** as N1017, no soft bedding. **Direct observation:** yes. **Match key:** `race_stratified_soft_bedding_control_vs_combined`. **Checks:** denominator/percent and definition.

## N1021 — eFigure/eTable 5 age-boundary and plot identity

- **Location:** DOC-003 pp. 9-11.
- **Printed values/labels:** eTable 5 says infant age `≥60 days`; eFigure says `>60 days`; y-axis 0-100 percentage, with outcomes supine position, roomshare without bedsharing, any pacifier use, no soft bedding use. eFigure directs reader to eTable 5 for sample sizes and excludes Other race/ethnicity.
- **Population/time/contrast/measure:** post hoc race/ethnicity display. **Direct observation:** yes. **Match key:** `eFigure_eTable5_age_threshold_label`. **Checks:** cross-display label/time-boundary; plot/table identity.
