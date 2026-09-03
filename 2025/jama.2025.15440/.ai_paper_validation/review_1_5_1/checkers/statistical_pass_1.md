# Statistical Consistency Review — Pass 1

**Reviewer stage:** mandatory independent statistical pass 1  
**Scope:** stable inferential-statistical relationships S001-S024, the complete set in `statistics/relationship_inventory.md`.  
**Direct-source confirmation:** source-linked extraction maps were used as locators; the relevant printed values and definitions were independently checked in DOC-001 (`jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`), DOC-003 (`joi250068supp2_prod_1760999665.29862.pdf`), and DOC-004 (`joi250068supp3_prod_1760999665.30362.pdf`).  
**Pass result:** 24/24 relationships have `PASS_1_COMPLETE`. One provisional candidate (SP1001) is emitted. No displayed `P = 0`, `p = 0.000`, or equivalent display-zero result was encountered in this scope.

## Relationship records

### S001 — Primary AF ratio of proportions

**PASS_1_COMPLETE**  
**Outcome:** Coherent.  
**Evidence:** DOC-001 PDF pp. 1 and 4 print 172/2520 (6.83%) versus 136/2520 (5.40%), ratio 1.26 (95% CI 1.02-1.57), P=.03; the methods specify an ITT chi-square comparison.  
**Checks:** The printed ratio is 0.06825397 / 0.05396825 = 1.2647, which rounds to 1.26. A diagnostic log-ratio interval from the displayed counts is exp[ln(1.2647) +/- 1.96 sqrt(1/172 - 1/2520 + 1/136 - 1/2520)] = 1.02 to 1.57 after rounding. The estimate is contained, endpoints are ordered, and a two-sided chi-square diagnostic from the displayed counts is compatible with P=.03. Repetition across abstract, narrative, and Figure 2 agrees.

### S002 — Anticoagulation-exposure permutation comparison

**PASS_1_COMPLETE**  
**Outcome:** Coherent; inferential-detail limitation recorded.  
**Evidence:** DOC-001 PDF pp. 1, 3, and 5 print means 1.63 versus 1.14 months, difference 0.50 months (95% CI 0.24-0.75), P<.001; methods identify a permutation test for total exposure.  
**Checks:** Direction, point estimate, ordered interval, and repeated values agree. The displayed arm-mean subtraction is 0.49 months before rounding and is compatible with the printed 0.50; the source does not supply raw values, resampling count, or permutation distribution, so a P-value/interval reconstruction is not applicable. `P<.001` is not a display zero.

### S003 — Stroke time-to-event rate ratio

**PASS_1_COMPLETE**  
**Outcome:** Provisional candidate SP1001.  
**Evidence:** DOC-001 PDF p. 1 abstract prints stroke 69 (2.7%) versus 64 (2.5%), rate ratio 1.08 (95% CI 0.76-1.53). DOC-001 PDF p. 5 narrative and p. 7 Figure 4B print the same arm counts and rate ratio 1.08 but 95% CI 0.77-1.51. Methods on PDF p. 3 identify time-to-event/log-rank-derived rate ratios and state different censoring handling for stroke than for primary-care AF.  
**Checks:** Each printed interval contains 1.08 and has ordered endpoints; both directions agree with the displayed counts. The two intervals are nevertheless not identical for the same stated outcome, contrast, follow-up, event counts, and rate-ratio point estimate. No compatible O-E or V values are supplied, so neither interval can be selected by recalculation.

### S004 — Chi-square and heterogeneity test rules

**PASS_1_COMPLETE**  
**Outcome:** Coherent definition record.  
**Evidence:** DOC-001 PDF p. 3 defines ITT chi-square comparisons for the primary outcome and age/sex subgroups, with chi-square heterogeneity tests. DOC-003 PDF p. 18 supplies the matching planned definition.  
**Checks:** The main-method and SAP definitions agree. This is a rule-only relationship; no test statistic, degrees of freedom, or output is printed here for independent numerical reconstruction.

### S005 — Log-rank rate-ratio and censoring rule

**PASS_1_COMPLETE**  
**Outcome:** Coherent definition record.  
**Evidence:** DOC-001 PDF p. 3 states log-rank comparisons and RR=exp((O-E)/V), and identifies censoring rules; DOC-003 PDF p. 19 describes the matching time-to-AF analysis.  
**Checks:** Formula, effect-measure label, and stated time-to-event direction are internally consistent. O-E and V are not supplied, so rate-ratio CIs or P values cannot be independently recreated from this definition alone.

### S006 — Permutation and multiplicity rules

