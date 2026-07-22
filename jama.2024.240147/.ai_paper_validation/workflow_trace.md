# Workflow Trace

Run date: 2026-07-21
Status: Human Adjudication Required

## Coordinator stages

- Package inventory: complete; 5 PDFs assigned DOC-001 through DOC-005.
- AI-use restriction screen: complete for every PDF. DOC-001 classified Explicit AI Training Restriction and withheld from scientific agents.
- PDF preprocessing: native extraction completed for all PDFs. DOC-003 pages 13-25 selectively rendered; OCR was not indicated.

## Specialist stages

- main_text_extractor: DOC-001 Not Audited pending Human Compliance Review; no scientific claims extracted.
- supplement_table_checker: DOC-003 reviewed; 7 local candidates returned.
- figure_flow_checker: DOC-003 reviewed; eFigure had no unambiguous issue; 7 local candidates returned, overlapping table findings.
- statistical_consistency_checker: DOC-003 reviewed; 5 local candidates plus 1 uncertain cross-table observation returned.

## Consolidation and verification

- Coordinator deduplicated and prioritized 10 candidates.
- Two low-priority local one-decimal rounding observations were not promoted: 14/69 (20.2%) on DOC-003 p. 20 and 87/758 (11.4%) on DOC-003 p. 25.
- evidence_verifier completed one round: 9 Verified, 1 Uncertain, 0 Rejected.
- critic retained 9 supported scientific findings: 1 Major and 8 Minor. C10 remained Uncertain.
- report_generator produced the human-adjudication report without adding findings.

The initial compliance-limited pass observed its 10-candidate, single-verification, single-critic, and 10-final-issue limits.

## Full-scope continuation

- On 2026-07-21, the user explicitly instructed continuation with DOC-001 included.
- DOC-001 pages 1-11 were rendered and visually checked; OCR was not indicated.
- main_text_extractor, supplement_table_checker, figure_flow_checker, and statistical_consistency_checker were rerun in parallel across the cleared main article/results-supplement scope.
- No specific report-to-protocol question was triggered; DOC-002 remained Not Audited by Design.
- The coordinator deduplicated and prioritized 10 full-scope candidates.
- The full-scope evidence verification completed in one round: 9 Verified, 1 Uncertain, 0 Rejected.
- The full-scope critic retained 8 supported findings (1 Major, 7 Minor), retained F3 as Uncertain, and rejected F10.
- The initial compliance-limited report was archived as `archive/final_report_compliance_limited.md`.
- report_generator produced the replacement full-scope human-adjudication report without adding findings.

The full-scope continuation observed its 10-candidate, single-verification, single-critic, and 10-final-issue limits.
