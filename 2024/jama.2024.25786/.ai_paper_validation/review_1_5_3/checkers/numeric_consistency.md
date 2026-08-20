# Numeric Consistency Review

## Complete assigned scope

This review applied numeric, arithmetic, total, subgroup-sum, numerator, denominator, percentage, missingness, population, rounding, measure/label/scale, unit, reference-group, rate/risk/proportion/person-time/count, and repeated-value checks to all 69 stable `N` relationships in `relationships/numeric_relationship_inventory.md`. The direct PDFs were checked at the cited pages for every candidate below. This checker registers observations for later human adjudication only; it assigns neither stable `C` IDs nor severity, validity, or disposition.

### Check rules and tolerances

- A displayed one-decimal percentage must equal `100 x numerator / denominator` rounded to one decimal; tolerance is plus or minus 0.05 percentage point, subject to the ordinary half-up/banker's-boundary ambiguity only at an exact half.
- A stated total must equal the sum of its explicitly presented mutually exclusive component counts, unless a source footnote or label identifies an omitted/missing subgroup.
- Counts, proportions, risks, cumulative incidences, odds ratios, and planned quantities are not substituted for one another. Population, time window, and model labels must match before a comparison.
- Different denominators in primary, per-protocol, AE, and missing-data sensitivity analyses were retained when the source supplied a population definition; they are not treated as conflicts merely because their values differ.

## Candidate observations requiring human adjudication

### Supplement 2 eTable 2: liberal walk-in transport percentage does not reconcile with its printed count and denominator

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** `joi240147supp2_prod_1738701765.29201.pdf#page=15`, eTable 2, “Type of transport to the trauma center,” liberal oxygen group, “Walk-in.”
- **Printed inputs:** `4/743 (5.3)`.
- **Direct observation:** The direct PDF prints numerator 4, denominator 743, and percentage 5.3 in the same liberal-group cell.
- **Reproducible rule and calculation:** `100 x 4 / 743 = 0.538...%`, which rounds to `0.5%` at one decimal place, not `5.3%`.
- **Tolerance:** One-decimal percentage tolerance is plus or minus 0.05 percentage point. The absolute difference from the printed percentage is `|5.3 - 0.538...| = 4.762...` percentage points, outside tolerance.
- **Inference versus observation:** The three printed inputs and their nonreconciliation are direct observations. An assertion that either the count, denominator, or percentage should change is an inference and is not made here.
- **Alternative source-grounded interpretations:** The denominator may be mistranscribed in the table, the numerator may be a typesetting error, or the percentage may contain a misplaced decimal. The adjacent transport rows use denominator 743 for the liberal group, so they do not supply a different printed denominator for this cell.
- **Quality-control relevance:** A transport-category percentage could be copied into a baseline-characteristics extraction or used in a subgroup description; the printed values do not permit a reproducible extraction without clarification.
- **Exact human question:** Which value is authoritative for liberal-group walk-in transport in eTable 2: the count 4, the denominator 743, or the printed percentage 5.3%?

### Supplement 2 eTable 2: liberal vascular-surgery percentage does not reconcile with its printed zero numerator

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** `joi240147supp2_prod_1738701765.29201.pdf#page=15`, eTable 2, “Surgery performed in the trauma resuscitation room,” liberal oxygen group, “Vascular surgery.”
- **Printed inputs:** `0/747 (1.1)`.
- **Direct observation:** The direct PDF prints numerator 0, denominator 747, and percentage 1.1 in the same liberal-group cell.
- **Reproducible rule and calculation:** `100 x 0 / 747 = 0.0%`; a zero numerator remains zero under any rounding precision.
- **Tolerance:** One-decimal percentage tolerance is plus or minus 0.05 percentage point. The absolute difference from the printed percentage is `1.1` percentage points, outside tolerance.
- **Inference versus observation:** The printed cell and nonreconciliation are direct observations. It is an inference, not a finding here, that either 0 or 1.1 was intended to be replaced.
- **Alternative source-grounded interpretations:** The count may be a typographic zero, the percentage may have been carried from another cell, or an unprinted denominator/population qualifier may have been intended. No eTable 2 footnote supplies such a qualifier for this row.
- **Quality-control relevance:** The table presents a count, denominator, and percentage as one baseline relationship. Its mismatch can propagate an incorrect rare-event frequency into data extraction.
- **Exact human question:** What numerator and percentage should be reported for liberal-group vascular surgery, given the printed `0/747 (1.1)`?

