# Statistical Consistency Pass 2

## Scope and method

This independent pass-2 review revisited every canonical inferential relationship `S001` through `S083` after reading the complete stable candidate ledger (`C001`-`C009`), mechanical evidence recheck, numeric-consistency check, cross-source-consistency check, and statistical pass 1. Direct PDF evidence and the current source-matched records were used as the authority. No source, reused asset, relationship inventory, candidate ledger, or other artifact was modified by this pass.

For every applicable relationship, this pass checked point-estimate containment, interval endpoint ordering, null/direction agreement, effect-measure and scale labels, duplicate/repeated-value status, applicable denominator or population implications, and cross-source/recheck implications. Exact interval-to-P-value, test-statistic, or SE reconstruction was not performed unless compatible model and inferential definitions were supplied; none of the source records supplies a matched variance estimator and exact CI/test construction for a definitive identity calculation. Any crude event-proportion comparison below is explicitly diagnostic and is not a reconstruction of a hazard or subdistribution-hazard model.

- **Assigned relationship coverage:** `S001`-`S083` (83 of 83).
- **Complete candidate ledger read:** `C001`, `C002`, `C003`, `C004`, `C005`, `C006`, `C007`, `C008`, and `C009`.
- **New distinct pass-2 leads:** 0.
- **Display-zero review:** `DISPLAY_ZERO_NOT_CANDIDATE` records: 0. No assigned relationship prints `P = 0`, `p = 0.000`, or an equivalent finite-precision display zero. The `P=1.00` in S063 is not a display zero.
- **Existing-ledger implication:** C005 applies to S023; C006 applies to S055-S057; C008 applies to S001-S012 and S018 as a time-origin definition comparison; and C009 applies directly to S009-S012. C001, C002, C003, C004, and C007 were also considered for population, denominator, label, and cross-source implications where relevant. None supplies a new, distinct contradiction for another S record.

## Complete relationship recheck

