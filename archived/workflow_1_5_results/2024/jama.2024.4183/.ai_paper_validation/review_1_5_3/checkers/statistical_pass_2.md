# Statistical Consistency Review — Pass 2

- **Runtime agent ID:** `/root/statistics_pass_2`
- **Model / reasoning effort:** `gpt-5.6-terra` / `high`
- **Scope:** `S001`, `S002`, `S003`, `S004`, `S005`, `S006`, `S007`, `S008`, `S009`, `S010`, `S011`, `S012`, `S013`, `S014`, `S015`, `S016`, `S017`, `S018`, `S019`, `S020`, `S021`, `S022`, `S023`, `S024`, `S025`, `S026`, `S027`, `S028`, `S029`, and `S030`; complete `C001`-`C020` ledger and mechanical evidence recheck.
- **Completion:** every assigned relationship is recorded as `PASS_2_COMPLETE` in `statistics/relationship_inventory.md`.

## Method and boundaries

This independent pass revisited all stable inferential relationships against the supplied PDFs, the complete stable ledger, and the mechanical recheck. It reconciled denominator, arithmetic, population, duplicate-value, label/scale, rate/count, figure, and cross-source implications only after matching the printed population, time point, contrast, and measure. Interval/P-value/test/statistic/SE compatibility was not derived where the supplied Bayesian sources omit a compatible test, sidedness, degrees of freedom, covariance, variance estimator, multiplicity rule, or estimator definition. Diagnostic calculations are explicitly labelled below. No conventional finite-precision display-zero P value was found; zero outcome estimates and zero-width CrIs were not treated as P-value displays or candidates.

## Relationship-by-relationship pass-2 record

| S ID | Pass-2 reconciliation with ledger/recheck | Pass-2 result |
|---|---|---|
| S001 | Rechecked model/CrI labels; no compatible frequentist test or SE definition is supplied. | No new candidate; missing definitions retained. |
| S002 | Rechecked counts, ordered CrIs, containment, and CNRT-minus-varenicline direction. | No new candidate. |
| S003 | Reconciled matched abstract/Results/eTable interval strings with C006. | Existing C006 remains the matched-interval issue; no new candidate. |
| S004 | Revisited C005: the abstract's singular following interval has unresolved grammatical scope, while Results/eTable agree for increased CNRT. | No new candidate; scope ambiguity retained. |
| S005 | Rechecked containment/order; NNT derivation and rounding rule remain unsupplied. | No new candidate. |
| S006 | Reconciled raw 0% versus 3%, main negative RD, benefit wording, and eTable positive ARD with C007. | Existing C007; no new candidate. |
| S007 | Rechecked the 24% versus 23% matched upper CrI endpoints with C008. | Existing C008; no new candidate. |
| S008 | Rechecked containment/order and label; NNT convention remains unsupplied. | No new candidate. |
| S009 | Rechecked the -5% versus -4% matched lower CrI endpoints with C009. | Existing C009; no new candidate. |
| S010 | Rechecked cell and ARD narrative strings against eFigure 2/eTable 9 and C014/C016. | Existing C014 and C016; no new candidate. |
| S011 | Rechecked 8% cell, ordered figure CrI, and narrative `5.0%-1.1%` with C015. | Existing C015; no new candidate. |
| S012 | Rechecked zero outcome estimates and zero-width CrIs as outcome results, not P values. | No new candidate. |
| S013 | Rechecked all three narrative `5.0%-1.1%` occurrences against figure/tables and C017. | Existing C017; no new candidate. |
| S014 | Rechecked increase-minus-switch label, direction, containment, and interval order. | No new candidate. |
| S015 | Rechecked increase-minus-switch label, direction, containment, and interval order. | No new candidate. |
| S016 | Rechecked C018. Also found the page-10 phase-1-abstainer summary directs readers to ETable 10, whereas ETable 11 is the printed phase-1-abstainer table. | Existing C018 plus new pass-2 record P2-NEW-01. |
| S017 | Rechecked detailed six-month CNRT-switch values and the erroneous ETable 7 cross-reference with C019. | Existing C019; no new candidate. |
| S018 | Rechecked containment, order, label, and stated continuation reference. | No new candidate. |
| S019 | Rechecked zero outcome estimates and zero-width CrIs as outcomes, not P values. | No new candidate. |
| S020 | Rechecked containment, order, label, and stated continuation reference. | No new candidate. |
| S021 | Rechecked increase-minus-switch label, direction, containment, and interval order. | No new candidate. |
| S022 | Rechecked the six-month VAR-plus-versus-switch statement. It cites ETable 9 for a switch comparison, while ETable 10 is the printed switch-reference table. | New pass-2 record P2-NEW-02. |
| S023 | Rechecked C020's narrative noncontainment, scale mismatch, direction/reference ambiguity, and probability difference. The incorrect phase-1-abstainer ETable 10 summary cross-reference is also P2-NEW-01. | Existing C020 plus P2-NEW-01; no additional candidate. |
| S024 | Rechecked all six GEE probabilities within ordered frequentist CIs; did not impose posterior compatibility. | No new candidate. |
| S025 | Rechecked IPW-rate/count distinction and estimate containment in ordered CrIs. | No new candidate. |
| S026 | Rechecked IPW-rate/count distinction, labels, and ordered CrIs; no variance or multiplicity convention inferred. | No new candidate. |
| S027 | Rechecked planned Bayesian model/contrast labels; no publication-version crosswalk is supplied. | No new candidate. |
| S028 | Rechecked C010. **Diagnostic approximation:** printed Beta(785,869) has mean 0.4746, not the paired 0.50 label. | Existing C010; no new candidate. |
| S029 | Rechecked all planned simulated estimates within ordered intervals. | No new candidate. |
| S030 | Rechecked Table 3 containment/order, the Aim-1 threshold-power sequence in C011, and duplicate Aim-2 comparator label in C012. The same-simulation/nested-detection definition needed to force monotonicity remains unsupplied. | Existing C011 and C012; no new candidate. |

