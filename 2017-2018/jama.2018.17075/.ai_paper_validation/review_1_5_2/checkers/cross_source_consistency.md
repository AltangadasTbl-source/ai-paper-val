# Cross-Source Consistency Check

## Scope, method, and coverage

This fresh cross-source lane covered every canonical relationship in the supplied
package: numeric relationships `N001`--`N073` and statistical relationships
`S001`--`S032`.  It used only the fresh extraction maps, native/layout text, and
rendered supplied PDF pages for `DOC-001`--`DOC-004`; no old audit derivative or
external source was used.  `DOC-004` was checked as a no-result data-sharing
statement.

Before comparing printed values, each comparison was restricted to records with
the same population, analysis set, time window, contrast, outcome definition,
effect measure, scale/unit, and displayed precision.  A protocol version or a
post-randomization analysis set was not treated as a comparator to the final
intention-to-treat result merely because it used a similar outcome name.  A
displayed zero P value was not treated as a candidate; no such display was the
basis of an observation below.

| Checked relationship scope | Cross-source locations and matching decision | Result |
|---|---|---|
| `N001`--`N011`, `S001`--`S005` | Main-article trial design, eligibility, allocation, temperature targets, outcome definition, sample-size and analysis definitions were checked against the version-controlled protocol and amendment material (`DOC-002` pp. 14-28, 69-86, 139, 174-179) and Supplement 2 eligibility table (DOC-003 p. 3). Version-specific changes in age threshold, control-temperature range, recruitment target, run-in, and interim plan are identified as such in the supplied protocol; they are not matched-result conflicts. | No candidate observation from properly version-matched definitions. |
| `N012`--`N019`, `N020`--`N027`, `S006`--`S010` | Main flow, randomized denominators, treatment delivery, baseline characteristics, analysis rules, and outcome-model definitions were checked against Supplement 2 eTables 2-13/eFigures 1-2 (DOC-003 pp. 4-23). Different denominators for randomized, consented, primary-evaluable, mortality, per-protocol, as-treated, and post-hoc populations were retained rather than compared as if interchangeable. | No candidate observation except the exact same-ITT comparisons recorded below. |
| `N028`, `S006` | Primary favourable GOS-E 5-8 result, same 6-month primary-evaluable population (117/240 vs 111/226), hypothermia-minus-normothermia risk-difference convention, RR, CI and P value were checked across abstract, main narrative and Table 2. | One candidate observation: the abstract omits the risk-difference minus sign; recorded below. |
| `N030`--`N040`, `S007`--`S010` | Main Table 2/narrative/abstract adverse-event, mortality, subgroup and sensitivity results were checked against their matching Supplement 2 displays. Per-protocol/as-treated and missingness tables were not compared with ITT results as if they were the same population. | Two candidate observations: the two same-ITT bleeding P values differ between Table 2 and eTable 6; recorded below. All other comparable displayed counts, percentages, primary RR/CI/P, mortality HR, pneumonia results, and analysis-set labels matched or were non-comparable by design. |
| `N041`--`N058`, `S011`--`S017` | All result-relevant DOC-002 protocol, amendment, SAP-reference, and DSMC pages were checked against final-source definitions and later supplied interim displays. DSMC Group x/y interim results are masked monitoring data and not the final named treatment contrast; historical protocol targets/definitions are versioned. | No qualifying cross-source candidate observation. The supplied package contains SAP citations/links but not the linked SAP/update text, so no unprovided SAP statement was inferred. |
| `N059`--`N072`, `S018`--`S032` | All Supplement 2 eligibility, randomization, process-of-care, adverse-event, per-protocol, as-treated, missingness and adequate-cooling results were checked against their matching main-article statements/tables and their own stated analysis populations. | The two eTable 6/Table 2 P-value observations below are the only qualifying same-result mismatches identified. Other differences are explained by an explicitly different analysis set, outcome type, time point, model, or summary statistic. |
| `N073` | DOC-004 p. 1 data-sharing statement. | No trial-result numeric or statistical comparator is present. |

## Candidate observations for human adjudication

The items below are observations of printed-source inconsistencies, not stable
candidate IDs, corrections, severity assessments, or adjudications.

### CS-X01 — Primary risk-difference sign differs between the abstract and body/table

- **Matched result and rule:** Six-month favourable outcome (GOS-E 5-8),
  primary-evaluable population, hypothermia versus normothermia, absolute risk
  difference on the percentage-point scale. Both displays give 117/240 (48.8%)
  and 111/226 (49.1%), so they meet the population, time, contrast, outcome and
  precision match rule.
