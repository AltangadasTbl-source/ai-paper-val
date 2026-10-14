# v.2.4.1 validation, 2024

Built by `build_v_2_4_1.py` from the workflow 1.6.2 reports (`2024/<paper>/.ai_paper_validation/final_report_1_6_2.md`) and the canonical 2018 v.2.3.1 template, following `../BUILD_SPEC.md`. Checked by `validate_v_2_4_1.py`; machine-readable results are in `validation_report.json`.

## Scope

- 10 papers, 113 candidates. Rebuilt on 2026-10-11 after `jama.2024.12829` received its 1.6.2 report (7 candidates). It had been an empty placeholder sheet in the first build (106 candidates). The placeholder declaration was removed from the build and validate scripts, and the Papers sheet now has the standard three columns.
- Per-paper counts and domain counts are recorded in `candidates_2024.json` (`papers`, `parse_checks`).

## What was checked (performed)

1. Per paper, worksheet row count = Candidate Index rows = `## Cnnn` cards = Review-Domain Summary total. The build additionally fails if index domain/relationship type differ from the card, or if per-domain card counts differ from the summary table.
2. Keys `2024::<paper>::Cnnn` unique and sequential, matching report IDs; E in the four allowed domains and equal to the card; D blank; F `no`; B equal to the card heading title; B and C non-empty with no markdown residue (`](`, `**`, `<a id`, backticks) and no "Pending Human Adjudication" text.
3. Every G-L formula equal to the template row-2 pattern after substituting row number, `$A$2:$A$<last>` and the key prefix (the substitution model is first verified to reproduce every G-L formula in the 2018 template); data validations and conditional formats cover exactly rows 2..last with template settings and rules; M-Q hidden at width 3; freeze pane B2; column widths, header and data-row styles, row heights and autofilter as template.
4. Sheet list Setup, Checks, Papers, C_ sheets (plain string order), Codebook; Setup B2/B3 blank, B4 role, B5 = 2024 (integer); Papers rows; Checks B3 = 113 (integer), B4/B5 exact COUNTIF sums, other Checks cells as template; Codebook identical to template in values, styles and dimensions except the two specified fixes; R_A and R_B differ only in Setup!B4 (all cell values compared).
5. Recalculation with the Python `formulas` package (1.3.4) on copies in a scratch directory outside the repository: (a) blank file, every G = `CHECK REVIEWER ID`, Checks!B7 = `ACTION NEEDED`; (b) reviewer ID plus a valid answer for each row's domain and `primary_done`, every G = `PRIMARY READY`, B4 = B3 = 113, B7 = `PRIMARY READY`; (c) one statistical_results row with an inactive K value, that row `CLEAR INACTIVE VALUES`, B7 `ACTION NEEDED`; (d) one `discuss` row, B5 = 1 and still `PRIMARY READY`. R_B blank file also recalculated (B2 = `R_B`, B7 `ACTION NEEDED`).
6. Source reports and template unchanged (sha256 before = after build, and current = recorded in `output_hashes.json`); workbook hashes match `output_hashes.json`; the year folder holds only the specified files.

In the first build, the validator was also run against deliberately corrupted copies (altered G formula, formula in the placeholder, Codebook edit, invalid domain, markdown residue, removed data validation, unhidden spacer column); each was detected.

## Rebuild result (2026-10-11)

`validate_v_2_4_1.py` reported 311 passed, 0 failed after the rebuild. The coordinator separately confirmed that the `C_jama.2024.12829` formulas match the template pattern, the Codebook is identical to 2018's, and the new sheet is included in the Checks formulas.

## Not performed

- Desktop Excel smoke test (opening in Excel, dropdowns, conditional-format rendering, Excel recalculation, save and reopen): **PENDING**. The `formulas` package is not Microsoft Excel.
