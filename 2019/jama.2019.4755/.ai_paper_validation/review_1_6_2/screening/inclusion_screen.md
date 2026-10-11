# Independent inclusion screening

Initial screening by fresh agent `root/initial_screen`, run model `gpt-6.1-sol`, reasoning effort `high`. Complete normative scope and the inclusion-screen contract were read. Assigned checker scope: numeric consistency (no findings), cross-source consistency (F-XS-001), and statistical pass 1 (F-ST1-001, F-ST1-002). Decisions below follow independent rereading of exact supplied PDF locations; checker transcriptions are locators rather than final authority. No earlier review conclusions or external sources were used. There is no target finding count.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-ST1-001 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |
| F-ST1-002 | statistics_pass_1 | initial | SCREENED_OUT | CONTEXT_RESOLVES | — |

## One-sentence justifications

- **F-XS-001:** Route A, category 5 qualifies because the supplied protocol expressly assigns specificity, ROC AUC and, in §7.2, both assays' sensitivity to the primary outcome set, whereas other protocol clauses, the SAP and the report assign these outcomes secondary status, with AUC explicitly unreported and no supplied outcome-hierarchy amendment reconciling the status conflict.
- **F-ST1-001:** This reproduces the same primary-outcome hierarchy pattern as F-XS-001, so it is consolidated into that included issue with every additional location and its statistical-checker provenance retained below.
- **F-ST1-002:** Permission to collect postponed specimens does not establish their eligibility for the original day-specific primary analysis, whose immediate §7.2 context explains the restriction, and the SAP expressly replaces that primary population with intention-to-screen, so the retained operational wording does not leave the reported sensitivity population or a printed extraction value unresolved.

## Consolidated included issue: primary-outcome hierarchy

**Finding provenance:** F-XS-001 (cross-source checker) and F-ST1-001 (statistical pass 1); one included issue. The duplicate finding remains fully traceable and is not a separate issue.

**Roles and all compared source locations:**

