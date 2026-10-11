# Statistical Pass 1 Checker

## Completion record

- **Pass:** 1 of 2.
- **Scope:** every inferential relationship assigned from all 40 direct-source pages: D001 pp. 1-9, D002 pp. 1-15, and D003 pp. 1-16.
- **Relationships checked:** 25 stable records, `S001` through `S025`; each record is marked `PASS_1_COMPLETE` in `statistics/relationship_inventory.md`.
- **Candidate-discovery count:** 0. No independent supplied-source contradiction was identified. This checker assigns no candidate IDs and makes no adjudication, severity, validity, or correction statement.

## Mechanical pass-1 summary

| Check domain | Applied relationships | Result |
|---|---|---|
| Point estimate containment and endpoint order | S004-S007, S009-S010, S013, S020, S024 | Every displayed point estimate was within correctly ordered displayed interval endpoints. |
| Sign/direction, reference, measure, and scale labels | S001-S025, where an estimate/definition was supplied | No conflicting direction, reference group, effect-measure, outcome, time point, or scale label was observed for a matched result. |
| Cross-location repetitions | S004, S006-S012, S015, S018-S020, S024-S025 | Matched main/protocol/supplement repetitions agree after population, outcome, analysis, and contrast were matched. Planned-versus-final covariate adjustment is recorded as definition-limited, not contradictory. |
| Formula and arithmetic checks supplied by source | S009-S010, S019, S022, S024 | Printed percentage differences, fractions, and eTable 3 formula values reconcile at the source's displayed precision. eTable 3's three one-hundredth subtraction appearances are compatible with independent rounding of P1/P0. |
| Interval/P/test/statistic/SE compatibility | S003-S007, S009-S011, S013, S018-S025 | Applied only qualitatively when the matched source supplied an estimate, interval, and P label. Exact numerical reconstruction was not performed where test, sidedness, degrees of freedom, variance estimator, covariance, confidence-interval construction, multiplicity family, weighting, or imputation-combination definitions were absent. |
| Display-zero exclusion | S001-S025 | No mapped relationship displays `P = 0`, `p = 0.000`, or equivalent. `.0001` and `<.0001` are nonzero printed values. No display-zero candidate was emitted. |

## Definition-limited relationships

- **S001:** sample-size formula inputs beyond the printed planning values are absent.
- **S002, S003, S004-S007, S009-S011, S013, S019-S020, S023-S025:** exact test and/or CI construction, sidedness, degrees of freedom, variance estimator, covariance, or model-estimand mapping is not fully supplied.
- **S014:** the final text does not specify a covariate set; this does not establish an adjusted-versus-unadjusted conflict with the protocol plan.
- **S016:** no completed mediation estimate is supplied.
- **S017-S018, S022:** MI test/variance-combination definitions are incomplete for a numerical P reconciliation.
- **S021 and S025:** eAppendix D identifies logistic interaction betas, SEs, and P values but not the test distribution/sidedness/degrees of freedom/variance estimator. A beta/SE normal-tail calculation would be a diagnostic approximation only and was not used as a candidate basis.

## Pass-1 observation log

1. Main ITT and repeated PPA RDs, RRs, ORs, 95% CIs, P thresholds, and repeated abstract/table/discussion statements are internally concordant for their stated estimands.
2. CCA and IPRW estimates are consistently distinguished from missing=vaping ITT estimates; matching values repeat between the main article, eAppendix C, and eTable 5.
3. The MI grid supplies its own rate-difference/RR/OR formulas. Its values reconcile at displayed precision; no independent contradiction beyond ordinary rounding was observed.
4. The moderation supplement uses explicitly labelled nominal and Holm-adjusted P values. It supports, rather than conflicts with, the main-paper statement that no moderator remained statistically significant after Holm adjustment.

## Per-relationship completion index

S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, and S025 each received a `PASS_1_COMPLETE` record in the statistical relationship inventory.

## Limitations

- This is a pass-1 statistical consistency inventory, not an inference that unreported model details follow a conventional method.
- No web, external literature, old candidate ledger, prior checker, verifier, critic, endetail, or final report was used as scientific input.
- Pass 2 must use a different fresh Terra/high runtime agent and revisit every stable relationship with the complete cross-lane candidate ledger and mechanical recheck facts.
