# Cross-Source Quantitative Consistency Check

## Scope and method

This checker reviewed the complete canonical inventories: numeric/reporting relationships `N001` through `N071` (71) and inferential-statistical relationships `S001` through `S093` (93). It compared every mapped occurrence for which another supplied location reported the same result or supplied a definition needed to identify the result. Comparisons required agreement of population, analysis set, time point, intervention contrast and reference direction, outcome definition, model where applicable, measure, scale/unit, and printed precision before a difference was called.

Direct source confirmation was performed for the qualifying matched-result discrepancy. Protocol/SAP planning values were not compared as if they were final results; where a planned and an implemented analysis differ, the supplied documents were checked for an allowed revision or an explicit overdispersion/transform contingency.

## Candidate proposals

### XSC-001 — Conflicting reported median adherence with identical IQR

- **Provisional checker finding key:** XSC-001
- **Proposed category:** Cross-document numeric inconsistency
- **Matched result:** Full or partial study-product doses taken among the 302 residents who initiated at least one dose. This is a pooled adherence summary, not an arm-specific or primary-outcome rate.
- **Exact source locations:** [jama_butler_2020_oi_200054.pdf — PDF p. 4](../../../jama_butler_2020_oi_200054.pdf#page=4), intervention-fidelity paragraph; [joi200054supp2_prod.pdf — PDF p. 5](../../../joi200054supp2_prod.pdf#page=5), text immediately above eTable 2. Mapped relationships: `N011`, `N059`, `S080`.
- **Printed values:** The main article states: “a median of **93.3%** (interquartile range [IQR], **93.56% to 99.45%**) full or partial doses were taken.” The results supplement states: “median percentage ... was **97.8%** (IQR **93.56 to 99.45**).”
- **Comparison logic:** Both locations describe full-or-partial-dose adherence and print the identical IQR endpoints. A median of 93.3% lies below the printed lower IQR endpoint of 93.56%, whereas 97.8% lies within the same IQR. The two displayed medians differ by 4.5 percentage points after matching the statistic, definition, and precision; this is not attributable to rounding at the displayed one-decimal precision.
- **Direct observation versus inference:** Direct observation is the two conflicting printed medians and the shared IQR. The inference is limited to the conclusion that at least one displayed adherence summary requires human checking; the supplied sources do not identify which printed value reflects the underlying calculation.
- **Supported alternatives:** The supplement’s 97.8% may be the intended pooled median, because it is inside the identical IQR. Alternatively, the main article and supplement could be using distinct unprinted analysis subsets or adherence derivations despite near-identical wording; neither cited passage identifies such a distinction.
- **Human verification steps:** (1) Check the analysis dataset and program output for the pooled full-or-partial-dose percentage among the stated 302 initiators. (2) Confirm whether the main text and eTable 2 were intended to use the same denominator and treatment of partial doses. (3) Recalculate or obtain the ordered adherence distribution and verify the median and quartiles. (4) Determine which location, if either, needs correction; no correction is assigned here.

## Complete matched-result coverage

`NO_CANDIDATE` means that matched printed values agreed after the stated identity matching, or that a documented precision difference was consistent with rounding. `CONTEXT_MATCHED_NO_CANDIDATE` means that a protocol/SAP definition or planned-analysis record was checked against the reported result and did not create a concrete numeric, measure, scale, rate/count, or reference-group conflict. `XSC-001` indicates the single proposal above.

| Inventory IDs | Matched-result families checked | Outcome |
|---|---|---|
| N001-N004, S001 | Abstract versus main narrative/Table 2: design population, arm sizes, primary CAAD result, adverse-event totals | NO_CANDIDATE |
| N005-N007, N047-N057, S044-S078 | Main methods/results versus protocol, SAP, and results-supplement definitions: CAAD numerator/denominator, ITT/complete-case description, planned/revised sample target, models, time-at-risk, infection, diarrhoea, and scale definitions | CONTEXT_MATCHED_NO_CANDIDATE |
| N008-N010 | Main flow figure versus participant/follow-up narrative: randomized and primary-analysis counts, person-time, truncation, and attrition | NO_CANDIDATE |
| N011, N049, N059, S047, S069-S070, S074, S080 | Main adherence paragraph versus protocol/SAP adherence definitions and results-supplement eTable 2 | XSC-001; all other matched definition/model records NO_CANDIDATE |
| N012-N013, N040-N042, N061-N068, S002-S005, S041-S043, S083-S088 | Main microbiology narrative versus results-supplement eTable 5: organism-positive counts, denominators, ARD direction, adjusted ORs, intervals, P values, and no-analysis cells | NO_CANDIDATE |
| N014-N016, N043-N045 | Repeated main-text results: nonprophylactic antibiotic use, primary CAAD outcome, adverse events, and conclusion/discussion statements | NO_CANDIDATE |
| N017-N029, S006-S018, N051-N052, S050-S051, S061, S077 | Main Table 2 versus its narrative, table footnotes, protocol/SAP, and eFigure definitions: infection-specific antibiotic days, infection incidence, duration, and cumulative infection days | NO_CANDIDATE |
| N030-N039, S019-S040, N053, N056, S052-S053, S062-S065 | Main Table 3 versus narrative and protocol/SAP definitions: EQ-5D, EQ-VAS, ICECAP-O, hospital, death, AAD, and all-cause-diarrhoea results | NO_CANDIDATE |
| N058, N060, S079, S081 | Results-supplement sensitivity eTables versus the main discussion’s description of the sensitivity analyses | NO_CANDIDATE |
| N015, N054, N071, S071 | Baseline Table 1 and figure/derived-measure references versus protocol/SAP definitions | CONTEXT_MATCHED_NO_CANDIDATE |
| N069-N070, S067, S078, S090-S093 | Protocol/SAP subgroup specification versus results-supplement eTable 6: subgroup variables, interaction contrasts, gender adjustment, and printed P values | NO_CANDIDATE |

## Precision and measure safeguards applied

- Table-versus-narrative variants for lower-respiratory antibiotic days (`S008`), infection duration (`S017`), and 3-month self-reported ICECAP-O (`S027`) were retained as precision-compatible representations of the same contrast, not called differences.
- For microbiology absolute risk differences, the printed direction was interpreted using the sources’ comparator/reference convention; a negative/positive ARD was not compared naively against the displayed probiotic-first counts. The corresponding odds ratios and counts agree with the results supplement at displayed precision.
- Protocol Poisson specifications and the reported negative-binomial primary model were not called a model mismatch because the protocol/SAP explicitly permits negative binomial modelling for overdispersion and the results supplement states that implementation.
- No rate was treated as a count: CAAD, infection-day, AAD, and hospital outcomes were checked against their supplied numerator/denominator and exposure-time definitions.
- No `P = 0`, `p = 0.000`, or equivalent display-zero result was present. `P<.001` was treated as an inequality display, not as a display-zero candidate.

## Counts and limitations

- Canonical inventory coverage: 71 numeric/reporting relationships plus 93 inferential-statistical relationships; 164 total.
- Candidate proposals: 1 distinct provisional checker finding (`XSC-001`); no stable candidate ID or adjudication was assigned.
- Limitations: This is a cross-source check using supplied PDFs and the canonical mapping artifacts. The package contains no participant-level adherence dataset or analysis program, so it cannot resolve which of the two printed medians reflects the underlying calculation.
