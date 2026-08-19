# Numeric consistency checks

## Scope, evidence, and rules

This independent numeric-consistency pass covers every relationship `N001`-`N028` in `relationships/numeric_relationship_inventory.md`, corresponding to the complete canonical main/support quantitative evidence maps and all four direct supplied PDFs (41 PDF pages). It applies arithmetic, totals, subgroup sums, numerator/denominator/percentage, missingness/population, rounding, scale/unit/reference labels, rate/risk/proportion/count distinctions, and repeated-value checks where the source supplies the required inputs.

Candidate proposals below are source-grounded quality-control observations for **Pending Human Adjudication**. They do not have `C` IDs and this checker assigns no severity, validity, correction, disposition, or conclusion impact. Calculations use only printed source inputs. Rounded percentages use the tolerance stated in the inventory: 0.5 percentage point for a whole percent and 0.05 percentage point for one decimal place.

## Completed non-candidate checks

- **N001-N003:** Allocation, abstract completion and adverse-event numerator/denominator displays reconcile within printed precision.
- **N004:** Figure 1 exclusion reasons sum to 214 and allocation sums to 262. Its later completion/discontinuation identity is a proposal below.
- **N005-N006:** All supplied threshold, scale, time, unit, power, reliability, and population labels were checked. No concrete numeric contradiction was found.
- **N007:** Table 1 sex and site totals reconcile to arm totals; printed count/percentage pairs reconcile at their shown precision. Baseline WORMS categories lack an explicit denominator/missingness statement, so their non-total is not treated as a candidate.
- **N008-N011:** Follow-up, adverse-event, and exposure values reconcile at the stated precision except the Figure 1/results conflict listed below.
- **N012:** Main PDF p. 10 has no applicable relationship.
- **N013-N021:** Protocol/SAP values are planned definitions or methods. No concrete reported numeric contradiction was found; planned N=260 is not required to equal actual N=262.
- **N023:** eTable 3 has explicitly varying biomarker sample sizes; no unsupported total identity was imposed.
- **N026:** eTable 6 does not define blank cells versus `--`, so no numerical value is inferred.
- **N027-N028:** Supplementary adverse-event tables label event classifications/counts rather than participant risks. No rate-versus-count mismatch was identified.

## Candidate proposals

### NP-001 — Figure 1 placebo discontinuations do not reconcile with the results-text placebo withdrawal/loss count

- **Category:** Denominator, proportion, or total inconsistency; analysis-unit or population inconsistency only insofar as it creates this reported count conflict.
- **Exact source locations:** [Main PDF p. 3, Figure 1](<../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3>); [Main PDF p. 7, Results](<../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7>).
- **Printed inputs:** Figure 1 prints placebo `132 Randomized`, `111 Completed 24 wk of placebo treatment`, and `21 Discontinued` (8 adverse event + 6 lack of efficacy + 6 could not be contacted + 1 withdrew consent). Results text prints `Forty participants withdrew or were lost to follow-up (15%), including 17 (13.1%) in the krill oil group and 23 (17.4%) in the placebo group; 222 (84.7%) completed the trial.`
- **Rule and calculation:** For the same randomised placebo arm, completed plus discontinued/withdrawn-or-lost should equal randomised when both statements describe trial completion. Figure: `111 + 21 = 132`. Results text: `132 - 23 = 109`, not 111. Across arms, Figure discontinuations are `17 + 21 = 38`, while results text reports `17 + 23 = 40`; Figure completions `113 + 111 = 224`, while results text reports 222.
- **Tolerance:** Exact integer identity; tolerance 0.
- **Direct observation versus inference:** Directly observed are the conflicting printed counts. The inference is only that the labels appear to describe the same arm-level trial completion disposition; the sources do not state a separate definition that explains two additional placebo withdrawals/losses.
- **Source-grounded alternatives:** The Figure may omit two placebo participants who were withdrawn/lost but not classified as discontinued, or the results-text placebo count may be a transcription error. The supplied pages do not define such a distinction.
- **Quality-control relevance:** Flow denominators and completion populations can be copied into evidence extraction and affect interpretation of follow-up/missingness counts.
- **Exact human question:** Does the 23-person placebo withdrawal/loss count include two participants excluded from Figure 1's `21 Discontinued` category, and if so, what is their Figure 1 disposition and why does the Figure still print 111 completers?

