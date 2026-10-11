# Statistical Consistency Review — Pass 1

## Execution and complete scope

- **Stage:** `statistics_pass_1`
- **Runtime agent ID:** `/root/statistical_pass_1`
- **Model / reasoning effort:** `gpt-5.6-terra` / `high`
- **Start mode:** `FRESH_SPAWN`
- **Scope completed:** every S001-S091 relationship in `statistics/relationship_inventory.md`: main Table 2 (S001-S019), main ICC (S020), results-supplement eTable 1 (S021-S023), results-supplement eTable 4 (S024-S085), protocol/SAP definitions and power statements (S086-S089), and protocol historical inferential statements (S090-S091).
- **Pass marker:** every assigned record is `PASS_1_COMPLETE` in the relationship inventory.

## Methods and constraints

I checked point-estimate containment, ordered endpoints, sign/direction, effect-measure and scale labels, repeated locations, and supplied model/inferential definitions. Main article pp. 4 and 7 and supplement eTable 4 state a linear mixed model, 95% intervals, and two-sided P-value context. They do not supply covariance structure, degrees of freedom, variance estimator, exact CI construction, or a cell-by-cell estimand rule. Therefore, any interval/P comparison was only a labelled conventional normal-approximation diagnostic; it did not infer omitted specifications or replace the reported analysis.

No assigned result displays `P = 0`, `p = 0.000`, or an equivalent zero. No display-zero candidate was created. Printed point estimates `0`, `0.0`, and `-0.0003` are estimates rather than P-value display zeros and were checked under their reported finite precision.

## Candidate proposals for coordinator merge (no C IDs; Pending Human Adjudication)

### SP1-01 — eTable 4 repeats the 4-week WOMAC-function arm-change pair in the 4-week weight-bearing-pain row

- **Proposed category:** `Statistical reporting inconsistency`
- **Exact source location:** results supplement, `joi240048supp3_prod_1727199125.83025.pdf#page=5`, eTable 4, 4-week `Weight bearing pain` and 4-week `Function` rows.
- **Direct observation:** the weight-bearing-pain row prints krill change `-84 (-122 to -46)` and placebo change `-103 (-141 to -65)`. The function row immediately below prints the exact same two arm-change estimates and intervals: `-84 (-122 to -46)` and `-103 (-141 to -65)`.
- **Comparator / rule:** the rows are separately labelled WOMAC weight-bearing pain (scale 0-300) and WOMAC physical function (scale 0-1700). Exact repeated paired estimates and intervals for two differently labelled endpoint rows require source confirmation because the corresponding printed final/baseline columns differ and the rows are intended to describe different endpoints.
- **Diagnostic observation, not a reconstructed analysis:** the source's mixed-model/linear-combination description means final-minus-baseline arithmetic is not assumed to equal the reported modelled change. The proposal rests on the exact cross-row repetition, not on such arithmetic.
- **Missing definition / human question:** does the source table intentionally use the identical modelled arm-change pair for both endpoints, or was a pair of printed cells transposed or copied? Confirm against the analysis output/table-production source.

### SP1-02 — eTable 4 exactly repeats the 4-week back-pain result for 12-week lower-leg strength

- **Proposed category:** `Statistical reporting inconsistency`
- **Exact source location:** results supplement, `joi240048supp3_prod_1727199125.83025.pdf#page=6`, eTable 4, `Back pain, VAS` at 4 weeks and `Lower leg strength (N)` at 12 weeks.
- **Direct observation:** both rows print the complete between-group result `-1.4 (-5.9 to 3.0)`, `P=.53`. Their arm-level change estimates also match exactly: krill `-2.8 (-6.0 to 0.4)` and placebo `-4.2 (-7.4 to -1.1)`.
- **Comparator / rule:** the rows have different endpoint labels, units, directions, and assessment contexts: back-pain VAS is 0-100 with higher=worse, while lower-leg strength is 0-250 N with higher=greater force. An exact repeat of all displayed inferential fields across these rows is a source-grounded duplicated-value observation requiring reconciliation.
- **Diagnostic observation, not a reconstructed analysis:** this proposal is based on exact duplicated printed values, intervals, and P values across different labels; it does not assume an unreported covariance, SE, or model form.
- **Missing definition / human question:** were the lower-leg-strength 12-week values intentionally equal to the back-pain 4-week output, or were values/labels copied between rows? Confirm against the tabulation source.

### SP1-03 — eTable 4 exactly repeats the 12-week hsCRP between-group result in the 12-week fasting-glucose row

- **Proposed category:** `Statistical reporting inconsistency`
- **Exact source location:** results supplement, `joi240048supp3_prod_1727199125.83025.pdf#page=6`, eTable 4, `High sensitivity C-reactive protein` at 12 weeks and `Fasting glucose` at 12 weeks.
- **Direct observation:** both rows print the between-group result `0.07 (-1.19 to 1.33)`, `P=.92`. The hsCRP row is labelled a median (IQR) endpoint, while fasting glucose is labelled among the table's mean/95% CI endpoints and has different printed arm-level changes (`-0.53`/`0.24` for hsCRP; `0.09`/`0.15` for fasting glucose).
- **Comparator / rule:** the source distinguishes hsCRP (mg/dL) from fasting glucose (mmol/L) and uses different arm-level values, so an exact duplicated between-group estimate, interval, and P value across the two labelled endpoints is a candidate consistency issue requiring source confirmation.
- **Diagnostic observation, not a reconstructed analysis:** a conventional CI/P diagnostic alone does not contradict `P=.92`; the proposal is the independent cross-row duplicate, not the P-value notation or an inferred test calculation.
- **Missing definition / human question:** did the fasting-glucose 12-week between-group result intentionally equal the hsCRP result, or was the printed result copied from that row? Confirm against the statistical output.

## Relationships with no candidate proposal from pass 1

- S001-S035, S037-S075, S077-S083, S085-S091: checks complete without a pass-1 proposal.
- S036/S048, S060/S066, and S076/S084 are each included in the relevant duplicate-value proposal above; no additional duplicate proposal was emitted for the same printed comparator and rule.

## Pass-1 limitations to carry forward

1. The source does not explicitly define the orientation of “between-group difference in change” or eTable 1 “absolute between group difference”; signs were not recast by convention.
2. The supplied final-model definition lacks covariance, degrees of freedom, variance-estimator, exact CI/P-value, and detailed estimand-mapping specifications. No exact SE, test-statistic, or tail-probability reconstruction was attempted.
3. The historical pilot statements and planned power calculations lack sufficient compatible calculation definitions for reproduction; they remain covered relationship records rather than omissions.
4. All three proposals require direct mechanical recheck of the cited source pages and comparison with any available source-grounded table/output explanation. They remain `Pending Human Adjudication`; this pass assigns no severity, validity, acceptance, rejection, or correction.

## Counts and artifact handoff

- **Relationships completed:** 91
- **Distinct candidate proposals:** 3
- **Display-zero exclusions:** 0 encountered / 0 proposals
- **Primary durable artifacts:** `statistics/relationship_inventory.md`; `checkers/statistical_pass_1.md`

## Explicit pass-1 relationship register

PASS_1_COMPLETE for every relationship: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091.
