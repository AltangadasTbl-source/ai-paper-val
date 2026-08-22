# Evidence Quality Audit

## Audit status and boundaries

This source-local quality-control audit covers every stable candidate (`C001`, `C002`, and `C003`), every row of `coverage_manifest.md`, all four direct-source rows in `source_coverage.md`, the complete numeric and statistical relationship inventories, the numeric and cross-source checker outputs, both statistical-pass outputs, `candidate_ledger.md`, `verification/evidence_recheck.md`, and `agent_execution_manifest.md`. It used only the supplied package and current Workflow 1.5.1 artifacts. It did not use the web or any legacy candidate, verifier, critic, queue, endetail, quality, or report artifact as scientific evidence.

Scientific source coverage is complete. The four direct PDFs contain 63 pages: 20 reusable-backed pages plus 43 fresh-required pages equals 63 total pages, and 63 mapped pages equals 63 total pages. The source rows close independently as follows: DOC-001, `10 + 0 = 10`, mapped `10`; DOC-002, `0 + 42 = 42`, mapped `42`; DOC-003, `10 + 0 = 10`, mapped `10`; DOC-004, `0 + 1 = 1`, mapped `1`. All four rows use `PDF_PAGE` and `COMPLETE`. The complete mapper union covers DOC-001 PDF pages 1-10, DOC-002 PDF pages 1-42, DOC-003 PDF pages 1-10, and DOC-004 PDF page 1. Explicit no-applicable records close contents, bibliography, administrative, and data-availability pages without converting those units into findings.

All 94 designated reusable-artifact hashes and all four direct-source hashes reproduce against the current files. The direct PDFs have the page counts recorded in the source inventory: 10, 42, 10, and 1. The candidate PDF links resolve to existing files and use truthful direct-PDF pagination within those bounds. Direct page extraction reproduced the cited Table 5 values on DOC-001 page 9, the HbA1c labels on DOC-001 pages 1, 7, and 8 and DOC-003 page 9, and the recruitment values on DOC-002 pages 7, 17, and 21.

The coverage manifest has one plain relative artifact path in every row and disjoint shard identifiers. Every artifact for a completed stage exists, including all mapper parts, merged inventories, checker outputs, candidate ledger, and evidence recheck. This audit supplies the previously in-progress `quality/evidence_quality_audit.md` path. The `report_generation` row is correctly downstream of this audit and was still pending at audit time; its single assigned path is `../final_report_1_5_1.md`. The coordinator must mark the quality row `COMPLETE` after this file is present and must replace the report row's pending scope/status with the explicit full set `C001, C002, C003` and `COMPLETE` only after the report artifact exists.

Discovery was not controlled by a top-N boundary, an old candidate list, a target count, or early stopping. The manifest and checkers cover all 60 numeric relationships (`N001`-`N060`), all 48 statistical relationships (`S001`-`S048`), and all 108 relationships in the cross-source lane. The three distinct numeric leads were registered as C001-C003; the two cross-source leads and one statistical lead are provenance for those same source/rule relationships rather than unregistered additional candidates. No stable candidate was deleted, merged, ranked, suppressed, renumbered, adjudicated, or assigned severity or validity.

