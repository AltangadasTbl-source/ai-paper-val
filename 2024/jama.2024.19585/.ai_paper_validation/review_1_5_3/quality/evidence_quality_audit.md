# Evidence Quality and Complete-Coverage Audit

- **Audit runtime ID:** `/root/quality_control_auditor`
- **Required route:** `gpt-5.6-sol` / `high`
- **Stable candidate set audited:** C001, C002, C003
- **Coverage status:** COMPLETE for source-unit and relationship-unit mapping; COORDINATOR REPAIR REQUIRED for C001 source interpretation and for downstream manifest/card completion.
- **Adjudication boundary:** Every stable ID remains Pending Human Adjudication. This audit does not delete, merge, renumber, rank, suppress, or assign a scientific disposition to any candidate.

## Audited scope

The audit read the governing scope and contract, `source_coverage.md`, `coverage_manifest.md`, both extraction maps, the 80-record numeric inventory, the 57-record statistical inventory, all four checker outputs, both statistical-pass records, `candidate_ledger.md`, `verification/evidence_recheck.md`, `agent_execution_manifest.md`, the source and reusable-asset inventories, and the before-hash ledgers. Direct PDF pages cited by C001-C003 were checked as source authority, including visual layout where hierarchy or table structure controls the comparison.

## Coverage, discovery, routing, and integrity findings

1. **Direct-source closure:** DOC-001 has 11/11 mapped PDF pages, DOC-002 has 46/46, and DOC-003 has 23/23, for 80/80 mapped source units. Reusable plus fresh-required units partition every row: DOC-001 11+0=11, DOC-002 0+46=46, and DOC-003 23+0=23. The fresh DOC-002 extraction contains 46 one-page native files and 46 one-page layout files. There is no unresolved scientific-coverage gap.
2. **Relationship closure:** The numeric inventory contains N001-N080, all 80 records were assigned to the numeric checker, and the statistical inventory contains S001-S057. The statistical inventory has 57 `PASS_1_COMPLETE` records and 57 `PASS_2_COMPLETE` records; the pass-2 checker also returns 57 explicit S rows.
3. **No count boundary:** The reusable-asset curator states that legacy candidates, checkers, verifier/critic material, and reports were not read as discovery inputs. Both quantitative inventories were rebuilt over all 80 direct-source pages. Checker scopes are stated as complete, and candidate production continued through all 80 N records and all 57 S records. No fixed-count, desired-count, queue, or early-stopping rule appears in the discovery artifacts.
4. **Fresh statistical runtimes:** Statistical pass 1 is `/root/statistics_pass_1` and statistical pass 2 is `/root/statistics_pass_2`. They are distinct fresh runtime IDs and both are recorded as `gpt-5.6-terra` / `high` with `FRESH_SPAWN`. Pass 2 explicitly received C001-C003 and the mechanical recheck and revisited S001-S057.
5. **Routing:** `routing_preflight.md` reports PASS, coordinator `gpt-5.6-sol` / `high`, ordinary specialists `gpt-5.6-terra` / `medium`, statistical specialists `gpt-5.6-terra` / `high`, Sol specialists `gpt-5.6-sol` / `high`, `Coordinator inference: PASS`, `INTERACTIVE_CLI`, and all nine named presets verified.
6. **Coverage-manifest paths:** Every existing coverage row contains one plain relative artifact path. All artifacts in rows currently marked COMPLETE exist. After this audit, the coordinator must change the `evidence_quality` row scope from `Stable candidate set and all coverage rows` to the explicit `C001, C002, C003` and mark it COMPLETE. The later `report_generation` row must likewise enumerate `C001, C002, C003`, not use `Stable candidate set` shorthand, and may be marked COMPLETE only after the report exists.
7. **Execution manifest:** All currently spawned specialist IDs are distinct and use the required routes. The report-generator row is not yet present because that stage has not run. The coordinator row still uses `COORDINATOR-CURRENT-SESSION`, which the contract presents as a placeholder; the coordinator must replace it with the exact current runtime ID if the runtime exposes one, then add the fresh report generator exactly once.
8. **Integrity:** `sha256sum -c` reproduced all three direct-source hashes and every reusable-artifact hash in the before ledgers. No source or reused artifact changed.
9. **Display-zero exclusion:** No stable C card mentions `P = 0`, `p = 0.000`, or equivalent. The statistical agents correctly distinguish DOC-002's printed `0.000` ICC grid value from a P value and treat `<.001` as a bounded display. No conditional `Independent contradiction beyond P=0 display` field is required for C001-C003.
10. **Categories and tone:** The ledger assigns one allowed primary category to each ID: C001 `Numeric or arithmetic inconsistency`, C002 `Cross-document numeric inconsistency`, and C003 `Measure, label, or scale inconsistency`. Wording is generally neutral and bounded. C001 nevertheless requires factual repair described below.

