# Final Evidence-Quality Audit

## Audit status and scope

- **Audit status:** COMPLETE for the assigned pre-report evidence-quality stage.
- **Stable candidate set covered:** C001, C002, C003, C004, C005, C006, and C007.
- **Candidate-set result:** The candidate ledger and mechanical recheck contain the same seven stable IDs. This audit returns all seven. No stable ID was deleted, merged, renumbered, ranked, suppressed, adjudicated, or assigned severity.
- **Human status:** Every candidate remains **Pending Human Adjudication**.
- **Evidence boundary:** Only supplied package sources and current Workflow 1.5.3 artifacts were used. No web source or legacy candidate conclusion was used.

## Complete coverage and execution audit

The five direct-source rows close correctly: DOC-001 is 10 total = 10 reusable + 0 fresh-required = 10 mapped; DOC-002 is 66 = 0 + 66 = 66; DOC-003 is 40 = 0 + 40 = 40; DOC-004 is 2 = 2 + 0 = 2; and DOC-005 is 1 = 0 + 1 = 1. Package totals are 119 total = 12 reusable + 107 fresh-required = 119 mapped, with every row marked `COMPLETE`. The main map accounts for all 12 reusable-backed units, and the support map accounts for all 107 fresh-required units. No scientific-coverage gap remains.

The numeric inventory is continuous and complete from N001 through N065. The numeric checker explicitly covers all 65 records. The statistical inventory is continuous and complete from S001 through S033. Both statistical checker artifacts explicitly revisit all 33 records, and every record has both `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. The cross-source checker covers all five supplied documents and all mapped matched-result groups. The candidate ledger merged only two genuine pre-ID duplicate pairs: the readmission-window observation from numeric and cross-source review into C003, and the confidence-level observation from numeric and statistical review into C005. Similar ERAS observations C004 and C007 use different comparators and rules and are not duplicates.

Discovery was not controlled by a top-N boundary, a desired count, or an old candidate list. The reusable-asset inventory was source-linked and used old document records only for identity or preprocessing provenance. The main and support maps rebuilt source-unit coverage, all four checkers state complete assigned scope, and stable IDs were assigned only after cross-lane merging. Seven is the resulting complete stable set, not a cap.

`routing_preflight.md` reports `PASS`, the coordinator route is `gpt-5.6-sol`/`high`, all nine presets are verified, and execution mode is `INTERACTIVE_CLI`. Statistical pass 1 and pass 2 have distinct fresh runtime IDs, `/root/statistical_pass_1` and `/root/statistical_pass_2`, both recorded as `gpt-5.6-terra`/`high` with `FRESH_SPAWN`. Their artifacts document complete S001-S033 coverage.

Every existing coverage-manifest data row contains one plain relative artifact path. At audit intake, the `evidence_quality` and `report_generation` rows were still pending and used placeholder scope text. After this artifact is returned, the coordinator must replace the `evidence_quality` scope with `C001, C002, C003, C004, C005, C006, C007` and mark it `COMPLETE`. The later report-generation row must enumerate the same seven IDs and be marked `COMPLETE`. The current execution manifest stops at statistical pass 2; the coordinator must add this fresh auditor exactly once and later add the fresh report generator. These are manifest-finalization repairs, not evidence gaps.

The current SHA-256 baselines were mechanically checked: all five direct sources and all 38 inventoried reusable artifacts return `OK`. The five supplied PDFs exist with the inventoried page counts of 10, 66, 40, 2, and 1. Candidate-ledger and recheck links resolve locally and use real PDF page fragments. Some relationship-map rows use plural page labels with a link that opens only the first named page; those compressed inventory locators must not be copied as if one link opened every listed page. Each final evidence card must instead use one truthful link per cited page, from the final report location, ending in `#page=N`.

No mapped relationship or stable card has a display-zero P value. No candidate is based on `P = 0`, `p = 0.000`, finite precision, underflow, or nonzero-tail reasoning. The conditional independent-contradiction field is therefore not required for C001-C007.

## C001 — Primary-outcome 72-hour clock origin is not stated consistently

