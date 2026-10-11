# Quantitative Quality-Control Consistency Review — JAMA 2019.4755

**Pending Human Adjudication**

Workflow 1.6.2 reviews quantitative reporting consistency in the supplied paper package. Every candidate remains Pending Human Adjudication. Classification, evidence reproduction and inclusion audit describe the review record; they do not adjudicate the scientific issue.

# Executive Quality-Control Summary

Complete review of five supplied PDFs, comprising 88 physical pages, identified **one stable candidate, C001**. The candidate concerns the primary outcome hierarchy: broad protocol clauses designate specificity, ROC AUC and both assays' sensitivity as primary, while narrower protocol clauses, the SAP and the article retain quantitative FOBGold sensitivity as primary and assign the other diagnostic metrics secondary/exploratory or unreported status. Independent screening retained the issue under Route A, category 5. Direct-source recheck reproduced it, and the independent inclusion audit recorded CONFIRMED.

The numeric checker emitted no findings. Both statistical passes covered all 105 statistical relationship groups; the registered issue is a categorical outcome-status comparison. The 90 displayed difference intervals and 87 visibly printed point differences reproduce under the supplied interval method and display precision. No numerical replacement or change in the article's conclusion is asserted. Three checker findings received screening decisions: one INCLUDE and two SCREENED_OUT, yielding one distinct candidate.

# Package and Reused-Evidence Provenance

The package reports a randomized, double-blind trial of a single 300-mg aspirin dose versus placebo and fecal immunochemical test performance for advanced colorectal neoplasms. Document roles were assigned by content. Prospective protocol/SAP content is PLAN even when supplied as a supplement; completed results and the availability statement are REPORT.

