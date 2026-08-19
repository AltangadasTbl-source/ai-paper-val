# Evidence-Quality Audit for the Quantitative Quality-Control Review

This audit is complete for the current immutable stable set, C001, C002, C003, C004, C005, and C006. All six IDs remain **Pending Human Adjudication**. The audit does not rank, remove, renumber, combine, or suppress any stable ID.

## Coverage and execution status

- **Direct-source coverage:** Four supplied PDFs contain 99 source units: 11, 65, 22, and 1 PDF pages. The page counts were reproduced with `pdfinfo`. In every `source_coverage.md` row, reusable units plus fresh-required units equal total units, mapped units equal total units, and status is `COMPLETE`. The totals are 26 reusable units plus 73 fresh-required units, yielding 99 mapped units. The main map closes 11 of 11 pages; the support map closes 88 of 88 pages. Administrative, reference, instrument, and no-applicable-result pages are explicitly recorded rather than omitted.
- **Reusable-plus-fresh partition:** DOC-001 pp. 1-11 and DOC-003 pp. 8-22 are reusable-backed. DOC-002 pp. 1-65, DOC-003 pp. 1-7, and DOC-004 p. 1 are fresh-required and directly mapped. Thus every direct-source row has both a closed unit partition and a durable mapping artifact.
- **Relationship coverage:** The numeric inventory contains 91 stable records: N001-N088 plus N038a, N038b, and N039a. The statistical inventory contains 151 stable records: S001-S148 plus S028a, S028b, and S029a. The mapping artifacts, numeric checker, cross-source checker, statistical pass 1, statistical pass 2, ledger, and recheck jointly cover these assigned scopes. Statistical pass 2 explicitly returns every one of the 151 S IDs as `PASS_2_COMPLETE`.
- **No count boundary:** The inventories start from all mapped source units and state that old candidate, queue, critic, and report records were not scientific inputs. The maps include all 99 source pages, the numeric checker covers all 91 N relationships, both statistical passes cover all 151 S relationships, and the cross-source checker states that it reports all qualifying observations in scope. Nothing in the audited discovery artifacts indicates a rank-based, desired-count, count-limited, or legacy-candidate boundary.
- **Coverage-manifest paths:** Every manifest row has exactly one undecorated relative artifact path. The completed upstream artifact paths resolve. The `evidence_quality` path resolves to this artifact. The future report row remains a downstream coordinator task.
- **Routing:** `routing_preflight.md` reports `PASS`, `Coordinator inference: PASS`, execution mode `INTERACTIVE_CLI`, the required Sol/Terra model-effort matrix, and all nine named presets. `agent_execution_manifest.md` records statistical pass 1 as `/root/statistics_pass_1` and statistical pass 2 as `/root/statistics_pass_2`; these are distinct fresh runtime IDs, each using `gpt-5.6-terra` with `high` reasoning effort and a different durable artifact.
- **Source integrity:** All four direct-source hashes and all 54 reused-artifact hashes reproduce from the before-hash ledgers. No source or reused asset failed the hash check.
- **Display-zero boundary:** No stable candidate mentions `P = 0`, `p = 0.000`, or an equivalent P-value display. The `0%` remission display with a source-supplied `2e-16` rate is retained as a non-candidate diagnostic in N084, S047, S131, and S147. None of C001-C006 depends on finite precision, underflow, or nonzero-tail reasoning. Therefore no candidate requires the conditional independent-contradiction field.
- **Stable-ID reconciliation:** `candidate_ledger.md` and `verification/evidence_recheck.md` each return C001-C006 under `## C00X —` headings. This audit returns the same six headings below. Statistical pass 2 reported no new proposal; the complete coverage audit subsequently identified C006 from already mapped N041/N081 and S030/S134, and a fresh Sol/high repair rechecker confirmed its direct-source facts before this audit closed.

## Completed repairs and remaining coordinator tasks