Both statistical reviews are complete for all 48 S relationships. Their execution-manifest rows identify distinct fresh agents, `/root/statistics_pass_1` and `/root/statistics_pass_2`, each with model `gpt-5.6-terra`, reasoning effort `high`, start mode `FRESH_SPAWN`, and one checker artifact. Pass 2 also reconciles C001, C002, and C003 against the complete ledger and mechanical recheck. During this audit, the coordinator repaired the stale `PENDING` cells in `statistics/relationship_inventory.md`; all 48 rows now state `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. This repair changed metadata only and did not change any relationship or candidate identity.

No assigned statistical relationship displays `P = 0`, `p = 0.000`, or an equivalent display zero. The nonzero displays `P < .001` and `P = .0002` were not treated as display zeros. None of C001-C003 has a display-zero P value as its basis or mentions one, so no conditional independent-contradiction field is applicable.

The ledger and recheck ID sets are identical: C001, C002, and C003. Each recheck includes the cited-location check, source and comparator transcription, applicable rule, reproduced calculation or logical comparison, available and missing inputs, source-grounded alternative, direct-observation/inference separation, and exact remaining human question. Each category is one exact category allowed by `QUALITY_CONTROL_SCOPE.md`, and every candidate remains `Pending Human Adjudication`.

## C001 — Table 5 absolute difference does not reproduce from the displayed counts

- **Identity and category audit:** C001 appears once in the ledger and once in the recheck with the same title and source relationship. Its category, `Numeric or arithmetic inconsistency`, is an exact primary category. Its status remains `Pending Human Adjudication`.
- **Evidence and pagination audit:** DOC-001 PDF page 9 directly prints, in both the total-cholesterol and LDL rows, `9 (14.1)` under the `n = 64` group, `6 (9.7)` under the `n = 62` group, and `4.3 (-8 to 17.2)` under `Absolute Unadjusted Difference Between Groups, % (95% CI)`. The linked PDF exists and has 10 pages. The ledger and recheck links point truthfully to PDF page 9.
- **Arithmetic audit:** `9 / 64 = 14.0625%`, which displays as `14.1%`; `6 / 62 = 9.677419%`, which displays as `9.7%`; and `(9 / 64 - 6 / 62) x 100 = 4.3850806` percentage points, which displays as `4.4` under nearest one-decimal rounding. The printed percentages independently give `14.1 - 9.7 = 4.4`. The difference between `4.3850806` and the printed `4.3` is approximately `0.0851` percentage point, exceeding a half-unit one-decimal rounding tolerance of `0.05`.
- **Assumption and alternative audit:** The candidate does not claim that nearest rounding or the raw estimator is definitively the production rule. The recheck explicitly names truncation, row-specific denominators, another estimator, and unprinted analysis-population inputs as unresolved alternatives. The source labels the result unadjusted but does not supply the point-estimator or rounding rule. The candidate therefore frames a reproducible printed-value mismatch and an exact human question rather than a final correction.
- **Duplicate audit:** The total-cholesterol and LDL rows repeat the same counts, percentages, point estimate, interval, comparator, and rule. Treating those linked occurrences as one pre-ID relationship is supported and does not hide a distinct comparator. No other stable candidate duplicates this relationship.
- **Evidence-card field audit:** The ledger and recheck together support the candidate statement, exact locations, source evidence, reported-versus-comparator values, reasoning procedure, calculation, alternatives, mechanical recheck, quality-control relevance, bounded downstream impact, and human verification question. The final report must preserve the conditional wording and must not convert `4.4` into an AI-prescribed correction. No unsupported evidence field is required.
- **Impact and tone audit:** The bounded risk is that a table or evidence extractor could copy an absolute difference that does not reproduce under the displayed raw-proportion rule. There is no claim that this small display discrepancy changes the paper-level conclusion or has already propagated downstream.
- **Audit result:** Complete and supportable as a neutral quality-control candidate. No arithmetic, pagination, category, identity, or evidence repair is required.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — HbA1c interaction is labelled with a concentration unit while matched displays use percent

- **Identity and category audit:** C002 appears once in the ledger and once in the recheck with the same relationship. Its category, `Measure, label, or scale inconsistency`, is an exact primary category. Its status remains `Pending Human Adjudication`.
- **Evidence and pagination audit:** DOC-001 PDF pages 1 and 7 directly repeat the HbA1c treatment-by-time estimate `-0.0002 mg/dL` with the interval `-0.0021 to 0.0016`; page 7 also describes the result as a daily rate. DOC-001 page 8 labels the Table 4 measure `HbA1c, %`. DOC-003 page 9 labels eFigure 8 `HbA1c (%)` and displays randomized-group mixed-model estimated least-square means over days. Both source PDFs exist, their cited pages are within the recorded page counts, and all four links use truthful PDF pagination.
- **Label and model audit:** The exact coefficient and interval agree across DOC-001 pages 1 and 7; the mismatch is the unit label, not the numeric repetition. The percent-scale table and matched longitudinal eFigure support the comparator. No supplied source defines a transformation or a separate concentration-scale HbA1c variable. A numeric conversion is therefore neither available nor asserted.
- **Assumption and alternative audit:** The candidate does not infer a replacement unit as a scientific fact. It preserves two source-grounded possibilities: a production-label carryover or a distinct transformed analysis whose definition is absent. The exact human question asks which possibility applies and requests the missing transformation/unit if applicable.
- **Duplicate audit:** N016, S008, S012, S047, the cross-source Lead A, and statistical-pass Lead L1 are provenance for the same outcome, matched labels, and consistency rule. Their consolidation into C002 occurred before the stable ID and does not suppress a distinct numeric, interval, P-value, or model-result contradiction. Pass 2 found no separate additional contradiction.
- **Evidence-card field audit:** The ledger and recheck together support every required final-card content field. The report generator must state that the calculation is a label comparison and that no conversion is supportable; it must not invent a percentage-point-per-day correction. Human verification should inspect the analysis-variable definition and production source while preserving the printed estimate, interval, population, and model unless human review establishes otherwise.
- **Impact and tone audit:** The bounded risk is misclassification of the HbA1c measure or effect scale during data extraction. The record does not assert that the model result, inference, clinical conclusion, or paper-level conclusion is wrong.
- **Audit result:** Complete and supportable as a neutral quality-control candidate. No pagination, category, identity, label-comparison, or evidence repair is required.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Protocol recruitment target conflicts between 82 and 98 participants per site

- **Identity and category audit:** C003 appears once in the ledger and once in the recheck with the same relationship. Its category, `Denominator, proportion, or total inconsistency`, is an exact primary category. Its status remains `Pending Human Adjudication`.
- **Evidence and pagination audit:** DOC-002 page 7 directly prints `Acute Phase (N=392)` and states enrollment across four sites. DOC-002 page 17 states that each of the four sites will recruit 98 acutely ill participants and randomize 44 remitted participants. DOC-002 page 21 states that the proposed multicentered study has four research sites, each recruiting 82 patients with the stated psychotic-depression population. The PDF exists and has 42 pages; all three linked pages are truthful and within bounds.
- **Arithmetic audit:** `98 x 4 = 392`, reproducing the page 7 total. `82 x 4 = 328`, which is 64 below 392. The per-site statements differ by `98 - 82 = 16`. The separate `44 x 4 = 176` randomization total agrees with the planned randomized total and does not resolve the acute-recruitment discrepancy.
- **Assumption and alternative audit:** Applicability is explicitly conditional on the three statements referring to the same planned acute recruitment population. The source does not label page 21 as a different phase, subset, time period, or protocol version. The recheck nevertheless retains an earlier target, an amendment, or a distinct human-subjects subset as alternatives and asks the human reviewer to establish the population/version distinction. The candidate does not compare the prospective target with later observed enrollment as though they were the same quantity.
- **Duplicate audit:** N044 and cross-source Lead B concern the same three printed recruitment values and the same four-site identity. They correctly support one stable candidate. N026, N027, N029, N042, S011, and planning/power relationships are context or arithmetic provenance and are not suppressed candidates with a different comparator.
- **Evidence-card field audit:** The ledger and recheck together support every required final-card content field. The final card should ask for protocol/version and population verification and must not prescribe either 82 or 98 as the correct value. The bounded evidence question is whether a definition or version distinction resolves the printed totals.
- **Impact and tone audit:** The bounded risk is inconsistent extraction of a planned recruitment denominator or per-site target. The candidate does not imply a defect in observed participant flow, the final randomized analysis, or the paper-level conclusion.
- **Audit result:** Complete and supportable as a neutral quality-control candidate. No arithmetic, pagination, category, identity, or evidence repair is required.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Repairs and remaining limitations

One supportable upstream omission was repaired through the coordinator: the 48 statistical-inventory rows now record the already-established pass statuses instead of stale `PENDING` cells. No candidate content, relationship identity, source evidence, calculation, category, or stable ID changed.

Two workflow-finalization actions remain outside this audit artifact: mark the `evidence_quality` coverage row complete after this file is present, and complete the downstream report-generation row only after a report containing C001, C002, and C003 exists. The report generator must use all exact report-card labels, retain the bounded alternatives and questions above, and use `__` for each Validity, Importance, Action, Initials, and Notes subfield. These are stage-order actions, not scientific-coverage gaps.

Source limitations remain bounded to definitions absent from the supplied package: C001 lacks the exact point-estimator/rounding convention or row-specific denominator definition; C002 lacks the intended coefficient unit or any transformed HbA1c definition; and C003 lacks a version, phase, time, or subset distinction for the two per-site recruitment targets. The statistical inventories also record absent SEs, test statistics, model-variance details, band definitions, and simulation inputs where applicable. These omissions constrain explanation or deeper reconstruction but do not prevent reproduction of the three registered comparisons.

Final audit ID set: C001, C002, C003. Candidate repairs required: 0. Metadata repairs completed: 1. Scientific source-coverage gaps: 0. Stable-ID suppression, adjudication, ranking, or severity assignment: 0.
