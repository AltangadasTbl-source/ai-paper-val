# Evidence-Quality Audit

This final source-first quality audit covers all five stable candidates, all 16 coverage-manifest rows, all three source-coverage rows, all 59 numeric relationships, all 51 statistical relationships, both statistical passes, the complete execution manifest, and the DOC-002 page 37 mapping repair. The review remains a neutral quantitative quality-control exercise. Every candidate remains **Pending Human Adjudication**.

## Coverage assessment

- **Direct-source coverage:** 3 of 3 direct PDFs; 81 of 81 stable PDF-page units. Every source row has `Reusable units = 0`, `Fresh-required units = Total units`, `Mapped units = Total units`, and `Status = COMPLETE`. Totals reproduce as `10 + 69 + 2 = 81`.
- **Source integrity:** `sha256sum -c .ai_paper_validation/review_1_5_2/source_hashes_before.sha256` reproduced all three recorded hashes. Direct `pdfinfo` confirmed 10, 69, and 2 pages. No source hash changed during this audit.
- **Fresh-source boundary:** The source inventory, evidence-asset inventory, mapper/checker methods, and run-state boundary all state that prior audit derivatives were not evidence inputs. The current evidence chain cites only the three supplied PDFs and fresh `review_1_5_2` assets. No legacy audit path or decision appears as evidence or as a discovery boundary.
- **Coverage manifest:** 16 rows cover all 12 required stages. Each row contains exactly one undecorated POSIX-style relative artifact path. The 14 currently marked `COMPLETE` resolve to existing artifacts; this audit creates the pending evidence-quality artifact, and report generation remains sequenced after this audit.
- **Relationship coverage:** `N001`-`N059` are contiguous and unique (59/59); the numeric checker records all 59 complete, with its N052 superseding addendum clearly overriding the earlier N052 no-candidate sentence. `S001`-`S051` are contiguous and unique (51/51); both pass artifacts contain 51 explicit relationship-complete rows.
- **Stable-ID identity:** The ledger and mechanical recheck each contain exactly C001, C002, C003, C004, and C005. This audit returns the same five IDs. No stable ID was deleted, merged, ranked, or suppressed.
- **Statistical execution:** Pass 1 agent `/root/statistics_pass_1` and pass 2 agent `/root/statistics_pass_2` are distinct, fresh-spawned `gpt-5.6-terra` agents at `high` reasoning effort. The manifest also contains the coordinator and all preprocessing, mapping, numeric, cross-source, recheck, and current audit agents known at this stage, each once with one primary artifact.
- **Discovery boundary:** The artifacts document complete source and relationship processing, no candidate limit, no top-N selection, no review queue, and no early stopping. The five-candidate set arose after full N/S coverage.
- **Display-zero boundary:** No assigned relationship contains `P = 0`, `p = 0.000`, or an equivalent display zero. No stable candidate is based on display-zero notation, so no conditional independent-contradiction field is required for C001-C005.

## DOC-002 page 37 repair trail

The documented mapping omission was repaired without using an old derivative. Direct PDF page 37 prints 62 participants per group, an additional 24 participants for 20% loss to follow-up, and target 146. The relationship is now present in the fresh support evidence map; provisional `UN029` and `US019`; stable `N052` and `S042`; the numeric-checker and pass-1 superseding addenda; the cross-source checker; C002 and C003; all five-ID recheck; and pass 2. The direct arithmetic is reproducible: `62 + 62 + 24 = 148`, not 146. The distinct SAP/main comparator on DOC-002 page 62 and DOC-001 page 3 prints 65 per group, 12% loss, and target 146. No relationship or candidate remains omitted because of the initial page 37 mapping gap.

Two bounded coordinator repairs remain before final reporting:

1. In `relationships/numeric_relationship_inventory.md`, revise the introductory source-record range from `UN001`-`UN028` to acknowledge the appended `UN029` merged into N052. In `statistics/relationship_inventory.md`, likewise revise `US001`-`US018` to acknowledge `US019` merged into S042. The canonical tables and counts are already complete; only the introductions lag the repaired mapping.
2. Before marking the two pending coverage rows complete, enumerate `C001 C002 C003 C004 C005` literally in the `Exact scope` cells for `evidence_quality` and `report_generation`. The current phrases “Every stable candidate ID” do not satisfy the candidate-stage enumeration rule. Update the evidence-quality row to `COMPLETE` only after this artifact is present, and the report row only after the complete report is assembled.

## C001 — Talc-arm ECOG unknown percentage does not match the count and denominator

