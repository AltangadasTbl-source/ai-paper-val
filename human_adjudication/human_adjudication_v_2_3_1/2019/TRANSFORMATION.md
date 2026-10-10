# 2019 construction record — v.2.3.1

The user's latest scope instruction supersedes the original annual totals in WORKFLOW.md: the deliverables contain **9 papers and 62 candidates per independent reviewer**. Both files use precisely the same included candidates, in baseline order. No original paper package or other year folder was modified.

## Baseline and relocation

The historical v.2.1.5.3 directory referenced by the supplied preflight had been moved into `../../previous/archived_not_touch.zip`. Seven required baseline files were read from that archive and extracted only into this folder's `sources/human_adjudication_v_2_1_5_3/`. Each SHA-256 matches `baseline_inventory.json`; the archive hash is also recorded. The original archive is unchanged.

`preflight.py` was changed only to allow the local verified source copies when the original directory is absent. `baseline_inventory.current.json` matches the supplied historical inventory after normalizing source paths. Its original annual totals describe the historical input, not the reduced release. `source_hash_manifest.json` records original paths, archive members, local paths and hashes.

The baseline USAGE, DESIGN, VALIDATION, annual workbook, build.mjs, codebook.json and source catalog were inspected. The old builder was never executed. The Chinese PDF was not needed. Construction uses Python 3.12.3 and openpyxl 3.1.5 in `.venv`; all dependency versions are pinned in `requirements-construction.txt`.

## Transformation

- Apply the user-authorized subset to Papers, C_ sheets, Candidates, Evidence, Links, Relations and every result table. Source values of retained rows are unchanged and match the catalog subset exactly: 62 Candidates, 224 Evidence, 274 Links and 68 Relations rows.
- Construct R_A and R_B independently from the same blank baseline. Role-specific cells and formulas contain only that workbook's own role. Reviewer ID/name, dispositions and notes start blank; Complete starts `no`.
- Preserve A–C, suggested E, H–L default formulas, row order, navy headers, wrapped text, baseline freeze panes and common/optional colors. E explicitly identifies its AI suggestion. Widen E, G and L and increase some candidate-row heights using a conservative text-wrap estimate. This is not a rendered Excel layout test.
- Keep the original 18-column positions. Remove all content, dropdowns, formulas and workflow labels from M–Q; hide them at width 2. R remains the editable notes field. Use an AutoFilter across complete A:R rows, rather than tables requiring nonblank spacer headers.
- Remove Primary_snapshot and replace Setup, Start, Checks and result sheets. Remove obsolete workflow names, formulas, validations and Codebook sections. Preserve all primary methodological option definitions verbatim. New schema: `xlsx-adjudication-independent-primary-2.3.1`.
- G validates ID (including ordinary spaces, tabs/newlines and nonbreaking spaces), own role/year, candidate identity, completion option, D/E, active required/optional judgments and stale inactive values. Exact code checks also reject uppercase/padded pasted codes. Effective result fields normalize inactive inputs only after readiness can flag stale inputs.
- Decisions uses internal INDEX/MATCH by candidate key, including one-cell lookup ranges. Outcomes are blank for unfinished or discuss rows. P_R/P_P precede domain eligibility and remain descriptive. S_C/S_W substantive confirmed/probable statistical findings are primary_temporal; substantive report-internal inconsistencies are secondary_temporal. Other ready non-discuss records are not_eligible. Indeterminate judgments follow baseline eligibility and do not imply absence of error.
- Paper_counts separates entry completion, unfinished rows and unresolved/discuss count. Outcome counts remain blank until every paper row is primary-ready and none is discuss. This is the explicit independent-review adaptation of the old outcome gate. A reviewer may finish with unresolved discuss responses.
- Add internal navigation and clickable original-document targets without changing source href cell text. All targets are checked from the actual output location. The six jama.2019.14901 candidates have no Evidence rows or statement/location text in the baseline; their embedded rationale/ambiguity is preserved, candidate keys open Candidates, and reportHref opens the original report. No source text was invented.
- Protection ranges: **none**. Rule_defaults is a visible, unprotected reference. All serialized cell style XFs and normal cell XFs explicitly contain locked=0 and hidden=0, including the default style for unused cells. No passwords, sheet protection or workbook structure protection.
- Normal internal Excel formulas, dropdowns and conditional formatting implement review-time logic. Calculation is automatic with full recalculation on opening. There are no external workbook formulas, macros, connections, queries or registered automation.

## Construction and release safeguards

The builder resolves paths from its own directory, refuses other years, refuses output outside this folder, refuses direct release writes and refuses existing workbook outputs. Once either release workbook exists, the builder refuses any further build for this version. Corrections require a separately named new version and review of the changes.

Only clean staging templates are promoted to release. Synthetic answers and interpreter values exports are confined to `tests/`. A Python formula interpreter is used solely for construction tests; no reviewer installs or runs it. Full Excel calculation/rendering and the interactive reviewer smoke test remain pending. See VALIDATION.md.
