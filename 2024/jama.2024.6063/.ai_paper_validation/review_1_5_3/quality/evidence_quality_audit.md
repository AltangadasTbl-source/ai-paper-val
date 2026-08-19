# Evidence-Quality Audit

- **Audit status:** COMPLETE; coordinator repairs are listed below.
- **Stable candidate set audited:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016.
- **Scientific coverage:** 41 of 41 direct PDF pages mapped. The four source rows partition as 24 reusable units plus 17 fresh-required units, and every row has mapped units equal to total units.
- **Relationship coverage:** N001 through N028, all 52 cross-source match groups, and S001 through S091 were covered. Every S relationship has an explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` record.
- **Agent routing:** statistical pass 1 (`/root/statistical_pass_1`) and statistical pass 2 (`/root/statistical_pass_2`) are distinct fresh `gpt-5.6-terra`/`high` agents. All currently executed mandatory stages have distinct runtime IDs and the required model/effort pair.
- **Discovery boundary:** the source inventory, asset inventory, maps, and checkers state that discovery was rebuilt from the complete source-linked evidence scope. No count boundary, review queue, or old candidate set controlled discovery.
- **Source integrity:** all four direct-source hashes and all 55 reused-artifact hashes matched their before-review records during this audit.
- **Display-zero rule:** no stable candidate is based on a P value displayed as zero. No candidate card mentions such a display, so the conditional independent-contradiction field is not applicable to the current set.
- **Candidate identity:** the ledger and mechanical recheck contain the identical ordered set C001 through C016. This audit returns the same set once each.
- **Categories and tone:** every ledger category is one of the exact categories in `QUALITY_CONTROL_SCOPE.md`. The candidate wording is neutral quality control and does not assign severity, scientific disposition, or paper-level conclusion impact.

## Coverage and artifact-conformance repairs for the coordinator

1. In `source_coverage.md`, replace each status cell of the form `COMPLETE — explanation` with the exact status `COMPLETE`. Move the explanatory text outside the status cells. The unit arithmetic itself is complete: 10/10, 15/15, 1/1, and 15/15 mapped, for 41/41 total.
2. In `coverage_manifest.md`, every row has exactly one plain relative artifact path. After this audit artifact is present, change the `evidence_quality` row from `PENDING` to `COMPLETE`. Change `report_generation` to `COMPLETE` only after the report exists. The statistical rows enumerate all S001 through S091, and all four candidate-stage rows enumerate C001 through C016.
3. Repair `routing_preflight.md` to include the validator-required exact unbolded fields and values: `Status: PASS`, `Provider: openrouter`, coordinator model/effort, ordinary specialist model/effort, statistical specialist model/effort, Sol specialist model/effort, `Fixed model matrix: PASS`, `Named agent presets: PASS`, `Named agent preset count: 9`, `Mandatory specialist stages: 10`, `Mandatory agent start contract: FRESH_DISTINCT`, `Coordinator inference: PASS`, `Execution mode: INTERACTIVE_CLI`, `Launch command: codex --approve-for-me`, and `Checked UTC:` with the UTC timestamp. The current matrix content supports these values, but several exact fields and labels are absent or differently formatted.
4. Forty source-PDF links in `extraction/support_quantitative_evidence.md` and `checkers/cross_source_consistency.md` use `../../source.pdf#page=N`. From those two subdirectories, the direct sources require `../../../source.pdf#page=N`. The page numbers are within the true 10-, 15-, 1-, and 15-page source bounds, but the current relative paths do not resolve. Candidate-ledger links and evidence-recheck links resolve correctly.
5. Repair the C012 mapping and card wording. `extraction/support_quantitative_evidence.md` calls the eTable 1 value `-0.27` a krill-minus-placebo contrast. The printed arm changes give `-19.93 - (-20.21) = +0.28`, while the table prints `-0.27` and does not define operand order. Remove the unsupported krill-minus-placebo assertion from the map, cross-source checker, ledger, recheck summary, and future card. State instead that matched primary-result displays use opposite signs and that the supplied sources do not establish a common contrast orientation. Retain C012 and its exact human question.
6. Add the fresh report-generator agent to `agent_execution_manifest.md` when spawned, with its required distinct runtime ID, `gpt-5.6-terra`/`medium`, `FRESH_SPAWN`, and primary artifact. Do not mark the workflow complete before that row, the report artifacts, token accounting, final hashes, and validation are complete.

## Evidence-card field audit

The ledger is not in final-report card form. Every C001-C016 entry already supplies an exact category, source locations, source evidence, comparator/rule content, direct-versus-derived separation, alternatives, a human question, and checker provenance. Every future report card still needs these exact labels that are absent from the ledger form: **Candidate statement:**, **Reported-versus-comparator:**, **Reasoning procedure:**, **Calculation:**, **Alternative source-grounded interpretations:**, **Mechanical evidence recheck:**, **Quality-control relevance:**, **Potential downstream evidence impact:**, **Human verification steps:**, and **Human adjudication fields:**.

