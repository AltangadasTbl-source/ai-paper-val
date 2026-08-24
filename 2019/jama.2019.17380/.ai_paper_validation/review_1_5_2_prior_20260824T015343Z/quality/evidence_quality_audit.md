# Final Evidence-Quality Audit

## Scope and evidence boundary

This final refresh audits all four direct sources, all 12 coverage-manifest rows, `N001`-`N066`,
`S001`-`S044`, both statistical passes, the complete stable ledger (`C001`, `C002`, `C003`, `C004`),
the complete mechanical recheck, `source_coverage.md`, `agent_execution_manifest.md`, and the current
`run_state.md`. It incorporates the completed quality-repair wave that registered and rechecked C002,
C003, and C004 without deleting, merging, suppressing, or renumbering C001.

Only supplied-package PDFs, fresh page-addressable Acrobat native text, and current workflow 1.5.2
artifacts were used. The audit did not use an old audit derivative, an old candidate set, the web,
external literature, a top-N rule, a desired count, or a review queue. All language below is neutral
quality control. Every C ID remains **Pending Human Adjudication**.

## Source and coverage audit

### Direct-source rows

| Source | Total | Reusable | Fresh-required | Mapped | Status | Fresh page markers | Current SHA-256 versus before |
|---|---:|---:|---:|---:|---|---:|---|
| DOC-001 `jama_de_boer_2019_oi_190122.pdf` | 11 | 0 | 11 | 11 | COMPLETE | 11 | Identical |
| DOC-002 `joi190122supp1_prod.pdf` | 33 | 0 | 33 | 33 | COMPLETE | 33 | Identical |
| DOC-003 `joi190122supp2_prod.pdf` | 19 | 0 | 19 | 19 | COMPLETE | 19 | Identical |
| DOC-004 `joi190122supp3_prod.pdf` | 1 | 0 | 1 | 1 | COMPLETE | 1 | Identical |

Result: 4/4 rows pass. The totals are 64 total units, 0 reusable units, 64 fresh-required units, and
64 mapped units. Thus `fresh-required = mapped = total` for every source. The 64 fresh page markers
reproduce the 11+33+19+1 inventory. Recomputed hashes match `source_hashes_before.sha256` for all four
sources. DOC-004's one stable page is consistently documented as the final catalog page rather than
three incremental revisions of the same page object.

The evidence-asset inventory truthfully records the absence of layout-preserving PDF extraction,
rendering, and usable CPU OCR in this environment. Fresh Acrobat native text is page-addressable for
all units. This establishes complete structural source coverage, while leaving the stated visual-layout
limitations for C001-C003 and graphical numeric checks.

### Coverage-manifest rows

| Stage | Scope check | Artifact-cell check | Status at audit refresh | Audit result |
|---|---|---|---|---|
| source_inventory | DOC-001 through DOC-004 | One plain path | COMPLETE | Complete |
| evidence_assets | All 64 source pages | One plain path | COMPLETE | Complete |
| main_evidence_mapping | DOC-001 pp.1-11 | One plain path | COMPLETE | Complete |
| support_evidence_mapping | DOC-002 pp.1-33; DOC-003 pp.1-19; DOC-004 p.1 | One plain path | COMPLETE | Complete |
| numeric_checks | Every ID N001-N066 individually enumerated | One plain path | COMPLETE | Complete after C002-C004 repair |
| statistics_pass_1 | Every ID S001-S044 individually enumerated | One plain path | COMPLETE | Complete |
| cross_source_checks | All N and S relationships across DOC-001-DOC-004 | One plain path | COMPLETE | Structurally complete; remaining durable-artifact refresh noted below |
| candidate_registration | C001, C002, C003, C004 | One plain path | COMPLETE | Complete |
| evidence_recheck | C001, C002, C003, C004 | One plain path | COMPLETE | Complete |
| statistics_pass_2 | Every S ID, all four C IDs, and all recheck facts | One plain path | IN_PROGRESS | Artifact work is complete; manifest status needs coordinator finalization |
| evidence_quality | All four C IDs and every coverage/source row | One plain path | IN_PROGRESS | Completed by this refreshed artifact; manifest status needs coordinator finalization |
| report_generation | C001, C002, C003, C004 | One plain path | PENDING | Correct pre-report state |

