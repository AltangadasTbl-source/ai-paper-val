# Human adjudication v.2.1.4 — Validation

Validation date: 2026-09-13. Review version/revision: v.2.1.4; schema: xlsx-adjudication-6. Runtime: Python 3.12.3 / openpyxl 3.1.5.

## Release and source checks

The top-level version directory contains exactly four annual review XLSX files. The catalog is under resources; explicitly synthetic 2019 examples are under examples.

| Year | Visible paper sheets | Candidates |
|---|---:|---:|
| 2018 | 10 | 119 |
| 2019 | 10 | 71 |
| 2024 | 10 | 91 |
| 2025 | 15 | 131 |
| Total | 45 | 412 |

All four annual layouts were compared directly with the corresponding v.2.1.3 Checker files: all 19 headers, column widths, header fills, row alignment, row height, freeze panes, filter range, and per-paper candidate rows match. Each workbook includes visible Start, Setup, Papers, Candidates, Evidence, and Codebook sheets. Primary-stage checker-only cells are blank and locked. No human disposition or completed review is prefilled in the four release templates.

The complete source candidate objects match the v.2.1.3 catalog, including evidence and source metadata. Relationship counts remain P_R=45, P_P=50, S_C=65, S_W=252. All release workbooks and catalog passed English-only package checks and contain no macros, external workbook links, or active hyperlinks.

## Regression suite

**24 tests passed in 109.414 seconds.** Command:

```bash
python3 -m unittest discover -s human_adjudication/human_adjudication_v_2_1_4 -p test_v_2_1_4.py -v
```

Coverage includes:

- Four release files with 45 Checker-layout paper sheets and unchanged source data.
- Primary completion without checker answers; rejected checker-only entries before handoff.
- Completed-primary handoff preserving the input, identity, snapshot, visible summary, and provenance; checker completion resets and fields unlock.
- All four years passing through primary completion, checker agreement, and combined export with 412 decisions and 45 paper rows.
- Key-based inheritance after complete-row reordering; invalid/misplaced/missing candidates and changed paper indexes rejected.
- Snapshot, primary summary, identity, and lookup-range changes detected.
- Required versus optional domain judgments, conditional defaults, newly applicable checker fields, and protocol/plan exclusion from temporal outcomes.
- Formula/error answers and non-English content rejected; Codebook fields and dropdown ranges verified in both stages.
- Agree cannot conceal changes; non-agree needs comments; disagreement and primary discuss require joint resolution.
- Complete zero-result papers exported with zeros; unfinished paper counts remain blank in provisional exports.
- Duplicate-year inputs, repeated handoff from checker files, and overwriting existing outputs rejected.
- Restoring defaults preserves the frozen primary snapshot.

Regression simulations use temporary directories. The separately requested 2019 example is deliberately published under examples, with synthetic identities, Start banners, and per-row notes; it is not a reviewed research dataset. Its 71 primary rows are marked complete with exclude placeholders, and all checker rows remain pending. Both sample files are validated, and the prepared copy retains exactly the sample primary records.

## Additional release checks

All 3,324 formulas in the four annual templates and two examples passed formula tokenization; the longest has 2,221 characters. The source catalog contains no review formulas. A saved-and-reopened test of the published 2019 checker example successfully changed one row to agreement: one resolved candidate and 70 pending candidates, with no validation errors. The published sample itself remains unfilled at checker stage.

The English/Chinese Markdown notes and Chinese TeX/PDF were updated. XeLaTeX completed two passes and produced a two-page PDF, with no missing characters, overfull boxes, undefined references, or fatal errors. The installed CTEX packages emit LaTeX release-date warnings. All local links in the current entry point and v.2.1.4 Markdown documents resolve.

## Limits

These checks validate XLSX structure, saved values, and the Python workflow. Native desktop Microsoft Excel, WPS, and LibreOffice rendering, dropdown interaction, and formula recalculation have not been tested in this environment. Default formulas are interpreted from saved inputs by validation; it does not trust cached formula results.

The manager still runs prepare-checker for the stage transition. Existing files are not overwritten; an annual checker working copy embeds both stages and the completed primary file remains a backup. Editing an answer requires manually rechecking Complete. Changing a domain does not erase literal old answers; conditional formatting flags them for cleanup. Protection and hashes detect workflow edits, not malicious forgery.
