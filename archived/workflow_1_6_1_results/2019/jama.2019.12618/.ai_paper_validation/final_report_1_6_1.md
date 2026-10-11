# Quantitative Quality-Control Consistency Review — FAST Trial, Workflow 1.6.1

**Pending Human Adjudication**

This report prepares candidate quantitative reporting issues for human review. Evidence states, review domains and inclusion-audit records describe the review evidence and classification; they do not adjudicate the candidates or the paper.

## Executive Quality-Control Summary

Complete review of the five supplied PDFs identified **2 stable candidates**, C001 and C002. All **263 source pages** were mapped: 234 pages had usable reusable evidence and 29 required fresh direct-source inspection. The numeric review covered 195 relationships, and two distinct fresh high-effort statistical reviewers each covered all 77 registered statistical relationships.

C001 concerns compatibility of the reported missed-dose mean/SD summaries and P=.87 with the explicitly stated two-sided Welch comparison. C002 concerns the interpretation of a six-month primary-outcome sensitivity labeled per protocol whose reported adherence criterion differs from both supplied SAP versions. Both evidence states are `reproduced`, and both inclusion audits are `CONFIRMED`; both candidates remain **Pending Human Adjudication**.

Five checker findings received independent screening: four INCLUDE rows were consolidated into the two candidates, and one finding was screened out as `CONDITIONAL_OR_UNREPORTED`. The independent audit reviewed every screening decision and all 82 checker excluded observations, with no additional qualifying finding or classification change. No scientific source-coverage gap remains. Missing analysis outputs and operative population details limit the questions that can be answered from this package.

## Package and Reused-Evidence Provenance

The package reports the randomized FAST trial comparing methotrexate and mycophenolate mofetil for uveitis. Document roles were assigned from content. The main article and non-plan results supplement are REPORT material; the bound original/final protocol and statistical analysis plan, including their change summaries, are PLAN material. The data-sharing statement is administrative REPORT-associated material and has no applicable quantitative relationship.

| Source ID | Supplied filename | Content role | Complete units |
|---|---|---|---:|
| DOC-001 | jama_rathinam_2019_oi_190092.pdf | REPORT — main article | 10 PDF pages |
| DOC-002 | joi190092supp1_prod.pdf | REPORT — results supplement | 16 PDF pages |
| DOC-003 | joi190092supp2_prod.pdf | PLAN — original/final protocol and manual, revisions | 153 PDF pages |
| DOC-004 | joi190092supp3_prod.pdf | PLAN — original/final SAP, revisions | 83 PDF pages |
| DOC-005 | joi190092supp4_prod.pdf | REPORT — data-sharing statement | 1 PDF page |
| Total | Five supplied PDFs | Content-based role assignment | 263 PDF pages |

The curator inventoried and froze 52 eligible existing assets: 26 per-page native/layout texts, 9 layout-range texts, 1 duplicate layout text, 5 rendered images, 5 document records, 1 package manifest, 2 page manifests, 2 source-linked quantitative maps and 1 OCR-engine metadata record. Current direct text extraction matched all 26 per-page texts and all 9 nonduplicate layout-range texts byte for byte. Historical maps and document records were used only as locators; their historical scope restrictions did not limit this review. Prior-run candidate, checker, screening, classification and final-report content was not used for discovery.

Reusable images without retained renderer/source-hash provenance were treated as partial aids rather than proof of complete coverage. Fresh derivatives used direct Poppler 26.01.0 and, where needed, Tesseract 5.5.0 CPU OCR. Every candidate was independently checked against the exact supplied PDF pages, including visual source confirmation. Detailed provenance is retained in the [source inventory](review_1_6_1/source_inventory.md), [evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md) and [tooling record](review_1_6_1/tooling_record.md).

## Scope, Complete Coverage, and Exclusions

The review covers counts and denominators; estimate, interval and test logic; statistical method logic; and planned-versus-reported statistical design under QUALITY_CONTROL_SCOPE.md. It includes every direct-source unit, every result-relevant table and figure, primary and key-secondary matched results, and the supplied plan versions and amendments. References, administrative pages and other pages without an applicable relationship were explicitly mapped rather than omitted.