**PASS_1_COMPLETE**  
**Outcome:** Coherent definition record.  
**Evidence:** DOC-001 PDF p. 3 states permutation testing for days with AF and anticoagulation exposure, two-sided P<.05 for the primary outcome, and no formal multiplicity adjustment for secondary/sensitivity/exploratory results. DOC-003 PDF pp. 18 and 22 provides the matching empirical-permutation and multiplicity language.  
**Checks:** No conflicting threshold, effect label, or inferential definition was observed. The source supplies no common resampling output for a numerical compatibility check.

### S007 — Detailed primary AF ratio

**PASS_1_COMPLETE**  
**Outcome:** Coherent.  
**Evidence:** DOC-001 PDF p. 4 and Figure 2 on p. 6 print 172/2520 versus 136/2520, ratio 1.26 (95% CI 1.02-1.57), P=.03.  
**Checks:** This is an exact detailed repetition of S001. The displayed-count diagnostic reproduces ratio 1.2647, the interval is ordered and contains the estimate, and the sign/direction and P-value are compatible with the stated chi-square comparison.

### S008 — Time to first primary-care AF

**PASS_1_COMPLETE**  
**Outcome:** Coherent.  
**Evidence:** DOC-001 PDF pp. 3, 5, and 6 print log-rank RR 1.29 (95% CI 1.03-1.61), P=.03 for first postrandomization primary-care AF through 2.5 years. DOC-003 PDF p. 19 gives the matched planned 2.5-year time-to-AF definition.  
**Checks:** The RR is inside an ordered CI and direction agrees with earlier AF detection in the patch group. As a diagnostic only, ln(1.29) divided by [(ln(1.61)-ln(1.03))/3.92] is about 2.24, compatible after rounding with a two-sided P near .03; the exact log-rank O-E/V inputs are not printed.

### S009 — Mean days with known AF permutation comparison

**PASS_1_COMPLETE**  
**Outcome:** Coherent; inferential-detail limitation recorded.  
**Evidence:** DOC-001 PDF pp. 3 and 5 print 41 (95% CI 37-45) versus 21 (17-25) days, difference 20 (13-28), P<.001. DOC-003 PDF p. 18 defines the empirical permutation calculation, and p. 19 explicitly specifies the same framework for the exploratory 2.5-year outcome.  
**Checks:** The displayed difference and direction are coherent; 41-21=20 and the difference CI is ordered. The SAP distinguishes a five-year secondary outcome from its explicitly planned 2.5-year exploratory analogue, so the reported 2.5-year analysis is not a planning-window contradiction. Simulation count and result distribution are not supplied; P/CI reconstruction is therefore not applicable. `P<.001` is not a display zero.

### S010 — Oral-anticoagulation prescription proportion comparison

**PASS_1_COMPLETE**  
**Outcome:** Coherent.  
**Evidence:** DOC-001 PDF p. 5 prints 364/2520 (14.4%) versus 322/2520 (12.8%), relative risk 1.13 (95% CI 0.98-1.30), P=.08; methods identify an analogous ITT proportion comparison. DOC-003 PDF p. 19 specifies chi-square testing for this outcome.  
**Checks:** 364/322=1.1304, which rounds to 1.13. The CI is ordered and contains the estimate; its inclusion of 1 is directionally compatible with P=.08. A simple displayed-count two-sided proportion-test diagnostic is close to .08. The exact interval method is not supplied, so small differences from a log-Wald diagnostic do not establish a contradiction.

### S011 — Time to first oral-anticoagulation record

**PASS_1_COMPLETE**  
**Outcome:** Coherent.  
**Evidence:** DOC-001 PDF pp. 3, 5, and 7 print log-rank RR 1.15 (95% CI 0.99-1.34), P=.07. DOC-003 pp. 19-20 gives the planned time-to-record, censoring, and log-rank rules.  
**Checks:** RR is inside an ordered CI and direction matches greater occurrence/earlier record in the patch group. A CI-derived log-scale diagnostic gives a two-sided P approximately .07; exact time-to-event inputs are not printed.

### S012 — Figure 2 overall and heterogeneity P values

**PASS_1_COMPLETE**  
**Outcome:** Coherent; test-detail limitation recorded.  
**Evidence:** DOC-001 PDF p. 6 prints overall P=.03, age heterogeneity P=.78, sex heterogeneity P=.06, with 95% CIs not adjusted for multiplicity.  
**Checks:** The overall value repeats S001/S007; subgroup CIs and the stated heterogeneous-comparison labels do not conflict with the printed P values. The source does not provide heterogeneity test statistics, degrees of freedom, or model matrix; no further reconstruction is justified.

### S013 — Figure 4B death/stroke rate ratios

