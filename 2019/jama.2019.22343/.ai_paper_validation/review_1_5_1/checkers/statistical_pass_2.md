# Statistical Consistency Pass 2

## Scope, independence, and completion

This fresh pass-2 review revisited all **71 of 71** canonical inferential relationships (`S001` through `S071`) against the complete current-run numeric and cross-source checker records, stable candidate ledger `C001`-`C006`, and mechanical evidence-recheck facts. Direct PDFs remained the authority; source pages were rechecked for the six existing candidate implications and the Figure 4 direction label.

Every row below is explicitly `PASS_2_COMPLETE`. This is a reviewer record only: it assigns no severity, validity, acceptance, rejection, correction, or other disposition.

- **Point estimate / interval checks:** every printed point estimate remains inside its own printed interval; every printed interval has lower endpoint no greater than upper endpoint.
- **Direction / label checks:** OR, RD, RR/incidence-rate, SMD, WMD, and unit labels remain compatible with the source definitions except for the already registered quality-of-life direction-label issue (`C003`).
- **P-value / test / SE compatibility:** threshold-direction screening is coherent wherever both a 95% interval and P value are printed. Exact CI/P/statistic/SE compatibility was not asserted because the sources do not provide a compatible per-result test statistic, degrees of freedom, standard error, confidence-interval construction, study weights, covariance, continuity correction, variance estimator, or mapping from rounded intervals to P values. The `S002` CI-to-P calculation remains a labelled diagnostic approximation only.
- **Display-zero rule:** no printed P-value display zero occurs. `S056` is a non-P serious-adverse-event incidence of `0 per patient (95% CI, 0.00-0.01)` and is not a display-zero candidate.

## Existing-candidate reconciliation

- **C001 / S001:** retained implication. The matched BPAP mortality displays print lower CI endpoints 0.50 (Figure 1) and 0.51 (abstract/narrative); the matched point estimate, upper endpoint, and 1423-patient total remain aligned.
- **C002 / S005:** retained implication. The matched BPAP quality-of-life displays print upper CI endpoints 0.38 (Figure 4) and 0.39 (abstract/narrative); the point estimate and 833-patient total remain aligned.
- **C003 / S005, S053, S054:** the direct Figure 4 orientation is **negative side favors NIPPV; positive side favors no NIPPV**. This corrects any contrary wording in earlier checker prose. The pass-2 source-grounded inconsistency is the methods statement that standardized quality-of-life direction used higher scores for better outcomes versus Table 2 footnote b stating higher scores indicate worse quality of life, with mixed native instrument directions in Supplement 2. Figure 4 alone does not establish the group-subtraction order; that definition is absent and is not inferred.
- **C004 / S024:** retained implication. The matched 14-patient CAT result has WMD 2.30 in both locations but CIs -2.23 to 6.83 (main article) and -2.35 to 6.95 (Supplement 2).
- **C005 / S020:** retained implication. The Cheung baseline rows visibly total 47 (24 + 23), while matched effectiveness displays state 49 patients; enrolled/randomized/baseline/outcome-analysis population definitions are absent.
- **C006 / S058 and concrete final-result contexts:** retained implication. The protocol explicitly places 3-18-study syntheses in a DerSimonian-Laird-plus-Knapp-Hartung branch, while the final article describes DerSimonian-Laird random effects for `k >= 3` without the adjustment. The supplied package does not state whether the adjustment was retained, omitted from prose, or amended.

## Relationship-level pass-2 record

