# Statistical consistency review — pass 1

## Scope, evidence boundary, and method

Independent fresh pass-1 review of every canonical inferential relationship, `S001`–`S038`, in `statistics/relationship_inventory.md`. Evidence was restricted to the three supplied direct PDFs and current-run fresh text/layout/rendered assets and relationship maps. No legacy audit output, web material, or inferred model detail was used.

`PASS_1_COMPLETE` records completed coverage only. It does not assign a severity, validity decision, correction, acceptance, or adjudication outcome. Candidate signals below have no stable `C` IDs and are for coordinator registration and later mechanical recheck.

Checks applied where the supplied source permitted them: point-estimate containment; interval ordering; sign/direction; population, contrast, label, and scale matching; arithmetic from printed counts/denominators; cross-location repetition; and P-value/test/interval compatibility only where the paper supplied a compatible rule. Diagnostic approximations are explicitly labelled and do not replace the reported analysis. No sidedness, degrees of freedom, covariance, variance estimator, CI construction, multiplicity handling, denominator, model, or estimand mapping was inferred from convention alone.

## Relationship-by-relationship pass-1 record

| S ID | PASS_1_COMPLETE review record |
|---|---|
| S001 | **PASS_1_COMPLETE.** DOC-001 p.3 defines the primary contrast as BMV minus ETI and requires a two-sided 95% CI lower limit greater than `-1%` for noninferiority. This establishes the decision rule and direction used for S002–S004; no observed-result contradiction is in this definition itself. |
| S002 | **PASS_1_COMPLETE.** DOC-001 pp.1,4 reports ITT difference `0.11%`, one-sided 97.5% CI `-1.64% to infinity`, and P for noninferiority `.11`. The estimate is within the ordered interval; the lower endpoint is below the stated `-1%` margin, so the printed noninferiority conclusion is directionally coherent. The same p.4 narrative also says the lower limit was “greater” than the threshold; that direct statement conflicts with the displayed endpoint and rule and is retained as SP1-01. |
| S003 | **PASS_1_COMPLETE.** DOC-001 p.4 hierarchical center-random-effect result `0.05%` is inside its one-sided 97.5% interval `-1.70% to infinity`. It is explicitly a distinct post-hoc model; no comparison to the unadjusted ITT estimate is warranted. |
| S004 | **PASS_1_COMPLETE.** DOC-001 p.4 PP result `4.3%` versus `4.2%`, difference `.08%`, one-sided 97.5% CI `-1.74% to infinity`, P `.12`, retains a distinct PP population. Estimate containment and endpoint order hold; its lower endpoint is below the `-1%` margin. No exact P reconstruction is supported by a row-specific variance/test definition. |
| S005 | **PASS_1_COMPLETE.** DOC-001 p.3 supplies secondary-endpoint rules: chi-square tests on proportions, 95% CIs for odds ratios and differences, two-sided alpha `.05`, and no multiplicity adjustment. The rule is conditional and does not identify a row-specific CI construction or chi-square-versus-Fisher choice. |
| S006 | **PASS_1_COMPLETE.** DOC-001 p.6 ITT day-28-survival difference `.1%` lies in ordered `-1.8% to 2.1%`; counts `55/1018` and `54/1022` give approximately `.12` percentage points, compatible with `.1%` at the displayed precision. P `.90` is not independently reconstructed. |
| S007 | **PASS_1_COMPLETE.** DOC-001 p.6 assigns P `.68` to the multicategory ITT CPC distribution. The test statistic, degrees of freedom, and row-level method are absent; it is not a P value for a single CPC level. |
| S008 | **PASS_1_COMPLETE.** DOC-001 p.6 ITT hospital-admission difference `-3.7%` lies in ordered `-7.7% to .3%`; printed counts/denominators give approximately `-3.70` percentage points. Direction and repeated narrative/table presentation agree. |
| S009 | **PASS_1_COMPLETE.** DOC-001 pp.4,6 ITT ROSC difference `-4.7%` lies in ordered `-8.8% to -.5%`; `348/1018 - 397/1022` is approximately `-4.67` percentage points. The text says ROSC was greater with ETI, agreeing with the BMV-minus-ETI sign. |
| S010 | **PASS_1_COMPLETE.** DOC-001 p.6 PP day-28-survival point difference `.1%` is inside ordered CI `-10 to 9.7` and P `.99` is displayed. However, the printed counts/denominators imply about `.019` percentage points (rounding to `.0` at one decimal), not `.1`; this direct arithmetic signal is SP1-02. The unusually wide displayed CI, considered separately under the supplied secondary-analysis framework, is SP1-03. |
| S011 | **PASS_1_COMPLETE.** DOC-001 p.6 gives PP CPC-distribution P `.76`, attached to the full five-category distribution. It lacks a test statistic/method detail needed for reconstruction; no cross-location conflict was found. |
| S012 | **PASS_1_COMPLETE.** DOC-001 p.6 PP hospital-admission difference `-4.0%` lies in ordered `-7.6% to .6%`; `289/995 - 312/943` is approximately `-4.04` percentage points. P `.055` is not recalculated because the row-specific test/CI construction is not supplied. |
| S013 | **PASS_1_COMPLETE.** DOC-001 p.6 PP ROSC prints BMV `342/995 (34.4%)`, ETI `377/943 (30.0%)`, and BMV-minus-ETI `-5.6%` with CI `-9.9% to -1.3%`. The estimate is inside the ordered interval, but the ETI percentage conflicts with its count/denominator and the displayed percentage direction conflicts with the printed difference. This direct signal is SP1-04. |
| S014 | **PASS_1_COMPLETE.** DOC-001 pp.1,4,6 safety difficulty difference `4.7%` lies in ordered `1.5% to 7.9%`; `186/1027 - 134/996` is approximately `4.66` percentage points. Matched locations agree. |
| S015 | **PASS_1_COMPLETE.** DOC-001 pp.1,4,6 safety failure difference `4.6%` lies in ordered `2.8% to 6.4%`; printed counts give approximately `4.61` percentage points. `P<.001` is an inequality display, not a display-zero result. |
| S016 | **PASS_1_COMPLETE.** DOC-001 pp.1,4,6 regurgitation difference `7.7%` lies in ordered `4.9% to 10.4%`; printed counts give approximately `7.68` percentage points. `P<.001` is an inequality display, not a display-zero result. |
| S017 | **PASS_1_COMPLETE.** DOC-001 p.4 center-5 CCF BMV-minus-ETI difference `-1%` lies in `-4% to 2%` and agrees with BMV `86%` versus ETI `87%`. The analysis model/denominator for its P `.70` is not supplied. |
| S018 | **PASS_1_COMPLETE.** DOC-001 p.4 describes a comparison of the *number of pauses longer than 2 seconds*: BMV `27` versus ETI `16`, then labels the arithmetic difference `11 seconds` (CI `7 to 15`; P `<.001`). `27-16=11`, but a count comparison and a seconds label do not use the same stated measure. This direct label/scale signal is SP1-05; P is an inequality, not display zero. |
| S019 | **PASS_1_COMPLETE.** DOC-001 p.3 planning values `956` per group, 80% power, two-sided 95% CI, 5,000 simulations, and a 2,000-person target are explicitly planning inputs. `956 x 2 = 1,912`, which does not exceed the planned 2,000 total; no outcome inference is implied. |
| S020 | **PASS_1_COMPLETE.** DOC-001 pp.3,6 labels VAS `0-100 mm`, Han `>2`, IDS `>5`, and medians/IQRs. Values and labels are distinct measures; no P value or direct label contradiction occurs in this relationship. |
| S021 | **PASS_1_COMPLETE.** DOC-002 pp.11,35-36 defines ITT and PP populations. The definitions match the population labels used in the main result records; major-deviation classification is not supplied and is not inferred. |
| S022 | **PASS_1_COMPLETE.** DOC-002 pp.11,36-37 defines a two-sided 95% CI for BVM/TI difference and lower limit `>-.01`. This is directionally compatible with the main article's one-sided 97.5% lower-bound presentation after exact contrast matching; no observed protocol result is printed. |
| S023 | **PASS_1_COMPLETE.** DOC-002 p.36 records H0 `<=-.01`, H1 `>=-.01`, and a difference test only after noninferiority. It agrees with S022's stated boundary direction; no post-noninferiority observed test is supplied. |
| S024 | **PASS_1_COMPLETE.** DOC-002 pp.11,37 conditionally specifies chi-square/95% OR-plus-difference CIs and t test/Mann-Whitney. It does not select a test or variance/CI model for a particular observed row. |
| S025 | **PASS_1_COMPLETE.** DOC-002 pp.11,36 describes planned interim reviews at 50% and 75% for futility/sample-size recalculation. No observed interim result, stopping boundary, or alpha-spending calculation is supplied. |
| S026 | **PASS_1_COMPLETE.** DOC-002 pp.11,37 repeats 3%, 2%, 1% margin, 956/group, power `.8`, alpha `.025`, 2,000 total, and 5,000 simulations. These planning values are internally nonconflicting; no simulation inputs beyond those printed are inferred. |
| S027 | **PASS_1_COMPLETE.** DOC-002 p.37 supplies planned safety chi-square/95% OR and exploratory logistic regression definitions. No reported row-specific safety-model statistic is available for further compatibility checking. |
| S028 | **PASS_1_COMPLETE.** DOC-002 p.37 specifies worst-case no-success primary ITT missing-data treatment and possible multiple-imputation sensitivity. No supplied result identifies missing observations or an incompatible observed denominator. |
| S029 | **PASS_1_COMPLETE.** DOC-002 pp.64-66 repeats S021-S026 framework values in a revised-protocol summary. Matched definitions agree at the mapped level; historical version changes are not treated as a same-result contradiction. |
| S030 | **PASS_1_COMPLETE.** DOC-002 pp.120-121 SAP restates BVM-minus-TI noninferiority margin `-.01`, H0/H1 direction, and two-sided alpha `.05`. This agrees with the CI decision framework after distinction between primary noninferiority and secondary testing. |
| S031 | **PASS_1_COMPLETE.** DOC-002 p.124 specifies a two-sided 95% primary CI, strict lower limit `>-.01`, possible exact CI, and ITT/PP/AT populations. The observed main lower-bound presentation is compatible in form; its exact CI construction is not supplied. |
| S032 | **PASS_1_COMPLETE.** DOC-002 pp.120,123 says planned interims were cancelled, only final analysis occurred, no multiplicity adjustment, primary missing data count as no success, and secondary endpoints are not imputed. No supplied matched outcome contradicts those definitions. |
| S033 | **PASS_1_COMPLETE.** DOC-002 pp.123-124 specifies nonmissing categorical denominators, one-decimal rounding, secondary chi-square/difference-CI methods, and t/Mann-Whitney alternatives. This permits count/denominator checking but does not define an exact row-level CI estimator. |
| S034 | **PASS_1_COMPLETE.** DOC-002 p.124 defines safety ITT/AT and chi-square/Fisher/t/Mann-Whitney alternatives. No unreported row-level choice was assumed. |
| S035 | **PASS_1_COMPLETE.** DOC-003 p.3 post-hoc exclusion result `.4` has ordered CI `[-2.2,1.3]` containing the estimate; printed counts `43/971` and `39/978` yield approximately `.44` percentage points. P `.63` is not reconstructed without selected chi-square/Fisher method and CI construction. |
| S036 | **PASS_1_COMPLETE.** DOC-003 p.3 reclassification result `.9` has ordered CI `[-.9,2.7]` containing the estimate; `41/863 - 45/1174` is approximately `.92` percentage points. P `.31` is not independently reconstructed for the same limitation. |
| S037 | **PASS_1_COMPLETE.** DOC-002 p.122's SAP safety list predates DOC-002 pp.114-116 additions of aspiration pneumonia/BVM failure. This is a versioned-definition difference; no supplied final analysis-set definition or matched result establishes a contradiction. |
| S038 | **PASS_1_COMPLETE.** Fresh visual recheck of DOC-002 rendered p.103 shows IDS `0<IDS<=5` slight and `IDS>5` moderate-major; DOC-001 calls IDS `>5` difficult. The definitions agree and score 5 is explicitly categorized as slight difficulty; no candidate. |

