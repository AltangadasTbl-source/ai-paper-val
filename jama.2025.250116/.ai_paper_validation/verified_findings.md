# Evidence Verification — Round 1

All seven submitted candidates were verified against the original PDFs, native text, and rendered pages. No second verification round was required.

| ID | Status | Category after verification | Evidence summary |
|---|---|---|---|
| C01 | Verified | Statistical reporting inconsistency | Main Table 2 reports 52/131 (39.7%); narrative reports 51/131 (39.7%); supplement strata sum to 52. |
| C02 | Verified | Arithmetic inconsistency | eTable 10 reports OR 1.194 from 40/106 versus 29/122; cross-product OR is 1.9436 and matches the printed CI. |
| C03 | Verified | Statistical reporting inconsistency | eFigure 9 reports OR 0.11 outside CI 0.36-3.42; displayed cells yield 1.107 and the printed CI. |
| C04 | Verified | Presentation inconsistency | eFigure 8 panel B duplicates all eFigure 7 panel-B estimates despite a different outcome and different event cells. |
| C05 | Verified with scoped wording | Statistical reporting inconsistency | eFigures 7 and 9 label high-stratum treatment ORs as interaction tests; main text interprets selected entries as interactions. Do not rely on eFigure 8 for this finding. |
| C06 | Verified | Presentation inconsistency | eTable 14 cell `45 42.5)` is missing an opening parenthesis. |
| C07 | Verified | Presentation inconsistency | eTable 14 cell `0 0 (0.0)` contains a duplicated zero. |

## Verification details

- C01: `12 + 40 = 52`; `52/131 = 39.7%`, while `51/131 = 38.9%`.
- C02: non-events are 66 and 93; `(40×93)/(66×29) = 1.9436`; log-OR CI is approximately 1.10-3.45.
- C03: eFigure 9 APACHE ≥25 cells are 31/38 versus 32/40; `(31×8)/(7×32) = 1.107`, with CI approximately 0.358-3.421.
- C04: eFigures 7 and 8 repeat the same six OR/CI/P triplets; eFigure 8 high-stratum mortality ORs from displayed cells are approximately 0.66, 0.42, and 0.46, not 1.85, 5.79, and 3.08.
- C05: eFigure 7 high-stratum ORs reconstruct exactly as 1.846, 5.798, and 3.084. For SOFA, the low-stratum OR is 2.019, so the crude interaction ratio is approximately 1.53, not 3.08. eFigure 9 high-stratum CCI and SOFA estimates similarly reconstruct as 0.4875 and 0.5253. The finding is independently supported without eFigure 8.
- C06: `45/106 = 42.45%`, so 42.5% is arithmetically correct but the cell is malformed.
- C07: the table heading establishes `n (%)`; the first zero is duplicated.

