# Independent initial inclusion screen

Fresh screener runtime `01a128e8-3ee6-74b0-9150-548d0b31afea`; role `qc161_inclusion_screener`, gpt-6.1-sol/high. Exact assigned scope: all 12 findings in `checkers/numeric_consistency.md` (2), `checkers/cross_source_consistency.md` (5), and `checkers/statistical_pass_1.md` (5). Read QUALITY_CONTROL_SCOPE.md and the complete review contract, both new evidence maps, and every finding. Decisions below apply all four inclusion criteria independently and apply comparison tiers before the threshold. No historical conclusions, web, external literature, unpermitted Python, or human dispositions used.

Source confirmation: independently visually read current exact-source Poppler renders of main PDF pp.1,4,6,8; protocol PDF pp.31,33,34; results PDF pp.2,7. Reread direct `pdftotext -layout` output from main p.7, protocol p.30, and all nine results-supplement pages; searched the entire direct main-PDF extraction for Cox/hazard, mortality, subgroup, disease, and weaning passages and read all matching contexts. Viewed the reusable results-supplement p.9 image in full; its title matches the current direct-source title and its overall day-90 log-rank result is P=.37. The complete new maps and direct report reads confirm the reported analysis set and supplied results inventory. Existing renders remain untouched; no derivative was created by this stage. Direct tooling: Poppler 26.01.0 CPU as recorded in tooling_record.md; the reused p.9 image has no recorded renderer version.

Coordinator registration has assigned the stable C IDs shown below to the five independently included issues. Several INCLUDE rows belong to one conceptual issue; this preserves every qualifying checker provenance without creating separate candidates for repeated observations. There is exactly one screening table.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-002 | cross_source_consistency_reviewer | initial | SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | — |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-004 | cross_source_consistency_reviewer | initial | SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | — |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-ST1-003 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-004 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-ST1-005 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C002 |

## Finding-by-finding justifications

- **F-NUM-001:** The exact main abstract/narrative print −8.7 while Table 2 prints −8.5 for the same abstract-reported day-7 respiratory-failure contrast, and their disjoint half-unit intervals leave the reported absolute effect to extract unclear.
- **F-NUM-002:** The exact eTable 4 mortality row prints 54/254 and 50/276 with absolute difference −3.8, whereas its source-described proportion contrast is −3.14390049 percentage points and even conservative half-unit input intervals cannot reach the displayed effect.
- **F-XS-001:** This independently reproduced repeated-location effect discrepancy meets the threshold and belongs to the same issue as F-NUM-001, retaining every cited report location.
- **F-XS-002:** Closed half-unit intervals [.005,.015] and [.015,.025] intersect at .015, so the mandatory display-precision rule screens out P=.01 versus P=.02 without assuming an unreported rounding convention or chi-square variant.
- **F-XS-003:** The explicit severe-reintubation acidosis item changes from plan pH<7.35 to report pH<7.25, changing a planned decision rule underpinning the primary endpoint without an immediate amendment explanation.
- **F-XS-004:** The plan's backward-selected Cox passage describes variables associated with reintubation, does not expressly specify a randomized-treatment effect or forced treatment term, and therefore does not establish an omitted adjusted treatment HR or replacement of the explicitly planned chi-square primary comparison.
- **F-XS-005:** The plan expressly commits to primary-outcome analyses by disease and weaning-test factors, whereas the complete supplied report identifies only PaCO2 subgroup analyses and provides no explanation resolving the prespecified primary subgroup set.
- **F-ST1-001:** Its absolute-difference subpart is reproduced and joins F-NUM-001/F-XS-001, but its P-value subpart is excluded under ROUNDING_OR_DISPLAY_PRECISION and cannot create an S_C relationship.
- **F-ST1-002:** The exact-source nonhypercapnic day-90 mortality arithmetic discrepancy joins F-NUM-002 and is a within-row effect-identity check, rather than a peripheral comparison between secondary displays.
- **F-ST1-003:** The plan explicitly includes ICU mortality in between-treatment Kaplan–Meier/log-rank comparisons, but the report supplies the abstract-reported ICU result as chi-square P=.25 and only a distinct overall day-90 log-rank result, leaving the planned/reported ICU analysis identity unresolved.
- **F-ST1-004:** The absent disease/weaning primary subgroup families join F-XS-005 as one repeated planned-analysis reporting pattern, without inferring subgroup effects or treatment heterogeneity.
- **F-ST1-005:** The exact severe-failure pH-threshold discrepancy joins F-XS-003, retaining the supplementary criterion counts as corroborating report context rather than another independent inconsistency.

## Included conceptual issues for registration

These labels are working descriptions, not stable C IDs. The coordinator registers one candidate per issue in source order and writes that C ID into every corresponding INCLUDE row. Comparators below retain all finding locations; corroborating sources do not add relationship types.

