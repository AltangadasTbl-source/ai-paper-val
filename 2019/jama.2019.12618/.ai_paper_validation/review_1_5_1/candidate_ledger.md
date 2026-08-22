# Candidate ledger

All entries are **Pending Human Adjudication**.  The eight stable IDs below follow the coordinator-approved merge map. C007 and C008 are the only duplicate merges; their numeric and cross-source provenance is retained. No severity, validity judgment, disposition, or correction is assigned.

## C001 — protocol timeline end date

**Status:** Pending Human Adjudication.

**Category:** Numeric or arithmetic inconsistency.

**Checker provenance:** Numeric consistency `N044` (`parts/numeric_checks_N001_N094.md`).

**Exact source locations:** [Protocol PDF p. 11, Table 1](../../joi190092supp2_prod.pdf#page=11).

**Printed evidence:** Enrollment: November 2012 through May 2015; six-month completion: through December 2015; maximum 12-month follow-up plus one-month window: through July 2015.

**Comparison logic and calculation:** May 2015 + 12 months + 1-month window ends no earlier than June 2016. July 2015 is also earlier than the printed December 2015 six-month completion; calendar dates have no rounding tolerance.

**Supported alternatives:** A typographical year or a schedule limited to an earlier cohort.

**Human verification steps:** Check the final amendment and confirm the July date and applicable cohort.

## C002 — eligible failure total vs switching denominators

**Status:** Pending Human Adjudication.

**Category:** Denominator, proportion, or total inconsistency.

**Checker provenance:** Numeric consistency `N010` (`parts/numeric_checks_N001_N094.md`), with source relationship `N009` and Table 2/Figure 1 as supporting evidence.

**Exact source locations:** [Main PDF p. 7](../../jama_rathinam_2019_oi_190092.pdf#page=7); [main PDF p. 6, Table 2](../../jama_rathinam_2019_oi_190092.pdf#page=6); [main PDF p. 3, Figure 1](../../jama_rathinam_2019_oi_190092.pdf#page=3).

**Printed evidence:** 49 of 68 eligible failures switched; arm fractions are 20/32 (62.5%) and 29/42 (69.0%). Table 2 gives 32 and 42 failures; Figure 1 gives 20 and 29 switches.

**Comparison logic and calculation:** 20+29=49 and 32+42=74. The implied arm denominators exceed the stated eligible total by 74−68=6, while the individual fractions are correct.

**Supported alternatives:** 32 and 42 may be all failures, with 68 a separate eligible subset.

**Human verification steps:** Identify the denominator for each fraction and allocation of six ineligible failures by original arm.

## C003 — allocation block sizes

**Status:** Pending Human Adjudication.

**Category:** Cross-document numeric inconsistency.

**Checker provenance:** Cross-source `N002` and `S014` (`parts/cross_source_N001_N094_S001_S025.md`); later SAP allocation records `N196` and `N237` provide version-specific alternative evidence.

**Exact source locations:** [Main PDF p. 2](../../jama_rathinam_2019_oi_190092.pdf#page=2); [Protocol PDF p. 13](../../joi190092supp2_prod.pdf#page=13).

**Printed evidence:** The article lists permutated blocks 4 and 6; the protocol lists 4, 6, or 8 with equal probability.

**Comparison logic and calculation:** Matched allocation descriptions state different possible-block sets: `{4,6}` versus `{4,6,8}`.

**Supported alternatives:** A later amendment or implementation choice may have removed size 8, or the article may describe realized blocks. The supplied SAP at PDF p. 9 and revised SAP at pp. 49–50 specify only block sizes 4 (probability 2/3) and 6 (probability 1/3), matching the article's possible-size set and showing version-specific definitions.

**Human verification steps:** Review the approved amendment and randomization-list specification, and determine whether the later SAP rule on PDF pp. 9 and 49–50 governed the generated allocation sequence.

## C004 — six-month success injection-after-90-days criterion

**Status:** Pending Human Adjudication.

**Category:** Cross-document numeric inconsistency.

**Checker provenance:** Cross-source `N004`, `N026`, and `S024` (`parts/cross_source_N001_N094_S001_S025.md`), protocol endpoint relationship `N112`, and SAP sensitivity relationship `N263` on physical SAP PDF p. 70.

**Exact source locations:** [Main PDF p. 3](../../jama_rathinam_2019_oi_190092.pdf#page=3); [Protocol manual PDF p. 80](../../joi190092supp2_prod.pdf#page=80).

**Printed evidence:** The manual requires no periocular/intravitreal corticosteroid injection after 90 days; the article’s enumerated success definition omits injection status and calls other injections protocol deviations.

**Comparison logic and calculation:** Otherwise matched six-month patient-level success definitions differ by an explicit 90-day injection classification rule that could change a success count.

**Supported alternatives:** The article may abbreviate a separate operational failure rule, or the endpoint may have changed across versions. The SAP sensitivity section on physical PDF p. 70 classifies a corticosteroid injection at 90 days using inflammation status at injection; this is supplied context but does not establish the primary-analysis rule.

**Human verification steps:** Verify version-in-force, post-day-90 injection classifications, and treatment of the eight reported injection cases in the 64/96 and 56/98 results.

## C005 — missed-dose Welch P=.87 compatibility

**Status:** Pending Human Adjudication.

**Category:** Statistical reporting inconsistency.

**Checker provenance:** Statistical pass 1 `S006` (`checkers/statistical_pass_1.md`).

**Exact source locations:** [Main PDF p. 4](../../jama_rathinam_2019_oi_190092.pdf#page=4); [main PDF p. 6, Table 2](../../jama_rathinam_2019_oi_190092.pdf#page=6).

**Printed evidence:** MTX 4.6 (SD 1.0)% (`n=96`) versus MMF 4.3 (SD 0.5)% (`n=98`), P=.87; the methods name a Welch t test.

**Comparison logic and calculation:** From printed summaries, SE≈`sqrt(1.0²/96+0.5²/98)=0.114`; t≈`0.3/0.114=2.63`; two-sided Welch P≈.01, not .87. This diagnostic does not replace the reported analysis.

**Supported alternatives:** Different analytic N, unrounded/scaled values, summary definition, or another comparison’s P value.

**Human verification steps:** Inspect row-specific analysis output and unrounded input summaries.

## C006 — main Table 3 MMF n=109 header vs supplement N=108/percentages

**Status:** Pending Human Adjudication.

**Category:** Cross-document numeric inconsistency.

**Checker provenance:** Main-table records `N029`, `N030`, and `N034`; cross-source supplement records `N276`–`N278` (`parts/cross_source_N249_N282_S081_S101.md`).

**Exact source locations:** [Main PDF p. 8, Table 3](../../jama_rathinam_2019_oi_190092.pdf#page=8); [Supplement PDF p. 10, eTable 4](../../joi190092supp1_prod.pdf#page=10); [p. 11, eTable 5](../../joi190092supp1_prod.pdf#page=11); [p. 12, eTable 6](../../joi190092supp1_prod.pdf#page=12).

**Printed evidence:** Main Table 3 header is MMF n=109 but has 19 (17.6) for decreased/defective vision and 59 (54.6) for fatigue. eTables 4–6 each label the treated MMF population N=108; eTable 4 repeats the matched decreased/defective-vision value 19 (17.6). The 59 (54.6) fatigue value is an internal main-table denominator comparison, not a repeated eTable 6 cell. Main Table 3's footnote says one assigned patient never received study drug.

**Comparison logic and calculation:** 19/108=17.6% and 59/108=54.6% at display precision; with 109 they are 17.4% and 54.1%.

**Supported alternatives:** The main header may be randomized N and percentages treated-N, signaled only by footnote.

**Human verification steps:** Confirm the approved table-denominator convention and each MMF percentage.

## C007 — eTable 9 MMF serious diarrhea 1 (3.4) vs N=20

**Status:** Pending Human Adjudication.

**Category:** Denominator, proportion, or total inconsistency.

**Checker provenance:** Numeric consistency `N281` (`parts/numeric_checks_N189_N282.md`); cross-source `N280`/`N281` (`parts/cross_source_N249_N282_S081_S101.md`). Merged as the same cell, comparator, and arithmetic rule.

**Exact source locations:** [Supplement PDF p. 15, eTable 9](../../joi190092supp1_prod.pdf#page=15), MMF N=20 Serious Systemic diarrhea row.

**Printed evidence:** The cell is 1 (3.4), and entries are number of patients reporting at least one event (%).

**Comparison logic and calculation:** `100×1/20=5.0%` to one decimal, not 3.4%; N=20 cells elsewhere show 1 (5.0), while N=29 MTX cells show 1 (3.4).

**Supported alternatives:** An unprinted denominator near 29, header error, transposed percentage, or typesetting error.

**Human verification steps:** Verify the AE tabulation, exact denominator, and whether a subset exception exists.

## C008 — eTable 8 serious-ocular hypertension label vs eTable 1 surgery-required definition

**Status:** Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency.

**Checker provenance:** Numeric consistency `N282` (`parts/numeric_checks_N189_N282.md`); cross-source `N279`/`N282` (`parts/cross_source_N249_N282_S081_S101.md`). Merged as the same eTable 1 criterion and eTable 8 label comparison.

**Exact source locations:** [Supplement PDF p. 5, eTable 1](../../joi190092supp1_prod.pdf#page=5); [Supplement PDF p. 14, eTable 8](../../joi190092supp1_prod.pdf#page=14).

**Printed evidence:** eTable 1 calls ≥24 mm Hg non-serious and surgery required serious; eTable 8 places “Ocular hypertension >24mm Hg” under both Non-Serious Ocular and Serious Ocular, with the serious row showing MTX 1 (1.6) and MMF 0 (0.0). The eTable 8 footnote actually refers to “eFigure 2,” not eTable 1; no eFigure 2 content appears in the supplied supplement text. As an additional direct comparator, eTable 9 on PDF p. 15 labels the serious row “Ocular hypertension, surgery required.”

**Comparison logic and calculation:** Under the supplied eTable 1 definitions, the serious-row label states the non-serious pressure threshold rather than the surgery requirement and duplicates eTable 8's own non-serious row label. Percentages are not the mismatch; the unresolved “eFigure 2” reference is part of the human source check.

**Supported alternatives:** An abbreviated surgery-required event, copied threshold label, or unprinted cohort definition.

**Human verification steps:** Review the event-level case, cohort criterion, and matching eTable 9 serious row.

## Ledger limitations

The direct sources do not include participant-level classifications, unrounded analytic data, final amendment history, randomization lists, or full statistical output. These missing inputs restrict explanation of the printed discrepancies but do not erase their stated source-grounded comparisons.
