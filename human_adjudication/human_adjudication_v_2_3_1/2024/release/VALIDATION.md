# Validation — 2024 v.2.3.1

Construction completed 2026-09-18. **Static validation passed; full Excel validation remains pending.** Exactly two clean primary-review templates are in `release/`. No human or synthetic judgments are present in them.

## Checks actually executed

- Read-only preflight exactly matched the supplied inventory and all seven source hashes. Both files contain 10 paper sheets and 91 unique candidates in baseline order. Candidates (91), Evidence (364), Links (357) and Relations (107) match the annual baseline and catalog subset cell-for-cell. Source hashes remained unchanged after validation.
- `release/validation_report.json` records **228 passed checks, zero failures**. This includes source equality, blank reviewer inputs, identical role templates except three role-label cells, formula/reference inspection, protection, navigation and bounded formula regression probes. Four additional builder refusal tests passed; see `tests/builder_guard_report.json`.
- Per workbook, all 640 hyperlinks and 1,835 formulas were inspected (maximum formula length: 1,791 characters). All internal hyperlinks and original source-file hyperlinks resolve at the **final release location**. Source href text is preserved, with separately rebased hyperlink targets. Formula names/references and Excel length limits were inspected; no external workbook links, macros, queries, connections, cached error cells or legacy workflow logic were found. Historic source paths containing “checkers” are unchanged evidence references, not runtime logic.
- Every serialized cell style, including the default and named styles, has locked=0 and hidden=0. All human inputs and unused cells remain editable. No sheet protection, password, hidden formulas or workbook structure lock. **Protected ranges: none.** Rule_defaults is an unprotected applicability reference.
- The local construction-only formula probe traversed every formula in blank and all-complete templates. Regression cases cover all four domains, untouched defaults, required/optional values, invalid pasted values, inactive stale values, domain/disposition changes, optional clearing, exclude, discuss, empty/whitespace identity, invalid completion flags including checker_done, manual reset, duplicate/missing/foreign-paper keys, relationship precedence and unfinished outcomes.
- Synthetic all-paper completion yielded 91 ready rows and reconciled all ten paper totals: 45 primary_temporal, 29 secondary_temporal, 11 protocol_descriptive and 6 plan_descriptive. **These are artificial regression data, not research findings.** Additional cases checked not_eligible, minor/indeterminate findings, discuss as ready but unresolved, withheld paper counts, key matching after whole-row reorder and a one-candidate fixture. The single-candidate fixture uses artificial 2024 data; no other year's release was touched.
- Synthetic copies were saved/reopened through openpyxl, and their formulas were re-probed. Editing a test copy of R_A left R_B's bytes and blank identity unchanged. Clean final templates were reopened and revalidated. Builder refusals were exercised for another year, existing workbooks, the release directory and an outside-year directory.

## Tools and limits

Python 3.12.3, openpyxl 3.1.5 and et_xmlfile 2.0.0 were used only for construction/validation. Versions are recorded in `requirements-construction.txt`. openpyxl does **not** evaluate formulas. `tests/formula_probe.py` is a deliberately bounded interpreter of the generated formula subset: its passing assertions do not establish Excel compatibility, caching, UI behavior, sorting semantics or rendering. No cached calculation values were treated as proof of recalculation.

The following are **NOT RUN** because no desktop Excel or compatible calculation/rendering executable was available:

- Excel/compatible-engine recalculation of test workbooks and inspection of saved/reopened calculated caches.
- Interactive Excel reviewer smoke test, including real whole-row sorting and save/close/reopen.
- Rendered comparison with baseline previews, text-clipping checks and dropdown usability at ordinary zoom.

The templates therefore are **not claimed fully validated**. No engine-converted artifacts were released. Static dimensions, wrapped text, fills, conditional-format rules and freeze panes were checked; this is not a visual rendering check.

## Exact pending manual Excel checks

Use disposable copies of each template in the same release folder; never put test answers in the templates. All actions below are performed entirely in Excel.

