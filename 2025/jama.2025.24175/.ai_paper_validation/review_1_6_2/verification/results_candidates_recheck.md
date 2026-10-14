# Mechanical evidence recheck: results candidates

Scope: C008, C009, C010, C011, C012, C013, C014. All seven stable IDs and every affected location were rechecked separately. All remain Pending Human Adjudication. This artifact records evidence facts and classification; it assigns no adjudication or proposed replacement result.

The complete `QUALITY_CONTROL_SCOPE.md`, `workflow_1_6_2/review_contract.md`, the assigned ledger cards and classification rows, screening groups G08–G14, and corresponding current-run checker facts were read. Printed values were then independently read from fresh renders of exact supplied PDFs. Existing text, screening calculations and checker conclusions were locators, not final authority. No external source or earlier-run scientific conclusion was used.

## Recheck coverage and provenance

Eleven unique source pages were freshly rendered and visually inspected: DOC-003 pp.22,27,29,44,51,52,53; DOC-001 pp.6,7,8; DOC-002 p.70. The extra DOC-003 p.29 confirms the patient-count definition supporting the safety comparisons. No new OCR was needed.

The recorded missing direct rendering capability was handled with the supplied helper and temporary package-local interpreter. Every derivative uses PyMuPDF 1.26.4, 200 dpi, CPU PDF rendering. The tooling record's `GPU_USER_REQUESTED` records the user's GPU OCR request; no GPU OCR engine or OCR derivative was needed here. Sources and reused assets were read without modification.