| Relationship | Pass-2 source-grounded recheck | Status |
|---|---|---|
| S001 | HR 0.76 is contained in ordered 95% CI 0.50-1.14; the CI crosses 1 and P=.18. Abstract, narrative, and Figure 2A repeat the matched result. C008 identifies a protocol/report time-origin definition difference, but does not supply a different observed estimate. Cox-HR label and vitamin-D-below-placebo curve direction agree. | PASS_2_COMPLETE |
| S002 | HR 0.95 is contained in 0.57-1.57; CI crosses 1 and P=.83. Matched abstract, narrative, and Figure 2B displays agree. C008 is a definition-level time-origin comparison only; no different observed OS estimate is printed. | PASS_2_COMPLETE |
| S003 | HR 0.46 is contained in 0.24-0.86; CI excludes 1 and P=.02. Narrative, Figure 3A, and multiple-imputation duplicate S044 agree at printed precision and retain the middle-stratum Cox-HR label. C008 supplies no competing numeric result. | PASS_2_COMPLETE |
| S004 | HR 1.15 is contained in 0.65-2.05; CI crosses 1 and P=.63. Figure 3B and multiple-imputation duplicate S043 agree at printed precision; its low stratum is not interchangeable with S003. | PASS_2_COMPLETE |
| S005 | The interaction P=.04 is separately labelled from the subgroup HR P values. The source identifies a low-versus-middle Cox interaction but supplies no interaction estimate, CI, statistic, or matched variance definition. | PASS_2_COMPLETE |
| S006 | HR 0.60 is contained in 0.28-1.30; CI crosses 1 and P=.20. Figure 3C and multiple-imputation duplicate S046 agree at printed precision; the outcome label is all-cause death. | PASS_2_COMPLETE |
| S007 | HR 1.36 is contained in 0.66-2.81; CI crosses 1 and P=.41. Figure 3D and multiple-imputation duplicate S045 agree at printed precision. | PASS_2_COMPLETE |
| S008 | The death interaction P=.13 is separately printed from within-stratum P values. No interval, statistic, or compatible test definition is supplied for exact recheck. | PASS_2_COMPLETE |
| S009 | Subdistribution HR 0.75 is contained in 0.48-1.17; CI crosses 1 and P=.21. Figure 2C and Table 2 agree and identify a competing-risk subdistribution HR, distinct from S001's Cox HR. C009 independently identifies the Table 2 direction footnote as opposite the curve/narrative direction; it is an existing ledger candidate, not a new pass-2 lead. | PASS_2_COMPLETE |
| S010 | Low HR 1.18 (0.64-2.19), P=.59 and middle HR 0.44 (0.21-0.89), P=.02 each pass containment/order and null/P screening. P=.04 is separately labelled interaction P. C009's Table 2 direction footnote applies to the displayed subdistribution-HR orientation; it does not create a second issue for the values themselves. | PASS_2_COMPLETE |
| S011 | Total/low/middle cancer-specific-death HRs 1.09/1.45/0.78 are each contained in their ordered CIs, which cross 1; P=.80/.38/.63. C009's footnote conflict is directly applicable: the reported total HR above 1 accompanies a diagnostically higher crude vitamin-D event proportion, whereas the footnote says HR>1 means decreased probability. Crude proportions are diagnostic only; event times and exact HR inputs are absent. | PASS_2_COMPLETE |
| S012 | Total/low/middle noncancer-death HRs 0.70/1.11/0.39 are each contained in ordered CIs crossing 1; P=.44/.89/.15. C009 directly applies: the total HR below 1 accompanies a diagnostically lower crude vitamin-D event proportion, opposite the footnote's stated orientation. No exact time-to-event reconstruction is attempted. | PASS_2_COMPLETE |
| S013 | Age-adjusted HR 0.66 (0.43-0.99), P=.048 and HR 0.81 (0.48-1.36), P=.42 pass containment/order and null/P screening. They are adjustment-specific, not duplicates of S001/S002. Stage-I-adjusted claims have no printed estimate, interval, statistic, or SE. | PASS_2_COMPLETE |
| S014 | Named Wilcoxon signed-rank and Mann-Whitney analyses distinguish within- and between-group P values. All printed values align with the stated P<.05 convention; the source lacks matched test statistics, paired/cross-group denominators, sidedness per test, and distributional inputs. `<.001` is not a display-zero notation. | PASS_2_COMPLETE |
| S015 | PH-test, imputation, and subgroup-summary claims contain no matched statistic, SE, interval, or numeric comparator. The named missing definitions are model details, event data, and numeric outputs; no contradiction is supplied. | PASS_2_COMPLETE |
| S016 | Planned Freedman/log-rank output remains arithmetically coherent: N1=160 plus N2=240 equals N=400, consistent with the stated 3:2 allocation. Alpha=.0500 two-sided is stated, but the software convention underlying the printed h ratio is not expanded; it is not treated as an observed-result comparator. | PASS_2_COMPLETE |
| S017 | Annual interim analyses after 200 entries and Peto P<.001 are clearly planned thresholds. C003 concerns differing accrual stopping wording, not an interim-test result; no actual interim timing or statistic is printed. | PASS_2_COMPLETE |
| S018 | Planned ITT Kaplan-Meier/Cox HR with 95% CI is compatible with the reported RFS/OS framework after retaining plan-versus-result distinction. C008 records a different protocol time-origin wording but no supplied matched estimate under a second origin. | PASS_2_COMPLETE |
| S019 | The protocol's Wilcoxon signed-rank plan matches the main article's named within-group 25(OH)D method. No matched statistic, paired analysis denominator, sidedness, or test definition permits exact comparison. | PASS_2_COMPLETE |
| S020 | Planned t, Mann-Whitney, and chi-square tests are conditional on type/distribution. No same-result baseline comparison with sufficient definitions is supplied; C001/C007 denominator observations do not identify a test-result contradiction. | PASS_2_COMPLETE |
| S021 | The protocol plans RR for relapse/safety while the article's competing-risk analysis uses a subdistribution HR. No same population/time/model result is printed under both measures; this is not a measure contradiction. | PASS_2_COMPLETE |
| S022 | The protocol supplies a two-sided P convention and P<.05 rule, supporting only threshold screening. It does not provide individual test, df, covariance, variance estimator, CI construction, or multiplicity mapping. | PASS_2_COMPLETE |
| S023 | The p. 23 high label `(40 ng/mL)` lacks an operator, while p. 31 gives `>40 ng/mL`; C005 already records this cross-location label inconsistency. Interaction/no-multiplicity descriptions otherwise match, and no boundary participant or different interaction estimate is supplied. | PASS_2_COMPLETE |
| S024 | Initial and final SAP fields are explicitly versioned and the change summary gives the pre-trial target decision. C003 is a distinct within-final-protocol accrual-threshold candidate, not a version-history statistical contradiction. | PASS_2_COMPLETE |
| S025 | The FokI log-rank P=.005 is an external background citation, not an observed trial analysis; no AMATERASU comparator exists. | PASS_2_COMPLETE |
| S026 | The external genetic-association P<.0001 is background only, with no trial population/model/comparator match. | PASS_2_COMPLETE |
| S027 | HR 0.62 is contained in 0.37-1.02; CI crosses 1 and P=.06. eTable 1 states outcome, reference <20, and unadjusted HR; no exact CI/test construction is supplied. | PASS_2_COMPLETE |
| S028 | AHR 0.61 is contained in 0.37-1.01; CI crosses 1 and P=.05. The vitamin-D-supplementation adjustment footnote distinguishes it from S027; no matched variance/CI construction supports exact P reconstruction. | PASS_2_COMPLETE |
| S029 | HR 0.66 is contained in 0.35-1.24; CI crosses 1 and P=.20. Outcome, reference, and unadjusted label are retained. | PASS_2_COMPLETE |
| S030 | AHR 0.64 is contained in 0.34-1.20; CI crosses 1 and P=.16. The stated adjusted label distinguishes it from S029. | PASS_2_COMPLETE |
| S031 | HR 0.47 is contained in 0.27-0.84; CI excludes 1 and P=.01. The unadjusted average-25(OH)D analysis is not the same exposure/time definition as the main baseline analysis. | PASS_2_COMPLETE |
| S032 | AHR 0.44 is contained in 0.24-0.82; CI excludes 1 and P=.009. Adjustment is explicitly distinct from S031. | PASS_2_COMPLETE |
| S033 | HR 0.39 is contained in 0.18-0.84; CI excludes 1 and P=.02. It exactly repeats S048 after matching outcome, stratum, and unadjusted model; intended repetition is not a duplicate-value contradiction. | PASS_2_COMPLETE |
| S034 | AHR 0.33 is contained in 0.15-0.74; CI excludes 1 and P=.007. The adjustment label is explicit. | PASS_2_COMPLETE |
| S035 | HR 0.29 is contained in 0.11-0.74; CI excludes 1 and P=.01. It exactly repeats S047 with the same outcome, stratum, and unadjusted model. | PASS_2_COMPLETE |
| S036 | AHR 0.26 is contained in 0.10-0.71; CI excludes 1 and P=.008. Its adjustment label is retained. | PASS_2_COMPLETE |
| S037 | HR 0.44 is contained in 0.17-1.16; CI crosses 1 and P=.10. The unadjusted model/reference label is explicit. | PASS_2_COMPLETE |
| S038 | AHR 0.34 is contained in 0.12-0.96; CI excludes 1 and P=.04. It is distinct from S037 by the stated adjustment. | PASS_2_COMPLETE |
| S039 | HR 0.44 is contained in 0.21-0.96; CI excludes 1 and P=.04. The unadjusted model/reference label is explicit. | PASS_2_COMPLETE |
| S040 | AHR 0.40 is contained in 0.18-0.92; CI excludes 1 and P=.03. The stated adjustment distinguishes it from S039. | PASS_2_COMPLETE |
| S041 | HR 0.55 is contained in 0.24-1.29; CI crosses 1 and P=.17. The unadjusted model/reference label is explicit. | PASS_2_COMPLETE |
| S042 | AHR 0.43 is contained in 0.17-1.08; CI crosses 1 and P=.07. The stated adjustment distinguishes it from S041. | PASS_2_COMPLETE |
| S043 | Multiple-imputation HR 1.15 is contained in 0.65-2.05; CI crosses 1 and P=.63. It agrees with main S004 at printed precision while retaining its multiple-imputation/baseline-stratum definition. | PASS_2_COMPLETE |
| S044 | Multiple-imputation HR 0.46 is contained in 0.24-0.86; CI excludes 1 and P=.02. It agrees with main S003 at printed precision after matching stratum/outcome. | PASS_2_COMPLETE |
| S045 | Multiple-imputation HR 1.36 is contained in 0.66-2.81; CI crosses 1 and P=.41. It agrees with main S007 at printed precision. | PASS_2_COMPLETE |
| S046 | Multiple-imputation HR 0.60 is contained in 0.28-1.30; CI crosses 1 and P=.20. It agrees with main S006 at printed precision. | PASS_2_COMPLETE |
| S047 | HR 0.29 is contained in 0.11-0.74; CI excludes 1 and P=.01, exactly repeating S035. The `~20` chart shorthand has no contrary boundary definition and is not treated as a separate stratum contradiction. | PASS_2_COMPLETE |
| S048 | HR 0.39 is contained in 0.18-0.84; CI excludes 1 and P=.02, exactly repeating S033. The `~20` shorthand is not an independently defined competing reference group. | PASS_2_COMPLETE |
| S049 | HR 0.65 is contained in 0.34-1.26; CI crosses 1 and P=.20; interaction P=.65 is separately printed. Figure-level model, adjustment, test, CI construction, and HR orientation are absent. | PASS_2_COMPLETE |
| S050 | HR 0.77 is contained in 0.42-1.43; CI crosses 1 and P=.41; interaction P=.90 is distinct. The missing figure-level inferential definitions preclude exact compatibility testing. | PASS_2_COMPLETE |
| S051 | HR 0.97 is contained in 0.32-2.88; CI crosses 1 and P=.95; interaction P=.67 is distinct. Required model/test/reference details are absent. | PASS_2_COMPLETE |
| S052 | HR 0.44 is contained in 0.03-7.16; CI crosses 1 and P=.56; interaction P=.66 is distinct. Required model/test/reference details are absent. | PASS_2_COMPLETE |
| S053 | HR 0.60 is contained in 0.24-1.48; CI crosses 1 and P=.27; interaction P=.50 is distinct. Required model/test/reference details are absent. | PASS_2_COMPLETE |
| S054 | HR 0.86 is contained in 0.52-1.41; CI crosses 1 and P=.55; interaction P=.38 is distinct. Required model/test/reference details are absent. | PASS_2_COMPLETE |
| S055 | HR 0.69 is contained in 0.34-1.38; CI crosses 1 and P=.29; interaction P=.64 is distinct. C006 already records that its panel label `CDK2` conflicts with matched Cdx2/CDX2 source labels; no second statistical mismatch is supplied. | PASS_2_COMPLETE |
| S056 | HR 0.72 is contained in 0.39-1.32; CI crosses 1 and P=.28; interaction P=.63 is distinct. C006 applies to the panel label only, with no different printed statistical value. | PASS_2_COMPLETE |
| S057 | HR 1.82 is contained in 0.48-6.88; CI crosses 1 and P=.38; interaction P=.19 is distinct. C006 applies to the panel label only. | PASS_2_COMPLETE |
| S058 | HR 1.00 is contained in 0.49-2.05; CI crosses 1 and P=.99; interaction P=.35 is distinct. Required model/test/reference definitions are absent. | PASS_2_COMPLETE |
| S059 | HR 0.70 is contained in 0.38-1.27; CI crosses 1 and P=.24; interaction P=.63 is distinct. Required model/test/reference definitions are absent. | PASS_2_COMPLETE |
| S060 | HR 0.53 is contained in 0.15-1.84; CI crosses 1 and P=.32; interaction P=.49 is distinct. Required model/test/reference definitions are absent. | PASS_2_COMPLETE |
| S061 | HR 0.87 is contained in 0.52-1.46; CI crosses 1 and P=.60; interaction P=.35 is distinct. Required model/test/reference definitions are absent. | PASS_2_COMPLETE |
| S062 | HR 0.49 is contained in 0.22-1.10; CI crosses 1 and P=.08; interaction P=.20 is distinct. Required model/test/reference definitions are absent. | PASS_2_COMPLETE |
| S063 | HR/CI are not estimable and print dashes; P=1.00 and interaction P=dash. Estimability, event pattern, model, test, and reference orientation are absent, so no point/interval or P/test compatibility is reconstructable. | PASS_2_COMPLETE |
| S064 | HR 0.71 is contained in 0.42-1.22; CI crosses 1 and P=.22; interaction P=.63 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S065 | HR 1.00 is contained in 0.44-2.24; CI crosses 1 and P=.99; interaction P=.49 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S066 | HR 0.65 is contained in 0.14-2.92; CI crosses 1 and P=.57; interaction P=.91 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S067 | HR 0.60 is contained in 0.34-1.05; CI crosses 1 and P=.07; interaction P=.16 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S068 | HR 1.19 is contained in 0.55-2.60; CI crosses 1 and P=.66; interaction P=.16 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S069 | HR 0.80 is contained in 0.20-3.20; CI crosses 1 and P=.75; interaction P=1.00 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S070 | HR 0.59 is contained in 0.37-0.97; CI excludes 1 and P=.04; interaction P=.13 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S071 | HR 1.18 is contained in 0.56-2.51; CI crosses 1 and P=.66; interaction P=.13 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S072 | HR 0.86 is contained in 0.44-1.68; CI crosses 1 and P=.65; interaction P=.48 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S073 | HR 0.63 is contained in 0.37-1.05; CI crosses 1 and P=.07; interaction P=.48 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S074 | HR 0.75 is contained in 0.49-1.16; CI crosses 1 and P=.20; interaction P=.87 is distinct. C007's BMI available-case denominator issue is an existing population/denominator candidate; the figure supplies no test/model details or second statistical result. | PASS_2_COMPLETE |
| S075 | HR 0.88 is contained in 0.22-3.55; CI crosses 1 and P=.86; interaction P=.87 is distinct. C007 applies to the complementary BMI subgroup population but does not supply a second HR for comparison. | PASS_2_COMPLETE |
| S076 | HR 1.01 is contained in 0.42-2.44; CI crosses 1 and P=.99; interaction P=.65 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S077 | HR 0.84 is contained in 0.40-1.76; CI crosses 1 and P=.64; interaction P=.88 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S078 | HR 0.69 is contained in 0.39-1.24; CI crosses 1 and P=.22; interaction P=.66 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S079 | HR 0.39 is contained in 0.14-1.13; CI crosses 1 and P=.08; interaction P=.14 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S080 | HR 1.20 is contained in 0.51-2.80; CI crosses 1 and P=.68; interaction P=.23 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S081 | HR 0.86 is contained in 0.51-1.46; CI crosses 1 and P=.58; interaction P=.62 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S082 | HR 0.70 is contained in 0.43-1.13; CI crosses 1 and P=.14; interaction P=.47 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |
| S083 | HR 1.18 is contained in 0.54-2.60; CI crosses 1 and P=.68; interaction P=.47 is distinct. Figure-level model/adjustment/test/CI/reference definitions are absent. | PASS_2_COMPLETE |

