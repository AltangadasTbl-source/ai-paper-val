# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6

**Pending Human Adjudication.** Every candidate below is an evidence-linked quality-control record. Suggested review dispositions are mechanical pre-fills; the human reviewer decides validity, importance and action. No candidate is a final correction or a paper-level conclusion judgment.

## Executive Quality-Control Summary

The review mapped all **39 physical PDF pages** in the supplied three-document package and registered **18 stable candidates, C001–C018**, without a count limit. Direct-source rechecking assigned 16 `recorded_candidate` states and two `record_input_error` states. The latter records, C011 and C017, retain their IDs and explicitly identify unsupported comparator-alignment assumptions. The corresponding mechanical pre-fills are 16 `retain` and two `discuss`; all 18 remain Pending Human Adjudication.

The records concern five displayed absolute-risk-difference comparisons, count/percentage and denominator questions, measure and unit labels, endpoint and table identity, matching-direction wording, a figure-axis label, reciprocal ratio conventions and a precision-conditional eligibility boundary. A candidate can be a small preventable reporting defect. If confirmed, such a defect could affect subsequent evidence extraction; this review establishes neither propagation nor changed conclusions.

## Package and Reused-Evidence Provenance

Only supplied package evidence was used. Document roles were assigned from content. Physical PDF page numbers below are independent of printed journal pagination.

