# Independent inclusion screen — initial

Scope: all 10 findings in checkers/numeric_consistency.md (F-NUM-001, F-NUM-002), checkers/cross_source_consistency.md (F-XS-001, F-XS-002, F-XS-003, F-XS-004, F-XS-005), and checkers/statistical_pass_1.md (F-ST1-001, F-ST1-002, F-ST1-003). QUALITY_CONTROL_SCOPE.md and the complete review contract were read. Decisions apply the comparison tiers first and then all four inclusion criteria; there is no expected finding count. No earlier-run scientific conclusions or external evidence were consulted.

Five distinct issues meet the threshold. Repeated checker descriptions are consolidated using DUPLICATE_OF_INCLUDED; no duplicate location is discarded. Candidate cells remain PENDING until the coordinator registers stable IDs and replaces each group’s representative and duplicate cells with its single C ID. These screening decisions do not assign dispositions; registered candidates remain Pending Human Adjudication.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-001 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-005 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C005 |
| F-ST1-001 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C003 |
| F-ST1-002 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C002 |
| F-ST1-003 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |

## One-sentence decisions

- F-NUM-001: The exact assignment counts conflict with the counts paired with treatment-specific primary eGFR means/SDs, while the figure captions do not define an alternative population or column ordering, leaving treatment-specific and subgroup N-to-summary extraction unclear.
- F-NUM-002: eTable 7 explicitly attributes both 944 and 991 to its complete-case ACR analysis through separate internally consistent constructions, leaving the population size of the displayed sensitivity effects unresolved.
- F-XS-001: This is the same forest count-to-summary pairing pattern as F-NUM-001, and its added eTable 11 corroboration is retained in that group.
- F-XS-002: The implemented plan defines primary inclusion through follow-up biosample return whereas the report specifies inclusion irrespective of follow-up, so the planned-versus-reported primary population definition cannot be extracted as equivalent without an unstated linkage.
- F-XS-003: The implemented primary equation omits the report’s routine age, sex and baseline-ACR adjustments and assigns additional baseline adjustments to a conditional sensitivity step, leaving the primary-model specification correspondence unresolved.
- F-XS-004: Continuous medication adherence of at least 80% and at least two-thirds use on four of six assessments are different membership rules for the reported primary-outcome robustness analysis, and no supplied amendment reconciles them.
- F-XS-005: This is the same 944-versus-991 complete-case ACR population construction as F-NUM-002, with all cited retention context retained.
- F-ST1-001: This repeats F-XS-002’s primary inclusion-rule comparison and provides no independent issue beyond that group.
- F-ST1-002: This repeats F-XS-003’s primary-covariate specification comparison, including the conditional sensitivity paragraph and its continuation.
- F-ST1-003: This repeats F-XS-004’s adherence membership-rule comparison across both interventions and both outcome sensitivity tables.

## Consolidated groups and retained source locations

The registration order below follows the earliest affected main-report location, including its within-page reading order, followed by affected support-source locations; corroborating locations do not determine the order. The coordinator assigns IDs. Each group retains its representative and every duplicate finding ID as provenance, even though the duplicate findings have no separate included issue.

### Group A — adherence sensitivity definition

Representative F-XS-004; merged provenance F-ST1-003. Proposed domain protocol_report; relationship P_R; focus D.

