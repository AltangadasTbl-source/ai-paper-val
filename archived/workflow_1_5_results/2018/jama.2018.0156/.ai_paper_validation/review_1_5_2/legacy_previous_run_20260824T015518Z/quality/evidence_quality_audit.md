# Evidence Quality Audit

## Audit scope and evidence boundary

This fresh quality-control audit covers the complete current-run source inventory, evidence-asset inventory, `source_coverage.md`, all 23 rows of `coverage_manifest.md`, both canonical relationship inventories and all eight relationship-map parts, all four checker artifacts, the stable candidate ledger, the four-record mechanical evidence recheck, and all 14 current rows of `agent_execution_manifest.md`. It uses only supplied package sources, fresh-run artifacts, and the explicitly user-authorized source-hash-matched OCR assets. No web source, new OCR, prior candidate set, old checker conclusion, old final report, top-N rule, review queue, or candidate-count target was used.

The direct-source SHA-256 values were independently recomputed and match `source_hashes_before.sha256` for all three PDFs. The authorized OCR text and image paths all resolve. One copied OCR image checksum is inaccurate and is listed below as a required provenance repair; it does not affect C001-C004, which all use DOC-001.

## Mechanical coverage status

| Audit item | Completed scope | Audit result |
|---|---:|---|
| Direct sources | 3/3 | DOC-001 `9/9`, DOC-002 `134/134`, and DOC-003 `3/3` have `Reusable units = 0`, `Fresh-required units = Total units`, `Mapped units = Total units`, and `COMPLETE`. DOC-002 p. 134 remains an explicit empty-page limitation. |
| Source units | 146/146 | Every page belongs to one disjoint evidence-mapping shard. The user-authorized OCR exception is bounded to the provenance index; no OCR was run in this review. |
| Numeric relationships | 98/98 | N001-N098 are gap-free; shard totals are 29 + 17 + 38 + 14 = 98; the numeric checker has 98 explicit relationship rows. |
| Statistical relationships | 55/55 in each pass | S001-S055 are gap-free; shard totals are 17 + 14 + 14 + 10 = 55; both pass artifacts contain 55 explicit `PASS_1_COMPLETE` or `PASS_2_COMPLETE` rows. |
| Cross-source relationships | 153/153 | N001-N098 plus S001-S055 are explicitly covered. Two cross-lane wording/calculation reconciliations are required below. |
| Stable candidates | 4/4 | Ledger and recheck ID sets are identical: C001, C002, C003, C004. This audit returns the same set. No stable ID is deleted, merged, ranked, renumbered, or suppressed. |
| Evidence rechecks | 4/4 | Location, source text, comparator, rule, calculation, available/missing inputs, alternatives, inference boundary, and human question are present separately for every stable ID. |
| Coverage rows | 23/23 structurally checked | Every existing row contains exactly one undecorated relative artifact path. All 21 rows currently marked `COMPLETE` resolve. The audit and report rows are correctly still `PENDING` at the time of this audit. Two canonical relationship-inventory rows are missing and require addition. |
| Statistical agents | 2/2 | Pass 1 agent `73b64cf4-d780-58b8-b200-d7723373321d` and pass 2 agent `23866370-c384-545f-af7b-e837892be6b0` are distinct fresh `gpt-5.6-terra`/`high` agents with distinct artifacts and full S001-S055 scopes. |
| Current execution manifest | 14/14 rows checked | The coordinator appears once; every current row has one agent ID, model, effort, start mode, and one artifact. The later report-generator agent and any repair agent must be added when actually spawned. |
| Candidate evidence links | 4/4 | DOC-001 links for PDF pp. 4 and 6 resolve; both anchors are within the 9-page source. Recheck links to the ledger and fresh simple/layout locator files also resolve. No false pagination was found. |
| Display-zero rule | 4/4 candidates compliant | No source relationship displays `P = 0`, `p = 0.000`, or an equivalent display zero. `P < .001` and `P < .0001` are correctly treated as thresholds. No candidate is based on display-zero reasoning, so the conditional independent-contradiction field is not applicable. |

The candidate categories are single allowed `QUALITY_CONTROL_SCOPE.md` categories. All stable records remain exactly `Pending Human Adjudication`; no scientific disposition or severity is assigned. The downstream-reuse statements are bounded to what an extractor or later evidence product could copy if a candidate is confirmed, and none claims observed propagation or a changed paper conclusion.

## C001 — Per-protocol ETI ROSC proportion/denominator relationship

