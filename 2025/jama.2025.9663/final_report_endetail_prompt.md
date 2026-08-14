Project path:
  [PROJECT_PATH];local directory (as default)

  Your task is to transform the existing `.ai_paper_validation/final_report.md`
  into a substantially more detailed, source-verifiable English report and then
  render it as `.ai_paper_validation/final_report.html`, replacing any existing
  HTML file with that name.

  Do not browse the web. Use only the supplied article-package files and local
  workflow records. Preserve all source PDFs and workbooks unchanged.

  This is a verification-and-explanation task only. The candidate dispositions,
  categories, severities, and critic inclusion decisions already recorded by the
  completed workflow are locked. Do not perform a second adjudication and do not
  change, override, add to, or remove any scientific decision.

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

  Locked dispositions and verification-only rules
  ===============================================

  Treat the completed evidence-verifier and critic records as authoritative:

  - The evidence-verifier output controls each formal candidate's disposition:
    `Verified`, `Uncertain`, or `Rejected`.
  - The critic output controls which verified findings remain in the final
    scientific finding list and controls their retained category and severity.
  - The existing final report is a report-generation artifact. If it conflicts
    with the evidence-verifier or critic output, reproduce the authoritative
    verifier/critic decision and describe the record conflict without making a
    new scientific judgment.

  For every formal candidate actually present in the authoritative workflow
  records, do only the following:

  1. Verify that the cited source locations, quotations, values, and calculations
     can be found or reproduced from the supplied files.
  2. Explain the reasoning already supporting the locked disposition.
  3. Expand the evidence trail, limitations, and human verification instruction
     without changing the decision.

  Prohibited actions:

  - Do not independently re-adjudicate any candidate.
  - Do not change a disposition, category, severity, critic acceptance decision,
    or candidate scope, whether silently or explicitly.
  - Do not promote a Rejected or Uncertain candidate to Verified.
  - Do not demote a Verified candidate to Uncertain or Rejected.
  - Do not convert a verifier-rejected item into an excluded interpretation with
    a different substantive judgment, or vice versa.
  - Do not introduce a new candidate, finding, correction, or error mechanism.
  - Do not fabricate unused candidates or placeholder decisions merely to fill
    the C01-C10 maximum. If the workflow contains fewer than 10 formal
    candidates, report only the candidates that actually exist.

  If a cited source cannot be located, a value cannot be reproduced, or the
  report appears to conflict with the source, do not change the locked decision
  and do not create a new Uncertain disposition. Record a clearly labeled
  `Source-verification exception requiring Human Adjudication` in “Audit Method
  and Revision Status,” state exactly what could not be verified, and preserve
  the authoritative disposition unchanged.

  The meanings of `Verified`, `Uncertain`, and `Rejected` may be explained for
  readers, but they must not be reapplied to reach a new disposition during this
  report-detailing task.

  Examples of required caution while verifying and explaining the locked
  decisions:

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
  - Use diagnostic checks only to explain an existing decision; never use them
    to replace or revise that decision.

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

  Every PDF evidence link must be a page-level deep link, not merely a link to
  the beginning of the PDF. Append the standard PDF fragment `#page=N`, where
  `N` is the one-based PDF page containing the cited evidence. The visible link
  text must contain the complete actual filename, PDF page number, and the table,
  figure, section, row, or footnote label when applicable. For example:

  [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 8, eTable 3](../joi250046supp4_prod_1755300121.15587.pdf#page=8)

  If one sentence cites evidence on multiple PDF pages, create a separate deep
  link for every page. Do not use one file-level hyperlink followed by unlinked
  page references. Thus eFigure 4 on PDF p. 11 and eFigure 5 on PDF p. 12 must
  have separate `#page=11` and `#page=12` links. General package-manifest links
  that identify a document without citing evidence may remain file-level links.

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

  Copy these fields from the authoritative verifier and critic records. Preserve
  the number and order of the formal candidates. Do not assume that all ten
  possible candidate slots were used, and do not create Cxx entries that are not
  present in the completed workflow.

  For every candidate, provide at least the following detail:

  ## Cxx — Concise descriptive title

  - Evidence status
  - Category
  - Severity, or potential severity if uncertain
  - Exact source location using actual filenames
  - Reported values/statements

  **Reasoning procedure**

  1. Identify exactly which source values or statements are being compared.
  2. Explain why the verifier or critic determined that those values should
     reconcile or agree, as applicable to the locked disposition.
  3. Show every relevant calculation explicitly.
  4. Perform within-table, between-table, figure, text, workbook, or
     cross-document checks as applicable.
  5. State which portions are direct source observations and which are derived
     calculations.
  6. Explain alternative interpretations recorded by the completed workflow or
     directly needed to explain its decision.
  7. State how those alternatives support the existing disposition; do not use
     them to reach a different disposition.

  Then provide:

  - Existing supported conclusion
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
  3. Do not change any severity, disposition, category, critic acceptance
     decision, or candidate scope. This prohibition applies to both silent and
     explicitly explained changes.
  4. Do not introduce new findings outside the approved candidate set.
  5. Do not modify original PDFs or workbooks.
  6. Ensure no `DOC-xxx` references remain in `final_report.md`.
  7. Preserve clickable relative source links.
  7a. Use `#page=N` deep links for every cited PDF page and a separate link for
      each cited page; include the complete filename, PDF page, and evidence
      label in the visible link text.
  8. Do not regenerate or modify a PDF unless explicitly requested.
  9. Preserve the authoritative candidate count and candidate order; do not add
     unused Cxx placeholders.

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

  1. Every formal candidate actually present in the authoritative verifier output
     has a detailed explanation, and no unused candidate placeholder was added.
  2. Every disposition exactly matches the evidence-verifier output.
  3. Every retained finding, category, and severity exactly matches the critic
     output.
  4. No candidate was re-adjudicated, promoted, demoted, added, removed, or
     substantively reframed.
  5. Verified and Uncertain candidates are in separate sections when both exist.
  6. All displayed calculations are reproducible from printed values and are used
     only to explain the locked decisions.
  7. All limitations, unsupported mechanisms, and source-verification exceptions
     are explicit.
  8. No `DOC-xxx` identifier remains in Markdown or HTML.
  9. Every relative PDF/XLSX link resolves to an existing file.
  9a. Every PDF evidence link includes the correct one-based `#page=N` fragment,
      and multi-page evidence uses one independently clickable link per page.
  10. The HTML contains the revised findings and table of contents.
  11. `final_report.html` is valid UTF-8 HTML.
  12. Source PDFs and workbooks remain unchanged.
  13. `git diff --check` reports no newly introduced formatting errors.

  In your final response, provide clickable links to:

  - `final_report.md`
  - `final_report.html`

  Also summarize:

  - Number of Verified, Uncertain, and Rejected candidates, exactly matching the
    authoritative verifier output
  - Confirmation that no disposition, category, severity, candidate, or critic
    decision was changed
  - Any source-verification exception requiring Human Adjudication, without
    changing the locked decision
  - Confirmation that source files were not modified