### Supplement 2 eTable 10: stated postrandomization-exclusion total does not equal the two displayed group counts, without a corresponding explanatory footnote

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** `joi240147supp2_prod_1738701765.29201.pdf#page=24`, eTable 10, first row and its footnote; comparator `jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3`, Figure 1, postrandomization exclusion branches.
- **Printed inputs:** eTable 10 labels the first row `Exclusion after randomization – no./total no. (%) (N=130)` and prints `55/750 (45)` restrictive and `67/758 (55)` liberal. Figure 1 prints 59 restrictive and 71 liberal excluded after randomization, totaling 130. eTable 10's footnote states that **two** patients with missing randomized-oxygen data explain the *secondary-exclusion* `N=341` discrepancy, not the first-row `N=130` relationship.
- **Direct observation:** The eTable's displayed first-row group counts sum to `55 + 67 = 122`, whereas its parenthetical total is `N=130`. The matched Figure 1 supplies a 59-plus-71 equals 130 postrandomization-exclusion total.
- **Reproducible rule and calculation:** Under the first-row label, `55 + 67 = 122`; `130 - 122 = 8`. The eTable's displayed first-row percentages are 45 and 55, which sum to 100, but their displayed group counts do not reach the stated total.
- **Tolerance:** Counts and stated totals are exact integers; tolerance is 0 participants. The mismatch is 8 participants.
- **Inference versus observation:** The eTable total, group counts, footnote scope, Figure 1 counts, and arithmetic gap are direct observations. It is not known from the printed material whether eight patients had unavailable randomized-oxygen intervention data, whether eTable 10's group counts describe a narrower population, or whether a label/count is erroneous.
- **Alternative source-grounded interpretations:** Figure 1's 59/71 values may represent all exclusions whereas eTable 10's 55/67 may intentionally represent only exclusions with recorded intervention distribution. If so, the first row needs a label or footnote parallel to the secondary-exclusion explanation; the currently printed footnote identifies only two patients and only the `N=341` secondary-exclusion row.
- **Quality-control relevance:** The table is explicitly presented as the distribution among postrandomization-excluded patients. An unexplained population gap can lead a reader to use inconsistent exclusion denominators or incorrectly reconcile the participant flow.
- **Exact human question:** Does eTable 10's first row intentionally restrict the 130 postrandomization exclusions to 122 patients with known randomized-oxygen intervention data; if yes, what accounts for the remaining eight and where is that restriction stated?

## Checked relationships without a registered candidate

- Participant flow reconciles when its stated subgroups and the two missing randomized-oxygen data records for secondary exclusions are applied: 130 plus 341 equals the main-paper 471 postrandomization exclusions.
- Main-paper and results-supplement primary, key-secondary, exploratory, AE, subgroup, and protocol-violation count/percentage pairs were checked against their stated denominators. Explicitly distinct populations (mITT, per-protocol, AE observation, and missing-data scenarios) were not conflated.
- eTable 1 site totals reconcile to 750 restrictive and 758 liberal participants. eTable 3 oxygen-category percentages are footnoted to sum to 100%, and the printed category counts do so within their stated denominators.
- Figure 2 risk differences are percentage-point differences, not odds ratios; Figure 3 displays cumulative incidence with at-risk and event rows, not person-time rates. No person-time rate/count conversion was applicable.
- The eTable 11 `135//750` presentation is a directly observed double slash, but `135/750 = 18.0%` reconciles. It is retained as a presentation note in N064 rather than emitted as a numeric inconsistency candidate.
- No coherent display-zero P value was found; no candidate was registered on that basis.

## Counts and limitations

- **Stable numeric relationships checked:** 69.
- **Distinct candidate observations emitted:** 3.
- **Limitations:** The review can establish printed arithmetic and cross-location reconciliation, but cannot determine the intended corrected values or recover unprinted population definitions. It does not replace the required inferential-statistical or cross-source reviewer passes. No workbook, CSV, DOC/DOCX, raw data, person-time dataset, or formula cells were supplied.