- **Coverage and source grounding:** DOC-001 Table 2, PDF p. 6, directly prints PP denominators `995` and `943`, BMV `342 (34.4)`, ETI `377 (30.0)`, BMV-minus-ETI `-5.6 (-9.9 to -1.3)`, and `P = .01`. The ledger and recheck locations resolve and agree.
- **Reproduction:** `100 x 342/995 = 34.371859%`; `100 x 377/943 = 39.978791%`; and `100 x (342/995 - 377/943) = -5.606932` percentage points. The displayed ETI percentage is therefore 9.978791 percentage points below the count-derived value, while the count-derived signed difference agrees with `-5.6` at one decimal.
- **Fields, category, and inference boundary:** The ledger has every recheck-required field. `Denominator, proportion, or total inconsistency` is an allowed primary category. The alternative denominator/production explanations and intended-value question are explicitly separated from direct observation. The merged propositions compare the same row, printed values, and rule; no possible duplicate remains.
- **Required repair:** In `checkers/statistical_pass_1.md`, `STAT1-CAND-002`, change the purported exact count-derived difference from `-5.6068...` to `-5.606932...` (or a correctly rounded `-5.6069`). Do not turn the arithmetic correction into an intended source correction.
- **Audit limitation:** The package does not identify which printed element was intended or provide an alternate ETI denominator. Human adjudication remains required.

## C002 — Per-protocol day-28-survival displayed point difference

- **Coverage and source grounding:** DOC-001 Table 2, PDF p. 6, directly prints `54/995 (5.4%)`, `51/943 (5.4%)`, BMV-minus-ETI `0.1`, CI `-10 to 9.7`, and `P = .99`. The ledger and recheck locations resolve and agree.
- **Reproduction:** `100 x 54/995 = 5.427136%`; `100 x 51/943 = 5.408271%`; the direct count-derived difference is `0.018864` percentage points, not `0.0191` or `0.01907`. Its distance from the printed `0.1` is `0.081136` percentage points, exceeding a 0.05-percentage-point half-last-place tolerance. Ordinary one-decimal rounding gives `0.0`.
- **Fields, category, and inference boundary:** The ledger has every recheck-required field. `Numeric or arithmetic inconsistency` is allowed. The ledger correctly makes the calculation conditional on the printed pairs defining the estimator and names the missing estimator/denominator/retained-rate definitions. C002 is not a duplicate of C003: C002 checks the point display and rounding, while C003 checks the interval scale/span.
- **Required repairs:** (1) In `candidate_ledger.md`, C002 `Reproducible rule and calculation` and `Tolerance`, replace `0.0191` and `0.0809` with `0.018864` and `0.081136` (or correctly rounded equivalents). (2) In `checkers/statistical_pass_1.md`, `STAT1-CAND-001`, replace `0.01907...` with `0.018864...`. (3) In `checkers/cross_source_consistency.md`, `CROSS-CAND-002`, replace the false statement that about `0.019` is compatible with displayed `0.1` after rounding; state that it rounds to `0.0` and cross-reference the distinct point-display proposition without creating another stable ID.
- **Audit limitation:** The source does not supply a row-specific estimator or retained group rates, so the audit cannot assign a replacement point estimate.

## C003 — Per-protocol day-28-survival confidence-interval scale/span

- **Coverage and source grounding:** The same DOC-001 Table 2 row directly prints the percentage-point effect label, counts, group percentages, `0.1`, 95% CI `-10 to 9.7`, and `P = .99`; the article methods supply chi-square/Fisher alternatives but not the row-specific CI construction.
- **Reproduction:** From the printed count/denominator pairs, the diagnostic unpooled binomial standard error is `1.028756` percentage points, and `0.018864 +/- 1.96 x 1.028756` gives approximately `-1.997498 to 2.035226` percentage points. This diagnostic interval is not a proposed correction. The printed interval spans 19.7 percentage points. `P = .99` is a near-unit P value and is directionally compatible with a near-null point estimate; it does not independently identify the CI variance or prove the interval span incompatible.
- **Fields, category, and inference boundary:** The ledger has every recheck-required field. `Statistical reporting inconsistency` is allowed. The diagnostic method, missing row-specific construction, possible alternate/adjusted method, and possible production issue are distinguished. C003 remains distinct from C002 because its comparator and rule concern interval scale/span, not one-decimal point rounding.
- **Required repairs:** (1) In `candidate_ledger.md`, C003 `Comparator`, replace `near-zero P-value display` with `near-unit P-value display` or neutral `same-row P-value display`. (2) In the same card, replace the approximate SE/interval values `1.05` and `-2.0 to 2.1` with the rechecked values above, or state a consistently rounded `about 1.03` and `about -2.00 to 2.04`. (3) Remove or bound wording that suggests `P = .99` independently contradicts the wide interval; retain it only as observed context that does not supply the missing CI construction. (4) Apply the same arithmetic and inference-boundary repairs to `CROSS-CAND-002` in `checkers/cross_source_consistency.md`, especially the statements that the wide interval is not coherent with `P = .99` and that the printed counts yield a P-value contradiction.
- **Audit limitation:** The exact CI formula, variance estimator, row-specific test selection, adjustment, and software options are not supplied. The audit supports a verification question, not intended interval limits or a final correction.