All 12 required stages occur. Every row has exactly one undecorated POSIX-style relative artifact path.
All artifacts marked complete resolve locally. The pending final report does not yet exist, consistent
with its status. Candidate-stage scopes enumerate all four IDs rather than using a range.

## Relationship and statistical-execution audit

| Record set | Required set | Found | Missing/duplicate IDs | Result |
|---|---|---:|---|---|
| Numeric inventory | N001-N066 | 66 | None | Complete |
| Numeric checker | N001-N066 | 66 | None | Complete after repaired N031 and N059 |
| Statistical inventory | S001-S044 | 44 | None | Complete |
| Statistical pass 1 | S001-S044 | 44 explicit `PASS_1_COMPLETE` records | None | Complete |
| Statistical pass 2 | S001-S044 | 44 explicit `PASS_2_COMPLETE` records | None | Complete |
| Stable ledger | C001-C004 | 4 | None | Complete |
| Mechanical recheck | C001-C004 | 4 | None | Complete |
| Quality audit | C001-C004 | 4 headings below | None | Complete |

The repaired numeric checker now records three distinct qualifying proposals linked to C002-C004:
two separate N031 endpoint/count relationships and one N059 analysis-population relationship. It no
longer treats agreement of combined totals as proof that treatment-specific allocations agree, and it
explicitly reproduces the 944-versus-991 N059 difference.

Statistical pass 1 and pass 2 use distinct runtime IDs, `/root/statistics_pass_1` and
`/root/statistics_pass_2`. Both manifest rows record model `gpt-5.6-terra`, reasoning effort `high`,
start mode `FRESH_SPAWN`, and one canonical artifact. Pass 2 retains all 44 original S records and now
contains a repair addendum reviewing C001-C004 plus the updated recheck facts. It emits no duplicate
candidate and no new inferential candidate.

No mapped relationship displays `P = 0`, `p = 0.000`, or an equivalent display zero. No stable ID has
a display-zero basis, so no independent-contradiction conditional field is applicable. The relationship
counts and explicit per-ID records show no count cap, top-N boundary, or early stopping.

## Candidate-card quality audit

Each ledger record has an exact location, printed evidence and comparator, an applicable consistency
rule, a reproducible calculation or logical comparison, direct observation separated from inferred
explanation, a source-grounded alternative, necessary missing input/definition, an exact human
question, and bounded downstream relevance. Categories exactly follow `QUALITY_CONTROL_SCOPE.md`.

## C001 — eFigure 2 and eFigure 3 comparator wording conflicts with the active-versus-placebo contrast

- **Threshold and category:** Pass. `Measure, label, or scale inconsistency` is an allowed primary
  category. DOC-003 pp.18-19 print titles framed as active treatment `Versus Placebo` and captions
  saying `comparing the active treatment assignment to year 5`; DOC-003 p.11 and DOC-001 p.4 identify
  placebo as the comparison group.
- **Rule and reasoning:** Pass. The same sentence already identifies baseline-to-year-5 as the change
  window; a time point does not supply the control-group label for an active-versus-placebo effect.
  No arithmetic is required. The direct phrases are separated from the inference that placebo may
  have been intended.
- **Assumptions and limitation:** Supportable. The ledger and recheck do not assume a correction. They
  retain the possibility that non-layout extraction omitted or reordered a visual element and require
  rendered-page confirmation.
- **Location and link check:** Pass. DOC-003 pp.18, 19, and 11 and DOC-001 p.4 are true page-marked
  locations. All recheck links resolve and end in `#page=N`.
- **Duplicate check:** Pass. The two captions repeat the same statement, comparator rule, and change
  window. One C001 retains both occurrences. It is not duplicated by C002-C004.
- **Impact wording:** Pass. It states only what a data extractor could copy if confirmed and explicitly
  disclaims established propagation or conclusion change.
- **Remaining human question:** Does visual rendering confirm the caption phrase, and if so should the
  comparison-group wording identify placebo while preserving the baseline-to-year-5 window?

## C002 — Omega-3 eGFR panel repeats vitamin-D contributor counts instead of omega-3 allocation counts

