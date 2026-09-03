# Statistical Consistency Review — Pass 2

## Execution, authority, and complete scope

- **Stage:** mandatory independent statistical consistency pass 2.
- **Reviewer runtime ID:** `/root/statistical_pass_2`.
- **Scope:** all 34 canonical inferential relationships: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, and S034.
- **Inputs reviewed:** the current canonical statistical inventory; complete numeric and cross-source checker artifacts; stable candidate ledger C001-C007; and the mechanical direct-source recheck. These artifacts were used as locators and cross-lane evidence only. Direct supplied PDFs were re-read for the primary-result pages (DOC-001 pp. 1, 4, 7), the protocol/statistical-plan pages (DOC-002 pp. 6, 15-16, 36-39), and the Supplement 2 method/result pages (DOC-003 pp. 8, 28-30, 34-35, 39-62). No legacy review output was used as scientific input.
- **Checks applied:** matched population, time point, contrast and direction; count/denominator arithmetic; direct point-estimate versus one-sided-bound ordering where applicable; effect-measure/percentage-point/test labels; cross-location repetitions; and recheck implications. Interval/P-value/test/statistic/SE compatibility was not reconstructed when the source did not supply the compatible model, variance estimator, sidedness, covariance, degrees of freedom, or estimand definition.
- **Display-zero control:** no assigned relationship displays `P = 0`, `p = 0.000`, or an equivalent finite-precision zero. No display-zero candidate was created.

## Cross-lane and recheck reconciliation

The complete stable ledger was revisited before new discovery. The following pre-existing candidates remain relevant to statistical relationships; this is not an adjudication or a new stable-ID assignment.

| Existing stable ID | Pass-2 statistical implication | Result of revisit |
|---|---|---|
| C001 | S001 and S008-S010: protocol versus reported endpoint/failure-condition definition | The direct-source recheck confirms that this is a governing-definition comparison, not a rederived noninferiority calculation. Missing dated amendment/final-SAP history and component status for the 15 listed participants prevent quantification; no additional statistical contradiction was found. |
| C004 | S022 and S024-S026: `p=.014` footnote repeats beneath tables with different displayed contrasts | The source pages confirm distinct site, baseline-A1C, and completion-status column contrasts. The existing unresolved scope/label issue remains; there is no basis to recalculate the unreported rank-sum outputs or assign an additional candidate. |
| C005 | S026: no-significance wording paired with `p<.05` | The direct page and recheck preserve the inequality-direction contradiction. No completion-status test results are supplied to identify a further distinct discrepancy. |
| C006 | S018 and S028: eTable 10 method says chi-squared; eTable 10b footnote says Wilcoxon rank-sum | The directly printed 6/183 versus 7/185 counts round to 3.3% versus 3.8%; the displayed `P=.793` is numerically compatible with an ordinary uncorrected two-proportion/chi-squared diagnostic, but that diagnostic cannot identify the named generating procedure. The incompatible labels remain one issue, not two. |
| C007 | S019 and S031: MI-pooled percentages 32.2%/31.9% and AI-minus-human RD −1.1 pp | Direct subtraction of the printed one-decimal percentages remains positive, whereas the printed RD is negative. The source still omits the full estimand/model/standardization/pooling calculation, so the existing candidate and its human question remain the appropriate record; no separate interval or P-value candidate was created. |

Numeric-only C002 and label-only C003 were also considered as cross-lane context. Neither supplies an additional inferential contradiction for an S relationship.

## Relationship-level pass-2 record

`NO_NEW_CANDIDATE` means no distinct qualifying candidate beyond the stable ledger was located. It is not an adjudication of the printed result. One-sided 95% values are lower confidence bounds, not two-sided intervals.

