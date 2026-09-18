# Migration validation — v.2.2.1

Verified 2026-09-17. These checks validate the conversion and blank review templates, not human adjudication or scientific correctness.

## Inventory

| Year | Paper Markdown files | Candidates |
| --- | --- | --- |
| 2018 | 10 | 119 |
| 2019 | 10 | 71 |
| 2024 | 10 | 91 |
| 2025 | 15 | 131 |
| Total | 45 | 412 |

The release contains 50 files, all `.md`: 45 paper files and five shared documents. Each year directory contains exactly one file per paper. No XLSX, HTML, PDF, JSON, or executable file is included in this release.

## Source fidelity

- Parsed the source tables from the frozen v.2.1.5.3 catalog and independently compared them with the corresponding source sheets in all four v.2.1.5.3 annual workbooks. All match.
- Parsed the generated Markdown back into source records. All 412 candidate rows, including every one of the 28 source fields, match the catalog exactly after Markdown escaping is decoded.
- All 1,624 evidence records match by candidate key, order, section, and full text.
- All 1,400 link records match by candidate key, kind, order, label, and destination after accounting for the new relative path depth.
- All 468 relationship records match by candidate key, kind, order, and relationship.
- All 412 candidate keys are unique and appear in the correct year and paper file. Paper year comes from the catalog, including DOI/year mismatches.
- Primary relationship totals remain P_R=45, P_P=50, S_C=65, S_W=252.
- The six candidates without evidence excerpts in jama.2019.14901 are explicitly marked. Their source links remain available. No evidence has been invented to fill the gaps.

## Review forms and navigation

- All eight Primary and Checker / final assessment fields start blank. Both completion markers start as `no`; all checker records, final outcomes, and final counts start blank. No TEST or human answers were imported.
- All 45 paper files have reviewer setup, a candidate index, primary and final assessment columns, checker/discussion fields, result counts, and an unchecked completion checklist.
- All local Markdown navigation, candidate anchors, source links, original Markdown reports, and paper-package paths resolve. Original PDF page fragments are retained; page contents were not re-reviewed during conversion.
- Markdown tables have consistent column counts, and source punctuation is escaped where needed. Evidence remains readable blockquote text. No embedded HTML is required.
- The codebook retains methodological codes and final outcome rules. Usage explains manual applicability checks, completion markers, distinct reviewer identities, preservation of Primary, agreement comparison, discussion resolution, and withheld results until completion.

## Limits

Markdown cannot recalculate counts, validate entries, freeze answers, or reset completion after edits. Reviewers perform the documented checks and preserve a primary backup or recoverable revision. Migration validation does not imply any paper is adjudicated or final. Original source documents remain in their repository locations; sharing the review files alone does not copy those documents.
