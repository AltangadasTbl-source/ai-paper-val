# Statistical Consistency Review — Pass 2

## Scope and method

This independent pass revisited every registered inferential relationship, S001 through S021, after review of the complete numeric relationship inventory, numeric and cross-source checker artifacts, stable candidate ledger C001-C006, and mechanical evidence recheck. The supplied PDFs remain authoritative; direct-page confirmation was repeated for the result-bearing C001, C004, C005, and C006 locations. This pass neither assigns candidate IDs nor adjudicates existing candidates. All existing ledger entries remain Pending Human Adjudication.

Pass-2 checks covered point-estimate containment, endpoint ordering, sign/direction, effect-measure and scale labels, denominator/arithmetic implications, duplicate/cross-location values, and test/interval/P/SE/statistic compatibility only where the package supplies compatible definitions. Calculations from rounded values are expressly diagnostic. No sidedness, degrees of freedom, covariance, variance estimator, multiplicity sequence, denominator, model, or estimand mapping was inferred from convention alone.

## Per-relationship completion records

| S ID | Pass-2 cross-lane and recheck review | Result | Existing ledger implication | Status |
|---|---|---|---|---|
| S001 | Model, population, contrast, adjustment, and scale definitions against numeric and cross-source records | No supplied mismatch; covariance/variance and simultaneous-CI definitions remain absent | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S002 | HR/CI containment and ordering; direction; abstract/narrative repetition; randomized denominator | HR 0.25 remains within 0.13-0.48 and agrees with reduced relapse direction; no same-test reconstruction beyond diagnostic precision | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S003 | Covariate HR/CI/P vectors, reference contrasts, and cross-location context | All displayed HRs remain within ordered CIs and have compatible displayed direction; model-specific variance details absent | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S004 | Figure direction, at-risk/count context, and distinction from adjusted primary HR | Log-rank result is a distinct unadjusted comparison; no numeric CI-band coordinates or statistic supplied | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S005 | Sensitivity HR/CI/P vector and analysis-population distinction | HR 0.22 remains within 0.11-0.43 with compatible direction; seven-person exclusion makes it nonduplicate of S002 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S006 | Eight estimates/CIs, adjusted-P labels, table scale, and repeated abstract/Results text | Containment/order and direction hold. HbA1c's mg/dL-versus-percent scale conflict is retained; adjusted P values are not forced to equal uncharacterized CIs | C001 retained | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S007 | Estimate/CI, score construction, and adjusted-P/model context | Containment/order/direction hold; the stated 0-40 versus 0-36 constructions are not a scale contradiction; no compatible exact P calculation | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S008 | Sixteen within-arm change intervals, raw-summary caveat, and estimand labels | All point estimates remain within ordered CIs. Raw changes are not equated to marginal subtraction because the table names missing-data differences; no paired inputs supplied | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S009 | Four risk-difference intervals, arm counts/percentages, exact-CI labels, and Table 5 arithmetic | Interval containment/order and direction hold. The independently printed Total-cholesterol and LDL point differences do not reconcile with their stated raw proportions; no unprinted denominator is assumed | C002, C003 retained | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S010 | Missing-data and pattern-mixture wording against reported results | No inferential vector is supplied; no model-output comparison can be performed | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S011 | Medication-change sensitivity population and qualitative conclusion | Definition and qualitative result are present, but no estimate/CI/P/statistic is printed | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S012 | Power inputs, revised target, and enrollment context | Revision statement is coherent; alpha, assumed control risk, allocation, attrition handling, and calculation details are missing | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S013 | Two-sided and Holm labels against secondary-outcome reporting | Labels remain coherent. CI-adjustment construction and Holm sequence are not printed, so P/CI equality is not imposed | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S014 | Bayesian/frequentist effect types, interval types, ARD sign, risk/rate labels | HR/CrI, RR/CI, ARD, and rates remain differentiated; no unprinted variance/formula is derived | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S015 | All 44 DIC/I2/model entries against the printed model-selection rule and recheck | Forty-three selections remain reproducible at display precision. The all-patient Incident Cancer row remains nonreproducible from the displayed strict threshold and values; unrounded I2 is absent | C004 retained | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S016 | ARD signs/intervals, conditional NNT/NNH display, endpoint/rate labels | Ordered intervals and stated conditional display rule hold. Rounded reciprocal checks remain diagnostics because model-weighted risks and full precision are unavailable | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S017 | Estimate/SE/t/P vector and the mechanical recheck's nearest-hundredth interval test | The recheck controls the pass-1 diagnostic disagreement: conditional on the displayed estimate and SE being the t-test inputs, their ordinary nearest-hundredth intervals give an absolute t ratio from 0.600 through below 0.621, which cannot display as 0.59. The figure lacks the exact test/parameter definition, df, sidedness, and unrounded inputs; no P reconstruction is made | C005 retained; no new proposal | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S018 | HR/CrI containment, endpoints, total-stroke population, and precision footnote | Containment/order and direction hold. The explicit 1.004 footnote resolves the printed 1.00 upper endpoint; no display issue is proposed | C006 cross-lane context retained | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S019 | Forest RR/CI containment, fixed/random and endpoint labels, total-stroke duplicate ASCEND vector | RR/CI containment/order and labels hold. The total-stroke ASCEND endpoint-membership/count issue remains a cross-source conflict; no Q or df is supplied for heterogeneity-P checks | C006 retained | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S020 | Sensitivity HR/CrI containment, analysis N/study labels, and finite precision | Containment/order hold. The MI <=100-mg/day upper endpoint is explicitly 0.9989, so its 1.00 display is coherent rounding | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S021 | All-stroke definition, 12-versus-13 study count, denominators, duplicate ASCEND forest row, and recheck arithmetic | Each forest-minus-table arm total is exactly 7,740, the ASCEND per-arm denominator. A frequentist endpoint convention allowing ischemic-only ASCEND under Total stroke is not supplied | C006 retained | PASS_1_COMPLETE; PASS_2_COMPLETE |

