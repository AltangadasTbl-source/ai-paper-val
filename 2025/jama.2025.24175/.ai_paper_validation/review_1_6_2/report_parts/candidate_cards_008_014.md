<a id="C008"></a>

## C008 — Unadjusted day-15 immunoparalysis odds ratio does not reconcile with its counts

Pending Human Adjudication.

**Candidate statement:** The final row of eTable 10 prints an unadjusted odds ratio of 1.194 for day-15 SOFA response in sepsis-induced immunoparalysis. Its displayed counts yield 1.943574 under the count-based method that reproduces all three companion rows.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 10 final row vs companion rows and displayed counts

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 4.

**Classification rationale:** The point, counts, unadjusted label and supporting companion rows are reported results within one results supplement. This is an estimate-construction comparison, with no conflicting PLAN location. F-ST1-004 independently described the same issue and was screened as duplicate provenance.

**Classification ambiguity:** The document roles are clear. An alternative unadjusted computation or analysis population that would associate 1.194 with this row is not identified.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.22, eTable 10, final day-15 immunoparalysis row and all three companion rows](../../../joi250116supp2_prod_1771885794.27755.pdf#page=22).

**Source evidence:** The affected row reports precision immunotherapy 40/106 (37.7%) and placebo 29/122 (23.8%), difference 13.9 (1.9–25.6), unadjusted OR 1.194 (95% CI, 1.09–3.45), and P=.030. The other three rows report counts 12/25 versus 4/23 with OR 4.38; 34/106 versus 22/122 with OR 2.15; and 12/25 versus 5/23 with OR 3.32. Direct source inspection confirms that the affected point reads 1.194, rather than 1.94.

**Reported-versus-comparator:** Printed 1.194 is compared with the count-cross-product OR 1.943573668. The comparator is justified by the explicit unadjusted label and the same display's three reproducing rows; this is not a comparison of an adjusted estimate with a crude ratio.

**Reasoning procedure:** Read the row, outcome window and column alignment from the source page. Compute event odds in each arm and their ratio. Apply the same construction to the other three rows, then allow the displayed inputs and point their half-unit precision intervals. The unresolved question is which unadjusted computation and population produced the printed point, rather than which estimate should replace it.

**Calculation:** The affected OR is `40×(122−29)/[(106−40)×29]=1.943573668`. Companion values are 4.384615385, 2.146464646 and 3.323076923, reproducing their displayed points. Conservatively allowing independent count/denominator half-unit ranges gives `[39.5×92/(67×29.5),40.5×94/(65×28.5)]=[1.838603592,2.055060729]`. Printed 1.194 allows [1.1935,1.1945]. The minimum gap is .644103592 and relative discrepancy `.644103592/1.194=.539450245`, above .05. Exact-integer inputs would narrow the comparator range. The CI's geometric center, approximately 1.93920, is additional corroboration and is not adopted as a replacement estimate.

**Affected result or extracted value:** The unadjusted day-15 SOFA-response OR for the immunoparalysis subgroup, specifically its effect magnitude.

**Why context does not resolve it:** Route A, category 4 applies: a printed estimate does not reproduce beyond the display threshold under a method that reproduces the companion rows. Reconstructing a plausible intended point does not remove the printed reading that an extractor could take.

**Alternative source-grounded interpretations:** A different underlying population or unprinted unadjusted computation could account for the point. The display identifies neither distinction. A substituted digit is another possible explanation, but no production mechanism or intended replacement is established.

**Mechanical evidence recheck:** A fresh 200-dpi CPU render of the exact source page was visually read; every affected and companion count/point was confirmed. Independent arithmetic reproduced the discrepancy with no source transcription or location change. The evidence state records this comparison, without adjudicating an intended value.

**Potential downstream evidence impact:** If confirmed, the issue could affect extraction of the subgroup's unadjusted OR and its magnitude. No propagation or change to a synthesized conclusion is established.

<a id="C009"></a>

## C009 — MALS number-needed-to-harm direction does not reconcile with patient risks

Pending Human Adjudication.

**Candidate statement:** eTable 15 labels positive MALS NNH1=8.8 as the number needed to treat to induce at least one serious treatment-emergent adverse event, whereas the corresponding patient risks are lower under anakinra than placebo.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 13 Any SAE counts vs eTable 15 MALS NNH1

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-005

**Qualifying route:** Route A, category 2.

**Classification rationale:** The harm-induction label, NNH point and corresponding patient risks are conflicting REPORT content within the results supplement. Its patient-count footnote is corroboration. No prospective plan comparison participates.

**Classification ambiguity:** The table does not specify a sign convention or whether an unsigned reciprocal is used for both prevention and induction of harm. This uncertainty does not alter the source roles or relationship.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.27, eTable 13, MALS Any SAE row](../../../joi250116supp2_prod_1771885794.27755.pdf#page=27); [physical PDF p.44, eTable 15, MALS NNH1 and induce-harm definition](../../../joi250116supp2_prod_1771885794.27755.pdf#page=44). Definition support: [physical PDF p.29, eTable 13 footnote a](../../../joi250116supp2_prod_1771885794.27755.pdf#page=29).

**Source evidence:** Any SAE occurs in 20/25 (80.0%) MALS patients under anakinra and 21/23 (91.3%) under placebo. The marked footnote confirms numbers of patients for this row, rather than numbers of events. eTable 15 prints NNH1=8.8 (95% CI, 3.2–10.0) and defines this quantity as patients needed to treat to induce at least one serious TEAE; NNH is defined as number needed to harm.

**Reported-versus-comparator:** The positive harm-induction reading is compared with a negative treatment-minus-placebo risk difference and its negative signed reciprocal. The unsigned reciprocal magnitude is close to 8.8; direction and reference convention, rather than that magnitude's rounding, are the issue.

**Reasoning procedure:** Confirm that the adverse-event inputs count patients with at least one event. Calculate treatment risk minus placebo risk, then its signed reciprocal. Test whether the direction survives conservative half-unit ranges and compare it with the explicit induce-harm label. The unresolved question is whether 8.8 denotes prevention or induction, and which reference/sign convention governs it.

**Calculation:** `20/25−21/23=−.113043478`; its signed reciprocal is −8.846153846. Conservative count/denominator ranges give risk difference `[19.5/25.5−21.5/22.5,20.5/24.5−20.5/23.5]=[−.190849673,−.035605732]`. Its reciprocal range is [−28.085365854,−5.239726027], separated from the printed point range [8.75,8.85] by at least 13.989726027; relative discrepancy is 1.589741594. Printed risk precision also preserves the negative direction: [79.95,80.05]% minus [91.25,91.35]% gives [−11.40,−11.20] percentage points.

**Affected result or extracted value:** The harm-versus-benefit interpretation and treatment/reference direction of MALS NNH1=8.8.

**Why context does not resolve it:** Route A, category 2 applies: the explicit harm-induction reading reverses the direction supported by the corresponding patient risks, beyond display precision. The source does not explain an unsigned or reversed-reference convention.

**Alternative source-grounded interpretations:** An absolute reciprocal convention, or placebo relative to anakinra as the reference direction, could generate positive 8.8. Neither is stated in the label, which does not distinguish prevention from induction for this row. The card does not choose among these explanations.

**Mechanical evidence recheck:** Fresh source renders of pp.27,29 and44 were visually reread. Patient counts, denominators, footnote marker, NNH point and harm wording were confirmed; independent signed-risk and half-unit calculations reproduced the direction comparison without transcription changes. C010 separately examines confidence-set compatibility, using a distinct rule.

**Potential downstream evidence impact:** If confirmed, extraction could associate 8.8 with induction rather than prevention of serious TEAEs, or assign a different reference direction. This is a bounded evidence-description concern, not a clinical safety judgment.

<a id="C010"></a>

## C010 — Finite NNH1 intervals versus nonsignificant source-specified safety comparisons

Pending Human Adjudication.

**Candidate statement:** The finite positive 95% NNH1 intervals for MALS and immunoparalysis omit the no-effect/infinite-number limit, while independently applying the supplied two-sided Fisher safety test to the corresponding patient counts gives nonsignificant comparisons. The connection between the confidence procedure and that test is not specified.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 13 MALS/IP counts vs eTable 15 NNH1 intervals; supplied safety test is corroboration

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-006

**Qualifying route:** Route A, category 1.

**Classification rationale:** The conflicting numerical displays are within the REPORT results supplement. The main article's methods and PLAN SAP supply the safety-test definition as corroboration; neither prints a competing numerical result. They therefore add neither S_C nor P_R.

**Classification ambiguity:** The NNH confidence construction, its analysis population and its correspondence to the Fisher safety test are undefined. The candidate does not assume identical confidence and test procedures.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.27, eTable 13, MALS and immunoparalysis Any SAE patient rows](../../../joi250116supp2_prod_1771885794.27755.pdf#page=27); [physical PDF p.44, eTable 15, both NNH1 intervals](../../../joi250116supp2_prod_1771885794.27755.pdf#page=44). Patient-count support: [physical PDF p.29, footnote a](../../../joi250116supp2_prod_1771885794.27755.pdf#page=29). Test corroboration: [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf — physical PDF p.6, significance and SAP-following statements](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6); [joi250116supp1_prod_1771885794.26255.pdf — physical PDF p.70, SAP Safety and two-sided significance specification](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70).

**Source evidence:** MALS NNH1 is 8.8 (95% CI, 3.2–10.0); immunoparalysis NNH1 is 47.6 (95% CI, 9.9–55.8), both labeled for induction of at least one serious TEAE. Corresponding patient counts are MALS 20/25 versus 21/23 and immunoparalysis 96/106 versus 108/122. The SAP specifies Fisher's exact comparisons of serious/nonserious TEAE incidence by immune stratum and two-sided .05 significance; the article states that analyses followed the SAP.

**Reported-versus-comparator:** Printed finite positive confidence bounds are compared with independently recomputed Fisher probabilities .419120073 and .669907887. These probabilities are calculations from supplied counts and the stated test; they are not printed publication P values. Under an ordinary reciprocal risk-difference confidence-set reading, the bounds exclude zero risk difference and the infinite-NNH no-effect limit.

**Reasoning procedure:** Confirm the patient-risk pairs, confidence level and safety-test specification. Enumerate the fixed-margin probability-order two-sided Fisher tests. Invert the positive finite NNH limits to identify the risk-difference values they represent, then compare their no-effect compatibility with those tests. The question is what confidence transformation, population and sign/set convention produced the bounds and how they relate to the named safety comparisons.

**Calculation:** The independently recomputed two-sided Fisher probabilities are .419120073 for MALS and .669907887 for immunoparalysis, both above .05. Reciprocals of the printed intervals give MALS `[1/10.0,1/3.2]=[.100000,.312500]` and immunoparalysis `[1/55.8,1/9.9]=[.017921,.101010]`, neither containing zero. Each exact-count half-unit interval contains only its displayed integer for contingency enumeration. Bound rounding also preserves positive finite limits: MALS [3.15,3.25] and [9.95,10.05]; immunoparalysis [9.85,9.95] and [55.75,55.85]. It cannot reach infinity/no effect. Route A category 1 is not screened by the .05 relative-discrepancy rule.

**Affected result or extracted value:** Confidence-set interpretation and no-effect compatibility of the two NNH1 entries, rather than the separately registered MALS direction issue in C009.

**Why context does not resolve it:** Route A, category 1 applies to the interval-versus-specified-test comparison. The missing procedure remains a bounded explanation question; attributing the interval and test to different analyses is an alternative, rather than removal of this category.

**Alternative source-grounded interpretations:** A different confidence procedure or patient population may underlie the intervals. Their finite bounds could also abbreviate a split confidence set crossing the reciprocal singularity, or use an absolute-risk-difference convention. A confidence procedure and Fisher test need not be computationally identical. None of these mappings is supplied, and no replacement interval is proposed.

**Mechanical evidence recheck:** Fresh original-page renders confirmed both confidence intervals, both patient-count pairs, the patient-count footnote and methodological corroboration. Independent exact-test enumeration reproduced the two nonsignificant probabilities. The state records the specified interval/test comparison, without determining which unreported confidence-set interpretation applies.

**Potential downstream evidence impact:** If confirmed, an extractor could record finite confidence bounds as excluding no effect despite the nonsignificant named safety comparisons, or interpret an abbreviated confidence set as an ordinary connected interval. No downstream use or conclusion change is asserted.

<a id="C011"></a>

## C011 — Five subgroup P values do not reproduce under the companion-row test

Pending Human Adjudication.

**Candidate statement:** Five panel-A P values across eFigures 7–9 do not reproduce under probability-order two-sided Fisher calculations from their printed integer counts, beyond the display threshold. The same calculation reproduces all 13 other rows under that rule.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eFigures 7, 8 and 9 panel A P values vs same-display counts and companion rows

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 4.

**Classification rationale:** The conflicting counts and P values are within the REPORT results supplement. Main-article Fisher methods corroborate the calculation but do not supply a conflicting result or add S_C. This repeated pattern is one candidate; it does not assign a crude count test to panel-B model interactions.

**Classification ambiguity:** A row-specific alternative test, analysis population, sidedness or adjustment could explain the affected values, but no such distinction is printed.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.51, eFigure 7 panel A, primary response, APACHE II≥25, CCI≥5 and SOFA≥10 rows](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51); [physical PDF p.52, eFigure 8 panel A, 28-day mortality, SOFA≥10 row](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52); [physical PDF p.53, eFigure 9 panel A, 90-day mortality, SOFA≥10 row](../../../joi250116supp2_prod_1771885794.27755.pdf#page=53). Each page's remaining panel-A rows supplies companion evidence. Corroborating methods: [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf — physical PDF p.6](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6).

**Source evidence:** Panel-A captions identify primary attainment, 28-day mortality and 90-day mortality. Counts below are reordered to treatment first and placebo second; reversing the source's column order does not change a two-sided Fisher probability. The five printed P values are .439, .003, .035, .045 and .209 for the named rows.

**Reported-versus-comparator:** The complete affected pattern is:

| Outcome / stratum | Treatment events/total | Placebo events/total | Printed P | Recomputed Fisher P | Minimum precision gap | Relative gap |
|---|---|---|---:|---:|---:|---:|
| Primary response, APACHE II≥25 | 12/38 | 8/40 | .439 | .303200218 | .135299782 | .308199958 |
| Primary response, CCI≥5 | 20/54 | 7/76 | .003 | .000158910 | .002341090 | .780363217 |
| Primary response, SOFA≥10 | 25/67 | 11/68 | .035 | .006531327 | .027968673 | .799104929 |
| 28-day mortality, SOFA≥10 | 35/67 | 48/68 | .045 | .034400792 | .010099208 | .224426837 |
| 90-day mortality, SOFA≥10 | 49/67 | 57/68 | .209 | .146989715 | .061510285 | .294307583 |

**Reasoning procedure:** Read every panel-A row directly and independently enumerate the exact probability-order two-sided Fisher test for its integer contingency table. Establish the method's reproduction in each display through companion rows before applying the precision rule to the five affected rows. Which test and contingency population produced those five P values remains unspecified; no source mechanism is inferred.

**Calculation:** For treatment sample size n, placebo size m, total events K and treatment events a, sum `choose(K,x)×choose(n+m−K,n−x)/choose(n+m,n)` over feasible integer x whose probability is no greater than the observed table's probability. Printed three-decimal P intervals are P±.0005: [.4385,.4395], [.0025,.0035], [.0345,.0355], [.0445,.0455] and [.2085,.2095]. Exact input-count half-unit intervals contain only the printed integer, so each recomputed P interval is a singleton. Its distance from the printed interval, divided by printed P, gives the table's relative gap; all five exceed .05.

All 13 companion rows reproduce under the stipulated rule:

| Outcome / stratum | Treatment events/total | Placebo events/total | Printed P | Recomputed Fisher P | Relative precision gap |
|---|---|---|---:|---:|---:|
| Primary response, APACHE II<25 | 34/93 | 18/105 | .002 | .002176542 | 0 |
| Primary response, CCI<5 | 26/77 | 19/69 | .475 | .474644233 | 0 |
| Primary response, SOFA<10 | 21/64 | 15/77 | .083 | .082691021 | 0 |
| 28-day mortality, APACHE II≥25 | 22/38 | 27/40 | .489 | .483109060 | .011024416 |
| 28-day mortality, APACHE II<25 | 35/93 | 45/105 | .472 | .471707802 | 0 |
| 28-day mortality, CCI≥5 | 24/54 | 50/76 | .020 | .019643739 | 0 |
| 28-day mortality, CCI<5 | 33/77 | 22/69 | .231 | .231037136 | 0 |
| 28-day mortality, SOFA<10 | 22/64 | 24/77 | .721 | .720788007 | 0 |
| 90-day mortality, APACHE II≥25 | 31/38 | 32/40 | >.99 | 1.000000000 | Inequality satisfied |
| 90-day mortality, APACHE II<25 | 59/93 | 66/105 | >.99 | 1.000000000 | Inequality satisfied |
| 90-day mortality, CCI≥5 | 39/54 | 64/76 | .123 | .125049970 | .012601380 |
| 90-day mortality, CCI<5 | 51/77 | 34/69 | .045 | .044623206 | 0 |
| 90-day mortality, SOFA<10 | 41/64 | 41/77 | .231 | .231336669 | 0 |

The two nonzero companion relative gaps remain below .05; exact agreement to every printed digit is not claimed.

**Affected result or extracted value:** The five named subgroup P values and their interpretation for primary response, 28-day mortality and 90-day mortality.

**Why context does not resolve it:** Route A, category 4 applies: the calculation reproducing all companion rows does not reproduce the five printed results beyond display precision. An unstated row-specific method is the explanation question, not a reason to treat the comparison as conditional.

**Alternative source-grounded interpretations:** Different tests, contingency populations or adjustments could underlie the five values. No immediate row label identifies such differences. These possibilities are retained without asserting which value or procedure was intended, and no exact forest-plot interval is inferred from pixels.

**Mechanical evidence recheck:** Fresh source renders confirmed all 18 contingency tables, all P entries and outcome labels. Independent exact calculations reproduced the five discrepancies and the 13 supporting rows, with no source transcription or location change.

**Potential downstream evidence impact:** If confirmed, extraction could take any of the five printed subgroup P values rather than the value produced by the companion-supported method. This concern is limited to those five entries; it does not establish a change in overall trial inference.

<a id="C012"></a>

## C012 — Repeated APACHE coefficient does not reproduce the companion interval construction

Pending Human Adjudication.

**Candidate statement:** In panel B of both eFigures 7 and 8, the APACHE II≥25 main-effect OR .47 does not reproduce the geometric center of its 95% CI .30–1.62 beyond display precision, while all five companion rows reproduce that construction under the workflow rule.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eFigures 7 and 8 panel B APACHE coefficient vs interval and companion rows

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-003

**Qualifying route:** Route A, category 4.

**Classification rationale:** The points, intervals and method-support comparators are REPORT content within one results supplement. No PLAN location or cross-document conflicting result is involved. C013 separately addresses outcome attribution rather than interval construction.

**Classification ambiguity:** The precise confidence procedure is not printed. A row-specific non-log-symmetric procedure remains possible, but no such distinction is identified.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.51, eFigure 7 panel B, APACHE II≥25 main-effect row and five companions](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51); [physical PDF p.52, eFigure 8 panel B, corresponding row and five companions](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52).