| Source ID | Total pages | Reusable pages | Fresh-required pages | Mapped pages | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | 16 | 16 | 0 | 16 | COMPLETE |
| DOC-003 | 153 | 129 | 24 | 153 | COMPLETE |
| DOC-004 | 83 | 78 | 5 | 83 | COMPLETE |
| DOC-005 | 1 | 1 | 0 | 1 | COMPLETE |
| Total | 263 | 234 | 29 | 263 | COMPLETE |

Fresh protocol inspection covered PDF pages 15, 18, 19, 47, 74, 80, 81, 84, 89, 90, 91, 94, 96, 105, 107, 109, 116, 118, 120, 129, 133, 134, 136 and 150. Twenty pages lacked usable layout segments, and four additional pages had embedded content incompletely represented by text. Fresh SAP formula inspection covered pages 23, 24, 26, 34 and 63; adjacent pages 22 and 64 were also visually confirmed and counted once as reusable-backed. Final counts supersede the initial partition as newly discovered derivative gaps were closed. Reusable plus fresh-required equals total, and mapped equals total, for every source.

Observations were excluded when display precision, immediate context, clear notation or wording, distinct modeled versus crude quantities, unsupported assumptions, peripheral comparisons or scope boundaries resolved their significance under the normative threshold. No preferred analysis, clinical judgment, broad study-design assessment, misconduct judgment or participant-level data audit was performed. No external literature or web evidence was used. The [complete coverage ledger](review_1_6_1/source_coverage.md) and [coverage manifest](review_1_6_1/coverage_manifest.md) retain the source and stage assignments.

## Quantitative and Statistical Relationship Coverage

The current source maps reconstruct participant flow and analysis populations; event and outcome counts; percentages and subgroup totals; effect-measure identities; estimate/interval/direction consistency; matching abstract, narrative, table, figure and supplement results; and planned models, endpoints, missingness, power, noninferiority, multiplicity and monitoring rules. Model-based effects were not required to equal crude recomputations, and unspecified computational conventions were not assumed.

| Review component | Scope | Completion |
|---|---|---|
| Numeric relationships | N001–N195; 94 main/plan bundles plus 101 disjoint supplement relationships | 195/195 complete |
| Statistical pass 1 | Every S001–S077 relationship; fresh root/statistics_one, gpt-6.1-sol/high | 77/77 PASS_1_COMPLETE |
| Statistical pass 2 | Every S001–S077 relationship, complete ledger, five finding decisions and recheck; fresh root/statistics_two, gpt-6.1-sol/high | 77/77 PASS_2_COMPLETE |
| Cross-source review | Matched REPORT/REPORT, PLAN/REPORT and applicable plan-version relationships | Complete |
| Mechanical evidence recheck | C001, C002; all repeated and contextual cited pages | 2/2 complete |
| Independent inclusion and evidence-quality audit | Five finding decisions, 82 checker exclusions, 263 pages and both inventories | Complete |

The two statistical passes used different fresh runtime IDs. Pass 2 revisited both registered issues and the screened rescue-model finding without emitting new findings; a second inclusion screener was therefore not applicable. Missing definitions received explicit completed relationship records. Completion means that the available source evidence was reviewed, including its limits; it does not imply exact reconstruction of every reported model or approximate planning calculation.

Pass 2 qualified the initial wording about rescue-power reproduction: the seventh normal diagnostic is approximately .8233 against a table explicitly labeled approximate 80%, rather than an exact nearest-whole-percent match to 80%. The available rounding allowances and approximate planning context do not establish another candidate. Source inputs, algorithms, quantile conventions and stratum allocations remain bounded limitations where not supplied.

Canonical evidence is retained in the [main map](review_1_6_1/extraction/main_quantitative_evidence.md), [support map](review_1_6_1/extraction/support_quantitative_evidence.md), [numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6_1/statistics/relationship_inventory.md), [first statistical pass](review_1_6_1/checkers/statistical_pass_1.md) and [second statistical pass](review_1_6_1/checkers/statistical_pass_2.md).

