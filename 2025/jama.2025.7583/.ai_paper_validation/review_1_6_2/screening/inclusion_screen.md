# Independent initial inclusion screen

Runtime ID: 01a12bd0-1da8-7853-a91b-e1e467622b2b. Model: gpt-6.1-sol; reasoning effort: high; start mode: FRESH_SPAWN. Assigned scope: all nine findings in the completed fresh numeric, cross-source and statistical-pass-1 checker artifacts. QUALITY_CONTROL_SCOPE.md, the complete review contract and settings were read. Every cited source location was independently reread; decisions use the supplied sources and the two-route threshold, with no count target or legacy conclusions. Candidate registration remains with the coordinator; PENDING is a registration placeholder, not a stable ID.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-003 | cross_source_consistency_reviewer | initial | SCREENED_OUT | TERMINOLOGY_OR_WORDING | — |
| F-XS-004 | cross_source_consistency_reviewer | initial | SCREENED_OUT | CONTEXT_RESOLVES | — |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-ST1-003 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C001 |

## One-sentence justifications

- **F-NUM-001 — G4:** Route A, category 3, applies to the reproduced within-table sample constraint because both midline-shift samples of 161 exceed the stated unilateral populations of 127 and 130 after half-unit intervals, with relative gaps 0.204969 and 0.186335, leaving the samples underlying the two medians unclear.
- **F-XS-001 — G2:** Route A, category 5, applies because the SAP's visually confirmed >5-mm boundary and the protocol/report's ≥5-mm boundary define different primary-composite inclusion sets at exactly 5 mm, without asserting a participant-count change.
- **F-XS-002 — G3:** Route A, category 5, applies because the original protocol's all-death failure rule differs from the reported cause-restricted primary composite, while the final SAP expressly documents the amendment and corroborates the reported definition.
- **F-XS-003:** The report retains all five categories as secondary endpoints in its endpoint list and Table 2, and its immediate explanation that uncorrected secondary/subgroup analyses should be considered exploratory is inferential caution rather than a reproduced change of formal outcome status, so category 5 does not apply.
- **F-XS-004:** The report explicitly identifies evaluation of the planned center component, its estimated zero variance and the resulting stated primary model, so no missing planned primary comparison is reproduced for category 5 and the immediate explanation resolves the model representation without changing an extractable result.
- **F-XS-005 — G1:** Route A, category 5, applies because the protocol and SAP explicitly prescribe a between-arm minor/major complication comparison for an abstract-listed key secondary endpoint, whereas the supplied reports provide only intervention-arm counts and no comparative result.
- **F-ST1-001 — G3:** Route A, category 5, applies to the same reproduced all-death versus cause-restricted composite change as F-XS-002, preserving the additional SAP interim-rule location and the disclosed final-version amendment in that single issue.
- **F-ST1-002 — G2:** Route A, category 5, applies to the same reproduced strict versus inclusive primary-composite boundary as F-XS-001, and all protocol, SAP and report occurrences are retained in that single issue.
- **F-ST1-003 — G1:** Route A, category 5, applies to the same unreported planned key secondary complication comparison as F-XS-005, retaining both plan specifications and every cited report occurrence in that single issue.

## Consolidated issue groups for coordinator registration

Groups below are handoff labels only; the coordinator assigns stable C IDs. Multiple INCLUDE rows within a group map to one candidate. The source-order key uses the first affected REPORT location in the source inventory's document order, then physical page and within-page section; it does not rank the issues.

### G1 — Planned complication comparison has no supplied comparative result