### Respiratory-failure absolute difference

**Finding IDs:** F-NUM-001, F-XS-001, F-ST1-001. **Review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W. **Document roles:** REPORT main article abstract/narrative versus REPORT main article Table 2. **Focus:** A/B.

**Locations:** [main p.1 abstract Results](../../../jama_thille_2019_oi_190108.pdf#page=1), [main p.6 Secondary Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=6), [main p.8 Table 2 respiratory-failure row and population headings](../../../jama_thille_2019_oi_190108.pdf#page=8). Additional cited REPORT context: [main p.4 statistical methods](../../../jama_thille_2019_oi_190108.pdf#page=4), [results p.2 eTable 1](../../../joi190108supp2_prod.pdf#page=2), [results p.6 hypercapnic outcomes](../../../joi190108supp2_prod.pdf#page=6), [results p.7 nonhypercapnic outcomes](../../../joi190108supp2_prod.pdf#page=7).

**Reproduction and threshold:** The source prints −8.7 (95% CI −15.2 to −1.8) in abstract/narrative and −8.5 with the identical CI in Table 2. Their intervals [−8.75,−8.65] and [−8.55,−8.45] do not intersect. Counts give 100×(70/339−88/302)=−8.4901053 percentage points. This is a matched key-secondary result by abstract inclusion; no separate estimator or population distinguishes the repeated effect statements. The named extracted quantity is the overall day-7 respiratory-failure absolute treatment difference. Counts favor the table computation but do not establish the intended repeated reported estimate or explain the narrative computation, so the two reported effects remain relevant to extraction.

**Qualifying limit:** The main/supplement P=.01/.02 subpart is screened out because its half-unit intervals overlap at .015; do not carry the P discrepancy into the candidate title, inconsistency claim, or All relationships. Supplement counts corroborate the endpoint and do not establish a cross-report discrepancy. No adjusted estimate is compared with a crude calculation as though it must be crude.

### Severe-acidosis threshold in the primary reintubation rule

**Finding IDs:** F-XS-003, F-ST1-005. **Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R. **Document roles:** PLAN protocol severe-reintubation definition versus REPORT main Outcomes definition. **Focus:** D.

**Locations:** [protocol p.30 section 5.4 start](../../../joi190108supp1_prod.pdf#page=30), [protocol p.31 severe-failure criteria](../../../joi190108supp1_prod.pdf#page=31), [main p.4 Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=4). Affected/corroborating REPORT context: [main p.8 primary Table 2 row](../../../jama_thille_2019_oi_190108.pdf#page=8), [results p.2 severe respiratory-acidosis counts 12 and 9](../../../joi190108supp2_prod.pdf#page=2).

**Reproduction and threshold:** Both sources require at least two severe respiratory criteria; the corresponding acidosis item is pH<7.35 with PaCO2>45 in the plan and pH<7.25 with PaCO2>45 in the report. These are different specified cutoffs, not rounded measurements. The less-severe secondary respiratory-failure definition is separately pH<7.35 in both sources and cannot resolve the severe-item comparison. The primary day-7 reintubation decision rule is a qualifying planned rule; which threshold operated is not disclosed by the supplementary criterion counts or immediate text. No actual patient recategorization, changed event count, clinical preference, or undisclosed amendment is asserted.

### Planned versus reported ICU mortality comparison

**Finding IDs:** F-ST1-003. **Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R. **Document roles:** PLAN protocol mortality treatment-comparison specification versus REPORT main ICU mortality methods/result. **Focus:** D.

**Locations:** [protocol p.34 section 6.3 continuation](../../../joi190108supp1_prod.pdf#page=34), [main p.4 Statistical Analysis](../../../jama_thille_2019_oi_190108.pdf#page=4), [main p.1 abstract ICU mortality](../../../jama_thille_2019_oi_190108.pdf#page=1), [main p.8 Table 2 ICU mortality](../../../jama_thille_2019_oi_190108.pdf#page=8), [results p.9 survival eFigure](../../../joi190108supp2_prod.pdf#page=9). Entire main pp.1–11 and results pp.1–9 considered for availability of a separately identified ICU log-rank output.

**Reproduction and threshold:** The plan's unconditional Kaplan–Meier/log-rank sentence explicitly lists ICU mortality and says comparisons are between treatment groups; the report explicitly assigns ICU mortality to chi-square and reports 21/339 versus 26/302, difference −2.4 (95% CI −6.7 to 1.7), P=.25. The supplied survival figure is overall extubation-to-day-90 log-rank P=.37, not a separately identified ICU-death comparison. ICU mortality qualifies as key secondary because it appears in the abstract. The named affected quantity is the analysis identity of its P=.25 and the availability of its planned log-rank comparison. Distinct coherent tests do not resolve an explicit plan/report specification difference or supply a change explanation. Do not infer a log-rank P value from final event counts, and do not append conditional mortality Cox-model omissions to this issue.

### Prespecified disease and weaning-test primary subgroup analyses

**Finding IDs:** F-XS-005, F-ST1-004. **Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R. **Document roles:** PLAN protocol primary-subgroup commitments versus REPORT supplied subgroup analysis set. **Focus:** D.

**Locations:** [protocol p.34 section 6.4](../../../joi190108supp1_prod.pdf#page=34), [main p.4 subgroup methods](../../../jama_thille_2019_oi_190108.pdf#page=4), [main p.7 subgroup results](../../../jama_thille_2019_oi_190108.pdf#page=7), [main p.8 Figure 3](../../../jama_thille_2019_oi_190108.pdf#page=8), complete [results supplement pp.1–9, contents p.1](../../../joi190108supp2_prod.pdf#page=1), [eTable 3 p.6](../../../joi190108supp2_prod.pdf#page=6), [eTable 4 p.7](../../../joi190108supp2_prod.pdf#page=7).

**Reproduction and threshold:** The plan states main and secondary outcome subgroup analyses will be performed in patients with underlying cardiac/respiratory disease and by T-piece versus minimum pressure-support weaning test, in addition to PaCO2. The supplied report's subgroup definition and outputs concern PaCO2 only, including interaction P=.25 and primary stratum differences −12.9 and −5.0. Baseline disease/weaning rows provide no primary subgroup effects. The missing prespecified primary subgroup result set qualifies directly under focus D; it is not a peripheral baseline comparison or an inference from conventional but unreported methods. Both factor families form one repeated omission pattern. Register only the primary-outcome subgroup aspect, without extending the issue to omission of all non-key secondary subgroup analyses or inferring subgroup estimates.

### Nonhypercapnic day-90 mortality absolute difference

**Finding IDs:** F-NUM-002, F-ST1-002. **Review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W. **Document roles:** REPORT eTable 4 row/counts versus REPORT same-table absolute-difference entry. **Focus:** A/B/C.

**Locations:** [results p.7 eTable 4 headings and final mortality row](../../../joi190108supp2_prod.pdf#page=7); contextual [main p.4 categorical and adjusted-primary analysis descriptions](../../../jama_thille_2019_oi_190108.pdf#page=4).

**Reproduction and threshold:** The source shows control 54 (21%) of n=254 and intervention 50 (18%) of n=276 with absolute difference −3.8 (95% CI −9.9 to 3.6), P=.3626. The source-described proportion difference is 100×(50/276−54/254)=−3.14390049 percentage points. Even giving each count and denominator a conservative continuous half-unit interval yields [−3.596663,−2.691302], disjoint from the printed difference interval [−3.85,−3.75]. Neighboring binary contrasts use the stated arm proportions and no adjusted day-90 mortality estimator is identified; main adjustment descriptions explicitly concern the primary reintubation outcome. The named extracted value is the nonhypercapnic day-90 mortality absolute effect. This within-row computation-identity check does not compare peripheral secondary displays across locations. An unreported model is a possible human explanation, not established evidence requiring MODEL_VERSUS_CRUDE exclusion; no raw data or CI symmetry assumption is used. The final nonsignificance conclusion is not claimed to change.

## Detailed excluded-finding note

**F-XS-004:** Exact protocol p.33 first defines a clear treatment comparison of primary day-7 proportions by chi-square. The later Cox paragraph selects variables associated with reintubation at P<.20 and reports adjusted associations after backward selection; it does not state a forced treatment term or identify a randomized-treatment hazard-ratio estimand. Main pp.4,7 report the planned chi-square treatment comparison, log-rank curves, a treatment-effect logistic adjustment and post hoc hospital adjustment. Absence of a predictor-selection Cox output from the supplied report is acknowledged, but identifying it as a missing primary treatment-effect HR or an alternative prespecified treatment-effect analysis requires a mapping the package does not establish. The finding's affected adjusted time-to-reintubation treatment result therefore depends on an unstated specification. This differs from the included subgroup and ICU comparisons, where the prospective treatment/outcome comparisons are expressly named. No claim that an auxiliary prognostic result was performed or not performed is made.

## Counts and limitations

12 findings screened; 10 INCLUDE rows consolidate into 5 distinct issues; 2 SCREENED_OUT findings: ROUNDING_OR_DISPLAY_PRECISION=1, CONDITIONAL_OR_UNREPORTED=1. The P-value subpart of F-ST1-001 is additionally excluded within that included combined finding; it is not another independent finding or table row. Included conceptual domains: statistical_results=2 and protocol_report=3. No scientific source-confirmation gap, source modification, or local tool limitation. Absence of a separate supplied SAP/amendment, raw participant data, and exact table estimator/test settings remains an evidence limitation and is not filled by assumptions. All included issues await coordinator registration, mechanical recheck, independent audit, and human adjudication.
