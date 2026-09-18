# Human adjudication v.2.1.5.2 — Design

This release updates v.2.1.5.1 so Primary assessment (column M) stays blank throughout primary review. The column remains locked. Preparing a checker copy still populates it with the completed primary judgments. The validator requires a blank primary-stage cell and an unchanged checker-stage summary.

The following layout and terminology changes from v.2.1.5.1 are preserved:

1. Remove the optional Related cluster column and its human-review field from snapshots, summaries, inheritance, and exports.
2. Rename Statistical error to `Statistcal_or_numerical issue`, preserving the requested spelling. The internal human-review key is `statisticalIssueStatus`, with `confirmed_issue`, `probable_issue`, `not_issue`, and `indeterminate` verdicts.
3. Use issue terminology throughout field names, option meanings, explanations, examples, instructions, and header comments. Frozen source descriptions and evidence remain verbatim. Software validation failures still use their existing technical terminology.
4. Rename Internal or plan assessment to `Report-internal or planning-material inconsistency`. In the report domain, assess conflicts within the main paper, within the updated supplement, or between them. In the plan-material domain, assess planning materials such as protocol versions or protocol versus SAP. Planned versus reported conduct remains the separate protocol_report domain.
5. Remove `wording_only` from both inconsistency and protocol interpretation dropdowns. Use `minor_presentation` for a small wording or presentation problem with clear intended meaning; use `non_inconsistency` for equivalent wording without an actual conflict. Both modules include these choices and examples. The old `not_inconsistency` and `not_discrepancy` codes are replaced by `non_inconsistency`.
6. Exchange Primary assessment and Notes. After removing Related cluster, Primary assessment occupies M, checker/discussion fields N–Q, and Notes R. Remove `(read only)` from the Primary assessment header while retaining its locked snapshot behavior.

All four annual workbooks and both synthetic 2019 examples have 18 columns. Header height and the two longer field-name column widths increase to keep labels readable. Other field widths, colors, data-row heights, wrapping, and B2 freezing follow the previous version. Codebook field names match the review headers exactly.

Both review stages, saved-answer validation, primary snapshots, summaries, defaults, conditional formatting, and exports use the revised schema (`xlsx-adjudication-8`). Version and revision are v.2.1.5.2. Confirmed/probable substantive statistical findings retain their temporal classification. Protocol/plan findings remain descriptive. Protocol interpretation remains optional.

The catalog is copied from the frozen v.2.1.5.1 catalog. Its 412 candidate records, evidence, AI suggestions, source references, and relationship codes are unchanged. Parent catalog version and signature are recorded. No human answers are imported. Earlier workbooks, including the edited 2019 workbook, are preserved.

Older human-answer workbooks are not accepted by the new schema. In particular, a previous wording_only answer requires a human choice between a minor presentation issue and equivalent wording with no inconsistency. The release does not silently map those answers.

See [USAGE.md](USAGE.md) for review and handoff commands and [VALIDATION.md](VALIDATION.md) for measured checks.
