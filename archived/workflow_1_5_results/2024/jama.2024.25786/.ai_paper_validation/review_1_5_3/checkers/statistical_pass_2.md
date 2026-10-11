# Statistical consistency review — pass 2

## Completion record

- **Runtime agent ID:** `/root/statistics_pass_2`
- **Configured role/model/effort:** fresh `statistics_pass_2`; `gpt-5.6-terra`; `high`.
- **Exact scope:** S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, and S036 in `statistics/relationship_inventory.md`; complete C001-C008 ledger; and all direct-source facts in `verification/evidence_recheck.md`.
- **Relationship count:** 36; every S record is explicitly marked `PASS_2_COMPLETE` in the relationship inventory.
- **Existing-ledger reconciliation:** C001-C008 were all considered. No existing stable ID was suppressed, reclassified, adjudicated, or assigned a correction.
- **New candidate-observation count:** 0. No new distinct candidate observation was emitted.
- **Evidence authority:** the supplied PDFs. Durable maps, the ledger, and the recheck artifact were used to identify comparisons; the main article Figure 2/methods, eTables 4-11, and final SAP method pages were re-read from the direct PDFs.

## Complete pass-2 relationship reconciliation

| S scope | Pass-2 checks applied | Result and ledger/recheck implication |
|---|---|---|
| S001-S002 | Population, model, CI/test, BH, planning, sample-size, and interim-definition comparison across the final report, protocol, and SAP | Versioned planning material remains distinct from observed results. No power, alpha-spending, or exact estimator definition supports a new reconstruction. C001-C002 and C006-C007 are numeric/flow presentations, not compatible inferential comparators. |
| S003-S005 | Point-estimate containment; CI ordering; OR sign/direction against counts; effect labels; CI/P diagnostic only under supplied two-sided 95% CI/model definitions; Figure 2 cross-location/risk-difference assessment | OR/CI/P relationships remain diagnostic-compatible, with GEE/IPW limits retained. C003 is an existing conditional adjusted-CI observation: eTable 4 says 0.68-1.41 and eTable 7 says 0.68-1.39, while table-specific model identity is absent. Figure 2 risk differences do not reproduce adjacent crude risks under one orientation, but the source does not say they are crude or define their estimator; this is a missing-definition limitation, not a candidate. |
| S006-S014 | Denominators, outcome windows, count/risk/OR labels, endpoint order, sign/direction, duplicate values, P/CI diagnostics, and BH implications | No new observation. Hypoxemia FDR is not reconstructed; explicitly eligible postdischarge-pneumonia denominators are retained. The 0.0% myocardial-infarction count is not a P-value display zero. |
| S015 | Continuous-outcome scale/unit, median-versus-mean-difference label, CI containment/order, sign, and P diagnostic | No new observation. The variance estimator and row-level model details are not supplied, so diagnostic normal approximations remain only diagnostics. |
| S016-S021 | All-patient and subgroup denominators, event rates, OR/CI directions, adjusted labels, Figure 4/eTable 7 repetitions, interaction P definitions, and C003-C005 implications | C004 and C005 remain existing direct raw-percentage/cross-location observations. C003 remains conditional because its adjusted-model definition is absent. No interaction P is recalculated: model term, statistic, degrees of freedom, covariance, and variance information are not supplied. |
| S022-S024 | Per-protocol definition, group headers versus outcome denominators, counts, OR/CI labels/direction, and P diagnostics | No new observation. The source does not assert equality between group headers and outcome-specific denominators. |
| S025-S028 | Sensitivity population definition, counts, CI ordering, OR direction, P diagnostics, text duplication, and C008 implications | C008 remains an existing notation observation: the direct source prints `135//750`, while 135/750 is compatible with 18.0%. It is independent of P-value formatting. No additional inferential discrepancy is observed. |
| S029 | AE/SAE population and descriptive zero percentage check | No new observation. These descriptive zeros are not inferential P-value display zeros. |
| S030-S035 | Planned/final model, population, missingness, multiplicity, estimator, scale, and monitoring definition comparison | No new observation. S030-S031 are planning-only; S032-S034 lack row-level adjusted-P/variance/model-matrix inputs where needed; S035 is a monitoring definition, not an observed effect. |
| S036 | P-value display-zero search and independent-contradiction test | No supplied inferential `P = 0`, `p = 0.000`, or equivalent was found. `DISPLAY_ZERO_NOT_CANDIDATE` is not applicable because there is no P-value display zero; no tail probability or threshold was derived. |

