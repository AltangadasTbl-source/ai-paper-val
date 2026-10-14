# Complete screening-decision handoff

Mechanical extraction of the canonical initial screening table and all independent decision justifications, plus bounded repair and registration record. Every consolidated source-fact group is preserved in full in candidate_ledger.md; this handoff omits only that duplicate group text to keep later statistical/audit context bounded. Canonical complete screening/inclusion_screen.md remains unchanged and authoritative.

# Independent inclusion screen — initial stage

Fresh inclusion screener `/root/inclusion_initial`, gpt-6.1-sol/high. Read QUALITY_CONTROL_SCOPE.md completely and the complete inclusion-screen section and classification constraints of the 1.6.2 review contract. Independently screened all 21 findings in the three current-run canonical checker artifacts: three numeric, seven cross-source and eleven statistical pass-1 findings. Every cited PDF page was reread visually from a source-matched render; checker transcriptions served as locators. No earlier-run conclusions, external material or participant data were used. Included issues are ready for coordinator registration; no stable candidate IDs or human dispositions are assigned here.

There are 13 included issue groups, six duplicate findings and two other screened-out findings. Coordinator has assigned stable C IDs to all included and duplicate rows; G labels below retain the original consolidation locators. Group numbering does not determine candidate order.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-101 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-NUM-102 | numeric_consistency_reviewer | initial | SCREENED_OUT | NOT_REPRODUCED | — |
| F-NUM-201 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-XS-006 | cross_source_consistency_reviewer | initial | SCREENED_OUT | CONTEXT_RESOLVES | — |
| F-XS-007 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-ST1-003 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-ST1-004 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C002 |
| F-ST1-005 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |
| F-ST1-006 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C005 |
| F-ST1-007 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-ST1-008 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C006 |
| F-ST1-009 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C007 |
| F-ST1-010 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-011 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C012 |

## Independent decision justifications

- F-NUM-101: Route A, category 3 qualifies the three visibly printed portal count/denominator/percentage combinations because their conservative relative gaps are .154653, .059815 and .151175, and the prospective recruitment context does not reconcile within-display arithmetic (G01).
- F-NUM-102: The source confirms the listed Reading percentages sum to 91%, but prints neither an exhaustive-total assertion nor a complete race-category partition, so a conflict with a purported printed 100% total is not reproduced and an unlisted category remains possible.
- F-NUM-201: Route A, category 3 qualifies both 5 (5%) version rows against the explicitly named AI primary-analysis population of 183, with relative gap .297260, consolidated as one repeated pattern (G02).
- F-XS-001: Route A, category 5 qualifies the primary-composite addition of an HbA1c ≥6.5% disqualifier, explicitly identified as a change in the supplied SAP summary (G03).
- F-XS-002: Route A, category 5 qualifies replacement of exclusion of withdrawal/missing twelve-month data by inclusion of all randomized participants with failure assignment (G04).
- F-XS-003: Route A, category 5 qualifies replacement of the planned clustered mixed-effects logistic primary model by unadjusted binomial RD regression, even with the supplied rationale (G05).
- F-XS-004: Route A, category 5 qualifies replacement of the planned primary PA multiple-imputation rule and its 100%-valid-PA complete-case sensitivity by zero assignment and different supportive analyses (G06).
- F-XS-005: Route A, category 5 qualifies replacement of the program-completer supportive primary analysis by the complete-twelve-month-data/no-prohibited-medication population (G07).
- F-XS-006: The plan specifies covariate adjustment in logistic/linear models, whereas the report explicitly implements binomial RD analyses and calls the five implemented sensitivities post hoc; the changed implementation resolves why the full executed analysis can bear that label even though the general conditional covariate-selection idea was prospective, and no distinct printed estimate or prespecified-outcome status conflict remains beyond G05.
- F-XS-007: Route A, category 5 qualifies the printed primary PA window comparison of months 6–11 with all available postbaseline wear periods; the supplied dated amendment acknowledges a timeframe modification without supplying its exact replacement wording (G08).
- F-ST1-001: Route B qualifies the same-row pooled proportions 32.2%/31.9% versus RD −1.1 pp because the supplied pooling description does not map those opposite-direction quantities to distinct final estimands/models, and the precision intervals remain disjoint (G09).
- F-ST1-002: Route B qualifies the direct discrepancy between claimed interpolated preprocessing and the printed calculation pipeline, which computes ac_imp but sends ac to both subsequent summary loops, leaving the stream underlying the PA-dependent primary outcome unclear (G10).
- F-ST1-003: Route B qualifies the report's valid/available-period denominator alongside zero assignment to missing periods because the joining rule changes the primary 150-min/week calculation and is not specified by those statements (G11).
- F-ST1-004: This is the same PA-window issue as included F-XS-007 (G08); all amendment and report locations are retained in that group.
- F-ST1-005: This is the same additional diabetes-range disqualifier as included F-XS-001 (G03); report p30 is retained with the other locations.
- F-ST1-006: This is the same primary-model replacement as included F-XS-003 (G05).
- F-ST1-007: This is the same primary-population/failure-assignment replacement as included F-XS-002 (G04).
- F-ST1-008: This is the same original-versus-reported primary PA missing-data replacement as included F-XS-004 (G06).
- F-ST1-009: This is the same supportive primary-analysis population replacement as included F-XS-005 (G07).
- F-ST1-010: Route A, category 5 qualifies the separately amended HbA1c branch restriction to baseline 5.7–6.4%, explicitly disclosed in version 1.4 and reflected in the report's 130/130 component denominators (G12).
- F-ST1-011: Route B qualifies the categorical P-value/result mapping because the displayed 108/260 subgroup counts and named general categorical methods yield values outside the printed .024/.018 intervals, with the site significance reading also changing; no confidence interval is printed, so the checker-proposed Route A category 1 is not assumed (G13).

## Bounded confirmation and stable registration

The original 38-image screening scope exceeded the 32-image context bound and is preserved in parts/initial_full_scope.md. Before registration, fresh report/numeric and protocol confirmation agents repeated every decision over disjoint seven-finding/17-page and fourteen-finding/30-page scopes. Both independently confirmed the decisions and source facts; complete durable records are [bounded report screen](parts/bounded_reports.md) and [bounded protocol screen](parts/bounded_protocol.md). No scientific location was omitted to meet the bound. The canonical table retains exactly one initial decision per finding.

Source-order registration mapping: G03=C001; G08=C002; G12=C003; G04=C004; G05=C005; G06=C006; G07=C007; G01=C008; G10=C009; G11=C010; G02=C011; G13=C012; G09=C013. Every candidate remains Pending Human Adjudication.