- **Category audit:** `Cross-document numeric inconsistency` is an allowed primary category. The report must keep the issue limited to an unaligned quantitative time-origin label.
- **Evidence-card completeness:** The ledger supplies the statement, category, locations, printed evidence, rule, alternatives, and human question. The recheck supplies source matching, comparator matching, necessary and missing inputs, logical comparison, and observation-versus-inference separation. The final card still must present the exact report fields `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, and `Human verification steps` rather than relying on the two upstream artifacts.
- **Assumption audit:** The evidence does not establish that the analysis actually used different timestamps. “After surgery/operation” may be shorthand for “after the start of operation.” The card must say that the printed origin is not explicitly aligned, not that a different derivation occurred.
- **Arithmetic and logic:** No numerical recalculation is claimed. The matched counts and effects agree. The reproducible comparison is the absence versus presence of the phrase “start of operation.”
- **Pagination and links:** DOC-001 pp. 1, 5, and 6 and DOC-003 p. 9 are real, separately linked pages. No false candidate pagination was found. Final-report links must be regenerated relative to `.ai_paper_validation/final_report_1_5_3.md`.
- **Duplicate audit:** This is one time-origin relationship spanning S001, S002, and S019, not three candidates and not a duplicate of the 24-hour/72-hour window issue in C002.
- **Conclusion and downstream bounds:** The evidence does not show that the primary counts, effect estimate, or paper conclusion changes. If confirmed, an extractor could copy an ambiguous endpoint clock origin; no propagation is assumed.
- **Required report repair:** State the missing derivation inputs and ask which timestamp was used. Include direct verification of the final data dictionary, timestamp fields, and derivation code.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Postoperative opioid-consumption window is 24 hours versus 72 hours

- **Category audit:** `Cross-document numeric inconsistency` is an allowed primary category and accurately identifies the matched measure-window difference.
- **Evidence-card completeness:** The ledger and recheck jointly support every factual component. The final card must add the exact report fields `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, and `Human verification steps` in report-card form.
- **Assumption audit:** The evidence does not show that the 24-hour values were mislabeled, that a 72-hour analysis was omitted, or that an undocumented amendment occurred. Those remain alternatives.
- **Arithmetic and logic:** `72 hours - 24 hours = 48 hours` is correct. Cumulative 24-hour and 72-hour consumption are not interchangeable. The supplied aggregates cannot reconstruct the missing 72-hour values.
- **Pagination and links:** DOC-001 pp. 4 and 6, DOC-002 p. 17, and DOC-003 p. 11 are real, separately linked pages. No false candidate pagination was found.
- **Duplicate audit:** This is a postoperative opioid-accumulation window issue and is distinct from C001 and C003.
- **Conclusion and downstream bounds:** The evidence does not establish a treatment-effect or conclusion change. If confirmed, an extractor could attach the reported medians to the wrong accumulation window.
- **Required report repair:** Name the missing amendment, final outcome dictionary, populated 72-hour output, and derivation record, and ask which window produced 70.6 mg and 45.0 mg.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Unplanned-readmission window is 90 days versus 30 days

