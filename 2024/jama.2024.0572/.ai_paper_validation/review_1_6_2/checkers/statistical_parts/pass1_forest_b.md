# Statistical pass 1: forest B

- Runtime agent identity: /root/stat1_forest_b
- Model/effort: gpt-6.1-sol/high
- Start mode: FRESH_SPAWN
- Exact assigned scope: DOC-006 physical pp16-19,eFigures10-13,A031-A034;64 effect/CI rows and32 interaction tests.
- Relationship IDs: S2001-S2096; every record PASS_1_COMPLETE.
- Findings:1,F-ST1-201. Excluded apparent observations:3. Scientific coverage gaps:0.
- Relationship artifact: statistics/parts/forest_b.md.
- Sources and reused evidence preserved; no web, old candidate conclusions or unapproved extraction helpers used.

The complete scope and review contract were read. All four forest source-linked images were read visually, with direct PDF text establishing captions and directly read main-report/current-analysis-SAP methods supplying adjustment, endpoint and test context. Every printed point estimate is inside its95%CI and all interval endpoints are ordered;64/64 containment checks reconcile. Interaction P values were treated as tests of treatment heterogeneity, never as individual row-effect P values. No superiority, noninferiority, equivalence or stopping claim is made by these displays. Numeric findings are restricted to reproduced source observations; no adjusted RR is replaced by a crude ratio.

### F-ST1-201

**Title:** eFigure13 direction annotations reverse the interpretation of the printed complete-dependence/death relative risks.

**Exact compared locations and document roles:** REPORT [DOC-006 physical p19,eFigure13](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=19), title (“complete dependence or death(mRS5-6) at90-day follow-up”), column “Relative Risk(95%CI),” both treatment-event columns, all16 plotted rows, and bottom axis “Relative Risk of achieving mRS5-6(95%CI) in Thrombectomy group compared to Medical Management group.” On that same axis, the left side is labeled “Favours Medical Management” and the right side “Favours Thrombectomy.” The comparison is entirely within this REPORT page. [REPORT main article p3](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3) identifies mRS5-6 as complete dependence or death; it corroborates endpoint identity without being a second side of the discrepancy.

**Printed values and affected locations:**

| S ID | eFigure13 row | Printed EVT event count(percent) | Printed MM event count(percent) | Printed relative risk(95%CI) |
|---|---|---|---|---|
| S2049 | 1: NCCT<70 (N=132) | 27(39.71) | 39(60.94) | .68(.49-.95) |
| S2050 | 2: NCCT≥70 (N=204) | 49(49.00) | 63(60.58) | .77(.62-.97) |
| S2051 | 3: largest<70 (N=80) | 14(33.33) | 17(44.74) | .82(.49-1.37) |
| S2052 | 4: largest≥70 (N=256) | 62(49.21) | 85(65.38) | .72(.60-.88) |
| S2053 | 5: NCCT<100 (N=207) | 37(35.92) | 60(57.69) | .61(.46-.81) |
| S2054 | 6: NCCT≥100 (N=129) | 39(60.00) | 42(65.62) | .87(.69-1.10) |
| S2055 | 7: largest<100 (N=165) | 26(32.50) | 44(51.76) | .62(.44-.86) |
| S2056 | 8: largest≥100 (N=171) | 50(56.82) | 58(69.88) | .78(.64-.96) |
| S2057 | 9: NCCT<150 (N=297) | 69(45.70) | 85(58.22) | .76(.62-.93) |
| S2058 | 10: NCCT≥150 (N=39) | 7(41.18) | 17(77.27) | .55(.33-.94) |
| S2059 | 11: largest<150 (N=273) | 59(43.70) | 78(56.52) | .72(.58-.90) |
| S2060 | 12: largest≥150 (N=63) | 17(51.52) | 24(80.00) | .69(.48-.97) |
| S2061 | 13: largest profile ratio≥1.2/volume≥10:0 (N=74) | 12(35.29) | 23(57.50) | .67(.41-1.10) |
| S2062 | 14: largest profile ratio≥1.2/volume≥10:1 (N=262) | 64(47.76) | 79(61.72) | .74(.61-.90) |
| S2063 | 15: largest profile ratio≥1.8/volume≥15:0 (N=211) | 50(45.05) | 61(61.00) | .76(.60-.95) |
| S2064 | 16: largest profile ratio≥1.8/volume≥15:1 (N=125) | 26(45.61) | 41(60.29) | .71(.53-.97) |

**Rule and reproduced calculation:** For the printed adverse outcome and printed contrast, RR=risk(mRS5-6|EVT)/risk(mRS5-6|MM). Values below1 correspond to less complete dependence/death with EVT; values above1 correspond to more of that outcome with EVT. All16 printed point estimates are below1, with RR ranging.55-.87, but each lies on the axis side labeled as favoring medical management. For example, row1 prints RR.68(.49-.95), EVT27(39.71%) and MM39(60.94%); its modeled RR shows lower adverse-outcome risk with EVT, while the side annotation assigns that region to medical-management benefit. Descriptive arm proportions also have the same lower-risk direction, but no crude proportion ratio is substituted for the adjusted RR.

