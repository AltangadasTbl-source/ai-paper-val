# Evidence Verifier Response — Round 1

Disposition: **6 Accepted, 1 Uncertain, 0 Rejected**. No second verification round used.

## C-01 — Accepted

- Category: Arithmetic inconsistency.
- Source: DOC-003 PDF p. 55, eTable 12, second outcome-pattern row, Human-led DPP column.
- Evidence: Column denominator `N=59`; cell reports `10 (19%)`. The preceding row reports the same numerator as `10 (17%)`.
- Basis: `10/59 × 100 = 16.95%`, rounding to 17%, not 19%.
- Human verification: Inspect the cited cell and denominator and recompute `10/59`.

## C-02 — Uncertain

- Source: DOC-003 PDF p. 59, eTable 16; supplement methodological description p. 30; DOC-001 PDF p. 4, Statistical Analysis.
- Evidence: MI-pooled outcome percentages are 32.2% AI and 31.9% human, while the reported risk difference is -1.1 percentage points.
- Basis: Direct subtraction gives +0.3 percentage points, but the supplement states 20 imputed datasets were combined using Rubin's rules and the main article says risk differences were estimated by binomial regression. The package does not expose the eTable 16 model specification/output sufficiently to establish whether -1.1 is separately modeled.
- Human verification: Reproduce the MI pooling and binomial-regression estimate; determine whether -1.1 is adjusted/model-derived and label the estimand if so.

## C-03 — Accepted

- Category: Presentation inconsistency.
- Sources: DOC-001 PDF p. 6, Table footnote a; DOC-003 PDF pp. 39–47.
- Evidence: Main footnote cites eTable 4 (overall), eTable 6 (by site), and eTable 7 (by baseline HbA1c). Matching supplement titles are eTable 3 (overall), eTable 5 (by site), and eTable 6 (by baseline A1C); eTables 4 and 7 concern eligibility and completion.
- Basis: All three cited numbers are shifted from the tables described by their parentheticals.
- Human verification: Compare every descriptor with the supplement titles; intended citations appear to be eTables 3, 5, and 6.

## C-04 — Accepted, narrowed

- Category: Statistical reporting inconsistency.
- Primary source: DOC-003 PDF pp. 53–54, eTable 11, footnotes 1 and 2.
- Evidence: Footnote 1 reports age `P=.010` and sex `P=.041`, with all other characteristics `P>.05`. Footnote 2, attached to age, reports age `P=.014` and says all other baseline characteristics were similar (`P>.05`). The identical `P=.014` age footnote also appears in eTables 5–7 on pp. 43, 45, and 47.
- Basis: eTable 11 assigns age two unexplained P values, and footnote 2's “all other” statement conflicts with footnote 1's significant sex result. Other locations support a copied/inapplicable-footnote pattern but their correct P values are not established.
- Human verification: Determine which age P value applies to eTable 11's N=151/N=149 population and remove or identify the other footnote's population.

## C-05 — Accepted

- Category: Presentation inconsistency.
- Sources: DOC-001 PDF p. 8, Figure 3 footnote a; comparator Table on PDF p. 6.
- Evidence: Figure footnote calls `32.2 (28.2–35.9) kg/m²` and `32.5 (29.3–37.7) kg/m²` baseline median “weight”; the Table labels the identical values as BMI.
- Basis: The values and unit reproduce the BMI row, not weight.
- Human verification: Compare Figure 3 footnote a with the `BMI, median (IQR)` row.

## C-06 — Accepted

- Category: Cross-document inconsistency.
- Sources: DOC-001 PDF p. 8, Figure 3B; DOC-001 p. 3, Outcomes; DOC-003 PDF p. 57, eTable 14.
- Evidence: Figure 3B axes run to 149 human and 151 AI, while eTable 14 reports HbA1c-change N=103 human and N=106 AI. Main p. 3 limits this endpoint to baseline HbA1c 5.7%–6.4%. PDF vector inspection found at least 117 human-colored and 121 AI-colored nonzero bar rectangles, already exceeding 103/106.
- Basis: Figure 3B represents a larger analysis set than eTable 14 without caption explanation.
- Human verification: Inspect the plotting data and reconcile the participant ranks with N=103/N=106 and the endpoint eligibility rule.

## C-07 — Accepted

- Category: Cross-document inconsistency.
- Sources: DOC-003 PDF p. 34, eFigure 3 row label and footnote 3; DOC-001 PDF p. 3 and Figure 2 on p. 7.
- Evidence: Supplement uses `0.2% A1C reduction`; main article defines an absolute decrease of at least `0.2 percentage points`. Counts remain 35/130 in each arm.
- Basis: Relative percent and absolute percentage-point notation are not equivalent; matching counts indicate a labeling inconsistency.
- Human verification: Compare exact endpoint wording and revise the supplement label if it represents the same endpoint.
