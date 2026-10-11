# Quantitative Reporting Quality-Control Consistency Review — PROBESE

**Pending Human Adjudication**

This Workflow 1.6.2 review prepares source-linked candidate reporting issues for human adjudication. Inclusion audit and evidence-state labels record workflow checks; they are not scientific adjudications or proposed corrections.

# Executive Quality-Control Summary

The complete supplied package yielded **13 stable candidates**: eight in `statistical_results` and five in `protocol_report`. All 13 source comparisons were reproduced, and the independent inclusion audit returned CONFIRMED for all 13. Every candidate remains Pending Human Adjudication.

The review mapped all 100 pages of six supplied PDFs, reconstructed 120 numeric and 211 statistical relationships, and completed two independent statistical passes over all 211 relationships. Independent screening considered 22 checker findings: 13 were included and nine screened out, including six duplicate findings whose provenance remains attached to the corresponding candidates. Statistical pass 2 and the audit identified no additional issue requiring registration.

The candidate set concerns effect-measure identity, printed interval/test compatibility, a repeated binary-effect conditioning pattern, percentage contrasts, one same-display interval relation, and planned-versus-reported endpoint or analysis definitions. These observations identify possible extraction choices without asserting any clinical conclusion change or downstream propagation.

# Package and Reused-Evidence Provenance

The package contains the PROBESE randomized trial article and five supplements. Document roles follow content. Protocol, amendments and prospective SAP are PLAN; the publication, results supplement and data-sharing statement are REPORT.