**Source evidence:** Both pages print APACHE II≥25 OR .47 (95% CI, .30–1.62), P=.70. This is the main-effect row, distinct from the APACHE-treatment interaction immediately beneath it. The other five points and intervals are identical on both pages and are listed below.

**Reported-versus-comparator:** The point .47 is compared with `sqrt(.30×1.62)=.697137002`, the center of a log-symmetric ratio interval. Same-display companion reproduction supports the construction. The printed P=.70 is retained as a source fact; this candidate does not assert an independent exact Wald-test contradiction.

**Reasoning procedure:** Confirm the point, confidence limits, row identity and companion rows on both original pages. Evaluate the geometric center and its range over rounded interval endpoints, then compare with the printed point's precision range. Determine whether the construction also reproduces the other rows. The remaining question is which coefficient and confidence procedure produced the repeated APACHE point/interval pairing.

**Calculation:** Limits [.295,.305] and [1.615,1.625] allow center range [.690235467,.704006392]. Point .47 allows [.465,.475], giving minimum gap .215235467 and relative discrepancy `.215235467/.47=.457947802`. All five companion rows satisfy the .05 threshold:

| Row on both pages | OR (95% CI) | Geometric center | Center range from rounded limits | Minimum point-range gap | Relative gap |
|---|---|---:|---|---:|---:|
| APACHE II≥25×precision immunotherapy | 1.85 (.66–5.19) | 1.850783618 | [1.842871401,1.858675604] | 0 | 0 |
| CCI≥5 | .22 (.09–.53) | .218403297 | [.211246302,.225444006] | 0 | 0 |
| CCI≥5×precision immunotherapy | 5.79 (2.34–15.05) | 5.934391291 | [5.927062932,5.941714820] | .132062932 | .022808797 |
| SOFA≥10 | .56 (.27–1.19) | .566833309 | [.560379336,.573258232] | 0 | 0 |
| SOFA≥10×precision immunotherapy | 3.08 (1.37–6.96) | 3.087911916 | [3.081164553,3.094652646] | 0 | 0 |

