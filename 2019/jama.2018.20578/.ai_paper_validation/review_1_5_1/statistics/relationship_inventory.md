# Canonical Inferential-Statistical Relationship Inventory — Pass 1

## Scope and method

This inventory canonicalizes the disjoint mapper records `MS001`-`MS013` and `SS001`-`SS008` into 21 stable inferential relationship IDs. It covers DOC-001 PDF pp. 1-10, DOC-002 PDF pp. 1-7, and DOC-003 PDF pp. 1-29. Pass 1 used the new 1.5.1 mapper artifacts as locators and verified the result-bearing direct PDF pages, including direct rendered/OCR confirmation of DOC-003 eFigure 4 pp. 22-26. No legacy candidate, checker, recheck, quality, or report artifact was used.

`PASS_1_COMPLETE` means that the stated pass-1 checks were completed; it is not an adjudication, validity decision, or severity assessment. Candidate proposals, if any, remain unnumbered and Pending Human Adjudication until coordinator registration.

## Canonical records

### S001 — Prespecified main-trial analysis framework

- **Mapper provenance:** MS001.
- **Direct source:** DOC-001 pp. 4-6 (`jama_flint_2019_oi_190079.pdf#page=4`).
- **Relationship:** Cox primary model; linear mixed models for continuous outcomes; overdispersed Poisson mixed-effects model for Simpson-Angus; two-sided testing and post hoc Holm adjustment.
- **Pass-1 result:** Models, populations, contrasts, and adjustment labels are explicitly supplied and distinguish the primary, secondary, and scale-score analyses. No incompatible printed result is identified.
- **Missing definition:** The printed material does not give covariance/variance-estimator details or simultaneous-CI construction; no unreported compatibility calculation is imposed.
- **Pass-2 result:** Cross-lane model, population, effect-measure, scale, and adjustment labels remain internally differentiated; the same named missing definitions still preclude an unsupported reconstruction.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S002 — Main-trial primary treatment hazard ratio

- **Mapper provenance:** MS002.
- **Direct source:** DOC-001 p. 1 and pp. 6-7 (`jama_flint_2019_oi_190079.pdf#page=1`, `#page=6`).
- **Relationship:** HR 0.25, 95% CI 0.13-0.48, P<.001, 126 randomized participants, olanzapine-plus-sertraline versus placebo-plus-sertraline for relapse.
- **Pass-1 result:** The estimate lies within ordered endpoints; direction agrees with the stated reduced relapse risk and the repeated abstract/result values. Diagnostic log-HR/endpoint calculation is compatible with P<.001 after display precision; it is not a replacement analysis.
- **Pass-2 result:** Containment, ordering, direction, 126-participant context, and matched repetitions remain compatible. No same-test variance, sidedness, or exact inferential definition is added.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S003 — Main-trial Cox covariate results

- **Mapper provenance:** MS003.
- **Direct source:** DOC-001 pp. 6-7 (`jama_flint_2019_oi_190079.pdf#page=6`).
- **Relationship:** Age, remission-status, and site HR/95% CI/P vectors from the primary Cox model.
- **Pass-1 result:** Every printed HR is contained by ordered CI endpoints; signs/directions agree with its reference contrast. Diagnostic log-scale interval/P comparisons are compatible at displayed precision. No supplied-source contradiction found.
- **Pass-2 result:** Cross-lane review retains containment, endpoint ordering, reference-direction labels, and compatible displayed repetitions; no unreported model variance or inferential convention is imposed.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S004 — Kaplan-Meier log-rank result

- **Mapper provenance:** MS004.
- **Direct source:** DOC-001 p. 7 (`jama_flint_2019_oi_190079.pdf#page=7`).
- **Relationship:** Figure 2 relapse-free survival comparison, log-rank P<.001, with plotted 95% CI bands.
- **Pass-1 result:** Direction agrees with the curve labels, relapse counts, and primary-model result. It is a distinct unadjusted comparison from S002, not a duplicate P value. The figure supplies no numeric band coordinates or test statistic, so no interval/test reconstruction is made.
- **Pass-2 result:** The log-rank comparison remains distinct from the adjusted Cox result, with curve/count direction compatible. No coordinates, statistic, or compatible calculation inputs are supplied.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S005 — Main-trial medication-discontinuer sensitivity analysis

- **Mapper provenance:** MS005.
- **Direct source:** DOC-001 p. 7 (`jama_flint_2019_oi_190079.pdf#page=7`).
- **Relationship:** Excluding 7 continuing-assessment medication discontinuers: HR 0.22, 95% CI 0.11-0.43, P<.001.
- **Pass-1 result:** Estimate containment, endpoint order, direction, and displayed P compatibility hold diagnostically. The analysis population is explicitly different from S002.
- **Pass-2 result:** HR 0.22 remains within the ordered 0.11-0.43 interval, with compatible direction and a distinct seven-person-exclusion population from S002.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S006 — Main-trial secondary treatment-by-time effects

