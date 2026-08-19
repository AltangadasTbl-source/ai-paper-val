# Numeric Consistency Review

## Scope and completion

This review applied arithmetic, total, subgroup-sum, numerator, denominator, percentage, missingness, population, rounding, unit, scale, label, reference-group, rate/risk/proportion/count, repeated-value, and concrete participant-flow checks to the 60 canonical relationships in `relationships/numeric_relationship_inventory.md`. Scope: DOC-001 pp. 1-11, DOC-002 pp. 1-46, DOC-003 pp. 1-9, and DOC-004 pp. 1-48. Direct supplied PDFs were the authority. All 114 mapped source pages were within scope; no web or legacy candidate/reviewer/report conclusion was used.

Rounding tolerance was one half of the last displayed percentage unit: +/-0.05 percentage points for one-decimal percentages and +/-0.5 percentage points for whole percentages. A source-stated available-N, timepoint-specific denominator, non-mutual-exclusivity statement, planned-versus-observed distinction, or component-event definition was applied before considering a mismatch. Exact P-value and interval compatibility is assigned to the independent statistical review; no display-zero P-value issue is raised here.

**Numeric relationship count:** 60.  
**Relationships with an emitted candidate:** 4.  
**Distinct candidate count:** 4.  
**Status of every candidate below:** Pending Human Adjudication.

## Candidate NC-1 — Smoking percentages use group headers rather than the stated smoking totals

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** DOC-001 [PDF p. 5, Table 1, “Smoking status”](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=5>).
- **Printed inputs:** iNPWT column header `n = 411`; smoking `Total No. 405`; never `220 (53.5%)`, current `95 (23.1%)`, previous `90 (21.9%)`. Surgeon’s-preference header `n = 410`; smoking `Total No. 402`; never `223 (54.4%)`, current `70 (17.1%)`, previous `109 (26.6%)`.
- **Direct observation:** The three smoking counts sum exactly to the printed smoking totals: 220 + 95 + 90 = 405 and 223 + 70 + 109 = 402. The percentages are nevertheless those obtained with the column-header populations: 220/411 x 100 = 53.527% -> 53.5%; 95/411 x 100 = 23.114% -> 23.1%; 90/411 x 100 = 21.898% -> 21.9%; 223/410 x 100 = 54.390% -> 54.4%; 70/410 x 100 = 17.073% -> 17.1%; 109/410 x 100 = 26.585% -> 26.6%.
- **Reproducible rule and calculation:** Where a row prints `Total No.` for a categorical variable and its category counts sum to it, category percentages conventionally need an explicit denominator label if they instead use the full randomized group. Under the printed Total-No. denominator, the corresponding values would be 54.3%, 23.5%, 22.2% and 55.5%, 17.4%, 27.1%, respectively. The observed gaps are 0.7-1.1 percentage points, exceeding the +/-0.05-point one-decimal tolerance.
- **Tolerance:** +/-0.05 percentage points for a one-decimal percent; the discrepancy is not ordinary rounding.
- **Inference, not direct observation:** The likely explanation may be that `Total No.` denotes the number with a recorded smoking category while Table 1 deliberately calculates all percentages using the randomized-column header. The table does not say this.
- **Source-grounded alternatives:** (1) percentages intentionally use all 411/410 randomized participants and the unlabelled remainder has missing smoking status; (2) `Total No.` was intended as the percentage denominator, in which case the percentages are inconsistent; (3) a footnote or table convention outside the displayed row defines the denominator. No relevant footnote is printed on the table page.
- **Quality-control relevance:** A data extractor can reasonably use 405/402 as the denominator because the table prints it; differing denominator conventions change baseline prevalence and missingness interpretation.
- **Exact human question:** What denominator convention was intended for the smoking percentages, and should Table 1 explicitly state that 6 iNPWT and 8 control smoking values are missing if percentages are calculated from randomized-group denominators?

## Candidate NC-2 — Operating-surgeon level counts exceed the participant denominators without a multi-operator label

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** DOC-001 [PDF p. 7, Table 2, “Level of operating surgeon”](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>).
- **Printed inputs:** Table 2 headers are iNPWT `n = 411` and surgeon’s preference `n = 410`. Operating-surgeon rows are consultant `319 (77.6%)` and `318 (77.6%)`; registrar `123 (29.9%)` and `110 (26.8%)`; senior house officer `4 (1.0%)` and `1 (0.2%)`.
- **Direct observation:** Within each displayed group, counts sum to 446 and 429: 319 + 123 + 4 = 446; 318 + 110 + 1 = 429. Those exceed the printed participant denominators by 35 and 19. The respective percentages likewise sum to 108.5% and 104.6%.
- **Reproducible rule and calculation:** For an exhaustively labelled single “level of operating surgeon” per participant, category counts should sum to no more than the participant denominator and percentages to approximately 100%, subject only to rounding. The excesses are 35/411 = 8.52 percentage points and 19/410 = 4.63 percentage points, much larger than the three-row rounding bounds (+/-0.15 points).
- **Tolerance:** Count tolerance 0; summed one-decimal percentages tolerance +/-0.15 percentage points. Neither can account for the observed excess.
- **Inference, not direct observation:** Multiple surgeons may have been recorded for a single operation, which would make these a multi-response measure rather than a participant partition. The table label and footnotes define seniority equivalents but do not state that responses may be multiple.
- **Source-grounded alternatives:** (1) multiple operating surgeons were intentionally counted per procedure; (2) the row is a multi-response field whose label/footnote is incomplete; (3) a category count or denominator is inaccurate.
- **Quality-control relevance:** Without a multi-response qualifier, the table presents these as `No. of participants (%)`; a reader may interpret them as an exclusive distribution of participant operations.
- **Exact human question:** Can more than one operating-surgeon level be recorded for one participant, and if yes, should Table 2 label these rows as non-mutually-exclusive operator records rather than participant categories?

