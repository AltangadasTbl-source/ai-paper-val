# 2024 independent primary review — v.2.3.1

Two separate templates cover the same 10 papers and 91 candidates:

- `human_adjudication_v_2_3_1_2024_R_A.xlsx`
- `human_adjudication_v_2_3_1_2024_R_B.xlsx`

The coordinator assigns two different people and distributes only the corresponding file to each. R_A/R_B are roles, not person IDs. Neither file imports or depends on the other person's assessment. A standalone file cannot verify the other person's identity.

1. Open your assigned template in Excel and **Save As** a working copy in this folder. Enter your own ID/name in Setup B2; full name in B3 is optional.
2. Use Papers to open each C_ sheet. Candidate keys link to embedded Evidence. Candidates, Links and Relations contain the frozen source material. Source-file links require the original repository folders; keep their relative layout when moving a working copy.
3. Choose D (retain/exclude/discuss), confirm or change the AI-suggested E domain, answer applicable H–L, and optionally add English notes in R. Read Codebook for definitions. M–Q are empty hidden spacers.
4. For retained statistical_results, H and I are required and J optional. Retained report_internal_inconsistency or plan_material requires K. Retained protocol_report has optional L and no extra required judgment. Inactive fields must be blank or not_applicable; not_applicable is invalid in an active field.
5. Untouched H–L formulas display blank when potentially applicable and not_applicable otherwise. Entering an answer replaces that input formula. Domain/disposition changes do not remove old literal answers. Clear stale inactive values when G requests it. Blank means no answer.
6. After manual review, set F=primary_done and inspect G. Before editing a completed row, manually reset F=no, review again and then mark primary_done. Excel cannot automatically reset an entered completion flag.
7. Inspect Checks and Decisions. When every row is PRIMARY READY, save, close, reopen to confirm saved entries, and deliver this workbook. Preserve ordinary Excel backups. No terminal, Python, scripts, refresh, synchronization or export command is part of review or delivery.

`discuss` may be a completed independent assessment, but remains unresolved scientific uncertainty. Its outcome stays blank. Paper_counts shows completion separately and withholds outcome counts until every paper row is ready and none is discuss. Retained P_R/P_P results are descriptive and never temporal. See Start and Codebook inside each workbook for full instructions.

**Protection: none.** All cells and styles, including unused cells, are unlocked. There are no passwords or structure locks. Rule_defaults is an unprotected visible reference. Preserve source keys, evidence and calculation cells; undo accidental edits or recover from a backup. Do not rebuild completed reviews.

**Validation status:** construction and static checks passed. Desktop Excel recalculation, rendering and reviewer smoke tests have **not been run**. Follow the exact pending checks in [VALIDATION.md](VALIDATION.md) on disposable copies before operational use. The Python regression probe is not an Excel-compatible calculation engine.
