# Statistical consistency pass 1

- Runtime agent: root/statistics_one; canonical task /root/statistics_one.
- Role: qc16_statistical_consistency_reviewer; model gpt-6.1-sol; effort high; start mode FRESH_SPAWN.
- Scope: complete inferential union, main article REPORT pp. 1–10, protocol/SAP PLAN pp. 1–25, results supplement REPORT pp. 1–9.
- Completion: 104 stable S relationships; each PASS_1_COMPLETE; scientific coverage gaps 0.
- Emitted observations: 3 distinct candidates for coordinator registration; no C IDs assigned here.
- Every observation remains Pending Human Adjudication.
- Inputs: [statistical inventory](../statistics/relationship_inventory.md), [main map](../extraction/main_quantitative_evidence.md), [support map](../extraction/support_quantitative_evidence.md).
- Tools: direct Poppler pdftotext 25.03.0; direct source confirmation main pp. 4–5, 7–8, PLAN pp. 17–19, results supplement pp. 5–9. Reusable maps/images were locators. Text was read in memory. No source or reused derivative changed; no Python, installation, web, GPU, or old audit inputs.

S044 consolidates M-S044/SUP-S040 and S045 consolidates M-S045/SUP-S041: genuine repeated sensitivity results. All other provisional groups remain, with an added plotted-quantity label relationship S104. Thus 105 provisional groups minus two repetitions plus one added relationship yields 104 stable records.

The inventory gives exact inputs, source links, roles, direct checks and missing definitions. Source two-sided tests, 95% CIs, broad models and adjustment lists do not establish identical interval/P construction. Exact variance, working covariance, degrees of freedom, CI algorithm and P test are not inferred from convention. No numeric SE or test statistic is printed.

## STAT-A — In-hospital death interval and P give different inferential signals

**Relationships:** S035/M-S035; separate HR S036 supplies context.

**Proposed category and relationship type:** Statistical reporting inconsistency; S_W; all relationships S_W.

