# Validation — 2019 v.2.3.1

Status: **construction checks passed; desktop Excel smoke test and rendering NOT RUN.** The latest user scope is **9 papers / 62 candidates per role**. Two separate blank templates are delivered. **575 static checks, 535 formula-interpreter assertions and 5 builder refusal checks passed.** Protected ranges: **none**.

## Checks performed

- Read the prescribed v.2.1.5.3 references and inspected actual workbook layout, styles, source tables, default formulas, validation and conditional formatting. The historical baseline is unprotected.
- Recovered the seven required source files from the unchanged historical ZIP into this year folder only. Every source hash matches the supplied inventory. The supplied preflight matches after normalizing relocated paths. Its historical annual totals are distinct from the user-authorized release subset.
- Per role: 9 C_ sheets, 62 unique keys, identical included source order, blank reviewer identity/dispositions/notes and F=no. A–C, suggested E and untouched H–L formulas match baseline. Candidates (62), Evidence (224), Links (274) and Relations (68) match both baseline and catalog included rows cell-for-cell. All excluded identifiers are absent from every delivered workbook XML part and relationship.
- Static checks inspect all 1,526 formulas per file (maximum length 2,622 characters), all 539 hyperlinks per file, formula references, option codes, empty M–Q, calculation settings, source descriptions and Codebook definitions. No external workbook links, macros, connections, queries, obsolete workflow, stage selector, broken names, stored error values or imported human assessments were found. Source targets are rechecked at the final release location.
- All worksheet cells and all serialized style XFs, including the default style for unused cells, are explicitly unlocked and have no hidden formulas. There is no sheet protection, workbook structure lock, password or protected range. Every human input remains editable when a domain changes.
- A saved synthetic modification to one role leaves the other role byte-identical and blank. The roles otherwise have identical workbook content after normalizing their own role labels.
- Builder refusal cases: wrong year, path outside this folder, direct release output and existing workbook output. Once release exists, a further build is also refused. All work stays inside this year's folder; original sources and other years are unchanged.

## Formula calculation tests

Engine: **formulas 1.3.4**, a Python interpreter for Excel formulas, installed in the local construction environment. openpyxl 3.1.5 constructs and inspects workbooks; it does not evaluate formulas. The engine is never part of review or delivery.

`tests/calculation_report.json` records the actual assertions and expected/observed values. Tests evaluate every formula in blank role templates and in physical synthetic copies. They cover all retained domains; required/optional blanks and invalid codes; exclude and discuss; empty, padded, tab/newline and nonbreaking-space identity; invalid pasted codes; inactive stale answers; domain/disposition changes; optional clearing; manual completion reset; forbidden completion flags; missing/duplicate/foreign keys; descriptive relationship precedence; unfinished outcomes; and paper-count gating.

The synthetic fully completed cohort has 62 ready records and 9 papers with count gates open. Its expected outcomes are 22 primary_temporal, 26 secondary_temporal, 7 protocol_descriptive and 7 plan_descriptive. These are **test answers only**, not findings or release data. Additional cases verify completed exclusions, ready and draft discuss totals, zero versus withheld counts, key-matched notes and protocol/plan results. Whole A:R reordering keeps outcomes and notes associated with their keys. A one-candidate fixture also calculates correctly.

The completed test copy was saved and reopened with formulas retained. Interpreter results were separately written to a clearly named **values-only test export**, saved and reopened, and compared. This is not a desktop Excel save/reopen test. The release files retain formulas and automatic full recalculation; no synthetic answers or fabricated cached formula results are inserted.

Interpreter limitation: directly overriding an originally empty cell can leave an already assembled blank lookup range unchanged in the interpreter. Notes and sorting were therefore tested using physically saved filled copies. This does not substitute for testing Excel itself.

## Pending checks — exact desktop Excel procedure

Use disposable working copies; do not enter tests into the clean release templates. No terminal or external process is needed.