No human-adjudication subfield is currently present in the ledger or recheck, so no nonblank value was found. Every final card must add exactly one of each of the following and leave each value exactly blank as `__`:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

The downstream-impact field for each card must be conditional and bounded to the specific value a data extractor, systematic review, meta-analysis, or guideline could copy if the candidate is confirmed. None of the evidence supports a claim that propagation occurred or that the paper-level conclusion changes.

## C001 — Placebo discontinuation counts differ between Figure 1 and the Results text

- **Evidence-card fields missing:** all ten exact labels listed in the evidence-card field audit.
- **Evidence and arithmetic audit:** Main PDF pp. 3 and 7 are truthful locations. `111 + 21 = 132`, `113 + 111 = 224`, `17 + 21 = 38`, `17 + 23 = 40`, and `132 - 23 = 109` are reproduced correctly.
- **Assumption boundary:** equivalence of “discontinued” with “withdrew or were lost” and of “completed treatment” with “completed the trial” is not supplied. The ledger and recheck appropriately make that comparison conditional; the final card must retain the missing category definitions.
- **Duplicate and impact audit:** this is not a duplicate of another stable ID. Its bounded copy target is the placebo and total completion/attrition counts, not a claim about treatment effect or the paper conclusion.
- **Coordinator card repair:** add the exact report fields, cite the mechanical recheck, state the zero-tolerance integer identities, provide the two-category-definition alternative, and use the exact blank adjudication template.

## C002 — eTable 2 names 167 and 165 for the overall adherence population

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Supplement 3 p. 3 is truthful. `82/83 = 98.7952%`, `81/84 = 96.4286%`, and `83 + 84 = 167` reproduce the displayed row at one-decimal precision.
- **Assumption boundary:** the arm denominators 83 and 84 are derived from the integer counts, displayed percentages, and printed row total. Whether the footnote's 165 defines that same population is unresolved and must remain conditional.
- **Duplicate and impact audit:** C002 is related to but distinct from C016: C002 compares the eTable row with its footnote, whereas C016 compares the main narrative with the cited row. The bounded copy target is the adherence or per-protocol denominator.
- **Coordinator card repair:** preserve the distinct comparator, state the missing population definition, add the exact report fields and mechanical recheck, and use the exact blank adjudication template.

## C003 — eTable 5 krill “Smaller by 1 unit” percentage conflicts with 10 of 107

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Supplement 3 p. 8 is truthful. `100 × 10/107 = 9.3458%`, which rounds to 9%, not 12%, at whole-percent precision.
- **Assumption boundary:** use of the printed arm total 107 as the category denominator is supported by the table structure, but an unprinted denominator remains a source-grounded alternative.
- **Duplicate and impact audit:** this is a distinct printed cell relationship, not a duplicate of C004-C008. The bounded copy target is this one ordinal imaging-category proportion.
- **Coordinator card repair:** add the exact report fields, the tolerance and calculation, the alternative-denominator question, the mechanical recheck, and the exact blank adjudication template.

## C004 — eTable 5 krill “No change” percentage conflicts with 80 of 107

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Supplement 3 p. 8 is truthful. `100 × 80/107 = 74.7664%`, which rounds to 75%, not 72%.
- **Assumption boundary:** the displayed arm total is the source-supported denominator; any other denominator is unreported.
- **Duplicate and impact audit:** the comparator is the separate krill no-change cell, so it remains distinct from the other eTable 5 IDs. The bounded copy target is the no-change proportion.
- **Coordinator card repair:** add the exact report fields, calculation, tolerance, alternative interpretation, mechanical recheck, and exact blank adjudication template.

## C005 — eTable 5 krill “Larger by 1 unit” percentage conflicts with 12 of 107

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Supplement 3 p. 8 is truthful. `100 × 12/107 = 11.2150%`, which rounds to 11%, not 12%.
- **Assumption boundary:** no category-specific denominator other than the displayed arm total is supplied.
- **Duplicate and impact audit:** this distinct worsening-category cell is not a duplicate of C003 or C004. The bounded copy target is this category percentage.
- **Coordinator card repair:** add the exact report fields, calculation and tolerance, alternative denominator, mechanical recheck, and exact blank adjudication template.

