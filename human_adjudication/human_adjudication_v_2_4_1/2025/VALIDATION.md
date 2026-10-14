# v.2.4.1 validation, 2025

Built on 2026-10-11 by `build_v_2_4_1.py` from the workflow 1.6.2 reports (`2025/<paper>/.ai_paper_validation/final_report_1_6_2.md`) and the canonical 2018 v.2.3.1 template, following `../BUILD_SPEC.md`. Checked by `validate_v_2_4_1.py`; machine-readable results are in `validation_report.json`.

The build and validate scripts are copies of the 2024 scripts. Year-specific changes:
- `YEAR = 2025` and two placeholders;
- the validator accepts more than one placeholder;
- the parser accepts three 2025 report layouts: location fields written as separate paragraphs, a lead-in sentence followed by a bullet list, and level-1 section headings;
- the validator compares one-row data-validation and conditional-format ranges by the cells covered (`D2` = `D2:D2`).

## Scope

- 15 papers. 13 have a 1.6.2 report and supply 109 candidates. Two of the papers are `jama.2024.24764` and `jama.2024.27643`, which belong to the 2025 cohort despite their IDs.
- **Placeholders.** `jama.2025.11178` and `jama.2025.15185` have no `final_report_1_6_2.md`. Their 1.6.2 runs reached the checker stage, with `run_state.md` reporting target status PENDING and no screening, verification, quality audit or final report. Their files were last modified at 08:59 on 2026-10-11.
  - Each has a placeholder sheet: header row plus an A3 note, Candidates = 0 with a Note on the Papers sheet, and no formulas, data validations or conditional formats.
  - Both are excluded from the Checks formulas.
  - When their reports exist, remove them from `PLACEHOLDERS` in both scripts and rebuild.
- Domains (AI suggestions): statistical_results 33, report_internal_inconsistency 3, plan_material 11, protocol_report 62.

## What was checked (performed)

`validate_v_2_4_1.py` reported 415 passed, 0 failed:

1. **Counts.** Per paper, worksheet rows = Candidate Index rows = `## Cnnn` cards = Review-Domain Summary total, and per-domain counts match the summary.
2. **Row content.** Keys are unique and sequential. E is valid and equals the card; D is blank; F is `no`. B equals the card heading title. B and C contain no markdown residue. Every candidate row's C names a source file.
3. **Formulas and layout.** Every G–L formula matches the template pattern. Data validations and conditional formats cover exactly rows 2..last. M–Q are hidden, the freeze pane is B2, and styles and widths match the template. The placeholder sheets have only the header and A3.
4. **Workbook structure.** The sheet list and order, Setup, Papers and Checks are as specified (B3 = 109). The Codebook is identical to the template except the two specified fixes. R_A and R_B differ only in Setup!B4.
5. **Recalculation** with the Python `formulas` package on scratch copies:
   - (a) blank file: all G = `CHECK REVIEWER ID`, B7 = `ACTION NEEDED`;
   - (b) all rows valid and `primary_done`: all G = `PRIMARY READY`, B4 = B3 = 109;
   - (c) one inactive literal: `CLEAR INACTIVE VALUES`;
   - (d) one `discuss` row: counted in B5 and still `PRIMARY READY`.
6. **Source integrity.** Source reports and the template are unchanged, and the workbook hashes match `output_hashes.json`.

The coordinator separately confirmed that the formulas, headers, Setup and Checks labels and Codebook are identical to the 2018, 2019 and 2024 workbooks.

## Source-text notes

- Location fields in jama.2025.4390 are written as separate paragraphs. In jama.2025.20765, 9110 and 9663 (and in some cards elsewhere) they are bullet lists. In jama.2024.27643 a lead-in sentence on the label line is followed by a bullet list. All forms are joined with `; `. The full list is in `candidates_2025.json` (`parse_notes`).
- The longest C cells are about 1,500 characters (jama.2025.19843 C006/C007, jama.2025.24175 C007).

## Not performed

- Desktop Excel smoke test (open in Excel, dropdowns, conditional-format rendering, Excel recalculation, save and reopen): **PENDING**.