- **Threshold and category:** Pass. `Denominator, proportion, or total inconsistency` is allowed.
  DOC-001 p.7 Figure 2 panel B and DOC-001 p.8 Table 2 are matched to the same omega-3/placebo eGFR
  endpoint and baseline/year-2/year-5 timepoints.
- **Arithmetic reproduced:** Panel B prints 701/607, 531/459, 496/438; Table 2 prints 657/651,
  499/491, 472/462. Combined totals agree at 1308, 990, and 934, while allocation differences are
  +44/-44, +32/-32, and +24/-24. Panel B's sequence equals vitamin-D panel A's sequence. No rounding
  rule can reconcile integer arm allocations.
- **Assumptions and limitation:** Supportable. Copying is only a possible explanation. The native text
  associates values with panel B, but the candidate retains visual-panel confirmation as a missing
  input because extraction is not layout-preserving.
- **Location and link check:** Pass. DOC-001 pp.7-8 are exact, and both recheck links resolve with
  `#page=7` and `#page=8`.
- **Duplicate check:** Pass. C002 concerns eGFR and Table 2. It is not merged with C003's ACR/eTable 6
  relationship merely because a copying mechanism might be shared.
- **Impact wording:** Pass. It is limited to possible copying of arm-specific contributor denominators
  if confirmed; no estimate or conclusion change is claimed.
- **Remaining human question:** Does the rendered panel B attach the repeated counts to omega-3 versus
  placebo, and if so what source-defined reason accounts for the Table 2 difference?

## C003 — Omega-3 urine-ACR panel repeats vitamin-D contributor counts instead of omega-3 allocation counts

- **Threshold and category:** Pass. `Denominator, proportion, or total inconsistency` is allowed.
  DOC-001 p.7 Figure 2 panel D and DOC-003 p.11 eTable 6 are matched to the same omega-3/placebo ACR
  endpoint and timepoints.
- **Arithmetic reproduced:** Panel D prints 702/609, 529/463, 505/440; eTable 6 prints 658/653,
  502/490, 478/467. Totals agree at 1311, 992, and 945, but allocation differences are +44/-44,
  +27/-27, and +27/-27. Panel D's sequence equals vitamin-D panel C's sequence.
- **Assumptions and limitation:** Supportable. No copying cause or correction is asserted. The required
  visual panel/count association remains explicit.
- **Location and link check:** Pass. DOC-001 p.7 and DOC-003 p.11 are exact; both recheck links resolve
  and end in page fragments.
- **Duplicate check:** Pass. Different endpoint, printed count set, and exact comparator source make
  C003 distinct from C002. It is also distinct from C001's caption label and C004's analysis N.
- **Impact wording:** Pass. Possible downstream copying is conditional and bounded; no actual reuse or
  conclusion effect is claimed.
- **Remaining human question:** Does the rendered panel D attach the repeated counts to omega-3 versus
  placebo, and if so what source-defined reason accounts for the eTable 6 difference?

## C004 — eTable 7 reports 944 analyzed participants but its footnote states that 991 were included

- **Threshold and category:** Pass. `Denominator, proportion, or total inconsistency` is allowed.
  DOC-003 p.12 contains the title, both factorial row totals, the attached asterisk, and the inclusion
  footnote.
- **Arithmetic reproduced:** 504+440=944; 477+467=944; 991+320+1=1312; 1311-320=991; and 991-944=47.
  The title and rows therefore identify 944, while the attached footnote says 991 `were included in
  this analysis`. No rounding issue exists.
- **Assumptions and limitation:** Supportable. The possibility that 47 donated sample pairs lacked
  usable ACR or another required input is clearly inferred, not supplied. The missing source-defined
  exclusion/population rule is named.
- **Location and link check:** Pass. DOC-003 p.12 is exact; its recheck link resolves and ends in
  `#page=12`.
- **Duplicate check:** Pass. C004 compares one table's title/rows to its attached footnote and is
  distinct from the figure allocation relationships.
- **Impact wording:** Pass. It only identifies a denominator an evidence extractor could copy if the
  issue is confirmed and does not claim estimate or conclusion impact.
- **Remaining human question:** Is the intended analysis population 944 or 991, and what exact
  availability or population rule accounts for the 47 participants?

### Required final-report card normalization

