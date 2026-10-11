# ACS QUIK: Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.1

**Pending Human Adjudication.** This report presents candidate reporting issues for human review. Evidence states and inclusion-audit records describe the review process; the five human adjudication fields remain blank for each candidate.

## Executive Quality-Control Summary

Complete review of the supplied four-PDF package identified **2 stable candidates**, C001 and C002. C001 concerns the identification of two adjusted time-effect outputs in Table 2; C002 concerns the relationship between the supplied SAP age-subgroup specification and the reported primary-endpoint age analyses. Both candidates were source-reproduced and their inclusion was independently confirmed. Neither record adjudicates validity or establishes a change in the overall trial conclusion.

All **80 physical PDF pages** were mapped: 79 using reusable evidence assets and one requiring fresh direct rendering. The review covered 298 numeric relationships, 324 statistical relationships in each of two fresh passes, and 120 cross-source comparison relationships. Three emitted findings received independent screening: two INCLUDE decisions and one SCREENED_OUT decision for a duplicate of C002. All 117 checker exclusion rows were separately audited; no additional candidate arose from that audit.

## Package and Reused-Evidence Provenance

The package contains the main ACS QUIK article, its protocol, its SAP, and a mixed operational-toolkit/results supplement. Roles follow the content of each location. The toolkit's sample reports and prospective forms are PLAN material rather than completed trial observations.

| Source ID | Actual source filename | Role by content | Physical PDF pages |
|---|---|---|---:|
| DOC-001 | jama_huffman_2018_oi_170166.pdf | REPORT | 12 |
| DOC-002 | joi170166supp1_prod.pdf | PLAN: protocol dated 22 September 2014 | 32 |
| DOC-003 | joi170166supp2_prod.pdf | PLAN: SAP dated 17 June 2015 | 9 |
| DOC-004 | joi170166supp3_prod.pdf | REPORT p. 1 and pp. 17–27; PLAN pp. 2–16 | 27 |
| Total | Four supplied PDFs | Location-specific roles retained | 80 |

The review reused **77 source-linked assets**: native/layout text, rendered pages, OCR and its source/page metadata, and extraction/document-location notes. Current curation confirmed source matching and recorded usable or partial coverage. Text and OCR served as locators and transcription aids; cited source pages and source-matched images provided final candidate evidence. Historical extraction versions are not asserted where metadata does not supply them. Older candidate selections, screening decisions and conclusions did not define discovery scope.

Full provenance is recorded in the [source inventory](review_1_6_1/source_inventory.md), [evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md), [source hash record](review_1_6_1/source_hashes_before.sha256), and [reused-asset hash record](review_1_6_1/reused_artifact_hashes_before.sha256). Read-only integrity checks recorded by the quality audit matched all four sources and all 77 reused assets; final closure checks are performed by the coordinator after Markdown assembly.

## Scope, Complete Coverage, and Exclusions

The review addressed counts and denominators; estimate, interval and test logic; statistical-method identification; and planned-versus-reported statistical design. Every direct source unit was inspected and mapped, including administrative pages, blank forms and references with no additional applicable trial-result relationship.

| Source | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 12 | 12 | 0 | 12 | COMPLETE |
| DOC-002 | 32 | 31 | 1 | 32 | COMPLETE |
| DOC-003 | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-004 | 27 | 27 | 0 | 27 | COMPLETE |
| Total | 80 | 79 | 1 | 80 | COMPLETE |