- **Evidence and arithmetic:** Direct PDF page 4, Table 1, contains talc `n = 72` and ECOG cells `53 (74)`, `14 (19)`, and `5 (17)`. Counts sum to 72. `100 x 5/72 = 6.944...%`, which rounds to 7%, while companion cells demonstrate ordinary whole-percent rounding. The source location, count, denominator, comparator, and calculation were reproduced.
- **Category and scope:** `Denominator, proportion, or total inconsistency` follows `QUALITY_CONTROL_SCOPE.md`. This is a printed count/percentage identity, not a broad baseline-balance or study-design critique.
- **Assumptions and alternatives:** The audit does not assume that `5 (7)` is the intended final cell. The ledger and recheck correctly preserve alternatives involving the count, denominator, or percentage and identify the missing table-production record.
- **Pagination and links:** DOC-001 PDF page 4 exists; the recheck link resolves to `jama_thomas_2017_oi_170130.pdf#page=4` from its artifact location. The fresh page-4 render also exists.
- **Duplicate assessment:** The numeric and cross-source propositions used the same printed cell, denominator, and percentage rule and were properly merged before C001. It does not duplicate another stable candidate.
- **Report-card readiness:** The ledger and recheck support the required statement, category, locations, evidence, comparator, reasoning, calculation, alternatives, mechanical recheck, and human question. The report generator must add an explicit bounded quality-control relevance statement, bounded downstream evidence-impact statement, concrete human verification steps, and the exact blank adjudication template. It must not state that `5 (7)` is established without the production record.
- **Impact language:** Existing wording is bounded to possible reader interpretation or evidence extraction; it does not claim known propagation or a paper-level conclusion change.

## C002 — Final-protocol sample-size addition does not equal the printed total

- **Evidence and arithmetic:** Direct DOC-002 PDF page 37 prints 62 per group, an additional 24 participants, and target 146. The whole-person addition reproduces as `62 + 62 + 24 = 148`; target 146 instead leaves an addition of 22. The 20% calculation is contextual and is not needed to establish the direct addition mismatch.
- **Category and scope:** `Numeric or arithmetic inconsistency` follows the primary scope category and is limited to the same-page whole-person identity.
- **Assumptions and alternatives:** The candidate does not infer the intended attrition convention or power-test calculation. It names the unavailable power output, rounding convention, and production record, and preserves each printed component as a possible source of the mismatch.
- **Pagination and links:** DOC-002 PDF page 37 exists; the recheck link resolves to `joi170130supp1_prod.pdf#page=37`. The fresh page-37 render exists and the printed paragraph was reproduced directly.
- **Duplicate assessment:** C002 is distinct from C003. C002 applies a same-page addition rule; C003 compares parameter sets across documents. Shared sample-size context and target 146 do not make their comparators or rules identical.
- **Report-card readiness:** The ledger and recheck support the required evidence and reasoning fields. The report generator must add bounded quality-control relevance, bounded downstream impact, human verification steps, and the exact blank adjudication template. It must keep `124/(1-0.20)=155` and alternative attrition conventions clearly secondary to the direct `124 + 24` comparison.
- **Impact language:** No current candidate text claims that recruitment, power, conclusions, or downstream evidence products were changed.

## C003 — Final protocol and SAP/main article give different sample-size inputs for the same target

- **Evidence and comparison:** DOC-002 PDF page 37 prints 62 per group and a 20%/24-participant allowance for target 146. DOC-002 PDF page 62 and DOC-001 PDF page 3 print 65 per group, 12% loss, and target 146. The parameter sets differ while naming the same AMPLE target.
- **Category and scope:** `Cross-document numeric inconsistency` is the applicable primary category. The candidate appropriately asks for the supplied-source link or amendment that explains which parameter set governed recruitment.
- **Assumptions and alternatives:** The ledger and recheck do not assume that the later SAP/main basis superseded the final protocol. They identify chronology as supporting a possible revision while naming the absent operative amendment or approval record.
- **Pagination and links:** DOC-002 pages 37, 51, 52, and 62 and DOC-001 page 3 all exist. Every recheck PDF link resolves and ends in the correct `#page=N` fragment.
- **Duplicate assessment:** C003 is not a duplicate of C002 because its comparator is cross-document parameter identity rather than same-paragraph addition. It is not duplicated elsewhere in the stable set.
- **Report-card readiness:** The ledger and recheck support the required source, comparator, alternatives, and human question. The final card must add bounded quality-control relevance, bounded downstream impact, concrete amendment/version-record checks, and the exact blank adjudication template. It must describe supersession only conditionally unless an operative source is added to the supplied package.
- **Impact language:** Existing wording does not claim that the trial used the wrong target or that any analysis or conclusion changed.

