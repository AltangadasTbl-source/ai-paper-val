# Final Evidence-Quality Audit

## Audit status

**COMPLETE WITH REPAIRABLE UPSTREAM DEFECTS.** This audit covers every stable candidate (`C001`; `C002`; `C003`; `C004`; `C005`), all 16 coverage-manifest rows, all 3 source-coverage rows, the complete fresh source/evidence inventory, all 64 numeric relationships, all 29 statistical relationships, both statistical passes and their canonical pass-status index, the 10 currently manifested agents, and every candidate evidence location and calculation. The five stable IDs remain **Pending Human Adjudication**. This audit assigns no severity, scientific disposition, acceptance/exclusion decision, or correction.

## Coverage and provenance audit

| Audit unit | Mechanical result |
|---|---|
| Direct sources | 3 supplied PDFs; 9 + 21 + 12 = 42 PDF pages. Current SHA-256 values exactly match all 3 entries in `source_hashes_before.sha256`; sizes, PDF versions, and page counts match `source_inventory.md`. |
| Fresh evidence assets | 42 native page-text files, 42 layout page-text files, 42 fresh 200-dpi page renders, 3 whole-document native files, 3 whole-document layout files, and 3 metadata files exist. OCR was not required because all result-relevant native/layout text was usable; DOC-002 p. 21 was visually documented as page-number-only. |
| Source coverage | 3/3 rows are `COMPLETE`. For every row, reusable units = 0 and fresh-required units = mapped units = total units. Totals are 42/42 fresh-required and 42/42 mapped. |
| Coverage manifest | 16 rows cover every required stage. Every `Artifact` cell contains exactly one plain relative path. At audit time, 14 rows are marked `COMPLETE`; `evidence_quality` and `report_generation` remain `PENDING` until the coordinator incorporates this artifact and assembles the report. Two candidate-stage scopes require exact-ID repair below. |
| Numeric relationships | 64/64 canonical `N` relationships are inventoried and checked: N001--N043 and N1001--N1021. One checker summary sentence and one provisional-candidate page link require repair below; neither changes the stable ID set. |
| Statistical relationships | 29/29 canonical `S` relationships are inventoried: S001--S017 and S1001--S1012. Pass 1 contains 29 explicit `PASS_1_COMPLETE` records; pass 2 contains 29 explicit `PASS_2_COMPLETE` records; the canonical pass-2 index contains the same 29 IDs. |
| Statistical execution | Pass 1 agent `/root/statistical_pass_1` and pass 2 agent `/root/statistical_pass_2` are distinct fresh runtime IDs. Both are recorded as `gpt-5.6-terra`, high effort, `FRESH_SPAWN`, with one primary artifact each. |
| Agent manifest | 10 current pre-report agents, including the coordinator and this auditor, appear exactly once with one primary artifact. Any later report generator or repair agent must be appended exactly once before completion and token accounting. |
| Stable-ID equality | Candidate ledger = evidence recheck = this audit = `{C001, C002, C003, C004, C005}`; each set contains 5 unique IDs. No post-registration deletion, merge, ranking, or suppression is supported. |
| Discovery boundary | The fresh artifacts explicitly exclude prior audit/OCR/extraction/candidate/report derivatives as evidence. The inventories and checkers show complete source/relationship scopes, with no top-N, desired-count, queue, candidate cap, or early-stopping boundary. |
| Display-zero rule | No supplied statistical relationship prints `P = 0`, `p = 0.000`, or an equivalent display zero. No stable ID is based on a display-zero P value, and no conditional independent-contradiction field is applicable. |
| Scientific boundary and tone | All five primary categories are permitted by `QUALITY_CONTROL_SCOPE.md`; the records are neutral quality-control observations. No card claims paper invalidity, conclusion change, observed downstream propagation, or unbounded harm. |

All candidate PDF links in `verification/evidence_recheck.md` resolve to the supplied source files and end in `#page=N`. The cited page content was mechanically re-read from the supplied PDFs. Paths in the evidence-asset tables are understandable from their stated `preprocessing/` context, but the path-normalization repair below would make them unambiguous from the review root.

## Candidate-by-candidate audit

## C001 — Matched 205/291 result is printed as 70.4% and 70.5%

- **Category check:** `Cross-document numeric inconsistency` is an allowed primary category and fits the matched Table 3/eTable 5 display conflict.
- **Evidence and pagination:** Found at DOC-001 PDF p. 7, Table 3, and DOC-003 PDF p. 9, eTable 5. The population, outcome, control arm, age label, numerator, denominator, measure, and one-decimal precision match.
- **Reproduction:** `205 / 291 × 100 = 70.446735395%`; nearest-one-decimal display is 70.4%, while the linked supplement prints 70.5%.
- **Assumption control:** The mismatch between the two printed percentages is direct. A transcription, export, weighting, hidden base, or production-rounding explanation is not supplied and remains explicitly hypothetical.
- **Recheck completeness:** All nine required recheck facts are present: location, source value, comparator, rule, calculation, necessary/missing inputs, source-grounded alternative, direct/inferred separation, and remaining human question.
- **Duplicate review:** This is the genuine merge of `CROSS-CAND-001` and `STAT1-CAND-001`; no other stable ID compares the same printed values under the same rule.
- **Bounded report text:** `If confirmed, a data extractor could copy either 70.4% or 70.5% for the same printed 205/291 result. The supplied package does not establish that either value has propagated or changed a conclusion.`
- **Human verification text:** `Confirm whether both displays were generated from the identical unweighted 205/291 result and production rounding rule; then identify the intended displayed percentage.`

