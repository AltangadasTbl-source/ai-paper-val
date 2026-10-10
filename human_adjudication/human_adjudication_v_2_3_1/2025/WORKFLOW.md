# v.2.3.1 construction workflow — 2025

This is the complete task specification for a fresh Codex session opened in this directory. Build only the 2025 release: **15 papers, 131 candidate keys, two independent primary-review workbooks, R_A and R_B**. The user chose v.2.1.5.3 for its primary-check format and steps. Construction and validation may use Python; after release, every review action, check, calculation and delivery must work in Excel alone.

## 1. Scope and independence

- Create `release/human_adjudication_v_2_3_1_2025_R_A.xlsx` and `release/human_adjudication_v_2_3_1_2025_R_B.xlsx`. Separate files are intentional: hiding another reviewer's sheet in one workbook does not provide independent review.
- Both reviewers perform the full primary check of the same frozen candidates and evidence. Neither reviewer starts from, sees, imports, or depends on the other's judgments, completion flags, comments or summaries. Construct both blank templates before review begins, from the same baseline.
- R_A and R_B are role labels, not actual person IDs. Each reviewer enters their own ID/name. Tell the coordinator in the workbook instructions to assign two different people and distribute only the corresponding file. A standalone file cannot verify the other person's ID without exchanging data; do not invent such a gate.
- No primary-to-checker handoff, frozen snapshot, checker mode, agreement/disagreement entry, joint resolution, comparison dashboard, consensus result, or third review. `discuss` remains an independent primary-review response; it does not initiate a shared discussion workflow.
- Keep existing sources and every other year unchanged. All generated code, temporary files, environments and outputs belong to this year folder. No shared `/tmp/export.xlsx`, common build directory or cross-year output. Do not run old builders: they can build multiple years and restore the old handoff.
- Work locally with a single agent by default. No delegated work is needed. Finish this year's construction and report validation honestly; do not ask for routine implementation confirmations.

## 2. Read the actual baseline first

Repository root: `/home/juliz/ai-paper-val`.
Baseline directory: `../../../human_adjudication/previous/human_adjudication_v_2_1_5_3/` relative to this folder.

Read these files; do not substitute v.2.1.5.4 or v.2.2.1:

1. `USAGE.md`, `DESIGN.md`, `VALIDATION.md`.
2. `human_adjudication_v_2_1_5_3_2025.xlsx`: actual layout, widths, wrapped text, freeze panes, colors, dropdowns, conditional formatting, formulas, links and source sheets.
3. `maintenance/build.mjs` and `maintenance/codebook.json`: primary rules, meanings, applicability and original defaults. They are references; implement the new release with construction-only Python.
4. `resources/source_catalog_v_2_1_5_3.xlsx`: immutable candidate/source reference. Include this year's needed source material inside each review workbook; no external workbook links or refresh dependencies.
5. The Chinese step-by-step PDF may clarify the preferred primary workflow, but its checker instructions are obsolete for this task.

Run the supplied read-only inspection tool:

```bash
python3 preflight.py > baseline_inventory.current.json
```

Compare with the supplied `baseline_inventory.json`. Investigate source hash or total differences before building. The preflight uses only the Python standard library; it inventories the source, not the new release. Confirm 15 `C_` paper sheets and 131 unique keys. Do not infer annual membership from a DOI's year: the annual baseline defines the cohort.

## 3. Construction tools and artifacts

Start by checking available tools (`python3 --version`, Python import probes, and `command -v libreoffice`). This environment had `python3`, but neither `python` nor `openpyxl` nor a LibreOffice executable was available when these instructions were prepared; recheck rather than assume.

