# Statistical Consistency Pass 2

## Independent scope, evidence, and method

This fresh second statistical pass covered every canonical relationship explicitly assigned in `statistics/relationship_inventory.md`: S001-S022 and S501-S534 (56/56). It also revisited the entire cross-lane stable ledger C001-C012, the pass-1, numeric, and cross-source checker artifacts, and `verification/evidence_recheck.md`. The supplied PDFs remain the authority. Fresh native/layout extraction and result-page renderings were used to locate and visually verify printed fields; no old audit derivative, web source, raw data, or unstated model convention was used.

For frequentist Table 2 results, an interval/P-value diagnostic was made only where the source supplies a two-sided convention, a dependent-t-test label, a 95% CI label, and the relevant table-level or subgroup N. Such calculations use rounded fields and are diagnostic. Direct endpoint ordering and point-estimate containment checks do not depend on reconstructing an unreported model. Bayesian credible intervals, posterior probabilities, and the prospective protocol were retained in their supplied analysis/version contexts.

No observation in this pass is a finding, correction, severity assessment, or adjudication. Registered stable candidates remain **Pending Human Adjudication**. `STAT2` identifiers below are provisional distinct observations for the coordinator to register and mechanically recheck if appropriate; they are not C IDs.

## Newly identified provisional observations

### STAT2-001 — First handgrip-action-myotonia placebo-period interval is printed in reverse endpoint order and excludes its point estimate

