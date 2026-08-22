# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.5.1

> **Pending Human Adjudication.** This report records source-grounded quantitative reporting quality-control candidates. It does not determine validity, prescribe a correction, or attribute an authorial explanation.

## Executive Quality-Control Summary

Complete review of the five supplied PDFs mapped all 263/263 direct-source pages and produced eight distinct candidate consistency issues (C001–C008). The candidates concern one timeline, one denominator total, two cross-document definitions, one statistical compatibility check, two adverse-event denominator/label observations, and one allocation-description comparison. Small preventable reporting defects can matter for downstream evidence extraction; this report does not claim that any candidate propagated, changed a conclusion, or caused serious harm.

All eight cards are **Pending Human Adjudication**. The candidate count is an output of complete coverage, not a cap, queue, ranking, or deferred subset. No candidate is based solely on a display-zero P value.

## Package and Reused-Evidence Provenance

The package contains five supplied PDF direct sources: the main article (10 pages), Supplement 1/results (16), protocol (153), SAP (83), and data-sharing statement (1). The direct-source inventory, SHA-256 records, and reusable-asset inventory are retained in [the review artifacts](review_1_5_1/source_inventory.md), [source hashes](review_1_5_1/source_hashes_before.sha256), and [reused-artifact hashes](review_1_5_1/reused_artifact_hashes_before.sha256).

Twenty-six pages had usable pre-existing native/layout text (all main-article and Supplement 1 pages); those assets were used as locators and transcription aids, with direct-source confirmation for recheck. The remaining 237 pages required fresh direct PDF mapping. No Office, workbook, CSV, or participant-level source was supplied.

## Scope, Complete Coverage, and Exclusions

| Source | Units | Reusable | Fresh required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| Main article | 10 | 10 | 0 | 10 | COMPLETE |
| Supplement 1/results | 16 | 16 | 0 | 16 | COMPLETE |
| Protocol | 153 | 0 | 153 | 153 | COMPLETE |
| SAP | 83 | 0 | 83 | 83 | COMPLETE |
| Data-sharing statement | 1 | 0 | 1 | 1 | COMPLETE |
| **Total** | **263** | **26** | **237** | **263** | **COMPLETE** |

Coverage was assigned through disjoint source and checking artifacts in [coverage_manifest.md](review_1_5_1/coverage_manifest.md). Bibliographic, cover, and purely administrative source units were mapped as no-applicable where appropriate rather than omitted. This was a quantitative reporting consistency review; it did not conduct a broad clinical, methodological, raw-data, misconduct, or external-literature audit.

## Quantitative and Statistical Relationship Coverage

The mapped numeric/reporting inventory covers **N001–N282**; numeric consistency checking covered 282/282. The inferential-statistical inventory covers **S001–S101**. Both independent statistical passes covered 101/101 relationships, and pass 2 revisited all eight stable candidates. Cross-source checking covered the complete union of the 282 numeric and 101 statistical relationships. Planned protocol/SAP definitions were not treated as evidence that an observed analysis used the same model without a matched source comparator.

The relationship maps and pass records are [numeric inventory](review_1_5_1/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_5_1/statistics/relationship_inventory.md), [statistical pass 1](review_1_5_1/checkers/statistical_pass_1.md), and [statistical pass 2](review_1_5_1/checkers/statistical_pass_2.md).

## Candidate Index