## Candidate signals for coordinator registration

### SP1-01 — Primary-outcome narrative reverses the displayed noninferiority-bound direction

- **Proposed category:** Statistical reporting inconsistency.
- **Exact source locations:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=3` (rule: lower two-sided-95% CI limit must be `>-1%`); DOC-001 `jama_jabre_2018_oi_180004.pdf#page=4` (ITT result and narrative).
- **Direct observation:** The p.4 ITT result prints difference `.11%` and one-sided 97.5% CI `-1.64% to infinity`, then states: “The lower limit of the confidence interval was greater than the threshold of noninferiority, thus noninferiority was not demonstrated.”
- **Rule and calculation:** `-1.64%` is not greater than the stated `-1.00%` threshold; `-1.64 - (-1.00) = -0.64` percentage points. The reported lower endpoint fails the stated strict `>-1%` rule. The sentence's conclusion that noninferiority was not demonstrated agrees with the numeric rule, but its word “greater” does not.
- **Limitations:** No inferential approximation is needed. This signal concerns the printed direction statement, not an intended correction or the noninferiority conclusion.
- **Source-grounded alternative interpretation:** “Greater” may be a wording error for “not greater”; the supplied package does not explicitly state this.
- **Exact human question:** Should the p.4 direction word be “not greater” (or otherwise revised), while retaining the printed conclusion that noninferiority was not demonstrated?
- **Status:** Pending Human Adjudication.

