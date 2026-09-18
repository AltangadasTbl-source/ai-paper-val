# Validation — v.2.1.5.3 Excel-only update

Verified 2026-09-17.

- Four annual templates: 2018=119, 2019=71, 2024=91, 2025=131 candidates; 412 unique keys across 45 paper sheets. Source Candidates, Evidence, Links and Relations match the previous v.2.1.5.3 files cell-for-cell. No entered primary dispositions or completions existed before replacement; concurrent-edit checks also passed.
- Six review workbooks (four templates plus two synthetic examples): 149 sheets, 23,942 formulas. Exported files reopened successfully. No cached formula errors; maximum serialized formula length 5,996 characters, below Excel's 8,192 limit. Automatic recalculation is enabled.
- No worksheet or workbook protection; all cell styles, including the default style, explicitly set locked=0 and hidden=0. English-only XLSX content confirmed. The existing unprotected frozen-source catalog is unchanged.
- 32 scenario assertions passed: initial M blank, primary completion, snapshot handoff, unfrozen handoff rejected, primary_done insufficient for checking, direct checker edits, unchanged agree, changed agree rejected, required comments, disagreements, resolution notes, discuss blocked, invalid/obsolete options, inactive values, optional clearing, distinct reviewer IDs, duplicate keys, key-based reordering, and temporal/descriptive outcomes.
- Complete synthetic primary → frozen snapshot → checker runs passed for all four years, including the single-candidate 2025 paper. Every paper's completed count reconciled with its candidate total. TEST answers are confined to examples; official templates remain blank for human decisions.
- Spreadsheet previews checked: Start, Checks, and checker Primary assessment. The 11-page Chinese PDF was rendered to PNGs and every page visually reviewed; browser layout checks found no footer overlap or page overflow. The PDF remains in this version folder.
- Start, Codebook, USAGE, examples and PDF describe the same Excel-only workflow. Old Python review entry points and requirements file removed from the active release; old version folders preserved.

Limits: entry checks do not verify the scientific judgment, make records tamper-proof, or protect editable formulas/source cells. Preserve the primary backup. Completed-row flags require manual reset after edits. Validation used the artifact calculation engine and exported OOXML inspection; an interactive desktop Excel session was not used.
