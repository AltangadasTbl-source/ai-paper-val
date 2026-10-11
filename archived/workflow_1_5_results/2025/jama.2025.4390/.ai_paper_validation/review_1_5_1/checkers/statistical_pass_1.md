# Statistical Consistency Review — Pass 1

## Execution and scope

- **Pass:** 1 of 2; independent statistical consistency review.
- **Assigned scope:** every stable inferential relationship `S001` through `S035` in `statistics/relationship_inventory.md`.
- **Evidence used:** current direct PDFs and fresh-source maps only: `extraction/main_quantitative_evidence.md`, `extraction/support_quantitative_evidence.md`, and their named fresh direct-extraction parts. Targeted direct confirmation used current DOC-001 PDF pp. 1, 6-9; DOC-004 PDF pp. 33, 37, and 49; and the current DOC-002/DOC-003 evidence extracts for protocol and SAP definitions. No legacy candidate, checker, verifier, quality, or report artifact was used.
- **Checks applied where source definitions permitted:** point-estimate containment and CI ordering; direction/sign and treatment-reference consistency; outcome/measure/scale labels; repetitions across the main paper and supplements; count and denominator implications; and diagnostic compatibility of confidence intervals and P values. A test statistic, sidedness, CI construction, covariance, variance estimator, or adjusted-model definition was not inferred when it was not expressly supplied.
- **P-value display-zero handling:** no assigned relationship prints `P = 0`, `p = 0.000`, or an equivalent display zero. Printed values such as `P < .001` were not treated as display-zero candidates.

## Candidate proposals for coordinator registration

These are proposals, not stable candidate IDs, dispositions, severity ratings, corrections, or adjudications. Each requires mechanical recheck against the stated source locations before any ledger registration.

### P1-STAT-01 — Figure 3 primary-event rate column conflicts with the matched Table 2 rate definition

- **Proposed category:** Measure, label, or scale inconsistency (with rate-versus-count implications).
- **Exact source locations:** DOC-001, `jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8`, Table 2 composite primary-outcome row; and `jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9`, Figure 3 all-patients row and column header.
- **Direct observation:** Table 2 identifies the composite primary outcome as 163 bedtime events and 173 morning events, with a column headed `Rate per 100 patient-years` showing **2.30** and **2.44**, respectively. Figure 3 names the same composite primary outcome and heads its corresponding columns `Rate per 100 patient-years`, yet its all-patients row prints **71.0** for bedtime and **71.0** for morning, alongside the matched 163 and 173 event counts and HR 0.96 (95% CI 0.77-1.19). The Figure 3 subgroup values partition to 71.0 within several mutually exhaustive characteristics (for example male 30.5 plus female 40.5), which does not resolve the printed rate-unit conflict.
- **Consistency rule and calculation:** for the same outcome, allocation groups, and stated rate unit, a cross-location repetition should retain the rate measure or identify a different denominator/scale. The supplied Figure 3 caption supplies the same composite-outcome and allocation context but no alternate time-at-risk denominator or alternate rate scale. The direct comparison is `Figure 3: 71.0/71.0 per 100 patient-years` versus `Table 2: 2.30/2.44 per 100 patient-years`.
- **Alternative source-grounded interpretation / human question:** the Figure 3 values may represent a different, unstated quantity rather than event rates, or a figure-column label/value may be wrong. Confirm the intended Figure 3 rate calculation and denominator from the analysis output; do not assume the intended correction.

### P1-STAT-02 — eTable 5 “Other” ethnicity row duplicates White/Caucasian values and exceeds the matched randomized-category totals