Command template, run once for every row below:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render "SOURCE.pdf" --page N ".ai_paper_validation/review_1_6_2/preprocessing/recheck_results/OUTPUT.png" --dpi 200
```

| Source | Physical PDF page | Derivative relative to review_1_6_2 | Engine and device |
|---|---:|---|---|
| joi250116supp2_prod_1771885794.27755.pdf | 22 | preprocessing/recheck_results/supp-22.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 27 | preprocessing/recheck_results/supp-27.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 29 | preprocessing/recheck_results/supp-29.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 44 | preprocessing/recheck_results/supp-44.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 51 | preprocessing/recheck_results/supp-51.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 52 | preprocessing/recheck_results/supp-52.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 53 | preprocessing/recheck_results/supp-53.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf | 6 | preprocessing/recheck_results/main-6.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf | 7 | preprocessing/recheck_results/main-7.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf | 8 | preprocessing/recheck_results/main-8.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp1_prod_1771885794.26255.pdf | 70 | preprocessing/recheck_results/plan-70.png | PyMuPDF 1.26.4; CPU; 200 dpi |

Independent arithmetic was performed in JavaScript without Python scientific orchestration. Two-sided Fisher values use the probability-order definition: for treatment sample size n, comparator size m, total events K, and treatment events a, sum `choose(K,x)*choose(n+m-K,n-x)/choose(n+m,n)` over feasible integer x whose probability is no larger than the observed probability at a. Log-factorial evaluations avoid overflow. Floating-point summation within approximately 4×10⁻¹³ of 1 is reported as 1. Every displayed exact count's half-unit interval contains only its displayed integer for an exact contingency calculation.

| ID | Locations found and source/comparator matched | Primary relationship | All relationships | Review domain | Evidence state |
|---|---|---|---|---|---|
| C008 | Yes, all four eTable 10 rows | S_W | S_W | statistical_results | reproduced |
| C009 | Yes, MALS patient risks and NNH1 point/direction | S_W | S_W | statistical_results | reproduced |
| C010 | Yes, both patient-risk pairs, both intervals and test specification | S_W | S_W | statistical_results | reproduced |
| C011 | Yes, five affected rows and all 13 companion rows | S_W | S_W | statistical_results | reproduced |
| C012 | Yes, both APACHE rows and all five companion rows in each panel | S_W | S_W | statistical_results | reproduced |
| C013 | Yes, both complete six-row arrays, outcome captions and narrative use | S_W | S_W | report_internal_inconsistency | reproduced |
| C014 | Yes, named point, both limits, P value and outcome caption | S_W | S_W | statistical_results | reproduced |

All role, primary relationship, all-relationship and review-domain assignments are confirmed; zero classification changes. DOC-003 and DOC-001 contain reported trial results and are REPORT by content. DOC-002 p.70 is prospective SAP material and is PLAN by content. Corroboration from another document is identified below and is not counted as an additional conflicting relationship.

## C008 — Source-printed unadjusted day-15 immunoparalysis OR

**Status:** Pending Human Adjudication

**Location found:** Yes. [DOC-003 p.22, eTable 10](../../../joi250116supp2_prod_1771885794.27755.pdf#page=22), final row for the day-15 mean-SOFA responder endpoint in sepsis-induced immunoparalysis, plus all three companion unadjusted-OR rows in the same table. The fresh source render confirms the table title, response window, column alignment and explicit unadjusted label.

**Source printed value/text matched:** Yes. Precision immunotherapy 40/106 (37.7%), placebo 29/122 (23.8%); difference 13.9 (1.9–25.6); unadjusted OR **1.194** (1.09–3.45); P=.030. The point is visibly 1.194, not 1.94.

**Comparator matched:** Yes. The other three rows show 12/25 versus 4/23 with OR 4.38, 34/106 versus 22/122 with OR 2.15, and 12/25 versus 5/23 with OR 3.32.

**Consistency rule applicable:** Yes. The source explicitly labels the point unadjusted. The count-based binary odds-ratio method reproduces all three companion points, supporting Route A category 4. This comparison does not require equating a model-based estimate with a crude ratio.

**Calculation reproduced and display precision:** `40×(122−29)/[(106−40)×29] = 1.943573668`. Companion points independently reproduce as 4.384615385, 2.146464646 and 3.323076923. Allowing all four displayed count inputs their half-unit intervals gives OR range `[39.5×92/(67×29.5), 40.5×94/(65×28.5)] = [1.838603592,2.055060729]`. The printed point interval is [1.1935,1.1945]. The minimum gap is 0.644103592 and relative discrepancy is 0.644103592/1.194 = **0.539450245**, above 0.05. Allowing continuous half-unit count values is conservative; requiring exact integers would narrow the recomputed range. The geometric center of its displayed CI is approximately 1.93920, additional corroboration rather than a substitute result.

**Necessary inputs available:** Yes for the registered point comparison: all four cell-count inputs, comparator rows and the unadjusted label. **Exact missing inputs or definitions:** an alternative unadjusted computation or different underlying analysis population that could associate 1.194 with this row is not identified. These are unnecessary to reproduce the count-supported discrepancy but necessary to explain its origin.

**Source-grounded alternative interpretation:** The point could refer to an unprinted population or another computation. The display supplies neither distinction; no such interpretation is adopted. Neighboring counts and CI may help a reader reconstruct a plausible intended value, but the recheck does not replace the printed point.

**Direct observation versus inferred explanation:** Direct observation is the source-printed 1.194 under an unadjusted-OR label and its failure to reproduce by the method reproducing the other rows. A digit substitution, publication transcription or different analysis is an inferred possible mechanism only.

**Classification confirmed:** Every conflicting location is REPORT within DOC-003. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. No PLAN statement is needed or in conflict. Classification ambiguity: no alternative method/population is identified, but document roles are clear.

**Evidence state:** **reproduced**. Determining fact: exact source visual confirms 1.194, and the conservative recomputation remains separated by relative discrepancy 0.539450245. No registered source value or source location needed transcription correction.

**Exact remaining human question:** Which unadjusted odds ratio and analysis inputs belong to the day-15 immunoparalysis response comparison, and how does 1.194 reconcile with 40/106 versus 29/122 and the neighboring rows' count-reproducing method?

## C009 — MALS NNH1 harm/benefit direction

**Status:** Pending Human Adjudication

**Locations found:** Yes. [DOC-003 p.27, eTable 13 Any SAE row](../../../joi250116supp2_prod_1771885794.27755.pdf#page=27); [p.44, eTable 15 MALS NNH1 row and harm-induction label](../../../joi250116supp2_prod_1771885794.27755.pdf#page=44). Supplemental definition checked at [p.29, eTable 13 footnote a](../../../joi250116supp2_prod_1771885794.27755.pdf#page=29): the flagged data represent numbers of patients; other subrows represent event numbers. The Any SAE row on p.27 carries that footnote marker.

**Source printed value/text matched:** Yes. MALS NNH1 is **8.8**, 95% CI 3.2–10.0, explicitly labeled number of patients needed to treat to **induce at least 1 serious TEAE**. Abbreviations define NNH as number needed to harm.

**Comparator matched:** Yes. MALS anakinra N=25, Any SAE 20 (80.0%); MALS placebo N=23, Any SAE 21 (91.3%). The patient-count footnote supports treating these as risks of at least one event.

**Consistency rule applicable:** Yes. Under treatment-minus-placebo direction, inducing an additional serious event requires a positive risk increase. The observed treatment risk is smaller. The reported magnitude alone is close to the unsigned reciprocal, but the harm-induction label associates that magnitude with the opposite direction. This is the registered Route A category 2 direction/reference-group comparison.

**Calculation reproduced and display precision:** RD=`20/25−21/23 = −0.113043478`; signed reciprocal=`−8.846153846`. Conservative independent half-unit count/denominator intervals give RD lower `19.5/25.5−21.5/22.5 = −0.190849673` and upper `20.5/24.5−20.5/23.5 = −0.035605732`. The signed reciprocal interval is [−28.085365854,−5.239726027], disjoint from the printed point's [8.75,8.85]. Minimum signed gap is 13.989726027 and relative discrepancy is **1.589741594**, above 0.05. Printed risk intervals [79.95,80.05]% and [91.25,91.35]% likewise preserve a negative treatment-minus-placebo difference, [−11.40,−11.20] percentage points. This candidate concerns direction, not rounding of the unsigned magnitude.

**Necessary inputs available:** Yes: affected patient counts, group denominators, patient-count definition, point and explicit induce-harm wording. **Exact missing inputs or definitions:** the table's treatment/reference-group sign convention and whether absolute reciprocals are used for benefit and harm alike are not supplied.

**Source-grounded alternative interpretation:** An unsigned reciprocal convention or a reversed comparator could generate positive 8.8. The label does not explain such a convention or distinguish prevention from induction for this row. The alternative is recorded without assuming the direction the authors intended.

**Direct observation versus inferred explanation:** Direct facts are fewer patients with any SAE under anakinra and the positive point under an induce-harm label. An unsigned calculation or switched reference group is an inferred explanation, not a source-printed method.

**Classification confirmed:** Both conflicting table locations are REPORT in DOC-003; p.29 is REPORT corroboration of the input definition. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. No role or relationship ambiguity alters these fields.

**Evidence state:** **reproduced**. Determining fact: the exact printed patient risks retain the opposite treatment-minus-placebo direction from the positive harm-induction reading, including conservative half-unit ranges.

**Exact remaining human question:** Does MALS 8.8 represent the number needed to prevent or to induce a serious TEAE, and what treatment/reference-group and sign convention define it?

## C010 — NNH1 confidence intervals versus source-specified safety tests

**Status:** Pending Human Adjudication

**Locations found:** Yes. Conflicting REPORT results are [DOC-003 p.27, eTable 13 MALS and immunoparalysis Any SAE patient rows](../../../joi250116supp2_prod_1771885794.27755.pdf#page=27) and [p.44, eTable 15 corresponding NNH1 intervals](../../../joi250116supp2_prod_1771885794.27755.pdf#page=44). The [p.29 footnote a](../../../joi250116supp2_prod_1771885794.27755.pdf#page=29) confirms patient counts. Methodological corroboration is [DOC-001 p.6, significance and all-analyses-follow-SAP statements](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6) and [DOC-002 p.70, Safety and two-sided significance rule](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70).

**Source printed value/text matched:** Yes. MALS NNH1 8.8 with 95% CI **3.2–10.0**; immunoparalysis NNH1 47.6 with 95% CI **9.9–55.8**. Both are finite positive intervals labeled 95% CIs for the number needed to induce at least one serious TEAE.

**Comparator matched:** Yes. MALS 20/25 versus 21/23; immunoparalysis 96/106 versus 108/122. DOC-002 p.70 explicitly specifies Fisher's exact comparison of serious/nonserious TEAE incidence between treatments in each immune stratum, with two-sided .05 significance. DOC-001 p.6 states P<.05 and that analyses followed the SAP. No safety P value for these two rows is printed at the compared table locations; the values below are independently recomputed under the supplied test, not transcribed publication P values.

**Consistency rule applicable:** Yes, as an interval-versus-specified-test comparison (Route A category 1). A conventional confidence set for the reciprocal of the same risk difference must accommodate the no-effect/infinite-number limit when its corresponding comparison is nonsignificant. The printed finite positive intervals omit that limit. The source permits comparison to a named safety test, while the missing interval procedure remains the precise human question.

**Calculation reproduced and display precision:** Independent probability-order two-sided Fisher summation gives **P=.419120073** for MALS and **P=.669907887** for immunoparalysis, both above .05. Positive finite NNH intervals imply reciprocal risk-difference intervals [1/10.0,1/3.2]=[.100000,.312500] and [1/55.8,1/9.9]=[.017921,.101010], neither containing zero. Exact-integer half-unit count ranges cannot change the contingency tables. Even granting each printed bound its .05 half-unit uncertainty, all limits remain finite and positive: MALS [3.15,3.25] and [9.95,10.05]; immunoparalysis [9.85,9.95] and [55.75,55.85]. Thus no display rounding reaches the no-effect limit. Category 1 is not subject to the relative-discrepancy .05 exclusion. C009 separately records the MALS direction comparison, which uses a different rule.

**Necessary inputs available:** Yes for this bounded recheck: patient counts, denominators, named safety test, two-sided significance level and confidence level. **Exact missing inputs or definitions:** the NNH confidence procedure, whether the bounds are an ordinary connected interval or shorthand for a split confidence set, whether they use signed or absolute risk differences, and whether their analysis population differs from the Any SAE rows. The precise interval computation cannot be reconstructed from the supplied text.

**Source-grounded alternative interpretation:** The intervals could arise from a different analysis/population or could abbreviate a split confidence set crossing the reciprocal singularity. A confidence interval procedure and the Fisher test could also be nonmatching procedures. None of those interpretations is specified in the supplied display; each remains an alternative rather than removal of the registered interval/test comparison.

**Direct observation versus inferred explanation:** Direct source facts are finite positive 95% bounds, patient counts and the safety test specification. The nonsignificant P values are independently reproduced calculations from those inputs. No source-printed P value, undocumented confidence construction or computational mechanism is asserted.

**Classification confirmed:** The conflicting numerical locations are both REPORT in DOC-003. DOC-001 p.6 is REPORT methods corroboration; DOC-002 p.70 is PLAN methods corroboration by prospective content. Neither corroborating location states a competing result. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. The SAP does not create P_R, and main-article method corroboration does not create S_C. Classification ambiguity: the relation of the interval procedure to the specified test is undefined, as recorded in the human question.

**Evidence state:** **reproduced**. Determining fact: the exact finite positive NNH1 confidence bounds exclude the no-effect limit while independent application of the supplied safety test to the corresponding exact patient counts is nonsignificant in both strata. This evidence state does not decide which interval/test interpretation applies.

**Exact remaining human question:** Which patient-risk comparison, sign convention and confidence transformation produced these two NNH1 intervals, and how do the reported finite bounds relate to the nonsignificant Fisher safety comparisons or to a split confidence set?

## C011 — Five panel-A P values under the companion-row reproducing test

**Status:** Pending Human Adjudication

**Locations found:** Yes. [DOC-003 p.51, eFigure 7 panel A](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51), all APACHE II, CCI and SOFA rows; [p.52, eFigure 8 panel A](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52), all corresponding rows; [p.53, eFigure 9 panel A](../../../joi250116supp2_prod_1771885794.27755.pdf#page=53), all corresponding rows. Corroborating methods at [DOC-001 p.6](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6) name Fisher's exact comparisons. All five affected rows and all 13 companion rows were visually read from their original page renders.

**Source printed value/text matched:** Yes. The five affected rows have P=.439, .003 and .035 for primary-response APACHE II≥25, CCI≥5 and SOFA≥10 respectively; P=.045 for day-28 SOFA≥10; P=.209 for day-90 SOFA≥10.

**Comparator matched:** Yes. The table below transcribes every integer event/denominator pair with treatment first; the source plots display placebo first. Panel captions identify primary attainment, 28-day mortality and 90-day mortality respectively. Switching column order does not change a two-sided Fisher test.

**Consistency rule applicable:** Yes. The same probability-order two-sided Fisher calculation reproduces 13 of 18 rows under the workflow display rule, with companion support in each display. The five other printed P values fail that reproducing method beyond .05 relative discrepancy. Route A category 4 applies. This comparison does not reinterpret panel-B model/interaction tests as Fisher tests.

**Calculation reproduced and display precision:** All 18 independent calculations are recorded below. For each numeric printed P with three decimals, the printed half-unit interval is P±.0005. Each exact input count's half-unit interval contains only the displayed integer for an exact contingency table. The recomputed P interval is consequently the singleton result of that table. Gap is the distance from that value to the printed half-unit interval; relative gap divides by the printed P.

| Page/outcome | Row | Treatment events/total | Placebo events/total | Printed P | Recomputed Fisher P | Minimum gap | Relative gap |
|---|---|---|---|---:|---:|---:|---:|
| 51 primary | APACHE II≥25 | 12/38 | 8/40 | .439 | .303200218 | .135299782 | .308199958 |
| 51 primary | APACHE II<25 | 34/93 | 18/105 | .002 | .002176542 | 0 | 0 |
| 51 primary | CCI≥5 | 20/54 | 7/76 | .003 | .000158910 | .002341090 | .780363217 |
| 51 primary | CCI<5 | 26/77 | 19/69 | .475 | .474644233 | 0 | 0 |
| 51 primary | SOFA≥10 | 25/67 | 11/68 | .035 | .006531327 | .027968673 | .799104929 |
| 51 primary | SOFA<10 | 21/64 | 15/77 | .083 | .082691021 | 0 | 0 |
| 52 day 28 | APACHE II≥25 | 22/38 | 27/40 | .489 | .483109060 | .005390940 | .011024416 |
| 52 day 28 | APACHE II<25 | 35/93 | 45/105 | .472 | .471707802 | 0 | 0 |
| 52 day 28 | CCI≥5 | 24/54 | 50/76 | .020 | .019643739 | 0 | 0 |
| 52 day 28 | CCI<5 | 33/77 | 22/69 | .231 | .231037136 | 0 | 0 |
| 52 day 28 | SOFA≥10 | 35/67 | 48/68 | .045 | .034400792 | .010099208 | .224426837 |
| 52 day 28 | SOFA<10 | 22/64 | 24/77 | .721 | .720788007 | 0 | 0 |
| 53 day 90 | APACHE II≥25 | 31/38 | 32/40 | >.99 | 1.000000000 | 0 | Not applicable; inequality satisfied |
| 53 day 90 | APACHE II<25 | 59/93 | 66/105 | >.99 | 1.000000000 | 0 | Not applicable; inequality satisfied |
| 53 day 90 | CCI≥5 | 39/54 | 64/76 | .123 | .125049970 | .001549970 | .012601380 |
| 53 day 90 | CCI<5 | 51/77 | 34/69 | .045 | .044623206 | 0 | 0 |
| 53 day 90 | SOFA≥10 | 49/67 | 57/68 | .209 | .146989715 | .061510285 | .294307583 |
| 53 day 90 | SOFA<10 | 41/64 | 41/77 | .231 | .231336669 | 0 | 0 |

The five affected printed intervals are [.4385,.4395], [.0025,.0035], [.0345,.0355], [.0445,.0455] and [.2085,.2095]. Each affected relative gap exceeds .05. Two companion rows have nonzero gaps, but their relative gaps .011024416 and .012601380 are below .05 and therefore support reproduction under the stipulated display rule.

**Necessary inputs available:** Yes: all 18 integer contingency tables, their printed P values, outcome/stratum labels, and companion evidence for the reproducing test. **Exact missing inputs or definitions:** any row-specific alternative test, contingency population, sidedness or adjustment that explains the five affected P values is not printed. No patient data are necessary for the exact-table calculation; unprinted row-specific differences cannot be determined.

**Source-grounded alternative interpretation:** A distinct test or population may have generated the five P values. The immediate displays do not label a different row-specific procedure, and the other rows reproduce under the stated calculation. This alternative remains the human question, not an assumed mechanism.

**Direct observation versus inferred explanation:** Direct facts are the counts and P values in all three panels. Fisher values and gap calculations are independent reproductions. The identity of any alternative test or source of the discrepancy is inferred only as a possibility. Exact forest-plot interval endpoints are not inferred from pixels.

**Classification confirmed:** All conflicts are within the REPORT results supplement DOC-003. REPORT main-article p.6 supplies method corroboration, not a contradictory cross-document result. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. No classification change or additional S_C relation is warranted.

**Evidence state:** **reproduced**. Determining fact: all five printed values and contingency inputs are confirmed at their exact source locations, the same method reproduces the 13 other rows under the display rule, and each affected relative gap exceeds .05.

**Exact remaining human question:** Which test and contingency counts produced each of the five affected panel-A P values, and what row-specific distinction explains their separation from the Fisher calculation that reproduces the companion rows?

## C012 — Repeated APACHE coefficient versus companion-row interval construction

**Status:** Pending Human Adjudication

**Locations found:** Yes. [DOC-003 p.51, eFigure 7 panel B APACHE II≥25 main-effect row and all five companion rows](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51); [p.52, eFigure 8 panel B corresponding row and all five companion rows](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52). Both complete panels were visually checked.

**Source printed value/text matched:** Yes, both pages print APACHE II≥25 OR **.47**, 95% CI **.30–1.62**, P=**.70**. This is the main-effect row, distinct from the APACHE-treatment row beneath it.

**Comparator matched:** Yes, all five other rows have identical points and limits on both pages, as transcribed in the calculation table. The source labels all bounds 95% CIs for ORs.

**Consistency rule applicable:** Yes. A log-symmetric ratio interval has geometric center `sqrt(lower×upper)`. The method reproduces all five other rows in each panel under the workflow half-unit/.05 rule, but not the APACHE main-effect row. This supplies the same-display method support required for Route A category 4. No approximation of a P-value test is used as the basis of this candidate; the source-printed .70 is recorded without claiming an independent Wald-test contradiction.

**Calculation reproduced and display precision:** APACHE center `sqrt(.30×1.62)=.697137002`. The endpoint ranges [.295,.305] and [1.615,1.625] imply geometric-center range [.690235467,.704006392]. The source point range [.465,.475] is separated by gap .215235467; relative discrepancy **.457947802**, above .05. Every companion point has two decimals, so its interval is point±.005; the endpoints likewise use ±.005.

| Row, on both pages | Printed OR (95% CI) | Geometric center | Center range from rounded limits | Minimum gap to printed-point range | Relative gap |
|---|---|---:|---|---:|---:|
| APACHE II≥25 | .47 (.30–1.62) | .697137002 | [.690235467,.704006392] | .215235467 | .457947802 |
| APACHE II≥25×precision immunotherapy | 1.85 (.66–5.19) | 1.850783618 | [1.842871401,1.858675604] | 0 | 0 |
| CCI≥5 | .22 (.09–.53) | .218403297 | [.211246302,.225444006] | 0 | 0 |
| CCI≥5×precision immunotherapy | 5.79 (2.34–15.05) | 5.934391291 | [5.927062932,5.941714820] | .132062932 | .022808797 |
| SOFA≥10 | .56 (.27–1.19) | .566833309 | [.560379336,.573258232] | 0 | 0 |
| SOFA≥10×precision immunotherapy | 3.08 (1.37–6.96) | 3.087911916 | [3.081164553,3.094652646] | 0 | 0 |

The CCI-treatment companion has a nonzero gap, but .022808797 is within .05 and therefore reproduces under the stipulated rule. This is not a claim that every companion interval is exactly log-symmetric to all printed digits. The independent arithmetic slightly refines approximate companion centers in the registration text (1.85046, 5.93456 and 3.08799); no source reading was changed and the method-support conclusion is unchanged.

**Necessary inputs available:** Yes for the same-display construction comparison: the point and both limits of every row, precision and interval labels. **Exact missing inputs or definitions:** the exact interval-construction procedure, coefficient standard errors/covariance and whether this APACHE row alone uses a non-log-symmetric method are not printed. A P-value test definition is not needed to establish the registered geometric-center comparison.

**Source-grounded alternative interpretation:** A non-log-symmetric interval procedure could apply to this row, or its point and bounds could come from different coefficients/analyses. The page does not identify such a row-specific distinction. The missing method remains the human question; no preferred procedure or replacement point is proposed.

**Direct observation versus inferred explanation:** Direct observations are repeated .47 (.30–1.62), .70 and the ten companion rows. Geometric-center/gap values are independent arithmetic. A substituted value, mixed row or different interval method is an inferred possible explanation only. Repetition under different outcome captions is separately recorded as C013 and is not the rule establishing C012.

**Classification confirmed:** Both conflicting rows and all method-support comparators are REPORT in DOC-003. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. No PLAN comparison or cross-document result conflict participates. Classification ambiguity: the exact confidence procedure remains unspecified.

**Evidence state:** **reproduced**. Determining fact: both exact source rows match and fail the geometric construction beyond .05 relative discrepancy while all five companion rows in each panel reproduce under the same display rule. Companion arithmetic refinement is not a source-transcription correction.

**Exact remaining human question:** Which coefficient and interval-construction procedure produced .47 (.30–1.62) in each APACHE II≥25 main-effect row, and does a documented row-specific interval procedure explain its separation from the companion-row construction?

## C013 — Six-row output attributed to two different outcomes

**Status:** Pending Human Adjudication

**Locations found:** Yes. [DOC-003 p.51, complete eFigure 7 panel B and caption](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51), and [p.52, complete eFigure 8 panel B and caption](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52). Also found and reread: [DOC-001 p.7, Post Hoc and Subgroup Analyses opening](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7) and [p.8, interaction-narrative continuation](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=8).

**Source printed value/text matched:** Yes. eFigure 7 is titled attainment of the primary endpoint according to baseline severity; its panel-B caption explicitly assigns interaction tests to the primary endpoint. eFigure 8 is titled 28-day mortality according to baseline severity; its panel-B caption explicitly assigns interaction tests to 28-day mortality. The six OR/CI/P rows are identical at displayed precision.

**Comparator matched:** Yes, the entire corresponding output array was compared row by row, including interaction markers and P-value inequality:

| Corresponding row in both panels | OR | 95% CI | P |
|---|---:|---|---:|
| APACHE II≥25 | .47 | .30–1.62 | .70 |
| APACHE II≥25×precision immunotherapy | 1.85 | .66–5.19 | .24 |
| CCI≥5 | .22 | .09–.53 | .001 |
| CCI≥5×precision immunotherapy | 5.79 | 2.34–15.05 | <.0001 |
| SOFA≥10 | .56 | .27–1.19 | .13 |
| SOFA≥10×precision immunotherapy | 3.08 | 1.37–6.96 | .007 |

Panel-A events differ between the outcomes: treatment/placebo APACHE-high 12/38 versus 8/40 for response and 22/38 versus 27/40 for death; CCI-high 20/54 versus 7/76 and 24/54 versus 50/76; SOFA-high 25/67 versus 11/68 and 35/67 versus 48/68. DOC-001 p.8 attributes significant high-CCI/high-SOFA interactions to primary attainment with eFigure 7 and to decreased 28-day mortality with eFigure 8. The p.7 opening merely begins that narrative; neither main-article page prints a separate conflicting six-row coefficient array.

**Consistency rule applicable:** Yes, the registered rule is result-to-outcome attribution under Route B, focus B/C. The same complete printed output is assigned to distinct outcomes, and the package does not distinguish the model/coding that would identify which coefficient belongs to each outcome. The affected extraction is the six-row model output, particularly the CCI and SOFA interaction coefficients and tests supporting the 28-day mortality narrative. This is a bounded attribution question; equality of rounded outputs alone does not prove that two analyses cannot coincide.

**Logical comparison reproduced and display precision:** All six rows, all 18 point/limit values and all six P entries match between pages. Their half-unit intervals overlap completely, so the numeric copy discrepancy is zero. The registered inconsistency is the unresolved attribution of that whole array to two separately named outcome analyses; it is not a claim of a beyond-rounding numeric difference. No calculation comparing modeled interactions with crude subgroup odds ratios is used. The different source-printed event counts independently confirm that the captions refer to distinct endpoints.

**Necessary inputs available:** Yes to reproduce the repeated array, distinct outcome captions, different event arrays and narrative use. **Exact missing inputs or definitions:** the dependent outcome and its coding for each fitted model, model structure/covariates, reference groups, coefficient meanings and source model outputs are not provided in sufficient detail to explain the exact repeated array. Those details are necessary to determine which output should be extracted for each outcome, not to observe the repeated array.

**Source-grounded alternative interpretation:** Two distinct outcome analyses could coincidentally yield identical rounded output, or coding/model distinctions could lead to the displayed equality. Their existence is possible, but no supplied statement identifies one. No copying mechanism is asserted, and no modeled-versus-crude contradiction is alleged.

**Direct observation versus inferred explanation:** Direct observation is six identical displayed OR/CI/P rows under primary-response and 28-day-death captions and narrative use for both outcomes. Unclear coefficient-to-outcome mapping is the bounded consequence recorded for human review. A duplicated production step, misassigned caption, or coincident output is an inferred possible explanation only.

**Classification confirmed:** The conflicting outcome attribution is within DOC-003 REPORT content. DOC-001 pp.7–8 are REPORT narrative corroboration, without a directly conflicting coefficient array. Primary relationship **S_W**; all relationships **S_W**; review domain **report_internal_inconsistency**, because the issue concerns which outcome the numeric array belongs to. C012 separately handles interval construction. No S_C is added for narrative corroboration and no PLAN relationship exists. Classification ambiguity: exact model/output assignment remains unspecified, not the document roles.

**Evidence state:** **reproduced**. Determining fact: direct-source comparison confirms the entire identical array, the distinct explicit outcome labels and unresolved output attribution in immediate context. This state records that observation, not a determination that the analyses must have different numerical outputs.

**Exact remaining human question:** Which outcome model generated each panel-B array, and which coefficients, intervals and tests apply to primary response and to 28-day mortality for each of the six displayed rows? If distinct analyses yielded the same rounded array, what source specification identifies their outcome coding and model mapping?

## C014 — 90-day APACHE-treatment point outside its interval

**Status:** Pending Human Adjudication

**Location found:** Yes. [DOC-003 p.53, eFigure 9 panel B APACHE II≥25×precision immunotherapy row](../../../joi250116supp2_prod_1771885794.27755.pdf#page=53). The same page's panel-B caption explicitly identifies 90-day mortality. The interaction row was distinguished from the APACHE main-effect row above it.

**Source printed value/text matched:** Yes. OR **.11**, 95% CI **.36–3.42**, P=**.86**.

**Comparator matched:** Yes. The row's lower .36 and upper 3.42 are printed in the 95% CI column on the same line; .86 is printed in its P-value column. The source row label and outcome caption match the registration.

**Consistency rule applicable:** Yes. An estimate must be contained in its stated interval. Point .11 is below lower bound .36. This is Route A category 1; no exact fitted model, confidence construction or raw data are required to check containment.

**Calculation reproduced and display precision:** `.11 < .36`. Point half-unit interval [.105,.115], lower-bound interval [.355,.365], upper-bound interval [3.415,3.425]. Even the greatest allowed point is below the least allowed lower bound: minimum gap `.355−.115=.240`; relative gap `.240/.11=2.181818182`. No half-unit reading permits containment. Route A category 1 is never removed by the .05 display rule. The printed CI contains 1 and P>.05; the registered issue is point containment, not a separately inferred interval/P disagreement.

**Necessary inputs available:** Yes: point, both limits, row label, confidence level and outcome. **Exact missing inputs or definitions:** the underlying coefficient/model output that identifies whether the point or limits belong to a different quantity is not supplied. That input is unnecessary for containment reproduction but needed to identify the intended row output.

**Source-grounded alternative interpretation:** A digit/decimal substitution or an interval assigned from another coefficient could account for the reading. The source does not select an explanation; a geometric center or neighboring result is not adopted as a replacement point.

**Direct observation versus inferred explanation:** Direct observation is the printed .11 and .36–3.42 on the named interaction row. Noncontainment is direct arithmetic. A publication-production mechanism or intended alternative value is an inference only.

**Classification confirmed:** Point and comparator limits are REPORT in the same DOC-003 display. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. No classification change, PLAN comparison or cross-document discrepancy is involved.

**Evidence state:** **reproduced**. Determining fact: exact source point and limits match, and their half-unit intervals cannot satisfy containment.

**Exact remaining human question:** Which odds ratio and 95% confidence limits belong to the APACHE II≥25×precision-immunotherapy row for 90-day mortality, and what source output identifies that point/interval pairing?

## Bounded remaining inputs

Seven IDs covered, seven evidence states `reproduced`, zero `reproduced_after_transcription_correction`, zero `not_reproduced`, zero classification changes. Every registered affected source location is found; the definition-support location DOC-003 p.29 was additionally inspected. No unreadable page or OCR limitation remains in this shard. Remaining inputs are the exact unadjusted computation/population for C008, direction convention for C009, NNH confidence construction and test mapping for C010, row-specific tests/counts for C011, interval procedure for C012, outcome-model attribution for C013, and underlying point/interval pairing for C014. These bound the explanatory human questions; they do not authorize changing or deleting IDs.