## C004 — SAP ITT definition conflicts with the reported 144-patient ITT denominator

- **Evidence and arithmetic:** DOC-002 pages 62-63 define ITT as all randomized subjects, including those not receiving the assigned intervention. DOC-001 page 3 reports `74 + 72 = 146` randomized; page 4 excludes one pre-intervention withdrawal in each arm and calls `73 + 71 = 144` ITT; page 6 labels the same 73/71 denominators as ITT. The difference `146 - 144 = 2` exactly matches the two exclusions.
- **Category and scope:** `Analysis-unit or population inconsistency` is permissible here because the population definition creates a concrete conflict in the printed ITT label and denominator. The candidate stays within the secondary-category boundary and does not become a broad trial-design critique.
- **Assumptions and alternatives:** The candidate does not infer data availability, consent consequences, or an unstated modified-ITT rule. The recheck names these as source-grounded possibilities and identifies the absent amendment, withdrawal rule, and analysis flag.
- **Pagination and links:** All cited DOC-001 and DOC-002 PDF pages exist, and recheck links resolve with exact page fragments. No printed-page/PDF-page substitution was used.
- **Duplicate assessment:** This is one population-definition/denominator relationship. Its implications across multiple ITT-labelled outcomes are cross-references, not separate stable candidates. It does not duplicate C001's table-cell denominator rule.
- **Report-card readiness:** The ledger and recheck support the required evidence fields. The final card must add bounded quality-control relevance, bounded downstream impact, exact checks for an operative amendment/withdrawal rule/analysis flag, and the exact blank adjudication template. It must not claim that including the two participants would numerically change any effect estimate without participant-level evidence.
- **Impact language:** Existing text is neutral and does not assert a changed result, statistical significance, or paper-level conclusion.

## C005 — Estimated-difference contrast direction is unlabeled and reverses between the main and MI tables

- **Evidence and arithmetic:** DOC-001 page 6 and DOC-003 page 2 both order IPC before talc and label a signed estimated-difference column without a subtraction order. Main baseline dyspnea `50.0` versus `52.2` with `+2.27` and day 1 `64.5` versus `69.7` with `+5.25` imply talc minus IPC. MI baseline `49.8` versus `51.9` with `-2.06` and day 1 `65.5` versus `71.7` with `-6.19` imply IPC minus talc. The signs, not exact equality to rounded group estimates, establish the opposite implied directions.
- **Category and scope:** `Measure, label, or scale inconsistency` is appropriate because a signed contrast lacks an explicit reference-group/subtraction-order label across related tables. The candidate does not equate the primary and MI estimates or claim a statistical-result contradiction.
- **Assumptions and alternatives:** The record preserves intentional opposite model parameterizations as a plausible interpretation. It does not infer coefficient coding, unrounded model means, or MI pooling details.
- **Pagination and links:** DOC-001 page 6 and DOC-003 page 2 exist; both recheck links resolve and both fresh renders exist.
- **Duplicate assessment:** S010-S024, S033, and S051 are multiple rows participating in one cross-table label relationship. Their common unlabeled contrast rule supports one stable candidate rather than row-level duplicates.
- **Report-card readiness:** The ledger and recheck support the source and arithmetic fields. The final card must add bounded quality-control relevance, bounded downstream impact, human checks of model coding/table specifications, and the exact blank adjudication template. It must keep magnitude differences separate from the contrast-label issue.
- **Impact language:** Existing text is bounded to possible reader interpretation and does not assert changed clinical direction, significance, or conclusions.

## Final report safeguards and limitations

The final report has not yet been assembled, so its card-field identity and adjudication placeholders cannot be mechanically confirmed in this pre-report audit. For every C001-C005 card, the report generator must include every exact bold label required by `report_spec.md`. Every human adjudication subfield must remain exactly blank as follows:

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

No candidate card should contain a display-zero conditional field because no candidate mentions a display-zero P value. Downstream-impact wording must identify only what a data extractor, systematic review, meta-analysis, or guideline could copy if a candidate is confirmed; it must not assert actual propagation or conclusion change.

The supplied package contains no participant-level data, analysis code, table-production records, exact rank-test/HL interval construction, mixed-model coefficient coding or variance details, MI pooling details, operative protocol amendment linking the two sample-size calculations, or operative withdrawal/modified-ITT rule. These are bounded human-verification limitations, not grounds to suppress a stable ID. Apart from the two coordinator metadata repairs above and the expected report-stage card assembly, no supportable omission remains in the candidate, recheck, source-coverage, relationship-coverage, statistical-pass, evidence-link, or source-integrity records audited here.
