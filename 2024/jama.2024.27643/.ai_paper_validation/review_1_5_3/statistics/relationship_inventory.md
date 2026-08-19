# Statistical Relationship Inventory — Pass 1

## Scope and rules applied

- **Pass:** 1 of 2; **runtime agent ID:** `/root/statistics_pass_1`; **model/effort:** `gpt-5.6-terra` / `high`.
- **Scope:** every mapper-designated inferential relationship in DOC-001 and DOC-002, plus every result-bearing inferential relation and accompanying statistical-definition relation mapped in DOC-003 and DOC-004. DOC-005 and DOC-006 contain no applicable inferential result.
- **Source authority:** supplied PDFs only. Reused extraction was used as a locator; the source PDF was checked directly for each raw candidate.
- **Checks:** point estimate containment, endpoint ordering, direction/sign, effect-measure and scale labels, and matched cross-location repetitions. Interval/P-value/test/statistic/SE calculations were used only as explicitly labelled diagnostics when model/inferential definitions were sufficiently supplied; no sidedness, covariance, variance estimator, multiplicity adjustment, degrees of freedom, denominator, model version, or estimand was inferred from convention.
- **Display-zero rule:** no `P = 0`, `p = 0.000`, or equivalent display-zero P value was found among these relationships. `DISPLAY_ZERO_NOT_CANDIDATE` count: 0.
- **Stable-ID convention:** a repeated instance of the same matched result is retained within one S record. Distinct contrasts, endpoints, dose levels, and subgroup sets have separate records.

## Stable relationship records