1. Open a copy in desktop Excel. Confirm no repair warning, external-workbook update prompt or macro requirement. Confirm Formulas → Calculation Options → Automatic. Before identity/answers, Checks should show 91 candidates, 0 ready, 91 unfinished, 0 discuss and ACTION NEEDED. Enter a unique test ID in Setup B2. Spaces alone must not satisfy identity; then restore a real test ID.
2. Complete one representative row per domain using D=retain and F=primary_done after answering:

   | Sheet / row | Domain | Answers | Expected G / outcome |
   |---|---|---|---|
   | C_jama.2024.0318 row 2 | statistical_results | H=confirmed_issue, I=substantive, J blank | PRIMARY READY / primary_temporal |
   | C_jama.2024.0318 row 3 | report_internal_inconsistency | K=substantive_inconsistency | PRIMARY READY / secondary_temporal |
   | C_jama.2024.11057 row 2 | protocol_report | L blank | PRIMARY READY / protocol_descriptive |
   | C_jama.2024.12829 row 11 | plan_material | K=substantive_inconsistency | PRIMARY READY / plan_descriptive |

   Preserve the suggested domain in these examples. The untouched inactive formulas should display not_applicable; no unlock step may be needed. Checks should now show 4 ready and 87 unfinished. Paper outcome counts remain blank where other rows are unfinished.
3. On statistical row 2, set F=no before changing E to protocol_report. The old H/I answers must remain visible and G must request CLEAR INACTIVE VALUES. Clear H/I, leave L blank, review and set F=primary_done. G must return PRIMARY READY. Because this candidate's relationship remains S_W, its outcome becomes not_eligible; changing a domain must not change a frozen relationship code.
4. Reset F=no; return E to statistical_results and enter H=probable_issue, I=substantive, J=possible. Complete, then reset F and clear J. Recomplete: G remains PRIMARY READY and the effective downstream-impact result is blank. Set active J=not_applicable: G must show CHECK FIELDS. Clear J again. Paste an invalid H value (paste can bypass validation): G must reject it. Restore H.
5. Reset F=no and choose D=exclude without clearing H/I: G must request CLEAR INACTIVE VALUES. Clear H/I, complete: outcome not_eligible. Change to discuss through the manual-reset sequence: row remains PRIMARY READY, outcome blank and discuss count rises. Blank or invalid E must prevent completion even for exclude/discuss. Pasted F=checker_done must be rejected by G.
6. Use a separate disposable copy of `tests/all_primary_complete.xlsx` for an all-paper calculation test; its inputs are visibly synthetic. Press Ctrl+Alt+F9. Expect 91 ready, 0 unfinished, 0 discuss, PRIMARY READY, all paper gates yes, and the synthetic totals reported above. Change one complete row to discuss after clearing inactive answers: ready stays 91, discuss becomes 1, that paper remains primary_complete=yes but outcomes_available=no and all five outcome counts become blank. Set F=no: ready falls to 90 and that paper is no longer complete.
7. On disposable copies, sort one C_ sheet using its AutoFilter across **entire A:R rows**. Confirm key-associated notes, assessments, Decisions results and Protocol_plan_table remain aligned. Open `tests/single_candidate.xlsx` and confirm Decisions G2=PRIMARY READY after recalculation. Temporarily duplicate or clear a candidate key in a full copy: G and the missing candidate's Decisions status must block readiness. Undo afterward.
8. Check Papers navigation, Candidate-key evidence navigation and at least one PDF link at the final folder location. Inspect Start, Codebook, all primary input columns and results at normal zoom. Confirm full instructions/options are readable; expand row heights if needed for lengthy preserved evidence. Check yellow required/common, blue optional and gray inactive formatting after domain changes. Confirm M–Q contain no values and reviewer notes remain in R.
9. Save, close and reopen each test copy. Verify ID, answers, readiness, discuss count and results persist and recalculate without any terminal or external process. Record Excel version, date, files tested, actual observations and any failures. Keep the release templates blank. These results have not yet been recorded.

## Construction records

`source_hash_manifest.json`, `release/output_hashes.json`, `release/validation_report.json`, `TRANSFORMATION.md`, `requirements-construction.txt`, local builder/validator and `tests/` retain the evidence. To reproduce construction checks only:

```text
.venv/bin/python validate_v_2_3_1.py --year 2024 --input-dir release
```

That command writes construction reports and synthetic test copies only. It is **not** a reviewer step. The builder must use a fresh local staging directory and refuses release targets or workbook overwrites. Settled reviews are edited, saved and delivered in Excel; no build, snapshot, synchronization or export process is required.