- **Category audit:** `Cross-document numeric inconsistency` is an allowed primary category. The issue includes an internal article mismatch and matching planning-document comparators.
- **Evidence-card completeness:** The ledger and recheck provide direct values, comparators, arithmetic, alternatives, and the unresolved question. The final card must add the exact report fields `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, and `Human verification steps`.
- **Assumption audit:** The printed counts cannot identify their ascertainment window. The card must not select a label error or endpoint amendment without the missing readmission dates and final output.
- **Arithmetic and logic:** `90 days - 30 days = 60 days` is correct. `31 / 279 x 100 = 11.11%`, which rounds to 11.1%, and `34 / 278 x 100 = 12.23%`, which rounds to 12.2%. The arithmetic validates the denominators but not the time window.
- **Pagination and links:** DOC-001 pp. 4 and 8, DOC-002 p. 18, and DOC-003 pp. 10 and 27 are real, separately linked pages. No false candidate pagination was found.
- **Duplicate audit:** Numeric-review and cross-source observations used the same counts, comparator, and window rule and were correctly merged before C003 was assigned.
- **Conclusion and downstream bounds:** The evidence does not show that the counts or paper conclusion are wrong. If confirmed, an extractor could code the 31 and 34 events as 30-day or 90-day readmissions incorrectly.
- **Required report repair:** Ask for participant-level dates, final cutoff output, outcome dictionary, and amendment history; do not claim which window governs until checked.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — ERAS subgroup cut points differ from the protocol bands

- **Category audit:** `Measure, label, or scale inconsistency` is an allowed primary category. The report should frame this as unresolved comparability of printed category definitions.
- **Evidence-card completeness:** The ledger and recheck supply the printed bands, eFigure thresholds, three counts, arithmetic, missing definitions, and human question. The final card must add the exact report fields `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, and `Human verification steps`.
- **Assumption audit:** The protocol introduces its bands with “e.g.,” so it is unsupported to treat them as mandatory final cut points. The eFigure also states that the high/moderate/low definitions were not predefined, and the SAP supplies category names without cut points. The card must foreground these source-grounded alternatives. It must not state that the protocol rule governed the final model.
- **Arithmetic and logic:** `4 / 10 x 100 = 40%` is correct; 40% lies within the printed 30%-60% example band while the eFigure's fewer-than-5 rule places 4/10 in low. `191 + 274 + 92 = 557` is correct. A moderate range of 5-6 is only an inference if the displayed categories are exhaustive and mutually exclusive.
- **Pagination and links:** DOC-002 pp. 17 and 18, DOC-003 p. 15, and DOC-004 p. 2 are real, separately linked pages. No false candidate pagination was found.
- **Duplicate audit:** C004 concerns cut-point definitions. C007 concerns the number of named factor levels. They share ERAS evidence but have different comparators and rules and are not duplicates.
- **Conclusion and downstream bounds:** The evidence does not establish erroneous subgroup assignments or an altered interaction result. If confirmed, an extractor could reproduce or label the adherence categories incorrectly.
- **Required report repair:** Include the protocol's “e.g.” qualifier, the eFigure statement that definitions were not predefined, the absent moderate definition, final code, eligible-item denominator rule, and supersession record. Phrase the candidate as a definition-reconciliation question.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — The eFigure assigns both 99% and 95% labels to the same intervals

- **Category audit:** `Statistical reporting inconsistency` is the correct allowed primary category.
- **Evidence-card completeness:** The ledger and recheck support the two direct labels, their visual linkage, the SAP comparator, missing calculation metadata, alternatives, and human question. The final card must add the exact report fields `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, and `Human verification steps`.
- **Assumption audit:** The SAP supports a 99% intention but does not prove the confidence level used to calculate the plotted values. The card must not choose the legend or caption as correct without the missing statistical output.
- **Arithmetic and logic:** `99% - 95% = 4 percentage points` is correct, and explicit confidence-level labels have no rounding tolerance. The candidate does not depend on reconstructing an interval.
- **Pagination and links:** DOC-004 p. 2 and DOC-003 p. 15 are real links. The direct render closed the graphical-text limitation. No false candidate pagination was found.
- **Duplicate audit:** Numeric and statistical pass-1 observations concerned the same interval set and same label conflict and were correctly merged before C005. The application of one conflict to multiple subgroup rows does not create multiple candidates.
- **Conclusion and downstream bounds:** The evidence does not show that subgroup estimates or the main conclusion change. If confirmed, an extractor could record the displayed subgroup intervals under the wrong confidence level.
- **Required report repair:** Distinguish the overall 95% interval from within-subgroup intervals where relevant, and require the populated output or interval-construction metadata before selecting the correct label.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Day-5 EQ-5D inference conflicts with blanket no-difference prose

- **Category audit:** `Statistical reporting inconsistency` is the correct allowed primary category.
- **Evidence-card completeness:** The ledger and recheck provide the table values, prose, framework, arithmetic, missing narrative rule, alternatives, and human question. The final card must add the exact report fields `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, and `Human verification steps`.
- **Assumption audit:** The row supports a nominal time-specific non-null contrast, not an overall EQ-5D treatment effect, clinical importance, or a conclusion change. The prose may use an unreported omnibus or endpoint-level decision rule.
- **Arithmetic and logic:** `-0.111 < -0.057 < -0.003` is correct; zero is outside the interval because the upper endpoint is below zero; and `.04 < .05`. These comparisons reproduce the nominal row-level inference. No exact P-value reconstruction is necessary.
- **Pagination and links:** DOC-001 pp. 5 and 6 and DOC-003 pp. 13 and 14 are real pages. The ledger cites p. 13 and the recheck adds the relevant p. 14 continuation. The final card should link both support pages if it uses both statements. No false candidate pagination was found.
- **Duplicate audit:** This table-to-prose relationship is distinct from interval-label C005 and from the ERAS candidates.
- **Conclusion and downstream bounds:** The evidence does not establish an overall quality-of-life effect or that the paper conclusion is wrong. If confirmed, an extractor could omit a nominal day-5 contrast or incorrectly treat a blanket summary as applying to every time point.
- **Required report repair:** Explicitly label the inference nominal and time-specific, state that no secondary multiplicity adjustment was planned, and ask for the estimand or decision rule governing the narrative.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — ERAS subgroup is labeled as two levels versus three levels

