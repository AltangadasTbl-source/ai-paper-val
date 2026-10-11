# Statistical Consistency Review — Pass 2

## Completion and scope

- **Status:** PASS_2_COMPLETE.
- **Independent pass scope:** all 151 stable statistical relationships: S001-S148, S028a, S028b, and S029a. The pass revisited the supplied direct-source results, the complete current cross-lane candidate ledger (C001-C005), numeric and cross-source checker records, pass-1 records, and the mechanical evidence recheck.
- **Checks applied:** denominator/arithmetic/population implications; point-estimate containment and endpoint ordering; sign, direction, effect-measure, scale, reference, rate/count, duplicate-value, figure, and cross-location implications; and interval/P/test/statistic/SE compatibility only where a matching supplied model and inferential definition were available.
- **No adjudication:** this record assigns no severity, validity, acceptance, rejection, correction, or other disposition.

## Pass-2 reconciliation

1. **Containment, ordering, direction, label, and scale.** The printed estimates and positive odds ratios in S001-S067 remain inside correctly ordered printed intervals. The source-defined direction is retained: Table 2/eTable 2 continuous differences are surgery minus medical/lifestyle changes; eTable 4 differences are surgical minus medical means; binary group differences are odds ratios. Net HbA1c change, relative percent change, urine albumin:creatinine fold change, rates/percentages, counts, and ORs were not interchanged.
2. **Denominator, rate/count, population, arithmetic, and duplicate-value implications.** S004/S032/S128 retain the C005 death-rate population issue without creating a duplicate statistical proposal; the within-group counts and percentages still reconcile to 96 and 166, while the abstract denominator remains unspecified. S136 retains the C001 Figure 1 population implication without treating original allocation counts as the enrolled analysis denominators. S053-S060 and S068-S121 retain event/procedure counts as rates or counts exactly as labelled; zero event counts/percentages and `NA` test entries are not P-value displays.
3. **Cross-location and figure implications.** S001, S003, S007-S013, S016-S034, S038, S042, S044, S050-S052, S116, and S122-S138 were revisited against matched direct-source locations. Same-result repetitions remain compatible at stated precision except the already registered eTable 2 time-label issue (C002) and matched HbA1c P-value issue (C003). Overall longitudinal figure P values were not compared as if they were single-visit contrasts. Sparse visual coordinates were not reverse engineered.
4. **Ledger/recheck implications.** C002 directly affects the time/estimand interpretation of S036-S052, S129-S130, and S137; C003 directly affects S002, S036, and S129; C004 directly affects S009 and S029a. C001 and C005 add population/denominator context to S136 and S004/S032/S128, respectively. The recheck supplies no new independently distinct contradiction for another S relationship.
5. **Interval/P/test/statistic/SE boundary.** The supplied mixed-model, GEE, IPW, chi-square/Fisher-family, and planned-primary-test descriptions support the label/direction checks above. Exact reconstruction was not performed for secondary, event, and most table rows because the package does not supply every row's test selection, sidedness, degrees of freedom, covariance, variance estimator, confidence convention, or unrounded parameter values. eTable 4's rounded estimate/SE/P combinations (S061-S067) show no direct printed contradiction, but its row-specific test/df and unrounded values are absent; no diagnostic approximation is presented as a reconstructed test.
6. **Display-zero boundary.** No `P = 0`, `p = 0.000`, or equivalent P-value display occurs in this statistical inventory. S047, S057, S060, S080, S082, S084, S086-S088, S100, S104, S107-S108, S117-S121, S131, and S147 include zero event counts, zero percentages, `NA`, or the explicitly supplied remission rate `2e-16`; these are not P-value display-zero candidate triggers. P inequalities such as `<.001` are likewise not display zeros.

## Stable relationship coverage record

Each named record below received the checks described above and is explicitly `PASS_2_COMPLETE`.