The ledger is a registration artifact rather than the final report card. It supplies the evidence
needed for all required report fields, but the report generator must use these exact labels on every
C001-C004 card: `Candidate statement`, `Category`, `Exact source locations`, `Source evidence`,
`Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded
interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream
evidence impact`, `Human verification steps`, and `Human adjudication fields`.

Every card must contain this exact blank template:

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

No C card mentions a display-zero P value, so the conditional `Independent contradiction beyond P=0
display` field is not required.

## Agent, run-state, and provenance audit

The agent manifest currently has ten unique rows: the coordinator, fresh preprocessor, two mappers,
numeric checker, cross-source checker, pass 1, rechecker, pass 2, and this quality auditor. Each has one
primary artifact. The coordinator occurs exactly once. Both required statistical agents are fresh,
distinct, Terra/high, and their artifacts cover 44/44 S relationships. Any future report generator or
new repair agent must be added exactly once before token accounting; every final manifested agent must
then have a token-ledger record.

`run_state.md` correctly records 64 total/fresh units, 45+21=66 numeric relationships, 25+19=44
statistical relationships, the three quality-repair registrations, preservation of C001, and pending
report/token/hash-finalization/rendering/validation work. Its package-specific 45-70 minute target is
bounded to the four-source extraction and relationship burden. `Finished UTC`, elapsed time, target
status, and exceedance causes correctly remain blank before complete report assembly.

The fresh-evidence declarations are mutually consistent across preprocessing, mappings, checkers,
recheck, and pass 2: old audit outputs and external sources were not evidence inputs. This audit can
confirm the documented evidence chain and local paths; it cannot reconstruct an independent process
transcript beyond those durable records. No artifact examined uses a legacy derivative as cited
scientific evidence.

## Repair resolution and remaining coordinator actions

The three scientific omissions found in the first audit are resolved in the durable ledger, repaired
numeric checker, mechanical recheck, and statistical-pass-2 addendum:

- N031 eGFR allocation omission -> C002, retained and rechecked.
- N031 ACR allocation omission -> separate C003, retained and rechecked.
- N059 944-versus-991 omission -> C004, retained and rechecked.

No additional stable candidate is supportable from the refreshed artifacts. No stable ID should be
deleted, merged, ranked, suppressed, or assigned a scientific disposition.

Concrete coordinator actions still required before report generation begins:

1. Refresh `checkers/cross_source_consistency.md` so its N031 matched-source discussion acknowledges
   C002 and C003 without duplicating them; its current zero-proposal narrative predates the quality
   repair and does not document the corrected group-allocation comparison.
2. Change the `statistics_pass_2` coverage row and run-state field from in-progress to complete now
   that the addendum covers C001-C004, and change `evidence_quality` to complete after accepting this
   artifact.
3. Ensure `run_state.md` describes the evidence-quality scope as C001-C004 rather than C001 only.
4. Generate the report with all four cards, exact page-fragment links, exact required labels, bounded
   impact language, and the five exact `__` placeholders per card. Add the report generator to the
   agent manifest if a new agent is used.

After report assembly, the coordinator must finalize timing, account for every manifested agent,
recompute source hashes, calculate token summaries, render standalone HTML, and validate. Those are
required later workflow stages rather than defects in this pre-report evidence audit.

## Final audit status

- **Source rows:** 4/4; 64/64 total units fresh-required and mapped; 0 reusable.
- **Coverage rows:** 12/12 audited; one artifact path per row.
- **Numeric relationships:** 66/66; repaired candidates C002-C004 retained.
- **Statistical relationships:** pass 1 44/44 and pass 2 44/44.
- **Stable IDs:** ledger = recheck = quality = `{C001, C002, C003, C004}`.
- **Candidate threshold/card audits:** 4/4 support all threshold elements; final report label/template
  normalization remains required.
- **Display-zero-only candidates:** 0.
- **Source links:** all recheck PDF targets resolve and all end in `#page=N`.
- **Scientific repair status:** complete; three discovered omissions registered and rechecked.
- **Remaining pre-report coordinator repairs:** four bounded synchronization/report-preparation actions
  above; no new scientific candidate registration required.
- **Go/no-go:** **NO-GO for report generation until actions 1-3 are completed; GO immediately afterward
  for four-card report generation under action 4.**
- **Primary artifact:** `quality/evidence_quality_audit.md`.
