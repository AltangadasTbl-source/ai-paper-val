# Statistical Consistency Review — Pass 1

## Scope, method, and completion

Fresh statistical pass 1 covered every stable relationship `S001` through
`S033` in `statistics/relationship_inventory.md`: all 17 mapped main-result
inferential records and all 16 mapped support-definition/model records.  The
review used only supplied package sources and source-linked mapped extraction.
Candidate observations below were confirmed against the supplied PDF locations.

For each relationship, this pass checked point-estimate containment, endpoint
ordering, sign/direction, effect-measure and scale labels, and matched
cross-location repetition.  P/CI/test compatibility was evaluated only where
the source supplied a compatible stated model and confidence framework; such
calculations are labelled diagnostic and were not used to infer unstated model
details.  Every S record is `PASS_1_COMPLETE` in the inventory.

No coherent finite-precision display zero (`P = 0`, `p = 0.000`, or equivalent)
occurred in the mapped inferential results.  No display-zero candidate was
created.

## Candidate observations for coordinator registration

These are distinct quality-control candidate observations, without `C` IDs and
without any severity or validity assignment.  Each is pending human
adjudication.

### Candidate observation 1 — Day-5 EQ-5D table inference conflicts with no-significance prose

- **Direct observation:** Table 2 prints the postoperative-day-5 EQ-5D-5L
  treatment contrast as `-0.057 (95% CI, -0.111 to -0.003); P = .04`.
  The point estimate lies in the ordered interval; the interval excludes zero.
  With the stated repeated linear mixed model and 95% CI framework, a
  normal-approximation diagnostic from the interval gives a two-sided P close
  to .04 after rounding.
- **Comparator:** The Results text says there was “no statistically significant
  difference” in quality of life (EQ-5D-5L) between groups.
- **Exact locations:** DOC-001,
  `jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6` (Table 2) and
  `jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5` (Results text).
  The support framework reports 95% CIs except subgroup analyses and no
  adjustment to secondary outcomes: DOC-003,
  `joi240139supp2_prod_1741633738.17362.pdf#page=13`.
- **Consistency rule:** A tabled 95% CI excluding the null and P=.04 is a
  nominal non-null result under the same printed model/CI framework.  The
  blanket prose statement of no statistically significant EQ-5D difference
  does not reconcile with that row as printed.
- **Human question:** Was the day-5 estimate excluded from the narrative’s
  intended endpoint-level inference under an unstated hierarchy or decision
  rule, or is the prose statement overbroad?  The supplied sources do not name
  such a rule.

### Candidate observation 2 — eFigure gives incompatible 99% and 95% CI labels for the same subgroup intervals

- **Direct observation:** The eFigure legend labels the horizontal subgroup
  bars `99% CI`.  Its prose immediately below the plot says “The numbers on the
  right are the within-subgroup relative risks and 95% confidence interval.”
  Those right-side numbers are the values displayed beside the same horizontal
  subgroup intervals (for example, 6-hour RR 0.92 [0.73, 1.15]).
- **Exact locations:** DOC-004,
  `joi240139supp3_prod_1741633738.18862.pdf#page=2`.  The supplied SAP states
  that subgroup analyses use a two-sided 1% level and “Corresponding 99%
  confidence intervals”: DOC-003,
  `joi240139supp2_prod_1741633738.17362.pdf#page=15`.
- **Consistency rule:** The identical printed within-subgroup interval set
  cannot simultaneously carry the mutually different 99% and 95% confidence
  levels.  Endpoint containment/order is otherwise intact.  The SAP supplies
  an independent 99%-CI comparator.
- **Human question:** Which CI level was used for the eFigure’s displayed
  subgroup intervals, and which CI label should govern the eFigure prose and
  legend?

### Candidate observation 3 — ERAS subgroup level label differs between main text and eFigure/SAP

- **Direct observation:** The article’s subgroup-methods sentence identifies
  “high vs low enhanced recovery protocol adherence.”  The eFigure reports a
  single ERAS interaction P=.966 and three strata—high (n=191), moderate
  (n=274), low (n=92)—and the SAP specifies `ERAS protocol compliance (High,
  moderate, low)`.
- **Exact locations:** DOC-001,
  `jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5`; DOC-004,
  `joi240139supp3_prod_1741633738.18862.pdf#page=2`; DOC-003,
  `joi240139supp2_prod_1741633738.17362.pdf#page=15`.
- **Consistency rule:** A two-level high-versus-low subgroup label does not
  match a reported/modelled three-level high/moderate/low subgroup, particularly
  where the three eFigure Ns sum to the complete primary-analysis population
  (557).
- **Human question:** Is “high vs low” intended as shorthand for a
  three-level categorical interaction, or should the main-text subgroup label
  state all three analysed levels?

## Non-candidate outcomes and limitations

- The primary outcome’s abstract, main text, and Table 2 repetitions match;
  their P/CI diagnostics are compatible after displayed precision.
- All displayed OBAS, QoR-15, and EQ-5D point estimates are inside ordered
  intervals; their table P values are diagnostically compatible with stated
  95% mixed-model intervals after rounding.  Candidate observation 1 concerns
  a separate table-to-prose contradiction, not a P/CI mismatch.
- Displayed HRs and IRR all lie within ordered intervals and have compatible
  effect-measure labels.  No P, SE, statistic, or exact variance inputs were
  supplied for several of them, so no ungrounded compatibility calculation was
  attempted.
- The SAP’s post-analysis correction from a stated logit to log link and its
  note that the ERAS subgroup was inserted after analysis do not by themselves
  establish a conflicting final printed effect; no candidate was issued solely
  for those provenance statements.
- The support sources contain many planned/dummy output tables with no
  populated inferential results.  Blank fields were not treated as values.

Pass 1 counts: **33 relationships reviewed; 3 candidate observations; 0
display-zero candidates.**

## Pass 1 Complete Relationship Index

Each relationship below received the full pass-1 checks described above.

| Relationship | Status |
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
