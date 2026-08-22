# Final Evidence-Quality Audit

## Audit outcome

The evidence-quality review covers every stable candidate `C001` through `C013`, every direct-source row, every coverage-manifest row, the complete numeric and inferential relationship inventories, both statistical passes, the candidate ledger, the mechanical recheck, evidence links, source hashes, and the execution manifest. All 13 stable candidates remain **Pending Human Adjudication**. No candidate was deleted, merged, ranked, suppressed, renumbered, assigned severity, or given a scientific disposition.

The candidate evidence set is supportable for report assembly. One discovery omission was repaired during the run: the control 9-month BMI-count mismatch became `C013` without changing earlier IDs. This audit also identified the previously unnumbered DOC-002 p. 64 revised-protocol relationship underlying `C010` and `C012`; the coordinator added it as `PN020`/`N064`, checked it in the numeric and cross-source lanes, updated coverage, and retained all stable candidate IDs. Final workflow completion remains conditional on marking the evidence-quality and report-generation rows `COMPLETE`; adding the report generator and any later repair agent to the execution manifest; assembling every final report card; and completing token accounting, final source hashing, rendering, and validation.

## Overall source, coverage, and integrity audit

| Audit area | Result |
|---|---|
| Direct sources | `DOC-001` 11/11 pages, `DOC-002` 113/113 pages, and `DOC-003` 8/8 pages are `COMPLETE`; for every row reusable units are 0 and total = fresh-required = mapped. Totals are 132/132/132. |
| Source hashes | All three current SHA-256 values exactly match `source_hashes_before.sha256`. No source-integrity change was found. |
| Fresh-source boundary | The evidence chain cites the supplied PDFs and fresh Workflow 1.5.2 derivatives only. No legacy audit path or legacy disposition appears as evidence or a discovery boundary. The preprocessing and pass-2 artifacts expressly record nonreuse. |
| Page/unit mapping | DOC-001 pp. 1-11, DOC-002 pp. 1-113, and DOC-003 pp. 1-8 are explicitly accounted for. Result-relevant text, tables, figures, schedules, and model definitions are mapped; nonapplicable pages are explicitly marked. |
| Numeric relationships | The original canonical set `N001`-`N063` had one explicit checker status per ID with no gap. Audit repair added `PN020`/`N064` for DOC-002 p. 64. The final inventory and numeric checker now contain 64 unique, gap-free rows, and the cross-source and coverage scopes explicitly include `N064`. Its two implications remain the already registered `C010` and `C012`. |
| Statistical relationships | `S001`-`S071` are present without gaps. Pass 1 has 71 explicit `PASS_1_COMPLETE` records and pass 2 has 71 explicit `PASS_2_COMPLETE` records. |
| Statistical agents | Pass 1 runtime ID `/root/statistics_pass_1` and pass 2 runtime ID `/root/statistics_pass_2` are distinct fresh agents, each recorded as `gpt-5.6-terra`, `high`, `FRESH_SPAWN`, with one primary artifact. |
| Stable-ID parity | Ledger and recheck sets are identical: `C001`-`C013`, 13 unique IDs. This audit contains the same 13 headings. Pass 2 reconciles all 13 and appends none. |
| Candidate discovery boundary | No target, minimum, maximum, top-N rule, review queue, or early-stopping rule controlled discovery. The complete 64 numeric relationships after audit repair and all 71 inferential relationships are the boundary. |
| Display-zero exclusion | No stable candidate is based on `P = 0`, `p = 0.000`, or equivalent. No candidate card needs the conditional independent-contradiction field. |
| Categories and tone | Every ledger category is allowed by `QUALITY_CONTROL_SCOPE.md`. Wording is neutral quality control and does not assign severity, validity, acceptance, rejection, or correction. |
| Evidence links and pagination | Every candidate-ledger and recheck PDF target resolves locally, and each link ends in the cited `#page=N`. The cited printed content was found on those PDF pages. No false pagination was found. Final-report links must be rebased to the report location (`../SOURCE.pdf#page=N`) rather than copied verbatim from deeper artifacts. |
| Coverage manifest | All required stages are present and every artifact cell contains one plain relative path. Numeric and cross-source scopes include `N001`-`N064`; candidate-stage scopes enumerate all 13 IDs; statistical scopes enumerate all 71 S IDs. Only the active quality row and planned report row require final status updates. |
| Execution manifest | The coordinator and all 11 specialists used through this audit are each listed once with one primary artifact. No duplicate agent ID was found. The report generator and any later repair/model agent must be appended exactly once when used. |

