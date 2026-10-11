# Statistical consistency review — pass 1

## Scope and evidence boundary

Fresh independent pass-1 review of all 55 canonical statistical relationships (`S001`–`S055`). Evidence was restricted to the current-run direct-source text assets, the source-hash-matched authorized OCR provenance where it applies, and the current-run relationship maps needed to preserve source locations. No web material, old audit derivative, new OCR, or adjudication was used. `PASS_1_COMPLETE` below records coverage, not a validity, severity, or correction decision.

`DOC-001` is `jama_jabre_2018_oi_180004.pdf`; `DOC-002` is `joi180004supp1_prod.pdf`; `DOC-003` is `joi180004supp2_prod.pdf`. PDF locations use the supplied PDF-page numbering.

## Relationship-by-relationship results

| S ID | PASS_1_COMPLETE review result |
|---|---|
| S001 | **PASS_1_COMPLETE.** DOC-001 pp. 1, 3-4: `0.11%` lies within the one-sided 97.5% interval `-1.64% to infinity`; its lower bound is not greater than the stated `-1%` margin. The printed failure to demonstrate noninferiority follows the supplied decision rule. P-value/test-statistic reconstruction is not applicable because no compatible variance/test statistic is supplied. |
| S002 | **PASS_1_COMPLETE.** DOC-001 p. 4: hierarchical centre-random-effect estimate `0.05%` lies in `-1.70% to infinity`. It is a separately labelled model, not a value to substitute for the unadjusted ITT result; no conflicting matched statement was found. |
| S003 | **PASS_1_COMPLETE.** DOC-001 p. 4: PP `0.08%` lies in `-1.74% to infinity`, whose lower bound is below the `-1%` margin. The PP population and one-sided 97.5% convention are explicit. The printed `P=.12` cannot be independently recalculated without the specified test/variance, but no source-grounded contradiction was found. |
| S004 | **PASS_1_COMPLETE.** DOC-001 pp. 1, 4, 6: ITT day-28-survival difference `0.1%` lies in ordered `-1.8% to 2.1%`; counts `55/1018` and `54/1022` give an unrounded BMV-minus-ETI difference about `0.119` percentage points, compatible with `0.1%` at one decimal. Matched narrative/table values agree. |
| S005 | **PASS_1_COMPLETE.** DOC-001 pp. 1, 4, 6: ITT admission difference `-3.7%` lies in ordered `-7.7% to 0.3%`; `294/1018 - 333/1022` is about `-3.70` percentage points. Direction and matched locations agree. |
| S006 | **PASS_1_COMPLETE.** DOC-001 pp. 4, 6: ITT ROSC difference `-4.7%` lies in ordered `-8.8% to -0.5%`; `348/1018 - 397/1022` is about `-4.67` percentage points. Direction agrees. Exact P-value reproduction is not warranted because the row-specific chi-square/Fisher selection is not supplied. |
| S007 | **PASS_1_COMPLETE.** DOC-001 p. 6: the ITT CPC-distribution `P=.68` is attached to the five-category distribution, while primary success is separately defined as CPC 1+2. Counts give `35+9=44` and `37+6=43`, matching the primary numerator. No distribution-test details support recalculation. |
| S008 | **PASS_1_COMPLETE.** DOC-001 p. 6: all three PP secondary rows have ordered intervals containing their printed differences. The admission difference is compatible with counts. Two distinct printed-value inconsistencies in this relationship are recorded as `STAT1-CAND-001` and `STAT1-CAND-002` below; no row-specific chi-square/Fisher selection or CI method is supplied for P/CI reconstruction. |
| S009 | **PASS_1_COMPLETE.** DOC-001 p. 6: PP CPC-distribution `P=.76` is attached to the PP five-category distribution, not to a single category. The PP population label is explicit; no test statistic/row construction is supplied for independent P-value calculation. |
| S010 | **PASS_1_COMPLETE.** DOC-001 pp. 1, 4, 6: safety difficulty difference `4.7%` lies in `1.5% to 7.9%`; `186/1027 - 134/996` is about `4.66` percentage points, compatible with display rounding. |
| S011 | **PASS_1_COMPLETE.** DOC-001 pp. 1, 4, 6: safety failure difference `4.6%` lies in `2.8% to 6.4%`; `69/1028 - 21/996` is about `4.61` percentage points. `P<.001` is a threshold display, not a display-zero record. |
| S012 | **PASS_1_COMPLETE.** DOC-001 pp. 1, 4, 6: regurgitation difference `7.7%` lies in `4.9% to 10.4%`; `156/1027 - 75/999` is about `7.68` percentage points. `P<.001` is a threshold display, not a display-zero record. |
| S013 | **PASS_1_COMPLETE.** DOC-001 p. 6: Table 3 says chi-square *or* Fisher exact was used. The supplied evidence does not identify the row-specific choice, so no test-statistic/P-value reconciliation is valid; no incompatible claim was found. |
| S014 | **PASS_1_COMPLETE.** DOC-001 p. 3: the secondary-analysis family distinguishes difference and odds-ratio CIs, chi-square rate testing, and t/Mann-Whitney quantitative testing. The source supplies no rule that makes each displayed interval/P value from a common model; no unjustified measure substitution was made. |
| S015 | **PASS_1_COMPLETE.** DOC-001 p. 4: post-hoc centre-5 CCF BMV-minus-ETI difference `-1%` lies in `-4% to 2%` and agrees with displayed `86%` versus `87%`. No compatible model/denominator is supplied for P-value reproduction. |
| S016 | **PASS_1_COMPLETE.** DOC-001 p. 4: post-hoc pause result is labelled in seconds; `11` lies in ordered `7 to 15` seconds and direction agrees with BMV `27` versus ETI `16`. The quantitative-test choice/distribution is not supplied. `P<.001` is not a display zero. |
| S017 | **PASS_1_COMPLETE.** DOC-001 pp. 3, 7-8: planned `3%/2%`, 1% margin, 956/group, 80% power are consistently separated from observed 4.3%/4.2% primary estimates and the discussion’s underpowering interpretation. No design-result conflation was found. |
| S018 | **PASS_1_COMPLETE.** DOC-002 p. 11 and pp. 36-37: planned BMV/bag-minus-tracheal primary contrast, two-sided 95% CI, and lower-limit `>-0.01` rule are compatible with the matched main-paper one-sided 97.5% lower-bound convention after exact endpoint/population matching. No observed protocol result is printed. |
| S019 | **PASS_1_COMPLETE.** DOC-002 pp. 11, 36: exact-CI use is conditional. The source does not identify an observed CI construction to reconcile, so no method-specific inference was made. |
| S020 | **PASS_1_COMPLETE.** DOC-002 p. 36: printed NI hypotheses retain their boundary inequalities. No observed result is at the boundary, so no boundary-convention contradiction is present. |
| S021 | **PASS_1_COMPLETE.** DOC-002 p. 36: a difference test is planned after NI demonstration, but no alpha/test details or such observed test result are supplied. |
| S022 | **PASS_1_COMPLETE.** DOC-002 pp. 11, 37: planned secondary rate analysis says chi-square and 95% CIs for odds ratios and differences. It does not establish that a particular reported CI is an OR CI rather than a difference CI; no unsupported comparison was made. |
| S023 | **PASS_1_COMPLETE.** DOC-002 pp. 11, 37: t test/Mann-Whitney choice is conditional on distribution, with no observed endpoint-specific choice supplied. |
| S024 | **PASS_1_COMPLETE.** DOC-002 pp. 11, 36: interim analyses at 50%/75% are described for futility/sample-size recalculation; no stopping/alpha boundary is printed. |
| S025 | **PASS_1_COMPLETE.** DOC-002 pp. 11, 37: planned sample-size inputs `3%`, `2%`, `1%`, 956/group, power `.8`, alpha `.025`, 2,000 total, and 5,000 simulations agree with the repeated planned framework. They are not observed CAAM outcomes. |
| S026 | **PASS_1_COMPLETE.** DOC-002 p. 36: ITT and PP definitions are planned population definitions. The supplied exact definitions do not create a contradiction with the labelled ITT/PP main results. |
| S027 | **PASS_1_COMPLETE.** DOC-002 p. 37: safety/dichotomized endpoint plan specifies chi-square and 95% OR CI; no observed row-specific inferential construction is supplied. |
| S028 | **PASS_1_COMPLETE.** DOC-002 p. 37: multivariable logistic regression is exploratory; covariates and estimand are not supplied, and no numerical regression result is printed for reconciliation. |
| S029 | **PASS_1_COMPLETE.** DOC-002 p. 37: ITT missing-primary-endpoint worst-case rule and conditional sensitivity/multiple-imputation plan are stated. No evidence establishes missing primary data requiring a different observed-result denominator. |
| S030 | **PASS_1_COMPLETE.** DOC-002 pp. 17, 37: centre-stratified blocked randomization is a design rule; the source supplies no block size or realized-allocation rule from which an inconsistency could be inferred. |
| S031 | **PASS_1_COMPLETE.** DOC-002 p. 37: SAS 9.2 identifies planned software only; it defines no reproducible numerical relationship. |
| S032 | **PASS_1_COMPLETE.** DOC-002 p. 66: repeated primary ITT 95%-two-sided CI and strict lower-limit `>-0.01` NI rule matches the protocol framework and the appropriately matched main result convention. No conflict found. |
| S033 | **PASS_1_COMPLETE.** DOC-002 p. 90: repeated hypotheses/difference-test sequence retains the same contrast/margin. No boundary-equality result or post-NI difference test result is supplied. |
| S034 | **PASS_1_COMPLETE.** DOC-002 p. 91: repeated 28-day CPC<=2 ITT rule is consistent with the endpoint/population/margin controls used for S001. |
| S035 | **PASS_1_COMPLETE.** DOC-002 p. 66: secondary rate methods distinguish OR and difference CI. No matched result relabels one as the other. |
| S036 | **PASS_1_COMPLETE.** DOC-002 p. 91: repeated secondary rate methods contain no row-level variance, test, or CI construction for a stricter reconciliation. |
| S037 | **PASS_1_COMPLETE.** DOC-002 pp. 66, 91: t/Mann-Whitney distribution-dependent rule is repeated; outcome-specific distribution/test selection remains unreported. |
| S038 | **PASS_1_COMPLETE.** DOC-002 pp. 66, 91: 50%/75% interim purpose is repeated with no alpha-spending/futility threshold supplied. |
| S039 | **PASS_1_COMPLETE.** DOC-002 p. 92: the repeated 3%/2%, 1%, 956/group, .8, .025, 2,000, 5,000 design record is internally consistent and explicitly planned. |
| S040 | **PASS_1_COMPLETE.** DOC-002 p. 91: repeated ITT/PP definitions do not conflict with matched main-result labels; classification of major violations is not supplied. |
| S041 | **PASS_1_COMPLETE.** DOC-002 p. 92: safety chi-square/OR-CI and exploratory logistic-regression plan has no observed model-specific result to test. |
| S042 | **PASS_1_COMPLETE.** DOC-002 p. 92: missing-primary worst-case and conditional multiple-imputation rule is repeated; no matched evidence shows an incompatible observed handling. |
| S043 | **PASS_1_COMPLETE.** DOC-002 pp. 72, 92: stratified blocked randomization repeats without a block size/sequence or equal-realized-allocation requirement. |
| S044 | **PASS_1_COMPLETE.** DOC-002 p. 67: external-background `40/120 (33%)` versus `69/573 (12%)`, `P<.0001`, concerns different timing groups in a cited study, not the CAAM contrast. The threshold P display is not a display zero. |
| S045 | **PASS_1_COMPLETE.** DOC-002 p. 67: external-background `2.9%` among 367,837 BMV versus `1.0%` among 41,972 TI is labelled observational/cited and has different outcome/time context from CAAM. |
| S046 | **PASS_1_COMPLETE.** DOC-002 pp. 119-121: SAP NI hypotheses and day-28 favourable-neurological-survival endpoint match the protocol framework after BVM/TI wording and exact population matching. Native SAP text controls over authorized-OCR character uncertainty in duplicate pages. |
| S047 | **PASS_1_COMPLETE.** DOC-002 p. 120: SAP sample-size plan repeats BVM 3%, TI 2%, 1% margin, 956/group, .8, .025, 2,000, and 5,000 Newcombe-Wilson simulations. Planning alpha `.025` is distinct from later two-tailed `.05` secondary-test policy. |
| S048 | **PASS_1_COMPLETE.** DOC-002 pp. 121, 123-124: ITT/PP/AT and missing-data rules are definitions; the source does not identify a missing-data result that conflicts with reported matched outcomes. |
| S049 | **PASS_1_COMPLETE.** DOC-002 p. 122: day-28 CPC<=2 primary parameter and secondary outcome labels/time points are explicit. No matched label/scale conflict was found. |
| S050 | **PASS_1_COMPLETE.** DOC-002 p. 123: SAP gives non-missing denominators, one-decimal categorical rounding, and permissible rounded totals. This rule supports, rather than alters, exact count/denominator checks in matched tables. |
| S051 | **PASS_1_COMPLETE.** DOC-002 p. 124: primary two-sided 95% CI for BVM-minus-tracheal and strict lower-limit `>-0.01` rule is compatible with the matched primary result’s one-sided 97.5% lower interval. Exact CI construction remains conditional. |
| S052 | **PASS_1_COMPLETE.** DOC-002 p. 124: secondary chi-square/OR/difference CI, t/Mann-Whitney, two-tailed .05, and safety chi-square/Fisher methods are conditional alternatives. They do not establish a row-specific test or covariance/variance estimator. |
| S053 | **PASS_1_COMPLETE.** DOC-003 p. 2: eTable 1 centre counts sum to BMV `1018` and ETI `1022`; each displayed percentage is compatible with its stated group denominator at one decimal. This relationship has no inferential statistic. |
| S054 | **PASS_1_COMPLETE.** DOC-003 p. 3: eTable 2 exclusion row gives `43/971=4.4%`, `39/978=4.0%`, unrounded difference about `0.44` percentage points (compatible with `0.4`), and `0.4` lies within `[-2.2, 1.3]`. Row-specific chi-square/Fisher selection and CI construction are absent, so P=.63 is not reconstructed. |
| S055 | **PASS_1_COMPLETE.** DOC-003 p. 3: reclassification row gives `41/863=4.8%`, `45/1174=3.8%`, unrounded difference about `0.92` percentage points (compatible with `0.9`), and `0.9` lies within `[-0.9, 2.7]`. Row-specific test/CI construction is not supplied, so P=.31 is not reconstructed. |

