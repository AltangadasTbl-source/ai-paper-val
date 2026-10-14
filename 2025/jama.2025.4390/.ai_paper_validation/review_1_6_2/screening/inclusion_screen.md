# Independent initial inclusion screen

Fresh inclusion_screener/high runtime 01a12bcf-3c84-72a3-8667-fcaaa0aecdfa; model gpt-6.1-sol. Scope: all 20 findings in the current numeric_consistency.md (3), cross_source_consistency.md (9), and statistical_pass_1.md (8). QUALITY_CONTROL_SCOPE.md and the complete review contract were read. Decisions below follow independent exact-source rereading, with source-matched derivatives as locators. No old scientific conclusions, external evidence, candidate-count expectation, or adjudication was used.

Candidate registration is complete. The coordinator assigned C001-C013 to the source-ordered issue groups and inserted the stable IDs in included and duplicate rows. The independent decisions remain unchanged. No stable C ID was assigned by this screener.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-NUM-003 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-XS-001 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-007 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-008 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-XS-009 | cross_source_consistency_reviewer | initial | SCREENED_OUT | TERMINOLOGY_OR_WORDING | — |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C012 |
| F-ST1-003 | statistics_pass_1 | initial | SCREENED_OUT | CONTEXT_RESOLVES | — |
| F-ST1-004 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C008 |
| F-ST1-005 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-ST1-006 | statistics_pass_1 | initial | SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | — |
| F-ST1-007 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-ST1-008 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |

## One-sentence independent justifications

- F-NUM-001: Route B qualifies because Figure 3's explicitly labeled primary rate 71.0 in both arms conflicts far beyond display precision with matched Table 2 rates 2.30/2.44, and its caption leaves the quantity needed for primary/subgroup rate extraction undefined.
- F-NUM-002: Route A, category 3 qualifies because eTable 5 ethnicity counts sum to 85/111 against denominators 44/57, and its missing-data footnote supplies no overlapping-category permission or definition of Other that reconciles the displayed distribution.
- F-NUM-003: Route A, category 3 qualifies because the printed ARB PM fraction 1/37 gives 2.7027%, disjoint from printed 7.7% by relative gap .64251, and the table's multiple-reason permission does not alter that individual fraction.
- F-XS-001: This repeats F-NUM-001's primary/subgroup Figure 3 column issue; its Key Points p.2 location is retained in I001.
- F-XS-002: Route A, category 5 qualifies because six Figure 3 medication treatment-effect subgroup axes are covered by the prespecified caption but absent from the supplied SAP's 13-axis list and corresponding protocol/amendment specifications.
- F-XS-003: Route A, category 5 qualifies because the source explicitly changes overall health from secondary to exploratory and new glaucoma from the original safety list to the later secondary list, with disclosed blinded evolution and tolerability/safety terminology retained for human interpretation.
- F-XS-004: Route B qualifies because the reported acute/unplanned-only exclusions narrow the SAP's unqualified all-cause utilization endpoint, changing the event membership represented by 993/1047 and HR .93 rather than merely its wording.
- F-XS-005: Route B qualifies because SAP's inclusion of assisted-living admission and the report's added loss-of-medication-timing-control criterion imply different eligible events for the 38/26-event LTC result, without a supplied definition establishing equivalence.
- F-XS-006: Route B qualifies because supplied no-block/no-stratification allocation and reported blocks of 10/12 stratified by province are distinct statistical-design specifications underlying the province-adjusted primary result, and no supplied amendment explicitly connects them.
- F-XS-007: Route B qualifies because the six-week versus six-month assessment and all-bedtime-users versus diuretic-monotherapy comparison feed a planned enrollment decision, so they affect a decision rule rather than peripheral process counts.
- F-XS-008: Route B qualifies because study-start versus previous-follow-up vision references define different observations for the reported 420/411-event safety outcome, and the final SAP's agreement with the report does not document how the earlier reference was replaced.
- F-XS-009: The report expressly distinguishes information collected since the beginning from outcomes prespecified for analysis, and the original named safety/tolerability collection list does not itself specify their inferential analyses, so this wording difference is resolved without changing the supplied final tests.
- F-ST1-001: Route A, category 4 qualifies because the source counts yield Pearson P=.017964632 while the printed .09 interval [.085,.095] remains disjoint by relative gap .74484, and the same method reproduces other categorical rows of eTable 4.
- F-ST1-002: Route A, category 4 qualifies because both displayed 9/44 versus 16/57 medication comparisons give Pearson P=.379220624, reproducing combination .38 and other binary rows while remaining disjoint from diuretic .34 by relative gap .10065.
- F-ST1-003: The main paragraph concerns outcome availability and the supplement immediately specifies covariate replacement versus no outcome imputation, providing a coherent outcome-only reading of the shortened main statement without competing reported fitted results or populations.
- F-ST1-004: This repeats F-XS-002's six medication-class prespecification pattern, with all six estimates and interaction locations retained in I008.
- F-ST1-005: Route A, category 5 qualifies because neither pooled interview-retention eTable 4 nor cross-arm unavailable-follow-up eTable 5 supplies the SAP's arm-specific censored-versus-not-censored comparison for the primary survival analysis.
- F-ST1-006: The SAP separately defines withdrawal and loss to follow-up, and the report prints a censoring rule for participants lost to all follow-up plus a distinct loss definition rather than a contrary date for the 95 withdrawals, leaving only an unreported exception and no reproduced alternative withdrawal rule.
- F-ST1-007: This repeats F-XS-006's allocation specification discrepancy; main p.7 province-adjustment context is retained in I004.
- F-ST1-008: This repeats F-NUM-001's Figure 3 quantity/scale pattern, with every subgroup location retained in I001.

## Coverage and source authority

All cited locations were reread: main physical pp.1,2,3,4,6,7,8,9; original protocol physical pp.3–4 and complete supplied amendment log pp.8–18; SAP physical pp.2,3,4,6; results supplement physical pp.15,16,20,21,33,34,35,36,37,38,39,40,45,46,48. Main/results native/layout text was freshly generated against current sources; key numeric cells, report methods, amendment rationale, original protocol pp.3–4, and SAP pp.2,3,4,6 were additionally read visually. Current renders are in preprocessing/main_fresh, preprocessing/results_b_fresh, preprocessing/stats1_confirmation, and preprocessing/cross_confirmation; SAP renders in review_1_5_1/preprocessing/support_protocol_sap are source-matched reusable assets, with no old conclusions read. No new extraction/OCR was required; no derivative was modified.

Continuous printed values/P copies use half-unit intervals; exact integer participant counts retain their discrete values. The chronotype recomputation was independently calculated from the six source counts; a conservative continuous ±.5 input envelope [.0152689,.0210417] reported by the checker also remains disjoint, but is unnecessary once count discreteness is honored. The identical medication comparison was independently recomputed. Other same-display categorical rows were reread to establish the reproducing-method basis, including age X²=30.217601/P=.00000442, medication-number categorical tests, and matching eTable 5 binary comparisons. No unstated original test engine is asserted.

Summary: 20 findings; 13 INCLUDE rows representing 13 distinct issues; 7 SCREENED_OUT rows: DUPLICATE_OF_INCLUDED 4, TERMINOLOGY_OR_WORDING 1, CONTEXT_RESOLVES 1, CONDITIONAL_OR_UNREPORTED 1. Every finding has exactly one decision. No scientific screening gap remains. Limits are unprinted original test engines/subsets, no exact participant censoring dates, and unavailable later protocol/nocturia publications; these do not authorize assumptions or external lookup. All included issues remain Pending Human Adjudication.