1. Open both templates separately in Excel. Confirm no repair prompt, external-workbook update prompt or password. After recalculation, Checks should show 62 total, 0 ready, 62 unfinished and 0 discuss. Inspect Start, Setup, Codebook and the C_ sheets at ordinary zoom for clipped instructions, wrapped text, dropdown readability, colors and freeze panes. Verify M–Q are empty hidden spacers and R contains notes.
2. In an R_A test copy, enter your own test ID in Setup B2. In C_jama.2019.10517 row 2, choose D=retain, E=statistical_results, H=confirmed_issue, I=substantive and F=primary_done. Leave J blank. G should show PRIMARY READY and the matching Decisions outcome should be primary_temporal. Enter J=direct, then clear it: readiness remains valid and the effective optional value is blank.
3. Complete row 3 of that sheet using report_internal_inconsistency with K=substantive_inconsistency, and row 4 using plan_material with K=substantive_inconsistency; clear any inactive literal answers. Complete a protocol row, such as C_jama.2019.12618 row 4, using protocol_report and leaving L blank. Confirm L remains editable and protocol/plan results stay descriptive.
4. Reset F=no on the statistical row, change E to report_internal_inconsistency and leave H/I in place. G should say CLEAR INACTIVE VALUES. Clear H/I/J, enter K, and re-mark F=primary_done. Change back and test missing H/I, active not_applicable, optional invalid J, and pasted invalid D/E or completion codes. Each must block readiness. Confirm no unlock step occurs.
5. On a valid statistical row, set F=no and change D to exclude, leaving substantive answers: G must flag stale inactive values. Clear H–L and re-mark done: outcome becomes not_eligible. Change D to discuss with H–L cleared: G may be PRIMARY READY; outcome stays blank and Checks shows an unresolved row. Paper outcome counts must remain blank while a paper has unfinished or discuss rows. In `tests/all_complete.xlsx`, first open and recalculate, then change one valid row to discuss and clear active literals: entry completion stays PRIMARY READY, while that paper's counts become blank. This file contains synthetic answers and must never be submitted.
6. Temporarily clear Setup B2 or enter only spaces/tabs/nonbreaking spaces; completion must be blocked. Restore identity. Reset a completed row's F to no; its outcome and paper counts must be withheld until it is reviewed and re-marked done. Confirm a valid edit alone cannot erase an entered completion flag; manual reset is required.
7. In a test copy, add distinct R notes and sort the entire candidate A:R range, including hidden M–Q. Decisions and Protocol_plan_table must still match the correct keys and notes. Temporarily duplicate or remove a key: readiness and original candidate outcome must be blocked. Undo. Open `tests/single_candidate.xlsx` and confirm PRIMARY READY, one ready record and a primary_temporal outcome after recalculation.
8. Follow Papers links, candidate-key links, Candidates reportHref and original-source hyperlinks. For the six jama.2019.14901 candidates, confirm navigation to the embedded rationale because separate Evidence rows are absent in the baseline. Confirm access to originals and PDF page fragments in your Excel/PDF viewer environment.
9. Save, close and reopen the test workbook in desktop Excel. Confirm identity, input judgments, manual completion flags, readiness, counts and source links persist and recalculate. Repeat a representative entry in the R_B copy and verify R_A is unaffected. Deliver only independently completed real review files.

## Records

- `release/validation_report.json`: final-location static validation and hashes.
- `tests/calculation_report.json`: formula-interpreter cases and limitations.
- `tests/builder_guard_report.json`: builder refusal checks.
- `source_hash_manifest.json`: source/archive provenance; `release/output_hashes.json`: release hashes.
- `TRANSFORMATION.md`: scope, source relocation, schema, rules and layout changes.
- `build_v_2_3_1.py`, `validate_v_2_3_1.py`, `tests/run_calculations.py`, and `requirements-construction.txt`: construction-only records.

No desktop Excel or LibreOffice executable is available in this environment. Visual comparison against rendered baseline previews, interactive dropdown behavior, native Excel sorting, actual source/PDF opening, and the desktop reviewer save/close/reopen smoke test remain **NOT RUN**. Do not describe these files as fully Excel-validated until those checks are completed.