## Inclusion Screening Summary

A finding qualifies only when it is reproduced from the supplied source, is in focus, remains unresolved by immediate context for a statistically literate reader in the field, and could change interpretation or extraction of a specific reported result. The independent screener applied all four criteria without a candidate-count target, and the auditor reconsidered decisions in both directions.

| Decision | Finding rows | Consequence |
|---|---:|---|
| INCLUDE | 4 | Consolidated into 2 distinct stable candidates |
| SCREENED_OUT | 1 | No candidate card |
| Total findings screened | 5 | Exactly one screening decision per finding |

| Decision/reason code | Count |
|---|---:|
| INCLUDE / MEETS_THRESHOLD | 4 |
| SCREENED_OUT / NOT_REPRODUCED | 0 |
| SCREENED_OUT / ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT / NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT / TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT / MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT / CONTEXT_RESOLVES | 0 |
| SCREENED_OUT / CONDITIONAL_OR_UNREPORTED | 1 |
| SCREENED_OUT / PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT / OUT_OF_FOCUS | 0 |
| SCREENED_OUT / DUPLICATE_OF_INCLUDED | 0 |

F-ST1-001 maps to C001. F-NUM-001, F-XS-001 and F-ST1-002 map to the same C002 issue; their consolidation preserves every finding and source location. F-XS-002 was screened out because the supplied SAP explicitly permits a site-adjusted secondary rescue analysis, and the reported rescue estimate is not uniquely identified as the different primary Aim 2 analysis. A contradiction would require an unsupported identification of those results. Its decision remains `CONDITIONAL_OR_UNREPORTED`.

Checker self-screening tables contain a separate 82 excluded-observation rows: numeric 24, cross-source 25, statistical pass 1 26 and statistical pass 2 7. All were independently audited, and none required promotion. These rows are not emitted finding IDs and are not included in the five-finding screening denominator. Display-zero P values did not form the basis of either candidate. The [single screening log](review_1_6_1/screening/inclusion_screen.md) and [quality audit](review_1_6_1/quality/evidence_quality_audit.md) preserve the decisions and justifications.

## Review-Domain Summary

Each candidate has exactly one review domain. `statistical_results` covers numerical and statistical-method logic in REPORT materials. `report_internal_inconsistency` covers a report conflict about the outcome, time point, population or comparison to which a number belongs. `protocol_report` covers a supplied PLAN versus REPORT statistical-design or analysis difference. `plan_material` covers a statistical-design inconsistency within PLAN material on which the reported analysis relies. These are classification fields for human review.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 1 |
| report_internal_inconsistency | 0 |
| protocol_report | 1 |
| plan_material | 0 |
| Total | 2 |

| Primary relationship type | Meaning | Stable candidates |
|---|---|---:|
| S_W | Within one REPORT document | 1 |
| S_C | Between different REPORT documents | 0 |
| P_R | PLAN versus REPORT | 1 |
| P_P | Within PLAN material | 0 |
| Total | One primary relationship per candidate | 2 |

Both candidates have a single actual relationship, so all-relationship counts are also S_W=1, P_R=1, S_C=0 and P_P=0. Corroborating locations do not add a conflict relationship. The precedence rule is P_R > P_P > S_C > S_W.

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 2 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 2 |

| Inclusion audit | Stable candidates |
|---|---:|
| CONFIRMED | 2 |
| QUESTIONED | 0 |
| Total | 2 |

Every count reconciles to the two stable ledger IDs. `CONFIRMED` records the independent inclusion audit; it does not complete human adjudication.

## Candidate Index

| Stable ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Missed-dose summaries and stated Welch comparison | statistical_results | S_W | reproduced | CONFIRMED |
| C002 | Reported per-protocol adherence criterion versus supplied SAP | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Missed-dose summaries and stated Welch comparison do not reconcile

**Candidate statement:** The main article describes a two-sided Welch t test for missed-dose percentages, but reports mean (SD) 4.6 (1.0)% versus 4.3 (0.5)% with P=.87 in both table and prose. These summaries and P value do not reconcile for any valid Welch sample sizes, including all allowed display intervals.