**Display-precision calculation:** This is a categorical reversal of the direction attached to an explicitly printed risk contrast, rather than disagreement between two numeric copies. No recomputed numeric interval or relative numeric discrepancy applies to the label itself. The direction is nevertheless invariant to half-unit rounding: row1 printed RR.68 permits [.675,.685], wholly below null1; all16 printed points have upper half-unit limits at most.875, also below1. Thirteen printed CIs are wholly below1; the other three contain1, but their point estimates still share the direction mismatch. The issue is the direction label, not significance claimed for those three intervals.

**Focus area:** B, estimate and test logic; agreement between estimate, endpoint and direction annotations.

**Proposed review domain:** statistical_results.

**Proposed relationship type:** S_W. **All relationships:** S_W. **Compared document roles:** REPORT vs REPORT within DOC-006 p19. Main-method text only corroborates the adverse-outcome definition and is not an additional comparison relationship.

**Qualifying route:** Route A, category2.

**Affected result or extracted value:** The EVT-versus-MM interpretation of every eFigure13 relative risk for complete dependence or death at90days, including.68(.49-.95) for NCCT<70mL and.55(.33-.94) for NCCT≥150mL. A reader using the figure's printed favor annotations could assign the direction of these estimates to the opposite treatment.

**Why context does not resolve it:** Route A category2 requires registration of a reproduced direction statement that reverses printed values. The title and axis identify an adverse-outcome RR in EVT relative to MM, while the favor labels identify the lower-risk region as favoring MM. Immediate counts make the lower-event-rate arm identifiable but do not remove the opposite interpretation explicitly printed on the axis.

**Source-grounded alternatives and missing definitions:** The side annotations could have been carried over from desirable-outcome forests; that production mechanism is not inferred as fact. Alternatively, the annotations might be intended for avoiding mRS5-6, or the reciprocal MM/EVT contrast, but the printed title, count columns and axis identify achieving mRS5-6 and EVT relative to MM. Those alternative readings would require a different stated outcome or contrast. No raw-data or covariance definition is needed to reproduce this categorical inconsistency.

**Exact human question:** Which outcome direction and treatment contrast should a reader use when interpreting the “Favours Medical Management” and “Favours Thrombectomy” annotations in eFigure13, given the printed EVT/MM risk of complete dependence or death and the16 relative risks below1?

**Human review status:** Pending Human Adjudication.

## Excluded observations

Only apparent issues decided against emission are listed; reconciling checks are retained in the relationship inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-006 p17,eFigure11,NCCT≥150mL,S2026 | Printed adjusted RR.12(.01-1.05) contrasts with a crude ratio from1/17 versus1/22, equal to22/17=1.2941. The stated modified Poisson model adjusts prognostic variables, so crude direction and magnitude do not reproduce its adjusted estimate. The missing fitted coefficients cannot establish a conflicting adjusted calculation. | MODEL_VERSUS_CRUDE |
| REPORT DOC-006 p17,eFigure11,NCCT≥150mL,S2026 | Log-center diagnostic sqrt(.01×1.05)=.10247 differs from printed.12. Allowing endpoint half-unit intervals [.005,.015] and[1.045,1.055] gives a geometric-center interval [.072284,.125797], overlapping the point's[.115,.125]. Display-precision gap0; relative discrepancy0. This diagnostic does not assume the CI method as final authority. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-006 p16,eFigure10,NCCT150 interaction,S2069 with effect rowsS2009-S2010 | A diagnostic independent-normal reconstruction from GenOR1.70(1.33-2.19) and2.21(1.16-4.19) yields SE of log-difference≈.35146,z≈.74650,two-sided P≈.455, whereas printed interactionP=.8886. This diagnostic assumes independent subgroup estimates and a common log-Wald test; the source supplies neither that covariance nor the interaction coefficient/test statistic. It is not a method shown to reproduce the other interaction rows of this display. | CONDITIONAL_OR_UNREPORTED |

The final exclusion does not remove any interval-versus-own-P conflict: the printed P is explicitly an interaction test, not the P of either subgroup's treatment effect. Subgroup effect CIs do not establish the fitted interaction covariance or test. No Route A category4 observation has been reproduced by a method reproducing the other rows.

## Limits and handoff

Exact adjusted-model estimate/CI regeneration and exact interaction P regeneration require D1/D2 inputs named in the relationship inventory; their absence is documented without treating it as a conflicting printed result. No missing input blocks interval containment, endpoint ordering, endpoint/reference identity, within-display percentages, or source-defined direction checks. All96 assigned relationships are complete for pass1. Pass2 must be a distinct fresh high-effort statistical agent and revisit every ID together with the full ledger, screen and mechanical recheck; this agent has not assigned any stable candidate IDs or adjudication.

Artifact paths: statistics/parts/forest_b.md and checkers/statistical_parts/pass1_forest_b.md.

