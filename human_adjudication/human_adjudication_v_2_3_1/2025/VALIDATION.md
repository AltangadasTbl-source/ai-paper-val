# v.2.3.1 — 2025 construction validation

Validated 2026-09-18. Executed checks passed: 94 static assertions per validation run and 88 functional assertions; final-location static validation passed for both files. Four builder refusal tests also passed.

Validation scope: two independent primary-review templates, 15 papers and 131 candidates each. Construction uses Python 3.12.3, openpyxl 3.1.5 and formulas 1.3.4 in the local `.venv`; exact installed versions are in `requirements-construction.txt`. These packages are not review-time dependencies.

Desktop Excel smoke testing and visual rendering are **NOT RUN**. No desktop Excel or LibreOffice executable is available. The compatible `formulas` evaluator tests actual workbook formulas, but does not establish Excel UI behavior or exact compatibility. The templates require Excel's normal automatic recalculation on opening. No Python step is needed by a reviewer.

## Executed checks

Machine-readable results are recorded in `validation_report.json` (staging static and functional checks) and `validation_report.release.json` (final-location static checks). `tests/validation.log` records the functional run. `output_hash_manifest.json` identifies the released bytes.

- The supplied preflight was run; `baseline_inventory.current.json` is byte-for-byte identical to `baseline_inventory.json`. All seven inventoried source hashes were checked before construction and after validation. The annual cohort includes papers with 2024 DOI names; membership follows the 2025 annual baseline.
- Both roles have the same source content, candidate order, relationship codes and AI suggestions. Candidates, Evidence, Links and Relations match both the annual workbook and the annual subset of the immutable catalog cell-for-cell. Human dispositions, notes and identity begin blank; F begins `no`; the baseline H–L default formulas are preserved.
- Roles differ only in Start B2, Setup B4 and Manifest B5. Saving an edited A test copy leaves B unchanged. Both files have independent internal formulas and no references to one another.
- No snapshot, second-review logic, stage selector, external workbook links, macros, queries, connections, stale names, invalid references or cached error cells were found. Formula lengths, dropdown codes, source links, navigation, editable input styles and automatic recalculation settings were inspected.
- Synthetic calculations exercise every domain; required and optional answers, missing/invalid/pasted values, inactive stale values, domain/disposition changes, optional clearing, completion reset, forbidden completion values, duplicate/missing keys, blank/spaces/tab/newline/nonbreaking-space identity, exclude, discuss and all outcome branches. `tests/cases.json` identifies row-level expectations.
- Actual default formulas are evaluated across blank/retain dispositions in all four domains and exclude/discuss branches. Effective inactive results normalize to `not_applicable`; stale input still blocks readiness. A supplemental inspection of the saved engine-calculated test copy verifies every inactive effective judgment (see `tests/supplemental_checks.json`).
- A fully completed synthetic annual review verifies all 131 ready rows, all 15 completed papers, and all paper outcome totals: 50 primary temporal, 43 secondary temporal, 15 protocol descriptive, 23 plan descriptive. These are synthetic validation counts, **not research findings**.
- Reversed complete C_ records retain correct key-to-assessment, note and outcome mappings for all 131 candidates. The test translates same-row formula references to simulate Excel whole-record sorting; actual Excel sorting remains part of the manual smoke test below.
- A separate all-ready fixture with one discuss response confirms PRIMARY READY can coexist with unresolved uncertainty. The actual one-candidate paper remains independently complete while its outcome counts stay blank.
- Engine-calculated results were inserted as formula caches into a TEST-only copy, saved and reopened with openpyxl. Cached values and retained formulas were checked. This was not an Excel save/reopen operation, and loading `data_only=True` alone was not used as proof of calculation.

## Protection and layout

**Protected ranges: NONE.** This is permitted by the optional limited-protection policy. Every cell style, including the default style for unused cells, is explicitly unlocked and has visible formulas. No worksheet protection, workbook structure lock or password exists. Rule_defaults is a visible, unprotected applicability reference. D/E/F/H–L/R and Setup B2:B3 remain editable throughout review.

