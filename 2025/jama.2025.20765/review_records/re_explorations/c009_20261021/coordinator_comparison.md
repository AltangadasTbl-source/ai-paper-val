# C009 targeted re-exploration and record comparison

Date: 2026-10-21. This is a bounded follow-up, not a complete Workflow 1.6.2 rerun. C009 remains Pending Human Adjudication; no original record or source was rewritten.

## Scope and independence

The existing C009 ledger entry was used to locate the question. The coordinator directly inspected the protocol passages, surrounding economic subsections, SAP primary rule, article missing-outcome paragraph, Figure 1 and Table 2; detailed historical conclusions were then compared. A fresh source-only evidence rechecker, `/root/c009_source_independent` (named gpt-6.1-sol/high role), was instructed not to read any earlier candidate, checker, screening, recheck, audit, report, or re-exploration conclusions. Its full evidence is in independent_source_check.md.

Direct pdftotext produced main_p3_p4_layout.txt and main_p6_layout.txt. Direct pdftoppm rendered targeted pages on CPU. Existing source-matched images of plan pp28,66,77,91 and article p4 were reused. The character-encoded plan native extraction was not treated as evidence authority. No web, new OCR, custom Python, raw data or model refitting was used.

## Direct-source result

1. PLAN Supplement 1 PDF p28, printed p28, heading 11.2.2 Statistical analysis, lines 759-764, and PDF p66, printed p25, heading 28.2.2 Statistical analysis, lines 2011-2016, state that outcomes will primarily be analysed in a missing-at-random architecture using generalised linear mixed models. The two statements are one repeated pattern.
2. Their preceding economic subsection concerns costs and QALYs. Directly read pp27-28 and65-66 show Statistical analysis as a separate sibling subsection rather than text within the cost-effectiveness subsection. Its broad Outcomes wording is not expressly restricted to economic outcomes or missing covariates. Its exact primary-abstinence scope is nevertheless not spelled out.
3. PLAN SAP PDF p91, printed SAP p14, section 30, lines 2890-2892 explicitly states an ITT primary analysis and says dropouts/incomplete data will be regarded as continuing smokers. SAP p92, section37, separately repeats the regression after excluding missing primary outcomes.
4. REPORT article PDF p3, printed p338, Statistical Analysis, explicitly treats missing primary outcomes as negative/not abstinent and separately describes complete-case analysis discarding missing primary outcomes. Thus SAP and report agree on the reported primary rule.
5. REPORT Figure1, PDF p4, printed p339, and Table2, PDF p6, printed p341, reconcile exactly. No count discrepancy is asserted.

| Quantity | mHealth | Usual care |
|---|---:|---:|
| Randomized and retained in primary ITT | 720 | 360 |
| Died | 25 | 27 |
| No contact | 18 | 9 |
| Withdrew | 10 | 6 |
| Missing primary outcomes | 53 | 42 |
| Available-outcome denominators | 667 | 318 |
| CO<10 ITT abstinent numerator | 300 | 55 |
| CO<10 available-outcome abstinent numerator | 300 | 55 |

53+42=95; 95/1080=8.7963%, agreeing with the printed 8.8%. The complete-case denominators are 720-53=667 and360-42=318. Table2 labels the available-outcome row PP, whereas the methods describe complete-case exclusion; no new label issue is registered here. The primary ITT RR is 3.0 (95% CI2.0-4.9); the available-outcome row prints RR2.9 (95% CI2.0-4.7). Their presence does not identify either as a specified MAR implementation.

## Existing-record trajectory

| Record | C009 handling |
|---|---|
| checkers/cross_source_consistency.md line47, F-XS-002 | Identifies protocol MAR wording versus SAP/report negative assignment; RouteB. |
| checkers/statistical_pass_1.md line80, F-ST1-004 / S089 | Independently identifies the same specification comparison. |
| screening/inclusion_screen.md lines18,33 and51,66 | Both INCLUDE / MEETS_THRESHOLD; consolidated as C009. |
| verification/evidence_recheck.md line273 | Source statements confirmed; reproduced; no classification correction. Historical PENDING_AUDIT predates the final audit. |
| checkers/statistical_pass_2.md line323, S089 | PASS_2_COMPLETE; retains existing C009; counts reconcile without a bias calculation. |
| quality/evidence_quality_audit.md line397 | CONFIRMED inclusion audit, RouteB, retaining economic-scope and supersession alternatives. |
| final_report_1_6_2.md line632 | Retains C009 as protocol_report / P_R; all relationships P_R,P_P; reproduced; CONFIRMED; Pending Human Adjudication. |

Paths except the final report are relative to .ai_paper_validation/review_1_6_2/. The final report is in .ai_paper_validation/.

## Independent interpretation

The reproduced issue is the unresolved scope and correspondence of two printed analysis specifications. The article clearly states its primary missing-as-not-abstinent rule. The missing definition is how the protocol's broadly stated MAR framework relates to that rule, rather than what rule the report describes.

MAR is a missingness mechanism/framework; assigning missing primary outcomes to nonabstinence is an operational analysis rule. Their names are not universally mathematically incompatible. They could relate to different outcomes, covariates, estimands or sensitivity analyses. Neither the source counts nor an ITT label establishes a particular MAR-based implementation. Complete-case analysis does not automatically supply the missing mapping.

Economic adjacency is a substantive alternative, but the separate sibling headings and unrestricted Outcomes sentence do not establish an economic-only restriction. SAP replacement is also possible; p77's change statement contains no missing-outcome amendment, and p28 itself bears a V6.0 header. Bundle order alone does not establish which specification superseded another or when it was finalized relative to data access. No claim about an undisclosed change or prespecification timing follows.

For this bounded issue, the source-only rechecker independently supports reproduced, focusD, RouteB. Protocol versus article yields P_R; protocol versus SAP yields P_P; P_R has precedence, producing protocol_report. SAP/article agreement and the flow diagram's corroboration supply no additional S_C or S_W conflict.

## Bounded downstream impact

The recorded review domain is protocol_report, not statistical_results. An evidence extractor could attach MAR-based handling or missing-as-nonabstinent handling to the same primary RR. The latter is explicitly reported; whether and how it supersedes or instantiates the protocol framework is not mapped. Coding analysis provenance and distinguishing the 720/360 ITT denominators from the 667/318 available-outcome denominators can affect reuse. No alternative MAR-based estimate, numerical effect of switching rules, bias direction, statistical-significance change or evidence-synthesis conclusion change can be established from the supplied materials. Missing-as-smoking should not automatically be described as conservative from these counts.

## Integrity and execution deviation

Source SHA-256 checks against source_hashes_before.sha256 passed before and after exploration for all three supplied PDFs. Checks of every listed reusable artifact against reused_artifact_hashes_before.sha256 produced no failure. Existing review records were not edited.

The independent subtask initially created exactly ten new CPU-rendered PNGs, uniquely prefixed c009-independent-, under .ai_paper_validation/review_1_6_2/preprocessing/, contrary to the user's narrower write restriction. The coordinator moved only those ten new files into this directory with non-overwriting moves and confirmed no c009-independent files remained in the old directory. The subtask confirmed no other outside artifacts were created. This deviation was disclosed in the session. All final new artifacts reside in review_records/re_explorations/c009_20261021/; this statement does not claim that no temporary outside write occurred.
