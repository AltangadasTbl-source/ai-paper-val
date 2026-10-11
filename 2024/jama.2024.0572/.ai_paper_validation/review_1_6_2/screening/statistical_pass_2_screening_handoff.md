# Complete initial screening decisions for statistical pass 2

Mechanical lossless selection of the complete 32-row decision table, every one-sentence justification, and both screened-out source-confirmation rationales from screening/inclusion_screen.md. The omitted duplicated G001–G018 issue-group bodies are retained in full in candidate_ledger.md and the source recheck. This handoff changes no scientific decision.

# Independent initial inclusion screen

Fresh runtime: root/inclusion_initial; gpt-6.1-sol/high; initial independent screening. Complete QUALITY_CONTROL_SCOPE.md and Workflow 1.6.2 review contract read. Scope: all 31 findings in the current canonical numeric (4), cross-source (11), and statistical-pass-1 (16) checker artifacts. No earlier scientific conclusions, external sources, or candidate-count expectation used. Sources and reused derivatives preserved. Decisions rest on independently reread exact source pages, direct native PDF extraction, and direct source-page renderings, rather than checker transcriptions alone.

All 31 findings have exactly one initial decision: 29 INCLUDE findings consolidated into 18 distinct issue groups, and 2 SCREENED_OUT findings (PERIPHERAL_COMPARISON: 1; CONDITIONAL_OR_UNREPORTED: 1). Repeated qualifying findings remain INCLUDE and will share their group's stable ID, preserving their provenance and union of locations. The coordinator assigned C001–C018 to these consolidated groups in source order. Every eventual candidate remains Pending Human Adjudication.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-NUM-101 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C017 |
| F-NUM-201 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C018 |
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C015 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-XS-101 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-XS-102 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-XS-103 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C017 |
| F-XS-104 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C018 |
| F-XS-105 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-ST1-101 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-ST1-201 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C017 |
| F-ST1-301 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-ST1-302 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-ST1-303 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-ST1-304 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-305 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C016 |
| F-ST1-306 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-ST1-401 | statistics_pass_1 | initial | SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | — |
| F-ST1-501 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-ST1-502 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-ST1-503 | statistics_pass_1 | initial | SCREENED_OUT | PERIPHERAL_COMPARISON | — |
| F-ST1-504 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-ST1-505 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C014 |
| F-ST1-506 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C012 |
| F-ST2-601 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C019 |

## One-sentence decision justifications

- F-NUM-001: Route B qualifies because the same REPORT labels 8/336 and 204/336 as follow-up MRI populations, leaving the analysis-population size for the infarct-growth result unresolved well beyond display precision.
- F-NUM-002: Route B qualifies because Figure 2B's ≥100-mL EVT primary mRS distribution gives approximately 38% ambulation and 62% mRS≥4, whereas the matched discussion describes approximately 20% and 80%.
- F-NUM-101: Route A, category 2 qualifies because eFigure 13 labels the below-one side of an explicitly adverse-outcome EVT/MM risk contrast as favoring MM, reversing the printed estimates' treatment direction.
- F-NUM-201: Route A, category 3 qualifies because the same MM discordant-profile-2 populations in eTables 9 and 10 have mutually exclusive mRS0–3 and mRS5–6 event proportions exceeding 100% beyond precision.
- F-XS-001: Route A, category 5 qualifies because the same planned 90-day functional-independence endpoint has primary and secondary status, and imaging/stay endpoints change secondary-to-tertiary status within supplied PLAN material.
- F-XS-002: Route A, category 5 qualifies because the specific SAP calls composite core primary and prespecified while the REPORT calls its matched analyses post hoc sensitivities.
- F-XS-003: Route A, category 5 qualifies because the specific all-as-treated plan is replaced for primary imaging-stratified treatment comparisons by randomized-group reporting.
- F-XS-004: Route B qualifies because supplied plans define the reported sICH endpoint using 4-hour versus 24-hour ascertainment and differing death inclusion, leaving the definition attached to its reported event counts unclear.
- F-XS-005: Route B qualifies because the explicitly planned age/time prognostic analysis and supplied fitted surfaces use different time endpoints without an identified replacement specification; independent ambulation is not established as key secondary, so absent-key-secondary Route A status is not assumed.
- F-XS-006: Route A, category 2 qualifies because the literal positive alternative P(MM score≤EVT score)=.5+.0791 points toward lower MM disability while the printed decision is labeled EVT efficacy.
- F-XS-101: Route B qualifies because the matched ≥100-mL primary mRS distribution does not yield the supplementary independence/ambulation event percentages in either treatment arm after segment-wise rounding allowances.
- F-XS-102: Route A, category 2 qualifies because the narrative says EVT independence/ambulation probability increases with mismatch volume while both explicitly cited EVT curves decrease.
- F-XS-103: Route A, category 2 qualifies for the same eFigure 13 treatment-direction pattern as F-NUM-101.
- F-XS-104: Route A, category 2 qualifies because matched discordant-profile-2 favorable events move between explicitly labeled treatment arms, with unchanged arm denominators and a supporting distribution showing the opposing attribution.
- F-XS-105: Route B qualifies because CTP/MRI and composite core are distinct numerical covariates but competing captions and narrative do not identify which produced the 70/100/150-mL independent-ambulation surfaces.
- F-ST1-001: Route A, category 1 qualifies because two printed 95% intervals ending at ratio null 1.00 accompany significant-association statements, and hidden endpoint precision does not remove this category.
- F-ST1-101: Route B qualifies because finite RR1.00 and CI0.37–2.72 accompany all-zero within-subgroup outcomes despite a stated ordinary within-subgroup modified-Poisson analysis that needs an additional estimation step to produce a finite fit.
- F-ST1-201: Route A, category 2 qualifies for the same eFigure 13 direction pattern as F-NUM-101 and F-XS-103.
- F-ST1-301: Route A, category 2 qualifies for the same continuous mismatch-volume EVT narrative-versus-curve reversal as F-XS-102.
- F-ST1-302: Route B qualifies for the same competing core-covariate labels as F-XS-105.
- F-ST1-303: Route A, category 5 qualifies for the same replaced primary treatment-group specification as F-XS-003.
- F-ST1-304: Route A, category 5 qualifies for the same composite-core primary/prespecified-versus-post-hoc-sensitivity pattern as F-XS-002.
- F-ST1-305: Route A, category 5 qualifies because the SAP explicitly plans mismatch-volume 50/100-mL analyses of the primary 90-day mRS distribution, whereas the complete supplied REPORT counterpart scope contains only different joint profiles and continuous mismatch analyses.
- F-ST1-306: Route B qualifies for the same planned-versus-reported time-predictor definition as F-XS-005 without claiming that ambulation is key secondary.
- F-ST1-401: The source reproduces RR1.29(0.93–1.79) and RD0.168(0.011–0.325), but different adjusted scales and confidence constructions can yield different null-inclusion readings, and no supplied common estimand/interval identity or same-effect P/test establishes a contradiction rather than a missing mapping.
- F-ST1-501: Route A, category 1 qualifies because both historical SELECT 95% OR intervals print a lower endpoint of 1.00 while their P values .041/.049 are significant, and this always-register category is retained despite historical PLAN context.
- F-ST1-502: Route A, category 5 qualifies for the same protocol outcome-hierarchy pattern as F-XS-001.
- F-ST1-503: The source reproduces 21.2% versus 51.2% scenario-4 fixed-design simulation power, but this plan-internal operating-characteristic output is peripheral and does not change any printed sample-size/power input, primary decision boundary, reported primary/key result, or analysis-population size.
- F-ST1-504: Route A, category 2 qualifies for the same explicit planned probability-direction reversal as F-XS-006.
- F-ST1-505: Route B qualifies because the PLAN simultaneously retains a 200/380 inferential schedule with no additional analysis and reports a boundary-based rejection after 300 outcomes, leaving the operative stopping decision rule unidentified.
- F-ST1-506: Route A, category 1 qualifies because the historical safety statement includes sICH with P=.072 while describing the listed outcomes as significantly increased at the default .05 threshold.