1. **Completed:** `coverage_manifest.md` now enumerates the exact 91 numeric identities, N001-N088 plus N038a, N038b, and N039a; no nonexistent N089-N091 are claimed.
2. **Completed:** `checkers/cross_source_consistency.md` now locates the death Results narrative on PDF p. 7 and Table 3 on PDF p. 8.
3. **Completed:** C006 was appended without changing C001-C005, received a fresh targeted direct-source recheck, and was merged into the canonical recheck. The ledger and canonical recheck opening count/scope sentences now identify all six candidates.
4. After this audit is incorporated, set the `coverage_manifest.md` `evidence_quality` scope to `C001 C002 C003 C004 C005 C006` and its status to `COMPLETE`.
5. Add the fresh quality-control-auditor runtime to `agent_execution_manifest.md` exactly once with model `gpt-5.6-sol`, reasoning effort `high`, start mode `FRESH_SPAWN`, and artifact `quality/evidence_quality_audit.md`.
6. The report-generation stage must return C001-C006 and add the exact evidence-card labels required by `report_spec.md`. Each card's human fields must use this exact blank template:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

No audited upstream candidate artifact currently contains a populated human field. The final report must not replace any `__` with prose, a dash, a checkbox, or an inferred value.

## C001 — Figure 1 allocation branches exceed the displayed available cohort by 10 participants

- **Evidence quality:** Direct PDF p. 3 shows a parent box of 305 and connected branches of 193 and 122. The same page reports enrolled treatment groups of 166 and 96. The candidate ledger and mechanical recheck match the source text.
- **Calculation and reproducibility:** `193 + 122 = 315`, and `315 - 305 = 10`. The separate enrollment identity is `166 + 96 = 262`; `262 / 305 x 100 = 85.9016%`, which supports the printed 86% after whole-percent rounding. All inputs are printed on PDF p. 3.
- **Assumption and alternatives:** The branch-partition rule is supported by the figure's connecting lines but remains conditional because the source does not separately define the 193/122 population. The ledger properly retains the alternatives that those numbers reflect an earlier assignment cohort, that the parent count differs, or that one or both branch counts or labels differ. No participant-level flow crosswalk is supplied.
- **Relationship overlap:** N010 is the direct flow relationship and S136 supplies broader population context. Their scopes overlap but are not competing candidate cards. The checker provenance was combined before stable-ID assignment, and no second stable C ID represents this same count-rule comparison.
- **Category and scope:** `Denominator, proportion, or total inconsistency` matches `QUALITY_CONTROL_SCOPE.md`. The observation concerns a printed flow identity. It does not establish a change in any reported treatment effect or paper-level conclusion.
- **Pagination and links:** PDF p. 3 is the truthful page. The source filename resolves. The final card must turn the locator into a PDF link ending in `#page=3`.
- **Downstream-impact boundary:** If the observation is confirmed, an extractor could copy the displayed allocation count, available-cohort count, retention denominator, or missingness quantity inconsistently. No downstream use or harm is asserted to have occurred.
- **Evidence-card field audit:** The ledger supplies the category, source location, printed evidence, arithmetic rule, alternatives, direct-observation boundary, remaining question, and provenance. The final card must separately label `Candidate statement`, `Exact source locations`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, and `Human verification steps`, then append the exact blank human template above.
- **Required card repair:** State explicitly that the 193/122 population definition and treatment-arm distribution of the 11-person difference between 316 and 305 are unavailable, and ask which count or population label is intended. Do not state that the treatment-effect analysis used an incorrect denominator.

## C002 — Supplement eTable 2 mixes year-12 headings with year-7 quantitative footnote definitions

