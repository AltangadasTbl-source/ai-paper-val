# Stable Candidate Ledger

All entries are quality-control candidates and remain **Pending Human Adjudication**. Genuine duplicate observations from the numeric, statistical-pass-1, and cross-source lanes were merged before stable IDs. Similar observations with different comparators or consistency rules remain distinct. No candidate was registered from a display-zero P value.

## C001 — eTable 2 assigns the N=3,311 column a second intervention-group label

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-004 eTable 2 header, PDF p. 3](../../joi190106supp3_prod_1635377898.49725.pdf#page=3); [DOC-004 eTable 2 continuation, PDF p. 5](../../joi190106supp3_prod_1635377898.49725.pdf#page=5); [DOC-001 Table 2, PDF p. 5](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5)
- **Printed evidence:** The first eTable 2 page labels N=3,272 and N=3,311 as “Intervention group”; later continuation pages and the main table identify N=3,311 as control.
- **Rule and diagnostic:** A fixed treatment-arm column must retain one group identity. The numerical contrast directions are compatible with N=3,311 being control, suggesting—but not proving—a header production error.
- **Alternative source-grounded interpretation:** An unprinted table-specific population definition could exist, but none appears in the supplied package.
- **Exact human question:** Is the N=3,311 header on eTable 2 p. 3 intended to read “Control group”?
- **Checker provenance:** QC-X0001; QC-S001; canonical S093.
- **Status:** Pending Human Adjudication

## C002 — eTable 2 red-wine median lies above its printed upper quartile

- **Category:** Numeric or arithmetic inconsistency
- **Exact source location:** [DOC-004 eTable 2 red-wine row, PDF p. 7](../../joi190106supp3_prod_1635377898.49725.pdf#page=7)
- **Printed evidence:** Intervention baseline red wine is `33 (0, 29)` g/week and the footnote defines baseline entries as median (IQR).
- **Rule and calculation:** For median (Q1, Q3), Q1 ≤ median ≤ Q3. Here `0 ≤ 33 ≤ 29` is false; the median exceeds Q3 by 4 g/week.
- **Alternative source-grounded interpretations:** The median, upper quartile, or row alignment may contain a printing error; the source does not establish the intended replacement.
- **Exact human question:** What are the intended intervention baseline red-wine median and IQR?
- **Checker provenance:** QC-N001; QC-S002; part of QC-X0002; canonical N146/S093.
- **Status:** Pending Human Adjudication

## C003 — all-randomized red-wine baseline summaries differ between eTables 2 and 7

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [DOC-004 eTable 2, PDF p. 7](../../joi190106supp3_prod_1635377898.49725.pdf#page=7); [DOC-004 eTable 7, PDF p. 19](../../joi190106supp3_prod_1635377898.49725.pdf#page=19)
- **Printed evidence:** eTable 2 gives intervention/control baseline median (IQR) as `33 (0, 29)` and `4 (0, 29)`; eTable 7 gives `0 (0, 29)` in both arms. Both display N=3,272/N=3,311 and the same baseline measure/unit.
- **Rule:** A follow-up missing-value method does not by itself change a baseline summary for the same stated groups; the displayed medians conflict at printed precision.
- **Alternative source-grounded interpretation:** eTable 7 may use an unstated baseline subset or baseline handling rule despite the identical displayed arm Ns.
- **Exact human question:** Which baseline population and red-wine medians were used in each table?
- **Checker provenance:** QC-X0002; canonical N146/N211 and S093/S488.
- **Status:** Pending Human Adjudication

## C004 — PDQS baseline mean differs between the principal and baseline-value-carried-forward tables

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [DOC-001 Table 2, PDF p. 5](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5); [DOC-004 eTable 6, PDF p. 16](../../joi190106supp3_prod_1635377898.49725.pdf#page=16)
- **Printed evidence:** Main Table 2 reports `21.1 (3.7)` in both arms; eTable 6 reports `21.0 (3.7)` in both arms, with the same N=3,272/N=3,311 and PDQS 0-42 label.
- **Rule:** Matched baseline summaries for the same stated groups and scale should agree at displayed precision unless a different baseline rule is stated.
- **Alternative source-grounded interpretations:** An undocumented baseline subset/handling or a different rounding convention may have been used.
- **Exact human question:** Were different baseline inputs or rounding rules used for PDQS in the two displays?
- **Checker provenance:** QC-X0003; canonical N024/N189 and S009/S463.
- **Status:** Pending Human Adjudication

## C005 — intervention baseline energy SD differs between Table 3 and eTable 8

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [DOC-001 Table 3, PDF p. 7](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7); [DOC-004 eTable 8, PDF p. 21](../../joi190106supp3_prod_1635377898.49725.pdf#page=21); [DOC-001 Statistical Analysis, PDF p. 4](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4)
- **Printed evidence:** Table 3 gives intervention baseline energy `2355 (555)` kcal/d; eTable 8 gives `2,355 (544)` for the same displayed N=3,272. The matched control value is `2369 (555)` in both.
- **Rule:** The same baseline group summary should retain its SD; 555 and 544 cannot be reconciled by integer rounding.
- **Alternative source-grounded interpretation:** eTable 8 may use an unstated baseline subset or separate baseline calculation.
- **Exact human question:** What baseline denominator and calculation produced the intervention SD in each table?
- **Checker provenance:** QC-X0004; canonical N041/N212 and S017/S621.
- **Status:** Pending Human Adjudication

## C006 — baseline body-weight summaries differ between Table 1 and eTable 9

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [DOC-001 Table 1, PDF p. 4](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [DOC-004 eTable 9, PDF p. 23](../../joi190106supp3_prod_1635377898.49725.pdf#page=23)
- **Printed evidence:** Table 1 gives intervention/control weight `86.7 (13.0)`/`86.4 (13.0)` kg; eTable 9 gives `86.5 (12.9)`/`86.3 (13.0)` under the same displayed N=3,272/N=3,311.
- **Rule:** Baseline summaries with matched measure, unit, arms, and displayed Ns should agree at printed precision absent a stated distinct population.
- **Alternative source-grounded interpretation:** eTable 9 may use outcome-specific availability or baseline imputation not fully described by its header.
- **Exact human question:** What exact baseline weight denominator and handling rule was used in each display?
- **Checker provenance:** QC-X0005; canonical N015/N225 and S700.
- **Status:** Pending Human Adjudication

## C007 — baseline BMI means differ between Table 1 and eTable 9

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [DOC-001 Table 1, PDF p. 4](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [DOC-004 eTable 9, PDF p. 23](../../joi190106supp3_prod_1635377898.49725.pdf#page=23)
- **Printed evidence:** Table 1 gives BMI `32.5 (3.4)`/`32.5 (3.5)` kg/m²; eTable 9 gives `32.6 (3.4)`/`32.6 (3.5)` for the same displayed N=3,272/N=3,311.
- **Rule:** Matched baseline group means should agree at the displayed one-decimal precision unless a distinct derivation or population is stated.
- **Alternative source-grounded interpretation:** BMI may have been recomputed under different rounding or missing-data conventions, neither of which is stated.
- **Exact human question:** Were BMI inputs, derivation, denominator, or rounding different between the two tables?
- **Checker provenance:** QC-X0006; canonical N016/N227 and S700.
- **Status:** Pending Human Adjudication

## C008 — Figure 4 threshold labels do not preserve the Methods boundary operators

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-001 Outcomes, PDF p. 4](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [DOC-001 Figure 4, PDF p. 10](../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=10)
- **Printed evidence:** Methods defines clinically meaningful changes as “at least” 5%, 5 mm Hg, or 2.5 mm Hg as applicable. Figure 4 uses strict `>5%`/`>5 mm Hg` labels and gives the diastolic label as `Reduction 2.5 mm Hg` without an operator.
- **Rule:** A label for the same classified outcome should preserve whether the boundary is inclusive or strict.
- **Alternative source-grounded interpretation:** The analysis may have used one consistent rule and only the prose or figure typography may be imprecise; the supplied package does not identify which.
- **Exact human question:** Which boundary operator was implemented for each Figure 4 classification, and which displayed labels should be harmonized?
- **Checker provenance:** QC-S003; canonical S044-S054 and N020/N083-N093.
- **Status:** Pending Human Adjudication

## C009 — eTable 4 total-olive-oil baseline row conflicts with the table's median/IQR convention

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [DOC-004 eTable 4 total-olive-oil row, PDF p. 10](../../joi190106supp3_prod_1635377898.49725.pdf#page=10); [DOC-004 eTable 4 footnote, PDF p. 11](../../joi190106supp3_prod_1635377898.49725.pdf#page=11); [DOC-004 eTable 2 comparator, PDF p. 3](../../joi190106supp3_prod_1635377898.49725.pdf#page=3); [DOC-004 eTable 7 comparator, PDF p. 17](../../joi190106supp3_prod_1635377898.49725.pdf#page=17)
- **Printed evidence:** eTable 4 labels the total-olive-oil baseline as `mean (SD)` and prints `350 (175, 350)` in both arms; its continuation footnote says baseline food data are `median (IQR)`, as do matching food tables and other rows.
- **Rule:** Mean (SD) and median (IQR) are different summary conventions; a row label and its table footnote cannot both define the same display absent an explicit exception.
- **Alternative source-grounded interpretation:** Total olive oil may have an unstated row-specific convention, although no such exception appears in the supplied package.
- **Exact human question:** Should the eTable 4 row be labelled median (IQR), or is there a source-supported row-specific mean (SD) definition?
- **Checker provenance:** QC-S2-001; canonical S251.
- **Status:** Pending Human Adjudication

## Registration summary

- Stable candidates: C001, C002, C003, C004, C005, C006, C007, C008, C009.
- All nine remain Pending Human Adjudication.
- No assigned ID was suppressed, merged after registration, or created from display-zero notation.
