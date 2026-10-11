# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.1

**Pending Human Adjudication.** All candidates require human review. The classifications and evidence states below organize the quantitative reporting checks; they do not adjudicate validity, importance, or action.

## Executive Quality-Control Summary

The complete supplied package yielded **1 stable candidate, C001**, consolidating two independently screened findings about the same binary-effect definition. Eight Table 2 risk-ratio rows do not reconcile with their adjacent intervention event fractions under conservative display-precision bounds. Two additional rows and four abstract repetitions are retained with their precise evidential qualifications. The candidate concerns the quantity and confidence interval a reader could extract as an intervention effect; a particular computational mechanism is not established.

All **94 PDF pages across 5 direct sources** were mapped: 86 had usable reusable evidence and 8 required fresh direct-source coverage. Numeric review covered 112 grouped relationships. Two fresh statistical specialists each completed all 64 statistical relationships, including every supplemental result comparison. Independent screening included both emitted findings as one issue, and the quality audit recorded CONFIRMED for inclusion of C001. No change in the primary conclusion or the secondary nonsignificance statements is established. The complete stable candidate is presented for human adjudication.

## Package and Reused-Evidence Provenance

The package contains the main PReVENT randomized-trial article comparing low and intermediate tidal-volume ventilation in ICU patients without ARDS, a protocol, an updated statistical analysis plan (SAP), a results supplement, and a data-sharing statement. Document roles were assigned by content. The protocol and SAP remain PLAN material even though supplied as supplements.

