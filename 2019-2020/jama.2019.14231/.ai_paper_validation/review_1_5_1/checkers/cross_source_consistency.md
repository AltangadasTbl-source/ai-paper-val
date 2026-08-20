# Cross-Source Consistency Check

## Scope and method

This checker independently reviewed the `cross-001` scope in `coverage_manifest.md`: every matched occurrence assigned to N001, N005-N013, N017-N019, N021, N025, N029, N035-N038 and S001-S008, S011-S021, and S023-S025. The review used the current canonical numeric and statistical inventories, the current main/support mapping parts and evidence maps, reusable extraction only as a locator, and direct confirmation against the three supplied PDFs. Old candidate, checker, verifier, critic, adjudication, and report outputs were not used as scientific inputs.

Before comparing printed values, this review matched population, time, outcome, contrast, model, analysis set, measure, scale, unit, reference group, and displayed precision. Rounded narrative values, separately bootstrapped absolute-risk differences, outcome-specific risk sets, available-measurement denominators, and opposite but stated contrast orientations were not treated as differences.

**Assigned relationships checked:** 42 (20 numeric/reporting relationships and 22 statistical relationships).

**Qualifying proposals:** 3. These are pending human review only; this checker assigns no stable candidate IDs, severity, verdict, or adjudication.

## Qualifying proposals

### CROSS-P001 — Protocol reverses the printed 1:5 matching direction

**Category:** Cross-document numeric inconsistency.

**Assigned relationship IDs:** N001.