- **Proposed category:** Numeric or arithmetic inconsistency.
- **Exact source locations:** DOC-004, `joi250019supp3_prod_1749674951.30054.pdf#page=37`, eTable 5 ethnicity rows; and DOC-004 `...pdf#page=29`, eTable 3 randomized baseline ethnicity rows (continued table spans pp. 29-32).
- **Direct observation:** eTable 5 states its comparison is Morning Allocation `n=44` versus Bedtime Allocation `n=57`. Under ethnicity it prints White/Caucasian as **40 (90.9%)** and **53 (93.0%)**, then prints its separate `Other` row as the identical **40 (90.9%)** and **53 (93.0%)**. The fresh eTable 3 map records the randomized-baseline `Other` totals as **5 morning** and **9 bedtime** (the map’s source-order triplet is bedtime 9; morning 5; overall 14).
- **Consistency rule and calculation:** eTable 5’s displayed `Other` counts cannot exceed the corresponding full randomized-baseline `Other` counts for the same allocation and baseline label: morning `40 > 5`; bedtime `53 > 9`. The duplicated eTable 5 values also exactly reproduce the immediately preceding White/Caucasian row. Independently, its printed ethnicity entries including the repeated row cannot be reconciled to the stated allocation denominators without an unstated overlapping-category rule; eTable 3’s category totals form the stated randomized partition.
- **Alternative source-grounded interpretation / human question:** likely repeated values or a mislabeled/misplaced row, but the source does not identify the intended `Other` counts. Confirm the eTable 5 source dataset and whether the category label or values were transposed; do not infer replacement values from the randomized baseline table.

## Relationship-by-relationship records

### S001 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 1 abstract gives 2.3 versus 2.4 events per 100 patient-years and adjusted HR 0.96 (95% CI 0.77-1.19), P=.70. The HR lies within its correctly ordered CI and direction is compatible with the stated bedtime-versus-morning comparison. It repeats in S005/S007/S010. No source-defined Cox test/CI construction was supplied for a strict P-value reconstruction; a Wald-style approximation is diagnostic only. **Outcome:** no separate candidate proposal.

### S002 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 3 reports 80% power, two-sided alpha .05, HR <=.75, 379 events, and a 7% inflation to 406. Arithmetic check: `379 x 1.07 = 405.53`, which rounds to 406. This is a planning relationship, not a final-effect estimate. **Outcome:** no candidate proposal.

### S003 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 3 reports 155 outcomes at the interim review and stopping-consideration thresholds P<=.001 for benefit and P<=.05 for harm. This is a monitoring rule; no observed interim effect or test statistic is supplied for compatibility testing. The version-specific 200-event protocol plan is addressed in S026. **Outcome:** no candidate proposal; missing information for further inference is the interim analysis statistic/model and revised monitoring specification.

### S004 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 4 explicitly distinguishes ITT/as-randomized Cox for primary/survival analyses, Cox or Poisson for most other outcomes, available-data non-survival analyses, and two-sided P<.05. These labels align with Table 2 HR/RR footnotes and the SAP model assignments reviewed in S029. **Outcome:** no candidate proposal.

### S005 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 6 repeats the primary adjusted HR 0.96 (0.77-1.19), P=.70 and unadjusted HR 0.94 (0.76-1.17), with rates 2.3/2.4. Both estimates are positive, within ordered CIs, and directions/contrast are coherent. The adjusted result matches abstract/Table 2/Figure 2. **Outcome:** no separate candidate proposal.

### S006 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 6 per-protocol sensitivity reports n=1042/1023, rates 1.7/1.8, unadjusted HR 0.94 (0.68-1.28), adjusted HR 0.90 (0.65-1.23), P=.50. Both HRs are contained in ordered CIs and below one in the displayed bedtime-versus-morning direction. Its population differs from ITT by stated exclusions, so it is not compared as an identical result. Strict P reconstruction is unavailable because the reported P-to-estimate/model linkage is not specified. **Outcome:** no candidate proposal.

### S007 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 7 Figure 2 prints adjusted HR 0.96 (0.77-1.19), unadjusted HR 0.94 (0.76-1.17), and the adjusted covariate list. Values and contrast repeat S005/Table 2 consistently. The listed covariates match the later SAP primary analysis plan (S029); the earlier protocol’s original covariate list is version-specific (S027) and does not establish a matched-result contradiction. **Outcome:** no candidate proposal.