**Compared locations and roles:** REPORT Table 3 in-hospital adjusted absolute-difference interval and its paired P, both [main article p. 8](../../../jama_wang_2018_oi_180070.pdf#page=8). REPORT [main article p. 4](../../../jama_wang_2018_oi_180070.pdf#page=4) supplies 95% CIs, two-sided tests, P<.05 and patient/hospital adjustment. PLAN [p. 18](../../../joi180070supp1_prod.pdf#page=18) corroborates broad GEE/mean-difference definitions; it is not a conflicting comparator.

**Printed values:** Intervention 11/2400 (0.5%), control 23/2400 (1.0%); adjusted difference −0.7 percentage points, 95% CI −1.1 to +0.2, P=.009. Separate HR 0.96 (0.90–1.02), P=.14.

**Direct observation:** The interval crosses zero while its adjacent P=.009 is below .05. The estimate is contained and endpoints ordered. The positive endpoint +0.2 was confirmed from the supplied PDF.

**Reproducible rule and applicability:** A 95% interval obtained by inverting the same two-sided test cannot contain zero when that test gives P<.05. Shared construction is not established here. This is a printed inferential-signal discrepancy requiring clarification, not a proven same-Wald incompatibility.

**Diagnostic arithmetic only:** Midpoint (−1.1+0.2)/2=−0.45 differs from estimate −0.7 by 0.25 percentage points. With one-decimal rounding, the estimate lies in [−0.75,−0.65] and midpoint in [−0.50,−0.40], without overlap. This would not reconcile as a symmetric original-scale interval centered on the estimate. Symmetry and Wald construction are not source-defined. No diagnostic P or replacement endpoint is prescribed.

**Missing definitions:** AD model/link and marginal estimand, CI algorithm, P test, variance estimator, degrees of freedom, and whether CI/P use the same fitted contrast and inferential construction.

**Source-grounded alternatives:** An asymmetric or non-inverted interval with a different test could give different signals. A CI endpoint or P could have a transcription discrepancy. The separate HR cannot supply the AD P. Supplied evidence does not select an explanation.

**Human question:** What analysis generated the in-hospital adjusted difference, CI and P=.009, and are these printed values correct for the same contrast?

**Candidate boundary:** CI versus P. STAT-B compares prose versus P and is separate.

**Bounded downstream relevance:** An extractor could copy inconsistent uncertainty/significance metadata if confirmed. No conclusion change is established.

## STAT-B — Mortality prose says no significant difference despite AD P=.009

**Relationships:** S035/S036 and the matched narrative.

**Proposed category and relationship type:** Statistical reporting inconsistency; S_W; all relationships S_W.

**Compared locations and roles:** REPORT Clinical Events [main article p. 5](../../../jama_wang_2018_oi_180070.pdf#page=5) versus REPORT Table 3 in-hospital AD P at [main article p. 8](../../../jama_wang_2018_oi_180070.pdf#page=8). REPORT [main article p. 4](../../../jama_wang_2018_oi_180070.pdf#page=4) gives P<.05.

**Printed values:** “There was no significant difference in total mortality rates in the hospital and at 3, 6, and 12 months (Figure 2B).” In-hospital AD P=.009; separate HR P=.14. Figure 2B at [main article p. 8](../../../jama_wang_2018_oi_180070.pdf#page=8) shows 12-month death HR 0.86 (0.68–1.09), P=.21.

**Direct comparison and rule:** The blanket sentence includes in-hospital mortality as nonsignificant, while .009<.05 under the printed threshold. This prose/P comparison does not require a reconstructed CI, SE or test statistic.

**Calculation:** .009<.05; .14>.05; .21>.05. Other death AD Ps .08, .38, .05 and HR Ps .23, .81, .21 do not give the same clear below-threshold discrepancy. Printed .05 does not determine unrounded significance.

**Source-grounded alternative:** The prose may summarize only HR survival comparisons. In-hospital HR P=.14 then agrees, as does the referenced Figure 2B 12-month HR analysis. Distinct AD/HR analyses need not give identical significance.

**Missing definitions:** Intended estimand/test scope of the blanket sentence; whether AD P=.009 is correctly printed.

**Human question:** Is the mortality sentence restricted to HR tests, or intended to cover all Table 3 mortality comparisons including in-hospital AD P=.009?

**Candidate boundary:** Prose versus AD P, distinct from STAT-A. Matching checker provenance for this exact pair/rule can be consolidated.

**Bounded downstream relevance:** A reviewer could copy a blanket nonsignificance interpretation while also extracting a below-threshold AD P. Intended scope or reporting defect requires human review.

## STAT-C — Discussion calls cumulative-incidence plots “HR curves”

**Relationship:** S104; M-N062/M-N066. S028/S046 give separate HR and method context.

**Proposed category and relationship type:** Measure, label, or scale inconsistency; S_W; all relationships S_W.

**Compared locations and roles:** REPORT Discussion [main article p. 7](../../../jama_wang_2018_oi_180070.pdf#page=7) versus REPORT Figure 2A [main article p. 8](../../../jama_wang_2018_oi_180070.pdf#page=8). REPORT Methods [main article p. 4](../../../jama_wang_2018_oi_180070.pdf#page=4) identifies Kaplan–Meier curves/Cox analysis. No PLAN location is a conflicting comparator.

**Printed values:** “The HR curves of these new clinical vascular events were almost completely separated in the first 30 days.” Figure 2A has two arm curves and y-axis “Cumulative Incidence,” ticks 0, .05, .10, .15; separate scalar HR 0.72 (95% CI 0.60–0.87), P<.001.

**Direct comparison and rule:** The figure labels its ordinate cumulative incidence in each arm. HR is a relative contrast, separately annotated, and is not the ordinate of the two displayed arm curves. The source's own figure label and separate HR annotation establish the quantity distinction.

**Calculation:** None needed; quantity name versus labeled ordinate. Intervention below control is compatible with HR<1. The qualitative first-30-days separation claim is not separately diagnosed.

**Source-grounded alternative:** “HR curves” may be shorthand for survival curves accompanied by an HR analysis. Correct figure labels bound confusion. Exact underlying curve values are not supplied.

**Missing definition and human question:** Does “HR curves” refer to Figure 2A's cumulative-incidence curves, or a separate unshown HR-versus-time curve? If Figure 2A is intended, is the quantity name shorthand or a reporting label requiring review? No alternate HR curve is identified.

**Candidate boundary:** Matching numeric/cross-source comparisons of this exact p.7 wording/p.8 axis can share provenance. Annotation log-rank/Cox provenance is a separate missing-definition limitation with no opposing number.

**Bounded downstream relevance:** The quantity name could be copied into a summary if confirmed. No effect-estimate change is assumed.

## Complete pass-1 coverage

Every record was checked for containment, endpoint order, sign/direction, effect-measure/scale labels, matched repetitions, and interval/P/test/SE/statistic compatibility to the extent defined by supplied evidence. All printed estimates lie inside ordered intervals; Ps remain paired with their own columns.

Named boundaries D-AD, D-GEE, D-COX, D-DISABILITY, D-BASELINE, D-POWER, D-SURVEY, D-UNQUANTIFIED, D-FIGURE are fully specified in the inventory. Missing definitions alone are not candidates.

Completed non-candidate checks include adjusted effects versus crude proportions; HR versus raw risk ratios; separate AD/HR significance or sign; narrative rounding; printed .05 boundaries; Figure 2 P provenance without an opposing value; insufficient rank-test/power inputs; the illustrative seven-opportunity example; and explicit primary/sensitivity denominator changes.

No displayed-zero P occurs. DISPLAY_ZERO_NOT_CANDIDATE was applied globally; no tiny positive tail probability was reconstructed. S041's −0.0 is a rounded interval endpoint, not a displayed-zero P.

| Relationship ID | Completion | Provenance and definition boundary | Candidate or bounded decision |
|---|---|---|---|
| S001 | PASS_1_COMPLETE | M-S001; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S002 | PASS_1_COMPLETE | M-S002; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S003 | PASS_1_COMPLETE | M-S003; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S004 | PASS_1_COMPLETE | M-S004; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S005 | PASS_1_COMPLETE | M-S005; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S006 | PASS_1_COMPLETE | M-S006; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S007 | PASS_1_COMPLETE | M-S007; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S008 | PASS_1_COMPLETE | M-S008; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S009 | PASS_1_COMPLETE | M-S009; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S010 | PASS_1_COMPLETE | M-S010; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S011 | PASS_1_COMPLETE | M-S011; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S012 | PASS_1_COMPLETE | M-S012; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S013 | PASS_1_COMPLETE | M-S013; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S014 | PASS_1_COMPLETE | M-S014; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S015 | PASS_1_COMPLETE | M-S015; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S016 | PASS_1_COMPLETE | M-S016; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S017 | PASS_1_COMPLETE | M-S017; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S018 | PASS_1_COMPLETE | M-S018; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S019 | PASS_1_COMPLETE | M-S019; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S020 | PASS_1_COMPLETE | M-S020; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S021 | PASS_1_COMPLETE | M-S021; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S022 | PASS_1_COMPLETE | M-S022; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S023 | PASS_1_COMPLETE | M-S023; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S024 | PASS_1_COMPLETE | M-S024; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S025 | PASS_1_COMPLETE | M-S025; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S026 | PASS_1_COMPLETE | M-S026; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S027 | PASS_1_COMPLETE | M-S027; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S028 | PASS_1_COMPLETE | M-S028; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S029 | PASS_1_COMPLETE | M-S029; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S030 | PASS_1_COMPLETE | M-S030; D-DISABILITY; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S031 | PASS_1_COMPLETE | M-S031; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S032 | PASS_1_COMPLETE | M-S032; D-DISABILITY; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S033 | PASS_1_COMPLETE | M-S033; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S034 | PASS_1_COMPLETE | M-S034; D-DISABILITY; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S035 | PASS_1_COMPLETE | M-S035; D-AD; exact inputs/PDF pages in inventory | STAT-A CI/P; STAT-B prose/P: distinct comparisons. |
| S036 | PASS_1_COMPLETE | M-S036; D-COX; exact inputs/PDF pages in inventory | Separate HR P=.14 context for STAT-A/STAT-B. |
| S037 | PASS_1_COMPLETE | M-S037; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S038 | PASS_1_COMPLETE | M-S038; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S039 | PASS_1_COMPLETE | M-S039; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S040 | PASS_1_COMPLETE | M-S040; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S041 | PASS_1_COMPLETE | M-S041; D-AD; exact inputs/PDF pages in inventory | Boundary/rounding does not establish contradiction without unrounded/shared construction. |
| S042 | PASS_1_COMPLETE | M-S042; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S043 | PASS_1_COMPLETE | M-S043; D-UNQUANTIFIED; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S044 | PASS_1_COMPLETE | M-S044;SUP-S040; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S045 | PASS_1_COMPLETE | M-S045;SUP-S041; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S046 | PASS_1_COMPLETE | M-S046;M-N066; D-FIGURE; exact inputs/PDF pages in inventory | Unknown annotation P provenance alone is not a candidate. |
| S047 | PASS_1_COMPLETE | SUP-S001;M-N012; D-POWER; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S048 | PASS_1_COMPLETE | SUP-S002;M-N014; D-BASELINE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S049 | PASS_1_COMPLETE | SUP-S003;M-N009;M-N014;M-N015; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S050 | PASS_1_COMPLETE | SUP-S004;M-N010;M-N014;M-N016; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S051 | PASS_1_COMPLETE | SUP-S005;SUP-N025;SUP-N026; D-SURVEY; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S052 | PASS_1_COMPLETE | SUP-S006; D-BASELINE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S053 | PASS_1_COMPLETE | SUP-S007; D-BASELINE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S054 | PASS_1_COMPLETE | SUP-S008; D-BASELINE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S055 | PASS_1_COMPLETE | SUP-S009; D-BASELINE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S056 | PASS_1_COMPLETE | SUP-S010; D-BASELINE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S057 | PASS_1_COMPLETE | SUP-S011; D-BASELINE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S058 | PASS_1_COMPLETE | SUP-S012; D-BASELINE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S059 | PASS_1_COMPLETE | SUP-S013; D-BASELINE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S060 | PASS_1_COMPLETE | SUP-S014; D-BASELINE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S061 | PASS_1_COMPLETE | SUP-S015; D-BASELINE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S062 | PASS_1_COMPLETE | SUP-S016; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S063 | PASS_1_COMPLETE | SUP-S017; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S064 | PASS_1_COMPLETE | SUP-S018; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S065 | PASS_1_COMPLETE | SUP-S019; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S066 | PASS_1_COMPLETE | SUP-S020; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S067 | PASS_1_COMPLETE | SUP-S021; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S068 | PASS_1_COMPLETE | SUP-S022; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S069 | PASS_1_COMPLETE | SUP-S023; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S070 | PASS_1_COMPLETE | SUP-S024; D-AD; exact inputs/PDF pages in inventory | Boundary/rounding does not establish contradiction without unrounded/shared construction. |
| S071 | PASS_1_COMPLETE | SUP-S025; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S072 | PASS_1_COMPLETE | SUP-S026; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S073 | PASS_1_COMPLETE | SUP-S027; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S074 | PASS_1_COMPLETE | SUP-S028; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S075 | PASS_1_COMPLETE | SUP-S029; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S076 | PASS_1_COMPLETE | SUP-S030; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S077 | PASS_1_COMPLETE | SUP-S031; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S078 | PASS_1_COMPLETE | SUP-S032; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S079 | PASS_1_COMPLETE | SUP-S033; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S080 | PASS_1_COMPLETE | SUP-S034; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S081 | PASS_1_COMPLETE | SUP-S035; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S082 | PASS_1_COMPLETE | SUP-S036; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S083 | PASS_1_COMPLETE | SUP-S037; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S084 | PASS_1_COMPLETE | SUP-S038; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S085 | PASS_1_COMPLETE | SUP-S039; D-COX; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S086 | PASS_1_COMPLETE | SUP-S042; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S087 | PASS_1_COMPLETE | SUP-S043; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S088 | PASS_1_COMPLETE | SUP-S044; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S089 | PASS_1_COMPLETE | SUP-S045; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S090 | PASS_1_COMPLETE | SUP-S046; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S091 | PASS_1_COMPLETE | SUP-S047; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S092 | PASS_1_COMPLETE | SUP-S048; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S093 | PASS_1_COMPLETE | SUP-S049; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S094 | PASS_1_COMPLETE | SUP-S050; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S095 | PASS_1_COMPLETE | SUP-S051; D-GEE; exact inputs/PDF pages in inventory | Boundary/rounding does not establish contradiction without unrounded/shared construction. |
| S096 | PASS_1_COMPLETE | SUP-S052; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S097 | PASS_1_COMPLETE | SUP-S053; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S098 | PASS_1_COMPLETE | SUP-S054; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S099 | PASS_1_COMPLETE | SUP-S055; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S100 | PASS_1_COMPLETE | SUP-S056; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S101 | PASS_1_COMPLETE | SUP-S057; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S102 | PASS_1_COMPLETE | SUP-S058; D-AD; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S103 | PASS_1_COMPLETE | SUP-S059; D-GEE; exact inputs/PDF pages in inventory | No independent statistical contradiction found; named reconstruction boundary recorded. |
| S104 | PASS_1_COMPLETE | M-N062;M-N066; D-FIGURE; exact inputs/PDF pages in inventory | STAT-C: plotted quantity versus discussion quantity name. |

## Pass-2 handoff

A different fresh gpt-6.1-sol/high agent must revisit all 104 records with the complete numeric/cross-source ledger and mechanical recheck. S052–S061 availability-group counts require full-cohort Table 1 reconciliation from cross-lane evidence, without inventing unavailable inputs. Carry forward source recheck facts, AD/HR distinctions, interval/P construction limits, prose scope, and plotted quantity names. No assigned candidate or relationship ID may be deleted or renumbered. This pass-1 agent has not performed pass 2.