## C002 — eTable 2 prints 917/1263 as 72.7%

- **Category check:** `Numeric or arithmetic inconsistency` is allowed and is supported by the within-eTable count/denominator calculation independently of cross-location wording.
- **Evidence and pagination:** The `917 (72.7%)` row and `N=1263` heading are on DOC-003 PDF p. 3, not p. 4. The four Table 1 counts are on DOC-001 PDF p. 5 and the 72.6% narrative is on DOC-001 p. 8.
- **Reproduction:** `205 + 214 + 262 + 236 = 917`; `917 / 1263 × 100 = 72.604908947%`, which displays as 72.6% to one decimal under nearest rounding.
- **Assumption control:** The main narrative says `8 to 12 weeks`, whereas the tabular bin is `8–11 weeks`; the recheck correctly treats that wording as supportive but not proven population identity. The direct 917/1263 calculation is sufficient.
- **Recheck completeness:** All nine required recheck facts are present. The stale claim that the current ledger cites p. 4 must be repaired; the ledger already cites p. 3.
- **Duplicate review:** `NUM-CAND-001` and `CROSS-CAND-002` concern the same printed fraction/percentage relationship and were correctly merged before stable registration.
- **Bounded report text:** `If confirmed, a data extractor could record 72.7% rather than the fraction-derived 72.6% for 917 of 1263 respondents. The package does not establish propagation or conclusion change.`
- **Human verification text:** `Confirm the denominator and production basis for the eTable 2 cell and clarify whether the narrative's 8-to-12-week wording denotes the table's 8–11-week bin.`

## C003 — eTable 2 uses undisclosed reduced education and marital-status bases

- **Category check:** `Denominator, proportion, or total inconsistency` is allowed and fits the unlabeled difference between full column Ns and variable-specific category totals.
- **Evidence and pagination:** Found at DOC-003 PDF p. 3, eTable 2. The table provides full heading Ns but no missing/unknown row or row-specific N for the two blocks.
- **Reproduction:** Education sums are 1258/336/1594, leaving 5/1/6 relative to 1263/337/1600. Marital-status sums are 1248/332/1580, leaving 15/5/20. Discriminating cells reproduce the reduced bases, including `640/1248 = 51.2821%` versus `640/1263 = 50.6730%`.
- **Assumption control:** Missing observations and complete-case denominators are plausible explanations but are not printed facts. The candidate is about disclosure/reconciliation, not a claim that the percentages are analytically wrong.
- **Recheck completeness:** All nine required recheck facts are present, including the exact missing denominator definitions.
- **Duplicate review:** C003 is distinct from C004 because it concerns eTable 2 respondent/nonrespondent/total columns and different printed values.
- **Bounded report text:** `If confirmed, a secondary user could mistakenly use the full respondent-status Ns as the education or marital-status percentage bases. The package does not show that this has occurred.`
- **Human verification text:** `Confirm the variable-specific nonmissing denominators and missing counts for each respondent-status column and determine whether the table should disclose them.`

## C004 — eTable 3 uses several undisclosed reduced bases

- **Category check:** `Denominator, proportion, or total inconsistency` is allowed and fits the affected baseline characteristic blocks.
- **Evidence and pagination:** Found at DOC-003 PDF p. 5, eTable 3. The four group headings are 417/387/421/379, with no missing/unknown row or variable-specific N in the affected blocks.
- **Reproduction:** Race/ethnicity sums are 416/387/421/379; education sums are 417/387/421/377; marital-status sums are 414/387/419/377. Discriminating examples include `155/416 = 37.2596%` versus `155/417 = 37.1703%`, and `87/377 = 23.0769%` versus `87/379 = 22.9551%`.
- **Assumption control:** Variable-specific missingness is a plausible but unprinted explanation. The records do not infer that all group members had observed values or prescribe an analytic correction.
- **Recheck completeness:** All nine required recheck facts are present. The recheck appropriately notes that `51/377` alone is not denominator-discriminating at one decimal and supplies other discriminating cells.
- **Duplicate review:** C004 is not a duplicate of C003 because it concerns a different table, population grouping, printed values, and denominator identities.
- **Bounded report text:** `If confirmed, a secondary user could reconstruct affected eTable 3 percentages with the displayed full group Ns instead of the apparent variable-specific bases. The package does not establish downstream use or conclusion change.`
- **Human verification text:** `Confirm the nonmissing Ns and missing counts for each affected eTable 3 group-variable block and determine whether row-specific bases should be disclosed.`

