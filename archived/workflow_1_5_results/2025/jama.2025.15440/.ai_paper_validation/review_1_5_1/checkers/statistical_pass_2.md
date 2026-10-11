# Statistical Consistency Review — Pass 2

**Reviewer stage:** mandatory independent statistical pass 2  
**Scope:** every stable inferential-statistical relationship, S001-S024, in `statistics/relationship_inventory.md`; the complete stable ledger (C001, C002); `checkers/statistical_pass_1.md`, `checkers/numeric_consistency.md`, `checkers/cross_source_consistency.md`; and `verification/evidence_recheck.md`.  
**Source authority:** supplied PDFs were inspected directly for the cited main-article, SAP, and results-supplement locations. Current mapping and review artifacts were used only to locate and reconcile the already mapped relationships. No legacy scientific output or external source was used.

## Pass-2 result

All 24 relationships have an explicit `PASS_2_COMPLETE` record below. The direct recheck facts support the two already registered, distinct candidates: C001 concerns conflicting confidence-interval endpoints for one matched stroke rate ratio; C002 concerns the conditional nonpartition of stroke subtype event counts. Neither is removed, merged, adjudicated, or given a severity. No additional distinct candidate is emitted.

The P values encountered are conventional decimal values or inequalities (including `P < .001`); no coherent finite-precision `P = 0`/`p = 0.000` display was found. Thus no display-zero candidate was created.

## Relationship records

### S001 — Primary AF ratio of proportions

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-001 PDF pp. 1 and 4 and Figure 2 on p. 6 repeat 172/2520 (6.83%, displayed 6.8%) versus 136/2520 (5.40%, displayed 5.4%), ratio 1.26 (95% CI 1.02-1.57), P=.03. The printed count ratio rounds to 1.26; its ordered interval contains the estimate. The main/SAP chi-square and ITT labels agree, and the cross-source review found no different denominator, outcome source, time window, scale, or duplicate value. No new candidate.

### S002 — Anticoagulation-exposure permutation comparison

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-001 pp. 1, 3, and 5 reports 1.63 versus 1.14 months, difference 0.50 months (95% CI 0.24-0.75), P<.001; the SAP identifies a permutation comparison of calendar-month exposure. The displayed means differ by 0.49 before independent rounding and are compatible with a displayed 0.50 difference. The measure remains months of exposure, not a proportion, rate, or time-to-first-record result. Resampling output, count, and distribution are absent, so no unsupported P-value/CI reconstruction was made. No new candidate.

### S003 — Stroke time-to-event rate ratio

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** Direct recheck confirms DOC-001 p. 1 prints 69 (2.7%) versus 64 (2.5%), RR 1.08 (95% CI 0.76-1.53), while p. 5 and Figure 4B on p. 7 print the same counts, percentages, 2.5-year context, and RR 1.08 but 95% CI 0.77-1.51. The cross-source difference is already registered as C001 and is not a new pass-2 candidate. Each interval is ordered and contains 1.08; no O-E, V, event times, unrounded endpoints, or interval construction is supplied to select an intended interval. C001's mechanical recheck establishes the direct reporting mismatch and names those missing inputs.

### S004 — Chi-square and heterogeneity test rules

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-001 p. 3 and DOC-003 pp. 18-19 consistently define ITT chi-square comparisons for the primary outcome/subgroups and heterogeneity testing. The source provides no heterogeneity statistic, degrees of freedom, covariance, or model matrix. This definition record has no repeated numerical result that conflicts across sources; no inference beyond the stated test labels was made. No new candidate.

### S005 — Log-rank rate-ratio and censoring rule

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-001 p. 3 labels time-to-event comparisons as log-rank analyses and defines RR as `exp((O-E)/V)` with outcome-specific censoring; DOC-003 p. 19 supplies the matching planned AF time-to-event framework. Labels, direction, and scale agree. O-E, V, risk sets, event times, and CI rule are unavailable, so neither a rate-ratio interval nor P value was reconstructed. No new candidate.

### S006 — Permutation and multiplicity rules

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-001 p. 3 and DOC-003 pp. 18 and 22 agree on permutation testing for time-with-known-AF and anticoagulation exposure, two-sided primary-outcome alpha, and no formal multiplicity adjustment for secondary/exploratory analyses. No conflicting alpha, test label, effect scale, or stated resampling definition was found. The absence of individual resampling outputs prevents further compatibility computation. No new candidate.

### S007 — Detailed primary AF ratio

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** The detailed p. 4 and Figure 2 p. 6 primary-result values exactly repeat S001: 172/2520 versus 136/2520, ratio 1.26 (1.02-1.57), P=.03. Cross-lane denominator checks and the supplied ITT/chi-square definition are compatible. This is a true repetition, not a distinct inferential relationship or duplicate-value contradiction. No new candidate.