## Candidate NC-3 — Fascia-closing surgeon level counts exceed the participant denominators without a multi-operator label

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** DOC-001 [PDF p. 7, Table 2 continuation, “Level of surgeon closing fascia”](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>).
- **Printed inputs:** iNPWT `n = 411`: consultant `201 (48.9%)`, registrar `218 (53.0%)`, senior house officer `26 (6.3%)`. Surgeon’s preference `n = 410`: consultant `193 (47.1%)`, registrar `225 (54.9%)`, senior house officer `15 (3.7%)`.
- **Direct observation:** Counts sum to 445 and 433: 201 + 218 + 26 = 445; 193 + 225 + 15 = 433. The sums exceed 411 and 410 by 34 and 23. Percentages sum to 108.2% and 105.7%.
- **Reproducible rule and calculation:** A single closing-fascia operator category per participant would require sums no greater than n. The count excesses are 34/411 = 8.27 percentage points and 23/410 = 5.61 percentage points, outside the +/-0.15-point three-row percentage-rounding tolerance.
- **Tolerance:** Count tolerance 0; summed one-decimal percentage tolerance +/-0.15 percentage points.
- **Inference, not direct observation:** Co-closure by more than one surgeon could explain an intentionally multi-response field, but Table 2 does not disclose that interpretation.
- **Source-grounded alternatives:** (1) multiple surgeon levels are recorded for a single fascia closure; (2) the field is multi-response but insufficiently labelled; (3) the table contains a count/denominator error.
- **Quality-control relevance:** The printed unit is participants, not procedures or operator records; an unqualified denominator excess prevents reliable extraction of the operator-level distribution.
- **Exact human question:** What is the analysis unit for “Level of surgeon closing fascia,” and were multiple operator levels allowed per participant? If so, where is that non-mutual-exclusivity stated?

## Candidate NC-4 — Skin-closing surgeon level counts exceed the participant denominators without a multi-operator label

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** DOC-001 [PDF p. 7, Table 2 continuation, “Level of surgeon closing skin”](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>).
- **Printed inputs:** iNPWT `n = 411`: consultant `115 (28.0%)`, registrar `214 (52.1%)`, senior house officer `96 (23.4%)`. Surgeon’s preference `n = 410`: consultant `102 (24.9%)`, registrar `241 (58.8%)`, senior house officer `73 (17.8%)`.
- **Direct observation:** Counts sum to 425 and 416: 115 + 214 + 96 = 425; 102 + 241 + 73 = 416. The sums exceed the group denominators by 14 and 6. Percentages sum to 103.5% and 101.5%.
- **Reproducible rule and calculation:** A single skin-closing operator category per participant would require sums no greater than 411/410. The excesses are 14/411 = 3.41 percentage points and 6/410 = 1.46 percentage points, greater than the +/-0.15-point rounding tolerance for the three displayed one-decimal percentages.
- **Tolerance:** Count tolerance 0; summed one-decimal percentage tolerance +/-0.15 percentage points.
- **Inference, not direct observation:** A multi-operator skin closure may be a legitimate explanation, but it is not stated in Table 2 or its footnotes.
- **Source-grounded alternatives:** (1) more than one surgeon-level record can apply to one skin closure; (2) the field is intentionally multi-response but lacks the necessary table qualifier; (3) one or more printed counts/denominators is wrong.
- **Quality-control relevance:** This affects whether the rows represent a patient-level baseline distribution or operator-level records and therefore whether their percentages can be compared or reused as participant proportions.
- **Exact human question:** Were consultant, registrar, and senior-house-officer skin-closure records allowed to co-occur for one participant, and should the table disclose this or revise the denominator/labels?

## Checked relationships not emitted as candidates

All other listed relationships were checked under their applicable printed rule. In particular: Figure 1 flow and ineligibility totals reconcile; percentage discrepancies between Table 3 and narrative are display precision; blood-loss, procedure, approach, ASA, contamination, skin-preparation, adherence, eTable N totals, and wound-complication grids reconcile; the eTable 5 84/83 component-event totals are explicitly not participant totals; and the eTable 6 “only” rows reconcile the 112/108 primary SSI counts. Source-defined multi-response dressing data and component-event data were not incorrectly subjected to participant subgroup-sum tests.

## Limitations

- This lane does not determine whether the four candidates are errors; it documents their observable denominator/label conflicts and the exact missing definition for human review.
- The supplied sources contain no participant-level dataset or data dictionary to decide whether multiple surgeon-level records per operation are permitted.
- SAP and protocol sources primarily contain planned methods and blank templates, so they cannot validate unprinted observed totals.
