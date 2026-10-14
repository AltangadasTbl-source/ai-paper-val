# Independent initial inclusion screen

Fresh screener runtime: `/root/initial_screener`; model `gpt-6.1-sol`; reasoning effort `high`. Scope: all nine findings in the current numeric, cross-source and statistical-pass-1 checker artifacts. The full scope, review contract and tooling record were read. Exact source-linked rendered pages were independently reread, with current maps and raw extraction used as locators. No historical scientific conclusions or external material were used. Sources and reused assets were preserved.

Each reproduced issue was screened against the comparison tiers, route A, route B and display-precision rule. Nine INCLUDE findings consolidate into five issues; several findings share one issue group and share one coordinator-assigned candidate ID. Stable candidate IDs were assigned by the coordinator after this independent screen; all remain Pending Human Adjudication. Detailed facts, groups and all retained locations are in [initial issue groups](initial_issue_groups.md).

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-ST1-003 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-004 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C002 |

F-NUM-001 — Route B qualifies because the SAP explicitly applies adherence progression thresholds to patients with a deviation while its adherence definition and final protocol use adherence, leaving complementary numerators that can reverse a planned decision classification.

F-XS-001 — Route A, category 5 qualifies because the final protocol retains a stratification-only primary-outcome analysis for which the supplied reports give no matched estimate, and their crude and fully adjusted contrasts do not reproduce that adjustment set.

F-XS-002 — Route B qualifies because main Table 2 and supplemental eTable 7 explicitly assign different censoring times to the same missing hospital-stay outcomes, beyond display precision, leaving the analysis definition attached to the hospital sHR unresolved.

F-XS-003 — Route B qualifies because final SAP §7 prescribes MICE for unavailable secondary outcomes whereas both reports explicitly use early censoring for missing stay outcomes, a reproduced analysis-specification difference retained within the broader missing-data issue.

F-XS-004 — Route B qualifies because the final protocol retains survival-stratified Wilcoxon stay comparisons while the final SAP and report specify Fine–Gray regression, without explicitly identifying whether the protocol comparison was replaced or retained.

F-ST1-001 — Route B qualifies for the independently reproduced hospital-stay censoring-time discrepancy and shares the same issue as F-XS-002.

F-ST1-002 — Route A, category 5 qualifies for the retained stratification-only primary-outcome analysis without a supplied result and shares the same issue as F-XS-001.

F-ST1-003 — Route B qualifies because final SAP §7 specifies all-outcome imputation predictors but eTable 7 specifies selected auxiliary outcomes or None and duration censoring, forming one missing-data specification issue with F-XS-003.

F-ST1-004 — Route B qualifies for the retained final-protocol Wilcoxon versus final-SAP/report Fine–Gray specification difference and shares the same issue as F-XS-004.

Counts: nine findings screened; nine INCLUDE rows; zero SCREENED_OUT rows; five distinct included issue groups. Screened-out reason-code counts are zero for NOT_REPRODUCED, ROUNDING_OR_DISPLAY_PRECISION, NOTATION_OR_TYPOGRAPHY, TERMINOLOGY_OR_WORDING, MODEL_VERSUS_CRUDE, CONTEXT_RESOLVES, CONDITIONAL_OR_UNREPORTED, PERIPHERAL_COMPARISON, OUT_OF_FOCUS and DUPLICATE_OF_INCLUDED. Parallel checker provenance is retained as INCLUDE rows sharing issue groups, rather than duplicate exclusions.

Limitations: supplied material does not include the executed analysis code, actual pilot progression statistic, or a separate stratification-only result. Absence claims are bounded to the two supplied REPORT documents and supported by their complete current evidence maps and raw text searches; OCR alone is not an absence test. No change in a reported effect estimate is inferred from the method discrepancies. The rechecker will assign evidence states after stable-ID registration.
