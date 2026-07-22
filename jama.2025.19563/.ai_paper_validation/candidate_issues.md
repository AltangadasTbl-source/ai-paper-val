# Deduplicated Candidate Issues for Evidence Verification

Candidate count: 7 (package limit: 10). These are candidates, not accepted findings.

## C-01 — Arithmetic inconsistency

- Location: DOC-003, PDF p. 55, eTable 12, second outcome-pattern row, Human-led DPP column.
- Source values: `10 (19%)`, column denominator `N=59`; the first row reports the same numerator as `10 (17%)`.
- Basis: 10 / 59 × 100 = 16.95%, which rounds to 17%, not 19%.
- Verification: Inspect the cell and denominator visually and recompute.

## C-02 — Arithmetic inconsistency

- Location: DOC-003, PDF p. 59, eTable 16.
- Source values: MI-pooled primary outcome 32.2% AI vs 31.9% human; reported risk difference `-1.1` percentage points (one-sided 95% CI lower bound `-11.5`).
- Basis: the displayed marginal difference is +0.3 percentage points, not -1.1. The table does not label the risk difference as adjusted or otherwise based on a different estimand.
- Verification: Determine from the table and supplied package whether -1.1 is an adjusted/model-derived estimate. Accept only if the document itself makes the estimator mismatch demonstrable; otherwise classify Uncertain.

## C-03 — Presentation inconsistency

- Location: DOC-001, PDF p. 6, main Table footnote a; comparator DOC-003 PDF pp. 39–45.
- Source statements: Footnote cites eTable 4 (overall), eTable 6 (by site), and eTable 7 (by baseline HbA1c). The matching supplement titles are eTable 3 (overall), eTable 5 (by site), and eTable 6 (by baseline A1C). eTables 4 and 7 concern eligibility and completion status.
- Basis: the cross-references point to mismatched table numbers/titles.
- Verification: Compare every cited number and parenthetical descriptor with the supplement table titles.

## C-04 — Statistical reporting inconsistency

- Locations: DOC-003 eTables 5–7 and 11, PDF pp. 42–47 and 53–54, repeated age/significance footnotes.
- Source statements: eTable 5 reports age P=.017 by site but a repeated footnote gives P=.014 by study group and says all other characteristics P>.05 despite other significant table results; eTable 6 says all other characteristics P>.05 but repeats age P=.014; eTable 7 says no characteristics differed yet repeats age P=.014; eTable 11 reports age P=.010 and sex P=.041 but repeats age P=.014 and says all other characteristics P>.05.
- Basis: the repeated footnote appears inapplicable and creates table-local contradictions or unexplained duplicate P values.
- Verification: Inspect each table’s footnote markers and text; determine whether this is one repeated-footnote production error and identify exactly which tables contain a demonstrable contradiction.

## C-05 — Presentation inconsistency

- Location: DOC-001, PDF p. 8, Figure 3 footnote a; comparator main Table on PDF p. 6.
- Source values: Figure footnote calls 32.2 and 32.5 kg/m² baseline median `weight`; the same values and units are labeled BMI in the Table.
- Basis: kg/m² and the repeated values identify BMI, not weight.
- Verification: Visually compare Figure 3 footnote a with the Table BMI row.

## C-06 — Cross-document inconsistency

- Location: DOC-001, PDF p. 8, Figure 3B; comparator DOC-003, PDF p. 57, eTable 14, plus DOC-001 Outcomes on p. 3.
- Source values: Figure 3B visually labels participant sequences with endpoints 149 human and 151 AI, while eTable 14 reports HbA1c-change N=103 human and N=106 AI. The main article limits this endpoint to baseline HbA1c 5.7%–6.4%.
- Basis: the figure appears to show the full restricted population rather than the smaller HbA1c-eligible analysis set, with no explanatory caption note.
- Verification: Confirm visually whether 149/151 are intended as participant counts or only rank-axis labels and whether the plotted data contain 103/106 observations. Reject if the labels do not assert sample size.

## C-07 — Cross-document inconsistency

- Location: DOC-003, PDF p. 34, eFigure 3 row label and footnote 3; comparators DOC-001 PDF p. 3 and Figure 2 on p. 7.
- Source statements: Supplement says `0.2% A1C reduction`; main article defines an absolute decrease of at least `0.2 percentage points`.
- Basis: percent and percentage points are not equivalent notation for an HbA1c absolute-change threshold.
- Verification: Compare exact endpoint wording across the cited locations.

## Consolidation notes

- Duplicate checker reports for the Figure 3 BMI label and HbA1c denominator were merged into C-05 and C-06.
- eTable 5–7 and 11 repeated-footnote observations were merged into C-04 as one apparent production pattern.
- Ambiguous narrative wording and checks that reconciled were not forwarded as candidates; they remain in the checker responses for the final rejected/uncertain appendix.
