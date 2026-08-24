# Final Evidence-Quality Audit

**Audit stage status:** COMPLETE WITH COORDINATOR REPAIRS REQUIRED  
**Stable candidate set:** C001, C002, C003, C004 (4/4)  
**Candidate status:** Every stable ID remains **Pending Human Adjudication**.

This is a non-adjudicative quality-control audit of the current fresh Workflow 1.5.2 artifacts. It used the three supplied PDFs, the current fresh extraction and relationship artifacts, the two current statistical-pass artifacts, the stable ledger, and the current mechanical recheck. The preserved prior review, old reports, external literature, sibling packages, and the web were not inspected or used. No stable ID was deleted, merged, renumbered, ranked, suppressed, or assigned a scientific disposition.

## Coverage, execution, and integrity audit

### Direct-source inventory and source coverage

The package root contains exactly three direct paper sources, all PDFs. The source inventory identifies 49 unique PDF-page units. Current SHA-256 recalculation matches `source_hashes_before.sha256` for all three sources.

| Source row | Total units | Reusable units | Fresh-required units | Mapped units | Status | Audit result |
|---|---:|---:|---:|---:|---|---|
| DOC-001 — `jama_driver_2018_oi_180054.pdf` | 11 | 0 | 11 | 11 | COMPLETE | Complete; PDF metadata reports 11 pages; current SHA-256 is `684db2edf58f16d1d24e8ddb6a463429b027450314c923e06700acdd0167e7d2`. |
| DOC-002 — `joi180054supp1_prod.pdf` | 25 | 0 | 25 | 25 | COMPLETE | Complete; PDF metadata reports 25 pages; current SHA-256 is `38c1822278c238d2e9f217cd626c307b9d7ad8152f93f3281a03f58990e6108c`. |
| DOC-003 — `joi180054supp2_prod.pdf` | 13 | 0 | 13 | 13 | COMPLETE | Complete; PDF metadata reports 13 pages; current SHA-256 is `b8b7e9731b69407ff10ffc262eb42477965333e3697461e848d8fe50e13b4b31`. |

Result: 3/3 direct-source rows satisfy `fresh-required units = mapped units = total units`, reusable units are zero, and all statuses are `COMPLETE`. The fresh evidence-asset inventory has one page-level usability/OCR decision for each of the 49 pages. Native and layout text were usable; no OCR or GPU use was needed. Rendered result-relevant pages are documented. These records support a fresh source-first chain rather than reuse of old derivatives.

### Coverage-manifest row audit

The current manifest has all 12 required stages and exactly one undecorated relative artifact path in every `Artifact` cell. Ten rows were `COMPLETE` and two were `PLANNED` when this audit began. Candidate-stage scopes for registration and recheck enumerate all four stable IDs. The quality and report scopes require the coordinator repairs listed below.

| Stage / shard | Assigned scope audited | One artifact path | Current-stage audit |
|---|---|---|---|
| `source_inventory` / `source-001` | DOC-001 pp. 1-11; DOC-002 pp. 1-25; DOC-003 pp. 1-13 | Yes | COMPLETE; all 49 source units assigned. |
| `evidence_assets` / `assets-001` | Same 49 source units | Yes | COMPLETE; all units have a fresh asset/decision record. |
| `main_evidence_mapping` / `main-001` | DOC-001 pp. 1-11 | Yes | COMPLETE; 11/11 pages mapped, subject to the two exact wording repairs below. |
| `support_evidence_mapping` / `support-001` | DOC-002 pp. 1-25 and DOC-003 pp. 1-13 | Yes | COMPLETE; 38/38 support pages mapped. |
| `numeric_checks` / `numeric-001` | N001-N047 | Yes | COMPLETE; 47/47 explicit completion records and four discovery records. |
| `statistics_pass_1` / `statistics-001` | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037 | Yes | COMPLETE; 37/37 `PASS_1_COMPLETE` records. |
| `cross_source_checks` / `cross-001` | N001-N047 and S001-S037; 118 direct occurrence comparisons | Yes | COMPLETE; 84/84 relationship records addressed. |
| `candidate_registration` / `candidates-001` | C001, C002, C003, C004 | Yes | COMPLETE; stable set is 4/4. |
| `evidence_recheck` / `recheck-001` | C001, C002, C003, C004 | Yes | COMPLETE; recheck set equals ledger set. |
| `statistics_pass_2` / `statistics-002` | S001-S037 plus C001, C002, C003, C004 and recheck facts | Yes | COMPLETE; 37/37 `PASS_2_COMPLETE` records and 4/4 stable IDs revisited. |
| `evidence_quality` / `quality-001` | Current text says “All stable C IDs” plus all source/coverage rows | Yes | This artifact completes the work, but the manifest scope must explicitly enumerate `C001, C002, C003, C004` and status must be changed to `COMPLETE`. |
| `report_generation` / `report-001` | Current text says “All stable C IDs” plus metadata | Yes | Still legitimately `PLANNED`; before completion, explicitly enumerate `C001, C002, C003, C004`, create the assigned artifact, and change status to `COMPLETE`. |