The CCI-treatment row has a nonzero precision gap, but its relative gap is below .05. Thus the statement is reproduction under the workflow rule, not exact log symmetry at every printed digit.

**Affected result or extracted value:** The repeated APACHE II≥25 main-effect point and its associated confidence interval in the primary-response and 28-day-mortality panel-B outputs.

**Why context does not resolve it:** Route A, category 4 applies: the printed point does not reproduce the construction supported by all five other rows, beyond display precision. The source does not supply a row-specific interval method explaining its separation.

**Alternative source-grounded interpretations:** A non-log-symmetric confidence procedure could apply to this row, or the point and limits could refer to different coefficients or analyses. Neither interpretation is specified. No preferred procedure or replacement coefficient is proposed, and unavailable coefficient standard errors/covariance prevent reconstructing the original fit.

**Mechanical evidence recheck:** Both complete source panels were freshly rendered and visually inspected. Every source point and limit was confirmed, and independent arithmetic reproduced the affected gap and companion support. Refined companion-center arithmetic changed no source transcription, so the evidence state remains reproduced.

**Potential downstream evidence impact:** If confirmed, extraction could pair .47 with an interval generated under an unidentified construction or from a different coefficient. This concern is bounded to the repeated APACHE rows and does not establish any downstream effect.

<a id="C013"></a>

