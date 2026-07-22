# Critic Disposition

Retained **6 of 6 verifier-accepted issues**: **1 Major, 5 Minor**. No new issues added.

## 1. C-06 — Major — Cross-document inconsistency

- Location: DOC-001 PDF p. 8, Figure 3B and p. 3, Outcomes; comparator DOC-003 PDF p. 57, eTable 14.
- Evidence: Figure 3B's ranked axes end at 149 Human and 151 AI. Vector inspection identified at least 117 Human-colored and 121 AI-colored nonzero bars, already exceeding eTable 14's HbA1c-change populations of Human `N=103` and AI `N=106`. The article limits the endpoint to baseline HbA1c 5.7%–6.4%.
- Basis: The figure demonstrably displays a larger HbA1c analysis set than the co-cited table without caption explanation. Exact underlying figure N is not asserted.
- Verification: Count the plotting-data records and reconcile the inclusion rule with eTable 14 and the stated HbA1c restriction.

## 2. C-01 — Minor — Arithmetic inconsistency

- Location: DOC-003 PDF p. 55, eTable 12, second component-pattern row, Human-led DPP column.
- Evidence: Column denominator `N=59`; cell `10 (19%)`; preceding row reports the same numerator as `10 (17%)`.
- Basis: `10/59 × 100 = 16.95%`, rounding to 17%, not 19%.
- Verification: Inspect the cell and denominator and recompute.

## 3. C-03 — Minor — Presentation inconsistency

- Location: DOC-001 PDF p. 6, main Table footnote a; comparator DOC-003 PDF pp. 39–47.
- Evidence: Footnote cites eTable 4 “overall,” eTable 6 “by site,” and eTable 7 “by baseline HbA1c.” Matching supplement titles are eTable 3, p. 39; eTable 5, p. 42; and eTable 6, p. 44. eTable 4 concerns eligibility and eTable 7 completion status.
- Basis: All three cross-reference numbers fail to match their descriptors.
- Verification: Compare each descriptor with the supplement title; intended references appear to be eTables 3, 5, and 6.

## 4. C-04 — Minor — Statistical reporting inconsistency

- Location: DOC-003 PDF pp. 53–54, eTable 11, age row and footnotes 1–2.
- Evidence: Footnote 1 reports age `P=.010`, sex `P=.041`, and all other characteristics `P>.05`. Footnote 2 reports age `P=.014` and says all other characteristics were similar (`P>.05`).
- Basis: The table assigns age two unexplained P values; footnote 2 also conflicts with the significant sex result.
- Verification: Establish which age P value applies to the eTable 11 N=151/N=149 population and identify or remove the other footnote.

## 5. C-05 — Minor — Presentation inconsistency

- Location: DOC-001 PDF p. 8, Figure 3 footnote a; comparator main Table, PDF p. 6.
- Evidence: Figure footnote labels `32.2 (28.2–35.9) kg/m²` and `32.5 (29.3–37.7) kg/m²` as baseline median “weight”; the Table reports them as BMI.
- Basis: The unit and values identify BMI, not weight.
- Verification: Compare Figure 3 footnote a with the Table BMI row.

## 6. C-07 — Minor — Cross-document inconsistency

- Location: DOC-003 PDF p. 34, eFigure 3 row label and footnote 3; comparators DOC-001 PDF p. 3 and Figure 2 on p. 7.
- Evidence: Supplement states `0.2% A1C reduction`; the main article defines an absolute decrease of at least `0.2 percentage points`. Both report 35/130 per arm.
- Basis: Percent and percentage points are not equivalent; matching counts show the same endpoint is labeled differently.
- Verification: Compare the exact wording and revise the supplement if it represents the same endpoint.

## Exclusions and mergers

- C-02 remains Uncertain because MI pooling and binomial-regression estimation may explain why the reported risk difference is not the direct marginal subtraction.
- C-04 is one narrowed eTable 11 issue; repeated P=.014 footnotes in eTables 5–7 are corroborating production-pattern evidence, not separate findings.
- C-06 does not claim axis endpoints alone prove exact sample sizes; verified visible bar counts already exceed eTable 14 denominators.

Final retained count: 6, within the maximum of 10.
