# Quantitative Reporting Quality-Control Consistency Review — BEAM Trial

**Pending Human Adjudication**

This review identifies candidate reporting issues in the supplied randomized-trial package. Evidence reproduction and inclusion audit are workflow facts, not adjudications of the candidates or the study.

## Executive Quality-Control Summary

Complete review of the three supplied PDFs identified **13 stable candidates**, consolidated from 19 independently screened findings. Seven concern planned versus reported statistical design, five concern numerical or inferential reporting within the main article, and one concerns an internal primary-outcome recovery specification in the protocol. Direct-source evidence recheck reproduced all 13; the independent inclusion audit recorded 13 CONFIRMED and 0 QUESTIONED. Every candidate remains Pending Human Adjudication.

All 49 supplied PDF pages were mapped. The review tracked 182 numeric relationships and 106 statistical relationships; both fresh statistical passes completed all 106 statistical records. No finding was added by the second pass or audit. The review does not estimate whether any candidate changed an observed treatment effect, conclusion, or downstream decision.

## Package and Reused-Evidence Provenance

The article reports the comparison of bougie versus endotracheal tube with stylet for first-attempt intubation success. Source locations below use physical PDF pages, not journal page numbers.

| Source | Content role | PDF pages | Reusable-backed | Fresh-required | Mapped |
|---|---|---:|---:|---:|---:|
| [jama_driver_2018_oi_180054.pdf](<../jama_driver_2018_oi_180054.pdf#page=1>) | REPORT: main article | 11 | 11 | 0 | 11 |
| [joi180054supp1_prod.pdf](<../joi180054supp1_prod.pdf#page=1>) | PLAN: clinical trial protocol | 25 | 25 | 0 | 25 |
| [joi180054supp2_prod.pdf](<../joi180054supp2_prod.pdf#page=1>) | REPORT results pp. 1–6; PLAN blank operational form pp. 7–13 | 13 | 13 | 0 | 13 |
| **Total** | | **49** | **49** | **0** | **49** |

The run reused 47 source-linked assets: six native/layout text files and 41 PNG page images. Complete source-matched native text supports every page. Eight legacy images are absent, but their pages have usable text and complete scientific mapping. Reusable assets are provenance and locator aids; supplied source pages are the authority for evidence recheck. A protocol quotation within the observed interim-analysis supplement is classified by content, separately from the adjacent reported results.

The [source inventory](review_1_6_2/source_inventory.md), [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md), [coverage ledger](review_1_6_2/source_coverage.md), and [coverage manifest](review_1_6_2/coverage_manifest.md) preserve unit-level provenance. Earlier candidates, dispositions and reports were not discovery inputs. Supplied sources and reused assets were preserved.

## Scope, Complete Coverage, and Exclusions

The review addresses counts and denominators, estimate and test logic, statistical method logic, and planned versus reported statistical design under Workflow 1.6.2. Main mapping covered all 11 article pages; support mapping covered all 25 protocol and 13 mixed-support pages, including covers, administrative text, references and blank forms. Every direct-source row has mapped units equal to total units. There is no scientific-coverage gap.

The review applies the supplied inclusion threshold, rather than a candidate-count target. A reproduced observation qualifies through an always-register category (route A) or through all three route B criteria: in focus, unresolved by immediate context, and bearing on interpretation or extraction of a named result. Numerical precision comparisons allow each displayed input and comparator its half-unit interval. A remaining relative gap at most 0.05 is screened out, except that the scope explicitly exempts interval-versus-test conflicts from that exclusion. Model-based contrasts are not required to equal crude ratios or differences of marginal summaries.

The review excludes a broad clinical, design, novelty, misconduct or raw-data audit; preferred alternative analyses; recoverable notation and terminology; peripheral comparisons; and absence-only observations without a conflicting specification. Only supplied package evidence was used. No web or external literature was consulted.

## Quantitative and Statistical Relationship Coverage

The [main evidence map](review_1_6_2/extraction/main_quantitative_evidence.md) and [support evidence map](review_1_6_2/extraction/support_quantitative_evidence.md) reconstruct result-relevant relationships across narrative, tables, figures, protocol clauses and operational fields. The [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) contains 182 complete records, assembled without loss from two disjoint parts of 120 and 62 records. The [statistical inventory](review_1_6_2/statistics/relationship_inventory.md) contains 106 records: 73 main-paper and 33 support relationships.

| Review stage | Completed scope | Finding output |
|---|---|---:|
| Numeric consistency | All 182 numeric records | 2 findings |
| Cross-source consistency | All applicable report/plan and matched-source relationships | 8 findings |
| Statistical pass 1 | All 106 statistical records, PASS_1_COMPLETE | 9 findings |
| Statistical pass 2 | All 106 statistical records, PASS_2_COMPLETE; full ledger, screen, recheck and 20 prior exclusions | 0 new findings |
| Independent quality audit | 49 source pages, inventories, coverage, classifications, all 19 screening decisions, all 20 exclusions and all 13 candidates | 0 new findings |

The two statistical passes used different fresh high-effort agents. They cover null-value compatibility, interval order and containment, statistical-method identity, sample-size inputs, planned analyses and decision rules, matching populations/contrasts, and cross-lane count implications. Missing definitions are recorded separately from reproduced printed comparisons. Diagnostic calculations do not replace stated analyses. A continuity-corrected sample-size diagnostic was consistent with approximately 187 per arm and the printed 374 total; the supplied Stata command could not be executed locally.

## Inclusion Screening Summary

The [single screening log](review_1_6_2/screening/inclusion_screen.md) records exactly one decision for each of 19 initial findings. All 19 were INCLUDE with MEETS_THRESHOLD, mapping to 13 distinct issues. Shared candidate mappings consolidate six overlapping checker pairs while retaining all findings and locations. Pass 2 and audit emitted no additional findings, so no second screening wave was required.

| Finding decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 19 |
| SCREENED_OUT | All screened-out codes | 0 |
| **Total findings screened** | | **19** |

For each permitted screened-out finding reason code, the screening-log count is zero: NOT_REPRODUCED, ROUNDING_OR_DISPLAY_PRECISION, NOTATION_OR_TYPOGRAPHY, TERMINOLOGY_OR_WORDING, MODEL_VERSUS_CRUDE, CONTEXT_RESOLVES, CONDITIONAL_OR_UNREPORTED, PERIPHERAL_COMPARISON, OUT_OF_FOCUS and DUPLICATE_OF_INCLUDED.

Separately, the three initial checkers retained 20 self-excluded observations (numeric 4, cross-source 8, statistical 8). These were not emitted findings and did not receive candidate IDs. Pass 2 and the quality auditor reread all 20 against both inclusion routes and the precision rule, retaining their exclusions. Their reason counts are:

| Checker exclusion reason | Observations |
|---|---:|
| ROUNDING_OR_DISPLAY_PRECISION | 2 |
| NOTATION_OR_TYPOGRAPHY | 1 |
| TERMINOLOGY_OR_WORDING | 4 |
| MODEL_VERSUS_CRUDE | 2 |
| CONTEXT_RESOLVES | 1 |
| CONDITIONAL_OR_UNREPORTED | 5 |
| PERIPHERAL_COMPARISON | 4 |
| OUT_OF_FOCUS | 1 |
| NOT_REPRODUCED | 0 |
| DUPLICATE_OF_INCLUDED | 0 |
| **Total** | **20** |

Post-registration precision refinement narrowed C008's independently qualifying cells to the two medical Other cells. Its two respiratory/cardiac cells remain examined context with relative gaps at most 0.05. C007 also uses the normative all-input half-unit calculation. These refinements preserve the included findings and stable IDs; exact-count sensitivities remain transparently separate.

## Review-Domain Summary

`statistical_results` concerns numerical and inferential logic in report materials. `report_internal_inconsistency` concerns conflicts identifying which reported outcome, population or time point a number represents. `protocol_report` concerns differences between report and plan statistical design. `plan_material` concerns statistical design inconsistencies wholly within prospective material.

| Review domain | Candidates |
|---|---:|
| statistical_results | 5 |
| report_internal_inconsistency | 0 |
| protocol_report | 7 |
| plan_material | 1 |
| **Total** | **13** |

| Primary relationship type | Candidates |
|---|---:|
| P_R | 7 |
| P_P | 1 |
| S_C | 0 |
| S_W | 5 |
| **Total** | **13** |

C001 additionally involves P_P; P_R takes precedence. The relationship-type counts above use the single primary type per candidate. A source that only corroborates one side does not create another conflicting relationship; C010 therefore remains S_W only.

| Evidence state | Candidates |
|---|---:|
| reproduced | 13 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **13** |

Inclusion audit: CONFIRMED 13; QUESTIONED 0. Evidence state and inclusion audit do not determine human adjudication.

## Candidate Index

| ID | Candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#c001--primary-difficult-airway-subgroup-criteria) | Primary difficult-airway subgroup criteria | protocol_report | P_R | reproduced | CONFIRMED |
| [C002](#c002--randomization-stratification-criteria) | Randomization stratification criteria | protocol_report | P_R | reproduced | CONFIRMED |
| [C003](#c003--hypoxemia-ascertainment-window) | Hypoxemia ascertainment window | protocol_report | P_R | reproduced | CONFIRMED |
| [C004](#c004--duration-endpoint) | Duration endpoint | protocol_report | P_R | reproduced | CONFIRMED |
| [C005](#c005--enrollment-stopping-rule) | Enrollment stopping rule | protocol_report | P_R | reproduced | CONFIRMED |
| [C006](#c006--planned-kaplanmeier-percentile-and-censoring-summaries) | Planned Kaplan–Meier summaries | protocol_report | P_R | reproduced | CONFIRMED |
| [C007](#c007--initial-oxygen-saturation-denominators-and-missingness) | Initial oxygen-saturation missingness | statistical_results | S_W | reproduced | CONFIRMED |
| [C008](#c008--medical-indication-percentage-denominator-pattern) | Medical-indication percentage denominators | statistical_results | S_W | reproduced | CONFIRMED |
| [C009](#c009--three-process-confidence-intervals-and-tests) | Process intervals and tests | statistical_results | S_W | reproduced | CONFIRMED |
| [C010](#c010--all-patient-duration-interval-ordering) | Duration interval ordering | statistical_results | S_W | reproduced | CONFIRMED |
| [C011](#c011--grade-4-confidence-interval-and-test) | Grade-4 interval and test | statistical_results | S_W | reproduced | CONFIRMED |
| [C012](#c012--primary-missing-data-recovery-target-inside-the-plan) | Primary recovery target in the plan | plan_material | P_P | reproduced | CONFIRMED |
| [C013](#c013--interim-analysis-population-and-continuation-basis) | Interim population and continuation basis | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

Every card below remains **Pending Human Adjudication**. Classification fields reproduce the final ledger table exactly. Full direct-source confirmation facts are preserved in the [mechanical recheck](review_1_6_2/verification/evidence_recheck.md) and [independent audit](review_1_6_2/quality/evidence_quality_audit.md).

## C001 — Primary difficult-airway subgroup criteria

**Pending Human Adjudication**

**Candidate statement:** The printed primary difficult-airway criteria omit the protocol’s independent neck-trauma criterion and broaden airway edema to obstruction or edema; the operational form also differs from the original protocol.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** REPORT main article primary-subgroup definition vs PLAN protocol and operational-form definitions

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Qualifying route:** Route B

**Classification rationale:** REPORT main result/definition versus PLAN protocol and PLAN operational form. Primary P_R; all relationships P_R, P_P; domain protocol_report. P_R takes precedence over P_P. No S_C is added for a blank form.

**Classification ambiguity:** whether the form is an amended operational specification is not dated by the supplied material.

**Exact source locations:** PLAN [protocol p.13 §5.1, printed lines 427–431](../joi180054supp1_prod.pdf#page=13); REPORT [main p.1 Main Outcomes](../jama_driver_2018_oi_180054.pdf#page=1), [p.2 Patient Selection](../jama_driver_2018_oi_180054.pdf#page=2), [p.4 Figure 1 definition](../jama_driver_2018_oi_180054.pdf#page=4), [p.7 Table 3 primary row](../jama_driver_2018_oi_180054.pdf#page=7); PLAN [operational form p.7 item 3a](../joi180054supp2_prod.pdf#page=7) and [p.9 item 12](../joi180054supp2_prod.pdf#page=9).

**Source evidence:** Main pp.1,2,4 each define the primary difficult subgroup using facial trauma and airway obstruction or edema, alongside body fluids, obesity, short neck, small mandible, large tongue and cervical immobilization. Table 3 identifies 380 patients, successes 191/198 and 150/182, difference 14 percentage points (95% CI 8 to 20). Form item 12 lists facial trauma and airway obstruction/edema, with examples foreign body, angioedema, anaphylaxis and infection. Form item 3a separately lists Facial Trauma and Neck Trauma among indication choices.

**Reported-versus-comparator:** Protocol §5.1 includes facial **or neck** trauma and airway **edema**, alongside its other listed difficult characteristics, and expressly assigns that subgroup to the primary analysis. The form is a blank prospective measurement instrument, not results content. It independently differs from the original protocol list and thus supports a genuine plan-internal comparison.

**Reasoning procedure:** Focus D, route B: an analysis-population membership rule is not reconciled by names alone when a criterion is omitted or broadened. The primary count/result is the affected quantity; no actual change in its patient membership is asserted.


Direct observation is the three content lists and the Table 3 result. Changes in membership, reasons for amendment, or effect on success rates are not observed and are not inferred as facts.

**Calculation:** Neck trauma is an independent item in the original protocol, not in the report/form difficult-feature lists; obstruction without edema is included in the report/form literal list but not expressly in the original list. Common criteria and nearby exclusions do not explicitly equate these rule sets. Cervical immobility/immobilization and blood/vomit/body-fluid descriptions alone are not used to sustain the candidate. Display-precision intervals are not applicable to categorical inclusion rules; the matching result counts are context, not a discrepant arithmetic computation.

**Affected result or extracted value:** Primary first-attempt success in 380 difficult-airway patients: 191/198 versus 150/182, difference 14 percentage points (95% CI 8 to 20), and its population definition.

**Why context does not resolve it:** Shared criteria and nearby exclusions do not equate neck trauma with facial trauma or establish that obstruction without edema has identical eligibility. Immediate context does not identify the implemented membership rule for the 380-patient primary subgroup.

**Alternative source-grounded interpretations:** The operational form may reflect an amendment; affected features may all overlap with other qualifying features, or exclusions may remove some obstruction examples. The supplied lists and exclusions do not establish these possibilities for the primary cohort.


Remaining source question: Which criteria defined the 380-patient primary subgroup, and how were neck trauma without another qualifying feature and airway obstruction without edema handled?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for the printed list comparison and affected primary result. **Exact missing inputs or definitions:** implemented primary-population criteria, any amendment/version mapping, and a cross-classification of neck-only trauma or obstruction-without-edema cases.


Evidence reproduced. Determining recheck fact: the source-confirmed criterion lists remain different for the independent neck-trauma and obstruction items; no supplied mapping reconciles them.

**Potential downstream evidence impact:** An extractor could attach different eligibility criteria to the primary success counts and effect estimate, affecting population matching if the candidate is confirmed. No propagation or conclusion change is established by this review.

## C002 — Randomization stratification criteria

**Pending Human Adjudication**

**Candidate statement:** The report’s allocation strata omit apparent facial/neck trauma, an independent stratification feature in the protocol.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article randomization vs PLAN protocol randomization

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002, F-ST1-008

**Qualifying route:** Route B

**Classification rationale:** REPORT main randomization versus PLAN protocol randomization; primary/all P_R; domain protocol_report. The primary-results location identifies affected context and does not add S_W.

**Classification ambiguity:** possible undisclosed specification version.

**Exact source locations:** PLAN [protocol p.11 §4.1.1, lines 373–378](../joi180054supp1_prod.pdf#page=11); REPORT [main p.2 Randomization opening](../jama_driver_2018_oi_180054.pdf#page=2), [p.3 continuation](../jama_driver_2018_oi_180054.pdf#page=3), and [p.7 primary result](../jama_driver_2018_oi_180054.pdf#page=7).

**Source evidence:** Main pp.2–3 specify 1:1 assignment, blocks of 2, 4, 6, 8, 10, and two strata: obesity or cervical immobilization versus neither. The affected Table 3 primary result is 191/198 versus 150/182.

**Reported-versus-comparator:** Protocol p.11 specifies the same ratio and block sizes, but the first stratum is any cervical collar, gestalt obesity or apparent facial/neck trauma; the second has none of those characteristics.

**Reasoning procedure:** Focus D, route B: compare the stated allocation stratification rule, not the separately postprocedural primary-subgroup definition.


Direct: the written strata omit/include trauma differently. Inferred possibilities: an amendment or abbreviated reporting. No allocation imbalance or treatment-effect consequence is inferred.

**Calculation:** A patient with apparent facial/neck trauma and neither obesity nor immobilization is assigned to the first stratum by the protocol description and second by the report description. This is a logical rule example, not an assertion that such a patient occurred. Equal ratio/block sizes do not settle the third criterion. Half-unit intervals are not applicable to a categorical stratification rule; no discrepant copied number is alleged.

**Affected result or extracted value:** The allocation-stratum design attached to the primary difficult-airway success result, 191/198 versus 150/182.

**Why context does not resolve it:** Matching allocation ratio and block sizes do not settle whether trauma independently triggered the first stratum. Neither the report nor protocol identifies the implemented schedule or a replacement specification.

**Alternative source-grounded interpretations:** The report may abbreviate an implemented fuller rule, or the rule may have been amended. All trauma patients may have also met immobilization, but the sources do not state this.


Remaining source question: Was facial/neck trauma included in the actual allocation schedule, and which approved stratification specification underlies the reported trial?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for the rule comparison. **Exact missing inputs or definitions:** implemented allocation schedule, any amended stratum specification and the overlap of trauma with retained criteria.


Evidence reproduced. Determining recheck fact: the direct-source allocation descriptions retain different independent trauma criteria.

**Potential downstream evidence impact:** A trial-design extraction could record different allocation stratification features alongside the primary result if the candidate is confirmed; no allocation imbalance is inferred. No propagation or conclusion change is established by this review.

## C003 — Hypoxemia ascertainment window

**Pending Human Adjudication**

**Candidate statement:** The report anchors hypoxemia capture to first-attempt completion, while the protocol anchors it to cuff inflation.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article and results-supplement hypoxemia windows vs PLAN protocol window

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004, F-ST1-005

**Qualifying route:** Route A, category 5

**Classification rationale:** PLAN protocol versus REPORT main article and REPORT results supplement. Primary/all P_R; domain protocol_report. The two report sources agree, so no S_C conflict is added.

**Classification ambiguity:** possible amendment not supplied.

**Exact source locations:** PLAN [protocol p.9 §2.2(1),(4), lines 304–325](../joi180054supp1_prod.pdf#page=9) and [p.10 §3.2, lines 340–344,353–354](../joi180054supp1_prod.pdf#page=10). REPORT [main p.1 hypoxemia context](../jama_driver_2018_oi_180054.pdf#page=1), [p.3 Measurements/Trial Outcomes](../jama_driver_2018_oi_180054.pdf#page=3), [p.7 Table 3 composite rows/note b](../jama_driver_2018_oi_180054.pdf#page=7), [p.9 Table 5 hypoxemia row/note b](../jama_driver_2018_oi_180054.pdf#page=9), [supplement p.2 composite rows](../joi180054supp2_prod.pdf#page=2) and [p.3 hypoxemia note](../joi180054supp2_prod.pdf#page=3).

**Source evidence:** Main measurements run until one minute following the end of the first attempt. Both main notes and supplement note define hypoxemia during or within one minute after completion of the attempt. The main defines attempt duration by insertion/removal of the blade. Thresholds are <90%, or an absolute fall >10% when beginning below 90%. Table 3 composites: difficult-airway 156/191 versus 123/177, overall 317/371 versus 282/366; supplement reproduces these arm data. Table 5 standalone hypoxemia: 47/371 versus 50/364; abstract gives rounded 13%/14%.

**Reported-versus-comparator:** Protocol defines the same threshold, but capture ends one minute after ETT cuff inflation. Measurement §3.2 specifies recording every 20 seconds to that endpoint and the lowest value; standalone secondary 4 uses the same hypoxemia definition as composite secondary 1.

**Reasoning procedure:** Focus D, route A category 5: a defined component/window of planned standalone and composite outcomes changes its terminal anchor.


Direct: the two stated endpoints and reported counts. Inferred: whether any patient's hypoxemia status changed; no numerical change is claimed.

**Calculation:** One minute after cuff inflation and one minute after first-attempt completion are different written windows. The sources do not equate the terminal events; in a first-attempt failure cuff inflation need not occur at that attempt. Matching the threshold cannot prove equal ascertainment. Display-precision intervals cannot reconcile categorical timestamp anchors. Counts/percentages are matched affected-result locations, not an asserted event-count discrepancy.

**Affected result or extracted value:** Hypoxemia and success-without-hypoxemia definitions: difficult composite 156/191 versus 123/177; overall composite 317/371 versus 282/366; standalone hypoxemia 47/371 versus 50/364.

**Why context does not resolve it:** Route A, category 5: planned versus reported outcomes and analyses (or a plan-internal primary-analysis definition).

**Alternative source-grounded interpretations:** The anchors may be close in successful first attempts or an operational revision may have been implemented; these are possible explanations, not supplied equalities.


Remaining source question: Which terminal anchor was used for standalone and composite hypoxemia ascertainment, including failed first attempts, and was the planned cuff-inflation window revised?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for both window definitions and all retained affected cells. **Exact missing inputs or definitions:** applied capture window, paired cuff/blade timestamps, failure-case observation rule and any approved amendment.


Evidence reproduced. Determining recheck fact: direct-source window descriptions retain distinct terminal anchors despite matching saturation thresholds.

**Potential downstream evidence impact:** An extractor could attach a different observation window to standalone hypoxemia events or the success-without-hypoxemia composite. No changed event count is inferred. No propagation or conclusion change is established by this review.

## C004 — Duration endpoint

**Pending Human Adjudication**

**Candidate statement:** The reported first-attempt duration ends at blade removal, while the planned endpoint ends at cuff inflation with tracheal placement.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article and results-supplement duration endpoint vs PLAN protocol endpoint

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003, F-ST1-004

**Qualifying route:** Route A, category 5

**Classification rationale:** PLAN protocol versus REPORT main and REPORT results supplement; primary/all P_R; domain protocol_report. Report documents agree on blade removal; no S_C conflict.

**Classification ambiguity:** unspecified amendment history.

**Exact source locations:** PLAN [protocol p.9 §2.2(2), lines 315–317](../joi180054supp1_prod.pdf#page=9), [p.10 §3.2, lines 346–347](../joi180054supp1_prod.pdf#page=10), [p.19 §8.1, lines 657–660](../joi180054supp1_prod.pdf#page=19). REPORT [main p.1 secondary/median result](../jama_driver_2018_oi_180054.pdf#page=1), [p.3 Trial Outcomes](../jama_driver_2018_oi_180054.pdf#page=3), [p.4 time methods](../jama_driver_2018_oi_180054.pdf#page=4), [p.5 secondary time results](../jama_driver_2018_oi_180054.pdf#page=5), [p.7 Table 3 duration rows/note c](../jama_driver_2018_oi_180054.pdf#page=7), [p.8 Figure 2](../jama_driver_2018_oi_180054.pdf#page=8), [supplement p.2 duration rows](../joi180054supp2_prod.pdf#page=2), [p.3 duration note](../joi180054supp2_prod.pdf#page=3), and [p.4 eFigure 1](../joi180054supp2_prod.pdf#page=4).

**Source evidence:** Main p.3 and Table 3 note c define duration from blade insertion to blade removal. Main difficult-airway medians are 39 (IQR 29–52) and 40 (27–63) seconds, difference −1 (95% CI −6 to 3), P = .50; overall 38 (29–51) and 36 (25–54), difference 1 (4 to −1), P = .24. Supplement retains medians, prints differences −1 (−6 to3), P = .31 and 1 (−1 to4), P = .95, and states physician clustering. Figures/captions supply first-attempt time-to-success analysis, difficult HR 1.29 (1.04–1.60), log-rank P = .02; overall HR 1.12 (.97–1.30), log-rank P = .12. Abstract includes duration medians 38/36, establishing key-secondary relevance.

**Reported-versus-comparator:** Protocol defines time to intubation for the first attempt from attempt beginning to ETT cuff inflation with the tube in the trachea; stopwatch measurement refers to that definition. §8.1 describes time-to-event summaries; its absent specific summaries are separately rechecked in C006.

**Reasoning procedure:** Focus D, route A category 5: the reported planned-secondary duration uses a distinct terminal event and no supplied result is separately identified as the planned cuff-inflation measure.


Direct: endpoint texts, labels, medians and time analyses. Inferred only as possibilities: amendment or close timing. No direction or size of a resulting median change is inferred.

**Calculation:** Cuff inflation with tracheal placement and blade removal are distinct operational events. In failure cases, blade removal can terminate an attempt without successful cuff inflation at that attempt. The report does not state equality of these timestamps. No rounding interval comparison applies to the categorical endpoint change; medians are not recomputed or changed. C010 separately records the printed interval ordering.

**Affected result or extracted value:** Duration medians 39/40 seconds in difficult airways and 38/36 overall, their contrasts, and reported first-attempt time-to-success curves/HRs.

**Why context does not resolve it:** Route A, category 5: planned versus reported outcomes and analyses (or a plan-internal primary-analysis definition).

**Alternative source-grounded interpretations:** A revised operational endpoint may have been approved, or successful-attempt timestamps may be close; neither is documented as equivalence in the supplied package.


Remaining source question: Was cuff-inflation time amended to blade-removal duration, and which reported result or documented revision represents the originally planned endpoint?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for definitions and affected results. **Exact missing inputs or definitions:** approved endpoint revision, paired cuff/blade times, and any separately reported cuff-inflation result.


Evidence reproduced. Determining recheck fact: the supplied plan and report define duration using different terminal events, with no stated equivalence or identified planned-endpoint result.

**Potential downstream evidence impact:** An extractor could combine duration summaries or time-to-success effects defined by different terminal events if the candidate is confirmed. No numerical timing shift is estimated. No propagation or conclusion change is established by this review.

## C005 — Enrollment stopping rule

**Pending Human Adjudication**

**Candidate statement:** The report and protocol give distinct enrollment stopping rules underlying the primary sample.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article enrollment stopping rule vs PLAN protocol stopping rule

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005, F-ST1-007

**Qualifying route:** Route B

**Classification rationale:** REPORT main statistical stopping rule versus PLAN protocol stopping rule; primary/all P_R; domain protocol_report.

**Classification ambiguity:** undisclosed chronology or joint rule.

**Exact source locations:** PLAN [protocol p.19 §8.2, lines 665–674](../joi180054supp1_prod.pdf#page=19); REPORT [main p.1 study interval/final sample](../jama_driver_2018_oi_180054.pdf#page=1), [p.2 Trial Design dates](../jama_driver_2018_oi_180054.pdf#page=2), [p.3 Statistical Analysis](../jama_driver_2018_oi_180054.pdf#page=3), [p.4 Figure 1/final population](../jama_driver_2018_oi_180054.pdf#page=4), and [p.7 Table 3 primary size](../jama_driver_2018_oi_180054.pdf#page=7).

**Source evidence:** Main p.3 says the difficult-airway count was monitored and the trial stopped when more than 374 such patients enrolled. Main gives September 2016 through August 2017, final 757 overall and 380 difficult-airway patients, distributed 198/182 for primary analysis.

**Reported-versus-comparator:** Protocol targets 374 difficult-airway patients but specifies one calendar year or 1000 total patients, whichever first, followed by IRB discussion of extension if 374 difficult-airway patients were not reached.

**Reasoning procedure:** Focus D, route B: compare explicit statistical accrual decision rules underlying the final primary sample, not an administrative date-copy difference.


Direct: the two differently described triggers. Not directly observed: a departure in realized closure or its effect on precision.

**Calculation:** A first-boundary rule based on calendar year/overall count is not identical to a difficult-subgroup trigger >374. The realized 380/757 and trial months can be compatible with both; the recheck does not claim an observed date violates either boundary. Numerical rounding cannot reconcile different predicates, so no half-unit discrepancy is asserted for 374 versus 380.

**Affected result or extracted value:** Primary sample size 380 difficult-airway participants among 757 overall, and the statistical enrollment-closure rule accompanying its success estimate.

**Why context does not resolve it:** The realized trial dates and 380 difficult/757 overall participants may satisfy both boundaries, but do not establish whether the subgroup trigger replaced, supplemented or coincided with the calendar-year/1000-patient rule.

**Alternative source-grounded interpretations:** Count and calendar limits may have coincided, a subgroup target may have supplemented the limit, or a revision may have replaced it. These are not excluded by the dates but are not distinguished by the text.


Remaining source question: Did the >374 difficult-airway trigger replace, supplement or coincide with the calendar-year/1000-patient rule, and which rule governed final closure?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for printed rules and final samples. **Exact missing inputs or definitions:** exact closure trigger/date, joint rule implementation, amendments and any extension decision.


Evidence reproduced. Determining recheck fact: the two explicit trigger descriptions remain distinct; actual enrollment dates alone do not identify their relationship.

**Potential downstream evidence impact:** A design extraction could assign a different accrual stopping rule to the final primary sample and its planned precision. No realized boundary departure is asserted. No propagation or conclusion change is established by this review.

## C006 — Planned Kaplan–Meier percentile and censoring summaries

**Pending Human Adjudication**

**Candidate statement:** The supplied reports do not identify the prescribed Kaplan–Meier quartile confidence intervals and percentage censored for the key secondary time outcome.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article and results-supplement time analyses vs PLAN protocol planned summaries

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-008

**Qualifying route:** Route A, category 5

**Classification rationale:** PLAN protocol versus REPORT main and REPORT supplement; primary/all P_R; domain protocol_report. No S_C is added because report documents do not conflict about the omitted quantities.

**Classification ambiguity:** a replacement specification is not supplied.

**Exact source locations:** PLAN [protocol p.9 §2.2(2)](../joi180054supp1_prod.pdf#page=9) and [p.19 §8.1, lines 657–660](../joi180054supp1_prod.pdf#page=19). REPORT [main p.1 duration result](../jama_driver_2018_oi_180054.pdf#page=1), [p.4 time methods](../jama_driver_2018_oi_180054.pdf#page=4), [p.5 secondary time results](../jama_driver_2018_oi_180054.pdf#page=5), [p.7 duration rows](../jama_driver_2018_oi_180054.pdf#page=7), [p.8 Figure 2](../jama_driver_2018_oi_180054.pdf#page=8), [supplement p.2 eTable 1](../joi180054supp2_prod.pdf#page=2), [p.3 notes](../joi180054supp2_prod.pdf#page=3), and [p.4 eFigure 1](../joi180054supp2_prod.pdf#page=4). Fresh full-report native text searches for percentile, censoring, Kaplan and duration were combined with visual inspection of both figures.

**Source evidence:** Main Table 3 and eTable 1 provide duration median/IQR, between-group contrasts with CIs, and P values. Main methods name Kaplan–Meier estimates, log-rank testing and unadjusted Cox analysis. Main secondary text and Figure 2 provide HR 1.29 (1.04–1.60), P = .02; overall text/eFigure1 HR 1.12 (.97–1.30), log-rank P = .12. Figures have censoring ticks, event curves and risk counts; neither has percentile confidence limits or a printed percentage censored.

**Reported-versus-comparator:** Protocol §8.1 expressly prescribes KM estimates of the 25th, 50th, 75th percentiles with two-sided 95% confidence intervals and percentage censored. §2.2(2) identifies the planned secondary time outcome; main abstract reports duration, making it key secondary under the scope definition.

**Reasoning procedure:** Focus D, route A category 5: a prescribed key-secondary analysis summary is not reported in the supplied results.


Direct: explicit planned quantities and the distinct printed analyses. Inference is confined to possible replacement or external availability; actual production/nonproduction of the missing summaries is not established.

**Calculation:** A sample median/IQR is not three KM percentile estimates each with a confidence interval; a contrast CI or HR CI estimates another quantity. A risk table or plotted censoring tick is not the specified percentage censored. No specified percentile-CI set or censoring percentage was found in either supplied REPORT source. Half-unit intervals do not apply to absent distinct summaries. This comparison remains independently applicable even if the endpoint-anchor issue C004 were reconciled.

**Affected result or extracted value:** Key-secondary time-to-event quartile confidence intervals and censoring percentage, distinct from medians/IQRs, contrast CIs, HR CIs and event curves.

**Why context does not resolve it:** Route A, category 5: planned versus reported outcomes and analyses (or a plan-internal primary-analysis definition).

**Alternative source-grounded interpretations:** The displayed curves/HR strategy may have superseded the summaries or the summaries may exist outside this package. The sources do not document either; no external search was performed.


Remaining source question: Were the prescribed KM percentile confidence intervals and censoring summaries produced, and where are they reported or their replacement documented?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for the explicit plan and complete supplied report locations; enough to reproduce the absence of the specified summaries. **Exact missing inputs or definitions:** KM percentile CIs, censoring percentages, the analysis dataset/event/censoring times, and a documented replacement specification.


Evidence reproduced. Determining recheck fact: the explicitly specified percentile CIs and censoring percentage are absent from the complete supplied REPORT displays, despite other time-to-event results being printed.

**Potential downstream evidence impact:** A synthesis seeking KM percentile intervals or censoring burden could treat distinct reported summaries as substitutes, or leave the prescribed fields unavailable. No missing result is numerically reconstructed. No propagation or conclusion change is established by this review.

## C007 — Initial oxygen-saturation denominators and missingness

**Pending Human Adjudication**

**Candidate statement:** Initial oxygen-saturation threshold denominators imply missing counts that do not reconcile with the same table’s explicit saturation-missingness footnote.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 1 saturation denominators vs REPORT same-table missingness footnote

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-002

**Qualifying route:** Route A, category 3

**Classification rationale:** Both sides are REPORT content within the same main-table display; primary/all S_W; domain statistical_results.

**Classification ambiguity:** none about roles; data-availability definition is unresolved.

**Exact source locations:** REPORT [main p.5 Table 1 headers, saturation median/threshold rows and footnote b](../jama_driver_2018_oi_180054.pdf#page=5), confirmed with a new direct-source image.

**Source evidence:** Arm totals 381/376; saturation median 99 (95–100)/99 (96–100); <90% rows44/352 (13)/40/344 (12); <80% rows21/352 (6)/11/344 (3). Both threshold rows use the same352/344 denominators.

**Reported-versus-comparator:** Footnote b states43 missing initial oxygen saturations,19 bougie and 24 tube, after describing initial vital signs as first readings after enrollment and before intubation. It separately gives missing heart rates 61 (29/32) and systolic pressures185 (94/91). These are matched as separately labeled comparator counts, not substituted for saturation.

**Reasoning procedure:** Focus A, route A category 3: within-display counts, data denominators and explicit missingness for the same initial measurement must reconcile, allowing every displayed input its precision interval.


Direct:352/344 and 19/24, plus their printed measurement labels. Inference: possible exclusion or alignment mechanism. No replacement denominator is assigned.

**Calculation:** Normative continuous bounds: 381±.5 minus 352±.5 yields [28,30] missing bougie; 376±.5 minus 344±.5 yields [31,33] missing tube. Compare with 19±.5=[18.5,19.5] and 24±.5=[23.5,24.5]. Gaps 8.5 and 6.5 imply relative discrepancies 8.5/19=.44737 and 6.5/24=.27083. Combining the four arm/observed-count input intervals yields total missing [59,63]; printed 43±.5=[42.5,43.5], gap 15.5, relative 15.5/43=.36047. All exceed .05. If the separately displayed19+24 is summed instead of printed 43, its [42,44] interval also does not overlap [59,63], gap 15, relative 15/43=.34884. These are the normative calculations.

Exact-count sensitivity: 381−352=29,376−344=32,total 61 versus 19/24,total 43. Singleton gaps10/19=.52632,8/24=.33333,18/43=.41860 match the checker arithmetic but are not the normative relaxed-input comparison. Event percentages themselves are rounding-compatible with their printed denominators. The candidate compares expressly printed missing counts rather than dividing the mismatch by larger observed-data denominators.

**Affected result or extracted value:** Initial saturation availability: observed threshold denominators 352/344 versus footnote missing counts 19/24 (43 total); both <90% and <80% threshold rows.

**Why context does not resolve it:** Route A, category 3: counts, denominator and percentage/missingness within one display do not reconcile beyond the display-precision threshold.

**Alternative source-grounded interpretations:** Threshold rows could have further exclusions or distinct usable observations. Their denominators equal arm totals minus missing heart rates, which suggests a possible alignment explanation but does not establish origin or a replacement value.


Remaining source question: Do352/344 describe all participants with initial saturation available; if so, how do they reconcile with 43 missing (19/24), and if not, which additional rule defines those threshold-row denominators?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for both threshold rows, headers and missingness arithmetic. **Exact missing inputs or definitions:** any threshold-specific eligibility/exclusion rule and whether median/IQR and threshold rows intentionally use different subsets.


Evidence reproduced. Determining recheck fact: even the normative half-unit allowance leaves every arm/total comparison above .05. Source values matched; the refinement is arithmetic precision handling, not transcription correction.

**Potential downstream evidence impact:** An extractor could copy either the threshold-row data-availability counts or the footnote’s missingness totals when describing initial saturation completeness. No propagation or conclusion change is established by this review.

## C008 — Medical-indication percentage denominator pattern

**Pending Human Adjudication**

**Candidate statement:** The two medical Other percentage cells do not reconcile with their counts and arm denominators beyond normative display precision; equally nested rows do not support one uniform alternative denominator.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 1 medical-indication percentages vs REPORT same-table counts and denominators

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 3

**Classification rationale:** REPORT main Table 1 versus REPORT same-table counts/headers; primary/all S_W; domain statistical_results.

**Classification ambiguity:** none about content roles; denominator convention is missing.

**Exact source locations:** REPORT [main p.5 Table 1 arm headers, medical parent and all six nested medical indication rows](../jama_driver_2018_oi_180054.pdf#page=5), confirmed visually from the supplied PDF.

**Source evidence:** Headers 381/376. Medical parents 318 (83)/315 (84). All nested rows: altered mental status 185 (49)/173 (46); cardiac arrest 32 (8)/23 (6); septic shock 21 (6)/27 (7); seizure 20 (5)/28 (7); asthma/COPD/heart failure/pneumonia 16 (5)/23 (7); Other 44 (14)/41 (13). All four originally cited percentage cells and all contextual rows were found and matched.

**Reported-versus-comparator:** Arm headers are the denominator basis being tested. Medical parent counts are an alternative conditional basis. Counts sum185+32+21+20+16+44=318 and 173+23+27+28+23+41=315. Neighboring equally indented altered-mental-status percentages agree with arm totals, not medical totals.

**Reasoning procedure:** Focus A, route A category 3: a count, displayed denominator and percentage within one display are compared under the normative half-unit allowance for every input. All examined locations remain recorded, while only comparisons beyond the required threshold independently sustain the reproduced issue.


Direct: printed counts, percentages, hierarchy and headers; the two Other cells remain above the precision threshold. Inferred explanation: denominator switching during preparation; intentional mixed reporting also remains possible.

**Calculation:** For c/n×100, the normative recomputed interval is [100(c−.5)/(n+.5),100(c+.5)/(n−.5)]; printed p uses [p−.5,p+.5].

| Examined cell | Inputs c/n | Recomputed interval, % | Printed interval, % | Gap, percentage points | Relative gap / printed p | Independent support under normative rule |
|---|---|---|---|---|---|---|
| Bougie asthma/COPD/heart failure/pneumonia | 16/381 | [4.06291,4.33640] | [4.5,5.5] | .16360 | .03272 | At most .05; does not independently support inclusion. |
| Tube asthma/COPD/heart failure/pneumonia | 23/376 | [5.97610,6.25832] | [6.5,7.5] | .24168 | .03453 | At most .05; does not independently support inclusion. |
| Bougie medical Other | 44/381 | [11.40236,11.69514] | [13.5,14.5] | 1.80486 | .12892 | Greater than .05; supports the reproduced pattern. |
| Tube medical Other | 41/376 | [10.75697,11.05193] | [12.5,13.5] | 1.44807 | .11139 | Greater than .05; supports the reproduced pattern. |

Exact-count sensitivity: percentages 4.19948,6.11702,11.54856,10.90426 versus printed 5,7,14,13 have gaps .30052,.38298,1.95144,1.59574 after percentage rounding; relative .06010,.05471,.13939,.12275. Those checker values are retained as exact-count sensitivity, not the normative calculation. The normative allowance narrows independently supporting cells to the two medical Other cells, and preserves one stable repeated issue. No source transcription changed.

Using medical parents instead gives 16/318=5.031%,23/315=7.302%,44/318=13.836%,41/315=13.016%, reproducing the four displayed percentages. But 185/318=58.176% and 173/315=54.921% differ from printed 49%/46%; one uniform conditional reading cannot explain the nested column. This is an observed denominator-pattern compatibility, not a claimed production mechanism.

**Affected result or extracted value:** Medical Other: bougie 44 (14%) and tube 41 (13%), with arm totals 381/376. Respiratory/cardiac cells 16 (5%)/23 (7%) are retained as contextual locations, not independent normative support.

**Why context does not resolve it:** Route A, category 3: counts, denominator and percentage/missingness within one display do not reconcile beyond the display-precision threshold.

**Alternative source-grounded interpretations:** Some rows may intentionally use the medical-only base while others use the arm base. The table supplies no statement defining that change. Medical indentation alone does not explain the different basis across equally nested rows.


Remaining source question: Which denominator applies to each medical indication row, especially Other, and are the percentages intended to use a common marginal or conditional base?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for all four cited cells, all nested comparators, counts and normative precision calculations. **Exact missing inputs or definitions:** row-specific percentage denominator definition and any intended change between marginal and conditional percentages.


Evidence reproduced. Determining recheck fact: both medical Other cells remain beyond .05 under the mandated all-input rounding intervals. The two respiratory/cardiac cells are retained as examined context and do not independently sustain inclusion under that rule. This is a calculation refinement, not reproduced_after_transcription_correction.

**Potential downstream evidence impact:** An extractor could copy 14%/13% as arm-based medical Other percentages or use a different conditional denominator. The intended denominator convention determines those descriptive fields. No propagation or conclusion change is established by this review.

## C009 — Three process confidence intervals and tests

**Pending Human Adjudication**

**Candidate statement:** Three process-result 95% difference intervals include the zero null while their corresponding two-sided P values are below .05.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 process intervals vs REPORT same-table P values and methods

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-001

**Qualifying route:** Route A, category 1

**Classification rationale:** All compared content is REPORT main article; primary/all S_W; domain statistical_results.

**Classification ambiguity:** none about roles or relationships.

**Exact source locations:** REPORT [main p.6 Table 2 senior-resident/fellow, junior-resident and video-screen-during-passage rows](../jama_driver_2018_oi_180054.pdf#page=6); REPORT [p.4 statistical methods](../jama_driver_2018_oi_180054.pdf#page=4). All three numerical rows were visually confirmed on a new direct-source render.

**Source evidence:** Senior/fellow 318/381 versus 334/376, difference−5 (95% CI−10 to0), P = .03; junior 57/381 versus 37/376, difference 5 (0 to10), P = .03; video during passage 75/377 versus 98/372, difference−6 (−12 to0), P = .04.

**Reported-versus-comparator:** Each P is in the same row as its 95% difference interval. Methods specify binary chi-square tests and two-sided .05, with 95% CIs. The screen-use row uses377/372 data denominators rather than overall381/376; this alignment was confirmed.

**Reasoning procedure:** Focus B, route A category 1: printed confidence interval containing the zero null versus significant two-sided test at.05.


Direct: three printed zero endpoints with significant P values. Inferred: rounding or differing-method explanations. The same displayed pattern is consolidated into one stable issue; all three occurrences remain explicit.

**Calculation:** Each printed interval contains zero, while .03,.03,.04<.05. Diagnostic endpoint rounding intervals are [-10.5,−9.5]/[−.5,.5], [−.5,.5]/[9.5,10.5], and [−12.5,−11.5]/[−.5,.5]. Printed P intervals [.025,.035],[.025,.035],[.035,.045] remain below .05. An unrounded zero-adjacent endpoint could be nonzero, but the scope expressly exempts category 1 conflicts from the rounding/relative-discrepancy exclusion; no relative-gap threshold is used here.

**Affected result or extracted value:** Senior-resident/fellow difference −5 (−10 to 0), P = .03; junior-resident difference 5 (0 to 10), P = .03; video-screen during passage difference −6 (−12 to 0), P = .04; all differences in percentage points.

**Why context does not resolve it:** Route A, category 1: interval-versus-P-value/test conflict; this category is not excluded by endpoint rounding or different inferential constructions.

**Alternative source-grounded interpretations:** Unrounded limits may exclude zero or CIs/tests may use different inferential constructions; the checker diagnostics illustrate such possibilities but do not establish actual methods or replace the printed quantities.


Remaining source question: What are the unrounded limits and CI constructions for these three process rows, and how should their displayed zero endpoints be read alongside P = .03,.03,.04?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for printed CI/test compatibility at stated levels. **Exact missing inputs or definitions:** exact difference-CI construction and unrounded interval endpoints for each row. Those are not necessary to reproduce the printed conflict.


Evidence reproduced. Determining recheck fact: all three printed 95% intervals include zero while their corresponding printed P values are below the stated .05 threshold.

**Potential downstream evidence impact:** An extractor could record different null-value conclusions from the printed process intervals and corresponding P values, or copy zero endpoints without their unresolved inferential context. No propagation or conclusion change is established by this review.

## C010 — All-patient duration interval ordering

**Pending Human Adjudication**

**Candidate statement:** The all-patient duration difference is printed with descending 95% confidence limits, 4 to −1 seconds, leaving lower/upper extraction fields unclear.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 all-patient duration interval vs REPORT same-document interval order and methods

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-003

**Qualifying route:** Route B

**Classification rationale:** REPORT main interval versus REPORT main interval-order convention/methods; primary/all S_W; domain statistical_results. The supplement is REPORT but only corroborates an alternative ordering under a distinct analysis, so the checker suggestion to add S_C is not retained. Ledger S_W only is confirmed.

**Classification ambiguity:** none about roles; original interval output remains absent.

**Exact source locations:** REPORT [main p.7 Table 3 all-patient duration row](../jama_driver_2018_oi_180054.pdf#page=7) and [p.4 continuous-analysis methods](../jama_driver_2018_oi_180054.pdf#page=4); REPORT [supplement p.2 corresponding eTable 1 row](../joi180054supp2_prod.pdf#page=2) and [p.3 clustering explanation](../joi180054supp2_prod.pdf#page=3). The main interval was visually confirmed from the supplied PDF.

**Source evidence:** Main row medians 38 (29–51)/36 (25–54) seconds, difference 1 (95% CI 4 to−1), P = .24. Methods name Hodges–Lehmann differences for continuous variables and Wilcoxon rank-sum tests.

**Reported-versus-comparator:** Main-table difference intervals otherwise use ascending endpoints, including difficult duration−6 to3 and successful-attempt duration2 to7. Supplement corresponding row gives1 (−1 to4), P = .95; its note explicitly recalculates difference/interval/P columns for physician clustering while leaving arm columns unchanged.

**Reasoning procedure:** Focus B, route B: a lower/upper confidence interval requires its first lower position not to exceed its second upper position; this determines extracted endpoint fields.


Direct:4 to−1 printed in the main. Inferred: transposition or another intended numeric reading; no final replacement is assigned.

**Calculation:** The main prints 4>−1. First endpoint half-unit interval [3.5,4.5] and second [−1.5,−.5] retain minimum descending separation3.5−(−.5)=4 seconds. Gap relative to first printed endpoint4 is4/4=1.00> .05. Point estimate interval [.5,1.5] lies between the unordered extrema, but cannot make the printed order lower-to-upper. Supplement[-1,4] corroborates a possible reorder, not a reconstruction of the main inferential method. No P conflict is created by comparing explicitly different analyses.

**Affected result or extracted value:** All-patient duration contrast 1 second, printed 95% CI 4 to −1, P = .24, particularly the extracted lower and upper limits.

**Why context does not resolve it:** The table’s ascending intervals elsewhere do not define a descending convention or establish original inferential limits. Choosing a lower/upper value requires a numeric reinterpretation that the immediate main-table context does not specify.

**Alternative source-grounded interpretations:** Limits may have been transposed; a descending reporting convention would require a definition absent from the otherwise ascending display. The adjusted supplement supports one possible ascending reading but does not establish the original main limits.


Remaining source question: Which value is the lower and which the upper95% limit for the all-patient duration difference, and what original main-analysis output establishes them?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for the printed ordering and precision rule. **Exact missing inputs or definitions:** unrounded main Hodges–Lehmann limits, original duration ranks/ties and CI construction sufficient to identify the intended endpoints.


Evidence reproduced. Determining recheck fact: direct-source endpoints are descending and every permitted half-unit value retains that ordering. No transcribed source value was changed.

**Potential downstream evidence impact:** An extractor could populate reversed lower/upper CI fields or choose an ascending reinterpretation unsupported by the original main-analysis output. No replacement limits are assigned. No propagation or conclusion change is established by this review.

## C011 — Grade-4 confidence interval and test

**Pending Human Adjudication**

**Candidate statement:** The Grade-4 success difference interval excludes zero while its corresponding within-grade P value is nonsignificant at .05.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Grade-4 interval vs REPORT same-table P value and methods

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 1

**Classification rationale:** REPORT main interval and REPORT same-row test/methods; primary/all S_W; domain statistical_results.

**Classification ambiguity:** none; interaction remains a separate hypothesis.

**Exact source locations:** REPORT [main p.7 Table 3 Cormack–Lehane Grade 4 row](../jama_driver_2018_oi_180054.pdf#page=7), confirmed visually; REPORT [main p.4 significance methods](../jama_driver_2018_oi_180054.pdf#page=4).

**Source evidence:** Bougie 3/3, 100% (95% CI 29 to100); tube 2/5, 40% (5 to85); difference 60 percentage points (95% CI 17 to100); within-grade P = .09; interaction P = .78.

**Reported-versus-comparator:** The .09 value is the within-grade comparison P in the same row as the difference CI; .78 is separately labeled interaction P and concerns another hypothesis. Methods give chi-square tests,95% CIs and two-sided .05.

**Reasoning procedure:** Focus B, route A category 1: difference CI excludes zero although its corresponding test is nonsignificant at the stated level.


Direct: positive difference interval and nonsignificant within-grade P. Inferred: method mismatch or interval capping; no chosen method or replacement result is assigned.

**Calculation:** [17,100] excludes zero and .09> .05. Half-unit lower endpoint[16.5,17.5] remains positive; upper[99.5,100.5] also positive; P [.085,.095] remains> .05. Difference estimate [59.5,60.5] is within possible ordered endpoint ranges; containment and ordering are not the conflict. Route A category 1 has no relative-gap exclusion. Crude count difference 100×(3/3−2/5)=60 matches the estimate, but is not asserted to identify its actual CI construction.

**Affected result or extracted value:** Grade-4 first-attempt success contrast: 60 percentage points (95% CI 17 to 100), P = .09; separate interaction P = .78 is not the comparator.

**Why context does not resolve it:** Route A, category 1: interval-versus-P-value/test conflict; this category is not excluded by endpoint rounding or different inferential constructions.

**Alternative source-grounded interpretations:** A CI from a different construction and chi-square P may yield this display; the checker normal-interval/Pearson diagnostics are compatible explanations but are not supplied method identities.


Remaining source question: Which method produced the17-to100% CI and which produced P = .09, and how should their different null-value conclusions be interpreted?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for printed CI/test compatibility. **Exact missing inputs or definitions:** the difference-CI method/unrounded limits and any deliberate difference between inferential constructions. These do not prevent the observed comparison.


Evidence reproduced. Determining recheck fact: the same-row interval excludes zero while P remains above .05 even after permitted display rounding.

**Potential downstream evidence impact:** An extractor could code statistical significance from the positive interval or nonsignificance from P = .09 for the same Grade-4 comparison. No propagation or conclusion change is established by this review.

## C012 — Primary missing-data recovery target inside the plan

**Pending Human Adjudication**

**Candidate statement:** The protocol’s primary missing-data recovery instruction targets success without hypoxemia, while its primary outcome is success alone and the composite is separately secondary.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol primary definition vs PLAN same-protocol primary missing-data recovery target

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007, F-ST1-009

**Qualifying route:** Route A, category 5

**Classification rationale:** Every conflicting location is PLAN in the same protocol; primary/all P_P; domain plan_material. REPORT Table 3 merely identifies affected outcomes and does not add P_R. Ledger classification is confirmed.

**Classification ambiguity:** implementation is unknown, not document role.

**Exact source locations:** PLAN [protocol p.8 §2.1, lines280–282](../joi180054supp1_prod.pdf#page=8), [p.9 primary continuation/secondary1, lines284–312](../joi180054supp1_prod.pdf#page=9), [p.20 §8.4.1 and §8.6.1, lines693–697,719–720](../joi180054supp1_prod.pdf#page=20), [p.21 §8.6.1, lines721–722](../joi180054supp1_prod.pdf#page=21). REPORT [main p.7 primary/composite rows](../jama_driver_2018_oi_180054.pdf#page=7) is affected-result context only.

**Source evidence:** Protocol §2.1 defines primary first-pass tracheal-intubation success and §8.4.1 primary analysis in the difficult-airway subset. Its missing-data clause begins “For the primary outcome” on p.20, and continues on p.21 with video review to determine first-pass success **without hypoxemia**, excluding if video is unavailable.

**Reported-versus-comparator:** Protocol p.9 explicitly assigns success without hypoxemia to secondary outcome1, requiring both first-attempt success and no hypoxemia. Primary success alone is separately defined. Main Table 3 context distinguishes primary 191/198 versus 150/182 from secondary composite156/191 versus 123/177; these results do not demonstrate actual use of the recovery pathway.

**Reasoning procedure:** Focus D, route A category 5: a planned primary-analysis ascertainment step adds the component assigned to a separate secondary composite.


Direct: an internally different recovery criterion inside the protocol. Inferred possibilities: dual-component reconstruction or wording origin. No claim is made about a recovered patient's classification or effect on published counts.

**Calculation:** Primary predicate is success; stated primary-recovery predicate is success AND no hypoxemia. They differ for a successful first attempt with hypoxemia. This is a logical illustration, not a claim such an observation was recovered. Rounding intervals are not applicable to outcome predicates; no numerical primary-result change is inferred.

**Affected result or extracted value:** Primary first-pass success ascertainment after missing-form video recovery; affected published context distinguishes primary 191/198 versus 150/182 from composite 156/191 versus 123/177.

**Why context does not resolve it:** Route A, category 5: planned versus reported outcomes and analyses (or a plan-internal primary-analysis definition).

**Alternative source-grounded interpretations:** Video may have supplied separate success and hypoxemia values, retaining success alone for primary analysis; the composite phrase may not reflect implementation. No supplied implementation statement resolves the targets.


Remaining source question: Was primary video recovery intended to determine success alone or success without hypoxemia, how was primary status derived, and was that pathway used?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for the internal clause comparison. **Exact missing inputs or definitions:** whether video was to recover both component values separately, how primary success was derived, whether any patient's forms triggered this pathway and any clarification/amendment.


Evidence reproduced. Determining recheck fact: the primary missing-data clause expressly adds no-hypoxemia to a target otherwise defined as success alone and elsewhere labels that composite secondary.

**Potential downstream evidence impact:** A plan extraction could record a composite rather than success-alone primary recovery target. Whether it affected any published participant status is not established. No propagation or conclusion change is established by this review.

## C013 — Interim analysis population and continuation basis

**Pending Human Adjudication**

**Candidate statement:** The reported interim continuation display accounts for all 507 enrolled patients, while the protocol prescribes the primary difficult-airway subset and no separate primary-subgroup interim result is supplied.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT results-supplement observed interim population vs PLAN protocol primary-population interim rule

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006, F-ST1-006

**Qualifying route:** Route A, category 5

**Classification rationale:** PLAN original protocol versus REPORT observed interim results; primary/all P_R; domain protocol_report. The p.6 prospective quotation corroborates the original plan; it is not a second conflicting plan or an additional S_W relationship. Main p.3 supplies REPORT affected-population context.

**Classification ambiguity:** quoted prospective content is distinguished from adjacent observed results by its heading/tense; no extra relationship is assigned merely because both occur on one physical page.

**Exact source locations:** PLAN [protocol p.20 §8.4.1/§8.5, lines693–706](../joi180054supp1_prod.pdf#page=20), [p.21 §8.6.2, lines730–742](../joi180054supp1_prod.pdf#page=21). REPORT [supplement p.6 eAppendix1 observed interim rates/continuation](../joi180054supp2_prod.pdf#page=6); REPORT [main p.3 primary-population paragraph](../jama_driver_2018_oi_180054.pdf#page=3) corroborates population context. The prospective protocol quotation on supplement p.6 was also found and matched.

**Source evidence:** Supplement reports after 507 enrolled, bougie 250/257 (97%), tube 213/250 (85%), then states that using the above assumptions the trial was not stopped for futility. Main separates difficult-airway primary and overall secondary analyses.

**Reported-versus-comparator:** Original protocol defines primary analysis in the difficult-airway ITT subset and overall analysis as secondary. §8.6.2 specifies interim after 500 enrolled, primary outcome only, and projected1000 equally allocated with unchanged tube success and bougie success15 percentage points higher in the second half, capped at100%. The quoted rule on supplement p.6 matches the original source; the original is used as the PLAN comparator.

**Reasoning procedure:** Focus D, route A category 5: the documented continuation calculation displays the entire enrolled population and supplies no separately identified planned primary-subgroup interim analysis.


Direct: complete-cohort denominators, population specifications and stated continuation. Inferred: use of these rates instead of an unreported calculation; the record does not establish that no primary-only analysis occurred.

**Calculation:** Exact denominators 257+250=507 account for all reported interim enrollment. With all displayed inputs allowed half units, denominator sum[506,508] overlaps enrolled 507±.5=[506.5,507.5], gap 0: no numerical count mismatch is alleged. Bougie percentage recomputation [100×249.5/257.5,100×250.5/256.5]=[96.89320,97.66082] overlaps 97±.5=[96.5,97.5]; tube [100×212.5/250.5,100×213.5/249.5]=[84.83034,85.57114] overlaps 85±.5=[84.5,85.5]. Relative gaps are 0. Exact rates 97.276%/85.2% also reproduce displayed percentages. The unresolved comparison is population identification and its link to continuation, not percentage arithmetic or500 versus 507 timing.

The source does not report difficult-airway denominators/rates for this interim. The final 757-patient cohort contains 380 difficult-airway participants; therefore all 507 interim patients cannot have belonged to that subgroup under unchanged classification and complete final inclusion. Such a possibility would require a changed classification or inclusion specification, which the supplied package does not document. A separate difficult-only interim calculation might have existed but is not established by this display. The registered observable issue is the all-enrolled result presented as the supporting continuation calculation while the specified primary-subgroup result is not identified. Exact projection/test reproduction is not possible without the difficult-subgroup data and exact futility test definition.

**Affected result or extracted value:** Interim analysis population and continuation basis accompanying 250/257 (97%) versus 213/250 (85%) after 507 enrollment.

**Why context does not resolve it:** Route A, category 5: planned versus reported outcomes and analyses (or a plan-internal primary-analysis definition).

**Alternative source-grounded interpretations:** Displayed overall rates may supplement an unreported primary-only calculation, or a documented revision may have changed the interim population or classification. The suggestion that all 507 interim patients met the unchanged final primary definition does not reconcile with the final subgroup size of 380. No primary-subgroup futility result or undocumented revision is inferred.


Remaining source question: Was futility assessed in the difficult-airway primary subset or all 507 enrolled patients, and what primary-subgroup result or documented amendment supports the continuation decision?

**Mechanical evidence recheck:** All cited locations were found; source and comparator text/value matched. Yes for the original primary/interim specifications, observed overall denominators and the continuation sentence. **Exact missing inputs or definitions:** interim difficult-airway patient counts/successes, any separately performed primary-only result, exact projection/futility test and approved population amendment.


Evidence reproduced. Determining recheck fact: the reported continuation display accounts for all 507 enrolled and does not identify the difficult-airway primary-subgroup interim calculation specified by the original protocol. The state records this supplied-source mismatch/omitted planned result, not a conclusion about actual unseen implementation.

**Potential downstream evidence impact:** A design extraction could assign the all-enrolled interim rates to the primary difficult-airway decision rule or treat them as its reported result. No unseen interim implementation is inferred. No propagation or conclusion change is established by this review.

## Downstream Evidence-Chain Considerations

Published tables, abstracts, figures and plan summaries can become inputs to trial databases, systematic reviews, meta-analyses and guideline evidence tables. Population definitions and endpoint windows determine which results can be matched; denominator conventions determine which counts and percentages belong together; interval endpoints and P values can support different significance fields. The candidates identify specific points where those extracted fields may require clarification.

The observed printed comparisons do not establish that a downstream reviewer copied a value, that an estimate propagated, or that a clinical or synthesis conclusion changed. Alternatives remain source-grounded possibilities. No final replacement number, preferred analysis, severity or disposition is assigned. Each stable ID preserves the supplied evidence for later human adjudication.

## Limitations and Missing Definitions

The package contains no participant-level dataset, populated capture form, workbook, CSV, separate SAP, implemented allocation schedule or documented amendment history. Blank prospective forms specify capture options but do not demonstrate observed outcomes or implemented missing-data recovery. This is a supplied-evidence reporting review rather than a reanalysis.

Eight legacy page images are unavailable: main p. 11 and protocol pp. 1–4 and 23–25. All have usable source-matched native/layout text and complete mapping. One legacy main layout derivative places an unchanged axis label on a different line from current Poppler extraction; native text and source imagery resolve that derivative placement. Legacy image engine/version metadata was not retained. These are derivative limitations, not scientific-coverage gaps. Fresh targeted CPU source renders confirmed the main numerical tables and both time-to-success figures.

Exact binary difference-CI construction and unrounded endpoints are absent (C009, C011); original Hodges–Lehmann ranks, ties and interval output are absent (C010). The physician-cluster formula, weighting, covariance, variance estimator and test degrees of freedom are not supplied. Interaction model/scale and covariance, Cox coefficients and standard errors, and a numeric proportional-hazards statistic are also unavailable. Absence alone did not create candidates or authorize an assumed inferential method.

Implementation questions include the primary-subgroup criteria and operational-form version (C001), allocation strata (C002), hypoxemia capture and paired cuff/blade timing (C003–C004), closure trigger and joint rules or extension decisions (C005), planned KM percentile intervals/censoring percentages and any replacement specification (C006), row-specific availability/percentage bases (C007–C008), primary video-recovery implementation (C012), and interim primary-subgroup counts/successes, exact futility test and any population amendment (C013). These missing definitions limit explanations and numeric reconstruction; the direct-source discrepancies remain reproduced.

All 507 interim patients cannot belong to the unchanged difficult-airway primary subgroup under complete final inclusion because only 380 difficult-airway patients appear in the final 757-patient cohort. A separately performed but unreported primary-only interim calculation or a documented classification/population revision remains possible; neither is inferred as an actual implementation. Similarly, no effect on patient membership, event counts, treatment allocation, endpoint timings or recovered outcome status is inferred from the plan/report comparisons.

Direct OCR and Office conversion tools were unavailable but unnecessary for these native-text PDFs. No fallback environment, OCR or GPU was used. Stata was unavailable; the sample-size check is an explicitly labeled diagnostic, not execution of the original command. Complete limitations and report-curation notes are preserved in [limitations.md](review_1_6_2/limitations.md).

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

Workflow: 1.6.2. Routing preflight: PASS. Run model: gpt-6.1-sol; source: DEFAULT. Provider: CURRENT_SESSION. Execution mode: INTERACTIVE_CLI. Coordinator inference and all ten required preset model/effort pairs passed preflight. Rendering and source confirmation used the CPU; no GPU was requested or used.

Direct engines: Poppler 25.03.0 for PDF information, native/layout text and targeted source rendering; GNU coreutils sha256sum 9.7 for integrity. Python 3.13.5 is available for the approved local workflow helpers; Pandoc 3.1.11.1 is available for standalone HTML rendering. Reused legacy native text was matched to current sources; reused-image engine metadata is limited as stated above. Current-source recheck created three complete layout files and five targeted renders (main pp. 5–7 at 110 dpi; main p. 8 and support p. 4 at 100 dpi), each separately recorded in the evidence inventory and coverage manifest.

The [before-source hashes](review_1_6_2/source_hashes_before.sha256) and [before-reuse hashes](review_1_6_2/reused_artifact_hashes_before.sha256) record three direct sources and 47 reused assets. The independent pre-report quality audit recomputed and matched all 50 hashes. Final paired hash recomputation and mechanical validation are completed by the coordinator after Markdown assembly; their canonical records are [source hashes after](review_1_6_2/source_hashes_after.sha256), [reused-asset hashes after](review_1_6_2/reused_artifact_hashes_after.sha256), and [review validation](review_1_6_2/review_validation.json).

### Agent execution

Every runtime agent appears once below, as recorded in the [execution manifest](review_1_6_2/agent_execution_manifest.md). Specialist canonical task IDs omit the leading slash for validator syntax; prepending it restores the collaboration API ID. All specialist stages used fresh, distinct agents; statistical passes 1 and 2 used different high-effort IDs. No pass-2 inclusion screener was needed because pass 2 emitted no findings. Primary artifact paths are relative to review_1_6_2/.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129af-3c90-76c1-a2de-88a4033e022d | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_one | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/inclusion_one | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_two | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

The package-specific target is a planning range, never a source, relationship or candidate cap. The coordinator finalizes the finish and observed-duration fields immediately after this complete Markdown assembly; local HTML rendering and mechanical validation lie outside the review window.

- **Target basis:** Three native-text PDFs contain 49 pages; all 49 have byte-matched reusable native extraction, with six reusable text files and 41 reusable PNGs. No mandatory fresh extraction or Office conversion is needed; eight absent PNGs remain text-covered. Scope includes main tables/figures, a 25-page protocol, and mixed results/form support content. The 25–40 minute target allows parallel mapping and checker waves followed by mandatory screening, direct evidence recheck, a distinct second statistical pass, quality audit and complete report assembly; candidate count is not a planning input.
- **Total source units:** 49
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T06:39:19Z
- **Finished UTC:** 2026-10-11T07:25:24Z
- **Observed elapsed minutes:** 46.08
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Detailed direct-source confirmation and all-input display-precision refinement for C007 and C008; complete exclusion and candidate audit with C013 alternative clarification; full 13-card report assembly across mandatory sequential review waves; mechanical expansion of pass-1 relationship scope during validation
