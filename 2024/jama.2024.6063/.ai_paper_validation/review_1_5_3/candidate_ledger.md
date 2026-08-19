# Stable Candidate Ledger

All 16 candidates below are **Pending Human Adjudication**. They are quality-control observations,
not AI dispositions. Stable IDs were assigned only after merging genuine duplicates. The statistical
proposals SP1-01, SP1-02, and SP1-03 duplicate NP-009, NP-010, and NP-011 respectively and are merged
into C009, C010, and C011 with both checker provenances retained. No other proposals share the same
printed values, comparator, and consistency rule.

## C001 — Placebo discontinuation counts differ between Figure 1 and the Results text

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Main PDF p. 3, Figure 1](<../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3>); [Main PDF p. 7, Results](<../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7>).
- **Source evidence:** Figure 1 reports 132 placebo participants randomized, 111 completing treatment, and 21 discontinuing. Results reports 23 placebo participants withdrew or were lost and 222 total completed.
- **Comparator and rule:** For the same arm-level completion disposition, Figure 1 gives `111 + 21 = 132`; Results implies `132 - 23 = 109`. Across arms, Figure 1 has 38 discontinuations and 224 completers, while Results has 40 withdrawals/losses and 222 completers.
- **Direct observation and derived diagnostic:** The counts are printed observations; the arithmetic identity has zero tolerance. It is inferred, but not established, that “discontinued” and “withdrew or were lost” use the same disposition definition.
- **Source-grounded alternatives:** Two placebo participants may be in a separately defined withdrawal/loss category absent from Figure 1, or one display may contain a transcription difference.
- **Remaining human question:** What are the dispositions of the two additional placebo participants in the Results count, and how do they reconcile with 111 Figure 1 completers?
- **Checker provenance:** Numeric proposal NP-001.