**PASS_1_COMPLETE**  
**Outcome:** Coherent; inferential-detail limitation recorded.  
**Evidence:** DOC-001 PDF p. 7 Figure 4B prints rate ratios (95% CIs): cardiovascular death 0.74 (0.47-1.17), presumed ischemic stroke 1.03 (0.72-1.48), noncardiovascular death 0.85 (0.62-1.17), any death 0.82 (0.63-1.06), any stroke 1.08 (0.77-1.51), and hemorrhagic stroke 1.94 (0.77-4.90).  
**Checks:** Every point estimate is contained in an ordered interval; values below/above 1 agree with the indicated patch-versus-usual-care event directions. The `any stroke` row is the detailed comparator in SP1001. No P values, O-E values, or variances are supplied for these figure rows, precluding further test reconstruction.

### S014 — Planned primary AF analysis

**PASS_1_COMPLETE**  
**Outcome:** Coherent cross-source definition.  
**Evidence:** DOC-003 PDF pp. 7-9 and 18 specifies an ITT primary-care AF proportion through 2.5 years, chi-square comparison, arm proportions, ratio of proportions, and 95% CI. DOC-001 PDF pp. 3-4 reports those same elements.  
**Checks:** Population, follow-up window, effect-measure label, direction, and test rule match the reported primary analysis. No unreported model detail has been inferred.

### S015 — Planned subgroup and heterogeneity analyses

**PASS_1_COMPLETE**  
**Outcome:** Coherent cross-source definition.  
**Evidence:** DOC-003 PDF pp. 9 and 18 plans <80 versus >=80 and sex subgroup chi-square comparisons with heterogeneity testing; DOC-001 PDF p. 6 reports the matching age and sex subgroup displays and heterogeneity P values.  
**Checks:** Strata labels, endpoint, comparison, and multiplicity qualification are consistent. No heterogeneity test statistic or degrees of freedom is supplied for numerical reconstruction.

### S016 — Planned and reported mean time with known AF

**PASS_1_COMPLETE**  
**Outcome:** Coherent cross-source definition.  
**Evidence:** DOC-003 PDF p. 18 defines the five-year secondary permutation analysis and its empirical P-value formula. DOC-003 PDF p. 19 separately and explicitly plans the 2.5-year exploratory version under the same framework. DOC-001 PDF pp. 3 and 5 reports that 2.5-year analysis.  
**Checks:** The apparent 5-year/2.5-year difference is explained within the SAP by the separately named 2.5-year exploratory analysis; it is not a cross-document inconsistency. The reported 2.5-year time window, direction, and permutation label align. Simulation number and raw distribution are absent.

### S017 — Sensitivity primary/secondary-care AF analysis

**PASS_1_COMPLETE**  
**Outcome:** Coherent cross-source definition.  
**Evidence:** DOC-003 PDF p. 18 plans sensitivity analyses using AF in primary or secondary-care records. DOC-001 PDF p. 5 refers to the sensitivity analyses, and DOC-004 PDF p. 8 displays them.  
**Checks:** Population, follow-up, and outcome-source expansion match across the sources. The detailed result is evaluated under S022-S023.

### S018 — Planned time-to-first-AF analysis

**PASS_1_COMPLETE**  
**Outcome:** Coherent cross-source definition.  
**Evidence:** DOC-003 PDF p. 19 plans 2.5- and 5-year AF time-to-event curves, censoring, and log-rank testing. DOC-001 PDF pp. 3, 5, and 6 reports the 2.5-year curve and log-rank RR.  
**Checks:** The reported analysis is the specified 2.5-year member of the planned analyses; endpoint, censoring description, time scale, direction, and effect-measure label are consistent.

### S019 — Planned anticoagulation analyses

**PASS_1_COMPLETE**  
**Outcome:** Coherent cross-source definition.  
**Evidence:** DOC-003 PDF pp. 19-20 plans a chi-square comparison for postrandomization record proportions, permutation comparison of calendar-month exposure, and log-rank time-to-record analysis. DOC-001 PDF pp. 3, 5, and 7 reports the matching 2.5-year outcomes.  
**Checks:** The reported proportion RR, months-based exposure, and time-to-record RR retain their respective effect labels and testing rules. The source’s month/year date precision explains reporting exposure in months; no rate/count confusion is present.

### S020 — Power, alpha, and multiplicity

**PASS_1_COMPLETE**  
**Outcome:** Coherent cross-source planning relationship.  
**Evidence:** DOC-003 PDF pp. 21-22 specifies initial n=2500, expanded n=5000, expected 1.75% versus 4.4% at 2.5 years, ratio approximately 2.5, two-sided alpha statements, and no formal multiplicity adjustment. DOC-001 PDF p. 3 reports the same planning quantities and qualification.  
**Checks:** Planning values, effect scale, direction, and multiplicity language agree. These are planning assumptions rather than observed-effect statistics, so no outcome-based recalculation was applied.

### S021 — eTable 2 association tests

