# Mechanical Evidence Recheck — Workflow 1.6.2

Pending Human Adjudication. Fresh stage agent `/root/evidence_rechecker`, model `gpt-6.1-sol`, reasoning effort `high`. Assigned scope: C001, C002, C003, C004, C005, C006, C007, C008, including every registered occurrence and repeated-pattern entry. These evidence states record reproduction facts, not human dispositions. No stable ID was removed, and the ledger was not edited by this agent.

The direct supplied PDFs were independently reread with Poppler `pdftotext -layout -f N -l N SOURCE -`, and source-matched current-run renders were visually inspected for the numbers, zero endpoint, code lists, matching sentence and font-dependent diagnosis condition. Tool engine: Poppler 26.01.0; compute device: CPU, as recorded in `tooling_record.md`. No OCR, GPU, fallback environment, external source, or Python extraction was used. No new derivatives were needed. Existing source-matched inspection aids were `screening/confirmation/screener-main-p007.png`, `screener-results-p002.png`, `screener-results-p012.png`, `screener-results-p020.png`, `screener-plan-p003.png`, and `screener-plan-p004.png`; the source PDF links below remain the evidence authority. Direct extraction covered main PDF pp1–4, 6–9, results supplement pp2, 7, 9, 12, 19–20, and original protocol/amendment pp3–7. SHA-256 of all three direct sources agrees with `source_hashes_before.sha256`.

Document roles follow content. Main article and results supplement are REPORT: completed observational analyses and operational descriptions of those analyses. The January 6, 2019 protocol and August 2, 2019 amendment are PLAN: prospective specifications and a disclosed amended plan. A corroborating occurrence is not a conflicting relationship. All source links are relative to this `verification/` directory and end in truthful PDF page anchors.

| ID | Review domain | Relationship type | All relationships | Evidence state | Classification change |
|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | reproduced | None |
| C002 | statistical_results | S_W | S_W | reproduced | None |
| C003 | statistical_results | S_W | S_W | reproduced | None |
| C004 | protocol_report | P_R | P_R | reproduced | None |
| C005 | protocol_report | P_R | P_R | reproduced | None |
| C006 | protocol_report | P_R | P_R | reproduced | None |
| C007 | statistical_results | S_W | S_W | reproduced | None |
| C008 | statistical_results | S_W | S_W | reproduced | None |

## C001 — Primary matching allocation

**Location found:** Yes, every assigned location listed below was independently found.