- **Evidence quality:** Supplement PDF pp. 15-16 directly show a year-12 title and two `Year 12` columns. Footnotes a-c directly define baseline and year-7 data, 7-year-over-baseline changes or odds, and year-7 group comparisons. Main PDF p. 3 points to eTable 2 for the 12-year HbA1c result. Footnote e also calls remission a 12-year rate.
- **Calculation and reproducibility:** This is a label identity check rather than numeric arithmetic: year 12 and year 7 are different follow-up times. The conflicting labels are printed in the same table and cannot be reconciled by rounding.
- **Assumption and alternatives:** No supplied analysis output maps each eTable 2 column to a visit. The current wording appropriately treats copied residual footnotes, an incorrect heading, or an intentional but unstated mixed-timepoint table as alternatives. It does not select one explanation.
- **Relationship overlap:** N083 and N084 retain the continuous and binary table relationships; S036-S052 retain row-level inferential records; S130 is the dedicated table-wide time-label comparison. This creates possible bookkeeping overlap but preserves distinct row and table-wide scopes. The report should cross-reference these records and present only C002 for the time-label contradiction.
- **Category and scope:** `Measure, label, or scale inconsistency` is an exact allowed category. The candidate concerns estimand time labels and does not establish that any displayed estimate itself is numerically wrong or that the paper's conclusions change.
- **Pagination and links:** Supplement pp. 15-16 and main p. 3 are truthful locations. The final card needs separate PDF links ending in `#page=15`, `#page=16`, and `#page=3`.
- **Downstream-impact boundary:** If confirmed, an extractor could attach a 7-year or 12-year timepoint to the wrong descriptive value, change, odds ratio, or P value. No actual propagation is claimed.
- **Evidence-card field audit:** The ledger contains the core evidence, rule, alternatives, observation/inference split, and human question. The final card still needs the exact report labels for the candidate statement, reported-versus-comparator, reasoning procedure, mechanical recheck, quality-control relevance, bounded downstream impact, human steps, and blank human fields. The `Calculation` field should state that no arithmetic is needed and reproduce the year-12 versus year-7 label comparison.
- **Required card repair:** Name the absent column-to-visit analysis specification and ask which visit governs every descriptive, change, comparison, binary-odds, and P-value column. Keep C003's separate P-value comparison distinct.

## C003 — Matched 12-year HbA1c result has incompatible printed P values

- **Evidence quality:** Main PDF pp. 1 and 3 print a 12-year surgery-minus-medical/lifestyle HbA1c difference of -1.1 percentage points, 95% CI -1.7 to -0.5, and `P = .002`. Supplement PDF p. 15 prints the same displayed estimate and interval under its year-12 heading with `P < .001`. The main text explicitly points to eTable 2.
- **Calculation and reproducibility:** The printed P-value statements do not overlap because `.002 < .001` is false. The estimate and interval match at displayed precision. This is a direct cross-location comparison and does not depend on reconstructing a tail probability.
- **Assumption and alternatives:** Exact analytic equivalence is not fully documented because unrounded output, row-specific test details, covariance, variance method, and the C002 timepoint mapping are absent. The candidate appropriately asks whether the two locations use the same analysis and retains a different test, model, variance method, or timepoint as an alternative.
- **Relationship overlap:** N003, N084, S002, S036, and S129 all touch this result; S129 is the dedicated cross-location repetition. This is possible relationship-level duplication and should be cross-referenced as one stable candidate, C003. It does not justify altering any stable C ID.
- **Category and scope:** `Cross-document numeric inconsistency` is an exact allowed category. The source-grounded issue is the incompatible repeated P displays for an apparently matched result. It does not establish which P value belongs to the intended analysis or that the substantive result changes.
- **Pagination and links:** Main pp. 1 and 3 and supplement p. 15 are truthful locations. Each final-card PDF link must end in its corresponding `#page=N` fragment.
- **Downstream-impact boundary:** If confirmed as the same analysis, an extractor could copy `.002` or `<.001` for the same effect record. The final card must not state that this changes a meta-analysis effect estimate, guideline, or paper conclusion.
- **Evidence-card field audit:** The ledger supplies the source values, comparison rule, alternatives, observation/inference separation, question, and provenance. The final card must use all exact report labels, explicitly include the mechanical recheck, give human steps to inspect the exact analysis output and table-generation record, and append the blank human template. No independent-contradiction-beyond-display-zero field is needed because neither P display is zero.
- **Required card repair:** Preserve the C002 time-label uncertainty as a named alternative. Do not describe the two analyses as definitively identical until the row-specific analysis definition is supplied.

## C004 — The same year-7 glycemic outcome is labeled as both HbA1c less than or equal to 6.5% and HbA1c below 6.5%