- **Mapper provenance:** MS006.
- **Direct source:** DOC-001 p. 1 and p. 7 (`jama_flint_2019_oi_190079.pdf#page=1`, `#page=7`); Table 4 label context at p. 8.
- **Relationship:** Eight olanzapine-minus-placebo daily-rate estimates, 95% CIs, and Holm-adjusted P values from linear mixed models.
- **Pass-1 result:** All eight estimates are contained in ordered intervals. Direction and nominal interval crossing agree with the associated qualitative narrative. Exact CI/P reconstruction is not imposed because reported P values are Holm-adjusted while CI multiplicity construction is not specified. One measure-unit label conflict is proposed separately in statistical pass 1 (SP1-01).
- **Pass-2 result:** Containment, ordering, direction, and repeated values remain compatible. The HbA1c mg/dL-versus-percent conflict is retained as existing C001; Holm-adjusted P values are not forced to match uncharacterized CIs.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S007 — Simpson-Angus weekly-change result

- **Mapper provenance:** MS007.
- **Direct source:** DOC-001 p. 7 (`jama_flint_2019_oi_190079.pdf#page=7`), scale footnote at p. 6.
- **Relationship:** Weekly difference 0.022 points, 95% CI 0.009-0.036, Holm-adjusted P=.009.
- **Pass-1 result:** Containment, ordering, positive direction, and narrative agree. A Wald-style calculation from the rounded endpoints is only diagnostic because the source supplies a Poisson mixed model with overdispersion and an adjusted P, not the needed variance and adjustment sequence. The p. 4 general 0-40 instrument description and p. 6 0-36 analysis score explicitly differ by exclusion of the head-dropping item; no contradiction is inferred.
- **Pass-2 result:** Containment, ordering, direction, model/scale labels, and the explicit 0-40 versus 0-36 construction remain compatible; no exact P calculation is supported.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S008 — Table 4 within-arm change intervals

- **Mapper provenance:** MS008.
- **Direct source:** DOC-001 p. 8 (`jama_flint_2019_oi_190079.pdf#page=8`).
- **Relationship:** Sixteen unadjusted within-arm mean/median baseline-to-termination changes with 95% CIs.
- **Pass-1 result:** All displayed estimates are contained by ordered intervals. They are clearly distinct estimands from S006; the table warns that changes need not equal displayed termination minus baseline because of missing data. No P values, paired-data inputs, or test definitions are supplied.
- **Pass-2 result:** All 16 estimates remain contained in ordered intervals. The raw-change/missing-data caveat preserves their distinct estimand; paired inputs and test definitions remain absent.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S009 — Table 5 incident-high risk-difference intervals

- **Mapper provenance:** MS009.
- **Direct source:** DOC-001 p. 9 (`jama_flint_2019_oi_190079.pdf#page=9`).
- **Relationship:** Four absolute unadjusted percentage-point differences with 95% CIs (two marked exact).
- **Pass-1 result:** Each difference lies in ordered endpoints, directions agree with arm proportions, and all intervals include zero as described. Exact methods are named only for two rows; no unsupported test/P calculation is made.
- **Pass-2 result:** Interval containment/order and arm-proportion direction remain compatible. Existing C002 and C003 retain the two independently printed point-difference arithmetic conflicts; no unprinted denominator or method is assumed.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S010 — Missing-data and pattern-mixture inference

- **Mapper provenance:** MS010.
- **Direct source:** DOC-001 p. 5 (`jama_flint_2019_oi_190079.pdf#page=5`).
- **Relationship:** Missing-at-random mixed-model inference and pattern-mixture statement, including triglyceride exception.
- **Pass-1 result:** The text distinguishes the model assumption from the stated sensitivity result. No numerical inferential vector is supplied to reconcile.
- **Pass-2 result:** Cross-lane review finds no numerical vector, duplicate result, or contradictory label to reconcile; no missing model definition is inferred.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S011 — Medication-change sensitivity analyses

- **Mapper provenance:** MS011.
- **Direct source:** DOC-001 pp. 5 and 7 (`jama_flint_2019_oi_190079.pdf#page=5`).
- **Relationship:** Post hoc exclusion of pertinent values after medication starts/changes; qualitative similarity statement.
- **Pass-1 result:** The sensitivity-analysis definition and its qualitative conclusion are supplied, but no estimates, CIs, or P values are printed. No numerical compatibility claim is possible.
- **Pass-2 result:** Population definition and qualitative conclusion remain identifiable, but no estimate, interval, P value, or test statistic is supplied for compatibility checking.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S012 — Main-trial power relationship

