# Quantitative Quality-Control Consistency Review — EPOCH Randomized Clinical Trial

**Pending Human Adjudication**

Workflow 1.6.1 reviews quantitative reporting in the supplied package. Classification and evidence fields prepare human review; they do not adjudicate the candidate or the study. All human adjudication fields remain unfilled.

## Executive Quality-Control Summary

Complete review of four supplied PDFs, comprising **69 of 69 physical pages**, identified **one stable candidate reporting issue (C001)**. Two independently screened checker findings were consolidated into that single issue. C001 concerns the planned versus reported eligibility definition of the key secondary significant clinical deterioration event (SCDE) composite: both the circulatory conjunction and the death location/window differ. It belongs to `protocol_report`, has relationship type `P_R`, evidence state `reproduced`, and inclusion audit `CONFIRMED`.

The affected report gives 127 versus 259 SCDEs, rates 0.50 versus 0.84 per 1000 patient-days, and adjusted rate ratio 0.77 (95% CI 0.61–0.97), P=.03. Matched report counts and estimates reconcile. The candidate concerns the endpoint definition attached to those quantities. Supplied aggregates cannot establish a changed event count, estimate, or paper conclusion.

The review covered 110 numeric relationship groups and 84 statistical relationships. Both fresh statistical passes covered all 84 relationships. Independent source recheck and quality audit retained C001 for human adjudication; neither stage added another issue.

## Package and Reused-Evidence Provenance

The paper is *Effect of a Pediatric Early Warning System on All-Cause Mortality in Hospitalized Pediatric Patients: The EPOCH Randomized Clinical Trial*, supplied as `jama_parshuram_2018_oi_180015.pdf`. The package also supplies a research protocol, statistical analysis plan (SAP), and non-plan results supplement. Roles were assigned by content.

| Source ID | Actual supplied filename | Role | Stable units | Content basis |
|---|---|---|---:|---|
| DOC-001 | jama_parshuram_2018_oi_180015.pdf | REPORT | 11 PDF pages | Published main article, journal pp.1002–1012. |
| DOC-002 | joi180015supp1_prod.pdf | PLAN | 37 PDF pages | Protocol 005, version dated 23 February 2011, including operational tables and appendices. |
| DOC-003 | joi180015supp2_prod.pdf | PLAN | 7 PDF pages | SAP, including analysis models, illustrative code, sensitivities and aggregation rules; no visible date/version. |
| DOC-004 | joi180015supp3_prod.pdf | REPORT | 14 PDF pages | Results supplement with two eFigures and five eTables. |

The fresh asset curator inspected and hashed **66 existing preprocessing assets**. Usable native/layout text covers every source page; 53 existing rendered pages are readable, of which 52 were byte-matched to current direct rendering. DOC-004 p.1 has visually matching content despite a rendering hash difference and is classified PARTIAL as an image asset; its source-matched text covers the unit. A historical structural page-status manifest is STALE and was excluded as current scientific mapping authority. Its historical coverage claims did not determine this review's scope.