The embedded Time and Events diagram on [joi170166supp1_prod.pdf — physical p. 14](../joi170166supp1_prod.pdf#page=14) was absent from reusable text. Fresh CPU rendering and visual mapping closed that gap. Fourteen scanned toolkit pages were covered by source-matched existing OCR and paired images. Rotated flow and graphical displays were inspected visually. The [source-coverage ledger](review_1_6_1/source_coverage.md) and [coverage manifest](review_1_6_1/coverage_manifest.md) retain every source and shard assignment.

Rounding and display precision, immediately resolvable notation or wording, modeled-versus-crude comparisons, conditional or unreported details, peripheral comparisons and observations outside the quantitative scope were screened out under the supplied scope rules. A repeated qualifying pattern is one candidate with all affected locations. The review does not assess raw data, analysis code, broad clinical or design choices, novelty or misconduct, and does not select a preferred analysis.

## Quantitative and Statistical Relationship Coverage

| Review scope | Relationships | Completion |
|---|---:|---|
| Numeric: main A | 100 | COMPLETE |
| Numeric: main B | 89 | COMPLETE |
| Numeric: support | 109 | COMPLETE |
| Numeric total | 298 | COMPLETE |
| Statistical: main A and PLAN | 112 | PASS_1_COMPLETE and PASS_2_COMPLETE |
| Statistical: main graphical relationships | 60 | PASS_1_COMPLETE and PASS_2_COMPLETE |
| Statistical: support baseline, graph and methods | 83 | PASS_1_COMPLETE and PASS_2_COMPLETE |
| Statistical: support outcome tuples and methods | 69 | PASS_1_COMPLETE and PASS_2_COMPLETE |
| Statistical total | 324 | Both passes complete for every relationship |
| Cross-source matched comparisons | 120 | COMPLETE |

The canonical [numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md) and [statistical inventory](review_1_6_1/statistics/relationship_inventory.md) preserve individual relationships. Both statistical passes used distinct fresh high-effort agents and disjoint context-bounded shards. Pass 2 reconsidered the complete inventory after registration, independent screening and mechanical recheck, and emitted no new finding. The support scope includes 34 arm-marginal intervals added when checking identified that the initial tuple summary counted only differences; all received both passes. Approximate graphical readings remain approximate.

Checks addressed count accounting and display intervals, estimate containment and endpoint order, direction and reference scales, matched analysis populations and quantities, supplied model specifications, and prospective analysis and decision rules. Exact estimate/CI/P compatibility was limited wherever the package does not identify the common test construction, variance estimator or other necessary input. No assumed model output, test or graphical coordinate replaced a supplied result.

## Inclusion Screening Summary

A finding qualifies only when reproduced from supplied sources, within the quantitative focus, unresolved by immediate context for a statistically literate reader, and relevant to a named result's interpretation or extraction. Independent screening covered all **3 emitted findings** in the single [screening log](review_1_6_1/screening/inclusion_screen.md).

| Decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 2 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 1 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| Total | All screening decisions | 3 |

F-ST1-001 maps to C001 and F-XS-001 maps to C002. F-ST1-002 is SCREENED_OUT/DUPLICATE_OF_INCLUDED, retains its connection to C002 and contributes its contextual location and provenance. It has no separate card. Numeric review emitted zero findings, cross-source review one, statistical pass 1 two, and pass 2 zero. A second inclusion-screen stage was therefore not applicable. The audit retained all decisions, with no audit-stage new finding or screening reversal.

Checker exclusions are a separate audit count, not additional rows in the emitted-finding screening log: numeric 28, cross-source 18, statistical pass 1 34 and statistical pass 2 37, totaling 117. Every row was audited against the inclusion threshold; none was promoted to a new candidate.

## Review-Domain Summary

| Review domain | Definition | Candidates |
|---|---|---:|
| statistical_results | Counts, estimates, intervals, tests or statistical-method logic in REPORT material | 1 |
| report_internal_inconsistency | Conflicting REPORT attribution of a number to an outcome, time point, analysis set or comparison | 0 |
| protocol_report | REPORT versus PLAN statistical-design or analysis specification | 1 |
| plan_material | PLAN-internal statistical-design inconsistency relied upon by the reported analysis | 0 |
| Total | Stable ledger candidates | 2 |

| Relationship type | Meaning | Candidates |
|---|---|---:|
| S_W | Within one REPORT document | 1 |
| S_C | Between REPORT documents | 0 |
| P_R | REPORT versus PLAN | 1 |
| P_P | Within PLAN material | 0 |
| Total | Primary relationship types | 2 |

| Evidence state | Candidates |
|---|---:|
| reproduced | 2 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 2 |

The inclusion audit records CONFIRMED for 2 candidates and QUESTIONED for 0. All relationships in each candidate are its sole primary relationship, so precedence is unambiguous. These classifications prefill human review and are not human adjudications.

## Candidate Index

| Stable ID | Candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#C001) | Identification of adjusted time-effect outputs | statistical_results | S_W | reproduced | CONFIRMED |
| [C002](#C002) | Planned and reported age-subgroup specification | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Identification of the adjusted time-effect outputs

**Status:** Pending Human Adjudication


**Candidate statement:** Table 2 gives two adjusted time-effect outputs for each of door-to-balloon and door-to-needle time, without identifying the separate analysis targets that produced its difference and beta-coefficient columns.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 time rows and footnotes vs REPORT main article Statistical Analysis

**Finding IDs:** F-ST1-001

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Mechanical evidence recheck:** Every cited and contextual page was found and source-confirmed; printed inputs, half-unit display bounds and the method-identification comparison were reproduced without a transcription or classification change. See [complete recheck facts](review_1_6_1/verification/evidence_recheck.md).

**Checker provenance:** Fresh statistical pass 1 main/PLAN shard; independently included by root/screen_initial.

**Classification rationale:** All conflicting method/output descriptions are in the main REPORT. The issue concerns statistical-method identification and the quantity extracted. No PLAN location is a conflicting comparator.

**Classification ambiguity:** The two outputs may intentionally target distinct conditional, marginal, transformed, or otherwise defined quantities; the supplied descriptions do not identify the mapping. No equality of those quantities is assumed.

**Exact source locations:** All main locations are REPORT in jama_huffman_2018_oi_170166.pdf: [physical p. 6, Table 2 door-to-balloon row](../jama_huffman_2018_oi_170166.pdf#page=6); [physical p. 6, Table 2 door-to-needle row](../jama_huffman_2018_oi_170166.pdf#page=6); [physical p. 6, Table 2 title and both effect headers](../jama_huffman_2018_oi_170166.pdf#page=6); [physical p. 6, Table 2 footnotes a/b/c](../jama_huffman_2018_oi_170166.pdf#page=6); and [physical p. 3, Statistical Analysis](../jama_huffman_2018_oi_170166.pdf#page=3). Context is [physical p. 6, paragraph below Table 2](../jama_huffman_2018_oi_170166.pdf#page=6) and [physical p. 7, process narrative](../jama_huffman_2018_oi_170166.pdf#page=7). Physical pp. 3, 6 and 7 are printed pp. 569, 572 and 573.

**Source evidence:** Door-to-balloon medians are control 65 (53–105) min, n=4022, and intervention 77 (55–118) min, n=3639. Difference: 6.18 (95% CI −4.78 to 17.14); beta coefficient: 13.00 (3.64–22.36). Door-to-needle medians are 44 (30–67) min, n=1455, and 45 (27–75) min, n=1433. Difference: 0.40 (−5.23 to 6.03); beta coefficient: 5.00 (−5.20–15.20). Both outputs cite the common footnote describing marginal effects and mixed-effects logistic or quantile regression with clustering and temporal trends; footnote c identifies beta coefficients.

**Reported-versus-comparator:** Two distinct effect columns share an adjustment description without a separate time-result model/target mapping. Their distinct values are an observation; neither is asserted to fail arithmetic or its own interval rule.

**Footnote precision:** Both effect headers cite footnote b, but its grammatical subject is the ORs and beta coefficients. It names marginal-effects differences and mixed-effects logistic or quantile regression; it does not separately identify the time Difference column's target. Inclusion does not assume that a conditional coefficient must equal a marginal contrast.

**Reasoning procedure:** Identify the outcome, units, population, contrast, model labels and both reported outputs. Apply display-precision bounds and distinguish a source-grounded method-identification gap from the immediately resolvable percent header. Do not compare modeled effects with crude median differences as an identity test.

**Calculation:** Balloon point bounds [6.175,6.185] and [12.995,13.005] are disjoint; point difference 6.82. Needle bounds [0.395,0.405] and [4.995,5.005] are disjoint; point difference 4.60. Balloon's first CI spans zero, while beta lower-bound display interval [3.635,3.645] excludes zero. These calculations establish different outputs and inferential readings, without asserting they must be equal.

**Affected result or extracted value:** The adjusted intervention time effects, especially balloon 6.18 (−4.78,17.14) versus 13.00 (3.64,22.36), and the analysis quantity to which each belongs.

**Why context does not resolve it:** The column names identify two outputs but the common method text does not map their models, quantiles, standardization targets or reference populations. The minute units are readily identifiable; the adjusted quantity to extract remains unclear.

**Alternative source-grounded interpretations:** An intentionally distinct marginal time contrast and conditional quantile coefficient, or different transformed/model targets, could explain the two columns. The package does not establish which explanation applies. Missing definitions: column-specific model, target, quantile/scale, reference population, and interval construction.

**Potential downstream evidence impact:** An extractor could select a different adjusted time estimate and interval, including a different zero-inclusion reading, if the analysis target is not clarified. No downstream propagation or paper-level conclusion change is asserted.

**Human verification steps:** Read the two rows and footnotes together with the statistical methods, identify the model and estimand for each column, and establish which adjusted time quantity each reported estimate represents.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Planned and reported age-subgroup specification

**Status:** Pending Human Adjudication


**Candidate statement:** The supplied SAP specifies an age split at 65 for the primary-endpoint subgroup analysis, while the report calls age groups split at 50 and 70 prespecified.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP section 7.5.2 vs REPORT main article Methods and Figure 3 age subgroups

**Finding IDs:** F-XS-001

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Mechanical evidence recheck:** All PLAN and REPORT locations, including contextual main p. 2, were found and visually source-confirmed. Cutoffs, effect rows and arm/event sums reproduce; no transcription or classification change was needed. See [complete recheck facts](review_1_6_1/verification/evidence_recheck.md).

**Checker provenance:** F-XS-001 from the fresh cross-source checker and F-ST1-002 from the independent statistical checker describe one issue. The screen includes F-XS-001 and links the duplicate F-ST1-002 to C002. All locations from both findings are retained.

**Classification rationale:** Prospective SAP content is PLAN; the main results are REPORT. Their age analysis specifications differ. Consistent report repetitions and the SAP-referencing statement are context, not additional S_W relationships.

**Classification ambiguity:** A later prospective amendment may not be supplied. This limits attribution of the specification change, not the observed printed comparison.

**Exact source locations:** PLAN joi170166supp2_prod.pdf: [physical p. 7, section 7.5.2, lines 1243–1254, especially line 1251](../joi170166supp2_prod.pdf#page=7), with adjacent primary-analysis context in [physical p. 7, section 7.5, lines 1229–1238](../joi170166supp2_prod.pdf#page=7). REPORT jama_huffman_2018_oi_170166.pdf: [physical p. 3, Statistical Analysis subgroup sentence](../jama_huffman_2018_oi_170166.pdf#page=3); [physical p. 9, Figure 3 title and age <50 row](../jama_huffman_2018_oi_170166.pdf#page=9); [physical p. 9, age 50–69 row](../jama_huffman_2018_oi_170166.pdf#page=9); [physical p. 9, age ≥70 row](../jama_huffman_2018_oi_170166.pdf#page=9); and [physical p. 9, adjacent subgroup paragraph](../jama_huffman_2018_oi_170166.pdf#page=9). Contextual REPORT locations are [physical p. 2, Study Design SAP reference](../jama_huffman_2018_oi_170166.pdf#page=2) and [physical p. 7, Table 3 aggregate MACE counts](../jama_huffman_2018_oi_170166.pdf#page=7). Main physical pp. 2, 3, 7 and 9 are printed pp. 568, 569, 573 and 575.

**Source evidence:** SAP a priori age groups: <65 and >65 years. Reported prespecified groups: <50, 50–69 and ≥70 years. Respective adjusted MACE ORs: 1.53 (0.83–2.79), 0.89 (0.67–1.19), 0.98 (0.71–1.35); adjusted differences: 1.42% (−0.71 to 3.54), −0.57% (−2.02 to 0.88), −0.23% (−3.32 to 2.85). Intervention event/denominators: 58/2079, 297/6606, 247/2623; control: 68/2045, 326/5863, 251/2158.

**Reported-versus-comparator:** The three reported categories cannot be matched to the SAP's two planned categories by variable name alone. The report confirms prespecification without identifying a revised specification in those locations.

**Reasoning procedure:** Match primary 30-day MACE, analysis population, model and age subgroup family. Compare group membership boundaries, not the preferred clinical cutoff. Preserve the possibility of a later amendment without assuming one exists.

**Calculation:** Intervention denominators 2079+6606+2623=11308 and events 58+297+247=602; control denominators 2045+5863+2158=10066 and events 68+326+251=645. The reported middle age group crosses 65, so no merging of the displayed categories recovers the planned split. Uncertainty about age exactly 65 and numeric display precision do not reconcile cutoffs at 50 and 70. Adjusted ORs/RDs cannot be remapped by averaging the displayed effects.

**Affected result or extracted value:** The three age-specific adjusted primary MACE effects and their interpretation as prespecified analyses, compared with effects for the planned split at 65.

**Why context does not resolve it:** The displayed age groups are clear, but neither the adjacent report statements nor the supplied SAP explains how those groups relate to the a priori split. Different category membership is not a field-specific synonym.

**Alternative source-grounded interpretations:** An additional prospective amendment could define the reported groups; an additional analysis may have been displayed; or the planned split may have been performed separately. The supplied evidence does not identify which applies.

**Potential downstream evidence impact:** A reviewer could extract the three reported age effects as the planned age-specific effects even though they do not represent the SAP split. No conclusion change or downstream propagation is asserted.

**Human verification steps:** Confirm the boundaries and all age effects directly, identify any later prospective specification, and establish how the reported analysis relates to the SAP age split.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Data extraction depends on identifying the outcome, population, analysis target, model, contrast, units and prospective status that belong to a reported value. If a candidate is confirmed by human review, an unresolved distinction could affect which estimate and interval are copied or how a subgroup analysis is described in evidence synthesis. These are possible extraction consequences. The supplied package does not establish downstream propagation, a changed overall conclusion or harm.

For C001, the relevant link is between an adjusted time estimate and its target definition; for C002, it is between the reported age-specific MACE effects and their prospective specification. Human clarification should precede treating either pair of distinct quantities or category schemes as interchangeable.

## Limitations and Missing Definitions

All source pages and registered relationships are covered. Remaining limits concern definitions and unprinted inputs, as recorded in [limitations.md](review_1_6_1/limitations.md).

The figures lack exact printed coordinates for every point and interval, so graphical checks establish visible order, containment, direction and labels without inventing exact coordinates or counts. The package does not fully supply CI/test construction, variance/covariance estimators, degrees of freedom, row-specific model contributor counts, missing-outcome coding, imputation details or the full stepped-wedge power implementation. Their absence limits exact reconstruction and does not independently establish another reporting issue.

C001 needs a column-specific model and estimand, relevant quantile or scale, standardization/reference population and interval construction to identify the two adjusted time outputs. C002 needs a dated prospective specification or disclosed amendment linking the reported age categories to the supplied SAP, including whether the planned split was additionally performed or replaced. A later specification may exist outside the supplied package; its absence here does not establish that none existed. The convention for exactly age 65 does not reconcile the observed category schemes.

CPU OCR and Office conversion were unavailable locally. Existing source-matched OCR and visual inspection completed the scanned-page scope; the package contains no direct Office source. No unresolved scientific inspection gap remains. Review is restricted to supplied package evidence and does not reconstruct unrecorded runtime actions or downstream use.

## Human Adjudication Checklist

1. Read every cited source page, including all affected rows and immediate footnotes or paragraphs.
2. Confirm the source role, analysis population, endpoint, time point, contrast, quantity and precision relevant to each card.
3. For C001, identify the target and model for each adjusted time output without imposing equality between distinct conditional and marginal quantities.
4. For C002, identify the dated prospective age specification and establish its relationship to the displayed MACE subgroup analyses.
5. Consider the source-grounded alternatives and missing definitions, then fill Validity, Importance, Action, Initials and Notes independently for each candidate.

Both cards remain **Pending Human Adjudication** until a human completes that review.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Reproducibility and source integrity

Workflow controls are the supplied [scope](../QUALITY_CONTROL_SCOPE.md), [review contract](../workflow_1_6_1/review_contract.md), [report specification](../workflow_1_6_1/report_spec.md), [performance profile](../PERFORMANCE_PROFILE.md) and [settings](../workflow_1_6_1/settings.toml). Current scientific artifacts are linked in the preceding sections; the complete [mechanical recheck](review_1_6_1/verification/evidence_recheck.md) and [quality audit](review_1_6_1/quality/evidence_quality_audit.md) preserve the evidence facts and independent threshold audit for C001 and C002.

Direct-source SHA-256 values are:

| Actual filename | SHA-256 |
|---|---|
| jama_huffman_2018_oi_170166.pdf | 11311a6bb5c7a4be734ed60776b308f525ad101671ccc8d34bab18735aaca5f5 |
| joi170166supp1_prod.pdf | 0e13bdfc6e5e3c8b86e187f54f0a3d7d0217fc0614be9fbdbbb7839dbab9004a |
| joi170166supp2_prod.pdf | d49019c3cf6ee0766fb319f254f27f87751a73bfec66c34d38bae16a956bb1c6 |
| joi170166supp3_prod.pdf | 511f4a907e4c48d920f1c6b89d444fe76c7c91e11bbae84cdee834fa0393f3ec |

The audit's read-only source and reused-asset hash comparisons all matched. The coordinator recomputes both sets at closure and performs local rendering and validation after timing finalization; this assembly does not claim those later checks have already completed.

The [tooling record](review_1_6_1/tooling_record.md) records Linux, direct pdfinfo/pdftotext/pdftoppm/pdftocairo availability and missing tesseract/libreoffice. Poppler PDF information, text and rendering tools were version 25.03.0; Pandoc was 3.1.11.1. Fresh protocol-diagram rendering used 150 dpi; targeted source-confirmation renders used 120 dpi. Existing images retain their historical engine metadata. No fallback environment was needed or created, and no new OCR or GPU operation was used.

### Agent execution

Routing preflight records PASS, coordinator inference PASS, execution mode INTERACTIVE_CLI, Provider CURRENT_SESSION and verification of all ten fixed role presets. Every actual runtime agent, including the coordinator, continuation shards and this report generator, appears below with the exact fixed model and effort. The coordinator used CURRENT_SESSION; every specialist used FRESH_SPAWN. The statistical passes have distinct agent identities. No conditional pass-2 screener was needed because pass 2 emitted no finding. Primary artifact paths are relative to review_1_6_1/; the full durable assignment record is the [execution manifest](review_1_6_1/agent_execution_manifest.md).

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_main_a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_continuation_main_b | root/numeric_main_b | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_main_b.md |
| numeric_continuation_support | root/numeric_support | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| cross_source_consistency_reviewer | root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_1_main_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support | root/statistics_1_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support.md |
| statistics_pass_1_main_b | root/statistics_1_main_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_main_b.md |
| statistics_pass_1_support_outcomes | root/statistics_1_outcomes | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support_outcomes.md |
| inclusion_screener | root/screen_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/recheck_initial | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_2_main_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_main_b | root/statistics_2_main_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_main_b_pass_2.md |
| statistics_pass_2_support | root/statistics_2_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support_pass_2.md |
| statistics_pass_2_support_outcomes | root/statistics_2_outcomes | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support_outcomes_pass_2.md |
| quality_control_auditor | root/audit_candidates | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_coverage_provenance_auditor | root/audit_coverage | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_provenance_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

- **Target basis:** Four PDF sources contain 80 unique pages, all initially backed by reusable extraction or images, with one embedded protocol diagram subsequently requiring fresh rendering and no Office conversion. Fourteen scanned toolkit pages use existing source-matched OCR and images, and complex flow/figure pages require visual reading. Complete discovery and statistical relationships are rebuilt through parallel main/support mapping and checker waves, followed by independent screening, recheck, a second statistical pass, audit, and report generation; the required sequential agent waves remain the principal latency burden.
- **Total source units:** 80
- **Fresh-source units:** 1
- **Target elapsed minutes:** 22-35
- **Started UTC:** 2026-10-11T02:52:35Z
- **Finished UTC:** 2026-10-11T03:29:13Z
- **Observed elapsed minutes:** 36.63
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Additional context-bounded numeric, statistical and audit shards for complete scope; 34 supplementary arm-marginal intervals added during completeness checking; sequential independent screening, recheck, second-pass and audit stages

The package-specific planning target reflects reusable evidence, one fresh diagram, scanned and graphical content, the complete relationship volume and required sequential review waves. Timing is finalized by the coordinator immediately after complete Markdown assembly. Local HTML rendering and mechanical validation remain outside the observed review duration; any later model-assisted repair requires updated finish and performance fields.
