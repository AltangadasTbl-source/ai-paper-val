# Quantitative Quality-Control Consistency Review — Workflow 1.6.1

**Pending Human Adjudication**

This report supports human review of quantitative reporting in the supplied paper package. Its classifications, coverage records, and inclusion screening are quality-control records, not a paper-level adjudication.

## Executive Quality-Control Summary

No stable candidates were identified. Scope: all five supplied PDFs, comprising 88 physical pages, reviewed for counts and denominators, estimate and test logic, statistical method logic, and planned-versus-reported statistical design. All 88 pages were mapped, using 85 reusable-backed units and fresh direct visual mapping of three protocol pages.

The completed review covers 107 numeric relationships, 116 statistical relationships in two distinct fresh statistical passes, and 36 cross-source comparison groups. The four checkers emitted zero formal findings. The independent screening log contains zero INCLUDE decisions and zero SCREENED_OUT finding decisions. The quality audit reconsidered all 81 checker exclusion entries and identified no observation meeting the inclusion threshold. These entries overlap across checker lanes and are not 81 distinct reporting issues.

The stable ledger, evidence recheck, quality audit, candidate index, and report evidence-card set are identical and empty. No candidate classification or evidence state is assigned. The result is bounded by the supplied evidence and the missing definitions listed below; it does not establish that every unreported analysis detail can be reconstructed.

## Package and Reused-Evidence Provenance

The package contains the main article by Brenner and colleagues and four supplements. Source roles follow their content. The prospective protocol and SAP are PLAN; the article, results supplement, and retrospective availability statement are REPORT.