### SP1-02 — PP day-28-survival displayed point difference does not reconcile with its printed counts and denominators

- **Proposed category:** Numeric or arithmetic inconsistency / Statistical reporting inconsistency.
- **Exact source location:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=6`, Table 2, Per-Protocol Analysis, survival at 28 days.
- **Direct observation:** The row prints BMV `54/995 (5.4)`, ETI `51/943 (5.4)`, and BMV-minus-ETI difference `.1` percentage points.
- **Rule and calculation:** `(54/995 - 51/943) x 100 = 0.0189...` percentage points, which rounds to `.0` at the table's one-decimal percentage precision, rather than `.1`. The supplied SAP states that categorical values use nonmissing denominators and one-decimal rounding (DOC-002 `joi180004supp1_prod.pdf#page=123`).
- **Limitations:** The source does not identify a different PP denominator or a hidden retained quantity. This is an arithmetic check from the printed count/denominator pair, not a reconstruction of the CI or P value.
- **Source-grounded alternative interpretation:** A row element may use a different retained analysis dataset or an unprinted denominator; neither is stated in the Table 2 row or its footnote.
- **Exact human question:** Is the displayed PP difference intended to be `.0`, or is a numerator, denominator, or analysis-population definition different from the values printed in Table 2?
- **Status:** Pending Human Adjudication.