## Pass-1 candidate propositions

### STAT1-CAND-001 — PP day-28-survival printed difference does not reconcile with displayed counts and denominators

- **Category:** Numeric or arithmetic inconsistency / Statistical reporting inconsistency.
- **Exact evidence:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=6`, Table 2, PP day-28 survival: BMV `54/995 (5.4)`; ETI `51/943 (5.4)`; printed BMV-minus-ETI difference `0.1` (95% CI `-10 to 9.7`), P=`.99`.
- **Direct observation:** the counts, denominators, and printed difference occur together in the labelled PP row.
- **Reproducible rule and calculation:** a displayed BMV-minus-ETI percentage-point difference should equal `(54 / 995 - 51 / 943) × 100 = 0.018864...` percentage points. At the table’s one-decimal percentage precision, this is `0.0`, not the printed `0.1`.
- **What was and was not checked:** `0.1` is within the ordered CI, so interval containment does not resolve the discrepancy. P-value and CI-method compatibility were not reconstructed because the table gives only chi-square-or-Fisher alternatives and no row-specific selection/CI construction.
- **Source-grounded alternative interpretation:** the printed counts, denominator, or one-decimal difference may refer to differently retained precision or a differently defined PP analysis set; no such alternative population or calculation is stated in the table or its footnote.
- **Exact human question:** Which of the PP survival counts, denominators, or displayed BMV-minus-ETI difference is intended, and does the analysis dataset contain information not represented by the row’s printed numerator/denominator pairs?
- **Status:** Pending Human Adjudication.

### STAT1-CAND-002 — PP ROSC ETI percentage conflicts with its printed numerator/denominator and with the row’s directionally coherent difference

- **Category:** Denominator, proportion, or total inconsistency / Statistical reporting inconsistency.
- **Exact evidence:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=6`, Table 2, PP ROSC: BMV `342/995 (34.4)`; ETI `377/943 (30.0)`; printed BMV-minus-ETI difference `-5.6` (95% CI `-9.9 to -1.3`), P=`.01`.
- **Direct observation:** `377/943` is printed alongside `30.0%`, while the same row prints a negative BMV-minus-ETI difference.
- **Reproducible rule and calculation:** `(377 / 943) × 100 = 39.9788...%`, which rounds to `40.0%`, not `30.0%`. Also, `(342 / 995 - 377 / 943) × 100 = -5.606932...` percentage points, compatible with the printed `-5.6` and its negative direction. In contrast, the displayed percentages `34.4 - 30.0` imply `+4.4` percentage points, the opposite direction.
- **What was and was not checked:** the printed `-5.6` lies within the ordered CI `-9.9 to -1.3`. P-value/test/CI reconstruction was not performed because Table 2 provides only chi-square-or-Fisher alternatives, no row-specific choice, and no CI construction.
- **Source-grounded alternative interpretation:** `30.0` may be a typographical percentage rather than a different ETI numerator or denominator, because the displayed counts and BMV-minus-ETI difference agree with approximately `40.0%`; the supplied source does not state this explanation.
- **Exact human question:** Is ETI PP ROSC intended to be `377/943 (40.0%)`, or is another printed element of this row based on a different analysis population?
- **Status:** Pending Human Adjudication.

## Display-zero coverage and limitations

- **DISPLAY_ZERO_NOT_CANDIDATE records:** 0. None of the assigned sources displays `P = 0`, `p = 0.000`, or an equivalent finite-precision display zero. `P<.001` and `P<.0001` are threshold displays and were not treated as display zeros or candidates.
- Exact P-value, test-statistic, SE, and CI recalculation was deliberately limited to relationships with supplied compatible model/test/variance definitions. Table 2/Table 3 do not provide row-specific chi-square-versus-Fisher selection or CI construction; protocol/SAP methods are frequently conditional or planned rather than observed.
- No sidedness, degrees of freedom, covariance, variance estimator, multiplicity rule, denominator, model, or estimand mapping was inferred from convention alone.

## Coverage totals

- Assigned and completed relationships: **55/55** (`S001`–`S055`).
- Distinct pass-1 candidate propositions: **2** (`STAT1-CAND-001`, `STAT1-CAND-002`).
- Display-zero records: **0**.