### NP-002 — eTable 2 overall-adherence denominator statement conflicts with the footnote population count

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [Supplement 3 PDF p. 3, eTable 2](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=3>).
- **Printed inputs:** The overall row is headed `Overall, 0-24 weeks follow-up (n = 167), n (%)` and prints krill oil `82 (98.8)` and placebo `81 (96.4)`. The footnote says: `Adherence only calculated for those with available pill count data and who completed the trial (n = 165 [75%]).`
- **Rule and calculation:** The printed percentages imply integer arm denominators `82 / 83 = 98.795%`, rounded to 98.8%, and `81 / 84 = 96.429%`, rounded to 96.4%; `83 + 84 = 167`, agreeing with the row heading. If the footnote describes the same overall eligible analysis population, it names 165 instead, a difference of 2.
- **Tolerance:** One-decimal percentage tolerance ±0.05 percentage point. The count identity has tolerance 0.
- **Direct observation versus inference:** Directly observed are row `n = 167`, its two count/percentage cells, and footnote `n = 165`. The inference is that the footnote is intended to define the same overall adherence population; the table does not name distinct numerator/denominator sets that reconcile 167 and 165.
- **Source-grounded alternatives:** The footnote may be a stale/incorrect total, or `n = 165` may refer to a narrower unlabelled subset while the row uses 167 participants with arm-specific pill-count denominators. No supplied definition specifies that distinction.
- **Quality-control relevance:** The denominator determines the reported adherence percentage and any per-protocol population derived from it.
- **Exact human question:** What precise participant set does footnote `n = 165` denote, and why does it differ from the explicitly stated overall adherence denominator `n = 167` implied by the printed arm percentages?

### NP-003 — eTable 5 krill-oil “Smaller - 1 unit” percentage does not reconcile to its printed count and total

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Printed inputs:** Krill oil `Smaller - 1 unit: 10 (12%)`; krill total `107 (100%)`.
- **Rule and calculation:** `100 × 10 / 107 = 9.3458%`, which rounds to `9%` at whole-percent precision, not `12%`.
- **Tolerance:** ±0.5 percentage point; printed 12% differs by 2.6542 percentage points.
- **Direct observation versus inference:** Both count/total and percentage are direct observations; the calculation is direct arithmetic.
- **Source-grounded alternatives:** A different unprinted denominator could produce approximately 12%, but eTable 5 prints total 107 for this arm and does not identify another denominator for the category.
- **Quality-control relevance:** The category proportion describes the distribution of ordinal imaging-score change.
- **Exact human question:** Is the printed `12%` for 10 krill-oil participants a percentage transcription error, or was a denominator other than the displayed 107 intended?

### NP-004 — eTable 5 krill-oil “No change” percentage does not reconcile to its printed count and total

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Printed inputs:** Krill oil `No change: 80 (72%)`; total `107 (100%)`.
- **Rule and calculation:** `100 × 80 / 107 = 74.7664%`, which rounds to `75%`, not `72%`.
- **Tolerance:** ±0.5 percentage point; difference 2.7664 percentage points.
- **Direct observation versus inference:** Direct printed cells plus arithmetic calculation.
- **Source-grounded alternatives:** An unprinted denominator could yield 72%, but none is supplied and the table prints 107 as the arm total.
- **Quality-control relevance:** The no-change category is the largest category and can be extracted as an ordinal-outcome proportion.
- **Exact human question:** Which of the printed krill-oil values—80, 72%, or total 107—was intended for this category?

### NP-005 — eTable 5 krill-oil “Larger - 1 unit” percentage does not reconcile to its printed count and total

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Printed inputs:** Krill oil `Larger - 1 unit: 12 (12%)`; total `107 (100%)`.
- **Rule and calculation:** `100 × 12 / 107 = 11.2150%`, which rounds to `11%`, not `12%`.
- **Tolerance:** ±0.5 percentage point; difference 0.7850 percentage point.
- **Direct observation versus inference:** Direct printed cells plus arithmetic calculation.
- **Source-grounded alternatives:** A different unprinted denominator could yield 12%, but eTable 5 supplies only 107 for the arm total.
- **Quality-control relevance:** The percentage is a reported category proportion used to describe worsening.
- **Exact human question:** Was 12% calculated with an unreported denominator, or should the displayed whole-percent value be 11%?

### NP-006 — eTable 5 placebo “Smaller - 2 units” percentage does not reconcile to its printed count and total

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Printed inputs:** Placebo `Smaller - 2 units: 2 (1.9%)`; total `109 (100%)`.
- **Rule and calculation:** `100 × 2 / 109 = 1.8349%`, which rounds to `1.8%` at one decimal place, not `1.9%`.
- **Tolerance:** ±0.05 percentage point; difference 0.0651 percentage point.
- **Direct observation versus inference:** Direct printed cells plus arithmetic calculation.
- **Source-grounded alternatives:** The displayed 1.9% would be compatible with a denominator near 105, but eTable 5 prints 109 and supplies no alternative denominator.
- **Quality-control relevance:** Exact decimal proportions can be copied into outcome summaries.
- **Exact human question:** Was a denominator other than the displayed placebo total 109 used for the `1.9%`, or is the percentage rounded/transcribed incorrectly?