### S008 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 7 and DOC-004 p. 49 repeat the ABPM means, differences, CIs, and P values. Each difference is inside its ordered CI; signed bedtime-minus-morning differences agree with the displayed group means within shown-mean rounding (including sleep DBP, where -2.7 may reflect unrounded means). CI exclusion of zero is directionally compatible with P<.001 or P=.02; intervals spanning zero are compatible with P=.15/.72. The source does not give the linear-model/variance/CI construction needed for an exact recalculation. **Outcome:** no candidate proposal.

### S009 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 7 reports EQ-5D-5L means 78.9/79.5, difference -0.75 (95% CI -1.69 to 0.19), P=.12. The estimate is contained in its ordered CI and the interval spans zero, compatible with the nonsignificant P. The displayed rounded group-mean difference (-0.6) is not treated as a contradiction because the SAP specifies a multiple-linear-regression analysis for overall health and the source does not state whether this printed difference is adjusted or its exact calculation. **Outcome:** no candidate proposal; required definition for a stricter comparison is the reported-difference estimand/model specification.

### S010 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 8 Table 2 primary row gives HR 0.96 (0.77-1.19), P=.70, and rates 2.30/2.44. CI ordering/containment and direction are coherent; this is the exact-precision source for S001/S005/S007. **Outcome:** no separate candidate proposal.

### S011 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 8 component HRs (mortality, stroke, MI/ACS, and heart failure) each lie within ordered CIs: 0.90 (0.67-1.22), 0.86 (0.52-1.44), 1.25 (0.82-1.91), and 0.72 (0.45-1.15). The displayed rate differences have the same directional orientation as treatment-minus-control rates. All intervals include one and corresponding P values .50/.57/.30/.17 exceed .05. **Outcome:** no candidate proposal.

### S012 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 8 gives HR 0.93 (0.85-1.02), P=.10, and 23.26 versus 25.15 events/100 patient-years, difference -1.89. The point estimate is inside an ordered CI including one; rate-difference sign agrees with the printed rates. **Outcome:** no candidate proposal.

### S013 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 8 fracture HRs 0.92 (0.74-1.14), P=.44 and 0.65 (0.37-1.15), P=.14 are point-contained with ordered, one-spanning CIs. Rate-difference signs agree with the displayed group rates. **Outcome:** no candidate proposal.

### S014 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 8 identifies falling, syncope, and lightheadedness as Poisson/RR outcomes and reports RRs 0.96 (0.86-1.07), 1.28 (0.93-1.75), and 0.95 (0.90-1.00), with P=.47/.12/.06. All estimates are point-contained and CIs are ordered; directions are compatible with the displayed interview-percentage means. Exact P/CI reconstruction is not performed because the regression/robust-variance specification is not supplied. **Outcome:** no candidate proposal.

### S015 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 8 gives glaucoma HR 1.13 (0.73-1.74), P=.58 and subjective-vision RR 1.02 (0.89-1.17), P=.74. Both effect labels match the Table 2 footnote/model assignment; point containment, endpoint order, and direction agree with the displayed treatment/control values. **Outcome:** no candidate proposal.

### S016 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 8 reports cognitive-decline RR 0.98 (0.85-1.13), P=.82; dementia-consistent impairment RR 1.12 (0.83-1.51), P=.48; and nursing-home HR 1.38 (0.83-2.27), P=.21. All points are contained in ordered CIs spanning one. Count/percentage directions are compatible with RR directions; the nursing-home rate difference is positive with HR above one. **Outcome:** no candidate proposal.

### S017 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 9 Figure 3 HRs for all patients, sex, and age strata are point-contained in ordered CIs and use the stated unadjusted HR scale. Interaction P values derive from a specified interaction Cox framework, but cannot be reconstructed from stratum CIs because covariance/test details are not supplied. The all-patients Figure 3 rate values create proposal P1-STAT-01; no independent effect-estimate/CI inconsistency was found.