## C002 — eTable 2 names 167 and 165 for the overall adherence population

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source location:** [Supplement 3 PDF p. 3, eTable 2](<../../joi240048supp3_prod_1727199125.83025.pdf#page=3>).
- **Source evidence:** The overall 0-24-week row states `n = 167` and prints 82 (98.8%) and 81 (96.4%); its footnote says adherence was calculated for available pill-count data and completers, `n = 165 (75%)`.
- **Comparator and rule:** The displayed percentages imply denominators 83 and 84: `82/83 = 98.8%`, `81/84 = 96.4%`, and `83 + 84 = 167`, not 165.
- **Direct observation and derived diagnostic:** Both totals and cells are printed; percentage reconciliation uses one-decimal rounding tolerance of 0.05 percentage point.
- **Source-grounded alternatives:** The footnote may describe a narrower unlabelled subset, or it may be stale relative to the row.
- **Remaining human question:** What precise population does the footnote's 165 denote, and why does it differ from the row's reproducible denominator of 167?
- **Checker provenance:** Numeric proposal NP-002.

## C003 — eTable 5 krill “Smaller by 1 unit” percentage conflicts with 10 of 107

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Source evidence:** Krill oil `Smaller - 1 unit` is `10 (12%)`; arm total is `107 (100%)`.
- **Comparator and rule:** `100 × 10/107 = 9.3458%`, rounding to 9%, not 12%.
- **Direct observation and derived diagnostic:** Printed count, percentage, and total are direct; whole-percentage tolerance is 0.5 percentage point.
- **Source-grounded alternatives:** An unprinted denominator could yield about 12%, but no such denominator is identified.
- **Remaining human question:** Is the count, percentage, or displayed arm total the intended value?
- **Checker provenance:** Numeric proposal NP-003.

## C004 — eTable 5 krill “No change” percentage conflicts with 80 of 107

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Source evidence:** Krill oil `No change` is `80 (72%)`; arm total is `107 (100%)`.
- **Comparator and rule:** `100 × 80/107 = 74.7664%`, rounding to 75%, not 72%.
- **Direct observation and derived diagnostic:** Printed cells are direct; whole-percentage tolerance is 0.5 percentage point.
- **Source-grounded alternatives:** A different unprinted denominator could yield 72%.
- **Remaining human question:** Which of 80, 72%, or 107 should define this category?
- **Checker provenance:** Numeric proposal NP-004.

## C005 — eTable 5 krill “Larger by 1 unit” percentage conflicts with 12 of 107

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Source evidence:** Krill oil `Larger - 1 unit` is `12 (12%)`; arm total is `107 (100%)`.
- **Comparator and rule:** `100 × 12/107 = 11.2150%`, rounding to 11%, not 12%.
- **Direct observation and derived diagnostic:** Printed cells are direct; whole-percentage tolerance is 0.5 percentage point.
- **Source-grounded alternatives:** A different denominator could yield 12%, but none is printed for this row.
- **Remaining human question:** Was another denominator used, or should the percentage be reconciled to 12 of 107?
- **Checker provenance:** Numeric proposal NP-005.

## C006 — eTable 5 placebo “Smaller by 2 units” percentage conflicts with 2 of 109

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Source evidence:** Placebo `Smaller - 2 units` is `2 (1.9%)`; arm total is `109 (100%)`.
- **Comparator and rule:** `100 × 2/109 = 1.8349%`, rounding to 1.8% at one decimal, not 1.9%.
- **Direct observation and derived diagnostic:** Printed cells are direct; one-decimal tolerance is 0.05 percentage point and the discrepancy is approximately 0.065.
- **Source-grounded alternatives:** A denominator near 105 would display 1.9%, but none is supplied.
- **Remaining human question:** Was another denominator used, or is the displayed percentage rounded or transcribed incorrectly?
- **Checker provenance:** Numeric proposal NP-006.

## C007 — eTable 5 placebo “Smaller by 1 unit” percentage conflicts with 16 of 109

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Source evidence:** Placebo `Smaller - 1 unit` is `16 (12%)`; arm total is `109 (100%)`.
- **Comparator and rule:** `100 × 16/109 = 14.6789%`, rounding to 15%, not 12%.
- **Direct observation and derived diagnostic:** Printed cells are direct; whole-percentage tolerance is 0.5 percentage point.
- **Source-grounded alternatives:** A denominator near 133 would yield 12%, but it conflicts with the displayed 109 total.
- **Remaining human question:** Which of the count, percentage, or total was intended?
- **Checker provenance:** Numeric proposal NP-007.

## C008 — eTable 5 placebo “No change” percentage conflicts with 75 of 109

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Source evidence:** Placebo `No change` is `75 (72%)`; arm total is `109 (100%)`.
- **Comparator and rule:** `100 × 75/109 = 68.8073%`, rounding to 69%, not 72%.
- **Direct observation and derived diagnostic:** Printed cells are direct; whole-percentage tolerance is 0.5 percentage point.
- **Source-grounded alternatives:** A denominator near 104 would yield 72%, but none is stated.
- **Remaining human question:** Is 72% based on another population, or should it reconcile to 75 of 109?
- **Checker provenance:** Numeric proposal NP-008.

## C009 — eTable 4 repeats week-4 function changes in the weight-bearing-pain row

- **Category:** Numeric or arithmetic inconsistency
- **Exact source location:** [Supplement 3 PDF p. 5, eTable 4](<../../joi240048supp3_prod_1727199125.83025.pdf#page=5>).
- **Source evidence:** Week-4 weight-bearing pain prints arm changes `-84 (-122 to -46)` and `-103 (-141 to -65)`; the adjacent week-4 function row prints the exact same pair. Weight-bearing final/baseline means are 100/127 and 108/141.
- **Comparator and rule:** Exact paired estimate/interval repetition across distinct scales is the primary rule. Descriptive subtractions are `100 - 127 = -27` and `108 - 141 = -33`, not -84 and -103; these are diagnostics because modelled changes need not equal raw subtraction.
- **Direct observation and derived diagnostic:** The duplicate cells and distinct labels are direct. A copied or misplaced pair is inferred, not established.
- **Source-grounded alternatives:** An unlabelled model estimand could differ from descriptive subtraction, but the supplied definitions do not explain exact duplication across distinct outcomes.
- **Remaining human question:** Were function cells copied into weight-bearing pain, and what are the intended arm-change values?
- **Checker provenance:** Numeric NP-009 and statistical pass-1 SP1-01 (merged genuine duplicate; S036/S048).

## C010 — eTable 4 repeats week-4 back-pain results in week-12 lower-leg strength

- **Category:** Statistical reporting inconsistency
- **Exact source location:** [Supplement 3 PDF p. 6, eTable 4](<../../joi240048supp3_prod_1727199125.83025.pdf#page=6>).
- **Source evidence:** Week-12 strength and week-4 back pain both print arm changes `-2.8 (-6.0 to 0.4)` and `-4.2 (-7.4 to -1.1)` and the full between-group result `-1.4 (-5.9 to 3.0)`, `P=.53`. Strength final/baseline values are 72.6/66.5 and 70.2/65.9.
- **Comparator and rule:** The complete inferential result repeats across outcomes with different units and directions. Descriptive strength differences are +6.1 and +4.3, a diagnostic rather than a reconstructed model result.
- **Direct observation and derived diagnostic:** Exact repetition is direct; copying is an inferred explanation.
- **Source-grounded alternatives:** Coincidence is mathematically possible, but no source definition explains identical full outputs and arm changes for distinct endpoints.
- **Remaining human question:** Do the strength cells belong to strength, and what does the source analysis output show?
- **Checker provenance:** Numeric NP-010 and statistical pass-1 SP1-02 (merged genuine duplicate; S060/S066).

## C011 — eTable 4 repeats the week-12 hsCRP result in fasting glucose

- **Category:** Statistical reporting inconsistency
- **Exact source location:** [Supplement 3 PDF p. 6, eTable 4](<../../joi240048supp3_prod_1727199125.83025.pdf#page=6>).
- **Source evidence:** Week-12 hsCRP and fasting glucose both print `0.07 (-1.19 to 1.33)`, `P=.92`; glucose arm changes are `0.09 (-0.07 to 0.24)` and `0.15 (-0.01 to 0.31)` and differ from hsCRP arm changes.
- **Comparator and rule:** Exact estimate/CI/P repetition across distinct measures and units is the direct consistency rule. The unadjusted glucose change contrast `0.09 - 0.15 = -0.06` is only diagnostic.
- **Direct observation and derived diagnostic:** Repeated printed fields are direct; a copied table cell is inferred.
- **Source-grounded alternatives:** A separately modelled glucose result could differ from arm-change subtraction, but no supplied rule explains exact equality with hsCRP.
- **Remaining human question:** Does the printed cell belong to fasting glucose, and what are the intended estimate, interval, and P value?
- **Checker provenance:** Numeric NP-011 and statistical pass-1 SP1-03 (merged genuine duplicate; S076/S084).

## C012 — Key Points and other matched primary-result displays use opposite signs

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [Main PDF p. 2, Key Points](<../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2>); [p. 1, Abstract](<../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1>); [p. 6, Table 2](<../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6>); [p. 7, Results](<../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7>); [Supplement 3 p. 2, eTable 1](<../../joi240048supp3_prod_1727199125.83025.pdf#page=2>).
- **Source evidence:** Key Points prints `0.30 (95% CI -6.9 to 6.4; P=.94)`; the other main locations print `-0.3`, and eTable 1 prints `-0.27`, with matching interval/P.
- **Comparator and rule:** The matched displays have the same endpoint, time, interval, and P value, while `-0.27` rounds to `-0.3`, not `+0.30`. The package does not define a common signed operand order, so no krill-minus-placebo orientation is assumed.
- **Direct observation and derived diagnostic:** Opposite printed signs across otherwise matched displays are direct. A shared orientation, absolute-magnitude intent, or lost sign is inferred rather than established.
- **Source-grounded alternatives:** Key Points may intend an unsigned magnitude; another display may use an unstated opposite operand order; or a sign may have been lost.
- **Remaining human question:** What signed contrast orientation was intended in each location, and was Key Points intended as an absolute magnitude or a signed difference?
- **Checker provenance:** Cross-source proposal 1.

## C013 — Placebo extremity-pain event count is 6 in Table 3 and 5 elsewhere

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [Main PDF p. 1, Abstract](<../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1>); [Main PDF p. 8, Table 3 and narrative](<../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8>); [Supplement 3 p. 10, eTable 7](<../../joi240048supp3_prod_1727199125.83025.pdf#page=10>).
- **Source evidence:** Table 3 prints pain in extremity as 1/6 krill/placebo; Abstract, narrative, and eTable 7 print 1/5.
- **Comparator and rule:** These are matched event counts for the same arm and category; exact integers should agree.
- **Direct observation and derived diagnostic:** The difference is directly printed. A coding-aggregate distinction is possible but not defined.
- **Source-grounded alternatives:** “Lower-extremity” and “in extremity” could theoretically be different aggregates, though the surrounding matched rows and citations support identity.
- **Remaining human question:** Does Table 3 use a different event aggregate, or is one placebo count incorrect?
- **Checker provenance:** Cross-source proposal 2.

## C014 — Table 3 regular-adverse-event footnote points to eTable 4 instead of eTable 7

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [Main PDF p. 8, Table 3 footnote a and narrative](<../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8>); [Supplement 3 p. 5, eTable 4](<../../joi240048supp3_prod_1727199125.83025.pdf#page=5>); [Supplement 3 p. 10, eTable 7](<../../joi240048supp3_prod_1727199125.83025.pdf#page=10>).
- **Source evidence:** Footnote a sends detailed regular-adverse-event information to eTable 4; eTable 4 contains secondary outcome time series. The narrative points to eTable 7, which is the detailed adverse-event table.
- **Comparator and rule:** A source cross-reference should identify a table containing the stated subject.
- **Direct observation and derived diagnostic:** Table identifiers and headers are direct; stale renumbering is an inferred explanation.
- **Source-grounded alternatives:** The footnote may retain an earlier supplement numbering scheme.
- **Remaining human question:** Which eTable reference was intended in Table 3 footnote a?
- **Checker provenance:** Cross-source proposal 3.

## C015 — Table 3 serious-adverse-event footnote points to eTables 5 and 6 instead of eTable 8

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [Main PDF p. 8, Table 3 footnote c and narrative](<../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8>); [Supplement 3 p. 8, eTable 5](<../../joi240048supp3_prod_1727199125.83025.pdf#page=8>); [Supplement 3 p. 9, eTable 6](<../../joi240048supp3_prod_1727199125.83025.pdf#page=9>); [Supplement 3 p. 14, eTable 8](<../../joi240048supp3_prod_1727199125.83025.pdf#page=14>).
- **Source evidence:** Footnote c sends comprehensive serious-event detail to eTables 5 and 6, which contain WORMS score and analgesic-use tables. The narrative points to eTable 8, the serious-adverse-event table.
- **Comparator and rule:** A source cross-reference should identify the table containing the stated subject.
- **Direct observation and derived diagnostic:** Table identifiers and contents are direct; stale renumbering is inferred.
- **Source-grounded alternatives:** The footnote may reflect an earlier supplement layout.
- **Remaining human question:** Which serious-event table reference was intended in footnote c?
- **Checker provenance:** Cross-source proposal 4.

## C016 — Main-text 95% adherence does not reproduce the cited eTable 2 overall result

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [Main PDF p. 7, Process Measures](<../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7>); [Supplement 3 p. 3, eTable 2](<../../joi240048supp3_prod_1727199125.83025.pdf#page=3>).
- **Source evidence:** Main text states 95% consumed at least 80% of softgels over 24 weeks. The cited eTable overall row gives 82 and 81 adherent participants, arm percentages 98.8% and 96.4%, and overall `n=167`; the footnote separately names 165.
- **Comparator and rule:** Using the row's values, `(82 + 81)/167 = 97.6%`, conventionally 98%, not 95%. The same threshold and period are named.
- **Direct observation and derived diagnostic:** Printed statements are direct; pooled arithmetic is derived. The narrative denominator is absent.
- **Source-grounded alternatives:** The 95% may use an unstated subset or an earlier table version.
- **Remaining human question:** What numerator and denominator produced 95%, and how do they reconcile with the cited row and its footnote?
- **Checker provenance:** Cross-source proposal 5. This remains distinct from C002 because its comparator is main text versus the table row, whereas C002 compares the table row with its footnote.