### NP-007 — eTable 5 placebo “Smaller - 1 unit” percentage does not reconcile to its printed count and total

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Printed inputs:** Placebo `Smaller - 1 unit: 16 (12%)`; total `109 (100%)`.
- **Rule and calculation:** `100 × 16 / 109 = 14.6789%`, which rounds to `15%`, not `12%`.
- **Tolerance:** ±0.5 percentage point; difference 2.6789 percentage points.
- **Direct observation versus inference:** Direct printed cells plus arithmetic calculation.
- **Source-grounded alternatives:** A denominator near 133 would yield 12%, but that conflicts with the displayed eTable 5 placebo total 109; no separate denominator is supplied.
- **Quality-control relevance:** This is an ordinal imaging-score improvement category.
- **Exact human question:** Which placebo value in this row is intended: the count 16, percentage 12%, or the displayed total 109?

### NP-008 — eTable 5 placebo “No change” percentage does not reconcile to its printed count and total

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [Supplement 3 PDF p. 8, eTable 5](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=8>).
- **Printed inputs:** Placebo `No change: 75 (72%)`; total `109 (100%)`.
- **Rule and calculation:** `100 × 75 / 109 = 68.8073%`, which rounds to `69%`, not `72%`.
- **Tolerance:** ±0.5 percentage point; difference 3.1927 percentage points.
- **Direct observation versus inference:** Direct printed cells plus arithmetic calculation.
- **Source-grounded alternatives:** A denominator near 104 would yield 72%, but eTable 5 prints 109 and gives no alternate category denominator.
- **Quality-control relevance:** The no-change percentage is a core descriptive result.
- **Exact human question:** Is the placebo no-change percentage 72% based on an unreported denominator, or should it reconcile to 75 of 109?

### NP-009 — eTable 4 week-4 weight-bearing-pain change cells duplicate the week-4 function change cells and do not reconcile to their displayed means

- **Category:** Numeric or arithmetic inconsistency; repeated-value check.
- **Exact source location:** [Supplement 3 PDF p. 5, eTable 4](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=5>).
- **Printed inputs:** Week-4 weight-bearing pain prints krill final `100 (88 to 112)`, baseline `127 (116 to 138)`, change `-84 (-122 to -46)`; placebo final `108 (97 to 119)`, baseline `141 (130 to 151)`, change `-103 (-141 to -65)`. The next week-4 WOMAC function row prints the same change cells: krill `-84 (-122 to -46)` and placebo `-103 (-141 to -65)`.
- **Rule and calculation:** Direct descriptive subtraction gives krill `100 - 127 = -27` and placebo `108 - 141 = -33`, not the displayed `-84` and `-103`. The same two change values and intervals recur immediately in the distinct function row, whose final-minus-baseline values are approximately `493 - 578 = -85` and `503 - 618 = -115`.
- **Tolerance:** Values are printed as whole numbers; descriptive reconciliation tolerance ±0.5 unit. Differences are 57 and 70 units. Exact repeated-value comparison has tolerance 0.
- **Direct observation versus inference:** The duplicated change cells and printed means are direct observations. The inference is that a copy/paste or row-placement error may have occurred. eTable 4 states analyses are baseline-adjusted for some endpoints, so simple subtraction is diagnostic rather than a replacement for any modelled estimate; however, no stated adjustment explains exact duplication of the two adjacent function cells in the weight-bearing-pain row.
- **Source-grounded alternatives:** The eTable layout might intentionally display a different, unlabelled estimand for change, but that would still leave the exact duplication with the function row unexplained. The supplied footnote identifies baseline adjustment for weight-bearing pain but does not define it as a reason to repeat function values.
- **Quality-control relevance:** These cells can be extracted as within-arm changes and affect any check of the reported between-group result.
- **Exact human question:** Were the week-4 weight-bearing-pain change values/intervals inadvertently copied from the WOMAC-function row, and what are the intended labelled change values for each arm?

### NP-010 — eTable 4 week-12 lower-leg-strength change cells duplicate the week-4 back-pain change cells and conflict with their displayed means

