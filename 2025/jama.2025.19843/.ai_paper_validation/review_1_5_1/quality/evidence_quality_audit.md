# Final Evidence-Quality Audit

## Final status and scope

- **Audit result:** PASS_READY.
- **Stable candidate scope:** C001 (1/1).
- **Coverage-manifest scope:** all 19 current data rows.
- **Direct-source scope:** DOC-001 through DOC-006, all 194 PDF pages.
- **Numeric scope:** N001 through N052 (52/52).
- **Statistical scope:** S001 through S024 (24/24) under the corrected canonical meanings.
- **Prior repair scope:** all seven items in `quality/evidence_quality_audit.md`.
- **Candidate disposition:** none assigned. C001 remains **Pending Human Adjudication**.

This audit used only the supplied package, current Workflow 1.5.1 artifacts, and direct local source files. No web source was used. The retained original checker files document the superseded ID drift; the corrective pass and cross-source artifacts provide the canonical completion records. No old candidate list, top-N rule, or 10-candidate boundary controlled discovery.

## Source, coverage, and integrity audit

The direct-source inventory contains six PDFs. Independent `pdfinfo` checks confirmed page counts of 10, 153, 9, 18, 3, and 1, totaling 194. Every direct-source row closes:

| Source ID | Total | Reusable | Fresh-required | Reusable + fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---:|---|
| DOC-001 | 10 | 10 | 0 | 10 | 10 | COMPLETE |
| DOC-002 | 153 | 0 | 153 | 153 | 153 | COMPLETE |
| DOC-003 | 9 | 0 | 9 | 9 | 9 | COMPLETE |
| DOC-004 | 18 | 18 | 0 | 18 | 18 | COMPLETE |
| DOC-005 | 3 | 0 | 3 | 3 | 3 | COMPLETE |
| DOC-006 | 1 | 0 | 1 | 1 | 1 | COMPLETE |
| **Total** | **194** | **28** | **166** | **194** | **194** | **COMPLETE** |

The main map explicitly covers DOC-001 pp. 1-10. The support map explicitly partitions DOC-002 pp. 1-47, 48-93, 94-139, and 140-153; covers DOC-003 pp. 1-9 and DOC-004 pp. 1-18; and records every DOC-005 and DOC-006 page as an inspected no-applicable-result unit. `source_coverage.md` now correctly defines mapped units as completed direct-source scientific mapping.

All six direct-source SHA-256 checks pass against `source_hashes_before.sha256`. All 58 reused-artifact SHA-256 checks pass against `reused_artifact_hashes_before.sha256`. No source or reused evidence asset changed.

The current `coverage_manifest.md` has 19 data rows. Every Artifact cell contains exactly one undecorated relative path. Every assigned source, numeric, and statistical unit is complete. The candidate-registration, evidence-recheck, evidence-quality, and report scopes each explicitly enumerate C001 rather than using a range. The quality row still records the completed first audit as `REPAIR_REQUIRED`, and the report row remains `NOT_STARTED`; after accepting this final audit, the coordinator should point or add the final quality row to `quality/evidence_quality_audit_final.md` with exact scope `C001` and status `COMPLETE`, then mark report generation complete only after the complete Markdown report exists. These are downstream manifest-state transitions, not unresolved scientific-coverage defects.

## Quantitative and statistical relationship audit

The canonical numeric inventory contains one row for every N001-N052 relationship, and the numeric checker contains one explicit `CHECKED_NO_CANDIDATE` outcome for every one of those 52 IDs. Rechecked arithmetic includes participant-flow sums, group and subgroup totals, available-case denominators, displayed percentages and percentage-point differences, event-frequency distributions, matched table/figure counts, units, measure labels, and risk-versus-count distinctions. Calculations are reproducible at the printed precision. Model-derived bootstrap intervals, hazard ratios, and curve coordinates were not overclaimed as independently regenerated from unavailable aggregate inputs.