| Source ID | Actual filename | Content role | Complete PDF pages |
|---|---|---|---:|
| DOC-001 | [jama_simonis_2018_oi_180108.pdf](<../jama_simonis_2018_oi_180108.pdf#page=1>) | REPORT — main article | 9 |
| DOC-002 | [joi180108supp1_prod.pdf](<../joi180108supp1_prod.pdf#page=1>) | PLAN — protocol version 3.2 | 49 |
| DOC-003 | [joi180108supp2_prod.pdf](<../joi180108supp2_prod.pdf#page=1>) | PLAN — updated SAP version 1.0 and modification table | 22 |
| DOC-004 | [joi180108supp3_prod.pdf](<../joi180108supp3_prod.pdf#page=1>) | REPORT — results supplement | 13 |
| DOC-005 | [joi180108supp4_prod.pdf](<../joi180108supp4_prod.pdf#page=1>) | REPORT — retrospective data-sharing statement | 1 |

The [source inventory](review_1_6_1/source_inventory.md) records exact units and source SHA-256 values. The [evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md) records 66 preserved derivatives: 5 native text files, 5 layout text files, and 56 page images from review_1_5_2/preprocessing. No reusable OCR, structured table extraction, workbook extraction, or document map was available. Nine text derivatives matched current extraction byte for byte; the main layout text had a page-7 axis-label placement difference resolved by source-matched native text and its page image. Partial text omitted raster content, which was covered by reusable images or fresh rendering. Original derivative engine versions are undocumented; fresh extraction and rendering used direct Poppler 25.03.0.

Discovery and classification were rebuilt from source-linked assets and complete new maps. Earlier candidate selections, screening decisions, classifications, and reports were preserved and were not scientific inputs. Supplied PDFs remained authoritative for candidate confirmation.

## Scope, Complete Coverage, and Exclusions

The review followed [QUALITY_CONTROL_SCOPE.md](../QUALITY_CONTROL_SCOPE.md), focusing on counts and denominators, estimate and test logic, statistical method logic, and planned versus reported statistical design. Every source unit was assigned and mapped, including covers, references, historical material, table shells, and administrative pages with explicit no-applicable-content records.

| Source ID | Unit type | Total | Reusable | Fresh-required | Mapped | Status |
|---|---|---:|---:|---:|---:|---|
| DOC-001 | PDF_PAGE | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 | PDF_PAGE | 49 | 41 | 8 | 49 | COMPLETE |
| DOC-003 | PDF_PAGE | 22 | 22 | 0 | 22 | COMPLETE |
| DOC-004 | PDF_PAGE | 13 | 13 | 0 | 13 | COMPLETE |
| DOC-005 | PDF_PAGE | 1 | 1 | 0 | 1 | COMPLETE |
| **Total** | | **94** | **86** | **8** | **94** | **COMPLETE** |

The eight fresh-required protocol pages were PDF pages 12, 13, 14, 36, 39, 40, 41, and 42. Direct native/layout extraction and rendered-page visual inspection closed their raster gaps. The [main map](review_1_6_1/extraction/main_quantitative_evidence.md) covers 9 pages; the [support map](review_1_6_1/extraction/support_quantitative_evidence.md) covers 85 pages. The [source-coverage ledger](review_1_6_1/source_coverage.md) and [coverage manifest](review_1_6_1/coverage_manifest.md) retain page and stage assignments. No scientific source-unit coverage gap remains.

Observations were excluded when they reconciled, were within display precision, were immediately resolved by notation, terminology or context, compared established modeled effects with crude quantities, depended on unsupplied assumptions, were peripheral, or fell outside the four focus areas. Cross-document comparisons retained primary and key secondary results and statistical design elements while applying the scope's peripheral-comparison rule. General clinical, methodology, novelty, misconduct, and raw-data audits were outside this review.

## Quantitative and Statistical Relationship Coverage

The [numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md) contains 112 canonical groups, N001–N112, retaining every constituent printed cell. Main and support mapper keys are provenance locators; the canonical IDs define checker coverage. The [statistical inventory](review_1_6_1/statistics/relationship_inventory.md) contains 64 groups, S001–S035 and S101–S129, each explicitly marked PASS_1_COMPLETE and PASS_2_COMPLETE.

| Coverage component | Complete scope |
|---|---:|
| Numeric/reporting relationship groups reviewed | 112 of 112 |
| Statistical groups reviewed in fresh pass 1 | 64 of 64 |
| Statistical groups reviewed in different fresh pass 2 | 64 of 64 |
| eTable 1 paired comparisons | 48 of 48 |
| eTable 2 paired comparisons | 72 of 72 |
| eTable 3 paired comparisons | 72 of 72 |
| eTable 4 paired comparisons | 30 of 30 |
| eTable 5 paired comparisons | 16 of 16 |
| Total supplemental paired comparisons | 238 of 238 |
| Additional subgroup interaction P values | 8 of 8 |
| Additional graphical P values | 9 of 9 |

Checks covered participant flow, outcome-specific fractions, totals, percentages, mean differences, interval ordering and containment, effect direction and identity, matched abstract/table/figure results, stated model and test logic, analysis populations, missingness, sample-size inputs, and the complete original/current/paper/post-hoc SAP bridge. Noninferiority, equivalence, and numerical efficacy stopping calculations were not applicable to the supplied design. Unreported statistics, event times, covariance, model links, and denominator definitions were not inferred.

The [numeric checker](review_1_6_1/checkers/numeric_consistency.md) emitted F-NUM-001 and recorded 22 excluded observations. The [cross-source checker](review_1_6_1/checkers/cross_source_consistency.md) emitted no findings and recorded 25 exclusions. [Statistical pass 1](review_1_6_1/checkers/statistical_pass_1.md) emitted F-ST1-001 and recorded 18 exclusions. [Statistical pass 2](review_1_6_1/checkers/statistical_pass_2.md), conducted after registration and recheck, revisited C001 and every relationship, emitted no new findings, and recorded 22 exclusions. The independent [quality audit](review_1_6_1/quality/evidence_quality_audit.md) assessed all 87 checker exclusions and both screening decisions, with no screening changes or additional findings.

## Inclusion Screening Summary

A fresh independent screener reread every finding's cited source locations. Inclusion required reproduction from supplied evidence, a qualifying focus/domain, an inconsistency not resolved at once by immediate context, and a plausible effect on interpretation or extraction of a named result. The single [screening log](review_1_6_1/screening/inclusion_screen.md) contains exactly two finding rows.

| Decision | Reason code | Finding rows |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 2 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 0 |
| **Total finding rows screened** | | **2** |

Included findings: 2. Screened-out findings: 0. Consolidated included issues and stable candidates: 1. F-NUM-001 and F-ST1-001 independently describe the same pattern and both map to C001. The 87 checker exclusions are separate self-screening records, not additional finding rows in this table. Statistical pass 2 emitted no findings, so a pass-2 screening stage was not required. Inclusion audit counts are CONFIRMED 1 and QUESTIONED 0.

## Review-Domain Summary

The four domains organize the nature of the comparison: `statistical_results` covers counts, estimates, intervals, tests and statistical methods in reports; `report_internal_inconsistency` covers conflicting report attribution of results; `protocol_report` covers report-versus-plan statistical design differences; and `plan_material` covers plan-internal statistical design inconsistencies relevant to the reported analysis.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 1 |
| report_internal_inconsistency | 0 |
| protocol_report | 0 |
| plan_material | 0 |
| **Total** | **1** |

| Primary relationship type | Stable candidates |
|---|---:|
| S_W — within one REPORT | 1 |
| S_C — between REPORT documents | 0 |
| P_R — REPORT versus PLAN | 0 |
| P_P — within PLAN material | 0 |
| **Total** | **1** |

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 1 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **1** |

Each summary counts candidates once and reconciles to the ledger's one stable ID. The SAP corroborates the effect label in C001 and does not add a conflicting PLAN relationship.

## Candidate Index

| Stable ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#c001--binary-risk-ratio-definition-does-not-reconcile-with-the-displayed-intervention-event-fractions) | Binary RR definition and intervention event fractions | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Binary risk-ratio definition does not reconcile with the displayed intervention event fractions

**Status:** Pending Human Adjudication

**Candidate statement:** The repeated binary risk ratios and intervals in Table 2 and the abstract do not identify the same intervention event-risk quantity as the printed low-versus-intermediate event fractions. Eight rows remain discrepant under conservative display-precision intervals; two near-null rows are corroborating occurrences only. An alternative conditional ratio tracks the printed family, but the supplied materials do not define that quantity as the reported intervention effect.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 2 and footnote c vs REPORT main article Statistical Analysis and abstract
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-001, F-ST1-001
**Classification rationale:** The conflicting effect label, fractions and displayed estimates occur inside the main REPORT. The PLAN SAP corroborates the intended RR label and is not a conflicting comparator, so no P_R relationship is added. One repeated effect-definition pattern is registered with all occurrences.
**Classification ambiguity:** None

**Exact source locations:**

| Role | Exact affected or supporting location | Evidence link |
|---|---|---|
| REPORT | Table 2, ICU mortality | [jama_simonis_2018_oi_180108.pdf — PDF p. 6](../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, hospital mortality | [jama_simonis_2018_oi_180108.pdf — PDF p. 6](../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, development of ARDS | [jama_simonis_2018_oi_180108.pdf — PDF p. 6](../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, development of pneumonia | [jama_simonis_2018_oi_180108.pdf — PDF p. 6](../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, pneumothorax | [jama_simonis_2018_oi_180108.pdf — PDF p. 6](../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, atelectasis; corroborating under the conservative count test | [jama_simonis_2018_oi_180108.pdf — PDF p. 6](../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, extrapulmonary infection | [jama_simonis_2018_oi_180108.pdf — PDF p. 6](../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, extrapulmonary sepsis | [jama_simonis_2018_oi_180108.pdf — PDF p. 6](../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, delirium | [jama_simonis_2018_oi_180108.pdf — PDF p. 6](../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Table 2, need for tracheostomy; corroborating under the conservative count test | [jama_simonis_2018_oi_180108.pdf — PDF p. 6](../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Abstract Results, ARDS | [jama_simonis_2018_oi_180108.pdf — PDF p. 1](../jama_simonis_2018_oi_180108.pdf#page=1) |
| REPORT | Abstract Results, pneumonia | [jama_simonis_2018_oi_180108.pdf — PDF p. 1](../jama_simonis_2018_oi_180108.pdf#page=1) |
| REPORT | Abstract Results, severe atelectasis; precision nuance retained | [jama_simonis_2018_oi_180108.pdf — PDF p. 1](../jama_simonis_2018_oi_180108.pdf#page=1) |
| REPORT | Abstract Results, pneumothorax | [jama_simonis_2018_oi_180108.pdf — PDF p. 1](../jama_simonis_2018_oi_180108.pdf#page=1) |
| REPORT | Table 2, footnote c; RR, interval and test specification | [jama_simonis_2018_oi_180108.pdf — PDF p. 6](../jama_simonis_2018_oi_180108.pdf#page=6) |
| REPORT | Statistical Analysis, binary outcome specification | [jama_simonis_2018_oi_180108.pdf — PDF p. 4](../jama_simonis_2018_oi_180108.pdf#page=4) |
| PLAN corroboration | SAP Secondary outcomes, RR/Wald/chi-square specification; no conflicting plan side | [joi180108supp2_prod.pdf — PDF p. 13](../joi180108supp2_prod.pdf#page=13) |

**Source evidence:**

| Table 2 outcome | Low event/total | Intermediate event/total | Reported RR (95% CI) | Event-risk ratio at printed counts | Alternative conditional ratio |
|---|---|---|---|---|---|
| ICU mortality | 132/450 | 115/458 | 1.11 (0.96–1.27) | 1.168232 | 1.110840 |
| Hospital mortality | 151/477 | 140/484 | 1.06 (0.93–1.22) | 1.094400 | 1.066452 |
| ARDS | 17/448 | 23/462 | 0.86 (0.59–1.24) | 0.762228 | 0.857889 |
| Pneumonia | 19/450 | 17/462 | 1.07 (0.78–1.47) | 1.147451 | 1.072699 |
| Pneumothorax | 8/448 | 6/462 | 1.16 (0.73–1.84) | 1.375000 | 1.163636 |
| Atelectasis | 51/449 | 52/464 | 1.00 (0.81–1.23) | 1.013534 | 1.007708 |
| Extrapulmonary infection | 20/448 | 28/463 | 0.84 (0.60–1.18) | 0.738202 | 0.840148 |
| Extrapulmonary sepsis | 12/448 | 16/463 | 0.87 (0.56–1.33) | 0.775112 | 0.867955 |
| Delirium | 149/343 | 132/361 | 1.15 (0.99–1.34) | 1.188025 | 1.156162 |
| Need for tracheostomy | 54/477 | 52/484 | 1.03 (0.84–1.26) | 1.053701 | 1.029707 |

**Reported-versus-comparator:** RR labels and effect values versus the treatment-event risk contrast supplied by the adjacent arm-specific fractions; all compared locations are in REPORT material.

**Reasoning procedure:** Match event, assessment population, low/reference group and effect definition. Check all fractions and repeated abstract values directly. Compare R=(a/n)/(c/m) with each two-decimal RR interval, retaining half-unit intervals for every displayed count. Evaluate Q=[a/(a+c)]/[(n−a)/(n+m−a−c)] only as a diagnostic alternative, not as an assertion about computation code. A chi-square P value is symmetric under contingency-table transposition, so this finding does not assert a separate P-value contradiction.

**Calculation:** For ARDS, R=(17/448)/(23/462)=0.762228, conservative half-unit range 0.722479–0.803849, disjoint from reported 0.855–0.865. Q=(17/40)/(431/870)=0.857889; diagnostic log-Wald interval 0.594560–1.237844 tracks printed 0.59–1.24. For pneumothorax, R=1.375000, half-unit range 1.187291–1.597257, disjoint from reported 1.155–1.165; Q=1.163636. ICU/hospital mortality, pneumonia, infection, sepsis and delirium also remain discrepant. Atelectasis and tracheostomy overlap under the conservative precision test and are corroborating locations only. Full row precision bounds and CI diagnostics are preserved in the [numeric checker](review_1_6_1/checkers/numeric_consistency.md).

**Affected result or extracted value:** Binary intervention RRs and 95% CIs, particularly the abstract ARDS, pneumonia and pneumothorax effects, used in downstream effect extraction.

**Why context does not resolve it:** The methods, footnote and abstract give no alternate conditioning or established binary model that identifies the displayed effect quantity. A reader can calculate the column-count event ratio but cannot identify which definition generated the printed effect and interval. Nearby Cox, GLM and mixed-model descriptions apply to separately identified outcomes.

**Alternative source-grounded interpretations:** The displayed effects may reflect the diagnostic reverse-conditioned quantity, or an additional binary model whose coding, adjustment and estimand are unstated. Neither mechanism is asserted; binary computation code and a complete effect definition are unavailable.

**Mechanical evidence recheck:** Direct source recheck matched all ten Table 2 rows, four abstract repetitions, methods and corroborating SAP text; reproduced the eight robust count-based discrepancies and documented overlapping corroborating rows and diagnostic limitations. See the [mechanical evidence recheck](review_1_6_1/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed by human review, clarification could change the binary effect quantity and interval extracted for evidence synthesis. No change in the primary conclusion or the secondary nonsignificance statements is established by this observation.

**Human verification steps:** Inspect every Table 2 RR row and footnote c, the p. 4 binary analysis paragraph and repeated p. 1 results; clarify outcome/group coding, denominator conditioning, reference group and any adjustment behind the effect and interval. No replacement analysis or final value is selected here.

Recheck precision nuance: the abstract's rounded atelectasis percentages (11.4%/11.2%) imply an event-risk ratio range 1.008889–1.026906, disjoint from the printed RR interval 0.995–1.005. The deliberately broader count-half-unit test for its Table 2 fraction overlaps. Both facts are retained; this row remains corroborating in the registered eight-robust-row pattern, with no new issue or inferred computation code.

Additional calculation detail retained from the mechanical recheck: each two-decimal printed RR is allowed r ± 0.005, and each count and denominator is conservatively allowed ± 0.5. For low events a/total n and intermediate events c/total m, R = am/(nc), with R_min = (a − 0.5)(m − 0.5)/[(n + 0.5)(c + 0.5)] and R_max = (a + 0.5)(m + 0.5)/[(n − 0.5)(c − 0.5)]. These generous bounds preserve the robust/corroborating distinction:

| Outcome | Conservative event-risk R interval | Printed RR rounding interval | Evidence contribution |
|---|---|---|---|
| ICU mortality | 1.156219–1.180375 | 1.105–1.115 | Disjoint |
| Hospital mortality | 1.084634–1.104255 | 1.055–1.065 | Disjoint |
| ARDS | 0.722479–0.803849 | 0.855–0.865 | Disjoint |
| Pneumonia | 1.082955–1.215998 | 1.065–1.075 | Disjoint |
| Pneumothorax | 1.187291–1.597257 | 1.155–1.165 | Disjoint |
| Atelectasis | 0.991864–1.035674 | 0.995–1.005 | Overlap; corroborating only |
| Extrapulmonary infection | 0.705568–0.772108 | 0.835–0.845 | Disjoint |
| Extrapulmonary sepsis | 0.718726–0.835286 | 0.865–0.875 | Disjoint |
| Delirium | 1.176221–1.199950 | 1.145–1.155 | Disjoint |
| Need for tracheostomy | 1.031852–1.076020 | 1.025–1.035 | Overlap; corroborating only |

The diagnostic Q conditions low-group membership on event status. Its ordinary diagnostic log-Wald interval uses Q exp(±1.96s), where s² = 1/a − 1/(a+c) + 1/(n−a) − 1/(n+m−a−c). This tracks the printed effect/interval family but does not reconstruct the exact reported pipeline. Some final digits do not match at the printed counts: hospital Q = 1.066452 versus reported 1.06, and the ICU diagnostic upper endpoint = 1.278765 versus reported 1.27. The individually evaluated diagnostic endpoint ranges overlap printed endpoint precision intervals, but do not demonstrate a jointly fitted interval or computation code. The exact binary model, orientation, adjustment if any, and confidence-interval implementation remain human clarification questions. All source values, bounds, diagnostic values and their qualifications are retained in the [complete recheck](review_1_6_1/verification/evidence_recheck.md) and [numeric checker](review_1_6_1/checkers/numeric_consistency.md).


**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

An evidence extractor may copy an effect label, point estimate, confidence interval, event fraction and reference group from an abstract or table into a systematic-review dataset. Human clarification of C001 could affect which binary quantity and interval represent the intervention contrast. Maintaining the distinction between reported estimates and arithmetic diagnostics helps avoid substituting an unestablished analysis during extraction.

This report does not establish that any external dataset has copied these values, that a synthesis or guideline has changed, or that harm occurred. It does not infer a change in the trial's primary conclusion or select final replacement values. Adjudication should establish the intended quantity before any downstream action is chosen.

## Limitations and Missing Definitions

Complete source mapping does not imply exact reconstruction of every fitted analysis. The supplied package lacks participant-level data and binary computation code; the binary outcome/exposure orientation, denominator conditioning, reference category, any additional adjustment or marginalization, and exact Wald approximation function are not fully defined. Outcome-specific event fractions are available and were preserved.

For other relationships, exact reconstruction is limited by unprinted t-test statistics, degrees of freedom and equal-variance choice; individual event and censoring times and Cox implementation details; GLM/GLMM link, covariance and variance specifications; per-cell supplemental test mappings; survivor and subgroup sample sizes; full variable-specific descriptive denominators; and the precise sample-size software function. Graphs were inspected without inferring exact unprinted coordinates. Numerical results for disclosed unreported analyses are absent. Missing details were not converted into assumptions or separate candidates.

Reusable engine versions are undocumented. Direct OCR and Office conversion tools were unavailable, but all direct sources are PDFs and native text plus reusable/fresh page rendering and visual inspection covered every page; no unit required OCR or Office conversion. The eight reusable raster gaps were fully mapped from direct sources. No scientific coverage gap remains. Full limitations are recorded in [limitations.md](review_1_6_1/limitations.md).

## Human Adjudication Checklist

1. Open every linked location in C001 and confirm outcome, strategy order, explicit fractions, RR labels, confidence intervals, and binary-analysis text.
2. Distinguish the eight disjoint conservative count comparisons from the two corroborating rows, retaining the abstract atelectasis precision nuance.
3. Establish the binary estimand, outcome/group orientation, conditioning, reference category, additional model adjustment if any, and interval implementation. Treat Q and its interval as diagnostics until source clarification establishes the analysis.
4. Decide what quantity and interval should be extracted for each affected outcome, keeping that decision separate from any paper-level conclusion assessment.
5. Complete Validity, Importance, Action, Initials, and Notes in the candidate's blank fields. C001 remains Pending Human Adjudication until that human review.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The [routing preflight](review_1_6_1/routing_preflight.md) records PASS, coordinator inference PASS, INTERACTIVE_CLI, CURRENT_SESSION, and all ten named preset pairs. The coordinator used gpt-6.1-sol/high; ordinary specialists used gpt-6.1-sol/medium; statistical, screening, recheck and audit specialists used gpt-6.1-sol/high. Every mandatory specialist stage used a distinct fresh runtime identity.

The [execution manifest](review_1_6_1/agent_execution_manifest.md) records all 12 agents:

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a128dd-7b19-7ec2-80a8-c33eeb3c63ce | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | task:/root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | task:/root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | task:/root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | task:/root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | task:/root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | task:/root/statistics_pass1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | task:/root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | task:/root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | task:/root/statistics_pass2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | task:/root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | task:/root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Specialist runtime identifiers preserve the exact collaboration API canonical task names with the explicit task: namespace prefix. Each identifies one distinct fresh spawn; the coordinator uses the current session UUID.

The [tooling record](review_1_6_1/tooling_record.md) records Linux, direct Poppler 25.03.0 PDF tools and Pandoc 3.1.11.1. No fallback environment was created; removal status is NOT_CREATED. All preprocessing and inspection were local CPU work. No supplied input or reused asset was modified. Before-review integrity manifests are [source hashes](review_1_6_1/source_hashes_before.sha256) and [reused-asset hashes](review_1_6_1/reused_artifact_hashes_before.sha256). The independent audit checked all 5 source and 66 reused-asset hashes and found them unchanged; final completion checks are recorded by the coordinator. The ledger, recheck, audit and this report contain the identical stable set C001, with matching classification fields.

### Reproducibility performance

- **Target basis:** Five native-text PDFs contain 94 pages and 66 reusable derivatives. Eight protocol pages need fresh visual coverage of embedded images; no Office conversion or full-document OCR is required. The main results, five supplemental result tables, four supplemental figures, protocol, and detailed SAP require parallel mapping, three checking lanes, two fresh statistical passes, independent screening, recheck, audit, and report assembly. A 30-45 minute planning range reflects strong extraction reuse with substantial plan-to-report relationship mapping.
- **Total source units:** 94
- **Fresh-source units:** 8
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-10-11T02:52:40Z
- **Finished UTC:** 2026-10-11T03:25:45Z
- **Observed elapsed minutes:** 33.08
- **Target status:** MET_TARGET
- **Exceedance causes:** None

The coordinator finalizes finish-related values immediately after complete Markdown assembly. Local HTML rendering and mechanical validation are outside the observed scientific-review duration; any later model-assisted repair requires updated timing. The planning range does not limit coverage or candidate inclusion.

Final integrity recomputation: all 5 source hashes and 66 reused-asset hashes match their before-review manifests exactly. The completed after-review manifests are [source hashes after](review_1_6_1/source_hashes_after.sha256) and [reused-asset hashes after](review_1_6_1/reused_artifact_hashes_after.sha256). The local mechanical completion result is recorded in [review_validation.json](review_1_6_1/review_validation.json).
