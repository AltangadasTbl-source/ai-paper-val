# Statistical Consistency Review — Pass 1

## Completed scope

Independent pass-1 review of every canonical inferential relationship `S001` through `S035` in `statistics/relationship_inventory.md`, covering all four supplied PDFs and all direct-source locations mapped in the current run. No legacy candidate, verification, critic, or final-report artifact was used as scientific input.

- **Relationships completed:** 35/35 (`S001-S035`), each explicitly marked `PASS_1_COMPLETE` in the canonical inventory.
- **Complete relationship enumeration:** S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035.
- **Candidate records emitted without C IDs:** 2 (`SP1-CAND-001`, `SP1-CAND-002`).
- **Display-zero result review:** No observed result displayed `P = 0`, `p = 0.000`, or equivalent; therefore no `DISPLAY_ZERO_NOT_CANDIDATE` record was needed.

## Check record

| Check domain | Relationships checked | Result |
|---|---|---|
| Point-estimate containment and endpoint order | S003-S024, S027-S030 | Every displayed estimate lay within its correctly ordered displayed CI. |
| Null/sign/direction and effect-measure/scale labels | S002-S024, S027-S035 | RR/RD/MD/ratio labels, stated nulls, reference groups, and directions were compatible within each result and across repetitions, except the planned-versus-final analysis descriptions recorded as the two candidates. |
| Cross-location repetitions | S001-S004, S008-S010, S013-S015, S027-S032 | Matched final, narrative, table, figure, and supplement values agreed at displayed precision. |
| Interval/P/test/statistic/SE compatibility | S001-S014, S025, S027-S030 | Qualitative null/CI/P agreement holds for every result with a printed P. Exact algebraic reconstruction was not claimed where SE, df, final covariance, variance estimator, or convergence/fallback choices were missing. The labelled log-RR and normal-CI diagnostics in the inventory found no independent contradiction. |
| Planned-versus-final model specifications | S007, S026, S034-S035 | Two source-grounded differences in model/effect-measure specifications were retained as separate candidates; no unsupported explanation was inferred. |
| Display-zero exclusion | All observed P-value relationships | No coherent display-zero P value was present; no candidate was generated on that basis. |

## Candidate handoff (no C IDs)

1. `SP1-CAND-001`: SAP unstructured covariance plus robust sandwich SE versus final-article independent covariance for the SF-12/EQ-5D longitudinal model family. See S026.
2. `SP1-CAND-002`: SAP/protocol LOS adjusted mean-difference (or skewed unadjusted median-difference) plan versus final article’s log-transformed adjusted ratio of geometric means. See S007.

Both records are **Pending Human Adjudication**. They state direct supplied-source comparisons and the missing definition; they do not assign validity, severity, acceptance, rejection, or a correction.

## Limitations carried forward

The supplied package does not provide final fitted-model SEs, degrees of freedom, covariance estimates, variance-estimator output, convergence/fallback selections, or numerical tipping-point data. These omissions prevent exact CI/P/test-statistic reconstruction and preclude inference from convention alone. They do not suppress the two directly observed planned-versus-final reporting differences.