**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main p.4 statistical methods vs REPORT main p.6 adherence table and prose
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-ST1-001
**Classification rationale:** Both the stated comparison method and its numerical summaries are printed within the main REPORT. No PLAN or second REPORT is a conflicting comparator. The issue concerns estimate/test and method logic.
**Classification ambiguity:** None
**Status:** Pending Human Adjudication
**Relationship inventory references:** S017.

**Exact source locations:** [Main PDF p.4 — Statistical Analyses](../jama_rathinam_2019_oi_190092.pdf#page=4); [main PDF p.6 — Table 2 missed-dose row and matching paragraph](../jama_rathinam_2019_oi_190092.pdf#page=6). All table and prose occurrences of the pattern are consolidated.

**Source evidence:** Methods identify a Welch t test for missed-dose comparison and two-sided testing. Table 2 labels the summaries “Missed doses, mean (SD), %” and gives 4.6 (1.0), 4.3 (0.5), P=.87; prose repeats mean (SD) and the same values. The footnote defines each patient's missed doses relative to expected doses throughout enrollment. The current checker and independent screener directly read and visually inspected p.6.

**Reported-versus-comparator:** Reported P=.87, whose two-decimal rounding interval is [.865,.875], versus an upper bound .8508783587 on P under the explicitly stated Welch comparison using all permissible rounded mean/SD inputs and any valid group sizes.

**Reasoning procedure:** Permit the full half-unit interval around each one-decimal mean and SD. A valid sample SD/Welch test requires each group to have at least two observations. Bound the smallest mean difference and largest possible standard error without assuming actual adherence sample sizes. Welch degrees of freedom are at least one. The df=1 Student t tail is a conservative upper bound on the two-sided P for the resulting positive statistic.

**Calculation:** Means are within [4.55,4.65] and [4.25,4.35]; SDs within [.95,1.05] and [.45,.55] percentage points. Absolute difference >=.20; SE <=sqrt((1.05^2+.55^2)/2)=.8381527307; |t| >=.2386199945; df>=1. Therefore P<=1−(2/pi)atan(.2386199945)=.8508783587, below the printed P interval. Endpoint inclusion makes the bound conservative. Percent-to-proportion conversion cancels in the test statistic. This is an analytic compatibility bound under the source-stated method, not an assumed-denominator reconstruction.

**Affected result or extracted value:** The adherence comparison P=.87 and the mean/SD summaries 4.6 (1.0)% versus 4.3 (0.5)%.
**Why context does not resolve it:** Table and prose repeat the values and SD label, and the methods expressly identify Welch. Neither rounding, missing sample sizes nor units resolves the discrepancy, and the package does not identify which reported summary or test value should be interpreted differently.
**Alternative source-grounded interpretations:** A different dispersion quantity, adherence variable or comparison method may underlie the printed P. None is established by the supplied materials. No replacement result is inferred.
**Mechanical evidence recheck:** Fresh direct-source recheck found all cited locations and reproduced the stated comparison; no transcription or classification correction. Complete separate facts are recorded in [the mechanical evidence recheck](review_1_6_1/verification/evidence_recheck.md).
**Potential downstream evidence impact:** If confirmed, an extractor could copy an adherence P value or dispersion statistic that does not match the stated comparison. No primary-outcome conclusion change is asserted.
**Human verification steps:** Check the printed method and both p.6 occurrences; establish the actual adherence summaries, dispersion definition and comparison result from the corresponding analysis output.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Reported per-protocol adherence criterion differs from the supplied SAP

**Candidate statement:** The supplied original and final SAP define noncompliance for the per-protocol efficacy population as receipt below 50% of study drug, while the article labels a primary-outcome sensitivity per protocol and includes only patients missing less than 20% of doses.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN SAP pp.31,71 population definitions vs REPORT main pp.6,7 per-protocol sensitivity
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-001, F-XS-001, F-ST1-002
**Classification rationale:** The conflict compares the REPORT's named analysis population with its definition in prospective PLAN material. Original and final SAP versions agree on the disputed threshold and do not create a plan-internal conflict; table/prose/figure corroboration within the article does not create a separate report-internal relationship.
**Classification ambiguity:** None
**Status:** Pending Human Adjudication
**Relationship inventory references:** N040, N078; S022, S065.

**Exact source locations:** [Main PDF p.6 — sensitivity narrative](../jama_rathinam_2019_oi_190092.pdf#page=6); [main PDF p.7 — Figure 2 model 4 and footnote e](../jama_rathinam_2019_oi_190092.pdf#page=7); [SAP PDF p.31 — original §4.1](../joi190092supp3_prod.pdf#page=31); [SAP PDF p.71 — final §4.1](../joi190092supp3_prod.pdf#page=71). Related definition and amendment context: [SAP PDF p.72 — major deviations](../joi190092supp3_prod.pdf#page=72), [SAP PDF p.80 — changes](../joi190092supp3_prod.pdf#page=80), [SAP PDF p.81 — changes continuation](../joi190092supp3_prod.pdf#page=81). All cited occurrences from the three included findings are retained.

**Source evidence:** The SAP per-protocol efficacy population excludes major deviations or noncompliance, explicitly receipt below 50% by self-report or pill counts. The main narrative includes only participants missing less than 20%; Figure 2 calls model 4 “Per protocol,” repeats that cutoff and gives n=184, 61/90 versus 54/94, OR 1.56 (95% CI .84–2.96), P=.17. The supplied change summary does not reconcile the adherence definition.

**Reported-versus-comparator:** Report eligibility is missed doses <20%, equivalent to receipt >80% on the matching expected-dose fraction; SAP adherence eligibility is receipt >=50%, before its additional exclusions. The criteria differ by 30 percentage points.
**Reasoning procedure:** Compare the explicit selection rules for the same named primary-outcome sensitivity population. Distinguish original/final plan versions, disclosed changes and additional major-deviation conditions. Do not infer a participant-level membership difference or an unreported alternative estimate.
**Calculation:** If a is fraction received and m=1−a is fraction missed, the report requires m<.20, hence a>.80; the SAP excludes a<.50. Explicit cutoffs are selection rules rather than rounded outcome estimates. The printed n=90+94=184 itself reconciles.
**Affected result or extracted value:** Interpretation of the n=184 per-protocol primary-outcome sensitivity and OR 1.56 (.84–2.96), P=.17 as the prospectively defined analysis population.
**Why context does not resolve it:** The article clearly identifies its actual cutoff but does not explain the different definition of its named per-protocol population relative to either supplied SAP version. The immediate source context supplies no corresponding amendment or separately reported estimate under the SAP definition.
**Alternative source-grounded interpretations:** This may be an additional stricter-adherence sensitivity labeled per protocol, or an amendment absent from the supplied package may have changed the threshold. Application of other major-deviation exclusions is unreported. These possibilities do not establish an alternative count or effect.
**Mechanical evidence recheck:** Fresh direct-source recheck found all cited locations and reproduced the stated comparison; no transcription or classification correction. Complete separate facts are recorded in [the mechanical evidence recheck](review_1_6_1/verification/evidence_recheck.md).
**Potential downstream evidence impact:** If confirmed, an extractor could attribute this estimate to the SAP-defined per-protocol population or classify it as prespecified under a population definition that differs from the supplied plan. No direction or magnitude of an alternative result is asserted.
**Human verification steps:** Match the model 4 inclusion rule and deviation exclusions to the operative SAP definition; establish whether the displayed result is the prespecified per-protocol estimate or an additional sensitivity, and document any operative amendment.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

An extractor could carry forward a reported adherence summary and comparison P value without establishing that they describe the same analysis, or could tag a sensitivity estimate as belonging to a prospectively defined per-protocol population despite the supplied definition difference. If a candidate is confirmed through human review, those specific fields may require reconciliation before evidence reuse. This report does not claim that such reuse, a conclusion change or downstream harm has occurred.

The primary trial estimate, subgroup findings and unavailable alternative-population results are not replaced by the candidate calculations. C001's conservative bound is a compatibility check, not a replacement P value. C002's explicit rule comparison does not establish a different realized population size or effect. These distinctions should accompany extraction and any subsequent synthesis.

## Limitations and Missing Definitions

All supplied units were mapped and no scientific source-coverage gap remains. The evidence is restricted to this package, which contains no participant-level dataset or computational output. Actual adherence-test group sizes, unrounded mean/SD values, individual adherence observations and the generating output are unavailable. C001 does not require a specific group size, but the exact intended summary and test result cannot be reconstructed.

For C002, the operative dose denominator and observation period, reconciliation of self-report and pill counts, actual major-deviation exclusions, individual analysis-set membership and any amendment not supplied remain unavailable. The written cutoff comparison is reproduced; a different realized membership, effect or omitted planned analysis is not asserted. A separate stricter-adherence sensitivity or an unsupplied operative amendment remains a bounded alternative explanation.

Some secondary estimates lack the full variance/covariance, degrees of freedom, test-tail convention, interval inversion, risk-difference mapping or detailed estimator implementation needed for exact numerical reproduction. Imputation draws and pooled standard errors, prospective anatomical-stratum allocation, complete power algorithms and quantile conventions are also absent. The supplied materials do not give the noninferiority-specific one-sided alpha, realized interim information fractions/statistics or final adjusted critical value. These limitations were recorded rather than filled with assumed software defaults or preferred analyses. Absence of a separate reason-adjusted rescue estimate or other planned secondary output alone does not establish replacement of a planned analysis.

Reusable text was source-matched, but exact historical extraction versions and image-renderer/source-hash provenance are incomplete for some derivatives. Fresh direct inspection and targeted CPU OCR closed all identified text, embedded-content and formula gaps. Original assets were preserved, and candidate evidence was confirmed visually from exact source pages.

Two initial protocol context plans exceeded the 200000-character bound after newly populated OCR text was added: pages 1–64 reached 200637 characters and pages 65–128 reached 223504. Four fresh medium-effort confirmations repaired the plans using disjoint 32-page scopes, with burdens of 96000, 104637, 114186 and 109318 characters. They retained the original mappings and reused current text/images without repeating extraction or OCR; no new inferential or design relationship emerged.

The bounded confirmations transparently superseded a compressed current derivative summary for protocol page 96: the Phase II laboratory-report baseline entry is blank, with week 2, months 1–5 and month 6 scheduled and failure marked (x). The source matrix had been retained. The current N080 spending-function arithmetic was also corrected to .001000000324 and .007517835706, consistent with the source's approximate .001/.0075 and S070. These derivative corrections do not describe source reporting issues and do not change candidate evidence states or the complete statistical relationship set. The rescue-power approximation qualification is retained in the relationship-coverage section. Further details are in [limitations.md](review_1_6_1/limitations.md).

## Human Adjudication Checklist

1. Read the exact linked source pages and distinguish printed PDF pagination from plan folios.
2. For C001, reconcile the adherence summary variable, dispersion definition, actual analysis output and the method attached to P=.87. Do not interpret the conservative compatibility bound as a substitute result.
3. For C002, establish whether Figure 2 model 4 is the SAP-defined per-protocol efficacy analysis or an additional adherence sensitivity, and identify the operative dose denominator/period, deviation exclusions and any supporting amendment.
4. Consider whether each issue changes interpretation or extraction of the named result, keeping missing definitions and bounded alternative explanations explicit.
5. Complete the five blank human adjudication fields on each card. Both cards remain Pending Human Adjudication until that review is documented.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Reproducibility and source integrity

Workflow profile: 1.6.1. Execution platform: local CPU-only Linux. Routing preflight: PASS; provider: CURRENT_SESSION; execution mode: INTERACTIVE_CLI; configured coordinator: gpt-6.1-sol/high. All ten named agent presets were verified, with ordinary roles at medium effort and statistical, screening, recheck and audit roles at high effort. Mandatory stages used fresh distinct runtimes; no agent was promoted across mandatory stages.

Direct tools available: pdfinfo, pdftotext, pdftoppm, pdftocairo, tesseract, libreoffice and pandoc. Current PDF processing used Poppler 26.01.0; targeted OCR used Tesseract 5.5.0 CPU; hashing used sha256sum from uutils coreutils 0.10.0. Pandoc 3.7.0.2 is available for local rendering. Fallback environment: NOT_NEEDED; fallback capabilities used: None; fallback environment removed: NOT_CREATED. No global installation or GPU operation was used.

All five direct sources and all 52 frozen reused assets were hashed before review. The independent audit's direct hash checks found all 5/5 source and 52/52 reused hashes unchanged. Final coordinator hash recomputation, local standalone HTML rendering and mechanical validation follow Markdown assembly; those completion checks are recorded in the canonical integrity and validation artifacts, rather than inferred from the scientific audit. The before manifests are [source hashes](review_1_6_1/source_hashes_before.sha256) and [reused-asset hashes](review_1_6_1/reused_artifact_hashes_before.sha256). All supplied sources and pre-existing audit assets were preserved.

Canonical controls and artifacts include the [routing preflight](review_1_6_1/routing_preflight.md), [run state](review_1_6_1/run_state.md), [execution manifest](review_1_6_1/agent_execution_manifest.md), [candidate ledger](review_1_6_1/candidate_ledger.md), [evidence recheck](review_1_6_1/verification/evidence_recheck.md) and [evidence-quality audit](review_1_6_1/quality/evidence_quality_audit.md). The complete stable set is C001 and C002 throughout those candidate artifacts and this report. Final mechanical status is retained in [review_validation.json](review_1_6_1/review_validation.json).

### Agent execution

The table below copies every actual runtime from the execution manifest. Identifiers root/NAME denote the canonical runtime task /root/NAME. Artifact paths are relative to review_1_6_1. The coordinator appears once; the report-generator artifact includes the finalized limitations, with this complete report listed separately in the coverage manifest.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_sap_shard | root/sap_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap_001_064.md |
| support_protocol_a_shard | root/protocol_a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_001_064.md |
| support_protocol_b_shard | root/protocol_b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_065_128.md |
| support_protocol_c_shard | root/protocol_c | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_129_153.md |
| support_sap_formula_repair | root/sap_formula_repair | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap_formula_visual_confirmation.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_one | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| numeric_supplement_shard | root/numeric_supplement_shard | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_supplement.md |
| inclusion_screener | root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_two | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| support_protocol_b1_context_repair | root/protocol_b1_confirmation | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_065_096_bounded_confirmation.md |
| support_protocol_b2_context_repair | root/protocol_b2_confirmation | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_097_128_bounded_confirmation.md |
| support_protocol_a1_context_repair | root/protocol_a1_confirmation | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_001_032_bounded_confirmation.md |
| support_protocol_a2_context_repair | root/protocol_a2_confirmation | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_033_064_bounded_confirmation.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

The package-specific target is a planning range and does not limit coverage or candidate inclusion. The exact canonical performance fields below are copied from run_state.md; the coordinator finalizes finish, observed duration, status and bounded causes immediately after Markdown assembly. Local HTML rendering and mechanical validation are excluded from observed review duration; a later model repair requires updated timing before rendering and validation.

- **Target basis:** Five native-text PDF sources contain 263 unique pages; 234 pages have source-matched reusable text and 24 protocol pages and 5 SAP formula pages require fresh visual inspection or targeted CPU OCR. Protocol/manual and SAP each exceed the 200000-character bound and need disjoint mapping shards, while main/results/admin material is smaller. No Office conversion or fallback environment is needed. A 35-55 minute planning range allows parallel bounded mapping, parallel first checkers, initial screening and source recheck, a distinct complete statistical second pass, inclusion audit and full report assembly; candidate volume does not set scope.
- **Total source units:** 263
- **Fresh-source units:** 29
- **Target elapsed minutes:** 35-55
- **Started UTC:** 2026-10-11T02:45:41Z
- **Finished UTC:** 2026-10-11T03:24:11Z
- **Observed elapsed minutes:** 38.50
- **Target status:** MET_TARGET
- **Exceedance causes:** None