## C009 independent statistical assessment

C009 was assessed independently because it is an existing stable ledger candidate tied to S009-S012. Table 2's footnote says that HR values greater than 1 mean vitamin D is associated with a decreased probability of outcome. The same article reports lower vitamin-D cumulative relapse incidence in the middle stratum with subdistribution HR 0.44 and displays the total-population Figure 2C vitamin-D curve below placebo with subdistribution HR 0.75. Table 2 also prints total noncancer-death HR 0.70, while the direct-source event-count comparison is diagnostically lower for vitamin D (10/251) than placebo (9/166); cancer-specific-death HR 1.09 accompanies the diagnostically higher vitamin-D proportion (27/251) than placebo (16/166).

This direction comparison is source-grounded. The crude proportions are diagnostics, not substituted estimates for the time-to-event models. The source does not supply individual event/censoring times, model code, or an explicit per-row numerator/reference declaration that would reconstruct the HRs. A table-only reversed contrast would make the footnote coherent, but the plotted/narrative relapse direction supplies no stated support for that alternate contrast. This pass therefore identifies no new candidate: C009 already records the same footnote-versus-displayed-direction comparator and rule.

## Limitations and completion statement

- No sidedness, degrees of freedom, covariance, variance estimator, confidence-interval construction, multiplicity adjustment, denominator, model formula, or estimand mapping was inferred from convention alone.
- S014, S015, S017, S019-S022, S025-S026, and S063 are retained with their named unavailable definitions rather than being mechanically over-interpreted. S049-S083 lack figure-level model/test/CI/reference definitions needed for exact inferential identity testing.
- C001 and C007 identify available-case/analysis-set ambiguities, but no source supplies the absent denominator/missingness definition needed to map them into an additional statistical contradiction. C002-C006 and C008 similarly do not produce an unregistered distinct inferential inconsistency beyond the current ledger. C009 remains the sole existing footnote-direction implication for S009-S012.
- Every assigned relationship has an explicit `PASS_2_COMPLETE` record above. This artifact registers no new distinct lead and does not assign severity, validity, acceptance, rejection, correction, or any disposition.