The canonical statistical inventory contains one row for every S001-S024 relationship. Corrective pass 1 and corrective pass 2 each contain one explicit completion row for all 24 canonical IDs. The corrected cross-source artifact covers the disjoint union N001-N052 and S001-S024. The repaired support meanings are preserved exactly:

| Stable ID | Canonical meaning | Final audit result |
|---|---|---|
| S021 | DOC-004 p. 11 mortality figure: D30 log-rank P=.47 and D60 log-rank P=.56. | Complete; D60 retains the existing C001 implication against prose P=.78. |
| S022 | DOC-004 p. 13 MACE figure: D30 log-rank P=.87 and D60 log-rank P=.94, with terminal counts aligned to eTable 3. | Complete; no candidate. |
| S023 | DOC-004 p. 16 ICU/hospital RMST display: ICU 17.5 vs 19 days and hospital 28 vs 35 days. | Complete; the main ICU value 18 is compatible with whole-day display precision. |
| S024 | DOC-004 p. 18 supplement subgroup Fine-Gray sHR/CI occurrence. | Complete; explicitly retained as separate source-occurrence tracking cross-referenced to main S013, not a second analysis. |

The current execution manifest contains the coordinator and all 13 specialist or repair agents used through this final audit exactly once. It records two distinct fresh statistical agents, `/root/statistics_pass_1` and `/root/statistics_pass_2`, each as `gpt-5.6-terra`, high reasoning effort, `FRESH_SPAWN`, with unique original pass artifacts. The later corrective statistical agents are also distinct fresh Terra/high agents and have unique repair artifacts. No medium-effort agent or follow-up effort change substitutes for either required pass.

All inspected Markdown evidence targets in the numeric checker, corrected statistical passes, corrected cross-source checker, candidate ledger, and evidence recheck resolve locally. Every PDF target uses an in-range `#page=N` fragment. The repaired cross-source row now splits main methods p. 3 and main Results p. 4 into separate exact links. S013/S024 duplicate-source tracking is explicit. No false pagination remains: the former DOC-002 `1805-1935` notation is now identified as fresh layout-extraction line numbers, while DOC-002 p. 37 is the direct PDF location.

## C001 — Conflicting printed P values for the matched day-60 mortality result

