# Human adjudication v.2.1.4 — Design

v.2.1.4 is based directly on v.2.1.3. The release has four annual workbooks, using the v.2.1.3 Checker presentation for both review stages. There are 45 visible paper sheets across the four templates, containing 412 unique candidates (119/71/91/131 by year).

## Presentation

Every paper uses C_<paper> throughout the workflow. All 19 headers, column widths, header colors, row heights, wrapping, filtering, and B2 freeze panes match the corresponding v.2.1.3 Checker sheet. Start, Setup, Papers, Candidates, Evidence, and Codebook remain self-contained. The catalog is stored under resources.

The annual template starts in primary review. Assessment fields contain only the existing suggested domain and conditional defaults; disposition and human judgments are unfilled. Checker-only columns O–R are blank, gray, and locked. The last column explains the future primary snapshot. The same Complete column applies to the current stage.

## Preserving both stages

The existing prepare-checker handoff validates completed primary review and creates the next annual working copy with the same paper sheets and columns. It freezes primary answers by candidate key in _Primary, preserves primary identity and file provenance, displays the primary summary on each row, clears checker overrides, resets completion, and unlocks checker controls. The checker file contains both primary and checker records. The completed primary input remains as a backup; existing files are never overwritten.

This retains the v.2.1.3 handoff mechanism while reducing the release from eight templates to four. There is no separate blank checker template, no duplicate visible primary paper sheets, no manual answer copying, and no external workbook dependency. A manager still runs the handoff command; Excel alone does not perform the stage transition. Snapshot protection and hashes detect workflow edits but are not cryptographic authentication.

## Validation and analysis

The schema is xlsx-adjudication-6, with primary and checker stages. Primary validation checks its 19-column structure and rejects any checker-only entries before handoff, including pasted values. Checker validation checks embedded primary content, identity, summaries, lookup ranges, candidate membership, required fields, and discussion resolution. Known default formulas are interpreted from saved values; cached results are not trusted.

Candidate/evidence data and scientific rules come from v.2.1.3. Statistical error status and substantiveness remain required for retained statistical findings. Downstream impact and protocol interpretation remain optional. Internal nonstatistical and plan-material domains share their assessment field. Documentation and Justification remain absent. P_R/P_P remain descriptive; S_C/S_W eligibility retains the same substantive criteria.

Blank checker inputs inherit by key; newly applicable fields cannot inherit old inactive values. Agree cannot conceal assessment changes. Non-agree requires a comment; disagreement, inability to resolve, and changes from primary discuss need documented joint resolution. Only prepared checker files can be exported, at most one per year. Unfinished counts remain unknown rather than zero.

The implementation and regression suite are adapted from v.2.1.3. Release checks compare all four annual layouts and every source candidate with v.2.1.3, and exercise both stages and a 412-candidate, 45-paper export in temporary files. See [VALIDATION.md](VALIDATION.md) for results and desktop verification limits.