## C001 — Usual-care exclusion-reason hierarchy

### Source and calculation audit

The direct visual source on [DOC-001 PDF p. 5](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=5) does not support the current calculation in the numeric checker, ledger, or recheck. Figure 1 displays `13 Physician preference` as a top-level reason and places `7 Disease status or progression`, `4 Perceived psychosocial issues`, and `2 Reason not provided` at a deeper indentation beneath it. Those child counts reproduce their parent exactly: `7 + 4 + 2 = 13`.

The complete top-level usual-care exclusion calculation is therefore:

`13 Physician preference + 15 Treatment outside of trial network + 14 Cognitive disability + 7 Language + 4 Visual impairment + 3 No parent available + 2 Cancer not disclosed = 58`.

The current `71` calculation adds the parent value 13 and its three child values a second time. The parallel symptom-screening branch confirms the same hierarchy: `42 Physician preference` has deeper-indented children `32 + 4 + 2 + 4 = 42`. The main extraction map itself correctly records that parallel branch as a parent with bracketed children. Consequently, overlap, exhaustiveness, and a different denominator are not missing inputs needed to reproduce the printed usual-care total; the visual parent-child structure supplies the applicable rule.

### Evidence-card quality

- **Unsupported assumption:** Treating all ten displayed numbers as peer, mutually exclusive children of 58 ignores the source's indentation and the parallel branch.
- **Incorrect arithmetic procedure:** The addition is arithmetically accurate but structurally incorrect because it double-counts the `13 Physician preference` parent.
- **Possible duplicate relationship:** None. C001 is distinct from C002 and C003.
- **Pagination and link:** The DOC-001 p. 5 link resolves and is truthful. Final evidence should explicitly describe the visual indentation and the parallel left branch, because flattened text alone loses the hierarchy.
- **Conclusion impact:** The current conclusion that the printed exclusion reasons fail to reconcile is not source-supported as written. The source-grounded top-level counts reconcile exactly. This statement is an evidence-quality finding, not a scientific disposition, and C001 must remain present and Pending Human Adjudication.
- **Downstream impact boundary:** Do not claim altered participant flow or paper conclusions. If human review finds the layout ambiguous, the bounded risk is that a flattened-text extractor could double-count the physician-preference parent and its subreasons; the visually structured source itself supports 58.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields` are not present under their required exact labels in the ledger. The current recheck cannot be carried forward unchanged because it repeats the hierarchy error.

### Required coordinator repair

Preserve C001 and its number. Repair the numeric checker implication, the N018 inventory outcome, the C001 ledger card, the mechanical recheck, any pass-2 summary that relies on the old recheck, and the final report. State the exact parent-child and top-level calculations above. Do not retain the unsupported claim that all ten numbers are peer reasons or that overlap is the unresolved definition. Keep the status `Pending Human Adjudication` and ask the human to confirm the printed hierarchy rather than to locate an unprinted overlap rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Rejected-statement percentage across documents

### Source and calculation audit

[DOC-001 PDF p. 2](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=2) prints 6.4% rejected across all intervention sites. [DOC-003 eTable 3 on PDF p. 6](../../../joi240111supp2_prod_1733431204.76024.pdf#page=6) prints 135 decisions at each of 10 sites and reject counts `15, 23, 5, 25, 9, 25, 12, 11, 11, 6`. Their sum is 142 and the displayed denominator is `10 x 135 = 1,350`, giving `142 / 1,350 x 100 = 10.5185...%`, or 10.5% to one decimal. Keep and adapt totals of 551 and 657 independently reproduce 40.8% and 48.7%. The calculation and cross-document identity are reproducible, and ordinary rounding does not reconcile 6.4% with 10.5%.

### Evidence-card quality

- **Unsupported assumptions:** None in the primary comparison. A unique-template denominator or narrower rejection definition is a permissible alternative, but it is unprinted and must remain an unresolved human question rather than an assumed explanation.
- **Arithmetic:** Correct and reproducible from direct-source counts.
- **Possible duplicate relationship:** Numeric NC-02 and the cross-source checker record concern the same printed percentage, table counts, comparator, and aggregation rule; their pre-ID merge into C002 is supported. No merger with C001 or C003 is supported.
- **Pagination and links:** Both PDF links resolve to the exact pages and end in page anchors.
- **Conclusion impact:** The current bounded statement is appropriate. Do not claim an effect on trial outcomes or paper-level conclusions.
- **Downstream impact boundary:** A systematic-review or data-extraction workflow could copy either 6.4% or the table-implied 10.5% as the intervention-implementation rejection proportion if the discrepancy is confirmed. Do not state that propagation has occurred.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields` are not present under their required exact labels in the ledger. The recheck supplies supportable content for these fields.