### S018 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 9 frailty, polypharmacy, and health-score subgroup HRs are positive and contained in ordered CIs; interaction P=.22/.49/.14 is labelled as interaction rather than subgroup-effect P. Figure rate values for complementary subgroups sum to the Figure’s displayed all-patient 71.0 values, but their unit issue is captured once in P1-STAT-01 rather than duplicated. **Outcome:** no separate candidate proposal.

### S019 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 9 resistant-hypertension, heart-failure, and diabetes HRs are point-contained in ordered CIs, and interactions are labelled P=.07/.16/.05. The supplied interaction-model description does not establish an exact test calculation. **Outcome:** no separate candidate proposal.

### S020 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 9 CAD, stroke/TIA, and sleep-apnea subgroup HRs are point-contained in ordered CIs; interaction P=.93/.57/.54 is correctly placed as a characteristic-level interaction. **Outcome:** no separate candidate proposal.

### S021 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 9 CKD and sedentary subgroup HRs are point-contained in ordered CIs; interaction P=.97/.69 is labelled as such. No source supplies enough covariance/variance detail to calculate these interaction P values independently. **Outcome:** no separate candidate proposal.

### S022 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 9 ACE-inhibitor, ARB, and beta-blocker subgroup HRs are point-contained in ordered CIs; interaction P=.05/.44/.54 is a separate treatment-by-characteristic test. Subgroup CIs do not license inference of interaction compatibility without the joint model outputs. **Outcome:** no separate candidate proposal.

### S023 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 9 CCB, diuretic, and combination-medicine subgroup HRs are point-contained in ordered CIs; interaction P=.66/.43/.72 is correctly labelled. The table’s event-rate column issue remains the single proposal P1-STAT-01. **Outcome:** no separate candidate proposal.

### S024 — PASS_1_COMPLETE

**Evidence and checks:** DOC-001 p. 10 states that the primary CI excludes HR <=.76 and the planning threshold was HR <=.75. The reported lower endpoint .77 supports both statements at displayed precision. MAPEC/Hygia comparison CIs are not printed in the supplied main paper, so their asserted nonoverlap cannot be mechanically evaluated. **Outcome:** no candidate proposal; missing comparator CIs are recorded as an evidence limitation, not a finding.

### S025 — PASS_1_COMPLETE

**Evidence and checks:** DOC-002 p. 3 original protocol power relationship (80%, alpha .05, 25% reduction, 379 plus 7%=406 events) matches S002 as a version-matched planning statement. `379 x 1.07 = 405.53`, supporting displayed rounding to 406. **Outcome:** no candidate proposal.

### S026 — PASS_1_COMPLETE

**Evidence and checks:** DOC-002 p. 4 original protocol sets the 200-event DSMB review and P<=.001 benefit/P<=.05 harm rules. Main-paper S003 reports an actual review with 155 outcomes after documented recruitment/event-target changes. The supplied sources distinguish original plan from later conduct and do not supply a matched revised trigger that would establish a contradiction. **Outcome:** no candidate proposal; missing information for a stricter comparison is the finalized revised DSMB analysis specification.

### S027 — PASS_1_COMPLETE

**Evidence and checks:** DOC-002 p. 4 gives the original Cox covariate set. The later SAP’s primary Cox list and Figure 2 list differ in form/contents, but the SAP is a later prespecified analysis document and supplies the Figure 2 covariate framework. The package does not identify the original protocol list as the immutable final-model list. **Outcome:** no candidate proposal; document-version evolution is a source-grounded alternative explanation.

### S028 — PASS_1_COMPLETE

**Evidence and checks:** DOC-002 p. 13 letter-substudy statement reports target 2 percentage-point response difference, alpha .05, and 80% power. It gives no observed recruitment-substudy effect/test output for compatibility checking. **Outcome:** no candidate proposal; missing observed-statistic/model details are not a contradiction.