The cross-source checker initially recorded 8 BMI arm-by-time discrepancies and 4 other provisional items. The numeric checker recorded all 9 nonzero BMI arm-by-time discrepancies; mechanical recheck repaired the omitted control 9-month relationship as `C013`. The ledger introduction was correspondingly repaired from “eight” to “nine.” This is complete discovery repair, not candidate suppression or retrospective top-N selection.

## Final-card assembly requirements

The ledger and recheck contain enough source-grounded material to populate every required final-report label for every ID: candidate statement, category, exact source locations, source evidence, reported-versus-comparator, reasoning procedure, calculation, alternative source-grounded interpretations, mechanical evidence recheck, quality-control relevance, bounded potential downstream evidence impact, human verification steps, and human adjudication fields. The report generator must not merely copy the shorter ledger format. It must use the exact labels in `report_spec.md`, keep direct observation separate from inferred explanations, and rebase source links for a report stored directly in `.ai_paper_validation/`.

For every candidate, the downstream statement must be conditional and bounded to what an evidence extractor, systematic review, meta-analysis, or guideline author could copy if the candidate is confirmed. There is no supplied-package evidence that any candidate propagated downstream or changed the paper-level conclusion.

## C001 — Intervention 3-month BMI-observation count differs across result displays

- **Evidence-quality result:** Supportable source-grounded candidate; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-001 Figure 1 p. 3 prints 288; DOC-001 Figure 2 p. 7 and DOC-003 eTable 1 p. 2 print 279. `288 - 279 = 9` is correct; all cited pages and local link targets resolve.
- **Missing definitions and unsupported assumptions:** Participant-level reconciliation and any post-collection validity/cleaning rule are unavailable. A nine-record exclusion is a possible explanation, not an established fact.
- **Duplicate/category check:** Distinct from the other BMI-count candidates because the arm, visit, and printed integers differ. Category `Cross-document numeric inconsistency` is in scope.
- **Impact/report repair:** State only that a confirmed mismatch could affect extraction of the intervention 3-month observed-BMI denominator. Do not claim effect-estimate or conclusion change. Populate every required report-card label from the ledger and recheck.

## C002 — Control 3-month BMI-observation count differs across result displays

- **Evidence-quality result:** Supportable source-grounded candidate; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-001 Figure 1 p. 3 prints 277; DOC-001 Figure 2 p. 7 and DOC-003 eTable 1 p. 2 print 271. `277 - 271 = 6` is correct; pages and links resolve.
- **Missing definitions and unsupported assumptions:** No record-level cleaning, validity, or exclusion definition is supplied. The six-record exclusion explanation must remain conditional.
- **Duplicate/category check:** Separate control-arm/3-month relationship; not a duplicate of `C001` or later visits. Allowed cross-document category.
- **Impact/report repair:** Bound reuse risk to the control 3-month displayed denominator; do not infer model-result or paper-conclusion impact. Populate all required report fields.

## C003 — Intervention 9-month BMI-observation count differs across result displays

- **Evidence-quality result:** Supportable source-grounded candidate; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-001 Figure 1 p. 3 prints 282; DOC-001 Figure 2 p. 7 and DOC-003 eTable 1 p. 2 print 280. `282 - 280 = 2` is correct; pages and links resolve.
- **Missing definitions and unsupported assumptions:** The two record identities and any descriptive-display inclusion rule are missing. Post-collection exclusion is inferred only.
- **Duplicate/category check:** Unique intervention/9-month count identity; not merged with `C013`, which is the control arm at the same visit. Category is allowed.
- **Impact/report repair:** Limit downstream wording to possible extraction of the wrong intervention 9-month denominator; no conclusion-change claim. Populate all report labels.

## C004 — Intervention 12-month BMI-observation count differs across result displays

- **Evidence-quality result:** Supportable source-grounded candidate; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-001 Figure 1 p. 3 prints 275; DOC-001 Figure 2 p. 7 and DOC-003 eTable 1 p. 2 print 274. `275 - 274 = 1` is correct; pages and links resolve.
- **Missing definitions and unsupported assumptions:** The one record and any cleaning/analytic-subset rule are absent. Do not state that an exclusion occurred.
- **Duplicate/category check:** Distinct arm/visit/count relationship; allowed cross-document category.
- **Impact/report repair:** Bound reuse risk to the intervention 12-month denominator and avoid claims about analysis or conclusion effects. Populate all required report fields.

## C005 — Control 12-month BMI-observation count differs across result displays

- **Evidence-quality result:** Supportable source-grounded candidate; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-001 Figure 1 p. 3 prints 276; DOC-001 Figure 2 p. 7 and DOC-003 eTable 1 p. 2 print 275. `276 - 275 = 1` is correct; pages and links resolve.
- **Missing definitions and unsupported assumptions:** No record identity, disposition, or subset rule is supplied. A cleaning exclusion is only an alternative.
- **Duplicate/category check:** Separate control/12-month identity; not a duplicate of `C004`. Category is allowed.
- **Impact/report repair:** Restrict downstream language to possible reuse of the control 12-month denominator. Populate all exact report-card labels and make no conclusion claim.

