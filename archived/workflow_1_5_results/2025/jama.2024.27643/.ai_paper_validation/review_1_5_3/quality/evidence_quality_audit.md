# Final Evidence-Quality Audit

## Audit identity and outcome

- **Runtime agent ID:** `/root/quality_auditor`
- **Model and reasoning effort:** `gpt-5.6-sol` / `high`
- **Audit status:** COMPLETE WITH COORDINATOR REPAIRS REQUIRED
- **Stable candidate set audited:** C001, C002, C003, C004, C005, C006, C007, C008.
- **Candidate-set result:** The candidate ledger and mechanical recheck contain the same eight stable IDs. This artifact returns all eight IDs. No ID was deleted, merged, renumbered, ranked, suppressed, or adjudicated.
- **Review boundary:** Every candidate remains `Pending Human Adjudication`. This audit assigns no scientific disposition and does not determine a correction.

## Coverage, routing, and discovery audit

- `routing_preflight.md` reports `PASS`, coordinator `gpt-5.6-sol`/`high`, execution mode `INTERACTIVE_CLI`, `Coordinator inference: PASS`, and all nine named presets at their required model and effort pairs.
- `source_coverage.md` has one row for each of six direct PDFs. Its arithmetic closes in every row: 404 total units equal 38 reusable-backed plus 366 fresh-required units, and 404 mapped units equal 404 total units. The mapping artifacts document DOC-001 12/12, DOC-002 229/229, DOC-003 130/130, DOC-004 26/26, DOC-005 6/6, and DOC-006 1/1 physical PDF pages.
- The coverage manifest partitions every reusable-backed and fresh-required mapping unit and gives exactly one plain relative artifact path per row. Every presently completed artifact path resolves. The evidence-quality path resolves after creation of this audit. The report-generation row remains `ASSIGNED` until the final report is written.
- The quantitative inventories contain 56 stable `N` relationships and 65 stable `S` relationships. Numeric review covers N001 through N056. Both statistical passes cover S001 through S065, with explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records. Cross-source review covers all mapped matched-result groups.
- The execution manifest records distinct fresh runtime IDs for the completed mandatory stages. Statistical pass 1 is `/root/statistics_pass_1` and statistical pass 2 is `/root/statistics_pass_2`; both are distinct `gpt-5.6-terra`/`high` fresh spawns. The report-generator row must be appended after that fresh stage runs.
- Discovery was explicitly restarted without a count limit. The source maps cover the complete source-unit partition, the N and S inventories are uncapped, all raw checker observations were merged only by printed relationship before stable assignment, and eight stable IDs were retained. No top-N boundary, desired candidate count, legacy queue, or old candidate set is evidenced as a discovery control.
- Current SHA-256 checks reproduce all six direct-source hashes and all 65 reused-artifact hashes. Candidate-ledger and recheck PDF links resolve and every cited candidate page was confirmed directly.
- No stable card mentions `P = 0`, `p = 0.000`, or an equivalent display-zero P value. The `0` in an eTable confidence-interval endpoint for C006 is not a P value. No independent-contradiction field is therefore conditionally required for C001 through C008.

## Cross-artifact repairs required from the coordinator