### S029 — PASS_1_COMPLETE

**Evidence and checks:** DOC-003 pp. 4-6 SAP specifies Cox, Poisson, multiple linear regression, Mann-Whitney/t, and Fisher assignments by outcome. These assignments match the main article’s broad statistical-analysis statement and Table 2 HR/RR footnote. SAP primary Cox covariates align with Figure 2. **Outcome:** no candidate proposal.

### S030 — PASS_1_COMPLETE

**Evidence and checks:** DOC-003 p. 4 specifies the one-covariate-per-10-events or per-20-randomized-continuous-participants rule and no stepwise selection. This is a planning/model-constraint statement; the record contains no fully enumerated model-event accounting that would support a concrete incompatibility candidate. **Outcome:** no candidate proposal; no inference about unreported model selection was made.

### S031 — PASS_1_COMPLETE

**Evidence and checks:** DOC-003 p. 6 defines the subgroup set and Fisher-exact withdrawal/loss sensitivity framework. It matches the topics appearing in Figure 3/eTables while preserving distinct populations and test purposes. No result labelled as the Fisher sensitivity test is supplied for a strict cross-check. **Outcome:** no candidate proposal.

### S032 — PASS_1_COMPLETE

**Evidence and checks:** DOC-004 pp. 20-21 describes reduced Cox models, covariate imputation/replacement, and a 1000-simulated-pattern PH check with no violation. This framework is compatible with the article’s no-PH-violation statement. Simulation output, diagnostics, and exact model parameters are not printed, so they cannot be independently recalculated. **Outcome:** no candidate proposal.

### S033 — PASS_1_COMPLETE

**Evidence and checks:** DOC-004 pp. 33-36 eTable 4 gives unadjusted baseline-comparison P values for completed/death n=2726 versus withdrew/lost n=631. Direct p. 33 checks show count/percentage values consistent with their displayed denominators after normal rounding and total groups sum to 3357. The source calls values unadjusted but does not specify the row-specific test or exact calculation, so no strict P reconstruction was assumed. **Outcome:** no candidate proposal.

### S034 — PASS_1_COMPLETE

**Evidence and checks:** DOC-004 pp. 37-40 eTable 5 provides baseline-comparison P values for Morning n=44 versus Bedtime n=57. Direct p. 37 confirmation found the duplicated `Other` ethnicity values and their contradiction with eTable 3 randomized baseline category totals; this is proposal P1-STAT-02. Apart from that proposed table-value inconsistency, point/denominator and printed P-value assessment is limited because row-specific tests are not specified. No P-value display-zero issue occurs.

### S035 — PASS_1_COMPLETE

**Evidence and checks:** DOC-004 p. 49 eTable 9 repeats the ABPM relationships in S008, including N=151/151, treatment-minus-control mean-difference scale, all CIs, and P values. Direct table confirmation finds all points inside ordered CIs and direction/P relationships qualitatively coherent. The source does not state the exact inferential procedure, so exact P/CI reconstruction is diagnostic-only and unnecessary for the observed check. **Outcome:** no candidate proposal.

## Pass-1 totals and limitations

- **Relationships completed:** 35/35 (`S001`-`S035`), each explicitly marked `PASS_1_COMPLETE` above.
- **Candidate proposals emitted:** 2 distinct proposals (`P1-STAT-01`, `P1-STAT-02`); neither has a stable `C` ID and both remain Pending Human Adjudication if registered by the coordinator.
- **Display-zero-only candidates:** 0.
- **Limitations:** The supplied PDFs do not provide enough information to reproduce exact Cox/Poisson/linear-model P values or CIs in many relationships (for example, variance estimator, CI/test construction, covariance, and full adjusted-model output). Those absent definitions were not inferred. Figure 3 subgroup interaction P values cannot be derived from separate subgroup CIs. DOC-003 native text has defective embedded encoding; this pass relied on its fresh visual-confirmed mapper transcription and current direct-source provenance for SAP content.
