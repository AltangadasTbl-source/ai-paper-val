# Cross-Source Quantitative Consistency Review

## Scope and method

This review independently reconciled the fresh mappings for all direct sources: DOC-001 main article (PDF pp. 1-10), DOC-002 protocol/SAP supplement (PDF pp. 1-69), and DOC-003 multiple-imputation eTable (PDF pp. 1-2). It reviewed numeric/reporting relationships `N001`-`N059` and inferential relationships `S001`-`S051` where a cross-location comparator exists. Matches were made only after checking population, analysis set, endpoint/time point, contrast direction, method/model, scale/unit, and displayed precision. The cited PDFs are supplied package evidence.

## Complete matched-result coverage

| Matched scope | Exact source locations checked | Result |
|---|---|---|
| Randomization, flow, analysis populations, baseline counts/percentages, primary and secondary hospital outcomes, further procedures, survival, adverse events, figures, captions, table notes, and narrative/abstract repetitions (`N001`-`N031`; `S001`-`S033`) | [DOC-001 pp. 1-9](../../../jama_thomas_2017_oi_170130.pdf#page=1) | Matched repetitions were consistent after stated rounding, endpoint definitions, and analysis-set distinctions, except the separate Table 1 percentage proposition below. |
| Original and final protocol, amendment history, original SAP definitions, analysis rules, and output shells (`N032`-`N054`; `S034`-`S050`) | [DOC-002 pp. 1-69](../../../joi170130supp1_prod.pdf#page=1) | Planned versus observed material was kept distinct. Blank flow/table shells with `X`, `Y`, and `n=...` placeholders were not compared as results. One cross-document sample-size-design discrepancy is recorded below. |
| MI ITT eTable, matched main Table 2 values, missing-data statements, scales, and 15 estimate/CI/P-value rows (`N055`-`N059`; `S051`) | [DOC-003 p. 2](../../../joi170130supp2_prod.pdf#page=2); [DOC-001 pp. 3, 6, 8](../../../jama_thomas_2017_oi_170130.pdf#page=3) | No observed-result contradiction. DOC-003 uses 20 chained-equation MI data sets and prints IPC-minus-talc estimates; DOC-001 Table 2 is the non-MI/primary display and its arithmetic signs correspond to talc-minus-IPC. After contrast reversal and method matching, differences in printed estimates, CIs, and P values are expected and not candidate propositions. |

## Non-candidate reconciliations retained

- Abstract, Results, Table 2, Figure 2, and captions consistently identify the primary ITT hospital-day comparison as IPC `n=73` versus talc `n=71`, with medians `10` versus `12` days and HL location shift `2.92` days (95% CI `0.43-5.84`; `P=.03`).
- The main article’s total, effusion-related, non-effusion-related, initial-admission, and post-hoc initial-hospital-admission measures are not interchangeable. In particular, the initial-admission results on DOC-001 pp. 5 and 8 have separately stated definitions and were not treated as the same result.
- The protocol’s historical block allocation and early `0.5-0.7` minimization probability are historical/planned specifications. The final protocol records the later `0.8` probability after regional stratification; the main article’s `0.5-0.8` range is compatible with that sequence.
- The final protocol’s minimum six-month follow-up wording and the SAP/main article’s 12-month-or-death outcome horizon do not establish a conflicting observed follow-up result: the former states a minimum follow-up/schedule, while the latter defines the analysis horizon.
- The supplementary MI eTable’s 15 differences reconcile with its displayed arm estimates to printed precision. Its direction is IPC minus talc; the main table’s displayed signs are the reverse direction. The main article explicitly describes MI as a sensitivity analysis for missing VAS/EQ5D data. These are different estimation procedures, not conflicting observations.
- No display-zero P value was used as a candidate proposition.

## Qualifying candidate propositions for human adjudication

### Proposition A — Final-protocol and SAP/main sample-size inputs conflict despite the same 146-participant target

**Category:** Cross-document numeric inconsistency.

**Exact source locations:** [DOC-002 final protocol, PDF p. 37](../../../joi170130supp1_prod.pdf#page=37); [DOC-002 SAP, PDF p. 62](../../../joi170130supp1_prod.pdf#page=62); [DOC-001 Methods, PDF p. 3](../../../jama_thomas_2017_oi_170130.pdf#page=3).

**Printed values:** The final protocol states that `62` patients per group give 80% power for `0.54` standard deviations at two-sided 5%, that this is about `5` days based on `18` days post-pleurodesis, and that a `20%` lost-to-follow-up allowance adds `24` patients for target `146`. The SAP instead states `65` per group, 80% power and alpha `.05`, a `≥5`-day difference, `18` days and SD `9.3`, and a `12%` allowance yielding `73` per group/`146` total. DOC-001 repeats the SAP/main values: `65` per group, `18` days, SD `9.3`, and `12%` loss allowance for target `146`.

**Comparison logic:** These are both stated sample-size calculations for the same named AMPLE trial and same target of 146, but they use incompatible per-group base sample sizes and attrition allowances (`62` with `20%` versus `65` with `12%`). They cannot both be the single contemporaneous calculation underlying the reported target without an intervening revision.

**Direct observation versus inference:** Directly observed is the printed parameter mismatch. The possible explanation that the SAP revised or superseded the final protocol is an inference; the supplied pages reviewed here do not explicitly connect the two parameter sets with a versioned replacement statement.

**Supported source-grounded alternatives:** The final protocol predates the SAP and may preserve an earlier calculation; the SAP and main article may be the governing analysis/reporting plan. The unchanged total target of 146 may reflect a deliberate redesign rather than a reporting transcription error.

**Human verification steps:** Check the protocol amendment/version history and trial-master records for a dated replacement of the 62-per-group/20% calculation; confirm which calculation was approved and governed recruitment; then determine whether the main article needs a clarification of the relationship between final protocol and SAP.

### Proposition B — Table 1 talc-arm ECOG “unknown” percentage does not match its displayed count and denominator

**Category:** Denominator, proportion, or total inconsistency.

**Exact source location:** [DOC-001 Table 1, PDF p. 4](../../../jama_thomas_2017_oi_170130.pdf#page=4).

**Printed values:** The talc arm is labelled `n=72`. Its ECOG rows are `53 (74)` for score 0-2, `14 (19)` for score 3-4, and `5 (17)` for unknown.

**Comparison logic:** `5/72 × 100 = 6.94%`, which rounds to `7%`, not `17%`. The three displayed counts sum to 72, so the arm denominator is available and the count cannot be reconciled with the printed percentage. By contrast, the other two talc percentages are consistent with their displayed counts to rounding (`53/72≈74%`, `14/72≈19%`).

**Direct observation versus inference:** The direct observation is an incompatible count/percentage pair in one table cell. Whether `17` is a typographic percentage, whether the count is incorrect, or whether another denominator was intended is not established by supplied evidence.

**Supported source-grounded alternatives:** If the percentage was intended to be `7`, the row and arm total reconcile. If `17%` was intended, a count near 12 would be expected, but that would no longer reconcile with the three printed counts summing to the labelled `n=72`.

**Human verification steps:** Verify the source baseline dataset or table-production record for talc-arm ECOG unknown status; confirm the intended numerator and denominator; correct only after that source check. This proposition overlaps the within-table arithmetic lane and should be merged with that lane only if its printed values, comparator, and rule are identical.

## Outcome and limitations

Two distinct candidate propositions were identified: one planned-document sample-size discrepancy and one Table 1 count/percentage discrepancy. All other matched observed results reconciled under their supplied population, endpoint, analysis, contrast, scale, or precision context. This is a source-based quality-control review, not an adjudication of validity or a correction.