## C013 — Complete six-row output has unresolved attribution to two outcomes

Pending Human Adjudication.

**Candidate statement:** The complete six-row panel-B OR/CI/P array is identical in eFigures 7 and 8, although the captions explicitly assign it to primary response and 28-day mortality respectively. The supplied material does not identify the outcome-model mapping that explains this repeated array.

**Review domain:** report_internal_inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eFigure 7 primary-response panel B vs eFigure 8 28-day-mortality panel B

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-008

**Qualifying route:** Route B.

**Classification rationale:** The issue concerns which outcome a reported numeric array belongs to within the REPORT results supplement, rather than estimate arithmetic; its domain is therefore report_internal_inconsistency. Main-article narrative corroborates use for both outcomes but prints no competing coefficient array, so it does not add S_C. C012 independently concerns interval construction.

**Classification ambiguity:** The document roles are clear. The fitted dependent outcome, coding, coefficient meaning and model-output assignment remain insufficiently specified to explain the complete repeated array. Identical rounded outputs from distinct analyses are possible.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.51, eFigure 7 complete panel B and primary-response caption](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51); [physical PDF p.52, eFigure 8 complete panel B and 28-day-mortality caption](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52). Narrative corroboration: [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf — physical PDF p.7, Post Hoc and Subgroup Analyses opening](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7); [physical PDF p.8, interaction continuation](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=8).