### S008 — Time to first primary-care AF

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-001 pp. 3, 5, and 6 reports log-rank RR 1.29 (95% CI 1.03-1.61), P=.03 through 2.5 years; DOC-003 p. 19 gives the matching endpoint and censoring definition. The RR is inside ordered endpoints and its direction agrees with the labelled patch-versus-usual-care curves. A CI-derived two-sided diagnostic is only approximately compatible with .03 because time-to-event inputs are missing; it is not a substitute for the stated log-rank analysis. No new candidate.

### S009 — Mean days with known AF permutation comparison

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-001 p. 5 gives 41 (37-45) versus 21 (17-25) days, difference 20 (13-28), P<.001. DOC-003 p. 18 defines the 5-year secondary permutation outcome and p. 19 separately specifies the 2.5-year exploratory counterpart; this resolves the apparent planning-window difference. The means, contrast, direction, and day scale agree; marginal CIs were not subtracted. Simulation details and raw data are absent. No new candidate.

### S010 — Oral-anticoagulation prescription proportion comparison

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-001 p. 5 reports 364/2520 (14.4%) versus 322/2520 (12.8%), RR 1.13 (0.98-1.30), P=.08, and DOC-003 p. 19 specifies the comparable chi-square proportion analysis. The count ratio rounds to 1.13; the ordered CI includes 1 and is directionally compatible with the displayed P value. It is distinct from calendar-month exposure (S002) and time-to-first record (S011), so no rate/count or duplicate-result issue arises. No new candidate.

### S011 — Time to first oral-anticoagulation record

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-001 pp. 3, 5, and 7 reports log-rank RR 1.15 (0.99-1.34), P=.07; DOC-003 pp. 19-20 supplies the planned time-to-record/censoring framework. Estimate containment and interval order are correct, and this time-to-event measure is separately labelled from the prescription proportion and exposure-month comparison. A CI-only diagnostic is compatible at displayed precision; missing event-time inputs preclude an exact calculation. No new candidate.

### S012 — Figure 2 overall and heterogeneity P values

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-001 p. 6 prints the repeated primary overall P=.03, age heterogeneity P=.78, sex heterogeneity P=.06, and unadjusted 95% CIs. The primary result matches S001/S007. Subgroup labels, counts, ratios, direction, and the SAP plan agree; no heterogeneity statistic, degrees of freedom, or covariance is supplied to compute a replacement P value. No new candidate.

### S013 — Figure 4B death and stroke rate ratios

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** Direct Figure 4B inspection confirms every printed rate ratio lies within ordered 95% CI endpoints and directions accord with the arm event displays. The `Any stroke` RR/CI repeats the detailed side of C001 (S003). The patch stroke subtype count arithmetic, 60+12=72 versus `Any stroke` 69, is already the distinct stable candidate C002: its recheck establishes that the figure calls cells event counts but does not establish mutually exclusive, exhaustive participant-level subtype rows. Therefore C002 remains a conditional counting-rule issue; it does not prove a new rate-ratio, denominator, or scale contradiction. No P values, O-E, V, or CI method are supplied. No new candidate.

### S014 — Planned primary AF analysis

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-003 pp. 7-9 and 18 defines an ITT primary-care AF proportion through 2.5 years with chi-square testing, ratio of proportions, and 95% CI. It matches DOC-001 pp. 3-4 and S001/S007 on population, follow-up, comparator, measure, and scale. No planning quantity is falsely treated as an observed result. No new candidate.

### S015 — Planned subgroup and heterogeneity analyses

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-003 pp. 9 and 18 plans the <80/at-least-80 and sex subgroup comparisons and heterogeneity tests shown in DOC-001 p. 6. The strata and endpoint are matched; the reported CIs are expressly unadjusted and no changed estimand is labelled. Missing heterogeneity test statistics and model details prevent a numerical reanalysis. No new candidate.

### S016 — Planned and reported mean time with known AF

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** The SAP separately defines the 5-year secondary and 2.5-year exploratory permutation outcomes (DOC-003 pp. 18-19); the main article reports the latter through 2.5 years. The differing window is explicitly named, so it is not a population, scale, or cross-source mismatch. The reported direction and days scale are consistent with S009. No new candidate.

### S017 — Sensitivity primary/secondary-care AF analysis

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-003 p. 18 specifies AF captured in either primary or secondary care for sensitivity analyses; DOC-001 p. 5 refers to these analyses and DOC-004 p. 8 gives the detailed results (S022-S023). The expanded outcome source explains its distinct counts from the primary-care-only analysis; it is not a duplicate-value or denominator contradiction. No new candidate.

