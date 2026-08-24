# Statistical consistency pass 2

## Scope, independence, and rules

This independent second pass reviewed every canonical inferential relationship, `S001` through `S067`, against the current source-first relationship mappings and the supplied PDFs. It also reconciled the complete stable candidate ledger (`C001` through `C011`), the pass-1 statistical checker, the numeric-consistency checker, the cross-source checker, and the mechanical evidence recheck. No legacy audit derivative or web source was used.

For each relationship, the pass revisited printed denominators and arithmetic where they bear on the result; point-estimate containment; endpoint ordering; sign/direction; measure, scale, and model labels; repeated values; matching cross-document results; and recheck implications. Interval-to-P or test-statistic reconstruction was used only as a labelled diagnostic where the direct source supplies a compatible two-sided, same-result 95% CI/P framing. The package does not specify a shared estimator, variance method, degrees of freedom, covariance structure, or exact CI/test inversion for the adjusted absolute differences, so no such approximation is used as a decision rule.

`NO_NEW_CANDIDATE` means this second-pass review found no additional distinct candidate for that relationship. It is not an adjudication of any existing stable ID. No mapped result uses `P = 0`, `p = 0.000`, or an equivalent display zero; none was treated as a candidate.

## Reconciliation of stable-ledger and recheck implications

| Stable ID | Pass-2 reconciliation relevant to statistical relationships | Affected S IDs | Result |
|---|---|---|---|
| C001 | Direct recheck confirms `311 (13.05)` with a printed intervention total of 2400. This baseline arithmetic observation has no distinct inferential-result comparator. | S033 (baseline comparison context) | PASS_2_COMPLETE; no new statistical candidate. |
| C002 | Direct sources retain `LDL >100` in the article and `LDL >=100` in the protocol/eTable. The threshold/eligibility label remains distinct from the supplied odds-ratio and absolute-difference calculations. | S018, S064 | PASS_2_COMPLETE; existing label candidate creates no additional statistical candidate. |
| C003 | The `20 patients per cluster` and 801-baseline-patient comparison does not define a different estimate, interval, or P value for a canonical S result. | S001, S028, S033 | PASS_2_COMPLETE; no new statistical candidate. |
| C004 | Direct PDF recheck shows `23/238 (9.66)`, not `9.6`; `23/238 x 100 = 9.6639...`, which rounds to `9.66` at the visibly used two-decimal precision. The paired `46/254 (18.11)` also reconciles. | S058 | PASS_2_COMPLETE; this recheck fact yields no new candidate and does not alter the retained C004 ID. |
| C005 | `2141/2400 (89.3)` remains a printed arithmetic issue. Its sensitivity-analysis difference/ORPA have separately labeled intervals and P values whose direction and null decisions are coherent at displayed precision. | S062 | PASS_2_COMPLETE; no added statistical candidate. |
| C006 | `39/174 (22.5)` remains a printed arithmetic issue. Its sensitivity-analysis effect displays have internally ordered intervals and direction-consistent labels. | S063 | PASS_2_COMPLETE; no added statistical candidate. |
| C007 | `1439/1586 (90.8)` remains a printed arithmetic issue; C002 separately preserves the LDL-boundary comparator. Neither supplies a conflict between the displayed sensitivity effect, interval, or P value. | S064 | PASS_2_COMPLETE; no added statistical candidate. |
| C008 | `557/688 (81.1)` remains a printed arithmetic issue. The corresponding sensitivity difference and ORPA have compatible direction, interval containment, and printed P values. | S066 | PASS_2_COMPLETE; no added statistical candidate. |
| C009 | Direct recheck confirms the Table 3 absolute-difference display is `-0.7 (95% CI, -1.1 to +0.2)` with adjacent `P=.009`; the CI contains 0. The distinct HR block is `.96 (.90 to 1.02), P=.14`. The article's two-sided statement supports the null-boundary comparison, while missing estimator/variance/df details preclude an exact inversion. | S023 | PASS_2_COMPLETE; existing C009 is retained pending human adjudication; no distinct new candidate. |
| C010 | The package separately labels patient-level mean (SD), an opportunity-level ORPA analysis, and a pooled baseline definition. This affects estimand mapping but does not identify a new incompatible printed point/interval/P pair after labels and populations are matched. | S002, S011, S031, S057 | PASS_2_COMPLETE; existing analysis-unit candidate creates no added statistical candidate. |
| C011 | `Within 48 hours` and `by end of hospital day 2` remain nonidentical labels absent an operational definition. The respective primary and sensitivity DVT effects are separately labeled by analysis population and remain directionally coherent. | S015, S061 | PASS_2_COMPLETE; no added statistical candidate. |

