# Statistical Relationship Inventory — Pass 1 and Pass 2

## Scope and conventions

This is the package-wide pass-1 inventory rebuilt from the mapped main-result
relationships (`S001`-`S017` in the main map) and mapped support
definitions/models (`S-SUP-001`-`S-SUP-016`).  Stable IDs below are new for this
review and cover every mapped inferential relationship.  Direct PDF checking was
used for the three candidate observations and for the main table/eFigure labels.
The remaining mapped values were checked against the supplied source-linked
extractions.  `PASS_1_COMPLETE` means that the specified pass-1 checks were
performed; it is not an adjudication.

Compatibility rule: point estimate containment and endpoint ordering were
checked whenever an interval was printed.  Direction, effect-measure/scale
labels, and matched repetitions were checked where present.  Interval/P-value
compatibility is marked **diagnostic** only unless the source supplies the same
model, 95% CI, and two-sided inferential framework.  No sidedness, degrees of
freedom, covariance, variance estimator, multiplicity rule, or unprinted
estimand was inferred.

No `P = 0`, `p = 0.000`, or equivalent finite-precision display zero was found
in the assigned mapped inferential results; `DISPLAY_ZERO_NOT_CANDIDATE` was
therefore not applicable to an individual record.

## Stable relationship records

| Stable ID | Crosswalked mapped relationship | Exact supplied locations | Pass-1 checks and result | Pass-1 status |
|---|---|---|---|---|
| S001 | Abstract primary GI-3 result: adjusted absolute difference and RR | DOC-001 p. 1 | Difference -1.9% lies in -8.0% to 4.2%; RR 0.97 lies in 0.88 to 1.07; endpoint order, negative direction, RR label, and abstract/main repeat agree. No P is printed here. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S002 | Main-text primary GI-3 analysis | DOC-001 p. 5 | Same values as S001 and Table 2. With stated 95% CI and P=.54, a log-RR/normal diagnostic gives a two-sided P near .54; compatible after rounding. Fixed age/sex effects and random site effect are supplied. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S003 | Per-protocol primary GI-3 analysis | DOC-001 pp. 5-6 | Difference -2.3 lies in -8.9 to 4.3 and RR 0.96 lies in 0.86 to 1.07; P=.49 is diagnostically compatible with the displayed 95% RR interval and direction. The per-protocol denominator is separately labelled 267/265. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S004 | Main-paper sample-size/power statement | DOC-001 p. 5 | 60.0% to 73.2% is +13.2 percentage points and a 22% relative increase; complementing these rates gives non-return 40.0% to 26.8%, a 33% relative reduction. It reconciles with S030. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S005 | Time to GI-3 recovery HR | DOC-001 p. 6; DOC-003 pp. 14, 20, 34 | HR 0.98 lies in 0.83 to 1.17, endpoints ordered, and HR/Cox labels agree with the supplied plan/code. No P is printed. Time origin wording is not sufficiently defined to equate “after operation” with every protocol time-origin phrase. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S006 | Time to GI-2 recovery HR | DOC-001 p. 6; DOC-003 pp. 14, 20, 34 | HR 1.03 lies in 0.86 to 1.23, endpoints ordered, and HR/Cox labels agree. No P is printed. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S007 | Prolonged postoperative ileus: difference and IRR | DOC-001 p. 6; DOC-003 pp. 10, 21, 35 | Difference 1.8 lies in -3.3 to 6.8 and IRR 1.13 lies in 0.80 to 1.61; labels and event-direction definition agree. No P is printed. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S008 | Repeated OBAS score contrasts, postoperative days 1-7 | DOC-001 p. 6; DOC-003 pp. 14, 24, 35 | All seven estimates lie in ordered 95% CIs. Stated linear mixed model/time-by-treatment contrasts and displayed two-sided Ps are diagnostically compatible after rounding. OBAS direction is supplied (lower score means greater analgesic benefit); no contrary narrative interpretation was found. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S009 | Repeated QoR-15 score contrasts, days 1-7 and day 30 | DOC-001 p. 6; DOC-003 pp. 14, 25, 35 | All eight estimates lie in ordered 95% CIs; stated mixed-model/time-by-treatment contrasts and Ps are diagnostically compatible after rounding. QoR-15 0-150, higher-better scale agrees with its label. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S010 | Repeated EQ-5D-5L utility contrasts, days 1-7, day 30, day 90 | DOC-001 p. 6; DOC-003 pp. 14, 25, 36 | All nine estimates lie in ordered 95% CIs and P values are diagnostically compatible. Day-5 estimate -0.057, CI -0.111 to -0.003, P=.04 is an individually non-null nominal table result; its conflict with the prose quality-of-life statement is recorded as Candidate observation 1 in the pass-1 checker. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S011 | Time to clinician-assessed and patient-assessed discharge readiness | DOC-001 p. 7; DOC-003 pp. 26, 36 | Both HRs 0.99 lie in their ordered CIs (0.84-1.17; 0.83-1.17). HR/Cox labels in the article and planned GLM wording/code are insufficiently identical to derive an additional test; no P is printed. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S012 | Total length of stay: negative-binomial IRR | DOC-001 p. 8; DOC-003 pp. 27, 36 | IRR 1.03 lies in 0.92-1.14; endpoints ordered, IRR/negative-binomial label agrees with the article, and no P is printed. The support template lacks populated results. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S013 | eFigure overall primary-effect repeat | DOC-004 p. 2; DOC-001 pp. 1, 5-6 | RR 0.97 (0.88,1.07) matches S001/S002 and its 95% CI. The forest-plot legend’s “99% CI” is visually attached to the subgroup bars; the prose identifies the right-side within-subgroup values as 95% CIs. The directly conflicting CI-level labels are recorded under S014-S018, not treated as a discrepancy in the repeated overall estimate. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S014 | Intended-duration subgroup RRs and interaction P=.401 | DOC-004 p. 2; DOC-003 pp. 15, 37 | Each RR lies in ordered displayed interval; duration Ns sum to 532, the treatment-recipient per-protocol population. CI level is internally contradictory: legend 99% versus prose 95%; Candidate observation 2. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S015 | Operation subgroup RRs and interaction P=.773 | DOC-004 p. 2; DOC-003 pp. 15, 37 | Each RR lies in ordered interval; Ns sum to 557. CI-level label conflict noted in S014 applies to this printed subgroup interval too. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S016 | Sex subgroup RRs and interaction P=.830 | DOC-004 p. 2; DOC-003 pp. 15, 37 | Each RR lies in ordered interval; Ns sum to 557. CI-level label conflict noted in S014 applies. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S017 | Age subgroup RRs and interaction P=.162 | DOC-004 p. 2; DOC-003 pp. 15, 38 | Each RR lies in ordered interval; Ns sum to 557. CI-level label conflict noted in S014 applies. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S018 | ERAS-adherence subgroup RRs and interaction P=.966 | DOC-001 p. 5; DOC-004 p. 2; DOC-003 pp. 3, 15, 38 | Each RR lies in ordered interval; high/moderate/low Ns sum to 557. Main text calls the subgroup “high vs low,” whereas the eFigure and SAP enumerate high/moderate/low; Candidate observation 3. CI-level label conflict noted in S014 also applies. SAP version history says the ERAS subgroup was included after analysis while describing it as pre-planned; that chronology alone does not establish a numerical or inferential contradiction. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S019 | Support primary GI-3 estimand and log-link model | DOC-002 pp. 15-18, 40; DOC-003 pp. 9-10, 14, 20, 32-34 | Binary GI-3 definition, ITT population, log-link model, minimisation adjustment, centre random effect, robust variance, and exponentiation are supplied and consistent with S001-S002 labels. SAP records a post-analysis correction from “logit” to “log”; this is source provenance, not a conflicting final printed effect. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S020 | Support GI-2/GI-3 time-to-event definitions and Cox plan | DOC-002 pp. 15-18; DOC-003 pp. 10, 14, 20, 34 | Endpoint definitions and Cox/shared-centre-frailty code provide compatible labels for S005-S006. No corresponding P, test statistic, or SE is printed for article HRs. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S021 | Support PPOI binary definition and log-link model | DOC-002 pp. 15-18, 40; DOC-003 pp. 10, 21, 35 | PPOI failure-by-120-h direction and adjusted log-link model agree with S007. No P/test statistic/SE is supplied. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S022 | Support PONV definition/threshold and planned descriptive output | DOC-002 pp. 10, 15-18, 30-37, 61; DOC-003 pp. 10-12, 21 | Score >=5 and daily denominator definitions identify the Table 2 PONV counts. No inferential estimate, CI, or P is supplied for those counts; no compatibility test is applicable. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S023 | Support OBAS formula, direction, and repeated-model definition | DOC-002 pp. 17, 31-37, 60; DOC-003 pp. 19, 24, 32, 35 | Formula and lower-is-better direction agree with S008; source supplies a mixed model and interaction contrast but not enough model output to derive an exact alternative calculation. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S024 | Support QoR-15 scale and repeated-model definition | DOC-002 pp. 17, 31-37; DOC-003 pp. 16, 25, 32, 35 | 0-150/higher-better scale and interaction model agree with S009. No additional exact test inputs supplied. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S025 | Support EQ-5D/QALY scale and repeated-model definition | DOC-002 pp. 17, 31-37, 41-42; DOC-003 pp. 16, 25, 32, 36 | Repeated EQ-5D model and separate health-economic measures are distinguished. The plan supplies no estimand mapping that could resolve the prose/table conflict in S010; Candidate observation 1 remains a human question. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S026 | Support ERAS categories and exploratory interaction framework | DOC-002 pp. 17-18, 31-37; DOC-003 pp. 3, 14-15, 26, 36, 38 | Protocol categories, SAP high/moderate/low subgroup, and eFigure category labels agree; this exposes the main-text two-level wording recorded in S018/Candidate observation 3. No unreported contrast is inferred. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S027 | Support discharge-readiness definitions and planned model | DOC-002 p. 18; DOC-003 pp. 26, 36 | Five versus six discharge criteria distinguish the two S011 outcomes. Article HR/Cox reporting and support `meglm` code are not sufficiently defined as one identical estimand to test P/SE compatibility. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S028 | Support length-of-stay, mortality/readmission, and safety inferential plan | DOC-002 pp. 18-19, 34-35; DOC-003 pp. 10, 27, 36 | Support source assigns adjusted GLM analysis to total stay and descriptive/safety treatment to the other outcomes; consistent with S012’s sole printed IRR. No missing P is inferred. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S029 | Support population, randomisation, treatment, and ITT definitions | DOC-002 pp. 19-20, 23-24; DOC-003 pp. 8-9, 13-15, 17 | Participant-level 1:1 allocation and treatment-received/per-protocol distinction provide the population labels for S001-S004 and S014. No incompatible inferred population is found. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S030 | Support sample-size/power basis | DOC-002 pp. 19-20, 40; DOC-003 pp. 13-15 | 562, 90%, two-sided 5%, and 40% to 26.8% non-return reconcile arithmetically with S004. No calculation inputs for an independent power recomputation are supplied. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S031 | Support CI, multiplicity, missing-data, and sensitivity framework | DOC-003 pp. 13-16 | States 95% CIs except subgroup analyses and no secondary multiplicity adjustment. It supports reading the S010 Day-5 95% CI/P as a nominal table inference but does not supply a separate declared narrative decision rule. | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S032 | Support subgroup interaction framework and 99% CI specification | DOC-003 pp. 14-15, 37-38 | Prespecified interactions, 1% two-sided threshold, and corresponding 99% CI are stated. This independently supports the forest-plot legend and conflicts with the eFigure prose claim of 95% CIs (Candidate observation 2). | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S033 | p-POSSUM predictive-mortality formula and score range | DOC-003 pp. 18-19, 31-32 | Formula, component score ranges, and missing-item rule are supplied only in plan/template material; no populated observed risk, CI, or P exists for cross-check. | PASS_1_COMPLETE; PASS_2_COMPLETE |

## Pass-1 candidate observations and limitations

Three distinct candidate observations were emitted to
`checkers/statistical_pass_1.md`, without candidate IDs.  Their exact source
locations, printed values, and rules are there for coordinator merging.  The
limitations are: unreported degrees of freedom and variance details for all
displayed interval/P diagnostics; no printed P for several HR/IRR results;
ambiguous time-origin wording across article and support sources; and no stated
narrative decision rule that resolves the Day-5 EQ-5D table result.  These are
recorded, not filled by convention.

Pass 1 relationship count: **33**.  Pass 1 candidate-observation count: **3**.