## Reconciliation of every existing ledger item

| Existing ID | Relevant S relationship(s) | Pass-2 treatment |
|---|---|---|
| C001 | S001, S029 context only | Direct eTable 2 count/denominator/percentage mismatch is distinct baseline arithmetic. It supplies no compatible model-based inference input and yields no new S observation. |
| C002 | S001, S029 context only | Direct eTable 2 zero-numerator/nonzero-percentage mismatch is distinct baseline arithmetic. It is not a P-value display zero and yields no new S observation. |
| C003 | S003, S016, S033 | Direct recheck facts record the two printed upper limits. The model-equivalence definition is still absent; it remains an existing conditional cross-location observation, with no P-value/SE reconstruction. |
| C004 | S018 | Direct recheck facts record `48/473 (10.1)` versus `48/473 (9.2)`. This raw percentage issue does not disturb OR/CI containment or permit interaction-P calculation. |
| C005 | S019 | Direct recheck facts record `14/69 (20.3)` versus `14/69 (20.2)`. This raw percentage issue does not disturb OR/CI containment or permit interaction-P calculation. |
| C006 | S001, S032 context only | The eTable 10/Figure 1 postrandomization flow discrepancy has a stated eight-person pattern but no printed table population rule. It supplies no reason to replace an mITT, per-protocol, or outcome denominator. |
| C007 | S001, S032 context only | The eTable 10 secondary-exclusion cells combine a within-group denominator with a cross-group partition percentage. The intended flow estimand remains unspecified and is not imported into outcome models. |
| C008 | S026 | Direct recheck facts record the doubled separator. The count/percentage arithmetic and reported sensitivity OR/CI/P remain separately compatible. |

## Limitations and inferential boundaries

- No sidedness, degrees of freedom, covariance, variance estimator, multiplicity threshold, denominator, model, or estimand mapping was inferred from convention alone.
- Where source text supplied two-sided 95% CI/model definitions but GEE/IPW and row-level inputs prevented replication, interval/P-value calculations remained labelled diagnostics; they were not used as reconstructed analyses.
- Interaction P values lack a printed interaction term, test statistic, degrees of freedom, covariance, and variance details. They were not recomputed.
- Figure 2 risk differences do not reproduce the adjacent crude event risks under a common direction, but the source does not state that they are crude and does not supply a risk-difference estimator, adjustment, standardization, or CI method. This is a precisely recorded missing-definition limitation, not an independent supplied-source contradiction or candidate.
- The complete C001-C008 mechanical recheck provides facts about printed values and missing definitions, not an adjudication. This pass assigns no severity, validity, Verified, Rejected, Uncertain, acceptance, correction, or final disposition.
- There are no supplied inferential display-zero P values. No tiny positive tail probability was derived, and no candidate is based on finite-precision zero notation.

## Per-relationship pass-2 completion index

+- S001: PASS_2_COMPLETE
- S002: PASS_2_COMPLETE
- S003: PASS_2_COMPLETE
- S004: PASS_2_COMPLETE
- S005: PASS_2_COMPLETE
- S006: PASS_2_COMPLETE
- S007: PASS_2_COMPLETE
- S008: PASS_2_COMPLETE
- S009: PASS_2_COMPLETE
- S010: PASS_2_COMPLETE
- S011: PASS_2_COMPLETE
- S012: PASS_2_COMPLETE
- S013: PASS_2_COMPLETE
- S014: PASS_2_COMPLETE
- S015: PASS_2_COMPLETE
- S016: PASS_2_COMPLETE
- S017: PASS_2_COMPLETE
- S018: PASS_2_COMPLETE
- S019: PASS_2_COMPLETE
- S020: PASS_2_COMPLETE
- S021: PASS_2_COMPLETE
- S022: PASS_2_COMPLETE
- S023: PASS_2_COMPLETE
- S024: PASS_2_COMPLETE
- S025: PASS_2_COMPLETE
- S026: PASS_2_COMPLETE
- S027: PASS_2_COMPLETE
- S028: PASS_2_COMPLETE
- S029: PASS_2_COMPLETE
- S030: PASS_2_COMPLETE
- S031: PASS_2_COMPLETE
- S032: PASS_2_COMPLETE
- S033: PASS_2_COMPLETE
- S034: PASS_2_COMPLETE
- S035: PASS_2_COMPLETE
- S036: PASS_2_COMPLETE
