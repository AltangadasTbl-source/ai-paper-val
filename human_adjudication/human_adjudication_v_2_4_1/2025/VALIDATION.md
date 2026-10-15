# v.2.4.1 validation, 2025

Built on 2026-10-11 and rebuilt on 2026-10-14 by `build_v_2_4_1.py` from the workflow 1.6.2 reports (`2025/<paper>/.ai_paper_validation/final_report_1_6_2.md`) and the canonical 2018 v.2.3.1 template, following `../BUILD_SPEC.md`. Checked by `validate_v_2_4_1.py`; machine-readable results are in `validation_report.json`.

The build and validate scripts are copies of the 2024 scripts. Year-specific changes:
- `YEAR = 2025`, and two placeholders in the first build (none since 2026-10-14);
- the validator accepts more than one placeholder;
- the parser accepts four 2025 report layouts: location fields written as separate paragraphs, a lead-in sentence followed by a bullet list, or a table (added 2026-10-14), and level-1 section headings;
- the validator compares one-row data-validation and conditional-format ranges by the cells covered (`D2` = `D2:D2`).

## Scope

- 15 papers with 133 candidates. Two of the papers are `jama.2024.24764` and `jama.2024.27643`, which belong to the 2025 cohort despite their IDs.
- **Rebuild of 2026-10-14.** The first build (2026-10-11, 109 candidates) had placeholder sheets for `jama.2025.11178` and `jama.2025.15185`, whose 1.6.2 runs had stopped at the checker stage. Their final reports were completed on 2026-10-14 (11178: 18 candidates; 15185: 6 candidates). Both were removed from `PLACEHOLDERS` in the two scripts and the workbooks were rebuilt. The 109 candidates of the other 13 papers are identical in `candidates_2025.json` before and after the rebuild (every field compared), and their source reports match the hashes recorded in the first build. Without placeholders the Papers sheet has no Note column, as in 2018, 2019 and 2024.
- **Parser change.** `jama.2025.11178` C018 gives its source locations as a table. The parser now accepts a table in that field and writes one item per data row: the location column, followed by the content-role column in parentheses. The paragraph after the table is kept, as for other paragraph-form fields. No other card uses this layout.
- Domains (AI suggestions): statistical_results 49, report_internal_inconsistency 3, plan_material 11, protocol_report 70.

## What was checked (performed)

`validate_v_2_4_1.py` reported 451 passed, 0 failed on the 2026-10-14 rebuild (415 on the first build):

1. **Counts.** Per paper, worksheet rows = Candidate Index rows = `## Cnnn` cards = Review-Domain Summary total, and per-domain counts match the summary.
2. **Row content.** Keys are unique and sequential. E is valid and equals the card; D is blank; F is `no`. B equals the card heading title. B and C contain no markdown residue. Every candidate row's C names a source file.
3. **Formulas and layout.** Every G–L formula matches the template pattern. Data validations and conditional formats cover exactly rows 2..last. M–Q are hidden, the freeze pane is B2, and styles and widths match the template.
4. **Workbook structure.** The sheet list and order, Setup, Papers and Checks are as specified (B3 = 133). The Codebook is identical to the template except the two specified fixes. R_A and R_B differ only in Setup!B4.
5. **Recalculation** with the Python `formulas` package on scratch copies:
   - (a) blank file: all G = `CHECK REVIEWER ID`, B7 = `ACTION NEEDED`;
   - (b) all rows valid and `primary_done`: all G = `PRIMARY READY`, B4 = B3 = 133;
   - (c) one inactive literal: `CLEAR INACTIVE VALUES`;
   - (d) one `discuss` row: counted in B5 and still `PRIMARY READY`.
6. **Source integrity.** Source reports and the template are unchanged, and the workbook hashes match `output_hashes.json`.

The coordinator separately confirmed that the formulas, headers, Setup and Checks labels and Codebook are identical to the 2018, 2019 and 2024 workbooks.

## Source-text notes

- Location fields in jama.2025.4390 are written as separate paragraphs, and in jama.2025.11178 C018 as a table. In jama.2025.20765, 9110 and 9663 (and in some cards elsewhere) they are bullet lists. In jama.2024.27643 a lead-in sentence on the label line is followed by a bullet list. All forms are joined with `; `. The full list is in `candidates_2025.json` (`parse_notes`).
- The longest C cells are about 1,500 characters (jama.2025.19843 C006/C007, jama.2025.24175 C007).

## Not performed

- Desktop Excel smoke test (open in Excel, dropdowns, conditional-format rendering, Excel recalculation, save and reopen): **PENDING**.
