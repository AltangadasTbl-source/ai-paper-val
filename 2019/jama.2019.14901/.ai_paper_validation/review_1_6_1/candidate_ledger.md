# Workflow 1.6.1 Candidate Ledger

Pending Human Adjudication. Five issues were registered only after independent inclusion screening of all 12 initial checker findings. Stable IDs are never deleted. Source order follows the first conflicting REPORT location: main abstract, main Outcomes, main Statistical Analysis mortality comparison, main subgroup specification, and supplementary eTable 4. Corroborating locations do not create additional relationships. All five evidence states are reproduced after the independent mechanical recheck; the final independent audit confirmed inclusion for all five.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main abstract and narrative vs REPORT main Table 2 | reproduced | CONFIRMED | F-NUM-001, F-XS-001, F-ST1-001 |
| C002 | protocol_report | P_R | P_R | PLAN protocol severe-reintubation definition vs REPORT main Outcomes definition | reproduced | CONFIRMED | F-XS-003, F-ST1-005 |
| C003 | protocol_report | P_R | P_R | PLAN protocol ICU mortality treatment-comparison specification vs REPORT main ICU mortality methods and result | reproduced | CONFIRMED | F-ST1-003 |
| C004 | protocol_report | P_R | P_R | PLAN protocol primary-subgroup commitments vs REPORT supplied subgroup analysis set | reproduced | CONFIRMED | F-XS-005, F-ST1-004 |
| C005 | statistical_results | S_W | S_W | REPORT results supplement eTable 4 counts and headings vs REPORT same-table absolute-difference entry | reproduced | CONFIRMED | F-NUM-002, F-ST1-002 |

## C001 — Day-7 respiratory-failure absolute difference differs within the main report