| ID | Candidate consistency issue | Primary category |
|---|---|---|
| [C001](#c001--protocol-timeline-end-date) | Protocol timeline end date | Numeric or arithmetic inconsistency |
| [C002](#c002--eligible-failure-total-vs-switching-denominators) | Eligible failure total vs switching denominators | Denominator, proportion, or total inconsistency |
| [C003](#c003--allocation-block-sizes) | Allocation block sizes | Cross-document numeric inconsistency |
| [C004](#c004--six-month-success-injection-after-90-days-criterion) | Six-month success injection-after-90-days criterion | Cross-document numeric inconsistency |
| [C005](#c005--missed-dose-welch-p87-compatibility) | Missed-dose Welch P=.87 compatibility | Statistical reporting inconsistency |
| [C006](#c006--main-table-3-mmf-n109-header-vs-supplement-n108percentages) | Main Table 3 MMF n=109 header vs supplement N=108/percentages | Cross-document numeric inconsistency |
| [C007](#c007--etable-9-mmf-serious-diarrhea-1-34-vs-n20) | eTable 9 MMF serious diarrhea 1 (3.4) vs N=20 | Denominator, proportion, or total inconsistency |
| [C008](#c008--etable-8-serious-ocular-hypertension-label-vs-etable-1-surgery-required-definition) | eTable 8 serious-ocular hypertension label vs eTable 1 surgery-required definition | Measure, label, or scale inconsistency |

## Candidate Evidence Cards

## C001 — protocol timeline end date

**Candidate statement:** Pending Human Adjudication: the printed protocol timeline has a maximum 12-month follow-up plus a one-month window ending before both the implied endpoint for the final enrollment month and the printed shorter follow-up endpoint.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [joi190092supp2_prod.pdf — PDF p. 11, Table 1](<../joi190092supp2_prod.pdf#page=11>).

**Source evidence:** Table 1 prints enrollment through May 2015, six-month follow-up through December 2015, and maximum 12-month follow-up plus a one-month visit window through July 2015.

**Reported-versus-comparator:** The July 2015 maximum-follow-up endpoint is compared with the May 2015 last enrollment month plus the printed duration, and independently with December 2015 for the shorter follow-up phase.

**Reasoning procedure:** Apply month-level calendar ordering under the stated reading that the maximum follow-up applies to the final enrollee; no rounding convention is needed.

**Calculation:** May 2015 + 12 months + one-month window reaches approximately June 2016. July 2015 is also five months earlier than December 2015.

**Alternative source-grounded interpretations:** July 2015 may refer to an earlier cohort, a year digit may be typographical, or an unsupplied amendment may govern the schedule.

**Mechanical evidence recheck:** The cited table and all three date statements were found and transcribed consistently; the remaining question is which amendment and cohort the July date governs.

**Quality-control relevance:** A timeline field is internally inconsistent under the printed schedule and could impair structured protocol-date extraction.

**Potential downstream evidence impact:** If confirmed, a protocol or trial-timeline extractor could copy a conflicting follow-up endpoint. No observed follow-up change or conclusion change is established.

**Human verification steps:** Check the final amendment, final enrollment date, and cohort applicability of the July endpoint.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — eligible failure total vs switching denominators

**Candidate statement:** Pending Human Adjudication: the arm-specific switching denominators total 74 while the prose reports 49 of 68 eligible failures, although the switching numerators and individual percentages reconcile.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_rathinam_2019_oi_190092.pdf — PDF p. 7](<../jama_rathinam_2019_oi_190092.pdf#page=7>); [jama_rathinam_2019_oi_190092.pdf — PDF p. 6, Table 2](<../jama_rathinam_2019_oi_190092.pdf#page=6>); [jama_rathinam_2019_oi_190092.pdf — PDF p. 3, Figure 1](<../jama_rathinam_2019_oi_190092.pdf#page=3>).

**Source evidence:** The prose gives 49 of 68 eligible patients, then 20/32 (62.5%) and 29/42 (69.0%). Table 2 gives 32 and 42 failures; Figure 1 gives 20 and 29 switches.

**Reported-versus-comparator:** The aggregate eligible denominator (68) is compared with the sum of the two printed arm denominators (32+42).

**Reasoning procedure:** Reconcile stated switch numerators and denominators without assuming which failures were eligible.

**Calculation:** 20+29=49; 32+42=74; 74−68=6. Individually, 20/32=62.5% and 29/42=69.05%, displayed as 69.0%.

**Alternative source-grounded interpretations:** The 32 and 42 may be all failures and 68 a narrower eligible subset; the original-arm allocation and reason for the six excluded failures are not supplied.

**Mechanical evidence recheck:** All pages, values, and fractions were found. The literal denominator comparison is applicable, while the intended denominator definition remains unreported.

**Quality-control relevance:** The aggregate and arm-specific denominators need an explicit relationship for reproducible participant-flow and treatment-switch extraction.

**Potential downstream evidence impact:** If confirmed, a data extractor could pair the aggregate eligible count with incompatible arm denominators. No treatment-effect or conclusion change is established.

**Human verification steps:** Identify the eligible denominator by original arm and document the six excluded failures and reasons.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — allocation block sizes

**Candidate statement:** Pending Human Adjudication: matched trial allocation descriptions list different possible block-size sets.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_rathinam_2019_oi_190092.pdf — PDF p. 2](<../jama_rathinam_2019_oi_190092.pdf#page=2>); [joi190092supp2_prod.pdf — PDF p. 13](<../joi190092supp2_prod.pdf#page=13>); [joi190092supp3_prod.pdf — PDF p. 9](<../joi190092supp3_prod.pdf#page=9>); [joi190092supp3_prod.pdf — PDF pp. 49–50](<../joi190092supp3_prod.pdf#page=49>) and [p. 50](<../joi190092supp3_prod.pdf#page=50>).

**Source evidence:** The article lists permutated block sizes 4 and 6. The protocol lists 4, 6, or 8 with equal probability. Later supplied SAP definitions specify 4 (probability 2/3) and 6 (probability 1/3).

**Reported-versus-comparator:** The article set {4,6} is compared with the protocol set {4,6,8}; the later SAP is alternative version-specific context rather than proof of the applied allocation list.

**Reasoning procedure:** Compare stated possible-block sets for the same site-stratified trial allocation, while retaining version uncertainty.

**Calculation:** `{4,6}` versus `{4,6,8}` has symmetric difference `{8}`.

**Alternative source-grounded interpretations:** A later amendment or implementation decision may have removed size 8, the article may describe realized rather than possible sizes, and the SAP's later 4/6 rule may govern the generated list.

**Mechanical evidence recheck:** Both compared passages were found; the protocol page is dated September 4, 2012. Final amendment history and the randomization list are absent.

**Quality-control relevance:** Allocation-rule fields need a version label when source documents provide different possible values.

**Potential downstream evidence impact:** If confirmed, a trial-methods extractor could copy different allocation-block specifications. No randomization failure or conclusion change is established.

**Human verification steps:** Review the approved amendment and randomization-list specification and determine whether the SAP rule governed the generated sequence.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — six-month success injection-after-90-days criterion

**Candidate statement:** Pending Human Adjudication: the protocol manual includes a post-day-90 injection condition in six-month success, whereas the article's enumerated success definition omits it.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_rathinam_2019_oi_190092.pdf — PDF p. 3](<../jama_rathinam_2019_oi_190092.pdf#page=3>); [jama_rathinam_2019_oi_190092.pdf — PDF p. 6](<../jama_rathinam_2019_oi_190092.pdf#page=6>); [joi190092supp2_prod.pdf — PDF p. 80, §2.5.1](<../joi190092supp2_prod.pdf#page=80>); [joi190092supp3_prod.pdf — PDF p. 70](<../joi190092supp3_prod.pdf#page=70>).

**Source evidence:** Protocol manual Version 4.5 requires no periocular or intravitreal corticosteroid injection after the first 90 days. The article's three-part success definition omits injection status, calls other injections protocol deviations, and reports four post-day-90 injections in each arm. The SAP sensitivity context on physical PDF p. 70 classifies an injection at 90 days using inflammation status at injection.

**Reported-versus-comparator:** The article's enumerated six-month success criteria are compared with the manual's explicit no-injection-after-90-days condition. The SAP text supplies context, not an established primary-analysis rule.

**Reasoning procedure:** Compare the criterion sets only; do not recalculate success counts absent participant-level classifications and the in-force endpoint version.

**Calculation:** The manual adds one explicit condition absent from the article's enumerated set. Eight reported cases are 4+4, but no revised 64/96 or 56/98 success count can be calculated.

**Alternative source-grounded interpretations:** The article may abbreviate an operational rule, protocol-deviation status may map to failure elsewhere, or an endpoint amendment may explain the difference. The SAP uses “90 days after enrollment”; a separate later deviation text uses `>90 days`, so these are not silently normalized.

**Mechanical evidence recheck:** The physical protocol PDF p. 80 (internal p. 16) was directly visually inspected because native text was unusable. The source does not establish whether every deviation counted as a primary-endpoint failure.

**Quality-control relevance:** Endpoint criteria and protocol-deviation rules should be explicitly aligned for reproducible outcome extraction.

**Potential downstream evidence impact:** If confirmed, an outcome-definition extractor could omit or add a post-day-90 injection criterion. No altered success count or conclusion change is established.

**Human verification steps:** Verify the endpoint version in force, classification of all eight injection cases, and their treatment in the 64/96 and 56/98 analyses.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — missed-dose Welch P=.87 compatibility

**Candidate statement:** Pending Human Adjudication: the reported P=.87 is not compatible with a conventional two-sided Welch calculation from the displayed missed-dose summaries and header sample sizes, subject to unreported analytic details.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_rathinam_2019_oi_190092.pdf — PDF p. 4](<../jama_rathinam_2019_oi_190092.pdf#page=4>); [jama_rathinam_2019_oi_190092.pdf — PDF p. 6, Table 2](<../jama_rathinam_2019_oi_190092.pdf#page=6>).

**Source evidence:** Table 2 prints MTX 4.6 (SD 1.0)% with n=96 and MMF 4.3 (SD 0.5)% with n=98, P=.87. Methods name a Welch t test for missed doses.

**Reported-versus-comparator:** The reported P=.87 is compared with a diagnostic conventional two-sample, two-sided Welch calculation using the displayed summaries and header n values.

**Reasoning procedure:** Treat the reconstruction as conditional: the row-specific analytic n, SD meaning, scale, transformation, weighting, and output are not supplied.

**Calculation:** `SE=sqrt(1.0²/96+0.5²/98)=0.113875753`; difference `=0.3`; `t=2.634450`, approximately 139.06 Welch degrees of freedom; two-sided diagnostic `P=0.009382747` (about .01), not .87.

**Alternative source-grounded interpretations:** Different analytic n, unrounded or transformed data, another summary definition, weighting, or a P value belonging to another comparison could explain the mismatch.

**Mechanical evidence recheck:** The method, table values, n headers, and P value were found. The reconstruction does not replace the reported analysis or establish a corrected P value.

**Quality-control relevance:** A printed summary/test/P relationship should be reproducible or explicitly qualified when analytic inputs differ from displayed values.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy the P value with summaries that do not support it under the stated diagnostic assumptions. No effect estimate or conclusion change is established.

**Human verification steps:** Inspect row-specific observations, analytic sample sizes, transformation/scale, and Welch-test output.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — main Table 3 MMF n=109 header vs supplement N=108/percentages

**Candidate statement:** Pending Human Adjudication: Main Table 3 uses an MMF header n=109 while its selected percentages reconcile to treated N=108, which matches Supplement 1 headers; the row-level denominator convention is implicit.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_rathinam_2019_oi_190092.pdf — PDF p. 8, Table 3](<../jama_rathinam_2019_oi_190092.pdf#page=8>); [joi190092supp1_prod.pdf — PDF p. 10, eTable 4](<../joi190092supp1_prod.pdf#page=10>); [joi190092supp1_prod.pdf — PDF p. 11, eTable 5](<../joi190092supp1_prod.pdf#page=11>); [joi190092supp1_prod.pdf — PDF p. 12, eTable 6](<../joi190092supp1_prod.pdf#page=12>).

**Source evidence:** Main Table 3 header is MMF n=109; it reports 19 (17.6) decreased/defective vision and 59 (54.6) fatigue, with a footnote that one assigned patient never received study drug. eTables 4–6 label treated MMF N=108. Only eTable 4 repeats the matched decreased/defective-vision cell 19 (17.6); the 59 (54.6) fatigue figure is an internal main-table denominator check, not an eTable 6 repeated cell.

**Reported-versus-comparator:** Main header n=109 and its count/percentage cells are compared with treated N=108 headers and the matched eTable 4 cell; the fatigue example is compared internally with its two possible denominators.

**Reasoning procedure:** Test each displayed count/percentage at one-decimal precision without inferring whether a randomized header was intentionally paired with treated-population percentages.

**Calculation:** `19/108=17.5926%`→17.6%, versus `19/109=17.4312%`→17.4%; `59/108=54.6296%`→54.6%, versus `59/109=54.1284%`→54.1%.

**Alternative source-grounded interpretations:** The header may intentionally report randomized N=109 while percentages use the 108 treated participants, signaled by the footnote but not stated as a row-level denominator convention.

**Mechanical evidence recheck:** The header, footnote, cells, and all three supplement N=108 headers were found. eTable 5's 19 (17.6) concerns a different row; eTable 6 does not repeat 59 (54.6).

**Quality-control relevance:** Explicit denominator labeling is needed when a table header and percentage denominator may refer to different populations.

**Potential downstream evidence impact:** If confirmed, an adverse-event extractor could use n=109 rather than the apparent treated denominator 108. No broader adverse-event effect or conclusion change is established.

**Human verification steps:** Confirm the approved Table 3 denominator convention and whether each MMF percentage uses 108.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — eTable 9 MMF serious diarrhea 1 (3.4) vs N=20

**Candidate statement:** Pending Human Adjudication: eTable 9 reports MMF N=20 and Serious Systemic diarrhea 1 (3.4), although the stated count-over-N rule yields 5.0% to one decimal.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [joi190092supp1_prod.pdf — PDF p. 15, eTable 9](<../joi190092supp1_prod.pdf#page=15>), MMF N=20, Serious Systemic diarrhea row.

**Source evidence:** The table defines entries as patients reporting at least one event (%), labels MMF N=20, and prints 1 (3.4) for Serious Systemic diarrhea. Other N=20 count-one cells show 1 (5.0); N=29 MTX count-one cells show 1 (3.4).

**Reported-versus-comparator:** The displayed 3.4% is compared with the table's own N=20 denominator and count-over-denominator definition.

**Reasoning procedure:** Apply the printed denominator and one-decimal display convention; no diarrhea-specific denominator exception is printed.

**Calculation:** `100×1/20=5.0%`; `100×1/29=3.4483%`, displayed as 3.4%.

**Alternative source-grounded interpretations:** The percentage may have been transposed from the N=29 column, the header/count may be wrong, or an unprinted subset near 29 may apply.

**Mechanical evidence recheck:** The cell and header were visually confirmed. Event-level tabulation and any event-specific denominator are absent.

**Quality-control relevance:** Count, denominator, and displayed percentage need to be aligned in a table intended for event extraction.

**Potential downstream evidence impact:** If confirmed, a safety-data extractor could copy 3.4% as the MMF serious-diarrhea proportion. No broader adverse-event rate or conclusion effect is established.

**Human verification steps:** Verify the adverse-event tabulation, operative denominator, and whether a subset exception exists.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — eTable 8 serious-ocular hypertension label vs eTable 1 surgery-required definition

**Candidate statement:** Pending Human Adjudication: eTable 8 places “Ocular hypertension >24mm Hg” in both non-serious and serious sections, whereas eTable 1 defines serious ocular hypertension as surgery required.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi190092supp1_prod.pdf — PDF p. 5, eTable 1](<../joi190092supp1_prod.pdf#page=5>); [joi190092supp1_prod.pdf — PDF p. 14, eTable 8](<../joi190092supp1_prod.pdf#page=14>); [joi190092supp1_prod.pdf — PDF p. 15, eTable 9](<../joi190092supp1_prod.pdf#page=15>).

**Source evidence:** eTable 1 classifies ocular hypertension at least 24 mm Hg as non-serious and surgery required (laser or incisional) as serious. eTable 8 repeats “Ocular hypertension >24mm Hg” under both sections; the serious row is MTX 1 (1.6), MMF 0 (0.0). eTable 9 labels the serious row “Ocular hypertension, surgery required.”

**Reported-versus-comparator:** The eTable 8 serious-row label is compared with eTable 1's serious surgery-required criterion, eTable 8's own non-serious label, and eTable 9's surgery-required serious label.

**Reasoning procedure:** Compare categorical labels and threshold/seriousness definitions; percentages are not the mismatch.

**Calculation:** No percentage calculation applies. The serious eTable 8 row states a threshold-only criterion, while eTable 1 assigns threshold-only ocular hypertension to non-serious and surgery-required cases to serious; eTable 8 also uses `>24` where eTable 1 uses at least 24.

**Alternative source-grounded interpretations:** The serious event may have required surgery but have an abbreviated/copied label, or eTable 8 may use another unprinted definition. Its footnote points to **eFigure 2**, not eTable 1; no eFigure 2 content appears in the supplied supplement text.

**Mechanical evidence recheck:** All three printed labels and the eFigure 2 footnote were found. The eFigure 2 reference is an unresolved citation nuance, and eTable 1 remains a separate supplied comparator.

**Quality-control relevance:** Seriousness labels need to state a consistent criterion for reliable safety-event categorization.

**Potential downstream evidence impact:** If confirmed, a safety-data extractor could classify the displayed event differently. No event-level clinical consequence or paper-conclusion effect is established.

**Human verification steps:** Review the event-level case, whether surgery occurred, and the intended content or reference for eFigure 2.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If human adjudication confirms a candidate, structured evidence products could copy the affected timeline, denominator, allocation rule, endpoint criterion, P value, adverse-event percentage, or seriousness label. These are bounded extraction considerations only. The supplied package does not establish that any error propagated to a systematic review, meta-analysis, guideline, or later publication, and it does not establish a conclusion change.

## Limitations and Missing Definitions

The supplied PDFs lack participant-level classifications, adverse-event tabulations, unrounded missed-dose data, row-specific analytic n, transformations/weights, final analysis output, amendment history, the final randomization list, and eFigure 2 content. These absences limit explanation and correction, but do not erase the directly observed comparisons. Protocol PDF p. 80 required direct visual confirmation because its native text layer was unusable. The complete limitations record is [limitations.md](review_1_5_1/limitations.md).

## Human Adjudication Checklist

For every card, confirm the cited source page and transcription; verify the stated comparator and rule; obtain the named missing definition or primary record; decide whether an erratum, clarification, or no action is appropriate; and complete the five blank adjudication fields. This checklist does not assign an adjudication outcome.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- **Source-unit counts:** 263 total; 26 reusable; 237 fresh-required; 263 mapped.
- **Coverage result:** 263/263 mapped, with each direct-source row COMPLETE.
- **Relationship result:** N001–N282 and S001–S101 inventoried; both statistical passes cover S001–S101.
- **Candidate identity result:** Ledger, evidence recheck, quality audit, and this report contain C001–C008.
- **Source integrity:** Pre-review SHA-256 inventories cover all five direct sources and eligible reused assets; the quality audit records that `sha256sum -c` reproduced them. Post-assembly hash and validator stages remain coordinator work.

### Agent execution manifest

| Stage | Agent ID | Model / effort | Durable artifact |
|---|---|---|---|
| Coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol / high | run_state.md |
| Reuse asset curator | /root/reuse_asset_curator | gpt-5.6-terra / medium | evidence_asset_inventory.md |
| Main quantitative mapper | /root/main_mapper | gpt-5.6-terra / medium | extraction/main_quantitative_evidence.md |
| Support mapper (results) | /root/supp_results_mapper | gpt-5.6-terra / medium | parts/support_supp_results_pp001_016.md |
| Support mappers (protocol pp. 1–153) | /root/protocol_mapper_001_032; /root/protocol_mapper_033_064; /root/protocol_mapper_065_096; /root/protocol_mapper_097_128; /root/protocol_mapper_129_153 | gpt-5.6-terra / medium | five protocol shard artifacts |
| Support mappers (SAP pp. 1–83) | /root/sap_mapper_001_032; /root/sap_mapper_033_064; /root/sap_mapper_065_083 | gpt-5.6-terra / medium | three SAP shard artifacts |
| Support mapper (data sharing) | /root/data_sharing_mapper | gpt-5.6-terra / medium | parts/support_data_sharing_p001.md |
| Relationship consolidator | /root/relationship_consolidator | gpt-5.6-terra / medium | extraction/support_quantitative_evidence.md |
| Numeric checkers | /root/numeric_checker_001_094; /root/numeric_checker_095_188; /root/numeric_checker_189_282 | gpt-5.6-terra / medium | three numeric-check shard artifacts |
| Cross-source checkers | /root/cross_checker_scope_1; /root/cross_checker_scope_2; /root/cross_checker_scope_3; /root/cross_checker_scope_4 | gpt-5.6-terra / medium | four cross-source shard artifacts |
| Statistical pass 1 | /root/statistics_pass_1 | gpt-5.6-terra / high | checkers/statistical_pass_1.md |
| Numeric checker consolidator | /root/numeric_checker_consolidator | gpt-5.6-terra / medium | checkers/numeric_consistency.md |
| Candidate registration | /root/cross_candidate_consolidator | gpt-5.6-terra / medium | checkers/cross_source_consistency.md |
| Evidence recheck | /root/evidence_rechecker | gpt-5.6-sol / high | verification/evidence_recheck.md |
| Statistical pass 2 | /root/statistics_pass_2 | gpt-5.6-terra / high | checkers/statistical_pass_2.md |
| Evidence quality audit | /root/quality_control_auditor | gpt-5.6-sol / high | quality/evidence_quality_audit.md |
| Report generation | /root/report_generator | gpt-5.6-terra / medium | ../final_report_1_5_1.md |

The authoritative complete manifest, including each fresh-spawn start mode, is [agent_execution_manifest.md](review_1_5_1/agent_execution_manifest.md).

### Performance

- **Target basis:** Five direct-source PDFs totaling 263 pages, with reusable page-level text for 26 pages and 237 pages requiring fresh direct-source mapping; the package includes a 153-page protocol and an 83-page SAP with dense quantitative definitions, so the bounded target is scaled above the 102-page calibration while allowing concurrent disjoint mapping.
- **Total source units:** 263
- **Fresh-source units:** 237
- **Target elapsed minutes:** 80-120
- **Started UTC:** 2026-08-18T22:16:11Z
- **Finished UTC:** 2026-08-18T23:09:53Z
- **Observed elapsed minutes:** 53.7
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token-usage and cost metadata

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Runtime/API token counts | Token-only API-equivalent estimate |
|---|---|---|
| gpt-5.6-sol | UNAVAILABLE | UNAVAILABLE |
| gpt-5.6-terra | UNAVAILABLE | UNAVAILABLE |

The local versioned token summary is [token_usage_summary.md](review_1_5_1/token_usage_summary.md). The runtime exposed no authoritative response-level token counts for the coordinator or specialists, so each manifested agent is recorded as `UNAVAILABLE`; no usage is estimated from text. Cached-input/cache-write counts are input subsets and reasoning counts are output subsets, not additive totals. The known amount is a token-only API-equivalent estimate under the dated pricing snapshot, not an invoice.