1. Correct false physical-page attribution in `extraction/main_quantitative_evidence.md`: Table 2 and Figure 2 are on DOC-001 PDF p. 7, Figure 3 and the biomarker/safety results are on p. 8, and the Discussion sentence giving 13 events is on p. 9. The current page-applicability table incorrectly calls p. 9 non-applicable. Correct the corresponding main-map locations without changing the mapped relationships.
2. Correct `statistics/relationship_inventory.md` S009 through S014 from DOC-001 p. 6 Table 2 to DOC-001 p. 7 Table 2. Stable candidate locations are already truthful.
3. Repair C007 in `candidate_ledger.md`: simple subtraction of the two rounded percentage changes is not the fitted geometric-mean-ratio rule. The mechanical recheck correctly reproduces the article's `-23.2%` diagnostic as `[(1.004 / 1.308) - 1] x 100 = -23.24%`. Retain the source-supported cross-display differences, but remove the unsupported claim that `0.4 - 30.8` must equal the fitted contrast.
4. For C002, remove the unsupplied `4.345 weeks/month` conversion from the final evidence card or identify it explicitly as an illustrative diagnostic assumption. The candidate basis is the directly printed rate-versus-24-week-change label conflict; the package does not define a month-length conversion for this estimand.
5. For C006, do not claim that the eTable's integer endpoint `0` establishes a different unrounded relation to the null. State only that the printed interval differs and that the unrounded endpoint and table-specific rounding rule are unavailable. The same-page Figure 3/prose endpoint difference remains an independent printed repetition mismatch.
6. Assemble every final evidence card with all exact report-specification labels. Use the exact five human-adjudication subfields, each with the blank value `__`. Keep every downstream statement conditional and bounded to what a data extractor, systematic review, meta-analysis, or guideline could copy if the candidate is confirmed.
7. After the report generator finishes, add its distinct fresh runtime row to `agent_execution_manifest.md`, change the manifest's evidence-quality and report-generation rows to `COMPLETE`, close `run_state.md`, and make the ledger, recheck, quality-audit, and final-report ID sets identical.

## Evidence-card field audit