## C006 — Intervention 24-month BMI-observation count differs across result displays

- **Evidence-quality result:** Supportable source-grounded candidate; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-001 Figure 1 p. 3 prints 280; DOC-001 Figure 2 p. 7 and DOC-003 eTable 1 p. 2 print 278. `280 - 278 = 2` is correct; pages and links resolve.
- **Missing definitions and unsupported assumptions:** Participant-level dispositions and display-inclusion rules are unavailable. Do not assert that two records were invalid or excluded.
- **Duplicate/category check:** Unique intervention/24-month count identity; allowed cross-document category.
- **Impact/report repair:** Bound reuse risk to the intervention 24-month denominator; do not extend it to a proven model or conclusion effect. Populate all required fields.

## C007 — Control 24-month BMI-observation count differs across result displays

- **Evidence-quality result:** Supportable source-grounded candidate; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-001 Figure 1 p. 3 prints 267; DOC-001 Figure 2 p. 7 and DOC-003 eTable 1 p. 2 print 266. `267 - 266 = 1` is correct; pages and links resolve.
- **Missing definitions and unsupported assumptions:** The one record and any validity/cleaning rule are missing. Exclusion is not established.
- **Duplicate/category check:** Distinct control/24-month relationship; not a duplicate of `C006`. Category is allowed.
- **Impact/report repair:** Restrict potential reuse to the displayed control 24-month denominator and avoid conclusion-impact claims. Populate every required report label.

## C008 — Intervention 36-month BMI-observation count differs across result displays

- **Evidence-quality result:** Supportable source-grounded candidate; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-001 Figure 1 p. 3 prints 278 retained and defines retained by BMI collection; DOC-001 Figure 2 p. 7 and DOC-003 eTable 1 p. 2 print 276. `278 - 276 = 2` is correct; pages and links resolve.
- **Missing definitions and unsupported assumptions:** The operational meaning of retained and any post-collection exclusion rule are unavailable. Broader administrative retention and record exclusion are alternatives, not facts.
- **Duplicate/category check:** Unique intervention/36-month identity. Control 36-month values agree and correctly have no separate candidate. Category is allowed.
- **Impact/report repair:** Bound reuse risk to the intervention 36-month observed/retained denominator; do not claim the adjusted effect or conclusion changed. Populate all report-card fields.

## C009 — Final SAP says six assessment points but enumerates five

- **Evidence-quality result:** Supportable direct count/list candidate; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-002 final SAP p. 110 lists baseline, 3, 9, 12, and 36 months beside “6 time points”; DOC-002 p. 112 separately says six repeated measurements. `count = 5`, not 6. DOC-002 p. 15, DOC-001 p. 4, and DOC-003 p. 2 include 24 months; links and pages resolve.
- **Missing definitions and unsupported assumptions:** The archived analysis input schedule is unavailable. Identifying 24 months as the intended omitted item is strongly source-supported but still an inference; the candidate does not prove its exclusion from the model.
- **Duplicate/category check:** `NUM-P02`, `PC-S001`, and `XSR-009` were correctly merged because they compare the same sentence, schedule, and rule. Category `Numeric or arithmetic inconsistency` is allowed.
- **Impact/report repair:** Bound downstream language to extraction of the planned measurement schedule or model-timepoint description. Do not claim that 24-month data were omitted from analysis or that conclusions changed.

## C010 — Revised protocol gives six points but lists seven including 48 months

- **Evidence-quality result:** Supportable direct total/list candidate; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-002 revised protocol p. 64 prints `6-points in time (T1-T6)` and lists baseline, 3, 9, 12, 24, 36, and 48 months; `count = 7`. The page also says seven data-collection points. Article p. 4 and supplement p. 2 report through 36 months. Pages and links resolve.
- **Missing definitions and unsupported assumptions:** Amendment/version history and whether 48 months was a separate extension are unavailable. Absence of a 48-month result is not itself proof of error; the candidate must remain centered on the internal six-versus-seven wording.
- **Duplicate/category check:** Distinct from `C009` because it concerns a different protocol version, sentence, comparator, and seven-item rule. Category `Denominator, proportion, or total inconsistency` is within the allowed total-inconsistency scope.
- **Impact/report repair:** Bound reuse risk to protocol schedule abstraction. Do not imply a missing outcome, protocol violation, or conclusion change. Preserve the complete `PN020`/`N064`, `N010`, `N047`, and `N056`-`N060` schedule/result provenance.