| Exact location and role | Source value/text matched | Comparator or contextual fact matched |
|---|---|---|
| [PLAN original protocol p3, Matching Process](../../../joi190103supp2_prod.pdf#page=3) | Each nonsurgical patient will be propensity-score matched to five surgical patients | Explicit exposure-group orientation is surgical:nonsurgical 5:1 |
| [PLAN protocol p6, Sensitivity analyses](../../../joi190103supp2_prod.pdf#page=6) | Ratios 1:1, 1:5, 1:10; reported results from one dataset using 1:5 | This sentence omits group orientation and does not expressly revise p3 |
| [PLAN amendment p7](../../../joi190103supp2_prod.pdf#page=7) | Adds adverse-event/nutritional and E-value work | No revised matching allocation found in its complete content |
| [REPORT main abstract p1](../../../jama_aminian_2019_oi_190103.pdf#page=1) | 2287 surgical patients matched 1:5 to nonsurgical patients; 11435 controls | Reported cohort orientation is surgical:nonsurgical 1:5 |
| [REPORT main Figure 1 and caption p3](../../../jama_aminian_2019_oi_190103.pdf#page=3) | 2287 surgery and 11435 matched controls; each surgical patient matched to 5 nonsurgical patients | Caption and flow agree with the abstract |
| [REPORT main statistical methods and results p4](../../../jama_aminian_2019_oi_190103.pdf#page=4) | Each surgical patient matched by nearest neighbor to 5 nonsurgical patients; total 13722 | Same performed orientation and population; primary HR 0.61 (0.55–0.69) |

**Source value/text matched:** Yes, the explicit p3 PLAN sentence was checked in source text and its page render, including both group names and five (5).

**Comparator matched:** Yes, the REPORT statements and patient counts match the registration at all three occurrences.

**Consistency rule applicable:** Hold the primary matching design and group identities fixed; five surgical per nonsurgical and five nonsurgical per surgical describe inverse allocations. Focus D, Route B: primary matching specification is in focus; knowing the performed allocation leaves the intended original plan unresolved; it bears on the matched population behind primary HR 0.61.

**Calculation or logical comparison reproduced:** 11435/2287 = 5 exactly; 2287 + 11435 = 13722. The observed report uses surgical:nonsurgical 1:5, whereas the explicit original sentence uses 5:1.

**Display-precision interval check:** Counts are exact integers, not rounded estimates, and the five-per-patient specification is categorical. No half-unit rounding allowance or relative-gap threshold can reverse group orientation. The comparison does not equate an adjusted estimate with a crude ratio.

**Necessary inputs available:** Yes for the printed design comparison: group identities, oriented sentences, counts, plan sensitivity statement and amendment content.

**Exact missing inputs or definitions:** A dated statement of intended original group orientation, any matching amendment, and the implementation specification reconciling the p3 wording with the completed cohort.

**Source-grounded alternative interpretation:** PLAN p6's 1:5 sensitivity shorthand may reflect the same intended allocation as the REPORT, and p3 may have transposed group orientation in prose. Alternatively, performed allocation may differ from the explicit p3 allocation. The supplied documents do not establish which explanation applies.

**Direct observation versus inferred explanation:** Observed: the group names in the two oriented rules are reversed and the counts support the report. Inferred only: any prose-production mechanism or implementation change. Neither is asserted.

**Exact remaining human question:** Which surgical:nonsurgical allocation was intended for the primary January 6 protocol analysis, and how is the p3 matching sentence reconciled with the reported 2287:11435 cohort?

**Compared document roles:** PLAN original protocol p3 and p6/amendment p7; REPORT main abstract p1, Figure 1/caption p3, statistical methods/results p4, all confirmed by content.

**Relationship type:** P_R

**All relationships:** P_R

**Review domain:** protocol_report

**Classification rationale:** The conflicting oriented specifications are PLAN versus REPORT. PLAN p6 has no independently defined inverse direction, so it does not establish a separate P_P relationship. Repeated REPORT statements agree; no S_W or S_C conflict is added. Precedence selects P_R. No classification correction is needed.

**Classification ambiguity:** Intended plan orientation remains unresolved; document roles and relationship are unambiguous.

**Evidence state:** reproduced

**Determining recheck fact:** The direct original sentence specifies five surgical patients per nonsurgical patient, and the direct report specifies five nonsurgical patients per surgical patient.

## C002 — Five absolute 8-year risk differences

**Location found:** Yes, all five affected Table 2 rows, the three reproducing comparison rows, footnote a and methods were found; the five year-8 risk copies in eTable 5 were also found.

**Source value/text matched:** Yes. Main [REPORT Table 2 p7](../../../jama_aminian_2019_oi_190103.pdf#page=7) labels surgery/control cumulative incidences at 8 years and absolute 8-year risk differences. Footnote a states control minus surgery and 95% bootstrap CIs from 1000 samples. [REPORT methods p4](../../../jama_aminian_2019_oi_190103.pdf#page=4) identifies Kaplan–Meier risk estimates and percentile bootstrap confidence intervals.

**Comparator matched:** Yes, every surgery/control pair below matches both Table 2 and the corresponding year-8 entries in [REPORT eTable 5 p7](../../../joi190103supp1_prod.pdf#page=7). That supplement corroborates the risk inputs and does not create a second conflicting relationship.

**Consistency rule applicable:** Subtract displayed surgery risk from displayed control risk, as the footnote defines. This method reproduces three other rows of the same display. Route A category 4 applies to the five printed point results exceeding display allowance. No adjusted HR is compared with a crude risk calculation; no risk-difference CI is reconstructed from marginal risk CIs.

**Calculation or logical comparison reproduced:** Independently reproduced for every affected row. Each one-decimal risk input has half-unit allowance ±0.05 percentage points, so the subtraction interval is the printed subtraction ±0.10. Each printed one-decimal ARD has allowance ±0.05. The remaining interval gap divided by the printed ARD is the relative discrepancy.

| Exact affected REPORT location | Surgery risk | Control risk | Printed ARD and 95% CI | Subtraction | Recomputed interval | Printed ARD interval | Remaining gap | Relative discrepancy |
|---|---:|---:|---|---:|---|---|---:|---:|
| [Table 2 p7, heart failure](../../../jama_aminian_2019_oi_190103.pdf#page=7) | 6.8 | 18.9 | 12.9 (10.4–15.1) | 12.1 | [12.00,12.20] | [12.85,12.95] | 0.65 | 0.0503876 |
| [Table 2 p7, coronary artery disease](../../../jama_aminian_2019_oi_190103.pdf#page=7) | 7.9 | 11.6 | 4.2 (1.9–6.8) | 3.7 | [3.60,3.80] | [4.15,4.25] | 0.35 | 0.0833333 |
| [Table 2 p7, cerebrovascular disease](../../../jama_aminian_2019_oi_190103.pdf#page=7) | 4.1 | 5.6 | 1.8 (−0.03 to 3.4) | 1.5 | [1.40,1.60] | [1.75,1.85] | 0.15 | 0.0833333 |
| [Table 2 p7, nephropathy](../../../jama_aminian_2019_oi_190103.pdf#page=7) | 6.1 | 16.3 | 11.1 (8.8–13.6) | 10.2 | [10.10,10.30] | [11.05,11.15] | 0.75 | 0.0675676 |
| [Table 2 p7, atrial fibrillation](../../../jama_aminian_2019_oi_190103.pdf#page=7) | 7.9 | 13.6 | 6.5 (4.4–8.7) | 5.7 | [5.60,5.80] | [6.45,6.55] | 0.65 | 0.1000000 |

**Display-precision interval check:** Every relative discrepancy is greater than 0.05, including heart failure's 0.0503876 after full interval allowance. Independent comparison rows in [Table 2 p7](../../../jama_aminian_2019_oi_190103.pdf#page=7) reproduce: primary 47.7 − 30.8 = 16.9, recomputed [16.8,17.0] versus printed [16.85,16.95]; secondary 27.6 − 17.0 = 10.6, [10.5,10.7] versus [10.55,10.65]; mortality 17.8 − 10.0 = 7.8, [7.7,7.9] versus [7.75,7.85]. Their interval gaps are zero.

**Necessary inputs available:** Yes for the same-display subtraction comparison and precision calculation. All group risks, ARDs, units, orientation and reference rows are printed.

**Exact missing inputs or definitions:** Exact unrounded group risks and ARDs; bootstrap output and code; whether the ARD point estimate is the original-sample risk subtraction, a bootstrap mean, a standardized difference, or a different risk-set construction; which population applies if it differs from the displayed group risks. Individual baseline-history exclusions are described but do not specify a separate population for the ARD point column.

**Source-grounded alternative interpretation:** Stated bootstrap resampling could accompany a separately constructed point estimate, or a risk-set/standardization step could differ for the five individual outcomes. The supplied source specifies bootstrap confidence intervals without identifying a different point-estimate construction for those five rows. The three reproducing rows support the comparator but do not prove the production algorithm for the other rows.

**Direct observation versus inferred explanation:** Observed: all five printed ARDs and input risks match source and exceed the 0.05 relative-gap rule under the supported subtraction. Inferred only: any bootstrap, standardization or population mechanism. The ARD CI limits are retained as printed; no recalculated CI or preferred numerical replacement is proposed.

**Exact remaining human question:** What point-estimate definition and analysis populations produced the five individual-outcome absolute 8-year risk differences, and how should they be interpreted alongside the displayed surgery/control risks?

**Compared document roles:** REPORT main Table 2 risks versus REPORT main Table 2 ARDs; REPORT main p4 method; REPORT results supplement p7 corroborating risks.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** statistical_results

**Classification rationale:** The conflicting estimates are within one REPORT display. The supplement only corroborates risk inputs, so no S_C relationship is added. No PLAN conflicts occur; precedence leaves S_W. No classification correction is needed.

**Classification ambiguity:** None for role/domain; the point-estimate construction remains a missing definition.

**Evidence state:** reproduced

**Determining recheck fact:** All five source-matched point ARDs remain separated from their supported risk-subtraction intervals with relative gaps above 0.05.

## C003 — Cerebrovascular interval and treatment test

**Location found:** Yes, all six content locations below were found, including the narrative continuation from p4 to p6.

| Exact location and role | Source value/text matched | Comparator or contextual fact matched |
|---|---|---|
| [REPORT main Table 2 p7, cerebrovascular row](../../../jama_aminian_2019_oi_190103.pdf#page=7) | ARD 1.8 (95% CI −0.03 to 3.4) | Adjusted HR 0.67 (0.48–0.94), P = .02 |
| [REPORT main Table 2 p7, footnotes a/b](../../../jama_aminian_2019_oi_190103.pdf#page=7) | ARD has 95% bootstrap CI, 1000 samples, at 8 years | HR and P are from adjusted Cox models of relative instantaneous risk |
| [REPORT main methods p4](../../../jama_aminian_2019_oi_190103.pdf#page=4) | Percentile bootstrap risk CI; fully adjusted Cox model; two-sided alpha .05 | Explicitly separate risk and hazard constructions |
| [REPORT main narrative pp4 and 6](../../../jama_aminian_2019_oi_190103.pdf#page=6) | Statement begun on p4 says significantly lower incidence of other five individual endpoints; p6 names cerebrovascular among them | Statement is compatible with the significant Cox result; it does not supply an ARD-specific test |
| [REPORT main Figure 3D p8](../../../jama_aminian_2019_oi_190103.pdf#page=8) | HR 0.67 (0.48–0.94), P = .02 | Corroborates the hazard inference |
| [REPORT eTable 6 p9](../../../joi190103supp1_prod.pdf#page=9) | HR 0.67 (0.48,0.94), treatment P = 0.02 | Distinct PH-test P = 0.10 is not the treatment P |

**Source value/text matched:** Yes; the negative −0.03 lower limit was visually confirmed in Table 2, not normalized to a positive value.

**Comparator matched:** Yes, the treatment P = .02 and hazard interval are consistent across Table 2, Figure 3D and eTable 6.

**Consistency rule applicable:** Route A category 1: at the stated 95%/.05 levels, a printed interval including the null and a significant displayed treatment test give different null readings. The scope explicitly retains this category when source assigns the interval and test to different analyses. Their different analyses are the principal alternative interpretation, not an assertion that risk and hazard estimands must agree numerically.

**Calculation or logical comparison reproduced:** −0.03 ≤ 0 ≤ 3.4, whereas .02 < .05. The adjusted HR interval satisfies 0.48 ≤ 0.67 ≤ 0.94 < 1 and reconciles with its significant P. The reproduced observation is specifically the ARD-interval versus displayed treatment-test reading, not a contradiction inside the HR tuple.

**Display-precision interval check:** Category A1 is exempt from the relative-gap rounding screen. For transcription robustness, −0.03 has [−0.035,−0.025], 3.4 has [3.35,3.45], and .02 has [.015,.025]; all permitted lower ARD limits stay negative, upper limits positive, and treatment P values below .05. No cross-estimand P reconstruction is performed.

**Necessary inputs available:** Yes for printed null inclusion and significance: interval limits, confidence level, P, two-sided alpha and analysis labels are available.

**Exact missing inputs or definitions:** An ARD-specific test/P; unrounded bootstrap outputs; whether any significance statement is intended to apply to the ARD rather than solely to adjusted hazards. Individual data are not supplied for separate bootstrap reproduction.

**Source-grounded alternative interpretation:** Footnotes a/b explicitly distinguish bootstrap 8-year ARD from adjusted instantaneous-hazard inference. The displayed P may intentionally refer only to the HR, and the lower-incidence narrative may use that inference. This can explain distinct decisions; it is retained prominently as required by category A1.

**Direct observation versus inferred explanation:** Observed: the printed ARD CI contains zero, printed P is significant, and source assigns them different analyses. Inferred only: whether the different estimands, covariate adjustment, time horizon or bootstrap sampling explains the decisions. No numerical equivalence is asserted.

**Exact remaining human question:** Should P = .02 and the lower-incidence statement be read solely as adjusted-hazard inference, and how should the 8-year cerebrovascular ARD interval containing zero be interpreted and extracted?

**Compared document roles:** REPORT main Table 2 interval versus REPORT main Table 2 hazard test, with REPORT methods/narrative/Figure 3D and REPORT eTable 6 contextual corroboration.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** statistical_results

**Classification rationale:** The compared interval/test are in one REPORT document. The other REPORT copies agree with the hazard side and add no S_C conflict. No PLAN conflict is involved. No classification correction is needed.

**Classification ambiguity:** None for roles/type/domain. Distinct analyses are expressly disclosed and constrain the inference made from the reproduced printed reading.

**Evidence state:** reproduced

**Determining recheck fact:** Direct source confirms ARD CI −0.03 to 3.4 contains zero and displayed treatment P = .02 is significant at .05; category A1 expressly retains this different-analysis comparison.

## C004 — Coronary diagnosis-position criteria

**Prominent source-grounded incorporation alternative:** [PLAN protocol p4](../../../joi190103supp2_prod.pdf#page=4) begins the outcome section with a reference to eTable 1 for diagnosis codes/definitions. That reference may incorporate the fuller operational conditions in the reported table. The package does not supply a separately dated original incorporated table or an explicit rule of precedence between the inline code list and that table. The recheck preserves this ambiguity and does not assert a change in implemented eligibility, event totals, or timing.

**Location found:** Yes, all assigned locations, including both relevant bold-code occurrences and the primary-diagnosis footnote.

| Exact location and role | Source value/text matched | Comparator or contextual fact matched |
|---|---|---|
| [PLAN original protocol p4, opening reference and coronary Other](../../../joi190103supp2_prod.pdf#page=4) | Inline 411.X; 411.X AND 414.X; no diagnosis-position condition or bold convention in this passage | Explicit eTable 1 incorporation reference is present |
| [PLAN original protocol p4, Primary endpoint](../../../joi190103supp2_prod.pdf#page=4) | First occurrence of composite outcomes 1–6 | Coronary disease is one primary component |
| [REPORT eTable 1 p2, coronary row and footnote](../../../joi190103supp1_prod.pdf#page=2) | Standalone 411.X bold; paired 411.X regular; paired 414.X bold | Footnote: bold text must be a primary diagnosis |
| [REPORT main endpoint definition p2](../../../jama_aminian_2019_oi_190103.pdf#page=2) | Coronary events include unstable angina, MI or coronary intervention/surgery | Main points to eTable 1 definitions/codes, continued on p3 |
| [REPORT main Table 2 p7](../../../jama_aminian_2019_oi_190103.pdf#page=7) | Coronary HR 0.69 (0.54–0.87) and primary composite HR 0.61 (0.55–0.69) | These identify the named results whose component ascertainment is relevant |
| [PLAN amendment p7](../../../joi190103supp2_prod.pdf#page=7) | Nutritional/adverse-event and E-value additions | No coronary-position clarification in the supplied amendment |

**Source value/text matched:** Yes. Source text and visual plan p4 confirm the inline code identities; source report p2 render confirms the bold-versus-regular distinction item by item. Text extraction alone does not carry that font condition.

**Comparator matched:** Yes. Both standalone 411.X and the 414.X member of the pair carry the reported primary-diagnosis requirement; the paired 411.X does not carry bold formatting. No whole-row requirement was substituted for these specific occurrences.

**Consistency rule applicable:** Compare printed operational eligibility predicates for a planned primary component, Route A category 5, focus D. The report's indicated predicate includes primary diagnosis; the inline plan predicate does not specify that condition. The observation concerns a component definition, not the choice to use bold typography.

**Calculation or logical comparison reproduced:** Inline predicate for standalone 411.X is code match with diagnosis position unstated; reported predicate is code match AND primary diagnosis. Inline paired predicate is 411.X AND 414.X with positions unstated; reported paired predicate additionally requires primary diagnosis for 414.X. These are different printed specifications. Absence of a plan position condition is not proof that all positions were implemented.

**Display-precision interval check:** Not applicable to this categorical code/position comparison. There is no numerical rounding gap or estimate comparison.

**Necessary inputs available:** Yes for the printed predicates, their source roles, bold-footnote rule, composite membership and incorporation reference.

**Exact missing inputs or definitions:** Dated original version of the incorporated eTable 1; precedence of incorporated versus inline specifications; any ascertainment amendment or implementation rule; event-level diagnosis-position records needed to measure any actual count consequence.

**Source-grounded alternative interpretation:** The explicit eTable 1 reference may incorporate the fuller primary-diagnosis rule, with the inline list acting as an abbreviated code summary. Alternatively, fuller operational restrictions may have been elaborated subsequently. The first interpretation is directly supported by the reference and remains prominently visible; neither temporal explanation is established.

**Direct observation versus inferred explanation:** Observed: inline codes have no explicit position predicate; reported bold codes have one; the plan points to eTable 1. Inferred only: whether intended or implemented ascertainment changed. No actual event-count change or revised baseline-history classification is asserted.

**Exact remaining human question:** Did the original incorporated eTable 1 require primary-diagnosis status for standalone 411.X and paired 414.X, and how should that version and the inline protocol criteria be read together for planned and reported ascertainment?

**Compared document roles:** PLAN original prospective outcome criteria p4 and amendment p7 versus REPORT completed-study operational definitions in eTable 1 p2; REPORT main p2/p7 identifies endpoints and results.

**Relationship type:** P_R

**All relationships:** P_R

**Review domain:** protocol_report

**Classification rationale:** The direct criterion comparison is PLAN versus REPORT, so P_R applies. Main report and results table complement each other rather than conflict. No separate P_P or S_C relationship is established. No classification correction is needed.

**Classification ambiguity:** The explicit original-plan eTable 1 incorporation could reconcile intended criteria; no dated incorporated version or precedence rule is supplied. P_R describes the printed comparison and does not imply an implementation violation.

**Evidence state:** reproduced

**Determining recheck fact:** Exact source confirms the two report primary-diagnosis predicates and their absence from the inline plan passage, while confirming its incorporation reference; the registered printed-specification comparison remains under category A5 with that bounded ambiguity.

## C005 — Atrial-fibrillation ICD10 code criterion

**Prominent source-grounded incorporation alternative:** [PLAN protocol p4](../../../joi190103supp2_prod.pdf#page=4) expressly refers to eTable 1 for diagnosis codes/definitions. A fuller incorporated table could already include i48.1, even though the inline AF list omits it. No separately dated original table or priority rule is supplied. This is retained alongside the printed list comparison; no implemented code-set expansion or event-count change is asserted.

**Location found:** Yes, every assigned location and the corroborating ICD9/CPT entries were found.

| Exact location and role | Source value/text matched | Comparator or contextual fact matched |
|---|---|---|
| [PLAN original protocol p4, AF list and opening reference](../../../joi190103supp2_prod.pdf#page=4) | ICD10 i48.0, i48.2, i48.91 | Opening explicitly refers to eTable 1 |
| [REPORT eTable 1 p2, AF row](../../../joi190103supp1_prod.pdf#page=2) | ICD10 i48.0, i48.1, i48.2, i48.91 | Both lists have ICD9 427.31 and CPT 93650,93653,93656,93657 |
| [PLAN original protocol p4, primary composite](../../../joi190103supp2_prod.pdf#page=4) | First occurrence of outcomes 1–6, including AF | Primary-component status is matched |
| [REPORT main endpoint definition p2](../../../jama_aminian_2019_oi_190103.pdf#page=2) | Six-component composite includes AF | Named endpoint agrees; main uses supplement codes |
| [REPORT main Table 2 p7](../../../jama_aminian_2019_oi_190103.pdf#page=7) | AF HR 0.78 (0.62–0.97); primary composite HR 0.61 (0.55–0.69) | Identifies the affected endpoint results |
| [PLAN amendment p7](../../../joi190103supp2_prod.pdf#page=7) | Adverse-event/nutritional and E-value additions | No AF-code clarification in its supplied content |

**Source value/text matched:** Yes; the inline PLAN AF list and REPORT AF list were checked in direct-source text and both page renders.

**Comparator matched:** Yes; the report list contains precisely the same three inline codes plus i48.1, and the ICD9/CPT comparators agree.

**Consistency rule applicable:** Compare operational diagnosis-code sets for a prespecified primary composite component, focus D and Route A category 5. This is a code-eligibility comparison, not merely different endpoint terminology.

**Calculation or logical comparison reproduced:** Printed report ICD10 set minus printed inline plan set = {i48.1}; printed inline plan set minus report set is empty. The named six-component composite agrees. This logical result does not establish which code set was used in the EHR extraction.

**Display-precision interval check:** Not applicable to exact categorical code identifiers; there is no rounding interval to compute.

**Necessary inputs available:** Yes for source list comparison, matching ICD9/CPT entries, primary-component status and original-plan incorporation reference.

**Exact missing inputs or definitions:** Dated original incorporated eTable 1; precedence between inline and incorporated definitions; any reconciled extraction code list/version; baseline and incident records needed to quantify actual eligibility or event-count effects.

**Source-grounded alternative interpretation:** The eTable 1 incorporation may supply the fuller intended list; the inline protocol list may be abbreviated; or the report may reflect a subsequently elaborated list. The supplied amendment does not identify which interpretation holds.

**Direct observation versus inferred explanation:** Observed: i48.1 is printed in the report list and not in the inline plan list, and plan incorporates eTable 1 by reference. Inferred only: change in planned, implemented or effective code coverage. No event-count, risk-set or timing effect is asserted.

**Exact remaining human question:** Was i48.1 present in the original incorporated definition and in baseline/incident AF ascertainment, and how should that definition be reconciled with the inline protocol list?

**Compared document roles:** PLAN protocol prospective AF/component criteria p4 and amendment p7 versus REPORT eTable 1 completed-study code description p2; REPORT main p2/p7 identifies named endpoints/results.

**Relationship type:** P_R

**All relationships:** P_R

**Review domain:** protocol_report

**Classification rationale:** The printed criterion comparison crosses PLAN and REPORT. Named endpoint agreement and corroborating main results add no S_C or S_W conflict, and no plan-internal conflict is established. No classification correction is needed.

**Classification ambiguity:** Original-plan eTable 1 incorporation may reconcile the intended code set, but its original version and precedence are not supplied. P_R does not imply an implementation violation.

**Evidence state:** reproduced

**Determining recheck fact:** Direct source confirms the inline three-code set versus report four-code set, with i48.1 as the sole printed difference and with the original incorporation reference retained under category A5.

## C006 — Planned multiplicity rule and 52 longitudinal intervals

**Location found:** Yes, PLAN [original statistical analysis p6](../../../joi190103supp2_prod.pdf#page=6), PLAN [amendment p7](../../../joi190103supp2_prod.pdf#page=7), REPORT [main methods p4](../../../jama_aminian_2019_oi_190103.pdf#page=4), and REPORT [eTable 8 p12](../../../joi190103supp1_prod.pdf#page=12), including all 13 variable rows at each of four times and both method/confidence footnotes.

**Source value/text matched:** PLAN p6 names prospective weight-loss/HbA1c comparisons over time, followed by significance .05, 95% CIs where applicable, no adjustment for multiple comparisons of secondary endpoints and exploratory interpretation. Amendment p7 adds nutritional variables/adverse-event work but contains no multiplicity-family clarification. REPORT main p4 gives general two-sided .05/95% language and describes spline/proportion analyses.

**Comparator matched:** REPORT eTable 8 has four Estimate (98.8% CI) headings and explicitly states that displayed intervals are 98.8% Bonferroni-corrected. Its method footnote describes four-knot spline interacted with treatment for metabolic/nutritional variables and two-sample proportions test for medication data at each time point. The 52 printed entries below were confirmed individually in direct-source extraction and the full source-page render. All are under the same corrected confidence heading; cells contain estimate [lower,upper].

| Exact REPORT row location | Year 1 | Year 2 | Year 5 | Year 8 |
|---|---|---|---|---|
| [eTable 8 p12, weight lbs](../../../joi190103supp1_prod.pdf#page=12) | −56.6 [−57.1,−56.1] | −73.7 [−74.4,−73.0] | −45.2 [−45.9,−44.6] | −44.8 [−45.5,−44.1] |
| [eTable 8 p12, weight kg](../../../joi190103supp1_prod.pdf#page=12) | −25.7 [−25.9,−25.4] | −33.4 [−33.7,−33.1] | −20.5 [−20.8,−20.2] | −20.3 [−20.6,−20.0] |
| [eTable 8 p12, HbA1c %](../../../joi190103supp1_prod.pdf#page=12) | −1.5 [−1.6,−1.4] | −1.6 [−1.7,−1.5] | −1.0 [−1.1,−0.9] | −1.1 [−1.2,−1.0] |
| [eTable 8 p12, protein g/dL](../../../joi190103supp1_prod.pdf#page=12) | −0.5 [−0.6,−0.5] | −0.5 [−0.5,−0.5] | −0.3 [−0.3,−0.3] | −0.3 [−0.3,−0.3] |
| [eTable 8 p12, albumin g/dL](../../../joi190103supp1_prod.pdf#page=12) | −0.3 [−0.3,−0.3] | −0.2 [−0.2,−0.1] | −0.1 [−0.1,−0.1] | −0.2 [−0.2,−0.1] |
| [eTable 8 p12, hemoglobin g/dL](../../../joi190103supp1_prod.pdf#page=12) | −0.6 [−0.6,−0.5] | −0.4 [−0.4,−0.3] | −0.1 [−0.2,0] | −0.2 [−0.2,−0.1] |
| [eTable 8 p12, vitamin D25 ug/L](../../../joi190103supp1_prod.pdf#page=12) | 6.4 [5.0,7.7] | 4.1 [2.6,5.7] | −0.9 [−2.7,0.9] | −1.4 [−4.4,1.7] |
| [eTable 8 p12, non-insulin diabetes medication %](../../../joi190103supp1_prod.pdf#page=12) | −50 [−52.9,−47.1] | −51.5 [−54.6,−48.3] | −47.4 [−51.9,−42.9] | −37.9 [−45.3,−30.6] |
| [eTable 8 p12, insulin %](../../../joi190103supp1_prod.pdf#page=12) | −8.3 [−11.1,−5.4] | −9.1 [−12.3,−5.9] | −9.1 [−13.7,−4.6] | −8.1 [−15.5,−0.7] |
| [eTable 8 p12, renin–angiotensin inhibitors %](../../../joi190103supp1_prod.pdf#page=12) | −25 [−28.1,−21.9] | −26.6 [−30.1,−23.1] | −27.5 [−32.3,−22.7] | −26.4 [−34,−18.8] |
| [eTable 8 p12, other antihypertensive medication %](../../../joi190103supp1_prod.pdf#page=12) | −2.7 [−5.6,0.3] | −3.4 [−6.7,−0.2] | −7.7 [−12.1,−3.2] | −10.6 [−17.6,−3.7] |
| [eTable 8 p12, lipid-lowering medication %](../../../joi190103supp1_prod.pdf#page=12) | −16.7 [−19.8,−13.5] | −21.1 [−24.5,−17.6] | −26.4 [−31.1,−21.7] | −28.3 [−35.8,−20.8] |
| [eTable 8 p12, aspirin %](../../../joi190103supp1_prod.pdf#page=12) | −24.5 [−27.1,−21.9] | −24.4 [−27.4,−21.4] | −25.9 [−30.2,−21.6] | −27 [−34,−20] |

**Consistency rule applicable:** Focus D, Route B: compare a planned confidence/multiplicity decision rule with the reported explicit corrected rule. Even for ancillary longitudinal results, the comparison falls under the planned-decision-rule exception to peripheral comparisons. It concerns which confidence rule accompanies extracted weight/HbA1c and related contrasts.

**Calculation or logical comparison reproduced:** PLAN states no secondary-endpoint multiplicity adjustment and 95% CIs; REPORT expressly states Bonferroni-corrected 98.8% CIs for every one of the 52 entries. A family of four at alpha .05 would give 1 − .05/4 = .9875 = 98.75%, which can print 98.8%. This arithmetic is a diagnostic of a possible four-time-point family, not proof of the actual family. REPORT year-1 other-antihypertensive entry −2.7 [−5.6,0.3], P = .02 was independently matched; at corrected alpha approximately .012, P = .02 and inclusion of zero reconcile, so that entry is not an independent interval/test conflict.

**Display-precision interval check:** Confidence percentages as printed allow 95% [94.5,95.5] and 98.8% [98.75,98.85], but a numeric relative gap would not be the relevant reproduction rule: the registered comparison is the explicit unadjusted versus Bonferroni-corrected categorical decision rule. Half-unit allowance does not turn an explicitly corrected procedure into the stated no-adjustment procedure. No interval limits are recalculated from a guessed standard error.

**Necessary inputs available:** Yes for the two explicit rules, original prospective longitudinal paragraph, amended nutritional scope and 52 disclosed corrected intervals.

**Exact missing inputs or definitions:** Which family the original no-adjustment rule covers; a prospective or amended separate longitudinal correction rule; the number and membership of comparisons underlying 98.8%; whether the reported P values are adjusted or unadjusted; exact confidence level before rounding. Covariance and spline contrast definitions are absent for recreating the 52 intervals from patient data.

**Source-grounded alternative interpretation:** The original no-adjustment rule may apply only to seven cardiovascular secondary outcomes, with longitudinal comparisons treated as a separate family. Four time points may form that separate corrected family. The plan names weight/HbA1c immediately before its inference paragraph but never specifies this family boundary; the amendment likewise does not define it. The report discloses the correction, and no concealed adjustment or preferred alternative analysis is asserted.

**Direct observation versus inferred explanation:** Observed: prospective general/no-adjustment language and a fully disclosed Bonferroni-corrected display. Inferred only: which family was intended and when its rule was established. The diagnostic four-comparison calculation is explicitly not an identified implementation fact.

**Exact remaining human question:** What analysis family and prospective or amended rule produced the 98.8% Bonferroni intervals, and how does that longitudinal rule relate to the original plan's unadjusted secondary-endpoint statement?

**Compared document roles:** PLAN protocol p6 inference rule and amendment p7 versus REPORT results supplement p12 corrected confidence rule; REPORT main p4 provides general method context.

**Relationship type:** P_R

**All relationships:** P_R

**Review domain:** protocol_report

**Classification rationale:** The registered conflict compares planned and reported decision rules, so P_R applies. The report's specific footnote can qualify its own general 95% wording; that contextual general statement does not independently establish an additional S_C issue. No P_P inconsistency is identified in the amendment. No classification correction is needed.

**Classification ambiguity:** The original unadjusted family may be cardiovascular-only, leaving a separate longitudinal family; its boundary and planned correction are not supplied. This limits the interpretation of P_R without changing the content-based roles.

**Evidence state:** reproduced

**Determining recheck fact:** Direct source matches the planned unadjusted rule and the explicitly Bonferroni-corrected 98.8% rule applied to all 52 entries; their analysis-family relationship remains unresolved.

## C007 — Year-5 hemoglobin interval versus P

**Location found:** Yes, REPORT [eTable 8 p12, hemoglobin year 5](../../../joi190103supp1_prod.pdf#page=12), its confidence heading and both footnotes; REPORT [main methods p4](../../../jama_aminian_2019_oi_190103.pdf#page=4), including spline treatment interaction and two-sided testing.

**Source value/text matched:** Yes; source text and render print −0.1 g/dL, 98.8% CI (−0.2, 0). The upper endpoint is a numerical zero, not a display-zero P value.

**Comparator matched:** Yes, the same year-5 hemoglobin row prints P < 0.001 with an asterisk. Other hemoglobin entries are year 1 −0.6 [−0.6,−0.5], year 2 −0.4 [−0.4,−0.3], year 8 −0.2 [−0.2,−0.1], each P < 0.001. All three comparison intervals exclude zero and do not show this printed null reading.

**Consistency rule applicable:** Route A category 1 at the actual printed confidence level: 98.8% corresponds to alpha .012, and a possibly rounded 98.75% corresponds to .0125. A same-contrast P < .001 rejects at both, while the printed interval includes zero. The comparison does not use .05 against a corrected confidence interval and is not about a P displayed as zero.

**Calculation or logical comparison reproduced:** −0.2 ≤ 0 ≤ 0; P < .001 < .012 and P < .001 < .0125. Printed estimate −0.1 remains within its interval. The reproduced observation is null inclusion at the upper endpoint versus significant printed test.

**Display-precision interval check:** Category A1 is exempt from the relative-gap rounding rule. The estimate's allowance is [−0.15,−0.05], lower endpoint [−0.25,−0.15], and confidence percentage [98.75,98.85]. A literal integer zero has half-unit interval [−0.5,0.5]; a zero formatted at the neighboring one-decimal scale would instead allow [−0.05,0.05]. Either allowance permits a small negative unprinted limit, so underlying inference could reconcile through rounding. Under the scope this is recorded as an alternative, while the source's extractable printed endpoint remains zero; it is not screened by relative gap.

**Necessary inputs available:** Yes for printed interval/test inference, confidence level, units, time and row assignment, and broad spline method.

**Exact missing inputs or definitions:** Unrounded upper and lower confidence limits; exact mean-change contrast; test target, statistic, degrees of freedom and covariance/standard error; whether P tests the same year-specific contrast or another spline association; exact Bonferroni family/confidence before rounding.

**Source-grounded alternative interpretation:** A small negative upper limit may round to zero, or the spline P may test a different target from the time-specific interval. The source describes the spline interaction but gives neither unrounded limit nor a separately identified target for this P. These alternatives can reconcile the underlying inference without replacing the printed category A1 observation.

**Direct observation versus inferred explanation:** Observed: upper endpoint zero and P < .001 in the same source row, under the corrected confidence heading. Inferred only: rounding or a distinct test target. No approximation using a standard error substitutes for the source's analysis.

**Exact remaining human question:** What unrounded year-5 hemoglobin interval and test/contrast produced the printed 98.8% CI (−0.2,0) and P < .001, and do both refer to the same time-specific mean-change difference?

**Compared document roles:** REPORT results supplement p12 interval versus REPORT same row P; REPORT main p4 supports method context.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** statistical_results

**Classification rationale:** This is an interval/test relationship within one REPORT display. General main-method context corroborates analysis description rather than contributing a conflicting S_C value. No PLAN is compared in this independent candidate. No classification correction is needed.

**Classification ambiguity:** None for roles/type/domain; unrounded limit and test target remain missing definitions.

**Evidence state:** reproduced

**Determining recheck fact:** Direct source confirms the printed zero upper endpoint and P < .001 at 98.8% confidence; category A1 preserves this printed interval/test comparison even though unrounded values could reconcile.

## C008 — Primary E-value pair and the 14 reproducing comparator entries

**Location found:** Yes, both primary entries and all seven nonprimary point/limit pairs in REPORT [eTable 12 p20](../../../joi190103supp1_prod.pdf#page=20); repeated primary numeric interpretation in REPORT [p19 E-value section](../../../joi190103supp1_prod.pdf#page=19); corresponding eight treatment HR/upper-CI pairs in REPORT [eTable 6 p9](../../../joi190103supp1_prod.pdf#page=9) and REPORT [main Table 2 p7](../../../jama_aminian_2019_oi_190103.pdf#page=7); robustness narrative in REPORT [main p9](../../../jama_aminian_2019_oi_190103.pdf#page=9). PLAN [amendment p7](../../../joi190103supp2_prod.pdf#page=7) was read for corroborating sensitivity scope only.

**Source value/text matched:** Yes, eTable 12 primary E-values 2.15 and 1.92; p19 explicitly repeats both and primary HR 0.61 (0.55–0.69). Source defines E-values on the risk-ratio scale while the table labels HR estimate and upper limit of 95% CI. All 14 nonprimary entries below were individually checked in the source render and source text.

**Comparator matched:** Yes, the seven nonprimary treatment HR/upper-limit inputs agree between eTable 6 and main Table 2. They are not the known-risk-factor HRs in eTable 12's right-hand columns.

**Consistency rule applicable:** Route A category 4: a within-display algebraic comparator supported by every nonprimary point/limit entry does not reproduce the primary pair after display allowance. The supplied source does not print a formula; E(h) = 1/h + sqrt((1/h)(1/h − 1)), h < 1, is used here only as the reproducing comparator supported by these supplied rows, not as an external mandatory convention. No web or literature was consulted.

**Calculation or logical comparison reproduced:** Independently evaluated the monotone comparator using each two-decimal HR's [h−.005,h+.005] interval: transformed interval is [E(h+.005),E(h−.005)]. Printed two-decimal E-values have ±.005; the AF point value is printed 1.9 and has ±.05. All 14 comparator entries overlap their transformed intervals, so their remaining gaps and relative discrepancies are zero.

| Exact REPORT comparator location | Entry | Printed HR input | HR allowance | Recomputed E interval | Printed E | Printed E allowance | Gap / relative discrepancy |
|---|---|---:|---|---|---:|---|---|
| [eTable 12 p20, secondary](../../../joi190103supp1_prod.pdf#page=20) | Point | .62 | [.615,.625] | [2.579796,2.634933] | 2.62 | [2.615,2.625] | 0 / 0 |
| [eTable 12 p20, secondary](../../../joi190103supp1_prod.pdf#page=20) | Upper-CI limit | .72 | [.715,.725] | [2.102627,2.145250] | 2.11 | [2.105,2.115] | 0 / 0 |
| [eTable 12 p20, mortality](../../../joi190103supp1_prod.pdf#page=20) | Point | .59 | [.585,.595] | [2.750246,2.810607] | 2.81 | [2.805,2.815] | 0 / 0 |
| [eTable 12 p20, mortality](../../../joi190103supp1_prod.pdf#page=20) | Upper-CI limit | .72 | [.715,.725] | [2.102627,2.145250] | 2.13 | [2.125,2.135] | 0 / 0 |
| [eTable 12 p20, heart failure](../../../joi190103supp1_prod.pdf#page=20) | Point | .38 | [.375,.385] | [4.634336,4.774852] | 4.69 | [4.685,4.695] | 0 / 0 |
| [eTable 12 p20, heart failure](../../../joi190103supp1_prod.pdf#page=20) | Upper-CI limit | .49 | [.485,.495] | [3.455825,3.541515] | 3.52 | [3.515,3.525] | 0 / 0 |
| [eTable 12 p20, coronary](../../../joi190103supp1_prod.pdf#page=20) | Point | .69 | [.685,.695] | [2.233479,2.279195] | 2.27 | [2.265,2.275] | 0 / 0 |
| [eTable 12 p20, coronary](../../../joi190103supp1_prod.pdf#page=20) | Upper-CI limit | .87 | [.865,.875] | [1.546918,1.580836] | 1.55 | [1.545,1.555] | 0 / 0 |
| [eTable 12 p20, cerebrovascular](../../../joi190103supp1_prod.pdf#page=20) | Point | .67 | [.665,.675] | [2.326056,2.374123] | 2.35 | [2.345,2.355] | 0 / 0 |
| [eTable 12 p20, cerebrovascular](../../../joi190103supp1_prod.pdf#page=20) | Upper-CI limit | .94 | [.935,.945] | [1.306371,1.342194] | 1.31 | [1.305,1.315] | 0 / 0 |
| [eTable 12 p20, nephropathy](../../../joi190103supp1_prod.pdf#page=20) | Point | .40 | [.395,.405] | [4.373734,4.500804] | 4.46 | [4.455,4.465] | 0 / 0 |
| [eTable 12 p20, nephropathy](../../../joi190103supp1_prod.pdf#page=20) | Upper-CI limit | .52 | [.515,.525] | [3.217528,3.294018] | 3.29 | [3.285,3.295] | 0 / 0 |
| [eTable 12 p20, AF](../../../joi190103supp1_prod.pdf#page=20) | Point | .78 | [.775,.785] | [1.864562,1.902376] | 1.9 | [1.85,1.95] | 0 / 0 |
| [eTable 12 p20, AF](../../../joi190103supp1_prod.pdf#page=20) | Upper-CI limit | .97 | [.965,.975] | [1.187809,1.230138] | 1.21 | [1.205,1.215] | 0 / 0 |

**Display-precision interval check:** Both primary entries remain discrepant above .05, as reproduced below. Display allowance is applied to both the input HR and the printed E-value, and not just to a nominal-point calculation.

| Exact affected REPORT location | Entry | HR allowance | Recomputed E interval | Printed E allowance | Remaining gap | Relative discrepancy |
|---|---|---|---|---|---:|---:|
| [eTable 12 p20, primary; repeated p19](../../../joi190103supp1_prod.pdf#page=20) | Point 2.15, HR .61 | [.605,.615] | [2.634932817,2.691719429] | [2.145,2.155] | .479932817 | .223224566 |
| [eTable 12 p20, primary; repeated p19](../../../joi190103supp1_prod.pdf#page=20) | Limit 1.92, upper HR .69 | [.685,.695] | [2.233479210,2.279195048] | [1.915,1.925] | .308479210 | .160666255 |

The duplicated [p19 interpretation](../../../joi190103supp1_prod.pdf#page=19) independently matches point 2.15-fold and limit 1.92-fold, so both primary discrepancies apply to both numeric occurrences. Main [p9](../../../jama_aminian_2019_oi_190103.pdf#page=9) repeats the generic robustness interpretation but no additional primary numeric pair.

**Necessary inputs available:** Yes for the same-display comparator: all eight HR/upper-limit pairs, all 16 E-value entries, their displayed precision and row identity, and the risk-ratio-scale definition. Fourteen comparator entries support the algebra under source display allowance.

**Exact missing inputs or definitions:** Actual E-value formula/software setting; unrounded HRs and confidence limits; HR-to-RR conversion and its inputs, thresholds and incidence/time-horizon assumptions; any primary-specific construction; exact risk-ratio values used after conversion. No raw event-time output or calculation script is supplied.

**Source-grounded alternative interpretation:** A distinct primary HR-to-RR conversion may be intentional. The source defines E-values on a risk-ratio scale and the primary endpoint has a larger cumulative risk than several individual outcomes, so a primary-specific conversion is a plausible interpretation. The package does not name that conversion or supply its inputs. It could reconcile the pair without making the reproducing comparator a universal formula; its absence remains the exact human question under category A4.

**Direct observation versus inferred explanation:** Observed: printed primary pair and duplicated interpretation do not reproduce the algebra supported by all 14 nonprimary entries after display allowance. Inferred only: use of a distinct HR-to-RR conversion or another production mechanism. The comparator's support within the display is demonstrated; it is not declared the authors' actual algorithm.

**Exact remaining human question:** Which HR-to-risk-ratio transformation and input values produced primary E-values 2.15/1.92, and why does that construction differ from the comparator that reproduces both entries of every other outcome row?

**Compared document roles:** REPORT eTable 12 primary pair versus REPORT eTable 12 comparator pattern, with REPORT eTable 6/p19 and REPORT main Table 2/p9 inputs/context. PLAN amendment p7 only corroborates intended E-value analysis of eight endpoints and is not a conflicting relationship.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** statistical_results

**Classification rationale:** The primary/nonprimary transformation pattern and corresponding treatment-HR inputs occur within the same REPORT supplement. Main Table 2 agrees with those inputs and adds no S_C conflict. The PLAN amendment only corroborates analysis intent, so it adds no P_R. No classification correction is needed.

**Classification ambiguity:** None for roles/type/domain; the unstated primary HR-to-RR construction remains the bounded methodological ambiguity.

**Evidence state:** reproduced

**Determining recheck fact:** Direct source confirms primary 2.15/1.92 and all 14 supporting comparator entries; primary interval gaps are .223224566 and .160666255 relative to the printed values, both above .05 under the supported within-display comparator.

## Completion and limits

Covered stable IDs: C001, C002, C003, C004, C005, C006, C007, C008. Evidence states: reproduced 8; reproduced_after_transcription_correction 0; not_reproduced 0. No source/location transcription correction or role/type/domain correction was needed. Every assigned ID and affected repeated-pattern location remains recorded. C002 covers five affected rows and three reproducing rows; C006 covers 52 longitudinal estimate/interval entries; C008 covers both primary entries, their p19 repetition and 14 comparator entries.

No cited scientific location remains unavailable. Exact unrounded/individual-level outputs, original incorporated endpoint-table version/precedence, inference-family boundaries and primary HR-to-RR construction remain absent, as separately named in each candidate. These missing definitions constrain explanations and human questions; they are not substituted with external evidence. Source and reused assets were preserved. All candidates remain Pending Human Adjudication.