- **Category:** Numeric or arithmetic inconsistency; repeated-value check.
- **Exact source location:** [Supplement 3 PDF p. 6, eTable 4](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=6>).
- **Printed inputs:** Week-12 lower-leg strength prints krill final `72.6 (65.1 to 80.1)`, baseline `66.5 (59.8 to 73.2)`, change `-2.8 (-6.0 to 0.4)`; placebo final `70.2 (62.3 to 78.1)`, baseline `65.9 (59.4 to 72.3)`, change `-4.2 (-7.4 to -1.1)`. Earlier on the same page, week-4 back-pain VAS prints the identical krill and placebo change cells `-2.8 (-6.0 to 0.4)` and `-4.2 (-7.4 to -1.1)`.
- **Rule and calculation:** Direct descriptive subtraction gives strength changes `72.6 - 66.5 = +6.1` and `70.2 - 65.9 = +4.3`, not the displayed negative values. The repeated cells match a different outcome/time point exactly.
- **Tolerance:** One-decimal values; descriptive reconciliation tolerance ±0.05 unit. Differences are 8.9 and 8.5 units. Exact repeated-value comparison has tolerance 0.
- **Direct observation versus inference:** The source cells and their exact repetition are direct observations. The inference is a possible copied-cell or row-placement error. As with NP-009, simple subtraction is diagnostic because eTable 4 may use modelled changes, but the table supplies no rule explaining the exact back-pain values in a strength row.
- **Source-grounded alternatives:** An unlabelled modelling convention could make a modelled strength change differ from raw mean subtraction; it does not by itself explain exact duplication of both back-pain change cells and intervals.
- **Quality-control relevance:** The sign and magnitude of a strength change are outcome-defining numerical data.
- **Exact human question:** Are the printed week-12 lower-leg-strength change cells copied from week-4 back-pain VAS, and what are the intended strength change estimates and intervals?

### NP-011 — eTable 4 week-12 fasting-glucose between-group result duplicates the week-12 hsCRP result and conflicts with the displayed glucose changes

- **Category:** Numeric or arithmetic inconsistency; repeated-value check; measure/label inconsistency.
- **Exact source location:** [Supplement 3 PDF p. 6, eTable 4](<../../../joi240048supp3_prod_1727199125.83025.pdf#page=6>).
- **Printed inputs:** Week-12 hsCRP prints between-group difference `0.07 (-1.19 to 1.33)`, `P = .92`. Week-12 fasting glucose prints the identical between-group difference `0.07 (-1.19 to 1.33)`, `P = .92`, while its arm-specific changes are krill `0.09 (-0.07 to 0.24)` and placebo `0.15 (-0.01 to 0.31)`.
- **Rule and calculation:** Exact duplication across distinct measures is checked with tolerance 0. The displayed glucose changes differ by `0.09 - 0.15 = -0.06` before any model adjustment, whereas the reported glucose contrast is `+0.07` with the same wide interval/P value as hsCRP. The latter direct subtraction is a diagnostic only; the exact copied result is the primary observation.
- **Tolerance:** Exact repeated-value comparison tolerance 0. The diagnostic contrast uses one- or two-decimal display precision and is not used to prescribe a corrected estimate.
- **Direct observation versus inference:** Identical contrast/interval/P cells are directly observed. The inference is possible row/cell copying. The source does not state that hsCRP and fasting glucose share a common outcome scale, model result, or rescaled estimand that would explain identical values.
- **Source-grounded alternatives:** A table-generation or layout error could have repeated the hsCRP cell; an unreported separate glucose model could in principle yield the displayed contrast, but cannot explain why all three result fields match hsCRP exactly without further source information.
- **Quality-control relevance:** The measure label, effect estimate, interval, and P value are routinely copied into structured evidence tables.
- **Exact human question:** Does the week-12 fasting-glucose between-group cell belong to glucose, or was the week-12 hsCRP contrast/interval/P value duplicated into that row; what are the intended glucose result fields?

## Summary and remaining limitations

- **Relationships checked:** 28 stable `N` relationships, covering all main-paper and support numeric/reporting map entries.
- **Candidate proposals:** 11 (`NP-001`-`NP-011`); none has a stable candidate ID or an AI adjudication.
- **No-candidate display-zero rule:** No candidate was proposed solely from a display-zero P value; no such numeric-only issue was encountered in this pass.
- **Limitations:** No source definition resolves eTable 6 blanks/dashes. Baseline WORMS category missingness in Table 1 is not specified. Statistical model compatibility, confidence intervals, and P values other than the direct copied-field pattern in NP-011 are assigned to the independent statistical passes.