### S018 — Planned time-to-first-AF analysis

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-003 p. 19 explicitly plans 2.5- and 5-year cumulative-incidence analyses, time origin, censoring, and log-rank testing. DOC-001 reports the specified 2.5-year primary-care result. Endpoint, time scale, direction, and RR label match; no output for an exact test-statistic calculation is supplied. No new candidate.

### S019 — Planned anticoagulation analyses

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-003 pp. 19-20 specifies three distinct outcomes—participant record proportion/chi-square, calendar-month exposure/permutation, and time to first record/log-rank—that DOC-001 reports as S010, S002, and S011. Their labels, units, time horizons, and effect measures remain distinct. The review found no inappropriate substitution of a rate, count, proportion, or months-based quantity. No new candidate.

### S020 — Power, alpha, and multiplicity

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-003 pp. 21-22 and DOC-001 p. 3 agree on planning sample sizes, expected 1.75% versus 4.4% AF risks, approximate ratio 2.5, two-sided alpha, and multiplicity qualification. These are labelled prospective assumptions rather than claims that they equal observed trial results. No new candidate.

### S021 — eTable 2 association tests

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** Direct DOC-004 pp. 5-6 inspection confirms eTable 2's categorical chi-square, ordinal trend, and continuous-variable test labels, stated missing-data exclusion, denominator labels, and displayed P values. Counts and means/SDs have no observed duplicate, direction, label, or scale conflict with their comparator columns. The source does not identify the exact distribution decision, test statistic, or all test inputs; no unwarranted recalculation was made. No new candidate.

### S022 — Sensitivity overall ratio of proportions

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-004 p. 8 prints 251/2520 (9.96%) versus 207/2520 (8.21%), difference 1.75% (0.16%-3.33%), ratio 1.21 (1.02-1.45), P=.03. The count ratio rounds to 1.21, the estimate lies in ordered endpoints, and a count-based diagnostic is compatible at displayed precision. The figure explicitly labels the endpoint as primary-or-secondary-care AF, so values are not compared as duplicates of S001. No new candidate.

### S023 — Sensitivity subgroup heterogeneity P values

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-004 p. 8 reports age heterogeneity P=.28 and sex heterogeneity P=.07 with correctly labelled subgroup ratios, CIs, and unadjusted-multiplicity note. The component counts and directions support the labels. No test statistic, degrees of freedom, covariance, or exact heterogeneity procedure is supplied, so a new calculated P value would require unsupported assumptions. No new candidate.

### S024 — Urgent-patch-report to primary-care-AF Kaplan-Meier display

**PASS_2_COMPLETE**  
**Pass-2 reconciliation:** DOC-004 p. 10 labels the 89-case restricted Kaplan-Meier display, risk sets 89, 34, 18, 10, 8, 7, and 6, and the explicit convention that seven records predating urgent report are immediate events. This agrees with the urgent-report context in DOC-001 p. 5. Risk sets are not event totals; no RR, CI, P value, individual event times, or censoring count is printed. No new candidate.

## Candidate and recheck reconciliation

- **Existing candidates revisited:** 2 of 2 (C001, C002).
- **C001:** The mechanical recheck found and matched all three cited main-article locations. It reproduces the direct 0.01 lower- and 0.02 upper-endpoint discrepancy after matching outcome, groups, counts, follow-up, and RR. Missing O-E/V, event times, CI construction, and unrounded endpoints prevent selection of either displayed interval. Retained unchanged as Pending Human Adjudication.
- **C002:** The mechanical recheck reproduces the direct patch arithmetic `60 + 12 = 72` versus 69 and the usual-care arithmetic `58 + 6 = 64`. It also confirms the source does not state an exclusivity, unit-of-count, deduplication, recurrence, or subtype-overlap rule. Retained unchanged as Pending Human Adjudication; this pass does not convert the conditional observation into a definitive partition claim.
- **New distinct candidates:** 0. No provisional candidate requires coordinator registration or further mechanical recheck.

## Limitations

- Aggregate PDFs do not supply the event-time data, risk-set histories, O-E/V values, variance estimators, unrounded endpoints, model matrices, covariance, heterogeneity statistics/degrees of freedom, or permutation distributions needed to reproduce every inferential output. These missing definitions were not inferred from convention.
- The review applies diagnostic count/interval checks only where the source provides compatible definitions and prints the necessary quantities. Diagnostics do not replace the stated analyses.
- C001 and C002 remain quality-control candidates only, pending human adjudication; this pass makes no validity, severity, correction, acceptance, exclusion, or final-disposition determination.