Baseline navy headers, wrapped text, freeze panes, yellow common/required fields, blue optional fields and conditional gray inactive fields are retained. E/H/K/L are widened for option codes. M–Q are blank, narrow and hidden. C_ sheets use whole-record AutoFilters instead of structured tables so spacer headers remain genuinely blank. These properties were inspected structurally; visual clipping, dropdown display and Excel rendering have not been verified.

Source href cell text is unchanged for auditability. The clickable hyperlink relationships are rebased to the deeper output directory. File targets and internal destinations are checked again from `release/`. PDF page fragments are retained from the baseline; actual PDF viewer navigation was not exercised. Embedded evidence and source text remain available even when original documents are not distributed with a workbook.

## Pending manual Excel smoke test

Perform these checks on Save As test copies of each role template; never enter synthetic data into the release originals.

1. Open a copy in desktop Excel. Confirm no repair warning or external-update prompt, normal automatic calculation, readable Start instructions, and working Papers → C_ → Evidence navigation. Open a PDF via Links. Check widths, wrapped content, dropdown visibility and yellow/blue/gray formatting.
2. In Setup B2 enter your test identity. On an S_C or S_W row set D=retain, E=statistical_results, H=confirmed_issue, I=substantive; leave J blank. Mark F=primary_done. Expect G=PRIMARY READY, the ready count to increase, and the key-matched Decisions outcome to be primary_temporal. J=not_applicable must produce CHECK FIELDS; clearing J must restore readiness.
3. Reset F=no before editing. Change E to report_internal_inconsistency while H/I are literal answers. Expect CLEAR INACTIVE VALUES. Clear H/I, set K=substantive_inconsistency and re-mark primary_done. Expect secondary_temporal for S_C/S_W. Repeat with plan_material: K is required. On a P_P row a retained assessment yields plan_descriptive.
4. Use a P_R row with E=protocol_report, D=retain and L blank. Clear any inactive literals and mark primary_done. Expect PRIMARY READY and protocol_descriptive. Try L=version_timing, then clear it; both are valid. Retained P_R/P_P rows must remain descriptive even if E is changed to statistical_results and H/I are valid substantive issue answers.
5. Reset F=no and change a completed row to exclude, then discuss. Clear stale H–L values; E remains required. Exclude yields not_eligible. Discuss is PRIMARY READY with a blank outcome and increments the unresolved count. Its paper's outcome counts remain blank. Inspect `tests/TEST_sorted_and_discuss.xlsx` as a clearly synthetic all-ready example: Checks is PRIMARY READY, one discuss remains, and the one-candidate paper has independent completion=yes but counts available=no.
6. Paste an invalid option or completion value (bypassing the dropdown): expect CHECK FIELDS or CHECK COMPLETE. Enter only spaces in Setup B2: expect CHECK REVIEWER ID. On a disposable copy duplicate a candidate key, then delete one: expect CHECK KEY and affected records not ready. Undo these key edits.
7. On a disposable copy, use the C_ filter to sort complete A:R records. Confirm Decisions retains the correct key, notes and outcome. Verify the one-candidate paper too. Do not sort only one column. Open `tests/TEST_all_complete.xlsx` to inspect the full synthetic count reconciliation if desired.
8. Confirm inputs are editable without any unlock step, including changing domain on a completed row. Reset F=no manually before changes and re-review; verify that Excel does not automatically reset completion. Save, close and reopen the copy; verify inputs persist and G/Checks/results recalculate without running any script.
9. Repeat the basic identity/entry/save/reopen checks in a separate B copy. Do not transfer judgments between reviewers. Record Excel version, operating system, date, tester, observed results and any defects before calling the templates fully verified in desktop Excel.

## Construction boundaries

The scripts accept only 2025; the builder refuses release paths, paths outside this folder and existing output workbooks. Construction temporaries are configured under `.tmp/`. Synthetic workbooks are confined to `tests/`; release templates contain no synthetic judgments. Sources and other years are unchanged. No runtime script, scheduled task, watch process, refresh service or export command is part of review. Future corrections require a separately named new version and review of changes.