## C005 pass-1 diagnostic reconciliation

Pass 1 described the ratio from rounded Egger inputs as compatible with `t=-0.59`; that conclusion is not supported under the ordinary nearest-hundredth display convention mechanically checked for C005. For a displayed estimate magnitude from 0.465 through below 0.475 and a displayed SE from 0.765 through below 0.775, the attainable absolute ratio is 0.600 through below 0.621. A two-decimal t displayed as 0.59 requires 0.585 through below 0.595. The intervals do not overlap.

This is a diagnostic conditional on the figure's adjacent estimate and SE being the numerator and denominator for the printed t statistic. The page does not supply the exact Egger regression/test definition, the unrounded inputs, degrees of freedom, sidedness, or confirmation that the stated SE is that t statistic's SE. Therefore pass 2 retains the existing C005 source-grounded reporting-consistency candidate and its stated human question; it does not derive a P value or assert an unexplained mechanism.

## Candidate and display-zero record

- **Existing ledger IDs reviewed:** C001, C002, C003, C004, C005, and C006. Their source facts and remaining human questions are retained; pass 2 adds no adjudication or disposition.
- **Genuinely new candidate proposals:** 0. No distinct contradiction beyond C001-C006 was found after complete cross-lane review.
- **DISPLAY_ZERO_NOT_CANDIDATE records:** 0. No S001-S021 relationship prints `P = 0`, `p = 0.000`, or an equivalent display zero. `P < .001` values were not converted into reconstructed tail probabilities.

## Limitations

The supplied sources do not provide the missing unrounded I2, Egger test definition/unrounded inputs/df/sidedness, covariance or variance-estimator details, simultaneous-CI construction, Holm sequence and CI adjustment rule, Table 4 paired inputs, Table 5 measure-specific denominators, power-calculation inputs, or a frequentist total-stroke ASCEND endpoint convention. These missing definitions bound the compatibility checks but do not erase direct printed comparisons.