If needed, create a local environment and install construction dependencies, using the environment's normal network/approval mechanism if required:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install openpyxl
```

Do not modify the global Python environment. If installation is unavailable, use an available spreadsheet tool or carefully scoped Python `zipfile`/`xml.etree.ElementTree` OOXML editing. Report the actual tool used. Do not merely rename/copy the old workbook and claim the new workflow is implemented.

Implement local `build_v_2_3_1.py` and `validate_v_2_3_1.py`, a dependency record, and the validation cases below. Suggested stable interfaces to implement (these scripts do not exist yet):

```bash
.venv/bin/python build_v_2_3_1.py --year 2025 --output-dir staging
.venv/bin/python validate_v_2_3_1.py --year 2025 --input-dir staging
```

If using standard-library tools instead, use `python3` consistently and document the change. The builder must refuse any year other than 2025, resolve paths from its own location, and never overwrite a released workbook. Build in `staging/`; keep synthetic examples in `tests/`. Keep a source hash manifest and a transformation record so the changes are auditable.

## 4. Preserve the primary-review experience

Retain the 18-column `C_` layout, including original field meanings and row order:

| Column | v.2.3.1 behavior |
|---|---|
| A–C | Candidate key, title, source location; preserve baseline contents. |
| D | Disposition: `retain`, `exclude`, `discuss`; initially blank. |
| E | Review domain: retain the baseline AI-suggested default, visibly a suggestion and editable. |
| F | Complete: only `no`, `primary_done`; initially `no` or blank as documented. |
| G | Excel-calculated validation hint for this reviewer only. |
| H | Statistical/numerical issue judgment. |
| I | Substantiveness. |
| J | Optional downstream impact. |
| K | Report-internal or planning-material inconsistency. |
| L | Optional protocol interpretation. |
| M–Q | Blank, narrow spacer columns with no legacy labels, formulas, dropdowns or required inputs. Preserve positions so notes remain in R. These may be hidden for readability; they must contain no other reviewer's information. |
| R | Optional English notes, editable. |

Preserve English workbook content, the familiar navy headers, wrapped text, yellow common/required fields, blue optional fields and gray inactive fields. Preserve navigation from Papers to C_ sheets and candidate-key navigation to evidence. Any source hyperlink must be adjusted for the deeper output directory and checked at the final release location. References to original PDFs are allowed; formulas must not depend on another file, and structured evidence/source text must be embedded.

Keep `Start`, `Setup`, `Checks`, `Papers`, C_ sheets, `Candidates`, `Evidence`, `Links`, `Relations`, `Codebook`, `Manifest` and self-contained result sheets. Remove `Primary_snapshot` entirely. Rewrite `Decisions`, `Paper_counts` and `Protocol_plan_table` for one reviewer's primary assessment, without checker/consensus/initial-versus-final columns. Remove stale named ranges, formulas, validations and instructions. Setup contains this file's role, reviewer ID/name and year; no checker identity or stage switch. Use a new v.2.3.1 schema identifier and document the columns.

Each workbook's Start sheet must explain: Save As a working copy → enter own identity → use Papers/Candidates/Evidence → choose D, confirm E, answer applicable H–L, add R if needed → set F=primary_done after manual review → inspect G and Checks → save completed workbook and deliver this file. Changing an already completed row requires manually resetting F to no, reviewing again, then marking primary_done. Excel formulas cannot automatically erase an entered completion flag.

## 5. Primary rules and defaults

Preserve the baseline option meanings and option codes, including `not_applicable` for inactive judgments. Copy definitions from the baseline Codebook and remove only obsolete checker material.

| D=retain and E | Required | Optional | Inactive |
|---|---|---|---|
| statistical_results | H and I | J | K and L |
| report_internal_inconsistency | K | None | H, I, J, L |
| plan_material | K | None | H, I, J, L |
| protocol_report | No additional judgment | L | H, I, J, K |

- H options: `confirmed_issue`, `probable_issue`, `not_issue`, `indeterminate`.
- I: `substantive`, `minor_presentation`, `indeterminate`.
- J: `direct`, `possible`, `unlikely`, `unknown`.
- K: `substantive_inconsistency`, `minor_presentation`, `non_inconsistency`, `indeterminate`.
- L: `substantive_difference`, `minor_presentation`, `version_timing`, `non_inconsistency`, `indeterminate`.
- D and a valid E are required for completion, including exclude/discuss. H–L judgments are active only for retain; exclude/discuss must not leave stale substantive judgments in those cells.
- The baseline's untouched H–L formulas show blank for a potentially applicable field while D is blank or retain, otherwise `not_applicable`. Selecting a judgment overwrites that input formula. Preserve this behavior and explain it. A blank is blank, never an inherited reviewer answer. Domain/disposition changes do not automatically erase literal answers.
- In effective results, normalize inactive fields to `not_applicable`. But first flag any stale, nonblank, non-not_applicable inactive input as `CLEAR INACTIVE VALUES`; never silently hide a stale judgment and call it complete.
- Required active judgments cannot be blank or not_applicable. Optional active judgments may be blank but must use a valid option if populated; not_applicable is not a valid active answer.
- G must catch missing/whitespace identity, invalid options including pasted values, duplicate/missing keys, missing required judgments, stale inactive values and invalid completion flags. A dropdown alone cannot validate pasted input. Ready requires valid fields and `primary_done`.
- Preserve `discuss` as a completed primary assessment when otherwise valid, matching v.2.1.5.3 primary behavior. Show the discuss/unresolved total prominently; distinguish completion of independent data entry from resolution of scientific uncertainty. No consensus is required to complete this task.

## 6. Narrow protection policy

The inspected v.2.1.5.3 files are entirely unprotected; do not claim they already contained locks. The user's v.2.3.1 instruction permits locks only in areas holding rule-derived defaults, not general worksheet/output/formula protection.

- Explicitly unlock all cell styles and cells by default, including unused cells. No workbook-structure lock, encryption, password or runtime unlock step.
- D/E/F/H–L/R and identity/name inputs remain editable throughout review. E is an editable suggested domain, not a locked decision. Never lock H–L merely because their initial formula currently displays not_applicable: the domain can change.
- Use a small, visible `Rule_defaults` reference area for the fixed applicability table and default value `not_applicable` if protection is useful. Only this documented fixed rule area may be protected, without a password. List every protected range and its source rule in Manifest and validation; protection is an accidental-edit guard, not security. All other cells on that sheet must remain unlocked. No broad locking of source tables, calculated results, candidate IDs or validation formulas.
- Cell protection cannot follow a formula's result or conditional formatting in macro-free Excel. Do not introduce VBA, Office Scripts, Python hooks or stage locks to simulate dynamic protection. The primary judgment inputs stay editable; conditional formatting and readiness formulas enforce applicability.

## 7. Excel-native results

Build all review-time logic as normal internal Excel formulas, dropdowns and conditional formatting. Use robust candidate-key lookups rather than relying on matching row positions across sheets; test whole-row sorting and the single-candidate case. Avoid volatile/external/dynamic service dependencies. Set calculation mode to automatic, full recalculation on opening, and check formula lengths against Excel limits.

`Decisions` includes year, paper, candidate key, relationship, reviewer role/ID, readiness, effective assessment, notes and reviewer-specific outcome. Outcomes remain blank for unfinished records. Preserve substantive eligibility rules from v.2.1.5.3:

- A ready retained P_R/P_P record yields protocol_descriptive/plan_descriptive; these never enter temporal comparisons.
- Ready retained S_C/S_W statistical findings with confirmed_issue/probable_issue and substantive yield primary_temporal.
- Ready retained report-internal substantive_inconsistency findings yield secondary_temporal, subject to the same baseline relationship precedence.
- Other ready determinate records are not_eligible. A discuss response is explicitly unresolved, not a confirmed absence of error; keep its outcome blank and count it separately.

`Paper_counts` withholds outcome counts until all the paper's rows are primary-ready **and none is discuss**. Display independent review completion and unresolved count separately. This avoids treating uncertainty as zero while allowing both primary reviews to finish without reconciliation. This is an explicit v.2.3.1 adaptation of the old final-result gate; document it in the workbook.

`Protocol_plan_table` retains P_R/P_P source descriptions and this reviewer's judgments/status. Checks summarizes total, ready, unfinished and discuss counts, with PRIMARY READY only when every row passes primary checks. It never reports a shared FINAL READY or a consensus result. Neither workbook contains or links to the other reviewer.

## 8. Construction-time validation

Create validation reports, not just successful saves. Run synthetic scenarios only on temporary copies, never in the deliverable templates.

1. Totals: 15 papers and 131 unique keys per role, same keys/order/source text in both. Compare Candidates/Evidence/Links/Relations cell values with the annual baseline; preserve relationship codes and AI suggestions exactly. No human answers imported; D/R and reviewer identity blank, F not done, and no synthetic answers in release.
2. Independence: both roles start from blank primary assessments; editing A does not change B. Neither XLSX has external workbook links, queries, connections, macros, the other role's assessments, Primary_snapshot, checker logic or a stage switch. Result columns and instructions match the new workflow.
3. Primary cases: each retained domain; required/optional missing and invalid values; exclude; discuss; empty and whitespace identity; invalid pasted values; inactive stale answers; domain/disposition changes; optional clearing; completion reset; forbidden checker_done; duplicate and missing keys.
4. Outcomes: confirmed/probable substantive statistical, minor and indeterminate cases, substantive internal inconsistency, P_R/P_P precedence, excluded/not eligible, unfinished blank outcomes, discuss counted separately, and paper counts gated as specified. Test all-paper completion and totals for this year.
5. Layout/key cases: whole-row reordering still maps the right candidate; include a one-candidate fixture (the 2025 baseline itself has one); no broken references/names/hyperlinks, formula error values, truncated instructions or unreadable dropdowns. Check primary columns against baseline screenshots/previews if rendering is available.
6. Protection: exact permitted fixed-default ranges only, every human input editable, no passwords or structure locks, no hidden formulas. Inspect serialized styles as well as sheetProtection settings. Exercise domain changes without unlocking anything.
7. Calculation: `openpyxl` writes but does not evaluate formulas. Loading a file with data_only=True is not proof of recalculation. Use Excel or an available compatible calculation engine on test copies and record the engine, results and limitations; inspect a saved/reopened workbook. LibreOffice can alter formatting/validation, so any converted artifact must be revalidated. If no engine is available, complete static checks, label functional calculation/rendering checks NOT RUN, and provide exact manual Excel checks in VALIDATION.md. Do not claim full verification.
8. Reviewer smoke test in Excel: open a copy, set identity, finish one candidate per domain, change domain and clear stale answers, observe G/Checks/results update, save/close/reopen. No terminal or external process should be necessary. Record whether this was actually executed or is pending.

## 9. Release and stop runtime automation

After validation, place the two clean templates in `release/` with a plain-language `USAGE.md`. Every instruction necessary for reviewers must also be in each workbook. Keep build scripts, dependency versions, source/output hashes and `VALIDATION.md` as construction records in this year folder. Clearly identify any pending Excel smoke test before declaring the work fully validated.

The settled workbook is the authority: reviewers may edit and Save As in Excel, and all checks/results update there. There is no Python run, snapshot freeze, export command, synchronization, refresh, scheduled task, watch process, external calculation service or rebuild in review or delivery. Do not register any automation. Preserve completed review files with normal Excel backups; do not overwrite or regenerate them. Builder/validator tools are for pre-release construction only. Future corrections require a separately named new version and explicit review of changes.

Deliver exactly two independent primary-review templates for 2025; do not combine the reviewers' answers or start work on other years. Report output paths, actual validation performed, any pending checks and the narrow protection ranges.