- **Status:** Pending Human Adjudication.
- **Category:** `Cross-document numeric inconsistency`, an allowed primary category in `QUALITY_CONTROL_SCOPE.md`.
- **Checker provenance:** Statistical pass 1 proposal SP1-01; numeric and cross-source context is retained without a duplicate stable candidate.
- **Stable relationships:** S008 and S021; N025 and N047.
- **Cited locations found:** Yes. The abstract is at [DOC-001 p. 1](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1), the relevant methods at [DOC-001 p. 3](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3), the Results sentence and supplement cross-reference at [DOC-001 p. 4](../../../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4), the planned mortality analysis at [DOC-003 p. 7](../../../joi250087supp2_prod_1766516490.96511.pdf#page=7), and eFigure 2 at [DOC-004 p. 11](../../../joi250087supp3_prod_1766516490.97011.pdf#page=11).
- **Printed values matched:** DOC-001 reports 28/101 (27.7%) versus 26/104 (25.0%), risk difference 2.7 percentage points (95% CI, -9.0 to 15.3), and `P=.78`. DOC-004 eFigure 2 displays the same day-60 terminal deaths and `p=0.56, Log-rank`.
- **Arithmetic reproduced:** `28/101 = 27.72%`, `26/104 = 25.00%`, and their difference is 2.72 percentage points, which rounds to 2.7. The printed P values differ by .22 and cannot be two rounded displays of one underlying value.
- **Rule applicability:** Conditional. If both P values report the same planned day-60 mortality comparison, they should agree. The prose does not name the procedure behind `.78`, so a distinct fixed-time or other analysis remains a source-grounded alternative.
- **Unsupported assumptions excluded:** Neither the ledger nor the recheck claims that `.78` is proved to be log-rank, reconstructs a P value from the RR interval, or claims that the paper-level conclusion is wrong.
- **Possible duplicate:** None. Pass 2 preserves C001 as the existing implication and emits no duplicate candidate.
- **Quality-control relevance:** The same endpoint, time point, randomized groups, counts, and direct supplement reference carry different printed P values without a definition that reconciles them.
- **Potential downstream evidence impact:** If human review confirms a reporting mismatch, an extractor could copy a different P value depending on whether the prose or supplement figure is used. This is a bounded possibility, not a claim that propagation or conclusion change occurred.
- **Human verification steps:** Identify the exact test/model, estimand, analysis population, adjustment, and censoring rule that generated `.78`; compare those definitions with the labelled eFigure 2 log-rank analysis and the prespecified mortality method; then determine whether the two displays are intentionally distinct or whether one requires correction.
- **Exact remaining human question:** Does `.78` represent a different prespecified analysis, and if so which exact test/model, estimand, analysis population, adjustment, and time-to-event/censoring rule produced it; or is either displayed P value erroneous?
- **Display-zero exclusion:** C001 compares `.78` and `.56`; neither is a display zero. The exclusion is not implicated, and no conditional display-zero report field is required.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

All required human-adjudication subfields use the exact blank placeholder `__`. No severity, validity judgment, scientific disposition, ranking, deletion, merger, suppression, or renumbering is assigned.

## Seven-item repair verification

| Prior repair item | Verification |
|---|---|
| 1. Statistical pass 1 canonical IDs | COMPLETE. The corrective pass explicitly checks canonical S021 mortality, S022 MACE, S023 RMST, and S024 subgroup occurrence, with S021 linked to the existing S008/C001 implication. |
| 2. Statistical pass 2 canonical IDs | COMPLETE. The independent corrective pass covers S001-S024 and C001 with the same canonical alignment and complete recheck facts. |
| 3. Cross-source canonical IDs | COMPLETE. S020 is method/measure definition, S021 mortality, S022 MACE, S023 RMST, and S024 subgroup occurrence cross-referenced to S013; the full N/S union is covered. |
| 4. False source location | COMPLETE. UN006 now cites DOC-002 p. 37 and labels 1805-1935 only as layout-extraction lines. |
| 5. Source-coverage semantics | COMPLETE. `Mapped units` now means completed direct-source scientific mapping and closes 194/194. |
| 6. Coverage-manifest candidate scope | SUBSTANTIVELY COMPLETE. C001 is explicitly enumerated in evidence-quality and report-generation scope. The coordinator must perform the expected post-acceptance status/path transition for this final audit and later report completion. |
| 7. Link labels and duplicate tracking | COMPLETE. The last noncontiguous p. 3/p. 4 label was split into exact links; S013 and S024 are explicitly separate source occurrences of one matched result family. |

## ID-set and final gates

- Candidate ledger ID set: `{C001}`.
- Evidence-recheck ID set: `{C001}`.
- First quality-audit ID set: `{C001}`.
- Final quality-audit ID set: `{C001}`.
- The existing candidate, recheck, and quality artifacts therefore have identical stable-ID sets.
- The final report does not yet exist and must contain exactly `{C001}` with the blank human-adjudication fields above.
- Report generation, token accounting, final hash recomputation, HTML rendering, and validator execution remain later coordinator stages and are outside this final evidence-audit artifact.

## Limitations

The supplied package does not identify the test/model that generated prose `P=.78`, and it does not include individual event and censoring times sufficient to regenerate the log-rank result. Some model-derived intervals and curve coordinates likewise cannot be independently recomputed from aggregate pages. The checkers appropriately limit those records to supported arithmetic, interval ordering, direction, label, precision, and matched-location checks. These limitations preserve C001's exact human question but do not leave a source unit or canonical N/S relationship unmapped.

**Final evidence-quality conclusion:** PASS_READY. No supportable evidence-card omission, incorrect arithmetic, false pagination, duplicate candidate, unsupported analytic assumption, unbounded downstream-impact claim, category defect, display-zero violation, or unresolved scientific-coverage defect remains.