| Source ID | Actual supplied filename and source link | Document role | Content | Physical PDF pages |
|---|---|---|---|---:|
| DOC-001 | [jama_brenner_2019_oi_190039.pdf](../jama_brenner_2019_oi_190039.pdf#page=1) | REPORT | Main original investigation, participant flow, and Tables 1–3 | 7 |
| DOC-002 | [joi190039supp1_prod.pdf](../joi190039supp1_prod.pdf#page=1) | PLAN | Clinical study protocol version 1.5, dated 24 July 2015 | 62 |
| DOC-003 | [joi190039supp2_prod.pdf](../joi190039supp2_prod.pdf#page=1) | PLAN | Statistical analysis plan, including explicit analysis changes | 10 |
| DOC-004 | [joi190039supp3_prod.pdf](../joi190039supp3_prod.pdf#page=1) | REPORT | Eligibility material and observed-results eTables | 8 |
| DOC-005 | [joi190039supp4_prod.pdf](../joi190039supp4_prod.pdf#page=1) | REPORT | Retrospective availability statement | 1 |

No Office document, workbook, CSV, structured result file, or individual raw dataset is supplied. External publications and code pointers were not retrieved. Only local supplied-package evidence was used.

The [source inventory](review_1_6_1/source_inventory.md) records SHA-256 identities and complete physical-page scopes. The [evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md) records 107 reused extraction, image, and provenance assets: 58 USABLE, 44 PARTIAL, and 5 DUPLICATE after fitness reassessment. Asset counts are distinct from source-page counts; overlapping derivatives add no source units. Canonical native/layout text was compared with the current source. OCR, page images, maps, and metadata served as locators and transcription aids, while direct sources retained authority. Historical candidates, dispositions, and reports were preserved and did not define discovery.

Fresh CPU Poppler renders closed the protocol text-fitness gaps on [PDF p.16](../joi190039supp1_prod.pdf#page=16), [p.20](../joi190039supp1_prod.pdf#page=20), and [p.49](../joi190039supp1_prod.pdf#page=49). A targeted direct render also confirmed results-supplement [PDF p.7](../joi190039supp3_prod.pdf#page=7), whose reusable full-page images already supplied coverage; this confirmation adds no fresh-required unique unit. Native hidden numerals and visibly minus-only women's PPV cells remain explicitly distinguished in the evidence records.

## Scope, Complete Coverage, and Exclusions

| Source ID | Total source units | Reusable units | Fresh-required units | Mapped units | Coverage status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 7 | 7 | 0 | 7 | COMPLETE |
| DOC-002 | 62 | 59 | 3 | 62 | COMPLETE |
| DOC-003 | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-004 | 8 | 8 | 0 | 8 | COMPLETE |
| DOC-005 | 1 | 1 | 0 | 1 | COMPLETE |
| **Total** | **88** | **85** | **3** | **88** | **COMPLETE** |

The unit is one physical PDF page. Every source partitions into reusable and fresh-required units, and every mapped count equals its total. Covers, references, contacts, signatures, administrative appendices, and availability material have explicit mapped records even where no current result relationship applies. Protocol physical pagination differs from printed pagination after its repeated signature page; evidence links consistently use physical PDF pages.

The [coverage manifest](review_1_6_1/coverage_manifest.md) assigns disjoint main, protocol, and remaining-support mapping scopes, followed by complete checking, screening, recheck, audit, and reporting stages. The [main evidence map](review_1_6_1/extraction/main_quantitative_evidence.md) and [support evidence map](review_1_6_1/extraction/support_quantitative_evidence.md) preserve all mapped content and both support parts. No scientific coverage gap remains.

The review applied the four-part inclusion threshold: a source-reproduced inconsistency, within the quantitative focus, unresolved by immediate context for a statistically literate field reader, and plausibly relevant to interpretation of a named result or extraction of a value. Display precision was assessed using half-unit intervals. Sample counts, participant counts, events, analysis populations, scheduled days, and actual days were matched before comparisons. Model estimates were not treated as crude count ratios without a supplied basis.

Excluded scope includes broad clinical or design critique, raw-data auditing, preferred-analysis proposals, novelty and misconduct assessment, and peripheral comparisons without a primary/key-secondary result, analysis-population, or planned-decision consequence. Rounding, readily resolved notation or wording, conditional observations, and absent details alone do not qualify.

## Quantitative and Statistical Relationship Coverage

| Review lane | Completed scope | Completion record | Formal findings |
|---|---|---|---:|
| Numeric consistency | N001–N107; all 107 numeric relationship groups | [Numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md) and [numeric checker](review_1_6_1/checkers/numeric_consistency.md) | 0 |
| Cross-source consistency | XS01–XS36; all 36 matched comparison groups | [Cross-source checker](review_1_6_1/checkers/cross_source_consistency.md) | 0 |
| Statistical pass 1 | S001–S116; every relationship explicitly PASS_1_COMPLETE | [Pass 1](review_1_6_1/checkers/statistical_pass_1.md) | 0 |
| Statistical pass 2 | S001–S116; every relationship explicitly PASS_2_COMPLETE | [Pass 2](review_1_6_1/checkers/statistical_pass_2.md) | 0 |

The [statistical inventory](review_1_6_1/statistics/relationship_inventory.md) retains both pass records for every S ID. Its 116 relationship records contain 108 inferential result/test endpoints and 44 method/design records: 36 paired supplementary records retain 72 endpoint subcells alongside 36 individual main-table endpoints. The inferential total consists of 90 effect-difference intervals and 18 site SD/P endpoints. Grouping did not omit an outcome, sex, assay, or cutoff subcell.

Numeric review reconciled participant-flow branches, all 27 diagnostic matrices, diagnostic proportions and differences, sample-category partitions, subgroup additions, and full versus nonmissing denominators. The independent audit reproduced 270 diagnostic point comparisons, 72 All=Men+Women count-cell comparisons, 20 valid-sample partitions, 40 Any-row column totals, and 32 baseline percentages.

Both statistical passes checked ordered interval endpoints, point containment, direction, significance decisions, analysis definitions, and applicable design rules. The quality audit independently reproduced all 90 Agresti-Caffo difference intervals; all 180 displayed limits reconcile within their 0.05-percentage-point display intervals. Exact individual outcome P algorithms and site-test reference laws were not inferred. Power calculations were explicitly diagnostic approximations where the exact implementation was unspecified.

Matched primary results agree between the [abstract, PDF p.1](../jama_brenner_2019_oi_190039.pdf#page=1) and [Table 2, PDF p.5](../jama_brenner_2019_oi_190039.pdf#page=5): sensitivity differences of 9.8 percentage points (95% CI −3.1 to 22.2; P=.14) and 6.0 points (−5.7 to 17.5; P=.32). The reported nonsignificant primary conclusion agrees with both intervals. Scheduled-day intention-to-screen, exact-day per-protocol, combined-sample, pooled, subgroup, and interaction hypotheses were kept distinct.

The [SAP, PDF p.9, section 7](../joi190039supp2_prod.pdf#page=9) explicitly changes the primary analysis set and missing-collection-date treatment. The [SAP, PDF p.4 footnote](../joi190039supp2_prod.pdf#page=4) renumbers medication day 1 as day 0, preserving the elapsed two-day primary window. These supplied context statements resolve earlier wording without creating a candidate. Planned design targets and realized enrollment were also distinguished.

Two different fresh high-effort agents performed statistical passes 1 and 2. Pass 2 read the complete ledger, independent screen, and mechanical recheck, emitted no new finding, and required no second finding-screening stage. The [canonical quality audit](review_1_6_1/quality/evidence_quality_audit.md) and its three durable parts completed independent coverage and inclusion review without changing a supplied scientific result.

## Inclusion Screening Summary

The counts below reconcile to the single formal table in the [independent inclusion screening log](review_1_6_1/screening/inclusion_screen.md). Inclusion requires all four threshold criteria stated above; there is no expected candidate count.

| Formal finding/decision measure | Count |
|---|---:|
| Findings submitted for independent screening | 0 |
| INCLUDE decisions, reason MEETS_THRESHOLD | 0 |
| SCREENED_OUT finding decisions | 0 |
| Total formal screening decisions | 0 |
| Included distinct issues / stable candidates | 0 |
| Additional pass-2 findings | 0 |
| Additional quality-audit findings | 0 |

| SCREENED_OUT reason code | Formal screening decisions |
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
| **Total** | **0** |

### Checker exclusion catalogues and independent audit

The checker self-screens recorded excluded observations without formal finding IDs. Their 81 entries are separate from the empty formal screening table. The initial three catalogues contain 58 entries; statistical pass 2 adds 23. Independent quality auditing reconsidered every entry in both inclusion directions and identified zero eligible observations.

| Checker catalogue | Exclusion entries audited |
|---|---:|
| Numeric | 14 |
| Cross-source | 22 |
| Statistical pass 1 | 22 |
| Statistical pass 2 | 23 |
| **Total** | **81** |

| Reason code | Checker exclusion entries, across all four lanes |
|---|---:|
| NOT_REPRODUCED | 4 |
| ROUNDING_OR_DISPLAY_PRECISION | 4 |
| NOTATION_OR_TYPOGRAPHY | 8 |
| TERMINOLOGY_OR_WORDING | 2 |
| MODEL_VERSUS_CRUDE | 0 |
| CONTEXT_RESOLVES | 29 |
| CONDITIONAL_OR_UNREPORTED | 26 |
| PERIPHERAL_COMPARISON | 6 |
| OUT_OF_FOCUS | 2 |
| DUPLICATE_OF_INCLUDED | 0 |
| **Total** | **81** |

These totals retain cross-lane repetition as checker provenance; they do not count distinct issues or screened-out formal findings. The quality audit records five current-run accounting/provenance refinements: explicit numeric coverage enumeration, nonmissing indication totals, one exclusion-code refinement, bounded site-model family/link wording, and full-page image provenance. They changed neither a supplied scientific value nor a formal screening decision, and created no stable candidate.

## Review-Domain Summary

The following counts reconcile independently to the stable candidate count of zero. Definitions describe the framework; no classification is assigned to a nonexistent candidate.

| Review domain | Definition | Stable candidates |
|---|---|---:|
| statistical_results | Counts, estimates, intervals, tests, or statistical method logic in REPORT material | 0 |
| report_internal_inconsistency | Conflicting result attribution within or between REPORT materials that leaves the applicable outcome, time, population, or comparison unclear | 0 |
| protocol_report | A statistical design or analysis inconsistency between PLAN and REPORT material | 0 |
| plan_material | A statistical design inconsistency solely within PLAN material on which the reported analysis relies | 0 |
| **Total** | | **0** |

| Relationship type | Definition | Stable candidates |
|---|---|---:|
| P_R | REPORT versus PLAN inconsistency | 0 |
| P_P | Inconsistency solely within PLAN material | 0 |
| S_C | Inconsistency between different REPORT documents | 0 |
| S_W | Inconsistency within one REPORT document | 0 |
| **Total** | | **0** |

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 0 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **0** |

Inclusion-audit counts are CONFIRMED 0 and QUESTIONED 0. The [ledger classification table](review_1_6_1/candidate_ledger.md) has its required header and no data rows. Candidate-specific role comparisons, relationship precedence, rationale, ambiguity, and evidence states have no applicable unit.

## Candidate Index

No stable candidates were identified. Scope: the complete five-PDF package and all mapped quantitative, statistical, and cross-source relationships following both statistical passes and the independent quality audit.

| ID | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|

The index is intentionally empty and matches the stable ledger. No candidate ID is omitted.

## Candidate Evidence Cards

No stable candidates were identified. Scope: all 88 supplied physical pages, 107 numeric relationships, 116 statistical relationships with both passes complete, and 36 cross-source groups, including the independently audited checker exclusions.

There are no applicable evidence cards or candidate-specific adjudication fields. No excluded observation is presented as a card. The [mechanical evidence recheck](review_1_6_1/verification/evidence_recheck.md) confirms the empty stable set; the subsequent quality audit and this report preserve that set.

## Downstream Evidence-Chain Considerations

Evidence extraction should retain each result's analysis population, assay, cutoff, scheduled or actual collection day, comparison direction, and units. Diagnostic samples, unique participants, events, and fitted model SDs are different quantities. Difference intervals should retain their reported construction rather than be replaced with an assumed test inversion or a subtraction of rounded displayed percentages.

No candidate-specific downstream extraction consequence was identified under the inclusion threshold. This report does not claim that propagation, a synthesis conclusion change, or harm occurred. The maps and exact-source links provide traceability for future systematic-review, meta-analysis, guideline, or data-extraction work.

## Limitations and Missing Definitions

The [complete limitations record](review_1_6_1/limitations.md) bounds stronger reconstruction without leaving a scientific coverage gap. The supplied package lacks individual raw data and executable analysis inputs; exact individual outcome P algorithms and unprinted group intervals; individual interaction coefficient/P mappings; site likelihood statistics, reference law, fixed-effects covariance, and exact family/link; exact power-test/correction implementation and sex-specific affected allocations; numerical missingness outputs and treatment-decision boundaries; participant-level duplicate records; complete exploratory outputs; midpoint recruitment counts and a numerical serious-reaction stopping boundary; an evaluated safety denominator; and a numerical assay conversion factor.

These named absences do not establish a reporting issue on their own. Direct native and rendered content were distinguished where needed, and the three protocol extraction-fitness gaps were closed through fresh full-page visual inspection. The supplied evidence supports complete reporting-quality coverage while limiting claims of exact reconstruction beyond the stated methods and inputs. This review does not adjudicate overall study validity or perform a broad methodology audit.

## Human Adjudication Checklist

1. Confirm that the five supplied sources and 88 physical pages constitute the intended package scope.
2. Review the formal zero-finding screening reconciliation and distinguish it from the 81 overlapping checker exclusion entries.
3. Inspect the bounded reconstruction limits and source-native/render distinctions before extracting a result.
4. Retain endpoint, population, timing, assay, cutoff, contrast, and unit definitions when reusing evidence.
5. If human review identifies an additional reporting issue, document its exact supplied-source comparison and apply all four inclusion criteria. There is no existing candidate-specific adjudication to complete.

Every registered candidate would remain Pending Human Adjudication, with validity, importance, action, initials, and notes left as the exact blank placeholder `__`. No substantive human field is prefilled in this empty candidate set.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Source integrity and tooling

The [direct-source hash baseline](review_1_6_1/source_hashes_before.sha256) covers all five PDFs, and the [reused-artifact hash baseline](review_1_6_1/reused_artifact_hashes_before.sha256) covers all 107 reused assets. At the completed quality-audit snapshot, direct SHA-256 checks matched every baseline hash. Final post-assembly hash reconciliation, HTML rendering, cleanup confirmation, and mechanical validation are coordinator completion gates; no final validator status is inferred from the scientific audit.

The [tooling record](review_1_6_1/tooling_record.md) reports Linux with direct pdfinfo, pdftotext, pdftoppm, pdftocairo, tesseract, libreoffice, and pandoc available. Source inspection and fresh page rendering used CPU Poppler; no new OCR, global installation, or GPU operation was required. Fallback environment: NOT_NEEDED; fallback packages/capabilities: None; fallback environment removed: NOT_CREATED. Historical renderer uncertainty and partial OCR fitness are recorded in asset provenance.

The [routing preflight](review_1_6_1/routing_preflight.md) records PASS, INTERACTIVE_CLI, Provider CURRENT_SESSION, Coordinator inference PASS, coordinator gpt-6.1-sol/high, and all ten named specialist presets verified at their required model/effort pairs. Every actual runtime appears once in the manifest below.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a128d8-ef89-7251-8e09-114b0845654c | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/protocol_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_other_shard | root/other_support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_other.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/inclusion_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor_mapping_numeric_shard | root/audit_mapping_numeric | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/mapping_numeric_audit.md |
| quality_control_auditor_cross_source_shard | root/audit_cross_screening | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/cross_source_screening_audit.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |


This table reproduces the complete current [agent execution manifest](review_1_6_1/agent_execution_manifest.md): 15 distinct runtimes, including the coordinator, all mandatory specialist stages, an additional support mapper, and two audit shards. Artifact cells are plain paths relative to review_1_6_1; full report links appear in the relevant sections. Statistical passes use different fresh high-effort runtimes. No second screener was applicable because pass 2 emitted no finding.

### Reproducibility performance

- **Target basis:** Five all-native PDFs contain 88 unique pages, with reusable layout text covering 85 pages and three protocol pages requiring targeted direct visual mapping. No Office conversion or new OCR is expected; direct CPU renders resolve the three text-fitness gaps. Main text has 66427 characters and support text has 217588 characters, requiring one main and two bounded support mapper scopes. Diagnostic-result tables, participant flow, protocol/SAP comparisons, two distinct statistical passes, screening, recheck, audit, and report generation require the full mandatory agent waves. A package-specific 25-40 minute target reflects low preprocessing burden and substantive plan/report relationship coverage.
- **Total source units:** 88
- **Fresh-source units:** 3
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T02:44:53Z
- **Finished UTC:** 2026-10-11T03:23:19Z
- **Observed elapsed minutes:** 38.433
- **Target status:** MET_TARGET
- **Exceedance causes:** None

The exact field labels and current values above are copied from [run_state.md](review_1_6_1/run_state.md). The coordinator finalizes Finished UTC, Observed elapsed minutes, Target status, and bounded Exceedance causes immediately after complete Markdown assembly, then synchronizes these fields before rendering and validation. Pending values do not claim a completed timing or validation gate. Local HTML rendering and mechanical validation lie outside the observed review duration; any later model-assisted repair requires updated timing. The planning target did not cap sources, relationships, findings, or candidates.