| Stable ID | PASS_2_COMPLETE result | Pass-2 check and source-grounded limitation |
|---|---|---|
| S001 | NO_NEW_CANDIDATE; C001_CONTEXT | DOC-001 pp. 1,4 labels the ITT AI-minus-human RD, one-sided lower-bound noninferiority rule, and −15-pp margin consistently. C001 records the distinct protocol-definition issue; protocol amendment history is absent. |
| S002 | NO_NEW_CANDIDATE | DOC-001 p. 4: 276 analyzable participants and 25% attrition yield 368 target participants (`276/0.75=368`). The power formula and variance assumptions are not supplied. |
| S003 | NO_NEW_CANDIDATE | DOC-001 p. 4 differentiates binomial, chi-squared, descriptive-CI, and sensitivity families. Its eTable 10 method implication is captured once under C006/S018-S028. |
| S004 | NO_NEW_CANDIDATE | DOC-001 pp. 1,4,7: 58/183 versus 59/185 gives approximately −0.2 pp; the printed one-sided lower bound −8.2 pp is below the estimate and remains above −15 pp. Compatible binomial-model details beyond the stated label are unavailable. |
| S005 | NO_NEW_CANDIDATE | DOC-001 p. 7 explicitly calls component one-sided CIs descriptive and says no multiplicity adjustment was applied; no contrary formal-test claim was found. |
| S006 | NO_NEW_CANDIDATE | DOC-001 p. 4 initiation/completion directions match the printed fractions (171/183 versus 153/185; 117/183 versus 93/185) and their chi-squared P-value labels. Exact test options are not supplied. |
| S007 | NO_NEW_CANDIDATE | DOC-001 p. 4 and DOC-003 p. 56 distinguish incident diabetes-range A1C counts/percentages from diagnosis. `P=.78` has no source-grounded contradictory comparator. |
| S008 | NO_NEW_CANDIDATE_MISSING_DEFINITION; C001_CONTEXT | DOC-002 pp. 6,15-16 supplies the planned binary endpoint but not all matched margin/CI/test/population detail in this relationship. C001 preserves the separately observed endpoint-definition difference. |
| S009 | NO_NEW_CANDIDATE_MISSING_DEFINITION; C001_CONTEXT | DOC-002 pp. 36-37 gives the 15-pp plan, 50% assumption, alpha/power, target sample, and CI framework. The exact sample-size/CI formula and final governing amendment are unavailable. |
| S010 | NO_NEW_CANDIDATE_MISSING_DEFINITION; C001_CONTEXT | DOC-002 pp. 37-39 names planned ITT/per-protocol, logistic, linear, mixed, and sensitivity models but gives no observed coefficient, interval, test statistic, or final model output. |
| S011 | NO_NEW_CANDIDATE | DOC-002 pp. 38-39 supplies a conditional PA-missingness/MI plan. It is not an observed result and has no matched contradiction. |
| S012 | NO_NEW_CANDIDATE_MISSING_DEFINITION | DOC-002 p. 39 gives the planned cost-effectiveness horizon, discounting, Markov/QALY/ICER framework but no observed economic estimate or uncertainty result. |
| S013 | NO_NEW_CANDIDATE_MISSING_DEFINITION | DOC-003 p. 8 supplies a device-discordance threshold relative to a 95% CI but no estimate, interval endpoints, or test statistic for a compatibility calculation. |
| S014 | NO_NEW_CANDIDATE | DOC-003 pp. 28,34 explicitly identifies age-adjusted AI-minus-human RDs in percentage points with one-sided lower bounds and a −15-pp line. Adjusted RDs need not equal crude displayed proportions. |
| S015 | NO_NEW_CANDIDATE | DOC-003 pp. 28,35 identifies exploratory subgroup RDs, direction, scale, one-sided bounds, and no multiplicity adjustment. Displayed subgroup counts agree with the shown directions at rounding precision. |
| S016 | NO_NEW_CANDIDATE | DOC-003 p. 29 distinguishes chi-squared tests for proportions from Wilcoxon rank-sum tests for continuous eTable 4 measures. No eTable 4 result-label conflict was located. |
| S017 | NO_NEW_CANDIDATE | DOC-003 pp. 29,51 separately defines outside-window proportion and continuous-day comparisons; `P=.016` is attached to the 12-month days-outside-window comparison. Test details needed to reproduce it are absent. |
| S018 | NO_NEW_CANDIDATE; C006_CONTEXT | DOC-003 p. 29 specifies chi-squared for eTable 10's binary proportion comparison. The distinct incompatible p. 52 result-table label remains C006. |
| S019 | NO_NEW_CANDIDATE; C007_CONTEXT | DOC-003 p. 30 provides 20-set MICE and Rubin's-rules context. The p. 59 MI displayed-value/RD issue remains C007; no unreported pooling calculation was inferred. |
| S020 | NO_NEW_CANDIDATE | DOC-003 p. 34's age-adjusted primary/component RDs retain coherent AI-minus-human direction, percentage-point scale, and one-sided-bound framing. |
| S021 | NO_NEW_CANDIDATE | DOC-003 p. 35 subgroup RDs and lower bounds are consistently labelled as exploratory one-sided results; no same-population, same-contrast duplicate conflicts. |
| S022 | NO_NEW_CANDIDATE; C004_CONTEXT | DOC-003 pp. 39-40 prints the randomized-group age `p=.014` note, compatible with main-table `P=.01` at coarser precision. Its unlabelled repetition beneath other table contrasts is C004. |
| S023 | NO_NEW_CANDIDATE_MISSING_DEFINITION | DOC-003 p. 41 states no significant eligibility difference without test, statistic, or exact P value. The source does not support a compatibility calculation. |
| S024 | NO_NEW_CANDIDATE; C004_CONTEXT | DOC-003 pp. 42-43 supplies site-specific P values (including age `.017`) and separately repeats the `.014` randomized-group note. Different contrasts prevent treating these as a direct numeric duplicate; C004 preserves the scope-label issue. |
| S025 | NO_NEW_CANDIDATE; C004_CONTEXT | DOC-003 pp. 44-45 provides baseline-A1C-stratum site/ethnicity P values and repeats the `.014` note. No same-comparator contradiction beyond C004 was found. |
| S026 | NO_NEW_CANDIDATE; C004_AND_C005_CONTEXT | DOC-003 pp. 46-47 has the completion-status table, the repeated `.014` statement (C004), and the internally reversed no-significance `p<.05` wording (C005). Missing completion-status test outputs prohibit a further calculation. |
| S027 | NO_NEW_CANDIDATE | DOC-003 p. 51 prints attendance/window denominators and `P=.016` for 12-month days outside the window; arithmetic and direction are coherent at display precision. |
| S028 | NO_NEW_CANDIDATE; C006_CONTEXT | DOC-003 p. 52 prints 6/183 versus 7/185, 3.3% versus 3.8%, and `P=.793`; the binary-proportion arithmetic is coherent. C006 retains the incompatible chi-squared/Wilcoxon labels. |
| S029 | NO_NEW_CANDIDATE | DOC-003 pp. 53-54 identifies the distinct per-protocol population and labels age `.010`, sex `.041`, and other characteristics `p>.05`; no cross-population value was conflated. |
| S030 | NO_NEW_CANDIDATE | DOC-003 p. 58: per-protocol binary fractions reproduce displayed percentages and RD directions; one-sided lower bounds are lower than their point estimates. The baseline-A1C restriction is labelled. |
| S031 | NO_NEW_CANDIDATE; C007_CONTEXT | DOC-003 p. 59 prints MI-pooled 32.2%/31.9% and RD −1.1 pp with lower bound −11.5. C007 captures the direct-subtraction/sign inconsistency and the missing estimand definition. |
| S032 | NO_NEW_CANDIDATE | DOC-003 p. 60: 58/183 (31.7%) minus 70/185 (37.8%) is −6.1 pp at display precision; the lower bound −14.3 and stated pattern-mixture assumptions are coherent. |
| S033 | NO_NEW_CANDIDATE | DOC-003 p. 61: 58/183 (31.7%) minus 60/185 (32.4%) is approximately −0.7 pp, compatible with printed −0.74 and the lower bound −8.8 under each stated scenario. |
| S034 | NO_NEW_CANDIDATE | DOC-003 p. 62: 58/183 (31.7%) minus 59/185 (31.9%) agrees with RD −0.20. The two different cluster rules explain distinct lower bounds −4.8 and −6.8; cluster-robust variance inputs are not supplied. |

