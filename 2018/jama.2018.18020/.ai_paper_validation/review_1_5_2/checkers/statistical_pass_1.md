# Statistical Consistency Pass 1

## Execution scope and method

Independent pass-1 review of all 56 canonical relationships: S001-S022 and S501-S534. Direct supplied PDFs and the current fresh native/layout assets were checked; earlier audit outputs and the web were not used. A result was only mechanically recomputed when the source supplied a compatible test, confidence level, sidedness, effect, and population. Approximate calculations below use rounded printed values and are diagnostics, not replacements for the reported analyses.

The main article states that P values are two-sided. Table 2 states that IVR outcomes use a linear mixed model and other secondary outcomes use dependent t tests. For total-group dependent-t rows, the Table 2 heading gives N=27; for subgroup rows, the footnote gives CLCN1 n=16 and SCN4A n=11. These supplied facts support the specific t/CI diagnostics reported below. No source printed a P-value display zero; the `0.00` in S532 is a simulated type-I-error rate, not a P value.

## Candidate consistency observations forwarded for registration

These are provisional `STAT1` observations only. They are not C IDs, severity labels, corrections, or adjudications; each requires human adjudication after ledger merge and mechanical recheck.

### STAT1-001 — Table 2 secondary-outcome contrast header conflicts with displayed effect direction

- **Relationships:** S010-S021 (the non-IVR secondary-outcome section of Table 2).
- **Exact evidence:** `jama_stunnenberg_2018_oi_180136.pdf#page=7`, Table 2, column header `Treatment Effect (Placebo-Mexiletine), Mean (95% CI)`; values on pp. 7-8.
- **Direct observation:** The printed effects follow mexiletine minus placebo, not the printed `Placebo-Mexiletine` header. Examples using printed period changes: INQoL: `-21.44 - (-7.22) = -14.22`, the reported effect; handgrip first attempt: `-2.39 - 0.46 = -2.85`, the reported effect; SF-36 physical: `8.66 - 1.04 = 7.62`, directionally matching the reported `7.81` (the small magnitude difference is compatible with unrounded paired data). Conversely, placebo minus mexiletine reverses each displayed sign.
- **Rule:** A stated treatment-effect contrast must agree with the direction of the period values and its own effect column. This is a label/scale inconsistency, not an inference about clinical validity.
- **Human question:** Was the header intended to be `Mexiletine-Placebo`, or do the reported effects use an undocumented sign convention?

### STAT1-002 — SF-36 mental-component P value is not compatible with its printed dependent-t 95% CI under the supplied total-group definition

- **Relationship:** S010.
- **Exact evidence:** `jama_stunnenberg_2018_oi_180136.pdf#page=7`, Table 2: effect `6.78`, 95% CI `1.64 to 11.92`, `P=.001`; Table 2 heading `N=27`; Methods PDF p.3 and Table 2 footnote identify two-sided dependent t tests for non-IVR secondary outcomes.
- **Diagnostic calculation:** With df=26, `t_(0.975,26)≈2.056`; CI half-width `(11.92-1.64)/2=5.14` gives `SE≈5.14/2.056=2.50`, hence `t≈6.78/2.50=2.71` and two-sided `P≈.012`. Printed rounding cannot bridge this to `.001`.
- **Rule:** The supplied dependent-t test, 95% CI, two-sided P convention, and total-group N define a compatible result set.
- **Human question:** Which of the printed P value, interval, total analyzed paired sample, or inferential procedure is the intended one?

### STAT1-003 — SCN4A fifth handgrip-action-myotonia P value conflicts with its 95% CI

- **Relationship:** S013.
- **Exact evidence:** `jama_stunnenberg_2018_oi_180136.pdf#page=7`, Table 2: SCN4A effect `-1.96`, 95% CI `-3.41 to 0.51`, `P=.009`; Table 2 footnote supplies dependent t test and SCN4A `n=11`; Methods supplies two-sided P values.
- **Diagnostic calculation:** With df=10, `t_(0.975,10)≈2.228`; CI half-width `1.96` gives `SE≈.880`, `|t|≈2.23`, and two-sided `P≈.05`. The printed 95% CI crosses zero while the printed two-sided P is `.009`.
- **Rule:** For the supplied paired-t framework, a 95% CI and two-sided P describe the same reported effect.
- **Human question:** Does the row contain a P-value, CI-endpoint, subgroup-N, or test-label transcription error?

### STAT1-004 — SCN4A fifth transient-paresis P value conflicts with its 95% CI