- **Finding provenance:** F-XS-005; F-ST1-003.
- **Source-order key:** DOC-001-MAIN, PDF p. 1, abstract Main Outcomes and Measures/Results.
- **Qualifying route:** Route A, category 5.
- **Proposed domain:** protocol_report.
- **Compared roles:** PLAN protocol and SAP versus REPORT main article and results supplement.
- **Proposed primary relationship / All relationships:** P_R / P_R; the two plans agree and the two reports agree, so neither matching pair adds a conflicting relationship.
- **Issue statement:** The supplied plan specifies a between-arm chi-square/Fisher comparison of minor and major procedure complications, but the abstract-listed endpoint is reported with intervention-arm risks alone.
- **All affected locations:** PLAN [protocol p. 50, secondary-endpoint analysis](../../../joi250033supp1_prod_1750956987.76581.pdf#page=50); PLAN [SAP p. 4, secondary endpoints](../../../joi250033supp5_prod_1750956987.78281.pdf#page=4), [p. 7, section 3.6 fifth bullet](../../../joi250033supp5_prod_1750956987.78281.pdf#page=7); REPORT [main p. 1, abstract](../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=1), [p. 3, Secondary End Points](../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3), [p. 6, Table 2 complication rows/footnote j and narrative](../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=6), [p. 7, complication narrative](../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=7); REPORT [results supplement p. 12, eTable 3](../../../joi250033supp4_prod_1750956987.77981.pdf#page=12), [p. 13, eTable 3 continuation](../../../joi250033supp4_prod_1750956987.77981.pdf#page=13).
- **Independent reproduction:** Both plans explicitly say complications will be compared between the groups; Table 2's standard-care, difference and P cells are blank for these rows, and eTable 3 contains only the embolization N=171 column, with 1 major and 3 minor complications.
- **Precision and comparison tier:** This is a categorical planned-analysis comparison, not a numeric discrepancy; the printed risks reconcile as 1/171=0.584795% and 3/171=1.754386%, and the abstract listing makes the endpoint key secondary rather than peripheral.
- **Inclusion rationale:** The planned key secondary analysis lacks a supplied comparative result, independently satisfying category 5.
- **Affected extraction:** Whether the minor/major complication endpoint has comparative inference, alongside intervention risks 0.6% and 1.8%.
- **Alternative and human question:** Procedure-specific safety may have intentionally been reported descriptively, or a planned comparison may have been performed but omitted; was the comparison performed or replaced, and what supplied result or documented analysis change accompanies it?
- **Limits:** A blank control cell supplies neither a zero count nor a test result; no preferred comparison is proposed.

### G2 — Strict versus inclusive primary recurrence boundary

- **Finding provenance:** F-XS-001; F-ST1-002.
- **Source-order key:** DOC-001-MAIN, PDF p. 3, End Points first criterion.
- **Qualifying route:** Route A, category 5.
- **Proposed domain:** protocol_report.
- **Compared roles:** PLAN SAP versus PLAN protocol and REPORT main article/results supplement.
- **Proposed primary relationship / All relationships:** P_R / P_R, P_P; the SAP conflicts both with the reported definition and independently with the protocol's definition.
- **Issue statement:** The SAP prints a primary-composite midline-shift criterion >5 mm, while the protocol and reports use ≥5 mm.
- **All affected locations:** PLAN [SAP p. 3, section 2.1 first bullet](../../../joi250033supp5_prod_1750956987.78281.pdf#page=3); PLAN [protocol p. 7, synopsis](../../../joi250033supp1_prod_1750956987.76581.pdf#page=7), [p. 16, section 4.1.1 primary endpoint](../../../joi250033supp1_prod_1750956987.76581.pdf#page=16), [p. 21, follow-up recurrence definitions](../../../joi250033supp1_prod_1750956987.76581.pdf#page=21), [p. 31, section 8.1](../../../joi250033supp1_prod_1750956987.76581.pdf#page=31); REPORT [main p. 3, End Points](../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3); REPORT [results supplement p. 11, eTable 2 criterion 1 and 1a](../../../joi250033supp4_prod_1750956987.77981.pdf#page=11), [p. 15, EMPROTECT primary endpoint](../../../joi250033supp4_prod_1750956987.77981.pdf#page=15).
- **Independent reproduction:** The SAP rendered page clearly prints >5 mm; the protocol prints ≥5 mm or its expanded inclusive wording, the main article says 5 mm or greater, and both results-supplement locations print ≥5 mm; the protocol p. 16 location is section 4.1.1, rather than the checker shorthand section 3.1.
- **Precision and comparison tier:** At exactly 5.0 mm, >5 is false and ≥5 is true; the comparison is a primary endpoint inclusion rule, so half-unit display arithmetic and peripheral-comparison exclusions do not apply.
- **Inclusion rationale:** The reproduced primary-composite definition difference satisfies category 5, even if the strict operator reflects a textual convention.
- **Affected extraction:** The endpoint definition underlying 24/162 versus 33/157 and adjusted OR 0.64 (0.36–1.14), including the shift branch with 11/24 and 17/33 cases.
- **Alternative and human question:** The inclusive rule may have governed all adjudications despite the SAP text; which boundary was implemented, and did any otherwise qualifying case lie exactly at 5 mm?
- **Limits:** Exact-boundary participant counts are unavailable; no change in observed counts or model estimates is inferred.

### G3 — Disclosed cause-restricted death amendment in primary composite

- **Finding provenance:** F-XS-002; F-ST1-001.
- **Source-order key:** DOC-001-MAIN, PDF p. 3, Statistical Analysis primary population paragraph.
- **Qualifying route:** Route A, category 5.
- **Proposed domain:** protocol_report.
- **Compared roles:** PLAN original protocol versus REPORT main article/results supplement; PLAN final SAP documents and corroborates the reported amendment.
- **Proposed primary relationship / All relationships:** P_R / P_R; the final SAP's disclosed version change corroborates the reported definition rather than creating an independent unresolved plan-internal conflict, and its distinct interim/final specifications are stage-specific.
- **Issue statement:** The original protocol treats deaths without recurrence as primary failures without a cause restriction, while the final report uses neurological/unknown-cause deaths and imputes other-cause deaths as nonevaluable outcomes under the documented final-SAP amendment.
- **All affected locations:** PLAN [protocol p. 48, interim primary analysis](../../../joi250033supp1_prod_1750956987.76581.pdf#page=48), [p. 49, final primary analysis](../../../joi250033supp1_prod_1750956987.76581.pdf#page=49); PLAN [SAP p. 5, interim analysis](../../../joi250033supp5_prod_1750956987.78281.pdf#page=5), [p. 6, final analysis](../../../joi250033supp5_prod_1750956987.78281.pdf#page=6), [p. 8, version-change table](../../../joi250033supp5_prod_1750956987.78281.pdf#page=8); REPORT [main p. 3, Statistical Analysis](../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3), [p. 4, Figure 1](../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=4), [p. 6, Table 2](../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=6); REPORT [results supplement p. 5, imputation methods](../../../joi250033supp4_prod_1750956987.77981.pdf#page=5), [p. 9, no-imputation footnote](../../../joi250033supp4_prod_1750956987.77981.pdf#page=9), [p. 11, recurrence/death criteria](../../../joi250033supp4_prod_1750956987.77981.pdf#page=11).
- **Independent reproduction:** The original final-analysis paragraph has no cause restriction; SAP p. 6 restricts treatment failures to neurological/undetermined deaths, and p. 8 expressly labels this a changed definition; the report matches that final rule, with 3/8 other-cause deaths nonevaluable and 2/1 neurological/undetermined deaths counted as recurrence.
- **Precision and comparison tier:** This is a primary-composite inclusion/missingness rule; numeric rounding cannot reconcile the different event definitions.
- **Inclusion rationale:** The reproduced planned-versus-reported composite-definition change satisfies category 5, and its explicit amendment history remains part of the evidence.
- **Affected extraction:** Primary endpoint definition and missingness handling accompanying 24/162 versus 33/157, adjusted OR 0.64 (0.36–1.14), P=.13.
- **Alternative and human question:** The SAP states that its final version was prepared before final database lock and gives version 2 date 2024/02/28 (document heading 20/03/2024), so this may be an intended prospectively documented amendment; how should that amendment be documented with the final result, and is an original-definition analysis supplied?
- **Limits:** No original-definition effect estimate is supplied; no counterfactual recurrence assignment, treatment effect, unauthorized change or concealment is inferred.

### G4 — Midline-shift samples exceed stated unilateral populations

- **Finding provenance:** F-NUM-001.
- **Source-order key:** DOC-001-MAIN, PDF p. 5, Table 1 Initial imaging results.
- **Qualifying route:** Route A, category 3; independently, Route B also applies because this is an unresolved within-display count/population constraint that changes the samples a reader would extract for the medians.
- **Proposed domain:** statistical_results.
- **Compared roles:** REPORT main article Table 1 count rows, sample labels and footnote.
- **Proposed primary relationship / All relationships:** S_W / S_W.
- **Issue statement:** Table 1 labels midline-shift data unilateral-only but prints n=161 in each arm, exceeding the same display's unilateral CSDH populations of 127 and 130.
- **All affected locations:** REPORT [main p. 5, Table 1 Unilateral CSDH row, Midline shift row and continuation footnote d](../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=5).
- **Independent reproduction:** The source rendering confirms the superscript d on the midline-shift row, the unilateral-only footnote, unilateral counts 127 (74.3%) and 130 (76.0%), and medians 10 (7–13) [n=161] and 10.5 (7–14) [n=161].
- **Display precision:** The sample interval [160.5,161.5] cannot fit within unilateral upper bounds 127.5 and 130.5; gaps 33 and 30 divided by the printed sample 161 are 0.204968944 and 0.186335404, each above 0.05.
- **Comparison tier and inclusion rationale:** This is a count constraint within one display, rather than a peripheral comparison of baseline copies across documents, and satisfies category 3.
- **Affected extraction:** Both participant sample sizes and the unilateral/full-arm population attributed to baseline midline-shift medians 10 and 10.5 mm.
- **Alternative and human question:** The samples may include bilateral participants despite the footnote, or the sample labels may refer to another unstated unit; which participants and sample sizes underlie each median?
- **Limits:** The table provides no repeated-scan or hemisphere-level sample definition; individual measurements are unavailable.

## Source reread and screening limits

All cited pages were reread: main 1, 3, 4, 5, 6, 7; protocol 7, 8, 16, 17, 18, 21, 31, 48, 49, 50; SAP 3, 4, 5, 6, 7, 8; results supplement 5, 9, 11, 12, 13, 15. For the missing complication comparison, the supplied full report text was additionally searched and the complete eTable 3 inspected; main p. 9 contains references, and no additional comparison was located.

Current-run, exact-source derivatives were reused as transcription aids: preprocessing/statistical1-main.txt, statistical1-sap.txt, statistical1-results.txt and protocol-mapper-statistical-native.txt, generated with the permitted pinned PyMuPDF 1.26.4 helper. The current-source numeric-checker-main-p5.png and cross-source-sap-page-003.png were visually reread. Source-matched retained main p. 6 and results p. 9 images were also inspected for blank cells and the sensitivity footnote. Direct supplied protocol pp. 7–8, 16–18, 21 and 31 were reread using the permitted helper's text capability streamed to /dev/stdout; no new derivative was retained. No new rendering, OCR, web access or arbitrary Python was used. Sources and reused assets were preserved.

The two screened-out findings were also reread at every cited location. F-XS-003 does not reproduce a formal outcome-status change: main pp. 1/3/6 retain secondary endpoints, and p. 4 explicitly ties exploratory interpretation to no multiplicity correction; the matching planned secondary lists and alpha statements do not conflict with that caution. F-XS-004 identifies a coherent zero-variance implementation at main p. 3, with the actual adjustment specified again in Table 2/eFigure 2; the stated variance evaluation does not establish an omitted planned primary comparison, and requiring an unreported refit detail would not independently qualify. These decisions distinguish findings outside category 5 from reproduced category-5 observations, which cannot be removed merely by contextual explanation.

Counts: nine findings; seven INCLUDE rows consolidated into four issues; two SCREENED_OUT rows, TERMINOLOGY_OR_WORDING=1 and CONTEXT_RESOLVES=1; all other screened-out reason counts=0. No assigned-source screening gap remains. Missing exact-boundary cases, individual measurements, model objects and an original-definition/comparative complication result limit quantification only; they do not add findings or prevent the source comparisons above.

Coordinator registration completed after this independent screen. G1→C001, G2→C002, G3→C003, G4→C004 in the stated source order. Every INCLUDE row above now contains its permanent stable ID; historical descriptions of the initial PENDING placeholder explain the handoff, rather than the final table state. No screening decision was changed during registration.