## C006 — eTable 5 placebo “Smaller by 2 units” percentage conflicts with 2 of 109

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Supplement 3 p. 8 is truthful. `100 × 2/109 = 1.8349%`, which rounds to 1.8%, not 1.9%, at one decimal. The discrepancy is approximately 0.0651 percentage point, just outside the stated 0.05 tolerance.
- **Assumption boundary:** another denominator or different underlying table inputs are not supplied but remain alternatives. The card must not imply importance from the size of the rounding difference.
- **Duplicate and impact audit:** the cell is distinct from C003-C005 and C007-C008. The bounded copy target is the printed decimal proportion only.
- **Coordinator card repair:** add the exact report fields, precision rule, calculation, mechanical recheck, neutral relevance, and exact blank adjudication template.

## C007 — eTable 5 placebo “Smaller by 1 unit” percentage conflicts with 16 of 109

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Supplement 3 p. 8 is truthful. `100 × 16/109 = 14.6789%`, which rounds to 15%, not 12%.
- **Assumption boundary:** a denominator near 133 could produce 12%, but it conflicts with the displayed arm total and is not printed.
- **Duplicate and impact audit:** this improvement-category cell is distinct from every other stable cell relationship. The bounded copy target is the category count/percentage pair.
- **Coordinator card repair:** add the exact report fields, calculation, alternative, mechanical recheck, and exact blank adjudication template.

## C008 — eTable 5 placebo “No change” percentage conflicts with 75 of 109

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Supplement 3 p. 8 is truthful. `100 × 75/109 = 68.8073%`, which rounds to 69%, not 72%.
- **Assumption boundary:** no alternate category denominator is supplied; a denominator near 104 is only an inferred alternative.
- **Duplicate and impact audit:** the placebo no-change cell is a distinct relationship. The bounded copy target is this descriptive ordinal-outcome proportion.
- **Coordinator card repair:** add the exact report fields, calculation, tolerance, alternative, mechanical recheck, and exact blank adjudication template.

## C009 — eTable 4 repeats week-4 function changes in the weight-bearing-pain row

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Supplement 3 p. 5 is truthful. The two arm-change estimate/interval pairs repeat exactly. `100 - 127 = -27` and `108 - 141 = -33` are correctly reproduced as diagnostics, not as reconstructed model estimates.
- **Assumption boundary:** the source does not supply cell-level estimand mapping, covariance, or source analysis output. The card must rest on the exact cross-row duplicate and must not claim that raw subtraction proves the intended modelled values.
- **Duplicate and impact audit:** numeric NP-009 and statistical SP1-01 were genuine duplicate proposals merged before stable IDs; no other stable ID repeats this relationship. The bounded copy target is the two weight-bearing-pain arm-change cells.
- **Coordinator card repair:** keep the diagnostic qualification, add the exact report fields and recheck, identify the source output needed for human verification, and use the exact blank adjudication template.

## C010 — eTable 4 repeats week-4 back-pain results in week-12 lower-leg strength

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Supplement 3 p. 6 is truthful. Both arm changes and the complete between-group estimate/interval/P fields repeat exactly. `72.6 - 66.5 = +6.1` and `70.2 - 65.9 = +4.3` are correct diagnostics only.
- **Assumption boundary:** modelled change can differ from descriptive subtraction, and coincidence cannot be excluded from supplied evidence. The direct issue is identical full output across distinct labels, units, times, and directions.
- **Duplicate and impact audit:** NP-010 and SP1-02 were merged before C010; C010 is not duplicated elsewhere. The bounded copy target is the week-12 strength result fields.
- **Coordinator card repair:** add the exact report fields, preserve the distinction between direct duplication and diagnostic arithmetic, cite the recheck, and use the exact blank adjudication template.

## C011 — eTable 4 repeats the week-12 hsCRP result in fasting glucose

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Supplement 3 p. 6 is truthful. The between-group estimate, interval, and `P = 0.92` repeat exactly. `0.09 - 0.15 = -0.06` is correctly labelled diagnostic and does not reconstruct the adjusted model.
- **Assumption boundary:** no supplied model mapping proves copying or supplies a corrected glucose value. `P = 0.92` is not a display-zero P value and triggers no display-zero conditional field.
- **Duplicate and impact audit:** NP-011 and SP1-03 were merged before C011. The bounded copy target is the week-12 fasting-glucose estimate, interval, and P value.
- **Coordinator card repair:** add the exact report fields, distinguish exact duplication from the diagnostic arm-change contrast, cite the recheck, and use the exact blank adjudication template.

