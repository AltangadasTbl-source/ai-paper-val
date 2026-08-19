# Statistical Consistency Review — Pass 1

## Completion

- **Status:** PASS_1_COMPLETE.
- **Scope:** 151 IDs: S001-S148 plus S028a, S028b, and S029a in `statistics/relationship_inventory.md`; all statistical/inferential relationships mapped in DOC-001 through DOC-004.
- **Checks applied:** point-estimate containment, endpoint ordering, sign/direction, effect-measure and scale labels, matched cross-location repetitions, and interval/P/test/statistic/SE compatibility only when compatible supplied definitions exist.
- **No adjudication:** the proposals below are quality-control observations for human review only. No severity, validity, acceptance, rejection, or correction is assigned.

## Results by check family

1. **Containment and endpoint ordering:** all printed estimates/ORs checked in S001-S067 lie within their printed ordered intervals. The sole reported `SE 0.0` (eTable 4 calcium, S065) is a finite-precision SE display; no exact diagnostic is possible without the unrounded SE/test/df.
2. **Sign, direction, and measure labels:** main article continuous and binary results use their supplied change/OR directions consistently. Table 2’s net-change, relative-percent-change, fold-change, and OR distinctions were preserved. eTable 4's surgery-minus-medical difference label agrees with the printed signs.
3. **Cross-location repetitions:** main year-7 HbA1c, weight, remission, medication, clinical/lipid, BMI-subgroup, crossover, and safety statements were compared with the matching table/figure/supplement material at compatible population/time/contrast/precision. P1-01 and P1-02 are the two observed exceptions requiring human clarification.
4. **Compatibility boundaries:** the supplied primary model identifies a two-sided planned primary test, and the supplement identifies mixed-model/GEE/IPW and chi-square/Fisher families. It does not supply every CI level, row-specific test selection, statistic, df, covariance, or variance estimate. Accordingly, no exact reconstructed P value, SE, or tail probability was used for secondary/event rows.
5. **Display-zero rule:** no `P = 0`, `p = 0.000`, or equivalent was used as a candidate. The eTable 2 medical remission rate `2e-16`, displayed as `0%`, is a coherent finite-precision rate display and is not a P-value candidate.

## Candidate proposals (no stable C IDs)

### P1-01 — Internal time-label conflict in Supplement 2 eTable 2

- **Source:** DOC-003, `joi240004supp2_prod_1721756962.82552.pdf` PDF pp. 15-16.
- **Observation:** eTable 2 title and columns state Year 12, with its remission footnote also saying 12-year; footnotes a-c define baseline and year-7 data, 7-year changes, and year-7 group comparisons/ORs.
- **Rule:** a table’s time labels for a displayed result require a coherent time definition.
- **Human question:** Which time point is intended for eTable 2 changes, comparisons, ORs, and P values?

### P1-02 — Different P values for matched printed year-12 HbA1c result

- **Sources:** DOC-001 `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf` PDF pp. 1 and 3; DOC-003 `joi240004supp2_prod_1721756962.82552.pdf` PDF p. 15.
- **Observation:** both locations print −1.1% with 95% CI −1.7% to −0.5% for the stated surgery-minus-medical year-12 HbA1c contrast. The main article prints `P = .002`; eTable 2 prints `P < .001`.
- **Rule:** matched repeated inferential results require either matching P values or an explicit distinction of analyses/tests.
- **Human question:** Is the eTable P associated with another time point, analysis, or test, or is a printed P value inconsistent?

## Limitations

- Exact compatibility diagnostics were withheld when the source omitted a confidence level, sidedness, df, test statistic, row-specific test assignment, covariance, variance estimator, or complete estimand mapping.
- eTable 2’s conflicting time labels prevent treating its footnote time definition as resolved.
- Sparse plotted trajectories have no printed coordinates and were not converted into invented exact estimates.

## Counts

- **Stable S IDs:** 151.
- **Candidate proposals:** 2.
- **DISPLAY_ZERO_NOT_CANDIDATE records:** none applicable; the observed finite-precision zero was a remission rate, not a P value.

## Literal stable-ID completion index

Every stable relationship listed below received the full pass-1 check families described above and is explicitly `PASS_1_COMPLETE`. This literal index preserves the complete 151-ID scope without changing the relationship evidence in the canonical inventory.

- S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 — PASS_1_COMPLETE
- S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S028a S028b — PASS_1_COMPLETE
- S029 S029a S030 S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042 — PASS_1_COMPLETE
- S043 S044 S045 S046 S047 S048 S049 S050 S051 S052 S053 S054 S055 S056 S057 — PASS_1_COMPLETE
- S058 S059 S060 S061 S062 S063 S064 S065 S066 S067 S068 S069 S070 S071 S072 — PASS_1_COMPLETE
- S073 S074 S075 S076 S077 S078 S079 S080 S081 S082 S083 S084 S085 S086 S087 — PASS_1_COMPLETE
- S088 S089 S090 S091 S092 S093 S094 S095 S096 S097 S098 S099 S100 S101 S102 — PASS_1_COMPLETE
- S103 S104 S105 S106 S107 S108 S109 S110 S111 S112 S113 S114 S115 S116 S117 — PASS_1_COMPLETE
- S118 S119 S120 S121 S122 S123 S124 S125 S126 S127 S128 S129 S130 S131 S132 — PASS_1_COMPLETE
- S133 S134 S135 S136 S137 S138 S139 S140 S141 S142 S143 S144 S145 S146 S147 — PASS_1_COMPLETE
- S148 — PASS_1_COMPLETE