### Required coordinator repair

Retain C002 unchanged in identity and category. Build the final card with all exact required labels, copy the direct-source calculations and the unprinted-denominator alternative from the recheck, and keep downstream language conditional and bounded.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eTable 10 effect-measure label

### Source and logical-comparison audit

DOC-003 eTable 10 prints `Difference (95% CI)` above each modeled-effect column on [PDF p. 13](../../../joi240111supp2_prod_1733431204.76024.pdf#page=13), with the table continuing on [PDF p. 14](../../../joi240111supp2_prod_1733431204.76024.pdf#page=14) and [PDF p. 15](../../../joi240111supp2_prod_1733431204.76024.pdf#page=15). DOC-003 eMethods on [PDF p. 22](../../../joi240111supp2_prod_1733431204.76024.pdf#page=22) states that the documentation, any-intervention, and symptom-specific-intervention analyses fit logistic regression models to estimate odds ratios. Values such as 0.53 (0.28, 1.01), 5.30 (2.50, 11.24), and 17.96 (1.03, 313.1) are consistent with the named multiplicative odds-ratio measure. The label-versus-estimand comparison is direct and requires no reconstructed P value, standard error, or model implementation.

### Evidence-card quality

- **Unsupported assumptions:** The candidate does not require an assumption about the per-cell mixed-versus-fixed fallback. The possible interpretation of `Difference` as a generic modeled comparison is source-grounded only as an alternative human question; the source does not define that usage.
- **Arithmetic:** No arithmetic reconstruction is needed. The relevant rule is measure-label identity.
- **Possible duplicate relationship:** S045-S047 all inherit one shared header across three table blocks. They concern the same printed header, methods comparator, and identity rule, so one C003 card is appropriate. No separate candidate should be created for each block.
- **Pagination and links:** The ledger text says pp. 13-15 but links only to `#page=13`, while representative values 5.30 and 17.96 are on p. 14 and the logistic-model footnote is on p. 15. The final card must provide separate truthful links to PDF pp. 13, 14, 15, and 22; it must not describe a page range with only a page-13 anchor.
- **Conclusion impact:** Keep the observation limited to identification of the modeled effect measure. Do not imply that the odds-ratio values or inferential conclusions are numerically wrong.
- **Downstream impact boundary:** If confirmed, a data extractor could misclassify the table's odds ratios as additive differences. Do not claim that such reuse or any conclusion change has occurred.
- **Missing exact final-card fields:** `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields` are not present under their required exact labels in the ledger. The recheck supplies supportable content for them.

### Required coordinator repair

Retain C003 and its category. Add separate p. 13, p. 14, p. 15, and p. 22 links in the final card, preserve the generic-heading alternative, and avoid any claim that the underlying effect estimates are numerically inconsistent.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Coordinator repair register

1. Repair C001 everywhere it is carried forward, without deleting, merging, renumbering, suppressing, or adjudicating it. Replace the 71-versus-58 premise with the source-grounded hierarchy and the exact reconciled calculations.
2. Update `coverage_manifest.md`: enumerate `C001, C002, C003` for `evidence_quality`, mark that row COMPLETE after this artifact is accepted, and later enumerate the same IDs for `report_generation`.
3. Replace the coordinator runtime placeholder in `agent_execution_manifest.md` when the exact runtime ID is available; add the fresh report-generator row after spawning it. Preserve the two distinct Terra/high statistical IDs.
4. Generate every final evidence card with all 13 required bold labels. For every card, use the exact five-line human-adjudication template with `__` in every subfield. No existing candidate mentions a display-zero P value, so do not add the conditional display-zero field unless later wording introduces such a mention and a separate source-grounded contradiction exists.
5. For C003, use one page-specific link each for DOC-003 pp. 13, 14, 15, and 22.
6. Keep C002 and C003 conclusion-impact and downstream-impact language bounded as described above. For C001, do not repeat a participant-flow mismatch that results from double-counting a parent and its children.

## Limitations

The final Markdown/HTML report, token ledger, token summary, after-hash ledgers, finalized run state, report-generator manifest row, and validator result did not yet exist at this mandatory pre-report audit stage and therefore could not be audited here. Those completion artifacts remain coordinator responsibilities. This audit used only supplied package evidence and local derivatives; no web evidence was used.

## Final audit status

- **Covered stable IDs:** C001, C002, C003.
- **Covered source units:** 80/80.
- **Covered numeric relationships:** N001-N080.
- **Covered statistical relationships:** S001-S057 in both distinct passes.
- **Supportable candidate records after evidence-quality review:** C002 and C003 have reproducible source comparisons as framed; C001 remains in the stable set but requires the source-hierarchy repair above before report assembly.
- **Audit result:** COMPLETE WITH REQUIRED COORDINATOR REPAIRS.