## Per-relationship completion record

| Stable ID | PASS_2 status | Second-pass checks and conclusion |
|---|---|---|
| S001 | PASS_2_COMPLETE | Main/protocol planned 4,800, 40 clusters, 80% power, 5% significance, ICC .02, and 5% target agree. C003 does not establish a different sample-size result. Exact power reconstruction lacks the design-effect and other inputs. NO_NEW_CANDIDATE. |
| S002 | PASS_2_COMPLETE | Composite 88.2 vs 84.8, difference 3.54 (.68 to 6.40), P=.02, and ORPA 1.39 (1.12 to 1.72), P=.003 retain ordered/containing intervals, positive direction, and matched repeats. C010 records differing labelled units but no new printed inferential contradiction. NO_NEW_CANDIDATE. |
| S003 | PASS_2_COMPLETE | All-or-none difference 6.69 (-.41 to 13.79), P=.06 and ORPA 1.19 (.85 to 1.67), P=.31 both contain their null and have compatible non-significant printed P values. NO_NEW_CANDIDATE. |
| S004 | PASS_2_COMPLETE | Three-month vascular-event difference -2.03 (-3.51 to -.55), P=.007 and HR .65 (.49 to .86), P=.002 have direction-consistent labels, exclude their nulls, and match repeats. NO_NEW_CANDIDATE. |
| S005 | PASS_2_COMPLETE | Six-month vascular-event difference -2.18 (-4.0 to -.35), P=.02 and HR .72 (.57 to .90), P=.004 are ordered, null-excluding, and directionally matched. NO_NEW_CANDIDATE. |
| S006 | PASS_2_COMPLETE | Twelve-month vascular-event difference -3.13 (-5.28 to -.97), P=.005 and HR .72 (.60 to .87), P<.001 agree across narrative, Table 3, and Figure 2A after matching the same outcome/time point. NO_NEW_CANDIDATE. |
| S007 | PASS_2_COMPLETE | Supplied GEE/logistic/Cox/binary-link labels, adjustment set, 95% CI convention, and two-sided statement match their stated outcomes. Common variance/df/inversion definitions are absent. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S008 | PASS_2_COMPLETE | Three-month disability difference -3.72 (-6.7 to -.79), P=.01 and OR .76 (.63 to .91), P=.002 have consistent beneficial direction and null exclusion. NO_NEW_CANDIDATE. |
| S009 | PASS_2_COMPLETE | Six-month disability difference -3.86 (-6.60 to -1.13), P=.006 and OR .74 (.61 to .89), P=.002 are internally and directionally compatible. NO_NEW_CANDIDATE. |
| S010 | PASS_2_COMPLETE | Twelve-month disability difference -3.13 (-5.80 to -.46), P=.02 and OR .74 (.59 to .93), P=.01 retain compatible sign, interval, and P displays. NO_NEW_CANDIDATE. |
| S011 | PASS_2_COMPLETE | Sensitivity composite difference 4.20 (1.77 to 6.63), P<.001 and ORPA 1.36 (1.11 to 1.67), P=.003 match the eTable after associating each P with its own labelled column. C010 adds no matched-result contradiction. NO_NEW_CANDIDATE. |
| S012 | PASS_2_COMPLETE | Primary rtPA <=3-hour result 46/212 vs 23/204, difference 7.3 (-5.3 to 19.9), P=.26 and ORPA 3.18 (.94 to 10.78), P=.06 have compatible null-containing intervals and directions. NO_NEW_CANDIDATE. |
| S013 | PASS_2_COMPLETE | Primary early-antithrombotics difference 1.5 (-.3 to 3.2), P=.10 and ORPA 1.93 (.94 to 3.95), P=.07 are compatible at displayed precision. NO_NEW_CANDIDATE. |
| S014 | PASS_2_COMPLETE | Primary dysphagia difference 1.6 (-2.1 to 5.3), P=.41 and ORPA 2.49 (.84 to 7.40), P=.10 have ordered null-containing intervals and compatible directions. NO_NEW_CANDIDATE. |
| S015 | PASS_2_COMPLETE | Primary DVT difference 15.6 (3.3 to 27.9), P=.01 and ORPA 2.42 (1.02 to 5.72), P=.04 are internally compatible. C011 is a timing-label issue, not a new effect/interval/P contradiction. NO_NEW_CANDIDATE. |
| S016 | PASS_2_COMPLETE | Primary discharge-antithrombotics difference 4.2 (-.6 to 8.9), P=.09 and ORPA 2.29 (.86 to 6.11), P=.10 remain compatible. NO_NEW_CANDIDATE. |
| S017 | PASS_2_COMPLETE | Primary AF-anticoagulation difference 12.9 (-5.8 to 31.6), P=.18 and ORPA 1.80 (.68 to 4.75), P=.23 remain directionally and inferentially compatible. NO_NEW_CANDIDATE. |
| S018 | PASS_2_COMPLETE | Primary lipid-lowering difference 2.4 (-1.6 to 6.4), P=.25 and ORPA 1.35 (.67 to 2.73), P=.40 have compatible null decisions. C002 concerns eligibility wording, not these matched estimate/interval/P displays. NO_NEW_CANDIDATE. |
| S019 | PASS_2_COMPLETE | Primary antihypertensive difference 6.1 (-.6 to 12.7), P=.07 and ORPA 1.44 (.94 to 2.20), P=.10 are compatible. NO_NEW_CANDIDATE. |
| S020 | PASS_2_COMPLETE | Primary antidiabetic difference 5.0 (.8 to 9.3), P=.02 and ORPA 1.57 (1.08 to 2.28), P=.02 are ordered, positive, and null excluding. NO_NEW_CANDIDATE. |
| S021 | PASS_2_COMPLETE | Figure 2A/Table 3 HR .72 (.60 to .87), P<.001 is a matched 12-month vascular-event display and agrees in direction with the corresponding count/difference result. NO_NEW_CANDIDATE. |
| S022 | PASS_2_COMPLETE | Figure 2B/Table 3 death HR .86 (.68 to 1.09), P=.21 has a null-containing interval and compatible P value. NO_NEW_CANDIDATE. |
| S023 | PASS_2_COMPLETE | In-hospital death absolute-difference CI -1.1 to +0.2 contains 0 while same-block P=.009 is below .05; direct recheck confirms positive `+0.2` and distinct HR/P block. This is the exact C009 observation; missing common construction details are recorded. No distinct additional candidate. |
| S024 | PASS_2_COMPLETE | Three-month death difference -1.0 (-2.1 to .1), P=.08 and HR .81 (.57 to 1.15), P=.23 retain compatible null decisions. NO_NEW_CANDIDATE. |
| S025 | PASS_2_COMPLETE | Six-month death difference -.5 (-1.7 to .6), P=.38 and HR .97 (.73 to 1.29), P=.81 are separately adjusted estimates and are internally compatible; crude counts do not require adjusted HR=1. NO_NEW_CANDIDATE. |
| S026 | PASS_2_COMPLETE | Twelve-month death difference -1.5 (-3.0 to -.0), P=.05 is boundary-compatible at displayed rounding; HR .86 (.68 to 1.09), P=.21 is a distinct measure. NO_NEW_CANDIDATE. |
| S027 | PASS_2_COMPLETE | Symptomatic ICH 1/46 vs 2/23 and P=.26 have direction-consistent counts. No source-defined test/CI/variance rule permits further exact checking. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S028 | PASS_2_COMPLETE | Protocol sample-size parameters repeat S001. C003 does not establish a competing planned sample-size display. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S029 | PASS_2_COMPLETE | Protocol descriptive-statistics labels (proportion, mean/SD, median/IQR) introduce no conflicting reported result. NO_NEW_CANDIDATE. |
| S030 | PASS_2_COMPLETE | Protocol univariate-test labels are not linked to a uniquely reconstructable displayed P in the supplied results. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S031 | PASS_2_COMPLETE | Protocol GEE/population-average OR and mean-difference definitions match article model labels. C010 identifies an unresolved estimator/unit mapping, but no newly conflicting printed inference. NO_NEW_CANDIDATE. |
| S032 | PASS_2_COMPLETE | Protocol Kaplan-Meier/Cox plan matches the clinical-event/mortality model labels and time points in the article. NO_NEW_CANDIDATE. |
| S033 | PASS_2_COMPLETE | Baseline 80.2 vs 79.5 has no printed P and is pre-randomization. C001/C003 do not establish a matched inferential contradiction. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S034 | PASS_2_COMPLETE | eTable 2 age P=.81 accompanies identical printed medians/IQRs; exact test mapping is not supplied. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S035 | PASS_2_COMPLETE | eTable 2 male 2497/3949 vs 546/851, P=.61 has coherent denominators and no supplied exact test reconstruction rule. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S036 | PASS_2_COMPLETE | eTable 2 ischemic-stroke history 1137/3949 vs 251/851, P=.68 is directionally/denominator coherent. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S037 | PASS_2_COMPLETE | eTable 2 diabetes 890/3949 vs 196/851, P=.75 is denominator coherent with no named exact test construction. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S038 | PASS_2_COMPLETE | eTable 2 hypertension 2552/3949 vs 538/851, P=.44 is denominator coherent with no named exact test construction. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S039 | PASS_2_COMPLETE | eTable 2 dyslipidemia 285/3949 vs 62/851, P=.94 is denominator coherent with no named exact test construction. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S040 | PASS_2_COMPLETE | eTable 2 CAD/previous-MI 512/3949 vs 97/851, P=.21 remains compatible; C001 concerns another table/population. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S041 | PASS_2_COMPLETE | eTable 2 atrial fibrillation 200/3949 vs 45/851, P=.79 is denominator coherent with no named exact test construction. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S042 | PASS_2_COMPLETE | eTable 2 ever smoking 1736/3949 vs 380/851, P=.71 is denominator coherent with no named exact test construction. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S043 | PASS_2_COMPLETE | eTable 2 NIHSS 3 (2 to 6) vs 3 (2 to 6), P=.99 has identical displayed summaries; scale is stated as 0-42. NO_NEW_CANDIDATE; DEFINITION_LIMITATION_RECORDED. |
| S044 | PASS_2_COMPLETE | Three-month ischemic-stroke difference -.57 (-1.91 to .76), P=.40 and HR .89 (.59 to 1.36), P=.59 are null-containing and count-direction coherent. NO_NEW_CANDIDATE. |
| S045 | PASS_2_COMPLETE | Three-month hemorrhagic-stroke difference -.35 (-.92 to .22), P=.23 and HR .85 (.40 to 1.83), P=.68 are compatible. NO_NEW_CANDIDATE. |
| S046 | PASS_2_COMPLETE | Three-month MI difference -.10 (-.36 to .17), P=.48 and HR .58 (.13 to 2.67), P=.48 are compatible at displayed precision. NO_NEW_CANDIDATE. |
| S047 | PASS_2_COMPLETE | Three-month vascular-death difference -1.43 (-2.33 to -.54), P=.001 and HR .62 (.42 to .92), P=.02 agree in direction and null exclusion. NO_NEW_CANDIDATE. |
| S048 | PASS_2_COMPLETE | Six-month ischemic-stroke difference -1.40 (-2.82 to -.02), P=.05 and HR .72 (.53 to .99), P=.04 are rounded-boundary displays consistent with negative direction. NO_NEW_CANDIDATE. |
| S049 | PASS_2_COMPLETE | Six-month hemorrhagic-stroke difference -.25 (-.80 to .30), P=.38 and HR .92 (.46 to 1.82), P=.80 are compatible. NO_NEW_CANDIDATE. |
| S050 | PASS_2_COMPLETE | Six-month MI difference -.03 (-.35 to .29), P=.86 and HR .78 (.27 to 2.24), P=.64 are compatible. Equal crude event counts do not impose HR=1 under the supplied Cox model. NO_NEW_CANDIDATE. |
| S051 | PASS_2_COMPLETE | Six-month vascular-death difference -1.06 (-2.08 to -.04), P=.04 and HR .78 (.56 to 1.10), P=.16 are distinct labeled measures and individually compatible. NO_NEW_CANDIDATE. |
| S052 | PASS_2_COMPLETE | Twelve-month ischemic-stroke difference -1.84 (-3.45 to -.23), P=.03 and HR .73 (.57 to .93), P=.01 are directionally and inferentially compatible. NO_NEW_CANDIDATE. |
| S053 | PASS_2_COMPLETE | Twelve-month hemorrhagic-stroke difference -.08 (-.71 to .55), P=.80 and HR 1.02 (.55 to 1.88), P=.96 are compatible. NO_NEW_CANDIDATE. |
| S054 | PASS_2_COMPLETE | Twelve-month MI difference -.13 (-.46 to .21), P=.45 and HR .71 (.30 to 1.67), P=.43 are compatible. NO_NEW_CANDIDATE. |
| S055 | PASS_2_COMPLETE | Twelve-month vascular-death difference -1.94 (-3.26 to -.62), P=.004 and HR .71 (.54 to .94), P=.02 agree in direction and null exclusion. NO_NEW_CANDIDATE. |
| S056 | PASS_2_COMPLETE | eTable 3 expressly permits different vascular-event types in one patient; component sums therefore do not identify a duplicate-value or denominator conflict. NO_NEW_CANDIDATE. |
| S057 | PASS_2_COMPLETE | Sensitivity composite difference 4.20 (1.77 to 6.63), P<.001 and ORPA 1.36 (1.11 to 1.67), P=.003 match S011 after column-specific P matching. C010 adds no new conflicting result. NO_NEW_CANDIDATE. |
| S058 | PASS_2_COMPLETE | Sensitivity rtPA <2-hour difference 5.81 (-4.57 to 16.19), P=.27 and ORPA 2.60 (.76 to 8.87), P=.13 are compatible. C004 recheck confirms 23/238 (9.66), eliminating the discovery transcription as an additional statistical issue. NO_NEW_CANDIDATE. |
| S059 | PASS_2_COMPLETE | Sensitivity early-antithrombotics difference 2.68 (.48 to 4.87), P=.02 and ORPA 1.73 (1.05 to 2.87), P=.03 are compatible. NO_NEW_CANDIDATE. |
| S060 | PASS_2_COMPLETE | Sensitivity dysphagia difference 1.72 (-1.95 to 5.40), P=.36 and ORPA 2.37 (.69 to 8.18), P=.17 are compatible. NO_NEW_CANDIDATE. |
| S061 | PASS_2_COMPLETE | Sensitivity DVT difference 14.79 (3.16 to 26.42), P=.01 and ORPA 2.09 (.95 to 4.62), P=.07 have distinct labelled estimates; C011 is a timing-label issue only. NO_NEW_CANDIDATE. |
| S062 | PASS_2_COMPLETE | Sensitivity discharge-antithrombotics difference 5.32 (.44 to 10.20), P=.03 and ORPA 1.89 (.99 to 3.64), P=.05 remain compatible. C005 is a separately printed fraction/percentage issue. NO_NEW_CANDIDATE. |
| S063 | PASS_2_COMPLETE | Sensitivity AF-anticoagulation difference 12.90 (-3.51 to 29.3), P=.12 and ORPA 1.78 (.61 to 5.14), P=.29 are compatible. C006 is separately arithmetic. NO_NEW_CANDIDATE. |
| S064 | PASS_2_COMPLETE | Sensitivity lipid-lowering difference 2.46 (-2.03 to 6.95), P=.28 and ORPA 1.17 (.61 to 2.24), P=.63 are compatible. C002/C007 retain their stated label/arithmetic comparisons without a new inferential discrepancy. NO_NEW_CANDIDATE. |
| S065 | PASS_2_COMPLETE | Sensitivity antihypertensive difference 6.32 (-.58 to 13.21), P=.07 and ORPA 1.47 (.97 to 2.23), P=.07 are compatible. NO_NEW_CANDIDATE. |
| S066 | PASS_2_COMPLETE | Sensitivity antidiabetic difference 6.16 (1.70 to 10.62), P=.007 and ORPA 1.59 (1.11 to 2.23), P=.01 are directionally/inferentially compatible. C008 is separately arithmetic. NO_NEW_CANDIDATE. |
| S067 | PASS_2_COMPLETE | eTable 4 adjustment-covariate statement and ORPA definition match the sensitivity-effect label. No duplicate-value, scale, or cross-source inference conflict is identified. NO_NEW_CANDIDATE. |

## Pass-2 result and limitations

- **Canonical relationships completed:** 67 of 67: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067.
- **New provisional candidates:** 0. No `SP2-NEW-*` identifier was issued.
- **Existing-ledger reconciliation:** C004's direct source reads `9.66` and reconciles at two decimals; C009's source reads CI `-1.1 to +0.2` with same-block `P=.009`. These are recorded as source facts without adjudicating any existing ID.
- **Display-zero exclusion:** No mapped display-zero P value occurred.
- **Limitations:** Exact interval/P/test compatibility cannot be reconstructed where the supplied package omits an explicit estimator-to-CI/P mapping, variance estimator, covariance, degrees of freedom, sidedness for the specific comparison, or adjustment/inversion rule. Primary and sensitivity results were not equated when their supplied analysis populations or denominators differ.