- **Category audit:** `Measure, label, or scale inconsistency` is an allowed primary category.
- **Evidence-card completeness:** The ledger and recheck supply the two-level phrase, three-level SAP/eFigure display, counts, interaction P value, missing model coding, alternatives, and human question. The final card must add the exact report fields `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, and `Human verification steps`.
- **Assumption audit:** The three displayed rows do not prove the final interaction model matrix or degrees of freedom. “High vs low” may be shorthand or may describe a separate contrast. The card must describe incomplete labeling, not assert the model coding.
- **Arithmetic and logic:** `191 + 274 + 92 = 557` is correct. The one printed interaction P value beside three rows supports a three-level display but is not enough to reconstruct factor coding.
- **Pagination and links:** DOC-001 p. 5, DOC-003 p. 15, and DOC-004 p. 2 are real, separately linked pages. No false candidate pagination was found.
- **Duplicate audit:** C007 concerns omitted naming of the moderate level; C004 concerns category thresholds. They are distinct relationships and must remain separate.
- **Conclusion and downstream bounds:** The evidence does not show that the interaction calculation or paper conclusion is wrong. If confirmed, an extractor could record a two-level subgroup when the displayed result uses three named strata.
- **Required report repair:** Ask for the final model formula, factor coding, degrees of freedom, contrast matrix, and populated output, and bound the statement to the observed label mismatch.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Required coordinator and report-generator repairs

1. Add this fresh quality-control auditor to `agent_execution_manifest.md` exactly once, using its runtime ID, `gpt-5.6-sol`, `high`, `FRESH_SPAWN`, and `quality/evidence_quality_audit.md`.
2. Replace the `coverage_manifest.md` evidence-quality placeholder scope with the explicit seven-ID list and mark the row `COMPLETE`. After report assembly, do the same for the report-generation row.
3. Generate all seven final evidence cards with every exact field required by `report_spec.md`. Use the five-field adjudication template shown under every candidate above, with `__` for every value.
4. Generate final-report evidence links relative to `.ai_paper_validation/final_report_1_5_3.md`; do not copy the deeper relative prefixes from the ledger or recheck. Use one PDF page per link ending in `#page=N`.
5. Apply the candidate-specific wording repairs for C001, C004, C006, and C007 so ambiguity is not presented as a proved production mechanism or conclusion change.

## Limitations

The supplied package lacks participant-level data, final endpoint derivation records, some amendment history, populated model output, subgroup interval-construction metadata, factor coding, contrast matrices, and a stated EQ-5D narrative decision rule. These limitations prevent selecting among the source-grounded alternatives but do not prevent reproducing the seven printed quality-control relationships. Run finalization, report assembly, token accounting, final hash recording, HTML rendering, and mechanical validation remain coordinator stages after this audit.
