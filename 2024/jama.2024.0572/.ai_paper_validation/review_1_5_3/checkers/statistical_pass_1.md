# Statistical Consistency Review — Pass 1

## Completed scope

Pass 1 covered all stable statistical relationships `S001` through `S077` in `.ai_paper_validation/review_1_5_3/statistics/relationship_inventory.md`: 36 main-paper relationships and 41 protocol/SAP/supplement relationships. Every record is marked `PASS_1_COMPLETE` in that inventory.

The review checked point-estimate containment, endpoint ordering, sign/direction, effect-measure and scale labels, and compatible repeated locations. Interval/P-value/test/statistic/SE calculations were performed only when the supplied sources gave the compatible inferential definitions; where these were absent, that absence is recorded rather than inferred from convention.

## Provisional candidate emitted for coordinator registration

### P1-S01 — `aRR` is expanded as an absolute risk reduction but defined and displayed on a rate-ratio scale

- **Provisional category:** Measure, label, or scale inconsistency.
- **Exact direct-source locations:** [main PDF p. 7](<../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), Table 2; [main PDF p. 9](<../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), Table 3; the supporting statistical-model statement is [main PDF p. 4](<../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>).
- **Direct observations:** Both Table 2 and Table 3 expand `aRR` as “absolute risk reduction.” Their footnotes also state, respectively, that “aRR greater than 1 indicates higher rate ratio for mRS 0-2, 0-3, and 5-6.” The tables print multiplicative values and CIs, for example 0.89 (0.84-0.95), 1.05 (1.02-1.08), and 1.33 (0.52-3.44). The statistical methods state that secondary outcomes use modified Poisson regression with robust standard errors (p. 4).
- **Consistency rule:** An absolute risk reduction is an additive absolute-difference measure, whereas the source footnotes expressly interpret these `aRR` values as rate ratios, a multiplicative scale. The same abbreviation therefore carries incompatible effect-measure/scale labels within the supplied source.
- **Diagnostic note:** No approximation is needed. This observation does not derive a P value, SE, or unreported model quantity.
- **Source-grounded alternative interpretation:** `aRR` may have been intended as an adjusted rate ratio (or a differently named adjusted relative measure); that is a possible explanation, not a correction assigned by this review.
- **Exact human question:** Which expansion and effect-measure label was intended for `aRR` in Tables 2 and 3 and the related narrative, and should the table and prose labels be aligned with that intended measure?
- **Relationship provenance:** S022-S025, S028-S034, and S036. Related ratio-scale supplementary results are S068-S069 and S071-S076.
- **State:** Pending Human Adjudication. This is provisional and has no `C` ID; the coordinator must merge only genuine duplicates before stable registration.

## Checks with no provisional candidate

- The mapped aGenOR, aRR, aRD, RR, and AUC point estimates were within their printed intervals, and every printed interval had endpoints in ascending order.
- The source-defined direction of aGenOR (>1 better mRS outcome with EVT) and ratio measures was consistent with its figure/table labels and matched main-text repetitions.
- Protocol and SAP definitions distinguish planned ITT WMW/CMH and final/exploratory PIM or modified-Poisson analyses. No contradiction was emitted merely from that explicitly described difference.
- No raw test statistic, degrees of freedom, covariance, variance estimator, or sufficient model output is provided for most P values. No sidedness, denominator, model, estimand, or multiplicity rule was inferred.
- `DISPLAY_ZERO_NOT_CANDIDATE`: 0 cases. There were no supplied results printed as `P = 0`, `p = 0.000`, or an equivalent zero display.

## Counts and limitations

- Statistical relationships reviewed: 77.
- Provisional candidates emitted: 1.
- Display-zero non-candidates: 0.
- Limitations: no compatible statistic/SE output for most P values; graphical curves with no printed estimates were not digitized; and no inference was made from planning documents alone.

## Explicit pass-1 relationship coverage ledger

Every stable statistical relationship is explicitly recorded here as complete; details are in `statistics/relationship_inventory.md`.

| ID | Status |
|---|---|
| S001 | PASS_1_COMPLETE |
| S002 | PASS_1_COMPLETE |
| S003 | PASS_1_COMPLETE |
| S004 | PASS_1_COMPLETE |
| S005 | PASS_1_COMPLETE |
| S006 | PASS_1_COMPLETE |
| S007 | PASS_1_COMPLETE |
| S008 | PASS_1_COMPLETE |
| S009 | PASS_1_COMPLETE |
| S010 | PASS_1_COMPLETE |
| S011 | PASS_1_COMPLETE |
| S012 | PASS_1_COMPLETE |
| S013 | PASS_1_COMPLETE |
| S014 | PASS_1_COMPLETE |
| S015 | PASS_1_COMPLETE |
| S016 | PASS_1_COMPLETE |
| S017 | PASS_1_COMPLETE |
| S018 | PASS_1_COMPLETE |
| S019 | PASS_1_COMPLETE |
| S020 | PASS_1_COMPLETE |
| S021 | PASS_1_COMPLETE |
| S022 | PASS_1_COMPLETE |
| S023 | PASS_1_COMPLETE |
| S024 | PASS_1_COMPLETE |
| S025 | PASS_1_COMPLETE |
| S026 | PASS_1_COMPLETE |
| S027 | PASS_1_COMPLETE |
| S028 | PASS_1_COMPLETE |
| S029 | PASS_1_COMPLETE |
| S030 | PASS_1_COMPLETE |
| S031 | PASS_1_COMPLETE |
| S032 | PASS_1_COMPLETE |
| S033 | PASS_1_COMPLETE |
| S034 | PASS_1_COMPLETE |
| S035 | PASS_1_COMPLETE |
| S036 | PASS_1_COMPLETE |
| S037 | PASS_1_COMPLETE |
| S038 | PASS_1_COMPLETE |
| S039 | PASS_1_COMPLETE |
| S040 | PASS_1_COMPLETE |
| S041 | PASS_1_COMPLETE |
| S042 | PASS_1_COMPLETE |
| S043 | PASS_1_COMPLETE |
| S044 | PASS_1_COMPLETE |
| S045 | PASS_1_COMPLETE |
| S046 | PASS_1_COMPLETE |
| S047 | PASS_1_COMPLETE |
| S048 | PASS_1_COMPLETE |
| S049 | PASS_1_COMPLETE |
| S050 | PASS_1_COMPLETE |
| S051 | PASS_1_COMPLETE |
| S052 | PASS_1_COMPLETE |
| S053 | PASS_1_COMPLETE |
| S054 | PASS_1_COMPLETE |
| S055 | PASS_1_COMPLETE |
| S056 | PASS_1_COMPLETE |
| S057 | PASS_1_COMPLETE |
| S058 | PASS_1_COMPLETE |
| S059 | PASS_1_COMPLETE |
| S060 | PASS_1_COMPLETE |
| S061 | PASS_1_COMPLETE |
| S062 | PASS_1_COMPLETE |
| S063 | PASS_1_COMPLETE |
| S064 | PASS_1_COMPLETE |
| S065 | PASS_1_COMPLETE |
| S066 | PASS_1_COMPLETE |
| S067 | PASS_1_COMPLETE |
| S068 | PASS_1_COMPLETE |
| S069 | PASS_1_COMPLETE |
| S070 | PASS_1_COMPLETE |
| S071 | PASS_1_COMPLETE |
| S072 | PASS_1_COMPLETE |
| S073 | PASS_1_COMPLETE |
| S074 | PASS_1_COMPLETE |
| S075 | PASS_1_COMPLETE |
| S076 | PASS_1_COMPLETE |
| S077 | PASS_1_COMPLETE |
