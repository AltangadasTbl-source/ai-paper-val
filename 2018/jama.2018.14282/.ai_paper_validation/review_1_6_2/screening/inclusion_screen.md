# Independent inclusion screen — initial

Runtime ID: 01a129ca-c991-7a90-b0ad-3686288f164b. Scope: every finding in the current numeric, cross-source and statistical-pass-1 checker artifacts; 32 findings screened independently against exact supplied source locations. QUALITY_CONTROL_SCOPE.md was read completely, together with the review-contract inclusion-screen section. Direct Poppler 25.03.0 source layout reads and a preserved source-matched Figure 3 image were used on CPU; no web or earlier scientific conclusions were used. Source and reused assets were preserved. Candidate cells contain stable coordinator-assigned IDs following completed independent screening.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C014 |
| F-NUM-003 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C015 |
| F-NUM-004 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C012 |
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-002 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C012 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-005 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C005 |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-XS-007 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-XS-008 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-XS-009 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-010 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-XS-011 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-012 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-013 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C002 |
| F-XS-014 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C016 |
| F-ST1-001 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C012 |
| F-ST1-002 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C005 |
| F-ST1-003 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C005 |
| F-ST1-004 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C006 |
| F-ST1-005 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C009 |
| F-ST1-006 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C010 |
| F-ST1-007 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C002 |
| F-ST1-008 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C011 |
| F-ST1-009 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |
| F-ST1-010 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C007 |
| F-ST1-011 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-ST1-012 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-ST1-013 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C003 |
| F-ST1-014 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C016 |

## One-sentence justifications

- F-NUM-001: Route A, category 3 applies because four Table 1 count/percentage pairs fail the printed 388-person denominators after half-unit precision, with relative interval gaps 0.0751–0.1184.
- F-NUM-002: Route A, category 3 applies because the paragraph explicitly attaches 153 (19.7%) and 31 (4%) to separate 388-person treatment arms although only the pooled 776-person denominator reproduces those percentages.
- F-NUM-003: Route B applies because Figure 3 contains smaller PaO2:FIO2 and hematologic-malignancy subgroup populations and event totals without a stated restriction, while the article positively states no exclusion for missing/incomplete data, leaving the primary-mortality and IMV subgroup analysis populations unresolved above display precision.
- F-NUM-004: Route A, category 2 applies to the overall IMV HR direction/reference reading of 0.85 in Table 2 versus 1.17 with unchanged favors headings in Figure 3, and the consolidated issue retains every affected Figure 3 row from F-XS-002 and F-ST1-001.
- F-XS-001: Route B applies because the abstract assigns the key-secondary oxygenation result to days after intubation while the matching 150/119 result is explicitly six hours after randomization, changing the population and time origin a reader would extract.
- F-XS-002: This is the same Figure 3 contrast/favors-heading pattern included as F-NUM-004, with both panels and all 26 rows retained in that group.
- F-XS-003: Route B applies because the main article's Gray cumulative-incidence comparison and the supplement's explicit log-rank label are attached to the same key-secondary IMV display and P=.17 without distinguishing separate analyses.
- F-XS-004: Route A, category 5 applies to the consolidated final-plan primary-analysis pattern because the promised primary relative-risk, confounder-adjusted and per-protocol analyses have no identified supplied results alongside the univariable Cox/ITT report.
- F-XS-005: The adjusted and per-protocol primary-analysis locations are consolidated with the omitted/replaced primary-analysis pattern included as F-XS-004, retaining both requirements and all source locations.
- F-XS-006: Route A, category 5 applies because the final plan's adjusted competing-risk analyses for key-secondary IMV and infection are replaced or unidentified in the reported univariable IMV and infection-proportion procedures.
- F-XS-007: Route A, category 5 applies because the final plan positively requires joint longitudinal analyses of abstract-reported oxygenation, comfort and dyspnea, but the supplied results do not identify them.
- F-XS-008: Route A, category 5 applies because the final plan's overall and survivor/decedent ICU-stay survival analyses are not identified alongside the reported pooled Wilcoxon comparison.
- F-XS-009: Route A, category 5 applies because Borg dyspnea and lowest-SpO2 oxygenation remain named final-plan components of key-secondary outcomes but have no supplied outcome results.
- F-XS-010: Route A, category 5 applies because the initially prespecified secondary intubated-mortality analysis receives post hoc status in the report, with the disclosed redesign and its removal from the final endpoint list retained as an alternative explanation.
- F-XS-011: Route B applies because the final plan's categorical control-group HFNO prohibition differs from the report's explicit DNI rescue allowance used in 30 controls, changing the primary-mortality and IMV comparator strategy.
- F-XS-012: Route B applies to the consolidated stratum-definition pattern because equality at 9 L/min changes plan/report oxygen-flow membership and day 2 changes methods/figure ICU-time membership, affecting primary-mortality and IMV subgroup populations and interactions.
- F-XS-013: The ICU-time regrouping is retained within the stratum-definition pattern included as F-XS-012, together with its independent S_W relationship and every source location.
- F-XS-014: Route A, category 5 applies because Figure 3 calls the unknown-diagnosis and hematologic-malignancy analyses predefined while none of the supplied prospective subgroup specifications contains those named treatment interactions.
- F-ST1-001: This repeats the direction/reference issue included as F-NUM-004, and its main-p.4 treatment-contrast statement and all 26 forest rows are retained.
- F-ST1-002: This repeats the relative-risk and adjusted-primary components of the final-plan primary-analysis pattern included as F-XS-004.
- F-ST1-003: This repeats the retained final-plan per-protocol primary-analysis component consolidated under F-XS-004.
- F-ST1-004: This repeats the final-plan IMV/infection competing-risk and adjustment pattern included as F-XS-006.
- F-ST1-005: This repeats the absent/unidentified final-plan joint-model results included as F-XS-007.
- F-ST1-006: This repeats the final-plan ICU-stay estimator and population analyses included as F-XS-008.
- F-ST1-007: Both its time and oxygen-flow locations are retained in the stratum-definition pattern included as F-XS-012.
- F-ST1-008: This repeats the intubated-mortality outcome-status change included as F-XS-010, including the early summary pages and disclosed final redesign.
- F-ST1-009: This repeats the abstract-versus-randomization oxygenation attribution included as F-XS-001.
- F-ST1-010: This repeats the Gray-versus-log-rank attribution issue included as F-XS-003.
- F-ST1-011: Route A, category 4 applies because the log-event-count interval construction reproduces the other two Table 2 HR intervals but not the printed infection interval 0.96–1.06, with precision-adjusted relative endpoint gaps 0.3109 and 0.4611.
- F-ST1-012: The absent Borg component is retained in the final-plan measurement-component pattern included as F-XS-009.
- F-ST1-013: This repeats the final-plan control-HFNO prohibition versus reported rescue allowance included as F-XS-011.
- F-ST1-014: This repeats the predefined diagnosis/malignancy interaction pattern included as F-XS-014, retaining all supplied prospective specification locations.

## Counts and limits

32 finding rows; 16 INCLUDE rows corresponding to 16 consolidated included issues; 16 SCREENED_OUT rows, all DUPLICATE_OF_INCLUDED; 0 screened-out rows for each other reason code. There is no numerical target. All included and duplicate locations/provenance are preserved in inclusion_screen_notes.md. Unavailable raw event times, model variances, unreported subgroup-covariate completeness and plan-amendment mapping are named alternative/reproduction limits, not missing assigned screening coverage. Candidate IDs and all later-stage fields are left to the coordinator and required specialists.