- **Relationship:** S019.
- **Exact evidence:** `jama_stunnenberg_2018_oi_180136.pdf#page=7`, Table 2: SCN4A effect `13.71`, 95% CI `-1.96 to 25.47`, `P=.02`; Table 2 footnote supplies dependent t test and SCN4A `n=11`; Methods supplies two-sided P values.
- **Diagnostic calculation:** With df=10, interval half-width `13.715` gives `SE≈6.16`, `t≈2.23`, and two-sided `P≈.05`; the printed 95% CI crosses zero while `P=.02` is below .05.
- **Rule:** Same as STAT1-003.
- **Human question:** Does the row contain a P-value, CI-endpoint, subgroup-N, or test-label transcription error?
- **Fresh-asset correction for coordinator:** The supplied PDF prints `P=.02` in this S019 row. The current fresh main evidence map assigns `.28` to S019; `.28` belongs to the later mean transient-paresis SCN4A row (S020). That derivative mismatch is not itself a supplied-source candidate.

### STAT1-005 — Myotonic-discharge P value is not compatible with its printed dependent-t 95% CI under the supplied total-group definition

- **Relationship:** S021.
- **Exact evidence:** `jama_stunnenberg_2018_oi_180136.pdf#page=8`, Table 2 continuation: effect `.67`, 95% CI `.23 to 1.11`, `P<.001`; Table 2 heading `N=27`; Methods PDF p.3 and the Table 2 footnote identify two-sided dependent t tests.
- **Diagnostic calculation:** With df=26, CI half-width `.44` gives `SE≈.214`, `t≈3.13`, and two-sided `P≈.004`. This remains above .001 after reasonable rounding of the printed endpoints.
- **Rule:** Same supplied paired-t/95%-CI/two-sided-P relationship as STAT1-002.
- **Human question:** Which reported inferential field (P value, interval, sample used, or test implementation) is intended?

### STAT1-006 — Bayesian total and genotype model parameter definitions reverse the treatment labels used by their code

- **Relationships:** S530 and S531.
- **Exact evidence:** `joi180136supp2_prod.pdf#page=11`, eMethods 2; `joi180136supp2_prod.pdf#page=13`, eMethods 3. In both code blocks, `Stiff_Plac` is modeled using `mu_plac` and `Stiff_Mex` using `mu_mex`, but the subsequent parameter-definition text describes `mu_mex[i]` as placebo and `mu_plac[i]` as mexiletine.
- **Rule:** A parameter label must agree with the code’s data-to-parameter mapping and the accompanying `diff = mu.plac - mu.mex` contrast.
- **Human question:** Are the two prose parameter definitions transposed, and which label should downstream extractors apply?

### STAT1-007 — Genotype-model `diff_CLCN1` prose definition names the wrong subgroup

- **Relationship:** S531.
- **Exact evidence:** `joi180136supp2_prod.pdf#page=14`, eMethods 3. Code defines `diff_CLCN1 <- mu.plac_CLCN1 - mu.mex_CLCN1`, whereas the parameter-definition text says `diff_CLCN1 ... for SCN4A patients`.
- **Rule:** A parameter’s label must agree with its code-defined genotype contrast.
- **Human question:** Is this a prose-label transposition only, or is there a separate reportable mapping that should be used for the CLCN1 subgroup?

## Relationship-level completion record