Reusable assets were locators and transcription aids. Fresh scientific mapping reconstructed the complete supplied-source scope, without reading prior candidate, checker, screening, classification, adjudication, audit, or report outputs as scientific inputs. Source PDFs remained authoritative. Asset fitness, coverage and extraction engines are recorded in [Evidence Asset Inventory](review_1_6_1/evidence_asset_inventory.md), and source identity and hashes in [Source Inventory](review_1_6_1/source_inventory.md) and [Source Hashes Before](review_1_6_1/source_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

Scope followed the four focus areas in QUALITY_CONTROL_SCOPE.md: counts and denominators; estimate and test logic; statistical method logic; and planned versus reported statistical design. Primary and key secondary results, analysis populations, endpoint definitions and planned decision rules were compared across matched locations and content roles. Cover, administrative and reference pages were inspected and explicitly mapped even when they contained no applicable trial relationship.

| Source ID | Total units | Reusable units | Fresh-required extraction units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | 37 | 37 | 0 | 37 | COMPLETE |
| DOC-003 | 7 | 7 | 0 | 7 | COMPLETE |
| DOC-004 | 14 | 14 | 0 | 14 | COMPLETE |
| **Total** | **69** | **69** | **0** | **69** | **COMPLETE** |

Fresh-required extraction counts describe derivative availability, not the freshness of scientific review. Every reusable-backed page was scientifically mapped in this run. Main and support mapping scopes are disjoint: 11 main pages and 58 support pages. [Source Coverage](review_1_6_1/source_coverage.md) and [Coverage Manifest](review_1_6_1/coverage_manifest.md) document the assignments and completion.

The review excluded display precision, field-resolvable notation or wording, model-versus-crude comparisons, unsupported conditional observations, peripheral comparisons and matters outside the four focus areas. It did not conduct a broad clinical, design, novelty, misconduct, or raw-data audit and did not propose a preferred analysis. Only supplied package evidence was used; no external literature or web evidence was consulted.

## Quantitative and Statistical Relationship Coverage

| Evidence scope | Registered coverage | Completed work |
|---|---:|---|
| Main numeric groups | 65 | N001–N065, including all component tuples and matched occurrences. |
| Support numeric groups | 45 | N101–N145, including full hospital tables, distributions, definitions and plan inputs. |
| All numeric groups | 110/110 | Counts, denominators, totals, precision intervals and effect-measure identity reviewed. |
| Statistical pass 1 | 84/84 | All S001–S084 carry PASS_1_COMPLETE; fresh gpt-6.1-sol/high agent. |
| Statistical pass 2 | 84/84 | All S001–S084 carry PASS_2_COMPLETE; a different fresh gpt-6.1-sol/high agent, after ledger, screening and recheck. |

The complete maps retain all 21 hospital rows in each hospital table, all 19 ICU distribution rows, all 15 eTable 4 estimate/interval/P triples, all eight Table 2 inferential rows, and all 13 Table 3 outcome rows. Numeric groups track inseparable component tuples rather than imposing a count on individual values. Inferential coverage includes containment, interval order, direction, null/decision compatibility, models and links, denominator/time/population matching, multiplicity, sample-size inputs, missingness and planned-versus-reported specifications.

Exact test construction and covariance are not supplied, so CI-to-P diagnostics were not treated as definitive identities. Adjusted estimates were not required to equal crude arithmetic. Disclosed separate baseline specifications resolve the SCDE ratio-versus-difference interval contrast. S049 and S050 track C001's two eligibility components; S003 and S080 track the affected result and interpretation in both passes.

Durable records: [Main Quantitative Evidence](review_1_6_1/extraction/main_quantitative_evidence.md), [Support Quantitative Evidence](review_1_6_1/extraction/support_quantitative_evidence.md), [Numeric Relationship Inventory](review_1_6_1/relationships/numeric_relationship_inventory.md), [Statistical Relationship Inventory](review_1_6_1/statistics/relationship_inventory.md), [Statistical Pass 1](review_1_6_1/checkers/statistical_pass_1.md), and [Statistical Pass 2](review_1_6_1/checkers/statistical_pass_2.md).

## Inclusion Screening Summary

A finding qualified only if reproduced from the supplied source, within focus, unresolved at once by a statistically literate reader from immediate context, and capable of affecting interpretation or extraction of a named result. A fresh independent screener reread every checker finding and consolidated the common endpoint-definition issue without a candidate-count target.

| Screening measure | Count |
|---|---:|
| Finding rows screened | 2 |
| INCLUDE / MEETS_THRESHOLD | 2 |
| SCREENED_OUT finding rows | 0 |
| Consolidated stable candidates | 1 |

| Finding ID | Source checker | Stage | Decision | Reason code | Stable ID |
|---|---|---|---|---|---|
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C001 |

Both findings meet the endpoint-definition threshold and concern the same SCDE result. F-XS-001 supplies the circulatory comparison; F-ST1-001 also supplies the death location/window comparison. They remain two INCLUDE rows linked to one candidate. Numeric review, statistical pass 2 and quality audit emitted no additional finding, so no pass-2 screening stage was required.

| SCREENED_OUT reason code | Finding-row count |
|---|---:|
| NOT_REPRODUCED | 0 |
| ROUNDING_OR_DISPLAY_PRECISION | 0 |
| NOTATION_OR_TYPOGRAPHY | 0 |
| TERMINOLOGY_OR_WORDING | 0 |
| MODEL_VERSUS_CRUDE | 0 |
| CONTEXT_RESOLVES | 0 |
| CONDITIONAL_OR_UNREPORTED | 0 |
| PERIPHERAL_COMPARISON | 0 |
| OUT_OF_FOCUS | 0 |
| DUPLICATE_OF_INCLUDED | 0 |
| **Total SCREENED_OUT** | **0** |

Checker self-screening is a separate record: numeric review lists 15 excluded-observation rows, cross-source review 21, statistical pass 1 20, and statistical pass 2 26. The auditor examined all **82 lane-specific rows**, including patterns revisited by different lanes. These are not 82 unique issues or findings and do not add rows to the independent screening table. The threshold-boundary wording observation is excluded from C001. Counts above reconcile to [Inclusion Screen](review_1_6_1/screening/inclusion_screen.md); the audit found no screening decision requiring amendment.

## Review-Domain Summary

The four domains describe what is compared and prepare human review. `statistical_results` covers counts, estimates, tests and methods in REPORT materials. `report_internal_inconsistency` covers unresolved result attribution across REPORT locations. `protocol_report` covers planned-versus-reported statistical design or analysis. `plan_material` covers inconsistencies confined to PLAN specifications relied on by the report.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 0 |
| report_internal_inconsistency | 0 |
| protocol_report | 1 |
| plan_material | 0 |
| **Total** | **1** |

| Primary relationship type | Meaning | Stable candidates |
|---|---|---:|
| P_R | PLAN versus REPORT | 1 |
| P_P | Within PLAN material | 0 |
| S_C | Between REPORT documents | 0 |
| S_W | Within one REPORT document | 0 |
| **Total** | | **1** |

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 1 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **1** |

Inclusion audits: CONFIRMED 1; QUESTIONED 0. CONFIRMED records the independent threshold audit and leaves human adjudication pending. C001 has only P_R in All relationships: agreement between the two REPORT sources corroborates one side rather than creating S_C. Counts and classification agree with [Candidate Ledger](review_1_6_1/candidate_ledger.md), [Evidence Recheck](review_1_6_1/verification/evidence_recheck.md), and [Evidence Quality Audit](review_1_6_1/quality/evidence_quality_audit.md).

## Candidate Index

| Stable ID | Candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#C001) | Planned and reported SCDE eligibility components differ | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

<a id="C001"></a>

## C001 — Planned and reported eligibility components of the key secondary deterioration composite differ

Pending Human Adjudication.

**Candidate statement:** The supplied protocol requires both qualifying fluid and vasoactive therapy for the circulatory component and restricts the death component to ward death; the report permits either circulatory therapy and also includes death within one hour after urgent ICU admission. The package does not reconcile these eligibility definitions for the reported significant clinical deterioration event (SCDE) composite.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol pp.10,11,24 vs REPORT main article p.4 and REPORT results supplement p.6
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-001, F-ST1-001
**Classification rationale:** Prospective protocol definitions conflict with reported outcome definitions. Both REPORT documents agree on the retained components; corroboration does not create S_C. The SAP supplies count-model context without a conflicting endpoint predicate. P_R is the sole relationship and maps to protocol_report.
**Classification ambiguity:** A dated endpoint amendment or operational classification document might reconcile these definitions, but none is supplied.

**Exact source locations:**

- PLAN [protocol p.10, main secondary outcome](../joi180015supp1_prod.pdf#page=10): ward death without DNR and reference to operational Table 5.
- PLAN [protocol p.11, deterioration scale context](../joi180015supp1_prod.pdf#page=11): early-ICU resuscitation components and death before transfer.
- PLAN [protocol p.24, Table 5 categories 4–7](../joi180015supp1_prod.pdf#page=24): circulatory conjunction, category eligibility, ward death with no transfer, separate early-ICU CPR/ECMO category.
- REPORT [main article p.4, Study Outcomes](../jama_parshuram_2018_oi_180015.pdf#page=4): one-or-more composite, vasoactive therapy or fluid boluses, first-hour ICU death.
- REPORT [results supplement p.6, eTable 1 components b and d](../joi180015supp3_prod.pdf#page=6): fluid and/or vasoactive therapy; ward or first-hour ICU death; intent-to-resuscitate pronouncement without CPR.
- Matching affected REPORT result locations: [abstract p.1](../jama_parshuram_2018_oi_180015.pdf#page=1), [secondary-result narrative p.6](../jama_parshuram_2018_oi_180015.pdf#page=6), [Table 3 p.7](../jama_parshuram_2018_oi_180015.pdf#page=7), [discussion p.9](../jama_parshuram_2018_oi_180015.pdf#page=9), and [results supplement p.11, eTable 3](../joi180015supp3_prod.pdf#page=11).

**Source evidence:** Protocol Table 5 circulatory category requires >60 mL/kg intravenous/intraosseous fluid in the preceding 12 hours and an inotrope/vasopressor at transfer or in that window. Category 7 defines no-DNR ward death with no transfer. Report eTable 1 uses and/or for therapies and includes ward or first-hour urgent-ICU death; it permits pronouncement without CPR when there was intent to resuscitate. The main definition agrees on either therapy and first-hour ICU death. Exact fluid-threshold boundary wording is outside this candidate.

Protocol p.11 separately lists first-hour intubation, CPR and mechanical circulatory support while describing death before transfer; protocol p.24 category 6 permits first-hour chest compressions or ECMO. These provisions do not explicitly expand category 7's death location. Intent to perform CPR with pronouncement without CPR appears in both the planned and reported death wording and is not itself a changed condition. It also prevents assuming that every qualifying first-hour ICU death necessarily received the chest compressions required by category 6.

**Reported-versus-comparator:** REPORT circulatory F OR V versus PLAN F AND V; REPORT death W OR I versus PLAN W, where W is qualifying ward death and I qualifying first-hour urgent-ICU death. The reported key secondary result is 127 versus 259 events (386 total), at 0.50 versus 0.84 per 1000 patient-days, rate ratio 0.77 (95% CI 0.61–0.97), P=.03. The absolute difference −0.34 (95% CI −0.73 to 0.05) uses the disclosed baseline-omitting model and is not another inconsistency.

**Reasoning procedure:** Read exact operational eligibility predicates, hold the population/window and non-boundary fluid threshold fixed, compare truth conditions, and separately identify what the aggregate data can establish. Circulatory and death-location changes are retained components of one named endpoint-definition issue shared by both checker findings. No numerical effect change is inferred.

**Calculation:** F AND V differs from F OR V for (F,V)=(true,false) or (false,true). The added component subsets are (F minus V) union (V minus F), apart from patients already qualifying through another component. W differs from W OR I outside W. Rounding does not alter conjunctions or death locations. Rates reproduce: 127/251859×1000=0.50425; 259/307584×1000=0.84205; 127+259=386. Individual component overlap and revised counts cannot be calculated from the supplied aggregates.

| Qualifying fluid F | Qualifying vasoactive therapy V | PLAN: F AND V | REPORT: F OR V |
|---|---|---|---|
| false | false | false | false |
| true | false | false | true |
| false | true | false | true |
| true | true | true | true |

The logical comparison holds the eligible population and treatment windows fixed and holds fluid status away from the disputed boundary wording. The possible additional death subset is I outside W and outside any other qualifying component; its observed size is not supplied. Supporting rates lie inside their half-unit display intervals: 0.50 corresponds to [0.495,0.505), and 0.84 to [0.835,0.845). The counts and denominators therefore reconcile. The adjusted rate ratio is not required to equal a crude ratio, and the disclosed ratio and absolute-difference models do not share a required test statistic.

**Affected result or extracted value:** The prespecified key secondary SCDE eligibility definition attached to 386 events and the reported adjusted rate ratio 0.77 (0.61–0.97), P=.03. An extractor could record the protocol intersection/ward-only definition or the reported union/expanded-death definition with the same estimate.

**Why context does not resolve it:** The prospective operational table explicitly supplies narrower predicates; the report explicitly supplies broader ones. Neither the SAP nor immediate reported context identifies an amendment or a component-level mapping between them. Separate CPR/ECMO eligibility does not guarantee every early ICU death overlapped another component. The observed event totals alone cannot establish which rule was used throughout classification.

**Alternative source-grounded interpretations:** A prospective amendment may have reconciled the definitions; the report may state the consistently implemented operational rule; or overlapping components may have left observed counts unchanged. The package cannot select among these alternatives. No preferred definition or revised estimate is proposed.

**Mechanical evidence recheck:** The fresh rechecker found all ten cited pages, confirmed every predicate and matching result value, reproduced the logical comparison and precision check, and confirmed PLAN versus REPORT roles, P_R and protocol_report. Evidence state reproduced. Component overlaps, operational classification records and a dated amendment remain unavailable; no numerical consequence is established. Complete facts are in [Evidence Recheck](review_1_6_1/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed by human review, endpoint harmonization or prespecification extraction could differ depending on the component definition attached to the SCDE estimate. No propagation, numerical effect change or changed paper conclusion is established.

**Human verification steps:** Inspect the source pages, operational case-report/adjudication definition and any dated amendment. Identify which circulatory conjunction and death location/window classified the 127 versus 259 events; determine whether component overlaps reconcile the supplied definitions.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Evidence extraction links a numeric result to its population, endpoint definition, time window, denominator and model. A confirmed endpoint-definition discrepancy could affect how a systematic reviewer harmonizes SCDE with composites from other trials or records prespecification, even when copied counts and estimates agree. The appropriate human question is which definition belongs with the supplied estimate and whether documentation reconciles the plan and report. No downstream propagation, numerical consequence, or changed study conclusion is established by this package.

## Limitations and Missing Definitions

All 69 source pages and all registered numeric/statistical groups were covered; no scientific-coverage or cited-source access gap remains. The scope is supplied reporting and plan material, without individual data or operational analysis output.

For C001, individual fluid/vasoactive indicators, overlap with other composite components, first-hour ICU death counts and overlaps, event-classification records, and a dated endpoint amendment/version history are unavailable. These inputs would be needed to establish implementation or any revised event count, rate or model estimate. Hospital aggregates, 59 cardiac arrests and 8 deaths before ICU transfer do not replace them. The supplied SAP lacks a visible date/version and supplies model context without a competing SCDE eligibility predicate.

Other mechanical limits include exact GEE covariance/test and interval construction, exact cluster-power equations and baseline covariance, complete Holm family membership/order, operational code/output, individual prediction values, precise histogram percentages and some post-period ICU-discharge denominators. Diagnostic assumptions cannot fill these inputs; their absence alone did not qualify as a candidate.

Sixteen historical rendered images are absent: DOC-001 pp.10–11 and DOC-002 pp.1–6,18,31–37. Readable source-matched native/layout text covered every affected page. DOC-004 p.1's readable image is PARTIAL by rendering hash; text covers it. Historical extraction/rendering versions are partly undocumented and were checked against current direct-source tools. CPU OCR and Office conversion are unavailable, but no OCR or Office conversion was needed for these four PDFs. No fallback environment was created. Detailed limits are in [Limitations](review_1_6_1/limitations.md).

## Human Adjudication Checklist

1. Inspect every linked definition and matching result page in C001, distinguishing PLAN specifications from REPORT definitions.
2. Identify the circulatory predicate and death location/window used to classify the 127 versus 259 SCDEs.
3. Examine any dated amendment, operational definition or event-classification documentation that reconciles the supplied predicates.
4. If numerical equivalence is proposed, establish the relevant component overlaps rather than inferring them from aggregate counts.
5. Record the human decision and rationale in the five blank card fields. Keep the endpoint-definition question separate from claims about estimates or conclusions that require additional evidence.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

This is a local CPU-only Workflow 1.6.1 review. [Routing Preflight](review_1_6_1/routing_preflight.md) records PASS, coordinator inference PASS, INTERACTIVE_CLI, Provider CURRENT_SESSION and verification of all ten named presets. Every mandatory specialist stage used a distinct fresh runtime agent with the fixed model/effort contract. Both statistical agents used gpt-6.1-sol/high and were distinct from the mappers, screen, recheck and audit agents. No provider credentials or provider configuration were written.

Direct tools: Poppler pdfinfo/pdftotext/pdftoppm/pdftocairo 25.03.0; Pandoc 3.1.11.1 renders the standalone HTML through the supplied local renderer. Direct native/layout reads and source-matched images confirmed all ten C001 source pages. No new OCR, Office conversion, GPU use, fallback capability or temporary fallback environment was needed. [Tooling Record](review_1_6_1/tooling_record.md) records the full probe and environment state.

Final hash recomputation after Markdown assembly matched all 4 direct sources and all 66 inventoried assets to their before-review hashes. Sources and reused assets were preserved. Hash records: [Direct Sources Before](review_1_6_1/source_hashes_before.sha256), [Direct Sources After](review_1_6_1/source_hashes_after.sha256), [Reused Assets Before](review_1_6_1/reused_artifact_hashes_before.sha256), and [Reused Assets After](review_1_6_1/reused_artifact_hashes_after.sha256). Local rendering and mechanical validation use the supplied scripts after timing finalization; the completion result is recorded in [Review Validation](review_1_6_1/review_validation.json).

### Agent execution

The following table copies [Agent Execution Manifest](review_1_6_1/agent_execution_manifest.md). Specialist IDs are the canonical runtime task identifiers exposed by the interactive tool; no specialist UUID was exposed. Primary artifact paths are relative to review_1_6_1.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a128db-ac31-7600-90f5-a3c9f0724f87 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

Timing fields below match the finalized run_state.md. Finish timing includes complete Markdown assembly and coordinator editorial checks. Local HTML rendering and mechanical validation are excluded from review duration.

- **Target basis:** Four PDF-only sources contain 69 physical pages, all with reusable readable native/layout text and 53 readable rendered pages (52 byte-matched to current source rendering); 0 units need fresh extraction. Source-matched visual tables and figures still require full scientific mapping, a 37-page protocol and 7-page analysis plan require planned-versus-reported comparisons, and the fixed workflow requires parallel mapper/checker waves followed by independent screening, recheck, a second statistical pass, audit and report generation. No Office conversion or OCR is currently necessary. The bounded 25-40 minute range reflects these combined evidence and agent-wave burdens, not page count alone.
- **Total source units:** 69
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T02:52:44Z
- **Finished UTC:** 2026-10-11T03:26:58Z
- **Observed elapsed minutes:** 34.23
- **Target status:** MET_TARGET
- **Exceedance causes:** None