| Source ID | Supplied source | Role | Complete scope | Units |
|---|---|---|---|---:|
| DOC-001 | [jama_aminian_2019_oi_190103.pdf](../jama_aminian_2019_oi_190103.pdf#page=1) | REPORT | Main article, Tables 1–2 and Figures 1–5, pp. 1–12 | 12 |
| DOC-002 | [joi190103supp1_prod.pdf](../joi190103supp1_prod.pdf#page=1) | REPORT | Results supplement, eTables 1–12 and eFigures 1–4, pp. 1–20 | 20 |
| DOC-003 | [joi190103supp2_prod.pdf](../joi190103supp2_prod.pdf#page=1) | PLAN | Original January 6, 2019 protocol and August 2, 2019 amendment, pp. 1–7 | 7 |
| Total | Three PDFs; no Office/workbook/CSV source | 32 REPORT pages; 7 PLAN pages | Entire package | 39 |

The curator inventoried and hashed 90 eligible existing evidence assets: 55 usable, 27 duplicate or normalized assets and eight partial metadata/selective-map assets. Reusable source-matched raw text covered all 39 pages. Partial maps and metadata were not treated as a scientific coverage boundary; old candidate sets, checker conclusions, dispositions and reports were not discovery inputs. Every page received new quantitative mapping. Existing text and images served as locators or transcription aids; the supplied PDFs remained authority. Direct Poppler renders were visually inspected for each candidate’s cited pages.

See the [source inventory](review_1_6/source_inventory.md), [evidence-asset inventory](review_1_6/evidence_asset_inventory.md), [main evidence map](review_1_6/extraction/main_quantitative_evidence.md), [support evidence map](review_1_6/extraction/support_quantitative_evidence.md) and [mechanical evidence recheck](review_1_6/verification/evidence_recheck.md). Legacy extraction/render engine versions were not always recorded; direct Poppler 26.01.0 source checks established present-run source matching. New derivatives identify their engine and command in the tooling/evidence records.

## Scope, Complete Coverage, and Exclusions

| Direct source | Total units | Reusable-backed units | Fresh-required extraction units | Newly mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 main article | 12 | 12 | 0 | 12 | COMPLETE |
| DOC-002 results supplement | 20 | 20 | 0 | 20 | COMPLETE |
| DOC-003 protocol/amendment | 7 | 7 | 0 | 7 | COMPLETE |
| Total | 39 | 39 | 0 | 39 | COMPLETE |

Reusable-backed and fresh-required counts partition the complete source scope. Zero fresh-required extraction units means reusable raw extraction existed for every page; it does not mean that scientific mapping or source confirmation was reused. Pages containing contents, administrative material or references were inspected and mapped with their applicable numerical content or explicit absence of new study-result relationships. There is no scientific coverage gap.

The review prioritized arithmetic, denominators/proportions/totals, statistical reporting, matched cross-document quantities, measure/label/scale identity and rates versus counts. Analysis populations were considered only where they affected a concrete reported number or comparison. It did not perform a raw-data, broad methodology, clinical, novelty or misconduct audit. Bibliographic identifiers, general design concerns and unsupported assumptions did not independently generate candidates. No coherent display-zero P value alone was registered. See [source coverage](review_1_6/source_coverage.md) and [stage coverage manifest](review_1_6/coverage_manifest.md).

## Quantitative and Statistical Relationship Coverage

The [numeric inventory](review_1_6/relationships/numeric_relationship_inventory.md) contains 123 hierarchical records, N001–N123: 38 parent source groups plus 85 expanded row records (61 baseline rows, eight outcomes and 16 risk-set rows). These are cross-referenced coverage records, not 123 independent scalar measurements. All mapped flow, count, percentage, time, risk-set, measure and unit relationships were checked; the last three risk-set records also received a separate fresh-agent confirmation. The [numeric checker](review_1_6/checkers/numeric_consistency.md) and [cross-source checker](review_1_6/checkers/cross_source_consistency.md) preserve duplicate aliases and reconciled observations.

Both statistical passes covered all **438 unique registered relationships, S001–S438**, without significance selection. Each pass used four distinct fresh high-effort agents over the same disjoint partition; no mapper was promoted into a statistical reviewer. Pass 2 read the full cross-lane stable ledger and all recheck facts and produced no additional stable candidates.

| Disjoint statistical range | Relationships | Full assigned scope |
|---|---:|---|
| S001–S120 | 120 | Eight rate-difference CIs; 48 cumulative-risk CIs; 16 subgroup HR CIs; eight interaction tests; eight association tests; eight proportional-hazards tests; 24 time-varying HR CIs and their repetitions |
| S121–S236 | 116 | 52 eTable 8 estimate/98.8%-CI/P tuples, 24 intervention-risk CIs and 40 known-risk-factor HR CIs |
| S237–S356 | 120 | Every eFigure 4 endpoint × ratio × index-date iteration: eight endpoints × three ratios × five iterations |
| S357–S438 | 82 | 32 main Table 2 tuples, five continuous-outcome tuples, six medication P-only relationships, five narrative claim groups, 16 trend curves, 16 E-values and two PLAN rule groups |
| Total per pass | 438 | Complete identical relationship scope in two independent fresh passes |

Checks retained endpoint/model/time/population identity, interval ordering and containment, direction, repeated values, unit labels and supplied inferential rules. The 120 sensitivity HR/CIs were inspected graphically: 111 excluded the null and nine crossed it; endpoint significance counts reconciled with the supplied narrative. Exact graph-only scalar coordinates were not invented. Covariance, sidedness, degrees of freedom, estimator or multiplicity rules were not filled in by convention. An ARD bootstrap CI and an adjusted Cox CI/P were not treated as the same inferential test. Generic two-sample-proportion wording versus Fisher wording and the BMI quartile concern were reconciled before registration.

The [complete statistical inventory](review_1_6/statistics/relationship_inventory.md), [pass 1](review_1_6/checkers/statistical_pass_1.md) and [pass 2](review_1_6/checkers/statistical_pass_2.md) preserve the complete per-relationship evidence, checker provenance and completion markers.

## Document-Role Classification Summary

REPORT means reporting content in the main article or results supplement. PLAN means prospective protocol, amendment or analysis-plan content, including background material within that bundle. Relationship definitions are: `P_R`, REPORT–PLAN; `P_P`, solely within/between PLAN material; `S_C`, between distinct REPORT documents; `S_W`, within one REPORT document. For genuine mixed discrepancies the precedence is P_R > P_P > S_C > S_W. A corroborating document does not create a new discrepancy relationship.

| Primary relationship type | Count |
|---|---:|
| S_W | 14 |
| S_C | 2 |
| P_R | 2 |
| P_P | 0 |
| Total | 18 |

C011 additionally records S_W in All relationships; its primary S_C follows precedence. C013’s PLAN context only corroborates the main definition and adds no P_R. Primary counts count each ID once.

| Derived review domain | Count |
|---|---:|
| statistical_results | 11 |
| report_internal_inconsistency | 5 |
| protocol_report | 2 |
| plan_material | 0 |
| Total | 18 |

| Evidence state | Count | Mechanical suggested disposition |
|---|---:|---|
| recorded_candidate | 16 | retain |
| record_input_error | 2 | discuss |
| not_reproduced | 0 | exclude |
| repaired_residual | 0 | retain |
| Total | 18 | All Pending Human Adjudication |

`recorded_candidate` records reproduced source facts and a reproduced mismatch or a bounded missing-definition question. `record_input_error` identifies an unsupported alignment or input assumption whose residual discrepancy cannot be settled. `not_reproduced` would denote direct-source disproof; `repaired_residual` would denote corrected source inputs leaving a different residual question. No evidence state adjudicates scientific validity. Review domains and suggested dispositions follow the supplied rules mechanically.

## Candidate Index

| ID | Category | Relationship type | Review domain | Evidence state |
|---|---|---|---|---|
| C001 | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C002 | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C003 | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C004 | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C005 | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C006 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C007 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C008 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C009 | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C010 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C011 | Denominator, proportion, or total inconsistency | S_C | statistical_results | record_input_error |
| C012 | Rate-versus-count inconsistency | S_W | statistical_results | recorded_candidate |
| C013 | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C014 | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C015 | Measure, label, or scale inconsistency | P_R | protocol_report | recorded_candidate |
| C016 | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C017 | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | record_input_error |
| C018 | Numeric or arithmetic inconsistency | P_R | protocol_report | recorded_candidate |

## Candidate Evidence Cards

## C001 — Heart-failure absolute risk difference

**Status:** Pending Human Adjudication

**Candidate statement:** The heart-failure row’s printed absolute risk difference does not equal nonsurgical minus surgical risk under its stated subtraction rule, beyond nearest-tenth rounding.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 2 group risks vs REPORT main Table 2 absolute risk difference and footnote a

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Main PDF p. 7, Table 2 heart failure row and footnote a](../jama_aminian_2019_oi_190103.pdf#page=7); [main PDF p. 4, Statistical Analysis](../jama_aminian_2019_oi_190103.pdf#page=4). Both pages visually inspected directly.

**Source evidence:** Surgical 6.8%; nonsurgical 18.9%; ARD 12.9% (95% CI 10.4–15.1).

**Reported-versus-comparator:** The heart failure absolute 8-year risk difference is 12.9% (95% CI 10.4–15.1). The same row reports surgical cumulative incidence 6.8% and nonsurgical cumulative incidence 18.9%. Footnote a names the difference as nonsurgical control group minus metabolic surgery. Page 4 describes Kaplan–Meier cumulative incidence and absolute risk differences; bootstrap percentile calculation is specified for the CIs.

**Reasoning procedure:** The comparison rule applies to the displayed same-outcome, same-time risk subtraction. It does not equate this risk-difference CI with the adjusted Cox HR CI or P value. The row values and footnote are direct source observations. Subtraction and the rounding bound are reproduced diagnostics. No numerical replacement, production error mechanism, or effect on conclusions is established.

**Calculation:** 18.9−6.8=12.1 percentage points, compared with 12.9; difference 0.8 percentage points. With three quantities individually rounded to a tenth, combined nearest-tenth uncertainty is at most 0.15 percentage points, below 0.8. This is a displayed point-estimate comparison, not a reconstruction of the fitted model or bootstrap distribution.

**Alternative source-grounded interpretations:** The source supplies bootstrap uncertainty estimation and outcome-specific risk sets; a separately generated ARD point estimate could conceivably explain the display, but the source does not state that its point estimate differs from subtraction of the same-row risks. This remains an alternative requiring a definition, not an inferred production process. Missing definition/input: Unrounded cumulative incidence values and the precise point-estimation implementation for the ARD, including whether a separately derived point estimate or risk set was used. Bootstrap CIs alone do not define an alternative ARD point estimate.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Direct source confirms all registered values and the same-row subtraction remains different beyond displayed rounding. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the heart-failure absolute risk difference. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-01; ARD_HEART_FAILURE; ST-M01; N103; S371.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the heart-failure absolute risk difference with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Was the heart failure ARD point estimate calculated from the same 8-year Kaplan–Meier risks printed in Table 2, or from a separately defined estimand, risk set, or point-estimation rule; where is that rule documented?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Coronary-artery-disease absolute risk difference

**Status:** Pending Human Adjudication

**Candidate statement:** The coronary-artery-disease row’s printed absolute risk difference does not equal the stated subtraction of its same-row risks, beyond nearest-tenth rounding.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 2 group risks vs REPORT main Table 2 absolute risk difference and footnote a

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Main PDF p. 7, Table 2 coronary artery disease row and footnote a](../jama_aminian_2019_oi_190103.pdf#page=7); [main PDF p. 4, Statistical Analysis](../jama_aminian_2019_oi_190103.pdf#page=4). Both pages visually inspected directly.

**Source evidence:** Surgical 7.9%; nonsurgical 11.6%; ARD 4.2% (95% CI 1.9–6.8).

**Reported-versus-comparator:** The coronary artery disease absolute 8-year risk difference is 4.2% (95% CI 1.9–6.8). The same row reports surgical cumulative incidence 7.9% and nonsurgical cumulative incidence 11.6%. Footnote a names the difference as nonsurgical control group minus metabolic surgery. Page 4 describes Kaplan–Meier cumulative incidence and absolute risk differences; bootstrap percentile calculation is specified for the CIs.

**Reasoning procedure:** The comparison rule applies to the displayed same-outcome, same-time risk subtraction. It does not equate this risk-difference CI with the adjusted Cox HR CI or P value. The row values and footnote are direct source observations. Subtraction and the rounding bound are reproduced diagnostics. No numerical replacement, production error mechanism, or effect on conclusions is established.

**Calculation:** 11.6−7.9=3.7 percentage points, compared with 4.2; difference 0.5 percentage points. With three quantities individually rounded to a tenth, combined nearest-tenth uncertainty is at most 0.15 percentage points, below 0.5. This is a displayed point-estimate comparison, not a reconstruction of the fitted model or bootstrap distribution.

**Alternative source-grounded interpretations:** The source supplies bootstrap uncertainty estimation and outcome-specific risk sets; a separately generated ARD point estimate could conceivably explain the display, but the source does not state that its point estimate differs from subtraction of the same-row risks. This remains an alternative requiring a definition, not an inferred production process. Missing definition/input: Unrounded cumulative incidence values and the precise point-estimation implementation for the ARD, including whether a separately derived point estimate or risk set was used. Bootstrap CIs alone do not define an alternative ARD point estimate.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Direct source confirms all registered values and the same-row subtraction remains different beyond displayed rounding. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the coronary-artery-disease absolute risk difference. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-02; ARD_CORONARY; ST-M02; N104; S375.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the coronary-artery-disease absolute risk difference with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Was the coronary artery disease ARD point estimate calculated from the same 8-year Kaplan–Meier risks printed in Table 2, or from a separately defined estimand, risk set, or point-estimation rule; where is that rule documented?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Cerebrovascular-disease absolute risk difference

**Status:** Pending Human Adjudication

**Candidate statement:** The cerebrovascular-disease row’s printed absolute risk difference does not equal the stated subtraction of its same-row risks, beyond nearest-tenth rounding.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 2 group risks vs REPORT main Table 2 absolute risk difference and footnote a

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Main PDF p. 7, Table 2 cerebrovascular disease row and footnote a](../jama_aminian_2019_oi_190103.pdf#page=7); [main PDF p. 4, Statistical Analysis](../jama_aminian_2019_oi_190103.pdf#page=4). Both pages visually inspected directly.

**Source evidence:** Surgical 4.1%; nonsurgical 5.6%; ARD 1.8% (95% CI −0.03 to 3.4).

**Reported-versus-comparator:** The cerebrovascular disease absolute 8-year risk difference is 1.8% (95% CI −0.03 to 3.4). The same row reports surgical cumulative incidence 4.1% and nonsurgical cumulative incidence 5.6%. Footnote a names the difference as nonsurgical control group minus metabolic surgery. Page 4 describes Kaplan–Meier cumulative incidence and absolute risk differences; bootstrap percentile calculation is specified for the CIs.

**Reasoning procedure:** The comparison rule applies to the displayed same-outcome, same-time risk subtraction. It does not equate this risk-difference CI with the adjusted Cox HR CI or P value. The row values and footnote are direct source observations. Subtraction and the rounding bound are reproduced diagnostics. No numerical replacement, production error mechanism, or effect on conclusions is established.

**Calculation:** 5.6−4.1=1.5 percentage points, compared with 1.8; difference 0.3 percentage points. With three quantities individually rounded to a tenth, combined nearest-tenth uncertainty is at most 0.15 percentage points, below 0.3. This is a displayed point-estimate comparison, not a reconstruction of the fitted model or bootstrap distribution.

**Alternative source-grounded interpretations:** The source supplies bootstrap uncertainty estimation and outcome-specific risk sets; a separately generated ARD point estimate could conceivably explain the display, but the source does not state that its point estimate differs from subtraction of the same-row risks. This remains an alternative requiring a definition, not an inferred production process. Missing definition/input: Unrounded cumulative incidence values and the precise point-estimation implementation for the ARD, including whether a separately derived point estimate or risk set was used. Bootstrap CIs alone do not define an alternative ARD point estimate.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Direct source confirms all registered values and the same-row subtraction remains different beyond displayed rounding. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the cerebrovascular-disease absolute risk difference. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-03; ARD_CEREBROVASCULAR; ST-M03; N105; S379.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the cerebrovascular-disease absolute risk difference with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Was the cerebrovascular disease ARD point estimate calculated from the same 8-year Kaplan–Meier risks printed in Table 2, or from a separately defined estimand, risk set, or point-estimation rule; where is that rule documented?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Nephropathy absolute risk difference

**Status:** Pending Human Adjudication

**Candidate statement:** The nephropathy row’s printed absolute risk difference does not equal the stated subtraction of its same-row risks, beyond nearest-tenth rounding.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 2 group risks vs REPORT main Table 2 absolute risk difference and footnote a

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Main PDF p. 7, Table 2 nephropathy row and footnote a](../jama_aminian_2019_oi_190103.pdf#page=7); [main PDF p. 4, Statistical Analysis](../jama_aminian_2019_oi_190103.pdf#page=4). Both pages visually inspected directly.

**Source evidence:** Surgical 6.1%; nonsurgical 16.3%; ARD 11.1% (95% CI 8.8–13.6).

**Reported-versus-comparator:** The nephropathy absolute 8-year risk difference is 11.1% (95% CI 8.8–13.6). The same row reports surgical cumulative incidence 6.1% and nonsurgical cumulative incidence 16.3%. Footnote a names the difference as nonsurgical control group minus metabolic surgery. Page 4 describes Kaplan–Meier cumulative incidence and absolute risk differences; bootstrap percentile calculation is specified for the CIs.

**Reasoning procedure:** The comparison rule applies to the displayed same-outcome, same-time risk subtraction. It does not equate this risk-difference CI with the adjusted Cox HR CI or P value. The row values and footnote are direct source observations. Subtraction and the rounding bound are reproduced diagnostics. No numerical replacement, production error mechanism, or effect on conclusions is established.

**Calculation:** 16.3−6.1=10.2 percentage points, compared with 11.1; difference 0.9 percentage points. With three quantities individually rounded to a tenth, combined nearest-tenth uncertainty is at most 0.15 percentage points, below 0.9. This is a displayed point-estimate comparison, not a reconstruction of the fitted model or bootstrap distribution.

**Alternative source-grounded interpretations:** The source supplies bootstrap uncertainty estimation and outcome-specific risk sets; a separately generated ARD point estimate could conceivably explain the display, but the source does not state that its point estimate differs from subtraction of the same-row risks. This remains an alternative requiring a definition, not an inferred production process. Missing definition/input: Unrounded cumulative incidence values and the precise point-estimation implementation for the ARD, including whether a separately derived point estimate or risk set was used. Bootstrap CIs alone do not define an alternative ARD point estimate.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Direct source confirms all registered values and the same-row subtraction remains different beyond displayed rounding. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the nephropathy absolute risk difference. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-04; ARD_NEPHROPATHY; ST-M04; N106; S383.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the nephropathy absolute risk difference with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Was the nephropathy ARD point estimate calculated from the same 8-year Kaplan–Meier risks printed in Table 2, or from a separately defined estimand, risk set, or point-estimation rule; where is that rule documented?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Atrial-fibrillation absolute risk difference

**Status:** Pending Human Adjudication

**Candidate statement:** The atrial-fibrillation row’s printed absolute risk difference does not equal the stated subtraction of its same-row risks, beyond nearest-tenth rounding.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 2 group risks vs REPORT main Table 2 absolute risk difference and footnote a

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Main PDF p. 7, Table 2 atrial fibrillation row and footnote a](../jama_aminian_2019_oi_190103.pdf#page=7); [main PDF p. 4, Statistical Analysis](../jama_aminian_2019_oi_190103.pdf#page=4). Both pages visually inspected directly.

**Source evidence:** Surgical 7.9%; nonsurgical 13.6%; ARD 6.5% (95% CI 4.4–8.7).

**Reported-versus-comparator:** The atrial fibrillation absolute 8-year risk difference is 6.5% (95% CI 4.4–8.7). The same row reports surgical cumulative incidence 7.9% and nonsurgical cumulative incidence 13.6%. Footnote a names the difference as nonsurgical control group minus metabolic surgery. Page 4 describes Kaplan–Meier cumulative incidence and absolute risk differences; bootstrap percentile calculation is specified for the CIs.

**Reasoning procedure:** The comparison rule applies to the displayed same-outcome, same-time risk subtraction. It does not equate this risk-difference CI with the adjusted Cox HR CI or P value. The row values and footnote are direct source observations. Subtraction and the rounding bound are reproduced diagnostics. No numerical replacement, production error mechanism, or effect on conclusions is established.

**Calculation:** 13.6−7.9=5.7 percentage points, compared with 6.5; difference 0.8 percentage points. With three quantities individually rounded to a tenth, combined nearest-tenth uncertainty is at most 0.15 percentage points, below 0.8. This is a displayed point-estimate comparison, not a reconstruction of the fitted model or bootstrap distribution.

**Alternative source-grounded interpretations:** The source supplies bootstrap uncertainty estimation and outcome-specific risk sets; a separately generated ARD point estimate could conceivably explain the display, but the source does not state that its point estimate differs from subtraction of the same-row risks. This remains an alternative requiring a definition, not an inferred production process. Missing definition/input: Unrounded cumulative incidence values and the precise point-estimation implementation for the ARD, including whether a separately derived point estimate or risk set was used. Bootstrap CIs alone do not define an alternative ARD point estimate.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Direct source confirms all registered values and the same-row subtraction remains different beyond displayed rounding. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the atrial-fibrillation absolute risk difference. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-05; ARD_ATRIAL_FIBRILLATION; ST-M05; N107; S387.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the atrial-fibrillation absolute risk difference with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Was the atrial fibrillation ARD point estimate calculated from the same 8-year Kaplan–Meier risks printed in Table 2, or from a separately defined estimand, risk set, or point-estimation rule; where is that rule documented?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Unmatched male percentage

**Status:** Pending Human Adjudication

**Candidate statement:** The displayed unmatched male percentage differs from direct nearest-tenth rounding of the printed count divided by the cohort denominator; the percentage-production rule requires clarification.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 1 count/percentage vs REPORT same-column cohort denominator

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Main Table 1, PDF p. 5, men row and column header](../jama_aminian_2019_oi_190103.pdf#page=5), directly rendered and visually inspected.

**Source evidence:** Men 18895 (48.2%); unmatched nonsurgical N=39267.

**Reported-versus-comparator:** The count/percentage cell is 18895 (48.2%). Its cohort column header gives N=39267.

**Reasoning procedure:** The comparison is conditional on ordinary unweighted count/cohort-denominator percentages and direct nearest-tenth rounding. Those are the displayed number/percentage/header relationship; the source does not prescribe a rounding sequence. Cell and header are source observations; the division and rounding comparison are diagnostics. A transcription mechanism, alternate denominator, or two-stage process is not established.

**Calculation:** 100×18895/39267=48.119285914%. This lies outside [48.15,48.25)%, the direct nearest-tenth interval for 48.2%; direct rounding yields 48.1%. The arithmetic is independently reproduced.

**Alternative source-grounded interpretations:** No specified alternative denominator or weighting is printed for this cell. A separate denominator or weighting could explain the percentage only if documented; the displayed sex counts sum to the full unmatched cohort. Missing definition/input: Exact percentage denominator, any weighting or analytic restriction, and rounding sequence/tie-breaking convention. No underlying participant data or production code is supplied.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Direct source confirms the registered cell and denominator, and the direct count-to-percentage rule gives the reproduced mismatch. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the unmatched male percentage. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-06; N041.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the unmatched male percentage with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: What numerator, denominator, or weighting rule produced 48.2% for 18895 men in the stated unmatched cohort of 39267?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Matched other-race percentage

**Status:** Pending Human Adjudication

**Candidate statement:** The displayed matched other-race percentage differs from direct nearest-tenth rounding of its count/cohort proportion. An intermediate rounding step could reconcile it and remains a concrete alternative.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 1 count/percentage vs REPORT same-column cohort denominator

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Main Table 1, PDF p. 5, other race row and column header](../jama_aminian_2019_oi_190103.pdf#page=5), directly rendered and visually inspected.

**Source evidence:** Other race 234 (2.1%); matched nonsurgical N=11435.

**Reported-versus-comparator:** The count/percentage cell is 234 (2.1%). Its cohort column header gives N=11435.

**Reasoning procedure:** The comparison is conditional on ordinary unweighted count/cohort-denominator percentages and direct nearest-tenth rounding. Those are the displayed number/percentage/header relationship; the source does not prescribe a rounding sequence. Cell and header are source observations; the division and rounding comparison are diagnostics. A transcription mechanism, alternate denominator, or two-stage process is not established.

**Calculation:** 100×234/11435=2.046348929%. This lies outside [2.05,2.15)%, the direct nearest-tenth interval for 2.1%; direct rounding yields 2.0%. The arithmetic is independently reproduced. A documented two-stage rounding rule would reconcile this specific display.

**Alternative source-grounded interpretations:** Two-stage rounding is a concrete numerical alternative: 2.046348929% → 2.05% → 2.1%. Neither a two-stage sequence nor its tie-breaking convention is stated. It can reconcile the display under that convention and must not be asserted as the authors’ production process. Missing definition/input: Exact percentage denominator, any weighting or analytic restriction, and rounding sequence/tie-breaking convention. No underlying participant data or production code is supplied.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Direct source confirms the registered cell and denominator, and the direct count-to-percentage rule gives the reproduced mismatch, with a named two-stage rounding alternative remaining unresolved. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the matched other-race percentage. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-07; N050.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the matched other-race percentage with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Was 2.1% calculated directly from 234/11435 or produced by two-stage rounding (2.046348929% → 2.05% → 2.1%), and what rounding convention was used?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Unmatched UACR missingness percentage

**Status:** Pending Human Adjudication

**Candidate statement:** The displayed unmatched UACR missingness percentage differs from direct nearest-tenth rounding of its count/cohort proportion. Intermediate rounding could reconcile it and requires confirmation.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 1 count/percentage vs REPORT same-column cohort denominator

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Main Table 1, PDF p. 6, UACR missingness row and column header](../jama_aminian_2019_oi_190103.pdf#page=6), directly rendered and visually inspected.

**Source evidence:** UACR missing 14665 (37.4%); unmatched nonsurgical N=39267.

**Reported-versus-comparator:** The count/percentage cell is 14665 (37.4%). Its cohort column header gives N=39267.

**Reasoning procedure:** The comparison is conditional on ordinary unweighted count/cohort-denominator percentages and direct nearest-tenth rounding. Those are the displayed number/percentage/header relationship; the source does not prescribe a rounding sequence. Cell and header are source observations; the division and rounding comparison are diagnostics. A transcription mechanism, alternate denominator, or two-stage process is not established.

**Calculation:** 100×14665/39267=37.346881605%. This lies outside [37.35,37.45)%, the direct nearest-tenth interval for 37.4%; direct rounding yields 37.3%. The arithmetic is independently reproduced. A documented two-stage rounding rule would reconcile this specific display.

**Alternative source-grounded interpretations:** Two-stage rounding is a concrete numerical alternative: 37.346881605% → 37.35% → 37.4%. Neither a two-stage sequence nor its tie-breaking convention is stated. It can reconcile the display under that convention and is not an observed production process. Missing definition/input: Exact percentage denominator, any weighting or analytic restriction, and rounding sequence/tie-breaking convention. No underlying participant data or production code is supplied.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Direct source confirms the registered cell and denominator, and the direct count-to-percentage rule gives the reproduced mismatch, with a named two-stage rounding alternative remaining unresolved. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the unmatched UACR missingness percentage. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-08; N088.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the unmatched UACR missingness percentage with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Was 37.4% calculated directly from 14665/39267 or produced by two-stage rounding (37.346881605% → 37.35% → 37.4%), and what rounding convention was used?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Absolute standardized-difference definition versus signed entries

**Status:** Pending Human Adjudication

**Candidate statement:** Table 1 defines absolute standardized differences but displays signed negative entries in the corresponding columns.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 1 footnote b vs REPORT main Table 1 signed columns

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Main PDF p. 5, standardized-difference columns](../jama_aminian_2019_oi_190103.pdf#page=5) and [p. 6, Table 1 footnote b and continued columns](../jama_aminian_2019_oi_190103.pdf#page=6), both directly rendered and inspected.

**Source evidence:** Footnote defines the absolute value of surgery-minus-control difference divided by pooled SD; examples −28.0/−2.9 for men, −75.3/−19.9 for age.

**Reported-versus-comparator:** Footnote b defines standardized differences as the absolute value of the difference in means or proportions between groups (metabolic surgery − nonsurgical control group) divided by pooled standard deviation. Before/after matching entries include men −28.0/−2.9 and age −75.3/−19.9. Other negative entries are also visible.

**Reasoning procedure:** An absolute numerator divided by a positive standard deviation cannot be negative. Reconstructing the precise SD formula is unnecessary to the sign comparison. Footnote and signs are directly observed. The nonnegativity comparison is deductive. A software or copyediting mechanism is not established.

**Calculation:** Each named negative cell is below zero, whereas the stated absolute-value definition yields a nonnegative standardized difference whenever defined.

**Alternative source-grounded interpretations:** The negative signs follow the named surgery-minus-control direction, consistent with a signed definition; the word absolute may instead describe a different intended presentation. Either interpretation requires human confirmation of the intended label. Missing definition/input: Whether the columns intentionally show signed differences and whether the footnote is intended to define absolute differences; underlying means/variances and exact pooled-SD formula are absent for magnitude reconstruction.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Printed absolute-value definition and source-confirmed negative entries conflict in sign. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the signed or absolute standardized-difference convention. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-09; SIGNED_STANDARDIZED_DIFFERENCE; N007 and N039–N099.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the signed or absolute standardized-difference convention with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Are the columns intended to show signed or absolute standardized differences, and which definition should govern extraction of the printed values?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Surgical biguanide percentage

**Status:** Pending Human Adjudication

**Candidate statement:** The surgical biguanide count and table denominator yield a percentage different from the printed 67.9% under the ordinary common-denominator rule.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 3 count/percentage vs REPORT eTable 3 surgical denominator

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Results supplement eTable 3, PDF p. 5, biguanides row and column header](../joi190103supp1_prod.pdf#page=5), directly rendered and visually inspected.

**Source evidence:** Biguanides 1530 (67.9%); surgical N=2287.

**Reported-versus-comparator:** The count/percentage cell is 1530 (67.9%). Its cohort column header gives N=2287.

**Reasoning procedure:** The comparison is conditional on ordinary unweighted count/cohort-denominator percentages and direct nearest-tenth rounding. Those are the displayed number/percentage/header relationship; the source does not prescribe a rounding sequence. Cell and header are source observations; the division and rounding comparison are diagnostics. A transcription mechanism, alternate denominator, or two-stage process is not established.

**Calculation:** 100×1530/2287=66.899868824%. This lies outside [67.85,67.95)%, the direct nearest-tenth interval for 67.9%; direct rounding yields 66.9%. The arithmetic is independently reproduced.

**Alternative source-grounded interpretations:** The eTable supplies a common surgery denominator and no special biguanide denominator or weighting. A different medication-specific analytic set could explain the display only if independently defined; no such definition is printed in this table. Missing definition/input: Exact percentage denominator, any weighting or analytic restriction, and rounding sequence/tie-breaking convention. No underlying participant data or production code is supplied.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Direct source confirms the registered cell and denominator, and the direct count-to-percentage rule gives the reproduced mismatch. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the baseline surgical biguanide percentage. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-10; N024.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the baseline surgical biguanide percentage with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Is biguanide use based on the printed 1530 count and 2287 denominator, or on a separately defined analytic denominator or weighting rule?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Baseline medication analytic sample versus cohort size

**Status:** Pending Human Adjudication

**Candidate statement:** The registered comparison aligned a medication analytic sample with the enrolled cohort without a supplied equality requirement. The printed two-person difference is real, but that unsupported alignment prevents establishing a residual reporting inconsistency.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT results supplement eTable 10 analytic sample vs REPORT supplement eTable 3 cohort header and REPORT main Table 1 cohort header

**Review domain:** statistical_results

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** The comparison includes different REPORT documents; any within-supplement relationship is recorded separately. A merely corroborating PLAN is not a discrepancy comparator.

**Classification ambiguity:** Analytic sample and enrolled cohort may differ legitimately; absence of an exclusion definition does not prove a numeric inconsistency.

**Exact source locations:** [Results supplement p. 14, eTable 10 year-0 nonsurgical sample](../joi190103supp1_prod.pdf#page=14); [supplement p. 5, eTable 3 header](../joi190103supp1_prod.pdf#page=5); [main p. 6, Table 1 matched nonsurgical header](../jama_aminian_2019_oi_190103.pdf#page=6); [main p. 3, Other Outcomes and Statistical Analysis](../jama_aminian_2019_oi_190103.pdf#page=3); [main p. 4, Statistical Analysis and Results](../jama_aminian_2019_oi_190103.pdf#page=4). All directly rendered and visually inspected.

**Source evidence:** Medication-proportion analytic N=11433 at year 0; enrolled matched nonsurgical N=11435.

**Reported-versus-comparator:** eTable 10 year 0 reports surgery 2287 and nonsurgical 11433; its title explicitly identifies sample sizes for computing medication proportions. eTable 3 and main Table 1 report the matched nonsurgical cohort as 11435. Main p. 4 Results also identifies 11435 enrolled matched controls, and pp. 3–4 discuss medication measurements/proportion tests without requiring complete analytic availability at year 0.

**Reasoning procedure:** No unconditional equality rule is established. The comparison would require the enrolled matched cohort and year-0 medication-proportion analytic sample to be identical; the titles describe distinct quantities. Both Ns and the two-person difference are observations/derived arithmetic. The equality of populations and any exclusion mechanism are unestablished assumptions.

**Calculation:** 11435−11433=2 reproduces the count difference. It does not reproduce an established denominator inconsistency because population identity is an unsupported input alignment.

**Alternative source-grounded interpretations:** eTable 10 is explicitly an analytic sample table and may legitimately restrict participants available for medication-proportion computation. Two unavailable observations would explain the difference, but this number-specific cause is not stated and is not inferred as fact. Missing definition/input: Medication analytic inclusion/availability rule at year 0; identities/reasons for any omitted participants; an explicit statement requiring the analytic and enrolled populations to coincide.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. The comparison equates an enrolled cohort header with an explicitly medication-specific analytic sample without a source statement establishing their identity. The residual denominator question cannot be settled from the package. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the medication analytic denominator and its population definition. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-11; N032, N013, N006; cross-source noncandidate comparator.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the medication analytic denominator and its population definition with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: What is the year-0 medication analytic eligibility/availability rule, why does its nonsurgical N equal 11433, and does any supplied definition require this N to equal the 11435 enrolled controls?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Percentage suffix on person-time rates

**Status:** Pending Human Adjudication

**Candidate statement:** The event-rate title adds a percentage suffix to quantities explicitly expressed per 100 patient-years, leaving a dimensional labeling question despite coherent rate arithmetic.

**Category:** Rate-versus-count inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 4 title and contents vs REPORT same table person-time units

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Results supplement p. 6, eTable 4 title, headers, footnotes, and primary row](../joi190103supp1_prod.pdf#page=6); [p. 1, contents entry](../joi190103supp1_prod.pdf#page=1), both directly rendered and inspected.

**Source evidence:** Title: Cause-Specific Event Rates (%) per 100 Patient-Years; rates 4.51 and 7.45, difference 2.94 per 100 patient-years.

**Reported-versus-comparator:** The title/contents say Cause-Specific Event Rates (%) per 100 Patient-Years of Follow-up at 8 Years. Headers specify rate per 100 patient-years and difference in event rate per 100 patient-years. Primary rates are 4.51 surgery and 7.45 nonsurgery, difference 2.94. Footnote b repeats the event-rate difference per 100 patient-years.

**Reasoning procedure:** The comparison rule applies to the dimensional label. Events divided by patient-time are a rate; a percentage of patients is dimensionless. Scaling the rate by 100 retains time in the denominator. Title, header, footnotes, and example values are directly observed. Unit comparison is deductive; no wrong event counts or clinical conclusion is inferred.

**Calculation:** 7.45−4.51=2.94 per 100 patient-years, so the example rate difference reconciles. The (%) title suffix introduces an additional dimensionless-risk reading not supplied by the table’s person-time units.

**Alternative source-grounded interpretations:** The title may use (%) informally for a rate scaled per 100 patient-years. That reading reconciles intent but still requires the extractor to retain person-time units rather than treat the numbers as risk percentages. Missing definition/input: Whether (%) intentionally denotes informal per-100 scaling rather than patient risk; any explicit interpretation of that suffix. Raw person-time totals would be needed to recompute rates, which this candidate does not attempt.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. The percentage suffix and explicit person-time-rate labels coexist in the source; the unit ambiguity remains as registered. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the person-time rate units. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-12; RATE_PERCENT_SUFFIX; STA-A-01; N025; S001–S008.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the person-time rate units with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Is (%) intended solely as informal per-100 rate notation, and should the table be extracted exclusively as events per 100 patient-years?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Five-component label attached to six-component primary result

**Status:** Pending Human Adjudication

**Candidate statement:** The supplement describes the matched primary E-value result as five-component MACE while the main article defines that primary endpoint with six components.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement primary E-value interpretation vs REPORT main primary endpoint definition

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The conflicting component counts occur in different REPORT documents, so the relationship is S_C. The original PLAN only corroborates the main six-component definition; it adds no P_R or P_P discrepancy. No independent within-supplement component-count comparator establishes an S_W relationship.

**Classification ambiguity:** None

**Exact source locations:** [Results supplement p. 19, E-value primary-outcome interpretation](../joi190103supp1_prod.pdf#page=19); [main p. 2, Primary and Secondary End Points](../jama_aminian_2019_oi_190103.pdf#page=2); [main p. 7, Figure 2 caption and Table 2 primary result](../jama_aminian_2019_oi_190103.pdf#page=7). [PLAN p. 4, six listed outcomes and primary definition](../joi190103supp2_prod.pdf#page=4) is corroboration only. All cited pages directly rendered and inspected.

**Source evidence:** Supplement says 5-component MACE while linking primary HR 0.61 (0.55–0.69), E-value 2.15; main defines six components.

**Reported-versus-comparator:** Supplement interpretation names 5-component MACE. Its immediately preceding primary-outcome discussion specifies HR 0.61 (95% CI 0.55–0.69) and E-value 2.15. Main defines the primary composite as six outcomes, listing all-cause mortality, coronary artery events, cerebrovascular events, heart failure, nephropathy, and atrial fibrillation; Figure 2 caption repeats six and the primary HR/CI match the supplement.

**Reasoning procedure:** Matching endpoint name/context and identical HR/CI identify the reported primary result; the component-count labels differ. The labels, list, and identical HR/CI are directly observed. Result-identity reasoning is grounded in these matches; an omitted-word or editing mechanism is not established.

**Calculation:** Six enumerated components versus five in the interpretation differ by one. No five-component primary analysis is defined in these locations.

**Alternative source-grounded interpretations:** The phrase could refer to a separate five-component analysis, but the surrounding source explicitly ties it to the primary HR and E-value; a separate analysis would need definition rather than assumption. Missing definition/input: Whether a distinct five-component analysis was intended by the E-value interpretation and, if so, its component list and identity.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. The source interpretation explicitly says five while the matched primary endpoint definition says six. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the component identity attached to the primary HR and E-value. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-13; PRIMARY_COMPONENT_LABEL; ST-M07; N036/N002; S404,S421,S422.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the component identity attached to the primary HR and E-value with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Does the E-value 2.15 interpretation concern the six-component primary outcome associated with HR 0.61, or a separately defined five-component outcome, and where is that definition?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — Time-varying HR text points to rate table

**Status:** Pending Human Adjudication

**Candidate statement:** The supplement’s time-varying-HR paragraph points to eTable 4, whose supplied content is a rate table; eTable 7 has the described HRs and time points.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement p.19 table reference vs REPORT supplement eTable 4 and eTable 7 contents

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** None

**Exact source locations:** [Results supplement p. 19, Time-varying hazard ratios paragraph and repeated eTable 7](../joi190103supp1_prod.pdf#page=19); [p. 6, eTable 4](../joi190103supp1_prod.pdf#page=6); [p. 10, eTable 7](../joi190103supp1_prod.pdf#page=10), all directly rendered and inspected.

**Source evidence:** Text says eTable 4 displays adjusted HR/95% CI at years 2,5,8; eTable 4 contains 8-year rates per 100 patient-years; eTable 7 displays the stated HRs.

**Reported-versus-comparator:** Page 19 says eTable 4 displays adjusted hazard ratios and 95% confidence intervals at 2, 5, and 8 years. eTable 4 is a cause-specific event-rate table per 100 patient-years at 8 years; primary rates 4.51/7.45 and difference 2.94. eTable 7, on pp. 10 and 19, supplies time-varying HRs at 2/5/8 years; primary HRs 0.57 (0.49,0.65), 0.78 (0.66,0.93), 0.79 (0.64,0.97).

**Reasoning procedure:** A specific numbered table reference must identify a table containing the named measure and time points. Reference text and both table structures are directly observed. Intended number and production cause are unknown.

**Calculation:** Number 4 leads to per-time rates at 8 years; number 7 leads to the named HR/CI structure at three years. This is a table-identity/measure comparison, not a demand that rate numbers equal HRs.

**Alternative source-grounded interpretations:** A draft numbering scheme could have used number 4, but the supplied document physically labels the matching table eTable 7; historical production numbering is not documented. Missing definition/input: Intended numbered reference. No model inputs are needed to confirm the reference mismatch.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Printed eTable 4 reference demonstrably identifies different content from its stated HR/CI description, which matches eTable 7. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the table identity for time-varying hazard ratios. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-14; TIME_VARYING_TABLE_REFERENCE; STA-A-02; ST-M08; N036/N028; S097–S120,S403.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the table identity for time-varying hazard ratios with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Which supplied table is intended by the page-19 statement that eTable 4 displays adjusted HRs and CIs at 2, 5, and 8 years?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C015 — Named matching direction in protocol versus report

**Status:** Pending Human Adjudication

**Candidate statement:** The prospective protocol and report name opposite groups as the one-to-five matching anchor. Their wording differs; actual implementation or a protocol departure is not established.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original protocol matching statement vs REPORT main matching caption and achieved cohort

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** A prospective PLAN statement is compared with its matched REPORT statement; context-only plan statements add no P_P relationship.

**Classification ambiguity:** The source wording reverses groups; supplied evidence cannot establish implementation or protocol violation.

**Exact source locations:** [PLAN PDF p. 3, Matching Process](../joi190103supp2_prod.pdf#page=3); [main p. 3, Figure 1 caption and final cohort boxes](../jama_aminian_2019_oi_190103.pdf#page=3); [main p. 4, Statistical Analysis continuation and Results](../jama_aminian_2019_oi_190103.pdf#page=4); [PLAN p. 6, Sensitivity analyses context](../joi190103supp2_prod.pdf#page=6), all directly rendered and inspected.

**Source evidence:** PLAN says each nonsurgical patient matched to five surgical patients. REPORT says each surgical patient matched to five nonsurgical patients; N=2287 surgery/11435 controls.

**Reported-versus-comparator:** The prospective protocol says each non-surgical patient will be matched by propensity score to five surgical patients. Main Figure 1 caption says each surgical patient was matched to five nonsurgical patients; p. 4 repeats that named direction. Final Ns are 2287 surgery and 11435 nonsurgery.

**Reasoning procedure:** The two explicit named-group statements reverse the matching direction. This rule compares report wording with plan wording; it does not reconstruct actual matching implementation. The two sentences and achieved cohort Ns are source observations. Literal ratio comparison is a diagnostic. A wording mistake, implementation difference, or protocol departure is not established.

**Calculation:** REPORT surgery:nonsurgery = 2287:11435 = 1:5. Literal PLAN named direction implies surgery:nonsurgery = 5:1 for that matching statement.

**Alternative source-grounded interpretations:** The PLAN sentence may reverse group names while referring to the same intended matching. PLAN p. 6 describes ratios 1:1, 1:5, 1:10 without naming numerator/denominator order; this corroborative context cannot independently prove a plan-internal discrepancy. Missing definition/input: Intended original protocol group order, actual implementation code, and whether a disclosed amendment intentionally changed the named direction. No claim of a proven implementation or compliance difference follows.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Source pages contain oppositely named matching statements, and the achieved ratio agrees with the REPORT direction. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the named surgery/control matching direction. It is bounded to the printed comparison and named unresolved definition. Checker provenance: NUM-15; MATCHING_DIRECTION; N001/N037/N038.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the named surgery/control matching direction with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Which group order was intended by the prospective matching statement, and does the reversal reflect wording or a documented change in the matching plan?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C016 — Lower zero tick on descending weight-change axis

**Status:** Pending Human Adjudication

**Candidate statement:** The source Figure 4A prints a lower vertical-axis zero beneath −25 on an otherwise descending scale. Its glyph is confirmed; the intended tick or annotation remains unresolved.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Figure 4A upper and lower ticks vs REPORT same panel percent-change axis

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** Direct source inspection confirms the lower vertical-axis zero glyph and distinguishes it from the horizontal-axis zero. Whether it is an unintended annotation or a mislabeled tick, and the intended lower scale value, remain human questions.

**Exact source locations:** [Main PDF p. 9, Figure 4A vertical axis and panel annotation](../jama_aminian_2019_oi_190103.pdf#page=9), directly rendered with Poppler and visually inspected.

**Source evidence:** Percent-change axis descends 0,−5,−10,−15,−20,−25, then another lower 0; panel reports Δ14.7% (95% CI 14.5–14.9), P<.001.

**Reported-versus-comparator:** The vertical percent-change axis shows 0, −5, −10, −15, −20, −25, then 0 at its lowest displayed level. The lower glyph is physically printed to the left of the vertical axis at the bottom horizontal-axis intersection; the x-axis time-zero glyph is separately printed below the intersection. The upper 0 and intervening negative ticks form evenly spaced descending steps; panel labels Percent Change, % (95% CI) and Total weight loss, %. Annotation reports Δ=14.7% (95% CI, 14.5–14.9), P<.001.

**Reasoning procedure:** An unbroken linear numeric axis cannot repeat 0 below −25 after successive −5 steps. No axis break or scale reset is shown. Both zeros and their positions are directly visible in a fresh render from the supplied PDF. Linear-sequence inconsistency is deductive. OCR artifacts are disproven; the production cause and intended replacement are not established.

**Calculation:** Differences between displayed adjacent ticks through −25 are −5. A next equally spaced step would continue the negative sequence; the printed lower 0 instead changes by +25. This diagnosis does not prescribe a corrected label.

**Alternative source-grounded interpretations:** It could have been intended as an annotation rather than a tick, but its alignment with the vertical-axis labels and the distinct x-axis zero make that interpretation require explicit figure-design confirmation. Missing definition/input: Intended bottom tick/axis extent and whether the lower glyph was intended as an independent annotation. No extraction ambiguity remains about the glyph itself.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. The supplied-source render visibly contains a lower vertical-axis 0 distinct from x-axis time zero, confirming the registered visual mismatch. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the vertical weight-change scale label. It is bounded to the printed comparison and named unresolved definition. Checker provenance: ST-M06; S392.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the vertical weight-change scale label with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Is the lower vertical-axis 0 intended as a tick or independent annotation, and what bottom scale value/extent was intended for Figure 4A?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C017 — Reciprocal matching-ratio notation in sensitivity figure

**Status:** Pending Human Adjudication

**Candidate statement:** The registered comparison treated reciprocal ratio lists as conflicting allocations without a supplied common group order. Reverse conventions can reconcile them, so the residual legend-identity question remains open.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement sensitivity prose vs REPORT same supplement eFigure 4 legend

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** All substantive compared statements occur within one REPORT document.

**Classification ambiguity:** Same group order is not established by the supplied legend; no numerical HR contradiction is asserted.

**Exact source locations:** [Results supplement p. 17, Matching and index date sampling prose](../joi190103supp1_prod.pdf#page=17); [p. 18, eFigure 4 legend/title](../joi190103supp1_prod.pdf#page=18), both directly rendered and inspected.

**Source evidence:** Prose ratios 1:1,1:5,1:10; figure legend 1:1,5:1,10:1.

**Reported-versus-comparator:** Prose gives matching ratios 1:1, 1:5, and 1:10. The figure legend headed Matching ratio gives 1:1, 5:1, and 10:1. The legend and caption do not name numerator/denominator group order. The figure title concerns HRs for metabolic surgery versus no surgery, which defines the HR comparison, not necessarily the matching-ratio convention.

**Reasoning procedure:** Conditional only. Ratios conflict if both locations use the same named-group order. Neither of the compared ratio lists specifies that order, so this alignment is not established. Reciprocal strings are directly observed. Same-order alignment is an unsupported input assumption; a plotting-label mistake is not established.

**Calculation:** 1:5 and 5:1, and 1:10 and 10:1, are reciprocal ordered ratios. Reversing numerator/denominator group convention makes them equivalent descriptions of the same group-size allocation. No HR mismatch is inferred from the legend notation.

**Alternative source-grounded interpretations:** Prose may use surgery:nonsurgery and the legend nonsurgery:surgery. That gives coherent reciprocal notation without different analyses. The underlying reference HRs and named surgery-versus-control treatment contrast do not determine ratio numerator order. Missing definition/input: Explicit surgery:nonsurgery or nonsurgery:surgery group order for each ratio list and the allocation associated with each figure color.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Treating the reciprocal strings as conflicting allocations requires unsupported same-order alignment. The package does not define both lists’ orders, and the alternative reverse-order convention can reconcile them; residual discrepancy cannot be settled. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the legend-to-sensitivity-dataset group order. It is bounded to the printed comparison and named unresolved definition. Checker provenance: GRAPH-P1-01; S237–S356; cross-source noncandidate ratio-order observation.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the legend-to-sensitivity-dataset group order with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: What named-group order is used by each matching-ratio list, and which surgery/control allocation does each eFigure 4 legend color represent?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C018 — Precision-conditional HbA1c eligibility boundary

**Status:** Pending Human Adjudication

**Candidate statement:** The protocol’s >6.4% and report’s ≥6.5% surgical HbA1c predicates differ conditionally for unmedicated finer-precision values, but agree on a one-decimal grid. Actual screening differences are not established.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original surgical HbA1c threshold vs REPORT main surgical eligibility threshold

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** A prospective PLAN statement is compared with its matched REPORT statement; context-only plan statements add no P_P relationship.

**Classification ambiguity:** Actual storage/selection precision is missing; conditional threshold mismatch, not an established population or protocol-compliance difference.

**Exact source locations:** [PLAN PDF p. 2, surgical inclusion criterion b](../joi190103supp2_prod.pdf#page=2); [main PDF p. 2, Surgical Patients criterion 3](../jama_aminian_2019_oi_190103.pdf#page=2); [main p. 3, Figure 1 eligibility footnote b](../jama_aminian_2019_oi_190103.pdf#page=3), all directly rendered and inspected.

**Source evidence:** PLAN surgical HbA1c>6.4% or diabetes medication; REPORT HbA1c≥6.5% or medication.

**Reported-versus-comparator:** PLAN surgical inclusion says HbA1c >6.4% or on diabetes medication. REPORT surgical inclusion says HbA1c 6.5% or greater or taking at least one diabetes medication. Figure 1 footnote b describes exclusion below 6.5% without diabetes medication.

**Reasoning procedure:** This is a conditional comparison of explicitly printed numerical predicates for the same surgical eligibility context. For medication users the medication alternative may make both true. For unmedicated persons the two HbA1c predicates are equivalent on a 0.1% grid but not universally equivalent for finer-precision values. The rule does not presume actual measurement precision or changed enrolled populations. The two printed rules are directly observed. The 6.45 example and one-decimal equivalence are logical diagnostics. Actual screening differences, population changes, and protocol compliance are not inferred.

**Calculation:** An unmedicated value 6.45% satisfies >6.4% and fails ≥6.5%. On one-decimal values, the smallest value above 6.4 is 6.5, so the rules agree. The possible distinguishing interval is (6.4,6.5)%; neither endpoint itself creates a difference.

**Alternative source-grounded interpretations:** The criteria may be intended as equivalent shorthand for one-decimal laboratory results. No supplied precision definition proves or disproves that reading. The source does not establish any affected participant count. Missing definition/input: HbA1c storage precision, the precision and rounding used by eligibility selection, whether selection acted on rounded/displayed or full-precision values, and whether any unmedicated records were in the distinguishing interval.

**Mechanical evidence recheck:** Direct-source Poppler renders of all cited pages were visually inspected; reusable text was a locator, not final authority. Direct source confirms >6.4 versus ≥6.5 for the same surgical criterion, reproducing the registered conditional comparison while preserving one-decimal equivalence and missing actual selection precision. The independent quality audit covered this ID and confirmed its present classification and evidence state.

**Quality-control relevance:** This comparison concerns the identity or faithful display of the surgical HbA1c eligibility boundary and precision. It is bounded to the printed comparison and named unresolved definition. Checker provenance: HBA1C_THRESHOLD_PRECISION; cross-source alias printed as HBA 1 C_THRESHOLD_PRECISION; numeric no-candidate precision observation.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, an evidence extractor or systematic review could copy the surgical HbA1c eligibility boundary and precision with an incorrect value, unit or identity. The supplied package does not establish that this happened or changed a conclusion.

**Human verification steps:** Reopen the linked source pages, confirm the quoted quantities and comparison identity, and resolve the named definition before deciding whether any reporting action is warranted. Exact question: Did eligibility selection use a one-decimal HbA1c grid or finer/full-precision values, and were >6.4% and ≥6.5% intended to implement the identical boundary for unmedicated patients?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Small preventable numeric or labeling defects may matter when later evidence products copy them. Absolute differences and baseline percentages can enter extraction tables; rate units, endpoint composition, table identity and group-order labels can determine whether quantities are compared appropriately. Eligibility precision and analytic denominators can determine which population an extractor describes. These are conditional reasons for human quality control. This review does not show that any candidate propagated, altered a meta-analysis, changed the paper’s conclusions or caused harm.

## Limitations and Missing Definitions

All 39 direct-source pages and all registered numeric/statistical relationships were mapped and reviewed. No scientific source-coverage gap remains. Limitations below describe what the supplied package cannot resolve; they do not authorize omitted candidates or invented inputs.

- C001–C005: unrounded group risks and the precise ARD point-estimation/risk-set rule. Bootstrap CI methodology alone does not specify a different point estimand.
- C006–C008 and C010: exact percentage denominator, weighting and rounding/formatting sequence. Two-stage rounding is a concrete possible reconciliation for C007/C008, not an observed production rule.
- C009: intended signed versus absolute standardized-difference convention and complete scaling/pooled-SD implementation; negative signs alone suffice for the definition comparison.
- C011: medication analytic inclusion/availability rule and any supplied equality requirement with enrolled cohort. The registered alignment is unsupported; no missing-person error is established.
- C012: intended meaning of the percentage suffix on person-time rates; event/person-time totals are unavailable for independent raw rate reconstruction.
- C013: whether a separately defined five-component analysis was intended in the primary E-value interpretation. No external E-value conversion formula was imported.
- C014: intended numbered table reference and any historical numbering explanation.
- C015: intended named matching direction, implementation code and any disclosed change. No protocol violation is established.
- C016: intended lower vertical-axis value/extent and annotation-versus-tick intent. The source glyph itself is visually confirmed.
- C017: explicit numerator/denominator group order for both ratio lists and legend-color allocation. No wrong sensitivity HR or implemented ratio is established.
- C018: actual stored HbA1c precision, selection rounding and whether any unmedicated records lay strictly between 6.4% and 6.5%. One-decimal rules agree; no affected count or population change is established.

Some statistical relationships lack exact test statistics, standard errors, covariance, degrees of freedom, variance estimator or full CI-production rules. Graph-only confidence endpoints and trend-band levels cannot always be read as exact scalars. These limits were recorded rather than resolved by assuming conventions. The review does not reconstruct raw data, bootstrap samples, person-time or model fits. Legacy asset engine/version metadata was incomplete for some reusable images/text, but present-run source matching and targeted direct-source inspection support their use. No scientific conclusion, clinical consequence or downstream propagation is adjudicated.

The user requested the current provider. The unchanged original validator expects literal openrouter; the documented auxiliary copy changes only that expected provider to CURRENT_SESSION_DEFAULT, retaining every scientific/integrity/coverage check. [Validation outcomes](review_1_6/validation_override/validation_results.md) record the original and adjusted results separately. Completion requires provider-adjusted PASS and allows only the documented provider expectation to differ in the baseline. No provider/authentication configuration or original helper was modified.


## Human Adjudication Checklist

- Review all 18 stable cards, including C011/C017 with unsupported alignment inputs; do not treat retain/discuss as decisions.
- Confirm the linked source values and document roles, then check endpoint, population, time, estimator, measure, unit and group-order identity.
- Resolve the card-specific missing definition and evaluate its explicit source-grounded alternative. For C007/C008 assess intermediate rounding; for C018 assess medication status and selection precision.
- Keep observed printed facts separate from diagnostics and proposed production explanations. A clarified small reporting defect need not imply changed conclusions.
- Enter validity, importance, action, initials and notes in the blank human fields. Only the human reviewer determines any final correction or disposition.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Source integrity and durable artifacts

Three source hashes and all 90 reused-asset hashes were recomputed after scientific review and are unchanged. Original workflow/configuration-control hashes also match. See [integrity check](review_1_6/quality/integrity_check.md), [source before hashes](review_1_6/source_hashes_before.sha256), [source after hashes](review_1_6/source_hashes_after.sha256), [reused before hashes](review_1_6/reused_artifact_hashes_before.sha256) and [reused after hashes](review_1_6/reused_artifact_hashes_after.sha256). All supplied sources and pre-existing audit artifacts were preserved. The [stable ledger](review_1_6/candidate_ledger.md), [recheck](review_1_6/verification/evidence_recheck.md), [quality audit](review_1_6/quality/evidence_quality_audit.md) and this report contain the identical C001–C018 set. The [limitations record](review_1_6/limitations.md) preserves the bounded unresolved definitions.

### Tooling and routing

Direct local PDF information/text/rendering, hashing and OCR tools were available; no fallback Python environment was needed or created. Present-run PDF work used CPU-only Poppler 26.01.0. Tool/version/derivative commands and final removal status are documented in the [tooling record](review_1_6/tooling_record.md). No GPU or web source was used. Routing preflight records PASS, interactive CLI execution, fixed gpt-6.1-sol role routing, and all nine named presets verified. The coordinator and all scientific specialists produced responses; ordinary specialists used medium effort, statistical/recheck/audit roles used high.

The provider remains the user-requested current session default, recorded truthfully as CURRENT_SESSION_DEFAULT. The bundled validator’s literal openrouter requirement conflicts with that instruction. The original helper is unchanged; a [documented copy and one-string diff](review_1_6/validation_override/README.md) alter only the provider expectation. Separate [validation outcomes](review_1_6/validation_override/validation_results.md) preserve the unmodified baseline and the provider-adjusted result; the [canonical validation JSON](review_1_6/review_validation.json) identifies the adjusted completion check. An adjusted result is never represented as an unmodified baseline result.

### Complete agent execution

The execution used 18 actual agents, including the coordinator, with fresh distinct runtime IDs for every mandatory specialist stage. Eight fresh statistical agents cover the four disjoint shards in two passes. One optional medium-effort numeric tail agent confirmed the last three hierarchical risk-set records. Exact execution records follow; every model is gpt-6.1-sol.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a1287e-6025-7ab1-bc15-d6d8c40ceebd | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a1287f-6a5d-7b22-829b-dc1eace1af13 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12882-140f-7461-abff-e4b82f713701 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12882-33e4-7cd2-9bdd-f27b095e87fc | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a12886-0eb9-7ba0-bdcd-bccaf6412cd7 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12886-30d5-7c72-ad44-dd0cfbe300b9 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12886-5cb4-74b3-b751-c0153f581281 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support_a | 01a12886-83ee-7ac0-afea-c841f69920e7 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support_a.md |
| statistics_pass_1_support_b | 01a12886-ab23-7d51-9109-ce84b0abfc61 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support_b.md |
| statistics_pass_1_graph | 01a12886-d3a5-7901-bcca-fa2475b4b9ee | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_graph.md |
| evidence_rechecker | 01a1288e-8403-7051-b0a2-9dde819d0e0a | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| numeric_consistency_tail | 01a1288f-6d3c-7061-8f37-fde691f58c4c | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_tail_N121_N123.md |
| statistics_pass_2 | 01a12893-27ee-7b01-8b06-12a270139f0a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_support_a | 01a12893-5344-7fb2-a4f4-e1a8e8ac9e7c | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support_a.md |
| statistics_pass_2_support_b | 01a12893-81b4-72f3-b8a7-0148d9978ace | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support_b.md |
| statistics_pass_2_graph | 01a12893-ae96-73e1-b2e5-d1025d6d004a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_graph.md |
| quality_control_auditor | 01a12897-ea72-7dc3-a2e8-fa4228d5574f | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a1289d-9b30-70f0-b3f7-2b5d937c986c | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

The planning target is package-specific and does not limit source coverage or candidate discovery. The coordinator finalized finish/elapsed/status immediately after complete Markdown assembly; local rendering and mechanical validation are outside that review window.

- **Target basis:** Three text-layer PDFs covering 39 unique pages, with source-matched reusable text for every page and no Office conversion or fresh OCR burden. Dense cohort/outcome and longitudinal tables, 21 existing rendered pages, sensitivity analyses and an original protocol plus amendment require new relationship mapping. Ten fresh specialist stages include two distinct high-effort statistical passes, evidence recheck and quality audit. The 25–40 minute target permits these agent waves without assuming a candidate count.
- **Total source units:** 39
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T01:06:33Z
- **Finished UTC:** 2026-10-11T01:43:01Z
- **Observed elapsed minutes:** 36.47
- **Target status:** MET_TARGET
- **Exceedance causes:** None
