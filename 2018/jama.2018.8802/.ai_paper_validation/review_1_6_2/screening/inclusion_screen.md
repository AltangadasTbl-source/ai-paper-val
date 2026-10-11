# Independent inclusion screen — Workflow 1.6.2

Runtime agent: /root/screen. Model: gpt-6.1-sol. Reasoning effort: high. Stage: initial; fresh independent specialist. QUALITY_CONTROL_SCOPE.md and the complete review contract were read. Scope: all ten findings in numeric_consistency.md, cross_source_consistency.md and statistical_pass_1.md. The numeric-tail artifact was also read completely: it contains zero additional finding IDs and eight excluded observations. No earlier scientific conclusions or external evidence were used.

Each finding was independently reproduced from supplied-source page content using fresh direct `pdftotext -layout` reads to stdout (Poppler 25.03.0, CPU): main PDF pp.1,3,4,5,6,7,8; plan PDF pp.16,17,18,19; report supplement PDF p.2. The reusable main p.5 and p.8 full-page images were visually inspected to confirm figure labels, table alignment and signs; these images were transcription aids, with direct-source text confirming the same readings. No new extraction derivative, OCR or rendering was required, and no source/reused asset was changed.

Ten qualifying finding records consolidate to **four distinct included issues**. Multiple INCLUDE rows are intentionally retained under the contract's shared-candidate provision; the coordinator must assign one common C ID to all findings in each merged group below. PENDING denotes an unassigned ID, not a separate issue. No threshold exclusion is necessary among these ten findings; screened-out counts are zero for every reason code. Checker exclusions are not converted to findings by this initial screening stage and remain available for the mandatory pass-2 and audit reviews.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-ST1-003 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-004 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-ST2-001 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C005 |

## One-sentence independent justifications

- **F-NUM-001:** Route B qualifies because the figure and Results explicitly attach discrepant counts to the primary analysis, the display-precision gap exceeds .05, and extracting 3980 instead of 4800 changes the named analysis-population size even though the smaller numbers can also be identified as follow-up completers.
- **F-NUM-002:** Route A, category 1 qualifies because Table 3 pairs an in-hospital death 95% absolute-difference CI that contains zero with P=.009 under the stated two-sided P<.05 rule.
- **F-XS-001:** Route B qualifies because the primary-analysis population is an eligible comparison tier and the report's conflicting primary-analysis labels leave a 3980-versus-4800 extraction discrepancy after display precision, consolidating with F-NUM-001.
- **F-XS-002:** Route B qualifies because the same named key secondary vascular-event results and disability results are explicitly assigned to follow-up after discharge and after symptom onset, leaving the time horizon attached to their extracted estimates unresolved.
- **F-XS-003:** Route A, category 5 qualifies because the plan's total-over-total composite definition and the main report's explicit average of patient-specific proportions specify different primary-outcome weighting, with the report supplement affirming that its total-over-total definition applies to the randomized phase.
- **F-XS-004:** Route A, category 1 qualifies because the direct Table 3 reread confirms the same null-crossing interval/P conflict as F-NUM-002, while the separate HR/P and mortality narrative are retained as alternative inferential context.
- **F-ST1-001:** Route A, category 1 qualifies because −1.1 to +0.2 contains the difference null while its adjacent P=.009 is below .05, consolidating with F-NUM-002 without requiring the checker's diagnostic normal approximation.
- **F-ST1-002:** Route A, category 5 qualifies because the direct plan, main-report and supplement definitions reproduce the composite-weighting discrepancy, consolidating with F-XS-003 without claiming an unavailable trial-level recomputation.
- **F-ST1-003:** Route B qualifies because the report attributes its Table 3 clinical results to two distinct time origins without describing separate analysis windows, consolidating with F-XS-002 and affecting extraction of the key secondary vascular effects.
- **F-ST1-004:** Route B qualifies because the figure's explicit primary-analysis counts conflict beyond display precision with the 4800 primary-analysis statement and 2400-per-arm co-primary denominators, consolidating with F-NUM-001.

## Merged issue: primary composite definition and weighting

**Finding provenance:** F-XS-003 and F-ST1-002; also the numeric-tail source-confirmed N140 overlap, which has no separate finding ID. Register exactly one issue for these records.

