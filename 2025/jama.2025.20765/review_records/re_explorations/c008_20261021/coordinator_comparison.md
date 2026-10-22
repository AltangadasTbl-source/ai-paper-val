# C008 targeted source re-exploration and historical-record comparison

Date: 2026-10-21. This is a bounded follow-up, not a new complete Workflow 1.6.2 review or a human adjudication. Existing sources and review artifacts remain unchanged. All new files are confined to this directory.

## Independence and methods

The coordinator used the existing C008 registration to locate its question, then directly inspected the source-matched SAP p84 image, newly rendered Table 2 p6 and eTable 9 p13, native source text, the main methods and result context. A fresh source-only specialist, `/root/c008_source_independent`, separately investigated the sources without reading any previous ledger, screening, checker, recheck, audit or final-report conclusions. Its complete artifact is `independent_source_check.md`.

Direct Poppler pdftotext produced main_p3_p4_layout.txt, main_p6_layout.txt, and supp_p13_p14_layout.txt. Direct pdftoppm produced the source-page images and the targeted PP-cell render. Rendering used CPU; no OCR, external sources, fallback environment or custom Python was used. The existing plan page image was used only as a source-matched visual derivative, not as an earlier scientific conclusion.

## Direct-source observations

- PLAN Supplement 1 PDF p84, printed SAP p7, lines 2656-2660: the six-month primary endpoint uses biochemical verification by CO<10 ppm.
- Main REPORT PDF p3, printed p338: the Trial Outcomes definition also uses CO<10 ppm. Statistical Analysis explicitly says: "A post hoc sensitivity analysis using a carbon monoxide cutoff of less than 6 ppm was performed for the primary outcome."
- Main REPORT PDF pp4-5 distinguishes its CO<6 post hoc analysis, RR 3.7 (95% CI 2.4-5.8), from the primary analysis. The primary CO<10 ITT result is 300/720 versus 55/360, RR 3.0 (95% CI 2.0-4.9).
- Main REPORT PDF p6, printed p341, Table 2: the singular Primary outcome block contains CO<10 ITT/PP, CO<6 ITT/PP, and self-report-only analyses. Thus block membership alone does not establish separate planned primary endpoints.
- Results REPORT PDF p13: eTable 9 is explicitly titled "Post-hoc sensitivity analysis (intention to treat) after excluding deaths". Its Primary outcomes block includes both CO<10 and CO<6 rows.

## Direct transcription of the CO<6 rows

| Display and analysis | mHealth | Usual care | Printed RR (95% CI) | Printed adjusted RR (95% CI) |
|---|---|---|---|---|
| Main Table 2, ITT | 264/720 | 38/360 | 3.7 (2.4-5.8) | 3.9 (2.4-6.9) |
| Main Table 2, PP | 264/667 | **38/318** | 3.6 (2.14-6.87) | 3.8 (2.3-7.7) |
| eTable 9, excluding deaths | 264/695 | 38/333 | 3.6 (2.4-5.4) | 3.8 (2.4-6.2) |

Table 2's PP usual-care percentage is 11.9 (8.6 to 16.1). Both coordinator and independent specialist read 38/318 directly. Native extraction agrees; pdftotext -bbox identifies the word 38/318 at xMin=182.641357, yMin=437.377766, xMax=188.648113, yMax=459.442118 on PDF p6 (PDF point coordinates). The targeted source render is main_p6_pp_cell.png. Arithmetic 100*38/318=11.9496855%, which rounds to the printed 11.9%.

## Existing-record trajectory

1. Statistical pass 1, F-ST1-008, registered the proposition that a post hoc CO<6 sensitivity was presented as primary. It invoked Route A category 5 and proposed P_R and S_C.
2. Initial screening retained that finding as INCLUDE / MEETS_THRESHOLD and assigned C008. The cross-source checker separately excluded the same grouping observation as TERMINOLOGY_OR_WORDING because the immediate context identifies sensitivity analysis; this disagreement already existed at the initial review stage.
3. Evidence recheck expanded the affected main-table locations to both CO<6 rows and added S_W. It recorded reproduced_after_transcription_correction because the main p6 location had been characterized as a sensitivity-definition passage whereas it actually contains the primary block. This state refers to the documented source-location/context correction, not an alteration of the trial's data or outcome threshold.
4. Statistical pass 2 retained the already registered issue without a new duplicate finding.
5. The quality audit questioned the inclusion premise: the headings and thresholds exist, but actual formal outcome-status promotion is not established. It recorded QUESTIONED while preserving the initial INCLUDE row and stable C008.
6. Final ledger and report retain protocol_report / P_R, all relationships P_R, S_C, S_W; evidence state reproduced_after_transcription_correction; inclusion audit QUESTIONED; Pending Human Adjudication. These are historical recorded fields, not a fresh independent confirmation that all alleged conflicts exist.

Record locators: checkers/statistical_pass_1.md line 140; checkers/cross_source_consistency.md line 220; screening/inclusion_screen.md lines 37 and 70; verification/evidence_recheck.md line 241; quality/evidence_quality_audit.md line 357; final_report_1_6_2.md line 574. All but the last path are relative to .ai_paper_validation/review_1_6_2/; the final report is directly in .ai_paper_validation/.

## Source-versus-record transcription discrepancy

The historical recheck, ledger, audit and final report print **39/318** for the Table 2 CO<6 PP usual-care cell, sometimes calling it literally printed. The supplied PDF instead reads **38/318**, confirmed visually and by direct native extraction. The historical audit's auxiliary calculation based on 39/318 therefore does not describe the source cell. This observation concerns the review's transcription; it supplies no evidence of a participant-count discrepancy in the article. Existing records were preserved, not rewritten.

## Independent interpretation

The table grouping is directly reproduced. The further proposition that CO<6 became a planned primary endpoint is not reproduced by the source context. Methods, result narrative, and the supplement caption distinguish post hoc sensitivity from the primary CO<10 analysis. Route A5 requires an actual status change, not merely membership in a table block; Route B's unresolved-context premise is also not established here. The source-only specialist independently reached this bounded conclusion and identified NOT_REPRODUCED for the proposed status-change proposition. This is not a replacement screening row and does not delete C008 or decide a human disposition.

The final report retains its original route argument alongside the later QUESTIONED audit. The preserved route/evidence-state fields should not be read alone as confirmation that endpoint hierarchy changed. The registered P_R/S_C/S_W structure likewise depends on treating block headings as formal status designations; if the headings simply group analyses of the primary construct, the SAP corroborates the defined endpoint instead of furnishing a conflicting comparator.

## Bounded downstream implications

C008's recorded domain is protocol_report, not statistical_results. Potential extraction implications concern CO threshold, analysis population and primary-versus-post-hoc metadata. A reader extracting only a block heading might choose a CO<6 result in place of the explicit CO<10 primary result, or duplicate related analyses as independent outcomes. The supplied package does not show that such propagation occurred or changed an evidence synthesis. No estimate, interval or conclusion change is established by the grouping observation. Separately, reusing 39/318 from the historical review would transmit a transcription inconsistent with the source; the direct-source cell is 38/318.

## Integrity and limits

The three original PDF SHA-256 values were checked against .ai_paper_validation/review_1_6_2/source_hashes_before.sha256 both before and after exploration; all passed. This investigation covers C008 and its cited source context, not all 109 plan pages or a raw-data/model audit. No new candidate IDs, severity labels, or human adjudications were assigned.