The current candidate ledger supplies `Category` and `Exact source locations` for every ID, but it is not yet a complete final-report card. For each ID below, the coordinator must add or normalize these exact fields: `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The final human block must be exactly:

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C001 — Shared-placebo race missingness does not reconcile with the printed denominator

- **Evidence support:** Direct DOC-001 PDF p. 6 confirmation reproduces `n=164`, the race numerator sum `2 + 6 + 151 + 1 = 160`, and footnote count 3. The calculation `164 - 160 = 4` and the one-participant difference are reproducible.
- **Missing card fields:** All fields listed in the evidence-card field audit require exact-label assembly; `Category` and `Exact source locations` are already present.
- **Unsupported assumption or missing definition:** The four printed rows are the complete displayed race classification, but the package does not define whether another status was deliberately excluded from the common denominator. Frame the observation as displayed accounting, not as proof of which field is wrong.
- **Pagination and link audit:** DOC-001 PDF p. 6 is truthful and the link resolves.
- **Possible duplicate relationship:** None among stable IDs. Numeric N007 is its checker provenance, not a second stable candidate.
- **Impact wording control:** Do not claim a participant-level data error or paper-level conclusion effect. A bounded statement may say that, if confirmed, a baseline denominator or missingness count could be copied inconsistently by a data extractor.
- **Required coordinator repair:** Add the complete card fields and preserve the exact unresolved question about an additional unclassified status versus a printed denominator, numerator, or footnote issue.

## C002 — SVC values have incompatible monthly-rate and 24-week-change labels

- **Evidence support:** Direct DOC-001 PDF p. 4 and DOC-004 PDF p. 16 confirmation reproduces the same `-9.32`, `-8.53`, and `-0.78` values under different time-scale labels.
- **Missing card fields:** All fields listed in the evidence-card field audit require exact-label assembly; `Category` and `Exact source locations` are already present.
- **Unsupported assumption or missing definition:** The `4.345 weeks/month` convention is not supplied. The fitted estimand, its time unit, and any conversion rule remain missing. Do not use the illustrative conversion as source authority.
- **Pagination and link audit:** DOC-001 p. 4 and DOC-004 p. 16 are truthful and resolve.
- **Possible duplicate relationship:** Numeric N012 and statistical RAW-S-P1-004 are the same printed relationship and were properly merged into one stable ID.
- **Impact wording control:** Do not state that either label is definitively wrong. If confirmed, a rate and cumulative change could be extracted as different effect scales; no paper-level conclusion change is established.
- **Required coordinator repair:** Base the card on the direct label conflict and clearly label or omit any assumed time conversion.

## C003 — Shared-placebo ALSFRS-R credible-interval endpoints differ for the cited primary model

- **Evidence support:** DOC-001 p. 4 prints `-1.176 to -0.892`; DOC-004 p. 15 prints `-1.181 to -0.894`. Endpoint differences of `0.005` and `0.002` reproduce exactly.
- **Missing card fields:** All fields listed in the evidence-card field audit require exact-label assembly; `Category` and `Exact source locations` are already present.
- **Unsupported assumption or missing definition:** The identity match is source-supported, but posterior run, seed, data lock, unrounded quantiles, and production history are absent. Do not infer the cause.
- **Pagination and link audit:** DOC-001 p. 4 and DOC-004 p. 15 are truthful and resolve.
- **Possible duplicate relationship:** C003, C004, and C005 share a model-output block and may share a production cause, but they concern different printed component values. They remain separate stable IDs.
- **Impact wording control:** Limit any impact statement to the alternative interval a downstream extractor could copy if confirmed; do not claim altered inference or conclusion.
- **Required coordinator repair:** Add exact card fields and retain the missing model-run definition as the human question.

## C004 — Pooled-active ALSFRS-R credible-interval endpoints differ for the cited primary model

- **Evidence support:** DOC-001 p. 4 prints `-1.153 to -0.858`; DOC-004 p. 15 prints `-1.143 to -0.847`. Endpoint differences of `0.010` and `0.011` reproduce exactly.
- **Missing card fields:** All fields listed in the evidence-card field audit require exact-label assembly; `Category` and `Exact source locations` are already present.
- **Unsupported assumption or missing definition:** Posterior run, data lock, unrounded quantiles, and production history are absent. The audit cannot select an authoritative interval.
- **Pagination and link audit:** DOC-001 p. 4 and DOC-004 p. 15 are truthful and resolve.
- **Possible duplicate relationship:** It is related to C003 and C005 but uses a distinct pooled-active component and printed comparator. Preserve it separately.
- **Impact wording control:** State only that an extractor could copy different uncertainty endpoints if confirmed. Do not assert a changed inferential conclusion.
- **Required coordinator repair:** Add exact card fields and keep the conclusion limited to a repeated-value mismatch.

## C005 — Bayesian mortality event rates differ between article text and cited eTable 2

- **Evidence support:** DOC-001 p. 4 prints `0.007` and `0.006`; DOC-004 p. 15 prints `0.010` and `0.009` events/month. Both group differences are `0.003 events/month`, beyond common three-decimal identity.
- **Missing card fields:** All fields listed in the evidence-card field audit require exact-label assembly; `Category` and `Exact source locations` are already present.
- **Unsupported assumption or missing definition:** The exact event variable, posterior summary, run identifier, and whether any death-only versus death/PAV distinction applies are absent. Do not infer one.
- **Pagination and link audit:** DOC-001 p. 4 and DOC-004 p. 15 are truthful and resolve.
- **Possible duplicate relationship:** It shares the primary-model block with C003 and C004 but is a distinct rate relationship. Preserve it separately.
- **Impact wording control:** Replace qualitative amplification such as `materially different` with the exact numerical difference. No conclusion impact is established.
- **Required coordinator repair:** Add exact card fields and identify only the model-rate values a downstream extractor could copy differently if confirmed.

## C006 — Plasma NfL confidence intervals differ across Figure 3, narrative, and eTable 3B

- **Evidence support:** DOC-001 p. 8 prints Figure upper endpoint `-0.5%` and prose endpoint `-0.4%`; DOC-004 p. 17 prints `-18.0, 0`. The same point estimate and P value are repeated.
- **Missing card fields:** All fields listed in the evidence-card field audit require exact-label assembly; `Category` and `Exact source locations` are already present.
- **Unsupported assumption or missing definition:** The unrounded interval, interval method, output version, and table-specific rounding convention are absent. The integer `0` does not establish that the unrounded eTable interval reaches or crosses the null.
- **Pagination and link audit:** DOC-001 p. 8 and DOC-004 p. 17 are truthful and resolve.
- **Possible duplicate relationship:** Numeric N018, cross-source candidate 5, and RAW-S-P1-003 were properly merged because they concern the same repeated interval. No other stable ID duplicates it.
- **Impact wording control:** State that printed uncertainty bounds could be extracted differently if confirmed. Do not claim a changed significance determination or conclusion.
- **Required coordinator repair:** Remove the overstatement about the eTable endpoint's unrounded relation to the null and add all exact card fields.

## C007 — Serum NfL regimen-only values and contrast differ across displays

- **Evidence support:** DOC-001 p. 8 and DOC-004 p. 17 directly reproduce placebo changes `30.8%` versus `26.8%`, contrasts `-23.2%` versus `-26.4%`, and different interval endpoints, while active change and P value agree.
- **Missing card fields:** All fields listed in the evidence-card field audit require exact-label assembly; `Category` and `Exact source locations` are already present.
- **Unsupported assumption or incorrect arithmetic:** The ledger's crude `0.4 - 30.8 = -30.4%` rule is not valid for a fitted back-transformed geometric-mean ratio. The recheck correctly shows that the article's printed contrast is compatible with `[(1.004 / 1.308) - 1] x 100 = -23.24%`. That diagnostic uses rounded displayed arm changes and must not replace the fitted model.
- **Pagination and link audit:** DOC-001 p. 8 and DOC-004 p. 17 are truthful and resolve.
- **Possible duplicate relationship:** Numeric N019, cross-source candidate 4, and RAW-S-P1-002 were properly merged as one matched relationship.
- **Impact wording control:** Do not claim an internal arithmetic error in the article or a changed paper conclusion. If confirmed, the alternative printed biomarker effect and interval could be copied differently.
- **Required coordinator repair:** Remove the crude-subtraction claim, use the direct cross-display values as the candidate basis, and state the missing fitted-contrast definition.

## C008 — Discussion total of 13 events differs from the 14 events displayed in Table 2

- **Evidence support:** DOC-001 p. 7 prints `5/120` and `9/162`, whose numerators sum to 14; DOC-001 p. 9 prints 13 events for the named groups.
- **Missing card fields:** All fields listed in the evidence-card field audit require exact-label assembly; `Category` and `Exact source locations` are already present.
- **Unsupported assumption or missing definition:** The Discussion does not define `events`, its cutoff, or whether it uses Table 2's death/PAV composite. The calculation is applicable conditionally when those definitions match.
- **Pagination and link audit:** DOC-001 Table 2 is truthfully on p. 7 and the Discussion statement on p. 9; both links resolve. Upstream main-map locations require the global pagination repair above.
- **Possible duplicate relationship:** None among stable IDs. It is a separate event-total relationship from the Bayesian model rates in C005.
- **Impact wording control:** Do not claim Table 2 or the Discussion is wrong. If confirmed as the same event definition and cutoff, an extractor could copy a total differing by one event; no conclusion impact is established.
- **Required coordinator repair:** Make the conditional matching rule prominent and retain the exact unresolved event-definition/cutoff question.

## Limitations and completion conditions

- The package does not supply participant-level data, analysis code, model outputs, posterior draws, unrounded confidence limits, run identifiers, or production history needed to resolve the remaining human questions.
- The canonical final report and report-generator execution do not yet exist at the time of this audit. Consequently, final ledger/recheck/quality/report ID-set identity, final-card field completeness, closed timing/token metadata, and rendered-report validation cannot yet be confirmed.
- The direct sources and reused assets are unchanged at this audit point. Fresh preprocessing artifacts are review outputs, not reused-input mutations.
- Subject to the enumerated coordinator repairs and final report-stage completion, the scientific source-unit coverage, stable-ID recheck coverage, two-pass statistical coverage, source integrity, category choices, and neutral pending-adjudication framing are complete.