## Pass-2 candidate discovery result

- **New provisional candidates (`STAT2-NEW`):** none.
- **Reason:** all directly observable statistical, label, direction, denominator, arithmetic, duplicate-value, and cross-source implications either reconcile at stated precision, are already represented by the distinct stable records C001 and C004-C007, or lack a named source definition required for a compatible inferential calculation.
- **No candidate was created from a missing model definition, a protocol/result comparison without a matched governing version, an adjusted-versus-crude comparison, a one-sided lower bound treated as a two-sided interval, or a finite-precision P-value display.**

## Completion and limitations

- **Relationships completed:** 34/34, all with an explicit `PASS_2_COMPLETE` result above.
- **Stable cross-lane candidate set revisited:** C001, C002, C003, C004, C005, C006, C007 (7/7).
- **Existing statistical candidate contexts revisited:** C001, C004, C005, C006, C007 (5/5); no ID was deleted, merged, renumbered, or adjudicated.
- **Limitations:** the supplied PDFs do not provide final protocol/SAP amendment history, all test options, degrees of freedom, covariance/variance estimators, individual-level values, full MICE per-imputation outputs, or exact adjusted estimands. These inputs were not inferred from convention. Diagnostic arithmetic is expressly limited to printed values and stated contrast order.

`PASS_2_COMPLETE`