- **Relationship:** S012.
- **Category:** Statistical reporting inconsistency.
- **Exact supplied-source location:** DOC-001, [PDF p. 7](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2, `Handgrip action myotonia, s`, `First attempt`, `Change Placebo Period, Mean (95% CI)`.
- **Direct observation:** The printed placebo-period change is `0.46 (−0.30 to −1.23)`. The first printed endpoint, `−0.30`, is greater than the second, `−1.23`; as printed, the point estimate `0.46` is also outside the displayed interval.
- **Rule:** A displayed 95% confidence interval must state endpoints from lower to upper and, for the displayed estimate from that same result, contain the point estimate. This is a direct display-order/containment check, not a recomputation of the dependent-t analysis.
- **Cross-lane/ledger result:** No C001-C012 record concerns these printed placebo-period values or this endpoint-order rule. This is distinct from C003 (the treatment-effect contrast header) and C010 (the SCN4A fifth-attempt treatment-effect CI/P fields).
- **Exact remaining human question:** Were the two placebo-period endpoints transposed, was one endpoint/sign transcribed incorrectly, or does a different printed estimate/interval belong in this row?

### STAT2-002 — Mean Timed Up&Go placebo-period point estimate is outside its displayed interval

- **Relationship:** S015.
- **Category:** Statistical reporting inconsistency.
- **Exact supplied-source location:** DOC-001, [PDF p. 7](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Table 2, `Timed Up&Go, s`, `Mean`, `Change Placebo Period, Mean (95% CI)`.
- **Direct observation:** The printed placebo-period change is `0.07 (−0.67 to 0.01)`. The endpoints are ordered, but the printed point estimate `0.07` exceeds the displayed upper endpoint `0.01`.
- **Rule:** A displayed 95% confidence interval must contain its corresponding displayed point estimate. This direct containment rule does not assume a degrees of freedom, covariance, variance estimator, or CI construction method.
- **Cross-lane/ledger result:** No C001-C012 record concerns this placebo-period mean/interval pair. It is distinct from C003, whose comparator is the separate treatment-effect header and effect column.
- **Exact remaining human question:** Does the point estimate require a sign/value correction, does the upper CI endpoint belong to another result, or did the source use a different unprinted pairing of estimate and interval?

## Relationship-level completion record

| ID | PASS_2_COMPLETE outcome | Cross-lane and recheck implications |
|---|---|---|
| S001 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Ordered/containing mixed-model CI and repeated result remain compatible; `P<.001` is not a display-zero issue. |
| S002 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Prior-RCT value has a distinct study context and is not a same-result comparator. |
| S003 | PASS_2_COMPLETE — REGISTERED_C008_REVISITED | Bayesian means are contained in ordered CrIs; the matched narrative `CLNC1` label issue is already C008. |
| S004 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Posterior probabilities and the stated .75 threshold remain coherent and are not P values. |
| S005 | PASS_2_COMPLETE — UNRESOLVED_DEFINITION | Order/period P values have no supplied statistic, SE, or row-level output for a compatible recalculation; no contradiction observed. |
| S006 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Each Mann-Whitney P remains attached to its matching Table 1 subgroup measure; no compatible statistic/interval is supplied. |
| S007 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Ordered/containing mixed-model CIs, signs, and narrative/Table repetitions reconcile. |
| S008 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Bayesian secondary means are contained in ordered CrIs and remain distinct from S007 frequentist effects. |
| S009 | PASS_2_COMPLETE — UNRESOLVED_DEFINITION | Mixed-model subgroup CIs contain estimates and signs/labels agree; CI/P diagnostic remains unsupported without its supplied df/variance/implementation linkage. |
| S010 | PASS_2_COMPLETE — REGISTERED_C003_AND_C009_REVISITED | Secondary-header sign conflict is C003; mental-component CI/P diagnostic is C009. No additional distinct field conflict found. |
| S011 | PASS_2_COMPLETE — REGISTERED_C003_REVISITED | INQoL treatment-effect sign follows the existing C003 header contradiction; its own estimate/CI/P diagnostic is otherwise compatible at printed precision. |
| S012 | PASS_2_COMPLETE — REGISTERED_C003_REVISITED; NEW_STAT2-001 | Existing C003 applies to the treatment-effect header. The separate first-attempt placebo-period CI order/containment defect is STAT2-001. |
| S013 | PASS_2_COMPLETE — REGISTERED_C003_AND_C010_REVISITED | Existing header issue C003 and SCN4A fifth-attempt CI/P/centering issue C010 remain distinct and source matched. |
| S014 | PASS_2_COMPLETE — REGISTERED_C003_REVISITED | Existing treatment-effect header issue only; printed effect/CI/P signs are otherwise compatible. |
| S015 | PASS_2_COMPLETE — REGISTERED_C003_REVISITED; NEW_STAT2-002 | Existing header issue C003 applies separately. The mean Timed Up&Go placebo point/CI containment failure is STAT2-002. |
| S016 | PASS_2_COMPLETE — REGISTERED_C003_REVISITED | Existing header issue only; all displayed treatment effects are contained in ordered CIs. |
| S017 | PASS_2_COMPLETE — REGISTERED_C003_REVISITED | Existing header issue only; force direction and displayed treatment-effect fields otherwise reconcile. |
| S018 | PASS_2_COMPLETE — REGISTERED_C003_REVISITED | Existing header issue only; transient-paresis treatment-effect fields otherwise reconcile. |
| S019 | PASS_2_COMPLETE — REGISTERED_C003_AND_C011_REVISITED | Direct PDF confirms SCN4A fifth-row `P=.02`, zero-crossing/off-center CI, and existing C011; C003 remains separate. |
| S020 | PASS_2_COMPLETE — REGISTERED_C003_REVISITED | Existing header issue only; mean-SCN4A `P=.28` agrees directionally with its zero-containing CI. |
| S021 | PASS_2_COMPLETE — REGISTERED_C003_AND_C012_REVISITED | Existing header issue C003 and EMG CI/P diagnostic C012 remain source matched and distinct. |
| S022 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Two-sided/exploratory conventions were applied; no P-value display zero is printed. |
| S501 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S502 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S503 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; 81%/continued is compatible with the printed strict threshold. |
| S504 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S505 | PASS_2_COMPLETE — UNRESOLVED_PRECISION | Printed 80%/continued may represent an unrounded value above the strict >80% rule; no contradiction is established. |
| S506 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S507 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S508 | PASS_2_COMPLETE — DISPLAY_ZERO_NOT_CANDIDATE | `0.00` is a Bayesian effect estimate, not a P value; its wide CrI and stated special-prior explanation are coherent. |
| S509 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S510 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; 2%/stopped agrees with the <20% rule. |
| S511 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S512 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S513 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S514 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S515 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S516 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; 99%/continued agrees with the rule. |
| S517 | PASS_2_COMPLETE — UNRESOLVED_PRECISION | Printed 80%/continued may reflect unrounded probability above strict >80%; no candidate. |
| S518 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S519 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; 1%/stopped agrees with the <20% rule. |
| S520 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S521 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S522 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S523 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S524 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S525 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S526 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S527 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Individual Bayesian mean is within its ordered CrI; threshold/action labels agree. |
| S528 | PASS_2_COMPLETE — UNRESOLVED_PRECISION | `4+23=27` reconciles. The printed 80% continuation records are not candidates without unrounded probabilities; special patient-11 context is supplied. |
| S529 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | Group posterior areas, N=27, .75 threshold, outcome labels, and placebo-minus-mexiletine direction agree with main results. |
| S530 | PASS_2_COMPLETE — REGISTERED_C005_AND_C007_REVISITED | Code/prose treatment-label swap is C005 and `sigma.mex` period-label conflict is C007; no additional code/result contradiction found. |
| S531 | PASS_2_COMPLETE — REGISTERED_C005_C006_AND_C007_REVISITED | Existing individual-label swap C005, `diff_CLCN1` subgroup-label conflict C006, and `sigma.mex` label conflict C007 remain distinct. |
| S532 | PASS_2_COMPLETE — DISPLAY_ZERO_NOT_CANDIDATE | `0/1,000=0.00` is a simulated type-I-error frequency, not a P-value display; no display-zero P candidate exists. |
| S533 | PASS_2_COMPLETE — NO_NEW_OBSERVATION | `685/1,000=68.5%`, `315+685=1,000`, and `1.29-1.75=-.46` reconcile in the stated simulation context. |
| S534 | PASS_2_COMPLETE — UNRESOLVED_VERSION_CONTEXT | Protocol `>=80%`/`<=20%` wording is prospective and version-contextual; it is not a matched observed-result contradiction with the published strict wording. |

## Stable-ledger cross-lane audit

| Stable ID | Pass-2 result |
|---|---|
| C001 | Already registered; enrolled denominator/count/percentage comparison is mechanically rechecked and has no additional S-specific implication. |
| C002 | Already registered; the INQoL scale-bound observation is distinct from inference checks in S011. |
| C003 | Already registered; applies to the separate Table 2 treatment-effect header across S010-S021. It does not explain STAT2-001 or STAT2-002, which concern placebo-period fields. |
| C004 | Already registered; adverse-reaction denominator/rounding issue remains outside a supplied inferential relationship. |
| C005 | Already registered; code/prose treatment mapping conflict is reconfirmed for S530-S531. |
| C006 | Already registered; code/prose genotype-label conflict is reconfirmed for S531. |
| C007 | Already registered; code/dictionary `sigma.mex` treatment-period conflict is reconfirmed for S530-S531. |
| C008 | Already registered; `CLNC1`/`CLCN1` label conflict is reconfirmed as a matched subgroup-label issue relevant to S003. |
| C009 | Already registered; S010 rounded dependent-t diagnostic remains conditional on table N=27/df=26 and its source fields remain unmatched. |
| C010 | Already registered; S013 SCN4A fifth-row zero-crossing/off-center CI and `.009` remain distinct from the interaction P value. |
| C011 | Already registered; S019 direct PDF confirms `13.71 (−1.96 to 25.47), P=.02`; existing CI/estimate/P incompatibility remains. |
| C012 | Already registered; S021 rounded dependent-t CI/P diagnostic remains conditional on table N=27/df=26 and its source fields remain unmatched. |

## Limitations and exclusions

- The package supplies no row-specific complete-pair counts, paired-difference data, SEs, covariance matrices, unrounded inferential output, or mixed-model CI/P implementation. Those missing definitions were not inferred from convention.
- C009-C012 remain direct printed-field mismatches with diagnostics conditional on the table-level/group N and dependent-t description; the direct interval ordering/containment observations STAT2-001 and STAT2-002 need no such diagnostic assumption.
- The prospective protocol was not treated as a same-version numerical result source. Bayesian credible intervals/posterior probabilities were not treated as frequentist P values.
- No coherent `P=0`, `p=0.000`, or equivalent display-zero P result was found. S508's `0.00` is an estimate and S532's `0.00` is a simulation frequency; neither is a P-value candidate.

## Pass summary

- **Assigned/completed relationships:** 56/56: S001-S022 and S501-S534, each with an explicit `PASS_2_COMPLETE` outcome.
- **Stable-ledger audit:** 12/12: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, and C012 all revisited.
- **New distinct provisional observations:** 2: `STAT2-001` (S012) and `STAT2-002` (S015). Neither has a matching existing C ID; both require coordinator registration and mechanical evidence recheck before any report-card inclusion.
- **Display-zero P-value-only observations:** 0.