| Stable ID | Relationship and source locations | Pass-1 checks and result | Missing definition / diagnostic boundary | Status |
|---|---|---|---|---|
| S001 | Sample-size/power design: DOC-001 PDF p. 3; DOC-002 pp. 60-65. | Design quantities and one-sided 2.5% threshold are labels/planned operating characteristics, not realized effect estimates; no incompatible repetition found. | Simulation inputs and realized operating calculation are not supplied. | PASS_1_COMPLETE |
| S002 | Analysis methods, hierarchy, and nominal P-value rules: DOC-001 pp. 3-4; DOC-003 pp. 12, 17-24. | CAFS/SVC/survival test labels, sequential rule, and stated nominal-P convention are internally directional and label-compatible. | Effective SAP/version mapping for every reported result is not declared in the article. | PASS_1_COMPLETE |
| S003 | Primary pooled DRR, Bayesian model: DOC-001 pp. 1, 2, 4, 6; DOC-004 p. 15 eTable 2. | DRR 0.97 lies within 0.783-1.175; endpoints ordered; DRR <1 has the stated slowing direction; main posterior 0.65 and eTable 0.6450 are compatible finite-precision presentations. | Bayesian posterior is not a two-sided frequentist P value; no P/CI inversion applied. | PASS_1_COMPLETE |
| S004 | Regimen-only primary DRR: DOC-001 p. 4. | DRR 0.96 lies within 0.709-1.357 and retains the stated DRR direction. | No matched supplemental interval for this sensitivity was located. | PASS_1_COMPLETE |
| S005 | Primary model component slopes and mortality rates: DOC-001 p. 4; DOC-004 p. 15 eTable 2. | Each displayed slope lies within its displayed CrI; exact cross-location values diverge and are recorded as raw candidate `RAW-S-P1-001`. | Whether the article text and eTable 2 use an undocumented model run, analysis date, or population distinction is not supplied. | PASS_1_COMPLETE |
| S006 | CAFS pooled comparison and NfL sensitivity: DOC-001 p. 4. | Mean-rank direction is concordant with the reported P=.51/.88; no effect interval or compatible test statistic is supplied. | CAFS analysis/version and whether each P is adjusted are not fully linked to the printed analysis result. | PASS_1_COMPLETE |
| S007 | Pooled SVC repeated-measures result: DOC-001 p. 4; DOC-004 p. 16 eTable 3A. | Difference -0.78 lies within -4.25 to 2.68 and agrees in direction with arm values; eTable SE 1.77 gives a labelled approximate Wald diagnostic consistent with the CI/P=.66. The main article’s `PPN/month` label differs from eTable’s 24-week SVC `% predicted` change and is recorded as `RAW-S-P1-004`. | The effective CI method and analysis version are not explicitly tied across article and eTable. | PASS_1_COMPLETE |
| S008 | Death/PAV pooled adjusted Cox comparison and NfL sensitivity: DOC-001 pp. 4, 6. | HRs 0.46 and 0.45 lie within their intervals; endpoints ordered and HR<1 matches lower event hazard for active. | Profile-log-likelihood CI is supplied, but no test statistic/sidedness is supplied; no reconstructed P check. | PASS_1_COMPLETE |
| S009 | PAV-free survival, pooled active vs shared placebo: DOC-001 p. 7 Table 2. | HR 0.46 lies within 0.12-1.49; HR label/direction and P=.22 are compatible with null-containing interval. | Profile likelihood, not a stated Wald calculation. | PASS_1_COMPLETE |
| S010 | PAV-free survival, 30 mg vs shared placebo: DOC-001 p. 7 Table 2. | HR 0.06 lies within 0.002-0.56; HR<1 and P=.04 align directionally with the interval excluding 1. | No sidedness or exact profile-likelihood test is supplied. | PASS_1_COMPLETE |
| S011 | PAV-free survival, 60 mg vs shared placebo: DOC-001 p. 7 Table 2. | HR 0.96 lies within 0.25-3.08; P=.95 aligns directionally with null-containing interval. | No exact test reconstruction. | PASS_1_COMPLETE |
| S012 | PAV-free survival, pooled active vs regimen-C placebo: DOC-001 p. 7 Table 2. | HR 0.25 lies within 0.05-1.09; P=.06 aligns directionally with null-containing interval. | No exact test reconstruction. | PASS_1_COMPLETE |
| S013 | PAV-free survival, 30 mg vs regimen-C placebo: DOC-001 p. 7 Table 2. | HR 0.03 lies within 0.0004-0.36; P=.03 aligns directionally with interval excluding 1. | No exact test reconstruction. | PASS_1_COMPLETE |
| S014 | PAV-free survival, 60 mg vs regimen-C placebo: DOC-001 p. 7 Table 2. | HR 0.47 lies within 0.10-2.16; P=.32 aligns directionally with null-containing interval. | No exact test reconstruction. | PASS_1_COMPLETE |
| S015 | Exploratory assisted-ventilation Cox result: DOC-001 p. 7. | HR 0.40 lies within 0.17-1.01; null-containing CI is compatible with narrative non-significance. | Exact analysis population and P not printed. | PASS_1_COMPLETE |
| S016 | Exploratory gastrostomy Cox result: DOC-001 p. 7. | HR 0.37 lies within 0.14-1.04; null-containing CI is compatible with narrative non-significance. | Exact analysis population and P not printed. | PASS_1_COMPLETE |
| S017 | Exploratory ALS-related SAE-hospitalization Cox result: DOC-001 p. 7. | HR 0.23 lies within 0.04-1.33; null-containing CI is compatible with narrative non-significance. | Exact analysis population and P not printed. | PASS_1_COMPLETE |
| S018 | Exploratory SAE-hospitalization Cox result: DOC-001 p. 7. | HR 0.48 lies within 0.18-1.33; null-containing CI is compatible with narrative non-significance. | Exact analysis population and P not printed. | PASS_1_COMPLETE |
| S019 | Serum NfL primary analysis: DOC-001 p. 8 Figure 3/text; DOC-004 p. 17 eTable 3B. | Main difference -23.2% lies within -39.5% to -2.5% and sign matches placebo increase vs active near-zero change. The matched ERO eTable differs in placebo change, difference, and CI; recorded as `RAW-S-P1-002`. | Whether the displays represent undocumented different datasets/models is not supplied. | PASS_1_COMPLETE |
| S020 | Serum NfL post hoc outlier sensitivity: DOC-001 p. 8; DOC-004 p. 25 eFigure. | Reversing the eFigure placebo-minus-active contrast gives active-minus-placebo -9.7% (CI -18.5% to +0.1%), matching article direction/values; P=.05 versus .051 is compatible rounding. | Figure/model effective P precision and CI construction are not supplied. | PASS_1_COMPLETE |
| S021 | Plasma NfL primary analysis: DOC-001 p. 8 Figure 3/text; DOC-004 p. 17 eTable 3B. | Difference -9.5% and P=.04 match repetitions; figure CI upper endpoint -0.5% conflicts with article text -0.4%, recorded as `RAW-S-P1-003`. ERO table `-18.0, 0` is not treated as a P/CI contradiction because its integer endpoint precision is insufficient. | Rounding convention for the figure/text CI endpoint is not supplied. | PASS_1_COMPLETE |
| S022 | Serious TEAE group comparison: DOC-001 p. 8. | Group percentages and P=.31 are reported without effect estimate, interval, test name, or denominator for the P; no inferential compatibility calculation is applicable. | Test, comparison set, and multiplicity treatment absent. | PASS_1_COMPLETE |
| S023 | FAS repeated-measures ALSFRS-R pooled vs shared placebo: DOC-004 p. 16 eTable 3A. | Difference 0.0 lies within -1.03 to 1.11; SE=.55 and P=.94 give an approximate Wald diagnostic compatible with rounding. | CI/test construction not explicitly specified for this table. | PASS_1_COMPLETE |
| S024 | FAS repeated-measures SVC pooled vs shared placebo: DOC-004 p. 16 eTable 3A. | Difference -0.78 lies within -4.25 to 2.68; SE=1.77 and P=.66 are approximately compatible. Cross-reference S007 for the article unit-label discrepancy. | Diagnostic only; no assumed Wald convention. | PASS_1_COMPLETE |
| S025 | FAS repeated-measures ALSFRS-R, 30 mg vs shared placebo: DOC-004 p. 16 eTable 3A. | Difference -0.19 lies within -1.53 to 1.16; SE=.69/P=.79 approximately agree. | Diagnostic only. | PASS_1_COMPLETE |
| S026 | FAS repeated-measures SVC, 30 mg vs shared placebo: DOC-004 p. 16 eTable 3A. | Difference 0.69 lies within -3.55 to 4.92; SE=2.19/P=.75 approximately agree. | Diagnostic only. | PASS_1_COMPLETE |
| S027 | FAS repeated-measures ALSFRS-R, 60 mg vs shared placebo: DOC-004 p. 16 eTable 3A. | Difference 0.27 lies within -1.07 to 1.60; SE=.68/P=.69 approximately agree. | Diagnostic only. | PASS_1_COMPLETE |
| S028 | FAS repeated-measures SVC, 60 mg vs shared placebo: DOC-004 p. 16 eTable 3A. | Difference -2.26 lies within -6.75 to 2.24; SE=2.29/P=.33 approximately agree. | Diagnostic only. | PASS_1_COMPLETE |
| S029 | ERO repeated-measures ALSFRS-R pooled vs regimen placebo: DOC-004 p. 17 eTable 3B. | Difference -0.07 lies within -1.71 to 1.57; SE=.83/P=.94 approximately agree. | Diagnostic only. | PASS_1_COMPLETE |
| S030 | ERO repeated-measures SVC pooled vs regimen placebo: DOC-004 p. 17 eTable 3B. | Difference -2.83 lies within -8.10 to 2.44; SE=2.67/P=.29 approximately agree. | Diagnostic only. | PASS_1_COMPLETE |
| S031 | ERO repeated-measures ALSFRS-R, 30 mg vs regimen placebo: DOC-004 p. 17 eTable 3B. | Difference -0.17 lies within -2.00 to 1.66; SE=.93/P=.85 approximately agree. | Diagnostic only. | PASS_1_COMPLETE |
| S032 | ERO repeated-measures SVC, 30 mg vs regimen placebo: DOC-004 p. 17 eTable 3B. | Difference -0.87 lies within -6.69 to 4.95; SE=2.94/P=.77 approximately agree. | Diagnostic only. | PASS_1_COMPLETE |
| S033 | ERO repeated-measures ALSFRS-R, 60 mg vs regimen placebo: DOC-004 p. 17 eTable 3B. | Difference 0.04 lies within -1.79 to 1.87; SE=.93/P=.97 approximately agree. | Diagnostic only. | PASS_1_COMPLETE |
| S034 | ERO repeated-measures SVC, 60 mg vs regimen placebo: DOC-004 p. 17 eTable 3B. | Difference -4.79 lies within -10.76 to 1.19; SE=3.03/P=.12 approximately agree. | Diagnostic only. | PASS_1_COMPLETE |
| S035 | ERO plasma NfL, 30 mg vs regimen placebo: DOC-004 p. 17 eTable 3B. | Difference -8.5 lies within -18 to 2; null-containing interval and P=.10 agree directionally. | No SE, exact CI precision, or model test statistic. | PASS_1_COMPLETE |
| S036 | ERO serum NfL, 30 mg vs regimen placebo: DOC-004 p. 17 eTable 3B. | Difference -25.5 lies within -52.2 to 1.3; null-containing interval and P=.06 agree directionally. | No SE or exact CI precision. | PASS_1_COMPLETE |
| S037 | ERO plasma NfL, 60 mg vs regimen placebo: DOC-004 p. 17 eTable 3B. | Difference -10.5 lies within -20 to 0; P=.04 is not treated as contradictory because the integer endpoint may be a rounded value below zero. | Exact unrounded CI and test are absent. | PASS_1_COMPLETE |
| S038 | ERO serum NfL, 60 mg vs regimen placebo: DOC-004 p. 17 eTable 3B. | Difference -27.4 lies within -45.1 to -0.7; P=.05 directionally aligns with interval excluding 0 at displayed precision. | Exact P and CI precision absent. | PASS_1_COMPLETE |
| S039 | Forest plot all participants, ALSFRS-R slope difference: DOC-004 pp. 18-20 eTable 4. | 0.03 lies within -0.16 to 0.23; interval crosses no difference as caption states. | No P/test for all-participant row. | PASS_1_COMPLETE |
| S040 | Forest plot riluzole-use subgroup differences: DOC-004 pp. 18-20 eTable 4. | Both subgroup estimates lie within their CIs; both cross no difference; displayed interaction P=.22 is not a within-row effect P. | Interaction test specification absent. | PASS_1_COMPLETE |
| S041 | Forest plot edaravone-use subgroup differences: DOC-004 pp. 18-20 eTable 4. | Both estimates lie within CIs; both cross no difference; interaction P=.19 is label-compatible. | Interaction test specification absent. | PASS_1_COMPLETE |
| S042 | Forest plot combined riluzole/edaravone-use subgroup differences: DOC-004 pp. 18-20 eTable 4. | All four estimates lie within CIs and cross no difference. | No test/P displayed. | PASS_1_COMPLETE |
| S043 | Forest plot age subgroup differences: DOC-004 pp. 18-20 eTable 4. | Both estimates lie within CIs and cross no difference; interaction P=.81 is label-compatible. | Interaction test specification absent. | PASS_1_COMPLETE |
| S044 | Forest plot sex subgroup differences: DOC-004 pp. 18-20 eTable 4. | Both estimates lie within CIs and cross no difference; interaction P=.50 is label-compatible. | Interaction test specification absent. | PASS_1_COMPLETE |
| S045 | Forest plot race/ethnicity subgroup differences: DOC-004 pp. 18-20 eTable 4. | White and non-Hispanic/Latino estimates each lie within CIs and cross no difference. | Other levels/test definitions are not printed. | PASS_1_COMPLETE |
| S046 | Forest plot weight subgroup differences: DOC-004 pp. 18-20 eTable 4. | All three estimates lie within CIs and cross no difference. | No test/P displayed. | PASS_1_COMPLETE |
| S047 | Forest plot BMI subgroup differences: DOC-004 pp. 18-20 eTable 4. | All five estimates lie within CIs and cross no difference. | No test/P displayed. | PASS_1_COMPLETE |
| S048 | Forest plot CKD subgroup differences: DOC-004 pp. 18-20 eTable 4. | Both estimates lie within CIs and cross no difference. | No test/P displayed. | PASS_1_COMPLETE |
| S049 | Forest plot symptom-onset subgroup differences: DOC-004 pp. 18-20 eTable 4. | Both estimates lie within CIs and cross no difference; interaction P=.59 is label-compatible. | Interaction test specification absent. | PASS_1_COMPLETE |
| S050 | Forest plot El Escorial/onset subgroup differences: DOC-004 pp. 18-20 eTable 4. | Both estimates lie within CIs and cross no difference; interaction P=.53 is label-compatible. | Interaction test specification absent. | PASS_1_COMPLETE |
| S051 | Forest plot baseline-severity subgroup differences: DOC-004 pp. 18-20 eTable 4. | Both estimates lie within CIs and cross no difference; interaction P=.38 is label-compatible. | Interaction test specification absent. | PASS_1_COMPLETE |
| S052 | Forest plot NfL subgroup differences: DOC-004 pp. 18-20 eTable 4. | Both estimates lie within CIs and cross no difference; interaction P=.74 is label-compatible. | Interaction test specification absent. | PASS_1_COMPLETE |
| S053 | Forest plot delta-FRS subgroup differences: DOC-004 pp. 18-20 eTable 4. | Both estimates lie within CIs and cross no difference; interaction P=.70 is label-compatible. | Interaction test specification absent. | PASS_1_COMPLETE |
| S054 | DOC-002 primary endpoint/model: DOC-002 pp. 12, 25-27, 51-52, 60-65. | Protocol DRR definition, endpoint, and planned Bayesian model are internally label/scale compatible; they support, but do not replace, realized-result definitions. | Protocol is not a realized analysis output. | PASS_1_COMPLETE |
| S055 | DOC-002 shared-control analysis population: DOC-002 pp. 61-63. | Shared-control timing and population rules are supplied; no result value is compared without matched population/time. | No result-specific implemented-control listing here. | PASS_1_COMPLETE |
| S056 | DOC-002 endpoint scale and SVC measurement rules: DOC-002 pp. 51-52, 73-75. | ALSFRS-R and SVC direction/scale labels are internally compatible. | Planned protocol definitions may differ from later effective SAP details. | PASS_1_COMPLETE |
| S057 | DOC-002 safety inferential/summary definitions: DOC-002 pp. 55-59, 64-65. | Planned summaries and survival notation have no realized numerical comparator in this source. | Test/CI rules for every safety result are not specified here. | PASS_1_COMPLETE |
| S058 | DOC-002 regimen-specific primary endpoint/model: DOC-002 p. 112 and pp. 184-185. | Planned Bayesian repeated-measures endpoint and mortality-loss-to-follow-up label are internally compatible; no direct incompatible realized result found. | Separate regimen SAP details are referenced; no inference from absent details. | PASS_1_COMPLETE |
| S059 | DOC-002 regimen statistical considerations: DOC-002 p. 137 and p. 212. | No-early-success rule, simulation reference, and shared-control rationale are planned definitions only and are label-compatible. | Effective simulation/SAP details and realized decision path are not supplied. | PASS_1_COMPLETE |
| S060 | DOC-002 Figures 1-2 preclinical ANOVA/Dunnett relation: DOC-002 pp. 174-175. | Printed one-way-ANOVA/Dunnett threshold and graphical labels are retained; no numerical bars/SEs permit compatibility calculations. | Raw values, degrees of freedom, and multiplicity implementation absent. | PASS_1_COMPLETE |
| S061 | DOC-002 Figures 4-9 preclinical tests: DOC-002 pp. 176-183. | Printed ANOVA/Fisher, Mantel-Cox, t-test, and Breslow-Wilcoxon labels align with their labelled outcomes; no candidate from rasterized values. | Exact bar data, test statistics, sidedness, and variance definitions absent. | PASS_1_COMPLETE |
| S062 | DOC-003 master-SAP primary Bayesian analysis and multiplicity: DOC-003 pp. 18, 33-41. | Planned DRR direction, credible-interval label, and one-sided primary/closed-testing definitions are internally compatible. | This SAP has versioned revisions; it is not presumed to be the realized effective model without an explicit match. | PASS_1_COMPLETE |
| S063 | DOC-003 master-SAP repeated-measures, survival, CAFS, and event-analysis definitions: DOC-003 pp. 19, 23-24, 85-89, 119-126. | Effect-measure, scale, and planned CI/test labels are internally coherent. | Covariance selection, convergence outcomes, and realized analysis settings are absent. | PASS_1_COMPLETE |
| S064 | DOC-003 RGC-SAP primary DRR/sensitivity definitions: DOC-003 pp. 83, 116-117. | Primary estimand and active/placebo direction are compatible with the reported DRR construct. | V1.0/V3.0 version linkage to each article display is not supplied. | PASS_1_COMPLETE |
| S065 | DOC-003 RGC-SAP secondary hierarchy, NfL, and exploratory models: DOC-003 pp. 84-93, 117-130. | Planned test labels, NfL log-scale/back-transform convention, rate-difference label, and hierarchy are internally coherent. | Actual multiplicity path, model convergence, covariance, and estimand mapping per reported result are not supplied. | PASS_1_COMPLETE |