PLAN [original protocol p. 19, §VI.g](../../../joi190122supp1_prod.pdf#page=19) specifies at least 80% adherence; PLAN [addendum p. 33, §15g](../../../joi190122supp1_prod.pdf#page=33) specifies continuous adherence to at least 80%. REPORT [main p. 3, Covariates and Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3) defines highly adherent participants by at least two-thirds use; REPORT [main p. 4, primary robustness narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4) connects the restricted analyses to the primary result. REPORT [eTable 1 p. 6, footnote](../../../joi190122supp2_prod.pdf#page=6), [eTable 5 p. 10, definition and effect rows](../../../joi190122supp2_prod.pdf#page=10), and [eTable 8 p. 13, definition and effect rows](../../../joi190122supp2_prod.pdf#page=13) specify at least two-thirds on four of six questionnaires and the adherence populations of 1032 per intervention.

The two-thirds threshold is approximately 66.7%, distinct from 80%, and four qualifying assessments out of six do not require continuous qualification. This comparison qualifies through a prespecified primary-outcome sensitivity population and the reported primary robustness interpretation, rather than through a peripheral adherence percentage. The affected extracted results are eTable 5’s five-year eGFR differences 0.89 (95% CI −0.74 to 2.52), P=.28, and 0.42 (−1.22 to 2.06), P=.61; eTable 8 is an additional occurrence of the same definition. The actual reported rule is clear, but its correspondence to the supplied prospective restriction is not supplied; differing rules cannot be made equivalent through rounding or a group-name substitution. No alternative result, population size under the planned rule, or changed conclusion is inferred.

### Group B — primary adjustment specification

Representative F-XS-003; merged provenance F-ST1-002. Proposed domain protocol_report; relationship P_R; focus D.

PLAN [addendum p. 32, §15e Equation 2 and sensitivity paragraph](../../../joi190122supp1_prod.pdf#page=32) specifies treatment, categorical time, treatment-by-time and a participant random intercept; PLAN [p. 33, continuation](../../../joi190122supp1_prod.pdf#page=33) continues the covariate exploration description. Additional baseline characteristics are assigned to sensitivity analyses conditional on imbalance. REPORT [main p. 3, Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3) adds age, sex and their time interactions to the primary models and baseline ACR with its time interaction to eGFR models. REPORT [main p. 8, Table 2 footnote a and primary effect rows](../../../jama_de_boer_2019_oi_190122.pdf#page=8) confirms this primary adjustment. REPORT [eTable 4 p. 9](../../../joi190122supp2_prod.pdf#page=9) and [eTable 5 p. 10](../../../joi190122supp2_prod.pdf#page=10) corroborate the applied adjustment in sensitivity analyses.

The supplied equation and its separate conditional sensitivity provision do not identify the routinely adjusted reported model as the same planned primary specification. The affected results are the primary vitamin-D and omega-3 five-year eGFR differences 0.9 (−0.7 to 2.5), P=.25, and 0.9 (−0.7 to 2.6), P=.27, specifically their planned-versus-reported model classification. This is an explicit focus-D comparator, rather than critique of a stated coherent model or inference from an unreported numerical consequence. A later expanded model specification or an implemented sensitivity trigger could explain the difference, but neither linkage is supplied.

### Group C — primary population definition

Representative F-XS-002; merged provenance F-ST1-001. Proposed domain protocol_report; relationship P_R; focus D.

PLAN [addendum implementation cover p. 31](../../../joi190122supp1_prod.pdf#page=31) dates the implemented analytic amendment; PLAN [p. 32, §15c](../../../joi190122supp1_prod.pdf#page=32) defines intention-to-treat analyses by inclusion of all participants who return at least one follow-up biosample. REPORT [main p. 3, primary analysis paragraph](../../../jama_de_boer_2019_oi_190122.pdf#page=3) explicitly includes all participants irrespective of follow-up. REPORT [main p. 4, retention and primary results](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [p. 6, Figure 1](../../../jama_de_boer_2019_oi_190122.pdf#page=6), and [p. 8, Table 2](../../../jama_de_boer_2019_oi_190122.pdf#page=8) establish the reported primary results, primary population and follow-up context.

The primary boxes total 370+333+289+320=1312, whereas any follow-up blood boxes total 303+280+242+265=1090; reported any follow-up urine return is 1091. These marginal return counts do not establish the blood/urine union and do not demonstrate a particular planned population size. The included issue is the explicit operational-definition comparison, not an asserted 222-person change to an any-biosample population. Because §15c says this is what intent-to-treat means and sits within the implemented amendment, interpreting it merely as a minimum inclusion guarantee requires a new unstated interpretation. The affected extraction is the primary population/missing-data specification underlying both five-year eGFR differences of 0.9 and their intervals. No supplied later amendment connects the definitions; shared intent-to-treat wording does not do so.

### Group D — forest count-to-summary alignment

Representative F-NUM-001; merged provenance F-XS-001. Proposed domain statistical_results; primary relationship S_C; all relationships S_C, S_W; focus A.

REPORT [main p. 5, Table 1](../../../jama_de_boer_2019_oi_190122.pdf#page=5) and [p. 6, Figure 1](../../../jama_de_boer_2019_oi_190122.pdf#page=6) give four arms 370, 333, 289 and 320, establishing vitamin-D active/placebo 703/609 and omega-3 active/placebo 659/653. REPORT [main p. 8, Table 2 and Figure 3](../../../jama_de_boer_2019_oi_190122.pdf#page=8) and [p. 9, Figure 4](../../../jama_de_boer_2019_oi_190122.pdf#page=9) pair opposite overall count orders with means that match their printed treatment headings: Figure 3 Placebo 703, −13.1 (14.4), Vitamin D 609, −12.3 (14.8); Figure 4 Placebo 659, −13.1 (14.8), Omega-3 653, −12.2 (14.5). REPORT [eTable 6 p. 11](../../../joi190122supp2_prod.pdf#page=11) and [eTable 11 p. 16](../../../joi190122supp2_prod.pdf#page=16) corroborate overall means and assignment totals, respectively. REPORT [eFigure 2 p. 18](../../../joi190122supp2_prod.pdf#page=18) and [eFigure 3 p. 19](../../../joi190122supp2_prod.pdf#page=19) repeat the count ordering alongside geometric changes whose printed treatment headings match eTable 6.

Retain all rows in both vitamin-D displays: Overall 703/609; White 451/406; Black 148/130; ACR<30 635/559; ACR≥30 67/50; 25(OH)D<20 110/85, 20–<30 230/203, ≥30 332/297; eGFR≥60 612/531, <60 89/76; BMI<25 87/87, 25–<30 228/205, ≥30 364/294; omega-3 placebo 333/320, active 370/289. Retain all rows in both omega-3 displays: Overall 659/653; EPA/DHA≤2.2 332/347, >2.2 308/292; ACR<30 596/598, ≥30 62/55; hsCRP≤0.2 334/335, >0.2 323/316; fish<1.5 servings/week 354/329, ≥1.5 295/310; vitamin-D placebo 289/320, active 370/333. Pair order is the literal displayed placebo/active N order. Equal counts in one row do not independently establish a discrepancy, and exact unavailable subgroup populations are not invented.

Known Table 1 strata reproduce the conflict independently: active/placebo vitamin-D White totals are 240+211=451 and 199+207=406; corresponding <20-ng/mL totals are 62+48=110 and 41+44=85, each printed under opposite N headings. These exact integers cannot reconcile through display precision. Whole-heading exchange would put the overall means in conflict with Table 2/eTable 6, whereas keeping the printed headings pairs assignment counts with opposite summaries. A repeated count-column alignment is a plausible explanation, but the supplied captions do not explicitly establish which subgroup counts and SDs belong together. The issue qualifies through primary eGFR analysis-size extraction and its attached mean/SD values, with ACR occurrences retained as the same pattern; it is not registered as an isolated peripheral heading difference or a crude-versus-model recomputation. No change to the adjusted overall treatment effects or P values is established.

### Group E — complete-case ACR population accounting

Representative F-NUM-002; merged provenance F-XS-005. Proposed domain statistical_results; relationship S_W; focus A.

REPORT [eTable 7 p. 12, title, baseline/year 5 counts and asterisk footnote](../../../joi190122supp2_prod.pdf#page=12) prints N=944 and partitions 504+440=944 and 477+467=944, while the same directly referenced footnote says 991 were included and 320 baseline contributors excluded, satisfying 1311−320=991. REPORT [main p. 4, urine retention](../../../jama_de_boer_2019_oi_190122.pdf#page=4) and [eTable 6 p. 11, year 5 counts](../../../joi190122supp2_prod.pdf#page=11) corroborate final urine availability of 945 and do not themselves create another relationship.

The two explicit analysis-size constructions differ by 47 participants, with no rounding explanation for exact integers. The title and repeated arm partitions favor an analysis total of 944, but the footnote explicitly assigns its distinct 991/320 accounting to this analysis rather than merely reporting a separate return pool. The immediate table does not explain additional exclusions or distinguish returned specimens from usable measurements sufficiently to reconcile that claim. This is an analysis-population-size issue under the comparison-tier exception, even though the ACR complete-case analysis is a sensitivity result. The affected extraction is the N and inclusion/exclusion accounting attached to five-year ACR ratios 1.03 (0.86 to 1.22), P=.77, and 0.93 (0.78 to 1.11), P=.44; no different treatment-effect conclusion is inferred.

## Source confirmation and limitations

The screener reread the supplied PDFs directly using available CPU Poppler pdftotext -layout: main physical pp. 3–6 and 8–9; plan physical pp. 19 and 31–33; results supplement physical pp. 6, 9–13 and 16–19. Text for the raster forest panels was supplemented by visual inspection of current direct-source Poppler renders preprocessing/numeric-main-p8.png, preprocessing/numeric-main-p9.png, preprocessing/numeric-supp2-p12.png, preprocessing/numeric-supp2-p18.png and preprocessing/numeric-supp2-p19.png. The original supplied PDF remains the authority; native text and current renders were used to reread its exact locations, not as independent comparators. No new persistent derivative was needed, no source or reusable artifact was changed, and no source-confirmation gap remains for the assigned findings.

Limits on claims: the blood/urine follow-up union, a later amendment, exact planned continuous-80% adherence membership, unrounded model outputs, and raw analysis data are not supplied. None is invented. The included issues name the actual reported result or extracted definition they affect and do not infer how alternative analyses would change estimates.

Counts: 10 findings screened; 5 representative INCLUDE decisions consolidated into 5 distinct issues; 5 SCREENED_OUT decisions, all DUPLICATE_OF_INCLUDED; every other screened-out reason code has count 0. Review-domain group counts: protocol_report 3, statistical_results 2, report_internal_inconsistency 0, plan_material 0.

Coordinator registration completed: Group A C001; Group B C002; Group C C003; Group D C004; Group E C005. Every representative and duplicate table cell now points to its permanent candidate. The earlier PENDING description records the handoff state only.