**Exact locations and roles:** PLAN [protocol p.16, lines216–220](../../../joi180070supp1_prod.pdf#page=16); REPORT [results supplement p.2, eAppendix](../../../joi180070supp2_prod.pdf#page=2); REPORT [main p.3, Outcomes composite-definition paragraph](../../../jama_wang_2018_oi_180070.pdf#page=3); REPORT [main p.7, Table 2 composite row](../../../jama_wang_2018_oi_180070.pdf#page=7). PLAN [pp.18–19, opportunity analysis](../../../joi180070supp1_prod.pdf#page=18) and REPORT [main p.4, Data Analysis opportunity example](../../../jama_wang_2018_oi_180070.pdf#page=4) distinguish the inferential units rather than supply another discrepancy.

**Source-grounded reproduction:** The plan and supplement define total interventions performed among eligible patients divided by total possible interventions among eligible patients; the supplement explicitly says the endpoint definition is the same as in the randomized phase. The main report defines eligible measures performed divided by eligible measures for a given patient and explicitly calculates that proportion for each patient before averaging. For fulfilled opportunities r_i and eligible opportunities k_i, the first definition is Σr_i/Σk_i, while the second is Σ(r_i/k_i)/n. The first weights patient proportions by k_i; the second weights patients equally. The sources describe patient-dependent eligibility. The formulas can coincide for particular data, but are not identical definitions. Display-precision numeric intervals are inapplicable to this formula comparison; no trial-level numerical discrepancy is claimed.

**Affected values:** Main Table 2 composite means 88.2 (SD15.1)% and 84.8 (SD18.2)%, adjusted difference 3.5 (95%CI0.7–6.4) percentage points, P=.02; the abstract/main narrative give the corresponding 3.54 (0.68–6.40) contrast. The primary composite's weighting and its relation to the baseline power input are the human questions. This is a primary-outcome definition comparison, not a peripheral baseline-copy comparison or a crude estimate compared with a model estimate.

**Qualifying route:** Route A, category 5, changed planned-versus-reported composite definition. Immediate context supplies two explicit definitions and does not equate them. A possibility that aggregate language was intended loosely, or that descriptive patient means intentionally differ from the opportunity-level inferential estimand, remains an alternative interpretation rather than grounds for exclusion.

**Proposed classification:** Review domain protocol_report; relationship type P_R; all relationships P_R, S_C. PLAN protocol versus REPORT main supplies P_R; REPORT supplement versus REPORT main supplies S_C. Opportunity-analysis passages corroborate/distinguish estimands and do not add P_P or S_W conflicts. Classification ambiguity: the plan's aggregate wording might have intended a within-patient calculation, but no explanatory equivalence or amendment is supplied. Patient-specific eligibility and exact adjusted-difference construction are absent.

**Human question:** Which weighting generated the planned and reported composite outcome, reported means and adjusted difference, and how does the same-endpoint statement in the eAppendix reconcile those definitions?

## Merged issue: primary-analysis population counts

**Finding provenance:** F-NUM-001, F-XS-001 and F-ST1-004. Register exactly one issue for these records.

**Exact locations and roles:** All REPORT: [main p.4, Results opening and final baseline paragraph](../../../jama_wang_2018_oi_180070.pdf#page=4); [main p.5, Figure 1 enrollment/follow-up/bottom primary-analysis boxes](../../../jama_wang_2018_oi_180070.pdf#page=5); [main p.7, Table 2 all-or-none row](../../../jama_wang_2018_oi_180070.pdf#page=7); [main p.1, abstract enrollment and twelve-month completion](../../../jama_wang_2018_oi_180070.pdf#page=1).

**Source-grounded reproduction:** Results explicitly states 4800 patients were enrolled and included in the primary analysis. Figure 1 enrolls and treats 2400 per arm, shows 397/423 lost at twelve months and labels 2003/1977 as included in primary analysis. Its smaller counts equal 2400−397=2003 and 2400−423=1977; Results identifies the same counts as twelve-month completers and the abstract reports 3980 completed follow-up. The co-primary all-or-none result uses 1290/2400 and 1147/2400. Thus the mismatch concerns printed primary-analysis attribution and its population size, not whether follow-up losses add correctly.

**Display precision:** Figure-count sum 2003+1977=3980 has conservative half-unit interval [3979,3981]; narrative total4800 has [4799.5,4800.5]. Gap818.5/4800=.1705208>.05. Per-arm gaps are [2399.5,2400.5] versus [2002.5,2003.5], giving396/2400=.165, and versus [1976.5,1977.5], giving422/2400=.1758333. All exceed .05.

**Qualifying route:** Route B: B1 primary-analysis counts are focus A and the comparison tier explicitly permits an analysis-population-size change; B2 identifying the smaller numbers as follow-up completers does not reconcile their explicit primary-analysis designation with the same designation for4800; B3 an extractor can take3980 or4800 as the named primary-analysis population. Figure ordering suggests a follow-up-set interpretation, but it does not state a separately named analysis or resolve which primary outcome the bottom count applies to.

**Proposed classification:** Review domain statistical_results; relationship type S_W; all relationships S_W. The issue concerns printed counts/denominators, for which the scope directs statistical_results. Classification ambiguity: numeric/statistical checkers proposed report_internal_inconsistency for the population attribution, while the cross-source checker proposed statistical_results; either attribution emphasis is source-grounded, but this screen uses the explicit counts-domain rule. All compared documents are the same REPORT. No actual exclusion from computational analysis is inferred.

**Human question:** Which analysis population do the2003/1977 bottom figure boxes describe, and how do those labels reconcile with4800 primary-analysis patients and2400-per-arm co-primary denominators?

## Merged issue: clinical follow-up origin

**Finding provenance:** F-XS-002 and F-ST1-003; also numeric-tail N141 overlap without a separate finding ID. Register exactly one issue for these records.

**Exact locations and roles:** REPORT [main p.5, Clinical Events opening and vascular/disability results](../../../jama_wang_2018_oi_180070.pdf#page=5); REPORT [main p.3, secondary-outcome definition](../../../jama_wang_2018_oi_180070.pdf#page=3); REPORT [main p.4, time-to-event specification](../../../jama_wang_2018_oi_180070.pdf#page=4); REPORT [main p.8, Table 3 disability footnote and Figure 2 axes/caption](../../../jama_wang_2018_oi_180070.pdf#page=8). REPORT [main p.6, length-of-stay row](../../../jama_wang_2018_oi_180070.pdf#page=6) provides supporting context. PLAN [p.16, lines223–230](../../../joi180070supp1_prod.pdf#page=16) and PLAN [p.19, lines280–282](../../../joi180070supp1_prod.pdf#page=19) corroborate onset only.

**Source-grounded reproduction:** Clinical Events expressly attributes Table 3 long-term mortality, vascular-event and disability outcomes at3,6,12 months to time after discharge. The outcome definition and time-to-event methods specify initial symptom onset; Table 3's disability footnote specifies after stroke onset; Figure 2 specifies days after stroke symptom onset in both axes and caption. Protocol outcome and Cox specifications also use symptom onset. The two origins are distinct; the reported median hospital stays13 and12 days are supporting context, not a conversion of patient-specific onset-to-discharge durations.

**Affected values:** Key secondary vascular-event results in the abstract/main text, including differences−2.03,−2.18,−3.13 percentage points at3,6,12 months, and Table 3 disability and mortality follow-up results. No rates are recomputed, and no numerical discrepancy percentage or rounding interval applies to the time-origin comparison.

**Qualifying route:** Route B: B1 this attributes named primary/key-secondary-tier results to a time point and is within estimate/analysis interpretation; B2 the sentence directly assigns the same Table 3 outcomes to discharge while methods and footnote/figure assign onset without identifying separate windows; B3 a data extractor needs to know the time horizon attached to the vascular/disability estimates. Postdischarge contact could be informal wording, but no stated visit/analysis distinction connects it to the onset-based windows; this is result attribution rather than an immediately interchangeable outcome name or symbol.

**Proposed classification:** Review domain report_internal_inconsistency; relationship type S_W; all relationships S_W. Classification ambiguity: possible informal discharge wording or distinct clinical/survival windows is recorded for human review. Plan merely corroborates one report side and does not make the candidate P_R. No planned-versus-reported timing change is separately asserted.

**Human question:** Which time origin governs each Table 3 clinical result and the corresponding disability/survival analyses, and does the discharge-based Results wording denote a distinct follow-up window?

## Merged issue: in-hospital death interval/P pairing

**Finding provenance:** F-NUM-002, F-XS-004 and F-ST1-001. Register exactly one issue for these records; do not add a second issue for the same interval's midpoint or narrative analysis choice.

**Exact locations and roles:** REPORT [main p.8, Table 3 Death/In hospital row and separate P columns](../../../jama_wang_2018_oi_180070.pdf#page=8); REPORT [main p.4, Data Analysis confidence/significance rule](../../../jama_wang_2018_oi_180070.pdf#page=4); REPORT [main p.5, total-mortality narrative](../../../jama_wang_2018_oi_180070.pdf#page=5).

**Source-grounded reproduction:** Table 3 prints11/2400(0.5%) and23/2400(1.0%), adjusted absolute difference−0.7 percentage points,95%CI−1.1 to+0.2, and adjacent P=.009. The separate HR column prints0.96(0.90–1.02), P=.14. Methods give95%CIs, P<.05 and two-sided tests. Zero belongs to [−1.1,+0.2] while .009<.05. The direct-source column alignment and positive upper endpoint were confirmed visually and by fresh layout text.

**Qualifying route:** Route A, category 1. The display-precision rule cannot exclude interval/test conflicts; even illustrative half-unit bounds leave lower endpoint[−1.15,−1.05], upper endpoint[.15,.25] and P[.0085,.0095], retaining the opposite null-exclusion readings. No normal-approximation assumption is needed. The point itself lies inside the interval and the endpoints are ordered.

**Affected values and alternatives:** Extraction and significance reading of the adjusted in-hospital mortality absolute-difference CI/P pair. The separate nonsignificant HR/P may explain the narrative's no-significant-mortality statement; it does not reconcile the difference pair. Distinct inferential procedures for CI and P remain a source-grounded possibility, with their specific constructions unreported. The route A requirement applies even if such a different-analysis interpretation is later confirmed.

**Proposed classification:** Review domain statistical_results; relationship type S_W; all relationships S_W. Classification ambiguity: none concerning document roles or relationship; the inferential construction remains the human question. The narrative is contextual rather than an independent mismatch warranting another candidate.

**Human question:** Which analyses and inferential procedures produced the in-hospital death absolute-difference CI and P=.009, and how should a reader reconcile their different null-exclusion readings?

## Completion and bounded limitations

Finding records screened:10. INCLUDE rows:10. Distinct included issues:4. SCREENED_OUT rows:0. Screened-out counts: NOT_REPRODUCED0; ROUNDING_OR_DISPLAY_PRECISION0; NOTATION_OR_TYPOGRAPHY0; TERMINOLOGY_OR_WORDING0; MODEL_VERSUS_CRUDE0; CONTEXT_RESOLVES0; CONDITIONAL_OR_UNREPORTED0; PERIPHERAL_COMPARISON0; OUT_OF_FOCUS0; DUPLICATE_OF_INCLUDED0. Consolidation is implemented by the four shared groups, not by discarding qualifying provenance.

Every cited finding location was reread. No supplied source-location gap remains in this screening scope. Individual care opportunities, outcome dates and CI/test construction details are absent, limiting trial-level recalculation but not reproduction of the printed conflicts. Reusable image-engine versions are unrecorded; fresh direct Poppler reads confirmed the inputs independently. Proposed classifications remain subject to the separate mechanical recheck and audit. No C IDs, evidence states, audit judgments or human dispositions are assigned here.

Coordinator registration: composite group C001; population group C002; time-origin group C003; mortality group C004. The screening table now carries these stable IDs; the original PENDING descriptions above document the screen-before-registration handoff.

## Pass-2 screening and append-only registration

F-ST2-001 independently qualifies by Route A, category 1: the three-month vascular-death adjusted difference/CI/P does not reconcile under the normal-Wald relationship supported by all eleven other difference rows, after full printed-input allowances. The independently evaluated attainable P interval is [0.001576789,0.001913909] versus printed [0.0005,0.0015], giving a minimum relative gap0.076789>.05. Exact symmetric centering preserves the discrepancy and support from every other row. Actual CI/test construction is unreported and remains a human question; no significance reversal is claimed. Detailed source reread and calculations are in screening/inclusion_screen_pass_2.md. Registered C005 without renumbering C001–C004. Final screening totals:11 findings,11 INCLUDE rows,5 distinct candidates,0 SCREENED_OUT rows; all screened-out reason-code counts remain0.