- **Evidence quality:** Main PDF p. 4 uses the inclusive wording and cites Table 2 with `P = .002`. Main PDF p. 6 labels the matched row `HbA1c <6.5%, %` with the same P value and a printed OR of 2.89 (95% CI 1.48-5.64). Supplement PDF p. 4 supplies supporting binary-analysis context but does not print the threshold operator.
- **Calculation and reproducibility:** `{x: x < 6.5}` is a subset of `{x: x <= 6.5}`; only measurements exactly equal to 6.5 differ in membership. The logical comparison is exact.
- **Assumption and alternatives:** The package does not supply the programmed condition, preclassification precision, rounding convention, row analysis counts, or the count at exactly 6.5%. The candidate therefore supports a label inconsistency, not an assertion that a participant classification, OR, P value, or conclusion changes. Imprecise prose, a missing equality sign, or an undocumented precision rule remain source-consistent alternatives.
- **Relationship overlap:** N007 supplies the general outcome definition, N014/S009 the narrative comparison, and N039a/S029a the table row. These records are related but represent definition, narrative, and row scopes. Only C004 presents the operator comparison.
- **Category and scope:** `Measure, label, or scale inconsistency` is an exact allowed category. The threshold operator is part of the outcome measure label.
- **Pagination and links:** Main pp. 4 and 6 and supplement p. 4 are truthful locations. Final-card links must end in `#page=4`, `#page=6`, and `#page=4`, paired with their full filenames.
- **Downstream-impact boundary:** If confirmed, a data extractor could copy different binary-outcome definitions. No numerical or clinical impact is established without boundary-value data.
- **Evidence-card field audit:** The ledger contains category, exact locations, evidence, the set rule, alternatives, direct-versus-inferred boundaries, and the human question. The final card must add the exact report labels, a mechanical-recheck summary, a bounded relevance statement, human steps to inspect the programmed threshold and data dictionary, and the exact blank human template.
- **Required card repair:** State the missing programmed dichotomization and measurement-precision definitions. Keep any possible numeric impact conditional on observations at exactly 6.5%.

## C005 — Abstract percentage for four deaths does not reconcile with displayed group counts and denominators

- **Evidence quality:** Main PDF p. 1 prints four deaths, 2.2%, and two in each group. Main PDF p. 3 gives enrolled groups of 96 and 166. The death narrative is on PDF p. 7. Table 3 is on PDF p. 8 and prints 2 of 96 (2.1%) and 2 of 166 (1.2%). The ledger and recheck use these truthful pages.
- **Calculation and reproducibility:** `2 / 96 x 100 = 2.0833%`, which rounds to 2.1%; `2 / 166 x 100 = 1.2048%`, which rounds to 1.2%; and `4 / (96 + 166) x 100 = 1.5267%`, which rounds to 1.5%, not 2.2%. Every input is source printed.
- **Assumption and alternatives:** Treating 262 as the combined crude denominator is supported by the displayed group denominators, but the abstract does not name its denominator or measure. A smaller time-specific risk set, a complete-case or censoring convention, another population, or a transcription difference remains possible. The package lacks a participant-level mortality risk set.
- **Relationship overlap:** N005, N042, N044, N046, S004, S032, and S128 cover abstract, narrative, table, and safety context. These are overlapping contexts for one count/denominator comparison, retained as the single stable candidate C005.
- **Category and scope:** `Denominator, proportion, or total inconsistency` is an exact allowed category. The candidate does not assume that 2.2% is a crude proportion; it asks for the missing quantitative definition.
- **Pagination and links:** The ledger, recheck, and repaired cross-source checker correctly use p. 7 for the narrative and p. 8 for Table 3. Final-card links must separately use `#page=1`, `#page=3`, `#page=7`, and `#page=8`.
- **Downstream-impact boundary:** If confirmed, an extractor could copy a mortality count, percentage, or denominator that does not share one stated population definition. No effect on the study's treatment comparison or conclusion is established.
- **Evidence-card field audit:** The ledger contains the evidence, arithmetic, alternatives, direct/inferred boundary, question, and provenance. The final card must use the exact report labels, include the mechanical recheck and all three calculations, name the absent denominator/measure definition, give human steps to inspect the mortality risk set and abstract production record, and append the exact blank human template.
- **Required card repair:** Preserve the repaired p. 7 narrative and p. 8 table pagination, keep a distinct-risk-set explanation conditional, and avoid stating that an unstated denominator near 182 exists; only the approximate denominator implied by four divided by 2.2% can be derived.