**Source evidence:** The captions expressly identify interaction tests for different outcomes. Both panels print every row below:

| Corresponding row | OR | 95% CI | P |
|---|---:|---|---:|
| APACHE II≥25 | .47 | .30–1.62 | .70 |
| APACHE II≥25×precision immunotherapy | 1.85 | .66–5.19 | .24 |
| CCI≥5 | .22 | .09–.53 | .001 |
| CCI≥5×precision immunotherapy | 5.79 | 2.34–15.05 | <.0001 |
| SOFA≥10 | .56 | .27–1.19 | .13 |
| SOFA≥10×precision immunotherapy | 3.08 | 1.37–6.96 | .007 |

**Reported-versus-comparator:** The primary-response array is compared row by row with the 28-day-mortality array, including all points, limits, P values and interaction markers. Their different panel-A event counts confirm distinct endpoints: treatment/placebo APACHE-high counts are 12/38 versus 8/40 for response and 22/38 versus 27/40 for death; CCI-high counts are 20/54 versus 7/76 and 24/54 versus 50/76; SOFA-high counts are 25/67 versus 11/68 and 35/67 versus 48/68. The main narrative associates significant high-CCI/high-SOFA interactions with both primary attainment and decreased 28-day mortality.

**Reasoning procedure:** Confirm both full arrays and the explicit outcome captions; compare corresponding rows and inspect the narrative's attribution. Distinguish direct printed equality from an explanation of how that equality arose. The unresolved question is which outcome model generated each array and which coefficients apply to each named outcome, including whether a model/coding specification explains coincident rounded output.

