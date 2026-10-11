# Bulun_version: provenance

Reviewer of record: BulunTe (role R_B, all four years). Created 2026-10-10.

On 2026-10-10, BulunTe checked and accepted the R_B judgments drafted by the AI-simulated reviewer runs in `../ai_reviewer_runs/<year>/R_B/`. The workbooks here are identical to those drafts except Setup B2, which is now `BulunTe`, and Setup B3, which is cleared. No judgments, domains, completion flags or notes were changed.

Later on 2026-10-10, at BulunTe's request, `R_B` was dropped from the file names, and all v.2.3.1 workbooks were reduced to Setup, Checks, Papers, the C_ paper sheets and Codebook using `../ai_reviewer_runs/trim_workbook.py`. That covers the blank release templates, the R_A and R_B runs and this folder. The G validation formulas and Checks totals were rewritten so they no longer depend on the removed sheets. The candidate-key links to Evidence were removed. No reviewer inputs changed.

| File | Source |
|---|---|
| `human_adjudication_v_2_3_1_2018_BulunTe.xlsx` | `../ai_reviewer_runs/2018/R_B/human_adjudication_v_2_3_1_2018_R_B_completed.xlsx` |
| `human_adjudication_v_2_3_1_2019_BulunTe.xlsx` | `../ai_reviewer_runs/2019/R_B/human_adjudication_v_2_3_1_2019_R_B_completed.xlsx` |
| `human_adjudication_v_2_3_1_2024_BulunTe.xlsx` | `../ai_reviewer_runs/2024/R_B/human_adjudication_v_2_3_1_2024_R_B_completed.xlsx` |
| `human_adjudication_v_2_3_1_2025_BulunTe.xlsx` | `../ai_reviewer_runs/2025/R_B/human_adjudication_v_2_3_1_2025_R_B_completed.xlsx` |

`judgments_<year>_BulunTe.json` holds the per-candidate evidence and rationale behind each workbook, with the reviewer ID changed the same way. The drafting reviewers' summaries and independence disclosures remain in `../ai_reviewer_runs/<year>/R_B/REVIEW_SUMMARY.md` and `../ai_reviewer_runs/README.md`.

Check: all four workbooks recalculate with every row and the Checks sheet at PRIMARY READY under the `formulas` 1.3.4 interpreter (119, 62, 91 and 131 rows for 2018, 2019, 2024 and 2025). The desktop Excel smoke test is pending.