## C006 — The same exploratory BMI subgroup boundary is labeled as both 35 or greater and greater than 35

- **Evidence quality:** Main PDF p. 7 defines the cited exploratory analysis as BMI 27 to less than 35 versus BMI 35 or greater. Supplement PDF p. 13 eFigure 6 repeatedly prints `BMI <35` and `BMI >35` in its title, legends, and explanatory text for the same HbA1c and weight-loss analysis. A fresh targeted Sol/high mechanical recheck confirmed both direct-source locations.
- **Calculation and reproducibility:** For a two-part partition at 35, the complement of `{x: x < 35}` is `{x: x >= 35}`. The supplement's pair `{x: x < 35}` and `{x: x > 35}` leaves `x = 35` unassigned, while the main-text higher set includes it. This is a logical set comparison and needs no arithmetic approximation.
- **Assumption and alternatives:** The subgroup-creation code, data dictionary, unrounded participant BMI values, preassignment precision or rounding rule, count exactly equal to 35, and explicit boundary-handling rule are absent. An omitted equality sign in the figure, imprecise main prose, or no participant at the exact boundary remain possible. None is established by the package.
- **Relationship overlap:** N041 and S030 retain the main subgroup result; N081 and S134 retain the supplement repetition and matched result. The boundary operator was not separately registered before the final coverage audit. C006 is distinct from C004 because it compares a BMI population partition and different source locations rather than the HbA1c outcome threshold.
- **Category and scope:** `Measure, label, or scale inconsistency` is an exact allowed category. The observation concerns the subgroup boundary label. It does not establish that group membership, estimates, P values, or paper-level conclusions change.
- **Pagination and links:** Main p. 7 and supplement p. 13 are truthful locations. The targeted recheck links resolve and end in `#page=7` and `#page=13`. The final card must preserve those full filenames and page fragments.
- **Downstream-impact boundary:** If confirmed, an extractor could copy `>=35` or `>35` as the subgroup definition. No different membership or quantitative effect is claimed without participant-level boundary data.
- **Evidence-card field audit:** The ledger and recheck provide the category, exact source text, comparator, logical rule, missing definitions, alternatives, observation/inference split, and remaining question. The final card must use every exact report label, summarize the fresh mechanical recheck, provide human steps to inspect the subgroup code and data dictionary, state the bounded relevance, and append the exact blank human template.
- **Required card repair:** Keep possible membership and estimate effects conditional. Ask which operator was implemented and how BMI exactly 35 was handled.

## Audit limitations

- Aggregate PDFs do not supply participant-level flow, mortality-risk-set, threshold-boundary, or model-output data. The audit can reproduce the printed contradictions and calculations but cannot select the intended source value or label.
- eTable 2's year-7/year-12 conflict limits exact analytic matching for C002 and C003.
- Sparse figure trajectories lack printed point coordinates and were appropriately not reverse engineered.
- The final report and its candidate cards are downstream of this audit. Card-label, link, and blank-field requirements are therefore recorded as mandatory coordinator tasks rather than treated as already assembled.
- Relationship records deliberately preserve row, narrative, cross-location, and table-wide scopes. The overlaps named above require cross-references so they are not mistaken for additional stable candidates.

## Compact completion record

- **Coverage status:** Complete for 99 of 99 source units, 91 numeric relationships, 151 statistical relationships in both passes, and all six stable candidates, subject to the remaining coordinator tasks listed above.
- **Covered IDs:** C001, C002, C003, C004, C005, C006.
- **Repairs:** Numeric-scope, C005-pagination, and six-candidate count/scope repairs are complete; C006 was appended and mechanically rechecked. Close the manifest quality row, add the auditor execution row, and assemble every final card with exact labels, bounded language, source-page links, and exact `__` human-field blanks.
- **Artifact:** `.ai_paper_validation/review_1_5_3/quality/evidence_quality_audit.md`.
