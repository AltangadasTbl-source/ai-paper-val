# Quantitative Reporting Quality-Control Consistency Review — HIGH-WEAN

**Pending Human Adjudication**

This report records quantitative consistency candidates for the supplied JAMA paper package (jama.2019.14901). Evidence states and suggested review dispositions describe the evidence record and mechanically pre-fill human review. They do not decide validity, importance, or correction. Small preventable reporting defects can matter for downstream evidence extraction; this review establishes neither actual propagation nor a change in the paper's conclusion.

# Executive Quality-Control Summary

Complete review of four supplied PDFs and all 69 physical pages produced **32 stable candidates, C001–C032**. Every candidate appears in the index and in a complete evidence card below. Direct printed differences, conditional rounding or inferential diagnostics, and comparisons whose alignment was disproven or remains unsupported are distinguished in their cards.

The direct-source recheck records 29 `recorded_candidate`, one `not_reproduced` (C013), and two `record_input_error` (C019 and C028). Mechanical suggestions are respectively 29 `retain`, one `exclude`, and two `discuss`; every candidate remains Pending Human Adjudication. These counts describe the registered record, not 32 established defects.

Examples of observable printed differences include complementary percentages in four hypercapnic cough/secretion cells, respiratory-failure estimates across main-article locations, duration contrasts under a percent-unit heading, and conflicting survival time-origin labels. Several smaller discrepancies depend on unspecified rounding, estimator, test, denominator, or implementation conventions. C013 has an explicit coherent two-stage rounding calculation. C019 cannot establish a pooled-variance discrepancy without measured sample sizes. C028 compares statistical objects that need not yield the same P value.

# Package and Reused-Evidence Provenance