- **Mapper provenance:** MS012.
- **Direct source:** DOC-001 p. 4 (`jama_flint_2019_oi_190079.pdf#page=4`).
- **Relationship:** Planned n=176, 80% power, 20% risk difference, up to 15% attrition; revised target n=128 after observed higher relapse risk.
- **Pass-1 result:** The change in target and its stated reason are coherent. Alpha, assumed control risk, allocation/attrition handling, and detailed calculation are absent, so the power claim is not reconstructed.
- **Pass-2 result:** The planned/revised targets and stated higher-relapse rationale remain coherent; alpha, control risk, allocation, attrition handling, and calculation details remain unavailable.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S013 — Main-trial multiplicity and interpretation rule

- **Mapper provenance:** MS013.
- **Direct source:** DOC-001 p. 6 (`jama_flint_2019_oi_190079.pdf#page=6`).
- **Relationship:** Two-sided overall 5% testing and post hoc Holm stepdown adjustment for multiple secondary outcomes.
- **Pass-1 result:** The adjustment label agrees with the secondary-result P labels. The source does not state whether CIs were adjusted, so exact P-to-CI equivalence is not required.
- **Pass-2 result:** Two-sided and post hoc Holm labels remain compatible with the secondary-result labels; Holm sequence and CI-adjustment construction remain unstated.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S014 — Aspirin meta-analysis definitions

- **Mapper provenance:** SS001.
- **Direct source:** DOC-002 p. 6; DOC-003 pp. 3-4 (`joi180151supp2_prod.pdf#page=3`).
- **Relationship:** Bayesian HR/95% CrI and frequentist Mantel-Haenszel RR/95% CI frameworks; risk/rate and ARD direction definitions.
- **Pass-1 result:** Effect measures, interval types, and risk-versus-rate labels are stated. The ARD prose defines direction but does not print a full numerical formula or variance derivation; no inferred formula is used to challenge rounded ARD values.
- **Pass-2 result:** Bayesian HR/CrI, frequentist RR/CI, ARD direction, and risk/rate labels remain differentiated; no unprinted ARD formula or variance derivation is imposed.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S015 — DIC and I2 model-selection matrix

- **Mapper provenance:** SS002.
- **Direct source:** DOC-003 pp. 4-6 (`joi180151supp2_prod.pdf#page=4`, `#page=5`, `#page=6`).
- **Relationship:** Forty-four fixed/random DIC comparisons, fixed-effect I2 values, and selected Bayesian model labels.
- **Pass-1 result:** Forty-three printed selections reconcile with the stated rule at displayed precision. The all-patient incident-cancer selection is proposed separately (SP1-02): its printed fixed DIC 27.06, random DIC 27.93, I2=25%, and selected `random` do not reproduce under the supplied rule for DIC differences within 3 and random selection only when I2>25%.
- **Pass-2 result:** All 44 rows were revisited. Forty-three remain reproducible; the Incident Cancer row remains existing C004 because displayed 25 is not greater than 25 under the printed strict rule, while the unrounded I2 is missing.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S016 — ARD/NNT/NNH and endpoint-scale matrix

- **Mapper provenance:** SS003.
- **Direct source:** DOC-003 pp. 4 and 15-18 (`joi180151supp2_prod.pdf#page=15`).
- **Relationship:** ARD intervals and conditional NNT/NNH presentation; event-rate, HR/CrI, and RR/CI scale distinctions.
- **Pass-1 result:** ARD sign labels, NNT/NNH display condition, and risk/rate/effect-measure labels are explicit. Rounded reciprocal checks are diagnostic only and do not yield a candidate; model-weighted risk and full-precision ARD are not supplied.
- **Pass-2 result:** ARD sign/intervals, conditional NNT/NNH display, and risk/rate/effect labels remain compatible; reciprocal calculations remain diagnostic only without full-precision model-weighted risks.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S017 — Egger small-study test

- **Mapper provenance:** SS004.
- **Direct source:** DOC-003 p. 21 (`joi180151supp2_prod.pdf#page=21`).
- **Relationship:** Egger estimate -0.47, SE 0.77, t=-0.59, P=.57.
- **Pass-1 result:** Diagnostic division of the rounded estimate by the rounded SE gives about -0.61, compatible with the printed t=-0.59 at finite precision. Degrees of freedom and a test-specific sidedness statement are absent; no exact P reconstruction is made.
- **Pass-2 result:** The mechanical recheck resolves the pass-1 diagnostic disagreement: conditional on the adjacent estimate and SE being t-test inputs, their nearest-hundredth intervals yield absolute ratios 0.600 through below 0.621 and cannot display as 0.59. Existing C005 is retained; the exact test/parameter definition, unrounded inputs, df, and sidedness remain absent, so no P reconstruction is made.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S018 — eTable 4 total-stroke HR/CrI results