### SP1-03 — PP day-28-survival interval is diagnostically incompatible with its same-row scale and reported near-null result

- **Proposed category:** Statistical reporting inconsistency / Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=3` (secondary rate endpoints use chi-square and corresponding 95% difference CIs); DOC-001 `jama_jabre_2018_oi_180004.pdf#page=6`, Table 2 PP survival row (`.1`, 95% CI `-10 to 9.7`, P `.99`).
- **Direct observation:** The Table 2 column is labelled BMV(%) minus ETI(%) `(95% CI)` and prints a `.1` percentage-point difference, but a 20-percentage-point-wide interval `-10 to 9.7`.
- **Diagnostic calculation (not a replacement analysis):** From the printed proportions, the ordinary unpooled binomial standard-error approximation is `1.028756` percentage points. With point difference `0.018864`, its ordinary Wald 95% interval is `-1.997498 to 2.035226`, or about `-2.00 to 2.04` percentage points, not `-10 to 9.7`. The printed `.99` is retained only as near-null context and does not independently identify or contradict the missing CI construction. These diagnostics identify a scale/decimal or transcription question; they do not determine intended endpoints.
- **Limitations:** The paper supplies chi-square/Fisher alternatives and says difference CIs are corresponding, but does not name the row-specific test selection, CI construction, variance estimator, or retained analysis data. Therefore no exact P/CI identity is asserted.
- **Source-grounded alternative interpretation:** The table might contain a decimal/scale transcription issue, or a nonstandard row-specific CI construction; the package does not distinguish these possibilities.
- **Exact human question:** Confirm the two printed PP-survival CI endpoints and their units, then provide the row-specific CI method and retained inputs used for the published `.99` result.
- **Status:** Pending Human Adjudication.