## Pass-1 coverage summary

- **Stable S records:** 65 (`S001`-`S065`), all `PASS_1_COMPLETE`.
- **Raw candidate records:** 4, detailed in `checkers/statistical_pass_1.md`; no C IDs assigned.
- **Display-zero records:** 0 (`DISPLAY_ZERO_NOT_CANDIDATE`).
- **No-applicable source units:** DOC-005 pp. 1-6 and DOC-006 p. 1; no inferential result relationship.

## Pass-2 completion update

- **Pass:** 2 of 2; **runtime agent ID:** `/root/statistics_pass_2`; **model/effort:** `gpt-5.6-terra` / `high`.
- **Scope:** all existing `S001`–`S065`, revisited against the complete numeric and cross-source records, stable ledger `C001`–`C008`, and mechanical recheck. Direct PDF confirmation was repeated for the matched-result displays in DOC-001 and DOC-004.
- **Outcome:** every S record below is `PASS_2_COMPLETE`. No new raw candidate was emitted. Existing candidates remain untouched. No display-zero P-value record occurred.

| Stable ID | Pass-2 status |
|---|---|
| S001 | PASS_2_COMPLETE |
| S002 | PASS_2_COMPLETE |
| S003 | PASS_2_COMPLETE |
| S004 | PASS_2_COMPLETE |
| S005 | PASS_2_COMPLETE |
| S006 | PASS_2_COMPLETE |
| S007 | PASS_2_COMPLETE |
| S008 | PASS_2_COMPLETE |
| S009 | PASS_2_COMPLETE |
| S010 | PASS_2_COMPLETE |
| S011 | PASS_2_COMPLETE |
| S012 | PASS_2_COMPLETE |
| S013 | PASS_2_COMPLETE |
| S014 | PASS_2_COMPLETE |
| S015 | PASS_2_COMPLETE |
| S016 | PASS_2_COMPLETE |
| S017 | PASS_2_COMPLETE |
| S018 | PASS_2_COMPLETE |
| S019 | PASS_2_COMPLETE |
| S020 | PASS_2_COMPLETE |
| S021 | PASS_2_COMPLETE |
| S022 | PASS_2_COMPLETE |
| S023 | PASS_2_COMPLETE |
| S024 | PASS_2_COMPLETE |
| S025 | PASS_2_COMPLETE |
| S026 | PASS_2_COMPLETE |
| S027 | PASS_2_COMPLETE |
| S028 | PASS_2_COMPLETE |
| S029 | PASS_2_COMPLETE |
| S030 | PASS_2_COMPLETE |
| S031 | PASS_2_COMPLETE |
| S032 | PASS_2_COMPLETE |
| S033 | PASS_2_COMPLETE |
| S034 | PASS_2_COMPLETE |
| S035 | PASS_2_COMPLETE |
| S036 | PASS_2_COMPLETE |
| S037 | PASS_2_COMPLETE |
| S038 | PASS_2_COMPLETE |
| S039 | PASS_2_COMPLETE |
| S040 | PASS_2_COMPLETE |
| S041 | PASS_2_COMPLETE |
| S042 | PASS_2_COMPLETE |
| S043 | PASS_2_COMPLETE |
| S044 | PASS_2_COMPLETE |
| S045 | PASS_2_COMPLETE |
| S046 | PASS_2_COMPLETE |
| S047 | PASS_2_COMPLETE |
| S048 | PASS_2_COMPLETE |
| S049 | PASS_2_COMPLETE |
| S050 | PASS_2_COMPLETE |
| S051 | PASS_2_COMPLETE |
| S052 | PASS_2_COMPLETE |
| S053 | PASS_2_COMPLETE |
| S054 | PASS_2_COMPLETE |
| S055 | PASS_2_COMPLETE |
| S056 | PASS_2_COMPLETE |
| S057 | PASS_2_COMPLETE |
| S058 | PASS_2_COMPLETE |
| S059 | PASS_2_COMPLETE |
| S060 | PASS_2_COMPLETE |
| S061 | PASS_2_COMPLETE |
| S062 | PASS_2_COMPLETE |
| S063 | PASS_2_COMPLETE |
| S064 | PASS_2_COMPLETE |
| S065 | PASS_2_COMPLETE |