- **Printed values and exact locations:** The abstract prints “risk difference,
  **0.4%** (95% CI, -9.4% to 8.7%)” at
  [DOC-001 p. 1](../../../jama_cooper_2018_oi_180132.pdf#page=1).  The Results
  narrative prints “absolute risk difference, **-0.4 percentage points** (95%
  CI, -9.4 to 8.7)” at
  [DOC-001 p. 5](../../../jama_cooper_2018_oi_180132.pdf#page=5), and Table 2
  prints **-0.4 (-9.4 to 8.7)** at
  [DOC-001 p. 7](../../../jama_cooper_2018_oi_180132.pdf#page=7).
- **Comparison logic/calculation:** Using the printed group percentages in the
  stated order gives 48.8% - 49.1% = -0.3 percentage points before rounding;
  the underlying printed fractions give approximately -0.4 percentage points.
  Thus the body/table sign agrees with the stated contrast and the abstract
  point estimate has the opposite displayed sign.
- **Supported alternative interpretation:** The abstract may have intended an
  unsigned magnitude while the body/table explicitly report a signed
  hypothermia-minus-normothermia difference. The CI endpoints alone do not
  resolve that presentation difference; the matching fractions and labelled
  contrast do.
- **Human verification question:** In the final publication record, should the
  abstract risk difference carry a leading minus sign to match the table and
  Results narrative, or was a different risk-difference orientation intended
  only for the abstract?

### CS-X02 — Intracranial-bleeding P value differs between matching Table 2 and eTable 6

- **Matched result and rule:** New or increased intracranial bleeding within the
  reported adverse-event window, intention-to-treat group denominators 260 and
  240, hypothermia versus normothermia, and a P-value display for the same
  binary outcome.
- **Printed values and exact locations:** Main Table 2 prints 47/260 (18.1%)
  versus 37/240 (15.4%), with **P = .70**, at
  [DOC-001 p. 7](../../../jama_cooper_2018_oi_180132.pdf#page=7).  Supplement 2
  eTable 6 prints the same two counts and percentages but **P = .43**, at
  [DOC-003 p. 10](../../../joi180132supp2_prod.pdf#page=10).
- **Comparison logic/calculation:** The raw numerator, denominator, percentage,
  group order, outcome label, and ITT populations are identical in the two
  displays. The printed P values differ by 0.27; no recalculation is required
  to establish the printed-source mismatch.
- **Supported alternative interpretation:** The two displays could have used
  different unprinted test implementations or adjustments, but the main-methods
  text describes unadjusted chi-square testing for adverse-event proportions and
  neither table labels a different test or adjusted population for this row.
- **Human verification question:** Which P value, .70 or .43, belongs to the
  intracranial-bleeding row under the reported Table 2/eTable 6 analysis?

### CS-X03 — Extracranial-bleeding P value differs between matching Table 2 and eTable 6

- **Matched result and rule:** New significant extracranial bleeding within the
  reported adverse-event window, intention-to-treat group denominators 260 and
  240, hypothermia versus normothermia, and a P-value display for the same
  binary outcome.
- **Printed values and exact locations:** Main Table 2 prints 8/260 (3.1%)
  versus 6/240 (2.5%), with **P = .43**, at
  [DOC-001 p. 7](../../../jama_cooper_2018_oi_180132.pdf#page=7).  Supplement 2
  eTable 6 prints the same two counts and percentages but **P = .70**, at
  [DOC-003 p. 10](../../../joi180132supp2_prod.pdf#page=10).
- **Comparison logic/calculation:** The raw numerator, denominator, percentage,
  group order, outcome label, and ITT populations are identical in the two
  displays. The printed P values differ by 0.27; no recalculation is required
  to establish the printed-source mismatch.
- **Supported alternative interpretation:** The values may represent a
  transposition of the two bleeding-row P values between the two tables, but
  that explanation is an inference rather than an established correction. As
  with CS-X02, no different test, adjustment, or population is printed.
- **Human verification question:** Which P value, .43 or .70, belongs to the
  extracranial-bleeding row under the reported Table 2/eTable 6 analysis?

## Limitations

The supplied package does not embed the text of the referenced SAP, SAP update,
or SAP correction; their external linked content was not used.  Graphical marks
without printed numerical labels (main Figure 3 and some support figures) were
checked for scale, population and label agreement but were not reverse-read as
exact values.  Historical protocol and DSMC records have explicitly different
versions, timing, masking or analysis populations; these differences were not
misclassified as conflicts with the final report.

**Counts:** 73/73 numeric relationships and 32/32 statistical relationships
covered; 3 distinct candidate observations; 0 display-zero-P observations.
