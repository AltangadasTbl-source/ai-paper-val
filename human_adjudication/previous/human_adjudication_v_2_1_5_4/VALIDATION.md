# Validation — v.2.1.5.4 compatibility repair

Verified 2026-09-17.

## Reproduced defect and fix

Desktop Microsoft Excel displayed “We found a problem with some content” when opening the v.2.1.5.3 2019 workbook. The unlock post-processor had put protection after extLst in five cell-format records. Reordering those elements alone allowed the same workbook to open without a recovery prompt. The v.2.1.5.4 release applies that repair to all six review workbooks. The maintenance build now uses a parsed-XML normalizer, with a regression test for this exact case.

## Desktop Excel verification

Opened each final file directly in Microsoft Excel on macOS without recovery or repair prompts:

- 2018 annual workbook: 24 sheets.
- 2019 annual workbook: 24 sheets.
- 2024 annual workbook: 24 sheets.
- 2025 annual workbook: 29 sheets.
- 2019 TEST primary-complete example: 24 sheets; Checks displays 71 primary-ready rows and PRIMARY READY.
- 2019 TEST checker-ready example: 24 sheets.

## Preservation checks

ZIP/XML comparison confirms identical package parts and identical contents except release labels and the ordering of style children. Parsed style comparisons preserve all attributes and child content. Candidate records, evidence, human-input values, formulas, table definitions, dropdowns, conditional formatting and snapshot values are unchanged. The four annual templates still contain 412 candidates across 45 paper sheets. The source catalog was versioned without changing candidate/evidence data.

All six review files retain explicit unlocked cell styles and no sheet/workbook protection. The catalog retains its unprotected state. Formula-engine recalculation and stage-display checks cover the 2019 and 2025 templates and both examples. The former 32 scenario checks and four completed annual simulations remain applicable to the unchanged formulas; native opening is now independently verified rather than inferred from an artifact-tool import.

The Chinese PDF was regenerated with the new version number in the v.2.1.5.4 folder. All 11 pages rendered successfully; layout and instructions otherwise match the previously reviewed guide.

Prior release files are preserved. No Python is needed for review, handoff, checking or delivery.