## Screened-out source confirmations

F-ST1-401: independently reread REPORT results pp.43–44 and main p.4. The MM ratio interval[.93,1.79] contains1 and difference interval[.011,.325] excludes0 for all endpoint half-unit allowances; this numerical observation is reproduced. However, the cell labels two distinct adjusted measures, supplies no common risk-pair identity or confidence construction, and prints no same-effect P/statistic (the .83 is heterogeneity). Different confidence intervals on nonlinear scales or conditional/marginal estimands need not give the same null inclusion. Treating that difference alone as a contradictory same-analysis result assumes an unstated mapping; asking only for that mapping is missing-method detail, rather than a reproduced logical contradiction. No routeA1 interval-versus-own-test or routeA4 same-display reproducing method is established. The issue is therefore CONDITIONAL_OR_UNREPORTED, not rounding, despite robust endpoint separation.

F-ST1-503: independently reread PLAN protocolp49 and directly rendered trialSAPp11. Fixed power21.2%vs51.2% has intervals[21.15,21.25]vs[51.15,51.25], gap29.90percentage points and relative29.90/21.2=1.410377. Matching scenario4 effects(.4,.4,.4,.4,−.1,−.1),weighted.1,adaptiveN502/power78.5%,fixedN560 are confirmed. This is simulated operating-characteristic output under an alternative scenario, not an input used to select the primary sample size or an implemented boundary. The maximum560,planned alpha/power inputs,all displayed decision boundaries and observed result remain unchanged. Apply scope comparison tiers first: peripheral plan-internal output comparison. No printed production mechanism establishes a routeA2 digit slip, no interval/test conflict, no counts, and no source-defined reproducing simulation method that reconstructs other rows establishes routeA4. PERIPHERAL_COMPARISON is the sole reason code.



## Complete pass-2 screening update

F-ST2-601 qualifies by Route B: protocol p.48 permits selected-subgroup rescue after final overall efficacy failure, while trial SAP p.10 states terminal non-superiority and p.9 retains final-selection language. Differing versions and unexecuted-final-stage limits are explicit alternatives. It is distinct from C014's executed interim300 review. All exact source facts and locations are preserved in C019 and its recheck; no observed final statistic or result change is inferred.

Cumulative total:32 findings,30 INCLUDE findings consolidated into19 stable candidates,2 SCREENED_OUT findings (one CONDITIONAL_OR_UNREPORTED and one PERIPHERAL_COMPARISON). This mechanically selected handoff preserves all decisions/justifications; complete source details remain in canonical screening and pass-2 working artifact.
