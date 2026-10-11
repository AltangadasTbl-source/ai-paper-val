# Workflow 1.6.1 Independent Initial Inclusion Screen

Fresh screener runtime ID: 01a128e5-2413-7142-a2ea-ee880aee0ed9; gpt-6.1-sol/high. Scope: every finding in the current numeric, cross-source, and statistical pass-1 checker artifacts. The numeric checker emits no finding; the other checkers emit eight findings. All cited locations were independently reread from the supplied PDFs using fresh Poppler layout extraction, with visual confirmation of protocol pp.16,23,28,43 and SAP p.4. Decisions apply all four criteria and the comparison tiers of QUALITY_CONTROL_SCOPE.md, without a count target. No legacy conclusions or external evidence were used.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-ST1-003 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C004 |

- F-XS-001: The protocol and report give materially different numerical assumptions and powering contrasts for the primary MDD design, without explaining how the interaction-oriented 30%/15%,20%-dropout specification relates to the main-effect 30%/20%,22%-attrition specification; the operative design assumptions accompanying the primary null result therefore remain unreconciled.
- F-XS-002: The protocol explicitly defines EPA+DHA as 1.0 g/day, whereas both results documents define 1412 mg/day for the same one-year intervention, exceeding the protocol's stated 125% upper manufacturing tolerance and changing dose extraction.
- F-XS-003: Although the SAP clearly specifies the reported primary logistic analysis, its explicit planned secondary Cox analysis remains designated post hoc in the report, and the supplied protocol also assigns different primary-model priority, changing the prospective status attached to the reported MDD estimates.
- F-XS-004: IDS is placed both among the protocol's main endpoints and in its primary-analysis subsection, but in the SAP/report it is secondary and interpreted as exploratory, leaving a substantive endpoint-hierarchy difference for the reported IDS effect rather than only an interchangeable outcome name.
- F-XS-005: The SAP unconditionally specifies an additive-interaction RERI sensitivity analysis and confidence interval for primary MDD, while the supplied results contain only multiplicative interaction and other sensitivity analyses, so the explicitly planned primary-outcome sensitivity is not reported or reconciled.
- F-ST1-001: Independent rereading reproduces the same primary-MDD power-specification issue as F-XS-001, retained as a second included provenance row for their single consolidated issue.
- F-ST1-002: Independent rereading reproduces the same MDD model-priority and Cox-prespecification issue as F-XS-003, retained as a second included provenance row for their single consolidated issue.
- F-ST1-003: Independent rereading reproduces the same IDS endpoint-hierarchy issue as F-XS-004, retained as a second included provenance row for their single consolidated issue.

Eight findings screened; eight included finding rows; five consolidated included issues; zero screened-out finding rows. Several INCLUDE rows will share one coordinator-assigned stable ID: F-XS-001/F-ST1-001, F-XS-003/F-ST1-002, and F-XS-004/F-ST1-003. The coordinator registered C001-C005 in the proposed source order and populated every INCLUDE row. The detailed independent evidence, all affected locations, classification, alternatives, and deterministic source-order proposal are in initial_working_notes.md. All five issues remain Pending Human Adjudication.

Screened-out counts are zero for each normative reason code: NOT_REPRODUCED; ROUNDING_OR_DISPLAY_PRECISION; NOTATION_OR_TYPOGRAPHY; TERMINOLOGY_OR_WORDING; MODEL_VERSUS_CRUDE; CONTEXT_RESOLVES; CONDITIONAL_OR_UNREPORTED; PERIPHERAL_COMPARISON; OUT_OF_FOCUS; DUPLICATE_OF_INCLUDED. Consolidation uses shared INCLUDE provenance, as permitted by the review contract, rather than separate duplicate candidates.
