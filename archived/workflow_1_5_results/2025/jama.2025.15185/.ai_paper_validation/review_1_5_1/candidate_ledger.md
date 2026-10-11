# Candidate Ledger

All entries remain **Pending Human Adjudication**. Genuine duplicates from the numeric, cross-source, and statistical-pass-1 checker artifacts were merged before stable IDs. After registration, IDs are immutable and may not be deleted, merged, or renumbered.

## C001 — Baseline index-stroke type counts differ across baseline tables

- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** QN001; QC001; N006/N018
- **Exact source locations:** DOC-001 `jama_engelter_2025_oi_250066_1761597796.45511.pdf` p.4, Table 1; DOC-004 `joi250066supp3_prod_1761597796.4701.pdf` pp.10-11, eTable 1.
- **Printed evidence:** Main levodopa arm: ischemic `260 (84.7%)`, hemorrhagic `47 (15.3%)`. Supplement levodopa arm: ischemic `263 (85.7%)`, hemorrhagic `44 (14.3%)`. Both tables label the randomized levodopa population as n=307; placebo values match.
- **Rule/calculation:** Same-population, same-arm, mutually exclusive stroke-type counts should agree. Both pairs sum to 307, but three participants switch categories.
- **Alternative source-grounded interpretation:** An unstated recoding or data cut could explain the difference; neither table identifies one.
- **Human question:** Which levodopa stroke-type pair is intended, and was a different classification rule used?
- **Status:** Pending Human Adjudication

## C002 — Baseline NIHSS statistic and label do not reconcile across tables

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** QN003; QC002; N007/N019
- **Exact source locations:** DOC-001 p.4, Table 1 and p.5, Results; DOC-004 pp.10-11, eTable 1.
- **Printed evidence:** Main reports median (IQR) NIHSS `7 (5-11)` levodopa, `8 (5-10)` placebo, and overall `7 (5-10)`. eTable 1 labels `Median NIHSS at randomization [IQR]` but prints overall/placebo/levodopa `8.2 (3.9)`, `8.3 (3.8)`, `8.2 (3.9)`.
- **Rule/calculation:** A median/IQR should supply interval endpoints; a decimal value plus one parenthesized value instead resembles mean (SD) and is not the same printed summary.
- **Alternative source-grounded interpretation:** The eTable values may be means (SDs) under a stale label.
- **Human question:** What statistic is `8.2 (3.9)`, and which label/values are intended?
- **Status:** Pending Human Adjudication

## C003 — Time from stroke onset to randomization differs across baseline tables

- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** QN002; QC003; N007/N019
- **Exact source locations:** DOC-001 p.4, Table 1; DOC-004 p.11, eTable 1.
- **Printed evidence:** Main reports `3.0 (2.0-5.0)` days for both arms. Supplement's identically named row reports overall `7 [5,10]`, placebo `8 [5,10]`, and levodopa `7 [5-11]`, but the supplement row does not visibly print a unit.
- **Rule/calculation:** Under a common day unit, the same named variable and arms cannot have medians of 3 versus 7/8 through rounding; exact cross-source identity therefore requires confirmation of the supplement's omitted unit.
- **Alternative source-grounded interpretation:** A different unstated unit, time origin, or variable derivation may have been used.
- **Human question:** What unit and time origin apply to the supplement row, and which values are intended?
- **Status:** Pending Human Adjudication

## C004 — Estimand 4 confidence-interval upper endpoint differs within eTable 2

- **Category:** Statistical reporting inconsistency
- **Checker provenance:** QN004; QS001; N021/S015
- **Exact source locations:** DOC-004 p.12, eTable 2 narrative Results; DOC-004 p.13, eTable 2 result row.
- **Printed evidence:** Narrative gives `1.06 (95% CI, 0.86 to 1.25)`; matched Estimand 4 row gives `1.06 [0.86-1.26]` for the same full analysis set, composite endpoint, and estimand.
- **Rule/calculation:** Same estimate and CI repeated for the same estimand should have one upper endpoint; `1.25 != 1.26`.
- **Alternative source-grounded interpretation:** One occurrence may reflect a one-hundredth transcription or rounding difference.
- **Human question:** Is the intended upper 95% CI endpoint 1.25 or 1.26?
- **Status:** Pending Human Adjudication

## C005 — Levodopa PROMIS-29 descriptive mean differs between main text and eTable 4

- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** QN005; QC004; N013/N024/S003/S017
- **Exact source locations:** DOC-001 p.6, Secondary Outcomes; DOC-004 p.15, eTable 4.
- **Printed evidence:** Main: levodopa `66 (14)`, placebo `65 (14)`. eTable: levodopa `64.74 (14.33)`, placebo `65.11 (13.79)`.
- **Rule/calculation:** `64.74` rounds to 65, not 66, at whole-number precision; the eTable raw contrast `64.74-65.11=-0.37` aligns with its reported effect.
- **Alternative source-grounded interpretation:** A different unstated scoring transformation or analysis set could have been used.
- **Human question:** Which levodopa mean and scoring/analysis definition is intended?
- **Status:** Pending Human Adjudication

## C006 — PROMIS-10 descriptive means differ between main text and eTable 4

- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** QN006; QC005; N013/N024/S004/S017
- **Exact source locations:** DOC-001 p.6, Secondary Outcomes; DOC-004 p.15, eTable 4.
- **Printed evidence:** Main prints `28 (6)` for both arms. eTable prints placebo `29.87 (5.74)` and levodopa `30.04 (5.73)`.
- **Rule/calculation:** Both eTable means round to 30, not 28, at the main text's whole-number precision.
- **Alternative source-grounded interpretation:** An unstated different PROMIS-10 scoring or analysis version may have been used.
- **Human question:** Which group means and score transformation are intended?
- **Status:** Pending Human Adjudication