## C011 — Original protocol labels BMI percentile/BMI% while results use BMI kg/m²

- **Evidence-quality result:** Supportable label/scale candidate; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-002 original protocol p. 16 prints `BMI Percentile`/`BMI%` beside a kg/m² formula; final SAP pp. 110-111 models BMI, DOC-001 p. 3 defines kg/m², and DOC-003 p. 2 prints raw BMI values. This is a categorical scale comparison with no rounding calculation. Pages and links resolve.
- **Missing definitions and unsupported assumptions:** The analysis variable/codebook and any approved scale amendment are missing. A typographical shorthand or a later outcome-scale change are alternatives; neither is established.
- **Duplicate/category check:** `NUM-P03` and `XSR-011` were correctly merged as the same label/scale relationship. Category `Measure, label, or scale inconsistency` is exact and allowed.
- **Impact/report repair:** Bound downstream wording to possible misclassification of the prespecified/reported outcome scale by an evidence extractor. Do not claim the analysis used the wrong variable or that conclusions changed.

## C012 — Control-condition session count and duration differ across protocol versions and article

- **Evidence-quality result:** Supportable cross-document candidate with a material version/component ambiguity; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-002 original protocol p. 14 prints 12 quarterly 60-minute sessions (`12 x 60 = 720` minutes); revised protocol p. 64 prints seven 45-minute programs (`7 x 45 = 315` minutes); DOC-001 pp. 1 and 3 print six 30-minute activities (`6 x 30 = 180` minutes). Arithmetic and pages are correct, and links resolve.
- **Missing definitions and unsupported assumptions:** Protocol chronology, amendment mapping, session logs, and distinctions among sessions, activities, newsletters, field trips, planned exposure, and delivered exposure are missing. The three descriptions must not be asserted to be the identical delivered component.
- **Duplicate/category check:** Not a duplicate of `C010`: `C010` is the internal visit-count identity, while `C012` compares control-exposure counts and durations. Category `Cross-document numeric inconsistency` is allowed.
- **Impact/report repair:** Frame the question as an unresolved mapping among plan versions/components and actual delivery. Bound reuse risk to extraction of the control exposure; do not allege protocol nonadherence or conclusion change. Include `N002`, `N047`, and repaired `N064` provenance.

## C013 — Control 9-month BMI-observation count differs across result displays

- **Evidence-quality result:** Supportable source-grounded candidate added through complete-coverage repair; **Pending Human Adjudication**.
- **Arithmetic and pagination:** DOC-001 Figure 1 p. 3 prints 282; DOC-001 Figure 2 p. 7 and DOC-003 eTable 1 p. 2 print 280. `282 - 280 = 2` is correct; pages and links resolve.
- **Missing definitions and unsupported assumptions:** Participant-level record reconciliation and post-collection inclusion rules are unavailable. A two-record exclusion is inferred only.
- **Duplicate/category check:** Distinct from `C003` because it is the control arm. Its later registration repaired an omission and did not duplicate, merge, or renumber any earlier ID. Category is allowed.
- **Impact/report repair:** Bound reuse risk to the control 9-month displayed denominator; do not infer model-result or paper-conclusion impact. Populate all required report fields.

## Human adjudication placeholder audit

Every final report card must contain the following exact blank template. No subfield may contain a dash, checkbox, AI disposition, or prefilled judgment.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Required coordinator repairs and limitations

1. Preserve the completed ledger wording repair: the grouped BMI-count record contains nine, not eight, distinct arm-by-time comparisons.
2. Preserve the completed `PN020`/`N064` repair across the fresh support map, canonical inventory, numeric checker, cross-source scope/count statement, coverage manifest, and `C010`/`C012` provenance.
3. After this artifact is accepted, set the `evidence_quality` coverage row to `COMPLETE`. After report assembly, enumerate `C001`-`C013` in the report-generation scope and set that row to `COMPLETE`.
4. Add the report generator and every later model/repair agent exactly once to `agent_execution_manifest.md` and to authoritative token accounting. Do not change the two distinct Terra/high statistical runtime IDs.
5. Generate all 13 report cards with every exact required label, rebased PDF links, conditional bounded downstream-impact statements, and the exact blank human-adjudication template.
6. Recompute final source hashes and verify them against the baseline; then render and validate until the versioned validator reports `PASS`.

Limitations are bounded to unavailable participant-level denominator reconciliation, incomplete protocol amendment/component mapping, missing primary-analysis variable history, missing full model details and moderator coding/centering, and unprinted figure coordinates. These limitations do not justify deleting or adjudicating any stable ID. No display-zero-only candidate, unsupported severity, unbounded downstream-impact claim, or paper-level conclusion-change claim was found in the reviewed candidate evidence.