- PLAN [protocol PDF p.11, §3.4](../../../joi190039supp1_prod.pdf#page=11): FOBGold sensitivity is primary; specificity and ROC AUC are secondary.
- PLAN [protocol PDF p.22, §6.1](../../../joi190039supp1_prod.pdf#page=22): the narrow primary and secondary lists repeat.
- PLAN [protocol PDF p.13, §3.9](../../../joi190039supp1_prod.pdf#page=13), continuing on [p.14](../../../joi190039supp1_prod.pdf#page=14): the parenthetical primary endpoint includes FOBGold sensitivity, specificity and ROC AUC on original day 3.
- PLAN [protocol PDF p.28, §§7.1–7.2](../../../joi190039supp1_prod.pdf#page=28): §7.1 identifies primary FOBGold sensitivity and assigns confirmatory status to primary endpoints; §7.2 identifies sensitivity, specificity and ROC AUC of two immunochemical FOBTs as primary.
- PLAN [SAP PDF p.6, §3.2](../../../joi190039supp2_prod.pdf#page=6): FOBGold sensitivity is primary; qualitative-test sensitivity, quantitative AUC and both tests' specificities are secondary.
- PLAN [SAP PDF p.8, §§5.4–5.5](../../../joi190039supp2_prod.pdf#page=8): the primary-sensitivity and secondary-performance analysis descriptions maintain the narrow hierarchy.
- PLAN [SAP PDF p.9, §7](../../../joi190039supp2_prod.pdf#page=9): the disclosed changes address the primary analysis set and missing values, without an explicit outcome-hierarchy change.
- REPORT [main PDF p.1, Main Outcome and Measures](../../../jama_brenner_2019_oi_190039.pdf#page=1): quantitative sensitivity at two cutoffs is the primary outcome.
- REPORT [main PDF p.3, Outcomes and Statistical Analyses](../../../jama_brenner_2019_oi_190039.pdf#page=3): quantitative sensitivity is primary; specificity and qualitative sensitivity are secondary; ROC AUC is secondary and explicitly unreported; secondary analyses are exploratory.
- REPORT [main PDF p.4, Primary and Secondary End Points](../../../jama_brenner_2019_oi_190039.pdf#page=4): quantitative-specificity differences −6.4 (95% CI −9.6 to −3.2), P<.001 and −3.1 (−5.4 to −0.8), P=.008, and qualitative-sensitivity difference 12.7 (0.1 to 24.7), P=.048 appear as secondary results.

**Independent reproduced comparison:** The broad protocol clauses explicitly use primary-endpoint language for outcomes designated secondary elsewhere. This is an outcome-status conflict, not a comparison of numerically mismatched estimates, an assay synonym, or the disclosed day renumbering. The report follows the narrow list but does not reconcile the broad list. Route A category 5 requires inclusion of this reproduced status pattern regardless of which governing-list interpretation a human reviewer ultimately adopts. Numeric recomputation intervals and relative discrepancy are not applicable to this categorical comparison.

**Affected named results:** Prespecified primary/confirmatory versus secondary/exploratory interpretation of the quantitative-specificity results P<.001 and P=.008 and qualitative-sensitivity result P=.048, and completeness of reporting ROC AUC if the broader primary clauses governed; the reported numeric estimates themselves are not alleged to conflict.

**Proposed classification for coordinator registration:** `protocol_report`; primary relationship `P_R`; all relationships `P_R, P_P`; compared roles PLAN versus REPORT and PLAN versus PLAN. The direct report-versus-broad-protocol status comparison establishes P_R, and conflicting protocol clauses/SAP establish P_P. No report-internal or report-supplement discrepancy is part of this issue.

**Source-grounded alternatives and human question:** Detailed endpoint sections and the SAP may establish the governing narrow list while the broader clauses retain another specification; alternatively the broad clauses may reflect an earlier primary set. The supplied evidence does not identify a hierarchy amendment or governing-clause precedence. Which prespecified hierarchy governed specificity, qualitative sensitivity and ROC AUC, and what supplied statement reconciles the explicit broad-primary descriptions with secondary/exploratory and unreported status?

## Independent assessment of F-ST1-002

All three finding locations were reread from newly extracted source text and visually confirmed: PLAN [protocol PDF p.18, §5](../../../joi190039supp1_prod.pdf#page=18), [p.21, Table 1 footnote 4](../../../joi190039supp1_prod.pdf#page=21), and [p.28, §7.2](../../../joi190039supp1_prod.pdf#page=28). The first two permit delayed collection and the third contains the study-exclusion wording in the sentence defining day-3 primary comparisons. The wording exists, but collection permission does not itself assert primary-analysis inclusion. The same protocol also plans other-day and combined-day analyses and defines safety analyses for randomized participants independently of sample availability (§7.1). Thus general collection and the original strict primary time window are distinguishable from the immediate statistical context.

The governing later PLAN [SAP PDF p.4, §2.1 and day-renumbering footnote](../../../joi190039supp2_prod.pdf#page=4) distinguishes exact-day per-protocol observations from valid pre-colonoscopy intention-to-screen observations; [p.9, §7](../../../joi190039supp2_prod.pdf#page=9) explicitly changes the primary analysis to intention-to-screen. REPORT [main PDF p.3, Outcomes](../../../jama_brenner_2019_oi_190039.pdf#page=3) follows the scheduled-day intention-to-screen population and separately reports exact-day per-protocol analyses. No supplied participant-level count establishes an affected primary denominator, and the original restriction is not the rule that the reported primary analysis relies on.

This observation does not reproduce an outcome-status/composite change, an allegedly prespecified absent analysis, or a missing primary/key-secondary result, so route A category 5 does not apply. Route B fails because the intended original primary window and the subsequently amended reported primary population can be identified from the immediate/source-disclosed context; construing the older operational phrase as an unresolved rule for the reported numeric result would require disregarding that distinction and change. The residual wording alone supplies no alternative printed sensitivity or denominator for extraction. The single screening reason is CONTEXT_RESOLVES; this assessment neither assigns an adjudication nor changes any source.

## Completion, counts and derivative provenance

Three findings screened: one INCLUDE row and one distinct included issue; two SCREENED_OUT rows, comprising one DUPLICATE_OF_INCLUDED and one CONTEXT_RESOLVES. Numeric checker has zero findings and therefore contributes zero screening rows. Its four excluded observations, the cross-source checker's nine and statistical pass 1's ten remain in their checker artifacts for the independent pass-2 and quality audit stages. No finding was omitted. No source-inspection limitation.

Direct confirmation used Poppler `pdftotext`/`pdftoppm` 26.01.0 on CPU, without OCR or Python extraction. All derivatives are new, uniquely owned outputs under `preprocessing/`; supplied sources and reused assets were unchanged.

- Layout commands: `pdftotext -layout -f N -l N SOURCE .ai_paper_validation/review_1_6_2/preprocessing/screen-initial-TAG-pN.txt`; protocol pages 11, 13, 14, 18, 21, 22, 28; SAP pages 4, 6, 8, 9; main pages 1, 3, 4. TAG is `protocol`, `SAP` or `main`; SOURCE is the exact linked PDF for that role.
- Visual commands: `pdftoppm -f N -l N -singlefile -scale-to 1800 -png SOURCE .ai_paper_validation/review_1_6_2/preprocessing/screen-initial-TAG-pN`; protocol pages 13, 18, 21, 28; SAP pages 6, 9; main page 3. Every resulting PNG was viewed directly.

The coordinator assigned C001 to the included hierarchy issue and its duplicate after screening. No severity, disposition, evidence state or final correction is assigned by this screening stage.
