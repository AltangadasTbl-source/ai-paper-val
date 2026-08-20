Project path:
  [PROJECT_PATH];local directory (as default)

  Your task is to transform the existing `.ai_paper_validation/final_report.md`
  into a substantially more detailed, source-verifiable English report and then
  render it as `.ai_paper_validation/final_report.html`, replacing any existing
  HTML file with that name.

  Do not browse the web. Use only the supplied article-package files and local
  workflow records. Preserve all source PDFs and workbooks unchanged.

  Before editing
  ==============

  1. Read the applicable AGENTS.md instructions completely.
  2. Inspect at least:
     - `.ai_paper_validation/final_report.md`
     - `.ai_paper_validation/package_manifest.md`
     - `.ai_paper_validation/candidate_set.md`
     - `.ai_paper_validation/checker_outputs/`
     - `.ai_paper_validation/verification/evidence_verifier_output.md`
     - `.ai_paper_validation/critic/critic_output.md`
     - `.ai_paper_validation/document_outputs/`
     - Every original source file cited by the report
  3. Confirm the mapping between internal document identifiers and actual source
     filenames using `package_manifest.md` and the files on disk.
  4. Where practical, compare source-file hashes with those recorded in the
     package manifest.
  5. Re-read the cited original PDF pages, tables, figures, workbook sheets, and
     cells. Do not merely expand the wording of the existing report.
  6. Do not modify checker, verifier, critic, manifest, or source-document records
     unless the user explicitly requests those changes.

  Evidence and classification rules
  =================================

  For every C01-C10 candidate, independently determine whether it is:

  - Verified
  - Uncertain
  - Rejected

  Use these definitions:

  - Verified: The inconsistency can be reproduced directly from the supplied
    files without relying on an unstated statistical test, external convention,
    speculative correction, or assumed production mechanism.
  - Uncertain: The printed values are confirmed, but the claimed inconsistency
    depends on an inferential assumption or definition not supplied in the
    package.
  - Rejected: The source files do not support the candidate as formulated.

  Do not automatically preserve the previous verifier or critic disposition.
  If close reading changes a disposition, explain the change explicitly in an
  “Audit Method and Revision Status” section.

  Examples of required caution:

  - Do not assume a P value tests `H0: coefficient = 0` unless the table, methods,
    model output, or an unambiguous presentation establishes that interpretation.
  - Do not assume a P value and confidence interval use the same test,
    sidedness, variance estimator, or degrees-of-freedom correction.
  - Diagnostic calculations may be shown, but label them as diagnostic rather
    than authoritative replacements.
  - Do not infer corrected cell values, row labels, column assignments, analytic
    denominators, or production-error mechanisms unless the supplied files
    establish them.
  - Distinguish a directly verified inconsistency from an uncertain explanation
    of how it occurred.
  - Do not treat differences between medians as if they must equal differences
    between means.
  - Preserve the project’s allowed issue taxonomy and candidate limits.

  Source-location requirements
  ============================

  Do not use opaque identifiers such as `DOC-001-MAIN` or `DOC-005-RESULTS` in
  the final report.

  Instead, use the complete actual source filename everywhere, for example:

  [joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf),
  PDF p. 8, eTable 3.

  For spreadsheets, include:

  - Actual workbook filename
  - Worksheet name
  - Exact cells or ranges

  For PDFs, include:

  - Actual filename
  - PDF page
  - Journal page when available
  - Table, figure, section, row, column, or footnote label

  Make every filename a relative Markdown link to the original source file so
  that it remains clickable in both Markdown and rendered HTML.

  Required report structure
  =========================

  Retain and update these sections:

  1. Package Manifest
  2. AI Training Restriction Summary
  3. Audit Method and Revision Status
  4. Candidate Disposition Summary
  5. Verified Scientific Findings
  6. Uncertain Candidates
  7. Rejected and Excluded Interpretations
  8. Human Adjudication Checklist

  Keep the AI Training Restriction Summary separate from the scientific issue
  list.

  The Candidate Disposition Summary must contain every candidate and show:

  | Candidate | Disposition | Category | Severity |

  For every candidate, provide at least the following detail:

  ## Cxx — Concise descriptive title

  - Evidence status
  - Category
  - Severity, or potential severity if uncertain
  - Exact source location using actual filenames
  - Reported values/statements

  **Reasoning procedure**

  1. Identify exactly which source values or statements are being compared.
  2. Explain why those values should reconcile or agree.
  3. Show every relevant calculation explicitly.
  4. Perform within-table, between-table, figure, text, workbook, or
     cross-document checks as applicable.
  5. State which portions are direct source observations and which are derived
     calculations.
  6. Explain alternative interpretations that were considered.
  7. State why those alternatives are supported, unsupported, or unresolved.

  Then provide:

  - Supported conclusion
  - Limit on interpretation
  - Verification instruction

  Required level of detail
  ========================

  The revised report must be at least as detailed as the following examples:

  - For participant-flow findings, show the overall and arm-specific sums,
    identify mutually exclusive categories, compare them with randomized and
    follow-up totals, and cross-check figures and workbook partitions.
  - For arithmetic findings, identify the denominator rule, calculate the
    denominator, reproduce the percentage, reconcile row and column totals, and
    search the workbook for possible alternative occurrences.
  - For confidence-interval findings, show point-estimate containment checks,
    endpoint-order checks, or sign-preservation logic explicitly.
  - For duplicated rows, compare the label, time point, estimate, CI, and P value.
  - For ambiguous labels, list the duplicate labels and their distinct estimates.
  - For cross-text/table findings, match the outcome, time point, comparison, and
    displayed precision before declaring a discrepancy.
  - For uncertain statistical findings, state the exact missing inferential
    definition and what model output is required to resolve it.

  Do not use vague statements such as “the numbers do not match” without showing
  the calculations.

  Editing requirements
  ====================

  1. Write the report in clear professional English.
  2. Preserve exact source values and quotations.
  3. Do not silently change severity or disposition.
  4. Do not introduce new findings outside the approved candidate set.
  5. Do not modify original PDFs or workbooks.
  6. Ensure no `DOC-xxx` references remain in `final_report.md`.
  7. Preserve clickable relative source links.
  8. Do not regenerate or modify a PDF unless explicitly requested.

  HTML rendering
  ==============

  After completing and validating `final_report.md`, replace:

  `.ai_paper_validation/final_report.html`

  with a standalone UTF-8 HTML5 rendering of the revised Markdown.

  Prefer Pandoc and use:

  pandoc \
    --from=gfm \
    --to=html5 \
    --standalone \
    --toc \
    --toc-depth=3 \
    --metadata title="AI Paper Validation Final Report" \
    --variable maxwidth=90em \
    --output=final_report.html \
    final_report.md

  Run the command from `.ai_paper_validation/` so the relative source links
  remain valid.

  If Pandoc is unavailable, use another reliable Markdown-to-HTML renderer, but
  the result must still be:

  - Standalone HTML5
  - UTF-8
  - Equipped with a table of contents
  - Saved as `final_report.html`
  - Linked correctly to the original local files

  Final validation
  ================

  Before reporting completion, verify all of the following:

  1. Every candidate C01-C10 has a detailed disposition.
  2. Verified and Uncertain candidates are in separate sections.
  3. All calculations are reproducible from printed values.
  4. All limitations and unsupported mechanisms are explicit.
  5. No `DOC-xxx` identifier remains in Markdown or HTML.
  6. Every relative PDF/XLSX link resolves to an existing file.
  7. The HTML contains the revised findings and table of contents.
  8. `final_report.html` is valid UTF-8 HTML.
  9. Source PDFs and workbooks remain unchanged.
  10. `git diff --check` reports no newly introduced formatting errors.

  In your final response, provide clickable links to:

  - `final_report.md`
  - `final_report.html`

  Also summarize:

  - Number of Verified, Uncertain, and Rejected candidates
  - Any material disposition changes
  - Confirmation that source files were not modified