### SP1-04 — PP ROSC ETI percentage conflicts with its numerator/denominator and reverses the displayed difference direction

- **Proposed category:** Denominator, proportion, or total inconsistency / Statistical reporting inconsistency.
- **Exact source location:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=6`, Table 2, Per-Protocol Analysis, return of spontaneous circulation.
- **Direct observation:** The row prints BMV `342/995 (34.4)`, ETI `377/943 (30.0)`, BMV-minus-ETI difference `-5.6` (95% CI `-9.9 to -1.3`), P `.01`.
- **Rule and calculation:** `(377/943) x 100 = 39.9788...%`, which rounds to `40.0%`, not `30.0%`. `(342/995 - 377/943) x 100 = -5.6069...` percentage points, agreeing with printed `-5.6`. By contrast, the displayed percentages yield `34.4 - 30.0 = +4.4` percentage points, the opposite direction. The printed `-5.6` is inside its ordered CI.
- **Limitations:** No row-specific test/CI construction is supplied, so the P value is not reconstructed. The direct count/percentage/direction contradiction is independent of that missing definition.
- **Source-grounded alternative interpretation:** `30.0` may be a percentage transcription error rather than an alternate numerator/denominator, because the printed count and difference align with about `40.0%`; this explanation is not stated in the source.
- **Exact human question:** Is ETI PP ROSC intended to be `377/943 (40.0%)`, or does a different ETI numerator, denominator, or PP population underlie the row?
- **Status:** Pending Human Adjudication.

### SP1-05 — Center-5 pauses result labels a count difference and interval in seconds

- **Proposed category:** Measure, label, or scale inconsistency.
- **Exact source location:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=4`, Post-Hoc Analyses.
- **Direct observation:** The text says the analysis determined “the number of pauses greater than 2 seconds,” reports BMV `27` versus ETI `16`, and then prints “difference, 11 seconds [95% CI, 7 to 15]; P < .001.”
- **Rule and calculation:** The reported group values are counts of qualifying pauses; `27 - 16 = 11` counts. A difference and CI for that stated count measure should not be labelled in seconds unless the 27 and 16 values instead denote a time quantity, which the sentence does not say.
- **Limitations:** The source does not provide individual-level pause summaries, a unit for the group values, distributional form, or test selection. No P-value reconstruction is attempted. `P<.001` is an inequality display, not a display-zero candidate.
- **Source-grounded alternative interpretation:** The authors may have intended to compare pause duration rather than the number of pauses, or “seconds” may be a unit-label error; the package does not resolve which.
- **Exact human question:** Were 27 and 16 numbers of pauses or duration summaries, and what unit should apply to the reported difference and CI?
- **Status:** Pending Human Adjudication.

## Display-zero coverage and limitations

- **DISPLAY_ZERO_NOT_CANDIDATE records:** 0. No assigned S relationship contains `P = 0`, `p = 0.000`, or equivalent. `P<.001` is an inequality display and was not treated as a display zero or candidate.
- P-value, test-statistic, SE, and exact CI reconciliation was not attempted where the sources leave the row-level model, test choice, CI construction, variance estimator, covariance, sidedness, degrees of freedom, multiplicity rule, denominator, or estimand mapping undefined.
- S037 remains a versioned-definition coverage record, not a candidate. S038 is a coherent scale-definition record after visual confirmation that score 5 belongs to slight difficulty.

## Coverage totals

- Assigned and completed relationships: **38/38** (`S001`–`S038`).
- Distinct pass-1 candidate signals emitted: **5** (`SP1-01` through `SP1-05`); no stable candidate IDs assigned.
- Display-zero non-candidates: **0**.