## New pass-2 candidate records — no C ID assigned

### P2-NEW-01 — Phase-1-abstainer secondary-outcome summary cites the nonabstainer comparison table

- **Primary category:** Measure, label, or scale inconsistency
- **Exact source locations:** [Supplement 2 PDF p. 10](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=10>); [Supplement 2 ETable 10, PDF p. 34](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=34>); [Supplement 2 ETable 11, PDF p. 35](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=35>).
- **Direct observation:** The page-10 summary says phase-1 abstainers had an EOT+30 CNRT-versus-varenicline difference and no six-month difference, then directs readers to `E-Table 10`. ETable 10 is explicitly the phase-2 switch-versus-increase comparison among week-6 nonabstainers. ETable 11 is explicitly the phase-1-abstainer CNRT-versus-VAR table and prints the cited EOT+30 and six-month comparison results.
- **Consistency rule:** A source cross-reference for a stated population and comparison must identify the table carrying that population and comparison.
- **Mechanical comparison:** ETable 10 has nonabstainer CNRT-plus-versus-switch and VAR-plus-versus-switch columns; it has no phase-1-abstainer CNRT-versus-VAR row. ETable 11 has `ARD For CNRT vs. VAR` for phase-1 abstainers with EOT+30 11% (-1% to 22%), 97%, and six months 1% (-11% to 12%), 56%.
- **Necessary inputs / missing definition:** The printed summary and table titles/rows are sufficient. No source supplies a table-number version history that would explain the citation.
- **Alternative source-grounded interpretation:** `E-Table 10` may be an obsolete or transposed table number.
- **Direct observation versus inferred explanation:** The page-10 citation and table scopes are direct observations. An obsolete/transposed number is an inferred explanation.
- **Exact remaining human question:** Should the phase-1-abstainer summary on Supplement 2 PDF page 10 cite ETable 11 rather than ETable 10?

### P2-NEW-02 — Six-month VAR-plus-versus-switch statement cites the continuation-comparison table

- **Primary category:** Measure, label, or scale inconsistency
- **Exact source locations:** [Supplement 2 PDF p. 12](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=12>); [Supplement 2 ETable 9, PDF p. 33](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=33>); [Supplement 2 ETable 10, PDF p. 34](<../../../joi240036supp2_prod_1716416466.01349.pdf#page=34>).
- **Direct observation:** The six-month VAR-nonabstainer narrative gives VAR-plus ARD 2.0% (1.0%-5.0%) relative to both continuation `(see E-Table 9)` and switching to CNRT `(see E-Table 9)`. ETable 9 defines comparisons of each rescue strategy versus continuation. ETable 10 defines switch as reference and prints VAR-plus versus CNRT switch as 2% (1%-5%), probability greater than 99%.
- **Consistency rule:** A source cross-reference for the stated switch-reference contrast must identify the table that defines and reports that contrast.
- **Mechanical comparison:** ETable 9 contains VAR-plus versus VAR continuation, 2% (1%-5%), but no VAR-plus-versus-CNRT-switch contrast. ETable 10 contains the latter contrast with the same printed 2% (1%-5%) values.
- **Necessary inputs / missing definition:** Narrative text, contrast labels, reference definitions, and matching table values are supplied. No document-version history is supplied.
- **Alternative source-grounded interpretation:** The second `E-Table 9` may be a repeated citation where `E-Table 10` was intended.
- **Direct observation versus inferred explanation:** The duplicated ETable 9 citation and table contrast scopes are direct observations. A repeated-citation mechanism is inferred.
- **Exact remaining human question:** Should the switch-to-CNRT clause on Supplement 2 PDF page 12 cite ETable 10 rather than ETable 9?

## Totals and limitations

- **Stable inferential relationships revisited:** 30 of 30, `S001` through `S030`.
- **Stable ledger/recheck IDs reconciled:** 20 of 20, `C001` through `C020`.
- **New pass-2 candidate records:** 2 (`P2-NEW-01`, `P2-NEW-02`), intentionally without C IDs for coordinator registration and required mechanical recheck.
- **Display-zero P-value records:** none. Coherent zero outcome estimates and zero-width CrIs were not candidates.
- **Limitations:** Bayesian result reporting lacks compatible conventional P values, test statistics, SEs, degrees of freedom, sidedness, covariance, variance estimators, and posterior draws for independent inferential reconstruction. NNT derivation/rounding and a protocol-to-publication version crosswalk are not supplied. Missing definitions are not inferred from convention.