### Relationship and checker completeness

- The canonical numeric inventory is sequential N001-N047; the numeric checker contains 47/47 explicit `COMPLETE` rows. Four discoveries, NC-01 through NC-04, map without loss to C001 through C004.
- The canonical statistical inventory is sequential S001-S037. Pass 1 contains 37/37 relationship rows with `PASS_1_COMPLETE`; pass 2 independently contains 37/37 relationship rows with `PASS_2_COMPLETE` and revisits all four ledger/recheck records.
- The cross-source checker covers all 47 numeric and 37 statistical relationships and documents 118 occurrence-to-occurrence comparisons after matching population, time, contrast, analysis set, model, measure, scale, unit, reference, and precision.
- No relationship was omitted because of a desired count, queue, top-N rule, or early stopping. The artifacts repeatedly state uncapped complete coverage, and their explicit ID sets support that statement.
- No assigned relationship prints `P = 0`, `p = 0.000`, or an equivalent display zero. Values such as `<.001` are inequalities. None of C001-C004 is based on display-zero reasoning, so no conditional independent-contradiction field is required.

### Agent-execution manifest

The current manifest has 10 distinct agent IDs, each exactly once and with one primary relative artifact path. All current primary artifacts exist after creation of this audit.

| Stage | Agent ID | Model / effort | Start mode | Audit result |
|---|---|---|---|---|
| coordinator | `/root` | `gpt-5.6-sol` / high | CURRENT_SESSION | Current coordinator recorded once. |
| fresh_source_preprocessing | `/root/fresh_preprocessing` | `gpt-5.6-terra` / medium | FRESH_SPAWN | Role allocation and artifact agree. |
| main_evidence_mapping | `/root/main_mapper` | `gpt-5.6-terra` / medium | FRESH_SPAWN | Role allocation and artifact agree. |
| support_evidence_mapping | `/root/support_mapper` | `gpt-5.6-terra` / medium | FRESH_SPAWN | Role allocation and artifact agree. |
| numeric_checks | `/root/numeric_review` | `gpt-5.6-terra` / medium | FRESH_SPAWN | Role allocation and artifact agree. |
| cross_source_checks | `/root/cross_source_review` | `gpt-5.6-terra` / medium | FRESH_SPAWN | Role allocation and artifact agree. |
| statistics_pass_1 | `/root/statistics_pass_1` | `gpt-5.6-terra` / high | FRESH_SPAWN | Fresh statistical pass 1; 37/37 relationships. |
| evidence_recheck | `/root/evidence_recheck` | `gpt-5.6-sol` / high | FRESH_SPAWN | Mechanical recheck covers C001-C004. |
| statistics_pass_2 | `/root/statistics_pass_2` | `gpt-5.6-terra` / high | FRESH_SPAWN | Fresh statistical pass 2; 37/37 relationships and 4/4 rechecks. |
| evidence_quality | `/root/evidence_quality_audit` | `gpt-5.6-sol` / high | FRESH_SPAWN | Current final evidence-quality audit. |

The required Terra/high statistical reviewers are fresh, distinct runtime IDs: `/root/statistics_pass_1` and `/root/statistics_pass_2`. Their files self-identify the same IDs, model, effort, and fresh start, and their assigned S sets are complete. Any later report-generation or repair agent must be appended exactly once to both the execution manifest and the token ledger by the coordinator.

### Identity, links, categories, and tone

