# AI-simulated reviewer runs: v.2.3.1 (2026-10-10)

These eight workbooks were completed by Claude Opus 5.5 agents (high effort) acting as reviewers R_A and R_B for each year. **They are not human adjudications.** Each Setup sheet's reviewer ID is `AI-sim-ClaudeOpus5.5-<year>-<role>`. Do not submit, pool or report them as human review. The release templates in `../<year>/release/` were not modified: their hashes match `output_hashes.json` for 2018, 2019 and 2024, and the 2025 templates are unchanged in git.

## Layout

```
fill_review.py      judgments JSON -> copy of the release template (rule checks; refuses overwrite or writing into release/)
recalc_check.py     recalculates a completed workbook with the `formulas` interpreter; reports G and Checks
compare_roles.py    post hoc R_A vs R_B agreement (descriptive)
trim_workbook.py    keeps only Setup, Checks, Papers, C_ sheets and Codebook; makes G and Checks self-contained
<year>/<role>/judgments.json      every judgment with the evidence inspected and the rationale/recomputation
<year>/<role>/*_completed.xlsx    completed copy of the role's release template
<year>/<role>/REVIEW_SUMMARY.md   counts, disagreements with the AI, extra-candidate observations, disclosures
```

Run the scripts with `../2019/.venv/bin/python`; it has openpyxl 3.1.5 and formulas 1.3.4.

## Sheet reduction (2026-10-10)

At the user's request, all v.2.3.1 workbooks were reduced with `trim_workbook.py`: the blank release templates, these completed runs and `../Bulun_version/`. The removed sheets are Start, Decisions, Paper_counts, Protocol_plan_table, Candidates, Evidence, Links, Relations, Rule_defaults and Manifest. The G key check now tests the key's `<year>::<paper>::` prefix instead of looking it up in Decisions or Candidates, and Checks counts directly from the C_ sheets. The embedded evidence and the per-paper outcome results are therefore no longer in the workbooks; the evidence and rationale for each completed review remain in its `judgments.json`.

## Results

All eight workbooks recalculate with every row and the Checks sheet at `PRIMARY READY` under the `formulas` interpreter. Desktop Excel was not used.

| Year | Role | Candidates | Retain | Exclude | Discuss | Substantive* |
|---|---|---:|---:|---:|---:|---:|
| 2018 | R_A | 119 | 118 | 1 | 0 | 25 |
| 2018 | R_B | 119 | 118 | 1 | 0 | 25 |
| 2019 | R_A | 62 | 58 | 4 | 0 | 10 |
| 2019 | R_B | 62 | 59 | 3 | 0 | 11 |
| 2024 | R_A | 91 | 84 | 7 | 0 | 12 |
| 2024 | R_B | 91 | 87 | 4 | 0 | 15 |
| 2025 | R_A | 131 | 106 | 25 | 0 | 38 |
| 2025 | R_B | 131 | 112 | 19 | 0 | 35 |

\*Substantive means one of two cases among retained rows:
- a statistical result with H = confirmed_issue or probable_issue and I = substantive;
- a report-internal or plan-material inconsistency with K = substantive_inconsistency.

R_A vs R_B agreement from `compare_roles.py`. The outcome column uses that script's derived categories.

| Year | D agreement (kappa) | E agreement (kappa) | Outcome agreement (kappa) |
|---|---|---|---|
| 2018 | 1.000 (1.00) | 0.992 (0.98) | 0.958 (0.94) |
| 2019 | 0.984 (0.85) | 0.984 (0.98) | 0.952 (0.93) |
| 2024 | 0.967 (0.71) | 0.956 (0.92) | 0.890 (0.84) |
| 2025 | 0.924 (0.73) | 1.000 (1.00) | 0.901 (0.87) |

These agreement figures do **not** estimate human inter-rater reliability. Both roles are the same model reading the same evidence, so their errors are likely correlated. Kappa values from a few hundred items with very unbalanced categories are also unstable.

## Limitations and independence record

- **No `discuss`.** No reviewer used `discuss` for any of the 806 role-candidate judgments. Treat this as possible overconfidence, not evidence that every candidate was clear-cut.
- **Shared scratchpad.** All agents shared one session scratchpad. Several wrote files to its top level before using private folders, and same-named helper scripts and sheet dumps were overwritten. Two agents saw other agents' content:
  - 2019 R_B read sheet dumps containing 2024 candidate material.
  - 2018 R_B and 2024 R_A each saw one traceback line of another agent's script.

  The coordinator searched every command these agents ran, including the four forks used by 2025 R_A. No agent read the same-year opposite role's output folder or private working folder, the AI pipeline's internal outputs (`.ai_paper_validation/`), or `human_adjudication/previous/`. No rationale or workbook note is identical between the R_A and R_B reviews of 2025. Future runs should give each role its own working directory from the start.
- **Pipeline instructions leaked into context.** Opening PDFs in paper folders loaded each paper's pipeline `AGENTS.md` automatically. The agents that reported this say they ignored it; this cannot be verified. For cleaner runs, copy only the source PDFs into a neutral folder.
- **Earlier annotation file.** `2024/jama.2024.2302/Detailed_Errors_On_C1_C3_C5.docx` looks like an earlier error annotation. Neither 2024 agent opened it, but it should be kept away from human reviewers.
- **Forks in 2025 R_A.** 2025 R_A split its papers across four forks working to shared written conventions. Its borderline exclusion calls may be less internally consistent than a single reviewer's.
- **PDF reading.** No poppler is installed, so the Read tool cannot render PDFs. Agents used PyMuPDF from the system user site-packages, plus pypdf/pdfplumber in a scratch venv, for text extraction and page rendering.
- **Completion flags.** `fill_review.py` sets F = `primary_done` for every judged row. The desktop Excel smoke test in each year's VALIDATION.md is still pending.

## Template issues found by the reviewers

- **jama.2019.14901:** all 6 candidates have no source location and no Evidence rows. The only links point into `.ai_paper_validation/`.
- **jama.2024.4183:** the Evidence text is generic placeholder wording.
- **jama.2024.25786:** the Evidence sheet repeats the full text in each field and contains leftover adjudication-form text.
- **AI disposition visible:** the Candidates sheet shows `ai_disposition`, although the Codebook says no AI disposition is preselected. Column D is blank, so the Codebook's statement holds only for that column.
- **Cosmetic:**
  - the header reads "Statistcal_or_numerical issue" in 2018, 2024 and 2025;
  - the Codebook section numbering skips 5;
  - candidate statements carry "Pending Human Adjudication" boilerplate.

Several reviewers also recorded possible errors outside the candidate set. These appear in each `REVIEW_SUMMARY.md` and were not adjudicated.
