# 2019 independent primary review — v.2.3.1

Use the two Excel templates in `release/`. Each contains the same **9 papers / 62 candidates**. R_A and R_B are role labels. The coordinator assigns two different people and gives each person only their corresponding file.

1. Open the assigned template in Excel and **Save As** a working copy. In Setup B2, enter your own reviewer ID or name. B3 is an optional full name.
2. Use Papers to open a C_ sheet. Click a candidate key for embedded evidence or its Candidates rationale. Consult Candidates, Evidence and Links. Source-file hyperlinks require access to the repository's source folders; structured evidence is embedded.
3. Choose D (`retain`, `exclude`, `discuss`), confirm or edit the AI-suggested E domain, answer applicable H–L, and optionally add English notes in R. Read Codebook for definitions. Yellow fields are common/required; blue fields are optional; gray fields are inactive. M–Q are empty hidden spacers.
4. After manually reviewing a row, set F=`primary_done` and check that G says `PRIMARY READY`. Use F=`no` while drafting. Correct any validation message before completing the row.
5. Inspect Checks and the built-in Decisions, Paper_counts and Protocol_plan_table. When Checks says `PRIMARY READY`, save and deliver your workbook. Keep ordinary Excel backups.

Retained statistical_results requires H and I; J is optional. Retained report_internal_inconsistency or plan_material requires K. Retained protocol_report has only optional L. Exclude/discuss makes all H–L inactive. D and a valid E are always required. Optional active judgments may be blank, but may not be not_applicable.

Untouched H–L formulas show blank for potentially applicable fields and not_applicable for inactive ones. Selecting an answer replaces that formula. Changing D/E does not erase literal answers. Clear stale inactive entries or choose not_applicable, then answer newly required fields. G checks pasted values as well as dropdown selections.

**Before changing a completed row, manually reset F to no.** Review the revised row, then mark primary_done again. Excel formulas cannot erase an entered completion flag automatically.

A valid `discuss` row can be PRIMARY READY and remains unresolved. Its outcome is blank. Paper outcome counts stay blank until all rows in that paper are primary-ready and none is discuss. Completion means independent data entry is finished; it does not resolve scientific uncertainty. No shared resolution step is required.

All cells are editable, including reference and calculation cells. **Protected ranges: none; no password or unlock step.** Preserve source data, keys and formulas; use Undo or a backup after accidental edits. When sorting, include the complete A:R candidate rows, including hidden columns.

All review steps, validation and results operate in Excel. There is no Python run, refresh, export, synchronization or rebuild during review or delivery. Do not regenerate completed workbooks. The local builder, validator, environment and tests are construction records only.

The desktop Excel smoke test and visual inspection are pending; see the adjacent VALIDATION.md. Construction checks and formula-interpreter tests have been run. Instructions needed for review are also embedded in each workbook's Start, Setup and Codebook sheets.
