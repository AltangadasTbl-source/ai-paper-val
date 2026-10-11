# Statistical relationship inventory — support A, passes 1 and 2

Runtime ID: 01a12886-83ee-7ac0-afea-c841f69920e7; model gpt-6.1-sol; effort high; FRESH_SPAWN. Exact disjoint scope S001–S120: supplement eTable4p6, eTable5p7, eFigure1p8, eTable6p9, eTable7pp10/19. Exactly120relationships,104unique scalar estimate/95%CI tuples,16additional interaction/PH tests. Each record is PASS_1_COMPLETE. Pass 2 completed by distinct fresh runtime 01a12893-5344-7fb2-a4f4-e1a8e8ac9e7c; gpt-6.1-sol/high; FRESH_SPAWN. All original pass-1 values/proof are preserved. Candidate aliases STA-A-01 and STA-A-02 are discovery records only, pending coordinator stable registration and human adjudication.

## Source definitions and bounded inferential limits

- **A — rate difference:** REPORT supplement p6 eTable4 title, rate columns and footnote b specify nonsurgical minus surgical event rates per100patient-years at8years and95% bootstrap CIs from1000samples. Compare displayed subtraction, interval ordering/containment, positive direction and rate units. No P, bootstrap sample values or exact CI construction algorithm are printed on that page. Main p4 specifies percentile bootstrap for absolute *risk* differences; do not silently transfer that rule to rate differences. The parenthesized rates for five individual endpoints are death/outcome composite rates, not confidence endpoints.
- **B — cumulative incidence:** REPORT supplement p7 eTable5 specifies percent,95%CI, years2/5/8 and both treatments; REPORT main p4 defines Kaplan–Meier cumulative incidence. Check containment,0–100 bounds, monotonic point estimates and surgical/nonsurgical direction. The variance estimator/transform and unrounded values for each CI are not supplied; no P is printed in eTable5, so do not test an individual marginal interval against the overall Cox association P. All16year8 tuples repeat without value differences in REPORT main p7 Table2; trailing-zero precision is compatible.
- **C — subgroup HR:** REPORT supplement p8 eFigure1 specifies adjusted HR,95%CI, primary composite, surgery versus usual care, null1 and decreased/increased-risk arrows. Its footnote specifies replacing the original covariate by the dichotomous version and treatment interaction; age/eGFR use medians. All16graphic markers/bars agree with printed left-of-null direction. Rounded identical values for distinct subgroups are not an identity contradiction. No within-subgroup association P, SE, coefficient covariance or unrounded coefficients are printed.
- **D — interaction P:** REPORT supplement p8 explicitly identifies the eight P values as subgroup-variable × surgical-indicator interactions in the modified fully adjusted Cox model. REPORT main p4 states two-sided comparisons and no interaction heterogeneity. All eight P values exceed0.05. They are not the association P values for the sixteen within-subgroup HRs. Exact test statistic, df, contrast covariance, variance estimator and pooling rule for each interaction are not printed; do not infer an independent-subgroup z-test from the two marginal CIs.
- **E — overall Cox association:** REPORT supplement p9 eTable6 and REPORT main p7 Table2 print identical HR/95%CI/association-P triples. REPORT main p4 supplies fully adjusted Cox models, baseline covariates, five imputed datasets, Rubin SE, alpha0.05 and two-sided comparisons; PLAN protocol p6 corroborates model/SE definitions. Printed intervals all exclude1 downward and association P values are below0.05. Exact CI/test statistic construction, pooled df and covariance or variance details are not supplied. This permits direct qualitative consistency and repeated-value checks; it does not establish a unique numerical interval-to-P inversion. No asymptotic normal P reconstruction is used as evidence.
- **F — PH P:** REPORT supplement p9 footnote identifies a proportional-hazards-assumption test for each outcome; REPORT main p4 and PLAN protocol p6 identify Grambsch–Therneau weighted residuals for the treatment term. PH P is not the Cox treatment-association P or a test of HR=1. No weighted-residual statistic, df, transformation or exact pooling implementation is supplied. AF PH P0.04 is a reported diagnostic result; a departure from PH does not contradict the existence of an overall estimate or time-varying sensitivity estimate.
- **G — time-varying HR:** REPORT supplement pp10/19 eTable7 prints95%CI for adjusted surgery/nonsurgical HRs at years2/5/8. Footnote/prose specifies treatment interacted with a restricted cubic spline on observed follow-up time. REPORT main p4 similarly describes a time-spline treatment interaction; PLAN protocol p6 specifies these time points. All24tuples repeat exactly between pp10/19. The constant-HR model is a different model; do not require its numerical estimate to equal an individual time-varying estimate. No time-specific P, SE, spline coefficients/covariance, df, knots or full CI construction rule are supplied. AF8-year upper endpoint1.00 is a rounded endpoint, not proof of an exact-null bound.

Source roles are assigned by content: the article and results supplement are REPORT; prospective protocol is PLAN. Definitions supplied by PLAN only corroborate compatible REPORT methods and do not create a conflicting role relationship. Source authority is the unchanged PDFs; raw text and reused images are locators/transcription aids. Direct Poppler26.01.0 `pdftotext -layout -f 6 -l 10 joi190103supp1_prod.pdf -` and `-f 19 -l 19` confirmed scalar tables, units and both label observations. Reused p8 image was visually inspected for all16labels, values and bars; native text has no embedded scalar figure values. Reused p6/p19 images confirm page layout. No newly persisted derivative, OCR, Python extraction or web use.

Rules use printed precision; no unrounded estimate, estimand mapping, sidedness, covariance, variance estimator, multiplicity, denominator or df is inferred from convention. No assigned P value is displayed as zero; DISPLAY_ZERO_NOT_CANDIDATE is therefore NOT_APPLICABLE. No diagnostic tail-probability calculation is made.

## Complete relationship records