## C012 — Key Points and other matched primary-result displays use opposite signs

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Main PDF pp. 1, 2, 6, and 7 and Supplement 3 p. 2 are truthful. The Key Points value is `+0.30`; the other matched displays are `-0.3` or `-0.27` with matching intervals and P values. Rounding `-0.27` gives `-0.3`.
- **Unsupported assumption requiring repair:** the current map and ledger call `-0.27` krill minus placebo. The printed arm changes instead give approximately `+0.28` for krill minus placebo and approximately `-0.28` for placebo minus krill. The source heading says “Absolute between group difference” but prints a negative value and does not define operand order. The card must not assert a common contrast orientation that the package does not supply.
- **Duplicate and impact audit:** C012 is the only stable sign/orientation relationship. The bounded copy target is the signed primary mean difference; the evidence does not support a claim that the interval, P value, or paper conclusion changes.
- **Coordinator card repair:** use an orientation-neutral candidate statement, present the sign displays exactly, name missing contrast orientation as the alternative, ask whether the difference is orientation, absolute-value wording, or a lost sign, add all exact report fields and the recheck, and use the exact blank adjudication template.

## C013 — Placebo extremity-pain event count is 6 in Table 3 and 5 elsewhere

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Main PDF pp. 1 and 8 and Supplement 3 p. 10 are truthful. The exact placebo event-count difference is one; the krill count is one in every location.
- **Assumption boundary:** identity of “lower-extremity pain” and “Pain in extremity” is strongly supported by the surrounding matched categories and eTable reference but is not defined by a supplied coding dictionary. Retain that alternative.
- **Duplicate and impact audit:** this event-count relationship is distinct from the overall adverse-event totals and from the cross-reference candidates C014-C015. The bounded copy target is the placebo category event count, not a participant risk or treatment conclusion.
- **Coordinator card repair:** add the exact report fields, preserve event-versus-participant language, cite the recheck, name the coding dictionary as the human verification source, and use the exact blank adjudication template.

## C014 — Table 3 regular-adverse-event footnote points to eTable 4 instead of eTable 7

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and logical audit:** Main PDF p. 8 and Supplement 3 pp. 5 and 10 are truthful. eTable 4 is the secondary-endpoint time-series table; eTable 7 is the adverse-event table cited by the narrative.
- **Assumption boundary:** stale supplement renumbering is a possible production explanation, not a demonstrated cause. No arithmetic is applicable.
- **Duplicate and impact audit:** C014 concerns footnote a and regular adverse events; it is distinct from C015, which concerns footnote c and serious adverse events. The bounded copy target is the table cross-reference used to locate event detail.
- **Coordinator card repair:** add the exact report fields, logical header/content comparison, mechanical recheck, production-version verification step, and exact blank adjudication template.

## C015 — Table 3 serious-adverse-event footnote points to eTables 5 and 6 instead of eTable 8

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and logical audit:** Main PDF p. 8 and Supplement 3 pp. 8, 9, and 14 are truthful. eTables 5 and 6 contain WORMS and analgesic-use content, while eTable 8 contains serious-adverse-event details and is cited by the narrative.
- **Assumption boundary:** an earlier numbering scheme remains an inferred alternative. No correction is prescribed from supplied production history.
- **Duplicate and impact audit:** this distinct serious-event cross-reference is not a duplicate of C014. The bounded copy target is the location reference for serious-event detail.
- **Coordinator card repair:** add the exact report fields, logical comparison, recheck, human production-history step, and exact blank adjudication template.

## C016 — Main-text 95% adherence does not reproduce the cited eTable 2 overall result

- **Evidence-card fields missing:** all ten exact labels listed above.
- **Evidence and arithmetic audit:** Main PDF p. 7 and Supplement 3 p. 3 are truthful. `82 + 81 = 163` and `163/167 × 100 = 97.6048%`, displaying as 97.6% or 98%, not 95%.
- **Assumption boundary:** the narrative numerator and denominator are absent, and eTable 2 itself names both 167 and 165. The pooled comparison is applicable only if the narrative and row use the same population; that unresolved condition must remain explicit.
- **Duplicate and impact audit:** C016 is distinct from C002 because its comparator is the narrative 95% versus the cited table, not the table row versus its footnote. The bounded copy target is the 24-week adherence percentage and its numerator/denominator.
- **Coordinator card repair:** add the exact report fields, conditional population rule, calculation, recheck, exact numerator/denominator human question, and exact blank adjudication template.

## Audit limitations

- Source analysis outputs, covariance and variance specifications, cell-level estimand mappings, adverse-event coding definitions, participant-level disposition definitions, adherence population definitions, and production-version histories are not supplied. They remain named human questions and do not authorize candidate deletion or adjudication.
- The 40 broken supporting-artifact links require a mechanical relative-path repair, but all cited candidate page numbers were found within the supplied PDFs and the canonical ledger/recheck evidence links resolve.
- The current artifact set precedes report generation, token accounting, final hash records, HTML rendering, and final validation. Those later stages cannot be confirmed by this audit and must be completed by the coordinator.
- No stable ID was deleted, merged, ranked, suppressed, renumbered, assigned severity, or given a scientific disposition in this audit.