## C007 — Placebo five-week FMA standard deviation differs from eTable 4

- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** QC006; N014/S008/S017
- **Exact source locations:** DOC-001 p.6, Secondary Outcomes; DOC-004 p.15, eTable 4.
- **Printed evidence:** Main placebo mean (SD) is `56 (26)`; eTable placebo is `56.27 (25.20)`. Levodopa `57 (27)` is compatible with `57.37 (26.70)`.
- **Rule/calculation:** Ordinary whole-number rounding of 25.20 is 25, not 26.
- **Alternative source-grounded interpretation:** A different unstated SD convention or analysis population could have been used.
- **Human question:** What is the intended placebo SD and rounding convention?
- **Status:** Pending Human Adjudication

## C008 — Placebo PRAI no-improvement numerator differs between main text and eTable 4

- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** QN007; QC007; N013/N024/S017
- **Exact source locations:** DOC-001 p.6, Secondary Outcomes; DOC-004 p.15, eTable 4.
- **Printed evidence:** Main reports placebo `52/270 (19%)`; eTable reports placebo `51 (18.89%) (n=270)`. Levodopa is 51/276 in both.
- **Rule/calculation:** With the same outcome and denominator, the numerator cannot be both 51 and 52; `51/270=18.89%`, while `52/270=19.26%`.
- **Alternative source-grounded interpretation:** An unstated response-category rule could differ by one record.
- **Human question:** Is the placebo numerator 51 or 52, and were different response rules used?
- **Status:** Pending Human Adjudication

## C009 — eTable 6 overall adverse-event total is one below arms and category sums

- **Category:** Denominator, proportion, or total inconsistency
- **Checker provenance:** QN008; QC008; N010/N012/N026
- **Exact source locations:** DOC-001 pp.6-7, Table 2 and narrative; DOC-004 p.17, eTable 6.
- **Printed evidence:** Main reports 146 prespecified adverse events, 79 levodopa and 67 placebo. eTable header gives overall `n=145`, placebo 67, levodopa 79; its intensity rows sum `58+86+2=146`, outcome rows `1+29+116=146`, and relation rows also total 146.
- **Rule/calculation:** `67+79=146`, not 145, and every complete eTable classification totals 146.
- **Alternative source-grounded interpretation:** One event might be excluded under an unstated rule, but that does not reconcile the printed category totals.
- **Human question:** Should overall n be 146, or what rule explains 145 while all displayed totals equal 146?
- **Status:** Pending Human Adjudication

## C010 — eFigure 4 switches locally from “FMA” to “FMMA” without qualification

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** QN009; N030/S019
- **Exact source locations:** DOC-004 p.23, eFigure 4 x-axis/title/legend; DOC-003 p.2, SAP objective; DOC-001 pp.1,3,6, FMA definition and results.
- **Printed evidence:** The figure title/legend use `FMA`, while the x-axis reads `Adjusted Mean Difference (FMMA points)`. The SAP separately defines `Fugl-Meyer Motor Assessment (FMMA)` for the same assessment.
- **Rule/calculation:** A figure should use one locally clear outcome abbreviation or explicitly identify synonymous abbreviations; the title/legend-to-axis switch is not qualified on the figure page.
- **Alternative source-grounded interpretation:** `FMMA` is source-defined in the SAP as the same assessment, so the axis may intentionally use a synonym rather than contain a typographic error.
- **Human question:** Is the local FMA/FMMA switch intentional, and should the figure use one abbreviation or define both locally?
- **Status:** Pending Human Adjudication

## C011 — Estimand 4 win ratio appears under an FMA mean-difference column heading

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** QS002; S015
- **Exact source locations:** DOC-004 p.13, eTable 2 column header and Estimand 4 row.
- **Printed evidence:** The column is headed `Estimated Effect of Levodopa: Mean Difference on FMA, [CI]`; Estimand 4 defines its population-level summary as a `win ratio [95% CI]` for the composite of death and 3-month FMA and prints `1.06 [0.86-1.26]`.
- **Rule/calculation:** A dimensionless win ratio is not an FMA-point mean difference; the row and column heading identify incompatible measures/scales.
- **Alternative source-grounded interpretation:** The column heading may be intended for all rows except Estimand 4 but is not qualified that way.
- **Human question:** Should the column heading be qualified for Estimand 4, or should the row's measure be changed?
- **Status:** Pending Human Adjudication

## C012 — Estimand 4 is called an odds ratio in prose and a win ratio in the table

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** QS003; S015
- **Exact source locations:** DOC-004 p.12, eTable 2 narrative Results; DOC-004 p.13, Estimand 4 row.
- **Printed evidence:** Narrative calls `1.06` an `odds ratio`; matched row identifies the same full-analysis-set composite effect as a `win ratio [95% CI]`.
- **Rule/calculation:** The same estimand/effect should have one measure label; odds ratio and win ratio are not interchangeable labels under the supplied definitions.
- **Alternative source-grounded interpretation:** A modelling implementation might relate the quantities, but the supplied source does not define them as synonyms.
- **Human question:** Is the intended Estimand 4 measure an odds ratio or a win ratio?
- **Status:** Pending Human Adjudication

## Registration summary

- Stable candidates registered: 12 (`C001`-`C012`).
- Every candidate remains Pending Human Adjudication.
- Duplicate checker proposals were merged only when they concerned the same printed values, comparator, and consistency rule. C011 and C012 remain distinct because their comparators differ (column heading versus narrative label).