| Stable S ID | Pass-2 record |
|---|---|
| S001 | PASS_2_COMPLETE — containment, direction, matched repetitions; definitions limited exact reconstruction. |
| S002 | PASS_2_COMPLETE — C003 cross-location P implication retained; no duplicate proposal. |
| S003 | PASS_2_COMPLETE — OR/rate direction and matched repetitions checked. |
| S004 | PASS_2_COMPLETE — C005 denominator/rate implication retained; no duplicate proposal. |
| S005 | PASS_2_COMPLETE — primary model/contrast label checked. |
| S006 | PASS_2_COMPLETE — IPW/GEE/multiplicity labels checked without inference. |
| S007 | PASS_2_COMPLETE — procedure contrast direction and intervals checked. |
| S008 | PASS_2_COMPLETE — IPW direction/interval/scale checked. |
| S009 | PASS_2_COMPLETE — C004 threshold-label implication retained; no duplicate proposal. |
| S010 | PASS_2_COMPLETE — medication directions and matched labels checked. |
| S011 | PASS_2_COMPLETE — year-specific weight direction/repetitions checked. |
| S012 | PASS_2_COMPLETE — figure/narrative direction checked; no visual reconstruction. |
| S013 | PASS_2_COMPLETE — remission/procedure labels checked. |
| S014 | PASS_2_COMPLETE — table scale/available-measurement labels checked. |
| S015 | PASS_2_COMPLETE — model-derived change/OR framework checked. |
| S016 | PASS_2_COMPLETE — containment, direction, S001 repetition checked. |
| S017 | PASS_2_COMPLETE — interval/null direction and scale checked. |
| S018 | PASS_2_COMPLETE — containment, direction, figure repetition checked. |
| S019 | PASS_2_COMPLETE — interval/null direction and narrative checked. |
| S020 | PASS_2_COMPLETE — interval/null direction checked. |
| S021 | PASS_2_COMPLETE — interval/null direction and narrative checked. |
| S022 | PASS_2_COMPLETE — containment/direction and narrative checked. |
| S023 | PASS_2_COMPLETE — interval/null direction checked. |
| S024 | PASS_2_COMPLETE — containment/direction and narrative checked. |
| S025 | PASS_2_COMPLETE — interval/null direction checked. |
| S026 | PASS_2_COMPLETE — fold-change/difference scale checked. |
| S027 | PASS_2_COMPLETE — OR containment and rate direction checked. |
| S028 | PASS_2_COMPLETE — OR containment and medication direction checked. |
| S028a | PASS_2_COMPLETE — OR containment/null direction checked. |
| S028b | PASS_2_COMPLETE — OR containment and medication direction checked. |
| S029 | PASS_2_COMPLETE — OR containment/rate direction checked. |
| S029a | PASS_2_COMPLETE — C004 threshold-label implication retained; OR containment checked. |
| S030 | PASS_2_COMPLETE — subgroup direction/interval/interaction label checked. |
| S031 | PASS_2_COMPLETE — clinical/lipid repetitions checked. |
| S032 | PASS_2_COMPLETE — C005 rate/denominator implication retained; no duplicate proposal. |
| S033 | PASS_2_COMPLETE — crossover/revision labels checked. |
| S034 | PASS_2_COMPLETE — safety-event labels checked. |
| S035 | PASS_2_COMPLETE — shared method labels checked. |
| S036 | PASS_2_COMPLETE — C002/C003 time and P implications retained; no duplicate proposal. |
| S037 | PASS_2_COMPLETE — interval/null direction checked. |
| S038 | PASS_2_COMPLETE — weight direction/repetition checked. |
| S039 | PASS_2_COMPLETE — interval/null direction checked. |
| S040 | PASS_2_COMPLETE — interval/null direction checked. |
| S041 | PASS_2_COMPLETE — interval/null direction checked. |
| S042 | PASS_2_COMPLETE — containment/direction checked. |
| S043 | PASS_2_COMPLETE — interval/null direction checked. |
| S044 | PASS_2_COMPLETE — containment/direction checked. |
| S045 | PASS_2_COMPLETE — interval/null direction checked. |
| S046 | PASS_2_COMPLETE — fold-change/difference scale checked. |
| S047 | PASS_2_COMPLETE — rate/OR/NA labels checked; not a display-zero P result. |
| S048 | PASS_2_COMPLETE — OR containment/null direction checked. |
| S049 | PASS_2_COMPLETE — OR containment/null direction checked. |
| S050 | PASS_2_COMPLETE — OR containment/rate direction checked. |
| S051 | PASS_2_COMPLETE — OR containment/rate direction checked. |
| S052 | PASS_2_COMPLETE — OR containment/rate direction checked. |
| S053 | PASS_2_COMPLETE — count/percentage/reference labels checked. |
| S054 | PASS_2_COMPLETE — count/percentage/reference labels checked. |
| S055 | PASS_2_COMPLETE — count/percentage/reference labels checked. |
| S056 | PASS_2_COMPLETE — count/percentage/reference labels checked. |
| S057 | PASS_2_COMPLETE — zero counts/NA are not P displays. |
| S058 | PASS_2_COMPLETE — count/percentage/reference labels checked. |
| S059 | PASS_2_COMPLETE — count/percentage/reference labels checked. |
| S060 | PASS_2_COMPLETE — zero count/percentage is not a P display. |
| S061 | PASS_2_COMPLETE — LS mean/difference/SE labels checked; exact test undefined. |
| S062 | PASS_2_COMPLETE — LS mean/difference/SE labels checked; exact test undefined. |
| S063 | PASS_2_COMPLETE — LS mean/difference/SE labels checked; exact test undefined. |
| S064 | PASS_2_COMPLETE — LS mean/difference/SE labels checked; exact test undefined. |
| S065 | PASS_2_COMPLETE — rounded SE 0.0 retained; exact test undefined. |
| S066 | PASS_2_COMPLETE — LS mean/difference/SE labels checked; exact test undefined. |
| S067 | PASS_2_COMPLETE — LS mean/difference/SE labels checked; exact test undefined. |
| S068 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S069 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S070 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S071 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S072 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S073 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S074 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S075 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S076 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S077 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S078 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S079 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S080 | PASS_2_COMPLETE — zero count/percentage is not a P display. |
| S081 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S082 | PASS_2_COMPLETE — zero count/percentage is not a P display. |
| S083 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S084 | PASS_2_COMPLETE — zero count/percentage is not a P display. |
| S085 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S086 | PASS_2_COMPLETE — zero count/percentage is not a P display. |
| S087 | PASS_2_COMPLETE — zero count/percentage is not a P display. |
| S088 | PASS_2_COMPLETE — zero count/percentage is not a P display. |
| S089 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S090 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S091 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S092 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S093 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S094 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S095 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S096 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S097 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S098 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S099 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S100 | PASS_2_COMPLETE — zero count/percentage is not a P display. |
| S101 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S102 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S103 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S104 | PASS_2_COMPLETE — zero count/percentage is not a P display. |
| S105 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S106 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S107 | PASS_2_COMPLETE — zero count/percentage is not a P display. |
| S108 | PASS_2_COMPLETE — zero count/percentage is not a P display. |
| S109 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S110 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S111 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S112 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S113 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S114 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S115 | PASS_2_COMPLETE — event count/rate and test-family label checked. |
| S116 | PASS_2_COMPLETE — count/rate direction and repetition checked. |
| S117 | PASS_2_COMPLETE — procedure counts/rates and test-family labels checked. |
| S118 | PASS_2_COMPLETE — procedure counts/rates and test-family labels checked. |
| S119 | PASS_2_COMPLETE — procedure counts/rates and test-family labels checked. |
| S120 | PASS_2_COMPLETE — procedure counts/rates and test-family labels checked. |
| S121 | PASS_2_COMPLETE — procedure counts/rates and test-family labels checked. |
| S122 | PASS_2_COMPLETE — figure model/scale/P labels checked; no visual reconstruction. |
| S123 | PASS_2_COMPLETE — protocol planned-model labels checked. |
| S124 | PASS_2_COMPLETE — protocol power context retained; not observed result. |
| S125 | PASS_2_COMPLETE — parent-trial context not matched to current outcome. |
| S126 | PASS_2_COMPLETE — crossover components/rate labels checked. |
| S127 | PASS_2_COMPLETE — LS/raw figure-scale distinction checked. |
| S128 | PASS_2_COMPLETE — C005 denominator/rate implication retained; no duplicate proposal. |
| S129 | PASS_2_COMPLETE — C002/C003 cross-location implications retained. |
| S130 | PASS_2_COMPLETE — C002 time-label implication retained. |
| S131 | PASS_2_COMPLETE — finite-precision remission rate is not a P display. |
| S132 | PASS_2_COMPLETE — matched weight repetition checked. |
| S133 | PASS_2_COMPLETE — overall-versus-single-time comparison distinction retained. |
| S134 | PASS_2_COMPLETE — BMI-subgroup repetition/direction checked. |
| S135 | PASS_2_COMPLETE — per-protocol estimand label checked. |
| S136 | PASS_2_COMPLETE — C001 population implication retained; no duplicate proposal. |
| S137 | PASS_2_COMPLETE — source-specific time/scale labels checked; C002 retained. |
| S138 | PASS_2_COMPLETE — CI/SE display distinction checked; no exact reconstruction. |
| S139 | PASS_2_COMPLETE — finite P displays checked; no P=0 notation. |
| S140 | PASS_2_COMPLETE — P inequalities are not display-zero notation. |
| S141 | PASS_2_COMPLETE — planned-primary sidedness not extended to secondary results. |
| S142 | PASS_2_COMPLETE — surgery-minus-medical direction labels checked. |
| S143 | PASS_2_COMPLETE — surgery-subgroup reference labels checked. |
| S144 | PASS_2_COMPLETE — chi-square/Fisher family retained; row test unspecified. |
| S145 | PASS_2_COMPLETE — no applicable inferential statistic. |
| S146 | PASS_2_COMPLETE — P inequality with nonzero contrast; no display-zero issue. |
| S147 | PASS_2_COMPLETE — `2e-16` remission rate/`0%` display is not a P display. |
| S148 | PASS_2_COMPLETE — missing-definition register reviewed and retained. |

## New distinct proposals

**New-proposal count: 0.** The pass-2 review found no additional distinct supplied-source contradiction beyond C001-C005. The C002-C004 statistical implications remain linked to their existing ledger records; C001 and C005 remain denominator/population issues already represented in the ledger. No stable C ID was assigned or changed here.

## Limitations

- The package does not provide row-specific degrees of freedom, test statistics, covariance, variance estimator, exact test assignment for event/procedure rows, all secondary-result sidedness, all confidence conventions, or unrounded estimates/SEs.
- eTable 2's inconsistent year-7/year-12 labels leave its exact estimand mapping unresolved; no convention was used to select a time point.
- Figure trajectories lack sufficient printed coordinates for exact numerical comparisons; displayed figures were assessed only for their stated model, scale, direction, and direct repetitions.
- No web or external literature was used.