**Calculation:** All six ORs, 12 confidence endpoints and six P entries match between pages; their precision intervals overlap completely, giving zero numeric copy discrepancy. This is not a beyond-rounding numeric mismatch. No modeled interaction estimate is tested against a crude subgroup OR. The registered observation is the unresolved attribution of the complete repeated array to two separately named analyses with different event arrays.

**Affected result or extracted value:** Outcome assignment of all six panel-B rows, especially the CCI and SOFA interaction coefficients and tests used in the 28-day-mortality narrative.

**Why context does not resolve it:** Route B applies: the comparison concerns estimate/test attribution in focus B/C; immediate captions and narrative assign the array to distinct outcomes without explaining the model mapping; and an extractor must associate these six results with a specific outcome. Neither caption identifies a common dependent outcome or coding convention that reconciles that assignment at once.

**Alternative source-grounded interpretations:** Two distinct outcome analyses could coincidentally yield identical rounded arrays, or model/coding distinctions could explain the equality. A misassigned caption or production-stage duplication is another possible explanation, but no copying mechanism is asserted. Equality alone does not prove that the two analyses cannot coincide. The source model outputs, dependent-variable coding, reference groups, covariates and coefficient meanings needed to select an explanation are not supplied in sufficient detail.

**Mechanical evidence recheck:** Fresh source renders confirmed both complete arrays, both explicit outcome captions, different event arrays and supporting narrative. The reproduced state records those direct observations and their unresolved attribution; it is not a determination that distinct analyses must produce different numbers.