| Source ID | Supplied source and entry page | Content role | Physical pages |
|---|---|---|---:|
| DOC-001 | [jama_thille_2019_oi_190108.pdf](../jama_thille_2019_oi_190108.pdf#page=1) | REPORT: main randomized-trial article | 11 |
| DOC-002 | [joi190108supp1_prod.pdf](../joi190108supp1_prod.pdf#page=1) | PLAN: protocol version 4, 17 October 2017, including historical background and operational appendices | 48 |
| DOC-003 | [joi190108supp2_prod.pdf](../joi190108supp2_prod.pdf#page=1) | REPORT: non-plan results eTables and survival eFigure | 9 |
| DOC-004 | [joi190108supp3_prod.pdf](../joi190108supp3_prod.pdf#page=1) | REPORT: administrative data-sharing statement | 1 |

No supplied Office, workbook, or CSV source exists. Roles are assigned by content; historical numerical summaries in the protocol remain PLAN material. Physical PDF pages govern the evidence links, including the protocol's inconsistent printed footer page totals.

The [source inventory](review_1_6/source_inventory.md), [asset inventory](review_1_6/evidence_asset_inventory.md), and [before-source hashes](review_1_6/source_hashes_before.sha256) establish provenance. There are 128 hashed reused extraction, image, metadata, and map assets: 99 USABLE, 28 PARTIAL, and one DUPLICATE. All 69 native/layout page records were source-matched against direct Poppler extraction. Partial legacy maps and prior scope exclusions did not define fresh scientific coverage. Old candidates, classifications, decisions, and final reports were preserved and were not scientific inputs.

Reusable text and images served as locators and transcription aids. Candidate rechecking used exact supplied-source layout text and targeted visual confirmation. Fresh rendering of [protocol physical page 42](../joi190108supp1_prod.pdf#page=42) recovered the embedded weaning worksheet omitted from its otherwise matching text layer. The [fresh derivative](review_1_6/preprocessing/support_mapping/protocol-p42.png) is provenance; the supplied PDF remains the evidence authority.

# Scope, Complete Coverage, and Exclusions

| Source | Total pages | Reusable pages | Fresh-required pages | Mapped pages | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | 48 | 47 | 1 | 48 | COMPLETE |
| DOC-003 | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-004 | 1 | 1 | 0 | 1 | COMPLETE |
| **Total** | **69** | **68** | **1** | **69** | **COMPLETE** |

The partition is 68 + 1 = 69, and mapped units equal total units for every source. Coverage includes covers, administrative material, references, plan background, all article tables/figures, all results eTables, and the survival figure. The data-sharing statement contains no applicable quantitative outcome but is mapped and classified. The [source-coverage ledger](review_1_6/source_coverage.md) and [coverage manifest](review_1_6/coverage_manifest.md) record the complete assignments.

Scope is numeric, denominator/proportion/total, inferential-statistical, matched cross-location/cross-document, effect-measure/label/scale, and rate-versus-count consistency. Analysis-unit or population questions qualify only through a concrete quantitative relationship. This is not a broad design, clinical, novelty, misconduct, or raw-data audit. No external literature or web evidence was used. Coherent finite-precision display zeros alone do not generate candidates; none of the stable cards depends on one.

# Quantitative and Statistical Relationship Coverage

Fresh mapping covers [the complete main article](review_1_6/extraction/main_quantitative_evidence.md), [the full protocol and administrative statement](review_1_6/extraction/support_quantitative_evidence.md), and [the complete results supplement](review_1_6/extraction/support_results_quantitative_evidence.md). The [numeric inventory](review_1_6/relationships/numeric_relationship_inventory.md) contains N001–N140 and numeric components of S001–S137: 277 checked groups. Four bounded numeric parts contain 109, 54, 109, and five groups. These include totals, stratum partitions, explicit measured denominators, all 30 center cells, rounded continuous moments, composite-event identities, and all 16 plotted risk-count additions.

The [statistical inventory](review_1_6/statistics/relationship_inventory.md) has 137 registered groups. Both [pass 1](review_1_6/checkers/statistical_pass_1.md) and [pass 2](review_1_6/checkers/statistical_pass_2.md) cover every group, including grouped subcomparisons: 137 PASS_1_COMPLETE and 137 PASS_2_COMPLETE records. Distinct fresh high-effort runtimes were `root/statistical_pass_1` and `root/statistical_pass_2`; each processed sequential 43-group and 94-group scopes. Pass 2 also read every cross-lane candidate and direct-source recheck fact; it added no new candidate.

Checks included effect containment and interval ordering, direction, test/interval/statistic compatibility where compatible definitions exist, arithmetic and denominator alignment, repeated results, scale/unit identity, and test/time-origin distinctions. No interval endpoint-order or point-containment candidate was found. Survival risk-table attrition was not treated as event counts, medians were not treated as mean estimators, and count proportions were not treated as person-time rates. Conditional standard-test calculations are diagnostic and do not supply unreported model definitions.

The [ledger](review_1_6/candidate_ledger.md) preserves genuine duplicate reconciliation and checker provenance. The [mechanical recheck](review_1_6/verification/evidence_recheck.md) records every input, source location, comparison condition, calculation, missing definition, alternative, and human question. The [quality audit](review_1_6/quality/evidence_quality_audit.md) assessed all 32 IDs and complete scientific coverage before report generation. It does not claim that this subsequently generated final report had already been audited.

# Document-Role Classification Summary

`S_W` means a discrepancy within one REPORT; `S_C` means between different REPORT documents; `P_R` means between REPORT and PLAN content; and `P_P` means solely within PLAN material. Mixed substantive relationships would use precedence P_R > P_P > S_C > S_W. Each registered candidate here has one substantive relationship; corroborative sources do not add a discrepancy relationship.

| Relationship type | Count |
|---|---:|
| S_W | 19 |
| S_C | 6 |
| P_R | 4 |
| P_P | 3 |
| **Total** | **32** |

| Derived review domain | Count |
|---|---:|
| statistical_results | 19 |
| report_internal_inconsistency | 6 |
| protocol_report | 4 |
| plan_material | 3 |
| **Total** | **32** |

| Evidence state | Count | Mechanical suggested review disposition |
|---|---:|---|
| recorded_candidate | 29 | retain |
| not_reproduced | 1 | exclude |
| record_input_error | 2 | discuss |
| repaired_residual | 0 | retain |
| **Total** | **32** | **29 retain; 1 exclude; 2 discuss** |

Review domains derive from relationship type and primary category under the supplied scope. Suggested review dispositions derive only from evidence state. They are mechanical pre-fills, never adjudications. The exact classification-table values are copied into every card, including the ledger's source-location wording.

# Candidate Index