- **Mapper provenance:** SS005.
- **Direct source:** DOC-003 p. 16 (`joi180151supp2_prod.pdf#page=16`).
- **Relationship:** All/low/high/diabetes HR (95% CrI), including diabetes upper endpoint 1.004 displayed as 1.00.
- **Pass-1 result:** Every HR is contained by ordered endpoints; directions match their contrasts. The explicit 1.004 footnote resolves the finite-precision `1.00` display and is not a candidate. Cross-location endpoint/population disagreement involving total stroke is proposed separately in SP1-03.
- **Pass-2 result:** Containment, ordering, direction, and the explicit 1.004 precision note remain compatible. The distinct total-stroke endpoint/population comparison remains existing C006.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S019 — Frequentist forest-plot RR/CI results

- **Mapper provenance:** SS006.
- **Direct source:** DOC-003 pp. 22-26 (`joi180151supp2_prod.pdf#page=22` through `#page=26`).
- **Relationship:** Outcome-level fixed/random RR/95% CI and heterogeneity summaries; individual-study rows including total-stroke ASCEND.
- **Pass-1 result:** Printed summary RRs lie inside ordered CIs and fixed/random labels, aspirin/no-aspirin direction, and heterogeneity labels are supplied. No Q statistic or degrees of freedom are supplied for exact heterogeneity P checks. The total-stroke ASCEND inclusion/matched-total issue is proposed separately in SP1-03.
- **Pass-2 result:** RR/CI containment, ordering, direction, and fixed/random labels remain compatible. The total-stroke ASCEND endpoint-membership/count issue remains existing C006; Q and df remain absent.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S020 — Bayesian sensitivity-analysis HR/CrI matrix

- **Mapper provenance:** SS007.
- **Direct source:** DOC-003 p. 18 (`joi180151supp2_prod.pdf#page=18`).
- **Relationship:** Eleven outcomes across four sensitivity definitions, HR (95% CrI), and analysis N/study counts.
- **Pass-1 result:** All point estimates are contained by ordered intervals. The MI <=100-mg endpoint printed as 1.00 is explicitly 0.9989 in the footnote and is not a display contradiction. No P values are printed for the CrI results.
- **Pass-2 result:** All estimates remain contained by ordered CrIs and retain their sensitivity-analysis labels. The explicit 0.9989 footnote resolves the 1.00 display; no P values are printed.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

### S021 — Total-stroke matched-source population/endpoint comparison

- **Mapper provenance:** SS008; direct companion labels in SN004 and SN008.
- **Direct source:** DOC-002 p. 7; DOC-003 pp. 9, 16, and 24 (`joi180151supp1_prod.pdf#page=7`, `joi180151supp2_prod.pdf#page=9`, `#page=16`, `#page=24`).
- **Relationship:** eTable 4 total stroke uses 12 studies and 73,883/72,317; the frequentist total-stroke forest plot has 13 rows and 81,623/80,057, including ASCEND 7,740/7,740. eTable 1 says ASCEND all stroke is not included because it reports ischaemic stroke only.
- **Pass-1 result:** The source locations and arithmetic difference (7,740 per arm) are directly reproducible. A matched endpoint convention explaining the forest-plot ASCEND row is not supplied in these source units. This is proposed separately in SP1-03.
- **Pass-2 result:** The exact 7,740-per-arm differences, 12-versus-13 study comparison, and duplicate ASCEND forest row remain reproducible. No frequentist total-stroke endpoint convention reconciling the all-stroke exclusion is supplied; existing C006 is retained.
- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE.

## Pass-1 coverage summary

- **Stable S IDs:** 21 (`S001`-`S021`), all `PASS_1_COMPLETE` and `PASS_2_COMPLETE`.
- **Unnumbered candidate proposals:** 3 (SP1-01 through SP1-03), all Pending Human Adjudication.
- **DISPLAY_ZERO_NOT_CANDIDATE records:** 0. No supplied result was printed as `P = 0`, `p = 0.000`, or an equivalent display zero.
- **Key limitations:** No exact P/CI reconstruction without supplied compatible inference definitions; no unrounded I2 beyond printed table; no endpoint-convention statement for ASCEND in the frequentist total-stroke forest plot; no Table 4 paired-data inputs; no full power-calculation inputs.