**Potential downstream evidence impact:** If confirmed, an extractor could assign these six coefficients and tests to primary response, 28-day mortality, or both without a documented model mapping. No propagation, conclusion change or judgment about the trial's overall validity follows from this card.

<a id="C014"></a>

## C014 — 90-day APACHE-treatment point lies outside its stated confidence interval

Pending Human Adjudication.

**Candidate statement:** eFigure 9 panel B prints an APACHE II≥25×precision-immunotherapy OR .11 with 95% CI .36–3.42. The point is below the interval's lower limit, including all allowed half-unit readings.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eFigure 9 panel B APACHE-treatment point vs its interval

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-001

**Qualifying route:** Route A, category 1.

**Classification rationale:** The point and its confidence bounds are in one REPORT display. The issue is point containment, so the domain is statistical_results. No PLAN statement or cross-document conflicting result participates.

**Classification ambiguity:** None for document roles, row identity or containment. The source model output needed to identify the intended point/interval pairing is unavailable.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.53, eFigure 9 panel B, APACHE II≥25×precision-immunotherapy row and 90-day-mortality caption](../../../joi250116supp2_prod_1771885794.27755.pdf#page=53).

**Source evidence:** The interaction row prints OR .11, 95% CI .36–3.42, P=.86. It is distinct from the APACHE main-effect row above it. The panel caption identifies 90-day mortality.

**Reported-versus-comparator:** The point .11 is compared with its same-row lower bound .36 and upper bound 3.42. The CI contains 1 and P=.86 is nonsignificant; the registered issue is the point outside the interval, not a separately inferred CI/P disagreement.

**Reasoning procedure:** Confirm row and column alignment from the exact source page, then test containment of the point in its labeled interval. Expand each displayed number by its half-unit precision range. No fitted-model reconstruction or raw data are necessary for this containment comparison. The unresolved question is which point and confidence limits belong to the named interaction row.

**Calculation:** `.11<.36`. The point permits [.105,.115], lower bound [.355,.365], and upper bound [3.415,3.425]. Even the maximum permitted point is below the minimum lower bound, with gap `.355−.115=.240`; relative gap `.240/.11=2.181818182`. No allowed half-unit reading permits containment. Route A category 1 is never removed by the .05 rounding exclusion.

**Affected result or extracted value:** The APACHE II≥25×precision-immunotherapy OR and confidence interval for 90-day mortality.

**Why context does not resolve it:** Route A, category 1 applies directly to a point estimate outside its interval. The immediate row does not identify a different quantity or analysis for either point or limits.

**Alternative source-grounded interpretations:** A digit or decimal substitution, or limits associated with another coefficient, could account for the display. The source does not select an explanation. Neither a geometric center nor a neighboring coefficient is adopted as a replacement point, and no exact underlying model is inferred.

**Mechanical evidence recheck:** The original page was freshly rendered and visually reread. The named interaction label, point, both bounds, P value and outcome caption matched registration. Independent half-unit arithmetic reproduced noncontainment without a source transcription or location change.

**Potential downstream evidence impact:** If confirmed, an extractor could copy this noncontaining point/interval pairing for a 90-day mortality interaction. No actual evidence propagation or conclusion change is established.
