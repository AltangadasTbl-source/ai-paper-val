# Quantitative Quality-Control Consistency Review — Workflow 1.5.3

## Pending Human Adjudication

Every candidate in this report is **Pending Human Adjudication**. These are source-grounded quantitative reporting quality-control observations, not conclusions about validity, authorship, misconduct, or the paper's conclusions.

## Executive Quality-Control Summary

Complete review coverage registered **16 stable candidates (C001–C016)**. The candidates concern reported counts, denominators and percentages, repeated table output, a sign/orientation discrepancy, adverse-event counts, cross-references, and an adherence percentage. Small preventable reporting defects can matter for downstream evidence extraction; this report does not claim that any defect propagated, changed a conclusion, or caused serious harm.

## Package and Reused-Evidence Provenance

The supplied package contains four direct PDF sources. Direct source PDFs were the evidence authority; reusable native text, layout text, page maps, and rendered material were used as locators and transcription aids. The mechanical recheck confirmed every cited candidate location against the original supplied PDF page. Source and reusable-artifact inventories, hashes, and fitness assessments are recorded in the versioned review artifacts.

## Scope, Complete Coverage, and Exclusions

All **41 of 41** PDF-page source units were mapped: main article 10/10, Supplement 1 15/15, Supplement 2 1/1, and Supplement 3 15/15. Reusable and fresh-required units partitioned every source: 24 reusable and 17 fresh-required units. No scientific-coverage gap remains.

The review addressed quantitative reporting consistency: arithmetic, denominators, percentages, statistics, duplicated output, sign/direction, matched cross-document values, labels, and rate/count distinctions. It did not conduct a broad clinical, methodological, misconduct, raw-data, or external-literature audit. Coherent display-zero P values were not candidates; no assigned relationship contained `P = 0`, `p = 0.000`, or an equivalent display zero.

## Quantitative and Statistical Relationship Coverage

Numeric/reporting relationships **N001–N028** were completed. Inferential-statistical relationships **S001–S091** were completed in two fresh, distinct statistical passes: pass 1 and pass 2. Pass 2 revisited all 91 S relationships and the complete cross-lane ledger/recheck facts; it added no stable candidate. The statistically implicated existing candidates are C009, C010, C011, and C012. Candidate registration, evidence recheck, and evidence-quality audit each cover the identical stable set C001–C016.

## Candidate Index

| ID | Candidate |
|---|---|
| C001 | Placebo discontinuation counts differ between Figure 1 and Results |
| C002 | eTable 2 names 167 and 165 for overall adherence |
| C003 | eTable 5 krill “Smaller by 1 unit” percentage |
| C004 | eTable 5 krill “No change” percentage |
| C005 | eTable 5 krill “Larger by 1 unit” percentage |
| C006 | eTable 5 placebo “Smaller by 2 units” percentage |
| C007 | eTable 5 placebo “Smaller by 1 unit” percentage |
| C008 | eTable 5 placebo “No change” percentage |
| C009 | eTable 4 duplicated week-4 changes |
| C010 | eTable 4 duplicated lower-leg-strength result |
| C011 | eTable 4 duplicated hsCRP/glucose result |
| C012 | Opposite signs in matched primary-result displays |
| C013 | Placebo extremity-pain count differs across displays |
| C014 | Regular-adverse-event footnote cross-reference |
| C015 | Serious-adverse-event footnote cross-reference |
| C016 | Main-text 95% adherence versus cited eTable 2 |

## Candidate Evidence Cards

## C001 — Placebo discontinuation counts differ between Figure 1 and the Results text

**Candidate statement:** Figure 1 and Results print different placebo-arm discontinuation/completion counts if their disposition terms refer to the same participants.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Main article — PDF p. 3](<../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3>); [Main article — PDF p. 7](<../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7>).

**Source evidence:** Figure 1 prints 132 placebo randomized, 111 completing treatment, and 21 discontinuing. Results prints 23 placebo participants withdrew or were lost and 222 total completed.

**Reported-versus-comparator:** Figure 1’s placebo 21 discontinuations and 111 completers versus Results’ 23 withdrawals/losses and implied 109 placebo completers.

**Reasoning procedure:** Apply randomized-arm accounting only conditionally, because the source does not define the compared disposition categories as identical.