- Ledger IDs and recheck IDs are identical: C001, C002, C003, C004. This audit returns the same four headings in the same order.
- Mechanical inspection of all current-run Markdown before this artifact found 312 local link occurrences and no unresolved target. All 311 PDF page-fragment occurrences were within the respective 11-, 25-, or 13-page bounds. Candidate and recheck links resolve from their own artifact directories to the supplied PDFs.
- Candidate pagination was also checked against direct `pdftotext -f/-l -layout` reads of DOC-001 pp. 3, 7, and 9; DOC-002 pp. 9-10; and DOC-003 pp. 2-3 and 10. No false candidate pagination was found.
- Every candidate uses exactly one category from `QUALITY_CONTROL_SCOPE.md`: C001 uses `Statistical reporting inconsistency`; C002 uses `Denominator, proportion, or total inconsistency`; C003 and C004 use `Measure, label, or scale inconsistency`.
- The wording remains neutral and bounded. No candidate claims that a paper-level conclusion changed or that downstream propagation occurred.

## C001 — Reverse-ordered confidence-interval endpoints for all-patient first-attempt duration

- **Status:** Pending Human Adjudication.
- **Category and threshold audit:** `Statistical reporting inconsistency` is the applicable primary category. Exact source values, a reproducible interval-order rule, direct-versus-inferred separation, an alternative interpretation, and an exact human question are all present.
- **Exact evidence and provenance:** [DOC-001 Table 3 — PDF p. 7](../../../jama_driver_2018_oi_180054.pdf#page=7) prints all-patient medians `38 (29 to 51)` and `36 (25 to 54)` seconds, difference `1 (4 to -1)`, and `P=.24`. [DOC-003 eTable 1 — PDF p. 2](../../../joi180054supp2_prod.pdf#page=2) prints `1 s (-1 s to 4 s), P=0.95`; [its note — PDF p. 3](../../../joi180054supp2_prod.pdf#page=3) says inferential columns were recalculated for physician clustering. Provenance aligns across NC-01, cross-source record 1, P1-01, N021/N043, and S007/S030.
- **Mechanical recheck alignment:** The recheck found each cited location and matched both source strings. The rule is applicable: a displayed interval in `L to U` form requires `L <= U`. The direct calculation is `4 > -1`; endpoint order fails. The separately clustered interval is contextual evidence only and is not an unclustered replacement.
- **Direct observation versus inference:** Direct observation is limited to the descending printed sequence and the distinct clustered display. Endpoint transposition or a table-production mechanism is plausible inference, not a source-established correction.
- **Alternative source-grounded interpretation:** An unstated reverse-order convention or source-specific transcription could explain the main display, although other intervals use ascending endpoints. The unclustered analysis output is unavailable.
- **Missing definitions/inputs:** Analysis-specific unclustered Hodges-Lehmann output, original table-production record, individual durations, and any special endpoint-order convention.
- **Duplicate and cross-relationship audit:** C001 is not a duplicate of C004. C001 concerns the order of the two printed CI limits; C004 concerns the outcome's stop event. S007 is the direct inferential relationship and S030 is explicitly model-distinct supporting context.
- **Arithmetic, pagination, and assumption audit:** `4 > -1` is correct, source page 7 is correct, and no ordinary subtraction of group medians is used to challenge the Hodges-Lehmann estimate. No P-value display-zero reasoning is present.
- **Report-card completeness requirement:** The ledger has evidence, category, comparator/rule, calculation, alternatives, and human question, but is not itself a final report card. The final card must add the exact labels `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`, while retaining all existing source/provenance content.
- **Candidate statement required in report:** DOC-001 Table 3 prints the all-patient first-attempt-duration confidence limits in descending order (`4 to -1`); the intended unclustered limits remain unresolved.
- **Quality-control relevance:** A descending interval display can cause a reader or data extractor to reverse, normalize, or copy the limits inconsistently.
- **Potential downstream evidence impact:** If human adjudication confirms a display defect, a systematic-review or meta-analysis extractor could otherwise copy the two confidence limits in the wrong order. No supplied evidence shows that this has occurred or that a conclusion changed.
- **Human verification steps:** Inspect the original unclustered Hodges-Lehmann output and table-production file; identify the intended two limits and their order; document whether the main-table sequence was transposed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Two-patient ETT+stylet denominator difference across linked hypoxemia outcomes

- **Status:** Pending Human Adjudication.
- **Category and threshold audit:** `Denominator, proportion, or total inconsistency` is the applicable primary category. The directly printed denominator difference is reproducible, but the identity rule is conditional; the final card must preserve that condition and must not assert that the two denominators necessarily should be equal.
- **Exact evidence and provenance:** [DOC-001 Table 3 — PDF p. 7](../../../jama_driver_2018_oi_180054.pdf#page=7) prints ETT+stylet first-attempt success without hypoxemia as `282/366 (77%)`. [DOC-001 Table 5 — PDF p. 9](../../../jama_driver_2018_oi_180054.pdf#page=9) prints ETT+stylet hypoxemia as `50/364 (14%)`. Both footnotes use the same hypoxemia threshold/window and state that a valid pulse-oximetry waveform was unavailable for all patients; Bougie uses denominator 371 in both rows. [DOC-002 protocol — PDF p. 9](../../../joi180054supp1_prod.pdf#page=9) defines the composite as first-attempt success plus no hypoxemia. Provenance aligns across NC-02, cross-source record 2, N019/N027/N035, S006/S018, and the pass-2 reconciliation.
- **Mechanical recheck alignment:** The recheck found both locations and reproduced `366 - 364 = 2`, `376 - 366 = 10`, and `376 - 364 = 12`. It correctly states that denominator identity follows only if both rows require observed hypoxemia classification for every denominator member.
- **Direct observation versus inference:** Direct observations are the two ETT+stylet denominators, the same hypoxemia wording, the waveform limitation, and matching Bougie denominators. An unreported exclusion, data-cleaning rule, or deterministic classification is inference.
- **Alternative source-grounded interpretation:** A known first-attempt failure may be classifiable as not achieving the composite even when no valid waveform permits classification of hypoxemia alone. That mechanism could validly make the composite denominator larger. The aggregate sources do not show whether this explains the two patients.
- **Missing definitions/inputs:** Joint patient-level first-attempt-success/hypoxemia/waveform table, the identities and outcome states of the two patients, implemented denominator-construction code or rule, and outcome-specific data-recovery records.
- **Duplicate and cross-relationship audit:** C002 is not a duplicate of C003. C002 concerns who enters two denominators; C003 concerns the end event defining the hypoxemia observation window. The relationships can share hypoxemia evidence without sharing the same comparator or rule.
- **Arithmetic, pagination, and assumption audit:** All three subtractions are correct and pages 7, 9, and protocol page 9 are correct. The current ledger and recheck avoid the unsupported assumption that hypoxemia and success-without-hypoxemia are simple complements. The final report must retain the conditional rule and must not propose a corrected denominator or rate.
- **Report-card completeness requirement:** The ledger supplies category, exact evidence, a conditional rule, calculation, alternatives, and human question, but the final card must add the exact labels `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The alternative deterministic-classification explanation is mandatory context.
- **Candidate statement required in report:** The ETT+stylet denominators differ by two across linked waveform-dependent outcomes (`366` versus `364`), and the supplied aggregate sources do not establish whether the difference is intentional under an outcome-specific denominator rule.
- **Quality-control relevance:** Without a stated construction rule, a reader cannot reproduce which ETT+stylet patients contribute to each displayed percentage.
- **Potential downstream evidence impact:** If human adjudication identifies a denominator-label or documentation defect, an outcome extractor could otherwise copy a percentage without the correct analysis denominator. No supplied evidence shows propagation or conclusion change.
- **Human verification steps:** Reconcile patient IDs across first-attempt success, waveform availability, and hypoxemia; inspect the analysis code and missing-data log; determine whether the two extra composite-denominator patients were deterministically classifiable failures; document the applicable rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Protocol and published hypoxemia observation windows use different endpoint events

- **Status:** Pending Human Adjudication.
- **Category and threshold audit:** `Measure, label, or scale inconsistency` is the applicable primary category. The candidate compares the same named hypoxemia threshold/window across supplied protocol and published sources and isolates the nonidentical end events.
- **Exact evidence and provenance:** [DOC-002 protocol — PDF p. 9](../../../joi180054supp1_prod.pdf#page=9) states that hypoxemia recording ends one minute after ETT-cuff inflation; [measurement procedure — PDF p. 10](../../../joi180054supp1_prod.pdf#page=10) repeats the cuff-inflation endpoint. [DOC-001 Table 3 — PDF p. 7](../../../jama_driver_2018_oi_180054.pdf#page=7), [DOC-001 Table 5 — PDF p. 9](../../../jama_driver_2018_oi_180054.pdf#page=9), and [DOC-003 eTable note — PDF p. 3](../../../joi180054supp2_prod.pdf#page=3) use one minute after completion of the intubation attempt. [DOC-003 data form — PDF p. 10](../../../joi180054supp2_prod.pdf#page=10) says attempt 1 ends when the blade is removed. Provenance aligns across NC-03, cross-source record 3, N035, S033/S034, and both later checks.
- **Mechanical recheck alignment:** Threshold and starting event match. The logical comparison is `one minute after ETT-cuff inflation` versus `one minute after attempt completion/blade removal`. No source-supplied identity equates those named events.
- **Direct observation versus inference:** The two end-event descriptions are direct. A protocol amendment, editorial shorthand, synchronization in practice, or operational equivalence is inferred as possible and is not supplied.
- **Alternative source-grounded interpretation:** “Attempt completion” could be shorthand for cuff inflation, or the events could occur close together. The data form's explicit blade-removal end definition prevents assuming equivalence from the supplied package alone.
- **Missing definitions/inputs:** Implemented surveillance-stop timestamp, patient-level cuff-inflation/blade-removal times, protocol amendment or analysis-plan revision, and any operational instruction equating the events.
- **Duplicate and cross-relationship audit:** C003 is distinct from C004. C003 changes the event eligibility window for a binary hypoxemia outcome; C004 changes the stop timestamp of a duration measure. The two candidates may share documentation but not comparator, measure, or possible extracted field.
- **Arithmetic, pagination, and assumption audit:** No arithmetic is applicable. PDF pages 9-10, 7, 9, 3, and 10 were directly located. The current wording appropriately avoids asserting that different wording changed any observed event count or rate.
- **Report-card completeness requirement:** The ledger supplies category, source statements, rule, alternatives, and human question, but the final card must add the exact labels `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. Protocol-planned versus implemented-result status must remain explicit.
- **Candidate statement required in report:** The protocol ends hypoxemia surveillance one minute after ETT-cuff inflation, while the published materials end it one minute after intubation-attempt completion; the supplied package does not document whether those events were treated as equivalent or whether the definition changed.
- **Quality-control relevance:** The named stop event determines which desaturation observations are eligible for the outcome and therefore should be traceable across protocol and results reporting.
- **Potential downstream evidence impact:** If human adjudication confirms a definition change or labeling defect, a review or guideline extractor could otherwise record the published hypoxemia result under the protocol's different observation window. No supplied evidence establishes actual propagation or a changed conclusion.
- **Human verification steps:** Inspect the implemented case-report timing instructions, amendment history, analysis specification, and timestamp logic; identify the surveillance-stop event used in the analyzed data; document any approved change or equivalence rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Protocol and published first-attempt-duration measures use different endpoint events

- **Status:** Pending Human Adjudication.
- **Category and threshold audit:** `Measure, label, or scale inconsistency` is the applicable primary category. Exact planned and published definitions are available, the start events are compatible, and the stop events are nonidentical.
- **Exact evidence and provenance:** [DOC-002 protocol — PDF p. 9](../../../joi180054supp1_prod.pdf#page=9) defines first-attempt time to intubation from attempt start through ETT-cuff inflation with the tube in the trachea. [DOC-001 outcome methods — PDF p. 3](../../../jama_driver_2018_oi_180054.pdf#page=3) and [DOC-001 Table 3 — PDF p. 7](../../../jama_driver_2018_oi_180054.pdf#page=7) define and report blade-entry-to-blade-removal duration, including all-patient medians `38` versus `36` seconds. [DOC-003 eTable note — PDF p. 3](../../../joi180054supp2_prod.pdf#page=3) and [data form — PDF p. 10](../../../joi180054supp2_prod.pdf#page=10) repeat the blade-removal endpoint. Provenance aligns across NC-04, cross-source record 4, N036, S005/S007/S023/S027/S030, and both later checks.
- **Mechanical recheck alignment:** With blade insertion as a compatible start, the planned endpoint is cuff inflation and the published endpoint is blade removal. Their patient-level difference would be `time(blade removal) - time(cuff inflation)`, but no source supplies both timestamps, so no numerical effect is assigned.
- **Direct observation versus inference:** The planned and published definitions and reported summaries are direct. An intended measurement change, harmonized timing instruction, amendment, or accommodation of failed attempts is inferred as possible but not documented.
- **Alternative source-grounded interpretation:** The published blade-removal measure may deliberately assign a duration to failed attempts, whereas protocol time to cuff inflation naturally describes successful tracheal placement. Repetition across the article, supplement, and form supports deliberate use of the published operational measure but does not document its relationship to the protocol outcome.
- **Missing definitions/inputs:** Patient-level cuff-inflation and blade-removal timestamps, stopwatch stop instruction, revised plan/amendment, and handling of a failed first attempt that never reaches cuff inflation.
- **Duplicate and cross-relationship audit:** C004 is not a duplicate of C001 or C003. It addresses the duration scale; C001 addresses one interval's endpoint order; C003 addresses the hypoxemia observation window. Shared source rows and timing terminology do not make the consistency rules identical.
- **Arithmetic, pagination, and assumption audit:** The symbolic timing relationship is correct, no unsupported numerical difference is calculated, and source pages 9, 3, 7, 3, and 10 are correct. The current wording does not assert that the published medians, interval, or P value are numerically wrong.
- **Report-card completeness requirement:** The ledger supplies category, exact definitions, comparison rule, alternatives, and human question, but the final card must add the exact labels `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. Planned-versus-implemented scope and failed-attempt handling must remain explicit.
- **Candidate statement required in report:** The protocol defines first-attempt time to intubation through ETT-cuff inflation, whereas the published analyses use blade removal; the supplied package does not document how or why the measurement endpoint changed.
- **Quality-control relevance:** The stop event defines the reported time scale and affects whether failed attempts have a measurable duration under the same rule.
- **Potential downstream evidence impact:** If human adjudication confirms a definition or labeling defect, a meta-analysis or outcome extractor could otherwise treat the protocol and published duration as the same measure. No supplied evidence shows actual propagation or conclusion change.
- **Human verification steps:** Inspect the protocol/amendment history, stopwatch/data-collection instructions, analysis code, and available timestamp fields; determine which stop event generated each published duration analysis and how failed attempts were handled.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Coordinator repair register

The following repairs are exact and supportable from current fresh artifacts. They do not change the stable candidate set.

1. In `extraction/main_quantitative_evidence.md`, provisional relationship MN014 currently says the Table 2 operator and laryngoscope categories “sum to full arms.” Repair it to state that Bougie operator counts sum to 383 (`318 + 57 + 8`) because the Table 2 footnote records physician changes, while the ETT+stylet operator counts sum to 376 and the laryngoscope categories sum to 381 and 376. The numeric checker already carries the correct distinction.
2. In `extraction/main_quantitative_evidence.md`, provisional relationship MN027 currently says the Table 5 hypoxemia denominators “match” the Table 3 all-patient success-without-hypoxemia denominators. Repair it to state that Bougie matches at 371, while ETT+stylet differs (`364` versus `366`) and is the denominator relationship carried into C002.
3. In `coverage_manifest.md`, replace “All stable C IDs” in the `evidence_quality` exact scope with `C001, C002, C003, C004`, then mark that row `COMPLETE` after this artifact is durable.
4. Before final completion, replace “All stable C IDs” in the `report_generation` exact scope with `C001, C002, C003, C004`, create its one assigned artifact, and mark the row `COMPLETE`.
5. The report generator must emit all four cards with every exact field required by `report_spec.md`, the exact five `__` adjudication placeholders, neutral candidate wording, and the bounded downstream statements above. Where C003 uses evidence from both protocol pages 9 and 10, provide separate page-anchored links in the final card.
6. Append any report-generation or later repair agent to `agent_execution_manifest.md` exactly once and include it in token accounting. The present 10-row manifest is complete for the agents active through this audit.

## Audit limitations

- Individual-level trial data, analysis code, row-specific interval/test algorithms, continuous-outcome analysis output, denominator-construction logic, cluster-model details, protocol amendments, and event timestamps are not supplied. These absences remain human questions and were not filled by convention.
- Figure curves were audited through printed captions, risk sets, effect estimates, and model labels; no curve-coordinate digitization was required for the registered candidates.
- The final Markdown/HTML report, finalized run-state fields, post-review hashes, token ledger/summary, and validator result did not yet exist when this stage began. They remain coordinator/report-generation tasks and cannot be certified by this artifact in advance.

## Completion statement

Current evidence-quality coverage is complete for all 3 source rows, all 12 current coverage rows, all 10 currently manifested agents, N001-N047, both 37/37 statistical passes, and C001-C004. Ledger, recheck, and quality-audit ID sets are identical. Four stable candidates remain **Pending Human Adjudication**. Six bounded coordinator actions are listed above; no candidate suppression, renumbering, scientific disposition, or replacement value is recommended.