| S ID | Pass-2 checks reconciled | Result |
|---|---|---|
| S001 | CI/order, OR direction, repeated locations, denominators, C001 and C006 context | PASS_2_COMPLETE — existing C001/C006 implication only |
| S002 | CI/order, OR direction, repeated locations, diagnostic CI-to-P review | PASS_2_COMPLETE — diagnostic only; compatible exact inferential definition absent |
| S003 | CI/order, OR direction, repeated locations, C006 model-rule context | PASS_2_COMPLETE — no new observation |
| S004 | CI/order, RR/rate label, repeated locations, C006 model-rule context | PASS_2_COMPLETE — no new observation |
| S005 | CI/order, SMD scale/direction, repeated locations, C002/C003 context | PASS_2_COMPLETE — existing C002/C003 implication only |
| S006 | CI/order, OR direction, denominators, repeated locations | PASS_2_COMPLETE — no new observation |
| S007 | CI/order, RR/incidence-rate label, repeated locations | PASS_2_COMPLETE — no new observation |
| S008 | CI/order, RR/incidence-rate label, adverse-event quantity | PASS_2_COMPLETE — no new observation |
| S009 | CI/order, RD/OR labels and direction | PASS_2_COMPLETE — no new observation |
| S010 | CI/order, RR/incidence-rate label and direction | PASS_2_COMPLETE — no new observation |
| S011 | CI/order, RR/incidence-rate label and direction | PASS_2_COMPLETE — no new observation |
| S012 | CI/order, RD/OR labels and direction | PASS_2_COMPLETE — no new observation |
| S013 | CI/order, RR/incidence-rate label and direction | PASS_2_COMPLETE — no new observation |
| S014 | CI/order, RD/OR labels and direction | PASS_2_COMPLETE — no new observation |
| S015 | CI/order, SMD direction/scale label | PASS_2_COMPLETE — no new observation |
| S016 | CI/order, SMD direction/scale label | PASS_2_COMPLETE — no new observation |
| S017 | CI/order, SMD direction/scale label | PASS_2_COMPLETE — no new observation |
| S018 | CI/order, mean-difference unit/direction | PASS_2_COMPLETE — no new observation |
| S019 | CI/order, mean-difference unit/direction | PASS_2_COMPLETE — no new observation |
| S020 | CI/order, RD/OR labels, cross-table total, C005 | PASS_2_COMPLETE — existing C005 implication only |
| S021 | percentage direction, population/duration label, repeated location | PASS_2_COMPLETE — no new observation |
| S022 | rate-per-patient versus count label, adherence population, repeated location | PASS_2_COMPLETE — no new observation |
| S023 | rate-per-patient versus count label, adherence population, repeated location | PASS_2_COMPLETE — no new observation |
| S024 | CI/order, CAT higher-worse label, cross-source repetition, C004 | PASS_2_COMPLETE — existing C004 implication only |
| S025 | CI/order, RD/OR labels and direction | PASS_2_COMPLETE — no new observation |
| S026 | CI/order, WMD and SGRQ higher-worse label | PASS_2_COMPLETE — no new observation |
| S027 | CI/order, WMD/meters unit and direction | PASS_2_COMPLETE — no new observation |
| S028 | CI/order, WMD and ESS higher-worse label | PASS_2_COMPLETE — no new observation |
| S029 | CI/order, RD/OR labels and direction | PASS_2_COMPLETE — no new observation |
| S030 | CI/order, WMD and SRIQ higher-better label | PASS_2_COMPLETE — no new observation |
| S031 | CI/order, WMD and MRC higher-worse label | PASS_2_COMPLETE — no new observation |
| S032 | CI/order, WMD/meters unit and direction | PASS_2_COMPLETE — no new observation |
| S033 | CI/order, admissions WMD/count label | PASS_2_COMPLETE — no new observation |
| S034 | CI/order, WMD and SRIQ higher-better label | PASS_2_COMPLETE — no new observation |
| S035 | CI/order, WMD/meters unit and direction | PASS_2_COMPLETE — no new observation |
| S036 | CI/order, OR direction, stable-population label | PASS_2_COMPLETE — no new observation |
| S037 | CI/order, RR/incidence-rate label, stable-population label | PASS_2_COMPLETE — no new observation |
| S038 | CI/order, OR direction, stable-population label | PASS_2_COMPLETE — no new observation |
| S039 | CI/order, SMD direction/scale; no P printed | PASS_2_COMPLETE — no new observation |
| S040 | CI/order, OR direction, recent-exacerbation label | PASS_2_COMPLETE — no new observation |
| S041 | CI/order, SMD direction/scale, recent-exacerbation label | PASS_2_COMPLETE — no new observation |
| S042 | CI/order, RR/incidence-rate label, recent-exacerbation label | PASS_2_COMPLETE — no new observation |
| S043 | CI/order, OR direction, recent-exacerbation label | PASS_2_COMPLETE — no new observation |
| S044 | CI/order, SMD direction/PaCO2 subgroup label | PASS_2_COMPLETE — no new observation |
| S045 | CI/order, SMD direction/PaCO2 subgroup label | PASS_2_COMPLETE — no new observation |
| S046 | CI/order, SMD direction/PaCO2 subgroup label | PASS_2_COMPLETE — no new observation |
| S047 | CI/order, OR direction, RCT-only label | PASS_2_COMPLETE — no new observation |
| S048 | CI/order, OR direction, observational-only label | PASS_2_COMPLETE — no new observation |
| S049 | CI/order, OR direction, RCT-only label | PASS_2_COMPLETE — no new observation |
| S050 | CI/order, OR direction, observational-only label | PASS_2_COMPLETE — no new observation |
| S051 | CI/order, RR/incidence-rate label, RCT-only label | PASS_2_COMPLETE — no new observation |
| S052 | CI/order, RR/incidence-rate label, observational-only label | PASS_2_COMPLETE — no new observation |
| S053 | CI/order, standardized-QOL scale, Table 2/figure direction, C003 | PASS_2_COMPLETE — existing C003 implication only |
| S054 | CI/order, standardized-QOL scale, Table 2/figure direction, C003 | PASS_2_COMPLETE — existing C003 implication only |
| S055 | incidence estimate/CI order, rate-versus-count label | PASS_2_COMPLETE — no new observation |
| S056 | incidence estimate/CI order, non-P zero, rate-versus-count label | PASS_2_COMPLETE — non-P zero not a candidate |
| S057 | incidence estimate/CI order, rate-versus-count label | PASS_2_COMPLETE — no new observation |
| S058 | protocol model-rule wording, final-article comparison, C006 | PASS_2_COMPLETE — existing C006 implication only |
| S059 | protocol heterogeneity/subgroup/sensitivity/funnel definitions | PASS_2_COMPLETE — no source-defined numerical comparison applicable |
| S060 | SOE definition/label identity | PASS_2_COMPLETE — no source-defined numerical comparison applicable |
| S061 | eligibility/titration/use thresholds and units | PASS_2_COMPLETE — no new observation |
| S062 | IVAPS/BPAP-ST thresholds, titration, use units | PASS_2_COMPLETE — no new observation |
| S063 | physiologic eligibility/titration target thresholds and units | PASS_2_COMPLETE — no new observation |
| S064 | adherence/use definition, nested population and units | PASS_2_COMPLETE — no new observation |
| S065 | stated direction and P label; no effect/CI/test mapping supplied | PASS_2_COMPLETE — no new observation |
| S066 | stated direction and P label; no effect/CI/test mapping supplied | PASS_2_COMPLETE — no new observation |
| S067 | stated direction and P label; no effect/CI/test mapping supplied | PASS_2_COMPLETE — no new observation |
| S068 | CI/order, WMD and MRC higher-worse label | PASS_2_COMPLETE — no new observation |
| S069 | duration contrast, SGRQ higher-worse label, P display | PASS_2_COMPLETE — no new observation |
| S070 | CI/order, RD/OR labels, percentage/denominator context | PASS_2_COMPLETE — no new observation |
| S071 | comparison/outcome label; no estimate, CI, or P supplied | PASS_2_COMPLETE — no new observation |

## Candidate-discovery result

- **New candidate proposals for append:** **0**.
- **Append required:** **No.** No new independent supplied-source contradiction was found. Existing candidates remain in the stable ledger without renumbering or disposition.

## Limitations and missing definitions

- Exact effect-test definitions, degrees of freedom, SEs, covariance, variance estimator, continuity corrections, final weights, unrounded estimates/intervals, and a per-result CI-to-P mapping are not supplied; diagnostic approximations were not promoted to candidates.
- The group-subtraction order for standardized quality-of-life effects is not explicitly supplied. Figure 4 orientation was read directly and is reported above; no contrary orientation was inferred.
- No printed P-value display zero was found. No threshold for replacing a display zero was derived or prescribed.