**Exact linked locations:** [DOC-003, protocol PDF p. 3](../../../joi190103supp2_prod.pdf#page=3), “(3) Matching Process”; [DOC-001, main article PDF p. 1](../../../jama_aminian_2019_oi_190103.pdf#page=1), Abstract; [DOC-001, main article PDF p. 3](../../../jama_aminian_2019_oi_190103.pdf#page=3), Figure 1 caption and flow diagram; [DOC-001, main article PDF p. 4](../../../jama_aminian_2019_oi_190103.pdf#page=4), Methods.

**Printed values and comparator:** The protocol says, “Each non-surgical patient will be matched ... to five (5) surgical patients.” The main article says that 2,287 surgical patients were “matched 1:5 to nonsurgical patients,” resulting in 11,435 control patients; Figure 1 likewise reports “2,287 Patients undergoing metabolic surgery included” and “11,435 Matched (1:5) nonsurgical patients included.” The Methods specify that each surgical patient was matched to 5 nonsurgical patients.

**Comparison logic:** For the same study cohort and matching process, the main article’s displayed counts give 11,435 / 2,287 = 5. The article’s wording and counts therefore identify five nonsurgical controls per surgical patient. The protocol sentence instead states the reverse one-nonsurgical-to-five-surgical direction, which would describe a 1:5 allocation in the opposite direction and cannot yield the displayed 2,287 surgical and 11,435 nonsurgical matched groups.

**Supported alternatives:** The protocol may contain a directional wording/transcription error rather than a description of the executed analysis. The protocol’s intended convention could also differ from its sentence-level grammatical direction; the printed main-study counts nonetheless directly establish the direction used in the reported matched cohort.

**Human verification steps:** Confirm the protocol source version and whether the sentence was superseded before analysis. Confirm the MatchIt call or matching output, then determine whether the protocol should say “each surgical patient ... to five nonsurgical patients” or should otherwise state the allocation direction unambiguously.

### CROSS-P002 — Medication-comparison test label conflicts between the main figure and supplement table

**Category:** Measure, label, or scale inconsistency.

**Assigned relationship IDs:** S013 and S025.

**Exact linked locations:** [DOC-001, main article PDF p. 4](../../../jama_aminian_2019_oi_190103.pdf#page=4), Methods; [DOC-001, main article PDF p. 10](../../../jama_aminian_2019_oi_190103.pdf#page=10), Figure 5 caption; [DOC-002, Supplement 1 PDF p. 12](../../../joi190103supp1_prod.pdf#page=12), eTable 8 title, medication rows, and footnote.

**Printed values and comparator:** The main Methods say that “a 2-sample proportions test was used” for medication proportions at 1, 2, 5, and 8 years. Figure 5 says, “P values from a Fisher exact test are also displayed comparing the proportion of surgical and nonsurgical patients taking drug at 8 years.” For the matched 8-year medication comparisons, eTable 8 prints the same six result family P values: non-insulin medication, renin-angiotensin inhibitor, other antihypertensive medication, lipid-lowering medication, and aspirin each `<0.001*`; insulin `0.008*`. Its footnote says “two-sample proportions test was used for medication data at each time point.”

**Comparison logic:** Figure 5 expressly directs its 8-year statistical comparison and sample size to eTable 8 and eTable 10. The treatment groups, medication outcomes, time point, and displayed P-value family align. Yet the figure calls those displayed 8-year P values a Fisher exact test, while both the article Methods and eTable 8 call the medication comparisons a two-sample proportions test. A Fisher exact test and a two-sample proportions test are distinct named test procedures, so the test-method label is not reconciled by rounding or by the P-value display precision.

**Supported alternatives:** The authors may have used a Fisher exact test specifically at year 8 and two-sample proportions tests at the other time points, with the eTable 8 footnote intentionally abbreviated. Conversely, the Figure 5 caption may be the mislabeled location. The supplied package does not state which test generated each exact 8-year P value.

**Human verification steps:** Inspect the analysis code or statistical-analysis record for each Figure 5 8-year comparison. Confirm whether the eTable 8 year-8 P values were generated by Fisher exact or a two-sample proportions test, and harmonize the Methods, figure caption, and eTable footnote accordingly.

### CROSS-P003 — Time-varying-HR narrative names eTable 4, while the printed result is eTable 7

**Category:** Measure, label, or scale inconsistency.

**Assigned relationship IDs:** N038 and S024.

**Exact linked locations:** [DOC-002, Supplement 1 PDF p. 6](../../../joi190103supp1_prod.pdf#page=6), eTable 4; [DOC-002, Supplement 1 PDF p. 10](../../../joi190103supp1_prod.pdf#page=10), eTable 7; [DOC-002, Supplement 1 PDF p. 19](../../../joi190103supp1_prod.pdf#page=19), “B. Time-varying hazard ratios” narrative and repeated eTable 7.

**Printed values and comparator:** On Supplement 1 p. 19, the time-varying-HR narrative says, “eTable 4 displays adjusted hazard ratios and 95% confidence intervals at 2, 5, and 8 years after the index date.” Directly below, the table is headed “eTable 7. Time-Varying Hazard Ratios and 95% CIs at 2, 5, and 8 Years...” and reports, for example, primary HRs `0.57 (0.49, 0.65)`, `0.78 (0.66, 0.93)`, and `0.79 (0.64, 0.97)`. The duplicate on p. 10 is also headed eTable 7. In contrast, eTable 4 on p. 6 is headed “Cause-Specific Event Rates (%) per 100 Patient-Years” and reports rates, not time-varying HRs.

**Comparison logic:** The narrative, its stated measure (adjusted HRs with 95% CIs), and its stated times (2, 5, and 8 years) match eTable 7 exactly. eTable 4 instead has a different measure (event rate per 100 patient-years) and table title. Thus the narrative’s `eTable 4` cross-reference does not identify the printed table that contains the described results.

**Supported alternatives:** This may be a cross-reference-numbering error confined to the p. 19 narrative. It is also possible that an earlier supplement layout had a different table number, but the supplied final PDF contains eTable 7 at both locations.

**Human verification steps:** Verify the final submitted/production supplement table numbering. Correct the p. 19 cross-reference to eTable 7 if that numbering is authoritative, and confirm that no separate time-varying-HR result is intended to be cited as eTable 4.

## Complete assigned relationship coverage

| Assigned ID | Matched-source comparison performed | Result |
|---|---|---|
| N001 | Main cohort counts and 1:5 direction versus protocol matching definition. | CROSS-P001. |
| N005 | Main Table 1 baseline columns; no same-result conflicting support occurrence was assigned. | COMPLETE — no qualifying cross-source difference. |
| N006 | Primary event counts, 8-year incidences, ARD, and control-minus-surgery direction across abstract, Results, Table 2, Figure 2, and eTable 5. | COMPLETE — matched after precision/context alignment. |
| N007 | Secondary-composite counts, incidences, and ARD across Results, Table 2, Figure 2, and eTable 5. | COMPLETE — matched. |
| N008 | Mortality counts, incidence, ARD, and HR across abstract, Results, Table 2, Figure 3, and eTable 5/6. | COMPLETE — matched. |
| N009 | Heart-failure risk set/incidence/ARD across Table 2, Figure 3, and eTable 5. | COMPLETE — no difference; the 12.9-point ARD is separately bootstrapped, not direct subtraction of rounded incidences. |
| N010 | Coronary-disease risk set/incidence/ARD across Table 2, Figure 3, and eTable 5. | COMPLETE — matched. |
| N011 | Cerebrovascular-disease risk set/incidence/ARD across Table 2, Figure 3, and eTable 5. | COMPLETE — matched. |
| N012 | Nephropathy risk set/incidence/ARD across Table 2, Figure 3, and eTable 5. | COMPLETE — matched. |
| N013 | Atrial-fibrillation risk set/incidence/ARD across Table 2, Figure 3, and eTable 5. | COMPLETE — matched. |
| N017 | Eight-year mean weight reductions and 20.3-kg contrast versus eTable 8’s surgical-minus-nonsurgical estimate. | COMPLETE — magnitude matches; sign follows stated contrast orientation. |
| N018 | Figure 4’s 14.7% total-weight-loss and 1.1-point HbA1c contrasts versus eTable 8. | COMPLETE — values match after measure, scale, and contrast-direction alignment. |
| N019 | Ninety-day postoperative counts/percentages versus protocol amendment’s early-event definition. | COMPLETE — definition is compatible; no conflicting count or denominator is printed. |
| N021 | Figure 5 qualitative medication curves and referred eTable 8/eTable 10 numeric material. | COMPLETE — no unaligned curve value treated as a comparator; test-label conflict is recorded under S013/S025. |
| N025 | Overall fully adjusted Cox HR/CI/outcome-P/PH-P rows compared with main Table 2 and text. | COMPLETE — matched after distinguishing outcome P values from PH-assumption P values. |
| N029 | eTable 3 matched-cohort baseline denominator 11,435 versus eTable 10 medication-availability denominator 11,433 at year 0. | COMPLETE — different stated analysis sets; no rate/count confusion established. |
| N035 | Protocol composite membership and outcome-specific risk-set definitions versus main endpoint statements/Table 2. | COMPLETE — matched. |
| N036 | Protocol rate, cumulative-incidence, Cox, PH, imputation, multiplicity, and sensitivity definitions versus implemented reports. | COMPLETE — no concrete matched numeric inconsistency. |
| N037 | Protocol amendment adverse-event/E-value definitions versus main/supplement reporting. | COMPLETE — matched definitions; no conflicting value. |
| N038 | Supplement p. 19 time-varying-HR table cross-reference. | CROSS-P003. |
| S001 | Primary adjusted HR/CI/P across abstract, main Results/Table 2/Figure 2, and eTable 6. | COMPLETE — matched. |
| S002 | Secondary adjusted HR/CI/P across main Results/Table 2/Figure 2 and eTable 6. | COMPLETE — matched. |
| S003 | Mortality adjusted HR/CI/P across abstract, main Results/Table 2/Figure 3, and eTable 6. | COMPLETE — matched. |
| S004 | Heart-failure adjusted HR/CI/P across Table 2/Figure 3 and eTable 6. | COMPLETE — matched. |
| S005 | Coronary-disease adjusted HR/CI/P across Table 2/Figure 3 and eTable 6. | COMPLETE — matched. |
| S006 | Cerebrovascular-disease adjusted HR/CI/P across Table 2/Figure 3 and eTable 6. | COMPLETE — matched. |
| S007 | Nephropathy adjusted HR/CI/P across Table 2/Figure 3 and eTable 6. | COMPLETE — matched. |
| S008 | Atrial-fibrillation adjusted HR/CI/P across Table 2/Figure 3 and eTable 6, with time-varying context separated. | COMPLETE — matched. |
| S011 | Weight contrasts/intervals/P values across main Results/Figure 4 and eTable 8. | COMPLETE — matched after kg versus percent-loss measure alignment. |
| S012 | HbA1c contrast/interval/P value across main Results/Figure 4 and eTable 8. | COMPLETE — matched after contrast orientation. |
| S013 | Medication comparison P values and named test across main Methods/Figure 5 and eTable 8. | CROSS-P002. |
| S014 | Main subgroup claim versus eFigure 1 interaction model/result labels. | COMPLETE — matched. |
| S015 | Main PH-assumption statement versus eTable 6 PH P-value column and eTable 7 AF time-varying results. | COMPLETE — matched after distinguishing PH P values from outcome P values. |
| S016 | Fifteen-dataset sensitivity design/counts across main article and Supplement 1 eFigure 4 narrative. | COMPLETE — matched. |
| S017 | Five-imputation/Rubin-formula context across main Methods and protocol. | COMPLETE — matched. |
| S018 | Two-sided alpha, CI level, and exploratory-secondary-analysis statement across main Methods and protocol. | COMPLETE — matched. |
| S019 | Protocol per-100-patient-year rate definition versus eTable 4 rates/differences. | COMPLETE — matched; rate is not compared as a cumulative incidence or count. |
| S020 | Protocol cumulative-incidence definition versus eTable 5 endpoint/time/group values and main Table 2. | COMPLETE — matched. |
| S021 | Protocol time-varying-HR definition versus duplicate eTable 7 on pp. 10 and 19. | COMPLETE — duplicate values match. |
| S023 | Protocol E-value scale/nearest-null-CI definition versus Supplement 1 E-value values. | COMPLETE — matched; E-values were not compared numerically with HRs. |
| S024 | Time-varying-HR narrative table reference. | CROSS-P003. |
| S025 | eTable 8 longitudinal estimate/unit/CI/P alignment, including medication-test footnote. | CROSS-P002 for the named test only; all printed estimates, units, intervals, and P values otherwise matched their stated contexts. |

## Limitations

This review is limited to the supplied three PDFs and their source-linked current-run maps. The supplied package does not include the analysis code, matching object, protocol version history, or a statistical-analysis-plan amendment that could determine which of the conflicting matching or test-method labels is authoritative. These missing materials do not prevent identification of the printed cross-source differences above.
