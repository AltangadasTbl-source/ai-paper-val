# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.1

**Pending Human Adjudication**

Paper package: *Effect of a Nutritional and Behavioral Intervention on Energy-Reduced Mediterranean Diet Adherence Among Patients With Metabolic Syndrome: Interim Analysis of the PREDIMED-Plus Randomized Clinical Trial* (JAMA, 2019; package jama.2019.14630).

## Executive Quality-Control Summary

**Stable candidate count: 0.** No stable candidates were identified after complete scientific mapping of all 149 supplied PDF pages, review of 259 unique numeric relationships and 276 unique statistical relationships, both fresh statistical passes, independent screening, mechanical evidence recheck of the empty stable-ID set, and the independent quality-control audit.

The initial checkers emitted three formal findings. All three received an independent `SCREENED_OUT` decision with reason `CONDITIONAL_OR_UNREPORTED`; no finding received a stable C ID. Statistical pass 2 and the quality audit emitted no additional findings. The auditor also reviewed all 152 checker-excluded observation rows across the four review lanes and upheld the complete empty candidate set. These counts describe this supplied package and the stated inclusion threshold; they are not calibrated to any expected number.

This is quantitative reporting quality control for interpretation and evidence extraction. The zero-candidate result does not establish that every unreported analytic detail is known or that every result can be independently reconstructed from summary data. The limitations below retain the source-defined attendance, plan-applicability, and analytic-input uncertainties. Human review remains responsible for adjudication.

## Package and Reused-Evidence Provenance

Five supplied PDFs form the complete direct-source package. Document roles were assigned by content and independently confirmed by the evidence rechecker. Physical PDF pages are used throughout.