| ID | PASS_1_COMPLETE outcome | Notes / candidate linkage |
|---|---|---|
| S001 | PASS_1_COMPLETE — NO_ISSUE | Estimate lies inside ordered 95% CI; repeated locations, positive Pbo-minus-Mx direction, and `P<.001` are compatible. |
| S002 | PASS_1_COMPLETE — NO_ISSUE | Prior-RCT estimate is contained in ordered CI; distinct study is not equated to current trial. |
| S003 | PASS_1_COMPLETE — NO_ISSUE | All total/subgroup Bayesian means lie within ordered CrIs; subgroup sizes and positive Pbo-minus-Mx direction match. |
| S004 | PASS_1_COMPLETE — NO_ISSUE | Posterior probabilities use the stated `.75` threshold and are not P values. |
| S005 | PASS_1_COMPLETE — UNRESOLVED_DEFINITION | Order/period P values have source model context but no statistic/SE/df for mechanical recalculation; no contradiction observed. |
| S006 | PASS_1_COMPLETE — NO_ISSUE | Each Mann-Whitney P value is paired to its Table 1 subgroup row; no interval/test statistic is supplied for further compatibility testing. |
| S007 | PASS_1_COMPLETE — NO_ISSUE | Effects are within ordered CIs and narrative/Table values agree; supplied linear-mixed-model labels and direction agree. |
| S008 | PASS_1_COMPLETE — NO_ISSUE | Bayesian means are within ordered CrIs; no conflation with frequentist S007. |
| S009 | PASS_1_COMPLETE — UNRESOLVED_DEFINITION | Intervals contain effects and sign/interaction labels agree. A rounded CI/P diagnostic for the SCN4A mixed-model row is not registered because the source does not define its CI/P degrees-of-freedom or implementation linkage. |
| S010 | PASS_1_COMPLETE — OBSERVATIONS | STAT1-001 (contrast header) and STAT1-002 (mental-component P/CI). Physical-component fields otherwise compatible. |
| S011 | PASS_1_COMPLETE — OBSERVATION | STAT1-001. INQoL effect/CI/P are otherwise compatible with its scale and paired-t diagnostic. |
| S012 | PASS_1_COMPLETE — OBSERVATION | STAT1-001. Total-group handgrip rows have ordered/containing CIs and compatible P diagnostics. |
| S013 | PASS_1_COMPLETE — OBSERVATIONS | STAT1-001 and STAT1-003; interaction is kept distinct from subgroup P values. |
| S014 | PASS_1_COMPLETE — OBSERVATION | STAT1-001; effect/CI/P signs and paired-t diagnostics otherwise agree. |
| S015 | PASS_1_COMPLETE — OBSERVATION | STAT1-001; time-direction, effect/CI/P consistency otherwise agree. |
| S016 | PASS_1_COMPLETE — OBSERVATION | STAT1-001; zero-containing CIs and non-significant P values agree. |
| S017 | PASS_1_COMPLETE — OBSERVATION | STAT1-001; force direction and effect/CI/P diagnostics otherwise agree. |
| S018 | PASS_1_COMPLETE — OBSERVATION | STAT1-001; percent-severity direction and effect/CI/P diagnostics otherwise agree. |
| S019 | PASS_1_COMPLETE — OBSERVATIONS | STAT1-001 and STAT1-004. Direct PDF P is `.02`, not the `.28` transcribed in the fresh map. |
| S020 | PASS_1_COMPLETE — OBSERVATION | STAT1-001; direct source’s mean-SCN4A `P=.28` agrees with its zero-containing CI. |
| S021 | PASS_1_COMPLETE — OBSERVATIONS | STAT1-001 and STAT1-005. |
| S022 | PASS_1_COMPLETE — NO_ISSUE | Two-sided/exploratory conventions and row-specific model distinctions were applied; no P-value display zero occurs. |
| S501 | PASS_1_COMPLETE — NO_ISSUE | Mean 4.4 is within ordered CrI; threshold probability/action coherent. |
| S502 | PASS_1_COMPLETE — NO_ISSUE | Mean 3.1 is within ordered CrI; threshold probability/action coherent. |
| S503 | PASS_1_COMPLETE — NO_ISSUE | Mean 1.1 is within ordered CrI; 81% and continued action use stated threshold. |
| S504 | PASS_1_COMPLETE — NO_ISSUE | Mean 4.7 is within ordered CrI; threshold probability/action coherent. |
| S505 | PASS_1_COMPLETE — UNRESOLVED_PRECISION | Mean lies in ordered CrI; printed 80%/continued may reflect an unprinted probability above the strict >80% threshold after rounding. |
| S506 | PASS_1_COMPLETE — NO_ISSUE | Mean 3.2 is within ordered CrI; threshold probability/action coherent. |
| S507 | PASS_1_COMPLETE — NO_ISSUE | Mean 3.7 is within ordered CrI; threshold probability/action coherent. |
| S508 | PASS_1_COMPLETE — NO_ISSUE | Mean 0.00 lies within wide ordered CrI; special prior/no-stiffness footnote explains action. `0.00` is an estimate, not a display-zero P value. |
| S509 | PASS_1_COMPLETE — NO_ISSUE | Mean 2.66 is within ordered CrI; threshold probability/action coherent. |
| S510 | PASS_1_COMPLETE — NO_ISSUE | Mean -.05 is within ordered CrI; 2% and stopped action agree with <20% definition. |
| S511 | PASS_1_COMPLETE — NO_ISSUE | Mean 3.5 is within ordered CrI; threshold probability/action coherent. |
| S512 | PASS_1_COMPLETE — NO_ISSUE | Mean 2.7 is within ordered CrI; threshold probability/action coherent. |
| S513 | PASS_1_COMPLETE — NO_ISSUE | Mean 4.49 is within ordered CrI; threshold probability/action coherent. |
| S514 | PASS_1_COMPLETE — NO_ISSUE | Mean 3.22 is within ordered CrI; threshold probability/action coherent. |
| S515 | PASS_1_COMPLETE — NO_ISSUE | Mean 2.55 is within ordered CrI; threshold probability/action coherent. |
| S516 | PASS_1_COMPLETE — NO_ISSUE | Mean 2.63 is within ordered CrI; 99% and action coherent. |
| S517 | PASS_1_COMPLETE — UNRESOLVED_PRECISION | Mean lies within ordered CrI; printed 80%/continued may be a rounded value above strict >80%. |
| S518 | PASS_1_COMPLETE — NO_ISSUE | Mean 4.41 is within ordered CrI; threshold probability/action coherent. |
| S519 | PASS_1_COMPLETE — NO_ISSUE | Mean .01 is within ordered CrI; 1% and stopped action agree with <20% definition. |
| S520 | PASS_1_COMPLETE — NO_ISSUE | Mean 5.49 is within ordered CrI; threshold probability/action coherent. |
| S521 | PASS_1_COMPLETE — NO_ISSUE | Mean 2.64 is within ordered CrI; threshold probability/action coherent. |
| S522 | PASS_1_COMPLETE — NO_ISSUE | Mean 1.65 is within ordered CrI; threshold probability/action coherent. |
| S523 | PASS_1_COMPLETE — NO_ISSUE | Mean 4.65 is within ordered CrI; threshold probability/action coherent. |
| S524 | PASS_1_COMPLETE — NO_ISSUE | Mean 3.14 is within ordered CrI; threshold probability/action coherent. |
| S525 | PASS_1_COMPLETE — NO_ISSUE | Mean 4.50 is within ordered CrI; threshold probability/action coherent. |
| S526 | PASS_1_COMPLETE — NO_ISSUE | Mean 6.99 is within ordered CrI; threshold probability/action coherent. |
| S527 | PASS_1_COMPLETE — NO_ISSUE | Mean 3.57 is within ordered CrI; threshold probability/action coherent. |
| S528 | PASS_1_COMPLETE — UNRESOLVED_PRECISION | `4+23=27`; dropouts/nonresponders reconcile. The two printed 80% continued actions are not candidates absent unrounded probabilities. |
| S529 | PASS_1_COMPLETE — NO_ISSUE | Outcome-specific posterior areas, N=27, `.75` threshold, and Pbo-minus-Mx direction agree with main source. |
| S530 | PASS_1_COMPLETE — OBSERVATION | STAT1-006; individual/total code otherwise defines the correct positive Pbo-minus-Mx contrast and posterior thresholds. |
| S531 | PASS_1_COMPLETE — OBSERVATIONS | STAT1-006 and STAT1-007; genotype code, subgroup direction, and thresholds otherwise agree. |
| S532 | PASS_1_COMPLETE — NO_ISSUE | `0/1,000=0.00` type-I error; this is a simulation frequency, not a P-value display zero. |
| S533 | PASS_1_COMPLETE — NO_ISSUE | `685/1,000=68.5%`, `315+685=1,000`, and `1.29-1.75=-.46` reconcile. |
| S534 | PASS_1_COMPLETE — UNRESOLVED_VERSION_CONTEXT | Protocol stop wording (`>=80%`, `<=20%`) differs from published strict wording, but it is a prospective version with no unrounded matched observed probability; no candidate. |

## Limitations and exclusions

- No raw data, model output, SEs, covariance matrices, CI-construction method for the linear mixed model, or unrounded posterior probabilities were supplied. No such quantity was inferred from convention alone.
- S009’s mixed-model CI/P diagnostic was therefore retained as an unresolved definition rather than a candidate.
- S505/S517 and S528 print exactly 80% but the decision rule is strict `>80%`; displayed whole-percent rounding does not establish a contradiction.
- No coherent finite-precision P-value display zero was found. No candidate is based on a zero display.

## Pass summary

- **Assigned/completed relationships:** 56/56 (S001-S022; S501-S534).
- **Provisional statistical observations:** 7 (`STAT1-001` through `STAT1-007`), pending ledger merge and human adjudication.
- **No-candidate / unresolved-definition records:** retained explicitly for every remaining relationship.