## C004 — Centre-5 count outcome versus seconds unit

- **Coverage and source grounding:** DOC-001 Results, PDF p. 4, and Methods, PDF p. 3, both name the `number of pauses` exceeding a 2-second threshold. Results print BMV `27`, ETI `16`, `difference, 11 seconds`, CI `7 to 15`, and `P < .001`. Both PDF pages and locator files resolve.
- **Reproduction:** `27 - 16 = 11`. Under the explicitly named count interpretation, `11` is a difference in qualifying pauses; `2 seconds` defines the event threshold and does not supply a duration unit for the count. No rounding tolerance applies.
- **Fields, category, and inference boundary:** The ledger has every recheck-required field. `Measure, label, or scale inconsistency` is allowed. The source does not define whether 27 and 16 are totals, means, medians, or duration summaries; the ledger preserves that alternative rather than assigning a correction. This relationship is distinct from the CCF percentage result and from C001-C003.
- **Required repair:** In `checkers/cross_source_consistency.md`, the N025 coverage row currently says the pause seconds/count wording is not conflated and the matched result is coherent. Replace that with bounded cross-lane reconciliation: the arithmetic is coherent, but the named count-versus-seconds label remains the separately registered NUM-CAND-003/C004 issue; no additional cross-source proposition is created.
- **Audit limitation:** No underlying monitor data or group-summary definition is supplied, so the audit cannot choose whether the count wording or time unit was intended.

## Global required repairs before report assembly

1. **Authorized OCR provenance checksum:** In `preprocessing/reused_ocr/DOC-002_authorized_ocr_provenance.md`, DOC-002 p. 129 `Image SHA-256`, replace `97bd40bf0758a17204a30cd62791725b379595119872f2e72e3b31ef16b30ba0` with the independently recomputed `97bd40bf189df679ac64199e8a3bc06e379ddf56cfe5c7cfb37b1d0fab85a5ef`. All other listed OCR text/image checksums matched. This repair changes provenance metadata only.
2. **Source-coverage table structure:** `source_coverage.md` contains the three required direct-source rows plus a fourth bold total row. The contract requires exactly one data row per direct source. Move the `146/0/146/146` aggregate to prose outside the table so the table has exactly three data rows; retain all three source rows unchanged.
3. **Coverage-manifest canonical inventories:** Add one unique coverage row for `relationships/numeric_relationship_inventory.md` with scope N001-N098 and one unique row for `statistics/relationship_inventory.md` with scope S001-S055. Each row must contain exactly one plain relative artifact path. These canonical merge artifacts exist and are represented by the manifested relationship-inventory work but are absent from the current 23-row manifest.
4. **Stage closeout after this artifact:** Change only the `evidence_quality` row in `coverage_manifest.md` from `PENDING` to `COMPLETE` after this file is durable. Keep report generation pending until its artifact exists.
5. **Report and execution closeout:** The future report generator, and any agent used for the repairs above, must be added exactly once to `agent_execution_manifest.md` and later to `token_usage_ledger.csv`. The report-generation coverage row must enumerate C001, C002, C003, C004 and change to `COMPLETE` only after the Markdown exists.
6. **Human-adjudication placeholders:** The final report does not yet exist, so its card fields cannot be mechanically confirmed in this audit. Every C001-C004 final card must use exactly `Validity: __`, `Importance: __`, `Action: __`, `Initials: __`, and `Notes: __`. No dash, prose, checkbox, or prefilled adjudication is permitted.

## Audit totals and limitations

- Stable IDs audited: **4/4**.
- Stable IDs with source location, comparator, rule, and mechanical recheck: **4/4**.
- Candidate-specific repair groups: **4** (C001 exact pass-1 arithmetic; C002 arithmetic/rounding reconciliation; C003 P-value wording and diagnostic arithmetic; C004 cross-lane wording).
- Global repair groups: **6** (OCR checksum, source-table structure, two missing canonical coverage rows, evidence-quality stage closeout, future agent/report closeout, and final-card blank placeholders).
- Stable IDs rejected, deleted, merged, ranked, renumbered, or suppressed: **0**.
- Display-zero-only stable IDs: **0**.
- False candidate PDF pagination found: **0**.
- Broken candidate/recheck local links found: **0**.

The current evidence supports carrying all four stable IDs forward as neutral quality-control candidates pending human adjudication. The repairs above are reproducibility, arithmetic, inference-boundary, cross-lane-consistency, provenance, and closeout repairs; none assigns a scientific disposition, severity, intended source correction, or paper-level conclusion impact.