| Source ID | Actual supplied file | Content role and basis | Physical PDF pages |
|---|---|---|---:|
| DOC-001 | [jama_brenner_2019_oi_190039.pdf](../jama_brenner_2019_oi_190039.pdf#page=1) | REPORT — completed randomized-trial article | 7 |
| DOC-002 | [joi190039supp1_prod.pdf](../joi190039supp1_prod.pdf#page=1) | PLAN — protocol version 1.5, 24 July 2015, including prospective operational appendices | 62 |
| DOC-003 | [joi190039supp2_prod.pdf](../joi190039supp2_prod.pdf#page=1) | PLAN — statistical analysis plan and disclosed changes | 10 |
| DOC-004 | [joi190039supp3_prod.pdf](../joi190039supp3_prod.pdf#page=1) | REPORT — non-plan eligibility/results supplement, eTables 1–6 | 8 |
| DOC-005 | [joi190039supp4_prod.pdf](../joi190039supp4_prod.pdf#page=1) | REPORT — protocol, code and dataset availability statement | 1 |
| Total | Five supplied PDFs | Two PLAN and three REPORT sources | 88 |

The [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md) identifies 108 preserved, SHA-256-hashed reusable extraction, OCR, page-image, coordinate-layout and source-location assets. These overlap in their page coverage and therefore are not counted as 108 source units. Eligible assets cover 86 unique pages. Discovery was rebuilt from supplied-source evidence and current maps; earlier candidate sets, screening decisions, classifications and final reports were not scientific inputs.

Source-matched normalized native/layout extraction supersedes earlier character-corrupted main text. Historical OCR and partial locators serve as transcription aids. Exact supplied PDF pages remain authoritative. Current CPU rendering and native/layout extraction used Poppler 26.01.0; historical OCR identifies RapidOCR/ONNX Runtime CPU, while some historical extraction/rendering version numbers are unavailable. New derivatives are inventoried separately and do not alter the preserved reusable hash set.

# Scope, Complete Coverage, and Exclusions

The review covers counts and denominators; estimate, interval and test logic; statistical method logic; and planned versus reported statistical design. Every supplied page was mapped, including covers, references, appendices, signed approval and financial pages. Units without applicable current-trial quantitative relationships were explicitly accounted for.

| Source | Total units | Reusable units | Fresh-required units | Mapped units | Coverage |
|---|---:|---:|---:|---:|---|
| DOC-001 | 7 | 7 | 0 | 7 | COMPLETE |
| DOC-002 | 62 | 60 | 2 | 62 | COMPLETE |
| DOC-003 | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-004 | 8 | 8 | 0 | 8 | COMPLETE |
| DOC-005 | 1 | 1 | 0 | 1 | COMPLETE |
| Total | 88 | 86 | 2 | 88 | COMPLETE |

Protocol physical pages 20 and 49 lacked usable reusable extraction. Fresh CPU rendering and direct visual inspection mapped the complete flowchart on page 20 and the image-only signed approval on page 49. The inserted signed page affects subsequent physical versus printed numbering; all evidence anchors use physical PDF pages. These derivative gaps are closed and leave no scientific coverage gap. See [source coverage](review_1_6_2/source_coverage.md) and the [complete assignment manifest](review_1_6_2/coverage_manifest.md).

The review does not assess broad methodology, clinical merit, novelty, misconduct or raw data, and does not propose a preferred analysis. Historical observational results, administrative budgets and bibliography numerals were distinguished from current trial results. Peripheral comparisons, readily resolved wording/notation, disclosed amendments, missing ordinary secondary outputs without a conflicting result, model-versus-crude comparisons and display-precision differences were screened under the normative scope. No external literature or web evidence was used. There is no candidate-count target.

# Quantitative and Statistical Relationship Coverage

The [main map](review_1_6_2/extraction/main_quantitative_evidence.md) covers all seven article pages. Two disjoint support shards cover the 62-page protocol and the remaining 19 pages; their lossless [canonical support map](review_1_6_2/extraction/support_quantitative_evidence.md) preserves the complete union.

| Relationship class | Main article | Protocol | SAP/other support | Total | Completion |
|---|---:|---:|---:|---:|---|
| Numeric groups | 43 | 7 | 6 | 56 | Every group NUMERIC_COMPLETE |
| Statistical groups | 49 | 34 | 22 | 105 | Every group PASS_1_COMPLETE and PASS_2_COMPLETE |

Groups retain every relevant displayed cell, rather than sampling rows. Numeric checks cover participant flow, all baseline count/percentage rows, diagnostic confusion matrices, sex-component totals, valid-test denominators, predictive-value conditioning, twenty eTable 2 sample-frequency rows and forty Any-column sums. Sample counts, deduplicated participants, disease-positive denominators and full analyzed cohorts remain distinct. In particular, primary quantitative sensitivity uses disease denominators 112/102, rather than the full-cohort advanced-neoplasm counts 115/109.

Fresh statistical agents `root/statistics_one` and `root/statistics_two`, each gpt-6.1-sol/high, independently covered every S relationship. Pass 2 additionally integrated all screening and recheck facts and reconsidered all 23 initial checker exclusions against both qualifying routes and display precision. It emitted no new findings. The quality auditor reviewed all 24 excluded-observation rows, including the pass-2 reconsideration.

The [arithmetic record](review_1_6_2/statistics/stat1_calculation_record.md) preserves every one of the 90 displayed aspirin-minus-placebo difference intervals and 87 visible point differences. All intervals reproduce the stated Agresti–Caffo construction; all visible points reproduce observed proportions. Their displayed half-unit intervals contain the recomputations, with zero residual discrepancy. Raw point differences need not coincide with the adjusted interval centers. The independent auditor recomputed all ninety rows and confirmed their endpoints and visible points.

All six printed main P-value/95% CI pairs agree in significance at two-sided .05. Both primary sensitivity intervals include zero, agreeing with the article's nonsignificance statement. Site-effect results, sex interactions, power/precision inputs, population amendments, missingness rules, endpoint definitions, intervention dose/timing, multiplicity and stopping statements were reviewed wherever applicable. Exact unprinted algorithms were not inferred. Diagnostic power/interaction approximations remain labeled as diagnostics in the statistical artifacts. Detailed traceability is retained in the [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6_2/statistics/relationship_inventory.md), [pass 1](review_1_6_2/checkers/statistical_pass_1.md) and [pass 2](review_1_6_2/checkers/statistical_pass_2.md).

# Inclusion Screening Summary

A finding qualifies only when reproduced and covered by an always-register Route A category, or by all Route B criteria: in focus, unresolved by immediate context and relevant to interpretation or extraction of a named result. Printed-number comparisons propagate half-unit display intervals; residual relative discrepancy at most 0.05 is display precision. Interval-versus-P/test conflicts are independently considered under Route A category 1.

The [single screening log](review_1_6_2/screening/inclusion_screen.md) contains exactly one decision for each of the three emitted findings. The independent [quality audit](review_1_6_2/quality/evidence_quality_audit.md) confirmed every decision in both directions and requested no screening changes.

| Decision | Reason code | Findings | Candidate mapping |
|---|---|---:|---|
| INCLUDE | MEETS_THRESHOLD | 1 | F-XS-001 → C001 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 1 | F-ST1-001 → existing C001; provenance and all locations retained |
| SCREENED_OUT | CONTEXT_RESOLVES | 1 | F-ST1-002; no candidate ID |
| Total | All screened findings | 3 | One distinct stable candidate |

| Checker | Emitted findings | INCLUDE rows | SCREENED_OUT rows |
|---|---:|---:|---:|
| Numeric | 0 | 0 | 0 |
| Cross-source | 1 | 1 | 0 |
| Statistical pass 1 | 2 | 0 | 2 |
| Statistical pass 2 | 0 | 0 | 0 |
| Total | 3 | 1 | 2 |

The duplicate statistical finding observes the same outcome-hierarchy pattern as the included cross-source finding. The other emitted finding concerns postponed collection versus the original day-specific primary restriction. Immediate analysis-window context and the SAP's explicit later intention-to-screen amendment resolve its bearing on the reported population; no conflicting printed denominator is established. Pass 2 and the audit independently reconsidered that decision.

Checker excluded-observation rows are a separate trace, not additional emitted findings or screening decisions. Their totals reconcile to the quality audit:

| Excluded-observation reason | Rows |
|---|---:|
| ROUNDING_OR_DISPLAY_PRECISION | 3 |
| CONTEXT_RESOLVES | 8 |
| NOT_REPRODUCED | 5 |
| TERMINOLOGY_OR_WORDING | 2 |
| CONDITIONAL_OR_UNREPORTED | 6 |
| Total | 24 |

There are four numeric, nine cross-source, ten pass-1 and one pass-2 excluded-observation rows. All other screened-out reason codes have zero rows in these retained exclusion tables. The twenty-four rows include repeated observations across independent stages and are not twenty-four distinct issues.

# Review-Domain Summary

Each candidate has one review domain. `statistical_results` concerns counts, estimates, intervals, tests and methods in REPORT material. `report_internal_inconsistency` concerns conflicting attribution of a report result to an outcome, population, time or comparison. `protocol_report` concerns REPORT-versus-PLAN statistical design or analysis. `plan_material` concerns a statistical design inconsistency confined to PLAN material that the reported analysis relies on.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 0 |
| report_internal_inconsistency | 0 |
| protocol_report | 1 |
| plan_material | 0 |
| Total | 1 |

| Primary relationship type | Meaning | Stable candidates |
|---|---|---:|
| P_R | REPORT versus PLAN | 1 |
| P_P | PLAN versus PLAN | 0 |
| S_C | Between different REPORT documents | 0 |
| S_W | Within one REPORT document | 0 |
| Total | One primary type per candidate | 1 |

C001 additionally involves P_P. That additional relationship describes the same issue and is not a second candidate. Primary-type precedence is P_R > P_P > S_C > S_W; therefore C001 is protocol_report/P_R with All relationships P_R, P_P. Prospective content, rather than supplement filenames, determines the PLAN roles.

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 1 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 1 |

Inclusion audits total one CONFIRMED and zero QUESTIONED. Every stable candidate remains Pending Human Adjudication.

# Candidate Index

| ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#C001) | Primary outcome hierarchy differs across supplied plan clauses and the report | protocol_report | P_R | reproduced | CONFIRMED |

# Candidate Evidence Cards

## C001 — Primary outcome hierarchy differs across supplied plan clauses and the report {#C001}

Pending Human Adjudication.

**Candidate statement:** Broad primary-endpoint descriptions in protocol §§3.9 and 7.2 include specificity and ROC AUC, with §7.2 referring to both immunochemical assays, whereas other protocol sections, the SAP and the report identify quantitative FOBGold sensitivity as primary and the other metrics as secondary. The report explicitly does not present AUC results. The supplied hierarchy statements do not reconcile.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol and DOC-003 SAP vs REPORT DOC-001 main article; PLAN vs PLAN

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Checker provenance:** Cross-source F-XS-001 is included; statistical F-ST1-001 independently reproduces the same issue and is screened out as DUPLICATE_OF_INCLUDED, linked to C001. All locations from both findings are retained.

**Qualifying route:** Route A, category 5

**Classification rationale:** The broad protocol primary list conflicts directly with the report's secondary/unreported status, establishing P_R; mutually conflicting protocol clauses and SAP content also establish P_P. P_R takes precedence. The plan is a conflicting comparator, rather than merely corroborating an internal report observation.

**Classification ambiguity:** The detailed endpoint sections and SAP may have governed the narrow hierarchy; the broad clauses may reflect a retained specification. The supplied package does not state a hierarchy amendment or governing-clause precedence. This does not establish which list governed.

**Exact source locations:**

- PLAN [DOC-002 protocol PDF p11 §3.4](../joi190039supp1_prod.pdf#page=11) and [p22 §6.1](../joi190039supp1_prod.pdf#page=22): narrow primary and secondary lists.
- PLAN [DOC-002 PDF p13 §3.9](../joi190039supp1_prod.pdf#page=13), continuing [p14](../joi190039supp1_prod.pdf#page=14): broader parenthetical primary endpoint.
- PLAN [DOC-002 PDF p28 §§7.1–7.2](../joi190039supp1_prod.pdf#page=28): narrow primary sensitivity and confirmatory status in §7.1; broad both-assay primary wording in §7.2.
- PLAN [DOC-003 SAP PDF p6 §3.2](../joi190039supp2_prod.pdf#page=6) and [p8 §5.4 continuation and §5.5](../joi190039supp2_prod.pdf#page=8): quantitative sensitivity primary, other diagnostic metrics secondary.
- PLAN [DOC-003 PDF p9 §7](../joi190039supp2_prod.pdf#page=9): disclosed population/missingness changes; no explicit hierarchy amendment.
- REPORT [DOC-001 PDF p1 Main Outcome and Measures](../jama_brenner_2019_oi_190039.pdf#page=1) and [p3 Outcomes/Statistical Analyses](../jama_brenner_2019_oi_190039.pdf#page=3): narrow primary hierarchy; secondary analyses exploratory; AUC explicitly unreported.
- REPORT [DOC-001 PDF p4 Primary/Secondary End Points](../jama_brenner_2019_oi_190039.pdf#page=4): numerical secondary specificity and qualitative-sensitivity results.

**Source evidence:** Protocol §§3.4/6.1 designate FOBGold sensitivity primary and specificity/AUC secondary. The §3.9 primary parenthesis adds specificity and AUC of FOBGold; §7.2 adds sensitivity, specificity and ROC AUC of two immunochemical FOBTs. Protocol §7.1 says primary endpoints are confirmatory. SAP and report retain quantitative sensitivity primary. The report identifies secondary outcomes not presented, including AUC, and regards secondary analyses as exploratory.

**Reported-versus-comparator:** Quantitative specificity is secondary in the report but included in broader protocol primary lists. Qualitative sensitivity, qualitative specificity and ROC AUC fall within the broad both-assay list but are secondary in the SAP/report; AUC results are explicitly absent. Narrow protocol clauses agree with the report and are retained as alternative source-grounded interpretation.

**Reasoning procedure:** Compare the exact outcome-status lists within one supplied protocol version and between PLAN and REPORT. Preserve the explicit SAP amendments to population and missing timing; neither explicitly reconciles outcome status. Consolidate the repeated hierarchy pattern into one candidate.

**Calculation:** Categorical status comparison; recomputed rounding intervals and relative discrepancy are not applicable. No numeric estimate, interval or P-value conflict is asserted. Both statistical passes separately review all inferential relationships.

**Affected result or extracted value:** Primary/confirmatory versus secondary/exploratory status of quantitative-specificity differences −6.4 percentage points (95% CI −9.6 to −3.2), P<.001, and −3.1 (−5.4 to −0.8), P=.008; qualitative-sensitivity difference 12.7 (0.1 to 24.7), P=.048, and qualitative-specificity difference −8.0 (−11.0 to −4.9), P<.001; and completeness of AUC reporting if the broader primary list governed.

**Why context does not resolve it:** Route A category 5 requires registration of a reproduced outcome-status conflict. Plausible precedence of detailed endpoint sections does not remove the express broader primary language; the package supplies no explicit hierarchy reconciliation.

**Alternative source-grounded interpretations:** Detailed endpoint sections/SAP may establish the intended narrow primary list, while broad synopsis/power wording retains another specification. Alternatively a broader original list may have been narrowed. The package does not identify the mechanism or governing hierarchy, and no actual conclusion change is inferred.

**Mechanical evidence recheck:** Fresh root/evidence_recheck inspected all eleven exact source pages; source and comparator statements matched, rule applicable and categorical discrepancy reproduced; no transcription or classification replacement. Evidence state reproduced.

**Potential downstream evidence impact:** A data extractor could classify quantitative specificity or qualitative sensitivity/specificity as primary/confirmatory or secondary/exploratory depending on the plan clause selected, and could assess AUC reporting completeness differently. No actual propagation, change in the paper's conclusion, or quantitative correction is asserted.

**Exact human question:** Which prespecified primary outcome hierarchy governed quantitative specificity, qualitative sensitivity/specificity and ROC AUC, and what supplied statement reconciles the broad protocol lists with the narrow endpoint sections/SAP and the report's secondary/exploratory or unreported status?

# Downstream Evidence-Chain Considerations

Quantitative evidence extraction relies on preserving the outcome, assay, threshold, analysis set, time point, contrast and inferential status attached to a result. A confirmed hierarchy issue could affect the primary/confirmatory versus secondary/exploratory labels an extractor records or the completeness assessment for a planned outcome. Source-linked comparison permits those possibilities to be examined without assigning a governing hierarchy.

The report documents potential relevance to systematic reviews, meta-analyses or guidelines. It does not establish that any candidate propagated into another evidence product or changed a conclusion. Reported numerical estimates and source-grounded alternatives remain separately traceable; the categorical candidate does not supply a replacement numerical value.

# Limitations and Missing Definitions

All 88 supplied pages and all mapped relationships are covered; no scientific coverage gap remains. The review is bounded by the supplied package and aggregate results. The [limitations record](review_1_6_2/limitations.md) preserves the following limits.

- The supplied broad and narrow primary-outcome clauses have no explicit governing-clause precedence or hierarchy amendment. SAP changes on physical page 9 disclose population/missingness changes, without reconciling metric status. This missing hierarchy definition limits resolution of C001, while the printed categorical comparison is reproduced.
- The broad two-assay ROC AUC wording does not provide separate assay-specific AUC definitions or numerical estimates. No unprinted qualitative AUC value or effect is inferred.
- Exact observed-data P-value algorithms, individual test statistics and standard errors are not supplied for the six main contrasts. Their stated significance and interval compatibility can be checked, but an exact P-value inversion is not asserted from the CI convention alone.
- Exact planning algorithms and sex-specific allocation inputs are unprinted. Power and interaction calculations are diagnostics where their precise generating specification is unavailable. The site likelihood-ratio reference distribution, fit details and participant-level records are not supplied for exact model reconstruction.
- Participant-level first-sample dates, duplicate selection and delayed-collection counts are unavailable. Aggregate sample frequencies do not establish that a specific participant or primary denominator was affected by the screened timing observation. The dataset-availability statement supplies no raw dataset, and no external source was retrieved.
- DOC-004 physical page 7 visibly shows dashes in three women's PPV point-difference cells, whereas its embedded text layer contains numerical tokens. Direct source-page confirmation retains the visible dashes and separates hidden metadata. The printed intervals reproduce; the derivative/display distinction is not a candidate.
- Some historical extraction/rendering versions are unrecorded, and earlier text/OCR layers contain character or cell-reading limitations. Source-matched native/layout assets and direct visual confirmation closed the relevant reading gaps. Protocol pages 20 and 49 were freshly mapped on CPU.

# Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

Routing preflight is [PASS](review_1_6_2/routing_preflight.md): run model gpt-6.1-sol, source DEFAULT, execution INTERACTIVE_CLI and provider CURRENT_SESSION. The coordinator uses high reasoning effort; ordinary specialists medium; statistical, screening, recheck and audit specialists high. All ten named presets were verified. No model substitution or reasoning escalation occurred.

The [execution manifest](review_1_6_2/agent_execution_manifest.md) records thirteen actual runtimes, including the coordinator, the disjoint optional support shard and this fresh report generator. Every mandatory specialist stage has a fresh distinct runtime. Both statistical passes use distinct high-effort agents. No second inclusion screen was needed because pass 2 emitted no findings.

| Stage | Runtime agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper | root/support_protocol_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper_other_shard | root/support_other_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistics_one | gpt-6.1-sol | high | FRESH_SPAWN |
| inclusion_screener | root/initial_screen | gpt-6.1-sol | high | FRESH_SPAWN |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistics_two | gpt-6.1-sol | high | FRESH_SPAWN |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN |

The independent audit reconfirmed all five source hashes and all 108 reused-artifact hashes against the before manifests, with no change. Exact records are [source hashes before](review_1_6_2/source_hashes_before.sha256) and [reused hashes before](review_1_6_2/reused_artifact_hashes_before.sha256). The audit also confirmed local evidence-link existence and physical page bounds. Final hash recomputation, standalone HTML rendering and mechanical validation follow the coordinator's timing finalization; this Markdown assembly does not itself claim a final validator result.

The [tooling record](review_1_6_2/tooling_record.md) records Linux, CPU processing, available direct PDF/render/OCR/Office tools, Poppler 26.01.0 and Pandoc 3.7.0.2. CPU processing was announced before rendering. No fresh OCR, Office conversion, GPU execution or temporary fallback environment was required; fallback removal status is NOT_CREATED. Python was confined to the permitted tooling probe and subsequent renderer/validator; auxiliary scientific arithmetic is recorded as JavaScript.

Two current-run audit metadata descriptions were repaired before assembly: protocol fresh-required scope is physical pages 20 and 49, with sixty reusable-backed pages, and eTable 2 Any-column checks total forty, reflecting ten numeric columns across four Any rows. These repairs change neither supplied source content nor the candidate set or classification.

## Reproducibility Performance

The following exact fields are copied from run_state.md at complete Markdown assembly. The coordinator finalizes finish-dependent values immediately after assembly and before rendering/validation. The planning range reflects source formats, reusable/fresh burden, diagnostic tables and required review waves; it never constrains coverage or candidate count. Local rendering/validation are excluded from the observed review duration unless subsequent model work requires a revised finish time.

- **Target basis:** Five PDFs with 88 physical pages: 7-page main report, 62-page protocol including operational appendices, 10-page SAP, 8-page results supplement and one availability page. Source-matched reusable extraction covers 86 pages; two protocol pages need fresh CPU visual inspection. No Office conversion or broad OCR is required. Protocol/SAP design comparisons and multiple diagnostic-performance tables require bounded parallel mapping, three checker lanes, independent screening, recheck, two statistical passes and final audit/report waves. These scope, reuse and review-wave considerations support a 35-50 minute package-specific planning range.
- **Total source units:** 88
- **Fresh-source units:** 2
- **Target elapsed minutes:** 35-50
- **Started UTC:** 2026-10-11T04:55:09Z
- **Finished UTC:** 2026-10-11T05:30:31Z
- **Observed elapsed minutes:** 35.37
- **Target status:** MET_TARGET
- **Exceedance causes:** None