| Source | Supplied filename | Content role | Pages |
|---|---|---|---:|
| DOC-001 | [jama_bluth_2019_oi_190055_16092.pdf](../jama_bluth_2019_oi_190055_16092.pdf#page=1) | REPORT: main article | 14 |
| DOC-002 | [joi190055supp1_prod_16092.pdf](../joi190055supp1_prod_16092.pdf#page=1) | PLAN: protocol version 2.6, October 2016 | 36 |
| DOC-003 | [joi190055supp2_prod_16092.pdf](../joi190055supp2_prod_16092.pdf#page=1) | PLAN: approved protocol changes | 3 |
| DOC-004 | [joi190055supp3_prod_16092.pdf](../joi190055supp3_prod_16092.pdf#page=1) | PLAN: updated SAP | 3 |
| DOC-005 | [joi190055supp4_prod_16092.pdf](../joi190055supp4_prod_16092.pdf#page=1) | REPORT: results eMethods, tables and figures | 43 |
| DOC-006 | [joi190055supp5_prod_16092.pdf](../joi190055supp5_prod_16092.pdf#page=1) | REPORT: data sharing | 1 |
| Total | Six PDFs; no Office, workbook or CSV source supplied | Three REPORT and three PLAN documents | 100 |

The curator inventoried and hashed 100 immutable reused assets: 12 complete native/layout text files, six PDF metadata files, 73 rendered PNGs and nine selected-page text files. Current Poppler outputs byte-match the reusable complete text. Reuse provided locators and transcriptions; supplied PDFs remained final evidence authority. Earlier candidate sets, checkers, screening decisions and reports were not scientific inputs. [Source inventory](review_1_6_2/source_inventory.md), [asset inventory](review_1_6_2/evidence_asset_inventory.md) and the two [source](review_1_6_2/source_hashes_before.sha256)/[reused-asset](review_1_6_2/reused_artifact_hashes_before.sha256) baseline manifests preserve provenance.

# Scope, Complete Coverage, and Exclusions

Scope comprises counts and denominators, estimates and tests, statistical method logic, and planned-versus-reported statistical design. Every source page received an explicit quantitative or no-applicable-result mapping, including administrative and reference pages. All result graphics were inspected; unlabeled plot coordinates were not converted into fabricated precise values.

| Source | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 14 | 14 | 0 | 14 | COMPLETE |
| DOC-002 | 36 | 36 | 0 | 36 | COMPLETE |
| DOC-003 | 3 | 3 | 0 | 3 | COMPLETE |
| DOC-004 | 3 | 3 | 0 | 3 | COMPLETE |
| DOC-005 | 43 | 43 | 0 | 43 | COMPLETE |
| DOC-006 | 1 | 1 | 0 | 1 | COMPLETE |
| Total | 100 | 100 | 0 | 100 | COMPLETE |

Reusable and fresh-required units partition the total for every source, and mapped units equal total units. Current confirmation derivatives do not change the initial fresh-required count. No scientific-coverage gap remains. The [source coverage](review_1_6_2/source_coverage.md) and [coverage manifest](review_1_6_2/coverage_manifest.md) provide complete closure.

The review excludes broad clinical or methodological critique, preferences for another analysis, novelty or misconduct assessment, and raw-data auditing. Immediately resolved wording, peripheral comparisons, unsupported procedural assumptions, explicitly modeled estimates compared only with crude ratios, and discrepancies within the prescribed display tolerance do not independently qualify. Printed interval/test conflicts retain Route A treatment even when rounded endpoints or different procedures offer an explanation.

# Quantitative and Statistical Relationship Coverage

| Evidence scope | Numeric relationships | Statistical relationships | Closure |
|---|---:|---:|---|
| Main article | 98 | 123 | Complete disjoint mapping |
| Support documents | 22 | 88 | Complete disjoint mapping |
| Total | 120 | 211 | Every relationship retained |

The [main map](review_1_6_2/extraction/main_quantitative_evidence.md) and [support map](review_1_6_2/extraction/support_quantitative_evidence.md) retain all table cells, intervals, P values, definitions and matching narrative locations. Numeric review covers all 120 numeric records and numeric applicability for all 211 statistical records. Cross-source review covers 130 disjoint comparisons: 51 result, 49 criterion/definition and 30 design/analysis comparisons.

[Statistical pass 1](review_1_6_2/checkers/statistical_pass_1.md) and [statistical pass 2](review_1_6_2/checkers/statistical_pass_2.md) each cover the same complete 211-record union in disjoint 101/110-record parts. The [statistical inventory](review_1_6_2/statistics/relationship_inventory.md) contains explicit completion records for each relationship in each pass. The two agents have distinct runtime IDs and high reasoning effort. Pass 2 reread all 13 stable candidates, all 22 screening decisions, all recheck facts and all 43 original checker exclusions; the [individual exclusion review](review_1_6_2/statistics/pass_2/excluded_observation_review.md) preserves every row. One original conditional log-rank exclusion is explicitly cross-referenced to included C005; it is not treated as an exclusion of that planned primary output.

# Inclusion Screening Summary

A reproduced issue qualifies through an always-register Route A category or through all three Route B criteria: in focus, not resolved by immediate context, and bearing on interpretation or extraction. For ordinary numeric comparisons, independent half-unit rounding intervals must leave a relative gap greater than 0.05, or a positive gap against a printed zero. Route A category 1 interval/test conflicts are not removed by this rounding rule. There was no expected candidate count.

| Decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 13 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 6 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 1 |
| SCREENED_OUT | OUT_OF_FOCUS | 1 |
| SCREENED_OUT | CONTEXT_RESOLVES | 1 |
| Total | 13 included + 9 screened out | 22 |

All other screening reason codes have zero findings. The 43 checker excluded-observation rows are a separate review input and are not additional findings or screening decisions. Every finding has one decision in the [screening log](review_1_6_2/screening/inclusion_screen.md), and each included anchor maps to one stable ID. No pass-2 or audit finding required a further screen. F-NUM-003's scalar duplicate target is C009, while its separately documented per-protocol edema portion remains provenance for C013. No screened-out finding receives an evidence card.

# Review-Domain Summary

`statistical_results` concerns counts, estimates, intervals, tests and statistical methods in REPORT materials. `report_internal_inconsistency` concerns unresolved attribution of a reported number to an outcome, time point or analysis set. `protocol_report` concerns PLAN-to-REPORT statistical design or analysis comparisons. `plan_material` concerns plan-internal design inconsistencies used by the reported analysis.

| Review domain | Candidates |
|---|---:|
| statistical_results | 8 |
| report_internal_inconsistency | 0 |
| protocol_report | 5 |
| plan_material | 0 |
| Total | 13 |

| Primary relationship type | Meaning | Candidates |
|---|---|---:|
| S_W | Within one REPORT | 7 |
| S_C | Between distinct REPORT documents | 1 |
| P_R | PLAN versus REPORT | 5 |
| P_P | Solely within PLAN material | 0 |
| Total | One primary relationship per candidate | 13 |

C003 additionally involves P_P, with P_R taking precedence. Repetition of an internal pattern across report displays does not itself add a cross-document conflict. A plan that only corroborates an internal report comparison does not add P_R.

| Evidence state | Candidates |
|---|---:|
| reproduced | 13 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 13 |

Inclusion audit: CONFIRMED 13; QUESTIONED 0. These are inclusion-threshold checks. All candidates remain Pending Human Adjudication.

# Candidate Index

| ID | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|
| C001 | statistical_results | S_C | reproduced | CONFIRMED |
| C002 | statistical_results | S_W | reproduced | CONFIRMED |
| C003 | protocol_report | P_R | reproduced | CONFIRMED |
| C004 | statistical_results | S_W | reproduced | CONFIRMED |
| C005 | protocol_report | P_R | reproduced | CONFIRMED |
| C006 | protocol_report | P_R | reproduced | CONFIRMED |
| C007 | statistical_results | S_W | reproduced | CONFIRMED |
| C008 | statistical_results | S_W | reproduced | CONFIRMED |
| C009 | statistical_results | S_W | reproduced | CONFIRMED |
| C010 | statistical_results | S_W | reproduced | CONFIRMED |
| C011 | protocol_report | P_R | reproduced | CONFIRMED |
| C012 | protocol_report | P_R | reproduced | CONFIRMED |
| C013 | statistical_results | S_W | reproduced | CONFIRMED |

# Candidate Evidence Cards

## C001 — Primary collapsed-composite RR/OR identity

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: The primary collapsed-composite tuple is labeled RR in the article and placed under an OR heading in the results supplement.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main article RR versus REPORT results supplement eFigure 12 OR

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Qualifying route:** Route B

**Reported-versus-comparator:** The primary collapsed-composite tuple is labeled RR in the article and placed under an OR heading in the results supplement. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** Primary PPC collapsed-composite effect .93 (.83–1.04), S054/S101/S108/S385; coding as RR versus OR.

**Why context does not resolve it:** Both RR and OR are plausible beside the distinct fitted global models. No row-specific collapsed OR fit or heading exception identifies the quantity to extract. This meets B1 method focus, B2 unresolved quantity identity and B3 extraction of the named primary tuple.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: Primary PPC collapsed-composite effect .93 (.83–1.04), S054/S101/S108/S385; coding as RR versus OR. No propagation, clinical conclusion change or participant impact is established.

Duplicate checker provenance retained separately: F-ST1-009.


**Exact source locations:** REPORT [main p. 1](../jama_bluth_2019_oi_190055_16092.pdf#page=1) abstract, [main p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4) primary binary methods, [main p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table 3, [main p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) Figure 2 versus REPORT [results p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure 12 collapsed-composite row. PLAN [SAP p. 2](../joi190055supp3_prod_16092.pdf#page=2) corroborates RR only.

**Source evidence:** Locations found: yes, all five REPORT locations and the corroborating PLAN location. Source value/text matched: main RR .93 (.83–1.04), 211/989 versus 233/987; comparator matched: eFigure 12 prints exactly .93 [.83,1.04] under its Odds Ratio (95% CI) global heading. The component section has its own Risk Ratio (99.58% CI) heading. The three other global rows are separately named count/common/average-effect OR models.

**Reasoning procedure:** Route B effect-measure identity applies because RR and OR are different extraction quantities. This is separate from C004's within-display conditioning comparison.

**Calculation:** Printed point copies [.925,.935] overlap; lower [.825,.835] and upper [1.035,1.045] copies also overlap. All copy gaps and relative discrepancies are zero. The inconsistency is the matched tuple's quantity label, not a numerical rounding discrepancy.

**Necessary inputs available; exact missing inputs or definitions:** All printed labels, populations and matched tuple are available. Missing: row-specific model/estimand definition for the eFigure collapsed-composite row, and an explicit exception to the global OR heading.

**Alternative source-grounded interpretations:** The global heading could group the RR row with OR rows; alternatively the collapsed row could be a separate OR fit producing the same rounded tuple. The source does not identify which applies.

**Direct observation versus inferred explanation:** Direct observation: exact tuple and competing headings. Inference only: any production or layout mechanism; no mechanism is established.

**Classification rationale:** Two distinct publication-results documents conflict about the effect measure; S_C and statistical_results follow. The SAP is corroboration and adds no P_R.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** The article labels .93 (.83–1.04) RR while the results figure places that identical collapsed tuple under OR. No ledger value/location transcription was changed.


## C002 — Abstract hypoxemia signed confidence limit

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: The abstract hypoxemia interval has a positive upper limit and includes zero despite P < .001; the matched table has a negative upper limit.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article abstract versus REPORT main article Table 3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-002

**Qualifying route:** Route A, category 1; independently Route A, category 2

**Reported-versus-comparator:** The abstract hypoxemia interval has a positive upper limit and includes zero despite P < .001; the matched table has a negative upper limit. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** Hypoxemia high-minus-low difference −8.6%, its signed upper confidence limit, and abstract null-inclusion reading; S085.

**Why context does not resolve it:** Route A, category 1; independently Route A, category 2 is an always-register category. The reproduced printed conflict or planned-versus-reported element remains registered with the source-grounded alternatives below; it does not require an additional Route B context argument.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: Hypoxemia high-minus-low difference −8.6%, its signed upper confidence limit, and abstract null-inclusion reading; S085. No propagation, clinical conclusion change or participant impact is established.

Duplicate checker provenance retained separately: F-XS-001, F-ST1-001.


**Exact source locations:** REPORT [main p. 1](../jama_bluth_2019_oi_190055_16092.pdf#page=1) Results hypoxemia versus [main p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table 3 hypoxemia, with [main p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) secondary interpretation and [main p. 11](../jama_bluth_2019_oi_190055_16092.pdf#page=11) discussion.

**Source evidence:** Locations found: yes. Source matched: abstract difference −8.6%, 95% CI −11.1% to +6.1%, P < .001 and 5.0% versus 13.6%. Comparator matched: Table 3 49/989 versus 134/987, −8.6 (−11.1 to −6.1), P < .001. Fresh source renders confirm the positive abstract upper limit and negative table upper limit. Both narrative locations support less hypoxemia with high PEEP.

**Reasoning procedure:** Route A categories 1 and 2 apply: the abstract interval crosses zero despite P < .001, and the sign changes the printed interval's significance reading.

**Calculation:** Upper-limit half-unit intervals [6.05,6.15] and [−6.15,−6.05] have gap 12.10 percentage points; gap/6.1 = 1.98361. Matching estimate and lower limit overlap. The abstract interval/P conflict has no rounding exclusion under category 1.

**Necessary inputs available; exact missing inputs or definitions:** Necessary signed limits, confidence level, P, contrast and population are available. Missing: authoritative abstract upper-limit sign and any separately intended abstract analysis.

**Alternative source-grounded interpretations:** The table and prose support a negative upper limit; a distinct abstract analysis is not identified. Reconstructable intended sign does not remove the printed abstract reading.

**Direct observation versus inferred explanation:** Direct observation: opposed signed limits and abstract null inclusion. A missing display sign is a possible explanation, not demonstrated computational provenance.

**Classification rationale:** Both conflicting values are in the same REPORT; S_W, statistical_results.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** The abstract prints +6.1 while the matching table prints −6.1, and the abstract interval crosses zero despite P < .001. No ledger value/location transcription was changed.


## C003 — Original secondary hierarchy and mortality follow-up

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: Original standalone secondary endpoints and the 90-day mortality window differ from the updated SAP and reported endpoint hierarchy.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN original protocol versus PLAN updated SAP and REPORT article/results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Qualifying route:** Route A, category 5

**Reported-versus-comparator:** Original standalone secondary endpoints and the 90-day mortality window differ from the updated SAP and reported endpoint hierarchy. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** Status and reporting windows of standalone postoperative ventilation, 30-day hospital readmission and 90-day mortality, including severe PPC and in-hospital mortality counterparts.

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced printed conflict or planned-versus-reported element remains registered with the source-grounded alternatives below; it does not require an additional Route B context argument.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: Status and reporting windows of standalone postoperative ventilation, 30-day hospital readmission and 90-day mortality, including severe PPC and in-hospital mortality counterparts. No propagation, clinical conclusion change or participant impact is established.


**Exact source locations:** PLAN [protocol p. 5](../joi190055supp1_prod_16092.pdf#page=5) synopsis and [protocol p. 12](../joi190055supp1_prod_16092.pdf#page=12) §7.1.2 versus PLAN [SAP p. 1](../joi190055supp3_prod_16092.pdf#page=1) updated outcome list and REPORT [main p. 3](../jama_bluth_2019_oi_190055_16092.pdf#page=3) Secondary Outcomes, [results p. 21](../joi190055supp4_prod_16092.pdf#page=21) §2.8. PLAN amendments [p. 1](../joi190055supp2_prod_16092.pdf#page=1), [p. 2](../joi190055supp2_prod_16092.pdf#page=2), [p. 3](../joi190055supp2_prod_16092.pdf#page=3) and REPORT [main p. 2](../jama_bluth_2019_oi_190055_16092.pdf#page=2) final-SAP identification were reread as context.

**Source evidence:** Locations found: yes, including all amendment pages. Source matched: original standalone postoperative invasive/noninvasive ventilation, hospital readmission within 30 days, and mortality at day 90; synopsis also states 90-day survival/mortality. Comparators matched: updated SAP and article identify severe PPC, in-hospital mortality and hospital-free days at 90; results definitions identify in-hospital and five-day death, not 90-day mortality or standalone hospital readmission. Severe respiratory failure includes ventilation within the composite, without reproducing the original standalone endpoint.

**Reasoning procedure:** Route A category 5 applies to the outcome hierarchy/windows. The supplied updated SAP explicitly states January 20, 2018 finalization and endorsement before last inclusion/database locking/statistical analysis; source-grounded prospective supersession must accompany this observation.

**Calculation:** Logical list/window comparison reproduced: in-hospital death is not the 90-day window; a ventilation-defined severe component is not the standalone ventilation endpoint; ICU readmission is not hospital readmission. Display-precision interval arithmetic is inapplicable to endpoint status and windows.

**Necessary inputs available; exact missing inputs or definitions:** Necessary original/final lists and disclosed timing are available. Missing: explicit endpoint-by-endpoint supersession/status record, standalone outcome locations, 90-day death output and amendment mapping. The supplied amendment list does not identify these particular changes.

**Alternative source-grounded interpretations:** The prospectively finalized final SAP may have superseded the earlier hierarchy. The article identifies that final SAP. This establishes a disclosed updated plan, not an assertion of undisclosed change or noncompliance.

**Direct observation versus inferred explanation:** Direct observation: differing lists/time windows and final-SAP timing. Inference only: whether any original outcome was collected, removed, absorbed or analyzed without display.

**Classification rationale:** Original PLAN versus final PLAN creates P_P; original PLAN versus reported endpoint list creates P_R. P_R takes precedence over P_P, giving protocol_report. No S_C/S_W conflict is inferred from the broad supplementary list.  

**Classification ambiguity:** The updated SAP explicitly documents prospective finalization; exact supersession of individual original endpoints remains unspecified.


**Mechanical evidence recheck:** The original endpoint lists and mortality window differ from the final SAP/report lists; final-SAP prospective timing is explicitly preserved. No ledger value/location transcription was changed.


## C004 — Repeated outcome-risk estimand identity

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: Repeated displayed binary effects track a conditional-allocation diagnostic rather than the outcome-risk orientation described by the report; the estimand mapping remains unidentified.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT binary-outcome labels and event counts versus REPORT displayed effect estimates within each display

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route B

**Reported-versus-comparator:** Repeated displayed binary effects track a conditional-allocation diagnostic rather than the outcome-risk orientation described by the report; the estimand mapping remains unidentified. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** All 33 main binary rows, all 13 per-protocol rows, all 11 Figure 2 rows including both S100 strata, all 12 eFigure 12 components, and abstract/narrative/method repetitions. All 57 numeric occurrences and 12 component repeats appear below with exact page links. Twenty-one arithmetic diagnostic gaps exceed .05: 13 main plus six per-protocol rows independently support the pattern, and two explicitly modeled subgroup rows are supporting diagnostics only. Near-equal and undefined-zero-control rows are not independent qualifying discrepancies.

**Why context does not resolve it:** The systematic source-linked orientation pattern is not mapped to an identified marginal/adjusted estimator, transformation or denominator definition in immediate context. This meets B1 estimand focus, B2 unresolved conditioning identity and B3 extraction of the named binary effects. Explicitly fitted estimates are not required to equal crude risks.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: All 33 main binary rows, all 13 per-protocol rows, all 11 Figure 2 rows including both S100 strata, all 12 eFigure 12 components, and abstract/narrative/method repetitions. All 57 numeric occurrences and 12 component repeats appear below with exact page links. Twenty-one arithmetic diagnostic gaps exceed .05: 13 main plus six per-protocol rows independently support the pattern, and two explicitly modeled subgroup rows are supporting diagnostics only. Near-equal and undefined-zero-control rows are not independent qualifying discrepancies. No propagation, clinical conclusion change or participant impact is established.

Duplicate checker provenance retained separately: F-ST1-004.


**Exact source locations:** REPORT [main p. 1](../jama_bluth_2019_oi_190055_16092.pdf#page=1) primary abstract; [main p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4) binary methods; [main p. 8](../jama_bluth_2019_oi_190055_16092.pdf#page=8) primary/mild/pleural narrative; [main p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) every Table 3 binary row; [main p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) continued rows, ratio notes and every Figure 2 row; [results p. 29](../joi190055supp4_prod_16092.pdf#page=29) every eTable 8 row; [results p. 42](../joi190055supp4_prod_16092.pdf#page=42) all twelve component rows. PLAN [SAP p. 2](../joi190055supp3_prod_16092.pdf#page=2) corroborates the incidence/RR terminology, not an opposing result.

**Source evidence:** Locations found: yes. Source value/text matched and comparator matched for every occurrence in the complete tables below: 57 numeric tuples and 12 component repeats, plus abstract/narrative/method repeats. Main columns and notes name RR of intervention outcomes; eTable 8 literally says Effect Estimate, retained without relabeling. Figure 2 is a source-described GLM subgroup analysis and eFigure 12 component fits use Bonferroni correction. Main p.8 repeats primary .93 (.83–1.04), mild .92 (.80–1.05), pleural 1.35 (1.14–1.62).

**Reasoning procedure:** Route B concerns the source-supported systematic estimand/conditioning identity: intended risk of event by arm versus a different conditional allocation quantity that reconstructs displayed values. Explicit modeled quantities are not forced to equal crude risks. C001 independently compares RR/OR headings; C009/C013 independently compare interval/test decisions.

**Calculation:** For high a/H and low b/L, R = (a/H)/(b/L). Diagnostic T = [a/(a+b)]/[(H−a)/(H+L−a−b)] conditions on event status rather than treatment arm. Half-unit R bounds = [(a−.5)/(H+.5)×(L−.5)/(b+.5), (a+.5)/(H−.5)×(L+.5)/(b−.5)] for b > .5, with nonnegative numerator clipping. Printed point allows ±.005; relative gap is the nonoverlap gap divided by the printed effect. Independent arithmetic reproduces pleural [1.97075,2.11980] versus [1.345,1.355], relative .45611, T 1.35795; hypoxemia [.35950,.37041] versus [.505,.515], relative .26390, T .51074; hypotension [1.82729,1.84769] versus [1.425,1.435], relative .27433, T 1.43123. Complete per-row reproduction follows. Zero-control DIC forward R is undefined; neither a finite R nor a finite relative discrepancy is assigned.

**Necessary inputs available; exact missing inputs or definitions:** Printed counts, totals, arm orientation, labels and point estimates are available for all applicable rows. Missing: actual response variable, denominator/conditioning variable, link, adjustment, marginalization, reference orientation and interval construction tying each stated binary effect to its output; raw data and analysis code are not supplied. Subgroup/component fitted parameters cannot be recovered from counts alone.

**Alternative source-grounded interpretations:** A separately fitted adjusted/marginal estimator or display transformation could differ from crude event risks; the report does not identify such a mapping for these binary columns. GLM subgroup and component effects remain modeled supporting occurrences. Diagnostic resemblance to a transposed table does not establish how the outputs were produced.

**Direct observation versus inferred explanation:** Direct observations: source labels/counts/effects and reproduced numerical conditioning pattern. Inferred explanation: transposed computation, coding, adjustment or display mechanism; none is established.

**Classification rationale:** The conflict is internal to each REPORT display; its recurrence in multiple REPORT documents adds occurrences, not an opposing matched-result S_C relationship. All relationships S_W and domain statistical_results. PLAN RR wording merely corroborates one side. The numeric checker's proposed S_C is corrected to S_W as already reflected in the ledger.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** All source occurrences retain the different conditioning identity, with reproduced above-.05 half-unit gaps in multiple binary rows and no reported estimand mapping. No ledger value/location transcription was changed.


### Complete repeated-occurrence recheck

Each row below was matched to the current source display, including the displayed arm/event order. The 57 input tuples comprise 33 Table 3 binary rows, 11 Figure 2 rows (both S100 strata retained), and 13 per-protocol rows. Table 3 and eTable 8 matching used current source renders; Figure 2 matching also used current direct layout text. Printed effect intervals in this arithmetic table are point-display half-unit intervals, not confidence intervals. Twenty-one of the 57 rows exceed .05 under the event-risk reading; one has undefined forward risk ratio; the remaining rows support the repeated identity pattern without individually qualifying as numeric discrepancies. Explicit modeled subgroup rows remain supporting diagnostics only.

| ID | Exact source / row | High a/H | Low b/L | Printed effect half-unit interval | Outcome-risk R | R half-unit interval | Conditional-allocation T | Relative gap | Recheck use |
|---|---|---|---|---|---:|---|---:|---:|---|
| S054 | [S054 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 211/989 | 233/987 | 0.93 [0.925, 0.935] | 0.90375 | [0.89877, 0.90876] | 0.93579 | 0.01747 | within display tolerance; support |
| S055 | [S055 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 135/989 | 154/987 | 0.92 [0.915, 0.925] | 0.87485 | [0.86791, 0.88184] | 0.92277 | 0.03604 | within display tolerance; support |
| S056 | [S056 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 42/989 | 58/987 | 0.83 [0.825, 0.835] | 0.72267 | [0.70725, 0.73838] | 0.83202 | 0.10436 | above .05 |
| S057 | [S057 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 30/989 | 36/987 | 0.90 [0.895, 0.905] | 0.83165 | [0.80577, 0.85829] | 0.90530 | 0.04079 | within display tolerance; support |
| S058 | [S058 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 44/989 | 55/987 | 0.88 [0.875, 0.885] | 0.79838 | [0.78141, 0.81569] | 0.88277 | 0.06740 | above .05 |
| S059 | [S059 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 43/989 | 21/987 | 1.35 [1.345, 1.355] | 2.04348 | [1.97075, 2.11980] | 1.35795 | 0.45611 | above .05 |
| S060 | [S060 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 14/989 | 18/987 | 0.87 [0.865, 0.875] | 0.77620 | [0.72752, 0.82773] | 0.87231 | 0.04284 | within display tolerance; support |
| S061 | [S061 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 17/989 | 9/987 | 1.31 [1.305, 1.315] | 1.88507 | [1.73158, 2.05674] | 1.31173 | 0.31800 | above .05 |
| S062 | [S062 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 12/989 | 10/987 | 1.09 [1.085, 1.095] | 1.19757 | [1.09192, 1.31446] | 1.09091 | 0.00000 | within display tolerance; support |
| S063 | [S063 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 10/989 | 10/987 | 0.99 [0.985, 0.995] | 0.99798 | [0.90202, 1.10415] | 0.99898 | 0.00000 | within display tolerance; support |
| S064 | [S064 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 2/989 | 1/987 | 1.33 [1.325, 1.335] | 1.99596 | [0.99697, 4.99494] | 1.33266 | 0.00000 | within display tolerance; support |
| S065 | [S065 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 3/989 | 1/987 | 1.50 [1.495, 1.505] | 2.99393 | [1.66161, 6.99292] | 1.50000 | 0.10441 | above .05 |
| S066 | [S066 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 1/989 | 3/987 | 0.50 [0.495, 0.505] | 0.33266 | [0.14242, 0.59939] | 0.49899 | 0.00000 | within display tolerance; support |
| S067 | [S067 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 116/989 | 134/987 | 0.91 [0.905, 0.915] | 0.86392 | [0.85613, 0.87178] | 0.91737 | 0.03651 | within display tolerance; support |
| S068 | [S068 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 167/989 | 150/987 | 1.06 [1.055, 1.065] | 1.11108 | [1.10296, 1.11927] | 1.06324 | 0.03581 | within display tolerance; support |
| S069 | [S069 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 93/989 | 83/987 | 1.06 [1.055, 1.065] | 1.11822 | [1.10443, 1.13219] | 1.06154 | 0.03719 | within display tolerance; support |
| S070 | [S070 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 18/989 | 15/987 | 1.09 [1.085, 1.095] | 1.19757 | [1.12561, 1.27457] | 1.09147 | 0.02808 | within display tolerance; support |
| S071 | [S071 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 7/989 | 10/987 | 0.82 [0.815, 0.825] | 0.69858 | [0.61717, 0.78868] | 0.82143 | 0.03210 | within display tolerance; support |
| S072 | [S072 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 7/989 | 8/987 | 0.93 [0.925, 0.935] | 0.87323 | [0.76239, 0.99899] | 0.93191 | 0.00000 | within display tolerance; support |
| S073 | [S073 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 65/989 | 56/987 | 1.07 [1.065, 1.075] | 1.15837 | [1.13813, 1.17899] | 1.07845 | 0.05900 | above .05 |
| S075 | [S075 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 31/989 | 32/987 | 0.98 [0.975, 0.985] | 0.96679 | [0.93562, 0.99899] | 0.98259 | 0.00000 | within display tolerance; support |
| S077 | [S077 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 29/989 | 23/987 | 1.11 [1.105, 1.115] | 1.25832 | [1.20909, 1.30978] | 1.11771 | 0.08476 | above .05 |
| S078 | [S078 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 9/989 | 9/987 | 0.99 [0.985, 0.995] | 0.99798 | [0.89202, 1.11652] | 0.99898 | 0.00000 | within display tolerance; support |
| S079 | [S079 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 2/989 | 2/987 | 0.99 [0.985, 0.995] | 0.99798 | [0.59818, 1.66498] | 0.99899 | 0.00000 | within display tolerance; support |
| S080 | [S080 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 1/989 | 0/987 | 2.00 [1.995, 2.005] | undefined | undefined | 1.99899 | not applied | zero control; no finite R |
| S082 | [S082 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 22/989 | 26/987 | 0.91 [0.905, 0.915] | 0.84444 | [0.80886, 0.88146] | 0.91382 | 0.02587 | within display tolerance; support |
| S083 | [S083 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 41/989 | 32/987 | 1.12 [1.115, 1.125] | 1.27866 | [1.24238, 1.31613] | 1.12743 | 0.10480 | above .05 |
| S085 | [S085 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 49/989 | 134/987 | 0.51 [0.505, 0.515] | 0.36493 | [0.35950, 0.37041] | 0.51074 | 0.26390 | above .05 |
| S086 | [S086 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 313/989 | 170/987 | 1.43 [1.425, 1.435] | 1.83745 | [1.82729, 1.84769] | 1.43123 | 0.27433 | above .05 |
| S087 | [S087 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 98/989 | 59/987 | 1.27 [1.265, 1.275] | 1.65766 | [1.63369, 1.68206] | 1.27433 | 0.28243 | above .05 |
| S088 | [S088 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=9) | 12/989 | 5/987 | 1.41 [1.405, 1.415] | 2.39515 | [2.08457, 2.77497] | 1.41538 | 0.47487 | above .05 |
| S089 | [S089 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 59/989 | 166/987 | 0.49 [0.485, 0.495] | 0.35470 | [0.35029, 0.35915] | 0.49371 | 0.25683 | above .05 |
| S090 | [S090 Table 3](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 491/989 | 439/987 | 1.10 [1.095, 1.105] | 1.11619 | [1.11266, 1.11973] | 1.10892 | 0.00696 | within display tolerance; support |
| S344 | [S344 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 186/917 | 209/912 | 0.92 [0.915, 0.925] | 0.88510 | [0.87965, 0.89058] | 0.92374 | 0.02654 | within display tolerance; support |
| S345 | [S345 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 119/917 | 140/912 | 0.90 [0.895, 0.905] | 0.84537 | [0.83790, 0.85289] | 0.90395 | 0.04679 | within display tolerance; support |
| S346 | [S346 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 38/917 | 51/912 | 0.84 [0.835, 0.845] | 0.74104 | [0.72339, 0.75905] | 0.84519 | 0.09042 | above .05 |
| S347 | [S347 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 25/917 | 35/912 | 0.83 [0.825, 0.835] | 0.71039 | [0.68563, 0.73590] | 0.82633 | 0.10734 | above .05 |
| S348 | [S348 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 3/917 | 1/912 | 1.50 [1.495, 1.505] | 2.98364 | [1.65577, 6.96945] | 1.49754 | 0.10051 | above .05 |
| S349 | [S349 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 11/917 | 10/912 | 1.04 [1.035, 1.045] | 1.09400 | [0.99346, 1.20524] | 1.04531 | 0.00000 | within display tolerance; support |
| S350 | [S350 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 14/917 | 14/912 | 0.99 [0.985, 0.995] | 0.99455 | [0.92495, 1.06939] | 0.99723 | 0.00000 | within display tolerance; support |
| S351 | [S351 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 10/917 | 9/912 | 1.05 [1.045, 1.055] | 1.10505 | [0.99346, 1.22990] | 1.05031 | 0.00000 | within display tolerance; support |
| S352 | [S352 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 2/917 | 1/912 | 1.33 [1.325, 1.335] | 1.98909 | [0.99346, 4.97818] | 1.33042 | 0.00000 | within display tolerance; support |
| S353 | [S353 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 38/917 | 18/912 | 1.37 [1.365, 1.375] | 2.09960 | [2.01377, 2.19040] | 1.36872 | 0.46626 | above .05 |
| S354 | [S354 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 38/917 | 50/912 | 0.85 [0.845, 0.855] | 0.75586 | [0.73772, 0.77438] | 0.85528 | 0.08308 | above .05 |
| S355 | [S355 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 15/917 | 7/912 | 1.36 [1.355, 1.365] | 2.13117 | [1.92069, 2.37421] | 1.36590 | 0.40860 | above .05 |
| S356 | [S356 eTable 8](../joi190055supp4_prod_16092.pdf#page=29) | 1/917 | 2/912 | 0.66 [0.655, 0.665] | 0.49727 | [0.19869, 0.99564] | 0.66448 | 0.00000 | within display tolerance; support |
| S092 | [S092 Figure 2](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 79/240 | 74/253 | 1.09 [1.085, 1.095] | 1.12539 | [1.10627, 1.14486] | 1.09041 | 0.01034 | modeled supporting diagnostic |
| S093 | [S093 Figure 2](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 130/740 | 156/727 | 0.88 [0.875, 0.885] | 0.81869 | [0.81183, 0.82561] | 0.88003 | 0.05613 | modeled supporting diagnostic |
| S094 | [S094 Figure 2](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 76/336 | 94/376 | 0.93 [0.925, 0.935] | 0.90476 | [0.89154, 0.91817] | 0.93195 | 0.00735 | modeled supporting diagnostic |
| S095 | [S095 Figure 2](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 135/653 | 139/611 | 0.94 [0.935, 0.945] | 0.90876 | [0.90072, 0.91687] | 0.94165 | 0.01929 | modeled supporting diagnostic |
| S096 | [S096 Figure 2](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 88/317 | 112/342 | 0.88 [0.875, 0.885] | 0.84768 | [0.83657, 0.85893] | 0.88192 | 0.01827 | modeled supporting diagnostic |
| S097 | [S097 Figure 2](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 123/672 | 121/645 | 0.99 [0.985, 0.995] | 0.97569 | [0.96625, 0.98521] | 0.98524 | 0.00000 | modeled supporting diagnostic |
| S098 | [S098 Figure 2](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 32/126 | 25/126 | 1.16 [1.155, 1.165] | 1.28000 | [1.22553, 1.33710] | 1.16461 | 0.05218 | modeled supporting diagnostic |
| S099 | [S099 Figure 2](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 179/863 | 208/861 | 0.90 [0.895, 0.905] | 0.85858 | [0.85314, 0.86406] | 0.90410 | 0.03438 | modeled supporting diagnostic |
| S100 below1 | [S100 below1 Figure 2](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 97/467 | 100/457 | 0.97 [0.965, 0.975] | 0.94923 | [0.93761, 0.96099] | 0.96747 | 0.00413 | modeled supporting diagnostic |
| S100 at least1 | [S100 at least1 Figure 2](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 98/447 | 112/449 | 0.92 [0.915, 0.925] | 0.87891 | [0.86860, 0.88934] | 0.91729 | 0.02789 | modeled supporting diagnostic |
| S101 | [S101 Figure 2](../jama_bluth_2019_oi_190055_16092.pdf#page=10) | 211/989 | 233/987 | 0.93 [0.925, 0.935] | 0.90375 | [0.89877, 0.90876] | 0.93579 | 0.01747 | modeled supporting diagnostic |

All twelve component occurrences were separately source-matched in the current eFigure 12 image. These are explicitly modeled component estimates with 99.58% Bonferroni intervals; event-risk recomputations remain diagnostics, not an equality imposed on those fitted estimates. Their count comparators are the matching main Table 3 rows, not counts invented from the figure. Numerical copy changes .90→.91, .99→1.00 and 1.35→1.36 have zero half-unit gap and are not separate cross-report discrepancies.

| ID | Exact source component | Main count comparator | Printed RR and 99.58% CI | R half-unit diagnostic | Relative diagnostic gap | Source/comparator match |
|---|---|---|---|---:|---|
| S373 | [mild](../joi190055supp4_prod_16092.pdf#page=42) | [S055](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 135/989; 154/987 | 0.92 (.76–1.12) | [0.86791, 0.88184] | 0.03604 | both matched; model-based support |
| S374 | [moderate](../joi190055supp4_prod_16092.pdf#page=42) | [S056](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 42/989; 58/987 | 0.83 (.59–1.17) | [0.70725, 0.73838] | 0.10436 | both matched; model-based support |
| S375 | [severe](../joi190055supp4_prod_16092.pdf#page=42) | [S057](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 30/989; 36/987 | 0.91 (.61–1.34) | [0.80577, 0.85829] | 0.05133 | both matched; model-based support |
| S376 | [aspiration](../joi190055supp4_prod_16092.pdf#page=42) | [S064](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 2/989; 1/987 | 1.33 (.41–4.30) | [0.99697, 4.99494] | 0.00000 | both matched; model-based support |
| S377 | [bronchospasm](../joi190055supp4_prod_16092.pdf#page=42) | [S062](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 12/989; 10/987 | 1.09 (.62–1.91) | [1.09192, 1.31446] | 0.00000 | both matched; model-based support |
| S378 | [ARDS](../joi190055supp4_prod_16092.pdf#page=42) | [S065](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 3/989; 1/987 | 1.50 (.65–3.44) | [1.66161, 6.99292] | 0.10441 | both matched; model-based support |
| S379 | [infection](../joi190055supp4_prod_16092.pdf#page=42) | [S063](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 10/989; 10/987 | 1.00 (.52–1.90) | [0.90202, 1.10415] | 0.00000 | both matched; model-based support |
| S380 | [atelectasis](../joi190055supp4_prod_16092.pdf#page=42) | [S058](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 44/989; 55/987 | 0.88 (.64–1.23) | [0.78141, 0.81569] | 0.06740 | both matched; model-based support |
| S381 | [edema](../joi190055supp4_prod_16092.pdf#page=42) | [S061](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 17/989; 9/987 | 1.31 (.87–1.98) | [1.73158, 2.05674] | 0.31800 | both matched; model-based support |
| S382 | [pleural](../joi190055supp4_prod_16092.pdf#page=42) | [S059](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 43/989; 21/987 | 1.36 (1.05–1.76) | [1.97075, 2.11980] | 0.44541 | both matched; model-based support |
| S383 | [pneumothorax](../joi190055supp4_prod_16092.pdf#page=42) | [S066](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 1/989; 3/987 | 0.50 (.04–5.96) | [0.14242, 0.59939] | 0.00000 | both matched; model-based support |
| S384 | [infiltrates](../joi190055supp4_prod_16092.pdf#page=42) | [S060](../jama_bluth_2019_oi_190055_16092.pdf#page=9): 14/989; 18/987 | 0.87 (.49–1.55) | [0.72752, 0.82773] | 0.04284 | both matched; model-based support |

## C005 — Planned primary log-rank output

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: The planned primary log-rank comparison has no identifiable reported counterpart in the supplied package.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP primary log-rank comparison versus REPORT Cox/time-to-PPC outputs

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-008

**Qualifying route:** Route A, category 5

**Reported-versus-comparator:** The planned primary log-rank comparison has no identifiable reported counterpart in the supplied package. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** Test identity and reporting provenance of the prespecified primary time-to-PPC comparison, including eFigure 8 HR .88 (.73–1.06), P .190.

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced printed conflict or planned-versus-reported element remains registered with the source-grounded alternatives below; it does not require an additional Route B context argument.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: Test identity and reporting provenance of the prespecified primary time-to-PPC comparison, including eFigure 8 HR .88 (.73–1.06), P .190. No propagation, clinical conclusion change or participant impact is established.


**Exact source locations:** PLAN [SAP p. 2](../joi190055supp3_prod_16092.pdf#page=2) primary analysis versus REPORT [main p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4) time-to-PPC methods and [results p. 38](../joi190055supp4_prod_16092.pdf#page=38) eFigure 8. Negative-search context: REPORT [main p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10), [main p. 11](../jama_bluth_2019_oi_190055_16092.pdf#page=11), [results p. 30](../joi190055supp4_prod_16092.pdf#page=30) eTable 9 and [results p. 42](../joi190055supp4_prod_16092.pdf#page=42) eFigure 12; PLAN [SAP p. 3](../joi190055supp3_prod_16092.pdf#page=3).

**Source evidence:** Locations found: yes. Source matched: SAP explicitly says Kaplan–Meier curves will be compared with log-rank tests. Comparator matched: article describes Cox proportional hazards output; current figure gives HR .88 (95% CI .73–1.06), P = .190, and Schoenfeld-residual P = .05. The supplied report has no test label identifying a log-rank counterpart.

**Reasoning procedure:** Route A category 5 applies to an identifiable output for the planned primary comparison. The observed fact is absence of an identified counterpart, not proof that the planned test was never performed.

**Calculation:** Fresh complete current main pp.1–14 and results pp.1–43 layout extractions were searched for log-rank/log rank, with direct page reading and current visual reading of image-only sensitivity/time-to-event displays. No named log-rank output was located. The .190 P is separately reproduced but its test identity is unspecified. Display-precision arithmetic is inapplicable to that identity/coverage comparison.

**Necessary inputs available; exact missing inputs or definitions:** Plan test and reported figure/methods are available. Missing: test provenance of eFigure 8's .190, named log-rank statistic/P, and explicit replacement or omission statement.

**Alternative source-grounded interpretations:** The displayed P could be log-rank even beside the HR/Cox discussion; the planned comparison may have been replaced, performed without an identified output, or omitted. None is established.

**Direct observation versus inferred explanation:** Direct observation: planned named test and report labels/search result. Inferred explanation: nonperformance or substitution; not asserted.

**Classification rationale:** The actual contrast is PLAN versus REPORT planned primary output; P_R, protocol_report. Multiple report locations corroborate the same unidentified counterpart and add no S_C.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** The SAP explicitly names log-rank; complete current REPORT searches and visual displays locate no output identified as that comparison. No ledger value/location transcription was changed.


## C006 — Planned primary clinical-severity-weighted GEE

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: The planned clinical-severity-weighted primary-composite GEE has no identified weights or weighted result among the supplied sensitivity outputs.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP weighted primary GEE versus REPORT identified primary sensitivity outputs

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-009

**Qualifying route:** Route A, category 5

**Reported-versus-comparator:** The planned clinical-severity-weighted primary-composite GEE has no identified weights or weighted result among the supplied sensitivity outputs. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** Identification of the planned clinical-severity-weighted primary sensitivity effect, distinct from site-random, count, common-effect, heterogeneity and average-effect analyses.

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced printed conflict or planned-versus-reported element remains registered with the source-grounded alternatives below; it does not require an additional Route B context argument.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: Identification of the planned clinical-severity-weighted primary sensitivity effect, distinct from site-random, count, common-effect, heterogeneity and average-effect analyses. No propagation, clinical conclusion change or participant impact is established.

Duplicate checker provenance retained separately: F-ST1-008.


**Exact source locations:** PLAN [SAP p. 3](../joi190055supp3_prod_16092.pdf#page=3) clinical severity weight versus REPORT [main p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4) sensitivity methods, [main p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) additional analysis, [main p. 11](../jama_bluth_2019_oi_190055_16092.pdf#page=11) sensitivity discussion, [results p. 30](../joi190055supp4_prod_16092.pdf#page=30) all eTable 9 rows/footnotes and [results p. 42](../joi190055supp4_prod_16092.pdf#page=42) all eFigure 12 component/global rows.

**Source evidence:** Locations found: yes. Source matched: SAP separately specifies a posteriori clinical component weights and a common-effect GEE applying them. Comparators matched: eTable 9 random-effect OR .86 (.68–1.08), P .19; count mean .35(.88)/.38(.86), proportional-odds .88 (.72–1.09), P .25; common GEE .93 (.80–1.08), P .37; treatment-component interaction P .11; average relative GEE .99 (.94–1.05), P .98. Footnotes identify common effect across 12 components but no severity weighting. eFigure 12 reproduces common/count/average outputs alongside all twelve modeled components and collapsed .93 (.83–1.04), with no weights or weighted label.

**Reasoning procedure:** Route A category 5 applies to the distinctly planned primary-composite severity-weighted sensitivity analysis, independently from C005's time-to-event comparison.

**Calculation:** Every sensitivity row was matched, including S357–S361, S373–S388, and linked plan/report method relationships S110/S123/S318. Fresh complete report-text search for severity weight, clinical severity, weighted and sensitivity identifies no weight/result mapping; current image-only display reading supplies the necessary visual check. Numeric copies overlap at their stated precision. No numeric computation of a weighted OR is possible without weights and model inputs; display-precision exclusion is inapplicable to the absent identification.

**Necessary inputs available; exact missing inputs or definitions:** Necessary distinct plan specification and complete displayed sensitivity list are available. Missing: all twelve clinical severity weights, weighted model definition and result provenance, or explicit omission statement. Clinical weighting cannot be reconstructed from raw component counts alone.

**Alternative source-grounded interpretations:** A displayed common-effect or average-effect row could incorporate weights without stating them; alternatively weighting was performed without report or omitted. The report identifies no such explanation.

**Direct observation versus inferred explanation:** Direct observation: separate planned weighting bullet and no identified weighted output. Inference only: whether weighting was actually performed and which unlabelled output contains it.

**Classification rationale:** PLAN versus REPORT primary sensitivity specification gives P_R and protocol_report. No statistical-results relationship is added by internally agreeing sensitivity copies.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** The SAP specifies a separate weighted GEE, while every sensitivity row/footnote identifies neither severity weights nor a weighted counterpart. No ledger value/location transcription was changed.


## C007 — Table 2 null-endpoint/significant-P pattern

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: Three Table 2 printed intervals include zero while their accompanying P values are significant at .05.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT Table 2 printed intervals versus REPORT same-row P values

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 1

**Reported-versus-comparator:** Three Table 2 printed intervals include zero while their accompanying P values are significant at .05. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** First-hour tidal volume, last-hour tidal volume and last-hour respiratory-rate intervals and accompanying tests; S002/S003/S016.

**Why context does not resolve it:** Route A, category 1 is an always-register category. The reproduced printed conflict or planned-versus-reported element remains registered with the source-grounded alternatives below; it does not require an additional Route B context argument.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: First-hour tidal volume, last-hour tidal volume and last-hour respiratory-rate intervals and accompanying tests; S002/S003/S016. No propagation, clinical conclusion change or participant impact is established.


**Exact source locations:** REPORT [main p. 7](../jama_bluth_2019_oi_190055_16092.pdf#page=7) Table 2 S002/S003/S016 and [main p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4) two-sided significance definition.

**Source evidence:** Locations found: yes, every pattern row. Source and comparator matched: tidal volume first hour .1 (0 to .2), P .007; tidal volume last hour .1 (0 to .2), P .008; respiratory rate last hour −.4 (−.7 to 0), P .02. The current source image confirms each zero endpoint and P glyph.

**Reasoning procedure:** Route A category 1 applies to the printed 95% interval/test decisions at two-sided .05. All three intervals include the difference null zero; every P is below .05.

**Calculation:** First and last-hour tidal volume lower limit printed 0 at the table's one-decimal scale permits [−.05,.05]; their P rounding intervals [.0065,.0075] and [.0075,.0085] stay below .05. Respiratory upper 0 permits [−.05,.05], P [.015,.025] stays below .05. Unrounded endpoints could exclude zero, but category 1 does not allow this display-precision explanation to remove the printed conflict. No gap/relative-discrepancy threshold is used.

**Necessary inputs available; exact missing inputs or definitions:** Necessary contrast, confidence and significance levels and tuples are available. Missing: unrounded endpoints, row-specific interval procedure, test statistic/SE, and whether each interval and P use the same procedure.

**Alternative source-grounded interpretations:** Rounding of an excluding endpoint to zero or separate interval/test procedures could explain the displayed opposition; both remain alternatives for each row.

**Direct observation versus inferred explanation:** Direct observation: all three zero-containing intervals and significant printed P values. Inference only: underlying unrounded significance or procedure generating the endpoints.

**Classification rationale:** All conflicts occur within one Table 2 REPORT; S_W, statistical_results.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** All three source intervals include printed null zero and each accompanying P is significant at .05. No ledger value/location transcription was changed.


## C008 — Monitoring/reversal displayed percentage contrasts

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: The monitoring and reversal percentage contrasts do not reconcile with the displayed absolute differences beyond display precision.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT Table 2 printed percentages versus REPORT absolute differences and fractions

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-003

**Qualifying route:** Route A, category 2; independently Route B

**Reported-versus-comparator:** The monitoring and reversal percentage contrasts do not reconcile with the displayed absolute differences beyond display precision. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** Monitoring and reversal percentages and high-minus-low percentage-point differences; S038/S039.

**Why context does not resolve it:** Route A category 2 retains the magnitude/direction-changing printed contrasts. Independently, Route B applies because the table does not identify the competing percentage and difference populations, and an extractor could take either contrast. Individual fraction/percentage residuals within .05 do not resolve the distinct contrast discrepancy.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: Monitoring and reversal percentages and high-minus-low percentage-point differences; S038/S039. No propagation, clinical conclusion change or participant impact is established.


**Exact source locations:** REPORT [main p. 8](../jama_bluth_2019_oi_190055_16092.pdf#page=8) continued Table 2 monitoring/reversal rows S038/S039, preceding neuromuscular-blockade row and monitoring note d.

**Source evidence:** Locations found: yes, both rows. Source matched: monitoring 632/982 (64.9%) versus 651/984 (67.7%), difference −1.8 (−6.0 to 2.4), P .40; reversal 724/982 (74.3%) versus 723/984 (75.2%), difference +.2 (−3.6 to 4.1), P .90. Comparator matched: printed percentages imply high-minus-low −2.8 and −.9, respectively. The fractions independently support the displayed contrast's alternative denominator reading.

**Reasoning procedure:** Route A category 2 / Route B apply to the printed magnitude/direction contradiction in explicit percentage contrasts. The issue is not each individual small count/percentage residual.

**Calculation:** Monitoring displayed percentages imply [−2.90,−2.70] versus printed contrast [−1.85,−1.75]; gap .85, relative .47222. Reversal implies [−1.00,−.80] versus [.15,.25]; gap .95, relative 4.75 and opposed sign. Exact printed fractions give monitoring −1.800084% and reversal +.251478%. Independent ±.5 count/denominator propagation gives fraction-difference intervals [−1.96820,−1.63197] and [.07487,.42808], both overlapping their printed contrast intervals. Individual fraction-versus-percent residuals remain within .05 relative tolerance.

**Necessary inputs available; exact missing inputs or definitions:** All fractions, percentages, contrasts and displayed reference populations are available. Missing: actual denominator for each percentage and intended population of the difference column. Preceding blockade counts 974/961 resemble an alternative percentage denominator but the table does not assign them to these row fractions.

**Alternative source-grounded interpretations:** The percentages may use blockade-treated denominators while fractions/difference use monitored/reversal-available populations, or the displayed percentages/contrasts may need a denominator explanation. Those denominators are not silently assigned.

**Direct observation versus inferred explanation:** Direct observation: two arithmetic conflicts and fraction/difference reconciliation under half-unit precision. Inference only: denominator reuse or production mechanism.

**Classification rationale:** Both conflicts occur within one REPORT table; S_W, statistical_results.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** Both percentage-derived contrast intervals remain disjoint from displayed contrast intervals, with relative gaps .47222 and 4.75. No ledger value/location transcription was changed.


## C009 — DIC interval/test compatibility

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: The DIC ratio interval excludes one while its accompanying P > .99 is nonsignificant.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT Table 3 DIC interval versus REPORT same-row P value

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-005

**Qualifying route:** Route A, category 1

**Reported-versus-comparator:** The DIC ratio interval excludes one while its accompanying P > .99 is nonsignificant. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** DIC RR 2.00 (1.91–2.09), its null-exclusion reading and P > .99; S080.

**Why context does not resolve it:** Route A, category 1 is an always-register category. The reproduced printed conflict or planned-versus-reported element remains registered with the source-grounded alternatives below; it does not require an additional Route B context argument.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: DIC RR 2.00 (1.91–2.09), its null-exclusion reading and P > .99; S080. No propagation, clinical conclusion change or participant impact is established.

Duplicate checker provenance retained separately: Primary DIC portion of F-NUM-003.


**Exact source locations:** REPORT [main p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table 3 DIC S080 and [main p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) notes b/c.

**Source evidence:** Locations found: yes. Source matched: DIC 1/989 (.1%) versus 0/987; RR 2.00 (1.91–2.09), P > .99. Comparator matched: same-row χ² P is nonsignificant and RD .1 (−.1 to .3) includes zero. Notes b/c explicitly name the ratio interval approximation and χ² test.

**Reasoning procedure:** Route A category 1 applies: 95% ratio interval excludes null one while same-row P is nonsignificant at .05. This rule is independent of C004's point estimand identity and C013's separate sparse-event result.

**Calculation:** Lower bound half-unit [1.905,1.915] and upper [2.085,2.095] remain above one. Point [1.995,2.005] lies inside the displayed interval. P > .99 remains above .05. The RD interval has lower [−.15,−.05], upper [.25,.35] and contains zero. Category 1 uses no rounding/relative gap exclusion; zero control events do not supply a finite crude RR.

**Necessary inputs available; exact missing inputs or definitions:** Necessary labels, event counts, null, confidence level, P and named methods are available. Missing: zero-cell handling, exact ratio/interval parameterization, SE/covariance and hypothesis-test implementation.

**Alternative source-grounded interpretations:** Named Wald-style interval and χ² test could use distinct sparse-data approximations; unspecified zero-cell handling may be relevant. These are retained explanations, not evidence that the printed null-inclusion decisions agree.

**Direct observation versus inferred explanation:** Direct observation: opposed interval/test significance readings. Inference only: how sparse cells or the conditional identity pattern produced the narrow interval.

**Classification rationale:** Internal same-row REPORT conflict gives S_W, statistical_results.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** The exact DIC ratio interval excludes one while the same-row P > .99 is nonsignificant. No ledger value/location transcription was changed.


## C010 — Mortality same-display interval relation

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: The mortality interval does not reproduce the log-symmetric relation that reproduces neighboring intervals in the same display.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT Table 3 mortality interval versus REPORT same-display comparator interval relation

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-006

**Qualifying route:** Route A, category 4

**Reported-versus-comparator:** The mortality interval does not reproduce the log-symmetric relation that reproduces neighboring intervals in the same display. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** In-hospital mortality RR 1.41 (.95–1.81), particularly the lower confidence limit; S088.

**Why context does not resolve it:** Route A, category 4 is an always-register category. The reproduced printed conflict or planned-versus-reported element remains registered with the source-grounded alternatives below; it does not require an additional Route B context argument.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: In-hospital mortality RR 1.41 (.95–1.81), particularly the lower confidence limit; S088. No propagation, clinical conclusion change or participant impact is established.


**Exact source locations:** REPORT [main p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table 3 in-hospital mortality S088 and pleural/hypoxemia/bradycardia comparators; [main p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) note b and vasoactive comparator.

**Source evidence:** Locations found: yes, all five tuples and common note. Source matched: mortality 12/989 versus 5/987, RR 1.41 (.95–1.81), P .09. Comparator matched: pleural 1.35 (1.14–1.62), hypoxemia .51 (.40–.65), bradycardia 1.27 (1.11–1.45), vasoactive 1.10 (1.01–1.21).

**Reasoning procedure:** Route A category 4 uses the log-symmetric ratio relation point² = lower×upper that reproduces neighboring intervals under the common interval footnote. This is a same-display algebra diagnostic, not a variance assumption or crude-risk equality. Mortality's interval/P both give nonsignificance, so this ID is not a duplicate interval/test conflict.

**Calculation:** Allow point [1.405,1.415] and upper [1.805,1.815]. Recomputed lower interval [1.087617,1.109266] versus printed [.945,.955] gives gap .132617, relative .139597. Neighboring recomputed lower intervals: pleural [1.113246,1.136858] versus [1.135,1.145]; hypoxemia [.389351,.411202] versus [.395,.405]; bradycardia [1.099811,1.125000] versus [1.105,1.115]; vasoactive [.986852,1.013299] versus [1.005,1.015]. Each comparator overlaps its printed lower half-unit interval; all comparator gaps zero. Independently recomputed in JavaScript.

**Necessary inputs available; exact missing inputs or definitions:** Necessary point and endpoint tuples and shared method footnote are available. Missing: mortality-specific asymmetric or non-log interval procedure, exception to the shared method, unrounded inputs and covariance/SE.

**Alternative source-grounded interpretations:** A mortality-specific asymmetric interval procedure can explain departure from log symmetry, but the shared footnote identifies no row-specific exception. The source does not establish the computation mechanism.

**Direct observation versus inferred explanation:** Direct observation: mortality tuple and source-supported same-display algebra discrepancy. Inference only: why this interval differs or which limit/estimator was intended.

**Classification rationale:** All compared methods/tuples are inside the same REPORT display; S_W, statistical_results.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** Mortality's lower endpoint remains separated by relative .139597 from the half-unit log-symmetric reconstruction that overlaps four same-display comparator limits. No ledger value/location transcription was changed.


## C011 — Mild/moderate respiratory-failure flow boundary

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: Protocol and report criteria assign different mild/moderate respiratory-failure membership through the report's explicit 2 L/min flow boundary.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN respiratory-failure components versus REPORT oxygen-flow criteria

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006

**Qualifying route:** Route A, category 5

**Reported-versus-comparator:** Protocol and report criteria assign different mild/moderate respiratory-failure membership through the report's explicit 2 L/min flow boundary. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** Mild and moderate respiratory-failure definitions and severe PPC composite excluding mild; printed counts 135/154, 42/58 and 116/134 are context, not demonstrated changed totals.

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced printed conflict or planned-versus-reported element remains registered with the source-grounded alternatives below; it does not require an additional Route B context argument.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: Mild and moderate respiratory-failure definitions and severe PPC composite excluding mild; printed counts 135/154, 42/58 and 116/134 are context, not demonstrated changed totals. No propagation, clinical conclusion change or participant impact is established.


**Exact source locations:** PLAN [protocol p. 31](../joi190055supp1_prod_16092.pdf#page=31) pulmonary definitions versus REPORT [main p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10) Table 3 note d and [results p. 20](../joi190055supp4_prod_16092.pdf#page=20) §2.8, with PLAN [SAP p. 1](../joi190055supp3_prod_16092.pdf#page=1) severe-composite definition and REPORT [main p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) affected counts.

**Source evidence:** Locations found: yes. Source matched: protocol mild responds to supplemental oxygen without a stated flow split; moderate persists despite supplemental oxygen. Comparators matched: main mild responds to 2 L or less and moderate only to greater than 2 L; results mild prints =2 L/min and moderate >2 L/min. Current renders confirm the = symbol in results, inclusive prose in main, and absence of a protocol flow boundary.

**Reasoning procedure:** Route A category 5 applies to primary-composite component definitions and the severe composite excluding mild. A responder only at >2 L/min can satisfy report moderate criteria but the original protocol's responding-to-oxygen mild criterion; therefore the operational lists differ.

**Calculation:** Logical membership comparison reproduced. A flow-responsive case at 3 L/min illustrates distinct criteria without claiming such a participant existed. The printed 2 L threshold is an operational cutpoint, not a rounded continuous estimate; half-unit display intervals do not turn unbounded response wording into the specified split. Relevant source counts: mild 135/154, moderate 42/58, severe PPC composite 116/134.

**Necessary inputs available; exact missing inputs or definitions:** Necessary component and severe-composite definitions/counts are available. Missing: operational oxygen-flow algorithm, patient-level responses/flows, and approved clarification/revision mapping. Actual recategorization and numeric impact cannot be calculated.

**Alternative source-grounded interpretations:** The report may supply an intended operational refinement or clarification of the protocol. Supplement =2 versus main ≤2 is kept as shorthand context, not a separately registered issue.

**Direct observation versus inferred explanation:** Direct observation: different component rules. Inference only: whether any patient changed category, the reason for the specification or its approval.

**Classification rationale:** Prospective PLAN definitions versus REPORT operational definition gives P_R, protocol_report. SAP only corroborates severe-composite relevance; report shorthand is not added as S_C.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** The protocol criteria lack the REPORT's explicit 2 L/min split and differ in moderate-component membership. No ledger value/location transcription was changed.


## C012 — Coma score inclusion threshold

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: The protocol includes GCS 8 in coma, whereas the report definition excludes it under the same sedation and therapeutic-coma exclusions.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol coma threshold versus REPORT results supplement coma threshold

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007

**Qualifying route:** Route A, category 5

**Reported-versus-comparator:** The protocol includes GCS 8 in coma, whereas the report definition excludes it under the same sedation and therapeutic-coma exclusions. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** Coma component membership at GCS 8 and the extrapulmonary definition; coma 2/2 and extrapulmonary 167/150 counts are contextual only.

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced printed conflict or planned-versus-reported element remains registered with the source-grounded alternatives below; it does not require an additional Route B context argument.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: Coma component membership at GCS 8 and the extrapulmonary definition; coma 2/2 and extrapulmonary 167/150 counts are contextual only. No propagation, clinical conclusion change or participant impact is established.


**Exact source locations:** PLAN [protocol p. 32](../joi190055supp1_prod_16092.pdf#page=32) extra-pulmonary coma definition versus REPORT [results p. 21](../joi190055supp4_prod_16092.pdf#page=21) §2.8 coma definition; REPORT [main p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9) coma/extrapulmonary composite counts. Fresh exact-source [protocol glyph detail](review_1_6_2/preprocessing/evidence_recheck/protocol-p32-coma-detail.png) is a visual derivative, with the linked PDF as authority.

**Source evidence:** Locations found: yes. Source matched visually: protocol has < with a separate underline, i.e. ≤8; comparator matched visually: results has strict <8. Both exclude therapeutic coma/sedation. Native direct pdftotext reads protocol <8 because it does not capture the separate underline; this disagreement is explicitly retained. The current 300 dpi crop resolves the decisive glyph; the 160 dpi full-page view alone is insufficient.

**Reasoning procedure:** Route A category 5 applies because score 8 is included by the PLAN component and excluded by the REPORT component under the same exclusions.

**Calculation:** Logical check: at GCS = 8, PLAN 8≤8 is true; REPORT 8<8 is false. GCS is a discrete inclusion score; half-unit rounding intervals are not applicable to its stated inequality. Source counts are coma 2/2 and extrapulmonary composite 167/150, without patient-level scores.

**Necessary inputs available; exact missing inputs or definitions:** Necessary exact glyphs and exclusions are available. Missing: operational case-report definition, score-8 participant count, amendment/clarification record and actual eligibility handling. No numeric change to reported counts is demonstrated.

**Alternative source-grounded interpretations:** An operational definition may have followed either threshold; the separate protocol underline is not an OCR-inferred addition. A definition revision or clarification is possible but not identified in supplied changes.

**Direct observation versus inferred explanation:** Direct observation: source-confirmed opposed inequalities. Inference only: any affected participant, actual implementation or cause.

**Classification rationale:** Prospective PLAN versus publication-results REPORT gives P_R and protocol_report. Native derivative/source mismatch does not change document roles or add a relationship.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** A current 300 dpi source crop confirms the protocol's separately underlined ≤8 glyph, whereas the results page prints <8. No ledger value/location transcription was changed.


## C013 — Per-protocol cardiopulmonary-edema interval/test compatibility

Pending Human Adjudication.

**Candidate statement:** Candidate reporting issue: The per-protocol cardiopulmonary-edema interval excludes ratio null one while its accompanying P = .09 is nonsignificant.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT eTable 8 per-protocol cardiopulmonary-edema interval versus REPORT same-row P value

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-007

**Qualifying route:** Route A, category 1

**Reported-versus-comparator:** The per-protocol cardiopulmonary-edema interval excludes ratio null one while its accompanying P = .09 is nonsignificant. The exact printed tuples, labels and matching comparators are retained in Source evidence and Calculation below.

**Affected result or extracted value:** Per-protocol cardiopulmonary-edema Effect Estimate 1.36 (1.02–1.82), P .09, for 15/917 versus 7/912; S355.

**Why context does not resolve it:** Route A, category 1 is an always-register category. The reproduced printed conflict or planned-versus-reported element remains registered with the source-grounded alternatives below; it does not require an additional Route B context argument.

**Potential downstream evidence impact:** If confirmed through human adjudication, a data extractor could copy competing values, effect definitions, intervals or analysis-provenance fields for this specific result: Per-protocol cardiopulmonary-edema Effect Estimate 1.36 (1.02–1.82), P .09, for 15/917 versus 7/912; S355. No propagation, clinical conclusion change or participant impact is established.

Duplicate checker provenance retained separately: Secondary per-protocol edema portion of F-NUM-003; the screening row's scalar duplicate target remains C009.


**Exact source locations:** REPORT [results p. 29](../joi190055supp4_prod_16092.pdf#page=29) eTable 8 cardiopulmonary edema S355; REPORT [main p. 4](../jama_bluth_2019_oi_190055_16092.pdf#page=4) binary/per-protocol methods supplies context.

**Source evidence:** Locations found: yes. Source matched: 15/917 (1.6%) versus 7/912 (.8%), Effect Estimate 1.36 (95% CI 1.02–1.82), P .09. Comparator matched: same-row P .09 is nonsignificant while the printed interval excludes one. The heading is literally Effect Estimate and is not replaced with RR in this recheck.

**Reasoning procedure:** Route A category 1 applies with ratio null one from the binary-outcome method context. RR versus OR uncertainty does not alter the multiplicative null; a row-specific nonratio interpretation is not supplied. C009's distinct DIC result and C004's point estimand identity remain separate IDs.

**Calculation:** Lower [1.015,1.025], upper [1.815,1.825] and point [1.355,1.365] confirm interval exclusion of one and point containment. P [.085,.095] stays above .05. Category 1 uses no rounding/relative gap exclusion; no raw-data recalculation is necessary to compare these printed inferential decisions.

**Necessary inputs available; exact missing inputs or definitions:** Necessary tuple, confidence level, P and source binary-analysis context are available. Missing: row-specific effect-measure definition, precise interval/test procedures, sparse-cell handling and fitted variance inputs.

**Alternative source-grounded interpretations:** Different interval/test procedures may explain the opposed decisions; a generic effect heading leaves exact ratio definition open. No unreported nonratio scale is assumed, and no analysis mechanism is attributed.

**Direct observation versus inferred explanation:** Direct observation: exact generic label, interval and nonsignificant P. Inference only: model/interval construction and connection to the conditional-allocation pattern.

**Classification rationale:** Conflict is within eTable 8 REPORT, so S_W, statistical_results. Main methods contextualize rather than conflict and add no S_C.  

**Classification ambiguity:** None


**Mechanical evidence recheck:** The exact PP edema 95% interval 1.02–1.82 excludes ratio null one while the same-row P .09 is nonsignificant. No ledger value/location transcription was changed.


# Downstream Evidence-Chain Considerations

A systematic review or meta-analysis may separately extract a point estimate, its measure, confidence limits, significance reading, population and outcome definition. The cards preserve those distinctions rather than replacing one field with a reconstructed value. Effect-measure identity can affect how a result is coded; interval/test conflicts can leave competing inferential readings; changed endpoint windows or unidentified planned outputs can affect description of outcome and analysis provenance.

These are possible extraction consequences if a candidate is later confirmed. The supplied package does not establish that any result propagated into evidence synthesis, altered a guideline, changed a clinical conclusion or affected a participant. No preferred analysis or final correction is proposed.

# Limitations and Missing Definitions

All six supplied sources and all 100 pages were mapped. The limitations below concern unavailable definitions and inputs, rather than source-coverage gaps. The complete durable record is [limitations.md](review_1_6_2/limitations.md).

- Participant-level records, analytic code and operational case-report forms were not supplied. Actual category membership at GCS 8 or particular oxygen flows cannot be determined.
- Row-specific response, conditioning variable, denominators, link, adjustment, marginalization and reference orientation are unidentified for the repeated binary-effect pattern. Its diagnostic resemblance does not establish a production mechanism. Explicit subgroup, component and GEE estimates are not equated with crude ratios.
- Unrounded endpoints, exact sparse-cell/zero-cell procedures, fitted variance or covariance inputs, mortality-specific interval construction and average-GEE transformation/test mapping are unavailable. Source-reproduced interval/test observations remain registered with those alternatives.
- Clinical-severity weights and an identifiable weighted output, test provenance for the primary time-to-event P value, individual-endpoint supersession records and additional clarification/amendment documentation are unavailable. Absence of an identified output is not proof of nonperformance. The SAP documents prospective January 20, 2018 finalization and endorsement before last inclusion, database locking and analysis.
- Full sequential-design software settings and actual interim statistics are unavailable; no stopping-rule conflict is inferred from their absence.
- Historical reusable-PNG rendering engines are unrecorded. Current direct source renders and page extraction records provide documented authority checks; the protocol p.32 detached inequality underline requires visual reading. Unlabeled graphical coordinates support direction and containment checks, not exact additional scalar estimates.

# Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

## Reproducibility and integrity

Routing preflight reports PASS, run model `gpt-6.1-sol` with source DEFAULT, coordinator inference PASS, execution mode INTERACTIVE_CLI and provider CURRENT_SESSION. All ten named role presets were verified against their fixed model/effort pairs. No provider configuration or credentials were written to the package.

Processing ran on CPU. Direct Poppler pdfinfo/pdftotext/pdftoppm 26.01.0 provided information, extraction and current rendering. Tesseract 5.5.0 was available but no OCR was required. Pandoc 3.7.0.2 is available for coordinator rendering. No fallback environment was created: NOT_NEEDED, removal state NOT_CREATED. The [tooling record](review_1_6_2/tooling_record.md) records the probe and engines.

Current source confirmations comprise 17 statistical-pass-1 derivatives, 28 inclusion-screen derivatives and 16 evidence-recheck derivatives. The latter include 13 full-page images, one 300 dpi glyph detail and two complete layout-text files. Each derivative has a CPU/Poppler engine record in its [pass-1](review_1_6_2/preprocessing/statistics_pass_1/engine_manifest.md), [screening](review_1_6_2/preprocessing/inclusion_initial/engine_manifest.md) or [recheck](review_1_6_2/preprocessing/evidence_recheck/engine_manifest.md) manifest. Later stages reused these current confirmations without modification.

The independent auditor checked all six source hashes and all 100 reused-asset hashes against baseline and found them unchanged. Final coordinator controls recompute the [source after-hashes](review_1_6_2/source_hashes_after.sha256) and [reused-asset after-hashes](review_1_6_2/reused_artifact_hashes_after.sha256), compare them byte for byte with baseline, render standalone HTML with embedded CSS and a table of contents, and require [mechanical validation](review_1_6_2/review_validation.json) to report PASS. Those local rendering/validation steps are outside the scientific review timing window.

Canonical scientific records are the [candidate ledger](review_1_6_2/candidate_ledger.md), [mechanical recheck](review_1_6_2/verification/evidence_recheck.md) and [independent quality audit](review_1_6_2/quality/evidence_quality_audit.md). C004 retains the entire 57-row calculation and all 12 modeled component repeats inline; the [independent arithmetic diagnostic](review_1_6_2/statistics/effect_measure_diagnostics.md) remains available as a complete auxiliary record. Every stable ID is present in the ledger, recheck, audit and this report.

## Actual agent execution

All specialists started as fresh, distinct runtime agents. Both statistical passes and the screening, recheck and audit stages use high effort; the other specialist stages use medium. The coordinator uses high. The [execution manifest](review_1_6_2/agent_execution_manifest.md) records every actual agent once.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a1294f-a238-7102-ba12-2a47f70500b4 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12951-4413-7920-9cd3-819456285203 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12953-79b8-7ef2-9d11-54bb3662d6a4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12953-9a0b-7d70-809d-2684b6fa0b34 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a12959-5a05-7980-8b19-ced046b9cf42 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12959-801d-7763-b4b6-80ba61b5f412 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12959-b34f-7793-ae97-9dece6336e61 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a12968-bd54-7e42-add6-25f56ec40245 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a1296f-944f-75b1-9a85-459ba68c6feb | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12976-52fb-70f1-b0b8-5613697ae6a0 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a1297e-2ec3-7fb3-877c-703890291f7c | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12985-28c4-7602-8515-5ff9125ecbcf | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

## Reproducibility performance

The target is a package-specific planning range, not a stopping rule. Timing fields are copied from the coordinator-owned run state; the coordinator captures finish time immediately after complete Markdown assembly and fills the pending performance values before HTML rendering and validation.

- **Target basis:** Six native-text PDFs, 100 unique source pages, all backed by byte-matched native/layout extraction and 73 reusable rendered images including overlapping confirmations; no OCR or Office conversion is initially required. Main and support mapping can run concurrently under the 200,000-character bound, with separate visual batches under 32 pages. Protocol, amendments, SAP, main results and 43-page results supplement require cross-source reconciliation, three parallel checker lanes, independent screening/recheck, a distinct second statistical pass, audit and report waves. A 30-45 minute target reflects low fresh-extraction burden plus substantive plan/report and visual-result mapping; it is not derived from page count alone.
- **Total source units:** 100
- **Fresh-source units:** 0
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-10-11T04:55:46Z
- **Finished UTC:** 2026-10-11T05:55:56Z
- **Observed elapsed minutes:** 60.17
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Complete 211-record statistical reviews and 57-row effect-measure reconstruction; independent rereading of 22 findings; full 13-ID source recheck including high-resolution threshold confirmation; mandatory sequential fresh-agent screening, recheck, second statistical pass, audit and report waves