### S001 — Primary composite 8-year rate difference

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p6](../../../../joi190103supp1_prod.pdf#page=6) eTable4 Primary composite row; REPORT same-page title/header/footnote b
- **Printed inputs:** Surgical 4.51; nonsurgical 7.45; difference 2.94 (2.42, 3.48) per100patient-years;95%CI
- **Definition/missing inputs:** A; see the complete source definition above.
- **Checks and compared occurrences:** 7.45−4.51=2.94; 2.42≤2.94≤3.48; ordered CI above0; nonsurgical−surgical direction agrees. Shared title '(%)' conflicts with rate unit, distinct from coherent values. No matched risk-difference identity assumed.
- **Pass 1:** PASS_1_COMPLETE; Numeric checks: NO_CANDIDATE; shared label candidate STA-A-01
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed nonsurgical-minus-surgical subtraction, CI containment/order and positive direction remain coherent. Existing C012 (STA-A-01) retains the REPORT supplement p1/p6 title '(%)' versus p6 patient-time headers/footnote comparison; do not reinterpret rates as risks. C014's reference does not make eTable4 values time-varying HRs. Exact bootstrap CI algorithm, bootstrap replicates, unrounded rates and person-time totals are absent; no supplied association P for the rate difference.

### S002 — Secondary composite 8-year rate difference

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p6](../../../../joi190103supp1_prod.pdf#page=6) eTable4 Secondary composite row; REPORT same-page title/header/footnote b
- **Printed inputs:** Surgical 2.11; nonsurgical 3.64; difference 1.53 (1.18, 1.87) per100patient-years;95%CI
- **Definition/missing inputs:** A; see the complete source definition above.
- **Checks and compared occurrences:** 3.64−2.11=1.53; 1.18≤1.53≤1.87; ordered CI above0; nonsurgical−surgical direction agrees. Shared title '(%)' conflicts with rate unit, distinct from coherent values. No matched risk-difference identity assumed.
- **Pass 1:** PASS_1_COMPLETE; Numeric checks: NO_CANDIDATE; shared label candidate STA-A-01
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed nonsurgical-minus-surgical subtraction, CI containment/order and positive direction remain coherent. Existing C012 (STA-A-01) retains the REPORT supplement p1/p6 title '(%)' versus p6 patient-time headers/footnote comparison; do not reinterpret rates as risks. C014's reference does not make eTable4 values time-varying HRs. Exact bootstrap CI algorithm, bootstrap replicates, unrounded rates and person-time totals are absent; no supplied association P for the rate difference.

### S003 — All-cause mortality 8-year rate difference

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p6](../../../../joi190103supp1_prod.pdf#page=6) eTable4 All-cause mortality row; REPORT same-page title/header/footnote b
- **Printed inputs:** Surgical 1.19; nonsurgical 2.22; difference 1.03 (0.76, 1.29) per100patient-years;95%CI
- **Definition/missing inputs:** A; see the complete source definition above.
- **Checks and compared occurrences:** 2.22−1.19=1.03; 0.76≤1.03≤1.29; ordered CI above0; nonsurgical−surgical direction agrees. Shared title '(%)' conflicts with rate unit, distinct from coherent values. No matched risk-difference identity assumed.
- **Pass 1:** PASS_1_COMPLETE; Numeric checks: NO_CANDIDATE; shared label candidate STA-A-01
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed nonsurgical-minus-surgical subtraction, CI containment/order and positive direction remain coherent. Existing C012 (STA-A-01) retains the REPORT supplement p1/p6 title '(%)' versus p6 patient-time headers/footnote comparison; do not reinterpret rates as risks. C014's reference does not make eTable4 values time-varying HRs. Exact bootstrap CI algorithm, bootstrap replicates, unrounded rates and person-time totals are absent; no supplied association P for the rate difference.

### S004 — Heart failure 8-year rate difference

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p6](../../../../joi190103supp1_prod.pdf#page=6) eTable4 Heart failure row; REPORT same-page title/header/footnote b
- **Printed inputs:** Surgical 0.92; nonsurgical 2.49; difference 1.57 (1.32, 1.82) per100patient-years;95%CI
- **Definition/missing inputs:** A; see the complete source definition above.
- **Checks and compared occurrences:** 2.49−0.92=1.57; 1.32≤1.57≤1.82; ordered CI above0; nonsurgical−surgical direction agrees. Shared title '(%)' conflicts with rate unit, distinct from coherent values. No matched risk-difference identity assumed.
- **Pass 1:** PASS_1_COMPLETE; Numeric checks: NO_CANDIDATE; shared label candidate STA-A-01
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed nonsurgical-minus-surgical subtraction, CI containment/order and positive direction remain coherent. Existing C012 (STA-A-01) retains the REPORT supplement p1/p6 title '(%)' versus p6 patient-time headers/footnote comparison; do not reinterpret rates as risks. C014's reference does not make eTable4 values time-varying HRs. Exact bootstrap CI algorithm, bootstrap replicates, unrounded rates and person-time totals are absent; no supplied association P for the rate difference.

### S005 — Coronary artery disease 8-year rate difference

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p6](../../../../joi190103supp1_prod.pdf#page=6) eTable4 Coronary artery disease row; REPORT same-page title/header/footnote b
- **Printed inputs:** Surgical 1.03; nonsurgical 1.55; difference 0.52 (0.29, 0.77) per100patient-years;95%CI
- **Definition/missing inputs:** A; see the complete source definition above.
- **Checks and compared occurrences:** 1.55−1.03=0.52; 0.29≤0.52≤0.77; ordered CI above0; nonsurgical−surgical direction agrees. Shared title '(%)' conflicts with rate unit, distinct from coherent values. No matched risk-difference identity assumed.
- **Pass 1:** PASS_1_COMPLETE; Numeric checks: NO_CANDIDATE; shared label candidate STA-A-01
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed nonsurgical-minus-surgical subtraction, CI containment/order and positive direction remain coherent. Existing C012 (STA-A-01) retains the REPORT supplement p1/p6 title '(%)' versus p6 patient-time headers/footnote comparison; do not reinterpret rates as risks. C014's reference does not make eTable4 values time-varying HRs. Exact bootstrap CI algorithm, bootstrap replicates, unrounded rates and person-time totals are absent; no supplied association P for the rate difference.

### S006 — Cerebrovascular disease 8-year rate difference

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p6](../../../../joi190103supp1_prod.pdf#page=6) eTable4 Cerebrovascular disease row; REPORT same-page title/header/footnote b
- **Printed inputs:** Surgical 0.45; nonsurgical 0.73; difference 0.28 (0.12, 0.43) per100patient-years;95%CI
- **Definition/missing inputs:** A; see the complete source definition above.
- **Checks and compared occurrences:** 0.73−0.45=0.28; 0.12≤0.28≤0.43; ordered CI above0; nonsurgical−surgical direction agrees. Shared title '(%)' conflicts with rate unit, distinct from coherent values. No matched risk-difference identity assumed.
- **Pass 1:** PASS_1_COMPLETE; Numeric checks: NO_CANDIDATE; shared label candidate STA-A-01
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed nonsurgical-minus-surgical subtraction, CI containment/order and positive direction remain coherent. Existing C012 (STA-A-01) retains the REPORT supplement p1/p6 title '(%)' versus p6 patient-time headers/footnote comparison; do not reinterpret rates as risks. C014's reference does not make eTable4 values time-varying HRs. Exact bootstrap CI algorithm, bootstrap replicates, unrounded rates and person-time totals are absent; no supplied association P for the rate difference.

### S007 — Nephropathy 8-year rate difference

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p6](../../../../joi190103supp1_prod.pdf#page=6) eTable4 Nephropathy row; REPORT same-page title/header/footnote b
- **Printed inputs:** Surgical 0.89; nonsurgical 2.07; difference 1.18 (0.93, 1.42) per100patient-years;95%CI
- **Definition/missing inputs:** A; see the complete source definition above.
- **Checks and compared occurrences:** 2.07−0.89=1.18; 0.93≤1.18≤1.42; ordered CI above0; nonsurgical−surgical direction agrees. Shared title '(%)' conflicts with rate unit, distinct from coherent values. No matched risk-difference identity assumed.
- **Pass 1:** PASS_1_COMPLETE; Numeric checks: NO_CANDIDATE; shared label candidate STA-A-01
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed nonsurgical-minus-surgical subtraction, CI containment/order and positive direction remain coherent. Existing C012 (STA-A-01) retains the REPORT supplement p1/p6 title '(%)' versus p6 patient-time headers/footnote comparison; do not reinterpret rates as risks. C014's reference does not make eTable4 values time-varying HRs. Exact bootstrap CI algorithm, bootstrap replicates, unrounded rates and person-time totals are absent; no supplied association P for the rate difference.

### S008 — Atrial fibrillation 8-year rate difference

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p6](../../../../joi190103supp1_prod.pdf#page=6) eTable4 Atrial fibrillation row; REPORT same-page title/header/footnote b
- **Printed inputs:** Surgical 1.14; nonsurgical 1.77; difference 0.63 (0.36, 0.88) per100patient-years;95%CI
- **Definition/missing inputs:** A; see the complete source definition above.
- **Checks and compared occurrences:** 1.77−1.14=0.63; 0.36≤0.63≤0.88; ordered CI above0; nonsurgical−surgical direction agrees. Shared title '(%)' conflicts with rate unit, distinct from coherent values. No matched risk-difference identity assumed.
- **Pass 1:** PASS_1_COMPLETE; Numeric checks: NO_CANDIDATE; shared label candidate STA-A-01
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed nonsurgical-minus-surgical subtraction, CI containment/order and positive direction remain coherent. Existing C012 (STA-A-01) retains the REPORT supplement p1/p6 title '(%)' versus p6 patient-time headers/footnote comparison; do not reinterpret rates as risks. C014's reference does not make eTable4 values time-varying HRs. Exact bootstrap CI algorithm, bootstrap replicates, unrounded rates and person-time totals are absent; no supplied association P for the rate difference.

### S009 — Primary composite year2 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Primary composite row/2-year Surgical column
- **Printed inputs:** 7.6 (6.4, 8.8)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 6.4≤7.6≤8.8; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S010 — Primary composite year2 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Primary composite row/2-year Nonsurgical column
- **Printed inputs:** 12.2 (11.5, 12.8)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 11.5≤12.2≤12.8; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S011 — Primary composite year5 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Primary composite row/5-year Surgical column
- **Printed inputs:** 17.7 (15.6, 19.7)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 15.6≤17.7≤19.7; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S012 — Primary composite year5 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Primary composite row/5-year Nonsurgical column
- **Printed inputs:** 30.4 (29.4, 31.5)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 29.4≤30.4≤31.5; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S013 — Primary composite year8 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Primary composite row/8-year Surgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 30.8 (27.6, 34)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 27.6≤30.8≤34; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Year8 main Table2 repetition matches and 47.7−30.8=16.9 agrees with its ARD. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S014 — Primary composite year8 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Primary composite row/8-year Nonsurgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 47.7 (46.1, 49.2)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 46.1≤47.7≤49.2; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Year8 main Table2 repetition matches and 47.7−30.8=16.9 agrees with its ARD. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S015 — Secondary composite year2 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Secondary composite row/2-year Surgical column
- **Printed inputs:** 3.3 (2.5, 4.1)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 2.5≤3.3≤4.1; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S016 — Secondary composite year2 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Secondary composite row/2-year Nonsurgical column
- **Printed inputs:** 5.5 (5.1, 6.0)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 5.1≤5.5≤6.0; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S017 — Secondary composite year5 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Secondary composite row/5-year Surgical column
- **Printed inputs:** 8.8 (7.2, 10.4)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 7.2≤8.8≤10.4; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S018 — Secondary composite year5 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Secondary composite row/5-year Nonsurgical column
- **Printed inputs:** 15.5 (14.7, 16.4)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 14.7≤15.5≤16.4; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S019 — Secondary composite year8 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Secondary composite row/8-year Surgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 17 (14.3, 19.7)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 14.3≤17≤19.7; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Year8 main Table2 repetition matches and 27.6−17.0=10.6 agrees with its ARD. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S020 — Secondary composite year8 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Secondary composite row/8-year Nonsurgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 27.6 (26.2, 29.0)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 26.2≤27.6≤29.0; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Year8 main Table2 repetition matches and 27.6−17.0=10.6 agrees with its ARD. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S021 — All-cause mortality year2 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 All-cause mortality row/2-year Surgical column
- **Printed inputs:** 1.8 (1.2, 2.4)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 1.2≤1.8≤2.4; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S022 — All-cause mortality year2 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 All-cause mortality row/2-year Nonsurgical column
- **Printed inputs:** 3.2 (2.8, 3.5)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 2.8≤3.2≤3.5; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S023 — All-cause mortality year5 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 All-cause mortality row/5-year Surgical column
- **Printed inputs:** 4.9 (3.7, 6.1)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 3.7≤4.9≤6.1; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S024 — All-cause mortality year5 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 All-cause mortality row/5-year Nonsurgical column
- **Printed inputs:** 10.1 (9.4, 10.8)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 9.4≤10.1≤10.8; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S025 — All-cause mortality year8 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 All-cause mortality row/8-year Surgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 10 (7.8, 12.2)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 7.8≤10≤12.2; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Year8 main Table2 repetition matches and 17.8−10.0=7.8 agrees with its ARD. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S026 — All-cause mortality year8 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 All-cause mortality row/8-year Nonsurgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 17.8 (16.6, 19.0)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 16.6≤17.8≤19.0; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Year8 main Table2 repetition matches and 17.8−10.0=7.8 agrees with its ARD. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S027 — Heart failure year2 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Heart failure row/2-year Surgical column
- **Printed inputs:** 1.5 (1.0, 2.1)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 1.0≤1.5≤2.1; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S028 — Heart failure year2 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Heart failure row/2-year Nonsurgical column
- **Printed inputs:** 4.2 (3.8, 4.6)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 3.8≤4.2≤4.6; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S029 — Heart failure year5 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Heart failure row/5-year Surgical column
- **Printed inputs:** 3.8 (2.6, 4.9)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 2.6≤3.8≤4.9; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S030 — Heart failure year5 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Heart failure row/5-year Nonsurgical column
- **Printed inputs:** 10.4 (9.7, 11.2)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 9.7≤10.4≤11.2; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S031 — Heart failure year8 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Heart failure row/8-year Surgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 6.8 (4.9, 8.6)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 4.9≤6.8≤8.6; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Existing C001: 18.9−6.8=12.1 percentage points versus ARD12.9; gap0.8; the supplement risk tuple matches REPORT main p7 Table2. This corroborates the existing main-internal ARD subtraction comparison, without a new cross-document discrepancy. Gap exceeds combined nearest-tenth tolerance0.15; exact ARD point-estimation/risk-set rule remains missing. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S032 — Heart failure year8 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Heart failure row/8-year Nonsurgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 18.9 (17.6, 20.2)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 17.6≤18.9≤20.2; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Existing C001: 18.9−6.8=12.1 percentage points versus ARD12.9; gap0.8; the supplement risk tuple matches REPORT main p7 Table2. This corroborates the existing main-internal ARD subtraction comparison, without a new cross-document discrepancy. Gap exceeds combined nearest-tenth tolerance0.15; exact ARD point-estimation/risk-set rule remains missing. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S033 — Coronary artery disease year2 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Coronary artery disease row/2-year Surgical column
- **Printed inputs:** 1.7 (1.1, 2.3)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 1.1≤1.7≤2.3; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S034 — Coronary artery disease year2 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Coronary artery disease row/2-year Nonsurgical column
- **Printed inputs:** 2.9 (2.6, 3.3)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 2.6≤2.9≤3.3; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S035 — Coronary artery disease year5 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Coronary artery disease row/5-year Surgical column
- **Printed inputs:** 4.2 (3.1, 5.3)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 3.1≤4.2≤5.3; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S036 — Coronary artery disease year5 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Coronary artery disease row/5-year Nonsurgical column
- **Printed inputs:** 6.8 (6.2, 7.4)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 6.2≤6.8≤7.4; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S037 — Coronary artery disease year8 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Coronary artery disease row/8-year Surgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 7.9 (5.9, 9.8)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 5.9≤7.9≤9.8; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Existing C002: 11.6−7.9=3.7 versus ARD4.2; gap0.5; the supplement risk tuple matches REPORT main p7 Table2. This corroborates the existing main-internal ARD subtraction comparison, without a new cross-document discrepancy. Gap exceeds combined nearest-tenth tolerance0.15; exact ARD point-estimation/risk-set rule remains missing. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S038 — Coronary artery disease year8 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Coronary artery disease row/8-year Nonsurgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 11.6 (10.5, 12.6)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 10.5≤11.6≤12.6; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Existing C002: 11.6−7.9=3.7 versus ARD4.2; gap0.5; the supplement risk tuple matches REPORT main p7 Table2. This corroborates the existing main-internal ARD subtraction comparison, without a new cross-document discrepancy. Gap exceeds combined nearest-tenth tolerance0.15; exact ARD point-estimation/risk-set rule remains missing. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S039 — Cerebrovascular disease year2 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Cerebrovascular disease row/2-year Surgical column
- **Printed inputs:** 0.7 (0.3, 1.1)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 0.3≤0.7≤1.1; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S040 — Cerebrovascular disease year2 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Cerebrovascular disease row/2-year Nonsurgical column
- **Printed inputs:** 1.3 (1.1, 1.5)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 1.1≤1.3≤1.5; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S041 — Cerebrovascular disease year5 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Cerebrovascular disease row/5-year Surgical column
- **Printed inputs:** 2.2 (1.4, 3.0)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 1.4≤2.2≤3.0; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S042 — Cerebrovascular disease year5 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Cerebrovascular disease row/5-year Nonsurgical column
- **Printed inputs:** 3.1 (2.7, 3.5)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 2.7≤3.1≤3.5; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S043 — Cerebrovascular disease year8 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Cerebrovascular disease row/8-year Surgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 4.1 (2.7, 5.5)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 2.7≤4.1≤5.5; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Existing C003: 5.6−4.1=1.5 versus ARD1.8; gap0.3; the supplement risk tuple matches REPORT main p7 Table2. This corroborates the existing main-internal ARD subtraction comparison, without a new cross-document discrepancy. Gap exceeds combined nearest-tenth tolerance0.15; exact ARD point-estimation/risk-set rule remains missing. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S044 — Cerebrovascular disease year8 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Cerebrovascular disease row/8-year Nonsurgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 5.6 (4.9, 6.3)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 4.9≤5.6≤6.3; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Existing C003: 5.6−4.1=1.5 versus ARD1.8; gap0.3; the supplement risk tuple matches REPORT main p7 Table2. This corroborates the existing main-internal ARD subtraction comparison, without a new cross-document discrepancy. Gap exceeds combined nearest-tenth tolerance0.15; exact ARD point-estimation/risk-set rule remains missing. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S045 — Nephropathy year2 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Nephropathy row/2-year Surgical column
- **Printed inputs:** 1.4 (0.8, 2.0)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 0.8≤1.4≤2.0; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S046 — Nephropathy year2 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Nephropathy row/2-year Nonsurgical column
- **Printed inputs:** 2.3 (2.0, 2.7)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 2.0≤2.3≤2.7; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S047 — Nephropathy year5 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Nephropathy row/5-year Surgical column
- **Printed inputs:** 3.9 (2.8, 5.1)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 2.8≤3.9≤5.1; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S048 — Nephropathy year5 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Nephropathy row/5-year Nonsurgical column
- **Printed inputs:** 8.8 (8.0, 9.5)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 8.0≤8.8≤9.5; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S049 — Nephropathy year8 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Nephropathy row/8-year Surgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 6.1 (4.4, 7.8)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 4.4≤6.1≤7.8; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Existing C004: 16.3−6.1=10.2 versus ARD11.1; gap0.9; the supplement risk tuple matches REPORT main p7 Table2. This corroborates the existing main-internal ARD subtraction comparison, without a new cross-document discrepancy. Gap exceeds combined nearest-tenth tolerance0.15; exact ARD point-estimation/risk-set rule remains missing. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S050 — Nephropathy year8 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Nephropathy row/8-year Nonsurgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 16.3 (15.0, 17.6)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 15.0≤16.3≤17.6; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Existing C004: 16.3−6.1=10.2 versus ARD11.1; gap0.9; the supplement risk tuple matches REPORT main p7 Table2. This corroborates the existing main-internal ARD subtraction comparison, without a new cross-document discrepancy. Gap exceeds combined nearest-tenth tolerance0.15; exact ARD point-estimation/risk-set rule remains missing. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S051 — Atrial fibrillation year2 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Atrial fibrillation row/2-year Surgical column
- **Printed inputs:** 2.3 (1.6, 3.1)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 1.6≤2.3≤3.1; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S052 — Atrial fibrillation year2 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Atrial fibrillation row/2-year Nonsurgical column
- **Printed inputs:** 2.7 (2.4, 3.0)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 2.4≤2.7≤3.0; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S053 — Atrial fibrillation year5 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Atrial fibrillation row/5-year Surgical column
- **Printed inputs:** 4.8 (3.6, 6.0)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 3.6≤4.8≤6.0; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S054 — Atrial fibrillation year5 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Atrial fibrillation row/5-year Nonsurgical column
- **Printed inputs:** 7.6 (7.0, 8.2)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 7.0≤7.6≤8.2; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. No other exact printed same-time scalar repetition located in mapped sources. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. No exact same-time scalar contradiction is supplied elsewhere; the five existing eight-year ARD candidates do not redefine this year2/year5 estimate. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S055 — Atrial fibrillation year8 Surgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Atrial fibrillation row/8-year Surgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 7.9 (6.1, 9.7)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 6.1≤7.9≤9.7; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Existing C005: 13.6−7.9=5.7 versus ARD6.5; gap0.8; the supplement risk tuple matches REPORT main p7 Table2. This corroborates the existing main-internal ARD subtraction comparison, without a new cross-document discrepancy. Gap exceeds combined nearest-tenth tolerance0.15; exact ARD point-estimation/risk-set rule remains missing. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S056 — Atrial fibrillation year8 Nonsurgical cumulative incidence

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p7](../../../../joi190103supp1_prod.pdf#page=7) eTable5 Atrial fibrillation row/8-year Nonsurgical column; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 same endpoint/treatment/year tuple
- **Printed inputs:** 13.6 (12.5, 14.7)%;95%CI
- **Definition/missing inputs:** B; see the complete source definition above.
- **Checks and compared occurrences:** 12.5≤13.6≤14.7; interval ordered, contained in0–100%; cumulative point estimates increase across2/5/8years in this group; surgical estimate lower than matched nonsurgical estimate at this year. Main Table2 repetition matches after trailing-zero precision normalization. No individual incidence P is supplied.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. CI containment/order, 0–100% bounds, within-treatment time monotonicity and matched treatment direction remain coherent; no simple baseline-cohort proportion is substituted. Existing C005: 13.6−7.9=5.7 versus ARD6.5; gap0.8; the supplement risk tuple matches REPORT main p7 Table2. This corroborates the existing main-internal ARD subtraction comparison, without a new cross-document discrepancy. Gap exceeds combined nearest-tenth tolerance0.15; exact ARD point-estimation/risk-set rule remains missing. C011's medication analytic denominator is not an outcome risk-set denominator. Cox association P is not an ARD-bootstrap or marginal-risk P. CI variance/transform, unrounded risks and time-specific risk sets are absent; no individual marginal-risk P is supplied. Kaplan–Meier risks cannot be recalculated as event count divided by baseline N.

### S057 — Primary endpoint Gender Male subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Gender/Male printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.58 (0.49, 0.69);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.49≤0.58≤0.69<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated Gender interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S058 — Primary endpoint Gender Female subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Gender/Female printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.64 (0.56, 0.74);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.56≤0.64≤0.74<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated Gender interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S059 — Primary endpoint Age years <54 subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Age years/<54 printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.57 (0.47, 0.68);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.47≤0.57≤0.68<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated Age years interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S060 — Primary endpoint Age years ≥54 subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Age years/≥54 printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.57 (0.50, 0.66);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.50≤0.57≤0.66<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated Age years interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S061 — Primary endpoint BMI kg/m² <40 subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 BMI kg/m²/<40 printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.62 (0.49, 0.78);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.49≤0.62≤0.78<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated BMI kg/m² interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S062 — Primary endpoint BMI kg/m² ≥40 subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 BMI kg/m²/≥40 printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.61 (0.54, 0.69);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.54≤0.61≤0.69<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated BMI kg/m² interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S063 — Primary endpoint HbA1c % <7% subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 HbA1c %/<7% printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.62 (0.52, 0.74);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.52≤0.62≤0.74<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated HbA1c % interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S064 — Primary endpoint HbA1c % ≥7% subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 HbA1c %/≥7% printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.60 (0.52, 0.70);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.52≤0.60≤0.70<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated HbA1c % interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S065 — Primary endpoint eGFR ml/min <91 subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 eGFR ml/min/<91 printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.61 (0.54, 0.70);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.54≤0.61≤0.70<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated eGFR ml/min interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S066 — Primary endpoint eGFR ml/min ≥91 subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 eGFR ml/min/≥91 printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.62 (0.51, 0.75);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.51≤0.62≤0.75<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated eGFR ml/min interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S067 — Primary endpoint Insulin No subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Insulin/No printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.63 (0.55, 0.73);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.55≤0.63≤0.73<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated Insulin interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S068 — Primary endpoint Insulin Yes subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Insulin/Yes printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.59 (0.50, 0.70);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.50≤0.59≤0.70<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated Insulin interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S069 — Primary endpoint Sulfonylureas No subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Sulfonylureas/No printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.63 (0.55, 0.72);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.55≤0.63≤0.72<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated Sulfonylureas interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S070 — Primary endpoint Sulfonylureas Yes subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Sulfonylureas/Yes printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.60 (0.49, 0.74);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.49≤0.60≤0.74<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated Sulfonylureas interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S071 — Primary endpoint Lipid-lowering medications No subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Lipid-lowering medications/No printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.61 (0.52, 0.73);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.52≤0.61≤0.73<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated Lipid-lowering medications interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S072 — Primary endpoint Lipid-lowering medications Yes subgroup HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Lipid-lowering medications/Yes printed tuple and matched graphic bar/marker/axis arrows
- **Printed inputs:** 0.62 (0.53, 0.71);adjustedHR;95%CI
- **Definition/missing inputs:** C; see the complete source definition above.
- **Checks and compared occurrences:** 0.53≤0.62≤0.71<1; positive ordered ratio interval; printed and graphic decrease-risk direction agree. The associated Lipid-lowering medications interaction P is a different hypothesis, tracked separately.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Ordered positive HR CI contains the estimate below1; figure marker/bar and decreased-risk arrow agree. Subgroup labels/refit definitions remain coherent. Identical rounded HRs in distinct subgroups are permissible and do not establish a duplicated analysis. C015/C017 matching-ratio language supplies no subgroup denominator or effect contrast change; C018 supplies no demonstrated changed subgroup population. Within-subgroup P, unrounded model coefficients, SE/covariance and subgroup sample/risk-set counts are absent; the figure supplies interaction P separately.

### S073 — Gender treatment interaction P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Gender pair/interaction column and footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) primary-endpoint no-heterogeneity narrative
- **Printed inputs:** Interaction P=0.35; associated HRs 0.58 (0.49, 0.69) and 0.64 (0.56, 0.74)
- **Definition/missing inputs:** D; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.35≤1 and 0.35>0.05; compatible with printed no-interaction-heterogeneity narrative. All paired subgroup HRs below1 does not require interaction P<0.05. Marginal CIs do not supply interaction covariance/statistic.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Interaction P lies in[0,1] and exceeds0.05, consistent with the REPORT no-heterogeneity narrative. This P concerns treatment×subgroup heterogeneity, not either marginal subgroup association; no ratio difference or P reconstruction is inferred from rounded estimates/CI widths. Interaction statistic, df, coefficient covariance, variance estimator and pooling implementation are absent; marginal subgroup CIs do not define an independent-subgroup interaction test.

### S074 — Age years treatment interaction P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Age years pair/interaction column and footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) primary-endpoint no-heterogeneity narrative
- **Printed inputs:** Interaction P=0.93; associated HRs 0.57 (0.47, 0.68) and 0.57 (0.50, 0.66)
- **Definition/missing inputs:** D; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.93≤1 and 0.93>0.05; compatible with printed no-interaction-heterogeneity narrative. All paired subgroup HRs below1 does not require interaction P<0.05. Marginal CIs do not supply interaction covariance/statistic.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Interaction P lies in[0,1] and exceeds0.05, consistent with the REPORT no-heterogeneity narrative. This P concerns treatment×subgroup heterogeneity, not either marginal subgroup association; no ratio difference or P reconstruction is inferred from rounded estimates/CI widths. Interaction statistic, df, coefficient covariance, variance estimator and pooling implementation are absent; marginal subgroup CIs do not define an independent-subgroup interaction test.

### S075 — BMI kg/m² treatment interaction P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 BMI kg/m² pair/interaction column and footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) primary-endpoint no-heterogeneity narrative
- **Printed inputs:** Interaction P=0.90; associated HRs 0.62 (0.49, 0.78) and 0.61 (0.54, 0.69)
- **Definition/missing inputs:** D; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.90≤1 and 0.90>0.05; compatible with printed no-interaction-heterogeneity narrative. All paired subgroup HRs below1 does not require interaction P<0.05. Marginal CIs do not supply interaction covariance/statistic.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Interaction P lies in[0,1] and exceeds0.05, consistent with the REPORT no-heterogeneity narrative. This P concerns treatment×subgroup heterogeneity, not either marginal subgroup association; no ratio difference or P reconstruction is inferred from rounded estimates/CI widths. Interaction statistic, df, coefficient covariance, variance estimator and pooling implementation are absent; marginal subgroup CIs do not define an independent-subgroup interaction test.

### S076 — HbA1c % treatment interaction P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 HbA1c % pair/interaction column and footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) primary-endpoint no-heterogeneity narrative
- **Printed inputs:** Interaction P=0.80; associated HRs 0.62 (0.52, 0.74) and 0.60 (0.52, 0.70)
- **Definition/missing inputs:** D; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.80≤1 and 0.80>0.05; compatible with printed no-interaction-heterogeneity narrative. All paired subgroup HRs below1 does not require interaction P<0.05. Marginal CIs do not supply interaction covariance/statistic.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Interaction P lies in[0,1] and exceeds0.05, consistent with the REPORT no-heterogeneity narrative. This P concerns treatment×subgroup heterogeneity, not either marginal subgroup association; no ratio difference or P reconstruction is inferred from rounded estimates/CI widths. Interaction statistic, df, coefficient covariance, variance estimator and pooling implementation are absent; marginal subgroup CIs do not define an independent-subgroup interaction test.

### S077 — eGFR ml/min treatment interaction P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 eGFR ml/min pair/interaction column and footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) primary-endpoint no-heterogeneity narrative
- **Printed inputs:** Interaction P=0.94; associated HRs 0.61 (0.54, 0.70) and 0.62 (0.51, 0.75)
- **Definition/missing inputs:** D; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.94≤1 and 0.94>0.05; compatible with printed no-interaction-heterogeneity narrative. All paired subgroup HRs below1 does not require interaction P<0.05. Marginal CIs do not supply interaction covariance/statistic.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Interaction P lies in[0,1] and exceeds0.05, consistent with the REPORT no-heterogeneity narrative. This P concerns treatment×subgroup heterogeneity, not either marginal subgroup association; no ratio difference or P reconstruction is inferred from rounded estimates/CI widths. Interaction statistic, df, coefficient covariance, variance estimator and pooling implementation are absent; marginal subgroup CIs do not define an independent-subgroup interaction test.

### S078 — Insulin treatment interaction P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Insulin pair/interaction column and footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) primary-endpoint no-heterogeneity narrative
- **Printed inputs:** Interaction P=0.53; associated HRs 0.63 (0.55, 0.73) and 0.59 (0.50, 0.70)
- **Definition/missing inputs:** D; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.53≤1 and 0.53>0.05; compatible with printed no-interaction-heterogeneity narrative. All paired subgroup HRs below1 does not require interaction P<0.05. Marginal CIs do not supply interaction covariance/statistic.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Interaction P lies in[0,1] and exceeds0.05, consistent with the REPORT no-heterogeneity narrative. This P concerns treatment×subgroup heterogeneity, not either marginal subgroup association; no ratio difference or P reconstruction is inferred from rounded estimates/CI widths. Interaction statistic, df, coefficient covariance, variance estimator and pooling implementation are absent; marginal subgroup CIs do not define an independent-subgroup interaction test.

### S079 — Sulfonylureas treatment interaction P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Sulfonylureas pair/interaction column and footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) primary-endpoint no-heterogeneity narrative
- **Printed inputs:** Interaction P=0.72; associated HRs 0.63 (0.55, 0.72) and 0.60 (0.49, 0.74)
- **Definition/missing inputs:** D; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.72≤1 and 0.72>0.05; compatible with printed no-interaction-heterogeneity narrative. All paired subgroup HRs below1 does not require interaction P<0.05. Marginal CIs do not supply interaction covariance/statistic.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Interaction P lies in[0,1] and exceeds0.05, consistent with the REPORT no-heterogeneity narrative. This P concerns treatment×subgroup heterogeneity, not either marginal subgroup association; no ratio difference or P reconstruction is inferred from rounded estimates/CI widths. Interaction statistic, df, coefficient covariance, variance estimator and pooling implementation are absent; marginal subgroup CIs do not define an independent-subgroup interaction test.

### S080 — Lipid-lowering medications treatment interaction P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p8](../../../../joi190103supp1_prod.pdf#page=8) eFigure1 Lipid-lowering medications pair/interaction column and footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) primary-endpoint no-heterogeneity narrative
- **Printed inputs:** Interaction P=0.98; associated HRs 0.61 (0.52, 0.73) and 0.62 (0.53, 0.71)
- **Definition/missing inputs:** D; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.98≤1 and 0.98>0.05; compatible with printed no-interaction-heterogeneity narrative. All paired subgroup HRs below1 does not require interaction P<0.05. Marginal CIs do not supply interaction covariance/statistic.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Interaction P lies in[0,1] and exceeds0.05, consistent with the REPORT no-heterogeneity narrative. This P concerns treatment×subgroup heterogeneity, not either marginal subgroup association; no ratio difference or P reconstruction is inferred from rounded estimates/CI widths. Interaction statistic, df, coefficient covariance, variance estimator and pooling implementation are absent; marginal subgroup CIs do not define an independent-subgroup interaction test.

### S081 — Primary composite overall Cox HR/association P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Primary composite HR/association-P columns; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 corresponding row; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) model definitions; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) corroborating methods
- **Printed inputs:** 0.61 (0.55, 0.69);95%CI;associationP=<0.001; PH P=0.89 belongs to separate diagnostic
- **Definition/missing inputs:** E; see the complete source definition above.
- **Checks and compared occurrences:** 0.55≤0.61≤0.69<1; ordered positive HR interval and below-null direction; associationP <0.001 below0.05 is qualitatively compatible. Main Table2 triple is identical. Exact CI↔P reconstruction is not established by printed model information; PH P is not its comparator.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Positive ordered HR CI contains the estimate and excludes1 downward; association P below0.05 agrees qualitatively. REPORT supplement p9 and REPORT main p7 HR/CI/P repetitions match after display precision. PH P belongs to a different test. C001–C005 concern ARD point subtraction and cannot be tested using this adjusted Cox P. C013's five-versus-six primary component label is an existing contextual result-identity observation; the HR0.61/CI0.55–0.69 repeat correctly. Exact pooled CI/test construction, df and full covariance/variance details are absent; two-sided Cox/Rubin definitions permit qualitative checks but not a unique numerical CI-to-P inversion.

### S082 — Secondary composite overall Cox HR/association P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Secondary composite HR/association-P columns; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 corresponding row; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) model definitions; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) corroborating methods
- **Printed inputs:** 0.62 (0.53, 0.72);95%CI;associationP=<0.001; PH P=0.76 belongs to separate diagnostic
- **Definition/missing inputs:** E; see the complete source definition above.
- **Checks and compared occurrences:** 0.53≤0.62≤0.72<1; ordered positive HR interval and below-null direction; associationP <0.001 below0.05 is qualitatively compatible. Main Table2 triple is identical. Exact CI↔P reconstruction is not established by printed model information; PH P is not its comparator.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Positive ordered HR CI contains the estimate and excludes1 downward; association P below0.05 agrees qualitatively. REPORT supplement p9 and REPORT main p7 HR/CI/P repetitions match after display precision. PH P belongs to a different test. C001–C005 concern ARD point subtraction and cannot be tested using this adjusted Cox P. Exact pooled CI/test construction, df and full covariance/variance details are absent; two-sided Cox/Rubin definitions permit qualitative checks but not a unique numerical CI-to-P inversion.

### S083 — All-cause mortality overall Cox HR/association P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 All-cause mortality HR/association-P columns; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 corresponding row; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) model definitions; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) corroborating methods
- **Printed inputs:** 0.59 (0.48, 0.72);95%CI;associationP=<0.001; PH P=0.63 belongs to separate diagnostic
- **Definition/missing inputs:** E; see the complete source definition above.
- **Checks and compared occurrences:** 0.48≤0.59≤0.72<1; ordered positive HR interval and below-null direction; associationP <0.001 below0.05 is qualitatively compatible. Main Table2 triple is identical. Exact CI↔P reconstruction is not established by printed model information; PH P is not its comparator.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Positive ordered HR CI contains the estimate and excludes1 downward; association P below0.05 agrees qualitatively. REPORT supplement p9 and REPORT main p7 HR/CI/P repetitions match after display precision. PH P belongs to a different test. C001–C005 concern ARD point subtraction and cannot be tested using this adjusted Cox P. Exact pooled CI/test construction, df and full covariance/variance details are absent; two-sided Cox/Rubin definitions permit qualitative checks but not a unique numerical CI-to-P inversion.

### S084 — Heart failure overall Cox HR/association P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Heart failure HR/association-P columns; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 corresponding row; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) model definitions; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) corroborating methods
- **Printed inputs:** 0.38 (0.30, 0.49);95%CI;associationP=<0.001; PH P=0.65 belongs to separate diagnostic
- **Definition/missing inputs:** E; see the complete source definition above.
- **Checks and compared occurrences:** 0.30≤0.38≤0.49<1; ordered positive HR interval and below-null direction; associationP <0.001 below0.05 is qualitatively compatible. Main Table2 triple is identical. Exact CI↔P reconstruction is not established by printed model information; PH P is not its comparator.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Positive ordered HR CI contains the estimate and excludes1 downward; association P below0.05 agrees qualitatively. REPORT supplement p9 and REPORT main p7 HR/CI/P repetitions match after display precision. PH P belongs to a different test. C001–C005 concern ARD point subtraction and cannot be tested using this adjusted Cox P. Exact pooled CI/test construction, df and full covariance/variance details are absent; two-sided Cox/Rubin definitions permit qualitative checks but not a unique numerical CI-to-P inversion.

### S085 — Coronary artery disease overall Cox HR/association P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Coronary artery disease HR/association-P columns; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 corresponding row; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) model definitions; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) corroborating methods
- **Printed inputs:** 0.69 (0.54, 0.87);95%CI;associationP=0.002; PH P=0.24 belongs to separate diagnostic
- **Definition/missing inputs:** E; see the complete source definition above.
- **Checks and compared occurrences:** 0.54≤0.69≤0.87<1; ordered positive HR interval and below-null direction; associationP 0.002 below0.05 is qualitatively compatible. Main Table2 triple is identical. Exact CI↔P reconstruction is not established by printed model information; PH P is not its comparator.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Positive ordered HR CI contains the estimate and excludes1 downward; association P below0.05 agrees qualitatively. REPORT supplement p9 and REPORT main p7 HR/CI/P repetitions match after display precision. PH P belongs to a different test. C001–C005 concern ARD point subtraction and cannot be tested using this adjusted Cox P. Exact pooled CI/test construction, df and full covariance/variance details are absent; two-sided Cox/Rubin definitions permit qualitative checks but not a unique numerical CI-to-P inversion.

### S086 — Cerebrovascular disease overall Cox HR/association P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Cerebrovascular disease HR/association-P columns; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 corresponding row; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) model definitions; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) corroborating methods
- **Printed inputs:** 0.67 (0.48, 0.94);95%CI;associationP=0.02; PH P=0.10 belongs to separate diagnostic
- **Definition/missing inputs:** E; see the complete source definition above.
- **Checks and compared occurrences:** 0.48≤0.67≤0.94<1; ordered positive HR interval and below-null direction; associationP 0.02 below0.05 is qualitatively compatible. Main Table2 triple is identical. Exact CI↔P reconstruction is not established by printed model information; PH P is not its comparator.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Positive ordered HR CI contains the estimate and excludes1 downward; association P below0.05 agrees qualitatively. REPORT supplement p9 and REPORT main p7 HR/CI/P repetitions match after display precision. PH P belongs to a different test. C001–C005 concern ARD point subtraction and cannot be tested using this adjusted Cox P. Exact pooled CI/test construction, df and full covariance/variance details are absent; two-sided Cox/Rubin definitions permit qualitative checks but not a unique numerical CI-to-P inversion.

### S087 — Nephropathy overall Cox HR/association P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Nephropathy HR/association-P columns; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 corresponding row; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) model definitions; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) corroborating methods
- **Printed inputs:** 0.40 (0.31, 0.52);95%CI;associationP=<0.001; PH P=0.46 belongs to separate diagnostic
- **Definition/missing inputs:** E; see the complete source definition above.
- **Checks and compared occurrences:** 0.31≤0.40≤0.52<1; ordered positive HR interval and below-null direction; associationP <0.001 below0.05 is qualitatively compatible. Main Table2 triple is identical. Exact CI↔P reconstruction is not established by printed model information; PH P is not its comparator.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Positive ordered HR CI contains the estimate and excludes1 downward; association P below0.05 agrees qualitatively. REPORT supplement p9 and REPORT main p7 HR/CI/P repetitions match after display precision. PH P belongs to a different test. C001–C005 concern ARD point subtraction and cannot be tested using this adjusted Cox P. Exact pooled CI/test construction, df and full covariance/variance details are absent; two-sided Cox/Rubin definitions permit qualitative checks but not a unique numerical CI-to-P inversion.

### S088 — Atrial fibrillation overall Cox HR/association P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Atrial fibrillation HR/association-P columns; REPORT [main article physical p7](../../../../jama_aminian_2019_oi_190103.pdf#page=7) Table2 corresponding row; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) model definitions; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) corroborating methods
- **Printed inputs:** 0.78 (0.62, 0.97);95%CI;associationP=0.03; PH P=0.04 belongs to separate diagnostic
- **Definition/missing inputs:** E; see the complete source definition above.
- **Checks and compared occurrences:** 0.62≤0.78≤0.97<1; ordered positive HR interval and below-null direction; associationP 0.03 below0.05 is qualitatively compatible. Main Table2 triple is identical. Exact CI↔P reconstruction is not established by printed model information; PH P is not its comparator.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; exact numerical reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Positive ordered HR CI contains the estimate and excludes1 downward; association P below0.05 agrees qualitatively. REPORT supplement p9 and REPORT main p7 HR/CI/P repetitions match after display precision. PH P belongs to a different test. C001–C005 concern ARD point subtraction and cannot be tested using this adjusted Cox P. Exact pooled CI/test construction, df and full covariance/variance details are absent; two-sided Cox/Rubin definitions permit qualitative checks but not a unique numerical CI-to-P inversion.

### S089 — Primary composite PH diagnostic P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Primary composite PH-P column/footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) weighted-residual definition; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) same diagnostic definition
- **Printed inputs:** PH P=0.89; separate associationP=<0.001
- **Definition/missing inputs:** F; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.89≤1; footnote identifies PH assumption test rather than HR=1 association test. No association-P/PH-P equivalence asserted. Exact weighted-residual statistic cannot be reconstructed.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; test reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed diagnostic P lies in[0,1]; source identifies the treatment-term PH assumption test. It is neither the association P nor an interval bound and does not share an HR=1 inference rule. No ledger/recheck fact establishes a contradictory PH statement for this outcome. Weighted-residual statistic, df, transform and exact pooling implementation are absent; PH diagnostic P tests a different hypothesis from HR=1.

### S090 — Secondary composite PH diagnostic P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Secondary composite PH-P column/footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) weighted-residual definition; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) same diagnostic definition
- **Printed inputs:** PH P=0.76; separate associationP=<0.001
- **Definition/missing inputs:** F; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.76≤1; footnote identifies PH assumption test rather than HR=1 association test. No association-P/PH-P equivalence asserted. Exact weighted-residual statistic cannot be reconstructed.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; test reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed diagnostic P lies in[0,1]; source identifies the treatment-term PH assumption test. It is neither the association P nor an interval bound and does not share an HR=1 inference rule. No ledger/recheck fact establishes a contradictory PH statement for this outcome. Weighted-residual statistic, df, transform and exact pooling implementation are absent; PH diagnostic P tests a different hypothesis from HR=1.

### S091 — All-cause mortality PH diagnostic P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 All-cause mortality PH-P column/footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) weighted-residual definition; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) same diagnostic definition
- **Printed inputs:** PH P=0.63; separate associationP=<0.001
- **Definition/missing inputs:** F; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.63≤1; footnote identifies PH assumption test rather than HR=1 association test. No association-P/PH-P equivalence asserted. Exact weighted-residual statistic cannot be reconstructed.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; test reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed diagnostic P lies in[0,1]; source identifies the treatment-term PH assumption test. It is neither the association P nor an interval bound and does not share an HR=1 inference rule. No ledger/recheck fact establishes a contradictory PH statement for this outcome. Weighted-residual statistic, df, transform and exact pooling implementation are absent; PH diagnostic P tests a different hypothesis from HR=1.

### S092 — Heart failure PH diagnostic P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Heart failure PH-P column/footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) weighted-residual definition; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) same diagnostic definition
- **Printed inputs:** PH P=0.65; separate associationP=<0.001
- **Definition/missing inputs:** F; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.65≤1; footnote identifies PH assumption test rather than HR=1 association test. No association-P/PH-P equivalence asserted. Exact weighted-residual statistic cannot be reconstructed.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; test reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed diagnostic P lies in[0,1]; source identifies the treatment-term PH assumption test. It is neither the association P nor an interval bound and does not share an HR=1 inference rule. No ledger/recheck fact establishes a contradictory PH statement for this outcome. Weighted-residual statistic, df, transform and exact pooling implementation are absent; PH diagnostic P tests a different hypothesis from HR=1.

### S093 — Coronary artery disease PH diagnostic P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Coronary artery disease PH-P column/footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) weighted-residual definition; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) same diagnostic definition
- **Printed inputs:** PH P=0.24; separate associationP=0.002
- **Definition/missing inputs:** F; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.24≤1; footnote identifies PH assumption test rather than HR=1 association test. No association-P/PH-P equivalence asserted. Exact weighted-residual statistic cannot be reconstructed.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; test reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed diagnostic P lies in[0,1]; source identifies the treatment-term PH assumption test. It is neither the association P nor an interval bound and does not share an HR=1 inference rule. No ledger/recheck fact establishes a contradictory PH statement for this outcome. Weighted-residual statistic, df, transform and exact pooling implementation are absent; PH diagnostic P tests a different hypothesis from HR=1.

### S094 — Cerebrovascular disease PH diagnostic P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Cerebrovascular disease PH-P column/footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) weighted-residual definition; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) same diagnostic definition
- **Printed inputs:** PH P=0.10; separate associationP=0.02
- **Definition/missing inputs:** F; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.10≤1; footnote identifies PH assumption test rather than HR=1 association test. No association-P/PH-P equivalence asserted. Exact weighted-residual statistic cannot be reconstructed.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; test reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed diagnostic P lies in[0,1]; source identifies the treatment-term PH assumption test. It is neither the association P nor an interval bound and does not share an HR=1 inference rule. No ledger/recheck fact establishes a contradictory PH statement for this outcome. Weighted-residual statistic, df, transform and exact pooling implementation are absent; PH diagnostic P tests a different hypothesis from HR=1.

### S095 — Nephropathy PH diagnostic P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Nephropathy PH-P column/footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) weighted-residual definition; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) same diagnostic definition
- **Printed inputs:** PH P=0.46; separate associationP=<0.001
- **Definition/missing inputs:** F; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.46≤1; footnote identifies PH assumption test rather than HR=1 association test. No association-P/PH-P equivalence asserted. Exact weighted-residual statistic cannot be reconstructed.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; test reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed diagnostic P lies in[0,1]; source identifies the treatment-term PH assumption test. It is neither the association P nor an interval bound and does not share an HR=1 inference rule. No ledger/recheck fact establishes a contradictory PH statement for this outcome. Weighted-residual statistic, df, transform and exact pooling implementation are absent; PH diagnostic P tests a different hypothesis from HR=1.

### S096 — Atrial fibrillation PH diagnostic P

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p9](../../../../joi190103supp1_prod.pdf#page=9) eTable6 Atrial fibrillation PH-P column/footnote; REPORT [main article physical p4](../../../../jama_aminian_2019_oi_190103.pdf#page=4) weighted-residual definition; PLAN [protocol physical p6](../../../../joi190103supp2_prod.pdf#page=6) same diagnostic definition
- **Printed inputs:** PH P=0.04; separate associationP=0.03
- **Definition/missing inputs:** F; see the complete source definition above.
- **Checks and compared occurrences:** 0≤0.04≤1; footnote identifies PH assumption test rather than HR=1 association test. AF0.04 is below0.05; the supplied report presents a time-varying sensitivity model rather than claiming all PH diagnostics exceeded0.05. Exact weighted-residual statistic cannot be reconstructed.
- **Pass 1:** PASS_1_COMPLETE; NO_CANDIDATE; test reconstruction MISSING_INPUT
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Printed diagnostic P lies in[0,1]; source identifies the treatment-term PH assumption test. It is neither the association P nor an interval bound and does not share an HR=1 inference rule. AF PH P0.04 below0.05 is explicitly printed; the supplied time-varying sensitivity analysis does not assert that every PH test exceeded0.05. Weighted-residual statistic, df, transform and exact pooling implementation are absent; PH diagnostic P tests a different hypothesis from HR=1.

### S097 — Primary composite year2 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Primary composite/2-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.57 (0.49, 0.65);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.49≤0.57≤0.65; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S098 — Primary composite year5 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Primary composite/5-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.78 (0.66, 0.93);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.66≤0.78≤0.93; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S099 — Primary composite year8 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Primary composite/8-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.79 (0.64, 0.97);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.64≤0.79≤0.97; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S100 — Secondary composite year2 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Secondary composite/2-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.51 (0.42, 0.63);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.42≤0.51≤0.63; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S101 — Secondary composite year5 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Secondary composite/5-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.82 (0.65, 1.04);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.65≤0.82≤1.04; ordered positive HR interval; printed CI spans1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. A CI spanning1 does not contradict the different constant-model association P. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S102 — Secondary composite year8 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Secondary composite/8-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.73 (0.56, 0.95);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.56≤0.73≤0.95; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S103 — All-cause mortality year2 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 All-cause mortality/2-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.43 (0.33, 0.57);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.33≤0.43≤0.57; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S104 — All-cause mortality year5 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 All-cause mortality/5-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.69 (0.50, 0.95);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.50≤0.69≤0.95; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S105 — All-cause mortality year8 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 All-cause mortality/8-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.80 (0.56, 1.15);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.56≤0.80≤1.15; ordered positive HR interval; printed CI spans1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. A CI spanning1 does not contradict the different constant-model association P. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S106 — Heart failure year2 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Heart failure/2-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.31 (0.23, 0.41);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.23≤0.31≤0.41; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S107 — Heart failure year5 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Heart failure/5-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.40 (0.31, 0.53);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.31≤0.40≤0.53; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S108 — Heart failure year8 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Heart failure/8-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.52 (0.35, 0.79);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.35≤0.52≤0.79; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S109 — Coronary artery disease year2 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Coronary artery disease/2-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.52 (0.38, 0.69);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.38≤0.52≤0.69; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S110 — Coronary artery disease year5 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Coronary artery disease/5-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 1.03 (0.71, 1.51);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.71≤1.03≤1.51; ordered positive HR interval; printed CI spans1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. This point above1 has a CI spanning1 and represents an instantaneous adjusted time-specific HR; it need not follow the direction of a cumulative-risk difference or constant HR. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S111 — Coronary artery disease year8 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Coronary artery disease/8-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.99 (0.64, 1.51);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.64≤0.99≤1.51; ordered positive HR interval; printed CI spans1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. A CI spanning1 does not contradict the different constant-model association P. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S112 — Cerebrovascular disease year2 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Cerebrovascular disease/2-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.68 (0.45, 1.04);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.45≤0.68≤1.04; ordered positive HR interval; printed CI spans1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. A CI spanning1 does not contradict the different constant-model association P. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S113 — Cerebrovascular disease year5 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Cerebrovascular disease/5-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 1.29 (0.77, 2.15);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.77≤1.29≤2.15; ordered positive HR interval; printed CI spans1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. This point above1 has a CI spanning1 and represents an instantaneous adjusted time-specific HR; it need not follow the direction of a cumulative-risk difference or constant HR. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S114 — Cerebrovascular disease year8 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Cerebrovascular disease/8-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.60 (0.28, 1.25);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.28≤0.60≤1.25; ordered positive HR interval; printed CI spans1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. A CI spanning1 does not contradict the different constant-model association P. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S115 — Nephropathy year2 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Nephropathy/2-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.41 (0.30, 0.58);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.30≤0.41≤0.58; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S116 — Nephropathy year5 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Nephropathy/5-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.40 (0.26, 0.61);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.26≤0.40≤0.61; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S117 — Nephropathy year8 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Nephropathy/8-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.46 (0.30, 0.70);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.30≤0.46≤0.70; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S118 — Atrial fibrillation year2 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Atrial fibrillation/2-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.68 (0.52, 0.89);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.52≤0.68≤0.89; ordered positive HR interval; printed CI below1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S119 — Atrial fibrillation year5 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Atrial fibrillation/5-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.88 (0.62, 1.25);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.62≤0.88≤1.25; ordered positive HR interval; printed CI spans1. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. A CI spanning1 does not contradict the different constant-model association P. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

### S120 — Atrial fibrillation year8 time-varying HR

- **Source locations and roles:** REPORT [joi190103supp1_prod.pdf physical p10](../../../../joi190103supp1_prod.pdf#page=10) eTable7 Atrial fibrillation/8-year cell and footnote; REPORT [joi190103supp1_prod.pdf physical p19](../../../../joi190103supp1_prod.pdf#page=19) duplicate eTable7 corresponding cell and time-varying prose
- **Printed inputs:** 0.65 (0.42, 1.00);95%CI;adjusted time-varyingHR
- **Definition/missing inputs:** G; see the complete source definition above.
- **Checks and compared occurrences:** 0.42≤0.65≤1.00; ordered positive HR interval; printed upper endpoint equals1.00 at displayed precision. The p10/p19 printed tuple is identical. Time-specific direction is read without replacing it by constant-HR significance. p19 prose names eTable4, whereas displayed repeated table is eTable7; shared identity-label candidate STA-A-02.
- **Pass 1:** PASS_1_COMPLETE; Tuple/repetition checks: NO_CANDIDATE; shared reference candidate STA-A-02
- **Pass 2:** PASS_2_COMPLETE; NO_NEW_CANDIDATE. Time-varying HR CI is positive, ordered and contains its point; REPORT supplement pp10/19 tuples match exactly. Existing C014 (STA-A-02) retains REPORT p19 'eTable4' reference versus actual p6 rates/eTable7 pp10/19; scalar repetition remains coherent. Upper endpoint1.00 is rounded and supplies no exact significance claim. Time-specific P, SE, spline coefficients/covariance, df, knots and full CI rule are absent; time-varying HR is a different estimand/model from constant HR or cumulative risk.

## Shard completion

Assigned IDs: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120.

PASS_1_COMPLETE count120. Scalar estimate/interval tuples104; separate interaction tests8; PH diagnostics8. Candidate aliases2(STA-A-01,STA-A-02). Scalar ordering/containment or matched repeated-value contradictions0. No assigned P display zero. Supplied-definition limitations A–G; no scientific coverage gap. PASS_2_COMPLETE count120 under runtime 01a12893-5344-7fb2-a4f4-e1a8e8ac9e7c. New candidate aliases0; existing C012/C014 retained without duplication; existing C001–C005 corroborated by repeated eight-year risks. Complete18-ID ledger/recheck implications are documented in ../../checkers/parts/statistical_pass_2_support_a.md.