| Source ID | Actual supplied file and identity location | Content role | Total pages |
|---|---|---|---:|
| DOC-001 | [jama_saynorea_2019_oi_190106_1635377898.43062.pdf — main article, PDF p. 1](<../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1>) | REPORT | 14 |
| DOC-002 | [joi190106supp1_prod_1635377898.47058.pdf — protocol, PDF p. 2](<../joi190106supp1_prod_1635377898.47058.pdf#page=2>) | PLAN | 75 |
| DOC-003 | [joi190106supp2_prod_1635377898.49605.pdf — SAP title/version, PDF p. 2](<../joi190106supp2_prod_1635377898.49605.pdf#page=2>) | PLAN | 30 |
| DOC-004 | [joi190106supp3_prod_1635377898.49725.pdf — results-supplement contents, PDF p. 1](<../joi190106supp3_prod_1635377898.49725.pdf#page=1>) | REPORT | 29 |
| DOC-005 | [joi190106supp4_prod_1635377898.50723.pdf — retrospective data-sharing statement, PDF p. 1](<../joi190106supp4_prod_1635377898.50723.pdf#page=1>) | REPORT | 1 |
| Total | Five direct-source PDFs | Three REPORT and two PLAN documents | 149 |

No supplied Office, workbook, or CSV source was found. The data-sharing statement is administrative REPORT content; its page was mapped even though no additional quantitative relationship was applicable.

The [evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md) records 119 existing evidence/document assets: 90 `USABLE`, 27 `PARTIAL`, and 2 `DUPLICATE`. Of these, 97 were reused or retained for provenance and hashed. Complete source-matched whole-document layouts cover all 149 pages and were byte-compared with current direct `pdftotext -layout` output. Retained rendered pages and OCR support tables, sparse continuation pages, and figures. Some older derivative engine metadata is unavailable; each asset's recorded engine and fitness remain visible in the inventory.

Reuse served as a preprocessing optimization. Every supplied page received newly reconstructed scientific mapping. Selected legacy page manifests, narrative maps interleaving prior comparisons, prior candidates, and prior review conclusions did not define discovery scope. The [source inventory](review_1_6_1/source_inventory.md), [source coverage](review_1_6_1/source_coverage.md), and [coverage manifest](review_1_6_1/coverage_manifest.md) retain the disjoint assignments and durable handoffs.

## Scope, Complete Coverage, and Exclusions

The review applied the four focus areas in `QUALITY_CONTROL_SCOPE.md`: counts and denominators; estimate and test logic; statistical method logic; and planned versus reported statistical design. Matching accounted for outcome, time point, population, contrast, model, units, and reference group before comparing values. Primary and key secondary result comparisons, analysis-population sizes, and planned decision rules received the scope assessment required by the workflow.

| Source ID | Exact mapped scope | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---:|---:|---:|---:|---|
| DOC-001 | PDF pp. 1–14 | 14 | 14 | 0 | 14 | COMPLETE |
| DOC-002 | PDF pp. 1–75 | 75 | 75 | 0 | 75 | COMPLETE |
| DOC-003 | PDF pp. 1–30 | 30 | 30 | 0 | 30 | COMPLETE |
| DOC-004 | PDF pp. 1–29 | 29 | 29 | 0 | 29 | COMPLETE |
| DOC-005 | PDF p. 1 | 1 | 1 | 0 | 1 | COMPLETE |
| Total | All supplied pages | 149 | 149 | 0 | 149 | COMPLETE |

Reusable plus fresh-required units equals total units in every row, and mapped units equals total units. Zero fresh-required preprocessing pages does not mean zero new scientific mapping. Context-only pages, references, affiliations, separator pages, and the data-sharing statement were explicitly covered. The [coordinator coverage verification](review_1_6_1/quality/coordinator_coverage_verification.md) and [independent quality audit](review_1_6_1/quality/evidence_quality_audit.md) confirm each complete consecutive page set. There is no scientific coverage gap.

The review excluded observations resolved by display precision, obvious notation or wording, model-versus-crude distinctions, immediate context, unsupported assumptions or unreported details, peripheral comparisons, and matters outside the four focus areas. Peripheral baseline descriptions, individual-time-point contributor counts, administrative details, and exploratory displays did not qualify without a demonstrated effect on a primary or key secondary result, an analysis-population size, or a planned decision rule. Display-zero P values alone did not qualify. The review did not undertake a raw-data, broad methodological, clinical, novelty, or misconduct audit and did not prescribe a preferred analysis.

## Quantitative and Statistical Relationship Coverage

The freshly reconstructed [main evidence map](review_1_6_1/extraction/main_quantitative_evidence.md) and [support evidence map](review_1_6_1/extraction/support_quantitative_evidence.md) underpin the canonical inventories. Relationship counts refer to unique registered IDs, not repeated cross-references or duplicated merged text.

| Disjoint relationship scope | Numeric relationships | Statistical relationships | Statistical pass 1 | Statistical pass 2 |
|---|---:|---:|---|---|
| Main report and shared plan relationships | 106 | 118 | COMPLETE | COMPLETE |
| Support A: eTables 1–5, eFigures 1–2, and related context | 80 | 81 | COMPLETE | COMPLETE |
| Support B: eTables 6–9 and eFigure 3 | 73 | 77 | COMPLETE | COMPLETE |
| Total unique relationships | 259 | 276 | 276 of 276 | 276 of 276 |

Numeric checking covered participant-flow arithmetic, analyzed and outcome-specific populations, totals, percentages, units, direction, effect-measure identity, and matched result occurrences. Statistical checking covered estimate containment, interval ordering, direction, test/interval compatibility when source inputs supported it, model and missing-data logic, and plan/report analysis, endpoint, intervention, power, and decision-rule comparisons. Half-unit display-precision intervals were applied before treating a printed difference as a finding. Adjusted or modeled contrasts were not required to equal crude differences of rounded values.

Every one of the 276 statistical relationships has explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records. Each pass used three fresh high-effort agents, and all six runtime IDs are distinct. Pass 2 read the complete current ledger, screening, and recheck context and emitted no new findings. Where test, interval, pooling, or design inputs were unavailable, the relationship still received both completion records with the limitation retained; a diagnostic approximation did not substitute for the reported analysis.

The [numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6_1/statistics/relationship_inventory.md), [statistical completion index](review_1_6_1/quality/statistical_completion_index.md), and canonical [numeric](review_1_6_1/checkers/numeric_consistency.md), [cross-source](review_1_6_1/checkers/cross_source_consistency.md), [pass-1](review_1_6_1/checkers/statistical_pass_1.md), and [pass-2](review_1_6_1/checkers/statistical_pass_2.md) checkers retain the detailed assessments.

## Inclusion Screening Summary

A finding qualifies only if the source comparison is reproduced, falls within focus A–D, remains unresolved by immediate context for a statistically literate reader in the field, and could change interpretation or extraction of a named result. A finding failing any criterion receives one screened-out reason code and no stable C ID.

The [independent screening log](review_1_6_1/screening/inclusion_screen.md) contains exactly three finding rows and one decision per finding. The independent auditor upheld all three decisions. Pass 2 emitted no finding, so a second inclusion screen was not applicable; the audit emitted no finding or screening-decision amendment.

| Screening stage | Findings screened | INCLUDE | SCREENED_OUT | Stable candidates added |
|---|---:|---:|---:|---:|
| Initial | 3 | 0 | 3 | 0 |
| Pass 2 | 0 | 0 | 0 | 0 |
| Audit | 0 | 0 | 0 | 0 |
| Total | 3 | 0 | 3 | 0 |

| Formal screening reason code | SCREENED_OUT count |
|---|---:|
| NOT_REPRODUCED | 0 |
| ROUNDING_OR_DISPLAY_PRECISION | 0 |
| NOTATION_OR_TYPOGRAPHY | 0 |
| TERMINOLOGY_OR_WORDING | 0 |
| MODEL_VERSUS_CRUDE | 0 |
| CONTEXT_RESOLVES | 0 |
| CONDITIONAL_OR_UNREPORTED | 3 |
| PERIPHERAL_COMPARISON | 0 |
| OUT_OF_FOCUS | 0 |
| DUPLICATE_OF_INCLUDED | 0 |
| Total | 3 |

The screened completion-count comparison required an unsupported equivalence between follow-up attendance and availability of every dietary measurement. The screened weight-analysis and waist-interval comparisons acknowledged the SAP's explicit year-one schedules; they required an unestablished mapping between the selected exploratory nutrition-cohort analysis and the scheduled clinical-main analysis, including applicable plan version and missingness scope. Exact source-grounded rationales remain in the screening log. These findings are not candidate cards.

Checker self-screening is recorded separately from the three formal screening rows. Its 152 rows retain observations considered across lanes; recurrence across lanes does not imply 152 distinct issues.

| Checker lane | Checker-excluded observation rows audited |
|---|---:|
| Numeric consistency | 38 |
| Cross-source consistency | 27 |
| Statistical pass 1 | 44 |
| Statistical pass 2 | 43 |
| Total across lanes | 152 |

| Checker-exclusion reason code | Rows |
|---|---:|
| NOT_REPRODUCED | 3 |
| ROUNDING_OR_DISPLAY_PRECISION | 17 |
| NOTATION_OR_TYPOGRAPHY | 9 |
| TERMINOLOGY_OR_WORDING | 6 |
| MODEL_VERSUS_CRUDE | 7 |
| CONTEXT_RESOLVES | 46 |
| CONDITIONAL_OR_UNREPORTED | 40 |
| PERIPHERAL_COMPARISON | 24 |
| OUT_OF_FOCUS | 0 |
| DUPLICATE_OF_INCLUDED | 0 |
| Total across lanes | 152 |

The [complete exclusion index](review_1_6_1/quality/checker_exclusion_index.md) preserves these rows, and the [quality audit](review_1_6_1/quality/evidence_quality_audit.md) records their independent bidirectional threshold review. No excluded observation led to an appended candidate.

## Review-Domain Summary

The following counts describe stable candidates only. Each table sums to the stable candidate count of zero. Screened-out findings receive no candidate domain, relationship type, evidence state, or inclusion-audit classification.

| Review domain | Definition | Stable candidate count |
|---|---|---:|
| statistical_results | Counts, denominators, estimates, intervals, tests, or statistical method logic in REPORT material. | 0 |
| report_internal_inconsistency | REPORT material conflicts about the outcome, time, population, or comparison to which a number belongs. | 0 |
| protocol_report | REPORT versus PLAN statistical design or analysis comparison. | 0 |
| plan_material | A statistical design inconsistency solely within PLAN material relied on by the reported analysis. | 0 |
| Total | | 0 |

| Primary relationship type | Meaning | Stable candidate count |
|---|---|---:|
| P_R | REPORT versus PLAN | 0 |
| P_P | Within or between PLAN documents | 0 |
| S_C | Between different REPORT documents | 0 |
| S_W | Within one REPORT document | 0 |
| Total | | 0 |

Relationship precedence is `P_R > P_P > S_C > S_W`. Corroborating-only plan material does not create a conflicting relationship. `P_R` maps to `protocol_report`, `P_P` to `plan_material`, and `S_C`/`S_W` to one of the two REPORT domains by content.

| Evidence state | Stable candidate count |
|---|---:|
| reproduced | 0 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 0 |

Inclusion-audit counts are `CONFIRMED` 0 and `QUESTIONED` 0. The completed empty-set recheck is not a `not_reproduced` classification. The [ledger classification table](review_1_6_1/candidate_ledger.md) has no candidate data row.

## Candidate Index

No stable candidates were identified

Completed scope: all five supplied PDFs, 149 of 149 pages, 259 numeric relationships, 276 statistical relationships in both fresh passes, three formal screening decisions, 152 checker-excluded observation rows, mechanical recheck of zero stable IDs, and the complete independent scientific audit.

| Stable ID | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|

The stable ID set is empty and agrees with the [candidate ledger](review_1_6_1/candidate_ledger.md), [evidence recheck](review_1_6_1/verification/evidence_recheck.md), and [quality audit](review_1_6_1/quality/evidence_quality_audit.md).

## Candidate Evidence Cards

There are no stable candidate evidence cards. The complete empty set is reported; screened-out findings and checker exclusions do not receive cards or human dispositions.

## Downstream Evidence-Chain Considerations

Evidence extraction should retain the reported outcome, time point, analysis population, model, effect scale, confidence level, and multiplicity status together. Main multiple-imputation and completer results represent separately labeled analyses; modeled changes should retain their reported model labels. Attendance, outcome availability, and analysis inclusion require distinct definitions before one is substituted for another.

No registered candidate requires an alternative extraction value in this report. The limitations may nevertheless guide a human extractor when recording observed follow-up or identifying which plan governed an exploratory analysis. The report does not establish that a value propagated into a synthesis, that any conclusion changed, or that downstream harm occurred. Its purpose is to preserve source identity and bounded extraction context.

## Limitations and Missing Definitions

All supplied scientific units were mapped; no tooling or scientific coverage gap remains. The [limitations record](review_1_6_1/limitations.md) retains these boundaries:

- **Follow-up completion definition:** The [abstract, PDF p. 1](<../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1>), [flow diagram, PDF p. 3](<../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=3>), and [Table 2, PDF p. 5](<../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5>) identify analyzed and instrument-specific observed/imputed information. They do not provide a matched visit-attendance count and definition that equates follow-up completion with every dietary outcome being observed. No substitute attendance total was inferred.
- **Report-specific plan applicability and version mapping:** The [SAP schedule, PDF p. 9](<../joi190106supp2_prod_1635377898.49605.pdf#page=9>) expressly includes year-one weight and waist. Its [ancillary interval rule, PDF p. 12](<../joi190106supp2_prod_1635377898.49605.pdf#page=12>) includes waist, and its [analysis/missingness specification, PDF p. 26](<../joi190106supp2_prod_1635377898.49605.pdf#page=26>) gives completer-first priority and a two-year-loss imputation target. The [version record, PDF p. 2](<../joi190106supp2_prod_1635377898.49605.pdf#page=2>) identifies November 2018 version 1 and July 2019 version 2, but substantive version-1 text and revision mapping are absent. No supplied report-specific SAP establishes how those rules apply to the selected exploratory cohort using the March 2019 database. Neither chronology nor the exploratory label alone resolves this applicability question.
- **Exact inferential reconstruction:** The [main methods, PDF p. 4](<../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4>) and [results methods, PDF p. 24](<../joi190106supp3_prod_1635377898.49725.pdf#page=24>) supply general model and imputation context without every cell's test identity, statistic, degrees of freedom, covariance/variance estimator, interval construction, or multiple-imputation pooling details. Exact CI/P compatibility or adjusted interval endpoints cannot universally be reconstructed from printed summaries.
- **Power and figure inputs:** The supplied plan's power material and report figures do not supply every formula/design input or every plotted count, denominator, or construction input needed for exact numerical reproduction. Source-grounded diagnostics were retained as diagnostics; absent inputs were not inferred.
- **Data boundary and derivative provenance:** No participant-level raw data or report-specific SAP is supplied. Some retained derivative engine metadata is undocumented, although whole-document layouts were matched to current source extraction and targeted source-page confirmation was performed. No external evidence was used to fill these gaps.

These limitations constrain what can be inferred from the supplied package. They do not establish a candidate reporting inconsistency, and they do not alter the complete source or relationship coverage counts.

## Human Adjudication Checklist

The current stable-ID set contains no card requiring per-candidate adjudication. A human reviewer may inspect the source coverage, screening rationale, and bounded definitions above when assessing the review's scope and its use for extraction.

1. Confirm that the five actual supplied files and their complete page sets match the intended package.
2. Review the three independent screening rationales and the attendance/plan-applicability limits against the cited source pages.
3. Preserve distinctions between analysis inclusion, instrument-specific observations, attendance, and separately labeled modeled analyses in any extraction.
4. If additional supplied evidence establishes a qualifying inconsistency, require a stable-ID registration, exact source recheck, complete classification, and a full evidence card before adjudication.

For any subsequently registered card, status remains **Pending Human Adjudication**, and the human fields use the following exact blanks:

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Reproducibility and source integrity

The [routing preflight](review_1_6_1/routing_preflight.md) records `PASS`, `INTERACTIVE_CLI`, `CURRENT_SESSION`, coordinator `gpt-6.1-sol`/`high`, and verification of all ten named specialist presets. The [tooling record](review_1_6_1/tooling_record.md) records Linux and available direct PDF, rendering, CPU OCR, Office, hashing, and Pandoc capabilities. Recorded engines include Poppler 26.01.0, Tesseract 5.5.0, Pandoc 3.7.0.2, and sha256sum/uutils coreutils 0.10.0. No fallback environment was needed or created. No GPU or web evidence was used.

Before scientific work, all five sources and 97 reused assets were SHA-256 hashed in the [source before-manifest](review_1_6_1/source_hashes_before.sha256) and [reused-asset before-manifest](review_1_6_1/reused_artifact_hashes_before.sha256). The independent audit's preservation checks returned 5 of 5 source matches and 97 of 97 reused-asset matches. Post-assembly [source hashes](review_1_6_1/source_hashes_after.sha256) and [reused-asset hashes](review_1_6_1/reused_artifact_hashes_after.sha256) are identical to their before-manifests. The audit's pre-report scan checked 1791 local Markdown links across 51 then-present run files, with no unresolved target or out-of-range direct-source page fragment; the report generator separately confirmed all 62 links in its report and limitations artifacts. The standalone HTML accompanies this Markdown report. The [final mechanical validation record](review_1_6_1/review_validation.json) records the package completion checks and their status.

### Agent execution

Every actual runtime listed in the current [execution manifest](review_1_6_1/agent_execution_manifest.md) appears below. All specialists were fresh spawns; each statistical pass uses runtime IDs distinct from the other pass. Runtime task names are the identifiers exposed by the collaboration service, normalized by omitting the leading slash.

| Stage | Runtime agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper | root/protocol_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper_results_shard | root/sap_results_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_support_a | root/numeric_support_a | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_support_b | root/numeric_support_b | gpt-6.1-sol | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistics_one_main | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_1_support_a | root/statistics_one_a | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_1_support_b | root/statistics_one_b | gpt-6.1-sol | high | FRESH_SPAWN |
| cross_source_consistency_reviewer | root/cross_plan | gpt-6.1-sol | medium | FRESH_SPAWN |
| cross_source_report_shard | root/cross_report | gpt-6.1-sol | medium | FRESH_SPAWN |
| inclusion_screener | root/inclusion_initial | gpt-6.1-sol | high | FRESH_SPAWN |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistics_two_main | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2_support_a | root/statistics_two_a | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2_support_b | root/statistics_two_b | gpt-6.1-sol | high | FRESH_SPAWN |
| quality_control_auditor | root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN |

A pass-2 inclusion-screening runtime was not applicable because pass 2 emitted no finding. The mechanical evidence recheck completed the explicit zero-ID scope and confirmed source roles; no candidate evidence state was assigned. The scientific audit completed the complete source, relationship, finding, exclusion, and classification scope.

### Reproducibility performance

The following exact fields agree with the finalized run state. Completion timing records the scientific review and complete Markdown assembly; rendering and local mechanical validation follow assembly. The selected planning range concerns the package's preprocessing, mapping burden, figures, relationship volume, and mandatory review waves; it is not a hard timeout or a candidate-count criterion.

- **Target basis:** Five PDF sources contain 149 unique pages, all with source-matched reusable whole-document layouts; 0 pages require new preprocessing. The 75-page protocol and 30-page SAP require complete fresh relationship mapping, while dense report tables and figures need retained visual confirmation. Separate bounded mapping shards, concurrent initial checks, two mandatory statistical passes, independent screening, recheck, audit, and report generation require successive agent waves. No Office conversion, new whole-document OCR, or missing-tool installation is expected.
- **Total source units:** 149
- **Fresh-source units:** 0
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-10-11T02:46:06Z
- **Finished UTC:** 2026-10-11T03:29:06Z
- **Observed elapsed minutes:** 43.00
- **Target status:** MET_TARGET
- **Exceedance causes:** None