**Candidate statement:** The same overall day-7 respiratory-failure contrast is reported as −8.7 percentage points in the abstract/narrative and −8.5 in Table 2.
**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main abstract and narrative vs REPORT main Table 2
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-001, F-XS-001, F-ST1-001
**Classification rationale:** The conflicting effects are within one REPORT. Supplementary counts merely corroborate the endpoint; the P-value subpart was independently screened out and adds no S_C relationship.
**Classification ambiguity:** None
**Exact source locations:** [Main p.1 abstract](../../jama_thille_2019_oi_190108.pdf#page=1), [p.6 secondary narrative](../../jama_thille_2019_oi_190108.pdf#page=6), [p.8 Table 2 respiratory-failure row and headings](../../jama_thille_2019_oi_190108.pdf#page=8). Method context [main p.4](../../jama_thille_2019_oi_190108.pdf#page=4); corroborating [eTable 1 p.2](../../joi190108supp2_prod.pdf#page=2), [eTable 3 p.6](../../joi190108supp2_prod.pdf#page=6), [eTable 4 p.7](../../joi190108supp2_prod.pdf#page=7).
**Source evidence:** Main abstract and narrative give 21% versus 29%, difference −8.7 (95% CI −15.2 to −1.8), P=.01. Table 2 gives 70/339 versus 88/302, difference −8.5 with the same CI/P.
**Calculation:** 100×(70/339−88/302)=−8.4901053 percentage points. Display intervals [−8.75,−8.65] and [−8.55,−8.45] are disjoint.
**Affected result or extracted value:** Overall day-7 postextubation respiratory-failure absolute treatment difference, an abstract-reported key secondary result.
**Why context does not resolve it:** Both locations identify the same population, endpoint, time and unqualified contrast; no alternate estimator explains the repeated narrative effect.
**Alternative source-grounded interpretations:** Counts support the table computation; an unlabelled calculation or transcription could explain the narrative, but the package does not establish which.
**Human verification steps:** Compare every repeated source occurrence and establish the intended calculation/denominators. Do not carry P=.01 versus .02 into the candidate: its half-unit intervals overlap at .015.

## C002 — Severe-acidosis threshold differs between plan and reported reintubation rule

**Candidate statement:** The acidosis component of the two-component severe respiratory-failure rule uses pH<7.35 in the plan and pH<7.25 in the report, each with PaCO2>45 mm Hg.
**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol severe-reintubation definition vs REPORT main Outcomes definition
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-003, F-ST1-005
**Classification rationale:** A prospective PLAN operational decision rule is compared with a REPORT definition underlying the primary reintubation endpoint.
**Classification ambiguity:** No role ambiguity; no separate applicable amendment is supplied.
**Exact source locations:** [Protocol p.30 section 5.4 start](../../joi190108supp1_prod.pdf#page=30), [p.31 continuation](../../joi190108supp1_prod.pdf#page=31), [main p.4 Outcomes](../../jama_thille_2019_oi_190108.pdf#page=4). Affected/corroborating [main p.8 primary result](../../jama_thille_2019_oi_190108.pdf#page=8), [eTable 1 p.2 severe-acidosis counts](../../joi190108supp2_prod.pdf#page=2).
**Source evidence:** Both sources require at least two severe respiratory criteria for reintubation, but the corresponding pH cutoffs differ. The separate secondary respiratory-failure definition uses pH<7.35 in both and cannot resolve the severe-rule comparison.
**Calculation:** With PaCO2>45, the range 7.25≤pH<7.35 satisfies the plan's acidosis component but not the report's. One other matching component can therefore produce different rule eligibility; this is a specified-rule comparison only.
**Affected result or extracted value:** Operational decision rule underpinning primary day-7 reintubation (40/339 versus 55/302) and the related criterion description.
**Why context does not resolve it:** The severe definitions are explicit; no supplied amendment or report explanation establishes which cutoff applied.
**Alternative source-grounded interpretations:** An applicable later amendment or a reporting transcription may explain the contrast; neither is established. No actual patient reassignment or event-count change is inferred.
**Human verification steps:** Check dated operational rules and establish which severe-acidosis cutoff governed primary endpoint ascertainment.

## C003 — ICU mortality comparison is planned as log-rank and reported as chi-square

**Candidate statement:** The plan expressly includes ICU mortality in treatment-group Kaplan–Meier/log-rank comparisons, whereas the report assigns the abstract-reported ICU mortality result to chi-square and provides no separately identified ICU log-rank result.
**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol ICU mortality treatment-comparison specification vs REPORT main ICU mortality methods and result
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-003
**Classification rationale:** Explicit PLAN and REPORT statistical specifications for the same key secondary outcome are compared; coherent distinct tests do not establish an explanation of the change.
**Classification ambiguity:** No role ambiguity; no separate applicable SAP or amendment is supplied.
**Exact source locations:** [Protocol p.34 section 6.3](../../joi190108supp1_prod.pdf#page=34), [main p.4 Statistical Analysis](../../jama_thille_2019_oi_190108.pdf#page=4), [main p.1 abstract ICU mortality](../../jama_thille_2019_oi_190108.pdf#page=1), [main p.8 ICU mortality Table 2](../../jama_thille_2019_oi_190108.pdf#page=8), [results p.9 survival eFigure](../../joi190108supp2_prod.pdf#page=9). Complete main pp.1-11 and results pp.1-9 were considered for separately supplied ICU time-to-event output.
**Source evidence:** Plan lists ICU mortality in unconditional Kaplan–Meier/log-rank treatment comparisons. Main specifies ICU/hospital mortality chi-square; ICU deaths are 21/339 versus 26/302, difference −2.4 (95% CI −6.7 to 1.7), P=.25. The supplied overall day-90 survival curve gives log-rank P=.37 and is a different endpoint/window.
**Calculation:** Specification comparison: ICU mortality log-rank versus ICU mortality chi-square. No log-rank P can be recovered from final event counts alone.
**Affected result or extracted value:** Analysis identity of the key-secondary ICU mortality P=.25 and availability of its planned log-rank comparison.
**Why context does not resolve it:** The day-90 survival output does not identify an ICU mortality analysis, and the package supplies no change explanation.
**Alternative source-grounded interpretations:** A later SAP could amend the comparison or a retained ICU analysis could be unreported; neither is supplied. Conditional mortality Cox omissions are excluded from this candidate.
**Human verification steps:** Check the applicable mortality analysis specification and locate the planned ICU log-rank output or a disclosed amendment/explanation.

## C004 — Prespecified disease and weaning-test primary subgroup results are absent

**Candidate statement:** The plan commits to primary-outcome subgroup analyses by underlying cardiac/respiratory disease and weaning-test type, but the complete supplied subgroup results cover PaCO2 only.
**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol primary-subgroup commitments vs REPORT supplied subgroup analysis set
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-005, F-ST1-004
**Classification rationale:** Two factors within the same repeated planned primary-analysis reporting pattern form one candidate. PLAN commitments are compared with REPORT analysis availability.
**Classification ambiguity:** No role ambiguity; a separate applicable SAP or amendment is not supplied.
**Exact source locations:** [Protocol p.34 section 6.4](../../joi190108supp1_prod.pdf#page=34), [main p.4 subgroup methods](../../jama_thille_2019_oi_190108.pdf#page=4), [main p.7 subgroup results](../../jama_thille_2019_oi_190108.pdf#page=7), [main p.8 Figure 3](../../jama_thille_2019_oi_190108.pdf#page=8), [results p.1 contents](../../joi190108supp2_prod.pdf#page=1), [p.6 eTable 3](../../joi190108supp2_prod.pdf#page=6), [p.7 eTable 4](../../joi190108supp2_prod.pdf#page=7). Complete main pp.1-11 and results pp.1-9 assessed for the absent families.
**Source evidence:** Protocol states main/secondary outcome subgroup analyses will be performed in patients with underlying cardiac/respiratory disease and according to T-piece versus minimum pressure-support weaning test, in addition to PaCO2. Report describes PaCO2 interaction P=.25 and subgroup primary differences −12.9 and −5.0; baseline factor rows supply no subgroup outcome effects.
**Calculation:** Set comparison: explicitly prespecified primary subgroup factors include PaCO2, disease and weaning-test; supplied primary subgroup output factors include PaCO2 only.
**Affected result or extracted value:** Availability and prespecified interpretation of primary day-7 reintubation subgroup results by disease and weaning-test mode.
**Why context does not resolve it:** Explicit primary analysis commitments have no corresponding supplied results or change explanation; baseline descriptors cannot identify the intended subgroup effects.
**Alternative source-grounded interpretations:** The applicable SAP may have removed these analyses or their results may lie outside the supplied package; neither is established. No subgroup effect/interaction is inferred.
**Human verification steps:** Establish whether both planned primary subgroup families were retained and locate their results or reporting explanation. Do not extend this candidate to all non-key secondary subgroup analyses.

## C005 — Nonhypercapnic day-90 mortality absolute difference does not reconcile

**Candidate statement:** eTable 4 prints a mortality absolute difference of −3.8 percentage points with counts 54/254 and 50/276, whose stated proportion contrast is −3.14390049 points.
**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT results supplement eTable 4 counts and headings vs REPORT same-table absolute-difference entry
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-002, F-ST1-002
**Classification rationale:** The quantity-identity discrepancy is within one REPORT table. It is not a peripheral cross-location subgroup comparison, and no adjusted day-90 mortality estimator is identified.
**Classification ambiguity:** None
**Exact source locations:** [Results supplement p.7 eTable 4 headings and final mortality row](../../joi190108supp2_prod.pdf#page=7); method context [main p.4](../../jama_thille_2019_oi_190108.pdf#page=4).
**Source evidence:** Nonhypercapnic control n=254, deaths 54 (21%); intervention n=276, deaths 50 (18%). Absolute difference −3.8 (95% CI −9.9 to 3.6), P=.3626. Neighboring binary rows use intervention-minus-control proportions.
**Calculation:** 100×(50/276−54/254)=−3.14390049 points. Conservative continuous half-unit input intervals give [−3.596663,−2.691302], disjoint from the displayed effect interval [−3.85,−3.75].
**Affected result or extracted value:** Nonhypercapnic day-90 mortality absolute effect extracted from eTable 4.
**Why context does not resolve it:** The displayed fractions and difference column yield distinct effects beyond display precision; no alternate population or estimator identifies the printed value's calculation.
**Alternative source-grounded interpretations:** An unreported model or alternate denominator could explain it if established. No such explanation, raw data, or preferred estimator is inferred. The reported nonsignificance conclusion is not claimed to change.
**Human verification steps:** Establish the estimator and denominators underlying the reported difference and its relationship to the printed event fractions.