**Calculation:** `111 + 21 = 132`; `132 - 23 = 109`, not 111. Across arms, Figure 1 has 38 discontinuations/224 completers versus Results’ 40/222.

**Alternative source-grounded interpretations:** Results may include two placebo participants outside Figure 1’s discontinuation category, or one display may have a transcription difference.

**Mechanical evidence recheck:** Both pages and all printed counts were found; category equivalence remains undefined.

**Quality-control relevance:** A disposition-count mismatch can impede reproducible participant-flow extraction.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an inconsistent placebo completion or discontinuation count; no propagation or conclusion change is asserted.

**Human verification steps:** Reconcile participant-level dispositions and define the Figure 1 and Results completion/withdrawal categories.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — eTable 2 names 167 and 165 for the overall adherence population

**Candidate statement:** The overall eTable 2 row is supported by 167 participants while its adherence footnote names 165.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 3 — PDF p. 3](<../joi240048supp3_prod_1727199125.83025.pdf#page=3>).

**Source evidence:** The overall 0–24-week row prints `n = 167`, 82 (98.8%), and 81 (96.4%); the footnote names `n = 165` for pill-count data and completers.

**Reported-versus-comparator:** Row total 167 and percentage-supported arm denominators versus footnote total 165.

**Reasoning procedure:** Reproduce the two displayed one-decimal percentages and compare their summed denominators with the footnote population.

**Calculation:** `82/83 × 100 = 98.7952%`; `81/84 × 100 = 96.4286%`; `83 + 84 = 167`, not 165.

**Alternative source-grounded interpretations:** The footnote may describe an unlabelled narrower subset, or it may be stale relative to the row.

**Mechanical evidence recheck:** The row, footnote, counts, and percentages were found and reproduced.

**Quality-control relevance:** A denominator definition is required to interpret and extract adherence percentages consistently.

**Potential downstream evidence impact:** If confirmed, a reviewer could copy the wrong adherence denominator or population; no downstream use or conclusion change is asserted.

**Human verification steps:** Identify the precise participant set for 165 and its relation to the row’s 167.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eTable 5 krill “Smaller by 1 unit” percentage conflicts with 10 of 107

**Candidate statement:** The printed 12% does not reproduce from the printed krill count 10 and total 107.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 3 — PDF p. 8](<../joi240048supp3_prod_1727199125.83025.pdf#page=8>).

**Source evidence:** The krill `Smaller - 1 unit` cell is `10 (12%)`; its total is `107 (100%)`.

**Reported-versus-comparator:** Printed 12% versus the percentage from 10/107.

**Reasoning procedure:** Apply whole-percentage rounding to the displayed count divided by the displayed arm total.

**Calculation:** `10/107 × 100 = 9.3458%`, which rounds to 9%, not 12%.

**Alternative source-grounded interpretations:** An unprinted denominator or a different table version could explain the discrepancy.

**Mechanical evidence recheck:** The count, percentage, and total were found; no alternative denominator is printed.

**Quality-control relevance:** Count/percentage reconciliation supports reliable categorical-outcome extraction.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a mismatched category percentage; no propagation or conclusion change is asserted.

**Human verification steps:** Confirm the intended count, percentage, and denominator from the table source.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — eTable 5 krill “No change” percentage conflicts with 80 of 107

**Candidate statement:** The printed 72% does not reproduce from the printed krill count 80 and total 107.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 3 — PDF p. 8](<../joi240048supp3_prod_1727199125.83025.pdf#page=8>).

**Source evidence:** Krill `No change` is `80 (72%)`; the arm total is `107 (100%)`.

**Reported-versus-comparator:** Printed 72% versus the percentage from 80/107.

**Reasoning procedure:** Apply whole-percentage rounding to the printed count and total.

**Calculation:** `80/107 × 100 = 74.7664%`, which rounds to 75%, not 72%.

**Alternative source-grounded interpretations:** A different unprinted denominator or a table-version difference is possible.

**Mechanical evidence recheck:** The printed cells were found; no category-specific denominator is supplied.

**Quality-control relevance:** The observation identifies an unresolved categorical denominator/percentage relationship.

**Potential downstream evidence impact:** If confirmed, a categorical outcome percentage could be copied inconsistently; no downstream effect is claimed.

**Human verification steps:** Verify whether 80, 72%, or 107 is the intended reported value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — eTable 5 krill “Larger by 1 unit” percentage conflicts with 12 of 107

**Candidate statement:** The printed 12% does not reproduce from the printed krill count 12 and total 107.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 3 — PDF p. 8](<../joi240048supp3_prod_1727199125.83025.pdf#page=8>).

**Source evidence:** Krill `Larger - 1 unit` is `12 (12%)`; the arm total is `107 (100%)`.

**Reported-versus-comparator:** Printed 12% versus the percentage from 12/107.

**Reasoning procedure:** Apply whole-percentage rounding to the displayed count and total.

**Calculation:** `12/107 × 100 = 11.2150%`, which rounds to 11%, not 12%.

**Alternative source-grounded interpretations:** Another unprinted denominator or a table-version difference could explain the cells.

**Mechanical evidence recheck:** The count, percentage, and total were found; an alternative denominator is absent.

**Quality-control relevance:** Reconciled count/percentage pairs are needed for reproducible outcome extraction.

**Potential downstream evidence impact:** If confirmed, the percentage for this category could be copied incorrectly; no propagation or conclusion change is asserted.

**Human verification steps:** Verify the source denominator and intended percentage.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — eTable 5 placebo “Smaller by 2 units” percentage conflicts with 2 of 109

**Candidate statement:** The printed 1.9% does not reproduce from the printed placebo count 2 and total 109 at one-decimal precision.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 3 — PDF p. 8](<../joi240048supp3_prod_1727199125.83025.pdf#page=8>).

**Source evidence:** Placebo `Smaller - 2 units` is `2 (1.9%)`; the arm total is `109 (100%)`.

**Reported-versus-comparator:** Printed 1.9% versus the percentage from 2/109.

**Reasoning procedure:** Apply one-decimal percentage rounding with a 0.05 percentage-point tolerance.

**Calculation:** `2/109 × 100 = 1.8349%`, which rounds to 1.8%, not 1.9%.

**Alternative source-grounded interpretations:** A denominator near 105 or a table-version difference could account for 1.9%; neither is supplied.

**Mechanical evidence recheck:** The cell and total were found and the arithmetic was reproduced.

**Quality-control relevance:** The small rounding discrepancy remains a reproducible reporting check, not a conclusion about clinical importance.

**Potential downstream evidence impact:** If confirmed, a detailed categorical percentage could be transcribed differently by evidence users; no propagation or harm is claimed.

**Human verification steps:** Confirm the category denominator and the intended one-decimal value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — eTable 5 placebo “Smaller by 1 unit” percentage conflicts with 16 of 109

**Candidate statement:** The printed 12% does not reproduce from the printed placebo count 16 and total 109.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 3 — PDF p. 8](<../joi240048supp3_prod_1727199125.83025.pdf#page=8>).

**Source evidence:** Placebo `Smaller - 1 unit` is `16 (12%)`; the arm total is `109 (100%)`.

**Reported-versus-comparator:** Printed 12% versus the percentage from 16/109.

**Reasoning procedure:** Apply whole-percentage rounding to the printed count and total.

**Calculation:** `16/109 × 100 = 14.6789%`, which rounds to 15%, not 12%.

**Alternative source-grounded interpretations:** A denominator near 133 would yield 12%, but it conflicts with the printed total; a version difference is also possible.

**Mechanical evidence recheck:** The printed count, percentage, and total were confirmed.

**Quality-control relevance:** The discrepancy affects the reproducibility of a categorical descriptive result.

**Potential downstream evidence impact:** If confirmed, a reviewer could extract a category percentage inconsistent with its displayed total; no downstream outcome is asserted.

**Human verification steps:** Determine which displayed value and denominator are intended.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — eTable 5 placebo “No change” percentage conflicts with 75 of 109

**Candidate statement:** The printed 72% does not reproduce from the printed placebo count 75 and total 109.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 3 — PDF p. 8](<../joi240048supp3_prod_1727199125.83025.pdf#page=8>).

**Source evidence:** Placebo `No change` is `75 (72%)`; the arm total is `109 (100%)`.

**Reported-versus-comparator:** Printed 72% versus the percentage from 75/109.

**Reasoning procedure:** Apply whole-percentage rounding to the printed count and total.

**Calculation:** `75/109 × 100 = 68.8073%`, which rounds to 69%, not 72%.

**Alternative source-grounded interpretations:** A denominator near 104 or a different table version could explain 72%; neither is printed.

**Mechanical evidence recheck:** The cited cell and total were found and the calculation was reproduced.

**Quality-control relevance:** This is a distinct placebo categorical-outcome percentage relationship.

**Potential downstream evidence impact:** If confirmed, a categorical percentage could be copied inconsistently into evidence extraction; no propagation or conclusion change is claimed.

**Human verification steps:** Confirm the applicable denominator and intended percentage.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — eTable 4 repeats week-4 function changes in the weight-bearing-pain row

**Candidate statement:** eTable 4 prints the same two week-4 arm-change estimate/interval pairs for weight-bearing pain and function.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Supplement 3 — PDF p. 5](<../joi240048supp3_prod_1727199125.83025.pdf#page=5>).

**Source evidence:** Weight-bearing pain and the adjacent function row both print `-84 (-122 to -46)` and `-103 (-141 to -65)`; weight-bearing final/baseline values are 100/127 and 108/141.

**Reported-versus-comparator:** Identical arm-change estimate/interval pairs across distinct, separately labelled outcome rows.

**Reasoning procedure:** Apply an exact duplicate-value check; use final-minus-baseline only as a labelled diagnostic, not as reconstruction of model estimates.

**Calculation:** The paired printed values match character for character. Diagnostics: `100 - 127 = -27` and `108 - 141 = -33`, not -84 and -103.

**Alternative source-grounded interpretations:** Modelled changes may differ from descriptive subtraction; copying, displacement, or coincidence is not established from the package.

**Mechanical evidence recheck:** Both rows, labels, values, intervals, and adjustment context were confirmed; source model output is absent.

**Quality-control relevance:** Exact output duplication across endpoints can obstruct accurate endpoint-specific extraction.

**Potential downstream evidence impact:** If confirmed, the two weight-bearing-pain arm-change cells could be copied into evidence products; no propagation or conclusion change is asserted.

**Human verification steps:** Inspect source analysis output, cell-level estimand mapping, and table-production history.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — eTable 4 repeats week-4 back-pain results in week-12 lower-leg strength

**Candidate statement:** eTable 4 prints the complete week-4 back-pain output again for week-12 lower-leg strength.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Supplement 3 — PDF p. 6](<../joi240048supp3_prod_1727199125.83025.pdf#page=6>).

**Source evidence:** Both rows print arm changes `-2.8 (-6.0 to 0.4)` and `-4.2 (-7.4 to -1.1)`, and between-group `-1.4 (-5.9 to 3.0)`, `P = .53`; strength final/baseline values are 72.6/66.5 and 70.2/65.9.

**Reported-versus-comparator:** Identical arm changes, estimate, interval, and P value across differently labelled outcomes, times, units, and directions.

**Reasoning procedure:** Apply exact duplicated-output checking; do not reconstruct adjusted results from descriptive means.

**Calculation:** All displayed output fields match exactly. Diagnostic strength changes are `72.6 - 66.5 = +6.1` and `70.2 - 65.9 = +4.3`.

**Alternative source-grounded interpretations:** A modelled change can differ from subtraction, and coincidence is possible; no supplied definition explains complete identity.

**Mechanical evidence recheck:** All compared fields were confirmed against the source page; model mapping and production history are unavailable.

**Quality-control relevance:** A full repeated inferential result may prevent unambiguous extraction for the strength outcome.

**Potential downstream evidence impact:** If confirmed, the week-12 strength result fields could be copied incorrectly; no propagation or conclusion change is asserted.

**Human verification steps:** Obtain the strength analysis output and table-production source for the intended estimate, interval, and P value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — eTable 4 repeats the week-12 hsCRP result in fasting glucose

**Candidate statement:** eTable 4 prints the same between-group estimate, interval, and P value for week-12 hsCRP and fasting glucose.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Supplement 3 — PDF p. 6](<../joi240048supp3_prod_1727199125.83025.pdf#page=6>).

**Source evidence:** Both rows print `0.07 (-1.19 to 1.33)`, `P = .92`; glucose arm changes are `0.09 (-0.07 to 0.24)` and `0.15 (-0.01 to 0.31)`.

**Reported-versus-comparator:** Identical estimate/interval/P output for separately labelled measures with different arm-level changes.

**Reasoning procedure:** Apply exact duplicate-value and measure-label checking; retain arm-change subtraction as a diagnostic only.

**Calculation:** The three between-group fields match exactly. Diagnostic glucose contrast: `0.09 - 0.15 = -0.06`, which does not reconstruct an adjusted model.

**Alternative source-grounded interpretations:** A separately modelled glucose result may differ from subtraction, and equality may be coincidental; no supplied rule explains the full repeated output.

**Mechanical evidence recheck:** Both rows and all result fields were found; model estimand mapping and source output are absent.

**Quality-control relevance:** Exact duplication can affect the clarity and extractability of the glucose result.

**Potential downstream evidence impact:** If confirmed, the glucose estimate, interval, and P value could be copied inconsistently; no downstream consequence is asserted.

**Human verification steps:** Verify the glucose source analysis output and table-production mapping.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Key Points and other matched primary-result displays use opposite signs

**Candidate statement:** Otherwise matched displays of the 24-week primary result print `+0.30` in Key Points and `-0.3`/`-0.27` elsewhere, without defining a common signed operand order.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Main article — PDF p. 2](<../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2>); [Main article — PDF p. 1](<../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1>); [Main article — PDF p. 6](<../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6>); [Main article — PDF p. 7](<../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7>); [Supplement 3 — PDF p. 2](<../joi240048supp3_prod_1727199125.83025.pdf#page=2>).

**Source evidence:** Key Points prints `0.30 (95% CI -6.9 to 6.4; P = .94)`. Abstract, Table 2, and Results print `-0.3`; eTable 1 prints `-0.27 (-6.92 to 6.38)`, `P = .94`.

**Reported-versus-comparator:** Positive `0.30` in Key Points versus negative matched point estimates with matching intervals and P values.

**Reasoning procedure:** Compare the matched endpoint, 24-week time point, interval, and P value; do not infer an operand orientation absent from the supplied source.

**Calculation:** Rounding `-0.27` to one decimal gives `-0.3`, not `+0.30`.

**Alternative source-grounded interpretations:** Key Points may intend an unsigned magnitude; one display may use an unstated opposite operand order; or a sign may have been lost. The sources do not define a common signed contrast orientation.

**Mechanical evidence recheck:** All five displays and their surrounding matching fields were confirmed. No assertion of krill-minus-placebo orientation is supported.

**Quality-control relevance:** A signed primary-result display needs an explicit, consistent orientation for reproducible extraction.

**Potential downstream evidence impact:** If confirmed, the signed primary mean difference could be copied with the wrong sign or orientation; no propagation, interval change, P-value change, or conclusion change is asserted.

**Human verification steps:** Determine the intended signed operand order in each display and whether Key Points intended an unsigned magnitude or lost sign.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Placebo extremity-pain event count is 6 in Table 3 and 5 elsewhere

**Candidate statement:** Table 3 prints six placebo `Pain in extremity` events, while matched Abstract, narrative, and eTable 7 displays print five.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Main article — PDF p. 1](<../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1>); [Main article — PDF p. 8](<../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8>); [Supplement 3 — PDF p. 10](<../joi240048supp3_prod_1727199125.83025.pdf#page=10>).

**Source evidence:** Table 3 prints pain in extremity as 1 krill and 6 placebo events. Abstract, narrative, and eTable 7 print lower-extremity/pain-in-extremity as 1 and 5.

**Reported-versus-comparator:** Table 3 placebo count 6 versus three matched displays’ placebo count 5.

**Reasoning procedure:** Compare exact event counts while retaining category identity/aggregation as an explicit condition.

**Calculation:** Krill is 1 in all locations; placebo differs by one event: `6 - 5 = 1`.

**Alternative source-grounded interpretations:** The phrasings could denote different coding aggregates, though eTable 7 uses `Pain in extremity` and prints 5; a transcription difference is also possible.

**Mechanical evidence recheck:** All source locations and counts were found. No adverse-event coding dictionary is supplied.

**Quality-control relevance:** Consistent event counts are necessary for transparent adverse-event tabulation.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent placebo event count, not a participant risk; no propagation or conclusion change is asserted.

**Human verification steps:** Consult the coding dictionary and source event listings to confirm category identity and intended Table 3 count.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — Table 3 regular-adverse-event footnote points to eTable 4 instead of eTable 7

**Candidate statement:** Table 3 footnote a directs regular-adverse-event detail to eTable 4, whereas eTable 7 is the supplied adverse-event table cited by the narrative.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Main article — PDF p. 8](<../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8>); [Supplement 3 — PDF p. 5](<../joi240048supp3_prod_1727199125.83025.pdf#page=5>); [Supplement 3 — PDF p. 10](<../joi240048supp3_prod_1727199125.83025.pdf#page=10>).

**Source evidence:** Footnote a cites eTable 4 for detailed information. eTable 4 is `Change in secondary endpoints`; the narrative cites eTable 7, `Summary of adverse events`.

**Reported-versus-comparator:** Footnote destination eTable 4 versus the supplied table that contains the stated adverse-event subject, eTable 7.

**Reasoning procedure:** Compare the cross-reference subject with the cited tables’ printed headers and contents.

**Calculation:** Not applicable; logical header/content matching identifies eTable 4 as a secondary-endpoint table and eTable 7 as the adverse-event table.

**Alternative source-grounded interpretations:** Footnote a may retain an earlier supplement numbering scheme.

**Mechanical evidence recheck:** Footnote, narrative, table titles, and contents were confirmed; production history is absent.

**Quality-control relevance:** Accurate cross-references support traceable access to event details.

**Potential downstream evidence impact:** If confirmed, a reader or extractor could be directed to the wrong supporting table; no propagation or harm is asserted.

**Human verification steps:** Check supplement production history and confirm the intended footnote destination.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C015 — Table 3 serious-adverse-event footnote points to eTables 5 and 6 instead of eTable 8

**Candidate statement:** Table 3 footnote c directs serious-adverse-event detail to eTables 5 and 6, while eTable 8 contains the supplied serious-adverse-event detail.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Main article — PDF p. 8](<../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8>); [Supplement 3 — PDF p. 8](<../joi240048supp3_prod_1727199125.83025.pdf#page=8>); [Supplement 3 — PDF p. 9](<../joi240048supp3_prod_1727199125.83025.pdf#page=9>); [Supplement 3 — PDF p. 14](<../joi240048supp3_prod_1727199125.83025.pdf#page=14>).

**Source evidence:** Footnote c cites eTables 5 and 6. Those tables concern WORMS effusion score and analgesic use; the narrative cites eTable 8, the serious-adverse-event table.

**Reported-versus-comparator:** Footnote destinations eTables 5/6 versus eTable 8, which contains the stated serious-event subject.

**Reasoning procedure:** Compare the footnote claim with printed table titles and the narrative’s matched reference.

**Calculation:** Not applicable; neither eTable 5 nor eTable 6 contains serious-event detail, while eTable 8 does.

**Alternative source-grounded interpretations:** The footnote may reflect an earlier supplement layout or numbering scheme.

**Mechanical evidence recheck:** All cited references, headers, and contents were confirmed; production history is not supplied.

**Quality-control relevance:** Accurate serious-event cross-references are needed for auditable evidence navigation.

**Potential downstream evidence impact:** If confirmed, a reader or evidence extractor could be directed away from the relevant detailed table; no propagation or conclusion change is asserted.

**Human verification steps:** Verify supplement production history and the intended Table 3 footnote-c reference.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C016 — Main-text 95% adherence does not reproduce the cited eTable 2 overall result

**Candidate statement:** The main text’s 95% 24-week adherence statement does not reproduce from the cited eTable 2 overall row, conditional on a shared population.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Main article — PDF p. 7](<../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7>); [Supplement 3 — PDF p. 3](<../joi240048supp3_prod_1727199125.83025.pdf#page=3>).

**Source evidence:** Main text states 95% consumed at least 80% of softgels over 24 weeks and cites eTable 2. The overall row prints `n = 167`, 82 (98.8%), and 81 (96.4%); its footnote separately names 165.

**Reported-versus-comparator:** Main-text 95% versus pooled 163 of 167 from the cited row.

**Reasoning procedure:** Match the named threshold and time period, then compute the row’s pooled percentage while explicitly retaining the absent narrative denominator as a condition.

**Calculation:** `82 + 81 = 163`; `163/167 × 100 = 97.6048%`, displayed as 97.6% or 98%, not 95%.

**Alternative source-grounded interpretations:** The main text may use an unstated subset or earlier table version; the cited table itself names both 167 and 165.

**Mechanical evidence recheck:** Narrative, citation, row, footnote, counts, and percentages were confirmed. The narrative numerator/denominator is absent.

**Quality-control relevance:** A cited adherence percentage needs a defined numerator and denominator to be reproducibly interpreted.

**Potential downstream evidence impact:** If confirmed, a reviewer could copy a 24-week adherence percentage or denominator that differs from the cited table; no propagation or conclusion change is asserted.

**Human verification steps:** Identify the numerator and denominator for 95% and reconcile it with the 163/167 row and separate 165 footnote population.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If a candidate is confirmed, its bounded relevance is to the corresponding count, denominator, percentage, signed estimate, event count, cross-reference, or table-result field that may be copied during evidence extraction. Systematic reviews, meta-analyses, guidelines, and other evidence products may rely on reported values, but this review does not claim that any value has propagated or that any conclusion changed.

## Limitations and Missing Definitions

The supplied package lacks participant-level disposition mapping; complete adherence population definitions; category-specific alternative denominators; source analysis output, covariance specifications, and cell-level estimand mappings; a common signed contrast orientation; adverse-event coding definitions; and supplement production-version histories. These limitations define human questions and do not themselves adjudicate any candidate. See [limitations.md](<review_1_5_3/limitations.md>) for the versioned limitation record.

## Human Adjudication Checklist

For each card, confirm the cited source location, reproduce the stated arithmetic or logical comparison, assess the named source-grounded alternatives, obtain the specifically requested missing source material where needed, and complete all five adjudication fields. No card is ranked, accepted, rejected, or assigned severity in this report.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- **Routing preflight:** PASS; coordinator inference PASS; execution mode INTERACTIVE_CLI.
- **Source coverage:** 41/41 mapped source units; 24 reusable units and 17 fresh-source units.
- **Relationship coverage:** N001–N028 complete; S001–S091 `PASS_1_COMPLETE` and `PASS_2_COMPLETE`.
- **Stable candidate set:** C001–C016 in the ledger, recheck, quality audit, and this report.
- **Evidence authority:** original supplied PDF pages; reusable derivatives were locator/transcription aids.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | `source_inventory.md` |
| main_quantitative_mapper | root/main_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support_quantitative_mapper | root/support_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/support_quantitative_evidence.md` |
| numeric_consistency_reviewer | root/numeric_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/numeric_consistency.md` |
| cross_source_consistency_reviewer | root/cross_source_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| quality_control_auditor | root/quality_control_auditor | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | `limitations.md` |

### Performance profile

- **Target basis:** This package has 41 physical PDF-page source units across four PDFs. Twenty-four units have usable page-matched native text, while 17 units require fresh direct-source mapping (the main article's unextracted p10, all 15 protocol pages, and the one-page statistical analysis plan). The work also requires four-source reconciliation, two mapper lanes, and the mandatory reviewer waves. This is materially smaller than the 102-unit/81-fresh-unit calibration package, but the two wholly uncovered support sources require direct extraction and mapping.
- **Total source units:** 41
- **Fresh-source units:** 17
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-19T04:33:27Z
- **Finished UTC:** 2026-08-19T05:02:09Z
- **Observed elapsed minutes:** 28.7
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Known token cost (USD) | Status |
|---|---:|---:|---:|---:|---|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

Authoritative response-level runtime/API token counts were not exposed for the coordinator or any specialist, so the ledger records one `UNAVAILABLE` row for each of the 11 manifested agents. The known subtotal is therefore zero and the complete count and price remain explicitly incomplete; no text-length estimate was made. See `review_1_5_3/token_usage_summary.md` for per-agent detail. Cached input and cache-write counts are input subsets; reasoning is an output subset and is not added to total tokens. Any available amount uses the bundled pricing snapshot dated 2026-08-18 and is a token-only estimate, not an invoice.