## C005 — Linked displays use ≥60 versus >60 days

- **Category check:** `Measure, label, or scale inconsistency` is an allowed primary category. The concrete issue is a non-equivalent threshold label in reciprocally linked table/figure displays, not a general study-design concern.
- **Evidence and pagination:** DOC-003 PDF p. 9, eTable 5 title, prints `≥60 days`; p. 10 refers readers to the eFigure; p. 11, eFigure title, prints `>60 days` and refers readers to eTable 5 for sample sizes.
- **Reproduction:** `age ≥ 60` includes age 60; `age > 60` excludes it. No record-level numerical calculation is possible from the supplied aggregate displays.
- **Assumption control:** The record does not assert that any infant was exactly 60 days old, that table and figure values differ, or that the strict symbol was used operationally. Those are unresolved alternatives.
- **Recheck completeness:** All nine required recheck facts are present, including the missing operational filter and exact remaining question.
- **Duplicate review:** `NUM-CAND-004`, `CROSS-CAND-003`, and `STAT1-CAND-002` are genuine duplicates of the same linked-display threshold conflict and were correctly merged before stable registration.
- **Bounded report text:** `If confirmed, a data extractor could record either an inclusive or strict 60-day eligibility rule for the linked displays. The supplied package does not establish that the underlying data differ or that a downstream conclusion changed.`
- **Human verification text:** `Confirm the operational age filter used for both displays, determine whether any exactly-60-day records existed, and identify the intended labels.`

## Final-card field audit

The final report had not yet been assembled at this audit cutoff, so candidate-card compliance cannot be marked complete yet. For every C ID, the ledger and recheck supply source locations, evidence, comparator, rule, calculation, alternatives, mechanical recheck facts, and the human question. The report generator must add the exact report-spec labels for candidate statement, category, exact locations, source evidence, reported-versus-comparator, reasoning procedure, calculation, alternatives, mechanical recheck, quality-control relevance, bounded downstream impact, human verification steps, and human adjudication fields.

Every final card must use this exact blank template:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

No candidate mentions a display-zero P value, so the conditional `Independent contradiction beyond P=0 display` field must not be added to these cards.

## Repairable upstream defects and exact repair text

1. **Numeric checker, false pagination for NUM-CAND-001.** In `checkers/numeric_consistency.md`, replace the DOC-003 p. 4 link with: `[DOC-003#page=3](../../../joi170077supp2_prod.pdf#page=3), eTable 2, respondent infant age at follow-up, 8–11 weeks: 917 (72.7%)`.
2. **Numeric checker, overbroad N1017--N1020 summary.** Replace `All 40 fractions reproduce displayed percentages within tolerance` with: `All checked eTable 5 fractions reproduce their displayed percentages within tolerance except the N1018 all-race control room-sharing cell, where 205/291 is printed as 70.5%; that matched conflict is registered as C001 through the cross-source and statistical lanes.`
3. **Evidence recheck, stale statement about the ledger.** In C002, replace the opening of `Cited location found` with: `Yes. The 917 (72.7%) row and respondent heading N=1263 are on DOC-003 PDF p. 3, eTable 2; PDF p. 4 contains only continuation rows.` In the summary, replace `ledger-cited p. 4` with `an earlier provisional checker citation to p. 4`.
4. **Statistical pass 2, stale pagination lineage.** In the C002 reconciliation row, replace `The recheck corrects the location to DOC-003 PDF p. 3 (not p. 4)` with: `The ledger and recheck identify the exact location as DOC-003 PDF p. 3; an earlier provisional numeric-checker link to p. 4 requires correction.`
5. **Coverage-manifest candidate scopes.** Replace the `evidence_quality` scope with `C001; C002; C003; C004; C005; all 16 coverage rows; all 3 source-coverage rows` and the `report_generation` scope with `C001; C002; C003; C004; C005; complete run metadata`. Mark the evidence-quality row `COMPLETE` after accepting this artifact and the report row `COMPLETE` only after the complete Markdown report exists.
6. **Evidence-asset path clarity.** Where `evidence_asset_inventory.md` names derivative files as `metadata/...`, `native_text/...`, `layout_text/...`, `page_text/...`, or `rendered_pages/...`, prefix them with `preprocessing/` when the path is intended to be review-root-relative. The assets themselves exist; this is a reproducibility-path normalization.
7. **Final-card completeness.** Populate every report card using all required labels, the bounded candidate-specific text above, and the exact `__` adjudication template. Do not infer a correction, severity, downstream propagation, or conclusion impact.

## Audit conclusion

All five stable candidates are source-grounded and reproducible as neutral quality-control observations. All candidate rechecks contain every required fact, the stable ID sets agree, both complete statistical passes use distinct fresh Terra/high agents, all direct-source units and relationship units are covered, and no display-zero-only candidate exists. Completion remains contingent on the seven repair items above, final report assembly, manifest/token updates for any later agent calls, hash recomputation, HTML rendering, and mechanical validation.
