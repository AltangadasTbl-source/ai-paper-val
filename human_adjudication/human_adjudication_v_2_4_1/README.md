# v.2.4.1: independent primary review of workflow 1.6.2 candidates

v.2.4.1 uses the final, trimmed v.2.3.1 workbook layout: Setup, Checks, Papers, one `C_<paper>` sheet per paper, and Codebook. The candidates are replaced with those in each paper's `.ai_paper_validation/final_report_1_6_2.md`. The v.2.3.1 candidate sets came from the earlier pipeline and are not carried over. The build rules are in [BUILD_SPEC.md](BUILD_SPEC.md).

| Year | Papers | Candidates per reviewer | statistical_results | report_internal_inconsistency | plan_material | protocol_report | Files |
|---|---:|---:|---:|---:|---:|---:|---|
| 2018 | 10 | 115 | 49 | 4 | 7 | 55 | [2018/](2018/) |
| 2019 | 9 | 79 | 26 | 0 | 4 | 49 | [2019/](2019/) |
| 2024 | 10 | 113 | 51 | 2 | 15 | 45 | [2024/](2024/) |
| 2025 | 15 | 133 | 49 | 3 | 11 | 70 | [2025/](2025/) |

Review domains are the AI suggestions shown in column E, which the reviewer can edit. Disposition (column D) is blank.

Each year has one R_A and one R_B workbook. The two are identical except for Setup!B4. Distribute only the assigned file. Reviewers check candidates against the original PDFs named in Source location. For the full candidate statement, calculation and evidence, they consult the paper's `final_report_1_6_2.html`.

Reviewer instructions: English [REVIEWER_GUIDE_EN.md](REVIEWER_GUIDE_EN.md); Chinese [REVIEWER_GUIDE_CN.md](REVIEWER_GUIDE_CN.md), rendered as [REVIEWER_GUIDE_CN.pdf](REVIEWER_GUIDE_CN.pdf) with XeLaTeX/ctex (`bash render_guide/render.sh` re-renders it after edits).

## Changes from v.2.3.1

- Candidates come from workflow 1.6.2. jama.2019.0556 is new.
- jama.2019.14231 was removed on 2026-10-14. It is an observational study, and its paper package was moved to `archived/jama.2019.14231/`. The 2019 workbooks were rebuilt without it (79 candidates in 9 papers, all unchanged; validator 41/41 PASS), and the 2019 reviewer runs were revised to match (`reviewer_runs/README.md`).
- The H header and the Codebook field name are spelled `Statistical_or_numerical issue`, and the Codebook's section numbering no longer skips 5. The layout, dropdowns, formulas, formatting and Codebook text are otherwise unchanged.
- 2025 was first built on 2026-10-11 from the 13 finished 1.6.2 reports (109 candidates), with empty placeholder sheets for jama.2025.11178 and jama.2025.15185, whose 1.6.2 runs had stopped before screening. Their reports were completed on 2026-10-14 (18 and 6 candidates), and the 2025 workbooks were rebuilt with them (133 candidates; validator 451/451 PASS; the other 109 candidates are unchanged). See `2025/VALIDATION.md`. The 2025 cohort also includes jama.2024.24764 and jama.2024.27643.
- jama.2024.12829 first shipped as an empty placeholder sheet because its 1.6.2 report was not finished. The report was completed on 2026-10-11 and has 7 candidates, so the 2024 workbooks were rebuilt with them (113 candidates; validator 311/311 PASS).

## Review decisions fixed before distribution (2026-10-11)

1. **Disclosed changes count as differences.** A plan–report change that the report itself discloses still counts as a difference: for example, an analysis labelled post hoc, or a model replaced after nonconvergence. Reviewers retain it and note "disclosed" in column R. Disclosure is context, not grounds for exclusion.
2. **Protocol interpretation (L) stays optional.** It is optional for retained `protocol_report` rows, as the Codebook states. Deviation from protocol is common in randomized trials. How much a given plan–report difference matters is a question for the later analysis, not a required reviewer field in this round. A blank L therefore means "not described", not "no difference".

## Known source-text limitations

- jama.2018.18020 C022: the report's location field refers only to a table further down the card, so column C has no file or page. Use the card in the report.
- Several reports omit the file name from location link text. The builders added the file name as `<file> — <text>`.
- Location fields that are bullet lists or tables are joined with `; `. A few cells are long, up to about 2,500 characters.

## Validation status

Each year's `validate_v_2_4_1.py` passed every check in BUILD_SPEC.md: counts against the Candidate Index, the cards and the domain summary; key, formula, validation and formatting identity with the v.2.3.1 template; Codebook identity; R_A and R_B equivalence; source hashes; and recalculation scenarios with the `formulas` interpreter. The coordinator separately confirmed that the formula patterns, headers, Setup and Checks labels and Codebook are identical across all six files. The desktop Excel smoke test (open, recalculate, edit, save, reopen) is **pending**.