**PASS_1_COMPLETE**  
**Outcome:** Coherent; definition and precision limitation recorded.  
**Evidence:** DOC-004 PDF pp. 5-6 eTable 2 prints categorical chi-square P values, Mantel-Haenszel trend P values for ordinal factors, two-sample t-test or Mann-Whitney U-test P values for continuous variables, and exclusion of missing data.  
**Checks:** Test labels match the displayed variable types and footnotes. The displayed category counts, means/SDs, and P values have no observed label, direction, or duplicate-value conflict. Exact test inputs, handling beyond the stated missing-data exclusion, and distributional determinations are not fully supplied; no calculation that assumes them was made.

### S022 — Sensitivity overall ratio of proportions

**PASS_1_COMPLETE**  
**Outcome:** Coherent.  
**Evidence:** DOC-004 PDF p. 8 eFigure 1 prints 251/2520 (9.96%) versus 207/2520 (8.21%), absolute difference 1.75% (0.16%-3.33%), ratio 1.21 (1.02-1.45), P=.03.  
**Checks:** 251/207=1.2126, which rounds to 1.21. A diagnostic log-ratio CI from the displayed counts is approximately 1.02 to 1.45, and its two-sided normal diagnostic is approximately .03. Point estimate containment, endpoint ordering, direction, effect label, and stated primary/secondary-care sensitivity endpoint are coherent.

### S023 — Sensitivity subgroup heterogeneity P values

**PASS_1_COMPLETE**  
**Outcome:** Coherent; test-detail limitation recorded.  
**Evidence:** DOC-004 PDF p. 8 eFigure 1 prints age heterogeneity P=.28 and sex heterogeneity P=.07, and labels its 95% CIs as unadjusted for multiplicity.  
**Checks:** The age and sex subgroup ratios/intervals are correctly labelled and directionally agree with their component counts. No test statistic, degrees of freedom, covariance, or exact heterogeneity method is supplied, so recalculation is not applicable.

### S024 — Urgent-patch-report to primary-care-AF Kaplan-Meier display

**PASS_1_COMPLETE**  
**Outcome:** Coherent.  
**Evidence:** DOC-004 PDF p. 10 eFigure 3 labels a Kaplan-Meier display restricted to 89 patch-detected AF cases, gives the risk set 89, 34, 18, 10, 8, 7, 6, and states that seven records predating the urgent report are counted as immediate events. DOC-001 PDF p. 5 reports the matched urgent-report context.  
**Checks:** The restriction, time origin, immediate-event convention, and risk-set label are explicit and nonconflicting. No RR, CI, P value, censoring count, or individual event times are supplied; no unsupported inference was made.

## Provisional candidate emitted by pass 1

### SP1001 — Conflicting stroke rate-ratio confidence intervals across matched main-article locations

**Candidate statement:** The DOC-001 abstract and detailed results/Figure 4B report the same stroke event counts and rate-ratio point estimate but different 95% confidence-interval endpoints.  
**Primary category:** Cross-document numeric inconsistency.  
**Exact source locations:** `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1` (abstract); `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=5` (results narrative); `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=7` (Figure 4B).  
**Direct observation:** Abstract: 69 (2.7%) versus 64 (2.5%), rate ratio 1.08 (95% CI 0.76-1.53). Narrative/Figure 4B: the same 69 versus 64 and rate ratio 1.08, but 95% CI 0.77-1.51. The figure caption identifies the same 2.5-year stroke time-to-event context.  
**Reproducible comparison:** Lower endpoints differ by 0.01 (0.76 versus 0.77) and upper endpoints by 0.02 (1.53 versus 1.51). This is a direct printed-value comparison; it does not assume a censoring rule, variance estimator, or CI construction method.  
**Alternative source-grounded interpretations:** The two locations may have been generated from different unreported calculation or rounding pipelines, or one may not have received a final update. The supplied package does not state that the abstract used a different estimand, population, follow-up, or confidence-interval method.  
**Missing definitions:** The source does not provide O-E, V, the exact CI procedure, or a statement explaining the interval difference; those omissions prevent selection of either interval as authoritative.  
**Human question:** For the matched 2.5-year any-stroke time-to-event comparison, which 95% CI pair is the intended reported interval, and is any difference in estimand or interval method intended?

## Pass-1 limitations

- Compatibility calculations are diagnostics based only on printed counts or intervals. They do not replace the reported analysis and were not used where the source lacks a compatible test, sidedness, variance, covariance, model, or resampling definition.
- No displayed P value in S001-S024 is a coherent finite-precision display zero; therefore `DISPLAY_ZERO_NOT_CANDIDATE` was not applicable in this scope.
- SP1001 is a quality-control candidate only and remains pending human adjudication; this pass assigns no validity, severity, correction, or final disposition.
